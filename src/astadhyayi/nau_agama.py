# -*- coding: utf-8 -*-
"""
७.३.३२–४३ — हन् before a ञित्, and what the causal puts in.

Twelve sūtras, and the heading changes twice inside them. 7.3.32
हनस्तोऽचिण्णलोः closes the उत्तरपद run — **तद्धितेष्विति
निवृत्तम्। तत्संबद्धं कितीत्यपि** — and turns हन् into त् before
a ञित् or णित् that is neither चिण् nor णल्: घातयति, घातकः. Then
7.3.33 and 7.3.34 argue about an आ-final stem's युक् before चिण्
and a कृत्; and from 7.3.36 the word is णौ alone, and the rest of
the run is about augments and substitutes in the causal —
अर्पयति, ह्रेपयति, पाययति, भीषयते, स्फावयति, शातयति.

**AND EVERY AUGMENT OF THE CAUSAL IS PUT BEFORE THE ENDING AND
NOT AFTER.** **एतेऽपि पूर्वान्ता एव क्रियन्ते** — the पुक्, युक्,
जुक्, नुक् and षुक् all attach to what precedes, and the reason
is a rule three pādas on: only so does the reduplicated aorist
shorten the right vowel, **न्यशीशयत्, अपीपलत्, अदूधुनत्**.

**AND TWO OF THEM ARE LICENSED BY A SENSE.** ली and ला take their
नुक् and लुक् only of MELTING — घृतं विलीनयति but जतु विलापयति;
and भी takes its षुक् only where the FRIGHTENER is the fear's
cause — मुण्डो भीषयते but कुञ्चिकयैनं भाययति.

**WHAT THIS MODULE DOES NOT DO.** It says what goes in. What the
causal means, and that णि comes at all, is 3.1.26's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
NAU_RUN: Tuple[str, str] = ("7.3.32", "7.3.43")

#: Where the उत्तरपद heading ends and this run begins.
UTTARAPADA_ENDS_AT: str = "7.3.32"

#: Where णौ takes over and the rest is about the causal.
NAU_FROM: str = "7.3.36"

#: 7.3.36's six, which take पुक् before णि.
ARTI_SIX: Tuple[str, ...] = ("ṛ", "hrī", "vlī", "rī", "knūyī",
                             "kṣmāyī")

#: 7.3.37's seven, which take युक्.
SA_CHA_SEVEN: Tuple[str, ...] = (
    "śā", "chā", "sā", "hvā", "vyā", "ve", "pā")

#: What the vṛtti says about where every one of these augments
#: goes, and the rule it is said for.
PURVANTA: str = "एतेऽपि पूर्वान्ता एव क्रियन्ते"


@dataclass(frozen=True)
class Nau:
    """One rule of 7.3.32–43: a substitute or augment before णि."""

    sutra: str
    #: What is supplied: `t`, `yuk`, `puk`, `juk`, `nuk`, `luk`,
    #: `ṣuk`, `v`, `p` — or "" where the rule refuses.
    does: str = ""
    #: The roots named outright.
    of: Tuple[str, ...] = ()
    #: The root class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: The sense the rule wants.
    sense: str = ""
    #: True where the rule supplies an आगम.
    augment: bool = False
    refuses: bool = False
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NAU_TABLE: Tuple[Nau, ...] = (
    Nau(
        "7.3.32", does="t", of=("han",), before=("ñit", "ṇit"),
        not_before=("ciṇ", "ṇal"),
        keeps_out="अघानि, जघान — चिण् and णल्, named out; "
                  "वार्त्रघ्नम् इतरत् — a taddhita's ञित्, and "
                  "the rule wants the root's own affix",
        why="हनस्तोऽचिण्णलोः — हन् becomes त् before a ञित् or "
            "णित् that is neither चिण् nor णल्: **घातयति, "
            "घातकः, साधुघाती, घातंघातम्, घातो वर्तते**.\\n\\n"
            "**AND TWO WORDS OF THE HEADING FALL AWAY HERE.** "
            "**तद्धितेष्विति निवृत्तम्। तत्संबद्धं कितीत्यपि** — "
            "the taddhita condition goes and the कित् with it, "
            "since that was there only for the taddhitas' sake. "
            "**ञ्णितीति वर्तते** is what is left, and this is "
            "where 7.3.10's उत्तरपद heading ends.\\n\\n"
            "**AND THE RULE IS ABOUT A ROOT'S OWN AFFIX.** "
            "**धातोः कार्यम् उच्यमानं धातोः प्रत्यये विज्ञायते** "
            "— so वार्त्रघ्नम् is untouched, its ञित् belonging "
            "to a noun"),
    Nau(
        "7.3.33", does="yuk", gana="ā-anta", before=("ciṇ", "kṛt"),
        augment=True,
        keeps_out="ददौ, दधौ — neither चिण् nor a कृत्; चौडिः, "
                  "बालाकिः — a taddhita's इञ्",
        why="आतो युक् चिण्कृतोः — an आ-final stem takes the "
            "augment युक् before चिण् and before a ञित् or णित् "
            "कृत्: **अदायि, अधायि; दायः, दायकः, धायः, धायकः**"),
    Nau(
        "7.3.34", refuses=True, gana="udātta-upadeśa-m-anta",
        of=("ā-cam",), before=("ciṇ", "kṛt"), blocks=("7.2.116",),
        keeps_out="यामकः, रामकः — not उदात्त in the उपदेश; "
                  "चारकः, पाठकः — not म्-final; आचामकः — आचम्, "
                  "named out",
        why="नोदात्तोपदेशस्य मान्तस्यानाचमेः — but a म्-final "
            "root that is उदात्त as it is taught does not take "
            "7.2.116's vṛddhi before चिण् or a कृत्, आचम् "
            "excepted: **अशमि, अतमि, अदमि; शमकः, तमकः, दमकः; "
            "शमः, तमः, दमः**. **किं चोक्तम्? अत उपधायाः इति "
            "वृद्धिः** — the vṛtti has to say which of the "
            "earlier rules the *what is said* refers to. And "
            "उपदेशे is what gets शमी and दमी while keeping "
            "यामकः out"),
    Nau(
        "7.3.35", refuses=True, of=("jan", "vadh"),
        before=("ciṇ", "kṛt"), blocks=("7.2.116",),
        keeps_out="जजान गर्भम् — णल्, and neither चिण् nor a कृत्",
        why="जनिवध्योश्च — and जन् and वध्: **अजनि, जनकः, "
            "प्रजनः; अवधि, वधकः, वधः**. The वध् meant is the "
            "consonant-final root that exists in its own right, "
            "**वधिः प्रकृत्यन्तरं व्यञ्जनान्तोऽस्ति तस्यायं "
            "प्रतिषेधो विधीयते** — the वध that replaces हन् "
            "ends in अ and would never have taken the vṛddhi"),
    Nau(
        "7.3.36", does="puk", of=ARTI_SIX, gana="ā-anta",
        before=("ṇi",), augment=True,
        why="अर्त्तिह्रीब्लीरीक्नूयीक्ष्माय्यातां पुङ्णौ — six "
            "roots and every आ-final stem take पुक् before णि: "
            "**अर्पयति, ह्रेपयति, व्लेपयति, रेपयति, क्नोपयति, "
            "क्ष्मापयति; दापयति, धापयति**. Two roots of the "
            "shape ऋ are both meant, and two of the shape री.\\n\\n"
            "**AND THE AUGMENT IS PUT BEFORE THE ENDING FOR A "
            "REASON THREE PĀDAS ON.** **पुकः पूर्वान्तकरणम् "
            "अदीदपद् इत्यत्रोपधाह्रस्वो यथा स्यात्** — only so "
            "does the reduplicated aorist shorten the right "
            "vowel.\\n\\n"
            "**AND THE HEADING CHANGES HERE.** **सर्वं निवृत्तम्, "
            "अङ्गस्येति वर्तते** — everything the pāda has been "
            "carrying falls away, and णौ alone governs the rest "
            "of the run"),
    Nau(
        "7.3.37", does="yuk", of=SA_CHA_SEVEN, before=("ṇi",),
        augment=True,
        why="शाच्छासाह्वाव्यावेपां युक् — seven roots take युक् "
            "before णि: **निशाययति, अवच्छाययति, अवसाययति, "
            "ह्वाययति, संव्याययति, वाययति, पाययति**. The पा "
            "meant takes in the drying-root as well, "
            "**पाग्रहणे पै ओवै शोषणे इत्यस्यापीह ग्रहणम् "
            "इच्छन्ति**, but not the protecting one. And two "
            "vārttikas add more: **लुगागमस्तु तस्य "
            "वक्तव्यः** giving पालयति, and **धूञ्प्रीञोर् नुग् "
            "वक्तव्यः** giving धूनयति and प्रीणयति"),
    Nau(
        "7.3.38", does="juk", of=("vā",), before=("ṇi",),
        sense="vidhūnana", augment=True,
        keeps_out="आवापयति केशान् — no shaking meant, and the "
                  "root is the drying one",
        why="वो विधूनने जुक् — वा takes जुक् before णि where "
            "SHAKING is meant: **पक्षेणोपवाजयति**. Without that "
            "sense it is **आवापयति केशान्**, and the root there "
            "is the drying one — **पै ओवै शोषणे इत्येतस्यैतद् "
            "रूपम्**, a different word of the same shape"),
    Nau(
        "7.3.39", does="nuk-luk", of=("lī", "lā"), before=("ṇi",),
        sense="sneha-vipātana", augment=True, optional=True,
        keeps_out="जतु विलापयति, जटाभिरालापयते — no melting of "
                  "fat is meant",
        why="लीलोर्नुग्लुकावन्यतरस्यां स्नेहविपातने — ली and ला "
            "take नुक् and लुक् OPTIONALLY before णि where "
            "MELTING is meant: **घृतं विलीनयति, घृतं विलाययति; "
            "विलालयति, विलापयति**. The ली is written with an "
            "ई read into it, so that the नुक् reaches only the "
            "ई-final root and not the one 6.1.51 has already "
            "turned into ला"),
    Nau(
        "7.3.40", does="ṣuk", of=("bhī",), before=("ṇi",),
        sense="hetu-bhaya", augment=True,
        keeps_out="कुञ्चिकयैनं भाययति — the key is the fear's "
                  "cause and not its agent, **नात्र हेतुः "
                  "प्रयोजको भयकारणम्**",
        why="भियो हेतुभये षुक् — भी takes षुक् before णि where "
            "the FRIGHTENER is himself the fear's occasion: "
            "**मुण्डो भीषयते; जटिलो भीषयते**. Again an ई is "
            "read into the root, **कृतात्वस्य षुग्निवृत्त्यर्थः** "
            "— else भापयते would take it too"),
    Nau(
        "7.3.41", does="v", of=("sphāy",), before=("ṇi",),
        why="स्फायो वः — स्फाय् becomes व before णि: "
            "**स्फावयति**. One root, one substitute, and no "
            "condition beyond the affix — the shortest sūtra of "
            "the run, and the only one the vṛtti has nothing to "
            "argue about"),
    Nau(
        "7.3.42", does="t", of=("śad",), before=("ṇi",),
        sense="a-gati",
        keeps_out="गाः शादयति गोपालकः — the herdsman DRIVES the "
                  "cattle, and motion is meant",
        why="शदेरगतौ तः — शद् becomes त् before णि where MOTION "
            "is NOT meant: **पुष्पाणि शातयति**, he makes the "
            "flowers fall. **अगताविति किम्? गाः शादयति "
            "गोपालकः** — the herdsman DRIVES his cattle, and "
            "there the change does not come"),
    Nau(
        "7.3.43", does="p", of=("ruh",), before=("ṇi",),
        optional=True,
        why="रुहः पोऽन्यतरस्याम् — and रुह् becomes प "
            "OPTIONALLY: **व्रीहीन् रोपयति, व्रीहीन् "
            "रोहयति**. Both forms stand, and the option is the "
            "last thing the pāda says about the causal before it "
            "turns to the feminine's क"),
)


def _reaches(row: Nau, root: str, gana: str, before: str,
             sense: str) -> bool:
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.sense and sense != row.sense:
        return False
    return True


def _how_specific(row: Nau, root: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, a named
    sense beats a named root, and a named root beats a class.

    7.3.36 against 7.3.37 to 7.3.40 is what needs it: one rule
    gives every आ-final stem a पुक्, and four name particular
    roots that take something else instead.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.sense)
        + 6 * bool(row.of and root in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 2 * bool(row.before)
    )


@dataclass(frozen=True)
class Put:
    """What the run answers: a substitute, an augment, a refusal."""

    does: str
    sutra: str
    why: str
    augment: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_ni(root: str = "", *, gana: str = "", before: str = "",
              sense: str = "") -> Put:
    """
    7.3.32–43 — what goes in before णि, and what हन् becomes.

    Nothing answers by default. Most roots take the causal's णि
    with no augment at all, and this run is the ones that do not.
    """
    matched = [
        row for row in NAU_TABLE
        if _reaches(row, root, gana, before, sense)
    ]
    if not matched:
        return Put(
            "", "", "No rule of 7.3.32-43 is reached, so nothing "
                    "goes in before the affix")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Put("" if row.refuses else row.does, row.sutra, row.why,
               augment=row.augment, optional=row.optional,
               blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Nau, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NAU_TABLE if row.sutra == sutra_id)


__all__ = [
    "Nau", "NAU_TABLE", "NAU_RUN", "UTTARAPADA_ENDS_AT",
    "NAU_FROM", "ARTI_SIX", "SA_CHA_SEVEN", "PURVANTA", "Put",
    "before_ni", "provisions_for",
]
