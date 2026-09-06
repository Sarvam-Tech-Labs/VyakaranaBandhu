# -*- coding: utf-8 -*-
"""
६.४.१–२१ — अङ्गस्य, and the first things done to a stem.

6.4.1 अङ्गस्य opens the longest heading in the Aṣṭādhyāyī. Its own
vṛtti says how far: **अधिकारोऽयम् आ सप्तमाध्यायपरिसमाप्तेः** — to
the END OF ADHYĀYA 7, six hundred and thirteen sūtras, every one
of them read as being about the अङ्ग, the stem an affix attaches
to. Nothing else in the grammar governs a quarter of it.

**AND THE HEADING IS ITS OWN COUNTER-EXAMPLE THREE TIMES OVER.**
The vṛtti does not merely state the scope; it takes the next three
rules that will use it and shows what falls outside each:
**हलः — हूतः; अङ्गस्येति किम्? निरुतम्। नामि दीर्घः — अग्नीनाम्;
अङ्गस्येति किम्? क्रिमिणां पश्य। अतो भिस ऐस् — वृक्षैः;
अङ्गस्येति किम्?** — one from this pāda, one from the next, one
from 7.1.

Under it, twenty-one rules and two operations. Seventeen lengthen
a vowel — before नाम्, before a सर्वनामस्थान, before सन्, before
क्त्वा — and the last three replace छ् and व् with श् and ऊठ्:
प्रश्नः, स्योनः, जूः, मूः.

**AND ONE RULE IS STATED ONLY TO BE REFUSED, AND THE REFUSAL IS
WHAT TEACHES.** 6.4.4 न तिसृचतसृ stops 6.4.3's lengthening, and
**इदम् एव नामीति दीर्घप्रतिषेधवचनं ज्ञापकम् — अचि र ऋतः
इत्येतस्मात् पूर्वविप्रतिषेधेन नुडागमो भवतीति**: the refusal only
makes sense if the नुट् got there first, so the refusal proves the
order.

**WHAT THIS MODULE DOES NOT DO.** It reports whether the stem
lengthens or takes a substitute, and by which rule. It does not
identify the stem: that तिसृ has an ऋ to lengthen, or that प्रच्छ्
has a छ् under a तुक्, is what the query says.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: The longest heading in the grammar: **अधिकारोऽयम् आ
#: सप्तमाध्यायपरिसमाप्तेः**.
ANGA_RUN: Tuple[str, str] = ("6.4.1", "7.4.97")

#: And this module's own stretch inside it, closing where 6.4.22
#: असिद्धवत् opens a heading of a different kind.
DIRGHA_RUN: Tuple[str, str] = ("6.4.1", "6.4.21")

#: 6.4.11's list — one affix, one class, and eight kinship and
#: priestly words, all lengthening their penult before a
#: सर्वनामस्थान.
APTRN_LIST: Tuple[str, ...] = (
    "ap", "tṛn", "tṛc", "svasṛ", "naptṛ", "neṣṭṛ", "tvaṣṭṛ",
    "kṣattṛ", "hotṛ", "potṛ", "praśāstṛ")

#: 6.4.12–13's four, whose lengthening 6.4.12 turns into a नियम:
#: **इन्हन्पूषार्यम्णाम् उपधायाः शावेव दीर्घो भवति नान्यत्र**.
IN_HAN_FOUR: Tuple[str, ...] = ("in", "han", "pūṣan", "aryaman")

#: 6.4.20's five, in which व् AND the penult together become ऊठ्.
JVARADI: Tuple[str, ...] = ("jvar", "tvar", "sriv", "av", "mav")

#: What 6.3.137 अन्येषामपि दृश्यते is called on to cover here:
#: **स्वर्गं लोकं समजिगांसद् इति छन्दसि यद् अनिङादेशस्यापि
#: दीर्घत्वं दृश्यते, तद् अन्येषामपि दृश्यते इत्यनेन भवति**.
LEANS_ON_6_3_137: str = "6.3.137"


@dataclass(frozen=True)
class AngaDirgha:
    """One rule of 6.4.1–21: what is done to the stem."""

    sutra: str
    #: dīrgha; or the substitute — śa, ūṭh, ūḍ, lopa.
    does: str = ""
    #: The stems the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of stem instead.
    gana: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: What part of the stem is affected — upadhā, saṃprasāraṇa,
    #: cha-va.
    part: str = ""
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    #: A नियम: the operation was already available and the rule
    #: fences where.
    niyama: bool = False
    nipatana: bool = False
    heading: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ANGA_DIRGHA_TABLE: Tuple[AngaDirgha, ...] = (
    AngaDirgha(
        "6.4.1", heading=True,
        why="अङ्गस्य — **अधिकारोऽयम् आ सप्तमाध्यायपरिसमाप्तेः। "
            "यदित ऊर्ध्वम् अनुक्रमिष्यामोऽङ्गस्येत्येवं तद् "
            "वेदितव्यम्** — every rule from here to the end of "
            "adhyāya 7 is about the अङ्ग, the stem an affix "
            "attaches to. Six hundred and thirteen sūtras under "
            "one word, and nothing else in the grammar governs a "
            "quarter of it.\\n\\n"
            "**AND THE VṚTTI PROVES THE SCOPE THREE TIMES, FROM "
            "THREE DIFFERENT PLACES.** It takes the next rule that "
            "will use the heading, then one from further on, then "
            "one from the adhyāya after: **वक्ष्यति हलः — हूतः, "
            "जीनः, संवीतः। अङ्गस्येति किम्? निरुतम्, दुरुतम्**; "
            "**नामि दीर्घः — अग्नीनाम्, वायूनाम्। अङ्गस्येति "
            "किम्? क्रिमिणां पश्य, पामनां पश्य**; **अतो भिस ऐस् — "
            "वृक्षैः, प्लक्षैः। अङ्गस्येति किम्?** Each pair shows "
            "the same operation applying and not applying, and the "
            "only difference is whether what it would act on is an "
            "अङ्ग"),
    AngaDirgha(
        "6.4.2", does="dīrgha", part="saṃprasāraṇa",
        result=("hal-pūrva",), excludes=("aṇ-anya",),
        keeps_out="उतः, उतवान् — no consonant before the "
                  "vocalisation; निरुतम्, दुरुतम् — the हल् is not "
                  "part of the stem; विद्धः, विचितः — the "
                  "vocalisation is not at the stem's end; "
                  "तृतीयः — by निपातन",
        why="हलः — a stem whose संप्रसारण stands at its END and "
            "after a CONSONANT of the stem lengthens: **हूतः, "
            "जीनः, संवीतः**.\\n\\n"
            "**AND अङ्गस्य HAS TO BE READ TWICE INTO IT.** "
            "**अङ्गग्रहणम् आवर्तयितव्यं हल्विशेषणार्थम्, "
            "अङ्गकार्यप्रतिपत्त्यर्थं च** — once to say the "
            "consonant is the stem's, and once to say the "
            "lengthening is. निरुतम् has a consonant before the "
            "उ, but it is the preverb's"),
    AngaDirgha(
        "6.4.3", does="dīrgha", before=("nām",),
        keeps_out="क्रिमिणां पश्य, पामनां पश्य — the नाम् is not "
                  "after an अङ्ग; चर्मणाम् — the penult, which "
                  "6.4.7 wants and this rule does not reach",
        why="नामि — a stem lengthens before नाम्, the genitive "
            "plural with its नुट् already in: **अग्नीनाम्, "
            "वायूनाम्, कर्तॄणाम्, हर्तॄणाम्**. **नामित्येतत् "
            "षष्ठीबहुवचनम् आगतनुट्कं गृह्यते**, and 6.4.2's अण् "
            "is dropped here — **अण इत्येतद् अत्र निवृत्तम्**.\\n\\n"
            "**AND THE नुट् HAS TO BE THERE FIRST, WHICH IS A "
            "CIRCLE THE VṚTTI BREAKS BY VERSE.** **नामि दीर्घ आमि "
            "चेत् स्यात् कृते दीर्घे न नुड् भवेत्। वचनाद् यत्र "
            "तन् नास्ति नोपधायाश्च चर्मणाम्** — if the rule spoke "
            "of आम् rather than नाम्, the lengthening would happen "
            "first and 7.1.54 would then have no short vowel to "
            "put a नुट् after. Naming the नुट् in the condition is "
            "what fixes the order"),
    AngaDirgha(
        "6.4.4", refuses=True, of=("tisṛ", "catasṛ"),
        before=("nām",), blocks=("6.4.3",),
        why="न तिसृचतसृ — but तिसृ and चतसृ do not lengthen there: "
            "**तिसृणाम्, चतसृणाम्**.\\n\\n"
            "**AND THE REFUSAL IS WHAT PROVES AN ORDER ELSEWHERE.** "
            "**इदम् एव नामीति दीर्घप्रतिषेधवचनं ज्ञापकम् — अचि र "
            "ऋतः इत्येतस्मात् पूर्वविप्रतिषेधेन नुडागमो भवतीति** "
            "— refusing the lengthening only makes sense if there "
            "is a नुट् for it to have applied after, so 7.1.54 must "
            "beat 7.2.100 by पूर्वविप्रतिषेध. A rule that supplies "
            "nothing and settles something"),
    AngaDirgha(
        "6.4.5", does="dīrgha", of=("tisṛ", "catasṛ"),
        before=("nām",), chandasi=True, optional=True,
        blocks=("6.4.4",),
        why="छन्दस्युभयथा — and in the Veda BOTH ways are seen: "
            "**तिसृणां मध्यन्दिने** beside **तिसृणां मध्यदिने**; "
            "**चतसृणां मध्यदिने** twice over. **उभयथा दृश्यते, "
            "दीर्घश्चादीर्घश्च** — the option undoes the refusal "
            "of the sūtra before, and only in the Veda"),
    AngaDirgha(
        "6.4.6", does="dīrgha", of=("nṛ",), before=("nām",),
        optional=True,
        why="नृ च — and नृ goes both ways: **त्वं नृणां नृपते** "
            "with the long vowel and with the short.\\n\\n"
            "**AND WHETHER IT IS VEDIC IS DISPUTED.** **केचिद् "
            "अत्र छन्दसीति नानुवर्तयन्ति। तेन भाषायाम् अपि "
            "विकल्पो भवति** — some do not read छन्दसि down from "
            "6.4.5, and on their reading the option holds outside "
            "the Veda too. The vṛtti records the disagreement "
            "without settling it"),
    AngaDirgha(
        "6.4.7", does="dīrgha", part="upadhā", before=("nām",),
        result=("n-anta",),
        keeps_out="चतुर्णाम् — चतुर् does not end in न्; चर्मणाम् "
                  "— it does, and the नाम् is there, so this is "
                  "one the verse at 6.4.3 had to account for",
        why="नोपधायाः — a stem ending in न् lengthens its PENULT "
            "before नाम्: **पञ्चानाम्, सप्तानाम्, नवानाम्, "
            "दशानाम्**. 6.4.3 lengthened the final; this lengthens "
            "the vowel before the न्, which is why both rules are "
            "needed and neither displaces the other"),
    AngaDirgha(
        "6.4.8", does="dīrgha", part="upadhā",
        before=("sarvanāmasthāna",), result=("n-anta",),
        excludes=("sambuddhi",),
        keeps_out="राजनि, सामनि — not a सर्वनामस्थान; हे राजन्, "
                  "हे तक्षन् — a vocative singular, which the "
                  "sūtra shuts out",
        why="सर्वनामस्थाने चासम्बुद्धौ — and before a "
            "सर्वनामस्थान, the vocative singular excepted: "
            "**राजा, राजानौ, राजानः; राजानम्; सामानि तिष्ठन्ति, "
            "सामानि पश्य**. This is the rule that makes राजा out "
            "of राजन्, and it is the same lengthening 6.4.7 gave "
            "before नाम्, now before a different set of endings"),
    AngaDirgha(
        "6.4.9", does="dīrgha", part="upadhā",
        before=("sarvanāmasthāna",), result=("ṣa-pūrva", "nigama"),
        excludes=("sambuddhi",), optional=True, blocks=("6.4.8",),
        keeps_out="तक्षा, तक्षाणौ, तक्षाणः — outside the Veda, "
                  "where 6.4.8 is compulsory",
        why="वा षपूर्वस्य निगमे — but where a ष् stands before the "
            "vowel, the lengthening is OPTIONAL in the Veda: "
            "**स तक्षाणं तिष्ठन्तम् अब्रवीत्** beside **स तक्षणं "
            "तिष्ठन्तम् अब्रवीत्**; **ऋभुक्षाणम् इन्द्रम्** "
            "beside **ऋभुक्षणम् इन्द्रम्**"),
    AngaDirgha(
        "6.4.10", does="dīrgha", part="upadhā", of=("mahat",),
        gana="sānta-saṃyoga", before=("sarvanāmasthāna",),
        excludes=("sambuddhi",),
        keeps_out="हे श्रेयन्, हे महन् — a vocative singular",
        why="सान्तमहतः संयोगस्य — and the न् of a cluster ending "
            "in स्, and महत्, lengthen their penult before a "
            "सर्वनामस्थान: **श्रेयान्, श्रेयांसौ, श्रेयांसः; "
            "श्रेयांसि, पयांसि, यशांसि**; and **महान्, महान्तौ, "
            "महान्तः**. The rule 6.3.46 had made महा of महत् "
            "before a second member; this makes महान् of it before "
            "an ending"),
    AngaDirgha(
        "6.4.11", does="dīrgha", part="upadhā", of=APTRN_LIST,
        before=("sarvanāmasthāna",), excludes=("sambuddhi",),
        why="अप्तृन्तृच्स्वसृनप्तृनेष्टृत्वष्टृक्षत्तृहोतृपोतृ"
            "प्रशास्तॄणाम् — eleven more lengthen their penult "
            "before a सर्वनामस्थान: **आपः** for अप्; **कर्तारौ "
            "कटान्, वदितारौ जनापवादान्** for तृन्; and the eight "
            "kinship and priestly words.\\n\\n"
            "**AND अप् NEEDS TWO PARIBHĀṢĀS TO COME OUT RIGHT.** "
            "**बह्वाम्पि तडागानीति केचिद् इच्छन्ति। तत्र "
            "समासान्तो विधिरनित्यः इति समासान्तो न क्रियते। "
            "नित्यम् अपि च नुमम् अकृत्वा दीर्घत्वम् इष्यते** — the "
            "समासान्त is left off because it is not compulsory, "
            "and the नुम् is held back although it is"),
    AngaDirgha(
        "6.4.12", does="dīrgha", part="upadhā", gana="in-han-four",
        before=("śi",), niyama=True,
        keeps_out="दण्डिनौ, छत्रिणौ, वृत्रहणौ, पूषणौ, अर्यमणौ — "
                  "before any other सर्वनामस्थान, and the "
                  "lengthening is fenced off",
        why="इन्हन्पूषार्यम्णां शौ — stems in इन्, हन्, पूषन् and "
            "अर्यमन् lengthen their penult before शि: "
            "**बहुदण्डीनि, बहुच्छत्राणि, बहुवृत्रहाणि, "
            "बहुभ्रूणहानि, बहुपूषाणि, बह्वर्यमाणि**.\\n\\n"
            "**AND THE RULE GRANTS NOTHING — IT FENCES.** "
            "**सिद्धे सत्यारम्भो नियमार्थः — इन्हन्पूषार्यम्णाम् "
            "उपधायाः शावेव दीर्घो भवति नान्यत्र** — 6.4.8 had "
            "already reached them before every सर्वनामस्थान. "
            "Saying शौ restricts it to that one, and the "
            "counter-examples are the other endings"),
    AngaDirgha(
        "6.4.13", does="dīrgha", part="upadhā", gana="in-han-four",
        before=("su",), excludes=("sambuddhi",), blocks=("6.4.12",),
        keeps_out="हे दण्डिन्, हे वृत्रहन्, हे पूषन्, हे अर्यमन् "
                  "— a vocative singular",
        why="सौ च — and before सु, the vocative singular excepted: "
            "**दण्डी, वृत्रहा, पूषा, अर्यमा**. Stated because "
            "6.4.12's नियम had just shut every ending but शि out, "
            "and सु has to be let back in"),
    AngaDirgha(
        "6.4.14", does="dīrgha", part="upadhā",
        gana="atu-as-anta", before=("su",),
        excludes=("sambuddhi", "dhātu"),
        keeps_out="पिण्डग्रः, चर्मवः — these end in अस् and are "
                  "roots, which the sūtra shuts out",
        why="अत्वसन्तस्य चाधातोः — a stem ending in अतु or अस्, "
            "and not a root, lengthens its penult before सु: "
            "**भवान्** (डवतु), **कृतवान्** (क्तवतु), **गोमान्, "
            "यवमान्** (मतुप्); and **सुपयाः, सुयशाः, सुस्रोताः** "
            "for अस्.\\n\\n"
            "**AND THE LENGTHENING HAS TO HAPPEN BEFORE THE नुम् "
            "DOES.** **अत्र कृते दीर्घे नुमागमः कर्तव्यः। यदि हि "
            "परत्वाद् नित्यत्वात् च नुम् स्यात्, दीर्घस्य निमित्तम् "
            "अजुपधा विहन्येत** — the नुम् is both later and "
            "compulsory and would ordinarily go first; if it did, "
            "the penult would no longer be a vowel and this rule "
            "would have nothing to act on"),
    AngaDirgha(
        "6.4.15", does="dīrgha", part="upadhā",
        gana="anunāsika-anta", before=("kvip", "jhal"),
        result=("kṅit",),
        keeps_out="ओदनपक्, पक्वः, पक्ववान् — no nasal at the end; "
                  "गम्यते, रम्यते — neither क्विप् nor a झल्; "
                  "गन्ता, रन्ता — the affix is neither कित् nor "
                  "ङित्",
        why="अनुनासिकस्य क्विझलोः क्ङिति — a nasal-final stem "
            "lengthens its penult before क्विप्, and before a "
            "झल्-initial कित् or ङित्: **प्रशान्, प्रतान्** for "
            "क्विप्; **शान्तः, शान्तवान्, शान्त्वा, शान्तिः** for "
            "the कित्; **शंशान्तः, तन्तान्तः** for the ङित्, "
            "these last **यङ्लुगन्तात्**"),
    AngaDirgha(
        "6.4.16", does="dīrgha", gana="ac-anta",
        of=("han", "gam"), before=("san",), result=("jhal-ādi",),
        keeps_out="संजिगंसते वत्सो मात्रे — गम् without the इङ् "
                  "substitute, by the vārttika "
                  "**गमेरिङादेशस्येति वक्तव्यम्**",
        why="अज्झनगमां सनि — a vowel-final stem, and हन् and गम्, "
            "lengthen before सन् beginning with a झल्: "
            "**विवीषति, तुष्टूषति, चिकीर्षति, जिहीर्षति**; "
            "**जिघांसति** for हन्; **अधिजिगांसते** for गम्.\\n\\n"
            "**AND THE VEDIC FORM THAT BREAKS THE VĀRTTIKA IS "
            "SENT TO ANOTHER RULE.** **स्वर्गं लोकं समजिगांसद् "
            "इति छन्दसि यद् अनिङादेशस्यापि दीर्घत्वं दृश्यते, तद् "
            "अन्येषामपि दृश्यते इत्यनेन भवति** — 6.3.137, the "
            "catch-all of the pāda before, is what covers it"),
    AngaDirgha(
        "6.4.17", does="dīrgha", of=("tan",), before=("san",),
        result=("jhal-ādi",), optional=True,
        keeps_out="तितनिषति — the सन् has an इट् and no longer "
                  "begins with a झल्",
        why="तनोतेर्विभाषा — and तन् lengthens before सन् "
            "OPTIONALLY: **तितांसति / तितंसति**. The इट् that "
            "makes the third form comes from a vārttika: "
            "**सनीवन्तर्ध० इत्यत्र तनोतेर् उपसंख्यानाद् इडागमो "
            "भवति विकल्पेन**"),
    AngaDirgha(
        "6.4.18", does="dīrgha", part="upadhā", of=("kram",),
        before=("ktvā",), result=("jhal-ādi",), optional=True,
        keeps_out="क्रमित्वा — the क्त्वा has an इट्; प्रक्रम्य, "
                  "उपक्रम्य — a ल्यप् and not a क्त्वा",
        why="क्रमश्च क्त्वि — क्रम् lengthens its penult "
            "optionally before क्त्वा beginning with a झल्: "
            "**क्रन्त्वा / क्रान्त्वा**.\\n\\n"
            "**AND THE ल्यप् FORMS ARE OUT BY A PARIBHĀṢĀ ABOUT "
            "ORDER.** **प्रक्रम्य, उपक्रम्येति बहिरङ्गोऽपि "
            "ल्यबादेशोऽन्तरङ्गानपि विधीन् बाधते इति पूर्वम् एव "
            "दीर्घत्वं न प्रवर्तते** — the ल्यप् substitution is "
            "outer and still goes first, so there is no क्त्वा "
            "left for this rule to act before"),
    AngaDirgha(
        "6.4.19", does="śa-ūṭh", part="cha-va",
        before=("anunāsika", "kvip", "jhal"), result=("kṅit",),
        why="छ्वोः शूडनुनासिके च — छ् becomes श् and व् becomes "
            "ऊठ्, matched one to one, before a nasal-initial "
            "affix, before क्विप्, and before a झल्-initial कित् "
            "or ङित्: **प्रश्नः, विश्नः** for the छ्; **स्योनः** "
            "for the व्.\\n\\n"
            "**AND EACH OF THE TWO NEEDS A DIFFERENT ORDER "
            "ARGUMENT.** **अन्तरङ्गत्वाच् छे च इति तुकि कृते "
            "सतुक्कस्य शादेशः** — 6.1.73's तुक् is inner and goes "
            "first, so what श् replaces is छ् WITH its तुक्. And "
            "for the other: **सिवेर् औणादिके नप्रत्यये "
            "लघूपधगुणात् पूर्वम् ऊठ् क्रियते** — the ऊठ् is put in "
            "before the guṇa would have been"),
    AngaDirgha(
        "6.4.20", does="ūḍ", part="va-upadhā", of=JVARADI,
        before=("kvip", "anunāsika", "jhal"), result=("kṅit",),
        why="ज्वरत्वरस्रिव्यविमवामुपधायाश्च — in five stems the "
            "व् AND the penult together become ऊठ्: **जूः, जूरौ, "
            "जूरः; जूर्तिः**; **तूः, तूर्तिः**; **स्रूः, स्रूतः, "
            "स्रूतिः**; **ऊः, ऊतिः**; **मूः, मूतिः**.\\n\\n"
            "**AND THE PENULT IS NOT ON THE SAME SIDE OF THE व् IN "
            "ALL FIVE.** **ज्वरत्वरोर् उपधा वकारात् परा, "
            "स्रिव्यवमवां पूर्वा** — in ज्वर् and त्वर् it follows "
            "the व्, in the other three it precedes. One "
            "substitute for two sounds, and which two depends on "
            "the stem"),
    AngaDirgha(
        "6.4.21", does="lopa", part="cha-va", result=("r-pūrva",),
        before=("kvip", "jhal"),
        why="राल्लोपः — after a र्, the छ् and the व् are simply "
            "DROPPED instead: **मूः, मुरौ, मुरः; मूर्तः, "
            "मूर्तिः** from मुर्छ्; **हूः, हूर्णः, हूर्तिः** from "
            "हुर्छ्; **तूः, तूर्णः, तूर्तिः** from तुर्व्.\\n\\n"
            "**AND HERE THE छ् IS TAKEN WITHOUT ITS तुक्.** "
            "**राल्लोपे सतुक्कस्य छस्याभावात् केवलो गृह्यते** — "
            "the exact opposite of 6.4.19, where the तुक् had to "
            "be there first. A र् before the छ् means 6.1.73 never "
            "applied, so there is a bare छ् to drop"),
)


def _reaches(row: AngaDirgha, stem: str, gana: str, before: str,
             part: str, result: str, chandasi: bool) -> bool:
    if row.heading:
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
                         or result in row.excludes
                         or gana in row.excludes):
        return False
    return True


def _supplies(row: AngaDirgha, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.does and not row.refuses


def _how_specific(row: AngaDirgha, stem: str, gana: str) -> int:
    """
    A refusal beats what it refuses, a rule that undoes a refusal
    beats the refusal, and a named stem beats a named class.

    6.4.3, 6.4.4 and 6.4.5 are all three at once: the first
    lengthens before नाम्, the second refuses it for two stems,
    and the third gives it back to those same two in the Veda. So
    the score has to weigh `blocks` as well as `refuses`, or the
    Vedic form is unreachable.
    """
    # `blocks` on a REFUSAL records what it refuses, and the
    # refusal is already weighed; counting both would make a
    # refusal doubly strong and unreachable past. On a supplying
    # rule it records what that rule displaces, and there it is
    # the only thing that can put it first.
    return (
        12 * (0 if row.refuses else len(row.blocks))
        + 10 * bool(row.refuses)
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.part)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Done:
    """What the run answers: an operation, and by which rule."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    niyama: bool = False
    blocked_by: Tuple[str, ...] = ()


def to_the_stem(stem: str = "", *, gana: str = "",
                before: str = "", part: str = "",
                result: str = "", chandasi: bool = False,
                wants: str = "") -> Done:
    """
    6.4.1–21 — what happens to the stem before the affix.

    Nothing answers by default: where no rule is reached the stem
    stands as it is, with the length and the sounds it had.
    """
    matched = [
        row for row in ANGA_DIRGHA_TABLE
        if _reaches(row, stem, gana, before, part, result, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Done(
            "", "", "No rule of 6.4.1–21 is reached, so the stem "
                    "stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Done("" if row.refuses else row.does, row.sutra, row.why,
                optional=row.optional, niyama=row.niyama,
                blocked_by=row.blocks)


def anga_runs() -> Done:
    """
    How far 6.4.1's one word reaches: **अधिकारोऽयम् आ
    सप्तमाध्यायपरिसमाप्तेः**.
    """
    return Done(
        "", ANGA_RUN[0],
        "अङ्गस्य governs %s–%s — to the end of adhyāya 7, the "
        "longest heading in the grammar. This module covers "
        "%s–%s of it, closing where %s असिद्धवत् opens a heading "
        "of a different kind"
        % (ANGA_RUN[0], ANGA_RUN[1], DIRGHA_RUN[0], DIRGHA_RUN[1],
           "6.4.22"))


def provisions_for(sutra_id: str) -> Tuple[AngaDirgha, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ANGA_DIRGHA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "AngaDirgha", "ANGA_DIRGHA_TABLE", "ANGA_RUN", "DIRGHA_RUN",
    "APTRN_LIST", "IN_HAN_FOUR", "JVARADI", "LEANS_ON_6_3_137",
    "Done", "to_the_stem", "anga_runs", "provisions_for",
]
