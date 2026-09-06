# -*- coding: utf-8 -*-
"""
अध्याय ४, पाद २ — a case-relation and a sense, and the affix
understood.

4.1 spent 178 sūtras on one sense and named the affix in nearly every
rule. This pāda changes the shape: each rule states a CASE-RELATION
and a SENSE, and lets 4.1.83's default supply the affix unless it has
reason to speak. That is what 4.1.82 समर्थानां प्रथमाद्वा was for —
it said the affix attaches to the first of the syntactically connected
words, and these rules say which connection, in which case, and in
what sense.
"""

from __future__ import annotations

from src.astadhyayi.sense_taddhita import case_run, in_sense
from src.astadhyayi.sources import register

_RULES = {
    '4.2.1': (
        'SETTLED — तेन रक्तं रागात्. शुक्लस्य वर्णान्तरापादनम् इह\n'
        '  रञ्जेरर्थः, रज्यतेऽनेनेति रागः. कषायेण रक्तं वस्त्रं काषायम्;\n'
        '  माञ्जिष्ठम्, कौसुम्भम्. रागादिति किम्? देवदत्तेन रक्तं\n'
        '  वस्त्रम् — the base must name a DYE and not the dyer.\n'
        '\n'
        'SETTLED — A NEW SHAPE OF RULE. 4.1 spent 178 sūtras on one\n'
        '  sense and named the affix in nearly every rule. From here each\n'
        '  rule states **a case-relation and a sense** and leaves the\n'
        "  affix to 4.1.83's default unless it has reason to speak. That\n"
        '  is what 4.1.82 समर्थानां प्रथमाद्वा was for: it said the affix\n'
        '  attaches to the FIRST of the connected words, and these rules\n'
        '  say which connection, in which case, and in what sense.\n'
        '\n'
        'SETTLED — and the vṛtti names where the case stops:\n'
        '  **द्वैपवैयाघ्रादञ् इति यावत् तृतीयासमर्थविभक्तिरनुवर्तते** —\n'
        '  the instrumental runs to 4.2.12. Both ends of the range are\n'
        '  stated, which is not true of most anuvṛtti.\n'
        '\n'
        'NOTE — कथं काषायौ गर्दभस्य कर्णौ? **उपमानाद् भविष्यति**,\n'
        "  काषायाविव काषायौ. An ass's ears are not dyed, and the form\n"
        '  stands by likeness — the instrument 4.1.103 and 4.1.105 used\n'
        '  for three famous names.'
    ),
    '4.2.2': (
        'SETTLED — लाक्षारोचनाशकलकर्दमाट् ठक्, अणोऽपवादः. लाक्षिकम्,\n'
        '  रौचनिकम्, शाकलिकम्, कार्दमिकम्; and शकलकर्दमाभ्यामणपीष्यते —\n'
        '  शाकलम्, कार्दमम्.\n'
        '\n'
        'NOTE — four vārttikas give four more dyes four more affixes:\n'
        '  नील्या अन् (नीलं वस्त्रम्), पीतात् कन् (पीतकम्),\n'
        '  हरिद्रामहारजनाभ्यामञ् (हारिद्रम्, माहारजनम्). A different\n'
        '  affix for each colour, and none of them is in the sūtra.'
    ),
    '4.2.3': (
        'SETTLED — नक्षत्रेण युक्तः कालः. पौषी रात्रिः, पौषमहः; माघी\n'
        '  रात्रिः. नक्षत्रेणेति किम्? चन्द्रमसा युक्ता रात्रिः. काल\n'
        '  इति किम्? पुष्येण युक्तश्चन्द्रमाः.\n'
        '\n'
        'SETTLED — AND THE VṚTTI HAS TO EXPLAIN HOW A TIME CAN BE JOINED\n'
        '  WITH A STAR AT ALL. कथं पुनर्नक्षत्रेण पुष्यादिना कालो\n'
        '  युज्यते? **पुष्यादिसमीपस्थे चन्द्रमसि वर्तमानाः\n'
        '  पुष्यादिशब्दाः प्रत्ययमुत्पादयन्ति** — the star-names are\n'
        '  used of the MOON standing near those stars, and it is the moon\n'
        '  the time is joined with. A grammatical rule that cannot be\n'
        '  applied without an astronomical gloss, and the vṛtti supplies\n'
        '  it rather than leaving the rule unusable.'
    ),
    '4.2.4': (
        'SETTLED — लुबविशेषे. Where no PARTICULAR part of the\n'
        '  day-and-night is meant, the affix is dropped: अद्य पुष्यः,\n'
        '  अद्य कृत्तिकाः. यावान् कालो नक्षत्रेण युज्यतेऽहोरात्रः,\n'
        '  तस्याविशेषे लुब् भवति. अविशेष इति किम्? पौषी रात्रिः.\n'
        '\n'
        'NOTE — one word separates this rule from the one before it. The\n'
        '  same base, the same case, the same sense — and one gives an\n'
        '  affix while the other takes it away. The elision is what lets\n'
        '  a star-name serve as the name of a day.'
    ),
    '4.2.5': (
        'SETTLED — संज्ञायां श्रवणाश्वत्थाभ्याम्. अविशेषे लुब् विहितः\n'
        '  पूर्वेण, **विशेषार्थोऽयमारम्भः** — begun for the particular\n'
        '  case the rule before excluded: श्रवणा रात्रिः, अश्वत्थो\n'
        '  मुहूर्तः. संज्ञायामिति किम्? श्रावणी, आश्वत्थी रात्रिः.\n'
        '\n'
        'SETTLED — लुपि युक्तवद्भावः कस्माद् न भवति? **निपातनात्**\n'
        '  विभाषा फाल्गुनीश्रवणाकार्तिकी इति. The gender and number of\n'
        "  an elided affix's base normally carry over, and here they do\n"
        '  not — and the evidence is a form fixed EIGHTEEN SŪTRAS AHEAD.\n'
        "  A rule's behaviour read off a later rule's example."
    ),
    '4.2.6': (
        'SETTLED — द्वन्द्वाच्छः. From a DVANDVA of star-names, and\n'
        '  विशेषे चाविशेषे च — in both cases: राधानुराधीया रात्रिः, and\n'
        '  अद्य राधानुराधीयम्.\n'
        '\n'
        'NOTE — **लुपं परत्वाद् बाधते**, it beats the elision by being\n'
        '  later. परत्व settling a conflict in one word, where 3.4.37\n'
        '  needed पूर्वविप्रतिषेध to settle one in reverse.'
    ),
    '4.2.7': (
        'SETTLED — तेन दृष्टम्. क्रुञ्चेन दृष्टं क्रौञ्चं साम;\n'
        '  वासिष्ठम्, वैश्वामित्रम्. The sense is a CHANT SEEN by a\n'
        '  seer, which is how the tradition speaks of composition — and\n'
        '  the rule takes it as a plain instrumental relation.'
    ),
    '4.2.8': (
        'SETTLED — कलेर्ढक्, अणोऽपवादः. कालेयम्.\n'
        '\n'
        'SETTLED — THE DENSEST VĀRTTIKA-SET SINCE 4.1.85, AND IT ENDS IN\n'
        '  A VERSE. सर्वत्राग्निकलिभ्यां ढग् वक्तव्यः — आग्नेयम्, and\n'
        '  एवमग्नौ भवम्, अग्नेरागतम्, अग्नेः स्वम् इति **सर्वत्र ढगेव\n'
        '  भवति**: one affix for one word in EVERY sense, which is a rule\n'
        '  about a word rather than about a sense. दृष्टे सामनि अण् वा\n'
        '  डिद् भवति — औशनसम्, औशनम्. तीयादीकक् स्वार्थे वा —\n'
        '  द्वैतीयीकम्, but **न विद्यायाः**, not of a branch of learning.\n'
        '  गोत्रादङ्कवदिष्यते — औपगवकम्.\n'
        '\n'
        '  दृष्टे सामनि जाते च द्विरण् डिद् वा विधीयते / तीयादीकक् न\n'
        '  विद्याया गोत्रादङ्कवदिष्यते — five vārttikas gathered into one\n'
        '  verse, which is how the tradition remembers a set.'
    ),
    '4.2.9': (
        'SETTLED — वामदेवाड् ड्यड्ड्यौ, अणोऽपवादः. वामदेव्यं साम.\n'
        '  तित्करणं स्वरार्थम्.\n'
        '\n'
        'SETTLED — AND THE ड् IS THERE TO KEEP THE AFFIX OUT OF A RULE\n'
        '  FOUR CHAPTERS AWAY. डित्करणं किमर्थम्? ययतोश्चातदर्थे इति नञ\n'
        '  उत्तरस्यान्तोदात्तत्वे विधीयमाने **अनयोर्ग्रहणं मा भूत्** —\n'
        '  6.2.156 names य and यत्, and without the ड् these two would\n'
        '  be caught by it, giving अवामदेव्यम् the wrong accent. The\n'
        '  exclusion runs through two paribhāṣās: a name with no mark,\n'
        '  or with one, does not reach an affix with two.\n'
        '\n'
        '  And a verse states the whole argument: सिद्धे यस्येतिलोपेन\n'
        '  किमर्थं ययतौ डितौ / ग्रहणं मातदर्थे भूद् वामदेव्यस्य नञ्स्वरे.'
    ),
    '4.2.10': (
        'SETTLED — तेन परिवृतो रथः. वस्त्रेण परिवृतो रथो वास्त्रो रथः;\n'
        '  काम्बलः, चार्मणः. रथ इति किम्? वस्त्रेण परिवृतः कायः.\n'
        '\n'
        'SETTLED — and परिवृत is defined tightly. समन्ताद् वेष्टितः\n'
        '  परिवृत उच्यते, **यस्य न कश्चिदवयवो वस्त्रादिभिरवेष्टितः** —\n'
        '  wrapped on every side, with no part left uncovered. तेनेह न\n'
        '  भवति — छात्रैः परिवृतो रथः: a chariot surrounded by students\n'
        '  is not wrapped in them.'
    ),
    '4.2.11': (
        'SETTLED — पाण्डुकम्बलादिनिः, अणोऽपवादः. पाण्डुकम्बली.\n'
        '  पाण्डुकम्बलशब्दो राजास्तरणस्य वर्णकम्बलस्य वाचकः.\n'
        '\n'
        'SETTLED — **मत्वर्थीयेनैव सिद्धे वचनमणो निवृत्त्यर्थम्**: the\n'
        '  affix was available anyway as a possessive, so the rule exists\n'
        '  only to keep the DEFAULT out. A rule stated for what it\n'
        '  prevents rather than for what it gives — 4.1.84 was the same,\n'
        '  and there the thing prevented had not yet been stated.'
    ),
    '4.2.12': (
        'SETTLED — द्वैपवैयाघ्रादञ्, अणोऽपवादः, **स्वरे विशेषः** — the\n'
        '  two affixes differ only in accent, the fourth such pair since\n'
        '  4.1.25. द्वैपेन परिवृतो रथो द्वैपः; वैयाघ्रः.\n'
        '  द्वीपिव्याघ्रयोर्विकारभूते चर्मणी द्वैपवैयाघ्रे — the bases\n'
        '  are themselves derived, naming the HIDES of those animals.\n'
        '\n'
        "NOTE — and this is the rule 4.2.1's vṛtti named as where the\n"
        '  instrumental stops.'
    ),
    '4.2.13': (
        'SETTLED — कौमारापूर्ववचने. निपात्यते: कौमारः पतिः, a husband\n'
        "  who is a girl's FIRST — पाणिग्रहणस्यापूर्ववचनम्. **उभयतः\n"
        '  स्त्रिया अपूर्वत्वे निपातनमेतत्**, the fixing covers the\n'
        '  firstness on both sides: कौमारी भार्या as well.\n'
        '\n'
        'NOTE — and the vṛtti gives two derivations in a verse rather\n'
        '  than one: कौमारापूर्ववचने कुमार्या अण् विधीयते / **अपूर्वत्वं\n'
        '  यदा तस्याः कुमार्यां भवतीति वा** — either from the girl, or\n'
        '  simply *what happens in girlhood*, कुमार्यां भवः कौमारः पतिः,\n'
        '  तस्य स्त्री कौमारी भार्या. The second needs no निपातन at all,\n'
        '  which is the point of offering it.'
    ),
    '4.2.14': (
        'SETTLED — तत्रोद्धृतममत्रेभ्यः. शरावेषूद्धृतः शाराव ओदनः;\n'
        '  माल्लिकः, कार्परः. **भुक्तोच्छिष्टमुद्धृतमुच्यते**, and अमत्रं\n'
        '  भाजनं पात्रम् — what is taken up means the leavings of a meal,\n'
        '  and the base names a vessel. अमत्रेभ्य इति किम्? पाणावुद्धृत\n'
        '  ओदनः.\n'
        '\n'
        'SETTLED — and the vṛtti names where THIS case stops:\n'
        '  **क्षीराड् ढञ् इति यावत्** — the locative runs to 4.2.20,\n'
        '  exactly as 4.2.1 said of the instrumental. Two case-runs, two\n'
        '  boundaries, and both stated in the rule that opens them.'
    ),
    '4.2.15': (
        'SETTLED — स्थण्डिलाच्छयितरि व्रते. स्थण्डिले शयितुं व्रतमस्य\n'
        '  स्थाण्डिलो भिक्षुः. **व्रतमिति शास्त्रितो नियम उच्यते** — a\n'
        '  restraint laid down by a text.\n'
        '\n'
        '  व्रत इति किम्? स्थण्डिले शेते ब्रह्मदत्तः: sleeping there is\n'
        '  not enough, it has to be a VOW. The affix carries the vow and\n'
        '  nothing else, which is as far as this section goes from a\n'
        '  grammatical condition.'
    ),
    '4.2.16': (
        'SETTLED — संस्कृतं भक्षाः. भ्राष्ट्रे संस्कृता भक्षा भ्राष्ट्रा\n'
        '  अपूपाः; कालशाः, कौम्भाः. भक्षा इति किम्? पुष्पपुटे संस्कृतो\n'
        '  मालागुणः.\n'
        '\n'
        'NOTE — two definitions the sūtra does not give.\n'
        '  **खरविशदमभ्यवहार्यं भक्षम्**, a hard dry thing eaten; and\n'
        '  **सत उत्कर्षाधानं संस्कारः**, preparation is the improving of\n'
        '  what already is.'
    ),
    '4.2.17': (
        'SETTLED — शूलोखाद् यत्, अणोऽपवादः. शूल्यं मांसम्; उख्यम्.'
    ),
    '4.2.18': (
        'SETTLED — दध्नष्ठक्. दाधिकम्.\n'
        '\n'
        'SETTLED — AND THE VṚTTI ASKS WHY THE RULE IS NEEDED, THEN\n'
        '  ANSWERS BY A DISTINCTION IN THE SITUATION RATHER THAN IN THE\n'
        '  GRAMMAR. ननु च संस्कृतार्थे प्राग् वहतेष्ठकं वक्ष्यति, तेनैव\n'
        '  सिद्धम्? — 4.4.1 gives the same affix in the same sense.\n'
        '  न सिध्यति: दध्ना हि तत् संस्कृतं यस्य **दधिकृतमेव\n'
        '  उत्कर्षाधानम्**, इह तु दधि **केवलमाधारभूतम्**, द्रव्यान्तरेण\n'
        '  लवणादिना संस्कारः क्रियते. There the curds do the improving;\n'
        '  here they are only what the thing stands in, and salt does the\n'
        '  work. Two rules, one affix, one sense — and they differ in WHO\n'
        '  IS ACTING.'
    ),
    '4.2.19': (
        'SETTLED — उदश्वितोऽन्यतरस्याम्. औदश्वित्कम्, and पक्षे\n'
        '  यथाप्राप्तमण् — औदश्वितम्.'
    ),
    '4.2.20': (
        'SETTLED — क्षीराड् ढञ्, अणोऽपवादः. क्षीरे संस्कृता क्षैरेयी\n'
        "  यवागूः. The rule 4.2.14's vṛtti named as where the locative\n"
        '  stops.'
    ),
    '4.2.21': (
        'SETTLED — सास्मिन् पौर्णमासीति संज्ञायाम्. पौषी पौर्णमासी\n'
        '  अस्मिन् पौषो मासः, पौषोऽर्धमासः, पौषः संवत्सरः —\n'
        '  मासार्धमाससंवत्सराणामेषा संज्ञा. इह न भवति — पौषी पौर्णमासी\n'
        '  अस्मिन् दशरात्रे.\n'
        '\n'
        'SETTLED — AND THE VṚTTI ASKS WHY TWO WORDS ARE SPENT ON ONE JOB.\n'
        '  इतिकरणस्य संज्ञाशब्दस्य च तुल्यमेव फलं प्रयोगानुसरणम्, तत्र\n'
        '  किमर्थं द्वयमुपादीयते? — both इति and संज्ञायाम् hold the rule\n'
        '  to established usage. **संज्ञाशब्देन तुल्यताम् इतिकरणस्य\n'
        '  ज्ञापयितुम्, न ह्ययं लोके तथा प्रसिद्धः**: the pair is there\n'
        '  to TEACH that इति does that job, since it is not commonly\n'
        '  known to. A word explained by being placed beside one that is\n'
        '  understood — and once taught, संप्रति ज्ञापिते, it can be used\n'
        '  alone wherever the grammar says इतिकरणस्ततश्चेद् विवक्षा.\n'
        '\n'
        'NOTE — अथ पौर्णमासीति कोऽयं शब्दः? Two derivations again:\n'
        '  पूर्णमासादण् (वा० ४.२.३५), or पूर्णो माः पूर्णमाः, **मा इति\n'
        '  चन्द्र उच्यते** — *the moon being full*.'
    ),
    '4.2.22': (
        'SETTLED — आग्रहायण्यश्वत्थाट् ठक्, अणोऽपवादः. आग्रहायणिको मासः,\n'
        '  अर्धमासः, संवत्सरः; आश्वत्थिकः. सास्मिन् पौर्णमासीति\n'
        '  सर्वमनुवर्तते.'
    ),
    '4.2.23': (
        'SETTLED — विभाषा फाल्गुनीश्रवणाकार्तिकीचैत्रीभ्यः. नित्यमणि प्राप्ते\n'
        '  पक्षे ठग् विधीयते: फाल्गुनो मासः beside फाल्गुनिकः,\n'
        '  श्रावणः beside श्रावणिकः.\n'
        '\n'
        "NOTE — this is the rule 4.2.5's vṛtti reached FORWARD to,\n"
        "  eighteen sūtras earlier, to settle how an elided affix's\n"
        '  base behaves: निपातनात्, from a form fixed here.'
    ),
    '4.2.24': (
        'SETTLED — सास्य देवता. ऐन्द्रं हविः; आदित्यम्, बार्हस्पत्यम्,\n'
        '  प्राजापत्यम्. **यागसंप्रदानं देवता, देयस्य पुरोडाशादेः\n'
        '  स्वामिनी** — a deity is what a sacrifice is given TO, the\n'
        '  owner of the cake offered, and the affix goes on the\n'
        '  OFFERING. देवतेति किम्? कन्या देवदत्तस्य.\n'
        '\n'
        'NOTE — two attested forms accounted for, neither licensed:\n'
        '  कथमैन्द्रो मन्त्रः? **मन्त्रस्तुत्यमपि देवतेत्युपचरन्ति**;\n'
        '  कथमाग्नेयो वै ब्राह्मणो देवतया? उपमानाद् भविष्यति.\n'
        '\n'
        'SETTLED — and the vṛtti names where the sense stops:\n'
        '  महाराजप्रोष्ठपदाट् ठञ् इति यावत् — 4.2.35. The third\n'
        '  range in this pāda with both ends stated.\n'
        '\n'
        'SETTLED — सेति प्रकृते **पुनः समर्थविभक्तिनिर्देशः\n'
        '  संज्ञानिवृत्त्यर्थः**: the case is named again though it\n'
        '  is already running, and the repetition is what stops\n'
        "  4.2.21's संज्ञायाम् carrying down with it. A word\n"
        "  restated to break a bundle — 4.1.65's move exactly."
    ),
    '4.2.25': (
        'SETTLED — कस्येत्. **ततः पूर्वेणैवाण्प्रत्ययः सिद्धः, इकारादेशार्थं\n'
        '  वचनम्** — the affix came already and the whole rule is\n'
        '  the इ: कायं हविः, कायमेककपालं निर्वपेत् (मै०सं०\n'
        '  ३.१५.१०). The fifth rule in two pādas whose stated affix\n'
        '  is not what it is for, after 4.1.7, 4.1.97, 4.1.115 and\n'
        '  4.1.116.'
    ),
    '4.2.26': (
        'SETTLED — शुक्राद् घन्, अणोऽपवादः. शुक्रियं हविः; शुक्रियोऽध्यायः.'
    ),
    '4.2.27': (
        'SETTLED — अपोनप्तृ अपांनप्तृभ्यां घः, अणोऽपवादः. अपोनप्त्रियं हविः\n'
        '  (का०श्रौ० २३.४.१४). अपोनपाद्, अपांनपाद् इति देवताया\n'
        '  नामधेये एते, and तयोस्तु प्रत्ययसन्नियोगेन रूपमिदं\n'
        '  निपात्यते — the shapes hold only when the affix comes.'
    ),
    '4.2.28': (
        'SETTLED — छ च. अपोनप्त्रीयं हविः, अपांनप्त्रीयम्.\n'
        '\n'
        'SETTLED — A RULE SPLIT SO THAT यथासंख्यम् MAY NOT APPLY.\n'
        '  **योगविभागः सङ्ख्यातानुदेशपरिहारार्थः**: had the two\n'
        '  affixes stood in one sūtra with the two bases, 1.3.10\n'
        '  would have paired them one to one. Dividing the rule is\n'
        '  what lets BOTH affixes reach BOTH words.\n'
        '\n'
        '  4.1.150 did the same job by BREAKING a compounding rule\n'
        '  and letting the breach be the signal; this does it by\n'
        '  splitting the sūtra. Two instruments for one purpose, a\n'
        '  pāda apart.\n'
        '\n'
        'NOTE — शतरुद्राच्छश्च घश्च gives both affixes to one word:\n'
        '  शतरुद्रीयम्, शतरुद्रियम्.'
    ),
    '4.2.29': (
        'SETTLED — महेन्द्राद् घाणौ च. THREE AFFIXES FOR ONE WORD, the third\n'
        '  by a च — and each form is cited to a different text:\n'
        '  महेन्द्रियं हविः, माहेन्द्रम् (तै०सं० ६.५.५.४),\n'
        "  महेन्द्रीयम् (काठ०सं० १५.१). Not a grammarian's\n"
        '  construction but three attested usages.'
    ),
    '4.2.30': (
        'SETTLED — सोमाट् ट्यण्, अणोऽपवादः. सौम्यं हविः, सौम्यं सूक्तम्,\n'
        '  सौमी ऋक् (मै०सं० १.७.४).\n'
        '\n'
        'SETTLED — **ण्कारो वृद्ध्यर्थः, टकारो ङीबर्थः**: the ण् for\n'
        "  the strengthening, the ट् so that 4.1.15's ङीप् reaches\n"
        '  it in the feminine. Two marks, two jobs, neither heard —\n'
        "  the same shape as 3.4.81's शकार and चकार."
    ),
    '4.2.31': (
        'SETTLED — वायुऋतुपित्रुषसो यत्, अणोऽपवादः. वायव्यम्, ऋतव्यम्,\n'
        '  पित्र्यम् (ऋ० ८.२०.१३), उषस्यम्.'
    ),
    '4.2.32': (
        'SETTLED — द्यावापृथिवीशुनासीरमरुत्वदग्नीषोमवास्तोष्पतिगृहमेधाच् छः,\n'
        '  and चकाराद् यत् च — **so every one of the six has two\n'
        '  forms and both are cited**: द्यावापृथिवीयम् (मै०सं०\n'
        '  १.८.१०) beside द्यावापृथिव्यम् (तै०सं० १.८.२.१);\n'
        '  शुनासीरीयम् (मा०सं० २४.१९) beside शुनासीर्यम् (मै०सं०\n'
        '  ४.३.३); and so through मरुत्वत्, अग्नीषोम, वास्तोष्पति,\n'
        '  गृहमेध.\n'
        '\n'
        'NOTE — शुनो वायुः, सीर आदित्यः: the vṛtti glosses which\n'
        '  gods the compound names, because the words are not\n'
        '  transparent even to a reader of the Veda.'
    ),
    '4.2.33': (
        'SETTLED — अग्नेर्ढक्, अणोऽपवादः. आग्नेयोऽष्टाकपालः (तै०सं० १.८.२.१).\n'
        "  And 4.2.8's vārttika is repeated here:\n"
        '  प्राग्दीव्यतीयेषु तद्धितार्थेषु सर्वत्राग्निकलिभ्यां ढग् —\n'
        '  one affix for these two words in EVERY sense of the\n'
        '  section, which is a rule about words and not about\n'
        '  senses.'
    ),
    '4.2.34': (
        'SETTLED — कालेभ्यो भववत्. **AN अतिदेश REACHING FORWARD TO RULES NOT\n'
        '  YET STATED**: कालाट् ठञ् इति प्रकरणे भवे प्रत्यया\n'
        '  विधास्यन्ते, ते सास्य देवतेत्यस्मिन्नर्थे तथैवेष्यन्ते —\n'
        '  what 4.3.11 onward will give in the sense *born in* comes\n'
        '  here too. मासो देवतास्य मासिकम्; आर्धमासिकम्,\n'
        '  सांवत्सरिकम्, वासन्तम्, प्रावृषेण्यम्.\n'
        '\n'
        'SETTLED — **वत्करणं सर्वसादृश्यपरिग्रहार्थम्**: the वत्\n'
        '  takes in EVERY likeness and not merely the affix.\n'
        "  3.4.85's लोटो लङ्वत् had its borrowing bounded by an\n"
        '  option carried from two sūtras back; this one is stated\n'
        '  to be total.'
    ),
    '4.2.35': (
        'SETTLED — महाराजप्रोष्ठपदाट् ठञ्. माहाराजिकम्, प्रौष्ठपदिकम् — the\n'
        "  rule 4.2.24's vṛtti named as where the deity-sense stops.\n"
        '\n'
        'NOTE — ठञ्प्रकरणे **तदस्मिन् वर्तत** इति नवयज्ञादिभ्य\n'
        '  उपसंख्यानम्: नावयज्ञिकः कालः. A vārttika adding not words\n'
        '  but a whole further SENSE. And पूर्णमासादण् gives\n'
        "  पौर्णमासी तिथिः (मै०सं० १.६.९) — the very word 4.2.21's\n"
        '  vṛtti had to derive fourteen sūtras earlier.'
    ),
    '4.2.36': (
        'SETTLED — पितृव्यमातुलमातामहपितामहाः. निपात्यन्ते: पितृव्यः, मातुलः,\n'
        '  पितामहः, मातामहः, and मातरि षित् — पितामही, मातामही.\n'
        '\n'
        'SETTLED — THE MOST COMPLETE निपातन IN THE PROJECT.\n'
        '  **समर्थविभक्तिः प्रत्ययः प्रत्ययार्थोऽनुबन्ध इति सर्वं\n'
        '  निपातनाद् विज्ञेयम्** — the case-relation, the affix, the\n'
        '  sense of the affix and its marks are ALL to be read off\n'
        '  the fixing. Nothing in the rule is derived from anything;\n'
        '  the forms are given, and everything a rule normally\n'
        '  supplies is inferred backward from them.\n'
        '\n'
        'NOTE — three vārttikas fix three more sets on the same\n'
        '  footing: अविसोढम्, अविदूसम्, अविमरीसम्; तिलपिञ्जः,\n'
        '  तिलपेजः; and तिल्पिञ्जं दण्डनं नडम् (शौ०सं० १२.२.५४).'
    ),
    '4.2.37': (
        'SETTLED — तस्य समूहः. काकानां समूहः काकम्; बाकम्.\n'
        '\n'
        'SETTLED — AND THE VṚTTI HAS TO COMPUTE AN EXAMPLE BY\n'
        '  SUBTRACTION. किमिहोदाहरणम्? Every ordinary base is taken\n'
        '  by some later rule, so the answer is a list of what the\n'
        '  example must NOT be: **चित्तवद् आद्युदात्तम् अगोत्रम्\n'
        '  यस्य च नान्यत् प्रतिपदं ग्रहणम्** — animate, since\n'
        '  4.2.47 takes the inanimate; first-accented, since 4.2.44\n'
        '  takes the rest; not a lineage-name, since 4.2.39 takes\n'
        '  those; and not named in any rule of its own, since\n'
        '  4.2.40 and its like name words directly.\n'
        '  तत्परिहारेणात्रोदाहरणं द्रष्टव्यम्. **A rule whose\n'
        '  example exists only in the gap its own section leaves.**\n'
        '\n'
        'SETTLED — इनित्रकट्यचश्च इति यावत् समूहाधिकारः, to 4.2.51.\n'
        '  The fourth stated range in this pāda.'
    ),
    '4.2.38': (
        'SETTLED — भिक्षादिभ्योऽण्. भैक्षम्, गार्भिणम्. **अण्ग्रहणं\n'
        '  बाधकबाधनार्थम्** — the default named again in order to\n'
        "  beat what would have beaten it, which is 4.1.84's move\n"
        "  and 4.2.11's.\n"
        '\n'
        'NOTE — युवतिशब्दोऽत्र पठ्यते, **तस्य ग्रहणसामर्थ्यात्\n'
        '  पुंवद्भावो न भवति**: being named in the list is itself\n'
        '  the reason the feminine is not replaced by the masculine.\n'
        '  यौवतम्. A membership doing the work of a प्रतिषेध.'
    ),
    '4.2.39': (
        'SETTLED — गोत्रोक्षोष्ट्रोरभ्रराजराजन्यराजपुत्रवत्समनुष्याजाद् वुञ्.\n'
        '  औपगवकम्, औक्षकम्, राजकम्, मानुष्यकम्, आजकम्.\n'
        '\n'
        'SETTLED — AND गोत्र IS READ IN ITS ORDINARY SENSE HERE.\n'
        '  अपत्याधिकारादन्यत्र **लौकिकं गोत्रं गृह्यते** अपत्यमात्रम्,\n'
        '  न तु पौत्रप्रभृत्येव — outside the descendant section the\n'
        "  word means any descendant and not 4.1.162's\n"
        '  grandson-onward. The same word technical inside one\n'
        '  section and ordinary outside it, and the section is the\n'
        '  boundary.'
    ),
    '4.2.40': (
        'SETTLED — केदाराद् यञ् च, अचित्तलक्षणस्य ठकोऽपवादः. कैदार्यम्, and\n'
        '  by the च also कैदारकम्. गणिकायाश्च यञ् — गाणिक्यम्.'
    ),
    '4.2.41': (
        'SETTLED — ठञ् कवचिनश्च. कावचिकम् — and **चकारः केदारादित्यस्य\n'
        "  अनुकर्षणार्थः**, the च pulls the last rule's word down so\n"
        '  that कैदारिकम् stands too. A third form for one word,\n'
        '  made by a conjunction.'
    ),
    '4.2.42': (
        'SETTLED — ब्राह्मणमाणववाडवाद् यन्. ब्राह्मण्यम्, माणव्यम्,\n'
        '  वाडव्यम्. नकारः स्वरार्थः.\n'
        '\n'
        'NOTE — five vārttikas add five more, each with a different\n'
        '  affix: पृष्ठ्यः षडहः; **अह्नः खः क्रतौ** — अहीनः क्रतुः,\n'
        '  and क्रताविति किम्? आह्नः; पार्श्वम्,\n'
        '  पदसंज्ञकत्वाद् गुणो न भवति; and वातूलः.'
    ),
    '4.2.43': (
        'SETTLED — ग्रामजनबन्धुसहायेभ्यस्तल्. ग्रामता, जनता, बन्धुता,\n'
        '  सहायता. **The affix that gives the language its abstract\n'
        '  nouns**, and here it is a rule about crowds — the sense is\n'
        '  a COLLECTION and not a quality. गजाच्चेति वक्तव्यम्.'
    ),
    '4.2.44': (
        'SETTLED — अनुदात्तादेरञ्. कापोतम्, मायूरम्, तैत्तिरम्. The first of\n'
        "  the four rules 4.2.37's vṛtti had to subtract before it\n"
        '  could name an example of its own.'
    ),
    '4.2.45': (
        'SETTLED — खण्डिकादिभ्यश्च. खाण्डिकम्, वाडवम्. **आद्युदात्तार्थम्\n'
        '  अचित्तार्थं च वचनम्** — stated for the two grounds\n'
        '  4.2.44 and 4.2.47 would otherwise have taken.\n'
        '\n'
        'SETTLED — AND ONE MEMBER OF THE LIST TEACHES TWO THINGS AT\n'
        '  ONCE. क्षुद्रकमालव is in it though 4.2.44 already reaches\n'
        '  it: ननु च परत्वादञा वुञ् बाधिष्यते? **एवं तर्ह्येतज्\n'
        '  ज्ञापयति — वुञि पूर्वविप्रतिषेधः, सामूहिकेषु च\n'
        "  तदन्तविधिरस्तीति**. Its presence teaches that 4.2.39's\n"
        '  वुञ् wins by पूर्वविप्रतिषेध, AND that these rules reach\n'
        '  a compound through its last member — औपगवकम् for the\n'
        '  first, वानहस्तिकम् for the second. One list-entry read as\n'
        '  two general principles.\n'
        '\n'
        '  And the same member is then restated with a condition to\n'
        '  narrow it: क्षुद्रकमालवात् **सेनासंज्ञायाम्** एवाञ् भवति\n'
        '  — क्षौद्रकमालवी सेना, क्षौद्रकमालवकमन्यत्. Two kārikās\n'
        '  set out the whole argument.'
    ),
    '4.2.46': (
        'SETTLED — चरणेभ्यो धर्मवत्. **AN अतिदेश BORROWING FROM A VĀRTTIKA,\n'
        '  NOT FROM A SŪTRA.** गोत्रचरणाद् वुञ् इत्यारभ्य प्रत्यया\n'
        '  वक्ष्यन्ते, तत्रेदमुच्यते **चरणाद् धर्माम्नाययोः**\n'
        '  (वा० ४.३.१२६) इति, तेन धर्मवद् इत्यतिदेशः क्रियते. What\n'
        '  is borrowed is what a VĀRTTIKA on a later sūtra will\n'
        '  give, and the sūtra here points at it.\n'
        '  **वतिः सर्वसादृश्यार्थः** — total, as at 4.2.34.\n'
        '\n'
        '  काठकम्, कालापकम्, छान्दोग्यम्, औक्थिक्यम्, आथर्वणम् —\n'
        "  the same five forms serve for the school's practice and\n"
        '  for a group of its members.'
    ),
    '4.2.47': (
        'SETTLED — अचित्तहस्तिधेनोष्ठक्, अणञोरपवादः. आपूपिकम्, शाष्कुलिकम्;\n'
        '  हास्तिकम्, धैनुकम्. धेनोरनञ इति वक्तव्यम् — आधेनवम्.\n'
        "  The second of 4.2.37's four subtractions."
    ),
    '4.2.48': (
        'SETTLED — केशाश्वाभ्यां यञ्छावन्यतरस्याम्, यथासंख्यम्. कैश्यम् beside\n'
        '  कैशिकम्; अश्वीयम् beside आश्वम्.'
    ),
    '4.2.49': (
        'SETTLED — पाशादिभ्यो यः. पाश्या, तृण्या.'
    ),
    '4.2.50': (
        'SETTLED — खलगोरथात्. खल्या, गव्या, रथ्या. **पाशादिष्वपाठ\n'
        '  उत्तरार्थः** — the three are kept OUT of the previous\n'
        "  rule's list, though the affix is the same, so that the\n"
        '  NEXT rule may name them. A membership withheld for a\n'
        "  later rule's sake, which is 4.1.45's move in reverse."
    ),
    '4.2.51': (
        'SETTLED — इनित्रकट्यचश्च, यथासंख्यम्. खलिनी, गोत्रा, रथकट्या — the\n'
        "  rule 4.2.37's vṛtti named as where the collection-sense\n"
        '  stops.\n'
        '\n'
        'NOTE — four vārttikas add four more affixes, and the last\n'
        '  two are of a kind the section has not used: **कमलादिभ्यः\n'
        '  खण्डच्** — कमलखण्डम्, an आकृतिगण; **नरकरितुरङ्गाणां\n'
        '  स्कन्धच्** — नरस्कन्धः; and **पूर्वादिभ्यः काण्डः** —\n'
        '  पूर्वकाण्डम्, कर्मकाण्डम्. Affixes that are whole words,\n'
        '  and the last of them is what names the divisions of a\n'
        '  book.'
    ),
    '4.2.52': (
        'SETTLED — तस्य विषयो देशः. शिबीनां विषयो देशः शैबः; औष्ट्रः.\n'
        '  देश इति किम्? देवदत्तस्य विषयोऽनुवाकः.\n'
        '\n'
        'SETTLED — AND THE VṚTTI ENUMERATES FOUR SENSES OF ONE WORD\n'
        '  BEFORE SAYING WHICH IS MEANT. विषयशब्दोऽयं बह्वर्थः —\n'
        '  क्वचिद् ग्रामसमुदाये (विषयो लब्धः), क्वचिद्\n'
        '  इन्द्रियग्राह्ये (चक्षुर्विषयो रूपम्), क्वचिद्\n'
        '  अत्यन्तशीलिते ज्ञेये (देवदत्तस्य विषयोऽनुवाकः), क्वचिद्\n'
        '  अन्यत्राभावे (मत्स्यानां विषयो जलम्). **तत्र देशग्रहणं\n'
        '  ग्रामसमुदायप्रतिपत्त्यर्थम्**: the word देश is what picks\n'
        '  the first. A word disambiguated by a second word, with\n'
        '  the other three senses set out so the work is visible.'
    ),
    '4.2.53': (
        'SETTLED — राजन्यादिभ्यो वुञ्, अणोऽपवादः. राजन्यकः, दैवयानकः — and\n'
        '  **आकृतिगणश्चायम्**, so मालवकः, वैराटकः, त्रैगर्तकः come\n'
        '  too. The fourth open list the project has met.'
    ),
    '4.2.54': (
        'SETTLED — भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ, यथासंख्यम्,\n'
        '  अणोऽपवादः. भौरिकिविधः, वैपेयविधः; ऐषुकारिभक्तः,\n'
        '  सारस्यायनभक्तः. **Two affixes that are whole words** —\n'
        '  विध and भक्त, *portion* and *share* — matched to two\n'
        '  lists.'
    ),
    '4.2.55': (
        'SETTLED — सोऽस्यादिरिति छन्दसः प्रगाथेषु. पाङ्क्तः प्रगाथः;\n'
        '  आनुष्टुभः, जागतः.\n'
        '\n'
        'SETTLED — SIX WORDS AND THE VṚTTI ASSIGNS A JOB TO EACH\n'
        '  BEFORE GIVING A SINGLE EXAMPLE. स इति समर्थविभक्तिः;\n'
        '  अस्येति प्रत्ययार्थः; आदिरिति प्रकृतिविशेषणम्; इतिकरणो\n'
        '  विवक्षार्थः; छन्दस इति प्रकृतिनिर्देशः; प्रगाथेष्विति\n'
        '  प्रत्ययार्थविशेषणम्.\n'
        '\n'
        'NOTE — and प्रगाथ is defined: यत्र द्वे ऋचौ प्रग्रथनेन\n'
        '  तिस्रः क्रियन्ते, स प्रग्रथनात् प्रकर्षगानाद् वा प्रगाथ\n'
        '  इत्युच्यते — where two verses are made three by being\n'
        '  woven together.'
    ),
    '4.2.56': (
        'SETTLED — संग्रामे प्रयोजनयोद्धृभ्यः. भाद्रः संग्रामः, सौभद्रः,\n'
        '  गौरिमित्रः; and from the fighters — आहिमालः,\n'
        '  स्यान्दनाश्वः, भारतः.\n'
        '\n'
        'NOTE — प्रयोजनयोद्धृभ्य इति किम्? सुभद्रा प्रेक्षिकास्य\n'
        '  संग्रामस्य: a battle someone merely WATCHES is not one\n'
        '  she is the cause of.'
    ),
    '4.2.57': (
        'SETTLED — तदस्मिन् प्रहरणमिति क्रीडायाम्. दण्डः प्रहरणमस्यां\n'
        '  क्रीडायां दाण्डा; मौष्टा. प्रहरणमिति किम्? माला\n'
        '  भूषणमस्यां क्रीडायाम्. क्रीडायामिति किम्? खङ्गः\n'
        '  प्रहरणमस्यां सेनायाम् — the same weapon in an army and\n'
        '  not a game.'
    ),
    '4.2.58': (
        'SETTLED — घञः स्त्रियाम्. श्यैनंपाता, तैलंपाता. घञ इति कृद्ग्रहणम्,\n'
        '  तत्र गतिकारकपूर्वमपि गृह्यते.\n'
        '\n'
        'SETTLED — AND THE VṚTTI ASKS WHY THE CASE AND THE SENSE ARE\n'
        '  STATED AGAIN WHEN BOTH ARE ALREADY RUNNING. अथ\n'
        '  समर्थविभक्तिः प्रत्ययार्थश्च कस्मात् पुनरुपादीयते,\n'
        '  यावता द्वयमपि प्रकृतमेव? **क्रीडायामित्यनेन तत्\n'
        '  संबद्धम्, अतस्तदनुवृत्तौ क्रीडानुवृत्तिरपि संभाव्येत** —\n'
        '  because they came bundled with *in a game*, and carrying\n'
        '  them would have carried that too. Restating them is how\n'
        "  the bundle is broken: 4.2.24's move and 4.1.65's, a third\n"
        '  time. सामान्येन चेदं विधानम् — दाण्डपाता तिथिः.'
    ),
    '4.2.59': (
        'SETTLED — तदधीते तद्वेद. छान्दसः, वैयाकरणः, नैरुक्तः; and for the\n'
        '  knower — नैमित्तः, मौहूर्तः, औत्पातः.\n'
        '\n'
        'SETTLED — **द्विस्तद्ग्रहणम् अधीयानविदुषोः\n'
        '  पृथग्विधानार्थम्**: the word *that* is said TWICE so the\n'
        '  two are given separately. One who studies a thing and one\n'
        '  who knows it are not the same person, and a single\n'
        '  statement would have required both at once.'
    ),
    '4.2.60': (
        'SETTLED — क्रतूक्थादिसूत्रान्ताट् ठक्, अणोऽपवादः. आग्निष्टोमिकः,\n'
        '  वाजपेयिकः; औक्थिकः, लौकायतिकः; वार्तिकसूत्रिकः.\n'
        '\n'
        'NOTE — THE LONGEST VĀRTTIKA-SET IN THE PĀDA, and it is\n'
        '  about what people study. **आख्यानाख्यायिकयोर्\n'
        '  अर्थग्रहणम्, इतिहासपुराणयोः स्वरूपग्रहणम्** — of four\n'
        '  words in one vārttika, two are taken by their MEANING and\n'
        '  two by their FORM. And a word is refused for a reason\n'
        '  outside grammar altogether: औक्थिक्यशब्दाच्च प्रत्ययो न\n'
        '  भवत्येव, **अनभिधानात्** — because no one says it.'
    ),
    '4.2.61': (
        'SETTLED — क्रमादिभ्यो वुन्, अणोऽपवादः. क्रमकः, पदकः.'
    ),
    '4.2.62': (
        'SETTLED — अनुब्राह्मणादिनिः, अणोऽपवादः. अनुब्राह्मणी.\n'
        '  ब्राह्मणसदृशोऽयं ग्रन्थोऽनुब्राह्मणम्.\n'
        '\n'
        'NOTE — the vṛtti tries three answers before settling. \n'
        '  मत्वर्थेन अत इनिठनौ इतीनिना सिद्धम्? तत्रैतस्माट् ठन्नपि\n'
        '  प्राप्नोति. अनभिधानान्न भविष्यति? **अणो निवृत्त्यर्थं\n'
        '  तर्हि वचनम्** — the rule is there to keep the default\n'
        '  out. The fourth rule in two pādas read that way.'
    ),
    '4.2.63': (
        'SETTLED — वसन्तादिभ्यष्ठक्, अणोऽपवादः. वासन्तिकः, वार्षिकः.\n'
        '  **वसन्तसहचरितोऽयं ग्रन्थो वसन्तः** — the text is called\n'
        '  by the season it goes with, and the affix is given to the\n'
        '  text.'
    ),
    '4.2.64': (
        'SETTLED — प्रोक्ताल्लुक्. **प्रोक्तसहचरितः प्रत्ययः प्रोक्तः** — an\n'
        '  affix given in the sense *declared by* is itself called\n'
        '  *declared*, by association. पाणिनिना प्रोक्तं\n'
        '  पाणिनीयम्, तदधीते **पाणिनीयः**: the second affix is\n'
        '  elided, so the student and the work are one word.\n'
        '  आपिशलः. स्त्रियां स्वरे च विशेषः — पाणिनीया ब्राह्मणी.'
    ),
    '4.2.65': (
        'SETTLED — सूत्राच्च कोपधात्. **अप्रोक्तार्थ आरम्भः** — begun for the\n'
        '  case the rule before could not reach, the text not being\n'
        '  *declared by* anyone. पाणिनीयमष्टकं सूत्रम्, तदधीयते\n'
        '  **अष्टकाः पाणिनीयाः**; दशका वैयाघ्रपदीयाः; त्रिकाः\n'
        '  काशकृत्स्नाः — students named by how many sections their\n'
        '  book has.\n'
        '\n'
        'NOTE — संख्याप्रकृतेरिति वक्तव्यम्: माहावार्तिकः and\n'
        '  कालापकः stay out. कोपधादिति किम्? चातुष्टयः. And this is\n'
        '  where the studying-sense stops.'
    ),
    '4.2.66': (
        'SETTLED — छन्दोब्राह्मणानि च तद्विषयाणि. **A RULE THAT RESTRICTS\n'
        '  RATHER THAN GIVES, AND WHAT IT RESTRICTS IS A WHOLE CLASS\n'
        '  OF WORDS.** छन्दांसि ब्राह्मणानि च प्रोक्तप्रत्ययान्तानि\n'
        '  **तद्विषयाण्येव भवन्ति** — a Vedic text or a Brāhmaṇa\n'
        '  named by *declared by* is used of THAT SUBJECT ONLY.\n'
        '  कठाः, मौदाः, पैप्पलादाः, वाजसनेयिनः; ताण्डिनः,\n'
        '  ऐतरेयिणः.\n'
        '\n'
        'SETTLED — **अनन्यभावो विषयार्थः, तेन स्वातन्त्र्यम्\n'
        '  उपाध्यन्तरयोगो वाक्यं च निवर्तते** — *subject* means\n'
        '  having no other being, and THREE things fall away with\n'
        '  it: the word standing on its own, its joining another\n'
        '  qualifier, and a phrase in place of the word. One\n'
        '  restriction doing three refusals at once.\n'
        '\n'
        'NOTE — चकारोऽनुक्तसमुच्चयार्थः brings in the ritual\n'
        '  manuals and the aphorisms: काश्यपिनः, पाराशरिणो भिक्षवः,\n'
        '  **शैलालिनो नटाः** — actors, in a grammar of the Veda.\n'
        '  छन्दोब्राह्मणानीति किम्? पाणिनीयं व्याकरणम्.'
    ),
    '4.2.67': (
        'SETTLED — तदस्मिन्नस्तीति देशे तन्नाम्नि. उदुम्बरा अस्मिन् देशे\n'
        '  सन्ति औदुम्बरः; बाल्बजः, पार्वतः.\n'
        '\n'
        'SETTLED — **तन्नाम्नि: the country must be NAMED by the\n'
        '  derived word**, प्रत्ययान्तनामा. That clause carries down\n'
        '  through all four senses and is what 4.2.81 and 4.2.85\n'
        '  both lean on to keep an elision or an affix off — a\n'
        '  condition doing work fourteen and eighteen sūtras on.'
    ),
    '4.2.68': (
        'SETTLED — तेन निर्वृत्तम्. साहस्री परिखा, कौशाम्बी नगरी — a moat\n'
        '  made at the cost of a thousand, and a city founded by\n'
        '  Kuśāmba. **हेतौ कर्तरि च यथायोगं तृतीया समर्थविभक्तिः**:\n'
        '  the instrumental is read as the CAUSE in one and as the\n'
        '  DOER in the other, whichever fits.'
    ),
    '4.2.69': (
        'SETTLED — तस्य निवासः. **निवसन्त्यस्मिन्निति निवासः**. आर्जुनावो\n'
        '  देशः; शैबः, औदिष्ठः.'
    ),
    '4.2.70': (
        'SETTLED — अदूरभवश्च. वैदिशम्, हैमवतम्.\n'
        '\n'
        'SETTLED — AND THE च IS WHAT MAKES FOUR SENSES OUT OF FOUR\n'
        '  RULES. **चकारः पूर्वेषां त्रयाणामर्थानामिह\n'
        '  सन्निधानार्थः, तेनोत्तरेषु चत्वारोऽप्यर्थाः\n'
        '  संबध्यन्ते** — the conjunction brings the previous three\n'
        '  alongside this one, and from here all four carry\n'
        '  together into every rule that follows.\n'
        '\n'
        '  The tradition then names that whole run of affixes\n'
        '  चातुरर्थिक, *of-the-four-senses*. **A body of rules named\n'
        '  from a NUMBER, and the number produced by one syllable.**'
    ),
    '4.2.71': (
        'SETTLED — ओरञ्, अणोऽपवादः. आरडवम्, काक्षतवम्. नद्यां तु परत्वाद्\n'
        '  मतुब् भवति — इक्षुमती.\n'
        '\n'
        'SETTLED — **अञधिकारः प्राक् सुवास्त्वादिभ्योऽणः**: the\n'
        '  affix governs to 4.2.77. The sixth stated range in the\n'
        '  pāda, and the first stated of an AFFIX rather than of a\n'
        '  case or a sense.'
    ),
    '4.2.72': (
        'SETTLED — मतोश्च बह्वजङ्गात्, अणोऽपवादः. ऐषुकावतम्, सैध्रकावतम्.\n'
        '  बह्वजङ्गादिति किम्? आहिमतम्.\n'
        '\n'
        'SETTLED — **अङ्गग्रहणं किम्? बह्वजिति तद्विशेषणं यथा\n'
        '  विज्ञायेत, मत्वन्तविशेषणं मा विज्ञायि** — the word अङ्ग\n'
        '  is there so that *many-voweled* qualifies what the मतुप्\n'
        '  is ADDED TO and not the whole word: मालावतम्. A word\n'
        '  inserted to fix which of two things an adjective\n'
        '  attaches to.'
    ),
    '4.2.73': (
        'SETTLED — बह्वचः कूपेषु, अणोऽपवादः. दैर्घवरत्रः, कापिलवरत्रः.\n'
        '  **यथासंभवमर्थाः संबध्यन्ते** — whichever of the four\n'
        '  senses fits, and the vṛtti says so at nearly every rule\n'
        '  of this run.'
    ),
    '4.2.74': (
        'SETTLED — उदक् च विपाशः. Wells on the NORTH bank of the Vipāś:\n'
        '  दात्तः, गौप्तः. **अबह्वजर्थ आरम्भः**. उदगिति किम्?\n'
        '  दक्षिणतो विपाशः कूपेष्वणेव, **स्वरे विशेषः** — south of\n'
        '  the river the default comes and the two differ only in\n'
        '  accent.\n'
        '\n'
        'NOTE — and the vṛtti stops to say what it thinks of a rule\n'
        '  that turns on which bank of a river a well stands:\n'
        '  **महती सूक्ष्मेक्षिका वर्तते सूत्रकारस्य** — the\n'
        "  sūtra-maker's eye for fine distinctions is great."
    ),
    '4.2.75': (
        'SETTLED — संकलादिभ्यश्च, अणोऽपवादः. सांकलः, पौष्कलः.\n'
        '  **कूपेष्विति निवृत्तम्** — the wells stop here.'
    ),
    '4.2.76': (
        'SETTLED — स्त्रीषु सौवीरसाल्वप्राक्षु. दात्तामित्री; वैधूमाग्नी;\n'
        '  काकन्दी, माकन्दी. FEMININE place-names in three regions,\n'
        "  and the condition is the GENDER of the country's name."
    ),
    '4.2.77': (
        'SETTLED — सुवास्त्वादिभ्योऽण्. सौवास्तवम्, वार्णवम् — the rule\n'
        "  4.2.71's vṛtti named as where its affix stops.\n"
        '  **अण्ग्रहणं नद्यां मतुपो बाधनार्थम्**: the default is\n'
        "  named expressly to beat 4.2.85 — सौवास्तवी नदी. 4.1.84's\n"
        '  move for the fifth time.'
    ),
    '4.2.78': (
        'SETTLED — रोणी. **रोणीति कोऽयं निर्देशः, यावता प्रत्ययविधौ पञ्चमी\n'
        '  युक्ता?** — a rule that gives an affix should name its\n'
        '  base in the ablative, and this names it in the\n'
        '  nominative. **सर्वावस्थप्रतिपत्त्यर्थमेवमुच्यते**: so\n'
        '  that the word is taken in EVERY state, alone and as a\n'
        '  final member — रौणः, आजकरोणः, सैंहिकरोणः. A case\n'
        '  deliberately wrong so that no restriction follows from\n'
        "  it, which is 4.1.150's instrument used on a case-ending."
    ),
    '4.2.79': (
        'SETTLED — कोपधाच्च. कार्णच्छिद्रिकः कूपः; कार्कवाकवम्, त्रैशङ्कवम्.'
    ),
    '4.2.80': (
        'SETTLED — वुञ्छण्कठजिलसेनिरढञ्ययफक्फिञिञ्ञ्यकक्ठकोऽरीहण ... आदिभ्यः.\n'
        '\n'
        'SETTLED — **SEVENTEEN AFFIXES AND SEVENTEEN LISTS, MATCHED\n'
        '  IN ORDER.** वुञादयः सप्तदश प्रत्ययाः, अरीहणादयोऽपि\n'
        '  सप्तदशैव प्रातिपदिकगणाः, **आदिशब्दः प्रत्येकम्\n'
        '  अभिसंबध्यते** — and the word *and-the-rest* attaches to\n'
        '  each of the seventeen separately. The longest यथासंख्य\n'
        "  correspondence in the grammar, five times 4.1.42's\n"
        '  eleven, and one sūtra holds all of it.\n'
        '\n'
        '  आरीहणकम्, कार्शाश्वीयः, ऋश्यकः, कुमुदिकम्, काशिलम्,\n'
        '  तृणसः, प्रेक्षी, अश्मरः, साखेयम्, सांकाश्यम्, बल्यः,\n'
        '  पाक्षायणः, कार्णायनिः, सौतङ्गमिः, प्रागद्यम्, वाराहकम्,\n'
        '  कौमुदिकम् — seventeen forms, one from each list.\n'
        '\n'
        'NOTE — and one word is in THREE of the seventeen:\n'
        '  शिरीषशब्दोऽरीहणादिषु, कुमुदादिषु, वराहादिषु च पठ्यते,\n'
        '  **औत्सर्गिकोऽपि तत इष्यते** — with the default wanted\n'
        "  from it as well, so four affixes; and then 4.2.82's list\n"
        '  elides one of them.'
    ),
    '4.2.81': (
        'SETTLED — जनपदे लुप्. **ग्रामसमुदायो जनपदः** — where the country is\n'
        '  a group of villages the affix is DROPPED: पञ्चालानां\n'
        '  निवासो जनपदः **पञ्चालाः**; कुरवः, मत्स्याः, अङ्गाः,\n'
        '  वङ्गाः, मगधाः. The affix is given and removed, and what\n'
        '  remains is the name of a PEOPLE used as the name of\n'
        '  their country.\n'
        '\n'
        'SETTLED — इह कस्माद् न भवति औदुम्बरो जनपदः?\n'
        '  **तन्नाम्नीति वर्तते, न चात्र लुबन्तं तन्नामधेयं भवति**\n'
        "  — 4.2.67's clause carries down fourteen sūtras and\n"
        '  decides where the elision may bite: the elided form is\n'
        '  not what those countries are called.'
    ),
    '4.2.82': (
        'SETTLED — वरणादिभ्यश्च. **अजनपदार्थ आरम्भः** — begun for what is\n'
        '  not a country: वरणानामदूरभवं नगरं वरणाः; शृङ्गी,\n'
        '  शाल्मलयः. चकारोऽनुक्तसमुच्चयार्थ आकृतिगणतामस्य बोधयति.'
    ),
    '4.2.83': (
        'SETTLED — शर्करायां वा. शर्करा beside शार्करम्.\n'
        '\n'
        'SETTLED — AND THE वा IS READ AS A ज्ञापक. वाग्रहणं किम्,\n'
        '  यावता शर्कराशब्दः कुमुदादिषु वराहादिषु च पठ्यते, तत्र\n'
        '  पाठसामर्थ्यात् प्रत्ययस्य पक्षे श्रवणं भविष्यति? — being\n'
        "  in two of 4.2.80's lists would have given the\n"
        '  alternative already. **एवं तर्ह्येतज् ज्ञापयति —\n'
        '  शर्कराशब्दादौत्सर्गिको भवति, तस्यायं विकल्पितो लुब्**:\n'
        '  so the word teaches that the DEFAULT affix comes from\n'
        '  this base too, and it is that one being optionally\n'
        '  elided.\n'
        '\n'
        '  **तदेवं षड् रूपाणि भवन्ति** — शर्करा, शार्करम्,\n'
        '  शर्करिकम्, शार्करकम्, शार्करिकम्, शर्करीयम्. Six forms\n'
        '  for one word, counted out.'
    ),
    '4.2.84': (
        'SETTLED — ठक्छौ च. शार्करिकम्, शर्करीयम् — the two that bring the\n'
        '  count to six.'
    ),
    '4.2.85': (
        'SETTLED — नद्यां मतुप्. उदुम्बरावती, मशकावती, इक्षुमती.\n'
        '  **तन्नाम्नो देशस्य विशेषणं नदी**.\n'
        '\n'
        'NOTE — इह कस्माद् न भवति भागीरथी?\n'
        '  **मतुबन्तस्यातन्नामधेयत्वात्** — those rivers are not\n'
        "  called by a मतुप्-form. 4.2.67's clause deciding again,\n"
        '  eighteen sūtras on.'
    ),
    '4.2.86': (
        'SETTLED — मध्वादिभ्यश्च. **अनद्यर्थ आरम्भः**. मधुमान्, बिसवान्.'
    ),
    '4.2.87': (
        'SETTLED — कुमुदनडवेतसेभ्यो ड्मतुप्. कुमुद्वान्, नड्वान्, वेतस्वान्.\n'
        '  महिषाच्चेति वक्तव्यम् — महिष्मान् नाम देशः.'
    ),
    '4.2.88': (
        'SETTLED — नडशादाड् ड्वलच्. नड्वलम्, शाद्वलम्.'
    ),
    '4.2.89': (
        'SETTLED — शिखाया वलच्. शिखावलं नाम नगरम्.\n'
        '\n'
        'NOTE — मतुप्प्रकरणेऽपि शिखाया वलचं वक्ष्यति, **तददेशार्थं\n'
        '  वचनम्** — 5.2.113 gives the same affix to the same word,\n'
        '  and that one is for what is NOT a place. Two rules, one\n'
        '  affix, one base, told apart by what the result is:\n'
        "  4.2.18's shape again, seventy-one sūtras on."
    ),
    '4.2.90': (
        'SETTLED — उत्करादिभ्यश्छः. उत्करीयम्, शफरीयम्.'
    ),
    '4.2.91': (
        'SETTLED — नडादीनां कुक् च. नडकीयम्, प्लक्षकीयम् — the affix and an\n'
        '  augment together, and this is where the four-senses run\n'
        '  stops.'
    ),
    '4.2.92': (
        'SETTLED — शेषे, **अधिकारोऽयम्**. यानित ऊर्ध्वं प्रत्ययान्\n'
        '  अनुक्रमिष्यामः, शेषेऽर्थे ते वेदितव्याः.\n'
        '\n'
        'SETTLED — A HEADING WHOSE CONTENT IS *EVERYTHING NOT\n'
        '  ALREADY PROVIDED FOR*. **उपयुक्तादन्यः शेषः** —\n'
        '  अपत्यादिभ्यश्चतुरर्थपर्यन्तेभ्योऽन्योऽर्थः शेषः: whatever\n'
        '  is left over from the descendant-sense through the four.\n'
        '  Not a sense at all but the COMPLEMENT of all the senses\n'
        "  so far, which is what 3.4.114's आर्धधातुकं शेषः was for\n"
        '  names — and the same word does it.\n'
        '\n'
        'SETTLED — and the vṛtti gives two reasons for stating it,\n'
        '  pulling opposite ways. तस्येदंविशेषा ह्यपत्यसमूहादयः,\n'
        '  **तेषु घादयो मा भूवन्निति शेषाधिकारः क्रियते** — the\n'
        '  earlier senses are special cases of *this belongs to\n'
        '  that*, so without the heading the affixes from here\n'
        '  would reach back into them. किं च, सर्वेषु जातादिषु\n'
        '  घादयो यथा स्युः ... **साकल्यार्थं शेषवचनम्** — and so\n'
        '  that they reach ALL of what remains rather than only the\n'
        '  nearest sense. **One word doing an exclusion and an\n'
        '  inclusion at once.**\n'
        '\n'
        'NOTE — **शेष इति लक्षणं चाधिकारश्च**: it is both a\n'
        '  statement of the ground and a heading, which is the\n'
        '  third time the vṛtti has declined to choose between two\n'
        '  readings of a rule because nothing turns on it — after\n'
        '  4.1.83 and 4.1.93. चाक्षुषं रूपम्, श्रावणः शब्दः,\n'
        '  दार्षदाः सक्तवः, आश्वो रथः.'
    ),
    '4.2.93': (
        'SETTLED — राष्ट्रावारपाराद् घखौ, यथासंख्यम्. राष्ट्रियः;\n'
        '  अवारपारीणः. विगृहीतादपीष्यते — अवारीणः, पारीणः; and\n'
        '  विपरीताच्च — पारावारीणः.\n'
        '\n'
        'SETTLED — AND HERE THE AFFIX COMES FIRST AND THE SENSE\n'
        '  AFTERWARDS. **प्रकृतिविशेषोपादानमात्रेण तावत् प्रत्यया\n'
        '  विधीयन्ते; तेषां तु जातादयोऽर्थाः समर्थविभक्तयश्च\n'
        '  पुरस्ताद् वक्ष्यन्ते** — these rules give affixes by\n'
        '  naming their BASES only, and the senses they carry and\n'
        '  the cases they attach in are stated further on, at\n'
        '  4.3.53 and after.\n'
        '\n'
        '  The exact reverse of everything from 4.2.1 to 4.2.91,\n'
        '  where a rule named a case and a sense and left the affix\n'
        "  to 4.1.83. That is what 4.2.92's शेषे makes possible:\n"
        '  with the sense given as *whatever is left*, an affix can\n'
        '  be supplied before anyone has said what it will mean.'
    ),
    '4.2.94': (
        'SETTLED — ग्रामाद् यखञौ. ग्राम्यः, ग्रामीणः — two affixes and no\n'
        '  option stated, so both stand.'
    ),
    '4.2.95': (
        'SETTLED — कत्र्यादिभ्यो ढकञ्. कात्रेयकः, औम्भेयकः.'
    ),
    '4.2.96': (
        'SETTLED — कुलकुक्षिग्रीवाभ्यः श्वास्यलंकारेषु, यथासंख्यम्.\n'
        '  **कौलेयको भवति श्वा चेत्, कौलोऽन्यः** — a DOG of the\n'
        '  family takes one affix and anything else the other;\n'
        '  कौक्षेयको भवत्यसिश्चेत् for a sword, ग्रैवेयको\n'
        '  भवत्यलंकारश्चेत् for an ornament. Three bases, three\n'
        '  things the result must BE, matched in order — and each\n'
        '  with the form that stands when it is something else.'
    ),
    '4.2.97': (
        'SETTLED — नद्यादिभ्यो ढक्. नादेयम्, माहेयम्.\n'
        '\n'
        'SETTLED — TWO READINGS OF ONE LIST-ENTRY, AND BOTH ARE\n'
        '  AUTHORITATIVE. पूर्वनगरीशब्दोऽत्र पठ्यते —\n'
        '  पौर्वनगरेयम्; **केचित् तु पूर्वनगिरीति पठन्ति,\n'
        '  विच्छिद्य च प्रत्ययं कुर्वन्ति** — पौरेयम्, वानेयम्,\n'
        '  गैरेयम्, reading the entry as three words and giving\n'
        '  the affix to each. **तदुभयमपि दर्शनं प्रमाणम्**.\n'
        '  4.1.117 gave the same verdict about two readings of a\n'
        '  SŪTRA; this is the same about two readings of a गण.'
    ),
    '4.2.98': (
        'SETTLED — दक्षिणापश्चात्पुरसस्त्यक्. दाक्षिणात्यः, पाश्चात्त्यः,\n'
        '  पौरस्त्यः.'
    ),
    '4.2.99': (
        'SETTLED — कापिश्याः ष्फक्. **षकारो ङीषर्थः** — the ष् so that\n'
        "  4.1.41's ङीष् comes in the feminine: कापिशायनं मधु,\n"
        '  कापिशायनी द्राक्षा. A letter placed a hundred and\n'
        '  fifty-eight sūtras from the rule that spends it.'
    ),
    '4.2.100': (
        'SETTLED — रङ्कोरमनुष्येऽण् च. राङ्कवो गौः; and by the च\n'
        '  राङ्कवायणो गौः. अमनुष्य इति किम्? राङ्कवको मनुष्यः.\n'
        '\n'
        'SETTLED — A NEGATIVE READ AS *LIKE-BUT-NOT* RATHER THAN\n'
        '  AS *NOT*. **नैवायं मनुष्यप्रतिषेधः; किं तर्हि?\n'
        '  नञिवयुक्तन्यायेन मनुष्यसदृशे प्राणिनि प्रतिपत्तिः\n'
        '  क्रियते** — अमनुष्य does not mean *not a man* but *a\n'
        '  living thing RESEMBLING a man*, by the principle that a\n'
        '  नञ् is joined with an *iva*. तेन **राङ्कवः कम्बल** इति\n'
        '  ष्फग् न भवति: a blanket is not a man and not like one\n'
        '  either. A whole class of things excluded by reading a\n'
        '  negative as a comparison.'
    ),
    '4.2.101': (
        'SETTLED — दिक्प्रागपागुदक्प्रतीचो यत्. दिव्यम्, प्राच्यम्,\n'
        '  उदीच्यम्, प्रतीच्यम्. अव्ययात् तु कालवाचिनः परत्वात्\n'
        '  ट्युट्युलौ भवतः — प्राक्तनम्.'
    ),
    '4.2.102': (
        'SETTLED — कन्थायाष्ठक्. कान्थिकः.'
    ),
    '4.2.103': (
        'SETTLED — वर्णौ वुक्, ठकोऽपवादः. **वर्णुर्नाम नदः, तत्समीपो देशो\n'
        '  वर्णुः** — a river, then the country beside it by the\n'
        '  same name, and the rule is about the word कन्था used of\n'
        '  THAT country. जातं हिमवत्सु कान्थकम्.'
    ),
    '4.2.104': (
        'SETTLED — अव्ययात् त्यप्. अमात्यः, इहत्यः, तत्रत्यः.\n'
        '\n'
        'SETTLED — AND A VERSE ENUMERATES WHICH INDECLINABLES,\n'
        '  BECAUSE THE RULE SAYS ONLY *AN INDECLINABLE*.\n'
        '  अमेहक्वतसित्रेभ्यस्त्यब्विधिर्योऽव्ययात् स्मृतः /\n'
        '  निनिर्भ्यां ध्रुवगत्योश्च प्रवेशो नियमे तथा — six\n'
        '  endings named and two prefixes with the senses they\n'
        '  must carry. **परिगणनं किम्?** औपरिष्टः, पौरस्तः,\n'
        '  पारस्तः: without the count those would take it too. A\n'
        '  kārikā doing the work of a गण.\n'
        '\n'
        'NOTE — निसो गते gives **निष्ट्यश्चण्डालादिः**, one gone\n'
        '  out from the orders of life; and आविसश्छन्दसि is cited\n'
        '  to आविष्ट्यो वर्धते (ऋ० १.९५.५).'
    ),
    '4.2.105': (
        'SETTLED — ऐषमोह्यःश्वसोऽन्यतरस्याम्. ऐषमस्त्यम् beside\n'
        '  ऐषमस्तनम्; ह्यस्त्यम्, श्वस्त्यम् likewise — and\n'
        '  **श्वसस्तुट् च इति ठञपि तृतीयो भवति**, शौवस्तिकम्: a\n'
        '  third form for one of the three, from a rule in the\n'
        '  next pāda.'
    ),
    '4.2.106': (
        'SETTLED — तीररूप्योत्तरपदादञ्ञौ, यथासंख्यम्, अणोऽपवादौ.\n'
        '  काकतीरम्, पाल्वलतीरम्; वार्करूप्यम्, शैवरूप्यम्.\n'
        '\n'
        'SETTLED — **तीररूप्यान्तादिति नोक्तम्,\n'
        '  बहुच्प्रत्ययपूर्वाद् मा भूदिति**: the rule says *having\n'
        '  तीर as its LAST MEMBER* and not *ending in तीर*, so a\n'
        '  word merely ending in those sounds is kept out —\n'
        '  बाहुतीरम्, अणेव भवति. Two ways of saying almost the\n'
        '  same thing, and the difference is a class of words.'
    ),
    '4.2.107': (
        'SETTLED — दिक्पूर्वपदादसंज्ञायां ञः, अणोऽपवादः. पौर्वशालः,\n'
        '  दाक्षिणशालः. असंज्ञायामिति किम्? पूर्वैषुकामशमः.\n'
        '  **पदग्रहणं स्वरूपविधिनिरासार्थम्** — the word *member*\n'
        '  is there so the rule is not read of the bare word दिश्.'
    ),
    '4.2.108': (
        'SETTLED — मद्रेभ्योऽञ्. पौर्वमद्रः, आपरमद्रः.\n'
        '  दिशोऽमद्राणाम् इति पर्युदासाद् आदिवृद्धिरेव — a rule\n'
        '  of the seventh chapter excepts this very word by name,\n'
        '  and the exception fixes which member is strengthened.'
    ),
    '4.2.109': (
        'SETTLED — उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात्, अणोऽपवादः.\n'
        '  शैवपुरम्, माण्डवपुरम्. **दिग्ग्रहणं निवृत्तम्**.\n'
        '\n'
        'NOTE — three words and a counter-example each:\n'
        '  माथुरम्, ध्वाजम्, शार्करीधानम् — and the last turns on\n'
        '  an accent placed by a mark on a quite different affix,\n'
        '  **लित्स्वरेण धाशब्द उदात्तः**.'
    ),
    '4.2.110': (
        'SETTLED — प्रस्थोत्तरपदपलद्यादिकोपधादण्. माद्रीप्रस्थः; पालदः;\n'
        '  नैलीनकः. **अण्ग्रहणं बाधकबाधनार्थम्** — the sixth time\n'
        '  in two pādas the default is named to beat what would\n'
        '  have beaten it.\n'
        '\n'
        'NOTE — and the list carries three separate purposes: one\n'
        '  member beats 4.2.117, one beats 4.2.123, and वाहीक is\n'
        '  in it **कोपधोऽपि पुनः पठ्यते परं छं बाधितुम्** — read\n'
        '  again though it already qualifies, in order to beat a\n'
        '  later rule.'
    ),
    '4.2.111': (
        'SETTLED — कण्वादिभ्यो गोत्रे, छस्यापवादः. काण्वाश्छात्राः,\n'
        '  गौकक्षाः.\n'
        '\n'
        'SETTLED — **गोत्रमिह न प्रत्ययार्थो न च\n'
        '  प्रकृतिविशेषणम्**: the word गोत्र here is neither the\n'
        '  sense of the affix nor a qualifier of the base.\n'
        '  तर्ह्येवं संबध्यते — कण्वादिभ्यो गोत्रे यः प्रत्ययो\n'
        '  विहितः, **तदन्तेभ्य एवाण्**: it points at the affix\n'
        '  4.1.111 gave in that sense, and this rule is stated of\n'
        '  stems ending in THAT. **A word in a rule naming neither\n'
        '  a ground nor a sense but another rule.**'
    ),
    '4.2.112': (
        'SETTLED — इञश्च, छस्यापवादः. दाक्षाः, प्लाक्षाः, माहकाः.\n'
        "  गोत्र इत्येव — सौतङ्गमीयम्, where the इञ् is 4.2.80's\n"
        '  and not a lineage-affix at all.'
    ),
    '4.2.113': (
        'SETTLED — न द्व्यचः प्राच्यभरतेषु. पैङ्गीयाः, चैदीयाः, काशीयाः.\n'
        '  द्व्यच इति किम्? पान्नागाराः.\n'
        '\n'
        'SETTLED — AND भरत IS NAMED SEPARATELY BECAUSE OF A\n'
        '  ज्ञापक ELSEWHERE. ज्ञापकाद् **अन्यत्र प्राच्यग्रहणेन\n'
        '  भरतग्रहणं न भवतीति** स्वशब्देन भरतानामुपादानं कृतम् —\n'
        '  2.4.66 teaches that *eastern* does not take in the\n'
        '  Bharatas anywhere else, so this rule must name them in\n'
        '  their own word.\n'
        '\n'
        'NOTE — काशीया इति कथमुदाहृतम्? **देशवाचिनः काशिशब्दस्य\n'
        '  तत्र ग्रहणम्, चेदिशब्देन साहचर्यात्** — the काशि of\n'
        '  4.2.116 is the COUNTRY, known by the company it keeps\n'
        '  in that list. साहचर्य settling which of two homonyms a\n'
        '  gaṇa-entry is, for the fifth time in the project.'
    ),
    '4.2.114': (
        'SETTLED — वृद्धाच्छः, अणोऽपवादः. गार्गीयः, वात्सीयः, शालीयः.\n'
        '  **गोत्र इति नानुवर्तते, सामान्येन विधानम्** — the\n'
        '  lineage stops carrying and the rule is general.\n'
        '\n'
        'NOTE — अव्ययतीररूप्योत्तरपदोदीच्यग्रामकोपधविधींस्तु\n'
        '  **परत्वाद् बाधते**: it beats four earlier rules by\n'
        '  standing later, and the vṛtti names all four.'
    ),
    '4.2.115': (
        'SETTLED — भवतष्ठक्छसौ, छस्यापवादौ. भावत्कः, भवदीयः.\n'
        '  **सकारः पदसंज्ञार्थः**, and भवतस्त्यदादित्वाद्\n'
        '  वृद्धसंज्ञा — the word is वृद्ध not by its own first\n'
        '  vowel but by belonging to the त्यदादि.\n'
        '  अवृद्धात् तु भवतः शतुरणेव भवति — भावतः, where the same\n'
        '  shape is a present participle and takes the default.'
    ),
    '4.2.116': (
        'SETTLED — काश्यादिभ्यष्ठञ्ञिठौ. काशिकी beside काशिका; चैदिकी\n'
        '  beside चैदिका — **स्त्रीप्रत्यये विशेषः**, the two\n'
        '  differ only in the feminine, and ञकार एवोभयत्र\n'
        '  विपर्यस्तदेशोऽनुबन्धः: the same mark on opposite ends\n'
        '  of the two affixes.\n'
        '\n'
        'SETTLED — and the Mahābhāṣya is quoted against the rule:\n'
        '  कथं भाष्य उदाहृतम् — वा नामधेयस्य वृद्धसंज्ञा\n'
        '  वेदितव्या (महाभाष्य १.१.८९)? If a proper name is\n'
        '  OPTIONALLY वृद्ध, then on the option that it is, this\n'
        '  rule would have to apply, and देवदत्तीयाः could not\n'
        '  stand beside दैवदत्ताः.\n'
        '\n'
        '  AND THE ANSWER READS THAT SENTENCE AS A\n'
        '  व्यवस्थितविभाषा. तत्रैवं वर्णयन्ति — **वा नामधेयस्येति\n'
        '  व्यवस्थितविभाषेयम्, सा छे कर्तव्ये भवति, ठञ्ञिठयोर्न\n'
        '  भवति**: the option is DISTRIBUTED, holding where छ is\n'
        '  to be given and not for these two affixes. The\n'
        '  instrument this project first met at 3.4.85, applied\n'
        '  here to a sentence of a commentary rather than to a\n'
        '  word of a sūtra.'
    ),
    '4.2.117': (
        'SETTLED — वाहीकग्रामेभ्यश्च, छस्यापवादौ. शाकलिकी beside शाकलिका;\n'
        '  मान्थविकी beside मान्थविका.'
    ),
    '4.2.118': (
        'SETTLED — विभाषोशीनरेषु. उशीनरेषु ये वाहीकग्रामाः, तद्वाचिभ्यो\n'
        '  वृद्धेभ्यो विभाषा ठञ्ञिठौ. आह्वजालिकी, आह्वजालिका,\n'
        '  आह्वजालीया; सौदर्शनिकी, सौदर्शनिका, सौदर्शनीया —\n'
        '  THREE forms where the last rule gave two, because the\n'
        "  option lets 4.2.114's छ back in beside the two affixes."
    ),
    '4.2.119': (
        'SETTLED — ओर्देशे ठञ्. नैषादकर्षुकः, शाबरजम्बुकः. देश इति किम्?\n'
        '  पटोश्छात्राः पाटवाः.\n'
        '\n'
        'SETTLED — AND A WORD READ TWICE IS A WORD THAT HAD\n'
        '  LAPSED. **वृद्धादिति नानुवर्तते, उत्तरसूत्रे\n'
        '  पुनर्वृद्धग्रहणात्** — वृद्ध stops carrying here, and\n'
        '  the proof offered is that the NEXT rule names it\n'
        '  again. Anuvṛtti argued backwards from a repetition,\n'
        '  which is the cleanest evidence there is for where a\n'
        '  word stops.\n'
        '\n'
        'SETTLED — AND AN AFFIX GIVEN IN A PAIR CANNOT BE CARRIED\n'
        '  ON ALONE. **ठञ्ञिठयोः प्रकरणे ठञः केवलस्यानुवृत्तिर्न\n'
        '  लभ्यत इति ठञ्ग्रहणं कृतम्** — 4.2.116 and 4.2.117 gave\n'
        '  ठञ् and ञिठ together, so this rule has to name ठञ्\n'
        '  itself rather than take it from them. What was joined\n'
        '  in the giving cannot be split in the carrying.'
    ),
    '4.2.120': (
        'SETTLED — वृद्धात् प्राचाम्, ओर्दश इत्येव. आढकजम्बुकः,\n'
        '  शाकजम्बुकः, नापितवास्तुकः.\n'
        '\n'
        'SETTLED — A RULE THAT ADDS NOTHING AND THEREFORE\n'
        '  RESTRICTS. **पूर्वेणैव ठञि सिद्धे नियमार्थं वचनम्** —\n'
        '  4.2.119 gave ठञ् on this ground already, so this rule\n'
        '  can only be a नियम: वृद्धादेव प्राचाम्, among the\n'
        '  eastern countries from a वृद्ध base ONLY. मल्लवास्तु\n'
        '  is not वृद्ध and gives माल्लवास्तवः.'
    ),
    '4.2.121': (
        'SETTLED — धन्वयोपधाद्वुञ्. **धन्वशब्दो मरुदेशवचनः** — धन्व names\n'
        '  a DESERT, so the rule reaches compounds whose last\n'
        '  member is one: पारेधन्वकः, ऐरावतकः. And from a\n'
        '  य-penultimate base: सांकाश्यकः, काम्पिल्यकः.\n'
        '\n'
        'SETTLED — AND THE PENULTIMATE IS NOT THE FINAL. This is\n'
        '  the first rule of the pāda stated on उपधा, the sound\n'
        '  1.1.65 defines as the one before the last. सांकाश्य\n'
        '  does not END in य — it ends in अ — so the table needs\n'
        '  a column of its own for it. Six rules of this run turn\n'
        '  on the penultimate, and storing any of them as a\n'
        '  stem-final would answer for words the rule never\n'
        '  reaches.'
    ),
    '4.2.122': (
        'SETTLED — प्रस्थपुरवहान्ताच्च, छस्यापवादः. **अन्तशब्दः\n'
        '  प्रत्येकमभिसंबध्यते** — *ending* attaches to each of\n'
        '  the three separately and not to the three as one\n'
        '  compound. मालाप्रस्थकः, नान्दीपुरकः, कान्तीपुरकः,\n'
        '  पैलुवहकः, फाल्गुनीवहकः.\n'
        '\n'
        'NOTE — पुरान्तो रोपधः: a word ending in पुर already has\n'
        '  र for its penultimate, so 4.2.123 would have covered\n'
        '  it. **अप्रागर्थमिह ग्रहणम्** — it is named here for\n'
        '  the countries that are not eastern.'
    ),
    '4.2.123': (
        'SETTLED — रोपधेतोः प्राचाम्, छस्यापवादः. Two grounds in one\n'
        '  compound: a र-penultimate base — पाटलिपुत्रकाः,\n'
        '  ऐकचक्रकाः — and an ई-final one, काकन्दी → काकन्दकः,\n'
        '  माकन्दी → माकन्दकः. प्राचामिति किम्? दात्तामित्रीयः.\n'
        '\n'
        'NOTE — **तपरकरणं विस्पष्टार्थम्**: the त appended to\n'
        '  the ई is there only to make the reading plain, and\n'
        '  takes nothing out that would otherwise have been in.'
    ),
    '4.2.124': (
        'SETTLED — जनपदतदवध्योश्च, छस्यापवादः. From a district —\n'
        "  आभिसारकः, आदर्शकः — and from a district's BOUNDARY,\n"
        '  औपुष्टकः, श्यामायनकः. **तदवधिरपि जनपद एव गृह्यते न\n'
        '  ग्रामः**: what the boundary bounds is a district and\n'
        '  not a village.\n'
        '\n'
        'SETTLED — AND THE SECOND WORD IS THERE TO BEAT A LATER\n'
        '  RULE. किमर्थं तर्हि अवधिग्रहणम्? **बाधकबाधनार्थम्** —\n'
        '  गर्तोत्तरपदाच्छं बाधित्वा वुञेव जनपदावधेर्भवति.\n'
        '  4.2.137 gives छ to a compound ending in गर्त, and\n'
        '  त्रिगर्त is one; the boundary is named so that\n'
        '  त्रैगर्तकः stands instead. A rule reaching thirteen\n'
        '  sūtras forward to protect its own ground.'
    ),
    '4.2.125': (
        'SETTLED — अवृद्धादपि बहुवचनविषयात्, जनपदतदवध्योरित्येव;\n'
        '  अण्छयोरपवादः. अङ्गाः → आङ्गकः, वङ्गाः → वाङ्गकः,\n'
        '  कलिङ्गाः → कालिङ्गकः; from boundaries अजमीढाः →\n'
        '  आजमीढकः; and from वृद्ध districts too, दार्वाः →\n'
        '  दार्वकः, कालञ्जराः → कालञ्जरकः.\n'
        '\n'
        'SETTLED — THE MAXIM OF BUTTERMILK FOR KAUṆḌINYA.\n'
        '  **अपिग्रहणं किम्, यावता वृद्धात् पूर्वेणैव सिद्धम्?**\n'
        '  If 4.2.124 already gave वुञ् from a वृद्ध district,\n'
        '  what is *also* doing? **तक्रकौण्डिन्यन्यायेन बाधा मा\n'
        '  विज्ञायीति समुच्चीयते** — so that no one reads this\n'
        '  rule as REPLACING the last one. Telling the servants\n'
        '  to give buttermilk to Kauṇḍinya does not cancel the\n'
        '  milk everyone else was already getting. A च that\n'
        '  gathers instead of displacing, and a named maxim for\n'
        '  the difference.\n'
        '\n'
        'NOTE — **विषयग्रहणमनन्यत्रभावार्थम्**: *domain* is\n'
        '  there so the rule holds only where the plural is the\n'
        "  word's own — जनपदैकशेषबहुत्वे मा भूत्, not where the\n"
        "  plural comes from 1.2.64's एकशेष. वर्तन्यः → वार्तनः."
    ),
    '4.2.126': (
        'SETTLED — कच्छाग्निवक्त्रवर्त्तोत्तरपदात्, छाणोरपवादः.\n'
        '  **उत्तरपदशब्दः प्रत्येकमभिसंबध्यते** — *last member*\n'
        '  attaches to each of the four. दारुकच्छकः,\n'
        '  पैप्पलीकच्छकः; काण्डाग्नकः, वैभुजाग्नकः;\n'
        '  ऐन्द्रवक्त्रकः, सैन्धुवक्त्रकः; बाहुगर्त्तकः,\n'
        '  चाक्रगर्त्तकः. वृद्ध does not carry: the rule takes\n'
        '  **चावृद्धाद् वृद्धात् च**, with the first vowel\n'
        '  lengthened and without.'
    ),
    '4.2.127': (
        'SETTLED — धूमादिभ्यश्च, अणादेरपवादः. धौमकः, खाण्डकः.\n'
        '\n'
        'SETTLED — AND THREE MEMBERS OF THE LIST ARE THERE FOR\n'
        '  SOMETHING ELSE ENTIRELY. पाथेय has य for its\n'
        '  penultimate and 4.2.121 gave वुञ् already, so\n'
        '  **सामर्थ्याददेशार्थं ग्रहणम्** — it is read here to\n'
        '  make the word a COUNTRY-word, which that rule needs it\n'
        '  to be. विदेह and आनर्त the other way about: the\n'
        '  district-rule gave वुञ् already, and **अदेशार्थः\n'
        '  पाठः**, they are read for the sense that is NOT a\n'
        '  country — विदेहानां क्षत्रियाणां स्वं वैदेहकम्,\n'
        '  आनर्तकम्. A list entry can be there to widen a rule\n'
        '  or to narrow one, and the same list holds both.\n'
        '\n'
        'NOTE — समुद्र is read for a narrower thing still,\n'
        '  **तस्य नावि मनुष्ये च वुञिष्यते**. सामुद्रिका नौः,\n'
        '  सामुद्रको मनुष्यः; but सामुद्रं जलम्, and the water\n'
        '  of the sea takes the default.'
    ),
    '4.2.128': (
        'SETTLED — नगरात् कुत्सनप्रावीण्ययोः. कुत्सनं निन्दनम्, प्रावीण्यं\n'
        '  नैपुण्यम् — blame and skill. **प्रत्ययार्थविशेषणं\n'
        '  चैतत्**: the two qualify the SENSE OF THE AFFIX and\n'
        '  not the base. कुत्सनप्रावीण्ययोरिति किम्? नागरा\n'
        '  ब्राह्मणाः.\n'
        '\n'
        'SETTLED — AND THE VṚTTI PUTS A VERSE ON EACH SIDE.\n'
        '  **केनायं मुषितः पन्था गात्रे पक्ष्मालिधूसरः** — who\n'
        '  robbed this traveller, grey with the dust on his\n'
        '  limbs? इह नगरे मनुष्येण संभाव्यत एतन्नागरकेण,\n'
        '  **चोरा हि नागरका भवन्ति**. And **केनेदं लिखितं चित्रं\n'
        '  मनोनेत्रविकाशि यत्** — who painted this picture that\n'
        '  opens the mind and the eye? The same answer, and\n'
        '  **प्रवीणा हि नागरका भवन्ति**. One affix, two verses,\n'
        '  opposite compliments.'
    ),
    '4.2.129': (
        'SETTLED — अरण्यान्मनुष्ये, औपसंख्यानिकस्य णस्यापवादः. आरण्यको\n'
        '  मनुष्यः — a man of the forest.\n'
        '\n'
        'SETTLED — A VĀRTTIKA WIDENS IT TO SIX THINGS.\n'
        '  **पथ्यध्यायन्यायविहारमनुष्यहस्तिष्विति वक्तव्यम्** —\n'
        '  आरण्यकः पन्थाः, आरण्यकोऽध्यायः, आरण्यको न्यायः,\n'
        '  आरण्यको विहारः, आरण्यको हस्ती. A forest ROAD, a\n'
        '  forest LESSON, a forest RULE, a forest pleasure-\n'
        '  ground, a forest elephant. The आरण्यक books of the\n'
        '  Veda are the second of those, and the grammar names\n'
        '  the class before it names any book in it.\n'
        '\n'
        'NOTE — **वा गोमयेषु**, and optionally of cow-dung:\n'
        '  आरण्याः beside आरण्यका गोमयाः. एतेष्विति किम्?\n'
        '  आरण्याः पशवः.'
    ),
    '4.2.130': (
        'SETTLED — विभाषा कुरुयुगन्धराभ्याम्. कौरवकः beside कौरवः;\n'
        '  यौगन्धरकः beside यौगन्धरः.\n'
        '\n'
        'SETTLED — AND THE OPTION TURNS OUT TO BE FOR ONE WORD.\n'
        '  **जनपदशब्दावेतौ** — both are district-words, so\n'
        '  4.2.125 gave वुञ् without an option and the option is\n'
        '  spoken against that. But कुरु is in the कच्छादि list\n'
        '  of 4.2.133 too, **तत्र वचनादणपि भविष्यति**, so अण्\n'
        '  comes by that rule whatever this one says. Which\n'
        '  leaves the option doing real work for युगन्धर alone:\n'
        '  **सैषा युगन्धरार्था विभाषा**.\n'
        '\n'
        'NOTE — 4.2.134 is untouched: from कुरु the वुञ् is\n'
        '  fixed when a man or what stands in him is meant.\n'
        '  कौरवको मनुष्यः, कौरवकमस्य हसितम्.'
    ),
    '4.2.131': (
        'SETTLED — मद्रवृज्योः कन्, जनपदवुञोऽपवादः. मद्रेषु जातो मद्रकः;\n'
        '  वृजिकः. कन् rather than वुञ्, and the two differ only\n'
        '  in the accent they place and in what later rules can\n'
        '  reach them by.'
    ),
    '4.2.132': (
        'SETTLED — कोपधादण्, जनपदवुञोऽपवादः. ऋषिकेषु जातः → आर्षिकः;\n'
        '  माहिषिकः. **अन्यत्र जनपदं मुक्त्वा पूर्वेणैव कोपधादणि\n'
        '  सिद्धम्** — outside the districts 4.2.110 gave अण्\n'
        '  from a क-penultimate base already, so this rule exists\n'
        '  for the districts alone.\n'
        '\n'
        'NOTE — **अण्ग्रहणमुवर्णान्तादपि यथा स्यात्**: the affix\n'
        "  is named so that it beats 4.2.119's ठञ् on a उ-final\n"
        '  base too, where both conditions are met at once.\n'
        '  इक्ष्वाकुषु जात ऐक्ष्वाकः.'
    ),
    '4.2.133': (
        'SETTLED — कच्छादिभ्यश्च, वुञादेरपवादः. काच्छः, सैन्धवः, वार्णवः.\n'
        '\n'
        'SETTLED — AND TWO ENTRIES ARE IN THE LIST FOR THE SAKE\n'
        '  OF LATER RULES. **कच्छशब्दो न बहुवचनविषयः** — कच्छ is\n'
        '  not a plural-domain word, so 4.2.125 never reached it;\n'
        '  **तस्य मनुष्यतत्स्थयोर्वुञर्थः पाठः**, it is here for\n'
        '  the sake of the NEXT rule, which needs the list to\n'
        '  name it. विजापक has क for its penultimate and 4.2.132\n'
        '  gave अण् already: **इह ग्रहणमुत्तरार्थम्**. Two\n'
        '  entries that add nothing where they stand and\n'
        '  everything to what follows.'
    ),
    '4.2.134': (
        'SETTLED — मनुष्यतत्स्थयोर्वुञ्, अणोऽपवादः. काच्छको मनुष्यः;\n'
        '  काच्छकमस्य हसितम्, जल्पितम्; काच्छिका चूडा. सैन्धवको\n'
        '  मनुष्यः, सैन्धविका चूडा. तत्स्थ is **what stands in\n'
        '  the man** — his laughter, his talk, the lock of hair\n'
        '  on his head. मनुष्यतत्स्थयोरिति किम्? काच्छो गौः,\n'
        '  सैन्धवः, वार्णवः: the ox of Kaccha keeps the अण्.'
    ),
    '4.2.135': (
        'SETTLED — अपदातौ साल्वात्. साल्व is in the कच्छादि list, **ततः\n'
        '  पूर्वेणैव मनुष्यतत्स्थयोर्वुञि सिद्धे नियमार्थं\n'
        '  वचनम्** — 4.2.134 gave the वुञ् already, so this rule\n'
        '  can only RESTRICT it: from साल्व the वुञ् comes for a\n'
        '  man who is not a FOOT-SOLDIER. साल्वको मनुष्यः,\n'
        '  साल्वकमस्य हसितम्. अपदाताविति किम्? साल्वः\n'
        '  पदातिर्व्रजति. The second नियम of this run built on\n'
        "  the same argument as 4.2.120's."
    ),
    '4.2.136': (
        'SETTLED — गोयवाग्वोश्च, कच्छाद्यणोऽपवादः. साल्वको गौः; साल्विका\n'
        '  यवागूः — the ox of Sālva and the gruel of Sālva.\n'
        '  **साल्वमन्यत्**: everything else keeps the अण्. The\n'
        '  last rule could not have given these two, because\n'
        '  neither an ox nor a gruel stands in a man.'
    ),
    '4.2.137': (
        'SETTLED — गर्तोत्तरपदाच्छः, अणोऽपवादः. वृकगर्तीयम्,\n'
        '  शृगालगर्तीयम्, श्वाविद्गर्तीयम्. And **वाहीकग्रामलक्षणं\n'
        '  च प्रत्ययं परत्वाद् बाधते**, it beats 4.2.117 by\n'
        '  standing later.\n'
        '\n'
        'NOTE — **उत्तरपदग्रहणं बहुच्पूर्वनिरासार्थम्**: *last\n'
        '  member* is there to keep out a गर्त preceded by बहुच्,\n'
        '  which is a prefix and not a first member at all.\n'
        '  बाहुगर्तम्. And 4.2.124 beats this rule the other way\n'
        "  for a district's boundary, naming the boundary in\n"
        '  order to do it.'
    ),
    '4.2.138': (
        'SETTLED — गहादिभ्यश्च, अणादेरपवादः. गहीयः, अन्तःस्थीयः.\n'
        '\n'
        'SETTLED — A HEADING THAT QUALIFIES ONLY WHAT IT CAN.\n'
        '  **देशाधिकारेऽपि संभवापेक्षं विशेषणम्, न सर्वेषाम्** —\n'
        '  the country-heading stands over this rule, but it\n'
        '  qualifies only the members that COULD be countries.\n'
        '  अङ्ग and वङ्ग and मगध are in the list; so are\n'
        '  पूर्वपक्ष and उत्तमशाख, which are not places at all.\n'
        '  A condition applied where it fits and dropped where it\n'
        '  cannot.\n'
        '\n'
        'NOTE — five गणसूत्र ride with the list. **मध्य मध्यमं\n'
        '  चाण् चरणे** — मध्य becomes मध्यम when the affix comes,\n'
        '  मध्यमीयाः, but in the sense of a school it takes अण्,\n'
        '  माध्यमाः. **मुखपार्श्वतसोर्लोपः** drops the तस्:\n'
        '  मुखतीयम्, पार्श्वतीयम्. **जनपरयोः कुक् च** inserts क —\n'
        '  जनकीयम्, परकीयम् — and **देवस्य च** adds देवकीयम्.\n'
        '  **वेणुकादिभ्यश्छण्** gives छण्, वैणुकीयम्, वैत्रकीयम्.\n'
        '  **आकृतिगणोऽयम्**, and the list is open.'
    ),
    '4.2.139': (
        'SETTLED — प्राचां कटादेः, अणोऽपवादः. कटनगरीयम्, कटघोषीयम्,\n'
        '  कटपल्वलीयम् — the कट-towns of the east, and the\n'
        '  eastern qualification is on the country and not on the\n'
        '  list.'
    ),
    '4.2.140': (
        'SETTLED — राज्ञः क च. राजकीयम्.\n'
        '\n'
        'SETTLED — AND THE RULE GIVES NO AFFIX AT ALL.\n'
        '  आदेशमात्रमिह विधेयम्, **प्रत्ययस्तु वृद्धाच्छ इत्येव\n'
        '  सिद्धः** — only the substitute क is enjoined here; the\n'
        "  छ was already 4.2.114's, since राजन् has आ for its\n"
        '  first vowel and is वृद्ध by 1.1.73. The च gathers this\n'
        '  rule onto that one instead of replacing it.\n'
        '\n'
        "  The code says the same thing by FETCHING 4.2.114's own\n"
        '  answer instead of naming छ a second time. A rule that\n'
        '  supplies a substitute and leaves the affix standing is\n'
        '  the first of its kind in this table, and the row names\n'
        '  the rule it leans on rather than copying its result.\n'
        '\n'
        'NOTE — **असंभवाद् देशाधिकारो न विशेषणम्**: the\n'
        '  country-heading cannot qualify this base, because a\n'
        '  king is not a place.'
    ),
    '4.2.141': (
        'SETTLED — वृद्धादकेकान्तखोपधात्, three rules beaten at once — the\n'
        '  कोपध अण् of 4.2.132, the वाहीकग्राम affix of 4.2.117,\n'
        '  and रोपधेतोः प्राचाम्. From अक: आरीहणकीयम्,\n'
        '  द्रौघणकीयम्. From इक: आश्वपथिकीयम्, शाल्मलिकीयम्.\n'
        '  From a ख-penultimate base: कौटिशिखीयम्, आयोमुखीयम्.\n'
        '\n'
        'NOTE — **अकेकान्तग्रहणे कोपधग्रहणं सौसुकाद्यर्थम्**: a\n'
        '  vārttika reads क for the penultimate beside the two\n'
        '  endings, for words like सौसुक that have neither.\n'
        '  सौसुकीयम्, मौसुकीयम्, ऐन्द्रवेणुकीयम्.'
    ),
    '4.2.142': (
        'SETTLED — कन्थापलदनगरग्रामह्रदोत्तरपदात्, वाहीकग्रामादिलक्षणस्य\n'
        '  प्रत्ययस्यापवादः. दाक्षिकन्थीयम्, माहिकिकन्थीयम्;\n'
        '  दाक्षिपलदीयम्; दाक्षिनगरीयम्; दाक्षिग्रामीयम्;\n'
        '  दाक्षिह्रदीयम् — five last members, each shown with\n'
        '  the same two first members, so that what varies in the\n'
        '  examples is exactly what the rule is about.'
    ),
    '4.2.143': (
        'SETTLED — पर्वताच्च, अणोऽपवादः. पर्वतीयो राजा, पर्वतीयः पुरुषः —\n'
        '  the king of the mountain and the man of the mountain.'
    ),
    '4.2.144': (
        'SETTLED — विभाषाऽमनुष्ये. **पूर्वेण नित्ये प्राप्ते विकल्प\n'
        '  उच्यते** — the last rule gave छ without an option, so\n'
        '  the option is spoken here. पर्वतीयानि फलानि beside\n'
        '  पार्वतानि फलानि; पर्वतीयमुदकम् beside पार्वतमुदकम्.\n'
        '  अमनुष्य इति किम्? पर्वतीयो मनुष्यः, where the छ is\n'
        '  fixed again — the option is for everything BUT the\n'
        '  man, which is the reverse of 4.2.129 and 4.2.134.'
    ),
    '4.2.145': (
        'SETTLED — कृकणपर्णाद्भारद्वाजे. कृकणीयम्, पर्णीयम्. भारद्वाज\n'
        '  इति किम्? कार्कणम्, पार्णम्.\n'
        '\n'
        'SETTLED — TWO WARNINGS ABOUT ONE WORD.\n'
        '  **भारद्वाजशब्दोऽपि देशवचन एव, न गोत्रशब्दः** —\n'
        '  भारद्वाज here is the COUNTRY and not the lineage,\n'
        '  though the same word is among the most famous gotras\n'
        '  there is; and **प्रकृतिविशेषणं चैतत्, न\n'
        '  प्रत्ययार्थः**, it qualifies the base rather than\n'
        '  being what the affix means. Both warnings are needed,\n'
        '  and neither would have been guessed.\n'
        '\n'
        'NOTE — the pāda closes here: **इति श्रीजयादित्यविरचितायां\n'
        '  काशिकायां वृत्तौ चतुर्थाध्यायस्य द्वितीयः पादः**.'
    ),
}

_CASE_RUN = ()

_IN_SENSE_LINE = (
    'in_sense(stem, gana=..., case=..., sense=..., result=..., '
    'samjna=..., unspecified=..., wants=...) -> which affix comes in '
    'the sense, from a base in that case.'
)

#: Every rule of this pāda that names no affix falls to 4.1.83, and
#: `in_sense` says so by RETURNING that rule's answer. The same
#: fall-through the 4.1 patronymics declared, and here it is the
#: normal case rather than the exception: eight of these twenty-one
#: rules give no affix at all.
_REUSES = {
    "4.2.1": ("4.1.83",),
    "4.2.3": ("4.1.83",),
    "4.2.7": ("4.1.83",),
    "4.2.10": ("4.1.83",),
    "4.2.14": ("4.1.83",),
    "4.2.16": ("4.1.83",),
    "4.2.24": ("4.1.83",),
    "4.2.34": ("4.1.83",),
    "4.2.37": ("4.1.83",),
    "4.2.52": ("4.1.83",),
    "4.2.55": ("4.1.83",),
    "4.2.56": ("4.1.83",),
    "4.2.59": ("4.1.83",),
    "4.2.67": ("4.1.83",),
    "4.2.68": ("4.1.83",),
    "4.2.69": ("4.1.83",),
    "4.2.70": ("4.1.83",),
    "4.2.92": ("4.1.83",),
    #: 4.2.34 कालेभ्यो भववत् borrows the affixes 4.3.11 onward
    #: gives. When it was codified those rules did not exist and
    #: the row fell to the default; they exist now, and the
    #: अतिदेश is executed rather than described.
    "4.2.34": ("4.3.11",),
}

for _sutra, _notes in _RULES.items():
    register(
        _sutra,
        apply=in_sense,
        codification=_IN_SENSE_LINE,
        notes=_notes,
        reuses=_REUSES.get(_sutra, ()),
    )
