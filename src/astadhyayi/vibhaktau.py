# -*- coding: utf-8 -*-
"""
७.२.७९–११३ — before an ending: the optative, and the pronouns.

Thirty-five sūtras in two halves. 7.2.79–83 finish the सार्वधातुक
run: the लिङ् loses a स् that is not last (कुर्यात्), its या
becomes इय् after an अ-final stem (पचेत्), आन gets a मुक् (पचमानः).

**AND THEN विभक्तौ GOVERNS TO THE END OF THE PĀDA'S MIDDLE.**
7.2.85's vṛtti says how far: **मृजेर्वृद्धिः इत्यतः प्राग्
विभक्त्यधिकारः** — every rule from 7.2.84 to 7.2.113 is about
what a stem becomes before a case ending. अष्टाभिः, राभ्याम्,
युष्माभिः, त्वाम्, तिस्रः, जरसा, सः, कः, असौ, अयम्, एभिः.

**THE PRONOUNS ARE DECLINED BY SUBSTITUTION, PIECE BY PIECE.**
युष्मद् and अस्मद् take thirteen sūtras (7.2.86–98) and the
substitutes are stated for the part of the word up to its म् —
7.2.91 मपर्यन्तस्य is a heading of its own, so that युवकाम् with
its कच् is not touched and त्वया does not lose its whole stem.
Then इदम् takes six more (7.2.108–113), and each names a
different piece: its म्, its द्, its इद्, and once the whole
thing.

**AND ONE SŪTRA IS THREE OPERATIONS AT ONCE.** 7.2.107 अदस औ
सुलोपश्च gives अदस् an औ for its स् AND deletes the सु — असौ.
Two verses then ask why the deletion is stated rather than
derived, and answer with four rules that would have fired
wrongly if it were.

**WHAT THIS MODULE DOES NOT DO.** It says what the stem becomes.
The ending it becomes it before was supplied by 4.1.2 and may
have been reshaped by 7.1.9–33; the sandhi at the join is
अध्याय ८'s.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
BEFORE_RUN: Tuple[str, str] = ("7.2.79", "7.2.113")

#: Where विभक्तौ starts governing, and where the vṛtti says it
#: stops — **मृजेर्वृद्धिः इत्यतः प्राग् विभक्त्यधिकारः**.
VIBHAKTI_FROM: str = "7.2.84"
VIBHAKTI_TO: str = "7.2.113"

#: 7.2.91's own heading, inside the larger one.
MAPARYANTA_FROM: str = "7.2.91"

#: The two words thirteen sūtras are about.
THE_TWO: Tuple[str, ...] = ("yuṣmad", "asmad")

#: 7.2.92–98's substitutes, each for a different ending.
PRONOUN_PAIRS: Tuple[Tuple[str, Tuple[str, str]], ...] = (
    ("dvivacana", ("yuva", "āva")),
    ("jas", ("yūya", "vaya")),
    ("su", ("tva", "aha")),
    ("ṅayi", ("tubhya", "mahya")),
    ("ṅasi-ṣaṣṭhī", ("tava", "mama")),
    ("ekavacana", ("tva", "ma")),
)

#: 7.2.99's two, feminine only.
TRI_CATUR: Tuple[Tuple[str, str], ...] = (
    ("tri", "tisṛ"), ("catur", "catasṛ"))

#: 7.2.102's list, which the vṛtti stops at द्वि —
#: **द्विपर्यन्तानां त्यदादीनाम् अत्वम् इष्यते**.
TYADADI: Tuple[str, ...] = (
    "tyad", "tad", "yad", "etad", "idam", "adas", "dvi")


@dataclass(frozen=True)
class Before:
    """One rule of 7.2.79–113: what the stem becomes."""

    sutra: str
    #: The substitute, or `lopa` where something is dropped.
    does: str = ""
    #: The stems named outright.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: Where stem and substitute are matched one to one.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: What part of the stem is affected.
    part: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: The number, where the rule wants one.
    number: str = ""
    #: The gender, likewise.
    gender: str = ""
    #: True where the rule also deletes the ending.
    deletes_ending: bool = False
    optional: bool = False
    chandasi: bool = False
    heading: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


BEFORE_TABLE: Tuple[Before, ...] = (
    Before(
        "7.2.79", does="sa-lopa", of=("liṅ",), part="an-antya-s",
        before=("sārvadhātuka",),
        keeps_out="कुर्युः, कुर्याः — the स् IS last; क्रियास्ताम्, "
                  "कृषीष्ट — an ārdhadhātuka लिङ्, where the स् "
                  "stays",
        why="लिङः सलोपोऽनन्त्यस्य — a सार्वधातुक लिङ् loses a स् "
            "that is NOT its last sound: **कुर्यात्, कुर्याताम्, "
            "कुर्युः; कुर्वीत, कुर्वीयाताम्, कुर्वीरन्**. "
            "**कः पुनर् अनन्त्यो लिङः सकारः? यो यासुट्सुट्सीयुटाम्** "
            "— the स् of the three augments, and no other"),
    Before(
        "7.2.80", does="iy", of=("yā",), gana="a-anta",
        before=("sārvadhātuka",),
        keeps_out="चिनुयात्, सुनुयात् — the stem is not अ-final; "
                  "यायात् — a long आ, which the तपर shuts out; "
                  "चिकीर्ष्यात् — an ārdhadhātuka",
        why="अतो येयः — after an अ-final stem the या of a "
            "सार्वधातुक becomes इय्: **पचेत्, पचेताम्, "
            "पचेयुः**.\\n\\n"
            "**AND IT HAS TO BEAT TWO OTHER RULES AT ONCE.** "
            "6.1.96's पररूप is displaced in पचेयुः; and asked "
            "why 6.4.48's अ-loss does not apply first, the vṛtti "
            "answers that 7.3.101's lengthening would have "
            "applied too. **तद् अनेनावश्यं विध्यन्तरं "
            "बाधितव्यम्** — something must be displaced whatever "
            "one does, and what displaces the one displaces the "
            "other"),
    Before(
        "7.2.81", does="iy", part="ā-of-ṅit", gana="a-anta",
        before=("sārvadhātuka",),
        keeps_out="पचन्ति, पचन्ते — no आ; पचावहै, पचामहै — the "
                  "affix is not ङित्",
        why="आतो ङितः — and the आ of a ङित् ending after an "
            "अ-final stem: **पचेते, पचेथे, पचेताम्, पचेथाम्; "
            "यजेते, यजेथे**.\\n\\n"
            "**AND THE WORD ङित् IS READ AS *LIKE A ङित्* AND "
            "NOT *WHEN A ङित् FOLLOWS*.** 1.2.4's "
            "सार्वधातुकमपित् makes such an affix ङिद्वत्; read "
            "the other way, 1.3.12's अनुदात्तङित आत्मनेपदम् "
            "would wrongly give an आत्मनेपद ending. "
            "**ङित इव ङिद्वद् इति**"),
    Before(
        "7.2.82", does="muk", part="a", before=("āna",),
        why="आने मुक् — before आन the stem's अ takes the augment "
            "मुक्: **पचमानः, यजमानः**.\\n\\n"
            "**AND THE AUGMENT BELONGS TO THE अ ALONE, WHICH "
            "MATTERS FOR THE ACCENT.** **अकारमात्रभक्तोऽयं मुक् "
            "अदुपदेशग्रहणेन गृह्यते** — so 6.1.186's "
            "अदुपदेशाल्लसार्वधातुकम् still reaches it and the "
            "ending is अनुदात्त. The objection is that with the "
            "मुक् in, the अ is a syllable and a half; the answer "
            "is that **उपदेशग्रहणं तत्र क्रियते**, the rule "
            "looks at the root as taught"),
    Before(
        "7.2.83", does="ī", of=("ās",), before=("āna",),
        why="ईदासः — and after आस् the आन becomes ई: **आसीनो "
            "यजते**. The genitive the substitution needs is read "
            "out of the ablative the sūtra has — **अत्र पञ्चम्या "
            "परस्य षष्ठी कल्प्यते**"),
    Before(
        "7.2.84", does="ā", of=("aṣṭan",), before=("vibhakti",),
        optional=True,
        keeps_out="अष्टत्वम्, अष्टता — a taddhita and no case "
                  "ending",
        why="अष्टन आ विभक्तौ — अष्टन् takes आ before a case "
            "ending: **अष्टाभिः, अष्टाभ्यः, अष्टानाम्, "
            "अष्टासु**.\\n\\n"
            "**AND THE विभक्ति HEADING BEGINS HERE.** "
            "**मृजेर्वृद्धिः इत्यतः प्राग् विभक्त्यधिकारः** — "
            "thirty rules, ending at 7.2.113.\\n\\n"
            "**AND THE OPTION IS NOT IN THE SŪTRA BUT READ OUT "
            "OF TWO OTHERS.** **विकल्पेनायम् आकारो भवति, एतद् "
            "ज्ञापितम् अष्टनो दीर्घात् इति दीर्घग्रहणाद्, "
            "अष्टाभ्य औश् इति च कृतात्वस्य निर्देशात्** — 6.1.172 "
            "says *after a LONG अष्टन्* and 7.1.21 names the one "
            "that HAS its आ, and neither wording would be needed "
            "if the आ were compulsory. So अष्टभिः stands beside "
            "अष्टाभिः"),
    Before(
        "7.2.85", does="ā", of=("rai",), before=("hal-vibhakti",),
        keeps_out="रायौ, रायः — a vowel-initial ending; रैत्वम्, "
                  "रैता — a taddhita",
        why="रायो हलि — रै becomes रा before a consonant-initial "
            "case ending: **राभ्याम्, राभिः**. And this sūtra's "
            "vṛtti is where the reader is told how far the "
            "विभक्ति heading reaches — **मृजेर्वृद्धिः इत्यतः "
            "प्राग् विभक्त्यधिकारः** — which is a fact about "
            "thirty rules and not about this one"),
    Before(
        "7.2.86", does="ā", of=THE_TWO, before=("vibhakti",),
        not_before=("ādeśa",),
        keeps_out="युष्मत्, अस्मत् — the ending has been replaced "
                  "already, and this rule wants one that has not",
        why="युष्मदस्मदोरनादेशे — युष्मद् and अस्मद् take आ "
            "before a case ending that has NOT been replaced: "
            "**युष्माभिः, अस्माभिः, युष्मासु, अस्मासु**. The "
            "word अनादेशे is put here although हलि would have "
            "sufficed, because 7.2.89 needs it — "
            "**उत्तरत्र त्वनादेशग्रहणेन प्रयोजनम्... तद् इहैव "
            "क्रियते**"),
    Before(
        "7.2.87", does="ā", of=THE_TWO, before=("dvitīyā",),
        why="द्वितीयायां च — and before the accusative: **त्वाम्, "
            "माम्, युवाम्, आवाम्, युष्मान्, अस्मान्**. "
            "**आदेशार्थं वचनम्** — the sūtra exists only for the "
            "substitute, since 7.2.86's अनादेशे would have "
            "reached the accusative anyway and its हलि would "
            "not"),
    Before(
        "7.2.88", does="ā", of=THE_TWO, before=("prathamā",),
        number="dvivacana",
        keeps_out="युवयोः, आवयोः — not the nominative; त्वम्, "
                  "अहम्, यूयम्, वयम् — not the dual; and in the "
                  "Veda **युवं वस्त्राणि पीवसा वसाथे**",
        why="प्रथमायाश्च द्विवचने भाषायाम् — and before the "
            "nominative DUAL, in the language: **युवाम्, "
            "आवाम्**. The word भाषायाम् is what keeps the "
            "Vedic युवम् standing"),
    Before(
        "7.2.89", does="y", of=THE_TWO, before=("ac-vibhakti",),
        not_before=("ādeśa",),
        keeps_out="युवाभ्याम्, आवाभ्याम् — a consonant-initial "
                  "ending; त्वद् गच्छति, मद् गच्छति — the "
                  "ending has been replaced",
        why="योऽचि — and य before a vowel-initial case ending "
            "that has not been replaced: **त्वया, मया, त्वयि, "
            "मयि, युवयोः, आवयोः**. **अचीत्येतत्** could have "
            "been dropped if हलि were carried down, and is put "
            "in **विस्पष्टार्थम्**"),
    Before(
        "7.2.90", does="lopa", of=THE_TWO, before=("śeṣa",),
        why="शेषे लोपः — and in every OTHER case ending the stem "
            "is dropped: **त्वम्, अहम्, यूयम्, वयम्, तुभ्यम्, "
            "मह्यम्, त्वत्, मत्, तव, मम, युष्माकम्, "
            "अस्माकम्**.\\n\\n"
            "**AND A VERSE SAYS WHICH ENDINGS THOSE ARE.** "
            "**पञ्चम्याश्च चतुर्थ्याश्च षष्ठीप्रथमयोरपि। "
            "यान्यद्विवचनान्यत्र तेषु लोपो विधीयते** — the "
            "ablative, the dative, the genitive and the "
            "nominative, dual excepted. And the loss leaves no "
            "feminine: **त्वं ब्राह्मणी** takes no टाप्, "
            "**अलिङ्गे वा युष्मदस्मदी**"),
    Before(
        "7.2.91", heading=True, of=THE_TWO,
        keeps_out="युवकाम्, आवकाम् — a कच् has come and the "
                  "substitute must not reach past the म्",
        why="मपर्यन्तस्य — a heading: **मपर्यन्तस्येत्ययम् "
            "अधिकारः। यदित ऊर्ध्वम् अनुक्रमिष्यामो "
            "मपर्यन्तस्येत्येवं तद् वेदितव्यम्** — every "
            "substitute from here replaces only so much of "
            "युष्मद् and अस्मद् as reaches their म्.\\n\\n"
            "**AND IT DOES TWO DIFFERENT JOBS.** Without it "
            "7.2.92 would reach युवकाम् and 7.2.97 would replace "
            "the whole word, and then **त्वमयोर् अकारस्य योऽचि "
            "इति यकारे कृतेऽनिष्टं रूपं स्यात्**. The word पर्यन्त "
            "rather than a bare मान्त is for showing where the "
            "boundary falls, **अवधिद्योतनार्थम्**"),
    Before(
        "7.2.92", pairs=(("yuṣmad", "yuva"), ("asmad", "āva")),
        of=THE_TWO, part="ma-paryanta", number="dvivacana",
        why="युवावौ द्विवचने — where TWO are meant, युष्मद् and "
            "अस्मद् become युव and आव as far as their म्: "
            "**युवाम्, आवाम्; युवाभ्याम्, आवाभ्याम्; युवयोः, "
            "आवयोः**. **द्विवचने इत्यर्थग्रहणम्** — the word "
            "names the SENSE and not the ending, which is what "
            "gets अतियुवाम् and अतियुवान् where the compound's "
            "own number is different"),
    Before(
        "7.2.93", pairs=(("yuṣmad", "yūya"), ("asmad", "vaya")),
        of=THE_TWO, part="ma-paryanta", before=("jas",),
        why="यूयवयौ जसि — before जस् they become यूय and वय: "
            "**यूयम्, वयम्; परमयूयम्, परमवयम्; अतियूयम्, "
            "अतिवयम्** — and the rule reaches a compound ending "
            "in them"),
    Before(
        "7.2.94", pairs=(("yuṣmad", "tva"), ("asmad", "aha")),
        of=THE_TWO, part="ma-paryanta", before=("su",),
        why="त्वाहौ सौ — before सु they become त्व and अह: "
            "**त्वम्, अहम्; परमत्वम्, परमाहम्; अतित्वम्, "
            "अत्यहम्**"),
    Before(
        "7.2.95", pairs=(("yuṣmad", "tubhya"), ("asmad", "mahya")),
        of=THE_TWO, part="ma-paryanta", before=("ṅayi",),
        why="तुभ्यमह्यौ ङयि — before ङे they become तुभ्य and "
            "मह्य: **तुभ्यम्, मह्यम्; परमतुभ्यम्, परममह्यम्; "
            "अतितुभ्यम्, अतिमह्यम्**. The ending itself has "
            "already become अम् by 7.1.28, so what is left for "
            "this rule is the stem in front of it"),
    Before(
        "7.2.96", pairs=(("yuṣmad", "tava"), ("asmad", "mama")),
        of=THE_TWO, part="ma-paryanta", before=("ṅasi-ṣaṣṭhī",),
        why="तवममौ ङसि — before the genitive singular they become "
            "तव and मम: **तव, मम; परमतव, परममम**. The ङसि of "
            "the sūtra is the SIXTH case's ending and not the "
            "fifth's, which 7.1.32 had already turned into अत् "
            "for these same two words"),
    Before(
        "7.2.97", pairs=(("yuṣmad", "tva"), ("asmad", "ma")),
        of=THE_TWO, part="ma-paryanta", number="ekavacana",
        why="त्वमावेकवचने — and where ONE is meant they become "
            "त्व and म: **त्वाम्, माम्, त्वया, मया, त्वत्, मत्, "
            "त्वयि, मयि**. Again a sense and not an ending, so "
            "अतित्वाम् and अतित्वान् come out where the "
            "compound's number is another; and where the "
            "ending-specific substitutes of 7.2.94–96 also "
            "reach, those win by prior contradiction"),
    Before(
        "7.2.98", pairs=(("yuṣmad", "tva"), ("asmad", "ma")),
        of=THE_TWO, part="ma-paryanta", number="ekavacana",
        before=("pratyaya", "uttarapada"), blocks=("7.2.90",),
        keeps_out="युष्मदीयम्, अस्मदीयम्, युष्मत्पुत्रः — more "
                  "than one is meant",
        why="प्रत्ययोत्तरपदयोश्च — and before an AFFIX or a "
            "second compound member, still where one is meant: "
            "**त्वदीयः, मदीयः; त्वत्तरः, मत्तरः; त्वद्यति, "
            "मद्यति; त्वत्पुत्रः, मत्पुत्रः; त्वन्नाथः, "
            "मन्नाथः**. The विभक्ति heading had confined the "
            "sūtra before to case endings; **ततोऽन्यत्रापि "
            "प्रत्यय उत्तरपदे च यथा स्याद् इत्ययम् आरम्भः**"),
    Before(
        "7.2.99", pairs=TRI_CATUR,
        of=tuple(one for one, _ in TRI_CATUR), gender="strī",
        before=("vibhakti",),
        keeps_out="त्रयः, चत्वारः, त्रीणि, चत्वारि — not feminine",
        why="त्रिचतुरोः स्त्रियां तिसृचतसृ — in the FEMININE त्रि "
            "and चतुर् become तिसृ and चतसृ before a case "
            "ending: **तिस्रः, चतस्रः, तिसृभिः, चतसृभिः**.\\n\\n"
            "**AND स्त्रियाम् QUALIFIES THE NUMERAL AND NOT THE "
            "STEM.** **तेन यदा त्रिचतुःशब्दौ स्त्रियाम्, अङ्गं "
            "तु लिङ्गान्तरे, तदाप्यादेशौ भवत एव** — so a "
            "masculine compound whose numeral is feminine still "
            "takes them: **प्रियतिसा ब्राह्मणः; प्रियतिसृ "
            "ब्राह्मणकुलम्**"),
    Before(
        "7.2.100", does="r", of=("tisṛ", "catasṛ"), part="ṛ",
        before=("ac-vibhakti",),
        keeps_out="तिसृभिः, चतसृभिः — a consonant-initial ending",
        why="अचि र ऋतः — and their ऋ becomes र before a "
            "vowel-initial case ending: **तिस्रस्तिष्ठन्ति, "
            "तिस्रः पश्य; चतस्रः पश्य; प्रियतिस्र आनय**. It "
            "displaces four things at once — "
            "**पूर्वसवर्णोत्त्वङिसर्वनामस्थानगुणानाम् अपवादः** — "
            "and beats the last two although they are later, "
            "**पूर्वविप्रतिषेधेन**"),
    Before(
        "7.2.101", does="jaras", of=("jarā",),
        before=("ac-vibhakti",), optional=True,
        keeps_out="जराभ्याम्, जराभिः — a consonant-initial ending",
        why="जराया जरसन्यतरस्याम् — जरा optionally becomes जरस् "
            "before a vowel-initial case ending: **जरसा दन्ताः "
            "शीर्यन्ते, जरया दन्ताः शीर्यन्ते; जरसे त्वा "
            "परिदद्युः, जरायै त्वा परिदद्युः**.\\n\\n"
            "**AND THE ORDER AGAINST TWO OTHER RULES IS WORKED "
            "OUT IN FULL.** In अतिजरसं ब्राह्मणकुलं three things "
            "want to happen at once — the ending's लुक्, its "
            "अम्, and this substitution. **लुक् तावद् "
            "अपवादत्वाद् अम्भावेन बाध्यते, अम्भावोऽपि परत्वाद् "
            "जरसादेशेन। न च पुनर् लुक्शास्त्रं प्रवर्तते, "
            "भ्रष्टावसरत्वात्** — the लुक् has missed its turn "
            "and does not come back"),
    Before(
        "7.2.102", does="a", of=TYADADI, before=("vibhakti",),
        keeps_out="भवान् — not one of the list; त्यद्, त्यदौ, "
                  "त्यदः — the pronoun is a name or subordinate, "
                  "**पाठाद् एव पर्युदस्ताः**",
        why="त्यदादीनामः — the त्यदादि stems take अ before a case "
            "ending: **स्यः, त्यौ, त्ये; सः, तौ, ते; यः, यौ, "
            "ये; एषः, एतौ, एते; अयम्, इमौ, इमे; असौ, अमू, अमी; "
            "द्वौ, द्वाभ्याम्**. The list is closed at द्वि — "
            "**द्विपर्यन्तानां त्यदादीनाम् अत्वम् इष्यते** — and "
            "a compound headed by one of them still takes it: "
            "**परमसः, परमतौ, परमते**"),
    Before(
        "7.2.103", does="ka", of=("kim",), before=("vibhakti",),
        why="किमः कः — किम् becomes क before a case ending: "
            "**कः, कौ, के**. And it reaches the form with कच् "
            "in it, **साकच्कस्याप्ययम् आदेशो भवति**, which is "
            "why the sūtra does not simply say किमोऽत्"),
    Before(
        "7.2.104", does="ku", of=("kim",),
        before=("ta-ādi-vibhakti", "ha-ādi-vibhakti"),
        blocks=("7.2.103",),
        why="कु तिहोः — before a त-initial and a ह-initial ending "
            "it becomes कु: **कुतः, कुत्र, कुह**. "
            "**तिहोरितीकार उच्चारणार्थः** — the इ is only there "
            "to say the sounds by"),
    Before(
        "7.2.105", does="kva", of=("kim",), before=("ati",),
        blocks=("7.2.103",),
        why="क्वाति — and before अति it becomes क्व: **क्व "
            "गमिष्यसि; क्व भोक्ष्यते**. A substitute is given "
            "rather than an affix so that 6.4.146's guṇa should "
            "not come — **आदेशान्तरवचनम् ओर्गुणनिवृत्त्यर्थम्**"),
    Before(
        "7.2.106", does="s", gana="tyadādi", part="an-antya-t-d",
        before=("su",),
        keeps_out="हे स, सा — the त् or द् IS last",
        why="तदोः सः सावनन्त्ययोः — a त् or द् of the त्यदादि "
            "that is not last becomes स् before सु: **स्यः, सः, "
            "एषः, असौ**"),
    Before(
        "7.2.107", does="au", of=("adas",), part="s",
        before=("su",), deletes_ending=True,
        why="अदस औ सुलोपश्च — अदस् takes औ for its स् AND the सु "
            "is deleted: **असौ**. Two operations in one "
            "sūtra.\\n\\n"
            "**AND TWO VERSES ASK WHY THE DELETION IS STATED.** "
            "**अदसः सोर् भवेद् औत्वं किं सुलोपो विधीयते।** — the "
            "answer is four rules that would have fired wrongly: "
            "the vocative's सु-loss wants a short vowel, आप् "
            "would take ए, a प्रत्ययस्थ क would give इ, and शी "
            "would come. Vārttikas add that with the औ refused "
            "for the कच्-form the स् takes उ instead — "
            "**असुकः, असकौ**"),
    Before(
        "7.2.108", does="m", of=("idam",), part="antya",
        before=("su",), blocks=("7.2.102",),
        why="इदमो मः — इदम् takes म् for its last sound before "
            "सु: **इयम्, अयम्**. A म् substituted for a म् — "
            "**इदमो मकारस्य मकारवचनं त्यदाद्यत्वबाधनार्थम्**, "
            "stated only to keep 7.2.102's अ out"),
    Before(
        "7.2.109", does="m", of=("idam",), part="d",
        before=("vibhakti",),
        why="दश्च — and its द् becomes म् before a case ending: "
            "**इमौ, इमे; इमम्, इमौ, इमान्**. The च carries "
            "इदमः down from the sūtra before while leaving its "
            "सौ behind, so this one reaches every ending and "
            "that one only the nominative singular"),
    Before(
        "7.2.110", does="y", of=("idam",), part="d",
        before=("su",), blocks=("7.2.109",),
        why="यः सौ — but before सु the द् becomes य्: **इयम्**. "
            "And it is the FEMININE that keeps it, the sūtra "
            "after this one naming the masculine — **उत्तरसूत्रे "
            "पुंसीति वचनात् स्त्रियामयं यकारः**"),
    Before(
        "7.2.111", does="ay", of=("idam",), part="id",
        before=("su",), gender="puṃs", blocks=("7.2.110",),
        keeps_out="इयं ब्राह्मणी — the feminine, where 7.2.110 "
                  "stands",
        why="इदोऽय् पुंसि — and in the MASCULINE the इद् of इदम् "
            "becomes अय् before सु: **अयं ब्राह्मणः**. Two "
            "sūtras for one ending, divided by gender, and it "
            "is this one's पुंसि that tells the reader the "
            "य् of the sūtra before belongs to the feminine — "
            "**उत्तरसूत्रे पुंसीति वचनात् स्त्रियामयं यकारः**"),
    Before(
        "7.2.112", does="an", of=("idam",), part="id",
        before=("āp-vibhakti",),
        keeps_out="इमकेन, इमकयोः — a क stands in the word",
        why="अनाप्यकः — the इद् of इदम् becomes अन् before the "
            "आप् endings, unless a क stands in it: **अनेन, "
            "अनयोः**. **आपीति प्रत्याहारः तृतीयैकवचनात् प्रभृति "
            "सुपः पकारेण** — a प्रत्याहार made on the spot, from "
            "the instrumental singular to the last ending"),
    Before(
        "7.2.113", does="lopa", of=("idam",), part="id",
        before=("hal-vibhakti",),
        why="हलि लोपः — and it is dropped before a "
            "consonant-initial case ending: **आभ्याम्, एभिः, "
            "एभ्यः, एषाम्, एषु**.\\n\\n"
            "**AND WHETHER THE WHOLE इद् GOES OR ONLY ITS इ IS "
            "ANSWERED TWO WAYS.** **नानर्थकेऽलोन्त्यविधिः इति "
            "सर्वस्यायम् इद्रूपस्य लोपः** — the maxim about a "
            "meaningless string makes it the whole; **अथ वा "
            "नायम् इल्लोपः। अनाप्यकः इत्यन्ग्रहणम् "
            "अनुवर्तते**, or else the अन् of the sūtra before is "
            "carried down and there is nothing to argue about. "
            "This closes the विभक्ति heading"),
)


def _reaches(row: Before, stem: str, gana: str, before: str,
             part: str, number: str, gender: str) -> bool:
    if row.heading and not row.of:
        return False
    if row.pairs and stem and stem not in dict(row.pairs):
        return False
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.part and part and part != row.part:
        return False
    if row.number and number != row.number:
        return False
    if row.gender and gender != row.gender:
        return False
    return True


def _becomes(row: Before, stem: str) -> str:
    """The substitute, where the rule matches one to one."""
    for named, shape in row.pairs:
        if named == stem:
            return shape
    return row.does


def _how_specific(row: Before, stem: str, gana: str,
                  part: str) -> int:
    """
    A rule that names what it displaces beats it, a named part
    beats a bare stem, and a named gender or number beats both.

    7.2.108–113 are the six that need it: all name इदम्, and
    they are told apart only by which piece of it they replace
    and what follows.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of and stem in row.of)
        + 6 * bool(row.gender)
        + 6 * bool(row.number)
        + 5 * bool(row.part and part and part == row.part)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.before)
        - 6 * bool(row.heading)
    )


@dataclass(frozen=True)
class Shaped:
    """What the run answers: the stem's new shape, or its loss."""

    does: str
    sutra: str
    why: str
    deletes_ending: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_ending(stem: str = "", *, gana: str = "",
                  before: str = "", part: str = "",
                  number: str = "", gender: str = "",
                  wants: str = "") -> Shaped:
    """
    7.2.79–113 — what the stem becomes before an ending.

    Nothing answers by default. वृक्ष and अग्नि go into every
    case unchanged, and this run is the pronouns and the handful
    of stems that do not.
    """
    matched = [
        row for row in BEFORE_TABLE
        if _reaches(row, stem, gana, before, part, number, gender)
        and (not wants or wants == _becomes(row, stem))
    ]
    if not matched:
        return Shaped(
            "", "", "No rule of 7.2.79-113 is reached, so the "
                    "stem goes in as it is")
    row = max(matched,
              key=lambda one: _how_specific(one, stem, gana, part))
    return Shaped(_becomes(row, stem), row.sutra, row.why,
                  deletes_ending=row.deletes_ending,
                  optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Before, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in BEFORE_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Before", "BEFORE_TABLE", "BEFORE_RUN", "VIBHAKTI_FROM",
    "VIBHAKTI_TO", "MAPARYANTA_FROM", "THE_TWO",
    "PRONOUN_PAIRS", "TRI_CATUR", "TYADADI", "Shaped",
    "before_ending", "provisions_for",
]
