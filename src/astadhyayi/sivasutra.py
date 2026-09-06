# -*- coding: utf-8 -*-
"""
The Māheśvara-sūtras (Śivasūtras) and the pratyāhāra machinery.

This is the foundation the Aṣṭādhyāyī is written on: fourteen aphorisms listing
every sound of the language in a deliberate order, each closed by a marker
consonant (it / anubandha). A pratyāhāra is then formed by
A. 1.1.71 ādir antyena sahetā — "an initial [sound], together with a final
it-marker, [denotes itself and everything between]" — so `aiC` means "from the
sound ai up to the it-marker C", i.e. {ai, au}.

Nothing here is asserted from a book: every pratyāhāra is *derived* from the
fourteen sūtras by the rule, and the tests check the derivations against the
standard readings. That makes this layer independently verifiable, which is
why it is built first.

Two conventions worth stating:

* The śivasūtras cite consonants with an inherent `a` for pronounceability
  (ha, ya, va, ra). The sound denoted is the bare consonant, so each entry
  keeps both a display form and the phoneme it stands for; membership tests
  use the phoneme.
* The it-marker Ṇ occurs twice (sūtras 1 and 6), so `aṆ` is genuinely
  ambiguous — the tradition reads it as {a, i, u} in 1.1.69 and as the wider
  set elsewhere. `resolve` returns the nearest (first) reading, which is the
  primary one; `resolve_all` returns every reading so a caller that needs the
  wider set can ask for it. The ambiguity is reported, never silently picked.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


class PratyaharaError(ValueError):
    """Raised for a pratyāhāra that the fourteen sūtras cannot form."""


@dataclass(frozen=True)
class Sound:
    """One sound listed in a śivasūtra."""

    #: The phoneme as the rest of the engine writes it (IAST, no inherent a).
    phoneme: str
    #: How the sūtra itself cites it (ha, ya, va… with the inherent a).
    cited: str
    devanagari: str

    @property
    def is_vowel(self) -> bool:
        return self.phoneme in {"a", "i", "u", "ṛ", "ḷ", "e", "o", "ai", "au"}


@dataclass(frozen=True)
class Sivasutra:
    number: int
    sounds: Tuple[Sound, ...]
    #: The closing it-marker (anubandha), cited without its inherent a.
    it: str
    it_devanagari: str
    devanagari: str
    iast: str


def _s(phoneme: str, cited: str, devanagari: str) -> Sound:
    return Sound(phoneme=phoneme, cited=cited, devanagari=devanagari)


#: The fourteen Māheśvara-sūtras, in order.
SIVASUTRAS: Tuple[Sivasutra, ...] = (
    Sivasutra(
        1,
        (_s("a", "a", "अ"), _s("i", "i", "इ"), _s("u", "u", "उ")),
        "ṇ", "ण्", "अ इ उ ण्", "a i u Ṇ",
    ),
    Sivasutra(
        2,
        (_s("ṛ", "ṛ", "ऋ"), _s("ḷ", "ḷ", "ऌ")),
        "k", "क्", "ऋ ऌ क्", "ṛ ḷ K",
    ),
    Sivasutra(
        3,
        (_s("e", "e", "ए"), _s("o", "o", "ओ")),
        "ṅ", "ङ्", "ए ओ ङ्", "e o Ṅ",
    ),
    Sivasutra(
        4,
        (_s("ai", "ai", "ऐ"), _s("au", "au", "औ")),
        "c", "च्", "ऐ औ च्", "ai au C",
    ),
    Sivasutra(
        5,
        (_s("h", "ha", "ह"), _s("y", "ya", "य"), _s("v", "va", "व"), _s("r", "ra", "र")),
        "ṭ", "ट्", "ह य व र ट्", "ha ya va ra Ṭ",
    ),
    Sivasutra(
        6,
        (_s("l", "la", "ल"),),
        "ṇ", "ण्", "ल ण्", "la Ṇ",
    ),
    Sivasutra(
        7,
        (
            _s("ñ", "ña", "ञ"), _s("m", "ma", "म"), _s("ṅ", "ṅa", "ङ"),
            _s("ṇ", "ṇa", "ण"), _s("n", "na", "न"),
        ),
        "m", "म्", "ञ म ङ ण न म्", "ña ma ṅa ṇa na M",
    ),
    Sivasutra(
        8,
        (_s("jh", "jha", "झ"), _s("bh", "bha", "भ")),
        "ñ", "ञ्", "झ भ ञ्", "jha bha Ñ",
    ),
    Sivasutra(
        9,
        (_s("gh", "gha", "घ"), _s("ḍh", "ḍha", "ढ"), _s("dh", "dha", "ध")),
        "ṣ", "ष्", "घ ढ ध ष्", "gha ḍha dha Ṣ",
    ),
    Sivasutra(
        10,
        (
            _s("j", "ja", "ज"), _s("b", "ba", "ब"), _s("g", "ga", "ग"),
            _s("ḍ", "ḍa", "ड"), _s("d", "da", "द"),
        ),
        "ś", "श्", "ज ब ग ड द श्", "ja ba ga ḍa da Ś",
    ),
    Sivasutra(
        11,
        (
            _s("kh", "kha", "ख"), _s("ph", "pha", "फ"), _s("ch", "cha", "छ"),
            _s("ṭh", "ṭha", "ठ"), _s("th", "tha", "थ"), _s("c", "ca", "च"),
            _s("ṭ", "ṭa", "ट"), _s("t", "ta", "त"),
        ),
        "v", "व्", "ख फ छ ठ थ च ट त व्", "kha pha cha ṭha tha ca ṭa ta V",
    ),
    Sivasutra(
        12,
        (_s("k", "ka", "क"), _s("p", "pa", "प")),
        "y", "य्", "क प य्", "ka pa Y",
    ),
    Sivasutra(
        13,
        (_s("ś", "śa", "श"), _s("ṣ", "ṣa", "ष"), _s("s", "sa", "स")),
        "r", "र्", "श ष स र्", "śa ṣa sa R",
    ),
    Sivasutra(
        14,
        (_s("h", "ha", "ह"),),
        "l", "ल्", "ह ल्", "ha L",
    ),
)


@dataclass(frozen=True)
class _Slot:
    """A sound's position in the flattened śivasūtra sequence."""

    index: int
    sutra: int
    sound: Sound


def _flatten() -> List[_Slot]:
    slots: List[_Slot] = []
    for sutra in SIVASUTRAS:
        for sound in sutra.sounds:
            slots.append(_Slot(len(slots), sutra.number, sound))
    return slots


_SLOTS: List[_Slot] = _flatten()

#: All fifty-odd sounds in śivasūtra order, as phonemes.
SOUND_ORDER: Tuple[str, ...] = tuple(slot.sound.phoneme for slot in _SLOTS)


def _start_positions(initial: str) -> List[int]:
    """Every slot index whose sound could open a pratyāhāra named `initial`."""
    return [
        slot.index
        for slot in _SLOTS
        if slot.sound.phoneme == initial or slot.sound.cited == initial
    ]


def _end_positions(marker: str) -> List[int]:
    """
    Every slot index a pratyāhāra closed by `marker` may run up to — the last
    sound of each sūtra carrying that it-marker.
    """
    positions: List[int] = []
    cursor = 0
    for sutra in SIVASUTRAS:
        cursor += len(sutra.sounds)
        if sutra.it == marker:
            positions.append(cursor - 1)
    return positions


def split_pratyahara(name: str) -> Tuple[str, str]:
    """
    Splits a pratyāhāra into (initial sound, it-marker). The marker is the last
    character; the rest is the initial. Accepts `aiC`, `aic`, `ऐच्`-style IAST.
    """
    text = name.strip()
    if len(text) < 2:
        raise PratyaharaError(f"{name!r} is too short to be a pratyāhāra")
    return text[:-1].lower(), text[-1].lower()


@dataclass(frozen=True)
class Pratyahara:
    """One resolution of a pratyāhāra, with the derivation that produced it."""

    name: str
    initial: str
    it: str
    sounds: Tuple[str, ...]
    #: Which śivasūtra the initial sound was taken from, and which supplied
    #: the closing it-marker — the audit trail for the derivation.
    from_sutra: int
    to_sutra: int

    def __contains__(self, sound: str) -> bool:
        return sound in self.sounds

    def __len__(self) -> int:
        return len(self.sounds)


def resolve_all(name: str) -> List[Pratyahara]:
    """
    Every reading of a pratyāhāra permitted by 1.1.71, nearest first.

    More than one reading means the it-marker occurs in more than one
    śivasūtra (only Ṇ does, at sūtras 1 and 6). The tradition disambiguates
    from context; this returns the options rather than choosing silently.
    """
    initial, marker = split_pratyahara(name)
    starts = _start_positions(initial)
    if not starts:
        raise PratyaharaError(
            f"{name!r}: no śivasūtra lists a sound {initial!r} to open the pratyāhāra"
        )
    ends = _end_positions(marker)
    if not ends:
        raise PratyaharaError(
            f"{name!r}: {marker!r} is not an it-marker of any śivasūtra"
        )

    start = starts[0]  # the first occurrence: the standard reading
    readings: List[Pratyahara] = []
    for end in ends:
        if end < start:
            continue
        span = [slot for slot in _SLOTS[start:end + 1]]
        # `ha` is listed twice — in sūtra 5 for its own sake and in sūtra 14 so
        # that pratyāhāras closing in L (haL, jhaL, śaL, vaL) reach it. It is
        # one sound, so a span covering both keeps it once: that is why the
        # tradition counts 33 consonants and 42 varṇas, not 34 and 43.
        seen = set()
        phonemes = []
        for slot in span:
            if slot.sound.phoneme in seen:
                continue
            seen.add(slot.sound.phoneme)
            phonemes.append(slot.sound.phoneme)
        readings.append(
            Pratyahara(
                name=name,
                initial=initial,
                it=marker,
                sounds=tuple(phonemes),
                from_sutra=span[0].sutra,
                to_sutra=span[-1].sutra,
            )
        )
    if not readings:
        raise PratyaharaError(
            f"{name!r}: the it-marker {marker!r} precedes the initial {initial!r}"
        )
    return readings


def resolve(name: str) -> Pratyahara:
    """
    The primary reading of a pratyāhāra — nearest it-marker after the initial.

    This is the machinery of **1.1.71** आदिरन्त्येन सहेता: an initial sound,
    taken with a final it-marker, denotes itself and everything between.
    `form_pratyahara`, registered as that sūtra, is a one-line delegate to
    this function — so anything that calls `resolve` is running 1.1.71, and
    saying so here is what makes that visible to the reuse walk.

    Use `resolve_all` where the wider reading may be intended (aṆ is the only
    genuinely ambiguous case in the fourteen sūtras).
    """
    return resolve_all(name)[0]


def sounds(name: str) -> Tuple[str, ...]:
    """Shorthand: the phonemes a pratyāhāra denotes, primary reading."""
    return resolve(name).sounds


def is_ambiguous(name: str) -> bool:
    """True when 1.1.71 admits more than one reading of this pratyāhāra."""
    return len(resolve_all(name)) > 1


def denotes(name: str, sound: str) -> bool:
    """Membership test against the primary reading."""
    return sound in resolve(name).sounds
