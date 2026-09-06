# -*- coding: utf-8 -*-
"""
प्रगृह्य — the vowels that refuse sandhi. 1.1.11 to 1.1.19.

    1.1.11  ईदूदेद्द्विवचनं प्रगृह्यम्       a dual ending in ī, ū or e
    1.1.12  अदसो मात्                        those, in अदस्, after its m
    1.1.13  शे                                the Vedic substitute शे
    1.1.14  निपात एकाजनाङ्                   a one-vowel particle, but not आङ्
    1.1.15  ओत्                               a particle ending in o
    1.1.16  सम्बुद्धौ शाकल्यस्येतावनार्षे    a vocative o before इति, non-Vedic
    1.1.17  उञः                               the particle उञ्, before इति
    1.1.18  ऊँ                                and its substitute ऊँ
    1.1.19  ईदूतौ च सप्तम्यर्थे              ī and ū used for a locative

The name has one consequence and the whole block exists for it: 6.1.125
प्लुतप्रगृह्या अचि नित्यम् keeps a pragṛhya vowel unchanged before another
vowel. So अग्नी अत्र stays अग्नी अत्र where अग्नि अत्र would have become
अग्न्यत्र. This module says whether a form bears the name; nothing here applies
or blocks a sandhi, because none of these nine sūtras does either.

Two of them are optional and say so in an unusual way. 1.1.16 and 1.1.17 name
Śākalya, and both the Kāśikā and the tradition read the naming of an authority
as making the rule a विभाषा: शाकल्यग्रहणं विभाषार्थम्. So वायो इति and
वायविति are both correct, and `Pragrhya.optional` carries that.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from src.chandas.core import scan_phonemes
from src.astadhyayi.varna import ANUNASIKA_MARK


#: 1.1.11's three finals. The sūtra writes them tapara — ईत् ऊत् एत् — and the
#: Kāśikā says why: तपरकरणमसंदेहार्थम्, to remove doubt. By 1.1.70 that holds
#: the name to these lengths and keeps the pluta out.
IDUDED: Tuple[str, ...] = ("ī", "ū", "e")

#: 1.1.19's two. e is not among them, and the sūtra says ईदूतौ for that reason.
IDUT: Tuple[str, ...] = ("ī", "ū")

#: 1.1.18's form: a long, nasalised u. The Kāśikā describes it as
#: दीर्घोऽनुनासिकश्च — long and nasal — which is exactly ū with a candrabindu.
UM = "ū" + ANUNASIKA_MARK


@dataclass(frozen=True)
class Pragrhya:
    """That a form bears the name, which sūtra gave it, and whether optionally."""

    by: str
    why: str
    optional: bool = False


def _final_vowel(form: str) -> Optional[str]:
    phonemes = scan_phonemes(form)
    for phoneme in reversed(phonemes):
        if phoneme.kind == "vowel":
            return phoneme.text
    return None


def _is_single_vowel(form: str) -> bool:
    """
    1.1.14's एकाच्, read as the Kāśikā reads it: एकश्चासावच्चेत्येकाच्, "it is
    one and it is a vowel" — a karmadhāraya. So the particle must BE a single
    vowel, not merely contain one.

    The difference is the sūtra's own counter-example. प्र has one vowel and
    three sounds, and एकाजिति किम्? is answered with प्राग्नये वाचमीरय — the
    sandhi goes through, so प्र is not pragṛhya. Reading एकाच् as "having one
    vowel" would have made it so.
    """
    phonemes = scan_phonemes(form)
    return len(phonemes) == 1 and phonemes[0].kind == "vowel"


def pragrhya(
    form: str,
    *,
    dvivacana: bool = False,
    nipata: bool = False,
    ang: bool = False,
    sambuddhi: bool = False,
    before_iti: bool = False,
    arsa: bool = False,
    saptami_artha: bool = False,
    stem: str = "",
) -> Optional[Pragrhya]:
    """
    Whether this form is pragṛhya, and by which sūtra.

    The conditions are what the nine sūtras ask about and cannot be read off a
    string: whether the form is a dual, a particle, a vocative, whether आङ् is
    meant rather than a bare ā, whether इति follows, whether the passage is
    Vedic. Each is a parameter for that reason.

    The order is the order of the sūtras, and nothing here overrides anything
    else — the nine are alternatives, and a form reached by more than one is
    pragṛhya either way. The first that applies is reported.
    """
    final = _final_vowel(form)

    # 1.1.11 ईदूदेद्द्विवचनं प्रगृह्यम्
    if dvivacana and final in IDUDED:
        return Pragrhya(
            "1.1.11",
            f"a dual ending in {final}: अग्नी, वायू, माले, पचेते. "
            f"द्विवचनमिति किम्? कुमार्यत्र — ī alone is not enough; "
            f"ईदूदेदिति किम्? वृक्षावत्र — a dual in au is not this either",
        )

    # 1.1.12 अदसो मात्
    if stem == "adas" and final in IDUDED:
        return Pragrhya(
            "1.1.12",
            "the ī or ū of अदस् standing after its m: अमी अत्र, अमू अत्र. "
            "The Kāśikā notes एकारस्य नास्त्युदाहरणम् — for e there is no "
            "example, though the rule admits it",
        )

    # 1.1.13 शे
    if form == "śe":
        return Pragrhya(
            "1.1.13",
            "शे, the Vedic sup-substitute of 7.1.39: युष्मे, अस्मे, त्वे, मे. "
            "छान्दसम् — the Kāśikā has only this one Vedic example",
        )

    # 1.1.14 निपात एकाजनाङ्
    if nipata and _is_single_vowel(form) and not ang:
        return Pragrhya(
            "1.1.14",
            "a particle of a single vowel: अ अपेहि, इ इन्द्रं पश्य, उ उत्तिष्ठ. "
            "एकाजिति किम्? प्राग्नये वाचमीरय — प्र has one vowel but is not "
            "one, and its sandhi goes through. अनाङिति किम्? आ उदकान्तात् "
            "gives ओदकान्तात्; a bare ā is not excluded: आ एवं नु मन्यसे",
        )

    # 1.1.15 ओत्
    if nipata and final == "o":
        return Pragrhya(
            "1.1.15",
            "a particle ending in o: आहो, उताहो. निपात is read down from "
            "1.1.14, and the o carries तदन्तविधि — ending in o, not being o",
        )

    # 1.1.16 सम्बुद्धौ शाकल्यस्येतावनार्षे
    if sambuddhi and final == "o" and before_iti and not arsa:
        return Pragrhya(
            "1.1.16",
            "a vocative in o before इति, outside Vedic: वायो इति beside "
            "वायविति. शाकल्यग्रहणं विभाषार्थम् — naming Śākalya makes it a "
            "विभाषा, so both forms stand",
            optional=True,
        )

    # 1.1.17 उञः
    if form == "u" and before_iti and not arsa:
        return Pragrhya(
            "1.1.17",
            "the particle उञ् before इति: उ इति beside विति. Śākalya is read "
            "down from 1.1.16, so this too is optional",
            optional=True,
        )

    # 1.1.18 ऊँ
    if form == UM:
        return Pragrhya(
            "1.1.18",
            "ऊँ, the substitute for उञ् before इति — दीर्घोऽनुनासिकश्च, long "
            "and nasal. With 1.1.17 this makes त्रीणि रूपाणि: उ इति, विति, "
            "ऊँ इति",
            optional=True,
        )

    # 1.1.19 ईदूतौ च सप्तम्यर्थे
    if saptami_artha and final in IDUT:
        return Pragrhya(
            "1.1.19",
            "ī or ū standing for a locative: मामकी तनू for मामक्यां तन्वाम्, "
            "गौरी for गौर्याम्. ईदूताविति किम्? — e is not included here, "
            "which is why this sūtra says ईदूतौ and not ईदूदेत्",
        )
    return None


def is_pragrhya(form: str, **conditions) -> bool:
    return pragrhya(form, **conditions) is not None


def blocks_sandhi(form: str, **conditions) -> bool:
    """
    Whether a following vowel leaves this one alone.

    That is the whole point of the saṃjñā, but it is not this block's doing:
    6.1.125 प्लुतप्रगृह्या अचि नित्यम् is the rule that protects the vowel, and
    it is not codified yet. This function only says that the condition for it
    is met, and is named so that a caller cannot mistake it for the sandhi rule.
    """
    return is_pragrhya(form, **conditions)


__all__ = [
    "IDUDED",
    "IDUT",
    "Pragrhya",
    "UM",
    "blocks_sandhi",
    "is_pragrhya",
    "pragrhya",
]
