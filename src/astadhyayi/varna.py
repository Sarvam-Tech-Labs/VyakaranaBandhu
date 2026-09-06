# -*- coding: utf-8 -*-
"""
The varṇa layer — sthāna (place), prayatna (effort), and savarṇatva.

This is the phonetic substrate several saṃjñās stand on. 1.1.9 defines savarṇa
in terms of place and effort; 1.1.10 restricts it; 1.1.8 defines anunāsika by
place; 1.1.7 defines saṃyoga over consonants; and 1.1.50 sthāne'ntaratamaḥ will
need "nearest" measured in exactly these features. Writing the features once,
here, is what keeps those sūtras from each growing a private copy.

Everything that CAN be derived, is. The Laghusiddhāntakaumudī does not give the
categories as lists — it gives them as pratyāhāras:

    खरो विवाराः श्वासा अघोषाश्च          khaR  → vivāra, śvāsa, aghoṣa
    हशः संवारा नादा घोषाश्च              haŚ   → saṃvāra, nāda, ghoṣa
    यणोऽन्तःस्थाः                        yaṆ   → antaḥstha
    शल ऊष्माणः                           śaL   → ūṣman
    अचः स्वराः                           aC    → svara
    वर्गाणां प्रथमतृतीयपञ्चमा यणश्चाल्पप्राणाः
    वर्गाणां द्वितीयचतुर्थौ शलश्च महाप्राणाः

so this module resolves those pratyāhāras through 1.1.71 rather than typing the
members out. The śivasūtras are therefore load-bearing for the phonetics too: a
fault there surfaces here, which is the intent.

Only two things are stated as primary data, because no rule derives them — the
varga arrangement of the stops, and the Śikṣā verse assigning places. Both are
quoted at the point of use.

Sources, all local:
  reference/mula/ancillary/gretil-laghusiddhantakaumudi.txt  (the Śikṣā verse
      and the prayatna definitions, quoted below verbatim)
  reference/commentary/kashika.json  at 1.1.9
  reference/mula/mahabhasya/         at 1.1.9, Kielhorn I.61-63
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Dict, FrozenSet, Optional, Tuple

from src.astadhyayi.sivasutra import resolve


# ---------------------------------------------------------------------------
# Feature vocabulary
# ---------------------------------------------------------------------------


class Place(Enum):
    """
    One articulator. The Śikṣā names six and adds the tongue-root for the
    jihvāmūlīya: कण्ठ, तालु, मूर्धा, दन्ताः, ओष्ठौ, नासिका.

    These are the components. A sthāna such as कण्ठतालु is two of them at once,
    and keeping the parts separate is what lets 1.1.50 say that i is nearer to
    e than to a — e shares तालु with it, a shares nothing.
    """

    KANTHA = "kaṇṭha"
    TALU = "tālu"
    MURDHAN = "mūrdhan"
    DANTA = "danta"
    OSTHA = "oṣṭha"
    NASIKA = "nāsikā"
    JIHVAMULA = "jihvāmūla"


class Sthana(Enum):
    """आस्य — the place in the mouth. The Śikṣā verse, quoted in the Kaumudī."""

    KANTHYA = "kaṇṭhya"
    TALAVYA = "tālavya"
    MURDHANYA = "mūrdhanya"
    DANTYA = "dantya"
    OSTHYA = "oṣṭhya"
    KANTHATALAVYA = "kaṇṭhatālavya"
    KANTHOSTHYA = "kaṇṭhoṣṭhya"
    DANTOSTHYA = "dantoṣṭhya"
    JIHVAMULIYA = "jihvāmūlīya"
    NASIKYA = "nāsikya"


#: Which articulators each sthāna uses. The Śikṣā's own names carry this — a
#: कण्ठतालव्य sound is made at कण्ठ and तालु together — so the mapping is a
#: reading of the compound rather than a further claim, and a test checks each
#: entry against the name it belongs to.
PLACES: Dict["Sthana", FrozenSet[Place]] = {}


class Abhyantara(Enum):
    """
    आभ्यन्तर प्रयत्न — internal effort. `ādyaḥ pañcadhā`: fivefold.

    The Kaumudī counts five. The Kāśikā on 1.1.9 says only four are *resorted
    to* in the savarṇa-saṃjñā — स्पृष्टता, ईषत्स्पृष्टता, संवृतता, विवृतता —
    omitting īṣadvivṛta, which folds the ūṣmans in with the vowels.

    The two accounts do NOT agree on every pair, and the difference is exactly
    what 1.1.10 is for. The Kāśikā's own examples on 1.1.10 are अवर्णहकारौ
    (daṇḍahastaḥ) and इवर्णशकारौ (dadhiśītam): a with h, i with ś. Those pairs
    share a place, and they share an effort only if īṣadvivṛta has collapsed
    into vivṛta. Under the fourfold reading 1.1.10 must block them; under the
    fivefold reading the effort has already parted them and 1.1.10 sits idle on
    these pairs. Both schemes are therefore kept — see `savarna(scheme=...)` —
    so the sūtra can be shown doing work rather than assumed to.
    """

    SPRSTA = "spṛṣṭa"
    ISATSPRSTA = "īṣatspṛṣṭa"
    ISADVIVRTA = "īṣadvivṛta"
    VIVRTA = "vivṛta"
    SAMVRTA = "saṃvṛta"


class Bahya(Enum):
    """बाह्य प्रयत्न — external effort. Deliberately not a savarṇa criterion."""

    VIVARA = "vivāra"
    SAMVARA = "saṃvāra"
    SVASA = "śvāsa"
    NADA = "nāda"
    GHOSA = "ghoṣa"
    AGHOSA = "aghoṣa"
    ALPAPRANA = "alpaprāṇa"
    MAHAPRANA = "mahāprāṇa"


# ---------------------------------------------------------------------------
# Primary data — the two things no rule derives
# ---------------------------------------------------------------------------

PLACES.update({
    Sthana.KANTHYA: frozenset({Place.KANTHA}),
    Sthana.TALAVYA: frozenset({Place.TALU}),
    Sthana.MURDHANYA: frozenset({Place.MURDHAN}),
    Sthana.DANTYA: frozenset({Place.DANTA}),
    Sthana.OSTHYA: frozenset({Place.OSTHA}),
    Sthana.KANTHATALAVYA: frozenset({Place.KANTHA, Place.TALU}),
    Sthana.KANTHOSTHYA: frozenset({Place.KANTHA, Place.OSTHA}),
    Sthana.DANTOSTHYA: frozenset({Place.DANTA, Place.OSTHA}),
    Sthana.JIHVAMULIYA: frozenset({Place.JIHVAMULA}),
    Sthana.NASIKYA: frozenset({Place.NASIKA}),
})


#: The varga arrangement. This is the alphabet's own order, not a pratyāhāra:
#: कादयो मावसानाः स्पर्शाः — "the sparśas run from ka and end with ma."
VARGA: Dict[str, Tuple[str, ...]] = {
    "ku": ("k", "kh", "g", "gh", "ṅ"),
    "cu": ("c", "ch", "j", "jh", "ñ"),
    "ṭu": ("ṭ", "ṭh", "ḍ", "ḍh", "ṇ"),
    "tu": ("t", "th", "d", "dh", "n"),
    "pu": ("p", "ph", "b", "bh", "m"),
}

#: A vowel letter in the Śikṣā stands for its whole varṇa — every length. The
#: Kāśikā on 1.1.9 notes ऌवर्णस्य दीर्घा न सन्ति, that ḷ has no long form; ḹ is
#: carried anyway so the inventory round-trips with src/phonetics.py, and the
#: fact is recorded rather than silently applied.
VOWEL_VARNA: Dict[str, Tuple[str, ...]] = {
    "a": ("a", "ā"),
    "i": ("i", "ī"),
    "u": ("u", "ū"),
    "ṛ": ("ṛ", "ṝ"),
    "ḷ": ("ḷ", "ḹ"),
    "e": ("e",),
    "ai": ("ai",),
    "o": ("o",),
    "au": ("au",),
}

#: Symbols for the visarga's positional variants, matching src/chandas/core.py
#: so the two engines name the same sounds the same way.
JIHVAMULIYA = "ẖ"
UPADHMANIYA = "ḫ"
ANUSVARA = "ṃ"
VISARGA = "ḥ"

#: Combining candrabindu — the anunāsika mark, as src/chandas/core.py writes it
#: in "m̐". A vowel or semivowel carrying it is uttered through the nose as
#: well as the mouth, which is exactly what 1.1.8 asks for.
ANUNASIKA_MARK = "̐"

#: The Śikṣā verse, as data. Each row is one quarter, kept beside the sounds it
#: places so the assignment can be checked against the line it came from.
SIKSA_STHANA: Tuple[Tuple[str, Tuple[str, ...], Sthana], ...] = (
    ("akuhavisarjanīyānāṃ kaṇṭhaḥ", ("a", "ku", "h", VISARGA), Sthana.KANTHYA),
    ("icuyaśānāṃ tālu", ("i", "cu", "y", "ś"), Sthana.TALAVYA),
    ("ṛṭuraṣāṇāṃ mūrdhā", ("ṛ", "ṭu", "r", "ṣ"), Sthana.MURDHANYA),
    ("ḷtulasānāṃ dantāḥ", ("ḷ", "tu", "l", "s"), Sthana.DANTYA),
    ("upūpadhmānīyānām oṣṭhau", ("u", "pu", UPADHMANIYA), Sthana.OSTHYA),
    ("edaitoḥ kaṇṭhatālu", ("e", "ai"), Sthana.KANTHATALAVYA),
    ("odautoḥ kaṇṭhoṣṭham", ("o", "au"), Sthana.KANTHOSTHYA),
    ("vakārasya dantoṣṭham", ("v",), Sthana.DANTOSTHYA),
    ("jihvāmūlīyasya jihvāmūlam", (JIHVAMULIYA,), Sthana.JIHVAMULIYA),
    ("nāsikānusvārasya", (ANUSVARA,), Sthana.NASIKYA),
)


def _expand(token: str) -> Tuple[str, ...]:
    """A Śikṣā token: a varga name, a vowel standing for its varṇa, or a sound."""
    if token in VARGA:
        return VARGA[token]
    if token in VOWEL_VARNA:
        return VOWEL_VARNA[token]
    return (token,)


# ---------------------------------------------------------------------------
# Derived categories — every one of these is a pratyāhāra in the Kaumudī
# ---------------------------------------------------------------------------

SVARA: FrozenSet[str] = frozenset(                      # अचः स्वराः
    s for v in resolve("aC").sounds for s in VOWEL_VARNA.get(v, (v,))
)
ANTAHSTHA: FrozenSet[str] = frozenset(resolve("yaṆ").sounds)   # यणोऽन्तःस्थाः
USMAN: FrozenSet[str] = frozenset(resolve("śaL").sounds)       # शल ऊष्माणः
SPARSA: FrozenSet[str] = frozenset(s for g in VARGA.values() for s in g)

#: खरो विवाराः श्वासा अघोषाश्च / हशः संवारा नादा घोषाश्च
_KHAR: FrozenSet[str] = frozenset(resolve("khaR").sounds)
_HAS: FrozenSet[str] = frozenset(resolve("haŚ").sounds)

#: वर्गाणां प्रथमतृतीयपञ्चमा यणश्चाल्पप्राणाः — 1st, 3rd, 5th of each varga, plus yaṆ.
#: वर्गाणां द्वितीयचतुर्थौ शलश्च महाप्राणाः — 2nd and 4th, plus śaL.
ALPAPRANA: FrozenSet[str] = frozenset(
    [g[i] for g in VARGA.values() for i in (0, 2, 4)]
) | ANTAHSTHA
MAHAPRANA: FrozenSet[str] = frozenset(
    [g[i] for g in VARGA.values() for i in (1, 3)]
) | USMAN

#: The nasals. ञमङणनानां नासिका च — "and the nose", in addition to their own
#: place, which is why nasality is a separate flag and not a Sthana here.
ANUNASIKA_STOPS: Tuple[str, ...] = tuple(g[4] for g in VARGA.values())


# ---------------------------------------------------------------------------
# The inventory
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Varna:
    """One sound, with the features 1.1.9 and 1.1.50 need."""

    sound: str
    sthana: Sthana
    abhyantara: Abhyantara
    bahya: FrozenSet[Bahya]
    svara: bool
    mukha: bool         # uttered through the mouth
    nasika: bool        # uttered through the nose
    siksa: str          # the verse quarter that placed it

    @property
    def places(self) -> FrozenSet[Place]:
        """The articulators this sound uses, for 1.1.50's nearness by place."""
        return PLACES[self.sthana] | (
            frozenset({Place.NASIKA}) if self.nasika else frozenset()
        )

    @property
    def sparsa(self) -> bool:
        return self.sound.rstrip(ANUNASIKA_MARK) in SPARSA

    @property
    def anunasika(self) -> bool:
        """1.1.8: both organs at once. See `is_anunasika` for the argument."""
        return self.mukha and self.nasika


def _abhyantara_of(sound: str, *, derivational: bool = True) -> Abhyantara:
    """
    तत्र स्पृष्टं प्रयत्नं स्पर्शानाम् । ईषत्स्पृष्टमन्तःस्थानाम् ।
    ईषद्विवृतमूष्मणाम् । विवृतं स्वराणाम् ।
    ह्रस्वस्यावर्णस्य प्रयोगे संवृतम् । प्रक्रियादशायां तु विवृतमेव ।

    The last pair is the load-bearing one. Short `a` is *pronounced* saṃvṛta,
    but during derivation it counts as vivṛta — and it has to, or it would not
    share an effort with ā and 6.1.101 akaḥ savarṇe dīrghaḥ could never fire.
    `derivational` is therefore True by default: this module exists to serve
    the rules, and the rules run in the prakriyā.
    """
    if sound == "a" and not derivational:
        return Abhyantara.SAMVRTA
    if sound in SPARSA:
        return Abhyantara.SPRSTA
    if sound in ANTAHSTHA:
        return Abhyantara.ISATSPRSTA
    if sound in USMAN or sound in (VISARGA, JIHVAMULIYA, UPADHMANIYA):
        return Abhyantara.ISADVIVRTA
    return Abhyantara.VIVRTA


def _bahya_of(sound: str) -> FrozenSet[Bahya]:
    out = set()
    if sound in _KHAR:
        out |= {Bahya.VIVARA, Bahya.SVASA, Bahya.AGHOSA}
    if sound in _HAS or sound in SVARA:
        out |= {Bahya.SAMVARA, Bahya.NADA, Bahya.GHOSA}
    if sound in ALPAPRANA or sound in SVARA:
        out.add(Bahya.ALPAPRANA)
    if sound in MAHAPRANA:
        out.add(Bahya.MAHAPRANA)
    return frozenset(out)


def _build() -> Dict[str, Varna]:
    table: Dict[str, Varna] = {}
    for quarter, tokens, sthana in SIKSA_STHANA:
        for token in tokens:
            for sound in _expand(token):
                table[sound] = Varna(
                    sound=sound,
                    sthana=sthana,
                    abhyantara=_abhyantara_of(sound),
                    bahya=_bahya_of(sound),
                    svara=sound in SVARA,
                    mukha=sound != ANUSVARA,
                    nasika=sound in ANUNASIKA_STOPS or sound == ANUSVARA,
                    siksa=quarter,
                )
    return table


VARNAS: Dict[str, Varna] = _build()


def varna(sound: str) -> Optional[Varna]:
    """
    The feature record for a sound, or None if it is outside the inventory.

    A sound carrying the anunāsika mark is not listed separately — the Śikṣā
    places sounds, and nasality is a quality laid over a placed sound. So the
    base is looked up and the nose is added.
    """
    if sound in VARNAS:
        return VARNAS[sound]
    if sound.endswith(ANUNASIKA_MARK):
        base = VARNAS.get(sound[: -len(ANUNASIKA_MARK)])
        if base is not None:
            return replace(base, sound=sound, nasika=True)
    return None


def nasalize(sound: str) -> str:
    """The anunāsika counterpart of a sound: ā -> ā̐."""
    return sound if sound.endswith(ANUNASIKA_MARK) else sound + ANUNASIKA_MARK


# ---------------------------------------------------------------------------
# savarṇatva
# ---------------------------------------------------------------------------

#: The two readings of आभ्यन्तर प्रयत्न. See `Abhyantara`.
FIVEFOLD = "kaumudī-5"
FOURFOLD = "kāśikā-4"


def effort(sound: str, scheme: str = FIVEFOLD) -> Optional[Abhyantara]:
    """
    The internal effort of a sound under the named reading of the prayatnas.

    Under FOURFOLD the ūṣmans' īṣadvivṛta is not distinguished from the vowels'
    vivṛta, which is the Kāśikā's count.
    """
    v = varna(sound)
    if v is None:
        return None
    if scheme == FOURFOLD and v.abhyantara is Abhyantara.ISADVIVRTA:
        return Abhyantara.VIVRTA
    return v.abhyantara


#: The sandhyakṣaras — e, ai, o, au. The Śikṣā gives e and ai one place
#: (कण्ठतालु) and o and au another (कण्ठोष्ठम्), and all four are vivṛta, so the
#: two criteria of 1.1.9 taken alone make e savarṇa with ai and o with au. They
#: are not, and the Kāśikā's enumeration on 1.1.9 is where it says so:
#:
#:     सन्ध्यक्षराणां ह्रस्वा न सन्ति, तान्यपि द्वादशप्रभेदानि
#:     "the sandhyakṣaras have no short forms; they too have twelve
#:      sub-varieties"
#:
#: — twelve being two lengths by three accents by two nasalities. That passage
#: is counting varṇa by varṇa, eighteen for the a-varṇa and twelve for the
#: ḷ-varṇa, so twelve *apiece* for e and ai makes them two varṇas rather than
#: one class of twenty-four.
#:
#: The system forces the same answer independently. aiC in 1.1.1 is not tapara,
#: so 1.1.69 widens it to the savarṇas of ai and au; were e savarṇa with ai,
#: vṛddhi would take in e, and e is guṇa by 1.1.2. The two saṃjñās would
#: overlap. Whichever way it is approached the four stand apart, so they are
#: separated here explicitly rather than left to the feature table.
_SANDHYAKSARA: FrozenSet[str] = frozenset(("e", "ai", "o", "au"))


#: वार्त्तिक ऋकारऌकारयोः सवर्णसञ्ज्ञा विधेया — Mahābhāṣya on 1.1.9, Kielhorn
#: I.62.27-63.23, repeated in the Laghukaumudī as ऋऌवर्णयोर्मिथः सावर्ण्यं
#: वाच्यम्. ṛ is mūrdhanya and ḷ dantya, so the sūtra alone would not join
#: them; the vārttika does.
_RL_VARTTIKA: FrozenSet[str] = frozenset(VOWEL_VARNA["ṛ"] + VOWEL_VARNA["ḷ"])


def savarna(
    first: str,
    second: str,
    *,
    varttika: bool = True,
    scheme: str = FIVEFOLD,
    restriction: bool = True,
    enumeration: bool = True,
) -> bool:
    """
    1.1.9 तुल्यास्यप्रयत्नं सवर्णम् — same place and same internal effort.

    A relation, not a property. The bhāṣya is explicit that both terms are
    सम्बन्धिशब्द: यत् प्रति यत् तुल्यास्यप्रयत्नं तत् प्रति तत् सवर्णसञ्ज्ञं भवति —
    "with respect to which a sound has equal place-and-effort, with respect to
    that it bears the name savarṇa." Hence two arguments.

    External effort is deliberately not consulted. k, kh, g, gh and ṅ differ in
    voice, aspiration and nasality and are savarṇa all the same; that is what
    makes 8.4.58 anusvārasya yayi parasavarṇaḥ work.

    Three switches, each so that a test can show a provision is load-bearing
    rather than decorative:

      `varttika=False`  drops the ṛ/ḷ extension
      `restriction=False`  drops 1.1.10 नाज्झलौ
      `scheme=FOURFOLD`  reads the prayatnas as the Kāśikā counts them
      `enumeration=False`  drops the sandhyakṣara separation
    """
    a, b = varna(first), varna(second)
    if a is None or b is None:
        return False
    # 1.1.10 नाज्झलौ — a vowel and a consonant, never; whatever the features say.
    if restriction and a.svara != b.svara:
        return False
    # The sandhyakṣaras are separate varṇas; see _SANDHYAKSARA.
    if enumeration and (first in _SANDHYAKSARA or second in _SANDHYAKSARA):
        return first == second
    if varttika and first in _RL_VARTTIKA and second in _RL_VARTTIKA:
        return True
    return (
        a.sthana is b.sthana
        and effort(first, scheme) is effort(second, scheme)
    )


def savarnas_of(sound: str, **kw) -> Tuple[str, ...]:
    """Every sound in the inventory savarṇa with this one, itself included."""
    return tuple(s for s in VARNAS if savarna(sound, s, **kw))


def blocked_by_na_ajjhalau(scheme: str = FIVEFOLD) -> Tuple[Tuple[str, str], ...]:
    """
    1.1.10 नाज्झलौ — the pairs this niṣedha actually rescues.

    Every ordered pair that 1.1.9 would have made savarṇa, and that 1.1.10
    stops because one is a vowel and the other a consonant. Under FIVEFOLD this
    comes out empty: the prayatnas have already done the work. Under FOURFOLD it
    yields the Kāśikā's own examples, a/h and i/ś among them.
    """
    return tuple(
        (x, y)
        for x in VARNAS
        for y in VARNAS
        if savarna(x, y, scheme=scheme, restriction=False)
        and not savarna(x, y, scheme=scheme, restriction=True)
    )


def is_anunasika(sound: str) -> bool:
    """
    1.1.8 मुखनासिकावचनोऽनुनासिकः — uttered by mouth AND nose together.

    Both organs are named, and the bhāṣya says why each is there:

        नासिकावचनः अनुनासिकः इति इयति उच्यमाने यमानुस्वाराणाम् एव प्रसज्येत
        "were only 'nose-uttered' said, it would fall on the yamas and the
         anusvāra alone"
        मुखवचनः अनुनासिकः इति इयति उच्यमाने कचटतपानाम् एव प्रसज्येत
        "were only 'mouth-uttered' said, it would fall on k c ṭ t p alone"

    So **anusvāra is not anunāsika**: its place is the nose by itself
    (नासिकाऽनुस्वारस्य), and mukha is in the sūtra to keep it out. The Kāśikā
    says the same — मुखग्रहणं किम्? अनुस्वारस्यैव हि स्यात्.

    The bhāṣya also warns against reading this as a constructor: नित्येषु शब्देषु
    सतः अनुनासिकस्य सञ्ज्ञा क्रियते, न सञ्ज्ञया अनुनासिको भाव्यते — the name is
    given to a nasal sound that is already nasal; the name does not make it so.
    Hence nasality is a feature of the varṇa here, and this function only reads
    it off.
    """
    v = varna(sound)
    return bool(v and v.anunasika)


__all__ = [
    "ALPAPRANA", "ANTAHSTHA", "ANUNASIKA_STOPS", "ANUSVARA", "Abhyantara",
    "ANUNASIKA_MARK", "Bahya", "JIHVAMULIYA", "MAHAPRANA", "SIKSA_STHANA", "SPARSA", "SVARA",
    "Place", "PLACES", "Sthana", "UPADHMANIYA", "USMAN", "VARGA", "VARNAS", "VISARGA",
    "VOWEL_VARNA", "FIVEFOLD", "FOURFOLD", "Varna", "blocked_by_na_ajjhalau", "effort",
    "is_anunasika", "nasalize", "savarna", "savarnas_of", "varna",
]
