# -*- coding: utf-8 -*-
"""
अध्याय ६, पाद २ — where the accent of a compound really falls.

6.1.223 समासस्य said a compound is accented on its last syllable, and
6.1.158 then silenced every other syllable of it. This whole pāda is
the exceptions, and 6.2.1's vṛtti says so outright:
समासान्तोदात्तत्वापवादोऽयम् आरभ्यते.

Two scope-words divide it. पूर्वपदम् governs 6.2.1–110 and उत्तरपदम्
governs 6.2.111 to the end — आ पादपरिसमाप्तेः. Inside each, three
placement-words take turns: प्रकृत्या, which changes nothing; आदिः,
the first syllable; and अन्तः, the last.
"""

from __future__ import annotations

from src.astadhyayi.purvapada_svara import first_member
from src.astadhyayi.purvapada_udatta import placed_on
from src.astadhyayi.uttarapada_svara import second_member
from src.astadhyayi.sources import register

_FIRST_MEMBER = (
    'first_member(purvapada, gana=..., kind=..., uttarapada=..., '
    'uttarapada_affix=..., samasa=..., case=..., result=...) -> '
    'whether the first member of the compound keeps its own accent, '
    'and by which rule of 6.2.1–63.'
)

register(
    '6.2.1',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — बहुव्रीहौ प्रकृत्या पूर्वपदम् — in a बहुव्रीहि the first\n'
        '  member keeps the accent it had: **कार्ष्णोत्तरासङ्गाः, यूपवलजः,\n'
        '  ब्रह्मचारिपरिस्कन्दः, स्नातकपुत्रः, अध्यापकपुत्रः,\n'
        '  श्रोत्रियपुत्रः**.\n'
        '\n'
        'SETTLED — **AND THE WHOLE PĀDA OPENS AS AN EXCEPTION.**\n'
        '  **समासान्तोदात्तत्वे हि सति अनुदात्तं पदमेकवर्जम् इति सोऽनुदात्तः\n'
        '  स्यादिति समासान्तोदात्तत्वापवादोऽयम् आरभ्यते** — 6.1.223 put the\n'
        '  accent at the end and 6.1.158 silenced the rest, so without this\n'
        '  rule the first member would have none.\n'
        '\n'
        'SETTLED — **AND प्रकृत्या SAYS THE ACCENT IS NOT CHANGED, NOT WHERE\n'
        '  IT GOES.** **पूर्वपदग्रहणमत्र पूर्वपदस्थे स्वर उदात्ते स्वरिते वा\n'
        '  वर्तते... स्वभावेनावतिष्ठते, न विकारमनुदात्तत्वमापद्यते** — an\n'
        '  उदात्त or a स्वरित, wherever an earlier rule put it. The six forms\n'
        '  above carry it on the first syllable, the middle and the last\n'
        '  between them, and one rule answers all three'
    ),
)

register(
    '6.2.2',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — तत्पुरुषे तुल्यार्थतृतीयासप्तम्युपमानाव्ययद्वितीयाकृत्याः\n'
        '  — seven kinds of first member keep their accent in a तत्पुरुष, and\n'
        '  they are described rather than listed: a word meaning *like*, an\n'
        '  instrumental, a locative, what the second member is compared to,\n'
        '  an indeclinable, an accusative, and a कृत्य participle.\n'
        '  **तुल्यश्वेतः, सदृक्श्वेतः, सदृशश्वेतः; शङ्कुलाखण्डः, किरिकाणः**.\n'
        '\n'
        'SETTLED — **AND THE THREE FORMS OF THE FIRST EXAMPLE CARRY THREE\n'
        '  DIFFERENT ACCENTS.** तुल्य is first-accented by 6.1.213, सदृक्\n'
        '  end-accented by 6.1.197 and 6.2.139, and सदृश middle-accented. One\n'
        '  rule, three placements, and प्रकृत्या is what lets it be so'
    ),
)

register(
    '6.2.3',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — वर्णो वर्णेष्वनेते — a colour-word before another\n'
        '  colour-word, and not before एत: **कृष्णसारङ्गः, लोहितकल्माषः**.\n'
        '  Three conditions and the vṛtti gives a counter-example for each,\n'
        '  which is the shape almost every rule of this section takes'
    ),
)

register(
    '6.2.4',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — गाधलवणयोः प्रमाणे — before गाध or लवण where a MEASURE is\n'
        '  meant: **शम्बगाधमुदकम्** — water only as deep as an oar;\n'
        '  **गोलवणम्** — as much salt as is given to a cow.\n'
        '\n'
        'SETTLED — **AND प्रमाण IS READ WIDELY.**\n'
        '  **प्रमाणमियत्तापरिच्छेदमात्रमिह द्रष्टव्यम्, न पुनरायाम एव** — any\n'
        '  settling of how much, and not length alone'
    ),
)

register(
    '6.2.5',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — दायाद्यं दायादे — before दायाद, where the first member\n'
        '  names what is INHERITED: **विद्यादायादः, धनदायादः**.\n'
        '\n'
        'SETTLED — **AND THE COMPOUND HAD TO BE ARGUED INTO EXISTENCE.**\n'
        '  2.3.39 gives दायाद its own genitive, and **प्रतिपदविधाना च षष्ठी न\n'
        '  समस्यते** would then forbid the compound. The answer is that the\n'
        '  genitive here is the residual one of 2.3.50, which 2.3.39 was\n'
        '  stated beside rather than against: **शेषलक्षणैवात्र षष्ठी**'
    ),
)

register(
    '6.2.6',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — प्रतिबन्धि चिरकृच्छ्रयोः — before चिर or कृच्छ्र, where\n'
        '  the first member names what MEETS an obstacle: **गमनचिरम्,\n'
        '  गमनकृच्छ्रम्, व्याहरणचिरम्**. And the vṛtti glosses the condition\n'
        '  rather than assuming it: **गमनं हि कारणविकलतया चिरकालभावि\n'
        '  कृच्छ्रयोगि वा प्रतिबन्धि जायते**'
    ),
)

register(
    '6.2.7',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — पदेऽपदेशे — before पद in the sense of a PRETEXT, which the\n'
        '  vṛtti glosses **अपदेशो व्याजः**: **मूत्रपदेन प्रस्थितः, उच्चारपदेन\n'
        '  प्रस्थितः** — gone on the pretext of relieving himself'
    ),
)

register(
    '6.2.8',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — निवाते वातत्राणे — before निवात where a SHELTER FROM WIND\n'
        '  is meant: **कुटीनिवातम्, शमीनिवातम्, कुड्यनिवातम्** — a hut, an\n'
        '  acacia or a wall as the one thing between you and the wind.\n'
        '\n'
        'SETTLED — **AND THE WORD ITSELF IS ANALYSED TWO WAYS.**\n'
        "  **वातस्याभावो निवातम्** by 2.1.6's अव्ययीभाव, or **निरुद्धो\n"
        '  वातोऽस्मिन्निति बहुव्रीहिः** — and either way it is then\n'
        '  compounded again with what shelters'
    ),
)

register(
    '6.2.9',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — शारदेऽनार्तवे — before शारद where it does NOT mean *of the\n'
        '  autumn*: **रज्जुशारदमुदकम्** — water fresh drawn; **दृषत्शारदाः\n'
        '  सक्तवः** — flour fresh from the grindstone. **शारदशब्दोऽयं\n'
        '  प्रत्यग्रवाची**, and the compound has no analysis of its own:\n'
        '  **नित्यसमासोऽस्वपदविग्रह इष्यते**'
    ),
)

register(
    '6.2.10',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — अध्वर्युकषाययोर्जातौ — before these two where a KIND is\n'
        '  meant: **प्राच्याध्वर्युः, कठाध्वर्युः, कालापाध्वर्युः;\n'
        '  सर्पिर्मण्डकषायम्, उमापुष्पकषायम्**. **एते समानाधिकरणसमासा\n'
        '  जातिवाचिनो नियतविषयाः** — appositional compounds with a settled\n'
        '  field'
    ),
)

register(
    '6.2.11',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — सदृशप्रतिरूपयोः सादृश्ये — before these two where\n'
        '  RESEMBLANCE is meant: **पितृसदृशः, मातृसदृशः; पितृप्रतिरूपः**.\n'
        '\n'
        'SETTLED — **AND सदृश IS NAMED THOUGH 6.2.2 ALREADY REACHED IT.**\n'
        '  2.1.31 makes सदृश an instrumental तत्पुरुष, which 6.2.2 covers.\n'
        '  **षष्ठीसमासार्थं च सदृशग्रहणमिह** — it is named here for the\n'
        '  GENITIVE compound, and particularly where the ending is not\n'
        '  dropped: **दास्याःसदृशः, वृषल्याःसदृशः**'
    ),
)

register(
    '6.2.12',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — द्विगौ प्रमाणे — before a द्विगु where a measure is meant:\n'
        '  **प्राच्यसप्तशमः, गान्धारिसप्तशमः** — seven *śama* being its\n'
        '  measure, with the मात्रच् dropped by a vārttika on 5.2.37'
    ),
)

register(
    '6.2.13',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — गन्तव्यपण्यं वाणिजे — before वाणिज, where the first member\n'
        '  names either where the trader GOES or what he SELLS: **मद्रवाणिजः,\n'
        '  काश्मीरवाणिजः** — one who trades by going to Madra; **गोवाणिजः,\n'
        '  अश्ववाणिजः** — one who trades in cattle. Two quite different\n'
        '  relations in one rule, and the vṛtti separates them'
    ),
)

register(
    '6.2.14',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — मात्रोपज्ञोपक्रमच्छाये नपुंसके — before four words where\n'
        '  the compound is NEUTER: **भिक्षामात्रं न ददाति याचितः;\n'
        '  समुद्रमात्रं न सरोऽस्ति किंचन; पाणिनोपज्ञम् अकालकं व्याकरणम्;\n'
        '  व्याड्युपज्ञं दुष्करणम्; आपिशल्युपज्ञं गुरुलाघवम्**.\n'
        '\n'
        'SETTLED — **AND मात्र IS SAID TO MEAN *AS MUCH AS* ONLY INSIDE A\n'
        '  COMPOUND.** **मात्रशब्दोऽयं वृत्तिविषय एव तुल्यप्रमाणे वर्तते** —\n'
        '  outside one it does not, so the compound has no analysis:\n'
        '  **अस्वपदविग्रहः षष्ठीसमासः**'
    ),
)

register(
    '6.2.15',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — सुखप्रिययोर्हिते — before सुख or प्रिय where what is GOOD\n'
        '  FOR one is meant: **गमनसुखम्, वचनसुखम्; गमनप्रियम्**. And the\n'
        '  vṛtti defines हित by what it does: **तद्धि हितं यदायत्यां प्रीतिं\n'
        '  करोति** — what makes for pleasure in time to come'
    ),
)

register(
    '6.2.16',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — प्रीतौ च — and where PLEASURE itself is meant:\n'
        '  **ब्राह्मणसुखं पायसम्; छात्रप्रियोऽनध्यायः; कन्याप्रियो मृदङ्गः**.\n'
        '\n'
        'SETTLED — **AND THE SECOND SENSE-WORD LOOKS IDLE AND IS NOT.**\n'
        '  **सुखप्रिययोः प्रीत्यव्यभिचारादिह प्रीतिग्रहणं\n'
        '  तदतिशयप्रतिपत्त्यर्थम्** — pleasure never fails of these two\n'
        '  words, so the word is there for the DEGREE of it'
    ),
)

register(
    '6.2.17',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — स्वं स्वामिनि — before स्वामिन्, where the first member\n'
        '  names what is OWNED: **गोस्वामी, अश्वस्वामी, धनस्वामी**'
    ),
)

register(
    '6.2.18',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — पत्यावैश्वर्ये — before पति where LORDSHIP is meant:\n'
        '  **गृहपतिः, सेनापतिः, नरपतिः, धान्यपतिः**. Where the word means a\n'
        '  husband instead the compound falls back to 6.1.223'
    ),
)

register(
    '6.2.19',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — न भूवाक्चिद्दिधिषु — four first members are refused what\n'
        '  the rule before gives: **भूपतिः, वाक्पतिः, चित्पतिः, दिधिषूपतिः**,\n'
        '  and **समासस्वरेणान्तोदात्ता भवन्ति** — 6.1.223 takes them back'
    ),
)

register(
    '6.2.20',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — वा भुवनम् — and भुवन optionally: **भुवनपतिः** with the\n'
        '  first syllable accented, beside the end-accented form.\n'
        '\n'
        'SETTLED — **AND THE WORD IS VEDIC IN ITS DERIVATION AND NOT IN ITS\n'
        '  USE.** भुवन comes from a उणादि rule stated **छन्दसि**; **कथं\n'
        '  भुवनपतिरादित्य इति? उणादयो बहुलम् इति बहुलवचनाद् भाषायामपि\n'
        '  प्रयुज्यते**'
    ),
)

register(
    '6.2.21',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — आशङ्काबाधनेदीयस्सु संभावने — before three words where\n'
        '  SUPPOSING is meant, and the vṛtti defines it: **अस्तित्वाध्यवसायः\n'
        '  संभावनम्**, settling that a thing is so. **गमनाशङ्कं वर्तते** — it\n'
        '  is supposed that going is feared; **गमनाबाधम्; गमननेदीयः**'
    ),
)

register(
    '6.2.22',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — पूर्वे भूतपूर्वे — before पूर्व in the sense of *formerly\n'
        '  so*: **आढ्यो भूतपूर्व आढ्यपूर्वः; दर्शनीयपूर्वः, सुकुमारपूर्वः**.\n'
        '  And the counter-example turns on how the compound is read:\n'
        '  **परमश्चासौ पूर्वश्चेति समासः, न तु परमो भूतपूर्व इति**'
    ),
)

register(
    '6.2.23',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — सविधसनीडसमर्यादसवेशसदेशेषु सामीप्ये — before five words\n'
        '  where NEARNESS is meant: **मद्रसविधम्, गान्धारिसनीडम्,\n'
        '  काश्मीरसमर्यादम्**.\n'
        '\n'
        'SETTLED — **AND THE FIVE ARE NOT WHAT THEY LOOK LIKE.** **सविधादीनां\n'
        '  सह विधयेत्येवमादिका व्युत्पत्तिरेव केवलम्। समीपवाचिनस्त्वेते\n'
        '  समुदायाः** — the derivation *with a rule*, *with a nest* is made\n'
        '  out and set aside; as wholes the five simply mean *near*'
    ),
)

register(
    '6.2.24',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — विस्पष्टादीनि गुणवचनेषु — a list of first members before\n'
        '  any quality-word: **विस्पष्टकटुकम्, विचित्रकटुकम्, व्यक्तलवणम्**.\n'
        '\n'
        'SETTLED — **AND THE COMPOUND IS NOT A कर्मधारय.** **कटुकादिभिश्च\n'
        '  शब्दैर्गुणवद् द्रव्यमभिधीयत इत्यसामानाधिकरण्यम्** — कटुक names the\n'
        '  thing that has the quality while विस्पष्ट qualifies the quality\n'
        "  itself, so the two do not refer to the same thing and 2.1.4's\n"
        '  सुप्सुपा is what joins them'
    ),
)

register(
    '6.2.25',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — श्रज्यावमकन्पापवत्सु भावे कर्मधारये — before five, in a\n'
        '  कर्मधारय, where the first member names an ACTION: **गमनश्रेष्ठम्,\n'
        '  वचनज्येष्ठम्, गमनावमम्, गमनकनिष्ठम्, गमनपापिष्ठम्**.\n'
        '\n'
        'SETTLED — **AND NAMING THE SUBSTITUTES NAMES WHAT ENDS IN THEM.**\n'
        '  श्र, ज्य and कन् are the आदेश of श्रेष्ठ etc. **श्रज्यकनामादेशानां\n'
        '  ग्रहणमिति सामर्थ्यात् तद्वद् उत्तरपदं गृह्यते** — a substitute\n'
        '  named in a rule reaches the word it stands inside'
    ),
)

register(
    '6.2.26',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — कुमारश्च — कुमार as first member of a कर्मधारय:\n'
        '  **कुमारश्रमणा, कुमारकुलटा, कुमारतापसी**.\n'
        '\n'
        'SETTLED — **AND THE COMMENTATORS DIVIDE ON HOW FAR IT REACHES.**\n'
        '  **केचित् लक्षणप्रतिपदोक्तयोः प्रतिपदोक्तस्यैव ग्रहणम् इति परिभाषया\n'
        '  कुमारः श्रमणादिभिः इत्यत्रैव समासे स्वरमेतमिच्छन्ति। केचित्\n'
        '  पुनरविशेषेण सर्वत्रैव कर्मधारये** — some confine it to the\n'
        '  compound 2.1.70 makes by name, others let it reach every कर्मधारय'
    ),
)

register(
    '6.2.27',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — आदिः प्रत्येनसि — and before प्रत्येनस् it is the FIRST\n'
        '  SYLLABLE of कुमार that takes the accent, not whatever accent the\n'
        '  word had: **कुमारप्रत्येनाः**. The first rule of the pāda to place\n'
        '  an accent rather than preserve one, and it stands thirty-seven\n'
        '  sūtras before the heading that will make placing the ordinary\n'
        '  case.\n'
        '\n'
        'SETTLED — **AND THE WORD उदात्त IS NOT IN THE RULE AT ALL.**\n'
        '  **उदात्त इत्येतदत्र सामर्थ्याद् वेदितव्यम्। पूर्वपदप्रकृतिस्वर एव\n'
        '  ह्ययमादेरुपदिश्यते** — it has to be supplied from the sense, since\n'
        '  saying *the beginning* of an accent that is merely preserved says\n'
        '  nothing'
    ),
)

register(
    '6.2.28',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — पूगेष्वन्यतरस्याम् — and before a word for a GUILD,\n'
        '  optionally: **कुमारचातकाः, कुमारलोहध्वजाः, कुमारबलाहकाः,\n'
        '  कुमारजीमूताः**, each in three accentuations.\n'
        '\n'
        'SETTLED — **AND THE THIRD ACCENTUATION DEPENDS ON HOW 6.2.26 WAS\n'
        '  READ.** **अत्र यदाद्युदात्तत्वं न भवति, तदा कुमारश्च इति\n'
        '  पूर्वपदप्रकृतिस्वरत्वम् एके कुर्वन्ति। ये तु तत्र प्रतिपदोक्तस्य\n'
        '  ग्रहणमिच्छन्ति तेषां समासान्तोदात्तत्वमेव भवति** — the\n'
        '  disagreement recorded at 6.2.26 shows up here as a difference in\n'
        '  the forms'
    ),
)

register(
    '6.2.29',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — इगन्तकालकपालभगालशरावेषु द्विगौ — in a द्विगु, before a\n'
        '  second member ending in an इक्, or naming a time, or one of three\n'
        '  vessels: **पञ्चारत्निः, दशारत्निः; पञ्चमास्यः, पञ्चवर्षः;\n'
        '  पञ्चकपालः, पञ्चभगालः, पञ्चशरावः**'
    ),
)

register(
    '6.2.30',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — बह्वन्यतरस्याम् — and for बहु the rule before is a CHOICE:\n'
        '  **बह्वरत्निः, बहुमास्यः, बहुकपालः** each beside its end-accented\n'
        '  form. **पूर्वेण नित्ये प्राप्ते विकल्पः** — what was fixed is\n'
        '  loosened'
    ),
)

register(
    '6.2.31',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — दिष्टिवितस्त्योश्च — and before these two, optionally:\n'
        '  **पञ्चदिष्टिः, पञ्चवितस्तिः**. Both are measures, so the मात्रच्\n'
        '  drops here as it did at 6.2.29'
    ),
)

register(
    '6.2.32',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — सप्तमी सिद्धशुष्कपक्वबन्धेष्वकालात् — a locative first\n'
        '  member before four words, and not where it names a TIME:\n'
        '  **सांकाश्यसिद्धः, काम्पिल्यसिद्धः; ऊकशुष्कः, निधनशुष्कः;\n'
        '  कुम्भीपक्वः, कलसीपक्वः, भ्राष्ट्रपक्वः; चक्रबन्धः, चारकबन्धः**'
    ),
)

register(
    '6.2.33',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु — four preverbs as\n'
        '  first member, before a word naming what is LEFT OUT or a part of a\n'
        '  day or a night: **परित्रिगर्तं वृष्टो देवः; प्रतिपूर्वाह्णम्;\n'
        '  उपपूर्वरात्रम्; अपसौवीरम्**. The preverbs are first-accented\n'
        '  already by **उपसर्गाश्चाभिवर्जम्**.\n'
        '\n'
        'SETTLED — **AND THE RULE IS FOR THE अव्ययीभाव ALONE.** **तत्पुरुषे\n'
        '  बहुव्रीहौ च सिद्धत्वाद् अव्ययीभावार्थोऽयम् आरम्भः** — in the other\n'
        '  two compounds the accent came already, so this rule exists for the\n'
        '  one where it did not. And only two of the four take the *left out*\n'
        '  sense: **अपपरी वर्जने इति तयोरेव वर्ज्यमानम् उत्तरपदम्**'
    ),
)

register(
    '6.2.34',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — राजन्यबहुवचनद्वन्द्वेऽन्धकवृष्णिषु — in a द्वन्द्व of\n'
        '  plural words for princes of the Andhaka and Vṛṣṇi houses:\n'
        '  **श्वाफल्कचैत्रकाः, चैत्रकरोधकाः, शिनिवासुदेवाः**. And राजन्य is\n'
        '  in the rule for a reason: **राजन्यग्रहणमिह अभिषिक्तवंश्यानां\n'
        '  क्षत्रियाणां ग्रहणार्थम्** — of the anointed line, which the\n'
        '  counter-example is not'
    ),
)

register(
    '6.2.35',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — संख्या — a numeral as first member of a द्वन्द्व: **एकादश,\n'
        '  द्वादश, त्रयोदश**. एक is first-accented by a नित् उणादि affix, and\n'
        '  the त्रयस् that stands for त्रि is laid down end-accented'
    ),
)

register(
    '6.2.36',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — आचार्योपसर्जनश्चान्तेवासी — in a द्वन्द्व of words for\n'
        '  pupils named after their teachers: **आपिशलपाणिनीयाः,\n'
        '  पाणिनीयरौढीयाः, रौढीयकाशकृत्स्नाः**.\n'
        '\n'
        'SETTLED — **AND THE CONDITION IS ON THE WHOLE COMPOUND, NOT ON ONE\n'
        '  MEMBER.** **आचार्योपसर्जनग्रहणं द्वन्द्वविशेषणार्थम्, सकलो\n'
        '  द्वन्द्व आचार्योपसर्जनो यथा विज्ञायेत** — which is what keeps\n'
        '  पाणिनीयदेवदत्तौ out'
    ),
)

register(
    '6.2.37',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — कार्तकौजपादयश्च — a list of द्वन्द्व compounds whose first\n'
        '  member keeps its accent: **कार्तकौजपौ, सावर्णिमाण्डूकेयौ,\n'
        '  अवन्त्यश्मकाः, पैलश्यापर्णेयाः**. **विभक्त्यन्तानां पाठो\n'
        '  वचनविवक्षार्थम्** — the members are listed with their endings on\n'
        '  to show the number each is used in, and **बहुवचनमतन्त्रम्**, that\n'
        '  number is not binding'
    ),
)

register(
    '6.2.38',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — महान्\n'
        '  व्रीह्यपराह्णगृष्ट्येष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु —\n'
        '  महत् before ten words: **महाव्रीहिः, महापराह्णः, महेष्वासः,\n'
        '  महाभारतः, महाप्रवृद्धः**.\n'
        '\n'
        'SETTLED — **AND THE RULE REACHES ONLY THE COMPOUND 2.1.61 MAKES BY\n'
        '  NAME.** **महच्छब्दस्य प्रतिपदोक्तो यः समासः\n'
        '  सन्महत्परमोत्तमोत्कृष्टाः इति तत्रैव स्वरः** — so the genitive\n'
        '  compound महतो व्रीहिः stays end-accented'
    ),
)

register(
    '6.2.39',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — क्षुल्लकश्च वैश्वदेवे — क्षुल्लक, and महत् carrying down,\n'
        '  before वैश्वदेव: **क्षुल्लकवैश्वदेवम्, महावैश्वदेवम्**'
    ),
)

register(
    '6.2.40',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — उष्ट्रः सादिवाम्योः — उष्ट्र before these two:\n'
        '  **उष्ट्रसादि, उष्ट्रवामि**. The compound is read either as a\n'
        '  कर्मधारय or as a genitive one'
    ),
)

register(
    '6.2.41',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — गौः सादसादिसारथिषु — गो before three: **गोसादः, गोसादिः,\n'
        '  गोसारथिः**, and the first is read two ways — **गोः सादो** or **गां\n'
        '  सादयति**'
    ),
)

register(
    '6.2.42',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED —\n'
        '  कुरुगार्हपतरिक्तगुर्वसूतजरत्यश्लीलदृढरूपापारेवडवातैतिलकद्रूपण्यकम्बलो\n'
        '  दासीभाराणां च — eight named compounds and the दासीभार list:\n'
        '  **कुरुगार्हपतम्, रिक्तगुरुः, असूतजरती, अश्लीलदृढरूपा**. And a\n'
        '  supplement adds one more first member: **कुरुवृज्योर्गार्हपत इति\n'
        '  वक्तव्यम्** — **वृजिगार्हपतम्**.\n'
        '\n'
        'SETTLED — **AND ONE MEMBER CARRIES AN OPTION FROM ANOTHER PĀDA.**\n'
        "  रिक्तगुरु is **रिक्तगुरुः** or **रिक्तगुरुः** — 6.1.208's विभाषा\n"
        '  on रिक्त reaching into the compound'
    ),
)

register(
    '6.2.43',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — चतुर्थी तदर्थे — a dative first member before a word\n'
        '  naming what is made FOR it: **यूपदारु** — wood for a sacrificial\n'
        '  post; **कुण्डलहिरण्यम्, रथदारु, वल्लीहिरण्यम्**.\n'
        '\n'
        'SETTLED — **AND THE RELATION HAS TO BE ONE OF MATERIAL.**\n'
        '  **प्रकृतिविकारभावे स्वरोऽयमिष्यते** — the second member must be\n'
        '  what the first is MADE OF, not merely what it is meant for'
    ),
)

register(
    '6.2.44',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — अर्थे — and before the word अर्थ itself: **मात्रर्थम्,\n'
        '  पित्रर्थम्, देवतार्थम्, अतिथ्यर्थम्**. The rule before reached\n'
        '  only particular materials — दारु, हिरण्य — and not the general\n'
        '  word.\n'
        '\n'
        'SETTLED — **AND SOME READ IT AS A ज्ञापक INSTEAD.** **केचित्\n'
        '  पुनराहुः — ज्ञापकार्थमिदम्। एतदनेन ज्ञाप्यते — पूर्वो विधिः\n'
        '  प्रकृतिविकृत्योः समासे भवति** — that 6.2.43 holds only of a\n'
        '  material and its product, which is why **अश्वघासः** and\n'
        '  **श्वश्रूसुरम्** do not take it though the *for* relation is there'
    ),
)

register(
    '6.2.45',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — क्ते च — and before a क्त participle: **गोहितम्,\n'
        '  अश्वहितम्, मनुष्यहितम्; गोरक्षितम्, अश्वरक्षितम्, तापसरक्षितम्**,\n'
        '  with the dative of the person the thing is for'
    ),
)

register(
    '6.2.46',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — कर्मधारयेऽनिष्ठा — in a कर्मधारय before a क्त participle,\n'
        '  where the first member is NOT itself one: **श्रेणिकृताः, ऊककृताः,\n'
        '  पूगकृताः, निधनकृताः**'
    ),
)

register(
    '6.2.47',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — अहीने द्वितीया — an accusative first member before a क्त\n'
        '  participle, where nothing is FALLEN SHORT OF: **कष्टश्रितः,\n'
        '  त्रिशकलपतितः, ग्रामगतः**. And a supplement adds a condition:\n'
        '  **द्वितीयानुपसर्ग इति वक्तव्यम्**. **अन्तः थाथ०\n'
        '  इत्यस्यापवादोऽयम्** — an exception to 6.2.144'
    ),
)

register(
    '6.2.48',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — तृतीया कर्मणि — an instrumental first member before a क्त\n'
        '  participle used in the OBJECT sense: **अहिहतः, वज्रहतः, महाराजहतः,\n'
        '  नखनिर्भिन्ना, दात्रलूना**'
    ),
)

register(
    '6.2.49',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — गतिरनन्तरः — a गति standing IMMEDIATELY before a क्त\n'
        '  participle used in the object sense: **प्रकृतः, प्रहृतः**.\n'
        '  **थाथादिस्वरापवादो योगः**.\n'
        '\n'
        'SETTLED — **AND अनन्तरः IS WHAT KEEPS A MAXIM OUT.**\n'
        '  **अनन्तरग्रहणसामर्थ्यादेव कृद्ग्रहणे गतिकारकपूर्वस्यापि इत्येतद्\n'
        '  नाश्रीयते** — the word would be idle if that maxim applied, so its\n'
        '  being there is what shows it does not'
    ),
)

register(
    '6.2.50',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — तादौ च निति कृत्यतौ — and before a कृत् affix beginning\n'
        '  with त् and marked न्, तु excepted: **प्रकर्ता** with तृन्,\n'
        '  **प्रकर्तुम्, प्रकृतिः**. **कृत्स्वरबाधनार्थं वचनम्** — stated to\n'
        "  displace the affix's own accent"
    ),
)

register(
    '6.2.51',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — तवै चान्तश्च युगपत् — the तवै takes the accent at its END\n'
        '  and the गति keeps its own at the same time: **अन्वेतवै,\n'
        '  परिस्तरितवै, परिपातवै; तस्मात् पिता नाभिचरितवै**.\n'
        '\n'
        'SETTLED — **AND THIS IS THE SECOND RULE OF THE BOOK TO PUT TWO\n'
        '  ACCENTS AT ONCE.** 6.1.200 was the first, and both say युगपत् for\n'
        '  the same reason — 6.1.158 allows a word one accent, so without the\n'
        '  word the two would be alternatives. **कृत्स्वरापवादो योगः**'
    ),
)

register(
    '6.2.52',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — अनिगन्तोऽञ्चतौ वप्रत्यये — a गति not ending in an इक्,\n'
        '  before अञ्च् with the affix वि: **प्राङ्, प्राञ्चौ, प्राञ्चः;\n'
        '  पराङ्, पराञ्चः**. And the single substitute is उदात्त or स्वरित by\n'
        '  8.2.6.\n'
        '\n'
        'SETTLED — **AND ONE FORM IS SETTLED BY विप्रतिषेध.**\n'
        '  **चोरनिगन्तोऽञ्चतौ वप्रत्यय इत्येष स्वरो भवति विप्रतिषेधेन** —\n'
        '  **पराचः, पराचा**'
    ),
)

register(
    '6.2.53',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — न्यधी च — and these two, which DO end in an इक् and so\n'
        '  were kept out by the rule before: **न्यङ्, न्यञ्चौ; अध्यङ्,\n'
        '  अध्यञ्चः, अधीचः**. 8.2.4 then makes the अ of अञ्च् स्वरित'
    ),
)

register(
    '6.2.54',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — ईषदन्यतरस्याम् — ईषद् optionally keeps its accent:\n'
        '  **ईषत्कडारः, ईषत्पिङ्गलः**, each beside its end-accented form. And\n'
        '  the rule reaches no further than that: **ईषद्भेद इत्येवमादाै\n'
        '  कृत्स्वर एव भवति** — where the second member is a कृत् stem, that\n'
        "  affix's own accent stands and the option never arises"
    ),
)

register(
    '6.2.55',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — हिरण्यपरिमाणं धने — a first member naming a WEIGHT OF\n'
        '  GOLD, before धन, optionally: **द्विसुवर्णधनम्** beside the\n'
        '  end-accented form. And the option reaches the बहुव्रीहि too,\n'
        '  **परत्वाद्**'
    ),
)

register(
    '6.2.56',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — प्रथमोऽचिरोपसंपत्तौ — प्रथम optionally, where NEWNESS is\n'
        '  meant, which the vṛtti glosses **अचिरोपश्लेषोऽभिनवत्वम्**:\n'
        '  **प्रथमवैयाकरणः** — one who has just begun grammar, beside the\n'
        '  same form meaning the foremost grammarian, which never takes it'
    ),
)

register(
    '6.2.57',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — कतरकतमौ कर्मधारये — these two optionally in a कर्मधारय:\n'
        '  **कतरकठः, कतमकठः**, each beside the end-accented form.\n'
        '  **कर्मधारयग्रहणमुत्तरार्थम्** — the word is put in for the rules\n'
        '  that follow, since here the compound could only be one'
    ),
)

register(
    '6.2.58',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — आर्यो ब्राह्मणकुमारयोः — आर्य optionally before these two\n'
        '  in a कर्मधारय: **आर्यब्राह्मणः, आर्यकुमारः**'
    ),
)

register(
    '6.2.59',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — राजा च — and राजन् likewise: **राजब्राह्मणः, राजकुमारः**.\n'
        '  **पृथग्योगकरणमुत्तरार्थम्** — split off from the rule before so\n'
        '  that राजन् alone carries into the next'
    ),
)

register(
    '6.2.60',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — षष्ठी प्रत्येनसि — राजन् in the GENITIVE before\n'
        '  प्रत्येनस्, optionally: **राजप्रत्येनाः** beside the end-accented\n'
        '  form'
    ),
)

register(
    '6.2.61',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — क्ते नित्यार्थे — before a क्त participle where the\n'
        '  compound means ALWAYS, optionally: **नित्यप्रहसितः, सततप्रहसितः**,\n'
        '  each beside its end-accented form'
    ),
)

register(
    '6.2.62',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — ग्रामः शिल्पिनि — ग्राम before a word for a CRAFTSMAN,\n'
        "  optionally: **ग्रामनापितः, ग्रामकुलालः** — the village's barber,\n"
        "  the village's potter"
    ),
)

register(
    '6.2.63',
    apply=first_member,
    codification=_FIRST_MEMBER,
    notes=(
        'SETTLED — राजा च प्रशंसायाम् — and राजन् before a craftsman-word\n'
        '  where PRAISE is meant, optionally: **राजनापितः, राजकुलालः**.\n'
        '\n'
        'SETTLED — **AND THE PRAISE IS READ TWO WAYS ACCORDING TO THE\n'
        '  COMPOUND.** **कर्मधारये राजगुणाध्यारोपेण उत्तरपदार्थस्य प्रशंसा।\n'
        '  षष्ठीसमासे च राजयोग्यतया तस्य** — in the one the craftsman is\n'
        "  praised by having a king's qualities put on him, in the other by\n"
        '  being fit for a king'
    ),
)


_PLACED_ON = (
    'placed_on(purvapada, gana=..., uttarapada=..., '
    'uttarapada_gana=..., uttarapada_affix=..., samasa=..., '
    'case=..., result=..., samjna=...) -> where in the first member '
    'the accent is placed, and by which rule of 6.2.64–110.'
)

register(
    '6.2.64',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — आदिरुदात्तः — **आदिरुदात्त इत्येतदधिकृतम्। इत उत्तरं यद्\n'
        '  वक्ष्यामस्तत्र पूर्वपदस्यादिरुदात्तो भवतीत्येवं तद् वेदितव्यम्** —\n'
        "  from here the first member's FIRST SYLLABLE takes the accent,\n"
        '  whatever accent it had. **स्तूपेशाणः, मुकुटेकार्षापणम्,\n'
        '  याज्ञिकाश्वः, वैयाकरणहस्ती, दृषदिमाषकः**.\n'
        '\n'
        "SETTLED — **AND THE HEADING'S TWO WORDS STOP IN DIFFERENT PLACES.**\n"
        '  **आदिरिति प्राग् अन्ताधिकारात्। उदात्त इति प्रकृत्या भगालम् इति\n'
        '  यावत्** — आदिः to 6.2.91, where अन्तः takes over; उदात्तः all the\n'
        '  way to 6.2.137. The same shape 6.2.1 had, and the second time the\n'
        "  pāda splits one sūtra's reach in two"
    ),
)

register(
    '6.2.65',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — सप्तमीहारिणौ धर्म्येऽहरणे — a locative first member, or\n'
        '  one naming the TAKER, before a word for what is due by custom, and\n'
        '  not before हरण: **स्तूपेशाणः, मुकुटेकार्षापणम्, हलेद्विपदिका,\n'
        '  दृषदिमाषकः; याज्ञिकाश्वः, वैयाकरणहस्ती, मातुलाश्वः**.\n'
        '\n'
        'SETTLED — **AND BOTH SENSE-WORDS ARE GLOSSED BEFORE USE.** **हारीति\n'
        '  देयं यः स्वीकरोति सोऽभिधीयते** — the one who takes what is to be\n'
        '  given; **धर्म्यमित्याचारनियतं देयम् उच्यते** — what custom has\n'
        '  settled shall be given. And the custom itself is named:\n'
        '  **स्तूपादिषु शाणादि दातव्यम्, याज्ञिकादीनाम् अश्वादि**'
    ),
)

register(
    '6.2.66',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — युक्ते च — where the compound names one SET TO a task,\n'
        '  which the vṛtti glosses **युक्त इति समाहितः, कर्तव्ये तत्परो यः**:\n'
        '  **गोबल्लवः, अश्वबल्लवः, गोमणिन्दः, गोसंख्यः**'
    ),
)

register(
    '6.2.67',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — विभाषाध्यक्षे — before अध्यक्ष, optionally: **गवाध्यक्षः,\n'
        '  अश्वाध्यक्षः**, each beside its end-accented form'
    ),
)

register(
    '6.2.68',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — पापं च शिल्पिनि — पाप before a craftsman-word, optionally:\n'
        '  **पापनापितः, पापकुलालः**.\n'
        '\n'
        'SETTLED — **AND THE COMPOUND HAS TO BE THE ONE 2.1.54 MAKES BY\n'
        '  NAME.** **पापाणके कुत्सितैः इति पापशब्दस्य प्रतिपदोक्तः\n'
        '  समानाधिकरणसमास इति षष्ठीसमासे न भवति** — the appositional\n'
        '  compound, not the genitive one'
    ),
)

register(
    '6.2.69',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — गोत्रान्तेवासिमाणवब्राह्मणेषु क्षेपे — before a word for a\n'
        '  lineage or a pupil, and before माणव or ब्राह्मण, where ABUSE is\n'
        '  meant: **जङ्घावात्स्यः** — one who becomes a Vātsya by giving away\n'
        '  his shanks; **भार्यासौश्रुतः, कुमारीदाक्षाः, कम्बलचारायणीयाः,\n'
        '  ओदनपाणिनीयाः, भिक्षामाणवः**. Each names a man by what he took to\n'
        '  get where he is'
    ),
)

register(
    '6.2.70',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — अङ्गानि मैरेये — before मैरेय, where the first member\n'
        '  names an INGREDIENT of it: **गुडमैरेयः, मधुमैरेयः** — the liquor\n'
        '  made of molasses, the liquor made of honey'
    ),
)

register(
    '6.2.71',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — भक्ताख्यास्तदर्थेषु — a word for FOOD before a word for\n'
        '  what holds it: **भिक्षाकंसः, श्राणाकंसः, भाजीकंसः**. **भक्तमन्नम्,\n'
        '  तदाख्यास्तद्वाचिनः शब्दाः** — the vṛtti reads the compound of the\n'
        '  sūtra out before using it'
    ),
)

register(
    '6.2.72',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — गोबिडालसिंहसैन्धवेषूपमाने — before four words used as a\n'
        '  LIKENESS: **धान्यगवः** — grain heaped in the shape of a cow;\n'
        '  **भिक्षाबिडालः, तृणसिंहः, सक्तुसैन्धवः**. And the vṛtti leaves the\n'
        '  likeness to be worked out case by case: **उपमानार्थोऽपि यथासंभवं\n'
        '  यथाप्रसिद्धि च योजयितव्यः**'
    ),
)

register(
    '6.2.73',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — अके जीविकार्थे — before a stem in अक where the compound\n'
        '  names a LIVELIHOOD: **दन्तलेखकः, नखलेखकः, अवस्करशोधकः** — men who\n'
        '  live by scratching teeth, by trimming nails, by cleaning drains'
    ),
)

register(
    '6.2.74',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — प्राचां क्रीडायाम् — before the same stem where an EASTERN\n'
        '  game is named: **उद्दालकपुष्पभञ्जिका, वीरणपुष्पप्रचायिका,\n'
        '  शालभञ्जिका**. A rule whose condition is where in the country the\n'
        '  word is used'
    ),
)

register(
    '6.2.75',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — अणि नियुक्ते — before a stem in अण् where the compound\n'
        '  names one APPOINTED to a charge: **छत्रधारः, तूणीरधारः,\n'
        '  कमण्डलुग्राहः**.\n'
        '\n'
        'SETTLED — **AND नियुक्त IS NOT युक्त.** **नियुक्तोऽधिकृतः, स च\n'
        '  कस्मिंश्चित् कर्तव्ये तत्परो न भवतीति नियुक्ते इत्यनेन न सिध्यति**\n'
        '  — one put in charge is not thereby one set to a task, so 6.2.66\n'
        '  does not cover it'
    ),
)

register(
    '6.2.76',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — शिल्पिनि चाकृञः — before a stem in अण् naming a CRAFTSMAN,\n'
        '  so long as the affix is not on कृञ्: **तन्तुवायः, तुन्नवायः,\n'
        '  वालवायः**'
    ),
)

register(
    '6.2.77',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — संज्ञायां च — and where the compound is a NAME:\n'
        '  **तन्तुवायो नाम कीटः, वालवायो नाम पर्वतः**. The कृञ् exception\n'
        '  carries down'
    ),
)

register(
    '6.2.78',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — गोतन्तियवं पाले — three first members before पाल:\n'
        '  **गोपालः, तन्तिपालः, यवपालः**. **अनियुक्तार्थ आरम्भः** — the rule\n'
        '  exists for the cowherd who was not APPOINTED one, whom 6.2.75\n'
        '  could not reach'
    ),
)

register(
    '6.2.79',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — णिनि — before a stem in णिनि: **पुष्पहारी, फलहारी,\n'
        '  पर्णहारी**. The shortest sūtra of the section, and the widest'
    ),
)

register(
    '6.2.80',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — उपमानं शब्दार्थप्रकृतावेव — where the first member is a\n'
        '  LIKENESS, the rule before holds only if the root names a SOUND and\n'
        '  does so of itself: **उष्ट्रक्रोशी, ध्वाङ्क्षरावी, खरनादी**.\n'
        '\n'
        'SETTLED — **AND THE एवकार RESTRICTS THE LIKENESS AND NOT THE ROOT.**\n'
        '  **एवकारकरणम् उपमानावधारणार्थम्। शब्दार्थप्रकृतौ त्वनुपमानम् उपमानं\n'
        '  चाद्युदात्तं भवति** — where the root does name a sound, likeness\n'
        '  or not, the accent comes: **सिंहविनर्दी, पुष्कलजल्पी**'
    ),
)

register(
    '6.2.81',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — युक्तारोह्यादयश्च — a list of whole compounds:\n'
        '  **युक्तारोही, आगतरोही, आगतयोधी, आगतवञ्ची; क्षीरहोता, भगिनीभर्ता;\n'
        '  ग्रामगोधुक्, अश्वत्रिरात्रः, एकशितिपात्**.\n'
        '\n'
        'SETTLED — **AND WHAT THE LIST IS FOR IS DISPUTED.** **एते णिन्नन्ता\n'
        '  णिनि इत्यस्यैवोदाहरणार्थं पठ्यन्ते। पूर्वोत्तरपदनियमार्था इति\n'
        '  केचित्** — some take the णिनि-final members to be mere examples of\n'
        '  6.2.79 and the list to be confining which first and second members\n'
        '  that rule reaches'
    ),
)

register(
    '6.2.82',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — दीर्घकाशतुषभ्राष्ट्रवटं जे — before ज, for a first member\n'
        '  ending in a long vowel and for four named words: **कुटीजः, शमीजः;\n'
        '  काशजः, तुषजः, भ्राष्ट्रजः, वटजः**'
    ),
)

register(
    '6.2.83',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — अन्त्यात् पूर्वं बह्वचः — and where the first member has\n'
        '  MANY VOWELS, it is the syllable before the last that takes the\n'
        '  accent: **उपसरजः, मन्दुरजः, आमलकीजः, वडवाजः**. Neither the first\n'
        '  syllable nor the last — the only rule of the pāda so far to place\n'
        '  an accent anywhere else'
    ),
)

register(
    '6.2.84',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — ग्रामेऽनिवसन्तः — before ग्राम, where the first member\n'
        '  does NOT name who lives there: **मल्लग्रामः, वणिग्ग्रामः** — with\n'
        '  ग्राम meaning a body of men; **देवग्रामः** — the village a god\n'
        '  owns'
    ),
)

register(
    '6.2.85',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — घोषादिषु च — before a list of second members:\n'
        '  **दाक्षिघोषः, दाक्षिकटः, दाक्षिह्रदः, दाक्षिबदरी, दाक्ष्यश्वत्थः,\n'
        '  आश्रममुनिः**.\n'
        '\n'
        "SETTLED — **AND WHETHER THE RULE BEFORE'S CONDITION CARRIES IS\n"
        '  DISPUTED.** **यान्यत्र निवासनामधेयानि तेषु निवसद्वाचीन्यपि\n'
        '  पूर्वपदान्याद्युदात्तानि भवन्ति। अनिवसन्त इति नानुवर्तयन्ति\n'
        '  केचित्। अपरे पुनरनुवर्तयन्ति** — some let the words for dwellings\n'
        '  take the accent even where the first member names who lives there,\n'
        '  and some do not'
    ),
)

register(
    '6.2.86',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — छात्र्यादयः शालायाम् — a list of first members before\n'
        '  शाला: **छात्रिशाला, ऐलिशाला, भाण्डिशाला**.\n'
        '\n'
        'SETTLED — **AND IT WINS AGAINST A LATER RULE BY BEING STATED\n'
        '  EARLIER.** **यदा शालान्तस्तत्पुरुषो नपुंसकलिङ्गो भवति, तदापि\n'
        '  तत्पुरुषे शालायां नपुंसके इत्येतस्मात् पूर्वविप्रतिषेधेन\n'
        '  पूर्वपदमाद्युदात्तं भवति** — 6.2.123 would place the accent\n'
        '  otherwise, and the earlier rule takes it: **छात्रिशालम्**'
    ),
)

register(
    '6.2.87',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — प्रस्थेऽवृद्धमकर्क्यादीनाम् — before प्रस्थ, for a first\n'
        '  member that is not वृद्ध and not on the कर्क्यादि list:\n'
        '  **इन्द्रप्रस्थः, कुण्डप्रस्थः, ह्रदप्रस्थः, सुवर्णप्रस्थः**'
    ),
)

register(
    '6.2.88',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — मालादीनां च — and a list of first members before प्रस्थ:\n'
        '  **मालाप्रस्थः, शालाप्रस्थः**. **वृद्धार्थ आरम्भः** — the rule\n'
        '  exists for exactly the वृद्ध words the one before it excepted, and\n'
        "  two of the list are वृद्ध only by 1.1.75's एङ् प्राचां देशे"
    ),
)

register(
    '6.2.89',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — अमहन्नवं नगरेऽनुदीचाम् — before नगर, for a first member\n'
        '  that is neither महत् nor नव, and not a northern name:\n'
        '  **सुह्मनगरम्, पुण्ड्रनगरम्**. Three conditions and a\n'
        '  counter-example for each'
    ),
)

register(
    '6.2.90',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — अर्मे चावर्णं द्व्यच् त्र्यच् — before अर्म, for a first\n'
        '  member ending in अ or आ and having two or three vowels:\n'
        '  **दत्तार्मम्, गुप्तार्मम्, कुक्कुटार्मम्, वायसार्मम्**. And\n'
        '  **अमहन्नवमित्येव** — the two words the rule before excepted carry\n'
        '  down'
    ),
)

register(
    '6.2.91',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — न भूताधिकसंजीवमद्राश्मकज्जलम् — six first members are\n'
        '  refused what the rule before gives: **भूतार्मम्, अधिकार्मम्,\n'
        '  संजीवार्मम्, मद्रार्मम्, अश्मार्मम्, कज्जलार्मम्**, and\n'
        '  **समासान्तोदात्तत्वमेवात्र भवति** — 6.1.223 takes them back.\n'
        '\n'
        'SETTLED — **AND TWO OF THE SIX ARE NAMED FOR THE COMPOUND OF THEM.**\n'
        '  **मद्राश्मग्रहणं संघातविगृहीतार्थम्** — for **मद्राश्मार्मम्** as\n'
        '  well as for each apart. And a supplement adds a Vedic list to the\n'
        '  आदि section as a whole: **आद्युदात्तप्रकरणे दिवोदासादीनां\n'
        '  छन्दस्युपसंख्यानम्** — **दिवोदासं वध्र्यश्वाय दाशुषे**'
    ),
)

register(
    '6.2.92',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — अन्तः — **अन्त इत्यधिकृतम्। इत उत्तरं यद् वक्ष्यामस्तत्र\n'
        '  पूर्वपदस्यान्त उदात्तो भवति** — from here it is the LAST syllable\n'
        '  of the first member, where 6.2.64 gave the first. The placement\n'
        '  moves and the scope does not: पूर्वपद still governs.\n'
        '\n'
        'SETTLED — **AND THE RUN IS BOUNDED BY THE NEXT SCOPE-WORD.**\n'
        '  **प्राग् उत्तरपदादिः इत्येतस्माद् अयम् अधिकारो वेदितव्यः** — to\n'
        '  6.2.110, where 6.2.111 takes the second member and the rest of the\n'
        '  pāda'
    ),
)

register(
    '6.2.93',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — सर्वं गुणकार्त्स्न्ये — सर्व where a QUALITY is meant IN\n'
        '  FULL: **सर्वश्वेतः, सर्वकृष्णः, सर्वमहान्**. Three words of the\n'
        '  rule and three counter-examples, and the third turns on a\n'
        '  supplement that lets तर be dropped in the compound: **गुणात्तरेण\n'
        '  समासस्तरलोपश्च वक्तव्यः**'
    ),
)

register(
    '6.2.94',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — संज्ञायां गिरिनिकाययोः — before गिरि or निकाय where the\n'
        '  compound is a NAME: **अञ्जनागिरिः, भञ्जनागिरिः; शापिण्डिनिकायः,\n'
        '  मौण्डिनिकायः**'
    ),
)

register(
    '6.2.95',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — कुमार्यां वयसि — before कुमारी where an AGE is meant:\n'
        '  **वृद्धकुमारी, जरत्कुमारी**. And the vṛtti is careful about which\n'
        '  sense of कुमारी is in play: **कुमारीशब्दः पुंसा सहासंप्रयोगमात्रं\n'
        '  प्रवृत्तिनिमित्तम् उपादाय प्रयुक्तः** — the word used of a woman\n'
        '  unmarried, whatever her years'
    ),
)

register(
    '6.2.96',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — उदकेऽकेवले — before उदक where the water is MIXED, **अकेवलं\n'
        '  मिश्रम्**: **गुडोदकम्, तिलोदकम्**. And the single substitute is\n'
        '  then उदात्त or स्वरित by 8.2.6'
    ),
)

register(
    '6.2.97',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — द्विगौ क्रतौ — before a द्विगु naming a SACRIFICE:\n'
        '  **गर्गत्रिरात्रः, चरकत्रिरात्रः, कुसुरविन्दसप्तरात्रः**'
    ),
)

register(
    '6.2.98',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — सभायां नपुंसके — before सभा where the compound is NEUTER:\n'
        '  **गोपालसभम्, पशुपालसभम्, स्त्रीसभम्, दासीसभम्**. And the neuter\n'
        '  meant is the one 2.4.23 gives सभा by name: **सभायां प्रतिपदोक्तमिह\n'
        '  नपुंसकलिङ्गं गृह्यते**'
    ),
)

register(
    '6.2.99',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — पुरे प्राचाम् — before पुर in an EASTERN name:\n'
        '  **ललाटपुरम्, काञ्चीपुरम्, शिवदत्तपुरम्, कार्णिपुरम्, नार्मपुरम्**.\n'
        '  And the condition is on where the NAME belongs and not on where\n'
        '  the city stands, which is why शिवपुरम् is left with the compound\n'
        '  accent'
    ),
)

register(
    '6.2.100',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — अरिष्टगौडपूर्वे च — and where अरिष्ट or गौड stands FIRST:\n'
        '  **अरिष्टपुरम्, गौडपुरम्**. And पूर्वे is what lets a third word\n'
        '  come between: **पूर्वग्रहणं किम्? इहापि यथा स्यात् —\n'
        '  अरिष्टश्रितपुरम्, गौडभृत्यपुरम्**'
    ),
)

register(
    '6.2.101',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — न हास्तिनफलकमार्देयाः — three first members are refused\n'
        '  what 6.2.99 gives: **हास्तिनपुरम्, फलकपुरम्, मार्देयपुरम्**'
    ),
)

register(
    '6.2.102',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — कुसूलकूपकुम्भशालं बिले — four first members before बिल:\n'
        '  **कुसूलबिलम्, कूपबिलम्, कुम्भबिलम्, शालाबिलम्**'
    ),
)

register(
    '6.2.103',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — दिक्शब्दा ग्रामजनपदाख्यानचानराटेषु — a direction-word\n'
        '  before a village-name, a country-name, a title, or चानराट:\n'
        '  **पूर्वेषुकामशमी; पूर्वपञ्चालाः; पूर्वाधिरामम्, पूर्वयायातम्;\n'
        '  पूर्वचानराटम्**.\n'
        '\n'
        'SETTLED — **AND शब्द IS SAID TO REACH A DIRECTION-WORD USED OF\n'
        '  TIME.** **शब्दग्रहणं कालवाचिनोऽपि दिक्शब्दस्य परिग्रहार्थम्** —\n'
        '  पूर्व and अपर are directions by shape even where they mean earlier\n'
        '  and later'
    ),
)

register(
    '6.2.104',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — आचार्योपसर्जनश्चान्तेवासिनि — and before a word for pupils\n'
        '  named after their teacher: **पूर्वपाणिनीयाः, अपरपाणिनीयाः,\n'
        '  पूर्वकाशकृत्स्नाः**'
    ),
)

register(
    '6.2.105',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — उत्तरपदवृद्धौ सर्वं च — before a second member that has\n'
        '  taken the vṛddhi 7.3.10 heads, for सर्व and for a direction-word:\n'
        '  **सर्वपाञ्चालकः, पूर्वपाञ्चालकः, उत्तरपाञ्चालकः**'
    ),
)

register(
    '6.2.106',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — बहुव्रीहौ विश्वं संज्ञायाम् — विश्व in a बहुव्रीहि that is\n'
        '  a NAME: **विश्वदेवः, विश्वयशाः, विश्वमहान्**.\n'
        '  **पूर्वपदप्रकृतिस्वरत्वेनाद्युदात्तत्वं प्राप्तम्** — 6.2.1 would\n'
        '  have kept its own accent, and this displaces that.\n'
        '\n'
        'SETTLED — **AND बहुव्रीहि BECOMES A HEADING HERE.**\n'
        '  **बहुव्रीहावित्येतद् अधिक्रियते प्राग् अव्ययीभावसंज्ञानात्** —\n'
        '  from 6.2.106 to 6.2.120 every rule is read as being about a\n'
        "  बहुव्रीहि, bounded by 6.2.121's word अव्ययीभावे. A fourth heading\n"
        '  inside a pāda that already had three'
    ),
)

register(
    '6.2.107',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — उदराश्वेषुषु — before three words, in a बहुव्रीहि that is\n'
        '  a name: **वृकोदरः, दामोदरः; हर्यश्वः, यौवनाश्वः; सुवर्णपुङ्खेषुः,\n'
        '  महेषुः**'
    ),
)

register(
    '6.2.108',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — क्षेपे — and before the same three where ABUSE is meant,\n'
        '  name or no name: **कुण्डोदरः, घटोदरः; कटुकाश्वः, स्पन्दिताश्वः;\n'
        '  अनिघातेषुः, चलाचलेषुः**. And where a नञ् or a सु stands first,\n'
        '  6.2.172 wins **विप्रतिषेधेन**: **अनुदरः, सूदरः**'
    ),
)

register(
    '6.2.109',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — नदी बन्धुनि — a नदी-final first member before बन्धु, in a\n'
        '  बहुव्रीहि: **गार्गीबन्धुः, वात्सीबन्धुः**. Both conditions are\n'
        '  shown by what fails them: ब्रह्मबन्धुः has no नदी first member and\n'
        "  keeps ब्रह्मन्'s own first-syllable accent, and गार्गीप्रियः has\n"
        '  no बन्धु'
    ),
)

register(
    '6.2.110',
    apply=placed_on,
    codification=_PLACED_ON,
    notes=(
        'SETTLED — निष्ठोपसर्गपूर्वमन्यतरस्याम् — a निष्ठा first member with\n'
        '  a preverb before it, in a बहुव्रीहि, optionally: **प्रधौतमुखः,\n'
        '  प्रक्षालितपादः**, in three accentuations between them.\n'
        '\n'
        'SETTLED — **AND WHICH THE THIRD IS DEPENDS ON WHAT THE SECOND MEMBER\n'
        '  NAMES.** **यदि मुखशब्दः स्वाङ्गवाची तदा पक्षे मुखं स्वाङ्गम्\n'
        '  इत्येतद् भवति, न चेत् पूर्वपदप्रकृतिस्वरत्वेन गतिरनन्तरः इत्येतद्\n'
        '  भवति** — a part of the body takes 6.2.167, anything else takes\n'
        '  6.2.49'
    ),
)


_SECOND_MEMBER = (
    'second_member(uttarapada, gana=..., affix=..., purvapada=..., '
    'purvapada_gana=..., samasa=..., case=..., result=..., '
    'chandasi=...) -> what happens to the second member of the '
    'compound, and by which rule of 6.2.111-199.'
)

register(
    '6.2.111',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — उत्तरपदादिः — **उत्तरपदादिरित्येतदधिकृतम्। यदित\n'
        '  ऊर्ध्वमनुक्रमिष्याम उत्तरपदस्यादिरुदात्तो भवतीत्येवं तद्\n'
        '  वेदितव्यम्** — from here it is the SECOND member that is accented,\n'
        '  on its first syllable. The vṛtti reads the next sūtra out as its\n'
        '  example: **वक्ष्यति कर्णो वर्णलक्षणात् — शुक्लकर्णः, कृष्णकर्णः**.\n'
        '\n'
        "SETTLED — **AND THE HEADING'S TWO WORDS STOP IN DIFFERENT PLACES,\n"
        '  FOR THE THIRD TIME IN THIS PĀDA.** **उत्तरपदस्येत्येतदा\n'
        '  पादपरिसमाप्तेः। आदिरिति प्रकृत्या भगालम् इति यावत्** — उत्तरपदम्\n'
        '  to the last sūtra of the pāda, आदिः only to 6.2.136. 6.2.1 split\n'
        '  प्रकृत्या from पूर्वपदम् the same way, and 6.2.64 split आदिः from\n'
        '  उदात्तः'
    ),
)

register(
    '6.2.112',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कर्णो वर्णलक्षणात् — कर्ण as second member of a बहुव्रीहि\n'
        '  takes the accent on its first syllable when the first member names\n'
        '  a COLOUR or a MARK: **शुक्लकर्णः, कृष्णकर्णः; दात्राकर्णः,\n'
        '  शङ्कूकर्णः**.\n'
        '\n'
        'SETTLED — **AND लक्षण HERE IS A BRAND AND NOT A PROPERTY.** **पशूनां\n'
        '  विभागज्ञापनार्थं दात्रशङ्कुप्रतिरूपकं कर्णादिषु चिह्नं यत् क्रियते\n'
        '  तदिह लक्षणं गृह्यते** — the sickle-shaped or peg-shaped nick cut\n'
        "  in a beast's ear to show whose herd it belongs to. **तेन स्थूलकर्ण\n"
        '  इत्यत्र न भवति**'
    ),
)

register(
    '6.2.113',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — संज्ञायामौपम्ययोश्च — and कर्ण takes the same accent where\n'
        '  the बहुव्रीहि is a NAME or a COMPARISON: **कुञ्चिकर्णः, मणिकर्णः**\n'
        '  for names, **गोकर्णः, खरकर्णः** for comparisons — one whose ears\n'
        "  are like a cow's, like a donkey's"
    ),
)

register(
    '6.2.114',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कण्ठपृष्ठग्रीवाजङ्घं च — and four more body-words go the\n'
        '  same way in a बहुव्रीहि that is a name or a comparison:\n'
        '  **शितिकण्ठाः, नीलकण्ठः** beside **खरकण्ठः, उष्ट्रकण्ठः**;\n'
        '  **काण्डपृष्ठः, नाकपृष्ठः** beside **गोपृष्ठः, अजपृष्ठः**;\n'
        '  **सुग्रीवः, नीलग्रीवः, दशग्रीवः** beside **गोग्रीवः, अश्वग्रीवः**;\n'
        '  **नाडीजङ्घः, तालजङ्घः** beside **गोजङ्घः, अश्वजङ्घः, एणीजङ्घः**'
    ),
)

register(
    '6.2.115',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — शृङ्गमवस्थायां च — शृङ्ग adds a third sense to the two\n'
        '  before it, a STAGE OF LIFE: **उद्गतशृङ्गः, द्व्यङ्गुलशृङ्गः,\n'
        '  त्र्यङ्गुलशृङ्गः**, and the vṛtti says what the stage is —\n'
        '  **शृङ्गोद्गमनादिकृतो गवादेर् वयोविशेषोऽवस्था**, the age of an ox\n'
        '  told by how far its horns have come up. With the name and the\n'
        '  comparison too: **ऋष्यशृङ्गः; गोशृङ्गः, मेषशृङ्गः**'
    ),
)

register(
    '6.2.116',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — नञो जरमरमित्रमृताः — after नञ्, these four second members\n'
        '  are accented on their first syllable in a बहुव्रीहि: **अजरः, अमरः,\n'
        '  अमित्रः, अमृतः**.\n'
        '\n'
        'SETTLED — **AND WHAT IT IS AN EXCEPTION TO COMES LATER THAN IT.**\n'
        '  **जरादय इति किम्? अशत्रुः। नञ्सुभ्याम् इति\n'
        '  उत्तरपदान्तोदात्तत्वमेवात्र भवति** — outside the four, 6.2.172\n'
        '  accents the LAST syllable instead. A rule carving four words out\n'
        '  of a rule fifty-six sūtras further on'
    ),
)

register(
    '6.2.117',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — सोर्मनसी अलोमोषसी — after सु, a second member ending in\n'
        '  मन् or in अस् is accented on its first syllable, except लोमन् and\n'
        '  उषस्: **सुकर्मा, सुधर्मा, सुप्रथिमा; सुपयाः, सुयशाः, सुस्रोताः**.\n'
        '\n'
        'SETTLED — **AND THE TWO ENDINGS ARE TAKEN WHETHER THEY MEAN ANYTHING\n'
        '  OR NOT.** **अनिनस्मन्ग्रहणान्यर्थवता चानर्थकेन च इत्यनर्थकयोरपि\n'
        '  मनसोरिह ग्रहणम्** — मन् and अस् count even where they are not\n'
        '  affixes carrying a sense but merely the shape the word ends in.\n'
        '\n'
        'SETTLED — **AND IT LOSES TO 6.2.173 BY BEING EARLIER.** It is an\n'
        '  अपवाद of 6.2.172 — **नञ्सुभ्याम् इत्यस्यायमपवादः** — but **कपि तु\n'
        '  परत्वात् कपि पूर्वम् इत्येतद् भवति**: add कप् and the later rule\n'
        '  takes over'
    ),
)

register(
    '6.2.118',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — क्रत्वादयश्च — and the क्रत्वादि words after सु:\n'
        '  **सुक्रतुः, सुदृशीकः**. The gaṇa is six long — **क्रतु। दृशीक।\n'
        '  प्रतीक। प्रतूर्ति। हव्य। भग। क्रत्वादिः**'
    ),
)

register(
    '6.2.119',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — आद्युदात्तं द्व्यच्छन्दसि — in the Veda, a second member\n'
        '  after सु that has TWO vowels and was ALREADY accented on its first\n'
        '  syllable stays so: **स्वश्वास्त्वा सुरथा मर्जयेम**.\n'
        '\n'
        'SETTLED — **SO THE RULE CHANGES NOTHING AND STILL DOES SOMETHING.**\n'
        '  **नित्स्वरेणाश्वरथशब्दावाद्युदात्तौ** — अश्व and रथ are already\n'
        '  ādi-accented by 6.1.197. What 6.2.119 does is stop 6.2.172 from\n'
        '  moving that accent to the end: **नञ्सुभ्याम् इत्यस्यायमपवादः**'
    ),
)

register(
    '6.2.120',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — वीरवीर्यौ च — and these two after सु, in the Veda:\n'
        '  **सुवीरस्ते; सुवीर्यस्य पतयः स्याम**.\n'
        '\n'
        'SETTLED — **AND NAMING वीर्य TEACHES SOMETHING ABOUT ANOTHER RULE.**\n'
        '  **वीर्यमिति यत्प्रत्ययान्तं तत्र यतोऽनावः इत्याद्युदात्तत्वं न\n'
        '  भवतीत्येतदेव वीर्यग्रहणं ज्ञापकम्। तत्र हि सति पूर्वेणैव सिद्धं\n'
        '  स्यात्** — if 6.1.213 यतोऽनावः reached वीर्य, 6.2.119 would\n'
        '  already have covered it and this sūtra would name it for nothing.\n'
        '  Naming it says 6.1.213 does not'
    ),
)

register(
    '6.2.121',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कूलतीरतूलमूलशालाक्षसमम् अव्ययीभावे — seven second members\n'
        '  are accented on their first syllable in an अव्ययीभाव: **परिकूलम्,\n'
        '  उपकूलम्, परितीरम्, उपतीरम्, परितूलम्, उपतूलम्, परिमूलम्, उपमूलम्,\n'
        '  परिशालम्, उपशालम्, पर्यक्षम्, उपाक्षम्, सुषमम्, विषमम्, निषमम्,\n'
        '  दुःषमम्**. They come in with the compound itself:\n'
        '  **तिष्ठद्गुप्रभृतिषु एते पठ्यन्ते**.\n'
        '\n'
        'SETTLED — **AND IT WINS AGAINST AN EARLIER RULE OF THIS PĀDA BY\n'
        '  BEING LATER.** **पर्यादिभ्यः कूलादीनामाद्युदात्तत्वं विप्रतिषेधेन\n'
        "  भवति** — where 6.2.33 would keep the first member's accent\n"
        '  instead, 6.2.121 takes it'
    ),
)

register(
    '6.2.122',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कंसमन्थशूर्पपाय्यकाण्डं द्विगौ — five second members are\n'
        '  accented on their first syllable in a द्विगु: **द्विकंसः,\n'
        '  त्रिकंसः, द्विमन्थः, त्रिमन्थः, द्विशूर्पः, त्रिशूर्पः,\n'
        '  द्विपाय्यः, त्रिपाय्यः, द्विकाण्डः, त्रिकाण्डः** — worth two\n'
        '  कंसas, worth three, and so on'
    ),
)

register(
    '6.2.123',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — तत्पुरुषे शालायां नपुंसके — शाला at the end of a NEUTER\n'
        '  तत्पुरुष is accented on its first syllable: **ब्राह्मणशालम्,\n'
        '  क्षत्रियशालम्**. The neuter is not chosen here but supplied by\n'
        '  another rule — **विभाषा सेनासुराच्छायाशालानिशानाम् इति\n'
        '  नपुंसकलिङ्गता**'
    ),
)

register(
    '6.2.124',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कन्था च — and कन्था likewise, in a neuter तत्पुरुष:\n'
        '  **सौशमिकन्थम्, आह्वकन्थम्, चप्पकन्थम्**. The neuter again comes\n'
        '  from elsewhere — **संज्ञायां कन्थोशीनरेषु इति नपुंसकलिङ्गता** —\n'
        '  and the vṛtti records what kind of compound these are:\n'
        '  **षष्ठीसमासा एते**'
    ),
)

register(
    '6.2.125',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — आदिश्चिहणादीनाम् — before कन्था, the चिहणादि words are\n'
        "  accented on THEIR first syllable, not on the second member's:\n"
        '  **चिहणकन्थम्, मडरकन्थम्, मडुरकन्थम्**.\n'
        '\n'
        'SETTLED — **AND THE REPEATED WORD आदिः IS WHAT TURNS THE RULE\n'
        '  ROUND.** **आदिरिति वर्तमाने पुनरादिग्रहणं\n'
        '  पूर्वपदाद्युदात्तार्थम्** — आदिः was already running from 6.2.111;\n'
        '  saying it again can only be to move it off the second member and\n'
        '  onto the first. The one rule in this whole run that accents the\n'
        '  पूर्वपद'
    ),
)

register(
    '6.2.126',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — चेलखेटकटुककाण्डं गर्हायाम् — four second members are\n'
        '  accented on their first syllable in a तत्पुरुष where CONTEMPT is\n'
        '  meant: **पुत्रचेलम्, भार्याचेलम्, उपानत्खेटम्, नगरखेटम्,\n'
        '  दधिकटुकम्, उदश्वित्कटुकम्, भूतकाण्डम्, प्रजाकाण्डम्**.\n'
        '\n'
        'SETTLED — **AND THE CONTEMPT IS CARRIED BY A COMPARISON.**\n'
        '  **चेलादीनां सादृश्येन पुत्रादीनां गर्हा। तत्र पुत्रश् चेलम् इवेति\n'
        '  विगृह्य व्याघ्रादेराकृतिगणत्वाद् उपमितं व्याघ्रादिभिः इति समासः**\n'
        '  — a son who is a mere rag, compounded by 2.1.56, whose व्याघ्रादि\n'
        '  is open-ended enough to admit चेल'
    ),
)

register(
    '6.2.127',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — चीरमुपमानम् — चीर is accented on its first syllable where\n'
        '  it is what something is COMPARED TO: **वस्त्रं चीरम् इव\n'
        '  वस्त्रचीरम्, पटचीरम्, कम्बलचीरम्** — cloth no better than a rag'
    ),
)

register(
    '6.2.128',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — पललसूपशाकं मिश्रे — three second members naming food are\n'
        '  accented on their first syllable where a MIXTURE is meant:\n'
        '  **गुडपललम्, घृतपललम्, घृतसूपः, मूलकसूपः, घृतशाकम्, मुद्गशाकम्**.\n'
        "  The compound is 2.1.35's — **गुडेन मिश्रं पललं गुडपललम्, भक्ष्येण\n"
        '  मिश्रीकरणम् इति समासः**'
    ),
)

register(
    '6.2.129',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कूलसूदस्थलकर्षाः संज्ञायाम् — four second members are\n'
        '  accented on their first syllable where the compound is a NAME:\n'
        '  **दाक्षिकूलम्, माहकिकूलम्, देवसूदम्, भाजीसूदम्, दाण्डायनस्थली,\n'
        '  माहकिस्थली, दाक्षिकर्षः** — and the vṛtti says of what:\n'
        '  **ग्रामनामधेयान्येतानि**, these are the names of villages.\n'
        '\n'
        'SETTLED — **AND स्थल COVERS स्थली TOO.** **स्थलग्रहणे\n'
        '  लिङ्गविशिष्टत्वात् स्थलीशब्दोऽपि गृह्यते** — naming a stem names\n'
        '  its feminine, here made by ङीष् under 4.1.42'
    ),
)

register(
    '6.2.130',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अकर्मधारये राज्यम् — राज्य is accented on its first\n'
        '  syllable in a तत्पुरुष that is NOT a कर्मधारय: **ब्राह्मणराज्यम्,\n'
        '  क्षत्रियराज्यम्**.\n'
        '\n'
        'SETTLED — **AND THE अव्यय ACCENT BEATS IT BY BEING EARLIER.**\n'
        '  **चेलराज्यादिस्वराद् अव्ययस्वरो भवति पूर्वविप्रतिषेधेन — कुचेलम्,\n'
        '  कुराज्यम्** — where the first member is an indeclinable, 6.2.2\n'
        '  wins over both 6.2.126 and this rule, and it wins by being the\n'
        '  EARLIER of the two'
    ),
)

register(
    '6.2.131',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — वर्ग्यादयश्च — and the वर्ग्यादि words in a non-कर्मधारय\n'
        '  तत्पुरुष: **वासुदेववर्ग्यः, वासुदेवपक्ष्यः, अर्जुनवर्ग्यः,\n'
        "  अर्जुनपक्ष्यः** — of Vāsudeva's party, of Arjuna's side.\n"
        '\n'
        'SETTLED — **AND THE GAṆA IS NOT WHERE ONE WOULD LOOK FOR IT.**\n'
        '  **वर्ग्यादयः प्रातिपदिकेषु न पठ्यन्ते। दिगादिषु तु वर्ग पूग गण\n'
        '  पक्ष इत्येवमादयो ये पठिताः, त एव यत्प्रत्ययान्ता वर्ग्यादय इह\n'
        "  प्रतिपत्तव्याः** — take दिगादि's members and put यत् on them, and\n"
        '  that is this list'
    ),
)

register(
    '6.2.132',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — पुत्रः पुम्भ्यः — पुत्र after a word for a MAN is accented\n'
        '  on its first syllable in a तत्पुरुष: **कौनटिपुत्रः, दामकपुत्रः,\n'
        '  माहिषकपुत्रः** — the son of Kaunaṭi, of Dāmaka. Named after the\n'
        '  father the accent moves forward; named after the mother it does\n'
        '  not'
    ),
)

register(
    '6.2.133',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — न आचार्यराजर्त्विक्संयुक्तज्ञात्याख्येभ्यः — but not after\n'
        "  a word naming a teacher, a king, a priest, a wife's kinsman or a\n"
        '  blood relation: **आचार्यपुत्रः, उपाध्यायपुत्रः, शाकटायनपुत्रः,\n'
        '  राजपुत्रः, ईश्वरपुत्रः, ऋत्विक्पुत्रः, याजकपुत्रः, संयुक्तपुत्रः,\n'
        '  श्यालपुत्रः, ज्ञातिपुत्रः**. The accent 6.2.132 would have moved\n'
        '  stays where 6.1.223 put it, at the end.\n'
        '\n'
        'SETTLED — **AND THE WORD आख्या OPENS THE FIVE OUT.** **आख्याग्रहणात्\n'
        '  स्वरूपस्य पर्यायाणां विशेषाणां च ग्रहणं भवति** — the word itself,\n'
        '  its synonyms, AND its species. So not आचार्य alone but उपाध्याय\n'
        '  and शाकटायन too; not राजन् alone but ईश्वर and नन्द. Each of the\n'
        '  five is glossed before use: **आचार्य उपाध्यायः। राजा ईश्वरः।\n'
        '  ऋत्विजो याजकाः। संयुक्ताः स्त्रीसंबन्धिनः श्यालादयः। ज्ञातयो\n'
        '  मातृपितृसंबन्धिनो बान्धवाः**'
    ),
)

register(
    '6.2.134',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — चूर्णादीन्यप्राणिषष्ठ्याः — the चूर्णादि second members\n'
        '  are accented on their first syllable after a genitive naming\n'
        '  something NOT ALIVE: **मुद्गचूर्णम्, मसूरचूर्णम्** — flour of\n'
        '  beans, flour of lentils. The vṛtti carries both headings down:\n'
        '  **उत्तरपदादिरिति वर्तते, तत्पुरुष इति च**.\n'
        '\n'
        'SETTLED — **AND THE SŪTRA HAS A SECOND READING.**\n'
        '  **चूर्णादीन्यप्राण्युपग्रहाद् इति सूत्रस्य पाठान्तरम्। तत्रोपग्रह\n'
        '  इति षष्ठ्यन्तमेव पूर्वाचार्योपचारेण गृह्यते** — where it reads\n'
        "  उपग्रह, उपग्रह is the older teachers' word for the genitive, and\n"
        '  nothing changes'
    ),
)

register(
    '6.2.135',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — षट् च काण्डादीनि — and six words already accented earlier\n'
        '  in this pāda are accented here too, now WITHOUT the\n'
        '  sense-conditions those rules attached. The vṛtti walks them one by\n'
        '  one: **काण्डं गर्हायाम् इत्युक्तम् अगर्हायामपि भवति — दर्भकाण्डम्,\n'
        '  शरकाण्डम्; चीरम् उपमानम् इत्युक्तम् अनुपमानमपि भवति — दर्भचीरम्,\n'
        '  कुशचीरम्; पललसूपशाकं मिश्रे इत्युक्तम् अमिश्रेऽपि भवति — तिलपललम्,\n'
        '  मुद्गसूपः, मूलकशाकम्; कूलं संज्ञायाम् इत्युक्तम् असंज्ञायामपि भवति\n'
        '  — नदीकूलम्, समुद्रकूलम्**. Four rules widened by one, at the price\n'
        '  of a new condition: a non-living genitive in front'
    ),
)

register(
    '6.2.136',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कुण्डं वनम् — कुण्ड is accented on its first syllable\n'
        '  where it names a THICKET: **दर्भकुण्डम्, शरकुण्डम्**. The vṛtti\n'
        '  says how a pot came to mean a wood: **कुण्डशब्दोऽत्र\n'
        '  कुण्डसादृश्येन वने वर्तते** — by the likeness of the shape. This\n'
        '  is the last rule under आदिः; 6.2.137 replaces the word'
    ),
)

register(
    '6.2.137',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — प्रकृत्या भगालम् — a second member meaning SKULL keeps its\n'
        '  own accent in a तत्पुरुष: **कुम्भीभगालम्, कुम्भीकपालम्,\n'
        '  कुम्भीनदालम्**, and the vṛtti says what that accent is —\n'
        '  **भगालादयो मध्योदात्ताः**, accented in the middle, which is\n'
        '  exactly what neither आदिः nor अन्तः could have given.\n'
        '\n'
        'SETTLED — **AND THE WORD प्रकृत्या STAYS ON AFTER THE RULE ENDS.**\n'
        '  **प्रकृत्येत्येतदधिकृतम् अन्तः इति यावद् वेदितव्यम्** — through\n'
        '  6.2.142, six sūtras, until 6.2.143 अन्तः displaces it. The\n'
        "  shortest of the pāda's five headings, and the third placement-word\n"
        '  to hold the second member'
    ),
)

register(
    '6.2.138',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — शितेर्नित्याबह्वज्बहुव्रीहावभसत् — after शिति, a second\n'
        '  member that ALWAYS has few vowels keeps its own accent in a\n'
        '  बहुव्रीहि, भसत् excepted: **शितिपादः, शित्यंसः, शित्योष्ठः** — and\n'
        '  the vṛtti says which accents are thereby kept: **पादशब्दो\n'
        '  वृषादित्वादाद्युदात्तः। अंसौष्ठशब्दौ च प्रत्ययस्य नित्त्वात्**.\n'
        '\n'
        'SETTLED — **AND THE WORD नित्यम् IS THERE FOR ONE WORD.**\n'
        '  **नित्यग्रहणं किम्? शितिककुत्** — ककुद् loses its द् by 5.4.146,\n'
        '  so ककुत् is short-voweled SOMETIMES and not always. नित्यम् shuts\n'
        '  out exactly that: a word that has to lose something first does not\n'
        '  count'
    ),
)

register(
    '6.2.139',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — गतिकारकोपपदात् कृत् — a कृत्-formed second member keeps\n'
        '  its own accent after a गति, a कारक or an उपपद: **प्रकारकः,\n'
        '  प्रकरणम्, प्रहारकः, प्रहरणम्; इध्मप्रव्रश्चनः, पलाशशातनः,\n'
        '  श्मश्रुकल्पनः; इषत्करः, दुष्करः, सुकरः** — and the vṛtti names the\n'
        '  accent kept: **सर्वत्रैवात्र लित्स्वरः**, the one 6.1.193 gives a\n'
        '  लित् affix.\n'
        '\n'
        'SETTLED — **AND THE WORD कृत् IS THERE ONLY TO BE CLEAR.**\n'
        '  **कृद्ग्रहणं विस्पष्टार्थम्** — with a note on what it does not\n'
        '  reach: **प्रपचतितराम्, प्रपचतितमाम् इत्यत्र तरबाद्यन्तेन समासः**,\n'
        '  where the second member ends in तरप् and is no कृदन्त. This is the\n'
        '  rule the commentaries call उत्तरपदप्रकृतिस्वर, and 6.2.144 is\n'
        '  built to override it'
    ),
)

register(
    '6.2.140',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — उभे वनस्पत्यादिषु युगपत् — in the वनस्पत्यादि compounds\n'
        '  BOTH members keep their own accents AT ONCE: **वनस्पतिः,\n'
        '  बृहस्पतिः, शचीपतिः**. Two उदात्तs in one word, where every other\n'
        '  rule of the pāda leaves exactly one.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI ACCOUNTS FOR EACH ACCENT SEPARATELY.**\n'
        "  **वनपतिशब्दावाद्युदात्तौ पारस्करप्रभृतित्वात् सुट्** — 6.1.157's\n"
        '  list supplies the स् and both words are ādi-accented; **तद्बृहतोः\n'
        '  करपत्योश्चोरदेवतयोः सुट् तलोपश्च इति सुट् तकारलोपश्च** for\n'
        '  बृहस्पति; and for शचीपति, **शचीशब्दः कृदिकारादक्तिनः इति\n'
        '  ङीषन्तत्वाद् अन्तोदात्तः**. Three words, three different reasons'
    ),
)

register(
    '6.2.141',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — देवताद्वन्द्वे च — and in a द्वन्द्व of GODS both members\n'
        '  keep their accents at once: **इन्द्रासोमौ, इन्द्रावरुणौ,\n'
        '  इन्द्राबृहस्पती**.\n'
        '\n'
        'SETTLED — **AND THE THIRD OF THOSE CARRIES THREE उदात्तs.**\n'
        '  **बृहस्पतिशब्दे वनस्पत्यादित्वाद् द्वावुदात्तौ, तेनेन्द्राबृहस्पती\n'
        '  इत्यत्र त्रय उदात्ता भवन्ति** — 6.2.140 has already given बृहस्पति\n'
        '  two, and इन्द्र brings a third. Nowhere else in the Aṣṭādhyāyī\n'
        '  does one word end with three'
    ),
)

register(
    '6.2.142',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — न उत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु — but not\n'
        '  where the SECOND word begins अनुदात्त, unless it is पृथिवी, रुद्र,\n'
        '  पूषन् or मन्थिन्: **इन्द्राग्नी, इन्द्रवायू** —\n'
        '  **अग्निवायुशब्दावन्तोदात्तौ**, so they begin low and 6.2.141 is\n'
        '  refused. The four exceptions keep it: **द्यावापृथिव्यौ,\n'
        '  सोमारुद्रौ**.\n'
        '\n'
        'SETTLED — **AND THE WORD उत्तरपदे IS THERE TO SAY WHOSE FIRST\n'
        '  SYLLABLE IS MEANT.** **उत्तरपदग्रहणम् अनुदात्तादाव्\n'
        '  इत्युत्तरपदविशेषणं यथा स्याद्, द्वन्द्वविशेषणं मा भूदिति** —\n'
        '  अनुदात्तादि qualifies the second member, not the compound. And the\n'
        '  condition is stated at all **विधिप्रतिषेधयोर्विषयविभागार्थम्**, to\n'
        '  divide the ground cleanly between 6.2.141 and this refusal'
    ),
)

register(
    '6.2.143',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अन्तः — **अन्त इत्यधिकारः। यदित ऊर्ध्वमनुक्रमिष्यामस्तत्र\n'
        '  समासस्योत्तरपदस्यान्त उदात्तो भवतीत्येवं तद् वेदितव्यम्** — from\n'
        "  here to the end of the pāda the accent goes on the second member's\n"
        '  LAST syllable. The vṛtti reads the next sūtra out as its example:\n'
        '  **वक्ष्यति थाथघञ्क्ताजबित्रकाणाम् इति — सुनीथः, अवभृथः**.\n'
        '\n'
        'SETTLED — The longest of the three runs: fifty-seven sūtras, 6.2.143\n'
        '  to 6.2.199, and the pāda has nothing else after it'
    ),
)

register(
    '6.2.144',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — थाथघञ्क्ताजबित्रकाणाम् — a second member ending in any of\n'
        '  eight affixes takes the accent on its LAST syllable after a गति, a\n'
        '  कारक or an उपपद: **सुनीथः, अवभृथः** (थ), **आवसथः, उपवसथः** (अथ),\n'
        '  **प्रभेदः, काष्ठभेदः, रज्जुभेदः** (घञ्), **दूरादागतः, विशुष्कः**\n'
        '  (क्त).\n'
        '\n'
        'SETTLED — **AND IT EXISTS ONLY TO UNDO 6.2.139.** **तत्र\n'
        '  कृदुत्तरपदप्रकृतिस्वरत्वेनाद्युदात्तम् उत्तरपदं स्यात्** — without\n'
        '  this rule the कृदन्त would keep its own accent under 6.2.139 five\n'
        '  sūtras back, and for these eight affixes that accent is at the\n'
        '  front. 6.2.144 moves it to the end'
    ),
)

register(
    '6.2.145',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — सूपमानात् क्तः — a क्त-formed second member takes the\n'
        '  accent on its last syllable after सु or after what something is\n'
        '  COMPARED TO: **सुकृतम्, सुभुक्तम्, सुपीतम्; वृकावलुप्तम्,\n'
        '  शशप्लुतम्, सिंहविनर्दितम्** — torn as a wolf tears, leaping as a\n'
        '  hare leaps.\n'
        '\n'
        'SETTLED — **AND EACH HALF OVERRIDES A DIFFERENT EARLIER RULE.**\n'
        '  **सुशब्दाद् गतिरनन्तरः इति प्राप्त उपमानादपि तृतीया कर्मणि\n'
        '  इत्ययमपवादः** — after सु it displaces 6.2.49, after a comparison\n'
        '  6.2.48. One sūtra, two अपवादs'
    ),
)

register(
    '6.2.146',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — संज्ञायामनाचितादीनाम् — a क्त-formed second member takes\n'
        '  the accent on its last syllable where the compound is a NAME, the\n'
        '  आचितादि words excepted: **संभूतो रामायणः, उपहूतः शाकल्यः, परिजग्धः\n'
        '  कौण्डिन्यः; धनुष्खाता नदी, कुद्दालखातं नगरम्, हस्तिमृदिता भूमिः**\n'
        '  — men and rivers and towns called by what was done to them.\n'
        '\n'
        'SETTLED — **AND IT DISPLACES TWO RULES AT ONCE, EACH FOR ITS OWN\n'
        '  HALF.** **गतिरनन्तरः इत्यत्र हि कर्मणीत्यनुवर्तते, तद्बाधनार्थं\n'
        '  चेदम्** for the first three; **तृतीया कर्मणि इति प्राप्तिरिह\n'
        '  बाध्यते** for the last three'
    ),
)

register(
    '6.2.147',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — प्रवृद्धादीनां च — and the प्रवृद्धादि words, all of them\n'
        '  क्त-formed, take the accent on their last syllable: **प्रवृद्धं\n'
        '  यानम्, प्रवृद्धो वृषलः, प्रयुक्ताः सक्तवः, अवहितो भोगेषु,\n'
        '  खट्वारूढः, कविशस्तः**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI LEAVES A DISPUTE STANDING.** The gaṇa\n'
        '  lists each word beside a noun — यान for प्रवृद्ध, and so on. Are\n'
        '  those nouns binding? **यानादीनामत्र गणे पाठः\n'
        '  प्रायोवृत्तिप्रदर्शनार्थः, न विषयनियमार्थः... विषयनियमार्थ\n'
        '  एवेत्येके** — most say they only show the usual case, some say\n'
        '  they fix it, and the vṛtti reports both without choosing. It adds\n'
        '  two things it is sure of: **असंज्ञार्थोऽयमारम्भः** — this rule is\n'
        '  for where 6.2.146 does not reach, the compound not being a name —\n'
        '  and **आकृतिगणश्च प्रवृद्धादिर्द्रष्टव्यः**, the list is open'
    ),
)

register(
    '6.2.148',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कारकाद् दत्तश्रुतयोरेवाशिषि — where a NAME carries a\n'
        '  BLESSING, only दत्त and श्रुत take the accent on their last\n'
        '  syllable, and only after a कारक: **देवा एनं देयासुर् देवदत्तः;\n'
        '  विष्णुर् एनं श्रुयाद् विष्णुश्रुतः** — may the gods grant him, may\n'
        '  Viṣṇu hear him.\n'
        '\n'
        'SETTLED — **AND THE WORD एव MAKES THE RULE A RESTRICTION AND NOT A\n'
        '  GRANT.** **एतस्माद् नियमाद् अत्र संज्ञायामनाचितादीनाम्\n'
        "  इत्यन्तोदात्तत्वं न भवति** — in a blessing-name, 6.2.146's wider\n"
        '  grant is shut off and 6.2.48 takes what is left. And the vṛtti\n'
        '  asks which of the two words एव restricts: **एवकारकरणं किम्?\n'
        '  कारकावधारणं यथा स्याद्, दत्तश्रुतावधारणं मा भूत्** — it restricts\n'
        '  the source, not the pair'
    ),
)

register(
    '6.2.149',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — इत्थंभूतेन कृतम् इति च — where the compound means DONE BY\n'
        '  ONE IN SUCH A STATE, the क्त-formed second member takes the accent\n'
        '  on its last syllable: **सुप्तप्रलपितम्, उन्मत्तप्रलपितम्,\n'
        '  प्रमत्तगीतम्, विपन्नश्रुतम्** — babbled by a sleeper, sung by a\n'
        '  drunk man. **इमं प्रकारम् आपन्न इत्थंभूतः**.\n'
        '\n'
        'SETTLED — **AND कृतम् IS TAKEN AS WIDELY AS POSSIBLE.** **कृतमिति\n'
        '  क्रियासामान्ये करोतिर्वर्तते, नाभूतप्रादुर्भाव एव। तेन\n'
        '  प्रलपिताद्यपि कृतं भवति** — done, in the sense of any action at\n'
        '  all and not only of bringing something into being; otherwise\n'
        '  babbling would not count as done. And the vṛtti notes where the\n'
        '  rule is not needed: **भावे तु यदा प्रलपितादयस्तदा थाथादिस्वरेणैव\n'
        '  सिद्धम्** — read as abstract nouns they are already end-accented\n'
        '  by 6.2.144'
    ),
)

register(
    '6.2.150',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अनो भावकर्मवचनः — a second member ending in अन takes the\n'
        '  accent on its last syllable after a कारक, where it names the\n'
        '  ACTION or the OBJECT: **ओदनभोजनं सुखम्, पयःपानं सुखम्,\n'
        '  चन्दनप्रियङ्गुकालेपनं सुखम्** for the action; **राजभोजनाः शालयः,\n'
        '  राजाच्छादनानि वासांसि** for the object — rice for a king to eat,\n'
        '  cloth for a king to wear.\n'
        '\n'
        'SETTLED — **AND THE TWO SENSES COME FROM TWO READINGS OF ONE EARLIER\n'
        '  SŪTRA.** **कर्मणि च येन संस्पर्शात् कर्तुः शरीरसुखम् इत्ययं योग\n'
        '  उभयथा वर्ण्यते — कर्मण्युपपदे भावे ल्युड् भवति, कर्मण्यभिधेये\n'
        '  ल्युड् भवतीति** — 3.3.116 is read two ways, and each reading\n'
        "  supplies one half of this rule's examples"
    ),
)

register(
    '6.2.151',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — मन्क्तिन्व्याख्यानशयनासनस्थानयाजकादिक्रीताः — six kinds of\n'
        '  second member take the accent on their last syllable: **रथवर्त्म,\n'
        '  शकटवर्त्म** (मन्), **पाणिनिकृतिः, आपिशलिकृतिः** (क्तिन्),\n'
        '  **ऋगयनव्याख्यानम्, छन्दोव्याख्यानम्**, **राजशयनम्,\n'
        '  ब्राह्मणशयनम्**, **राजासनम्, ब्राह्मणासनम्**, **गोस्थानम्,\n'
        '  अश्वस्थानम्**, and the याजकादि words — **ब्राह्मणयाजकः,\n'
        '  क्षत्रिययाजकः, ब्राह्मणपूजकः, क्षत्रियपूजकः**'
    ),
)

register(
    '6.2.152',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — सप्तम्याः पुण्यम् — पुण्य after a LOCATIVE first member\n'
        '  takes the accent on its last syllable: **अध्ययने पुण्यम्\n'
        '  अध्ययनपुण्यम्, वेदे पुण्यं वेदपुण्यम्** — merit in study, merit in\n'
        '  the Veda. The compound comes from splitting 2.1.40 in two:\n'
        '  **सप्तमी इति योगविभागात् समासः**.\n'
        '\n'
        'SETTLED — **AND WITHOUT IT THE FIRST MEMBER WOULD HAVE KEPT THE\n'
        '  ACCENT.** **तत्पुरुषे तुल्यार्थ० इति पूर्वपदप्रकृतिस्वरत्वं\n'
        '  प्राप्तम् इत्यन्तोदात्तत्वं विधीयते** — 6.2.2 would have reached\n'
        "  it. The vṛtti adds a caveat about the other party's derivation:\n"
        '  **उणादीनां तु व्युत्पत्तिपक्षे कृत्स्वरेणाद्युदात्तः पुण्यशब्दः\n'
        '  स्यात्**'
    ),
)

register(
    '6.2.153',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — ऊनार्थकलहं तृतीयायाः — words meaning SHORT BY, and the\n'
        '  word कलह, take the accent on their last syllable after an\n'
        '  instrumental: **माषोनम्, कार्षापणोनम्, माषविकलम्, कार्षापणविकलम्;\n'
        '  असिकलहः, वाक्कलहः** — short by a bean, short by a coin; a quarrel\n'
        '  with swords, a quarrel with words.\n'
        '  **तृतीयापूर्वपदप्रकृतिस्वरापवादो योगः**.\n'
        '\n'
        'SETTLED — **AND ONE PARTY WOULD READ अर्थ AS A WORD AND NOT AS A\n'
        '  SENSE.** **अत्र केचिदर्थ इति स्वरूपग्रहणम् इच्छन्ति — धान्येनार्थो\n'
        '  धान्यार्थः** — they would have the sūtra reach the word अर्थ\n'
        '  itself. The vṛtti answers that ऊन already carries the\n'
        '  sense-reading, and that तृतीया is then merely **विस्पष्टार्थम्**'
    ),
)

register(
    '6.2.154',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — मिश्रं च अनुपसर्गम् असंधौ — मिश्र takes the accent on its\n'
        '  last syllable after an instrumental, with no उपसर्ग on it and no\n'
        '  ALLIANCE meant: **गुडमिश्राः, तिलमिश्राः, सर्पिर्मिश्राः**. The\n'
        '  vṛtti glosses the excluded sense: **संधिरिति हि पणबन्धेनैकार्थ्यम्\n'
        '  उच्यते**, a common purpose struck by agreement.\n'
        '\n'
        'SETTLED — **AND SAYING अनुपसर्गम् HERE TEACHES SOMETHING\n'
        '  ELSEWHERE.** **इहानुपसर्गग्रहणं ज्ञापकम् अन्यत्र मिश्रग्रहणे\n'
        '  सोपसर्गग्रहणस्य। तेन मिश्रश्लक्ष्णैः इति सोपसर्गेणापि मिश्रशब्देन\n'
        '  तृतीयासमासो भवति** — the need to exclude an उपसर्ग here shows that\n'
        '  where 2.1.31 names मिश्र it does not exclude one'
    ),
)

register(
    '6.2.155',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — नञो गुणप्रतिषेधे संपाद्यर्हहितालमर्थास्तद्धिताः — after\n'
        '  नञ् used to DENY A QUALITY, a taddhita-formed second member\n'
        '  meaning fit for, deserving, good for, or equal to takes the accent\n'
        '  on its last syllable: **अकार्णवेष्टकिकम्** (not fit to be made\n'
        '  into earrings), **अच्छैदिकः** (not deserving to be cut),\n'
        '  **अवत्सीयः** (not good for calves), **असांतापिकः** (not equal to\n'
        '  causing pain). Each is glossed in full: **कर्णवेष्टकाभ्यां संपादि\n'
        '  मुखं कार्णवेष्टकिकम्, न कार्णवेष्टकिकम्**'
    ),
)

register(
    '6.2.156',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — ययतोश्च अतदर्थे — and taddhita य or यत् in the same\n'
        '  position, where the sense is NOT for-that-purpose: **पाशानां समूहः\n'
        '  पाश्या, न पाश्या अपाश्या; अतृण्या**; **दन्तेषु भवं दन्त्यम्, न\n'
        '  दन्त्यम् अदन्त्यम्; अकर्ण्यम्**.\n'
        '\n'
        'SETTLED — **AND ONLY THE BARE AFFIXES ARE MEANT.**\n'
        '  **निरनुबन्धकैकानुबन्धकयोर् ययतोर्ग्रहणाद् इह न भवति** — य with no\n'
        '  it-marker and यत् with one; an affix carrying two markers is not\n'
        '  named by either'
    ),
)

register(
    '6.2.157',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अच्कावशक्तौ — after नञ्, a second member ending in अच् or\n'
        '  क takes the accent on its last syllable where INABILITY is meant:\n'
        '  **अपचो यः पक्तुं न शक्नोति; अजयः; अविक्षिपः, अविलिखः** — one who\n'
        '  cannot cook, cannot win, cannot throw'
    ),
)

register(
    '6.2.158',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — आक्रोशे च — and where ABUSE is meant: **अपचोऽयं जाल्मः,\n'
        '  अपठोऽयं जाल्मः; अविक्षिपः, अविलिखः**. The vṛtti marks the\n'
        '  difference from the sūtra before: **पक्तुं पठितुं\n'
        '  शक्तोऽप्येवमाक्रुश्यते** — he CAN cook, he CAN recite, and is\n'
        '  called this anyway'
    ),
)

register(
    '6.2.159',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — संज्ञायाम् — and where the नञ्-compound is a NAME, still\n'
        '  in the sense of abuse: **अदेवदत्तः, अयज्ञदत्तः, अविष्णुमित्रः** —\n'
        '  a no-Devadatta, a worthless Devadatta. Here no affix is named at\n'
        '  all: any second member will do'
    ),
)

register(
    '6.2.160',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कृत्युकेष्णुच्चार्वादयश्च — three affixes and a gaṇa, all\n'
        '  after नञ्: **अकर्तव्यम्, अकरणीयम्** (कृत्य), **अनागामुकम्,\n'
        '  अनपलाषुकम्** (उक), **अनलंकरिष्णुः, अनिराकरिष्णुः** (इष्णुच्), and\n'
        '  **अचारुः, असाधुः, अयौधिकः, अवदान्यः** — **चारु। साधु। यौधिक।\n'
        '  वदान्य**.\n'
        '\n'
        'SETTLED — **AND NAMING इष्णुच् REACHES A SECOND AFFIX IT DOES NOT\n'
        '  NAME.** **इष्णुज्ग्रहणे कर्तरि भुवः खिष्णुच् इत्यस्य\n'
        '  द्व्यनुबन्धकस्यापि ग्रहणम् इकारादेर् विधानसामर्थ्याद् भवति** —\n'
        '  खिष्णुच् carries two markers and so is not named; but since\n'
        '  इष्णुच् is prescribed with an initial इ, the shape reaches it\n'
        '  anyway: **अनाढ्यंभविष्णुः, असुभगंभविष्णुः**'
    ),
)

register(
    '6.2.161',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — विभाषा तृन्नन्नतीक्ष्णशुचिषु — after नञ्, a तृन्-formed\n'
        '  second member and three named words are OPTIONALLY end-accented:\n'
        '  **अकर्ता / अकर्ता, अनन्नम् / अनन्नम्, अतीक्ष्णम् / अतीक्ष्णम्,\n'
        '  अशुचिः / अशुचिः**. And the vṛtti says what the other option is:\n'
        "  **पक्षेऽव्ययस्वर एव भवति** — 6.2.2's accent for an indeclinable\n"
        '  first member, नञ् being one'
    ),
)

register(
    '6.2.162',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — बहुव्रीहाविदमेतत्तद्भ्यः प्रथमपूरणयोः क्रियागणने — after\n'
        '  इदम्, एतद् or तद्, the word प्रथम or an ordinal takes the accent\n'
        '  on its last syllable in a बहुव्रीहि COUNTING AN ACT: **इदं प्रथमं\n'
        '  गमनं भोजनं वा यस्य स इदंप्रथमः; इदंद्वितीयः, इदंतृतीयः,\n'
        '  एतत्प्रथमः, तत्प्रथमः, तत्तृतीयः** — one for whom this is a first\n'
        '  going or a first eating'
    ),
)

register(
    '6.2.163',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — संख्यायाः स्तनः — स्तन after a NUMERAL takes the accent on\n'
        '  its last syllable in a बहुव्रीहि: **द्विस्तना, त्रिस्तना,\n'
        '  चतुःस्तना**'
    ),
)

register(
    '6.2.164',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — विभाषा — and in the Veda the same accent is OPTIONAL:\n'
        '  **द्विस्तनां कुर्याद् वामदेवः** beside **द्विस्तनां करोति\n'
        '  द्यावापृथिव्योर् दोहाय चतुःस्तनां करोति पशूनां दोहाय**. The same\n'
        '  words, accented both ways in the same passage'
    ),
)

register(
    '6.2.165',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — संज्ञायां मित्राजिनयोः — मित्र and अजिन take the accent on\n'
        '  their last syllable in a बहुव्रीहि that is a NAME: **देवमित्रः,\n'
        '  ब्रह्ममित्रः; वृकाजिनः, कूलाजिनः, कृष्णाजिनः**.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA TAKES THE ṚṢIS BACK OUT.** **ऋषिप्रतिषेधो\n'
        "  मित्रे — विश्वामित्र ऋषिः** — a seer's name in मित्र is not\n"
        '  end-accented, however much of a name it is'
    ),
)

register(
    '6.2.166',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — व्यवायिनोऽन्तरम् — अन्तर takes the accent on its last\n'
        '  syllable in a बहुव्रीहि after a word naming what COMES BETWEEN:\n'
        '  **वस्त्रान्तरः, पटान्तरः, कम्बलान्तरः** — **वस्त्रम् अन्तरं\n'
        '  व्यवधायकं यस्य स वस्त्रान्तरः**, one with a cloth in between.\n'
        '  **व्यवायी व्यवधाता**'
    ),
)

register(
    '6.2.167',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — मुखं स्वाङ्गम् — मुख takes the accent on its last syllable\n'
        '  in a बहुव्रीहि where it names a PART OF THE BODY: **गौरमुखः,\n'
        '  भद्रमुखः**. And स्वाङ्ग is not loose here: **स्वाङ्गम्\n'
        "  अद्रवादिलक्षणम् इह गृह्यते** — the technical sense 1.1.54's\n"
        '  vārttika fixes'
    ),
)

register(
    '6.2.168',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — न अव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः — but not\n'
        '  after eight kinds of first member: **उच्चैर्मुखः, नीचैर्मुखः**\n'
        '  (indeclinable), **प्राङ्मुखः, प्रत्यङ्मुखः** (direction),\n'
        '  **गोमुखः, महामुखः, स्थूलमुखः, मुष्टिमुखः, पृथुमुखः, वत्समुखः**.\n'
        '  **पूर्वपदप्रकृतिस्वरो यथायोगमेषु भवति** — each falls back to\n'
        "  whichever rule of 6.2.1–63 keeps the first member's accent.\n"
        '\n'
        'SETTLED — **AND THE REFUSAL ALSO KILLS AN OPTION.**\n'
        '  **गोमुष्टिवत्सपूर्वस्योपमानलक्षणो विकल्पः पूर्वविप्रतिषेधेन\n'
        '  बाध्यते** — गो, मुष्टि and वत्स could be read as comparisons and\n'
        "  so fall under 6.2.169's option; being named here, they do not"
    ),
)

register(
    '6.2.169',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — निष्ठोपमानादन्यतरस्याम् — after a निष्ठा or a comparison,\n'
        '  मुख as a part of the body is OPTIONALLY end-accented: **सिंहमुखः /\n'
        '  सिंहमुखः, व्याघ्रमुखः / व्याघ्रमुखः**.\n'
        '\n'
        'SETTLED — **AND THE OPTION MAKES THREE ACCENTUATIONS, NOT TWO.**\n'
        "  **प्रक्षालितमुखः, प्रक्षालितमुखः, प्रक्षालितमुखः** — this rule's\n"
        "  end-accent; failing that, 6.2.110's option putting the accent at\n"
        '  the end of the FIRST member; and failing that too, the first\n'
        '  member simply keeping what it had. One word, three readings, from\n'
        '  two options meeting'
    ),
)

register(
    '6.2.170',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — जातिकालसुखादिभ्योऽनाच्छादनात् क्तोऽकृतमितप्रतिपन्नाः — a\n'
        '  क्त-formed second member takes the accent on its last syllable in\n'
        '  a बहुव्रीहि after a word for a CLASS (not of clothing), for a\n'
        '  TIME, or one of the सुखादि: **सारङ्गजग्धः, पलाण्डुभक्षितः,\n'
        '  सुरापीतः; मासजातः, संवत्सरजातः, द्व्यहजातः, त्र्यहजातः; सुखजातः,\n'
        '  दुःखजातः, तृप्रजातः** — one who has eaten venison, one born a\n'
        '  month ago. कृत, मित and प्रतिपन्न are shut out by name'
    ),
)

register(
    '6.2.171',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — वा जाते — and with जात the accent is OPTIONAL, after the\n'
        '  same three kinds of first member: **दन्तजातः / दन्तजातः, स्तनजातः\n'
        '  / स्तनजातः; मासजातः / मासजातः, संवत्सरजातः / संवत्सरजातः; सुखजातः\n'
        '  / सुखजातः, दुःखजातः / दुःखजातः** — one whose teeth have come in,\n'
        '  one born a month ago, one who has grown happy'
    ),
)

register(
    '6.2.172',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — नञ्सुभ्याम् — after नञ् or सु, the second member of a\n'
        '  बहुव्रीहि takes the accent on its last syllable, whatever it is:\n'
        '  **अयवो देशः, अव्रीहिः, अमाषः; सुयवः, सुव्रीहिः, सुमाषः** — a land\n'
        '  with no barley, a land with good barley.\n'
        '\n'
        "SETTLED — **AND THE ACCENT IS THE COMPOUND'S END, NOT THE STEM'S.**\n"
        '  **समासस्यैतद् अन्तोदात्तत्वम् इष्यते। समासान्ताश्चावयवा भवन्ति इति\n'
        '  अनृचो बह्वृच इत्यत्र कृते समासान्तेऽन्तोदात्तत्वं भवति** — where a\n'
        '  समासान्त has been added, the accent falls at the end of THAT. This\n'
        '  is the rule 6.2.116, 6.2.117 and 6.2.119 are each carved out of'
    ),
)

register(
    '6.2.173',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — कपि पूर्वम् — but before कप्, it is what stands BEFORE the\n'
        '  कप् that is end-accented, not the compound: **अकुमारीको देशः,\n'
        '  अवृषलीकः, अब्रह्मबन्धूकः; सुकुमारीकः, सुवृषलीकः,\n'
        '  सुब्रह्मबन्धूकः**. The accent sits on the last syllable of the\n'
        '  part preceding the affix, and the affix itself is left low.\n'
        '\n'
        'SETTLED — **AND IT BEATS 6.2.117 SIMPLY BY COMING LATER.** **कपि तु\n'
        '  परत्वात् कपि पूर्वम् इत्येतद् भवति** — सुकर्मा is ādi-accented by\n'
        '  6.2.117, but add कप् and this rule takes it'
    ),
)

register(
    '6.2.174',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — ह्रस्वान्तेऽन्त्यात् पूर्वम् — and where what precedes the\n'
        '  कप् ends in a SHORT vowel, the accent moves back one more: not the\n'
        '  last syllable but the one before it. **अयवको देशः, अव्रीहिकः,\n'
        '  अमाषकः; सुयवकः, सुव्रीहिकः, सुमाषकः**.\n'
        '\n'
        'SETTLED — **AND THE REPEATED WORD पूर्वम् MAKES IT A RESTRICTION.**\n'
        '  **पूर्वमिति वर्तमाने पुनःपूर्वग्रहणं प्रवृत्तिभेदेन\n'
        '  नियमप्रतिपत्त्यर्थम् — ह्रस्वान्तेऽन्त्याद् एव पूर्वम् उदात्तं\n'
        '  भवति, न कपि पूर्वम् इति** — पूर्वम् was already running from\n'
        '  6.2.173; saying it again shuts 6.2.173 out entirely wherever this\n'
        '  rule applies. **तेन अज्ञकः सुज्ञक इत्यत्र कबन्तस्यैव\n'
        '  अन्तोदात्तत्वं भवति**'
    ),
)

register(
    '6.2.175',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — बहोर्नञ्वद् उत्तरपदभूम्नि — where बहु states that there is\n'
        '  MUCH of what the second member names, बहु is accented AS THOUGH IT\n'
        '  WERE नञ्. Not one rule but four at once, the vṛtti stepping\n'
        '  through them: **नञ्सुभ्याम् इत्युक्तम्, बहोरपि तथा भवति — बहुयवो\n'
        '  देशः, बहुव्रीहिः, बहुतिलः; कपि पूर्वम् इत्युक्तम्, बहोरपि तथा भवति\n'
        '  — बहुकुमारीको देशः, बहुवृषलीकः; ह्रस्वान्तेऽन्त्यात् पूर्वम्\n'
        '  इत्युक्तम्, बहोरपि तथा भवति — बहुयवको देशः, बहुव्रीहिकः,\n'
        "  बहुमाषकः**. And 6.2.116's four words follow too. A single word\n"
        '  नञ्वत् importing a whole run'
    ),
)

register(
    '6.2.176',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — न गुणादयोऽवयवाः — but not where the गुणादि words name\n'
        '  PARTS of the thing: **बहुगुणा रज्जुः, बह्वक्षरं पदम्,\n'
        '  बहुच्छन्दोमानम्, बहुसूक्तः, बह्वध्यायः** — a rope of many strands,\n'
        '  a word of many syllables. **गुणादिराकृतिगणो द्रष्टव्यः**, and the\n'
        "  difference the rule turns on is the vṛtti's own: a strand is part\n"
        '  of the rope, learning is not part of the brahmin'
    ),
)

register(
    '6.2.177',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — उपसर्गात् स्वाङ्गं ध्रुवम् अपर्शु — after an उपसर्ग, a\n'
        '  second member naming a FIXED part of the body, पर्शु excepted, is\n'
        '  end-accented in a बहुव्रीहि: **प्रपृष्ठः, प्रोदरः, प्रललाटः**. And\n'
        '  ध्रुवम् is glossed: **ध्रुवम् इत्येकरूपम् उच्यते। ध्रुवम् अस्य\n'
        '  शीलम् इति यथा। सततं यस्य प्रगतं पृष्ठं भवति स प्रपृष्ठः** — one\n'
        '  whose back is permanently thrust forward, not one who has just now\n'
        '  raised his arms'
    ),
)

register(
    '6.2.178',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — वनं समासे — वन after an उपसर्ग is end-accented in ANY\n'
        '  compound: **प्रवणे यष्टव्यम्, निर्वणे प्रणिधीयते** — the ण् coming\n'
        '  from 8.4.5. **समासग्रहणं समासमात्रपरिग्रहार्थम्, बहुव्रीहावेव हि\n'
        '  स्यात्** — without the word समासे the बहुव्रीहि heading running\n'
        '  from 6.2.106 would have confined it'
    ),
)

register(
    '6.2.179',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अन्तः — and वन after अन्तर् likewise: **अन्तर्वणो देशः**.\n'
        '  The vṛtti says why a separate sūtra was needed at all:\n'
        '  **अनुपसर्गार्थ आरम्भः** — अन्तर् is no उपसर्ग, so 6.2.178 could\n'
        '  not have reached it'
    ),
)

register(
    '6.2.180',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अन्तश्च — and the word अन्तर् ITSELF is end-accented after\n'
        '  an उपसर्ग: **प्रान्तः, पर्यन्तः**. Which compound this is the\n'
        '  vṛtti leaves open: **बहुव्रीहिरयं प्रादिसमासो वा**'
    ),
)

register(
    '6.2.181',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — न निविभ्याम् — but not after नि or वि: **न्यन्तः,\n'
        '  व्यन्तः**.\n'
        '\n'
        'SETTLED — **AND THE REFUSAL LEAVES A SVARITA BEHIND.**\n'
        '  **पूर्वपदप्रकृतिस्वरत्वे कृते यणादेशः। तत्र उदात्तस्वरितयोर्यणः\n'
        '  स्वरितोऽनुदात्तस्य इति स्वरितो भवति** — the first member keeps its\n'
        '  accent, then its इ becomes य्, and 8.2.4 turns the following low\n'
        '  vowel svarita. न्यन्तः is not merely un-end-accented but carries a\n'
        '  third kind of accent altogether'
    ),
)

register(
    '6.2.182',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — परेरभितोभावि मण्डलम् — after परि, a second member naming\n'
        '  what lies ON BOTH SIDES, and the word मण्डल, are end-accented:\n'
        '  **परिकूलम्, परितीरम्, परिमण्डलम्**. **अभित इत्युभयतः। अभितो\n'
        '  भावोऽस्यास्तीति तदभितोभावि**.\n'
        '\n'
        'SETTLED — **AND IT OVERRIDES AN EARLIER RULE ON EITHER READING.**\n'
        '  **बहुव्रीहिरयं प्रादिसमासोऽव्ययीभावो वा। अव्ययीभावपक्षेऽपि हि\n'
        '  परिप्रत्युपापावर्ज्यमानाहोरात्रावयवेषु इति पूर्वपदप्रकृतिस्वरत्वं\n'
        '  प्राप्तम् अनेन बाध्यते** — read as an अव्ययीभाव, 6.2.33 would have\n'
        "  kept परि's accent; this rule takes it"
    ),
)

register(
    '6.2.183',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — प्राद् अस्वाङ्गं संज्ञायाम् — after प्र, a second member\n'
        '  NOT naming a part of the body is end-accented where the compound\n'
        '  is a NAME: **प्रकोष्ठम्, प्रगृहम्, प्रद्वारम्** — the forearm, the\n'
        '  front room, the gateway'
    ),
)

register(
    '6.2.184',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — निरुदकादीनि च — and the निरुदकादि words are end-accented:\n'
        '  **निरुदकम्, निरुलपम्, निरुपलम्, निर्मशकम्, निर्मक्षिकम्,\n'
        '  निष्कालकः, निष्पेषः, दुस्तरीपः**. The list is of whole COMPOUNDS —\n'
        '  **निरुदकादीनि च शब्दरूपाणि** — not of second members, and the\n'
        "  vṛtti leaves each one's analysis open: **एषां प्रादिसमासो\n"
        '  बहुव्रीहिर्वा। अव्ययीभावे तु समासान्तोदात्तत्वेनैव सिद्धम्**'
    ),
)

register(
    '6.2.185',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अभेर्मुखम् — मुख after अभि is end-accented: **अभिमुखः**.\n'
        '\n'
        'SETTLED — **AND IT IS STATED THOUGH 6.2.177 ALREADY COVERED IT — FOR\n'
        '  THREE REASONS.** **उपसर्गात् स्वाङ्गम् इति सिद्धे वचनम्\n'
        '  अबहुव्रीह्यर्थम् अध्रुवार्थम् अस्वाङ्गार्थं च** — 6.2.177 wanted a\n'
        '  बहुव्रीहि, a FIXED part, and a part of the BODY; this rule wants\n'
        '  none of the three, so it reaches **अभिमुखा शाला**, a hall that\n'
        '  faces one'
    ),
)

register(
    '6.2.186',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अपाच्च — and मुख after अप: **अपमुखः, अपमुखम्**. The vṛtti\n'
        '  says what it is for even where 6.2.177 would reach:\n'
        '  **अव्ययीभावेऽप्यत्र प्रयोजयति। तत्रापि हि परिप्रत्युपापा\n'
        '  वर्ज्यमानाहोरात्रावयवेषु इत्युक्तम्** — as an अव्ययीभाव it would\n'
        '  have fallen to 6.2.33 instead. And why it is a separate sūtra at\n'
        '  all: **योगविभाग उत्तरार्थः**, so that अप may carry into the next\n'
        '  rule'
    ),
)

register(
    '6.2.187',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — स्फिगपूतवीणाञ्जोऽध्वकुक्षिसीरनामनामानि च — six named\n'
        '  words, the words for a PLOUGH, and the word नामन्, are\n'
        '  end-accented after अप: **अपस्फिगम्, अपपूतम्, अपवीणम्, अपाञ्जः,\n'
        '  अपाध्वा, अपकुक्षिः; अपसीरः, अपहलम्, अपलाङ्गलम्; अपनाम**.\n'
        '\n'
        'SETTLED — **AND अध्वन् IS NAMED BECAUSE A समासान्त MAY FAIL TO\n'
        '  APPEAR.** **उपसर्गादध्वनः इति यदा समासान्तो नास्ति,\n'
        '  तदानेनान्तोदात्तत्वं भवति। तस्मिन् हि सत्यच्प्रत्ययस्य चित्त्वादेव\n'
        "  सिद्धम्। अनित्यश्च समासान्तः इत्येतदेव ज्ञापकम्** — with 5.4.85's\n"
        '  अच् in place the accent follows from its चित् marker; naming\n'
        '  अध्वन् here shows that the समासान्त is not compulsory'
    ),
)

register(
    '6.2.188',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अधेरुपरिस्थम् — after अधि, a second member naming what\n'
        '  stands ABOVE is end-accented: **अधिदन्तः, अधिकर्णः, अधिकेशः**. The\n'
        '  vṛtti explains the first: **दन्तस्योपरि योऽन्यो दन्तो जायते स\n'
        '  उच्यतेऽधिदन्त इति** — a tooth grown over a tooth. And it offers\n'
        '  the compound two analyses, **अध्यारूढो दन्त इति प्रादिसमासः।\n'
        '  अध्यारूढो वा दन्त इति समानाधिकरण उत्तरपदलोपी समासः**'
    ),
)

register(
    '6.2.189',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अनोरप्रधानकनीयसी — after अनु, a second member that is NOT\n'
        '  the principal word, and the word कनीयस्, are end-accented:\n'
        '  **अनुगतो ज्येष्ठम् अनुज्येष्ठः, अनुमध्यमः; अनुगतः कनीयान्\n'
        '  अनुकनीयान्**.\n'
        '\n'
        'SETTLED — **AND कनीयस् IS NAMED BECAUSE IT IS THE PRINCIPAL WORD.**\n'
        '  **पूर्वपदार्थप्रधानः प्रादिसमासोऽयम्** for the first two, but\n'
        '  **उत्तरपदार्थप्रधानोऽयम्** for अनुकनीयान् — **प्रधानार्थं च\n'
        '  कनीयोग्रहणम्**. The sūtra names it precisely because अप्रधान would\n'
        '  have shut it out'
    ),
)

register(
    '6.2.190',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — पुरुषश्चान्वादिष्टः — and पुरुष after अनु, where it means\n'
        '  one SPOKEN OF AFTERWARDS: **अन्वादिष्टः पुरुषः अनुपुरुषः**. The\n'
        '  vṛtti glosses the sense three ways: **अन्वादिष्टोऽन्वाचितः\n'
        '  कथितानुकथितो वा**'
    ),
)

register(
    '6.2.191',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — अतेरकृत्पदे — after अति, a second member that is NOT a\n'
        '  कृदन्त, and the word पद, are end-accented: **अत्यङ्कुशो नागः,\n'
        '  अतिकशोऽश्वः** — an elephant past the goad, a horse past the whip;\n'
        '  **अतिपदा शक्वरी** for पद.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA ADDS A CONDITION THE SŪTRA DOES NOT\n'
        '  STATE.** **अतेर्धातुलोप इति वक्तव्यम्** — a verbal root must have\n'
        '  been dropped from the analysis. **इह मा भूत् — शोभनो गार्ग्यः\n'
        '  अतिगार्ग्यः। इह च यथा स्यात् — अतिक्रान्तः कारकाद् अतिकारक इति** —\n'
        '  so अतिकारक IS reached when it means gone past the agent, the verb\n'
        '  क्रान्त having dropped out, though अतिकारकः meaning a fine agent\n'
        '  is not'
    ),
)

register(
    '6.2.192',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — नेरनिधाने — after नि, the second member is end-accented\n'
        '  where CONCEALMENT is not meant: **निमूलम्, न्यक्षम्, नितृणम्**.\n'
        '  **निधानम् अप्रकाशता**.\n'
        '\n'
        'SETTLED — **AND WHY AN उपसर्ग CAN CARRY A SENSE AT ALL.**\n'
        '  **निशब्दोऽत्र निधानार्थं ब्रवीति। प्रादयो हि वृत्तिविषये ससाधनां\n'
        '  क्रियाम् आहुः** — inside a compound a प्रादि states a whole action\n'
        '  along with its means, and that is how नि can mean laid away and\n'
        '  not merely down'
    ),
)

register(
    '6.2.193',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — प्रतेरंश्वादयस्तत्पुरुषे — after प्रति, the अंश्वादि words\n'
        '  are end-accented in a तत्पुरुष: **प्रतिगतः अंशुः प्रत्यंशुः,\n'
        '  प्रतिजनः, प्रतिराजा**. The gaṇa runs **अंशु। जन। राजन्। उष्ट्र।\n'
        '  खेटक। अजिर। आर्द्रा। श्रवण। कृत्तिका। अर्ध। पुर**, and राजन् is in\n'
        '  it for a reason: **राजशब्दः समासान्तस्यानित्यत्वाद् यदा टज्\n'
        '  नास्ति, तदा प्रयोजयति**'
    ),
)

register(
    '6.2.194',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — उपाद् द्व्यजजिनमगौरादयः — after उप, a second member of TWO\n'
        '  VOWELS, and the word अजिन, are end-accented in a तत्पुरुष, the\n'
        '  गौरादि words excepted: **उपगतो देवम् उपदेवः, उपसोमः, उपेन्द्रः,\n'
        '  उपहोडः; उपाजिनम्**. The gaṇa closes **गौर। तैष। तैट। लट। लोट।\n'
        '  जिह्वा। कृष्णा। कन्या। गुड। कल्प। पाद। गौरादिः**'
    ),
)

register(
    '6.2.195',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — सोरवक्षेपणे — after सु, the second member of a तत्पुरुष is\n'
        '  end-accented where SCORN is meant: **इह खल्विदानीं सुस्थण्डिले\n'
        '  सुस्फिगाभ्यां सुप्रत्यवसितः**. **अवक्षेपणं निन्दा**.\n'
        '\n'
        'SETTLED — **AND सु ITSELF STILL MEANS PRAISE.** **सुशब्दोऽत्र\n'
        '  पूजायामेव। वाक्यार्थस्तु अवक्षेपणम् असूयया तथाभिधानात्** — the\n'
        '  scorn is not in the word but in the sentence: one says *nicely*\n'
        '  out of spite'
    ),
)

register(
    '6.2.196',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — विभाषोत्पुच्छे — उत्पुच्छ in a तत्पुरुष is OPTIONALLY\n'
        '  end-accented: **उत्क्रान्तः पुच्छाद् उत्पुच्छः / उत्पुच्छः**.\n'
        '\n'
        'SETTLED — **AND THE OPTION WORKS BOTH WAYS AT ONCE.** **यदा तु\n'
        '  पुच्छमुदस्यति उत्पुच्छयति, उत्पुच्छयतेरच्, उत्पुच्छः, तदा\n'
        '  थाथादिसूत्रेण नित्यम् अन्तोदात्तत्वे प्राप्ते विकल्पोऽयम् इति\n'
        '  सेयम् उभयत्रविभाषा भवति** — read one way the end-accent was not\n'
        '  otherwise available and the option grants it; read the other,\n'
        '  6.2.144 had already made it compulsory and the option takes it\n'
        '  away. An उभयत्रविभाषा'
    ),
)

register(
    '6.2.197',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — द्वित्रिभ्यां पाद्दन्मूर्धसु बहुव्रीहौ — after द्वि or\n'
        '  त्रि, these three are OPTIONALLY end-accented in a बहुव्रीहि:\n'
        '  **द्वौ पादावस्य द्विपात् / द्विपात्; त्रिपात् / त्रिपात्; द्विदन्\n'
        '  / द्विदन्; द्विमूर्धा / द्विमूर्धा**.\n'
        '\n'
        'SETTLED — **AND EACH OF THE THREE IS NAMED IN A DIFFERENT STATE.**\n'
        '  **पादिति कृताकारलोपः पादशब्दो गृह्यते। ददिति कृतददादेशो दन्तशब्दः।\n'
        '  मूर्धन्निति त्वकृतसमासान्तो नान्त एव मूर्धन्शब्दः** — पाद् after\n'
        '  its आ has gone, दत् after the दद्-substitution has happened, but\n'
        '  मूर्धन् before any समासान्त is added. Three words, three different\n'
        '  points in the derivation'
    ),
)

register(
    '6.2.198',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — सक्थं च अक्रान्तात् — सक्थ is OPTIONALLY end-accented\n'
        '  after a first member NOT ending in क: **गौरसक्थः / गौरसक्थः,\n'
        '  श्लक्ष्णसक्थः / श्लक्ष्णसक्थः**. And the word is named in a\n'
        '  particular state: **सक्थमिति कृतसमासान्तः सक्थिशब्दोऽत्र गृह्यते**\n'
        '  — सक्थि after its समासान्त has been added'
    ),
)

register(
    '6.2.199',
    apply=second_member,
    codification=_SECOND_MEMBER,
    notes=(
        'SETTLED — परादिश्छन्दसि बहुलम् — in the Veda, VARIOUSLY, the accent\n'
        '  falls on the first syllable of the FOLLOWING word:\n'
        '  **अञ्जिसक्थमालभेत; त्वाष्ट्रौ लोमशसक्थौ; ऋजुबाहुः, वाक्पतिः,\n'
        '  चित्पतिः**. And पर here is not any following word: **परशब्देनात्र\n'
        '  सक्थशब्द एव गृह्यते**, it carries सक्थ down from 6.2.198.\n'
        '\n'
        'SETTLED — **AND THE PĀDA ENDS BY ADMITTING THAT ITS OWN RULES ARE\n'
        '  NOT THE WHOLE STORY.** **परादिश्च परान्तश्च पूर्वान्तश्चापि\n'
        '  दृश्यते। पूर्वादयश्च दृश्यन्ते व्यत्ययो बहुलं ततः** —\n'
        '  first-of-the-second, last-of-the-second, last-of-the-first and\n'
        '  first-of-the-first are all attested, and the exchange between them\n'
        '  is many-sided. A vārttika adds one more list: **अन्तोदात्तप्रकरणे\n'
        '  त्रिचक्रादीनां छन्दस्युपसंख्यानम् — त्रिबन्धुरेण, त्रिवृता रथेन\n'
        '  त्रिचक्रेण**'
    ),
)


__all__ = ['first_member', 'placed_on', 'second_member']
