# -*- coding: utf-8 -*-
"""अध्याय ७, पाद २ — the सिच् aorist's vṛddhi, and where the इट् is refused."""

from __future__ import annotations

from src.astadhyayi.anga import mrjer_vrddhi
from src.astadhyayi.anit import no_it
from src.astadhyayi.it_agama import the_it
from src.astadhyayi.nniti_vrddhi import vrddhi_before
from src.astadhyayi.vibhaktau import before_ending
from src.astadhyayi.sici_vrddhi import vrddhi
from src.astadhyayi.sources import register


_VRDDHI = (
    'vrddhi(stem, gana=..., before=..., part=..., pada=...) -> '
    'whether the sic aorist strengthens its stem, and by which '
    'rule of 7.2.1-7.'
)

register(
    '7.2.1',
    apply=vrddhi,
    codification=_VRDDHI,
    notes=(
        'SETTLED — सिचि वृद्धिः परस्मैपदेषु — an इक्-final stem takes vṛddhi\n'
        '  before a सिच् followed by a परस्मैपद ending: **अचैषीत्, अनैषीत्,\n'
        '  अलावीत्, अपावीत्, अकार्षीत्, अहार्षीत्**.\n'
        '\n'
        'SETTLED — **AND IT HAS TO BEAT AN INNER RULE TO APPLY AT ALL.** guṇa\n'
        '  is अन्तरङ्ग and would come first, leaving no इक् to strengthen.\n'
        '  **अन्तरङ्गम् अपि गुणम् एषां वृद्धिर् वचनाद् बाधते** — the vṛddhi\n'
        '  displaces it by the mere fact of having been stated, since a\n'
        '  statement that could never apply would be idle. The vṛtti makes\n'
        '  the same argument again at 7.2.4 and at 7.2.5.\n'
        '\n'
        'SETTLED — **AND WHERE THE vṛddhi IS REFUSED SOMETHING ELSE GETS\n'
        '  IN.** **न्यनुवीद्, न्यधुवीद् इत्यत्र कुटादित्वाद् ङित्वे सति\n'
        '  प्रतिषिद्धायां वृद्धाव् उवङादेशः क्रियते** — the कुटादि roots are\n'
        "  ङित् by 1.2.1, 1.1.5 then refuses the vṛddhi, and 6.4.77's उवङ्\n"
        '  takes the space'
    ),
)

register(
    '7.2.2',
    apply=vrddhi,
    codification=_VRDDHI,
    notes=(
        'SETTLED — अतो र्लान्तस्य — and the अ of a stem ending in र् or ल्\n'
        '  takes it, that अ standing NEXT to the final: **अक्षारीत्,\n'
        '  अत्सारीत्, अज्वालीत्, अह्मालीत्**. **अतो हलादेर्लघोः इति\n'
        "  विकल्पस्यायम् अपवादः** — an exception to 7.2.7's option, so here\n"
        '  the vṛddhi is compulsory. And अन्तग्रहणम् is what keeps अवभ्रीत्\n'
        '  out: **अत्र यौ रेफलकाराव् अङ्गस्यान्तौ, न तावतः समीपौ**'
    ),
)

register(
    '7.2.3',
    apply=vrddhi,
    codification=_VRDDHI,
    notes=(
        'SETTLED — वदव्रजहलन्तस्याचः — and the vowel of वद्, व्रज् and of any\n'
        '  CONSONANT-final stem: **अवादीत्, अव्राजीत्; अपाक्षीत्, अभैत्सीत्,\n'
        '  अच्छैत्सीत्, अरौत्सीत्**. वद् and व्रज् are named to shut out\n'
        "  7.2.7's option, **विकल्पबाधनार्थम्**.\n"
        '\n'
        'SETTLED — **AND हलन्त IS SAID TO CATCH A CLUSTER AND NOT ONE\n'
        '  CONSONANT.** Split the sūtra and हलन्तग्रहणम् is unnecessary;\n'
        '  kept, it is **हल्समुदायपरिग्रहार्थम्** — **अराङ्क्षीत्,\n'
        '  असाङ्क्षीत्** need the vowel to be reached across TWO consonants,\n'
        '  and **येन नाव्यवधानं तेन व्यवहितेऽपि** by itself lets only one\n'
        '  stand between'
    ),
)

register(
    '7.2.4',
    apply=vrddhi,
    codification=_VRDDHI,
    notes=(
        'SETTLED — नेटि — but a consonant-final stem does NOT take it where\n'
        '  the सिच् has an इट् in front: **अदेवीत्, असेवीत्, अकोषीत्,\n'
        '  अमोषीत्**.\n'
        '\n'
        'SETTLED — **AND THE OBJECTION IS THAT EVERY STEM IS CONSONANT-FINAL\n'
        '  BY THEN.** guṇa and the अव् substitution would have made लू into\n'
        '  लाव्, so अलावीत् should be refused too. **नैतद् एवम्। अन्तरङ्गम्\n'
        '  अपि गुणं वचनारम्भसामर्थ्यात् सिचि वृद्धिर् बाधते इत्युक्तम्** —\n'
        '  the same answer as at 7.2.1, and the vṛtti says so by citing\n'
        '  itself'
    ),
)

register(
    '7.2.5',
    apply=vrddhi,
    codification=_VRDDHI,
    notes=(
        'SETTLED — ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम् — and neither do\n'
        '  ह्-final, म्-final and य्-final stems, nor क्षण्, श्वस्, जागृ, णि,\n'
        '  श्वि, nor the एदित् roots: **अग्रहीत्, अस्यमीत्, अवमीत्, अव्ययीत्,\n'
        '  अक्षणीत्, अश्वसीत्, अजागरीत्, औनयीत्, अश्वयीत्; अरगीत्, अकखीत्**.\n'
        '\n'
        'SETTLED — **AND THE LIST DOES TWO DIFFERENT JOBS AT ONCE.** For the\n'
        '  ह्म्य-final stems and क्षण् and श्वस् and the एदित् roots it\n'
        "  refuses 7.2.7's OPTION; for जागृ, णि and श्वि it refuses 7.2.1's\n"
        '  vṛddhi, which 7.2.4 could not reach because they are not\n'
        '  consonant-final. **सा च नेटि इति न प्रतिषिध्यते** — and naming णि\n'
        '  and श्वि proves that guṇa has not come first, or they would be\n'
        '  य्-final already and the naming idle'
    ),
)

register(
    '7.2.6',
    apply=vrddhi,
    codification=_VRDDHI,
    notes=(
        'SETTLED — ऊर्णोतेर्विभाषा — and ऊर्णु refuses it OPTIONALLY:\n'
        '  **प्रौर्णवीत्, प्रौर्णावीत्**.\n'
        '\n'
        "SETTLED — **AND IT IS AN OPTION ON TOP OF ANOTHER OPTION.** 1.2.3's\n"
        "  **विभाषोर्णोः** already makes ऊर्णु's affix ङित् or not. On the\n"
        '  अङित् side this sūtra then gives two forms; on the ङित् side 1.1.5\n'
        '  refuses both guṇa and vṛddhi and the उवङ् comes instead —\n'
        '  **प्रौर्णुवीत्**. Three forms out of two options, and the vṛtti\n'
        '  sets them out in that order'
    ),
)

register(
    '7.2.7',
    apply=vrddhi,
    codification=_VRDDHI,
    notes=(
        'SETTLED — अतो हलादेर्लघोः — and a LIGHT अ in a stem that begins with\n'
        '  a consonant refuses it optionally: **अकणीत्, अकाणीत्; अरणीत्,\n'
        '  अराणीत्**. Three conditions, and the vṛtti gives a counter-example\n'
        '  for each.\n'
        '\n'
        'SETTLED — **AND ITS अतः IS NEEDED FOR A REASON THAT HAS NOTHING TO\n'
        '  DO WITH ITS OWN EXAMPLES.** Drop it and अचः must be carried down\n'
        '  instead; then the vṛddhi is अच्-conditioned and not\n'
        "  इक्-conditioned, and 1.1.5's क्ङिति refusal — which only stops an\n"
        '  इक्-conditioned operation — would not reach न्यकुटीत् and\n'
        '  न्यपुटीत्. **तत्राज्लक्षणा वृद्धिर् इग्लक्षणा न भवति इति क्ङिति च\n'
        '  इति प्रतिषेधो न स्यात्**'
    ),
)


_NO_IT = (
    'no_it(root, gana=..., before=..., upasarga=..., sense=..., '
    'chandasi=...) -> whether the it augment is refused, and by '
    'which rule of 7.2.8-34.'
)

register(
    '7.2.8',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — नेड् वशि कृति — no इट् before a कृत् affix beginning with\n'
        '  a वश् sound: **ईश्वरः, दीप्रः, भस्म, याच्ञा**.\n'
        '\n'
        'SETTLED — **AND THE THREE AFFIXES THE vṛtti NAMES ARE AN\n'
        '  ILLUSTRATION AND NOT A LIST.** **वरमनादौ इत्युदाहरणप्रदर्शनार्थम्,\n'
        '  न परिगणनम्** — so the Uṇādi **ञमन्ताड् डः** is refused too, or\n'
        '  else **उणादयो बहुलम्** answers for it. And this is the first rule\n'
        '  of the run: every one of the twenty-seven refuses an augment\n'
        '  7.2.35 has not yet given'
    ),
)

register(
    '7.2.9',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — तितुत्रतथसिसुसरकसेषु च — nor before ति तु त्र त थ सि सु सर\n'
        '  क स: **तन्तिः, दीप्तिः, सक्तुः, पत्त्रम्, तन्त्रम्, हस्तः, लोतः,\n'
        '  पोतः, धूर्तः**.\n'
        '\n'
        'SETTLED — **AND ति IS TWO AFFIXES AND त IS NOT THE OBVIOUS ONE.**\n'
        '  **तीति क्तिन्क्तिचोः सामान्यग्रहणम्** — one syllable naming both.\n'
        "  And the त meant is the Uṇādi's तन् and not the निष्ठा's क्त:\n"
        '  **औणादिकस्यैव तशब्दस्य ग्रहणम् इष्यते, न पुनः क्तस्य। हसितम्\n'
        '  इत्येव हि तत्र भवति**'
    ),
)

register(
    '7.2.10',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — एकाच उपदेशेऽनुदात्तात् — nor after a root that is ONE\n'
        '  SYLLABLE and अनुदात्त as it is taught: **दाता, नेता, चेता, स्तोता,\n'
        '  कर्ता, हर्ता**. **प्रकृत्याश्रयोऽयं प्रतिषेधः** — this refusal\n'
        '  turns on the root and not on the affix, and it is the widest of\n'
        '  the twenty-seven.\n'
        '\n'
        'SETTLED — **AND THE vṛtti ANSWERS *WHICH ROOTS* WITH TWO VERSES.**\n'
        '  **के पुनर् उपदेशेऽनुदात्ताः? ये तथा गणे पठ्यन्ते** — those so read\n'
        '  in the धातुपाठ; and then, **विस्पष्टार्थम्**, the अनिट्कारिका\n'
        '  verses set them out: **अनिट् स्वरान्तो भवति** with the exceptions\n'
        '  **अदन्तम् ऋदन्तम् ऋतां च वृङ्वृञौ श्विडीङिवर्णेष्वथ\n'
        '  शीङ्श्रिञावपि**, and a second verse for the vowel-final rest\n'
        '  before the consonant-final roots begin'
    ),
)

register(
    '7.2.11',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — श्र्युकः किति — nor for श्रि and an उक्-final root before\n'
        '  a कित् affix: **श्रित्वा, श्रितः; युत्वा, युतः; लूत्वा, लूनः;\n'
        '  वृत्वा, वृतः; तीर्त्वा, तीर्णः**.\n'
        '\n'
        'SETTLED — **AND SOME READ A ग् INTO THE DOUBLED क्.** **केचिदत्र\n'
        '  द्विककारनिर्देशेन गकारप्रश्लेषं वर्णयन्ति, भूष्णुरित्येवं यथा\n'
        '  स्यात्** — to catch the गित् affixes too. The vṛtti answers that\n'
        '  3.2.139 already provides for that, **न किंचिद् एतत्**. And उपदेशे\n'
        '  is still running, which is what gets तीर्णः: with the इ\n'
        '  substituted first there would be no ॠ left'
    ),
)

register(
    '7.2.12',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — सनि ग्रहगुहोश्च — nor for ग्रह्, गुह् and an उक्-final\n'
        '  root before सन्: **जिघृक्षति, जुघुक्षति; रुरूषति, लुलूषति**. And\n'
        '  श्रि is NOT carried down from 7.2.11, since 7.2.49 makes its इट्\n'
        '  optional. For ग्रह् the refusal is absolute; for गुह्, being\n'
        '  ऊदित्, there is an option — **ग्रहेर् नित्यं प्राप्तः, गुहेर्\n'
        '  ऊदित्त्वाद् विकल्पः**'
    ),
)

register(
    '7.2.13',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि — eight roots take no इट्\n'
        '  in the perfect: **चकृव, ससृव, बभृव, ववृव, तुष्टुव, दुद्रुव,\n'
        '  सुस्रुव, शुश्रुव**.\n'
        '\n'
        'SETTLED — **AND IT IS A नियम AND NOT A FRESH REFUSAL.** **सिद्धे\n'
        '  सत्यारम्भो नियमार्थः। क्रादय एव लिट्य् अनिटस् ततोऽन्ये सेट इति** —\n'
        '  these eight and no others are अनिट् in the perfect, which is what\n'
        '  gives बिभिदिव its इट्. And the restriction cuts two ways at once:\n'
        '  for the अनुदात्तोपदेश roots it turns on the root, for वृञ् and\n'
        '  वृङ् on the affix, **तदुभयस्याप्ययं नियमः**. It even overrides\n'
        '  7.2.63, so तुष्टोथ and दुद्रोथ have no इट् either'
    ),
)

register(
    '7.2.14',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — श्वीदितो निष्ठायाम् — nor for श्वि and an ईदित् root in\n'
        '  the निष्ठा: **शूनः; लग्नः; उद्विग्नः; दीप्तः**.\n'
        '\n'
        'SETTLED — **AND THE WORD निष्ठा NOW GOVERNS FOR TWENTY-ONE SŪTRAS.**\n'
        '  **निष्ठायाम् इत्यधिकार आर्धधातुकस्येड् वलादेः इति यावत्** — to\n'
        '  7.2.34, where the run ends because 7.2.35 finally gives the इट्.\n'
        '\n'
        'SETTLED — **AND डीङ् BEING READ AMONG THE ओदित् ROOTS IS A ज्ञापक.**\n'
        "  8.2.45 turns the निष्ठा's त् into न् after an ओदित्, and that\n"
        '  could only bite if the त् were there without an इट् in front — **स\n'
        '  हि नत्वार्थः, नत्वं च निष्ठातोऽनन्तरस्य विधीयते। उड्डीनः**'
    ),
)

register(
    '7.2.15',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — यस्य विभाषा — nor for any root whose इट् is made OPTIONAL\n'
        "  somewhere else: **विधूतः** by 7.2.44's option, **गूढः** for गुह्,\n"
        "  **वृद्धः** by 7.2.56's. An option elsewhere becomes a refusal\n"
        '  here.\n'
        '\n'
        'SETTLED — **AND ONE WORD ESCAPES IT BY BEING LAID DOWN.** पत् has an\n'
        '  optional इट् by a vārttika on 7.2.49, so this rule should refuse\n'
        "  it in the निष्ठा; and 2.1.24's **द्वितीया श्रितातीतपतित०** reads\n"
        '  पतित WITH its इट्, **निपातनाद् इडागमः**'
    ),
)

register(
    '7.2.16',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — आदितश्च — nor for an आदित् root: **मिन्नः, क्ष्विण्णः,\n'
        '  स्विन्नः**, and by the च also **आश्वस्तः, वान्तः**.\n'
        '\n'
        'SETTLED — **AND THE SPLIT FROM THE NEXT SŪTRA IS A ज्ञापक.** The two\n'
        '  could have been one — *आदितश्च विभाषा भावादिकर्मणोः* — and 7.2.15\n'
        '  would have covered the rest. Split, they teach a principle: **यद्\n'
        '  उपाधेर् विभाषा तद् उपाधेः प्रतिषेध इति** — where an option is\n'
        '  given under a condition, the refusal that follows from it holds\n'
        '  under that same condition only. Which is how विदितः keeps its इट्,\n'
        "  7.2.68's option being for विद् *to get*"
    ),
)

register(
    '7.2.17',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — विभाषा भावादिकर्मणोः — but in the ABSTRACT and at the\n'
        '  START of an action the refusal is optional: **मिन्नमनेन,\n'
        '  मेदितमनेन; प्रमिन्नः, प्रमेदितः**. The Saunāgas want शक् optional\n'
        '  in the object sense too — **शकितो घटः कर्तुम्, शक्तो घटः कर्तुम्**\n'
        '  — and not in the abstract, **शक्तमनेन**'
    ),
)

register(
    '7.2.18',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि\n'
        '  मन्थमनस्तमःसक्ताविस्पष्टस्वरानायासभृशेषु — eight forms laid down\n'
        '  against eight senses, ONE TO ONE: **क्षुब्धो मन्थः** but\n'
        '  **क्षुभितं मन्थेन**; **स्वान्तम्** of the mind but **स्वनितो\n'
        '  मृदङ्गः**; **ध्वान्तम्** of darkness; **लग्नम्** of what sticks;\n'
        '  **म्लिष्टम्** of what is indistinct; **विरिब्धम्** of a sound. A\n'
        '  comparison lets the sense in sideways — **क्षुब्धा गिरिनदी\n'
        "  इत्येवमाद्य् उपमानाद् भविष्यति** — and म्लिष्ट's इ is laid down\n"
        '  with the rest, **इत्वमप्येकारस्य निपातनादेव**'
    ),
)

register(
    '7.2.19',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — धृषिशसी वैयात्ये — धृष् and शस् take no इट् in the निष्ठा\n'
        '  where BOLDNESS is meant: **धृष्टोऽयम्, विशस्तोऽयम्**. **वियातस्य\n'
        '  भावो वैयात्यम्, प्रागल्भ्यम्, अविनीतता**.\n'
        '\n'
        'SETTLED — **AND IT IS A नियम, BOTH REFUSALS BEING ALREADY\n'
        '  SUPPLIED.** धृष् is आदित् and caught by 7.2.16; शस् is उदित् and\n'
        '  caught through 7.2.15. **नियमार्थं वचनम्। धृषिशस्योर् वैयात्य\n'
        "  एवेड् न भवति** — in that sense only, and 7.2.17's option does not\n"
        '  reach it: **भावादिकर्मणोरपि वैयात्ये धृषिर् नास्ति**'
    ),
)

register(
    '7.2.20',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — दृढः स्थूलबलयोः — दृढ is laid down whole where THICKNESS\n'
        '  or STRENGTH is meant: **दृढः स्थूलः; दृढो बलवान्**. Four things at\n'
        '  once: **दृंहेः क्तप्रत्यय इडभावः, हकारनकारयोर् लोपः, परस्य\n'
        '  ढत्वम्**.\n'
        '\n'
        'SETTLED — **AND THE ह्-LOSS IS LAID DOWN RATHER THAN DERIVED, TO\n'
        '  ESCAPE 8.2.1.** Lose the ढ instead and the loss is असिद्ध for\n'
        "  everything earlier, and then 6.4.161's र would not reach द्रढिमा;\n"
        "  6.4.56's अय् would not reach परिद्रढय्य; and 4.1.78's ष्यङ् would\n"
        '  wrongly reach पारिदृढी. Three rules saved by one choice of what to\n'
        '  lay down'
    ),
)

register(
    '7.2.21',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — प्रभौ परिवृढः — and परिवृढ where a LORD is meant:\n'
        '  **परिवृढः कुटुम्बी**. **पूर्वेण तुल्यम् एतत्** — built exactly as\n'
        '  दृढ was, from वृंह्, and the ह्-loss laid down for the same three\n'
        '  reasons: **परिव्रढयति, परिव्रढय्य गतः, पारिवृढी कन्या**'
    ),
)

register(
    '7.2.22',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — कृच्छ्रगहनयोः कषः — कष् takes no इट् where HARDSHIP or a\n'
        '  THICKET is meant: **कष्टोऽग्निः; कष्टं व्याकरणम्; ततोऽपि कष्टतराणि\n'
        '  सामानि; कष्टानि वनानि; कष्टाः पर्वताः**. **कृच्छ्रं दुःखम्,\n'
        '  तत्कारणमप्य् अग्न्यादिकं कृच्छ्रम् इत्युच्यते** — the cause of the\n'
        "  difficulty is called by the difficulty's name, which is how fire\n"
        '  and grammar get on the same list'
    ),
)

register(
    '7.2.23',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — घुषिरविशब्दने — घुष् takes none where no DECLARING is\n'
        '  meant: **घुष्टा रज्जुः; घुष्टौ पादौ**. There are two घुष् roots,\n'
        '  one in भ्वादि and one in चुरादि, and **तयोर् इह सामान्येन\n'
        '  ग्रहणम्**.\n'
        '\n'
        'SETTLED — **AND THE EXCEPTION IS ITSELF A ज्ञापक.**\n'
        '  **विशब्दनप्रतिषेधश्च ज्ञापकश् चुरादिणिज् विशब्दनार्थस्यानित्य\n'
        '  इति** — the चुरादि णिच् is not compulsory in that sense, which\n'
        '  lets **जुघुषुः पुष्यमाणवाः** stand'
    ),
)

register(
    '7.2.24',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — अर्देः संनिविभ्यः — अर्द् takes none after सम्, नि and वि:\n'
        '  **समर्णः, न्यर्णः, व्यर्णः**. Three preverbs and no fourth, and\n'
        '  the vṛtti tests both halves of the condition: **अर्देरिति किम्?\n'
        '  समेधितः। संनिविभ्य इति किम्? अर्दितः**'
    ),
)

register(
    '7.2.25',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — अभेश्चाविदूर्येऽर्थे — and after अभि where NEARNESS is\n'
        '  meant: **अभ्यर्णा सेना; अभ्यर्णा शरत्**. **विदूरं विप्रकृष्टम्,\n'
        '  ततोऽन्यद् अविदूरम्, तस्य भाव आविदूर्यम्** — and the word being\n'
        "  laid down here is what lets it escape 5.1.121's refusal of an\n"
        '  abstract affix after a नञ्-compound'
    ),
)

register(
    '7.2.26',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — णेरध्ययने वृत्तम् — वृत्त is laid down for the causal of\n'
        '  वृत् where RECITATION is meant, with both the इट् refused and the\n'
        '  णि dropped: **वृत्तो गुणो देवदत्तेन; वृत्तं पारायणं देवदत्तेन**.\n'
        '\n'
        'SETTLED — **AND THE vṛtti ASKS WHETHER THE SŪTRA IS NEEDED AND GIVES\n'
        '  TWO ANSWERS.** वृत् is intransitive and becomes transitive in the\n'
        "  causal sense, so 5.1.79's pattern would have given the form\n"
        '  anyway. **तत् क्रियते यदापि णिचैव ण्यर्थोऽभिधीयते, तदा वर्तितम्\n'
        '  इत्यध्ययने मा भूद् इति केचित्। अपरे तु वर्तितो गुणो\n'
        '  देवदत्तेनेत्यपीच्छन्ति** — some make it exclusive, others allow\n'
        '  both'
    ),
)

register(
    '7.2.27',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — वा दान्तशान्तपूर्णदस्तस्पष्टच्छन्नज्ञप्ताः — seven causal\n'
        '  stems are laid down OPTIONALLY without the इट्, and with the णि\n'
        '  dropped: **दान्तः, दमितः; शान्तः, शमितः; पूर्णः, पूरितः; दस्तः,\n'
        '  दासितः; स्पष्टः, स्पाशितः; छन्नः, छादितः; ज्ञप्तः, ज्ञपितः**.\n'
        '  ज्ञप् is there for a different reason from the rest: 7.2.49 makes\n'
        '  its इट् optional, 7.2.15 would then have refused it outright, and\n'
        '  this sūtra gives the option back'
    ),
)

register(
    '7.2.28',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — रुष्यमत्वरसंघुषास्वनाम् — and five roots, likewise\n'
        '  optionally: **रुष्टः, रुषितः; अभ्यान्तः, अभ्यमितः; तूर्णः,\n'
        '  त्वरितः; संघुष्टौ पादौ, संघुषितौ पादौ; आस्वान्तो देवदत्तः,\n'
        '  आस्वनितो देवदत्तः**.\n'
        '\n'
        'SETTLED — **AND TWO OF THE FIVE DISPLACE EARLIER RULES BY BEING\n'
        '  LATER.** संघुष् would have been refused outright by 7.2.23 even\n'
        '  where declaring is meant, and आस्वन् laid down by 7.2.18 where the\n'
        '  mind is meant; **परत्वाद् अयम् एव विकल्पो भवति** — this option\n'
        '  wins over both, and संघुष्टं वाक्यम् and आस्वान्तं मनः have their\n'
        '  इट् forms beside them'
    ),
)

register(
    '7.2.29',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — हृषेर्लोमसु — हृष् takes the इट् optionally where HAIR is\n'
        '  meant: **हृष्टानि लोमानि, हृषितानि लोमानि; हृष्टाः केशाः, हृषिताः\n'
        '  केशाः**.\n'
        '\n'
        'SETTLED — **AND THE OPTION IS THERE BECAUSE THERE ARE TWO ROOTS.**\n'
        '  **हृषु अलीके** is उदित् and so अनिट् in the निष्ठा; **हृष तुष्टौ**\n'
        '  is सेट्. Naming both makes an option out of two settled facts —\n'
        '  **तयोर् उभयोर् इह ग्रहणम् इत्युभयत्रविभाषेयम्**. A vārttika adds\n'
        '  two more senses: **विस्मितप्रतिघातयोश्चेति वक्तव्यम्**'
    ),
)

register(
    '7.2.30',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — अपचितश्च — अपचित is laid down beside अपचायित, with the इट्\n'
        '  refused and चि standing for चाय्: **अपचितोऽनेन गुरुः, अपचायितोऽनेन\n'
        '  गुरुः**. And a vārttika makes it compulsory before क्तिन् —\n'
        '  **क्तिनि नित्यम् इति वक्तव्यम्। अपचितिः**'
    ),
)

register(
    '7.2.31',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — ह्रु ह्वरेश्छन्दसि — ह्वृ becomes ह्रु in the निष्ठा in\n'
        '  the Veda: **ह्रुतस्य चाह्रुतस्य च; अह्रुतमसि हविर्धानम्**'
    ),
)

register(
    '7.2.32',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — अपरिह्वृताश्च — but अपरिह्वृत is laid down WITHOUT that\n'
        '  substitution: **अपरिह्वृताः सनुयाम वाजम्**. A निपातन whose whole\n'
        '  content is that the sūtra before does not apply'
    ),
)

register(
    '7.2.33',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED — सोमे ह्वरितः — and ह्वरित is laid down of SOMA, with the\n'
        '  इट् GIVEN and guṇa besides: **मा नः सोमो ह्वरितः;\n'
        "  विह्वरितस्त्वम्**. The first of the run's two rules that supply\n"
        '  the augment instead of refusing it'
    ),
)

register(
    '7.2.34',
    apply=no_it,
    codification=_NO_IT,
    notes=(
        'SETTLED —\n'
        '  ग्रसितस्कभितस्तभितोत्तभितचत्तविकस्तविशस्तॄशंस्तृशास्तृतरुतृतरूतृवरुतृवरूतृवरुत्रीरुज्ज्वलितिक्षरितिक्षमितिवमित्यमितीति\n'
        '  च — nineteen Vedic forms laid down, and most of them WITH the इट्\n'
        '  that the ordinary grammar refuses: **ग्रसितं वा एतत् सोमस्य**\n'
        '  where the language has ग्रस्तम्; **विष्कभिते अजरे** for\n'
        '  विष्कब्धम्; **येन स्वः स्तभितम्** for स्तब्धम्; **सत्येनोत्तभिता\n'
        '  भूमिः** for उत्तब्धा. ग्रस्, स्कम्भ् and स्तम्भ् are all उदित् and\n'
        '  so अनिट् in the निष्ठा, and the Veda has them the other way.\n'
        '\n'
        'SETTLED — **AND उत्तभित IS NAMED WITH ITS PREVERB ON PURPOSE.**\n'
        '  **उत्तभितेति उत्पूर्वस्य निपातनसामर्थ्याद् अन्योपसर्गपूर्वः\n'
        '  स्तभितशब्दो न भवति** — laid down with उत्, it is available with\n'
        '  उत् and with nothing else.\n'
        '\n'
        'SETTLED — **AND THIS CLOSES THE निष्ठा HEADING.** The next sūtra is\n'
        '  आर्धधातुकस्येड् वलादेः, which finally gives the इट् that all\n'
        '  twenty-seven of these have been refusing'
    ),
)


_THE_IT = (
    'the_it(root, gana=..., before=..., upasarga=..., pada=..., '
    'sense=..., chandasi=...) -> whether the it augment comes, '
    'how long it is, or that it is refused, by rule of 7.2.35-78.'
)

register(
    '7.2.35',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — आर्धधातुकस्येड् वलादेः — an ārdhadhātuka affix beginning\n'
        '  with a वल् sound takes the इट्: **लविता, लवितुम्, लवितव्यम्;\n'
        '  पविता, पवितुम्, पवितव्यम्**.\n'
        '\n'
        'SETTLED — **THIS IS THE RULE THE WHOLE OF 7.2.8–34 WAS STATED\n'
        '  BEFORE.** Twenty-seven sūtras refuse an augment that only now\n'
        '  exists. And the छन्दस् heading has lapsed — **छन्दसीति\n'
        '  निवृत्तम्**.\n'
        '\n'
        'SETTLED — **AND IT SAYS आर्धधातुक RATHER THAN LEAVING 7.2.76 TO\n'
        '  RESTRICT IT.** **रुदादिभ्यः सार्वधातुके इत्येतस्मिन् नियमार्थे\n'
        '  विज्ञायमाने प्रतिपत्तिगौरवं भवति** — a restriction there would\n'
        '  have done the same work and cost the reader more. And इट् is said\n'
        '  twice over, **प्रतिषेधनिवृत्त्यर्थम्**, to end the refusals that\n'
        '  have been running'
    ),
)

register(
    '7.2.36',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — स्नुक्रमोरनात्मनेपदनिमित्ते — स्नु and क्रम् take the इट्\n'
        '  where they are NOT what occasions an आत्मनेपद ending:\n'
        '  **प्रस्नविता, प्रक्रमिता**.\n'
        '\n'
        'SETTLED — **AND IT IS A RESTRICTION WHOSE WHOLE POINT IS THE\n'
        '  REFUSAL.** **नियमार्थम् इदम्... प्रतिषेधफलं चेदं सूत्रम्।\n'
        '  स्नुक्रमोर् उदात्तत्वाद् इट् सिद्ध एव** — both roots are उदात्त\n'
        '  and 7.2.35 gives them the इट् anyway, so stating it again can only\n'
        '  be to take it away in the other case'
    ),
)

register(
    '7.2.37',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — ग्रहोऽलिटि दीर्घः — after ग्रह् the इट् is LONG, except in\n'
        '  the perfect: **ग्रहीता, ग्रहीतुम्, ग्रहीतव्यम्**. The next seven\n'
        '  sūtras are about this ई and not about whether the इ is there at\n'
        '  all'
    ),
)

register(
    '7.2.38',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — वॄतो वा — and after वृ and a ॠ-final root the इट् is long\n'
        '  OPTIONALLY: **वरिता, वरीता; प्रावरिता, प्रावरीता; तरिता, तरीता;\n'
        '  आस्तरिता, आस्तरीता**. **वृ इति वृङ्वृञोः सामान्येन ग्रहणम्** — one\n'
        '  syllable naming both roots'
    ),
)

register(
    '7.2.39',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — न लिङि — but not in the optative: **विवरिषीष्ट,\n'
        '  प्रावरिषीष्ट, आस्तरिषीष्ट, विस्तरिषीष्ट** — the short इ only'
    ),
)

register(
    '7.2.40',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — सिचि च परस्मैपदेषु — nor before a सिच् followed by a\n'
        '  परस्मैपद ending: **प्रावारिष्टाम्, प्रावारिषुः; अतारिष्टाम्,\n'
        '  अतारिषुः; आस्तारिष्टाम्, आस्तारिषुः**'
    ),
)

register(
    '7.2.41',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — इट् सनि वा — and before सन् the इट् itself is optional:\n'
        '  **वुवूर्षते, विवरिषते, विवरीषते; तितीर्षति, तितरिषति, तितरीषति**.\n'
        '  7.2.12 had refused it outright for an उक्-final root; this gives\n'
        "  the option back, and 7.2.38's lengthening then applies on the side\n"
        '  where the इट् is there. चिकीर्षति has none, its ॠ being one a rule\n'
        '  made and not one the उपदेश has'
    ),
)

register(
    '7.2.42',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — लिङ्सिचोरात्मनेपदेषु — and in the आत्मनेपद optative and\n'
        '  aorist the इट् is optional: **वृषीष्ट, वरिषीष्ट; आस्तरिषीष्ट,\n'
        '  आस्तीर्षीष्ट; अवृत, अवरिष्ट, अवरीष्ट**. The vṛtti gives no\n'
        '  counter-example for the optative — **असंभवाद्\n'
        '  यासुटोऽवलादित्वात्**, its यासुट् does not begin with a वल् at all'
    ),
)

register(
    '7.2.43',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — ऋतश्च संयोगादेः — and for an ऋ-final root that BEGINS with\n'
        '  a cluster: **ध्वृषीष्ट, ध्वरिषीष्ट; स्मृषीष्ट, स्मरिषीष्ट;\n'
        '  अध्वृषाताम्, अध्वरिषाताम्**. संस्कृषीष्ट has none — its सुट् is no\n'
        '  part of the root as taught'
    ),
)

register(
    '7.2.44',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — स्वरतिसूतिसूयतिधूञूदितो वा — four roots and every ऊदित्\n'
        '  root take it optionally: **स्वर्ता, स्वरिता; प्रसोता, प्रसविता;\n'
        '  सोता, सविता; धोता, धविता; विगाढा, विगाहिता; गोप्ता, गोपिता**.\n'
        '\n'
        'SETTLED — **AND EVERY NAME IN THE LIST IS SHAPED TO EXCLUDE\n'
        '  SOMETHING.** **सूतिसूयत्योर् विकरणनिर्देशः षू प्रेरणे इत्यस्य\n'
        '  निवृत्त्यर्थः** — the roots are named with their conjugation-signs\n'
        '  so that a third root of the same shape is left out; **धूञिति\n'
        '  सानुबन्धकस्य निर्देशो धू विधूनने इत्यस्य निवृत्त्यर्थः**, and that\n'
        '  one keeps its इट् always. And वा is said again although वा was\n'
        '  running, **लिङ्सिचोर् निवृत्त्यर्थम्**'
    ),
)

register(
    '7.2.45',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — रधादिभ्यश्च — and eight roots from रध् on: **रद्धा, रधिता;\n'
        '  नंष्टा, नशिता; त्रप्ता, तर्प्ता, तर्पिता; द्रोग्धा, द्रोढा,\n'
        '  द्रोहिता; मोग्धा, मोढा, मोहिता; स्नेग्धा, स्नेढा, स्नेहिता**.\n'
        '\n'
        'SETTLED — **AND WHETHER THE OPTION REACHES THE PERFECT IS\n'
        "  DISPUTED.** 7.2.13's restriction makes them सेट् there; this rule\n"
        '  is later and would make it optional. **केचिद् इच्छन्ति** the\n'
        '  option; **अपरे पुनराहुः — पूर्वविधेर् इण्निषेधविधानसामर्थ्याद्\n'
        '  बलीयस्त्वं प्रतिषेधनियमस्य**, and on that reading ररन्धिव keeps\n'
        '  its इट् without fail'
    ),
)

register(
    '7.2.46',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — निरः कुषः — and कुष् after निर्: **निष्कोष्टा, निष्कोषिता;\n'
        '  निष्कोष्टव्यम्, निष्कोषितव्यम्**.\n'
        '\n'
        'SETTLED — **AND THE FORM निरः IS ITSELF A ज्ञापक.** निसः was what\n'
        '  the grammar owed; निरः is written instead, **रेफान्तम्\n'
        '  उपसर्गान्तरम् अस्तीति ज्ञाप्यते** — there IS a separate र्-final\n'
        "  preverb. Which is what lets 8.2.19's ल् reach निलयनम्: from निस्\n"
        '  the र्-substitution would be असिद्ध and the ल् could not come'
    ),
)

register(
    '7.2.47',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — इण्निष्ठायाम् — but in the निष्ठा it is COMPULSORY:\n'
        '  **निष्कुषितः, निष्कुषितवान्**. **इड्ग्रहणं नित्यार्थम्** — the\n'
        '  word इट् is said again to make it so, and the sūtra exists to beat\n'
        '  7.2.15, which would otherwise have turned the option before it\n'
        '  into a refusal'
    ),
)

register(
    '7.2.48',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — तीषसहलुभरुषरिषः — five roots take it optionally before a\n'
        '  त-initial ārdhadhātuka: **एष्टा, एषिता; सोढा, सहिता; लोब्धा,\n'
        '  लोभिता; रोष्टा, रोषिता; रेष्टा, रेषिता**. And the इष् meant is\n'
        '  **इषु इच्छायाम्** alone: the दैवादिक and क्र्यादि roots of that\n'
        '  shape keep the इट् always, **प्रेषिता, प्रेषितुम्**'
    ),
)

register(
    '7.2.49',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — सनीवन्तर्धभ्रस्जदम्भुश्रिस्वृयूर्णुभरज्ञपिसनाम् — इ-final\n'
        '  roots and eleven named ones take it optionally before सन्:\n'
        '  **दिदेविषति, दुद्यूषति; अर्दिधिषति, ईर्त्सति; बिभ्रज्जिषति,\n'
        '  बिभ्रक्षति; दिदम्भिषति, धिप्सति; उच्छिश्रयिषति, उच्छिश्रीषति;\n'
        '  प्रोर्णुनविषति, प्रोर्णुनूषति**. भर is the भ्वादि भृञ्, and the\n'
        '  vṛtti knows it from the conjugation sign — **शपा निर्देशात्**'
    ),
)

register(
    '7.2.50',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — क्लिशः क्त्वानिष्ठयोः — क्लिश् takes it optionally before\n'
        '  क्त्वा and the निष्ठा: **क्लिष्ट्वा, क्लिशित्वा; क्लिष्टः,\n'
        '  क्लिशितः**. Two roots of the shape and two reasons: for **क्लिशू\n'
        '  विबाधने** the option in क्त्वा was already there and 7.2.15 would\n'
        '  have refused the निष्ठा outright; for **क्लिश उपतापे** the इट्\n'
        '  would have been compulsory in both, **तदर्थं क्त्वाग्रहणं\n'
        '  क्रियते**'
    ),
)

register(
    '7.2.51',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — पूङश्च — and पूङ्: **पूत्वा, पवित्वा; सोमोऽतिपूतः,\n'
        '  सोमोऽतिपवितः; पूतवान्, पवितवान्**. 7.2.11 had refused it for an\n'
        '  उक्-final root before a कित्, and this gives the option back'
    ),
)

register(
    '7.2.52',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — वसतिक्षुधोरिट् — वस् and क्षुध् take it without fail:\n'
        '  **उषित्वा, उषितः, उषितवान्; क्षुधित्वा, क्षुधितः, क्षुधितवान्**.\n'
        '  वस् is named with its conjugation sign only to be identified —\n'
        '  **वसतीति विकरणो निर्देशार्थ एव** — since being उदात्त it would\n'
        '  have had the इट् anyway; and **पुनरिड्ग्रहणं नित्यार्थम्**'
    ),
)

register(
    '7.2.53',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — अञ्चेः पूजायाम् — and अञ्च् where HONOURING is meant:\n'
        '  **अञ्चित्वा जानु जुहोति; अञ्चिता अस्य गुरवः**. 7.2.56 would have\n'
        '  made the क्त्वा optional and 7.2.15 would have refused the निष्ठा;\n'
        '  the sūtra is begun for both, **तदर्थम् इदम् प्रारब्धम्**'
    ),
)

register(
    '7.2.54',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — लुभो विमोचने — and लुभ् where CONFUSING is meant:\n'
        '  **लुभित्वा, लोभित्वा; विलुभिताः केशाः; विलुभितः सीमन्तः**.\n'
        '  **विमोहनम् आकुलीकरणम्** — the sense is hair in disarray and not\n'
        '  desire'
    ),
)

register(
    '7.2.55',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — जॄव्रश्च्योः क्त्वि — जॄ and व्रश्च् take it before\n'
        '  क्त्वा: **जरित्वा, जरीत्वा; व्रश्चित्वा**. For जॄ 7.2.11 had\n'
        '  refused it and for व्रश्च्, being ऊदित्, it was an option.\n'
        '  **क्त्वाग्रहणं निष्ठानिवृत्त्यर्थम्** — the निष्ठा running down\n'
        '  from 7.2.50 is cut off here'
    ),
)

register(
    '7.2.56',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — उदितो वा — and an उदित् root takes it optionally before\n'
        '  क्त्वा: **शमित्वा, शान्त्वा; तमित्वा, तान्त्वा; दमित्वा,\n'
        '  दान्त्वा**'
    ),
)

register(
    '7.2.57',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — सेऽसिचि कृतचृतच्छृदतृदनृतः — five roots take it optionally\n'
        '  before a स-initial ārdhadhātuka that is not सिच्: **कर्त्स्यति,\n'
        '  कर्तिष्यति; चिकृत्सति, चिकर्तिषति; छर्त्स्यति, छर्दिष्यति;\n'
        '  तर्त्स्यति, तर्दिष्यति; नर्त्स्यति, नर्तिष्यति**'
    ),
)

register(
    '7.2.58',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — गमेरिट् परस्मैपदेषु — गम् takes it without fail before a\n'
        '  स-initial ārdhadhātuka in the परस्मैपद: **गमिष्यति, अगमिष्यत्,\n'
        '  जिगमिषति**. **इड्ग्रहणं नित्यार्थम्**. And the refusal is only\n'
        '  where the root and the आत्मनेपद ending stand in one word —\n'
        '  **आत्मनेपदेन समानपदस्थस्य गमेर् अयम् इडागमो नेष्यते। अन्यत्र\n'
        '  सर्वत्रैवेष्यते**, so संजिगमिषिता and जिगमिष त्वम् both keep it'
    ),
)

register(
    '7.2.59',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — न वृद्भ्यश्चतुर्भ्यः — but four roots refuse it there:\n'
        '  **वर्त्स्यति, विवृत्सति; शर्त्स्यति; स्यन्त्स्यति, सिस्यन्त्सति**.\n'
        '\n'
        'SETTLED — **AND THE WORD चतुर्भ्यः IS ARGUED TO BE UNNECESSARY AND\n'
        "  KEPT.** The धातुपाठ's own वृत् already marks where the द्युतादि\n"
        '  end; if it marks the वृतादि too, nothing goes wrong. It is kept so\n'
        "  that स्यन्द्'s ऊदित् option — which is अन्तरङ्ग — should be beaten\n"
        '  by this refusal all the same'
    ),
)

register(
    '7.2.60',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — तासि च कॢपः — and कॢप् refuses it before तासि too: **श्वः\n'
        '  कल्प्ता; कल्प्स्यति, अकल्प्स्यत्, चिक्ऌप्सति**. The same rule\n'
        '  about one word holds here — **क्ऌपेरप्य् आत्मनेपदेन समानपदस्थस्य\n'
        '  इडागम इष्यते। अन्यत्र प्रतिषेधः**'
    ),
)

register(
    '7.2.61',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — अचस्तास्वत् थल्यनिटो नित्यम् — a vowel-final root that is\n'
        '  ALWAYS अनिट् before तासि refuses the इट् in the थल् as well:\n'
        '  **ययाथ, चिचेथ, निनेथ, जुहोथ**. **नित्यग्रहणं** is what shuts out\n'
        "  विधोता's optional case.\n"
        '\n'
        'SETTLED — **AND तास्वत् IS SAID AS A COMPARISON FOR A REASON.**\n'
        '  **तासौ सतस्थलि प्रतिषेधार्थः। यो हि तासाव् असन्, असत्त्वात् च\n'
        '  नित्यानिट्, तस्य थलि प्रतिषेधो न भवति** — a root that has no तासि\n'
        '  form at all is not अनिट् there in the required sense, so जघसिथ and\n'
        '  उवयिथ keep their इट्'
    ),
)

register(
    '7.2.62',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — उपदेशेऽत्वतः — and a root that HAS an अ as it is taught\n'
        '  and is अनिट् before तासि: **पपक्थ, इयष्ठ, शशक्थ**'
    ),
)

register(
    '7.2.63',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — ऋतो भारद्वाजस्य — an ऋ-final root refuses it in the थल्,\n'
        "  IN BHĀRADVĀJA'S VIEW: **सस्मर्थ, दध्वर्थ**. **सिद्धे सत्यारम्भो\n"
        '  नियमार्थः। ऋत एव भारद्वाजस्य, नान्येषां धातूनाम्** — a\n'
        '  restriction, and what the two sūtras before had made compulsory\n'
        '  becomes optional everywhere else: **ययिथ, वविथ, पेचिथ, शेकिथ**.\n'
        "  Naming the teacher is Pāṇini's way of recording a view rather than\n"
        '  adopting it'
    ),
)

register(
    '7.2.64',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — बभूथाततन्थजगृम्भववर्थेति निगमे — four Vedic perfects laid\n'
        '  down whole: **त्वं हि होता प्रथमो बभूथ**, where the language has\n'
        '  बभूविथ; **येनान्तरिक्षम् उर्वाततन्थ** for आतेनिथ; **जगृभ्मा ते\n'
        '  दक्षिणम् इन्द्र हस्तम्** for जगृहिम; **ववर्थ त्वं हि ज्योतिषा**\n'
        '  for ववरिथ. And it is a restriction and not a fresh refusal —\n'
        '  **निगम एव न भाषायाम् इति**'
    ),
)

register(
    '7.2.65',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — विभाषा सृजिदृशोः — सृज् and दृश् refuse it in the थल्\n'
        '  optionally: **सस्रष्ठ, ससर्जिथ; दद्रष्ठ, ददर्शिथ**'
    ),
)

register(
    '7.2.66',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — इडत्त्यर्तिव्ययतीनाम् — but अद्, ऋ and व्ये take it in the\n'
        '  थल् without fail: **आदिथ, आरिथ, विव्ययिथ**. For अद् and व्ये\n'
        "  7.2.63's restriction had made it optional, for ऋ it was refused\n"
        '  outright; **अत्रेड्ग्रहणं विस्पष्टार्थम्**, the word इट् being\n'
        '  there only to make the rule read plainly'
    ),
)

register(
    '7.2.67',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — वस्वेकाजाद्घसाम् — before वसु the इट् comes for a\n'
        '  reduplicated root of ONE syllable, for an आ-final root, and for\n'
        '  घस्: **आदिवान्, आशिवान्, पेचिवान्, शेकिवान्; ययिवान्, तस्थिवान्;\n'
        '  जक्षिवान्**.\n'
        '\n'
        'SETTLED — **AND *ONE SYLLABLE* IS COUNTED AFTER THE REDUPLICATION IS\n'
        '  DONE.** **धात्वभ्यासयोर् एकादेशे कृत एत्वाभ्यासलोपयोश्च कृतयोः\n'
        '  कृतद्विर्वचना एत एकाचो भवन्ति** — पच् is two syllables until the\n'
        '  perfect makes it पेच्. And it is a restriction: **एकाजाद्घसाम् एव\n'
        '  वसाव् इडागमो भवति नान्येषाम्**, so बिभिद्वान् and शिश्रिवान् have\n'
        '  none'
    ),
)

register(
    '7.2.68',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — विभाषा गमहनविदविशाम् — and four roots take it optionally:\n'
        '  **जग्मिवान्, जगन्वान्; जघ्निवान्, जघन्वान्; विविदिवान्,\n'
        '  विविद्वान्; विविशिवान्, विविश्वान्**. The विद् meant is the\n'
        '  तौदादिक one *to get* — **विशिना साहचर्यात्** — and the one meaning\n'
        '  *to know* keeps विविद्वान् always. A vārttika adds दृश्:\n'
        '  **ददृशिवान्, ददृश्वान्**'
    ),
)

register(
    '7.2.69',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — सनिंससनिवांसम् — ससनिवांसम् is laid down after सनिम्, with\n'
        '  the इट् and with no ए and no reduplication-loss: **आजिं\n'
        '  त्वाग्ने... सनिं ससनिवांसम्**. Elsewhere it is सेनिवांसम्, and\n'
        '  **भाषायां सेनिवांसम् इति भवति**'
    ),
)

register(
    '7.2.70',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — ऋद्धनोः स्ये — an ऋ-final root and हन् take it before स्य:\n'
        "  **करिष्यति, हरिष्यति, हनिष्यति**. And it beats 7.2.44's option for\n"
        '  स्वृ by prior contradiction — **स्वरतेर् वेट्त्वाद् ऋद्धनोः स्य\n'
        '  इत्येतद् भवति विप्रतिषेधेन। स्वरिष्यति**'
    ),
)

register(
    '7.2.71',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — अञ्जेः सिचि — अञ्ज् takes it before सिच्: **आञ्जीत्,\n'
        '  आञ्जिष्टाम्, आञ्जिषुः**. Being ऊदित् it would only have had the\n'
        '  option'
    ),
)

register(
    '7.2.72',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — स्तुसुधूञ्भ्यः परस्मैपदेषु — स्तु, सु and धूञ् take it\n'
        '  before a सिच् in the परस्मैपद: **अस्तावीत्, असावीत्, अधावीत्**'
    ),
)

register(
    '7.2.73',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — यमरमनमातां सक् च — यम्, रम्, नम् and every आ-final stem\n'
        '  take the augment सक् AND the इट् before a सिच् in the परस्मैपद:\n'
        '  **अयंसीत्, व्यरंसीत्, अनंसीत्; आयासीत्, अयासिष्टाम्**. 7.2.3 would\n'
        '  have given the four consonant-final ones vṛddhi, and 7.2.4 refuses\n'
        '  it once the इट् is there'
    ),
)

register(
    '7.2.74',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — स्मिपूङ्रञ्ज्वशां सनि — five roots take it before सन्:\n'
        '  **सिस्मयिषते, पिपविषते, अरिरिषति, अञ्जिजिषति, अशिशिषते**.\n'
        '  **ङकारग्रहणं पूञो मा भूत्** — the marker is there to keep the\n'
        '  other पू out, and अश् is named as the ऊदित् one so that अश्नाति\n'
        '  keeps its इट् always'
    ),
)

register(
    '7.2.75',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — किरश्च पञ्चभ्यः — and five more: **चिकरिषति, जिगरिषति,\n'
        '  दिदरिषते, दिधरिषते, पिपृच्छिषति**. 7.2.41 had made it optional for\n'
        '  कॄ and गॄ; this makes it compulsory, and the lengthening of 7.2.38\n'
        '  is not wanted here — **वृतो वा इति चास्येटो दीर्घत्वं नेच्छन्ति**'
    ),
)

register(
    '7.2.76',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — रुदादिभ्यः सार्वधातुके — five roots take the इट् before a\n'
        '  वल्-initial सार्वधातुक: **रोदिति, स्वपिति, श्वसिति, प्राणिति,\n'
        '  जक्षिति**. This is the affix class 7.2.35 shut out by name, and\n'
        '  the last three sūtras of the run are all about it'
    ),
)

register(
    '7.2.77',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — ईशः से — and ईश् before से: **ईशिषे, ईशिष्व**. One root\n'
        '  and one ending, and the sūtra says no more than that — but the\n'
        '  next one is read by some so as to catch ईशिध्वे as well, which\n'
        "  would make this rule's से the smaller half of a pair"
    ),
)

register(
    '7.2.78',
    apply=the_it,
    codification=_THE_IT,
    notes=(
        'SETTLED — ईडजनोर्ध्वे च — and ईड् and जन् before ध्वे and से:\n'
        '  **ईडिध्वे, ईडिध्वम्, ईडिषे, ईडिष्व; जनिध्वे, जनिषे, जनिष्व**.\n'
        '\n'
        'SETTLED — **AND SOME READ THE SŪTRA DIFFERENTLY TO CATCH ONE MORE\n'
        '  FORM.** **ध्वेशब्द ईशेरपि इडागम इष्यते — ईशिध्वे, ईशिध्वम् इति।\n'
        '  तदर्थं केचिद् ईडिजनोः स्ध्वे च इति सूत्रं पठन्ति** — a variant\n'
        '  reading recorded rather than settled'
    ),
)


_BEFORE_ENDING = (
    'before_ending(stem, gana=..., before=..., part=..., '
    'number=..., gender=...) -> what the stem becomes before an '
    'ending, by rule of 7.2.79-113.'
)

register(
    '7.2.79',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — लिङः सलोपोऽनन्त्यस्य — a सार्वधातुक लिङ् loses a स् that\n'
        '  is NOT its last sound: **कुर्यात्, कुर्याताम्, कुर्युः; कुर्वीत,\n'
        '  कुर्वीयाताम्, कुर्वीरन्**. **कः पुनर् अनन्त्यो लिङः सकारः? यो\n'
        '  यासुट्सुट्सीयुटाम्** — the स् of the three augments, and no other'
    ),
)

register(
    '7.2.80',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — अतो येयः — after an अ-final stem the या of a सार्वधातुक\n'
        '  becomes इय्: **पचेत्, पचेताम्, पचेयुः**.\n'
        '\n'
        "SETTLED — **AND IT HAS TO BEAT TWO OTHER RULES AT ONCE.** 6.1.96's\n"
        "  पररूप is displaced in पचेयुः; and asked why 6.4.48's अ-loss does\n"
        "  not apply first, the vṛtti answers that 7.3.101's lengthening\n"
        '  would have applied too. **तद् अनेनावश्यं विध्यन्तरं बाधितव्यम्** —\n'
        '  something must be displaced whatever one does, and what displaces\n'
        '  the one displaces the other'
    ),
)

register(
    '7.2.81',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — आतो ङितः — and the आ of a ङित् ending after an अ-final\n'
        '  stem: **पचेते, पचेथे, पचेताम्, पचेथाम्; यजेते, यजेथे**.\n'
        '\n'
        'SETTLED — **AND THE WORD ङित् IS READ AS *LIKE A ङित्* AND NOT *WHEN\n'
        "  A ङित् FOLLOWS*.** 1.2.4's सार्वधातुकमपित् makes such an affix\n"
        "  ङिद्वत्; read the other way, 1.3.12's अनुदात्तङित आत्मनेपदम् would\n"
        '  wrongly give an आत्मनेपद ending. **ङित इव ङिद्वद् इति**'
    ),
)

register(
    '7.2.82',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        "SETTLED — आने मुक् — before आन the stem's अ takes the augment मुक्:\n"
        '  **पचमानः, यजमानः**.\n'
        '\n'
        'SETTLED — **AND THE AUGMENT BELONGS TO THE अ ALONE, WHICH MATTERS\n'
        '  FOR THE ACCENT.** **अकारमात्रभक्तोऽयं मुक् अदुपदेशग्रहणेन\n'
        "  गृह्यते** — so 6.1.186's अदुपदेशाल्लसार्वधातुकम् still reaches it\n"
        '  and the ending is अनुदात्त. The objection is that with the मुक्\n'
        '  in, the अ is a syllable and a half; the answer is that\n'
        '  **उपदेशग्रहणं तत्र क्रियते**, the rule looks at the root as taught'
    ),
)

register(
    '7.2.83',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — ईदासः — and after आस् the आन becomes ई: **आसीनो यजते**.\n'
        '  The genitive the substitution needs is read out of the ablative\n'
        '  the sūtra has — **अत्र पञ्चम्या परस्य षष्ठी कल्प्यते**'
    ),
)

register(
    '7.2.84',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — अष्टन आ विभक्तौ — अष्टन् takes आ before a case ending:\n'
        '  **अष्टाभिः, अष्टाभ्यः, अष्टानाम्, अष्टासु**.\n'
        '\n'
        'SETTLED — **AND THE विभक्ति HEADING BEGINS HERE.** **मृजेर्वृद्धिः\n'
        '  इत्यतः प्राग् विभक्त्यधिकारः** — thirty rules, ending at 7.2.113.\n'
        '\n'
        'SETTLED — **AND THE OPTION IS NOT IN THE SŪTRA BUT READ OUT OF TWO\n'
        '  OTHERS.** **विकल्पेनायम् आकारो भवति, एतद् ज्ञापितम् अष्टनो\n'
        '  दीर्घात् इति दीर्घग्रहणाद्, अष्टाभ्य औश् इति च कृतात्वस्य\n'
        '  निर्देशात्** — 6.1.172 says *after a LONG अष्टन्* and 7.1.21 names\n'
        '  the one that HAS its आ, and neither wording would be needed if the\n'
        '  आ were compulsory. So अष्टभिः stands beside अष्टाभिः'
    ),
)

register(
    '7.2.85',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — रायो हलि — रै becomes रा before a consonant-initial case\n'
        "  ending: **राभ्याम्, राभिः**. And this sūtra's vṛtti is where the\n"
        '  reader is told how far the विभक्ति heading reaches —\n'
        '  **मृजेर्वृद्धिः इत्यतः प्राग् विभक्त्यधिकारः** — which is a fact\n'
        '  about thirty rules and not about this one'
    ),
)

register(
    '7.2.86',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — युष्मदस्मदोरनादेशे — युष्मद् and अस्मद् take आ before a\n'
        '  case ending that has NOT been replaced: **युष्माभिः, अस्माभिः,\n'
        '  युष्मासु, अस्मासु**. The word अनादेशे is put here although हलि\n'
        '  would have sufficed, because 7.2.89 needs it — **उत्तरत्र\n'
        '  त्वनादेशग्रहणेन प्रयोजनम्... तद् इहैव क्रियते**'
    ),
)

register(
    '7.2.87',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — द्वितीयायां च — and before the accusative: **त्वाम्, माम्,\n'
        '  युवाम्, आवाम्, युष्मान्, अस्मान्**. **आदेशार्थं वचनम्** — the\n'
        "  sūtra exists only for the substitute, since 7.2.86's अनादेशे would\n"
        '  have reached the accusative anyway and its हलि would not'
    ),
)

register(
    '7.2.88',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — प्रथमायाश्च द्विवचने भाषायाम् — and before the nominative\n'
        '  DUAL, in the language: **युवाम्, आवाम्**. The word भाषायाम् is\n'
        '  what keeps the Vedic युवम् standing'
    ),
)

register(
    '7.2.89',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — योऽचि — and य before a vowel-initial case ending that has\n'
        '  not been replaced: **त्वया, मया, त्वयि, मयि, युवयोः, आवयोः**.\n'
        '  **अचीत्येतत्** could have been dropped if हलि were carried down,\n'
        '  and is put in **विस्पष्टार्थम्**'
    ),
)

register(
    '7.2.90',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — शेषे लोपः — and in every OTHER case ending the stem is\n'
        '  dropped: **त्वम्, अहम्, यूयम्, वयम्, तुभ्यम्, मह्यम्, त्वत्, मत्,\n'
        '  तव, मम, युष्माकम्, अस्माकम्**.\n'
        '\n'
        'SETTLED — **AND A VERSE SAYS WHICH ENDINGS THOSE ARE.**\n'
        '  **पञ्चम्याश्च चतुर्थ्याश्च षष्ठीप्रथमयोरपि। यान्यद्विवचनान्यत्र\n'
        '  तेषु लोपो विधीयते** — the ablative, the dative, the genitive and\n'
        '  the nominative, dual excepted. And the loss leaves no feminine:\n'
        '  **त्वं ब्राह्मणी** takes no टाप्, **अलिङ्गे वा युष्मदस्मदी**'
    ),
)

register(
    '7.2.91',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — मपर्यन्तस्य — a heading: **मपर्यन्तस्येत्ययम् अधिकारः।\n'
        '  यदित ऊर्ध्वम् अनुक्रमिष्यामो मपर्यन्तस्येत्येवं तद् वेदितव्यम्** —\n'
        '  every substitute from here replaces only so much of युष्मद् and\n'
        '  अस्मद् as reaches their म्.\n'
        '\n'
        'SETTLED — **AND IT DOES TWO DIFFERENT JOBS.** Without it 7.2.92\n'
        '  would reach युवकाम् and 7.2.97 would replace the whole word, and\n'
        '  then **त्वमयोर् अकारस्य योऽचि इति यकारे कृतेऽनिष्टं रूपं स्यात्**.\n'
        '  The word पर्यन्त rather than a bare मान्त is for showing where the\n'
        '  boundary falls, **अवधिद्योतनार्थम्**'
    ),
)

register(
    '7.2.92',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — युवावौ द्विवचने — where TWO are meant, युष्मद् and अस्मद्\n'
        '  become युव and आव as far as their म्: **युवाम्, आवाम्; युवाभ्याम्,\n'
        '  आवाभ्याम्; युवयोः, आवयोः**. **द्विवचने इत्यर्थग्रहणम्** — the word\n'
        '  names the SENSE and not the ending, which is what gets अतियुवाम्\n'
        "  and अतियुवान् where the compound's own number is different"
    ),
)

register(
    '7.2.93',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — यूयवयौ जसि — before जस् they become यूय and वय: **यूयम्,\n'
        '  वयम्; परमयूयम्, परमवयम्; अतियूयम्, अतिवयम्** — and the rule\n'
        '  reaches a compound ending in them'
    ),
)

register(
    '7.2.94',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — त्वाहौ सौ — before सु they become त्व and अह: **त्वम्,\n'
        '  अहम्; परमत्वम्, परमाहम्; अतित्वम्, अत्यहम्**'
    ),
)

register(
    '7.2.95',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — तुभ्यमह्यौ ङयि — before ङे they become तुभ्य and मह्य:\n'
        '  **तुभ्यम्, मह्यम्; परमतुभ्यम्, परममह्यम्; अतितुभ्यम्, अतिमह्यम्**.\n'
        '  The ending itself has already become अम् by 7.1.28, so what is\n'
        '  left for this rule is the stem in front of it'
    ),
)

register(
    '7.2.96',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — तवममौ ङसि — before the genitive singular they become तव\n'
        '  and मम: **तव, मम; परमतव, परममम**. The ङसि of the sūtra is the\n'
        "  SIXTH case's ending and not the fifth's, which 7.1.32 had already\n"
        '  turned into अत् for these same two words'
    ),
)

register(
    '7.2.97',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — त्वमावेकवचने — and where ONE is meant they become त्व and\n'
        '  म: **त्वाम्, माम्, त्वया, मया, त्वत्, मत्, त्वयि, मयि**. Again a\n'
        '  sense and not an ending, so अतित्वाम् and अतित्वान् come out where\n'
        "  the compound's number is another; and where the ending-specific\n"
        '  substitutes of 7.2.94–96 also reach, those win by prior\n'
        '  contradiction'
    ),
)

register(
    '7.2.98',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — प्रत्ययोत्तरपदयोश्च — and before an AFFIX or a second\n'
        '  compound member, still where one is meant: **त्वदीयः, मदीयः;\n'
        '  त्वत्तरः, मत्तरः; त्वद्यति, मद्यति; त्वत्पुत्रः, मत्पुत्रः;\n'
        '  त्वन्नाथः, मन्नाथः**. The विभक्ति heading had confined the sūtra\n'
        '  before to case endings; **ततोऽन्यत्रापि प्रत्यय उत्तरपदे च यथा\n'
        '  स्याद् इत्ययम् आरम्भः**'
    ),
)

register(
    '7.2.99',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — त्रिचतुरोः स्त्रियां तिसृचतसृ — in the FEMININE त्रि and\n'
        '  चतुर् become तिसृ and चतसृ before a case ending: **तिस्रः, चतस्रः,\n'
        '  तिसृभिः, चतसृभिः**.\n'
        '\n'
        'SETTLED — **AND स्त्रियाम् QUALIFIES THE NUMERAL AND NOT THE STEM.**\n'
        '  **तेन यदा त्रिचतुःशब्दौ स्त्रियाम्, अङ्गं तु लिङ्गान्तरे,\n'
        '  तदाप्यादेशौ भवत एव** — so a masculine compound whose numeral is\n'
        '  feminine still takes them: **प्रियतिसा ब्राह्मणः; प्रियतिसृ\n'
        '  ब्राह्मणकुलम्**'
    ),
)

register(
    '7.2.100',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — अचि र ऋतः — and their ऋ becomes र before a vowel-initial\n'
        '  case ending: **तिस्रस्तिष्ठन्ति, तिस्रः पश्य; चतस्रः पश्य;\n'
        '  प्रियतिस्र आनय**. It displaces four things at once —\n'
        '  **पूर्वसवर्णोत्त्वङिसर्वनामस्थानगुणानाम् अपवादः** — and beats the\n'
        '  last two although they are later, **पूर्वविप्रतिषेधेन**'
    ),
)

register(
    '7.2.101',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — जराया जरसन्यतरस्याम् — जरा optionally becomes जरस् before\n'
        '  a vowel-initial case ending: **जरसा दन्ताः शीर्यन्ते, जरया दन्ताः\n'
        '  शीर्यन्ते; जरसे त्वा परिदद्युः, जरायै त्वा परिदद्युः**.\n'
        '\n'
        'SETTLED — **AND THE ORDER AGAINST TWO OTHER RULES IS WORKED OUT IN\n'
        '  FULL.** In अतिजरसं ब्राह्मणकुलं three things want to happen at\n'
        "  once — the ending's लुक्, its अम्, and this substitution. **लुक्\n"
        '  तावद् अपवादत्वाद् अम्भावेन बाध्यते, अम्भावोऽपि परत्वाद् जरसादेशेन।\n'
        '  न च पुनर् लुक्शास्त्रं प्रवर्तते, भ्रष्टावसरत्वात्** — the लुक्\n'
        '  has missed its turn and does not come back'
    ),
)

register(
    '7.2.102',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — त्यदादीनामः — the त्यदादि stems take अ before a case\n'
        '  ending: **स्यः, त्यौ, त्ये; सः, तौ, ते; यः, यौ, ये; एषः, एतौ, एते;\n'
        '  अयम्, इमौ, इमे; असौ, अमू, अमी; द्वौ, द्वाभ्याम्**. The list is\n'
        '  closed at द्वि — **द्विपर्यन्तानां त्यदादीनाम् अत्वम् इष्यते** —\n'
        '  and a compound headed by one of them still takes it: **परमसः,\n'
        '  परमतौ, परमते**'
    ),
)

register(
    '7.2.103',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — किमः कः — किम् becomes क before a case ending: **कः, कौ,\n'
        '  के**. And it reaches the form with कच् in it, **साकच्कस्याप्ययम्\n'
        '  आदेशो भवति**, which is why the sūtra does not simply say किमोऽत्'
    ),
)

register(
    '7.2.104',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — कु तिहोः — before a त-initial and a ह-initial ending it\n'
        '  becomes कु: **कुतः, कुत्र, कुह**. **तिहोरितीकार उच्चारणार्थः** —\n'
        '  the इ is only there to say the sounds by'
    ),
)

register(
    '7.2.105',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — क्वाति — and before अति it becomes क्व: **क्व गमिष्यसि;\n'
        '  क्व भोक्ष्यते**. A substitute is given rather than an affix so\n'
        "  that 6.4.146's guṇa should not come — **आदेशान्तरवचनम्\n"
        '  ओर्गुणनिवृत्त्यर्थम्**'
    ),
)

register(
    '7.2.106',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — तदोः सः सावनन्त्ययोः — a त् or द् of the त्यदादि that is\n'
        '  not last becomes स् before सु: **स्यः, सः, एषः, असौ**'
    ),
)

register(
    '7.2.107',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — अदस औ सुलोपश्च — अदस् takes औ for its स् AND the सु is\n'
        '  deleted: **असौ**. Two operations in one sūtra.\n'
        '\n'
        'SETTLED — **AND TWO VERSES ASK WHY THE DELETION IS STATED.** **अदसः\n'
        '  सोर् भवेद् औत्वं किं सुलोपो विधीयते।** — the answer is four rules\n'
        "  that would have fired wrongly: the vocative's सु-loss wants a\n"
        '  short vowel, आप् would take ए, a प्रत्ययस्थ क would give इ, and शी\n'
        '  would come. Vārttikas add that with the औ refused for the कच्-form\n'
        '  the स् takes उ instead — **असुकः, असकौ**'
    ),
)

register(
    '7.2.108',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — इदमो मः — इदम् takes म् for its last sound before सु:\n'
        '  **इयम्, अयम्**. A म् substituted for a म् — **इदमो मकारस्य\n'
        "  मकारवचनं त्यदाद्यत्वबाधनार्थम्**, stated only to keep 7.2.102's अ\n"
        '  out'
    ),
)

register(
    '7.2.109',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — दश्च — and its द् becomes म् before a case ending: **इमौ,\n'
        '  इमे; इमम्, इमौ, इमान्**. The च carries इदमः down from the sūtra\n'
        '  before while leaving its सौ behind, so this one reaches every\n'
        '  ending and that one only the nominative singular'
    ),
)

register(
    '7.2.110',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — यः सौ — but before सु the द् becomes य्: **इयम्**. And it\n'
        '  is the FEMININE that keeps it, the sūtra after this one naming the\n'
        '  masculine — **उत्तरसूत्रे पुंसीति वचनात् स्त्रियामयं यकारः**'
    ),
)

register(
    '7.2.111',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — इदोऽय् पुंसि — and in the MASCULINE the इद् of इदम्\n'
        '  becomes अय् before सु: **अयं ब्राह्मणः**. Two sūtras for one\n'
        "  ending, divided by gender, and it is this one's पुंसि that tells\n"
        '  the reader the य् of the sūtra before belongs to the feminine —\n'
        '  **उत्तरसूत्रे पुंसीति वचनात् स्त्रियामयं यकारः**'
    ),
)

register(
    '7.2.112',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — अनाप्यकः — the इद् of इदम् becomes अन् before the आप्\n'
        '  endings, unless a क stands in it: **अनेन, अनयोः**. **आपीति\n'
        '  प्रत्याहारः तृतीयैकवचनात् प्रभृति सुपः पकारेण** — a प्रत्याहार\n'
        '  made on the spot, from the instrumental singular to the last\n'
        '  ending'
    ),
)

register(
    '7.2.113',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — हलि लोपः — and it is dropped before a consonant-initial\n'
        '  case ending: **आभ्याम्, एभिः, एभ्यः, एषाम्, एषु**.\n'
        '\n'
        'SETTLED — **AND WHETHER THE WHOLE इद् GOES OR ONLY ITS इ IS ANSWERED\n'
        '  TWO WAYS.** **नानर्थकेऽलोन्त्यविधिः इति सर्वस्यायम् इद्रूपस्य\n'
        '  लोपः** — the maxim about a meaningless string makes it the whole;\n'
        '  **अथ वा नायम् इल्लोपः। अनाप्यकः इत्यन्ग्रहणम् अनुवर्तते**, or else\n'
        '  the अन् of the sūtra before is carried down and there is nothing\n'
        '  to argue about. This closes the विभक्ति heading'
    ),
)


register(
    '7.2.114',
    reuses=('1.1.1', '1.1.3', '1.1.4'),
    apply=mrjer_vrddhi,
    codification=(
        'mrjer_vrddhi(stem, dhatu=...) -> the stem after vṛddhi, and the '
        'rules that decided each part of it.'
    ),
    related=('1.1.1', '1.1.3', '1.1.50', '1.1.51'),
    notes=(
        'SETTLED — मृजेरङ्गस्य इको वृद्धिर्भवति: मार्ष्टा, मार्ष्टुम्,\n'
        '  मार्ष्टव्यम्.\n'
        '\n'
        'SETTLED — and the limit, which the Kāśikā states as a general\n'
        '  principle rather than a fact about this rule: मृजेरिति\n'
        '  धातुग्रहणम् इदम्, धातोश्च कार्यम् उच्यमानं धातुप्रत्यय एव\n'
        '  वेदितव्यम्. The sūtra names a *root*, so what it reaches is what\n'
        '  is built on मृज् as a root. कंसपरिमृड्भ्याम् and कंसपरिमृड्भिः\n'
        '  are nouns and are untouched. Codified as the `dhatu` condition.\n'
        '\n'
        'SETTLED — worth having beside 7.3.84 because it exercises a rule\n'
        '  that guṇa of इ never reaches: the vṛddhi of ऋ is ār, and it is\n'
        '  two steps, not one. 1.1.50 gives आ as the nearest of आ, ऐ, औ to\n'
        '  ऋ, and then 1.1.51 उरण् रपरः adds the र्. The verdict names both,\n'
        '  so the ār is visible as something derived rather than looked up.'
    ),
)




_VRDDHI_BEFORE = (
    'vrddhi_before(before, gana=..., part=..., taddhita=...) -> '
    'which vowel of the stem takes vrddhi, by rule of '
    '7.2.115-118.'
)

register(
    '7.2.115',
    apply=vrddhi_before,
    codification=_VRDDHI_BEFORE,
    notes=(
        'SETTLED — अचो ञ्णिति — a vowel-final stem takes vṛddhi before a ञित्\n'
        '  or णित् affix: **कारः, हारः** and **एकस्तण्डुलनिश्चायः** for the\n'
        '  ञित्; **गौः, गावौ, गावः; सखायौ, सखायः; जैत्रम्, यौत्रम्,\n'
        '  च्यौत्नः** for the णित्. This and the two after it are why so much\n'
        '  Sanskrit derivation begins with a strengthened vowel'
    ),
)

register(
    '7.2.116',
    apply=vrddhi_before,
    codification=_VRDDHI_BEFORE,
    notes=(
        'SETTLED — अत उपधायाः — and an अ in the PENULT: **पाकः, त्यागः, यागः;\n'
        '  पाचयति, पाचकः; पाठयति, पाठकः**. Both halves of the condition are\n'
        '  tested by the vṛtti, and each has its own counter-example'
    ),
)

register(
    '7.2.117',
    apply=vrddhi_before,
    codification=_VRDDHI_BEFORE,
    notes=(
        'SETTLED — तद्धितेष्वचामादेः — but in a TADDHITA it is the FIRST\n'
        '  vowel of the stem that takes it, wherever it stands: **गार्ग्यः,\n'
        '  वात्स्यः, दाक्षिः, प्लाक्षिः** for the ञित्; **औपगवः, कापटवः** for\n'
        '  the णित्.\n'
        '\n'
        'SETTLED — **AND IT DISPLACES BOTH THE RULES BEFORE IT.**\n'
        '  **त्वाष्ट्रः, जागत इत्यत्राचामादेर् वृद्धिर् अन्त्योपधालक्षणां\n'
        '  वृद्धिं बाधते** — त्वष्टृ would have strengthened its ऋ and जगत्\n'
        '  its penult; the first vowel wins in both. Which is why a\n'
        '  patronymic looks the way it does'
    ),
)

register(
    '7.2.118',
    apply=vrddhi_before,
    codification=_VRDDHI_BEFORE,
    notes=(
        'SETTLED — किति च — and before a कित् taddhita: **नाडायनः, चारायणः**\n'
        "  from 4.1.99's फक्; **आक्षिकः, शालाकिकः** from 4.4.1's ठक्.\n"
        '\n'
        'SETTLED — **AND THE कित् MARKING IS WHAT MAKES THE SŪTRA\n'
        "  NECESSARY.** 1.1.5's क्ङिति refuses a guṇa-or-vṛddhi conditioned\n"
        '  on an इक्, and both these affixes are marked कित् for other\n'
        '  reasons. Stating the vṛddhi here, on the FIRST vowel and not on an\n'
        "  इक्, puts it out of that rule's reach. This closes पाद ७.२: **इति\n"
        '  श्रीवामनविरचितायां काशिकायां वृत्तौ सप्तमाध्यायस्य द्वितीयः पादः**'
    ),
)


__all__ = [
    'before_ending',
    'mrjer_vrddhi',
    'no_it',
    'the_it',
    'vrddhi',
    'vrddhi_before',
]
