# -*- coding: utf-8 -*-
"""
७.१.५१–५७ — the augments the ending takes: असुक्, सुट्, नुट्.

Seven sūtras, and six of them put something in FRONT of a case
ending rather than replacing it. अश्व wanting a mare of its own is
अश्वस्यति, with असुक् before the क्यच्; सर्व + आम् is सर्वेषाम्,
with सुट्; वृक्ष + आम् is वृक्षाणाम्, with नुट्.

**सुट् AND नुट् DIVIDE THE GENITIVE PLURAL BETWEEN THEM.** 7.1.52
gives सुट् to an अ-final pronoun — सर्वेषाम्, तेषाम्, यासाम् — and
7.1.54 gives नुट् to a short-vowel stem, a नदी and an आप् —
वृक्षाणाम्, अग्नीनाम्, कुमारीणाम्, खट्वानाम्. Between them almost
every genitive plural in the language is accounted for, and the
one word that escapes both is त्रि, which 7.1.53 rebuilds as त्रय.

**AND ONE OF THE SEVEN IS NOT AN AUGMENT AT ALL.** 7.1.53
त्रेस्त्रयः replaces the whole stem — त्रयाणाम्, and a Vedic
त्रीणाम् beside it. It sits here because it is about the same आम्.

**WHAT THIS MODULE DOES NOT DO.** It says what the ending is given.
Whether the stem in front is a नदी is 1.4.3's business, and
whether it is a सर्वनामन् is 1.1.27's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
AGAMA_RUN: Tuple[str, str] = ("7.1.51", "7.1.57")

#: 7.1.51's four, which take असुक् before क्यच्.
ASVADI_FOUR: Tuple[str, ...] = ("aśva", "kṣīra", "vṛṣa", "lavaṇa")

#: And the two vārttikas that split their sense in half: a horse
#: and a bull want mating, milk and salt are craved.
WHAT_THEY_WANT: Tuple[Tuple[str, str], ...] = (
    ("aśva-vṛṣa", "maithuna-icchā"), ("kṣīra-lavaṇa", "lālasā"))

#: 7.1.54's three stem-shapes, all taking नुट्.
NUT_THREE: Tuple[str, ...] = ("hrasva-anta", "nadī-anta", "āp-anta")

#: What 7.1.55 adds to them: the षट् numerals and चतुर्.
SAT_AND_CATUR: Tuple[str, ...] = ("ṣaṭ", "catur")


@dataclass(frozen=True)
class Augment:
    """One rule of 7.1.51–57: what the ending is given, or becomes."""

    sutra: str
    #: The augment supplied, or the substitute where it is one.
    does: str = ""
    #: The ending or affix acted on.
    of: Tuple[str, ...] = ()
    #: The stems named outright.
    stem: Tuple[str, ...] = ()
    #: The stem class instead.
    after: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: The sense the rule wants.
    sense: str = ""
    #: True where the rule supplies an आगम, false where it
    #: replaces.
    augment: bool = True
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


AGAMA_TABLE: Tuple[Augment, ...] = (
    Augment(
        "7.1.51", does="asuk", of=("kyac",), stem=ASVADI_FOUR,
        sense="ātma-prīti",
        keeps_out="अश्वीयति, क्षीरीयति, वृषीयति, लवणीयति — the "
                  "wanting is for someone else, and no असुक् comes",
        why="अश्वक्षीरवृषलवणानामात्मप्रीतौ क्यचि — four stems take "
            "असुक् before क्यच् where the wanting is for ONESELF: "
            "**अश्वस्यति वडवा; क्षीरस्यति माणवकः; वृषस्यति गौः; "
            "लवणस्यत्युष्ट्रः**. And छन्दसि has stopped governing "
            "here — **छन्दसीत्यतः प्रभृति निवृत्तम्**, which is "
            "the vṛtti's own way of closing 7.1.38's "
            "heading.\\n\\n"
            "**AND TWO VĀRTTIKAS SPLIT THE SENSE IN HALF.** "
            "**अश्ववृषयोर्मैथुनेच्छायाम्** and "
            "**क्षीरलवणयोर्लालसायाम्** — the mare and the cow "
            "want mating, the boy and the camel crave. "
            "**तृष्णातिरेको लालसा**, and outside those two senses "
            "there is no असुक् even where the wanting is one's "
            "own. A third opinion widens it to every stem, and a "
            "fourth offers सुक् instead: **दधिस्यति, मधुस्यति**"),
    Augment(
        "7.1.52", does="suṭ", of=("ām",), after="a-varṇa-sarvanāma",
        keeps_out="भवताम् — भवत् is no सर्वनामन्, and the ending "
                  "stands bare",
        why="आमि सर्वनाम्नः सुट् — after an अ-final PRONOUN the "
            "genitive plural आम् takes सुट्: **सर्वेषाम्, "
            "विश्वेषाम्, येषाम्, तेषाम्; सर्वासाम्, यासाम्, "
            "तासाम्**.\\n\\n"
            "**AND THREE OTHER आम्s HAD TO BE RULED OUT.** The "
            "आम् meant is the genitive plural — not 7.3.116's "
            "ङेराम्, which is later and so takes आङ् आट् स्याट् "
            "first; not 5.4.11's किमेत्तिङव्ययघादामु; not "
            "3.1.35's आम् of the periphrastic perfect. "
            "**न तौ सर्वनाम्नः स्तः। सानुबन्धकाविति वा तौ न "
            "गृह्येते** — either they cannot follow a pronoun at "
            "all, or a paribhāṣā keeps a marked affix out"),
    Augment(
        "7.1.53", does="traya", of=("ām",), stem=("tri",),
        augment=False, blocks=("7.1.54",),
        why="त्रेस्त्रयः — त्रि becomes त्रय before आम्: "
            "**त्रयाणाम्**. Not an augment but a whole new stem, "
            "and the only rule of the seven that is. The Veda "
            "keeps another form beside it — **त्रीवामित्यपि "
            "छन्दसीष्यते। त्रीणामपि समुद्राणाम्**"),
    Augment(
        "7.1.54", does="nuṭ", of=("ām",), after="hrasva-nadī-āp",
        why="ह्रस्वनद्यापो नुट् — after a stem ending in a SHORT "
            "vowel, or in a नदी, or in आप्, the आम् takes नुट्: "
            "**वृक्षाणाम्, अग्नीनाम्, कर्तृणाम्** for the short "
            "vowel; **कुमारीणाम्, गौरीणाम्, लक्ष्मीणाम्, "
            "ब्रह्मबन्धूनाम्** for the नदी; **खट्वानाम्, "
            "मालानाम्, कारीषगन्ध्यानाम्** for the आप्. Three "
            "conditions, and the vṛtti works every one of them"),
    Augment(
        "7.1.55", does="nuṭ", of=("ām",), after="ṣaṭ-catur",
        keeps_out="प्रियषषाम्, प्रियपञ्चानाम्, प्रियचतुराम् — the "
                  "numeral is subordinate in the compound",
        why="षट्चतुर्भ्यश्च — and after a षट्-named numeral and "
            "after चतुर्: **षण्णाम्, पञ्चानाम्, सप्तानाम्, "
            "नवानाम्, दशानाम्; चतुर्णाम्**.\\n\\n"
            "**AND चतुर् IS NAMED APART BECAUSE IT IS NOT A "
            "षट्.** **रेफान्तायाः संख्यायाः षट्संज्ञा न विहिता, "
            "षड्भ्यो लुक् इति लुग् मा भूत्** — a र्-final numeral "
            "was kept out of the षट् name on purpose, or 7.1.22 "
            "would have dropped its जस्. So it has to be brought "
            "back in by name here. And the plural in the sūtra "
            "shows the numeral must be the compound's head: "
            "**परमषण्णाम्, परमचतुर्णाम्**"),
    Augment(
        "7.1.56", does="nuṭ", of=("ām",), stem=("śrī", "grāmaṇī"),
        chandasi=True,
        why="श्रीग्रामण्योश्छन्दसि — and श्री and ग्रामणी take it "
            "in the Veda: **श्रीणाम् उदारो धरुणो रयीणाम्; अपि "
            "तत्र सूतग्रामणीनाम्**.\\n\\n"
            "**AND EACH OF THE TWO IS THERE FOR A DIFFERENT "
            "REASON.** श्री is a नदी only optionally, by 1.4.5's "
            "वामि, so 7.1.54 would have reached it only half the "
            "time — **तत्र नित्यार्थं वचनम्**. सूतग्रामणीनाम् "
            "needs the rule only on one reading of the compound; "
            "on the other, **ह्रस्वादित्येव सिद्धम्**"),
    Augment(
        "7.1.57", does="nuṭ", of=("ām",), stem=("go",),
        before=("pāda-anta",), chandasi=True,
        keeps_out="गवां गोत्रम् उदसृजो यदङ्गिरः — not at the "
                  "verse-quarter's end",
        why="गोः पादान्ते — and गो takes it at the END OF A "
            "VERSE-QUARTER: **विद्मा हि त्वा गोपतिं शूर "
            "गोनाम्**. The condition is metrical and not "
            "grammatical, and even so it is not absolute — "
            "**सर्वे विधयश्छन्दसि विकल्प्यन्ते इति पादान्तेऽपि "
            "क्वचिद् न भवति। हन्तारं शत्रूणां कृधि विराजं "
            "गोपतिं गवाम्**"),
)


def _reaches(row: Augment, ending: str, stem: str, after: str,
             before: str, sense: str, chandasi: bool) -> bool:
    if row.of and ending and ending not in row.of:
        return False
    if row.stem and stem not in row.stem:
        return False
    if row.after and after != row.after:
        return False
    if row.before and before not in row.before:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Augment, stem: str, after: str) -> int:
    """
    A rule that names what it displaces beats it, a named stem
    beats a named class, and a metrical condition beats a plain
    Vedic one.

    7.1.53 against 7.1.54 is the pair that needs the first: त्रि
    is a short-vowel stem and would have taken नुट् like any
    other, and instead the whole stem is replaced.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.stem and stem in row.stem)
        + 5 * bool(row.after and after == row.after)
        + 4 * bool(row.before)
        + 4 * bool(row.sense)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Given:
    """What the run answers: an augment, or a stem replaced."""

    does: str
    sutra: str
    why: str
    augment: bool = True
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def takes(ending: str = "", *, stem: str = "", after: str = "",
          before: str = "", sense: str = "",
          chandasi: bool = False, wants: str = "") -> Given:
    """
    7.1.51–57 — what the ending is given before it goes in.

    Nothing answers by default. An आम् after a long-vowel stem
    that is no नदी takes neither सुट् nor नुट् — राज्ञाम् is bare,
    and that is what the two rules leave.
    """
    matched = [
        row for row in AGAMA_TABLE
        if _reaches(row, ending, stem, after, before, sense,
                    chandasi)
        and (not wants or wants == row.does)
    ]
    if not matched:
        return Given(
            "", "", "No rule of 7.1.51-57 is reached, so the "
                    "ending goes in as it is", augment=False)
    row = max(matched, key=lambda one: _how_specific(one, stem, after))
    return Given(row.does, row.sutra, row.why, augment=row.augment,
                 optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Augment, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in AGAMA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Augment", "AGAMA_TABLE", "AGAMA_RUN", "ASVADI_FOUR",
    "WHAT_THEY_WANT", "NUT_THREE", "SAT_AND_CATUR", "Given",
    "takes", "provisions_for",
]
