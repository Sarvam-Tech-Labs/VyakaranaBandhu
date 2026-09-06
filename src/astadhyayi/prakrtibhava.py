# -*- coding: utf-8 -*-
"""
६.१.११५–१३४ — प्रकृतिभाव, where two sounds meet and nothing happens.

Every rule from 6.1.72 has said what a junction DOES. These twenty say
where it does not: **प्रकृतिरिति स्वभावः कारणं वाभिधीयते** — the
sounds stand as they are, in their own nature. ते अग्ने अश्वमायुञ्जन्
keeps its ए and its अ, in the middle of a Vedic pāda, and no rule
of the eighty-six touches it.

**AND HERE THE FOUR ĀCĀRYAS ARE NAMED.** Three of them make the rule
no more optional than the वा already did — **आपिशलिग्रहणं पूजार्थम्।
वेति ह्युच्यत एव** at 6.1.92; **स्फोटायनग्रहणं पूजार्थम्, विभाषेत्येव
हि वर्तते** at 6.1.123; **शाकल्यस्य ग्रहणं पूजार्थम्।
आरम्भसामर्थ्यादेव हि यणादेशेन सह विकल्पः सिद्धः** at 6.1.127. And one
does the opposite: **चाक्रवर्मणग्रहणं विकल्पार्थम्** at 6.1.130 — the
name IS what makes it a choice. Four names, three for honour and one
for force, and the vṛtti says which is which each time.

**AND THE VEDIC RULES ARE SORTED BY WHICH CORPUS THEY HOLD IN.**
6.1.115 wants a position inside a पाद and so cannot reach the
Yajurveda, which has no verse-feet: **यजुषि पादानामभावाद्
अनन्तःपादार्थं वचनम्**, and 6.1.117 to 6.1.121 are stated for it
separately. A condition that fails not because the words are wrong
but because the corpus has no such thing.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule holds the
junction open, and what it leaves standing. It does not build the
Vedic line, and the citations in the notes are the Kāśikā's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: The four ācāryas this pāda names, and what the vṛtti says each
#: name is doing. Three are honour and one is force, and the section
#: would read the same for the first three if the names were struck
#: out — which is exactly why the fourth is worth marking.
TEACHERS: Tuple[Tuple[str, str, str], ...] = (
    ("Āpiśali", "6.1.92", "पूजार्थम् — वेति ह्युच्यत एव"),
    ("Sphoṭāyana", "6.1.123",
     "पूजार्थम् — विभाषेत्येव हि वर्तते"),
    ("Śākalya", "6.1.127",
     "पूजार्थम् — आरम्भसामर्थ्यादेव हि यणादेशेन सह विकल्पः सिद्धः"),
    ("Cākravarmaṇa", "6.1.130", "विकल्पार्थम् — the name IS the option"),
)

#: 6.1.116's seven, which hold the junction open THOUGH a व् or य्
#: follows the अ — the very condition 6.1.115 refuses on.
AVYADI: Tuple[str, ...] = (
    "avyāt", "avadyāt", "avakramuḥ", "avrata", "ayam", "avantu",
    "avasyu",
)

#: 6.1.118's list, all of it read for the Yajurveda alone.
YAJUSI_WORDS: Tuple[str, ...] = (
    "āpo", "juṣāṇo", "vṛṣṇo", "varṣiṣṭhe", "ambe", "ambāle",
)


@dataclass(frozen=True)
class Standing:
    """One rule of 6.1.115–134: what stays as it is, and where."""

    sutra: str
    #: What the rule does: prakṛtibhāva, avaṅ, aplutavat, ut, or
    #: su-lopa.
    does: str = ""
    #: The words the rule names outright.
    of: Tuple[str, ...] = ()
    #: What the EARLIER sound must be.
    after: str = ""
    #: What the LATER sound or word must be.
    before: str = ""
    #: Where in the text it must stand — antaḥpāda, or a sense the
    #: form must carry.
    result: str = ""
    #: What is put in, where the rule puts something in.
    gives: str = ""
    #: The ācārya whose opinion the rule reports.
    teacher: str = ""
    optional: bool = False
    #: True where the option is व्यवस्थितविभाषा — 6.1.123, settled
    #: by which compound the word stands in.
    vyavasthita: bool = False
    #: True where the rule holds in the Vedic corpus at large.
    chandasi: bool = False
    #: True where it holds in the YAJURVEDA alone. Kept apart from
    #: `chandasi` because 6.1.115's condition is a position inside a
    #: verse-foot and that corpus has none.
    yajusi: bool = False
    bahulam: bool = False
    #: The rule this one displaces or narrows, by ITS own number.
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


PRAKRTIBHAVA_TABLE: Tuple[Standing, ...] = (
    Standing(
        "6.1.115", does="prakṛtibhāva", after="eṅ", before="at",
        result="antaḥpāda", chandasi=True,
        keeps_out="एतेऽर्चन्ति — the junction is not inside a पाद; "
                  "तेऽवदन्, तेजोऽयस्मयम् — a व् or य् follows the अ",
        why="प्रकृत्यान्तःपादमव्यपरे — where ए or ओ meets a short अ "
            "inside a Vedic पाद, and no व् or य् follows that अ, both "
            "stand as they are: **ते अग्ने अश्वमायुञ्जन्; उपप्रयन्तो "
            "अध्वरम्; शिरो अपश्यम्; सुजाते अश्वसूनृते**.\\n\\n"
            "**AND प्रकृति IS DEFINED BEFORE IT IS USED.** "
            "**प्रकृतिरिति स्वभावः कारणं वाभिधीयते** — the sounds "
            "keep their own nature, or their character as causes: "
            "**स्वभावेनावतिष्ठते, कारणात्मना वा भवति, न विकारमापद्यते**. "
            "The first rule of the pāda that says nothing "
            "happens.\\n\\n"
            "**AND पाद MEANS A VEDIC FOOT AND NOT A VERSE-LINE.** "
            "**पादशब्देन च ऋक्पादस्यैव ग्रहणमिष्यते, न तु "
            "श्लोकपादस्य** — and the case is settled by "
            "**कया मती कुत एतास एतेऽर्चन्ति**, where the junction "
            "falls at the foot's edge and the rule fails.\\n\\n"
            "**AND SOME READ THE RULE WITH A न् AND MEAN SOMETHING "
            "MUCH LARGER.** **केचिदिदं सूत्रं नान्तःपादमव्यपर इति "
            "पठन्ति, ते संहितायामिह यदुच्यते तस्य सर्वस्य प्रतिषेधं "
            "वर्णयन्ति** — on that reading the rule refuses "
            "EVERYTHING 6.1.72 opened. The vṛtti reports it without "
            "adopting it"),
    Standing(
        "6.1.116", does="prakṛtibhāva", after="eṅ", before="avyādi",
        result="antaḥpāda", chandasi=True, blocks=("6.1.115",),
        why="अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च — seven words "
            "that hold the junction open THOUGH a व् or य् follows "
            "their अ, which is the one thing 6.1.115 refuses on: "
            "**नो अव्यात्; मित्रमहो अवद्यात्; मा शिवासो अवक्रमुः; "
            "ते नो अव्रताः; शतधारो अयं मणिः; ते नो अवन्तु पितरः; "
            "कुशिकासो अवस्यवः**. A list stated for no other reason "
            "than to defeat one word of the rule before"),
    Standing(
        "6.1.117", does="prakṛtibhāva", of=("uras",), before="at",
        yajusi=True,
        why="यजुष्युरः — in the Yajurveda the word उरस् keeps its ओ "
            "and the अ after it: **उरो अन्तरिक्षम्**.\\n\\n"
            "**AND THE RULE EXISTS BECAUSE THAT CORPUS HAS NO "
            "VERSE-FEET.** **यजुषि पादानामभावाद् अनन्तःपादार्थं "
            "वचनम्** — 6.1.115 wants a position inside a पाद, and "
            "there are none to be inside, so the whole run from here "
            "to 6.1.121 is stated over again for prose.\\n\\n"
            "**AND THE VṚTTI REPORTS A SECOND READING OF THE RULE "
            "ITSELF.** **अपरे यजुष्युरो इति सूत्रं पठन्ति** — some "
            "read उरो as the vocative of उरु rather than as उरस् "
            "with its स् gone, and cite **उरो अन्तरिक्षे सजूः** for "
            "it"),
    Standing(
        "6.1.118", does="prakṛtibhāva", of=YAJUSI_WORDS, before="at",
        yajusi=True,
        why="आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे — six "
            "more for the Yajurveda: **आपो अस्मान् मातरः शुन्धयन्तु; "
            "जुषाणो अप्तुराज्यस्य; वृष्णो अंशुभ्यां गभस्तिपूतः; "
            "वर्षिष्ठे अधि नाके; अम्बे अम्बाले अम्बिके**, the last "
            "two only where अम्बिका follows.\\n\\n"
            "**AND BEING LISTED HERE KEEPS ANOTHER RULE OFF THEM.** "
            "**अस्मादेव निपातनाद् अम्बार्थनद्योर्ह्रस्वः इति "
            "ह्रस्वत्वं न भवति** — 7.3.107 would shorten a vocative "
            "in अम्बा, and the words are cited here in their long "
            "form, so it does not"),
    Standing(
        "6.1.119", does="prakṛtibhāva", of=("aṅga",), before="at",
        yajusi=True,
        why="अङ्ग इत्यादौ च — and where अङ्गे is followed by अङ्गे, "
            "both the ए and the अ stand: **ऐन्द्रः प्राणो अङ्गेअङ्गे "
            "अदीध्यत्; ऐन्द्रः प्राणो अङ्गेअङ्गे निदीध्यत्**. The "
            "rule holds the junction open twice over in one phrase"),
    Standing(
        "6.1.120", does="prakṛtibhāva", after="eṅ",
        before="at-anudātta-ku-dha", yajusi=True,
        keeps_out="अधोऽग्रे — अग्रे is आद्युदात्त; सोऽयमग्निः "
                  "सहस्रियः — no guttural or ध follows the अ",
        why="अनुदात्ते च कुधपरे — in the Yajurveda, where the short "
            "अ is अनुदात्त and a guttural or a ध follows it, the "
            "junction stands open: **अयं नो अग्निः; अयं सो "
            "अध्वरः**. Two conditions at once, one on the accent of "
            "the vowel and one on what comes after it, and the "
            "vṛtti gives a counter-example for each"),
    Standing(
        "6.1.121", does="prakṛtibhāva", of=("avapathās",),
        before="at-anudātta", yajusi=True,
        keeps_out="यद्रुद्रेभ्योऽवपथाः — 8.1.30 keeps the निघात off "
                  "after यद्, so the अ is not अनुदात्त there",
        why="अवपथासि च — and before the word अवपथाः with its अ "
            "अनुदात्त: **त्री रुद्रेभ्यो अवपथाः**.\\n\\n"
            "**AND WHERE THAT WORD IS ACCENTED DECIDES IT.** The अ "
            "is अनुदात्त by 8.1.28's तिङ्ङतिङः; put यद् in front and "
            "8.1.30's निपातैर्यद्यदिहन्त… refuses that निघात, the "
            "accent returns, and the junction closes: "
            "**यद्रुद्रेभ्योऽवपथाः**. One word's accent, and the "
            "sandhi goes the other way"),
    Standing(
        "6.1.122", does="prakṛtibhāva", of=("go",), before="at",
        optional=True,
        why="सर्वत्र विभाषा गोः — after गो the short अ may stand "
            "open, and सर्वत्र means in ordinary speech as well as "
            "in the corpus: **गोऽग्रम्, गो अग्रम्**; and in the "
            "corpus **अपशवो वा अन्ये गोअश्वेभ्यः, पशवो गोअश्वान्**. "
            "The one प्रकृतिभाव rule of the run that is not confined "
            "to the Veda"),
    Standing(
        "6.1.123", does="avaṅ", of=("go",), before="ac", gives="avaṅ",
        teacher="Sphoṭāyana", optional=True, vyavasthita=True,
        why="अवङ् स्फोटायनस्य — and instead of holding the junction "
            "open, स्फोटायन puts अवङ् in for the ओ of गो before any "
            "vowel: **गवाग्रम्, गवाजिनम्, गवौदनम्** beside "
            "**गोऽग्रम्, गोऽजिनम्, गवोदनम्**. **अतीति निवृत्तम्** — "
            "the short अ of the rule before has lapsed, so this one "
            "reaches every vowel.\\n\\n"
            "**AND THE NAME IS FOR HONOUR, NOT FOR THE OPTION.** "
            "**स्फोटायनग्रहणं पूजार्थम्, विभाषेत्येव हि वर्तते** — "
            "the विभाषा was already carrying. The second of four "
            "ācāryas named in this pāda and the second whose name "
            "adds nothing but respect.\\n\\n"
            "**AND THE OPTION IS SETTLED WHERE IT MATTERS.** "
            "**व्यवस्थितविभाषेयम्, तेन गवाक्ष इत्यत्र नित्यमवङ् "
            "भवति** — in गवाक्ष the substitute is fixed.\\n\\n"
            "**AND THE SUBSTITUTE CARRIES ITS OWN ACCENT.** "
            "**आद्युदात्तश्चायमादेशो निपात्यते**, and that accent "
            "survives in a बहुव्रीहि — **गवाग्रः** — where elsewhere "
            "6.1.223's compound-final उदात्त would displace it"),
    Standing(
        "6.1.124", does="avaṅ", of=("go",), before="indra",
        gives="avaṅ", blocks=("6.1.123",),
        why="इन्द्रे च नित्यम् — before a vowel of the word इन्द्र "
            "the substitute is FIXED: **गवेन्द्रः, "
            "गवेन्द्रयज्ञस्वरः**. The word नित्यम् is what takes the "
            "option away, as नित्यम् did at 6.1.57 and 6.1.100 — and "
            "the vṛtti notes that **नित्य** is not read here by "
            "everyone"),
    Standing(
        "6.1.125", does="prakṛtibhāva", after="pluta-pragṛhya",
        before="ac", blocks=("6.1.127",),
        keeps_out="जानु उ अस्य — the उ there is not what would cause "
                  "the change, so 6.1.101 lengthens and the rule "
                  "does not hold",
        why="प्लुतप्रगृह्या अचि — a प्लुत vowel and a प्रगृह्य one "
            "stand open before any vowel: **देवदत्त३ अत्र न्वसि; "
            "अग्नी इति, वायू इति, खट्वे इति, माले इति**.\\n\\n"
            "**AND THE त्रिपादी IS NOT असिद्ध HERE.** प्लुत is laid "
            "down in the last three pādas and 8.2.1 would make it "
            "invisible to a rule of this one. **आश्रयादत्र प्लुतः "
            "सिद्धः** — being what the rule RESTS on rather than "
            "what it works against, it counts.\\n\\n"
            "**AND अचि IS SAID AGAIN THOUGH IT WAS ALREADY "
            "CARRYING.** **पुनरज्ग्रहणम् आदेशनिमित्तस्याचः "
            "परिग्रहार्थम्** — the vowel must be the one that would "
            "CAUSE the change. In जानु उ अस्य the following अ is no "
            "cause of the lengthening, so the lengthening happens "
            "anyway.\\n\\n"
            "**AND नित्यम् CARRIES DOWN FROM 6.1.124 TO KEEP ŚĀKALYA "
            "OFF.** **नित्यग्रहणमिहानुवर्तते। प्लुतप्रगृह्याणां "
            "नित्यमयमेव प्रकृतिभावो यथा स्याद् इकोऽसवर्णे इत्येतन् "
            "मा भूत्** — otherwise 6.1.127 would offer a shortened "
            "form beside it"),
    Standing(
        "6.1.126", does="prakṛtibhāva", of=("āṅ",), before="ac",
        gives="anunāsika", chandasi=True,
        keeps_out="इन्द्रो बाहुभ्यामातरत् — on the reading with "
                  "बहुलम्, the junction closes",
        why="आङोऽनुनासिकश्छन्दसि — in the corpus the preverb आ "
            "becomes nasalised before a vowel, and stands open: "
            "**अभ्र आँ अपः; गभीर आँ उग्रपुत्रे जिघांसतः**. And "
            "**केचिद् आङोऽनुनासिकश्छन्दसि बहुलम् इत्यधीयते** — some "
            "read बहुलम् into it, which is what admits "
            "**इन्द्रो बाहुभ्यामातरत्**"),
    Standing(
        "6.1.127", does="prakṛtibhāva", after="ik", before="asavarṇa-ac",
        gives="hrasva", teacher="Śākalya", optional=True,
        keeps_out="खट्वेन्द्रः — the earlier sound is not an इक्; "
                  "कुमारीन्द्रः — the two are savarṇa",
        why="इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च — शाकल्य holds that an "
            "इक् before an unlike vowel stands open, AND is "
            "shortened if it was long: **दधि अत्र, मधु अत्र, "
            "कुमारि अत्र, किशोरि अत्र** beside **दध्यत्र, मध्वत्र, "
            "कुमार्यत्र**.\\n\\n"
            "**AND THE NAME IS FOR HONOUR AGAIN.** **शाकल्यस्य "
            "ग्रहणं पूजार्थम्। आरम्भसामर्थ्यादेव हि यणादेशेन सह "
            "विकल्पः सिद्धः** — the rule's mere existence beside "
            "6.1.77 already makes the two alternatives.\\n\\n"
            "**AND TWO SUPPLEMENTS KEEP IT OUT OF TWO PLACES.** "
            "**सिन्नित्यसमासयोः शाकलप्रतिषेधो वक्तव्यः** — before a "
            "सित् affix (**ऋत्वियः**) and in a fixed compound "
            "(**व्याकरणम्, कुमार्यर्थम्**). And "
            "**ईषाअक्षादिषु छन्दसि प्रकृतिभावमात्रं वक्तव्यम्** — "
            "**इषा अक्षो हिरण्ययः; पथा अगमन्**, where the junction "
            "stands open WITHOUT the shortening"),
    Standing(
        "6.1.128", does="prakṛtibhāva", after="ak", before="ṛ",
        gives="hrasva", teacher="Śākalya", optional=True,
        keeps_out="खट्वेन्द्रः — the following vowel is not ऋ; "
                  "वृक्षावृश्यः — the earlier sound is not an अक्",
        why="ऋत्यकः — and before ऋ the same, now for an अक् and not "
            "only an इक्: **खट्व ऋश्यः, माल ऋश्यः, कुमारि ऋश्यः, "
            "होतृ ऋश्यः**.\\n\\n"
            "**AND THE RULE IS STATED FOR TWO THINGS THE ONE BEFORE "
            "IT COULD NOT DO.** **सवर्णार्थमनिगर्थं च वचनम्** — it "
            "reaches a savarṇa pair, which 6.1.127 excluded, and it "
            "reaches अ and आ, which are not इक् at all"),
    Standing(
        "6.1.129", does="aplutavat", after="pluta", before="upasthita",
        blocks=("6.1.125",),
        why="अप्लुतवदुपस्थिते — before the इति of a पदपाठ, a प्लुत "
            "vowel is treated LIKE a non-प्लुत one, so 6.1.125's "
            "प्रकृतिभाव does not hold and the junction closes: "
            "**सुश्लोक३ इति सुश्लोकेति; सुमङ्गल३ इति "
            "सुमङ्गलेति**.\\n\\n"
            "**AND उपस्थित IS DEFINED AS A THING THE ṚṢIS DID "
            "NOT DO.** **उपस्थितं नाम अनार्ष इतिकरणः, समुदायाद् "
            "अवच्छिद्य पदं येन स्वरूपेऽवस्थाप्यते** — the इति that "
            "a later analyst puts after a word to cut it out of the "
            "line and hold it in its own shape. The rule is about "
            "the पदपाठ and not about the text.\\n\\n"
            "**AND वत् IS SAID RATHER THAN अप्लुतः.** "
            "**वत्करणं किम्? अप्लुत इत्युच्यमाने प्लुत एव "
            "प्रतिषिध्यते** — say the प्लुत IS non-प्लुत and it "
            "ceases to be one, and then a vowel that is both प्लुत "
            "and प्रगृह्य would lose its length as well: "
            "**अग्नी३ इति, वायू३ इति**. *Treated like* keeps the "
            "length and takes only the प्रकृतिभाव"),
    Standing(
        "6.1.130", does="aplutavat", after="ī3", before="ac",
        teacher="Cākravarmaṇa", optional=True,
        why="ई३ चाक्रवर्मणस्य — चाक्रवर्मण holds that a प्लुत ई३ "
            "before a vowel is treated like a non-प्लुत one: "
            "**अस्तु हीत्यब्रूताम्** beside **अस्ति ही३ "
            "इत्यब्रूताम्**; **चिनु हीदम्** beside **चिनु ही३ "
            "इदम्**.\\n\\n"
            "**AND THIS NAME IS NOT FOR HONOUR.** "
            "**चाक्रवर्मणग्रहणं विकल्पार्थम्** — the name is what "
            "MAKES the rule a choice, where the other three teachers "
            "of this pāda are named **पूजार्थम्** beside a वा that "
            "already said it. One word of commentary, and the four "
            "names stop being one thing.\\n\\n"
            "**AND IT IS AN उभयत्रविभाषा.** "
            "**तदुपस्थिते निवृत्त्यर्थम् अनुपस्थिते प्राप्त्यर्थम्** "
            "— before इति it LOOSENS what 6.1.129 made fixed; "
            "elsewhere it SUPPLIES against 6.1.125's प्रकृतिभाव. And "
            "**ईकारादन्यत्राप्ययमप्लुतवद्भाव इष्यते** — "
            "**वशा३ इयम्, वशेयम्**"),
    Standing(
        "6.1.131", does="ut", of=("div",), result="pada", gives="u",
        keeps_out="दिवौ, दिवः — not a पद there; अक्षद्यूभ्याम् — "
                  "that दिव् is the ROOT, which is taught with a "
                  "marker",
        why="दिव उत् — where दिव् is a पद, उ stands for its final: "
            "**द्युकामः, द्युमान्, विमलद्यु दिनम्, द्युभ्याम्, "
            "द्युभिः**.\\n\\n"
            "**AND WHICH दिव् IS MEANT IS SETTLED BY A MAXIM ABOUT "
            "MARKERS.** **दिव इति प्रातिपदिकं गृह्यते न धातुः, "
            "सानुबन्धकत्वात्**, and **निरनुबन्धकग्रहणात्** — a word "
            "cited without markers means the one that has none. The "
            "root is दिवु, so it is not reached, and 6.4.19's ऊठ् "
            "gives **अक्षद्यूभ्याम्** instead.\\n\\n"
            "**AND THE त् IN उत् IS WHAT KEEPS THAT ऊठ् OFF HERE "
            "TOO.** **तपरकरणमूठो निवृत्त्यर्थम्** — a SHORT उ, since "
            "ऊठ् is stated later and would otherwise win on "
            "परत्व"),
    Standing(
        "6.1.132", does="su-lopa", of=("etad", "tad"), before="hal",
        keeps_out="यो ददाति — not एतद् or तद्; एतौ गावौ चरतः — not "
                  "the nominative singular; एषको ददाति — क stands "
                  "in the middle; अनेषो ददाति — a नञ् compound; "
                  "एषोऽत्र — a vowel follows",
        why="एतत्तदोः सुलोपोऽकोरनञ्समासे हलि — the nominative "
            "singular स् of एतद् and तद् is dropped before a "
            "consonant: **एष ददाति, स ददाति; एष भुङ्क्ते, स "
            "भुङ्क्ते**.\\n\\n"
            "**AND अकोः IS NEEDED BECAUSE OF A MAXIM.** "
            "**तन्मध्यपतितस्तद्ग्रहणेन गृह्यते** — a form with "
            "something inserted INTO it is still reached by the name "
            "of the thing it was inserted into, so एषक and सक would "
            "count as एतद् and तद् despite the क. The refusal is "
            "stated to stop that: **एषको ददाति, सको "
            "ददाति**.\\n\\n"
            "**AND अनञ्समासे TURNS ON WHERE THE MEANING SITS.** "
            "**उत्तरपदार्थप्रधानत्वाद् नञ्समासस्यैतत्तदोरेवात्र "
            "संबद्धः सुशब्दः** — in a नञ् compound the second member "
            "carries the sense, so the स् there really is एतद्'s and "
            "would be dropped; the rule says it is not: "
            "**अनेषो ददाति, असो ददाति**"),
    Standing(
        "6.1.133", does="su-lopa", of=("sya",), before="hal",
        chandasi=True, bahulam=True,
        keeps_out="यत्र स्यो निपतेत् — the same corpus, and the स् "
                  "standing",
        why="स्यश्छन्दसि बहुलम् — in the corpus the nominative "
            "singular ending is variously dropped after स्य before a "
            "consonant: **उत स्य वाजी क्षिपणिं तुरण्यति; एष स्य ते "
            "पवत इन्द्र सोमः** — and **न च भवति — यत्र स्यो "
            "निपतेत्**"),
    Standing(
        "6.1.134", does="su-lopa", of=("sa",), before="ac",
        result="pādapūraṇa", chandasi=True,
        keeps_out="स इव व्याघ्रो भवेत् — dropping it would not fill "
                  "out the foot",
        why="सोऽचि लोपे चेत् पादपूरणम् — the ending of सस् is dropped "
            "before a vowel, IF dropping it fills out the foot: "
            "**सेदु राजा क्षयति चर्षणीनाम्; सौषधीरनुरुध्यसे**. A "
            "condition on the METRE, and the only one in the "
            "pāda.\\n\\n"
            "**AND अचि IS SAID FOR CLARITY RATHER THAN FOR FORCE.** "
            "**अचीति विस्पष्टार्थम्** — before a consonant the "
            "syllable count would not change and the metre would "
            "gain nothing; it is the sandhi with a vowel that "
            "shortens the line.\\n\\n"
            "**AND SOME READ पाद AS A ŚLOKA'S FOOT TOO.** "
            "**पादग्रहणेनात्र श्लोकपादस्यापि ग्रहणं केचिदिच्छन्ति**, "
            "and then the verse **सैष दाशरथी रामः सैष राजा "
            "युधिष्ठिरः** is reached as well. 6.1.115 took पाद the "
            "other way, and the two readings stand side by side in "
            "one pāda"),
)


@dataclass(frozen=True)
class Stands:
    """What the resolver answers with."""

    does: str
    sutra: str
    why: str
    gives: str = ""
    teacher: str = ""
    optional: bool = False
    vyavasthita: bool = False
    chandasi: bool = False
    yajusi: bool = False
    bahulam: bool = False
    #: Where a rule displaces another, that rule's number.
    blocked_by: Tuple[str, ...] = ()


def _reaches(row: Standing, stem: str, after: str, before: str,
             result: str, teacher: str, chandasi: bool,
             yajusi: bool) -> bool:
    if row.chandasi and not chandasi:
        return False
    if row.yajusi and not yajusi:
        return False
    if row.teacher and teacher != row.teacher:
        return False
    if row.of and stem not in row.of:
        return False
    if row.after and after != row.after:
        return False
    if row.before and before != row.before:
        return False
    if row.result and result != row.result:
        return False
    return True


def _supplies(row: Standing, wants: str) -> bool:
    return not wants or wants == row.does


def _how_specific(row: Standing) -> int:
    """
    A named word beats a shape, and an ācārya's name beats both.

    The teacher counts highest because two of the four state rules
    that stand exactly where an unattributed one already does —
    6.1.123 against 6.1.122, 6.1.130 against 6.1.129 — and are
    distinguishable by nothing else a question can carry.
    """
    return (
        9 * bool(row.teacher)
        + 8 * bool(row.of)
        + 5 * bool(row.result)
        + 4 * bool(row.after)
        + 3 * bool(row.before)
        + 2 * bool(row.yajusi)
    )


def stands_open(stem: str = "", *, after: str = "", before: str = "",
                result: str = "", teacher: str = "",
                chandasi: bool = False, yajusi: bool = False,
                wants: str = "") -> Stands:
    """
    6.1.115–134 — where a junction is held open, and where it is not.

    `yajusi` is kept apart from `chandasi` because 6.1.115's condition
    is a POSITION inside a verse-foot, and the Yajurveda has none:
    **यजुषि पादानामभावाद् अनन्तःपादार्थं वचनम्**. Six rules are stated
    over again for that corpus for no other reason.

    Nothing answers by default. These rules say what does NOT happen,
    so where none is reached the ordinary sandhi of 6.1.72–114 holds.
    """
    matched = [
        row for row in PRAKRTIBHAVA_TABLE
        if _reaches(row, stem, after, before, result, teacher,
                    chandasi, yajusi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Stands(
            "", "", "No rule of 6.1.115–134 is reached, so nothing "
                    "holds the junction open and the ordinary rules "
                    "of 6.1.72–114 take it")
    row = max(matched, key=_how_specific)
    return Stands(row.does, row.sutra, row.why, gives=row.gives,
                  teacher=row.teacher, optional=row.optional,
                  vyavasthita=row.vyavasthita, chandasi=row.chandasi,
                  yajusi=row.yajusi, bahulam=row.bahulam,
                  blocked_by=row.blocks)


def named_teachers() -> Tuple[Tuple[str, str, str], ...]:
    """
    The four ācāryas named in this pāda, with what the vṛtti says
    each name is doing.

    Three are **पूजार्थम्**, honour beside a वा that already made the
    rule optional; the fourth is **विकल्पार्थम्**, and is what makes
    it optional at all. The distinction is the commentary's own and
    is not visible from the sūtras.
    """
    return TEACHERS


def provisions_for(sutra_id: str) -> Tuple[Standing, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in PRAKRTIBHAVA_TABLE
                 if row.sutra == sutra_id)
