# -*- coding: utf-8 -*-
"""
७.२.११५–११८ — vṛddhi before a ञित् or णित्, closing the pāda.

Four sūtras, and between them they are why so much of Sanskrit
derivation begins with a strengthened vowel. A vowel-final stem
takes vṛddhi before a ञित् or णित् affix (कारः, हारः, गौः,
सखायौ); so does an अ (a) in the penult (पाकः, त्यागः, पाचयति);
and in a TADDHITA it is the FIRST vowel of the stem that takes
it, wherever it stands (गार्ग्यः, औपगवः, नाडायनः, आक्षिकः).

**AND THE TADDHITA RULE DISPLACES THE OTHER TWO.** त्वाष्ट्रः
and जागतः would have strengthened their last or penultimate
vowel; **अचामादेर् वृद्धिर् अन्त्योपधालक्षणां वृद्धिं बाधते** —
the first-vowel rule beats them both. Which is why a patronymic
looks the way it does.

**AND ONE OF THE FOUR IS ABOUT A कित् AND NOT A ञित् OR णित्.**
7.2.118 किति च extends the same first-vowel vṛddhi to a कित्
taddhita — फक् at 4.1.99 and ठक् at 4.4.1 — and those two
affixes are marked कित् precisely so that 1.1.5's क्ङिति
refusal should NOT reach the operation this sūtra states.

**AND ONE SŪTRA OF THE STRETCH IS CODIFIED ELSEWHERE.** 7.2.114
मृजेर्वृद्धिः was read long before this pāda, as
`anga.mrjer_vrddhi`, because it exercises the two-step vṛddhi of
ऋ that 1.1.50 and 1.1.51 build between them.

**WHAT THIS MODULE DOES NOT DO.** It says that the vowel is
strengthened. WHICH sound the strengthened vowel is comes from
1.1.1's वृद्धिरादैच् and, for ऋ, from 1.1.50 and 1.1.51.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch, closing पाद ७.२.
NNIT_RUN: Tuple[str, str] = ("7.2.115", "7.2.118")

#: 7.2.114 मृजेर्वृद्धिः is codified in `anga.mrjer_vrddhi`.
CODIFIED_APART: Tuple[str, ...] = ("7.2.114",)

#: Where the first-vowel rule takes over from the other two.
TADDHITA_FROM: str = "7.2.117"

#: The two taddhita affixes 7.2.118 is worked on, and the rules
#: that supply them: फक् 4.1.99, ठक् 4.4.1.
KIT_TADDHITAS: Tuple[Tuple[str, str], ...] = (
    ("phak", "4.1.99"), ("ṭhak", "4.4.1"))


@dataclass(frozen=True)
class Nnit:
    """One rule of 7.2.115–118: which vowel takes the vṛddhi."""

    sutra: str
    #: `vṛddhi`, always — the rules differ in WHERE.
    does: str = "vṛddhi"
    #: Which vowel: the last, the penult, or the first.
    part: str = ""
    #: The stem class the rule reaches.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: True where the affix must also be a taddhita.
    taddhita: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NNIT_TABLE: Tuple[Nnit, ...] = (
    Nnit(
        "7.2.115", part="antya-ac", gana="ac-anta",
        before=("ñit", "ṇit"),
        why="अचो ञ्णिति — a vowel-final stem takes vṛddhi before "
            "a ञित् or णित् affix: **कारः, हारः** and "
            "**एकस्तण्डुलनिश्चायः** for the ञित्; **गौः, गावौ, "
            "गावः; सखायौ, सखायः; जैत्रम्, यौत्रम्, च्यौत्नः** "
            "for the णित्. This and the two after it are why so "
            "much Sanskrit derivation begins with a strengthened "
            "vowel"),
    Nnit(
        "7.2.116", part="upadhā-a", before=("ñit", "ṇit"),
        keeps_out="भेदयति, भेदकः — the penult is not अ; "
                  "चकासयति, तक्षकः — the अ is not the penult",
        why="अत उपधायाः — and an अ in the PENULT: **पाकः, "
            "त्यागः, यागः; पाचयति, पाचकः; पाठयति, पाठकः**. Both "
            "halves of the condition are tested by the vṛtti, "
            "and each has its own counter-example"),
    Nnit(
        "7.2.117", part="acām-ādi", before=("ñit", "ṇit"),
        taddhita=True, blocks=("7.2.115", "7.2.116"),
        why="तद्धितेष्वचामादेः — but in a TADDHITA it is the "
            "FIRST vowel of the stem that takes it, wherever it "
            "stands: **गार्ग्यः, वात्स्यः, दाक्षिः, प्लाक्षिः** "
            "for the ञित्; **औपगवः, कापटवः** for the "
            "णित्.\\n\\n"
            "**AND IT DISPLACES BOTH THE RULES BEFORE IT.** "
            "**त्वाष्ट्रः, जागत इत्यत्राचामादेर् वृद्धिर् "
            "अन्त्योपधालक्षणां वृद्धिं बाधते** — त्वष्टृ would "
            "have strengthened its ऋ and जगत् its penult; the "
            "first vowel wins in both. Which is why a patronymic "
            "looks the way it does"),
    Nnit(
        "7.2.118", part="acām-ādi", before=("kit",), taddhita=True,
        blocks=("7.2.115", "7.2.116"),
        why="किति च — and before a कित् taddhita: **नाडायनः, "
            "चारायणः** from 4.1.99's फक्; **आक्षिकः, "
            "शालाकिकः** from 4.4.1's ठक्.\\n\\n"
            "**AND THE कित् MARKING IS WHAT MAKES THE SŪTRA "
            "NECESSARY.** 1.1.5's क्ङिति refuses a "
            "guṇa-or-vṛddhi conditioned on an इक्, and both "
            "these affixes are marked कित् for other reasons. "
            "Stating the vṛddhi here, on the FIRST vowel and "
            "not on an इक्, puts it out of that rule's reach. "
            "This closes पाद ७.२: **इति श्रीवामनविरचितायां "
            "काशिकायां वृत्तौ सप्तमाध्यायस्य द्वितीयः पादः**"),
)


def _reaches(row: Nnit, gana: str, before: str, part: str,
             taddhita: bool) -> bool:
    if row.gana and gana != row.gana:
        return False
    if row.before and before not in row.before:
        return False
    if row.part and part and part != row.part:
        return False
    if row.taddhita and not taddhita:
        return False
    return True


def _how_specific(row: Nnit, part: str) -> int:
    """
    A rule that names what it displaces beats it, and a named
    part beats a bare environment.

    7.2.117 against 7.2.115 and 7.2.116 is the whole of it: all
    three reach त्वाष्ट्रः, and only the taddhita rule gives the
    form the language has.
    """
    return (
        12 * len(row.blocks)
        + 5 * bool(row.part and part and part == row.part)
        + 4 * bool(row.gana)
        + 3 * bool(row.before)
        + 2 * bool(row.taddhita)
    )


@dataclass(frozen=True)
class Strengthened:
    """What the run answers: which vowel takes the vṛddhi."""

    does: str
    where: str
    sutra: str
    why: str
    blocked_by: Tuple[str, ...] = ()


def vrddhi_before(before: str = "", *, gana: str = "",
                  part: str = "", taddhita: bool = False
                  ) -> Strengthened:
    """
    7.2.115–118 — which vowel is strengthened, and before what.

    Nothing answers by default. An affix that is neither ञित् nor
    णित् nor a कित् taddhita strengthens nothing here, whatever
    else may happen to the stem.
    """
    matched = [
        row for row in NNIT_TABLE
        if _reaches(row, gana, before, part, taddhita)
    ]
    if not matched:
        return Strengthened(
            "", "", "", "No rule of 7.2.115-118 is reached, so no "
                        "vrddhi is stated here")
    row = max(matched, key=lambda one: _how_specific(one, part))
    return Strengthened(row.does, row.part, row.sutra, row.why,
                        blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Nnit, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NNIT_TABLE if row.sutra == sutra_id)


__all__ = [
    "Nnit", "NNIT_TABLE", "NNIT_RUN", "CODIFIED_APART",
    "TADDHITA_FROM", "KIT_TADDHITAS", "Strengthened",
    "vrddhi_before", "provisions_for",
]
