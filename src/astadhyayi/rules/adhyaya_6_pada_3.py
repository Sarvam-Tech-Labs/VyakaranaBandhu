# -*- coding: utf-8 -*-
"""
अध्याय ६, पाद ३ — what happens to the FIRST member before a second.

6.2 asked where the accent of a compound falls. This pāda asks what
the first member LOOKS like once a second stands after it, and 6.3.1
opens two headings at once to say so: अलुक्, the case ending that does
not drop, and उत्तरपदे, the position everything here is stated for.
The vṛtti gives both bounds in one line — अलुगधिकारः प्रागानङः।
उत्तरपदाधिकारः प्रागङ्गाधिकारात् — so अलुक् holds twenty-four sūtras
and उत्तरपदे holds all hundred and thirty-nine.

Inside that, the pāda is a sequence of things done to the first
member: the ending kept (6.3.1–24), आनङ् and the dvandva
substitutions (6.3.25–33), a feminine stem behaving as a masculine
(6.3.34–45), and then substitution after substitution — महत् → महा,
हृदय → हृद्, पाद → पद्, उदक → उद, नञ् → अ, सह → स, समान → स.
"""

from __future__ import annotations

from src.astadhyayi.aluk import stays
from src.astadhyayi.dirgha_samhita import lengthens
from src.astadhyayi.purvapada_vikara import altered
from src.astadhyayi.hrasva_mum import adjusts
from src.astadhyayi.nan_saha_samana import shaped
from src.astadhyayi.anan_dvandva import substitute
from src.astadhyayi.pumvadbhava import behaves_as
from src.astadhyayi.purvapada_adesa import replaced_by
from src.astadhyayi.sources import register

_STAYS = (
    'stays(purvapada, gana=..., uttarapada=..., '
    'uttarapada_gana=..., samasa=..., result=...) -> which case '
    'ending stays inside the compound instead of being dropped by '
    '2.4.71, and by which rule of 6.3.1-24.'
)

register(
    '6.3.1',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — अलुगुत्तरपदे — **अलुगिति च, उत्तरपद इति चैतदधिकृतं\n'
        '  वेदितव्यम्। यदित ऊर्ध्वमनुक्रमिष्यामोऽलुगुत्तरपद इत्येवं तद्\n'
        '  वेदितव्यम्** — from here a case ending that 2.4.71 would have\n'
        '  dropped inside the compound STAYS, so long as something follows\n'
        '  it. The vṛtti reads the next sūtra out as its example: **वक्ष्यति\n'
        '  पञ्चम्याः स्तोकादिभ्यः — स्तोकान्मुक्तः, अल्पान्मुक्तः**.\n'
        '\n'
        'SETTLED — **AND उत्तरपदे IS SAID FOR SOMETHING OTHER THAN WHAT IT\n'
        '  MEANS.** **उत्तरपद इति किम्? निष्क्रान्तः स्तोकाद् निःस्तोकः** —\n'
        '  there स्तोक is the second word and nothing follows, so no ending\n'
        '  survives. But the vṛtti says that is not why the word is there:\n'
        '  **अन्यार्थम् इदम् उत्तरपदग्रहणम् इहाप्यलुको निवृत्तिं\n'
        '  करोतीत्येवमर्थं लक्षणप्रतिपदोक्तपरिभाषा नाश्रयितव्या** — without\n'
        '  it one would have to invoke the paribhāṣā that a rule framed by\n'
        '  description does not reach what another rule names outright.\n'
        '  Stating position instead settles it without the paribhāṣā.\n'
        '\n'
        "SETTLED — **AND THE HEADING'S TWO WORDS STOP IN DIFFERENT PLACES.**\n"
        '  **अलुगधिकारः प्रागानङः। उत्तरपदाधिकारः प्रागङ्गाधिकारात्** — अलुक्\n'
        '  to 6.3.24, where 6.3.25 आनङ् takes over; उत्तरपदे to the end of\n'
        '  the pāda, stopping only at 6.4.1 अङ्गस्य. The fourth heading in\n'
        '  two pādas built this way'
    ),
)

register(
    '6.3.2',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — पञ्चम्याः स्तोकादिभ्यः — an ablative stays after a word\n'
        '  meaning A LITTLE, NEAR, FAR or WITH DIFFICULTY: **स्तोकान्मुक्तः,\n'
        '  अल्पान्मुक्तः; अन्तिकादागतः, अभ्याशादागतः; दूरादागतः,\n'
        '  विप्रकृष्टादागतः; कृच्छ्रान्मुक्तः** — freed by a hair, come from\n'
        '  nearby, come from far off, barely got away.\n'
        '\n'
        'SETTLED — **AND THE FOUR ARE SENSES AND NOT WORDS.**\n'
        '  **स्तोकान्तिकदूरार्थकृच्छ्राणि स्तोकादीनि** — which is why अल्प\n'
        '  goes with स्तोक and विप्रकृष्ट with दूर.\n'
        '\n'
        'SETTLED — **AND THE DUAL AND PLURAL ARE OUT FOR A REASON THAT IS NOT\n'
        '  GRAMMATICAL.** **द्विवचनबहुवचनान्तानां तु स्तोकादीनाम् अनभिधानात्\n'
        '  समास एव न भवति — स्तोकाभ्यां मुक्तः, स्तोकेभ्यो मुक्त इति। तेनात्र\n'
        '  न कदाचिद् ऐकपद्यम् ऐकस्वर्यं च भवति** — nobody says it, so there\n'
        '  is no compound to keep an ending in, and hence neither one word\n'
        '  nor one accent. A vārttika adds one more: **ब्राह्मणाच्छंसिन\n'
        '  उपसंख्यानम्**'
    ),
)

register(
    '6.3.3',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — ओजःसहोऽम्भस्तमसस्तृतीयायाः — an instrumental stays after\n'
        '  these four: **ओजसाकृतम्, सहसाकृतम्, अम्भसाकृतम्, तमसाकृतम्** —\n'
        '  done by force, done by strength, done by water, done in the dark.\n'
        '\n'
        'SETTLED — **AND TWO VĀRTTIKAS ADD TO IT.** **अञ्जस उपसंख्यानम् —\n'
        '  अञ्जसाकृतम्**, and **पुंसानुजो जनुषान्ध इति वक्तव्यम् — पुंसानुजः,\n'
        '  जनुषान्धः** — born after a male child, blind from birth. The\n'
        '  second adds two whole compounds rather than a stem'
    ),
)

register(
    '6.3.4',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — मनसः संज्ञायाम् — an instrumental stays after मनस् where\n'
        '  the compound is a NAME: **मनसादत्ता, मनसागुप्ता, मनसासंगता** —\n'
        "  women's names, given by the heart, guarded by the heart"
    ),
)

register(
    '6.3.5',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — आज्ञायिनि च — and before आज्ञायिन्, whether or not the\n'
        '  compound is a name: **मनसा आज्ञातुं शीलमस्य मनसाज्ञायी** — one\n'
        '  whose way it is to understand by the mind alone'
    ),
)

register(
    '6.3.6',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — आत्मनश्च पूरणे — an instrumental stays after आत्मन् before\n'
        '  an ORDINAL: **आत्मनापञ्चमः, आत्मनाषष्ठः** — himself the fifth,\n'
        '  himself the sixth, a man counted in with four others.\n'
        '\n'
        'SETTLED — **AND BOTH THE CASE AND THE COMPOUND COME FROM SOMEWHERE\n'
        '  ELSE.** **तृतीयाविधाने प्रकृत्यादिभ्य उपसंख्यानम् इति तृतीया।\n'
        '  तृतीयेति योगविभागात् समासः** — the instrumental by a vārttika on\n'
        '  2.3.18, and the compound by splitting 2.1.30 in two. And the vṛtti\n'
        '  answers the obvious objection: **कथं जनार्दनस् त्वात्मचतुर्थ\n'
        '  एवेति? बहुव्रीहिरयम्**'
    ),
)

register(
    '6.3.7',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — वैयाकरणाख्यायां चतुर्थ्याः — a dative stays after आत्मन्\n'
        '  in a term GRAMMARIANS use: **आत्मनेपदम्, आत्मनेभाषा**. The vṛtti\n'
        '  glosses the condition twice over — **वैयाकरणानाम् आख्या\n'
        '  वैयाकरणाख्या। आख्या संज्ञा। यया संज्ञया वैयाकरणा एव व्यवहरन्ति** —\n'
        '  a name in which only grammarians deal. The dative is **तादर्थ्ये\n'
        '  चतुर्थी** and the compound again **चतुर्थीति योगविभागात्**'
    ),
)

register(
    '6.3.8',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — परस्य च — and after पर in the same kind of term:\n'
        '  **परस्मैपदम्, परस्मैभाषा**. Two sūtras for the two halves of one\n'
        '  pair of names, and the pair is what 1.4.99–100 then use to sort\n'
        '  every ending in the grammar'
    ),
)

register(
    '6.3.9',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — हलदन्तात् सप्तम्याः संज्ञायाम् — a locative stays after a\n'
        '  stem ending in a CONSONANT or in अ, where the compound is a NAME:\n'
        '  **युधिष्ठिरः, त्वचिसारः; अरण्येतिलकाः, अरण्येमाषकाः, वनेकिंशुकाः,\n'
        '  वनेहरिद्रकाः, वनेबल्वजकाः, पूर्वाह्णेस्फोटकाः, कूपेपिशाचकाः** —\n'
        '  steady in battle, and the names of plants and places.\n'
        '\n'
        'SETTLED — **AND ONE FAMOUS NAME IS NOT REACHED BY THIS RULE AT\n'
        '  ALL.** **गविष्ठिर इत्यत्र तु गवियुधिभ्यां स्थिरः इत्यत एव वचनाद्\n'
        '  अलुक्** — गो ends in neither, so the locative in गविष्ठिरः is kept\n'
        '  by 8.3.95 naming it, not by this.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA ADDS TWO STEMS OUTRIGHT.**\n'
        '  **हृद्द्युभ्यां ङेः — हृदिस्पृक्, दिविस्पृक्** — touching the\n'
        '  heart, touching the sky, with no condition that the compound be a\n'
        '  name'
    ),
)

register(
    '6.3.10',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — कारनाम्नि च प्राचां हलादौ — the same locative stays in an\n'
        '  EASTERN name for a due payment, before a second member beginning\n'
        '  with a consonant: **स्तूपेशाणः, दृषदिमाषकः, हलेद्विपदिका,\n'
        '  हलेत्रिपदिका**.\n'
        '\n'
        'SETTLED — **AND THE RULE GRANTS NOTHING — IT NARROWS.**\n'
        '  **कारविशेषस्य संज्ञा एताः, तत्र पूर्वेणैव सिद्धे नियमार्थम् इदम्**\n'
        '  — 6.3.9 had already supplied every one of these, all of them being\n'
        '  names. What 6.3.10 does is fence them: **एते च त्रयो नियमविकल्पा\n'
        '  अत्रेष्यन्ते — कारनाम्न्येव, प्राचामेव, हलादावेवेति**, three\n'
        '  restrictions from one sūtra, each with its own counter-example'
    ),
)

register(
    '6.3.11',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — मध्याद्गुरौ — a locative stays after मध्य before गुरु:\n'
        '  **मध्येगुरुः** — a metrical foot heavy in the middle. A vārttika\n'
        '  adds the other end: **अन्ताच्चेति वक्तव्यम् — अन्तेगुरुः**. And\n'
        '  the compound is again **सप्तमीति योगविभागात्**, the same split\n'
        '  6.3.6 and 6.3.7 leaned on for their own cases'
    ),
)

register(
    '6.3.12',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — अमूर्धमस्तकात् स्वाङ्गादकामे — a locative stays after a\n'
        '  word for a PART OF THE BODY, मूर्धन् and मस्तक excepted, and not\n'
        '  before काम: **कण्ठे कालोऽस्य कण्ठेकालः; उरसिलोमा; उदरेमणिः** —\n'
        "  blue-throated, hairy-chested, jewel-bellied. 6.3.9's हलदन्तात् is\n"
        '  still running, which is what keeps अङ्गुलित्राणः out'
    ),
)

register(
    '6.3.13',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — बन्धे च विभाषा — before बन्ध the locative stays\n'
        '  OPTIONALLY: **हस्तेबन्धः / हस्तबन्धः; चक्रेबन्धः / चक्रबन्धः**.\n'
        '  And बन्ध here is one particular formation: **बन्ध इति घञन्तो\n'
        '  गृह्यते**.\n'
        '\n'
        'SETTLED — **AND THE OPTION WORKS IN BOTH DIRECTIONS AT ONCE.**\n'
        '  **उभयत्रविभाषेयम्। स्वाङ्गाद्धि बहुव्रीहौ पूर्वेण नित्यम् अलुक्\n'
        '  प्राप्नोति। तत्पुरुषे तु स्वाङ्गाद् अस्वाङ्गात् च\n'
        '  नेन्सिद्धबध्नातिषु च इति प्रतिषेधः प्राप्नोति** — in a बहुव्रीहि\n'
        '  from a body-part, 6.3.12 would have kept the ending always, so the\n'
        '  option takes it away; in a तत्पुरुष, 6.3.19 would have refused it\n'
        '  always, so the option grants it. One विभाषा facing opposite ways'
    ),
)

register(
    '6.3.14',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — तत्पुरुषे कृति बहुलम् — in a तत्पुरुष before a कृत्-formed\n'
        '  second member the locative stays VARIOUSLY: **स्तम्बेरमः,\n'
        '  कर्णेजपः** — one that sports in the thicket, one who whispers in\n'
        '  the ear. **न च भवति — कुरुचरः, मद्रचरः**, where it does not.\n'
        '  बहुलम् is not an option offering two forms of one word: it is the\n'
        '  statement that both happen and the rule does not say which'
    ),
)

register(
    '6.3.15',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — प्रावृट्शरत्कालदिवां जे — a locative stays after these\n'
        '  four before ज: **प्रावृषिजः, शरदिजः, कालेजः, दिविजः** — born in\n'
        '  the rains, born in autumn, born in due season, born in heaven. The\n'
        '  vṛtti marks it as no more than a spelling-out of the rule before:\n'
        '  **पूर्वस्यैवायं प्रपञ्चः**'
    ),
)

register(
    '6.3.16',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — विभाषा — and after four more, optionally: **वर्षेजः /\n'
        '  वर्षजः; क्षरेजः / क्षरजः; शरेजः / शरजः; वरेजः / वरजः**. The bare\n'
        '  word विभाषा for a whole sūtra, with everything else carried down'
    ),
)

register(
    '6.3.17',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — घकालतनेषु कालनाम्नः — after a word naming a TIME, the\n'
        '  locative stays optionally before घ, before the word काल, and\n'
        '  before तन: **पूर्वाह्णेतरे / पूर्वाह्णतरे; पूर्वाह्णेतमे /\n'
        '  पूर्वाह्णतमे; पूर्वाह्णेकाले / पूर्वाह्णकाले; पूर्वाह्णेतने /\n'
        '  पूर्वाह्णतने**.\n'
        '\n'
        'SETTLED — **AND NAMING AN AFFIX HERE DOES NOT REACH WHAT ENDS IN\n'
        '  IT.** **उत्तरपदाधिकारे प्रत्ययग्रहणे तदन्तविधिर्नेष्यते** — under\n'
        '  the उत्तरपद heading, naming an affix names the affix and not a\n'
        '  stem ending in it. And the vṛtti says how that is known: **हृदयस्य\n'
        '  हृल्लेख० इति लेखग्रहणाद् लिङ्गात्** — from 6.3.50 having to say\n'
        '  लेख at all'
    ),
)

register(
    '6.3.18',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — शयवासवासिष्वकालात् — before शय, वास or वासिन्, and NOT\n'
        '  after a time-word, the locative stays optionally: **खेशयः / खशयः;\n'
        '  ग्रामेवासः / ग्रामवासः; ग्रामेवासी / ग्रामवासी** — lying in the\n'
        '  open, dwelling in the village.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA ADDS A STEM WITH THREE SECOND MEMBERS OF\n'
        '  ITS OWN.** **अपो योनियन्मतुषु सप्तम्या अलुग् वक्तव्यः —\n'
        '  अप्सुयोनिः, अप्सव्यः, अप्सुमन्तौ** — born in the waters, of the\n'
        "  waters, having waters. The यत् there is by 4.3.54's दिगादि"
    ),
)

register(
    '6.3.19',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — नेन्सिद्धबध्नातिषु च — but the locative does NOT stay\n'
        '  before a second member ending in इन्, before सिद्ध, or before a\n'
        '  form of बध्: **स्थण्डिलवर्ती; सांकाश्यसिद्धः, काम्पिल्यसिद्धः;\n'
        '  चक्रबद्धः, चारबद्धः** — each of them a कृदन्त that 6.3.14 would\n'
        '  otherwise have reached.\n'
        '\n'
        'SETTLED — **AND ONE OF ITS OWN EXAMPLES IS DISPUTED.** **चक्रबन्ध\n'
        '  इति केचिद् उदाहरन्ति तत् पचाद्यजन्तं द्रष्टव्यम्। घञन्ते हि बन्धे\n'
        '  च विभाषा इत्युक्तम्** — some cite चक्रबन्धः here, and it can only\n'
        "  be the अच्-formed word, since the घञ्-formed one is 6.3.13's and\n"
        '  optional'
    ),
)

register(
    '6.3.20',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — स्थे च भाषायाम् — nor before स्थ, in the SPOKEN language:\n'
        '  **समस्थः, विषमस्थः, कूटस्थः, पर्वतस्थः** — standing level,\n'
        '  standing on a peak. Naming the register is what leaves the Veda\n'
        '  alone, and the Vedic form is quoted to show it: **कृष्णोऽस्य\n'
        '  आखरेष्ठः**'
    ),
)

register(
    '6.3.21',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — षष्ठ्या आक्रोशे — a genitive stays where ABUSE is meant:\n'
        "  **चौरस्यकुलम्, वृषलस्यकुलम्** — a thief's family, a serf's family.\n"
        '\n'
        'SETTLED — **AND THE VĀRTTIKAS ON THIS ONE SŪTRA CARRY MOST OF THE\n'
        '  GENITIVES SANSKRIT ACTUALLY KEEPS.** **षष्ठीप्रकरणे\n'
        '  वाग्दिक्पश्यद्भ्यो युक्तिदण्डहरेषु यथासंख्यम् अलुग् वक्तव्यः —\n'
        '  वाचोयुक्तिः, दिशोदण्डः, पश्यतोहरः**, matched one to one;\n'
        '  **आमुष्यायणामुष्यपुत्रिकामुष्यकुलिकेति चालुग् वक्तव्यः**;\n'
        '  **देवानांप्रिय इत्यत्र च षष्ठ्या अलुग् वक्तव्यः**;\n'
        '  **शेपपुच्छलाङ्गूलेषु शुनः संज्ञायां षष्ठ्या अलुग् वक्तव्यः —\n'
        '  शुनःशेपः, शुनःपुच्छः, शुनोलाङ्गूलः**; and **दिवश्च दासे षष्ठ्या\n'
        '  अलुग् वक्तव्यः — दिवोदासाय गायति**. Śunaḥśepa and Divodāsa are\n'
        '  named men, and neither is reachable from a sūtra'
    ),
)

register(
    '6.3.22',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — पुत्रेऽन्यतरस्याम् — before पुत्र, still in abuse, the\n'
        '  genitive stays OPTIONALLY: **दास्याःपुत्रः / दासीपुत्रः;\n'
        '  वृषल्याःपुत्रः / वृषलीपुत्रः** — son of a slave woman, son of a\n'
        '  serf woman'
    ),
)

register(
    '6.3.23',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — ऋतो विद्यायोनिसम्बन्धेभ्यः — a genitive stays after an\n'
        '  ऋ-final word naming a relation of LEARNING or of BIRTH:\n'
        '  **होतुरन्तेवासी, होतुःपुत्रः; पितुरन्तेवासी, पितुःपुत्रः** — the\n'
        "  Hotṛ's pupil, the father's son.\n"
        '\n'
        'SETTLED — **AND THE CONDITION HAS TO HOLD OF BOTH MEMBERS.**\n'
        '  **विद्यायोनिसंबन्धेभ्यस्तत्पूर्वोत्तरपदग्रहणम्।\n'
        '  विद्यायोनिसंबन्धवाचिन्येवोत्तरपदे यथा स्याद्, अन्यत्र मा भूत् —\n'
        "  होतृधनम्, पितृधनम्, होतृगृहम्, पितृगृहम्** — a Hotṛ's money is not\n"
        '  a relation of learning, so the ending goes'
    ),
)

register(
    '6.3.24',
    apply=stays,
    codification=_STAYS,
    notes=(
        'SETTLED — विभाषा स्वसृपत्योः — and before स्वसृ and पति, optionally:\n'
        '  **मातुःष्वसा / मातृष्वसा; दुहितुःपतिः / दुहितृपतिः; ननान्दुःपतिः /\n'
        '  ननान्दृपतिः**.\n'
        '\n'
        'SETTLED — **AND WHICH WAY THE OPTION FALLS DECIDES A LATER RULE.**\n'
        '  **यदा लुक् तदा मातृपितृभ्यां स्वसा इति नित्यं षत्वम्। यदा त्वलुक्\n'
        '  तदा मातुःपितुर्भ्याम् अन्यतरस्याम् इति विकल्पेन षत्वम्** — drop\n'
        '  the ending and 8.3.84 gives ष् always; keep it and 8.3.85 gives ष्\n'
        '  only optionally. So मातुःष्वसा and मातुःस्वसा both stand beside\n'
        '  मातृष्वसा, three forms from two options meeting. This is the last\n'
        '  rule under अलुक्; 6.3.25 आनङ् replaces the word'
    ),
)


_SUBSTITUTE = (
    'substitute(purvapada, gana=..., uttarapada=..., dvandva=..., '
    'result=..., chandasi=...) -> what the first member of the '
    'dvandva becomes, and by which rule of 6.3.25-33.'
)

register(
    '6.3.25',
    apply=substitute,
    codification=_SUBSTITUTE,
    notes=(
        'SETTLED — आनङ् ऋतो द्वन्द्वे — in a द्वन्द्व of ऋ-final words for a\n'
        '  relation of LEARNING or of BIRTH, the first member takes आनङ्:\n'
        '  **होतापोतारौ, नेष्टोद्गातारौ, प्रशास्ताप्रतिहर्तारौ** for\n'
        '  learning; **मातापितरौ, याताननान्दरौ** for birth.\n'
        '\n'
        'SETTLED — **AND THE न् IS THERE TO STOP SOMETHING.** **नकारोच्चारणं\n'
        '  रपरत्वनिवृत्त्यर्थम्** — without it, 1.1.51 उरण् रपरः would make\n'
        '  the substitute for an ऋ carry a र् after it. Marking the\n'
        '  substitute आनङ् rather than आन् is what keeps the र् out.\n'
        '\n'
        'SETTLED — **AND ONE WORD CARRIES DOWN FROM THE अलुक् RUN.** **पुत्र\n'
        '  इत्यनुवर्तते, ऋत इति च। तेन पुत्रशब्देऽपि उत्तरपद\n'
        '  ऋकारान्तस्यानङादेशो भवति — पितापुत्रौ, मातापुत्रौ** — पुत्र was\n'
        '  last said at 6.3.22, two sūtras before the heading changed, and it\n'
        '  is still running'
    ),
)

register(
    '6.3.26',
    apply=substitute,
    codification=_SUBSTITUTE,
    notes=(
        'SETTLED — देवताद्वन्द्वे च — and in a द्वन्द्व of GODS:\n'
        '  **इन्द्रावरुणौ, इन्द्रासोमौ, इन्द्राबृहस्पती**.\n'
        '\n'
        'SETTLED — **AND SAYING द्वन्द्व AGAIN IS WHAT NARROWS IT.**\n'
        '  **द्वन्द्व इति वर्तमाने पुनर्द्वन्द्वग्रहणं प्रसिद्धसाहचर्यार्थम्।\n'
        '  अत्यन्तसहचरिते लोकविज्ञाते द्वन्द्वम् इत्येतद् निपात्यते** — the\n'
        '  word was already running from 6.3.25, so repeating it can only\n'
        '  restrict, and what it restricts to is the pairs usage has ALREADY\n'
        '  paired: **तत्र ये लोके प्रसिद्धसाहचर्या वेदे च ये\n'
        '  सहवापनिर्दिष्टास्तेषाम् इह ग्रहणं भवति। तेन ब्रह्मप्रजापती,\n'
        '  शिववैश्रवणावित्येवमादौ न भवति**. Two gods are not enough; they\n'
        '  have to be a pair'
    ),
)

register(
    '6.3.27',
    apply=substitute,
    codification=_SUBSTITUTE,
    notes=(
        'SETTLED — ईदग्नेः सोमवरुणयोः — but अग्नि becomes ई before सोम and\n'
        '  वरुण: **अग्नीषोमौ, अग्नीवरुणौ**. The ष् of the first is not this\n'
        "  rule's: **अग्नेःस्तुत्स्तोमसोमाः इति षत्वम्**, by 8.3.82"
    ),
)

register(
    '6.3.28',
    apply=substitute,
    codification=_SUBSTITUTE,
    notes=(
        'SETTLED — इद् वृद्धौ — and अग्नि becomes इ where a वृद्धि has\n'
        '  ALREADY been made in the second member: **आग्निवारुणीम् अनड्वाहीम्\n'
        '  आलभेत; आग्निमारुतं कर्म क्रियते**.\n'
        '\n'
        'SETTLED — **AND IT IS STATED TO DEFEAT TWO RULES AT ONCE.** **तत्र\n'
        '  देवताद्वन्द्वे च इत्युभयपदवृद्धौ कृतायाम् आनङम् ईत्वं च बाधितुम्\n'
        '  इकारः क्रियते** — 7.3.21 has strengthened both members, and this इ\n'
        "  then displaces both 6.3.26's आनङ् and 6.3.27's ई. A substitute\n"
        '  whose whole purpose is to arrive after another rule has acted.\n'
        '\n'
        'SETTLED — **AND ONE GOD IS TAKEN BACK OUT BY A VĀRTTIKA.** **इद्\n'
        '  वृद्धौ विष्णोः प्रतिषेधो वक्तव्यः — आग्नावैष्णवम् एकादशकपालं\n'
        '  निर्वपेत्** — with विष्णु the आनङ् stands after all, वृद्धि or no\n'
        '  वृद्धि. इन्द्र is a different case and is NOT named out:\n'
        '  **वृद्धाविति किम्? आग्नेन्द्रः। नेन्द्रस्य परस्य\n'
        '  इत्युत्तरपदवृद्धिः प्रतिषिध्यते** — there 7.3.22 refuses the\n'
        '  strengthening, so the condition this rule wants never arises'
    ),
)

register(
    '6.3.29',
    apply=substitute,
    codification=_SUBSTITUTE,
    notes=(
        'SETTLED — देवो द्यावा — दिव् becomes द्यावा in a द्वन्द्व of gods:\n'
        '  **द्यावाक्षामा, द्यावाभूमी**. The sūtra says देवः for दिव् — the\n'
        '  stem in its other shape — and the vṛtti reads it straight:\n'
        '  **दिवित्येतस्य द्यावा इत्ययमादेशो भवति**'
    ),
)

register(
    '6.3.30',
    apply=substitute,
    codification=_SUBSTITUTE,
    notes=(
        'SETTLED — दिवसश्च पृथिव्याम् — and दिव् becomes दिवस् before पृथिवी,\n'
        '  **चकाराद् द्यावा च** — so both **दिवस्पृथिव्यौ** and\n'
        '  **द्यावापृथिव्यौ** stand.\n'
        '\n'
        'SETTLED — **AND THE अ OF दिवस् IS THERE TO STOP THE स् FROM\n'
        '  CHANGING.** **अकारोच्चारणं सकारस्य विकाराभावप्रतिपत्त्यर्थम्। तेन\n'
        '  रुत्वादीनि न भवन्ति** — written दिवस् rather than दिवश्, the स् is\n'
        '  not the kind of final that 8.2.66 turns to रु. And the vṛtti\n'
        '  leaves one form unexplained: **कथं द्यावा चिदस्मै पृथिवी नमेते\n'
        '  इति? कर्तव्योऽत्र यत्नः**'
    ),
)

register(
    '6.3.31',
    apply=substitute,
    codification=_SUBSTITUTE,
    notes=(
        'SETTLED — उषासोषसः — उषस् becomes उषासा in a द्वन्द्व of gods:\n'
        '  **उषासासूर्यम्, उषासानक्ता** — Dawn and the Sun, Dawn and Night'
    ),
)

register(
    '6.3.32',
    apply=substitute,
    codification=_SUBSTITUTE,
    notes=(
        'SETTLED — मातरपितरावुदीचाम् — मातृ becomes मातर before पितृ on the\n'
        "  NORTHERNERS' authority: **मातरपितरावित्युदीचामाचार्याणां\n"
        '  मतेनारङादेशो मातृशब्दस्य निपात्यते**. Laid down whole rather than\n'
        '  derived, and credited to a school by name — **उदीचामिति किम्?\n'
        '  मातापितरौ**, which is what everyone else says'
    ),
)

register(
    '6.3.33',
    apply=substitute,
    codification=_SUBSTITUTE,
    notes=(
        'SETTLED — पितरामातरा च छन्दसि — and in the Veda the pair is laid\n'
        '  down the other way round: **आ मा गन्तां पितरामातरा च**.\n'
        '\n'
        'SETTLED — **AND ONLY THE FIRST HALF IS THE निपातन.**\n'
        '  **पूर्वपदस्याराङादेशो निपात्यते। उत्तरपदे तु सुपां सुलुक्० इति\n'
        '  आकारादेशः। तत्र ऋतो ङिसर्वनामस्थानयोः इति गुणः** — पितरा is laid\n'
        '  down, but the मातरा that follows is built: 7.1.39 gives the आ and\n'
        '  7.3.110 the guṇa. Half a निपातन and half a derivation, in one word'
    ),
)


_BEHAVES_AS = (
    'behaves_as(stem, before=..., result=...) -> whether the '
    'feminine stem takes the masculine\'s shape or is shortened '
    'before the second member, and by which rule of 6.3.34-45.'
)

register(
    '6.3.34',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे\n'
        "  स्त्रियामपूरणीप्रियादिषु — a feminine stem takes the MASCULINE'S\n"
        '  SHAPE before an appositional feminine second member:\n'
        '  **दर्शनीयभार्यः, श्लक्ष्णचूडः, दीर्घजङ्घः** — the man whose wife\n'
        '  is good-looking, whose crest is smooth, whose shanks are long.\n'
        '\n'
        'SETTLED — **AND THE CONDITION IS ONE COMPOUND, UNPACKED TWICE BEFORE\n'
        '  USE.** **भाषितः पुमान् येन समानायाम् आकृताव् एकस्मिन्\n'
        '  प्रवृत्तिनिमित्ते स भाषितपुंस्कः शब्दः** — a word whose masculine\n'
        '  is spoken with the SAME form and the SAME ground of application.\n'
        '  Then **ऊङोऽभावोऽनूङ्, भाषितपुंस्काद् अनूङ् यस्मिन् स्त्रीशब्दे, स\n'
        '  भाषितपुंस्कादनूङ् स्त्रीशब्दः। बहुव्रीहिरयम्, अलुग्। निपातनात्\n'
        '  पञ्चम्याः** — and even the ablative in the sūtra is there by\n'
        '  निपातन.\n'
        '\n'
        'SETTLED — **AND WHAT IT DOES IS NOT A DELETION.** **तस्य\n'
        '  भाषितपुंस्कादनूङः स्त्रीशब्दस्य पुंशब्दस्येव रूपं भवति** — the\n'
        '  word takes the form the masculine WOULD have had. Nothing is\n'
        '  dropped and nothing replaced; one word is told to look like\n'
        '  another.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA TIGHTENS TWO OF THE EXCEPTIONS.**\n'
        '  **प्रधानपूरणीग्रहणं कर्तव्यम् — इह मा भूत् कल्याणपञ्चमीकः पक्ष\n'
        '  इति** — the ordinal excepted is the PRINCIPAL one, and the vṛtti\n'
        '  carries the same reading into 5.4.116'
    ),
)

register(
    '6.3.35',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — तसिलादिष्वा कृत्वसुचः — and before the affixes from 5.3.7\n'
        '  तसिल् as far as 5.4.17 कृत्वसुच्: **तस्याः शालायास्ततः; तस्यां\n'
        '  तत्र; यस्या यतः; यस्यां यत्र** — the feminine is there in the\n'
        '  analysis and gone from the form.\n'
        '\n'
        'SETTLED — **AND THE STRETCH HAS TO BE COUNTED OUT BY HAND.**\n'
        '  **तसिलादिषु परिगणनं कर्तव्यम्** — a bound given as *from here to\n'
        '  there* leaves it unclear which affixes of the stretch are meant,\n'
        '  so a vārttika lists them: **त्रतसौ। तरप्तमपौ। चरट्जातीयरौ।\n'
        '  कल्पब्देश्यदेशीयरः। रूपप्पाशपौ। थम्थालौ। दार्हिलौ। तिल्तातिलौ**.\n'
        '\n'
        'SETTLED — **AND FOUR MORE VĀRTTIKAS ADD FOUR MORE PLACES.** **शसि\n'
        '  बह्वल्पार्थस्य — बहुशो देहि, अल्पशो देहि**; **त्वतलोर्गुणवचनस्य —\n'
        '  पटुत्वम्, पटुता**, but only for a quality-word: **गुणवचनस्येति\n'
        '  किम्? कठीत्वम्, कठीता**; **भस्याढे तद्धिते — हास्तिकम्**, and not\n'
        '  before a ढ: **श्यैनेयः, रौहिणेयः**; and **ठक्छसोश्च — भावत्काः**'
    ),
)

register(
    '6.3.36',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — क्यङ्मानिनोश्च — and before क्यङ् and मानिन्: **एनी —\n'
        '  एतायते; श्येनी — श्येतायते**; and **दर्शनीयमानी अयमस्याः,\n'
        '  दर्शनीयमानिनीयमस्याः**.\n'
        '\n'
        'SETTLED — **AND मानिन् IS NAMED FOR TWO CASES 6.3.34 COULD NOT\n'
        '  REACH.** **मानिनो ग्रहणम् अस्त्र्यर्थम् असमानाधिकरणार्थं च** —\n'
        '  where the whole word is not feminine, and where the two members\n'
        '  are not in apposition. **इह तु दर्शनीयाम् आत्मानं मन्यते\n'
        '  दर्शनीयमानिनीति पूर्वेणैव सिद्धम्** — the appositional feminine\n'
        '  case 6.3.34 had already'
    ),
)

register(
    '6.3.37',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — न कोपधायाः — but not where the feminine has a क before its\n'
        '  ending: **पाचिकाभार्यः, कारिकाभार्यः, मद्रिकाभार्यः,\n'
        '  वृजिकाभार्यः**, and the same through every environment the earlier\n'
        '  rules gave — **मद्रिकाकल्पा, मद्रिकायते, मद्रिकामानिनी,\n'
        '  वैलेपिकम्**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA SAYS WHICH क IS MEANT.** **कोपधप्रतिषेधे\n'
        '  तद्धितवुग्रहणं कर्तव्यम्। इह मा भूत् — पाकभार्यः, भेकभार्य इति** —\n'
        '  the क put there by the taddhita वुक्, not any क that happens to\n'
        '  stand before the ending'
    ),
)

register(
    '6.3.38',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — संज्ञापूरण्योश्च — nor where the feminine is a NAME or an\n'
        '  ORDINAL: **दत्ताभार्यः, गुप्ताभार्यः, दत्तापाशा, दत्तायते,\n'
        '  दत्तामानिनी**; **पञ्चमीभार्यः, दशमीभार्यः, पञ्चमीपाशा, पञ्चमीयते,\n'
        "  पञ्चमीमानिनी**. The ordinal was already excepted by 6.3.34's own\n"
        '  words in the appositional case; here it is refused across the rest'
    ),
)

register(
    '6.3.39',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे — nor where the\n'
        '  feminine ends in a taddhita that CAUSED a वृद्धि, unless that\n'
        '  taddhita was laid down for a dye or a modification:\n'
        '  **स्रौघ्नीभार्यः, माथुरीभार्यः, स्रौघ्नीपाशा, स्रौघ्नीयते,\n'
        '  स्रौघ्नीमानिनी**.\n'
        '\n'
        'SETTLED — **AND THE बहुव्रीहि READING IS WHAT LETS IT REACH A WHOLE\n'
        '  WORD.** **बहुव्रीहिपरिग्रहः किमर्थम्? तावद्भार्यः, यावद्भार्यः** —\n'
        '  read as *one whose taddhita caused a वृद्धि* the rule reaches the\n'
        '  stem that merely ENDS in such a taddhita, which is what these two\n'
        '  need'
    ),
)

register(
    '6.3.40',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — स्वाङ्गाच्चेतोऽमानिनि — nor where an ई follows a word for\n'
        '  a PART OF THE BODY, except before मानिन्: **दीर्घकेशीभार्यः,\n'
        '  श्लक्ष्णकेशीभार्यः, दीर्घकेशीपाशा, दीर्घकेशीयते**'
    ),
)

register(
    '6.3.41',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — जातेश्च — nor where the feminine names a CLASS, again\n'
        '  except before मानिन्: **कठीभार्यः, बह्वृचीभार्यः, कठीपाशा,\n'
        '  कठीयते**.\n'
        '\n'
        'SETTLED — **AND THE REFUSAL DOES NOT REACH WHAT A VĀRTTIKA\n'
        '  SUPPLIED.** **अयं प्रतिषेध औपसंख्यानिकस्य पुंवद्भावस्य नेष्यते।\n'
        '  हस्तिनीनां समूहो हास्तिकम्** — हस्तिनी names a class, and the\n'
        "  पुंवद्भाव in हास्तिकम् comes from 6.3.35's vārttika **भस्याढे\n"
        '  तद्धिते**, not from a sūtra, so this refusal does not touch it'
    ),
)

register(
    '6.3.42',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — पुंवत् कर्मधारयजातीयदेशीयेषु — in a कर्मधारय, and before\n'
        "  जातीय and देशीय, the feminine takes the masculine's shape after\n"
        '  all. **प्रतिषेधार्थोऽयम् आरम्भः** — the rule exists for the\n'
        '  refusals, and the vṛtti walks all five: **न कोपधायाः इत्युक्तम्,\n'
        '  तत्रापि भवति — पाचकवृन्दारिका, पाचकजातीया, पाचकदेशीया;\n'
        '  संज्ञापूरण्योश्च इत्युक्तम्, तत्रापि भवति — दत्तवृन्दारिका,\n'
        '  पञ्चमवृन्दारिका; वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे\n'
        '  इत्युक्तम्, तत्रापि भवति — स्रौघ्नवृन्दारिका;\n'
        '  स्वाङ्गाच्चेतोऽमानिनि इत्युक्तम्, तत्रापि भवति —\n'
        '  श्लक्ष्णमुखवृन्दारिका; जातेश्च इत्युक्तम्, तत्रापि भवति —\n'
        '  कठवृन्दारिका**.\n'
        '\n'
        "SETTLED — **BUT 6.3.34'S OWN TWO CONDITIONS STILL HOLD.**\n"
        '  **भाषितपुंस्कादित्येव — खट्वावृन्दारिका। अनूङित्येव —\n'
        '  ब्रह्मबन्धूवृन्दारिका** — undoing five refusals is not the same as\n'
        '  widening the rule they refused.\n'
        '\n'
        'SETTLED — **AND WHERE THE SHORTENING COULD ALSO APPLY, IT WINS.**\n'
        '  **पुंवद्भावाद् ह्रस्वत्वं खिद्घादिकेषु भवति विप्रतिषेधेन —\n'
        '  कालिंमन्या; पाट्वितरा, पट्वितमा**. A vārttika adds one more class:\n'
        '  **कुक्कुट्यादीनाम् अण्डादिषु पुंवद्भावो वक्तव्यः — कुक्कुटाण्डम्,\n'
        '  मृगपदम्, काकशावः**'
    ),
)

register(
    '6.3.43',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — घरूपकल्पचेलड्ब्रुवगोत्रमतहतेषु ङ्योऽनेकाचो ह्रस्वः —\n'
        '  before eight things, a ङी-ending feminine of more than one vowel\n'
        '  goes SHORT: **ब्राह्मणितरा, ब्राह्मणितमा** (घ), **ब्राह्मणिरूपा,\n'
        '  ब्राह्मणिकल्पा, ब्राह्मणिचेली, ब्राह्मणिब्रुवा, ब्राह्मणिगोत्रा,\n'
        '  ब्राह्मणिमता, ब्राह्मणिहता**.\n'
        '\n'
        'SETTLED — **AND THE EIGHT ARE NOT ALL OF ONE KIND.** **घरूपकल्पाः\n'
        '  प्रत्ययाश्चेलडादीन्युत्तरपदानि** — the first three are affixes and\n'
        '  the last five are second members. And ब्रुव is explained:\n'
        '  **ब्रुवीतीति ब्रुवः पचाद्यचि वच्यादेशो गुणश्च निपातनाद् न भवति**'
    ),
)

register(
    '6.3.44',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — नद्याः शेषस्यान्यतरस्याम् — and what 6.3.43 left of नदी\n'
        '  goes short OPTIONALLY: **ब्रह्मबन्धूतरा / ब्रह्मबन्धुतरा;\n'
        '  वीरबन्धूतरा / वीरबन्धुतरा; स्त्रितरा / स्त्रीतरा**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI SAYS WHAT THE REMAINDER IS.** **कश्च शेषः?\n'
        '  अङी च या नदी, ङ्यन्तं च यदेकाच्** — the नदी that has no ङी, and\n'
        '  the ङी-ending word that has only one vowel. Exactly the two things\n'
        "  6.3.43's ङ्यः and अनेकाचः had between them left out"
    ),
)

register(
    '6.3.45',
    apply=behaves_as,
    codification=_BEHAVES_AS,
    notes=(
        'SETTLED — उगितश्च — and a नदी after a उगित् stem goes short\n'
        '  optionally: **श्रेयसितरा / श्रेयसीतरा / श्रेयस्तरा; विदुषितरा /\n'
        '  विदुषीतरा / विद्वत्तरा** — three forms, not two.\n'
        '\n'
        "SETTLED — **AND THE THIRD OF THE THREE IS NOT THIS RULE'S.**\n"
        '  **पुंवद्भावोऽप्यत्र पक्षे वक्तव्यः। प्रकर्षयोगात् प्राक्\n'
        '  स्त्रीत्वस्याविवक्षितत्वाद् वा सिद्धम्** — श्रेयस्तरा is the\n'
        "  masculine's shape, either by a vārttika supplying पुंवद्भाव here\n"
        '  as well, or because the femininity was never meant in the first\n'
        '  place, the word being under comparison'
    ),
)


_REPLACED_BY = (
    'replaced_by(purvapada, before=..., uttarapada_gana=..., '
    'result=...) -> what the first member is replaced by before '
    'the second, and by which rule of 6.3.46-60.'
)

register(
    '6.3.46',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — आन्महतः समानाधिकरणजातीययोः — महत् becomes महा before an\n'
        '  APPOSITIONAL second member and before जातीय: **महादेवः,\n'
        '  महाब्राह्मणः, महाबाहुः, महाबलः; महाजातीयः**.\n'
        '\n'
        'SETTLED — **AND THE WORD समानाधिकरण IS THERE FOR THE बहुव्रीहि AND\n'
        '  NOT FOR THE GENITIVE.** **लक्षणोक्तत्वाद् एवात्र न भविष्यतीति\n'
        '  चेद्, बहुव्रीहावपि न स्यान् महाबाहुरिति। तदर्थं समानाधिकरणग्रहणं\n'
        '  वक्तव्यम्** — one could keep महत्पुत्रः out by a paribhāṣā, but\n'
        '  that would keep महाबाहुः out too, so the condition is stated'
    ),
)

register(
    '6.3.47',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः — द्वि and अष्टन्\n'
        '  take आ before a NUMERAL, but not in a बहुव्रीहि and not before\n'
        '  अशीति: **द्वादश, द्वाविंशतिः, द्वात्रिंशत्; अष्टादश, अष्टाविंशतिः,\n'
        '  अष्टात्रिंशत्**.\n'
        '\n'
        "SETTLED — **AND HOW HIGH IT GOES IS A VĀRTTIKA'S.** **प्राक् शतादिति\n"
        '  वक्तव्यम्। इह मा भूत् — द्विशतम्, द्विसहस्रम्, अष्टशतम्,\n'
        '  अष्टसहस्रम्** — nothing in the three sūtras says the numeral must\n'
        '  be below a hundred, and the forms show it must'
    ),
)

register(
    '6.3.48',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — त्रेस्त्रयः — and त्रि becomes त्रयस् in the same place:\n'
        '  **त्रयोदश, त्रयोविंशतिः, त्रयस्त्रिंशत्**. Everything else carries\n'
        "  down from the sūtra before, the vārttika's **प्राक् शतात्**\n"
        '  included'
    ),
)

register(
    '6.3.49',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — विभाषा चत्वारिंशत्प्रभृतौ सर्वेषाम् — from चत्वारिंशत्\n'
        '  upward, all three substitutions are OPTIONAL: **द्विचत्वारिंशत् /\n'
        '  द्वाचत्वारिंशत्; त्रिपञ्चाशत् / त्रयःपञ्चाशत्; अष्टपञ्चाशत् /\n'
        '  अष्टापञ्चाशत्**. The word सर्वेषाम् is what gathers the three\n'
        '  earlier rules under one option — **द्वि अष्टन् त्रि इत्येतेषां\n'
        '  यदुक्तं तद् विभाषा भवति**'
    ),
)

register(
    '6.3.50',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — हृदयस्य हृल्लेखयदण्लासेषु — हृदय becomes हृद् before four\n'
        '  things: **हृदयं लिखतीति हृल्लेखः; हृदयस्य प्रियं हृद्यम्;\n'
        '  हृदयस्येदं हार्दम्; हृदयस्य लासो हृल्लासः**.\n'
        '\n'
        'SETTLED — **AND WHICH लेख IS MEANT SETTLES A PARIBHĀṢĀ FOR THE WHOLE\n'
        '  PĀDA.** **लेख इत्यणन्तस्य ग्रहणम् इष्यते। घञि तु हृदयस्य लेखो\n'
        '  हृदयलेखः। एतदेव लेखग्रहणं ज्ञापकम् उत्तरपदाधिकारे प्रत्ययग्रहणे\n'
        '  तदन्ताग्रहणस्य** — the sūtra names यत् and अण् as affixes and लेख\n'
        '  as a word. If naming an affix under this heading reached\n'
        '  everything ending in it, लेख would have been redundant. Its being\n'
        "  there proves it does not — the fact 6.3.17's vṛtti had already\n"
        '  appealed to'
    ),
)

register(
    '6.3.51',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — वा शोकष्यञ्रोगेषु — and optionally before three more:\n'
        '  **हृच्छोकः / हृदयशोकः; सौहार्द्यम् / सौहृदय्यम्; हृद्रोगः /\n'
        '  हृदयरोगः**.\n'
        '\n'
        'SETTLED — **AND THE OPTION MAY BE DOING NOTHING AT ALL.**\n'
        '  **हृदयशब्देन समानार्थो हृच्छब्दः प्रकृत्यन्तरम् अस्ति, तेनैव\n'
        '  सिद्धे विकल्पविधानं प्रपञ्चार्थम्** — हृद् is an independent stem\n'
        '  of the same meaning, so both forms were available without any\n'
        '  rule, and the option is stated only to spell the matter out'
    ),
)

register(
    '6.3.52',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — पादस्य पदाज्यातिगोपहतेषु — पाद becomes पद् before four:\n'
        '  **पादाभ्याम् अजतीति पदाजिः; पादाभ्याम् अततीति पदातिः; पादाभ्यां\n'
        '  गच्छतीति पदगः; पादेनोपहतः पदोपहतः**.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTE CARRIES AN ACCENT THE ORIGINAL DID\n'
        '  NOT.** **पादशब्दो वृषादित्वाद् आद्युदात्तः, तस्य स्थाने पदादेश\n'
        '  उपदेश एवान्तोदात्तो निपात्यते। तेन पदोपहत इति** — पाद is accented\n'
        "  on its first syllable by 6.1.203's वृषादि, but पद् is laid down\n"
        '  end-accented in the statement itself, which is how पदोपहतः comes\n'
        '  out as it does instead of by 6.2.48'
    ),
)

register(
    '6.3.53',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — पद्यत्यतदर्थे — and before यत्, where the sense is NOT\n'
        '  for-that-purpose: **पादौ विध्यन्ति पद्याः शर्कराः; पद्याः\n'
        '  कण्टकाः** — gravel that pricks the feet.\n'
        '\n'
        'SETTLED — **AND ONLY THE LIMB IS MEANT.** **शरीरावयववचनस्य\n'
        "  पादशब्दस्य ग्रहणम् इह इष्यते** — so 5.1.34's पाद, a quarter, is\n"
        '  untouched. A vārttika adds one more place: **पद्भाव इके चरतौ\n'
        '  उपसंख्यानम् — पादाभ्यां चरति पदिकः**'
    ),
)

register(
    '6.3.54',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — हिमकाषिहतिषु च — and before three more: **पद्धिमम्; अथ\n'
        '  पत्काषिणो यान्ति; पद्धतिः** — cold in the feet, those who go\n'
        '  grazing the ground, a beaten track'
    ),
)

register(
    '6.3.55',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        "SETTLED — ऋचः शे — and before शस्, where the पाद is a VERSE's:\n"
        '  **पच्छो गायत्रीं शंसति** — he recites the Gāyatrī foot by foot.\n'
        "  The शस् is 5.4.43's, **पादंपादं शंसतीति संख्यैकवचनाच्च\n"
        '  वीप्सायाम्**'
    ),
)

register(
    '6.3.56',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — वा घोषमिश्रशब्देषु — and optionally before three:\n'
        '  **पद्घोषः / पादघोषः; पन्मिश्रः / पादमिश्रः; पच्छब्दः / पादशब्दः**.\n'
        '  A vārttika adds a fourth: **निष्के चेति वक्तव्यम् — पन्निष्कः,\n'
        '  पादनिष्कः**'
    ),
)

register(
    '6.3.57',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — उदकस्योदः संज्ञायाम् — उदक becomes उद where the compound\n'
        '  is a NAME: **उदमेघो नाम यस्य औदमेघिः पुत्रः; उदवाहो नाम यस्य\n'
        '  औदवाहिः पुत्रः**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA TURNS THE RULE ROUND.** **संज्ञायाम्\n'
        '  उत्तरपदस्य उदकशब्दस्य उदादेशो भवतीति वक्तव्यम् — लोहितोदः, नीलोदः,\n'
        '  क्षीरोदः** — the same substitute for उदक standing as the SECOND\n'
        '  member, which the sūtra as written cannot reach'
    ),
)

register(
    '6.3.58',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — पेषंवासवाहनधिषु च — and before four more, name or no name:\n'
        '  **उदपेषं पिनष्टि; उदकस्य वास उदवासः; उदकस्य वाहनम् उदवाहनः; उदकं\n'
        '  धीयतेऽस्मिन्नित्युदधिः** — ground with water, a store of water, a\n'
        "  water-cart, and the sea. The णमुल् of the first is 3.4.38's,\n"
        '  **स्नेहने पिषः**'
    ),
)

register(
    '6.3.59',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — एकहलादौ पूरयितव्येऽन्यतरस्याम् — optionally, before a\n'
        '  second member that begins with a SINGLE consonant and names\n'
        '  something TO BE FILLED: **उदकुम्भः / उदककुम्भः; उदपात्रम् /\n'
        '  उदकपात्रम्**.\n'
        '\n'
        'SETTLED — **AND एकहल् IS GLOSSED BEFORE USE.** **एकोऽसहायः,\n'
        '  तुल्यजातीयेनानन्तरेण हला विना, हल् आदिर्यस्य उत्तरपदस्य तद्\n'
        '  एकहलादिः** — one consonant with no second of its own kind next to\n'
        '  it'
    ),
)

register(
    '6.3.60',
    apply=replaced_by,
    codification=_REPLACED_BY,
    notes=(
        'SETTLED — मन्थौदनसक्तुबिन्दुवज्रभारहारवीवधगाहेषु च — and optionally\n'
        '  before nine more: **उदमन्थः / उदकमन्थः; उदौदनः / उदकौदनः; उदसक्तुः\n'
        '  / उदकसक्तुः; उदबिन्दुः / उदकबिन्दुः; उदवज्रः / उदकवज्रः; उदभारः /\n'
        '  उदकभारः; उदहारः / उदकहारः; उदवीवधः / उदकवीवधः** — and उदगाहः\n'
        '  beside उदकगाहः'
    ),
)


_ADJUSTS = (
    'adjusts(purvapada, stem=..., before=..., result=...) -> '
    'whether the first member is shortened or takes a mum or am '
    'augment before the second, and by which rule of 6.3.61-72.'
)

register(
    '6.3.61',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — इको ह्रस्वोऽङ्यो गालवस्य — an इक्-final feminine that is\n'
        "  NOT ङी-ending goes short before a second member, on Gālava's\n"
        '  authority: **ग्रामणिपुत्रः / ग्रामणीपुत्रः; ब्रह्मबन्धुपुत्रः /\n'
        '  ब्रह्मबन्धूपुत्रः**.\n'
        '\n'
        'SETTLED — **AND NAMING THE ĀCĀRYA IS HONOUR AND NOT OPTION.**\n'
        '  **गालवग्रहणं पूजार्थम्। अन्यतरस्यामिति हि वर्तते** — the option\n'
        "  was already running from 6.3.44, so Gālava's name adds nothing to\n"
        '  the grammar and everything to the record. The same distinction\n'
        '  6.1.92 and 6.1.130 turned on.\n'
        '\n'
        'SETTLED — **AND THE OPTION IS SETTLED AND NOT FREE.**\n'
        '  **व्यवस्थितविभाषा चेयम्। तेनेह न भवति — कारीषगन्धीपुत्र इति।\n'
        '  इयङुवङ्भाविनाम् अव्ययानां च न भवति। श्रीकुलम्, भ्रूकुलम्,\n'
        '  काण्डीभूतम्** — a विभाषा that holds in some places and not in\n'
        '  others, with the places named'
    ),
)

register(
    '6.3.62',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — एक तद्धिते च — एक goes short before a taddhita and before\n'
        '  a second member: **एकस्या आगतम् एकरूप्यम्, एकमयम्; एकस्या भाव\n'
        '  एकत्वम्, एकता**; and for the second member, **एकस्याः क्षीरम्\n'
        '  एकक्षीरम्, एकदुग्धम्**.\n'
        '\n'
        'SETTLED — **AND THE SHORTENING IS WHAT SHOWS THE WORD IS TAKEN WITH\n'
        '  ITS GENDER.** **लिङ्गिविशिष्टस्य ग्रहणम् एकशब्दह्रस्वत्वं\n'
        '  प्रयोजयति। अचा हि गृह्यमाणम् अत्र विशेष्यते, न पुनरज्\n'
        '  गृह्यमाणेनेति** — a rule that shortens a vowel must be naming a\n'
        '  word that HAS one to shorten, so एका and not the bare stem एक'
    ),
)

register(
    '6.3.63',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — ङ्यापोः संज्ञाछन्दसोर्बहुलम् — a ङी- or आप्-ending stem\n'
        '  goes short VARIOUSLY where the compound is a name and in the Veda:\n'
        '  **रेवतिपुत्रः, रोहिणिपुत्रः, भरणिपुत्रः** for the ङी in a name;\n'
        '  **कुमारिदा, उर्विदा** for the ङी in the Veda; **शिलवहम्,\n'
        '  शिलप्रस्थम्** for the आप् in a name; **अजक्षीरेण जुहोति** for the\n'
        '  आप् in the Veda. And बहुलम् is not an option: the vṛtti pairs\n'
        '  every example with a **न च भवति** of the same shape'
    ),
)

register(
    '6.3.64',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — त्वे च — and before त्व, variously: **तद् अजाया\n'
        '  भावोऽजत्वम्, अजात्वम्; तद् रोहिण्या भावो रोहिणित्वम्,\n'
        '  रोहिणीत्वम्**. The vṛtti notes where the examples have to come\n'
        '  from: **संज्ञायाम् असंभवाच् छन्दस्येवोदाहरणानि भवन्ति** — an\n'
        '  abstract noun in त्व cannot also be a name, so only the Veda\n'
        '  supplies them'
    ),
)

register(
    '6.3.65',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — इष्टकेषीकामालानां चिततूलभारिषु — three stems go short\n'
        '  before three second members, matched ONE TO ONE: **इष्टकचितम्;\n'
        '  इषीकतूलम्; मालभारिणी कन्या** — built of bricks, a tuft of reed, a\n'
        '  girl wearing a garland. यथासंख्यम्, so इष्टका goes with चित and\n'
        '  with nothing else.\n'
        '\n'
        'SETTLED — **AND NAMING THE THREE REACHES WHAT ENDS IN THEM.**\n'
        '  **इष्टकादिभ्यस् तदन्तस्यापि ग्रहणं भवति — पक्वेष्टकचितम्,\n'
        '  मुञ्जेषीकतूलम्, उत्पलमालभारिणी कन्या** — which is the opposite of\n'
        "  what 6.3.50's लेखग्रहण established for an AFFIX named under this\n"
        '  heading. A word named here does reach what ends in it; an affix\n'
        '  named here does not'
    ),
)

register(
    '6.3.66',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — खित्यनव्ययस्य — before a खित्, anything that is NOT an\n'
        '  indeclinable goes short: **कालिंमन्या, हरिणिंमन्या** — she who\n'
        '  thinks herself a black antelope.\n'
        '\n'
        'SETTLED — **AND THE MUM OF THE NEXT SŪTRA DOES NOT DISPLACE IT.**\n'
        '  **मुमा ह्रस्वो न बाध्यते, अन्यथा हि ह्रस्वशासनम् अनर्थकं स्यात्**\n'
        '  — if the augment won, this rule would never apply at all, so both\n'
        '  act and the shortening acts first.\n'
        '\n'
        'SETTLED — **AND SAYING अनव्ययस्य IS WHAT SHOWS खित् MEANS खिदन्त.**\n'
        '  **अनव्ययस्येत्येतद् एव ज्ञापकम् इह खिदन्तग्रहणस्य** — an\n'
        '  indeclinable could only be the first member, so the खित् the rule\n'
        '  speaks of must be the second member ENDING in one'
    ),
)

register(
    '6.3.67',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — अरुर्द्विषदजन्तस्य मुम् — अरुस्, द्विषत् and any\n'
        '  VOWEL-FINAL stem take the augment मुम् before a खित्, an\n'
        '  indeclinable excepted: **अरुंतुदः, द्विषंतपः; कालिंमन्या** — one\n'
        '  who probes a wound, one who scorches his enemies.\n'
        '\n'
        'SETTLED — **AND THE WORD अन्त IS THERE TO FIX THE ORDER.**\n'
        '  **अन्तग्रहणं किम्? कृताजन्तकार्यप्रतिपत्त्यर्थम्। अतो ह्रस्वे कृते\n'
        '  मुम् भवति** — saying अजन्त rather than अच् makes the rule speak of\n'
        '  a stem AFTER whatever was due to its final vowel has happened. So\n'
        '  6.3.66 shortens कालिनी to कालि and the मुम् is put into that'
    ),
)

register(
    '6.3.68',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — इच एकाचोऽम्प्रत्ययवच्च — a one-vowelled इच्-final stem\n'
        '  takes अम् instead, and that अम् behaves like the accusative\n'
        '  singular: **गांमन्यः; स्त्रींमन्यः, स्त्रियंमन्यः; नरंमन्यः;\n'
        '  श्रियंमन्यः; भ्रुवंमन्यः**. **अमिति हि द्विरावर्तते** — the word\n'
        '  अम् is read twice over, once as the augment and once as what it is\n'
        '  likened to.\n'
        '\n'
        'SETTLED — **AND THE LIKENESS IMPORTS FIVE RULES AT ONCE.**\n'
        '  **अम्प्रत्ययवच्चेत्यतिदेशाद् आत्वपूर्वसवर्णगुणेयङुवङादेशा भवन्ति**\n'
        '  — the आ, the single-vowel replacement, the guṇa, the इयङ् and the\n'
        '  उवङ् all follow, which is what makes गाम्मन्यः and श्रियंमन्यः the\n'
        '  shapes they are.\n'
        '\n'
        'SETTLED — **AND ONE FORM IS LEFT UNSETTLED.** **अथेह कथं भवितव्यम्,\n'
        '  श्रियम् आत्मानं ब्राह्मणकुलं मन्यत इत्युपक्रम्य श्रिमन्यम् इति\n'
        "  भवितव्यम् इति भाष्ये** — the Mahābhāṣya's reading, and the vṛtti\n"
        '  records it without resolving it'
    ),
)

register(
    '6.3.69',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — वाचंयमपुरन्दरौ च — two words laid down whole: **वाचंयम\n'
        '  आस्ते; पुरं दारयतीति पुरंदरः** — one who holds his speech, and the\n'
        '  breaker of forts. Neither is derived: **इत्येतौ निपात्येते**'
    ),
)

register(
    '6.3.70',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — कारे सत्यागदस्य — सत्य and अगद take मुम् before कार:\n'
        '  **सत्यं करोतीति, सत्यस्य वा कारः सत्यंकारः; एवमगदंकारः** — an\n'
        '  earnest-money pledge, and the making of a medicine.\n'
        '\n'
        'SETTLED — **AND FOUR VĀRTTIKAS ADD FOUR MORE.** **अस्तुसत्यागदस्य\n'
        '  कार इति वक्तव्यम् — अस्तुंकारः**; **भक्षस्य छन्दसि कारे मुम्\n'
        '  वक्तव्यः — भक्षंकारः**, and not outside the Veda — **छन्दसीति\n'
        '  किम्? भक्षकारः**; **धेनोर्भव्यायां मुम् वक्तव्यः — धेनुंभव्या**;\n'
        '  and **लोकस्य पृणे मुम् वक्तव्यः — लोकंपृणा**'
    ),
)

register(
    '6.3.71',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — श्येनतिलस्य पाते ञे — श्येन and तिल take मुम् before पात,\n'
        '  but only where a ञ affix follows: **श्येनपातोऽस्यां क्रियायां\n'
        '  श्यैनंपाता; तैलंपाता** — the swoop of a hawk, the pressing of\n'
        '  sesame. The condition is on what comes AFTER the second member,\n'
        '  not on the second member itself'
    ),
)

register(
    '6.3.72',
    apply=adjusts,
    codification=_ADJUSTS,
    notes=(
        'SETTLED — रात्रेः कृति विभाषा — रात्रि takes मुम् optionally before\n'
        '  a कृत्-formed second member: **रात्रिंचरः / रात्रिचरः; रात्रिमटः /\n'
        '  रात्र्यटः** — one who goes about by night.\n'
        '\n'
        'SETTLED — **AND THE OPTION ONLY GIVES WHAT WAS NOT ALREADY DUE.**\n'
        '  **अप्राप्तविभाषेयम्। खिति हि नित्यं मुम् भवति। रात्रिंमन्यः** —\n'
        '  before a खित् the मुम् is compulsory by 6.3.67, so this विभाषा can\n'
        '  only be about the कृदन्तs that are not खित्'
    ),
)


_SHAPED = (
    'shaped(purvapada, gana=..., before=..., samasa=..., '
    'result=..., chandasi=...) -> what nan, saha, samana or their '
    'fellows come out as before the second member, and by which '
    'rule of 6.3.73-95.'
)

register(
    '6.3.73',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — नलोपो नञः — the न् of नञ् is dropped before a second\n'
        '  member: **अब्राह्मणः, अवृषलः, असुरापः, असोमपः**. The particle is\n'
        '  नञ् and what survives of it is a.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA CARRIES IT OUTSIDE COMPOUNDS\n'
        '  ALTOGETHER.** **नञो नलोपोऽवक्षेपे तिङ्युपसंख्यानम् — अपचसि त्वं\n'
        '  जाल्म, अकरोषि त्वं जाल्म** — before a FINITE VERB, where scorn is\n'
        '  meant. There is no compound there at all, so the sūtra as written\n'
        '  cannot reach it'
    ),
)

register(
    '6.3.74',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — तस्मान्नुडचि — and after that न्-less नञ्, a नुट् is put\n'
        '  in before a vowel: **अनजः, अनश्वः**. So the a that 6.3.73 left\n'
        '  comes back out as an-.\n'
        '\n'
        'SETTLED — **AND तस्मात् IS THERE TO SAY AFTER WHICH नञ्.**\n'
        '  **तस्मादिति किम्? नञ एव हि स्यात्। पूर्वान्ते हि ङमो ह्रस्वादचि\n'
        '  ङमुण्नित्यम् इति प्राप्नोति** — without it the augment would\n'
        '  attach to नञ् entire, and 8.3.32 would then double the ङम् at the\n'
        '  end of the first part. Saying *after that* fixes it to the residue'
    ),
)

register(
    '6.3.75',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — नभ्राण्नपान्नवेदानासत्यानमुचिनकुलनखनपुंसकनक्षत्रनक्रनाकेषु\n'
        '  प्रकृत्या — but in eleven words नञ् stands as it is, न् and all:\n'
        '  **न भ्राजत इति नभ्राट्; न पातीति नपात्; न वेत्तीति नवेदाः; न सत्या\n'
        '  असत्याः, न असत्या नासत्याः; न मुञ्चतीति नमुचिः; नास्य कुलमस्ति\n'
        '  नकुलः; नास्य खमस्तीति नखम्**.\n'
        '\n'
        'SETTLED — **AND EVERY ONE OF THEM IS ANALYSED BEFORE IT IS LISTED.**\n'
        '  The vṛtti does not name the words and stop: it says which affix\n'
        '  built each — **भ्राजतेः क्विबन्तस्य नञ्समासः; पातिः शत्रन्तः;\n'
        '  वेत्तिर् असुन्प्रत्ययान्तः; मुचेर् औणादिकः किप्रत्ययः** — which is\n'
        '  what makes them derivations that keep their न् rather than opaque\n'
        '  words'
    ),
)

register(
    '6.3.76',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — एकादिश्च एकस्य चादुक् — and नञ् stands as it is where एक\n'
        '  begins the compound, and एक itself takes the augment आदुक्: **एकेन\n'
        '  न विंशतिर् एकान्नविंशतिः; एकान्नत्रिंशत्** — twenty less one,\n'
        '  thirty less one. The compound is **तृतीयेति योगविभागात्**.\n'
        '\n'
        'SETTLED — **AND THE AUGMENT IS PUT AT THE END OF THE FIRST PART AND\n'
        '  NOT THE START OF THE SECOND.** **पूर्वान्तोऽयम् आदुक् क्रियते,\n'
        '  पदान्तलक्षणोऽत्रानुनासिको विकल्पेन यथा स्यादिति** — so that the\n'
        "  nasal standing at a word's end may be optional, which it could not\n"
        '  be if the augment belonged to what follows'
    ),
)

register(
    '6.3.77',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — नगोऽप्राणिष्वन्यतरस्याम् — and in नग, of things NOT ALIVE,\n'
        '  नञ् stands as it is optionally: **नगा वृक्षाः / अगा वृक्षाः; नगाः\n'
        '  पर्वताः / अगाः पर्वताः** — trees and mountains, which do not go.\n'
        "  **न गच्छन्तीति नगाः**, with 4.1.114's ड"
    ),
)

register(
    '6.3.78',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — सहस्य सः संज्ञायाम् — सह becomes स where the compound is a\n'
        '  NAME: **साश्वत्थम्, सपलाशम्, सशिंशपम्** — places named for the\n'
        '  tree that stands there.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTE IS LAID DOWN WITH AN ACCENT.**\n'
        '  **सादेश उदात्तो निपात्यते। उदात्तानुदात्तवतो हि सहशब्दस्य\n'
        '  आन्तर्यतः स्वरितः स्यात्** — सह has an उदात्त and an अनुदात्त, so\n'
        '  the nearest single accent for a one-syllable substitute would have\n'
        '  been a स्वरित; the निपातन makes it उदात्त instead. And it matters\n'
        '  only sometimes: **स च निपातनस्वरः पूर्वपदप्रकृतिस्वरत्वं यत्र,\n'
        '  तत्र उपयुज्यते। अन्यत्र समासान्तोदात्तत्वेन बाध्यत एव — सेष्टि,\n'
        '  सपशुबन्धम्**'
    ),
)

register(
    '6.3.79',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — ग्रन्थान्ताधिके च — and where सह names the END OF A BOOK\n'
        '  or an EXCESS: **सकलं ज्यौतिषम् अधीते; समुहूर्तम्; ससंग्रहं\n'
        '  व्याकरणम् अधीयते** for the first, and **सद्रोणा खारी; समाषः\n'
        '  कार्षापणः** for the second — a khārī with a droṇa over.\n'
        '\n'
        'SETTLED — **AND IT IS STATED BECAUSE THE NEXT RULE WOULD NOT HAVE\n'
        '  REACHED THESE.** **कलान्तं मुहूर्तान्तं संग्रहान्तम् इति अन्तवचने\n'
        '  इत्यव्ययीभावः समासः। तत्र अव्ययीभावे चाकाले इति कालवाचिनि उत्तरपदे\n'
        '  सभावो न प्राप्नोतीत्ययमारम्भः** — these are अव्ययीभावs with a\n'
        '  time-word after them, and 6.3.81 excepts exactly that'
    ),
)

register(
    '6.3.80',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — द्वितीये चानुपाख्ये — and where सह names the SECOND of\n'
        '  two, the one that cannot be seen: **साग्निः कपोतः; सपिशाचा वात्या;\n'
        '  सराक्षसीका शाला** — a dove with fire in it, a whirlwind with a\n'
        '  demon in it.\n'
        '\n'
        'SETTLED — **AND BOTH WORDS ARE GLOSSED BEFORE USE.** **द्वयोः\n'
        '  सहयुक्तयोर् अप्रधानो यः, स द्वितीयः** — of two things together,\n'
        '  the one that is not the point; **उपाख्यायते प्रत्यक्षत उपलभ्यते\n'
        '  यः, स उपाख्यः, उपाख्याद् अन्योऽनुपाख्योऽनुमेयः** — and not seen\n'
        '  but inferred. **अग्न्यादयः साक्षाद् अनुपलभ्यमानाः कपोतादिभिर्\n'
        '  अनुमीयमाना अनुपाख्या भवन्ति**'
    ),
)

register(
    '6.3.81',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — अव्ययीभावे चाकाले — and in an अव्ययीभाव, where the second\n'
        '  member does NOT name a time: **सचक्रं धेहि; सधुरं प्राज** — set it\n'
        '  down with the wheel, drive it with the yoke-pole'
    ),
)

register(
    '6.3.82',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — वोपसर्जनस्य — and optionally wherever सह is SUBORDINATE:\n'
        '  **सपुत्रः / सहपुत्रः; सच्छात्रः / सहच्छात्रः**.\n'
        '\n'
        'SETTLED — **AND उपसर्जन HERE MEANS THE WHOLE COMPOUND AND NOT A\n'
        '  MEMBER.** **उपसर्जनसर्वावयवः समास उपसर्जनम्। यस्य सर्वेऽवयवा\n'
        '  उपसर्जनीभूताः स सर्वोपसर्जनो बहुव्रीहिर् गृह्यते** — a बहुव्रीहि,\n'
        '  in which every member is subordinate to something outside the\n'
        '  compound'
    ),
)

register(
    '6.3.83',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — प्रकृत्याशिष्यगोवत्सहलेषु — but in a BLESSING सह stands as\n'
        '  it is, except before गो, वत्स and हल: **स्वस्ति देवदत्ताय\n'
        '  सहपुत्राय सहच्छात्राय सहामात्याय**.\n'
        '\n'
        'SETTLED — **AND THE THREE EXCEPTED WORDS STILL HAVE THE OPTION OF\n'
        '  THE RULE BEFORE.** **अगोवत्सहलेष्विति किम्? स्वस्ति भवते सहगवे,\n'
        '  सगवे। सहवत्साय, सवत्साय। सहहलाय, सहलाय। वोपसर्जनस्य इति पक्षे\n'
        '  भवत्येव सभावः** — being excepted from a hold-back does not make\n'
        "  the substitution compulsory; it only lets 6.3.82's option through"
    ),
)

register(
    '6.3.84',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — समानस्य छन्दस्यमूर्धप्रभृत्युदर्केषु — समान becomes स in\n'
        '  the Veda, except before मूर्धन्, प्रभृति and उदर्क: **अनु भ्राता\n'
        '  सगर्भ्यः; अनु सखा सयूथ्यः; यो नः सनुत्यः** — born of the same\n'
        '  womb, of the same herd. **समानो गर्भः सगर्भः, तत्र भवः सगर्भ्यः**,\n'
        "  with 4.4.114's यन्. And the vṛtti records a reading that splits\n"
        '  the sūtra: **समानस्येति योगविभाग इष्यते**'
    ),
)

register(
    '6.3.85',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — ज्योतिर्जनपदरात्रिनाभिनामगोत्ररूपस्थानवर्णवयोवचनबन्धुषु —\n'
        '  and outside the Veda before twelve named words: **सज्योतिः,\n'
        '  सजनपदः, सरात्रिः, सनाभिः, सनामा, सगोत्रः, सरूपः, सस्थानः, सवर्णः,\n'
        '  सवयाः, सवचनः, सबन्धुः** — of the same light, the same country, the\n'
        '  same night, the same navel, the same name, the same lineage. सवर्ण\n'
        '  is the term 1.1.9 defines, and this is where its शब्द comes from'
    ),
)

register(
    '6.3.86',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — चरणे ब्रह्मचारिणि — and before ब्रह्मचारिन्, where a\n'
        '  SCHOOL is meant: **समानो ब्रह्मचारी सब्रह्मचारी**. The vṛtti works\n'
        '  the sense out in full: **ब्रह्म वेदः, तदध्ययनार्थं यद् व्रतं तदपि\n'
        '  ब्रह्म, तच्चरतीति ब्रह्मचारी, समानस् तस्यैव ब्रह्मणः समानत्वाद्\n'
        '  इत्ययमर्थो भवति — समाने ब्रह्मणि व्रतचारी सब्रह्मचारीति** — not a\n'
        '  fellow-student in general but one keeping the same vow over the\n'
        '  same Veda'
    ),
)

register(
    '6.3.87',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — तीर्थे ये — and before तीर्थ with यत् on it: **सतीर्थ्यः**\n'
        "  — one who studies at the same teacher's. The यत् is 4.4.107's,\n"
        '  **समानतीर्थे वासी**'
    ),
)

register(
    '6.3.88',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — विभाषोदरे — and optionally before उदर with यत् on it:\n'
        '  **सोदर्यः / समानोदर्यः** — born of the same belly. The यत् is\n'
        "  4.4.108's, **समानोदरे शयित ओ चोदात्तः**, which supplies the accent\n"
        '  too'
    ),
)

register(
    '6.3.89',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — दृग्दृशवतुषु — and before दृक्, दृश and वतु: **सदृक्,\n'
        '  सदृशः** — of the same look. The affixes are from a vārttika on\n'
        '  3.2.60: **त्यदादिषु दृशोऽनालोचने कञ् च इत्यत्र समानान्ययोश्चेति\n'
        '  वक्तव्यम् इति कञ्क्विनौ प्रत्ययौ क्रियेते**, and another adds a\n'
        '  fourth environment — **दृक्षे चेति वक्तव्यम् — सदृक्षः**. The\n'
        '  vṛtti notes why वतु is named at all: **वतुग्रहणम् उत्तरार्थम्**,\n'
        '  for the two sūtras after'
    ),
)

register(
    '6.3.90',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — इदंकिमोरीश्की — इदम् and किम् become ईश् and की in the\n'
        '  same place, matched ONE TO ONE: **ईदृक्, ईदृशः, इयान्; कीदृक्,\n'
        "  कीदृशः, कियान्**. The वतुप् of इयान् and कियान् is 5.2.40's,\n"
        '  **किमिदम्भ्यां वो घः**, and the vārttika reaches here too —\n'
        '  **दृक्षे चेति वक्तव्यम् — ईदृक्षः, कीदृक्षः**'
    ),
)

register(
    '6.3.91',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — आ सर्वनाम्नः — and any PRONOUN takes आ in the same place:\n'
        '  **तादृक्, तादृशः, तावान्; यादृक्, यादृशः, यावान्** — of that sort,\n'
        '  of which sort. **दृक्षे चेति वक्तव्यम् — तादृक्षः, यादृक्षः**'
    ),
)

register(
    '6.3.92',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — विष्वग्देवयोश्च टेरद्र्यञ्चतौ वप्रत्यये — before an अञ्चति\n'
        '  with व on it, the last vowel and what follows it in विष्वक्, देव\n'
        '  and any pronoun becomes अद्रि: **विष्वगञ्चतीति विष्वद्र्यङ्;\n'
        '  देवद्र्यङ्; तद्र्यङ्, यद्र्यङ्**.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTE IS LAID DOWN END-ACCENTED FOR A\n'
        '  REASON.** **अद्रिसध्र्योर् अन्तोदात्तनिपातनं\n'
        '  कृत्स्वरनिवृत्त्यर्थम्। तत्र यणादेशे कृते उदात्तस्वरितयोर्यणः\n'
        '  स्वरितोऽनुदात्तस्य इत्येष स्वरो भवति** — to cancel the accent the\n'
        '  कृत् would have given, and so that 8.2.4 can then make the\n'
        '  following vowel svarita once the य् appears'
    ),
)

register(
    '6.3.93',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — समः समि — सम् becomes समि in the same place: **सम्यङ्,\n'
        '  सम्यञ्चौ, सम्यञ्चः** — going together, and so straight, and so\n'
        '  right'
    ),
)

register(
    '6.3.94',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — तिरसस्तिर्यलोपे — तिरस् becomes तिरि in the same place,\n'
        '  where the अ is NOT dropped: **तिर्यङ्, तिर्यञ्चौ, तिर्यञ्चः**.\n'
        "  **अलोप इति किम्? तिरश्चा, तिरश्चे** — 6.4.138's अचः takes the अ\n"
        "  out there, and this rule's condition is that it has not"
    ),
)

register(
    '6.3.95',
    apply=shaped,
    codification=_SHAPED,
    notes=(
        'SETTLED — सहस्य सध्रिः — and सह becomes सध्रि: **सध्र्यङ्,\n'
        "  सध्र्यञ्चौ, सध्र्यञ्चः; सध्रीचः, सध्रीचा**. The last of the pāda's\n"
        '  three particles, and the last of its substitutions for them — सह\n'
        '  has now become स by six rules, stood unchanged by one, and become\n'
        '  सध्रि by this'
    ),
)


_ALTERED = (
    'altered(purvapada, gana=..., before=..., samasa=..., '
    'result=..., chandasi=...) -> what else happens to the first '
    'member before the second, and by which rule of 6.3.96-113.'
)

register(
    '6.3.96',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — सध मादस्थयोश्छन्दसि — in the Veda सह becomes सध before माद\n'
        '  and स्थ: **सधमादो द्युम्निनीरापः; सधस्थाः** — the waters that\n'
        '  rejoice together, the places where they stand together. The third\n'
        '  shape सह takes in this pāda, after स at 6.3.78 and सध्रि at 6.3.95'
    ),
)

register(
    '6.3.97',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — द्व्यन्तरुपसर्गेभ्योऽप ईत् — अप् becomes ई after द्वि,\n'
        '  after अन्तर्, and after an उपसर्ग: **द्वीपम्, अन्तरीपम्; नीपम्,\n'
        '  वीपम्, समीपम्** — an island, a place between waters, water near at\n'
        '  hand.\n'
        '\n'
        'SETTLED — **AND उपसर्ग IS SAID FOR SOMETHING WIDER THAN उपसर्ग.**\n'
        '  **अप्शब्दं प्रति क्रियायोगाभावाद् उपसर्गग्रहणं\n'
        '  प्राद्युपलक्षणार्थम्** — nothing here is joined to a verb, so\n'
        '  nothing here is strictly an उपसर्ग at all; the word stands for the\n'
        '  प्रादि list'
    ),
)

register(
    '6.3.98',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — ऊदनोर्देशे — and after अनु it becomes ऊ, where a REGION is\n'
        '  meant: **अनूपो देशः** — a watery country. **दीर्घोच्चारणम्\n'
        '  अवग्रहार्थम्। अनु ऊपोऽनूप इति** — the substitute is written long\n'
        '  so that the word may be resolved as अनु + ऊप'
    ),
)

register(
    '6.3.99',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — अषष्ठ्यतृतीयास्थस्यान्यस्य दुक् — अन्य takes the augment\n'
        '  दुक् before nine words, provided it is not standing in a genitive\n'
        '  or an instrumental: **अन्या आशीः अन्यदाशीः; अन्या आशा अन्यदाशा;\n'
        '  अन्य आस्थितः अन्यदास्थितः; अन्य उत्सुकः अन्यदुत्सुकः; अन्या ऊतिः\n'
        '  अन्यदूतिः; अन्यः कारकः अन्यत्कारकः; अन्यो रागः अन्यद्रागः;\n'
        '  अन्यस्मिन् भवोऽन्यदीयः**'
    ),
)

register(
    '6.3.100',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — अर्थे विभाषा — and before अर्थ, optionally: **अन्यदर्थः /\n'
        '  अन्यार्थः**'
    ),
)

register(
    '6.3.101',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — कोः कत् तत्पुरुषेऽचि — कु becomes कद् in a तत्पुरुष before\n'
        '  a second member beginning with a VOWEL: **कदजः, कदश्वः, कदुष्ट्रः,\n'
        '  कदन्नम्** — a wretched goat, a wretched horse. A vārttika adds one\n'
        '  more: **कद्भावे त्रावुपसंख्यानम् — कुत्सितास्त्रयः कत्त्रयः**'
    ),
)

register(
    '6.3.102',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — रथवदयोश्च — and before रथ and वद, vowel or no vowel:\n'
        '  **कद्रथः, कद्वदः** — a poor chariot, a poor speaker'
    ),
)

register(
    '6.3.103',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — तृणे च जातौ — and before तृण where a SPECIES is named:\n'
        '  **कत्तृणा नाम जातिः** — the plant so called, and not merely poor\n'
        '  grass'
    ),
)

register(
    '6.3.104',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — का पथ्यक्षयोः — कु becomes का before पथिन् and अक्ष:\n'
        '  **कापथः, काक्षः** — a bad road, a bad eye'
    ),
)

register(
    '6.3.105',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — ईषदर्थे च — and wherever कु means A LITTLE: **कामधुरम्,\n'
        '  कालवणम्** — slightly sweet, slightly salt.\n'
        '\n'
        'SETTLED — **AND IT BEATS THE VOWEL RULE BY STANDING LATER.**\n'
        '  **अजादावपि परत्वात् कादेश एव भवति। काम्लम्, कोष्णम्** — before a\n'
        '  vowel 6.3.101 would have given कद्, and this rule takes it'
    ),
)

register(
    '6.3.106',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — विभाषा पुरुषे — and before पुरुष, optionally: **कापुरुषः /\n'
        '  कुपुरुषः** — a wretch.\n'
        '\n'
        'SETTLED — **AND THE OPTION ONLY GIVES WHAT WAS NOT ALREADY DUE.**\n'
        '  **अप्राप्तविभाषेयम्। ईषदर्थे तु पूर्वविप्रतिषेधेन नित्यं का भवति।\n'
        '  ईषत्पुरुषः कापुरुषः** — in the sense *a little* 6.3.105 has\n'
        '  already made का compulsory, and the earlier rule wins, so this\n'
        '  विभाषा is only about the sense of contempt'
    ),
)

register(
    '6.3.107',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — कवं चोष्णे — before उष्ण, कु becomes कवम्, and का\n'
        '  optionally beside it: **कवोष्णम्, कोष्णम्, कदुष्णम्** — lukewarm,\n'
        "  in three forms. The कद् of the third is 6.3.101's, उष्ण beginning\n"
        '  with a vowel'
    ),
)

register(
    '6.3.108',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — पथि च छन्दसि — and before पथिन् in the Veda, कवम् and का\n'
        '  both, optionally: **कवपथः, कापथः, कुपथः** — three forms again, and\n'
        '  the third is कु unaltered'
    ),
)

register(
    '6.3.109',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — पृषोदरादीनि यथोपदिष्टम् — **पृषोदरप्रकाराणि शब्दरूपाणि,\n'
        '  येषु लोपागमवर्णविकाराः शास्त्रेण न विहिता दृश्यन्ते च, तानि\n'
        '  यथोपदिष्टानि साधूनि भवन्ति** — words in which a sound has been\n'
        '  dropped, added or altered with no rule behind it are correct as\n'
        '  the learned use them: **यानि यानि यथोपदिष्टानि शिष्टैरुच्चारितानि\n'
        '  प्रयुक्तानि, तानि तथैवानुगन्तव्यानि**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI THEN DERIVES THEM BY HAND ANYWAY.**\n'
        '  **पृषदुदरं यस्य पृषोदरम्** — with the त् dropped; **वारिवाहको\n'
        "  बलाहकः** — with ब् for the first word and ल् for the second's र्;\n"
        '  **जीवनस्य मूतो जीमूतः**. So the rule licenses the forms without\n'
        '  pretending they are opaque: each is analysed, and only the\n'
        '  operation is unlicensed'
    ),
)

register(
    '6.3.110',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — संख्याविसायपूर्वस्याह्नस्याहन्नन्यतरस्यां ङौ — where अह्न\n'
        '  follows a numeral, वि or साय, it optionally becomes अहन् before\n'
        '  the locative ending: **द्व्यह्नि / द्व्यहनि; त्र्यह्नि / त्र्यहनि;\n'
        '  व्यह्नि / व्यहनि; सायाह्नि / सायाहनि**.\n'
        '\n'
        'SETTLED — **AND NAMING वि AND साय TEACHES SOMETHING ELSE.**\n'
        '  **एकदेशिसमासः पूर्वादिभ्योऽन्यस्यापि भवतीत्येतद् एव\n'
        '  विसायपूर्वस्याह्नस्य ग्रहणं ज्ञापकम्** — a compound of a part with\n'
        "  its whole is not confined to the पूर्वादि words, and this rule's\n"
        '  naming वि and साय is what shows it'
    ),
)

register(
    '6.3.111',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — ढ्रलोपे पूर्वस्य दीर्घोऽणः — where a ढ् or a र् is\n'
        '  dropped, the अण् vowel before it goes LONG: **लीढम्, मीढम्,\n'
        '  उपगूढम्, मूढः** for the ढ्; **नीरक्तम्, अग्नी रथः, इन्दू रथः, पुना\n'
        '  रक्तं वासः, प्राता राजक्रयः** for the र्.\n'
        '\n'
        'SETTLED — **AND पूर्वस्य IS SAID SO THE RULE REACHES OUTSIDE A\n'
        '  COMPOUND.** **पूर्वग्रहणम् अनुत्तरपदेऽपि पूर्वमात्रस्य\n'
        "  दीर्घार्थम्** — 6.3.1's उत्तरपदे is still running, and saying *of\n"
        '  what precedes* is what frees the rule from it. लीढम् is one word'
    ),
)

register(
    '6.3.112',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — सहिवहोरोदवर्णस्य — but for सह् and वह् it is ओ and not a\n'
        '  lengthening, and only for an अ or आ: **सोढा, सोढुम्, सोढव्यम्;\n'
        '  वोढा, वोढुम्, वोढव्यम्**.\n'
        '\n'
        'SETTLED — **AND THE WORD वर्ण IS THERE TO CATCH THE STRENGTHENED\n'
        '  VOWEL TOO.** **वर्णग्रहणं किम्? कृतायाम् अपि वृद्धौ यथा स्यात्।\n'
        '  उदवोढाम्, उदवोढम्। तादपि परस्तपरः, तपरत्वाद् आकारस्य ग्रहणं न\n'
        '  स्यात्** — written अत् the rule would have taken only the short अ,\n'
        '  by 1.1.70; written अवर्ण it takes the आ that वृद्धि has made'
    ),
)

register(
    '6.3.113',
    apply=altered,
    codification=_ALTERED,
    notes=(
        'SETTLED — साढ्यै साढ्वा साढेति निगमे — three forms of सह् are laid\n'
        '  down whole for the Veda: **साढ्यै समन्तात्; साढ्वा शत्रून्;\n'
        '  साढा**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI TAKES EACH APART ANYWAY.** **सहेः\n'
        '  क्त्वाप्रत्यय ओत्त्वाभावः। पक्षे क्त्वाप्रत्ययस्य ध्यैभावः। साढेति\n'
        "  तृचि रूपम् एतत्** — साढ्वा is क्त्वा with 6.3.112's ओ not\n"
        '  applying, साढ्यै is the same क्त्वा turned to ध्यै, and साढा is\n'
        '  तृच्. Laid down, and still accounted for'
    ),
)


_LENGTHENS = (
    'lengthens(purvapada, gana=..., before=..., result=..., '
    'chandasi=...) -> whether the first member lengthens in '
    'connected speech, and by which rule of 6.3.114-139.'
)

register(
    '6.3.114',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — संहितायाम् — **संहितायामित्ययम् अधिकारः। यदित ऊर्ध्वम्\n'
        '  अनुक्रमिष्यामः संहितायाम् इत्येवं तद् वेदितव्यम्** — from here\n'
        '  everything holds in CONNECTED SPEECH only. The vṛtti reads the\n'
        "  run's own last-but-four sūtra out as its example: **वक्ष्यति\n"
        '  द्व्यचोऽतस्तिङः इति — विद्मा हि त्वा गोपतिं शूर गोनाम्**.\n'
        '\n'
        'SETTLED — **AND THE COUNTER-EXAMPLE IS THE SAME WORDS SAID APART.**\n'
        '  **संहितायामिति किम्? विद्म, हि, त्वा, गोपतिम्, शूर, गोनाम्** — one\n'
        '  line quoted twice over, joined and then separated, and the\n'
        '  lengthening is there in the first and gone in the second. The\n'
        '  fourth heading of the pāda, and the only one that is about the\n'
        '  condition of speech rather than about a position or an operation'
    ),
)

register(
    '6.3.115',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — कर्णे\n'
        '  लक्षणस्याविष्टाष्टपञ्चमणिभिन्नच्छिन्नच्छिद्रस्रुवस्वस्तिकस्य — a\n'
        '  word naming a MARK lengthens before कर्ण, nine excepted:\n'
        '  **दात्राकर्णः, द्विगुणाकर्णः, त्रिगुणाकर्णः, द्व्यङ्गुलाकर्णः,\n'
        '  अङ्गुलाकर्णः**.\n'
        '\n'
        'SETTLED — **AND लक्षण IS THE SAME BRAND 6.2.112 MEANT.** **यत्\n'
        '  पशूनां स्वामिविशेषसंबन्धज्ञापनार्थं दात्राकारादि क्रियते, तद् इह\n'
        "  लक्षणं गृह्यते** — the nick cut in a beast's ear to show whose\n"
        '  herd it is, word for word the gloss the accent rule of the pāda\n'
        '  before had given'
    ),
)

register(
    '6.3.116',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ — the first member\n'
        '  lengthens before seven roots with क्विप् on them: **उपानत्,\n'
        '  परीणत्** (नह्); **नीवृत्, उपावृत्** (वृत्); **प्रावृट्** (वृष्);\n'
        '  **मर्मावित्, हृदयावित्, श्वावित्** (व्यध्); **नीरुक्, अभीरुक्**\n'
        '  (रुच्); **ऋतीषट्** (सह्); **परीतत्** (तन्).\n'
        '\n'
        'SETTLED — **AND THE LAST OF THE SEVEN NEEDS A RULE BORROWED FROM\n'
        '  ANOTHER PLACE.** **गमः क्वौ इति गमादीनाम् इष्यते। ततस् तनोतेर् अपि\n'
        '  अनुनासिकलोपः** — 6.4.40 is stated of गम् and its fellows, and तन्\n'
        '  has to be read into it or परीतत् loses no nasal'
    ),
)

register(
    '6.3.117',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — वनगिर्योः संज्ञायां कोटरकिंशुलकादीनाम् — before वन and\n'
        '  गिरि, in a NAME, the कोटरादि and किंशुलकादि words lengthen,\n'
        '  matched ONE TO ONE: **कोटरावणम्, मिश्रकावणम्, सिध्रकावणम्,\n'
        '  सारिकावणम्** for वन; **किंशुलकागिरिः, अञ्जनागिरिः** for गिरि.\n'
        '  Crossing them is not Sanskrit: the gaṇas go **यथासंख्यम्**'
    ),
)

register(
    '6.3.118',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — वले — the first member lengthens before वल: **आसुतीवलः,\n'
        '  कृषीवलः, दन्तावलः**.\n'
        '\n'
        'SETTLED — **AND वल IS THE AFFIX AND NOT THE WORD.**\n'
        '  **रजःकृष्यासुतिपरिषदो वलच् इति वलच्प्रत्ययो गृह्यते, न\n'
        "  प्रातिपदिकम्** — 5.2.112's affix, so a stem that merely ends in\n"
        '  the syllable is not reached. And three exceptions come down from\n'
        '  the sūtras before: **अनुत्साहभ्रातृपितृणाम् इत्येव**'
    ),
)

register(
    '6.3.119',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — मतौ बह्वचोऽनजिरादीनाम् — a first member of MANY vowels\n'
        '  lengthens before मतुप् in a NAME, the अजिरादि words excepted:\n'
        '  **उदुम्बरावती, मशकावती, वीरणावती, पुष्करावती, अमरावती** —\n'
        "  river-names, by 4.2.85's **नद्यां मतुप्**, and the व् of the affix\n"
        "  by 8.2.11's **संज्ञायाम्**"
    ),
)

register(
    '6.3.120',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — शरादीनां च — and the शरादि words before मतुप् in a name:\n'
        "  **शरावती, वंशावती**. They are named because 6.3.119's condition of\n"
        '  many vowels does not hold of them. The list runs **शर। वंश। धूम।\n'
        '  अहि। कपि। मणि। मुनि। शुचि। हनु**, and the vṛtti adds why the व्\n'
        '  appears here and not everywhere: **यवादित्वाद् व्रीह्यादिभ्यो न\n'
        '  भवति**'
    ),
)

register(
    '6.3.121',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — इको वहेऽपीलोः — an इक्-final first member lengthens before\n'
        '  वह, पीलु excepted: **ऋषीवहम्, कपीवहम्, मुनीवहम्** — what carries a\n'
        '  seer, an ape, a sage'
    ),
)

register(
    '6.3.122',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — उपसर्गस्य घञ्यमनुष्ये बहुलम् — an उपसर्ग lengthens\n'
        '  VARIOUSLY before a घञ्-formed second member, where no man is\n'
        '  named: **वीक्लेदः, वीमार्गः, अपामार्गः**, and **न च भवति —\n'
        '  प्रसेवः, प्रसारः**.\n'
        '\n'
        'SETTLED — **AND TWO VĀRTTIKAS SPLIT THE बहुलम् INTO CASES.**\n'
        '  **सादकारयोः कृत्रिमे दीर्घो भवति — प्रासादः, प्राकारः**, and only\n'
        '  of what is MADE: **कृत्रिम इति किम्? प्रसादः, प्रकारः**. And\n'
        '  **वेशादिषु विभाषा दीर्घो भवति — प्रतिवेशः, प्रतीवेशः; प्रतिरोधः,\n'
        '  प्रतीरोधः**'
    ),
)

register(
    '6.3.123',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — इकः काशे — an इक्-final उपसर्ग lengthens before काश:\n'
        '  **नीकाशः, वीकाशः, अनूकाशः**. And which काश:\n'
        '  **पचाद्यच्प्रत्ययान्तोऽयं काशशब्दो न तु घञन्तः** — the अच्-formed\n'
        '  one, not the घञ्-formed one 6.3.122 would have reached'
    ),
)

register(
    '6.3.124',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — दस्ति — an इक्-final उपसर्ग lengthens before a त्-initial\n'
        '  substitute for दा: **नीत्तम्, वीत्तम्, परीत्तम्**.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTE ONLY LOOKS त्-INITIAL AFTER ANOTHER\n'
        '  RULE HAS ACTED.** **अच उपसर्गात् तः इत्यन्तस्य यद्यपि तकारः\n'
        '  क्रियते, तथापि चर्त्वस्याश्रयात् सिद्धत्वम् इति तकारादिर्भवति** —\n'
        '  7.4.47 makes a त् of the FINAL, and it is only because चर्त्व is\n'
        '  already settled that the whole substitute counts as beginning with\n'
        '  one'
    ),
)

register(
    '6.3.125',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — अष्टनः संज्ञायाम् — अष्टन् lengthens before a second\n'
        '  member where the compound is a NAME: **अष्टावक्रः, अष्टाबन्धुरः,\n'
        '  अष्टापदम्** — the eight-bent sage, the chessboard'
    ),
)

register(
    '6.3.126',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — छन्दसि च — and in the Veda, name or no name: **आग्नेयम्\n'
        '  अष्टाकपालं निर्वपेत्; अष्टाहिरण्या दक्षिणा; अष्टापदी देवता\n'
        '  सुमती**. A vārttika adds one case outside the Veda: **गवि च युक्ते\n'
        '  भाषायाम् अष्टनो दीर्घो भवतीति वक्तव्यम् — अष्टागवं शकटम्**'
    ),
)

register(
    '6.3.127',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — चितेः कपि — चिति lengthens before कप्: **एकचितीकः,\n'
        '  द्विचितीकः, त्रिचितीकः** — of one layer, of two, of three'
    ),
)

register(
    '6.3.128',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — विश्वस्य वसुराटोः — विश्व lengthens before वसु and राज्:\n'
        '  **विश्वावसुः, विश्वाराट्**.\n'
        '\n'
        'SETTLED — **AND राट् IS NAMED IN ITS ALTERED SHAPE ON PURPOSE.**\n'
        '  **राडिति विकारनिर्देशो यत्रास्यैतद् रूपं तत्रैव यथा स्यात्** — the\n'
        '  sūtra writes the word as it comes out, so the rule reaches only\n'
        '  where it comes out that way. **इह न भवति — विश्वराजौ, विश्वराजः**'
    ),
)

register(
    '6.3.129',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — नरे संज्ञायाम् — and before नर, in a NAME: **विश्वानरो नाम\n'
        '  यस्य वैश्वानरिः पुत्रः**'
    ),
)

register(
    '6.3.130',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — मित्रे चर्षौ — and before मित्र, where a SEER is meant:\n'
        '  **विश्वामित्रो नाम ऋषिः**. The pāda before had the same name at\n'
        '  6.2.165, where a vārttika kept the seers out of an accent rule;\n'
        '  here the seer is the whole condition'
    ),
)

register(
    '6.3.131',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — मन्त्रे सोमाश्वेन्द्रियविश्वदेव्यस्य मतौ — in a मन्त्र,\n'
        '  four words lengthen before मतुप्: **सोमावती, अश्वावती,\n'
        '  इन्द्रियावती, विश्वदेव्यावती**'
    ),
)

register(
    '6.3.132',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — ओषधेश्च विभक्तावप्रथमायाम् — and ओषधि lengthens before any\n'
        '  case ending but the nominative, still in a मन्त्र: **ओषधीभिः\n'
        '  पुनीतात्; नमः पृथिव्यै नम ओषधीभ्यः**. **मन्त्र इति वर्तते**'
    ),
)

register(
    '6.3.133',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — ऋचि तुनुघमक्षुतङ्कुत्रोरुष्याणाम् — in an ऋच्, eight\n'
        '  particles lengthen: **आ तू न इन्द्र वृत्रहन्** (तु); **नू करणे**\n'
        '  (नु); **उत वा घा स्यालात्** (घ); **मक्षू गोमन्तमीमहे** (मक्षु);\n'
        '  **भरता जातवेदसम्** (तङ्); **कूमनः** (कु); **अत्रा गौः** (त्र);\n'
        '  **उरुष्या णो अभिशस्तेः** (उरुष्य)'
    ),
)

register(
    '6.3.134',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — इकः सुञि — an इक्-final word lengthens before the particle\n'
        '  सु, in a मन्त्र: **अभी षु णः सखीनाम्; ऊर्ध्व ऊ षु ण ऊतये**. **सुञ्\n'
        '  निपातो गृह्यते** — the particle and not the affix. The ष् is\n'
        "  8.3.105's and the ण् is 8.4.27's"
    ),
)

register(
    '6.3.135',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — द्व्यचोऽतस्तिङः — in an ऋच्, a TWO-SYLLABLED finite verb\n'
        '  ending in अ lengthens that अ: **विद्मा हि त्वा गोपतिं शूर गोनाम्;\n'
        "  विद्मा शरस्य पितरम्**. This is the sūtra 6.3.114's vṛtti read out\n"
        "  as the heading's own example, twenty-one sūtras before reaching it"
    ),
)

register(
    '6.3.136',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — निपातस्य च — and any particle, in an ऋच्: **एवा ते;\n'
        '  अच्छा**. **ऋचीत्येव** — the condition is carried down and not\n'
        '  restated'
    ),
)

register(
    '6.3.137',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — अन्येषामपि दृश्यते — and a lengthening is SEEN in other\n'
        '  words too: **यस्य दीर्घत्वं न विहितम्, दृश्यते च प्रयोगे, तद् अनेन\n'
        '  कर्तव्यम्। स शिष्टप्रयोगाद् अनुगन्तव्यः** — **केशाकेशि, कचाकचि,\n'
        '  जलाषाट्, नारकः, पूरुषः**. The same shape 6.3.109 पृषोदरादीनि had,\n'
        '  twenty-eight sūtras earlier, and for the same reason.\n'
        '\n'
        "SETTLED — **AND A VĀRTTIKA MAKES ONE STEM'S CASE EXACT.** **शुनो\n"
        '  दन्तदंष्ट्राकर्णकुन्दवराहपुच्छपदेषु — श्वादन्तः, श्वादंष्ट्रः,\n'
        '  श्वाकर्णः, श्वाकुन्दः, श्वावराहः, श्वापुच्छः, श्वापदः** — seven\n'
        '  second members named for श्वन् alone, so that at least one corner\n'
        '  of the catch-all is decidable'
    ),
)

register(
    '6.3.138',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — चौ — the first member lengthens before चु: **दधीचः पश्य,\n'
        '  दधीचा, दधीचे; मधूचः पश्य, मधूचा, मधूचे**. And चु is अञ्चति in a\n'
        '  particular state: **चावित्यञ्चतिर्लुप्तनकाराकारो गृह्यते** — with\n'
        '  its न् and its अ already gone.\n'
        '\n'
        "SETTLED — **AND AN INNER RULE IS HELD OFF BY THIS ONE'S MERE\n"
        '  EXISTENCE.** **अन्तरङ्गोऽपि हि यणादेशो दीर्घविधानसामर्थ्याद् न\n'
        '  प्रवर्तते** — the यण् would ordinarily go first, being inner; if\n'
        '  it did, there would be no vowel left to lengthen and this rule\n'
        '  would be idle, so it does not'
    ),
)

register(
    '6.3.139',
    apply=lengthens,
    codification=_LENGTHENS,
    notes=(
        'SETTLED — संप्रसारणस्य — a first member ending in a संप्रसारण\n'
        '  lengthens before a second: **कारीषगन्धीपुत्रः, कारीषगन्धीपतिः,\n'
        '  कौमुदगन्धीपुत्रः, कौमुदगन्धीपतिः** — **उत्तरपद इति वर्तते**, the\n'
        "  heading opened at 6.3.1 still running at the pāda's last sūtra.\n"
        '\n'
        'SETTLED — **AND THE PĀDA CLOSES BY SETTLING A CONFLICT WITH ITS OWN\n'
        '  EARLIER SELF.** 6.3.61 इको ह्रस्वोऽङ्यो गालवस्य would have\n'
        '  SHORTENED the same vowel. The vṛtti answers twice:\n'
        '  **व्यवस्थितविभाषा हि सा** — that option does not fall here at all;\n'
        '  and then, for the reading on which it might, **अकृत एव दीर्घत्वे\n'
        '  ह्रस्वाभावपक्षे कृतार्थनापि दीर्घेण पक्षान्तरे परत्वाद् ह्रस्वो\n'
        '  बाध्यते। पुनःप्रसङ्गविज्ञानं च न भवति। सकृद् गतौ विप्रतिषेधे यद्\n'
        '  बाधितं तद् बाधितम् एव** — a rule set aside once in a conflict does\n'
        '  not come back for a second attempt'
    ),
)


__all__ = ['adjusts', 'altered', 'behaves_as', 'lengthens', 'replaced_by', 'shaped', 'stays', 'substitute']
