# -*- coding: utf-8 -*-
"""
The sūtras a step leans on, and what each contributed there.

Nearly every sandhi step rests on the same handful of rules of the first
adhyāya, and a step that names only its own sūtra leaves the reader to
reconstruct them:

    1.1.66  तस्मिन्निति निर्देशे पूर्वस्य   which SIDE of a vowel the change falls
    1.1.67  तस्मादित्युत्तरस्य              …and which side after an ablative
    1.1.50  स्थानेऽन्तरतमः                  which of several substitutes
    1.1.52  अलोऽन्त्यस्य                    how much of the sthānin goes
    1.1.54  आदेः परस्य                      the first sound of what follows
    1.1.55  अनेकाल्शित्सर्वस्य              the whole of a many-sound sthānin
    1.1.9   तुल्यास्यप्रयत्नं सवर्णम्        which sounds are alike
    1.1.69  अणुदित्सवर्णस्य चाप्रत्ययः      a letter stands for all its lengths
    1.1.70  तपरस्तत्कालस्य                 …but a t-marked one for its own length
    1.1.71  आदिरन्त्येन सहेता              what a pratyāhāra is
    1.3.10  यथासंख्यमनुदेशः समानाम्         equal lists correspond in order
    6.1.84  एकः पूर्वपरयोः                 one substitute for two sounds
    6.1.85  अन्तादिवच्च                     what that substitute counts as

Each function here returns a `Via` whose `role` says what the sūtra did in the
step at hand, not what it says in general — that is in the sūtra's own record.
Terms are written in IAST inside braces and printed in both scripts by the
trace.

**Class membership is derived.** `is_member("ī", "iK")` is true because 1.1.71
makes iK the four short sounds and 1.1.69 widens each to its savarṇas. Nothing
here lists the members.
"""

from __future__ import annotations

from functools import lru_cache
from typing import FrozenSet, Optional, Sequence, Tuple

from src.astadhyayi.adesa import antaratama as _antaratama
from src.astadhyayi.sandhi.rule import Via, sk
from src.astadhyayi.sandhi.segs import AC, base_of
from src.astadhyayi.sivasutra import resolve
from src.astadhyayi.varna import effort, savarna


# ---------------------------------------------------------------------------
# Membership of a pratyāhāra — 1.1.71, widened by 1.1.69
# ---------------------------------------------------------------------------


@lru_cache(maxsize=None)
def members(pratyahara: str) -> FrozenSet[str]:
    """
    Every sound `pratyahara` denotes.

    Its listed members are 1.1.71's business. For a pratyāhāra of vowels
    they are widened by 1.1.69 अणुदित्सवर्णस्य चाप्रत्ययः to the savarṇas of
    each — the ई of सुधी is an इक् though only the short इ is written — and the
    Tattvabodhinī says as much of iK: *तेन इक्शब्देन षट्षष्टिर्गृह्यन्ते*.
    """
    listed = resolve(pratyahara).sounds
    found = set(listed)
    vowels = [m for m in listed if m in AC]
    if vowels:
        found |= {v for v in AC if any(savarna(v, m) for m in vowels)}
    return frozenset(found)


def is_member(sound: str, pratyahara: str) -> bool:
    """Whether `sound` (nasal or not) is one of what the pratyāhāra denotes."""
    return base_of(sound) in members(pratyahara)


def long_form_used(sound: str, pratyahara: str) -> bool:
    """True where `sound` is in the pratyāhāra only by 1.1.69, not by being
    one of the sounds 1.1.71 lists — the reason to cite 1.1.69 in a step."""
    return (is_member(sound, pratyahara)
            and base_of(sound) not in resolve(pratyahara).sounds)


def nearest(sthanin: str, candidates: Sequence[str]) -> Optional[str]:
    """
    1.1.50 स्थानेऽन्तरतमः — the one substitute nearest the sthānin, or None.

    `adesa.antaratama` weighs place, then external quality, then length, and
    hands back every candidate tied at the top. Some ties are real and
    settled by the Kāśikā on internal effort: स् is ऊष्मन् (īṣadvivṛta) and so
    is श्, while छ् is स्पृष्ट — so स्→श् and not छ्, स्→ष् and not ठ्. The
    project's nearness model does not carry ābhyantara prayatna, so the
    tie is broken here, by `varna.effort`, and only when there is a tie.
    A tie still standing after that is reported as None and the rule does
    not fire, rather than one of two being taken silently.
    """
    tied = _antaratama(sthanin, candidates)
    if len(tied) > 1:
        same = tuple(c for c in tied if effort(c) is effort(sthanin))
        tied = same or tied
    return tied[0] if len(tied) == 1 else None


# ---------------------------------------------------------------------------
# The sūtras, as Vias
# ---------------------------------------------------------------------------


def saptami_purva(nimitta: str) -> Via:
    return Via(
        "1.1.66",
        f"the cause ({nimitta}) is named in the "
        f"seventh case, so the operation falls on the sound standing "
        f"immediately BEFORE it")


def pancami_para(nimitta: str) -> Via:
    return Via(
        "1.1.67",
        f"the cause ({nimitta}) is named in the fifth "
        f"case, so the operation falls on what stands immediately AFTER it")


def antaratama(sthanin: str, adesa: str, among: str) -> Via:
    return Via(
        "1.1.50",
        f"of the sounds {among} could put in place of "
        f"{sk(sthanin)}, {sk(adesa)} is the nearest in place and effort")


def alo_antyasya(sthanin: str) -> Via:
    return Via(
        "1.1.52",
        f"the sthānin {sk(sthanin)} is named in the sixth case, so "
        f"the substitute takes the place of its last sound only")


def adeh_parasya(sthanin: str) -> Via:
    return Via(
        "1.1.54",
        f"what is laid down for what follows replaces its "
        f"FIRST sound; here {sk(sthanin)}")


def sarvasya(sthanin: str) -> Via:
    return Via(
        "1.1.55",
        f"the substitute has more than one sound (or is "
        f"marked श्), so it replaces the whole of {sk(sthanin)}, not just its last "
        f"sound")


def savarna_of(first: str, second: str) -> Via:
    return Via(
        "1.1.9",
        f"{sk(first)} and {sk(second)} share place and "
        f"internal effort, so each is savarṇa to the other")


def varna_grahana(sound: str, pratyahara: str) -> Via:
    return Via(
        "1.1.69",
        f"a sound named without a त् stands for "
        f"all its savarṇas, so {sk(sound)} is {{{pratyahara}}} though only the "
        f"short letter is written in the śivasūtras")


def tapara(sound: str) -> Via:
    return Via(
        "1.1.70",
        f"the sound is written with a following त्, so it "
        f"names only sounds of its own length: {sk(sound)}")


def pratyahara(name: str, sounds: str) -> Via:
    return Via(
        "1.1.71",
        f"{{{name}}} is the first letter with the last, "
        f"and stands for {sk(sounds)}")


def yathasamkhya(first: str, second: str) -> Via:
    return Via(
        "1.3.10",
        f"the two lists are of equal length, so "
        f"they correspond in order: {sk(first)} takes {sk(second)}")


def ekadesa_one_for_two() -> Via:
    return Via(
        "6.1.84",
        "the substitute stands for the earlier sound AND the "
        "later one together, not for each separately")


def antadivat() -> Via:
    return Via(
        "6.1.85",
        "that single substitute counts as the last sound of the "
        "first word and the first sound of the second")


def samhita_condition() -> Via:
    return Via(
        "1.4.109",
        "the sounds are spoken with no pause between "
        "them; if they were spoken apart none of these rules would apply")


def avasana_condition() -> Via:
    return Via(
        "1.4.110",
        "the word is followed by a pause, which is the "
        "condition the rule names")


def it_removed(letters: str) -> Tuple[Via, ...]:
    """1.3.2 and 1.3.9: an इत् marked in the upadeśa is then lost, which is
    how a substitute like रु is left as र्."""
    return (
        Via("1.3.2", f"the nasalised {sk(letters)} of the "
                     f"enunciation is an इत्"),
        Via("1.3.9", f"and the इत् {sk(letters)} is then lost"),
    )


__all__ = [
    "adeh_parasya", "alo_antyasya", "antadivat", "antaratama",
    "avasana_condition", "ekadesa_one_for_two", "is_member", "it_removed",
    "long_form_used", "members", "nearest", "pancami_para", "pratyahara",
    "samhita_condition", "saptami_purva", "sarvasya", "savarna_of", "tapara",
    "varna_grahana", "yathasamkhya",
]
