# -*- coding: utf-8 -*-
"""
७.३.७०–८३ — before a शित्, and the guṇa that closes the run.

Fourteen sūtras, and most of them are why the present tense of a
root looks nothing like the root. पा becomes पिब and स्था becomes
तिष्ठ and दृश् becomes पश्य (7.3.78); शम् and seven more lengthen
their vowel (शाम्यति, ताम्यति); इष् and गम् and यम् take a छ्
(इच्छति, गच्छति, यच्छति); ज्ञा becomes जा (जानाति); and the
प्वादि roots shorten (पुनाति, लुनाति).

**7.3.78 IS THE LARGEST ONE-TO-ONE SUBSTITUTION IN THE BOOK.**
Eleven roots against eleven stems, matched in order: पा→पिब,
घ्रा→जिघ्र, ध्मा→धम, स्था→तिष्ठ, म्ना→मन, दाण्→यच्छ, दृश्→पश्य,
ऋ→ऋच्छ, सृ→धौ, शद्→शीय, सद्→सीद. Crossing any pair is not
Sanskrit, and the vṛtti argues about the accent and the guṇa of
पिब in the same breath.

**AND THE RUN ENDS ON THE GUṆA IT HAS BEEN CLEARING THE WAY
FOR.** 7.3.83 gives it before जुस् and 7.3.84 — codified long
before this pāda was read — before every सार्वधातुक and
आर्धधातुक. The vṛtti at 7.3.83 works out why चिनुयुः has none,
there being two ङित्-conditions in play and this rule displacing
only one of them.

**WHAT THIS MODULE DOES NOT DO.** It says what the stem becomes
before a शित्. Which शित् it is — शप्, श्यन्, श्ना — is 3.1's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
SITI_RUN: Tuple[str, str] = ("7.3.70", "7.3.83")

#: 7.3.84, the guṇa this run ends by clearing the way for, was
#: codified long before the pāda was read through.
CODIFIED_APART: Tuple[str, ...] = ("7.3.84",)

#: 7.3.74's eight, which lengthen before श्यन् — the same eight
#: the तच्छील run names, so they are asked for rather than
#: written out again.
from src.astadhyayi.tacchila import SAMADI as SAMADI_EIGHT  # noqa: E402

#: 7.3.77's three, which take a छ्.
ISU_GAM_YAM: Tuple[str, ...] = ("iṣ", "gam", "yam")

#: 7.3.78's eleven, matched one to one and in order.
PIBADI: Tuple[Tuple[str, str], ...] = (
    ("pā", "piba"), ("ghrā", "jighra"), ("dhmā", "dhama"),
    ("sthā", "tiṣṭha"), ("mnā", "mana"), ("dāṇ", "yaccha"),
    ("dṛś", "paśya"), ("ṛ", "ṛccha"), ("sṛ", "dhau"),
    ("śad", "śīya"), ("sad", "sīda"))

#: 7.3.73's four, whose क्स is optionally dropped.
DUHADI: Tuple[str, ...] = ("duh", "dih", "lih", "guh")


@dataclass(frozen=True)
class Siti:
    """One rule of 7.3.70–83: what the stem does before a शित्."""

    sutra: str
    #: `lopa`, `dīrgha`, `hrasva`, `cha`, `guṇa`, `jā` — or the
    #: substitute where the rule matches one to one.
    does: str = ""
    #: The roots named outright.
    of: Tuple[str, ...] = ()
    #: The root class instead.
    gana: str = ""
    #: Where root and substitute are matched one to one.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: परस्मैपद or आत्मनेपद.
    pada: str = ""
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


SITI_TABLE: Tuple[Siti, ...] = (
    Siti(
        "7.3.70", does="lopa", gana="ghu", before=("leṭ",),
        optional=True,
        keeps_out="यद् अग्निर् अग्नये ददात् — the loss does not "
                  "come, and the आट् augment gets the same form "
                  "in any case",
        why="घोर्लोपो लेटि वा — a घु root OPTIONALLY loses its "
            "vowel before लेट्: **दधद् रत्नानि दाशुषे; सोमो "
            "ददद् गन्धर्वाय**. And वा is said "
            "**विस्पष्टार्थम्** — someone might have feared "
            "that a loss stated at all would displace ददात्, "
            "which comes by another road"),
    Siti(
        "7.3.71", does="lopa", gana="o-anta", before=("śyan",),
        why="ओतः श्यनि — an ओ-final stem loses it before श्यन्: "
            "**निश्यति, अवच्छ्यति, अवद्यति, अवस्यति**. Four "
            "roots and four forms, and each of the four is an "
            "ओ-final root of the दिवादि class, which is where "
            "the श्यन् comes from at all"),
    Siti(
        "7.3.72", does="lopa", of=("ksa",), before=("ac",),
        keeps_out="अधुक्षत्, अधुक्षताम् — a consonant-initial "
                  "ending; उत्सौ, वत्साः — no क्स affix at all, "
                  "and the क् in the sūtra is what shuts them out",
        why="क्सस्याचि — the क्स affix loses its vowel before a "
            "vowel-initial ending: **अधुक्षाताम्, अधुक्षाथाम्, "
            "अधुक्षि**"),
    Siti(
        "7.3.73", does="luk", of=DUHADI, before=("dantya",),
        pada="ātmanepada", optional=True, blocks=("7.3.72",),
        keeps_out="व्यत्यपुक्षत — not one of the four; अधुक्षत् — "
                  "परस्मैपद; अधुक्षामहि — the ending does not "
                  "begin with a dental",
        why="लुग्वा दुहदिहलिहगुहामात्मनेपदे दन्त्ये — four roots "
            "OPTIONALLY drop the whole क्स in the आत्मनेपद "
            "before a dental: **अदुग्ध, अधुक्षत; अदुग्धाः, "
            "अधुक्षथाः; अदिग्ध, अधिक्षत; अलीढ, अलिक्षत; "
            "न्यगूढ, न्यघुक्षत**. लुक् is said rather than लोप "
            "**सर्वादेशार्थम्, तच्च वह्यर्थम्** — so that "
            "अदुह्वहि may come out, where dropping the last "
            "sound only would leave the wrong thing behind"),
    Siti(
        "7.3.74", does="dīrgha", of=SAMADI_EIGHT, before=("śyan",),
        keeps_out="अस्यति — not one of the eight; भ्रमति, बभ्राम "
                  "— no श्यन्, 3.1.70 making it optional",
        why="शमामष्टानां दीर्घः श्यनि — eight roots lengthen "
            "before श्यन्: **शाम्यति, ताम्यति, दाम्यति, "
            "श्राम्यति, भ्राम्यति, क्षाम्यति, क्लाम्यति, "
            "माद्यति**"),
    Siti(
        "7.3.75", does="dīrgha", of=("ṣṭhivu", "klami", "ācam"),
        before=("śit",),
        keeps_out="चमति, विचमति — चम् without आङ्, which the "
                  "sūtra's आ shuts out",
        why="ष्ठिवुक्लम्याचमां शिति — and three roots before any "
            "शित्: **ष्ठीवति, क्लामति, आचामति**. क्लम् is named "
            "again although 7.3.74 has it, **शबर्थम्** — for "
            "the शप् conjugation, which श्यन् did not reach"),
    Siti(
        "7.3.76", does="dīrgha", of=("kram",), before=("śit",),
        pada="parasmaipada",
        keeps_out="आक्रमत आदित्यः — आत्मनेपद",
        why="क्रमः परस्मैपदेषु — क्रम् lengthens before a शित् "
            "followed by a परस्मैपद ending: **क्रामति, "
            "क्रामतः, क्रामन्ति**.\\n\\n"
            "**AND उत्क्राम KEEPS ITS LENGTH THOUGH ITS ENDING "
            "IS GONE.** 1.1.63 should have stopped the rule "
            "reaching once the हि is elided; **न च हौ क्रमिर् "
            "अङ्गम्। किं तर्हि? शपि** — the stem the rule works "
            "on is the one before the शप्, not the one before "
            "the हि, so the prohibition does not bite"),
    Siti(
        "7.3.77", does="cha", of=ISU_GAM_YAM, before=("śit",),
        keeps_out="इष्यति, इष्णाति — the other two roots of that "
                  "shape, which the उदित् marking shuts out; "
                  "इषाण — a शित् that is not a vowel",
        why="इषुगमियमां छः — इष्, गम् and यम् take a छ् before a "
            "शित्: **इच्छति, गच्छति, यच्छति**. The इष् meant is "
            "the उदित् one, and readers who do not so read it "
            "carry अचि down from 7.3.72 instead — "
            "**तत् च प्रधानम् अज्ग्रहणं शितीत्यनेन विशेष्यत इति "
            "वर्णयन्ति**"),
    Siti(
        "7.3.78", pairs=PIBADI,
        of=tuple(one for one, _ in PIBADI), before=("śit",),
        why="पाघ्राध्मास्थाम्नादाण्दृश्यर्त्तिसर्त्तिशदसदां "
            "पिबजिघ्रधमतिष्ठमनयच्छपश्यर्च्छधौशीयसीदाः — eleven "
            "roots and eleven stems, matched ONE TO ONE: "
            "**पिबति, जिघ्रति, धमति, तिष्ठति, मनति, यच्छति, "
            "पश्यति, ऋच्छति, धावति, शीयते, सीदति**. The longest "
            "यथासंख्यम् of the pāda, and crossing any pair is "
            "not Sanskrit.\\n\\n"
            "**AND THE vṛtti ARGUES ABOUT पिब TWICE OVER.** The "
            "light penult should take guṇa; **अङ्गवृत्ते "
            "पुनर्वृत्ताव् अविधिर् निष्ठितस्य** stops it. And "
            "whether the substitute is आ-final and आद्युदात्त is "
            "a second question the vṛtti raises in the same "
            "breath"),
    Siti(
        "7.3.79", does="jā", of=("jñā", "jan"), before=("śit",),
        why="ज्ञाजनोर्जा — ज्ञा and जन् become जा before a शित्: "
            "**जानाति, जायते**. The जन् meant is the दैवादिक "
            "one, **जनेर् दैवादिकस्य ग्रहणम्**"),
    Siti(
        "7.3.80", does="hrasva", gana="pū-ādi", before=("śit",),
        why="प्वादीनां ह्रस्वः — the प्वादि roots shorten before "
            "a शित्: **पुनाति, लुनाति, स्तृणाति**.\\n\\n"
            "**AND WHERE THE LIST ENDS IS DISPUTED.** "
            "**केचिद् इच्छन्ति** it runs from पूञ् to प्ली, the "
            "वृत् of the धातुपाठ marking the end of both the "
            "ल्वादि and the प्वादि; **अपरे तु... आगणान्ताः "
            "प्वादय इति**, to the end of the whole class. On "
            "the second reading जानाति would shorten too, and "
            "7.3.79's जा is what saves it"),
    Siti(
        "7.3.81", does="hrasva", of=("mī",), before=("śit",),
        chandasi=True,
        keeps_out="प्रमीणाति — outside the Veda",
        why="मीनातेर्निगमे — and मी shortens in the Veda: "
            "**प्रमिणन्ति व्रतानि**, they transgress the vows. "
            "**निगम इति किम्? प्रमीणाति** — outside the Veda the "
            "long vowel stands, and निगम is the word used for "
            "the Veda where छन्दसि would have done"),
    Siti(
        "7.3.82", does="guṇa", of=("mid",), before=("śit",),
        keeps_out="मिद्यते — the यक् of the passive is no शित्",
        why="मिदेर्गुणः — मिद्'s इ takes guṇa before a शित्: "
            "**मेद्यति, मेद्यतः, मेद्यन्ति**. **शितीत्येव — "
            "मिद्यते** — the passive's यक् is no शित्, so the "
            "vowel stays short there, and one root shows both "
            "forms side by side"),
    Siti(
        "7.3.83", does="guṇa", gana="ik-anta", before=("jus",),
        why="जुसि च — and an इक्-final stem takes guṇa before "
            "जुस्: **अजुहवुः, अबिभयुः, अबिभरुः**.\\n\\n"
            "**AND WHY चिनुयुः HAS NONE IS WORKED OUT IN FULL.** "
            "Two ङित्-conditions are in play there, one from the "
            "सार्वधातुक and one from the यासुट्. This rule "
            "displaces the first, having nowhere else to apply "
            "against it — **नाप्राप्ते... प्रतिषेधे जुसि गुण "
            "आरभ्यमाणस्तम् एव बाधते** — but not the second, "
            "which it meets in a place where it could have "
            "applied anyway, **तत्र हि प्राप्ते चाप्राप्ते "
            "चारभ्यत इति**"),
)


def _reaches(row: Siti, root: str, gana: str, before: str,
             pada: str, chandasi: bool) -> bool:
    if row.pairs and root and root not in dict(row.pairs):
        return False
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.pada and pada != row.pada:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _becomes(row: Siti, root: str) -> str:
    """The substitute, where the rule matches one to one."""
    for named, shape in row.pairs:
        if named == root:
            return shape
    return row.does


def _how_specific(row: Siti, root: str, gana: str) -> int:
    """
    A rule that names what it displaces beats it, a named root
    beats a class, and a one-to-one pairing beats both.

    7.3.72 against 7.3.73 needs the first, 7.3.80 against 7.3.79
    the second: on one reading of the प्वादि list जानाति would
    shorten, and the substitute जा is what keeps it long.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.pairs and root in dict(row.pairs))
        + 6 * bool(row.of and root in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.pada)
        + 2 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Shaped:
    """What the run answers: the stem's shape before a शित्."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_sit(root: str = "", *, gana: str = "",
               before: str = "", pada: str = "",
               chandasi: bool = False, wants: str = "") -> Shaped:
    """
    7.3.70–83 — what the stem becomes before a शित्.

    Nothing answers by default. पच् and पठ् go into the present
    unchanged, and this run is the roots that do not.
    """
    matched = [
        row for row in SITI_TABLE
        if _reaches(row, root, gana, before, pada, chandasi)
        and (not wants or wants == _becomes(row, root))
    ]
    if not matched:
        return Shaped(
            "", "", "No rule of 7.3.70-83 is reached, so the "
                    "stem goes in as it is")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Shaped(_becomes(row, root), row.sutra, row.why,
                  optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Siti, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SITI_TABLE if row.sutra == sutra_id)


__all__ = [
    "Siti", "SITI_TABLE", "SITI_RUN", "CODIFIED_APART",
    "SAMADI_EIGHT", "ISU_GAM_YAM", "PIBADI", "DUHADI", "Shaped",
    "before_sit", "provisions_for",
]
