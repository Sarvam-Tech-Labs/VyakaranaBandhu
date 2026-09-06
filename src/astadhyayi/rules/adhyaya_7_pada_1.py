# -*- coding: utf-8 -*-
"""अध्याय ७, पाद १ — what the affix and the case ending become."""

from __future__ import annotations

from src.astadhyayi.anga import jho_antah
from src.astadhyayi.pratyaya_adesa import becomes
from src.astadhyayi.chandasi_adesa import in_the_veda
from src.astadhyayi.num_agama import num
from src.astadhyayi.sup_adesa import case_ending
from src.astadhyayi.sarvanamasthana import strong_stem
from src.astadhyayi.sut_nut import takes
from src.astadhyayi.sources import register


_BECOMES = (
    'becomes(affix, after=..., root=..., pada=..., chandasi=...) '
    '-> what the affix itself is replaced by, and by which rule '
    'of 7.1.1-8.'
)

register(
    '7.1.1',
    apply=becomes,
    codification=_BECOMES,
    notes=(
        'SETTLED — युवोरनाकौ — यु becomes अन and वु becomes अक, one to one:\n'
        '  **नन्दनः, रमणः** from ल्यु; **सायंतनः, चिरंतनः** from ट्युट्;\n'
        '  **कारकः, हारकः** from ण्वुल्; **वासुदेवकः, अर्जुनकः** from वुन्.\n'
        '\n'
        'SETTLED — **AND THE यु MEANT IS ONE NO WRITING SHOWS.**\n'
        '  **अनुनासिकयणोः प्रत्यययोर्ग्रहणम्** — the semivowel must be NASAL,\n'
        "  and **प्रतिज्ञानुनासिक्याः पाणिनीयाः**, the Pāṇinīyas' nasality is\n"
        "  by declaration and not by any mark. So ऊर्णायुः from 5.2.123's\n"
        '  युस् and भुज्युः from the Uṇādi युक् are untouched: **एवमादीनां हि\n'
        '  यणोऽनुनासिकत्वं न प्रतिज्ञायते**.\n'
        '\n'
        "SETTLED — **AND THE SŪTRA'S OWN WORD IS ARGUED OVER.** युवोः is a\n"
        '  dual, and the vṛtti walks through what follows if the dvandva is\n'
        '  taken as one thing or as two — **द्वित्वे यण् तु प्रसज्यते**, and\n'
        '  **अथ चेद् एकवद्भावः कथं पुंवद् भवेद् अयम्**. The verse ends\n'
        '  **द्वित्वे नैगमिको लोप एकत्वे नुमनित्यता** — either reading costs\n'
        '  something, and the vṛtti says which'
    ),
)

register(
    '7.1.2',
    apply=becomes,
    codification=_BECOMES,
    notes=(
        'SETTLED — आयनेयीनीयियः फढखच्छघां प्रत्ययादीनाम् — five sounds at the\n'
        '  HEAD of an affix, five substitutes, one to one: फ → आयन् in\n'
        '  **नाडायनः, चारायणः**; ढ → एय् in **सौपर्णेयः, वैनतेयः**; ख → ईन्\n'
        '  in **आढ्यकुलीनः**; छ → ईय् in **गार्गीयः, वात्सीयः**; घ → इय् in\n'
        '  **क्षत्रियः**.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTION HAPPENS WHILE THE AFFIX IS STILL\n'
        '  BEING TAUGHT.** **एत आयन्नादयः प्रत्ययोपदेशकाल एव भवन्ति** — not\n'
        "  when the word is built. That is what makes 4.4.117's घच् worth its\n"
        "  च् marker: the accent falls on the substitute's first vowel, which\n"
        '  would not exist yet if the change came later. And शङ्खः and षण्ढः\n'
        '  keep their sounds because **उणादयो बहुलम्**'
    ),
)

register(
    '7.1.4',
    apply=becomes,
    codification=_BECOMES,
    notes=(
        'SETTLED — अदभ्यस्तात् — after a REDUPLICATED stem the झ becomes अत्\n'
        '  and not अन्त्: **ददति, ददतु; दधति, दधतु; जक्षति, जक्षतु; जाग्रति,\n'
        '  जाग्रतु**. **अन्तादेशापवादोऽयम्** — an exception to 7.1.3 —\n'
        "  **जुसादेशेन तु बाध्यते**, and is itself set aside where 3.4.109's\n"
        '  जुस् has already taken the झ'
    ),
)

register(
    '7.1.5',
    apply=becomes,
    codification=_BECOMES,
    notes=(
        'SETTLED — आत्मनेपदेष्वनतः — and in the आत्मनेपद the झ becomes अत्\n'
        '  after a stem that does NOT end in अ: **चिन्वते, चिन्वताम्,\n'
        '  अचिन्वत; पुनते, लुनते, अलुनत**.\n'
        '\n'
        'SETTLED — **AND THE अनत् QUALIFIES THE STEM, NOT THE झ.**\n'
        '  **अनकारान्तेनाङ्गेन झकारविशेषणं किम्? इह मा भूत् — शयान्तै** —\n'
        '  read the other way the Vedic शयान्तै would lose its अन्त्. The\n'
        '  vṛtti also notes that the विकरण is put in first, being नित्य, so\n'
        '  7.1.3 has already had its chance'
    ),
)

register(
    '7.1.6',
    apply=becomes,
    codification=_BECOMES,
    notes=(
        'SETTLED — शीङो रुट् — after शीङ् the झ-substitute takes the augment\n'
        '  रुट् at its head: **शेरते, शेरताम्, अशेरत**.\n'
        '\n'
        'SETTLED — **AND IT IS AN AUGMENT TO THE SUBSTITUTE AND NOT TO THE\n'
        '  झ.** **स यदि झकारस्यैव स्यात् अदादेशो न स्यात्** — attached to the\n'
        "  झ itself it would have blocked 7.1.5's अत्, and शेरते needs both.\n"
        '  The sūtra names शीङ् with its ङ् — **सानुबन्धग्रहणम्\n'
        '  अयङ्लुगर्थम्**'
    ),
)

register(
    '7.1.7',
    apply=becomes,
    codification=_BECOMES,
    notes=(
        'SETTLED — वेत्तेर्विभाषा — and after विद् the रुट् is optional:\n'
        '  **संविदते, संविद्रते; संविदताम्, संविद्रताम्; समविदत, समविद्रत**.\n'
        '  **वेत्तेरिति लुग्विकरणस्य ग्रहणम्** — the विद् meant is the one\n'
        '  whose विकरण is elided, which is why विन्ते is out'
    ),
)

register(
    '7.1.8',
    apply=becomes,
    codification=_BECOMES,
    notes=(
        'SETTLED — बहुलं छन्दसि — and in the Veda the रुट् is बहुलम्: **देवा\n'
        '  अदुह्र, गन्धर्वाप्सरसो अदुह्र**, where the झ has become अत् and\n'
        '  then taken रुट्, and 7.1.41 drops the त्.\n'
        '\n'
        'SETTLED — **AND बहुलम् CUTS BOTH WAYS, WHICH IS THE POINT OF THE\n'
        '  WORD.** It reaches where no rule would have put it — **अदृश्रमस्य\n'
        "  केतवः** — and it lets 7.4.16's guṇa fail in the same form:\n"
        '  **ऋदृशोऽङि गुणः इत्येतदपि बहुलवचनादेवात्र न भवति**. One word\n'
        '  licensing both directions at once'
    ),
)


_CASE_ENDING = (
    'case_ending(ending, after=..., stem=..., case=..., '
    'chandasi=...) -> what the case ending becomes, or that it '
    'is dropped, by rule of 7.1.9-33.'
)

register(
    '7.1.9',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — अतो भिस ऐस् — after an अ-final stem भिस् becomes ऐस्:\n'
        '  **वृक्षैः, प्लक्षैः, अतिजरसैः**.\n'
        '\n'
        'SETTLED — **AND ONE OF ITS EXAMPLES IS THERE TO BREAK A PARIBHĀṢĀ.**\n'
        "  अतिजरसैः has जरा shortened to जरस् by 6.4.4's क्रम, so the अ the\n"
        '  rule needs was made by the very compound that would then destroy\n'
        '  it. **संनिपातलक्षणो विधिरनिमित्तं तद्विघातस्य इति परिभाषेयम्\n'
        "  अनित्या** — the maxim is not universal, and 3.1.14's **कष्टाय\n"
        '  क्रमणे** is where Pāṇini shows it. A verse settles the order\n'
        '  against एत्व: **कृतेऽप्येत्वे भौतपूर्व्याद् ऐस् तु नित्यस्तथा\n'
        '  सति**.\n'
        '\n'
        'SETTLED — **AND ITS अतः IS A HEADING.** **अत इत्यधिकारो जसः शी इति\n'
        '  यावत्** — every rule to 7.1.17 wants an अ-final stem'
    ),
)

register(
    '7.1.10',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — बहुलं छन्दसि — and in the Veda the ऐस् is बहुलम्, so it\n'
        '  reaches what 7.1.9 could not and fails where 7.1.9 would have\n'
        '  held: **अत इत्युक्तम् अनतोऽपि भवति नद्यैः इति। अतो न भवति —\n'
        '  देवेभिः सर्वेभिः प्रोक्तम्**. Both halves of बहुलम् shown in one\n'
        '  line'
    ),
)

register(
    '7.1.11',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — नेदमदसोरकोः — but इदम् and अदस् do NOT take ऐस्, unless a\n'
        '  क stands in them: **एभिः, अमीभिः**.\n'
        '\n'
        'SETTLED — **AND THE अकोः IS ITSELF A ज्ञापक.** **अकोरित्येतद् एव\n'
        '  प्रतिषेधवचनं ज्ञापकं तन्मध्यपतितस्तद्ग्रहणेन गृह्यते इति** — a\n'
        '  word with something inserted in the middle is still that word,\n'
        '  which is why the sūtra has to say *without a क* at all. Stated as\n'
        '  a प्रतिषेध rather than as a नियम **इदमदसोः कादिति**, because a\n'
        '  नियम could be read backwards and would then lose सर्वकैः'
    ),
)

register(
    '7.1.12',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — टाङसिङसामिनात्स्याः — after an अ-final stem टा ङसि ङस्\n'
        '  become इन आत् स्य, one to one: **वृक्षेण, प्लक्षेण; वृक्षात्,\n'
        "  प्लक्षात्; वृक्षस्य, प्लक्षस्य**. And where 7.1.9's अतिजरसैः went\n"
        '  through, अतिजरसिना is not settled — **अतिजरसिन अतिजरसाद् इति\n'
        '  केचिद् इच्छन्ति। यथा तु भाष्ये तथा नैतद् इष्यते**'
    ),
)

register(
    '7.1.13',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — ङेर्यः — and ङे, the dative singular, becomes य:\n'
        "  **वृक्षाय, प्लक्षाय**. The lengthening in वृक्षाय is 7.3.102's,\n"
        '  and it happens although the य that conditions it is the very thing\n'
        '  the अ made possible — **संनिपातलक्षणो विधिः० इति परिभाषेयम्\n'
        '  अनित्या, तेन दीर्घो भवति**, the same maxim 7.1.9 had to break'
    ),
)

register(
    '7.1.14',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — सर्वनाम्नः स्मै — after an अ-final PRONOUN the ङे becomes\n'
        '  स्मै instead: **सर्वस्मै, विश्वस्मै, यस्मै, तस्मै, कस्मै**.\n'
        '\n'
        "SETTLED — **AND IT HAS TO BE DONE BEFORE 2.4.32's अश्.** In\n"
        '  अथोऽत्रास्मै the अन्वादेश would give एकादेश first and the स्मै\n'
        '  would never be reached; **अन्तरङ्गत्वाद् एकादेशात् पूर्वं स्मैभावः\n'
        '  क्रियते, पश्चाद् एकादेशः** — the inner operation goes in first'
    ),
)

register(
    '7.1.15',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — ङसिङ्योः स्मात्स्मिनौ — and ङसि and ङि become स्मात् and\n'
        '  स्मिन्, one to one: **सर्वस्मात्, यस्मात्, कस्मात्; सर्वस्मिन्,\n'
        '  यस्मिन्, अन्यस्मिन्**'
    ),
)

register(
    '7.1.16',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — पूर्वादिभ्यो नवभ्यो वा — but after NINE of the pronouns\n'
        '  the स्मात् and स्मिन् are optional, and the ordinary ending stands\n'
        '  beside them: **पूर्वस्मात्, पूर्वात्; पूर्वस्मिन्, पूर्वे;\n'
        '  परस्मात्, परात्; स्वस्मात्, स्वात्; अन्तरस्मात्, अन्तरात्**. The\n'
        '  vṛtti gives both forms of all nine and then asks **नवभ्य इति\n'
        '  किम्?** — त्यस्मात्, which is not one of them'
    ),
)

register(
    '7.1.17',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — जसः शी — and जस् becomes शी: **सर्वे, विश्वे, ये, के,\n'
        '  ते**. The ई is written long for the sūtra that follows and not for\n'
        '  this one — **दीर्घोच्चारणम् उत्तरार्थम्**, which is how त्रपुणी\n'
        '  and जतुनी come out'
    ),
)

register(
    '7.1.18',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — औङ आपः — after an आप्-final stem the dual औङ् becomes शी:\n'
        '  **खट्वे तिष्ठतः, खट्वे पश्य, बहुराजे, कारीषगन्ध्ये**.\n'
        '\n'
        'SETTLED — **AND TWO VERSES ARGUE ABOUT ITS ङ्.** **ङकारः\n'
        '  सामान्यग्रहणार्थः, औटोऽपि ग्रहणं यथा स्यात्** — the marker is\n'
        '  there so that औट् is caught too. The objection: a ङित् substitute\n'
        '  would then bring ङित् effects with it. The answer: **ङित्त्वे\n'
        '  विद्याद् वर्णनिर्देशमात्रं** — here the ङ् only identifies a\n'
        '  sound, and a sound-naming ङ् carries nothing'
    ),
)

register(
    '7.1.19',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — नपुंसकाच्च — and after a NEUTER stem: **कुण्डे तिष्ठतः,\n'
        '  कुण्डे पश्य; दधिनी, मधुनी; त्रपुणी, जतुनी**. The शी would have\n'
        "  triggered 6.4.148's इ-loss, and a vārttika stops it — **श्यां\n"
        '  प्रतिषेधो वक्तव्यः**'
    ),
)

register(
    '7.1.20',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — जश्शसोः शिः — after a neuter stem जस् and शस् become शि:\n'
        '  **कुण्डानि तिष्ठन्ति, कुण्डानि पश्य; दधीनि, मधूनि; त्रपूणि,\n'
        '  जतूनि**. And the शस् meant is the one that keeps company with जस्\n'
        '  — **जसा सहचरितस्य शसो ग्रहणात्**, so the taddhita शस् is out'
    ),
)

register(
    '7.1.21',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — अष्टाभ्य औश् — अष्टा takes औश् for जस् and शस्: **अष्टौ\n'
        '  तिष्ठन्ति, अष्टौ पश्य**. And the अष्टन् meant is the one that has\n'
        '  ALREADY taken its आ — **कृताकारोऽष्टन्शब्दो गृह्यते** — which the\n'
        "  vṛtti then reads back as a ज्ञापक that 7.2.84's आ is optional at\n"
        '  all.\n'
        '\n'
        'SETTLED — **AND IT DISPLACES ONE RULE AND NOT THE OTHER.** **षड्भ्यो\n'
        '  लुक् इत्यस्यायम् अपवादः, नाप्राप्ते तस्मिन् इदम् आरभ्यते** —\n'
        "  7.1.22 is set aside. But 2.4.71's सुप् elision is not, **तस्मिन्\n"
        '  प्राप्ते चाप्राप्ते च**, and so अष्टपुत्रः stands'
    ),
)

register(
    '7.1.22',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — षड्भ्यो लुक् — after a षट्-named numeral जस् and शस् are\n'
        '  simply dropped: **षट् तिष्ठन्ति, षट् पश्य; पञ्च, सप्त, नव, दश**.\n'
        '  And it reaches a compound that ENDS in one — **षट्प्रधानात्\n'
        '  तदन्तादपि भवति। परमषट्, उत्तमषट्**'
    ),
)

register(
    '7.1.23',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — स्वमोर्नपुंसकात् — after a neuter stem सु and अम् are\n'
        '  dropped: **दधि तिष्ठति, दधि पश्य; मधु; त्रपु; जतु**.\n'
        '\n'
        "SETTLED — **AND THE LOSS BEATS 7.2.102's त्यदादि SUBSTITUTION IN तद्\n"
        '  ब्राह्मणकुलम्.** The reason given is not order but strength:\n'
        '  **लुको हि निमित्तम् अतोऽम् इति लक्षणान्तरेण विहन्यते, न पुनस्\n'
        '  त्यदाद्यत्वेनैव** — and **यस्य च लक्षणान्तरेण निमित्तं विहन्यते न\n'
        '  तद् अनित्यं भवति**'
    ),
)

register(
    '7.1.24',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — अतोऽम् — but after an अ-final neuter they become अम्\n'
        '  instead of going: **कुण्डं तिष्ठति, कुण्डं पश्य; वनम्, पीठम्**.\n'
        '  And it is अम् and not a bare म् for a reason the vṛtti gives in\n'
        '  four words — **दीर्घत्वं प्राप्नोति**, 7.3.102 would have\n'
        '  lengthened the stem before a consonant-initial ending'
    ),
)

register(
    '7.1.25',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — अद्ड् डतरादिभ्यः पञ्चभ्यः — and after five of the pronouns\n'
        '  they become अद्ड्: **कतरत्, कतमत्, इतरत्, अन्यतरत्, अन्यत्**.\n'
        '\n'
        'SETTLED — **AND THE ड् IS THERE TO STOP TWO DIFFERENT THINGS.**\n'
        '  **डित्करणं किम्? कतरत् तिष्ठतीत्यत्र पूर्वसवर्णदीर्घो मा भूत्** —\n'
        '  and asked why a plain त् substitute would not do, the vṛtti\n'
        '  answers **हे कतरद् इति संबुद्धेर्लोपो मा भूत्**. A verse sums\n'
        '  both: **अद्ड्डित्त्वाड् डतरादीनां न लोपो नापि दीर्घता**'
    ),
)

register(
    '7.1.26',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — नेतराच्छन्दसि — but इतर does not take the अद्ड् in the\n'
        '  Veda: **मृतम् इतरम् आण्डम् अवापद्यत; वार्त्रघ्नम् इतरम्**.\n'
        '\n'
        'SETTLED — **AND IT IS PUT AS A REFUSAL RATHER THAN JOINED TO THE\n'
        '  RULE BEFORE, FOR THE SAKE OF ONE WORD.** **अतोऽम् इत्यस्माद्\n'
        '  अनन्तरम् इतराच्छन्दसि इति वक्तव्ये नेतराच्छन्दसि इति वचनं\n'
        '  योगविभागार्थम्। एकतराद् धि सर्वत्र छन्दसि भाषायां प्रतिषेध\n'
        '  इष्यते** — एकतरम् is refused everywhere, and only a split sūtra\n'
        '  can say so'
    ),
)

register(
    '7.1.27',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — युष्मदस्मद्भ्यां ङसोऽश् — after युष्मद् and अस्मद् the\n'
        '  genitive singular becomes अश्: **तव स्वम्, मम स्वम्**. The श्\n'
        '  makes it replace the whole ending and not its first sound —\n'
        "  **शित्करणं सर्वादेशार्थम्** — and if it did not, 7.2.89's योऽचि\n"
        '  would not be reached'
    ),
)

register(
    '7.1.28',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — ङे प्रथमयोरम् — and ङे, the nominative and the accusative\n'
        '  all become अम्: **तुभ्यं दीयते, मह्यं दीयते; त्वम्, अहम्, युवाम्,\n'
        '  आवाम्, यूयम्, वयम्; त्वाम्, माम्**. **ङे इत्यविभक्तिकोऽयं\n'
        '  निर्देशः** — the ङे in the sūtra carries no case ending of its\n'
        '  own, which is how one word can name both an ending and two whole\n'
        '  विभक्तिs'
    ),
)

register(
    '7.1.29',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — शसो न — the accusative plural becomes न: **युष्मान्\n'
        '  ब्राह्मणान्, युष्मान् ब्राह्मणीः, अस्मान् ब्राह्मणीः, युष्मान्\n'
        '  कुलानि, अस्मान् कुलानि** — the same form whatever the gender of\n'
        '  what it stands beside'
    ),
)

register(
    '7.1.30',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — भ्यसो भ्यम् — भ्यस् becomes भ्यम्: **युष्मभ्यं दीयते,\n'
        '  अस्मभ्यं दीयते**.\n'
        '\n'
        "SETTLED — **AND A PARIBHĀṢĀ SAVES IT FROM 7.3.103's ए.** After the\n"
        "  substitution and 7.2.90's loss the stem ends before a झल्, and\n"
        '  बहुवचने झल्येत् would give *युष्मेभ्यम्. **अङ्गवृत्ते\n'
        '  पुनर्वृत्ताव् अविधिर् निष्ठितस्य** — a stem already finished with\n'
        '  is not operated on again. Some read the substitute as अभ्यम् to\n'
        '  reach the same end, and the vṛtti says which readings need which'
    ),
)

register(
    '7.1.31',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — पञ्चम्या अत् — and the ABLATIVE भ्यस् becomes अत्:\n'
        '  **युष्मद् गच्छन्ति, अस्मद् गच्छन्ति**. The same ending twice over,\n'
        '  once as a dative and once as an ablative, and the two go different\n'
        '  ways'
    ),
)

register(
    '7.1.32',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — एकवचनस्य च — and so does the ablative SINGULAR: **त्वद्\n'
        '  गच्छन्ति, मद् गच्छन्ति**. Two words, and everything else is\n'
        '  carried over: the अत् and the पञ्चमी from 7.1.31, and\n'
        '  युष्मदस्मद्भ्याम् from 7.1.27, four sūtras back. The shortest rule\n'
        '  of the block, and the one that shows how much anuvṛtti the run is\n'
        '  carrying by the time it ends'
    ),
)

register(
    '7.1.33',
    apply=case_ending,
    codification=_CASE_ENDING,
    notes=(
        'SETTLED — साम आकम् — the genitive plural becomes आकम्: **युष्माकम्,\n'
        '  अस्माकम्**.\n'
        '\n'
        'SETTLED — **AND THE ENDING IS NAMED WITH AN AUGMENT IT HAS NOT GOT\n'
        "  YET.** साम् is आम् with 7.1.52's सुट् in it, and the vṛtti asks\n"
        '  the obvious question — **न ह्यादेशविधानकाले सुड् विद्यते?** The\n'
        '  answer is that naming it so is what STOPS the सुट् coming later:\n'
        '  **तस्यैव तु भाविनः सुटो निवृत्त्यर्थम्**. Once आकम् is in, the\n'
        '  stem ends in अ and 7.1.52 would supply a second सुट्; the स् is\n'
        '  already inside the thing replaced, so it does not'
    ),
)


_IN_THE_VEDA = (
    'in_the_veda(what, root=..., after=..., before=..., '
    'sense=..., samasa=..., chandasi=...) -> what is supplied, '
    'and by which rule of 7.1.34-50.'
)

register(
    '7.1.34',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        "SETTLED — आत औ णलः — after an आ-final stem the perfect's णल् becomes\n"
        '  औ: **पपौ, तस्थौ, जग्लौ, मम्लौ**.\n'
        '\n'
        'SETTLED — **AND THE ORDER OF FOUR OPERATIONS IS SETTLED BY TWO\n'
        '  REASONS, NOT ONE.** **अत्रौत्वम् एकादेशः स्थानिवद्भावो द्विर्वचनम्\n'
        '  इत्यनेन क्रमेण कार्याणि क्रियन्ते** — the औ goes in first for\n'
        '  having nowhere else to apply, **अनवकाशत्वात्**, and the एकादेश\n'
        '  beats the reduplication for being later, **परत्वात्**'
    ),
)

register(
    '7.1.35',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — तुह्योस्तातङाशिष्यन्यतरस्याम् — तु and हि optionally\n'
        '  become तातङ् where a BLESSING is meant: **जीवताद् भवान्, जीवतात्\n'
        '  त्वम्** beside **जीवतु भवान्, जीव त्वम्**.\n'
        '\n'
        'SETTLED — **AND ITS ङ् DOES TWO JOBS AND IS ARGUED OVER FOR BOTH.**\n'
        '  **ङित्करणं गुणवृद्धिप्रतिषेधार्थम् इति सर्वादेशस्तातङ् भवति** —\n'
        "  the marker stops 1.1.5's strengthening, which shows the substitute\n"
        "  replaces the whole ending; and **ङित् च पिद् न भवति**, so 7.3.93's\n"
        '  ईट् does not come and ब्रूताद् भवान् stands. Two verses then ask\n'
        '  whether a ङित् can be an अन्त्यविधि at all: **तातङो\n'
        '  ङित्त्वसामर्थ्याद् नायम् अन्त्यविधिः स्मृतः**'
    ),
)

register(
    '7.1.36',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — विदेः शतुर्वसुः — after विद् the शतृ becomes वसु:\n'
        '  **विद्वान्, विद्वांसौ, विद्वांसः**.\n'
        '\n'
        'SETTLED — **AND ITS उ IS THERE FOR A RULE THREE PĀDAS BACK.**\n'
        '  **स्थानिवद्भावाद् उगित्कार्ये सिद्धे वसोर् उकारकरणं वसोः\n'
        '  संप्रसारणम् इत्यत्र क्वसोरपि सामान्यग्रहणार्थम्** — the substitute\n'
        '  could have been वस्, and is वसु so that 6.4.131 may catch क्वसु as\n'
        '  well. And **एकानुबन्धकग्रहणे न द्व्यनुबन्धकस्य** is set aside\n'
        '  here, or the उ would be pointless. Some read अन्यतरस्याम् in:\n'
        '  **विदन्, विदन्तौ, विदन्तः**'
    ),
)

register(
    '7.1.37',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — समासेऽनञ्पूर्वे क्त्वो ल्यप् — in a compound whose first\n'
        '  member is not नञ्, क्त्वा becomes ल्यप्: **प्रकृत्य, प्रहृत्य,\n'
        '  पार्श्वतःकृत्य, नानाकृत्य, द्विधाकृत्य**.\n'
        '\n'
        'SETTLED — **AND अनञ् MEANS MORE THAN नञ्.** **अनञ् इति नञोऽन्यद्\n'
        '  अनञ् नञ्सदृशम् अव्ययं परिगृह्यते** — an indeclinable LIKE नञ्,\n'
        '  which is how परमकृत्वा and उत्तमकृत्वा are kept out too, though\n'
        '  neither has a नञ् in it. And स्नात्वाकालकः keeps its क्त्वा by\n'
        "  2.1.72's निपातन"
    ),
)

register(
    '7.1.38',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — क्त्वाऽपि छन्दसि — but in the Veda the क्त्वा may STAY:\n'
        '  **कृष्णं वासो यजमानं परिधापयित्वा; प्रत्यञ्चम् अर्कं\n'
        '  प्रत्यर्पयित्वा** — and the अपि lets ल्यप् stand too, **उद्धृत्य\n'
        '  जुहुयात्**.\n'
        '\n'
        'SETTLED — **AND IT IS NOT PUT AS वा FOR A REASON.** **वा छन्दसीति\n'
        '  नोक्तं सर्वोपाधिव्यभिचारार्थम्** — said as an option it would have\n'
        '  varied only the one thing; said so, every condition of 7.1.37 may\n'
        '  lapse, and the ल्यप् reaches a NON-compound: **अर्च्य तान् देवान्\n'
        '  गतः**.\n'
        '\n'
        'SETTLED — **AND THE छन्दस् HEADING BEGINS HERE.** **छन्दोऽधिकार\n'
        '  आज्जसेरसुक् इति यावत्** — thirteen sūtras, ending at 7.1.50'
    ),
)

register(
    '7.1.39',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — सुपां सुलुक्पूर्वसवर्णाऽऽच्छेयाडाड्यायाजालः — in the Veda\n'
        "  ANY case ending may be replaced by सु, लुक्, the preceding vowel's\n"
        '  own long, आ, आत्, शे, या, डा, ड्या, याच् or आल्: **ऋजवः सन्तु\n'
        '  पन्थाः** where पन्थानः was due; **लोहिते चर्मन्** for चर्मणि;\n'
        '  **धीती, मती, सुष्टुती** for धीत्या, मत्या, सुष्ट्युत्या.\n'
        '\n'
        'SETTLED — **AND TWO VĀRTTIKAS WIDEN IT PAST WHAT IT SAYS.** **सुपां\n'
        '  सुपो भवन्तीति वक्तव्यम्** — any nominal ending for any other,\n'
        '  **धुरि दक्षिणायाः** for दक्षिणायाम्; and **तिङां तिङो भवन्तीति\n'
        '  वक्तव्यम्** — any verbal ending for any other, **ये अश्वयूपाय\n'
        '  तक्षति** for तक्षन्ति. One sūtra and two vārttikas, and the whole\n'
        '  Vedic declension and conjugation are let off'
    ),
)

register(
    '7.1.40',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — अमो मश् — the मिप्-substitute अम् becomes मश् in the Veda:\n'
        '  **वधीं वृत्रम्; क्रमीं वृक्षस्य शाखाम्**. The श् makes it replace\n'
        '  the whole ending — **शित्करणं सर्वादेशार्थम्**, since a bare म्\n'
        "  for a म् could only have been about the anusvāra. And 6.4.75's\n"
        '  बहुलम् is why there is no अट् augment'
    ),
)

register(
    '7.1.41',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — लोपस्त आत्मनेपदेषु — in the Veda the त् of an आत्मनेपद\n'
        '  ending is dropped: **देवा अदुह्र** for अदुहत; **दुहाम् अश्विभ्यां\n'
        '  पयो अघ्न्येयम्** for दुग्धाम्; **दक्षिणतः पुमान् स्त्रियम् उपशये**\n'
        "  for शेते. This is what finishes 7.1.8's अदुह्र — the झ became अत्,\n"
        '  took रुट्, and now loses its त्'
    ),
)

register(
    '7.1.42',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — ध्वमो ध्वात् — ध्वम् becomes ध्वात् in the Veda:\n'
        '  **अन्तरेवोष्माणं वारयध्वात्**, where वारयध्वम् was due'
    ),
)

register(
    '7.1.43',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — यजध्वैनमिति च — यजध्वैनम् is laid down whole before एनम्:\n'
        '  **यजध्वैनं प्रियमेधाः**. Two things are निपातित at once —\n'
        '  **मकारलोपो निपात्यते वकारस्य च यकारः** — the म् goes and the व्\n'
        '  becomes य्, and यजध्वम् एनम् was what the grammar owed'
    ),
)

register(
    '7.1.44',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        "SETTLED — तस्य तात् — the imperative's second-person plural त\n"
        '  becomes तात् in the Veda: **गात्रं गात्रम् अस्यानूनं कृणुतात्;\n'
        '  ऊवध्यगोहं पार्थिवं खनतात्; अस्ना रक्षः संसृजतात्; सूर्यं\n'
        '  चक्षुर्गमयतात्** — four in one verse, and the vṛtti names what\n'
        '  each displaces'
    ),
)

register(
    '7.1.45',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — तप्तनप्तनथनाश्च — and the same त may become तप्, तनप्, तन\n'
        '  or थन: **शृणोत ग्रावाणः** and **सुनोता** for तप्; **सं वरत्रा\n'
        '  दधातन** for तनप्; **जुजुष्टन** for तन; **यदिष्ठन** for थन.\n'
        '  **पित्करणम् अङित्त्वार्थम्** — the प् markers are there only to\n'
        '  stop the substitutes counting as ङित्'
    ),
)

register(
    '7.1.46',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — इदन्तो मसि — मस् takes an इ and ends in it, in the Veda:\n'
        '  **पुनस्त्वोद् दीपयामसि; शलभान् भञ्जयामसि; त्वयि रात्रि वसामसि**.\n'
        '  The rule is put as *ending in इ* rather than as an augment — **मसः\n'
        '  सकारान्तस्य इकारागमो भवति, स च तस्यान्तो भवति। तद्ग्रहणेन गृह्यत\n'
        '  इत्यर्थः** — so that a rule naming मसि catches it'
    ),
)

register(
    '7.1.47',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — क्त्वो यक् — क्त्वा takes the augment यक् in the Veda:\n'
        '  **दत्त्वाय सविता धियः**, where दत्त्वा was due. And the vṛtti asks\n'
        '  why it is not put next to 7.1.38, which is also about क्त्वा:\n'
        '  **समास इति तत्रानुवर्तते** — the compound condition is carried\n'
        '  here from 7.1.37 and would have been lost'
    ),
)

register(
    '7.1.48',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — इष्ट्वीनमिति च — इष्ट्वीनम् is laid down whole:\n'
        '  **इष्ट्वीनं देवान्**, where इष्ट्वा देवान् was due. The ईनम्\n'
        '  replaces the last part of यज् + क्त्वा, and the च takes in more\n'
        '  than is said — **पीत्वीनम् इत्यपीष्यते।\n'
        '  चकारस्यानुक्तसमुच्चयार्थत्वात् सिद्धम्**'
    ),
)

register(
    '7.1.49',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — स्नात्व्यादयश्च — स्नात्वी and its like are laid down\n'
        '  whole: **स्नात्वी मलादिव; पीत्वी सोमस्य वावृधे**. And the आदि is\n'
        '  not a list but a kind — **प्रकारार्थोऽयम् आदिशब्दः**, so the class\n'
        '  is open'
    ),
)

register(
    '7.1.50',
    apply=in_the_veda,
    codification=_IN_THE_VEDA,
    notes=(
        'SETTLED — आज्जसेरसुक् — after an अ-final stem the जस् takes the\n'
        '  augment असुक् in the Veda: **ब्राह्मणासः पितरः सोम्यासः**, where\n'
        '  ब्राह्मणाः सोम्याः was due.\n'
        '\n'
        'SETTLED — **AND IT CLOSES THE छन्दस् HEADING.** The vṛtti had said\n'
        '  at 7.1.38 that the heading runs **आज्जसेरसुक् इति यावत्**, and\n'
        '  here it ends. It also settles one order on the way: in **ये\n'
        "  पूर्वासो य उपरासः** the असुक् might have let 7.1.17's शी apply\n"
        '  afresh, and **सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितम् एव** —\n'
        '  what was once set aside stays set aside'
    ),
)


_TAKES = (
    'takes(ending, stem=..., after=..., before=..., sense=..., '
    'chandasi=...) -> the augment the ending is given, and by '
    'which rule of 7.1.51-57.'
)

register(
    '7.1.51',
    apply=takes,
    codification=_TAKES,
    notes=(
        'SETTLED — अश्वक्षीरवृषलवणानामात्मप्रीतौ क्यचि — four stems take\n'
        '  असुक् before क्यच् where the wanting is for ONESELF: **अश्वस्यति\n'
        '  वडवा; क्षीरस्यति माणवकः; वृषस्यति गौः; लवणस्यत्युष्ट्रः**. And\n'
        '  छन्दसि has stopped governing here — **छन्दसीत्यतः प्रभृति\n'
        "  निवृत्तम्**, which is the vṛtti's own way of closing 7.1.38's\n"
        '  heading.\n'
        '\n'
        'SETTLED — **AND TWO VĀRTTIKAS SPLIT THE SENSE IN HALF.**\n'
        '  **अश्ववृषयोर्मैथुनेच्छायाम्** and **क्षीरलवणयोर्लालसायाम्** — the\n'
        '  mare and the cow want mating, the boy and the camel crave.\n'
        '  **तृष्णातिरेको लालसा**, and outside those two senses there is no\n'
        "  असुक् even where the wanting is one's own. A third opinion widens\n"
        '  it to every stem, and a fourth offers सुक् instead: **दधिस्यति,\n'
        '  मधुस्यति**'
    ),
)

register(
    '7.1.52',
    apply=takes,
    codification=_TAKES,
    notes=(
        'SETTLED — आमि सर्वनाम्नः सुट् — after an अ-final PRONOUN the\n'
        '  genitive plural आम् takes सुट्: **सर्वेषाम्, विश्वेषाम्, येषाम्,\n'
        '  तेषाम्; सर्वासाम्, यासाम्, तासाम्**.\n'
        '\n'
        'SETTLED — **AND THREE OTHER आम्s HAD TO BE RULED OUT.** The आम्\n'
        "  meant is the genitive plural — not 7.3.116's ङेराम्, which is\n"
        "  later and so takes आङ् आट् स्याट् first; not 5.4.11's\n"
        "  किमेत्तिङव्ययघादामु; not 3.1.35's आम् of the periphrastic perfect.\n"
        '  **न तौ सर्वनाम्नः स्तः। सानुबन्धकाविति वा तौ न गृह्येते** — either\n'
        '  they cannot follow a pronoun at all, or a paribhāṣā keeps a marked\n'
        '  affix out'
    ),
)

register(
    '7.1.53',
    apply=takes,
    codification=_TAKES,
    notes=(
        'SETTLED — त्रेस्त्रयः — त्रि becomes त्रय before आम्: **त्रयाणाम्**.\n'
        '  Not an augment but a whole new stem, and the only rule of the\n'
        '  seven that is. The Veda keeps another form beside it —\n'
        '  **त्रीवामित्यपि छन्दसीष्यते। त्रीणामपि समुद्राणाम्**'
    ),
)

register(
    '7.1.54',
    apply=takes,
    codification=_TAKES,
    notes=(
        'SETTLED — ह्रस्वनद्यापो नुट् — after a stem ending in a SHORT vowel,\n'
        '  or in a नदी, or in आप्, the आम् takes नुट्: **वृक्षाणाम्,\n'
        '  अग्नीनाम्, कर्तृणाम्** for the short vowel; **कुमारीणाम्,\n'
        '  गौरीणाम्, लक्ष्मीणाम्, ब्रह्मबन्धूनाम्** for the नदी; **खट्वानाम्,\n'
        '  मालानाम्, कारीषगन्ध्यानाम्** for the आप्. Three conditions, and\n'
        '  the vṛtti works every one of them'
    ),
)

register(
    '7.1.55',
    apply=takes,
    codification=_TAKES,
    notes=(
        'SETTLED — षट्चतुर्भ्यश्च — and after a षट्-named numeral and after\n'
        '  चतुर्: **षण्णाम्, पञ्चानाम्, सप्तानाम्, नवानाम्, दशानाम्;\n'
        '  चतुर्णाम्**.\n'
        '\n'
        'SETTLED — **AND चतुर् IS NAMED APART BECAUSE IT IS NOT A षट्.**\n'
        '  **रेफान्तायाः संख्यायाः षट्संज्ञा न विहिता, षड्भ्यो लुक् इति लुग्\n'
        '  मा भूत्** — a र्-final numeral was kept out of the षट् name on\n'
        '  purpose, or 7.1.22 would have dropped its जस्. So it has to be\n'
        '  brought back in by name here. And the plural in the sūtra shows\n'
        "  the numeral must be the compound's head: **परमषण्णाम्,\n"
        '  परमचतुर्णाम्**'
    ),
)

register(
    '7.1.56',
    apply=takes,
    codification=_TAKES,
    notes=(
        'SETTLED — श्रीग्रामण्योश्छन्दसि — and श्री and ग्रामणी take it in\n'
        '  the Veda: **श्रीणाम् उदारो धरुणो रयीणाम्; अपि तत्र\n'
        '  सूतग्रामणीनाम्**.\n'
        '\n'
        'SETTLED — **AND EACH OF THE TWO IS THERE FOR A DIFFERENT REASON.**\n'
        "  श्री is a नदी only optionally, by 1.4.5's वामि, so 7.1.54 would\n"
        '  have reached it only half the time — **तत्र नित्यार्थं वचनम्**.\n'
        '  सूतग्रामणीनाम् needs the rule only on one reading of the compound;\n'
        '  on the other, **ह्रस्वादित्येव सिद्धम्**'
    ),
)

register(
    '7.1.57',
    apply=takes,
    codification=_TAKES,
    notes=(
        'SETTLED — गोः पादान्ते — and गो takes it at the END OF A\n'
        '  VERSE-QUARTER: **विद्मा हि त्वा गोपतिं शूर गोनाम्**. The condition\n'
        '  is metrical and not grammatical, and even so it is not absolute —\n'
        '  **सर्वे विधयश्छन्दसि विकल्प्यन्ते इति पादान्तेऽपि क्वचिद् न भवति।\n'
        '  हन्तारं शत्रूणां कृधि विराजं गोपतिं गवाम्**'
    ),
)


_NUM = (
    'num(stem, gana=..., before=..., upasarga=..., gender=..., '
    'sense=..., chandasi=...) -> whether the नुम् goes in, or '
    'what stands in its place, by rule of 7.1.58-83.'
)

register(
    '7.1.58',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — इदितो नुम् धातोः — a root taught with an इ takes नुम्:\n'
        '  **कुडि — कुण्डिता, कुण्डितुम्, कुण्डा; हुडि — हुण्डिता, हुण्डा**.\n'
        '\n'
        'SETTLED — **AND IT GOES IN WHILE THE ROOT IS STILL BEING TAUGHT.**\n'
        '  **अयं धातूपदेशावस्थायाम् एव नुमागमो भवति** — not when the word is\n'
        "  built, and the vṛtti gives two proofs. कुण्डा needs 3.3.103's अ,\n"
        '  which wants a heavy penult that only the नुम् supplies; and\n'
        "  3.1.80's **धिन्विकृण्व्योर च** complains of roots *with their\n"
        '  nasal already attached*, which they could not be if the नुम् came\n'
        '  later.\n'
        '\n'
        'SETTLED — **AND THE इ OF तासि AND सिच् IS NOT THIS इ.**\n'
        '  **तासिसिचोरिदित्कार्यं नास्तीत्युच्चारणार्थो निरनुनासिक इकारः\n'
        '  पठ्यते** — theirs is there to pronounce the root by, and is not\n'
        '  nasal'
    ),
)

register(
    '7.1.59',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — शे मुचादीनाम् — eight roots take नुम् before श: **मुञ्चति,\n'
        '  लुम्पति, विन्दति, लिम्पति, सिञ्चति, कृन्तति, खिन्दति, पिंशति**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA ADDS FIVE MORE THAT HAD ALREADY LOST A\n'
        '  NASAL.** **शे तृम्फादीनाम् उपसंख्यानं कर्तव्यम्** — तृम्फ, दृम्फ,\n'
        '  गुम्फ, उम्भ, शुम्भ are read in the धातुपाठ WITH a nasal, 6.4.24\n'
        '  takes it out, and this rule puts one back: **तृम्फति, गुम्फति,\n'
        '  शुम्भति**. And having been supplied on purpose it cannot be taken\n'
        '  out again — **स च विधानसामर्थ्याद् न लुप्यते**. The roots read\n'
        '  without the nasal give तृफति, गुफति, शुभति'
    ),
)

register(
    '7.1.60',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — मस्जिनशोर्झलि — मस्ज् and नश् take नुम् before a\n'
        '  झल्-initial affix: **मङ्क्ता, मङ्क्तुम्; नंष्टा, नंष्टुम्**.\n'
        '\n'
        'SETTLED — **AND FOR मस्ज् THE नुम् DOES NOT GO WHERE 1.1.47 WOULD\n'
        '  PUT IT.** **मस्जेरन्त्यात् पूर्वं नुमम्\n'
        '  इच्छन्त्यनुषङ्गादिलोपार्थम्** — before the LAST sound and not\n'
        '  before the last vowel, so that the cluster may then simplify:\n'
        '  **मग्नः, मग्नवान्**'
    ),
)

register(
    '7.1.61',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — रधिजभोरचि — रध् and जभ् take नुम् before a vowel-initial\n'
        '  affix: **रन्धयति, रन्धकः, साधुरन्धी; जम्भयति, जम्भकः**. And the\n'
        '  नुम् beats the vṛddhi that would otherwise have come, though the\n'
        '  vṛddhi is later — **परापि सती वृद्धिर् नुमा बाध्यते, नित्यत्वात्**'
    ),
)

register(
    '7.1.62',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — नेट्यलिटि रधेः — but रध् does NOT take it before an\n'
        '  इट्-initial affix that is not the perfect: **रधिता, रधितुम्,\n'
        '  रधितव्यम्**.\n'
        '\n'
        'SETTLED — **AND IT IS PUT AS A REFUSAL RATHER THAN AS A RESTRICTION\n'
        '  FOR A REASON.** **अथ क्वसौ कथं भवितव्यम्?** — रेधिवान् is built by\n'
        '  doing the एत्व and the reduplication-loss first, then the इट्,\n'
        '  then the नुम्. And a नियम was possible — *only before an इट् in\n'
        '  the perfect* — but **विपरीतमप्यवधारणं संभाव्येत**, it could be\n'
        '  read backwards, and then रधिता would keep its nasal'
    ),
)

register(
    '7.1.63',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — रभेरशब्लिटोः — रभ् takes नुम् before a vowel-initial affix\n'
        '  that is neither शप् nor the perfect: **आरम्भयति, आरम्भकः,\n'
        '  साध्वारम्भी, आरम्भो वर्तते**'
    ),
)

register(
    '7.1.64',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — लभेश्च — and so does लभ्: **लम्भयति, लम्भकः, साधुलम्भी,\n'
        '  लम्भो वर्तते**. It is given a sūtra of its own rather than joined\n'
        '  to the one before, and the vṛtti says why in three words —\n'
        '  **लभेश्च पृथग्योगकरणम् उत्तरार्थम्**, so that the five rules after\n'
        '  it may carry लभ् alone'
    ),
)

register(
    '7.1.65',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — आङो यि — after आङ् the लभ् takes नुम् before a य-initial\n'
        '  affix: **आलम्भ्या गौः, आलम्भ्या वडवा**. And the accent follows\n'
        '  from which affix it is: the नुम् goes in FIRST, so the root no\n'
        "  longer has an अ in its penult, so 3.1.124's ण्यत् applies and not\n"
        '  यत्, and the word is स्वरित at the end by 6.2.139 and 6.1.185'
    ),
)

register(
    '7.1.66',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — उपात् प्रशंसायाम् — and after उप where PRAISE is meant:\n'
        '  **उपलम्भ्या भवता विद्या; उपलम्भ्यानि धनानि**'
    ),
)

register(
    '7.1.67',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — उपसर्गात् खल्घञोः — and after ANY preverb before खल् and\n'
        '  घञ्: **ईषत्प्रलम्भः, सुप्रलम्भः; प्रलम्भः, विप्रलम्भः**. **सिद्धे\n'
        '  सत्यारम्भो नियमार्थः** — 7.1.64 had already supplied the नुम्, so\n'
        '  this sūtra can only be fencing it: after a preverb and NOT\n'
        '  otherwise'
    ),
)

register(
    '7.1.68',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — न सुदुर्भ्यां केवलाभ्याम् — but not after सु and दुर्\n'
        '  ALONE: **सुलभम्, दुर्लभम्; सुलाभः, दुर्लाभः**.\n'
        '\n'
        'SETTLED — **AND केवल IS THERE BECAUSE OF HOW THE CASE IS READ.**\n'
        '  **सुदुर्भ्यामिति तृतीयां मत्वा केवलग्रहणं क्रियते। पञ्चम्यां हि\n'
        '  व्यवहितत्वाद् एवाप्रसङ्गः** — read as an ablative the word would\n'
        '  have been unnecessary. And अतिसुलभम् keeps the refusal only while\n'
        '  अति is a कर्मप्रवचनीय; when it is a preverb the नुम् comes back —\n'
        '  **अतिसुलम्भः**'
    ),
)

register(
    '7.1.69',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — विभाषा चिण्णमुलोः — before चिण् and णमुल् the नुम् is\n'
        '  optional: **अलाभि, अलम्भि; लाभंलाभम्, लम्भंलम्भम्**. And the\n'
        '  option is a व्यवस्थित one — **तेनानुपसृष्टस्य विकल्पः, उपसृष्टस्य\n'
        '  नित्यं नुम् भवति। प्रालम्भि, प्रलम्भंप्रलम्भम्** — free only where\n'
        '  there is no preverb'
    ),
)

register(
    '7.1.70',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — उगिदचां सर्वनामस्थानेऽधातोः — a stem with उ, ऋ or ऌ for\n'
        '  its marker, and अञ्चति, take नुम् before a सर्वनामस्थान: **भवान्,\n'
        '  भवन्तौ, भवन्तः; श्रेयान्, श्रेयांसौ; पचन्, पचन्तौ; प्राङ्,\n'
        '  प्राञ्चौ**. This is the rule that gives the strong cases their\n'
        '  shape.\n'
        '\n'
        'SETTLED — **AND अधातोः IS THERE TO LET A FORMER ROOT BACK IN.**\n'
        '  **अधातोरिति किम्? अधातुभूतपूर्वस्यापि यथा स्यात्। गोमन्तम् इच्छति\n'
        '  गोमत्यति, गोमत्यतेरप्रत्ययो गोमान्** — गोमत् has been made a root\n'
        '  and then un-made, and without the word it would have been shut out\n'
        '  for what it briefly was'
    ),
)

register(
    '7.1.71',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — युजेरसमासे — युज् takes नुम् before a सर्वनामस्थान where\n'
        '  it is NOT in a compound: **युङ्, युञ्जौ, युञ्जः**. And the root is\n'
        '  named with an इ — **युजेरितीकारनिर्देशाद् युज समाधौ इत्यस्य ग्रहणं\n'
        '  न भवति** — so the other युज् is out'
    ),
)

register(
    '7.1.72',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — नपुंसकस्य झलचः — a NEUTER stem ending in a झल् or in a\n'
        '  vowel takes नुम् before a सर्वनामस्थान: **उदश्विन्ति, शकृन्ति,\n'
        '  यशांसि, पयांसि; कुण्डानि, वनानि, त्रपूणि, जतूनि**. Where a stem is\n'
        '  both उगित् and झल्-final this rule wins for being later —\n'
        '  **परत्वाद् अनेनैव नुम् भवति। श्रेयांसि, भूयांसि**. A vārttika\n'
        '  takes one word out: **बहूर्जि प्रतिषेधो वक्तव्यः**'
    ),
)

register(
    '7.1.73',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — इकोऽचि विभक्तौ — a neuter stem ending in इ, उ, ऋ or ऌ\n'
        '  takes नुम् before a VOWEL-INITIAL case ending: **त्रपुणी, जतुनी,\n'
        '  तुम्बुरुणी; त्रपुणे, जतुने**.\n'
        '\n'
        'SETTLED — **AND THE WORD अचि IS A ज्ञापक ABOUT SOMETHING ELSE.** The\n'
        '  vṛtti asks why it is there, since the next sūtra says it anyway,\n'
        '  and answers: **हे त्रपो इत्यत्र नुम् मा भूत्** — the vocative has\n'
        '  its ending elided, and 1.1.63 should have stopped the rule\n'
        '  reaching at all. That it has to be stopped by hand shows the\n'
        '  prohibition does not hold here — **एतद् एवाज्ग्रहणं ज्ञापकं\n'
        '  प्रत्ययलक्षणप्रतिषेधोऽत्र न भवतीति**'
    ),
)

register(
    '7.1.74',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — तृतीयादिषु भाषितपुंस्कं पुंवद्गालवस्य — in the\n'
        '  instrumental and after, a neuter stem that also has a masculine\n'
        "  behaves AS a masculine, in Gālava's view: **ग्रामण्या\n"
        '  ब्राह्मणकुलेन** beside **ग्रामणिना ब्राह्मणकुलेन**; **ग्रामण्ये**\n'
        '  beside **ग्रामणिने**.\n'
        '\n'
        'SETTLED — **AND WHAT IT BUYS IS THAT TWO RULES DO NOT APPLY.** **यथा\n'
        '  पुंसि ह्रस्वनुमौ न भवतः, तद्वद् अत्रापि न भवतः** — no shortening\n'
        "  and no नुम्. The sūtra names the teacher, which is Pāṇini's way of\n"
        '  recording a view as an option rather than adopting it. In the\n'
        '  genitive plural the नुट् wins by पूर्वविप्रतिषेध — **ग्रामणीनां\n'
        '  ब्राह्मणकुलानाम्**'
    ),
)

register(
    '7.1.75',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः — अस्थि, दधि, सक्थि and\n'
        '  अक्षि take अनङ् instead, and it is UDĀTTA: **अस्थ्ना, अस्थ्ने;\n'
        '  दध्ना, दध्ने; सक्थ्ना; अक्ष्णा, अक्ष्णे**.\n'
        '\n'
        'SETTLED — **AND THE ACCENT IS PART OF THE RULE.** **अस्थ्यादय\n'
        '  आद्युदात्ताः, तेषाम् अनङादेशः स्थानिवद्भावाद् अनुदात्तः स्याद्\n'
        '  इत्युदात्तवचनम्** — by 1.1.56 the substitute would have inherited\n'
        '  the toneless quality of what it replaced. With the accent stated,\n'
        "  6.4.134's अ-loss then throws it onto the ending by 6.1.161. And\n"
        '  the four reach a compound ending in them: **प्रियास्थ्ना\n'
        '  ब्राह्मणेन**'
    ),
)

register(
    '7.1.76',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — छन्दस्यपि दृश्यते — and in the Veda the अनङ् is seen where\n'
        "  none of 7.1.75's conditions holds: before a CONSONANT — **इन्द्रो\n"
        '  दधीचो अस्थभिः; भद्रं पश्येम अक्षभिः**; outside the तृतीयादि —\n'
        '  **अस्थान्युत्कृत्य जुहोति**; and with no case ending at all —\n'
        '  **अक्षण्वता लाङ्गलेन; अस्थन्वन्तं यद् अनस्था बिभर्ति**. Three\n'
        '  conditions lapsing, one for each quarter of the rule they came\n'
        '  from'
    ),
)

register(
    '7.1.77',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — ई च द्विवचने — and in the dual they take ई, also udātta:\n'
        '  **अक्षी ते इन्द्र पिङ्गले कपेरिव; अक्षीभ्यां ते नासिकाभ्याम्**.\n'
        "  The ई beats 7.1.73's नुम् for being later, and the नुम् does not\n"
        '  then come back — **सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितम्\n'
        '  एव**'
    ),
)

register(
    '7.1.78',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — नाभ्यस्ताच्छतुः — the शतृ after a REDUPLICATED stem does\n'
        '  not take नुम्: **ददत्, ददतौ, ददतः; दधत्; जक्षत्; जाग्रत्**. And\n'
        '  the refusal reaches across an intervening ई — **शतुरनन्तर ईकारो न\n'
        '  विहित इति व्यवहितस्यापि नुमः प्रतिषेधो विज्ञायते**'
    ),
)

register(
    '7.1.79',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — वा नपुंसकस्य — but for a NEUTER the नुम् is optional after\n'
        '  all: **ददति, ददन्ति कुलानि; दधति, दधन्ति; जक्षति, जक्षन्ति;\n'
        '  जाग्रति, जाग्रन्ति** — the refusal of the sūtra before undone by\n'
        '  half'
    ),
)

register(
    '7.1.80',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — आच्छीनद्योर्नुम् — after an अ-final stem the शतृ\n'
        '  optionally takes नुम् before शी and a नदी ending: **तुदती कुले,\n'
        '  तुदन्ती कुले; याती ब्राह्मणी, यान्ती ब्राह्मणी; करिष्यती,\n'
        '  करिष्यन्ती**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI CANNOT AGREE ON WHAT आत् QUALIFIES.** The\n'
        '  vowels have already merged, so there is no अ-final stem left to\n'
        '  speak of. **अत्र समाधिं केचिद् आहुः — शतुरवयवे शतृशब्दे वर्तते** —\n'
        "  some read आत् with the शतृ's own first sound; **अपरे पुनराहुः —\n"
        '  आदित्येतेन शीनद्यावेव विशेष्येते** — others read it with the शी\n'
        '  and the नदी. Two readings, and the vṛtti gives both without\n'
        '  choosing'
    ),
)

register(
    '7.1.81',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — शप्श्यनोर्नित्यम् — but after शप् and श्यन् the नुम् is\n'
        '  COMPULSORY: **पचन्ती कुले, पचन्ती ब्राह्मणी; दीव्यन्ती;\n'
        '  सीव्यन्ती**. **नित्यग्रहणं वेत्यस्य अधिकारस्य निवृत्त्यर्थम्** —\n'
        '  the word नित्यम् is there to end the वा that has been governing,\n'
        '  or one might have thought the option went on'
    ),
)

register(
    '7.1.82',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — सावनडुहः — अनडुह् takes नुम् before सु: **अनड्वान्; हे\n'
        "  अनड्वन्**. Whether it goes in before or after 7.1.98's आम् is\n"
        '  disputed — **केचिद् आदित्यधिकाराद् आममोः कृतयोर् नुमं कुर्वन्ति**,\n'
        '  while others let both apply without either displacing the other,\n'
        '  **यथा चिचीषत्यादिषु दीर्घत्वद्विर्वचनयोः**'
    ),
)

register(
    '7.1.83',
    apply=num,
    codification=_NUM,
    notes=(
        'SETTLED — दृक्स्ववस्स्वतवसां छन्दसि — दृक्, स्ववस् and स्वतवस् take\n'
        '  नुम् before सु in the Veda: **ईदृङ्, तादृङ्, यादृङ्, सदृङ्;\n'
        '  स्ववान्; स्वतवाँः पायुरग्ने**'
    ),
)


_STRONG_STEM = (
    'strong_stem(stem, gana=..., before=..., part=..., '
    'result=..., chandasi=...) -> what the stem becomes before a '
    'strong ending, by rule of 7.1.84-103.'
)

register(
    '7.1.84',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — दिव औत् — दिव् becomes द्यौ before सु: **द्यौः**. And the\n'
        '  दिव् meant is the noun — **दिविति प्रातिपदिकम् अस्ति निरनुबन्धकम्।\n'
        '  धातुस्तु सानुबन्धकः, स इह न गृह्यते**'
    ),
)

register(
    '7.1.85',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — पथिमथ्यृभुक्षामात् — पथिन्, मथिन् and ऋभुक्षिन् take आ\n'
        '  before सु: **पन्थाः, मन्थाः, ऋभुक्षाः**. The इन् they end in is\n'
        '  nasal and the आ that replaces it is not — **भाव्यमानेन सवर्णानां\n'
        '  ग्रहणं न भवति इति शुद्धो ह्ययम् उच्चार्यते**, a substitute being\n'
        '  brought into existence cannot be qualified by what it replaced'
    ),
)

register(
    '7.1.86',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — इतोऽत् सर्वनामस्थाने — and their इ becomes अ in every\n'
        '  strong case: **पन्थाः, पन्थानौ, पन्थानः, पन्थानम्; मन्थानौ;\n'
        '  ऋभुक्षाणौ, ऋभुक्षाणम्**. The sūtra says अत् again although आत् was\n'
        '  already running — **आदिति वर्तमाने पुनरद्वचनं षपूर्वार्थम्** — so\n'
        "  that 6.4.9's optional lengthening after a ष् may have something\n"
        '  short to work on: **ऋभुक्षणम्**'
    ),
)

register(
    '7.1.87',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — थो न्थः — and the थ् of पथिन् and मथिन् becomes न्थ् in\n'
        '  the strong cases: **पन्थाः, पन्थानौ, पन्थानः; मन्थाः, मन्थानौ,\n'
        '  मन्थानः**. Three rules acting on one word, and only all three\n'
        '  together give the form'
    ),
)

register(
    '7.1.88',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — भस्य टेर्लोपः — but where the stem is भ they lose their टि\n'
        '  altogether: **पथः, पथा, पथे; मथः, मथा; ऋभुक्षः, ऋभुक्षा**. The\n'
        '  सर्वनामस्थान that has been governing cannot come here —\n'
        '  **सर्वनामस्थान इत्यनुवर्तमानम् अपि विरोधाद् इह न सम्बध्यते** —\n'
        '  since a stem cannot be भ and strong at once, and the anuvṛtti is\n'
        '  dropped for contradiction'
    ),
)

register(
    '7.1.89',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — पुंसोऽसुङ् — पुंस् becomes पुमांस् in the strong cases:\n'
        '  **पुमान्, पुमांसौ, पुमांसः**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA IS NEEDED FOR THE ACCENT OF A COMPOUND.**\n'
        '  In परमपुमान् the समासान्त accent falls before the ending is even\n'
        '  added; the असुङ् then comes and would move it. **तदर्थम्\n'
        '  असुङ्युपदेशिवद्वचनं कर्तव्यम्** — treat the substitute as though\n'
        '  it had been there from the start, and परमपुमान् is अन्तोदात्त\n'
        '  while पुमान् alone stays आद्युदात्त'
    ),
)

register(
    '7.1.90',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — गोतो णित् — a सर्वनामस्थान after गो is treated as ङित्, so\n'
        '  its vṛddhi comes: **गौः, गावौ, गावः**.\n'
        '\n'
        'SETTLED — **AND THE vṛtti OFFERS TWO WAYS TO SAVE हे चित्रगो.**\n'
        '  Either **अङ्गवृत्ते पुनर्वृत्ताव् अविधिर् निष्ठितस्य** — the guṇa\n'
        '  is already done and the णित् does not come back; or गोतः is a\n'
        "  genitive of relation, and only an ending that expresses गो's own\n"
        "  number is गो's. Some read ओतो णित् instead, to catch द्यौः, द्यावौ\n"
        '  as well'
    ),
)

register(
    '7.1.91',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — णलुत्तमो वा — and the first-person णल् is optionally ङित्:\n'
        '  **अहं चकर, अहं चकार; अहं पपच, अहं पपाच**'
    ),
)

register(
    '7.1.92',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — सख्युरसम्बुद्धौ — a सर्वनामस्थान after सखि is ङित्, the\n'
        '  vocative singular excepted: **सखायौ, सखायः**'
    ),
)

register(
    '7.1.93',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — अनङ् सौ — and सखि becomes सखान् before सु, unless that सु\n'
        '  is the vocative: **सखा**. Two sūtras in a row for one word, and\n'
        '  they do different things: 7.1.92 makes the ending ङित् so that the\n'
        "  vṛddhi comes, and this one replaces the stem's own last part. Both\n"
        '  spare the vocative, and the vṛtti gives the same counter-example\n'
        '  twice — **असंबुद्धाविति किम्? हे सखे**'
    ),
)

register(
    '7.1.94',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — ऋदुशनस्पुरुदंसोऽनेहसां च — an ऋ-final stem, and उशनस्,\n'
        '  पुरुदंसस् and अनेहस्, take अनङ् before सु outside the vocative:\n'
        '  **कर्ता, हर्ता, माता, पिता, भ्राता; उशना, पुरुदंसा, अनेहा**.\n'
        '\n'
        'SETTLED — **AND उशनस् HAS THREE VOCATIVES AND THE VṚTTI CHOOSES\n'
        '  NONE.** **उशनसः संबुद्धावपि पक्षेऽनङ् इष्यते। हे उशनन्** — and\n'
        "  8.2.8's न-loss may be refused or not, giving **हे उशन** beside\n"
        "  **हे उशनः**. A verse records all three and adds a fourth teacher's\n"
        '  view: **संबोधने तूशनसस्त्रिरूपं सान्तं तथा नान्तमथाप्यदन्तम्।\n'
        '  माध्यंदिनिर्वष्टि गुणं त्विगन्ते**'
    ),
)

register(
    '7.1.95',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — तृज्वत् क्रोष्टुः — क्रोष्टु takes the SHAPE a तृच्-final\n'
        '  stem would have had: **क्रोष्टा, क्रोष्टारौ, क्रोष्टारः,\n'
        '  क्रोष्टारम्**.\n'
        '\n'
        'SETTLED — **AND WHICH तृच्-FINAL STEM IS A QUESTION THE VṚTTI HAS TO\n'
        '  ANSWER.** **रूपातिदेशोऽयम्। प्रत्यासत्तेश्च क्रुशेरेव तृजन्तस्य\n'
        '  यद् रूपं तद् अतिदिश्यते** — the nearest one, क्रोष्टृ from क्रुश्,\n'
        '  **तच्च अन्तोदात्तम्**. A shape is conferred and not a substitute\n'
        '  supplied, which is why the accent comes with it'
    ),
)

register(
    '7.1.96',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — स्त्रियां च — and in the feminine: **क्रोष्ट्री,\n'
        '  क्रोष्ट्रीभ्याम्, क्रोष्ट्रीभिः**. **असर्वनामस्थानार्थम् आरम्भः**\n'
        '  — the sūtra exists for the cases the one before could not reach.\n'
        '  Whether क्रोष्टु is in the गौरादि list is disputed, and the vṛtti\n'
        '  says what goes wrong on that reading: **पञ्चभिः क्रोष्ट्रीभिः\n'
        '  क्रीतैः पञ्चक्रोष्टृभी रथैः इति न सिध्यति। तत्र प्रतिविधेयम्**'
    ),
)

register(
    '7.1.97',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — विभाषा तृतीयाऽऽदिष्वचि — and in the oblique cases before a\n'
        '  vowel it is OPTIONAL: **क्रोष्ट्रा, क्रोष्टुना; क्रोष्ट्रे,\n'
        '  क्रोष्टवे; क्रोष्टरि, क्रोष्टौ**. And where the shape is conferred\n'
        '  the नुम् and नुट् still come, by पूर्वविप्रतिषेध — **तृज्वद्भावात्\n'
        '  पूर्वविप्रतिषेधेन नुम्नुटौ भवतः। प्रियक्रोष्टुनेऽरण्याय;\n'
        '  क्रोष्टूनाम्**'
    ),
)

register(
    '7.1.98',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — चतुरनडुहोरामुदात्तः — चतुर् and अनडुह् take the augment\n'
        '  आम्, and it is udātta: **चत्वारः; अनड्वान्, अनड्वाहौ, अनड्वाहः**.\n'
        '  It reaches a compound ending in one — **तदन्तविधिरत्रेष्यते।\n'
        '  प्रियचत्वाः, प्रियानड्वान्** — and a vārttika makes the feminine\n'
        '  optional: **अनडुहः स्त्रियां वेति वक्तव्यम्। अनडुही, अनड्वाही**'
    ),
)

register(
    '7.1.99',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — अम् सम्बुद्धौ — but in the vocative singular the augment\n'
        '  is अम् instead: **हे प्रियचत्वः; हे प्रियानड्वन्**. **पूर्वस्यायम्\n'
        '  अपवादः** — an exception to the sūtra before, and the vṛtti says so\n'
        '  in three words'
    ),
)

register(
    '7.1.100',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — ॠत इद्धातोः — a ॠ-final ROOT takes इ for it: **किरति,\n'
        '  गिरति, आस्तीर्णम्, विशीर्णम्**. And a root that is one only by a\n'
        "  rule's reckoning counts too — **लाक्षणिकस्याप्यत्र ग्रहणम् इष्यते।\n"
        '  चिकीर्षति** — which is what the word धातोः is doing in the sūtra'
    ),
)

register(
    '7.1.101',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — उपधायाश्च — and a ॠ in the PENULT: **कीर्तयति, कीर्तयतः,\n'
        '  कीर्तयन्ति**. Two words, and the whole of the rule before is\n'
        '  carried over: the इ, the root, and the ॠ it replaces. What is new\n'
        '  is only where in the stem it stands — last in 7.1.100, second-last\n'
        '  here'
    ),
)

register(
    '7.1.102',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — उदोष्ठ्यपूर्वस्य — but where a LABIAL stands before the ॠ\n'
        '  the substitute is उ: **पूर्ताः पिण्डाः; पुपूर्षति; मुमूर्षति**. A\n'
        '  dental-labial counts as a labial — **वुवूर्षति ऋत्विजम्** — and\n'
        '  the labial must be part of the stem itself, **अङ्गावयव एव\n'
        '  गृह्यते**, so संपूर्वस्य ऋ gives समीर्णम्.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA ORDERS THESE AGAINST THE\n'
        '  STRENGTHENINGS.** **इत्त्वोत्त्वाभ्यां गुणवृद्धी भवतो\n'
        '  विप्रतिषेधेन** — guṇa and vṛddhi win: **आस्तरणम्, आस्तारकः;\n'
        '  निगरणम्, निगारकः**'
    ),
)

register(
    '7.1.103',
    apply=strong_stem,
    codification=_STRONG_STEM,
    notes=(
        'SETTLED — बहुलं छन्दसि — and in the Veda the उ is बहुलम्, reaching\n'
        '  where no labial stands and failing where one does: **मित्रावरुणा\n'
        '  ततुरिम्; दूरे ह्यध्वा जगुरिः** with no labial, and **पप्रितमम्,\n'
        '  वव्रितमम्** with one and no उ. Sometimes both — **क्वचिद् भवति।\n'
        '  पपुरिः**.\n'
        '\n'
        "SETTLED — **AND THIS CLOSES पाद ७.१.** The Kāśikā's colophon follows\n"
        '  it: **इति श्रीवामनविरचितायां काशिकायां वृत्तौ सप्तमाध्यायस्य\n'
        '  प्रथमः पादः**'
    ),
)


register(
    '7.1.3',
    apply=jho_antah,
    codification='jho_antah(affix) -> the affix with its झ् replaced by अन्त्.',
    related=('1.3.7', '1.3.9', '1.4.2', '3.4.78'),
    notes=(
        'SETTLED — प्रत्ययावयवस्य झस्य अन्त इत्ययम् आदेशो भवति: कुर्वन्ति,\n'
        '  सुन्वन्ति, चिन्वन्ति, and पचन्ति.\n'
        '\n'
        'SETTLED — and it is an अपवाद to 1.3.7 चुटू, which the commentaries\n'
        '  say rather than leave to be inferred. The Kāśikā on 1.3.7 lists\n'
        '  झ् among the cu-series initials that become इत् and then notes\n'
        '  झस्य अन्तादेशं वक्ष्यति; the Nyāsa calls the substitution\n'
        '  इत्संज्ञापवादम् outright.\n'
        '\n'
        'SETTLED — the consequence is not decorative. Both rules reach the\n'
        '  झ् of झि, and if 1.3.7 wins the affix is a bare इ and पचन्ति is\n'
        '  underivable — the engine produced पचै before this was codified.\n'
        '  It is the first genuine विप्रतिषेध in the engine\'s rule set, and\n'
        '  the first place 1.4.2 is consulted about a real conflict rather\n'
        '  than a constructed one. It is settled the way 1.4.2 says such a\n'
        '  clash is NOT settled — by the exception defeating its उत्सर्ग,\n'
        '  whatever the numbers say.'
    ),
)


__all__ = ['becomes', 'case_ending', 'in_the_veda', 'jho_antah', 'num', 'strong_stem', 'takes']
