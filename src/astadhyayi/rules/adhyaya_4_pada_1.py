# -*- coding: utf-8 -*-
"""
अध्याय ४, पाद १ — the nominal base, the case-endings, and the feminine.

अध्याय ३ gave every affix that comes after a ROOT. This chapter gives
those that come after a STEM, and it opens by laying two foundations:
4.1.1 ङ्याप्प्रातिपदिकात् names what all of them attach to and governs
to the end of अध्याय ५, and 4.1.2 enumerates the twenty-one case
endings — the nominal counterpart of 3.4.78, and built the same way,
with silent letters cutting names out of the list.

Then 4.1.3 स्त्रियाम् opens the feminine affixes, which run to 4.1.75.
"""

from __future__ import annotations

from src.astadhyayi.apatya import (
    apatya_affix, apatya_sense, descendant_name, feminine_luk,
    only_one, tadraja, tadraja_luk,
)
from src.astadhyayi.sources import register
from src.astadhyayi.stri import stri_affix, stri_heading
from src.astadhyayi.taddhita import (
    default_affix, elision, prag_divyatah_affix, samartha,
    taddhita_heading,
)
from src.astadhyayi.sup import nominal_base, sup_endings


_RULES = {
    '4.1.1': (
        'SETTLED — ङ्याप्प्रातिपदिकात्, अधिकारोऽयम्. यदित ऊर्ध्वम्\n'
        '  अनुक्रमिष्याम आ पञ्चमाध्यायपरिसमाप्तेः — it governs to the END\n'
        '  OF अध्याय ५, which is the longest range a heading has claimed\n'
        "  in this project. 3.2.84's भूते covered part of a pāda; 3.4.67's\n"
        '  कर्तरि कृत् filled gaps in one; this governs two chapters.\n'
        '\n'
        'SETTLED — three names in one compound, two of them class-words.\n'
        '  ङीब्ङीष्ङीनां सामान्येन ग्रहणं ङीति,\n'
        '  टाप्डाप्चापामाबिति — ङी stands for three affixes and आप् for\n'
        '  three, and प्रातिपदिक is the name 1.2.45 and 1.2.46 confer.\n'
        '  तेषां समाहारनिर्देशो ङ्याप्प्रातिपदिकादिति.\n'
        '\n'
        'SETTLED — and the vṛtti asks why the two feminine names are\n'
        '  there at all, since प्रातिपदिकग्रहणे लिङ्गविशिष्टस्यापि ग्रहणं\n'
        '  भवति (परि० ७१) would bring a feminine stem under प्रातिपदिक\n'
        '  anyway. नैतदस्ति: that principle holds only where a base is\n'
        "  named AS ITSELF — स्वरूपविधिविषये परिभाषेयम् — and 2.1.67's\n"
        '  युवा खलतिपलितवलिनजरतीभिः is the ज्ञापक for reading it so.\n'
        '  There is a second reason as well: तदन्तात् तद्धितविधानार्थम्,\n'
        '  so that a taddhita may come after a feminine — कालितरा,\n'
        '  हरिणितरा, खट्वातरा — since otherwise विप्रतिषेधाद्धि\n'
        '  तद्धितबलीयस्त्वं स्यात्.'
    ),
    '4.1.2': (
        'SETTLED — स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्-\n'
        '  ङसोसाम्ङ्योस्सुप्: TWENTY-ONE case-endings, three numbers in\n'
        '  each of seven cases. कुमारी, कुमार्यौ, कुमार्यः through to\n'
        '  कुमार्याम्, कुमार्योः, कुमारीषु; and दृषद्, दृषदौ, दृषदः from\n'
        '  a bare stem.\n'
        '\n'
        'SETTLED — THE NOMINAL COUNTERPART OF 3.4.78, AND IT MAKES TWO\n'
        '  NAMES WHERE THAT MADE ONE. औटष्टकारः सुडिति\n'
        '  प्रत्याहारग्रहणार्थः — the ट् of the fifth ending makes सुट्,\n'
        '  the first five taken together; पकारः सुबिति प्रत्याहारार्थः —\n'
        '  the प् of the twenty-first makes सुप्, the whole. 3.4.78 spent\n'
        '  the last letter of its last member on तिङ्; this spends two\n'
        '  letters on two pratyāhāras, and the rest are\n'
        '  उकारादयोऽनुबन्धा यथायोगमुच्चारणविशेषणार्थाः, there only to\n'
        '  make the list sayable.\n'
        '\n'
        'SETTLED — and the senses are given somewhere else.\n'
        '  संख्याकर्मादयश्च स्वादीनामर्थाः शास्त्रान्तरेण विहिताः, तेन\n'
        '  सहास्यैकवाक्यता: number comes from 1.4.21 and the kāraka from\n'
        '  अध्याय २, and this rule is read as ONE SENTENCE with those.\n'
        '  The reverse of how the कृत् affixes were handled — each of\n'
        '  those was given IN a sense, and 3.4.67 had to supply one only\n'
        '  where a rule had not.'
    ),
    '4.1.3': (
        'SETTLED — स्त्रियाम्, अधिकारोऽयम्. वक्ष्यति अजाद्यतष्टाप् — अजा,\n'
        '  देवदत्ता. स्त्रियामिति किम्? अजः, देवदत्तः.\n'
        '\n'
        'SETTLED — A HEADING THAT TAKES ONLY PART OF THE HEADING ABOVE\n'
        '  IT. ङ्याप्प्रातिपदिकात् इति सर्वाधिकारेऽपि प्रातिपदिकमात्रम्\n'
        '  अत्र प्रकरणे संबध्यते, ङ्यापोरनेनैव विधानात् — 4.1.1 names\n'
        '  three things and only one of them can be the input here,\n'
        '  because this is the section that MAKES the other two. A rule\n'
        '  cannot take as its input what it is about to produce, and the\n'
        '  restriction is read off that fact rather than stated.\n'
        '\n'
        'SETTLED — and what स्त्री means is deliberately left open, twice\n'
        '  over. केयं स्त्री नाम? सामान्यविशेषाः स्त्रीत्वादयो गोत्वादया\n'
        '  इव बहुप्रकारा व्यक्तयः — femininity is a universal of many\n'
        '  kinds, and क्वचिदाश्रयविशेषाभावादुपदेशव्यङ्ग्या एव भवन्ति,\n'
        '  sometimes with no bodily mark at all, shown by usage as\n'
        '  ब्राह्मणत्व is. Then the syntax is left open too: स्त्रीत्वं च\n'
        '  प्रत्ययार्थः प्रकृत्यर्थविशेषणं चेत्युभयथापि युज्यते — it may\n'
        '  be what the AFFIX means or what qualifies what the STEM means,\n'
        '  and both readings work. A heading whose central word is given\n'
        '  two analyses and neither chosen.'
    ),
    '4.1.4': (
        'SETTLED — अजाद्यतष्टाप्. टाप् from the अजादि list and from any\n'
        '  stem in short अ: अजा, एडका, कोकिला, चटका, अश्वा; खट्वा,\n'
        '  देवदत्ता. तपरकरणं तत्कालार्थम् — the त holds it to the SHORT\n'
        '  vowel, which is why शुभंयाः and कीलालपाः take no टाप् and lose\n'
        '  their सु by 6.1.68 instead.\n'
        '\n'
        'SETTLED — a गण whose members do not share a reason.\n'
        '  अजादिग्रहणं तु क्वचिद् जातिलक्षणे ङीषि प्राप्ते, क्वचित् तु\n'
        '  पुंयोगलक्षणे, क्वचित् पुष्पफलोत्तरपदलक्षणे, क्वचित् वयोलक्षणे\n'
        '  ङीपि, क्वचित् टिल्लक्षणे — the members are there to block FIVE\n'
        '  different rules, a different one each, and हलन्तानां\n'
        '  त्वप्राप्त एव कस्मिंश्चिदाब् विधीयते: some are there for a\n'
        '  case no rule reached at all. The list is a list of\n'
        '  exceptions to different things, collected under one name\n'
        '  because they all end up with the same affix.\n'
        '\n'
        'SETTLED — पकारः सामान्यग्रहणार्थः, टकारः\n'
        '  सामान्यग्रहणाविघातार्थः. The प् so that आप् as a class-word\n'
        '  reaches it, and the ट् so that being reached as a class does\n'
        '  not stop 1.1.64 finding its टि. One letter enabling a general\n'
        '  reading and the other protecting what that reading would have\n'
        '  cost.\n'
        '\n'
        'NOTE — शूद्रा चामहत्पूर्वा जातिः (ग०सू० ३८) is where the vṛtti\n'
        '  argues that तदन्तविधि DOES hold in this section, against\n'
        '  ग्रहणवता प्रातिपदिकेन तदन्तविधिर्न (परि० ३१): एतदेव ज्ञापकम् —\n'
        '  भवत्यस्मिन् प्रकरणे तदन्तविधिरिति. The fruit is अतिधीवरी,\n'
        '  अतिपीवरी, अतिभवती, अतिमहती.'
    ),
    '4.1.5': (
        'SETTLED — ऋन्नेभ्यो ङीप्. From a stem in ऋ or in न्: कर्त्री,\n'
        '  हर्त्री; दण्डिनी, छत्रिणी. ङकारः सामान्यग्रहणार्थः — the ङ् so\n'
        "  that 4.1.1's class-word ङी reaches it, which is the same job\n"
        '  the प् of टाप् does for आप्.'
    ),
    '4.1.6': (
        'SETTLED — उगितश्च. उग् इद् यत्र संभवति यथाकथंचित्\n'
        '  तदुगिच्छब्दरूपम् — whatever has उ, ऋ or ऌ as an इत्, HOWEVER\n'
        '  it came by it: भवती, अतिभवती, पचन्ती, यजन्ती.\n'
        '\n'
        'NOTE — two vārttikas pulling opposite ways. धातोरुगितः\n'
        '  प्रतिषेधो वक्तव्यः takes out the case where the उगित् is a\n'
        '  root — उखास्रत्, पर्णध्वत् ब्राह्मणी — and\n'
        '  अञ्चतेश्चोपसंख्यानम् puts three words back: प्राची, प्रतीची,\n'
        '  उदीची. A class narrowed and then widened by name.'
    ),
    '4.1.7': (
        'SETTLED — वनो र च. From a वन्-final stem, with र replacing the\n'
        '  final: धीवरी, पीवरी, शर्वरी, परलोकदृश्वरी.\n'
        '\n'
        'SETTLED — the affix this rule names is not what it is for.\n'
        '  ऋन्नेभ्यः इत्येव ङीपि सिद्धे तत्सन्नियोगेन रेफविधानार्थं\n'
        '  वचनम् — 4.1.5 already gives ङीप् to any न्-final stem, so the\n'
        '  whole content of this rule is the र, and the affix is named\n'
        '  only because the two must come together. Compare 3.4.84, where\n'
        '  the endings and आह् were likewise one act.\n'
        '\n'
        'NOTE — वाने न हशः refuses BOTH after a consonant: सहयुध्वा\n'
        '  ब्राह्मणी. प्राप्तौ ङीब्रावुभावपि प्रतिषिध्येते.'
    ),
    '4.1.8': (
        'SETTLED — पादोऽन्यतरस्याम्. द्विपात् beside द्विपदी, त्रिपात्\n'
        '  beside त्रिपदी, चतुष्पाद् beside चतुष्पदी.\n'
        '\n'
        'NOTE — पाद इति कृतसमासान्तः पादशब्दो निर्दिश्यते: the form named\n'
        '  is the one a compound has ALREADY finished, not the bare word.\n'
        '  A rule whose subject is an intermediate stage of a derivation.'
    ),
    '4.1.9': (
        'SETTLED — टाब् ऋचि, ङीपोऽपवादः. Where a verse is meant, टाप् and\n'
        "  not the last rule's ङीप्: द्विपदा ऋक्, त्रिपदा ऋक्, चतुष्पदा\n"
        '  ऋक्. ऋचीत्यभिधेयनिर्देशः — the condition is what the word\n'
        '  DENOTES, not what it is made of. ऋचीति किम्? द्विपदी देवदत्ता.'
    ),
    '4.1.10': (
        'SETTLED — न षट्स्वस्रादिभ्यः. From a stem the grammar calls षट्,\n'
        '  and from स्वसृ and its list, NO feminine affix at all: पञ्च\n'
        '  ब्राह्मण्यः, सप्त, नव, दश; स्वसा, दुहिता, ननान्दा, याता, माता,\n'
        '  तिस्रः, चतस्रः.\n'
        '\n'
        'SETTLED — यो यतः प्राप्नोति स सर्वः प्रतिषिध्यते. Whichever affix\n'
        '  would have come from wherever, ALL of them are refused. Every\n'
        '  other प्रतिषेध of this run names the affix it refuses; this one\n'
        '  refuses the whole section, which is why its row alone carries\n'
        '  no affix.\n'
        '\n'
        'NOTE — the kārikā षट्संज्ञानामन्ते लुप्ते टाबुत्पत्तिः कस्मान्न\n'
        '  स्यात् / प्रत्याहाराच्चापा सिद्धं दोषस्त्वित्त्वे तस्मान्नोभौ\n'
        '  asks why टाप् does not come once a षट् word has lost its final,\n'
        '  and answers from the आप् class-word.'
    ),
    '4.1.11': (
        'SETTLED — मनः. 4.1.5 would give ङीप् to any न्-final stem; this\n'
        '  refuses it for those in मन्: दामा, पामा.\n'
        '\n'
        'SETTLED — and by परि० १६ (अनिनस्मन्ग्रहणान्यर्थवता चानर्थकेन च\n'
        '  तदन्तविधिं प्रयोजयन्ति) the refusal also reaches सीमा and\n'
        '  अतिमहिमा, where the मन् is not an affix and carries no meaning\n'
        '  of its own. A paribhāṣā that lets three named endings be read\n'
        '  as bare shapes, and it is stated for exactly these three.'
    ),
    '4.1.12': (
        'SETTLED — अनो बहुव्रीहेः. ङीप् refused for an अन्-final\n'
        '  bahuvrīhi: सुपर्वा, सुचर्मा. बहुव्रीहेरिति किम्? अतिराज्ञी.\n'
        '\n'
        'NOTE — अनुपधालोपी बहुव्रीहिरिहोदाहरणम्, उपधालोपिनो हि विकल्पं\n'
        '  वक्ष्यति: the example given is one that does NOT drop its\n'
        '  penultimate, because 4.1.28 will make that case optional\n'
        '  instead. The vṛtti chooses its example to keep two rules apart.'
    ),
    '4.1.13': (
        'SETTLED — डाब् उभाभ्यामन्यतरस्याम्. From BOTH the stems the last\n'
        '  two rules refused, डाप् comes optionally: पामा, पामे; सीमा,\n'
        '  सीमे; बहुराजा, बहुराजे; बहुतक्षा, बहुतक्षे. उभाभ्याम् is two\n'
        '  other sūtras taken as one word — a rule whose subject is a pair\n'
        '  of rules rather than a class of stems.\n'
        '\n'
        'SETTLED — and its option is spent six sūtras back.\n'
        '  अन्यतरस्यांग्रहणं किमर्थम्? बहुव्रीहौ वनो र च इत्यस्यापि\n'
        '  विकल्पो यथा स्यात् — the word *optionally* is here so that\n'
        "  4.1.7's र becomes optional in a bahuvrīhi: बहुधीवा beside\n"
        "  बहुधीवरी, बहुपीवा beside बहुपीवरी. The same shape as 3.4.111's\n"
        '  एवकार उत्तरार्थः, and running the other way.'
    ),
    '4.1.14': (
        'SETTLED — अनुपसर्जनात्, अधिकारोऽयम्. उत्तरसूत्रेषूपसर्जन-\n'
        '  प्रतिषेधं करोति: a stem that is a SUBORDINATE member of a\n'
        '  compound takes none of these affixes. बहुकुरुचरा against\n'
        '  कुरुचरी, बहुकुक्कुटा against कुक्कुटी.\n'
        '\n'
        'SETTLED — and the heading settles a question it does not raise.\n'
        '  अस्त्यत्र प्रकरणे तदन्तविधिरिति, तथा च प्रधानेन तदन्तविधिर्\n'
        '  भवति — the rules of this section DO reach a compound through\n'
        '  its last member, but only where that member is the principal\n'
        '  one: कुम्भकारी, नगरकारी. So one heading both permits the\n'
        '  compound-reaching and bounds it, and the bound is what it says\n'
        '  out loud.'
    ),
    '4.1.15': (
        'SETTLED — टिड्ढाणञ्द्वयसज्दघ्नञ्मात्रच्तयप्ठक्ठञ्कञ्क्वरप्-\n'
        '  ख्युनाम्, टापोऽपवादः. THIRTEEN kinds of affix named in one\n'
        '  compound, and a stem ending in any of them takes ङीप्:\n'
        '  कुरुचरी, सौपर्णेयी, कुम्भकारी, औत्सी, ऊरुद्वयसी, ऊरुदघ्नी,\n'
        '  ऊरुमात्री, पञ्चतयी, आक्षिकी, लावणिकी, यादृशी, इत्वरी,\n'
        '  आढ्यंकरणी.\n'
        '\n'
        'SETTLED — and being टित् is not always being टित्. इह कस्माद् न\n'
        '  भवति पचमाना, यजमाना? द्व्यनुबन्धकत्वाल् लटः — शानच् is टित्\n'
        '  only because लट् is, and लट् carries TWO marks, so the mark is\n'
        "  not the affix's own. ल्युडादिषु कथम्? टित्करणसामर्थ्यात्, and\n"
        '  इतरत्र तु टेरेत्वं फलम्: where the mark was put there on\n'
        '  purpose it counts, and where it was there for something else it\n'
        '  does not. पठिता विद्या is kept out on the same ground —\n'
        "  आगमटित्त्वमनिमित्तम्, an augment's mark is no cause.\n"
        '\n'
        'SETTLED — three of the thirteen carry a note. ढ:\n'
        '  निरनुबन्धको ढशब्दः स्त्रियां नास्तीति निरनुबन्धकपरिभाषा\n'
        '  (परि० ८१) न प्रवर्तते — the rule that an unmarked name means\n'
        '  the unmarked thing cannot apply, because there is no unmarked ढ\n'
        '  here for it to mean. अण्: णेऽपि क्वचिदण्कृतं कार्यं भवति\n'
        '  (परि० ८७), so चौरी and तापसी come by it and दाण्डा and मौष्टा\n'
        '  do not — a paribhāṣā that holds SOMETIMES, and the vṛtti says\n'
        '  which times. अञ्: 4.1.73 names it again, शार्ङ्गरवाद्यञः इति\n'
        '  पुनरञो ग्रहणं जातिलक्षणं ङीषं बाधितुम्, because this naming\n'
        '  cannot beat 4.1.63 and that one can.'
    ),
    '4.1.16': (
        'SETTLED — यञश्च, ङीबित्येव. गार्गी, वात्सी.\n'
        "  आपत्यग्रहणं कर्तव्यम् — only the patronymic यञ्, so 4.3.10's\n"
        '  द्वीपादनुसमुद्रं यञ् is left out and द्वैप्या stands.\n'
        '\n'
        'SETTLED — योगविभाग उत्तरार्थः. The rule is split off from 4.1.15\n'
        '  not for its own sake but for the NEXT one, which needs यञ्\n'
        '  standing alone to carry down. A rule made separate so that a\n'
        '  word may be borrowed from it.'
    ),
    '4.1.17': (
        "SETTLED — प्राचां ष्फ तद्धितः. In the eastern teachers' view,\n"
        '  ष्फ: गार्ग्यायणी, वात्स्यायनी. अन्येषाम् — गार्गी, वात्सी.\n'
        "  The fourth attribution the project has met, after 3.4.18's\n"
        "  प्राचाम्, 3.4.19's उदीचाम् and 3.4.111's शाकटायन.\n"
        '\n'
        'SETTLED — one affix bringing another. षकारो ङीषर्थः, and\n'
        '  प्रत्ययद्वयेनेह स्त्रीत्वं व्यज्यते — the ष् fetches ङीष् as\n'
        '  well, so the feminine is shown TWICE in one word.\n'
        '\n'
        'SETTLED — and calling it a taddhita is not description but\n'
        '  provision. तद्धितग्रहणं प्रातिपदिकसंज्ञार्थम्: the name is\n'
        '  what makes what it forms a प्रातिपदिक by 1.2.46, so the second\n'
        '  affix has something to attach to. A word in a rule that exists\n'
        '  to trigger a naming rule two chapters back.'
    ),
    '4.1.18': (
        'SETTLED — सर्वत्र लोहितादिकतन्तेभ्यः. पूर्वेण विकल्पे प्राप्ते\n'
        '  नित्यार्थं वचनम् — 4.1.17 left it open and this closes it for\n'
        '  the list from लोहित to कत: लौहित्यायनी, शांसित्यायनी,\n'
        '  बाभ्रव्यायणी.\n'
        '\n'
        'SETTLED — ANUVṚTTI RUNNING BACKWARD. सर्वत्रग्रहणम्\n'
        '  उत्तरसूत्रादिहापकृष्यते, बाधकबाधनार्थम् — the word सर्वत्र is\n'
        '  pulled DOWN out of this rule into 4.1.17, so that the eastern\n'
        "  teachers' ष्फ may beat even 4.1.75's चाप्: आवट्यायनी. Words\n"
        '  normally carry forward; this one is read the other way, and\n'
        '  the vṛtti says so in as many words.\n'
        '\n'
        'NOTE — कतशब्दः स्वतन्त्रं यत् प्रातिपदिकं तदवधित्वेन\n'
        '  परिगृह्यते: the boundary word is कत standing on its own —\n'
        '  कपिशब्दात् परः कपि कत — and not a कत inside a compound like\n'
        "  कुरुकत. A list's end named by a word, and the word taken\n"
        '  strictly.'
    ),
    '4.1.19': (
        'SETTLED — कौरव्यमाण्डूकाभ्यां च, यथाक्रमं टाब्ङीपोरपवादः: an\n'
        '  exception to टाप् for the first and to ङीप् for the second,\n'
        '  taken in order. कौरव्यायणी, माण्डूकायनी.\n'
        '\n'
        'NOTE — कथं कौरवी सेना? तस्येदम् इति विवक्षायामणि कृते भविष्यति.\n'
        '  A form that looks like a counter-example is not one, because it\n'
        '  is a different derivation altogether.'
    ),
    '4.1.20': (
        'SETTLED — वयसि प्रथमे. कालकृतशरीरावस्था यौवनादिर्वयः — an age is\n'
        '  a state of the body made by time. कुमारी, किशोरी, बर्करी.\n'
        '  प्रथम इति किम्? स्थविरा, वृद्धा. अत इत्येव — शिशुः.\n'
        '\n'
        'SETTLED — the rule says *first* and is read as *not last*.\n'
        '  वयस्यचरम इति वक्तव्यम् widens it to any age but the last, which\n'
        '  brings in वधूटी and चिरण्टी, द्वितीयवयोवचनावेतौ. कथं कन्या?\n'
        '  कन्यायाः कनीन च इति ज्ञापकात् — from a later rule taking that\n'
        '  form for granted. And उत्तानशया, लोहितपादिका are not\n'
        '  counter-examples: नैता वयःश्रुतयः, they do not name an age.'
    ),
    '4.1.21': (
        'SETTLED — द्विगोः. पञ्चपूली, दशपूली. कथं त्रिफला? अजादिषु\n'
        "  दृश्यते — 4.1.4's list again, which is where this run keeps\n"
        '  sending what it cannot otherwise place.'
    ),
    '4.1.22': (
        'SETTLED — अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि. Where a\n'
        '  taddhita has been elided, a द्विगु takes no ङीप् unless it ends\n'
        '  in a measure: पञ्चाश्वा, दशाश्वा; द्विबिस्ता, द्व्याचिता,\n'
        '  द्विकम्बल्या. अपरिमाणेति किम्? द्व्याढकी. तद्धितलुकीति किम्?\n'
        '  पञ्चाश्वी in the collective sense.\n'
        '\n'
        'SETTLED — and what counts as a measure is stated negatively.\n'
        '  सर्वतो मानं परिमाणम्, but कालः संख्या च न परिमाणम् — a time and\n'
        '  a number are not measures, so द्विवर्षा and द्विशता fall under\n'
        '  the refusal too. The three named words are there because they\n'
        '  ARE measures and would otherwise have escaped it.'
    ),
    '4.1.23': (
        'SETTLED — काण्डान्तात्क्षेत्रे. A प्रतिषेध narrowed by a later\n'
        '  प्रतिषेध: काण्डशब्दस्यापरिमाणवाचित्वात् पूर्वेणैव प्रतिषेधे\n'
        '  सिद्धे क्षेत्रे नियमार्थं वचनम् — 4.1.22 had already refused\n'
        '  it, since काण्ड names no measure, and this restricts the\n'
        '  refusal to a FIELD. द्विकाण्डा क्षेत्रभक्तिः, but द्विकाण्डी\n'
        '  रज्जुः keeps its ङीप्.\n'
        '\n'
        'NOTE — प्रमाणविशेषः काण्डम् closes the circle: काण्ड is a\n'
        '  particular measure after all, which is why the earlier rule\n'
        '  needed narrowing rather than repeating.'
    ),
    '4.1.24': (
        'SETTLED — पुरुषात्प्रमाणेऽन्यतरस्याम्. अपरिमाणान्तत्वाद् नित्ये\n'
        '  प्रतिषेधे प्राप्ते विकल्पार्थं वचनम् — 4.1.22 refused it\n'
        '  outright and this makes the refusal optional: द्विपुरुषा beside\n'
        '  द्विपुरुषी. प्रमाण इति किम्? द्विपुरुषा, bought with two men.\n'
        '  तद्धितलुकीत्येव — द्विपुरुषी in the collective.\n'
        '\n'
        'NOTE — three sūtras in a row working on one refusal: 4.1.22\n'
        '  states it, 4.1.23 narrows it, 4.1.24 loosens it. Each is\n'
        '  stated of a different stem, and none repeats the others.'
    ),
    '4.1.25': (
        'SETTLED — बहुव्रीहेरूधसो ङीष्. घटोध्नी, कुण्डोध्नी. Stated\n'
        "  because 5.4.131's अनङ् turns the compound अन्-final, and then\n"
        "  4.1.12's refusal and 4.1.13's डाप् would both have reached it:\n"
        '  a rule needed only because ANOTHER rule changes the shape its\n'
        '  neighbours were watching for.\n'
        '\n'
        'SETTLED — बहुव्रीहेरिति किम्? प्राप्तोधाः. And समासान्तश्च\n'
        '  स्त्रियामेव — the compound-ending itself comes only in the\n'
        '  feminine, which is why महोधाः पर्जन्यः stands.\n'
        '\n'
        'NOTE — अन उपधालोपिनः इत्यस्यापि ङीपोऽयमुत्तरत्रानुवृत्तेर्\n'
        "  बाधक इष्यते: this ङीष् is meant to beat 4.1.28's ङीप् as well,\n"
        '  three sūtras ahead of it, by being carried down.'
    ),
    '4.1.26': (
        'SETTLED — संख्याव्ययादेर्ङीप्. पूर्वेण ङीषि प्राप्ते ङीब्\n'
        '  विधीयते — the rule before gave ङीष् and this gives ङीप्, and\n'
        '  THE TWO DIFFER ONLY IN ACCENT. द्व्यूध्नी, त्र्यूध्नी;\n'
        '  अत्यूध्नी, निरूध्नी. A whole sūtra spent on where the pitch\n'
        '  falls.\n'
        '\n'
        'NOTE — आदिग्रहणं किम्? द्विविधोध्नी, त्रिविधोध्नी — so that a\n'
        '  compound merely BEGINNING with a numeral is reached, not one\n'
        '  whose first member is the numeral itself.'
    ),
    '4.1.27': (
        'SETTLED — दामहायनान्ताच्च. द्विदाम्नी, त्रिदाम्नी; द्विहायनी,\n'
        '  त्रिहायणी, चतुर्हायणी.\n'
        '\n'
        'SETTLED — HALF A CONDITION CARRIES DOWN AND HALF STOPS.\n'
        '  संख्याग्रहणमनुवर्तते, नाव्ययग्रहणम् — 4.1.26 named a numeral\n'
        '  OR an indeclinable, and only the numeral continues. Anuvṛtti\n'
        '  is usually all-or-nothing from a given rule; here one word of\n'
        '  two runs on.\n'
        '\n'
        'NOTE — हायनो वयसि स्मृतः, so द्विहायना शाला is outside it: a\n'
        '  year of a building is not an age. णत्वमपि त्रिचतुर्भ्यां\n'
        '  हायनस्येति वयस्येव स्मर्यते (महाभाष्य २.२१३) — even the ण of\n'
        '  त्रिहायणी is held to the same sense.'
    ),
    '4.1.28': (
        'SETTLED — अन उपधालोपिनोऽन्यतरस्याम्. From an अन्-final bahuvrīhi\n'
        '  that drops its penultimate: बहुराजा, बहुराज्ञी, बहुराजे —\n'
        '  THREE forms, because ङीपा मुक्ते डाप्प्रतिषेधौ भवतः, and where\n'
        '  this option is declined 4.1.12 and 4.1.13 take over between\n'
        '  them.\n'
        '\n'
        'SETTLED — and the rule exists for what it keeps out.\n'
        '  किमर्थं तर्हीदमुच्यते, ननु सिद्धा एव डाप्प्रतिषेधङीपः?\n'
        '  अनुपधालोपिनो ङीप्प्रतिषेधार्थं वचनम् — everything it grants\n'
        '  was available anyway; what it adds is that a stem which does\n'
        '  NOT drop gets no ङीप् at all: सुपर्वा, सुपर्वे. A rule that\n'
        '  states an option in order to deny one elsewhere. अन इति किम्?\n'
        '  बहुमत्स्या.'
    ),
    '4.1.29': (
        'SETTLED — नित्यं संज्ञाछन्दसोः, विकल्पस्यापवादः. Where it is a\n'
        '  name or in the Veda the option closes: सुराज्ञी, अतिराज्ञी नाम\n'
        '  ग्रामः; गौः पञ्चदाम्नी, एकदाम्नी, द्विदाम्नी, एकमूर्ध्नी\n'
        '  (शौ०सं० ८.९.१५), समानमूर्ध्नी (तै०सं० ४.३.११.४).'
    ),
    '4.1.30': (
        'SETTLED — केवलमामकभागधेयपापापरसमानार्यकृतसुमङ्गलभेषजाच्च,\n'
        '  संज्ञाछन्दसोरित्येव. Nine words: केवली (पै०सं० १६.२०.१),\n'
        '  मामकी (पै०सं० ६.६.८), भागधेयीः (तै०सं० १.३.१२.१), पापी\n'
        '  (मै०सं० ४.२.१४), अपरीभ्यः (ऋ० १.३२.१३), समानी (ऋ० १०.१९१.३),\n'
        '  आर्यकृती (मै०सं० १.८.३), सुमङ्गली (ऋ० १०.८५.३३), भेषजी\n'
        '  (तै०सं० ४.५.१०.१).\n'
        '\n'
        'NOTE — a rule whose examples are ALL attested and whose\n'
        '  counter-examples are all ordinary speech: each citation is\n'
        '  followed by इति भाषायाम् giving the everyday form beside it.\n'
        '  The vṛtti is not illustrating a rule so much as licensing nine\n'
        '  readings it found.'
    ),
    '4.1.31': (
        'SETTLED — रात्रेश्चाजसौ. जस्विषयादन्यत्र — everywhere but before\n'
        '  the nominative plural: या रात्री सृष्टा, रात्रीभिः\n'
        '  (ऋ० १०.१०.९); but यास्ता रात्रयः. अजसादिष्विति वक्तव्यम् widens\n'
        '  the exclusion past जस् alone: रात्रिं सहोषित्वा.\n'
        '\n'
        'SETTLED — one word reached by two rules of this run, told apart\n'
        '  by which affix each gives. कथं तिमिरपटलैरवगुण्ठिताश्च रात्र्यः?\n'
        "  ङीषयं बह्वादिलक्षणः — that form is 4.1.45's ङीष् and not this\n"
        "  rule's ङीप्, by कृदिकारादक्तिनः (ग०सू० ४९). The refusal here is\n"
        '  of ङीप् only, so a different affix is free to come.'
    ),
    '4.1.32': (
        'SETTLED — अन्तर्वत्पतिवतोर्नुक्. प्रकृतिर्निपात्यते, नुगागमस्तु\n'
        '  विधीयते — the two words are FIXED and the augment is what is\n'
        '  actually given; the ङीप् follows of itself, स तु\n'
        '  नकारान्तत्वादेव सिद्धः, because they now end in न्.\n'
        '  अन्तर्वत्नी गर्भिणी, पतिवत्नी जीवपतिः.\n'
        '\n'
        'SETTLED — TWO WORDS FIXED FROM OPPOSITE ENDS, IN ONE RULE.\n'
        '  अन्तर्वदिति मतुब् निपात्यते, वत्वं सिद्धम्; पतिवदिति वत्वं\n'
        '  निपात्यते, मतुप् सिद्धः — in the first the affix is the\n'
        '  irregular part and the sound-change follows regularly; in the\n'
        '  second the sound-change is the irregular part and the affix\n'
        '  follows. The same निपातन covering two words whose\n'
        '  irregularities are in opposite halves.\n'
        '\n'
        'SETTLED — निपातनसामर्थ्यात् च विशेषे वृत्तिर्भवति: because they\n'
        '  are fixed at all, they hold only in the special sense —\n'
        '  गर्भभर्तृसंयोगे — and not for अन्तरस्यां शालायां विद्यते or\n'
        '  पतिमती पृथिवी. And the kārikā makes the augment optional in\n'
        '  the Veda: सान्तर्वत्नी (मै०सं० ४.२.९) beside सान्तर्वती\n'
        '  (काठ०सं० ८.१०), पतिवत्नी beside पतिवती.'
    ),
    '4.1.33': (
        'SETTLED — पत्युर्नो यज्ञसंयोगे. पति becomes पत्न् where a\n'
        '  sacrifice is in question, and ङीप् follows because the stem now\n'
        '  ends in न्: पत्नि वाचं यच्छ. तत्साधनत्वात् फलग्रहीतृत्वाद् वा\n'
        '  यजमानस्य पत्नी — she is so called either as an instrument of\n'
        '  the rite or as a taker of its fruit, and the vṛtti offers both\n'
        '  without choosing.\n'
        '\n'
        'NOTE — यज्ञसंयोग इति किम्? ग्रामस्य पतिरियं ब्राह्मणी. कथं\n'
        '  वृषलस्य पत्नी? उपमानाद् भविष्यति — by likeness to the\n'
        "  sacrificer's wife, which is how a rule about ritual reaches\n"
        '  ordinary speech.'
    ),
    '4.1.34': (
        'SETTLED — विभाषा सपूर्वस्य. वृद्धपत्नी beside वृद्धपतिः,\n'
        '  स्थूलपत्नी beside स्थूलपतिः. अप्राप्तविभाषेयमयज्ञसंयोगत्वात् —\n'
        '  an option where the rule before gave nothing at all, since no\n'
        '  sacrifice is meant. सपूर्वस्येति किम्? पतिरियं ब्राह्मणी\n'
        '  ग्रामस्य.'
    ),
    '4.1.35': (
        'SETTLED — नित्यं सपत्न्यादिषु. समानः पतिरस्याः सपत्नी, एकपत्नी.\n'
        '  पूर्वेण विकल्पे प्राप्ते वचनम्, and नित्यग्रहणं विस्पष्टार्थम्\n'
        '  — the word *always* is there only for clarity, not because\n'
        '  anything would have gone wrong without it. Compare 3.4.99,\n'
        '  where the same word was the whole content of the rule.\n'
        '\n'
        'NOTE — समानादिष्विति वक्तव्ये समानस्य सभावार्थं वचनम्: the list\n'
        '  could have been called समानादि and is not, so that समान may\n'
        '  become स in its first member. A gaṇa named after its second\n'
        '  form rather than its first, to license the first.'
    ),
    '4.1.36': (
        'SETTLED — पूतक्रतोरै च. पूतक्रतायी — ऐ replaces the final and\n'
        '  ङीप् follows.\n'
        '\n'
        'SETTLED — त्रय एते योगाः पुंयोगप्रकरणे द्रष्टव्याः. This and the\n'
        '  next two are to be READ as belonging to the section on words\n'
        '  used of a woman because of a man, which does not begin until\n'
        '  4.1.48 — twelve sūtras ahead. यया हि पूताः क्रतवः पूतक्रतुः सा\n'
        '  भवति: she by whom the rites are purified would be पूतक्रतु in\n'
        '  her own right, and that is not what the rule is for. A group of\n'
        '  three rules placed here and belonging there.'
    ),
    '4.1.37': (
        'SETTLED — वृषाकप्यग्निकुसितकुसीदानामुदात्तः. The same ऐ, and\n'
        '  accented: वृषाकपायी, अग्नायी, कुसितायी, कुसीदायी. पुंयोग\n'
        '  इत्येव — वृषाकपिः स्त्री.\n'
        '\n'
        'SETTLED — a word in a rule stated for ONE member of its own\n'
        '  list. वृषाकपिशब्दो मध्योदात्त उदात्तत्वं प्रयोजयति;\n'
        '  अग्न्यादिषु पुनरन्तोदात्तेषु स्थानिवद्भावादेव सिद्धम् — the\n'
        '  other three are already end-accented, so the substitute takes\n'
        '  the accent by standing in their place, and only the first\n'
        '  needs it said.'
    ),
    '4.1.38': (
        'SETTLED — मनोरौ वा. मनायी (मै०सं० १.८.६), मनावी\n'
        '  (काठ०सं० ३०.१), and plain मनुः — THREE forms from one option.\n'
        '\n'
        'SETTLED — because the option covers a substitute it did not\n'
        '  supply. ऐ उदात्त इति वर्तते, and वाग्रहणेन द्वावपि\n'
        "  विकल्प्येते, तेन त्रैरूप्यं भवति: 4.1.37's ऐ is carried down,\n"
        '  this rule adds औ, and the single वा makes BOTH optional — so\n'
        '  a rule that names one substitute produces three readings.\n'
        '  मनुशब्द आद्युदात्तः.'
    ),
    '4.1.39': (
        'SETTLED — वर्णादनुदात्तात्तोपधात्तो नः. From a COLOUR-word,\n'
        '  unaccented at the end, with त for its penultimate: ङीप्\n'
        '  optionally and the त becoming न. एनी beside एता, श्येनी beside\n'
        '  श्येता, हरिणी beside हरिता.\n'
        '\n'
        'SETTLED — three conditions and a counter-example for each.\n'
        '  वर्णादिति किम्? प्रकृता, प्ररुता — front-accented by the\n'
        '  गतिस्वर and not colour-words. अनुदात्तादिति किम्? श्वेता,\n'
        '  end-accented घृतादित्वात्. तोपधादिति किम्? the next rule takes\n'
        '  those. Every accent cited is fixed by a rule of the\n'
        '  फिट्सूत्र — वर्णानां तणतिनितान्तानाम् (२.१०) — so the\n'
        '  condition is checkable against another text and not merely\n'
        '  asserted.\n'
        '\n'
        'NOTE — असितपलितयोः प्रतिषेधः takes two out, and छन्दसि\n'
        '  क्नमित्येके puts a third form in for the Veda: असिक्नी\n'
        '  (शौ०सं० १.२३.१), पलिक्नी (ऋ० ५.२.४). भाषायामपीष्यते then\n'
        '  brings that Vedic form into ordinary speech — a vārttika\n'
        '  licensing what a छन्दसि rule had confined.'
    ),
    '4.1.40': (
        'SETTLED — अन्यतो ङीष्, वेति निवृत्तम्. The same colour-words with\n'
        '  any penultimate BUT त, and no option: सारङ्गी, कल्माषी, शबली.\n'
        '  वर्णादित्येव — खट्वा. अनुदात्तादित्येव — कृष्णा, कपिला.\n'
        '\n'
        'SETTLED — स्वरे विशेषः, AND THAT IS THE WHOLE DIFFERENCE. ङीप्\n'
        '  and ङीष् both give ई; the two rules divide a distinction that\n'
        '  is inaudible except in pitch, and a sūtra is spent on each\n'
        '  side of it. The pair recurs at 4.1.25 against 4.1.26 and again\n'
        '  at 4.1.60, which is three times in one pāda.'
    ),
    '4.1.41': (
        "SETTLED — षिद्गौरादिभ्यश्च. From a षित्-marked stem — 3.1.145's\n"
        '  शिल्पिनि ष्वुन् gives नर्तकी, खनकी, रजकी — and from the गौरादि\n'
        '  list: गौरी, मत्सी.\n'
        '\n'
        'SETTLED — and the list ends by teaching that its own ground is\n'
        '  not invariable. मातामह and पितामह are in it, and\n'
        '  मातामहपितामहयोर्मातरि षिच् च would have given them the affix by\n'
        '  their षित्-ness alone: षित्त्वादेव सिद्धे ज्ञापनार्थं वचनम् —\n'
        '  अनित्यः षिल्लक्षणो ङीषिति. The redundancy is the teaching, the\n'
        "  same shape as 3.4.103's ङिद्वचनं ज्ञापनार्थम्, and the fruit\n"
        '  is दंष्ट्रा.'
    ),
    '4.1.42': (
        'SETTLED — जानपदकुण्डगोणस्थलभाजनागकालनीलकुशकामुककबरात्\n'
        '  वृत्त्यमत्रावपनाकृत्रिमाश्राणास्थौल्यवर्णानाच्छादनायोविकार-\n'
        '  मैथुनेच्छाकेशवेषेषु. ELEVEN WORDS AND ELEVEN SENSES, PAIRED\n'
        '  यथासंख्यम् — the longest such correspondence in the project.\n'
        '  जानपदी if a livelihood, जानपदान्या otherwise; कुण्डी if a\n'
        '  vessel, कुण्डान्या if not; and so through all eleven, each with\n'
        '  its counter-form beside it.\n'
        '\n'
        'SETTLED — the pairing decides not only WHETHER the affix comes\n'
        '  but WHICH RULE gives it. नागशब्दो गुणवचनः स्थौल्ये ङीषम्\n'
        '  उत्पादयति, अन्यत्र गुण एव टापम्; जातिवचनात् तु जातिलक्षणो\n'
        "  ङीषेव भवति — नागी in the sense of bulk is this rule's, नागी as\n"
        "  a class-name is 4.1.63's, and नागा as a quality is 4.1.4's.\n"
        '  One word, three rules, told apart by sense alone.\n'
        '\n'
        'NOTE — नीली is narrowed twice over: न च सर्वस्मिन्नाच्छादन\n'
        '  इष्यते, किं तर्हि? नीलादोषधौ प्राणिनि च — a plant or an animal,\n'
        '  and संज्ञायां वा for a name. The eleventh sense is not one\n'
        '  sense but a family.'
    ),
    '4.1.43': (
        'SETTLED — शोणात्प्राचाम्. शोणी beside शोणा वडवा. The fifth\n'
        '  attribution in the project and the third to the eastern\n'
        '  school, after 3.4.18 and 4.1.17.'
    ),
    '4.1.44': (
        'SETTLED — वोतो गुणवचनात्. From a QUALITY-word in उ, optionally:\n'
        '  पट्वी beside पटुः, मृद्वी beside मृदुः. उत इति किम्?\n'
        '  शुचिरियं ब्राह्मणी. गुणवचनादिति किम्? आखुः.\n'
        '\n'
        'SETTLED — A GRAMMATICAL CONDITION GIVEN A PHILOSOPHICAL\n'
        '  DEFINITION, because nothing in the form shows it.\n'
        '  गुणमुक्तवान् गुणवचनः, and then in verse: सत्त्वे निविशतेऽपैति\n'
        '  पृथग् जातिषु दृश्यते, आधेयश्चाक्रियाजश्च\n'
        '  सोऽसत्त्वप्रकृतिर्गुणः — it enters a substance and leaves it, is\n'
        '  seen apart\n'
        '  across classes, is borne rather than made by an act, and is\n'
        '  not itself a thing. Four marks, none of them visible in a\n'
        '  word. This is the first of three such definitions in the run;\n'
        '  4.1.54 defines स्वाङ्ग and 4.1.63 defines जाति the same way.\n'
        '\n'
        'NOTE — वसुशब्दाद् गुणवचनाद् ङीबाद्युदात्तार्थम् sends one word to\n'
        '  the OTHER affix for the accent: वस्वी. And\n'
        '  खरुसंयोगोपधात् प्रतिषेधो वक्तव्यः keeps खरु and पाण्डु out.'
    ),
    '4.1.45': (
        'SETTLED — बह्वादिभ्यश्च. बह्वी beside बहुः.\n'
        '\n'
        'SETTLED — a word put in a गण so that a LATER rule may point at\n'
        '  it. बहुशब्दो गुणवचन एव, तस्येह पाठ उत्तरार्थः — बहु is already\n'
        '  a quality-word and reached by 4.1.44, so its membership does\n'
        '  nothing here and everything for 4.1.46, which names the list.\n'
        "  The same move 3.4.111's एवकार made, and in the same direction.\n"
        '\n'
        'NOTE — the list carries two गणसूत्र of its own,\n'
        '  कृदिकारादक्तिनः (ग०सू० ४९) and सर्वतोऽक्तिन्नर्थादित्येके\n'
        '  (ग०सू० ५०), and those are what 4.1.31 sends रात्र्यः to when it\n'
        '  cannot account for the form itself.'
    ),
    '4.1.46': (
        'SETTLED — नित्यं छन्दसि. In the Veda the option closes: बह्वीषु\n'
        '  हित्वा प्रपिबन्, बह्वी नाम ओषधी.\n'
        '\n'
        'NOTE — नित्यग्रहणमुत्तरार्थम्, the word *always* is here for the\n'
        '  NEXT rule. That is the second time in two sūtras that\n'
        '  something is placed for what follows: 4.1.45 put a word in a\n'
        '  list for this rule, and this puts a word in the rule for\n'
        '  4.1.47.'
    ),
    '4.1.47': (
        'SETTLED — भुवश्च. विभ्वी (ऋ० ५.३८.१), प्रभ्वी (ऋ० १.१८८.५),\n'
        '  संभ्वी.\n'
        '\n'
        'SETTLED — इह कस्माद् न भवति स्वयम्भूः? उत इति तपरकरणम्\n'
        "  अनुवर्तते, ह्रस्वादेवेयं पञ्चमी — 4.1.44's त is still running\n"
        '  three sūtras later and holds this to the SHORT उ. A single\n'
        '  letter carried down and doing all the work of an exclusion.\n'
        '  भुव इति सौत्रो निर्देशः.'
    ),
    '4.1.48': (
        'SETTLED — पुंयोगादाख्यायाम्. पुंसा योगः पुंयोगः — from a stem\n'
        '  that stands for a woman BECAUSE OF a man and names him:\n'
        '  गणकस्य स्त्री गणकी, महामात्री, प्रष्ठी, प्रचरी.\n'
        '  पुंसि शब्दप्रवृत्तिनिमित्तस्य संभवात् पुंशब्दा एते, तद्योगात्\n'
        '  स्त्रियां वर्तन्ते.\n'
        '\n'
        "SETTLED — this is the section 4.1.36's vṛtti said three earlier\n"
        '  rules belonged to: त्रय एते योगाः पुंयोगप्रकरणे द्रष्टव्याः,\n'
        '  said twelve sūtras before the section begins. A group of\n'
        '  rules placed in one part of the text and read as belonging to\n'
        '  another.\n'
        '\n'
        'SETTLED — आख्याग्रहणं किम्? परिसृष्टा, प्रजाता —\n'
        '  पुंयोगादेते शब्दाः स्त्रियां वर्तन्ते, न तु पुमांसमाचक्षते.\n'
        '  Those are used of a woman on account of a man and do not NAME\n'
        '  him, and naming him is the whole work of आख्यायाम्.\n'
        '  पुंयोगादिति किम्? देवदत्ता, यज्ञदत्ता.\n'
        '\n'
        'NOTE — गोपालिकादीनां प्रतिषेधः, and सूर्याद् देवतायां चाब्\n'
        '  वक्तव्यः: सूर्या as a DEITY, सूरी otherwise — the same word\n'
        '  taking two affixes by what it denotes.'
    ),
    '4.1.49': (
        'SETTLED — इन्द्रवरुणभवशर्वरुद्रमृडहिमारण्ययवयवनमातुलाचार्याणाम्\n'
        '  आनुक्. Twelve words with the augment: इन्द्राणी, वरुणानी,\n'
        '  भवानी, शर्वाणी, रुद्राणी, मृडानी.\n'
        '\n'
        'SETTLED — ONE LIST, TWO CONTENTS. येषामत्र पुंयोग एवेष्यते,\n'
        '  तेषामानुगागममात्रं विधीयते, प्रत्ययस्तु पूर्वेणैव सिद्धः;\n'
        '  अन्येषां तूभयं विधीयते — for the members where a man is really\n'
        '  in question the affix came from 4.1.48 already and only the\n'
        '  augment is new; for the rest both are given here. The rule\n'
        '  gives different amounts to different members of its own list.\n'
        '\n'
        'SETTLED — and each vārttika states a SENSE, not just a word.\n'
        '  हिमारण्ययोर्महत्त्वे — हिमानी and अरण्यानी for GREATNESS;\n'
        '  यवाद् दोषे — यवानी for a spoilt grain; यवनाल्लिप्याम् —\n'
        '  यवनानी for a SCRIPT. And अर्यक्षत्रियाभ्यां वा is expressly\n'
        '  NOT about a man: विना पुंयोगेन स्वार्थ एवायं विधिः, पुंयोगे तु\n'
        '  ङीषैव भवितव्यम् — अर्याणी in its own sense, अर्यी of a wife.\n'
        '  A rule of the पुंयोग section with a member outside it.'
    ),
    '4.1.50': (
        'SETTLED — क्रीतात्करणपूर्वात्. करणं पूर्वमस्मिन्निति करणपूर्वं\n'
        '  प्रातिपदिकम् — where what precedes names the MEANS:\n'
        '  वस्त्रक्रीती, वसनक्रीती. करणपूर्वादिति किम्? सुक्रीता,\n'
        '  दुष्क्रीता.\n'
        '\n'
        'SETTLED — a form saved by the ORDER in which its compound was\n'
        '  made. इह कस्माद् न भवति सा हि तस्य धनक्रीता? टाबन्तेन समासः —\n'
        '  the compound there is made with a word that ALREADY has टाप्,\n'
        '  so this rule has nothing left to add. गतिकारकोपपदानां कृद्भिः\n'
        '  सह समासवचनं प्राक् सुबुत्पत्तेः is invoked as बहुलम्, by\n'
        "  2.1.32's कर्तृकरणे कृता बहुलम्."
    ),
    '4.1.51': (
        'SETTLED — क्तादल्पाख्यायाम्. अल्पाख्यायामिति समुदायोपाधिः —\n'
        '  the smallness qualifies the WHOLE compound and not either\n'
        '  member: अभ्रविलिप्ती द्यौः, सूपविलिप्ती पात्री,\n'
        '  अल्पसूपेत्यर्थः. अल्पाख्यायामिति किम्? चन्दनानुलिप्ता ब्राह्मणी.'
    ),
    '4.1.52': (
        'SETTLED — बहुव्रीहेश्चान्तोदात्तात्. शङ्खभिन्नी, ऊरुभिन्नी,\n'
        '  गलोत्कृत्ती, केशलूनी. बहुव्रीहेरिति किम्? पादपतिता.\n'
        '\n'
        'SETTLED — and four vārttikas cut it back from four directions.\n'
        '  अन्तोदात्ताज् जातप्रतिषेधः keeps दन्तजाता and स्तनजाता out;\n'
        '  अबहुनञ्सुकालसुखादिपूर्वात् keeps out बहुकृता, अकृता, सुकृता,\n'
        '  मासजाता, सुखजाता; and पाणिगृहीत्यादीनामर्थविशेषे makes the\n'
        '  affix mark a SENSE rather than a form — पाणिगृहीती is a wife,\n'
        '  यस्यास्तु कथंचित् पाणिर्गृह्यते पाणिगृहीता सा भवति.'
    ),
    '4.1.53': (
        'SETTLED — अस्वाङ्गपूर्वपदाद्वा, पूर्वेण नित्ये प्राप्ते विकल्प\n'
        '  उच्यते. Where the first member is NOT a body part the last\n'
        "  rule's affix becomes optional: शार्ङ्गजग्धी beside\n"
        '  शार्ङ्गजग्धा, पलाण्डुभक्षिती, सुरापीती. अस्वाङ्गपूर्वपदादिति\n'
        '  किम्? शङ्खभिन्नी. अन्तोदात्तादित्येव — वस्त्रच्छन्ना.'
    ),
    '4.1.54': (
        'SETTLED — स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्. From a BODY PART\n'
        '  that is the subordinate member and has no conjunct for its\n'
        '  penultimate, optionally: चन्द्रमुखी beside चन्द्रमुखा,\n'
        '  अतिकेशी beside अतिकेशा माला. स्वाङ्गादिति किम्? बहुयवा.\n'
        '  उपसर्जनादिति किम्? अशिखा. असंयोगोपधादिति किम्? सुगुल्फा,\n'
        '  सुपार्श्वा.\n'
        '\n'
        'SETTLED — and स्वाङ्ग is DEFINED IN VERSE, the second of three\n'
        '  such definitions in this run. अद्रवं मूर्तिमत् स्वाङ्गं\n'
        '  प्राणिस्थमविकारजम्, अतत्स्थं तत्र दृष्टं चेत् तस्य चेत्\n'
        '  तत्तथायुतम् — not liquid, having shape, situated in a living\n'
        '  thing, not produced by change; and a thing NOT so situated\n'
        '  counts if it is seen there and belongs there. Four conditions\n'
        '  and two extensions, for one word of one rule, and none of it\n'
        '  readable off the form.\n'
        '\n'
        'NOTE — अङ्गगात्रकण्ठेभ्य इति वक्तव्यम् adds three more:\n'
        '  मृद्वङ्गी, सुगात्री, स्निग्धकण्ठी.'
    ),
    '4.1.55': (
        'SETTLED — नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च. Seven body-parts\n'
        '  named because the rule before could not reach them —\n'
        '  बह्वज्लक्षणे संयोगोपधलक्षणे च प्रतिषेधे प्राप्ते वचनम्:\n'
        '  तुङ्गनासिकी, तिलोदरी, बिम्बोष्ठी, दीर्घजङ्घी, समदन्ती,\n'
        '  चारुकर्णी, तीक्ष्णशृङ्गी.\n'
        '\n'
        'SETTLED — but it lifts two exclusions and leaves a third\n'
        '  standing: सहनञ्विद्यमानपूर्वलक्षणस्तु प्रतिषेधो भवत्येव, so\n'
        '  4.1.57 still refuses these. A rule stated against two\n'
        '  प्रतिषेध and silent about the third, and the silence is read\n'
        '  as leaving it in force.\n'
        '\n'
        'NOTE — पुच्छाच्चेति वक्तव्यम् adds an eighth;\n'
        '  कबरमणिविषशरेभ्यो नित्यम् closes the option after four words;\n'
        '  and उपमानात् पक्षात् च पुच्छात् च reaches उलूकपक्षी सेना and\n'
        '  उलूकपुच्छी शाला, where the body-part is a COMPARISON and the\n'
        '  thing named is an army or a hall.'
    ),
    '4.1.56': (
        'SETTLED — न क्रोडादिबह्वचः. क्रोडादिराकृतिगणः — AN OPEN LIST,\n'
        '  whose members are recognised by their shape rather than\n'
        '  enumerated: कल्याणक्रोडा, कल्याणखुरा, कल्याणोखा, कल्याणबाला,\n'
        '  कल्याणशफा, कल्याणगुदा, कल्याणघोणा, सुभगा, सुगला. And from a\n'
        '  stem of MANY VOWELS: पृथुजघना, महाललाटा — a condition of\n'
        '  length, the only one in this run.\n'
        '\n'
        'NOTE — this is the rule that made the resolver ask the right\n'
        "  question. It states ONE condition against 4.1.54's two, so on\n"
        '  specificity the rule being excepted beat the exception. An\n'
        '  अपवाद is narrower by BEING one, not by counting its words.'
    ),
    '4.1.57': (
        'SETTLED — सहनञ्विद्यमानपूर्वाच्च. Where सह, the negative नञ् or\n'
        '  विद्यमान stands first: सकेशा, अकेशा, विद्यमानकेशा; सनासिका,\n'
        '  अनासिका, विद्यमाननासिका. It refuses both 4.1.54 and 4.1.55,\n'
        "  and 4.1.55's own vṛtti says so from the other side."
    ),
    '4.1.58': (
        'SETTLED — नखमुखात्संज्ञायाम्. Where the compound is a NAME:\n'
        '  शूर्पणखा, वज्रणखा, गौरमुखा, कालमुखा. संज्ञायामिति किम्?\n'
        '  ताम्रनखी कन्या, चन्द्रमुखी.'
    ),
    '4.1.59': (
        'SETTLED — दीर्घजिह्वी च छन्दसि. निपात्यते, and what the fixing\n'
        '  supplies is an affix 4.1.54 could NOT give:\n'
        '  संयोगोपधत्वादप्राप्तो ङीष् विधीयते, the penultimate being a\n'
        '  conjunct. दीर्घजिह्वी वै देवानां हव्यमवालेट् (मै०सं० ३.१०.६).\n'
        '\n'
        'NOTE — चकारः संज्ञानुकर्षणार्थः pulls the संज्ञा of 4.1.58 down,\n'
        '  and निपातनं नित्यार्थम् closes the option in the same breath.\n'
        '  A one-word rule doing three things.'
    ),
    '4.1.60': (
        'SETTLED — दिक्पूर्वपदान्ङीप्. Where a DIRECTION stands first,\n'
        '  ङीप् and not ङीष् — स्वरे विशेषः, the two differ only in\n'
        '  accent for the third time in this pāda: प्राङ्मुखी,\n'
        '  प्राङ्नासिकी.\n'
        '\n'
        'SETTLED — AND IT LOOKS BACK OVER A WHOLE SECTION, GIVING AND\n'
        '  REFUSING ALIKE. स्वाङ्गाच्चोपसर्जनाद् इत्येवमादिविधिप्रतिषेध-\n'
        '  विषयः सर्वोऽप्यपेक्ष्यते, यत्र ङीष् विहितस्तत्र तदपवादः — it\n'
        '  excepts 4.1.54 to 4.1.59 wherever ङीष् was GIVEN, and where\n'
        '  the section refused there is nothing for it to except: इह न\n'
        '  भवति प्राग्गुल्फा, प्राक्क्रोडा, प्राग्जघना.\n'
        '\n'
        'NOTE — the table states what the rule states, that a direction\n'
        '  in front gives ङीप्. The further condition — that a ङीष् must\n'
        '  actually have been reached — is on record here rather than in\n'
        "  the row, because it is a condition on the SECTION'S OUTPUT and\n"
        '  not on the stem, and no other rule of this run has that shape.'
    ),
    '4.1.61': (
        'SETTLED — वाहः. ङीषेव स्वर्यते, न ङीप् — the ACCENT of the rule\n'
        '  itself is what shows which of the two affixes is meant, since\n'
        '  the sūtra names neither. दित्यौही (तै०सं० ४.७.१०.१),\n'
        '  प्रष्ठौही.\n'
        '\n'
        'SETTLED — वहेरयं ण्विप्रत्ययान्तस्य निर्देशः, सामर्थ्यात्\n'
        '  तदन्तविधेर्विज्ञानम्: the word named is वह् with ण्वि, and\n'
        '  that it reaches a compound through its last member is read off\n'
        "  the fact that a bare one would have no use — the rule's\n"
        '  capacity, again, standing in for a condition it does not state.'
    ),
    '4.1.62': (
        'SETTLED — सख्यशिश्वी इति भाषायाम्. Two words fixed with ङीष्,\n'
        '  and ONLY in ordinary speech: सखीयं मे ब्राह्मणी; नास्याः\n'
        '  शिशुरस्तीति अशिश्वी. भाषायामिति किम्? सखा सप्तपदी भव\n'
        '  (आ०गृ० १.७.१९).\n'
        '\n'
        'SETTLED — THE REVERSE OF EVERY छन्दसि RULE IN THIS RUN. Those\n'
        '  license a Vedic form beside an ordinary one; this licenses an\n'
        '  ordinary form and leaves the Veda alone. 4.1.46, 4.1.47,\n'
        '  4.1.59 and 4.1.71 all run the other way, and this is the only\n'
        '  one of its kind here.'
    ),
    '4.1.63': (
        'SETTLED — जातेरस्त्रीविषयादयोपधात्. From a CLASS-word not\n'
        '  confined to the feminine and without य for its penultimate:\n'
        '  कुक्कुटी, सूकरी, ब्राह्मणी, वृषली, नाडायनी, चारायणी, कठी,\n'
        '  बह्वृची. जातेरिति किम्? मुण्डा. अस्त्रीविषयादिति किम्?\n'
        '  मक्षिका. अयोपधादिति किम्? क्षत्रिया.\n'
        '\n'
        'SETTLED — जाति DEFINED IN VERSE, the third such definition in\n'
        '  the run. आकृतिग्रहणा जातिर्लिङ्गानां च न सर्वभाक्,\n'
        '  सकृदाख्यातनिर्ग्राह्या गोत्रं च चरणैः सह — grasped by form,\n'
        '  not sharing in all genders, seized by being named once, and\n'
        "  taking in lineage along with the schools. Three of this run's\n"
        '  conditions — गुणवचन at 4.1.44, स्वाङ्ग at 4.1.54 and जाति here\n'
        '  — are defined in verse and none in a sūtra, because none of\n'
        '  them is visible in the word.\n'
        '\n'
        'NOTE — योपधप्रतिषेधे हयगवयमुकयमत्स्यमनुष्याणामप्रतिषेधः puts\n'
        '  five back: हयी, गवयी, मुकयी, मत्सी, मनुषी.'
    ),
    '4.1.64': (
        'SETTLED — पाककर्णपर्णपुष्पफलमूलवालोत्तरपदाच्च. Seven final\n'
        '  members, stated because the rule before could not reach them:\n'
        '  स्त्रीविषयत्वादेतेषां पूर्वेणाप्राप्तः प्रत्ययो विधीयते.\n'
        '  ओदनपाकी, शङ्कुकर्णी, शालपर्णी, शङ्खपुष्पी, दासीफली, दर्भमूली,\n'
        '  गोबाली.\n'
        '\n'
        'NOTE — पुष्पफलमूलोत्तरपदात् तु यतो नेष्यते तदजादिषु पठ्यते.\n'
        "  Whatever is not wanted goes into 4.1.4's list, which is the\n"
        "  second rule of the pāda to say so — after 4.1.21's कथं\n"
        '  त्रिफला? अजादिषु दृश्यते. A list that is a residue, and two\n'
        '  rules naming it as one.'
    ),
    '4.1.65': (
        'SETTLED — इतो मनुष्यजातेः. From an इ-final word naming a HUMAN\n'
        '  class: अवन्ती, कुन्ती, दाक्षी, प्लाक्षी. इत इति किम्? विट्,\n'
        '  दरत्. मनुष्यग्रहणं किम्? तित्तिरिः.\n'
        '\n'
        'SETTLED — a word repeated to lift ONE of three conditions.\n'
        '  जातेरिति वर्तमाने पुनर्जातिग्रहणं योपधादपि यथा स्यात् — जाति\n'
        '  is already carried down from 4.1.63, and saying it again\n'
        '  releases the अयोपध of that rule while leaving the rest: hence\n'
        "  औदमेयी. Anuvṛtti carries a rule's conditions as a bundle, and\n"
        '  restating one word is how a single condition is untied.\n'
        '\n'
        'NOTE — इञ उपसंख्यानमजात्यर्थम् adds सौतङ्गमी, मौनिचित्ती, where\n'
        '  the इञ् of 4.2.80 makes no class at all.'
    ),
    '4.1.66': (
        'SETTLED — ऊङुतः. From a उ-final word naming a human class, a\n'
        '  DIFFERENT affix: कुरूः, ब्रह्मबन्धूः, वीरबन्धूः.\n'
        '  ङकारो नोङ्धात्वोः इति विशेषणार्थः, दीर्घोच्चारणं कपो\n'
        '  बाधनार्थम् — the ङ् so that 6.1.175 can pick it out, the long\n'
        '  ऊ so that कप् is beaten. अयोपधादित्येतदत्रापेक्ष्यते —\n'
        '  अध्वर्युर्ब्राह्मणी.\n'
        '\n'
        'NOTE — अप्राणिजातेश्चारज्ज्वादीनाम् extends it past the human:\n'
        '  अलाबूः, कर्कन्धूः. अप्राणिग्रहणं किम्? कृकवाकुः.\n'
        '  अरज्ज्वादीनामिति किम्? रज्जुः, हनुः.'
    ),
    '4.1.67': (
        'SETTLED — बाह्वन्तात्संज्ञायाम्. भद्रबाहूः, जालबाहूः.\n'
        '  संज्ञायामिति किम्? वृत्तौ बाहू अस्याः वृत्तबाहुः.'
    ),
    '4.1.68': (
        'SETTLED — पङ्गोश्च. पङ्गूः. And श्वशुरस्योकाराकारयोर्लोपश्च\n'
        '  वक्तव्यः adds श्वश्रूः, where the affix arrives with two\n'
        '  elisions the sūtra does not mention.'
    ),
    '4.1.69': (
        'SETTLED — ऊरूत्तरपदादौपम्ये. Where a COMPARISON is meant:\n'
        '  कदलीस्तम्भोरूः, नागनासोरूः, करभोरूः. औपम्य इति किम्?\n'
        '  वृत्तोरुः स्त्री.'
    ),
    '4.1.70': (
        'SETTLED — संहितशफलक्षणवामादेश्च, अनौपम्यार्थ आरम्भः — begun for\n'
        '  the case where NO comparison is meant, which is exactly what\n'
        '  the rule before required: संहितोरूः, शफोरूः, लक्षणोरूः,\n'
        '  वामोरूः. सहितसहाभ्यां चेति वक्तव्यम् adds two more.\n'
        '\n'
        "NOTE — a rule stated to cover the complement of its neighbour's\n"
        "  condition, which is the same shape as 4.1.40's अन्यतः against\n"
        '  4.1.39 thirty sūtras earlier.'
    ),
    '4.1.71': (
        'SETTLED — कद्रुकमण्डल्वोश्छन्दसि. कद्रूश्च वै सुपर्णी च\n'
        '  (तै०सं० ६.१.६.१); मा स्म कमण्डलूं शूद्राय दद्यात्. छन्दसीति\n'
        '  किम्? कद्रुः, कमण्डलुः.\n'
        '\n'
        'NOTE — गुग्गुलुमधुजतुपतयालूनामिति वक्तव्यम् adds four, each\n'
        '  cited: गुग्गुलूः (शौ०सं० ४.३७.३), मधूः (शौ०सं० ७.५६.२),\n'
        '  जतूः (मै०सं० ३.१४.६), पतयालूः (शौ०सं० ७.११५.२).'
    ),
    '4.1.72': (
        'SETTLED — संज्ञायाम्, अच्छन्दोऽर्थं वचनम्. The same two words\n'
        '  outside the Veda, where they are NAMES: कद्रूः, कमण्डलूः.\n'
        '  संज्ञायामिति किम्? कद्रुः, कमण्डलुः.\n'
        '\n'
        'NOTE — two adjacent rules for two words, one for the Veda and\n'
        '  one for ordinary speech, and the difference between them is\n'
        '  the entire content of the second.'
    ),
    '4.1.73': (
        'SETTLED — शार्ङ्गरवाद्यञो ङीन्. शार्ङ्गरवी, कापटवी; बैदी,\n'
        '  और्वी. The sixth of the eight feminine affixes to be given,\n'
        "  and it had been in 4.1.1's class-word since the pāda began\n"
        '  with nothing supplying it.\n'
        '\n'
        'SETTLED — A RULE BEATEN OR NOT ACCORDING TO WHICH WORD OF IT IS\n'
        '  STILL RUNNING. जातिग्रहणं चेहानुवर्तते, तेन जातिलक्षणो ङीषनेन\n'
        "  बाध्यते, न पुंयोगलक्षणः — 4.1.63's ङीष् is beaten and 4.1.48's\n"
        '  is not, because only the first is stated with the word जाति,\n'
        '  which is what carries down to here. बैदस्य स्त्री बैदी stands\n'
        '  by that other rule.\n'
        '\n'
        'SETTLED — and this is the SECOND naming of अञ्. 4.1.15 named it\n'
        "  too, and that rule's own vṛtti said why the naming would be\n"
        "  repeated: पुनरञो ग्रहणं जातिलक्षणं ङीषं बाधितुम् — 4.1.15's\n"
        "  ङीप् could not beat 4.1.63 and this rule's ङीन् can. A\n"
        '  forward reference made fifty-eight sūtras before its object.'
    ),
    '4.1.74': (
        'SETTLED — यङश्चाप्. ञ्यङः ष्यङश्च सामान्यग्रहणमेतत् — यङ् is a\n'
        '  class-word for two affixes: आम्बष्ठ्या, सौवीर्या, कौसल्या from\n'
        '  the first; कारीषगन्ध्या, वाराह्या, बालाक्या from the second.\n'
        '  The last of the eight affixes to be given, which closes the\n'
        "  debt 4.1.1's class-words opened.\n"
        '\n'
        'NOTE — षाच्च यञः extends it to a यञ् standing after ष:\n'
        '  शार्कराक्ष्या, पौतिमाष्या, गौकक्ष्या.'
    ),
    '4.1.75': (
        'SETTLED — आवट्याच्च. अवटशब्दो गर्गादिः, तस्माद् यञि कृते ङीपि\n'
        '  प्राप्ते वचनमेतत् — 4.1.16 would have given ङीप्, and this\n'
        '  gives चाप्: आवट्या.\n'
        '\n'
        'SETTLED — AND IT IS BEATEN IN TURN, BY A RULE FIFTY-EIGHT\n'
        '  SŪTRAS BACK. प्राचां ष्फ एव, सर्वत्रग्रहणात् — आवट्यायनी.\n'
        "  That is what 4.1.18's सर्वत्र was pulled backward into 4.1.17\n"
        '  to do, बाधकबाधनार्थम्, and this is the rule it was pulled back\n'
        '  to beat. The transaction is now closed at both ends, and both\n'
        '  ends are in the commentary: 4.1.18 says which way the word\n'
        '  travels and 4.1.75 says what it arrives to do.'
    ),
    '4.1.76': (
        'SETTLED — तद्धिताः, अधिकारोऽयम्. आ पञ्चमाध्यायपरिसमाप्तेर्यानित\n'
        '  ऊर्ध्वमनुक्रमिष्यामः, तद्धितसंज्ञास्ते वेदितव्याः — the SAME\n'
        '  range 4.1.1 governs, and the two make a pair: one says what\n'
        '  the affixes attach TO and this says what they are CALLED.\n'
        '\n'
        'SETTLED — the plural is doing work.\n'
        '  बहुवचनमनुक्ततद्धितपरिग्रहार्थम्: the name is given in the\n'
        '  plural so that affixes NOT stated in these two chapters are\n'
        '  taken in as well — पृथिव्या ञाञौ (वा० ४.१.८५) and\n'
        '  अग्रादिपश्चाड्डिमच् (वा० ४.३.२३) become तद्धित though no sūtra\n'
        '  gives them. A grammatical number read as a scope.\n'
        '\n'
        'NOTE — तद्धितप्रदेशाः: कृत्तद्धितसमासाश्च इत्येवमादयः. 1.2.46 is\n'
        '  the first place the name is used, and it is what makes a\n'
        '  taddhita-formed word a प्रातिपदिक — so 4.1.1 can govern the\n'
        '  next affix after it. The two headings feed each other.'
    ),
    '4.1.77': (
        'SETTLED — यूनस्तिः, ङीपोऽपवादः. युवतिः.\n'
        '\n'
        'SETTLED — and स च तद्धितसंज्ञो भवति: the affix is a TADDHITA.\n'
        '  This is the first feminine affix of the pāda given from under\n'
        "  4.1.76 instead of 4.1.3, and 4.1.76's own vṛtti names it as\n"
        '  the first thing that heading will govern — वक्ष्यति यूनस्तिः.\n'
        '  The feminine is marked by two kinds of affix under two\n'
        '  headings, and the code keeps the two inventories apart.'
    ),
    '4.1.78': (
        'SETTLED — अणिञोरनार्षयोर्गुरूपोत्तमयोः ष्यङ् गोत्रे. Where a\n'
        '  गोत्र affix अण् or इञ् stands on a stem with a heavy\n'
        '  next-to-last syllable, ष्यङ् replaces it in the feminine:\n'
        '  कारीषगन्ध्या, कौमुदगन्ध्या, वाराह्या, बालाक्या.\n'
        '\n'
        'SETTLED — it replaces the AFFIX and not the word.\n'
        '  निर्दिश्यमानस्यादेशा भवन्ति इत्यणिञोरेव विज्ञायते, न तु\n'
        '  समुदायस्य: a substitute stands for what the rule NAMES, and\n'
        '  what this rule names is the two affixes.\n'
        '\n'
        'SETTLED — गुरूपोत्तम defined in two steps. उत्तमशब्दः\n'
        '  स्वभावात् त्रिप्रभृतीनामन्त्यमक्षरमाह, उत्तमस्य समीपम्\n'
        '  उपोत्तमम् — *last* means the last syllable of a word of THREE\n'
        '  OR MORE, and *near the last* the one before it. The first step\n'
        '  is what keeps a word of two out.\n'
        '\n'
        'SETTLED — four words and a counter-example for each. अणिञोरिति\n'
        '  किम्? आर्तभागी, whose affix is अञ् by बिदादि —\n'
        "  गुरूपोत्तमादिकं सर्वमस्तीति, न त्वणिञौ, so 4.1.15's ङीप्\n"
        '  comes. अनार्षयोरिति किम्? वासिष्ठी, वैश्वामित्री.\n'
        '  गुरूपोत्तमयोरिति किम्? औपगवी, कापटवी. गोत्र इति किम्?\n'
        '  आहिच्छत्री, कान्यकुब्जी.\n'
        '\n'
        'SETTLED — AN AFFIX CONSUMED FOUR SŪTRAS BEFORE IT IS GIVEN.\n'
        '  ङकारः सामान्यग्रहणार्थः, षकारस्तदविघातार्थः — the ङ् so that\n'
        "  4.1.74's class-word यङ् reaches it, the ष् so that being\n"
        '  reached as a class does not spoil it. 4.1.74 यङश्चाप् reads\n'
        '  यङ् as covering ञ्यङ् and ष्यङ्, and ष्यङ् is made HERE.\n'
        '  कारीषगन्ध्या is the example on both sides.'
    ),
    '4.1.79': (
        'SETTLED — गोत्रावयवात्. गोत्रावयवा गोत्राभिमताः कुलाख्याः\n'
        '  पुणिकभुणिकमुखरप्रभृतयः — family names taken as PARTS of a\n'
        '  lineage: पौणिक्या, भौणिक्या, मौखर्या. अगुरूपोत्तमार्थ आरम्भः,\n'
        '  begun for the case the rule before could not reach.\n'
        '\n'
        'NOTE — येषां त्वनन्तरापत्येऽपीष्यते दैवदत्या याज्ञदत्येति, ते\n'
        '  क्रौड्यादिषु द्रष्टव्याः: what this rule cannot hold goes into\n'
        "  the next one's list. The third time in this pāda that a गण is\n"
        '  used as somewhere to put what a rule will not take, after\n'
        '  4.1.21 and 4.1.64 both sent theirs to अजादि.'
    ),
    '4.1.80': (
        'SETTLED — क्रौड्यादिभ्यश्च. क्रौड्या, लाड्या.\n'
        '\n'
        'SETTLED — अगुरूपोत्तमार्थ आरम्भः, अनणिञर्थश्च: begun for BOTH\n'
        '  the conditions 4.1.78 stated and this list escapes — neither a\n'
        '  heavy penultimate nor the two named affixes. One list lifting\n'
        '  two conditions at once, where the rule before it lifted only\n'
        '  the first.'
    ),
    '4.1.81': (
        'SETTLED — दैवयज्ञिशौचिवृक्षिसात्यमुग्रिकाण्ठेविद्धिभ्योऽन्यतरस्याम्.\n'
        '  दैवयज्ञ्या beside दैवयज्ञी, शौचिवृक्ष्या beside शौचिवृक्षी.\n'
        '\n'
        'SETTLED — ONE OPTION DOING TWO DIFFERENT THINGS. इञन्ता एते,\n'
        '  गोत्रग्रहणं च नानुवर्तते, तेनोभयत्रविभाषेयम् — the word गोत्र\n'
        '  does NOT carry down here, so the rule covers two grounds and\n'
        '  the option means something different on each. गोत्रे पूर्वेण\n'
        '  नित्यः ष्यङादेशः प्राप्तो विकल्प्यते — in the lineage-sense it\n'
        '  LOOSENS what 4.1.78 made obligatory; अगोत्रे त्वनन्तरेऽपत्ये\n'
        '  पक्षे विधीयते — of an immediate descendant it GIVES what\n'
        '  nothing had given. And where it is declined, तेन मुक्ते इतो\n'
        '  मनुष्यजातेः इति ङीषेव भवति: 4.1.65 takes over.\n'
        '\n'
        'NOTE — a word failing to carry down is what makes the double\n'
        '  reading possible. 4.1.27 had half a condition carry and half\n'
        '  stop; here a whole word stops, and the rule widens rather than\n'
        '  narrows.'
    ),
    '4.1.82': (
        'SETTLED — समर्थानां प्रथमाद्वा. त्रयमप्यधिक्रियते समर्थानामिति\n'
        '  च, प्रथमादिति च, वेति च — THREE WORDS AND EACH GOVERNS\n'
        '  SEPARATELY, so one sūtra does the work of three headings.\n'
        '  उपगोरपत्यम् — औपगवः.\n'
        '\n'
        'SETTLED — and what each buys is shown by what goes wrong\n'
        '  without it. समर्थानामिति किम्? कम्बल उपगोः, अपत्यं\n'
        '  देवदत्तस्य — words in one sentence that do not go together,\n'
        '  and without this the affix would cross between them.\n'
        '  प्रथमादिति किम्? षष्ठ्यन्ताद् यथा स्यात् प्रथमान्ताद् मा\n'
        '  भूत्. वेति किम्? वाक्यमपि हि यथा स्यात् — so that the PHRASE\n'
        '  उपगोरपत्यम् may stand beside the single word औपगवः.\n'
        '\n'
        'SETTLED — समर्थानामिति निर्धारणे षष्ठी, समर्थानां मध्ये\n'
        '  प्रथमः प्रत्ययप्रकृतित्वेन निर्धार्यते: the genitive is one of\n'
        '  SELECTION, and the first is picked out from among the\n'
        '  connected words as the base. तस्येति सामान्यं\n'
        '  विशेषलक्षणार्थम्, तदीयं प्राथम्यं विशेषाणां विज्ञायते.\n'
        '\n'
        'SETTLED — the heading is bounded by the point at which its own\n'
        '  words stop meaning anything. स्वार्थिकप्रत्ययावधिश्चायम्\n'
        '  अधिकारः, प्राग् दिशो विभक्तिः इति यावत् —\n'
        '  स्वार्थिकेषु ह्यस्योपयोगो नास्ति, विकल्पोऽपि तत्रानवस्थितः,\n'
        '  केचिन्नित्यमेव भवन्ति: past 5.3.1 the affixes add no meaning\n'
        '  of their own, so there is nothing for *the first of the\n'
        '  connected words* to select, and the option is not steady\n'
        '  there either.\n'
        '\n'
        'NOTE — and the option keeps a compound alive. यद्येवं\n'
        '  समासवृत्तिस्तद्धितवृत्त्या बाध्येत उपग्वपत्यमिति? नैष दोषः,\n'
        "  पूर्वसूत्रादन्यतरस्यांग्रहणमनुवर्तते — 4.1.81's word carries\n"
        '  down and covers that too.'
    ),
    '4.1.83': (
        'SETTLED — प्राग्दीव्यतोऽण्. Until 4.4.2 the affix is अण् unless\n'
        '  something else is said: औपगवः, कापटवः.\n'
        '\n'
        'SETTLED — the boundary is named by taking ONE WORD out of the\n'
        '  rule it stops at. तेन दीव्यति is 4.4.2, and तदेकदेशो\n'
        '  दीव्यच्छब्दोऽवधित्वेन गृह्यते: a single word of that rule is\n'
        '  lifted out and used as the marker. The same instrument\n'
        "  3.3.140's option used, and the same 4.1.87 and 5.2.1 use.\n"
        '\n'
        'SETTLED — and the vṛtti offers three analyses and chooses none.\n'
        '  अधिकारः, परिभाषा, विधिर्वेति त्रिष्वपि दर्शनेष्वपवादविषयं\n'
        '  परिहृत्याण् प्रवर्तते — heading, principle or rule, the result\n'
        '  is the same: अण् comes wherever no exception has the ground.\n'
        '  Nothing turns on which it is, and the commentary says so\n'
        '  rather than deciding.\n'
        '\n'
        'SETTLED — THIS IS WHAT LETS THE RULES THAT FOLLOW STATE ONLY A\n'
        '  SENSE. तस्यापत्यम्, तेन रक्तं रागात्, तत्र भवः name no affix\n'
        "  at all, and 4.1.82's vṛtti calls them लक्षणवाक्यानि —\n"
        '  sentences that give the ground. The affix comes from here.'
    ),
    '4.1.84': (
        'SETTLED — अश्वपत्यादिभ्यश्च. आश्वपतम्, शातपतम्.\n'
        '\n'
        'SETTLED — a rule that gives what the default already gives, and\n'
        '  the vṛtti says why: पत्युत्तरपदाद् ण्यं वक्ष्यति, तस्यापवादः.\n'
        '  The NEXT rule would take these words away, so this one holds\n'
        '  them back **against a rule that has not been stated yet**. A\n'
        '  प्रतिषेध of the future, and the only way to read a rule that\n'
        '  otherwise says nothing.'
    ),
    '4.1.85': (
        'SETTLED — दित्यदित्यादित्यपत्युत्तरपदाण्ण्यः. दैत्यः, आदित्यः,\n'
        '  आदित्यम्; प्राजापत्यम्, सैनापत्यम्.\n'
        '\n'
        'SETTLED — the densest vārttika-set in the pāda, and most of it\n'
        '  cited straight to a text: वाच्यः (मा०सं० १३.५८), मात्या\n'
        '  (मै०सं० २.७.१९), पैतृमत्यम् (मा०सं० ७.४६), पार्थिवा\n'
        '  (ऋ० १.६४.३), पार्थिवी (पै०सं० १६.४६.३), दैव्यम्\n'
        '  (ऋ० १.३१.१७), बाह्याः (शौ०सं० १९.४४.६).\n'
        '\n'
        'SETTLED — and one vārttika settles a whole class of conflicts by\n'
        '  पूर्वविप्रतिषेध: ण्यादयोऽर्थविशेषलक्षणादणपवादात्\n'
        '  पूर्वविप्रतिषेधेन — an EARLIER rule made to beat a later one,\n'
        '  which is the instrument 3.4.37 used and the reverse of\n'
        "  3.3.142's परत्व. दितेरपत्यं दैत्यः, वनस्पतीनां समूहो\n"
        '  वानस्पत्यम्.\n'
        '\n'
        'NOTE — कथं दैतेयः? By making a feminine first — दितिशब्दात्\n'
        "  कृदिकारादक्तिनः (ग०सू० ४९) — and then 4.1.120's स्त्रीभ्यो\n"
        "  ढक्. लिङ्गविशिष्टपरिभाषा चानित्या: the principle 4.1.1's\n"
        '  vṛtti leaned on is here declared NOT invariable, which is the\n'
        '  second paribhāṣā of this pāda to be so declared, after\n'
        "  4.1.41's षिल्लक्षण."
    ),
    '4.1.86': (
        'SETTLED — उत्सादिभ्योऽञ्, अणस्तदपवादानां च बाधकः. It beats the\n'
        '  default AND the exceptions to the default — a rank above what\n'
        '  an ordinary अपवाद claims. औत्सः, औदपानः.\n'
        '\n'
        'NOTE — ग्रीष्मादच्छन्दसीति वक्तव्यम् (ग०सू० ५९), and the vṛtti\n'
        '  stops to say which छन्दस् is meant: छन्दश्चेह वृत्तं गृह्यते\n'
        '  न वेदः — the METRE and not the Veda. त्रिष्टुब् ग्रैष्मी\n'
        '  (काठ०सं० १६.१९). One word that means two things in this\n'
        '  grammar, told apart by the vṛtti where it matters.'
    ),
    '4.1.87': (
        'SETTLED — स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात्, यथाक्रमम्. And its\n'
        "  range is set the same way 4.1.83's was — प्राग् भवनसंशब्दनात्,\n"
        '  a word lifted out of 5.2.1 and used as the marker.\n'
        '\n'
        'SETTLED — ONE AFFIX SERVING FOUR SENSES IN A ROW. स्त्रीषु भवं\n'
        '  स्त्रैणम्; स्त्रीणां समूहः स्त्रैणम्; स्त्रीभ्य आगतं\n'
        '  स्त्रैणम्; स्त्रीभ्यो हितं स्त्रैणम् — born among, a\n'
        '  collection of, come from, good for, and the affix does not\n'
        '  change. The sense comes from the section the rule stands in,\n'
        "  which is exactly what 4.1.83's default made possible.\n"
        '\n'
        'NOTE — स्त्रियाः पुंवद् इति ज्ञापकाद् वत्यर्थे न भवति: one sense\n'
        '  is kept out, and by a ज्ञापक read off 6.3.34, two chapters\n'
        '  later. योगापेक्षं च ज्ञापकमिति स्त्रीवदित्यपि सिद्धम्.'
    ),
    '4.1.88': (
        'SETTLED — द्विगोर्लुगनपत्ये. After a numeral compound the\n'
        '  taddhita is ELIDED: पञ्चसु कपालेषु संस्कृतः पञ्चकपालः,\n'
        '  दशकपालः; द्वौ वेदावधीते द्विवेदः. अनपत्य इति किम्?\n'
        '  द्वैदेवदत्तिः.\n'
        '\n'
        'SETTLED — THIS IS THE MACHINERY THAT LETS A FORM BE DERIVED AND\n'
        '  THEN NOT APPEAR. पञ्चकपालः means *prepared in five bowls*, and\n'
        '  no part of the word that remains carries that meaning: the\n'
        '  affix that said it was given and then elided.\n'
        '\n'
        'SETTLED — and द्विगोः is read as naming the AFFIX. ननु च\n'
        '  प्रत्ययादर्शनस्यैषा संज्ञा? सत्यमेतत्. उपचारेण तु लक्षणया\n'
        '  द्विगुनिमित्तभूतः प्रत्यय एव द्विगुः, तस्य लुग् भवति — the\n'
        '  affix CAUSED by a द्विगु is itself called द्विगु by transfer.\n'
        '  A form that looks the same is then kept out by asking what\n'
        '  caused what: पाञ्चकपालम् stands because न तस्य द्विगुत्वं\n'
        '  निमित्तम्, इतरस्तु द्विगुत्वस्यैव निमित्तम्.\n'
        '\n'
        "NOTE — and 4.1.82's option runs down here: वेत्यनुवर्तते, सा च\n"
        '  व्यवस्थितविभाषा विज्ञायते, which is how पञ्चगर्गरूप्यम् keeps\n'
        '  its affix. The third व्यवस्थितविभाषा the project has met.'
    ),
    '4.1.89': (
        'SETTLED — गोत्रेऽलुगचि. Where a गोत्र affix was elided by\n'
        '  2.4.63 and its like, the elision is REFUSED before a\n'
        '  vowel-initial affix: गार्गीयाः, वात्सीयाः, आत्रेयीयाः,\n'
        '  खारपायणीयाः. अचीति किम्? गर्गरूप्यम्, गर्गमयम्. गोत्र इति\n'
        '  किम्? कौवलम्, बादरम्.\n'
        '\n'
        'NOTE — the two vārttikas divide it by NUMBER: गोत्रस्य बहुषु\n'
        '  लोपिनो बहुवचनान्तस्य प्रवृत्तौ द्व्येकयोरलुक् — बैदः, बैदौ;\n'
        '  and एकवचनद्विवचनान्तस्य प्रवृत्तौ बहुषु लोपो यूनि. Whether\n'
        '  the affix is dropped turns on how many people are meant.'
    ),
    '4.1.90': (
        'SETTLED — यूनि लुक्, and THE ELISION REACHES THE AFFIX BEFORE IT\n'
        '  IS FORMED. प्राग्दीव्यतीयेऽजादौ प्रत्यये विवक्षिते\n'
        '  **बुद्धिस्थेऽनुत्पन्न एव** युवप्रत्ययस्य लुग् भवति,\n'
        '  तस्मिन्निवृत्ते सति यो यतः प्राप्नोति स ततो भवति — what is\n'
        '  elided is something merely INTENDED, held in the mind and\n'
        '  never produced, and once it is gone whatever else would have\n'
        '  applied applies. फाण्टाहृतिः, फाण्टाहृतः.\n'
        '\n'
        '  An elision of a thing that was never there is a strange\n'
        '  instrument, and the vṛtti states it plainly rather than\n'
        '  softening it. It is what lets a derivation be BLOCKED by\n'
        '  running it and removing the result.'
    ),
    '4.1.91': (
        'SETTLED — फक्फिञोरन्यतरस्याम्. पूर्वसूत्रेण नित्ये लुकि प्राप्ते\n'
        '  विकल्प उच्यते — the rule before was obligatory and this makes\n'
        '  it optional for two affixes, so both forms stand: गार्गीयाः\n'
        '  and गार्ग्यायणीयाः, वात्सीयाः and वात्स्यायनीयाः, यास्कीयाः\n'
        '  and यास्कायनीयाः.\n'
        '\n'
        'NOTE — the vṛtti derives each example the long way, naming four\n'
        '  rules for one word: गर्गादिभ्यो यञि कृते यञिञोश्च इति फक्,\n'
        '  गार्ग्यायणः. It is showing that the affix being elided here is\n'
        '  itself the output of a chain, which is why the elision has to\n'
        '  be stated of the affix and not of the word.'
    ),
    '4.1.92': (
        'SETTLED — तस्यापत्यम्, अर्थनिर्देशोऽयम्. Three syllables naming\n'
        '  no affix at all, and it can be that short because 4.1.82 said\n'
        '  which word the affix attaches to and 4.1.83 said which affix\n'
        '  comes: तस्येति षष्ठीसमर्थादपत्यमित्येतस्मिन्नर्थे यथाविहितं\n'
        '  प्रत्ययो भवति — *the affix as it has been provided*.\n'
        '  उपगोरपत्यमौपगवः; आश्वपतः; दैत्यः; औत्सः; स्त्रैणः; पौंस्नः.\n'
        '\n'
        'SETTLED — AND IT FACES BOTH WAYS. पूर्वैरुत्तरैश्च प्रत्ययैर्\n'
        '  अभिसंबध्यते: connected with the affixes BEFORE it as well as\n'
        '  those after, which is how दैत्यः and औत्सः are patronymics\n'
        '  though 4.1.85 and 4.1.86 were stated first. Every heading the\n'
        '  project has met governed forward only — 4.1.1, 4.1.76, 4.1.82,\n'
        '  3.2.84, 3.4.67 — and this one reaches back as well.\n'
        '\n'
        'SETTLED — प्रकृत्यर्थविशिष्टः षष्ठ्यर्थोऽपत्यमात्रञ्चेह गृह्यते,\n'
        '  लिङ्गवचनादिकमन्यत् सर्वमविवक्षितम्. What is taken is the\n'
        "  genitive's sense as qualified by the base, and *descendant*\n"
        '  simply; gender and number are not in question at all.\n'
        '\n'
        'NOTE — the kārikā sets this rule against 4.3.120:\n'
        '  तस्येदमित्यपत्येऽपि बाधनार्थं कृतं भवेत् / उत्सर्गः शेष\n'
        '  एवासौ वृद्धान्यस्य प्रयोजनम् — *this belongs to him* would\n'
        '  have covered a descendant too and would then have needed\n'
        '  beating; this rule is what beats it, and the other stands as\n'
        '  the residue.'
    ),
    '4.1.93': (
        'SETTLED — एको गोत्रे. ONE affix for a whole lineage.\n'
        '  भेदेन प्रत्यपत्यं प्रत्ययोत्पत्तिप्रसङ्गे नियमः क्रियते — an\n'
        '  affix would otherwise come at every generation, and this says\n'
        '  गोत्र एक एव प्रत्ययो भवति, सर्वेऽपत्येन युज्यन्ते.\n'
        '\n'
        'SETTLED — गर्गस्यापत्यं गार्गिः, गार्गेरपत्यं गार्ग्यः,\n'
        '  तत्पुत्रोऽपि गार्ग्यः — and his son too, and his.\n'
        '  योऽपि व्यवहितेन जनितः, सोऽपि प्रथमप्रकृतेरपत्यं भवत्येव: a\n'
        '  descendant born at ANY remove is still the descendant of the\n'
        '  FIRST base, which is what stops the affixes accumulating.\n'
        '\n'
        'NOTE — अपतनादपत्यम्, *that which does not fall away*. And the\n'
        '  vṛtti offers the restriction two ways — प्रत्ययो नियम्यते or\n'
        '  प्रकृतिर्नियम्यते, the affix restricted or the base — without\n'
        '  choosing between them. The third time in two pādas that a\n'
        '  reading is left open because nothing turns on it.'
    ),
    '4.1.94': (
        'SETTLED — गोत्राद् यून्यस्त्रियाम्. The young-descendant affix is\n'
        '  added to the LINEAGE-FORM and not to the ultimate base:\n'
        '  गार्ग्यस्यापत्यं युवा गार्ग्यायणः, वात्स्यायनः, दाक्षायणः,\n'
        '  प्लाक्षायणः, औपगविः, नाडायनिः. न परमप्रकृत्यनन्तरयुवभ्यः.\n'
        '  अस्त्रियामिति किम्? दाक्षी, प्लाक्षी.\n'
        '\n'
        'SETTLED — A SŪTRA SPLIT IN TWO BECAUSE NEITHER READING OF IT\n'
        '  WHOLE WOULD WORK. किं पुनरत्र प्रतिषिध्यते? यदि नियमः,\n'
        '  स्त्रियामनियमः प्राप्नोति — read as a restriction it leaves\n'
        '  the feminine unrestricted; अथ युवप्रत्ययः, स्त्रियां\n'
        '  गोत्रप्रत्ययेनाभिधानं न प्राप्नोति, गोत्रसंज्ञाया युवसंज्ञया\n'
        '  बाधितत्वात् — read as giving an affix it leaves the feminine\n'
        '  with none at all. **तस्माद् योगविभागः कर्तव्यः**: गोत्राद्\n'
        '  यूनि प्रत्ययो भवति, and then ततोऽस्त्रियाम्.\n'
        '\n'
        '  What the second half then refuses is the NAME and not the\n'
        '  affix — युवसंज्ञैव प्रतिषिध्यते, तेन स्त्री गोत्रप्रत्ययेन\n'
        '  अभिधास्यते — so the feminine is named by the lineage-affix\n'
        '  after all. A division that changes what is being denied.'
    ),
    '4.1.95': (
        'SETTLED — अत इञ्, अणोऽपवादः. दक्षस्यापत्यं दाक्षिः.\n'
        '  तपरकरणं किम्? शुभंयाः, कीलालपा इत्यतो मा भूत् — the त holds\n'
        '  it to the short vowel, the same job it did at 4.1.4.\n'
        '\n'
        'NOTE — कथं प्रदीयतां दाशरथाय मैथिली (वा०रा० युद्ध० ९.२२)?\n'
        '  शेषविवक्षया भविष्यति. A famous line accounted for by the\n'
        '  residual sense rather than by this rule, which is how the\n'
        '  vṛtti keeps attested usage inside the grammar without\n'
        '  bending a rule to fit it.'
    ),
    '4.1.96': (
        'SETTLED — बाह्वादिभ्यश्च. बाहविः, औपबाहविः. अनकारार्थ आरम्भः,\n'
        '  begun for stems NOT in अ; and क्वचिद् बाधकबाधनार्थः, in\n'
        '  places to beat what would have beaten it.\n'
        '\n'
        'SETTLED — an आकृतिगण, and the च is what says so.\n'
        '  चकारोऽनुक्तसमुच्चयार्थ आकृतिगणतामस्य बोधयति — the list is\n'
        '  open, recognised by shape: जाम्बिः, ऐन्द्रशर्मिः, आजधेनविः,\n'
        '  आजबन्धविः, औङुलोमिः. The second such list in the pāda, after\n'
        "  4.1.56's क्रोडादि.\n"
        '\n'
        'NOTE — and two vārttikas narrow it by USE rather than by form.\n'
        '  बाह्वादिप्रभृतिषु येषां दर्शनं गोत्रभावे लौकिके ततोऽन्यत्र\n'
        '  तेषां प्रतिषेधः — a member seen in ordinary speech as a\n'
        '  lineage-name is refused elsewhere: बाहुर्नाम कश्चित्,\n'
        '  तस्यापत्यं बाहवः. And संबन्धिशब्दानां च तत्सदृशात् प्रतिषेधः.'
    ),
    '4.1.97': (
        'SETTLED — सुधातुरकङ् च. सुधातुरपत्यं सौधातकिः — the affix and a\n'
        '  substitution in the stem, तत्सन्नियोगेन, in one act. The same\n'
        "  shape as 4.1.7's र and 3.4.84's आह्.\n"
        '\n'
        'NOTE — व्यासवरुडनिषादचण्डालबिम्बानामिति वक्तव्यम् extends the\n'
        '  substitution to five more words: वैयासकिः, वारुडकिः,\n'
        '  नैषादकिः, चाण्डालकिः, बैम्बकिः.'
    ),
    '4.1.98': (
        'SETTLED — कुञ्जादिभ्यश्च्फञ्, इञोऽपवादः. कौञ्जायन्यः,\n'
        '  ब्राध्नायन्यः. गोत्र इति किम्? कुञ्जस्यापत्यमनन्तरं कौञ्जिः.\n'
        '\n'
        'SETTLED — ञकारो वृद्ध्यर्थः, and चकारो विशेषणार्थः: the च is\n'
        '  there for 5.3.113 व्रातच्फञोरस्त्रियाम् to pick this affix out\n'
        '  by — a letter placed for a rule a chapter away.\n'
        '\n'
        'SETTLED — AND THE ACCENT CHANGES WITH THE NUMBER, though the\n'
        '  affix does not. एकवचनद्विवचनयोः सतिशिष्टत्वाद् ञित्स्वरेणैव\n'
        '  भवितव्यम्; बहुवचने तु कौञ्जायना इति परमपि ञित्स्वरं त्यक्त्वा\n'
        '  चित्स्वर एवेष्यते — singular and dual take the accent one mark\n'
        "  gives and the plural the other's, and the later mark yields.\n"
        '\n'
        'NOTE — गोत्राधिकारश्च शिवादिभ्योऽण् इति यावत्: the vṛtti names\n'
        '  4.1.112 as where the गोत्र section stops, fourteen sūtras\n'
        '  before it gets there.'
    ),
    '4.1.99': (
        'SETTLED — नडादिभ्यः फक्. नाडायनः, चारायणः. गोत्र इत्येव —\n'
        '  नाडिः.\n'
        '\n'
        'NOTE — one member is in two lists, and the vṛtti reads the\n'
        '  double membership as teaching something. शालङ्किः पिता,\n'
        '  शालङ्किः पुत्रः — गोत्रविशेषे कौशिके फकं स्मरन्ति, इञेवान्यत्र;\n'
        "  अथवा पैलादिपाठ एव ज्ञापक इञो भावस्य. A word's place in one\n"
        '  gaṇa read as evidence about what happens in another.'
    ),
    '4.1.100': (
        'SETTLED — हरितादिभ्योऽञः, इञोऽपवादः. हारितायनः, कैन्दासायनः.\n'
        '  हरितादिर्बिदाद्यन्तर्गणः — a list inside a list.\n'
        '\n'
        'SETTLED — A HEADING PRESENT AND OVERRIDDEN BY CAPACITY.\n'
        '  ननु च गोत्र इति वर्तते, न च गोत्रादपरो गोत्रप्रत्ययो भवति,\n'
        '  एको गोत्रे इति वचनात्? सत्यमेतत् — 4.1.93 allows a lineage\n'
        '  only ONE affix, so under the heading as carried this rule\n'
        '  could give nothing. इह तु गोत्राधिकारेऽपि **सामर्थ्याद् यूनि\n'
        '  प्रत्ययो विज्ञायते**: the heading says गोत्र and the rule is\n'
        '  read as being about the YOUNG descendant instead, because it\n'
        '  could not otherwise do anything at all.\n'
        '  गोत्राधिकारस्तूत्तरार्थः — the heading is carried for the\n'
        '  rules after this one, not for this one.'
    ),
    '4.1.101': (
        'SETTLED — यञिञोश्च. गार्ग्यायणः, वात्स्यायनः; दाक्षायणः,\n'
        '  प्लाक्षायणः.\n'
        '\n'
        'SETTLED — गोत्रग्रहणेन यञिञौ विशेष्येते, तदन्तात् तु\n'
        '  यून्येवायं प्रत्ययः, गोत्राद् यूनीति वचनात्. The carried word\n'
        '  गोत्र qualifies the two AFFIXES named rather than the sense,\n'
        '  and what the rule gives is the young-descendant affix by\n'
        '  4.1.94 — so one word carried down does one job and a rule\n'
        '  seven sūtras back does the other.\n'
        '\n'
        'NOTE — द्वीपादनुसमुद्रं यञ् (4.3.10) and सुतङ्गमादिभ्य इञ्\n'
        '  (4.2.80) are kept out, neither being patronymic. The same\n'
        "  exclusion 4.1.16's आपत्यग्रहणं कर्तव्यम् made for the same\n"
        '  affix, eighty-five sūtras earlier.'
    ),
    '4.1.102': (
        'SETTLED — शरद्वच्छुनकदर्भाद् भृगुवत्साग्रायणेषु, यथासंख्यम्.\n'
        '  THREE WORDS AND THREE LINEAGES, each word taking the affix\n'
        '  only inside its own: शारद्वतायनो भवति भार्गवश्चेत्,\n'
        '  शारद्वतोऽन्यः; शौनकायनो भवति वात्स्यश्चेत्, शौनकोऽन्यः;\n'
        '  दार्भायणो भवत्याग्रायणश्चेत्, दार्भिरन्यः.\n'
        '\n'
        'SETTLED — **a condition that is nothing in the word at all but\n'
        '  a fact about whose family is meant.** Five rules of this run\n'
        '  turn on it — 4.1.102, 4.1.106, 4.1.107, 4.1.108, 4.1.111 —\n'
        '  and no rule anywhere earlier in the project does.\n'
        '  शरद्वच्छुनकशब्दौ बिदादी, ताभ्यामञोऽपवादः फक्.'
    ),
    '4.1.103': (
        'SETTLED — द्रोणपर्वतजीवन्तादन्यतरस्याम्, इञोऽपवादः. द्रौणायनः\n'
        '  beside द्रौणिः, पार्वतायनः beside पार्वतिः, जैवन्तायनः beside\n'
        '  जैवन्तिः.\n'
        '\n'
        'NOTE — कथमनन्तरोऽश्वत्थामा द्रौणायन इत्युच्यते? नैवात्र\n'
        '  महाभारतद्रोणो गृह्यते, किं तर्हि? अनादिः. **इदानीन्तनात् तु\n'
        '  श्रुतिसामान्यादध्यारोपेण तथाभिधानं भवति** — a present-day man\n'
        '  is called by a lineage-form through mere likeness of sound,\n'
        '  transferred onto him. The grammar declines to own the usage\n'
        '  and accounts for it anyway, which it does again two sūtras\n'
        '  later for राम and व्यास.'
    ),
    '4.1.104': (
        'SETTLED — अनृष्यानन्तर्ये बिदादिभ्योऽञ्. बैदः, और्वः.\n'
        '\n'
        'SETTLED — A NEGATIVE COMPOUND READ ONE WAY BECAUSE THE OTHER\n'
        '  WAY BREAKS A NAME. अनृष्यानन्तर्य is read as *the immediate\n'
        '  descendant of a NON-SAGE* — अनृषिभ्योऽनन्तरे भवतीति — and not\n'
        '  as *not being the immediate descendant of a sage*. ये पुनरत्र\n'
        '  अनृषिशब्दाः पुत्रादयः, तेभ्योऽनन्तरापत्य एव भवति: पौत्रः,\n'
        '  दौहित्रः.\n'
        '\n'
        '  The second reading would forbid the affix right after a sage,\n'
        '  and then कौशिको विश्वामित्रः would be wrong:\n'
        '  ऋष्यपत्यनैरन्तर्यविषये प्रतिषेधे विज्ञायमाने कौशिको\n'
        '  विश्वामित्र इति दुष्यति. **A grammatical reading settled by a\n'
        '  proper name it would otherwise spoil**, and the vṛtti says\n'
        '  अवश्यं चैतदेवं विज्ञेयम् — it MUST be read so.\n'
        '\n'
        'NOTE — इन्द्रभूः सप्तमः काश्यपानाम् is answered separately:\n'
        '  अनन्तरापत्यरूपेणैव ऋष्यणाभिधानं भविष्यति. And बैदिः is\n'
        '  accounted for by बाह्वादिराकृतिगणः — the open list of 4.1.96\n'
        '  reaching a word that is also in this one.'
    ),
    '4.1.105': (
        'SETTLED — गर्गादिभ्यो यञ्. गार्ग्यः, वात्स्यः.\n'
        '\n'
        'NOTE — three forms accounted for and none of them licensed.\n'
        '  मनुशब्दोऽत्र पठ्यते, तत्र कथं मानवी प्रजा? गोत्र इत्युच्यते,\n'
        '  अपत्यसामान्ये भविष्यति. कथमनन्तरो रामो जामदग्न्यः, व्यासः\n'
        '  पाराशर्य इति? गोत्ररूपाध्यारोपेण भविष्यति — the same transfer\n'
        '  4.1.103 used. And the vṛtti states what the grammar WOULD\n'
        '  give beside what people say: अनन्तरापत्यविवक्षायां तु\n'
        '  ऋष्यणैव भवितव्यं जामदग्नः, पाराशर इति.'
    ),
    '4.1.106': (
        'SETTLED — मधुबभ्र्वोर्ब्राह्मणकौशिकयोः, यथासंख्यम्. माधव्यो\n'
        '  भवति ब्राह्मणश्चेत्, माधव एवान्यः; बाभ्रव्यो भवति कौशिकश्चेत्,\n'
        '  बाभ्रव एवान्यः.\n'
        '\n'
        "SETTLED — and the word is ALREADY in 4.1.105's list, which is\n"
        '  why this is a restriction and not a gift. बभ्रुशब्दो गर्गादिषु\n'
        '  पठ्यते, ततः सिद्धे यञि कौशिके नियमार्थं वचनम्.\n'
        '\n'
        'NOTE — and the membership still earns its keep:\n'
        "  गर्गादिषु पाठोऽप्यन्तर्गणकार्यार्थः — 4.1.18's सर्वत्र\n"
        '  लोहितादिकतन्तेभ्यः reaches it through that list, बाभ्रव्यायणी.\n'
        '  A word in a gaṇa for one purpose, restricted out of it for\n'
        '  another, and kept in it for a third.'
    ),
    '4.1.107': (
        'SETTLED — कपिबोधादाङ्गिरसे. काप्यः, बौध्यः. आङ्गिरस इति किम्?\n'
        '  कापेयः, बौधिः.\n'
        '\n'
        'NOTE — the same shape as the rule before: कपिशब्दो गर्गादिषु\n'
        '  पठ्यते, तस्य नियमार्थं वचनम्, आङ्गिरसे यथा स्यात्, and\n'
        '  लोहितादिकार्यार्थश्च गणे पाठः — काप्यायनी. Two adjacent rules\n'
        '  doing the same three-part thing to two different words.'
    ),
    '4.1.108': (
        'SETTLED — वतण्डाच्च. वातण्ड्यः. आङ्गिरस इति किम्? वातण्डः.\n'
        '\n'
        'SETTLED — A WORD IN TWO LISTS, AND BOTH AFFIXES STAND WHERE THE\n'
        '  RULE DOES NOT REACH. किमर्थमिदं यावता गर्गादिष्वयं पठ्यते?\n'
        '  शिवादिष्वप्ययं पठ्यते — it is in गर्गादि AND in शिवादि, so\n'
        '  this rule is stated शिवाद्यणोऽपवादार्थम्, to except that other\n'
        '  list inside the Āṅgirasa lineage. And outside it,\n'
        '  अनाङ्गिरसे तूभयत्र पाठसामर्थ्यात् प्रत्ययद्वयमपि भवति:\n'
        '  वातण्ड्यः AND वातण्डः, both, **on the strength of being in two\n'
        '  lists**. A double membership read as licensing two forms\n'
        '  rather than as a conflict to be settled.'
    ),
    '4.1.109': (
        'SETTLED — लुक् स्त्रियाम्. वतण्डशब्दादाङ्गिरस्यां स्त्रियां\n'
        '  यञ्प्रत्ययस्य लुग् भवति.\n'
        '\n'
        'SETTLED — and WHAT THE ELISION BUYS IS A DIFFERENT AFFIX.\n'
        '  लुकि कृते शार्ङ्गरवादिपाठाद् ङीन् भवति — once the यञ् is gone,\n'
        '  4.1.73 reaches the bare word and supplies ङीन्: वतण्डी. A rule\n'
        '  that removes an affix in order that another may come, which is\n'
        "  4.1.90's elision-before-formation seen from the other end:\n"
        '  तस्मिन्निवृत्ते सति यो यतः प्राप्नोति स ततो भवति.\n'
        '\n'
        'NOTE — आङ्गिरस इति किम्? वातण्ड्यायनी. शिवाद्यणि तु वातण्डी —\n'
        '  and by the other list the same form arrives anyway, which is\n'
        '  what 4.1.108 said about that word being in two gaṇas.'
    ),
    '4.1.110': (
        'SETTLED — अश्वादिभ्यः फञ्. आश्वायनः, आश्मायनः.\n'
        '\n'
        'NOTE — ये त्वत्र प्रत्ययान्ताः पठ्यन्ते, तेभ्यः सामर्थ्याद्\n'
        '  यूनि प्रत्ययो विज्ञायते: the members that already end in an\n'
        '  affix are read as taking the young-descendant one, by\n'
        "  capacity. 4.1.100's argument again, ten sūtras later and about\n"
        '  members of a list rather than about a whole rule.'
    ),
    '4.1.111': (
        'SETTLED — भर्गात्त्रैगर्ते. भार्गायणो भवति त्रैगर्तश्चेत्,\n'
        '  भार्गिरन्यः. The fifth and last rule of this run to turn on\n'
        '  whose family is meant.'
    ),
    '4.1.112': (
        'SETTLED — शिवादिभ्योऽण्, यथायथमिञादीनामपवादः. शैवः, प्रौष्ठः.\n'
        '\n'
        'SETTLED — AND THE गोत्र SECTION ENDS HERE. गोत्र इति निवृत्तम्,\n'
        '  अतः प्रभृति सामान्येन प्रत्यया विज्ञायन्ते — from this rule on\n'
        '  the affixes are understood generally, of a descendant of any\n'
        "  degree. 4.1.98's vṛtti had already named this rule as the\n"
        '  place: गोत्राधिकारश्च शिवादिभ्योऽण् इति यावत्, said fourteen\n'
        '  sūtras before.\n'
        '\n'
        'SETTLED — A LIST USED FOR CO-APPLICATION RATHER THAN FOR\n'
        '  EXCEPTION. गङ्गाशब्दः पठ्यते तिकादिफिञा शुभ्रादिढका च\n'
        '  समावेशार्थम्, तेन त्रैरूप्यं भवति — गङ्गा is in THREE lists at\n'
        '  once so that three affixes may ALL apply: गाङ्गः, गाङ्गायनिः,\n'
        '  गाङ्गेयः. Every gaṇa in this pāda until now carved exceptions\n'
        '  out of other rules; this membership ADDS. विपाश is there for\n'
        '  the same reason — वैपाशः, वैपाशायन्यः.\n'
        '\n'
        'NOTE — and one member is there for the opposite purpose, and\n'
        '  only half of it: तक्षन्शब्दोऽत्र पठ्यते कारिलक्षणमुदीचामिञं\n'
        "  बाधितुम्, ण्यप्रत्ययस्य तु बाधो नेष्यते — it beats 4.1.153's\n"
        "  affix and is NOT wanted to beat 4.1.152's, so both ताक्ष्णः\n"
        '  and ताक्षण्यः stand. One membership beating one rule and\n'
        '  sparing another.'
    ),
    '4.1.113': (
        'SETTLED — अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः, ढकोऽपवादः.\n'
        '  यामुनः, ऐरावतः, वैतस्तः, नार्मदः; शैक्षितः, चैन्तितः.\n'
        '\n'
        'SETTLED — TWO KINDS OF CONDITION IN ONE RULE, AND THE VṚTTI\n'
        '  NAMES THE DIFFERENCE. अवृद्धाभ्य इति **शब्दधर्मः**,\n'
        '  नदीमानुषीभ्य इति **अर्थधर्मः** — the first is a property of\n'
        '  the WORD, whether its first vowel is a vṛddhi by 1.1.73; the\n'
        '  second is a property of what the word MEANS, a river or a\n'
        '  woman. तेनाभेदात् प्रकृतयो निर्दिश्यन्ते: stated as one\n'
        '  because there is no difference in what they pick out. The\n'
        '  distinction returns at 4.1.131 and 4.1.135.\n'
        '\n'
        'NOTE — तन्नामिकाभ्य इति सर्वनाम्ना प्रत्ययप्रकृतेः परामर्शः,\n'
        '  a pronoun pointing back at the base. Three counter-examples,\n'
        '  one per word: चान्द्रभागेयः, सौपर्णेयः, शौभनेयः.'
    ),
    '4.1.114': (
        'SETTLED — ऋष्यन्धकवृष्णिकुरुभ्यश्च, इञोऽपवादः. वासिष्ठः,\n'
        '  वैश्वामित्रः; श्वाफल्कः, रान्धसः; वासुदेवः, आनिरुद्धः;\n'
        '  नाकुलः, साहदेवः.\n'
        '\n'
        'SETTLED — AND HERE THE VṚTTI DEFENDS THE GRAMMAR AGAINST ITS\n'
        '  OWN EXAMPLES. कथं पुनर्नित्यानां शब्दानाम्\n'
        '  अन्धकादिवंशसमाश्रयणेनान्वाख्यानं युज्यते? — if words are\n'
        '  eternal, how can a rule be framed by reference to particular\n'
        '  royal houses, which are not?\n'
        '\n'
        '  Two answers, and neither is dropped. केचिदाहुः —\n'
        '  **काकतालीयन्यायेन** कुर्वादिवंशेष्वसंकरेणैव नकुलसहदेवादयः\n'
        '  शब्दास्सुबहवः संकलिताः, तानुपादाय पाणिनिना स्मृतिर्\n'
        '  उपनिबद्धेति: by the crow-and-palm-fruit coincidence a great\n'
        '  many such words happened to gather in those houses without\n'
        '  mixing, and Pāṇini recorded what he found — **the rule is a\n'
        '  record of an accident**. अथवान्धकवृष्णिकुरुवंशा अपि नित्या\n'
        '  एव, तेषु ये शब्दाः प्रयुज्यन्ते, तत्रेदं प्रत्ययविधानम्:\n'
        '  or the houses are eternal too.\n'
        '\n'
        '  The first answer is the more interesting, and the vṛtti puts\n'
        '  it first: a grammar of eternal speech containing a rule that\n'
        '  is admitted to be contingent.'
    ),
    '4.1.115': (
        'SETTLED — मातुरुत्संख्यासंभद्रपूर्वायाः. द्वैमातुरः,\n'
        '  षाण्मातुरः, सांमातुरः, भाद्रमातुरः.\n'
        '\n'
        'SETTLED — उकारादेशार्थं वचनम्, प्रत्ययः पुनरुत्सर्गेणैव\n'
        '  सिद्धः. The affix came already from 4.1.83, so the whole rule\n'
        '  is the उ. The fourth rule of this pāda whose stated affix is\n'
        '  not what it is for, after 4.1.7, 4.1.97 and 4.1.116.\n'
        '\n'
        'NOTE — स्त्रीलिङ्गनिर्देशोऽर्थापेक्षः, तेन धान्यमातुर्ग्रहणं\n'
        "  न भवति: the feminine of the rule's own word is read as being\n"
        '  about the SENSE. 4.1.120 will read the same kind of word the\n'
        '  opposite way, as naming an affix.'
    ),
    '4.1.116': (
        'SETTLED — कन्यायाः कनीन च, ढकोऽपवादः. तत्सन्नियोगेन कनीनशब्द\n'
        '  आदेशो भवति: कानीनः कर्णः, कानीनो व्यासः — Karṇa and Vyāsa in\n'
        '  one line, and both born of unmarried mothers, which is what\n'
        '  the word says.'
    ),
    '4.1.117': (
        'SETTLED — विकर्णशुङ्गच्छगलाद् वत्सभरद्वाजात्रिषु, यथासंख्यम्.\n'
        '  वैकर्णो भवति वात्स्यश्चेत्, वैकर्णिरन्यः; शौङ्गो भवति\n'
        '  भारद्वाजश्चेत्; छागलो भवत्यात्रेयश्चेत्. The sixth rule of\n'
        '  the pāda to turn on whose family is meant.\n'
        '\n'
        'SETTLED — TWO READINGS OF THE SŪTRA ITSELF, AND BOTH ARE\n'
        '  AUTHORITATIVE. शुङ्गाशब्दं स्त्रीलिङ्गमन्ये पठन्ति, ततो ढकं\n'
        '  प्रत्युदाहरन्ति शौङ्गेय इति — others read the word as\n'
        '  feminine and give a different counter-example. **द्वयमपि\n'
        '  चैतत् प्रमाणम् उभयथा सूत्रप्रणयनात्**: both are valid,\n'
        '  because the sūtra was composed both ways. Not two views of\n'
        '  one text but two texts, and the vṛtti accepts both without\n'
        '  choosing. The collation in this project records where the\n'
        '  editions differ; this is the commentary doing the same thing\n'
        '  and declining to settle it.'
    ),
    '4.1.118': (
        'SETTLED — पीलाया वा. पैलः beside पैलेयः. An option where\n'
        "  4.1.121's ढक् would have come outright, stated because that\n"
        "  rule beats 4.1.113's अण् — तन्नामिकाणो बाधके द्व्यचः इति\n"
        '  ढकि प्राप्तेऽण् प्रत्ययः पक्षे विधीयते. A rule stated to\n'
        '  restore, in part, what a rule three ahead takes away.'
    ),
    '4.1.119': (
        'SETTLED — ढक् च मण्डूकात्. माण्डूकेयः — and चकारादण् च वा,\n'
        '  **तेन त्रैरूप्यं भवति**: माण्डूकेयः, माण्डूकः, माण्डूकिः.\n'
        "  One च making three forms, which is 4.1.38's मनोरौ वा\n"
        '  eighty-one sūtras later and by a different instrument.'
    ),
    '4.1.120': (
        'SETTLED — स्त्रीभ्यो ढक्. सौपर्णेयः, वैनतेयः.\n'
        '\n'
        'SETTLED — स्त्री HERE NAMES THE AFFIX AND NOT THE SENSE. इह\n'
        '  स्त्रीग्रहणेन टाबादिप्रत्ययान्ताः शब्दा गृह्यन्ते, and\n'
        '  **स्त्रीप्रत्ययविज्ञापनाद् असत्यर्थग्रहणे** इह न भवति —\n'
        '  इडबिडोऽपत्यम्, दरदोऽपत्यम् give ऐडबिडः and दारदः, being\n'
        '  feminine in sense and carrying no feminine affix. The exact\n'
        '  reverse of 4.1.115, five sūtras back, where the feminine of\n'
        "  the rule's own word WAS read as being about the sense.\n"
        '\n'
        'NOTE — वडवाया वृषे वाच्ये: वाडवेयो वृषः स्मृतः, and\n'
        '  अपत्ये प्राप्तस्ततोऽपकृष्य विधीयते, तेनापत्ये वाडव इति\n'
        '  भवति — the affix is pulled OUT of the descendant-sense and\n'
        '  given to another, so the descendant is left with a different\n'
        '  one. अण् क्रुञ्चाकोकिलात् स्मृतः — क्रौञ्चः, कौकिलः.'
    ),
    '4.1.121': (
        'SETTLED — द्व्यचः, तन्नामिकाणोऽपवादः. दात्तेयः, गौपेयः.\n'
        "  द्व्यच इति किम्? यामुनः — three vowels, and 4.1.113's अण्\n"
        '  stands. A condition of sheer length, the second in the pāda\n'
        "  after 4.1.56's बह्वच्."
    ),
    '4.1.122': (
        'SETTLED — इतश्चानिञः. आत्रेयः, नैधेयः. स्त्रीग्रहणं निवृत्तम्,\n'
        '  चकारो द्व्यच इत्यस्यानुकर्षणार्थः — one word stops carrying\n'
        '  and a च pulls another down, in the same rule.\n'
        '\n'
        "SETTLED — अनिञः IS A CONDITION ON ANOTHER RULE'S OUTPUT. इत\n"
        '  इति किम्? दाक्षिः, प्लाक्षिः — those end in इ too, and the\n'
        "  only difference is that their इ is 4.1.95's इञ्. So the rule\n"
        '  excludes not a shape but a derivation. अनिञ इति किम्?\n'
        '  दाक्षायणः, प्लाक्षायणः. द्व्यच इत्येव — मारीचः.'
    ),
    '4.1.123': (
        'SETTLED — शुभ्रादिभ्यश्च, यथायोगमिञादीनामपवादः. शौभ्रेयः,\n'
        '  वैष्टपुरेयः.\n'
        '\n'
        'NOTE — चकारोऽनुक्तसमुच्चयार्थ आकृतिगणताम् अस्य बोधयति: the\n'
        "  third open list of the pāda, after 4.1.56's क्रोडादि and\n"
        "  4.1.96's बाह्वादि — and this one is what accounts for\n"
        '  गाङ्गेयः and पाण्डवेयः, two of the commonest patronymics in\n'
        '  the language, neither of which any closed rule reaches.'
    ),
    '4.1.124': (
        'SETTLED — विकर्णकुषीतकात् काश्यपे. वैकर्णेयः, कौषीतकेयः.\n'
        '  काश्यप इति किम्? वैकर्णिः, कौषीतकिः.\n'
        '\n'
        'NOTE — विकर्ण is here AND at 4.1.117, with a different affix in\n'
        '  a different family: वैकर्णः among the Vātsyas, वैकर्णेयः\n'
        '  among the Kāśyapas, वैकर्णिः elsewhere. One word, three\n'
        '  families, three affixes.'
    ),
    '4.1.125': (
        'SETTLED — भ्रुवो वुक् च. भ्रौवेयः — the affix and an augment\n'
        '  together, तत्सन्नियोगेन, for the fourth time in this pāda.'
    ),
    '4.1.126': (
        'SETTLED — कल्याण्यादीनामिनङ्. काल्याणिनेयः, सौभागिनेयः,\n'
        '  दौर्भागिनेयः — with उभयपदवृद्धि by 7.3.19, both members\n'
        '  strengthened.\n'
        '\n'
        'SETTLED — AND THE LIST IS THERE FOR TWO REASONS AT ONCE.\n'
        '  स्त्रीप्रत्ययान्तानाम् **आदेशार्थं** ग्रहणम्, प्रत्ययस्य\n'
        '  सिद्धत्वाद्; अन्येषाम् **उभयार्थम्** — for the members that\n'
        '  already end in a feminine affix the ढक् came from 4.1.120 and\n'
        '  only the substitution is new; for the rest both are given.\n'
        "  The same split 4.1.49's twelve words had, stated in the same\n"
        '  words, seventy-seven sūtras apart.'
    ),
    '4.1.127': (
        'SETTLED — कुलटाया वा. कौलटिनेयः beside कौलटेयः. आदेशार्थं\n'
        '  वचनम्, प्रत्ययश्च पूर्वेणैव सिद्धः — again the affix was\n'
        '  there already and the rule is for the substitution.\n'
        '\n'
        'SETTLED — and the vṛtti splits the word by what it MEANS.\n'
        '  कुलान्यटतीति कुलटा, पररूपं निपातनात्. या तु कुलान्यटन्ती\n'
        '  **शीलं भिनत्ति**, ततः क्षुद्राभ्यो वा इति परत्वाड् ढ्रका\n'
        '  भवितव्यम् — कौलटेरः. The same form takes a different affix\n'
        '  according to whether the woman merely goes about the houses\n'
        '  or is thereby disgraced, and the second reading sends it to\n'
        '  4.1.131 by परत्व.'
    ),
    '4.1.128': (
        'SETTLED — चटकाया ऐरक्. चाटकैरः.\n'
        '\n'
        'NOTE — three vārttikas on a one-word rule, and the last one\n'
        '  undoes it. चटकाच्चेति वक्तव्यम् adds the masculine —\n'
        '  चटकस्यापत्यं चाटकैरः — and **स्त्रियामपत्ये लुग् वक्तव्यः**\n'
        '  takes the affix away again where the descendant is female:\n'
        '  चटकाया अपत्यं स्त्री चटका, the same word over again.'
    ),
    '4.1.129': (
        'SETTLED — गोधाया ढ्रक्. गौधेरः.\n'
        '\n'
        'NOTE — **शुभ्रादिष्वयं पठ्यते, तेन गौधेयोऽपि भवति**: the word\n'
        "  is in 4.1.123's list as well, so both forms stand. A double\n"
        '  membership licensing two forms, as at 4.1.108, and here the\n'
        '  two rules are six apart.'
    ),
    '4.1.130': (
        'SETTLED — आरगुदीचाम्. गौधारः — in the view of the NORTHERN\n'
        '  teachers, and the seventh attribution in the project.\n'
        '\n'
        'SETTLED — **आचार्यग्रहणं पूजार्थम्**, the word *teachers* is\n'
        "  there FOR HONOUR. That is word for word what 3.4.18's vṛtti\n"
        '  said of प्राचामाचार्याणां मतेन, a hundred and thirteen\n'
        '  sūtras earlier and in a different chapter. And\n'
        '  वचनसामर्थ्यादेव पूर्वेण समावेशो भविष्यति: the two affixes\n'
        '  CO-APPLY on the strength of this rule being stated at all,\n'
        '  so the citation is not a claim to rank.\n'
        '\n'
        'SETTLED — AND THE RULE IS READ AS A ज्ञापक BECAUSE IT IS\n'
        '  OTHERWISE EMPTY. आरग्वचनमनर्थकम्, रका सिद्धत्वात्? —\n'
        "  4.1.129's ढ्रक् would have given the form already. **ज्ञापकं\n"
        '  त्वयमन्येभ्योऽपि भवतीति**: so the point of stating आरक् is\n'
        '  to teach that it comes after OTHER words too — जाडारः,\n'
        '  पाण्डारः. An empty rule read as evidence about words it does\n'
        '  not mention.'
    ),
    '4.1.131': (
        'SETTLED — क्षुद्राभ्यो वा, ढकोऽपवादः. क्षुद्रा अङ्गहीनाः\n'
        '  शीलहीनाश्च — the maimed and the disgraced. काणेरः beside\n'
        '  काणेयः, दासेरः beside दासेयः.\n'
        '\n'
        'SETTLED — ढ्रगनुवर्तते, न आरक्: one of the two affixes given\n'
        '  side by side in the last two rules carries down and the other\n'
        '  does not. Anuvṛtti selecting between two things stated\n'
        "  together, which is 4.1.27's half-a-condition seen at the\n"
        '  level of whole affixes.\n'
        '\n'
        'NOTE — अर्थधर्मेण तदभिधायिन्यः स्त्रीलिङ्गाः प्रकृतयो\n'
        '  निर्दिश्यन्ते: the bases are named by a property of their\n'
        "  MEANING, which is 4.1.113's अर्थधर्म again, eighteen sūtras\n"
        '  on and using the same word for it.'
    ),
    '4.1.132': (
        'SETTLED — पितृष्वसुश्छण्, अणोऽपवादः. पैतृष्वस्रीयः.'
    ),
    '4.1.133': (
        'SETTLED — ढकि लोपः. पैतृष्वसेयः — the स् of the stem goes\n'
        '  before ढक्.\n'
        '\n'
        'SETTLED — A RULE THAT IS ITS OWN ज्ञापक. कथं पुनरिह ढक्\n'
        '  प्रत्ययः? — the rule before gave छण्, and nothing anywhere\n'
        '  gives ढक् after this stem, so what is the elision stated\n'
        "  before? **एतदेव ज्ञापकं ढको भावस्य**: the rule's own\n"
        '  existence is the evidence that the affix comes. A sūtra whose\n'
        '  only support is that it was written — the extreme case of the\n'
        '  ज्ञापक argument this pāda has used four times.'
    ),
    '4.1.134': (
        'SETTLED — मातुश्च. पितृष्वसुरित्येतदपेक्षते,\n'
        '  **पितृष्वसुर्यदुक्तं तद् मातृष्वसुरपि भवति** — whatever was\n'
        "  said of the father's sister holds of the mother's:\n"
        '  छण्प्रत्ययो ढकि लोपश्च. मातृष्वस्रीयः, मातृष्वसेयः.\n'
        '\n'
        "  An अतिदेश carrying TWO rules at once, where 3.4.85's लोटो\n"
        '  लङ्वत् carried one set of operations from one rule. And one\n'
        '  of the two it carries is 4.1.133, which had nothing but its\n'
        '  own existence to stand on.'
    ),
    '4.1.135': (
        'SETTLED — चतुष्पाद्भ्यो ढञ्, अणादीनामपवादः. कामण्डलेयः,\n'
        '  शौन्तिबाहेयः, जाम्बेयः. चतुष्पादभिधायिनीभ्यः प्रकृतिभ्यः —\n'
        '  again a condition on what the base MEANS and not on its\n'
        '  shape, the third such in twenty-two sūtras.'
    ),
    '4.1.136': (
        'SETTLED — गृष्ट्यादिभ्यश्च, अणादीनामपवादः. गार्ष्टेयः,\n'
        '  हार्ष्टेयः.\n'
        '\n'
        'NOTE — गृष्टिशब्दो यश्चतुष्पाद्वचनः, ततः पूर्वेणैव सिद्धः;\n'
        "  **अचतुष्पादर्थं वचनम्** — the list's first member is already\n"
        '  covered by the rule before when it names a four-footed thing,\n'
        '  so the list exists for when it does not. A gaṇa stated for\n'
        "  the complement of its own first member's ordinary sense."
    ),
    '4.1.137': (
        'SETTLED — राजश्वशुरयोर्यत्, यथाक्रममणिञोरपवादः. राजन्यः, श्वशुर्यः.\n'
        '  राज्ञोऽपत्ये जातिग्रहणम् — राजन्यो भवति क्षत्रियजातिश्\n'
        '  चेत्, राजनोऽन्यः: only where the KṢATRIYA CLASS is meant.'
    ),
    '4.1.138': (
        'SETTLED — क्षत्राद् घः. क्षत्रियः — **अयमपि जातिशब्द एव**, a\n'
        '  class-word and not a patronymic; क्षात्रिरन्यः is the\n'
        '  descendant. Two rules running, and both give a CASTE in a\n'
        '  section that gives descendants.'
    ),
    '4.1.139': (
        'SETTLED — कुलात् खः. आढ्यकुलीनः, श्रोत्रियकुलीनः, कुलीनः.\n'
        '  **उत्तरसूत्रे पूर्वपदप्रतिषेधाद् इह तदन्तः केवलश्च\n'
        '  दृश्यते** — the NEXT rule refuses a first member, and that\n'
        '  refusal is what shows this rule takes both the compound and\n'
        "  the bare word. A rule's scope read off its neighbour's\n"
        '  exclusion.'
    ),
    '4.1.140': (
        'SETTLED — अपूर्वपदाद् यत् ढकञौ बहुलम्. कुल्यः, कौलेयकः — and\n'
        '  ताभ्यां मुक्ते खोऽपि भवति, कुलीनः. Three forms from two\n'
        '  rules. पदग्रहणं किम्? बहुच्पूर्वादपि यथा स्यात् — बहुकुल्यः,\n'
        '  so that बहु in front does not count as a first member.'
    ),
    '4.1.141': (
        'SETTLED — महाकुलाद् अञ्खञौ. माहाकुलः, माहाकुलीनः, and पक्षे खः —\n'
        '  महाकुलीनः.'
    ),
    '4.1.142': (
        'SETTLED — दुष्कुलाड् ढक्. दौष्कुलेयः, and अन्यतरस्यामित्यनुवृत्तेः\n'
        '  खश्च — दुष्कुलीनः.'
    ),
    '4.1.143': (
        'SETTLED — स्वसुश्छः, अणोऽपवादः. स्वस्रीयः.'
    ),
    '4.1.144': (
        'SETTLED — भ्रातुर्व्यच्च, अणोऽपवादः. भ्रातृव्यः, and चकाराच् छश्च —\n'
        '  भ्रात्रीयः. तकारः स्वरार्थः.'
    ),
    '4.1.145': (
        'SETTLED — व्यन् सपत्ने. भ्रातृव्यः — and **अपत्यार्थोऽत्र नास्त्येव**,\n'
        '  no descendant-sense at all: समुदायेन चेदमित्रः सपत्न\n'
        '  उच्यते, the whole word means an ENEMY. पाप्मना भ्रातृव्येण\n'
        '  (तै०सं० २.२.१.२). A rule inside the descendant section\n'
        '  whose affix makes no descendant, and the vṛtti says so.'
    ),
    '4.1.146': (
        'SETTLED — रेवत्यादिभ्यष्ठक्, यथायोगं ढगादीनामपवादः. रैवतिकः,\n'
        '  आश्वपालिकः.'
    ),
    '4.1.147': (
        'SETTLED — गोत्रस्त्रियाः कुत्सने ण च. गार्गो जाल्मः, ग्लौचुकायनः; and\n'
        '  चकारात् ठक् च — गार्गिकः.\n'
        '\n'
        '  AND THE VṚTTI SAYS WHAT THE CONTEMPT CONSISTS IN.\n'
        '  **पितुरसंविज्ञाने मात्रा व्यपदेशोऽपत्यस्य कुत्सा** — being\n'
        '  named by the MOTHER, where the father is not known, IS the\n'
        '  disparagement. A social fact stated as a grammatical\n'
        '  condition, and an affix is what carries it. गोत्रमिति\n'
        '  किम्? कारिकेयो जाल्मः. कुत्सन इति किम्? गार्गेयो माणवकः.'
    ),
    '4.1.148': (
        'SETTLED — वृद्धाट् ठक् सौवीरेषु बहुलम्. भागवित्तिकः, तार्णबिन्दविकः —\n'
        '  and पक्षे यथाप्राप्तं फक्, भागवित्तायनः.\n'
        '\n'
        '  **बहुलग्रहणम् उपाधिवैचित्र्यार्थम्**, and the vṛtti spells\n'
        '  out the variety: गोत्रस्त्रिया इत्यारभ्य चत्वारो योगाः,\n'
        '  तेषु **प्रथमः कुत्सन एव, अन्त्यः सौवीरगोत्र एव, मध्यमौ\n'
        '  द्वयोरपि**. Four rules against two conditions, and one word\n'
        '  tells you which rule carries which — a table stated as a\n'
        '  single syllable, with a kārikā to name the three words.'
    ),
    '4.1.149': (
        'SETTLED — फेश्छ च. यामुन्दायनीयः, and चकाराट् ठक् — यामुन्दायनिकः.\n'
        '  फेरिति फिञो ग्रहणं न फिनः, **वृद्धाधिकारात्** — an\n'
        '  abbreviation that could name either of two affixes, settled\n'
        '  by which heading is running.'
    ),
    '4.1.150': (
        'SETTLED — फाण्टाहृतिमिमताभ्यां णफिञौ, फकोऽपवादः. फाण्टाहृतः,\n'
        '  फाण्टाहृतायनिः; मैमतः, मैमतायनिः.\n'
        '\n'
        '  A COMPOUNDING RULE BROKEN ON PURPOSE, AS A SIGNAL.\n'
        '  **अल्पाच्तरस्यापूर्वनिपातो लक्षणव्यभिचारचिह्नम्, तेन\n'
        '  यथासंख्यमिह न भवति** — 2.2.34 puts the word with fewer\n'
        '  vowels first in a dvandva, and here it is not first. The\n'
        "  breach is a MARK that 1.3.10's *taken in order* does not\n"
        '  apply. A rule deliberately violated so that its violation\n'
        '  may carry information.'
    ),
    '4.1.151': (
        'SETTLED — कुर्वादिभ्यो ण्यः. कौरव्यः, गार्ग्यः.\n'
        '\n'
        "  The vṛtti works at telling this ण्य from 4.1.172's: स तु\n"
        '  क्षत्रियात् तद्राजसंज्ञकः, तस्य बहुषु लुका भवितव्यम्, अयं\n'
        '  तु श्रूयत एव — कौरव्याः. Two affixes of the same shape,\n'
        '  and the difference is whether they vanish in the plural.\n'
        '\n'
        '  कथं भाषायां वैन्यो राजेति? **छान्दस एवायं प्रमादात्\n'
        '  कविभिः प्रयुक्तः** — a Vedic form used in ordinary speech\n'
        '  BY THE CARELESSNESS OF POETS. The bluntest thing the vṛtti\n'
        '  says about attested usage anywhere in this pāda, and the\n'
        '  opposite of the अध्यारोप it offered at 4.1.103 and 4.1.105.'
    ),
    '4.1.152': (
        'SETTLED — सेनान्तलक्षणकारिभ्यश्च. कारिषेण्यः, लाक्षण्यः; and from the\n'
        '  कारि words — कारिशब्दः कारूणां तन्तुवायादीनां वाचकः —\n'
        '  तान्तुवाय्यः, कौम्भकार्यः, नापित्यः.'
    ),
    '4.1.153': (
        'SETTLED — उदीचामिञ्. कारिषेणिः, लाक्षणिः. ण्ये प्राप्त इञपरो\n'
        '  विधीयते.\n'
        '\n'
        '  वचनसामर्थ्यादेव प्रत्ययसमावेशे लब्धे **आचार्यग्रहणं\n'
        '  वैचित्र्यार्थम्** — the two co-apply on the strength of the\n'
        '  rule being stated, so naming the teachers is for VARIETY.\n'
        '  4.1.130 and 3.4.18 both read the same naming as being for\n'
        '  HONOUR; this is the third reading of the move and the only\n'
        '  one that differs.\n'
        '\n'
        '  तक्षन्शब्दः शिवादिः, तेनाणायमिञ् बाध्यते, न तु ण्यः —\n'
        "  which is what 4.1.112's note said from the other end."
    ),
    '4.1.154': (
        'SETTLED — तिकादिभ्यः फिञ्. तैकायनिः, कैतवायनिः. वृषशब्दोऽत्र पठ्यते,\n'
        '  तस्य प्रत्ययसन्नियोगेन यकारान्तत्वमिष्यते — वार्ष्यायणिः,\n'
        '  a member whose shape changes only when the affix comes.'
    ),
    '4.1.155': (
        'SETTLED — कौसल्यकार्मार्याभ्यां च, इञोऽपवादः. कौसल्यायनिः,\n'
        '  कार्मार्यायणिः. **परमप्रकृतेरेवायं प्रत्यय इष्यते** —\n'
        '  कोसलस्यापत्यम्, कर्मारस्यापत्यम्: the affix is wanted after\n'
        '  the ULTIMATE base though the rule names the derived form,\n'
        '  प्रत्ययसन्नियोगेन तु प्रकृतिरूपं निपात्यते. A rule that\n'
        '  names one thing and is stated of another.'
    ),
    '4.1.156': (
        'SETTLED — अणो द्व्यचः, इञोऽपवादः. कार्त्रायणिः, हार्त्रायणिः. अण इति\n'
        '  किम्? दाक्षायणः. द्व्यच इति किम्? औपगविः.'
    ),
    '4.1.157': (
        'SETTLED — उदीचां वृद्धादगोत्रात्. आम्रगुप्तायनिः, ग्रामरक्षायणिः.\n'
        '  Three words and a counter-example each: आम्रगुप्तिः,\n'
        '  याज्ञदत्तिः, औपगविः.'
    ),
    '4.1.158': (
        'SETTLED — वाकिनादीनां कुक् च. वाकिनकायनिः, गारेधकायनिः.\n'
        '\n'
        '  **यदिह वृद्धमगोत्रं शब्दरूपं तस्य आगमार्थमेव ग्रहणम्,\n'
        '  अन्येषाम् उभयार्थम्** — for the members the rule before\n'
        '  already reaches only the augment is new; for the rest both\n'
        '  are given. Third time in the pāda, after 4.1.49 and\n'
        '  4.1.126, and stated in the same words each time.'
    ),
    '4.1.159': (
        'SETTLED — पुत्रान्तादन्यतरस्याम्. **तेन त्रैरूप्यं संपद्यते** —\n'
        '  गार्गीपुत्रकायणिः, गार्गीपुत्रायणिः, गार्गीपुत्रिः. Three\n'
        '  forms, and here the option is only on the AUGMENT:\n'
        '  पुत्रान्तमगोत्रमिति पूर्वेणैव प्रत्ययः सिद्धः.'
    ),
    '4.1.160': (
        'SETTLED — प्राचामवृद्धात् फिन् बहुलम्. ग्लुचुकायनिः, अहिचुम्बकायनिः.\n'
        '\n'
        '  FIVE WAYS OF SAYING *OPTIONALLY*, AND ONE WOULD HAVE DONE.\n'
        '  उदीचां, प्राचाम्, अन्यतरस्याम्, बहुलम् इति **सर्व एते\n'
        '  विकल्पार्थाः, तेषामेकेनैव सिध्यति**. So the surplus is\n'
        '  read as two other things: तत्राचार्यग्रहणं **पूजार्थम्**,\n'
        '  बहुलग्रहणं **वैचित्र्यार्थम्** — the redundancy of a whole\n'
        '  run of rules turned into two separate readings.\n'
        '  क्वचिन्न भवत्येव — दाक्षिः, प्लाक्षिः.'
    ),
    '4.1.161': (
        'SETTLED — मनोर्जातावञ्यतौ षुक् च. मानुषः, मनुष्यः — and\n'
        '  **अपत्यार्थोऽत्र नास्त्येव**, जातिशब्दावेतौ. The second\n'
        '  such rule in the section, after 4.1.145.\n'
        '\n'
        '  तथा च मानुषा इति बहुषु न लुग् भवति — the plural keeps the\n'
        '  affix, which a descendant-affix would not, so the claim is\n'
        '  checkable rather than asserted. अपत्यविवक्षायां त्वणैव\n'
        '  भवितव्यम्: मानवी प्रजा. And a kārikā gives a third form\n'
        '  for a third sense: अपत्ये कुत्सिते मूढे मनोरौत्सर्गिकः\n'
        '  स्मृतः — माणवः.'
    ),
    '4.1.162': (
        'SETTLED — अपत्यं पौत्रप्रभृति गोत्रम्. गर्गस्यापत्यं पौत्रप्रभृति\n'
        '  गार्ग्यः. पौत्रप्रभृतीति किम्? कौञ्जिः, गार्गिः.\n'
        '\n'
        '  संबन्धिशब्दत्वादपत्यशब्दस्य यस्य यदपत्यं तदपेक्षया\n'
        '  पौत्रप्रभृतेर्गोत्रसंज्ञा विधीयते — *descendant* is a\n'
        '  RELATIVE term, so the count starts from whoever is in\n'
        '  question and not from a fixed ancestor.\n'
        '\n'
        'NOTE — गोत्रप्रदेशाः: एको गोत्रे इत्येवमादयः. The vṛtti\n'
        '  points back at 4.1.93, which used this name sixty-nine\n'
        '  sūtras before it was conferred.'
    ),
    '4.1.163': (
        'SETTLED — जीवति तु वंश्ये युवा. अभिजनप्रबन्धो वंशः — a father or\n'
        '  forefather still living, and the descendant is called\n'
        '  YOUNG: गार्ग्यायणः, वात्स्यायनः.\n'
        '\n'
        "SETTLED — A WORD'S CASE CHANGED IN READING TO MOVE A\n"
        '  BOUNDARY BY ONE GENERATION. पौत्रप्रभृतीति च न\n'
        '  सामानाधिकरण्येनापत्यं विशेषयति; किं तर्हि? **षष्ठ्या\n'
        '  विपरिणम्यते** पौत्रप्रभृतेर्यदपत्यमिति — read not as\n'
        '  *the descendant from the grandson on* but as *the\n'
        '  descendant OF one from the grandson on*, तेन\n'
        '  **चतुर्थादारभ्य** युवसंज्ञा विधीयते. तुशब्दोऽवधारणार्थः\n'
        '  — युवैव न गोत्रम्.'
    ),
    '4.1.164': (
        'SETTLED — भ्रातरि च ज्यायसि. An elder BROTHER alive, and the rule is\n'
        '  needed because a brother is not an ancestor:\n'
        '  **अवंश्यार्थोऽयमारम्भः**. पूर्वजाः पित्रादयो वंश्या\n'
        '  इत्युच्यन्ते; भ्राता तु न वंश्यः, **अकारणत्वात्** — not\n'
        '  being a cause of the person. गार्ग्ये जीवति गार्ग्यायणोऽस्य\n'
        '  कनीयान् भ्राता.'
    ),
    '4.1.165': (
        'SETTLED — वान्यस्मिन् सपिण्डे स्थविरतरे जीवति. गार्ग्यायणो गार्ग्यो\n'
        '  वा. **तरब्निर्देश उभयोत्कर्षार्थः** — the comparative is\n'
        '  used so that BOTH standing and age must be greater.\n'
        '  स्थविरतर इति किम्? स्थानवयोन्यूने गार्ग्य एव.\n'
        '\n'
        'SETTLED — and सपिण्ड is defined by RITUAL rather than by\n'
        '  descent. सप्तमपुरुषावधयः सपिण्डाः स्मर्यन्ते, येषाम्\n'
        '  **उभयत्र दशाहानि कुलस्यान्नं न भुज्यते** (मनु० ५.६१)\n'
        '  इत्येवमादिकायां क्रियायामनधिकारः — kinship measured by\n'
        '  whose food may not be eaten, and the grammar cites a\n'
        '  law-book to fix a grammatical condition.'
    ),
    '4.1.166': (
        'SETTLED — वृद्धस्य च पूजायाम्. The YOUNG-name used of an elder, OUT\n'
        '  OF RESPECT: तत्र भवान् गार्ग्यायणः, गार्ग्यो वा.\n'
        '  पूजायामिति किम्? गार्ग्यः.\n'
        '\n'
        'NOTE — वृद्धस्येति षष्ठीनिर्देशो **विचित्रा सूत्रस्य\n'
        '  कृतिः**: the genitive is odd, and the vṛtti says so rather\n'
        '  than explaining it away.'
    ),
    '4.1.167': (
        'SETTLED — यूनश्च कुत्सायाम्. And the LINEAGE-name used of a young man,\n'
        '  OUT OF CONTEMPT: गार्ग्यो जाल्मः, गार्ग्यायणो वा.\n'
        '\n'
        'SETTLED — **निवृत्तिप्रधानो विकल्पः**, the option is really\n'
        '  a refusal: युवसंज्ञायां प्रतिषिद्धायां पक्षे गोत्रसंज्ञैव\n'
        '  भवति, **प्रतिपक्षाभावात्** — with the young-name refused,\n'
        '  nothing else is left to be.\n'
        '\n'
        'NOTE — two adjacent rules, one for honour and one for scorn,\n'
        '  making the same pair of names optional in opposite\n'
        '  directions. The affix does not change; who is being\n'
        '  praised or disparaged does.'
    ),
    '4.1.168': (
        'SETTLED — जनपदशब्दात् क्षत्रियादञ्. पाञ्चालः, ऐक्ष्वाकः, वैदेहः.\n'
        '  जनपदशब्दादिति किम्? द्रौह्यवः. क्षत्रियादिति किम्?\n'
        '  पाञ्चालिः.\n'
        '\n'
        '  AND THE SAME AFFIX NAMES THE KING. क्षत्रियसमानशब्दाज्\n'
        '  जनपदशब्दात् **तस्य राजन्यपत्यवत्** — what is said of a\n'
        '  descendant holds of the RULER: पञ्चालानां राजा पाञ्चालः.\n'
        '  An अतिदेश repeated in the vṛtti of every one of the next\n'
        '  eight rules.'
    ),
    '4.1.169': (
        'SETTLED — साल्वेयगान्धारिभ्यां च. साल्वेयः, गान्धारः — stated because\n'
        "  4.1.171's ञ्यङ् would have come: अञपवादे वृद्धादिति ञ्यङि\n"
        '  प्राप्ते पुनरञ् विधीयते. A rule restating an affix to hold\n'
        '  off a rule two ahead, as 4.1.84 did.'
    ),
    '4.1.170': (
        'SETTLED — द्व्यञ्मगधकलिङ्गसूरमसादण्, अञोऽपवादः. आङ्गः, वाङ्गः,\n'
        '  पौण्ड्रः, सौह्मः; मागधः, कालिङ्गः, सौरमसः.'
    ),
    '4.1.171': (
        'SETTLED — वृद्धेत्कोसलाजादाञ् ञ्यङ्, अञोऽपवादः. आम्बष्ठ्यः,\n'
        '  सौवीर्यः; आवन्त्यः, कौन्त्यः; and कोसलाजादयोरवृद्धार्थं\n'
        '  वचनम् — कौसल्यः, आजाद्यः. तपरकरणं किम्? कौमारः, the same\n'
        '  letter doing the same job as at 4.1.4, 4.1.44 and 4.1.95.'
    ),
    '4.1.172': (
        'SETTLED — कुरुनादिभ्यो ण्यः, अणञोरपवादः. कौरव्यः; नैषध्यः, नैपथ्यः.\n'
        "  This affix and 4.1.151's are the same shape and different\n"
        '  things — **this one is a तद्राज and vanishes in the\n'
        "  plural** — and 4.1.151's vṛtti tells them apart by that."
    ),
    '4.1.173': (
        'SETTLED — साल्वावयवप्रत्यग्रथकलकूटाश्मकादिञ्, अञोऽपवादः. औदुम्बरिः,\n'
        '  तैलखलिः, माद्रकारिः, यौगन्धरिः, भौलिङ्गिः, शारदण्डिः.\n'
        '\n'
        '  साल्वा नाम क्षत्रिया, तस्य निवासः साल्वो जनपदः, तदवयवा\n'
        '  उदुम्बरादयः — the country is named from the people and the\n'
        '  districts from the country, so the rule reaches a place\n'
        '  through two steps of naming. A kārikā lists the six.'
    ),
    '4.1.174': (
        'SETTLED — ते तद्राजाः. तद्राजप्रदेशाः — तद्राजस्य बहुषु\n'
        '  तेनैवास्त्रियाम् इत्येवमादयः, and 2.4.62 is where the name\n'
        '  is spent.\n'
        '\n'
        'SETTLED — AND THE PRONOUN REACHES BACK ONLY SO FAR, BECAUSE\n'
        '  A SECTION STOPS IT. जनपदशब्दात् क्षत्रियादञ् इत्येवमादयः\n'
        '  प्रत्ययाः सर्वनाम्ना प्रत्यवमृश्यन्ते **न तु पूर्वे,\n'
        '  गोत्रयुवसंज्ञाकाण्डेन व्यवहितत्वात्** — *those* takes in\n'
        '  the affixes from 4.1.168 and no earlier ones, because\n'
        '  4.1.162 to 4.1.167 stand between and separate them.\n'
        '\n'
        '  A BLOCK OF RULES ACTING AS A BARRIER. Anuvṛtti has been\n'
        '  stopped by a word at 3.4.99, read backward at 4.1.18 and\n'
        '  carried half-way at 4.1.27; this is the first time a whole\n'
        '  section has blocked a reference by standing in its path.'
    ),
    '4.1.175': (
        'SETTLED — कम्बोजाल्लुक्. The affix 4.1.168 gives is ELIDED: कम्बोजः,\n'
        '  and by कम्बोजादिभ्यो लुग्वचनं चोलाद्यर्थम् also चोलः,\n'
        '  केरलः, शकः, यवनः — country-names identical with the name\n'
        '  of the people, which is what the elision produces.'
    ),
    '4.1.176': (
        'SETTLED — अवन्तिकुन्तिकुरुभ्यश्च. The तद्राज affix goes in the\n'
        '  feminine: अवन्ती, कुन्ती, कुरूः. अवन्तिकुन्तिभ्यां ञ्यङः,\n'
        '  कुरोर्ण्यस्य — three words and two affixes.\n'
        '  स्त्रियामिति किम्? आवन्त्यः, कौन्त्यः, कौरव्यः.'
    ),
    '4.1.177': (
        'SETTLED — अतश्च. And any तद्राज affix in अ goes: शूरसेनी, मद्री,\n'
        '  दरत्. तकारो विस्पष्टार्थः, the त only for clarity.\n'
        '\n'
        'NOTE — अवन्त्यादिभ्यो लुग्वचनात् **तदन्तविधिरत्र नास्ति**:\n'
        '  because the rule before named particular words, this one\n'
        '  does not reach a compound through its last member —\n'
        "  आम्बष्ठ्या, सौवीर्या keep their affixes. A neighbour's\n"
        "  form deciding this rule's reach, which is what 4.1.139 did\n"
        '  from the other direction.'
    ),
    '4.1.178': (
        'SETTLED — न प्राच्यभर्गादियौधेयादिभ्यः. The elision is REFUSED:\n'
        '  पाञ्चाली, वैदेही, मागधी; भार्गी, कारूषी, कैकेयी;\n'
        '  यौधेयी, शौभ्रेयी, शौक्रेयी.\n'
        '\n'
        'SETTLED — AND THE REFUSAL IS READ AS EVIDENCE ABOUT A RULE\n'
        '  TWO CHAPTERS AWAY. कस्य पुनरकारस्य प्रत्ययस्य\n'
        '  यौधेयादिभ्यो लुक् प्राप्तः प्रतिषिध्यते? पाञ्चमिकस्याञः —\n'
        "  5.3.117's. कथं पुनस्तस्य भिन्नप्रकरणस्थस्यानेन लुक्\n"
        '  प्राप्नोति? **एतदेव विज्ञापयति** पाञ्चमिकस्यापि\n'
        '  तद्राजस्य अतश्च इत्यनेन लुग् भवतीति: a refusal here is the\n'
        '  proof that 4.1.177 reaches an affix given in अध्याय ५.\n'
        '\n'
        '  And the point of the proof is a third rule entirely:\n'
        '  पर्श्वाद्यणः स्त्रियां लुक् सिद्धो भवति — पर्शुः, रक्षाः,\n'
        '  असुरी. **यौधेयादिप्रतिषेधो ज्ञापकः पर्श्वाद्यणो लुगिति**.\n'
        '  A refusal in one chapter used to license an elision in\n'
        '  another, and the pāda ends on it.'
    ),
}

_BASE = ("4.1.1",)
_ENDINGS = ("4.1.2",)
_HEADING = ("4.1.3",)
_TADDHITA = ("4.1.76",)
_SAMARTHA = ("4.1.82",)
_DEFAULT = ("4.1.83",)
_PRAG = ("4.1.84", "4.1.85", "4.1.86", "4.1.87")
_LUK = ("4.1.88", "4.1.89", "4.1.90", "4.1.91")
_APATYA_SENSE = ("4.1.92",)
_NIYAMA = ("4.1.93", "4.1.94")
_FEM_LUK = ("4.1.109",)
_NAMES = tuple("4.1.%d" % n for n in range(162, 168))
_TADRAJA = ("4.1.174",)
_TADRAJA_LUK = ("4.1.176", "4.1.177", "4.1.178")
_APATYA = tuple(
    "4.1.%d" % n for n in
    list(range(95, 109)) + [110, 111] + list(range(112, 162))
    + list(range(168, 174)) + [175]
)

_NAMES_LINE = (
    'descendant_name(generation=..., elder_alive=..., elder=..., '
    'attitude=...) -> which of the two names a descendant bears, '
    'and on what.'
)

_TADRAJA_LINE = (
    'tadraja() -> the name the country-name affixes bear, and how '
    'far back the rule\'s pronoun reaches.'
)

_TADRAJA_LUK_LINE = (
    'tadraja_luk(feminine=..., of=..., affix=..., gana=...) -> '
    'whether the affix vanishes in the feminine, and by which rule.'
)

_APATYA_SENSE_LINE = (
    'apatya_sense(kind=...) -> the sense the whole run is stated '
    'in, and why the rule can name no affix.'
)

_NIYAMA_LINE = (
    'only_one(kind=..., feminine=...) -> how many affixes a lineage '
    'may take, and what the young-descendant affix is added to.'
)

_APATYA_LINE = (
    'apatya_affix(stem, gana=..., stem_final=..., marked=..., '
    'kind=..., among=..., wants=...) -> which affix names a '
    'descendant, and by which rule.'
)

_FEM_LUK_LINE = (
    'feminine_luk(among=...) -> whether the affix goes in the '
    'feminine, and which affix arrives once it has.'
)

_TADDHITA_LINE = (
    'taddhita_heading() -> what the name covers, how far it runs, and '
    'what its plural takes in.'
)

_SAMARTHA_LINE = (
    'samartha(position=..., connected=...) -> which of the connected '
    'words takes the affix, and what each of the heading\'s three '
    'words is for.'
)

_DEFAULT_LINE = (
    'default_affix() -> the affix that comes where no rule says '
    'otherwise, and how far the default runs.'
)

_PRAG_LINE = (
    'prag_divyatah_affix(of) -> which affix comes after a named stem '
    'in the senses that run to 4.4.2.'
)

_LUK_LINE = (
    'elision(of=..., gotra=..., before_ac=..., apatya=..., '
    'yuvan=...) -> whether a taddhita that would have come is '
    'dropped, and by which rule.'
)

_BASE_LINE = (
    'nominal_base(ngi=..., ap=..., pratipadika=...) -> what the '
    'heading covers, and the sūtra it runs to.'
)

_ENDINGS_LINE = (
    'sup_endings(name=...) -> the twenty-one case-endings, or one of '
    'the two pratyāhāras the rule cuts out of them.'
)

_HEADING_LINE = (
    'stri_heading() -> what the feminine heading covers, and why it '
    'takes only part of the heading above it.'
)

_STRI_LINE = (
    'stri_affix(stem, gana=..., stem_final=..., marked=..., '
    'sense=..., compound=..., samjna=..., chandasi=..., '
    'upasarjana=..., wants=...) -> which affix makes the stem '
    'feminine, and by which rule.'
)

#: 4.1.3's whole content is a statement ABOUT 4.1.1 — प्रातिपदिकमात्रम्
#: अत्र प्रकरणे संबध्यते, ङ्यापोरनेनैव विधानात् — so `stri_heading`
#: asks that rule what it governs and subtracts what this section
#: gives. The vṛtti's argument comes out as one set difference, and the
#: declaration is a call rather than a citation.
#:
#: 4.1.4 declared the same edge and did not earn it. The module DOES
#: build its inventory from 4.1.1's two class-words, but that happens
#: once at import and no call from `stri_affix` ever asks 4.1.1
#: anything: the dependency is the module's and not the rule's. The
#: reuse guard caught it, which is the second time it has caught a
#: declaration that was true of the file and false of the sūtra.
_REUSES = {
    "4.1.3": ("4.1.1",),
    # 4.1.84 to 4.1.87 are the exceptions to 4.1.83's default, and the
    # code says so by REACHING FOR IT: asked about a ground none of
    # them names, `prag_divyatah_affix` returns `default_affix`'s
    # answer. The relation between an अपवाद and its उत्सर्ग is not a
    # citation but a fall-through, and this is the first place in the
    # project where it could be written as one.
    "4.1.84": ("4.1.83",),
    "4.1.85": ("4.1.83",),
    "4.1.86": ("4.1.83",),
    "4.1.87": ("4.1.83",),
    # Same shape, one heading further on. Every rule of the patronymic
    # run is an exception to 4.1.83's default, and `apatya_affix`
    # reaches for it when none of them names the ground — so the
    # fall-through is the declaration, as it was at 4.1.84.
    "4.1.95": ("4.1.83",),
    "4.1.96": ("4.1.83",),
    "4.1.112": ("4.1.83",),
    "4.1.135": ("4.1.83",),
    "4.1.136": ("4.1.83",),
    "4.1.143": ("4.1.83",),
    "4.1.168": ("4.1.83",),
}

for _sutra, _notes in _RULES.items():
    if _sutra in _BASE:
        _apply, _line = nominal_base, _BASE_LINE
    elif _sutra in _ENDINGS:
        _apply, _line = sup_endings, _ENDINGS_LINE
    elif _sutra in _HEADING:
        _apply, _line = stri_heading, _HEADING_LINE
    elif _sutra in _TADDHITA:
        _apply, _line = taddhita_heading, _TADDHITA_LINE
    elif _sutra in _SAMARTHA:
        _apply, _line = samartha, _SAMARTHA_LINE
    elif _sutra in _DEFAULT:
        _apply, _line = default_affix, _DEFAULT_LINE
    elif _sutra in _PRAG:
        _apply, _line = prag_divyatah_affix, _PRAG_LINE
    elif _sutra in _LUK:
        _apply, _line = elision, _LUK_LINE
    elif _sutra in _APATYA_SENSE:
        _apply, _line = apatya_sense, _APATYA_SENSE_LINE
    elif _sutra in _NIYAMA:
        _apply, _line = only_one, _NIYAMA_LINE
    elif _sutra in _FEM_LUK:
        _apply, _line = feminine_luk, _FEM_LUK_LINE
    elif _sutra in _NAMES:
        _apply, _line = descendant_name, _NAMES_LINE
    elif _sutra in _TADRAJA:
        _apply, _line = tadraja, _TADRAJA_LINE
    elif _sutra in _TADRAJA_LUK:
        _apply, _line = tadraja_luk, _TADRAJA_LUK_LINE
    elif _sutra in _APATYA:
        _apply, _line = apatya_affix, _APATYA_LINE
    else:
        _apply, _line = stri_affix, _STRI_LINE
    register(
        _sutra,
        apply=_apply,
        codification=_line,
        notes=_notes,
        reuses=_REUSES.get(_sutra, ()),
    )
