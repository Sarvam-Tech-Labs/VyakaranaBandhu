# -*- coding: utf-8 -*-
"""
व्युत्पत्ति (vyutpatti) — from the finished word back to the root it comes from.

Every rule in this codification runs one way. 3.1.68 कर्तरि शप् (kartari
śap) puts an affix after a root; nothing in the Aṣṭādhyāyī takes an affix
off a word. Pāṇini's grammar is a machine for **making** forms, and it has
no reverse gear — asking it "what is जयति (jayati) from?" is asking a
question it was not written to answer.

So the answer is not found by running rules backwards. It is found the only
way the grammar allows: **make every word the grammar can make, and see
which making produced this one.** The Kāśikā uses exactly this reasoning
when it wants to say what a word comes from — at 8.2.59 भित्तं शकलम्
(bhittaṃ śakalam) it says भिदिक्रिया शब्दव्युत्पत्तेर् एव निमित्तम्, "the
act of splitting is only the word's व्युत्पत्ति" — the root is where the
word *would be derived from*, established by pointing at the derivation
and not by taking the word apart.

**What the search is over.** The dhātupāṭha on disk, ~2,000 roots as
enunciated, is the whole list of things a verb can be made from. For each
one the engine in `prakriya.py` is run, and the results are matched. That
is why the answer comes back as a *set*: जयति (jayati) is derivable from
01.0642 जि जये (ji, jaye — "to win") and from 01.1096 जि अभिभवे (ji,
abhibhave — "to overcome"), two entries the dhātupāṭha spells identically
and separates only by sense. The grammar does not choose between them, and
neither does this. Only the sentence can.

**The class must be in reach, and all ten now are.** A root of the sixth
class takes श (śa) by 3.1.77 तुदादिभ्यः शः and not शप् (śap); deriving
तुद् (tud) with शप् would give तोदति (todati), which is not a word, and a
search matching against invented forms answers with invented roots. So a
class whose विकरण (vikaraṇa) the engine cannot apply is left out — and the
list of those is not written here. It is read off the engine's own rules,
which is why `unreachable()` is empty today and was eight entries long
before 3.1.69, 3.1.73, 3.1.77, 3.1.78, 3.1.79, 3.1.81, 3.1.25 and 2.4.75
were wired. See `IN_REACH`.

**The opening sound survives, with two exceptions the filter knows about.**
In लट् (laṭ) with no preverb there is no augment, so the first sound of the
word is the first sound of the root — after 6.1.64/65 धात्वादेः
(dhātvādeḥ) have turned an initial ष् (ṣ) into स् (s) and an initial ण्
(ṇ) into न् (n), which is why नयति (nayati) has to be looked for under न्
(n) though its root is written णीञ् (ṇīñ). The two exceptions:

  * a root of the **third class** is heard through its copy — 6.1.10's
    doubling and then 7.4.62 कुहोश्चुः and 8.4.54 अभ्यासे चर् च, so हु
    (hu) is जुहोति (juhoti) and belongs under ज् (j);
  * a root beginning with a **vowel** can surface on a semivowel — 6.1.77
    इको यणचि gives इण् (iṇ) both एति (eti) and यन्ति (yanti) — so a query
    beginning with य् व् र् or ल् searches the vowels as well.

None of that is assumed. `tests/test_astadhyayi_vyutpatti.py` derives every
form in reach and checks that the root that made it is among the candidates
the filter would have tried.

**What the answer means, exactly.** "जयति (jayati) is derivable from जि
(ji) **by the rules the engine has**, and here is the derivation." Not "and
by no other", and not "and every Sanskrit verb is answered". The forward
engine applies fifty-three operational rules out of 3,983 codified, so the
failure mode is a word it cannot build and therefore cannot recognise:
गच्छति (gacchati) gets no answer, because 7.3.77 इषुगमियमां छः is codified
but not wired, and the engine makes गमति (gamati) from गम् (gam) instead. Every such gap is a
**silence**, never a wrong root — and the derivation comes back with the
answer so that a reader can see precisely which rules were used.

**What this is not.** It is not a morphological analyser for running text.
It answers for finite verbs of लट् (laṭ), with no preverb, from every class
of the dhātupāṭha. `unreachable()` states any class the engine cannot build
— none, today — and `owed_for` the slots it still withholds.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, FrozenSet, List, Optional, Tuple

from src.astadhyayi.anga import (
    abhyase_car, adiprabhrtibhyah_sapah, dhatvadeh, kuhos_cuh)
from src.astadhyayi.corpus import Dhatu, load_dhatupatha
from src.astadhyayi.itsamjna import DHATU, analyze
from src.astadhyayi.prakriya import Prakriya, derive
from src.astadhyayi.prakriya_rules import all_rules, verb
from src.astadhyayi.vibhakti import NUMBERS, PERSONS
from src.astadhyayi.vibhaktau import before_ending
from src.astadhyayi.vikarana import CLASS_MARKERS, marker_of_class
from src.chandas.core import scan_phonemes
from src.normalizer import devanagari_to_iast, is_devanagari


#: The gaṇasūtras sit in the dhātupāṭha file as rows whose root column is a
#: single hyphen — their text lives in the companion ganasutras file. They
#: are not roots and nothing can be derived from them.
NOT_A_ROOT = "-"

#: लट् (laṭ) has nine person-number slots, and `verb` indexes them the way
#: 1.4.101 तिङस्त्रीणि त्रीणि does: प्रथम (prathama) first, then मध्यम
#: (madhyama), then उत्तम (uttama), each in three numbers. The European
#: "third person" is Pāṇini's first, which is why these are numbers here
#: and named only where a caller reads them. The names come from
#: `vibhakti`, which is where the ending tables they index live.
SLOTS: Tuple[Tuple[int, int], ...] = tuple(
    (person, number) for person in range(3) for number in range(3)
)


# ---------------------------------------------------------------------------
# Which classes the engine can actually build
# ---------------------------------------------------------------------------


@lru_cache(maxsize=1)
def _engine_sutras() -> FrozenSet[str]:
    """Every sūtra the forward engine has an operational rule for."""
    return frozenset(rule.sutra for rule in all_rules())


@lru_cache(maxsize=1)
def _in_reach() -> FrozenSet[str]:
    return frozenset(
        code for code, (_marker, sutra) in CLASS_MARKERS.items()
        if sutra in _engine_sutras()
    )


#: The classes the search covers, read off the engine at import rather than
#: listed. Two today — 01 भ्वादि (bhvādi) and 02 अदादि (adādi).
IN_REACH: FrozenSet[str] = _in_reach()


def in_reach(code: str) -> bool:
    """
    Whether a dhātupāṭha class is one the forward engine can build.

    The class takes a विकरण (vikaraṇa) and the engine either has a rule for
    that विकरण or it does not. Nothing about the answer is written down
    here — `vikarana.CLASS_MARKERS` says which sūtra each class turns on
    and `all_rules()` says which sūtras the engine applies, and this is the
    overlap. Wire 3.1.77 तुदादिभ्यः शः into the engine and the sixth class
    becomes reachable with no edit to this file.
    """
    return code in _in_reach()


def unreachable() -> Tuple[Tuple[str, str, str], ...]:
    """
    The classes the search cannot cover, each with what it would need.

    Returned as (class code, the marker, the sūtra that gives it) so that a
    caller can say *why* a word was not recognised rather than only that it
    was not: तुदति (tudati) is not unknown, it is out of reach, and 3.1.77
    is the reason.
    """
    return tuple(
        (code, gives, sutra)
        for code, (gives, sutra) in sorted(CLASS_MARKERS.items())
        if not in_reach(code)
    )


def owed_for(upadesa: str, ending: str, pada: str) -> Optional[Tuple[str, str]]:
    """
    A rule that must act on this ending and that the engine cannot apply.

    A class being in reach is not enough — one slot of a paradigm can owe a
    rule the other eight do not. 7.2.81 आतो ङितः (āto ṅitaḥ) is the one this
    engine still owes: the आ (ā) of आताम् (ātām) and आथाम् (āthām) becomes
    इय् (iy) after an अ-final stem, and with 6.1.66 लोपो व्योर्वलि and 6.1.87
    आद्गुणः behind it that is what makes पचेते (pacete) and एधेते (edhete).
    Without those three the engine gets as far as एधाते (edhāte), which is
    not a word — so the slot is withheld rather than answered wrongly.

    All three conditions the sūtra states are asked, not assumed:

      * the ending must begin with आ — पचन्ते (pacante) has no आ, and the
        Kāśikā's आत इति किम्? cites exactly that;
      * it must be ङित् — which by 1.2.4 सार्वधातुकमपित् every आत्मनेपद
        सार्वधातुक ending is, and पचावहै (pacāvahai) is not, ङित इति किम्?;
      * the stem must end in अ — which it does only while शप् (śap) stands,
        so the second class is untouched and आसाते (āsāte) and शयाते
        (śayāte) come out right and are not withheld. 2.4.72 is asked for
        that, the same function the engine itself asks.

    Returns (what the rule would do, which rule) or None. Wire 7.2.81 in and
    this returns None on its own.
    """
    if pada != "ātmanepada" or not ending.startswith("ā"):
        return None
    if adiprabhrtibhyah_sapah(upadesa).elided:
        return None
    shaped = before_ending(part="ā-of-ṅit", gana="a-anta",
                           before="sārvadhātuka")
    sutra = getattr(shaped, "sutra", "")
    if sutra and sutra not in _engine_sutras():
        return (shaped.does, sutra)
    return None


# ---------------------------------------------------------------------------
# The opening sound, which the derivation does not change
# ---------------------------------------------------------------------------


#: Every vowel-initial root goes in one bucket. गुण (guṇa) by 7.3.84 and
#: 6.1.78 एचोऽयवायावः both act on a root's own vowel, so a vowel-initial
#: root's opening is the one thing a लट् derivation can move.
VOWEL_BUCKET = "V"


def opening(text: str) -> str:
    """
    The bucket a form is filed under — its first sound, vowels lumped.

    Aspirates count as one sound, which `scan_phonemes` already knows: भू
    (bhū) opens on भ् (bh) and not on ब् (b).
    """
    sounds = scan_phonemes(text) if text else []
    if not sounds:
        return ""
    return VOWEL_BUCKET if sounds[0].kind == "vowel" else sounds[0].text


def root_opening(upadesa: str, gana: str = "") -> str:
    """
    The bucket a *root* is filed under, read through the rules that can
    change its opening before anything else does.

    1.3.9 तस्य लोपः first, because डुकृञ् (ḍukṛñ) opens on ड् (ḍ) only
    until 1.3.5 आदिर्ञिटुडवः has been applied to it; then 6.1.64/65
    धात्वादेः (dhātvādeḥ), because णीञ् (ṇīñ) is filed under न् (n).
    Neither is guessed at: both are codified and both are asked.

    **And the third class opens on its copy.** 2.4.75's श्लु doubles the
    root by 6.1.10, and the sound one hears first is the अभ्यास's, after
    7.4.62 कुहोश्चुः and 8.4.54 अभ्यासे चर् च have worked on it: हु (hu)
    gives जुहोति (juhoti) and belongs under ज् (j), not ह् (h). Without
    this the search asked the wrong bucket and found nothing at all for
    twenty-six roots.
    """
    stem = analyze(upadesa, DHATU).stem
    changed = dhatvadeh(stem)
    settled = changed.result if changed.changed else stem
    if gana == "03":
        for shape in (kuhos_cuh, abhyase_car):
            made = shape(settled)
            if made.result is not None:
                settled = made.result
    return opening(settled)


# ---------------------------------------------------------------------------
# The search space
# ---------------------------------------------------------------------------


@lru_cache(maxsize=1)
def searchable() -> Tuple[Dhatu, ...]:
    """Every dhātupāṭha entry the forward engine can make a verb from."""
    return tuple(
        entry for entry in load_dhatupatha().values()
        if entry.upadesa != NOT_A_ROOT and in_reach(entry.code.split(".")[0])
    )


@lru_cache(maxsize=None)
def _by_opening(bucket: str) -> Tuple[Dhatu, ...]:
    return tuple(entry for entry in searchable()
                 if root_opening(entry.upadesa,
                                 entry.code.split(".")[0]) == bucket)


#: 6.1.77 इको यणचि turns इ into य्, उ into व्, ऋ into र् and ऌ into ल्,
#: and 6.1.78 एचोऽयवायावः gives य् and व् too. So a root that opens on a
#: vowel can surface opening on one of these four — इण् (iṇ) gives एति
#: (eti) in the singular and **यन्ति** (yanti) in the plural — and a word
#: that begins with one has to be looked for in the vowel bucket as well
#: as its own. Nothing runs the other way: no rule here takes a root's
#: opening consonant off, so a word beginning with a vowel never comes
#: from a root that does not.
FROM_A_VOWEL: Tuple[str, ...] = ("y", "v", "r", "l")


def candidates(word: str) -> Tuple[Dhatu, ...]:
    """
    The roots worth trying for this word — those that open on its sound.

    A filter and not an answer: every root here is *tried*, and most fail.
    What matters is that no root outside it could have succeeded, which is
    the claim the tests check exhaustively, over every form in reach.
    """
    key = opening(iast(word))
    found = _by_opening(key)
    if key in FROM_A_VOWEL:
        found = found + _by_opening(VOWEL_BUCKET)
    return found


# ---------------------------------------------------------------------------
# Forward, once per root, remembered
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Made:
    """One form the engine made, and the derivation that made it."""

    surface: str
    person: int
    number: int
    pada: str
    prakriya: Prakriya


@lru_cache(maxsize=None)
def paradigm(upadesa: str, gana: str = "") -> Tuple[Made, ...]:
    """
    All nine लट् (laṭ) forms of one root, as the engine derives them.

    The class is passed and not looked up. जि (ji) is spelt the same at
    01.0642 and 10.0324, and the two take different विकरण (vikaraṇa) —
    शप् (śap) by 3.1.68 for the first, णिच् (ṇic) by 3.1.25 for the tenth,
    जयति (jayati) against जापयति (jāpayati). Only the dhātupāṭha's code
    tells them apart.

    Which endings — and so whether the root is परस्मैपद (parasmaipada) or
    आत्मनेपद (ātmanepada) — is not decided here. `verb` reads it off the
    root's accent through 1.3.12 अनुदात्तङित आत्मनेपदम् (anudāttaṅita
    ātmanepadam), which is why एध (edha) comes back एधते (edhate) and not
    एधति (edhati).

    A derivation that did not converge is dropped rather than matched. The
    engine says so itself — `Prakriya.stopped` — and a form it could not
    finish is not a form the grammar makes.
    """
    rules = all_rules()
    made: List[Made] = []
    for person, number in SLOTS:
        start = verb(upadesa, person=person, number=number, gana=gana)
        pada = ("ātmanepada" if "ātmanepada" in start.terms[-1].samjnas
                else "parasmaipada")
        if owed_for(upadesa, start.terms[-1].text, pada):
            continue
        done = derive(start, rules)
        if done.stopped != "no rule applies":
            continue
        made.append(Made(surface=done.surface, person=person,
                         number=number, pada=pada, prakriya=done))
    return tuple(made)


# ---------------------------------------------------------------------------
# The answer
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Vyutpatti:
    """One way the word could have been made, with the making."""

    word: str
    #: The root as the dhātupāṭha enunciates it — डुपचँष् (ḍupacaṣ), marks
    #: and all, because that is what the grammar operates on.
    upadesa: str
    #: What is left of it after 1.3.9 तस्य लोपः — पच् (pac).
    dhatu: str
    code: str
    gana: int
    artha: str
    person: int
    number: int
    pada: str
    prakriya: Prakriya

    @property
    def person_name(self) -> str:
        return PERSONS[self.person]

    @property
    def number_name(self) -> str:
        return NUMBERS[self.number]

    @property
    def marker(self) -> Optional[Tuple[str, str]]:
        """The class-marker this root's class takes, and by which sūtra."""
        return marker_of_class(self.code.split(".")[0])

    def trace(self) -> str:
        return self.prakriya.trace()


def iast(word: str) -> str:
    """A word in either script, as IAST. जयति and jayati are one query."""
    return devanagari_to_iast(word) if is_devanagari(word) else word


def roots_of(word: str) -> Tuple[Vyutpatti, ...]:
    """
    Every root the grammar could have made this word from.

        roots_of("जयति")   →  01.0642 जि जये, 01.1096 जि अभिभवे
        roots_of("nayati") →  01.1049 णीञ् प्रापणे

    Empty is not "no such word". It is "no root in reach makes it", and
    `unreachable()` says what is out of reach and why. Order is the
    dhātupāṭha's, so the answers come back in the order a reader of the
    root-list would meet them.
    """
    wanted = iast(word)
    found: List[Vyutpatti] = []
    for entry in candidates(wanted):
        for made in paradigm(entry.upadesa, entry.code.split(".")[0]):
            if made.surface != wanted:
                continue
            found.append(Vyutpatti(
                word=wanted,
                upadesa=entry.upadesa,
                dhatu=analyze(entry.upadesa, DHATU).stem,
                code=entry.code,
                gana=entry.gana,
                artha=entry.artha,
                person=made.person,
                number=made.number,
                pada=made.pada,
                prakriya=made.prakriya,
            ))
    return tuple(found)


def forms_of(upadesa: str, gana: str = "") -> Dict[Tuple[int, int], str]:
    """The nine forms of a root, keyed by (person, number). The way in."""
    return {(made.person, made.number): made.surface
            for made in paradigm(upadesa, gana)}


__all__ = [
    "IN_REACH", "NOT_A_ROOT", "NUMBERS", "PERSONS", "SLOTS",
    "FROM_A_VOWEL", "VOWEL_BUCKET", "Made", "Vyutpatti",
    "candidates", "forms_of",
    "iast", "in_reach", "opening", "owed_for", "paradigm",
    "root_opening",
    "roots_of", "searchable", "unreachable",
]


# ---------------------------------------------------------------------------
# Both directions, from the command line
# ---------------------------------------------------------------------------


def _both_scripts(text: str) -> str:
    from src.normalizer import iast_to_devanagari

    return iast_to_devanagari(text) + " (" + text + ")"


def _show_roots(word: str) -> None:
    """The reverse question: a word, and every root that could make it."""
    asked = iast(word)
    found = roots_of(asked)
    if not found:
        print(_both_scripts(asked) + " — no root in reach makes it.")
        for code, gives, sutra in unreachable():
            print("    gaṇa " + code + " is out of reach: " + sutra
                  + " gives it " + gives)
        return
    print(_both_scripts(asked) + " — " + str(len(found)) + " derivation(s)")
    for one in found:
        print("")
        print("  " + one.code + "  " + _both_scripts(one.dhatu)
              + "  from " + _both_scripts(one.upadesa)
              + "  — " + one.artha)
        print("  " + one.person_name + " " + one.number_name
              + ", " + one.pada)
        print("")
        print(one.trace())


def _show_forms(upadesa: str) -> bool:
    """
    The forward question: a root as enunciated, and its nine forms.

    Only a root the dhātupāṭha actually reads. Without that check every
    word was taken for a root and जयति (jayati) was conjugated as though
    it were one, giving जयतयति (jayatayati) — the engine will happily
    make a verb of anything, and the corpus is what says what is one.
    """
    entry = next((one for one in searchable()
                  if one.upadesa == upadesa), None)
    if entry is None:
        return False
    made = forms_of(upadesa, entry.code.split(".")[0])
    if not made:
        return False
    print(_both_scripts(upadesa) + " — लट् (laṭ)")
    for (person, number), form in sorted(made.items()):
        print("  " + PERSONS[person].ljust(9) + " "
              + NUMBERS[number].ljust(11) + " " + _both_scripts(form))
    return True


def main(argv: Optional[List[str]] = None) -> int:
    """
    Both directions, told apart by what is given.

        python -m src.astadhyayi.vyutpatti ji        → जयति and its eight
        python -m src.astadhyayi.vyutpatti जयति      → जि, with the making

    A root is recognised by being in the dhātupāṭha; anything else is
    treated as a word and traced back.
    """
    import sys

    words = list(argv if argv is not None else sys.argv[1:]) or ["jayati"]
    for word in words:
        if not _show_forms(iast(word)):
            _show_roots(word)
        print("")
    return 0


if __name__ == "__main__":       # pragma: no cover
    raise SystemExit(main())
