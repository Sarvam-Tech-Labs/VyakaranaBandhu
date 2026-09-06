# -*- coding: utf-8 -*-
"""
६.१.१३५–१५७ — सुट् कात् पूर्वः, an augment that never joins the root.

**सुट् कात् पूर्वः.** From 6.1.135 to 6.1.157, every rule is read with
*the augment स् stands before the क्*. **अधिकारोऽयम्, पारस्करप्रभृतीनि
च संज्ञायाम् इति यावत्** — and the heading is bounded by its own LAST
RULE, as 6.1.45's आकार was by 6.1.57. The second heading of this pāda
built that way, against two bounded from outside.

**AND कात् पूर्वः IS SAID TO SHOW THE AUGMENT IS NOT PART OF THE
ROOT.** **कात् पूर्वग्रहणं सुटोऽभक्तत्वज्ञापनार्थम्** — and the vṛtti
works out four consequences of that one phrase:

*The root does not become a cluster-initial one.* संस्कृषीष्ट and
संस्क्रियते take neither the इट् nor the guṇa that 7.4.10's
संयोगादि condition would give.

*The accent still reaches across it.* 8.1.28's निघात would be blocked
by the intervening स् — except that **स्वरविधौ व्यञ्जनमविद्यमानवत्**,
a consonant is as good as absent where an accent is concerned.

*But a guṇa does reach across it.* संचस्करतुः gets one, by
**तन्मध्यपतितस्तद्ग्रहणेन गृह्यते** — a form with something inserted
into it is still reached by the name of what it was inserted into.

*And the ट् of सुट् is for a rule three adhyāyas later.* **टित्करणं
सुट्स्तुस्वञ्जाम् इत्यत्र विशेषणार्थम्** — 8.3.70 names सुट् by that
marker.

**AND THE SECTION IS MOSTLY निपातन.** Fifteen of its twenty-three
rules lay a finished word down rather than deriving it, and each is
confined by a sense: गोष्पद only of pasture or of measure, आस्पद only
of standing, आश्चर्य only of what is not usual. The last rule's list
is an **आकृतिगण** and is defined by exclusion — **अविहितलक्षणः सुट्
पारस्करप्रभृतिषु द्रष्टव्यः**, any सुट् no rule accounts for belongs
here.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule inserts the
augment. It does not build the word: 8.3.70's षत्व turns the स् into
ष् in परिष्कर्ता, and 8.3.5's supplement makes the म् of सम् a स्.
Neither is codified.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where सुट् कात् पूर्वः governs, on the vṛtti's own bound at
#: 6.1.135: **पारस्करप्रभृतीनि च संज्ञायाम् इति यावत्**. The rule
#: named is the run's own LAST member.
SUT_RUN: Tuple[str, str] = ("6.1.135", "6.1.157")
SUT_MARKER: str = "6.1.157"

#: What कात् पूर्वः buys, each consequence with the rule it bears on.
#: One phrase in one sūtra, and the vṛtti draws four things out of it.
WHY_KAT_PURVAH: Tuple[Tuple[str, str], ...] = (
    ("7.4.10", "संस्कृषीष्ट takes no इट् and no guṇa — the root is "
               "not संयोगादि, the स् not being part of it"),
    ("8.1.28", "and the निघात still reaches, since "
               "स्वरविधौ व्यञ्जनमविद्यमानवत्"),
    ("7.4.10", "but संचस्करतुः DOES take its guṇa, by "
               "तन्मध्यपतितस्तद्ग्रहणेन गृह्यते"),
    ("8.3.70", "and the ट् of सुट् is what that rule names it by"),
)

#: 6.1.157's list, which the vṛtti calls an आकृतिगण — a class known
#: by its shape rather than by its members. **अविहितलक्षणः सुट्
#: पारस्करप्रभृतिषु द्रष्टव्यः**: whatever सुट् no rule accounts for
#: is filed here, so the list can never be closed.
PARASKARADI: Tuple[str, ...] = (
    "pāraskara", "kāraskara", "rathaspā", "kiṣku", "kiṣkindhā",
    "taskara", "bṛhaspati", "prāyaścitta",
)


@dataclass(frozen=True)
class Sut:
    """One rule of 6.1.135–157: where the augment स् goes in."""

    sutra: str
    #: What the rule does: suṭ, nipātana, or nothing where it is only
    #: the heading.
    does: str = ""
    #: The roots or finished words the rule names.
    of: Tuple[str, ...] = ()
    #: What must stand in front — सम्, परि, उप, अप, प्रति, प्र.
    pre: Tuple[str, ...] = ()
    #: The sense the form must carry.
    result: str = ""
    #: What must FOLLOW in the compound — चन्द्र at 6.1.151.
    uttarapada: str = ""
    #: What the agent must be — 6.1.157's supplement wants a cow.
    agent: str = ""
    #: What may stand BETWEEN the preverb and the क् without stopping
    #: the augment — the अट् of the imperfect, or the reduplicated
    #: syllable. 6.1.136 alone, and it is the whole of what that rule
    #: contributes: without the column it would state no condition and
    #: answer every question asked.
    across: Tuple[str, ...] = ()
    optional: bool = False
    #: True where the rule holds in a मन्त्र alone.
    mantra: bool = False
    #: True where the word must be a NAME.
    samjna: bool = False
    #: True where the row IS the heading.
    heading: bool = False
    #: The rule this one extends or narrows, by ITS own number.
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


SUT_TABLE: Tuple[Sut, ...] = (
    Sut(
        "6.1.135", heading=True,
        why="सुट् कात् पूर्वः — **अधिकारोऽयम्, पारस्करप्रभृतीनि च "
            "संज्ञायाम् इति यावत्। इत उत्तरं यद् वक्ष्यामस्तत्र "
            "सुडिति कात् पूर्व इति चैतदधिकृतं वेदितव्यम्** — every "
            "rule to 6.1.157 is read with *the augment स् before the "
            "क्*. **संस्कर्ता, संस्कर्तुम्, संस्कर्तव्यम्**. And the "
            "heading is bounded by its own last rule, as 6.1.45's "
            "आकार was.\\n\\n"
            "**AND कात् पूर्वः IS SAID TO SHOW THE AUGMENT IS NOT "
            "PART OF THE ROOT.** **कात् पूर्वग्रहणं "
            "सुटोऽभक्तत्वज्ञापनार्थम्** — and four things follow. "
            "**तथाहि संस्कृषीष्ट संस्क्रियत इति संयोगादिलक्षणाविड्"
            "गुणौ न भवतः**: the root is not cluster-initial, so "
            "7.4.10's condition fails and neither the इट् nor the "
            "guṇa comes.\\n\\n"
            "**AND THEN AN OBJECTION, AND ITS ANSWER.** "
            "**तिङ्ङतिङः इति निघातोऽपि तर्हि न प्राप्नोति, सुटा "
            "व्यवहितत्वात्?** — if the स् really stands apart, does "
            "it not also stand BETWEEN and block 8.1.28's accent "
            "rule? **स्वरविधौ व्यञ्जनमविद्यमानवद् इति वचनाद् नास्ति "
            "व्यवधानम्**: where an accent is concerned a consonant "
            "counts as absent.\\n\\n"
            "**AND A THIRD CASE GOES THE OTHER WAY.** "
            "**संचस्करतुः, संचस्करुरिति गुणः कथम्? "
            "तन्मध्यपतितस्तद्ग्रहणेन गृह्यते इति** — there the guṇa "
            "DOES reach, because a form with something inserted into "
            "it is still named by what it was inserted into.\\n\\n"
            "**AND THE ट् IS FOR A RULE THREE ADHYĀYAS LATER.** "
            "**टित्करणं सुट्स्तुस्वञ्जाम् इत्यत्र विशेषणार्थम्** — "
            "8.3.70 names this augment by that marker"),
    Sut(
        "6.1.136", does="suṭ", across=("aṭ", "abhyāsa"),
        blocks=("6.1.135",),
        why="अडभ्यासव्यवायेऽपि — the augment goes in before the क् "
            "even where the अट् of the imperfect or the reduplicated "
            "syllable stands between: **समस्करोत्, समस्कार्षीत्; "
            "संचस्कार, परिचस्कार**.\\n\\n"
            "**AND THE RULE IS NOT PĀṆINI'S.** It is made out of two "
            "vārttikas, **अड्व्यवाय उपसंख्यानम्** and "
            "**अभ्यासव्यवाये च**, read together as one sūtra.\\n\\n"
            "**AND IT IS NEEDED BECAUSE OF WHAT 6.1.135 ESTABLISHED.** "
            "The objection: **पूर्वं धातुरुपसर्गेण युज्यते** — root "
            "and preverb join first, so the सुट् is already in when "
            "the अट् and the doubling arrive; why say this? Because "
            "**अभक्तश्च सुडित्युक्तम्, ततः सकारादुत्तरावडभ्यासावनिष्टे "
            "देशे स्याताम्** — the augment standing apart, the अट् "
            "and the copy would land AFTER it, in the wrong place. "
            "The rule puts them before it and the augment back in "
            "front of the क्"),
    Sut(
        "6.1.137", does="suṭ", of=("kṛ",), pre=("sam", "pari", "upa"),
        result="bhūṣaṇa",
        keeps_out="उपकरोति — the sense is not adorning",
        why="संपर्युपेभ्यः करोतौ भूषणे — after सम्, परि or उप, before "
            "करोति, in the sense of ADORNING: **संस्कर्ता, "
            "परिष्कर्ता, उपस्कर्ता**.\\n\\n"
            "**AND TWO LATER RULES FINISH THE FORMS.** 8.3.70's "
            "षत्व makes the स् a ष् after परि and उप; and a "
            "supplement, **संपुंकानां सत्वम्**, turns the म् of सम् "
            "into a स् with the vowel before it nasalised.\\n\\n"
            "**AND THE SENSE-CONDITION IS ADMITTED TO LEAK.** "
            "**संपूर्वस्य क्वचिदभूषणेऽपि सुडिष्यते, संस्कृतमन्नमिति** "
            "— after सम् the augment is wanted sometimes where the "
            "sense is NOT adorning, and the vṛtti says so rather "
            "than stretching भूषण to cover cooked food"),
    Sut(
        "6.1.138", does="suṭ", of=("kṛ",), pre=("sam", "pari", "upa"),
        result="samavāya",
        why="समवाये च — and in the sense of coming together: "
            "**तत्र नः संस्कृतम्; तत्र नः परिष्कृतम्; तत्र न "
            "उपस्कृतम्**, which the vṛtti glosses **समुदितम्**. "
            "**समवायः समुदायः** — the word means an aggregate, and "
            "the three preverbs of the rule before carry down"),
    Sut(
        "6.1.139", does="suṭ", of=("kṛ",), pre=("upa",),
        result="pratiyatna",
        keeps_out="उपकरोति — none of the three senses",
        why="उपात् प्रतियत्नवैकृतवाक्याध्याहारेषु — after उप alone, "
            "in three further senses, and the vṛtti defines each "
            "before using it.\\n\\n"
            "**प्रतियत्न**: **सतो गुणान्तराधानम् आधिक्याय वृद्धस्य "
            "वा तादवस्थ्याय समीहा** — putting a further quality into "
            "something that already exists, to increase it or to "
            "hold it as it is. **एधोदकस्योपस्कुरुते; काण्डं गुडस्य "
            "उपस्कुरुते**.\\n\\n"
            "**वैकृत**: **विकृतमेव वैकृतम्**, with 5.4.38's प्रज्ञादि "
            "अण् adding nothing. **उपस्कृतं भुङ्क्ते, उपस्कृतं "
            "गच्छति**.\\n\\n"
            "**वाक्याध्याहार**: **गम्यमानार्थस्य वाक्यस्य "
            "स्वरूपेणोपादानम्** — putting into words a sentence that "
            "was only implied. **उपस्कृतं जल्पति, "
            "उपस्कृतमधीते**"),
    Sut(
        "6.1.140", does="suṭ", of=("kṝ",), pre=("upa",),
        result="lavana",
        keeps_out="उपकिरति देवदत्तः — not of reaping",
        why="किरतौ लवने — before किरति and in the sense of reaping: "
            "**उपस्कारं मद्रका लुनन्ति; उपस्कारं काश्मीरका "
            "लुनन्ति** — **विक्षिप्य लुनन्ति**, they scatter as they "
            "cut. And **णमुलत्र वक्तव्यः**, the affix in these forms "
            "being णमुल्"),
    Sut(
        "6.1.141", does="suṭ", of=("kṝ",), pre=("upa", "prati"),
        result="hiṃsā",
        keeps_out="प्रतिकीर्णम् — no harm meant",
        why="हिंसायां प्रतेश्च — and after प्रति as well as उप, where "
            "harm is meant: **उपस्कीर्णं हन्त ते वृषल भूयात्; "
            "प्रतिस्कीर्णं हन्त ते वृषल भूयात्** — the vṛtti "
            "glossing it **तथा ते वृषल विक्षेपो भूयाद् यथा हिंसाम् "
            "अनुबध्नाति**, a scattering that carries harm with "
            "it"),
    Sut(
        "6.1.142", does="suṭ", of=("kṝ",), pre=("apa",),
        result="ālekhana", agent="catuṣpād-śakuni",
        keeps_out="अपकिरति देवदत्तः — a man, not a beast or a bird; "
                  "अपकिरति श्वा ओदनपिण्डमाशितः — a dog that has "
                  "eaten, scratching for none of the three reasons",
        why="अपाच्चतुष्पाच्छकुनिष्वालेखने — after अप, of a "
            "four-footed animal or a bird scratching the ground: "
            "**अपस्किरते वृषभो हृष्टः; अपस्किरते कुक्कुटो भक्ष्यार्थी; "
            "अपस्किरते श्वा आश्रयार्थी** — **आलिख्य विक्षिपति**, it "
            "scrapes and throws.\\n\\n"
            "**AND THE THREE REASONS FOR SCRATCHING ARE THEMSELVES A "
            "CONDITION.** "
            "**हर्षजीविकाकुलायकरणेष्विति वक्तव्यम्** — out of "
            "gladness, for food, or to make a nest, and no other. "
            "The same three are what give the root its ātmanepada by "
            "a vārttika on 1.3.21, so one condition serves two "
            "rules"),
    Sut(
        "6.1.143", does="nipātana", of=("kustumburu",), result="jāti",
        keeps_out="कुतुम्बुरूणि — a contemptuous compound of तुम्बुरु, "
                  "the ebony fruit",
        why="कुस्तुम्बुरूणि जातिः — the word is laid down with its "
            "सुट्, and only where a SPECIES is meant: **कुस्तुम्बुरुर् "
            "नाम ओषधिजातिर्धान्यकम्**, coriander, and its seeds "
            "besides.\\n\\n"
            "**AND THE GENDER IN THE RULE IS NOT MEANT.** "
            "**सूत्रनिर्देशे नपुंसकलिङ्गमविवक्षितम्** — the word is "
            "cited in the neuter and is not confined to it"),
    Sut(
        "6.1.144", does="nipātana", of=("aparaspara",),
        result="kriyāsātatya",
        keeps_out="अपरपराः सार्था गच्छन्ति — some first and some "
                  "after, each going once",
        why="अपरस्पराः क्रियासातत्ये — laid down with its सुट् where "
            "an action goes on without a break: **अपरस्पराः सार्था "
            "गच्छन्ति** — **सन्ततमविच्छेदेन गच्छन्ति**.\\n\\n"
            "**AND THE VṚTTI STOPS TO EXPLAIN A WORD IN ITS OWN "
            "GLOSS.** **किमिदं सातत्यमिति? सततस्य भावः सातत्यम्। "
            "कथं सततम्?** — how is it सतत and not संतत? By a verse "
            "listing four places a nasal or a vowel drops: "
            "**लुम्पेदवश्यमः कृत्ये तुं काममनसोरपि। समो वा हितततयोर् "
            "मांसस्य पचि युड्घञोः॥** — the म् of सम् goes "
            "optionally before हित and तत, which gives सहित and "
            "सतत"),
    Sut(
        "6.1.145", does="nipātana", of=("goṣpada",), result="sevita",
        keeps_out="गोपदम् — a cow's footprint and nothing more",
        why="गोष्पदं सेवितासेवितप्रमाणेषु — laid down with its सुट् "
            "and its ष्, in three senses: land cows go over — "
            "**गोष्पदो देशः**; land they do not — **अगोष्पदान्यरण्यानि**; "
            "and a measure — **गोष्पदमात्रं क्षेत्रम्, गोष्पदपूरं "
            "वृष्टो देवः**, where **नात्र गोष्पदं स्वार्थप्रतिपादनार्थम् "
            "उपादीयते; किं तर्हि? क्षेत्रस्य वृष्टेश्च परिच्छेत्तुम् "
            "इयत्ताम्**.\\n\\n"
            "**AND असेवित IS ARGUED FOR, AGAINST AN OBVIOUS "
            "OBJECTION.** Why state it, when न गोष्पद gives "
            "अगोष्पद? Because a नञ् compound means what is LIKE the "
            "thing and not it: **यत्र तु सेवितप्रसङ्गोऽस्ति तत्रैव "
            "स्याद् अगोष्पदमिति, यत्र त्वत्यन्तासंभव एव तत्र न "
            "स्यात्** — so अगोष्पद would reach only land cows COULD "
            "graze and do not. **यानि हि महान्त्यरण्यानि येषु "
            "गवामत्यन्तासंभवस्तान्येवमुच्यन्ते**: the word is stated "
            "to reach the deep forests where they never could"),
    Sut(
        "6.1.146", does="nipātana", of=("āspada",), result="pratiṣṭhā",
        keeps_out="आपदम् — merely आ from a foot",
        why="आस्पदं प्रतिष्ठायाम् — laid down where a standing or a "
            "position is meant: **आस्पदमनेन लब्धम्**. And the sense "
            "is defined before it is used — "
            "**आत्मयापनाय स्थानं प्रतिष्ठा**, the place by which one "
            "keeps oneself going"),
    Sut(
        "6.1.147", does="nipātana", of=("āścarya",), result="anitya",
        keeps_out="आचर्यं कर्म शोभनम् — good conduct, which is not "
                  "unusual",
        why="आश्चर्यमनित्ये — laid down where what is wonderful is "
            "meant, and the vṛtti derives the sense from the word: "
            "**अनित्यतया विषयभूतया अद्भुतत्वमिह लक्ष्यते** — what "
            "astonishes does so by being uncommon. "
            "**आश्चर्यं यदि स भुञ्जीत; आश्चर्यं यदि सोऽधीयीत** — "
            "**चित्रमद्भुतम्**. The यत् is a vārttika's on 3.1.100 "
            "and the सुट् is this rule's"),
    Sut(
        "6.1.148", does="nipātana", of=("avaskara",), result="varcaska",
        keeps_out="अवकरः — sweepings, and no सुट्",
        why="वर्चस्केऽवस्करः — laid down for excrement, and the "
            "vṛtti reads the sense-word out: **कुत्सितं वर्चो "
            "वर्चस्कम् अन्नमलम्**. The word is किरति with अव and "
            "3.3.57's अप् in the passive sense — **अवकीर्यत "
            "इत्यवस्करोऽन्नमलम्** — and **तत्संबन्धाद् देशोऽपि "
            "तथोच्यते**, the place too by association"),
    Sut(
        "6.1.149", does="nipātana", of=("apaskara",),
        result="rathāṅga",
        keeps_out="अपकरः",
        why="अपस्करो रथाङ्गम् — laid down for a part of a chariot: "
            "**अपस्करो रथावयवः**. The same root and the same 3.3.57 "
            "as the rule before, and only the preverb and the sense "
            "differ"),
    Sut(
        "6.1.150", does="nipātana", of=("viṣkira",), agent="śakuni",
        optional=True,
        keeps_out="विकिर used of anything but a bird — and naming "
                  "that word in the rule is what prevents it",
        why="विष्किरः शकुनिर्विकिरो वा — laid down for a bird, and "
            "optionally, विकिर standing beside it: "
            "**सर्वे शकुनयो भक्ष्या विष्किराः कुक्कुटादृते**. The "
            "affix is 3.1.135's क.\\n\\n"
            "**AND THE SECOND WORD IS IN THE RULE TO CONFINE IT.** "
            "**विष्किरो वा शकुनाविति वा ग्रहणादेव सुड्विकल्पे सिद्धे "
            "विकिरग्रहणम् इह तस्यापि शकुनेरन्यत्र प्रयोगो मा भूत्** — "
            "the वा alone would have given both forms; naming विकिर "
            "as well is what stops THAT word being used of anything "
            "but a bird"),
    Sut(
        "6.1.151", does="suṭ", uttarapada="candra", mantra=True,
        keeps_out="सूर्याचन्द्रमसाविव — the vowel before it is long; "
                  "सुचन्द्रा पौर्णमासी — not a मन्त्र; "
                  "शुक्रमसि चन्द्रमसि — चन्द्र is not the second "
                  "member of a compound at all",
        why="ह्रस्वाच्चन्द्रोत्तरपदे मन्त्रे — in a मन्त्र, after a "
            "short vowel, before चन्द्र standing as the second "
            "member of a compound: **सुश्चन्द्र युष्मान्**.\\n\\n"
            "**AND उत्तरपद MEANS WHAT IT MEANS IN A COMPOUND.** "
            "**उत्तरपदं समास एव भवतीति प्रसिद्धम्** — not merely *the "
            "word after*, which is why **शुक्रमसि चन्द्रमसि** is "
            "untouched"),
    Sut(
        "6.1.152", does="nipātana", of=("kaś",), pre=("prati",),
        keeps_out="प्रतिकशोऽश्वः — कशा is a whip, a word FROM the "
                  "root and not the root",
        why="प्रतिष्कशश्च कशेः — before कश् with प्रति and 3.1.134's "
            "अच्, laid down with its सुट् and its ष्: "
            "**ग्राममद्य प्रवेक्ष्यामि भव मे त्वं प्रतिष्कशः** — "
            "**वार्तापुरुषः, सहायः, पुरोयायी वा**, a messenger or "
            "one who goes ahead.\\n\\n"
            "**AND NAMING THE ROOT IS WHAT FIXES THE PREVERB.** "
            "**कशेरिति धातोरुपादानं तदुपसर्गस्य प्रतेः "
            "प्रतिपत्त्यर्थम्। तेन धात्वन्तरोपसर्गाद् न भवति** — the "
            "प्रति of the rule is the one joined to THIS root, so a "
            "प्रति on some other root gets nothing"),
    Sut(
        "6.1.153", does="nipātana", of=("praskaṇva", "hariścandra"),
        result="ṛṣi", samjna=True,
        keeps_out="प्रकण्वो देशः; हरिचन्द्रो माणवकः",
        why="प्रस्कण्वहरिश्चन्द्रावृषी — two names laid down, and "
            "only of the ṛṣis who bear them: **प्रस्कण्व ऋषिः; "
            "हरिश्चन्द्र ऋषिः**. And the second is here for a "
            "reason 6.1.151 makes plain — **हरिश्चन्द्रग्रहणम् "
            "अमन्त्रार्थम्**: that rule would have given it already "
            "in a मन्त्र, and this one reaches it elsewhere"),
    Sut(
        "6.1.154", does="nipātana", of=("maskara", "maskarin"),
        keeps_out="मकरो ग्राहः; मकरी समुद्रः",
        why="मस्करमस्करिणौ वेणुपरिव्राजकयोः — two words यथासंख्यम्, a "
            "bamboo and a wandering mendicant: **मस्करो वेणुः; "
            "मस्करी परिव्राजकः**. On the plain reading मकर is "
            "**अव्युत्पन्नं प्रातिपदिकम्**, a stem with no "
            "derivation, and the सुट् is simply laid down.\\n\\n"
            "**AND A SECOND READING DERIVES BOTH AND GETS A GLOSS "
            "OUT OF IT.** **केचित् पुनरत्र माङ्युपपदे करोतेः करणे "
            "अच्प्रत्ययमपि निपातयन्ति** — मा + कृ with 3.1.134's "
            "अच् in the instrumental sense: **मा क्रियते येन "
            "प्रतिषिध्यते, स मस्करो वेणुः**, the staff by which one "
            "forbids. And with इनि in the sense of habit, "
            "**माकरणशीलो मस्करी कर्मापवादित्वात् परिव्राजक "
            "उच्यते** — one whose way is *do not*, and the vṛtti "
            "puts his words in: **स ह्येवमाह — मा कुरुत कर्माणि, "
            "शान्तिर्वः श्रेयसीति**.\\n\\n"
            "**AND वेणु IS AN INSTANCE AND NOT A LIMIT.** "
            "**वेणुग्रहणं च प्रदर्शनार्थम् अन्यत्रापि भवति — मस्करो "
            "दण्ड इति**"),
    Sut(
        "6.1.155", does="nipātana", of=("kāstīra", "ajastunda"),
        result="nagara", samjna=True,
        keeps_out="कातीरम्; अजतुन्दम्",
        why="कास्तीराजस्तुन्दे नगरे — two city names laid down: "
            "**कास्तीरं नाम नगरम्; अजस्तुन्दं नाम नगरम्**. The vṛtti "
            "gives each an etymology and then sets it aside: "
            "**ईषत्तीरमस्य, अजस्येव तुन्दमस्येति व्युत्पत्तिरेव "
            "क्रियते, नगरं तु वाच्यमेतयोः** — the derivation is made "
            "out, but what the words MEAN is a city, and that has to "
            "be stated"),
    Sut(
        "6.1.156", does="nipātana", of=("kāraskara",), result="vṛkṣa",
        keeps_out="कारकरः",
        why="कारस्करो वृक्षः — laid down for the tree of that name, "
            "with 3.2.21's ट: **कारस्करो वृक्षः**.\\n\\n"
            "**AND SOME DO NOT READ IT AS A SŪTRA AT ALL.** "
            "**केचिदिदं सूत्रं नाधीयते, पारस्करप्रभृतिष्वेव कारस्करो "
            "वृक्ष इति पठन्ति** — they take the word to be a member "
            "of the next rule's list instead, and the list does hold "
            "it"),
    Sut(
        "6.1.157", does="nipātana", of=PARASKARADI, samjna=True,
        keeps_out="तत्करः; बृहत्पतिः — neither a thief nor a deity; "
                  "प्रतुम्पति वनस्पतिः — the agent is not a cow",
        why="पारस्करप्रभृतीनि च संज्ञायाम् — a list of names laid "
            "down with their सुट्, and the rule whose words bound "
            "the heading opened at 6.1.135: **पारस्करो देशः; "
            "रथस्पा नदी; किष्कुः प्रमाणम्; किष्किन्धा गुहा**.\\n\\n"
            "**AND TWO OF THE LIST NEED A SOUND DROPPED AS WELL.** "
            "**करपत्योश्चोरदेवतयोः सुट् तलोपश्च** — तद् + कर gives "
            "**तस्करश्चोरः** and बृहत् + पति gives "
            "**बृहस्पतिर्देवता**, each losing its त्; and only in "
            "those two senses.\\n\\n"
            "**AND ONE SUPPLEMENT PUTS THE AUGMENT ON A FINITE "
            "VERB.** **प्रात्तुम्पतौ गवि कर्तरि** — "
            "**प्रस्तुम्पति गौः**, and the condition is WHO THE "
            "AGENT IS. Nothing else in the pāda conditions an "
            "augment on that.\\n\\n"
            "**AND THE LIST IS AN आकृतिगण, DEFINED BY EXCLUSION.** "
            "**पारस्करप्रभृतिराकृतिगणः। अविहितलक्षणः सुट् "
            "पारस्करप्रभृतिषु द्रष्टव्यः** — whatever सुट् no rule "
            "accounts for belongs here, so the list cannot be "
            "closed. **प्रायश्चित्तम्, प्रायश्चित्तिः** come in that "
            "way, and with them the Mahābhāṣya's own "
            "**प्रायस्य चित्तिचित्तयोः सुडस्कारो वा**"),
)


@dataclass(frozen=True)
class Inserted:
    """What the resolver answers with."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    mantra: bool = False
    samjna: bool = False
    #: Where a rule extends or narrows another, that rule's number.
    blocked_by: Tuple[str, ...] = ()


def _reaches(row: Sut, stem: str, pre: str, result: str,
             uttarapada: str, agent: str, across: str,
             mantra: bool) -> bool:
    # 6.1.135 states the words every rule is read with and inserts
    # nothing of its own; reachable, it would answer everything.
    if row.heading:
        return False
    if row.mantra and not mantra:
        return False
    if row.of and stem not in row.of:
        return False
    if row.pre and pre not in row.pre:
        return False
    if row.result and result != row.result:
        return False
    if row.uttarapada and uttarapada != row.uttarapada:
        return False
    if row.agent and agent != row.agent:
        return False
    if row.across and across not in row.across:
        return False
    return True


def _supplies(row: Sut, wants: str) -> bool:
    return not wants or wants == row.does


def _how_specific(row: Sut) -> int:
    """
    A named word beats a preverb, and a sense beats both.

    The sense counts highest of the three because 6.1.137 through
    6.1.142 all name करोति or किरति with a preverb and are told apart
    by nothing else: भूषण, समवाय, प्रतियत्न, लवन, हिंसा, आलेखन.
    """
    return (
        7 * bool(row.result)
        + 6 * bool(row.of)
        + 5 * bool(row.agent)
        + 4 * bool(row.uttarapada)
        + 3 * bool(row.pre)
        + 3 * bool(row.across)
        + 2 * bool(row.mantra)
    )


def sut_for(stem: str = "", *, pre: str = "", result: str = "",
            uttarapada: str = "", agent: str = "", across: str = "",
            mantra: bool = False, wants: str = "") -> Inserted:
    """
    6.1.135–157 — where the augment स् goes in before a क्.

    6.1.135 supplies nothing: it states the two things every rule of
    the run is read with, and a question that reaches no rule reaches
    nothing.
    """
    matched = [
        row for row in SUT_TABLE
        if _reaches(row, stem, pre, result, uttarapada, agent,
                    across, mantra)
        and _supplies(row, wants)
    ]
    if not matched:
        return Inserted(
            "", "", "No rule of 6.1.135–157 is reached. 6.1.135 is a "
                    "heading supplying the words the rest are read "
                    "with — सुट् and कात् पूर्वः — and no augment of "
                    "its own")
    row = max(matched, key=_how_specific)
    return Inserted(row.does, row.sutra, row.why, optional=row.optional,
                    mantra=row.mantra, samjna=row.samjna,
                    blocked_by=row.blocks)


def sut_run() -> Inserted:
    """
    How far सुट् कात् पूर्वः governs, and what कात् पूर्वः buys.

    **अधिकारोऽयम्, पारस्करप्रभृतीनि च संज्ञायाम् इति यावत्** — and
    the marker is the run's own last rule, as 6.1.57 was of the आकार.
    """
    opens, closes = SUT_RUN
    return Inserted(
        "", opens,
        "सुट् कात् पूर्वः governs from %s to %s, bounded by the words "
        "of %s — which is a MEMBER of the run. And कात् पूर्वः is "
        "said to show the augment is not part of the root: four "
        "consequences follow, on %s"
        % (opens, closes, SUT_MARKER,
           ", ".join(sorted({rule for rule, _ in WHY_KAT_PURVAH}))))


def provisions_for(sutra_id: str) -> Tuple[Sut, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SUT_TABLE if row.sutra == sutra_id)
