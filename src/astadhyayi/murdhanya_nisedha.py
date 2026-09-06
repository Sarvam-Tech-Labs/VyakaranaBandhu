# -*- coding: utf-8 -*-
"""
८.३.९०–११९ — the words laid down whole, and the ten refusals.

Thirty sūtras close पाद ८.३, and they fall into two halves that
pull opposite ways. 8.3.90–109 go on giving the cerebral: five
words are laid down outright — **प्रतिष्णातं सूत्रम्** of clean
thread, **कपिष्ठलः** as a family name, **प्रष्ठोऽश्वः** of the
horse that goes in front, **विष्टरो वृक्षः** of a tree, and
**विष्टारः** of a metre — and then eight sūtras name a first
member and a second: गविष्ठिरः, युधिष्ठिरः, विष्ठलम्,
अम्बष्ठः, सुषामा, हरिषेणः.

**AND EACH OF THE FIVE HAS ITS PLAIN FORM BESIDE IT.**
प्रतिस्नातम् anywhere but of thread, कपिस्थलम् where no family
is named, प्रस्थो व्रीहीणाम् of a measure of grain, विस्तरः of
a discourse. The laying-down is one word wide, and the other
word is what shows it.

**AND THEN THE PĀDA TURNS ROUND AND SPENDS TEN SŪTRAS TAKING IT
BACK.** 8.3.110–119: not after a र् and not of six named roots
(**विस्रब्धः, पुनःसृजति**), not of सात् and not at a word's
head (**अग्निसात्, दधिसात्**), not of the aorist's स् before
यङ् (**सेसिच्यते**), not of सेध् where MOTION is meant
(**अभिसेधयति गाः** — but प्रतिषेधयति of forbidding), not of सह्
in the shape सोढ् (**परिसोढा**), not before चङ्, not of सु
before स्य and सन्, not of the LATER स् in a perfect
(**अभिषसाद**, the first cerebral and the second not) — and, in
the Veda, optionally not across the augment (**न्यसीदत्** beside
न्यषीदत्).

**WHAT THIS MODULE DOES NOT DO.** It closes the pāda. 8.4.1
opens the last one, and 8.2.108's संहितायाम् runs on into it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.ru_anunasika import Joined  # noqa: E402

#: This module's stretch, which closes पाद ८.३.
NISEDHA_RUN: Tuple[str, str] = ("8.3.90", "8.3.119")

#: Where the run turns from giving the cerebral to refusing it.
REFUSALS_FROM: str = "8.3.110"

#: 8.3.90–94's five words, laid down whole with a cerebral no
#: rule would have given them.
NIPATANA_FIVE: Tuple[str, ...] = (
    "pratiṣṇāta", "kapiṣṭhala", "praṣṭha", "viṣṭara", "viṣṭāra")

#: 8.3.96's four first members, before स्थल.
VIKUSAMI_FOUR: Tuple[str, ...] = ("vi", "ku", "śami", "pari")

#: 8.3.110's six, whose स् refuses the cerebral by name.
SRPI_SIX: Tuple[str, ...] = (
    "sṛp", "sṛj", "spṛś", "spṛh", "savanādi", "ra-para")

#: 8.3.116's three, which refuse it before चङ्.
STAMBHU_THREE: Tuple[str, ...] = ("stambhu", "sivu", "sah")


@dataclass(frozen=True)
class Nisedha:
    """One rule of 8.3.90–119: a cerebral given or refused."""

    sutra: str
    #: `ṣa`, `nipātana`. A refusing row leaves it empty.
    does: str = ""
    #: The roots or words named outright.
    of: Tuple[str, ...] = ()
    #: The shape of what the rule reaches.
    gana: str = ""
    #: What must stand before.
    after: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    sense: Tuple[str, ...] = ()
    #: A named school's opinion — **एकेषाम्**, three times over.
    view: str = ""
    #: True where the sūtra only keeps the cerebral off.
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NISEDHA_TABLE: Tuple[Nisedha, ...] = (
    Nisedha(
        "8.3.90", does="nipātana", of=("pratiṣṇāta",),
        sense=("sūtra",), nipatana=True,
        keeps_out="प्रतिस्नातम् इत्येव अन्यत्र — anywhere but "
                  "of thread",
        why="सूत्रं प्रतिष्णातम् — **प्रतिष्णातम्** is laid down "
            "where THREAD is meant: **प्रतिष्णातं सूत्रम्**, "
            "**शुद्धम् इत्यर्थः** — clean. Anywhere else the "
            "plain प्रतिस्नातम् stands, and the pair is the "
            "shape every one of the five laid-down words of "
            "this run has"),
    Nisedha(
        "8.3.91", does="nipātana", of=("kapiṣṭhala",),
        sense=("gotra",), nipatana=True,
        keeps_out="कपेः स्थलं कपिस्थलम् — a monkey's ground, "
                  "where no family is named",
        why="कपिष्ठलो गोत्रे — and **कपिष्ठल** as a FAMILY NAME: "
            "**कपिष्ठलो नाम स यस्य कापिष्ठलिः पुत्रः** — the "
            "man whose son is called Kāpiṣṭhali. The "
            "counter-example takes the word apart into its two "
            "members and shows it means something else entirely"),
    Nisedha(
        "8.3.92", does="nipātana", of=("praṣṭha",),
        sense=("agragāmin",), nipatana=True,
        keeps_out="प्रस्थे हिमवतः पुण्ये; प्रस्थो व्रीहीणाम् — "
                  "a tableland, and a measure of grain",
        why="प्रष्ठोऽग्रगामिनि — and **प्रष्ठ** of one who goes "
            "IN FRONT: **प्रतिष्ठत इति प्रष्ठोऽश्वः। अग्रतो "
            "गच्छति इत्यर्थः** — the lead horse of a team. The "
            "two counter-examples are a plateau of the Himālaya "
            "and a dry measure, and neither takes the cerebral"),
    Nisedha(
        "8.3.93", does="nipātana", of=("viṣṭara",),
        sense=("vṛkṣa", "āsana"), nipatana=True,
        keeps_out="औलपिवाक्यस्य विस्तरः — the length of a "
                  "discourse",
        why="वृक्षासनयोर्विष्टरः — and **विष्टर** of a TREE or a "
            "SEAT: **विष्टरो वृक्षः; विष्टरम् आसनम्**. "
            "**विपूर्वस्य स्तृणातेः षत्वं निपात्यते** — it is "
            "वि plus स्तॄ, and what is laid down is the "
            "cerebral, the rest of the word coming as usual"),
    Nisedha(
        "8.3.94", does="nipātana", of=("viṣṭāra",),
        sense=("chandonāman",), nipatana=True,
        why="छन्दोनाम्नि च — and **विष्टार** as the NAME OF A "
            "METRE. The vṛtti works out where the long आ comes "
            "from: the घञ् of 3.3.34, which is itself given "
            "**छन्दोनाम्नि च** — so two sūtras with the same "
            "four syllables, five adhyāyas apart, make one word "
            "between them"),
    Nisedha(
        "8.3.95", does="ṣa", of=("sthira",), after="gavi-yudhi",
        why="गवियुधिभ्यां स्थिरः — the स् of स्थिर becomes "
            "cerebral after गवि and युधि: **गविष्ठिरः, "
            "युधिष्ठिरः**. And the laying-down buys something "
            "besides — **गोशब्दाद् अहलन्ताद् अपि एतस्माद् एव "
            "निपातनात् सप्तम्या अलुग् भवति** — the locative "
            "ending of गो survives inside the compound, which "
            "no ordinary rule allows"),
    Nisedha(
        "8.3.96", does="ṣa", of=("sthala",), after="vi-ku-śami-pari",
        why="विकुशमिपरिभ्यः स्थलम् — and स्थल after वि, कु, शमि "
            "and परि: **विष्ठलम्, कुष्ठलम्, शमिष्ठलम्, "
            "परिष्ठलम्**. Four first members and one second, "
            "and the sūtra says nothing else — which is what "
            "most of this stretch looks like"),
    Nisedha(
        "8.3.97", does="ṣa", of=("stha",), after="ambādi",
        why="अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गुमञ्जि"
            "पुञ्जिपरमेबर्हिर्दिव्यग्निभ्यः स्थः — and स्थ "
            "after eighteen named first members: अम्ब, आम्ब, "
            "गो, भूमि, सव्य, अप्, द्वि, त्रि, कु, शेकु, शङ्कु, "
            "अङ्, गु, मञ्जि, पुञ्जि, परमे, बर्हिस्, दिवि and "
            "अग्नि. **अम्बष्ठः** and the rest. It is the "
            "longest compound in the pāda and one of the "
            "longest in the work"),
    Nisedha(
        "8.3.98", does="ṣa", gana="suṣāmādi",
        why="सुषामादिषु च — and in the सुषामादि class: "
            "**शोभनं साम यस्य असौ सुषामा ब्राह्मणः; दुष्षामा; "
            "निष्षामा; निष्षेधः; दुष्षेधः**. The first is worth "
            "the sūtra on its own — सु is a कर्मप्रवचनीय there "
            "and not a preverb, so none of the preverb rules of "
            "8.3.65–89 could have reached it"),
    Nisedha(
        "8.3.99", does="ṣa", before=("e",), sense=("saṃjñā",),
        after="iṇ-ku-a-ga",
        keeps_out="हरिसक्थम् — no ए follows; पृथ्वी सेना — no "
                  "name is being made",
        why="ऐति संज्ञायामगात् — a स् before an ए becomes "
            "cerebral in a NAME, provided what stands before is "
            "not a ग: **हरिषेणः, वारिषेणः, जानुषेणी**. Three "
            "conditions at once — the following ए, the name, "
            "and the ग excepted — and the vṛtti tests two of "
            "them"),
    Nisedha(
        "8.3.100", does="ṣa", after="nakṣatra", before=("e",),
        sense=("saṃjñā",), optional=True, blocks=("8.3.99",),
        keeps_out="शतभिषक्सेनः — the first member ends in a ग, "
                  "which the sūtra before excepted",
        why="नक्षत्राद्वा — and after the name of a "
            "CONSTELLATION it is optional: **रोहिणीषेणः, "
            "रोहिणीसेनः; भरणीषेणः, भरणीसेनः**. The exception "
            "for a ग is carried down — **अगकाराद् इत्येव** — "
            "so शतभिषक्सेनः has neither form"),
    Nisedha(
        "8.3.101", does="ṣa", after="hrasva",
        before=("ta-ādi-taddhita",),
        why="ह्रस्वात् तादौ तद्धिते — and after a SHORT vowel "
            "before a त-initial taddhita: **सर्पिष्टरम्, "
            "यजुष्टरम्; सर्पिष्टमम्**. The vṛtti lists the "
            "seven affixes the rule can reach — तरप्, तमप्, "
            "तय, त्व, तल्, तस्, त्यप् — which is a way of "
            "saying that तादौ तद्धिते is a smaller class than "
            "it looks"),
    Nisedha(
        "8.3.102", does="ṣa", of=("tap",), after="nis",
        sense=("an-āsevana",),
        keeps_out="निस्तपति सुवर्णम् — heated again and again, "
                  "which आसेवन is",
        why="निसस्तपतावनासेवने — and the स् of निस् before तप् "
            "where the action is NOT REPEATED: **आसेवनं "
            "पुनःपुनः करणम्। निष्टपति सुवर्णम्। सकृद् अग्निं "
            "स्पर्शयति इत्यर्थः** — he puts the gold to the "
            "fire once. Doing it over and over gives "
            "निस्तपति, with no cerebral"),
    Nisedha(
        "8.3.103", does="ṣa", before=("yuṣmat", "tat", "tatakṣus"),
        gana="antaḥ-pāda", chandasi=True,
        why="युष्मत्तत्ततक्षुःष्वन्तःपादम् — and before the "
            "forms of युष्मद्, before तद् and before ततक्षुस्, "
            "provided the स् stands WITHIN a metrical quarter: "
            "**अग्निष् ट्वं नामासीत्**. The युष्मद्-forms meant "
            "are its substitutes — त्वम्, त्वाम्, ते, तव — so "
            "the rule names a paradigm by naming its stem"),
    Nisedha(
        "8.3.104", does="ṣa", before=("yuṣmat", "tat", "tatakṣus"),
        sense=("yajus",), view="ekeṣām", optional=True,
        why="यजुष्येकेषाम् — and in the YAJUS, in SOME "
            "TEACHERS' view: **अर्चिर्भिष् ट्वम्, "
            "अर्चिर्भिस्त्वम्; अग्निष् टेऽग्रम्**. एकेषाम् is "
            "the first of three such namings in a row, and it "
            "does what naming a teacher always does — makes the "
            "rule an option and leaves both readings standing"),
    Nisedha(
        "8.3.105", does="ṣa", of=("stuta", "stoma"),
        chandasi=True, view="ekeṣām", optional=True,
        why="स्तुतस्तोमयोश्छन्दसि — and of स्तुत and स्तोम in "
            "the Veda, in some teachers' view: **त्रिभिष्टुतस्य, "
            "त्रिभिस्तुतस्य; गोष्टोमम्**. एकेषाम् is carried "
            "down from the sūtra before rather than said again, "
            "which is how the three make one block"),
    Nisedha(
        "8.3.106", does="ṣa", after="pūrvapada", chandasi=True,
        view="ekeṣām", optional=True,
        why="पूर्वपदात् — and after a FIRST MEMBER, in the Veda, "
            "in some teachers' view: **द्विषन्धिः, "
            "द्विसन्धिः**. This is the widest of the three and "
            "the one that makes the other two nearly "
            "unnecessary — which is presumably why all three "
            "are given as somebody's opinion rather than as the "
            "grammar's own"),
    Nisedha(
        "8.3.107", does="ṣa", of=("suñ",), after="pūrvapada",
        chandasi=True,
        why="सुञः — and of the particle सुञ्: **अभी षु णः "
            "सखीनाम्; ऊर्ध्व ऊ षु ण ऊतये**. The particle is "
            "picked out by name because it is a particle and "
            "not a first member in any ordinary sense, and "
            "पूर्वपदात् is carried down all the same"),
    Nisedha(
        "8.3.108", does="ṣa", of=("san",), gana="a-an-anta",
        chandasi=True,
        keeps_out="गोसनिं वाचम् उदेयम् — the word ends in अन्, "
                  "which the sūtra excepts",
        why="सनोतेरनः — and of सन्, provided the word does not "
            "end in अन्: **गोषाः, नृषाः**. **पूर्वपदाद् इत्येव "
            "सिद्धे** — the sūtra before would have given it "
            "anyway, and what this adds is the exception"),
    Nisedha(
        "8.3.109", does="ṣa", of=("sah",), after="pṛtanā-ṛta",
        chandasi=True,
        why="सहेः पृतनर्ताभ्यां च — and of सह् after पृतना and "
            "ऋत: **पृतनाषाहम्, ऋताषाहम्**. **केचित् सहेः इति "
            "योगविभागं कुर्वन्ति** — some split the sūtra in "
            "two so that सहेः stands alone and reaches "
            "ऋतीषहम् besides, which the Kāśikā records without "
            "adopting"),
    Nisedha(
        "8.3.110", refuses=True, of=SRPI_SIX,
        blocks=("8.3.59", "8.3.65"),
        why="न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम् — and here the "
            "pāda turns: a स् with a र् before it does NOT "
            "become cerebral, nor the स् of सृप्, सृज्, स्पृश्, "
            "स्पृह् or the सवनादि: **विस्रंसिकायाः; विस्रब्धः "
            "कथयति; पुनःसृजति**. Ten sūtras of refusal follow, "
            "and this is the widest of them"),
    Nisedha(
        "8.3.111", refuses=True, of=("sāt", "pada-ādi"),
        blocks=("8.3.59",),
        why="सात्पदाद्योः — nor of सात्, nor of a स् that "
            "BEGINS a word: **अग्निसात्, दधिसात्**. The sūtra "
            "is needed because the two would have been reached "
            "for two different reasons — **प्रत्ययसकारत्वात् "
            "प्राप्तिः, पदादेश् च आदेशसकारत्वात्** — the first "
            "as an affix's स् and the second as a substitute's, "
            "which are exactly 8.3.59's two halves"),
    Nisedha(
        "8.3.112", refuses=True, of=("sic",), before=("yaṅ",),
        blocks=("8.3.65",),
        why="सिचो यङि — nor of the aorist's स् before यङ्: "
            "**सेसिच्यते, अभिसेसिच्यते**. And the vṛtti sorts "
            "out which of two refusals is doing the work — "
            "**उपसर्गात् इति या प्राप्तिः सा पदादिलक्षणम् एव "
            "प्रतिषेधं बाधते, न सिचो यङि इति** — the preverb "
            "rule is held off by 8.3.111's word-head refusal "
            "and not by this one"),
    Nisedha(
        "8.3.113", refuses=True, of=("sedh",), sense=("gati",),
        blocks=("8.3.65",),
        keeps_out="शिष्यम् अकार्यात् प्रतिषेधयति — forbidding, "
                  "where the cerebral does come",
        why="सेधतेर्गतौ — nor of सेध् where MOTION is meant: "
            "**अभिसेधयति गाः; परिसेधयति गाः** — he drives the "
            "cattle. Of forbidding the cerebral stands: "
            "**प्रतिषेधयति**. One root, two senses, and the "
            "commonest word for a prohibition in the grammar "
            "itself is on the other side of the line"),
    Nisedha(
        "8.3.114", refuses=True, nipatana=True,
        of=("pratistabdha", "nistabdha"), blocks=("8.3.67",),
        why="प्रतिस्तब्धनिस्तब्धौ च — and **प्रतिस्तब्धः** and "
            "**निस्तब्धः** are laid down without it: "
            "**स्तन्भेः इति प्राप्तं षत्वं प्रतिषिध्यते** — "
            "8.3.67 had given स्तम्भ् the cerebral after any "
            "preverb, and these two words are taken out of it "
            "by name"),
    Nisedha(
        "8.3.115", refuses=True, of=("sah",), gana="soḍha",
        blocks=("8.3.70",),
        keeps_out="परिषहते — the root is not in the सोढ् shape, "
                  "and the cerebral comes",
        why="सोढः — nor of सह् IN THE SHAPE सोढ्: **परिसोढा, "
            "परिसोढुम्, परिसोढव्यम्**. **सोड्भूतग्रहणं किम्? "
            "परिषहते** — the same root after the same preverb "
            "takes the cerebral wherever it has not become "
            "सोढ्, so the refusal is of one shape and not of a "
            "root"),
    Nisedha(
        "8.3.116", refuses=True, of=STAMBHU_THREE,
        before=("caṅ",), blocks=("8.3.67", "8.3.70"),
        why="स्तम्भुसिवुसहां चङि — nor of स्तम्भ्, सिव् and सह् "
            "before चङ्: **स्तन्भेः इति परिनिविभ्यः इति च "
            "प्राप्तो मूर्धन्यः प्रतिषिध्यते**. Two earlier "
            "rules had reached these three roots and this holds "
            "both off at once, in the causal aorist alone"),
    Nisedha(
        "8.3.117", refuses=True, of=("sunoti",),
        before=("sya", "san"), blocks=("8.3.65",),
        why="सुनोतेः स्यसनोः — nor of सु before स्य and सन्: "
            "**अभिसोष्यति, परिसोष्यति; अभ्यसोष्यत्**. And the "
            "vṛtti asks what the सन् is for and answers that it "
            "is for nothing — **सनि किम् उदाहरणम्? सुसूषति। "
            "न एतद् अस्ति प्रयोजनम्** — 8.3.61's नियम having "
            "already kept the cerebral out there"),
    Nisedha(
        "8.3.118", refuses=True, of=("sad", "ṣvañj"),
        before=("liṭ",), gana="para", blocks=("8.3.66", "8.3.70"),
        why="सदिष्वञ्जोः परस्य लिटि — and in the PERFECT of सद् "
            "and ष्वञ्ज् the LATER स् does not take it: "
            "**अभिषसाद, परिषसाद, निषसाद, विषसाद; परिषस्वजे, "
            "परिषस्वजाते, परिषस्वजिरे**. In each the first स् "
            "is cerebral and the reduplication's is not — one "
            "word with the same sound twice and the rule "
            "reaching only one of them"),
    Nisedha(
        "8.3.119", refuses=True, after="ni-vi-abhi",
        gana="aṭ-vyavāya", chandasi=True, optional=True,
        blocks=("8.3.63",),
        why="निव्यभिभ्योऽड्व्यवाये वा छन्दसि — and in the Veda, "
            "after नि, वि and अभि, the cerebral OPTIONALLY does "
            "not reach across the augment: **न्यषीदत् पिता नः, "
            "न्यसीदत्; व्यषीदत्, व्यसीदत्**. 8.3.63's heading "
            "had made that reach compulsory, and the pāda "
            "closes by making it a choice in one register — "
            "which is where it began, 8.3.8 having done the "
            "same thing for the रुँ"),
)


def _reaches(row: Nisedha, root: str, gana: str, after: str,
             before: str, sense: str, view: str,
             chandasi: bool) -> bool:
    # `of` and `gana` CONJOIN: 8.3.115 names सह् AND wants the
    # सोढ् shape, 8.3.108 names सन् AND excepts an अन्-final.
    # Where a sūtra really does name two alternatives — 8.3.111
    # सात्पदाद्योः is a dvandva, सात् OR a word's head — both go
    # into `of`, since two entries there are alternatives and a
    # `gana` beside them would not be. The first draft split
    # them across the two columns and सात् then reached nothing.
    if row.of and root not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.after and after != row.after:
        return False
    if row.before and before not in row.before:
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.view and view != row.view:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Nisedha) -> int:
    """
    A refusal outweighs the rules it refuses, a named word
    outweighs a shape, and a named sense outweighs both.

    8.3.113 is why the sense has to weigh: सेध् takes the
    cerebral of forbidding and refuses it of driving cattle,
    and nothing else tells the two apart.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of)
        + 6 * len(row.sense)
        + 4 * bool(row.gana)
        + 4 * bool(row.after)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
        + 1 * bool(row.view)
    )


def also_cerebral(root: str = "", *, gana: str = "",
                  after: str = "", before: str = "",
                  sense: str = "", view: str = "",
                  chandasi: bool = False) -> Joined:
    """
    8.3.90–119 — the last of the cerebrals, and the ten refusals.

    Nothing answers by default, and the answer is the same
    `Joined` the rest of the pāda gives.
    """
    matched = [
        row for row in NISEDHA_TABLE
        if _reaches(row, root, gana, after, before, sense, view,
                    chandasi)
    ]
    if not matched:
        return Joined(
            "", "", "No rule of 8.3.90-119 is reached, so the s "
                    "stands as 8.3.55-89 left it")
    row = max(matched, key=_how_specific)
    return Joined(row.does, row.sutra, row.why,
                  refuses=row.refuses, nipatana=row.nipatana,
                  optional=row.optional, view=row.view,
                  blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Nisedha, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NISEDHA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Nisedha", "NISEDHA_TABLE", "NISEDHA_RUN", "REFUSALS_FROM",
    "NIPATANA_FIVE", "VIKUSAMI_FOUR", "SRPI_SIX",
    "STAMBHU_THREE",
    "also_cerebral", "provisions_for",
]
