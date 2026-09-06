# -*- coding: utf-8 -*-
"""
७.४.२५–४० — the vowel lengthened before य्, and the क्यच् block.

Sixteen sūtras. 7.4.25 lengthens a vowel-final stem before a
क्ङित् य् that is neither a कृत् nor a सार्वधातुक — भृशायते,
चीयते, स्तूयते — and 7.4.26 does the same before च्वि,
शुचीकरोति. Then ऋ takes रीङ् (मात्रीयति), रिङ् (क्रियते), or
guṇa (स्मर्यते) according to what follows, and an अ-final stem
becomes ई before च्वि and क्यच् (शुक्लीभवति, पुत्रीयति).

**AND SIX SŪTRAS THEN LAY DOWN WHAT THE VEDA HAS INSTEAD.**
अशनाय of hunger and अशनीयति otherwise; उदन्य of thirst; धनाय of
greed; and then दुरस्युः, द्रविणस्युः, वृषण्यति, रिषण्यति —
Vedic forms each recorded against what the ordinary grammar owed.
7.4.35 refuses the whole of 7.4.25 and 7.4.33 in the Veda except
for पुत्र, which is why पुत्रीयन्तः stands beside मित्रयुः.

**WHAT THIS MODULE DOES NOT DO.** It says what the stem's vowel
becomes. The क्यच् itself is 3.1.8's and the च्वि 5.4.50's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
DIRGHA_RUN: Tuple[str, str] = ("7.4.25", "7.4.40")

#: Where the run turns to क्यच् and the Veda.
KYAC_FROM: str = "7.4.33"

#: 7.4.34's three, each laid down against one sense.
ASANAYADI: Tuple[Tuple[str, str], ...] = (
    ("aśanāya", "bubhukṣā"), ("udanya", "pipāsā"),
    ("dhanāya", "gardha"))

#: 7.4.36's four Vedic forms, and what each displaces.
CHANDASI_FOUR: Tuple[Tuple[str, str], ...] = (
    ("durasyu", "duṣṭīyati"), ("draviṇasyu", "draviṇīyati"),
    ("vṛṣaṇyati", "vṛṣīyati"), ("riṣaṇyati", "riṣṭīyati"))

#: 7.4.40's four, whose vowel becomes इ before a त-initial कित्.
DYATI_FOUR: Tuple[str, ...] = ("dyati", "syati", "mā", "sthā")


@dataclass(frozen=True)
class Dirgha:
    """One rule of 7.4.25–40: the vowel before य्, च्वि or क्यच्."""

    sutra: str
    #: `dīrgha`, `rīṅ`, `riṅ`, `guṇa`, `ī`, `it`, `lopa`, `āt` —
    #: or "" where the rule refuses.
    does: str = ""
    #: The stems named outright.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: The sense that licenses the form.
    sense: str = ""
    #: What the ordinary grammar would have given.
    instead_of: str = ""
    refuses: bool = False
    nipatana: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


DIRGHA_TABLE: Tuple[Dirgha, ...] = (
    Dirgha(
        "7.4.25", does="dīrgha", gana="ac-anta",
        before=("a-kṛt-a-sārvadhātuka-ya-kṅit",),
        keeps_out="प्रकृत्य, प्रहृत्य — a कृत्'s य्, and the "
                  "lengthening would have displaced the तुक्; "
                  "चिनुयात्, सुनुयात् — a सार्वधातुक; उरुया, "
                  "धृष्णुया — the affix is not क्ङित्",
        why="अकृत्सार्वधातुकयोर्दीर्घः — a vowel-final stem "
            "lengthens before a क्ङित् य् that is neither a "
            "कृत्'s nor a सार्वधातुक's: **भृशायते, सुखायते, "
            "दुःखायते; चीयते, चेचीयते; स्तूयते, तोष्टूयते; "
            "चीयात्, स्तूयात्**"),
    Dirgha(
        "7.4.26", does="dīrgha", gana="ac-anta", before=("cvi",),
        why="च्वौ च — and before च्वि: **शुचीकरोति, शुचीभवति, "
            "शुचीस्यात्; पटूकरोति, पटूभवति, पटूस्यात्**"),
    Dirgha(
        "7.4.27", does="rīṅ", gana="ṛ-anta",
        before=("a-kṛt-a-sārvadhātuka-ya", "cvi"),
        blocks=("7.4.25",),
        keeps_out="चेकीर्यते, निजेगिल्यते — the vowel is long ॠ, "
                  "which the तपर shuts out",
        why="रीङ् ऋतः — an ऋ-final stem takes रीङ् instead: "
            "**मात्रीयति, मात्रीयते; पित्रीयति, पित्रीयते; "
            "चेक्रीयते; मात्रीभूतः**. And क्ङिति has lapsed "
            "here — **क्ङिति इत्येतन् निवृत्तम्** — so पित्र्यम् "
            "comes out too"),
    Dirgha(
        "7.4.28", does="riṅ", gana="ṛ-anta",
        before=("śa", "yak", "liṅ"), blocks=("7.4.27",),
        keeps_out="बिभृयात् — a सार्वधातुक; कृषीष्ट, हृषीष्ट — "
                  "no य् at all",
        why="रिङ् शयग्लिङ्क्षु — but रिङ् before श, यक् and the "
            "optative: **आद्रियते, आध्रियते** for the श; "
            "**क्रियते, ह्रियते** for the यक्; **क्रियात्, "
            "ह्रियात्** for the optative. **रिङ्वचनं "
            "दीर्घनिवृत्त्यर्थम्** — a short substitute stated "
            "so that the lengthening shall not come"),
    Dirgha(
        "7.4.29", does="guṇa", of=("ṛ",),
        gana="ṛ-anta-saṃyoga-ādi", before=("yak", "liṅ"),
        blocks=("7.4.28",),
        keeps_out="स्वृषीष्ट, ध्वृषीष्ट — no य्; इयृयात् — a "
                  "सार्वधातुक",
        why="गुणोऽर्तिसंयोगाद्योः — and ऋ, and an ऋ-final root "
            "beginning with a cluster, take guṇa: **अर्यते, "
            "अर्यात्; स्मर्यते, स्मर्यात्**. संस्क्रियते has "
            "none, its सुट् being either असिद्ध or no part of "
            "the stem — **बहिरङ्गलक्षणस्य असिद्धत्वाद् "
            "अभक्तत्वाद् वा**"),
    Dirgha(
        "7.4.30", does="guṇa", of=("ṛ",),
        gana="ṛ-anta-saṃyoga-ādi", before=("yaṅ",),
        blocks=("7.4.28",),
        why="यङि च — and before यङ्: **अरार्यते, सास्वर्यते, "
            "दाध्वर्यते, सास्मर्यते**. A vārttika adds a form "
            "for हन् in the sense of harming — "
            "**हन्तेर्हिंसायां यङि घ्नीभावो वक्तव्यः। "
            "जेघ्नीयते** — as against जङ्घन्यते in any other"),
    Dirgha(
        "7.4.31", does="ī", of=("ghrā", "dhmā"), before=("yaṅ",),
        why="ई घ्राध्मोः — घ्रा and ध्मा become ई before यङ्: "
            "**जेघ्रीयते, देध्मीयते**. Both roots end in आ and "
            "7.4.25 would have lengthened it to no purpose; the "
            "substitute is a different vowel and not a longer "
            "one, which is the whole content of the rule"),
    Dirgha(
        "7.4.32", does="ī", gana="a-varṇa-anta", before=("cvi",),
        blocks=("7.4.26",),
        why="अस्य च्वौ — an अ-final stem becomes ई before च्वि: "
            "**शुक्लीभवति, शुक्लीस्यात्; खट्वीकरोति, "
            "खट्वीस्यात्**"),
    Dirgha(
        "7.4.33", does="ī", gana="a-varṇa-anta", before=("kyac",),
        blocks=("7.4.25",),
        why="क्यचि च — and before क्यच्: **पुत्रीयति, घटीयति, "
            "खट्वीयति, मालीयति**. **अकृत्सार्वधातुकयोर्दीर्घः "
            "इत्यस्य अपवादः** — an exception to the lengthening, "
            "and stated as a sūtra of its own "
            "**उत्तरार्थम्**, for the six rules that follow"),
    Dirgha(
        "7.4.34", does="āt", of=tuple(one for one, _ in ASANAYADI),
        before=("kyac",), nipatana=True,
        keeps_out="अशनीयति, उदकीयति, धनीयति — in any other sense",
        why="अशनायोदन्यधनाया बुभुक्षापिपासागर्द्धेषु — three "
            "forms laid down against three senses: "
            "**अशनायति** of HUNGER, **उदन्यति** of THIRST, "
            "**धनायति** of GREED. Each has its ordinary "
            "ई-form beside it in any other sense, and उदन्य "
            "changes the whole word — **उदकशब्दस्य उदन्नादेशो "
            "निपात्यते**"),
    Dirgha(
        "7.4.35", refuses=True, gana="a-varṇa-anta",
        before=("kyac",), chandasi=True,
        blocks=("7.4.25", "7.4.33"),
        keeps_out="पुत्रीयन्तः सुदानवः — पुत्र, named out; and a "
                  "vārttika widens the exception, "
                  "**अपुत्रादीनाम् इति वक्तव्यम्**",
        why="न च्छन्दस्यपुत्रस्य — in the Veda an अ-final stem "
            "takes NEITHER the lengthening nor the ई before "
            "क्यच्, पुत्र excepted: **मित्रयुः, संस्वेदयुः; "
            "देवाञ् जिगाति सुम्नयुः**. **किं चोक्तम्? दीर्घत्वम् "
            "ईत्वं च** — the vṛtti has to say which two rules "
            "the *what is said* means"),
    Dirgha(
        "7.4.36", does="nipātana",
        of=tuple(one for one, _ in CHANDASI_FOUR),
        chandasi=True, nipatana=True,
        why="दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति — four Vedic "
            "forms laid down, each against what was due: "
            "**अवियोना दुरस्युः** where दुष्टीयति was owed; "
            "**द्रविणस्युर् विपन्यया** for द्रविणीयति; "
            "**वृषण्यति** for वृषीयति; **रिषण्यति** for "
            "रिष्टीयति"),
    Dirgha(
        "7.4.37", does="āt", of=("aśva", "agha"), before=("kyac",),
        chandasi=True,
        why="अश्वाघस्यात् — अश्व and अघ take आ before क्यच् in "
            "the Veda: **अश्वायन्तो मघवन्; मा त्वा वृका अघायवो "
            "विदन्**. And this आ is itself read as proof that "
            "7.4.35's refusal covers the lengthening — "
            "**एतद् एव आत्ववचनं ज्ञापकं न च्छन्दस्यपुत्रस्य इति "
            "दीर्घप्रतिषेधो भवतीति**"),
    Dirgha(
        "7.4.38", does="āt", of=("deva", "sumna"),
        before=("kyac",), chandasi=True, sense="kāṭhaka-yajus",
        keeps_out="देवाञ् जिगाति सुम्नयुः — not in a यजुस्; "
                  "सुम्नयुरिदमसि — not in the Kāṭhaka",
        why="देवसुम्नयोर्यजुषि काठके — and देव and सुम्न take it "
            "in the Kāṭhaka's यजुस् alone: **देवायते "
            "यजमानाय; सुम्नायन्तो हवामहे**. Two conditions on "
            "one form, and the vṛtti tests each"),
    Dirgha(
        "7.4.39", does="lopa", of=("kavi", "adhvara", "pṛtanā"),
        before=("kyac",), chandasi=True, sense="ṛc",
        why="कव्यध्वरपृतनस्यर्चि लोपः — कवि, अध्वर and पृतना lose "
            "their last vowel before क्यच् in a ऋच्: "
            "**कव्यन्तः सुमनसः; अध्वर्यन्तः; पृतन्यन्तस् "
            "तिष्ठन्ति**"),
    Dirgha(
        "7.4.40", does="it", of=DYATI_FOUR,
        before=("ta-ādi-kit",),
        keeps_out="अवदाय — the affix does not begin with त्; "
                  "अवदाता — it is not कित्",
        why="द्यतिस्यतिमास्थामित्ति किति — द्यति, स्यति, मा and "
            "स्था take इ before a त-initial कित्: **निर्दितः, "
            "निर्दितवान्; अवसितः, अवसितवान्; मितः, मितवान्; "
            "स्थितः, स्थितवान्**"),
)


def _reaches(row: Dirgha, stem: str, gana: str, before: str,
             sense: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Dirgha, stem: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, a named
    stem beats a class, and a named sense beats both.

    7.4.25 against 7.4.27, 7.4.28, 7.4.29 and 7.4.33 is what
    needs it: one rule lengthens every vowel-final stem before a
    क्ङित् य्, and four give particular stems something else.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.sense)
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Shaped:
    """What the run answers: the vowel's change, or a form."""

    does: str
    sutra: str
    why: str
    instead_of: str = ""
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_ya(stem: str = "", *, gana: str = "", before: str = "",
              sense: str = "", chandasi: bool = False) -> Shaped:
    """
    7.4.25–40 — the stem's vowel before य्, च्वि and क्यच्.

    Nothing answers by default. A consonant-final stem before any
    of these affixes takes nothing from the run.
    """
    matched = [
        row for row in DIRGHA_TABLE
        if _reaches(row, stem, gana, before, sense, chandasi)
    ]
    if not matched:
        return Shaped(
            "", "", "No rule of 7.4.25-40 is reached, so the "
                    "stem's vowel stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Shaped("" if row.refuses else row.does, row.sutra,
                  row.why, instead_of=row.instead_of,
                  nipatana=row.nipatana, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Dirgha, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in DIRGHA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Dirgha", "DIRGHA_TABLE", "DIRGHA_RUN", "KYAC_FROM",
    "ASANAYADI", "CHANDASI_FOUR", "DYATI_FOUR", "Shaped",
    "before_ya", "provisions_for",
]
