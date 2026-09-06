# -*- coding: utf-8 -*-
"""
अध्याय ४, पाद ३ — the affixes of time, and then the senses come back.

4.2 inverted itself at 4.2.93: after ninety-one rules that named a
case and a sense and left the affix to 4.1.83, the rules began naming
only their bases, and the vṛtti promised that the senses and the cases
would be stated later. 4.3.25 तत्र जातः is where the promise is kept,
and it names no affix at all — यथाविहितम्, whichever was already
prescribed.

Before it, 4.3.11 कालाट् ठञ् opens a heading of its own and its vṛtti
says where it stops. And 4.3.1 opens the pāda by recording that the
last heading is over: देशाधिकारो निवृत्तः.
"""

from __future__ import annotations

from src.astadhyayi.kala_taddhita import born_in
from src.astadhyayi.sources import register

_RULES = {
    '4.3.1': (
        'SETTLED — युष्मदस्मदोरन्यतरस्यां खञ् च. **देशाधिकारो निवृत्तः** —\n'
        '  the country-heading that opened at 4.2.119 has lapsed,\n'
        '  and the first vṛtti of the new pāda records it before\n'
        '  saying anything else. चकाराच् छश्च, and\n'
        '  **अन्यतरस्यांग्रहणाद् यथाप्राप्तम्** lets अण् in\n'
        '  besides: **तदेते त्रयः प्रत्यया भवन्ति**. यौष्माकीणः,\n'
        '  आस्माकीनः; युष्मदीयः, अस्मदीयः; यौष्माकः, आस्माकः.\n'
        '\n'
        'SETTLED — AND यथासंख्य FAILS BECAUSE THE NUMBERS DO NOT\n'
        '  MATCH. तत्र **वैषम्याद् यथासंख्यं न भवति** — two bases\n'
        "  and three affixes, so 1.3.10's pairing cannot run and\n"
        '  each base takes all three. 4.2.80 matched seventeen\n'
        '  affixes with seventeen lists; two against three matches\n'
        '  with nothing, and the rule is read distributively\n'
        '  instead. **प्रत्येकं प्रत्ययत्रयं विधीयते.**\n'
        '\n'
        'NOTE — त्यदादित्वाद् वृद्धसंज्ञकयोर्युष्मदस्मदोश्छे\n'
        '  प्राप्ते: both words are वृद्ध not by their own first\n'
        "  vowel but by being त्यदादि, so 4.2.114's छ was already\n"
        '  coming. The same argument 4.2.115 made about भवत्.'
    ),
    '4.3.2': (
        'SETTLED — तस्मिन्नणि च युष्माकास्माकौ. यौष्माकीणः, आस्माकीनः;\n'
        '  यौष्माकः, आस्माकः. तस्मिन्नणि चेति किम्? युष्मदीयः,\n'
        '  अस्मदीयः.\n'
        '\n'
        'SETTLED — A PRONOUN PICKING OUT ONE OF TWO AFFIXES BY HOW\n'
        '  EACH OF THEM GOT THERE. **तस्मिन्निति साक्षाद् विहितः\n'
        '  खञ् निर्दिश्यते, न चकारानुकृष्टश्छः** — *that* means\n'
        '  the खञ् the last rule ENJOINED, not the छ its च dragged\n'
        '  in. Two affixes equally present in the previous rule,\n'
        '  and a demonstrative reaching only the one that was\n'
        '  stated outright.\n'
        '\n'
        'SETTLED — AND A SPLIT MADE TO STOP A CORRESPONDENCE.\n'
        '  **निमित्तयोरादेशौ प्रति यथासंख्यं कस्माद् न भवति?** If\n'
        '  the two substitutes pair with the two bases, why do\n'
        '  they not also pair with the two affixes खञ् and अण्?\n'
        '  **योगविभागः करिष्यते** — the rule is read as two:\n'
        '  *in that खञ्, these two for those two*, and then *and\n'
        '  in अण् too*. The instrument met at 4.3.21 as well, and\n'
        '  used there for the opposite purpose.'
    ),
    '4.3.3': (
        'SETTLED — तवकममकावेकवचने. तावकीनः, मामकीनः; तावकः, मामकः.\n'
        '  तस्मिन्नणि चेत्येव — त्वदीयः, मदीयः. And the pairing\n'
        '  between the two CAUSES is stopped here for the same\n'
        '  reason as in the rule before.\n'
        '\n'
        'SETTLED — A TECHNICAL TERM READ UNTECHNICALLY TO ESCAPE A\n'
        '  PARIBHĀṢĀ. ननु च **न लुमताङ्गस्य** [1.1.63] इति\n'
        '  प्रत्ययलक्षणप्रतिषेधाद् एकवचनपरता युष्मदस्मदोर्न\n'
        '  संभवति? — the singular ending has been elided, and\n'
        '  1.1.63 forbids treating an affix as still present once\n'
        '  a लुमत् rule has removed it. So the base cannot be\n'
        '  *followed by a singular* at all, and the rule has no\n'
        '  ground to stand on.\n'
        '\n'
        '  Two answers. **वचनात् प्रत्ययलक्षणं भविष्यति** — the\n'
        "  rule's own statement restores what the paribhāṣā took\n"
        '  away. Or, better, **नैवेदं प्रत्ययग्रहणम्; किं तर्हि?\n'
        '  अन्वर्थग्रहणम्**: एकवचन here is not the NAME 1.4.102\n'
        '  gave an ending but the two words read for what they\n'
        '  mean — *denoting one thing*. एकवचने युष्मदस्मदी\n'
        '  एकस्यार्थस्य वाचके. A term the grammar defined, taken\n'
        '  in this one rule the way anybody would take it, and the\n'
        '  paribhāṣā never gets a purchase.'
    ),
    '4.3.4': (
        'SETTLED — अर्धाद् यत्, अणोऽपवादः. अर्ध्यम्.\n'
        '\n'
        'NOTE — **सपूर्वपदाट् ठञ् वक्तव्यः**, a vārttika: where\n'
        '  something stands in front, ठञ् instead. बालेयार्धिकम्,\n'
        '  गौतमार्धिकम्. The same word, and the affix decided by\n'
        '  whether it is standing alone.'
    ),
    '4.3.5': (
        'SETTLED — परावराधमोत्तमपूर्वाच्च. परार्ध्यम्, अवरार्ध्यम्,\n'
        '  अधमार्ध्यम्, उत्तमार्ध्यम्.\n'
        '\n'
        'SETTLED — ONE WORD SPENT BECAUSE TWO OF THE FOUR HAVE A\n'
        '  SECOND LIFE. **पूर्वग्रहणं किम्?** Why say *preceded\n'
        '  by*, when अर्धात् carries over and the four could have\n'
        '  been named in the ablative? Because **परावरशब्दौ\n'
        '  अदिग्ग्रहणावपि स्तः** — पर and अवर are ordinary words\n'
        '  too, परं सुखम्, अवरं सुखम्, and they are\n'
        '  direction-words besides. **तत्र कृतार्थत्वाद्\n'
        '  दिक्छब्दपक्षे परेण ठञ्यतौ स्याताम्**: read as\n'
        '  directions they fall under the next rule, which would\n'
        '  give ठञ् as well. The one word पूर्व secures यत् alone\n'
        '  — परार्ध्यम्, अवरार्ध्यम्.'
    ),
    '4.3.6': (
        'SETTLED — दिक्पूर्वपदाट् ठञ् च, अणोऽपवादः. पौर्वार्धिकम् beside\n'
        '  पूर्वार्ध्यम्; दाक्षिणार्धिकम् beside दक्षिणार्ध्यम् —\n'
        '  the च bringing यत् along, so both stand.\n'
        '\n'
        'NOTE — **पदग्रहणं स्वरूपविधिनिवारणार्थम्**: *word* is\n'
        '  there so that the rule is not read as being about the\n'
        '  word दिश् itself. 4.2.107 spent the same word on the\n'
        '  same argument, and 1.1.68 is why either was needed.'
    ),
    '4.3.7': (
        'SETTLED — ग्रामजनपदैकदेशादञ्ठञौ, दिक्पूर्वपदादित्येव;\n'
        '  **यतोऽपवादौ** — both of them beat the यत् of the rule\n'
        '  before. इमे खल्वस्माकं ग्रामस्य जनपदस्य वा पौर्वार्धाः,\n'
        '  पौर्वार्धिकाः; दाक्षिणार्धाः, दाक्षिणार्धिकाः. A PART\n'
        '  of a village or of a district, named by the direction\n'
        '  it lies in, and two affixes for it with no option\n'
        '  stated, so both stand.'
    ),
    '4.3.8': (
        'SETTLED — मध्यान्मः, अणोऽपवादः. मध्यमः.\n'
        '\n'
        'NOTE — two vārttikas ride with it. **आदेश्चेति\n'
        '  वक्तव्यम्** — आदिम, on the same pattern. And\n'
        '  **अवोऽधसोर्लोपश्च**: from अव and अधस् with the final\n'
        '  dropped, अवमम् and अधमम्. Three of the commonest\n'
        '  ordinals in the language, made by one affix and two\n'
        '  supplements to it.'
    ),
    '4.3.9': (
        'SETTLED — अ साम्प्रतिके, मस्यापवादः. The sense is glossed with five\n'
        '  words at once: **सांप्रतिकं न्याय्यं युक्तम् उचितं\n'
        '  सममुच्यते** — fitting, proper, apt, becoming, even.\n'
        '  नातिदीर्घं नातिह्रस्वं **मध्यं काष्ठम्**, a stick\n'
        '  neither too long nor too short; नात्युत्कृष्टो\n'
        '  नात्यवकृष्टो **मध्यो वैयाकरणः**, a grammarian neither\n'
        '  outstanding nor bad; मध्या स्त्री. The affix is a bare\n'
        '  अ and the whole rule is three syllables long.'
    ),
    '4.3.10': (
        'SETTLED — द्वीपादनुसमुद्रं यञ्. An island NEAR THE SEA —\n'
        '  समुद्रसमीपे यो द्वीपः. **कच्छादिपाठाद् अणो\n'
        "  मनुष्यवुञश्चापवादः**: द्वीप is in 4.2.133's कच्छादि\n"
        "  list, so this rule has to beat both that rule's अण्\n"
        "  and 4.2.134's वुञ्. द्वैप्यम्, and a line quoted for\n"
        '  it — **द्वैप्यं भवन्तोऽनुचरन्ति चक्रम्**.\n'
        '\n'
        'NOTE — अनुसमुद्रमिति किम्? **द्वैपकम्**, which is\n'
        "  4.2.134's form; **द्वैपमन्यत्**, and 4.2.133's for\n"
        '  everything else. One word taking three different\n'
        '  affixes by three rules in two pādas, and the condition\n'
        '  that separates them is how far it is from the sea.'
    ),
    '4.3.11': (
        'SETTLED — कालाट् ठञ्, अणोऽपवादः; **वृद्धात् तु छं परत्वाद्\n'
        "  बाधते**, and it beats 4.2.114's छ by standing later.\n"
        '  मासिकः, आर्धमासिकः, सांवत्सरिकः.\n'
        '\n'
        'SETTLED — AND A FIGURATIVE TIME IS STILL A TIME.\n'
        '  यथाकथंचिद् **गुणवृत्त्यापि काले वर्तमानात् प्रत्यय\n'
        '  इष्यते** — the affix is wanted even from a word that\n'
        '  denotes a time only by transferring a quality to it.\n'
        '  **कादम्बपुष्पिकम्**, of the kadamba-blossom season;\n'
        '  **ब्रैहिपलालिकम्**, of the rice-straw season. The\n'
        '  season named by what happens in it, and the grammar\n'
        '  admitting the transfer rather than requiring a\n'
        '  time-word proper.\n'
        '\n'
        "SETTLED — AND THE HEADING'S END IS STATED. **तत्र जातः\n"
        '  इति प्रागतः कालाधिकारः** — काल carries up to 4.3.25\n'
        '  and not into it, so 4.3.24 is the last rule it\n'
        '  governs. The eighth range in two pādas with both ends\n'
        '  written down.'
    ),
    '4.3.12': (
        'SETTLED — श्राद्धे शरदः, ऋत्वणोऽपवादः. शारदिकं श्राद्धम्;\n'
        '  **शारदमन्यत्**.\n'
        '\n'
        'SETTLED — A MEANING EXCLUDED BY USAGE AND NOT BY RULE.\n'
        '  **श्राद्ध इति च कर्म गृह्यते, न श्रद्धावान् पुरुषः,\n'
        '  अनभिधानात्** — श्राद्ध here is the RITE and not a man\n'
        '  of faith, *because that is not how the word is said*.\n'
        '  अनभिधान is the ground: nothing in the grammar forbids\n'
        '  the other reading, and the language simply does not\n'
        '  use it. The project has met the argument before, and\n'
        '  it is the one place where the Aṣṭādhyāyī defers openly\n'
        '  to usage against its own machinery.'
    ),
    '4.3.13': (
        'SETTLED — विभाषा रोगातपयोः, शरद इत्येव; ऋत्वणोऽपवादः. शारदिको\n'
        '  रोगः beside शारदो रोगः; शारदिक आतपः beside शारद\n'
        '  आतपः — the autumn fever and the autumn heat, each\n'
        '  with two forms. रोगातपयोरिति किम्? शारदं दधि.'
    ),
    '4.3.14': (
        'SETTLED — निशाप्रदोषाभ्यां च. **कालाट् ठञ् इति नित्ये ठञि प्राप्ते\n'
        '  विकल्प उच्यते** — 4.3.11 gave the ठञ् without an\n'
        '  option, so the option is spoken against it. नैशिकम्\n'
        '  beside नैशम्; प्रादोषिकम् beside प्रादोषम्. The same\n'
        "  shape of argument as 4.2.144's, three rules into a new\n"
        '  pāda.'
    ),
    '4.3.15': (
        'SETTLED — श्वसस्तुट् च, विभाषेत्येव. शौवस्तिकः — the ठञ् with तुट्\n'
        '  prefixed to it.\n'
        '\n'
        'SETTLED — AND THE OPTION LEAVES ROOM FOR TWO MORE\n'
        '  AFFIXES FROM TWO MORE RULES. त्यप् is given from the\n'
        '  same word by **ऐषमोह्यःश्वसोऽन्यतरस्याम्** [4.2.105],\n'
        '  and **एताभ्यां मुक्ते ट्युट्युलावपि भवतः** — where\n'
        '  both of those are let go, the ट्यु and ट्युल् of\n'
        '  4.3.23 come. शौवस्तिकः, श्वस्त्यः, श्वस्तनः: three\n'
        '  words for *of tomorrow*, from three rules in two\n'
        '  pādas, and the options chain rather than compete.'
    ),
    '4.3.16': (
        'SETTLED — संधिवेलाद्यृतुनक्षत्रेभ्योऽण्, कालादित्येव; ठञोऽपवादः.\n'
        '  Three grounds in one rule: the संधिवेलादि list —\n'
        '  सांधिवेलम्, सांध्यम्; the SEASONS — ग्रैष्मम्,\n'
        '  शैशिरम्; and the LUNAR MANSIONS — तैषम्, पौषम्, which\n'
        '  is how the months are named. All three are reached\n'
        '  **कालवृत्तिभ्यः**, only as words denoting a time.\n'
        '\n'
        'SETTLED — THE DEFAULT NAMED TO BEAT ITS BEATER, AGAIN.\n'
        '  **अण्ग्रहणं वृद्धाच्छस्य बाधनार्थम्** — अण् is the\n'
        '  affix that would have come anyway, and it is named so\n'
        "  that 4.2.114's छ does not take the ground. 4.2.110 and\n"
        '  4.2.132 both did this, and the vṛtti called it\n'
        '  बाधकबाधनार्थम् there.\n'
        '\n'
        'NOTE — a गणसूत्र rides with the list: **संवत्सरात्\n'
        '  फलपर्वणोः** — सांवत्सरं फलम्, सांवत्सरं पर्व, from\n'
        '  संवत्सर when a fruit or a festival is meant.'
    ),
    '4.3.17': (
        'SETTLED — प्रावृष एण्यः, ऋत्वणोऽपवादः. **प्रावृषेण्यो बलाहकः** —\n'
        '  the cloud of the rains. An affix given to one word\n'
        '  only, and the word it makes outlives the rule in\n'
        '  poetry.'
    ),
    '4.3.18': (
        'SETTLED — वर्षाभ्यष्ठक्, ऋत्वणोऽपवादः. वार्षिकं वासः,\n'
        '  वार्षिकमनुलेपनम् — the cloak for the rains and the\n'
        '  ointment for them.'
    ),
    '4.3.19': (
        'SETTLED — छन्दसि ठञ्, ठकोऽपवादः. **स्वरे भेदः** — and the\n'
        '  difference between the two affixes is in the ACCENT\n'
        '  and nowhere else, since ठक् and ठञ् both become इक by\n'
        '  7.3.50. नभश्च नभस्यश्च **वार्षिकावृतू**\n'
        '  (तैत्तिरीयसंहिता ४.४.११.१). A rule whose entire effect\n'
        '  is inaudible in an unaccented text.'
    ),
    '4.3.20': (
        'SETTLED — वसन्ताच्च, छन्दसीत्येव; ऋत्वणोऽपवादः. मधुश्च माधवश्च\n'
        '  **वासन्तिकावृतू** (तैत्तिरीयसंहिता ४.४.११.१) — the\n'
        '  same verse of the same recension the last rule was\n'
        '  quoted from, and the next one too. The three rules\n'
        '  4.3.19 to 4.3.21 are read off a single passage naming\n'
        '  the seasons in order.'
    ),
    '4.3.21': (
        'SETTLED — हेमन्ताच्च, छन्दसीत्येव. सहश्च सहस्यश्च\n'
        '  **हैमन्तिकावृतू** (तैत्तिरीयसंहिता ४.४.११.१).\n'
        '\n'
        'NOTE — **योगविभाग उत्तरार्थः**: the rule is split off\n'
        '  from the one before it only so that the next rule has\n'
        '  something to be stated of. A division made for the\n'
        '  benefit of what follows, which is the reverse of\n'
        "  4.3.2's, made to stop something from following."
    ),
    '4.3.22': (
        'SETTLED — सर्वत्राण् च तलोपश्च. हैमनं वासः, हैमनमुपलेपनम् — the\n'
        '  अण् with the त of हेमन्त dropped in the same act.\n'
        '\n'
        'SETTLED — A NON-CARRYING SAID OUT LOUD SO THAT IT\n'
        '  REACHES BACKWARD. **सर्वत्रग्रहणं\n'
        '  छन्दोऽधिकारनिवृत्त्यर्थम्** — *everywhere* cancels the\n'
        '  Vedic heading. ननु च छन्दसीति नानुवर्तिष्यते? If it\n'
        '  simply would not have carried, why spend a word?\n'
        '  **सैवाननुवृत्तिः शब्देनाख्यायते प्रयत्नाधिक्येन\n'
        '  पूर्वसूत्रेऽपि संबन्धार्थम्** — the not-carrying is\n'
        '  SAID, with deliberate extra effort, so that it reaches\n'
        '  back and touches the previous rule as well.\n'
        '  हैमन्तिकमिति हि भाषायामपि ठञं स्मरन्ति: the ठञ् of\n'
        '  4.3.21 is remembered in the spoken language too, and\n'
        '  this word is what lets it out of the Veda.\n'
        '\n'
        'SETTLED — AND THE च GATHERS A SECOND अण् THAT IS NOT\n'
        '  THIS ONE. अथाण्चेति चकारः किमर्थः? अण्, **यथाप्राप्तं\n'
        "  च ऋत्वण्** — this rule's and 4.3.16's, both. कः\n"
        '  पुनरनयोरणोर्विशेषः? **ऋत्वणि हि तकारलोपो नास्ति**,\n'
        '  हैमन्ती पङ्क्तिः. Two affixes of identical shape told\n'
        '  apart by what else happens beside them.\n'
        '\n'
        'NOTE — **तदेवं त्रीणि रूपाणि भवन्ति**, and each is\n'
        '  cited from a different recension: हैमन्तिकम्\n'
        '  (तैत्तिरीयसंहिता ४.४.११.१), हैमन्तम् (पैप्पलादसंहिता\n'
        '  १७.२९.११), हैमनम् (शौनकसंहिता १५.४.१४). Three forms,\n'
        '  three texts, and the grammar accounts for all three\n'
        '  rather than choosing between them.'
    ),
    '4.3.23': (
        'SETTLED — सायंचिरम्प्राह्णेप्रगेऽव्ययेभ्यष्ट्युट्युलौ तुट् च,\n'
        '  कालादित्येव. सायंतनम्, चिरंतनम्, प्राह्णेतनम्,\n'
        '  प्रगेतनम्; and from any time-denoting indeclinable,\n'
        '  दोषातनम्, दिवातनम्.\n'
        '\n'
        'SETTLED — A RULE THAT GIVES AN AFFIX AND MAKES THE WORDS\n'
        '  IT ATTACHES TO. सायम् is already an indeclinable\n'
        '  ending in म्, **ततोऽव्ययत्वादेव सिद्धः प्रत्ययः** —\n'
        '  so the affix would have come by the second half of the\n'
        '  rule anyway. What the naming is for is the SHAPE: the\n'
        '  म-ending of the साय-word, which comes from स्यति in\n'
        '  the sense of ending — **दिवसावसानं सायः** — is\n'
        '  **प्रत्ययसन्नियोगेन निपात्यते**, laid down together\n'
        '  with the affix and not otherwise derivable. So is\n'
        "  चिर's म, and so is the ए of प्राह्णे and प्रगे.\n"
        '\n'
        'NOTE — four vārttikas ride with the rule.\n'
        '  **चिरपरुत्परारिभ्यस्त्नो वक्तव्यः** — चिरत्नम्,\n'
        '  परुत्नम्, परारित्नम्. **प्रगस्त छन्दसि गलोपश्च**:\n'
        '  प्रत्नम् (ऋग्वेद १.३६.४), where the ग goes and what\n'
        '  is left is one of the oldest words in the language.\n'
        '  **अग्रपश्चाड्डिमच्** — अग्रिमम्, पश्चिमम्. And\n'
        '  **अन्ताच्चेति वक्तव्यम्** — अन्तिमम्. Between them\n'
        '  they account for *first*, *last* and *western*.'
    ),
    '4.3.24': (
        'SETTLED — विभाषा पूर्वाह्णापराह्णाभ्याम्. **कालाट् ठञ् इति ठञि\n'
        '  प्राप्ते वचनम्, पक्षे सोऽपि भवति** — 4.3.11 had the\n'
        '  ground, so on the other side of the option its ठञ्\n'
        '  comes back: पूर्वाह्णेतनम् and पौर्वाह्णिकम् both.\n'
        '\n'
        'SETTLED — AND THE VISIBLE FORM REPORTS WHICH RELATION\n'
        '  WAS MEANT. **घकालतनेषु कालनाम्नः** [6.3.17] इति\n'
        '  सप्तम्या अलुक् — before these affixes a time-word\n'
        '  keeps its locative instead of losing it inside the\n'
        '  compound, which is why the form is पूर्वाह्णेतनम् and\n'
        '  not पूर्वाह्णतनम्. यदा तु न सप्तमी समर्थविभक्तिः —\n'
        '  पूर्वाह्णः सोढोऽस्य — **तदा पूर्वाह्णतन इति\n'
        '  भवितव्यम्**. Change the case-relation and the ending\n'
        '  goes, so the surviving ए tells the reader which\n'
        '  relation the word was formed in.'
    ),
    '4.3.25': (
        'SETTLED — तत्र जातः.\n'
        '\n'
        'SETTLED — THE PROMISE MADE AT 4.2.93 IS KEPT HERE.\n'
        '  **अणादयो घादयश्च प्रत्ययाः प्रकृताः, तेषामतः\n'
        '  प्रभृत्यर्थाः समर्थविभक्तयश्च निर्दिश्यन्ते** — the\n'
        '  affixes from अण् onward and from घ onward are already\n'
        '  in hand, and from this rule on the SENSES they carry\n'
        '  and the CASES they attach in are named for them.\n'
        "  4.2.93's vṛtti said this would happen, in nearly these\n"
        '  words, fifty-eight sūtras earlier: तेषां तु जातादयो\n'
        '  ऽर्थाः समर्थविभक्तयश्च पुरस्ताद् वक्ष्यन्ते.\n'
        '\n'
        '  So the rule names no affix. **यथाविहितं प्रत्ययो\n'
        '  भवति** — whichever was already prescribed. And the\n'
        '  examples are the outputs of 4.2.93, 4.2.94 and 4.2.95\n'
        '  read off in order: स्रुघ्ने जातः स्रौघ्नः, माथुरः,\n'
        '  औत्सः, औदपानः; राष्ट्रियः, अवारपारीणः; शाकलिकः,\n'
        '  माकलिकः; ग्राम्यः, ग्रामीणः; कात्रेयकः, औम्भेयकः.\n'
        '\n'
        '  The codification answers this rule by CALLING the one\n'
        '  that supplied the affix, because that is the whole of\n'
        "  what यथाविहितम् says. Ask it about ग्राम and 4.2.94's\n"
        "  य comes back; ask it about राष्ट्र and 4.2.93's घ."
    ),
    '4.3.26': (
        'SETTLED — प्रावृषष्ठप्, एण्यस्यापवादः. प्रावृषि जातः प्रावृषिकः.\n'
        '  **पकारः स्वरार्थः** — the प is there for the accent\n'
        '  and for nothing else; ठ् alone would have produced the\n'
        '  same इक by 7.3.50.'
    ),
    '4.3.27': (
        'SETTLED — संज्ञायां शरदो वुञ्, ऋत्वणोऽपवादः, **समुदायेन चेत्\n'
        '  संज्ञा गम्यते** — if the name is understood from the\n'
        '  WHOLE and not from its parts. शारदका दर्भाः, शारदका\n'
        '  मुद्गाः: दर्भविशेषस्य मुद्गविशेषस्य चेयं संज्ञा, the\n'
        '  name of a particular grass and a particular bean.\n'
        '  संज्ञायामिति किम्? शारदं सस्यम्.\n'
        '\n'
        'NOTE — **संज्ञाधिकारं केचित् कृतलब्धक्रीतकुशलाः इति\n'
        '  यावद् अनुवर्तयन्ति**: SOME carry the संज्ञा heading\n'
        '  all the way to 4.3.38. A range with both ends stated\n'
        '  and an authority named for it — which is not the same\n'
        '  thing as a range the tradition agrees on, and the\n'
        '  codification records whose reading it is.'
    ),
    '4.3.28': (
        'SETTLED — पूर्वाह्णापराह्णार्द्रामूलप्रदोषावस्करादद्वुन्, तत्र\n'
        '  जात इत्येतस्मिन् विषये संज्ञायां गम्यमानायाम्. And the\n'
        '  vṛtti pairs each base with the rule it displaces:\n'
        '  पूर्वाह्णकः, अपराह्णकः against 4.3.24; आर्द्रकः,\n'
        '  मूलकः **नक्षत्राणोऽपवादः** against 4.3.16; प्रदोषकः\n'
        '  against 4.3.14; अवस्करकः **औत्सर्गिकस्याणोऽपवादः**\n'
        '  against 4.1.83. Six bases and four different rules\n'
        '  beaten by one affix.\n'
        '\n'
        'NOTE — **असंज्ञायां तु यथाप्राप्तं ठञादय एव भवन्ति**:\n'
        '  where no name is meant, each of those four takes its\n'
        '  ground back. आर्द्रकम् is a name and आर्द्रम् is not.'
    ),
    '4.3.29': (
        'SETTLED — पथः पन्थ च, अणोऽपवादः. पथि जातः **पन्थकः** — the affix\n'
        '  and the substitute **प्रत्ययसन्नियोगेन**, in one act,\n'
        '  so that neither of them stands without the other. The\n'
        "  same joint enjoining as 4.2.140's क, and the same\n"
        "  shape as 4.3.22's dropped त."
    ),
    '4.3.30': (
        'SETTLED — अमावास्याया वा. अमावास्यकः beside आमावास्यः —\n'
        "  अमावास्या is in 4.3.16's संधिवेलादि list, so **संधिवेलादिषु\n"
        '  पाठादणोऽपवादः** and the अण् stands on the other side\n'
        '  of the option.\n'
        '\n'
        'SETTLED — A NAMED MAXIM DOING THE WORK OF A SECOND\n'
        '  ENTRY. **एकदेशविकृतस्यानन्यत्वात्** — *a thing\n'
        '  altered in one part is not a different thing* — so the\n'
        '  rule reaches अमावस्या as well without naming it:\n'
        '  अमावस्यकः, आमावस्यः. The pāda before used\n'
        '  तक्रकौण्डिन्यन्याय for the same kind of job, and this\n'
        '  is the second maxim in twenty sūtras invoked to save a\n'
        '  word in the text.'
    ),
    '4.3.31': (
        'SETTLED — अ च. **पूर्वेण वुन्नणोः प्राप्तयोरयं तृतीयः प्रत्ययो\n'
        '  विधीयते** — two affixes were already available on this\n'
        '  ground and this is a THIRD. With the variant spelling\n'
        '  the last rule let in, the count comes to six:\n'
        '  अमावास्यः, अमावास्यकः, आमावास्यः; अमावस्यः,\n'
        '  अमावस्यकः, आमावस्यः. Three affixes times two shapes of\n'
        '  one word, and the second shape is there only because\n'
        '  एकदेशविकृतस्यानन्यत्वात्.'
    ),
    '4.3.32': (
        'SETTLED — सिन्ध्वपकराभ्यां कन्. सिन्धुकः, अपकरकः.\n'
        '  **सिन्धुशब्दः कच्छादिः, ततोऽणि मनुष्यवुञि च प्राप्ते\n'
        "  विधानम्** — सिन्धु is in 4.2.133's कच्छादि list, so\n"
        '  from that word the rule has two affixes to beat, and\n'
        '  from अपकर only the general default.'
    ),
    '4.3.33': (
        'SETTLED — अणञौ च, यथासंख्यम्. सैन्धवः, आपकरः.\n'
        '  **पूर्वेण कनि प्राप्ते वचनम्** — the last rule gave\n'
        '  कन् on exactly this ground, so these two are spoken\n'
        '  against it and all three affixes stand.\n'
        '\n'
        "NOTE — and here 1.3.10's यथासंख्य DOES run: two bases,\n"
        "  two affixes, matched in order. 4.3.1's could not,\n"
        '  because two against three matches with nothing. The\n'
        '  same convention failing and working thirty-two sūtras\n'
        '  apart, for the same reason both times.'
    ),
    '4.3.34': (
        'SETTLED — श्रविष्ठाफल्गुन्यनुराधास्वातितिष्यपुनर्वसुहस्तविशाखाषाढा-\n'
        '  बहुलाल्लुक्. श्रविष्ठासु जातः **श्रविष्ठः** — the\n'
        '  affix given and then taken away, and what is left is\n'
        "  the mansion's own name used of a person born under it.\n"
        '  फल्गुनः, अनुराधः, स्वातिः, तिष्यः, पुनर्वसुः, हस्तः,\n'
        '  विशाखः, अषाढः, बहुलः.\n'
        '\n'
        'SETTLED — AND THE FEMININE AFFIX GOES WITH IT. तस्मिन्\n'
        '  स्त्रीप्रत्ययस्यापि **लुक् तद्धितलुकि** [1.2.49] इति\n'
        '  लुग् भवति. श्रविष्ठा is feminine and carries a\n'
        '  feminine affix; when the taddhita goes by लुक्, that\n'
        '  goes too, by a rule stated for exactly this case.\n'
        '\n'
        'SETTLED — AND THEN A DIFFERENT RULE PUTS ONE BACK. A\n'
        '  vārttika adds three words in the feminine —\n'
        '  **लुक्प्रकरणे चित्रारेवतीरोहिणीभ्यः\n'
        '  स्त्रियामुपसंख्यानम्** — चित्रायां जाता चित्रा,\n'
        '  रेवती, रोहिणी. And **स्त्रीप्रत्ययस्य लुकि कृते\n'
        '  गौरादित्वाद् ङीष्**: once 1.2.49 has removed the\n'
        '  feminine affix the stem is बहुलादि, so 4.1.41 supplies\n'
        '  a different one. An affix elided by one rule and\n'
        '  another put in its place by a second, and the visible\n'
        '  form is the same either way.\n'
        '\n'
        'NOTE — two more vārttikas. **फल्गुन्यषाढाभ्यां टानौ** —\n'
        '  फल्गुनी, अषाढा. **श्रविष्ठाषाढाभ्यां छणपि** —\n'
        '  श्राविष्ठीयः, आषाढीयः.'
    ),
    '4.3.35': (
        'SETTLED — स्थानान्तगोशालखरशालाच्च. गोस्थाने जातो **गोस्थानः**;\n'
        '  अश्वस्थानः; गोशालः; खरशालः. A person born in the\n'
        "  cow-shed is called by the shed's own name, and the\n"
        '  affix that would have marked the relation is gone.'
    ),
    '4.3.36': (
        'SETTLED — वत्सशालाभिजिदश्वयुक्छतभिषजो वा. वत्सशालायां जातो\n'
        '  वत्सशालः beside वात्सशालः; अभिजित् beside आभिजितः;\n'
        '  अश्वयुक् beside आश्वयुजः; शतभिषक् beside शातभिषजः.\n'
        '\n'
        'NOTE — **बहुलग्रहणस्यायं प्रपञ्चः**: the vṛtti reads\n'
        '  this rule, and the two before it, as an UNFOLDING of\n'
        '  the single word बहुलम् in the rule that follows. Three\n'
        '  rules spelling out what one word of the fourth would\n'
        '  have covered — and the fourth is still needed, because\n'
        '  even together they do not exhaust it.'
    ),
    '4.3.37': (
        'SETTLED — नक्षत्रेभ्यो बहुलम्. रोहिणः beside रौहिणः; मृगशिराः\n'
        '  beside मार्गशीर्षः.\n'
        '\n'
        'SETTLED — बहुलम् IS NOT विभाषा. An option says the affix\n'
        '  may come or may not, and both forms are equally\n'
        '  correct wherever it applies. *Variously* says the\n'
        '  elision happens in some places and not in others,\n'
        '  without the rule undertaking to say which — so the\n'
        '  three rules before it can spell out particular cases\n'
        '  and still leave the word doing work. The table keeps\n'
        '  the two in separate columns for that reason.'
    ),
    '4.3.38': (
        'SETTLED — कृतलब्धक्रीतकुशलाः, तत्रेत्येव. स्रुघ्ने कृतो वा लब्धो\n'
        '  वा क्रीतो वा कुशलो वा **स्रौघ्नः**; माथुरः,\n'
        '  राष्ट्रियः. Four senses in one rule and one affix for\n'
        '  all four.\n'
        '\n'
        'SETTLED — AND THE GRAMMAR DISTINGUISHES WHAT THE WORLD\n'
        '  DOES NOT. ननु च यद् यत्र कृतं जातमपि तत् तत्र भवति,\n'
        '  यच्च यत्र क्रीतं लब्धमपि तत् तत्रैव भवति, **किमर्थं\n'
        '  भेदेनोपादानं क्रियते?** — whatever was made somewhere\n'
        '  was also born there, and whatever was bought there was\n'
        '  also got there, so why name them separately at all?\n'
        '  **शब्दार्थस्य भिन्नत्वाद् वस्तुमात्रेण क्रीतं लब्धं\n'
        '  भवति, शब्दार्थस्तु भिद्यत एव** — as a matter of FACT\n'
        '  a thing bought is a thing got; the meanings of the\n'
        '  WORDS are different all the same.\n'
        '\n'
        '  The grammar is about what is said and not about what\n'
        '  is the case, and this is the plainest statement of it\n'
        '  the project has met.'
    ),
    '4.3.39': (
        'SETTLED — प्रायभवः, तत्रेत्येव. **प्रायशब्दः साकल्यस्य\n'
        '  किंचिन्न्यूनतामाह** — प्राय says *a little short of\n'
        '  the whole*. स्रुघ्ने प्रायेण बाहुल्येन भवति स्रौघ्नः.\n'
        '\n'
        'SETTLED — AND THE VṚTTI CALLS THE RULE POINTLESS.\n'
        '  **प्रायभवग्रहणमनर्थकम्, तत्रभवेन कृतार्थत्वात्** —\n'
        '  naming *mostly-there* achieves nothing, because 4.3.53\n'
        '  तत्र भवः covers it already. And the defence is turned\n'
        '  away too: अनित्यभवः प्रायभव इति चेद्, **मुक्तसंशयेन\n'
        '  तुल्यम्** — if you answer that प्रायभव means\n'
        '  *not-always-there*, that comes to the same thing as\n'
        '  the plain case with the doubt taken out.\n'
        '\n'
        '  A commentary concluding that the rule it is explaining\n'
        '  was not needed, and explaining it anyway. The\n'
        '  codification does the same: the row is there, and it\n'
        '  says what the vṛtti says about it.'
    ),
    '4.3.40': (
        'SETTLED — उपजान्वुपकर्णोपनीवेष्ठक्, अणोऽपवादः. औपजानुकः,\n'
        '  औपकर्णिकः, औपनीविकः — what is mostly about the knee,\n'
        '  the ear, the waistband. Three अव्ययीभाव compounds,\n'
        '  taking the affix as wholes.'
    ),
    '4.3.41': (
        'SETTLED — संभूते, तत्रेत्येव. स्रुघ्ने संभवति स्रौघ्नः.\n'
        '\n'
        'SETTLED — A SENSE NARROWED BY WHAT THE NEIGHBOURS\n'
        '  ALREADY TOOK. **अवक्ऌप्तिः प्रमाणानतिरेकश्च\n'
        '  संभवत्यर्थ इह गृह्यते, नोत्पत्तिः सत्ता वा,\n'
        '  जातभवाभ्यां गतत्वात्** — संभव here is *fitting in*,\n'
        '  not exceeding the measure of the place; it is NOT\n'
        '  arising and NOT being, because 4.3.25 जातः has arising\n'
        "  and 4.3.53 भवः has being. A word's range settled by\n"
        '  subtracting what two neighbouring rules have taken,\n'
        '  one of them fourteen sūtras ahead of it.'
    ),
    '4.3.42': (
        'SETTLED — कोशाड्ढञ्, अणोऽपवादः. कोशे संभूतं **कौशेयं वस्त्रम्** —\n'
        '  silk, what is produced in a cocoon.\n'
        '\n'
        'NOTE — **रूढिरेषा, तेन क्रिमौ न भवति, खड्गकोशाच्च**:\n'
        '  the word is CONVENTIONAL, fixed on the cloth. So it is\n'
        '  not used of the worm that lives in the cocoon, and not\n'
        '  of anything in a sword-sheath, though कोश names that\n'
        '  too. Two exclusions, neither of them by a rule.'
    ),
    '4.3.43': (
        'SETTLED — कालात् साधुपुष्प्यत्पच्यमानेषु. Three senses at once,\n'
        '  and an example for each. हेमन्ते साधुर् **हैमनः\n'
        '  प्राकारः**, a rampart that does well in winter; वसन्ते\n'
        '  पुष्प्यन्ति **वासन्त्यः कुन्दलताः**, jasmine that\n'
        '  flowers in spring; शरदि पच्यन्ते **शारदाः शालयः**,\n'
        '  rice that ripens in autumn. शैशिरमनुलेपनम्, ग्रैष्म्यः\n'
        '  पाटलाः, ग्रैष्मा यवाः.\n'
        '\n'
        'SETTLED — AND काल IS NAMED A SECOND TIME. The word\n'
        "  headed 4.3.11 to 4.3.24 and stopped where that rule's\n"
        '  own vṛtti said it would. Here it is spoken afresh in a\n'
        '  sūtra of its own and carries again as far as 4.3.52,\n'
        '  and that end is recorded by the rule AFTER it. One\n'
        '  word heading two ranges in one pāda, with the two\n'
        '  kinds of boundary-statement one each.'
    ),
    '4.3.44': (
        'SETTLED — उप्ते च, तत्रेत्येव कालादिति च. हेमन्त उप्यन्ते\n'
        '  **हैमन्ता यवाः**; ग्रैष्मा व्रीहयः — barley sown in\n'
        '  winter, rice sown in summer.\n'
        '\n'
        'NOTE — **योगविभाग उत्तरार्थः**: the rule is split off\n'
        '  from the last only so that the next has something to\n'
        '  be stated of. The third time in this pāda, after\n'
        "  4.3.2's and 4.3.21's."
    ),
    '4.3.45': (
        'SETTLED — आश्वयुज्या वुञ्, ठञोऽपवादः. आश्वयुज्यामुप्ता\n'
        '  **आश्वयुजका माषाः** — beans sown at the Āśvayujī full\n'
        '  moon.\n'
        '\n'
        'NOTE — the vṛtti derives the base before using it.\n'
        '  **अश्विनीभ्यां युक्ता पौर्णमासी आश्वयुजी**, the full\n'
        '  moon joined to the two Aśvinī stars; and\n'
        '  अश्विनीपर्यायोऽश्वयुक्शब्दः, अश्वयुज् being another\n'
        '  name for that mansion.'
    ),
    '4.3.46': (
        'SETTLED — ग्रीष्मवसन्तादन्यतरस्याम्, ऋत्वणोऽपवादः. ग्रैष्मकम्\n'
        '  beside ग्रैष्मं सस्यम्; वासन्तकम् beside वासन्तम्.'
    ),
    '4.3.47': (
        'SETTLED — देयमृणे, तत्रेत्येव कालादिति च. **यद् देयमृणं चेत् तद्\n'
        '  भवति** — the affix comes only if what is to be given\n'
        '  is a DEBT. मासे देयमृणं मासिकम्; आर्धमासिकम्,\n'
        '  सांवत्सरिकम्. ऋण इति किम्? **मासे देया भिक्षा** —\n'
        '  alms to be given monthly are not a debt.'
    ),
    '4.3.48': (
        'SETTLED — कलाप्यश्वत्थयवबुसाद् वुन्, कालादित्येव. कलापकम्,\n'
        '  अश्वत्थकम्, यवबुसकम्.\n'
        '\n'
        'SETTLED — THREE SEASONS NAMED BY WHAT HAPPENS IN THEM.\n'
        '  **कलाप्यादयः शब्दाः साहचर्यात् काले वर्तन्ते** — these\n'
        '  words denote times by the COMPANY THEY KEEP, and the\n'
        '  vṛtti unpacks each one. यस्मिन् काले मयूराः कलापिनो\n'
        '  भवन्ति स कलापी, the season when the peacocks have\n'
        '  their tail-fans; यस्मिन्नश्वत्थाः फलन्ति सोऽश्वत्थः,\n'
        '  when the fig trees bear; यस्मिन् यवबुसं संपद्यते स\n'
        '  यवबुसशब्देनोच्यते, when the barley-chaff comes.\n'
        '\n'
        '  4.3.11 allowed a word that denotes a time only\n'
        '  figuratively — गुणवृत्त्यापि — and gave कादम्बपुष्पिकम्\n'
        '  as its example. This rule names the mechanism:\n'
        '  साहचर्य, association. The principle and its name,\n'
        '  thirty-seven sūtras apart.'
    ),
    '4.3.49': (
        'SETTLED — ग्रीष्मावरसमाद् वुञ्, अण्ठञोरपवादः. ग्रीष्मे देयमृणं\n'
        '  ग्रैष्मकम्; आवरसमकम्. **प्रत्ययान्तरकरणं\n'
        '  वृद्ध्यर्थम्** — a different affix is given for the\n'
        '  sake of the वृद्धि, which the affix already available\n'
        '  would not have brought. समाशब्दो वर्षपर्यायः, समा\n'
        '  being another word for a year.'
    ),
    '4.3.50': (
        'SETTLED — संवत्सराग्रहायणीभ्यां ठञ् च. सांवत्सरिकम् and\n'
        '  सांवत्सरकम्; आग्रहायणिकम् and आग्रहायणकम्.\n'
        '\n'
        'SETTLED — AN AFFIX NAMED WHERE AN OPTION WOULD HAVE BEEN\n'
        '  SHORTER. **वेति वक्तव्ये ठञ्ग्रहणम्** — why name ठञ्\n'
        '  when वा would have said as much? Because संवत्सर is in\n'
        '  the गणसूत्र **संवत्सरात् फलपर्वणोः** read with\n'
        '  4.3.16, and where the फल is meant AS A DEBT the ठञ्\n'
        "  has to beat that rule's अण्. An option would have left\n"
        '  the other affix standing; naming this one displaces\n'
        '  it. The two devices do not have the same reach.'
    ),
    '4.3.51': (
        'SETTLED — व्याहरति मृगः, तत्रेत्येव कालादिति च. निशायां व्याहरति\n'
        '  मृगो **नैशः**, नैशिकः; प्रादोषः, प्रादोषिकः. A whole\n'
        '  rule for the time at which a deer calls.\n'
        '\n'
        'NOTE — मृग इति किम्? **निशायां व्याहरत्युलूकः** — the\n'
        '  owl calls at night as well, and gets nothing.'
    ),
    '4.3.52': (
        'SETTLED — तदस्य सोढम्, कालादित्येव. **सोढं जितमभ्यस्तमित्यर्थः** —\n'
        '  borne, conquered, practised. निशासहचरितमध्ययनं निशा,\n'
        '  तत् सोढमस्य छात्रस्य **नैशः**, नैशिकः: the study that\n'
        '  goes with the night is called *the night*, and the\n'
        '  student who has mastered it is नैश.\n'
        '\n'
        'SETTLED — AND THE CASE CHANGES FOR ONE RULE. तदिति\n'
        '  **प्रथमासमर्थात्** कालवाचिनः प्रातिपदिकाद् अस्येति\n'
        '  **षष्ठ्यर्थे** — the base stands in the nominative and\n'
        '  the relation to the person is a genitive. Every rule\n'
        '  since 4.3.25 has taken its base in the locative; this\n'
        '  one does not, and the next rule says तत्र again in\n'
        '  order to change it back.'
    ),
    '4.3.53': (
        'SETTLED — तत्र भवः. स्रुघ्ने भवः स्रौघ्नः; माथुरः, राष्ट्रियः.\n'
        '\n'
        'SETTLED — AND काल IS OVER. **कालादिति निवृत्तम्**. The\n'
        '  second of its two ranges in this pāda ends here, and\n'
        '  this end is recorded from OUTSIDE by the rule that\n'
        '  comes after it — where the first range was bounded in\n'
        '  advance by the rule that opened it. The same word,\n'
        '  both kinds of statement, forty sūtras apart.\n'
        '\n'
        'SETTLED — AND THE SENSE IS NARROWED BY SUBTRACTION.\n'
        '  **सत्ता भवत्यर्थो गृह्यते न जन्म, तत्र जातः इति\n'
        '  गतार्थत्वात्** — भव is BEING and not birth, because\n'
        '  4.3.25 has birth already. 4.3.41 made the same\n'
        '  subtraction, and made it against these same two rules.\n'
        '\n'
        'SETTLED — AND A WORD REPEATED IN ORDER TO PUSH ANOTHER\n'
        '  OUT. **पुनस्तत्रग्रहणं तदस्येति निवृत्त्यर्थम्** —\n'
        '  तत्र is said again not because it had lapsed but so\n'
        "  that the last rule's तदस्य goes. Anuvṛtti cancelled\n"
        '  by restating what it displaced.'
    ),
    '4.3.54': (
        'SETTLED — दिगादिभ्यो यत्, **अणश्छस्य चापवादः**. दिशि भवं दिश्यम्;\n'
        '  वर्ग्यम्.\n'
        '\n'
        'NOTE — **मुखजघनशब्दयोरशरीरावयवार्थः पाठः**: मुख and\n'
        '  जघन are in the list for the sense that is NOT a\n'
        '  body-part, since the next rule covers body-parts\n'
        '  anyway. सेनामुख्यम्, the van of an army, and\n'
        '  सेनाजघन्यम्, its rear. Two entries read for what the\n'
        '  neighbouring rule does not reach — the same shape as\n'
        "  4.2.127's विदेह and आनर्त."
    ),
    '4.3.55': (
        'SETTLED — शरीरावयवाच्च, अणोऽपवादः. **शरीरं प्राणिकायः** — a body\n'
        "  is a living thing's frame. दन्तेषु भवं **दन्त्यम्**;\n"
        '  **कर्ण्यम्**; **ओष्ठ्यम्**.\n'
        '\n'
        'NOTE — and those three are the phonetic terms *dental*\n'
        '  and *labial*. The śikṣā texts name the places of\n'
        '  articulation with words this rule makes, so a rule\n'
        '  about what is IN a body-part supplies the vocabulary\n'
        '  for describing speech.'
    ),
    '4.3.56': (
        'SETTLED — दृतिकुक्षिकलशिवस्त्यस्त्यहेर्ढञ्. दृतौ भवं दार्तेयम्;\n'
        '  कौक्षेयम्, कालशेयम्, वास्तेयम्, आस्तेयम्;\n'
        "  **आहेयमजरं विषम्**, the snake's venom that does not\n"
        '  age.\n'
        '\n'
        'NOTE — **अस्तिशब्दः प्रातिपदिकम्, न तिङन्तम्**: the\n'
        '  अस्ति in the rule is a NOMINAL STEM and not the finite\n'
        '  verb it is written exactly like. A warning the reader\n'
        '  needs and could not have supplied.'
    ),
    '4.3.57': (
        'SETTLED — ग्रीवाभ्योऽण् च, **शरीरावयवाद् यतोऽपवादः**. ग्रीवासु\n'
        '  भवं ग्रैवम्, ग्रैवेयम् — the च bringing ढञ् along, so\n'
        '  both stand.\n'
        '\n'
        'NOTE — **ग्रीवाशब्दो धमनीवचनः, तासां बहुत्वाद् बहुवचनं\n'
        '  कृतम्**: ग्रीवा names the ARTERIES of the neck, and\n'
        '  they are many, which is why the sūtra puts the word in\n'
        '  the plural. A grammatical number explained by anatomy.'
    ),
    '4.3.58': (
        'SETTLED — गम्भीराञ्ञ्यः, अणोऽपवादः. गम्भीरे भवं **गाम्भीर्यम्** —\n'
        '  depth, and the abstract noun is made by asking what is\n'
        '  IN the deep.\n'
        '\n'
        'NOTE — **बहिर्देवपञ्चजनेभ्यश्चेति वक्तव्यम्**: बाह्यम्,\n'
        '  दैव्यम्, पाञ्चजन्यम्.'
    ),
    '4.3.59': (
        'SETTLED — अव्ययीभावाच्च, अणोऽपवादः. परिमुखं भवं **पारिमुख्यम्**;\n'
        '  पारिहनव्यम्.\n'
        '\n'
        'SETTLED — A HEADING WORD USED AS A QUALIFIER OF A LIST.\n'
        '  **न च सर्वस्मादव्ययीभावाद् भवति; किं तर्हि?\n'
        '  परिमुखादेः** — not from every अव्ययीभाव but from the\n'
        '  परिमुखादि list, and औपकूलम् is what stands otherwise.\n'
        '  **परिमुखादीनां च गणपाठस्यैतदेव प्रयोजनम्**: that list\n'
        '  exists in the गणपाठ for this rule and for nothing\n'
        '  else. **तेषां विशेषणमव्ययीभावग्रहणम्** — so the word\n'
        '  अव्ययीभाव qualifies the LIST rather than being the\n'
        '  ground the rule stands on, which is the reverse of\n'
        '  how a संज्ञा usually works in a rule.'
    ),
    '4.3.60': (
        'SETTLED — अन्तःपूर्वपदाट् ठञ्, अव्ययीभावादित्येव; अणोऽपवादः.\n'
        '  **अन्तःशब्दो विभक्त्यर्थे समस्यते** — अन्तर् compounds\n'
        '  in the sense of a case-ending. आन्तर्वेश्मिकम्,\n'
        '  आन्तर्गेहिकम्.\n'
        '\n'
        'SETTLED — AND THIRTEEN VĀRTTIKAS RIDE WITH IT, GATHERED\n'
        '  INTO TWO ŚLOKAS AT THE END. समानशब्दाट् ठञ् —\n'
        '  सामानिकम्; तदादेश्च — सामानग्रामिकम्, सामानदेशिकम्;\n'
        '  **अध्यात्मादिभ्यश्च** — आध्यात्मिकम्, आधिदैविकम्,\n'
        '  आधिभौतिकम्, the three classical sources of affliction,\n'
        '  and अध्यात्मादिराकृतिगणः, an open list. ऊर्ध्वंदमाच्च\n'
        '  and ऊर्ध्वदेहाच्च — और्ध्वदेहिकम्, the rites for the\n'
        '  departed. लोकोत्तरपदाच्च — ऐहलौकिकम्, पारलौकिकम्, of\n'
        '  this world and of the next. मुखपार्श्वतसोरीयः,\n'
        '  जनपरयोः कुक् च, मध्यशब्दादीयः, मण्मीयौ, **मध्यो मध्यं\n'
        '  दिनण् चास्मात्** — माध्यन्दिनम्, which is the name of\n'
        '  a Yajurveda recension; स्थाम्नो लुक् — **अश्वत्थामा**;\n'
        '  अजिनान्ताच्च — वृकाजिनः, सिंहाजिनः.\n'
        '\n'
        'NOTE — four of these were read at 4.2.138 as गणसूत्र of\n'
        '  the गहादि list, and are read again here. The same\n'
        '  supplement stated at two rules, because two rules give\n'
        '  affixes that the same words could take.'
    ),
    '4.3.61': (
        'SETTLED — ग्रामात् पर्यनुपूर्वात्, अव्ययीभावादित्येव; अणोऽपवादः.\n'
        '  पारिग्रामिकः, आनुग्रामिकः — what is in the country\n'
        '  round the village, and what is in the country along\n'
        '  it.'
    ),
    '4.3.62': (
        "SETTLED — जिह्वामूलाङ्गुलेश्छः, **यतोऽपवादः** — it beats 4.3.55's\n"
        '  यत्, which would have reached both words as parts of\n'
        '  the body. जिह्वामूलीयम्, अङ्गुलीयम्.\n'
        '\n'
        "NOTE — and the first of those is the phoneticians' name\n"
        '  for the जिह्वामूलीय sound, articulated at the root of\n'
        '  the tongue. 4.3.55 gave दन्त्य and ओष्ठ्य; this rule\n'
        '  gives the third of the terms.'
    ),
    '4.3.63': (
        'SETTLED — वर्गान्ताच्च, अणोऽपवादः. कवर्गीयम्, चवर्गीयम् — and\n'
        '  these are the standard names for the rows of the\n'
        '  alphabet, made by asking what is IN the row.'
    ),
    '4.3.64': (
        'SETTLED — अशब्दे यत्खावन्यतरस्याम्, वर्गान्तादित्येव. **छे\n'
        '  प्राप्ते वचनं पक्षे सोऽपि भवति** — the last rule had\n'
        '  the ground, so on the other side of the option its छ\n'
        '  comes back and there are three forms:\n'
        '  वासुदेववर्ग्यः, वासुदेववर्गीणः, वासुदेववर्गीयः;\n'
        '  युधिष्ठिरवर्ग्यः, युधिष्ठिरवर्गीणः, युधिष्ठिरवर्गीयः.\n'
        '\n'
        'SETTLED — AND THE GRAMMAR RESERVES ONE FORM FOR TALKING\n'
        '  ABOUT ITSELF. अशब्द इति किम्? **कवर्गीयो वर्णः** —\n'
        '  where the वर्ग is a row of SOUNDS, the option does not\n'
        "  apply and only छ stands. So of Vāsudeva's party one\n"
        '  may say three things and of the k-row of the alphabet\n'
        '  only one, and the difference is stated in the rule.'
    ),
    '4.3.65': (
        'SETTLED — कर्णललाटात् कनलंकारे, यतोऽपवादः. **कर्णिका**,\n'
        '  **ललाटिका** — the ear-ornament and the\n'
        '  forehead-ornament. अलंकार इति किम्? कर्ण्यम्,\n'
        '  ललाट्यम्, which is what 4.3.55 gives for anything\n'
        '  else in an ear.'
    ),
    '4.3.66': (
        'SETTLED — तस्य व्याख्यान इति च व्याख्यातव्यनाम्नः.\n'
        '  **तस्येति षष्ठीसमर्थाद् व्याख्यातव्यनाम्नः\n'
        '  प्रातिपदिकाद् व्याख्यानेऽभिधेये यथाविहितं प्रत्ययो\n'
        '  भवति, तत्र भवे च** — the base stands in the GENITIVE\n'
        '  for the new sense and in the locative for the one\n'
        '  the च keeps.\n'
        '  **व्याख्यायतेऽनेनेति व्याख्यानम्** — an EXPOSITION is\n'
        '  what a thing is expounded by; व्याख्यातव्यस्य नाम\n'
        '  व्याख्यातव्यनाम, the name of the thing to be\n'
        '  expounded. सुपां व्याख्यानः **सौपो ग्रन्थः**, the\n'
        '  book that expounds the nominal endings; तैङः, कार्तः.\n'
        '  And by the च, सुप्सु भवं सौपम्.\n'
        '\n'
        "SETTLED — A च THAT GATHERS THE PREVIOUS SENTENCE'S\n"
        '  MEANING. **वाक्यार्थसमीपे चकारः श्रूयमाणः\n'
        '  पूर्ववाक्यार्थमेव समुच्चिनोति** — heard beside the\n'
        '  meaning of a sentence, the च joins the meaning of the\n'
        '  sentence BEFORE, which is 4.3.53 तत्र भवः.\n'
        '\n'
        'SETTLED — SO TWO HEADINGS GOVERN AT ONCE, AND THE VṚTTI\n'
        '  SAYS WHY. **भवव्याख्यानयोर्युगपदधिकारोऽपवादविधानार्थः,\n'
        '  कृतनिर्देशौ हि तौ** — the two are made to run\n'
        '  SIMULTANEOUSLY so that the seven exceptions after them\n'
        '  can be stated once for both instead of twice. Every\n'
        '  range this project has recorded until now displaced\n'
        '  the one before it; these two overlap on purpose, and\n'
        '  the purpose is economy in the rules that follow.\n'
        '\n'
        'NOTE — व्याख्यातव्यनाम्न इति किम्? पाटलिपुत्रस्य\n'
        '  व्याख्यानी सुकोसला — Sukosalā expounds Pāṭaliputra,\n'
        '  telling how the city is laid out; **न तु पाटलिपुत्रं\n'
        '  व्याख्यातव्यनाम**, a city is not the NAME of\n'
        '  something to be expounded.'
    ),
    '4.3.67': (
        'SETTLED — बह्वचोऽन्तोदात्ताट् ठञ्, अणोऽपवादः. षात्वणत्विकम्,\n'
        '  नातानतिकम् — books on ष-substitution and\n'
        '  ण-substitution, and on न-forms; **समासस्वरेणान्तोदात्ताः\n'
        '  प्रकृतयः**, the bases carry the final accent by the\n'
        '  compound-accent rule.\n'
        '\n'
        'NOTE — बह्वच इति किम्? **द्व्यचष्ठकं वक्ष्यति**: 4.3.72\n'
        '  will give ठक् for a two-vowel base, and एकाच् is what\n'
        '  the counter-examples show — सौपम्, तैङम्, कार्तम्. A\n'
        '  rule pointing five sūtras ahead to say what its own\n'
        '  condition excludes.\n'
        '\n'
        'NOTE — अन्तोदात्तादिति किम्? **संहितायाः सांहितम्**,\n'
        '  where संहिताशब्दो हि गतिस्वरेणाद्युदात्तः — the accent\n'
        '  falls at the front, placed by a rule about preverbs.'
    ),
    '4.3.68': (
        'SETTLED — क्रतुयज्ञेभ्यश्च, अणोऽपवादः. अग्निष्टोमस्य व्याख्यानस्\n'
        '  तत्र भवो वा **आग्निष्टोमिकः**; वाजपेयिकः, राजसूयिकः;\n'
        '  पाकयज्ञिकः, नावयज्ञिकः. **अनन्तोदात्तार्थ आरम्भः** —\n'
        '  the rule is begun for the bases whose accent is NOT\n'
        '  final, which the last rule could not reach.\n'
        '\n'
        'NOTE — **क्रतुभ्य इत्येव सिद्धे\n'
        '  यज्ञग्रहणमसोमयागेभ्योऽपि यथा स्यात्**: क्रतु alone\n'
        '  would have done for the soma sacrifices, and\n'
        '  *sacrifice* is named as well so that the rites which\n'
        '  are NOT soma-offerings come in too — पाञ्चौदनिकः,\n'
        '  दाशौदनिकः. **बहुवचनं स्वरूपविधिनिरासार्थम्**.'
    ),
    '4.3.69': (
        'SETTLED — अध्यायेष्वेवर्षेः, अणोऽपवादः. वसिष्ठस्य व्याख्यानस्तत्र\n'
        '  भवो वा **वासिष्ठिकोऽध्यायः**; वैश्वामित्रिकः.\n'
        '\n'
        "SETTLED — AND A SEER'S NAME MEANS HIS BOOK, BY THE\n"
        '  COMPANY IT KEEPS. **ऋषिशब्दाः प्रवरनामधेयानि** — the\n'
        '  seer-words here are the names invoked in the प्रवर.\n'
        '  And **व्याख्यातव्यनाम्न इत्यनुवर्तते, तत्साहचर्याद्\n'
        '  ऋषिशब्दैर्ग्रन्थ उच्यते**: because *the name of what\n'
        "  is to be expounded* carries over, a seer's name here\n"
        '  denotes his text. The same instrument 4.3.48 named —\n'
        '  साहचर्य — turned on a different kind of word.\n'
        '\n'
        'NOTE — अध्यायेष्विति किम्? **वासिष्ठी ऋक्**: a single\n'
        '  verse is not a lesson.'
    ),
    '4.3.70': (
        'SETTLED — पौरोडाशपुरोडाशात् ष्ठन्. **पुरोडाशाः पिष्टपिण्डाः**,\n'
        '  the flour-cakes; तेषां संस्कारको मन्त्रः पौरोडाशः,\n'
        '  the verse that consecrates them — and the book on THAT\n'
        "  is पौरोडाशिकः, पौरोडाशिकी. From the cakes' own word,\n"
        '  पुरोडाशिकः, पुरोडाशिकी. **षकारो ङीषर्थः**, the ष् is\n'
        '  there for the feminine, as at 4.2.99.'
    ),
    '4.3.71': (
        'SETTLED — छन्दसो यदणौ. **द्व्यच इति ठकि प्राप्ते वचनम्** — छन्दस्\n'
        '  has two vowels, so 4.3.72 would have given ठक्, and\n'
        '  these two are spoken against it. छन्दस्यः\n'
        '  (तैत्तिरीयसंहिता १.६.११.४), छान्दसः (कौषीतकिगृह्य\n'
        '  १४१.३४) — both forms cited from texts rather than\n'
        '  constructed.'
    ),
    '4.3.72': (
        'SETTLED — द्व्यजृद्ब्राह्मणर्क्प्रथमाध्वरपुरश्चरणनामाख्याताट् ठक्,\n'
        '  अणादेरपवादः. From a two-vowel base — ऐष्टिकः,\n'
        '  पाशुकः; from an ऋ-final — चातुर्होतृकः,\n'
        '  पाञ्चहोतृकः; and from the seven named words —\n'
        '  ब्राह्मणिकः, आर्चिकः, प्राथमिकः, आध्वरिकः,\n'
        '  पौरश्चरणिकः.\n'
        '\n'
        'NOTE — **नामाख्यातग्रहणं संघातविगृहीतार्थम्**: *noun*\n'
        '  and *verb* are named so that the rule reaches them\n'
        '  separately AND as a compound — नामिकः, आख्यातिकः, and\n'
        '  **नामाख्यातिकः**. A book on nouns, a book on verbs,\n'
        '  and a book on both, from one entry read two ways.'
    ),
    '4.3.73': (
        'SETTLED — अणृगयनादिभ्यः, ठञादेरपवादः. आर्गयनः, पादव्याख्यानः.\n'
        '  **अण्ग्रहणं बाधकबाधनार्थम्** — the default named to\n'
        '  beat its beater, the fourth time in three pādas;\n'
        '  वास्तुविद्यः is what it saves.\n'
        '\n'
        'NOTE — and the list is a catalogue of the sciences:\n'
        '  ऋगयन, पदव्याख्यान, छन्दोमान, छन्दोभाषा, छन्दोविचिति,\n'
        '  न्याय, पुनरुक्त, **निरुक्त**, **व्याकरण**, निगम,\n'
        '  वास्तुविद्या, अङ्गविद्या, क्षत्रविद्या, उत्पात,\n'
        '  उत्पाद, संवत्सर, मुहूर्त, निमित्त, **उपनिषद्**,\n'
        '  **शिक्षा**. Grammar itself is the ninth entry, and the\n'
        '  rule is how one says *a book about grammar*.'
    ),
    '4.3.74': (
        'SETTLED — तत आगतः. स्रुघ्नादागतः स्रौघ्नः; माथुरः, राष्ट्रियः.\n'
        '  The case changes to the ABLATIVE and the affix stays\n'
        '  यथाविहितम्.\n'
        '\n'
        'SETTLED — AND THE ABLATIVE MEANT IS THE PRINCIPAL ONE.\n'
        '  **तत इति मुख्यमपादानं विवक्षितं यत् तदिह गृह्यते, न\n'
        '  नान्तरीयकम्** — not one that merely came along with\n'
        '  it. स्रुघ्नादागच्छन् **वृक्षमूलादागत** इति: a man\n'
        '  coming from Srughna also comes from the foot of some\n'
        '  tree, and no affix follows from the tree. A condition\n'
        '  on which of several true descriptions the rule is\n'
        '  about.'
    ),
    '4.3.75': (
        'SETTLED — ठगायस्थानेभ्यः, अणोऽपवादः; **छं तु परत्वाद् बाधते**,\n'
        "  and 4.2.114's छ beats it by standing later.\n"
        '  **आय इति स्वामिग्राह्यो भाग उच्यते, स\n'
        '  यस्मिन्नुत्पद्यते तदायस्थानम्** — आय is the share the\n'
        '  owner takes, and a place where it arises is an\n'
        '  आयस्थान, a revenue-office. शुल्कशालाया आगतः\n'
        '  **शौल्कशालिकः**, from the customs-house; आकरिकम्,\n'
        '  from the mine.'
    ),
    '4.3.76': (
        'SETTLED — शुण्डिकादिभ्योऽण्, **आयस्थानठकोऽपवादः**. शुण्डिकादागतः\n'
        '  शौण्डिकः; कार्कणः. **अण्ग्रहणं बाधकबाधनार्थम्** — the\n'
        '  default named to beat its beater again, three sūtras\n'
        '  after the last time; औदपानः is what it saves.'
    ),
    '4.3.77': (
        'SETTLED — विद्यायोनिसंबन्धेभ्यो वुञ्, अणोऽपवादः; छं तु परत्वाद्\n'
        '  बाधते. **विद्यायोनिकृतः संबन्धो येषां ते\n'
        '  विद्यायोनिसंबन्धाः** — those whose connection is made\n'
        '  either by LEARNING or by BIRTH. उपाध्यायादागतम्\n'
        '  **औपाध्यायकम्**, शैष्यकम्, आचार्यकम्; and मातामहकः,\n'
        '  पैतामहकः, मातुलकः. One rule for the two kinds of\n'
        '  relation a person can stand in.'
    ),
    '4.3.78': (
        'SETTLED — ऋतष्ठञ्, विद्यायोनिसंबन्धेभ्य इत्येव; वुञोऽपवादः.\n'
        '  होतुरागतं **हौतृकम्**, पौतृकम्; भ्रातृकम्, स्वासृकम्,\n'
        '  मातृकम्. **तपरकरणं मुखसुखार्थम्** — the त appended to\n'
        '  the ऋ is there for ease of pronunciation and takes\n'
        '  nothing out. विद्यायोनिभ्यामन्यत्र **सावित्रम्**.'
    ),
    '4.3.79': (
        'SETTLED — पितुर्यच्च. पितुरागतं **पित्र्यम्** by the यत्, and\n'
        '  **पैतृकम्** by the च, which brings the ठञ् of the last\n'
        '  rule along. One word taking two affixes where the\n'
        '  general rule for its class gave one.'
    ),
    '4.3.80': (
        'SETTLED — गोत्रादङ्कवत्. **अपत्याधिकारादन्यत्र लौकिकं गोत्रम्\n'
        '  अपत्यमात्रं गृह्यते** — outside the descendant section\n'
        '  गोत्र has its everyday sense, any offspring at all;\n'
        '  the same reading 4.2.39 took, and the same words used\n'
        '  for it.\n'
        '\n'
        'SETTLED — AN अतिदेश REACHING NINETY-SEVEN SŪTRAS\n'
        '  FORWARD. अङ्कग्रहणेन **तस्येदमर्थसामान्यं लक्ष्यते** —\n'
        '  the word *brand* stands for the general sense *this\n'
        '  belongs to that*, and **तस्माद् वुञप्यतिदिश्यते\n'
        '  नाणेव**: so the वुञ् is borrowed too and not only the\n'
        '  अण् of 4.3.127 सङ्घाङ्कलक्षणेष्वञ्यञिञामण्.\n'
        '  औपगवानामङ्कः औपगवकः, and so औपगवेभ्य आगतम्\n'
        '  औपगवकम्; कापटवकम्, नाडायनकम्, चारायणकम्.\n'
        '\n'
        '  The rule it borrows from is not codified yet. The row\n'
        '  names it and the answer says whose affixes are meant\n'
        '  rather than pretending to have them — the same shape\n'
        "  as 4.2.34's debt, which collected itself when 4.3.11\n"
        '  arrived.'
    ),
    '4.3.81': (
        'SETTLED — हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः. **हेतुः कारणम्**.\n'
        '  समादागतं समरूप्यम् beside समीयम्, विषमरूप्यम् beside\n'
        "  विषमीयम् — and the second form of each is 4.2.138's छ,\n"
        '  **गहादित्वात्**. From men: देवदत्तरूप्यम्,\n'
        '  यज्ञदत्तरूप्यम्, beside दैवदत्तम्, याज्ञदत्तम्.\n'
        '\n'
        'NOTE — **मनुष्यग्रहणमहेत्वर्थम्**: *man* is named for\n'
        '  the case where the man is not the CAUSE of the coming.'
    ),
    '4.3.82': (
        'SETTLED — मयट् च. सममयम्, विषममयम्; देवदत्तमयम्, यज्ञदत्तमयम्.\n'
        '  **टकारो ङीबर्थः** — the ट् is for the feminine,\n'
        '  सममयी.\n'
        '\n'
        'SETTLED — A SPLIT MADE TO STOP A CORRESPONDENCE.\n'
        '  **योगविभागो यथासंख्यनिरासार्थः** — read as one rule,\n'
        '  two affixes against two grounds would have paired in\n'
        '  order by 1.3.10, and neither affix would have reached\n'
        '  both. The fifth योगविभाग of this pāda, and the second\n'
        "  made for this particular reason: 4.3.2's split was\n"
        "  the first, and 4.3.21's, 4.3.44's and 4.3.90's are for\n"
        '  the sake of what follows instead.'
    ),
    '4.3.83': (
        'SETTLED — प्रभवति, तत इत्येव. **प्रभवति प्रकाशते, प्रथमत\n'
        '  उपलभ्यत इत्यर्थः** — rises, shows itself, is first\n'
        '  found. हिमवतः प्रभवति **हैमवती गङ्गा**, the Ganges\n'
        '  that rises from the Himālaya; **दारदी सिन्धुः**, the\n'
        '  Indus from Darada.'
    ),
    '4.3.84': (
        'SETTLED — विदूराञ्ञ्यः, अणोऽपवादः. विदूरात् प्रभवति **वैदूर्यो\n'
        '  मणिः** — the beryl, and the English word comes\n'
        '  through this one.\n'
        '\n'
        'SETTLED — AN OBJECTION ANSWERED WITH A VERSE THAT\n'
        '  OFFERS TWO WAYS OUT AND CHOOSES NEITHER. ननु च\n'
        '  वालवायादसौ प्रभवति, न विदूरात्, तत्र तु संस्क्रियते?\n'
        '  — the stone comes from Bālavāya and is only CUT at\n'
        '  Vidūra, so the rule has the wrong place. एवं तर्हि:\n'
        '  **वालवायो विदूरं च प्रकृत्यन्तरमेव वा / न वै तत्रेति\n'
        '  चेद् ब्रूयाज्जित्वरीवदुपाचरेत्** — either Bālavāya\n'
        '  and Vidūra are two separate bases, or, if someone\n'
        '  insists the stone is not from there, let him treat\n'
        '  the word as he treats जित्वरी.'
    ),
    '4.3.85': (
        'SETTLED — तद् गच्छति पथिदूतयोः. स्रुघ्नं गच्छति **स्रौघ्नः पन्था\n'
        '  दूतो वा**; माथुरः. The base stands in the ACCUSATIVE\n'
        '  — तदिति द्वितीयासमर्थात् — the fourth case this pāda\n'
        '  has used, after the locative, the nominative and the\n'
        '  ablative.\n'
        '\n'
        'SETTLED — AND TWO READINGS OF THE SAME METAPHOR, WITH\n'
        '  THE RULE WORKING ON EITHER. **तत्स्थेषु गच्छत्सु\n'
        '  पन्था गच्छतीत्युच्यते** — a road is said to *go*\n'
        '  because what is on it goes; अथ वा **स्रुघ्नप्राप्तिः\n'
        "  पथो गमनम्**, or else a road's going just IS its\n"
        '  reaching Srughna. The vṛtti offers both and needs\n'
        '  neither to be settled.\n'
        '\n'
        'NOTE — पथिदूतयोरिति किम्? **स्रुघ्नं गच्छति सार्थः** —\n'
        '  a caravan really does go, and gets nothing.'
    ),
    '4.3.86': (
        'SETTLED — अभिनिष्क्रामति द्वारम्, तदित्येव. **आभिमुख्येन\n'
        '  निष्क्रामति** — goes out FACING it.\n'
        '  स्रुघ्नमभिनिष्क्रामति कान्यकुब्जद्वारं **स्रौघ्नम्**,\n'
        '  the gate of Kanyakubja that opens toward Srughna;\n'
        '  माथुरम्, राष्ट्रियम्.\n'
        '\n'
        'SETTLED — AN INSTRUMENT SPOKEN OF AS AN AGENT.\n'
        '  **द्वारमभिनिष्क्रमणक्रियायां करणं प्रसिद्धम्, तदिह\n'
        '  स्वातन्त्र्येण विवक्ष्यते** — a gate is ordinarily\n'
        '  what one goes out BY, and here it is spoken of as\n'
        '  acting on its own, **तथा साध्वसिश्छिनत्ति**, as one\n'
        "  says *the good sword cuts*. 1.4.54's स्वतन्त्रः कर्ता\n"
        '  is what makes that possible, and this is a plain case\n'
        '  of it.\n'
        '\n'
        'NOTE — द्वारमिति किम्? स्रुघ्नमभिनिष्क्रामति पुरुषः.'
    ),
    '4.3.87': (
        'SETTLED — अधिकृत्य कृते ग्रन्थे, तदित्येव. **अधिकृत्य, प्रस्तुत्य,\n'
        '  आगूर्येत्यर्थः** — taking as its subject, introducing,\n'
        '  undertaking. सुभद्रामधिकृत्य कृतो ग्रन्थः\n'
        '  **सौभद्रः**; गैरिमित्रः, यायातः. ग्रन्थ इति किम्?\n'
        '  सुभद्रामधिकृत्य कृतः प्रासादः — a palace built in her\n'
        '  honour is not a book.\n'
        '\n'
        'NOTE — **लुबाख्यायिकाभ्यः प्रत्ययस्य बहुलम्**: for the\n'
        '  romances the affix is VARIOUSLY dropped, so the title\n'
        "  is the heroine's own name — **वासवदत्ता**,\n"
        '  सुमनोत्तरा, **उर्वशी**. न च भवति — भैमरथी, where it\n'
        "  stands. The same बहुलम् as 4.3.37's, and the same\n"
        '  reason for not calling it an option.'
    ),
    '4.3.88': (
        'SETTLED — शिशुक्रन्दयमसभद्वन्द्वेन्द्रजननादिभ्यश्छः, अणोऽपवादः.\n'
        '  शिशूनां क्रन्दनं शिशुक्रन्दः, तमधिकृत्य कृतो ग्रन्थः\n'
        '  **शिशुक्रन्दीयः**; यमसभीयः. From a द्वन्द्व —\n'
        '  अग्निकाश्यपीयः, श्येनकपोतीयः, **शब्दार्थसंबन्धीयं\n'
        '  प्रकरणम्**, and **वाक्यपदीयम्**, which is\n'
        "  Bhartṛhari's title made by this rule.\n"
        '  इन्द्रजननीयम्, प्रद्युम्नागमनीयम्.\n'
        '\n'
        'SETTLED — A LIST TO BE FOLLOWED FROM USAGE AND NOT\n'
        '  WRITTEN DOWN. **इन्द्रजननादिराकृतिगणः\n'
        '  प्रयोगतोऽनुसर्तव्यः, प्रातिपदिकेषु न पठ्यते** — the\n'
        '  list is open and to be followed from actual usage;\n'
        '  it is\n'
        '  not in the गणपाठ at all. The project has met open\n'
        '  lists before; this is the first that is not written\n'
        '  out anywhere.\n'
        '\n'
        'NOTE — a vārttika refuses one kind: **द्वन्द्वे\n'
        '  देवासुरादिभ्यः प्रतिषेधः** — दैवासुरम्, राक्षोऽसुरम्,\n'
        '  गौणमुख्यम्. And the vṛtti then observes that if\n'
        '  इन्द्रजननादि is an आकृतिगण the earlier members belong\n'
        '  in it too, **प्रपञ्चार्थमेषां ग्रहणम्**, and the\n'
        '  refusal need not have been stated either.'
    ),
    '4.3.89': (
        'SETTLED — सोऽस्य निवासः. **निवसन्त्यस्मिन्निवासो देश उच्यते** — a\n'
        '  निवास is the place people live in. स्रुघ्नो निवासोऽस्य\n'
        '  **स्रौघ्नः**; माथुरः, राष्ट्रियः. The base is\n'
        '  प्रथमासमर्थ and the relation is the genitive of\n'
        "  अस्य — the same shape as 4.3.52's, and the fifth case\n"
        '  this pāda has used.'
    ),
    '4.3.90': (
        'SETTLED — अभिजनश्च, सोऽस्येत्येव. **अभिजनः पूर्वबान्धवः** — the\n'
        '  forebears; तत्संबन्धाद् देशोऽप्यभिजन इत्युच्यते,\n'
        '  **यस्मिन् पूर्वबान्धवैरुषितम्**, the place they lived\n'
        '  in. तस्माद् इह देशवाचिनः प्रत्ययः, न बन्धुभ्यः,\n'
        '  **निवासप्रत्यासत्तेः** — so the affix comes from the\n'
        '  PLACE-word and not from the kinsmen, because the last\n'
        '  rule was about a place and this one stands next to it.\n'
        '\n'
        'SETTLED — TWO RULES, IDENTICAL OUTPUTS, AND THE\n'
        '  DIFFERENCE ENTIRELY IN WHAT IS BEING REPORTED.\n'
        '  **निवासाभिजनयोः को विशेषः? यत्र संप्रत्युष्यते स\n'
        '  निवासः, यत्र पूर्वैरुषितं सोऽभिजनः** — where a man\n'
        '  lives NOW and where his forebears lived. स्रौघ्नः\n'
        '  either way, and nothing in the form says which.\n'
        '\n'
        'NOTE — **योगविभाग उत्तरार्थः**, and the split is for\n'
        '  the sake of what follows.'
    ),
    '4.3.91': (
        'SETTLED — आयुधजीविभ्यश्छः पर्वते, सोऽस्याभिजन इति वर्तते.\n'
        '  **आयुधजीविभ्य इति तादर्थ्ये चतुर्थी, पर्वत इति\n'
        '  प्रकृतिविशेषणम्** — the dative is *for the sake of*,\n'
        '  so the WEAPON-BEARERS are what the derived word is to\n'
        '  denote, and *mountain* qualifies the base instead.\n'
        '  हृद्गोलः पर्वतोऽभिजन एषामायुधजीविनां **हृद्गोलीयाः**;\n'
        '  अन्धकवर्तीयाः, रोहितगिरीयाः.\n'
        '\n'
        'NOTE — a counter-example for each condition.\n'
        '  आयुधजीविभ्य इति किम्? **आर्क्षोदा ब्राह्मणाः**,\n'
        '  brahmins and not soldiers. पर्वत इति किम्?\n'
        '  **सांकाश्यका आयुधजीविनः**, soldiers whose ancestral\n'
        '  place is not a mountain.'
    ),
    '4.3.92': (
        'SETTLED — शण्डिकादिभ्यो ञ्यः, अणादेरपवादः. शाण्डिक्यः,\n'
        '  सार्वसेन्यः.'
    ),
    '4.3.93': (
        'SETTLED — सिन्धुतक्षशिलादिभ्योऽणञौ, यथासंख्यम्. **आदिशब्दः\n'
        '  प्रत्येकमभिसंबध्यते** — *and-the-rest* attaches to\n'
        '  each of the two lists separately. सैन्धवः, वार्णवः;\n'
        '  ताक्षशिलः, वात्सोद्धरणः.\n'
        '\n'
        'NOTE — **ये तु कच्छादिषु पठ्यन्ते सिन्धुवर्णुप्रभृतयः,\n'
        '  तेभ्यस्तत एवाणि सिद्धे मनुष्यवुञो बाधनार्थं वचनम्**:\n'
        "  the first few of the first list are in 4.2.133's\n"
        '  कच्छादि already, so the अण् was coming from there —\n'
        "  the rule is spoken to keep 4.2.134's वुञ् out."
    ),
    '4.3.94': (
        'SETTLED — तूदीशलातुरवर्मतीकूचवाराड्ढक्छण्ढञ्यकः, यथासंख्यम्;\n'
        '  अणोऽपवादः. तौदेयः, **शालातुरीयः**, वार्मतेयः,\n'
        '  कौचवार्यः.\n'
        '\n'
        'SETTLED — FOUR BASES AND FOUR AFFIXES, MATCHED IN ORDER.\n'
        "  The tightest correspondence in this pāda: 4.3.1's two\n"
        '  bases against three affixes could not run at all, and\n'
        "  4.3.33's two against two hardly had to be checked.\n"
        '\n'
        'NOTE — and शालातुरीय, *the man of Śalātura*, is the\n'
        '  word by which Pāṇini himself is known. It is made by\n'
        '  his own rule, and by the second of these four affixes.'
    ),
    '4.3.95': (
        'SETTLED — भक्तिः. **समर्थविभक्तिः प्रत्ययार्थश्चानुवर्तते;\n'
        '  अभिजन इति निवृत्तम्** — the case and the relation\n'
        '  carry over from 4.3.89 and the ancestral home lapses.\n'
        '  **भज्यते सेव्यत इति भक्तिः**: devotion is what one is\n'
        '  devoted to. स्रुघ्नो भक्तिरस्य स्रौघ्नः.\n'
        '\n'
        'NOTE — a one-word sūtra. Everything else in it — the\n'
        '  nominative base, the genitive relation, the affix —\n'
        '  is carried from rules already stated.'
    ),
    '4.3.96': (
        'SETTLED — अचित्तादेशकालाट् ठक्, अणोऽपवादः; **वृद्धाच् छं परत्वाद्\n'
        '  बाधते**. अपूपो भक्तिरस्य **आपूपिकः**, the man devoted\n'
        '  to cakes; शाष्कुलिकः, पायसिकः.\n'
        '\n'
        'NOTE — three conditions and a counter-example for each.\n'
        '  अचित्तादिति किम्? दैवदत्तः. अदेशादिति किम्? स्रौघ्नः.\n'
        '  अकालादिति किम्? ग्रैष्मः. The rule takes what is\n'
        '  neither sentient, nor a place, nor a time — a\n'
        '  condition stated entirely by subtraction.'
    ),
    '4.3.97': (
        'SETTLED — महाराजाट् ठञ्, अणोऽपवादः. महाराजो भक्तिरस्य\n'
        '  **माहाराजिकः**. **प्रत्ययान्तरकरणं स्वरार्थम्** — a\n'
        '  different affix given for the sake of the accent, the\n'
        '  same reason 4.3.49 gave one.'
    ),
    '4.3.98': (
        'SETTLED — वासुदेवार्जुनाभ्यां वुन्, छाणोरपवादः. वासुदेवो\n'
        '  भक्तिरस्य **वासुदेवकः**; अर्जुनकः.\n'
        '\n'
        'SETTLED — WHY NAME THE FIRST WORD AT ALL? ननु च\n'
        '  वासुदेवशब्दाद् गोत्रक्षत्रियाख्येभ्यः इति वुञस् त्येव,\n'
        '  **न चात्र वुन्वुञोर्विशेषो विद्यते, किमर्थं\n'
        '  वासुदेवग्रहणम्?** — the next rule gives वुञ् from a\n'
        '  kṣatriya name, and वुन् and वुञ् differ in nothing\n'
        '  here. **संज्ञैषा देवताविशेषस्य न क्षत्रियाख्या**: the\n'
        '  word is the name of a GOD and not of a kṣatriya, so\n'
        '  the next rule would never have reached it.\n'
        '\n'
        'SETTLED — AND A PRINCIPLE OF COMPOUNDING TAUGHT BY THE\n'
        '  ORDER OF TWO WORDS. **अल्पाच्तरम्** [2.2.34] and\n'
        '  **अजाद्यदन्तम्** [2.2.33] should both have put अर्जुन\n'
        '  first in the dvandva — it is shorter and it begins\n'
        '  with a vowel. Declining to obey either, the rule\n'
        '  **ज्ञापयति — अभ्यर्हितं पूर्वं निपततीति**: the more\n'
        '  venerated goes first. A general rule of word order\n'
        "  established by one rule's refusal to follow two."
    ),
    '4.3.99': (
        'SETTLED — गोत्रक्षत्रियाख्येभ्यो बहुलं वुञ्, अणोऽपवादः; वृद्धाच्\n'
        '  छं परत्वाद् बाधते. ग्लुचुकायनिर्भक्तिरस्य\n'
        '  **ग्लौचुकायनकः**; औपगवकः, कापटवकः; and from kṣatriya\n'
        '  names नाकुलकः, साहदेवकः, साम्बकः.\n'
        '\n'
        'NOTE — **आख्याग्रहणं प्रसिद्धक्षत्रियशब्दपरिग्रहार्थम्,\n'
        '  यथाकथंचित् क्षत्रियवृत्तिभ्यो मा भूत्**: *name* is\n'
        '  there to take in the WELL-KNOWN kṣatriya words and\n'
        '  keep out anything that merely behaves like one.\n'
        '\n'
        'NOTE — and **बहुलग्रहणात् क्वचिदप्रवृत्तिरेव**: because\n'
        '  the rule says *variously*, in some places it simply\n'
        '  does not apply. पाणिनो भक्तिरस्य **पाणिनीयः**,\n'
        '  पौरवीयः.'
    ),
    '4.3.100': (
        'SETTLED — जनपदिनां जनपदवत् सर्वं जनपदेन समानशब्दानां बहुवचने.\n'
        '  **जनपदिनो जनपदस्वामिनः क्षत्रियाः** — the kṣatriyas\n'
        '  who own a district and are called by the same word as\n'
        '  the district. अङ्गा जनपदो भक्तिरस्य आङ्गकः, and\n'
        '  तद्वद् **अङ्गाः क्षत्रिया भक्तिरस्य आङ्गकः**.\n'
        '\n'
        'SETTLED — AN अतिदेश REACHING BACKWARD, AND THIS ONE CAN\n'
        "  BE RUN. 4.2.124's section is where the affixes come\n"
        '  from — ये प्रत्यया विहिताः, ते जनपदिभ्योऽस्मिन्नर्थे\n'
        '  ऽतिदिश्यन्ते. That rule is codified, so the code\n'
        "  answers this one by ASKING it. 4.3.80's forward-\n"
        '  reaching अतिदेश can still only name what it means,\n'
        '  and the two together show both halves of the same\n'
        '  instrument twenty sūtras apart.\n'
        '\n'
        'SETTLED — AND *ALL* IS THERE FOR THE BASE, NOT THE\n'
        '  AFFIX. **सर्वग्रहणं प्रकृत्यतिदेशार्थम्, स च\n'
        '  द्व्येकयोः प्रयोजयति** — it does its work in the\n'
        '  singular and the dual. मद्रस्यापत्यं माद्रः by\n'
        '  4.1.170, and स भक्तिरस्य: **प्रकृतिनिर्ह्रासे कृते\n'
        "  मद्रकः**, the base cut back to मद्र and 4.2.131's\n"
        '  कन् given. Nothing but a base-transfer could have\n'
        '  produced that.\n'
        '\n'
        'NOTE — **बहुवचनग्रहणं समानशब्दताविषयलक्षणार्थम्**: the\n'
        '  plural marks the DOMAIN in which the two words are\n'
        '  the same, not the number the rule applies in. अन्यथा\n'
        '  हि यत्रैव समानशब्दता तत्रैवातिदेशः स्याद्,\n'
        '  एकवचनद्विवचनयोर्न स्यात् — so वाङ्गो वाङ्गौ वा\n'
        '  भक्तिरस्य **वाङ्गकः**. जनपदेन समानशब्दानामिति किम्?\n'
        '  अनुषण्डो जनपदः, पौरवो राजा, स भक्तिरस्य पौरवीयः.'
    ),
    '4.3.101': (
        'SETTLED — तेन प्रोक्तम्. **प्रकर्षेणोक्तं प्रोक्तमित्युच्यते, न\n'
        '  तु कृतम्, कृते ग्रन्थे इत्यनेन गतार्थत्वात्** —\n'
        '  प्रोक्त is *set forth*, and NOT *made*, because\n'
        '  4.3.116 has making already. The third time in this\n'
        '  pāda that a sense is fixed by subtracting what a\n'
        '  neighbouring rule took, and this time across fifteen\n'
        '  sūtras.\n'
        '\n'
        '  **अन्येन कृता, माथुरेण प्रोक्ता माथुरी वृत्तिः** — a\n'
        '  commentary composed by one man and expounded by\n'
        '  another, and the affix reports the second. पाणिनीयम्,\n'
        '  आपिशलम्, काशकृत्स्नम्: three grammars named by their\n'
        '  teachers.'
    ),
    '4.3.102': (
        'SETTLED — तित्तिरिवरतन्तुखण्डिकोखाच्छण्, अणोऽपवादः. तित्तिरिणा\n'
        '  प्रोक्तमधीयते **तैत्तिरीयाः** — the name of a whole\n'
        '  recension of the Yajurveda. वारतन्तवीयाः,\n'
        '  खाण्डिकीयाः, औखीयाः.\n'
        '\n'
        'NOTE — **छन्दसि चायमिष्यते**: the affix is wanted for\n'
        '  the Veda, and तित्तिरिणा प्रोक्तः श्लोक इत्यत्र न\n'
        '  भवति — it does not reach an ordinary verse he set\n'
        "  forth, because 4.3.106's छन्दसि is carried back into\n"
        '  this rule. Anuvṛtti running BACKWARD, which is rare.'
    ),
    '4.3.103': (
        'SETTLED — काश्यपकौशिकाभ्यामृषिभ्यां णिनिः, छस्यापवादः. **णकार\n'
        '  उत्तरत्र वृद्ध्यर्थः** — the ण् is for the\n'
        '  strengthening in the rules that follow. काश्यपेन\n'
        '  प्रोक्तं कल्पमधीयते **काश्यपिनः**; कौशिकिनः.\n'
        '\n'
        'NOTE — ऋषिभ्यामिति किम्? **इदानींतनेन गोत्रकाश्यपेन\n'
        '  प्रोक्तं काश्यपीयम्** — set forth by a present-day\n'
        '  man of the Kāśyapa line and not by the seer. The\n'
        '  same word, and which affix it takes turns on which\n'
        '  man is meant.'
    ),
    '4.3.104': (
        'SETTLED — कलापिवैशंपायनान्तेवासिभ्यश्च, अणोऽपवादः; छं तु परत्वाद्\n'
        "  बाधते. Kalāpin's four pupils — हरिद्रुः, छगली,\n"
        '  तुम्बुरुः, उलप — give हारिद्रविणः, तौम्बुरविणः,\n'
        "  औलपिनः. Vaiśampāyana's nine — आलम्बिः, पलङ्गः, कमलः,\n"
        '  ऋचाभः, आरुणिः, ताण्ड्यः, श्यामायनः, कठः, कलापी —\n'
        '  give आलम्बिनः, पालङ्गिनः, कामलिनः, आर्चाभिनः,\n'
        '  आरुणिनः, ताण्डिनः, श्यामायनिनः.\n'
        '\n'
        'SETTLED — ONLY THE DIRECT PUPILS, AND THE LISTS\n'
        '  THEMSELVES PROVE IT. प्रत्यक्षकारिणो गृह्यन्ते,\n'
        '  **न तु व्यवहिताः शिष्यशिष्याः** — pupils of pupils\n'
        '  are out. कुतः? **कलापिखाडायनग्रहणात्**. कलापी stands\n'
        "  in this very list as Vaiśampāyana's pupil, so were\n"
        '  the rule transitive his own pupils would already be\n'
        '  in — and yet 4.3.108 gives him a rule of his own. कठ\n'
        '  likewise is in the list, and his pupil खाडायन is read\n'
        "  separately in 4.3.106's. **तदेतत्\n"
        '  प्रत्यक्षकारिग्रहणस्य लिङ्गम्**: two redundancies\n'
        '  that are redundant only on the wrong reading, and\n'
        '  together they settle it.\n'
        '\n'
        'NOTE — three verses list the thirteen, and **चरक इति\n'
        '  वैशंपायनस्याख्या, तत्संबन्धेन सर्वे\n'
        '  तदन्तेवासिनश्चरका इत्युच्यन्ते** — चरक is\n'
        "  Vaiśampāyana's own name, and by it the whole school\n"
        '  is called the Carakas. Which is what lets 4.3.107\n'
        '  reach all of them with one word.'
    ),
    '4.3.105': (
        'SETTLED — पुराणप्रोक्तेषु ब्राह्मणकल्पेषु.\n'
        '  **प्रत्ययार्थविशेषणमेतत्** — it qualifies what the\n'
        '  affix denotes. **पुराणेन चिरन्तनेन मुनिना प्रोक्ताः**,\n'
        '  set forth by an ANCIENT sage. भाल्लविनः,\n'
        '  शाट्यायनिनः, ऐतरेयिणः; and among the kalpas पैङ्गी\n'
        '  कल्पः, आरुणपराजी.\n'
        '\n'
        'SETTLED — AND THE GRAMMAR DATES ITS OWN TEXTS BY WHAT\n'
        '  PEOPLE SAY. पुराणप्रोक्तेष्विति किम्? **याज्ञवल्कानि\n'
        '  ब्राह्मणानि**, आश्मरथः कल्पः — why are those out?\n'
        '  **याज्ञवल्क्यादयोऽचिरकाला इत्याख्यानेषु वार्ता, तया\n'
        '  व्यवहरति सूत्रकारः**: the story goes in the\n'
        '  traditions that Yājñavalkya and the rest are recent,\n'
        '  and the sūtra-maker goes by that. A grammatical rule\n'
        '  resting on a chronology the grammar does not itself\n'
        '  establish and does not claim to.\n'
        '\n'
        'NOTE — **पुराण इति निपातनात् तुडभावः**: the shape\n'
        '  पुराण is laid down here without the तुट् that would\n'
        '  otherwise come, and **न चात्यन्तबाधैव, तेन पुरातनम्\n'
        '  इत्यपि भवति** — the other form is not thereby\n'
        '  forbidden.'
    ),
    '4.3.106': (
        'SETTLED — शौनकादिभ्यश्छन्दसि, छाणोरपवादः. शौनकेन प्रोक्तमधीयते\n'
        '  **शौनकिनः** (कौषीतकिसूत्र ८५.८); **वाजसनेयिनः**\n'
        '  (आपस्तम्बश्रौत १.८.१२) — which is how the\n'
        '  Vājasaneyins are named.\n'
        '\n'
        'NOTE — छन्दसीति किम्? **शौनकीया शिक्षा**, a treatise\n'
        '  and not scripture. And **कठशाठ इत्यत्र पठ्यते; तत्\n'
        '  संघातार्थम्, केवलाद् धि लुकं वक्ष्यति**: the\n'
        "  compound कठशाठ is in the list for the compound's\n"
        '  sake only, since from कठ alone the next rule elides.\n'
        '  काठशाठिनः.'
    ),
    '4.3.107': (
        'SETTLED — कठचरकाल्लुक्. कठेन प्रोक्तमधीयते **कठाः**; **चरकाः** —\n'
        '  the affix given and taken away, so a school is called\n'
        "  by its teacher's own name. From कठ what goes is\n"
        "  4.3.104's णिनि; from चरक, the अण्. छन्दसीत्येव —\n"
        '  काठाः, चारकाः.\n'
        '\n'
        "NOTE — and चरक is Vaiśampāyana's own name, so this one\n"
        '  word reaches the whole school that the list of nine\n'
        '  belongs to.'
    ),
    '4.3.108': (
        'SETTLED — कलापिनोऽण्. **वैशंपायनान्तेवासित्वाद् णिनेरपवादः** —\n'
        '  कलापी is in the list of nine, so this beats the णिनि\n'
        '  that rule would have given. कलापिना प्रोक्तमधीयते\n'
        '  **कालापाः**.\n'
        '\n'
        'NOTE — the form needs a vārttika. 6.4.164 इनण्यनपत्ये\n'
        '  would have kept the stem whole; **नान्तस्य टिलोपे\n'
        '  ... कलापि ... उपसंख्यानम्** drops the टि instead.\n'
        '\n'
        'NOTE — अथाण्ग्रहणं किम्, यथाप्राप्तमित्येव सिद्धम्?\n'
        '  **अधिकविधानार्थम्** — the affix is named in order to\n'
        '  give MORE than would have come anyway: माथुरी वृत्तिः,\n'
        '  सौलभानि ब्राह्मणानि and the like are got by it.'
    ),
    '4.3.109': (
        'SETTLED — छगलिनो ढिनुक्. **कलाप्यन्तेवासित्वाद् णिनेरपवादः** —\n'
        '  छगली is in the list of four. छगलिना प्रोक्तमधीयते\n'
        '  **छागलेयिनः**.'
    ),
    '4.3.110': (
        'SETTLED — पाराशर्यशिलालिभ्यां भिक्षुनटसूत्रयोः. **णिनिरिहानुवर्तते,\n'
        "  न ढिनुक्** — the णिनि carries and the last rule's\n"
        '  affix does not. यथासंख्यम्, and **सूत्रशब्दः\n'
        '  प्रत्येकमभिसंबध्यते**: *aphorisms* attaches to each,\n'
        "  so it is the BEGGARS' aphorisms and the ACTORS'.\n"
        '  पाराशरिणो **भिक्षवः**; शैलालिनो **नटाः**.\n'
        '\n'
        'NOTE — भिक्षुनटसूत्रयोरिति किम्? पाराशरम्, शैलालम्.'
    ),
    '4.3.111': (
        'SETTLED — कर्मन्दकृशाश्वादिनिः, भिक्षुनटसूत्रयोरित्येव;\n'
        '  अणोऽपवादः; यथासंख्यम्. कर्मन्दिनो भिक्षवः;\n'
        '  कृशाश्विनो नटाः. भिक्षुनटसूत्रयोरित्येव — कार्मन्दम्,\n'
        '  कार्शाश्वम्.'
    ),
    '4.3.112': (
        'SETTLED — तेनैकदिक्. **एकदिक् तुल्यदिक्, समानदिगित्यर्थः** —\n'
        '  lying in the same direction as that. सुदाम्ना एकदिक्\n'
        '  **सौदामनी विद्युत्**, the lightning on a line with\n'
        '  Sudāman; हैमवती, त्रैककुदी, पैलुमूली.\n'
        '\n'
        'NOTE — **तेनेति प्रकृते पुनः समर्थविभक्तिग्रहणं\n'
        '  छन्दोऽधिकारनिवृत्त्यर्थम्**: तेन was already\n'
        '  carrying, and it is said AGAIN in order to cancel the\n'
        '  Vedic heading. A word repeated to push another out,\n'
        '  as at 4.3.53.'
    ),
    '4.3.113': (
        'SETTLED — तसिश्च. **पूर्वेण घादिष्वणादिषु च प्राप्तेष्वयमपरः\n'
        '  प्रत्ययो विधीयते** — the last rule had घ and अण् and\n'
        '  the rest available, and this gives one more besides.\n'
        '  सुदामतः, हिमवत्तः, पिलुमूलतः.\n'
        '  **स्वरादिपाठादव्ययत्वम्**: the result is\n'
        '  indeclinable, because तसि is read in the स्वरादि\n'
        '  list.'
    ),
    '4.3.114': (
        'SETTLED — उरसो यच्च, अणोऽपवादः. उरसैकदिग् **उरस्यः** by the यत्,\n'
        '  and **उरस्तः** by the च, which brings the last\n'
        "  rule's तसि along."
    ),
    '4.3.115': (
        'SETTLED — उपज्ञाते, तेनेत्येव. **विनोपदेशेन ज्ञातमुपज्ञातम्,\n'
        '  स्वयमभिसंबुद्धमित्यर्थः** — known WITHOUT being\n'
        '  taught, worked out for oneself. पाणिनिनोपज्ञातं\n'
        '  **पाणिनीयमकालकं व्याकरणम्**, the tenseless grammar\n'
        '  Pāṇini found out himself; काशकृत्स्नं गुरुलाघवम्,\n'
        '  आपिशलं दुष्करणम्.'
    ),
    '4.3.116': (
        'SETTLED — कृते ग्रन्थे, तेनेत्येव. वररुचिना कृता **वाररुचाः\n'
        '  श्लोकाः**; हैकुपादो ग्रन्थः, भैकुराटो ग्रन्थः,\n'
        '  जालूकः. ग्रन्थ इति किम्? **तक्षकृतः प्रासादः**.\n'
        '\n'
        'SETTLED — AND THE DIFFERENCE FROM THE RULE BEFORE IT.\n'
        '  **उत्पादितं कृतम्, विद्यमानमेव ज्ञातमुपज्ञातम्\n'
        '  इत्ययमनयोर्विशेषः** — what is MADE is brought into\n'
        '  being; what is DISCOVERED was already there and came\n'
        '  to be known. Two rules one sūtra apart, and the whole\n'
        '  difference is whether the thing existed first.'
    ),
    '4.3.117': (
        'SETTLED — संज्ञायाम्. **समुदायेन चेत् संज्ञा ज्ञायते** — if the\n'
        '  NAME is known from the whole. मक्षिकाभिः कृतं\n'
        '  **माक्षिकम्**; कार्मुकम्, सारघम्, पौत्तिकम् —\n'
        '  **मधुनः संज्ञा एताः**, and all four are names for\n'
        '  kinds of honey, each called after the bee that made\n'
        '  it.'
    ),
    '4.3.118': (
        'SETTLED — कुलालादिभ्यो वुञ्. **तेन, कृते, संज्ञायामिति चैतत्\n'
        '  सर्वमनुवर्तते** — the instrumental, the making and\n'
        '  the name all carry. कौलालकम्, वारुडकम्.'
    ),
    '4.3.119': (
        'SETTLED — क्षुद्राभ्रमरवटरपादपादञ्, अणोऽपवादः; **स्वरे विशेषः**,\n'
        '  and the two affixes differ only in the accent.\n'
        '  क्षुद्राभिः कृतं **क्षौद्रम्**, honey made by the\n'
        '  small bees; भ्रामरम्, वाटरम्, पादपम् — and these too\n'
        '  are honeys, named by which bee made them.'
    ),
    '4.3.120': (
        'SETTLED — तस्येदम्. उपगोरिदम् **औपगवम्**; कापटवम्, राष्ट्रियम्,\n'
        '  अवारपारीणम्. **अणादयः पञ्च महोत्सर्गाः, घादयश्च\n'
        '  प्रत्यया यथाविहितं विधीयन्ते** — five GREAT general\n'
        '  rules stand behind this one.\n'
        '\n'
        'SETTLED — AND EVERYTHING BUT THE RELATION IS LEFT OUT\n'
        '  OF ACCOUNT. प्रकृतिप्रत्ययार्थयोः **षष्ठ्यर्थमात्रं\n'
        '  तत्संबन्धिमात्रं च विवक्षितम्, यदपरं\n'
        '  लिङ्गसंख्याप्रत्यक्षपरोक्षादिकं तत् सर्वमविवक्षितम्**\n'
        '  — only the genitive relation and the bare fact of\n'
        '  being related are meant; gender, number, whether the\n'
        "  thing is before one's eyes or out of sight, none of\n"
        '  it is. The widest sense in the taddhita section, and\n'
        '  the vṛtti states the price of it.\n'
        '\n'
        'NOTE — **अनन्तरादिष्वनभिधानाद् न भवति**: it does not\n'
        '  reach देवदत्तस्यानन्तरम्, because that is not how the\n'
        '  language says it — usage again, as at 4.3.12. Three\n'
        '  vārttikas add particular shapes: संवहेस्तुरणिट् च,\n'
        '  **सांवहित्रम्**; अग्नीधः शरणे रञ् भं च,\n'
        '  **आग्नीध्रम्**; समिधामाधाने षेण्यण्, **सामिधेन्यो\n'
        '  मन्त्रः** and सामिधेनी ऋक्.'
    ),
    '4.3.121': (
        'SETTLED — रथाद् यत्, अणोऽपवादः. रथस्येदं **रथ्यम्**, चक्रं वा\n'
        '  युगं वा — a wheel or a yoke.\n'
        '\n'
        'NOTE — **रथाङ्ग एवेष्यते नान्यत्र, अनभिधानात्**: only\n'
        '  of a PART of the chariot and nowhere else, because\n'
        '  that is not how the word is used. And a Mahābhāṣya\n'
        '  vārttika on 1.1.72, **रथसीताहलेभ्यो यद्विधौ**, adds\n'
        '  that the rule reaches compounds ending in these\n'
        '  words: परमरथ्यम्, उत्तमरथ्यम्.'
    ),
    '4.3.122': (
        'SETTLED — पत्रपूर्वादञ्, पूर्वस्य यतोऽपवादः. **पतन्ति तेनेति\n'
        '  पत्रम्** — a पत्र is what one travels by, a mount.\n'
        '  आश्वरथं चक्रम्, औष्ट्ररथम्, गार्दभरथम्: the wheel of\n'
        '  a horse-chariot, of a camel-chariot, of a\n'
        '  donkey-chariot.'
    ),
    '4.3.123': (
        'SETTLED — पत्राध्वर्युपरिषदश्च, अणोऽपवादः. **पत्रं वाहनम्**, and\n'
        '  a vārttika reads **पत्राद् वाह्ये**, only of what is\n'
        '  CARRIED by it. अश्वस्येदं वहनीयम् **आश्वम्**;\n'
        '  औष्ट्रम्, गार्दभम्. And from the two named words,\n'
        '  आध्वर्यवम्, पारिषदम्.'
    ),
    '4.3.124': (
        'SETTLED — हलसीराट् ठक्, अणोऽपवादः. हलस्येदं **हालिकम्**;\n'
        '  सैरिकम्.'
    ),
    '4.3.125': (
        'SETTLED — द्वन्द्वाद् वुन् वैरमैथुनिकयोः, अणोऽपवादः; छं तु\n'
        '  परत्वाद् बाधते. The two conditions qualify what the\n'
        '  affix denotes: a FEUD or an INTERMARRIAGE between\n'
        '  the two families the dvandva names.\n'
        '  **बाभ्रव्यशालङ्कायनिका**, the feud of the Bābhravyas\n'
        '  and the Śālaṅkāyanas; **काकोलूकिका**, of crows and\n'
        '  owls; अत्रिभरद्वाजिका, कुत्सकुशिकिका. **विवहनं\n'
        '  मैथुनिका.**\n'
        '\n'
        'NOTE — **वैरस्य नपुंसकत्वेऽप्यमी स्वभावतः\n'
        '  स्त्रीलिङ्गाः**: though वैर is neuter these forms\n'
        '  are feminine by their own nature. And a vārttika\n'
        '  refuses one kind — **वैरे देवासुरादिभ्यः\n'
        '  प्रतिषेधः**, दैवासुरम्, राक्षोऽसुरं वैरम् — the\n'
        '  same refusal 4.3.88 needed, for the same list.'
    ),
    '4.3.126': (
        'SETTLED — गोत्रचरणाद् वुञ्, अणोऽपवादः; छं तु परत्वाद् बाधते.\n'
        '  From a lineage — ग्लौचुकायनकम्, **औपगवकम्**. And a\n'
        '  vārttika narrows the other half: **चरणाद्\n'
        '  धर्माम्नाययोरिष्यते**, from a Vedic SCHOOL only when\n'
        '  its rule of life or its tradition is meant —\n'
        '  काठकम्, कालापकम्, मौदकम्, पैप्पलादकम्.\n'
        '\n'
        "NOTE — and this is the rule 4.3.80's अतिदेश actually\n"
        '  reaches. That rule says अङ्कवत् and so points at\n'
        '  4.3.127, but the words its examples are built on end\n'
        '  in अण् and not in अञ्, यञ् or इञ् — which is exactly\n'
        '  why the vṛtti there insists **तस्माद्\n'
        '  वुञप्यतिदिश्यते नाणेव**.'
    ),
    '4.3.127': (
        'SETTLED — संघाङ्कलक्षणेष्वञ्यञिञामण्, पूर्वस्य वुञोऽपवादः. Three\n'
        '  kinds of base and three conditions on what the affix\n'
        '  denotes — a BODY of men, a BRAND, a MARK — and a\n'
        '  vārttika adds a fourth, **घोषग्रहणमत्र कर्तव्यम्**,\n'
        '  a settlement.\n'
        '\n'
        'SETTLED — AND WITH FOUR AGAINST THREE THE PAIRING\n'
        '  CANNOT RUN. **तेन वैषम्याद् यथासंख्यं न भवति** — so\n'
        '  every base takes every sense: बैदः संघः, बैदोऽङ्कः,\n'
        '  बैदं लक्षणम्, बैदो घोषः; गार्गः and दाक्षः the same.\n'
        '  The same argument 4.3.1 made of two against three,\n'
        '  and here it is a vārttika that creates the\n'
        '  inequality.\n'
        '\n'
        'SETTLED — AND WHAT SEPARATES A BRAND FROM A MARK.\n'
        '  **अङ्कलक्षणयोः को विशेषः? लक्षणं लक्ष्यस्यैव\n'
        "  चिह्नभूतं स्वं**, a mark is the thing's OWN, यथा\n"
        "  विद्या बिदानाम् — as learning is the Bidas'; **अङ्कस्\n"
        '  तु गवादिस्थोऽपि गवादीनां स्वं न भवति**, a brand\n'
        '  stands on the cattle and still is not theirs.\n'
        '\n'
        'NOTE — **णित्करणं ङीबर्थं पुंवद्भावप्रतिषेधार्थं च**:\n'
        '  the ण् is for the feminine ङीप् and to stop 6.3.34\n'
        '  from treating that feminine as a masculine —\n'
        '  बैदी विद्यास्य बैदीविद्यः.\n'
        '\n'
        'NOTE — and this is the rule 4.3.80 reaches forward to.\n'
        '  That debt was written as the exact shortfall, a test\n'
        '  asserting this sūtra was NOT codified, and it\n'
        '  collects itself here.'
    ),
    '4.3.128': (
        'SETTLED — शाकलाद् वा, वुञोऽपवादः. शाकल्येन प्रोक्तमधीयते\n'
        '  शाकलाः, तेषां संघः **शाकलः** beside **शाकलकः**;\n'
        '  शाकलोऽङ्कः beside शाकलकोऽङ्कः, and so for the mark\n'
        '  and the settlement. Four conditions and two forms\n'
        '  under each.'
    ),
    '4.3.129': (
        'SETTLED — छन्दोगौक्थिकयाज्ञिकबह्वृचनटाञ् ञ्यः, वुञणोरपवादः.\n'
        '  **संघादयो निवृत्ताः, सामान्येन विधानम्** — the four\n'
        '  conditions of the last rules have lapsed and this\n'
        '  one is general.\n'
        '\n'
        'SETTLED — BUT A RESTRICTION CARRIES BY ASSOCIATION TO\n'
        '  A WORD IT CANNOT LITERALLY FIT. **चरणाद्\n'
        '  धर्माम्नाययोः, तत्साहचर्याद् नटशब्दादपि\n'
        "  धर्माम्नाययोरेव भवति** — the school-vārttika's\n"
        '  restriction reaches even नट, which is not a school\n'
        '  at all, because it keeps company with four that are.\n'
        '  छान्दोग्यम्, औक्थिक्यम्, याज्ञिक्यम्, बाह्वृच्यम्,\n'
        '  **नाट्यम्** — and the last of those is the ordinary\n'
        '  word for dramatic art. अन्यत्र छान्दोगं कुलम्.'
    ),
    '4.3.130': (
        'SETTLED — न दण्डमाणवान्तेवासिषु. **दण्डप्रधाना माणवा\n'
        '  दण्डमाणवाः**, boys carrying staves; अन्तेवासिनः\n'
        '  शिष्याः, pupils. Where THEY are what is meant the\n'
        '  affix does not come. गौकक्षाः दण्डमाणवा अन्तेवासिनो\n'
        '  वा; दाक्षाः, माहकाः.\n'
        '\n'
        'SETTLED — AND THE REFUSAL IDENTIFIES ITS TARGET BY\n'
        '  WHAT IT INHERITS. **गोत्रग्रहणमिहानुवर्तते, तेन\n'
        '  वुञ्प्रतिषेधो विज्ञायते** — the lineage-word carries\n'
        '  into this rule, and that is how one knows it is\n'
        "  4.3.126's वुञ् that is refused and not some other\n"
        '  affix. The only प्रतिषेध in this pāda, and it says\n'
        '  what it refuses by saying what it kept.'
    ),
    '4.3.131': (
        'SETTLED — रैवतिकादिभ्यश्छः. **गोत्रप्रत्ययान्ता एते, ततः\n'
        '  पूर्वेण वुञि प्राप्ते छविधानार्थं वचनम्** — every\n'
        '  member of this list already ends in a lineage-affix,\n'
        '  so 4.3.126 had them; the rule exists in order to give\n'
        '  छ instead. रैवतिकीयः, स्वापिशीयः.'
    ),
    '4.3.132': (
        'SETTLED — कौपिञ्जलहास्तिपदादण्, **गोत्रवुञोऽपवादः,\n'
        '  गोत्राधिकारात्** — an exception to the lineage-वुञ्,\n'
        '  and it is one because the lineage-heading is still\n'
        '  running. कौपिञ्जलः, हास्तिपदः.'
    ),
    '4.3.133': (
        'SETTLED — आथर्वणिकस्येकलोपश्च, अणित्येव; **चरणवुञोऽपवादः**. The\n'
        '  अण् and the loss of the इक in one act:\n'
        '  आथर्वणिकस्यायम् **आथर्वणो धर्म आम्नायो वा** — and\n'
        "  the school-vārttika's restriction to a rule of life\n"
        '  or a tradition holds here too.'
    ),
    '4.3.134': (
        'SETTLED — तस्य विकारः. **प्रकृतेरवस्थान्तरं विकारः** — a\n'
        '  modification is the source-material in another\n'
        '  state.\n'
        '\n'
        'SETTLED — AND THE VṚTTI ASKS WHAT IS LEFT FOR THE RULE\n'
        '  TO DO. **किमिहोदाहरणम्?** — and answers by\n'
        '  subtraction: **अप्राण्याद्युदात्तमवृद्धम्, यस्य च\n'
        '  नान्यत् प्रतिपदं विधानम्**, something not animate,\n'
        '  not initially accented, not वृद्ध, and not covered by\n'
        '  a rule of its own. अश्मनो विकार **आश्मनः**, आश्मः;\n'
        '  भास्मनः, मार्त्तिकः.\n'
        '\n'
        'SETTLED — AND तस्य IS SAID AGAIN INSIDE THE SECTION\n'
        '  THAT ALREADY HAD IT. **तस्यप्रकरणे तस्येति पुनर्वचनं\n'
        '  शैषिकनिवृत्त्यर्थम्** — to cancel the शैष heading.\n'
        '  The third time in this pāda a word is repeated to\n'
        "  push another out, after 4.3.53's and 4.3.112's.\n"
        '\n'
        'NOTE — **विकारावयवयोर्घादयो न भवन्ति**: the घ-affixes\n'
        '  do not reach these two senses. हालः, सैरः.'
    ),
    '4.3.135': (
        'SETTLED — अवयवे च प्राण्योषधिवृक्षेभ्यः. From words for LIVING\n'
        '  THINGS, HERBS and TREES in the sense of a PART — and\n'
        '  by the च in the sense of a modification as well.\n'
        '  कपोतस्य विकारोऽवयवो वा **कापोतः**; मायूरः, तैत्तिरः;\n'
        '  मौर्वं काण्डम्; कारीरं भस्म.\n'
        '\n'
        'SETTLED — AND THE SAME FORMULA AS 4.3.66, WORD FOR\n'
        '  WORD. कथं द्वयमप्यधिक्रियते तस्य विकारः, अवयवे च\n'
        '  प्राण्योषधिवृक्षेभ्य इति? **विकारावयवयोर्युगपदधिकारो\n'
        '  ऽपवादविधानार्थः, कृतनिर्देशौ हि तौ** — the two\n'
        '  headings are made to run SIMULTANEOUSLY so that the\n'
        '  exceptions after them can be stated once for both.\n'
        '  4.3.66 said exactly this of भव and व्याख्यान,\n'
        '  sixty-nine sūtras back, in the same words. Twice in\n'
        '  one pāda, and nowhere else in the project so far.\n'
        '\n'
        'NOTE — **इत उत्तरे प्रत्ययाः प्राण्योषधिवृक्षेभ्यो\n'
        '  विकारावयवयोर्भवन्ति, अन्येभ्यस्तु विकारमात्रे**:\n'
        '  from here on the affixes reach both senses for these\n'
        '  three classes and only the modification for anything\n'
        '  else.'
    ),
    '4.3.136': (
        'SETTLED — बिल्वादिभ्योऽण्, **यथायोगमञ्मयटोरपवादः**. बिल्वस्य\n'
        '  विकारोऽवयवो वा **बैल्वः**.\n'
        '\n'
        'NOTE — **गवेधुकाशब्दोऽत्र पठ्यते, ततः कोपधादेव सिद्धे\n'
        '  मयड्बाधनार्थं ग्रहणम्**: गवेधुका is in the list\n'
        "  although the next rule's कोपध would have given it\n"
        '  अण् anyway — it is read here to beat the मयट् of\n'
        '  4.3.143. An entry that adds nothing where it stands\n'
        '  and everything seven sūtras later.'
    ),
    '4.3.137': (
        'SETTLED — कोपधाच्च, अञोऽपवादः. तर्कु — **तार्कवम्**; तित्तिडीक\n'
        '  — तैत्तिडीकम्; माण्डूकम्, दार्दुरूकम्, माधूकम्.\n'
        '\n'
        'NOTE — the PENULTIMATE again, and the same point as at\n'
        '  4.2.132: तर्कु does not END in क, it ends in उ and\n'
        '  has क before it. A condition that would answer for\n'
        '  quite different words if it were read as a final.'
    ),
    '4.3.138': (
        'SETTLED — त्रपुजतुनोः षुक्, **ओरञोऽपवादः**. The अण् with षुक्\n'
        '  added to the base in the same act: त्रपुणो विकारः\n'
        '  **त्रापुषम्**; **जातुषम्** — of tin and of lac.\n'
        '\n'
        'NOTE — **अप्राण्यादित्वाद् नावयवे**: and not in the\n'
        '  sense of a PART, because neither word names a living\n'
        '  thing, a herb or a tree. The condition 4.3.135 set,\n'
        '  doing its work three sūtras later.'
    ),
    '4.3.139': (
        'SETTLED — ओरञ्, अणोऽपवादः. **अनुदात्तादेरन्यदिहोदाहरणम्** — the\n'
        '  example has to be something whose first vowel is NOT\n'
        '  unaccented, since the next rule takes those.\n'
        '  दैवदारवम्, भाद्रदारवम्.'
    ),
    '4.3.140': (
        'SETTLED — अनुदात्तादेश्च, अणोऽपवादः. दाधित्थम्, कापित्थम्,\n'
        '  माहित्थम् — from bases whose FIRST vowel is\n'
        '  unaccented.'
    ),
    '4.3.141': (
        'SETTLED — पलाशादिभ्यो वा. पालाशम्, खादिरम्, यावासम्.\n'
        '\n'
        'SETTLED — ONE OPTION DOING OPPOSITE WORK ON ONE LIST.\n'
        '  **उभयत्र विभाषेयम्** —\n'
        '  **पलाशखदिरशिंशपास्पन्दनानामनुदात्तादित्वात् प्राप्ते,\n'
        '  अन्येषामप्राप्ते**: for four members of the list the\n'
        '  affix was already coming by the last rule, and the\n'
        '  option lets it go; for the rest it was not coming,\n'
        '  and the option brings it. The same word denying and\n'
        '  granting at once, depending which entry it lands on.'
    ),
    '4.3.142': (
        'SETTLED — शम्यष्ट्लञ्, अञोऽपवादः. **शामीलं भस्म**, ash of the\n'
        '  śamī wood; **शामीली स्रुक्**, a ladle of it — and\n'
        '  the ट् is what brings the feminine ending on the\n'
        '  second.'
    ),
    '4.3.143': (
        'SETTLED — मयड्वैतयोर्भाषायामभक्ष्याच्छादनयोः. From ANY base,\n'
        '  optionally, IN THE SPOKEN LANGUAGE, where the thing\n'
        '  is neither food nor clothing. अश्ममयम् beside\n'
        '  आश्मनम्; मूर्वामयम् beside मौर्वम्.\n'
        '\n'
        'NOTE — three conditions and a counter-example each.\n'
        '  भाषायामिति किम्? **बैल्वः खादिरो वा यूपः**\n'
        '  (आपस्तम्बश्रौत १८.१.८), a Vedic sacrificial post.\n'
        '  अभक्ष्याच्छादनयोरिति किम्? **मौद्गः सूपः**, bean\n'
        '  soup, and **कार्पासमाच्छादनम्**, cotton cloth.\n'
        '\n'
        'SETTLED — AND THE TWO SENSES ARE NAMED THOUGH THEY\n'
        '  WERE ALREADY CARRYING. एतयोरित्यनेन किम्, यावता\n'
        '  विकारावयवौ प्रकृतावेव? **ये विशेषप्रत्ययाः\n'
        '  प्राणिरजतादिभ्योऽञ् इत्येवमादयस्तद्विषयेऽपि यथा\n'
        '  स्यात्** — so that the option reaches even where a\n'
        '  special affix has already been given: कपोतमयम्\n'
        '  beside कापोतम्, लोहमयम् beside लौहम्.'
    ),
    '4.3.144': (
        'SETTLED — नित्यं वृद्धशरादिभ्यः, भाषायामभक्ष्याच्छादनयोरित्येव.\n'
        '  From a वृद्ध base and from the शरादि list the मयट्\n'
        '  is FIXED where the last rule made it optional.\n'
        '  आम्रमयम्, शालमयम्, शाकमयम्; शरमयम्, दर्भमयम्,\n'
        '  मृन्मयम्.\n'
        '\n'
        'SETTLED — WHY SAY *ALWAYS*, WHEN STATING THE RULE\n'
        '  WOULD HAVE MADE IT SO? **नित्यग्रहणं किम्, यावता\n'
        '  आरम्भसामर्थ्यादेव नित्यं भविष्यति?** — **एकाचो\n'
        '  नित्यं मयटमिच्छन्ति, तदनेन क्रियते**: because a\n'
        '  ONE-VOWEL base is wanted to take मयट् always as\n'
        '  well, and the word does that. त्वङ्मयम्, स्रङ्मयम्,\n'
        '  **वाङ्मयम्** — and the last is the ordinary word for\n'
        '  literature.'
    ),
    '4.3.145': (
        'SETTLED — गोश्च पुरीषे. **गोमयम्** — cow-dung. पुरीष इति किम्?\n'
        '  **गव्यं पयः**.\n'
        '\n'
        'SETTLED — A RULE REACHING BACK OVER THE HEADING IT\n'
        '  SITS INSIDE. **पुरीषं न विकारो नाप्यवयवः,\n'
        '  तस्येदंविषये विधानम्** — dung is neither a\n'
        '  modification of the cow nor a part of her, so this\n'
        "  rule is stated in 4.3.120's sense and not in the two\n"
        '  that have been running over it. **विकारावयवयोस्तु\n'
        '  गोपयसोर्यतं वक्ष्यति**: for those two, 4.3.160 will\n'
        '  give यत् instead.'
    ),
    '4.3.146': (
        'SETTLED — पिष्टाच्च, अणोऽपवादः. **पिष्टमयं भस्म** — and the मयट्\n'
        '  is fixed here where 4.3.143 made it optional.'
    ),
    '4.3.147': (
        'SETTLED — संज्ञायां कन्, मयटोऽपवादः. **पिष्टकः** — a cake, where\n'
        '  the whole word is a NAME and not a description.'
    ),
    '4.3.148': (
        'SETTLED — व्रीहेः पुरोडाशे, बिल्वाद्यणोऽपवादः. **व्रीहिमयः\n'
        '  पुरोडाशः**, the sacrificial cake of rice;\n'
        '  **व्रैहमन्यत्**, and anything else takes the अण् of\n'
        '  4.3.136, since व्रीहि is in that list.'
    ),
    '4.3.149': (
        'SETTLED — असंज्ञायां तिलयवाभ्याम्. तिलमयम्, यवमयम्.\n'
        '\n'
        'NOTE — असंज्ञायामिति किम्? **तैलम्**, sesame OIL, and\n'
        '  **यावकः** by 5.4.29 यावादिभ्यः कन् — both of them\n'
        '  names, and so outside a rule stated for what is not\n'
        '  a name. The condition of 4.3.147 read the other way\n'
        '  round, two sūtras later.'
    ),
    '4.3.150': (
        'SETTLED — द्व्यचश्छन्दसि. **भाषायां मयडुक्तः, छन्दस्यप्राप्तो\n'
        '  विधीयते** — 4.3.143 gave the मयट् for the spoken\n'
        '  language, where it could not reach the Veda; this\n'
        '  rule supplies what was therefore unavailable there.\n'
        '\n'
        'NOTE — three quotations, one from each of three\n'
        '  recensions. **यस्य पर्णमयी जुहूर्भवति**\n'
        '  (तैत्तिरीयसंहिता ३.५.७.१); **दर्भमयं वासो भवति**\n'
        '  (मैत्रायणीसंहिता १.११.८); **शरमयं बर्हिर्भवति**\n'
        '  (आपस्तम्बश्रौत ९.७.५).'
    ),
    '4.3.151': (
        'SETTLED — नोत्वद्वर्ध्रबिल्वात्. **द्व्यचश्छन्दसि इति प्राप्तः\n'
        '  प्रतिषिध्यते** — what the last rule gave is taken\n'
        '  back for a base containing उ and for two named\n'
        '  words. **मौञ्जं शिक्यम्** (तैत्तिरीयसंहिता\n'
        '  ५.१.१०.५); **वार्ध्री बालप्रग्रथिता भवति**\n'
        '  (आपस्तम्बश्रौत १८.१०.२३).\n'
        '\n'
        'NOTE — **तपरकरणं तत्कालार्थम्**: the त appended to the\n'
        '  उ confines it to that quantity, so धूममयान्यभ्राणि\n'
        '  stands, its ऊ being long. And\n'
        '  **मतुब्निर्देशस्तदन्तविधिनिरासार्थः** — the rule\n'
        '  says *having* उ rather than *ending in* it, so\n'
        '  1.1.72 does not extend it and वैणवी यष्टिः stays\n'
        '  out.'
    ),
    '4.3.152': (
        'SETTLED — तालादिभ्योऽण्, **मयडादीनामपवादः**. **तालं धनुः**, a\n'
        '  bow of palm-wood — and a गणसूत्र **तालाद् धनुषि**\n'
        '  confines that first entry to a bow. बार्हिणम्,\n'
        '  ऐन्द्रालिशम्.'
    ),
    '4.3.153': (
        'SETTLED — जातरूपेभ्यः परिमाणे, मयडादीनामपवादः. **जातरूपं\n'
        '  सुवर्णम्** — gold; and **बहुवचननिर्देशात्\n'
        '  तद्वाचिनः सर्वे गृह्यन्ते**, the plural in the rule\n'
        '  takes in every word for it. हाटको निष्कः, हाटकं\n'
        '  कार्षापणम्; जातरूपम्, तापनीयम्.\n'
        '\n'
        'NOTE — परिमाण इति किम्? **यष्टिरियं हाटकमयी**: a\n'
        '  golden STAFF is no measure, and takes the मयट् back.'
    ),
    '4.3.154': (
        'SETTLED — प्राणिरजतादिभ्योऽञ्, अणादीनामपवादः. कापोतम्, मायूरम्,\n'
        '  तैत्तिरम्; राजतम्, सैसम्, **लौहम्** — and this is\n'
        '  the affix 4.3.135 promised when it named living\n'
        '  things.\n'
        '\n'
        'NOTE — **रजतादिषु येऽनुदात्तादयः पठ्यन्ते\n'
        '  रजतकण्टकारप्रभृतयः, तेभ्योऽञि सिद्धे पुनर्वचनं\n'
        '  मयड्बाधनार्थम्**: several members of the list have\n'
        '  an unaccented first vowel and so had the अञ् from\n'
        '  4.3.140 already — they are read again here to beat\n'
        "  the मयट्. The same shape as गवेधुका in 4.3.136's\n"
        '  list.'
    ),
    '4.3.155': (
        'SETTLED — ञितश्च तत्प्रत्ययात्, अञित्येव; मयटोऽपवादः. **ञिद् यो\n'
        '  विकारावयवप्रत्ययः, तदन्तात् प्रातिपदिकादञ्** — from\n'
        '  a base ending in a ञित् affix given in these two\n'
        '  senses, the अञ् again. दैवदारवस्य विकारो\n'
        '  दैवदारवम्; पालाशस्य पालाशम्; कापोतस्य कापोतम्;\n'
        '  कांस्यस्य कांस्यम्.\n'
        '\n'
        'SETTLED — AND THE VṚTTI LISTS THE RULES ITS CONDITION\n'
        '  POINTS AT, BY NUMBER. ओरञ् [4.3.139], शम्याष्ट्लञ्\n'
        '  [4.3.142], प्राणिरजतादिभ्योऽञ् [4.3.154], उष्ट्राद्\n'
        '  वुञ् [4.3.157], एण्या ढञ् [4.3.159],\n'
        '  कंसीयपरशव्ययोर्यञञौ [4.3.168] — six rules, and every\n'
        '  one of them gives an affix marked with ञ्. A\n'
        '  condition stated abstractly and then enumerated, so\n'
        '  that the claim can be checked instead of trusted.\n'
        '\n'
        'NOTE — ञित इति किम्? **बैल्वमयम्**. तत्प्रत्ययादिति\n'
        '  किम्? **बैदमयम्**, where the ञित् affix was given in\n'
        '  some OTHER sense.'
    ),
    '4.3.156': (
        'SETTLED — क्रीतवत् परिमाणात्, अणादीनामपवादः. **प्राग्वतेष्ठञ्\n'
        '  इत्यत आरभ्य क्रीतार्थे ये प्रत्ययाः परिमाणाद्\n'
        '  विहिताः, ते विकारेऽतिदिश्यन्ते** — the affixes given\n'
        '  from a measure in the sense *bought for* are\n'
        '  borrowed into the sense *a modification of*. निष्केण\n'
        '  क्रीतं नैष्किकम्, and so निष्कस्य विकारो\n'
        '  **नैष्किकः**; शत्यः, शतिकः, साहस्रः.\n'
        '\n'
        'SETTLED — AND THE वति TAKES IN EVERYTHING. **वतिः\n'
        '  सर्वसादृश्यार्थः** — the same words 4.2.34 used of\n'
        "  its own अतिदेश, so even 5.1.28's elision is borrowed\n"
        '  along with the affixes: द्विसहस्रः, द्विसाहस्रः;\n'
        '  द्विनिष्कः, द्विनैष्किकः. The third rule of this\n'
        '  pāda to reach FORWARD, and this one into a quarter\n'
        '  not codified at all, so the row names it and no\n'
        '  more.\n'
        '\n'
        'NOTE — **संख्यापि परिमाणग्रहणेन गृह्यते, न\n'
        '  रूढिपरिमाणमेव**: a NUMBER counts as a measure too,\n'
        '  and not only a measure properly so called.'
    ),
    '4.3.157': (
        'SETTLED — उष्ट्राद् वुञ्, **प्राण्यञोऽपवादः**. उष्ट्रस्य विकारो\n'
        '  ऽवयवो वा **औष्ट्रकः** — and वुञ् is one of the six\n'
        '  ञित् affixes 4.3.155 reaches for.'
    ),
    '4.3.158': (
        'SETTLED — उमोर्णयोर्वा. औमकम् beside औमम्; और्णकम् beside\n'
        '  और्णम् — flax and wool.'
    ),
    '4.3.159': (
        'SETTLED — एण्या ढञ्, प्राण्यञोऽपवादः. **ऐणेयं मांसम्**, the\n'
        '  flesh of the doe. **पुंसस्त्वञेव भवति**: from the\n'
        '  male it is the plain अञ्, एणस्य मांसम् **ऐणम्**.\n'
        '  One affix for the female of a species and another\n'
        '  for the male.'
    ),
    '4.3.160': (
        'SETTLED — गोपयसोर्यत्. **गव्यम्**, पयस्यम् — and this is the\n'
        '  rule 4.3.145 named when it said dung was neither of\n'
        '  these two senses.\n'
        '\n'
        'NOTE — **सर्वत्र गोरजादिप्रसङ्गे यत् अस्त्येव,\n'
        '  मयड्विषये तु विधीयते**: a vārttika on 4.1.85 gives\n'
        '  यत् from गो wherever अज् and the rest would come, so\n'
        '  this rule is stated for the ground the मयट् would\n'
        '  otherwise have had.'
    ),
    '4.3.161': (
        'SETTLED — द्रोश्च, ओरञोऽपवादः. **द्रव्यम्** — a thing, and the\n'
        '  word for MATTER in the philosophies is made by\n'
        '  asking what wood is turned into.'
    ),
    '4.3.162': (
        'SETTLED — माने वयः, यतोऽपवादः. **द्रुवयम्** — a wooden measure.\n'
        '  माने is a particular kind of modification, so the\n'
        '  condition is on what the result IS.'
    ),
    '4.3.163': (
        'SETTLED — फले लुक्. **विकारावयवयोरुत्पन्नस्य फले तद्विशेषे\n'
        '  विवक्षिते लुग् भवति** — where the FRUIT is what is\n'
        '  meant, the affix given in these two senses goes.\n'
        '  आमलक्याः फलम् **आमलकम्**; कुवलम्, बदरम्.\n'
        '\n'
        'SETTLED — AND WHY ONE RULE CAN BE STATED OF BOTH\n'
        '  SENSES AT ONCE. **फलितस्य वृक्षस्य फलमवयवो भवति\n'
        '  विकारश्च, पल्लवितस्येव पल्लवः** — a fruit is both a\n'
        '  PART of the tree that bore it and a MODIFICATION of\n'
        '  it, as a shoot is of what has shot. The two headings\n'
        '  4.3.135 made to overlap, and here is a thing that\n'
        '  falls under both at once.'
    ),
    '4.3.164': (
        'SETTLED — प्लक्षादिभ्योऽण्, फल इत्येव; अञोऽपवादः.\n'
        '  **विधानसामर्थ्यात् तस्य न लुग् भवति** — the last\n'
        "  rule's elision does not touch it, because a rule\n"
        '  stated for a ground would achieve nothing if what it\n'
        '  gave were removed at once. प्लाक्षम्, नैयग्रोधम्.'
    ),
    '4.3.165': (
        'SETTLED — जम्ब्वा वा, फल इत्येव; अञोऽपवादः. **अत्राणो\n'
        '  विधानसामर्थ्याल् लुग् न भवति, अञस्तु भवत्येव** — the\n'
        "  अण् this rule gives escapes 4.3.163's elision by the\n"
        '  same argument, and the अञ् that comes on the other\n'
        '  side of the option does not. **जाम्बवानि फलानि**\n'
        '  beside **जम्बूनि**.'
    ),
    '4.3.166': (
        'SETTLED — लुप् च, वेत्येव. जम्ब्वाः फलं **जम्बूः फलम्**, जम्बु\n'
        '  फलम्, जाम्बवमिति वा.\n'
        '\n'
        'SETTLED — AND लुप् IS NOT लुक्. **युक्तवद्भावे\n'
        '  विशेषः** — under लुप् what is left agrees by 1.2.51\n'
        '  with the word the affix stood on, and the feminine\n'
        '  ending is heard; under लुक् it is not. Two ways of\n'
        '  taking an affix away that leave different words, and\n'
        '  this pāda uses both.\n'
        '\n'
        'NOTE — a vārttika adds the grains: **लुप्प्रकरणे\n'
        '  फलपाकशुषामुपसंख्यानम्** — व्रीहयः, यवाः, माषाः,\n'
        '  मुद्गाः, तिलाः, the plants that wither when their\n'
        '  fruit ripens. And **पुष्पमूलेषु बहुलम्**: variously\n'
        '  of flowers and roots — मल्लिकायाः पुष्पं मल्लिका,\n'
        '  बिदार्या मूलं बिदारी; न च भवति पाटलानि पुष्पाणि.'
    ),
    '4.3.167': (
        'SETTLED — हरीतक्यादिभ्यश्च, फले. हरीतक्याः फलं **हरीतकी**;\n'
        '  कोशातकी, नखरजनी.\n'
        '\n'
        'SETTLED — AND HERE THE DIFFERENCE BETWEEN THE TWO\n'
        '  REMOVALS IS SPELT OUT. लुकि प्राप्ते लुपो विधाने\n'
        '  **युक्तवद्भावे स्त्रीप्रत्ययश्रवणे च विशेषः** —\n'
        "  4.3.163's लुक् was already available here, and लुप्\n"
        '  is enjoined instead because the two differ in\n'
        "  1.2.51's agreement and in whether the feminine affix\n"
        '  is still heard. The clearest statement of that\n'
        '  distinction the project has met.\n'
        '\n'
        'SETTLED — AND GENDER AND NUMBER PART COMPANY.\n'
        '  **अत्र च व्यक्तिर्युक्तवद्भावेनेष्यते, वचनं\n'
        '  त्वभिधेयवदेव भवति** — the GENDER follows the word\n'
        '  the affix stood on and the NUMBER follows what is\n'
        '  denoted: हरीतक्याः फलानि **हरीतक्यः**, feminine\n'
        '  because the tree is, plural because the fruits are.'
    ),
    '4.3.168': (
        'SETTLED — कंसीयपरशव्ययोर्यञञौ लुक् च, यथासंख्यम्. The two bases\n'
        '  are themselves derived — कंसीयः by 5.1.1\n'
        '  प्राक्क्रीताच्छः and परशव्यः by 5.1.2 उगवादिभ्यो\n'
        '  यत् — and the affix that made each is removed in the\n'
        '  same act that gives the new one. कंसीयस्य विकारः\n'
        '  **कांस्यः**; परशव्यस्य **पारशवः**.\n'
        '\n'
        'NOTE — **प्रातिपदिकाधिकाराद् धातुप्रत्ययस्य न लुग्\n'
        '  भवति**: the removal reaches a nominal affix only,\n'
        '  since the heading is about प्रातिपदिक. And\n'
        '  **परशव्यशब्दादनुदात्तादित्वादेवाञि सिद्धे लुगर्थं\n'
        '  वचनम्** — the अञ् was already coming to परशव्य by\n'
        "  4.3.140, so the rule is spoken for the elision's\n"
        '  sake.\n'
        '\n'
        'SETTLED — AND AN ALTERNATIVE DERIVATION REFUSED IN ONE\n'
        '  LINE. ननु च यस्येति [6.4.148] इति लोपे कृते\n'
        '  **हलस्तद्धितस्य** [6.4.150] इति यलोपो भविष्यति? —\n'
        '  could the य not simply drop by a general rule?\n'
        '  **नैतदस्ति; ईतीति तत्र वर्तते**: that rule carries\n'
        '  ईति from its own neighbourhood and so drops य only\n'
        '  before ई. A whole derivation set aside by naming one\n'
        '  word that is still in force where it stands.\n'
        '\n'
        '  The pāda ends here: **इति श्रीजयादित्यविरचितायां\n'
        '  काशिकायां वृत्तौ चतुर्थाध्यायस्य तृतीयः पादः**.'
    ),
}

_BORN_IN_LINE = (
    'born_in(stem, gana=..., sense=..., case=..., result=..., '
    'samjna=..., pre=..., stem_final=..., chandasi=..., before=..., '
    'wants=...) -> which affix comes from that base, in that time or '
    'that sense.'
)

#: 4.3.25 names a case and a sense and no affix, because the affixes
#: were all given ahead of it. `born_in` answers it by CALLING
#: `in_sense` and reporting what the शेष rules of 4.2 prescribed —
#: which is what यथाविहितम् means, and the vṛtti's own examples are
#: the outputs of these three rules read off in order.
_REUSES = {
    "4.3.25": ("4.2.93", "4.2.94", "4.2.95", "4.1.83"),
}

for _sutra, _notes in _RULES.items():
    register(
        _sutra,
        apply=born_in,
        codification=_BORN_IN_LINE,
        notes=_notes,
        reuses=_REUSES.get(_sutra, ()),
    )
