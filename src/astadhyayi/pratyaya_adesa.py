# -*- coding: utf-8 -*-
"""
७.१.१–८ — what an affix is replaced by, in itself.

अध्याय ७ opens on the affix rather than the stem. Eight sūtras,
and every one of them changes a sound INSIDE the affix before the
affix has done anything: यु becomes अन and वु becomes अक, so
नन्दि + ल्यु is नन्दनः and कृ + ण्वुल् is कारकः; फ ढ ख छ घ at the
head of a taddhita become आयन् एय् ईन् ईय् इय्, so नड + फक् is
नाडायनः and क्षत्र + घ is क्षत्रियः.

**THE AFFIXES ARE NAMED IN A SHAPE THEY ARE NEVER SEEN IN.**
ल्यु, ट्यु, ण्वुल्, वुन् are all taught with यु or वु in them and
not one of them is ever pronounced so. The Kāśikā says why the
rule can be stated at all: **अनुनासिकयणोः प्रत्यययोर्ग्रहणम्** —
the यु and वु meant are the ones whose semivowel is NASAL, which
is a thing no writing shows and only the tradition carries.
**प्रतिज्ञानुनासिक्याः पाणिनीयाः** — the Pāṇinīyas' nasality is
by declaration. That is why ऊर्णायुः and भुज्युः keep their यु.

**AND ONE OF THE EIGHT IS CODIFIED ELSEWHERE.** 7.1.3 झोऽन्तः
was read long before this pāda, as `anga.jho_antah`, because it
had to be settled against 1.3.7 चुटू before पचन्ति could be
derived at all. The constant `CODIFIED_APART` records the gap.

**WHAT THIS MODULE DOES NOT DO.** It says what the affix becomes,
not what the affix means or where it comes from. That नन्दि takes
ल्यु at all is 3.1.134's business.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch — the opening of अध्याय ७.
PRATYAYA_RUN: Tuple[str, str] = ("7.1.1", "7.1.8")

#: 7.1.3 झोऽन्तः is codified in `anga.jho_antah`, where it had to
#: be settled against 1.3.7 चुटू.
CODIFIED_APART: Tuple[str, ...] = ("7.1.3",)

#: 7.1.1's two, matched one to one.
YU_VU: Tuple[Tuple[str, str], ...] = (("yu", "ana"), ("vu", "aka"))

#: 7.1.2's five, likewise — and only at the HEAD of an affix.
ADI_FIVE: Tuple[Tuple[str, str], ...] = (
    ("pha", "āyan"), ("ḍha", "ey"), ("kha", "īn"),
    ("cha", "īy"), ("gha", "iy"))

#: The यु that is not nasal, and so is not touched: ऊर्णायुः,
#: भुज्युः, मृत्युः.
NOT_NASAL: Tuple[str, ...] = ("ūrṇāyu", "bhujyu", "mṛtyu")

#: 7.1.4's stems, all reduplicated: ददति, दधति, जक्षति, जाग्रति.
ABHYASTA_FOUR: Tuple[str, ...] = ("dā", "dhā", "jakṣ", "jāgṛ")

#: The four affixes 7.1.2 is worked on, with the taddhita rule
#: that supplies each: फक् 4.1.99, ढक् 4.1.120, ख 4.1.139,
#: छ 4.2.114, घ 4.1.138.
WHERE_THEY_COME_FROM: Tuple[Tuple[str, str], ...] = (
    ("pha", "4.1.99"), ("ḍha", "4.1.120"), ("kha", "4.1.139"),
    ("cha", "4.2.114"), ("gha", "4.1.138"))


@dataclass(frozen=True)
class Affix:
    """One rule of 7.1.1–8: a substitute inside the affix itself."""

    sutra: str
    #: What the named piece becomes, or the augment supplied.
    does: str = ""
    #: The pieces the rule names.
    of: Tuple[str, ...] = ()
    #: Where the naming is one to one.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: Only at the head of the affix (7.1.2).
    at_head: bool = False
    #: The stem class the affix must follow.
    after: str = ""
    #: The root it must follow, named.
    root: Tuple[str, ...] = ()
    #: आत्मनेपद or परस्मैपद.
    pada: str = ""
    #: True where the rule supplies an आगम and not an आदेश.
    augment: bool = False
    optional: bool = False
    chandasi: bool = False
    bahulam: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


AFFIX_TABLE: Tuple[Affix, ...] = (
    Affix(
        "7.1.1", pairs=YU_VU, of=("yu", "vu"),
        keeps_out="ऊर्णायुः, भुज्युः, मृत्युः — a यु whose "
                  "semivowel is not nasal, and so not this यु",
        why="युवोरनाकौ — यु becomes अन and वु becomes अक, one to "
            "one: **नन्दनः, रमणः** from ल्यु; **सायंतनः, "
            "चिरंतनः** from ट्युट्; **कारकः, हारकः** from ण्वुल्; "
            "**वासुदेवकः, अर्जुनकः** from वुन्.\\n\\n"
            "**AND THE यु MEANT IS ONE NO WRITING SHOWS.** "
            "**अनुनासिकयणोः प्रत्यययोर्ग्रहणम्** — the semivowel "
            "must be NASAL, and **प्रतिज्ञानुनासिक्याः "
            "पाणिनीयाः**, the Pāṇinīyas' nasality is by "
            "declaration and not by any mark. So ऊर्णायुः from "
            "5.2.123's युस् and भुज्युः from the Uṇādi युक् are "
            "untouched: **एवमादीनां हि यणोऽनुनासिकत्वं न "
            "प्रतिज्ञायते**.\\n\\n"
            "**AND THE SŪTRA'S OWN WORD IS ARGUED OVER.** युवोः "
            "is a dual, and the vṛtti walks through what follows "
            "if the dvandva is taken as one thing or as two — "
            "**द्वित्वे यण् तु प्रसज्यते**, and **अथ चेद् "
            "एकवद्भावः कथं पुंवद् भवेद् अयम्**. The verse ends "
            "**द्वित्वे नैगमिको लोप एकत्वे नुमनित्यता** — either "
            "reading costs something, and the vṛtti says which"),
    Affix(
        "7.1.2", pairs=ADI_FIVE,
        of=tuple(one for one, _ in ADI_FIVE), at_head=True,
        keeps_out="फक्कति, ढौकते, खनति, छिनत्ति, घूर्णते — roots "
                  "and not affixes; ऊरुदघ्नम्, जानुदघ्नम् — the "
                  "sound is in the affix but not at its head",
        why="आयनेयीनीयियः फढखच्छघां प्रत्ययादीनाम् — five sounds "
            "at the HEAD of an affix, five substitutes, one to "
            "one: फ → आयन् in **नाडायनः, चारायणः**; ढ → एय् in "
            "**सौपर्णेयः, वैनतेयः**; ख → ईन् in **आढ्यकुलीनः**; "
            "छ → ईय् in **गार्गीयः, वात्सीयः**; घ → इय् in "
            "**क्षत्रियः**.\\n\\n"
            "**AND THE SUBSTITUTION HAPPENS WHILE THE AFFIX IS "
            "STILL BEING TAUGHT.** **एत आयन्नादयः "
            "प्रत्ययोपदेशकाल एव भवन्ति** — not when the word is "
            "built. That is what makes 4.4.117's घच् worth its "
            "च् marker: the accent falls on the substitute's "
            "first vowel, which would not exist yet if the change "
            "came later. And शङ्खः and षण्ढः keep their sounds "
            "because **उणादयो बहुलम्**"),
    Affix(
        "7.1.4", does="at", of=("jha",), after="abhyasta",
        blocks=("7.1.3",),
        keeps_out="अददुः, अजगारुः — जुस् has replaced the झ "
                  "first, and this rule is not reached",
        why="अदभ्यस्तात् — after a REDUPLICATED stem the झ becomes "
            "अत् and not अन्त्: **ददति, ददतु; दधति, दधतु; "
            "जक्षति, जक्षतु; जाग्रति, जाग्रतु**. "
            "**अन्तादेशापवादोऽयम्** — an exception to 7.1.3 — "
            "**जुसादेशेन तु बाध्यते**, and is itself set aside "
            "where 3.4.109's जुस् has already taken the झ"),
    Affix(
        "7.1.5", does="at", of=("jha",), after="an-a-anta",
        pada="ātmanepada", blocks=("7.1.3",),
        keeps_out="च्यवन्ते, प्लवन्ते — the stem ends in अ; "
                  "चिन्वन्ति, लुनन्ति — परस्मैपद, so 7.1.3 stands",
        why="आत्मनेपदेष्वनतः — and in the आत्मनेपद the झ becomes "
            "अत् after a stem that does NOT end in अ: "
            "**चिन्वते, चिन्वताम्, अचिन्वत; पुनते, लुनते, "
            "अलुनत**.\\n\\n"
            "**AND THE अनत् QUALIFIES THE STEM, NOT THE झ.** "
            "**अनकारान्तेनाङ्गेन झकारविशेषणं किम्? इह मा भूत् — "
            "शयान्तै** — read the other way the Vedic शयान्तै "
            "would lose its अन्त्. The vṛtti also notes that the "
            "विकरण is put in first, being नित्य, so 7.1.3 has "
            "already had its chance"),
    Affix(
        "7.1.6", does="ruṭ", of=("jha-ādeśa",), root=("śīṅ",),
        augment=True,
        keeps_out="व्यतिशेश्यते — the सानुबन्ध शीङ् is named, so "
                  "the अयङ् that has been elided does not count",
        why="शीङो रुट् — after शीङ् the झ-substitute takes the "
            "augment रुट् at its head: **शेरते, शेरताम्, "
            "अशेरत**.\\n\\n"
            "**AND IT IS AN AUGMENT TO THE SUBSTITUTE AND NOT TO "
            "THE झ.** **स यदि झकारस्यैव स्यात् अदादेशो न "
            "स्यात्** — attached to the झ itself it would have "
            "blocked 7.1.5's अत्, and शेरते needs both. The "
            "sūtra names शीङ् with its ङ् — **सानुबन्धग्रहणम् "
            "अयङ्लुगर्थम्**"),
    Affix(
        "7.1.7", does="ruṭ", of=("jha-ādeśa",), root=("vid",),
        augment=True, optional=True,
        keeps_out="विन्ते, विन्दाते — the विद् with a विकरण, "
                  "which is not the one named",
        why="वेत्तेर्विभाषा — and after विद् the रुट् is optional: "
            "**संविदते, संविद्रते; संविदताम्, संविद्रताम्; "
            "समविदत, समविद्रत**. **वेत्तेरिति लुग्विकरणस्य "
            "ग्रहणम्** — the विद् meant is the one whose विकरण "
            "is elided, which is why विन्ते is out"),
    Affix(
        "7.1.8", does="ruṭ", of=("jha-ādeśa",), augment=True,
        chandasi=True, bahulam=True,
        why="बहुलं छन्दसि — and in the Veda the रुट् is बहुलम्: "
            "**देवा अदुह्र, गन्धर्वाप्सरसो अदुह्र**, where the "
            "झ has become अत् and then taken रुट्, and 7.1.41 "
            "drops the त्.\\n\\n"
            "**AND बहुलम् CUTS BOTH WAYS, WHICH IS THE POINT OF "
            "THE WORD.** It reaches where no rule would have put "
            "it — **अदृश्रमस्य केतवः** — and it lets 7.4.16's "
            "guṇa fail in the same form: **ऋदृशोऽङि गुणः "
            "इत्येतदपि बहुलवचनादेवात्र न भवति**. One word "
            "licensing both directions at once"),
)


def _reaches(row: Affix, affix: str, after: str, root: str,
             pada: str, chandasi: bool) -> bool:
    if row.pairs and affix and affix not in dict(row.pairs):
        return False
    if row.of and affix and affix not in row.of:
        return False
    if row.after and after != row.after:
        return False
    if row.root and root not in row.root:
        return False
    if row.pada and pada != row.pada:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _becomes(row: Affix, affix: str) -> str:
    """The substitute, where the rule matches one to one."""
    for named, shape in row.pairs:
        if named == affix:
            return shape
    return row.does


def _supplies(row: Affix, affix: str, wants: str) -> bool:
    return not wants or wants == _becomes(row, affix)


def _how_specific(row: Affix, affix: str, after: str) -> int:
    """
    A rule that names what it displaces beats it, a named root
    beats a named stem class, and the Veda beats the language.

    7.1.3, 7.1.4 and 7.1.5 are the three that need it: one turns
    every झ into अन्त्, and two take it back for a reduplicated
    stem and for the आत्मनेपद.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.root)
        + 6 * bool(row.pairs and _becomes(row, affix) != row.does)
        + 5 * bool(row.after and after == row.after)
        + 4 * bool(row.pada)
        + 3 * bool(row.of and affix in row.of)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Substituted:
    """What the run answers: the affix's new shape, or an augment."""

    does: str
    sutra: str
    why: str
    augment: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def becomes(affix: str = "", *, after: str = "", root: str = "",
            pada: str = "", chandasi: bool = False,
            wants: str = "") -> Substituted:
    """
    7.1.1–8 — what the affix itself is replaced by.

    Nothing answers by default. An affix with no यु, no वु, no
    झ and no फढखछघ at its head goes into the word as it stands,
    and that is most affixes.
    """
    matched = [
        row for row in AFFIX_TABLE
        if _reaches(row, affix, after, root, pada, chandasi)
        and _supplies(row, affix, wants)
    ]
    if not matched:
        return Substituted(
            "", "", "No rule of 7.1.1-8 is reached, so the affix "
                    "keeps the shape it was taught in")
    row = max(matched,
              key=lambda one: _how_specific(one, affix, after))
    return Substituted(_becomes(row, affix), row.sutra, row.why,
                       augment=row.augment, optional=row.optional,
                       blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Affix, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in AFFIX_TABLE if row.sutra == sutra_id)


__all__ = [
    "Affix", "AFFIX_TABLE", "PRATYAYA_RUN", "CODIFIED_APART",
    "YU_VU", "ADI_FIVE", "NOT_NASAL", "ABHYASTA_FOUR",
    "WHERE_THEY_COME_FROM", "Substituted", "becomes",
    "provisions_for",
]
