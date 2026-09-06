# -*- coding: utf-8 -*-
"""
द्विर्वचन — reduplication, and what happens to the copy afterwards.

    6.1.1   एकाचो द्वे प्रथमस्य      of the first one-vowelled part, two
    6.1.2   अजादेर्द्वितीयस्य         of a vowel-initial root, the second
    6.1.9   सन्यङोः                   after सन् and यङ्, the doubling happens
    7.4.59  ह्रस्वः                    the copy's vowel is shortened
    7.4.60  हलादिः शेषः               only its initial consonant remains
    7.4.66  उरत्                       an ऋ in the copy becomes अ
    7.4.82  गुणो यङ्लुकोः             an iK-final copy takes guṇa
    7.4.83  दीर्घोऽकितः                otherwise the copy's vowel lengthens
    7.4.90  रीगृदुपधस्य च             an ऋ-penult root gives the copy रीक्
    7.4.91  रुग्रिकौ च लुकि            and in the यङ्लुक्, रुक् and रिक् too

The first copy is the **अभ्यास** (abhyāsa), and it is the only part these
rules touch: 6.1.4 पूर्वोऽभ्यासः names it, and everything from 7.4.58 onward
is addressed to it. That is what makes reduplication different from the
operations already codified here — most rules read a form and substitute
inside it, while this one *builds a new term* and then rewrites that term
alone, leaving the original standing beside it.

Nothing in this module decides whether reduplication is called for. 6.1.9
says only that सन् and यङ् are two of the places it happens; the यङ् itself
is 3.1.22's, and the कर्मणि or लिट् cases are not codified.

**Scope.** The अभ्यासकार्य section runs 7.4.58 to 7.4.97 and ten of those
are here. Two kinds of root are outside it and both are known:

*Gutturals.* 7.4.62 कुहोश्चुः turns a क or ग in the copy into च or ज, and
it is not codified, so a guttural-initial root comes out with its own
consonant standing where the palatal should be.

*Roots needing work before the doubling.* अर्ति is admitted to यङ् by the
vārttika on 3.1.22 and gives अरार्यते, but getting there wants guṇa and
1.1.51's रपर on the root itself first, and the commentaries have not been
read for that ordering. अटि needs no such change and does work — अटाट्यते.

What the module is honest about is a consonant-initial root whose copy
needs no consonant change: every worked form of 3.1.22 that is not
guttural, and both of the stems 1.1.4 turns on.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

from src.chandas.core import scan_phonemes
from src.astadhyayi.adesa import guna_of, hrasva_of
from src.astadhyayi.sivasutra import resolve
from src.astadhyayi.svara import duration
from src.astadhyayi.varna import savarnas_of


@dataclass(frozen=True)
class Change:
    """One sūtra's work on the abhyāsa, and what it did."""

    by: str
    was: str
    now: str
    why: str


@dataclass(frozen=True)
class Doubled:
    """
    A stem split into its abhyāsa and the rest, with the record.

    `head` is what stands in FRONT of the copy, and it is empty for every
    consonant-initial root — which is all 3.1.22 admits before its vārttika,
    so the field looks idle until 6.1.2 turns up. अट् + यङ् is अटाट्यते: the
    अ stays where it is, ट्य doubles behind it, and the copy becomes टा. A
    split modelled as (abhyāsa, rest) has nowhere to keep that अ and drops
    it — the form came out ā.
    """

    abhyasa: str
    rest: str
    by: str
    why: str
    head: str = ""
    changes: Tuple[Change, ...] = ()

    @property
    def text(self) -> str:
        return self.head + self.abhyasa + self.rest


def _phonemes(text: str) -> List:
    return list(scan_phonemes(text))


def _vowel_positions(text: str) -> List[int]:
    return [i for i, p in enumerate(_phonemes(text)) if p.kind == "vowel"]


def is_ekac(stem: str) -> bool:
    """
    6.1.1's एकाच् — a form with exactly one vowel in it.

    Read as a bahuvrīhi, which the Kāśikā is explicit about: एकोऽच् यस्य
    सोऽयम् एकाच्, "that which has one vowel." Worth saying because 1.1.14
    reads the same word the other way — एकश्चासावच् च, a karmadhāraya, "it
    IS one vowel" — and `pragrhya._is_single_vowel` implements that reading.
    The two are different tests and neither can stand in for the other: प्र
    is एकाच् here and is not एकाच् there, which is exactly the difference
    the Kāśikā draws at 1.1.14 with प्राग्नये वाचमीरय.
    """
    return len(_vowel_positions(stem)) == 1


def is_haladi(stem: str) -> bool:
    """3.1.22's हलादि — the form begins with a consonant."""
    sounds = _phonemes(stem)
    return bool(sounds) and sounds[0].text in resolve("haL").sounds


def first_ekac(stem: str) -> Tuple[str, str]:
    """
    The opening one-vowelled portion, and what is left after it.

    6.1.1 प्रथमस्य. The portion runs from the start through the first vowel
    and on through any consonants that close it — but not through the
    consonant that opens the next syllable, which belongs to the vowel
    after it. मृज्य divides मृज् · य and not मृज्य् · अ, so the abhyāsa is
    मृज् and 7.4.60 has a ज् to drop.
    """
    sounds = _phonemes(stem)
    vowels = _vowel_positions(stem)
    if not vowels:
        return stem, ""
    if len(vowels) == 1:
        return stem, ""
    # up to, but not including, the consonant that begins the next syllable
    cut = vowels[1] - 1
    at = sounds[cut].start
    return stem[:at], stem[at:]


def second_ekac(stem: str) -> Tuple[str, str, str]:
    """
    6.1.2 अजादेर्द्वितीयस्य — for a vowel-initial root the SECOND portion
    doubles, not the first: अटिटिषति, अशिशिषति, अरिरिषति.

    Returns what precedes, the portion, and what follows.
    """
    sounds = _phonemes(stem)
    vowels = _vowel_positions(stem)
    if len(vowels) < 2:
        return "", stem, ""
    head = stem[:sounds[vowels[0] + 1].start] if vowels[0] + 1 < len(sounds) \
        else stem
    body, tail = first_ekac(stem[len(head):])
    return head, body, tail


def double(stem: str, *, after: str = "yaṅ") -> Doubled:
    """
    6.1.9 सन्यङोः — the doubling itself.

    धातोरनभ्यासस्य comes down from 6.1.8: it is a part of the *root* that
    doubles, and a part that is already an abhyāsa does not double again —
    जुगुप्सिषते, लोलूयिषते. `after` records which of the two affixes
    occasioned it, since 6.1.9 names both and this module is only used for
    one of them so far.
    """
    if _vowel_positions(stem) and not is_haladi(stem):
        head, body, tail = second_ekac(stem)
        return Doubled(
            body, body + tail, "6.1.2",
            "अजादेर्द्वितीयस्य — the root begins with a vowel, so it is the "
            "second one-vowelled portion that doubles and not the first: "
            "अटिटिषति, अशिशिषति, अरिरिषति. What precedes it stays where it "
            "is — the अ of अट् is not part of the copy",
            head=head,
        )
    body, tail = first_ekac(stem)
    return Doubled(
        body, body + tail, "6.1.9",
        f"सन्यङोः — after {after} the root's first one-vowelled part is "
        f"said twice: पापच्यते, यायज्यते, अटाट्यते. एकाचो द्वे प्रथमस्य is "
        f"read down from 6.1.1, and अनभ्यासस्य from 6.1.8 — a part that is "
        f"already an abhyāsa does not double again",
    )


def _is_r_varna(vowel: str) -> bool:
    """ऋवर्ण — ṛ and its savarṇas, which 1.1.9 decides."""
    return vowel in savarnas_of("ṛ")


def shape_abhyasa(
    abhyasa: str,
    *,
    rdupadha: bool = False,
    yan_luk: bool = False,
    augment: str = "rīk",
    kit: bool = False,
) -> Tuple[str, Tuple[Change, ...]]:
    """
    What the copy becomes — 7.4.59, 7.4.60, 7.4.66, 7.4.82, 7.4.83, and the
    ऋ-augments of 7.4.90 and 7.4.91.

    The order is the Kāśikā's own, and one step of it is stated outright at
    7.4.66: उः अदत्वे कृते रुगादय आगमाः क्रियन्ते — once अ has replaced the
    ऋ, *then* the रुक् / रिक् / रीक् augments are made. Reading it the other
    way round gives मृरी, and applying 1.1.51 उरण् रपरः to the अ gives मर्
    and then मर्री; the Kāśikā's own ववृते and शशृधे show the abhyāsa's ऋ
    going to a plain अ with no र् in it at all, and नर्नर्ति · नरिनर्ति ·
    नरीनर्ति show where the र् actually comes from — the three augments.

    `augment` chooses among them. In the यङ् proper only रीक् is available
    (7.4.90, before यङ् and यङ्लुक् alike); रुक् and रिक् are 7.4.91's and
    belong to the यङ्लुक् — नर्नर्ति, नरिनर्ति beside नरीनर्ति.
    """
    changes: List[Change] = []
    sounds = _phonemes(abhyasa)
    vowels = _vowel_positions(abhyasa)
    if not vowels:
        return abhyasa, ()

    # 7.4.60 हलादिः शेषः — the initial consonant, and nothing after the vowel.
    head = abhyasa[:sounds[vowels[0]].start]
    initial = head[:len(_phonemes(head)[0].text)] if head else ""
    vowel = sounds[vowels[0]].text
    kept = initial + vowel
    if kept != abhyasa:
        changes.append(Change(
            "7.4.60", abhyasa, kept,
            "हलादिः शेषः — अभ्यासस्य हलादिः शिष्यते, अनादिर्लुप्यते: of the "
            "copy the initial consonant stays and the rest go. पपाच, पपाठ",
        ))

    # 7.4.59 ह्रस्वः — and it is shortened.
    short = hrasva_of(vowel)
    if short is not None and short != vowel:
        was, kept = kept, initial + short
        vowel = short
        changes.append(Change(
            "7.4.59", was, kept,
            "ह्रस्वः — the copy's vowel is short: दुढौकिषते, तुत्रौकिषते",
        ))

    if _is_r_varna(vowel):
        # 7.4.66 उरत् — and an ऋ in it becomes अ.
        was, kept = kept, initial + "a"
        vowel = "a"
        changes.append(Change(
            "7.4.66", was, kept,
            "उरत् — ऋवर्णान्तस्य अभ्यासस्य अकारादेशः: ववृते, ववृधे, शशृधे. "
            "A plain अ, with no र् — the र् of नर्, नरि, नरी is the augment "
            "that comes next, not 1.1.51",
        ))
        if rdupadha:
            added = {"rīk": "rī", "rik": "ri", "ruk": "r"}.get(augment)
            if added is None:
                raise ValueError(
                    f"{augment!r} is not one of rīk, rik, ruk")
            if augment != "rīk" and not yan_luk:
                raise ValueError(
                    f"{augment} is 7.4.91's and belongs to the यङ्लुक्; "
                    f"in the यङ् proper only रीक् is available")
            by = "7.4.90" if augment == "rīk" else "7.4.91"
            why = (
                "रीगृदुपधस्य च — a root with ऋ for its penult gives the "
                "copy रीक्, before यङ् and यङ्लुक् alike: वरीवृत्यते, "
                "नरीनृत्यते. कित्, so 1.1.46 आद्यन्तौ टकितौ puts it at the "
                "end of the copy"
                if augment == "rīk" else
                "रुग्रिकौ च लुकि — in the यङ्लुक् the same copy may take "
                "रुक् or रिक् instead: नर्नर्ति, नरिनर्ति beside नरीनर्ति"
            )
            was, kept = kept, kept + added
            changes.append(Change(by, was, kept, why))
    else:
        if vowel in resolve("iK").sounds:
            # 7.4.82 गुणो यङ्लुकोः
            strengthened = guna_of(vowel)
            if strengthened is not None:
                was, kept = kept, initial + strengthened
                changes.append(Change(
                    "7.4.82", was, kept,
                    "गुणो यङ्लुकोः — इगन्तस्य अभ्यासस्य गुणः, in the यङ् and "
                    "the यङ्लुक् both: चेचीयते, लोलूयते, जोहवीति",
                ))
        elif not kit:
            # 7.4.83 दीर्घोऽकितः
            longer = [s for s in savarnas_of(vowel) if duration(s) == 2]
            if longer:
                was, kept = kept, initial + longer[0]
                changes.append(Change(
                    "7.4.83", was, kept,
                    "दीर्घोऽकितः — otherwise the copy's vowel is long: "
                    "पापच्यते, यायज्यते. अकितः इति किम्? यंयम्यते, रंरम्यते, "
                    "where a कित् augment has come in",
                ))

    return kept, tuple(changes)


def reduplicated(
    root: str,
    *,
    affix: str = "ya",
    after: str = "yaṅ",
    yan_luk: bool = False,
    augment: str = "rīk",
    kit: bool = False,
) -> Doubled:
    """
    The whole of it: double the root, then shape the copy.

    लू gives लोलूय and मृज् gives मरीमृज्य, which are the two stems 1.1.4
    is about. पच् gives पापच्य and यज् gives यायज्य, which are 3.1.22's own
    examples.

    `rdupadha` is not asked for — whether the root has ऋ for its penult is
    read off the root, since 7.4.90 says ऋदुपध and that is a fact about the
    letters. The vārttika widening it to ऋत्वत् — रीगृत्वत इति वक्तव्यम्,
    for वरीवृश्च्यते and परीपृच्छ्यते — is what the reading below actually
    implements, since it asks only whether an ऋ is in there.
    """
    stem = root + affix
    split = double(stem, after=after)
    rdupadha = any(_is_r_varna(p.text) for p in _phonemes(root)
                   if p.kind == "vowel")
    shaped, changes = shape_abhyasa(
        split.abhyasa, rdupadha=rdupadha, yan_luk=yan_luk,
        augment=augment, kit=kit,
    )
    return Doubled(shaped, split.rest, split.by, split.why,
                   head=split.head, changes=changes)


@dataclass(frozen=True)
class Applied:
    """The finished stem, and what one named sūtra of the run did to it."""

    text: str
    by: str
    acted: bool
    why: str
    abhyasa: str
    changes: Tuple[Change, ...] = ()


def for_sutra(sutra_id: str):
    """
    An entry point onto :func:`reduplicated` that answers for one sūtra.

    The stem is the work of several rules at once — लोलूय is 6.1.9, 7.4.59
    and 7.4.82 together — so there is no single rule to put in `by`. Each
    sūtra therefore gets its own way in, and says whether it was among the
    rules that acted and what it did. A reader on 7.4.59's page is asking
    about 7.4.59, not about whichever rule happened to run last.
    """

    def apply(
        root: str,
        affix: str = "ya",
        after: str = "yaṅ",
        yan_luk: bool = False,
        augment: str = "rīk",
        kit: bool = False,
    ) -> Applied:
        whole = reduplicated(root, affix=affix, after=after,
                             yan_luk=yan_luk, augment=augment, kit=kit)
        mine = [c for c in whole.changes if c.by == sutra_id]
        if mine:
            why = " ".join(c.why for c in mine)
        elif whole.by == sutra_id:
            why = whole.why
        elif sutra_id in ("6.1.1", "6.1.2", "6.1.9"):
            why = (f"{whole.by} is what split this stem; {sutra_id} did not "
                   f"reach it.")
        else:
            why = (f"{sutra_id} had no work on this copy — it came out "
                   f"{whole.abhyasa} without it.")
        acted = bool(mine) or whole.by == sutra_id
        return Applied(
            # Naming the sūtra that was asked about, whether or not it did
            # anything, makes a counter-example indistinguishable from a
            # worked one: 7.4.60 has no ज् to drop in लू, and saying it
            # fired there would teach the opposite of what the rule says.
            text=whole.text,
            by=sutra_id if acted else whole.by,
            acted=acted,
            why=why,
            abhyasa=whole.abhyasa,
            changes=whole.changes,
        )

    apply.__name__ = "rule_" + sutra_id.replace(".", "_")
    apply.__doc__ = (
        f"{sutra_id}, run over the whole reduplication so its effect can be "
        f"seen in a finished stem rather than on a fragment. Returns the "
        f"stem, whether this sūtra acted, and every rule that did."
    )
    return apply


__all__ = [
    "Applied", "Change", "Doubled", "double", "first_ekac", "for_sutra",
    "is_ekac", "is_haladi", "reduplicated", "second_ekac", "shape_abhyasa",
]
