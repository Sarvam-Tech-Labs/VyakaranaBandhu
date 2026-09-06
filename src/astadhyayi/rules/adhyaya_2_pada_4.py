# -*- coding: utf-8 -*-
r"""अध्याय २, पाद ४ — what number a compound counts as, and what gender."""

from __future__ import annotations

from src.astadhyayi.adesa_dhatu import substitute
from src.astadhyayi.anga import adiprabhrtibhyah_sapah
from src.astadhyayi.pratyaya_luk import (
    avyaya_ending, lut_prathama, verbal_luk,
)
from src.astadhyayi.samasalinga import ekavat, gender
from src.astadhyayi.sanadi import yan_luk
from src.astadhyayi.sources import register
from src.astadhyayi.taddhita_luk import sup_luk, taddhita_luk

_EKAVAT = (
    "ekavat(Compound(...)) -> whether the compound counts as ONE, and by "
    "which rule, or which प्रतिषेध refused it."
)
_GENDER = (
    "gender(Compound(...)) -> which gender the compound takes, or whose "
    "gender it borrows, and by which rule."
)

_NUMBER = {
    "2.4.1": (
        'SETTLED — द्विगुरेकवचनम्, and only of the समाहार द्विगु:\n'
        '  समाहारद्विगोश्चेदं ग्रहणम्, नान्यस्य. पञ्चपूली, दशपूली.\n'
        '\n'
        'SETTLED — एकवचन here is NOT the technical एकवचन of 1.4.102. The\n'
        '  Nyāsa argues it out: were it technical, पञ्चपूलीयं शोभना could\n'
        '  not be singular, अनुप्रयोगस्याद्विगुत्वात् — शोभना is not\n'
        '  itself a द्विगु. So the word is taken in its own sense,\n'
        '  एकस्य वचनम्, that which speaks of one. What is conferred is\n'
        '  oneness of MEANING; the ending follows from it. The code\n'
        '  returns `singular`, and this is what that word means here.\n'
        '\n'
        'SETTLED — the Mahābhāṣya asks why the rule is needed at all, and\n'
        '  answers: प्रत्यधिकरणं वचनोत्पत्तेः संख्यासामानाधिकरण्याच्च —\n'
        '  1.4.21 बहुषु बहुवचनम् would have given a plural, since the\n'
        '  compound stands in apposition with a numeral meaning many.'
    ),
    "2.4.2": (
        'SETTLED — द्वन्द्वश्च प्राणितूर्यसेनाङ्गानाम्: पाणिपादम्,\n'
        '  मार्दङ्गिकपाणविकम्, रथिकाश्वारोहम्.\n'
        '\n'
        'SETTLED — अङ्ग goes with each of the three SEPARATELY:\n'
        '  अङ्गशब्दस्य प्रत्येकं वाक्यपरिसमाप्त्या त्रीणि वाक्यानि\n'
        '  संपद्यन्ते. Read as one sentence it would cover a limb\n'
        '  compounded with a drum-part — व्यतिकीर्णावयवो द्वन्द्वः — and\n'
        '  the Nyāsa closes that off: न हि चतुर्थं वाक्यमस्ति. The three\n'
        '  are a tuple here and a mixed pair matches none of them.\n'
        '\n'
        'SETTLED — and this rule is overridden by 2.4.12 for पशु and\n'
        '  शकुनि, परत्वात्, by 1.4.2. The vṛtti says so in its own words:\n'
        '  हस्त्यश्वादिषु परत्वात् पशुद्वन्द्वे विभाषयैकवद् भवति.'
    ),
    "2.4.3": (
        'SETTLED — अनुवादे चरणानाम्: उदगात् कठकालापम्.\n'
        '\n'
        'SETTLED — चरण names the MEN, by way of the recension they\n'
        '  follow: चरणशब्दः शाखानिमित्तकः पुरुषेषु वर्तते. Where the word\n'
        '  names the recension itself, 2.4.6 जातिरप्राणिनाम् has it\n'
        '  already, so this rule would be redundant — the Nyāsa makes\n'
        '  exactly that argument to fix the scope.\n'
        '\n'
        'SETTLED — अनुवाद is restating what is known otherwise:\n'
        '  प्रमाणान्तरावगतस्य अर्थस्य शब्देन संकीर्तनमात्रम्. Said for the\n'
        '  first time, the schools stay many: उदगुः कठकालापाः.\n'
        '\n'
        'SETTLED — the vārttika स्थेणोरद्यतन्यां च holds the rule to two\n'
        '  roots in one tense. Both counters are codified: अनन्दिषुः\n'
        '  कठकालापाः is another root, उद्यन्ति कठकालापाः another tense.'
    ),
    "2.4.4": (
        'SETTLED — अध्वर्युक्रतुरनपुंसकम्: अर्काश्वमेधम्. An\n'
        '  अध्वर्युक्रतु is a rite laid down in the Yajurveda —\n'
        '  अध्वर्युवेदे यस्य क्रतोर्विधानम्.\n'
        '\n'
        'SETTLED — अनपुंसकम् keeps out the rite-names that are\n'
        '  themselves neuter: राजसूयवाजपेये.\n'
        '\n'
        'SETTLED — दर्शपौर्णमासौ escapes for a reason worth keeping:\n'
        '  क्रतुशब्दः सोमयागेषु रूढः, the word क्रतु is fixed by usage to\n'
        '  the soma rites and does not reach every ritual.'
    ),
    "2.4.5": (
        'SETTLED — अध्ययनतोऽविप्रकृष्टाख्यानाम्: पदकक्रमकम्,\n'
        '  क्रमकवार्त्तिकम्. संपाठः पदानां क्रमस्य च प्रत्यासन्नः — what\n'
        '  they recite stands close together.\n'
        '\n'
        'SETTLED — both counters are conditions, not decoration.\n'
        '  पितापुत्रौ fails अध्ययनतः: their nearness is not by study.\n'
        '  याज्ञिकवैयाकरणौ fails अविप्रकृष्ट: both study, but not the\n'
        '  same thing.'
    ),
    "2.4.6": (
        'SETTLED — जातिरप्राणिनाम्: आराशस्त्रि, धानाशष्कुलि.\n'
        '\n'
        'SETTLED — only classes of SUBSTANCE, by नञिवयुक्तन्याय:\n'
        '  द्रव्यजातीनामयमेकवद्भावः, न गुणक्रियाजातीनाम्. A quality-class\n'
        '  (रूपरसगन्धस्पर्शाः) and an action-class\n'
        '  (गमनाकुञ्चनप्रसारणानि) both stay many, so the field carries\n'
        '  which KIND of class it is and not a bare yes.\n'
        '\n'
        'SETTLED — and the class must be what is MEANT: जातिपरत्वे च …\n'
        '  न नियतद्रव्यविवक्षायाम्. इह कुण्डे बदरामलकानि तिष्ठन्ति —\n'
        '  particular fruits in a particular bowl, so the kinds are not\n'
        '  in view and the compound is not made one.'
    ),
    "2.4.7": (
        'SETTLED — विशिष्टलिङ्गो नदी देशोऽग्रामाः: गङ्गाशोणम्,\n'
        '  कुरुकुरुक्षेत्रम्.\n'
        '\n'
        'SETTLED — नदी देश इत्यसमासनिर्देश एवायम्. The two words are NOT\n'
        '  compounded in the sūtra, so they are separate conditions and\n'
        '  a river-and-region pair is not what is meant. Codified as two\n'
        '  values of one slot rather than as a joint condition.\n'
        '\n'
        'SETTLED — जनपदो हि देशः, a देश is a settled country. That is why\n'
        '  mountains are untouched: कैलासगन्धमादने.\n'
        '\n'
        'SETTLED — two vārttikas widen the अग्राम exclusion, and both are\n'
        '  codified: नगराणां प्रतिषेधो वक्तव्यः puts मथुरापाटलिपुत्रम्\n'
        '  out, and उभयतश्च ग्रामाणां प्रतिषेधो वक्तव्यः puts out a\n'
        '  town-and-village pair too — सौर्यकेतवते.'
    ),
    "2.4.8": (
        'SETTLED — क्षुद्रजन्तवः: दंशमशकम्, यूकालिक्षम्.\n'
        '\n'
        'SETTLED — the Kāśikā puts two definitions side by side —\n'
        '  क्षुद्रजन्तुरनस्थिः स्यादथ वा क्षुद्र एव यः, boneless or simply\n'
        '  small — and then settles it: आ नकुलादपीतीयमेव स्मृतिः\n'
        '  प्रमाणम्, इतरासां तद्विरोधात्. Up to and including the\n'
        '  mongoose. The bound is recorded because the vṛtti chose it.'
    ),
    "2.4.9": (
        'SETTLED — येषां च विरोधः शाश्वतिकः: मार्जारमूषकम्, अहिनकुलम्.\n'
        '  विरोधो वैरम्, शाश्वतिको नित्यः — enmity by nature.\n'
        '\n'
        'SETTLED — शाश्वतिक इति किम्? गोपालिशालङ्कायनाः कलहायन्ते. Men\n'
        '  who happen to be quarrelling are not enemies.\n'
        '\n'
        'SETTLED — the च is the whole point of the rule ORDER here.\n'
        '  चकारः पुनरस्यैव समुच्चयार्थः: तेन पशुशकुनिद्वन्द्वे विरोधिनाम्\n'
        '  अनेन नित्यम् एकवद्भावो भवति — अश्वमहिषम्, काकोलूकम्. So the\n'
        '  option 2.4.12 opens over 2.4.2 is shut again for the animals\n'
        '  that are enemies, and this row is therefore tested BEFORE\n'
        '  2.4.12 rather than in numerical order.'
    ),
    "2.4.10": (
        'SETTLED — शूद्राणामनिरवसितानाम्: तक्षायस्कारम्,\n'
        '  रजकतन्तुवायम्.\n'
        '\n'
        'SETTLED — निरवसित is glossed by the vṛtti itself: निरवसानं\n'
        '  बहिष्करणम्, कुतो बहिष्करणम्? पात्रात् — यैर्भुक्ते पात्रं\n'
        '  संस्कारेणापि न शुध्यति. The counter is चण्डालमृतपाः. Recorded\n'
        '  as the commentary states it; this project describes what the\n'
        '  grammar says, and does not endorse it.'
    ),
    "2.4.11": (
        'SETTLED — गवाश्वप्रभृतीनि च, read from the gaṇapāṭha on disk:\n'
        '  twenty-nine finished forms.\n'
        '\n'
        'SETTLED — and they are forms, not a pattern. The Mahābhāṣya:\n'
        '  गवाश्वप्रभृतिषु यथोच्चारितं द्वन्द्ववृत्तम्, and the Kāśikā adds\n'
        '  रूपान्तरे तु नायं विधिर्भवति — गोऽश्वम् and गोऽश्वौ are a\n'
        '  different shape and fall back to 2.4.12, पशुद्वन्द्वविभाषैव\n'
        '  भवति. So the row keys on the FORM and not on the members.'
    ),
    "2.4.12": (
        'SETTLED — विभाषा for the ten the sūtra names in its own body:\n'
        '  प्लक्षन्यग्रोधम् beside प्लक्षन्यग्रोधाः, दधिघृतम् beside\n'
        '  दधिघृते.\n'
        '\n'
        'SETTLED — the list is READ FROM THE SŪTRA, not from a gaṇa. The\n'
        '  gaṇapāṭha on disk has no वृक्षादि for this rule, and it should\n'
        '  not: the ten words stand in the sūtra itself.\n'
        '\n'
        'SETTLED — the vārttika बहुप्रकृतिः फलसेनावनस्पतिमृगशकुनि-\n'
        '  क्षुद्रजन्तुधान्यतृणानाम् holds the option to MORE than two for\n'
        '  eight of them: एषां बहुप्रकृतिरेव द्वन्द्व एकवद् भवति, न\n'
        '  द्विप्रकृतिः. बदरामलके and प्लक्षन्यग्रोधौ stay dual, so the\n'
        '  table carries a member COUNT and not only a kind.'
    ),
    "2.4.13": (
        'SETTLED — विप्रतिषिद्धं चानधिकरणवाचि: शीतोष्णम् beside शीतोष्णे,\n'
        '  सुखदुःखम्, जीवितमरणम्.\n'
        '\n'
        'SETTLED — विभाषानुकर्षणार्थश्चकारः. The च drags 2.4.12\'s option\n'
        '  down, so this rule too is a choice and not obligatory. The\n'
        '  same device as 2.3.73\'s च, which drags an option down over a\n'
        '  case-ending.\n'
        '\n'
        'SETTLED — both counters are real. कामक्रोधौ fails विप्रतिषिद्ध:\n'
        '  desire and anger are not opposites. शीतोष्णे उदके fails\n'
        '  अनधिकरणवाचि: there the words name the WATER that is hot and\n'
        '  cold rather than the qualities themselves.'
    ),
    "2.4.14": (
        'SETTLED — न दधिपयआदीनि, a प्रतिषेध: दधिपयसी, वाङ्मनसे, ऋक्सामे.\n'
        '  यथायथमेकवद्भावे प्राप्ते प्रतिषेध आरभ्यते — each of them was\n'
        '  otherwise caught by some rule above, which is why the\n'
        '  prohibition is written at all.\n'
        '\n'
        'SETTLED — the members are शब्दरूप, word-shapes, and the Kāśikā\n'
        '  gives them as finished DUAL forms. So the row keys on the\n'
        '  form, as 2.4.11 does.\n'
        '\n'
        'SCOPE — the gaṇapāṭha file on disk carries no members for this\n'
        '  gaṇa, so the list here is the Kāśikā\'s own enumeration and is\n'
        '  cited to it. Not taken from disk, and the note says so rather\n'
        '  than leaving a reader to assume it was.\n'
        '\n'
        'SETTLED — refusing IS this rule acting, so it reports itself.\n'
        '  That is not the scar 2.3.72 records: there a rule EXCEPTED a\n'
        '  word and another rule supplied the answer; here the rule\'s\n'
        '  whole content is the prohibition.'
    ),
    "2.4.15": (
        'SETTLED — अधिकरणैतावत्त्वे च, the second प्रतिषेध: दश दन्तोष्ठाः,\n'
        '  दश मार्दङ्गिकपाणविकाः.\n'
        '\n'
        'SETTLED — अधिकरणं वर्त्तिपदार्थः, the thing the compound\'s\n'
        '  meaning rests on: स हि समासस्यार्थस्याधारः. Where ten of them\n'
        '  are counted, the compound cannot at the same time be one.'
    ),
    "2.4.16": (
        'SETTLED — विभाषा समीपे: उपदशं दन्तोष्ठम् beside उपदशा\n'
        '  दन्तोष्ठाः. Near the count 2.4.15 refuses for, the choice is\n'
        '  open again — so this row is tested BEFORE the prohibition it\n'
        '  answers, or the prohibition would swallow it.\n'
        '\n'
        'SETTLED — and the two readings differ in more than number. The\n'
        '  vṛtti: तत्रैकवद्भावपक्षेऽव्ययीभावोऽनुप्रयुज्यते, इतरत्र\n'
        '  बहुव्रीहिः — on the एकवत् reading the उप- word is an\n'
        '  अव्ययीभाव, on the other a बहुव्रीहि.'
    ),
}

_GENDERS = {
    "2.4.17": (
        'SETTLED — स नपुंसकम्: यस्यायमेकवद्भावो विहितः स नपुंसकलिङ्गो\n'
        '  भवति. पञ्चगवम्, पाणिपादम्.\n'
        '\n'
        'SETTLED — the rule has NO content of its own. स points back at\n'
        '  2.4.1 to 2.4.16, so the implementation ASKS that table rather\n'
        '  than restating which compounds count as one. The same shape\n'
        '  as 2.3.50 षष्ठी शेषे, which cannot be computed before the\n'
        '  things it is the remainder of. This is the one place in the\n'
        '  pāda where code genuinely runs other code, and it is declared.\n'
        '\n'
        'SETTLED — परवल्लिङ्गतापवादो योगः: written to beat 2.4.26, which\n'
        '  is why it is tested before it.\n'
        '\n'
        'SCOPE — four vārttikas on the feminine of a द्विगु —\n'
        '  पञ्चपूली, दशरथी, पञ्चखट्वी, पञ्चतक्षी, with a प्रतिषेध for\n'
        '  पात्रादि (पञ्चपात्रम्, चतुर्युगम्, त्रिभुवनम्). They turn on\n'
        '  ङीप् and the समासान्त section, neither codified. Recorded.'
    ),
    "2.4.18": (
        'SETTLED — अव्ययीभावश्च: अधिस्त्रि, उपकुमारि, उन्मत्तगङ्गम्.\n'
        '\n'
        'SETTLED — why it must be STATED, in the vṛtti\'s own words:\n'
        '  पूर्वपदार्थप्रधानस्यालिङ्गतैव प्राप्ता, अन्यपदार्थप्रधानस्य\n'
        '  अभिधेयवल्लिङ्गता. A compound whose first member carries the\n'
        '  meaning would have had no gender at all; one whose meaning\n'
        '  lies outside it would take its referent\'s. Neither is the\n'
        '  neuter, so the neuter has to be given.\n'
        '\n'
        'SCOPE — अनुक्तसमुच्चयार्थश्चकारः, and three vārttikas ride on\n'
        '  that च: पुण्याहम् and सुदिनाहम्, त्रिपथम् and चतुष्पथम्, and\n'
        '  adverbs — मृदु पचति, शोभनं पचति. Recorded, not modelled: the\n'
        '  last of them is about क्रियाविशेषण and not about compounds.'
    ),
    "2.4.19": (
        'SETTLED — तत्पुरुषोऽनञ् कर्मधारयः is an अधिकार, not a rule that\n'
        '  fires: अधिकारोऽयमुत्तरसूत्रेषूपतिष्ठते. It governs 2.4.20 to\n'
        '  2.4.25 and puts two तत्पुरुष outside them.\n'
        '\n'
        'SETTLED — the two excluded are असेना (नञ्) and परमसेना\n'
        '  (कर्मधारय), and कर्मधारय is not restated here: 1.2.42\n'
        '  तत्पुरुषः समानाधिकरणः कर्मधारयः is codified and is asked.\n'
        '  Anything another rule decides is fetched from that rule.\n'
        '\n'
        'SETTLED — तत्पुरुष इति किम्? दृढसेनो राजा, a बहुव्रीहि. And the\n'
        '  vṛtti shows the अधिकार working by pointing forward to 2.4.25:\n'
        '  ब्राह्मणसेनम्, ब्राह्मणसेना.'
    ),
    "2.4.20": (
        'SETTLED — संज्ञायां कन्थोशीनरेषु: सौशमिकन्थम्, आह्वरकन्थम्.\n'
        '  Both counters are conditions — वीरणकन्था is no name,\n'
        '  दाक्षिकन्था is not among the Uśīnaras.\n'
        '\n'
        'SETTLED — परवल्लिङ्गतापवाद इदं प्रकरणम्. The vṛtti says it of\n'
        '  this rule and it holds for the whole run to 2.4.25: every one\n'
        '  of them exists to beat 2.4.26.'
    ),
    "2.4.21": (
        'SETTLED — उपज्ञोपक्रमं तदाद्याचिख्यासायाम्:\n'
        '  पाणिन्युपज्ञमकालकं व्याकरणम्, आढ्योपक्रमं प्रासादः,\n'
        '  नन्दोपक्रमाणि मानानि. आख्यातुमिच्छा आचिख्यासा.\n'
        '\n'
        'SETTLED — the condition is narrow and the counter shows how:\n'
        '  देवदत्तोपज्ञो रथः is a chariot Devadatta first thought of, but\n'
        '  the wish is not to tell of its BEGINNING, so no neuter.'
    ),
    "2.4.22": (
        'SETTLED — छाया बाहुल्ये: शलभच्छायम्, इक्षुच्छायम्.\n'
        '  पूर्वपदार्थधर्मो बाहुल्यम् — the abundance belongs to the\n'
        '  first member; it is the locusts that are many.\n'
        '\n'
        'SETTLED — why the rule exists at all, given 2.4.25 three sūtras\n'
        '  later: नित्यार्थमिदं वचनम्. 2.4.25 offers छाया a choice; this\n'
        '  makes it obligatory where abundance is meant. Without\n'
        '  बाहुल्य the option is all there is — कुड्यच्छाया.'
    ),
    "2.4.23": (
        'SETTLED — सभा राजामनुष्यपूर्वा: इनसभम्, ईश्वरसभम्; रक्षःसभम्,\n'
        '  पिशाचसभम्.\n'
        '\n'
        'SETTLED — राजसभा itself is NOT covered, and the reason is a\n'
        '  paribhāṣā: पर्यायवचनस्यैवेष्यते, जित् पर्यायस्यैव राजाद्यर्थम्\n'
        '  (vārttika on 1.1.68). Only SYNONYMS of राजन् are meant, not\n'
        '  the word itself.\n'
        '\n'
        'SETTLED — and काष्ठसभा escapes because अमनुष्य is not read as\n'
        '  "whatever is not a man": अमनुष्यशब्दो रूढिरूपेण रक्षःपिशाचादिषु\n'
        '  एव वर्तते, it is fixed by usage to demons and spirits.'
    ),
    "2.4.24": (
        'SETTLED — अशाला च: स्त्रीसभम्, दासीसभम्.\n'
        '\n'
        'SETTLED — सभा is taken here in a different sense from 2.4.23:\n'
        '  सङ्घातवचनोऽत्र सभाशब्दो गृह्यते, दासीसङ्घात इत्यर्थः — a\n'
        '  gathering of people, not a hall. अशालेति किम्? अनाथसभा, which\n'
        '  the vṛtti glosses अनाथकुटी, a shelter.'
    ),
    "2.4.25": (
        'SETTLED — विभाषा सेनासुराच्छायाशालानिशानाम्, five words and an\n'
        '  option apiece: ब्राह्मणसेनम् beside ब्राह्मणसेना, गोशालम्\n'
        '  beside गोशाला.\n'
        '\n'
        'SETTLED — छाया appears both here and at 2.4.22, and the two do\n'
        '  not conflict: 2.4.22 takes the बाहुल्य sense and makes it\n'
        '  obligatory, this leaves the rest a choice.'
    ),
    "2.4.26": (
        'SETTLED — परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः, the general rule\n'
        '  everything from 2.4.17 to 2.4.25 was written to beat:\n'
        '  कुक्कुटमयूर्याविमे but मयूरीकुक्कुटाविमौ, अर्धपिप्पली.\n'
        '\n'
        'SETTLED — it names no gender, it names a MEMBER. So the answer\n'
        '  is a slot and not a gender-name: returning one would be\n'
        '  inventing an answer the sūtra does not give.\n'
        '\n'
        'SETTLED — only the इतरेतरयोग द्वन्द्व is left to it:\n'
        '  समाहारद्वन्द्वे नपुंसकलिङ्गस्य विहितत्वाद् इतरेतरयोगद्वन्द्वस्य\n'
        '  इदं ग्रहणम्. 2.4.17 has taken the समाहार already.\n'
        '\n'
        'SETTLED — the vārttika द्विगुप्राप्तापन्नालंपूर्वगतिसमासेषु\n'
        '  प्रतिषेधो वक्तव्यः keeps it off five kinds: पञ्चकपालः,\n'
        '  प्राप्तजीविकः, आपन्नजीविकः, अलंजीविकः, निष्कौशाम्बिः. All five\n'
        '  are codified as a closed tuple.'
    ),
    "2.4.27": (
        'SETTLED — पूर्ववदश्ववडवौ: masculine after अश्व, not feminine\n'
        '  after वडवा. An apavāda of 2.4.26 for one compound.\n'
        '\n'
        'SETTLED — अर्थातिदेशश्चायम् न निपातनम्. It transfers the SENSE\n'
        '  rather than fixing a form, and the consequence is drawn:\n'
        '  तत्र द्विवचनमतन्त्रम्, वचनान्तरेऽपि पूर्ववल्लिङ्गता भवति —\n'
        '  the dual in the sūtra is not binding, and अश्ववडवान् and\n'
        '  अश्ववडवैः go the same way. So the row keys on the compound\n'
        '  and not on its number.'
    ),
    "2.4.28": (
        'SETTLED — हेमन्तशिशिरावहोरात्रे च च्छन्दसि: in the Veda both\n'
        '  take the FIRST member\'s gender, continuing 2.4.27\'s पूर्ववत्.\n'
        '\n'
        'SETTLED — it overrides two different rules at once, and the\n'
        '  Nyāsa says which. For हेमन्तशिशिरौ it is a नपुंसकत्वापवाद,\n'
        '  since शिशिर is neuter and 2.4.26 would have taken it. For\n'
        '  अहोरात्रे it is a पुंल्लिङ्गत्वापवाद, since 2.4.29 रात्राह्नाहाः\n'
        '  पुंसि would have given the masculine — छन्दसि लिङ्गव्यत्यय\n'
        '  उक्तः, by व्यत्ययो बहुलम् 3.1.85.\n'
        '\n'
        'SCAR — THE KĀŚIKĀ ON DISK FOR THIS SŪTRA IS THE WRONG TEXT. What\n'
        '  `reference/` holds under 2.4.28 is a vṛtti on a छ-affix rule —\n'
        '  अपोनप्तृ, अपोनप्त्रीयम्, शतरुद्रीयम् — with nothing to do with\n'
        '  हेमन्तशिशिरौ. Had this rule been codified from the first\n'
        '  commentary that answered, it would have been codified as a\n'
        '  taddhita rule in the middle of the gender section. Four other\n'
        '  witnesses on disk — Nyāsa, Padamañjarī, Siddhāntakaumudī,\n'
        '  Vasu — agree on the real content and are what it is codified\n'
        '  from. This is the standing argument for reading EVERY\n'
        '  commentary and not the first one that answers.'
    ),
    "2.4.29": (
        'SETTLED — रात्राह्नाहाः पुंसि: द्विरात्रः, पूर्वाह्णः, द्व्यहः.\n'
        '\n'
        'SETTLED — कृतसमासान्तानां निर्देशः. The three are named with\n'
        '  their समासान्त already made, which is why the row keys on\n'
        '  what the compound ENDS in and not on रात्रि, अहन्.\n'
        '\n'
        'SETTLED — why it is written: परवल्लिङ्गतया स्त्रीनपुंसकयोः\n'
        '  प्राप्तयोरिदं वचनम्. 2.4.26 would have given the feminine or\n'
        '  the neuter from रात्रि and अहन्.\n'
        '\n'
        'SCOPE — the vārttika अनुवाकादयः पुंसि adds अनुवाकः, शंयुवाकः,\n'
        '  सूक्तवाकः. Recorded; it is a separate list, not these three.'
    ),
    "2.4.30": (
        'SETTLED — अपथं नपुंसकम्: अपथमिदम्, अपथानि गाहते मूढः.\n'
        '\n'
        'SETTLED — तत्पुरुष इति वर्तते carries down from 2.4.19, and it\n'
        '  is what keeps अपथो देशः and अपथा नगरी out: those are बहुव्रीहि\n'
        '  and take their referent\'s gender. The vṛtti asks exactly that\n'
        '  question — इह कस्माद् न भवति? — and answers it by anuvṛtti.'
    ),
    "2.4.31": (
        'SETTLED — अर्धर्चाः पुंसि च, read from the gaṇapāṭha on disk.\n'
        '  BOTH genders stand: अर्धर्चः and अर्धर्चम्, गोमयः and गोमयम्.\n'
        '  So the answer carries `also`, as 2.3.34 and 2.3.73 do.\n'
        '\n'
        'SETTLED — शब्दरूपाश्रया चेयं द्विलिङ्गता: it attaches to the\n'
        '  word-shape. But क्वचिदर्थभेदेनापि व्यवतिष्ठते — sometimes the\n'
        '  two genders divide a meaning between them. The vṛtti gives\n'
        '  four: पद्म and शङ्ख are masculine as treasures and both as\n'
        '  water-born things; भूत is both of a spirit; सैन्धव is both of\n'
        '  the salt; सार is masculine for excellence and neuter for what\n'
        '  is sound, नैतत् सारम्; धर्म is masculine of the thing itself\n'
        '  and neuter of its means, तानि धर्माणि प्रथमान्यासन्.\n'
        '\n'
        'SETTLED — and this closes the compound section proper. 2.1.1\n'
        '  समर्थः पदविधिः to here: which words may join, which is spoken\n'
        '  first, what the result counts as, and what gender it takes.'
    ),
}

for _sutra, _notes in _NUMBER.items():
    register(
        _sutra,
        apply=ekavat,
        codification=_EKAVAT,
        notes=_notes,
        # No reuse is declared for these sixteen. They are one table and
        # one resolver, so everything any of them does is trivially
        # reachable from every other — the vacuous shape 1.1.15 records.
    )

for _sutra, _notes in _GENDERS.items():
    register(
        _sutra,
        apply=gender,
        codification=_GENDER,
        notes=_notes,
        # 2.4.17 is the one rule here that genuinely runs another's code:
        # स नपुंसकम् has no content but the back-reference, so `gender`
        # calls `ekavat`. 2.4.19 asks 1.2.42 for कर्मधारय by the same
        # standard. Nothing else in the run is a call: 2.4.26 being
        # beaten by 2.4.17 is precedence, which the ORDER expresses.
        reuses=(("2.4.1",) if _sutra == "2.4.17"
                else ("1.2.42",) if _sutra == "2.4.19"
                else ()),
    )


# -------------------------------------------------------------------------
# Two rules of this pāda were codified with the runs that needed
# them, far from 2.4.1 to 2.4.31: the शप् the second gaṇa drops,
# and the यङ् that goes before an अच्. Both belong to the affix
# half of the pāda, 2.4.71 onward, which is not yet read.
# -------------------------------------------------------------------------

register(
    '2.4.72',
    apply=adiprabhrtibhyah_sapah,
    codification=(
        'adiprabhrtibhyah_sapah(root) -> whether शप् is elided by लुक् '
        'after this root.'
    ),
    related=('1.1.61', '1.1.62', '3.1.68'),
    notes='SETTLED — अदिप्रभृतिभ्य उत्तरस्य शपो लुग् भवति: अत्ति, हन्ति,\n  द्वेष्टि. This is what makes the second conjugation look unlike\n  the first — एति beside भवति, with no अ between root and ending.\n\nSETTLED — it is लुक् and not लोप, which matters downstream: 1.1.61\n  names the three elisions apart, and 1.1.63 न लुमताङ्गस्य then\n  withholds from a लुमत् elision what 1.1.62 would otherwise let\n  through on the अङ्ग.\n\nNOTE — अदिप्रभृति is not listed here. It is the second gaṇa, and\n  the dhātupāṭha on disk numbers its own entries, so the rule asks\n  the corpus. A hand-copied list of the अदादि roots would be a\n  second statement of something the data already says, and the\n  kind of thing test_astadhyayi_no_restating exists to refuse.',
)

register(
    '2.4.74',
    apply=yan_luk,
    codification=(
        'yan_luk(stem, before_ac=...) -> the stem with यङ् gone, and what '
        'it was before.'
    ),
    notes='SETTLED — यङो लुग् भवत्यचि प्रत्यये परतः: लोलुवः, पोपुवः,\n  सनीस्रंसः, दनीध्वंसः.\n\nSETTLED — a लुक् takes the affix away and leaves its work standing.\n  The doubling stays and so does everything 7.4 did to the copy,\n  which is the only reason there is a लोलू left to speak of.\n\nSETTLED — this is the elision 1.1.4 calls a धातुलोप, and it counts\n  as one because 3.1.32 has already made the यङन्त stem a root.\n  The Kāśikā there puts the whole chain in a sentence and stresses\n  which affix matters: तमेवाचम् आश्रित्य — it is *that very* अच्,\n  the one that caused the लुक्, whose strengthening is forbidden.\n\nSCOPE — चकारेण बहुलग्रहणमनुकृष्यते, so the लुक् happens outside अच्\n  as well: शाकुनिको लालपीति, दुन्दुभिर्वावदीति. Not modelled — the\n  forms that need it are finite, and this run makes stems.',
)


# -------------------------------------------------------------------------
# 2.4.32 to 2.4.57 — one thing standing in for another.
# -------------------------------------------------------------------------

_SUBSTITUTION = (
    'substitute(of, before=..., sense=..., given=...) -> what stands '
    'in for this root or pronoun, and by which rule.'
)

_ADESA = {
    '2.4.32': 'SETTLED — इदमोऽन्वादेशेऽशनुदात्तस्तृतीयादौ: आभ्यां छात्राभ्यां\n  रात्रिरधीता, अथो आभ्यामहरप्यधीतम्. तृतीयादौ is the third case\n  ONWARD, so the first two are untouched — those go to 2.4.34.\n\nSETTLED — अन्वादेश is not mere later utterance. नेह पश्चाद्\n  उच्चारणमात्रमन्वादेशः; किं तर्हि? एकस्यैवाभिधेयस्य पूर्वं शब्देन\n  प्रतिपादितस्य द्वितीयं प्रतिपादनम् — the SAME referent said a\n  second time. So देवदत्तं भोजय, इमं च यज्ञदत्तम् is not one,\n  and the fact is asserted rather than inferred from position.\n\nSETTLED — the substitute is given as अश् and not as bare अ,\n  and the vṛtti says why: अशादेशवचनं साकच्कार्थम् — so that a\n  form with कच् is reached too, इमकाभ्याम्.',
    '2.4.33': 'SETTLED — एतदस्त्रतसोस्त्रतसौ चानुदात्तौ: एतस्मिन् ग्रामे सुखं\n  वसामः, अथोऽत्र युक्ता अधीमहे.\n\nSETTLED — the substitution was already available from 5.3.5\n  एतदोऽश्. पुनर्वचनमनुदात्तार्थम् — this rule exists for the\n  ACCENT, and the च carries it to त्र and तस् as well, so\n  सर्वानुदात्तं पदं भवति, the whole word is unaccented. The\n  accent is therefore carried in the answer and not dropped.',
    '2.4.34': "SETTLED — द्वितीयाटौस्स्वेनः: इमं छात्रम् … अथो एनम्; अनेन …\n  अथो एनेन; अनयोः … अथो एनयोः. And the same for एतद्.\n\nSETTLED — इदम् is carried down from 2.4.32 over 2.4.33, which\n  names एतद् only: मण्डूकप्लुतिन्यायेन इदमोऽनुवृत्तिः, by the\n  frog's-leap principle. Both stems are therefore on this row.\n\nSCOPE — the vārttika एनदिति नपुंसकैकवचने वक्तव्यम् gives एनद्\n  in the neuter singular: प्रक्षालयैनत्. Recorded; the run does\n  not carry gender.",
    '2.4.35': "SETTLED — आर्धधातुके is an अधिकार, not a rule that fires. The\n  vṛtti gives its extent: ण्यक्षत्रियार्षञितः इति यावत्, so it\n  governs through 2.4.57 and stops before 2.4.58.\n\nSETTLED — विषयसप्तमी चेयं न परसप्तमी. It is a locative of\n  SCOPE and not of what follows: तेनार्धधातुकविवक्षायाम्\n  आदेशेषु कृतेषु पश्चाद् यथाप्राप्तं प्रत्यया भवन्ति — the\n  substitution happens where an आर्धधातुक is intended, and the\n  affix arrives afterwards. भव्यम्, प्रवेयम्, आख्येयम् are the\n  vṛtti's own demonstrations.\n\nSCOPE — what MAKES an affix आर्धधातुक is 3.4.114 आर्धधातुकं\n  शेषः, which is not codified. 3.4.113's सार्वधातुक is, and the\n  complement could be taken here — but taking it would be\n  codifying 3.4.114 without registering it. So the condition is\n  passed in, as the kāraka is at 2.3.1, and this note records\n  the debt.",
    '2.4.36': "SETTLED — अदो जग्धिर्ल्यप्ति किति: प्रजग्ध्य, विजग्ध्य, जग्धः,\n  जग्धवान्. तीति किम्? अद्यते. कितीति किम्? अत्तव्यम्.\n\nSETTLED — इकार उच्चारणार्थः, नानुबन्धः, तेन नुम् न भवति. The इ\n  of जग्धि is there to make the form pronounceable and is not\n  an इत्, so 7.1.58's नुम् does not follow. एवं वच्यादीनामपि —\n  the same holds of वचि at 2.4.53 and गमि at 2.4.46.\n\nSETTLED — ल्यप् is named although जग्धि would have come anyway,\n  being अन्तरङ्ग, and the vṛtti draws the inference: ज्ञापयति\n  अन्तरङ्गाणां ल्यपा भवति बाधनम् — the naming TEACHES that ल्यप्\n  defeats inner operations. A rule stated where it was not\n  needed is doing other work.",
    '2.4.37': "SETTLED — लुङ्सनोर्घस्लृ: अघसत्, अघसताम्, अघसन्; जिघत्सति.\n\nSETTLED — ऌदित्करणमङर्थम्. The ऌ is marked so that 3.1.55 gives\n  अङ् in the aorist, which is what makes अघसत् and not अघासीत्.\n\nSCOPE — the vārttika घस्ऌभावेऽच्युपसंख्यानम् adds अच्: प्रघसः.\n  Recorded; 2.4.38's अप् is the affix this run carries.",
    '2.4.38': 'SETTLED — घञपोश्च: घासः, प्रघसः. The अप् is the one 3.3.59\n  उपसर्गेऽदः gives.',
    '2.4.39': 'SETTLED — बहुलं छन्दसि, and it is genuinely variable: घस्तां\n  नूनम् and सग्धिश्च मे have it, आत्तामद्य does not.\n\nSETTLED — बहुलम् is used where अन्यतरस्याम् would have served\n  for the option alone, and the vṛtti asks exactly that:\n  अन्यतरस्यांग्रहणमेव कस्मान्न क्रियते? कार्यान्तरार्थं\n  बहुलग्रहणम् — it carries other effects too, and one is named:\n  घस्तामित्यत्रोपधालोपो न भवति. So the answer is marked bahulam\n  and not merely optional; they are different claims.',
    '2.4.40': 'SETTLED — लिट्यन्यतरस्याम्: जघास, जक्षतुः, जक्षुः beside आद,\n  आदतुः, आदुः. Both stand.',
    '2.4.41': 'SETTLED — वेञो वयिः, with अन्यतरस्याम् carried down from 2.4.40:\n  उवाय, ऊयतुः, ऊयुः beside ऊवतुः, ऊवुः.\n\nSCOPE — which of 6.1.38, 6.1.39 and 6.1.40 applies turns on\n  which side of the option is taken. Recorded; those three are\n  not codified.',
    '2.4.42': "SETTLED — हनो वध लिङि: वध्यात्, वध्यास्ताम्, वध्यासुः.\n\nSETTLED — अकारान्तश्चायमादेशः, and that final अ is then dropped;\n  being स्थानिवत् by 1.1.56 it keeps 7.2.7's वृद्धि away, so\n  अवधीत् and not *अवाधीत्. The substitute's shape is doing work\n  after it has itself disappeared.",
    '2.4.43': "SETTLED — लुङि च: अवधीत्, अवधिष्टाम्, अवधिषुः.\n\nSETTLED — योगविभाग उत्तरार्थः, and the vṛtti states the purpose\n  exactly: आत्मनेपदेषु लुङि विकल्पो यथा स्याल्लिङि मा भूत्. Had\n  2.4.42 and this been one rule, 2.4.44's option would have\n  reached the benedictive too and वध्यात् would have become a\n  choice. Held by a test that merges the two rows and checks\n  the benedictive answer changes.",
    '2.4.44': 'SETTLED — आत्मनेपदेष्वन्यतरस्याम्: आवधिष्ट, आवधिषाताम्,\n  आवधिषत, beside आहत, आहसाताम्, आहसत.\n\nSETTLED — पूर्वेण नित्ये प्राप्ते विकल्प उच्यते. 2.4.43 had made\n  it obligatory; this makes it a choice. So the table takes the\n  LAST matching row and not the first — 1.4.2 विप्रतिषेधे परं\n  कार्यम्. Taking the first would make the option unreachable,\n  and the same shape recurs at 2.4.55 and 2.4.57.',
    '2.4.45': "SETTLED — इणो गा लुङि: अगात्, अगाताम्, अगुः.\n\nSETTLED — लुङ् was already running and is said AGAIN on purpose:\n  लुङीति वर्तमाने पुनर्लुङ्ग्रहणम् आत्मनेपदेष्वन्यतरस्याम्\n  इत्येतद् मा भूत् — so that 2.4.44's option does not carry down.\n  इह त्वविशेषेण नित्यं च भवति: obligatory in both padas, अगात्\n  and अगायि. Held by a test.\n\nSCOPE — the vārttika इण्वदिक extends it to इक्: अध्यगात्.\n  Recorded; it recurs at 2.4.46 and 2.4.47.",
    '2.4.46': 'SETTLED — णौ गमिरबोधने: गमयति, गमयतः, गमयन्ति. अबोधन इति किम्?\n  प्रत्याययति — where making someone KNOW is meant, the\n  substitute does not come, and the sense is a condition the\n  caller states.',
    '2.4.47': 'SETTLED — सनि च: जिगमिषति. अबोधन carries down — अर्थान्\n  प्रतीषिषति is the counter.\n\nSETTLED — योगविभाग उत्तरार्थः, the second of three in this run:\n  इङश्चेति सन्येव यथा स्यात्. Split from 2.4.46 so that 2.4.48\n  takes सन् alone and not णि. Held by a test that merges them\n  and checks इङ् before णि starts answering.',
    '2.4.48': "SETTLED — इङश्च: अधिजिगांसते, अधिजिगांसेते, अधिजिगांसन्ते.\n  Before सन् only, which is what 2.4.47's split bought.",
    '2.4.49': 'SETTLED — गाङ् लिटि: अधिजगे, अधिजगाते, अधिजगिरे.\n\nSETTLED — गाङोऽनुबन्धकरणं विशेषणार्थम्. The ङ् is marked so that\n  1.2.1 गाङ्कुटादिभ्यः reaches this substitute, and the vṛtti\n  says why marking was necessary: नहि स्थानिवद्भावेन गाङिति रूपं\n  लभ्यते — being स्थानिवत् for इङ् would not have supplied a ङ्\n  the substitute does not have. 1.2.1 is codified.',
    '2.4.50': 'SETTLED — विभाषा लुङ्लृङोः: अध्यगीष्ट beside अध्यैष्ट,\n  अध्यगीष्यत beside अध्यैष्यत.\n\nSETTLED — on the substitution side two further rules follow:\n  1.2.1 makes it ङित् and 6.4.66 gives the ई. Recorded because\n  they are what make the two readings differ in more than the\n  substitute itself.',
    '2.4.51': 'SETTLED — णौ च संश्चङोः: अधिजिगापयिषति beside अध्यापिपयिषति,\n  अध्यजीगपत् beside अध्यापिपत्.\n\nSETTLED — the two locatives are read at different depths, and\n  the vṛtti separates them: णावितीङपेक्षया परसप्तमी, संश्चङोरिति\n  च ण्यपेक्षया. णि follows the root, and सन् or चङ् follows णि —\n  so the row is keyed on the pair and not on णि alone.',
    '2.4.52': 'SETTLED — अस्तेर्भूः, through the whole heading: भविता,\n  भवितुम्, भवितव्यम्.\n\nSETTLED — it does not reach the periphrastic perfect ईहामास,\n  and the argument is one of purpose: 3.1.40 कृञ्चानुप्रयुज्यते\n  लिटि names अस् through a प्रत्याहार, and would be pointless if\n  भू had replaced it there — ग्रहणसामर्थ्यात्.',
    '2.4.53': "SETTLED — ब्रुवो वचिः: वक्ता, वक्तुम्, वक्तव्यम्. The इ is\n  उच्चारणार्थ, as at 2.4.36.\n\nSETTLED — being स्थानिवत् the substitute keeps ब्रू's middle\n  where the fruit of the act falls to the agent: ऊचे, वक्ष्यते.",
    '2.4.54': "SETTLED — चक्षिङः ख्याञ्: आख्याता, आख्यातुम्, आख्यातव्यम्.\n\nSETTLED — the ञ् is marked precisely so the substitute does NOT\n  inherit चक्षिङ्'s obligatory middle: स्थानिवद्भावेन नित्यम्\n  आत्मनेपदं न भवति, ञकारानुबन्धकरणसामर्थ्यात्. Hence आख्यास्यति\n  beside आख्यास्यते. Compare 2.4.49, where a मार्क was added to\n  gain what स्थानिवत्त्व would not give; here one is added to\n  refuse what it would.\n\nSCOPE — three vārttikas. क्शादिरप्ययमादेश इष्यते (आक्शाता);\n  वर्जने प्रतिषेधः (दुर्जनाः संचक्ष्याः); असनयोश्च प्रतिषेधः\n  (नृचक्षाः, विचक्षणः). Recorded, not modelled.",
    '2.4.55': 'SETTLED — वा लिटि: आचख्यौ beside आचचक्षे. पूर्वेण नित्ये प्राप्ते\n  विकल्प उच्यते, the same shape as 2.4.44 over 2.4.43.',
    '2.4.56': 'SETTLED — अजेर्व्यघञपोः: प्रवायकः, प्रवयणीयः. अघञपोरिति किम्?\n  समाजः, उदाजः — and beside those समजः and उदजः, by 3.3.69.\n\nSETTLED — the substitute is given LONG and the vṛtti asks why:\n  दीर्घोच्चारणं किम्? प्रवीताः. So it is वी and not वि.\n\nSCOPE — a vārttika adds क्यप् to the exclusion, समज्या; another\n  makes it optional before a वलादि आर्धधातुक — प्रवेता beside\n  प्राजिता. Recorded.',
    '2.4.57': "SETTLED — वा यौ, and यु stands for ल्युट्: प्रवयणो दण्डः beside\n  प्राजनो दण्डः. The third विकल्प written over an obligatory\n  rule immediately before it.\n\nSETTLED — and this is where 2.4.35's heading stops. 2.4.58\n  begins the taddhita elisions, which are not yet read.",
}

for _sutra, _notes in _ADESA.items():
    register(
        _sutra,
        apply=substitute,
        codification=_SUBSTITUTION,
        notes=_notes,
        # 2.4.49's ङ् is marked so that 1.2.1 गाङ्कुटादिभ्यः can reach
        # the substitute, and 2.4.50 leans on the same rule. That is a
        # dependency in the grammar which this table states rather than
        # runs: the row records the substitute, and 1.2.1 acts on it
        # later, in the aṅga section. Declaring it would repeat the
        # mistake 2.2.30 records.
    )


# -------------------------------------------------------------------------
# 2.4.58 to 2.4.71 — affixes added and then taken away.
# -------------------------------------------------------------------------

_TADDHITA_LUK = (
    'taddhita_luk(affix=..., sense=..., stem=..., plural=...) -> whether '
    'the descendant-affix is elided, and by which rule.'
)
_SUP_LUK = (
    'sup_luk(becomes=...) -> whether the सुप् is elided, and by which '
    'rule.'
)

_LUK = {
    '2.4.58': 'SETTLED — ण्यक्षत्रियार्षञितो यूनि लुगणिञोः: the YUVAN affix goes,\n  so father and son are called alike. कौरव्यः पिता, कौरव्यः पुत्रः;\n  श्वाफल्कः पिता, श्वाफल्कः पुत्रः.\n\nSETTLED — four kinds of stem, and the vṛtti sources each: ण्य from\n  4.1.151 कुर्वादिभ्यो ण्यः, क्षत्रियगोत्र and आर्ष from 4.1.114\n  ऋष्यन्धकवृष्णिकुरुभ्यश्च and ऋष्यण्, and ञित्. What is elided is\n  the इञ् or अण् those stems then take in the yuvan sense.\n\nSETTLED — कौरव्य is read in तिकादि too, which would give फिञ् and\n  कौरव्यायणिः. The vṛtti separates the two: क्षत्रियगोत्रस्य तत्र\n  ग्रहणम् — the तिकादि entry is the KṢATRIYA gotra, by 4.1.172,\n  while this one is the brahmin gotra by 4.1.151. Same spelling,\n  two words.',
    '2.4.59': 'SETTLED — पैलादिभ्यश्च: पैलः पिता, पैलः पुत्रः. Read from the\n  gaṇapāṭha on disk, and the file marks it आकृतिगण, as the vṛtti\n  does — so membership is a lookup and never a count.\n\nSETTLED — several of its members end in इञ् and 2.4.60 would have\n  reached them already. अप्रागर्थः पाठः: they are listed here\n  because 2.4.60 holds only among the easterners, and this rule\n  holds everywhere.',
    '2.4.60': 'SETTLED — इञः प्राचाम्: पान्नागारिः पिता, पान्नागारिः पुत्रः.\n  प्राचामिति किम्? दाक्षिः पिता, दाक्षायणः पुत्रः.\n\nSETTLED — गोत्रविशेषणं प्राग्ग्रहणम्, न विकल्पार्थम्. प्राचाम्\n  qualifies the gotra; it does not make the rule optional. Read\n  the other way the elision would be a choice everywhere, which\n  is why the vṛtti says so outright.\n\nSETTLED — and it does NOT reach the Bharatas, though they are\n  easterners. 2.4.66 names भरत where it did not have to, and the\n  vṛtti reads that as a ज्ञापन: अन्यत्र प्राग्ग्रहणे भरतग्रहणं न\n  भवति. So आर्जुनिः पिता, आर्जुनायनः पुत्रः. Held by a test.',
    '2.4.61': 'SETTLED — न तौल्वलिभ्यः, a प्रतिषेध against 2.4.60: तौल्वलिः पिता,\n  तौल्वलायनः पुत्रः. Read from disk.\n\nSETTLED — refusing IS this rule acting, so it reports itself, as\n  2.4.14 and 2.4.15 do. It is checked BEFORE the rule it refuses,\n  since a prohibition reached after that rule has answered could\n  never fire.',
    '2.4.62': 'SETTLED — तद्राजस्य बहुषु तेनैवास्त्रियाम्: अङ्गाः, वङ्गाः, मगधाः.\n\nSETTLED — three conditions, and the vṛtti gives a counter for each,\n  so each is codified separately and each refusal says WHICH one\n  failed. तद्राजस्येति किम्? औपगवाः. बहुष्विति किम्? आङ्गः.\n  तेनैवग्रहणं किम्? प्रियवाङ्गाः — there the plural comes from the\n  बहुव्रीहि and not from the affix. अस्त्रियामिति किम्? आङ्ग्यः\n  स्त्रियः. All three carry down to 2.4.70.',
    '2.4.63': 'SETTLED — यस्कादिभ्यो गोत्रे: यस्काः, लभ्याः. गोत्र इति किम्?\n  यास्काश्छात्राः. Read from disk.\n\nSETTLED — the गोत्र meant here is the ordinary one and not the\n  technical descendant of 4.1.162: प्रत्ययविधेश्चान्यत्र लौकिकस्य\n  गोत्रस्य ग्रहणम्, इत्यनन्तरापत्येऽपि लुग् भवत्येव — so it reaches\n  an immediate child too. Where a term is used outside the rules\n  that define it, the everyday sense is taken.',
    '2.4.64': 'SETTLED — यञञोश्च: गर्गाः and वत्साः from यञ् by 4.1.105, बिदाः and\n  उर्वाः from अञ् by 4.1.104.\n\nSETTLED — गोत्र इत्येव is a live condition, not carried decoration:\n  द्वैप्याः by 4.3.10 and औत्साश्छात्राः by 4.1.86 keep their\n  affixes, being no gotra affix at all.',
    '2.4.65': "SETTLED — अत्रिभृगुकुत्सवसिष्ठगोतमाङ्गिरोभ्यश्च, six names given in\n  the sūtra itself: अत्रयः, भृगवः, कुत्साः, वसिष्ठाः, गोतमाः,\n  अङ्गिरसः. Read from the sūtra and not from a gaṇa, as 2.4.12's\n  ten are.\n\nSETTLED — the affixes differ across the six and the vṛtti sources\n  them: ढक् for अत्रि by 4.1.122 इतश्चानिञः, ऋष्यण् for the rest.\n  What the rule elides is whichever gotra affix each took.",
    '2.4.66': 'SETTLED — बह्वच इञः प्राच्यभरतेषु: पन्नागाराः, मन्थरैषणाः; and among\n  the Bharatas युधिष्ठिराः, अर्जुनाः. बह्वच इति किम्? बैकयः,\n  पौष्पयः. प्राच्यभरतेष्विति किम्? बालाकयः, हास्तिदासयः.\n\nSETTLED — भरत did not need saying, and that is the point. भरताः\n  प्राच्या एव, तेषां पुनर्ग्रहणं ज्ञापनार्थम् — अन्यत्र\n  प्राग्ग्रहणे भरतग्रहणं न भवति. Saying a word where it was already\n  covered TEACHES that it is not covered elsewhere, and what it\n  teaches lands on 2.4.60: आर्जुनिः पिता, आर्जुनायनः पुत्रः. The\n  same form of argument as ल्यप् at 2.4.36. Held by a test, since\n  it is a claim about a rule OTHER than the one that states it.',
    '2.4.67': 'SETTLED — न गोपवनादिभ्यः, a प्रतिषेध against 2.4.64: गौपवनाः,\n  शैग्रवाः. बिदाद्यन्तर्गणोऽयम्, a sub-gaṇa inside बिदादि.\n\nSCAR — THE GAṆA ON DISK IS DEFECTIVE AND IS NOT WHAT IS CODIFIED.\n  The file holds eleven entries, one of which is the bare string\n  "1" — a parse artifact, not a word — with several spelling\n  variants beside it. The vṛtti fixes the extent outright:\n  एतावन्त एवाष्टौ गोपवनादयः, exactly eight, and names them. It\n  then says what the surplus is and why it matters: परिशिष्टानां\n  हरितादीनां प्रमादपाठः, ते हि चतुर्थे बिदादिषु पठ्यन्ते, तेभ्यश्च\n  बहुषु लुग् भवत्येव. The extra words belong to बिदादि and the\n  elision DOES happen for them — हरिताः, किंदासाः. Reading the\n  file straight would have made this prohibition block exactly the\n  forms the commentary says it must allow. Held by a test that\n  checks the disk list still disagrees, so a corrected corpus goes\n  red rather than silently agreeing.',
    '2.4.68': "SETTLED — तिककितवादिभ्यो द्वन्द्वे: तैकायनयश्च कैतवायनयश्च gives\n  तिककितवाः; वाङ्खरयश्च भाण्डीरथयश्च gives वङ्खरभण्डीरथाः.\n\nSETTLED — the gaṇa on disk holds finished PLURAL compounds and not\n  their members, which is right: the rule is about a द्वन्द्व, so\n  what it names is the द्वन्द्व. The same shape as 2.4.11's\n  गवाश्वादि. तिकादि proper, from which फिञ् comes by 4.1.154, is a\n  different list and is filed under that sūtra.",
    '2.4.69': 'SETTLED — उपकादिभ्योऽन्यतरस्यामद्वन्द्वे: उपकाः beside औपकायनाः,\n  लमकाः beside लामकायनाः. Read from disk.\n\nSETTLED — अद्वन्द्वग्रहणं द्वन्द्वाधिकारनिवृत्त्यर्थम्. The word\n  अद्वन्द्वे is there to CANCEL the द्वन्द्व heading 2.4.68 set up.\n  Three of उपकादि — उपकलमकाः, भ्राष्टककपिष्ठलाः,\n  कृष्णाजिनकृष्णसुन्दराः — are also read in तिककितवादि, and in a\n  द्वन्द्व those go by 2.4.68 obligatorily: तेषां पूर्वेण नित्यमेव\n  लुग् भवति, अद्वन्द्वे त्वनेन विकल्पः. So the option and the\n  obligation divide by whether it is a द्वन्द्व.',
    '2.4.70': 'SETTLED — आगस्त्यकौण्डिन्ययोरगस्तिकुण्डिनच्: अगस्तयः, कुण्डिनाः.\n  The only rule of this run that REPLACES as well as elides, and\n  यथासंख्यम् — each stem to its own substitute.\n\nSETTLED — चकारः स्वरार्थः. The च of कुण्डिनच् is there for the\n  accent: कुण्डिनी is मध्योदात्त and its substitute would else have\n  been so too. An अनुबन्ध added to refuse an inherited property,\n  as at 2.4.54.\n\nSCOPE — 4.1.89 गोत्रेऽलुगचि blocks the elision before a vowel, and\n  the vṛtti works out what then happens: आगस्तीयाश्छात्राः by a छ,\n  and कौण्डिनाश्छात्राः by अण् from 4.2.111. Recorded; none of\n  those rules is codified.',
    '2.4.71': "SETTLED — सुपो धातुप्रातिपदिकयोः: पुत्रीयति and घटीयति for the\n  root, कष्टश्रितः and राजपुरुषः for the stem.\n  धातुप्रातिपदिकयोरिति किम्? वृक्षः, प्लक्षः — an ordinary\n  inflected word keeps its ending.\n\nSETTLED — तदन्तर्गतास्तद्ग्रहणेन गृह्यन्ते: a word with a सुप्\n  INSIDE it is taken by the same naming. This is what lets a\n  compound be built out of inflected words and still come out with\n  one ending at the end, so it underwrites the whole of 2.1 and\n  2.2 — which were codified first and took it for granted.\n\nSETTLED — it stands outside both runs of this pāda: not a yuvan\n  elision, not a plural gotra one, and outside 2.4.35's\n  आर्धधातुक heading, which stopped at 2.4.57. Its own function,\n  which is why it has its own entry point.",
}

for _sutra, _notes in _LUK.items():
    register(
        _sutra,
        apply=sup_luk if _sutra == "2.4.71" else taddhita_luk,
        codification=_SUP_LUK if _sutra == "2.4.71" else _TADDHITA_LUK,
        notes=_notes,
        # No reuse is declared. The affixes these rules elide are given
        # by adhyāya 4 — 4.1.104, 4.1.105, 4.1.114, 4.1.151 and the rest
        # — and none of those is codified; which affix a stem took is
        # passed in, as आर्धधातुक is at 2.4.35 and the kāraka is at
        # 2.3.1. `Elided` is shared with 2.4.72, but sharing a return
        # type is not one rule running another.
    )


# -------------------------------------------------------------------------
# 2.4.73 and 2.4.75 to 2.4.85 — the affixes taken away last,
# and the three endings that close the pāda.
# -------------------------------------------------------------------------

_VERBAL = (
    'verbal_luk(affix=..., root=..., gana=...) -> whether the affix '
    'goes, by which rule, and which elision it is.'
)
_AVYAYA = (
    'avyaya_ending(avyayibhava=..., vibhakti=...) -> whether the ending '
    'goes or is replaced, and by which rule.'
)
_LUT = (
    'lut_prathama(number=...) -> which of the three endings, and by '
    'which rule.'
)

_CLOSING = {
    '2.4.73': 'SETTLED — बहुलं छन्दसि, carrying शप् down from 2.4.72.\n  बहुलम् cuts both ways here and the vṛtti says so outright:\n  अदिप्रभृतिभ्य उक्तस्ततो न भवत्यपि, अन्येभ्यश्च भवति. It FAILS\n  where 2.4.72 gave it — वृत्रं हनति, अहिः शयते, both अदादि roots\n  keeping their शप् — and it HAPPENS where that rule did not:\n  त्राध्वं नो देवाः. Neither direction is an option; both are\n  attested, which is what बहुलम् records.',
    '2.4.75': 'SETTLED — जुहोत्यादिभ्यः श्लुः: जुहोति, बिभर्ति, नेनेक्ति.\n\nSETTLED — and it is श्लु rather than the लुक् already running:\n  लुकि प्रकृते श्लुविधानं द्विर्वचनार्थम्. A श्लु is what triggers\n  6.1.10 श्लौ, the reduplication; a लुक् would not have. The\n  reduplicated stems of the third gaṇa exist because of which\n  elision was named, and 1.1.61 tells the three apart precisely\n  so this choice can be made. Held by a test on the elision kind.\n\nSETTLED — शबनुवर्तते, न यङ्. What 2.4.74 यङोऽचि च took away is\n  not what is carried here: it is शप् that श्लु replaces.',
    '2.4.76': 'SETTLED — बहुलं छन्दसि, for the श्लु of 2.4.75, and again in both\n  directions: यत्रोक्तं तत्र न भवति, अन्यत्रापि भवति. दाति and\n  धाति are जुहोत्यादि roots without it; विवष्टि and विवक्ति have\n  it without being of that gaṇa.',
    '2.4.77': "SETTLED — गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु: अगात्, अस्थात्,\n  अदात्, अधात्, अपात्, अभूत्. लुगनुवर्तते, न श्लुः — it is the\n  लुक् that carries here and not 2.4.75's श्लु.\n  परस्मैपदेष्विति किम्? अगासातां ग्रामौ देवदत्तेन.\n\nSETTLED — two of the five are read narrowly, and the vārttika\n  गापोः … इण्पिबत्योर्ग्रहणम् says which: the गा that इण् BECAME\n  at 2.4.45, and the पा of पिबति. Not गायति and not पाति —\n  अगासीन् नटः, अपासीन् नृपः keep their सिच्. So a rule earlier in\n  this same pāda supplies the root this one acts on, and the two\n  have to be read together.\n\nSETTLED — घु is not a root but the class 1.1.20 दाधा ध्वदाप् names,\n  which is how अदात् and अधात् are covered without दा and धा being\n  listed. 1.1.20 is codified.",
    '2.4.78': 'SETTLED — विभाषा घ्राधेट्शाच्छासः: अघ्रात् beside अघ्रासीत्, अधात्\n  beside अधासीत्, अशात् beside अशासीत्.\n\nSETTLED — the rule does two different things at once, and the\n  vṛtti separates them: धेटः पूर्वेण नित्ये प्राप्ते विभाषार्थं\n  वचनम्, परिशिष्टानामप्राप्ते. धेट् is a घु, so 2.4.77 had already\n  made its elision obligatory and this makes it a CHOICE; the\n  other four had nothing reaching them, so for those it GRANTS\n  the elision. One विभाषा doing both jobs.',
    '2.4.79': 'SETTLED — तनादिभ्यस्तथासोः: अतत beside अतनिष्ट, अतथाः beside\n  अतनिष्ठाः; असात beside असनिष्ट, with the आ from 6.4.42\n  जनसनखनाम्.\n\nSETTLED — थासा साहचर्यादात्मनेपदस्य तशब्दस्य ग्रहणम्. There are\n  two त endings; the one meant is the MIDDLE त, known by the\n  company थास् keeps it in. The active अतनिष्ट यूयम् is untouched,\n  and codifying it as the bare ending would have caught both.',
    '2.4.80': 'SETTLED — मन्त्रे घसह्वरणशवृदहाद्वृच्कृगमिजनिभ्यो लेः: अमीमदन्त,\n  मा ह्वार्, प्रणक्, मा न आ धक्, अक्रन्, अग्मन्. मन्त्रे is a\n  condition and not a note — outside one the ले stands.\n\nSETTLED — two of the ten are read wide, and the vṛtti says how far:\n  वृ इति वृङ्वृञोः सामान्येन ग्रहणम्, both roots at once; and आद्\n  is आकारान्तग्रहणम्, the ā-final root, which it identifies as प्रा\n  in आप्रा द्यावापृथिवी. Recorded as the vṛtti reads them rather\n  than as ten bare names.',
    '2.4.81': 'SETTLED — आमः: ईहांचक्रे, ऊहांचक्रे, ईक्षांचक्रे. मन्त्रे does NOT\n  carry down from 2.4.80 — these are ordinary periphrastic\n  perfects, so the condition stops at the sūtra that states it.',
    '2.4.82': 'SETTLED — अव्ययादाप्सुपः: तत्र शालायाम् and यत्र शालायाम् for the\n  आप्, कृत्वा and हृत्वा for the सुप्.\n\nSETTLED — this is what makes an indeclinable LOOK uninflected. The\n  ending is added like any other and then taken away, which is\n  why an अव्यय can still be said to stand in a case at all. It\n  carries on 2.4.71, which does the same inside a compound.',
    '2.4.83': 'SETTLED — नाव्ययीभावादतोऽम्त्वपञ्चम्याः. Two things in one rule:\n  the elision 2.4.82 would have given is refused, and अम् is put\n  there instead. उपकुम्भं तिष्ठति, उपकुम्भं पश्य, उपमणिकं तिष्ठति.\n\nSETTLED — अत इति किम्? अधिस्त्रि, अधिकुमारि. An अव्ययीभाव not\n  ending in अ falls back to 2.4.82 and loses its ending outright,\n  so the two rules divide the अव्ययीभावs between them.\n\nSETTLED — अपञ्चम्या इति किम्? उपकुम्भादानय. And the vṛtti draws\n  the consequence rather than leaving it: एतस्मिन् प्रतिषिद्धे\n  पञ्चम्याः श्रवणमेव भवति — with the अम् kept off, the fifth\n  ending is actually heard.\n\nSETTLED — and this lands on the compound section. उपकुम्भम् is the\n  अव्ययीभाव 2.1.6 makes and 2.4.18 calls neuter; here it is told\n  which ending it takes. One pāda builds the compound, another\n  names its gender, this one gives it an ending.',
    '2.4.84': 'SETTLED — तृतीयासप्तम्योर्बहुलम्: उपकुम्भेन कृतम् beside उपकुम्भं\n  कृतम्, उपकुम्भे निधेहि beside उपकुम्भं निधेहि.\n  पूर्वेण नित्यमम्भावे प्राप्ते वचनमिदम् — 2.4.83 had made the अम्\n  obligatory and this makes it various, the same shape as 2.4.44\n  over 2.4.43 and 2.4.78 over 2.4.77.\n\nSCOPE — a vārttika holds the अम् obligatory after ऋद्धि, नदी,\n  समास and संख्यावयव: सुमद्रम्, उन्मत्तगङ्गम्, एकविंशतिभारद्वाजम्.\n  The vṛtti then withdraws it — बहुलवचनात् सिद्धम्, the बहुल\n  covers it already. Recorded with the withdrawal, since a\n  vārttika its own commentary sets aside is not a rule to codify.',
    '2.4.85': 'SETTLED — लुटः प्रथमस्य डारौरसः, यथाक्रमम्: कर्ता, कर्तारौ,\n  कर्तारः. And it reaches the middle as well as the active —\n  अध्येता, अध्येतारौ, अध्येतारः — so the three endings are given\n  once for both padas rather than twice.\n  प्रथमस्येति किम्? श्वः कर्तासि, श्वोऽध्येतासे.\n\nSETTLED — the last rule of the pāda, and of adhyāya 2. The Kāśikā\n  closes here: इति द्वितीयाध्यायस्य चतुर्थः पादः.',
}

#: 2.4.82 to 2.4.84 answer together, and 2.4.85 alone.
_AVYAYA_RULES = ("2.4.82", "2.4.83", "2.4.84")

for _sutra, _notes in _CLOSING.items():
    if _sutra == "2.4.85":
        _apply, _line = lut_prathama, _LUT
    elif _sutra in _AVYAYA_RULES:
        _apply, _line = avyaya_ending, _AVYAYA
    else:
        _apply, _line = verbal_luk, _VERBAL
    register(
        _sutra,
        apply=_apply,
        codification=_line,
        notes=_notes,
        # 2.4.75's श्लु is what 6.1.10 needs — a real dependency in
        # the grammar and not a call here: the reduplication happens in
        # adhyāya 6, and what this run returns is which elision it is,
        # so that the rule which cares can tell.
        #
        # 2.4.77's घु IS a call. It is not a root but the class 1.1.20
        # दाधा ध्वदाप् names, and that rule is codified — so it is
        # asked. दा and धा copied into the list would be a second
        # statement of it, and would lose the conditions 1.1.20 has of
        # its own.
        reuses=(("1.1.20",) if _sutra == "2.4.77" else ()),
    )


__all__ = [
    "adiprabhrtibhyah_sapah", "avyaya_ending", "ekavat",
    "gender", "lut_prathama", "substitute", "sup_luk",
    "taddhita_luk", "verbal_luk", "yan_luk",
]
