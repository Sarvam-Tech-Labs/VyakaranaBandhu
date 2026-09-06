# -*- coding: utf-8 -*-
"""
अध्याय ५, पाद २ — no heading at all, and every rule its own sense.

The pāda before was seven headings deep and the question at each rule
was which affix displaced which. This one opens with none: each rule
names its own affix and its own sense, and the senses do not run in
families. A field where grain grows, a cloth reaching the toes, a cow
that calves every year, butter churned from yesterday's milking.

So the commentary changes its work. Where 5.1 argued about ranges,
5.2 glosses — भवन्ति जायन्तेऽस्मिन्निति भवनम्, गावस्तिष्ठन्त्यस्मिन्निति
गोष्ठम्, गोः पश्चाद् अनुगु — and five of the first twenty-eight rules
lay a whole form down rather than deriving it, with the vṛtti saying
each time that the analysis is a courtesy: यथाकथंचिद् व्युत्पादयितव्यौ.
"""

from __future__ import annotations

from src.astadhyayi.matup import what_comes
from src.astadhyayi.sources import register

_RULES = {
    '5.2.1': (
        'SETTLED — धान्यानां भवने क्षेत्रे खञ्. **निर्देशादेव समर्थविभक्तिः**\n'
        '  — the case is got from the wording. **भवन्ति जायन्तेऽस्मिन्निति\n'
        '  भवनम्**: a भवन is where things come to be. मुद्गानां भवनं क्षेत्रं\n'
        '  **मौद्गीनम्**; कौद्रवीणम्, कौलत्थीनम्.\n'
        '\n'
        'SETTLED — **धान्यानामिति किम्?** तृणानां भवनं क्षेत्रम् — grass is\n'
        '  not grain. **क्षेत्रमिति किम्?** मुद्गानां भवनं **कुसूलम्**, a\n'
        '  granary, which is a growing-place of a sort and not a FIELD.\n'
        '  **बहुवचनं स्वरूपविधिनिरासार्थम्** — and the plural stops the rule\n'
        '  applying to the word धान्य itself'
    ),
    '5.2.2': (
        'SETTLED — व्रीहिशाल्योर्ढक्, खञोऽपवादः. व्रीहीणां भवनं क्षेत्रं\n'
        '  **व्रैहेयम्**; शालेयम्'
    ),
    '5.2.3': (
        'SETTLED — यवयवकषष्टिकाद् यत्, खञोऽपवादः. यवानां भवनं क्षेत्रं\n'
        '  **यव्यम्**; यवक्यम्, षष्टिक्यम्'
    ),
    '5.2.4': (
        'SETTLED — विभाषा तिलमाषोमाभङ्गाणुभ्यः. **खञि प्राप्ते वचनम्, पक्षे\n'
        '  सोऽपि भवति** — the खञ् was coming and this makes the यत् an\n'
        '  alternative to it, so both stand: **तिल्यम्, तैलीनम्**; माष्यम्,\n'
        '  माषीणम्; उम्यम्, औमीनम्; भङ्ग्यम्, भाङ्गीनम्; अणव्यम्, आणवीनम्.\n'
        '\n'
        'SETTLED — **उमाभङ्गयोरपि धान्यत्वमाश्रितमेव** — and flax and hemp\n'
        '  are treated as grain here, though they are not eaten, or 5.2.1\n'
        '  could not have reached them at all'
    ),
    '5.2.5': (
        'SETTLED — सर्वचर्मणः कृतः खखञौ. **सर्वचर्मीणः, सार्वचर्मीणः**.\n'
        '\n'
        'SETTLED — **AND THE COMPOUND IN THE RULE IS ONE THAT SHOULD NOT\n'
        '  EXIST.** **सर्वशब्दश्चात्र प्रत्ययार्थेन कृतेन संबध्यते, न\n'
        '  चर्मणा** — the *all* goes with the MAKING, which is what the affix\n'
        '  reports, and not with the leather. So सर्व and चर्मन् have no\n'
        '  relation to each other and yet stand compounded: **तत्रायम्\n'
        '  असमर्थसमासो द्रष्टव्यः**, an असमर्थसमास, **सर्वश्चर्मणा कृत\n'
        '  इत्येतस्मिन् वाक्यार्थे वृत्तिः** — the compound holds the sense\n'
        '  of the whole sentence and not of its own two parts'
    ),
    '5.2.6': (
        'SETTLED — यथामुखसंमुखस्य दर्शनः खः. **दृश्यतेऽस्मिन्निति दर्शनः,\n'
        '  आदर्शादिः प्रतिबिम्बाश्रय उच्यते** — a दर्शन is what one is seen\n'
        '  IN, a mirror or anything that holds a reflection. यथामुखं दर्शनो\n'
        '  **यथामुखीनः**; सर्वस्य मुखस्य दर्शनः **सम्मुखीनः**.\n'
        '\n'
        'SETTLED — **निपातनात् सादृश्येऽव्ययीभावः** — and the अव्ययीभाव in\n'
        "  the sense of LIKENESS is got from the laying-down, since 2.1.6's\n"
        '  यथा compounds are for conformity and not resemblance'
    ),
    '5.2.7': (
        'SETTLED — तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति. **तदिति\n'
        '  द्वितीया समर्थविभक्तिः; व्याप्नोतीति प्रत्ययार्थः; परिशिष्टं\n'
        '  प्रकृतिविशेषणम्** — the first word gives the case, the verb gives\n'
        '  the sense, and everything left over describes the base. So: from a\n'
        '  compound beginning with सर्व and ending in one of five words.\n'
        '\n'
        'SETTLED — सर्वपथं व्याप्नोति **सर्वपथीनो रथः**, a chariot that\n'
        '  covers the whole road; **सर्वाङ्गीणस्तापः**, a fever through every\n'
        '  limb; सर्वकर्मीणः पुरुषः; सर्वपत्रीणः सारथिः; **सर्वपात्रीण\n'
        '  ओदनः**, rice enough to fill every dish'
    ),
    '5.2.8': (
        'SETTLED — आप्रपदं प्राप्नोति. **प्रपदमिति पादस्याग्रम् उच्यते; आङ्\n'
        '  मर्यादायाम्; तयोरव्ययीभावः** — प्रपद is the front of the foot and\n'
        '  आ marks the limit, and the two make an अव्ययीभाव. आप्रपदं\n'
        '  प्राप्नोति **आप्रपदीनः पटः**, a cloth reaching the toes.\n'
        '\n'
        'SETTLED — **शरीरेणासंबद्धस्यापि पटस्य प्रमाणमाख्यायते** — and it\n'
        "  states the cloth's MEASURE even when the cloth is not on a body at\n"
        '  all'
    ),
    '5.2.9': (
        'SETTLED — अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु, **यथासंख्यम्**;\n'
        '  the अनुपद member. **अनुरायामे सादृश्ये वा** — अनु of length or of\n'
        '  likeness. अनुपदं बद्धा उपानत् **अनुपदीना**, a sandal bound to the\n'
        "  foot, **पदप्रमाणा इत्यर्थः**, of the foot's measure\n"
        '\n'
        'SETTLED — अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु, the सर्वान्न\n'
        '  member. सर्वान्नानि भक्षयति **सर्वान्नीनो भिक्षुः**, a beggar who\n'
        '  eats any food at all\n'
        '\n'
        'SETTLED — अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु, the अयानय member —\n'
        '  and the word is from the board-game. **अयः प्रदक्षिणम्, अनयः\n'
        '  प्रसव्यम्; प्रदक्षिणप्रसव्यगामिनां शाराणां यस्मिन् परशारैः पदानाम्\n'
        '  असमावेशः सोऽयानयः**: अय is the rightward course and अनय the\n'
        "  leftward, and the square where the opponent's pieces cannot come\n"
        '  is the अयानय. अयानयं नेयः **अयानयीनः शारः**, **फलकशिरसि स्थित\n'
        '  इत्यर्थः**, a piece standing at the head of the board'
    ),
    '5.2.10': (
        'SETTLED — परोवरपरम्परपुत्रपौत्रमनुभवति; the परोवर member, and the\n'
        '  substitution comes with the affix. **परस्योत्वं प्रत्ययसंनियोगेन\n'
        '  निपात्यते** — the उ of परस् is laid down as yoked to the affix.\n'
        '  परांश्चावरांश्चानुभवति **परोवरीणः**, one who lives through high\n'
        '  and low alike\n'
        '\n'
        'SETTLED — परोवरपरम्परपुत्रपौत्रमनुभवति, the परम्पर member.\n'
        '  **परपरतराणां च परम्परभावो निपात्यते** — the shape परम्पर is laid\n'
        '  down for परपरतर. परांश्च परतरांश्चानुभवति **परम्परीणः**.\n'
        '\n'
        'SETTLED — **परम्परशब्दो विनापि प्रत्ययेन दृश्यते** — and the word is\n'
        '  seen without any affix, मन्त्रिपरम्परा मन्त्रं भिनत्ति, *a chain\n'
        '  of ministers breaks a secret*. **तच्छब्दान्तरमेव द्रष्टव्यम्**:\n'
        '  that is simply a different word\n'
        '\n'
        'SETTLED — परोवरपरम्परपुत्रपौत्रमनुभवति, the पुत्रपौत्र member — and\n'
        '  the only one of the three that needs no laying-down.\n'
        '  पुत्रपौत्राननुभवति **पुत्रपौत्रीणः**'
    ),
    '5.2.11': (
        'SETTLED — अवारपारात्यन्तानुकामं गामी. **गमिष्यतीति गामी**, 3.3.3\n'
        '  भविष्यति गम्यादयः — the participle is future, and 2.3.70\n'
        '  अकेनोर्भविष्यदाधमर्ण्ययोः forbids the genitive with it, which is\n'
        '  why the base stands in the accusative.\n'
        '\n'
        'SETTLED — अवारपारं गामी **अवारपारीणः**, one who will cross from this\n'
        '  bank to the far one. **विगृहीतादपीष्यते** — and from the members\n'
        '  separately too: अवारीणः, पारीणः; **विपरीताच्च**, and reversed:\n'
        '  पारावारीणः. अत्यन्तं गामी **अत्यन्तीनः**, **भृशं गन्ता**; अनुकामं\n'
        '  गामी **अनुकामीनः**, **यथेष्टं गन्ता**'
    ),
    '5.2.12': (
        'SETTLED — समांसमां विजायते. **समांसमामिति वीप्सा**, a distributive\n'
        '  doubling, and **सुबन्तसमुदायः प्रकृतिः** — the base is a bundle of\n'
        '  inflected words. **गर्भधारणेन सकलापि समा व्याप्यत इति\n'
        '  अत्यन्तसंयोगे द्वितीया** (2.1.29): the whole year is occupied by\n'
        '  the carrying, so the accusative of unbroken connection. समांसमां\n'
        '  विजायते **समांसमीना गौः**, a cow that calves every year.\n'
        '\n'
        'SETTLED — **पूर्वपदे सुपोऽलुग् वक्तव्यः** — the case-ending of the\n'
        '  first member is not dropped. And a second reading: **केचित् तु\n'
        '  समायांसमायां विजायत इति विगृह्णन्ति, गर्भविमोचने तु विजनिर्वर्तत\n'
        '  इत्याहुः** — some read a locative and take विजनि of the delivery\n'
        '  rather than the carrying'
    ),
    '5.2.13': (
        'SETTLED — अद्यश्वीनावष्टब्धे. **अद्यश्वीन इति निपात्यते** — a form\n'
        '  laid down, and laid down for something imminent. **आसन्ने\n'
        '  प्रसवे**: अद्य वा श्वो वा विजायते **अद्यश्वीना गौः**, a cow that\n'
        '  will calve today or tomorrow.\n'
        '\n'
        'SETTLED — **आविदूर्ये हि मूर्धन्यो विधीयते** — 8.3.68\n'
        '  अवाच्चालम्बनाविदूर्ययोः gives the cerebral only in the sense of\n'
        '  nearness, so the ष of अवष्टब्ध is itself evidence of what the rule\n'
        '  means.\n'
        '\n'
        'SETTLED — **केचित् तु विजायत इति नानुवर्तयन्ति, अवष्टब्धमात्रे\n'
        '  निपातनमित्याहुः** — and some do not carry the calving down, taking\n'
        '  the form for anything imminent at all: **अद्यश्वीनं मरणम्**, a\n'
        '  death expected today or tomorrow'
    ),
    '5.2.14': (
        'SETTLED — आगवीनः — a laid-down form, and the whole of a contract in\n'
        '  one word. **गोराङ्पूर्वाद् आ तस्य गोः प्रतिदानात् कर्मकारिणि खः\n'
        '  प्रत्ययो निपात्यते**: **आगवीनः कर्मकरः**, **यो गवा भृतः कर्म करोति\n'
        '  आ तस्य गोः प्रत्यर्पणात्** — a hired man who works for a cow,\n'
        '  UNTIL THE COW IS HANDED OVER. The आ of the compound is the term of\n'
        '  the hire'
    ),
    '5.2.15': (
        'SETTLED — अनुग्वलंगामी. **गोः पश्चाद् अनुगु** — अनुगु is *behind the\n'
        '  cattle*. अनुगु पर्याप्तं गच्छति **अनुगवीनो गोपालकः**, a herdsman\n'
        '  equal to following them'
    ),
    '5.2.16': (
        'SETTLED — अध्वनो यत्खौ. अध्वानमलंगामी **अध्वन्यः, अध्वनीनः** — one\n'
        '  equal to the road. 6.4.168 ये चाभावकर्मणोः and 6.4.169 आत्माध्वानौ\n'
        '  खे keep the stem unchanged before each of the two'
    ),
    '5.2.17': (
        'SETTLED — अभ्यमित्राच्छ च — and the च keeps both affixes of the rule\n'
        '  before, so three stand: अभ्यमित्रमलंगामी **अभ्यमित्रीयः,\n'
        '  अभ्यमित्र्यः, अभ्यमित्रीणः**, **अमित्राभिमुखं सुष्ठु\n'
        '  गच्छतीत्यर्थः** — one who goes well against the enemy'
    ),
    '5.2.18': (
        'SETTLED — गोष्ठात् खञ् भूतपूर्वे — and the affix changes nothing but\n'
        '  the shape. **गावस्तिष्ठन्त्यस्मिन्निति गोष्ठम्**; **गोष्ठशब्देन\n'
        '  सन्निहितगोसमूहो देश उच्यते**, the word means the place with the\n'
        '  cattle standing in it. **भूतपूर्वग्रहणं तस्यैव विशेषणम्**: and\n'
        '  *formerly* qualifies THAT — गोष्ठो भूतपूर्वो **गौष्ठीनो देशः**, a\n'
        '  place that used to be a cow-pen. **भूतपूर्वग्रहणं किम्?** गोष्ठो\n'
        '  वर्तते'
    ),
    '5.2.19': (
        'SETTLED — अश्वस्यैकाहगमः. **निर्देशादेव समर्थविभक्तिः**, and\n'
        '  **एकाहेन गम्यत इत्येकाहगमः**. अश्वस्यैकाहगमोऽध्वा **आश्वीनः** — a\n'
        "  day's ride, measured as a distance. **आश्वीनानि** शतं पतित्वा\n"
        '  (तां०ब्रा० २१.१.९)'
    ),
    '5.2.20': (
        'SETTLED — शालीनकौपीने अधृष्टाकार्ययोः, **यथासंख्यम्**; the शालीन\n'
        '  member. **अधृष्टोऽप्रगल्भः** — bashful. **शालाप्रवेशनमर्हति इति\n'
        '  खञ् प्रत्यय उत्तरपदलोपश्च निपात्यते**: *one who deserves to go\n'
        "  indoors*, with the affix and the loss of the compound's second\n"
        '  member both laid down. **शालीनो जडः**.\n'
        '\n'
        'SETTLED — **शालीनकौपीने अधृष्टाकार्ययोः पर्यायौ यथाकथंचिद्\n'
        '  व्युत्पादयितव्यौ** — the two are simply synonyms of *bashful* and\n'
        '  *not to be done*, and are to be derived somehow or other. The\n'
        "  vṛtti's own warning against reading the analysis too hard\n"
        '\n'
        'SETTLED — शालीनकौपीने अधृष्टाकार्ययोः, the कौपीन member. **अकार्यम्\n'
        '  अकरणार्हं विरुद्धम्** — what ought not to be done. कूपावतारमर्हति,\n'
        '  *deserving to be thrown down a well*: **कौपीनं पापम्**'
    ),
    '5.2.21': (
        'SETTLED — व्रातेन जीवति. **निर्देशादेव तृतीया समर्थविभक्तिः**, and\n'
        '  the vṛtti has to say what a व्रात is: **नानाजातीया अनियतवृत्तय\n'
        '  उत्सेधजीविनः संघा व्राताः** — troops of mixed birth and no settled\n'
        '  livelihood who live by their bodies, **उत्सेधः शरीरम्, तदायास्य ये\n'
        '  जीवन्ति**. तेन व्रातेन जीवति **व्रातीनः**.\n'
        '\n'
        'SETTLED — **तेषामेव व्रातानाम् अन्यतम उच्यते; यस्त्वन्यस् तदीयेन\n'
        '  जीवति, तत्र नेष्यते** — and it means one OF the troop, not an\n'
        '  outsider living off their work'
    ),
    '5.2.22': (
        'SETTLED — साप्तपदीनं सख्यम्. **निपात्यते** — a laid-down form for\n'
        '  FRIENDSHIP. **सप्तभिः पदैरवाप्यते साप्तपदीनम्**, won in seven\n'
        '  steps: **सख्यं जनाः साप्तपदीनम् आहुः**.\n'
        '\n'
        'SETTLED — **कथं साप्तपदीनः सखा?** How then can the word be used of\n'
        '  the FRIEND? **यदा गुणप्रधानः साप्तपदीनशब्दः सखिभावे तत्कर्मणि च\n'
        '  वर्तते, तदा सख्यशब्देन सामानाधिकरण्यं भवति; यदा तु लक्षणया वर्तते,\n'
        '  तदा पुरुषेण** — when it stands for the state it agrees with the\n'
        '  word for friendship, and when it is used figuratively it agrees\n'
        '  with the person'
    ),
    '5.2.23': (
        'SETTLED — हैयङ्गवीनं संज्ञायाम्. **निपात्यते** — laid down, with a\n'
        '  substitution inside it. **ह्योगोदोहस्य हियङ्ग्वादेशः, तस्य विकारे\n'
        "  खञ् प्रत्ययो भवति संज्ञायाम्**: what is made from YESTERDAY'S\n"
        '  MILKING — **ह्योगोदोहस्य विकारो हैयङ्गवीनम्**, and it is **घृतस्य\n'
        '  संज्ञा**, a name for clarified butter. **तेनेह न भवति —\n'
        '  ह्योगोदोहस्य विकार उदश्वित्**, and so not of buttermilk, which is\n'
        '  also made from it'
    ),
    '5.2.24': (
        'SETTLED — तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ,\n'
        '  **यथासंख्यम्**; the पील्वादि half, in the sense of RIPENING.\n'
        '  पीलूनां पाकः **पीलुकुणः**; कर्कन्धुकुणः. पीलु, कर्कन्धु, शमी,\n'
        '  करीर, कुवल, बदर, अश्वत्थ, खदिर — पील्वादिः\n'
        '\n'
        'SETTLED — तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ, the कर्णादि\n'
        '  half, in the sense of the ROOT of a thing. कर्णस्य मूलं\n'
        '  **कर्णजाहम्**. कर्ण, अक्षि, नख, मुख, मख, केश, पाद, गुल्फ,\n'
        '  भ्रूभङ्ग, दन्त, ओष्ठ, पृष्ठ, अङ्गुष्ठ — कर्णादिः'
    ),
    '5.2.25': (
        'SETTLED — पक्षात् तिः. **मूलग्रहणम् अनुवर्तते, न पाकग्रहणम्** — the\n'
        '  ROOT carries down and the ripening does not, though the rule\n'
        '  before stated them in one breath: **एकयोगनिर्दिष्टानाम्\n'
        '  अप्येकदेशोऽनुवर्तते**, even of things named in a single rule a\n'
        '  PART may carry on alone. पक्षस्य मूलं **पक्षतिः प्रतिपत्**'
    ),
    '5.2.26': (
        'SETTLED — तेन वित्तश्चुञ्चुप्चणपौ. **वित्तः प्रतीतो ज्ञातः** —\n'
        '  known, famous BY something. विद्यया वित्तो **विद्याचुञ्चुः,\n'
        '  विद्याचणः**, famous for learning'
    ),
    '5.2.27': (
        'SETTLED — विनञ्भ्यां नानाञौ नसह, **यथासंख्यम्**; the वि member. **न\n'
        '  सहेति प्रकृतिविशेषणम्** — the words must be standing for\n'
        '  SEPARATION and not for togetherness. **विना**\n'
        '\n'
        'SETTLED — विनञ्भ्यां नानाञौ नसह, the नञ् member. **नाना** — and both\n'
        '  affixes are स्वार्थे, changing nothing but the shape of an\n'
        '  indeclinable'
    ),
    '5.2.28': (
        'SETTLED — वेः शालच्छङ्कटचौ. **ससाधनक्रियावचनाद् उपसर्गात् स्वार्थे\n'
        '  प्रत्ययौ भवतः** — from a preverb standing for an action together\n'
        '  with its means. विगते शृङ्गे **विशाले, विशङ्कटे**, of a beast\n'
        '  whose horns are gone, **तद्योगाद् गौरपि विशालो विशङ्कट\n'
        '  इत्युच्यते**, and by association the animal itself.\n'
        '\n'
        'SETTLED — **परमार्थतस्तु गुणशब्दा एते यथाकथंचिद् व्युत्पाद्यन्ते।\n'
        '  नात्र प्रकृतिप्रत्ययार्थयोर् अभिनिवेशः** — but in truth these are\n'
        '  quality-words and are derived somehow or other; there is no\n'
        '  insisting here on a sense for the base and a sense for the affix.\n'
        '  The same warning 5.1.59 gave of the numerals'
    ),
    '5.2.29': (
        'SETTLED — संप्रोदश्च कटच्. **चकाराद् वेश्च** — and the च brings वि\n'
        '  in as a fourth. **संकटम्, प्रकटम्, उत्कटम्, विकटम्**. **AND THIS\n'
        '  ONE SŪTRA CARRIES EIGHT VĀRTTIKAS, EACH GIVING AN AFFIX OF ITS\n'
        '  OWN.** **कटच्प्रकरणेऽलाबूतिलोमाभङ्गाभ्यो रजस्युपसंख्यानम्** — the\n'
        '  same affix for POLLEN: अलाबूकटम्, तिलकटम्. **गोष्ठादयः स्थानादिषु\n'
        '  पशुनामादिभ्यः** — गोगोष्ठम्, महिषीगोष्ठम्. **संघाते कटज्\n'
        '  वक्तव्यः** — a herd, अविकटम्. **विस्तारे पटज्** — a spread,\n'
        '  अविपटम्. **द्वित्वे गोयुगच्** — a pair, उष्ट्रगोयुगम्.\n'
        '  **प्रकृत्यर्थस्य षट्त्वे षड्गवच्** — a set of six,\n'
        '  **हस्तिषड्गवम्**. **विकारे स्नेहे तैलच्** — an oil made from\n'
        '  something, **एरण्डतैलम्**, and by that vārttika तैल is\n'
        '  *sesame-oil* only by usage. **भवने क्षेत्र इक्ष्वादिभ्यः\n'
        "  शाकटशाकिनौ** — इक्षुशाकटम्, and the sense is 5.2.1's over again"
    ),
    '5.2.30': (
        'SETTLED — अवात् कुटारच्च — **चकारात् कटच्**, so both. **अवकुटारम्,\n'
        '  अवकटम्**'
    ),
    '5.2.31': (
        'SETTLED — नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्रटचः — three affixes\n'
        '  for one preverb, and the sense is a FLAT NOSE. **नमनं नतम्**.\n'
        '  नासिकाया नतम् **अवटीटम्, अवनाटम्, अवभ्रटम्**. **तद्योगाद्\n'
        '  नासिकापि, पुरुषोऽपि तथोच्यते** — and by association the nose is\n'
        '  called that, and so is the man: **अवटीटः, अवनाटः, अवभ्रटः**'
    ),
    '5.2.32': (
        'SETTLED — नेर्बिडज्बिरीसचौ. **नते नासिकाया इत्यनुवर्तते,\n'
        '  संज्ञायामिति च**. **निबिडम्, निबिरीसम्**, and by association\n'
        '  निबिडः, निबिरीसः. **कथं निबिडाः केशाः, निबिडं वस्त्रम्?** How then\n'
        '  is hair called निबिड, or cloth? **उपमानाद् भविष्यति** — by\n'
        '  comparison, and not by this rule'
    ),
    '5.2.33': (
        'SETTLED — इनच्पिटच्चिकचि च — and the affixes come with substitutions\n'
        '  matched to them. **तत्संनियोगेन च निशब्दस्य यथासंख्यं चिक चि\n'
        '  इत्येतावादेशौ भवतः**: **चिकिनः, चिपिटः**. **ककारः प्रत्ययो\n'
        '  वक्तव्यश्चिक् च प्रकृत्यादेशः** — a vārttika adds a third, क with\n'
        '  चिक्: **चिक्कः**, and the Mahābhāṣya states the whole set:\n'
        '  **इनच्पिटच्काश्चिकचिचिकादेशाश्च**. **क्लिन्नस्य चिल्पिल्लश्चास्य\n'
        '  चक्षुषी** — and a further vārttika for RUNNING EYES: क्लिन्ने अस्य\n'
        '  चक्षुषी **चिल्लः, पिल्लः**, and **चुलादेशो वक्तव्यः**, चुल्लः. And\n'
        '  a correction: **अस्येत्यनेन नार्थः; चक्षुषोरेवाभिधाने प्रत्यय\n'
        '  इष्यते** — the *of him* is not wanted, the affix being for naming\n'
        '  the EYES themselves: क्लिन्ने चक्षुषी **चिल्ले**; **तद्योगात् तु\n'
        '  पुरुषस् तथोच्यते**'
    ),
    '5.2.34': (
        'SETTLED — उपाधिभ्यां त्यकन्नासन्नारूढयोः, **यथासंख्यम्**; the उप\n'
        "  member. पर्वतस्यासन्नम् **उपत्यका**, the land at a mountain's\n"
        '  foot. **संज्ञाधिकाराच्च नियतविषयमासन्नारूढं गम्यते** — the\n'
        '  naming-heading makes the *near* and the *risen* definite things\n'
        '  and not any nearness at all. And it does one more job:\n'
        '  **प्रत्ययस्थात् कात् पूर्वस्य इति इत्वमत्र न भवति,\n'
        '  संज्ञाधिकारादेव** (7.3.44), the आ before the क is not shortened,\n'
        '  and it is the naming-heading that stops it\n'
        '\n'
        'SETTLED — उपाधिभ्यां त्यकन्नासन्नारूढयोः, the अधि member.\n'
        '  पर्वतस्यैवारूढम् **अधित्यका**, the tableland above'
    ),
    '5.2.35': (
        'SETTLED — कर्मणि घटोऽठच्. **निर्देशादेव समर्थविभक्तिः**, and **घटत\n'
        '  इति घटः** — one who exerts himself. कर्मणि घटते **कर्मठः पुरुषः**,\n'
        '  a man who throws himself into the work'
    ),
    '5.2.36': (
        'SETTLED — तदस्य संजातं तारकादिभ्य इतच्. **संजातग्रहणं\n'
        '  प्रकृतिविशेषणम्** — *come to be* describes the BASE. तारकाः संजाता\n'
        '  अस्य नभसः **तारकितं नभः**, a sky that has come to have stars;\n'
        '  **पुष्पितो वृक्षः**, a tree come into flower. तारका, पुष्प, मुकुल,\n'
        '  कण्टक, पिपासा, सुख, दुःख, ऋजीष, कुड्मल, रोग, विचार, व्याधि,\n'
        '  निष्क्रमण, किसलय, कुसुम, तन्द्रा, वेग, श्रद्धा, उत्कण्ठा,\n'
        '  **गर्भादप्राणिनि** (ग०सू०१२३) — **तारकादिराकृतिगणः**, an open list'
    ),
    '5.2.37': (
        'SETTLED — प्रमाणे द्वयसज्दघ्नञ्मात्रचः — three affixes for the\n'
        '  MEASURE of a thing. ऊरुः प्रमाणमस्य **ऊरुद्वयसम्, ऊरुदघ्नम्,\n'
        '  ऊरुमात्रम्**; जानुद्वयसम्, जानुदघ्नम्, जानुमात्रम्. **AND A KĀRIKĀ\n'
        '  DIVIDES THEM.** प्रथमश्च द्वितीयश्च ऊर्ध्वमाने मतौ मम । The first\n'
        '  two are for HEIGHT — ऊरुद्वयसमुदकम्, water thigh-deep — and\n'
        '  **मात्रच् पुनरविशेषेण प्रस्थमात्रमित्यपि भवति**, the third for\n'
        '  measure of any kind. **प्रमाणे लो वक्तव्यः** — after a word that\n'
        '  is ITSELF a measure-word the affix drops: शमः प्रमाणमस्य **शमः**;\n'
        '  दिष्टिः, वितस्तिः. **द्विगोर्नित्यम्**, and after a numeral\n'
        '  compound always: **द्विशमः**. **नित्यग्रहणं किम्?** so that the\n'
        '  elision holds even where a doubt-affix would come: द्वे दिष्टी\n'
        '  स्यातां वा न वा **द्विदिष्टिः**. **डट् स्तोमे**: पञ्चदशः स्तोमः.\n'
        '  **प्रमाणपरिमाणाभ्यां संख्यायाश्चापि संशये मात्रज्**: शममात्रम्,\n'
        '  **दशमात्रा गावः**, about ten cows'
    ),
    '5.2.38': (
        'SETTLED — पुरुषहस्तिभ्यामण् च — and the च keeps all three of the\n'
        '  rule before, so four forms apiece. पुरुषः प्रमाणमस्य **पौरुषम्**,\n'
        '  पुरुषद्वयसम्, पुरुषदघ्नम्, पुरुषमात्रम्; **हास्तिनम्**,\n'
        '  हस्तिद्वयसम्. **द्विगोर्नित्यं लुक्** — after a numeral compound\n'
        '  the affix always drops: **द्विपुरुषमुदकम्**, water two men deep;\n'
        '  द्विहस्ति, and in the feminine द्विपुरुषी, द्विहस्तिनी'
    ),
    '5.2.39': (
        'SETTLED — यत्तदेतेभ्यः परिमाणे वतुप्. यत् परिमाणमस्य **यावान्**;\n'
        '  तावान्, एतावान्. **AND परिमाण IS SAID THOUGH प्रमाण IS ALREADY\n'
        '  RUNNING**, because the two are different things, and a kārikā\n'
        '  gives the reason: डावतावर्थवैशेष्यान् निर्देशः पृथगुच्यते ।\n'
        '  मात्राद्यप्रतिघाताय भावः सिद्धश्च डावतोः ॥ **वतुप्प्रकरणे\n'
        '  युष्मदस्मद्भ्यां छन्दसि सादृश्य उपसंख्यानम्** — and in the Veda\n'
        '  the same affix for LIKENESS after the pronouns: न **त्वावाँ**\n'
        '  अन्यो दिव्यो न पार्थिवः (ऋ० ७.३२.२३); यज्ञं विप्रस्य **मावतः** (ऋ०\n'
        '  १.१४२.२), **त्वत्सदृशस्य मत्सदृशस्येत्यर्थः**'
    ),
    '5.2.40': (
        'SETTLED — किमिदंभ्यां वो घः — a substitution, and the vṛtti reads\n'
        '  the affix out of it. **एतदेव चादेशविधानं ज्ञापकं किमिदंभ्यां वतुप्\n'
        '  प्रत्ययो भवतीति**: that a substitute is enjoined for the व of\n'
        '  वतुप् after these two TELLS you the affix comes after them at all,\n'
        '  which no rule had said. **कियान्, इयान्**. **अथ वा योगविभागेन\n'
        '  वतुपं विधाय पश्चाद् वो घो विधीयते** — or else the rule is split in\n'
        '  two'
    ),
    '5.2.41': (
        'SETTLED — किमः संख्यापरिमाणे डति च. **संख्यायाः परिमाणं\n'
        '  संख्यापरिच्छेद इत्यर्थः** — the measuring OF a number, that is,\n'
        '  its being determined. का संख्या परिमाणमेषाम् **कति ब्राह्मणाः**,\n'
        '  and by the च with the substitution, **कियन्तो ब्राह्मणाः**. **AND\n'
        '  WHY संख्या IS QUALIFIED BY परिमाण AT ALL**, since a number is a\n'
        '  determining thing already: **यत्रापरिच्छेदकत्वेन विवक्ष्यते तत्र\n'
        '  मा भूदिति; क्षेपे हि परिच्छेदो नास्ति** — where a number is used\n'
        '  in CONTEMPT nothing is being determined, **केयमेषां संख्या\n'
        '  दशानाम्**, *what sort of number is this, ten?*'
    ),
    '5.2.42': (
        'SETTLED — संख्याया अवयवे तयप्. **अवयवा अवयविनः संबन्धिन इति\n'
        '  सामर्थ्याद् अवयवी प्रत्ययार्थो विज्ञायते** — parts belong to a\n'
        '  WHOLE, so what the affix reports is the whole and not the parts.\n'
        '  पञ्च अवयवा अस्य **पञ्चतयम्**; दशतयम्, चतुष्टयम्, चतुष्टयी'
    ),
    '5.2.43': (
        'SETTLED — द्वित्रिभ्यां तयस्यायज् वा — and it replaces the affix\n'
        '  rather than adding one. **द्वयम्, द्वितयम्**; त्रयम्, त्रितयम्.\n'
        '  **AND THE RULE NAMES THE AFFIX IT REPLACES FOR A REASON.**\n'
        '  **तयग्रहणं स्थानिनिर्देशार्थम्; अन्यथा प्रत्ययान्तरमयज् विज्ञायेत।\n'
        '  तत्र को दोषः?** — if अयज् were a separate affix instead of a\n'
        '  substitute, then **त्रयी गतिरिति तयनिबन्धन ईकारो न स्यात्**, the\n'
        '  feminine ई that hangs on तय would not come, and 1.1.33\n'
        '  प्रथमचरमतया… would not apply either. A substitution keeps what the\n'
        '  original was entitled to'
    ),
    '5.2.44': (
        'SETTLED — उभादुदात्तो नित्यम् — the same substitute, but obligatory\n'
        '  and accented. **वचनसामर्थ्याद् आदेर् उदात्तत्वं विज्ञायते** — the\n'
        '  force of the statement shows the accent is on the FIRST syllable.\n'
        '  **उभयो मणिः**; उ॒भये॑ऽस्य देवमनु॒ष्याः. **उभशब्दो यदि लौकिकी\n'
        '  संख्या, ततः पूर्वेणैव विहितस्य तयप आदेशविधानार्थं वचनम्; अथ न\n'
        '  संख्या, ततो योगविभागेन तयपं विधाय** — and whether the rule adds a\n'
        '  substitute or first supplies the affix too depends on whether उभ\n'
        '  counts as a numeral at all'
    ),
    '5.2.45': (
        'SETTLED — तदस्मिन्नधिकमिति दशान्ताड् डः — and every word of it is\n'
        '  tested. एकादश अधिका अस्मिन् शते **एकादशं शतम्**, a hundred and\n'
        '  eleven. **दशान्तादिति किम्?** पञ्चाधिका अस्मिन् शते. **अन्तग्रहणं\n'
        '  किम्?** दशाधिका अस्मिन् शते. And two restrictions the rule does\n'
        '  not state: **प्रत्ययार्थेन च समानजातीये प्रकृत्यर्थे सति प्रत्यय\n'
        '  इष्यते** — the excess must be of the SAME KIND, so एकादश माषा\n'
        '  अधिका अस्मिन् कार्षापणशते takes nothing; and\n'
        '  **शतसहस्रयोश्चेष्यते**, only of a hundred or a thousand, so not\n'
        '  एकादशाधिका अस्यां त्रिंशति. Both are got from the word इति:\n'
        '  **इतिकरणो विवक्षार्थ इत्युक्तम्, तत इदं सर्वं लभ्यते**. A kārikā\n'
        '  sums it: अधिके समानजाताविष्टं शतसहस्रयोः । यस्य संख्या तदाधिक्ये\n'
        '  डः कर्तव्यो मतो मम ॥'
    ),
    '5.2.46': (
        'SETTLED — शदन्तविंशतेश्च. त्रिंशदधिका अस्मिञ् छते **त्रिंशं शतम्**;\n'
        '  विंशं शतम्. **शद्ग्रहणेऽन्तग्रहणं प्रत्ययग्रहणे यस्मात् स तदादेः\n'
        '  अधिकार्थम्** — the word *ending in* is there so that a compound\n'
        '  ENDING in शद् is reached: **एकत्रिंशं शतम्**, एकचत्वारिंशं शतम्.\n'
        '  And **तदन्तादपीति वक्तव्यम्** does the same for विंशति: एकविंशं\n'
        '  शतम्. **संख्याग्रहणं च कर्तव्यम्** — twice, and both times to keep\n'
        '  out a compound that merely ends in the sound: **इह मा भूद् —\n'
        '  गोत्रिंशदधिका अस्मिन् गोशते**'
    ),
    '5.2.47': (
        'SETTLED — संख्याया गुणस्य निमाने मयट्. **गुणो भागः; निमानं मूल्यम्**\n'
        '  — a part, and a price. यवानां द्वौ भागौ निमानमस्योदश्विद्भागस्य\n'
        '  **द्विमयमुदश्विद् यवानाम्**, buttermilk worth two parts of barley.\n'
        '  **भागेऽपि तु विधीयमानः प्रत्ययः प्राधान्येन भागवन्तमाचष्टे** —\n'
        '  though given for the part, the affix names what HAS the part,\n'
        '  which is why the words agree. Four conditions, none of them in the\n'
        '  sūtra. **गुणस्येति चैकत्वं विवक्षितम्** — one kind of part only,\n'
        '  so not द्वौ भागौ यवानां त्रय उदश्वितः. **भूयसश्च वाचिकायाः\n'
        '  संख्यायाः प्रत्यय इष्यते** — a number greater than one, so not एको\n'
        '  भागो निमानमस्य, **बहुत्वमतन्त्रम्**, though two is enough.\n'
        '  **गुणशब्दः समानावयववचनः** — the parts must be EQUAL, so not\n'
        '  अध्यर्ध उदश्वित्. **निमेये चापि दृश्यते** — and the affix is seen\n'
        '  for the thing PRICED as well: **द्विमया यवा उदश्वितः**. **निमान\n'
        '  इति किम्?** द्विगुणं पच्यते तैलं क्षीरेण'
    ),
    '5.2.48': (
        'SETTLED — तस्य पूरणे डट् — the ORDINALS. **पूर्यतेऽनेनेति पूरणम्;\n'
        '  येन संख्या संख्यानं पूर्यते संपद्यते, स तस्याः पूरणः** — what\n'
        '  fills a count out. एकादशानां पूरण **एकादशः**; त्रयोदशः.\n'
        '  **यस्मिन्नुपसंजाते अन्या संख्या संपद्यते, स प्रत्ययार्थः** — what\n'
        '  the affix reports is that on whose arrival a NEW number comes\n'
        '  about. So **इह न भवति — पञ्चानां मुष्टिकानां पूरणो घटः**: a pot\n'
        '  that five handfuls fill is not a *fifth*'
    ),
    '5.2.49': (
        'SETTLED — नान्तादसंख्यादेर्मट् — an आगम on the affix the rule before\n'
        '  gave, after a numeral ending in न् that does not begin with a\n'
        '  numeral. **पञ्चानां पूरणः पञ्चमः**; सप्तमः. **नान्तादिति पञ्चमी डट\n'
        '  आगमसंबन्धे षष्ठीं प्रकल्पयति** — the ablative in the rule creates\n'
        '  the genitive that an आगम needs, since an augment belongs TO\n'
        '  something. **नान्तादिति किम्?** विंशतेः पूरणो **विंशः**.\n'
        '  **असंख्यादेरिति किम्?** एकादशानां पूरण **एकादशः**'
    ),
    '5.2.50': (
        'SETTLED — थट् च छन्दसि — a second augment for the same affix in the\n'
        '  Veda, **चकारात् पक्षे मडपि भवति**, the मट् of the rule before\n'
        '  standing in the other half. पर्णम॑यानि **पञ्चथा॑नि** भवन्ति\n'
        '  (काठ०सं० ८.२); सप्तथः॑. And the मट् too: **पञ्चम॑म्**\n'
        '  इन्द्रिय॑स्या॑पाक्रामत्'
    ),
    '5.2.51': (
        'SETTLED — षट्कतिकतिपयचतुरां थुक् — an augment for four named words.\n'
        '  षण्णां पूरणः **षष्ठः**; कतिथः, कतिपयथः, **चतुर्थः**. **AND ONE OF\n'
        '  THE FOUR IS NOT A NUMERAL AT ALL.** **कतिपयशब्दो न संख्या,\n'
        '  तस्यास्मादेव ज्ञापकाद् डट् प्रत्ययो विज्ञायते** — 5.2.48 gives the\n'
        '  ordinal affix after a NUMERAL, and कतिपय is none; that this rule\n'
        '  adds an augment to it is the evidence that it gets the affix at\n'
        '  all. The same reading a substitution gave at 5.2.40.\n'
        '  **चतुरश्छयतावाद्यक्षरलोपश्च** — a vārttika gives चतुर् two more\n'
        '  affixes with the loss of its first syllable: **तुरीयः, तुर्यः**'
    ),
    '5.2.52': (
        'SETTLED — बहुपूगगणसंघस्य तिथुक्. बहूनां पूरणो **बहुतिथः**; पूगतिथः,\n'
        '  गणतिथः, संघतिथः. **पूगसंघशब्दयोरसंख्यात्वाद् इदमेव ज्ञापकं डटो\n'
        '  भावस्य** — and the same reading a second time: पूग and संघ are not\n'
        '  numerals either, so this rule is what tells you they take the\n'
        '  ordinal affix'
    ),
    '5.2.53': (
        'SETTLED — वतोरिथुक्. **वत्वन्तस्य संख्यात्वात् पूर्वेण डड् विहितः,\n'
        '  तस्मिन्नयमागमो विधीयते** — a word in वतु is a numeral already, so\n'
        '  5.2.48 gave it the affix and this only adds the augment.\n'
        '  **यावतिथः, तावतिथः, एतावतिथः**'
    ),
    '5.2.54': (
        'SETTLED — द्वेस्तीयः, डटोऽपवादः. द्वयोः पूरणो **द्वितीयः**'
    ),
    '5.2.55': (
        'SETTLED — त्रेः संप्रसारणं च, डटोऽपवादः — the same affix and a\n'
        '  vowel-substitution yoked to it, **तत्सन्नियोगेन**. त्रयाणां पूरणः\n'
        '  **तृतीयः**. And two rules that would have applied do not: **हलः\n'
        '  इति संप्रसारणस्य दीर्घत्वं न भवति** (6.4.2), the substituted vowel\n'
        '  is not lengthened; and the अण् of 6.3.111 is carried into that\n'
        '  rule from ढ्रलोपे…, **पूर्वेण च णकारेणाण्ग्रहणम्**'
    ),
    '5.2.56': (
        'SETTLED — विंशत्यादिभ्यस्तमडन्यतरस्याम् — an optional augment, so\n'
        '  both forms stand. विंशतेः पूरणो **विंशतितमः, विंशः**; एकविंशतितमः,\n'
        '  एकविंशः; त्रिंशत्तमः, त्रिंशः. **AND THE LIST IS THE ORDINARY\n'
        '  NUMBER-WORDS AND NOT THE ONES 5.1.59 LAID DOWN.** **विंशत्यादयो\n'
        '  लौकिकाः संख्याशब्दा गृह्यन्ते, न पङ्क्त्यादिसूत्रसंनिविष्टाः;\n'
        '  तद्ग्रहणे ह्येकविंशतिप्रभृतिभ्यो न स्यात्, ग्रहणवता प्रातिपदिकेन\n'
        "  तदन्तविधिप्रतिषेधात्** — if the sūtra's own words were meant, a\n"
        '  rule naming them could not reach compounds ending in them, and\n'
        '  एकविंशति would be left out. **एवं च सति षष्ट्यादेश्चासंख्यादेः इति\n'
        '  पर्युदासो युज्यत एव**'
    ),
    '5.2.57': (
        'SETTLED — नित्यं शतादिमासार्धमाससंवत्सराच्च — and here the augment\n'
        '  is obligatory. शतस्य पूरणः **शततमः**; सहस्रतमः, लक्षतमः; **मासतमो\n'
        '  दिवसः**, अर्धमासतमः, संवत्सरतमः. **मासादयः संख्याशब्दा न भवन्ति,\n'
        '  तेभ्योऽस्मादेव ज्ञापकाद् डट् प्रत्ययो विज्ञायते** — a third time\n'
        '  the same reading: month and fortnight and year are not numerals,\n'
        '  and this rule is the evidence that they take the ordinal affix.\n'
        '  **षष्ट्यादेश्चासंख्यादेः इति वक्ष्यमाणेन सिद्धे शतादिग्रहणं\n'
        '  संख्याद्यर्थम्** — 5.2.58 would cover शत anyway, so naming it here\n'
        '  is for the compounds that BEGIN with a numeral: **एकशततमः,\n'
        '  द्विशततमः**'
    ),
    '5.2.58': (
        'SETTLED — षष्ट्यादेश्चासंख्यादेः. **विंशत्यादिभ्यः इति विकल्पेन\n'
        '  प्राप्ते नित्यार्थम्** — 5.2.56 made it optional and this makes it\n'
        '  fixed. **षष्टितमः, सप्ततितमः**. **असंख्यादेरिति किम्?** एकषष्टः,\n'
        '  एकषष्टितमः — where a numeral stands first the choice comes back'
    ),
    '5.2.59': (
        'SETTLED — मतौ छः सूक्तसाम्नोः. **मताविति मत्वर्थ उच्यते** — *having\n'
        '  it*, and the whole relation is got from that one word:\n'
        '  **मत्वर्थग्रहणेन समर्थविभक्तिः, प्रकृतिविशेषणं प्रत्ययार्थ इति\n'
        '  सर्वम् आक्षिप्यते**. अच्छावाकशब्दोऽस्मिन्निति **अच्छावाकीयं\n'
        '  सूक्तम्**; **यज्ञायज्ञीयं साम**. **अनुकरणशब्दाश्च\n'
        '  स्वरूपमात्रप्रधानाः प्रत्ययम् उत्पादयन्ति; तेनानेकपदादपि सिद्धम्**\n'
        '  — a quoted string counts as one word for this, so the affix comes\n'
        '  after a whole phrase: **अस्यवामीयम्**, **कयाशुभीयम्**, hymns named\n'
        '  from their first words'
    ),
    '5.2.60': (
        'SETTLED — अध्यायानुवाकयोर्लुक् — the affix removed where the thing\n'
        '  named is a CHAPTER or a section. **केन पुनरध्यायानुवाकयोः\n'
        '  प्रत्ययः? इदमेव लुग्वचनं ज्ञापकं तद्विधानस्य** — and by what rule\n'
        '  did they have the affix at all? By this one: that its removal is\n'
        '  enjoined is the evidence that it was given. The reading a fourth\n'
        '  time in twenty sūtras. **विकल्पेन च लुगयमिष्यते** — and the\n'
        '  removal is optional, so **गर्दभाण्डोऽध्यायः** stands beside\n'
        '  गर्दभाण्डीयः'
    ),
    '5.2.61': (
        'SETTLED — विमुक्तादिभ्योऽण्. विमुक्तशब्दोऽस्मिन्नस्ति\n'
        '  **वैमुक्तोऽध्यायोऽनुवाको वा**; दैवासुरः. विमुक्त, देवासुर, वसुमत्,\n'
        '  सत्वत्, उपसत्, हविर्धान, मित्री, सोमापूषन्, अग्नाविष्णु, वृत्रहति,\n'
        '  इडा, रक्षोसुर, सदसत्, वसु, मरुत्वत्, पत्नीवत्, दशार्ह, वयस्,\n'
        '  पतत्रि, सोम, हेतु — विमुक्तादिः'
    ),
    '5.2.62': (
        'SETTLED — गोषदादिभ्यो वुन्. **गोषदकोऽध्यायोऽनुवाको वा**; इषेत्वकः,\n'
        '  मातरिश्वकः. गोषद, इषेत्वा, मातरिश्वन्, देवस्यत्वा, देवीरापः,\n'
        '  कृष्णोस्याखरेष्टः, दैवींधियम्, रक्षोहण, अञ्जन, प्रभूत, प्रतूर्त,\n'
        '  कृशानु — गोषदादिः, and most of them are the opening words of what\n'
        '  they name'
    ),
    '5.2.63': (
        'SETTLED — तत्र कुशलः पथः. पथि कुशलः **पथकः**, one who knows the road'
    ),
    '5.2.64': (
        'SETTLED — आकर्षादिभ्यः कन्. आकर्षे कुशल **आकर्षकः**; त्सरुकः. आकर्ष,\n'
        '  त्सरु, पिपासा, पिचण्ड, अशनि, अश्मन्, विचय, चय, जय, आचय, अय, नय,\n'
        '  निपाद, गद्गद, दीप, ह्रद, ह्लाद, शकुनि — आकर्षादिः'
    ),
    '5.2.65': (
        'SETTLED — धनहिरण्यात् कामे. **काम इच्छा अभिलाषः**. धने कामो **धनको\n'
        '  देवदत्तस्य**; हिरण्यको देवदत्तस्य'
    ),
    '5.2.66': (
        'SETTLED — स्वाङ्गेभ्यः प्रसिते. **प्रसितः प्रसक्तस्तत्पर इत्यर्थः**\n'
        '  — taken up with, intent on. केशेषु प्रसितः **केशकः**,\n'
        '  **केशादिरचनायां प्रसक्त एवम् उच्यते**, one always at his hair.\n'
        '  **बहुवचनं स्वाङ्गसमुदायशब्दादपि यथा स्यात्** — the plural in the\n'
        '  rule lets a compound of several limbs in: **दन्तौष्ठकः, केशनखकः**'
    ),
    '5.2.67': (
        'SETTLED — उदराट् ठगाद्यूने. **आद्यून इति प्रत्ययार्थविशेषणम्;\n'
        '  उदरेऽविजिगीषुर्भण्यते; यो बुभुक्षयात्यन्तं पीड्यते, स एवमुच्यते**\n'
        '  — one who cannot master his belly, tormented by hunger. उदरे\n'
        '  प्रसित **औदरिक आद्यूनः**. **आद्यून इति किम्?** उदरकः — for anyone\n'
        '  else merely intent on his stomach, the affix of the rule before'
    ),
    '5.2.68': (
        'SETTLED — सस्येन परिजातः. **कन् प्रत्यय इत्येव स्वर्यते, न ठक्** —\n'
        '  the कन् of 5.2.64 carries down and the ठक् of the rule just before\n'
        '  does not. **सस्यशब्दोऽयं गुणवाची; परिः सर्वतो भावे वर्तते; यो\n'
        '  गुणैः संबद्धो जायते, यस्य किंचिदपि वैगुण्यं नास्ति** — born with\n'
        '  every quality and no flaw anywhere: **सस्यकः शालिः**, सस्यकः\n'
        '  साधुः, सस्यको मणिः, **आकरशुद्ध इत्यर्थः**, flawless from the mine'
    ),
    '5.2.69': (
        'SETTLED — अंशं हारी. अंशं हारी **अंशको दायादः**, an heir with a\n'
        '  share coming. **हारीत्यावश्यके णिनिः** (3.3.170), and **तत्र\n'
        '  षष्ठीप्रतिषेधात् कर्मणि द्वितीयैव भवति** — the genitive being\n'
        '  forbidden with that participle, the object stands in the\n'
        '  accusative'
    ),
    '5.2.70': (
        'SETTLED — तन्त्रादचिरापहृते. **अचिरापहृतः स्तोककालापहृत इत्यर्थः** —\n'
        '  taken off a short time ago. तन्त्रादचिरापहृतः **तन्त्रकः पटः**,\n'
        '  cloth fresh from the loom, **प्रत्यग्रो नव उच्यते**'
    ),
    '5.2.71': (
        'SETTLED — ब्राह्मणकोष्णिके संज्ञायाम्. **निपात्येते** — two forms\n'
        '  laid down with that affix, as NAMES. **ब्राह्मणको देशः**,\n'
        '  **यत्रायुधजीविनो ब्राह्मणाः सन्ति**, a country where the brahmins\n'
        '  live by arms; **उष्णिका यवागूः**, **अल्पान्ना यवागूः**, a thin\n'
        '  gruel'
    ),
    '5.2.72': (
        'SETTLED — शीतोष्णाभ्यां कारिणि. **क्रियाविशेषणाद् द्वितीयासमर्थादयं\n'
        '  प्रत्ययः** — the base is an adverb standing in the accusative.\n'
        '  शीतं करोति **शीतकः**, **अलसो जड उच्यते**, a sluggard; उष्णं करोति\n'
        '  **उष्णकः**, **शीघ्रकारी दक्ष उच्यते**, a quick worker. Cold and\n'
        '  hot for slow and brisk'
    ),
    '5.2.73': (
        'SETTLED — अधिकम्. **अधिकमिति निपात्यते.**\n'
        '  **अध्यारूढशब्दस्योत्तरपदलोपः कंश्च प्रत्ययः**, the second member\n'
        '  dropped and क given. **अधिको द्रोणः खार्याम्; अधिका खारी द्रोणेन**\n'
        '  — and it works both ways, **कर्तरि कर्मणि चाध्यारूढशब्दः**'
    ),
    '5.2.74': (
        'SETTLED — अनुकाभिकाभीकः कमिता. **निपात्यन्ते** — three forms laid\n'
        '  down for one who DESIRES. **अभेः पक्षे दीर्घत्वं च निपात्यते** —\n'
        '  and the lengthening of अभि in one of them is laid down too.\n'
        '  अनुकामयत **अनुकः**; **अभिकः, अभीकः**'
    ),
    '5.2.75': (
        'SETTLED — पार्श्वेनान्विच्छति. **अनृजुरुपायः पार्श्वम्** — पार्श्व\n'
        '  is a crooked means. तेनार्थान् अन्विच्छति **पार्श्वकः**, **मायावी\n'
        '  कौसृतिको जालिक उच्यते**, a trickster'
    ),
    '5.2.76': (
        'SETTLED — अयःशूलदण्डाजिनाभ्यां ठक्ठञौ, **यथासंख्यम्**; the अयःशूल\n'
        '  member. **तीक्ष्ण उपायोऽयःशूलम् उच्यते** — an iron-spike is a\n'
        '  harsh means. तेनान्विच्छति **आयःशूलिकः**, **साहसिक इत्यर्थः**, a\n'
        '  man of violence\n'
        '\n'
        'SETTLED — अयःशूलदण्डाजिनाभ्यां ठक्ठञौ, the दण्डाजिन member. **दम्भो\n'
        '  दण्डाजिनम्** — staff-and-deerskin is hypocrisy. तेनान्विच्छति\n'
        '  **दाण्डाजिनिकः**, **दाम्भिक इत्यर्थः**'
    ),
    '5.2.77': (
        'SETTLED — तावतिथं ग्रहणमिति लुग् वा. **तावतां पूरणं तावतिथम्;\n'
        '  गृह्यतेऽनेनेति ग्रहणम्** — from a word already made by an ORDINAL\n'
        '  affix, in its own sense, with that affix optionally removed.\n'
        '  द्वितीयेन रूपेण ग्रन्थं गृह्णाति **द्विकं ग्रहणम्, द्वितीयकम्**;\n'
        '  त्रिकम्, तृतीयकम्. **तावतिथेन गृह्णातीति कन् वक्तव्यः,\n'
        '  पूरणप्रत्ययस्य च नित्यं लुक्** — and a vārttika gives the same\n'
        '  affix for the READER rather than the reading, with the removal\n'
        '  obligatory: षष्ठेन रूपेण ग्रन्थं गृह्णाति **षट्को देवदत्तः**.\n'
        '  **इतिकरणो विवक्षार्थः; तेन ग्रन्थविषयमेव ग्रहणं विज्ञायते,\n'
        '  नान्यविषयम्** — the इति confines the *taking* to taking in a TEXT'
    ),
    '5.2.78': (
        'SETTLED — स एषां ग्रामणीः. **ग्रामणीः प्रधानो मुख्य इत्यर्थः** — the\n'
        '  chief of them. देवदत्तो ग्रामणीरेषां **देवदत्तकाः**; यज्ञदत्तकाः.\n'
        '  **ग्रामणीरिति किम्?** देवदत्तः शत्रुरेषाम् — a leader and not\n'
        '  merely someone they all have in common'
    ),
    '5.2.79': (
        'SETTLED — शृङ्खलमस्य बन्धनं करभे — and both the tether and the thing\n'
        '  tethered are named. **उष्ट्राणां बालकाः करभाः** — करभ is a camel\n'
        '  calf; **तेषां काष्ठमयं पाशकं पादे व्यतिषज्यते, तदुच्यते\n'
        '  शृङ्खलम्**, and शृङ्खल is the wooden hobble put on its foot.\n'
        '  शृङ्खलं बन्धनमस्य करभस्य **शृङ्खलकः**. **यद्यपि रज्ज्वादिकमपि\n'
        '  तत्रास्ति तथापि शृङ्खलमस्य अस्वतन्त्रीकरणे भवति साधनमिति\n'
        '  बन्धनमित्युच्यते** — there is a rope on it too, and the hobble is\n'
        "  called the BOND because it is what takes the animal's freedom away"
    ),
    '5.2.80': (
        'SETTLED — उत्क उन्मनाः — **उत्क इति निपात्यते**. **उद्गतं मनो यस्य स\n'
        '  उन्मनाः** — one whose mind has gone up and out. **उच्छब्दात्\n'
        '  ससाधनक्रियावचनात् तद्वति कन् प्रत्ययो निपात्यते**: **उत्को\n'
        '  देवदत्तः**; उत्कः प्रवासी, **उत्सुक इत्यर्थः**, a man away from\n'
        '  home and longing'
    ),
    '5.2.81': (
        'SETTLED — कालप्रयोजनाद् रोगे — from a word for a TIME or for a\n'
        '  CAUSE, of a disease. **अर्थलभ्या समर्थविभक्तिः** — the case is got\n'
        '  from the sense, each as it fits. **कालो दिवसादिः; प्रयोजनं कारणं\n'
        '  रोगस्य फलं वा**. द्वितीयेऽह्नि भवो **द्वितीयको ज्वरः**, a fever of\n'
        '  the second day; **चतुर्थकः**, a quartan. And from a cause:\n'
        '  विषपुष्पैर्जनितो **विषपुष्पको ज्वरः**; उष्णं कार्यमस्य **उष्णको\n'
        '  ज्वरः**. **उत्तरसूत्राद् इह संज्ञाग्रहणम् अपकृष्यते; तेनायं\n'
        '  प्रकारनियमः सर्वो लभ्यते** — and the *naming* is pulled BACKWARD\n'
        '  from the next rule, which is what makes all these settled names of\n'
        '  particular fevers'
    ),
    '5.2.82': (
        'SETTLED — तदस्मिन्नन्नं प्राये संज्ञायाम्. **प्रायो बाहुल्यम्** —\n'
        '  mostly. गुडापूपाः प्रायेणान्नमस्यां पौर्णमास्यां **गुडापूपिका**, a\n'
        '  full-moon day whose food is chiefly cakes in molasses; तिलापूपिका.\n'
        '  **संज्ञाग्रहणं तदन्तोपाधिः**. **वटकेभ्य इनिर्वक्तव्यः** — and a\n'
        '  different affix for one of them: **वटकिनी पौर्णमासी**'
    ),
    '5.2.83': (
        'SETTLED — कुल्माषादञ्. **ञकारो वृद्धिस्वरार्थः** — the ञ is for the\n'
        '  strengthening and the accent. कुल्माषाः प्रायेणान्नमस्यां\n'
        '  **कौल्माषी पौर्णमासी**'
    ),
    '5.2.84': (
        'SETTLED — श्रोत्रियंश्छन्दोऽधीते — **श्रोत्रियन्निति निपात्यते**,\n'
        '  and the whole SENTENCE is what the form stands for:\n'
        '  **श्रोत्रियंश्छन्दोऽधीत इति वाक्यार्थे पदवचनम्**, one word for *he\n'
        '  has learnt the Veda*. **नकारः स्वरार्थः**. **श्रोत्रियो\n'
        '  ब्राह्मणः**. **छन्दसो वा श्रोत्रभावः, तदधीत इति घंश्च प्रत्ययः** —\n'
        '  or else छन्दस् becomes श्रोत्र and घन् is the affix. **कथं\n'
        '  छन्दोऽधीते छान्दसः?** And how is the ordinary form छान्दसः\n'
        '  explained? **वाग्रहणमनुवर्तते** — the *optionally* of 5.2.77\n'
        '  carries down, so this form is one of two'
    ),
    '5.2.85': (
        'SETTLED — श्राद्धमनेन भुक्तमिनिठनौ. **श्राद्धशब्दः कर्मनामधेयं\n'
        '  तत्साधने द्रव्ये वर्तित्वा प्रत्ययम् उत्पादयति** — the word names\n'
        '  the RITE and then, standing for the food of it, takes the affix.\n'
        '  श्राद्धं भुक्तमनेन **श्राद्धी, श्राद्धिकः**. **इनिठनोः\n'
        '  समानकालग्रहणम्; अद्य भुक्ते श्राद्धे श्वः श्राद्धिक इति प्रयोगो मा\n'
        '  भूत्** — the eating and the naming must be of one time, so a man\n'
        '  who ate at a śrāddha today is not called that tomorrow'
    ),
    '5.2.86': (
        'SETTLED — पूर्वादिनिः. **अनेनेति प्रत्ययार्थः कर्ता अनुवर्तते; न च\n'
        '  क्रियामन्तरेण कर्ता संभवतीति यां कांचित् क्रियामध्याहृत्य प्रत्ययो\n'
        '  विधेयः** — the affix reports an AGENT, and an agent needs an\n'
        '  action, so some action or other has to be supplied. पूर्वं गतमनेन\n'
        '  भुक्तं पीतं वा **पूर्वी**, one who went, or ate, or drank before'
    ),
    '5.2.87': (
        'SETTLED — सपूर्वाच्च — from a stem ENDING in that word with\n'
        '  something before it. पूर्वं कृतमनेन **कृतपूर्वी कटम्**, one who\n'
        '  has made a mat before; भुक्तपूर्वी ओदनम्. **सुप्सुपेति समासं\n'
        '  कृत्वा तद्धित उत्पाद्यते** (2.1.4). **AND THE TWO RULES TOGETHER\n'
        '  TEACH TWO PARIBHĀṢĀS.** **योगद्वयेन चानेन पूर्वादिनिः\n'
        '  सपूर्वाच्चेति परिभाषाद्वयं ज्ञाप्यते** — that 5.2.87 is needed at\n'
        '  all shows **व्यपदेशिवद्भावोऽप्रातिपदिकेन** and **ग्रहणवता\n'
        '  प्रातिपदिकेन तदन्तविधिर्नास्ति**, that a rule naming a word does\n'
        '  not reach compounds ending in it. Two general principles read out\n'
        '  of one rule being split in two'
    ),
    '5.2.88': (
        'SETTLED — इष्टादिभ्यश्च. **इष्टी यज्ञे**, one who has sacrificed;\n'
        '  **पूर्ती श्राद्धे**. **क्तस्येन्विषयस्य कर्मणि इति\n'
        '  सप्तम्युपसंख्यायते** (वा० २.३.३६) — and a supplement gives the\n'
        '  locative for the object. इष्ट, पूर्त, उपसादित, निगदित, संकलित,\n'
        '  निपठित, संकल्पित, अर्चित, पूजित, परिगणित, आम्नात, श्रुत, अधीत,\n'
        '  आसेवित, निराकृत, उपकृत, अनुयुक्त, निगृहीत — इष्टादिः, and every\n'
        '  one of them is a past participle'
    ),
    '5.2.89': (
        'SETTLED — छन्दसि परिपन्थिपरिपरिणौ पर्यवस्थातरि. **निपात्येते** — two\n'
        '  forms laid down for the Veda. **पर्यवस्थाता प्रतिपक्षः सपत्न\n'
        '  उच्यते** — one who stands in the way, an adversary. मा त्वा॑\n'
        '  **परिप॒रिणो॑** विद॒न् मा त्वा॑ **परिप॒न्थिनो॑** विद॒न् (मा०सं०\n'
        '  ४.३४)'
    ),
    '5.2.90': (
        'SETTLED — अनुपद्यन्वेष्टा — **अनुपदीति निपात्यते**. **पदस्य\n'
        '  पश्चादनुपदम्** — on the track of. **अनुपदी गवाम्**, one who\n'
        '  follows cattle to find them; अनुपदी उष्ट्राणाम्'
    ),
    '5.2.91': (
        'SETTLED — साक्षाद् द्रष्टरि संज्ञायाम्. **साक्षाच्छब्दो ऽव्ययम्** —\n'
        '  an indeclinable, and the affix comes after it. साक्षाद् द्रष्टा\n'
        '  **साक्षी**, a witness. **संज्ञाग्रहणमभिधेयनियमार्थम्;\n'
        '  संज्ञाग्रहणाद् उपद्रष्टैवोच्यते, न दाता ग्रहीता वा** — the naming\n'
        '  confines it to the ONLOOKER, so a man who gives evidence or takes\n'
        '  it is not called by the word'
    ),
    '5.2.92': (
        'SETTLED — क्षेत्रियच् परक्षेत्रे चिकित्स्यः. **क्षेत्रियजिति\n'
        '  निपात्यते**, **परशब्दलोपश्च**, and the vṛtti offers FOUR readings\n'
        '  and accepts them all. **परक्षेत्रं जन्मान्तरशरीरम्, तत्र\n'
        '  चिकित्स्यः क्षेत्रियः** — a disease curable only in another\n'
        "  birth's body, that is, incurable: **नामृतस्य निवर्तत इत्यर्थः**.\n"
        '  Or **क्षेत्रियं विषम्, यत् परक्षेत्रे परशरीरे संक्रमय्य\n'
        '  चिकित्स्यते**, a poison treated by moving it into another body. Or\n'
        '  **क्षेत्रियाणि तृणानि, यानि सस्यार्थे क्षेत्रे जातानि चिकित्स्यानि\n'
        '  नाशयितव्यानि**, weeds in a cornfield, *treated* by being\n'
        '  destroyed. Or **क्षेत्रियः पारदारिकः; परदाराः परक्षेत्रम्, तत्र\n'
        '  चिकित्स्यो निग्रहीतव्यः**, an adulterer, *treated* by being\n'
        '  punished. **सर्वं चैतत् प्रमाणम्** — and all of it is\n'
        '  authoritative. The third place in these two pādas where the Kāśikā\n'
        '  declines to choose'
    ),
    '5.2.93': (
        'SETTLED — इन्द्रियमिन्द्रलिङ्गमिन्द्रदृष्टमिन्द्रसृष्टम्\n'
        '  इन्द्रजुष्टमिन्द्रदत्तमिति वा — six derivations for one word, and\n'
        '  the rule ends by saying it does not matter which.\n'
        '  **इन्द्रियमित्यन्तोदात्तं शब्दरूपं निपात्यते; रूढिरेषा\n'
        '  चक्षुरादीनां करणानाम्; तथा च व्युत्पत्तेरनियमं दर्शयति** — the\n'
        '  word is the settled name of the eye and the other instruments, and\n'
        '  the rule SHOWS that its derivation is not fixed. **इन्द्र आत्मा, स\n'
        '  चक्षुरादिना करणेनानुमीयते; नाकर्तृकं करणमस्ति** — इन्द्र is the\n'
        '  self, inferred from the instruments, since no instrument is\n'
        "  without an agent. So: the self's MARK, or what the self SEES by,\n"
        '  or SENDS FORTH, or RESORTS TO, or GIVES to the objects **यथायथं\n'
        '  ग्रहणाय**. **इतिकरणः प्रकारार्थः; सति संभवे व्युत्पत्तिर् अन्यथापि\n'
        '  कर्तव्या, रूढेरनियमादिति। वाशब्दः प्रत्येकमभिसंबध्यमानो विकल्पानां\n'
        '  स्वातन्त्र्यं दर्शयति** — the इति means *and so on*, so other\n'
        '  derivations may be made where they will serve, and the वा goes\n'
        '  with each severally, so no one of the six depends on another'
    ),
    '5.2.94': (
        'SETTLED — तदस्यास्त्यस्मिन्निति मतुप् — the rule by which Sanskrit\n'
        '  says a thing HAS something, and the one this module is named for.\n'
        '  **तदिति प्रथमा समर्थविभक्तिः; अस्यास्मिन्निति प्रत्ययार्थौ;\n'
        '  अस्तीति प्रकृतिविशेषणम्; इतिकरणो विवक्षार्थः**. गावोऽस्य सन्ति\n'
        '  **गोमान् देवदत्तः**; वृक्षा अस्मिन् सन्ति **वृक्षवान् पर्वतः**.\n'
        '  **AND THE इति FIXES WHEN IT MAY BE SAID AT ALL.** **इतिकरणाद्\n'
        '  विषयनियमः**, and a kārikā names the seven grounds:\n'
        '  भूमनिन्दाप्रशंसासु नित्ययोगेऽतिशायने । संसर्गेऽस्तिविवक्षायां\n'
        '  भवन्ति मतुबादयः ॥ ABUNDANCE — **गोमान्**. BLAME — **कुष्ठी**.\n'
        '  PRAISE — **रूपवती कन्या**. CONSTANT CONNECTION — **क्षीरिणो\n'
        '  वृक्षाः**. EXCESS — **उदरिणी कन्या**. CONTACT — **दण्डी, छत्री**.\n'
        '  And the bare wish to say *it is there* — **अस्तिमान्**. Seven, and\n'
        '  mere possession is not among them. **गुणवचनेभ्यो मतुपो लुग्\n'
        '  वक्तव्यः** — and after a quality-word the affix drops: शुक्लो\n'
        '  गुणोऽस्यास्ति **शुक्लः पटः**'
    ),
    '5.2.95': (
        'SETTLED — रसादिभ्यश्च. **रसवान्, रूपवान्**. **किमर्थमिदमुच्यते, न\n'
        '  पूर्वसूत्रेणैव मतुप् सिद्धः?** Why is it said, when 5.2.94 gives\n'
        '  मतुप् already? **रसादिभ्यः पुनर्वचनम् अन्यनिवृत्त्यर्थम्; अन्ये\n'
        '  मत्वर्थीया मा भूवन्** — to shut the OTHER possessive affixes out,\n'
        '  so that only मतुप् comes after these. **कथं रूपिणी कन्या, रूपिको\n'
        '  दारकः? प्रायिकमेतद् वचनम्** — and those forms stand because the\n'
        '  restriction holds for the most part. **गुणग्रहणं रसादीनां\n'
        '  विशेषणम्** — and the list is of QUALITIES: रस, रूप, गन्ध, स्पर्श,\n'
        '  शब्द, स्नेह, **गुणात्** (ग०सू०१२४), **एकाचः** (ग०सू०१२५). **तेन ये\n'
        '  रसनेन्द्रियादिग्राह्या गुणाः, तेषामेवायं पाठः** — only the\n'
        '  qualities the senses take in'
    ),
    '5.2.96': (
        'SETTLED — प्राणिस्थादातो लजन्यतरस्याम् — from a word ending in आ\n'
        '  that stands for something ON A LIVING BODY, optionally लच्, so the\n'
        '  मतुप् stands beside it. **चूडालः, चूडावान्**; कर्णिकालः,\n'
        '  कर्णिकावान्. **प्राणिस्थादिति किम्?** शिखावान् प्रदीपः — a lamp\n'
        '  has a flame-crest and is not a living body. **आदिति किम्?**\n'
        '  हस्तवान्, पादवान्. And **प्राण्यङ्गादिति वक्तव्यम्** narrows it\n'
        '  further, **इह मा भूत् — चिकीर्षास्यास्ति चिकीर्षावान्**: a wish is\n'
        '  IN a living thing but is not a LIMB of one'
    ),
    '5.2.97': (
        'SETTLED — सिध्मादिभ्यश्च. **सिध्मलः, सिध्मवान्**; गडुलः, गडुमान्.\n'
        '  **अन्यतरस्यांग्रहणेन मतुप् समुच्चीयते न तु प्रत्ययो विकल्प्यते;\n'
        '  तस्माद् अकारान्तेभ्य इनिठनौ प्रत्ययौ न भवतः** — the *optionally*\n'
        '  GATHERS मतुप् in rather than making the affix itself a choice, and\n'
        '  the consequence is that इनि and ठन् do not come after these at\n'
        '  all. सिध्म, गडु, मणि, नाभि, जीव, पांसु, सक्तु, हनु, मांस, परशु,\n'
        '  **पार्ष्णिधमन्योर्दीर्घश्च** (ग०सू०१२६) — पार्ष्णीलः; पर्ण, उदक,\n'
        '  प्रज्ञा, पार्श्व, गण्ड, ग्रन्थि, **वातदन्तबलललाटानामूङ् च**\n'
        '  (ग०सू०१२७) — वातूलः, दन्तूलः; **जटाघटाकलाः क्षेपे** (ग०सू०१२८) —\n'
        '  जटालः; कर्ण, स्नेह, शीत, श्याम, पित्त, पृथु, मृदु, कण्डु,\n'
        '  **क्षुद्रजन्तूपतापाच्चेष्यते** (ग०सू०१२९) — यूकालः, मक्षिकालः, and\n'
        '  for an affliction विचर्चिकालः, **मूर्छालः** — सिध्मादिः'
    ),
    '5.2.98': (
        'SETTLED — वत्सांसाभ्यां कामबले, **यथासंख्यम्**; the वत्स member.\n'
        '  **वत्सलः**, and it does not mean *having a calf*: **वृत्तिविषये\n'
        '  वत्सांसशब्दौ स्वभावात् कामबलयोर्वर्तमानौ तद्वति प्रत्ययमुत्पादयतः;\n'
        '  न ह्यत्र वत्सार्थोंऽसार्थो वा विद्यते** — inside the derivation\n'
        '  the two words stand for AFFECTION and STRENGTH by their own\n'
        '  nature, and the calf is not in it at all. **वत्सल इति\n'
        '  स्नेहवानुच्यते — वत्सलः स्वामी, वत्सलः पिता**. **न चायमर्थो मतुपि\n'
        '  संभवतीति नित्यं लजेव भवति** — and since मतुप् cannot carry that\n'
        '  sense, the affix here is not one of two but the only one.\n'
        '  **अन्यत्र वत्सवती गौः**, elsewhere the ordinary affix and the\n'
        '  ordinary sense\n'
        '\n'
        'SETTLED — वत्सांसाभ्यां कामबले, the अंस member. **अंसल इति\n'
        '  चोपचितमांसो बलवानुच्यते** — thick in the flesh, and so strong.\n'
        '  **अन्यत्र अंसवान् दुर्बलः**, where the ordinary affix leaves a man\n'
        '  with shoulders and no strength'
    ),
    '5.2.99': (
        'SETTLED — फेनादिलच् च — **चकारात् लच् च**, and the अन्यतरस्याम् of\n'
        '  5.2.96 carries: **अन्यतरस्यांग्रहणं मतुप्समुच्चयार्थं सर्वत्रैव\n'
        '  अनुवर्तते**, so मतुप् is gathered in through the whole stretch.\n'
        '  **फेनिलः, फेनलः, फेनवान्**'
    ),
    '5.2.100': (
        'SETTLED — लोमादिपामादिपिच्छादिभ्यः शनेलचः, **यथासंख्यम्**; the\n'
        '  लोमादि member. **लोमशः, लोमवान्**. लोमन्, रोमन्, वल्गु, बभ्रु,\n'
        '  हरि, कपि, शुनि, तरु — लोमादिः\n'
        '\n'
        'SETTLED — लोमादिपामादिपिच्छादिभ्यः शनेलचः, the पामादि member.\n'
        '  **पामनः, पामवान्**. पामन्, वामन्, हेमन्, श्लेष्मन्, कद्रु, बलि,\n'
        '  श्रेष्ठ, पलल, सामन्, **अङ्गात् कल्याणे** (ग०सू०१३०),\n'
        '  **शाकीपलालीदद्र्वां ह्रस्वत्वं च** (ग०सू०१३१),\n'
        '  **विष्वगित्युत्तरपदलोपश्चाकृतसन्धेः** (ग०सू०१३२), **लक्ष्म्या\n'
        '  अच्च** (ग०सू०१३३) — पामादिः, and four of the entries carry an\n'
        '  operation of their own\n'
        '\n'
        'SETTLED — लोमादिपामादिपिच्छादिभ्यः शनेलचः, the पिच्छादि member.\n'
        '  **पिच्छिलः, पिच्छवान्**; उरसिलः, उरस्वान्. पिच्छ, उरस्, ध्रुवका,\n'
        '  क्षुवका, **जटाघटाकलाः क्षेपे** (ग०सू०१३४), वर्ण, उदक, पङ्क,\n'
        '  प्रज्ञा — पिच्छादिः'
    ),
    '5.2.101': (
        'SETTLED — प्रज्ञाश्रद्धार्चाभ्यो णः. **मतुप् सर्वत्र समुच्चीयते**.\n'
        '  **प्राज्ञः, प्रज्ञावान्**; श्राद्धः, श्रद्धावान्; आर्चः,\n'
        '  अर्चावान्; वार्त्तः, वृत्तिमान्'
    ),
    '5.2.102': (
        'SETTLED — तपःसहस्राभ्यां विनीनी, and NOT यथासंख्यम् —\n'
        '  **प्रत्ययार्थयोस्तु यथासंख्यं सर्वत्रैवास्मिन् प्रकरणे नेष्यते**,\n'
        '  the matching in order is not wanted anywhere in this section.\n'
        '  तपोऽस्यास्मिन् वा विद्यते **तपस्वी**; सहस्री. **AND THE RULE IS\n'
        '  NEEDLESS AND STATED ANYWAY.** **असन्तत्वाद् अदन्तत्वाच्च सिद्धे\n'
        '  प्रत्यये पुनर्वचनम् अणा वक्ष्यमाणेन बाधा मा भूदिति** — तपस् would\n'
        '  get विनि for ending in अस् and सहस्र would get इनि for ending in\n'
        '  अ; the rule is stated so that the अण् of the NEXT sūtra does not\n'
        '  displace them. **सहस्रात् तु ठनपि बाध्यते**\n'
        '\n'
        'SETTLED — तपःसहस्राभ्यां विनीनी, the सहस्र half — and the two\n'
        '  affixes are NOT matched to the two words in order, **यथासंख्यं\n'
        '  सर्वत्रैवास्मिन् प्रकरणे नेष्यते**. **सहस्री**'
    ),
    '5.2.103': (
        'SETTLED — अण् च — and the split from the rule before is for two\n'
        '  reasons at once: **योगविभाग उत्तरार्थो यथासंख्यार्थश्च**. **तापसः,\n'
        '  साहस्रः**. **अण्प्रकरणे ज्योत्स्नादिभ्य उपसंख्यानम्** — and a\n'
        '  vārttika adds a list: ज्योत्स्ना विद्यतेऽस्मिन् पक्षे **ज्यौत्स्नः\n'
        '  पक्षः**, a fortnight that has moonlight; तामिस्रः, कौण्डलः,\n'
        '  वैसर्पः, वैपादिकः'
    ),
    '5.2.104': (
        'SETTLED — सिकताशर्कराभ्यां च. **सैकतो घटः**, a sandy pot; **शार्करं\n'
        '  मधु**, gritty honey. **अदेश इहोदाहरणम्; देशे तु लुबिलचौ भविष्यतः**\n'
        '  — and the examples are deliberately not PLACES, since a place is\n'
        "  the next rule's business"
    ),
    '5.2.105': (
        'SETTLED — देशे लुबिलचौ च — where the thing meant is a PLACE, the\n'
        '  affix is removed, or इलच् comes, **चकारादण् च, मतुप् च**. **कस्य\n'
        '  पुनरयं लुप्? मतुबादीनाम् अन्यतमस्य, विशेषाभावात्** — and WHICH\n'
        '  affix is removed? Any one of them, there being nothing to choose\n'
        '  between. सिकता अस्मिन् विद्यन्ते **सिकता देशः, सिकतिलः, सैकतः,\n'
        '  सिकतावान्** — four forms. **देश इति किम्?** सैकतो घटः'
    ),
    '5.2.106': (
        'SETTLED — दन्त उन्नत उरच्. **उन्नत इति प्रकृतिविशेषणम्** —\n'
        '  *prominent* describes the teeth and not the man. दन्ता उन्नता अस्य\n'
        '  सन्ति **दन्तुरः**, buck-toothed. **उन्नत इति किम्?** दन्तवान्'
    ),
    '5.2.107': (
        'SETTLED — ऊषसुषिमुष्कमधो रः. **ऊषरं क्षेत्रम्**, saline ground;\n'
        '  **सुषिरं काष्ठम्**, hollow wood; मुष्करः पशुः; **मधुरो गुडः**.\n'
        "  **इतिकरणो विवक्षार्थः सर्वत्राभिधेयनियमं करोति** — 5.2.94's इति\n"
        '  confines what may be NAMED, throughout: **इह न भवति — ऊषोऽस्मिन्\n'
        '  घटे विद्यते**, of salt in a pot rather than in the soil.\n'
        '  **रप्रकरणे खमुखकुञ्जेभ्य उपसंख्यानम्** — खमस्यास्ति कण्ठविवरं महत्\n'
        '  **खरः**; **मुखरः**; कुञ्जावस्य स्तः **कुञ्जरः**, an elephant,\n'
        '  **हस्तिहनू कुञ्जशब्देन उच्येते**, कुञ्ज being its jaws.\n'
        '  **नगपांसुपाण्डुभ्यश्चेति वक्तव्यम्** — **नगरम्**, पांसुरम्,\n'
        '  पाण्डुरम्; **कच्छ्वा ह्रस्वत्वं च** — कच्छुरम्'
    ),
    '5.2.108': (
        'SETTLED — द्युद्रुभ्यां मः. **द्युमः, द्रुमः**. **रूढिशब्दावेतौ;\n'
        '  रूढिषु मतुप् पुनर्न विकल्प्यते** — these are settled names, and\n'
        '  where a word is a settled name the मतुप् is not offered beside it.\n'
        '  So the gathering that runs through the rest of the stretch stops\n'
        '  here'
    ),
    '5.2.109': (
        'SETTLED — केशाद् वोऽन्यतरस्याम्. **ननु च प्रकृतम् अन्यतरस्यांग्रहणम्\n'
        '  अनुवर्तत एव?** The word was already running — why say it?\n'
        '  **मतुप्समुच्चयार्थं तदित्युक्तम्; अनेन त्विनिठनौ प्राप्येते; ततश्च\n'
        '  आतूरूप्यं भवति**: the carried one gathers मतुप्, and THIS one lets\n'
        '  इनि and ठन् in, so four forms stand — **केशवः, केशी, केशिकः,\n'
        '  केशवान्**. **वप्रकरणेऽन्येभ्योऽपि दृश्यत इति वक्तव्यम्** — मणिवः,\n'
        '  हिरण्यवः, **राजीवम्**; **अर्णसो लोपश्च**, अर्णवः. **छन्दसीवनिपौ च\n'
        '  वक्तव्यौ**: सु॒म॒ङ्ग॒**लीरि॒यं** व॒धूः (ऋ० १०.८५.३३), and वनिप् —\n'
        '  म॒**घवा॑नम्**ईमहे. **मेधारथाभ्यामिरन्निरचौ वक्तव्यौ** —\n'
        '  **मेधि॑रः**, र॑थि॒रः'
    ),
    '5.2.110': (
        'SETTLED — गाण्ड्यजगात् संज्ञायाम्. **गाण्डीवं धनुः**, **अजगवं धनुः**\n'
        '  — the two great bows. **ह्रस्वादपि भवति — गाण्डिवं धनुरिति; तत्र\n'
        '  तुल्या हि संहिता दीर्घह्रस्वयोः; उभयथा च सूत्रं प्रणीतम्** — the\n'
        '  short form is admitted too, because in continuous recitation the\n'
        '  long and the short of that vowel are indistinguishable, and the\n'
        '  sūtra was framed to be read either way. A rule deliberately left\n'
        '  ambiguous because the ambiguity is in the sound'
    ),
    '5.2.111': (
        'SETTLED — काण्डाण्डादीरन्नीरचौ, **यथासंख्यम्**; the काण्ड member.\n'
        '  **काण्डीरः**\n'
        '\n'
        'SETTLED — काण्डाण्डादीरन्नीरचौ, the अण्ड member. **अण्डीरः**'
    ),
    '5.2.112': (
        'SETTLED — रजःकृष्यासुतिपरिषदो वलच्. **रजस्वला स्त्री**; **कृषीवलः\n'
        '  कुटुम्बी**, a householder who ploughs; आसुतीवलः शौण्डिकः;\n'
        '  **परिषद्वलो राजा**, a king with a council. 6.3.118 वले gives the\n'
        '  lengthening. **इतिकरणो विषयनियमार्थः सर्वत्र संबध्यते; तेनेह न\n'
        '  भवति — रजोऽस्मिन् ग्रामे विद्यते** — the इति of 5.2.94 again,\n'
        '  confining what may be named. **वलच्प्रकरणेऽन्येभ्योऽपि दृश्यते** —\n'
        '  भ्रातृवलः, पुत्रवलः, उत्साहवलः'
    ),
    '5.2.113': (
        'SETTLED — दन्तशिखात् संज्ञायाम्. **दन्तावलो गजः**, an elephant,\n'
        '  named from its tusks; **शिखावलं नगरम्**, शिखावला स्थूणा'
    ),
    '5.2.114': (
        'SETTLED —\n'
        '  ज्योत्स्नातमिस्राशृङ्गिणोर्जस्विन्नूर्जस्वलगोमिन्मलिनमलीमसाः —\n'
        '  eight forms laid down, each with its own irregularity spelled out.\n'
        '  **ज्योतिष उपधालोपो नश्च प्रत्ययो निपात्यते** — **ज्योत्स्ना\n'
        '  चन्द्रप्रभा**, moonlight. **तमस उपधाया इकारो रश्च** — **तमिस्रा\n'
        '  रात्रिः**, and **स्त्रीत्वमतन्त्रम्; अन्यत्रापि दृश्यते — तमिस्रं\n'
        '  नभः**, the feminine is not binding. **शृङ्गादिनच् प्रत्ययो\n'
        '  निपात्यते** — **शृङ्गिणः**. **ऊर्जोऽसुगागमो निपात्यते विनिवलचौ\n'
        '  प्रत्ययौ** — **ऊर्जस्वी, ऊर्जस्वलः**. **गोर्मिनिप्रत्ययो\n'
        '  निपात्यते** — **गोमी**. **मलशब्दाद् इनजीमसचौ प्रत्ययौ निपात्येते**\n'
        '  — **मलिनः, मलीमसः**'
    ),
    '5.2.115': (
        'SETTLED — अत इनिठनौ — from any stem in short अ. **दण्डी, दण्डिकः**,\n'
        '  and **अन्यतरस्यामित्यधिकाराद् मतुबपि भवति**, दण्डवान्. **तपरकरणं\n'
        '  किम्?** श्रद्धावान् — the त marks the vowel SHORT. **AND A VERSE\n'
        '  NAMES FOUR PLACES WHERE THE TWO DO NOT COME.** एकाक्षरात् कृतो\n'
        '  जातेः सप्तम्यां च न तौ स्मृतौ ॥ From a ONE-SYLLABLE word —\n'
        '  **स्ववान्, खवान्**; from a कृत् formation — **कारकवान्**; from a\n'
        '  word for a KIND — **व्याघ्रवान्, सिंहवान्**; and in the LOCATIVE\n'
        '  sense — दण्डा अस्यां सन्ति **दण्डवती शाला**. **इतिकरणो\n'
        '  विषयनियमार्थः सर्वत्र संबध्यते; तेन क्वचिद् भवत्यपि** — and the\n'
        '  restriction is not absolute: **कार्यी, हार्यी, तण्डुली,\n'
        '  तण्डुलिकः**'
    ),
    '5.2.116': (
        'SETTLED — व्रीह्यादिभ्यश्च. **मतुब् भवत्येव**: **व्रीही, व्रीहिकः,\n'
        '  व्रीहिमान्**; मायी, मायिकः, मायावान्. **AND THE LIST IS NOT\n'
        '  UNIFORM.** **न च व्रीह्यादिभ्यः सर्वेभ्यः प्रत्ययद्वयमिष्यते** —\n'
        '  **शिखादिभ्य इनिर्वाच्य इकन् यवखदादिषु; परिशिष्टेभ्य उभयम्**: शिखा,\n'
        '  मेखला, संज्ञा, बलाका, माला, वीणा, वडवा, अष्टका, पताका, कर्मन्,\n'
        '  चर्मन्, हंसा take इनि only; यवखद, कुमारी, नौ take इकन् only; the\n'
        '  rest take both. **व्रीहिग्रहणं किमर्थम्, यावता तुन्दादिषु\n'
        '  व्रीहिशब्दः पठ्यते?** And why name व्रीहि when it is already in\n'
        '  another list? **एवं तर्हि तुन्दादिषु व्रीहिग्रहणम् अर्थग्रहणं\n'
        '  विज्ञायते** — there the word is taken for its MEANING, so that\n'
        '  शालि too is reached: **शालिलः, शाली, शालिकः, शालिमान्**.\n'
        '  **शीर्षाद् नञः** (ग०सू०१३५) — अशीर्षी, अशीर्षिकः'
    ),
    '5.2.117': (
        'SETTLED — तुन्दादिभ्य इलच् च — **चकाराद् इनिठनौ मतुप् च**, four\n'
        '  affixes at once. **तुन्दिलः, तुन्दी, तुन्दिकः, तुन्दवान्**;\n'
        '  उदरिलः, उदरी, उदरिकः, उदरवान्. तुन्द, उदर, पिचण्ड, घट, यव, व्रीहि,\n'
        '  **स्वाङ्गाद् विवृद्धौ च** (ग०सू०१३६) — तुन्दादिः, and the last\n'
        '  entry takes any part of the body when it is OVERGROWN'
    ),
    '5.2.118': (
        'SETTLED — एकगोपूर्वाट् ठञ् नित्यम्. एकशतमस्यास्तीति **ऐकशतिकः**;\n'
        '  ऐकसहस्रिकः; **गौशतिकः**, गौसहस्रिकः. **अत इत्येव** — the short अ\n'
        '  of 5.2.115 carries, so **एकविंशतिरस्यास्तीति न भवति**.\n'
        '  **कथमैकगविकः? समासान्ते कृते भविष्यति** — that form comes once the\n'
        '  compound-final has been added. **कथं गौशकटिकः? शकटीशब्देन\n'
        '  समानार्थः शकटशब्दोऽस्ति** — and that one from a synonym in अ.\n'
        "  **अवश्यं चात इत्यनुवर्त्यम्** for 5.2.128's sake. **नित्यग्रहणं\n"
        '  मतुपो बाधनार्थम्** — the *always* is there to keep the gathered\n'
        '  मतुप् out'
    ),
    '5.2.119': (
        'SETTLED — शतसहस्रान्ताच्च निष्कात् — from a stem ending in *hundred*\n'
        '  or *thousand*, those words standing after निष्क. निष्कशतमस्यास्ति\n'
        '  **नैष्कशतिकः**; नैष्कसहस्रिकः. **सुवर्णनिष्कशतमस्तीत्यनभिधानाद् न\n'
        '  भवति** — and with another word in front the language does not say\n'
        '  it'
    ),
    '5.2.120': (
        'SETTLED — रूपादाहतप्रशंसयोर्यप्. **निघातिकाताडनादिना दीनारादिषु रूपं\n'
        '  यदुत्पद्यते तदाहतम् उच्यते** — a stamp struck on a coin. आहतं\n'
        '  रूपमस्य **रूप्यो दीनारः**, a struck dinar; and in praise, प्रशस्तं\n'
        '  रूपमस्यास्ति **रूप्यः पुरुषः**, a handsome man. **आहतप्रशंसयोरिति\n'
        '  किम्?** रूपवान्. **यप्प्रकरणेऽन्येभ्योऽपि दृश्यते** — **हिम्याः\n'
        '  पर्वताः**, गुण्या ब्राह्मणाः'
    ),
    '5.2.121': (
        'SETTLED — असो मायामेधास्रजो विनिः; the अस्-final half. **मतुप्\n'
        '  सर्वत्र समुच्चीयत एव**. **यशस्वी, तपस्वी, पयस्वी**\n'
        '\n'
        'SETTLED — असो मायामेधास्रजो विनिः, the three named words. **मायावी,\n'
        '  मेधावी, स्रग्वी**. **मायाशब्दाद् व्रीह्यादिषु पाठाद् इनिठनावपि\n'
        "  भवतः** — and माया is in 5.2.116's list as well, so मायी and मायिकः\n"
        '  stand beside them'
    ),
    '5.2.122': (
        'SETTLED — बहुलं छन्दसि — and बहुलम् is doing a great deal of work.\n'
        '  अग्ने॑ **तेजस्विन्**; **न भवति, सूर्यो वर्चस्वान्**. Eight\n'
        '  vārttikas hang on that one word. **अष्ट्रामेखलाद्वयोभयरुजाहृदयानां\n'
        '  दीर्घत्वं च** — अष्ट्॒**रावी**, मेखलावी, उभया॒**वी**; **मर्मणश्च**\n'
        '  — मर्मावी; **सर्वत्रामयस्योपसंख्यानम्, छन्दसि भाषायां च** —\n'
        '  आमया॒**वी**, in the Veda and in speech alike;\n'
        '  **शृङ्गवृन्दाभ्यामारकन्** — **शृङ्गारकः**, वृ॒न्दारकः;\n'
        '  **फलबर्हाभ्यामिनज्** — फलिनः, बर्हिणः; **हृदयाच्चालुरन्यतरस्याम्**\n'
        '  — हृदयालुः, हृदयी, हृदयिकः, हृदयवान्; **शीतोष्णतृप्रेभ्यस्तद् न\n'
        '  सहत इत्यालुज्** — **शीतालुः**, one who cannot BEAR the cold, and\n'
        '  **हिमाच्चेलुः**, हिमेलुः, **बलादूलच्**, बलूलः, **वातात् समूहे च**\n'
        '  — वातूलः; **पर्वमरुद्भ्यां तन्** — प॑र्व॒तः, मरुत्तः; **अर्थात्\n'
        '  तदभाव इनिः** — **अर्थी**, one who LACKS it, against अर्थवान् who\n'
        '  has it. **तदेतत् सर्वं बहुलग्रहणेन सम्पद्यते**'
    ),
    '5.2.123': (
        'SETTLED — ऊर्णाया युस्. **सकारः पदसंज्ञार्थः** — the स is there to\n'
        '  make the result a पद. ऊर्णास्य विद्यते ऊ॒र्णा॒**युः**.\n'
        '  **केचिच्छन्दोग्रहणमनुवर्तयन्ति** — and some carry the\n'
        '  Veda-restriction down to it'
    ),
    '5.2.124': (
        'SETTLED — वाचो ग्मिनिः. **वाग्ग्मी**, वाग्ग्मिनौ, वाग्ग्मिनः —\n'
        '  eloquent'
    ),
    '5.2.125': (
        'SETTLED — आलजाटचौ बहुभाषिणि, **ग्मिनेरपवादः**. **वाचालः, वाचाटः**.\n'
        '  **कुत्सित इति वक्तव्यम्; यो हि सम्यग् बहु भाषते, वाग्ग्मीत्येव स\n'
        '  भवति** — and a vārttika adds that it must be BLAMEWORTHY talking,\n'
        '  since a man who talks much and well is वाग्ग्मी by the rule\n'
        '  before. The two rules divide the fluent from the garrulous'
    ),
    '5.2.126': (
        'SETTLED — स्वामिन्नैश्वर्ये — **स्वामिन्निति निपात्यते**.\n'
        '  **स्वशब्दाद् ऐश्वर्यवाचिनो मत्वर्थ आमिन् प्रत्ययो निपात्यते**:\n'
        '  स्वमस्यास्तीति, ऐश्वर्यमस्यास्तीति **स्वामी**. **ऐश्वर्य इति\n'
        '  किम्?** स्ववान् — a man with property and no lordship'
    ),
    '5.2.127': (
        'SETTLED — अर्शआदिभ्योऽच्. अर्शांसि अस्य विद्यन्ते **अर्शसः**; उरसः.\n'
        '  **आकृतिगणश्चायम्; यत्राभिन्नरूपेण शब्देन तद्वतो ऽभिधानं तत्\n'
        '  सर्वमिह द्रष्टव्यम्** — an open list, and the definition of it is\n'
        '  the shape of the result: wherever a word UNCHANGED IN FORM names\n'
        '  the thing that has it, the base belongs here. A gaṇa defined by\n'
        '  what its members do rather than by membership. अर्शस्, उरस्,\n'
        '  तुन्द, चतुर, पलित, जटा, घटा, अभ्र, कर्दम, आम, लवण, **स्वाङ्गाद्\n'
        '  हीनात्** (ग०सू०१३७), **वर्णात्** (ग०सू०१३८) — अर्शआदिः'
    ),
    '5.2.128': (
        'SETTLED — द्वन्द्वोपतापगर्ह्यात् प्राणिस्थादिनिः — three kinds of\n'
        '  base, all naming something ON a living body. **द्वन्द्वः समासः;\n'
        '  उपतापो रोगः; गर्ह्यं निन्द्यम्**. द्वन्द्वात् — **कटकवलयिनी**,\n'
        '  शङ्खनूपुरिणी; उपतापात् — **कुष्ठी**, किलासी; गर्ह्यात् —\n'
        '  **ककुदावर्ती**, काकतालुकी. **प्राणिस्थादिति किम्?** पुष्पफलवान्\n'
        '  वृक्षः. **प्राण्यङ्गाद् नेष्यते** — and NOT a limb, पाणिपादवती.\n'
        '  **अत इत्यनुवर्तते; तेनेह न भवति — चित्रललाटिकावती**. **सिद्धे\n'
        '  प्रत्यये पुनर्वचनं ठनादिबाधनार्थम्** — the affix was coming\n'
        '  anyway, and the rule is stated to shut ठन् and the rest out'
    ),
    '5.2.129': (
        'SETTLED — वातातिसाराभ्यां कुक् च. **वातातिसारयोर् उपतापत्वात्\n'
        '  पूर्वेणैव सिद्धे प्रत्यये कुगर्थमेवेदं वचनम्** — both are\n'
        '  diseases, so 5.2.128 gave the affix already; this rule is for the\n'
        '  कुक् alone. **वातकी, अतिसारकी**. **पिशाचाच्चेति वक्तव्यम्** —\n'
        '  **पिशाचकी वैश्रवणः**, and **रोगे चायमिष्यते; इह न भवति — वातवती\n'
        '  गुहा**'
    ),
    '5.2.130': (
        'SETTLED — वयसि पूरणात् — from a word made by an ORDINAL affix, when\n'
        '  an AGE is meant. पञ्चमोऽस्यास्ति मासः संवत्सरो वा **पञ्चमी\n'
        '  उष्ट्रः**, a camel in its fifth year; नवमी, दशमी. **सिद्धे सति\n'
        '  नियमार्थं वचनम् — इनिरेव भवति, ठन् न भवतीति** — the affix was\n'
        '  coming; the rule is a restriction, and shuts ठन् out. **वयसीति\n'
        '  किम्?** पञ्चमवान् ग्रामरागः'
    ),
    '5.2.131': (
        'SETTLED — सुखादिभ्यश्च — and again a restriction rather than a\n'
        '  giving, **इनिः प्रत्ययो नियम्यते**. **सुखी, दुःखी**. सुख, दुःख,\n'
        '  तृप्र, कृच्छ्र, आम्र, अलीक, करुणा, कृपण, सोढ, शील, हल, **माला\n'
        '  क्षेपे** (ग०सू०१३९), प्रणय — सुखादिः. **माला क्षेप इति पठ्यते,\n'
        '  व्रीह्यादिषु च मालाशब्दोऽस्ति, तदिह क्षेपे मतुब्बाधनार्थं वचनम्**\n'
        "  — माला is in 5.2.116's list too, and its entry here with *in\n"
        '  contempt* is to keep मतुप् out in that sense alone'
    ),
    '5.2.132': (
        'SETTLED — धर्मशीलवर्णान्ताच्च. **अन्तशब्दः प्रत्येकम् अभिसंबध्यते**\n'
        '  — *ending in* goes with each of the three severally. ब्राह्मणानां\n'
        '  धर्मो ब्राह्मणधर्मः, सोऽस्यास्तीति **ब्राह्मणधर्मी**;\n'
        '  ब्राह्मणशीली, ब्राह्मणवर्णी'
    ),
    '5.2.133': (
        'SETTLED — हस्ताज् जातौ — and only where the WHOLE WORD names a kind,\n'
        '  **समुदायेन चेज् जातिरभिधीयते**. हस्तोऽस्यास्तीति **हस्ती**, an\n'
        '  elephant. **जाताविति किम्?** हस्तवान् पुरुषः — a man with hands is\n'
        '  not a kind of thing'
    ),
    '5.2.134': (
        'SETTLED — वर्णाद् ब्रह्मचारिणि — where the whole word names a\n'
        '  STUDENT. **ब्रह्मचारीति त्रैवर्णिकोऽभिप्रेतः; स हि\n'
        '  विद्याग्रहणार्थमुपनीतो ब्रह्म चरति, नियमम् आसेवत इत्यर्थः** — one\n'
        '  of the three classes, initiated for learning, who *walks in the\n'
        '  sacred word*, that is, keeps the observances. **वर्णी**.\n'
        '  **ब्रह्मचारिणीति किम्?** वर्णवान्'
    ),
    '5.2.135': (
        'SETTLED — पुष्करादिभ्यो देशे — where the whole word names a PLACE.\n'
        '  **पुष्करिणी**, a lotus-pond; पद्मिनी. **देश इति किम्?** पुष्करवान्\n'
        '  हस्ती. **इनिप्रकरणे बलाद् बाहूरुपूर्वाद् उपसंख्यानम्** — बाहुबली,\n'
        '  ऊरुबली; **सर्वादेश्च** — सर्वधनी, **सर्वकेशी नटः**;\n'
        '  **अर्थाच्चासन्निहिते** — **अर्थी**, and **असन्निहित इति किम्?**\n'
        '  अर्थवान्; **तदन्ताच्च** — धान्यार्थी, हिरण्यार्थी. पुष्कर, पद्म,\n'
        '  उत्पल, तमाल, कुमुद, नड, कपित्थ, बिस, मृणाल, कर्दम, शालूक, करीष,\n'
        '  शिरीष, यवास, हिरण्य — पुष्करादिः'
    ),
    '5.2.136': (
        'SETTLED — बलादिभ्यो मतुबन्यतरस्याम् — and here मतुप् is given\n'
        '  OUTRIGHT where everywhere else it was gathered in by the carried\n'
        '  अन्यतरस्याम्. **अन्यतरस्यांग्रहणेन प्रकृत इनिः समुच्चीयते** — the\n'
        '  word now gathers the इनि instead, and the two affixes have changed\n'
        '  places. **बलवान्, बली**; उत्साहवान्, उत्साही. बल, उत्साह, उद्भाव,\n'
        '  उद्वास, शिखा, पूग, मूल, दंश, कुल, आयाम, व्यायाम, आरोह, अवरोह,\n'
        '  परिणाह, युद्ध — बलादिः'
    ),
    '5.2.137': (
        'SETTLED — संज्ञायां मन्माभ्याम् — from a stem ending in मन् or in\n'
        '  the sound म, where the whole word is a NAME. **प्रथिमिनी,\n'
        '  दामिनी**; and from the म-final, **होमिनी, सोमिनी**. **संज्ञायामिति\n'
        '  किम्?** सोमवान्, होमवान्'
    ),
    '5.2.138': (
        'SETTLED — कंशंभ्यां बभयुस्तितुतयसः — SEVEN affixes for two words in\n'
        '  one rule, the most of any sūtra in the pāda. **कम् शम् इति\n'
        '  मकारान्तावुदकसुखयोर्वाचकौ** — कम् is water and शम् is ease.\n'
        '  **कम्बः, शम्बः; कम्भः, शम्भः; कंयुः, शंयुः; कन्तिः, शन्तिः;\n'
        '  कन्तुः, शन्तुः; कन्तः, शन्तः; कंयः, शंयः**. **सकारः पदसंज्ञार्थः,\n'
        '  तेनानुस्वारपरसवर्णौ सिद्धौ भवतः; संज्ञायां हि असत्यां कम्यः शम्य\n'
        '  इति स्यात्** — the स in युस् makes the result a पद, and without\n'
        '  that the nasal would not become अनुस्वार and the forms would come\n'
        '  out कम्यः, शम्यः'
    ),
    '5.2.139': (
        'SETTLED — तुन्दिबलिवटेर्भः. **तुन्दिरिति वृद्धा नाभिर् उच्यते** — a\n'
        '  swollen navel. **तुन्दिभः**; बलिभः, वटिभः. **बलिशब्दः पामादिषु\n'
        '  पठ्यते, तेन बलिन इत्यपि भवति** — and बलि is in the पामादि list of\n'
        '  5.2.100 as well, so बलिनः stands too'
    ),
    '5.2.140': (
        'SETTLED — अहंशुभमोर्युस् — and the pāda ends. **अहमिति\n'
        '  शब्दान्तरमहंकारे वर्तते** — the अहम् here is a different word from\n'
        '  the pronoun and means SELF-REGARD; **शुभमित्यव्ययं शुभपर्यायः**.\n'
        '  **सकारः पदसंज्ञार्थः**. **अहंयुः**, **अहंकारवानित्यर्थः**;\n'
        '  **शुभंयुः**, **कल्याणवानित्यर्थः**. इति श्रीजयादित्यविरचितायां\n'
        '  काशिकायां वृत्तौ पञ्चमाध्यायस्य द्वितीयः पादः'
    ),
}

_WHAT_COMES_LINE = (
    'what_comes(stem, gana=..., sense=..., case=..., result=..., '
    'samjna=..., uttarapada=..., pre=..., usage=..., wants=...) -> '
    'which affix comes for that base in that sense.'
)

#: Nothing declared. Every rule of this pāda is answered by the one
#: resolver, so a declaration would name the function it already is —
#: which the reuse walk rejects, and rightly.
_REUSES = {}

for _sutra, _notes in _RULES.items():
    register(
        _sutra,
        apply=what_comes,
        codification=_WHAT_COMES_LINE,
        notes=_notes,
        reuses=_REUSES.get(_sutra, ()),
    )
