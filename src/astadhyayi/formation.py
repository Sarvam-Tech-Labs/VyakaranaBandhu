# -*- coding: utf-8 -*-
"""
What two blocks of provisions have in common.

1.2.1–1.2.26 and 1.3.14–1.3.93 are built the same way. Each is a run of sūtras
that assigns some property to a form under conditions on the root, the affix
and the sense; each has prohibitions cancelling earlier members; each has
options of two kinds. Writing that twice would be writing it twice, so the
parts that are genuinely general live here:

  * how a sūtra number orders against another;
  * what happens when an अप्राप्तविभाषा meets an invariable rule;
  * how a gaṇa named by its first member is read out of the dhātupāṭha;
  * the shape predicates — असंयोगान्त, इगन्त, रलन्त, झलादि, and the rest —
    which are not opinions about anything but questions about sounds.

The shape predicates are the substantial part. Every one of them is a
pratyāhāra applied to a position in the root, and both the pratyāhāras and the
positions are already codified: `sivasutra.resolve` builds the first by 1.1.71,
and `adesa.antya` and `adesa.upadha` locate the second by 1.1.52 and 1.1.65.
Nothing here re-derives either.
"""

from __future__ import annotations

from functools import lru_cache
from typing import List, Optional, Sequence, Tuple

from src.astadhyayi.adesa import antya, upadha
from src.astadhyayi.corpus import load_dhatupatha, load_ganapatha
from src.astadhyayi.pada import root_key
from src.astadhyayi.sivasutra import resolve
from src.astadhyayi.varna import SVARA


# --- reading a gaṇa out of the dhātupāṭha ---------------------------------


@lru_cache(maxsize=None)
def gana_run(first: str, last: str) -> Tuple[str, ...]:
    """
    The roots the dhātupāṭha reads between two of its entries, inclusive.

    A gaṇa named by its first member — कुटादि, द्युतादि, वृतादि — is not a list
    anywhere in the Aṣṭādhyāyī. It is a stretch of another text, and the
    commentaries fix its two ends. So it is read off the file between them
    rather than transcribed, and the ends are what the tests check.
    """
    entries = load_dhatupatha()
    codes = sorted(code for code in entries if first <= code <= last)
    return tuple(dict.fromkeys(root_key(entries[code].upadesa) for code in codes))


# --- the shape of a root ---------------------------------------------------


@lru_cache(maxsize=None)
@lru_cache(maxsize=None)
def gana_items(sutra_id: str, name_starts: str) -> Tuple[str, ...]:
    """
    One gaṇa, by the sūtra that calls it up and the start of its name.

    Both parts are needed: 2.1.59 calls up two gaṇas, श्रेण्यादि and कृतादि,
    so the sūtra alone does not identify one. The name is matched on its
    start because the gaṇapāṭha writes them with the -ādi already attached.
    """
    for gana in load_ganapatha().get(sutra_id, ()):
        if gana.name.startswith(name_starts):
            return tuple(gana.items)
    return ()


def _sounds(pratyahara: str) -> frozenset:
    return frozenset(resolve(pratyahara).sounds)


def _phonemes(text: str) -> List[str]:
    """
    The sounds of a form, aspirates kept whole.

    `bhid` is bh-i-d and not b-h-i-d, which matters wherever a rule asks after
    the last sound or the one before it.
    """
    out: List[str] = []
    index = 0
    while index < len(text):
        two = text[index:index + 2]
        if len(two) == 2 and two[1] == "h" and two[0] not in SVARA:
            out.append(two)
            index += 2
        else:
            out.append(text[index])
            index += 1
    return out


def ends_in(root: str, pratyahara: str) -> bool:
    """Does the root's last sound fall in this pratyāhāra? इगन्त, रलन्त, हलन्त."""
    last = antya(root_key(root))
    return bool(last) and last in _sounds(pratyahara)


def penult_in(root: str, pratyahara: str) -> bool:
    """Does the root's उपधा fall in this pratyāhāra? 1.1.65 defines the place."""
    before = upadha(root_key(root))
    return bool(before) and before in _sounds(pratyahara)


def penult_is(root: str, *sounds: str) -> bool:
    """Is the उपधा one of these sounds? उदुपध, नोपध, व्युपध."""
    return upadha(root_key(root)) in sounds


def begins_with(form: str, pratyahara: str) -> bool:
    """Does the form's first sound fall in this pratyāhāra? झलादि, हलादि."""
    first = _phonemes(form)[:1]
    return bool(first) and first[0] in _sounds(pratyahara)


def is_asamyoganta(root: str) -> bool:
    """
    Does the root end in something other than a conjunct? 1.2.5's condition.

    The Kāśikā's counter-examples are सस्रंसे and दध्वंसे, whose roots स्रंस्
    and ध्वंस् end in two consonants. भिद् and छिद् end in one, and ईज् in one
    after a vowel.

    The nasal of those two is written `n` in this dhātupāṭha — `sransu̐`,
    `dhvansu̐`, the same convention that writes वञ्चु as `vancu`. An anusvāra
    spelling is admitted too, since a reader is as likely to type स्रंस् as
    स्रन्स्; it is not in the śivasūtras and so not in हल्, but it is plainly a
    consonant for the purpose of 1.1.7 हलोऽनन्तराः संयोगः.
    """
    sounds = _phonemes(root_key(root))
    consonants = _sounds("haL") | {"ṃ", "ṁ", "ḥ"}
    return not (len(sounds) >= 2
                and sounds[-1] in consonants and sounds[-2] in consonants)


def ik_before_final_consonant(root: str) -> bool:
    """
    इगन्तात् इक्समीपात् हलः — 1.2.10's condition, and 1.2.11's.

    The Kāśikā reads अन्त as समीपवचन, 'near', so हलन्त means a consonant next
    to an इक्: भिद् and बुध् qualify, यज् does not because its अ is not an इक्.
    """
    sounds = _phonemes(root_key(root))
    return (len(sounds) >= 2
            and sounds[-1] in _sounds("haL")
            and sounds[-2] in _sounds("iK"))


# --- resolving between provisions -----------------------------------------


def order_of(sutra: str) -> Tuple[int, ...]:
    """Sūtra order, so a later provision can be recognised as later."""
    digits = []
    current = ""
    for character in sutra:
        if character.isdigit():
            current += character
        elif current:
            digits.append(int(current))
            current = ""
    if current:
        digits.append(int(current))
    return tuple(digits)


def drop_aprapta(candidates: Sequence) -> List:
    """
    अप्राप्तविभाषा — an option over what was not otherwise obtained.

    Where such an option and an invariable rule both reach the same form, the
    option has nothing to do and the invariable rule stands. The commentaries
    name the two kinds apart in so many words — अप्राप्तविभाषेयम् at 1.3.43,
    प्राप्तविभाषेयम् at 1.3.50 — and only the first yields.
    """
    if any(not p.optional for p in candidates):
        return [p for p in candidates if not p.aprapta]
    return list(candidates)


__all__ = [
    "begins_with",
    "drop_aprapta",
    "ends_in",
    "gana_run",
    "ik_before_final_consonant",
    "is_asamyoganta",
    "order_of",
    "penult_in",
    "penult_is",
]
