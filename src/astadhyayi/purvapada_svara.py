# -*- coding: utf-8 -*-
"""
६.२.१–६३ — बहुव्रीहौ प्रकृत्या पूर्वपदम्, and a compound keeps two
accents where 6.1.223 allowed it one.

6.1.223 समासस्य put the accent at the end of a compound, and 6.1.158
then made every other syllable अनुदात्त. This pāda is the exceptions,
and 6.2.1 opens them: **समासान्तोदात्तत्वे हि सति अनुदात्तं
पदमेकवर्जम् इति सोऽनुदात्तः स्यादिति समासान्तोदात्तत्वापवादोऽयम्
आरभ्यते** — in a बहुव्रीहि the FIRST member keeps the accent it had
before the compound was made.

**प्रकृत्या MEANS THE ACCENT IS NOT CHANGED, NOT THAT IT IS PUT
SOMEWHERE.** **पूर्वपदग्रहणमत्र पूर्वपदस्थे स्वर उदात्ते स्वरिते वा
वर्तते... स्वभावेनावतिष्ठते, न विकारमनुदात्तत्वमापद्यते.** Which
syllable of the first member carries it is whatever some earlier rule
already settled — 6.1.197's first syllable for कार्ष्ण, 6.1.193's
middle one for अध्यापक, 6.2.139's last one for ब्रह्मचारिन्. So a
single rule here answers three different placements.

**AND WHAT DECIDES A RULE OF THIS SECTION IS ALMOST ALWAYS THE SECOND
MEMBER.** Sixty-three sūtras and the pattern hardly varies: name the
word that must FOLLOW — गाध, दायाद, पति, सदृश, स्वामिन् — and add a
SENSE the compound must carry. Change the sense and the compound
falls back to 6.1.223: **गोस्वामी** against **परमस्वामी**,
**गृहपतिः** against **वृषलीपतिः**.

**AND ONE RULE OF IT PUTS TWO ACCENTS AT ONCE.** 6.2.51 तवै च अन्तश्च
युगपत् — the तवै takes the accent at its end and the preverb keeps its
own, at the same time. The second such rule the project has met, after
6.1.200, and both use the same word युगपत्.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule lets the first
member keep its accent. WHICH syllable that is was settled by 6.1's
rules, and `pada_svara` holds those.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where प्रकृत्या पूर्वपदम् governs. 6.2.64's vṛtti bounds it by
#: taking over: **आदिरुदात्त इत्येतदधिकृतम्। इत उत्तरं यद्
#: वक्ष्यामस्तत्र पूर्वपदस्यादिरुदात्तो भवति** — so this run stops
#: where that one starts.
PRAKRTYA_RUN: Tuple[str, str] = ("6.2.1", "6.2.63")

#: And पूर्वपद itself governs much further — to 6.2.110, where
#: 6.2.111's उत्तरपदादिः takes the whole rest of the pāda: **प्राग्
#: उत्तरपदादिः इत्येतस्माद् अयम् अधिकारो वेदितव्यः**.
PURVAPADA_RUN: Tuple[str, str] = ("6.2.1", "6.2.110")

#: The seven kinds of first member 6.2.2 names for a तत्पुरुष. Not a
#: list of words: each is a description, and three of the seven are
#: case-endings.
TATPURUSA_KINDS: Tuple[str, ...] = (
    "tulyārtha", "tṛtīyā", "saptamī", "upamāna", "avyaya",
    "dvitīyā", "kṛtya",
)

#: What the rule is an exception TO, named in 6.2.1's own vṛtti.
WHAT_IT_EXCEPTS: str = "समासान्तोदात्तत्वापवादोऽयम् आरभ्यते"


@dataclass(frozen=True)
class Purvapada:
    """One rule of 6.2.1–63: when the first member keeps its accent."""

    sutra: str
    #: What happens to the first member: prakṛti (it keeps whatever
    #: accent it had), or ādi (its first syllable takes an उदात्त),
    #: or ādi-anta where two accents fall at once.
    keeps: str = "prakṛti"
    #: The first members the rule names.
    of: Tuple[str, ...] = ()
    #: A named class of first member instead — विस्पष्टादि,
    #: दासीभारादि, संख्या.
    gana: str = ""
    #: The kinds of first member 6.2.2 names, which are neither words
    #: nor a gaṇa.
    kinds: Tuple[str, ...] = ()
    #: The words that must FOLLOW. This is what nearly every rule of
    #: the section turns on.
    uttarapada: Tuple[str, ...] = ()
    #: What the second member must END IN, where the rule names an
    #: affix rather than a word — क्त, तवै, अञ्च्.
    uttarapada_affix: str = ""
    #: Which compound it must be.
    samasa: str = ""
    #: The case the first member stands in.
    case: str = ""
    #: The sense the compound must carry, which is what most often
    #: separates a rule of this section from 6.1.223.
    result: str = ""
    #: What the rule keeps out of its own first-member class.
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    #: True where the row IS a heading.
    heading: bool = False
    #: The rule this one displaces or refuses, by ITS own number.
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


PURVAPADA_TABLE: Tuple[Purvapada, ...] = (
    Purvapada(
        "6.2.1", samasa="bahuvrīhi", heading=True,
        why="बहुव्रीहौ प्रकृत्या पूर्वपदम् — in a बहुव्रीहि the first "
            "member keeps the accent it had: **कार्ष्णोत्तरासङ्गाः, "
            "यूपवलजः, ब्रह्मचारिपरिस्कन्दः, स्नातकपुत्रः, "
            "अध्यापकपुत्रः, श्रोत्रियपुत्रः**.\\n\\n"
            "**AND THE WHOLE PĀDA OPENS AS AN EXCEPTION.** "
            "**समासान्तोदात्तत्वे हि सति अनुदात्तं पदमेकवर्जम् इति "
            "सोऽनुदात्तः स्यादिति समासान्तोदात्तत्वापवादोऽयम् "
            "आरभ्यते** — 6.1.223 put the accent at the end and "
            "6.1.158 silenced the rest, so without this rule the "
            "first member would have none.\\n\\n"
            "**AND प्रकृत्या SAYS THE ACCENT IS NOT CHANGED, NOT "
            "WHERE IT GOES.** **पूर्वपदग्रहणमत्र पूर्वपदस्थे स्वर "
            "उदात्ते स्वरिते वा वर्तते... स्वभावेनावतिष्ठते, न "
            "विकारमनुदात्तत्वमापद्यते** — an उदात्त or a स्वरित, "
            "wherever an earlier rule put it. The six forms above "
            "carry it on the first syllable, the middle and the "
            "last between them, and one rule answers all three"),
    Purvapada(
        "6.2.2", samasa="tatpuruṣa", kinds=TATPURUSA_KINDS,
        why="तत्पुरुषे तुल्यार्थतृतीयासप्तम्युपमानाव्ययद्वितीयाकृत्याः "
            "— seven kinds of first member keep their accent in a "
            "तत्पुरुष, and they are described rather than listed: a "
            "word meaning *like*, an instrumental, a locative, what "
            "the second member is compared to, an indeclinable, an "
            "accusative, and a कृत्य participle. **तुल्यश्वेतः, "
            "सदृक्श्वेतः, सदृशश्वेतः; शङ्कुलाखण्डः, किरिकाणः**.\\n\\n"
            "**AND THE THREE FORMS OF THE FIRST EXAMPLE CARRY THREE "
            "DIFFERENT ACCENTS.** तुल्य is first-accented by "
            "6.1.213, सदृक् end-accented by 6.1.197 and 6.2.139, and "
            "सदृश middle-accented. One rule, three placements, and "
            "प्रकृत्या is what lets it be so"),
    Purvapada(
        "6.2.3", samasa="tatpuruṣa", of=("varṇa",),
        uttarapada=("varṇa",), excludes=("eta",),
        keeps_out="परमकृष्णः — the first member is no colour; "
                  "कृष्णतिलाः — the second is not; कृष्णैतः — the "
                  "second is एत, which the rule excepts",
        why="वर्णो वर्णेष्वनेते — a colour-word before another "
            "colour-word, and not before एत: **कृष्णसारङ्गः, "
            "लोहितकल्माषः**. Three conditions and the vṛtti gives a "
            "counter-example for each, which is the shape almost "
            "every rule of this section takes"),
    Purvapada(
        "6.2.4", samasa="tatpuruṣa", uttarapada=("gādha", "lavaṇa"),
        result="pramāṇa",
        keeps_out="परमगाधम्, परमलवणम् — no measure meant",
        why="गाधलवणयोः प्रमाणे — before गाध or लवण where a MEASURE is "
            "meant: **शम्बगाधमुदकम्** — water only as deep as an "
            "oar; **गोलवणम्** — as much salt as is given to a "
            "cow.\\n\\n"
            "**AND प्रमाण IS READ WIDELY.** **प्रमाणमियत्तापरिच्छेद"
            "मात्रमिह द्रष्टव्यम्, न पुनरायाम एव** — any settling of "
            "how much, and not length alone"),
    Purvapada(
        "6.2.5", samasa="tatpuruṣa", uttarapada=("dāyāda",),
        result="dāyādya",
        keeps_out="परमदायादः — the first member is not what is "
                  "inherited",
        why="दायाद्यं दायादे — before दायाद, where the first member "
            "names what is INHERITED: **विद्यादायादः, "
            "धनदायादः**.\\n\\n"
            "**AND THE COMPOUND HAD TO BE ARGUED INTO EXISTENCE.** "
            "2.3.39 gives दायाद its own genitive, and "
            "**प्रतिपदविधाना च षष्ठी न समस्यते** would then forbid "
            "the compound. The answer is that the genitive here is "
            "the residual one of 2.3.50, which 2.3.39 was stated "
            "beside rather than against: **शेषलक्षणैवात्र षष्ठी**"),
    Purvapada(
        "6.2.6", samasa="tatpuruṣa", uttarapada=("cira", "kṛcchra"),
        result="pratibandhin",
        keeps_out="मूत्रकृच्छ्रम् — the first member is no obstacle",
        why="प्रतिबन्धि चिरकृच्छ्रयोः — before चिर or कृच्छ्र, where "
            "the first member names what MEETS an obstacle: "
            "**गमनचिरम्, गमनकृच्छ्रम्, व्याहरणचिरम्**. And the "
            "vṛtti glosses the condition rather than assuming it: "
            "**गमनं हि कारणविकलतया चिरकालभावि कृच्छ्रयोगि वा "
            "प्रतिबन्धि जायते**"),
    Purvapada(
        "6.2.7", samasa="tatpuruṣa", uttarapada=("pada",),
        result="apadeśa",
        keeps_out="विष्णुपदम् — a foot, not a pretext",
        why="पदेऽपदेशे — before पद in the sense of a PRETEXT, which "
            "the vṛtti glosses **अपदेशो व्याजः**: **मूत्रपदेन "
            "प्रस्थितः, उच्चारपदेन प्रस्थितः** — gone on the pretext "
            "of relieving himself"),
    Purvapada(
        "6.2.8", samasa="tatpuruṣa", uttarapada=("nivāta",),
        result="vātatrāṇa",
        keeps_out="राजनिवाते वसति; सुखं मातृनिवातम् — there निवात "
                  "means a side or a shelter of another kind",
        why="निवाते वातत्राणे — before निवात where a SHELTER FROM "
            "WIND is meant: **कुटीनिवातम्, शमीनिवातम्, "
            "कुड्यनिवातम्** — a hut, an acacia or a wall as the one "
            "thing between you and the wind.\\n\\n"
            "**AND THE WORD ITSELF IS ANALYSED TWO WAYS.** "
            "**वातस्याभावो निवातम्** by 2.1.6's अव्ययीभाव, or "
            "**निरुद्धो वातोऽस्मिन्निति बहुव्रीहिः** — and either "
            "way it is then compounded again with what shelters"),
    Purvapada(
        "6.2.9", samasa="tatpuruṣa", uttarapada=("śārada",),
        result="anārtava",
        keeps_out="परमशारदम् — of the autumn season, which is what "
                  "आर्तव means",
        why="शारदेऽनार्तवे — before शारद where it does NOT mean *of "
            "the autumn*: **रज्जुशारदमुदकम्** — water fresh drawn; "
            "**दृषत्शारदाः सक्तवः** — flour fresh from the "
            "grindstone. **शारदशब्दोऽयं प्रत्यग्रवाची**, and the "
            "compound has no analysis of its own: "
            "**नित्यसमासोऽस्वपदविग्रह इष्यते**"),
    Purvapada(
        "6.2.10", samasa="tatpuruṣa",
        uttarapada=("adhvaryu", "kaṣāya"), result="jāti",
        why="अध्वर्युकषाययोर्जातौ — before these two where a KIND is "
            "meant: **प्राच्याध्वर्युः, कठाध्वर्युः, "
            "कालापाध्वर्युः; सर्पिर्मण्डकषायम्, उमापुष्पकषायम्**. "
            "**एते समानाधिकरणसमासा जातिवाचिनो नियतविषयाः** — "
            "appositional compounds with a settled field"),
    Purvapada(
        "6.2.11", samasa="tatpuruṣa",
        uttarapada=("sadṛśa", "pratirūpa"), result="sādṛśya",
        keeps_out="परमसदृशः — the sense there is being praised, not "
                  "resembling",
        why="सदृशप्रतिरूपयोः सादृश्ये — before these two where "
            "RESEMBLANCE is meant: **पितृसदृशः, मातृसदृशः; "
            "पितृप्रतिरूपः**.\\n\\n"
            "**AND सदृश IS NAMED THOUGH 6.2.2 ALREADY REACHED IT.** "
            "2.1.31 makes सदृश an instrumental तत्पुरुष, which "
            "6.2.2 covers. **षष्ठीसमासार्थं च सदृशग्रहणमिह** — it "
            "is named here for the GENITIVE compound, and "
            "particularly where the ending is not dropped: "
            "**दास्याःसदृशः, वृषल्याःसदृशः**"),
    Purvapada(
        "6.2.12", samasa="dvigu", uttarapada=("dvigu",),
        result="pramāṇa",
        keeps_out="व्रीहिप्रस्थः — no द्विगु; परमसप्तशमः — no measure",
        why="द्विगौ प्रमाणे — before a द्विगु where a measure is "
            "meant: **प्राच्यसप्तशमः, गान्धारिसप्तशमः** — seven "
            "*śama* being its measure, with the मात्रच् dropped by a "
            "vārttika on 5.2.37"),
    Purvapada(
        "6.2.13", samasa="tatpuruṣa", uttarapada=("vāṇija",),
        of=("gantavya", "paṇya"),
        keeps_out="परमवाणिजः, उत्तमवाणिजः",
        why="गन्तव्यपण्यं वाणिजे — before वाणिज, where the first "
            "member names either where the trader GOES or what he "
            "SELLS: **मद्रवाणिजः, काश्मीरवाणिजः** — one who trades "
            "by going to Madra; **गोवाणिजः, अश्ववाणिजः** — one who "
            "trades in cattle. Two quite different relations in one "
            "rule, and the vṛtti separates them"),
    Purvapada(
        "6.2.14", samasa="tatpuruṣa",
        uttarapada=("mātra", "upajñā", "upakrama", "chāyā"),
        result="napuṃsaka",
        why="मात्रोपज्ञोपक्रमच्छाये नपुंसके — before four words where "
            "the compound is NEUTER: **भिक्षामात्रं न ददाति "
            "याचितः; समुद्रमात्रं न सरोऽस्ति किंचन; पाणिनोपज्ञम् "
            "अकालकं व्याकरणम्; व्याड्युपज्ञं दुष्करणम्; "
            "आपिशल्युपज्ञं गुरुलाघवम्**.\\n\\n"
            "**AND मात्र IS SAID TO MEAN *AS MUCH AS* ONLY INSIDE A "
            "COMPOUND.** **मात्रशब्दोऽयं वृत्तिविषय एव तुल्यप्रमाणे "
            "वर्तते** — outside one it does not, so the compound has "
            "no analysis: **अस्वपदविग्रहः षष्ठीसमासः**"),
    Purvapada(
        "6.2.15", samasa="tatpuruṣa", uttarapada=("sukha", "priya"),
        result="hita",
        keeps_out="परमसुखम्, परमप्रियम्",
        why="सुखप्रिययोर्हिते — before सुख or प्रिय where what is "
            "GOOD FOR one is meant: **गमनसुखम्, वचनसुखम्; "
            "गमनप्रियम्**. And the vṛtti defines हित by what it "
            "does: **तद्धि हितं यदायत्यां प्रीतिं करोति** — what "
            "makes for pleasure in time to come"),
    Purvapada(
        "6.2.16", samasa="tatpuruṣa", uttarapada=("sukha", "priya"),
        result="prīti",
        keeps_out="राजसुखम्, राजप्रियम्",
        why="प्रीतौ च — and where PLEASURE itself is meant: "
            "**ब्राह्मणसुखं पायसम्; छात्रप्रियोऽनध्यायः; "
            "कन्याप्रियो मृदङ्गः**.\\n\\n"
            "**AND THE SECOND SENSE-WORD LOOKS IDLE AND IS NOT.** "
            "**सुखप्रिययोः प्रीत्यव्यभिचारादिह प्रीतिग्रहणं "
            "तदतिशयप्रतिपत्त्यर्थम्** — pleasure never fails of "
            "these two words, so the word is there for the DEGREE "
            "of it"),
    Purvapada(
        "6.2.17", samasa="tatpuruṣa", uttarapada=("svāmin",),
        of=("sva",),
        keeps_out="परमस्वामी",
        why="स्वं स्वामिनि — before स्वामिन्, where the first member "
            "names what is OWNED: **गोस्वामी, अश्वस्वामी, "
            "धनस्वामी**"),
    Purvapada(
        "6.2.18", samasa="tatpuruṣa", uttarapada=("pati",),
        result="aiśvarya",
        keeps_out="ब्राह्मणो वृषलीपतिः — a husband, not a lord",
        why="पत्यावैश्वर्ये — before पति where LORDSHIP is meant: "
            "**गृहपतिः, सेनापतिः, नरपतिः, धान्यपतिः**. Where the "
            "word means a husband instead the compound falls back "
            "to 6.1.223"),
    Purvapada(
        "6.2.19", of=("bhū", "vāc", "cit", "didhiṣū"),
        uttarapada=("pati",), samasa="tatpuruṣa", result="aiśvarya",
        refuses=True, blocks=("6.2.18",),
        why="न भूवाक्चिद्दिधिषु — four first members are refused what "
            "the rule before gives: **भूपतिः, वाक्पतिः, चित्पतिः, "
            "दिधिषूपतिः**, and **समासस्वरेणान्तोदात्ता भवन्ति** — "
            "6.1.223 takes them back"),
    Purvapada(
        "6.2.20", of=("bhuvana",), uttarapada=("pati",),
        samasa="tatpuruṣa", result="aiśvarya", optional=True,
        why="वा भुवनम् — and भुवन optionally: **भुवनपतिः** with the "
            "first syllable accented, beside the end-accented "
            "form.\\n\\n"
            "**AND THE WORD IS VEDIC IN ITS DERIVATION AND NOT IN "
            "ITS USE.** भुवन comes from a उणादि rule stated "
            "**छन्दसि**; **कथं भुवनपतिरादित्य इति? उणादयो बहुलम् "
            "इति बहुलवचनाद् भाषायामपि प्रयुज्यते**"),
    Purvapada(
        "6.2.21", samasa="tatpuruṣa",
        uttarapada=("āśaṅka", "ābādha", "nedīyas"),
        result="sambhāvana",
        keeps_out="परमनेदीयः",
        why="आशङ्काबाधनेदीयस्सु संभावने — before three words where "
            "SUPPOSING is meant, and the vṛtti defines it: "
            "**अस्तित्वाध्यवसायः संभावनम्**, settling that a thing "
            "is so. **गमनाशङ्कं वर्तते** — it is supposed that going "
            "is feared; **गमनाबाधम्; गमननेदीयः**"),
    Purvapada(
        "6.2.22", samasa="tatpuruṣa", uttarapada=("pūrva",),
        result="bhūtapūrva",
        keeps_out="परमपूर्वः — there the compound is *the foremost "
                  "and first*, not *formerly foremost*",
        why="पूर्वे भूतपूर्वे — before पूर्व in the sense of "
            "*formerly so*: **आढ्यो भूतपूर्व आढ्यपूर्वः; "
            "दर्शनीयपूर्वः, सुकुमारपूर्वः**. And the "
            "counter-example turns on how the compound is read: "
            "**परमश्चासौ पूर्वश्चेति समासः, न तु परमो भूतपूर्व "
            "इति**"),
    Purvapada(
        "6.2.23", samasa="tatpuruṣa",
        uttarapada=("savidha", "sanīḍa", "samaryāda", "saveśa",
                    "sadeśa"),
        result="sāmīpya",
        keeps_out="समर्यादं क्षेत्रम् — a field WITH a boundary, "
                  "which is the words read apart",
        why="सविधसनीडसमर्यादसवेशसदेशेषु सामीप्ये — before five words "
            "where NEARNESS is meant: **मद्रसविधम्, गान्धारिसनीडम्, "
            "काश्मीरसमर्यादम्**.\\n\\n"
            "**AND THE FIVE ARE NOT WHAT THEY LOOK LIKE.** "
            "**सविधादीनां सह विधयेत्येवमादिका व्युत्पत्तिरेव "
            "केवलम्। समीपवाचिनस्त्वेते समुदायाः** — the derivation "
            "*with a rule*, *with a nest* is made out and set "
            "aside; as wholes the five simply mean *near*"),
    Purvapada(
        "6.2.24", gana="vispaṣṭādi", uttarapada=("guṇavacana",),
        why="विस्पष्टादीनि गुणवचनेषु — a list of first members before "
            "any quality-word: **विस्पष्टकटुकम्, विचित्रकटुकम्, "
            "व्यक्तलवणम्**.\\n\\n"
            "**AND THE COMPOUND IS NOT A कर्मधारय.** "
            "**कटुकादिभिश्च शब्दैर्गुणवद् द्रव्यमभिधीयत "
            "इत्यसामानाधिकरण्यम्** — कटुक names the thing that has "
            "the quality while विस्पष्ट qualifies the quality "
            "itself, so the two do not refer to the same thing and "
            "2.1.4's सुप्सुपा is what joins them"),
    Purvapada(
        "6.2.25", samasa="karmadhāraya",
        uttarapada=("śra", "jya", "avama", "kan", "pāpavat"),
        result="bhāva",
        keeps_out="गमनशोभनम् — not one of the five; गमनश्रेयः as a "
                  "genitive compound — not a कर्मधारय",
        why="श्रज्यावमकन्पापवत्सु भावे कर्मधारये — before five, in a "
            "कर्मधारय, where the first member names an ACTION: "
            "**गमनश्रेष्ठम्, वचनज्येष्ठम्, गमनावमम्, गमनकनिष्ठम्, "
            "गमनपापिष्ठम्**.\\n\\n"
            "**AND NAMING THE SUBSTITUTES NAMES WHAT ENDS IN "
            "THEM.** श्र, ज्य and कन् are the आदेश of श्रेष्ठ etc. "
            "**श्रज्यकनामादेशानां ग्रहणमिति सामर्थ्यात् तद्वद् "
            "उत्तरपदं गृह्यते** — a substitute named in a rule "
            "reaches the word it stands inside"),
    Purvapada(
        "6.2.26", samasa="karmadhāraya", of=("kumāra",),
        why="कुमारश्च — कुमार as first member of a कर्मधारय: "
            "**कुमारश्रमणा, कुमारकुलटा, कुमारतापसी**.\\n\\n"
            "**AND THE COMMENTATORS DIVIDE ON HOW FAR IT REACHES.** "
            "**केचित् लक्षणप्रतिपदोक्तयोः प्रतिपदोक्तस्यैव ग्रहणम् "
            "इति परिभाषया कुमारः श्रमणादिभिः इत्यत्रैव समासे "
            "स्वरमेतमिच्छन्ति। केचित् पुनरविशेषेण सर्वत्रैव "
            "कर्मधारये** — some confine it to the compound 2.1.70 "
            "makes by name, others let it reach every कर्मधारय"),
    Purvapada(
        "6.2.27", keeps="ādi", samasa="karmadhāraya", of=("kumāra",),
        uttarapada=("pratyenas",),
        why="आदिः प्रत्येनसि — and before प्रत्येनस् it is the FIRST "
            "SYLLABLE of कुमार that takes the accent, not whatever "
            "accent the word had: **कुमारप्रत्येनाः**. The first "
            "rule of the pāda to place an accent rather than "
            "preserve one, and it stands thirty-seven sūtras before "
            "the heading that will make placing the ordinary "
            "case.\\n\\n"
            "**AND THE WORD उदात्त IS NOT IN THE RULE AT ALL.** "
            "**उदात्त इत्येतदत्र सामर्थ्याद् वेदितव्यम्। पूर्वपद"
            "प्रकृतिस्वर एव ह्ययमादेरुपदिश्यते** — it has to be "
            "supplied from the sense, since saying *the beginning* "
            "of an accent that is merely preserved says nothing"),
    Purvapada(
        "6.2.28", keeps="ādi", samasa="karmadhāraya", of=("kumāra",),
        uttarapada=("pūga",), optional=True,
        why="पूगेष्वन्यतरस्याम् — and before a word for a GUILD, "
            "optionally: **कुमारचातकाः, कुमारलोहध्वजाः, "
            "कुमारबलाहकाः, कुमारजीमूताः**, each in three "
            "accentuations.\\n\\n"
            "**AND THE THIRD ACCENTUATION DEPENDS ON HOW 6.2.26 WAS "
            "READ.** **अत्र यदाद्युदात्तत्वं न भवति, तदा कुमारश्च "
            "इति पूर्वपदप्रकृतिस्वरत्वम् एके कुर्वन्ति। ये तु तत्र "
            "प्रतिपदोक्तस्य ग्रहणमिच्छन्ति तेषां "
            "समासान्तोदात्तत्वमेव भवति** — the disagreement recorded "
            "at 6.2.26 shows up here as a difference in the "
            "forms"),
    Purvapada(
        "6.2.29", samasa="dvigu",
        uttarapada=("iganta", "kāla", "kapāla", "bhagāla", "śarāva"),
        why="इगन्तकालकपालभगालशरावेषु द्विगौ — in a द्विगु, before a "
            "second member ending in an इक्, or naming a time, or "
            "one of three vessels: **पञ्चारत्निः, दशारत्निः; "
            "पञ्चमास्यः, पञ्चवर्षः; पञ्चकपालः, पञ्चभगालः, "
            "पञ्चशरावः**"),
    Purvapada(
        "6.2.30", samasa="dvigu", of=("bahu",), optional=True,
        blocks=("6.2.29",),
        why="बह्वन्यतरस्याम् — and for बहु the rule before is a "
            "CHOICE: **बह्वरत्निः, बहुमास्यः, बहुकपालः** each "
            "beside its end-accented form. **पूर्वेण नित्ये प्राप्ते "
            "विकल्पः** — what was fixed is loosened"),
    Purvapada(
        "6.2.31", samasa="dvigu", uttarapada=("diṣṭi", "vitasti"),
        optional=True,
        why="दिष्टिवितस्त्योश्च — and before these two, optionally: "
            "**पञ्चदिष्टिः, पञ्चवितस्तिः**. Both are measures, so "
            "the मात्रच् drops here as it did at 6.2.29"),
    Purvapada(
        "6.2.32", case="saptamī",
        uttarapada=("siddha", "śuṣka", "pakva", "bandha"),
        excludes=("kāla",),
        why="सप्तमी सिद्धशुष्कपक्वबन्धेष्वकालात् — a locative first "
            "member before four words, and not where it names a "
            "TIME: **सांकाश्यसिद्धः, काम्पिल्यसिद्धः; ऊकशुष्कः, "
            "निधनशुष्कः; कुम्भीपक्वः, कलसीपक्वः, भ्राष्ट्रपक्वः; "
            "चक्रबन्धः, चारकबन्धः**"),
    Purvapada(
        "6.2.33", of=("pari", "prati", "upa", "apa"),
        result="varjyamāna",
        why="परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु — four preverbs "
            "as first member, before a word naming what is LEFT OUT "
            "or a part of a day or a night: **परित्रिगर्तं वृष्टो "
            "देवः; प्रतिपूर्वाह्णम्; उपपूर्वरात्रम्; अपसौवीरम्**. "
            "The preverbs are first-accented already by "
            "**उपसर्गाश्चाभिवर्जम्**.\\n\\n"
            "**AND THE RULE IS FOR THE अव्ययीभाव ALONE.** "
            "**तत्पुरुषे बहुव्रीहौ च सिद्धत्वाद् अव्ययीभावार्थोऽयम् "
            "आरम्भः** — in the other two compounds the accent came "
            "already, so this rule exists for the one where it did "
            "not. And only two of the four take the *left out* "
            "sense: **अपपरी वर्जने इति तयोरेव वर्ज्यमानम् "
            "उत्तरपदम्**"),
    Purvapada(
        "6.2.34", samasa="dvandva", result="andhaka-vṛṣṇi",
        keeps_out="द्वैप्यहैमायनाः — Andhakas and Vṛṣṇis, but not of "
                  "the anointed line; संकर्षणवासुदेवौ — a dual, not "
                  "a plural; वृष्णिकुमाराः — no द्वन्द्व",
        why="राजन्यबहुवचनद्वन्द्वेऽन्धकवृष्णिषु — in a द्वन्द्व of "
            "plural words for princes of the Andhaka and Vṛṣṇi "
            "houses: **श्वाफल्कचैत्रकाः, चैत्रकरोधकाः, "
            "शिनिवासुदेवाः**. And राजन्य is in the rule for a "
            "reason: **राजन्यग्रहणमिह अभिषिक्तवंश्यानां क्षत्रियाणां "
            "ग्रहणार्थम्** — of the anointed line, which the "
            "counter-example is not"),
    Purvapada(
        "6.2.35", samasa="dvandva", gana="saṅkhyā",
        why="संख्या — a numeral as first member of a द्वन्द्व: "
            "**एकादश, द्वादश, त्रयोदश**. एक is first-accented by a "
            "नित् उणादि affix, and the त्रयस् that stands for त्रि "
            "is laid down end-accented"),
    Purvapada(
        "6.2.36", samasa="dvandva", result="ācāryopasarjana-antevāsin",
        keeps_out="पाणिनीयदेवदत्तौ — only one member is a pupil "
                  "named from his teacher; छान्दसवैयाकरणाः — named "
                  "from a subject, not a teacher",
        why="आचार्योपसर्जनश्चान्तेवासी — in a द्वन्द्व of words for "
            "pupils named after their teachers: **आपिशलपाणिनीयाः, "
            "पाणिनीयरौढीयाः, रौढीयकाशकृत्स्नाः**.\\n\\n"
            "**AND THE CONDITION IS ON THE WHOLE COMPOUND, NOT ON "
            "ONE MEMBER.** **आचार्योपसर्जनग्रहणं द्वन्द्वविशेषणार्थम्, "
            "सकलो द्वन्द्व आचार्योपसर्जनो यथा विज्ञायेत** — which is "
            "what keeps पाणिनीयदेवदत्तौ out"),
    Purvapada(
        "6.2.37", samasa="dvandva", gana="kārtakaujapādi",
        why="कार्तकौजपादयश्च — a list of द्वन्द्व compounds whose "
            "first member keeps its accent: **कार्तकौजपौ, "
            "सावर्णिमाण्डूकेयौ, अवन्त्यश्मकाः, पैलश्यापर्णेयाः**. "
            "**विभक्त्यन्तानां पाठो वचनविवक्षार्थम्** — the members "
            "are listed with their endings on to show the number "
            "each is used in, and **बहुवचनमतन्त्रम्**, that number "
            "is not binding"),
    Purvapada(
        "6.2.38", of=("mahat",),
        uttarapada=("vrīhi", "aparāhṇa", "gṛṣṭi", "iṣvāsa", "jābāla",
                    "bhāra", "bhārata", "hailihila", "raurava",
                    "pravṛddha"),
        keeps_out="महद्व्रीहिः — the genitive compound, where the "
                  "accent stays at the end",
        why="महान् व्रीह्यपराह्णगृष्ट्येष्वासजाबालभारभारतहैलिहिल"
            "रौरवप्रवृद्धेषु — महत् before ten words: **महाव्रीहिः, "
            "महापराह्णः, महेष्वासः, महाभारतः, महाप्रवृद्धः**.\\n\\n"
            "**AND THE RULE REACHES ONLY THE COMPOUND 2.1.61 MAKES "
            "BY NAME.** **महच्छब्दस्य प्रतिपदोक्तो यः समासः "
            "सन्महत्परमोत्तमोत्कृष्टाः इति तत्रैव स्वरः** — so the "
            "genitive compound महतो व्रीहिः stays end-accented"),
    Purvapada(
        "6.2.39", of=("kṣullaka", "mahat"), uttarapada=("vaiśvadeva",),
        why="क्षुल्लकश्च वैश्वदेवे — क्षुल्लक, and महत् carrying down, "
            "before वैश्वदेव: **क्षुल्लकवैश्वदेवम्, "
            "महावैश्वदेवम्**"),
    Purvapada(
        "6.2.40", of=("uṣṭra",), uttarapada=("sādin", "vāmin"),
        why="उष्ट्रः सादिवाम्योः — उष्ट्र before these two: "
            "**उष्ट्रसादि, उष्ट्रवामि**. The compound is read either "
            "as a कर्मधारय or as a genitive one"),
    Purvapada(
        "6.2.41", of=("go",), uttarapada=("sāda", "sādi", "sārathi"),
        why="गौः सादसादिसारथिषु — गो before three: **गोसादः, "
            "गोसादिः, गोसारथिः**, and the first is read two ways — "
            "**गोः सादो** or **गां सादयति**"),
    Purvapada(
        "6.2.42", gana="dāsībhārādi",
        why="कुरुगार्हपतरिक्तगुर्वसूतजरत्यश्लीलदृढरूपापारेवडवा"
            "तैतिलकद्रूपण्यकम्बलो दासीभाराणां च — eight named "
            "compounds and the दासीभार list: **कुरुगार्हपतम्, "
            "रिक्तगुरुः, असूतजरती, अश्लीलदृढरूपा**. And a "
            "supplement adds one more first member: "
            "**कुरुवृज्योर्गार्हपत इति वक्तव्यम्** — "
            "**वृजिगार्हपतम्**.\\n\\n"
            "**AND ONE MEMBER CARRIES AN OPTION FROM ANOTHER "
            "PĀDA.** रिक्तगुरु is **रिक्तगुरुः** or **रिक्तगुरुः** — "
            "6.1.208's विभाषा on रिक्त reaching into the compound"),
    Purvapada(
        "6.2.43", case="caturthī", result="tadartha",
        keeps_out="कुबेरबलिः — an offering FOR Kubera, but Kubera is "
                  "not what it is made of",
        why="चतुर्थी तदर्थे — a dative first member before a word "
            "naming what is made FOR it: **यूपदारु** — wood for a "
            "sacrificial post; **कुण्डलहिरण्यम्, रथदारु, "
            "वल्लीहिरण्यम्**.\\n\\n"
            "**AND THE RELATION HAS TO BE ONE OF MATERIAL.** "
            "**प्रकृतिविकारभावे स्वरोऽयमिष्यते** — the second member "
            "must be what the first is MADE OF, not merely what it "
            "is meant for"),
    Purvapada(
        "6.2.44", case="caturthī", uttarapada=("artha",),
        why="अर्थे — and before the word अर्थ itself: **मात्रर्थम्, "
            "पित्रर्थम्, देवतार्थम्, अतिथ्यर्थम्**. The rule before "
            "reached only particular materials — दारु, हिरण्य — and "
            "not the general word.\\n\\n"
            "**AND SOME READ IT AS A ज्ञापक INSTEAD.** "
            "**केचित् पुनराहुः — ज्ञापकार्थमिदम्। एतदनेन ज्ञाप्यते "
            "— पूर्वो विधिः प्रकृतिविकृत्योः समासे भवति** — that "
            "6.2.43 holds only of a material and its product, which "
            "is why **अश्वघासः** and **श्वश्रूसुरम्** do not take "
            "it though the *for* relation is there"),
    Purvapada(
        "6.2.45", case="caturthī", uttarapada_affix="kta",
        why="क्ते च — and before a क्त participle: **गोहितम्, "
            "अश्वहितम्, मनुष्यहितम्; गोरक्षितम्, अश्वरक्षितम्, "
            "तापसरक्षितम्**, with the dative of the person the thing "
            "is for"),
    Purvapada(
        "6.2.46", samasa="karmadhāraya", uttarapada_affix="kta",
        excludes=("niṣṭhā",),
        keeps_out="श्रेण्या कृतम् — an instrumental compound; "
                  "कृताकृतम् — the first member is itself a निष्ठा",
        why="कर्मधारयेऽनिष्ठा — in a कर्मधारय before a क्त "
            "participle, where the first member is NOT itself one: "
            "**श्रेणिकृताः, ऊककृताः, पूगकृताः, निधनकृताः**"),
    Purvapada(
        "6.2.47", case="dvitīyā", uttarapada_affix="kta",
        result="ahīna", blocks=("6.2.144",),
        keeps_out="कान्तारातीतः, योजनातीतः — the sense is falling "
                  "short; सुखप्राप्तः, दुःखापन्नः — a preverb stands "
                  "before the participle",
        why="अहीने द्वितीया — an accusative first member before a "
            "क्त participle, where nothing is FALLEN SHORT OF: "
            "**कष्टश्रितः, त्रिशकलपतितः, ग्रामगतः**. And a "
            "supplement adds a condition: "
            "**द्वितीयानुपसर्ग इति वक्तव्यम्**. "
            "**अन्तः थाथ० इत्यस्यापवादोऽयम्** — an exception to "
            "6.2.144"),
    Purvapada(
        "6.2.48", case="tṛtīyā", uttarapada_affix="kta",
        result="karman",
        keeps_out="रथेन यातो रथयातः — the participle is agentive "
                  "there, the root being one of motion",
        why="तृतीया कर्मणि — an instrumental first member before a "
            "क्त participle used in the OBJECT sense: **अहिहतः, "
            "वज्रहतः, महाराजहतः, नखनिर्भिन्ना, दात्रलूना**"),
    Purvapada(
        "6.2.49", of=("gati",), uttarapada_affix="kta",
        result="karman", blocks=("6.2.144",),
        keeps_out="अभ्युद्धृतः, समुद्धृतः, समुदाहृतः — the गति is "
                  "not next to the participle; प्रकृतः कटं देवदत्तः "
                  "— the sense is agentive",
        why="गतिरनन्तरः — a गति standing IMMEDIATELY before a क्त "
            "participle used in the object sense: **प्रकृतः, "
            "प्रहृतः**. **थाथादिस्वरापवादो योगः**.\\n\\n"
            "**AND अनन्तरः IS WHAT KEEPS A MAXIM OUT.** "
            "**अनन्तरग्रहणसामर्थ्यादेव कृद्ग्रहणे "
            "गतिकारकपूर्वस्यापि इत्येतद् नाश्रीयते** — the word "
            "would be idle if that maxim applied, so its being "
            "there is what shows it does not"),
    Purvapada(
        "6.2.50", of=("gati",), uttarapada_affix="ta-ādi-nit-kṛt",
        excludes=("tu",),
        keeps_out="प्रजल्पाकः — the affix does not begin with त्; "
                  "प्रकर्ता with तृच् — not नित्; आगन्तुः — the "
                  "affix is तु, which the rule excepts",
        why="तादौ च निति कृत्यतौ — and before a कृत् affix beginning "
            "with त् and marked न्, तु excepted: **प्रकर्ता** with "
            "तृन्, **प्रकर्तुम्, प्रकृतिः**. **कृत्स्वरबाधनार्थं "
            "वचनम्** — stated to displace the affix's own accent"),
    Purvapada(
        "6.2.51", keeps="ādi-anta", of=("gati",),
        uttarapada=("tavai",), blocks=("6.1.158",),
        why="तवै चान्तश्च युगपत् — the तवै takes the accent at its "
            "END and the गति keeps its own at the same time: "
            "**अन्वेतवै, परिस्तरितवै, परिपातवै; तस्मात् पिता "
            "नाभिचरितवै**.\\n\\n"
            "**AND THIS IS THE SECOND RULE OF THE BOOK TO PUT TWO "
            "ACCENTS AT ONCE.** 6.1.200 was the first, and both say "
            "युगपत् for the same reason — 6.1.158 allows a word one "
            "accent, so without the word the two would be "
            "alternatives. **कृत्स्वरापवादो योगः**"),
    Purvapada(
        "6.2.52", of=("gati",), uttarapada=("añc",),
        uttarapada_affix="va-pratyaya", excludes=("iganta",),
        keeps_out="प्रत्यङ्, प्रत्यञ्चौ — the गति ends in an इक्, and "
                  "6.2.139's accent takes it; उदञ्चनः — the affix is "
                  "not the वि",
        why="अनिगन्तोऽञ्चतौ वप्रत्यये — a गति not ending in an इक्, "
            "before अञ्च् with the affix वि: **प्राङ्, प्राञ्चौ, "
            "प्राञ्चः; पराङ्, पराञ्चः**. And the single substitute "
            "is उदात्त or स्वरित by 8.2.6.\\n\\n"
            "**AND ONE FORM IS SETTLED BY विप्रतिषेध.** "
            "**चोरनिगन्तोऽञ्चतौ वप्रत्यय इत्येष स्वरो भवति "
            "विप्रतिषेधेन** — **पराचः, पराचा**"),
    Purvapada(
        "6.2.53", of=("ni", "adhi"), uttarapada=("añc",),
        uttarapada_affix="va-pratyaya", blocks=("6.2.52",),
        why="न्यधी च — and these two, which DO end in an इक् and so "
            "were kept out by the rule before: **न्यङ्, न्यञ्चौ; "
            "अध्यङ्, अध्यञ्चः, अधीचः**. 8.2.4 then makes the अ of "
            "अञ्च् स्वरित"),
    Purvapada(
        "6.2.54", of=("īṣad",), optional=True,
        keeps_out="ईषद्भेदः — there the कृत् affix's own accent "
                  "stands",
        why="ईषदन्यतरस्याम् — ईषद् optionally keeps its accent: "
            "**ईषत्कडारः, ईषत्पिङ्गलः**, each beside its "
            "end-accented form. And the rule reaches no further than "
            "that: **ईषद्भेद इत्येवमादाै कृत्स्वर एव भवति** "
            "— where the second member is a कृत् stem, that affix's "
            "own accent stands and the option never arises"),
    Purvapada(
        "6.2.55", of=("hiraṇyaparimāṇa",), uttarapada=("dhana",),
        optional=True,
        keeps_out="प्रस्थधनम् — no gold; काञ्चनधनम् — gold but no "
                  "measure of it; निष्कमाला — not धन",
        why="हिरण्यपरिमाणं धने — a first member naming a WEIGHT OF "
            "GOLD, before धन, optionally: **द्विसुवर्णधनम्** beside "
            "the end-accented form. And the option reaches the "
            "बहुव्रीहि too, **परत्वाद्**"),
    Purvapada(
        "6.2.56", of=("prathama",), result="acira-upasampatti",
        optional=True,
        keeps_out="प्रथमवैयाकरणः meaning the foremost grammarian — "
                  "always end-accented",
        why="प्रथमोऽचिरोपसंपत्तौ — प्रथम optionally, where NEWNESS is "
            "meant, which the vṛtti glosses "
            "**अचिरोपश्लेषोऽभिनवत्वम्**: **प्रथमवैयाकरणः** — one who "
            "has just begun grammar, beside the same form meaning "
            "the foremost grammarian, which never takes it"),
    Purvapada(
        "6.2.57", of=("katara", "katama"), samasa="karmadhāraya",
        optional=True,
        why="कतरकतमौ कर्मधारये — these two optionally in a "
            "कर्मधारय: **कतरकठः, कतमकठः**, each beside the "
            "end-accented form. **कर्मधारयग्रहणमुत्तरार्थम्** — the "
            "word is put in for the rules that follow, since here "
            "the compound could only be one"),
    Purvapada(
        "6.2.58", of=("ārya",), uttarapada=("brāhmaṇa", "kumāra"),
        samasa="karmadhāraya", optional=True,
        keeps_out="आर्यक्षत्रियः — not one of the two; आर्यस्य "
                  "ब्राह्मणः — a genitive compound",
        why="आर्यो ब्राह्मणकुमारयोः — आर्य optionally before these "
            "two in a कर्मधारय: **आर्यब्राह्मणः, आर्यकुमारः**"),
    Purvapada(
        "6.2.59", of=("rājan",), uttarapada=("brāhmaṇa", "kumāra"),
        samasa="karmadhāraya", optional=True,
        why="राजा च — and राजन् likewise: **राजब्राह्मणः, "
            "राजकुमारः**. **पृथग्योगकरणमुत्तरार्थम्** — split off "
            "from the rule before so that राजन् alone carries into "
            "the next"),
    Purvapada(
        "6.2.60", of=("rājan",), case="ṣaṣṭhī",
        uttarapada=("pratyenas",), optional=True,
        keeps_out="राजा चासौ प्रत्येनाश्च — the कर्मधारय, not the "
                  "genitive compound",
        why="षष्ठी प्रत्येनसि — राजन् in the GENITIVE before "
            "प्रत्येनस्, optionally: **राजप्रत्येनाः** beside the "
            "end-accented form"),
    Purvapada(
        "6.2.61", uttarapada_affix="kta", result="nityārtha",
        optional=True,
        keeps_out="मुहूर्तप्रहसितः — for a moment, not always",
        why="क्ते नित्यार्थे — before a क्त participle where the "
            "compound means ALWAYS, optionally: **नित्यप्रहसितः, "
            "सततप्रहसितः**, each beside its end-accented form"),
    Purvapada(
        "6.2.62", of=("grāma",), result="śilpin", optional=True,
        keeps_out="परमनापितः — not ग्राम; ग्रामरथ्या — not a "
                  "craftsman",
        why="ग्रामः शिल्पिनि — ग्राम before a word for a CRAFTSMAN, "
            "optionally: **ग्रामनापितः, ग्रामकुलालः** — the "
            "village's barber, the village's potter"),
    Purvapada(
        "6.2.63", of=("rājan",), result="śilpin-praśaṃsā",
        optional=True,
        keeps_out="राजनापितः without praise; राजहस्ती — not a "
                  "craftsman",
        why="राजा च प्रशंसायाम् — and राजन् before a craftsman-word "
            "where PRAISE is meant, optionally: **राजनापितः, "
            "राजकुलालः**.\\n\\n"
            "**AND THE PRAISE IS READ TWO WAYS ACCORDING TO THE "
            "COMPOUND.** **कर्मधारये राजगुणाध्यारोपेण उत्तरपदार्थस्य "
            "प्रशंसा। षष्ठीसमासे च राजयोग्यतया तस्य** — in the one "
            "the craftsman is praised by having a king's qualities "
            "put on him, in the other by being fit for a king"),
)


@dataclass(frozen=True)
class Kept:
    """What the resolver answers with."""

    keeps: str
    sutra: str
    why: str
    optional: bool = False
    #: Where a rule displaces or refuses another, that rule's number.
    blocked_by: Tuple[str, ...] = ()


def _reaches(row: Purvapada, purvapada: str, gana: str, kind: str,
             uttarapada: str, uttarapada_affix: str, samasa: str,
             case: str, result: str) -> bool:
    # 6.2.1 is both the heading and a rule: it states बहुव्रीहि and
    # is answered like any other row, so nothing is excluded here.
    if row.of and purvapada not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.kinds and kind not in row.kinds:
        return False
    if row.uttarapada and uttarapada not in row.uttarapada:
        return False
    if row.uttarapada_affix and uttarapada_affix != row.uttarapada_affix:
        return False
    if row.samasa and samasa != row.samasa:
        return False
    if row.case and case != row.case:
        return False
    if row.result and result != row.result:
        return False
    if row.excludes and (purvapada in row.excludes
                         or uttarapada in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Purvapada, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.keeps and not row.refuses


def _how_specific(row: Purvapada) -> int:
    """
    A refusal beats what it refuses, and a named second member beats
    everything else.

    The second member counts highest of the conditions because this
    section is arranged by it: sixty-three rules and almost every one
    names the word that must FOLLOW. The sense comes next, since it
    is what most often separates two rules that name the same word —
    6.2.15 and 6.2.16 name सुख and प्रिय both.
    """
    return (
        10 * bool(row.refuses)
        + 8 * bool(row.uttarapada)
        + 7 * bool(row.result)
        + 6 * bool(row.of)
        + 5 * bool(row.uttarapada_affix)
        + 4 * bool(row.case)
        + 3 * bool(row.kinds)
        + 2 * bool(row.samasa)
        + 2 * bool(row.gana)
    )


def first_member(purvapada: str = "", *, gana: str = "",
                 kind: str = "", uttarapada: str = "",
                 uttarapada_affix: str = "", samasa: str = "",
                 case: str = "", result: str = "",
                 wants: str = "") -> Kept:
    """
    6.2.1–63 — whether the first member of a compound keeps its own
    accent, and by which rule.

    Nothing answers by default, and that is the point: where no rule
    of the section is reached, 6.1.223 stands and the accent is at
    the end of the compound.
    """
    matched = [
        row for row in PURVAPADA_TABLE
        if _reaches(row, purvapada, gana, kind, uttarapada,
                    uttarapada_affix, samasa, case, result)
        and _supplies(row, wants)
    ]
    if not matched:
        return Kept(
            "", "", "No rule of 6.2.1–63 is reached, so 6.1.223 "
                    "समासस्य stands and the accent is at the end of "
                    "the compound")
    row = max(matched, key=_how_specific)
    return Kept("" if row.refuses else row.keeps, row.sutra, row.why,
                optional=row.optional, blocked_by=row.blocks)


def prakrtya_run() -> Kept:
    """
    How far प्रकृत्या governs, and how far पूर्वपद governs past it.

    6.2.64's आदिरुदात्तः takes over the placement while पूर्वपद keeps
    running to 6.2.110, where 6.2.111's उत्तरपदादिः takes the rest of
    the pāda: **प्राग् उत्तरपदादिः इत्येतस्माद् अयम् अधिकारो
    वेदितव्यः**.
    """
    opens, closes = PRAKRTYA_RUN
    return Kept(
        "prakṛti", opens,
        "प्रकृत्या governs from %s to %s, and पूर्वपदम् runs on to "
        "%s — two words of one sūtra with two different reaches. "
        "And the whole of it is an exception to 6.1.223: %s"
        % (opens, closes, PURVAPADA_RUN[1], WHAT_IT_EXCEPTS))


def provisions_for(sutra_id: str) -> Tuple[Purvapada, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in PURVAPADA_TABLE
                 if row.sutra == sutra_id)
