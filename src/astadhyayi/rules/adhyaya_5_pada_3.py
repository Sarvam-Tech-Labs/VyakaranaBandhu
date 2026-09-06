# -*- coding: utf-8 -*-
"""
अध्याय ५, पाद ३ — प्राग्दिशो विभक्तिः, and the affixes stop meaning
anything of their own.

Every heading before this one supplied an AFFIX. This one supplies a
NAME: everything given from 5.3.1 to 5.3.26 is called a विभक्ति, and
the rule itself gives nothing. And with it the समर्थ heading lapses —
अतः परं स्वार्थिकाः प्रत्ययाः, from here the affixes add nothing to
the base's meaning, so there is no second word to construe with and
2.1.1 has nothing to do. Only the option carries on.
"""

from __future__ import annotations

from src.astadhyayi.sources import register
from src.astadhyayi.svarthika import in_own_sense

_RULES = {
    '5.3.1': (
        'SETTLED — प्राग्दिशो विभक्तिः — and the heading gives no affix.\n'
        '  **प्रागेतस्माद् दिक्संशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामो\n'
        '  विभक्तिसंज्ञास्ते वेदितव्याः**: everything named from here to\n'
        '  5.3.27 is CALLED a विभक्ति. The sixth heading bounded by lifting a\n'
        '  word out of the rule it stops at, and the first that bounds a\n'
        '  NAME.\n'
        '\n'
        'SETTLED — **AND THE NAME IS GIVEN FOR TWO CONSEQUENCES.**\n'
        '  **तसिलादीनां विभक्तित्वे प्रयोजनं त्यदादिविधयः, इदमो\n'
        '  विभक्तिस्वरश्च** — being a विभक्ति lets the त्यदादि rules reach\n'
        '  these forms, and lets 6.1.171 ऊडिदम्… accent the affix in **इह**.\n'
        '\n'
        'SETTLED — **AND THE समर्थ HEADING LAPSES HERE.** **अतः परं\n'
        '  स्वार्थिकाः प्रत्ययाः, तेषु समर्थाधिकारः प्रथमग्रहणं च\n'
        '  प्रतियोग्यपेक्षत्वाद् नोपयुज्यत इति द्वयमपि निवृत्तम्** — from\n'
        "  here the affixes add nothing to the base's meaning, so there is no\n"
        '  second word to construe with and 2.1.1 has nothing to do. **वावचनं\n'
        '  तु वर्तत एव**, and the option carries: **कुतः, कस्मात्; कुत्र,\n'
        '  कस्मिन्**'
    ),
    '5.3.2': (
        'SETTLED — किंसर्वनामबहुभ्योऽद्व्यादिभ्यः — the bases the whole\n'
        '  section works on. **प्राग् दिश इत्येव**. कुतः, कुत्र; यतः, यत्र;\n'
        '  ततः, तत्र; बहुतः, बहुत्र.\n'
        '\n'
        'SETTLED — **अद्व्यादिभ्य इति किम्?** द्वाभ्याम्, द्वयोः.\n'
        '  **प्रकृतिपरिसंख्यानं किम्?** वृक्षात्, वृक्षे — the rule names its\n'
        '  bases so that ordinary nouns are left out. **प्राग् दिश इत्येव** —\n'
        '  वैयाकरणपाशः.\n'
        '\n'
        'SETTLED — **सर्वनामत्वादेव सिद्धे किमो ग्रहणं द्व्यादिपर्युदासात्**\n'
        '  — किम् is a सर्वनामन् already and is named anyway, because the\n'
        '  exclusion of द्वि and the rest would otherwise have cut it out\n'
        '  too. **बहुग्रहणे संख्याग्रहणम्** — and बहु is taken as a NUMERAL:\n'
        '  **इह न भवति — बहोः सूपात्**'
    ),
    '5.3.3': (
        'SETTLED — इदम इश् — a substitution before any affix of this section.\n'
        '  **शकारः सर्वादेशार्थः** — the श makes it replace the WHOLE word\n'
        '  and not just its last sound (1.1.55). **इह**'
    ),
    '5.3.4': (
        'SETTLED — एतेतौ रथोः, **इशोऽपवादः** — two substitutes before an\n'
        '  affix beginning with र or थ. **रेफेऽकार उच्चारणार्थः** — the अ of\n'
        '  रेफ is only so the letter can be said. 5.3.16 इदमो र्हिल् →\n'
        '  **एतर्हि**; 5.3.24 इदमस्थमुः → **इत्थम्**'
    ),
    '5.3.5': (
        'SETTLED — एतदोऽन् — **शकारः सर्वादेशार्थः** again. **अतः, अत्र**.\n'
        '\n'
        'SETTLED — **एतद इति योगविभागः कर्तव्यः** — and the rule is to be\n'
        '  split, so that एतद् also takes the एत and इत् of 5.3.4 before र\n'
        '  and थ: **एतर्हि, इत्थम्**. **रेफादिः अनद्यतने र्हिलन्यतरस्याम् इति\n'
        '  विद्यत एव; थमुप्रत्ययः पुनरेतद उपसंख्येयः**'
    ),
    '5.3.6': (
        'SETTLED — सर्वस्य सोऽन्यतरस्यां दि — optionally स for सर्व before an\n'
        '  affix beginning with द. **सर्वदा, सदा**.\n'
        '\n'
        'SETTLED — **प्राग्दिशीय इत्येव** — and only before an affix of THIS\n'
        '  section: **सर्वं ददातीति सर्वदा ब्राह्मणी**, a woman who gives\n'
        '  everything, where the दा is a verb and not one of these affixes'
    ),
    '5.3.7': (
        'SETTLED — पञ्चम्यास्तसिल् — the affix that replaces an ablative.\n'
        "  **कुतः, यतः, ततः, बहुतः**, and by 5.3.1's option they stand beside\n"
        '  कस्मात्, यस्मात्'
    ),
    '5.3.8': (
        'SETTLED — तसेश्च — and here तसिल् replaces not a case-ending but\n'
        '  ANOTHER AFFIX. 5.4.44 प्रतियोगे पञ्चम्यास्तसिः and 5.4.45 give\n'
        '  तसि; after these bases that तसि becomes तसिल्. **कुत आगतः**, यतः,\n'
        '  ततः, बहुत आगतः.\n'
        '\n'
        'SETTLED — **तसेस्तसिल्वचनं स्वरार्थं विभक्त्यर्थं च** — and the\n'
        '  point of the substitution is the ACCENT and the विभक्ति name, the\n'
        '  two things 5.3.1 said the name was for'
    ),
    '5.3.9': (
        'SETTLED — पर्यभिभ्यां च. **सर्वोभयार्थे वर्तमानाभ्यां प्रत्यय\n'
        '  इष्यते** — only where the two mean ALL ROUND and ON BOTH SIDES.\n'
        '  **परितः**, **सर्वत इत्यर्थः**; **अभितः**, **उभयत इत्यर्थः**'
    ),
    '5.3.10': (
        "SETTLED — सप्तम्यास्त्रल् — and the locative's affix. **कुत्र, यत्र,\n"
        '  तत्र, बहुत्र**'
    ),
    '5.3.11': (
        "SETTLED — इदमो हः, **त्रलोऽपवादः**. **इह** — and with 5.3.3's इश्\n"
        '  the whole word is replaced, so इदम् + ह comes out as इह'
    ),
    '5.3.12': (
        'SETTLED — किमोऽत्, **त्रलोऽपवादः**. **क्व भोक्ष्यसे,\n'
        '  क्वाध्येष्यसे**.\n'
        '\n'
        'SETTLED — **त्रलमपि केचिदिच्छन्ति; तत् कथम्? उत्तरसूत्राद् वावचनं\n'
        '  पुरस्तादपकृष्यते** — some want कुत्र too, and it is got by\n'
        '  dragging the *optionally* of the NEXT rule BACKWARD. The अपकर्ष\n'
        '  again, and the second time in two pādas'
    ),
    '5.3.13': (
        'SETTLED — वा ह च छन्दसि — **यथाप्राप्तं च**, so the forms of the\n'
        '  rules before stand as well. **क्व**, **कुह॑** (ऋ० ८.७३.४);\n'
        '  कुत्रचिदस्य सा दूरे'
    ),
    '5.3.14': (
        'SETTLED — इतराभ्योऽपि दृश्यन्ते — from the OTHER cases too,\n'
        '  **पञ्चमीसप्तम्यपेक्षमितरत्वम्**. **दृशिग्रहणं प्रायिकविध्यर्थम्**\n'
        '  — *are seen* makes it a rule for the most part, **तेन\n'
        '  भवदादिभिर्योग एवैतद्विधानम्**: only in construction with भवत् and\n'
        '  the like.\n'
        '\n'
        'SETTLED — **के पुनर्भवदादयः? भवान् दीर्घायुरायुष्मान् देवानां प्रिय\n'
        '  इति** — the polite second person. स भवान्, **ततो भवान्, तत्र\n'
        '  भवान्**; तं भवन्तम्, ततो भवन्तम्, तत्र भवन्तम्; and so through all\n'
        '  seven cases'
    ),
    '5.3.15': (
        'SETTLED — सर्वैकान्यकिंयत्तदः काले दा, **त्रलोऽपवादः**. सर्वस्मिन्\n'
        '  काले **सर्वदा**; एकदा, अन्यदा, कदा, यदा, तदा. **काल इति किम्?**\n'
        '  सर्वत्र देशे — of a PLACE the affix of 5.3.10 comes instead'
    ),
    '5.3.16': (
        'SETTLED — इदमो र्हिल्, **हस्यापवादः**. **लकारः स्वरार्थः**. अस्मिन्\n'
        "  काले **एतर्हि** — with 5.3.4's एत, since the affix begins with र.\n"
        '  **काल इत्येव** — इह देशे'
    ),
    '5.3.17': (
        'SETTLED — अधुना — **अधुनेति निपात्यते; इदमोऽश्भावो धुना च\n'
        '  प्रत्ययः**, the substitution and the affix laid down together.\n'
        '  अस्मिन् काले **अधुना**'
    ),
    '5.3.18': (
        'SETTLED — दानीं च. अस्मिन् काले **इदानीम्**'
    ),
    '5.3.19': (
        'SETTLED — तदो दा च — **चकाराद् दानीं च**. तस्मिन् काले **तदा,\n'
        '  तदानीम्**.\n'
        '\n'
        'SETTLED — **तदो दावचनमनर्थकम्, विहितत्वात्** — and the दा of this\n'
        '  rule is idle, 5.3.15 having given it already. The vṛtti says so\n'
        '  and leaves it'
    ),
    '5.3.20': (
        'SETTLED — तयोर्दार्हिलौ च छन्दसि, **यथासंख्यम्**; the इदम् member,\n'
        '  taking दा. **तयोरिति प्रातिपदिकनिर्देशः**, and **चकाराद्\n'
        '  यथाप्राप्तं च**, so the ordinary forms stand too: **इदावत्सरीयः**;\n'
        '  इदं तर्हि, इदानीम्\n'
        '\n'
        'SETTLED — तयोर्दार्हिलौ च छन्दसि, the तद् member, taking र्हिल्.\n'
        '  **तदानीम्** stands beside it by यथाप्राप्तम्'
    ),
    '5.3.21': (
        'SETTLED — अनद्यतने र्हिलन्यतरस्याम् — of a time NOT of today.\n'
        '  **छन्दसीति न स्वर्यते; सामान्येन विधानम्** — the Veda-restriction\n'
        '  of the rule before is not carried, so this holds generally.\n'
        '  **कर्हि, कदा; यर्हि, यदा; तर्हि, तदा**'
    ),
    '5.3.22': (
        'SETTLED — सद्यःपरुत्परार्यैषमःपरेद्यव्यद्यपूर्वेद्युर्…उत्तरेद्युः.\n'
        '  **सद्यःप्रभृतयः शब्दा निपात्यन्ते** — eighteen forms laid down,\n'
        '  and the vṛtti says how much comes from the laying-down:\n'
        '  **प्रकृतिः, प्रत्ययः, आदेशः, कालविशेष इति सर्वमेतद् निपातनाद्\n'
        '  लभ्यते** — base, affix, substitution AND the particular time, all\n'
        '  four from the निपातन.\n'
        '\n'
        'SETTLED — समानेऽहनि **सद्यः**, today; पूर्वस्मिन् संवत्सरे\n'
        '  **परुत्**, last year; पूर्वतरे संवत्सरे **परारी**, the year\n'
        '  before; अस्मिन् संवत्सरे **ऐषमः**, this year; परस्मिन्नहनि\n'
        '  **परेद्यवि**, tomorrow; अस्मिन्नहनि **अद्य**, today; and then\n'
        '  eight in एद्युस् — **पूर्वेद्युः, अन्येद्युः, अन्यतरेद्युः,\n'
        '  इतरेद्युः, अपरेद्युः, अधरेद्युः, उभयेद्युः, उत्तरेद्युः**.\n'
        '  **द्युश्चोभयाद् वक्तव्यः** — उभयद्युः'
    ),
    '5.3.23': (
        'SETTLED — प्रकारवचने थाल् — of the MANNER of a thing. **कथा, यथा,\n'
        '  तथा**'
    ),
    '5.3.24': (
        "SETTLED — इदमस्थमुः. **इत्थम्** — with 5.3.4's इत्, the affix\n"
        '  beginning with थ'
    ),
    '5.3.25': (
        'SETTLED — किमश्च. **कथम्**'
    ),
    '5.3.26': (
        'SETTLED — था हेतौ च छन्दसि — and with it the विभक्ति section closes.\n'
        '  From किम् in the sense of a CAUSE, in the Veda'
    ),
    '5.3.27': (
        'SETTLED — दिक्शब्देभ्यः सप्तमीपञ्चमीप्रथमाभ्यो दिग्देशकालेष्वस्तातिः\n'
        '  — the marker, and the sūtra whose word दिक् bounded the whole\n'
        '  section before it. From the words for the QUARTERS, in three\n'
        '  cases, of a quarter or a place or a time'
    ),
    '5.3.28': (
        'SETTLED — दक्षिणोत्तराभ्यामतसुच्, **अस्तातेरपवादः**. **दक्षिणतो\n'
        '  वसति, दक्षिणत आगतः, दक्षिणतो रमणीयम्** — one form for all three\n'
        '  cases, which is what a स्वार्थिक affix does. **दक्षिणाशब्दः काले न\n'
        '  संभवतीति दिग्देशवृत्तिः परिगृह्यते** — *south* cannot be said of a\n'
        '  TIME, so only the quarter and the place are taken here, though\n'
        '  5.3.27 named three. **अकारो विशेषणार्थः** — and the अ of the\n'
        "  affix's name is there for 2.3.30 षष्ठ्यतसर्थप्रत्ययेन"
    ),
    '5.3.29': (
        'SETTLED — विभाषा परावराभ्याम् — optionally, so the अस्ताति of 5.3.27\n'
        '  stands in the other half. **परतो वसति** beside **परस्ताद् वसति**;\n'
        '  अवरतो वसति beside अवस्ताद् वसति'
    ),
    '5.3.30': (
        'SETTLED — अञ्चेर्लुक् — the अस्ताति is REMOVED after the\n'
        '  quarter-words ending in अञ्च्. प्राच्यां दिशि वसति → **प्राग्\n'
        '  वसति**; प्रत्यग् वसति. **लुक् तद्धितलुकि इति स्त्रीप्रत्ययोऽपि\n'
        '  निवर्तते** (1.2.49) — and when a taddhita goes by लुक् the\n'
        '  feminine affix goes with it, which is why it is प्राग् and not\n'
        '  प्राची'
    ),
    '5.3.31': (
        'SETTLED — उपर्युपरिष्टात् — two forms laid down. **ऊर्ध्वस्योपभावो\n'
        '  रिल्रिष्टातिलौ च प्रत्ययौ निपात्येते**: ऊर्ध्वायां दिशि वसति →\n'
        '  **उपरि वसति**, **उपरिष्टाद् वसति**'
    ),
    '5.3.32': (
        'SETTLED — पश्चात्. **पश्चादित्ययं शब्दो निपात्यते**; **अपरस्य\n'
        '  पश्चभाव आतिश्च प्रत्ययः**. अपरस्यां दिशि वसति → **पश्चाद् वसति**.\n'
        '  Three vārttikas widen it: **दिक्पूर्वपदस्य अपरस्य पश्चभावो\n'
        '  वक्तव्यः, आतिश्च प्रत्ययः** — दक्षिणपश्चात्, उत्तरपश्चात्;\n'
        '  **अर्धोत्तरपदस्य दिक्पूर्वपदस्य पश्चभावः** — दक्षिणपश्चार्धः;\n'
        '  **विनापि पूर्वपदेन पश्चभावः** — पश्चार्धः'
    ),
    '5.3.33': (
        'SETTLED — पश्च पश्चा च छन्दसि. **पश्चपश्चाशब्दौ निपात्येते** —\n'
        '  **चकारात् पश्चादित्यपि भवति**, so three forms. **अपरस्य\n'
        '  पश्चभावोऽकाराकारौ च प्रत्ययौ निपात्येते**: पुरा व्याघ्रो जायते\n'
        '  **पश्च सिंहः**; **पश्चा सिंहः**; पश्चात् सिंहः'
    ),
    '5.3.34': (
        'SETTLED — उत्तराधरदक्षिणादातिः. उत्तरस्यां दिशि वसति **उत्तराद्\n'
        '  वसति**; अधराद् वसति; दक्षिणाद् वसति'
    ),
    '5.3.35': (
        'SETTLED — एनबन्यतरस्यामदूरेऽपञ्चम्याः — and both of the conditions\n'
        '  are new. **अदूरे** — only where the measure from the point of\n'
        '  reference is NOT FAR; **अपञ्चम्याः** — and not from an ablative,\n'
        '  so **प्रकृतेऽपि पञ्चमी पर्युदस्यते; तेनायं सप्तमीप्रथमान्ताद्\n'
        '  विज्ञायते प्रत्ययः**, the affix comes from the locative and\n'
        '  nominative only. **उत्तरेण वसति**, beside उत्तराद् वसति and\n'
        '  उत्तरतो वसति — three forms. **अदूर इति किम्?** उत्तराद् वसति.\n'
        '  **अपञ्चम्या इति किम्?** उत्तरादागतः. **अपञ्चम्या इति प्रागसेः** —\n'
        '  the exclusion runs only as far as 5.3.39, **असिप्रत्ययस्तु\n'
        '  पञ्चम्यन्तादपि भवति**. And **केचिदिहोत्तरादिग्रहणं नानुवर्तयन्ति;\n'
        '  दिक्छब्दमात्रात् प्रत्ययं मन्यन्ते** — some do not carry the three\n'
        '  words down and give the affix after any quarter-word: **पूर्वेण\n'
        '  ग्रामम्**'
    ),
    '5.3.36': (
        'SETTLED — दक्षिणादाच्. **अदूर इति न स्वर्यते** — the *not far* of\n'
        '  the rule before is NOT carried, and **अपञ्चम्या इति वर्तते** is.\n'
        '  **दक्षिणा वसति, दक्षिणा रमणीयम्**. **अपञ्चम्या इत्येव** — दक्षिणत\n'
        '  आगतः. **चकारो विशेषणार्थः** for 2.3.29 अञ्चूत्तरपदाजाहियुक्ते'
    ),
    '5.3.37': (
        'SETTLED — आहि च दूरे — and now the OPPOSITE condition, **दूरे\n'
        '  चेदवधिमानवधेर्भवति**, where the measure from the reference point\n'
        '  IS far. **दक्षिणाहि वसति, दक्षिणा वसति**. **दूर इति किम्?**\n'
        '  दक्षिणतो वसति'
    ),
    '5.3.38': (
        'SETTLED — उत्तराच्च. **उत्तरा वसति, उत्तराहि वसति**. **दूर इत्येव**\n'
        '  — उत्तरेण प्रयाति. **अपञ्चम्या इत्येव** — उत्तरादागतः'
    ),
    '5.3.39': (
        'SETTLED — पूर्वाधरावराणामसि पुरधवश्चैषाम्, **यथासंख्यम्** — the\n'
        '  affix and three substitutes yoked to it. **अपञ्चम्या इति\n'
        '  निवृत्तम्; तिसृणां विभक्तीनामिह ग्रहणम्** — the exclusion of the\n'
        '  ablative lapses here, and all three cases are taken.\n'
        '  **असीत्यविभक्तिको निर्देशः**. **पुरो वसति, पुर आगतः, पुरो\n'
        '  रमणीयम्**; अधो वसति; अवो वसति'
    ),
    '5.3.40': (
        'SETTLED — अस्ताति च — the same three substitutes before the अस्ताति\n'
        '  of 5.3.27. **पुरस्ताद् वसति, अधस्ताद् वसति**. **इदमेवादेशविधानं\n'
        '  ज्ञापकम् — अस्तातिरेभ्यो भवति, असिप्रत्ययेन न बाध्यत इति** — that\n'
        '  a substitute is enjoined before the अस्ताति is the evidence that\n'
        '  these three DO take the अस्ताति, and that the असि of the rule\n'
        '  before does not displace it. The ज्ञापक device again'
    ),
    '5.3.41': (
        'SETTLED — विभाषावरस्य — **पूर्वेण नित्ये प्राप्ते विकल्प उच्यते**,\n'
        '  what the rule before made obligatory becomes a choice for one of\n'
        '  the three. **अवस्ताद् वसति, अवरस्ताद् वसति**'
    ),
    '5.3.42': (
        'SETTLED — संख्याया विधार्थे धा — and with it the quarter-words are\n'
        '  done and the NUMERALS begin. **विधा प्रकारः, स च सर्वक्रियाविषय एव\n'
        '  गृह्यते** — a विधा is a manner, and it is taken of any action\n'
        '  whatever. **एकधा भुङ्क्ते, द्विधा गच्छति**; त्रिधा, चतुर्धा,\n'
        '  पञ्चधा'
    ),
    '5.3.43': (
        'SETTLED — अधिकरणविचाले च — a second sense for the same affix.\n'
        '  **अधिकरणं द्रव्यम्, तस्य विचालः संख्यान्तरापादनम्; एकस्यानेकीकरणम्\n'
        '  अनेकस्य वा एकीकरणम्** — a substance being brought to a different\n'
        '  number, one made many or many made one. **एकं राशिं पञ्चधा कुरु**;\n'
        '  अनेकम् **एकधा कुरु**'
    ),
    '5.3.44': (
        'SETTLED — एकाद् धो ध्यमुञन्यतरस्याम् — a substitute for the affix\n'
        '  after एक. **एकधा राशिं कुरु, **ऐकध्यं** कुरु; एकधा भुङ्क्ते,\n'
        '  ऐकध्यं भुङ्क्ते. **प्रकरणादेव लब्धे पुनर्धाग्रहणं विधार्थे\n'
        '  विहितस्यापि यथा स्यात्; अनन्तरस्यैव ह्येतत् प्राप्नोति** — the\n'
        '  affix is named again though the section supplies it, so that the\n'
        '  धा of the *manner* rule is reached too and not only the one just\n'
        '  before'
    ),
    '5.3.45': (
        'SETTLED — द्वित्र्योश्च धमुञ् — **चकारो विकल्पानुकर्षणार्थः**, the च\n'
        '  dragging the option down. **द्विधा, द्वैधम्; त्रिधा, त्रैधम्**.\n'
        '  **धमुञन्तात् स्वार्थे डदर्शनम्** — and a vārttika adds a further\n'
        '  affix in the same sense on top of that: **मतिद्वैधानि संश्रयन्ते**'
    ),
    '5.3.46': (
        'SETTLED — एधाच्च — a third substitute, so three forms apiece:\n'
        '  **द्वेधा, द्वैधम्, द्विधा**; त्रेधा, त्रैधम्, त्रिधा'
    ),
    '5.3.47': (
        'SETTLED — याप्ये पाशप् — **याप्यः कुत्सित इत्युच्यते**, in CONTEMPT.\n'
        '  याप्यो वैयाकरणः **वैयाकरणपाशः**; याज्ञिकपाशः. **यो व्याकरणशास्त्रे\n'
        '  प्रवीणो दुःशीलः, तत्र कस्माद् न भवति?** Why not of a grammarian\n'
        '  who is skilled but ill-behaved? **यस्य गुणस्य सद्भावाद् द्रव्ये\n'
        '  शब्दनिवेशः, तस्य कुत्सायां प्रत्ययः** — the affix is for contempt\n'
        '  of the QUALITY the word is applied for, and there the contempt is\n'
        '  of something else'
    ),
    '5.3.48': (
        'SETTLED — पूरणाद् भागे तीयादन् — from a word ending in the ordinal\n'
        '  affix तीय, in the sense of a SHARE. **स्वरार्थं वचनम्** — the rule\n'
        '  is for the accent and nothing else, the affix adding no meaning.\n'
        '  द्वितीयो भागो **द्वितीयः**; तृतीयः. **भाग इति किम्?** द्वितीयम्,\n'
        '  तृतीयम्. **पूरणग्रहणमुत्तरार्थम्, न ह्यपूरणस्तीयोऽस्ति;\n'
        '  मुखतीयादिरनर्थकः** — and the word *ordinal* is there only for the\n'
        '  NEXT rule, since there is no तीय that is not an ordinal'
    ),
    '5.3.49': (
        'SETTLED — प्रागेकादशभ्योऽच्छन्दसि — from the ordinals of the numbers\n'
        '  BELOW ELEVEN, outside the Veda. **स्वरार्थं वचनम्** again.\n'
        '  **पञ्चमः, सप्तमः, नवमः, दशमः**. **प्रागेकादशभ्य इति किम्?**\n'
        '  एकादशः, द्वादशः. **अच्छन्दसीति किम्?** त॑स्य॒ **पञ्च॒म॑म्**\n'
        '  इ॒न्द्रि॒य॑स्या॑पा॒क्राम॒त् (मै०सं० १.९.४)'
    ),
    '5.3.50': (
        'SETTLED — षष्ठाष्टमाभ्यां ञ च — **चकारादन् च**, so both. षष्ठो भागः\n'
        '  **षाष्ठः, षष्ठः**; आष्टमः, अष्टमः'
    ),
    '5.3.51': (
        'SETTLED — मानपश्वङ्गयोः कन्लुकौ च, **यथासंख्यम्**; the षष्ठ member,\n'
        '  of a MEASURE. **षष्ठको भागो मानं चेत् तद् भवति**. **चकाराद्\n'
        '  यथाप्राप्तं च**, so षाष्ठः and षष्ठः stand too. **मानपश्वङ्गयोरिति\n'
        '  किम्?** षाष्ठः, षष्ठः\n'
        '\n'
        'SETTLED — मानपश्वङ्गयोः कन्लुकौ च, the अष्टम member, of a PART OF A\n'
        '  BEAST — and here the affix is removed. **कस्य लुक्? ञस्य लुक्, अनो\n'
        '  वा** — and which affix goes is left open, either of the two the\n'
        '  rule before gave'
    ),
    '5.3.52': (
        'SETTLED — एकादाकिनिच्चासहाये — **चकारात् कन्लुकौ च**, and **आकिनिचः\n'
        '  कनो वा लुग् विज्ञायते; स च विधानसामर्थ्यात् पक्षे भवति**: three\n'
        '  forms, **एकाकी, एककः, एकः**. **असहायग्रहणं संख्याशब्दनिरासार्थम्;\n'
        '  तदुपादाने हि द्विबह्वोर्न स्यात्** — *without a companion* is said\n'
        '  to keep the NUMERAL sense out, since a numeral एक would let द्वि\n'
        '  and बहु in too. एकाकिनौ, एकाकिनः'
    ),
    '5.3.53': (
        'SETTLED — भूतपूर्वे चरट्. **भूतपूर्वशब्दोऽतिक्रान्तकालवचनः;\n'
        '  प्रकृतिविशेषणं चैतत्** — *formerly so* describes the BASE. आढ्यो\n'
        '  भूतपूर्व **आढ्यचरः**, once rich; सुकुमारचरः. **टकारो ङीबर्थः** —\n'
        '  आढ्यचरी'
    ),
    '5.3.54': (
        'SETTLED — षष्ठ्या रूप्य च — and here the *formerly* has moved.\n'
        '  **षष्ठ्यन्तात् प्रत्ययविधानात् संप्रति भूतपूर्वग्रहणं\n'
        '  प्रत्ययार्थस्य विशेषणम्, न तु प्रकृत्यर्थविशेषणम्** — because the\n'
        '  affix now comes after a GENITIVE, *formerly* describes what the\n'
        '  affix reports and not the base. देवदत्तस्य भूतपूर्वो गौर्\n'
        "  **देवदत्तरूप्यः**, once Devadatta's; **देवदत्तचरः**"
    ),
    '5.3.55': (
        'SETTLED — अतिशायने तमबिष्ठनौ — the SUPERLATIVE. **अतिशयनमतिशायनम्,\n'
        '  प्रकर्षः; निपातनाद् दीर्घत्वम्**. सर्व इम आढ्याः, अयमेषामतिशयेन\n'
        '  आढ्यः **आढ्यतमः**; सर्व इमे पटवः, अयमेषाम् अतिशयेन पटुः\n'
        '  **पटिष्ठः**, लघिष्ठः, गरिष्ठः. **AND THE VṚTTI STATES WHAT A\n'
        '  स्वार्थिक AFFIX DOES.** **प्रकृत्यर्थविशेषणं च स्वार्थिकानां\n'
        "  द्योत्यं भवति** — a qualification of the base's own meaning is\n"
        '  what these affixes MAKE MANIFEST, rather than adding anything.\n'
        '  **यदा च प्रकर्षवतां पुनः प्रकर्षो विवक्ष्यते, तदा\n'
        '  अतिशायिकान्तादपरः प्रत्ययो भवत्येव** — and where excellent things\n'
        '  are compared again, a second superlative comes on top of the\n'
        '  first: **श्रेष्ठतमाय क॑र्मणे॒**; युधिष्ठिरः **श्रेष्ठतमः**\n'
        '  कुरूणाम्'
    ),
    '5.3.56': (
        'SETTLED — तिङश्च — and after a FINITE VERB, which needed saying:\n'
        '  **ङ्याप्प्रातिपदिकात् इत्यधिकारात् तिङो न प्राप्नोतीतीदं वचनम्**\n'
        '  (4.1.1), the whole taddhita section being for nominal stems. सर्व\n'
        '  इमे पचन्ति, अयमेषामतिशयेन पचति **पचतितमाम्**; जल्पतितमाम्.\n'
        '  **इष्ठन् नोदाह्रियते, गुणवचने तस्य नियतत्वात्** — and the other\n'
        '  affix is not exemplified here, because 5.3.58 confines it to\n'
        '  quality-words'
    ),
    '5.3.57': (
        'SETTLED — द्विवचनविभज्योपपदे तरबीयसुनौ — the COMPARATIVE,\n'
        '  **तमबिष्ठनोरपवादौ**. **द्वयोरर्थयोर्वचनं द्विवचनम्; विभक्तव्यो\n'
        '  विभज्यः** — where a word for TWO stands by, or one that DIVIDES.\n'
        '  **यथासंख्यमत्र नेष्यते** — and the two affixes are not matched to\n'
        '  the two conditions. द्वाविमौ आढ्यौ, अयमनयोरतिशयेन आढ्यः\n'
        '  **आढ्यतरः**; पचतितराम्; **पटीयान्**, लघीयान्. And with a dividing\n'
        '  word: माथुराः पाटलिपुत्रकेभ्य **आढ्यतराः**, पटीयांसः'
    ),
    '5.3.58': (
        'SETTLED — अजादी गुणवचनादेव — a NIYAMA and not a विधि.\n'
        '  **इष्ठन्नीयसुनावजादी सामान्येन विहितौ, तयोरयं विषयनियमः क्रियते —\n'
        '  गुणवचनादेव भवतस्तौ, नान्यस्मादिति**: the two vowel-initial affixes\n'
        '  were given generally and are here CONFINED to quality-words.\n'
        '  **पटीयान्, पटिष्ठः**; **इह न भवतः — पाचकतरः, पाचकतमः**. **एवकार\n'
        '  इष्टतोऽवधारणार्थः, प्रत्ययनियमोऽयं न प्रकृतिनियम इति** — and the\n'
        '  *only* restricts the AFFIX and not the base, so a quality-word may\n'
        '  still take the others: **पटुतरः, पटुतमः**'
    ),
    '5.3.59': (
        'SETTLED — तुश्छन्दसि — **तुरिति तृन्तृचोः सामान्येन ग्रहणम्**.\n'
        '  **पूर्वेण गुणवचनादेव नियमे कृते छन्दसि\n'
        '  प्रकृत्यन्तराण्यभ्यनुज्ञायन्ते** — the restriction just made is\n'
        '  loosened for the Veda, and other bases are let in. आसु॒तिं\n'
        '  **करि॑ष्ठः**; **दोहीयसी** धेनुः'
    ),
    '5.3.60': (
        'SETTLED — प्रशस्यस्य श्रः — a substitute before the two\n'
        '  vowel-initial affixes. **श्रेष्ठः, श्रेयान्**. **AND THE\n'
        '  SUBSTITUTION UNDOES THE RESTRICTION JUST MADE.** **ननु च\n'
        '  प्रशस्यशब्दस्य अगुणवचनत्वाद् अजादी न संभवतः?** प्रशस्य is not a\n'
        '  quality-word, so by 5.3.58 those affixes cannot come after it at\n'
        '  all. **एवं तर्हि आदेशविधानसामर्थ्यात् तद्विषयो नियमो न प्रवर्तते**\n'
        '  — the force of a substitute being enjoined before them is that the\n'
        '  restriction does not reach here. **एवमुत्तरेष्वपि योगेषु\n'
        '  विज्ञेयम्**, and the same holds of the rules after this one'
    ),
    '5.3.61': (
        'SETTLED — ज्य च — a second substitute for the same word. **ज्येष्ठः,\n'
        '  ज्यायान्**. 6.4.160 ज्यादादीयसः gives the आ'
    ),
    '5.3.62': (
        'SETTLED — वृद्धस्य च — the same substitute for another word.\n'
        '  **ज्येष्ठः, ज्यायान्**, and **तयोश्च सत्त्वं नियमाभावेन पूर्ववद्\n'
        '  ज्ञाप्यते** — that the affixes come at all is again read out of\n'
        '  the substitution. **प्रियस्थिर० इत्यादिना वृद्धशब्दस्य वर्षादेशो\n'
        '  विधीयते; वचनसामर्थ्यात् पक्षे सोऽपि भवति** (6.4.157) — and वर्ष is\n'
        '  a substitute too, so **वर्षिष्ठः, वर्षीयान्** stand beside'
    ),
    '5.3.63': (
        'SETTLED — अन्तिकबाढयोर्नेदसाधौ, **यथासंख्यम्**; the अन्तिक member.\n'
        '  **निमित्तयोर्यथासंख्यमत्र नेष्यते**. **नेदिष्ठम्, नेदीयः**\n'
        '\n'
        'SETTLED — अन्तिकबाढयोर्नेदसाधौ, the बाढ member. सर्व इमे बाढमधीयते,\n'
        '  अयमेषामतिशयेन बाढमधीते **साधिष्ठम्**; **साधीयः**'
    ),
    '5.3.64': (
        'SETTLED — युवाल्पयोः कनन्यतरस्याम् — optionally, so both sets stand.\n'
        '  **कनिष्ठः, कनीयान्**, and **यविष्ठः, यवीयान्** beside them; and of\n'
        '  अल्प, कनिष्ठः, कनीयान्, **अल्पिष्ठः, अल्पीयान्**'
    ),
    '5.3.65': (
        'SETTLED — विन्मतोर्लुक् — the possessive affix is REMOVED before the\n'
        '  two. **इदमेव वचनं ज्ञापकम् अजादिसद्भावस्य** — and that its removal\n'
        '  is enjoined here is the evidence that those affixes come after\n'
        '  such words at all, which 5.3.58 had seemed to forbid. The third\n'
        '  time in six rules. सर्व इमे स्रग्विणः, अयमेषामतिशयेन स्रग्वी\n'
        '  **स्रजिष्ठः, स्रजीयान्**; त्वग्वान् **त्वचिष्ठः, त्वचीयान्**'
    ),
    '5.3.66': (
        'SETTLED — प्रशंसायां रूपप् — in PRAISE. **प्रशंसा स्तुतिः**.\n'
        '  प्रशस्तो वैयाकरणो **वैयाकरणरूपः**. **स्वार्थिकाश्च प्रत्ययाः\n'
        '  प्रकृत्यर्थविशेषस्य द्योतका भवन्ति; प्रकृत्यर्थस्य वैशिष्ट्ये\n'
        '  प्रशंसा भवति** — and the praise may be bitter: **वृषलरूपोऽयम्, यः\n'
        '  पलाण्डुना सुरां पिबति**, a fine sort of low fellow, who drinks his\n'
        '  liquor with onions; **चोररूपः, दस्युरूपः, योऽक्ष्णोरपि अञ्जनं\n'
        '  हरेत्**, who would steal the very collyrium off your eyes.\n'
        '  **तिङश्चेत्यनुवर्तते** — and after a finite verb too:\n'
        '  **पचतिरूपम्**. **क्रियाप्रधानम् आख्यातम्; एका च क्रियेति\n'
        '  रूपप्प्रत्ययान्ताद् द्विवचनबहुवचने न भवतः; नपुंसकलिङ्गं तु भवति,\n'
        '  लोकाश्रयत्वाल् लिङ्गस्य** — an action is one, so no dual or\n'
        '  plural; but the gender is neuter, gender resting on usage'
    ),
    '5.3.67': (
        'SETTLED — ईषदसमाप्तौ कल्पब्देश्यदेशीयरः — ALMOST, and the vṛtti\n'
        '  defines it: **संपूर्णता पदार्थानां समाप्तिः; स्तोकेनासंपूर्णता\n'
        '  ईषदसमाप्तिः**. ईषदसमाप्तः पटुः **पटुकल्पः, पटुदेश्यः, पटुदेशीयः**.\n'
        '  **तिङश्चेत्येव** — पचतिकल्पम्'
    ),
    '5.3.68': (
        'SETTLED — विभाषा सुपो बहुच् पुरस्तात्तु — and the affix goes IN\n'
        '  FRONT. **स तु पुरस्तादेव भवति न परतः**. **बहुपटुः, बहुमृदुः**;\n'
        '  बहुगुडो द्राक्षा. **चित्करणमन्तोदात्तार्थम्**. **विभाषावचनात्\n'
        '  कल्पबादयोऽपि भवन्ति** — the option lets the affixes of the rule\n'
        '  before stand. **सुब्ग्रहणं तिङन्ताद् मा भूदिति** — and *from a\n'
        '  case-form* is said so that a finite verb is NOT reached, though\n'
        '  the rule before reached one'
    ),
    '5.3.69': (
        'SETTLED — प्रकारवचने जातीयर् — of a KIND. **सामान्यस्य भेदको विशेषः\n'
        '  प्रकारः**. पटुप्रकारः **पटुजातीयः**; मृदुजातीयः. **प्रकारवति चायं\n'
        '  प्रत्ययः; थाल् पुनः प्रकारमात्र एव भवति** — and this affix is for\n'
        "  what HAS a kind, where 5.3.23's थाल् was for the kind itself. The\n"
        '  same word प्रकार in two rules of one pāda, and the vṛtti divides\n'
        '  them'
    ),
    '5.3.70': (
        'SETTLED — प्रागिवात्कः — a heading, and this one DOES supply an\n'
        '  affix. **इवे प्रतिकृतौ इति वक्ष्यति। प्रागेतस्मादिवसंशब्दनाद्\n'
        '  यानित ऊर्ध्वमनुक्रमिष्यामः, कप्रत्ययस्तेष्वधिकृतो वेदितव्यः** — क\n'
        '  for every sense named between here and 5.3.96, the seventh heading\n'
        '  bounded by lifting a word out of the rule it stops at. **अश्वकः,\n'
        '  गर्दभकः**. **तिङन्तादयं प्रत्ययो नेष्यते, अकजिष्यते** — and after\n'
        "  a FINITE VERB this affix is not wanted; the next rule's अकच् comes\n"
        '  instead. **तिङश्च इत्यनुवृत्तम् उत्तरसूत्रेणैव संबन्धनीयम्** — so\n'
        '  the *and after a finite verb* carried down from 5.3.56 attaches to\n'
        '  5.3.71 and not to this rule'
    ),
    '5.3.71': (
        'SETTLED — अव्ययसर्वनाम्नामकच् प्राक् टेः, **कस्यापवादः** — and the\n'
        '  affix goes INSIDE the word, before its last vowel and consonant:\n'
        '  **स च प्राक् टेः, न परतः**. **उच्चकैः, नीचकैः, शनकैः**; **सर्वके,\n'
        '  विश्वके, उभयके**. **AND WHETHER IT ENTERS THE STEM OR THE\n'
        '  INFLECTED WORD IS DECIDED BY USAGE.** **प्रातिपदिकात् सुप इति\n'
        '  द्वयमपीहानुवर्तते; तत्राभिधानतो व्यवस्था भवति** — both headings\n'
        '  are running, and which applies is settled by what the language\n'
        '  actually says: **युष्मकाभिः, युवकयोः** show it in the STEM,\n'
        '  **त्वयका, मयका** in the inflected word. **अकच्प्रकरणे तूष्णीमः\n'
        '  काम् प्रत्ययो वक्तव्यः** — **तूष्णीकामास्ते**; **शीले को मलोपश्च**\n'
        '  — तूष्णींशीलः, तूष्णीकः. And by the carried तिङश्च: **पचतकि,\n'
        '  जल्पतकि**'
    ),
    '5.3.72': (
        'SETTLED — कस्य च दः — the final क of the base becomes द when the\n'
        '  अकच् goes in. **चकारः सन्नियोगार्थः**, and **सामर्थ्याच्च\n'
        '  अव्ययग्रहणमनुवर्तते, न सर्वनामग्रहणम्, ककारान्तस्य\n'
        '  सर्वनाम्नोऽसंभवात्** — only the indeclinables are carried, there\n'
        '  being no pronoun ending in क. धिक् → **धकित्**; हिरुक् → हिरकुत्;\n'
        '  पृथक् → **पृथकत्**'
    ),
    '5.3.73': (
        'SETTLED — अज्ञाते — of something whose PARTICULARS are not known.\n'
        '  **अज्ञातविशेषोऽज्ञातः; स्वेन रूपेण ज्ञाते पदार्थे\n'
        '  विशेषरूपेणाज्ञाते प्रत्ययविधानम् एतत्** — the thing itself is\n'
        '  known and something about it is not. कस्यायमश्व इति\n'
        '  स्वस्वामिसंबन्धेनाज्ञाते **अश्वकः**, a horse whose owner one does\n'
        '  not know; गर्दभकः, उष्ट्रकः. **एवमन्यत्रापि यथायोगमज्ञातता\n'
        '  विज्ञेया**'
    ),
    '5.3.74': (
        'SETTLED — कुत्सिते — in CONTEMPT. **कुत्सितो गर्हितो निन्दितः;\n'
        '  प्रकृत्यर्थविशेषणं चैतत्**. कुत्सितो ऽश्वः **अश्वकः**; उष्ट्रकः,\n'
        '  गर्दभकः. And through the carried rules: उच्चकैः, सर्वके, **पचतकि**'
    ),
    '5.3.75': (
        'SETTLED — संज्ञायां कन्, **कस्यापवादः** — where the derived word is\n'
        '  a NAME, **प्रत्ययान्तेन चेत् संज्ञा गम्यते**. **शूद्रकः, धारकः,\n'
        '  पूर्णकः**'
    ),
    '5.3.76': (
        'SETTLED — अनुकम्पायाम् — in PITY. **कारुण्येन अभ्युपपत्तिः परस्य\n'
        "  अनुकम्पा**, taking another's part out of tenderness. **पुत्रकः,\n"
        '  वत्सकः, दुर्बलकः, बुभुक्षितकः**; and of a finite verb, **स्वपितकि,\n'
        '  श्वसितकि**'
    ),
    '5.3.77': (
        'SETTLED — नीतौ च तद्युक्तात् — **सामदानादिरुपायो नीतिः**, the arts\n'
        '  of winning a man over, and from what is JOINED to the pitied\n'
        '  thing. **हन्त ते धानकाः, हन्त ते तिलकाः** — *here, take these\n'
        '  grains of yours*. **पूर्वेण प्रत्यासन्नानुकम्पासंबन्धाद्\n'
        '  अनुकम्प्यमानादेव प्रत्ययो विहितः; सम्प्रति व्यवहितादपि यथा\n'
        '  स्यादिति वचनम्** — the rule before reached only the thing pitied\n'
        '  itself; this reaches what stands at one remove from it'
    ),
    '5.3.78': (
        "SETTLED — बह्वचो मनुष्यनाम्नष्ठज्वा — from a MAN'S NAME of more than\n"
        '  two vowels, optionally. **देविकः, देवदत्तकः**; यज्ञिकः,\n'
        '  यज्ञदत्तकः. **बह्वच इति किम्?** दत्तकः, गुप्तकः. **मनुष्यनाम्न इति\n'
        '  किम्?** मद्रबाहुकः, भद्रबाहुकः'
    ),
    '5.3.79': (
        'SETTLED — घनिलचौ च — **चकाराद् यथाप्राप्तं च**, and **पूर्वेण ठचि\n'
        '  विकल्पेन प्राप्ते वचनम्**, so four forms: **देवियः, देविलः,\n'
        '  देविकः, देवदत्तकः**'
    ),
    '5.3.80': (
        "SETTLED — प्राचामुपादेरडज्वुचौ च — from a man's name beginning with\n"
        '  उप, five affixes in all. **उपडः, उपकः, उपियः, उपिलः, उपिकः**, and\n'
        '  उपेन्द्रदत्तकः. **प्राचांग्रहणं पूजार्थम्; वेत्येव हि वर्तते** —\n'
        '  *of the Eastern teachers* is a courtesy and not a condition, the\n'
        '  option being already running'
    ),
    '5.3.81': (
        "SETTLED — जातिनाम्नः कन् — from a man's name that is also a\n"
        '  KIND-word. **बह्वच इति नानुवर्तते; सामान्येन विधानम्** — the\n'
        '  two-vowel condition is not carried. **व्याघ्रकः, सिंहकः, शरभकः**,\n'
        '  and **वावचनानुवृत्तेर्यथादर्शनम् अन्योऽपि भवति**: व्याघ्रिलः,\n'
        '  सिंहिलः. **नामग्रहणं स्वरूपनिवृत्त्यर्थम्**'
    ),
    '5.3.82': (
        'SETTLED — अजिनान्तस्योत्तरपदलोपश्च — the affix AND the loss of the\n'
        "  compound's second member. **व्याघ्राजिनो नाम कश्चिद् मनुष्यः,\n"
        '  सोऽनुकम्पितो व्याघ्रकः**; सिंहकः'
    ),
    '5.3.83': (
        'SETTLED — ठाजादावूर्ध्वं द्वितीयादचः — everything above the SECOND\n'
        '  VOWEL of the base is lost before ठ and the vowel-initial affixes.\n'
        '  **ऊर्ध्वग्रहणं सर्वलोपार्थम्**. अनुकम्पितो देवदत्तो **देविकः,\n'
        '  देवियः, देविलः**. **ठग्रहणम् उको द्वितीयत्वे कविधानार्थम्** — the\n'
        '  ठ is named so that a उ or ऋ as second vowel gets the क:\n'
        '  **वायुदत्तो वायुकः, पितृदत्तः पितृकः**. Five vārttikas widen it:\n'
        '  **चतुर्थादच ऊर्ध्वस्य लोपः** — बृहस्पतिकः; **अनजादौ विभाषा लोपः**\n'
        '  — देवदत्तकः, देवकः; **लोपः पूर्वपदस्य च ठाजादावनजादौ च** —\n'
        '  **दत्तिकः**; **विनापि प्रत्ययेन पूर्वोत्तरपदयोर् विभाषा लोपः** —\n'
        '  देवदत्तो **दत्तः, देवः**; **उवर्णाल् ल इलस्य च** — भानुदत्तो\n'
        '  **भानुलः**, and a kārikā sums the five'
    ),
    '5.3.84': (
        'SETTLED — शेवलसुपरिविशालवरुणार्यमादीनां तृतीयात् — from the THIRD\n'
        '  vowel for these, **पूर्वस्यायम् अपवादः**. शेवलदत्तः **शेवलिकः,\n'
        '  शेवलियः, शेवलिलः**; सुपरिकः, विशालिकः, वरुणिकः, अर्यमिकः.\n'
        '  **शेवलादीनां तृतीयादचो लोपः स च अकृतसन्धीनाम् इति वक्तव्यम्** —\n'
        '  and the count is taken BEFORE sandhi has been made:\n'
        '  शेवलेन्द्रदत्तः gives शेवलिकः and not **शेवलयिकः**'
    ),
    '5.3.85': (
        'SETTLED — अल्पे — of what is SMALL. **परिमाणापचयेऽल्पशब्दः**, a word\n'
        '  for a lessening of quantity. अल्पं तैलं **तैलकम्**; घृतकम्,\n'
        '  सर्वकम्, उच्चकैः, **पचतकि**'
    ),
    '5.3.86': (
        'SETTLED — ह्रस्वे — of what is SHORT. **दीर्घप्रतियोगी ह्रस्वः**,\n'
        '  short being the correlate of long. ह्रस्वो वृक्षो **वृक्षकः**;\n'
        '  प्लक्षकः, स्तम्भकः'
    ),
    '5.3.87': (
        "SETTLED — संज्ञायां कन् — where the short thing's name is made from\n"
        '  its shortness, **ह्रस्वत्वहेतुका या संज्ञा**. **वंशकः, वेणुकः,\n'
        '  दण्डकः**'
    ),
    '5.3.88': (
        'SETTLED — कुटीशमीशुण्डाभ्यो रः, **कस्यापवादः**. **संज्ञाग्रहणं\n'
        '  नानुवर्तते; सामान्येन विधानम्**. ह्रस्वा कुटी **कुटीरः**; शमीरः,\n'
        '  शुण्डारः. **स्वार्थिकत्वेऽपि पुँल्लिङ्गता, लोकाश्रयत्वाल्\n'
        '  लिङ्गस्य** — though the affix adds no meaning, the word turns\n'
        '  masculine, gender resting on usage and not on the derivation'
    ),
    '5.3.89': (
        'SETTLED — कुत्वा डुपच्, **कसापवादः**. ह्रस्वा कुतूः **कुतुपम्**,\n'
        '  **चर्ममयं स्नेहभाजनम् उच्यते**, a leather oil-flask;\n'
        '  **कुतूरित्यावपनस्याख्या**'
    ),
    '5.3.90': (
        'SETTLED — कासूगोणीभ्यां ष्टरच्, **कस्यापवादः**. **षकारो ङीषर्थः**.\n'
        '  ह्रस्वा कासूः **कासूतरी**; गोणीतरी. **कासूरिति शक्तिर् आयुधविशेष\n'
        '  उच्यते**'
    ),
    '5.3.91': (
        'SETTLED — वत्सोक्षाश्वर्षभेभ्यश्च तनुत्वे — **ह्रस्व इति\n'
        '  निवृत्तम्**, and the sense is now SLIGHTNESS. **यस्य गुणस्य हि\n'
        '  भावाद् द्रव्ये शब्दनिवेशः, तस्य तनुत्वे प्रत्ययः** — the\n'
        '  slightness is of the quality the word is applied for, and the\n'
        '  vṛtti works all four out: **प्रथमवया वत्सः, तस्य तनुत्वं\n'
        '  द्वितीयवयःप्राप्तिः** — **वत्सतरः**, a calf less of a calf for\n'
        '  being a year older; **तरुण उक्षा, तस्य तनुत्वं तृतीयवयःप्राप्तिः**\n'
        '  — उक्षतरः; **अश्वेनाश्वायामुत्पन्नोऽश्वः, तस्य तनुत्वम्\n'
        '  अन्यपितृकता** — **अश्वतरः**, a mule, less of a horse for having\n'
        '  another sire; **अनड्वानृषभः, तस्य तनुत्वं भारवहने मन्दशक्तिता** —\n'
        '  ऋषभतरः, less of a bull for drawing poorly'
    ),
    '5.3.92': (
        'SETTLED — किंयत्तदो निर्धारणे द्वयोरेकस्य डतरच् — singling ONE OUT\n'
        '  OF TWO. **जात्या क्रियया गुणेन संज्ञया वा समुदायादेकदेशस्य\n'
        '  पृथक्करणं निर्धारणम्** — by kind, act, quality or name. **कतरो\n'
        '  भवतोः कठः**; यतरो भवतोः पटुः; ततर आगच्छतु. **महाविभाषया चात्र\n'
        '  प्रत्ययो विकल्प्यते** — the great option makes it a choice: **को\n'
        '  भवतोर् देवदत्तः**. **निर्धारण इति विषयसप्तमीनिर्देशः; द्वयोरिति\n'
        '  समुदायाद् निर्धारणविभक्तिः; एकस्येति निर्धार्यमाणनिर्देशः** — each\n'
        '  of the three words of the rule accounted for'
    ),
    '5.3.93': (
        'SETTLED — वा बहूनां जातिपरिप्रश्ने डतमच् — one out of MANY, where a\n'
        '  KIND is asked after. **कतमो भवतां कठः**; यतमो भवतां कठः, ततम\n'
        '  आगच्छतु. **वावचनमकजर्थम्** — the option is for the अकच् of 5.3.71:\n'
        '  **यको भवतां कठः, सक आगच्छतु**. **जातिपरिप्रश्न इति किम्?** को\n'
        '  भवतां देवदत्तः. **परिप्रश्नग्रहणं च किम एव विशेषणम्, न\n'
        '  यत्तदोरसंभवात्; जातिग्रहणं तु सर्वैरेव संबध्यते** — the *asking*\n'
        '  qualifies किम् alone, the *kind* all three'
    ),
    '5.3.94': (
        'SETTLED — एकाच्च प्राचाम् — **चकारो डतरचोऽनुकर्षणार्थः**, and\n'
        '  **जातिपरिप्रश्न इति नानुवर्तते; सामान्येन विधानम्**.\n'
        '  **द्वयोर्निर्धारणे डतरच्, बहूनां निर्धारणे डतमच्**: एकतरो\n'
        '  भवतोर्देवदत्तः, **एकतमो भवतां देवदत्तः**. **प्राचांग्रहणं\n'
        '  पूजार्थम्, विकल्पोऽनुवर्तत एव**'
    ),
    '5.3.95': (
        'SETTLED — अवक्षेपणे कन् — in REPROACH. **अवक्षिप्यते येन\n'
        '  तदवक्षेपणम्**. **व्याकरणकेन नाम त्वं गर्वितः** — *so it is your\n'
        '  GRAMMAR you are proud of*. **परस्य कुत्सार्थं यदुपादीयते,\n'
        '  तदिहोदाहरणम्; यत् पुनः स्वयमेव कुत्सितम्, तत्र कुत्सिते इत्यनेन\n'
        '  कन् प्रत्ययो भवति** — here the thing named is brought in to\n'
        '  belittle ANOTHER; where the thing itself is contemptible, 5.3.74\n'
        '  gives the affix instead. The same affix, and the contempt pointing\n'
        '  two different ways. **AND THE HEADING CLOSES HERE.**\n'
        '  **प्रागिवीयस्य पूर्णोऽवधिः** — the seventh time this project has\n'
        '  met the formula, and the marker 5.3.96 stands one sūtra past the\n'
        '  last rule'
    ),
    '5.3.96': (
        'SETTLED — इवे प्रतिकृतौ — the marker, and the sūtra whose word इव\n'
        '  bounded the whole क section. **इवार्थः सादृश्यम्, तस्य विशेषणं\n'
        '  प्रतिकृतिग्रहणम्; प्रतिकृतिः प्रतिरूपकं प्रतिच्छन्दकम्** — a\n'
        '  LIKENESS, and the word *image* narrows it to a made likeness. अश्व\n'
        '  इवायम् अश्वप्रतिकृतिः **अश्वकः**, a horse in effigy.\n'
        '  **प्रतिकृताविति किम्?** गौरिव गवयः — a gayal is like a cow and is\n'
        '  not an image of one'
    ),
    '5.3.97': (
        'SETTLED — संज्ञायां च — where the whole word is a NAME.\n'
        '  **अप्रतिकृत्यर्थ आरम्भः** — and the rule is begun for what is NOT\n'
        '  an image: अश्वसदृशस्य संज्ञा **अश्वकः**'
    ),
    '5.3.98': (
        'SETTLED — लुम्मनुष्ये — the affix REMOVED where a man is meant.\n'
        '  चञ्चेव मनुष्यः **चञ्चा**, a man like a straw figure; **दासी,\n'
        '  खरकुटी**. **मनुष्य इति किम्?** अश्वकः, उष्ट्रकः'
    ),
    '5.3.99': (
        'SETTLED — जीविकार्थे चापण्ये — removed where the image is made for a\n'
        '  LIVELIHOOD and is not for sale. **विक्रीयते यत् तत् पण्यम्**.\n'
        '  **वासुदेवः, शिवः, स्कन्दः, विष्णुः** — **देवलकादीनां जीविकार्था\n'
        "  देवप्रतिकृतय उच्यन्ते**, the temple-servants' images of the gods.\n"
        "  **अपण्य इति किम्?** हस्तिकान् विक्रीणीते — an image-seller's stock\n"
        '  keeps its affix'
    ),
    '5.3.100': (
        'SETTLED — देवपथादिभ्यश्च — removed after an OPEN list, **आदिशब्दः\n'
        '  प्रकारे; आकृतिगणश्चायम्**. **देवपथः, हंसपथः**. And a kārikā gives\n'
        '  the three settings: अर्चासु पूजनार्थासु चित्रकर्मध्वजेषु च । इवे\n'
        '  प्रतिकृतौ लोपः कनो देवपथादिषु ॥ IMAGES for worship — **शिवः,\n'
        '  विष्णुः**; PAINTINGS — **अर्जुनः, दुर्योधनः**; BANNERS — **कपिः,\n'
        '  गरुडः, सिंहः**'
    ),
    '5.3.101': (
        'SETTLED — वस्तेर्ढञ् — **इतः प्रभृति प्रत्ययाः सामान्येन भवन्ति,\n'
        '  प्रतिकृतौ चाप्रतिकृतौ च**, and from here the affixes come whether\n'
        '  an image is meant or not. वस्तिरिव **वास्तेयः, वास्तेयी**'
    ),
    '5.3.102': (
        'SETTLED — शिलाया ढः. शिलेव **शिलेयं दधि**, curd like stone.\n'
        '  **केचिदत्र ढञमपीच्छन्ति, तदर्थं योगविभागः कर्तव्यः** — some want\n'
        '  ढञ् too, and the rule is split for it: **शैलेयम्**, then शिलेयम्'
    ),
    '5.3.103': (
        'SETTLED — शाखादिभ्यो यत्. शाखेव **शाख्यः**; मुख्यः, जघन्यः. शाखा,\n'
        '  मुख, जघन, शृङ्ग, मेघ, चरण, स्कन्ध, शिरस्, उरस्, अग्र, शरण —\n'
        '  शाखादिः'
    ),
    '5.3.104': (
        'SETTLED — द्रव्यं च भव्ये — **द्रव्यशब्दो निपात्यते**.\n'
        '  **द्रुशब्दादिवार्थे यत् प्रत्ययो निपात्यते**: **द्रव्यं भव्यः,\n'
        '  आत्मवान्, अभिप्रेतानाम् अर्थानां पात्रभूत उच्यते** — one who is a\n'
        '  fit vessel for what is wished for. **द्रव्योऽयं राजपुत्रः**, a\n'
        '  prince of promise'
    ),
    '5.3.105': (
        'SETTLED — कुशाग्राच्छः. कुशाग्रमिव सूक्ष्मत्वात् **कुशाग्रीया\n'
        '  बुद्धिः**, a mind as fine as the point of a kuśa blade'
    ),
    '5.3.106': (
        'SETTLED — समासाच्च तद्विषयात् — from a compound ALREADY made in that\n'
        '  sense, in that sense again. **काकतालीयम्, अजाकृपाणीयम्,\n'
        '  अन्धकवर्तकीयम्** — **अतर्कितोपनतं चित्रीकरणमुच्यते**, a startling\n'
        '  coincidence. **AND THE VṚTTI WORKS THE FIGURE OUT.** **काकस्यागमनं\n'
        '  यादृच्छिकम्, तालस्य पतनं च; तेन तालेन पतता काकस्य वधः कृतः** — the\n'
        '  crow comes by chance and the palm-fruit falls by chance, and the\n'
        '  fruit kills the crow. So of Devadatta and the bandits: **तत्र यो\n'
        '  देवदत्तस्य दस्यूनां च समागमः स काकतालसमागमसदृश इत्येक उपमार्थः;\n'
        '  अतश्च देवदत्तस्य वधः, स काकतालवधसदृश इति द्वितीय उपमार्थः** — two\n'
        '  comparisons, **तत्र प्रथमे समासः, द्वितीये प्रत्ययः**: the\n'
        '  compound carries the first and the affix the second. And\n'
        '  **समासश्चायमस्मादेव ज्ञापकात्, नह्यस्यापरं लक्षणमस्ति** — that\n'
        '  compound has no rule of its own, and this rule is the evidence\n'
        '  that it exists'
    ),
    '5.3.107': (
        'SETTLED — शर्करादिभ्योऽण्. शर्करेव **शार्करम्**; कापालिकम्. शर्करा,\n'
        '  कपालिका, पिष्टिक, पुण्डरीक, शतपत्र, गोलोमन्, गोपुच्छ, नरालि,\n'
        '  नकुला, सिकता — शर्करादिः'
    ),
    '5.3.108': (
        'SETTLED — अङ्गुल्यादिभ्यष्ठक्. अङ्गुलीव **अङ्गुलिकः**; भारुजिकः.\n'
        '  अङ्गुलि, भरुज, बभ्रु, वल्गु, मण्डर, मण्डल, शष्कुल, कपि, उदश्वित्,\n'
        '  गोणी, उरस्, शिखर, कुलिश — अङ्गुल्यादिः'
    ),
    '5.3.109': (
        'SETTLED — एकशालायाष्ठजन्यतरस्याम् — **अन्यतरस्यांग्रहणेन अनन्तरष्ठक्\n'
        '  प्राप्यते**, the option letting the ठक् of the rule before stand.\n'
        '  एकशालेव **एकशालिकः, ऐकशालिकः**'
    ),
    '5.3.110': (
        'SETTLED — कर्कलोहितादीकक्. **कर्कः शुक्लोऽश्वः, तेन सदृशः\n'
        '  **कार्कीकः**; **लौहितीकः स्फटिकः**, **स्वयमलोहितोऽप्युपाश्रयवशात्\n'
        '  तथा प्रतीयते** — a crystal not itself red, but taken so from what\n'
        '  lies behind it'
    ),
    '5.3.111': (
        'SETTLED — प्रत्नपूर्वविश्वेमात् थाल् छन्दसि. तं प्॒**रत्नथा॑**\n'
        '  पू॒**र्वथा॑** वि॒**श्वथा** इ॒**मथा॑** (ऋ० ५.४४.१)'
    ),
    '5.3.112': (
        'SETTLED — पूगाञ् ञ्योऽग्रामणीपूर्वात् — **इवार्थ इति निवृत्तम्**,\n'
        "  and the pāda's last section begins. **नानाजातीया\n"
        '  अनियतवृत्तयोऽर्थकामप्रधानाः संघाः पूगाः** — a पूग is a troop of\n'
        '  mixed birth and no settled livelihood, bent on gain and pleasure.\n'
        '  **लौहध्वज्यः, शैब्यः, चातक्यः**. **अग्रामणीपूर्वादिति किम्?**\n'
        '  देवदत्तो ग्रामणीरेषां त इमे **देवदत्तकाः** — where the troop is\n'
        "  named from its LEADER, 5.2.78's affix comes instead"
    ),
    '5.3.113': (
        'SETTLED — व्रातच्फञोरस्त्रियाम् — **नानाजातीया अनियतवृत्तय\n'
        '  उत्सेधजीविनः संघा व्राताः**, the same definition 5.2.21 gave.\n'
        '  **कापोतपाक्यः, व्रैहिमत्यः**; and after a च्फञ्, **कौञ्जायन्यः,\n'
        '  ब्राध्नायन्यः**. **अस्त्रियामिति किम्?** कपोतपाकी, कौञ्जायनी'
    ),
    '5.3.114': (
        'SETTLED — आयुधजीविसंघाञ् ञ्यड् वाहीकेष्वब्राह्मणराजन्यात् — from the\n'
        '  words for a CONFEDERACY LIVING BY ARMS, among the Vāhīkas,\n'
        '  brahmins and kṣatriyas excepted. **टकारो ङीबर्थः; तेनास्त्रियामिति\n'
        '  नानुवर्तते** — the ट gives the feminine, so the *not in the\n'
        '  feminine* of the rule before is not carried. **कौण्डीबृस्यः,\n'
        '  क्षौद्रक्यः, मालव्यः**, and in the feminine कौण्डीबृसी, **मालवी**.\n'
        '  Four conditions, four counter-examples. **आयुधजीविग्रहणं किम्?**\n'
        '  मल्लाः, शयण्डाः. **संघग्रहणं किम्?** सम्राट्. **वाहीकेष्विति\n'
        '  किम्?** शबराः, पुलिन्दाः. **अब्राह्मणराजन्यादिति किम्?** गोपालवा\n'
        '  ब्राह्मणाः, शालङ्कायना राजन्याः'
    ),
    '5.3.115': (
        'SETTLED — वृकाट् टेण्यण्. **टकारो ङीबर्थः, णकारो वृद्ध्यर्थः**.\n'
        '  **वार्केण्यः**, वार्केण्यौ, वृकाः. **आयुधजीविसंघविशेषणं\n'
        '  जातिशब्दाद् मा भूत्** — the condition is there so that the affix\n'
        '  does not come after the word for the ANIMAL: **कामक्रोधौ\n'
        '  मनुष्याणां खादितारौ वृकाविव**, desire and anger, two wolves that\n'
        '  devour men'
    ),
    '5.3.116': (
        'SETTLED — दामन्यादित्रिगर्तषष्ठाच्छः. **दामनीयः, औलपीयः**; and from\n'
        '  the six of which त्रिगर्त is the sixth, **कौण्डोपरथीयः,\n'
        '  दाण्डकीयः**. And a verse names them: आहुस्त्रिगर्तषष्ठांस्तु\n'
        '  कौण्डोपरथदाण्डकी । क्रौष्टकिर्जालमानिश्च ब्राह्मगुप्तोऽथ जानकिः ॥\n'
        '  दामनी, औलपि, आकिदन्ती, काकरन्ति, शत्रुन्तपि, सार्वसेनि, बिन्दु,\n'
        '  मौञ्जायन, उलभ, सावित्रीपुत्र — दामन्यादिः'
    ),
    '5.3.117': (
        'SETTLED — पर्श्वादियौधेयादिभ्यामणञौ, the पर्श्वादि half. **पार्शवः,\n'
        '  आसुरः**. पर्शु, असुर, रक्षस्, बाह्लीक, वयस्, मरुत्, दशार्ह, पिशाच,\n'
        '  विशाल, अशनि, कार्षापण, सत्वत्, वसु — पर्श्वादिः\n'
        '\n'
        'SETTLED — पर्श्वादियौधेयादिभ्यामणञौ, the यौधेयादि half. **यौधेयः,\n'
        '  शौक्रेयः**. यौधेय, कौशेय, क्रौशेय, शौक्रेय, शौभ्रेय, धार्तेय,\n'
        '  वार्तेय, जाबालेय, त्रिगर्त, भरत, उशीनर — यौधेयादिः'
    ),
    '5.3.118': (
        'SETTLED — अभिजिद्विदभृच्छालावच्छिखावच्छमीवदूर्णावच्छ्रुमदणो यञ् —\n'
        '  **आयुधजीविसंघादिति निवृत्तम्**. **अभिजितोऽपत्यमित्यण्; तदन्ताद्\n'
        '  यञ्** — the affix comes after a stem that already carries अण्.\n'
        '  **आभिजित्यः, वैदभृत्यः, शालावत्यः**. **गोत्रप्रत्ययस्यात्राणो\n'
        '  ग्रहणमिष्यते** — and the अण् meant is the LINEAGE affix, so\n'
        '  **आभिजितो मुहूर्तः, आभिजितः स्थालीपाकः** are not reached'
    ),
    '5.3.119': (
        'SETTLED — ञ्यादयस्तद्राजाः — and the pāda ends as it began, with a\n'
        '  NAME. **पूगाञ् ञ्योऽग्रामणीपूर्वात् इत्यतः प्रभृति ये प्रत्ययाः,\n'
        '  ते तद्राजसंज्ञा भवन्ति** — everything from 5.3.112 to 5.3.118 is\n'
        '  called a तद्राज. **तद्राजप्रदेशाः — तद्राजस्य बहुषु… इत्येवमादयः**\n'
        '  (2.4.62) — and the vṛtti names where the name is USED, as 5.3.1\n'
        '  did of विभक्ति. A pāda opened by a saṃjñā-heading and closed by a\n'
        '  saṃjñā-rule, and both of them give the reason the name is worth\n'
        '  giving. इति श्रीजयादित्यविरचितायां काशिकायां वृत्तौ पञ्चमाध्यायस्य\n'
        '  तृतीयः पादः'
    ),
}

_IN_OWN_SENSE_LINE = (
    'in_own_sense(stem, gana=..., samjna=..., case=..., '
    'result=..., before=..., usage=..., wants=...) -> which affix '
    'is added to that base in its own sense.'
)

#: Nothing declared. Every rule of this pāda is answered by the one
#: resolver, so a declaration would name the function it already is —
#: which the reuse walk rejects, and rightly.
_REUSES = {}

for _sutra, _notes in _RULES.items():
    register(
        _sutra,
        apply=in_own_sense,
        codification=_IN_OWN_SENSE_LINE,
        notes=_notes,
        reuses=_REUSES.get(_sutra, ()),
    )
