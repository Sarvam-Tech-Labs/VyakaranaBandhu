# -*- coding: utf-8 -*-
"""
७.१.५८–८३ — नुम्, the nasal put inside a stem.

Twenty-six sūtras about one augment. नुम् goes in before the last
vowel of what it is attached to, so कुडि is कुण्डिता, मुच् is
मुञ्चति, भवत् is भवान्, यशस् is यशांसि. It is the commonest
augment in the book and the one that makes a Sanskrit stem look
the way it does in the strong cases.

**IT IS SUPPLIED FOR FOUR DIFFERENT REASONS.** For a root marked
with इ in the धातुपाठ (7.1.58) — कुण्डिता; for particular roots
before particular affixes (7.1.59–69) — मुञ्चति, मङ्क्ता, रन्धयति,
लम्भयति; for a stem before a सर्वनामस्थान (7.1.70–72) — भवान्,
प्राङ्, यशांसि; and for a neuter इक्-final stem before a
vowel-initial ending (7.1.73) — त्रपुणी.

**AND THREE SŪTRAS IN THE MIDDLE ARE NOT ABOUT नुम् AT ALL.**
7.1.75–77 give अस्थि, दधि, सक्थि and अक्षि an अनङ् — अस्थ्ना,
दध्ने, अक्ष्णा — and a Vedic ई besides. They stand here because
they are about the same stems in the same environment, and because
7.1.77's अक्षी beats the नुम् that 7.1.73 would have given.

**AND ONE SŪTRA NAMES A GRAMMARIAN AND DISAGREES WITH HIM.**
7.1.74 gives Gālava's view — that a भाषितपुंस्क neuter behaves as
a masculine in the oblique cases, so ग्रामण्या beside ग्रामणिना —
and Pāṇini records it as an option rather than adopting it.

**WHAT THIS MODULE DOES NOT DO.** It says where the नुम् goes in.
Where inside the stem it lands is 1.1.47's, and what the nasal
then becomes is 8.3's and 8.4's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
NUM_RUN: Tuple[str, str] = ("7.1.58", "7.1.83")

#: 7.1.59's eight, which take नुम् before श: मुञ्चति, लुम्पति,
#: विन्दति, लिम्पति, सिञ्चति, कृन्तति, खिन्दति, पिंशति.
MUCADI: Tuple[str, ...] = (
    "muc", "lup", "vid", "lip", "sic", "kṛt", "khid", "piś")

#: And the vārttika's five more, each with a nasal already lost by
#: 6.4.24 and put back here: तृम्फति, दृम्फति, गुम्फति, उम्भति,
#: शुम्भति.
TRMPHADI: Tuple[str, ...] = (
    "tṛmph", "dṛmph", "gumph", "umbh", "śumbh")

#: 7.1.61–69's roots, each with its own condition.
RADHI_JABHI: Tuple[str, ...] = ("radh", "jabh")

#: 7.1.75's four neuters, which take अनङ् and not नुम्.
ASTHYADI: Tuple[str, ...] = ("asthi", "dadhi", "sakthi", "akṣi")

#: 7.1.78–81's four reduplicated stems, where the शतृ's नुम् is
#: refused or made optional: ददत्, दधत्, जक्षत्, जाग्रत्. The
#: same four 7.1.4 names for its झ-substitute, so they are asked
#: for rather than written out again.
from src.astadhyayi.pratyaya_adesa import (  # noqa: E402
    ABHYASTA_FOUR)

#: 7.1.83's three, which take नुम् before सु in the Veda.
DRK_THREE: Tuple[str, ...] = ("dṛk", "svavas", "svatavas")

#: 7.1.74's own words for the view it records — Gālava's, given
#: as an option and not adopted.
GALAVA: str = "gālavasya ācāryasya matena"


@dataclass(frozen=True)
class Num:
    """One rule of 7.1.58–83: नुम्, or what stands in its place."""

    sutra: str
    #: `num` for the augment; `anaṅ`, `ī`, `puṃvat` where the
    #: rule supplies something else.
    does: str = "num"
    #: The roots or stems named outright.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: A further condition: the gender, the preverb, the sense.
    upasarga: str = ""
    gender: str = ""
    sense: str = ""
    refuses: bool = False
    optional: bool = False
    nitya: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NUM_TABLE: Tuple[Num, ...] = (
    Num(
        "7.1.58", gana="idit-dhātu",
        keeps_out="पचति, पठति — no इ in the धातुपाठ's reading; "
                  "भेत्ता, छेत्ता — an इर् and not an इ, and "
                  "इरितां समुदायस्य",
        why="इदितो नुम् धातोः — a root taught with an इ takes "
            "नुम्: **कुडि — कुण्डिता, कुण्डितुम्, कुण्डा; हुडि — "
            "हुण्डिता, हुण्डा**.\\n\\n"
            "**AND IT GOES IN WHILE THE ROOT IS STILL BEING "
            "TAUGHT.** **अयं धातूपदेशावस्थायाम् एव नुमागमो "
            "भवति** — not when the word is built, and the vṛtti "
            "gives two proofs. कुण्डा needs 3.3.103's अ, which "
            "wants a heavy penult that only the नुम् supplies; "
            "and 3.1.80's **धिन्विकृण्व्योर च** complains of "
            "roots *with their nasal already attached*, which "
            "they could not be if the नुम् came later.\\n\\n"
            "**AND THE इ OF तासि AND सिच् IS NOT THIS इ.** "
            "**तासिसिचोरिदित्कार्यं नास्तीत्युच्चारणार्थो "
            "निरनुनासिक इकारः पठ्यते** — theirs is there to "
            "pronounce the root by, and is not nasal"),
    Num(
        "7.1.59", of=MUCADI, before=("śa",),
        keeps_out="मोक्ता, मोक्तुम् — no श; तुदति, नुदति — not "
                  "one of the eight",
        why="शे मुचादीनाम् — eight roots take नुम् before श: "
            "**मुञ्चति, लुम्पति, विन्दति, लिम्पति, सिञ्चति, "
            "कृन्तति, खिन्दति, पिंशति**.\\n\\n"
            "**AND A VĀRTTIKA ADDS FIVE MORE THAT HAD ALREADY "
            "LOST A NASAL.** **शे तृम्फादीनाम् उपसंख्यानं "
            "कर्तव्यम्** — तृम्फ, दृम्फ, गुम्फ, उम्भ, शुम्भ are "
            "read in the धातुपाठ WITH a nasal, 6.4.24 takes it "
            "out, and this rule puts one back: **तृम्फति, "
            "गुम्फति, शुम्भति**. And having been supplied on "
            "purpose it cannot be taken out again — **स च "
            "विधानसामर्थ्याद् न लुप्यते**. The roots read without "
            "the nasal give तृफति, गुफति, शुभति"),
    Num(
        "7.1.60", of=("masj", "naś"), before=("jhal",),
        keeps_out="मज्जनम्, नशनम् — the affix does not begin with "
                  "a झल्",
        why="मस्जिनशोर्झलि — मस्ज् and नश् take नुम् before a "
            "झल्-initial affix: **मङ्क्ता, मङ्क्तुम्; नंष्टा, "
            "नंष्टुम्**.\\n\\n"
            "**AND FOR मस्ज् THE नुम् DOES NOT GO WHERE 1.1.47 "
            "WOULD PUT IT.** **मस्जेरन्त्यात् पूर्वं नुमम् "
            "इच्छन्त्यनुषङ्गादिलोपार्थम्** — before the LAST "
            "sound and not before the last vowel, so that the "
            "cluster may then simplify: **मग्नः, मग्नवान्**"),
    Num(
        "7.1.61", of=RADHI_JABHI, before=("ac",),
        keeps_out="रद्धा, जभ्यम् — a consonant-initial affix",
        why="रधिजभोरचि — रध् and जभ् take नुम् before a "
            "vowel-initial affix: **रन्धयति, रन्धकः, "
            "साधुरन्धी; जम्भयति, जम्भकः**. And the नुम् beats "
            "the vṛddhi that would otherwise have come, though "
            "the vṛddhi is later — **परापि सती वृद्धिर् नुमा "
            "बाध्यते, नित्यत्वात्**"),
    Num(
        "7.1.62", refuses=True, of=("radh",), before=("iṭ",),
        not_before=("liṭ",), blocks=("7.1.61",),
        keeps_out="रन्धनम्, रन्धकः — no इट्; ररन्धिव, ररन्धिम — "
                  "the perfect, where the refusal lapses",
        why="नेट्यलिटि रधेः — but रध् does NOT take it before an "
            "इट्-initial affix that is not the perfect: "
            "**रधिता, रधितुम्, रधितव्यम्**.\\n\\n"
            "**AND IT IS PUT AS A REFUSAL RATHER THAN AS A "
            "RESTRICTION FOR A REASON.** **अथ क्वसौ कथं "
            "भवितव्यम्?** — रेधिवान् is built by doing the "
            "एत्व and the reduplication-loss first, then the "
            "इट्, then the नुम्. And a नियम was possible — "
            "*only before an इट् in the perfect* — but "
            "**विपरीतमप्यवधारणं संभाव्येत**, it could be read "
            "backwards, and then रधिता would keep its nasal"),
    Num(
        "7.1.63", of=("rabh",), before=("ac",),
        not_before=("śap", "liṭ"),
        keeps_out="आरभते, आरेभे — शप् and the perfect; आरब्धा — "
                  "a consonant-initial affix",
        why="रभेरशब्लिटोः — रभ् takes नुम् before a vowel-initial "
            "affix that is neither शप् nor the perfect: "
            "**आरम्भयति, आरम्भकः, साध्वारम्भी, आरम्भो वर्तते**"),
    Num(
        "7.1.64", of=("labh",), before=("ac",),
        not_before=("śap", "liṭ"),
        keeps_out="लभते, लेभे, लब्धा — the same three exclusions",
        why="लभेश्च — and so does लभ्: **लम्भयति, लम्भकः, "
            "साधुलम्भी, लम्भो वर्तते**. It is given a sūtra of "
            "its own rather than joined to the one before, and "
            "the vṛtti says why in three words — **लभेश्च "
            "पृथग्योगकरणम् उत्तरार्थम्**, so that the five rules "
            "after it may carry लभ् alone"),
    Num(
        "7.1.65", of=("labh",), upasarga="āṅ", before=("ya-ādi",),
        keeps_out="लभ्यम् — no आङ्",
        why="आङो यि — after आङ् the लभ् takes नुम् before a "
            "य-initial affix: **आलम्भ्या गौः, आलम्भ्या वडवा**. "
            "And the accent follows from which affix it is: the "
            "नुम् goes in FIRST, so the root no longer has an अ "
            "in its penult, so 3.1.124's ण्यत् applies and not "
            "यत्, and the word is स्वरित at the end by 6.2.139 "
            "and 6.1.185"),
    Num(
        "7.1.66", of=("labh",), upasarga="upa", before=("ya-ādi",),
        sense="praśaṃsā",
        keeps_out="उपलभ्यम् अस्माद् वृषलात् किंचित् — no praise, "
                  "and 3.1.98's यत् gives a different word",
        why="उपात् प्रशंसायाम् — and after उप where PRAISE is "
            "meant: **उपलम्भ्या भवता विद्या; उपलम्भ्यानि "
            "धनानि**"),
    Num(
        "7.1.67", of=("labh",), upasarga="upasarga",
        before=("khal", "ghañ"),
        keeps_out="ईषल्लभः, लाभो वर्तते — no preverb at all",
        why="उपसर्गात् खल्घञोः — and after ANY preverb before खल् "
            "and घञ्: **ईषत्प्रलम्भः, सुप्रलम्भः; प्रलम्भः, "
            "विप्रलम्भः**. **सिद्धे सत्यारम्भो नियमार्थः** — "
            "7.1.64 had already supplied the नुम्, so this sūtra "
            "can only be fencing it: after a preverb and NOT "
            "otherwise"),
    Num(
        "7.1.68", refuses=True, of=("labh",),
        upasarga="su-dur-kevala", before=("khal", "ghañ"),
        blocks=("7.1.67",),
        keeps_out="सुप्रलम्भः, दुष्प्रलम्भः — another preverb "
                  "stands with them, so they are not केवल",
        why="न सुदुर्भ्यां केवलाभ्याम् — but not after सु and "
            "दुर् ALONE: **सुलभम्, दुर्लभम्; सुलाभः, "
            "दुर्लाभः**.\\n\\n"
            "**AND केवल IS THERE BECAUSE OF HOW THE CASE IS "
            "READ.** **सुदुर्भ्यामिति तृतीयां मत्वा केवलग्रहणं "
            "क्रियते। पञ्चम्यां हि व्यवहितत्वाद् एवाप्रसङ्गः** — "
            "read as an ablative the word would have been "
            "unnecessary. And अतिसुलभम् keeps the refusal only "
            "while अति is a कर्मप्रवचनीय; when it is a preverb "
            "the नुम् comes back — **अतिसुलम्भः**"),
    Num(
        "7.1.69", of=("labh",), before=("ciṇ", "ṇamul"),
        optional=True,
        why="विभाषा चिण्णमुलोः — before चिण् and णमुल् the नुम् "
            "is optional: **अलाभि, अलम्भि; लाभंलाभम्, "
            "लम्भंलम्भम्**. And the option is a व्यवस्थित one — "
            "**तेनानुपसृष्टस्य विकल्पः, उपसृष्टस्य नित्यं नुम् "
            "भवति। प्रालम्भि, प्रलम्भंप्रलम्भम्** — free only "
            "where there is no preverb"),
    Num(
        "7.1.70", gana="ugit-añcati", before=("sarvanāmasthāna",),
        not_before=("dhātu",),
        keeps_out="दृषद्, दृषदौ — no उगित्; भवतः, श्रेयसः — no "
                  "सर्वनामस्थान; उखास्रत्, पर्णध्वत् — a root "
                  "other than अञ्चति",
        why="उगिदचां सर्वनामस्थानेऽधातोः — a stem with उ, ऋ or ऌ "
            "for its marker, and अञ्चति, take नुम् before a "
            "सर्वनामस्थान: **भवान्, भवन्तौ, भवन्तः; श्रेयान्, "
            "श्रेयांसौ; पचन्, पचन्तौ; प्राङ्, प्राञ्चौ**. This "
            "is the rule that gives the strong cases their "
            "shape.\\n\\n"
            "**AND अधातोः IS THERE TO LET A FORMER ROOT BACK "
            "IN.** **अधातोरिति किम्? अधातुभूतपूर्वस्यापि यथा "
            "स्यात्। गोमन्तम् इच्छति गोमत्यति, गोमत्यतेरप्रत्ययो "
            "गोमान्** — गोमत् has been made a root and then "
            "un-made, and without the word it would have been "
            "shut out for what it briefly was"),
    Num(
        "7.1.71", of=("yuj",), before=("sarvanāmasthāna",),
        not_before=("samāsa",),
        keeps_out="अश्वयुक्, अश्वयुजौ — in a compound; युजम् "
                  "आपन्ना ऋषयः — युज् *concentration*, which is "
                  "not the root named",
        why="युजेरसमासे — युज् takes नुम् before a सर्वनामस्थान "
            "where it is NOT in a compound: **युङ्, युञ्जौ, "
            "युञ्जः**. And the root is named with an इ — "
            "**युजेरितीकारनिर्देशाद् युज समाधौ इत्यस्य ग्रहणं न "
            "भवति** — so the other युज् is out"),
    Num(
        "7.1.72", gender="napuṃsaka", gana="jhal-ac-anta",
        before=("sarvanāmasthāna",), blocks=("7.1.70",),
        keeps_out="अग्निचिद् ब्राह्मणः — not neuter; बहुपुरि, "
                  "चत्वारि, अहानि — neuter, but ending in "
                  "neither a झल् nor a vowel",
        why="नपुंसकस्य झलचः — a NEUTER stem ending in a झल् or in "
            "a vowel takes नुम् before a सर्वनामस्थान: "
            "**उदश्विन्ति, शकृन्ति, यशांसि, पयांसि; कुण्डानि, "
            "वनानि, त्रपूणि, जतूनि**. Where a stem is both "
            "उगित् and झल्-final this rule wins for being later "
            "— **परत्वाद् अनेनैव नुम् भवति। श्रेयांसि, "
            "भूयांसि**. A vārttika takes one word out: "
            "**बहूर्जि प्रतिषेधो वक्तव्यः**"),
    Num(
        "7.1.73", gender="napuṃsaka", gana="ik-anta",
        before=("ac-ādi-vibhakti",),
        keeps_out="कुण्डे, पीठे — the stem does not end in an "
                  "इक्; तौम्बुरवं चूर्णम् — a taddhita and no "
                  "case ending",
        why="इकोऽचि विभक्तौ — a neuter stem ending in इ, उ, ऋ or "
            "ऌ takes नुम् before a VOWEL-INITIAL case ending: "
            "**त्रपुणी, जतुनी, तुम्बुरुणी; त्रपुणे, जतुने**.\\n\\n"
            "**AND THE WORD अचि IS A ज्ञापक ABOUT SOMETHING "
            "ELSE.** The vṛtti asks why it is there, since the "
            "next sūtra says it anyway, and answers: **हे त्रपो "
            "इत्यत्र नुम् मा भूत्** — the vocative has its "
            "ending elided, and 1.1.63 should have stopped the "
            "rule reaching at all. That it has to be stopped by "
            "hand shows the prohibition does not hold here — "
            "**एतद् एवाज्ग्रहणं ज्ञापकं प्रत्ययलक्षणप्रतिषेधोऽत्र "
            "न भवतीति**"),
    Num(
        "7.1.74", does="puṃvat", gender="napuṃsaka",
        gana="bhāṣitapuṃska-ik-anta",
        before=("tṛtīyā-ādi-ac",), optional=True,
        blocks=("7.1.73",),
        why="तृतीयादिषु भाषितपुंस्कं पुंवद्गालवस्य — in the "
            "instrumental and after, a neuter stem that also has "
            "a masculine behaves AS a masculine, in Gālava's "
            "view: **ग्रामण्या ब्राह्मणकुलेन** beside "
            "**ग्रामणिना ब्राह्मणकुलेन**; **ग्रामण्ये** beside "
            "**ग्रामणिने**.\\n\\n"
            "**AND WHAT IT BUYS IS THAT TWO RULES DO NOT "
            "APPLY.** **यथा पुंसि ह्रस्वनुमौ न भवतः, तद्वद् "
            "अत्रापि न भवतः** — no shortening and no नुम्. The "
            "sūtra names the teacher, which is Pāṇini's way of "
            "recording a view as an option rather than adopting "
            "it. In the genitive plural the नुट् wins by "
            "पूर्वविप्रतिषेध — **ग्रामणीनां ब्राह्मणकुलानाम्**"),
    Num(
        "7.1.75", does="anaṅ", of=ASTHYADI, gender="napuṃsaka",
        before=("tṛtīyā-ādi-ac",), blocks=("7.1.73",),
        keeps_out="अस्थिनी, दधिनी — the dual, which is not "
                  "तृतीयादि; अस्थिभ्याम्, दधिभ्याम् — a "
                  "consonant-initial ending",
        why="अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः — अस्थि, दधि, सक्थि "
            "and अक्षि take अनङ् instead, and it is UDĀTTA: "
            "**अस्थ्ना, अस्थ्ने; दध्ना, दध्ने; सक्थ्ना; अक्ष्णा, "
            "अक्ष्णे**.\\n\\n"
            "**AND THE ACCENT IS PART OF THE RULE.** "
            "**अस्थ्यादय आद्युदात्ताः, तेषाम् अनङादेशः "
            "स्थानिवद्भावाद् अनुदात्तः स्याद् इत्युदात्तवचनम्** "
            "— by 1.1.56 the substitute would have inherited the "
            "toneless quality of what it replaced. With the "
            "accent stated, 6.4.134's अ-loss then throws it onto "
            "the ending by 6.1.161. And the four reach a "
            "compound ending in them: **प्रियास्थ्ना ब्राह्मणेन**"),
    Num(
        "7.1.76", does="anaṅ", of=ASTHYADI, chandasi=True,
        blocks=("7.1.75",),
        why="छन्दस्यपि दृश्यते — and in the Veda the अनङ् is seen "
            "where none of 7.1.75's conditions holds: before a "
            "CONSONANT — **इन्द्रो दधीचो अस्थभिः; भद्रं पश्येम "
            "अक्षभिः**; outside the तृतीयादि — **अस्थान्युत्कृत्य "
            "जुहोति**; and with no case ending at all — "
            "**अक्षण्वता लाङ्गलेन; अस्थन्वन्तं यद् अनस्था "
            "बिभर्ति**. Three conditions lapsing, one for each "
            "quarter of the rule they came from"),
    Num(
        "7.1.77", does="ī", of=ASTHYADI, before=("dvivacana",),
        chandasi=True, blocks=("7.1.73",),
        why="ई च द्विवचने — and in the dual they take ई, also "
            "udātta: **अक्षी ते इन्द्र पिङ्गले कपेरिव; अक्षीभ्यां "
            "ते नासिकाभ्याम्**. The ई beats 7.1.73's नुम् for "
            "being later, and the नुम् does not then come back "
            "— **सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितम् "
            "एव**"),
    Num(
        "7.1.78", refuses=True, of=("śatṛ",), gana="abhyasta",
        blocks=("7.1.70",),
        why="नाभ्यस्ताच्छतुः — the शतृ after a REDUPLICATED stem "
            "does not take नुम्: **ददत्, ददतौ, ददतः; दधत्; "
            "जक्षत्; जाग्रत्**. And the refusal reaches across "
            "an intervening ई — **शतुरनन्तर ईकारो न विहित इति "
            "व्यवहितस्यापि नुमः प्रतिषेधो विज्ञायते**"),
    Num(
        "7.1.79", of=("śatṛ",), gana="abhyasta",
        gender="napuṃsaka", optional=True, blocks=("7.1.78",),
        why="वा नपुंसकस्य — but for a NEUTER the नुम् is optional "
            "after all: **ददति, ददन्ति कुलानि; दधति, दधन्ति; "
            "जक्षति, जक्षन्ति; जाग्रति, जाग्रन्ति** — the "
            "refusal of the sūtra before undone by half"),
    Num(
        "7.1.80", of=("śatṛ",), gana="a-varṇa-anta",
        before=("śī", "nadī"), optional=True,
        why="आच्छीनद्योर्नुम् — after an अ-final stem the शतृ "
            "optionally takes नुम् before शी and a नदी ending: "
            "**तुदती कुले, तुदन्ती कुले; याती ब्राह्मणी, यान्ती "
            "ब्राह्मणी; करिष्यती, करिष्यन्ती**.\\n\\n"
            "**AND THE VṚTTI CANNOT AGREE ON WHAT आत् "
            "QUALIFIES.** The vowels have already merged, so "
            "there is no अ-final stem left to speak of. "
            "**अत्र समाधिं केचिद् आहुः — शतुरवयवे शतृशब्दे "
            "वर्तते** — some read आत् with the शतृ's own first "
            "sound; **अपरे पुनराहुः — आदित्येतेन शीनद्यावेव "
            "विशेष्येते** — others read it with the शी and the "
            "नदी. Two readings, and the vṛtti gives both without "
            "choosing"),
    Num(
        "7.1.81", of=("śatṛ",), gana="śap-śyan",
        before=("śī", "nadī"), nitya=True, blocks=("7.1.80",),
        why="शप्श्यनोर्नित्यम् — but after शप् and श्यन् the नुम् "
            "is COMPULSORY: **पचन्ती कुले, पचन्ती ब्राह्मणी; "
            "दीव्यन्ती; सीव्यन्ती**. **नित्यग्रहणं वेत्यस्य "
            "अधिकारस्य निवृत्त्यर्थम्** — the word नित्यम् is "
            "there to end the वा that has been governing, or "
            "one might have thought the option went on"),
    Num(
        "7.1.82", of=("anaḍuh",), before=("su",),
        why="सावनडुहः — अनडुह् takes नुम् before सु: **अनड्वान्; "
            "हे अनड्वन्**. Whether it goes in before or after "
            "7.1.98's आम् is disputed — **केचिद् आदित्यधिकाराद् "
            "आममोः कृतयोर् नुमं कुर्वन्ति**, while others let "
            "both apply without either displacing the other, "
            "**यथा चिचीषत्यादिषु दीर्घत्वद्विर्वचनयोः**"),
    Num(
        "7.1.83", of=DRK_THREE, before=("su",), chandasi=True,
        why="दृक्स्ववस्स्वतवसां छन्दसि — दृक्, स्ववस् and स्वतवस् "
            "take नुम् before सु in the Veda: **ईदृङ्, तादृङ्, "
            "यादृङ्, सदृङ्; स्ववान्; स्वतवाँः पायुरग्ने**"),
)


def _reaches(row: Num, stem: str, gana: str, before: str,
             upasarga: str, gender: str, sense: str,
             chandasi: bool) -> bool:
    # `of` and `gana` name DIFFERENT dimensions here — what the
    # rule acts on, and the class of what it follows — so where a
    # row carries both they are a conjunction and not a choice.
    # 7.1.80 and 7.1.81 are why: both name the शतृ, and they are
    # told apart only by the विकरण in front of it. Read as
    # alternatives, 7.1.81 swallows 7.1.80 and तुदती loses its
    # option.
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.upasarga and upasarga != row.upasarga:
        return False
    if row.gender and gender != row.gender:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Num, stem: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, and a named
    root beats a named class.

    7.1.78–81 is the stretch that needs both: 7.1.70 gives the
    शतृ its नुम्, 7.1.78 refuses it after a reduplicated stem,
    7.1.79 makes the refusal optional for a neuter, and 7.1.81
    makes the नुम् compulsory again after two विकरणs. Four
    layers, and each names the one below it.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of and stem in row.of)
        + 6 * bool(row.upasarga)
        + 5 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.gender)
        + 4 * bool(row.sense)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Nasal:
    """What the run answers: नुम्, or what stands in its place."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    nitya: bool = False
    blocked_by: Tuple[str, ...] = ()


def num(stem: str = "", *, gana: str = "", before: str = "",
        upasarga: str = "", gender: str = "", sense: str = "",
        chandasi: bool = False, wants: str = "") -> Nasal:
    """
    7.1.58–83 — where the नुम् goes in, and what stands instead.

    Nothing answers by default. Most stems take no नुम् anywhere,
    and the ones that do take it only in the environments these
    twenty-six sūtras name.
    """
    matched = [
        row for row in NUM_TABLE
        if _reaches(row, stem, gana, before, upasarga, gender,
                    sense, chandasi)
        and (not wants or (wants == row.does and not row.refuses))
    ]
    if not matched:
        return Nasal(
            "", "", "No rule of 7.1.58-83 is reached, so no नुम् "
                    "goes in")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Nasal("" if row.refuses else row.does, row.sutra,
                 row.why, optional=row.optional, nitya=row.nitya,
                 blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Num, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NUM_TABLE if row.sutra == sutra_id)


__all__ = [
    "Num", "NUM_TABLE", "NUM_RUN", "MUCADI", "TRMPHADI",
    "RADHI_JABHI", "ASTHYADI", "ABHYASTA_FOUR", "DRK_THREE",
    "GALAVA", "Nasal", "num", "provisions_for",
]
