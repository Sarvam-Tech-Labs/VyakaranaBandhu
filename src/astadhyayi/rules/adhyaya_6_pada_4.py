# -*- coding: utf-8 -*-
"""
अध्याय ६, पाद ४ — अङ्गस्य, the stem an affix attaches to.

6.4.1 opens the longest heading in the Aṣṭādhyāyī. Its vṛtti gives
the bound in one line — अधिकारोऽयम् आ सप्तमाध्यायपरिसमाप्तेः — so
every rule from here to the end of adhyāya 7 is read as being about
the stem. Six hundred and thirteen sūtras under one word.

Inside it, this pāda works through the stem operation by operation:
lengthening (6.4.1–21), then 6.4.22 असिद्धवत्, whose whole content
is that what follows is treated as not having happened, then the
loss of a न् (6.4.23–33), and then substitution after substitution.
"""

from __future__ import annotations

from src.astadhyayi.anga_dirgha import to_the_stem
from src.astadhyayi.anga_agama import augment_or_yan
from src.astadhyayi.abhyasa_lopa import in_the_perfect
from src.astadhyayi.bhasya import in_the_weak_stem
from src.astadhyayi.istha_prakrtibhava import before_istha
from src.astadhyayi.sarvadhatuka_lopa import before_sarvadhatuka
from src.astadhyayi.ardhadhatuka_lopa import before_ardhadhatuka
from src.astadhyayi.anunasika_lopa import the_nasal
from src.astadhyayi.nalopa import n_goes
from src.astadhyayi.asiddha import visible
from src.astadhyayi.anga import iyan_uvan
from src.astadhyayi.sources import register


_TO_THE_STEM = (
    'to_the_stem(stem, gana=..., before=..., part=..., '
    'result=..., chandasi=...) -> whether the stem lengthens or '
    'takes a substitute before the affix, and by which rule of '
    '6.4.1-21.'
)

register(
    '6.4.1',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — अङ्गस्य — **अधिकारोऽयम् आ सप्तमाध्यायपरिसमाप्तेः। यदित\n'
        '  ऊर्ध्वम् अनुक्रमिष्यामोऽङ्गस्येत्येवं तद् वेदितव्यम्** — every\n'
        '  rule from here to the end of adhyāya 7 is about the अङ्ग, the stem\n'
        '  an affix attaches to. Six hundred and thirteen sūtras under one\n'
        '  word, and nothing else in the grammar governs a quarter of it.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI PROVES THE SCOPE THREE TIMES, FROM THREE\n'
        '  DIFFERENT PLACES.** It takes the next rule that will use the\n'
        '  heading, then one from further on, then one from the adhyāya\n'
        '  after: **वक्ष्यति हलः — हूतः, जीनः, संवीतः। अङ्गस्येति किम्?\n'
        '  निरुतम्, दुरुतम्**; **नामि दीर्घः — अग्नीनाम्, वायूनाम्।\n'
        '  अङ्गस्येति किम्? क्रिमिणां पश्य, पामनां पश्य**; **अतो भिस ऐस् —\n'
        '  वृक्षैः, प्लक्षैः। अङ्गस्येति किम्?** Each pair shows the same\n'
        '  operation applying and not applying, and the only difference is\n'
        '  whether what it would act on is an अङ्ग'
    ),
)

register(
    '6.4.2',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — हलः — a stem whose संप्रसारण stands at its END and after a\n'
        '  CONSONANT of the stem lengthens: **हूतः, जीनः, संवीतः**.\n'
        '\n'
        'SETTLED — **AND अङ्गस्य HAS TO BE READ TWICE INTO IT.**\n'
        '  **अङ्गग्रहणम् आवर्तयितव्यं हल्विशेषणार्थम्,\n'
        '  अङ्गकार्यप्रतिपत्त्यर्थं च** — once to say the consonant is the\n'
        "  stem's, and once to say the lengthening is. निरुतम् has a\n"
        "  consonant before the उ, but it is the preverb's"
    ),
)

register(
    '6.4.3',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — नामि — a stem lengthens before नाम्, the genitive plural\n'
        '  with its नुट् already in: **अग्नीनाम्, वायूनाम्, कर्तॄणाम्,\n'
        '  हर्तॄणाम्**. **नामित्येतत् षष्ठीबहुवचनम् आगतनुट्कं गृह्यते**, and\n'
        "  6.4.2's अण् is dropped here — **अण इत्येतद् अत्र निवृत्तम्**.\n"
        '\n'
        'SETTLED — **AND THE नुट् HAS TO BE THERE FIRST, WHICH IS A CIRCLE\n'
        '  THE VṚTTI BREAKS BY VERSE.** **नामि दीर्घ आमि चेत् स्यात् कृते\n'
        '  दीर्घे न नुड् भवेत्। वचनाद् यत्र तन् नास्ति नोपधायाश्च चर्मणाम्**\n'
        '  — if the rule spoke of आम् rather than नाम्, the lengthening would\n'
        '  happen first and 7.1.54 would then have no short vowel to put a\n'
        '  नुट् after. Naming the नुट् in the condition is what fixes the\n'
        '  order'
    ),
)

register(
    '6.4.4',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — न तिसृचतसृ — but तिसृ and चतसृ do not lengthen there:\n'
        '  **तिसृणाम्, चतसृणाम्**.\n'
        '\n'
        'SETTLED — **AND THE REFUSAL IS WHAT PROVES AN ORDER ELSEWHERE.**\n'
        '  **इदम् एव नामीति दीर्घप्रतिषेधवचनं ज्ञापकम् — अचि र ऋतः\n'
        '  इत्येतस्मात् पूर्वविप्रतिषेधेन नुडागमो भवतीति** — refusing the\n'
        '  lengthening only makes sense if there is a नुट् for it to have\n'
        '  applied after, so 7.1.54 must beat 7.2.100 by पूर्वविप्रतिषेध. A\n'
        '  rule that supplies nothing and settles something'
    ),
)

register(
    '6.4.5',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — छन्दस्युभयथा — and in the Veda BOTH ways are seen:\n'
        '  **तिसृणां मध्यन्दिने** beside **तिसृणां मध्यदिने**; **चतसृणां\n'
        '  मध्यदिने** twice over. **उभयथा दृश्यते, दीर्घश्चादीर्घश्च** — the\n'
        '  option undoes the refusal of the sūtra before, and only in the\n'
        '  Veda'
    ),
)

register(
    '6.4.6',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — नृ च — and नृ goes both ways: **त्वं नृणां नृपते** with\n'
        '  the long vowel and with the short.\n'
        '\n'
        'SETTLED — **AND WHETHER IT IS VEDIC IS DISPUTED.** **केचिद् अत्र\n'
        '  छन्दसीति नानुवर्तयन्ति। तेन भाषायाम् अपि विकल्पो भवति** — some do\n'
        '  not read छन्दसि down from 6.4.5, and on their reading the option\n'
        '  holds outside the Veda too. The vṛtti records the disagreement\n'
        '  without settling it'
    ),
)

register(
    '6.4.7',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — नोपधायाः — a stem ending in न् lengthens its PENULT before\n'
        '  नाम्: **पञ्चानाम्, सप्तानाम्, नवानाम्, दशानाम्**. 6.4.3 lengthened\n'
        '  the final; this lengthens the vowel before the न्, which is why\n'
        '  both rules are needed and neither displaces the other'
    ),
)

register(
    '6.4.8',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — सर्वनामस्थाने चासम्बुद्धौ — and before a सर्वनामस्थान, the\n'
        '  vocative singular excepted: **राजा, राजानौ, राजानः; राजानम्;\n'
        '  सामानि तिष्ठन्ति, सामानि पश्य**. This is the rule that makes राजा\n'
        '  out of राजन्, and it is the same lengthening 6.4.7 gave before\n'
        '  नाम्, now before a different set of endings'
    ),
)

register(
    '6.4.9',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — वा षपूर्वस्य निगमे — but where a ष् stands before the\n'
        '  vowel, the lengthening is OPTIONAL in the Veda: **स तक्षाणं\n'
        '  तिष्ठन्तम् अब्रवीत्** beside **स तक्षणं तिष्ठन्तम् अब्रवीत्**;\n'
        '  **ऋभुक्षाणम् इन्द्रम्** beside **ऋभुक्षणम् इन्द्रम्**'
    ),
)

register(
    '6.4.10',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — सान्तमहतः संयोगस्य — and the न् of a cluster ending in स्,\n'
        '  and महत्, lengthen their penult before a सर्वनामस्थान: **श्रेयान्,\n'
        '  श्रेयांसौ, श्रेयांसः; श्रेयांसि, पयांसि, यशांसि**; and **महान्,\n'
        '  महान्तौ, महान्तः**. The rule 6.3.46 had made महा of महत् before a\n'
        '  second member; this makes महान् of it before an ending'
    ),
)

register(
    '6.4.11',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED —\n'
        '  अप्तृन्तृच्स्वसृनप्तृनेष्टृत्वष्टृक्षत्तृहोतृपोतृप्रशास्तॄणाम् —\n'
        '  eleven more lengthen their penult before a सर्वनामस्थान: **आपः**\n'
        '  for अप्; **कर्तारौ कटान्, वदितारौ जनापवादान्** for तृन्; and the\n'
        '  eight kinship and priestly words.\n'
        '\n'
        'SETTLED — **AND अप् NEEDS TWO PARIBHĀṢĀS TO COME OUT RIGHT.**\n'
        '  **बह्वाम्पि तडागानीति केचिद् इच्छन्ति। तत्र समासान्तो विधिरनित्यः\n'
        '  इति समासान्तो न क्रियते। नित्यम् अपि च नुमम् अकृत्वा दीर्घत्वम्\n'
        '  इष्यते** — the समासान्त is left off because it is not compulsory,\n'
        '  and the नुम् is held back although it is'
    ),
)

register(
    '6.4.12',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — इन्हन्पूषार्यम्णां शौ — stems in इन्, हन्, पूषन् and\n'
        '  अर्यमन् lengthen their penult before शि: **बहुदण्डीनि,\n'
        '  बहुच्छत्राणि, बहुवृत्रहाणि, बहुभ्रूणहानि, बहुपूषाणि,\n'
        '  बह्वर्यमाणि**.\n'
        '\n'
        'SETTLED — **AND THE RULE GRANTS NOTHING — IT FENCES.** **सिद्धे\n'
        '  सत्यारम्भो नियमार्थः — इन्हन्पूषार्यम्णाम् उपधायाः शावेव दीर्घो\n'
        '  भवति नान्यत्र** — 6.4.8 had already reached them before every\n'
        '  सर्वनामस्थान. Saying शौ restricts it to that one, and the\n'
        '  counter-examples are the other endings'
    ),
)

register(
    '6.4.13',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — सौ च — and before सु, the vocative singular excepted:\n'
        "  **दण्डी, वृत्रहा, पूषा, अर्यमा**. Stated because 6.4.12's नियम had\n"
        '  just shut every ending but शि out, and सु has to be let back in'
    ),
)

register(
    '6.4.14',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — अत्वसन्तस्य चाधातोः — a stem ending in अतु or अस्, and not\n'
        '  a root, lengthens its penult before सु: **भवान्** (डवतु),\n'
        '  **कृतवान्** (क्तवतु), **गोमान्, यवमान्** (मतुप्); and **सुपयाः,\n'
        '  सुयशाः, सुस्रोताः** for अस्.\n'
        '\n'
        'SETTLED — **AND THE LENGTHENING HAS TO HAPPEN BEFORE THE नुम्\n'
        '  DOES.** **अत्र कृते दीर्घे नुमागमः कर्तव्यः। यदि हि परत्वाद्\n'
        '  नित्यत्वात् च नुम् स्यात्, दीर्घस्य निमित्तम् अजुपधा विहन्येत** —\n'
        '  the नुम् is both later and compulsory and would ordinarily go\n'
        '  first; if it did, the penult would no longer be a vowel and this\n'
        '  rule would have nothing to act on'
    ),
)

register(
    '6.4.15',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — अनुनासिकस्य क्विझलोः क्ङिति — a nasal-final stem lengthens\n'
        '  its penult before क्विप्, and before a झल्-initial कित् or ङित्:\n'
        '  **प्रशान्, प्रतान्** for क्विप्; **शान्तः, शान्तवान्, शान्त्वा,\n'
        '  शान्तिः** for the कित्; **शंशान्तः, तन्तान्तः** for the ङित्,\n'
        '  these last **यङ्लुगन्तात्**'
    ),
)

register(
    '6.4.16',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — अज्झनगमां सनि — a vowel-final stem, and हन् and गम्,\n'
        '  lengthen before सन् beginning with a झल्: **विवीषति, तुष्टूषति,\n'
        '  चिकीर्षति, जिहीर्षति**; **जिघांसति** for हन्; **अधिजिगांसते** for\n'
        '  गम्.\n'
        '\n'
        'SETTLED — **AND THE VEDIC FORM THAT BREAKS THE VĀRTTIKA IS SENT TO\n'
        '  ANOTHER RULE.** **स्वर्गं लोकं समजिगांसद् इति छन्दसि यद्\n'
        '  अनिङादेशस्यापि दीर्घत्वं दृश्यते, तद् अन्येषामपि दृश्यते इत्यनेन\n'
        '  भवति** — 6.3.137, the catch-all of the pāda before, is what covers\n'
        '  it'
    ),
)

register(
    '6.4.17',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — तनोतेर्विभाषा — and तन् lengthens before सन् OPTIONALLY:\n'
        '  **तितांसति / तितंसति**. The इट् that makes the third form comes\n'
        '  from a vārttika: **सनीवन्तर्ध० इत्यत्र तनोतेर् उपसंख्यानाद् इडागमो\n'
        '  भवति विकल्पेन**'
    ),
)

register(
    '6.4.18',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — क्रमश्च क्त्वि — क्रम् lengthens its penult optionally\n'
        '  before क्त्वा beginning with a झल्: **क्रन्त्वा / क्रान्त्वा**.\n'
        '\n'
        'SETTLED — **AND THE ल्यप् FORMS ARE OUT BY A PARIBHĀṢĀ ABOUT\n'
        '  ORDER.** **प्रक्रम्य, उपक्रम्येति बहिरङ्गोऽपि\n'
        '  ल्यबादेशोऽन्तरङ्गानपि विधीन् बाधते इति पूर्वम् एव दीर्घत्वं न\n'
        '  प्रवर्तते** — the ल्यप् substitution is outer and still goes\n'
        '  first, so there is no क्त्वा left for this rule to act before'
    ),
)

register(
    '6.4.19',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — छ्वोः शूडनुनासिके च — छ् becomes श् and व् becomes ऊठ्,\n'
        '  matched one to one, before a nasal-initial affix, before क्विप्,\n'
        '  and before a झल्-initial कित् or ङित्: **प्रश्नः, विश्नः** for the\n'
        '  छ्; **स्योनः** for the व्.\n'
        '\n'
        'SETTLED — **AND EACH OF THE TWO NEEDS A DIFFERENT ORDER ARGUMENT.**\n'
        "  **अन्तरङ्गत्वाच् छे च इति तुकि कृते सतुक्कस्य शादेशः** — 6.1.73's\n"
        '  तुक् is inner and goes first, so what श् replaces is छ् WITH its\n'
        '  तुक्. And for the other: **सिवेर् औणादिके नप्रत्यये लघूपधगुणात्\n'
        '  पूर्वम् ऊठ् क्रियते** — the ऊठ् is put in before the guṇa would\n'
        '  have been'
    ),
)

register(
    '6.4.20',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — ज्वरत्वरस्रिव्यविमवामुपधायाश्च — in five stems the व् AND\n'
        '  the penult together become ऊठ्: **जूः, जूरौ, जूरः; जूर्तिः**;\n'
        '  **तूः, तूर्तिः**; **स्रूः, स्रूतः, स्रूतिः**; **ऊः, ऊतिः**; **मूः,\n'
        '  मूतिः**.\n'
        '\n'
        'SETTLED — **AND THE PENULT IS NOT ON THE SAME SIDE OF THE व् IN ALL\n'
        '  FIVE.** **ज्वरत्वरोर् उपधा वकारात् परा, स्रिव्यवमवां पूर्वा** — in\n'
        '  ज्वर् and त्वर् it follows the व्, in the other three it precedes.\n'
        '  One substitute for two sounds, and which two depends on the stem'
    ),
)

register(
    '6.4.21',
    apply=to_the_stem,
    codification=_TO_THE_STEM,
    notes=(
        'SETTLED — राल्लोपः — after a र्, the छ् and the व् are simply\n'
        '  DROPPED instead: **मूः, मुरौ, मुरः; मूर्तः, मूर्तिः** from मुर्छ्;\n'
        '  **हूः, हूर्णः, हूर्तिः** from हुर्छ्; **तूः, तूर्णः, तूर्तिः**\n'
        '  from तुर्व्.\n'
        '\n'
        'SETTLED — **AND HERE THE छ् IS TAKEN WITHOUT ITS तुक्.** **राल्लोपे\n'
        '  सतुक्कस्य छस्याभावात् केवलो गृह्यते** — the exact opposite of\n'
        '  6.4.19, where the तुक् had to be there first. A र् before the छ्\n'
        '  means 6.1.73 never applied, so there is a bare छ् to drop'
    ),
)


_N_GOES = (
    'n_goes(stem, gana=..., before=..., result=...) -> whether '
    'the stem loses its n before the affix, and by which rule of '
    '6.4.23-33.'
)

register(
    '6.4.23',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — श्नान्नलोपः — the न् after श्न is dropped: **अनक्ति,\n'
        '  भनक्ति, हिनस्ति**. And which श्न: **श्नादिति श्नमयम् उत्सृष्टाकारो\n'
        '  गृह्यते** — the infix श्नम् with its अ let go, not the affix श्ना.\n'
        '\n'
        'SETTLED — **AND THE श् IS WHAT KEEPS TWO OTHER WORDS OUT.**\n'
        '  **शकारवतो ग्रहणं किम्? यज्ञानाम्, यत्नानाम्। सुपि च इति परत्वात्\n'
        '  कृतेऽपि दीर्घत्वे स्थानिवद्भावाद् नलोपः स्याद् एव** — 7.3.102\n'
        '  lengthens the अ, and by स्थानिवद्भाव the stem would still count as\n'
        '  ending in the same shape, so the न् would go from those too.\n'
        '  Naming the श् is what stops it'
    ),
)

register(
    '6.4.24',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — अनिदितां हल उपधायाः क्ङिति — a consonant-final stem with\n'
        '  NO इ marker drops the न् of its penult before a कित् or ङित्:\n'
        '  **स्रस्तः, ध्वस्तः, स्रस्यते, ध्वस्यते, सनीस्रस्यते,\n'
        '  दनीध्वस्यते**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA ADDS TWO ROOTS, EACH IN ONE SENSE ONLY.**\n'
        '  **अनिदितां नलोपे लङ्गिकम्प्योर् उपतापशरीरविकारयोर् उपसंख्यानं\n'
        '  कर्तव्यम्** — लङ्ग् where illness is meant and कम्प् where a\n'
        '  change in the body is, matched one to one'
    ),
)

register(
    '6.4.25',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — दंशसञ्जस्वञ्जां शपि — three roots drop the न् of their\n'
        '  penult before शप्: **दशति, सजति, परिष्वजते** — he bites, he\n'
        '  clings, he embraces'
    ),
)

register(
    '6.4.26',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — रञ्जेश्च — and रञ्ज् likewise: **रजति, रजतः, रजन्ति**.\n'
        '  Stated apart from the three before it for a reason that lies\n'
        '  ahead: **पृथग्योगकरणम् उत्तरार्थम्** — so that रञ्ज् alone carries\n'
        '  down into 6.4.27'
    ),
)

register(
    '6.4.27',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — घञि च भावकरणयोः — and रञ्ज् drops it before घञ् where the\n'
        '  ACT or the MEANS is named: **आश्चर्यो रागः, विचित्रो रागः** for\n'
        '  the act; **रज्यतेऽनेनेति रागः** for the means. This is what\n'
        "  6.4.26's separate statement was for"
    ),
)

register(
    '6.4.28',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — स्यदो जवे — स्यद is laid down whole for the sense SPEED:\n'
        '  **गोस्यदः, अश्वस्यदः**. Two things are निपातन at once —\n'
        '  **स्यन्देर् नलोपो वृद्ध्यभावश्च** — the न् gone and the वृद्धि not\n'
        '  made.\n'
        '\n'
        'SETTLED — **AND ONE PROHIBITION IS NOT IN THE WAY.** **इक्प्रकरणाद्\n'
        '  न धातुलोप० इति प्रतिषेधो नास्ति** — 1.1.4 refuses guṇa and vṛddhi\n'
        '  after a root has lost a sound, but it is stated in the इक् section\n'
        '  and does not reach here'
    ),
)

register(
    '6.4.29',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — अवोदैधोद्मप्रश्रथहिमश्रथाः — five forms laid down whole:\n'
        '  **अवोदः** from उन्द् with अव, **एधः** from इन्ध्, **ओद्म** from\n'
        '  उन्द् with the Uṇādi मन्, **प्रश्रथः** and **हिमश्रथः** from\n'
        '  श्रन्थ्.\n'
        '\n'
        'SETTLED — **AND TWO OF THEM ARE LAID DOWN FOR TWO THINGS APIECE.**\n'
        '  **एध इति इन्धेर् घञि नलोपो गुणश्च निपात्यते। न धातुलोप आर्धधातुके\n'
        '  इति हि प्रतिषेधः स्यात्** — the न् gone AND the guṇa made, because\n'
        '  1.1.4 would otherwise have refused the guṇa to a root that has\n'
        '  lost a sound. Same for ओद्म'
    ),
)

register(
    '6.4.30',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — न अञ्चेः पूजायाम् — but अञ्च् does not drop its न् where\n'
        '  HONOUR is meant: **अञ्चिता अस्य गुरवः; अञ्चितम् इव शिरो वहति** —\n'
        '  his teachers are honoured; he carries his head as though it were.\n'
        "  The इट् that makes अञ्चिता is 7.2.53's, stated for the same sense"
    ),
)

register(
    '6.4.31',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — क्त्वि स्कन्दिस्यन्दोः — nor स्कन्द् and स्यन्द् before\n'
        '  क्त्वा: **स्कन्त्वा, स्यन्त्वा**.\n'
        '\n'
        'SETTLED — **AND FOR ONE OF THE TWO THE REFUSAL IS NOT NEEDED ON ONE\n'
        '  READING.** **स्यन्देर् ऊदित्त्वात् पक्ष इडागमः। स्यन्दित्वा। तत्र\n'
        '  यदा इडागमस् तदा न क्त्वा सेट् इति कित्त्वप्रतिषेधाद् एव\n'
        '  नलोपाभावः** — with the इट् in, 1.2.18 takes the कित् away and\n'
        '  6.4.24 could not have applied anyway'
    ),
)

register(
    '6.4.32',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — जान्तनशां विभाषा — and ज्-final stems and नश् refuse it\n'
        '  OPTIONALLY before क्त्वा: **रङ्क्त्वा / रक्त्वा; भङ्क्त्वा /\n'
        '  भक्त्वा; नंष्ट्वा / नष्ट्वा**, and **इट्पक्षे नशित्वा** for a\n'
        '  third'
    ),
)

register(
    '6.4.33',
    apply=n_goes,
    codification=_N_GOES,
    notes=(
        'SETTLED — भञ्जेश्च चिणि — भञ्ज् drops the न् before चिण् OPTIONALLY:\n'
        '  **अभाजि / अभञ्जि**.\n'
        '\n'
        'SETTLED — **AND IT READS AS A REFUSAL AND IS NOT ONE.**\n'
        '  **अप्राप्तोऽयं नलोपः पक्षे विधीयते। ततो नेति नानुवर्तते** — the\n'
        '  loss was never available before चिण्, so this sūtra GRANTS it\n'
        '  optionally rather than withholding it, and the न of 6.4.30 does\n'
        '  not carry down into it. Three refusals in a row and then one that\n'
        '  only looks like a fourth'
    ),
)


_THE_NASAL = (
    'the_nasal(stem, gana=..., before=..., result=...) -> what '
    "becomes of the stem's final nasal before the affix, and by "
    'which rule of 6.4.34-45.'
)

register(
    '6.4.34',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — शास इदङ्हलोः — शास् takes इ in its penult before अङ् and\n'
        '  before a consonant-initial कित् or ङित्: **अन्वशिषत्, अन्वशिषताम्,\n'
        '  अन्वशिषन्** for the अङ्; **शिष्टः, शिष्टवान्** for the कित्;\n'
        "  **आवां शिष्वः, वयं शिष्मः** for the ङित्. The ष् is 8.3.60's,\n"
        '  **शासिवसिघसीनां च**, and it comes only after the इ is in.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA ADDS ONE MORE PLACE.** **क्वौ च शास\n'
        '  इत्त्वं भवतीति वक्तव्यम् — आर्यान् शास्तीति मित्रशीः**'
    ),
)

register(
    '6.4.35',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — शा हौ — and before हि, शास् becomes शा outright:\n'
        '  **अनुशाधि, प्रशाधि**.\n'
        '\n'
        'SETTLED — **AND TWO CONDITIONS ARE DROPPED HERE AND THE GENITIVE\n'
        '  THEN MEANS SOMETHING ELSE.** **उपधाया इति निवृत्तम्, ततः शास इति\n'
        "  स्थानेयोगा षष्ठी भवति** — with उपधायाः gone, 1.1.49's rule makes\n"
        "  शासः mean *in place of शास्* rather than *of शास्'s penult*. And\n"
        '  **क्ङितीत्येतदपि निवृत्तम्। तेन यदा वा छन्दसि इति पित्त्वं\n'
        '  हिशब्दस्य, तदाप्यादेशो भवत्येव** — so the substitute holds even\n'
        '  where 3.4.88 makes हि पित्'
    ),
)

register(
    '6.4.36',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — हन्तेर्जः — and हन् becomes ज before हि: **जहि शत्रून्**.\n'
        '  One root, one substitute, and the same affix the sūtra before\n'
        '  named'
    ),
)

register(
    '6.4.37',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — अनुदात्तोपदेशवनतितनोत्यादीनाम् अनुनासिकलोपो झलि क्ङिति — a\n'
        '  nasal-final root taught with a LOW ACCENT, and वन् and तन् and\n'
        '  their fellows, drop the nasal before a झल्-initial कित् or ङित्:\n'
        '  **यत्वा, यतः, यतवान्, यतिः; रत्वा, रतः, रतिः; वतिः**.\n'
        '\n'
        'SETTLED — **AND THE CLASS IS NAMED BY ITS ACCENT AND THEN LISTED.**\n'
        '  **अनुदात्तोपदेशा अनुनासिकान्ता यमिरमिनमिगमिहनिमन्यतयः** — six\n'
        '  roots, gathered not by how they sound but by the accent they carry\n'
        '  where the Dhātupāṭha teaches them. A class the phonetics cannot\n'
        '  find'
    ),
)

register(
    '6.4.38',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — वा ल्यपि — and before ल्यप्, optionally: **प्रयत्य /\n'
        '  प्रयम्य; प्ररत्य / प्ररम्य; प्रणत्य / प्रणम्य; आगत्य / आगम्य**.\n'
        '\n'
        'SETTLED — **AND THE OPTION IS SETTLED AND NOT FREE.**\n'
        '  **व्यवस्थितविभाषा चेयम्। तेन मकारान्तानां विकल्पो भवति, अन्यत्र\n'
        '  नित्यमेव लोपः** — only the म्-final roots have the choice; the\n'
        '  rest simply drop, and **आहत्य, प्रमत्य, प्रवत्य, प्रक्षत्य** have\n'
        '  no second form'
    ),
)

register(
    '6.4.39',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — न क्तिचि दीर्घश्च — but before क्तिच् neither the\n'
        '  nasal-loss nor a lengthening: **यन्तिः, वन्तिः, तन्तिः**.\n'
        '\n'
        'SETTLED — **AND THE SECOND REFUSAL IS THERE BECAUSE THE FIRST WOULD\n'
        '  HAVE LET A THIRD RULE IN.** **अनुनासिकलोपे प्रतिषिद्धे अनुनासिकस्य\n'
        '  क्विझलोः क्ङिति इति दीर्घः प्राप्नोति, सोऽपि प्रतिषिध्यते** — stop\n'
        '  the loss and the root is still nasal-final, so 6.4.15 reaches it\n'
        '  and lengthens the penult. The word दीर्घश्च is there to shut that\n'
        '  off too. A refusal that has to refuse twice because refusing once\n'
        '  creates the second case'
    ),
)

register(
    '6.4.40',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — गमः क्वौ — गम् drops its nasal before क्विप्: **अङ्गगत्,\n'
        '  कलिङ्गगत्, अध्वगतो हरयः**.\n'
        '\n'
        'SETTLED — **AND TWO VĀRTTIKAS WIDEN IT IN TWO DIRECTIONS.**\n'
        '  **गमादीनाम् इति वक्तव्यम्। इहापि यथा स्यात् — संयत्, परीतत्** —\n'
        '  गम् and its fellows, so that 6.3.116 can lean on this for तन् as\n'
        '  well; and **ऊ च गमादीनाम् इति वक्तव्यम् — अग्रेगूः, अग्रेभूः**, a\n'
        '  ऊ beside the loss'
    ),
)

register(
    '6.4.41',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — विड्वनोरनुनासिकस्यात् — a nasal-final stem takes आ before\n'
        '  विट् and वनिप्: **अब्जा गोजा ऋतजा अद्रिजाः; गोषा इन्दो नृषा असि;\n'
        '  कूपखाः, शतखाः, सहस्रखाः; दधिक्राः; अग्रेगा उन्नेतॄणाम्**. The विट्\n'
        "  is 3.2.67's, **जनसनखनक्रमगमो विट्**, and the ष् of गोषाः is\n"
        "  8.3.106's"
    ),
)

register(
    '6.4.42',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — जनसनखनां सञ्झलोः — जन्, सन् and खन् take आ before सन्\n'
        '  beginning with a झल्, and before a झल्-initial कित् or ङित्:\n'
        '  **जातः, जातवान्, जातिः; सिषासति, सातः, सातिः; खातः, खातवान्,\n'
        '  खातिः**.\n'
        '\n'
        'SETTLED — **AND झल् IS CARRIED DOWN TO QUALIFY THE सन् AND NOT THE\n'
        '  OTHER AFFIX.** **झल्ग्रहणं सन्विशेषणार्थं किमर्थम् अनुवर्त्यते? इह\n'
        '  मा भूत् — जिजनिषति** — with an इट् the सन् begins with इ and is\n'
        '  out'
    ),
)

register(
    '6.4.43',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — ये विभाषा — and before a य्-initial कित् or ङित्,\n'
        '  optionally: **जायते / जन्यते; जाजायते / जञ्जन्यते; सायते / सन्यते;\n'
        '  खायते / खन्यते**.\n'
        '\n'
        'SETTLED — **AND ONE OF THE THREE HAS NO OPTION IN ONE PLACE.**\n'
        '  **जनेः श्यनि ज्ञाजनोर्जा इति नित्यं जादेशो भवति** — before श्यन्\n'
        '  7.3.79 gives जन् a जा outright, so the option never arises there'
    ),
)

register(
    '6.4.44',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — तनोतेर्यकि — and तन् takes आ before यक्, optionally:\n'
        '  **तायते / तन्यते**'
    ),
)

register(
    '6.4.45',
    apply=the_nasal,
    codification=_THE_NASAL,
    notes=(
        'SETTLED — सनः क्तिचि लोपश्चास्यान्यतरस्याम् — before क्तिच्, सन्\n'
        '  takes आ, and the आ is optionally DROPPED as well: **सातिः, सन्तिः,\n'
        '  सतिः** — three forms from one sūtra.\n'
        '\n'
        'SETTLED — **AND अन्यतरस्याम् IS SAID THOUGH विभाषा WAS ALREADY\n'
        '  RUNNING.** **अन्यतरस्यांग्रहणं विस्पष्टार्थम्। ये संबद्धं हि\n'
        "  विभाषाग्रहणम् इह निवृत्तम् इत्याशङ्क्येत** — 6.4.43's विभाषा was\n"
        '  tied to its ये, and one might have thought it had lapsed. Saying\n'
        '  the word again settles it'
    ),
)


_BEFORE_ARDHADHATUKA = (
    'before_ardhadhatuka(stem, gana=..., before=..., part=..., '
    'result=..., chandasi=...) -> what the stem loses or becomes '
    'before the affix, and by which rule of 6.4.46-70.'
)

register(
    '6.4.46',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — आर्धधातुके — **आर्धधातुक इत्यधिकारः। न ल्यपि इति प्राग्\n'
        '  एतस्माद् यदित ऊर्ध्वम् अनुक्रमिष्याम आर्धधातुक इत्येवं तद्\n'
        "  वेदितव्यम्** — a heading inside 6.4.1's, running twenty-three\n"
        '  sūtras and stopping because 6.4.69 says न ल्यपि. The vṛtti reads\n'
        '  the next rule out as its example: **वक्ष्यति अतो लोपः —\n'
        '  चिकीर्षिता, जिहीर्षिता। आर्धधातुक इति किम्? भवति, भवतः**.\n'
        '\n'
        'SETTLED — **AND THE HEADING HAS TO BE STATED BECAUSE ONE PARIBHĀṢĀ\n'
        '  WOULD OTHERWISE HAVE DONE THE WORK.** **अदिप्रभृतिभ्यः शपो\n'
        '  लुग्वचनं प्रत्ययलोपलक्षणप्रतिषेधार्थं स्याद् इत्येतद् न** — one\n'
        "  might think 2.4.72's लुक् was stated to keep 1.1.63 from acting,\n"
        '  and that the same reasoning would fence these rules; it does not'
    ),
)

register(
    '6.4.47',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — भ्रस्जो रोपधयो रमन्यतरस्याम् — the र् AND the penult of\n'
        '  भ्रस्ज् together become रम्, optionally: **भ्रष्टा / भर्ष्टा;\n'
        '  भ्रष्टुम् / भर्ष्टुम्; भ्रज्जनम् / भर्जनम्**.\n'
        '\n'
        "SETTLED — **AND THE SUBSTITUTE'S म् PUTS IT WHERE IT GOES.**\n"
        '  **रोपधयोरिति स्थानषष्ठीनिर्देशाद् उपधा रेफश्च निवर्तेते,\n'
        '  मित्त्वात् चायम् अचोऽन्त्यात् परो भवति** — the genitive says the\n'
        '  र् and the penult go, and the म् marker says the substitute lands\n'
        '  after the last vowel'
    ),
)

register(
    '6.4.48',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — अतो लोपः — an अ-final stem loses that अ before an\n'
        '  ārdhadhātuka: **चिकीर्षिता, चिकीर्षितुम्, चिकीर्षितव्यम्; धिनुतः,\n'
        '  कृणुतः**.\n'
        '\n'
        'SETTLED — **AND IT BEATS THE STRENGTHENING BY BEING NAMED EARLIER.**\n'
        '  **वृद्धिदीर्घाभ्याम् अतो लोपः पूर्वविप्रतिषेधेन — चिकीर्षकः,\n'
        '  जिहीर्षकः, चिकीर्ष्यते** — the vṛddhi and the lengthening would\n'
        '  both have reached the same अ, and the earlier rule takes it'
    ),
)

register(
    '6.4.49',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — यस्य हलः — a य standing after a consonant is lost before\n'
        '  an ārdhadhātuka: **बेभिदिता, बेभिदितुम्, बेभिदितव्यम्**.\n'
        '\n'
        'SETTLED — **AND WHAT IS LOST IS THE WHOLE य AND NOT ITS LAST\n'
        '  SOUND.** **यस्येति संघातग्रहणम् एतत्। तत्र अलोऽन्त्यस्य इत्येतद् न\n'
        '  भवति, अतो लोपः इत्यनेनैव तस्य सिद्धत्वात्** — read as a whole, so\n'
        '  1.1.52 does not cut it down to the final अ, which 6.4.48 had\n'
        '  already taken anyway. Or, the vṛtti offers, **हल इति वा\n'
        '  पञ्चमीनिर्देशः, तत्र आदेः परस्य इति यकारोऽनेन लुप्यते**'
    ),
)

register(
    '6.4.50',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — क्यस्य विभाषा — and क्य after a consonant is lost\n'
        '  OPTIONALLY: **समिध्यिता / समिधिता; दृषद्यिता / दृषदिता**. Which\n'
        '  क्य the vṛtti leaves to the derivation: **समिधम् आत्मन इच्छति,\n'
        '  समिद् इवाचरति इति वा क्यच्क्यङौ यथायोगं कर्तव्यौ**'
    ),
)

register(
    '6.4.51',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — णेरनिटि — the causal णि is lost before an ārdhadhātuka\n'
        '  that takes NO इट्: **अततक्षत्, अररक्षत्, आशिशत्, आटिटत्; कारणा,\n'
        '  हारणा; कारकः, हारकः; कार्यते, हार्यते; ज्ञीप्सति**. The vṛtti\n'
        '  names what it displaces in one breath:\n'
        '  **इयङ्यण्गुणवृद्धिदीर्घाणाम् अपवादः**'
    ),
)

register(
    '6.4.52',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — निष्ठायां सेटि — and the णि is lost before a निष्ठा WITH\n'
        '  an इट्: **कारितम्, हारितम्, गणितम्, लक्षितम्**. So the णि goes\n'
        '  both with the इट् and without it, and the two sūtras between them\n'
        '  leave only कारयिता standing.\n'
        '\n'
        'SETTLED — **AND SAYING सेटि IS WHAT KEEPS ONE FORM OUT OF BOTH\n'
        '  RULES.** **सेड्ग्रहणसामर्थ्याद् इह पूर्वेणापि न भवति** — the mere\n'
        '  fact that सेट् had to be said shows 6.4.51 does not reach\n'
        '  संज्ञपितः either'
    ),
)

register(
    '6.4.53',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — जनिता मन्त्रे — जनिता is laid down for a मन्त्र, with the\n'
        '  णि lost before an इट्-taking affix: **यो नः पिता जनिता**. Neither\n'
        '  6.4.51 nor 6.4.52 could have reached it, the affix having an इट्\n'
        '  and not being a निष्ठा'
    ),
)

register(
    '6.4.54',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — शमिता यज्ञे — and शमिता in the rite: **शृतं हविः शमितः**.\n'
        '  **तृचि संबुध्यन्तम् एतत्** — the form laid down is a vocative of\n'
        '  the तृच् stem, not the nominative'
    ),
)

register(
    '6.4.55',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — अय् आमन्तात्वाय्येत्न्विष्णुषु — before six affixes the णि\n'
        '  becomes अय् instead of going: **कारयांचकार, हारयांचकार** (आम्);\n'
        '  **गण्डयन्तः, मण्डयन्तः** (अन्त); **स्पृहयालुः, गृहयालुः** (आलु);\n'
        '  **स्पृहयाय्यः** (आय्य); **स्तनयित्नुः** (इत्नु); **पोषयिष्णवः,\n'
        '  पारयिष्णवः** (इष्णु).\n'
        '\n'
        'SETTLED — **AND SAYING अय् RATHER THAN न IS FOR THE RULE AFTER.**\n'
        '  **नेति वक्तव्येऽयादेशवचनम् उत्तरार्थम्** — *not* would have\n'
        '  sufficed here, since the णि simply staying would give the same\n'
        '  forms; अय् is said so that 6.4.56 can carry it'
    ),
)

register(
    '6.4.56',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — ल्यपि लघुपूर्वात् — and before ल्यप्, where the sound\n'
        '  before the णि is LIGHT: **प्रणमय्य, प्रतमय्य, प्रदमय्य, प्रशमय्य,\n'
        '  संदमय्य गतः; प्रबेभिदय्य गतः; प्रगणय्य गतः**.\n'
        '\n'
        "SETTLED — **AND 6.4.22's असिद्धत्व DOES NOT REACH HERE.**\n"
        '  **ह्रस्वयलोपाल्लोपानाम् असिद्धत्वं न भवति असमानाश्रयत्वात्।\n'
        '  ह्रस्वादयो हि णौ, ल्यपि णेर् अयादेशो भवति** — the shortening and\n'
        '  the two elisions rest on the णि, and this substitution rests on\n'
        "  the ल्यप्, so the two do not share a locus and 6.4.22's अत्र fails"
    ),
)

register(
    '6.4.57',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — विभाषाऽऽपः — and after आप्, optionally: **प्रापय्य गतः /\n'
        '  प्राप्य गतः**'
    ),
)

register(
    '6.4.58',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — युप्लुवोर्दीर्घश्छन्दसि — यु and प्लु lengthen before\n'
        '  ल्यप् in the Veda: **दान्त्यनुपूर्वं वियूय; यत्रापो दक्षिणा\n'
        '  परिप्लूय**'
    ),
)

register(
    '6.4.59',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — क्षियः — and क्षि lengthens before ल्यप्, Veda or no:\n'
        '  **प्रक्षीय**'
    ),
)

register(
    '6.4.60',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — निष्ठायामण्यदर्थे — and क्षि lengthens in a निष्ठा that is\n'
        "  NOT in a ण्यत्'s sense: **आक्षीणः, प्रक्षीणः, परिक्षीणः**. **ण्यतः\n"
        '  कृत्यस्यार्थो भावकर्मणी, ताभ्याम् अन्यत्र या निष्ठा** — the ण्यत्\n'
        '  means the act or the object, and a निष्ठा meaning either is out.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI ACCOUNTS FOR THE क्त IN TWO WAYS.**\n'
        '  **अकर्मकत्वात् क्षियः कर्तरि क्तः** for प्रक्षीणः, and\n'
        '  **प्रक्षीणम् इदं देवदत्तस्येति क्तोऽधिकरणे च\n'
        '  ध्रौव्यगतिप्रत्यवसानार्थेभ्यः इत्यधिकरणे क्तः** for the other\n'
        '  reading'
    ),
)

register(
    '6.4.61',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — वाऽऽक्रोशदैन्ययोः — but where ABUSE or MISERY is meant the\n'
        '  lengthening is OPTIONAL: **क्षितायुरेधि / क्षीणायुरेधि** for\n'
        '  abuse; **क्षितकः / क्षीणकः; क्षितोऽयं तपस्वी / क्षीणोऽयं तपस्वी**\n'
        '  for misery'
    ),
)

register(
    '6.4.62',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां वा\n'
        '  चिण्वदिट् च — before स्य, सिच्, सीयुट् and तासि in the passive or\n'
        '  the impersonal, a vowel-final stem as TAUGHT, and हन्, ग्रह् and\n'
        '  दृश्, behave AS THOUGH चिण् were there, and take an इट् with it.\n'
        '\n'
        'SETTLED — **AND WHAT THE चिण्वत् REACHES IS THE AFFIX AND NOT THE\n'
        '  STEM.** **यदा चिण्वत् तदा इडागमो भवति। कस्य? स्यसिच्सीयुट्तासीनाम्\n'
        '  एवेति वेदितव्यम्। ते हि प्रकृताः। अङ्गस्य तु लक्ष्यविरोधाद् न\n'
        '  क्रियते** — the इट् goes to the four affixes, because they are\n'
        '  what the sūtra has in hand, and giving it to the stem would\n'
        '  contradict the forms.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI OPENS BY ASKING WHAT THE SŪTRA IS FOR.**\n'
        '  **कानि पुनर् अस्य योगस्य प्रयोजनानि?** — and answers in verse. The\n'
        '  longest sūtra of the pāda, and the only one that makes one thing\n'
        '  behave like another rather than replacing it.\n'
        '\n'
        "SETTLED — **SCOPE** — the verse's list of प्रयोजनानि, and which of\n"
        "  चिण्'s own effects follow and which do not, is not modelled here"
    ),
)

register(
    '6.4.63',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — दीङो युडचि क्ङिति — दीङ् takes the augment युट् before a\n'
        '  vowel-initial कित् or ङित्: **उपदिदीये, उपदिदीयाते, उपदिदीयिरे**.\n'
        '\n'
        'SETTLED — **AND THE AUGMENT GOES TO THE AFFIX AND NOT THE ROOT.**\n'
        '  **दीङ इति पञ्चमीनिर्देशाद् अजादेर् युडागमो भवति** — the ablative\n'
        "  says *after दीङ्*, so the augment is the vowel-initial affix's.\n"
        '  And **विधानसामर्थ्यात् च एरनेकाचः० इति यणादेशे कर्तव्ये\n'
        '  तस्यासिद्धत्वं न भवति** — 6.4.22 would have hidden it from 6.4.82,\n'
        '  and the mere fact of the rule being stated stops that'
    ),
)

register(
    '6.4.64',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — आतो लोप इटि च — an आ-final stem loses that आ before an\n'
        '  इट्, and before a vowel-initial कित् or ङित्: **पपिथ, तस्थिथ** for\n'
        '  the इट्; **पपतुः, पपुः, तस्थतुः, तस्थुः; गोदः, कम्बलदः** for the\n'
        '  कित्; **प्रदा, प्रधा** for the ङित्. And **व्यत्यरे, व्यत्यले**\n'
        '  are रा and ला in the लङ् with an इट्'
    ),
)

register(
    '6.4.65',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — ईद्यति — and an आ-final stem takes ई before यत्: **देयम्,\n'
        '  धेयम्, हेयम्, स्तेयम्** — to be given, to be placed, to be\n'
        '  abandoned, to be stolen'
    ),
)

register(
    '6.4.66',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — घुमास्थागापाजहातिसां हलि — the घु class and six named\n'
        '  roots take ई before a consonant-initial कित् or ङित्: **दीयते,\n'
        '  धीयते, देदीयते** for घु; **मीयते, मेमीयते; स्थीयते, तेष्ठीयते;\n'
        '  गीयते, जेगीयते, अध्यगीष्ट; पीयते, पेपीयते; हीयते** for the rest'
    ),
)

register(
    '6.4.67',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — एर्लिङि — and the same seven take ए before लिङ्: **देयात्,\n'
        '  धेयात्, मेयात्, स्थेयात्, गेयात्, पेयात्, हेयात्, अवसेयात्**'
    ),
)

register(
    '6.4.68',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — वाऽन्यस्य संयोगादेः — and an आ-final stem BEGINNING with a\n'
        '  cluster, other than those seven, takes ए before लिङ् optionally:\n'
        '  **ग्लेयात् / ग्लायात्; म्लेयात् / म्लायात्**. This is the last\n'
        '  sūtra under आर्धधातुके; the next word ends the heading'
    ),
)

register(
    '6.4.69',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — न ल्यपि — but before ल्यप्, none of what was said of the\n'
        '  seven holds: **प्रदाय, प्रधाय, प्रमाय, प्रस्थाय, प्रगाय, प्रपाय,\n'
        '  प्रहाय, अवसाय**.\n'
        '\n'
        'SETTLED — **AND THIS SŪTRA IS ALSO THE BOUND OF THE HEADING.**\n'
        "  6.4.46's आर्धधातुके was read **न ल्यपि इति प्राग् एतस्मात्** — up\n"
        '  to but not including this. So one sūtra both refuses an operation\n'
        '  and closes the run that granted it'
    ),
)

register(
    '6.4.70',
    apply=before_ardhadhatuka,
    codification=_BEFORE_ARDHADHATUKA,
    notes=(
        'SETTLED — मयतेरिदन्यतरस्याम् — मय् takes इ before ल्यप्, optionally:\n'
        '  **अपमित्य / अपमाय**. Stated after the heading has closed, and\n'
        '  about the same affix that closed it'
    ),
)


_AUGMENT_OR_YAN = (
    'augment_or_yan(stem, gana=..., before=..., part=..., '
    'result=..., chandasi=...) -> which augment the stem takes '
    'before a past tense, or what its final vowel becomes, and by '
    'which rule of 6.4.71-95. 6.4.77 is answered by iyan_uvan.'
)

register(
    '6.4.71',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — लुङ्लङ्लृङ्क्ष्वडुदात्तः — before the लुङ्, the लङ् and\n'
        '  the लृङ् the stem takes the augment अट्, and the augment is\n'
        '  उदात्त: **अकार्षीत्, अहार्षीत्** (लुङ्); **अकरोत्, अहरत्** (लङ्);\n'
        '  **अकरिष्यत्, अहरिष्यत्** (लृङ्). The augment that makes a Sanskrit\n'
        '  past tense look like one, and the accent is part of the rule\n'
        '  rather than a consequence of it'
    ),
)

register(
    '6.4.72',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — आडजादीनाम् — and a VOWEL-INITIAL stem takes आट् instead,\n'
        '  also उदात्त: **ऐक्षिष्ट, ऐहिष्ट, औब्जीत्, औम्भीत्; ऐक्षत, ऐहत;\n'
        '  ऐक्षिष्यत, औब्जिष्यत्**.\n'
        '\n'
        'SETTLED — **AND ONE SET OF FORMS NEEDS AN ORDER ARGUMENT.** **इह\n'
        '  ऐज्यत औप्यत औह्यतेति लङि कृते लावस्थायाम् अडागमाद् अन्तरङ्गत्वाद्\n'
        '  लादेशः क्रियते। तत्र कृते विकरणो नित्यत्वाद् अडागमं बाधते** — the\n'
        '  ending is substituted first, being inner, and the class-marker\n'
        '  then beats the augment by being compulsory'
    ),
)

register(
    '6.4.73',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — छन्दस्यपि दृश्यते — and in the Veda the आट् is SEEN where\n'
        '  no rule puts it: **यत्र हि विहितस् ततोऽन्यत्रापि दृश्यते।\n'
        '  आडजादीनाम् इत्युक्तम् अनजादीनाम् अपि दृश्यते** — 6.4.72 gave it to\n'
        '  vowel-initial stems and the Veda has it on others: **सुरुचो वेन\n'
        '  आवः; आनक्; आयुनक्**'
    ),
)

register(
    '6.4.74',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — न माङ्योगे — but with मा neither augment: **मा भवान्\n'
        '  कार्षीत्, मा भवान् हार्षीत्; मा स्म करोत्, मा स्म हरत्; मा\n'
        '  भवानीहिष्ट, मा भवानीक्षिष्ट; मा स्म भवानीहत** — the prohibitive,\n'
        '  and the one place where a Sanskrit past-tense stem carries no\n'
        '  augment at all'
    ),
)

register(
    '6.4.75',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — बहुलं छन्दस्यमाङ्योगेऽपि — in the Veda both augments come\n'
        '  and go VARIOUSLY, with मा and without it: without — **जनिष्ठा\n'
        '  उग्रः; काममूनयीः; काममर्दयीत्** (and the augment absent); with —\n'
        '  **मा वः क्षेत्रे परबीजान्यवाप्सुः; मा अभित्थाः; मा आवः** (and the\n'
        "  augment there). So 6.4.74's refusal is lifted and 6.4.71's grant\n"
        '  is suspended, both in the same sūtra and both **बहुलम्**'
    ),
)

register(
    '6.4.76',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — इरयो रे — इर becomes रे in the Veda, variously: **गर्भं\n'
        '  प्रथमं दध्र आपः; याश्च परिददृश्रे**.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTION IS NOT SEEN BY THE RULE THAT\n'
        '  FOLLOWS IT.** **धाञो रेभावस्यासिद्धत्वाद् आतो लोपः भवति** —\n'
        "  6.4.22's असिद्धवत् hides the रे from 6.4.64, so the आ of धा is\n"
        '  still there to be dropped'
    ),
)

register(
    '6.4.78',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        "SETTLED — अभ्यासस्यासवर्णे — the REDUPLICATED syllable's final इ or\n"
        '  उ becomes इयङ् or उवङ् before a vowel NOT of its own class:\n'
        '  **इयेष, उवोष, इयर्ति**. The same pair of substitutes 6.4.77 gives\n'
        '  the stem, now given to the copy of it'
    ),
)

register(
    '6.4.79',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — स्त्रियाः — स्त्री takes इयङ् before a vowel affix:\n'
        '  **स्त्री, स्त्रियौ, स्त्रियः**. And **स्त्रीणाम् इत्यत्र परत्वाद्\n'
        '  नुडागमः** — the नुट् wins there by being later. Stated apart for\n'
        "  the next rule's sake: **पृथग्योगकरणम् उत्तरार्थम्**"
    ),
)

register(
    '6.4.80',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — वाऽंशसोः — and before अम् and शस्, optionally: **स्त्रीं\n'
        '  पश्य / स्त्रियं पश्य; स्त्रीः पश्य / स्त्रियः पश्य**. This is what\n'
        '  6.4.79 was split off for'
    ),
)

register(
    '6.4.81',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — इणो यण् — इण् takes a plain यण् before a vowel: **यन्ति,\n'
        '  यन्तु, आयन्**.\n'
        '\n'
        'SETTLED — **AND IT IS AN अपवाद THAT IS ITSELF OVERRULED.**\n'
        '  **इयङादेशापवादोऽयम्। मध्येऽपवादाः पूर्वान् विधीन् बाधन्ते इति\n'
        '  गुणवृद्धिभ्यां परत्वाद् अयं बाध्यते** — an exception standing in\n'
        '  the middle displaces the rules BEFORE it, so this beats 6.4.77 and\n'
        '  loses to the strengthening that comes after'
    ),
)

register(
    '6.4.82',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — एरनेकाचोऽसंयोगपूर्वस्य — an इ-final stem of MORE THAN ONE\n'
        '  VOWEL, with no cluster of the root before the इ, takes यण् before\n'
        '  a vowel: **निन्यतुः, निन्युः; उन्न्यौ, उन्न्यः; ग्रामण्यौ,\n'
        '  ग्रामण्यः**.\n'
        '\n'
        'SETTLED — **AND WHOSE CLUSTER IS MEANT IS SAID IN SO MANY WORDS.**\n'
        '  **धातोरिति वर्तते, तेन संयोगो विशेष्यते। धातोरवयवः संयोगः पूर्वो\n'
        '  यस्माद् इवर्णाद् न भवति** — the cluster has to belong to the ROOT,\n'
        '  and **असंयोगपूर्वग्रहणम् इवर्णविशेषणं यथा स्याद्, अङ्गविशेषणं मा\n'
        '  भूदिति** — it qualifies the इ and not the stem'
    ),
)

register(
    '6.4.83',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — ओः सुपि — and a उ-final stem of more than one vowel, with\n'
        '  no cluster of the root before the उ, takes यण् before a\n'
        '  vowel-initial सुप्: **खलप्वौ, खलप्वः; शतस्वौ, शतस्वः; सकृल्ल्वौ,\n'
        "  सकृल्ल्वः**. The condition is narrower than 6.4.82's — a सुप् and\n"
        '  not any vowel affix — and the vṛtti adds **गतिकारकाभ्याम्\n'
        '  अन्यपूर्वस्य** as a further limit'
    ),
)

register(
    '6.4.84',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — वर्षाभ्वश्च — and वर्षाभू before a vowel-initial सुप्:\n'
        '  **वर्षाभ्वौ, वर्षाभ्वः**. Two vārttikas add more: **पुनर्भ्वश्चेति\n'
        '  वक्तव्यम् — पुनर्भ्वौ, पुनर्भ्वः**, and **कारापूर्वस्यापीष्यते —\n'
        '  काराभ्वौ, काराभ्वः**'
    ),
)

register(
    '6.4.85',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — न भूसुधियोः — but भू and सुधी do not take it: **प्रतिभुवौ,\n'
        '  प्रतिभुवः; सुधियौ, सुधियः**. Two stems named against the two rules\n'
        '  just before, and the second of those two had just named a compound\n'
        '  of भू itself. **सुपि** is still running from 6.4.83, which is why\n'
        "  the refusal does not touch भू's वुक् at 6.4.88"
    ),
)

register(
    '6.4.86',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — छन्दस्युभयथा — and in the Veda both are seen: **वनेषु\n'
        '  चित्रं विभ्वं विशे** beside **विभुवं विशे**; **सुध्यो नव्यमग्ने**\n'
        '  beside **सुधियो नव्यमग्ने**. The same shape 6.4.5 had — a refusal\n'
        '  lifted for the Veda and lifted both ways at once'
    ),
)

register(
    '6.4.87',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — हुश्नुवोः सार्वधातुके — हु and a श्नु-ending stem of more\n'
        '  than one vowel, with no cluster before, take यण् before a\n'
        '  vowel-initial सार्वधातुक: **जुह्वति, जुह्वतु, जुह्वत्; सुन्वन्ति,\n'
        '  सुन्वन्तु, असुन्वन्**.\n'
        '\n'
        'SETTLED — **AND NAMING THE TWO TEACHES SOMETHING ABOUT ANOTHER\n'
        '  SECTION ENTIRELY.** **इदम् एव हुश्नुग्रहणं ज्ञापकं भाषायाम् अपि\n'
        '  यङ्लुग् अस्तीति** — if the यङ्लुक् were Vedic only, योयुवति and\n'
        '  रोरुवति would never arise outside the Veda and there would have\n'
        '  been nothing to keep out. The two names show the यङ्लुक् is\n'
        '  ordinary Sanskrit'
    ),
)

register(
    '6.4.88',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — भुवो वुग्लुङ्लिटोः — भू takes the augment वुक् before a\n'
        '  vowel in the लुङ् and the लिट्: **अभूवन्, अभूवम्** for the लुङ्;\n'
        '  **बभूव, बभूवतुः, बभूवुः** for the लिट्. The rule that gives बभूव\n'
        '  its second व्'
    ),
)

register(
    '6.4.89',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — ऊदुपधाया गोहः — गूह् lengthens its penult to ऊ before a\n'
        '  vowel affix: **निगूहयति, निगूहकः, साधुनिगूही, निगूहंनिगूहम्,\n'
        '  निगूहन्ति**.\n'
        '\n'
        'SETTLED — **AND उपधायाः IS SAID TO STOP A PARIBHĀṢĀ.** **उपधाया इति\n'
        '  किम्? अलोऽन्त्यस्य मा भूत्** — without it 1.1.52 would have put\n'
        '  the substitute at the end. And the root is named in its ALTERED\n'
        '  shape on purpose: **गोह इति विकृतग्रहणं विषयार्थम्**'
    ),
)

register(
    '6.4.90',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — दोषो णौ — दोष् lengthens its penult to ऊ before णि:\n'
        '  **दूषयति, दूषयतः, दूषयन्ति**. Named in its altered shape again,\n'
        '  and the vṛtti says why: **विकृतग्रहणं प्रक्रमाभेदार्थम्। पूर्वत्र\n'
        "  हि गोह इत्युक्तम्** — to keep the two sūtras' manner of naming the\n"
        '  same'
    ),
)

register(
    '6.4.91',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — वा चित्तविरागे — but where a change of MIND is meant,\n'
        '  optionally: **चित्तं दूषयति / चित्तं दोषयति; प्रज्ञां दूषयति /\n'
        '  प्रज्ञां दोषयति**'
    ),
)

register(
    '6.4.92',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — मितां ह्रस्वः — the मित् roots, **घटादयो मितः**, shorten\n'
        '  their penult before णि: **घटयति, व्यथयति, जनयति, रजयति, शमयति,\n'
        '  ज्ञपयति**.\n'
        '\n'
        'SETTLED — **AND SOME READ AN OPTION INTO IT.** **केचिद् अत्र\n'
        '  वेत्यनुवर्तयन्ति। सा च व्यवस्थितविभाषा। तेन उत्क्रामयति,\n'
        '  संक्रामयतीत्येवमादि सिद्धं भवति** — carrying वा down from 6.4.91,\n'
        '  and settled rather than free, so that the क्रम् forms come out'
    ),
)

register(
    '6.4.93',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — चिण्णमुलोर्दीर्घोऽन्यतरस्याम् — and before णि with चिण् or\n'
        '  णमुल् after it, the penult is optionally LONG instead: **अशमि /\n'
        '  अशामि; अतमि / अतामि; शमंशमम् / शामंशामम्; तमंतमम् / तामंतामम्**.\n'
        '\n'
        'SETTLED — **AND SAYING दीर्घ RATHER THAN MAKING 6.4.92 OPTIONAL IS\n'
        '  DELIBERATE.** **दीर्घग्रहणं किम्, न ह्रस्वविकल्प एव विधीयते? नैवं\n'
        '  शक्यम्, शमयन्तं प्रयुङ्क्त इति द्वितीये णिचि ह्रस्वविकल्पो न\n'
        '  स्यात्, णिलोपस्य स्थानिवद्भावात्** — with a second णि the\n'
        '  shortening is compulsory, so an option on it would not have\n'
        '  reached these forms'
    ),
)

register(
    '6.4.94',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — खचि ह्रस्वः — and before णि with खच् after it, the penult\n'
        '  shortens, मित् or not: **द्विषंतपः, परंतपः, पुरंदरः** — one who\n'
        '  scorches his foes, one who breaks forts'
    ),
)

register(
    '6.4.95',
    apply=augment_or_yan,
    codification=_AUGMENT_OR_YAN,
    notes=(
        'SETTLED — ह्लादो निष्ठायाम् — ह्लाद् shortens its penult before a\n'
        '  निष्ठा: **प्रह्लन्नः, प्रह्लन्नवान्**.\n'
        '\n'
        'SETTLED — **AND IT IS SPLIT FROM THE RULE BEFORE FOR ONE MORE\n'
        '  FORM.** **ह्लाद इति योगविभागः क्रियते, क्तिन्यपि यथा स्यात्\n'
        '  प्रह्लत्तिरिति** — dividing the sūtra lets the shortening reach a\n'
        '  क्तिन् as well as a निष्ठा'
    ),
)


_BEFORE_SARVADHATUKA = (
    'before_sarvadhatuka(stem, gana=..., before=..., part=..., '
    'result=..., chandasi=...) -> what the stem loses or becomes '
    'before the ending, and by which rule of 6.4.96-114.'
)

register(
    '6.4.96',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — छादेर्घेऽद्व्युपसर्गस्य — छाद् shortens its penult before\n'
        '  घ, if it has no two preverbs: **उरश्छदः, प्रच्छदः, दन्तच्छदः**.\n'
        '\n'
        'SETTLED — **AND THE MERE FACT OF THE RULE STOPS TWO OTHER THINGS.**\n'
        '  **णिलोपस्यासिद्धत्वं स्थानिवद्भावो वा वचनसामर्थ्याद् अत्र न भवतीति\n'
        "  ह्रस्वभाविन्युपधा भवति** — 6.4.22 would have hidden the णि's loss\n"
        '  and 1.1.56 would have kept it standing in its place; either way\n'
        "  there would be no vowel to shorten, so the rule's existence sets\n"
        '  both aside'
    ),
)

register(
    '6.4.97',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — इस्मन्त्रन्क्विषु च — and छाद् shortens before four more:\n'
        '  **छदिः** (इस्), **छद्म** (मन्), **छत्त्रम्** (त्रन्), **धामच्छत्,\n'
        '  उपच्छत्** (क्वि)'
    ),
)

register(
    '6.4.98',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — गमहनजनखनघसां लोपः क्ङित्यनङि — five roots lose the vowel\n'
        '  of their penult before a vowel-initial कित् or ङित् that is not\n'
        '  अङ्: **जग्मतुः, जग्मुः; जघ्नतुः, जघ्नुः; जज्ञे, जज्ञाते, जज्ञिरे;\n'
        '  चख्नतुः, चख्नुः; जक्षतुः, जक्षुः; अक्षन् पितरोऽमीमदन्त पितरः**'
    ),
)

register(
    '6.4.99',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — तनिपत्योश्छन्दसि — and तन् and पत् in the Veda:\n'
        '  **वितत्निरे कवयः; शकुना इव पप्तिम**'
    ),
)

register(
    '6.4.100',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — घसिभसोर्हलि च — and घस् and भस् in the Veda, before a\n'
        '  CONSONANT-initial कित् or ङित् as well as a vowel-initial one:\n'
        '  **सग्धिश्च मे सपीतिश्च मे; बब्धां ते हरी धानाः**. The vṛtti walks\n'
        '  सग्धि through three rules — **अदेः क्तिनि बहुलं छन्दसि इति\n'
        '  घस्लादेश उपधाया लोपे च कृते झलो झलि इति सकारलोपः**'
    ),
)

register(
    '6.4.101',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — हुझल्भ्यो हेर्धिः — after हु and after a झल्-final stem, a\n'
        '  consonant-initial हि becomes धि: **जुहुधि; भिन्द्धि, छिन्द्धि**.\n'
        '\n'
        'SETTLED — **AND THE FORMS WITH तातङ् ARE SETTLED BY A PARIBHĀṢĀ.**\n'
        '  **इह जुहुतात्, भिन्तात् त्वम् इति परत्वात् तातङि कृते सकृद्गतौ\n'
        '  विप्रतिषेधे...** — once the later rule has put the तातङ् in, the\n'
        '  conflict is spent and this rule does not come back'
    ),
)

register(
    '6.4.102',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — श्रुशृणुपॄकृवृभ्यश्छन्दसि — and after five roots in the\n'
        '  Veda, consonant or no: **श्रुधी हवमिन्द्र; गिरः शृणुधी; पूर्धि;\n'
        '  उरु णस्कृधि; अपा वृधि**.\n'
        '\n'
        'SETTLED — **AND ONE OF THE FIVE TEACHES THAT ANOTHER RULE DOES NOT\n'
        '  REACH IT.** **शृणुधीत्यत्र धिभावविधानसामर्थ्याद् उतश्च प्रत्ययाद्०\n'
        '  न भवति** — 6.4.106 would have dropped the हि after शृणु\n'
        '  altogether, and the mere fact that this rule gives it a shape\n'
        '  shows it does not'
    ),
)

register(
    '6.4.103',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — अङितश्च — and where the हि is NOT ङित्, which in the Veda\n'
        '  it may not be: **सोम रारन्धि; अस्मभ्यं तद्धर्यश्व प्रयन्धि;\n'
        '  युयोध्यस्मज्जुहुराणमेनः**. **वा छन्दसि इति\n'
        '  पित्त्वेनास्याङित्त्वम्** — 3.4.88 makes it पित् in the Veda, and\n'
        '  1.2.4 then does not make it ङित्'
    ),
)

register(
    '6.4.104',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — चिणो लुक् — the affix after चिण् is dropped altogether:\n'
        '  **अकारि, अहारि, अलावि, अपाचि** — it was done, it was taken, it was\n'
        '  cut, it was cooked. The whole of the Sanskrit aorist passive third\n'
        '  singular is this one rule.\n'
        '\n'
        'SETTLED — **AND THE लुक् DOES NOT REACH A तरप् AFTER IT.**\n'
        '  **अकारितराम् अहारितमाम् इत्यत्र तलोपस्यासिद्धत्वात् तरप्तमपोर् न\n'
        '  लुग् भवति। चिणो लुग् इत्येतद् विषयभेदाद् भिद्यते** — the तिप् is\n'
        '  gone and 6.4.22 hides that, so the तरप् is no longer *after चिण्*'
    ),
)

register(
    '6.4.105',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — अतो हेः — after an अ-final stem the हि is dropped\n'
        '  outright: **पच, पठ, गच्छ, धाव**. Every Sanskrit imperative of the\n'
        '  first class that looks like a bare stem is this rule'
    ),
)

register(
    '6.4.106',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — उतश्च प्रत्ययादसंयोगपूर्वात् — and after a उ that is an\n'
        '  AFFIX and has no cluster before it: **चिनु, सुनु, कुरु**. A\n'
        '  vārttika makes it optional in the Veda: **उतश्च प्रत्ययाच्छन्दसि\n'
        '  वेति वक्तव्यम्**'
    ),
)

register(
    '6.4.107',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — लोपश्चास्यान्यतरस्यां म्वोः — and that same उ is dropped\n'
        '  OPTIONALLY before an affix beginning with व् or म्: **सुन्वः /\n'
        '  सुनुवः; सुन्मः / सुनुमः; तन्वः / तनुवः; तन्मः / तनुमः**.\n'
        '\n'
        'SETTLED — **AND THE WORD लोप IS SAID THOUGH लुक् WAS RUNNING.**\n'
        '  **लुगिति वर्तमाने लोपग्रहणम् अन्त्यलोपार्थम्** — a लुक् takes the\n'
        '  whole affix and a लोप only its last sound, and here only the उ\n'
        '  goes'
    ),
)

register(
    '6.4.108',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — नित्यं करोतेः — but after कृ the loss is COMPULSORY:\n'
        '  **कुर्वः, कुर्मः**, and no second form. The word नित्यम् is the\n'
        '  whole of the difference from the sūtra before.\n'
        '\n'
        'SETTLED — **AND THE FORM THEN ESCAPES A LENGTHENING BY A NAMED\n'
        '  EXCEPTION.** **उकारलोपस्य दीर्घविधाव् अस्थानिवद्भावाद् हलि च इति\n'
        '  दीर्घत्वं प्राप्तं न भकुर्छुराम् इति प्रतिषिध्यते** — 1.1.58 does\n'
        '  not hide the loss from a lengthening rule, so 8.2.77 reaches\n'
        '  कुर्वः, and 8.2.79 names कुर् out'
    ),
)

register(
    '6.4.109',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — ये च — and before a य्-initial affix, also compulsory:\n'
        '  **कुर्यात्, कुर्याताम्, कुर्युः** — the optative of कृ, and the\n'
        '  commonest verb-form in Sanskrit prose'
    ),
)

register(
    '6.4.110',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — अत उत् सार्वधातुके — the अ of कृ with its उ-affix becomes\n'
        '  उ before a कित् or ङित् सार्वधातुक: **कुरुतः, कुर्वन्ति**.\n'
        '\n'
        'SETTLED — **AND सार्वधातुक IS SAID FOR AN AFFIX THAT IS NO LONGER\n'
        '  THERE.** **सार्वधातुकग्रहणं किम्? भूतपूर्वेऽपि सार्वधातुके यथा\n'
        '  स्यात् — कुरु** — the हि has been dropped by 6.4.106, and the rule\n'
        '  still has to reach what once stood before one'
    ),
)

register(
    '6.4.111',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — श्नसोरल्लोपः — the अ of श्न and of अस् is dropped before a\n'
        '  कित् or ङित् सार्वधातुक: **रुन्धः, रुन्धन्ति; भिन्तः, भिन्दन्ति;\n'
        '  स्तः, सन्ति**. This is the rule that makes the seventh class\n'
        '  conjugate as it does, and the one that makes सन्ति out of अस्'
    ),
)

register(
    '6.4.112',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — श्नाभ्यस्तयोरातः — the आ of श्ना and of a REDUPLICATED\n'
        '  stem is dropped before a कित् or ङित् सार्वधातुक: **लुनते,\n'
        '  लुनताम्, अलुनत**; **मिमते, मिमताम्, अमिमत; संजिहते, संजिहताम्,\n'
        '  समजिहत**'
    ),
)

register(
    '6.4.113',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — ई हल्यघोः — and that same आ becomes ई before a\n'
        '  CONSONANT-initial कित् or ङित् सार्वधातुक, the घु class excepted:\n'
        '  **लुनीतः, पुनीतः, लुनीथः, लुनीते**; **मिमीते, मिमीषे, मिमीध्वे;\n'
        "  संजिहीते, संजिहीषे, संजिहीध्वे**. So the ninth class's ना becomes\n"
        '  नी before a consonant and goes altogether before a vowel, by two\n'
        '  sūtras standing side by side'
    ),
)

register(
    '6.4.114',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — इद् दरिद्रस्य — and दरिद्रा takes इ before a\n'
        '  consonant-initial कित् or ङित् सार्वधातुक: **दरिद्रितः, दरिद्रिथः,\n'
        '  दरिद्रिवः, दरिद्रिमः**.\n'
        '\n'
        'SETTLED — **AND TWO VĀRTTIKAS SETTLE WHAT THE SŪTRA LEAVES.**\n'
        '  **दरिद्रातेर् आर्धधातुके लोपो वक्तव्यः**, and **सिद्धश्च\n'
        '  प्रत्ययविधौ भवतीति वक्तव्यम्** — the loss before an ārdhadhātuka,\n'
        '  and that loss counting as already done when an affix is being\n'
        '  prescribed, so that **दरिद्रातीति दरिद्रः** comes out'
    ),
)


_IN_THE_PERFECT = (
    'in_the_perfect(stem, gana=..., before=..., result=...) -> '
    'whether the vowel becomes e and the reduplication goes, and '
    'by which rule of 6.4.115-128.'
)

register(
    '6.4.115',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — भियोऽन्यतरस्याम् — भी takes इ OPTIONALLY before a\n'
        '  consonant-initial कित् or ङित् सार्वधातुक: **बिभितः / बिभीतः;\n'
        '  बिभिथः / बिभीथः; बिभिवः / बिभीवः; बिभिमः / बिभीमः**'
    ),
)

register(
    '6.4.116',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — जहातेश्च — and जहाति likewise: **जहितः / जहीतः; जहिथः /\n'
        '  जहीथः**. Stated apart for what follows: **पृथग्योगकरणम्\n'
        '  उत्तरार्थम्**'
    ),
)

register(
    '6.4.117',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — आ च हौ — and before हि, जहाति takes आ at its end, and इ\n'
        '  optionally beside it: **जहाहि, जहिहि, जहीहि** — three forms, the आ\n'
        '  from this rule, the इ from 6.4.116 carried down, and the ई from\n'
        '  neither'
    ),
)

register(
    '6.4.118',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — लोपो यि — and before a य्-initial कित् or ङित् सार्वधातुक\n'
        '  the आ of जहाति is simply DROPPED: **जह्यात्, जह्याताम्, जह्युः**'
    ),
)

register(
    '6.4.119',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — घ्वसोरेद्धावभ्यासलोपश्च — the घु class and अस् take ए\n'
        '  before हि, and the reduplication goes with it: **देहि, धेहि**; and\n'
        '  for अस्, **एधि**.\n'
        '\n'
        'SETTLED — **AND अस् GETS THERE BY A DIFFERENT ROAD.** **अस्तेः\n'
        '  श्नसोरल्लोपः इत्यकारलोपः** — 6.4.111 has already taken its अ, so\n'
        '  what this rule gives it is the ए and the loss of the copy. And the\n'
        '  loss is a शित्: **शिदयं लोपः। तेन सर्वस्याभ्यासस्य भवति** — so\n'
        '  1.1.55 makes it take the WHOLE reduplicated syllable and not\n'
        '  merely its last sound'
    ),
)

register(
    '6.4.120',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — अत एकहल्मध्येऽनादेशादेर्लिटि — where a stem does NOT begin\n'
        '  with a substitute, and a short अ stands BETWEEN TWO SINGLE\n'
        '  CONSONANTS, the perfect makes that अ an ए and drops the\n'
        '  reduplication: **रेणतुः, रेणुः; येमतुः, येमुः; पेचतुः, पेचुः;\n'
        '  देमतुः, देमुः**.\n'
        '\n'
        'SETTLED — **AND ONE RULE DOES TWO THINGS AT ONCE.** The vowel is\n'
        '  replaced AND the copied syllable is deleted, and neither happens\n'
        '  without the other. This is why the Sanskrit perfect of a light\n'
        '  root looks nothing like a reduplication: पेचुः is what पपचुः\n'
        '  became'
    ),
)

register(
    '6.4.121',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — थलि च सेटि — and the same before थल् WITH an इट्: **पेचिथ,\n'
        '  शेकिथ**.\n'
        '\n'
        'SETTLED — **AND THE WORD थल् IS SAID FOR CLARITY AND NOT FROM\n'
        '  NEED.** **थल्ग्रहणं विस्पष्टार्थम्। अक्ङिदर्थम् एतद् वचनम्\n'
        '  इत्यन्यस्येटोऽसंभवात्** — the rule is stated because थल् is not\n'
        '  कित्, and no other affix of the perfect takes an इट् anyway, so\n'
        '  naming it adds only plainness'
    ),
)

register(
    '6.4.122',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — तॄफलभजत्रपश्च — and four roots the conditions would have\n'
        '  missed: **तेरतुः, तेरुः, तेरिथ; फेलतुः, फेलुः, फेलिथ; भेजतुः,\n'
        '  भेजुः, भेजिथ; त्रेपे, त्रेपाते, त्रेपिरे**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI SAYS WHY EACH OF THE FOUR IS NAMED.**\n'
        '  **तरतेर् गुणार्थं वचनम्। फलिभजोर् आदेशाद्यर्थम्। त्रपेर्\n'
        '  अनेकहल्मध्यार्थम्** — तॄ for the guṇa that would have to happen\n'
        '  first, फल् and भज् because they begin with a substitute, and त्रप्\n'
        '  because it has two consonants before the vowel. Four roots, three\n'
        '  different reasons, all in one line'
    ),
)

register(
    '6.4.123',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — राधो हिंसायाम् — and राध् where INJURY is meant:\n'
        '  **अपरेधतुः, अपरेधुः, अपरेधिथ**.\n'
        '\n'
        'SETTLED — **AND THE tapara IS SET ASIDE HERE.** **अत इत्येतद्\n'
        '  इहोपस्थितं तपरत्वकृतम् अपास्य कालविशेषम् असंभवाद् अवर्णमात्रं\n'
        '  प्रतिपादयति** — राध् has a long आ and no short one, so the tapara\n'
        '  that 6.4.120 carried has to be dropped or the rule would reach\n'
        '  nothing'
    ),
)

register(
    '6.4.124',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — वा जॄभ्रमुत्रसाम् — and three roots OPTIONALLY: **जेरतुः /\n'
        '  जजरतुः; जेरिथ / जजरिथ; भ्रेमतुः / बभ्रमतुः; भ्रेमिथ / बभ्रमिथ;\n'
        '  त्रेसतुः / तत्रसतुः; त्रेसिथ / तत्रसिथ** — each with the copy gone\n'
        '  and each with it kept'
    ),
)

register(
    '6.4.125',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — फणां च सप्तानाम् — and the seven फणादि roots, also\n'
        '  optionally: **फेणतुः / पफणतुः; रेजतुः / रराजतुः; भ्रेजे /\n'
        '  बभ्राजे**. Seven roots and one option, and the vṛtti works each\n'
        '  pair out'
    ),
)

register(
    '6.4.126',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — न शसददवादिगुणानाम् — but not for शस्, not for दद्, not for\n'
        '  the व-initial roots, and not for an अ that GUṆA made: **विशशसतुः,\n'
        '  विशशसुः, विशशसिथ; दददे, दददाते, दददिरे; ववमतुः, ववमुः, ववमिथ;\n'
        '  विशशरतुः, विशशरुः, विशशरिथ; लुलविथ, पुपविथ**. Four classes kept\n'
        '  out at once, and the last of them is not a class of roots at all\n'
        '  but a class of vowels — an अ that was not there in the root'
    ),
)

register(
    '6.4.127',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — अर्वणस्त्रसावनञः — अर्वन् becomes अर्वत् unless a सु\n'
        '  follows it or a नञ् precedes: **अर्वन्तौ, अर्वन्तः; अर्वन्तम्,\n'
        '  अर्वतः; अर्वता, अर्वद्भ्याम्, अर्वद्भिः; अर्वती; आर्वतम्**. Two\n'
        '  conditions in one compound, one about what comes after and one\n'
        '  about what comes before'
    ),
)

register(
    '6.4.128',
    apply=in_the_perfect,
    codification=_IN_THE_PERFECT,
    notes=(
        'SETTLED — मघवा बहुलम् — and मघवन् becomes मघवत् VARIOUSLY: **मघवान्,\n'
        '  मघवन्तौ, मघवन्तः; मघवता; मघवती; माघवतम्**, and **न च भवति — मघवा,\n'
        '  मघवानौ, मघवानः; मघोनः, मघोना, मघवभ्याम्; मघोनी; माघवनम्**. Every\n'
        '  form given twice over, which is what बहुलम् means here and not an\n'
        '  option between two shapes of one word'
    ),
)


_IN_THE_WEAK_STEM = (
    'in_the_weak_stem(stem, gana=..., before=..., part=..., '
    'result=...) -> what the bha stem loses or becomes, and by '
    'which rule of 6.4.129-153.'
)

register(
    '6.4.129',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — भस्य — **भस्येत्ययमधिकारः, आ अध्यायपरिसमाप्तेः। यदित\n'
        "  ऊर्ध्वम् अनुक्रमिष्यामो भस्येत्येवं तद् वेदितव्यम्** — the pāda's\n"
        "  last heading, and it runs to the end of the adhyāya. भ is 1.4.18's\n"
        '  name for the stem before a vowel-initial weak ending or a\n'
        '  taddhita.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI READS THE NEXT SŪTRA OUT AS ITS EXAMPLE,\n'
        '  WITH A COUNTER-EXAMPLE.** **वक्ष्यति पादः पत् — द्विपदः पश्य,\n'
        '  द्विपदा कृतम्। भस्येति किम्? द्विपादौ, द्विपादः** — the same stem\n'
        '  before a strong ending is not भ and keeps its आ'
    ),
)

register(
    '6.4.130',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — पादः पत् — a stem ending in पाद् becomes पद् when it is भ:\n'
        '  **द्विपदः पश्य; द्विपदा; द्विपदे; द्विपदिकां ददाति;\n'
        '  वैयाघ्रपद्यः**. And the पाद meant is the one that has already lost\n'
        '  its आ — **पाद इति पादशब्दो लुप्ताकारो गृह्यते**.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTE TAKES THE NAMED WORD AND NOT WHAT\n'
        '  ENDS IN IT.** **स च निर्दिश्यमानस्यादेशा भवन्ति इति पाच्छब्दस्यैव\n'
        '  भवति, न तदन्तस्य सर्वस्य** — so द्विपदः is द्वि followed by पद्,\n'
        '  and not one new word.\n'
        '\n'
        'SETTLED — **AND THE WITNESSES DISAGREE ABOUT THE TEXT.** GRETIL\n'
        "  reads *vakṣyati - pādaḥ pat*, with the vṛtti's **वक्ष्यति** run\n"
        '  into the sūtra; Vidyut reads **पादः पत्**, which is the sūtra.\n'
        '  Recorded rather than inherited'
    ),
)

register(
    '6.4.131',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — वसोः संप्रसारणम् — a वस्-final भ stem vocalises: **विदुषः\n'
        '  पश्य; विदुषा; विदुषे; पेचुषः; पपुषः**.\n'
        '\n'
        'SETTLED — **AND 6.4.22 DOES NOT HIDE IT FROM WHAT COMES NEXT.**\n'
        '  **आकारलोपे कर्तव्ये वसुसंप्रसारणस्य व्याश्रयत्वाद् असिद्धत्वं न\n'
        '  भवति** — the vocalisation and the आ-loss rest on different things,\n'
        '  so the अत्र of 6.4.22 fails and the second sees the first. And\n'
        '  **वसुग्रहणे क्वसोरपि ग्रहणम् इष्यते** — the क्वसु affix is taken\n'
        '  along with the bare वस्'
    ),
)

register(
    '6.4.132',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — वाह ऊठ् — a वाह्-final भ stem vocalises to ऊठ् and not to\n'
        '  the plain उ: **प्रष्ठौहः, प्रष्ठौहा, प्रष्ठौहे; दित्यौहः,\n'
        "  दित्यौहा, दित्यौहे**. The औ is 6.1.89's, **एत्येधत्यूठ्सु**, which\n"
        '  names ऊठ् by name.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI ASKS WHY ऊठ् AT ALL.** **अथ किमर्थम् ऊठ्\n'
        '  क्रियते, संप्रसारण एव कृते गुणे च वृद्धिरेचि इति वृद्धौ\n'
        "  सत्याम्...** — a plain vocalisation with guṇa and then 6.1.88's\n"
        '  vṛddhi would have reached the same shape, and the ठ् is what makes\n'
        '  6.1.89 apply instead'
    ),
)

register(
    '6.4.133',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — श्वयुवमघोनामतद्धिते — श्वन्, युवन् and मघवन् vocalise\n'
        '  before an affix that is NOT a taddhita: **शुनः, शुना, शुने; यूनः,\n'
        '  यूना, यूने; मघोनः, मघोना, मघोने**.\n'
        '\n'
        'SETTLED — **AND ONE OF THE THREE WAS WORKED OVER FIVE SŪTRAS AGO.**\n'
        '  6.4.128 मघवा बहुलम् made मघवन् into मघवत्, variously; this makes\n'
        '  it मघोन्. The same stem, two rules, and the vṛtti of 6.4.128 gives\n'
        '  both sets of forms side by side'
    ),
)

register(
    '6.4.134',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — अल्लोपोऽनः — an अन्-final भ stem loses that अ: **राज्ञः\n'
        '  पश्य; राज्ञा; राज्ञे; तक्ष्णः पश्य; तक्ष्णा; तक्ष्णे**. This is\n'
        "  the rule that makes राज्ञः out of राजन्, and with 6.4.8's\n"
        '  lengthening for the strong cases it is most of how an न्-final\n'
        '  noun declines'
    ),
)

register(
    '6.4.135',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — षपूर्वहन्धृतराज्ञामणि — and before अण्, the same loss for\n'
        '  an अन् with a ष् before it, and for हन् and धृतराजन्: **औक्ष्णः,\n'
        '  ताक्ष्णः; भ्रौणघ्नः; धार्तराज्ञः**'
    ),
)

register(
    '6.4.136',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — विभाषा ङिश्योः — and before ङि and शी the loss is\n'
        '  OPTIONAL: **राज्ञि / राजनि; साम्नि / सामनि; साम्नी / सामनी**'
    ),
)

register(
    '6.4.137',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — न संयोगाद् वमन्तात् — but not after a cluster ending in व्\n'
        '  or म्: **पर्वणा, पर्वणे; अथर्वणा, अथर्वणे; चर्मणा, चर्मणे**. Both\n'
        '  halves of the condition are tested — a cluster, and one ending in\n'
        '  one of those two sounds'
    ),
)

register(
    '6.4.138',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — अचः — an अच्-final भ stem loses its अ: **दधीचः पश्य;\n'
        '  दधीचा; दधीचे; मधूचः पश्य; मधूचा; मधूचे**. And अच् here is अञ्चति\n'
        '  with its न् already gone — **अच इत्ययम् अञ्चतिर् लुप्तनकारो\n'
        '  गृह्यते** — the same word 6.3.138 called चु'
    ),
)

register(
    '6.4.139',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — उद ईत् — and after उद् the अच् becomes ई: **उदीचः, उदीचा,\n'
        '  उदीचे** — northern, and the word for the north'
    ),
)

register(
    '6.4.140',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — आतो धातोः — an आ-final ROOT that is भ loses that आ:\n'
        '  **कीलालपः पश्य; कीलालपा; कीलालपे; शुभंयः पश्य; शुभंया; शुभंये**.\n'
        '\n'
        'SETTLED — **AND THE SŪTRA IS SPLIT SO THAT आतः CAN CARRY ALONE.**\n'
        '  **आत इति योगविभागः। तेन क्त्वो ल्यप्, हलः श्नः शानच्०\n'
        '  इत्येवमादि...** — divided, the word आतः reaches further than the\n'
        '  whole sūtra could'
    ),
)

register(
    '6.4.141',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — मन्त्रेष्वाङ्यादेरात्मनः — in a मन्त्र, आत्मन् loses its\n'
        '  FIRST sound before आङ्: **त्मना देवेभ्यः; त्मना सोमेषु**. A\n'
        '  vārttika widens it: **आङोऽन्यत्रापि दृश्यते — त्मन्या समञ्जन्**'
    ),
)

register(
    '6.4.142',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — ति विंशतेर्डिति — विंशति loses its ति before a डित् affix:\n'
        '  **विंशत्या क्रीतो विंशकः; विंशतेः पूरणो विंशः; एकविंशः**'
    ),
)

register(
    '6.4.143',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — टेः — and any stem loses its टि before a डित्:\n'
        '  **कुमुद्वान्, नड्वान्, वेतस्वान्; उपसरजः, मन्दुरजः; त्रिंशता\n'
        '  क्रीतस् त्रिंशकः**.\n'
        '\n'
        'SETTLED — **AND THIS ONE REACHES PAST THE HEADING.** **डित्य्\n'
        '  अभस्याप्य् अनुबन्धकरणसामर्थ्यात् टिलोपो भवति** — भस्य is running,\n'
        '  and the mere fact that the ड् marker was put on the affix at all\n'
        '  shows the loss reaches a stem that is not भ as well'
    ),
)

register(
    '6.4.144',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — नस्तद्धिते — an न्-final भ stem loses its टि before a\n'
        "  taddhita: **आग्निशर्मिः, औडुलोमिः**, the इञ् by 4.1.96's बाह्वादि.\n"
        '  A vārttika adds a long list of stems the rule would otherwise miss\n'
        '  — **सब्रह्मचारिपीठसर्पिकलापिकुथुमि...**'
    ),
)

register(
    '6.4.145',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — अह्नष्टखोरेव — अहन् loses its टि before ट and ख and\n'
        '  NOWHERE ELSE: **द्वे अहनी समाहृते द्व्यहः; त्र्यहः; द्व्यहीनः,\n'
        '  त्र्यहीनः; अह्नां समूहः क्रतुर् अहीनः**. **सिद्धे सत्यारम्भो\n'
        '  नियमार्थः** — 6.4.144 had already supplied it, and the एव is what\n'
        '  fences it'
    ),
)

register(
    '6.4.146',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — ओर्गुणः — a उ-final भ stem takes guṇa before a taddhita:\n'
        '  **बाभ्रव्यः, माण्डव्यः; शङ्कव्यं दारु; पिचव्यः कार्पासः;\n'
        '  कमण्डलव्या मृत्तिका; परशव्यम् अयः; औपगवः; कापटवः**.\n'
        '\n'
        'SETTLED — **AND SAYING गुण RATHER THAN ओ IS WHAT LETS ANOTHER FORM\n'
        '  THROUGH.** **ओरोद् इति वक्तव्ये गुणग्रहणं संज्ञापूर्वको विधिर्\n'
        '  अनित्यः यथा स्यात्। तेन स्वायंभुव इति सिद्धं भवति** — an operation\n'
        '  stated by its technical name is not compulsory, and that is how\n'
        '  स्वायंभुव comes out'
    ),
)

register(
    '6.4.147',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — ढे लोपोऽकद्र्वाः — and before ढ the उ is simply DROPPED\n'
        '  instead, कद्रू excepted: **कामण्डलेयः, शैतवाहेयः, जाम्बेयः,\n'
        '  माद्रबाहेयः**'
    ),
)

register(
    '6.4.148',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — यस्येति च — an इ-final or अ-final भ stem loses that vowel\n'
        '  before ई and before a taddhita: **दाक्षी, प्लाक्षी, सखी**.\n'
        '\n'
        'SETTLED — **AND THE LOSS IS STATED RATHER THAN LEFT TO THE\n'
        '  SINGLE-VOWEL RULE FOR A REASON.** **सवर्णदीर्घत्वे हि सत्य्\n'
        '  अतिसखेर् आगच्छतीत्यत्र एकादेशस्यान्तवत्त्वाद् असखि इति घिसंज्ञायाः\n'
        '  प्रतिषेधः स्यात्** — 6.1.101 would have given one long vowel for\n'
        "  two, 6.1.85 would then treat it as the stem's end, and 1.4.7's\n"
        '  exception for सखि would wrongly bite'
    ),
)

register(
    '6.4.149',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः — four stems lose\n'
        '  the य of their penult before ई and a taddhita: **सूर्येणैकदिक्\n'
        '  सौरी बलाका**.\n'
        '\n'
        'SETTLED — **AND WHETHER 6.4.22 HIDES IT DEPENDS ON WHICH AFFIX\n'
        '  FOLLOWS.** **अणि यो यस्येति लोपस् तस्यासिद्धत्वं नास्ति,\n'
        '  व्याश्रयत्वात्। ईकारे तु यस् तस्यासिद्धत्वाद् उपधायकारो\n'
        '  भस्याणन्तस्य सूर्यस्य संबन्धीति लुप्यते** — before अण् the two\n'
        '  rest on different things and the असिद्धत्व fails; before ई they\n'
        '  rest on the same thing and it holds'
    ),
)

register(
    '6.4.150',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        "SETTLED — हलस्तद्धितस्य — a TADDHITA's य after a consonant is lost\n"
        '  before ई: **गार्गी, वात्सी**. **तद्धित इति निवृत्तम्** — the\n'
        '  taddhita is no longer the environment but the thing lost'
    ),
)

register(
    '6.4.151',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        "SETTLED — आपत्यस्य च तद्धितेऽनाति — a PATRONYMIC's य after a\n"
        '  consonant is lost before a taddhita that does not begin with आ:\n'
        '  **गर्गाणां समूहो गार्गकम्; वात्सकम्**. And **तद्धितग्रहणम् ईत्य्\n'
        '  अनापत्यस्यापि लोपार्थम् — सौमी इष्टिः**'
    ),
)

register(
    '6.4.152',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — क्यच्व्योश्च — and before क्य and च्वि: **वात्सीयति,\n'
        '  गार्गीयति; वात्सायते, गार्गायते; गार्गीभूतः, वात्सीभूतः**'
    ),
)

register(
    '6.4.153',
    apply=in_the_weak_stem,
    codification=_IN_THE_WEAK_STEM,
    notes=(
        'SETTLED — बिल्वकादिभ्यश्छस्य लुक् — after the बिल्वकादि stems the छ\n'
        '  of a भ stem is dropped before a taddhita: **बिल्वा यस्यां सन्ति\n'
        '  बिल्वकीया, तस्यां भवा बैल्वकाः; वेणुकीया — वैणुकाः; वेत्रकीया —\n'
        "  वैत्रकाः**. The बिल्वकादि are the नडादि words with 4.2.91's कुक्\n"
        '  already on them — **नडादिषु बिल्वादयः पठ्यन्ते। नडादीनां कुक् च\n'
        '  इति कृतकुगागमा बिल्वकादयो भवन्ति**'
    ),
)


_BEFORE_ISTHA = (
    'before_istha(stem, gana=..., before=..., part=..., '
    'result=..., chandasi=...) -> what the stem loses before '
    'istha/iman/iyas, or that it stands unchanged, by rule of '
    '6.4.154-175.'
)

register(
    '6.4.154',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — तुरिष्ठेमेयस्सु — तृ is lost before इष्ठन्, इमनिच् and\n'
        '  ईयसुन्: **आसुतिं करिष्ठः; विजयिष्ठः; वहिष्ठः; दोहीयसी धेनुः**.\n'
        '\n'
        'SETTLED — **AND THE WHOLE तृ GOES, NOT ITS LAST SOUND.** **सर्वस्य\n'
        '  तृशब्दस्य लोपार्थं वचनम्। अन्त्यस्य हि टेः इत्येव सिद्धः** —\n'
        '  6.4.155 would have taken the last part anyway, so this sūtra can\n'
        '  only be for the whole. And **लुगित्येतद् अत्र नानुवर्तते। तथा हि\n'
        "  सति न लुमताङ्ग०...** — a लुक् would have stopped the affix's own\n"
        '  effects by 1.1.63, and a लोप does not'
    ),
)

register(
    '6.4.155',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — टेः — and any भ stem loses its टि before the three: **पटु\n'
        '  — पटिष्ठः, पटिमा, पटीयान्; लघु — लघिष्ठः, लघिमा, लघीयान्**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA CARRIES THE WHOLE OF THIS RUN INTO THE\n'
        '  CAUSAL.** **णाविष्ठवत् प्रातिपदिकस्य कार्यं भवति इति वक्तव्यम्** —\n'
        '  before णि a stem is treated as it would be before इष्ठन्, and the\n'
        '  vṛtti lists what that buys: **पुंवद्भावरभावटिलोपयणादिपरार्थम् —\n'
        '  एनीम् आचष्टे एतयति; श्येतयति**'
    ),
)

register(
    '6.4.156',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च\n'
        '  गुणः — six stems lose everything from a semivowel onward AND take\n'
        '  guṇa in what is left: **स्थविष्ठः, स्थवीयान्; दविष्ठः, दवीयान्;\n'
        '  यविष्ठः, यवीयान्; ह्रसिष्ठः, ह्रसिमा, ह्रसीयान्; क्षेपिष्ठः;\n'
        '  क्षोदिष्ठः**. One rule doing two things, and the second of them\n'
        '  stated because the first would have left no vowel to strengthen'
    ),
)

register(
    '6.4.157',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां\n'
        '  प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः — ten stems and ten\n'
        '  substitutes, matched ONE TO ONE: **प्रेष्ठः, प्रेमा, प्रेयान्**\n'
        '  for प्रिय; **स्थेष्ठः, स्थेयान्** for स्थिर; **स्फेष्ठः** for\n'
        '  स्फिर. The longest यथासंख्यम् in the pāda, and crossing any pair\n'
        '  is not Sanskrit'
    ),
)

register(
    '6.4.158',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — बहोर्लोपो भू च बहोः — after बहु the three affixes are\n'
        '  themselves LOST, and बहु becomes भू: **भूमा, भूयान्**.\n'
        '\n'
        'SETTLED — **AND बहोः IS SAID TWICE FOR A REASON.** **बहोरिति\n'
        '  पुनर्ग्रहणं स्थानित्वप्रतिपत्त्यर्थम्, अन्यथा हि प्रत्ययानाम् एव\n'
        '  भूभावः स्यात्** — with the word said once, the भू would have\n'
        '  replaced the affixes that were just deleted. Saying it again fixes\n'
        '  what the substitute stands in place of'
    ),
)

register(
    '6.4.159',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — इष्ठस्य यिट् च — but इष्ठन् takes the augment यिट् instead\n'
        '  of going, and बहु still becomes भू: **भूयिष्ठः**. **लोपापवादो\n'
        '  यिडागमः, तस्मिन् इकार उच्चारणार्थः** — an exception to the loss,\n'
        '  and the इ of the augment is there only to pronounce it by'
    ),
)

register(
    '6.4.160',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — ज्यादाद् ईयसः — after ज्य the ईयस् takes आ: **ज्यायान्**.\n'
        '\n'
        'SETTLED — **AND आ IS SAID RATHER THAN LEAVING IT TO THE LOSS.**\n'
        '  **लोपस्य यिटा व्यवहितत्वाद् आद् इत्युच्यते। लोपे हि सति अकृद्यकारे\n'
        '  इति दीर्घत्वेन ज्यायान् इति सिध्यति** — the यिट् of 6.4.159 stands\n'
        '  between, so the loss cannot reach; hence a substitute of its own'
    ),
)

register(
    '6.4.161',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — र ऋतो हलादेर्लघोः — an ऋ that is LIGHT and has a consonant\n'
        '  before it becomes र before the three: **प्रथिष्ठः, प्रथिमा,\n'
        '  प्रथीयान्; म्रदिष्ठः, म्रदिमा, म्रदीयान्**. Three conditions and a\n'
        '  counter-example for each'
    ),
)

register(
    '6.4.162',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — विभाषर्जोश्छन्दसि — and ऋजु takes it OPTIONALLY in the\n'
        "  Veda, though 6.4.161's condition of a preceding consonant fails:\n"
        '  **रजिष्ठम् अनु नेषि पन्थाम्** beside **त्वम् ऋजिष्ठः**'
    ),
)

register(
    '6.4.163',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — प्रकृत्यैकाच् — a भ stem of ONE VOWEL stands unchanged\n'
        '  before the three: **स्रग्विन् — स्रजिष्ठः, स्रजीयान्, स्रजयति;\n'
        '  स्रुग्वत् — स्रुचिष्ठः, स्रुचीयान्, स्रुचयति**.\n'
        '\n'
        'SETTLED — **AND FROM HERE THE RUN REVERSES.** Everything from\n'
        '  6.4.154 to 6.4.162 took something away; from this sūtra to 6.4.173\n'
        '  the word is प्रकृत्या and the content of each rule is that the\n'
        '  loss does NOT happen. A vārttika adds one more: **प्रकृत्याके\n'
        '  राजन्यमनुष्य...**'
    ),
)

register(
    '6.4.164',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — इन्नण्यनपत्ये — an इन्-final stem stands unchanged before\n'
        '  अण्, where no DESCENDANT is meant: **सांकूटिनम्, सांराविणम्,\n'
        "  सांमार्जिनम्; स्रग्विण इदं स्राग्विणम्**. The इनुण् is 3.3.44's\n"
        "  and the अण् 5.4.15's"
    ),
)

register(
    '6.4.165',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — गाथिविदथिकेशिगणिपणिनश्च — and five stems stand unchanged\n'
        '  before अण् even WHERE a descendant is meant: **गाथिनोऽपत्यं\n'
        '  गाथिनः; वैदथिनः; कैशिनः; गाणिनः; पाणिनः**. **अपत्यार्थोऽयम्\n'
        '  आरम्भः** — the sūtra exists for exactly the case 6.4.164 shut out.\n'
        "  And the grammarian's own name is one of the five"
    ),
)

register(
    '6.4.166',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — संयोगादिश्च — and an इन्-final stem BEGINNING with a\n'
        '  cluster, descendant or no: **शङ्खिनोऽपत्यं शाङ्खिनः; माद्रिणः;\n'
        '  वाज्रिणः**'
    ),
)

register(
    '6.4.167',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — अन् — an अन्-final stem stands unchanged before अण्,\n'
        '  **अपत्ये चानपत्ये च**: **सामनः, वैमनः, सौत्वनः, जैत्वनः**.\n'
        '\n'
        "SETTLED — **AND THIS IS WHAT 6.4.135's COUNTER-EXAMPLES WERE\n"
        '  POINTING AT.** **अन् इति प्रकृतिभावेन अल्लोपटिलोपाव् उभाव् अपि न\n'
        '  भवतः** — both the अ-loss of 6.4.134 and the टि-loss of 6.4.144 are\n'
        '  held off at once, which is why सामनः keeps its whole ending'
    ),
)

register(
    '6.4.168',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — ये चाभावकर्मणोः — and before a य-initial taddhita, where\n'
        '  neither the ACT nor the OBJECT is meant: **सामसु साधुः सामन्यः;\n'
        "  वेमन्यः**. The यक् is 5.1.128's, राजन् standing in its पुरोहितादि\n"
        '  list'
    ),
)

register(
    '6.4.169',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — आत्माध्वानौ खे — आत्मन् and अध्वन् stand unchanged before\n'
        '  ख: **आत्मने हित आत्मनीनः; अध्वानम् अलंगामी अध्वनीनः**'
    ),
)

register(
    '6.4.170',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — न मपूर्वोऽपत्येऽवर्मणः — but an अन् with a म् before it\n'
        '  does NOT stand unchanged before अण् where a descendant is meant,\n'
        '  वर्मन् excepted: **सुषाम्णोऽपत्यं सौषामः; चान्द्रसामः**. A\n'
        '  vārttika offers an option: **मपूर्वप्रतिषेधे वा हितनाम्नः इति\n'
        '  वक्तव्यम्**'
    ),
)

register(
    '6.4.171',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — ब्राह्मोऽजातौ — ब्राह्म is laid down, with the टि-loss,\n'
        '  where no CLASS is meant: **ब्राह्मो गर्भः; ब्राह्मम् अस्त्रम्;\n'
        '  ब्राह्मं हविः**. And it is reached by dividing the sūtra:\n'
        '  **योगविभागोऽत्र क्रियते। ब्राह्म इत्येतद् अपत्याधिकारेऽपि\n'
        '  सामर्थ्याद् अपत्याद् अन्यत्राणि टिलोपार्थं निपात्यते**'
    ),
)

register(
    '6.4.172',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — कार्मस्ताच्छील्ये — कार्म is laid down with the टि-loss\n'
        '  where a HABIT is meant: **कर्मशीलः कार्मः**, the ण from 4.4.62.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI ASKS WHY THE SŪTRA IS THERE AT ALL.**\n'
        '  **यद्येवं किमर्थम् इदम्, नस्तद्धिते इत्येव टिलोपः सिद्धः? सत्यम्\n'
        '  एतत्। ज्ञापकार्थं तु। एतज् ज्ञापयति — ताच्छीलिके णेऽण्कृत...** —\n'
        '  6.4.144 had already supplied the loss, so this sūtra can only be\n'
        '  teaching something about the ण of habit'
    ),
)

register(
    '6.4.173',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — औक्षमनपत्ये — औक्ष is laid down with the टि-loss where no\n'
        '  descendant is meant: **औक्षं पदम्**. **अनपत्य इति किम्?\n'
        '  उक्ष्णोऽपत्यम् औक्ष्णः** — and there 6.4.135 takes the अ instead,\n'
        '  so the two rules divide उक्षन् between them by sense'
    ),
)

register(
    '6.4.174',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED —\n'
        '  दाण्डिनायनहास्तिनायनाथर्वणिकजैह्माशिनेयवासिनायनिभ्रौणहत्यधैवत्यसारवैक्ष्वाकमैत्रेयहिरण्मयानि\n'
        '  — eleven words laid down whole. The vṛtti works each back to a\n'
        '  rule it escaped: **दण्डिन् हस्तिन् इत्येतौ नडादिषु पठ्येते, तयोर्\n'
        '  आयने परतः प्रकृतिभावो निपात्यते** — and it records a disagreement\n'
        '  about the list it appeals to: **केषांचित् तु हस्तिन् इति नडादिषु न\n'
        '  पठ्यते**'
    ),
)

register(
    '6.4.175',
    apply=before_istha,
    codification=_BEFORE_ISTHA,
    notes=(
        'SETTLED — ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि छन्दसि — and five\n'
        '  more for the Veda: **ऋतौ भवम् ऋत्व्यम्; वास्तौ भवं वास्त्व्यम्;\n'
        '  वस्तुनि भवो वास्त्वम्**. Each is a यण् where the ordinary rule\n'
        '  would have given guṇa — **ऋतु वास्तु इत्येतयोर् यति यणादेशो\n'
        '  निपात्यते** — and this is the last sūtra of अध्याय ६'
    ),
)


register(
    '6.4.22',
    apply=visible,
    codification=(
        "visible(done, to, same_locus=...) -> whether one operation's work is seen by another."
    ),
    notes=(
        'SETTLED — an adhikāra to the end of the adhyāya, 6.4.175, and\n'
        '  आ भात् is an अभिविधि so that the भ section is included: तेन\n'
        '  भाधिकारेऽप्यसिद्धवद् भवति.\n'
        '\n'
        'SETTLED — the अत्र is not decoration. अत्रग्रहणं\n'
        '  समानाश्रयत्वप्रतिपत्त्यर्थम् — the two operations must rest on\n'
        '  the same thing. व्याश्रयं तु नासिद्धवद् भवति, and पपुषः पश्य,\n'
        '  चिच्युषः पश्य are the counter-examples: the saṃprasāraṇa is on\n'
        '  the affix and the ā-elision on the stem, so no asiddhatva.\n'
        '  Codified as an input, since whether two operations share a\n'
        '  locus is a fact about the derivation.\n'
        '\n'
        "SETTLED — the purpose is the same two halves as 8.2.1's:\n"
        '  उत्सर्गलक्षणभावार्थम् आदेशलक्षणप्रतिषेधार्थं च. एधि and शाधि\n'
        "  keep 6.4.101's धि because the एत्व and the शाभाव are invisible\n"
        "  to it; आगहि and जहि keep their हि because 6.4.105's लुक् cannot\n"
        '  see the anunāsika-elision.\n'
        '\n'
        'SETTLED — and one paribhāṣā is switched off inside it: असिद्धं\n'
        '  बहिरङ्गम् अन्तरङ्गे does not operate here, एषा हि परिभाषा\n'
        '  आभाच्छास्त्रीया — being itself of this section, it is asiddha\n'
        '  along with everything else, and the inner and outer never come\n'
        '  up together for it to judge. Recorded; not modelled, since\n'
        '  antaraṅga is carried as a `Strength` on `vipratisedha` rather\n'
        '  than derived.\n'
        '\n'
        'SCOPE — the vārttika वुग्युटावुवङ्यणोः सिद्धौ is not codified.'
    ),
)


register(
    '6.4.77',
    apply=iyan_uvan,
    codification=(
        "iyan_uvan(stem, dhatu=..., snu=..., bhru=..., "
        "ardhadhatuka=..., dhatu_lopa=...) -> इयङ् or उवङ् for the "
        "stem's final i or u before a vowel affix, or the rule "
        "standing down where the strengthening was not stopped."
    ),
    notes=(
        'SETTLED — अचि श्नुधातुभ्रुवां य्वोरियङुवङौ — इयङ् for a final i,\n'
        '  उवङ् for a final u, before a vowel affix. Only for three things:\n'
        '  an aṅga ending in the affix श्नु, a धातु, and भ्रू.\n'
        '  श्नुधातुभ्रुवामिति किम्? लक्ष्म्यै, वध्वै — neither is one of the\n'
        '  three and neither takes it.\n'
        '\n'
        'SETTLED — **AND IT DOES NOT ORDINARILY GET TO APPLY AT ALL.** The\n'
        '  Kāśikā is explicit: इयङुवङ्भ्यां गुणवृद्धी भवतो विप्रतिषेधेन —\n'
        '  where guṇa or vṛddhi is also available, those win by 1.4.2, and\n'
        '  चयनम्, चायकः, लवनम्, लावकः are the forms that result. So this\n'
        '  rule is reached only where the strengthening has been stopped by\n'
        '  something else, and the something else is usually one of the\n'
        '  three prohibitions.\n'
        '\n'
        'SETTLED — that is why the guṇa is asked about here rather than\n'
        '  assumed away. लू with अच् gives लोलवः if the strengthening\n'
        '  stands and लोलुवः if it does not, and the whole difference is\n'
        '  1.1.4 न धातुलोप आर्धधातुके — which is reached because the same\n'
        '  अच् elided the यङ्. With the strengthening standing, the\n'
        '  form is लोलवः: guṇa gives ओ and 6.1.78 एचोऽयवायावः turns that\n'
        '  into अव्. Stop it and उवङ् reaches the ऊ instead, giving उव.\n'
        '\n'
        'SCOPE — the छन्दस् vārttika, इयङुवङ्प्रकरणे तन्वादीनां छन्दसि\n'
        '  बहुलमुपसंख्यानम् — तनुवं beside तन्वं, सुवर्गः beside स्वर्गः —\n'
        '  is not modelled.'
    ),
)


__all__ = ['augment_or_yan', 'before_ardhadhatuka', 'before_sarvadhatuka', 'in_the_perfect', 'before_istha', 'in_the_weak_stem', 'iyan_uvan', 'n_goes', 'the_nasal', 'to_the_stem', 'visible']
