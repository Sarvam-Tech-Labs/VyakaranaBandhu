# -*- coding: utf-8 -*-
"""
६.४.२३–३३ — the न् dropped from a stem.

Eleven rules, one sound. A stem loses its न् before श्न (6.4.23),
before a कित् or ङित् affix if the stem has no इ marker (6.4.24),
before शप् for four roots (6.4.25–26), and before घञ् for one of
them in two senses (6.4.27). Then two sūtras lay down forms whole,
and four refuse the loss.

**AND THE WHOLE RUN STANDS UNDER 6.4.22.** असिद्धवत्रा भात् is the
sūtra immediately before it, and everything from there to the end
of the adhyāya is treated as not having happened for the purpose
of what shares its locus. So अनक्ति has lost its न् and the rules
that follow must not see that it has.

**AND THE FIRST OF THEM TURNS ON A LETTER THAT IS NOT PRONOUNCED.**
**श्नादिति श्नमयम् उत्सृष्टाकारो गृह्यते** — the श्न meant is श्नम्
with its अ let go, and the श् is there to tell it from anything
else ending in न. **शकारवतो ग्रहणं किम्? यज्ञानाम्, यत्नानाम्** —
without the श्, 7.3.102's lengthening would have made those look
like the same shape and the न् would have gone from them too.

**AND FOUR OF THE ELEVEN REFUSE, AND ONE OF THE FOUR REFUSES
NOTHING.** 6.4.33 भञ्जेश्च चिणि reads as a refusal and is not:
**अप्राप्तोऽयं नलोपः पक्षे विधीयते। ततो नेति नानुवर्तते** — the
loss was not available there at all, so the सूत्र grants it
optionally rather than withholding it, and the न् of 6.4.30 does
not carry down into it.

**WHAT THIS MODULE DOES NOT DO.** It reports whether the न् goes
and by which rule. It does not find the न्: which sound is the
penult, and whether a stem carries an इ marker, are what the query
says.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these eleven stand, between 6.4.22 असिद्धवत् and 6.4.34's
#: substitutions.
NALOPA_RUN: Tuple[str, str] = ("6.4.23", "6.4.33")

#: The heading every one of them stands under, and the one sūtra
#: of this pāda that was codified before any of them.
ASIDDHAVAT: str = "6.4.22"

#: 6.4.25's three, and 6.4.26's fourth.
SAPI_ROOTS: Tuple[str, ...] = ("daṃś", "sañj", "svañj")
RANJ: Tuple[str, ...] = ("rañj",)

#: 6.4.29's five, laid down whole rather than derived.
NIPATANA_FIVE: Tuple[str, ...] = (
    "avoda", "edha", "odma", "praśratha", "himaśratha")

#: What a vārttika adds to 6.4.24, and in what sense each:
#: **अनिदितां नलोपे लङ्गिकम्प्योर् उपतापशरीरविकारयोर्
#: उपसंख्यानं कर्तव्यम्**.
LANGI_KAMPI: Tuple[Tuple[str, str], ...] = (
    ("laṅg", "upatāpa"), ("kamp", "śarīravikāra"))


@dataclass(frozen=True)
class Nalopa:
    """One rule of 6.4.23–33: whether the न् goes."""

    sutra: str
    #: na-lopa, or nipātana where the form is laid down whole.
    does: str = ""
    #: The stems the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of stem instead.
    gana: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NALOPA_TABLE: Tuple[Nalopa, ...] = (
    Nalopa(
        "6.4.23", does="na-lopa", before=("śna",),
        keeps_out="यज्ञानाम्, यत्नानाम् — the न is not preceded by "
                  "the श् of श्नम्, though 7.3.102's lengthening "
                  "would otherwise have made them look alike",
        why="श्नान्नलोपः — the न् after श्न is dropped: **अनक्ति, "
            "भनक्ति, हिनस्ति**. And which श्न: **श्नादिति श्नमयम् "
            "उत्सृष्टाकारो गृह्यते** — the infix श्नम् with its अ "
            "let go, not the affix श्ना.\\n\\n"
            "**AND THE श् IS WHAT KEEPS TWO OTHER WORDS OUT.** "
            "**शकारवतो ग्रहणं किम्? यज्ञानाम्, यत्नानाम्। सुपि च "
            "इति परत्वात् कृतेऽपि दीर्घत्वे स्थानिवद्भावाद् नलोपः "
            "स्याद् एव** — 7.3.102 lengthens the अ, and by "
            "स्थानिवद्भाव the stem would still count as ending in "
            "the same shape, so the न् would go from those too. "
            "Naming the श् is what stops it"),
    Nalopa(
        "6.4.24", does="na-lopa", gana="anidit-hal-anta",
        before=("kṅit",),
        keeps_out="नन्द्यते, नानन्द्यते — नन्द् has an इ marker; "
                  "नीयते, नेनीयते — नी does not end in a "
                  "consonant; नह्यते — the न् is not the penult; "
                  "स्रंसिता, ध्वसिता — the affix is neither कित् "
                  "nor ङित्",
        why="अनिदितां हल उपधायाः क्ङिति — a consonant-final stem "
            "with NO इ marker drops the न् of its penult before a "
            "कित् or ङित्: **स्रस्तः, ध्वस्तः, स्रस्यते, "
            "ध्वस्यते, सनीस्रस्यते, दनीध्वस्यते**.\\n\\n"
            "**AND A VĀRTTIKA ADDS TWO ROOTS, EACH IN ONE SENSE "
            "ONLY.** **अनिदितां नलोपे लङ्गिकम्प्योर् "
            "उपतापशरीरविकारयोर् उपसंख्यानं कर्तव्यम्** — लङ्ग् "
            "where illness is meant and कम्प् where a change in "
            "the body is, matched one to one"),
    Nalopa(
        "6.4.25", does="na-lopa", of=SAPI_ROOTS, before=("śap",),
        why="दंशसञ्जस्वञ्जां शपि — three roots drop the न् of "
            "their penult before शप्: **दशति, सजति, परिष्वजते** — "
            "he bites, he clings, he embraces"),
    Nalopa(
        "6.4.26", does="na-lopa", of=RANJ, before=("śap",),
        why="रञ्जेश्च — and रञ्ज् likewise: **रजति, रजतः, "
            "रजन्ति**. Stated apart from the three before it for a "
            "reason that lies ahead: **पृथग्योगकरणम् उत्तरार्थम्** "
            "— so that रञ्ज् alone carries down into 6.4.27"),
    Nalopa(
        "6.4.27", does="na-lopa", of=RANJ, before=("ghañ",),
        result=("bhāva", "karaṇa"),
        keeps_out="रङ्गः — **रजन्ति तस्मिन्निति**, the place where "
                  "they are dyed, which is neither the act nor the "
                  "means",
        why="घञि च भावकरणयोः — and रञ्ज् drops it before घञ् where "
            "the ACT or the MEANS is named: **आश्चर्यो रागः, "
            "विचित्रो रागः** for the act; **रज्यतेऽनेनेति रागः** "
            "for the means. This is what 6.4.26's separate "
            "statement was for"),
    Nalopa(
        "6.4.28", does="nipātana", of=("syand",), before=("ghañ",),
        result=("java",), nipatana=True,
        keeps_out="तैलस्यन्दः, घृतस्यन्दः — no speed meant, and "
                  "the न् stays",
        why="स्यदो जवे — स्यद is laid down whole for the sense "
            "SPEED: **गोस्यदः, अश्वस्यदः**. Two things are "
            "निपातन at once — **स्यन्देर् नलोपो वृद्ध्यभावश्च** — "
            "the न् gone and the वृद्धि not made.\\n\\n"
            "**AND ONE PROHIBITION IS NOT IN THE WAY.** "
            "**इक्प्रकरणाद् न धातुलोप० इति प्रतिषेधो नास्ति** — "
            "1.1.4 refuses guṇa and vṛddhi after a root has lost a "
            "sound, but it is stated in the इक् section and does "
            "not reach here"),
    Nalopa(
        "6.4.29", does="nipātana", of=NIPATANA_FIVE, nipatana=True,
        why="अवोदैधोद्मप्रश्रथहिमश्रथाः — five forms laid down "
            "whole: **अवोदः** from उन्द् with अव, **एधः** from "
            "इन्ध्, **ओद्म** from उन्द् with the Uṇādi मन्, "
            "**प्रश्रथः** and **हिमश्रथः** from श्रन्थ्.\\n\\n"
            "**AND TWO OF THEM ARE LAID DOWN FOR TWO THINGS "
            "APIECE.** **एध इति इन्धेर् घञि नलोपो गुणश्च "
            "निपात्यते। न धातुलोप आर्धधातुके इति हि प्रतिषेधः "
            "स्यात्** — the न् gone AND the guṇa made, because "
            "1.1.4 would otherwise have refused the guṇa to a root "
            "that has lost a sound. Same for ओद्म"),
    Nalopa(
        "6.4.30", refuses=True, of=("añc",), result=("pūjā",),
        blocks=("6.4.24",),
        keeps_out="उदक्तम् उदकं कूपात् — **उद्धृतम् इत्यर्थः**, "
                  "drawn up and not honoured, so the न् does go",
        why="न अञ्चेः पूजायाम् — but अञ्च् does not drop its न् "
            "where HONOUR is meant: **अञ्चिता अस्य गुरवः; अञ्चितम् "
            "इव शिरो वहति** — his teachers are honoured; he "
            "carries his head as though it were. The इट् that "
            "makes अञ्चिता is 7.2.53's, stated for the same sense"),
    Nalopa(
        "6.4.31", refuses=True, of=("skand", "syand"),
        before=("ktvā",), blocks=("6.4.24",),
        why="क्त्वि स्कन्दिस्यन्दोः — nor स्कन्द् and स्यन्द् "
            "before क्त्वा: **स्कन्त्वा, स्यन्त्वा**.\\n\\n"
            "**AND FOR ONE OF THE TWO THE REFUSAL IS NOT NEEDED ON "
            "ONE READING.** **स्यन्देर् ऊदित्त्वात् पक्ष इडागमः। "
            "स्यन्दित्वा। तत्र यदा इडागमस् तदा न क्त्वा सेट् इति "
            "कित्त्वप्रतिषेधाद् एव नलोपाभावः** — with the इट् in, "
            "1.2.18 takes the कित् away and 6.4.24 could not have "
            "applied anyway"),
    Nalopa(
        "6.4.32", refuses=True, gana="j-anta", of=("naś",),
        before=("ktvā",), optional=True, blocks=("6.4.24",),
        why="जान्तनशां विभाषा — and ज्-final stems and नश् refuse "
            "it OPTIONALLY before क्त्वा: **रङ्क्त्वा / रक्त्वा; "
            "भङ्क्त्वा / भक्त्वा; नंष्ट्वा / नष्ट्वा**, and "
            "**इट्पक्षे नशित्वा** for a third"),
    Nalopa(
        "6.4.33", does="na-lopa", of=("bhañj",), before=("ciṇ",),
        optional=True,
        why="भञ्जेश्च चिणि — भञ्ज् drops the न् before चिण् "
            "OPTIONALLY: **अभाजि / अभञ्जि**.\\n\\n"
            "**AND IT READS AS A REFUSAL AND IS NOT ONE.** "
            "**अप्राप्तोऽयं नलोपः पक्षे विधीयते। ततो नेति "
            "नानुवर्तते** — the loss was never available before "
            "चिण्, so this sūtra GRANTS it optionally rather than "
            "withholding it, and the न of 6.4.30 does not carry "
            "down into it. Three refusals in a row and then one "
            "that only looks like a fourth"),
)


def _reaches(row: Nalopa, stem: str, gana: str, before: str,
             result: str) -> bool:
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.result and result not in row.result:
        return False
    if row.excludes and (stem in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Nalopa, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.does and not row.refuses


def _how_specific(row: Nalopa, stem: str, gana: str) -> int:
    """
    A refusal beats what it refuses, and a named stem beats a
    named class.

    6.4.24 reaches every consonant-final stem without an इ marker,
    which is most of what the run is about; 6.4.30, 6.4.31 and
    6.4.32 each carve a piece out of it by naming stems.
    """
    return (
        10 * bool(row.refuses)
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.before)
    )


@dataclass(frozen=True)
class Dropped:
    """What the run answers: whether the न् goes, and by which."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def n_goes(stem: str = "", *, gana: str = "", before: str = "",
           result: str = "", wants: str = "") -> Dropped:
    """
    6.4.23–33 — whether the stem loses its न्.

    Nothing answers by default: where no rule is reached the न्
    stays, which is what नन्द्यते and रङ्गः are.
    """
    matched = [
        row for row in NALOPA_TABLE
        if _reaches(row, stem, gana, before, result)
        and _supplies(row, wants)
    ]
    if not matched:
        return Dropped(
            "", "", "No rule of 6.4.23–33 is reached, so the न् "
                    "stays where it is")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Dropped("" if row.refuses else row.does, row.sutra,
                   row.why, optional=row.optional,
                   nipatana=row.nipatana, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Nalopa, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NALOPA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Nalopa", "NALOPA_TABLE", "NALOPA_RUN", "ASIDDHAVAT",
    "SAPI_ROOTS", "RANJ", "NIPATANA_FIVE", "LANGI_KAMPI",
    "Dropped", "n_goes", "provisions_for",
]
