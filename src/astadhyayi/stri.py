# -*- coding: utf-8 -*-
"""
४.१.३–३८ — which affix makes a stem feminine.

4.1.3 स्त्रियाम् opens a run that gives eight affixes — टाप्, डाप्,
चाप्, ङीप्, ङीष्, ङीन्, ऊङ्, ष्फ — and spends most of its length
saying which stem takes which. The whole of it stands under 4.1.1's
heading, but only in part: ङ्याप्प्रातिपदिकात् इति सर्वाधिकारेऽपि
**प्रातिपदिकमात्रमत्र प्रकरणे संबध्यते, ङ्यापोरनेनैव विधानात्** — a
heading that names three things governs a section with only one of
them, because this section is where the other two are MADE. A rule
cannot take as its input what it is about to produce.

**The question is the same as 3.2's and 3.3's — WHICH AFFIX COMES —
and it is asked of a different thing.** There the ground was a root
and a sense; here it is a stem and what the stem denotes. So the table
has the same shape and different columns, and the resolver is the same
resolver: the most specific matching row wins.

**What is new is that the answer is often no answer.** 4.1.10, 4.1.11,
4.1.12 refuse; 4.1.8, 4.1.13 leave it open; 4.1.32 and 4.1.33 fix
particular words. A run spent on saying which of eight affixes comes
is also spent on saying, eight times over, that none of them does.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.sup import AP, NGI, nominal_base

#: The eight affixes 4.1.3's section gives. The three ङी and the
#: three आप् are 4.1.1's two class-words, read off that rule rather
#: than typed again; ऊङ् and ष्फ stand outside both.
STRI: Tuple[str, ...] = NGI + AP + ("ūṅ", "ṣpha")

#: And two more, given by 4.1.77 to 4.1.81 from under 4.1.76
#: तद्धिताः rather than under 4.1.3 स्त्रियाम्. 4.1.77's vṛtti says
#: so outright — स च तद्धितसंज्ञो भवति — so the feminine is marked by
#: two kinds of affix under two headings, and the two inventories are
#: kept apart rather than merged.
#:
#: ष्यङ् is CONSUMED FOUR SŪTRAS BEFORE IT IS GIVEN. 4.1.74 यङश्चाप्
#: reads यङ् as a class-word for ञ्यङ् and ष्यङ् — ञ्यङः ष्यङश्च
#: सामान्यग्रहणमेतत् — and ष्यङ् is made at 4.1.78. कारीषगन्ध्या is
#: the example on both sides.
STRI_TADDHITA: Tuple[str, ...] = ("ti", "ṣyaṅ")


#: Which stem-final counts as an instance of which. A stem in मन् is
#: a stem in न्, which is exactly why 4.1.5 gives ङीप् to it and
#: 4.1.11 exists to take it away again; a stem in हायन is a stem in
#: अ, which is why 4.1.27 has to say टापि प्राप्ते.
#:
#: **Declared, not computed.** `stem_final` holds two kinds of value —
#: a SOUND (अ, ऋ, न्) and a whole final MEMBER (पाद, ऊधस्, हायन) — and
#: matching one against the other by spelling would make पाद a stem in
#: अ. That is the one-name-two-questions fault this codebase keeps
#: meeting, met inside a single field, and the answer is the same: say
#: what is meant instead of inferring it.
WITHIN = {
    "man": ("n",),
    "van": ("n",),
    "an": ("n",),
    "dāman": ("n", "man"),
    "hāyana": ("a",),
    "kāṇḍa": ("a",),
    "puruṣa": ("a",),
    "krīta": ("a",),
    "kta": ("a",),
    "pati": ("i",),
    "ūru": ("u",),
    "bāhu": ("u",),
}
#: The four that were owed are here now: 4.1.50 states क्रीत, 4.1.65
#: पति, 4.1.67 बाहु and 4.1.69 ऊरु. A containment to a final no
#: codified rule names is a guess, and a test holds both halves of
#: every entry to the table — which is what kept these four out
#: until their rules arrived.


@dataclass(frozen=True)
class Stri:
    """One rule about which affix makes a stem feminine."""

    sutra: str
    #: The affix. Where `refuses` is set this is what the rule
    #: says NO to, and "" where it refuses every one of them —
    #: which 4.1.10 alone does.
    gives: str = ""
    #: Particular stems the rule names.
    of: Tuple[str, ...] = ()
    #: A गण the rule names — अजादि, स्वस्रादि, सपत्न्यादि. Read from
    #: the गणपाठ where the text on disk has it.
    gana: str = ""
    #: What the stem ends in. NOT `ends_in`, which this codebase asks
    #: for a compound's last member, nor `root_final`, which it asks
    #: for a root's last sound: this is a nominal stem's.
    stem_final: str = ""
    #: An इत् the stem's own affix carried: उगित्, टित्, यञ्, अण्.
    marked: str = ""
    #: What the word denotes — जाति, संज्ञा, वयस्, ऋच्, क्षेत्र.
    sense: str = ""
    #: बहुव्रीहि or द्विगु, where the rule names one.
    compound: str = ""
    #: A named प्रातिपदिक-class this rule is stated of.
    of_samjna: str = ""
    #: True where the rule REFUSES rather than gives. A प्रतिषेध does
    #: not govern what it excepts, so a refusal reports the rule that
    #: would have supplied and carries this one on `blocked_by`.
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    #: A second thing the rule does in the same act: an augment, or a
    #: substitution in the stem. 4.1.7's र, 4.1.32's नुक्, 4.1.36's ऐ.
    along_with: str = ""
    #: An आचार्य the rule cites.
    authority: str = ""
    #: The accent the rule requires of the stem. 4.1.39 and 4.1.40
    #: want अनुदात्तान्त, 4.1.52 अन्तोदात्त. Two rules of this run
    #: differ in NOTHING ELSE than the accent they give, so it has to
    #: be a condition and not a remark.
    accent: str = ""
    #: The penultimate the rule names — 4.1.39's तोपधात्.
    upadha: str = ""
    #: The penultimate the rule REFUSES. 4.1.40 अन्यतः is stated
    #: against 4.1.39's, 4.1.63 wants अयोपध, 4.1.54 असंयोगोपध. A
    #: separate field rather than a tri-state, because a rule may name
    #: one and refuse another in the same breath.
    not_upadha: str = ""
    #: What stands BEFORE, as first member: करणपूर्व, दिक्पूर्व,
    #: स्वाङ्गपूर्व, and the सह-नञ्-विद्यमान of 4.1.57.
    pre: str = ""
    #: 4.1.42 maps eleven words onto eleven senses यथासंख्यम्, and no
    #: other rule of the run does anything like it. Held as pairs so
    #: the correspondence cannot come apart.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: What the rule's own words keep out, and the form that shows it.
    keeps_out: str = ""
    why: str = ""


STRI_TABLE: Tuple[Stri, ...] = (
    Stri("4.1.4", "ṭāp", gana="ajādi",
         why="अजाद्यतष्टाप्. अजादिभ्यः प्रातिपदिकेभ्यः स्त्रियां "
             "टाप्: अजा, एडका, कोकिला, चटका, अश्वा.\n\n"
             "AND THE LIST IS NOT ONE LIST. अजादिग्रहणं तु क्वचिद् "
             "जातिलक्षणे ङीषि प्राप्ते, क्वचित् तु पुंयोगलक्षणे, "
             "क्वचित् पुष्पफलोत्तरपदलक्षणे, क्वचित् वयोलक्षणे ङीपि, "
             "क्वचित् टिल्लक्षणे — its members are there to block "
             "FIVE different rules, each a different one, and "
             "हलन्तानां त्वप्राप्त एव कस्मिंश्चिदाब् विधीयते: some "
             "are there for a case no rule reached at all. A gaṇa "
             "whose members do not share a reason"),
    Stri("4.1.4", "ṭāp", stem_final="a",
         why="अजाद्यतष्टाप् — and from any stem in short अ: खट्वा, "
             "देवदत्ता. तपरकरणं तत्कालार्थम्, the त of अत् holding "
             "it to the SHORT vowel, which is why शुभंयाः and "
             "कीलालपाः get no टाप् and lose their सु by 6.1.68 "
             "instead.\n\n"
             "पकारः सामान्यग्रहणार्थः, टकारः "
             "सामान्यग्रहणाविघातार्थः — the प् so that आप् as a "
             "class-word reaches it, the ट् so that being reached as "
             "a class does not stop 1.1.64 finding its टि. Two "
             "letters, one enabling a general reading and the other "
             "protecting it"),
    Stri("4.1.5", "ṅīp", stem_final="ṛ",
         why="ऋन्नेभ्यो ङीप् — from a stem in ऋ: कर्त्री, हर्त्री. "
             "ङकारः सामान्यग्रहणार्थः, the ङ् so that ङी as a "
             "class-word reaches it"),
    Stri("4.1.5", "ṅīp", stem_final="n",
         why="ऋन्नेभ्यो ङीप् — and from a stem in न्: दण्डिनी, "
             "छत्रिणी"),
    Stri("4.1.6", "ṅīp", marked="ugit",
         why="उगितश्च. उग् इद् यत्र संभवति यथाकथंचित् तदुगिच्छब्दरूपम् "
             "— whatever has उ, ऋ or ऌ as an इत्, however it got "
             "there: भवती, अतिभवती, पचन्ती, यजन्ती.\n\n"
             "धातोरुगितः प्रतिषेधो वक्तव्यः — not where the उगित् is "
             "a ROOT: उखास्रत्, पर्णध्वत् ब्राह्मणी. And "
             "अञ्चतेश्चोपसंख्यानम्: प्राची, प्रतीची, उदीची are added "
             "back, so the vārttika takes a class out and the next "
             "puts three words in"),
    Stri("4.1.7", "ṅīp", stem_final="van", along_with="r",
         why="वनो र च. From a stem in वन्, WITH र replacing the "
             "final: धीवरी, पीवरी, शर्वरी, परलोकदृश्वरी.\n\n"
             "ऋन्नेभ्यः इत्येव ङीपि सिद्धे तत्सन्नियोगेन "
             "रेफविधानार्थं वचनम् — 4.1.5 already gives ङीप् to an "
             "न्-final stem, so this rule exists ONLY for the र, and "
             "the affix it names is along for the ride. वाने न हशः: "
             "after a consonant both are refused — सहयुध्वा ब्राह्मणी"),
    Stri("4.1.8", "ṅīp", stem_final="pāda", optional=True,
         why="पादोऽन्यतरस्याम्. पाद इति कृतसमासान्तः पादशब्दो "
             "निर्दिश्यते — the form named is the one a compound has "
             "already finished. द्विपात् beside द्विपदी, त्रिपात् "
             "beside त्रिपदी, चतुष्पाद् beside चतुष्पदी"),
    Stri("4.1.9", "ṭāp", stem_final="pāda", sense="ṛc",
         why="टाब् ऋचि, ङीपोऽपवादः. Where a verse is meant, टाप् and "
             "not the ङीप् of the rule before: द्विपदा ऋक्, त्रिपदा "
             "ऋक्, चतुष्पदा ऋक्. ऋचीत्यभिधेयनिर्देशः — the condition "
             "is what the word DENOTES. ऋचीति किम्? द्विपदी देवदत्ता",
         keeps_out="द्विपदी देवदत्ता"),
    Stri("4.1.10", of_samjna="ṣaṭ", refuses=True,
         why="न षट्स्वस्रादिभ्यः. From a stem the grammar calls षट् — "
             "the numerals from five up — NO feminine affix at all: "
             "पञ्च ब्राह्मण्यः, सप्त, नव, दश.\n\n"
             "यो यतः प्राप्नोति स सर्वः प्रतिषिध्यते — whichever "
             "affix would have come from wherever, all of them are "
             "refused. One rule in this whole run says no to every "
             "rule at once rather than to a named one"),
    Stri("4.1.10", gana="svasrādi", refuses=True,
         why="न षट्स्वस्रादिभ्यः — and from स्वसृ and its list: "
             "स्वसा, दुहिता, ननान्दा, याता, माता, तिस्रः, चतस्रः. "
             "The kinship words, which have no feminine affix "
             "because they are already nothing else"),
    Stri("4.1.11", "ṅīp", stem_final="man", refuses=True,
         why="मनः. 4.1.5 would give ङीप् to any न्-final stem, and "
             "this refuses it for those in मन्: दामा, पामा, and by "
             "परि० १६ (अनिनस्मन्ग्रहणान्यर्थवता चानर्थकेन च "
             "तदन्तविधिं प्रयोजयन्ति) also सीमा and अतिमहिमा, where "
             "the मन् carries no meaning of its own"),
    Stri("4.1.12", "ṅīp", stem_final="an", compound="bahuvrīhi",
         refuses=True,
         why="अनो बहुव्रीहेः. And refused for an अन्-final "
             "bahuvrīhi: सुपर्वा, सुचर्मा. अनुपधालोपी बहुव्रीहिर् "
             "इहोदाहरणम् — the example is one that does NOT drop its "
             "penultimate, because 4.1.28 will make that case "
             "optional instead. बहुव्रीहेरिति किम्? अतिराज्ञी",
         keeps_out="अतिराज्ञी"),
    Stri("4.1.13", "ḍāp", stem_final="man", optional=True,
         why="डाब् उभाभ्यामन्यतरस्याम्. From BOTH the stems the last "
             "two rules refused, डाप् comes optionally: पामा, पामे "
             "beside पामानः; सीमा, सीमे. उभाभ्याम् is the two "
             "preceding sūtras taken as one word — a rule whose "
             "subject is two other rules"),
    Stri("4.1.13", "ḍāp", stem_final="an", compound="bahuvrīhi",
         optional=True,
         why="डाब् उभाभ्यामन्यतरस्याम् — and from the bahuvrīhi: "
             "बहुराजा, बहुराजे; बहुतक्षा, बहुतक्षे.\n\n"
             "अन्यतरस्यांग्रहणं किमर्थम्? बहुव्रीहौ वनो र च इत्यस्य "
             "अपि विकल्पो यथा स्यात् — the word *optionally* is here "
             "so that 4.1.7's र becomes optional too in a bahuvrīhi: "
             "बहुधीवा beside बहुधीवरी. A word stated for one rule "
             "reaching a rule six sūtras back"),
    Stri("4.1.15", "ṅīp", marked="ṭit",
         why="टिड्ढाणञ्द्वयसज्दघ्नञ्मात्रच्तयप्ठक्ठञ्कञ्क्वरप्ख्युनाम्, "
             "टापोऽपवादः. Thirteen kinds of affix named in one "
             "compound, and a stem ending in any of them takes ङीप्. "
             "टितः: कुरुचरी, मद्रचरी.\n\n"
             "इह कस्माद् न भवति — पचमाना, यजमाना? "
             "द्व्यनुबन्धकत्वाल् लटः — शानच् is टित् only because लट् "
             "is, and लट् has TWO marks, so the टित्-ness is not its "
             "own. ल्युडादिषु कथम्? टित्करणसामर्थ्यात् — there the "
             "very act of marking it टित् is the argument",
         keeps_out="पचमाना, यजमाना"),
    Stri("4.1.15", "ṅīp", marked="aṇ",
         why="टिड्ढाणञ् ... अण् — कुम्भकारी, नगरकारी, औपगवी. "
             "णेऽपि क्वचिदण्कृतं कार्यं भवति (परि० ८७): चौरी, "
             "तापसी come by it though their affix is ण, but "
             "दाण्डा and मौष्टा do not. A paribhāṣā that holds "
             "sometimes, and the vṛtti says which"),
    Stri("4.1.15", "ṅīp", marked="añ",
         why="टिड्ढाणञ् ... अञ् — औत्सी, औदपानी. 4.1.73 names अञ् "
             "AGAIN, and the vṛtti says why: शार्ङ्गरवाद्यञः इति "
             "पुनरञो ग्रहणं जातिलक्षणं ङीषं बाधितुम् — the second "
             "naming is there to beat 4.1.63's ङीष्, which this one "
             "could not"),
    Stri("4.1.15", "ṅīp", marked="ḍha",
         why="टिड्ढाणञ् ... ढ — सौपर्णेयी, वैनतेयी. "
             "निरनुबन्धको ढशब्दः स्त्रियां नास्तीति "
             "निरनुबन्धकपरिभाषा (परि० ८१) न प्रवर्तते: the "
             "principle that an unmarked name means the unmarked "
             "thing does not apply, because there IS no unmarked ढ "
             "here to mean"),
    Stri("4.1.16", "ṅīp", marked="yañ",
         why="यञश्च, ङीबित्येव. From a यञ्-final stem: गार्गी, "
             "वात्सी. आपत्यग्रहणं कर्तव्यम् — only the patronymic "
             "यञ्, so 4.3.10's द्वीपादनुसमुद्रं यञ् is left out and "
             "द्वैप्या stands. योगविभाग उत्तरार्थः: the rule is split "
             "off from the last for the sake of the NEXT one, which "
             "needs यञ् by itself"),
    Stri("4.1.17", "ṣpha", marked="yañ", authority="prācām",
         optional=True,
         why="प्राचां ष्फ तद्धितः. In the view of the eastern "
             "teachers, ष्फ instead: गार्ग्यायणी, वात्स्यायनी. "
             "अन्येषाम् — गार्गी, वात्सी.\n\n"
             "षकारो ङीषर्थः — the ष् brings ङीष् as well, so "
             "प्रत्ययद्वयेनेह स्त्रीत्वं व्यज्यते: the feminine is "
             "shown by TWO affixes at once. And तद्धितग्रहणं "
             "प्रातिपदिकसंज्ञार्थम् — calling it a taddhita is what "
             "makes what it forms a प्रातिपदिक by 1.2.46, so the "
             "second affix has something to attach to"),
    Stri("4.1.18", "ṣpha", gana="lohitādi",
         why="सर्वत्र लोहितादिकतन्तेभ्यः. पूर्वेण विकल्पे प्राप्ते "
             "नित्यार्थं वचनम् — the rule before left it open, and "
             "this closes it for the list from लोहित to कत: "
             "लौहित्यायनी, शांसित्यायनी, बाभ्रव्यायणी.\n\n"
             "AND सर्वत्र IS BORROWED FORWARD, NOT BACKWARD. "
             "सर्वत्रग्रहणमुत्तरसूत्रादिहापकृष्यते, "
             "बाधकबाधनार्थम् — the word is pulled DOWN from this "
             "rule into 4.1.17 so that the eastern teachers' ष्फ may "
             "beat even 4.1.75's चाप्: आवट्यायनी. Anuvṛtti normally "
             "runs forward; this is one word read the other way"),
    Stri("4.1.19", "ṣpha", of=("kauravya", "māṇḍūka"),
         why="कौरव्यमाण्डूकाभ्यां च, यथाक्रमं टाब्ङीपोरपवादः — an "
             "exception to टाप् for the first and to ङीप् for the "
             "second, taken in order: कौरव्यायणी, माण्डूकायनी. "
             "कथं कौरवी सेना? तस्येदम् इति विवक्षायामणि कृते "
             "भविष्यति — that form is not this affix at all but a "
             "different derivation"),
    Stri("4.1.20", "ṅīp", sense="vayas-prathama",
         why="वयसि प्रथमे. कालकृतशरीरावस्था यौवनादिर्वयः — an age is "
             "a state of the body made by time. From a stem that "
             "denotes the FIRST age: कुमारी, किशोरी, बर्करी. "
             "प्रथम इति किम्? स्थविरा, वृद्धा.\n\n"
             "वयस्यचरम इति वक्तव्यम् — the vārttika widens it to any "
             "age but the LAST, which brings in वधूटी and चिरण्टी, "
             "words of the second age. So the rule says *first* and "
             "is read as *not last*",
         keeps_out="स्थविरा, वृद्धा"),
    Stri("4.1.21", "ṅīp", compound="dvigu",
         why="द्विगोः. From a stem the grammar calls द्विगु: "
             "पञ्चपूली, दशपूली. कथं त्रिफला? अजादिषु दृश्यते — that "
             "one is in 4.1.4's list, which is where the vṛtti keeps "
             "sending the exceptions to this run"),
    Stri("4.1.22", "ṅīp", compound="dvigu",
         of_samjna="taddhita-luk", refuses=True,
         why="अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि. Where a "
             "taddhita has been elided, the द्विगु does NOT take "
             "ङीप् unless it ends in a measure: पञ्चाश्वा, दशाश्वा; "
             "द्विबिस्ता, द्व्याचिता, द्विकम्बल्या.\n\n"
             "सर्वतो मानं परिमाणम्, and कालः संख्या च न परिमाणम् — "
             "a time and a number are not measures, so द्विवर्षा and "
             "द्विशता are refused too. अपरिमाणेति किम्? द्व्याढकी. "
             "तद्धितलुकीति किम्? पञ्चाश्वी in the collective sense",
         keeps_out="द्व्याढकी, पञ्चाश्वी"),
    Stri("4.1.23", "ṅīp", compound="dvigu", stem_final="kāṇḍa",
         of_samjna="taddhita-luk", sense="kṣetra", refuses=True,
         why="काण्डान्तात्क्षेत्रे. काण्डशब्दस्यापरिमाणवाचित्वात् "
             "पूर्वेणैव प्रतिषेधे सिद्धे क्षेत्रे नियमार्थं वचनम् — "
             "the rule before had already refused it, so this one is "
             "stated to RESTRICT the refusal to a field: "
             "द्विकाण्डा क्षेत्रभक्तिः, but द्विकाण्डी रज्जुः keeps "
             "its ङीप्. A प्रतिषेध narrowed by a later प्रतिषेध",
         keeps_out="द्विकाण्डी रज्जुः"),
    Stri("4.1.24", "ṅīp", compound="dvigu", stem_final="puruṣa",
         of_samjna="taddhita-luk", sense="pramāṇa",
         refuses=True, optional=True,
         why="पुरुषात्प्रमाणेऽन्यतरस्याम्. अपरिमाणान्तत्वाद् नित्ये "
             "प्रतिषेधे प्राप्ते विकल्पार्थं वचनम् — 4.1.22 refused "
             "it outright and this makes the refusal optional: "
             "द्विपुरुषा beside द्विपुरुषी. प्रमाण इति किम्? "
             "द्विपुरुषा, bought with two men, where no option "
             "arises",
         keeps_out="द्विपुरुषा (bought with two men)"),
    Stri("4.1.25", "ṅīṣ", stem_final="ūdhas", compound="bahuvrīhi",
         why="बहुव्रीहेरूधसो ङीष्. घटोध्नी, कुण्डोध्नी. Stated "
             "because 5.4.131's अनङ् makes the compound अन्-final, "
             "and then 4.1.12's refusal and 4.1.13's डाप् would both "
             "have reached it. समासान्तश्च स्त्रियामेव — the "
             "compound-ending itself comes only in the feminine, "
             "which is why महोधाः पर्जन्यः stands",
         keeps_out="महोधाः पर्जन्यः"),
    Stri("4.1.26", "ṅīp", stem_final="ūdhas", compound="bahuvrīhi",
         of_samjna="saṃkhyā-avyaya-ādi",
         why="संख्याव्ययादेर्ङीप्. पूर्वेण ङीषि प्राप्ते ङीब् "
             "विधीयते — the rule before gave ङीष् and this gives "
             "ङीप् instead, and the two differ only in ACCENT. "
             "द्व्यूध्नी, त्र्यूध्नी; अत्यूध्नी, निरूध्नी. "
             "आदिग्रहणं किम्? द्विविधोध्नी — so that a compound "
             "merely BEGINNING with a numeral is reached"),
    Stri("4.1.27", "ṅīp", stem_final="dāman",
         of_samjna="saṃkhyā-ādi",
         why="दामहायनान्ताच्च. संख्याग्रहणमनुवर्तते, नाव्ययग्रहणम् — "
             "the numeral is carried down from 4.1.26 but the "
             "indeclinable is NOT, so half of one rule's condition "
             "continues and half stops. दामान्तात् "
             "डाप्प्रतिषेधविकल्पेषु प्राप्तेषु नित्यार्थं वचनम्: "
             "द्विदाम्नी, त्रिदाम्नी"),
    Stri("4.1.27", "ṅīp", stem_final="hāyana",
         of_samjna="saṃkhyā-ādi", sense="vayas",
         why="दामहायनान्ताच्च — and from हायन, where टाप् would have "
             "come: द्विहायनी, त्रिहायणी, चतुर्हायणी. हायनो वयसि "
             "स्मृतः, so द्विहायना शाला is outside it — a year of a "
             "building is not an age. And णत्वमपि त्रिचतुर्भ्यां "
             "हायनस्येति वयस्येव स्मर्यते: even the ण of त्रिहायणी "
             "is held to the age-sense",
         keeps_out="द्विहायना शाला"),
    Stri("4.1.28", "ṅīp", stem_final="an", compound="bahuvrīhi",
         of_samjna="upadhālopin", optional=True,
         why="अन उपधालोपिनोऽन्यतरस्याम्. From an अन्-final bahuvrīhi "
             "that drops its penultimate: बहुराजा, बहुराज्ञी, "
             "बहुराजे — three forms, because ङीपा मुक्ते "
             "डाप्प्रतिषेधौ भवतः, where ङीप् does not come 4.1.12 "
             "and 4.1.13 take over.\n\n"
             "किमर्थं तर्हीदमुच्यते, ननु सिद्धा एव "
             "डाप्प्रतिषेधङीपः? अनुपधालोपिनो ङीप्प्रतिषेधार्थं "
             "वचनम् — the rule exists to keep ङीप् OFF the stems "
             "that do not drop: सुपर्वा, सुपर्वे. A rule that gives "
             "an option in order to deny it elsewhere"),
    Stri("4.1.29", "ṅīp", stem_final="an", compound="bahuvrīhi",
         of_samjna="upadhālopin", sense="saṃjñā",
         why="नित्यं संज्ञाछन्दसोः, विकल्पस्यापवादः. Where it is a "
             "NAME the option closes: सुराज्ञी, अतिराज्ञी नाम "
             "ग्रामः"),
    Stri("4.1.29", "ṅīp", stem_final="an", compound="bahuvrīhi",
         of_samjna="upadhālopin", chandasi=True,
         why="नित्यं संज्ञाछन्दसोः — and in the Veda: गौः "
             "पञ्चदाम्नी, एकदाम्नी, द्विदाम्नी; एकमूर्ध्नी "
             "(शौ०सं० ८.९.१५), समानमूर्ध्नी (तै०सं० ४.३.११.४)"),
    Stri("4.1.30", "ṅīp", gana="kevalādi", sense="saṃjñā",
         why="केवलमामकभागधेयपापापरसमानार्यकृतसुमङ्गलभेषजाच्च, "
             "संज्ञाछन्दसोरित्येव. केवली, मामकी, भागधेयीः, पापी, "
             "अपरीभ्यः, समानी, आर्यकृती, सुमङ्गली, भेषजी — nine "
             "words, each cited to a Vedic text, and each followed "
             "by इति भाषायाम् giving the ordinary form beside it. "
             "**A rule whose examples are all attested and whose "
             "counter-examples are all ordinary speech**"),
    Stri("4.1.31", "ṅīp", of=("rātri",), sense="saṃjñā",
         why="रात्रेश्चाजसौ. जस्विषयादन्यत्र — everywhere but before "
             "the nominative plural: या रात्री सृष्टा, रात्रीभिः "
             "(ऋ० १०.१०.९); but यास्ता रात्रयः. अजसादिष्विति "
             "वक्तव्यम् widens the exclusion past जस् alone.\n\n"
             "कथं तिमिरपटलैरवगुण्ठिताश्च रात्र्यः? ङीषयं "
             "बह्वादिलक्षणः — that form is 4.1.45's ङीष् and not "
             "this rule's ङीप्, by कृदिकारादक्तिनः (ग०सू० ४९). One "
             "word reached by two rules of one run, and the vṛtti "
             "tells them apart by which affix each gives",
         keeps_out="यास्ता रात्रयः"),
    Stri("4.1.32", "ṅīp", of=("antarvat", "pativat"),
         along_with="nuk",
         why="अन्तर्वत्पतिवतोर्नुक्. प्रकृतिर्निपात्यते, "
             "नुगागमस्तु विधीयते — the two words are FIXED and the "
             "augment is what is actually given; the ङीप् follows "
             "of itself, स तु नकारान्तत्वादेव सिद्धः, because they "
             "now end in न्. अन्तर्वत्नी गर्भिणी, पतिवत्नी "
             "जीवपतिः.\n\n"
             "AND THE TWO ARE FIXED FROM OPPOSITE ENDS. अन्तर्वदिति "
             "मतुब् निपात्यते, वत्वं सिद्धम्; पतिवदिति वत्वं "
             "निपात्यते, मतुप् सिद्धः — in one the affix is the "
             "irregular part and the sound-change follows; in the "
             "other the sound-change is irregular and the affix "
             "follows. One rule, two words, and each has its "
             "irregularity in the other's half.\n\n"
             "निपातनसामर्थ्यात् च विशेषे वृत्तिर्भवति: because they "
             "are fixed, they hold only in the special sense — "
             "अन्तर्वत् पतिवदिति गर्भभर्तृसंयोगे, and not for "
             "अन्तरस्यां शालायां विद्यते or पतिमती पृथिवी. And in "
             "the Veda the augment is optional: सान्तर्वत्नी "
             "(मै०सं० ४.२.९) beside सान्तर्वती (काठ०सं० ८.१०)",
         keeps_out="पतिमती पृथिवी"),
    Stri("4.1.33", "ṅīp", of=("pati",), sense="yajña-saṃyoga",
         along_with="n",
         why="पत्युर्नो यज्ञसंयोगे. पति becomes पत्न् where a "
             "sacrifice is in question, and ङीप् follows because "
             "the stem now ends in न्: पत्नि वाचं यच्छ. "
             "तत्साधनत्वात् फलग्रहीतृत्वाद् वा यजमानस्य पत्नी — she "
             "is so called either as an instrument of the rite or as "
             "a taker of its fruit. यज्ञसंयोग इति किम्? ग्रामस्य "
             "पतिरियं ब्राह्मणी. कथं वृषलस्य पत्नी? उपमानाद् "
             "भविष्यति — by likeness to the sacrificer's wife",
         keeps_out="ग्रामस्य पतिरियं ब्राह्मणी"),
    Stri("4.1.34", "ṅīp", stem_final="pati", along_with="n",
         optional=True,
         why="विभाषा सपूर्वस्य. Where something precedes, the same "
             "substitution optionally: वृद्धपत्नी beside वृद्धपतिः, "
             "स्थूलपत्नी beside स्थूलपतिः. अप्राप्तविभाषेयम् "
             "अयज्ञसंयोगत्वात् — an option where the rule before "
             "gave nothing, since no sacrifice is meant. "
             "सपूर्वस्येति किम्? पतिरियं ब्राह्मणी ग्रामस्य",
         keeps_out="पतिरियं ब्राह्मणी ग्रामस्य"),
    Stri("4.1.35", "ṅīp", gana="sapatnyādi", along_with="n",
         why="नित्यं सपत्न्यादिषु. पूर्वेण विकल्पे प्राप्ते वचनम्, "
             "and नित्यग्रहणं विस्पष्टार्थम् — the word *always* is "
             "there only for clarity, not because anything would "
             "have gone wrong without it. समानः पतिरस्याः सपत्नी, "
             "एकपत्नी.\n\n"
             "समानादिष्विति वक्तव्ये समानस्य सभावार्थं वचनम् — the "
             "list could have been called समानादि, and is not, so "
             "that समान may become स in the first member"),
    Stri("4.1.36", "ṅīp", of=("pūtakratu",), along_with="ai",
         sense="puṃyoga",
         why="पूतक्रतोरै च. पूतक्रतायी — ऐ replaces the final and "
             "ङीप् follows. त्रय एते योगाः पुंयोगप्रकरणे "
             "द्रष्टव्याः: this and the next two are to be read as "
             "belonging to the section on words used of a woman "
             "BECAUSE OF a man, which does not begin until 4.1.48. "
             "यया हि पूताः क्रतवः पूतक्रतुः सा भवति — she by whom "
             "the rites are purified would be पूतक्रतु in her own "
             "right, and that is not what the rule means"),
    Stri("4.1.37", "ṅīp",
         of=("vṛṣākapi", "agni", "kusita", "kusīda"),
         along_with="ai-udātta", sense="puṃyoga",
         why="वृषाकप्यग्निकुसितकुसीदानामुदात्तः. The same ऐ, and "
             "ACCENTED: वृषाकपायी, अग्नायी, कुसितायी, कुसीदायी.\n\n"
             "AND ONLY ONE OF THE FOUR NEEDS THE ACCENT SAID. "
             "वृषाकपिशब्दो मध्योदात्त उदात्तत्वं प्रयोजयति; "
             "अग्न्यादिषु पुनरन्तोदात्तेषु स्थानिवद्भावादेव सिद्धम् "
             "— the other three are already end-accented, so the "
             "substitute would take the accent by standing in their "
             "place. A word in a rule stated for one member of its "
             "own list. पुंयोग इत्येव — वृषाकपिः स्त्री",
         keeps_out="वृषाकपिः स्त्री"),
    Stri("4.1.38", "ṅīp", of=("manu",), along_with="au", optional=True,
         sense="puṃyoga",
         why="मनोरौ वा. ऐ उदात्त इति वर्तते, and वाग्रहणेन द्वावपि "
             "विकल्प्येते — the option covers BOTH substitutes, so "
             "तेन त्रैरूप्यं भवति, three forms stand: मनायी "
             "(मै०सं० १.८.६) with the ऐ carried down, मनावी "
             "(काठ०सं० ३०.१) with this rule's औ, and plain मनुः. "
             "**One वा making three forms** — because it is stated "
             "against a rule that had itself supplied a substitute"),
    # --- वर्ण, and two rules differing only in accent -----------------
    Stri("4.1.39", "ṅīp", sense="varṇa", accent="anudāttānta",
         upadha="t", along_with="n", optional=True,
         why="वर्णादनुदात्तात्तोपधात्तो नः. From a COLOUR-word that is "
             "unaccented at the end and has त for its penultimate, "
             "ङीप् optionally, with the त becoming न: एनी beside एता, "
             "श्येनी beside श्येता, हरिणी beside हरिता.\n\n"
             "वर्णादिति किम्? प्रकृता, प्ररुता — accented at the "
             "front by the गतिस्वर and not colour-words at all. "
             "अनुदात्तादिति किम्? श्वेता, end-accented by "
             "घृतादित्वात्. तोपधादिति किम्? the next rule takes those. "
             "Three conditions and a counter-example for each, and "
             "the accent of every example is fixed by "
             "वर्णानां तणतिनितान्तानाम् (फि०सू० २.१०).\n\n"
             "असितपलितयोः प्रतिषेधः, and छन्दसि क्नमित्येके: "
             "असिक्नी (शौ०सं० १.२३.१), पलिक्नी (ऋ० ५.२.४) — a third "
             "form for the Veda, and भाषायामपीष्यते brings it into "
             "ordinary speech as well",
         keeps_out="प्रकृता, श्वेता"),
    Stri("4.1.40", "ṅīṣ", sense="varṇa", accent="anudāttānta",
         not_upadha="t",
         why="अन्यतो ङीष्. वेति निवृत्तम् — the option stops here. "
             "The same colour-words, unaccented at the end, with any "
             "penultimate BUT त: सारङ्गी, कल्माषी, शबली.\n\n"
             "**स्वरे विशेषः — the two affixes differ in nothing but "
             "the accent they leave.** ङीप् and ङीष् both give ई, "
             "and one sūtra is spent on each side of a distinction "
             "that is inaudible except in pitch. वर्णादित्येव — "
             "खट्वा. अनुदात्तादित्येव — कृष्णा, कपिला",
         keeps_out="खट्वा, कृष्णा"),
    Stri("4.1.41", "ṅīṣ", marked="ṣit",
         why="षिद्गौरादिभ्यश्च. From a stem whose affix was षित्: "
             "3.1.145's शिल्पिनि ष्वुन् gives नर्तकी, खनकी, रजकी"),
    Stri("4.1.41", "ṅīṣ", gana="gaurādi",
         why="षिद्गौरादिभ्यश्च — and from the गौरादि list: गौरी, "
             "मत्सी. The list is long and ends with a ज्ञापक: "
             "मातामहपितामहयोर्मातरि षिच् च would have given these two "
             "by their षित्-ness alone, so putting them in the list "
             "as well teaches अनित्यः षिल्लक्षणो ङीषिति — the षित् "
             "ground is NOT invariable. तेन दंष्ट्रेत्युपपन्नं भवति"),
    Stri("4.1.42", "ṅīṣ",
         pairs=(("jānapada", "vṛtti"), ("kuṇḍa", "amatra"),
                ("goṇa", "āvapana"), ("sthala", "akṛtrima"),
                ("bhāja", "śrāṇā"), ("nāga", "sthaulya"),
                ("kāla", "varṇa"), ("nīla", "anācchādana"),
                ("kuśa", "ayovikāra"), ("kāmuka", "maithunecchā"),
                ("kabara", "keśaveśa")),
         why="जानपदकुण्डगोणस्थलभाजनागकालनीलकुशकामुककबरात् "
             "वृत्त्यमत्रावपनाकृत्रिमाश्राणास्थौल्यवर्णानाच्छादना"
             "योविकारमैथुनेच्छाकेशवेषेषु. **ELEVEN WORDS AND ELEVEN "
             "SENSES, PAIRED यथासंख्यम्** — the longest such "
             "correspondence the project has met, and every pair has "
             "its counter-form: जानपदी भवति वृत्तिश्चेत्, जानपदान्या "
             "otherwise; कुण्डी if a vessel, कुण्डान्या if not; and "
             "so through all eleven.\n\n"
             "The pairing is not decoration. नागशब्दो गुणवचनः "
             "स्थौल्ये ङीषमुत्पादयति, अन्यत्र गुण एव टापम्; "
             "जातिवचनात् तु जातिलक्षणो ङीषेव भवति — one of the "
             "eleven gets the same affix by ANOTHER rule when it "
             "names a class, so the sense decides not only whether "
             "the affix comes but which rule gives it"),
    Stri("4.1.43", "ṅīṣ", of=("śoṇa",), authority="prācām",
         optional=True,
         why="शोणात्प्राचाम्. In the eastern teachers' view: शोणी "
             "beside शोणा वडवा. The fifth attribution, and the third "
             "to that school"),
    Stri("4.1.44", "ṅīṣ", stem_final="u", sense="guṇavacana",
         optional=True,
         why="वोतो गुणवचनात्. From a QUALITY-word ending in उ, "
             "optionally: पट्वी beside पटुः, मृद्वी beside मृदुः. "
             "उत इति किम्? शुचिरियं ब्राह्मणी. गुणवचनादिति किम्? "
             "आखुः.\n\n"
             "गुणमुक्तवान् गुणवचनः, and the vṛtti closes with a "
             "definition in verse: सत्त्वे निविशतेऽपैति पृथग् जातिषु "
             "दृश्यते, आधेयश्चाक्रियाजश्च सोऽसत्त्वप्रकृतिर्गुणः — a "
             "quality enters a substance and leaves it, is seen "
             "apart across classes, is borne rather than made by an "
             "act, and is not itself a thing. **A grammatical "
             "condition given a philosophical definition**, because "
             "nothing in the form shows it.\n\n"
             "वसुशब्दाद् गुणवचनाद् ङीबाद्युदात्तार्थम् — वस्वी takes "
             "the OTHER affix, for the accent. And "
             "खरुसंयोगोपधात् प्रतिषेधो वक्तव्यः: खरुरियं ब्राह्मणी, "
             "पाण्डुरियं ब्राह्मणी",
         keeps_out="शुचिरियं ब्राह्मणी, आखुः"),
    Stri("4.1.45", "ṅīṣ", gana="bahvādi", optional=True,
         why="बह्वादिभ्यश्च. बह्वी beside बहुः. बहुशब्दो गुणवचन एव, "
             "तस्येह पाठ उत्तरार्थः — बहु is already a quality-word "
             "and reached by the rule before, so its place in this "
             "list is only for the NEXT rule, which names the list. "
             "A word put in a gaṇa to give a later rule something to "
             "point at.\n\n"
             "The list carries two गणसूत्र of its own — "
             "कृदिकारादक्तिनः and सर्वतोऽक्तिन्नर्थादित्येके — and "
             "those are what 4.1.31 sends रात्र्यः to"),
    Stri("4.1.46", "ṅīṣ", gana="bahvādi", chandasi=True,
         why="नित्यं छन्दसि. In the Veda the option closes: बह्वीषु "
             "हित्वा प्रपिबन्. नित्यग्रहणमुत्तरार्थम् — the word "
             "*always* is here for the NEXT rule and not for this "
             "one, which is the same move 4.1.45's बहु made one "
             "sūtra earlier and in the same direction"),
    Stri("4.1.47", "ṅīṣ", of=("bhū",), chandasi=True,
         why="भुवश्च. विभ्वी (ऋ० ५.३८.१), प्रभ्वी (ऋ० १.१८८.५), "
             "संभ्वी. इह कस्माद् न भवति स्वयम्भूः? उत इति "
             "तपरकरणमनुवर्तते, ह्रस्वादेवेयं पञ्चमी — 4.1.44's त "
             "is still running fifteen sūtras later and holds this "
             "to the SHORT उ. भुव इति सौत्रो निर्देशः",
         keeps_out="स्वयम्भूः"),
    # --- पुंयोग, the section 4.1.36 said it belonged to ----------------
    Stri("4.1.48", "ṅīṣ", sense="puṃyoga",
         why="पुंयोगादाख्यायाम्. पुंसा योगः पुंयोगः — from a stem "
             "that stands for a woman BECAUSE OF a man, and names "
             "him: गणकस्य स्त्री गणकी, महामात्री, प्रष्ठी, प्रचरी. "
             "पुंसि शब्दप्रवृत्तिनिमित्तस्य संभवात् पुंशब्दा एते, "
             "तद्योगात् स्त्रियां वर्तन्ते.\n\n"
             "This is the section 4.1.36's vṛtti said those three "
             "rules belonged to — त्रय एते योगाः पुंयोगप्रकरणे "
             "द्रष्टव्याः — twelve sūtras earlier.\n\n"
             "पुंयोगादिति किम्? देवदत्ता, यज्ञदत्ता. आख्याग्रहणं "
             "किम्? परिसृष्टा, प्रजाता — पुंयोगादेते शब्दाः स्त्रियां "
             "वर्तन्ते, न तु पुमांसमाचक्षते: they are used of a woman "
             "on account of a man and do not NAME him, which is the "
             "whole work of आख्यायाम्",
         keeps_out="देवदत्ता, परिसृष्टा"),
    Stri("4.1.49", "ṅīṣ", gana="indrādi", along_with="ānuk",
         why="इन्द्रवरुणभवशर्वरुद्रमृडहिमारण्ययवयवनमातुलाचार्याणाम् "
             "आनुक्. Twelve words, with the augment आनुक्: इन्द्राणी, "
             "वरुणानी, भवानी, शर्वाणी, रुद्राणी, मृडानी.\n\n"
             "AND THE RULE GIVES DIFFERENT AMOUNTS TO DIFFERENT "
             "MEMBERS. येषामत्र पुंयोग एवेष्यते, तेषाम् "
             "आनुगागममात्रं विधीयते, प्रत्ययस्तु पूर्वेणैव सिद्धः; "
             "अन्येषां तूभयं विधीयते — for those where a man is "
             "really in question the affix came from 4.1.48 already "
             "and only the augment is new; for the rest both are "
             "given here. One list, two contents.\n\n"
             "The vārttikas extend it and each states a sense: "
             "हिमारण्ययोर्महत्त्वे gives हिमानी and अरण्यानी for "
             "GREATNESS; यवाद् दोषे gives यवानी for a spoilt grain; "
             "यवनाल्लिप्याम् gives यवनानी for a SCRIPT. And "
             "अर्यक्षत्रियाभ्यां वा is expressly not about a man — "
             "विना पुंयोगेन स्वार्थ एवायं विधिः, पुंयोगे तु ङीषैव "
             "भवितव्यम्: अर्याणी in its own sense, अर्यी of a wife"),
    Stri("4.1.50", "ṅīṣ", stem_final="krīta", pre="karaṇa",
         why="क्रीतात्करणपूर्वात्. करणं पूर्वमस्मिन्निति करणपूर्वं "
             "प्रातिपदिकम् — where what precedes names the MEANS: "
             "वस्त्रेण क्रीयते सा वस्त्रक्रीती, वसनक्रीती. "
             "करणपूर्वादिति किम्? सुक्रीता, दुष्क्रीता.\n\n"
             "इह कस्माद् न भवति — सा हि तस्य धनक्रीता? टाबन्तेन "
             "समासः: there the compound is made with a word that "
             "ALREADY has टाप्, so this rule has nothing to add. A "
             "form saved by the order in which the compound was made",
         keeps_out="सुक्रीता, धनक्रीता"),
    Stri("4.1.51", "ṅīṣ", stem_final="kta", pre="karaṇa",
         sense="alpākhyā",
         why="क्तादल्पाख्यायाम्. अल्पाख्यायामिति समुदायोपाधिः — the "
             "smallness qualifies the WHOLE compound and not either "
             "member: अभ्रविलिप्ती द्यौः, सूपविलिप्ती पात्री, "
             "अल्पसूपेत्यर्थः. अल्पाख्यायामिति किम्? "
             "चन्दनानुलिप्ता ब्राह्मणी",
         keeps_out="चन्दनानुलिप्ता ब्राह्मणी"),
    Stri("4.1.52", "ṅīṣ", stem_final="kta", compound="bahuvrīhi",
         accent="antodātta",
         why="बहुव्रीहेश्चान्तोदात्तात्. शङ्खभिन्नी, ऊरुभिन्नी, "
             "गलोत्कृत्ती, केशलूनी. बहुव्रीहेरिति किम्? पादपतिता.\n\n"
             "The vārttikas cut it back from four directions: "
             "अन्तोदात्ताज् जातप्रतिषेधः (दन्तजाता, स्तनजाता); "
             "पाणिगृहीत्यादीनामर्थविशेषे — पाणिगृहीती is a WIFE, "
             "यस्यास्तु कथंचित् पाणिर्गृह्यते पाणिगृहीता सा भवति, so "
             "the affix marks a sense and not a form; and "
             "अबहुनञ्सुकालसुखादिपूर्वात्, which keeps out बहुकृता, "
             "अकृता, सुकृता, मासजाता, सुखजाता",
         keeps_out="पादपतिता, दन्तजाता"),
    Stri("4.1.53", "ṅīṣ", stem_final="kta", compound="bahuvrīhi",
         accent="antodātta", pre="asvāṅga", optional=True,
         why="अस्वाङ्गपूर्वपदाद्वा. पूर्वेण नित्ये प्राप्ते विकल्प "
             "उच्यते — the rule before was obligatory and this makes "
             "it optional where the first member is NOT a body part: "
             "शार्ङ्गजग्धी beside शार्ङ्गजग्धा, पलाण्डुभक्षिती, "
             "सुरापीती. अस्वाङ्गपूर्वपदादिति किम्? शङ्खभिन्नी. "
             "बहुलं संज्ञाछन्दसोरिति वक्तव्यम्",
         keeps_out="शङ्खभिन्नी, वस्त्रच्छन्ना"),
    # --- स्वाङ्ग, and the four rules that fence it --------------------
    Stri("4.1.54", "ṅīṣ", of_samjna="svāṅga", not_upadha="saṃyoga",
         optional=True,
         why="स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्. From a BODY PART that "
             "is the subordinate member and has no conjunct for its "
             "penultimate, optionally: चन्द्रमुखी beside चन्द्रमुखा, "
             "अतिकेशी beside अतिकेशा माला. स्वाङ्गादिति किम्? "
             "बहुयवा. उपसर्जनादिति किम्? अशिखा. असंयोगोपधादिति "
             "किम्? सुगुल्फा, सुपार्श्वा.\n\n"
             "अङ्गगात्रकण्ठेभ्य इति वक्तव्यम् adds three: मृद्वङ्गी, "
             "सुगात्री, स्निग्धकण्ठी.\n\n"
             "AND स्वाङ्ग IS DEFINED IN VERSE, because nothing in "
             "the form shows it: अद्रवं मूर्तिमत् स्वाङ्गं "
             "प्राणिस्थमविकारजम्, अतत्स्थं तत्र दृष्टं चेत् तस्य चेत् "
             "तत्तथायुतम् — not liquid, having shape, situated in a "
             "living thing, not produced by change; and a thing not "
             "so situated counts if it is seen there and belongs "
             "there. Five conditions and two extensions, for one "
             "word of one rule",
         keeps_out="बहुयवा, अशिखा, सुगुल्फा"),
    Stri("4.1.55", "ṅīṣ", gana="nāsikādi", optional=True,
         why="नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च. Seven body-parts "
             "named because the rule before could not reach them — "
             "बह्वज्लक्षणे संयोगोपधलक्षणे च प्रतिषेधे प्राप्ते "
             "वचनम्: तुङ्गनासिकी, तिलोदरी, बिम्बोष्ठी, दीर्घजङ्घी, "
             "समदन्ती, चारुकर्णी, तीक्ष्णशृङ्गी.\n\n"
             "But 4.1.57's refusal still holds — सहनञ्विद्यमान"
             "पूर्वलक्षणस्तु प्रतिषेधो भवत्येव. A rule that lifts "
             "two exclusions and leaves a third standing.\n\n"
             "पुच्छाच्चेति वक्तव्यम् adds an eighth, and "
             "कबरमणिविषशरेभ्यो नित्यम् makes it obligatory after "
             "four particular words; उपमानात् पक्षात् च पुच्छात् च "
             "reaches उलूकपक्षी सेना and उलूकपुच्छी शाला, where the "
             "body-part is a COMPARISON and the thing is an army or "
             "a hall"),
    Stri("4.1.56", "ṅīṣ", gana="kroḍādi", refuses=True,
         why="न क्रोडादिबह्वचः. क्रोडादिराकृतिगणः — an open list, "
             "one whose members are recognised by their shape rather "
             "than enumerated: कल्याणक्रोडा, कल्याणखुरा, "
             "कल्याणोखा, कल्याणबाला, कल्याणशफा, कल्याणगुदा, "
             "कल्याणघोणा, सुभगा, सुगला"),
    Stri("4.1.56", "ṅīṣ", of_samjna="bahvac", refuses=True,
         why="न क्रोडादिबह्वचः — and from a stem of MANY VOWELS: "
             "पृथुजघना, महाललाटा. A condition of length rather than "
             "of shape or sense, and the only one in this run"),
    Stri("4.1.57", "ṅīṣ", pre="saha-nañ-vidyamāna", refuses=True,
         why="सहनञ्विद्यमानपूर्वाच्च. Where सह, the negative नञ् or "
             "विद्यमान stands first, no ङीष्: सकेशा, अकेशा, "
             "विद्यमानकेशा; सनासिका, अनासिका, विद्यमाननासिका. It "
             "refuses both 4.1.54 and 4.1.55, and 4.1.55's own vṛtti "
             "says so"),
    Stri("4.1.58", "ṅīṣ", stem_final="nakha", sense="saṃjñā",
         refuses=True,
         why="नखमुखात्संज्ञायाम्. Where the compound is a NAME: "
             "शूर्पणखा, वज्रणखा, गौरमुखा, कालमुखा. संज्ञायामिति "
             "किम्? ताम्रनखी कन्या, चन्द्रमुखी",
         keeps_out="ताम्रनखी कन्या"),
    Stri("4.1.58", "ṅīṣ", stem_final="mukha", sense="saṃjñā",
         refuses=True,
         why="नखमुखात्संज्ञायाम् — and from मुख: गौरमुखा, कालमुखा"),
    Stri("4.1.59", "ṅīṣ", of=("dīrghajihva",), chandasi=True,
         why="दीर्घजिह्वी च छन्दसि. निपात्यते — the form is FIXED, "
             "and what the fixing supplies is an affix 4.1.54 could "
             "not give: संयोगोपधत्वादप्राप्तो ङीष् विधीयते, the "
             "penultimate being a conjunct. दीर्घजिह्वी वै देवानां "
             "हव्यमवालेट् (मै०सं० ३.१०.६). चकारः "
             "संज्ञानुकर्षणार्थः, and निपातनं नित्यार्थम् — the "
             "fixing also closes the option"),
    Stri("4.1.60", "ṅīp", pre="dik",
         why="दिक्पूर्वपदान्ङीप्. Where a DIRECTION stands first, "
             "ङीप् and not ङीष् — स्वरे विशेषः, the two differ only "
             "in accent again: प्राङ्मुखी, प्राङ्नासिकी.\n\n"
             "स्वाङ्गाच्चोपसर्जनाद् इत्येवमादिविधिप्रतिषेधविषयः "
             "सर्वोऽप्यपेक्ष्यते, यत्र ङीष् विहितस्तत्र तदपवादः — "
             "this rule looks back over the WHOLE स्वाङ्ग section, "
             "giving and refusing alike, and excepts it wherever ङीष् "
             "was given. So इह न भवति प्राग्गुल्फा, प्राक्क्रोडा, "
             "प्राग्जघना: where the section refused, this rule has "
             "nothing to except",
         keeps_out="प्राग्गुल्फा, प्राक्क्रोडा"),
    Stri("4.1.61", "ṅīṣ", stem_final="vāh",
         why="वाहः. ङीषेव स्वर्यते, न ङीप् — the accent shows which "
             "of the two is meant. वहेरयं ण्विप्रत्ययान्तस्य "
             "निर्देशः, सामर्थ्यात् तदन्तविधेर्विज्ञानम्: the word "
             "named is वह् with ण्वि, and the compound-reaching is "
             "read off the fact that a bare one would have no use. "
             "दित्यौही (तै०सं० ४.७.१०.१), प्रष्ठौही"),
    Stri("4.1.62", "ṅīṣ", of=("sakhi", "aśiśvi"), sense="bhāṣā",
         why="सख्यशिश्वी इति भाषायाम्. Two words fixed with ङीष्, "
             "and ONLY in ordinary speech: सखीयं मे ब्राह्मणी; "
             "नास्याः शिशुरस्तीति अशिश्वी. भाषायामिति किम्? सखा "
             "सप्तपदी भव (आ०गृ० १.७.१९) — the Vedic form keeps the "
             "masculine.\n\n"
             "**The reverse of every छन्दसि rule in this run.** Those "
             "license a Vedic form beside an ordinary one; this "
             "licenses an ordinary form and leaves the Veda alone",
         keeps_out="सखा सप्तपदी भव"),
    # --- जाति ---------------------------------------------------------
    Stri("4.1.63", "ṅīṣ", sense="jāti", of_samjna="astrīviṣaya",
         not_upadha="ya",
         why="जातेरस्त्रीविषयादयोपधात्. From a CLASS-word that is not "
             "confined to the feminine and has no य for its "
             "penultimate: कुक्कुटी, सूकरी, ब्राह्मणी, वृषली, "
             "नाडायनी, चारायणी, कठी, बह्वृची. जातेरिति किम्? मुण्डा. "
             "अस्त्रीविषयादिति किम्? मक्षिका. अयोपधादिति किम्? "
             "क्षत्रिया.\n\n"
             "AND जाति IS DEFINED IN VERSE, like स्वाङ्ग and "
             "गुणवचन before it: आकृतिग्रहणा जातिर्लिङ्गानां च न "
             "सर्वभाक्, सकृदाख्यातनिर्ग्राह्या गोत्रं च चरणैः सह — "
             "grasped by form, not sharing in all genders, seized by "
             "being named once, and taking in lineage along with the "
             "schools. **Three of this run's conditions are defined "
             "in verse and none in the sūtra**, because none of them "
             "is visible in the word.\n\n"
             "योपधप्रतिषेधे हयगवयमुकयमत्स्यमनुष्याणामप्रतिषेधः puts "
             "five back: हयी, गवयी, मुकयी, मत्सी, मनुषी",
         keeps_out="मुण्डा, मक्षिका, क्षत्रिया"),
    Stri("4.1.64", "ṅīṣ", gana="pākādi", sense="jāti",
         why="पाककर्णपर्णपुष्पफलमूलवालोत्तरपदाच्च. Seven final "
             "members, and stated because the rule before could not "
             "reach them: स्त्रीविषयत्वादेतेषां पूर्वेणाप्राप्तः "
             "प्रत्ययो विधीयते. ओदनपाकी, शङ्कुकर्णी, शालपर्णी, "
             "शङ्खपुष्पी, दासीफली, दर्भमूली, गोबाली.\n\n"
             "पुष्पफलमूलोत्तरपदात् तु यतो नेष्यते तदजादिषु पठ्यते — "
             "and whatever is NOT wanted is put in 4.1.4's list "
             "instead. The second rule of the pāda to say so"),
    Stri("4.1.65", "ṅīṣ", stem_final="i", sense="manuṣya-jāti",
         why="इतो मनुष्यजातेः. From an इ-final word naming a HUMAN "
             "class: अवन्ती, कुन्ती, दाक्षी, प्लाक्षी. इत इति किम्? "
             "विट्, दरत्. मनुष्यग्रहणं किम्? तित्तिरिः.\n\n"
             "जातेरिति वर्तमाने पुनर्जातिग्रहणं योपधादपि यथा स्यात् "
             "— the word जाति is said AGAIN though it is already "
             "carried down, so that a य-penultimate is reached too: "
             "औदमेयी. A repetition that lifts one of the previous "
             "rule's three conditions and leaves the others",
         keeps_out="विट्, तित्तिरिः"),
    # --- ऊङ् ----------------------------------------------------------
    Stri("4.1.66", "ūṅ", stem_final="u", sense="manuṣya-jāti",
         why="ऊङुतः. From a उ-final word naming a human class, a "
             "DIFFERENT affix: कुरूः, ब्रह्मबन्धूः, वीरबन्धूः. "
             "ङकारो नोङ्धात्वोः इति विशेषणार्थः, "
             "दीर्घोच्चारणं कपो बाधनार्थम् — the ङ् so that 6.1.175 "
             "can pick it out, and the long ऊ so that कप् is beaten. "
             "अयोपधादित्येतदत्रापेक्ष्यते — अध्वर्युर्ब्राह्मणी.\n\n"
             "अप्राणिजातेश्चारज्ज्वादीनाम् extends it: अलाबूः, "
             "कर्कन्धूः. अप्राणिग्रहणं किम्? कृकवाकुः. "
             "अरज्ज्वादीनामिति किम्? रज्जुः, हनुः",
         keeps_out="अध्वर्युर्ब्राह्मणी, रज्जुः"),
    Stri("4.1.67", "ūṅ", stem_final="bāhu", sense="saṃjñā",
         why="बाह्वन्तात्संज्ञायाम्. भद्रबाहूः, जालबाहूः. "
             "संज्ञायामिति किम्? वृत्तौ बाहू अस्याः वृत्तबाहुः",
         keeps_out="वृत्तबाहुः"),
    Stri("4.1.68", "ūṅ", of=("paṅgu",),
         why="पङ्गोश्च. पङ्गूः. And "
             "श्वशुरस्योकाराकारयोर्लोपश्च वक्तव्यः adds श्वश्रूः, "
             "where the affix comes with two elisions"),
    Stri("4.1.69", "ūṅ", stem_final="ūru", sense="aupamye",
         why="ऊरूत्तरपदादौपम्ये. Where a COMPARISON is meant: "
             "कदलीस्तम्भोरूः, नागनासोरूः, करभोरूः. औपम्य इति किम्? "
             "वृत्तोरुः स्त्री",
         keeps_out="वृत्तोरुः स्त्री"),
    Stri("4.1.70", "ūṅ", stem_final="ūru", gana="saṃhitādi",
         why="संहितशफलक्षणवामादेश्च. अनौपम्यार्थ आरम्भः — begun "
             "for the case where NO comparison is meant, which is "
             "what the rule before required: संहितोरूः, शफोरूः, "
             "लक्षणोरूः, वामोरूः. सहितसहाभ्यां चेति वक्तव्यम्"),
    Stri("4.1.71", "ūṅ", of=("kadru", "kamaṇḍalu"), chandasi=True,
         why="कद्रुकमण्डल्वोश्छन्दसि. कद्रूश्च वै सुपर्णी च "
             "(तै०सं० ६.१.६.१); मा स्म कमण्डलूं शूद्राय दद्यात्. "
             "छन्दसीति किम्? कद्रुः, कमण्डलुः. And "
             "गुग्गुलुमधुजतुपतयालूनाम् adds four, each cited: "
             "गुग्गुलूः (शौ०सं० ४.३७.३), मधूः (शौ०सं० ७.५६.२), "
             "जतूः (मै०सं० ३.१४.६), पतयालूः (शौ०सं० ७.११५.२)"),
    Stri("4.1.72", "ūṅ", of=("kadru", "kamaṇḍalu"), sense="saṃjñā",
         why="संज्ञायाम्. अच्छन्दोऽर्थं वचनम् — the same two words "
             "outside the Veda, where they are NAMES: कद्रूः, "
             "कमण्डलूः. संज्ञायामिति किम्? कद्रुः, कमण्डलुः. Two "
             "adjacent rules for two words, one for the Veda and one "
             "for ordinary speech, and the difference between them "
             "is the whole content of the second"),
    # --- ङीन् and चाप्, the two affixes nothing gave yet --------------
    Stri("4.1.73", "ṅīn", gana="śārṅgaravādi",
         why="शार्ङ्गरवाद्यञो ङीन्. शार्ङ्गरवी, कापटवी. "
             "जातिग्रहणं चेहानुवर्तते, तेन जातिलक्षणो ङीषनेन "
             "बाध्यते, न पुंयोगलक्षणः — 4.1.63's ङीष् is beaten and "
             "4.1.48's is not, because only the first has the word "
             "जाति that carries down here. **A rule beaten or not "
             "according to which word of it is still running**"),
    Stri("4.1.73", "ṅīn", marked="añ",
         why="शार्ङ्गरवाद्यञो ङीन् — and from an अञ्-final stem: "
             "बैदी, और्वी. This is the SECOND naming of अञ्: 4.1.15 "
             "named it too, and the vṛtti there said why the naming "
             "is repeated — पुनरञो ग्रहणं जातिलक्षणं ङीषं बाधितुम्, "
             "because that rule's ङीप् could not beat 4.1.63 and this "
             "one's ङीन् can. Two rules naming one affix, and the "
             "second exists for what the first could not do"),
    Stri("4.1.74", "cāp", marked="yaṅ",
         why="यङश्चाप्. ञ्यङः ष्यङश्च सामान्यग्रहणमेतत् — यङ् is a "
             "class-word for two affixes: आम्बष्ठ्या, सौवीर्या, "
             "कौसल्या from the first; कारीषगन्ध्या, वाराह्या, "
             "बालाक्या from the second. षाच्च यञः extends it to a "
             "यञ् standing after ष: शार्कराक्ष्या, पौतिमाष्या, "
             "गौकक्ष्या"),
    Stri("4.1.75", "cāp", of=("āvaṭya",),
         why="आवट्याच्च. अवटशब्दो गर्गादिः, तस्माद् यञि कृते ङीपि "
             "प्राप्ते वचनमेतत् — 4.1.16 would have given ङीप्, and "
             "this gives चाप् instead: आवट्या.\n\n"
             "AND IT IS BEATEN IN TURN, BY A RULE FIFTY-SEVEN "
             "SŪTRAS BACK. प्राचां ष्फ एव, सर्वत्रग्रहणात् — "
             "आवट्यायनी. That is what 4.1.18's सर्वत्र was pulled "
             "backward into 4.1.17 to do, बाधकबाधनार्थम्: **this is "
             "the rule it was pulled back to beat**, and the "
             "transaction is now closed at both ends"),
    # --- and two more, from under 4.1.76 rather than 4.1.3 -----------
    Stri("4.1.77", "ti", of=("yuvan",),
         why="यूनस्तिः, ङीपोऽपवादः. युवतिः — and स च तद्धितसंज्ञो "
             "भवति, the affix is a TADDHITA. This is the first "
             "feminine affix of the pāda given from under 4.1.76 "
             "instead of 4.1.3, and the vṛtti names it as the first "
             "thing that heading will govern: वक्ष्यति यूनस्तिः"),
    Stri("4.1.78", "ṣyaṅ", marked="aṇ", sense="gotra",
         of_samjna="guru-upottama",
         why="अणिञोरनार्षयोर्गुरूपोत्तमयोः ष्यङ् गोत्रे. Where a "
             "गोत्र affix अण् or इञ् stands on a stem whose "
             "next-to-last syllable is heavy, ष्यङ् replaces it in "
             "the feminine: कारीषगन्ध्या, कौमुदगन्ध्या, वाराह्या, "
             "बालाक्या.\n\n"
             "**IT REPLACES THE AFFIX AND NOT THE WORD.** "
             "निर्दिश्यमानस्यादेशा भवन्ति इत्यणिञोरेव विज्ञायते, न "
             "तु समुदायस्य — a substitute stands for what the rule "
             "NAMES, and the rule names the two affixes.\n\n"
             "उत्तमशब्दः स्वभावात् त्रिप्रभृतीनामन्त्यमक्षरमाह, "
             "उत्तमस्य समीपमुपोत्तमम् — *last* means the last "
             "syllable of a word of three or more, and *near the "
             "last* is the one before it. A condition stated in two "
             "steps because the first would otherwise reach a word "
             "of two.\n\n"
             "Four counter-examples, one for each word of the rule. "
             "अणिञोरिति किम्? आर्तभागी, whose affix is अञ् by "
             "बिदादि — गुरूपोत्तमादिकं सर्वमस्तीति, न त्वणिञौ, so "
             "4.1.15's ङीप् comes instead. अनार्षयोरिति किम्? "
             "वासिष्ठी, वैश्वामित्री. गुरूपोत्तमयोरिति किम्? "
             "औपगवी, कापटवी. गोत्र इति किम्? आहिच्छत्री, "
             "कान्यकुब्जी.\n\n"
             "ङकारः सामान्यग्रहणार्थः, षकारस्तदविघातार्थः — the ङ् "
             "so that 4.1.74's class-word यङ् reaches it, and the ष् "
             "so that being reached as a class does not spoil it. "
             "**4.1.74 uses this affix four sūtras before it is "
             "given**, and कारीषगन्ध्या is the example on both sides",
         keeps_out="आर्तभागी, वासिष्ठी, औपगवी"),
    Stri("4.1.78", "ṣyaṅ", marked="iñ", sense="gotra",
         of_samjna="guru-upottama",
         why="अणिञोरनार्षयोर्गुरूपोत्तमयोः ष्यङ् गोत्रे — and for "
             "इञ्: वराहस्यापत्यं वाराहिः by 4.1.95's अत इञ्, and "
             "then वाराह्या"),
    Stri("4.1.79", "ṣyaṅ", of_samjna="gotra-avayava", sense="gotra",
         why="गोत्रावयवात्. गोत्रावयवा गोत्राभिमताः कुलाख्याः "
             "पुणिकभुणिकमुखरप्रभृतयः — family names taken as PARTS "
             "of a lineage: पौणिक्या, भौणिक्या, मौखर्या.\n\n"
             "अगुरूपोत्तमार्थ आरम्भः — begun for the case the rule "
             "before could not reach, its heavy penultimate being "
             "absent. And where an IMMEDIATE descendant is meant, "
             "the vṛtti sends the word elsewhere: येषां "
             "त्वनन्तरापत्येऽपीष्यते दैवदत्या याज्ञदत्येति, ते "
             "क्रौड्यादिषु द्रष्टव्याः — into the next rule's list, "
             "which is the third time in this pāda that a list is "
             "used as somewhere to put what a rule cannot hold"),
    Stri("4.1.80", "ṣyaṅ", gana="krauḍyādi",
         why="क्रौड्यादिभ्यश्च. क्रौड्या, लाड्या. "
             "**अगुरूपोत्तमार्थ आरम्भः, अनणिञर्थश्च** — begun for "
             "BOTH the conditions 4.1.78 stated and this list "
             "escapes: neither a heavy penultimate nor the two named "
             "affixes. One list lifting two conditions at once, and "
             "the rule before it lifted only the first"),
    Stri("4.1.81", "ṣyaṅ", gana="daivayajñyādi", optional=True,
         why="दैवयज्ञिशौचिवृक्षिसात्यमुग्रिकाण्ठेविद्धिभ्योऽन्यतरस्याम्. "
             "दैवयज्ञ्या beside दैवयज्ञी, शौचिवृक्ष्या beside "
             "शौचिवृक्षी.\n\n"
             "**ONE OPTION DOING TWO DIFFERENT THINGS.** इञन्ता एते, "
             "गोत्रग्रहणं च नानुवर्तते, तेनोभयत्रविभाषेयम् — the "
             "word गोत्र does NOT carry down here, so the rule "
             "covers two grounds at once and the option means "
             "something different on each. गोत्रे पूर्वेण नित्यः "
             "ष्यङादेशः प्राप्तो विकल्प्यते — in a lineage-sense it "
             "loosens what 4.1.78 made obligatory; अगोत्रे "
             "त्वनन्तरेऽपत्ये पक्षे विधीयते — of an immediate "
             "descendant it GIVES what nothing had given. And where "
             "the option is declined, तेन मुक्ते इतो मनुष्यजातेः इति "
             "ङीषेव भवति: 4.1.65 takes over"),
)


@dataclass(frozen=True)
class Added:
    """The affix that makes a stem feminine, and by which rule."""

    gives: str
    by: str
    why: str
    #: A substitution or augment the same rule makes in one act.
    along_with: str = ""
    optional: bool = False
    #: Where a प्रतिषेध kept a rule out, the sūtra that refused. The
    #: affix is still reported by the rule that SUPPLIES it, since a
    #: rule that excepts a stem by name does not thereby govern it.
    blocked_by: str = ""


@dataclass(frozen=True)
class NotAdded:
    """That no feminine affix comes, and why."""

    by: str
    why: str
    gives: str = ""


def _reaches(row: Stri, stem: str, gana: str, stem_final: str,
             marked: str, sense: str, compound: str, samjna: str,
             chandasi: bool, accent: str, upadha: str,
             pre: str) -> bool:
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.stem_final and stem_final != row.stem_final:
        if row.stem_final not in WITHIN.get(stem_final, ()):
            return False
    if row.marked and marked != row.marked:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.compound and compound != row.compound:
        return False
    if row.of_samjna and samjna != row.of_samjna:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.accent and accent != row.accent:
        return False
    if row.upadha and upadha != row.upadha:
        return False
    # A refused penultimate is a condition that BITES when it is met,
    # so an unstated one satisfies it. 4.1.40 अन्यतः reaches a
    # वर्ण-word whose penultimate is anything but त, and asking about
    # such a word without naming its penultimate is asking about a
    # word that does not have the one refused.
    if row.not_upadha and upadha == row.not_upadha:
        return False
    if row.pre and pre != row.pre:
        return False
    if row.pairs and stem not in dict(row.pairs):
        return False
    if row.pairs and sense and dict(row.pairs).get(stem) != sense:
        return False
    return True


def _how_specific(row: Stri, stem_final: str = "") -> int:
    """
    How narrowly a row states its ground. A rule naming particular
    words is the narrowest thing in this run — 4.1.19, 4.1.31, 4.1.36
    each name one or two — and a class of stem the widest.

    And a rule that names the stem's ACTUAL final outranks one that
    names a final the stem merely contains: 4.1.11 मनः over 4.1.5's
    ऋन्नेभ्यः, which is the whole relation between those two rules.
    """
    return (
        7 * bool(row.of)
        + 5 * bool(row.sense)
        + 4 * bool(row.gana)
        + 4 * bool(row.of_samjna)
        + 3 * bool(row.compound)
        + 3 * bool(row.chandasi)
        + 2 * bool(row.stem_final)
        + 2 * bool(row.stem_final and row.stem_final == stem_final)
        + 2 * bool(row.marked)
        + 7 * bool(row.pairs)
        + 4 * bool(row.pre)
        + 3 * bool(row.accent)
        + 3 * bool(row.upadha)
        + 2 * bool(row.not_upadha)
    )


def stri_affix(stem: str = "", *, gana: str = "", stem_final: str = "",
               marked: str = "", sense: str = "", compound: str = "",
               samjna: str = "", chandasi: bool = False,
               upasarjana: bool = False, accent: str = "",
               upadha: str = "", pre: str = "",
               wants: str = "") -> object:
    """
    4.1.4–38 — which affix makes a stem feminine.

    `stem_final` is what the stem ends in, `marked` the इत् its own
    affix carried, `sense` what it denotes, and `samjna` a name the
    grammar has already given it — षट्, उपधालोपिन्, संख्यादि.

    `upasarjana` is 4.1.14's condition and refuses everything after
    it: अनुपसर्जनात् is an अधिकार, and a stem that is a subordinate
    member of a compound takes no feminine affix by these rules.

    `wants` picks between two rules that reach one stem and give
    different affixes — 4.1.25's ङीष् against 4.1.26's ङीप्, which
    differ only in accent.
    """
    if upasarjana:
        return NotAdded(
            "4.1.14",
            "अनुपसर्जनात् — अधिकारोऽयम्, उत्तरसूत्रेषूपसर्जन"
            "प्रतिषेधं करोति. A stem that is a SUBORDINATE member "
            "takes none of these affixes: बहुकुरुचरा against "
            "कुरुचरी, बहुकुक्कुटा against कुक्कुटी.\n\n"
            "अस्त्यत्र प्रकरणे तदन्तविधिरिति, तथा च प्रधानेन "
            "तदन्तविधिर्भवति — the rules of this section DO reach a "
            "compound through its last member, but only where that "
            "member is the principal one: कुम्भकारी, नगरकारी")
    matched = [
        row for row in STRI_TABLE
        if _reaches(row, stem, gana, stem_final, marked, sense,
                    compound, samjna, chandasi, accent, upadha, pre)
        and (not wants or row.gives == wants)
    ]
    if not matched:
        return NotAdded(
            "4.1.3–38",
            "no rule of this run reaches it, so the stem stands as it "
            "is: स्त्रियामिति किम्? अजः, देवदत्तः")
    def narrowest(rows):
        return max(rows, key=lambda item: _how_specific(item, stem_final))

    giving = [row for row in matched if not row.refuses]
    refusing = [row for row in matched if row.refuses]

    # 4.1.10 alone refuses every affix of the section, so it can
    # answer without a supplier: refusing is all it did.
    blanket = [row for row in refusing if not row.gives]
    if blanket and not giving:
        row = narrowest(blanket)
        return NotAdded(row.sutra, row.why)

    if not giving:
        row = narrowest(refusing)
        return NotAdded(row.sutra, row.why, gives=row.gives)

    supplies = narrowest(giving)
    # Specificity picks between rules that GIVE. Whether a प्रतिषेध
    # applies is a different question and is not settled by counting
    # words: an exception is narrower by BEING one. So the refusals
    # are asked separately, and only about the affix that actually
    # won.
    against = [row for row in refusing
               if not row.gives or row.gives == supplies.gives]
    if against:
        stops = narrowest(against)
        # A rule that excepts a stem by name does not thereby govern
        # it, so the answer comes back under the supplier with the
        # refusal recorded beside it.
        return Added("", supplies.sutra, stops.why,
                     blocked_by=stops.sutra)
    return Added(supplies.gives, supplies.sutra, supplies.why,
                 along_with=supplies.along_with,
                 optional=supplies.optional)


def stri_heading() -> object:
    """
    4.1.3 स्त्रियाम् — the heading every rule of this run stands
    under, and a heading that takes only PART of the heading above it.

    ङ्याप्प्रातिपदिकात् इति सर्वाधिकारेऽपि **प्रातिपदिकमात्रमत्र
    प्रकरणे संबध्यते, ङ्यापोरनेनैव विधानात्** — 4.1.1 names three
    things and this section can use only one of them, because it is
    the section that MAKES the other two. A rule cannot take as its
    input what it is about to produce.

    **And what स्त्री means is left open on purpose.** केयं स्त्री
    नाम? सामान्यविशेषाः स्त्रीत्वादयो गोत्वादया इव बहुप्रकारा
    व्यक्तयः — femininity is a universal like cowhood, of many kinds,
    and क्वचिदाश्रयविशेषाभावादुपदेशव्यङ्ग्या एव भवन्ति: sometimes it
    has no bodily mark at all and is shown only by usage, as
    brahmin-hood is.

    Then the vṛtti declines to settle the syntax either: स्त्रीत्वं च
    प्रत्ययार्थः प्रकृत्यर्थविशेषणं चेत्युभयथापि युज्यते — the
    feminine may be what the AFFIX means or what qualifies what the
    STEM means, स्त्रियामभिधेयायां or स्त्रियां वा यत् प्रातिपदिकं
    वर्तते, and both readings work. A heading whose central word is
    given two analyses and neither chosen.
    """
    # What this section can take as its INPUT is worked out from
    # 4.1.1 rather than restated: everything that rule governs, less
    # everything this section produces. The vṛtti's argument is
    # ङ्यापोरनेनैव विधानात्, and it comes out as one set difference.
    #
    # The subtraction is against STRI — the affixes this section IS
    # FOR — and not against whichever of its rules are codified so
    # far. A section is defined by what it gives, not by how much of
    # it has been read: subtracting the table would have said, while
    # 4.1.73 to 4.1.75 were still ahead, that this section may take
    # चाप् and ङीन् as INPUT, which is the opposite of true.
    governed = set(nominal_base().covers)
    takes = tuple(sorted(governed - set(STRI)))
    return Added(
        ", ".join(takes), "4.1.3",
        "स्त्रियाम् — अधिकारोऽयम्, यदित ऊर्ध्वमनुक्रमिष्यामः "
        "स्त्रियामित्येवं तद् वेदितव्यम्. वक्ष्यति अजाद्यतष्टाप् — "
        "अजा, देवदत्ता. स्त्रियामिति किम्? अजः, देवदत्तः.\n\n"
        "A HEADING THAT TAKES ONLY PART OF THE HEADING ABOVE IT. "
        "ङ्याप्प्रातिपदिकात् इति सर्वाधिकारेऽपि प्रातिपदिकमात्रमत्र "
        "प्रकरणे संबध्यते, ङ्यापोरनेनैव विधानात् — 4.1.1 names three "
        "things and only one of them can be the input here, because "
        "this is the section that makes the other two.\n\n"
        "AND WHAT स्त्री MEANS IS LEFT OPEN. केयं स्त्री नाम? "
        "सामान्यविशेषाः स्त्रीत्वादयो गोत्वादया इव बहुप्रकारा "
        "व्यक्तयः, and क्वचिदाश्रयविशेषाभावादुपदेशव्यङ्ग्या एव "
        "भवन्ति — sometimes shown by usage alone, as ब्राह्मणत्व is. "
        "Then the syntax is left open too: स्त्रीत्वं च प्रत्ययार्थः "
        "प्रकृत्यर्थविशेषणं चेत्युभयथापि युज्यते, both readings work "
        "and neither is chosen.\n\nWhat this section can take as its "
        "input is therefore %s — asked of 4.1.1 and reduced by what "
        "the section itself gives, rather than restated here"
        % (", ".join(takes) or "nothing"))


def provisions_for(sutra_id: str) -> Tuple[Stri, ...]:
    """Every row one sūtra states — several, where it gives a list."""
    return tuple(row for row in STRI_TABLE if row.sutra == sutra_id)
