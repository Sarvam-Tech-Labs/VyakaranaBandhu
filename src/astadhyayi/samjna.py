# -*- coding: utf-8 -*-
"""
Saṃjñās that name a class of word or affix — 1.1.20 to 1.3.1.

    1.1.20  दाधा घ्वदाप्              ghu: the dā and dhā roots, less dāp
    1.1.21  आद्यन्तवदेकस्मिन्         a lone item counts as first and as last
    1.1.22  तरप्तमपौ घः                gha: the affixes tarap and tamap
    1.1.23  बहुगणवतुडति संख्या         saṃkhyā: bahu, gaṇa, vatu, ḍati
    1.1.24  ष्णान्ता षट्               ṣaṭ: a saṃkhyā ending in ṣ or n
    1.1.25  डति च                      and one ending in ḍati
    1.1.26  क्तक्तवतू निष्ठा           niṣṭhā: the affixes kta and ktavatu
    1.1.27  सर्वादीनि सर्वनामानि      sarvanāman: sarva and the rest
    1.1.28  विभाषा दिक्समासे बहुव्रीहौ  optional in a directional bahuvrīhi
    1.1.29  न बहुव्रीहौ                 but not in a bahuvrīhi otherwise
    1.1.30  तृतीयासमासे                 nor in an instrumental compound
    1.1.31  द्वन्द्वे च                  nor in a dvandva
    1.1.32  विभाषा जसि                  optionally so, before jas
    1.1.33  प्रथमचरमतया...              seven more words, optional before jas
    1.1.34  पूर्वपरावर...                seven more, when they place a thing
    1.1.35  स्वमज्ञातिधनाख्यायाम्       sva, when it means neither kin nor wealth
    1.1.36  अन्तरं बहिर्योग...           antara, in two senses
    1.1.42  शि सर्वनामस्थानम्           sarvanāmasthāna: the substitute śi
    1.1.43  सुडनपुंसकस्य                and suṬ, except for a neuter
    1.1.44  न वेति विभाषा                vibhāṣā: the words na and vā
    1.1.73  वृद्धिर्यस्याचामादिः...      vṛddha: first vowel a vṛddhi
    1.1.74  त्यदादीनि च                  and the tyadādi words
    1.1.75  एङ् प्राचां देशे             and an eṄ, in an eastern place-name
    1.2.41  अपृक्त एकाल् प्रत्ययः        apṛkta: an affix of a single sound
    1.2.42  तत्पुरुषः समानाधिकरणः...     karmadhāraya
    1.2.43  प्रथमानिर्दिष्टं समास...     upasarjana, read off the first case
    1.2.44  एकविभक्ति चापूर्वनिपाते      and what keeps one case-ending
    1.2.45  अर्थवदधातुरप्रत्ययः...       prātipadika
    1.2.46  कृत्तद्धितसमासाश्च           and kṛt, taddhita and compound
    1.3.1   भूवादयो धातवः                dhātu: bhū and the roots listed with it

Two of these name their members by pointing outside the Aṣṭādhyāyī, and both
texts are on disk, so both are read rather than transcribed. 1.1.20 names roots
that the dhātupāṭha holds; 1.1.27 names a gaṇa that the Gaṇapāṭha holds. The
saving is not in the typing but in the checking: सर्वादि has thirty-five
members and a hand-copied list would be wrong somewhere without anyone
noticing.
"""

from __future__ import annotations

from functools import lru_cache
from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Optional, Tuple

from src.chandas.core import scan_phonemes
from src.astadhyayi.corpus import gana_for, load_dhatupatha
from src.astadhyayi.itsamjna import DHATU, analyze


# ---------------------------------------------------------------------------
# 1.1.20 दाधा घ्वदाप् — the ghu roots
# ---------------------------------------------------------------------------

#: The root-shapes the sūtra names, and the reason the list is longer than two.
#:
#: दा and धा name two families, but the dhātupāṭha spells several of their
#: members with a final ec: दो, दे, दै, धे. Those are dā- and dhā-roots all the
#: same, because 6.1.45 आदेच उपदेशेऽशिति turns a final ec into ā in upadeśa. So
#: the shape test admits them, and that is what makes the sūtra's exclusion
#: necessary — दैप् would otherwise come in as a dā-root.
#:
#: An earlier version left दै out of this set, which reached the right six by
#: the wrong route: दैप् was being dropped for having the wrong shape when the
#: tradition drops it by name. The Kāśikā is explicit that both are excluded by
#: name, दाब्दैपौ वर्जयित्वा, and a test caught the difference.
GHU_SHAPES: FrozenSet[str] = frozenset(
    {"dā", "dhā", "do", "de", "dai", "dhe"}
)

#: अदाप् — the exclusion. The sūtra names दाप्; the Kāśikā excludes दैप् with
#: it, दाब्दैपौ वर्जयित्वा, and the two are exactly what the shape test would
#: otherwise let through.
NOT_GHU: FrozenSet[str] = frozenset({"dāp", "daip"})


@lru_cache(maxsize=1)
def ghu_roots() -> Tuple[str, ...]:
    """
    The roots that bear the name ghu, read out of the dhātupāṭha.

    Every root whose upadeśa, with its it-letters removed by 1.3.2–1.3.9, is or
    becomes दा or धा — and then दाप् and दैप् taken out by name. The
    dhātupāṭha yields eight of that shape and the exclusion removes exactly
    two, leaving the six the Kāśikā names: डुदाञ्, दाण्, दो, देङ्, डुधाञ्, धेट्.
    """
    found = []
    for entry in sorted(load_dhatupatha().values(), key=lambda e: e.code):
        bare = entry.upadesa.replace("̐", "")
        if bare in NOT_GHU:
            continue
        stem = analyze(entry.upadesa, DHATU).stem.replace("̐", "")
        if stem in GHU_SHAPES:
            found.append(bare)
    return tuple(found)


def is_ghu(root: str) -> bool:
    """1.1.20: does this root, in its upadeśa form, bear the name ghu?"""
    return root in ghu_roots()


# ---------------------------------------------------------------------------
# 1.1.21 आद्यन्तवदेकस्मिन्
# ---------------------------------------------------------------------------


class Position(Enum):
    ADI = "ādi"          # first
    ANTA = "anta"        # last
    MADHYA = "madhya"    # neither


def positions(length: int, index: int) -> FrozenSet[Position]:
    """
    1.1.21: where an item stands in a sequence, with a lone item counting as
    both ends.

    असहायस्याद्यन्तोपदिष्टानि कार्याणि न सिध्यन्तीति — operations taught for a
    first or a last would not reach something that has no companion, so this
    atideśa gives it both. आदाविव अन्त इव एकस्मिन्नपि कार्यं भवति.

    The Kāśikā's illustrations are of exactly that shape: the accent that
    3.1.3 puts on the first sound of an affix reaches औपगवम्, whose affix is a
    single sound; the lengthening that 7.3.102 gives before a plural ending
    reaches आभ्याम्, where there is one.
    """
    if length == 1 and index == 0:
        return frozenset({Position.ADI, Position.ANTA})
    found = set()
    if index == 0:
        found.add(Position.ADI)
    if index == length - 1:
        found.add(Position.ANTA)
    return frozenset(found or {Position.MADHYA})


# ---------------------------------------------------------------------------
# 1.1.22, 1.1.26 — two pairs of affixes named outright
# ---------------------------------------------------------------------------

#: 1.1.22 तरप्तमपौ घः. In upadeśa; the p of each is indicatory by 1.3.3.
GHA: Tuple[str, ...] = ("tarap", "tamap")

#: 1.1.26 क्तक्तवतू निष्ठा. The Kāśikā notes what each mark is for:
#: ककारः कित्कार्यार्थः, उकार उगित्कार्यार्थः — the k so that 1.1.5 will block
#: guṇa, the u so that the ugit rules will reach it.
NISTHA: Tuple[str, ...] = ("kta", "ktavatu")


def is_gha(affix: str) -> bool:
    """1.1.22: तरप् and तमप् bear the name घ. कुमारितरा, कुमारितमा."""
    return affix in GHA


def is_nistha(affix: str) -> bool:
    """1.1.26: क्त and क्तवतु bear the name निष्ठा. कृतः, कृतवान्."""
    return affix in NISTHA


# ---------------------------------------------------------------------------
# 1.1.23 to 1.1.25 — number words
# ---------------------------------------------------------------------------

#: 1.1.23 बहुगणवतुडति संख्या. Four words that are not numerals and are given
#: the name anyway. भूर्यादीनां निवृत्त्यर्थं संख्यासंज्ञा विधीयते — the point
#: is to admit these four and keep भूरि and its like out.
SAMKHYA_BY_1_1_23: Tuple[str, ...] = ("bahu", "gaṇa", "vatu", "ḍati")

#: The numerals themselves, in their upadeśa forms. Primary data: the
#: Aṣṭādhyāyī nowhere lists them, and no gaṇa collects them, because being a
#: numeral is a fact about the word and not a grammatical assignment. The forms
#: matter for 1.1.24, whose test is on the upadeśa — अन्तग्रहणमौपदेशिकार्थम् —
#: so पञ्चन् and not पञ्च.
NUMERALS: Tuple[str, ...] = (
    "eka", "dvi", "tri", "catur", "pañcan", "ṣaṣ", "saptan", "aṣṭan",
    "navan", "daśan", "ekādaśan", "dvādaśan", "viṃśati", "triṃśat",
    "catvāriṃśat", "pañcāśat", "ṣaṣṭi", "saptati", "aśīti", "navati",
    "śata", "sahasra",
)


def is_samkhya(word: str) -> bool:
    """
    1.1.23: बहु, गण, वतु and डति bear the name saṃkhyā, and so do the numerals.

    The four are the sūtra's contribution; the numerals have the name already.
    The Kāśikā guards the four: बहुगणशब्दयोर्वैपुल्ये संङ्घे च वर्तमानयोरिह
    ग्रहणं नास्ति, संख्यावाचिनोरेव — बहु and गण are meant only where they
    denote number, not where they mean 'much' or 'a troop'. That distinction is
    semantic and is not made here; a caller that knows the sense should not
    pass the word.
    """
    return word in SAMKHYA_BY_1_1_23 or word in NUMERALS


def is_sat(word: str) -> bool:
    """
    1.1.24 ष्णान्ता षट्, with 1.1.25 डति च: a saṃkhyā ending in ṣ, in n, or in
    ḍati.

    संख्या is read down from 1.1.23, so the test applies to number words only.
    The final is of the upadeśa form and the Kāśikā says so —
    अन्तग्रहणमौपदेशिकार्थम् — which is why शतानि and सहस्राणि are outside:
    शत and सहस्र end in a. षष् ends in ṣ; पञ्चन्, सप्तन्, नवन्, दशन् in n;
    and कति in ḍati by 1.1.25.
    """
    if not is_samkhya(word):
        return False
    if word.endswith("ḍati") or word == "ḍati":
        return True     # 1.1.25
    phonemes = scan_phonemes(word)
    return bool(phonemes) and phonemes[-1].text in ("ṣ", "n")


# ---------------------------------------------------------------------------
# 1.1.27 सर्वादीनि सर्वनामानि
# ---------------------------------------------------------------------------


def sarvanaman_words() -> Tuple[str, ...]:
    """
    The sarvādi list, read from the Gaṇapāṭha rather than copied.

    सर्वादि means "sarva and the rest", and the rest are in a separate text.
    Thirty-five of them, and the gaṇa the Gaṇapāṭha keys to this very sūtra is
    the list Pāṇini is pointing at.
    """
    gana = gana_for("1.1.27")
    return gana.items if gana else ()


def is_sarvanaman(word: str) -> bool:
    """1.1.27: सर्वः, विश्वः, उभ, उभय, तद्, यद्, किम् and the rest."""
    return word in sarvanaman_words()


__all__ = [
    "GHA",
    "Pratipadika",
    "Vrddha",
    "SUT",
    "Sarvanamasthana",
    "Vibhasa",
    "PRATHAMADI",
    "PURVADI",
    "Samasa",
    "Sarvanaman",
    "TAYA_SUFFIX",
    "GHU_SHAPES",
    "NISTHA",
    "NOT_GHU",
    "NUMERALS",
    "Position",
    "SAMKHYA_BY_1_1_23",
    "ghu_roots",
    "is_gha",
    "is_ghu",
    "is_nistha",
    "is_samkhya",
    "is_sarvanaman",
    "is_sarvanamasthana",
    "is_sat",
    "is_vibhasa",
    "is_vrddha",
    "aprkta",
    "first_vowel",
    "dhatu_count",
    "is_dhatu",
    "is_pratipadika",
    "karmadharaya",
    "pratipadika",
    "upasarjana",
    "tyadadi",
    "vrddha",
    "sarvanamasthana",
    "vibhasa",
    "positions",
    "sarvanaman",
    "sarvanaman_words",
]


# ---------------------------------------------------------------------------
# 1.1.28 to 1.1.36 — what qualifies the sarvanāman saṃjñā
# ---------------------------------------------------------------------------
#
# Nine sūtras that between them take the name away and give it back. 1.1.27
# grants it to the whole gaṇa; 1.1.29 to 1.1.31 withdraw it in three kinds of
# compound; 1.1.28 and 1.1.32 make two of those withdrawals optional; and
# 1.1.33 to 1.1.36 make the name itself optional before jas for particular
# words. Reading them as one decision is the only way to get the answer right,
# because each is stated against the one before it.


class Samasa(Enum):
    """The compounds these sūtras distinguish."""

    NONE = "none"
    BAHUVRIHI = "bahuvrīhi"
    DIK_BAHUVRIHI = "diksamāsa-bahuvrīhi"    # 1.1.28
    TRTIYA = "tṛtīyāsamāsa"                   # 1.1.30
    DVANDVA = "dvandva"                       # 1.1.31


#: 1.1.33 प्रथमचरमतयाल्पार्धकतिपयनेमाः. Six of the seven are NOT in the sarvādi
#: gaṇa, so this sūtra is what brings them in at all — and only before jas and
#: only optionally. नेम is the exception: it IS in the gaṇa, so 1.1.27 gives it
#: the name outright and this sūtra relaxes it, exactly as 1.1.34 relaxes
#: पूर्व. A test that assumed all seven were outside the gaṇa is what found it.
PRATHAMADI: Tuple[str, ...] = (
    "prathama", "carama", "alpa", "ardha", "katipaya", "nema",
)

#: तय in the same sūtra is an affix, not a word: द्वितय, त्रितय and the like.
#: The Kāśikā treats it as तयबन्त, so the test is on the ending.
TAYA_SUFFIX = "taya"

#: 1.1.34 पूर्वपरावरदक्षिणोत्तरापराधराणि. These ARE in the sarvādi gaṇa — the
#: Gaṇapāṭha annotates them with this very sūtra — so 1.1.27 gives them the
#: name outright and this one relaxes it before jas.
PURVADI: Tuple[str, ...] = (
    "pūrva", "para", "avara", "dakṣiṇa", "uttara", "apara", "adhara",
)


@dataclass(frozen=True)
class Sarvanaman:
    """Whether the name applies here, whether by choice, and on what authority."""

    applies: bool
    optional: bool
    by: str
    why: str


def sarvanaman(
    word: str,
    *,
    samasa: "Samasa" = None,
    before_jas: bool = False,
    vyavastha: bool = False,
    is_name: bool = False,
    means_kin_or_wealth: bool = False,
    bahiryoga_or_upasamvyana: bool = False,
) -> Sarvanaman:
    """
    1.1.27 as its eight qualifiers leave it.

    The order is the order the sūtras argue in. A compound is looked at first,
    because 1.1.29 to 1.1.31 withdraw the name wholesale and 1.1.28 and 1.1.32
    are stated as reliefs from those withdrawals — तस्मिन्नित्ये प्रतिषेधे
    प्राप्ते विभाषेयमारभ्यते, "the option is begun where that unconditional
    prohibition would otherwise hold". Only then do the word-specific
    relaxations of 1.1.33 to 1.1.36 come up, since those concern a form that
    still has the name to relax.

    The conditions that are matters of sense — whether पूर्व places a thing or
    names it, whether स्व means kin or wealth, which of two senses अन्तर is in
    — are parameters. The sūtras ask about meaning and this project has no
    semantics, so the caller answers.
    """
    samasa = samasa or Samasa.NONE
    in_gana_list = is_sarvanaman(word)

    # --- the compounds, 1.1.28 to 1.1.32 -----------------------------------
    if samasa is Samasa.DIK_BAHUVRIHI:
        return Sarvanaman(
            True, True, "1.1.28",
            "विभाषा दिक्समासे बहुव्रीहौ — a bahuvrīhi of directions takes the "
            "name optionally, against the flat prohibition 1.1.29 would "
            "otherwise impose: उत्तरपूर्वस्यै beside उत्तरपूर्वायै",
        )
    if samasa is Samasa.BAHUVRIHI:
        return Sarvanaman(
            False, False, "1.1.29",
            "न बहुव्रीहौ — प्रियविश्वाय, प्रियोभयाय, द्व्यन्याय. The "
            "prohibition is needed because the saṃjñā would otherwise reach a "
            "compound ending in a sarvādi by तदन्तविधि",
        )
    if samasa is Samasa.TRTIYA:
        return Sarvanaman(
            False, False, "1.1.30",
            "तृतीयासमासे — मासपूर्वाय, संवत्सरपूर्वाय. समास is repeated so "
            "that the prohibition reaches the phrase as well as the compound: "
            "मासेन पूर्वाय",
        )
    if samasa is Samasa.DVANDVA:
        if before_jas:
            return Sarvanaman(
                False, True, "1.1.32",
                "विभाषा जसि — in a dvandva the prohibition of 1.1.31 is "
                "unconditional, and before jas it becomes optional: "
                "कतरकतमे beside कतरकतमाः",
            )
        return Sarvanaman(
            False, False, "1.1.31",
            "द्वन्द्वे च — पूर्वापराणाम्, कतरकतमानाम्",
        )

    # --- the word-specific relaxations, 1.1.33 to 1.1.36 -------------------
    if before_jas:
        if word in PRATHAMADI or word.endswith(TAYA_SUFFIX):
            return Sarvanaman(
                True, True, "1.1.33",
                "प्रथमचरमतयाल्पार्धकतिपयनेमाश्च — seven words the gaṇa does "
                "not hold, given the name optionally before jas: प्रथमे "
                "beside प्रथमाः, द्वितये beside द्वितयाः",
            )
        if word in PURVADI and vyavastha and not is_name:
            return Sarvanaman(
                True, True, "1.1.34",
                "पूर्वपरावरदक्षिणोत्तरापराधराणि व्यवस्थायामसंज्ञायाम् — these "
                "are in the gaṇa, so 1.1.27 gives them the name outright; "
                "before jas it becomes optional where they place a thing "
                "(स्वाभिधेयापेक्षावधिनियमो व्यवस्था) and are not a name: "
                "पूर्वे beside पूर्वाः",
            )
        if word == "sva" and not means_kin_or_wealth:
            return Sarvanaman(
                True, True, "1.1.35",
                "स्वमज्ञातिधनाख्यायाम् — स्व optionally before jas when it "
                "means one's own and not a kinsman or wealth: स्वे पुत्राः "
                "beside स्वाः पुत्राः",
            )
        if word == "antara" and bahiryoga_or_upasamvyana:
            return Sarvanaman(
                True, True, "1.1.36",
                "अन्तरं बहिर्योगोपसंव्यानयोः — अन्तर optionally before jas in "
                "the sense of what lies outside or of an undergarment: "
                "अन्तरे गृहाः beside अन्तरा गृहाः, अन्तरे शाटकाः beside "
                "अन्तराः शाटकाः",
            )

    # --- 1.1.27, unqualified ------------------------------------------------
    if in_gana_list:
        return Sarvanaman(
            True, False, "1.1.27",
            "सर्वादीनि सर्वनामानि — a member of the sarvādi gaṇa, with "
            "nothing to qualify it here",
        )
    return Sarvanaman(
        False, False, "", f"{word} is not in the sarvādi gaṇa"
    )


# ---------------------------------------------------------------------------
# 1.1.42, 1.1.43 सर्वनामस्थान
# ---------------------------------------------------------------------------

#: सुट् — the first five of the sup endings, which 4.1.2 enunciates as
#: स्वौजसमौट्छष्टाभ्याम्भिस्... The pratyāhāra runs from सु to the ट् of औट्,
#: and it cannot be resolved from the śivasūtras: it is formed within the
#: sup-list, which is a separate enumeration. Stated here for that reason, with
#: the sūtra that gives it.
SUT: Tuple[str, ...] = ("su", "au", "jas", "am", "auṭ")


@dataclass(frozen=True)
class Sarvanamasthana:
    """That an ending bears the name, and which sūtra gave it."""

    by: str
    why: str


def sarvanamasthana(
    affix: str, *, napumsaka: bool = False
) -> "Optional[Sarvanamasthana]":
    """
    1.1.42 with 1.1.43 — which endings bear the name sarvanāmasthāna.

    शि unconditionally, and the first five sup endings except in a neuter. The
    Kāśikā is careful that the exception does not cut both ways: नपुंसके न
    विधिर्न प्रतिषेधः, तेन जसः शेः सर्वनामस्थानसंज्ञा पूर्वेण भवत्येव — for a
    neuter there is neither a grant nor a refusal here, so a neuter's śi keeps
    the name it already has by 1.1.42. That is why śi is tested first.
    """
    if affix == "śi":
        return Sarvanamasthana(
            "1.1.42",
            "शि, the substitute for jas and śas by 7.1.20: कुण्डानि तिष्ठन्ति, "
            "कुण्डानि पश्य. It holds in a neuter too — नपुंसके न विधिर्न "
            "प्रतिषेधः",
        )
    if affix in SUT:
        if napumsaka:
            return None
        return Sarvanamasthana(
            "1.1.43",
            "one of the five सुट् endings, outside the neuter: राजा, राजानौ, "
            "राजानः, राजानम्. सुडिति किम्? राज्ञः पश्य — the sixth is outside "
            "the five",
        )
    return None


def is_sarvanamasthana(affix: str, **conditions) -> bool:
    return sarvanamasthana(affix, **conditions) is not None


# ---------------------------------------------------------------------------
# 1.1.44 न वेति विभाषा
# ---------------------------------------------------------------------------


class Vibhasa(Enum):
    """The two things the name covers."""

    PRATISEDHA = "pratiṣedha"    # न — a prohibition
    VIKALPA = "vikalpa"          # वा — a choice


def vibhasa(word: str) -> "Optional[Vibhasa]":
    """
    1.1.44: न and वा, in a rule, both bear the name विभाषा.

    नेति प्रतिषेधो वेति विकल्पः, तयोः प्रतिषेधविकल्पयोर्विभाषेति संज्ञा भवति.
    One name for two things, and the Kāśikā says how they act together where
    both are in play: तत्र प्रतिषेधेन समीकृते विषये पश्चाद् विकल्पः प्रवर्तते —
    the prohibition levels the ground first and the option operates after.

    The इति in the sūtra is doing work: इतिकरणोऽर्थनिर्देशार्थः, it marks that
    the WORDS न and वा are meant and not their senses. That is 1.1.68's
    स्वं रूपं showing up in the text itself.
    """
    if word == "na":
        return Vibhasa.PRATISEDHA
    if word == "vā":
        return Vibhasa.VIKALPA
    return None


def is_vibhasa(word: str) -> bool:
    return vibhasa(word) is not None


# ---------------------------------------------------------------------------
# 1.1.73 to 1.1.75 — वृद्ध
# ---------------------------------------------------------------------------


def tyadadi() -> Tuple[str, ...]:
    """
    1.1.74's त्यदादि — त्यद् and what follows it, read out of the sarvādi gaṇa.

    The list is not separate: it is the tail of सर्वादि, from त्यद् to the end.
    So it comes from the Gaṇapāṭha like the rest, by taking the slice rather
    than by copying twelve words. The Kāśikā's examples walk that tail —
    त्यदीयम्, तदीयम्, एतदीयम्, इदमीयम्, अदसीयम्, त्वदीयम्, मदीयम्,
    भवदीयम्, किमीयम्.
    """
    words = sarvanaman_words()
    if "tyad" not in words:
        return ()
    return words[words.index("tyad"):]


@dataclass(frozen=True)
class Vrddha:
    """That a word bears the name vṛddha, and which sūtra gave it."""

    by: str
    why: str
    optional: bool = False


def first_vowel(word: str) -> "Optional[str]":
    """यस्याचाम् आदिः — the first of the vowels of a word."""
    for phoneme in scan_phonemes(word):
        if phoneme.kind == "vowel":
            return phoneme.text
    return None


def vrddha(
    word: str, *, praci_desa: bool = False, is_name: bool = False
) -> "Optional[Vrddha]":
    """
    1.1.73 with 1.1.74 and 1.1.75 — which words bear the name vṛddha.

    The first two conditions are about the first VOWEL and not the first
    sound, which is what यस्याचामादिः says and why the Kāśikā glosses अचामिति
    जातौ बहुवचनम्. शालीयः, मालीयः, औपगवीयः, कापटवीयः all have a vṛddhi first.
    आदिरिति किम्? साभासन्नयनः — a vṛddhi that is not first does not count.

    1.1.74 does not use that condition and 1.1.75 does, and the Kāśikā says so
    at each: यस्याचामादिग्रहणमुत्तरार्थमनुवर्तते, इह तु न संबध्यते under 1.1.74,
    and यस्याचामादिग्रहणमनुवर्तते under 1.1.75. So the phrase skips a sūtra and
    resumes — an anuvṛtti that jumps, which is worth seeing once.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import is_vrddhi
    from src.astadhyayi.sivasutra import resolve

    initial = first_vowel(word)

    # 1.1.73 वृद्धिर्यस्याचामादिस्तद् वृद्धम्
    if initial is not None and is_vrddhi(initial):
        return Vrddha(
            "1.1.73",
            f"its first vowel is {initial}, a vṛddhi by 1.1.1: शालीयः, "
            f"मालीयः, औपगवीयः, कापटवीयः",
            optional=is_name,
        )

    # 1.1.74 त्यदादीनि च
    if word in tyadadi():
        return Vrddha(
            "1.1.74",
            "one of the त्यदादि, the tail of the sarvādi gaṇa. The first-vowel "
            "condition does not apply here — इह तु न संबध्यते — so तद् and "
            "किम् are vṛddha though neither begins with a vṛddhi: तदीयम्, "
            "किमीयम्",
        )

    # 1.1.75 एङ् प्राचां देशे
    if praci_desa and initial in resolve("eṄ").sounds:
        return Vrddha(
            "1.1.75",
            f"its first vowel is {initial}, an eṄ, and it names an eastern "
            f"place: एणीपचनीयः, भोजकटीयः, गोनर्दीयः. एङिति किम्? आहिच्छत्रः, "
            f"कान्यकुब्जः. देश इति किम्? गौमताः",
        )
    return None


def is_vrddha(word: str, **conditions) -> bool:
    return vrddha(word, **conditions) is not None


# ---------------------------------------------------------------------------
# 1.2.41 अपृक्त
# ---------------------------------------------------------------------------


def aprkta(affix: str) -> bool:
    """
    1.2.41 अपृक्त एकाल् प्रत्ययः — an affix of a single sound.

    असहायवाची एकशब्दः, the Kāśikā glosses — एक means "without a companion",
    the same reading it gives एकाच् at 1.1.14. So the test is on the affix as
    it stands after its it-letters are gone, and it is a test on SOUNDS: a
    digraph is one al.

    एकालिति किम्? दर्विः, जागृविः — two sounds, so not apṛkta.
    प्रत्यय इति किम्? सुराः — not an affix at all.

    The form must be given already stripped. क्विन् (3.2.58) and ण्वि (3.2.62)
    are the Kāśikā's examples, giving घृतस्पृक् and अर्धभाक्, and both reduce
    to व् — but only after the उच्चारणार्थ vowel goes, which no rule codified
    here removes. See the note on 1.3.9.
    """
    return len(scan_phonemes(affix)) == 1


# ---------------------------------------------------------------------------
# 1.2.42 कर्मधारय, 1.2.43 and 1.2.44 उपसर्जन
# ---------------------------------------------------------------------------


def karmadharaya(*, tatpurusa: bool, samanadhikarana: bool) -> bool:
    """
    1.2.42 तत्पुरुषः समानाधिकरणः कर्मधारयः.

    Both conditions, and the Kāśikā tests both. तत्पुरुष इति किम्?
    पाचिकाभार्यः — a bahuvrīhi with one referent is not this.
    समानाधिकरण इति किम्? ब्राह्मणराज्यम् — a tatpuruṣa whose members denote
    different things is not either. परमराज्यम् and उत्तमराज्यम् are.

    अधिकरणशब्दोऽभिधेयवाची, समानाधिकरणः समानाभिधेयः — "same locus" means
    "denoting the same thing", which is why this takes a flag and not two
    words: the question is semantic.
    """
    return tatpurusa and samanadhikarana


def upasarjana(
    sutra_id: str, *, ekavibhakti: bool = False, purvanipata: bool = False
) -> "Tuple[str, ...]":
    """
    1.2.43 with 1.2.44 — which word of a compound-rule names the upasarjana.

    प्रथमया विभक्त्या यद् निर्दिश्यते समासशास्त्रे तदुपसर्जनसंज्ञं भवति: what
    the rule states in the first case. So 2.1.24 द्वितीया श्रितातीतपतित... has
    द्वितीया in the first case, and that is the upasarjana, giving कष्टश्रितः;
    and so through तृतीया, चतुर्थी, पञ्चमी, षष्ठी and सप्तमी for their
    compounds — शङ्कुलाखण्डः, यूपदारु, वृकभयम्, राजपुरुषः, अक्षशौण्डः.

    1.2.44 adds a second ground: something that keeps ONE case-ending while its
    partner varies — एका विभक्तिर्यस्य तदिदमेकविभक्ति — except for the
    operation of being placed first. निष्कौशाम्बिः, निष्कौशाम्बिम् — the first
    member varies and the second stays ablative.
    """
    from src.astadhyayi.adesa import prathama_padas

    found = list(prathama_padas(sutra_id))
    if ekavibhakti and not purvanipata:
        found.append("(ekavibhakti, by 1.2.44)")
    return tuple(found)


# ---------------------------------------------------------------------------
# 1.2.45, 1.2.46 प्रातिपदिक
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Pratipadika:
    """That a form bears the name, and which of the two sūtras gave it."""

    by: str
    why: str


def pratipadika(
    form: str,
    *,
    arthavat: bool = True,
    dhatu: bool = False,
    pratyaya: bool = False,
    krdanta: bool = False,
    taddhitanta: bool = False,
    samasa: bool = False,
    nipata: bool = False,
    vakya: bool = False,
) -> "Optional[Pratipadika]":
    """
    1.2.45 with 1.2.46 — the stem a nominal ending attaches to.

    Three conditions in the first sūtra and the Kāśikā tests each:
      अर्थवदिति किम्? वनम्, धनम् — so that the -अन् that is no part of the
        meaning does not get the name and lose its न् by नलोप.
      अधातुरिति किम्? अहन्, हन्ति in the imperfect — again to save the न्.
      अप्रत्यय इति किम्? काण्डे, कुड्ये — else 1.2.47 would shorten them.

    1.2.46 then puts back what अप्रत्ययः had excluded:
    अप्रत्ययः इति पूर्वसूत्रे पर्युदासात् कृदन्तस्य तद्धितान्तस्य च अनेन
    प्रातिपदिकसंज्ञा विधीयते. कारकः, हारकः for the kṛt; औपगवः, कापटवः for the
    taddhita; राजपुरुषः, ब्राह्मणकम्बलः for the compound.

    समासग्रहणं नियमार्थम् — naming the compound is a RESTRICTION, not an
    addition: it is there so that a meaningful phrase, which would otherwise
    qualify under 1.2.45, does not. Hence `vakya`.
    """
    if krdanta or taddhitanta or samasa:
        return Pratipadika(
            "1.2.46",
            "कृत्तद्धितसमासाश्च — 1.2.45's अप्रत्ययः would have excluded a "
            "kṛt- or taddhita-final, and this admits them: कारकः, औपगवः, "
            "राजपुरुषः",
        )
    if vakya:
        return None     # समासग्रहणं नियमार्थम्
    if nipata:
        return Pratipadika(
            "1.2.45",
            "a nipāta, by the vārttika निपातस्यानर्थकस्य प्रातिपदिकसंज्ञा "
            "वक्तव्या — even a meaningless one takes the name: अध्यागच्छति, "
            "प्रलम्बते",
        )
    if arthavat and not dhatu and not pratyaya:
        return Pratipadika(
            "1.2.45",
            "अर्थवत्, and neither a root nor an affix: डित्थः, कपित्थः, "
            "कुण्डम्, पीठम्",
        )
    return None


def is_pratipadika(form: str, **conditions) -> bool:
    return pratipadika(form, **conditions) is not None


# ---------------------------------------------------------------------------
# 1.3.1 भूवादयो धातवः
# ---------------------------------------------------------------------------


def is_dhatu(form: str) -> bool:
    """
    1.3.1: भू and the words enumerated after it are called धातु (dhātu), roots.

    भू इत्येवमादयः शब्दाः क्रियावचना धातुसंज्ञा भवन्ति — the words beginning
    with भू, that denote an action, bear the name. The list is the dhātupāṭha,
    a separate text, and it is on disk: 2,259 roots, of which the Kāśikā's first
    three examples are entries 1, 2 and 3 — भू giving भवति, एध giving एधते,
    स्पर्ध giving स्पर्धते.

    Matched on the enunciated form, so डुकृञ् and कृ are the same root asked
    for two ways.
    """
    from src.astadhyayi.corpus import load_dhatupatha
    from src.astadhyayi.itsamjna import DHATU, analyze

    bare = form.replace("̐", "")
    for entry in load_dhatupatha().values():
        enunciated = entry.upadesa.replace("̐", "")
        if bare == enunciated:
            return True
        if bare == analyze(entry.upadesa, DHATU).stem.replace("̐", ""):
            return True
    return False


def dhatu_count() -> int:
    """How many roots the enumeration holds."""
    from src.astadhyayi.corpus import load_dhatupatha

    return len(load_dhatupatha())
