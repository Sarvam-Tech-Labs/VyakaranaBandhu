# -*- coding: utf-8 -*-
"""
ग्रहण — what a sound named in a rule actually picks up.

Four sūtras compose to answer this, and they are stated in the order of a
default and its exceptions:

    1.1.68  स्वं रूपं शब्दस्याशब्दसंज्ञा   a word denotes its own form,
                                            unless it is a technical term
    1.1.69  अणुदित् सवर्णस्य चाप्रत्ययः     an aṆ, or a sound marked with u,
                                            also denotes its savarṇas —
                                            but not when it is an affix
    1.1.70  तपरस्तत्कालस्य                  a sound with t attached denotes
                                            only those of its own duration
    1.1.71  आदिरन्त्येन सहेता               an initial with a final it-marker
                                            denotes the run between them

Nothing here re-derives the pieces. The pratyāhāras come from
`sivasutra.resolve` (1.1.71, already codified), savarṇatva from `varna.savarna`
(1.1.9), and duration from the prosody engine's own vowel tables, so a syllable
weighs the same to the grammar as it does to the metre.

The result carries the sūtras that produced it. That is the point of the module
as much as the sound set is: a derivation should be able to say which rule
widened or narrowed a denotation, and the Kāśikā argues in exactly those terms
(अणिति नानुवर्तते — "aṆ does not carry over" — when it explains that 1.1.70
displaces 1.1.69 rather than adding to it).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, Optional, Tuple

from src.chandas.core import LONG_VOWELS, SHORT_VOWELS
from src.astadhyayi.sivasutra import PratyaharaError, resolve, resolve_all
from src.astadhyayi.varna import (
    ANTAHSTHA,
    SVARA,
    VARNAS,
    nasalize,
    savarnas_of,
)


@dataclass(frozen=True)
class Grahana:
    """What a term denotes, and which sūtras decided it."""

    term: str
    sounds: Tuple[str, ...]
    #: Sūtra ids, in the order they applied.
    by: Tuple[str, ...]
    note: str = ""

    def __contains__(self, sound: str) -> bool:
        return sound in self.sounds

    def __len__(self) -> int:
        return len(self.sounds)


# ---------------------------------------------------------------------------
# Duration, borrowed from the prosody engine
# ---------------------------------------------------------------------------

#: The pluta mark. 1.1.70 restricts by duration, and the tradition counts three:
#: hrasva, dīrgha, pluta. Pluta is written with a following 3 in the texts.
PLUTA_MARK = "3"


def kala(sound: str) -> Optional[int]:
    """
    Duration in mātrās, for 1.1.70's तत्कालस्य: 1 hrasva, 2 dīrgha, 3 pluta.

    Which is not this function's own notion to define. **1.2.27**
    ऊकालोऽज्झ्रस्वदीर्घप्लुतः is the sūtra that measures a vowel, and
    `svara.duration` is that sūtra — so 1.1.70 asks it rather than counting
    again. Consonants have no duration and give None.

    This did carry a second copy of the test, identical line for line, and
    the two were kept honest by a test asserting they agreed. That test
    could only ever fail after one had already been changed and something
    built on the difference; agreement checked from outside is not the same
    as there being one answer.
    """
    from src.astadhyayi.svara import duration

    return duration(sound)


# ---------------------------------------------------------------------------
# 1.1.69 — the varieties a mention sweeps up
# ---------------------------------------------------------------------------

#: Which sounds have an anunāsika counterpart at all. The Kāśikā on 1.1.9 counts
#: the sub-varieties: अन्तःस्था द्विप्रभेदाः, रेफवर्जिता यवलाः सानुनासिका
#: निरनुनासिकाश्च — the semivowels have two, y v l but not r — while र and the
#: ūṣmans have none. Vowels have them throughout (the eighteen kinds of a).
ADMITS_ANUNASIKA: FrozenSet[str] = SVARA | (ANTAHSTHA - {"r"})


def varieties(sound: str) -> Tuple[str, ...]:
    """
    A sound together with the forms that differ from it only in the ways
    savarṇatva disregards.

    The Kāśikā on 1.1.69 names the three: स्वरानुनासिक्यकालभिन्नस्य ग्रहणं
    भवति — accent, nasality and duration. Duration is already covered, because
    the savarṇa relation joins a with ā. Nasality is added here. Accent is not
    modelled anywhere in this project and so is not represented; that is a gap
    in the encoding rather than a claim about the grammar.
    """
    if sound not in ADMITS_ANUNASIKA:
        return (sound,)
    return (sound, nasalize(sound))


# ---------------------------------------------------------------------------
# Reading a term
# ---------------------------------------------------------------------------

_VOWELS: Tuple[str, ...] = tuple(
    sorted(set(LONG_VOWELS) | set(SHORT_VOWELS), key=len, reverse=True)
)


def tapara_of(term: str, *, leading: bool = True) -> Optional[str]:
    """
    The sound a tapara term is about, or None if the term is not tapara.

    The Kāśikā allows the word both ways — तः परो यस्मात् सोऽयं तपरः, तादपि
    परस्तपरः, "that from which a t follows, and also that which follows a t" —
    so both अत् and ता count.

    The two readings are not equally safe to apply blind. The trailing form
    cannot be mistaken for anything else. The leading form collides head-on
    with the udit convention: तु is the t-varga, not t-followed-by-u, and
    reading it the other way costs five consonants and gains a vowel.
    `leading=False` asks for the unambiguous reading only, which is what
    `grahana` uses before it has ruled udit out.
    """
    for vowel in _VOWELS:
        if term == vowel + "t":
            return vowel
    if leading:
        for vowel in _VOWELS:
            if term == "t" + vowel:
                return vowel
    return None


def udit_of(term: str) -> Optional[str]:
    """
    The sound an udit term is about — कु, चु, टु, तु, पु and the like.

    A consonant marked with the it-letter u stands for its whole varga, which
    1.1.69 delivers through savarṇatva since a varga is exactly a savarṇa class.
    The Kāśikā's example is चुटू at 1.3.7.
    """
    if len(term) >= 2 and term.endswith(("u", "U")):
        base = term[:-1]
        if base in VARNAS and not VARNAS[base].svara:
            return base
    return None


def is_pratyahara(term: str) -> bool:
    try:
        resolve(term)
    except (PratyaharaError, KeyError, ValueError):
        return False
    return True


# ---------------------------------------------------------------------------
# The composed rule
# ---------------------------------------------------------------------------

#: The aṆ of 1.1.69 is the longer of the two readings. The Kāśikā says so
#: outright — परेण णकारेण प्रत्याहारग्रहणम्, "the pratyāhāra is taken with the
#: later ṇ" — giving the vowels together with h y v r l rather than just a i u.
#: The semivowels are in it because y, v and l have anunāsika counterparts to
#: sweep up, which is precisely what the wider reading is for.
#:
#: The set is closed under savarṇatva. The śivasūtras enumerate only the hrasva
#: vowels, so a literal reading would leave ā outside aṆ and make a rule that
#: writes ā denote ā alone. The tradition takes the pratyāhāra to stand for
#: varṇas: अण् गृह्यमाणः ... सवर्णानां ग्राहको भवति, and the aṆ being taken up
#: is itself the varṇa. The system is self-consistent on this, and 1.1.1 is the
#: proof — if a bare ā did not already reach short a, the t of आत् would have
#: nothing to exclude, and the Kāśikā would not have had to explain it.
AN: FrozenSet[str] = frozenset(
    variety
    for member in max(resolve_all("aṆ"), key=lambda r: len(r.sounds)).sounds
    for variety in savarnas_of(member)
)



#: Terms that are śabda-saṃjñās, so that 1.1.68's exception clause bites. Filled
#: from the registry by `sources.register(..., samjna=...)`, so it lists exactly
#: the names this project has actually codified and grows as more are added.
#: Deriving it instead from every saṃjñā-type sūtra in the corpus was tried and
#: abandoned: taking each prathamā-ekavacana pada yields the saṃjñin alongside
#: the saṃjñā (1.1.1 gives आत्-ऐच् as well as वृद्धिः), and no mechanical test
#: separates them reliably.
_SAMJNAS: dict = {}


def register_samjna(name: str, sutra_id: str) -> None:
    _SAMJNAS[name] = sutra_id


def known_samjnas() -> Tuple[str, ...]:
    return tuple(sorted(_SAMJNAS))


def samjna_source(name: str) -> Optional[str]:
    """Which sūtra defines this technical term, if any."""
    return _SAMJNAS.get(name)


def grahana(term: str, *, pratyaya: bool = False) -> Grahana:
    """
    What `term` denotes when it appears in a rule.

    The order matters and is the order of the sūtras. 1.1.68 sets the default;
    1.1.71 unpacks a pratyāhāra; then 1.1.69 widens each member to its savarṇas
    unless the term is an affix; and 1.1.70 replaces that widening — not
    narrows it, the Kāśikā is careful to say अणिति नानुवर्तते — with one
    restricted to a single duration.

    `pratyaya=True` marks the term as an affix, for 1.1.69's अप्रत्ययः.
    """
    if term in _SAMJNAS:
        return Grahana(
            term=term,
            sounds=(),
            by=("1.1.68",),
            note=(
                f"अशब्दसंज्ञा — {term} is the saṃjñā defined at "
                f"{_SAMJNAS[term]}, so it denotes what it names and not its "
                f"own form. The sounds are whatever that sūtra assigns."
            ),
        )

    # 1.1.70 — tapara. Checked before 1.1.69 because it supersedes it; but only
    # in the unambiguous trailing reading, or तु would be read as t-plus-u
    # instead of as the t-varga. The leading reading is tried further down,
    # after udit has had its chance.
    vowel = tapara_of(term, leading=False)
    if vowel is None and udit_of(term) is None:
        vowel = tapara_of(term)
    if vowel is not None:
        target = kala(vowel)
        same_kala = tuple(
            variety
            for savarna_sound in savarnas_of(vowel)
            if kala(savarna_sound) == target
            for variety in varieties(savarna_sound)
        )
        return Grahana(
            term=term,
            sounds=same_kala,
            by=("1.1.68", "1.1.70"),
            note=(
                f"tapara: {vowel} and its savarṇas of {target} mātrā, with "
                f"other qualities free. अणिति नानुवर्तते — 1.1.69 does not "
                f"carry over here."
            ),
        )

    # 1.1.71 — a pratyāhāra unpacks first, then each member is read by 1.1.69.
    if is_pratyahara(term):
        members = resolve(term).sounds
        seen: dict = {}
        for member in members:
            for savarna_sound in (
                savarnas_of(member) if not pratyaya else (member,)
            ):
                for variety in varieties(savarna_sound):
                    seen.setdefault(variety, None)
        by = ("1.1.68", "1.1.71") + (() if pratyaya else ("1.1.69",))
        note = f"pratyāhāra over {len(members)} sounds"
        if pratyaya:
            note += "; अप्रत्ययः — no savarṇa-grahaṇa, it is an affix"
        return Grahana(term=term, sounds=tuple(seen), by=by, note=note)

    # 1.1.69 — udit stands for a varga, which is a savarṇa class.
    base = udit_of(term)
    if base is not None:
        return Grahana(
            term=term,
            sounds=savarnas_of(base),
            by=("1.1.68", "1.1.69"),
            note=f"udit: {base} with its savarṇas, i.e. the {base}-varga",
        )

    # 1.1.69 — a plain aṆ picks up its savarṇas, unless it is an affix.
    if term in VARNAS:
        if pratyaya:
            return Grahana(
                term=term,
                sounds=(term,),
                by=("1.1.68",),
                note="अप्रत्ययः — an affix denotes its own form only",
            )
        if term in AN:
            widened = tuple(
                variety
                for savarna_sound in savarnas_of(term)
                for variety in varieties(savarna_sound)
            )
            return Grahana(
                term=term,
                sounds=widened,
                by=("1.1.68", "1.1.69"),
                note="aṆ: own form and savarṇas",
            )
        return Grahana(
            term=term,
            sounds=varieties(term),
            by=("1.1.68",),
            note="not an aṆ and not udit: own form only",
        )

    return Grahana(term=term, sounds=(), by=(), note="not a recognised term")


# ---------------------------------------------------------------------------
# 1.1.72 येन विधिस्तदन्तस्य — the tadantavidhi
# ---------------------------------------------------------------------------


def tadanta(term: str, word: str) -> bool:
    """Does `word` end in `term`? Compared by sound, not by character."""
    from src.chandas.core import scan_phonemes

    term_sounds = [p.text for p in scan_phonemes(term)]
    word_sounds = [p.text for p in scan_phonemes(word)]
    return bool(term_sounds) and word_sounds[-len(term_sounds):] == term_sounds


def tadantavidhi(
    term: str, word: str, *, samasa_or_pratyaya_vidhi: bool = False
) -> bool:
    """
    1.1.72: a qualifier in a rule reaches whatever ENDS in it, and itself.

    येन विशेषणेन विधिर्विधीयते स तदन्तस्यात्मान्तस्य समुदायस्य ग्राहको भवति,
    स्वस्य च रूपस्य — the qualifier denotes the aggregate that ends in it, and
    its own form too. So 3.3.56 एरच्, which adds aC after an i, reaches चि and
    जि and gives चयः and जयः; 3.1.125 ओरावश्यके reaches a u-final and gives
    अवश्यलाव्यम्.

    This belongs beside 1.1.68 and not on its own: स्वम् and रूपम् are read
    down into it, which the corpus records. 1.1.68 says a word denotes its own
    form; this says it denotes what ends in that form as well.

    What the qualifier reaches is what it DENOTES and not the letters it is
    written with, so this composes with the rest of the block: the उ of 3.1.125
    is not tapara, 1.1.69 therefore gives it ū as well, and लू is reached.

    `samasa_or_pratyaya_vidhi` is Kātyāyana's exception —
    समासप्रत्ययविधौ प्रतिषेधः — which stops the extension in a rule about
    compounds or about affixes. Without it 2.1.24 would compound
    कष्टं परमश्रितः as well as कष्टश्रितः, and 4.1.99 would make सौत्रनाडिः
    from सूत्रनडस्य as well as नाडायनः from नडस्य.
    """
    if word == term:
        return True
    if samasa_or_pratyaya_vidhi:
        return False
    # The term denotes a class, not a string: 1.1.68 gives it its own form,
    # 1.1.69 adds the savarṇas, 1.1.70 narrows them by duration, 1.1.71 unpacks
    # a pratyāhāra. So 3.1.125 ओरावश्यके, whose उ is not tapara, reaches लू as
    # well as लु — and comparing the letters alone would miss it.
    denoted = grahana(term).sounds or (term,)
    return any(tadanta(sound, word) for sound in denoted)

__all__ = [
    "ADMITS_ANUNASIKA",
    "AN",
    "Grahana",
    "PLUTA_MARK",
    "grahana",
    "kala",
    "known_samjnas",
    "register_samjna",
    "samjna_source",
    "tadanta",
    "tadantavidhi",
    "tapara_of",
    "udit_of",
    "varieties",
]
