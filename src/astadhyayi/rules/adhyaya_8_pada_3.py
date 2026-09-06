# -*- coding: utf-8 -*-
"""अध्याय ८, पाद ३ — the visarga."""

from __future__ import annotations

from src.astadhyayi.anga import kharavasanayoh
from src.astadhyayi.ru_anunasika import in_samhita
from src.astadhyayi.visarjaniya import the_visarga
from src.astadhyayi.murdhanya import the_cerebral
from src.astadhyayi.murdhanya_nisedha import also_cerebral
from src.astadhyayi.sources import register


register(
    '8.3.15',
    apply=kharavasanayoh,
    reuses=('1.1.71',),
    codification=(
        'kharavasanayoh(pada, at_pause=..., following=...) -> the pada with '
        'its final र् as a visarga.'
    ),
    related=('8.2.1', '8.2.66'),
    notes=(
        'SETTLED — रेफान्तस्य पदस्य खरि परतः अवसाने च विसर्जनीयादेशो\n'
        '  भवति: वृक्षः and प्लक्षः at a pause, वृक्षस्तरति before खर्.\n'
        '\n'
        'SETTLED — खरवसानयोरिति किम्? अग्निर्नयति, वायुर्नयति. न् is\n'
        '  neither खर् nor a pause, so the र् stands. Which is why this is\n'
        '  not "a final र् becomes ः" and why 8.2.66 stops at रु rather\n'
        '  than going straight to the visarga: the two part company\n'
        '  precisely there.\n'
        '\n'
        'NOTE — खर् is resolved from the śivasūtras, not listed.'
    ),
)


_IN_SAMHITA = (
    'in_samhita(word, gana=..., before=..., view=..., '
    'chandasi=...) -> the ru, the nasal before it and the '
    'anusvara, by rule of 8.3.1-33.'
)

register(
    '8.3.1',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — मतुवसो रु सम्बुद्धौ छन्दसि — a मतुप्-final or वस्-final\n'
        '  word takes रुँ before a vocative ending, in the Veda: **इन्द्र\n'
        '  मरुत्व इह पाहि सोमम्; हरिवो मेदिनं त्वा**. **संहितायाम् इति\n'
        "  वर्तते** — 8.2.108's heading is running, and every rule of this\n"
        '  pāda is said of sounds in close juncture'
    ),
)

register(
    '8.3.2',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — अत्रानुनासिकः पूर्वस्य तु वा — an अधिकार, and the first of\n'
        "  the pāda's own: **इत उत्तरं यस्य स्थाने रुर् विधीयते, ततः पूर्वस्य\n"
        '  तु वर्णस्य वा अनुनासिको भवति इत्येतद् अधिकृतं वेदितव्यम्**.\n'
        '  Wherever a रुँ is given from here on, the sound BEFORE it may go\n'
        '  nasal — **सँस्स्कर्ता** beside संस्स्कर्ता — and 8.3.4 gives the\n'
        '  other half of that option its anusvāra instead'
    ),
)

register(
    '8.3.3',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — आतोऽटि नित्यम् — but before an अट् the आ before a रुँ is\n'
        '  ALWAYS nasal: **महाँ असि**. 8.3.9 will give the रुँ there, and the\n'
        '  heading would have made the nasal optional — **ततः पूर्वस्य\n'
        '  अतोऽनुनासिकविकल्पे प्राप्ते नित्यार्थं वचनम्**. So the rule exists\n'
        '  only to take an option away'
    ),
)

register(
    '8.3.4',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — अनुनासिकात् परोऽनुस्वारः — and where the sound before the\n'
        '  रुँ has NOT been made nasal, an anusvāra is put in after it:\n'
        '  **संस्स्कर्ता; संस्कर्ता**. The vṛtti has to supply a word for the\n'
        '  sūtra to be read at all — **अन्यशब्दोऽत्र अध्याहर्तव्यः**,\n'
        "  अनुनासिकाद् अन्यः — so that the genitive means 'other than a\n"
        "  nasalised sound' and not 'after a nasal'"
    ),
)

register(
    '8.3.5',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — समः सुटि — सम् takes रुँ before a सुट्: **सँस्स्कर्ता,\n'
        '  सँस्स्कर्तुम्, सँस्स्कर्तव्यम्** and **संस्स्कर्ता** beside them.\n'
        '  The vṛtti walks the rest of the derivation out: the रुँ becomes a\n'
        '  visarga, and 8.3.36 वा शरि then makes the doubled स् optional'
    ),
)

register(
    '8.3.6',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — पुमः खय्यम्परे — पुम् takes रुँ before a खय् that has an\n'
        '  अम् after it: **पुँस्कामा, पुंस्कामा; पुँस्पुत्रः; पुँस्फलम्;\n'
        '  पुँश्चली**. Without it 8.3.37 कुप्वोः क पौ च would have given\n'
        '  पुंस्कामा a जिह्वामूलीय instead of the स्, which is what the vṛtti\n'
        '  says the rule is for'
    ),
)

register(
    '8.3.7',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — नश्छव्यप्रशान् — any न्-final word except प्रशान् takes\n'
        '  रुँ before a छव् with an अम् after it: **भवाँश्छादयति,\n'
        '  भवांश्छादयति; भवाँश्चिनोति; भवाँष्टीकते; भवाँस्तरति**. This is the\n'
        '  rule every भवान् in the language passes through before a stop, and\n'
        '  the exception is one word'
    ),
)

register(
    '8.3.8',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — उभयथर्क्षु — but in the ṛcs it goes both ways, with the\n'
        '  रुँ or with the न् left standing: **तस्मिंस् त्वा दधाति, तस्मिन्\n'
        '  त्वा दधाति**. **पूर्वेण नित्ये प्राप्ते विकल्पः क्रियते** — the\n'
        '  sūtra before had made it compulsory and this makes it a choice, in\n'
        '  one register of the Veda only'
    ),
)

register(
    '8.3.9',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — दीर्घादटि समानपादे — a word-final न् after a LONG vowel\n'
        '  takes रुँ before an अट्, provided the two stand in the SAME\n'
        '  metrical quarter: **परिधीँर् अति; देवाँ अच्छा दीद्यत्**. **तौ चेद्\n'
        '  निमित्तनिमित्तिनौ समानपादे भवतः** — and पाद here is the quarter of\n'
        '  a verse, **ऋक्ष्वि इति प्रकृतत्वाद् ऋक्पाद इह गृह्यते**, carried\n'
        '  down from the sūtra before. No other rule in the work asks where a\n'
        '  metrical line begins'
    ),
)

register(
    '8.3.10',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — नॄन् पे — नॄन् takes रुँ before प: **नॄँः पाहि, नॄंः पाहि;\n'
        '  नॄँः प्रीणीहि**. **अकार उच्चारणार्थः** — the अ in पे is only there\n'
        '  to make the letter pronounceable. And some carry उभयथा down from\n'
        '  8.3.8, which would make it optional; the Kāśikā records that\n'
        '  without adopting it'
    ),
)

register(
    '8.3.11',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — स्वतवान् पायौ — and स्वतवान् before पायु: **स्वतवाँः\n'
        '  पायुर् अग्ने**. One word before one word, for one line of the\n'
        '  Ṛgveda — which is what a great many of the Vedic rules of this\n'
        '  pāda come to, and the Kāśikā gives no more than the line'
    ),
)

register(
    '8.3.12',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — कानाम्रेडिते — and कान् before its own आम्रेडित:\n'
        '  **कांस्कान् आमन्त्रयते; कांस्कान् भोजयति**. The doubling is\n'
        "  8.1.4's वीप्सा and the word is in the कस्कादि list of 8.3.48\n"
        '  besides — **तेन कुप्वोः क पौ च इति न भवति** — so the स् is heard\n'
        '  and not a जिह्वामूलीय'
    ),
)

register(
    '8.3.13',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — ढो ढे लोपः — a ढ् before a ढ् is dropped: **लीढम्, मीढम्,\n'
        '  उपगूढम्**. The heading पदस्य is still running from 8.1.16, but a\n'
        '  word cannot end in ढ् before another ढ् — **तस्य असम्भवाद्\n'
        '  अपदान्तस्य ढकारस्य अयं लोपो विज्ञायते** — so the rule is read of a\n'
        '  ढ् INSIDE a word, and the heading is quietly set aside'
    ),
)

register(
    '8.3.14',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — रो रि — and a र् before a र् is dropped: **नीरक्तम्,\n'
        '  दूरक्तम्; अग्नी रथः; इन्दू रथः; पुना रक्तं वासः; प्राता\n'
        '  राजक्रयः**. The preceding vowel lengthens by 6.3.111, which is why\n'
        '  अग्नि gives अग्नी. And this rule too reaches inside a word — **तेन\n'
        '  अपदान्तस्य अपि रेफस्य लोपो भवति** — for अजर्घाः and अपास्पाः'
    ),
)

register(
    '8.3.16',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — रोः सुपि — the र् of a रुँ becomes a visarga before a\n'
        '  locative plural ending: **पयःसु, सर्पिःषु, यशःसु**. **सुपि इति\n'
        '  सप्तमीबहुवचनं गृह्यते** — सुप् names that one ending here and not\n'
        '  the whole class. And the rule is a restriction rather than a\n'
        '  provision — **सिद्धे सत्य् आरम्भो नियमार्थः। रोर् एव सुपि\n'
        '  विसर्जनीयादेशः, न अन्यस्य** — 8.3.15 would have given the visarga\n'
        '  anyway, and this confines it to a रुँ so that गीर्षु keeps its र्'
    ),
)

register(
    '8.3.17',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — भोभगोअघोअपूर्वस्य योऽशि — the र् of a रुँ standing after\n'
        '  भोः, भगोः, अघोः or an अ-vowel becomes य् before an अश्: **भो अत्र;\n'
        '  भगो अत्र; अघो अत्र; भो ददाति**; and after an अ, **क आस्ते, कय्\n'
        '  आस्ते; ब्राह्मणा ददति; पुरुषा ददति**. This is the rule the three\n'
        '  teachers of the next three sūtras then disagree about'
    ),
)

register(
    '8.3.18',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        "SETTLED — व्योर्लघुप्रयत्नतरः शाकटायनस्य — and in ŚĀKAṬĀYANA'S view\n"
        '  that य् — and a व् in the same position — is pronounced with LESS\n'
        '  effort: **भोयत्र, भो अत्र; कयास्ते, क आस्ते; अस्मायुद्धर, अस्मा\n'
        '  उद्धर**. Naming a teacher makes the rule an option in the\n'
        '  language, and both readings stand'
    ),
)

register(
    '8.3.19',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        "SETTLED — लोपः शाकल्यस्य — and in ŚĀKALYA'S view it is dropped\n"
        '  altogether: **क आस्ते, कयास्ते; काक आस्ते; अस्मा उद्धर; द्वा अत्र,\n'
        '  द्वावत्र; असा आदित्यः, असावादित्यः**. This is why a Vedic pada\n'
        '  text and a saṃhitā text differ where they do, and the sūtra is the\n'
        '  reason अ + अ hiatus is heard in recitation at all'
    ),
)

register(
    '8.3.20',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — ओतो गार्ग्यस्य — and after an ओ the य् is dropped in\n'
        "  GĀRGYA'S view: **भो अत्र; भगो अत्र; भो इदम्; भगो इदम्**.\n"
        '\n'
        'SETTLED — **AND HERE NAMING A TEACHER DOES NOT MAKE AN OPTION.**\n'
        '  **नित्यार्थोऽयम् आरम्भः। गार्ग्यग्रहणं पूजार्थम्** — the rule\n'
        '  exists to make the loss COMPULSORY after ओ where 8.3.19 left it\n'
        '  optional, and the name is an honour. It is the same thing 7.3.99\n'
        '  said of Gārgya and Gālava, and the opposite of what 8.3.18 and\n'
        '  8.3.19 do'
    ),
)

register(
    '8.3.21',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — उञि च पदे — and before उञ् STANDING AS A WORD: **स उ\n'
        '  एकविंशवर्तनिः; स उ एकाग्निः**. The पद is what the counter-example\n'
        '  turns on, and the vṛtti adds a nicety about how a उ that has come\n'
        "  from a वे-root's saṃprasāraṇa can still be recognised as the\n"
        '  particle — **भूतपूर्वेण ञकारेण शक्यते प्रत्यभिज्ञातुम्**'
    ),
)

register(
    '8.3.22',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — हलि सर्वेषाम् — and before a CONSONANT the य् is dropped\n'
        "  in EVERY teacher's view: **भो हसति; भगो हसति; अघो याति; वृक्षा\n"
        '  हसन्ति**. **सर्वेषांग्रहणं शाकटायनस्य अपि लोपो यथा स्यात्** —\n'
        '  Śākaṭāyana had only lightened the sound, and saying ALL is what\n'
        '  takes his lighter य् away here. Three sūtras of disagreement close\n'
        '  in one of agreement'
    ),
)

register(
    '8.3.23',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — मोऽनुस्वारः — a word-final म् becomes an anusvāra before a\n'
        '  consonant: **कुण्डं हसति; वनं हसति; कुण्डं याति**. This is the\n'
        '  rule every accusative singular and every neuter nominative in the\n'
        '  language passes through, and both its conditions are tested'
    ),
)

register(
    '8.3.24',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — नश्चापदान्तस्य झलि — and a न् or म् INSIDE a word becomes\n'
        '  an anusvāra before a झल्: **पयांसि, यशांसि, सर्पींषि, धनूंषि**,\n'
        '  and for the म् **आक्रंस्यते, आचिक्रंसते, अधिजिगांसते**. The neuter\n'
        '  plurals of every स्-final stem are made by this rule together with\n'
        "  7.1.72's नुम्"
    ),
)

register(
    '8.3.25',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — मो राजि समः क्वौ — but सम् keeps its म् before राज् with a\n'
        '  क्विप्: **सम्राट्, साम्राज्यम्**. **मकारस्य मकारवचनम्\n'
        '  अनुस्वारनिवृत्त्यर्थम्** — prescribing म् for म् is idle except as\n'
        '  a way of keeping the anusvāra out, which is exactly what it is\n'
        '  for. All three of its conditions are tested'
    ),
)

register(
    '8.3.26',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — हे मपरे वा — and before a ह् that has a म् after it, a म्\n'
        '  optionally stays: **किम् ह्मलयति, किं ह्मलयति; कथम् ह्मलयति**. A\n'
        '  vārttika extends it to three more sounds, one to one: **यवलपरे\n'
        '  यवला वा** — **किय् ह्यः, किं ह्यः; किव् ह्वलति** — so the म् takes\n'
        '  the shape of whatever follows the ह्'
    ),
)

register(
    '8.3.27',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — नपरे नः — and before a ह् with a न् after it, a म्\n'
        '  optionally becomes न्: **किन् ह्नुते, किं ह्नुते; कथन् ह्नुते**.\n'
        '  It is the same assimilation the vārttika on the sūtra before gave\n'
        '  for य्, व् and ल्, stated as a sūtra because न् is the one case\n'
        '  Pāṇini wrote out'
    ),
)

register(
    '8.3.28',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — ङ्णोः कुक्टुक् शरि — a word-final ङ् or ण् optionally\n'
        '  takes a कुक् or a टुक् before a शर्, one to one: **प्राङ्क् शेते,\n'
        '  प्राङ् शेते; प्राङ्क् षष्ठः; वण्ट् शेते, वण् शेते**. The augment\n'
        '  is put at the END of what precedes — **पूर्वान्तकरणम्** — and not\n'
        '  at the head of what follows, which is what makes it audible as\n'
        '  part of प्राङ्क्'
    ),
)

register(
    '8.3.29',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — डः सि धुट् — a स्-initial word after a ड्-final one\n'
        '  optionally takes a धुट्: **श्वलिट्त्साये, श्वलिट् साये;\n'
        '  मधुलिट्त्साये**. The augment goes at the head of the SECOND word —\n'
        "  **परादिकरणम्** — and the reason is given: 8.4.42's refusal of\n"
        '  ष्टुत्व after a word-final ट-class sound would otherwise apply,\n'
        '  and putting the धुट् first keeps the two apart'
    ),
)

register(
    '8.3.30',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — नश्च — and after a न्-final word: **भवान्त्साये, भवान्\n'
        '  साये; महान्त्साये**. And the augment is invisible to the rule that\n'
        '  would have given a रुँ — **धुटश् चर्त्वस्य च असिद्धत्वाद्\n'
        '  नश्छव्यप्रशान् इति रुत्वं न भवति** — so भवान्त्साये keeps its न्\n'
        '  where भवांश्छादयति does not, and the two forms of the same word\n'
        '  are five sūtras apart'
    ),
)

register(
    '8.3.31',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — शि तुक् — a word-final न् optionally takes a तुक् before\n'
        '  श्: **भवाञ्च्छेते**. **पूर्वान्तकरणं छत्वार्थम्** — the augment\n'
        "  goes at the end of the first word so that 6.1.73's छ् can then\n"
        '  come. And the vṛtti raises a difficulty it does not quite settle:\n'
        '  in कुर्वञ्च्छेते the न् is then no longer word-final and the\n'
        '  cerebral would apply, **तत्र समाधिम् आहुः**'
    ),
)

register(
    '8.3.32',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — ङमो ह्रस्वादचि ङमुण्नित्यम् — a vowel after a ङम्-final\n'
        '  word whose ङम् follows a SHORT vowel ALWAYS takes a ङमुट्, and the\n'
        '  three augments match the three sounds one to one:\n'
        '  **प्रत्यङ्ङास्ते** for the ङ्, **वण्णास्ते** for the ण्, and the\n'
        '  न् likewise. This is why a short vowel before a final nasal\n'
        '  doubles it in recitation and a long one does not'
    ),
)

register(
    '8.3.33',
    apply=in_samhita,
    codification=_IN_SAMHITA,
    notes=(
        'SETTLED — मय उञो वो वा — after a मय्, the particle उञ् optionally\n'
        '  becomes व् before a vowel: **शम्वस्तु वेदिः, शमु अस्तु वेदिः;\n'
        '  तद्वस्य परेतः; किम्वावपनम्, किमु आवपनम्**. The alternative is not\n'
        '  a plain hiatus but a प्रगृह्य, which is why the two readings are\n'
        '  heard as far apart as they are'
    ),
)


_THE_VISARGA = (
    'the_visarga(word, gana=..., before=..., sense=..., case=..., '
    'chandasi=...) -> what the visarga becomes and where it '
    'stays, by rule of 8.3.34-54.'
)

register(
    '8.3.34',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — विसर्जनीयस्य सः — the visarga becomes स् before a खर्:\n'
        '  **वृक्षश्छादयति, प्लक्षश्छादयति; वृक्षष्ठकारः; वृक्षस्थकारः;\n'
        '  वृक्षश्चिनोति; वृक्षस्तरति**. The sound heard is then further\n'
        "  shaped by 8.4's rules — श् before a palatal, ष् before a cerebral\n"
        '  — so what this rule gives is a स् that is almost never heard as\n'
        '  one'
    ),
)

register(
    '8.3.35',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — शर्परे विसर्जनीयः — but where the खर् has a शर् after it\n'
        '  the visarga STAYS a visarga: **शशः क्षुरम्; पुरुषः क्षुरम्; अद्भिः\n'
        '  प्सातम्; वासः क्षौमम्; पुरुषः त्सरुः; घनाघनः क्षोभणश्\n'
        '  चर्षणीनाम्**. The rule is stated as a substitute of a sound for\n'
        '  itself, which is the only way to keep 8.3.34 off without a\n'
        '  प्रतिषेध'
    ),
)

register(
    '8.3.36',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — वा शरि — and before a शर् it may do either: **वृक्षः शेते,\n'
        '  वृक्षश्शेते; प्लक्षः शेते; वृक्षः षण्डे, वृक्षष्षण्डे; वृक्षः\n'
        '  साये, वृक्षस्साये**. A vārttika adds a third possibility for a शर्\n'
        '  with a खर् after it — **खर्परे शरि वा लोपः** — which is where the\n'
        '  doubled स् of संस्स्कर्ता becomes single'
    ),
)

register(
    '8.3.37',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — कुप्वोः ≍क≍पौ च — and before a guttural or a labial the\n'
        '  visarga becomes the जिह्वामूलीय or the उपध्मानीय, one to one, and\n'
        '  by the च may also stay: **वृक्ष≍करोति, वृक्षः करोति; वृक्ष≍खनति;\n'
        '  वृक्ष≍पचति**. These are the two sounds Sanskrit writes with a mark\n'
        '  of their own and almost never prints, and the rule is why a\n'
        '  visarga before क् and before प् is not the same sound as one\n'
        '  before त्'
    ),
)

register(
    '8.3.38',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — सोऽपदादौ — the visarga becomes स् where the guttural or\n'
        "  labial does NOT begin a word: **पयस्पाशम्** by 5.3.47's पाशप्,\n"
        "  **पयस्कल्पम्, यशस्कल्पम्** by 5.3.67's कल्पप्, and so for the क\n"
        "  and the काम्य. Four affixes make the whole of the rule's scope,\n"
        '  since only they put a क or a प after a word without beginning one'
    ),
)

register(
    '8.3.39',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — इणः षः — but after an इण् it is ष्: **सर्पिष्पाशम्,\n'
        '  यजुष्पाशम्; सर्पिष्कल्पम्; सर्पिष्कः; सर्पिष्काम्यति**. The pair\n'
        "  8.3.38–39 is the same division 8.3.57's इण्कोः will make of the\n"
        '  whole rest of the pāda, stated here for one sound and four affixes'
    ),
)

register(
    '8.3.40',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — नमस्पुरसोर्गत्योः — नमस् and पुरस्, WHERE THEY ARE\n'
        '  PREVERBS, take स् before a guttural or a labial: **नमस्कर्ता,\n'
        '  नमस्कर्तुम्, नमस्कर्तव्यम्; पुरस्कर्ता**. The condition is the गति\n'
        '  name of 1.4.60 and following, and without it नमः कृत्वा would come\n'
        '  out नमस्कृत्वा'
    ),
)

register(
    '8.3.41',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — इदुदुपधस्य चाप्रत्ययस्य — and a word with इ or उ in its\n'
        '  penult, provided it is not an affix, takes ष्: **निष्कृतम्,\n'
        '  निष्पीतम्; दुष्कृतम्, दुष्पीतम्; बहिष्कृतम्; आविष्कृतम्;\n'
        '  चतुष्कपालम्; प्रादुष्कृतम्**. The Kāśikā lists the words the\n'
        '  condition picks out — निर्, दुर्, बहिर्, आविस्, चतुर्, प्रादुस् —\n'
        '  so the shape is a way of naming six words and not a class'
    ),
)

register(
    '8.3.42',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — तिरसोऽन्यतरस्याम् — तिरस् takes स् only OPTIONALLY:\n'
        '  **तिरस्कर्ता, तिरः कर्ता; तिरस्कर्तुम्, तिरः कर्तुम्**. गतेः is\n'
        '  carried down from 8.3.40, two sūtras back, so the same condition\n'
        '  holds and the only difference between the two rules is that this\n'
        '  one is a choice'
    ),
)

register(
    '8.3.43',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — द्विस्त्रिश्चतुरिति कृत्वोऽर्थे — द्विस्, त्रिस् and चतुर्\n'
        '  take ष् where a NUMBER OF TIMES is meant, optionally:\n'
        '  **द्विष्करोति, द्विःकरोति; त्रिष्करोति; चतुष्करोति**. ष is carried\n'
        '  down from 8.3.41 by अनुवृत्ति — **ष इति सम्बध्यते** — and the\n'
        "  sense is what tells चतुर् 'four times' from the चतुर् of 8.3.41"
    ),
)

register(
    '8.3.44',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — इसुसोः सामर्थ्ये — and an इस्- or उस्-final word where the\n'
        '  two words are CONSTRUED TOGETHER: **सर्पिष्करोति, सर्पिः करोति;\n'
        '  यजुष्करोति, यजुः करोति**. Where they are not — the counter-example\n'
        '  is two whole clauses side by side — no option arises at all, which\n'
        '  is what सामर्थ्य means here'
    ),
)

register(
    '8.3.45',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — नित्यं समासेऽनुत्तरपदस्थस्य — but inside a COMPOUND the ष्\n'
        '  is compulsory, provided the visarga is not standing in the second\n'
        '  member: **सर्पिष्कुण्डिका, धनुष्कपालम्, सर्पिष्पानम्, धनुष्फलम्**.\n'
        '  What was a choice one sūtra back is fixed here, and the difference\n'
        '  between सर्पिः करोति and सर्पिष्कुण्डिका is nothing but the\n'
        '  compounding'
    ),
)

register(
    '8.3.46',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — अतः कृकमिकंसकुम्भपात्रकुशाकर्णीष्वनव्ययस्य — an अ-final\n'
        '  word that is not indeclinable takes स् inside a compound before\n'
        '  seven named words: **अयस्कारः, पयस्कारः** before कृ; **अयस्कामः,\n'
        '  पयस्कामः** before कमि; and so before कंस, कुम्भ, पात्र, कुशा and\n'
        '  कर्णी. The list is one of the longest in the pāda and every one of\n'
        '  its members begins with a guttural or a labial'
    ),
)

register(
    '8.3.47',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — अधःशिरसी पदे — अधस् and शिरस् take स् inside a compound\n'
        '  before पद: **अधस्पदम्, शिरस्पदम्; अधस्पदी, शिरस्पदी**. Both\n'
        '  conditions of the sūtra before are carried down — the compound and\n'
        '  the not-in-the-second-member — and only the list and the following\n'
        '  word are new'
    ),
)

register(
    '8.3.48',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — कस्कादिषु च — and in the कस्कादि class the visarga becomes\n'
        '  स् or ष् as each word requires: **कस्कः; कौतस्कुतः;\n'
        '  भ्रातुष्पुत्रः; शुनस्कर्णः; सद्यस्कालः; सद्यस्क्रीः**. The class\n'
        '  is a list of finished words rather than a shape, which is why the\n'
        '  sūtra can leave यथायोगम् to sort out which of the two sounds each\n'
        '  takes'
    ),
)

register(
    '8.3.49',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — छन्दसि वाऽप्राम्रेडितयोः — and in the VEDA the स् comes\n'
        '  optionally before any guttural or labial, except before प्र and\n'
        '  before an आम्रेडित: **अयःपात्रम्, अयस्पात्रम्; विश्वतः पात्रम्,\n'
        '  विश्वतस्पात्रम्**. This is the widest of the seventeen and the\n'
        '  only one that needs no condition on the word at all'
    ),
)

register(
    '8.3.50',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — कःकरत्करतिकृधिकृतेष्वनदितेः — and in the Veda before five\n'
        '  forms of कृ, unless the word is अदिति: **विश्वतस्कः; विश्वतस्करत्;\n'
        '  पयस्करति; उरु णस् कृधि; ज्योतिष्कृतम्**. Five particular forms of\n'
        '  one root are named where a class would have done, which is what a\n'
        '  Vedic rule of this pāda usually looks like'
    ),
)

register(
    '8.3.51',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        "SETTLED — पञ्चम्याः परावध्यर्थे — an ABLATIVE's visarga becomes स्\n"
        '  before परि in the sense of अधि: **दिवस् परि प्रथमं जज्ञे; अग्निर्\n'
        '  हिमवतस् परि; दिवस् परि**. This is the first of the two sūtras in\n'
        '  the pāda that turn on the CASE of the word rather than on its\n'
        '  shape, and neither has any counterpart outside the Veda'
    ),
)

register(
    '8.3.52',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — पातौ च बहुलम् — and before the root पा it comes VARIOUSLY:\n'
        '  **दिवस् पातु; राज्ञस् पातु** — and **न च भवति — परिषदः पातु**.\n'
        '  बहुलम् here is doing what it always does: recording that the Vedic\n'
        '  corpus has it both ways and declining to say which way is the rule'
    ),
)

register(
    '8.3.53',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        "SETTLED — षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु — and a GENITIVE's\n"
        '  visarga becomes स् before seven named words: **वाचस्पतिं\n'
        '  विश्वकर्माणम् ऊतये; दिवस् पुत्राय सूर्याय**, and so before पृष्ठ,\n'
        '  पार, पद, पयस् and पोष. Every one of the seven begins with प, so\n'
        '  the following sound is the same throughout and it is the case that\n'
        '  does the work'
    ),
)

register(
    '8.3.54',
    apply=the_visarga,
    codification=_THE_VISARGA,
    notes=(
        'SETTLED — इडाया वा — but of इडा it comes only optionally:\n'
        '  **इडायास्पतिः, इडायाः पतिः; इडायास्पुत्रः, इडायाः पुत्रः;\n'
        '  इडायास्पृष्ठम्, इडायाः पृष्ठम्**. One word is taken out of the\n'
        '  sūtra before and given a choice, and with it the run of the\n'
        '  visarga closes'
    ),
)


_THE_CEREBRAL = (
    'the_cerebral(root, gana=..., after=..., before=..., sense=...) '
    '-> the s that becomes cerebral and the dh that becomes dha, '
    'by rule of 8.3.55-89.'
)

register(
    '8.3.55',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — अपदान्तस्य मूर्धन्यः — a heading, and it begins by\n'
        "  cancelling one: **पदाधिकारो निवृत्तः** — 8.1.16's पदस्य stops\n"
        '  here, and NOT-word-final takes its place. **अपदान्तस्य इति\n'
        '  मूर्धन्य इति च एतद् अधिकृतं वेदितव्यम् आ पादपरिसमाप्तेः**, and the\n'
        '  vṛtti proves it on the rule four sūtras later: **सिषेव, सुष्वाप,\n'
        '  अग्निषु, वायुषु**'
    ),
)

register(
    '8.3.56',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — सहेः साडः सः — the स् of सह् IN THE FORM साड् becomes\n'
        '  cerebral: **जलाषाट्, तुराषाट्, पृतनाषाट्**. Both words of the\n'
        '  sūtra are tested — **सहेर् इति किम्? साडिः; साड्ग्रहणं किम्?** —\n'
        '  the first keeping out a word that merely looks like it, the second\n'
        '  confining the rule to the one shape the root takes in a compound'
    ),
)

register(
    '8.3.57',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — इण्कोः — the second heading, and it says what must stand\n'
        '  BEFORE: **इणः कवर्गात् च इत्येवं तद् वेदितव्यम्** — a vowel other\n'
        '  than अ, a semivowel, ह्, or a guttural. **सिषेव, अग्निषु, वायुषु,\n'
        '  कर्तृषु**. Every cerebral of the rest of the pāda wants one of\n'
        '  those in front of it, and this is why the locative plural of अग्नि\n'
        '  has a ष् and that of वृक्ष has not'
    ),
)

register(
    '8.3.58',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — नुम्विसर्जनीयशर्व्यवायेऽपि — and the cerebral reaches\n'
        '  ACROSS a नुम्, a visarga or a शर्: **व्यवायशब्दः प्रत्येकम्\n'
        "  अभिसम्बध्यते**, the word 'intervention' goes with each of the\n"
        '  three. Across a नुम् — **सर्पींषि, यजूंषि, हवींषि** — which is how\n'
        '  every neuter plural of an इस्-final stem is made, the नुम् and the\n'
        '  anusvāra both standing between the इ and the ष्'
    ),
)

register(
    '8.3.59',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — आदेशप्रत्यययोः — a स् that is a SUBSTITUTE or belongs to\n'
        '  an AFFIX becomes cerebral after an इण् or a guttural: **सिषेव,\n'
        '  सुष्वाप** for the substitute, and **अग्निषु, वायुषु, कर्तृषु** for\n'
        '  the affix. **आदेशप्रत्यययोर् इति षष्ठी भेदेन सम्बध्यते** — the two\n'
        '  genitives are read apart and not as one compound. This is the rule\n'
        '  the whole locative plural turns on'
    ),
)

register(
    '8.3.60',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — शासिवसिघसीनां च — and the स् of शास्, वस् and घस्, though\n'
        '  it is neither a substitute nor an affix: **अन्वशिषत्, शिष्टः,\n'
        '  शिष्टवान्** from the first; **उषितः, उषितवान्, उषित्वा** from the\n'
        '  second; **जक्षतुः, जक्षुः** from the third. Three roots added to a\n'
        '  rule that otherwise reaches only what the grammar itself has put\n'
        '  there'
    ),
)

register(
    '8.3.61',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — स्तौतिण्योरेव षण्यभ्यासात् — of स्तु and of the causals,\n'
        '  before a सन् that has a ष् in it, and only after the reduplicated\n'
        '  syllable: **तुष्टूषति**; and for the causals **सिषेचयिषति,\n'
        '  सिषञ्जयिषति, सुष्वापयिषति**. **सिद्धे सत्य् आरम्भो नियमार्थः** —\n'
        '  the cerebral was available anyway and the sūtra is there to\n'
        '  confine it to these two, which is what the एव says'
    ),
)

register(
    '8.3.62',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — सः स्विदिस्वदिसहीनां च — but the causals of स्विद्, स्वद्\n'
        '  and सह् keep a plain स्: **सिस्वेदयिषति, सिस्वादयिषति,\n'
        '  सिसाहयिषति**. **सकारस्य सकारवचनम्** — prescribing स् for स् is\n'
        '  idle except as a way of keeping the cerebral out, which is what it\n'
        '  is for, and it is the same device 8.3.25 used for the म्'
    ),
)

register(
    '8.3.63',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — प्राक्सितादड्व्यवायेऽपि — a third heading, and a short\n'
        '  one: as far as the sūtra that names सित् — which is 8.3.70 — the\n'
        '  cerebral reaches ACROSS the augment अ, **अपिशब्दाद्\n'
        '  अनड्व्यवायेऽपि**, and across nothing as well. Without it every\n'
        '  imperfect and aorist of these roots would lose its cerebral:\n'
        '  **न्यषीदत्, व्यषीदत्, अभ्यष्टभ्नात्**'
    ),
)

register(
    '8.3.64',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — स्थादिष्वभ्यासेन चाभ्यासस्य — and for the स्थादि roots of\n'
        '  the next sūtra the cerebral reaches across the REDUPLICATION as\n'
        "  well, and reaches the reduplication's own स् besides. Two things\n"
        '  at once, and the second is what makes तिष्ठति come out with a ष्\n'
        '  in both syllables where the preverb calls for it'
    ),
)

register(
    '8.3.65',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — उपसर्गात्\n'
        '  सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम् — the स्\n'
        '  of eleven roots becomes cerebral after a PREVERB — that is, after\n'
        "  whatever in the preverb 8.3.57's heading names: **अभिषुणोति,\n"
        '  अभिषुवति, अभिष्यति, अभिष्टौति, अभिष्ठीवति, अभिषिञ्चति, अभिषजति,\n'
        '  परिष्वजते**. It is the longest single list in the pāda and the one\n'
        '  every later preverb rule is stated against'
    ),
)

register(
    '8.3.66',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — सदिरप्रतेः — and the स् of सद् after a preverb OTHER THAN\n'
        '  प्रति: **निषीदति, विषीदति; न्यषीदत्, व्यषीदत्; निषसाद, विषसाद**.\n'
        "  The imperfects come through 8.3.63's heading, and the perfects\n"
        '  show the cerebral reaching across the reduplication as well, which\n'
        "  is 8.3.64's"
    ),
)

register(
    '8.3.67',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — स्तम्भेः — and स्तम्भ्: **अभिष्टभ्नाति, परिष्टभ्नाति;\n'
        '  अभ्यष्टभ्नात्, पर्यष्टभ्नात्; अभितष्टम्भ, परितष्टम्भ**. The three\n'
        '  sets are the present, the imperfect across the augment, and the\n'
        '  perfect across the reduplication — the same three kinds of reach\n'
        '  the two headings before have given'
    ),
)

register(
    '8.3.68',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — अवाच्चालम्बनाविदूर्ययोः — and after अव, but only where\n'
        '  SUPPORT or NEARNESS is meant: **आलम्बनम् आश्रयणम्। अविदूरस्य भाव\n'
        '  आविदूर्यम्**. **अवष्टभ्यास्ते; अवष्टभ्य**. अव is a preverb like\n'
        '  any other, so 8.3.67 would have reached it — the sūtra exists to\n'
        '  put a sense-condition on that one preverb and no other'
    ),
)

register(
    '8.3.69',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — वेश्च स्वनो भोजने — and the स् of स्वन् after वि and अव\n'
        '  where EATING is meant: **विष्वणति, व्यष्वणत्, विषष्वाण; अवष्वणति,\n'
        '  अवाष्वणत्**. The vṛtti glosses the sense narrowly —\n'
        '  **अभ्यवहारक्रियाविशेषोऽभिधीयते** — a particular way of taking\n'
        '  food, and not sound, which is what the root ordinarily means'
    ),
)

register(
    '8.3.70',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम् — the स् of\n'
        '  eight roots becomes cerebral after परि, नि and वि: **परिषेवते,\n'
        '  निषेवते, विषेवते; पर्यषेवत, न्यषेवत, व्यषेवत**. This is the last\n'
        "  sūtra that names सित्, so 8.3.63's heading — the one that lets the\n"
        '  cerebral cross the augment — stops with it, and the imperfects\n'
        '  above are the last that come through it as of right'
    ),
)

register(
    '8.3.71',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — सिवादीनां वाऽड्व्यवायेऽपि — and for the last five of those\n'
        '  eight the cerebral crosses the augment only OPTIONALLY: **तथा च एव\n'
        '  उदाहृतम्** — the vṛtti simply points back at the forms it has just\n'
        "  given. With 8.3.63's heading over, what was compulsory becomes a\n"
        '  choice, and the sūtra is the hinge between the two'
    ),
)

register(
    '8.3.72',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु — the स् of स्यन्द्\n'
        '  after five preverbs, OPTIONALLY, and only where what flows is not\n'
        '  alive: **अनुष्यन्दते, विष्यन्दते, परिष्यन्दते, अभिष्यन्दते तैलम्,\n'
        '  निष्यन्दते**. Oil flows and a beast does not, which is the whole\n'
        '  of the condition'
    ),
)

register(
    '8.3.73',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — वेः स्कन्देरनिष्ठायाम् — and स्कन्द् after वि, optionally,\n'
        '  but not in a निष्ठा: **विष्कन्ता, विस्कन्ता; विष्कन्तुम्,\n'
        '  विस्कन्तुम्; विष्कन्तव्यम्, विस्कन्तव्यम्**. The exception is what\n'
        '  keeps the past participle out, and the option is what makes both\n'
        '  agent nouns stand'
    ),
)

register(
    '8.3.74',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — परेश्च — and after परि: **परिष्कन्ता, परिस्कन्ता;\n'
        '  परिष्कन्तुम्; परिष्कन्तव्यम्**. **पृथग्योगकरणसामर्थ्यात्** —\n'
        '  making it a separate sūtra rather than adding परि to the one\n'
        '  before is what lets the निष्ठा exception NOT be carried down, so\n'
        '  परिष्कण्णः stands where विस्कन्नः does not'
    ),
)

register(
    '8.3.75',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — परिस्कन्दः प्राच्यभरतेषु — **परिस्कन्दः** is laid down\n'
        '  WITHOUT the cerebral, as the eastern Bharatas use it: **पूर्वेण\n'
        '  मूर्धन्ये प्राप्ते तदभावो निपात्यते**. The sūtra before had just\n'
        "  given the ष्, and this takes it away again in one region's usage —\n"
        '  the only geographical condition in the whole pāda'
    ),
)

register(
    '8.3.76',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — स्फुरतिस्फुलत्योर्निर्निविभ्यः — and स्फुर् and स्फुल्\n'
        '  after निस्, नि and वि, optionally: **निष्ष्फुरति, निस्स्फुरति;\n'
        '  निष्फुरति, निस्फुरति; विष्फुरति, विस्फुरति**. Four forms for one\n'
        '  word, since the doubled and the single स् are themselves an option\n'
        "  of 8.4's"
    ),
)

register(
    '8.3.77',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — वेः स्कभ्नातेर्नित्यम् — but स्कभ् after वि takes it\n'
        '  ALWAYS: **विष्कभ्नाति, विष्कम्भिता, विष्कम्भितुम्,\n'
        '  विष्कम्भितव्यम्**. The word नित्यम् is there because everything\n'
        '  around it is optional — three sūtras before and one after — and\n'
        '  without it the option would have been carried down'
    ),
)

register(
    '8.3.78',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — इणः षीध्वंलुङ्लिटां धोऽङ्गात् — and here it is a ध् and\n'
        '  not a स् that goes cerebral: after a stem ending in इण्, the ध् of\n'
        '  षीध्वम् and of the aorist and perfect endings becomes ढ्:\n'
        '  **च्योषीढ्वम्, प्लोषीढ्वम्; अच्योढ्वम्, अप्लोढ्वम्; चकृढ्वे,\n'
        '  चकृढ्वम्**. One sūtra in the middle of a run about the स्, and the\n'
        '  reason is the same इण् in front'
    ),
)

register(
    '8.3.79',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — विभाषेटः — and after an इट् it is OPTIONAL: **लविषीढ्वम्,\n'
        '  लविषीध्वम्; पविषीढ्वम्, पविषीध्वम्; अलविढ्वम्, अलविध्वम्**. The\n'
        '  second of each pair is what 8.2.25 धि च was stated for — the\n'
        "  aorist's स् goes so that the ध् may be heard at all — so the two\n"
        '  pādas meet in one form'
    ),
)

register(
    '8.3.80',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — समासेऽङ्गुलेः सङ्गः — the स् of सङ्ग becomes cerebral\n'
        '  after अङ्गुलि inside a COMPOUND: **अङ्गुलिषङ्गः; अङ्गुलिषङ्गा\n'
        '  यवागूः; अङ्गुलिषङ्गो गाः सादयति**. Seven sūtras of this kind\n'
        '  follow, each naming one first member and one second, and each\n'
        '  wanting the compound'
    ),
)

register(
    '8.3.81',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — भीरोः स्थानम् — and स्थान after भीरु: **भीरुष्ठानम्**.\n'
        '  **समास इत्येव** — the compound is carried down from the sūtra\n'
        '  before and is what tells भीरुष्ठानम् from भीरोः स्थानम्'
    ),
)

register(
    '8.3.82',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — अग्नेः स्तुत्स्तोमसोमाः — and स्तुत्, स्तोम and सोम after\n'
        '  अग्नि: **अग्निष्टुत्, अग्निष्टोमः, अग्नीषोमौ**. The third is\n'
        '  different from the other two — **अग्नेर् दीर्घात् सोमस्य इष्यते**\n'
        '  — the cerebral coming only where अग्नि has been lengthened, which\n'
        '  is why the pair of gods is अग्नीषोमौ and not *अग्निषोमौ'
    ),
)

register(
    '8.3.83',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — ज्योतिरायुषः स्तोमः — and स्तोम after ज्योतिस् and आयुस्:\n'
        '  **ज्योतिष्टोमः, आयुष्टोमः**. Both first members end in स्, which\n'
        "  by 8.3.15 is a visarga and by 8.3.57's heading is not an इण् — so\n"
        "  the rule is needed where 8.3.82's was not"
    ),
)

register(
    '8.3.84',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — मातृपितृभ्यां स्वसा — and स्वसृ after मातृ and पितृ:\n'
        "  **मातृष्वसा, पितृष्वसा**. The ऋ is an इण्, so 8.3.57's heading is\n"
        '  met; what the sūtra adds is that the स् is neither a substitute\n'
        '  nor an affix and so would not have been reached by 8.3.59'
    ),
)

register(
    '8.3.85',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — मातुःपितुर्भ्यामन्यतरस्याम् — and after the forms मातुर्\n'
        '  and पितुर् it is OPTIONAL: **मातुःष्वसा, मातुःस्वसा; पितुःष्वसा,\n'
        '  पितुःस्वसा**. **मातुःपितुर् इति रेफान्तयोर् एतद् रूपम्** — these\n'
        '  are the र्-final shapes of the same two words, and the difference\n'
        '  between the two sūtras is nothing but which shape the first member\n'
        '  has'
    ),
)

register(
    '8.3.86',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — अभिनिसः स्तनः शब्दसंज्ञायाम् — and स्तन after अभिनिस्,\n'
        '  optionally, where a SOUND is being named: **अभिनिष्टानो वर्णः,\n'
        '  अभिनिस्तानो वर्णः; अभिनिष्टानो विसर्जनीयः**. The word is a\n'
        '  technical term of the phoneticians, and the sūtra exists for the\n'
        "  grammar's own vocabulary"
    ),
)

register(
    '8.3.87',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — उपसर्गप्रादुर्भ्यामस्तिर्यच्परः — and the स् of अस् after\n'
        '  a preverb or after प्रादुस्, when a य् or a vowel follows it:\n'
        '  **अभिषन्ति, निषन्ति, विषन्ति, प्रादुःषन्ति; अभिष्यात्, निष्यात्**.\n'
        '  Two conditions on what precedes and two on what follows, for one\n'
        '  of the commonest roots in the language'
    ),
)

register(
    '8.3.88',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — सुविनिर्दुर्भ्यः सुपिसूतिसमाः — and सुपि, सूति and सम\n'
        '  after सु, वि, निर् and दुर्: **सुषुप्तः, विषुप्तः, निःषुप्तः,\n'
        '  दुःषुप्तः**. The first is स्वप् with its saṃprasāraṇa already made\n'
        '  — **सुपि इति स्वपिः कृतसम्प्रसारणो गृह्यते** — so the rule reaches\n'
        '  a shape the root list does not have'
    ),
)

register(
    '8.3.89',
    apply=the_cerebral,
    codification=_THE_CEREBRAL,
    notes=(
        'SETTLED — निनदीभ्यां स्नातेः कौशले — and the स् of स्ना after नि and\n'
        '  after नदी, where SKILL is meant: **निष्णातः कटकरणे; निष्णातो\n'
        '  रज्जुवर्तने** — expert at mat-making, expert at rope-twisting. And\n'
        "  **नद्यां स्नातीति नदीष्णः**, where 3.2.4's सुपि स्थः gives the\n"
        '  second member its shape'
    ),
)


_ALSO_CEREBRAL = (
    'also_cerebral(root, gana=..., after=..., before=..., '
    'sense=..., view=..., chandasi=...) -> the last of the '
    'cerebrals and the ten refusals, by rule of 8.3.90-119.'
)

register(
    '8.3.90',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सूत्रं प्रतिष्णातम् — **प्रतिष्णातम्** is laid down where\n'
        '  THREAD is meant: **प्रतिष्णातं सूत्रम्**, **शुद्धम् इत्यर्थः** —\n'
        '  clean. Anywhere else the plain प्रतिस्नातम् stands, and the pair\n'
        '  is the shape every one of the five laid-down words of this run has'
    ),
)

register(
    '8.3.91',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — कपिष्ठलो गोत्रे — and **कपिष्ठल** as a FAMILY NAME:\n'
        '  **कपिष्ठलो नाम स यस्य कापिष्ठलिः पुत्रः** — the man whose son is\n'
        '  called Kāpiṣṭhali. The counter-example takes the word apart into\n'
        '  its two members and shows it means something else entirely'
    ),
)

register(
    '8.3.92',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — प्रष्ठोऽग्रगामिनि — and **प्रष्ठ** of one who goes IN\n'
        '  FRONT: **प्रतिष्ठत इति प्रष्ठोऽश्वः। अग्रतो गच्छति इत्यर्थः** —\n'
        '  the lead horse of a team. The two counter-examples are a plateau\n'
        '  of the Himālaya and a dry measure, and neither takes the cerebral'
    ),
)

register(
    '8.3.93',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — वृक्षासनयोर्विष्टरः — and **विष्टर** of a TREE or a SEAT:\n'
        '  **विष्टरो वृक्षः; विष्टरम् आसनम्**. **विपूर्वस्य स्तृणातेः षत्वं\n'
        '  निपात्यते** — it is वि plus स्तॄ, and what is laid down is the\n'
        '  cerebral, the rest of the word coming as usual'
    ),
)

register(
    '8.3.94',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — छन्दोनाम्नि च — and **विष्टार** as the NAME OF A METRE.\n'
        '  The vṛtti works out where the long आ comes from: the घञ् of\n'
        '  3.3.34, which is itself given **छन्दोनाम्नि च** — so two sūtras\n'
        '  with the same four syllables, five adhyāyas apart, make one word\n'
        '  between them'
    ),
)

register(
    '8.3.95',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — गवियुधिभ्यां स्थिरः — the स् of स्थिर becomes cerebral\n'
        '  after गवि and युधि: **गविष्ठिरः, युधिष्ठिरः**. And the laying-down\n'
        '  buys something besides — **गोशब्दाद् अहलन्ताद् अपि एतस्माद् एव\n'
        '  निपातनात् सप्तम्या अलुग् भवति** — the locative ending of गो\n'
        '  survives inside the compound, which no ordinary rule allows'
    ),
)

register(
    '8.3.96',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — विकुशमिपरिभ्यः स्थलम् — and स्थल after वि, कु, शमि and\n'
        '  परि: **विष्ठलम्, कुष्ठलम्, शमिष्ठलम्, परिष्ठलम्**. Four first\n'
        '  members and one second, and the sūtra says nothing else — which is\n'
        '  what most of this stretch looks like'
    ),
)

register(
    '8.3.97',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED —\n'
        '  अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गुमञ्जिपुञ्जिपरमेबर्हिर्दिव्यग्निभ्यः\n'
        '  स्थः — and स्थ after eighteen named first members: अम्ब, आम्ब, गो,\n'
        '  भूमि, सव्य, अप्, द्वि, त्रि, कु, शेकु, शङ्कु, अङ्, गु, मञ्जि,\n'
        '  पुञ्जि, परमे, बर्हिस्, दिवि and अग्नि. **अम्बष्ठः** and the rest.\n'
        '  It is the longest compound in the pāda and one of the longest in\n'
        '  the work'
    ),
)

register(
    '8.3.98',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सुषामादिषु च — and in the सुषामादि class: **शोभनं साम यस्य\n'
        '  असौ सुषामा ब्राह्मणः; दुष्षामा; निष्षामा; निष्षेधः; दुष्षेधः**.\n'
        '  The first is worth the sūtra on its own — सु is a कर्मप्रवचनीय\n'
        '  there and not a preverb, so none of the preverb rules of 8.3.65–89\n'
        '  could have reached it'
    ),
)

register(
    '8.3.99',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — ऐति संज्ञायामगात् — a स् before an ए becomes cerebral in a\n'
        '  NAME, provided what stands before is not a ग: **हरिषेणः, वारिषेणः,\n'
        '  जानुषेणी**. Three conditions at once — the following ए, the name,\n'
        '  and the ग excepted — and the vṛtti tests two of them'
    ),
)

register(
    '8.3.100',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — नक्षत्राद्वा — and after the name of a CONSTELLATION it is\n'
        '  optional: **रोहिणीषेणः, रोहिणीसेनः; भरणीषेणः, भरणीसेनः**. The\n'
        '  exception for a ग is carried down — **अगकाराद् इत्येव** — so\n'
        '  शतभिषक्सेनः has neither form'
    ),
)

register(
    '8.3.101',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — ह्रस्वात् तादौ तद्धिते — and after a SHORT vowel before a\n'
        '  त-initial taddhita: **सर्पिष्टरम्, यजुष्टरम्; सर्पिष्टमम्**. The\n'
        '  vṛtti lists the seven affixes the rule can reach — तरप्, तमप्, तय,\n'
        '  त्व, तल्, तस्, त्यप् — which is a way of saying that तादौ तद्धिते\n'
        '  is a smaller class than it looks'
    ),
)

register(
    '8.3.102',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — निसस्तपतावनासेवने — and the स् of निस् before तप् where\n'
        '  the action is NOT REPEATED: **आसेवनं पुनःपुनः करणम्। निष्टपति\n'
        '  सुवर्णम्। सकृद् अग्निं स्पर्शयति इत्यर्थः** — he puts the gold to\n'
        '  the fire once. Doing it over and over gives निस्तपति, with no\n'
        '  cerebral'
    ),
)

register(
    '8.3.103',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — युष्मत्तत्ततक्षुःष्वन्तःपादम् — and before the forms of\n'
        '  युष्मद्, before तद् and before ततक्षुस्, provided the स् stands\n'
        '  WITHIN a metrical quarter: **अग्निष् ट्वं नामासीत्**. The\n'
        '  युष्मद्-forms meant are its substitutes — त्वम्, त्वाम्, ते, तव —\n'
        '  so the rule names a paradigm by naming its stem'
    ),
)

register(
    '8.3.104',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        "SETTLED — यजुष्येकेषाम् — and in the YAJUS, in SOME TEACHERS' view:\n"
        '  **अर्चिर्भिष् ट्वम्, अर्चिर्भिस्त्वम्; अग्निष् टेऽग्रम्**. एकेषाम्\n'
        '  is the first of three such namings in a row, and it does what\n'
        '  naming a teacher always does — makes the rule an option and leaves\n'
        '  both readings standing'
    ),
)

register(
    '8.3.105',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — स्तुतस्तोमयोश्छन्दसि — and of स्तुत and स्तोम in the Veda,\n'
        "  in some teachers' view: **त्रिभिष्टुतस्य, त्रिभिस्तुतस्य;\n"
        '  गोष्टोमम्**. एकेषाम् is carried down from the sūtra before rather\n'
        '  than said again, which is how the three make one block'
    ),
)

register(
    '8.3.106',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — पूर्वपदात् — and after a FIRST MEMBER, in the Veda, in\n'
        "  some teachers' view: **द्विषन्धिः, द्विसन्धिः**. This is the\n"
        '  widest of the three and the one that makes the other two nearly\n'
        '  unnecessary — which is presumably why all three are given as\n'
        "  somebody's opinion rather than as the grammar's own"
    ),
)

register(
    '8.3.107',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सुञः — and of the particle सुञ्: **अभी षु णः सखीनाम्;\n'
        '  ऊर्ध्व ऊ षु ण ऊतये**. The particle is picked out by name because\n'
        '  it is a particle and not a first member in any ordinary sense, and\n'
        '  पूर्वपदात् is carried down all the same'
    ),
)

register(
    '8.3.108',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सनोतेरनः — and of सन्, provided the word does not end in\n'
        '  अन्: **गोषाः, नृषाः**. **पूर्वपदाद् इत्येव सिद्धे** — the sūtra\n'
        '  before would have given it anyway, and what this adds is the\n'
        '  exception'
    ),
)

register(
    '8.3.109',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सहेः पृतनर्ताभ्यां च — and of सह् after पृतना and ऋत:\n'
        '  **पृतनाषाहम्, ऋताषाहम्**. **केचित् सहेः इति योगविभागं कुर्वन्ति**\n'
        '  — some split the sūtra in two so that सहेः stands alone and\n'
        '  reaches ऋतीषहम् besides, which the Kāśikā records without adopting'
    ),
)

register(
    '8.3.110',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम् — and here the pāda\n'
        '  turns: a स् with a र् before it does NOT become cerebral, nor the\n'
        '  स् of सृप्, सृज्, स्पृश्, स्पृह् or the सवनादि: **विस्रंसिकायाः;\n'
        '  विस्रब्धः कथयति; पुनःसृजति**. Ten sūtras of refusal follow, and\n'
        '  this is the widest of them'
    ),
)

register(
    '8.3.111',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सात्पदाद्योः — nor of सात्, nor of a स् that BEGINS a\n'
        '  word: **अग्निसात्, दधिसात्**. The sūtra is needed because the two\n'
        '  would have been reached for two different reasons —\n'
        '  **प्रत्ययसकारत्वात् प्राप्तिः, पदादेश् च आदेशसकारत्वात्** — the\n'
        "  first as an affix's स् and the second as a substitute's, which are\n"
        "  exactly 8.3.59's two halves"
    ),
)

register(
    '8.3.112',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        "SETTLED — सिचो यङि — nor of the aorist's स् before यङ्: **सेसिच्यते,\n"
        '  अभिसेसिच्यते**. And the vṛtti sorts out which of two refusals is\n'
        '  doing the work — **उपसर्गात् इति या प्राप्तिः सा पदादिलक्षणम् एव\n'
        '  प्रतिषेधं बाधते, न सिचो यङि इति** — the preverb rule is held off\n'
        "  by 8.3.111's word-head refusal and not by this one"
    ),
)

register(
    '8.3.113',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सेधतेर्गतौ — nor of सेध् where MOTION is meant:\n'
        '  **अभिसेधयति गाः; परिसेधयति गाः** — he drives the cattle. Of\n'
        '  forbidding the cerebral stands: **प्रतिषेधयति**. One root, two\n'
        '  senses, and the commonest word for a prohibition in the grammar\n'
        '  itself is on the other side of the line'
    ),
)

register(
    '8.3.114',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — प्रतिस्तब्धनिस्तब्धौ च — and **प्रतिस्तब्धः** and\n'
        '  **निस्तब्धः** are laid down without it: **स्तन्भेः इति प्राप्तं\n'
        '  षत्वं प्रतिषिध्यते** — 8.3.67 had given स्तम्भ् the cerebral after\n'
        '  any preverb, and these two words are taken out of it by name'
    ),
)

register(
    '8.3.115',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सोढः — nor of सह् IN THE SHAPE सोढ्: **परिसोढा, परिसोढुम्,\n'
        '  परिसोढव्यम्**. **सोड्भूतग्रहणं किम्? परिषहते** — the same root\n'
        '  after the same preverb takes the cerebral wherever it has not\n'
        '  become सोढ्, so the refusal is of one shape and not of a root'
    ),
)

register(
    '8.3.116',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — स्तम्भुसिवुसहां चङि — nor of स्तम्भ्, सिव् and सह् before\n'
        '  चङ्: **स्तन्भेः इति परिनिविभ्यः इति च प्राप्तो मूर्धन्यः\n'
        '  प्रतिषिध्यते**. Two earlier rules had reached these three roots\n'
        '  and this holds both off at once, in the causal aorist alone'
    ),
)

register(
    '8.3.117',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सुनोतेः स्यसनोः — nor of सु before स्य and सन्:\n'
        '  **अभिसोष्यति, परिसोष्यति; अभ्यसोष्यत्**. And the vṛtti asks what\n'
        '  the सन् is for and answers that it is for nothing — **सनि किम्\n'
        "  उदाहरणम्? सुसूषति। न एतद् अस्ति प्रयोजनम्** — 8.3.61's नियम having\n"
        '  already kept the cerebral out there'
    ),
)

register(
    '8.3.118',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — सदिष्वञ्जोः परस्य लिटि — and in the PERFECT of सद् and\n'
        '  ष्वञ्ज् the LATER स् does not take it: **अभिषसाद, परिषसाद, निषसाद,\n'
        '  विषसाद; परिषस्वजे, परिषस्वजाते, परिषस्वजिरे**. In each the first\n'
        "  स् is cerebral and the reduplication's is not — one word with the\n"
        '  same sound twice and the rule reaching only one of them'
    ),
)

register(
    '8.3.119',
    apply=also_cerebral,
    codification=_ALSO_CEREBRAL,
    notes=(
        'SETTLED — निव्यभिभ्योऽड्व्यवाये वा छन्दसि — and in the Veda, after\n'
        '  नि, वि and अभि, the cerebral OPTIONALLY does not reach across the\n'
        '  augment: **न्यषीदत् पिता नः, न्यसीदत्; व्यषीदत्, व्यसीदत्**.\n'
        "  8.3.63's heading had made that reach compulsory, and the pāda\n"
        '  closes by making it a choice in one register — which is where it\n'
        '  began, 8.3.8 having done the same thing for the रुँ'
    ),
)


__all__ = [
    'also_cerebral',
    'in_samhita',
    'kharavasanayoh',
    'the_cerebral',
    'the_visarga',
]
