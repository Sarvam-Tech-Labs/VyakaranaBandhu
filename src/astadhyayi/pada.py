# -*- coding: utf-8 -*-
r"""
आत्मनेपद and परस्मैपद — which set of endings a verb takes. 1.3.12, 1.3.13.

    1.3.12  अनुदात्तङित आत्मनेपदम्   only a root marked anudātta, or ṅit
    1.3.13  भावकर्मणोः                and in the impersonal and the passive

1.3.12 is a नियम, a restriction and not a grant. The Kāśikā is explicit:
अविशेषेण धातोरात्मनेपदं परस्मैपदं च विधास्यते, तत्रायं नियमः क्रियते — both sets
are prescribed for a root without distinction, and THIS narrows it:
तेभ्य एवात्मनेपदं भवति नान्येभ्यः, from those alone and from no others.

This is where two earlier blocks meet. The mark is either the anudātta accent
of 1.2.30 or the ṅ of 1.3.3, and both are already codified — so the question
"does this root take ātmanepada?" is answered by reading the dhātupāṭha, not by
consulting a list. Of its 2,259 entries, 404 carry an anudātta **on the it** and
55 carry a ṅ; 458 in all, the two sets overlapping by one.

That emphasis is the whole of it. The dhātupāṭha accents roots and it-letters
with the same two signs, and only the one on the it is indicatory. आसँ॒ is
written `Asa~\` — the mark after the anunāsika it — and gives आस्ते; विँशँ is
`vi\Sa~`, the mark on the root's own vowel, and gives विशति, which is why
1.3.17 must grant निविशते its ātmanepada separately. Read without position the
two roots are identical and half the pāda has nothing left to do.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple

from functools import lru_cache

from src.astadhyayi.corpus import ANUDATTA, SVARITA, load_dhatupatha
from src.astadhyayi.itsamjna import DHATU, analyze


class Pada(Enum):
    """The two sets of personal endings."""

    ATMANEPADA = "ātmanepada"
    PARASMAIPADA = "parasmaipada"


@dataclass(frozen=True)
class PadaVerdict:
    """Which set, on what ground, and by which sūtra."""

    pada: Pada
    by: str
    why: str


# --- naming a root -------------------------------------------------------
#
# A sūtra names a root by its ordinary form — विशः, स्थः, नियः. The
# dhātupāṭha writes it in upadeśa, with its it-letters and, for some roots,
# an initial ष् or ण् that never surfaces. Two sūtras in the sixth adhyāya
# connect the two spellings, and both are needed here or six of the roots
# this pāda names would not be found at all:
#
#   6.1.64  धात्वादेः षः सः    ṣṭhā → sthā,  ṣmi → smi
#   6.1.65  णो नः              ṇīñ → nī,     ṇaśa → naś
#
# The it-stripping is 1.3.2–1.3.9's, already codified, so it is borrowed
# rather than repeated.

#: The corpus writes ñ before a stop as plain n — वञ्चु appears as `vancu`.
_NASAL_BEFORE_STOP = (("nc", "ñc"), ("nj", "ñj"))

#: 6.1.64 replaces the initial ष् with स्, and what follows a ष् is retroflex
#: only because the ष् was: ष्ठा is what स्था becomes. So the reversion runs
#: through the cluster — otherwise ष्ठा comes back as sṭhā and never matches
#: the स्थः of 1.3.22.
_UNRETROFLEX = {"ṭ": "t", "ṭh": "th", "ḍ": "d", "ḍh": "dh", "ṇ": "n"}


@lru_cache(maxsize=None)
def _upadesa_forms() -> frozenset:
    """Every form the dhātupāṭha actually enunciates."""
    return frozenset(e.upadesa for e in load_dhatupatha().values())


def _dhatvadeh(stem: str) -> str:
    """6.1.64 धात्वादेः षः सः and 6.1.65 णो नः, on the root's initial."""
    if stem.startswith("ṣ"):
        rest = stem[1:]
        for cluster in ("ṭh", "ḍh", "ṭ", "ḍ", "ṇ"):
            if rest.startswith(cluster):
                rest = _UNRETROFLEX[cluster] + rest[len(cluster):]
                break
        return "s" + rest
    if stem.startswith("ṇ"):
        return "n" + stem[1:]
    return stem


#: 8.2.18 कृपो रो लः turns the ṛ of कृप् into ḷ, so 1.3.93 names the root
#: कॢप् while the dhātupāṭha reads कृपू. Same species as 6.1.64: the sūtra uses
#: the shape the root wears, the file writes the shape it is taught in.
_AFTER_RULE = {"kḷp": "kṛp"}


def root_key(root: str) -> str:
    """
    A root reduced to the form a sūtra names it by.

    The it-rules run उपदेशे — in the enunciation — so they are applied only to
    a form the dhātupāṭha actually enunciates. Handing them a name that is
    already it-stripped would make 1.3.3 eat a real final: क्षिप् would come
    back as क्षि and मृष् as मृ, and neither sūtra would find its root.

    ḍukṛñ, kṛñ and kṛ all come back as `kṛ`; ṣṭhā as `sthā`; ṇīñ as `nī`.
    """
    root = root.strip()
    if root in _upadesa_forms():
        root = analyze(root, DHATU).stem     # 1.3.2–1.3.9
    root = _dhatvadeh(root)                  # 6.1.64, 6.1.65
    root = _AFTER_RULE.get(root, root)       # 8.2.18
    for written, meant in _NASAL_BEFORE_STOP:
        root = root.replace(written, meant)
    return root


@lru_cache(maxsize=None)
def _by_key() -> dict:
    """Every dhātupāṭha entry, gathered under the name a sūtra would use."""
    found: dict = {}
    for entry in load_dhatupatha().values():
        found.setdefault(root_key(entry.upadesa), []).append(entry)
    return found


def entries_for(root: str, *, artha: Optional[str] = None) -> tuple:
    """
    Every dhātupāṭha entry a sūtra's naming of this root reaches.

    A name usually reaches more than one, and 1.1.68 स्वं रूपम् is why: the
    sūtra's word denotes its own form, and every root so written answers to it.
    क्षिप् is read twice, in the fourth gaṇa and the sixth.

    That matters here because 174 of the 1,590 names carry *different marks* in
    different entries, and 1.3.12 and 1.3.72 turn on the marks. वह् is one:
    01.0720 वहि॒ (वृद्धौ) is anudāttet and 01.1159 वह॑ (प्रापणे) is svaritet, so
    the same name would take ātmanepada always by one reading and only by
    1.3.72 on the other. The commentaries settle it by citing the sense — the
    Kāśikā on 1.3.81 says «वह प्रापणे» स्वरितेत् — and `artha` is how a caller
    says the same thing. It matches against the dhātupāṭha's own gloss.
    """
    found = _by_key().get(root_key(root), ())

    # A caller who writes the whole upadeśa has already disambiguated, and
    # collapsing it to the bare name throws that away. डुपचँष् is one of
    # three entries called पच्, and it is the only svaritet among them —
    # asked as डुपचँष् the answer used to come back "anudāttet, 1.3.12,
    # ātmanepada", which is 01.0198 पचिँ speaking. पच् is ubhayapadī
    # precisely because *this* entry is svaritet and 1.3.72 makes the middle
    # conditional on कर्त्रभिप्राय.
    exact = tuple(e for e in found if e.upadesa == root)
    if exact:
        found = exact

    if artha is None:
        return tuple(found)
    return tuple(e for e in found if artha in (e.artha or ""))


def verbal_gana(root: str) -> frozenset:
    """
    Which classes of the dhātupāṭha this root is read in.

    The codes are the file's own — "02" for अदादि, "10" for चुरादि — and
    a name may answer to more than one: तन् is read in the eighth and
    the tenth both, so the answer is a set and never a single class.

    Rules that name a class ask this rather than carrying a list. A
    hand-copied गण would be a second statement of what the corpus
    already says, and would drift from it the first time the data is
    corrected.
    """
    return frozenset(e.code.split(".")[0] for e in entries_for(root))

def root_its(root: str) -> frozenset:
    """
    Every it-mark the dhātupāṭha writes on this root, across its entries.

    The marks are not read off the string here: 1.3.2 उपदेशेऽजनुनासिक
    इत् is what makes an anunāsika vowel an इत्, and it is codified, so
    `its_of` is asked. A second parser over the same upadeśas would be
    a second statement of that rule and would drift from it.

    A name answering to more than one entry gathers them all — शक् is
    read in the first gaṇa as शकि and in the fifth as शकॢ, so it is
    both इदित् and ऌदित् depending which is meant, and the union is
    what a rule naming the class has to see.
    """
    from src.astadhyayi.itsamjna import Context, its_of

    marks = set()
    for entry in entries_for(root):
        try:
            marks |= set(its_of(entry.upadesa, Context(dhatu=True)))
        except Exception:                   # noqa: BLE001 — odd upadeśa
            continue
    return frozenset(marks)



def marks_of(root: str) -> Tuple[Tuple[str, str, Tuple[str, ...]], ...]:
    """
    What each entry of this name is marked with — (code, artha, marks).

    Written for the reader rather than the resolver. Where a name is
    ambiguous this is what shows it, instead of a single boolean that quietly
    picks one entry.
    """
    out = []
    for entry in entries_for(root):
        marks = []
        if _entry_has(entry, ANUDATTA):
            marks.append("anudāttet")
        if _entry_has(entry, SVARITA):
            marks.append("svaritet")
        its = analyze(entry.upadesa, DHATU).it_letters
        if "ṅ" in its:
            marks.append("ṅit")
        if "ñ" in its:
            marks.append("ñit")
        out.append((entry.code, entry.artha or "", tuple(marks)))
    return tuple(out)


def _entry_has(entry, mark: str) -> bool:
    """Does this one entry carry the mark on an it-letter?"""
    spans = [(it.start, it.end) for it in analyze(entry.upadesa, DHATU).its]
    return any(
        found == mark and any(s < position <= e for s, e in spans)
        for position, found in entry.accent_positions
    )


def _accent_on_it(root: str, mark: str, artha: Optional[str] = None) -> bool:
    r"""
    Does an accent mark fall on one of the root's it-letters?

    This is the whole of 1.3.12's first condition and 1.3.72's, and it turns
    entirely on where the mark sits. The dhātupāṭha accents both roots and
    their it-letters with the same two signs, and only the one on the it is
    indicatory. In the file's own notation:

        Asa~\    the anudātta follows the anunāsika it   →  अनुदात्तेत्, आस्ते
        vi\Sa~   the anudātta is on the root's own vowel →  not it, विशति

    Reading the mark without its position makes those two roots identical, and
    then विशति comes out ātmanepada and 1.3.17 has nothing left to do.
    """
    return any(_entry_has(e, mark) for e in entries_for(root, artha=artha))


def is_anudattet(root: str, *, artha: Optional[str] = None) -> bool:
    """
    Is the root marked with an anudātta it — अनुदात्तेत्? 1.3.12's first ground.

    1.2.30 नीचैरनुदात्तः gives the accent its name; this asks whether the root's
    it carries it. 404 of the dhātupāṭha's 2,259 entries do.
    """
    return _accent_on_it(root, ANUDATTA, artha)


def is_svaritet(root: str, *, artha: Optional[str] = None) -> bool:
    """
    Is the root marked with a svarita it — स्वरितेत्? 1.3.72's first condition.

    The Kāśikā names four such roots while glossing this pāda, and all four
    are marked so in the file and only in the right position: क्षिप of the
    sixth gaṇa (1.3.80), वह (1.3.81), मृष (1.3.82) and युजिर् (1.3.64).
    """
    return _accent_on_it(root, SVARITA, artha)


def is_ngit(root: str, *, artha: Optional[str] = None) -> bool:
    """Is the root ṅit — marked with an indicatory ङ्? Read by 1.3.3."""
    return any(
        "ṅ" in analyze(entry.upadesa, DHATU).it_letters
        for entry in entries_for(root, artha=artha)
    ) or (artha is None and "ṅ" in analyze(root, DHATU).it_letters)


def is_nyit(root: str, *, artha: Optional[str] = None) -> bool:
    """
    Is the root ñit — marked with an indicatory ञ्? 1.3.72's second condition.

    Not the same mark as 1.3.12's ङ् and not interchangeable with it: डुक्रीञ्
    is ñit and takes ātmanepada only where the fruit reaches the agent, while
    शीङ् is ṅit and takes it always. Reading the two as one would collapse
    1.3.72 into 1.3.12.
    """
    return any(
        "ñ" in analyze(entry.upadesa, DHATU).it_letters
        for entry in entries_for(root, artha=artha)
    )


def pada_of(
    root: str, *, bhava_or_karman: bool = False, karmakartari: bool = False
) -> PadaVerdict:
    """
    Which endings this root takes.

    1.3.13 first, because it does not care what the root is marked with: in the
    impersonal and the passive the endings are ātmanepada whatever the root —
    भावे ग्लायते भवता, आस्यते भवता; कर्मणि क्रियते कटः, ह्रियते भारः.

    Then 1.3.12's restriction. आस् and वस् take it by their anudātta accent,
    giving आस्ते and वस्ते; षूङ् and शीङ् by their ṅ, giving सूते and शेते. A
    root with neither mark falls outside the restriction and takes parasmaipada.

    `karmakartari` is the Kāśikā's exception to 1.3.13 — लूयते केदारः
    स्वयमेवेति परस्मैपदं न भवति, where the object acts as its own agent. It
    notes that the second कर्तृग्रहण carries over, so parasmaipada is withheld
    there; passing the flag records that the case was considered.
    """
    if bhava_or_karman:
        return PadaVerdict(
            Pada.ATMANEPADA,
            "1.3.13",
            "भावकर्मणोः — in the impersonal or the passive the endings are "
            "ātmanepada whatever the root: ग्लायते भवता, क्रियते कटः"
            + (
                ". कर्मकर्तरि — लूयते केदारः स्वयमेव, where parasmaipada is "
                "still withheld"
                if karmakartari else ""
            ),
        )

    if is_anudattet(root):
        return PadaVerdict(
            Pada.ATMANEPADA,
            "1.3.12",
            f"अनुदात्तेत् — {root} is marked anudātta in the dhātupāṭha, so "
            f"the restriction admits it: आस्ते, वस्ते",
        )

    if is_ngit(root):
        return PadaVerdict(
            Pada.ATMANEPADA,
            "1.3.12",
            f"ङित् — {root} carries an indicatory ङ् by 1.3.3: सूते, शेते",
        )

    return PadaVerdict(
        Pada.PARASMAIPADA,
        "1.3.12",
        f"{root} is neither anudātta nor ṅit, and 1.3.12 is a नियम — "
        f"तेभ्य एवात्मनेपदं भवति नान्येभ्यः, from those alone. So the other "
        f"set stands.",
    )


def atmanepada_roots() -> "tuple":
    """
    Every root the restriction admits, read out of the dhātupāṭha.

    Not a list anyone typed: a root qualifies by carrying the accent 1.2.30
    names or the marker 1.3.3 finds, and both are in the file. Counted per
    entry rather than per name, because a name can be read twice with
    different marks — see `entries_for`.
    """
    found = []
    for entry in sorted(load_dhatupatha().values(), key=lambda e: e.code):
        its = analyze(entry.upadesa, DHATU).it_letters
        if _entry_has(entry, ANUDATTA) or "ṅ" in its:
            found.append(entry.upadesa.replace("̐", ""))
    return tuple(found)



__all__ = [
    "Pada",
    "PadaVerdict",
    "atmanepada_roots",
    "entries_for",
    "is_svaritet",
    "marks_of",
    "root_key",
    "is_anudattet",
    "is_ngit",
    "is_nyit",
    "pada_of",
]
