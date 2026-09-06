# -*- coding: utf-8 -*-
"""
६.४.१५४–१७५ — इष्ठ, इमन्, ईयस्, and the stems that stand unchanged.

The last twenty-two sūtras of अध्याय ६, still under 6.4.129's
भस्य, and they fall into two halves that pull opposite ways.

**The first half takes things away, and sometimes the whole word
with them.** Before इष्ठन्, इमनिच् and ईयसुन्, a stem loses its
तृ (6.4.154) or its टि (6.4.155); स्थूल and five others lose
everything from a semivowel onward and take guṇa besides
(6.4.156); ten stems are simply replaced by something shorter,
matched one to one (6.4.157); and बहु loses the affix itself and
becomes भू (6.4.158). पटिष्ठः, स्थविष्ठः, प्रेष्ठः, भूमा.

**The second half puts nothing anywhere.** From 6.4.163 the word
is प्रकृत्या — the stem STANDS: स्रजिष्ठः keeps its ज्, सामनः
keeps its अन्, पाणिनः keeps its इन्. Eleven sūtras whose whole
content is that the losses just prescribed do not happen.

**AND THE PĀDA ENDS ON TWO LISTS OF निपातन.** 6.4.174 gives
eleven words laid down whole and 6.4.175 five more for the Veda —
दाण्डिनायन, हिरण्मय, ऋत्व्य, माध्वी. The adhyāya closes by naming
what no rule of it reaches.

**WHAT THIS MODULE DOES NOT DO.** It reports what is lost, what
replaces it, or that nothing happens — and which rule says so. It
does not compare: that पटु with इष्ठन् MEANS *most clever* is
5.3.55's business.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch, closing the adhyāya.
ISTHA_RUN: Tuple[str, str] = ("6.4.154", "6.4.175")

#: Where प्रकृत्या takes over from the losses.
PRAKRTI_FROM: str = "6.4.163"

#: The three affixes the whole first half is stated before.
ISTHA_THREE: Tuple[str, ...] = ("iṣṭhan", "imanic", "īyasun")

#: 6.4.156's six, which lose everything from a semivowel on and
#: take guṇa besides.
STHULADI: Tuple[str, ...] = (
    "sthūla", "dūra", "yuvan", "hrasva", "kṣipra", "kṣudra")

#: 6.4.157's ten, matched one to one with what replaces them.
YATHASAMKHYAM_TEN: Tuple[Tuple[str, str], ...] = (
    ("priya", "pra"), ("sthira", "stha"), ("sphira", "spha"),
    ("uru", "var"), ("bahula", "baṃhi"), ("guru", "gar"),
    ("vṛddha", "varṣi"), ("tṛpra", "trap"), ("dīrgha", "drāghi"),
    ("vṛndāraka", "vṛnda"))

#: 6.4.165's five, which stand unchanged before अण्.
GATHIN_FIVE: Tuple[str, ...] = (
    "gāthin", "vidathin", "keśin", "gaṇin", "paṇin")

#: 6.4.174's eleven, laid down whole.
NIPATANA_ELEVEN: Tuple[str, ...] = (
    "dāṇḍināyana", "hāstināyana", "ātharvaṇika", "jaihmāśineya",
    "vāsināyani", "bhrauṇahatya", "dhaivatya", "sārava",
    "aikṣvāka", "maitreya", "hiraṇmaya")

#: And 6.4.175's five, for the Veda.
NIPATANA_VEDIC: Tuple[str, ...] = (
    "ṛtvya", "vāstvya", "vāstva", "mādhvī", "hiraṇyaya")


@dataclass(frozen=True)
class Istha:
    """One rule of 6.4.154–175: a loss, a substitute, or nothing."""

    sutra: str
    #: lopa, ṭi-lopa, guṇa, ādeśa, bhū, yiṭ, āt, ra —
    #: or `prakṛtyā`, where the rule's content is that nothing
    #: happens.
    does: str = ""
    #: The stems the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of stem instead.
    gana: str = ""
    #: Where stem and substitute are matched one to one.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: What part of the stem is affected.
    part: str = ""
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ISTHA_TABLE: Tuple[Istha, ...] = (
    Istha(
        "6.4.154", does="lopa", of=("tṛ",), before=ISTHA_THREE,
        why="तुरिष्ठेमेयस्सु — तृ is lost before इष्ठन्, इमनिच् "
            "and ईयसुन्: **आसुतिं करिष्ठः; विजयिष्ठः; वहिष्ठः; "
            "दोहीयसी धेनुः**.\\n\\n"
            "**AND THE WHOLE तृ GOES, NOT ITS LAST SOUND.** "
            "**सर्वस्य तृशब्दस्य लोपार्थं वचनम्। अन्त्यस्य हि टेः "
            "इत्येव सिद्धः** — 6.4.155 would have taken the last "
            "part anyway, so this sūtra can only be for the whole. "
            "And **लुगित्येतद् अत्र नानुवर्तते। तथा हि सति न "
            "लुमताङ्ग०...** — a लुक् would have stopped the "
            "affix's own effects by 1.1.63, and a लोप does not"),
    Istha(
        "6.4.155", does="ṭi-lopa", part="ṭi", before=ISTHA_THREE,
        why="टेः — and any भ stem loses its टि before the three: "
            "**पटु — पटिष्ठः, पटिमा, पटीयान्; लघु — लघिष्ठः, "
            "लघिमा, लघीयान्**.\\n\\n"
            "**AND A VĀRTTIKA CARRIES THE WHOLE OF THIS RUN INTO "
            "THE CAUSAL.** **णाविष्ठवत् प्रातिपदिकस्य कार्यं भवति "
            "इति वक्तव्यम्** — before णि a stem is treated as it "
            "would be before इष्ठन्, and the vṛtti lists what that "
            "buys: **पुंवद्भावरभावटिलोपयणादिपरार्थम् — एनीम् "
            "आचष्टे एतयति; श्येतयति**"),
    Istha(
        "6.4.156", does="guṇa", of=STHULADI, part="yaṇ-ādi-para",
        before=ISTHA_THREE,
        why="स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य "
            "च गुणः — six stems lose everything from a semivowel "
            "onward AND take guṇa in what is left: **स्थविष्ठः, "
            "स्थवीयान्; दविष्ठः, दवीयान्; यविष्ठः, यवीयान्; "
            "ह्रसिष्ठः, ह्रसिमा, ह्रसीयान्; क्षेपिष्ठः; "
            "क्षोदिष्ठः**. One rule doing two things, and the "
            "second of them stated because the first would have "
            "left no vowel to strengthen"),
    Istha(
        "6.4.157", does="ādeśa", pairs=YATHASAMKHYAM_TEN,
        of=tuple(one for one, _ in YATHASAMKHYAM_TEN),
        before=ISTHA_THREE,
        why="प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां "
            "प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः — ten "
            "stems and ten substitutes, matched ONE TO ONE: "
            "**प्रेष्ठः, प्रेमा, प्रेयान्** for प्रिय; "
            "**स्थेष्ठः, स्थेयान्** for स्थिर; **स्फेष्ठः** for "
            "स्फिर. The longest यथासंख्यम् in the pāda, and "
            "crossing any pair is not Sanskrit"),
    Istha(
        "6.4.158", does="bhū", of=("bahu",), before=ISTHA_THREE,
        why="बहोर्लोपो भू च बहोः — after बहु the three affixes "
            "are themselves LOST, and बहु becomes भू: **भूमा, "
            "भूयान्**.\\n\\n"
            "**AND बहोः IS SAID TWICE FOR A REASON.** **बहोरिति "
            "पुनर्ग्रहणं स्थानित्वप्रतिपत्त्यर्थम्, अन्यथा हि "
            "प्रत्ययानाम् एव भूभावः स्यात्** — with the word said "
            "once, the भू would have replaced the affixes that "
            "were just deleted. Saying it again fixes what the "
            "substitute stands in place of"),
    Istha(
        "6.4.159", does="yiṭ", of=("bahu",), before=("iṣṭhan",),
        blocks=("6.4.158",),
        why="इष्ठस्य यिट् च — but इष्ठन् takes the augment यिट् "
            "instead of going, and बहु still becomes भू: "
            "**भूयिष्ठः**. **लोपापवादो यिडागमः, तस्मिन् इकार "
            "उच्चारणार्थः** — an exception to the loss, and the "
            "इ of the augment is there only to pronounce it by"),
    Istha(
        "6.4.160", does="āt", of=("jya",), before=("īyasun",),
        why="ज्यादाद् ईयसः — after ज्य the ईयस् takes आ: "
            "**ज्यायान्**.\\n\\n"
            "**AND आ IS SAID RATHER THAN LEAVING IT TO THE LOSS.** "
            "**लोपस्य यिटा व्यवहितत्वाद् आद् इत्युच्यते। लोपे हि "
            "सति अकृद्यकारे इति दीर्घत्वेन ज्यायान् इति "
            "सिध्यति** — the यिट् of 6.4.159 stands between, so "
            "the loss cannot reach; hence a substitute of its own"),
    Istha(
        "6.4.161", does="ra", part="ṛ", before=ISTHA_THREE,
        result=("hal-ādi-laghu",),
        keeps_out="पटिष्ठः, पटिमा — no ऋ; ऋजिष्ठः, ऋजिमा — the "
                  "ऋ is not preceded by a consonant; कृष्णिष्ठः, "
                  "कृष्णिमा — not light",
        why="र ऋतो हलादेर्लघोः — an ऋ that is LIGHT and has a "
            "consonant before it becomes र before the three: "
            "**प्रथिष्ठः, प्रथिमा, प्रथीयान्; म्रदिष्ठः, "
            "म्रदिमा, म्रदीयान्**. Three conditions and a "
            "counter-example for each"),
    Istha(
        "6.4.162", does="ra", of=("ṛju",), part="ṛ",
        before=ISTHA_THREE, chandasi=True, optional=True,
        blocks=("6.4.161",),
        why="विभाषर्जोश्छन्दसि — and ऋजु takes it OPTIONALLY in "
            "the Veda, though 6.4.161's condition of a preceding "
            "consonant fails: **रजिष्ठम् अनु नेषि पन्थाम्** "
            "beside **त्वम् ऋजिष्ठः**"),
    Istha(
        "6.4.163", does="prakṛtyā", gana="ekāc", before=ISTHA_THREE,
        keeps_out="वसुमत् — **एकाजिति किम्? वसिष्ठः, वसीयान्**, "
                  "where the stem has more than one vowel and the "
                  "losses do reach it",
        why="प्रकृत्यैकाच् — a भ stem of ONE VOWEL stands "
            "unchanged before the three: **स्रग्विन् — स्रजिष्ठः, "
            "स्रजीयान्, स्रजयति; स्रुग्वत् — स्रुचिष्ठः, "
            "स्रुचीयान्, स्रुचयति**.\\n\\n"
            "**AND FROM HERE THE RUN REVERSES.** Everything from "
            "6.4.154 to 6.4.162 took something away; from this "
            "sūtra to 6.4.173 the word is प्रकृत्या and the "
            "content of each rule is that the loss does NOT "
            "happen. A vārttika adds one more: **प्रकृत्याके "
            "राजन्यमनुष्य...**"),
    Istha(
        "6.4.164", does="prakṛtyā", gana="in-anta", before=("aṇ",),
        excludes=("apatya",),
        keeps_out="दाण्डम् — **अनुदात्तादेरञ्** gives अञ् and not "
                  "अण्, so the condition fails",
        why="इन्नण्यनपत्ये — an इन्-final stem stands unchanged "
            "before अण्, where no DESCENDANT is meant: "
            "**सांकूटिनम्, सांराविणम्, सांमार्जिनम्; स्रग्विण "
            "इदं स्राग्विणम्**. The इनुण् is 3.3.44's and the "
            "अण् 5.4.15's"),
    Istha(
        "6.4.165", does="prakṛtyā", of=GATHIN_FIVE, before=("aṇ",),
        blocks=("6.4.164",),
        why="गाथिविदथिकेशिगणिपणिनश्च — and five stems stand "
            "unchanged before अण् even WHERE a descendant is "
            "meant: **गाथिनोऽपत्यं गाथिनः; वैदथिनः; कैशिनः; "
            "गाणिनः; पाणिनः**. **अपत्यार्थोऽयम् आरम्भः** — the "
            "sūtra exists for exactly the case 6.4.164 shut out. "
            "And the grammarian's own name is one of the five"),
    Istha(
        "6.4.166", does="prakṛtyā", gana="saṃyoga-ādi-in",
        before=("aṇ",), blocks=("6.4.164",),
        why="संयोगादिश्च — and an इन्-final stem BEGINNING with a "
            "cluster, descendant or no: **शङ्खिनोऽपत्यं शाङ्खिनः; "
            "माद्रिणः; वाज्रिणः**"),
    Istha(
        "6.4.167", does="prakṛtyā", gana="an-anta", before=("aṇ",),
        blocks=("6.4.134", "6.4.144"),
        why="अन् — an अन्-final stem stands unchanged before अण्, "
            "**अपत्ये चानपत्ये च**: **सामनः, वैमनः, सौत्वनः, "
            "जैत्वनः**.\\n\\n"
            "**AND THIS IS WHAT 6.4.135's COUNTER-EXAMPLES WERE "
            "POINTING AT.** **अन् इति प्रकृतिभावेन "
            "अल्लोपटिलोपाव् उभाव् अपि न भवतः** — both the "
            "अ-loss of 6.4.134 and the टि-loss of 6.4.144 are "
            "held off at once, which is why सामनः keeps its whole "
            "ending"),
    Istha(
        "6.4.168", does="prakṛtyā", gana="an-anta",
        before=("ya-taddhita",), excludes=("bhāva", "karman"),
        keeps_out="राज्यम् — **राज्ञो भावः कर्म वा**, which the "
                  "sūtra shuts out",
        why="ये चाभावकर्मणोः — and before a य-initial taddhita, "
            "where neither the ACT nor the OBJECT is meant: "
            "**सामसु साधुः सामन्यः; वेमन्यः**. The यक् is "
            "5.1.128's, राजन् standing in its पुरोहितादि list"),
    Istha(
        "6.4.169", does="prakṛtyā", of=("ātman", "adhvan"),
        before=("kha",),
        keeps_out="प्रत्यात्मम्, प्राध्वम् — a समासान्त and no ख",
        why="आत्माध्वानौ खे — आत्मन् and अध्वन् stand unchanged "
            "before ख: **आत्मने हित आत्मनीनः; अध्वानम् अलंगामी "
            "अध्वनीनः**"),
    Istha(
        "6.4.170", refuses=True, gana="ma-pūrva-an",
        before=("aṇ",), result=("apatya",), excludes=("varman",),
        blocks=("6.4.167",),
        keeps_out="सौत्वनः — no म् before the अन्; चार्मणः — no "
                  "descendant meant; चाक्रवर्मणः — वर्मन्, named "
                  "out",
        why="न मपूर्वोऽपत्येऽवर्मणः — but an अन् with a म् before "
            "it does NOT stand unchanged before अण् where a "
            "descendant is meant, वर्मन् excepted: **सुषाम्णोऽपत्यं "
            "सौषामः; चान्द्रसामः**. A vārttika offers an option: "
            "**मपूर्वप्रतिषेधे वा हितनाम्नः इति वक्तव्यम्**"),
    Istha(
        "6.4.171", does="ṭi-lopa", of=("brahman",), before=("aṇ",),
        excludes=("jāti",), nipatana=True,
        keeps_out="ब्राह्मणः — **अपत्ये जाताव् अणि ब्रह्मणष् "
                  "टिलोपो न भवति**",
        why="ब्राह्मोऽजातौ — ब्राह्म is laid down, with the "
            "टि-loss, where no CLASS is meant: **ब्राह्मो गर्भः; "
            "ब्राह्मम् अस्त्रम्; ब्राह्मं हविः**. And it is "
            "reached by dividing the sūtra: **योगविभागोऽत्र "
            "क्रियते। ब्राह्म इत्येतद् अपत्याधिकारेऽपि "
            "सामर्थ्याद् अपत्याद् अन्यत्राणि टिलोपार्थं "
            "निपात्यते**"),
    Istha(
        "6.4.172", does="ṭi-lopa", of=("karman",),
        result=("tācchīlya",), nipatana=True,
        why="कार्मस्ताच्छील्ये — कार्म is laid down with the "
            "टि-loss where a HABIT is meant: **कर्मशीलः कार्मः**, "
            "the ण from 4.4.62.\\n\\n"
            "**AND THE VṚTTI ASKS WHY THE SŪTRA IS THERE AT "
            "ALL.** **यद्येवं किमर्थम् इदम्, नस्तद्धिते इत्येव "
            "टिलोपः सिद्धः? सत्यम् एतत्। ज्ञापकार्थं तु। एतज् "
            "ज्ञापयति — ताच्छीलिके णेऽण्कृत...** — 6.4.144 had "
            "already supplied the loss, so this sūtra can only be "
            "teaching something about the ण of habit"),
    Istha(
        "6.4.173", does="ṭi-lopa", of=("ukṣan",), before=("aṇ",),
        excludes=("apatya",), nipatana=True,
        keeps_out="औक्ष्णः — a descendant, where 6.4.135's "
                  "अ-loss applies instead",
        why="औक्षमनपत्ये — औक्ष is laid down with the टि-loss "
            "where no descendant is meant: **औक्षं पदम्**. "
            "**अनपत्य इति किम्? उक्ष्णोऽपत्यम् औक्ष्णः** — and "
            "there 6.4.135 takes the अ instead, so the two rules "
            "divide उक्षन् between them by sense"),
    Istha(
        "6.4.174", does="nipātana", of=NIPATANA_ELEVEN,
        nipatana=True,
        why="दाण्डिनायनहास्तिनायनाथर्वणिकजैह्माशिनेयवासिनायनि"
            "भ्रौणहत्यधैवत्यसारवैक्ष्वाकमैत्रेयहिरण्मयानि — "
            "eleven words laid down whole. The vṛtti works each "
            "back to a rule it escaped: **दण्डिन् हस्तिन् "
            "इत्येतौ नडादिषु पठ्येते, तयोर् आयने परतः "
            "प्रकृतिभावो निपात्यते** — and it records a "
            "disagreement about the list it appeals to: "
            "**केषांचित् तु हस्तिन् इति नडादिषु न पठ्यते**"),
    Istha(
        "6.4.175", does="nipātana", of=NIPATANA_VEDIC,
        chandasi=True, nipatana=True,
        why="ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि छन्दसि — and "
            "five more for the Veda: **ऋतौ भवम् ऋत्व्यम्; "
            "वास्तौ भवं वास्त्व्यम्; वस्तुनि भवो वास्त्वम्**. "
            "Each is a यण् where the ordinary rule would have "
            "given guṇa — **ऋतु वास्तु इत्येतयोर् यति यणादेशो "
            "निपात्यते** — and this is the last sūtra of "
            "अध्याय ६"),
)


def _reaches(row: Istha, stem: str, gana: str, before: str,
             part: str, result: str, chandasi: bool) -> bool:
    if row.pairs and stem and stem not in dict(row.pairs):
        return False
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.part and part and part != row.part:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.excludes and (stem in row.excludes
                         or gana in row.excludes
                         or result in row.excludes):
        return False
    return True


def _becomes(row: Istha, stem: str) -> str:
    """The substitute, looked up where the rule matches one to one."""
    for named, shape in row.pairs:
        if named == stem:
            return shape
    return row.does


def _supplies(row: Istha, stem: str, wants: str) -> bool:
    if not wants:
        return True
    return wants == _becomes(row, stem) and not row.refuses


def _how_specific(row: Istha, stem: str, gana: str) -> int:
    """
    A refusal beats what it refuses, a rule that names what it
    displaces beats it, and a named stem beats a named class.

    6.4.164 to 6.4.167 are the stretch that needs all of it: one
    holds an इन्-final stem unchanged except for a descendant,
    two then name stems and a class back in, and 6.4.170 refuses
    the lot for an अन् with a म् before it.
    """
    return (
        12 * (0 if row.refuses else len(row.blocks))
        + 10 * bool(row.refuses)
        + 6 * bool(row.pairs and _becomes(row, stem) != row.does)
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Compared:
    """What the run answers: a loss, a substitute, or nothing."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_istha(stem: str = "", *, gana: str = "",
                 before: str = "", part: str = "",
                 result: str = "", chandasi: bool = False,
                 wants: str = "") -> Compared:
    """
    6.4.154–175 — the comparative's losses, and the stems that
    stand unchanged.

    Nothing answers by default: where no rule is reached the stem
    stands as it is — which is also what half of this run says in
    so many words, and the difference is that there a rule says it.
    """
    matched = [
        row for row in ISTHA_TABLE
        if _reaches(row, stem, gana, before, part, result, chandasi)
        and _supplies(row, stem, wants)
    ]
    if not matched:
        return Compared(
            "", "", "No rule of 6.4.154–175 is reached, so the "
                    "stem stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Compared("" if row.refuses else _becomes(row, stem),
                    row.sutra, row.why, optional=row.optional,
                    nipatana=row.nipatana, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Istha, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ISTHA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Istha", "ISTHA_TABLE", "ISTHA_RUN", "PRAKRTI_FROM",
    "ISTHA_THREE", "STHULADI", "YATHASAMKHYAM_TEN", "GATHIN_FIVE",
    "NIPATANA_ELEVEN", "NIPATANA_VEDIC", "Compared",
    "before_istha", "provisions_for",
]
