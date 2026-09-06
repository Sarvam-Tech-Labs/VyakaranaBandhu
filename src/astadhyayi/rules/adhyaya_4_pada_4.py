# -*- coding: utf-8 -*-
"""
अध्याय ४, पाद ४ — प्राग्वहतेष्ठक्, and the senses are actions.

4.1.83 प्राग्दीव्यतोऽण् put अण् over the whole taddhita section up to
the rule that names दीव्यति. That rule is 4.4.2, and this pāda opens
one sūtra before it by putting ठक् over everything from here to
4.4.76. The two great headings meet exactly at the join, and each is
bounded by lifting one word out of the sūtra it stops at.

From 4.4.2 the question changes too. The three pādas before asked
whose descendant a man was, where a thing came from, what it was made
of. Here it is what someone DOES by means of the thing — and the base
stands in the instrumental to say so.
"""

from __future__ import annotations

from src.astadhyayi.sources import register
from src.astadhyayi.thak import by_means_of

_RULES = {
    '4.4.1': (
        'SETTLED — प्राग्वहतेष्ठक्. **तद्वहति रथयुगप्रासङ्गम् इति\n'
        '  वक्ष्यति; प्रागेतस्माद् वहतिसंशब्दनाद्\n'
        '  यानर्थाननुक्रमिष्यामः, ठक् प्रत्ययस्तेष्वधिकृतो\n'
        '  वेदितव्यः** — ठक् is the affix for every sense named\n'
        '  between here and 4.4.76, unless a rule says otherwise.\n'
        '  अक्षैर्दीव्यति **आक्षिकः**.\n'
        '\n'
        'SETTLED — AND THE TWO GREAT HEADINGS MEET AT 4.4.2.\n'
        '  4.1.83 प्राग्दीव्यतोऽण् put अण् over the whole\n'
        '  taddhita section up to the rule that names दीव्यति,\n'
        '  and that rule is the next one. Each heading is bounded\n'
        '  by lifting ONE WORD out of the sūtra it stops at —\n'
        '  दीव्यति out of 4.4.2, वहति out of 4.4.76 — so the two\n'
        '  boundaries are the two halves of a single join, and\n'
        '  the whole taddhita section is divided between two\n'
        '  affixes at that point.\n'
        '\n'
        'SETTLED — BUT THE MARKER IS NOT THE LAST RULE. 4.4.75\n'
        '  प्राग्घिताद् यत् opens a heading of its own INSIDE\n'
        '  this range, so ठक् never reaches it; and 4.4.74\n'
        '  closes the account in as many words — **ठकः पूर्णो\n'
        '  ऽवधिः, अतः परमन्यः प्रत्ययो विधीयते**. The word\n'
        '  वहति marks the boundary from 4.4.76, and the last\n'
        '  rule the heading governs is 4.4.74. Two sūtras\n'
        '  apart, and nothing in the project had shown the\n'
        '  two could come apart until a second heading opened\n'
        '  inside the first.\n'
        '\n'
        'NOTE — four vārttikas add senses the sūtras do not name.\n'
        '  **ठक्प्रकरणे तदाहेति माशब्दादिभ्य उपसंख्यानम्** —\n'
        '  माशब्द इत्याह **माशब्दिकः**, one who says *no*, and\n'
        '  **वाक्यादेतत् प्रत्ययविधानम्**, the affix given from a\n'
        '  whole SENTENCE. **आहौ प्रभूतादिभ्यः** — प्राभूतिकः,\n'
        '  **क्रियाविशेषणात् प्रत्ययः**. **पृच्छतौ\n'
        '  सुस्नातादिभ्यः** — सुस्नातं पृच्छति सौस्नातिकः, one\n'
        "  who asks after another's bath. **गच्छतौ\n"
        '  परदारादिभ्यः** — **पारदारिकः**.'
    ),
    '4.4.2': (
        'SETTLED — तेन दीव्यति खनति जयति जितम्. Four senses in one rule.\n'
        '  अक्षैर्दीव्यति **आक्षिकः**, a dicer; अभ्र्या खनति\n'
        '  **आभ्रिकः**; अक्षैर्जयति आक्षिकः; अक्षैर्जितम्\n'
        '  **आक्षिकम्** — and the fourth is a PARTICIPLE where\n'
        '  the other three are finite verbs.\n'
        '\n'
        'SETTLED — AND THE INSTRUMENTAL IS ALWAYS THE INSTRUMENT.\n'
        '  **सर्वत्र करणे तृतीया समर्थविभक्तिः** — never the\n'
        '  agent. देवदत्तेन जितमिति प्रत्ययो न भवति,\n'
        '  **अनभिधानात्**: *won by Devadatta* takes nothing,\n'
        '  because that is not how the language says it. And\n'
        '  अङ्गुल्या खनतीति च — nor *digs with a finger*, though\n'
        '  a finger is an instrument.\n'
        '\n'
        'SETTLED — AND A TADDHITA FOREGROUNDS THE MEANS WHERE A\n'
        '  VERB FOREGROUNDS THE ACTION. **क्रियाप्रधानत्वेऽपि\n'
        '  चाख्यातस्य तद्धितः स्वभावात् साधनप्रधानः** — the\n'
        '  clearest statement in this section of what its affixes\n'
        '  are for. अक्षैर्दीव्यति is a sentence about playing;\n'
        '  आक्षिकः is a word about the dice.\n'
        '\n'
        'NOTE — **प्रत्ययार्थे संख्याकालयोरविवक्षा**: number and\n'
        '  time are not meant by the affix, so one form serves\n'
        '  however many dice and whenever the playing was.'
    ),
    '4.4.3': (
        'SETTLED — संस्कृतम्. **सत उत्कर्षाधानं संस्कारः** — a refinement\n'
        '  is the raising of something that already IS. दध्ना\n'
        '  संस्कृतं **दाधिकम्**; शार्ङ्गवेरिकम्, मारिचिकम्.\n'
        '\n'
        'NOTE — **योगविभाग उत्तरार्थः**, split off for the sake\n'
        '  of the next rule. The pāda before used the device five\n'
        '  times.'
    ),
    '4.4.4': (
        'SETTLED — कुलत्थकोपधादण्, ठकोऽपवादः. कुलत्थैः संस्कृतं\n'
        '  **कौलत्थम्**; and from a base with क for its\n'
        '  penultimate, तैत्तिडीकम्, दार्दभकम् — the third pāda\n'
        '  running to state a rule on the उपधा.'
    ),
    '4.4.5': (
        'SETTLED — तरति. **तरति प्लवत इत्यर्थः** — crosses, floats.\n'
        '  काण्डप्लवेन तरति **काण्डप्लविकः**; औडुपिकः, one who\n'
        '  crosses by a raft.'
    ),
    '4.4.6': (
        'SETTLED — गोपुच्छाट् ठञ्, ठकोऽपवादः. **स्वरे विशेषः** — the two\n'
        '  affixes differ in the accent and in nothing else.\n'
        '  **गौपुच्छिकः**, one who crosses a river holding a\n'
        "  cow's tail."
    ),
    '4.4.7': (
        'SETTLED — नौद्व्यचष्ठन्, ठकोऽपवादः. नावा तरति **नाविकः**, a\n'
        '  sailor; and from a two-vowel base घटिकः, प्लविकः,\n'
        '  बाहुकः — one who crosses by a pot, a float, his own\n'
        '  arms. **षकारः सांहितिको नानुबन्धः**: the ष् in the\n'
        '  sūtra is there by sandhi and is no marker, so the\n'
        '  feminine is बाहुका and not बाहुकी.\n'
        '\n'
        'SETTLED — AND A KĀRIKĀ COUNTS THE ष-AFFIXES OF THE WHOLE\n'
        '  SECTION, THEN CORRECTS ITSELF.\n'
        '\n'
        '      आकर्षात् पर्पादेर्भस्त्रादिभ्यः कुसीदसूत्राच्च ।\n'
        '      आवसथात् किशरादेः **षितः षडेते ठगधिकारे** ॥\n'
        '\n'
        '  Six of them, from six named grounds. And then:\n'
        '  **विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु सप्त** —\n'
        '  six as far as the rule-STATEMENTS go, but seven\n'
        '  affixes, because one of the six rules gives two. A\n'
        '  count offered and at once qualified by saying what it\n'
        '  is a count of.'
    ),
    '4.4.8': (
        'SETTLED — चरति. **चरतिर्भक्षणे गतौ च वर्तते** — चर् is both eating\n'
        '  and going, so one rule covers both. दध्ना चरति\n'
        '  **दाधिकः**, one who takes his food with curds;\n'
        '  हास्तिकः, शाकटिकः, one who travels by elephant or by\n'
        '  cart.'
    ),
    '4.4.9': (
        'SETTLED — आकर्षात् ष्ठल्, ठकोऽपवादः. **लकारः स्वरार्थः, षकारो\n'
        '  ङीषर्थः** — the ल् for the accent and the ष् for the\n'
        '  feminine. आकर्षेण चरति **आकर्षिकः**, आकर्षिकी.\n'
        '\n'
        'NOTE — **आकर्ष इति सुवर्णपरीक्षार्थो निकषोपल उच्यते**:\n'
        '  an आकर्ष is the touchstone one tests gold on, and the\n'
        '  derived word is the man who goes about with one. The\n'
        '  first of the six the kārikā at 4.4.7 counts.'
    ),
    '4.4.10': (
        'SETTLED — पर्पादिभ्यः ष्ठन्, ठकोऽपवादः. **नकारः स्वरार्थः,\n'
        '  षकारो ङीषर्थः**. पर्पिकः, पर्पिकी; अश्विकः, अश्विकी.\n'
        '  A गणसूत्र rides with the list — **पादः पच्च** — and\n'
        '  पाद gives पदिकः. The second of the six.'
    ),
    '4.4.11': (
        'SETTLED — श्वगणाट् ठञ् च, ठकोऽपवादः; the च bringing ष्ठन् along.\n'
        '  श्वगणेन चरति **श्वागणिकः**, श्वागणिकी, a man who goes\n'
        '  about with a pack of dogs; and by the ष्ठन् श्वगणिकः,\n'
        '  श्वगणिकी.\n'
        '\n'
        'SETTLED — AND A VĀRTTIKA IN THE SEVENTH CHAPTER IS\n'
        '  WRITTEN FOR THIS WORD. श्वादेरिञि [7.3.8] इत्यत्र\n'
        '  वक्ष्यति — **इकारादिग्रहणं च कर्तव्यं\n'
        '  श्वागणिकाद्यर्थम्**, and **तेन ठञि द्वारादिकार्यं न\n'
        '  भवति**: the supplement is added there so that the\n'
        '  द्वारादि operation shall not reach the form this rule\n'
        '  makes. A rule three chapters away amended on account\n'
        '  of one derivation here.'
    ),
    '4.4.12': (
        'SETTLED — वेतनादिभ्यो जीवति. वेतनेन जीवति **वैतनिकः कर्मकरः**, a\n'
        '  hired workman — one who lives by his wage.\n'
        '\n'
        'NOTE — **धनुर्दण्डग्रहणमत्र संघातविगृहीतार्थम्**:\n'
        '  धनुर्दण्ड is in the list so that the rule reaches the\n'
        '  COMPOUND and each of its MEMBERS — धानुर्दण्डिकः,\n'
        '  **धानुष्कः**, दाण्डिकः. The bowman and the\n'
        '  staff-bearer out of a single entry.'
    ),
    '4.4.13': (
        'SETTLED — वस्नक्रयविक्रयाट् ठन्, ठकोऽपवादः. वस्नेन जीवति\n'
        '  **वस्निकः**. **क्रयविक्रयग्रहणं संघातविगृहीतार्थम्**\n'
        "  — the same device as the last rule's, and the same\n"
        '  three forms: क्रयविक्रयिकः, क्रयिकः, विक्रयिकः. A\n'
        '  trader in both, a buyer, a seller.'
    ),
    '4.4.14': (
        'SETTLED — आयुधाच्छ च — the छ, and by the च the ठक् as well, so\n'
        '  both stand. आयुधेन जीवति **आयुधीयः**, **आयुधिकः**:\n'
        '  one who lives by arms.'
    ),
    '4.4.15': (
        'SETTLED — हरत्युत्सङ्गादिभ्यः, तेनेत्येव. **हरतिर्देशान्तर-\n'
        '  प्रापणे वर्तते** — हृ here is carrying from one place\n'
        '  to another. उत्सङ्गेन हरति **औत्सङ्गिकः**, one who\n'
        '  carries in his lap; औडुपिकः.'
    ),
    '4.4.16': (
        'SETTLED — भस्त्रादिभ्यः ष्ठन्. भस्त्रया हरति **भस्त्रिकः**,\n'
        '  भस्त्रिकी, one who carries in a leather bag; भरटिकः,\n'
        '  भरटिकी. The third of the six the kārikā counts.'
    ),
    '4.4.17': (
        'SETTLED — विभाषा विवधवीवधात्, हरतीत्येव. **तेन मुक्ते प्रकृतष्ठग्\n'
        '  भवति** — where the option lets this affix go, the ठक्\n'
        '  of the heading comes back. विवधिकः and वैवधिकः both.\n'
        '\n'
        'NOTE — **विवधवीवधशब्दौ समानार्थौ पथि पर्याहारे च\n'
        '  वर्तेते**: the two words mean the same thing and\n'
        '  denote both a road and a carrying-pole.'
    ),
    '4.4.18': (
        'SETTLED — अण् कुटिलिकायाः, हरतीत्येव. **कुटिलिका वक्रगतिः,\n'
        '  कर्माराणामायुधकर्षणी लोहमयी यष्टिश्चोच्यते** — a\n'
        '  कुटिलिका is a crooked movement, and also the iron rod\n'
        '  a smith draws his work with.\n'
        '\n'
        '  So one base gives two quite different men. कुटिलिकया\n'
        '  हरति मृगो व्याधं **कौटिलिको मृगः**, the deer that\n'
        '  carries the hunter off by its swerving; and कुटिलिकया\n'
        '  हरत्यङ्गारान् **कौटिलिकः कर्मारः**, the smith who\n'
        '  draws the coals with his rod. Two readings of one\n'
        '  word, and the derived form is the same in both.'
    ),
    '4.4.19': (
        'SETTLED — निर्वृत्तेऽक्षद्यूतादिभ्यः, तेनेत्येव. अक्षद्यूतेन\n'
        '  निर्वृत्तम् **आक्षद्यूतिकं वैरम्**, a feud brought\n'
        '  about by a game of dice; जानुप्रहृतिकम्, one caused by\n'
        '  a blow with the knee. The list is a catalogue of\n'
        '  quarrels and how they start.'
    ),
    '4.4.20': (
        'SETTLED — क्त्रेर्मम् नित्यम्, निर्वृत्त इत्येव. **ड्वितः क्त्रिः**\n'
        '  [3.3.88] इत्ययं त्रिशब्दो गृह्यते — the त्रि meant is\n'
        '  the affix that rule gives. डुपचष् पाके: **पक्त्रिमम्**;\n'
        '  डुवप्: उप्त्रिमम्; डुकृञ्: **कृत्रिमम्**, artificial.\n'
        '\n'
        "SETTLED — AND *ALWAYS* TAKES AWAY THE WORD'S\n"
        '  INDEPENDENCE. **नित्यग्रहणं\n'
        '  स्वातन्त्र्यनिवृत्त्यर्थम्; तेन त्र्यन्तं नित्यं\n'
        '  मप्प्रत्ययान्तमेव भवति, विषयान्तरे न प्रयोक्तव्यम्**\n'
        '  — a stem ending in that क्त्रि must ALWAYS carry this\n'
        '  affix and may not be used anywhere without it. Not a\n'
        '  rule about when an affix comes but about a word that\n'
        '  cannot stand alone.\n'
        '\n'
        'NOTE — **भावप्रत्ययान्तादिमब् वक्तव्यः**: पाकेन\n'
        '  निर्वृत्तं पाकिमम्; त्यागिमम्, सेकिमम्, कुट्टिमम्.'
    ),
    '4.4.21': (
        'SETTLED — अपमित्ययाचिताभ्यां कक्कनौ, यथासंख्यम्. **आपमित्यकम्**,\n'
        '  what has been brought about by borrowing;\n'
        '  **याचितकम्**, by asking. Two bases and two affixes\n'
        '  matched in order, and the two affixes differ in a\n'
        '  single letter.'
    ),
    '4.4.22': (
        'SETTLED — संसृष्टे, तेनेत्येव. **संसृष्टमेकीभूतमभिन्नम्\n'
        '  इत्यर्थः** — mixed, become one, no longer separable.\n'
        '  दध्ना संसृष्टं **दाधिकम्**; मारिचिकम्,\n'
        '  शार्ङ्गवेरिकम्, पैप्पलिकम् — food mixed with curds,\n'
        '  pepper, ginger, long pepper.'
    ),
    '4.4.23': (
        'SETTLED — चूर्णादिनिः, ठकोऽपवादः. चूर्णैः संसृष्टाः **चूर्णिनो\n'
        '  ऽपूपाः**, cakes mixed with powder; चूर्णिनो धानाः.'
    ),
    '4.4.24': (
        'SETTLED — लवणाल्लुक्. **संसृष्ट इत्यनेनोत्पन्नस्य ठको लवणशब्दाद्\n'
        '  लुग् भवति** — the ठक् given in this sense goes after\n'
        '  लवण. **लवणः सूपः**, salted soup; लवणं शाकम्, लवणा\n'
        '  यवागूः.\n'
        '\n'
        "SETTLED — AND ONLY ONE OF THE WORD'S TWO SENSES CAUSES\n"
        '  IT. **द्रव्यवाची लवणशब्दो लुकं प्रयोजयति, न\n'
        '  गुणवाची** — where लवण names the SUBSTANCE salt the\n'
        '  affix goes; where it names the QUALITY of being salty\n'
        '  it does not. A homonym split by which of its two\n'
        '  meanings is in play, and the visible form differs.'
    ),
    '4.4.25': (
        'SETTLED — मुद्गादण्, ठकोऽपवादः. **मौद्ग ओदनः**, rice mixed with\n'
        '  beans; मौद्गी यवागूः.'
    ),
    '4.4.26': (
        'SETTLED — व्यञ्जनैरुपसिक्ते, तेनेत्येव. From any word for a\n'
        '  SEASONING, in the sense *sprinkled with it*. दध्ना\n'
        '  उपसिक्तं **दाधिकम्**; सौपिकम्, खारिकम्.\n'
        '\n'
        'NOTE — व्यञ्जनैरिति किम्? **उदकेनोपसिक्त ओदनः** — rice\n'
        '  sprinkled with water takes nothing, water being no\n'
        '  seasoning.'
    ),
    '4.4.27': (
        'SETTLED — ओजःसहोऽम्भसा वर्तते. ओजसा वर्तते **औजसिकः शूरः**, a\n'
        '  hero who goes by his strength; **साहसिकश्चौरः**, a\n'
        '  robber who goes by force; **आम्भसिको मत्स्यः**, a\n'
        '  fish that goes by water. Three words, three\n'
        '  creatures, each named by what it lives on.'
    ),
    '4.4.28': (
        'SETTLED — तत् प्रत्यनुपूर्वमीपलोमकूलम्. **तदिति\n'
        '  द्वितीयासमर्थविभक्तिः** — and here the case changes to\n'
        '  the ACCUSATIVE, the first time in this pāda. प्रतीपं\n'
        '  वर्तते **प्रातीपिकः**, one who goes against the\n'
        '  stream; आन्वीपिकः, with it; प्रातिलोमिकः and\n'
        '  आनुलोमिकः, against and with the grain; प्रातिकूलिकः\n'
        '  and आनुकूलिकः, against and with the bank. Three words\n'
        '  and two prefixes, so six forms in opposed pairs.\n'
        '\n'
        'SETTLED — AND AN INTRANSITIVE VERB GIVEN AN OBJECT.\n'
        '  ननु च वृतिरकर्मकः, तस्य कथं कर्मणा संबन्धः? — वृत्\n'
        '  takes no object, so how can there be an accusative\n'
        '  with it? **क्रियाविशेषणमकर्मकाणामपि कर्म भवति**:\n'
        '  what QUALIFIES the action counts as an object even for\n'
        '  a verb that has none. Which is what lets the case\n'
        '  change here at all.'
    ),
    '4.4.29': (
        'SETTLED — परिमुखं च. परिमुखं वर्तते **पारिमुखिकः**.\n'
        '  **चकारोऽनुक्तसमुच्चयार्थः** — the च gathers what has\n'
        '  not been said, so पारिपार्श्विकः comes in as well: an\n'
        "  attendant who keeps at one's side."
    ),
    '4.4.30': (
        'SETTLED — प्रयच्छति गर्ह्यम्, तदित्येव — and only where what is\n'
        '  given is BLAMEWORTHY. **द्विगुणार्थं द्विगुणम्,\n'
        '  तादर्थ्यात् ताच्छब्द्यम्**: *double* stands for *for\n'
        '  the sake of double*, a word taking the name of what it\n'
        '  is for. द्विगुणं प्रयच्छति **द्वैगुणिकः**, a usurer\n'
        '  who lends at double; त्रैगुणिकः.\n'
        '\n'
        'NOTE — a vārttika supplies another shape:\n'
        '  **वृद्धेर्वृधुषिभावो वक्तव्यः** — **वार्धुषिकः**; and\n'
        '  **प्रकृत्यन्तरं वा वृद्धिपर्यायो वृधुषिशब्दः**, or\n'
        '  else वृधुषि is simply another word for interest.\n'
        '\n'
        'NOTE — गर्ह्यमिति किम्? **द्विगुणं प्रयच्छत्यधमर्णः**:\n'
        '  the DEBTOR who repays double does nothing\n'
        '  blameworthy, and gets no affix. One transaction, two\n'
        '  parties, and the affix reaches only the one at fault.'
    ),
    '4.4.31': (
        'SETTLED — कुसीददशैकादशात् ष्ठन्ष्ठचौ, यथासंख्यम्; ठकोऽपवादौ.\n'
        '  **कुसीदं वृद्धिः, तदर्थं द्रव्यं कुसीदम्** — कुसीद is\n'
        '  interest, and by transfer the capital lent for it.\n'
        '  **एकादशार्था दश दशैकादशशब्देनोच्यते** — ten lent for\n'
        '  eleven, the whole transaction in one word. कुसीदिकः,\n'
        '  **दशैकादशिकः**.\n'
        '\n'
        "SETTLED — AND THIS IS THE RULE THAT MAKES 4.4.7's COUNT\n"
        '  SEVEN. That kārikā named six grounds for the\n'
        '  ष-initial affixes of the section and then corrected\n'
        '  itself: **विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु\n'
        '  सप्त**, six statements but seven affixes. This is the\n'
        "  statement that gives two, and the verse's count can\n"
        '  now be checked rather than read.'
    ),
    '4.4.32': (
        'SETTLED — उञ्छति, तदिति द्वितीयासमर्थात्. **भूमौ पतितस्यैकैकस्य\n'
        '  कणस्योपादानमुञ्छः** — gleaning is taking up the\n'
        '  fallen grains one by one. बदराण्युञ्छति\n'
        '  **बादरिकः**; श्यामाकिकः, काणिकः.'
    ),
    '4.4.33': (
        'SETTLED — रक्षति. समाजं रक्षति **सामाजिकः**, one who keeps order\n'
        '  at an assembly; सांनिवेशिकः.'
    ),
    '4.4.34': (
        'SETTLED — शब्ददर्दुरं करोति. शब्दं करोति **शाब्दिको वैयाकरणः** —\n'
        '  *one who makes words* is the grammarian, and the\n'
        '  grammar names its own practitioner by a rule of its\n'
        '  own. **दार्दुरिकः कुम्भकारः**, the potter who makes\n'
        '  the drum.'
    ),
    '4.4.35': (
        'SETTLED — पक्षिमत्स्यमृगान् हन्ति. पाक्षिकः, मात्स्यिकः,\n'
        '  मार्गिकः — the fowler, the fisherman, the hunter.\n'
        '\n'
        'SETTLED — AND A NAME REACHES ITS SYNONYMS AND ITS\n'
        '  SPECIES. **स्वरूपस्य पर्यायाणां तद्विशेषाणां च\n'
        '  ग्रहणमिहेष्यते** — the word itself, the words that\n'
        '  mean the same, and the words for KINDS of the thing.\n'
        '  From पक्षिन् come **शाकुनिकः** by a synonym and\n'
        '  मायूरिकः, तैत्तिरिकः by species; from मत्स्य,\n'
        '  मैनिकः, शाफरिकः, शाकुलिकः; from मृग, हारिणिकः,\n'
        '  सौकरिकः, सारङ्गिकः. Three words in the rule, and a\n'
        '  whole vocabulary of hunters out of them.'
    ),
    '4.4.36': (
        'SETTLED — परिपन्थं च तिष्ठति. परिपन्थं तिष्ठति **पारिपन्थिकश्\n'
        '  चौरः** — the robber who waits on the road.\n'
        '\n'
        'SETTLED — A च OUT OF ITS PLACE GATHERING A SECOND\n'
        '  SENSE. **चकारो भिन्नक्रमः प्रत्ययार्थं समुच्चिनोति**\n'
        '  — so परिपन्थं हन्ति पारिपन्थिकः as well: one who\n'
        '  STRIKES on the road and not only one who waits there.\n'
        '\n'
        'SETTLED — AND A CASE RESTATED INSIDE ITS OWN SECTION,\n'
        '  WHICH IS READ AS EVIDENCE. **समर्थविभक्तिप्रकरणे\n'
        '  पुनर्द्वितीयोच्चारणं लौकिकवाक्यप्रदर्शनार्थम्** —\n'
        '  the accusative is uttered again to show the everyday\n'
        '  sentence; and **परिपथशब्दपर्यायः परिपन्थशब्दो\n'
        '  ऽस्तीति ज्ञापयति**, which indicates that परिपन्थ is\n'
        '  a synonym of परिपथ — **स विषयान्तरेऽपि\n'
        '  प्रयोक्तव्यः**, and may be used elsewhere too.'
    ),
    '4.4.37': (
        'SETTLED — माथोत्तरपदपदव्यनुपदं धावति. दण्डमाथं धावति\n'
        '  **दाण्डमाथिकः**; शौल्कमाथिकः; **पादविकः**, one who\n'
        '  runs on the track; **आनुपदिकः**, one who runs at\n'
        "  another's heels. **माथशब्दः पथिपर्यायः** — माथ is\n"
        '  another word for a road.'
    ),
    '4.4.38': (
        'SETTLED — आक्रन्दाट् ठञ् च — the ठञ्, and by the च the ठक् too;\n'
        '  **स्वरे विशेषः**. **आक्रन्दिकः**, आक्रन्दिकी.\n'
        '\n'
        'NOTE — the base is read two ways and both are kept.\n'
        '  **आक्रन्दन्त्येतस्मिन्नित्याक्रन्दो देशः** — a place\n'
        '  where people cry out; **अथवाक्रन्द्यत इत्याक्रन्द\n'
        '  आर्तायनमुच्यते**, or the cry for help itself.\n'
        '  **विशेषाभावाद् द्वयोरपि ग्रहणम्**: nothing separates\n'
        '  them, so both are taken.'
    ),
    '4.4.39': (
        'SETTLED — पदोत्तरपदं गृह्णाति. पूर्वपदं गृह्णाति\n'
        '  **पौर्वपदिकः**; **औत्तरपदिकः** — and both are the\n'
        "  grammarians' own words for the first and last member\n"
        '  of a compound.\n'
        '\n'
        'NOTE — **पदान्तादिति नोक्तम् — बहुच्पूर्वान् मा\n'
        '  भूदिति**: the rule says *last member* and not\n'
        '  *ending in पद*, so that a पद preceded by बहुच् does\n'
        '  not come in. The same argument 4.2.137 made with the\n'
        '  same word.'
    ),
    '4.4.40': (
        'SETTLED — प्रतिकण्ठार्थललामं च. प्रतिकण्ठं गृह्णाति\n'
        '  **प्रातिकण्ठिकः**, one who learns by heart;\n'
        '  **आर्थिकः**, one who takes the sense; लालामिकः.'
    ),
    '4.4.41': (
        'SETTLED — धर्मं चरति. **चरतिरासेवायां नानुष्ठानमात्रे** — चर्\n'
        '  here is PRACTISING habitually and not merely\n'
        '  performing once, which is why धार्मिकः means a man of\n'
        '  religion and not a man who has done one rite. And a\n'
        '  vārttika: **अधर्माच्चेति वक्तव्यम्** — आधर्मिकः.'
    ),
    '4.4.42': (
        'SETTLED — प्रतिपथमेति ठंश्च — the ठन्, and by the च the ठक् too.\n'
        '  प्रतिपथमेति **प्रतिपथिकः**, **प्रातिपथिकः**: one who\n'
        '  goes to meet another on the road.'
    ),
    '4.4.43': (
        'SETTLED — समवायान् समवैति. **समवायः समूह उच्यते, न संप्रधारणा**\n'
        '  — a समवाय here is a GATHERING and not a deliberation;\n'
        '  **समवैति आगत्य तदेकदेशीभवतीत्यर्थः**, to come and\n'
        '  become part of it. **सामवायिकः**; सामाजिकः,\n'
        '  सामूहिकः. **समवायानिति बहुवचनं\n'
        '  स्वरूपविधिनिरासार्थम्.**'
    ),
    '4.4.44': (
        'SETTLED — परिषदो ण्यः, ठकोऽपवादः. परिषदं समवैति **पारिषद्यः** —\n'
        '  one who attends an assembly.'
    ),
    '4.4.45': (
        'SETTLED — सेनाया वा, ठकोऽपवादः; **पक्षे सोऽपि भवति**. सेनां\n'
        '  समवैति **सैन्यः** and **सैनिकः** — and both of the\n'
        '  ordinary words for a soldier survive, one by each\n'
        '  side of the option.'
    ),
    '4.4.46': (
        'SETTLED — संज्ञायां ललाटकुक्कुट्यौ पश्यति.\n'
        '  **संज्ञाग्रहणमभिधेयनियमार्थम्, न तु रूढ्यर्थम्** —\n'
        '  the word *name* restricts what is denoted and does not\n'
        '  make the form merely conventional.\n'
        '\n'
        'SETTLED — AND BOTH RESULTS ARE IDIOMS THE VṚTTI HAS TO\n'
        '  EXPLAIN. ललाटं पश्यति **लालाटिकः सेवकः**:\n'
        '  **सर्वावयवेभ्यो ललाटं दूरे दृश्यते** — of all the\n'
        '  parts of a man the forehead is what is seen from\n'
        '  farthest off, so *one who looks at the forehead* is\n'
        '  the servant who keeps his distance, **स्वामिनः\n'
        "  कार्येषु नोपतिष्ठते**, never at hand for his master's\n"
        '  business.\n'
        '\n'
        '  **कौक्कुटिको भिक्षुः**: कुक्कुटीशब्देनापि\n'
        "  कुक्कुटीपातो लक्ष्यते — the hen's word stands for a\n"
        "  hen's stride, and **देशस्याल्पतया हि भिक्षुर्\n"
        '  अविक्षिप्तदृष्टिः पादविक्षेपदेशे चक्षुः संयम्य\n'
        '  गच्छति**: the monk who walks with his eyes fixed on\n'
        '  the little patch his foot will fall on. Two words for\n'
        '  two kinds of downcast look, and neither is derivable\n'
        '  without the story.'
    ),
    '4.4.47': (
        'SETTLED — तस्य धर्म्यम्, षष्ठीसमर्थात्. **धर्म्यं न्याय्यम्,\n'
        '  आचारयुक्तमित्यर्थः** — what is right, what accords\n'
        '  with usage. शुल्कशालाया धर्म्यं **शौल्कशालिकम्**;\n'
        '  आकरिकम्, आपणिकम्, गौल्मिकम्. And the case changes to\n'
        '  the genitive here.'
    ),
    '4.4.48': (
        'SETTLED — अण् महिष्यादिभ्यः, ठकोऽपवादः. महिष्या धर्म्यं\n'
        '  **माहिषम्**, what is due to the chief queen;\n'
        '  प्राजावतम्. The list runs from the queen through the\n'
        '  purohita to the sacrificer and the Hotṛ.'
    ),
    '4.4.49': (
        'SETTLED — ऋतोऽञ्, ठकोऽपवादः. पोतुर्धर्म्यं **पौत्रम्**;\n'
        '  औद्गात्रम् — the dues of the Potṛ and the Udgātṛ\n'
        '  priests.\n'
        '\n'
        'NOTE — three vārttikas add shapes. **नराच्चेति\n'
        '  वक्तव्यम्** — नरस्य धर्म्या **नारी**, and the\n'
        '  ordinary word for a woman is made by this rule.\n'
        '  **विशसितुरिड्लोपश्च** — वैशस्त्रम्;\n'
        '  **विभाजयितुर्णिलोपश्च** — वैभाजित्रम्.'
    ),
    '4.4.50': (
        'SETTLED — अवक्रयः, तस्येत्येव. **अवक्रीणीतेऽनेनेत्यवक्रयः,\n'
        '  पिण्डक उच्यते** — the rent by which a thing is\n'
        '  farmed. शुल्कशालाया अवक्रयः **शौल्कशालिकः**;\n'
        '  आकरिकः, आपणिकः, गौल्मिकः.\n'
        '\n'
        'SETTLED — AND WHY THIS IS NOT THE RULE BEFORE IT.\n'
        '  **नन्ववक्रयोऽपि धर्म्यमेव? नैतदस्ति; लोकपीडया\n'
        '  धर्मातिक्रमेणाप्यवक्रयो भवति** — is rent not also\n'
        "  what is DUE? No: rent can be exacted to the people's\n"
        '  hurt and in defiance of right, and the two senses\n'
        '  part company exactly there. A distinction drawn on\n'
        '  the ground of how the world works.'
    ),
    '4.4.51': (
        'SETTLED — तदस्य पण्यम्, प्रथमासमर्थाद् अस्येति षष्ठ्यर्थे.\n'
        '  अपूपाः पण्यमस्य **आपूपिकः**, a man whose wares are\n'
        '  cakes; शाष्कुलिकः, मौदकिकः. The case changes again —\n'
        '  the base in the nominative and the relation a\n'
        '  genitive.\n'
        '\n'
        'SETTLED — AND THE QUALIFIER IS ABSORBED INTO THE WORD.\n'
        '  **पण्यमिति विशेषणं तद्धितवृत्तावन्तर्भूतम्, अतः\n'
        '  पण्यशब्दो न प्रयुज्यते** — *wares* is taken up INTO\n'
        '  the derived word and is not said beside it. आपूपिकः\n'
        '  already says it, and saying it again would be saying\n'
        '  it twice.'
    ),
    '4.4.52': (
        'SETTLED — लवणाट् ठञ्, ठकोऽपवादः; **स्वरे विशेषः**. लवणं पण्यमस्य\n'
        '  **लावणिकः**, a salt-merchant — and the same word\n'
        '  whose affix 4.4.24 removed in another sense.'
    ),
    '4.4.53': (
        'SETTLED — किशरादिभ्यः ष्ठन्, ठकोऽपवादः. **किशरादयो\n'
        '  गन्धविशेषवचनाः** — the list is of particular\n'
        '  perfumes. किशराः पण्यमस्य **किशरिकः**, किशरिकी;\n'
        '  नरदिकः, नरदिकी. The fifth of the six the kārikā at\n'
        '  4.4.7 counts.'
    ),
    '4.4.54': (
        'SETTLED — शलालुनोऽन्यतरस्याम्, ठकोऽपवादः; पक्षे सोऽपि भवति.\n'
        '  **शलालुशब्दो गन्धविशेषवचनः** — another perfume.\n'
        '  **शलालुकः**, शलालुकी; and by the option **शालालुकः**,\n'
        '  शालालुकी.'
    ),
    '4.4.55': (
        'SETTLED — शिल्पम्, तदस्येत्येव. **शिल्पं कौशलम्** — a craft is a\n'
        '  skill. मृदङ्गवादनं शिल्पमस्य **मार्दङ्गिकः**, a\n'
        '  drummer; पाणविकः, **वैणिकः**, a lutanist.\n'
        '\n'
        'NOTE — **मृदङ्गवादने वर्तमानो मृदङ्गशब्दः\n'
        '  प्रत्ययमुत्पादयति**: the word मृदङ्ग here stands for\n'
        '  the PLAYING of the drum, and it is that which takes\n'
        '  the affix. **शिल्पं तद्धितवृत्तावन्तर्भवति**, and the\n'
        '  qualifier is absorbed as it was four sūtras back.'
    ),
    '4.4.56': (
        'SETTLED — मड्डुकझर्झरादण् अन्यतरस्याम्, ठकोऽपवादः; पक्षे सोऽपि\n'
        '  भवति. मड्डुकवादनं शिल्पमस्य **माड्डुकः**,\n'
        '  माड्डुकिकः; **झार्झरः**, झार्झरिकः — two more drums,\n'
        '  and two forms each.'
    ),
    '4.4.57': (
        'SETTLED — प्रहरणम्, तदस्येत्येव. असिः प्रहरणमस्य **आसिकः**, a\n'
        '  swordsman; प्रासिकः, चाक्रिकः, **धानुष्कः** — and\n'
        "  that last is the same word 4.4.12's compound-entry\n"
        '  produced in quite another sense, one who LIVES by the\n'
        '  bow against one who FIGHTS with it.'
    ),
    '4.4.58': (
        'SETTLED — परश्वधाट् ठञ् च — the ठञ्, and by the च the ठक्;\n'
        '  **स्वरे विशेषः**. परश्वधः प्रहरणमस्य\n'
        '  **पारश्वधिकः**, an axeman.'
    ),
    '4.4.59': (
        'SETTLED — शक्तियष्ट्योरीकक्, ठकोऽपवादः. शक्तिः प्रहरणमस्य\n'
        '  **शाक्तीकः**; **याष्टीकः** — the spearman and the\n'
        '  staff-fighter.'
    ),
    '4.4.60': (
        'SETTLED — अस्तिनास्तिदिष्टं मतिः, तदस्येत्येव. अस्ति मतिरस्य\n'
        '  **आस्तिकः**; नास्ति मतिरस्य **नास्तिकः**;\n'
        '  **दैष्टिकः**.\n'
        '\n'
        'SETTLED — AND THE RULE IS NOT ABOUT MERELY HAVING AN\n'
        '  OPINION. **न च मतिसत्तामात्रे प्रत्यय इष्यते; किं\n'
        '  तर्हि? परलोकोऽस्तीति यस्य मतिरस्ति, स आस्तिकः** —\n'
        '  one whose conviction is that the next world IS;\n'
        '  **तद्विपरीतो नास्तिकः**, one whose conviction runs\n'
        '  the other way; **प्रमाणानुपातिनी यस्य मतिः स\n'
        '  दैष्टिकः**, one whose conviction follows the\n'
        '  evidence.\n'
        '\n'
        '  **तदेतदभिधानशक्तिस्वभावाल् लभ्यते** — and all of\n'
        '  that is got from the nature of what the words can\n'
        '  denote, not from anything the rule itself says. Three\n'
        '  of the oldest terms of Indian philosophy, defined in\n'
        '  a grammar and by usage rather than by definition.\n'
        '\n'
        'NOTE — **अस्तिनास्तिशब्दौ निपातौ, वचनसामर्थ्याद् वा\n'
        '  आख्याताद् वाक्याच् च प्रत्ययः**: the first two are\n'
        '  particles, or else the affix comes from a finite verb\n'
        '  and from a whole sentence — which the vārttikas on\n'
        '  4.4.1 had already allowed.'
    ),
    '4.4.61': (
        'SETTLED — शीलम्, तदस्येत्येव. **शीलं स्वभावः** — a habit is a\n'
        "  man's nature. अपूपभक्षणं शीलमस्य **आपूपिकः**.\n"
        '  **भक्षणक्रिया तद्विशेषणं च शीलं\n'
        '  तद्धितवृत्तावन्तर्भवति** — the eating and the habit\n'
        '  that qualifies it are both taken up into the derived\n'
        '  word.'
    ),
    '4.4.62': (
        'SETTLED — छत्रादिभ्यो णः, ठकोऽपवादः. **छादनादावरणाच्छत्रम्** — a\n'
        '  छत्र is from covering.\n'
        '\n'
        'SETTLED — AND THE ORDINARY WORD FOR A STUDENT IS\n'
        '  EXPLAINED. **गुरुकार्येष्ववहितः\n'
        '  तच्छिद्रावरणप्रवृत्तश्छत्रशीलः शिष्यश्छात्रः** —\n'
        '  the pupil who attends to\n'
        "  his teacher's affairs and makes it his habit to COVER\n"
        '  his faults is a **छात्रः**. A word every Sanskrit\n'
        '  reader knows, and its derivation is a description of\n'
        '  discretion.\n'
        '\n'
        'NOTE — **स्थाशब्दोऽत्र पठ्यते, स चोपसर्गपूर्वोऽत्र\n'
        '  गृह्यते**: स्था is in the list and is taken only with\n'
        '  a preverb — आस्था, संस्था, अवस्था.'
    ),
    '4.4.63': (
        'SETTLED — कर्माध्ययने वृत्तम्, तदस्येत्येव. एकमन्यदध्ययने कर्म\n'
        '  वृत्तमस्य **ऐकान्यिकः**; द्वैयन्यिकः, त्रैयन्यिकः.\n'
        '\n'
        "SETTLED — AND THE WORD COUNTS A PUPIL'S MISTAKES.\n"
        '  **यस्याध्ययनप्रयुक्तस्य परीक्षाकाले पठतः स्खलितम्\n'
        '  अपपाठरूपमेकं जातम्, स उच्यत ऐकान्यिकः** — a student\n'
        '  who, reciting at his examination, has slipped ONCE\n'
        '  into a wrong reading; and so द्वैयन्यिकः for twice.\n'
        '  The grammar has a word for how many errors a pupil\n'
        '  made.\n'
        '\n'
        'NOTE — the base is compounded first: **एकमन्यदिति\n'
        '  विगृह्य तद्धितार्थो** [2.1.51] इति समासः, and then\n'
        '  the affix comes.'
    ),
    '4.4.64': (
        'SETTLED — बह्वच्पूर्वपदाट् ठच्, ठकोऽपवादः. द्वादशान्यानि\n'
        '  कर्माण्यध्ययने वृत्तान्यस्य **द्वादशान्यिकः**;\n'
        '  **चतुर्दशान्यिकः**, *he has made fourteen wrong\n'
        '  readings*.\n'
        '\n'
        'NOTE — and the vṛtti says what counts as one. **उदात्ते\n'
        '  कर्तव्ये योऽनुदात्तं करोति, स उच्यतेऽन्यत् त्वं\n'
        '  करोषीति** — where an acute was called for and he made\n'
        '  it grave, one says *you are doing something ELSE*.\n'
        '  Which is where the अन्य of the compound comes from.'
    ),
    '4.4.65': (
        'SETTLED — हितं भक्षाः, तदस्येत्येव. अपूपभक्षणं हितमस्मै\n'
        '  **आपूपिकः**.\n'
        '\n'
        'SETTLED — AND A CASE SILENTLY TURNED BY WHAT THE WORDS\n'
        '  REQUIRE. ननु च हितयोगे चतुर्थ्या भवितव्यम्, तत्र कथं\n'
        '  षष्ठ्यर्थे प्रत्ययो विधीयते? — *beneficial* governs a\n'
        '  dative, so how is the affix given in a genitive\n'
        '  sense? **एवं तर्हि सामर्थ्याद् विभक्तिविपरिणामो\n'
        '  भविष्यति**: the construction itself turns the case.\n'
        '  The heading says one thing and the sense requires\n'
        '  another, and the requirement wins.'
    ),
    '4.4.66': (
        'SETTLED — तदस्मै दीयते नियुक्तम्. **नियोगेनाव्यभिचारेण दीयते\n'
        '  इत्यर्थः; अव्यभिचारो नियोगः** — given by appointment\n'
        '  and without fail. अग्रे भोजनमस्मै नियुक्तं दीयते\n'
        '  **आग्रभोजनिकः**.\n'
        '\n'
        'NOTE — **केचित् तु नियुक्तं नित्यमाहुः**: some say\n'
        '  नियुक्त simply means *always* — अपूपा नित्यमस्मै\n'
        '  दीयन्त आपूपिकः. Two readings recorded and neither\n'
        '  chosen.'
    ),
    '4.4.67': (
        'SETTLED — श्राणामांसौदनाट् टिठन्, ठकोऽपवादः. **इकार\n'
        '  उच्चारणार्थः, टकारो ङीबर्थः** — the इ only to make\n'
        '  the affix pronounceable and the ट् for the feminine.\n'
        '  **श्राणिकः**, श्राणिकी; मांसौदनिकः, मांसौदनिकी.\n'
        '\n'
        'SETTLED — AND WHY NOT SIMPLY THE OTHER AFFIX? अथ ठञेव\n'
        '  कस्माद् नोक्तः, **न ह्यत्र ठञष्टिठनो वा\n'
        '  विशेषोऽस्ति?** — nothing separates the two.\n'
        '  **मांसौदनग्रहणं संघातविगृहीतार्थं केचिदिच्छन्ति;\n'
        '  तत्र वृद्ध्यभावो विशेषः**: because some read\n'
        '  मांसौदन as compound AND parts, and then the ABSENCE\n'
        '  of the strengthening is what tells the affixes apart\n'
        '  — ओदनिकः and not औदनिकः. A difference that shows only\n'
        '  on a reading some hold and others do not.'
    ),
    '4.4.68': (
        'SETTLED — भक्तादण् अन्यतरस्याम्, ठकोऽपवादः; पक्षे सोऽपि भवति.\n'
        '  भक्तमस्मै दीयते नियुक्तं **भाक्तः**, **भाक्तिकः**.'
    ),
    '4.4.69': (
        'SETTLED — तत्र नियुक्तः, सप्तमीसमर्थात्. **नियुक्तोऽधिकृतो\n'
        '  व्यापारित इत्यर्थः** — appointed, put in charge, set\n'
        '  to work. शुल्कशालायां नियुक्तः **शौल्कशालिकः**;\n'
        '  आकरिकः, आपणिकः, गौल्मिकः, **दौवारिकः**.\n'
        '\n'
        'NOTE — the same four bases 4.4.47 and 4.4.50 used, in a\n'
        '  third sense: what is DUE to the customs-house, its\n'
        '  RENT, and now the man APPOINTED to it.'
    ),
    '4.4.70': (
        'SETTLED — अगारान्ताट् ठन्, ठकोऽपवादः. देवागारे नियुक्तो\n'
        '  **देवागारिकः**; कोष्ठागारिकः, **भाण्डागारिकः** — the\n'
        '  temple-keeper, the granary-keeper, the storekeeper.'
    ),
    '4.4.71': (
        'SETTLED — अध्यायिन्यदेशकालात्, तत्रेत्येव. **अध्ययनस्य यौ\n'
        '  देशकालौ शास्त्रेण प्रतिषिद्धौ तावदेशकालशब्देनोच्येते**\n'
        '  — the *non-place* and *non-time* are the place and\n'
        '  hour at which another text FORBIDS study, and the\n'
        '  affix comes from those.\n'
        '\n'
        '  श्मशानेऽधीते **श्माशानिकः**, one who studies in a\n'
        '  cremation-ground; चातुष्पथिकः, at a crossroads; and\n'
        '  from the forbidden days **चातुर्दशिकः**,\n'
        '  आमावास्यिकः. अदेशकालादिति किम्? स्रुघ्नेऽधीते,\n'
        '  पूर्वाह्णेऽधीते — an ordinary place and an ordinary\n'
        '  hour get nothing.\n'
        '\n'
        '  A grammatical rule whose whole ground is what a\n'
        '  DIFFERENT text prohibits.'
    ),
    '4.4.72': (
        'SETTLED — कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति, तत्रेत्येव.\n'
        '  **व्यवहारः क्रियातत्त्वम्, यथा लौकिकव्यवहार इति** —\n'
        '  dealing is the thing actually done. वंशकठिने व्यवहरति\n'
        '  **वांशकठिनिकश्चक्रचरः**, the acrobat who works on a\n'
        '  bamboo frame; वार्ध्रकठिनिकः, प्रास्तारिकः,\n'
        '  सांस्थानिकः.'
    ),
    '4.4.73': (
        'SETTLED — निकटे वसति. **यस्य शास्त्रतो निकटवासस्तत्रायं विधिः**\n'
        '  — the rule is for one whose dwelling-near is laid\n'
        '  down by a text: **आरण्यकेन भिक्षुणा ग्रामात् क्रोशे\n'
        '  वस्तव्यमिति शास्त्रम्**, a forest mendicant must live\n'
        '  a krośa from the village. निकटे वसति **नैकटिको\n'
        '  भिक्षुः**. A second rule in three whose condition is\n'
        '  a monastic one.'
    ),
    '4.4.74': (
        'SETTLED — आवसथात् ष्ठल्, तत्रेत्येव. **लकारः स्वरार्थः, षकारो\n'
        '  ङीषर्थः**. आवसथे वसति **आवसथिकः**, आवसथिकी — one who\n'
        '  lives in a rest-house.\n'
        '\n'
        "SETTLED — THE SIXTH AND LAST OF THE KĀRIKĀ'S SIX.\n"
        "  4.4.7's verse named आकर्ष, पर्पादि, भस्त्रादि,\n"
        '  कुसीदसूत्र, आवसथ and किशरादि as the grounds of the\n'
        '  ष-initial affixes of this section. This is the last\n'
        '  of the six to arrive, and the whole count can now be\n'
        '  checked: six statements, seven affixes.\n'
        '\n'
        'SETTLED — AND IT CLOSES THE ठक् SECTION IN AS MANY\n'
        '  WORDS. **ठकः पूर्णोऽवधिः, अतः परमन्यः प्रत्ययो\n'
        "  विधीयते** — the ठक्'s limit is complete and from here\n"
        '  another affix is enjoined. So the LAST RULE the\n'
        '  heading governs is this one, though the word that\n'
        '  MARKS its boundary was lifted out of 4.4.76. A\n'
        "  heading's marker and its last rule are not the same\n"
        '  sūtra, and they come apart because a second heading\n'
        '  opens inside the first.'
    ),
    '4.4.75': (
        'SETTLED — प्राग्घिताद् यत्. **तस्मै हितम् [5.1.5] इति वक्ष्यति;\n'
        '  प्रागेतस्माद् हितसंशब्दनाद् यानित ऊर्ध्वम्\n'
        '  अनुक्रमिष्यामो यत्प्रत्ययस्तेष्वधिकृतो वेदितव्यः** —\n'
        '  यत् is the affix for every sense named from here to\n'
        '  5.1.4.\n'
        '\n'
        'SETTLED — THE THIRD GREAT प्राक्-HEADING, AND THE FIRST\n'
        '  TO CROSS A CHAPTER. 4.1.83 bounded अण् by lifting\n'
        '  दीव्यति out of 4.4.2; 4.4.1 bounded ठक् by lifting\n'
        '  वहति out of 4.4.76; this bounds यत् by lifting हित\n'
        '  out of 5.1.5. One device, three times — and this one\n'
        '  reaches out of अध्याय ४ altogether.\n'
        '\n'
        "NOTE — and the heading's own examples are taken from\n"
        '  the rule that follows it: वक्ष्यति तद्वहति\n'
        '  रथयुगप्रासङ्गम् — **रथ्यः, युग्यः, प्रासङ्ग्यः**.'
    ),
    '4.4.76': (
        'SETTLED — तद्वहति रथयुगप्रासङ्गम्. रथं वहति **रथ्यः**;\n'
        '  **युग्यः**, **प्रासङ्ग्यः** — the horse that draws a\n'
        '  chariot, a yoke, a training-harness.\n'
        '\n'
        'SETTLED — AND THIS IS THE RULE WHOSE WORD BOUNDED THE\n'
        '  LAST HEADING. वहति was lifted out of it to mark where\n'
        '  ठक् stops, and the rule itself falls under the NEW\n'
        '  heading and gives यत्. A sūtra used as a\n'
        '  boundary-post by one section and governed by another.\n'
        '\n'
        'NOTE — **रथसीताहलेभ्यो यद्विधौ** (महाभाष्यवार्त्तिक on\n'
        '  1.1.72) इति तदन्तविध्युपसंख्यानात् परमरथ्य इत्यपि\n'
        '  भवति: the same vārttika 4.3.121 needed, extending the\n'
        '  rule to compounds ending in these words.'
    ),
    '4.4.77': (
        'SETTLED — धुरो यड्ढकौ. धुरं वहति **धुर्यः**, **धौरेयः** — the\n'
        '  beast that bears the yoke-pole, and both words are\n'
        '  still the ordinary ones for a leader.'
    ),
    '4.4.78': (
        'SETTLED — खः सर्वधुरात्. सर्वधुरां वहति **सर्वधुरीणः**.\n'
        '  **स्त्रीलिङ्गे न्याय्ये सर्वधुरादिति\n'
        '  प्रातिपदिकमात्रापेक्षो निर्देशः** — the feminine\n'
        '  would have been proper, and the rule names the bare\n'
        '  stem instead.\n'
        '\n'
        'NOTE — **ख इति योगविभागः कर्तव्य इष्टसंग्रहार्थः**:\n'
        '  the rule is to be split, the ख standing alone, so\n'
        '  that उत्तरधुरीणः and दक्षिणधुरीणः come in too.'
    ),
    '4.4.79': (
        'SETTLED — एकधुराल्लुक् च. एकधुरां वहति **एकधुरीणः** and\n'
        '  **एकधुरः** — the affix and, by the च, its removal.\n'
        '  **वचनसामर्थ्यात् पक्षे लुग् विधीयते**: the mere fact\n'
        '  that the rule is spoken makes the elision optional,\n'
        '  since otherwise it would leave the affix nothing to\n'
        '  do.'
    ),
    '4.4.80': (
        'SETTLED — शकटादण्. शकटं वहति **शाकटो गौः** — the ox that draws a\n'
        '  cart.'
    ),
    '4.4.81': (
        'SETTLED — हलसीराट् ठक्. हलं वहति **हालिकः**; सैरिकः — the ox\n'
        '  that draws a plough.\n'
        '\n'
        'NOTE — the same rule stood in the pāda before. **4.3.124\n'
        '  हलसीराट् ठक्** gives the same affix from the same two\n'
        '  bases, in the sense *what belongs to a plough*. One\n'
        '  pair of words, one affix, and two senses a whole pāda\n'
        "  apart — there the plough's own gear, here the ox that\n"
        '  pulls it.'
    ),
    '4.4.82': (
        'SETTLED — संज्ञायां जन्याः. **जनी वधूरुच्यते** — जनी is the\n'
        '  bride. जनीं वहति **जन्या, जामातुर्वयस्या**: the\n'
        "  bridegroom's friend, **सा हि विहारादिषु\n"
        '  जामातृसमीपं प्रापयति**, because she is the one who\n'
        '  brings the bride to him. A whole social role in one\n'
        '  derived word.'
    ),
    '4.4.83': (
        'SETTLED — विध्यत्यधनुषा. पादौ विध्यन्ति **पद्याः शर्कराः**,\n'
        '  gravel that pierces the feet; **ऊरव्याः कण्टकाः**.\n'
        '\n'
        'SETTLED — AND AN EXCLUSION READ AS QUALIFYING THE ACT\n'
        '  BECAUSE IT WAS UNNECESSARY AS STATED. अधनुषेति किम्?\n'
        '  पादौ विध्यति धनुषा — but then: **ननु असमर्थत्वाद्\n'
        '  अनभिधानाच्च प्रत्ययो न भवति, न हि धनुषा पद्य\n'
        '  इत्युक्ते विवक्षितोऽर्थः प्रतीयते?** the words would\n'
        '  not convey the meaning anyway, so the exclusion has\n'
        '  nothing to exclude. **एवं तर्हि धनुष्प्रतिषेधेन\n'
        '  व्यधनक्रिया विशेष्यते — यस्यां धनुष्करणं न\n'
        '  संभाव्यत इति**: it is therefore read as qualifying\n'
        '  the ACT — a piercing in which a bow could not be the\n'
        '  instrument at all. **तेनेह न भवति — चौरं विध्यति,\n'
        '  शत्रुं विध्यति**, and so a man shot at gets no word.\n'
        '  A negation moved from the instrument to the action\n'
        '  because it was idle where it stood.'
    ),
    '4.4.84': (
        'SETTLED — धनगणं लब्धा. **धन्यः**, **गण्यः** — one who wins\n'
        '  wealth, one who wins a following. **लब्धेति\n'
        '  तृन्नन्तम्, तेन द्वितीया समर्था विभक्तिर्युज्यते**:\n'
        '  the word is an agent-noun in तृन्, which is why an\n'
        '  accusative can go with it at all.'
    ),
    '4.4.85': (
        'SETTLED — अन्नाण्णः. अन्नं लब्धा **आन्नः** — one who gets food.'
    ),
    '4.4.86': (
        'SETTLED — वशं गतः. वशं गतो **वश्यः** — **कामप्राप्तो विधेय\n'
        "  इत्यर्थः**, one brought under another's will and so\n"
        '  subject to him.'
    ),
    '4.4.87': (
        'SETTLED — पदमस्मिन् दृश्यम्. **निर्देशादेव प्रथमा\n'
        '  समर्थविभक्तिः** — the case is read off the wording\n'
        '  itself, the rule naming no case-word. पदं दृश्यमस्मिन्\n'
        '  **पद्यः कर्दमः**; पद्याः पांसवः.\n'
        '\n'
        'SETTLED — AND WHAT THE WORD NAMES IS A STATE OF MUD.\n'
        '  **शक्यार्थे कृत्यप्रत्ययः** — दृश्य is a कृत्य and\n'
        '  means *can be seen*; **यस्मिन् पदं द्रष्टुं\n'
        '  प्रतिमुद्रोत्पादनेन, स पद्यः कर्दमः**, mud in which\n'
        '  a footprint can be seen because it takes an\n'
        '  impression. **कर्दमस्यावस्थोच्यते नातिद्रवो\n'
        '  नातिशुष्क इति**: neither too wet nor too dry. A rule\n'
        '  about the consistency of mud.'
    ),
    '4.4.88': (
        'SETTLED — मूलमस्याबर्हि. **मूल्या माषाः**, मूल्या मुद्गाः.\n'
        '  **वृहू उद्यमने** — येषां मूलमावृह्यत उत्पाट्यते, ते\n'
        '  मूल्याः, **सुष्ठु निष्पन्नाः**: plants whose root has\n'
        '  to be pulled up, and that means fully grown —\n'
        '  **मूलोत्पाटनेन विना ग्रहीतुं न शक्यन्ते**, they\n'
        '  cannot be taken without uprooting. Ripeness described\n'
        '  by how one has to harvest it.'
    ),
    '4.4.89': (
        'SETTLED — संज्ञायां धेनुष्या. **धेनोः षुगागमो यश्च प्रत्ययो\n'
        '  निपात्यते** — the षुक् and the affix laid down\n'
        '  together, and **अन्तोदात्तोऽपि ह्ययमिष्यते**, the\n'
        '  final accent with them.\n'
        '\n'
        '  **या धेनुरुत्तमर्णाय ऋणप्रदानाद् दोहनार्थं दीयते सा\n'
        '  धेनुष्या** — the cow made over to a creditor, in\n'
        '  place of interest, for him to milk; **पीतदुग्धेति\n'
        '  यस्याः प्रसिद्धिः**, known as *the one whose milk is\n'
        '  drunk*. धेनुष्यां भवते ददामि. A financial instrument\n'
        '  with a word of its own.'
    ),
    '4.4.90': (
        'SETTLED — गृहपतिना संयुक्ते ञ्यः. **निर्देशादेव तृतीयासमर्थविभक्तिः**\n'
        '  — the instrumental is read off the wording. गृहपतिना\n'
        "  संयुक्तो **गार्हपत्योऽग्निः**, the householder's\n"
        '  fire, one of the three of the śrauta ritual.\n'
        '\n'
        'NOTE — **अन्यस्यापि गृहपतिना संयोगोऽस्ति, तत्र\n'
        '  संज्ञाधिकारादतिप्रसङ्गनिवृत्तिः**: other things are\n'
        '  joined to a householder too, and it is the संज्ञा\n'
        '  heading that keeps the rule from reaching them.'
    ),
    '4.4.91': (
        'SETTLED — \n'
        '  नौवयोधर्मविषमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसंमितेषु\n'
        '  — **अष्टभ्यः शब्देभ्योऽष्टस्वेव तार्यादिष्वर्थेषु यथासंख्यम्**:\n'
        '  eight bases against eight senses, matched in order, and मूल\n'
        '  answers two of them.\n'
        '\n'
        'SETTLED — नावा तार्यं **नाव्यमुदकम्**, water one can cross by boat;\n'
        "  वयसा तुल्यो **वयस्यः सखा**, a friend of one's own age; धर्मेण\n"
        '  प्राप्यं **धर्म्यम्**; विषेण वध्यो **विष्यः**; मूलेनानाम्यं\n'
        '  **मूल्यम्**; मूलेन समो **मूल्यः पटः**; सीतया समितं **सीत्यं\n'
        '  क्षेत्रम्**; तुलया संमितं **तुल्यम्**.\n'
        '\n'
        'SETTLED — **AND THE NEXT RULE IS SHOWN NOT TO COVER ONE OF THEM.**\n'
        '  ननु च धर्मादनपेते इति वक्ष्यमाणेनैव सिद्धम्? **नैतदस्ति; धर्मं\n'
        '  यदनुवर्तते तद् धर्मादनपेतमित्युच्यते; फलं तु धर्मादपेत्यैव,\n'
        '  कार्यविरोधित्वाद् धर्मस्य** — what *does not depart from* dharma\n'
        '  is what conforms to it, and a FRUIT departs from it, being the\n'
        '  opposite of the act. So *obtainable by dharma* needs its own rule'
    ),
    '4.4.92': (
        'SETTLED — धर्मपथ्यर्थन्यायादनपेते. **निर्देशादेव पञ्चमी\n'
        '  समर्थविभक्तिः** — the ablative is read off the wording.\n'
        '  धर्मादनपेतं **धर्म्यम्**; **पथ्यम्**, **अर्थ्यम्**, **न्याय्यम्**\n'
        '  — and all four are still the ordinary words for *proper*,\n'
        '  *wholesome*, *meaningful*, *just*'
    ),
    '4.4.93': (
        'SETTLED — छन्दसो निर्मिते. **निर्मित उत्पादितः**. छन्दसा निर्मितश्\n'
        '  **छन्दस्यः**, **इच्छया कृत इत्यर्थः** — and\n'
        '  **इच्छापर्यायश्छन्दःशब्द इह गृह्यते**: the छन्दस् here is not\n'
        '  metre but WILL, a synonym of *wish*'
    ),
    '4.4.94': (
        'SETTLED — उरसोऽण् च — the अण्, and by the च the यत्. उरसा निर्मित\n'
        "  **औरसः पुत्रः**, उरस्यः पुत्रः: a son made of one's own breast,\n"
        '  the legitimate son'
    ),
    '4.4.95': (
        'SETTLED — हृदयस्य प्रियः. हृदयस्य प्रियो **हृद्यो देशः**, हृद्यं\n'
        '  वनम् — a place dear to the heart. And the संज्ञा heading narrows\n'
        '  what may be meant: **इह न भवति — हृदयस्य प्रियः पुत्रः**, a\n'
        '  beloved SON is not what the word names'
    ),
    '4.4.96': (
        'SETTLED — बन्धने चर्षौ, हृदयस्येत्येव. **बध्यते येन तद् बन्धनम्**;\n'
        '  **ऋषिर्वेदो गृह्यते**. हृदयस्य बन्धनम् ऋषिर् **हृद्यः** —\n'
        '  **परहृदयं येन बध्यते वशीक्रियते, स वशीकरणमन्त्रो हृद्य\n'
        "  इत्युच्यते**: the verse by which another's heart is bound, a spell\n"
        '  for winning someone over'
    ),
    '4.4.97': (
        'SETTLED — मतजनहलात् करणजल्पकर्षेषु, **यथासंख्यम्**. Three bases\n'
        '  against three senses. **मतं ज्ञानं तस्य करणं मत्यम्**; जनस्य जल्पो\n'
        '  **जन्यः**; हलस्य कर्षो **हल्यः**, द्विहल्यः, त्रिहल्यः. **भावसाधनं\n'
        '  वा** — or each may be read as naming the act itself'
    ),
    '4.4.98': (
        'SETTLED — तत्र साधुः, सप्तमीसमर्थात्. सामसु साधुः **सामन्यः**;\n'
        '  वेमन्यः, **कर्मण्यः**, **शरण्यः**.\n'
        '\n'
        'SETTLED — **साधुरिह प्रवीणो योग्यो वा गृह्यते, नोपकारकः** — साधु\n'
        '  here is SKILLED or FIT and not *helpful*, **तत्र हि परत्वात् तस्मै\n'
        '  हितम् इत्यनेन विधिना भवितव्यम्**: for *helpful* the later rule\n'
        '  5.1.5 would have the ground. A sense narrowed by pointing at the\n'
        '  rule that would otherwise take it'
    ),
    '4.4.99': (
        'SETTLED — प्रतिजनादिभ्यः खञ्, यतोऽपवादः. प्रतिजने साधुः\n'
        '  **प्रातिजनीनः**, **जनेजने साधुरित्यर्थः** — good with every man he\n'
        '  meets. ऐदंयुगीनः, सांयुगीनः.\n'
        '\n'
        'SETTLED — **यत्र हितार्थ एव साध्वर्थस्तत्र वचनात् प्राक् क्रीतीया\n'
        "  बाध्यन्ते** — where *fit* amounts to *helpful*, this rule's being\n"
        '  spoken displaces the affixes of the section 5.1.1 opens'
    ),
    '4.4.100': (
        'SETTLED — भक्ताण्णः, यतोऽपवादः. भक्ते साधुर् **भाक्तः शालिः**, rice\n'
        '  that does well as a meal; भाक्तास्तण्डुलाः'
    ),
    '4.4.101': (
        'SETTLED — परिषदो ण्यः, यतोऽपवादः. परिषदि साधुः **पारिषद्यः**.\n'
        '\n'
        'SETTLED — **णप्रत्ययोऽप्यत्रेष्यते; तदर्थं योगविभागः क्रियते** —\n'
        '  the ण too is wanted, and the rule is split for it: *from परिषद्,\n'
        '  ण*, giving **पारिषदः**, and then *ण्य*. One rule read as two so\n'
        '  that both affixes come'
    ),
    '4.4.102': (
        'SETTLED — कथादिभ्यष्ठक्, यतोऽपवादः. कथायां साधुः **काथिकः**, a good\n'
        '  story-teller; वैकथिकः'
    ),
    '4.4.103': (
        'SETTLED — गुडादिभ्यष्ठञ्, यतोऽपवादः. गुडे साधुर् **गौडिक इक्षुः**,\n'
        '  sugarcane that makes good molasses; **कौल्माषिको मुद्गः**,\n'
        '  **साक्तुको यवः** — beans good for porridge, barley good for meal.\n'
        '  A list of what each crop is best turned into'
    ),
    '4.4.104': (
        'SETTLED — पथ्यतिथिवसतिस्वपतेर्ढञ्, यतोऽपवादः. पथि साधु **पाथेयम्**,\n'
        '  provision for the road; **आतिथेयम्**, what is fit for a guest;\n'
        '  वासतेयम्, **स्वापतेयम्**'
    ),
    '4.4.105': (
        'SETTLED — सभाया यः, यतोऽपवादः; **स्वरे विशेषः**, and the two differ\n'
        '  only in the accent. सभायां साधुः **सभ्यः** — one fit for an\n'
        '  assembly, and so *civil*'
    ),
    '4.4.106': (
        'SETTLED — ढश्छन्दसि, **यस्यापवादः**. **सभेयो युवास्य यजमानस्य वीरो\n'
        '  जायताम्** (माध्यन्दिनसंहिता २२.२२) — *let a hero be born to this\n'
        '  sacrificer, a youth fit for the assembly*'
    ),
    '4.4.107': (
        'SETTLED — समानतीर्थे वासी. **साधुरिति निवृत्तम्** — *fit* has\n'
        '  lapsed. समाने तीर्थे वासीति **सतीर्थ्यः**, **समानोपाध्याय\n'
        '  इत्यर्थः**: a fellow-student. **तीर्थशब्देनेह गुरुरुच्यते** —\n'
        '  तीर्थ here means the TEACHER, and the word for a shared ford is\n'
        '  the word for a shared master'
    ),
    '4.4.108': (
        'SETTLED — समानोदरे शयित ओ चोदात्तः. **शयितः स्थित इत्यर्थः** —\n'
        '  *lain* means *been*. समानोदरे शयितः **समानोदर्यो भ्राता**, a\n'
        '  brother born of the same womb; and the ओ is made acute in the same\n'
        '  act'
    ),
    '4.4.109': (
        'SETTLED — सोदराद् यः. **विभाषोदरे** [6.3.88] इति सूत्रेण यकारादौ\n'
        '  प्रत्यये विवक्षिते **प्रागेव समानस्य सभावः** — समान becomes स\n'
        '  before the affix is even added, by a rule of the sixth chapter.\n'
        '  समानोदरे शयितः **सोदर्यो भ्राता**. **ओ चोदात्त इति नानुवर्तते;\n'
        '  यकारे स्वरः**: the accent-clause does not carry, and the accent\n'
        '  falls on the य'
    ),
    '4.4.110': (
        'SETTLED — भवे छन्दसि, तत्रेत्येव; **अणादीनां घादीनां चापवादः**.\n'
        '  **नमो मेघ्याय च विद्युत्याय च नमः** (तैत्तिरीयसंहिता ४.५.७.२).\n'
        '\n'
        'SETTLED — **सति दर्शने तेऽपि भवन्ति, सर्वविधीनां छन्दसि\n'
        '  व्यभिचारात्** — and where they are actually attested the other\n'
        '  affixes come too, since EVERY rule is irregular in the Veda. An\n'
        '  exception stated and at once made porous.\n'
        '\n'
        'SETTLED — **आ पादपरिसमाप्तेश्छन्दोऽधिकारः, भवाधिकारश्च\n'
        '  समुद्राभ्राद् घः इति यावत्** — the Vedic heading runs to the END\n'
        '  OF THE PĀDA and the भव heading to 4.4.118. Two ranges opened by\n'
        '  one rule and stopped at different places'
    ),
    '4.4.111': (
        'SETTLED — पाथोनदीभ्यां ड्यण्, यतोऽपवादः. पाथसि भवः **पाथ्यो वृषा**\n'
        '  (ऋग्वेद ६.१६.१५); **चनो दधीत नाद्यो गिरो मे** (ऋग्वेद २.३५.१).\n'
        '  **पाथोऽन्तरिक्षम्** — पाथस् is the middle air'
    ),
    '4.4.112': (
        'SETTLED — वेशन्तहिमवद्भ्यामण्, यतोऽपवादः. **वैशन्तीभ्यः स्वाहा**\n'
        '  (तैत्तिरीयसंहिता ७.४.१३.९); **हैमवतीभ्यः स्वाहा**'
    ),
    '4.4.113': (
        'SETTLED — स्रोतसो विभाषा ड्यड्ड्यौ, यतोऽपवादः; पक्षे सोऽपि भवति.\n'
        '  स्रोतसि भवः **स्रोत्यः** (ऋग्वेद १०.१०४.८), **स्रोतस्यः**.\n'
        '  **ड्यड्ड्ययोः स्वरे विशेषः** — the two differ in the accent alone'
    ),
    '4.4.114': (
        'SETTLED — सगर्भसयूथसनुताद् यन्, यतोऽपवादः; **स्वरे विशेषः**. **अनु\n'
        '  भ्राता सगर्भ्यः**; **अनु सखा सयूथ्यः**; **यो नः सनुत्यः**.\n'
        '  **सर्वत्र समानस्य छन्दसि** [6.3.84] इति सभावः — समान becomes स in\n'
        '  all three, by a Vedic rule of the sixth chapter'
    ),
    '4.4.115': (
        'SETTLED — तुग्राद् घन्, यतोऽपवादः. **त्वमग्ने वृषभस्तुग्रियाणाम्**.\n'
        '  **अन्नाकाशयज्ञवरिष्ठेषु तुग्रशब्दः** — तुग्र is food, sky,\n'
        '  sacrifice and the best of anything, four senses for one word'
    ),
    '4.4.116': (
        'SETTLED — अग्राद् यत्. अग्रे भवम् **अग्र्यम्**.\n'
        '\n'
        'SETTLED — **किमर्थमिदं यावता सामान्येन यद् विहित एव?** — why state\n'
        '  it, when 4.4.110 gives यत् generally already? **घच्छौ च इति\n'
        '  वक्ष्यति, ताभ्यां बाधा मा भूदिति पुनर् विधीयते**: because the NEXT\n'
        '  rule adds घ and छ, and without this the यत् would have been\n'
        '  displaced by them. A rule restated so that its own successor\n'
        '  cannot beat it'
    ),
    '4.4.117': (
        'SETTLED — घच्छौ च. **अग्र्यम्** (खिल १.३.७), **अग्रियम्** (ऋग्वेद\n'
        '  १.१३.१०), **अग्रीयम्** (मैत्रायणीसंहिता २.७.१३). **चकारः तुग्राद्\n'
        "  घन् इत्यस्यानुकर्षणार्थः** — the च drags in 4.4.115's घन् as well,\n"
        '  so अग्रियम् comes by that too; **स्वरे विशेषः**, and the two\n'
        '  अग्रिय differ only in accent'
    ),
    '4.4.118': (
        'SETTLED — समुद्राभ्राद् घः, यतोऽपवादः. **समुद्रिया नदीनाम्**\n'
        '  (ऋग्वेद ७.८७.१); **अभ्रियस्येव घोषाः** (ऋग्वेद १०.६८.१).\n'
        '\n'
        'SETTLED — **अभ्रशब्दस्यापूर्वनिपातः, तस्य लक्षणस्य\n'
        '  व्यभिचारित्वात्** — अभ्र does not come first in the compound\n'
        '  though the rule for order would put it there, because that rule is\n'
        '  not without exception. And this rule is where the भव heading stops'
    ),
    '4.4.119': (
        'SETTLED — बर्हिषि दत्तम्. **भव इति निवृत्तम्** — *being* has\n'
        '  lapsed. **बर्हिष्येषु निधिषु प्रियेषु** (ऋग्वेद १०.१५.५) — of the\n'
        '  dear treasures laid on the sacred grass'
    ),
    '4.4.120': (
        'SETTLED — दूतस्य भागकर्मणी. **भागोंऽशः; कर्म क्रिया**. **यदग्ने\n'
        '  यासि दूत्यम्** (ऋग्वेद १.१२.४) — *when, Agni, you go on your\n'
        '  embassy*: दूतभागः, दूतकर्म वा'
    ),
    '4.4.121': (
        'SETTLED — रक्षोयातूनां हननी. **हन्यतेऽनयेति हननी** — that by which\n'
        '  they are killed. **या वां मित्रावरुणौ रक्षस्या तनूः**;\n'
        '  **यातव्या**.\n'
        '\n'
        'SETTLED — **बहुवचनं स्तुतिवैशिष्ट्यज्ञापनार्थम्; बहूनां रक्षसां\n'
        '  हननेन तनूः स्तूयते** — the plural in the rule is there to mark the\n'
        '  force of the praise: the body is praised for killing MANY demons'
    ),
    '4.4.122': (
        'SETTLED — रेवतीजगतीहविष्याभ्यः प्रशस्ये. **प्रशंसनं प्रशस्यम्; भावे\n'
        '  क्यप् प्रत्ययो भवति**. **यद्वो रेवती रेवत्यम्**, **यद्वो\n'
        '  जगतीर्जगत्यम्**, **यद्वो हविष्या हविष्यम्** (काठकसंहिता १.८) —\n'
        '  *what praise of you there is*, three times over'
    ),
    '4.4.123': (
        'SETTLED — असुरस्य स्वम्, अणोऽपवादः. **असुर्यं वा एतत् पात्रं यत्\n'
        '  कुलालकृतं चक्रवृत्तम्** (मैत्रायणीसंहिता १.८.३) — *that vessel is\n'
        "  the Asuras' own, the one the potter made and the wheel turned*"
    ),
    '4.4.124': (
        'SETTLED — मायायामण्, **पूर्वस्य यतोऽपवादः**. **आसुरी माया स्वधया\n'
        "  कृतासि** (माध्यन्दिनसंहिता ११.६९) — the Asuras' own, but only\n"
        '  where the MAGIC of them is meant'
    ),
    '4.4.125': (
        'SETTLED — तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः. The\n'
        '  longest rule of the pāda, and every word of it is conditional. A\n'
        '  stem ending in मतुप् takes यत् where the thing named is BRICKS and\n'
        '  the first word names the mantra by which they are laid — and the\n'
        '  मतुप् is removed in the same act, **लुक् च मतोरिति\n'
        '  प्रकृतिनिर्ह्रासः**.\n'
        '\n'
        'SETTLED — वर्चःशब्दो यस्मिन् मन्त्रेऽस्ति स वर्चस्वान्; **उपधीयते\n'
        '  येन स उपधानः, चयनवचन इत्यर्थः**. वर्चस्वानुपधानमन्त्र\n'
        '  आसामिष्टकानाम् इति विगृह्य — **वर्चस्या उपदधाति**, **तेजस्या**,\n'
        '  पयस्याः, रेतस्याः.\n'
        '\n'
        'SETTLED — Four counter-examples, one for each word: तद्वानिति किम्?\n'
        '  मन्त्रसमुदायादेव मा भूत्. उपधान इति किम्?\n'
        '  **वर्चस्वानुपस्थानमन्त्रः**. मन्त्र इति किम्? **अङ्गुलिमानुपधानो\n'
        '  हस्तः**. इष्टकास्विति किम्? **वर्चस्वानुपधानमन्त्र एषां\n'
        '  कपालानाम्**.\n'
        '\n'
        'SETTLED — **इतिकरणो नियमार्थः; अनेकपदसंभवेऽपि केनचिदेव पदेन तद्वान्\n'
        '  मन्त्रो गृह्यते, न सर्वेण** — and the इति restricts: though a\n'
        '  mantra may have many words, it counts as *having that* by ONE of\n'
        '  them and not by all'
    ),
    '4.4.126': (
        'SETTLED — अश्विमानण्, **पूर्वस्य यतोऽपवादः**. **अश्विनीरुपदधाति**\n'
        '  (शतपथब्राह्मण ८.२.१.१). And when the मतुप् goes, **इनण्यनपत्ये**\n'
        '  [6.4.164] इति प्रकृतिभावः keeps the stem whole where 4.3.108\n'
        '  needed a vārttika to cut it'
    ),
    '4.4.127': (
        'SETTLED — वयस्यासु मूर्ध्नो मतुप्, **पूर्वस्य यतोऽपवादः**. **मूर्धा\n'
        '  वयः प्रजापतिश्छन्दः** — where one mantra has BOTH words, it is\n'
        '  वयस्वान् and मूर्धन्वान् alike, and from the second the यत् would\n'
        '  have come; मतुप् is given instead. **मूर्धन्वतीर्भवन्ति**.\n'
        '\n'
        'SETTLED — **मूर्धन्वत इति वक्तव्ये मूर्ध्न इत्युक्तम्, मतुपो लुकं\n'
        '  भाविनं चित्ते कृत्वा** — the rule names the bare stem where it\n'
        '  should have named the मतुप्-form, with the coming elision of that\n'
        '  मतुप् already in mind. A rule worded for a state that does not yet\n'
        '  exist'
    ),
    '4.4.128': (
        'SETTLED — मत्वर्थे मासतन्वोः. **मत्वर्थीयानामपवादः** — an exception\n'
        '  to the whole class of possessive affixes, where the thing is a\n'
        '  MONTH or a BODY. नभांसि विद्यन्ते यस्मिन् मासे **नभस्यः**;\n'
        '  **सहस्यः**, **तपस्यः**, मधव्यः — the Vedic month-names. ओजोऽस्यां\n'
        '  विद्यत **ओजस्या तनूः**.\n'
        '\n'
        'SETTLED — मासतन्वोरिति किम्? **मधुमता पात्रेण चरति**. And a\n'
        '  vārttika adds four more endings for the months:\n'
        '  **लुगकारेकाररेफाश्च** — तपश्च तपस्यश्च by the elision, **इषः** and\n'
        '  **ऊर्जः** by अ, **शुचिः** by इ, **शुक्रः** by र. Six ways of\n'
        '  naming a month, all from one rule and its supplement'
    ),
    '4.4.129': (
        'SETTLED — मधोर्ञ च — the ञ, and by the च the यत्; and\n'
        '  **उपसंख्यानात् लुक् च**, the elision by a supplement. **माधवः**,\n'
        '  **मधव्यः**, **मधुः** — three names for one month, and the first is\n'
        '  the ordinary word for spring'
    ),
    '4.4.130': (
        'SETTLED — ओजसोऽहनि यत्खौ, मत्वर्थ इत्येव. **ओजस्यमहः**,\n'
        '  **ओजसीनमहः** — a day that has vigour in it'
    ),
    '4.4.131': (
        'SETTLED — वेशोयशआदेर्भगाद् यल्, मत्वर्थ इत्येव. **लकारः\n'
        '  स्वरार्थः**. वेशोभगो विद्यते यस्य स **वेशोभग्यः**; यशोभग्यः.\n'
        '\n'
        'SETTLED — **वेश इति बलमुच्यते; श्रीकामप्रयत्नमाहात्म्यवीर्ययशस्सु\n'
        '  भगशब्दः** — वेश is strength, and भग is fortune, desire, effort,\n'
        '  greatness, vigour or fame: six senses in the second member alone'
    ),
    '4.4.132': (
        'SETTLED — ख च. **योगविभागो यथासंख्यनिरासार्थ उत्तरार्थश्च** — the\n'
        '  rule is split BOTH to stop a pairing and for the sake of what\n'
        '  follows, which is the first time in the project a split has been\n'
        '  given two purposes at once. **वेशोभगीनः**, वेशोभग्यः; यशोभगीनः,\n'
        '  यशोभग्यः'
    ),
    '4.4.133': (
        'SETTLED — पूर्वैः कृतमिनयौ च. **मत्वर्थ इति निवृत्तम्**.\n'
        '  **गम्भीरेभिः पथिभिः पूर्विणेभिः**; **पूर्व्यैः**; पूर्वीणैः.\n'
        '\n'
        'SETTLED — **पूर्वैरिति बहुवचनान्तेन पूर्वपुरुषा उच्यन्ते; तत्कृताः\n'
        '  पन्थानः प्रशस्ता इति पथां प्रशंसा** — the plural names the men of\n'
        '  old, and roads THEY made are praised roads. The rule is a\n'
        '  compliment'
    ),
    '4.4.134': (
        'SETTLED — अद्भिः संस्कृतम्. **यस्येदमप्यं हविः** (ऋग्वेद १०.८६.१२)\n'
        '  — the offering prepared with water'
    ),
    '4.4.135': (
        'SETTLED — सहस्रेण संमितौ घः. **संमितस्तुल्यः सदृशः**. **अयमग्निः\n'
        '  सहस्रियः** (तैत्तिरीयसंहिता ४.७.१३.४), *worth a thousand*.\n'
        '\n'
        'SETTLED — **केचित्तु समिताविति पठन्ति; तत्रापि समित्या संमित एव\n'
        '  लक्षयितव्यः** — some read the word without the prefix, and even\n'
        '  then the sense has to be *measured against*. A variant reading\n'
        '  admitted and then read back to the same meaning'
    ),
    '4.4.136': (
        'SETTLED — मतौ च. सहस्रमस्य विद्यते **सहस्रियः** — an exception to\n'
        '  **तपःसहस्राभ्यां विनीनी** [5.2.102] and **अण् च** [5.2.103], two\n'
        '  rules in the chapter after this one'
    ),
    '4.4.137': (
        'SETTLED — सोममर्हति यः. **सोममर्हन्ति सोम्या ब्राह्मणाः**\n'
        '  (काठकसंहिता ५.२), **यज्ञार्हा इत्यर्थः** — brahmins fit to receive\n'
        '  the soma. **यति प्रकृते यग्रहणम्; स्वरे विशेषः**: यत् was already\n'
        '  carrying, and य is named instead for the accent alone'
    ),
    '4.4.138': (
        'SETTLED — मये च. **मय इति मयडर्थो लक्ष्यते** — the syllable stands\n'
        '  for the sense of मयट्, and the vṛtti lists every rule that gives\n'
        '  it: 4.3.81, 4.3.82, 4.3.143 and 5.4.21. **आगतविकारावयवप्रकृता\n'
        '  मयडर्थाः**, four senses gathered under one name. **पिबाति सोम्यं\n'
        '  मधु** (ऋग्वेद ८.२४.१३), सोममयम्'
    ),
    '4.4.139': (
        'SETTLED — मधोः. **यशब्दो निवृत्तः** — the य of the last rule has\n'
        "  lapsed and the heading's यत् returns. **मधव्यान् स्तोकान्**\n"
        '  (पैप्पलादसंहिता १.८८.२), मधुमयान्'
    ),
    '4.4.140': (
        'SETTLED — वसोः समूहे च. **वसव्यः समूहः**, and by the च in the मयट्\n'
        '  sense too.\n'
        '\n'
        'SETTLED — **अक्षरसमूहे छन्दसः स्वार्थ उपसंख्यानम्** — a vārttika\n'
        '  gives the affix to छन्दस् in its own sense when a count of\n'
        '  SYLLABLES is meant, and the vṛtti works the count: ओश्रावय four,\n'
        '  अस्तु श्रौषट् four, यज two, ये यजामहे five, वषट्कार two — **एष वै\n'
        '  सप्तदशाक्षरश् छन्दस्यः प्रजापतिर्यज्ञो मन्त्रे विहितः**. Seventeen\n'
        '  syllables, added up in the commentary'
    ),
    '4.4.141': (
        'SETTLED — नक्षत्राद् घः, स्वार्थे. **समूह इति नानुवर्तते** — the\n'
        '  collection-sense does not carry. **नक्षत्रियेभ्यः स्वाहा**\n'
        '  (माध्यन्दिनसंहिता २२.२८)'
    ),
    '4.4.142': (
        'SETTLED — सर्वदेवात् तातिल्, छन्दसि; स्वार्थिकः. **सर्वतातिम्**\n'
        '  (ऋग्वेद १०.३६.१४), **देवतातिम्** (ऋग्वेद ३.१९.२) — an affix that\n'
        '  changes nothing but the shape'
    ),
    '4.4.143': (
        'SETTLED — शिवशमरिष्टस्य करे. **करोतीति करः प्रत्ययार्थः**. शिवं\n'
        '  करोतीति **शिवतातिः**; **शंतातिः**, **अरिष्टतातिः** — *making\n'
        '  blessed*, *making peace*, *making unharmed*'
    ),
    '4.4.144': (
        'SETTLED — भावे च. शिवस्य भावः **शिवतातिः** — the same three words\n'
        '  and the same affix, now for the STATE and not the making. One form\n'
        '  for both, and only the context divides them.\n'
        '\n'
        'SETTLED — **AND THE PĀDA AND THE CHAPTER END BY CLOSING THE\n'
        '  HEADING.** **यतः पूर्णोऽवधिः, अतः परमन्यः प्रत्ययो ऽधिक्रियते** —\n'
        "  word for word what 4.4.74 said of ठक्. So यत्'s marker is 5.1.5\n"
        '  and its last rule is this one, because 5.1.1 प्राक्क्रीताच्छः\n'
        '  opens छ inside the range. Twice in one pāda, and the second time\n'
        "  settles that the gap between a heading's MARKER and its LAST RULE\n"
        '  is how these headings nest.\n'
        '\n'
        'SETTLED — इति काशिकायां वृत्तौ चतुर्थाध्यायस्य चतुर्थः पादः'
    ),
}

_BY_MEANS_OF_LINE = (
    'by_means_of(stem, gana=..., sense=..., case=..., result=..., '
    'samjna=..., upadha=..., vowels=..., pre=..., elided=..., '
    'wants=...) -> which affix comes for that action, from a base in '
    'that case.'
)

_REUSES = {}

for _sutra, _notes in _RULES.items():
    register(
        _sutra,
        apply=by_means_of,
        codification=_BY_MEANS_OF_LINE,
        notes=_notes,
        reuses=_REUSES.get(_sutra, ()),
    )
