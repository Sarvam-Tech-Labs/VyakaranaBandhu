# -*- coding: utf-8 -*-
"""
७.३.१०१–१२० — the अ lengthened, and the case ending's augments.

Twenty sūtras closing पाद ७.३, and between them they finish the
declension the pāda before began. An अ-final stem lengthens
before a य् or a nasal — पचामि, वृक्षाय, वृक्षाभ्याम् — and
becomes ए before a झल्-initial plural and before ओस् —
वृक्षेभ्यः, वृक्षेषु, वृक्षयोः.

**AND THE VOCATIVE GETS FOUR SŪTRAS AND AN ARGUMENT.** 7.3.106
gives an आप्-final stem ए (हे खट्वे), 7.3.107 shortens the
अम्बा-words and the नदी stems (हे अम्ब, हे कुमारि), and 7.3.108
gives a short-final stem guṇa (हे अग्ने, हे वायो). The vṛtti then
shows that the third cannot reach the second's stems, and gives
the reason as an argument from how Pāṇini would have written it
otherwise.

**AND THE LAST FIVE ARE AUGMENTS TO THE ENDING AND NOT THE
STEM.** आट् after a नदी (कुमार्यै), याट् after आप् (खट्वायै),
स्याट् after a pronoun (सर्वस्यै), and then ङि becomes आम्
(कुमार्याम्), औ (सख्यौ), or ना (अग्निना). पाद ७.३ ends where a
noun's declension does.

**WHAT THIS MODULE DOES NOT DO.** It says what the stem and the
ending become. What the ending was is 4.1.2's, and 7.1.9–33 may
already have replaced it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch, closing पाद ७.३.
DIRGHA_RUN: Tuple[str, str] = ("7.3.101", "7.3.120")

#: Where the run stops being about the stem's own vowel.
AUGMENTS_FROM: str = "7.3.112"

#: 7.3.101 and 7.3.107 were codified long before this pāda was
#: read through; both stay where they were.
CODIFIED_APART: Tuple[str, ...] = ("7.3.101",)

#: 7.3.107's own two classes: the words for *mother* and the
#: नदी stems, both shortened in the vocative.
AMBA_NADI: Tuple[str, ...] = ("ambā-artha", "nadī-anta")

#: 7.3.116–120's five answers for ङि, each after its own stem.
NGI_FIVE: Tuple[Tuple[str, str], ...] = (
    ("nadī-āp-nī", "ām"), ("id-ud-nadī", "ām"),
    ("id-ud", "au"), ("ghi", "au-ac"), ("ghi-a-strī", "nā"))


@dataclass(frozen=True)
class Dirgha:
    """One rule of 7.3.101–120: a lengthening, or an augment."""

    sutra: str
    #: `dīrgha`, `et`, `hrasva`, `guṇa`, or the augment's name.
    does: str = ""
    #: The stems named outright.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: The gender, where the rule wants one.
    gender: str = ""
    #: True where the rule supplies an आगम to the ENDING.
    augment: bool = False
    #: True where the rule also shortens the stem.
    also_shortens: bool = False
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


DIRGHA_TABLE: Tuple[Dirgha, ...] = (
    Dirgha(
        "7.3.101", does="dīrgha", gana="a-anta",
        before=("yañ-ādi-sārvadhātuka",),
        keeps_out="चिनुवः, चिनुमः — the stem is not अ-final; "
                  "पचतः, पचथः — the ending begins with neither "
                  "य् nor a nasal; अङ्गना, केशवः — no "
                  "सार्वधातुक at all",
        why="अतो दीर्घो यञि — an अ-final stem lengthens before a "
            "सार्वधातुक beginning with a य् or a nasal: "
            "**पचामि, पचावः, पचामः; पक्ष्यामि, पक्ष्यावः, "
            "पक्ष्यामः**. Some read तिङि down into it, and on "
            "that reading भववान् keeps its short vowel"),
    Dirgha(
        "7.3.102", does="dīrgha", gana="a-anta",
        before=("yañ-ādi-sup",),
        keeps_out="अग्निभ्याम् — not अ-final; वृक्षस्य, "
                  "प्लक्षस्य — the ending begins with स्",
        why="सुपि च — and before such a CASE ending: **वृक्षाय, "
            "प्लक्षाय; वृक्षाभ्याम्, प्लक्षाभ्याम्**. This is "
            "the lengthening 7.1.13's ङेर्यः needed and could "
            "not state, being about the ending and not the stem"),
    Dirgha(
        "7.3.103", does="et", gana="a-anta",
        before=("jhal-ādi-bahuvacana-sup",), blocks=("7.3.102",),
        keeps_out="वृक्षाभ्याम् — a dual and not a plural; "
                  "वृक्षाणाम् — the ending does not begin with a "
                  "झल्; यजध्वम्, पचध्वम् — a personal ending "
                  "and no सुप्",
        why="बहुवचने झल्येत् — and becomes ए before a "
            "झल्-initial PLURAL case ending: **वृक्षेभ्यः, "
            "प्लक्षेभ्यः; वृक्षेषु, प्लक्षेषु**"),
    Dirgha(
        "7.3.104", does="et", gana="a-anta", before=("os",),
        blocks=("7.3.102",),
        why="ओसि च — and before ओस्: **वृक्षयोः स्वम्, प्लक्षयोः "
            "स्वम्; वृक्षयोर् निधेहि, प्लक्षयोर् निधेहि**. The "
            "ओस् is the ending of two cases at once, the "
            "genitive and the locative dual, and the vṛtti gives "
            "an example of each rather than leaving the reader "
            "to supply the second"),
    Dirgha(
        "7.3.105", does="et", gana="āp-anta",
        before=("āṅ", "os"),
        keeps_out="कीलालपा ब्राह्मणेन — the आ is a root's and no "
                  "आप्; अतिखट्वेन ब्राह्मणकुलेन — the shortened "
                  "आप् of a compound, which a maxim shuts out",
        why="आङि चापः — an आप्-final stem becomes ए before the "
            "instrumental singular and before ओस्: **खट्वया, "
            "मालया; खट्वयोः, मालयोः; बहुराजया, "
            "कारीषगन्ध्यया**. आङ् is the older teachers' name "
            "for that ending — **आङिति पूर्वाचार्यनिर्देशेन "
            "तृतीयैकवचनं गृह्यते**"),
    Dirgha(
        "7.3.106", does="et", gana="āp-anta",
        before=("sambuddhi",),
        why="सम्बुद्धौ च — and in the vocative singular: **हे "
            "खट्वे; हे बहुराजे; हे कारीषगन्ध्ये**. **आप इति "
            "वर्तते** — the आप् is carried down from the sūtra "
            "before, so a stem whose आ is a root's own is not "
            "reached, and this is the first of the four rules "
            "the vocative gets"),
    Dirgha(
        "7.3.107", does="hrasva", gana="ambā-artha-nadī",
        before=("sambuddhi",),
        keeps_out="हे अम्बाडे, हे अम्बाले, हे अम्बिके — a "
                  "vārttika keeps the ड, ल and क words out",
        why="अम्बाऽर्थनद्योर्ह्रस्वः — the words for MOTHER and "
            "the नदी stems shorten in the vocative: **हे अम्ब, "
            "हे अक्क, हे अल्ल; हे कुमारि, हे शार्ङ्गरवि, हे "
            "ब्रह्मबन्धु, हे वीरबन्धु**. Two vārttikas add the "
            "exceptions and then make them optional in the Veda, "
            "and a third takes in the तल्-final stems: "
            "**तलो ह्रस्वो वा ङिसंबुद्ध्योः**"),
    Dirgha(
        "7.3.108", does="guṇa", gana="hrasva-anta",
        before=("sambuddhi",), blocks=("7.3.107",),
        why="ह्रस्वस्य गुणः — a short-final stem takes guṇa in "
            "the vocative: **हे अग्ने, हे वायो, हे पटो**.\\n\\n"
            "**AND IT CANNOT REACH THE STEMS THE SŪTRA BEFORE "
            "SHORTENED.** हे कुमारि and हे ब्रह्मबन्धु keep "
            "their short vowels — **ह्रस्वविधानसामर्थ्याद् गुणो "
            "न भवति**, the shortening would be pointless if the "
            "guṇa followed it. And the vṛtti proves it from how "
            "Pāṇini would have written the pair otherwise: "
            "**यदि गुण इष्टः स्यात्, अम्बार्थानां ह्रस्व "
            "इत्युक्त्वा नदीह्रस्वयोर् गुण इत्येवं ब्रूयात्**"),
    Dirgha(
        "7.3.109", does="guṇa", gana="hrasva-anta",
        before=("jas",),
        why="जसि च — and before जस्: **अग्नयः, वायवः, पटवः, "
            "धेनवः, बुद्धयः**. A vārttika makes everything from "
            "here to 7.4.1 optional in the Veda — "
            "**इतः प्रकरणात् प्रभृति छन्दसि वेति वक्तव्यम्** — "
            "which is how अम्बे beside अम्ब and शतक्रत्वः beside "
            "शतक्रतवः both stand"),
    Dirgha(
        "7.3.110", does="guṇa", gana="ṛ-anta",
        before=("ṅi", "sarvanāmasthāna"),
        why="ऋतो ङिसर्वनामस्थानयोः — an ऋ-final stem takes guṇa "
            "before ङि and before a strong ending: **मातरि, "
            "पितरि, भ्रातरि, कर्तरि**; **कर्तारौ, कर्तारः, "
            "मातरौ, पितरौ**"),
    Dirgha(
        "7.3.111", does="guṇa", gana="ghi", before=("ṅit",),
        keeps_out="सख्ये, पत्ये — not घि; अग्निभ्याम् — the "
                  "ending is not ङित्; पट्वी, कुरुतः — no "
                  "सुप् at all",
        why="घेर्ङिति — a घि stem takes guṇa before a ङित् "
            "ending: **अग्नये, वायवे; अग्नेर् आगच्छति, वायोर् "
            "आगच्छति; अग्नेः स्वम्, वायोः स्वम्**"),
    Dirgha(
        "7.3.112", does="āṭ", gana="nadī-anta", before=("ṅit",),
        augment=True,
        why="आण्नद्याः — after a नदी stem the ङित् ending takes "
            "the augment आट्: **कुमार्यै, ब्रह्मबन्ध्वै; "
            "कुमार्याः, ब्रह्मबन्ध्वाः**. From here the run is "
            "about the ENDING and not the stem"),
    Dirgha(
        "7.3.113", does="yāṭ", gana="āp-anta", before=("ṅit",),
        augment=True,
        keeps_out="अतिखट्वया — the shortened आप् of a compound, "
                  "which a maxim shuts out before the "
                  "lengthening is done",
        why="याडापः — and after an आप् stem, याट्: **खट्वायै, "
            "बहुराजायै, कारीषगन्ध्यायै; खट्वायाः, "
            "बहुराजायाः**. And whether अतिखट्वा takes it turns "
            "on when the lengthening is done: **अकृते दीर्घे "
            "ङ्याब्ग्रहणेऽदीर्घः इति वचनाद् याडागमो न भवति, "
            "कृते तु लाक्षणिकत्वात्** — before it, no; after "
            "it, yes"),
    Dirgha(
        "7.3.114", does="syāṭ", gana="sarvanāma-āp",
        before=("ṅit",), augment=True, also_shortens=True,
        blocks=("7.3.113",),
        keeps_out="भवति, भवते — no आप्",
        why="सर्वनाम्नः स्याड्ढ्रस्वश्च — after an आप्-final "
            "PRONOUN the ending takes स्याट् AND the stem "
            "shortens: **सर्वस्यै, विश्वस्यै, यस्यै, तस्यै, "
            "कस्यै; सर्वस्याः, यस्याः, कस्याः**. Two operations "
            "in one sūtra, and the shortening is what makes the "
            "स्याट् audible"),
    Dirgha(
        "7.3.115", does="syāṭ", of=("dvitīya", "tṛtīya"),
        before=("ṅit",), augment=True, also_shortens=True,
        optional=True, blocks=("7.3.114",),
        why="विभाषा द्वितीयातृतीयाभ्याम् — and after द्वितीय and "
            "तृतीय it is OPTIONAL, with the same shortening: "
            "**द्वितीयस्यै, द्वितीयायै; तृतीयस्यै, "
            "तृतीयायै**"),
    Dirgha(
        "7.3.116", does="ām", gana="nadī-āp-nī", before=("ṅi",),
        why="ङेराम्नद्याम्नीभ्यः — after a नदी stem, an आप् stem "
            "and नी, the locative singular ङि becomes आम्: "
            "**कुमार्याम्, गौर्याम्, ब्रह्मबन्ध्वाम्** for the "
            "नदी; **खट्वायाम्, बहुराजायाम्** for the आप्; "
            "**राजन्याम्, सेनान्याम्, ग्रामण्याम्** for नी"),
    Dirgha(
        "7.3.117", does="ām", gana="id-ud-nadī", before=("ṅi",),
        why="इदुद्भ्याम् — and after an इ or उ that is a नदी: "
            "**कृत्याम्, धेन्वाम्**. The sūtra before had "
            "reached the नदी stems by that name; this one names "
            "the two vowels, and what it adds is the stems that "
            "are नदी by 1.4.6's option rather than by 1.4.3"),
    Dirgha(
        "7.3.118", does="au", gana="id-ud", before=("ṅi",),
        blocks=("7.3.117",),
        why="औत् — and after an इ or उ that is NEITHER a नदी nor "
            "a घि, the ङि becomes औ: **सख्यौ, पत्यौ**. The "
            "sūtra is one word, and what it reaches is what the "
            "two rules before it left"),
    Dirgha(
        "7.3.119", does="au-ac", gana="ghi", before=("ṅi",),
        also_shortens=True, blocks=("7.3.118",),
        why="अच्च घेः — and after a घि stem the ङि becomes औ AND "
            "the घि's own vowel becomes अ: **अग्नौ, वायौ, "
            "कृतौ, धेनौ, पटौ**. The तपर keeps the feminine's "
            "टाप् out. Some read this and the sūtra before as "
            "ONE rule — **औदच्च घेरिति येषाम् एकम् एवेदं "
            "सूत्रम्** — and then the औ is the main provision "
            "and the अ an afterthought to it"),
    Dirgha(
        "7.3.120", does="nā", gana="ghi", before=("āṅ",),
        gender="a-strī",
        keeps_out="कृत्या, धेन्वा — feminine, and the rule wants "
                  "anything but",
        why="आङो नाऽस्त्रियाम् — and after a घि stem the "
            "instrumental singular becomes ना, except in the "
            "feminine: **अग्निना, वायुना, पटुना**. The sūtra "
            "says *not feminine* rather than *masculine* on "
            "purpose — **पुंसि इति नोक्तम् — अमुना "
            "ब्राह्मणकुलेन**, since a neuter needs it too. This "
            "closes पाद ७.३: **इति श्रीवामनविरचितायां काशिकायां "
            "वृत्तौ सप्तमाध्यायस्य तृतीयः पादः**"),
)


def _reaches(row: Dirgha, stem: str, gana: str, before: str,
             gender: str) -> bool:
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.gender and gender != row.gender:
        return False
    return True


def _how_specific(row: Dirgha, stem: str, gana: str) -> int:
    """
    A rule that names what it displaces beats it, a named stem
    beats a class, and a named gender beats both.

    7.3.116 to 7.3.120 are the five that need it: all name the
    locative singular, and they are told apart only by what
    stands in front of it.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of and stem in row.of)
        + 6 * bool(row.gender)
        + 5 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.before)
    )


@dataclass(frozen=True)
class Made:
    """What the run answers: a change in the stem, or an augment."""

    does: str
    sutra: str
    why: str
    augment: bool = False
    also_shortens: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_ending(stem: str = "", *, gana: str = "",
                  before: str = "", gender: str = "") -> Made:
    """
    7.3.101–120 — the stem's vowel, and the ending's augment.

    Nothing answers by default. A consonant-final stem before a
    consonant-initial ending takes nothing from this run, which
    is why राजभिः looks the way it does.
    """
    matched = [row for row in DIRGHA_TABLE
               if _reaches(row, stem, gana, before, gender)]
    if not matched:
        return Made(
            "", "", "No rule of 7.3.101-120 is reached, so the "
                    "stem and the ending stand as they are")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Made(row.does, row.sutra, row.why, augment=row.augment,
                also_shortens=row.also_shortens,
                optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Dirgha, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in DIRGHA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Dirgha", "DIRGHA_TABLE", "DIRGHA_RUN", "AUGMENTS_FROM",
    "CODIFIED_APART", "AMBA_NADI", "NGI_FIVE", "Made",
    "before_ending", "provisions_for",
]
