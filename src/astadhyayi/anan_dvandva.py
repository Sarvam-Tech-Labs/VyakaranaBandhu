# -*- coding: utf-8 -*-
"""
६.३.२५–३३ — आनङ् and the द्वन्द्व substitutions.

6.3.25 आनङ् ऋतो द्वन्द्वे ends the अलुक् heading and starts a
different kind of rule. Where 6.3.1–24 kept an ending that was due
to go, these nine REPLACE the first member outright, and every one
of them is about a द्वन्द्व.

Two classes of द्वन्द्व, and one substitution apiece:

**ऋ-final words of learning and birth** take आनङ् — होतापोतारौ,
मातापितरौ. It is the same class 6.3.23 and 6.3.24 had just been
keeping a genitive for, carried straight down; and the word पुत्र
carries down too, so पितापुत्रौ goes the same way.

**And the gods.** 6.3.26 gives them आनङ् as well — इन्द्रावरुणौ —
and then five sūtras replace particular gods with particular forms:
अग्नि becomes ई before सोम and वरुण, and इ where a वृद्धि has
already been made; दिव् becomes द्यावा, and दिवस् before पृथिवी;
उषस् becomes उषासा; and मातृ becomes मातर on the northerners'
authority, or पितरा in the Veda with the members reversed.

**AND THE WORD द्वन्द्व IS SAID TWICE FOR A REASON.** 6.3.26's
vṛtti: **द्वन्द्व इति वर्तमाने पुनर्द्वन्द्वग्रहणं
प्रसिद्धसाहचर्यार्थम्। अत्यन्तसहचरिते लोकविज्ञाते द्वन्द्वम्
इत्येतद् निपात्यते** — repeating a word already running can only
narrow it, and what it narrows to is the pairs that are ALREADY
paired in usage. So इन्द्रावरुणौ and not *ब्रह्मप्रजापती.

**WHAT THIS MODULE DOES NOT DO.** It reports which substitute the
first member takes and by which rule. It does not build the form:
that आनङ् then meets 6.1.87's एकादेश, and that अग्नीषोमौ gets its
ष् from 8.3.82, are other rules' business.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these nine stand — opened by 6.3.25, which is itself the
#: bound 6.3.1's अलुक् was read against (**अलुगधिकारः प्रागानङः**).
ANAN_RUN: Tuple[str, str] = ("6.3.25", "6.3.33")

#: The class 6.3.23 named and 6.3.25 inherits: ऋ-final words for a
#: relation of learning or of birth. The vṛtti's own examples.
RTA_VIDYA: Tuple[str, ...] = (
    "hotṛ", "potṛ", "neṣṭṛ", "udgātṛ", "praśāstṛ", "pratihartṛ")
RTA_YONI: Tuple[str, ...] = (
    "mātṛ", "pitṛ", "yātṛ", "nanāndṛ", "duhitṛ")

#: And the word 6.3.25's vṛtti says carries down from 6.3.22:
#: **पुत्र इत्यनुवर्तते, ऋत इति च। तेन पुत्रशब्देऽप्युत्तरपद
#: ऋकारान्तस्यानङादेशो भवति — पितापुत्रौ, मातापुत्रौ**.
PUTRA_CARRIES: Tuple[str, ...] = ("putra",)

#: What 6.3.26's repeated द्वन्द्व keeps out — pairs nobody pairs.
NOT_PAIRED: Tuple[str, ...] = (
    "brahma-prajāpati", "śiva-vaiśravaṇa")

#: And what a vārttika keeps out in either order:
#: **उभयत्र वायोः प्रतिषेधो वक्तव्यः — अग्निवायू, वाय्वग्नी**.
VAYU_VARTIKA: Tuple[str, ...] = ("vāyu",)


@dataclass(frozen=True)
class Anan:
    """One rule of 6.3.25–33: what the first member becomes."""

    sutra: str
    #: The substitute — ānaṅ, ī, i, dyāvā, divas, uṣāsā, mātara,
    #: pitarā-mātarā.
    becomes: str = ""
    #: The first members the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of first member instead.
    gana: str = ""
    #: The second members that must follow.
    uttarapada: Tuple[str, ...] = ()
    #: The kind of द्वन्द्व — ṛd-anta or devatā.
    dvandva: str = ""
    #: A further condition: वृद्धि already made, the Veda, the
    #: northerners' usage.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    chandasi: bool = False
    #: True where the form is laid down whole rather than derived.
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ANAN_TABLE: Tuple[Anan, ...] = (
    Anan(
        "6.3.25", becomes="ānaṅ", gana="ṛd-anta-vidyā-yoni",
        dvandva="ṛd-anta",
        keeps_out="पितृपितामहौ — पितामह does not end in ऋ",
        why="आनङ् ऋतो द्वन्द्वे — in a द्वन्द्व of ऋ-final words "
            "for a relation of LEARNING or of BIRTH, the first "
            "member takes आनङ्: **होतापोतारौ, नेष्टोद्गातारौ, "
            "प्रशास्ताप्रतिहर्तारौ** for learning; **मातापितरौ, "
            "याताननान्दरौ** for birth.\\n\\n"
            "**AND THE न् IS THERE TO STOP SOMETHING.** "
            "**नकारोच्चारणं रपरत्वनिवृत्त्यर्थम्** — without it, "
            "1.1.51 उरण् रपरः would make the substitute for an ऋ "
            "carry a र् after it. Marking the substitute आनङ् "
            "rather than आन् is what keeps the र् out.\\n\\n"
            "**AND ONE WORD CARRIES DOWN FROM THE अलुक् RUN.** "
            "**पुत्र इत्यनुवर्तते, ऋत इति च। तेन पुत्रशब्देऽपि "
            "उत्तरपद ऋकारान्तस्यानङादेशो भवति — पितापुत्रौ, "
            "मातापुत्रौ** — पुत्र was last said at 6.3.22, two "
            "sūtras before the heading changed, and it is still "
            "running"),
    Anan(
        "6.3.26", becomes="ānaṅ", dvandva="devatā",
        excludes=NOT_PAIRED + VAYU_VARTIKA,
        keeps_out="ब्रह्मप्रजापती, शिववैश्रवणौ — gods, but not a "
                  "pair anyone pairs; अग्निवायू and वाय्वग्नी — "
                  "the vārttika's **उभयत्र वायोः प्रतिषेधः**",
        why="देवताद्वन्द्वे च — and in a द्वन्द्व of GODS: "
            "**इन्द्रावरुणौ, इन्द्रासोमौ, इन्द्राबृहस्पती**.\\n\\n"
            "**AND SAYING द्वन्द्व AGAIN IS WHAT NARROWS IT.** "
            "**द्वन्द्व इति वर्तमाने पुनर्द्वन्द्वग्रहणं "
            "प्रसिद्धसाहचर्यार्थम्। अत्यन्तसहचरिते लोकविज्ञाते "
            "द्वन्द्वम् इत्येतद् निपात्यते** — the word was "
            "already running from 6.3.25, so repeating it can only "
            "restrict, and what it restricts to is the pairs "
            "usage has ALREADY paired: **तत्र ये लोके "
            "प्रसिद्धसाहचर्या वेदे च ये सहवापनिर्दिष्टास्तेषाम् "
            "इह ग्रहणं भवति। तेन ब्रह्मप्रजापती, "
            "शिववैश्रवणावित्येवमादौ न भवति**. Two gods are not "
            "enough; they have to be a pair"),
    Anan(
        "6.3.27", becomes="ī", of=("agni",),
        uttarapada=("soma", "varuṇa"), dvandva="devatā",
        blocks=("6.3.26",),
        why="ईदग्नेः सोमवरुणयोः — but अग्नि becomes ई before सोम "
            "and वरुण: **अग्नीषोमौ, अग्नीवरुणौ**. The ष् of the "
            "first is not this rule's: **अग्नेःस्तुत्स्तोमसोमाः "
            "इति षत्वम्**, by 8.3.82"),
    Anan(
        "6.3.28", becomes="i", of=("agni",), dvandva="devatā",
        result=("vṛddhi",), excludes=("viṣṇu",),
        blocks=("6.3.26", "6.3.27"),
        keeps_out="आग्नेन्द्रः — not excluded by name, but 7.3.22 "
                  "नेन्द्रस्य परस्य refuses the second member's "
                  "वृद्धि, so the condition never arises and "
                  "6.3.26's आनङ् stands; आग्नावैष्णवम् — विष्णु, "
                  "which IS excluded by name, by a vārttika",
        why="इद् वृद्धौ — and अग्नि becomes इ where a वृद्धि has "
            "ALREADY been made in the second member: "
            "**आग्निवारुणीम् अनड्वाहीम् आलभेत; आग्निमारुतं कर्म "
            "क्रियते**.\\n\\n"
            "**AND IT IS STATED TO DEFEAT TWO RULES AT ONCE.** "
            "**तत्र देवताद्वन्द्वे च इत्युभयपदवृद्धौ कृतायाम् "
            "आनङम् ईत्वं च बाधितुम् इकारः क्रियते** — 7.3.21 has "
            "strengthened both members, and this इ then displaces "
            "both 6.3.26's आनङ् and 6.3.27's ई. A substitute whose "
            "whole purpose is to arrive after another rule has "
            "acted.\\n\\n"
            "**AND ONE GOD IS TAKEN BACK OUT BY A VĀRTTIKA.** "
            "**इद् वृद्धौ विष्णोः प्रतिषेधो वक्तव्यः — "
            "आग्नावैष्णवम् एकादशकपालं निर्वपेत्** — with विष्णु "
            "the आनङ् stands after all, वृद्धि or no वृद्धि. "
            "इन्द्र is a different case and is NOT named out: "
            "**वृद्धाविति किम्? आग्नेन्द्रः। नेन्द्रस्य परस्य "
            "इत्युत्तरपदवृद्धिः प्रतिषिध्यते** — there 7.3.22 "
            "refuses the strengthening, so the condition this "
            "rule wants never arises"),
    Anan(
        "6.3.29", becomes="dyāvā", of=("div",), dvandva="devatā",
        why="देवो द्यावा — दिव् becomes द्यावा in a द्वन्द्व of "
            "gods: **द्यावाक्षामा, द्यावाभूमी**. The sūtra says "
            "देवः for दिव् — the stem in its other shape — and "
            "the vṛtti reads it straight: **दिवित्येतस्य द्यावा "
            "इत्ययमादेशो भवति**"),
    Anan(
        "6.3.30", becomes="divas", of=("div",),
        uttarapada=("pṛthivī",), dvandva="devatā",
        why="दिवसश्च पृथिव्याम् — and दिव् becomes दिवस् before "
            "पृथिवी, **चकाराद् द्यावा च** — so both **दिवस्पृथिव्यौ** "
            "and **द्यावापृथिव्यौ** stand.\\n\\n"
            "**AND THE अ OF दिवस् IS THERE TO STOP THE स् FROM "
            "CHANGING.** **अकारोच्चारणं सकारस्य "
            "विकाराभावप्रतिपत्त्यर्थम्। तेन रुत्वादीनि न भवन्ति** "
            "— written दिवस् rather than दिवश्, the स् is not the "
            "kind of final that 8.2.66 turns to रु. And the vṛtti "
            "leaves one form unexplained: **कथं द्यावा चिदस्मै "
            "पृथिवी नमेते इति? कर्तव्योऽत्र यत्नः**"),
    Anan(
        "6.3.31", becomes="uṣāsā", of=("uṣas",), dvandva="devatā",
        why="उषासोषसः — उषस् becomes उषासा in a द्वन्द्व of gods: "
            "**उषासासूर्यम्, उषासानक्ता** — Dawn and the Sun, "
            "Dawn and Night"),
    Anan(
        "6.3.32", becomes="mātara", of=("mātṛ",),
        uttarapada=("pitṛ",), result=("udīcām",), nipatana=True,
        keeps_out="मातापितरौ — the general form, by 6.3.25",
        why="मातरपितरावुदीचाम् — मातृ becomes मातर before पितृ on "
            "the NORTHERNERS' authority: "
            "**मातरपितरावित्युदीचामाचार्याणां मतेनारङादेशो "
            "मातृशब्दस्य निपात्यते**. Laid down whole rather than "
            "derived, and credited to a school by name — "
            "**उदीचामिति किम्? मातापितरौ**, which is what everyone "
            "else says"),
    Anan(
        "6.3.33", becomes="pitarā-mātarā", of=("pitṛ",),
        uttarapada=("mātṛ",), chandasi=True, nipatana=True,
        keeps_out="मातापितरौ — outside the Veda, and in the other "
                  "order",
        why="पितरामातरा च छन्दसि — and in the Veda the pair is "
            "laid down the other way round: **आ मा गन्तां "
            "पितरामातरा च**.\\n\\n"
            "**AND ONLY THE FIRST HALF IS THE निपातन.** "
            "**पूर्वपदस्याराङादेशो निपात्यते। उत्तरपदे तु सुपां "
            "सुलुक्० इति आकारादेशः। तत्र ऋतो ङिसर्वनामस्थानयोः "
            "इति गुणः** — पितरा is laid down, but the मातरा that "
            "follows is built: 7.1.39 gives the आ and 7.3.110 the "
            "guṇa. Half a निपातन and half a derivation, in one "
            "word"),
)


def _reaches(row: Anan, purvapada: str, gana: str, uttarapada: str,
             dvandva: str, result: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (purvapada in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.uttarapada and uttarapada not in row.uttarapada:
        return False
    if row.dvandva and dvandva != row.dvandva:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.excludes and (purvapada in row.excludes
                         or uttarapada in row.excludes):
        return False
    return True


def _supplies(row: Anan, wants: str) -> bool:
    return not wants or wants == row.becomes


def _how_specific(row: Anan, purvapada: str, gana: str,
                  uttarapada: str) -> int:
    """
    A rule that names the stem beats one that names only the kind
    of द्वन्द्व, and naming the following word beats both.

    6.3.26 reaches every pair of gods; 6.3.27 reaches अग्नि before
    two of them; 6.3.28 reaches अग्नि once a वृद्धि has been made
    and beats both. The order the vṛtti argues — **आनङम् ईत्वं च
    बाधितुम्** — has to fall out of the score, and by conditions
    alone it does not: 6.3.27 names a following word and 6.3.28
    does not, so it would win on sharpness. What settles it is
    that 6.3.28 SAYS what it displaces, and a rule that names two
    rules it defeats has to outrank both.
    """
    return (
        4 * len(row.blocks)
        + 8 * bool(row.uttarapada and uttarapada in row.uttarapada)
        + 7 * bool(row.of and purvapada in row.of)
        + 6 * bool(row.result)
        + 5 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.chandasi)
        + 2 * bool(row.dvandva)
    )


@dataclass(frozen=True)
class Replaced:
    """What the run answers: a substitute, and by which rule."""

    becomes: str
    sutra: str
    why: str
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def substitute(purvapada: str = "", *, gana: str = "",
               uttarapada: str = "", dvandva: str = "",
               result: str = "", chandasi: bool = False,
               wants: str = "") -> Replaced:
    """
    6.3.25–33 — what the first member of a द्वन्द्व becomes.

    Nothing answers by default: where no rule is reached the first
    member stands as it is, and the compound is formed with no
    substitution at all.
    """
    matched = [
        row for row in ANAN_TABLE
        if _reaches(row, purvapada, gana, uttarapada, dvandva,
                    result, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Replaced(
            "", "", "No rule of 6.3.25–33 is reached, so the first "
                    "member is not replaced and stands as it is")
    row = max(matched, key=lambda one: _how_specific(
        one, purvapada, gana, uttarapada))
    return Replaced(row.becomes, row.sutra, row.why,
                    nipatana=row.nipatana, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Anan, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ANAN_TABLE if row.sutra == sutra_id)


__all__ = [
    "Anan", "ANAN_TABLE", "ANAN_RUN", "RTA_VIDYA", "RTA_YONI",
    "PUTRA_CARRIES", "NOT_PAIRED", "VAYU_VARTIKA", "Replaced",
    "substitute", "provisions_for",
]
