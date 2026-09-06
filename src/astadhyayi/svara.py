# -*- coding: utf-8 -*-
"""
Duration and accent — 1.2.27 to 1.2.32.

    1.2.27  ऊकालोऽज्झ्रस्वदीर्घप्लुतः   a vowel of one, two or three mātrās
    1.2.28  अचश्च                        and those substitutes go on a vowel
    1.2.29  उच्चैरुदात्तः                 a high vowel is udātta
    1.2.30  नीचैरनुदात्तः                 a low one anudātta
    1.2.31  समाहारः स्वरितः               the two together, svarita
    1.2.32  तस्यादित उदात्तमर्धह्रस्वम्   of which the first half-mātrā is high

This block closes a gap the earlier codification kept recording. The note on
1.1.69 says accent is not modelled anywhere, so the third of the three
dimensions savarṇatva disregards — स्वर, आनुनासिक्य, काल — was represented only
in part. Two of the three are now here, and the third was always here: 1.2.27
is the sūtra that licenses the duration `grahana.kala` computes for 1.1.70.

1.2.27's ऊ is worth a second look. The Kāśikā reads it as a प्रश्लिष्टनिर्देश,
three enunciations fused into one by sandhi — उ, ऊ and ऊ३, of one, two and
three mātrās — matched in order against ह्रस्व, दीर्घ and प्लुत. So a sūtra of
four words defines three names at once, and the vowel it is written with IS the
measure it assigns.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Sequence, Tuple

from src.chandas.core import LONG_VOWELS, SHORT_VOWELS


#: 1.2.27's three durations, and the vowel each is enunciated with. The Kāśikā
#: spells the fusion out: उ ऊ ऊ३ इत्येवंकालोऽज् यथाक्रमं ह्रस्वदीर्घप्लुतः.
DURATIONS: Tuple[Tuple[str, str, int], ...] = (
    ("hrasva", "u", 1),
    ("dīrgha", "ū", 2),
    ("pluta", "ū3", 3),
)

#: The pluta mark, as the texts write it — a following 3.
PLUTA_MARK = "3"


class Accent(Enum):
    """1.2.29 to 1.2.31. Three names for a vowel, and every vowel has one."""

    UDATTA = "udātta"
    ANUDATTA = "anudātta"
    SVARITA = "svarita"


#: How the accents are marked in the SLP1 texts on disk. An unmarked vowel is
#: udātta; the dhātupāṭha's 1,868 tildes are nasality and these two are accent.
#: 1.3.12 अनुदात्तङित आत्मनेपदम् reads exactly this mark, which is why the
#: dhātupāṭha carries it and why `Dhatu.accent` keeps it apart from the form.
SLP1_ANUDATTA = "\\"
SLP1_SVARITA = "^"


def duration(vowel: str) -> Optional[int]:
    """
    1.2.27: the measure of a vowel in mātrās — 1, 2 or 3.

    कालग्रहणं परिमाणार्थम्, the word kāla is there for measure. उकालो ह्रस्वः:
    दधि, मधु. ऊकालो दीर्घः: कुमारी, गौरी. ऊ३कालः प्लुतः: देवदत्त३ अत्र न्वसि.

    The tables are src/chandas/core.py's, so a vowel is exactly as long to the
    grammar as it is to the metre. This is the sūtra that licenses what
    `grahana.kala` was already doing for 1.1.70.
    """
    if vowel.endswith(PLUTA_MARK):
        return 3
    if vowel in SHORT_VOWELS:
        return 1
    if vowel in LONG_VOWELS:
        return 2
    return None


def duration_name(vowel: str) -> Optional[str]:
    """Which of the three names 1.2.27 gives this vowel."""
    measure = duration(vowel)
    for name, _, matras in DURATIONS:
        if matras == measure:
            return name
    return None


def is_hrasva(vowel: str) -> bool:
    return duration(vowel) == 1


def is_dirgha(vowel: str) -> bool:
    return duration(vowel) == 2


def is_pluta(vowel: str) -> bool:
    return duration(vowel) == 3


def substitutable(sthanin: str) -> bool:
    """
    1.2.28 अचश्च — a hrasva, dīrgha or pluta prescribed by its own name goes in
    the room of a VOWEL and of nothing else.

    परिभाषेयं स्थानिनियमार्था: the paribhāṣā restricts the substituend. So
    1.2.47 ह्रस्वो नपुंसके shortens the vowel of रै, नौ and गो to give अतिरि,
    अतिनु and उपगु — the same three forms 1.1.48 turns on. अच इति किम्?
    सुवाग् ब्राह्मणकुलम्, where there is a consonant at the end and nothing to
    shorten; and अग्निचि३त् for the pluta of 8.2.82, where the pluta falls on
    the vowel and not on the final त्.
    """
    return duration(sthanin) is not None


# ---------------------------------------------------------------------------
# 1.2.29 to 1.2.32 — accent
# ---------------------------------------------------------------------------


def accent_of(marked: str) -> Accent:
    """
    The accent a marked vowel carries, by the convention the texts use.

    Unmarked is udātta, which is why the dhātupāṭha writes only two marks.
    """
    if SLP1_SVARITA in marked:
        return Accent.SVARITA
    if SLP1_ANUDATTA in marked:
        return Accent.ANUDATTA
    return Accent.UDATTA


@dataclass(frozen=True)
class SvaritaProfile:
    """1.2.32: how a svarita divides, in mātrās."""

    udatta: float
    anudatta: float

    @property
    def total(self) -> float:
        return self.udatta + self.anudatta


def svarita_profile(vowel: str) -> Optional[SvaritaProfile]:
    """
    1.2.32 तस्यादित उदात्तमर्धह्रस्वम् — of a svarita, the first half-mātrā is
    udātta and the remainder anudātta.

    1.2.31 says a svarita is the two accents combined —
    उदात्तानुदात्तस्वरसमाहारो योऽच् — but not in what proportion, and the
    Kāśikā puts the question: तत्र न ज्ञायते कस्मिन्नंशे उदात्तः? कियान्वा
    उदात्तः? This sūtra answers both at once: आदावर्धह्रस्वमुदात्तम्,
    परिशिष्टमनुदात्तम्.

    Half a mātrā, whatever the vowel's length — अर्धह्रस्वम् इति च
    अर्धमात्रोपलक्ष्यते। ह्रस्वग्रहणमतन्त्रम्। सर्वेषामेव
    ह्रस्वदीर्घप्लुतानां स्वरितानामेष स्वरविभागः. So a svarita dīrgha is half
    a mātrā high and one and a half low, and a pluta two and a half low.
    """
    measure = duration(vowel)
    if measure is None:
        return None
    return SvaritaProfile(udatta=0.5, anudatta=measure - 0.5)


def combines(first: Accent, second: Accent) -> Optional[Accent]:
    """
    1.2.31 समाहारः स्वरितः — udātta and anudātta together make a svarita.

    The Kāśikā is careful that it is the QUALITIES that combine and not two
    vowels: सामर्थ्याच्चात्र लोकवेदयोः प्रसिद्धौ गुणावेव वर्णधर्मावुदात्तानुदात्तौ
    गृह्येते, नाचौ. One vowel bears both in succession, which is what 1.2.32
    then measures out. शिक्यम्, कन्या, सामन्यः, क्व.
    """
    if {first, second} == {Accent.UDATTA, Accent.ANUDATTA}:
        return Accent.SVARITA
    return None


# --- 1.2.33 to 1.2.40: how the three accents are actually recited ---------
#
#     1.2.33  एकश्रुति दूरात् सम्बुद्धौ            calling from a distance
#     1.2.34  यज्ञकर्मण्यजपन्यूङ्खसामसु            in the rite, with three exceptions
#     1.2.35  उच्चैस्तरां वा वषट्कारः               and the वषट् higher, or not
#     1.2.36  विभाषा छन्दसि                        in the Veda, optionally
#     1.2.37  न सुब्रह्मण्यायां स्वरितस्य तूदात्तः  but not in the subrahmaṇyā
#     1.2.38  देवब्रह्मणोरनुदात्तः                  save for देव and ब्रह्मन्
#     1.2.39  स्वरितात् संहितायामनुदात्तानाम्       after a svarita, in saṃhitā
#     1.2.40  उदात्तस्वरितपरस्य सन्नतरः             and the one before a high tone
#
# 1.2.29–1.2.32 said what the three accents *are*. These eight say what
# becomes of them when someone speaks: in most of the settings named here the
# distinction is simply dropped — स्वराणाम् उदात्तादीनाम् अविभागो भेदतिरोधानम्
# एकश्रुतिः, the Kāśikā's gloss, a suppressing of the difference.
#
# So this block works over a sequence and not over a sound. 1.2.39 asks what
# came before, 1.2.40 what comes after, and neither question can be put to a
# vowel on its own. `recite` takes the accents of a phrase and returns what
# each syllable is actually said at.


class Register(Enum):
    """What a syllable is actually recited at, once these eight have run."""

    UDATTA = "udātta"
    ANUDATTA = "anudātta"
    SVARITA = "svarita"
    #: एकश्रुति — the three collapsed into one tone.
    EKASRUTI = "ekaśruti"
    #: सन्नतर, glossed अनुदात्ततर: lower still than an anudātta.
    SANNATARA = "sannatara"
    #: उच्चैस्तराम् — higher than an udātta.
    UCCAISTARAM = "uccaistarām"


#: The settings 1.2.33–1.2.36 name. Not a taxonomy of anything: just the four
#: occasions these sūtras distinguish, plus the ordinary case they contrast
#: with — त्रैस्वर्ये पदानां प्राप्ते, where all three accents stand.
SETTINGS = ("ordinary", "dūrāt-sambuddhi", "yajña", "chandas", "subrahmaṇyā")


@dataclass(frozen=True)
class Recitation:
    """Where the phrase is being said, as far as these eight sūtras care."""

    setting: str = "ordinary"
    #: 1.2.34's three exceptions, which keep their accents inside the rite.
    japa: bool = False
    nyunkha: bool = False
    saman: bool = False
    #: 1.2.35 — the वषट् (really वौषट्, says the Kāśikā) of the rite.
    vasatkara: bool = False
    #: 1.2.39's condition. Its counter-example is the pada-pāṭha, where the
    #: words stand apart and the rule does not reach them.
    samhita: bool = False
    #: 1.2.38 — which words of the subrahmaṇyā these syllables belong to.
    words: Tuple[str, ...] = ()


@dataclass(frozen=True)
class Recited:
    """One syllable's outcome, and the sūtra that decided it."""

    register: Register
    by: str
    why: str
    optional: bool = False


def _ekasruti_holds(where: Recitation) -> Optional[Tuple[str, str, bool]]:
    """
    Whether the whole phrase goes to one tone, and by which sūtra.

    Returns (sūtra, reason, optional), or None where the three accents stand.
    """
    if where.setting == "subrahmaṇyā":
        # 1.2.37 is a प्रतिषेध on 1.2.34 and 1.2.36 both, and the Kāśikā says
        # so: तत्र यज्ञकर्मणि इति विभाषा छन्दसि इति चैकश्रुतिः प्राप्ता
        # प्रतिषिध्यते.
        return None
    if where.setting == "dūrāt-sambuddhi":
        return ("1.2.33",
                "एकश्रुति दूरात् सम्बुद्धौ — calling to someone far off, the "
                "three accents are not distinguished: आगच्छ भो माणवक देवदत्त३",
                False)
    if where.setting == "yajña":
        if where.japa:
            return None
        if where.nyunkha:
            return None
        if where.saman:
            return None
        return ("1.2.34",
                "यज्ञकर्मण्यजपन्यूङ्खसामसु — in the rite, but not in a japa, a "
                "nyūṅkha or a sāman",
                False)
    if where.setting == "chandas":
        return ("1.2.36",
                "विभाषा छन्दसि — in the Veda, optionally; on the other reading "
                "the three accents stand, पक्षान्तरे त्रैस्वर्यमेव भवति",
                True)
    return None


def recite(
    accents: Sequence[Accent],
    where: Optional[Recitation] = None,
) -> Tuple[Recited, ...]:
    """
    What each syllable of a phrase is actually said at — 1.2.33 to 1.2.40.

    The order is the one the Kāśikā argues for. 1.2.37 comes first because it
    is a प्रतिषेध on two of the rules that would otherwise flatten everything,
    and 1.2.38 is an exception within it. Then the ekaśruti settings. Then, in
    the ordinary case, 1.2.39 and 1.2.40, which look backwards and forwards
    along the sequence.
    """
    where = where or Recitation()
    accents = tuple(accents)
    out: List[Recited] = []

    flatten = _ekasruti_holds(where)
    if flatten is not None:
        sutra, why, optional = flatten
        for accent in accents:
            if where.vasatkara and where.setting == "yajña":
                out.append(Recited(
                    Register.UCCAISTARAM, "1.2.35",
                    "उच्चैस्तरां वा वषट्कारः — the वषट् of the rite is said "
                    "higher still, or else at the one tone",
                    optional=True,
                ))
                continue
            out.append(Recited(Register.EKASRUTI, sutra, why, optional))
        return tuple(out)

    if where.setting == "subrahmaṇyā":
        for index, accent in enumerate(accents):
            word = where.words[index] if index < len(where.words) else None
            if accent is not Accent.SVARITA:
                out.append(Recited(
                    Register(_plain(accent)), "1.2.37",
                    "न सुब्रह्मण्यायाम् — the subrahmaṇyā keeps its accents",
                ))
            elif word in ("deva", "brahman"):
                out.append(Recited(
                    Register.ANUDATTA, "1.2.38",
                    "देवब्रह्मणोरनुदात्तः — but in these two words the svarita "
                    "goes to anudātta, not udātta: देवा ब्रह्माण आगच्छत",
                ))
            else:
                out.append(Recited(
                    Register.UDATTA, "1.2.37",
                    "स्वरितस्य तूदात्तः — and a svarita that would arise there "
                    "becomes udātta: सुब्रह्मण्योम् इन्द्रागच्छ",
                ))
        return tuple(out)

    # The ordinary case. 1.2.39 looks back to the nearest svarita; 1.2.40
    # looks ahead one syllable.
    seen_svarita = False
    for index, accent in enumerate(accents):
        following = accents[index + 1] if index + 1 < len(accents) else None

        if accent is Accent.SVARITA:
            seen_svarita = True
            out.append(Recited(
                Register.SVARITA, "1.2.31",
                "समाहारः स्वरितः — the two together, and nothing in this "
                "block reaches a svarita outside the subrahmaṇyā",
            ))
            continue

        if (accent is Accent.ANUDATTA and seen_svarita and where.samhita):
            out.append(Recited(
                Register.EKASRUTI, "1.2.39",
                "स्वरितात् संहितायामनुदात्तानाम् — the anudāttas following a "
                "svarita go to one tone, in continuous speech: इमं मे गङ्गे "
                "यमुने सरस्वति शुतुद्रि",
            ))
            continue

        if (accent is Accent.ANUDATTA
                and following in (Accent.UDATTA, Accent.SVARITA)):
            out.append(Recited(
                Register.SANNATARA, "1.2.40",
                "उदात्तस्वरितपरस्य सन्नतरः — an anudātta with an udātta or a "
                "svarita next after it is said lower still, अनुदात्ततर",
            ))
            continue

        out.append(Recited(Register(_plain(accent)), "1.2.29–1.2.31",
                           "the accent as 1.2.29–1.2.31 named it"))
    return tuple(out)


def _plain(accent: Accent) -> str:
    return {
        Accent.UDATTA: "udātta",
        Accent.ANUDATTA: "anudātta",
        Accent.SVARITA: "svarita",
    }[accent]


def recite_written(
    accents: Sequence[str],
    setting: str = "ordinary",
    *,
    japa: bool = False,
    nyunkha: bool = False,
    saman: bool = False,
    vasatkara: bool = False,
    samhita: bool = False,
    words: Sequence[str] = (),
) -> Tuple[Recited, ...]:
    """
    `recite` from written accent names — what a form on a page can supply.

    The three are named as the sūtras name them: udātta, anudātta, svarita.
    Anything else is read as anudātta, since that is what an unmarked
    syllable is by 1.2.30's neighbourhood, and a reader trying the playground
    should get an answer rather than an error.
    """
    named = {"udātta": Accent.UDATTA, "anudātta": Accent.ANUDATTA,
             "svarita": Accent.SVARITA, "u": Accent.UDATTA,
             "a": Accent.ANUDATTA, "s": Accent.SVARITA}
    return recite(
        [named.get(str(a).strip(), Accent.ANUDATTA) for a in accents],
        Recitation(setting=setting, japa=japa, nyunkha=nyunkha, saman=saman,
                   vasatkara=vasatkara, samhita=samhita,
                   words=tuple(words)),
    )


def ekasruti(accents: Sequence[Accent], where: Recitation) -> bool:
    """Does the whole phrase go to one tone? A shorthand over `recite`."""
    return all(r.register is Register.EKASRUTI for r in recite(accents, where))


__all__ = [
    "Accent",
    "Recitation",
    "Recited",
    "Register",
    "SETTINGS",
    "ekasruti",
    "recite",
    "recite_written",
    "DURATIONS",
    "PLUTA_MARK",
    "SLP1_ANUDATTA",
    "SLP1_SVARITA",
    "SvaritaProfile",
    "accent_of",
    "combines",
    "duration",
    "duration_name",
    "is_dirgha",
    "is_hrasva",
    "is_pluta",
    "substitutable",
    "svarita_profile",
    "parangavat", "Parangavat", "NOT_PARANGAVAT",
]


# ---------------------------------------------------------------------------
# 2.1.2 सुबामन्त्रिते पराङ्गवत् स्वरे
# ---------------------------------------------------------------------------


#: The operations 2.1.2 is asked about and refuses, with the sūtra that would
#: have performed each. The Kāśikā's स्वर इति किम्? names both: षत्व by
#: 8.3.59 and णत्व by 8.4.2 do *not* treat the subanta as a limb of what
#: follows, so कूपे सिञ्चन् keeps its s and चर्म नमन् its n.
NOT_PARANGAVAT: Tuple[Tuple[str, str], ...] = (
    ("ṣatva", "8.3.59"),
    ("ṇatva", "8.4.2"),
)


@dataclass(frozen=True)
class Parangavat:
    """Whether a subanta counts as a limb of the vocative that follows it."""

    holds: bool
    by: str
    why: str
    #: वत्करणं किम्? The atideśa does not cost the word its own operations.
    keeps_own: bool = True


def _resolve_operation(name):
    """The named operation, or None for the empty string. Raises on a typo."""
    from src.astadhyayi.operations import resolve

    return resolve(name)


def parangavat(
    preceding_is_sup: bool = True,
    following_is_amantrita: bool = True,
    operation: str = "svara",
) -> Parangavat:
    """
    2.1.2: a subanta before a vocative behaves as a limb of it — for accent.

    तादात्म्यातिदेशोऽयम्, an atideśa of identity: सुबन्तम् आमन्त्रितम्
    अनुप्रविशति, the subanta *enters into* the vocative rather than merely
    resembling it. What it is for is 6.1.198 आमन्त्रितस्य च, which makes a
    vocative initially udātta; the atideśa carries that accent back over the
    subanta, so कुण्डे॑नाटन् and मद्रा॑णां राजन् are accented as one.

    Every word of the sūtra is answered by a कim? in the Kāśikā, and each is
    a condition here:

      सुबिति किम्?      पीड्ये पीड्यमान — the first word must be a subanta.
      आमन्त्रित इति किम्? गेहे गार्ग्यः — the second must be a vocative.
      परग्रहणं किम्?     पूर्वस्य मा भूत् — only what *precedes* the vocative;
                        in देव॑दत्त कुण्डे॑नाटन् the following word is untouched.
      अङ्गग्रहणं किम्?   so that it becomes a *limb* and not one mass —
                        यथा मृत्पिण्डीभूतः स्वरं लभेत, उभयोः आद्युदात्तत्वं मा भूत्.
      वत्करणं किम्?     स्वाश्रयमपि कार्यं यथा स्यात् — the वत् leaves the word
                        its own operations besides; hence `keeps_own`.
      स्वर इति किम्?     कूपे सिञ्चन्, चर्म नमन् — accent only, and see
                        :data:`NOT_PARANGAVAT`.

    The vārttikas on this sūtra go further — पूर्वाङ्गवच्चेति वक्तव्यम् in
    the other direction, अव्ययानां न, अव्ययीभावस्य त्विष्यते — and are left
    where the 921 others are: read, recorded, not yet codified.
    """
    if not preceding_is_sup:
        return Parangavat(
            False, "2.1.2",
            "सुप् इति किम्? पीड्ये पीड्यमान — what precedes is not a "
            "subanta, and the atideśa has nothing to move.",
        )
    if not following_is_amantrita:
        return Parangavat(
            False, "2.1.2",
            "आमन्त्रिते इति किम्? गे॒हे गार्ग्यः॑ — what follows is not a "
            "vocative, so there is no limb to belong to.",
        )
    named = _resolve_operation(operation)
    blocked = dict(NOT_PARANGAVAT).get(named.name if named else operation)
    if blocked:
        return Parangavat(
            False, "2.1.2",
            f"स्वरे इति किम्? — the atideśa is for accent alone, and "
            f"{operation} is done by {blocked}. षत्वणत्वे प्रति पराङ्गवद् न "
            f"भवति: कूपे सिञ्चन्, चर्म नमन्.",
        )
    if named is None or named.name != "svara":
        return Parangavat(
            False, "2.1.2",
            f"स्वरे इति किम्? — {operation!r} is not an accent operation, "
            f"and the sūtra reaches no other.",
        )
    return Parangavat(
        True, "2.1.2",
        "सुबामन्त्रिते पराङ्गवत् स्वरे — the subanta counts as a limb of the "
        "vocative that follows, for accent. तादात्म्यातिदेशोऽयम्, and what "
        "it is for is 6.1.198 आमन्त्रितस्य च: कुण्डे॑नाटन्, पर॑शुना वृश्चन्, "
        "मद्रा॑णां राजन्.",
    )
