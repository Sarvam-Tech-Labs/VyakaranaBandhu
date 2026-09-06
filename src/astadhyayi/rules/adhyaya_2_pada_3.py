# -*- coding: utf-8 -*-
r"""अध्याय २, पाद ३ — which case-ending a kāraka takes."""

from __future__ import annotations

from src.astadhyayi.karakavibhakti import amantrita, vibhakti_for
from src.astadhyayi.sources import register

_CODIFICATION = (
    "vibhakti_for(karaka, expressed_by=..., ...) -> which case-ending and "
    "by which rule, or why none is given."
)

_VIBHAKTI = {
    "2.3.1": (
        'SETTLED — an अधिकार over everything that follows: यद् इत ऊर्ध्वम्\n'
        '  अनुक्रमिष्यामः अनभिहिते इत्येवं तद् वेदितव्यम्. A kāraka takes\n'
        '  an ending only where nothing has said it already.\n'
        '\n'
        'SETTLED — and the list of what can say it is CLOSED:\n'
        '  तिङ्कृत्तद्धितसमासैः परिसंख्यानम्. Four, and the Kāśikā gives\n'
        '  one counter for each — क्रियते कटः, कृतः कटः, शत्यः,\n'
        '  प्राप्तोदको ग्रामः. Being a परिसंख्या it is a tuple here and\n'
        '  not a flag, and a fifth name is refused rather than accepted.\n'
        '\n'
        'SETTLED — this is where two halves of the grammar meet. 1.4.23 to\n'
        '  1.4.55 decide WHICH kāraka a participant is, and they are\n'
        '  codified; these rules take that answer and give it an ending.\n'
        '  The kāraka is passed through rather than worked out again.'
    ),
    "2.3.2": (
        'SETTLED — कर्मणि द्वितीया: कटं करोति, ग्रामं गच्छति. Which\n'
        '  participant is the कर्म is 1.4.49 कर्तुरीप्सिततमं कर्म.\n'
        '\n'
        'SCOPE — the vārttikas admitting उभयतः, सर्वतः, धिक्, उपरि,\n'
        '  अभितः, परितः and the rest — उभयतो ग्रामम्, धिग् देवदत्तम् —\n'
        '  are not modelled. They give a second where there is no कर्म at\n'
        '  all, which is a different rule wearing the same ending.'
    ),
    "2.3.3": (
        'SETTLED — तृतीया च होश्छन्दसि: in the Veda the object of हु takes\n'
        '  a third, and the च keeps the second beside it — यवाग्वा\n'
        '  अग्निहोत्रं जुहोति and यवागूम् अग्निहोत्रं जुहोति both stand.\n'
        '\n'
        'SETTLED — छन्दसीति किम्? outside the Veda only the second.'
    ),
    "2.3.4": (
        'SETTLED — अन्तराऽन्तरेण युक्ते: अन्तरा त्वां च मां च कमण्डलुः,\n'
        '  अन्तरेण पुरुषकारं न किंचिल् लभ्यते. The two words differ in\n'
        '  sense — अन्तरा is what lies between, अन्तरेण is that and also\n'
        '  "without" — and the sūtra takes them together साहचर्यात्.\n'
        '\n'
        'SETTLED — षष्ठ्यपवादोऽयं योगः: it displaces a genitive.\n'
        '\n'
        'SETTLED — युक्तग्रहणं किम्? अन्तरा तक्षशिलां च पाटलिपुत्रं च\n'
        '  स्रुघ्नस्य प्राकारः — there the words are not construed with it.'
    ),
    "2.3.5": (
        'SETTLED — कालाध्वनोरत्यन्तसंयोगे: मासमधीते, क्रोशं कुटिला नदी.\n'
        '  क्रियागुणद्रव्यैः साकल्येन कालाध्वनोः संबन्धोऽत्यन्तसंयोगः —\n'
        '  the whole stretch taken up, by an act, a quality or a thing.\n'
        '\n'
        'SETTLED — अत्यन्तसंयोग इति किम्? मासस्य द्विरधीते, क्रोशस्यैकदेशे\n'
        '  पर्वतः — part of the stretch, and the ending is not this one.'
    ),
    "2.3.6": (
        'SETTLED — अपवर्गे तृतीया: मासेनानुवाकोऽधीतः. अपवर्गः फलप्राप्तौ\n'
        '  सत्यां क्रियापरिसमाप्तिः — the act carried through AND its\n'
        '  result got.\n'
        '\n'
        'SETTLED — अपवर्ग इति किम्? मासमधीतः, and the Kāśikā presses the\n'
        '  point: मासमधीतोऽनुवाकः, न चानेन गृहीतः — read for a month and\n'
        '  not learnt, so no third.'
    ),
    "2.3.7": (
        'SETTLED — सप्तमीपञ्चम्यौ कारकमध्ये: अद्य भुक्त्वा देवदत्तो द्व्यहे\n'
        '  भोक्ता, द्व्यहाद् वा भोक्ता; इहस्थोऽयम् इष्वासः क्रोशे लक्ष्यं\n'
        '  विध्यति, क्रोशाल् लक्ष्यं विध्यति.\n'
        '\n'
        'SETTLED — संख्यातानुदेशो न भवति, अस्वरितत्वात्. The two endings\n'
        '  are NOT paired off one each against कालाध्वनोः: either may go\n'
        '  with either, and the reason given is that the sūtra carries no\n'
        '  svarita — 1.3.10 यथासंख्यम् needs one.'
    ),
    "2.3.8": (
        'SETTLED — कर्मप्रवचनीययुक्ते द्वितीया: शाकल्यस्य संहितामनु\n'
        '  प्रावर्षत्. Which particles are कर्मप्रवचनीय is 1.4.83 to\n'
        '  1.4.98, and 1.4.84 अनुर्लक्षणे is the one at work here.'
    ),
    "2.3.9": (
        'SETTLED — यस्मादधिकं यस्य चेश्वरवचनं तत्र सप्तमी: उप खार्यां\n'
        '  द्रोणः, a droṇa over and above a khārī.\n'
        '\n'
        'SETTLED — यस्य चेश्वरवचनम् covers owner and owned BOTH, and\n'
        '  either may take the seventh: अधि ब्रह्मदत्ते पञ्चालाः beside\n'
        '  अधिपञ्चालेषु ब्रह्मदत्तः.\n'
        '\n'
        'SETTLED — द्वितीयापवादो योगः: it displaces 2.3.8.'
    ),
    "2.3.10": (
        'SETTLED — पञ्चम्यपाङ्परिभिः: अप त्रिगर्तेभ्यो वृष्टो देवः, आ\n'
        '  पाटलिपुत्राद् वृष्टो देवः.\n'
        '\n'
        'SETTLED — परि is admitted only in the sense of exclusion, and\n'
        '  the reason is its company: अपेन साहचर्यात् परेर् वर्जनार्थस्य\n'
        '  ग्रहणम्. So वृक्षं परि विद्योतते विद्युत् — lightning flashing\n'
        '  ROUND a tree, 1.4.90 — keeps its second.'
    ),
    "2.3.11": (
        'SETTLED — प्रतिनिधिप्रतिदाने च यस्मात्: मुख्यसदृशः प्रतिनिधिः,\n'
        '  दत्तस्य प्रतिनिर्यातनं प्रतिदानम्. अभिमन्युरर्जुनतः प्रति;\n'
        '  माषानस्मै तिलेभ्यः प्रति यच्छति.\n'
        '\n'
        'SETTLED — the Kāśikā raises an objection and answers it: the\n'
        '  sūtra says the substitution is with a karmapravacanīya, not\n'
        '  that the thing replaced is — नैष दोषः, संबन्धसंबन्धात्.'
    ),
    "2.3.12": (
        'SETTLED — गत्यर्थकर्मणि द्वितीयाचतुर्थ्यौ चेष्टायामनध्वनि:\n'
        '  ग्रामं गच्छति beside ग्रामाय गच्छति.\n'
        '\n'
        'SETTLED — four conditions and the Kāśikā tests each.\n'
        '  गत्यर्थग्रहणं किम्? ओदनं पचति. कर्मणीति किम्? अश्वेन व्रजति.\n'
        '  चेष्टायामिति किम्? मनसा पाटलिपुत्रं गच्छति — the mind travels\n'
        '  and the body does not. अनध्वनीति किम्? अध्वानं गच्छति, and\n'
        '  अध्वनीत्यर्थग्रहणम्, so पन्थानम् and मार्गम् are out too.'
    ),
    "2.3.13": (
        'SETTLED — चतुर्थी सम्प्रदाने: उपाध्यायाय गां ददाति, देवदत्ताय\n'
        '  रोचते. Which participant is the सम्प्रदान is 1.4.32 कर्मणा यम्\n'
        '  अभिप्रैति स सम्प्रदानम्.\n'
        '\n'
        'SCOPE — three vārttikas widen it and none is modelled:\n'
        '  तादर्थ्ये (यूपाय दारु, which 2.1.36 also compounds),\n'
        '  क्ऌपिसंपद्यमाने (मूत्राय कल्पते यवागूः), and उत्पातेन\n'
        '  ज्ञाप्यमाने. Each gives a fourth where there is no सम्प्रदान,\n'
        '  so they are additions to the ending rather than to the kāraka.'
    ),
    "2.3.14": (
        'SETTLED — क्रियार्थोपपदस्य च कर्मणि स्थानिनः: where a verb of\n'
        '  purpose stands as उपपद and the verb it belongs to is not\n'
        '  spoken, what THAT verb would have reached takes a fourth.\n'
        '  एधेभ्यो व्रजति — goes for firewood, the fetching unspoken.\n'
        '  द्वितीयापवादो योगः.\n'
        '\n'
        'SETTLED — क्रियार्थोपपदस्येति किम्? प्रविश पिण्डीम् — there the\n'
        '  unspoken verb is eating and no purpose-verb stands beside it.'
    ),
    "2.3.15": (
        'SETTLED — तुमर्थाच्च भाववचनात्: पाकाय व्रजति, भूतये व्रजति.\n'
        '  तुमुना समानार्थस्तुमर्थः — a noun meaning what तुमुन् means.\n'
        '\n'
        'SETTLED — two counters, one per word. तुमर्थादिति किम्? पाकः,\n'
        '  त्यागः — the bare noun, no purpose. भाववचनादिति किम्?\n'
        '  कारको व्रजति — that names a doer, not an act.'
    ),
    "2.3.16": (
        'SETTLED — नमःस्वस्तिस्वाहास्वधालंवषड्योगाच्च: नमो देवेभ्यः,\n'
        '  स्वस्ति प्रजाभ्यः, स्वाहा अग्नये, स्वधा पितृभ्यः, वषडग्नये.\n'
        '\n'
        'SETTLED — अलमिति पर्याप्त्यर्थग्रहणम्: the word is taken in the\n'
        '  sense of sufficiency and not by its form, so प्रभुर्मल्लो\n'
        '  मल्लाय and शक्तो मल्लो मल्लाय take the fourth too. Codified —\n'
        '  a sense-reading admits words the list does not name.'
    ),
    "2.3.17": (
        'SETTLED — मन्यकर्मण्यनादरे विभाषाऽप्राणिषु: न त्वा तृणं मन्ये\n'
        '  beside न त्वा तृणाय मन्ये. अनादरस्तिरस्कारः.\n'
        '\n'
        'SETTLED — three conditions and the Kāśikā tests each.\n'
        '  मन्यतिग्रहणं किम्? न त्वा तृणं चिन्तयामि. अनादर इति किम्? the\n'
        '  verse अश्मानं दृषदं मन्ये, where nothing is being belittled.\n'
        '  अप्राणिषु — the thing thought little of must not be alive.\n'
        '\n'
        'SETTLED — विकरणनिर्देशः: the sūtra says मन्य and not मन्, which\n'
        '  keeps out न त्वा तृणं मन्वे, the same root in another class.'
    ),
    "2.3.18": (
        'SETTLED — कर्तृकरणयोस्तृतीया: देवदत्तेन कृतम्, दात्रेण लुनाति,\n'
        '  परशुना छिनत्ति. Which participant is कर्तृ or करण is 1.4.54\n'
        '  and 1.4.42, both codified.\n'
        '\n'
        'SCOPE — तृतीयाविधाने प्रकृत्यादिभ्य उपसंख्यानम् adds a third\n'
        '  where there is neither doer nor tool — प्रकृत्याभिरूपः,\n'
        '  प्रायेण याज्ञिकः, गार्ग्योऽस्मि गोत्रेण, द्विद्रोणेन धान्यं\n'
        '  क्रीणाति. Recorded, not modelled: it is a list and not a rule.'
    ),
    "2.3.19": (
        'SETTLED — सहयुक्तेऽप्रधाने: पुत्रेण सहागतः पिता. The father is\n'
        '  what the sentence speaks of and the son is only understood —\n'
        '  पितुरत्र क्रियादिसंबन्धः शब्देनोच्यते, पुत्रस्य तु\n'
        '  प्रतीयमानः — so the son is the अप्रधान and takes the third.\n'
        '\n'
        'SETTLED — the rule is worded by SENSE, सहार्थेन, so सार्धम्\n'
        '  serves as well as सह; and 1.2.65 shows it working with no\n'
        '  such word present at all.\n'
        '\n'
        'SETTLED — अप्रधान इति किम्? शिष्येण सहोपाध्यायस्य गौः.'
    ),
    "2.3.20": (
        'SETTLED — येनाङ्गविकारः: अक्ष्णा काणः, पादेन खञ्जः, पाणिना\n'
        '  कुण्ठः. अङ्ग here is the body entire and येन picks out the\n'
        '  part — अवयवधर्मेण समुदायो व्यपदिश्यते, the whole named by\n'
        '  what is true of a piece of it.\n'
        '\n'
        'SETTLED — अङ्गविकार इति किम्? अक्षि काणमस्य — the eye itself\n'
        '  being called blind, and no third.\n'
        '\n'
        'SETTLED — and अक्ष्णा काणः is the same example 2.1.30 uses as\n'
        '  its counter: blind IN the eye, not blinded BY it. The two\n'
        '  sūtras look at the one phrase from opposite ends.'
    ),
    "2.3.21": (
        'SETTLED — इत्थंभूतलक्षणे: अपि भवान् कमण्डलुना छात्रम्\n'
        '  अद्राक्षीत्, शिखया परिव्राजकम्. कञ्चित् प्रकारं प्राप्त\n'
        '  इत्थंभूतः — someone in some state, known by a mark.\n'
        '\n'
        'SETTLED — not where the mark is already inside a compound:\n'
        '  कमण्डलुपाणिश्छात्रः, लक्षणस्य समासेऽन्तर्भूतत्वात्.'
    ),
    "2.3.22": (
        'SETTLED — संज्ञोऽन्यतरस्यां कर्मणि: पित्रा संजानीते beside\n'
        '  पितरं संजानीते. सम् + ज्ञा only, and the option is against\n'
        '  the second 2.3.2 would else have given.'
    ),
    "2.3.23": (
        'SETTLED — हेतौ: धनेन कुलम्, कन्यया शोकः, विद्यया यशः.\n'
        '  फलसाधनयोग्यः पदार्थो लोके हेतुरुच्यते — what is fit to bring\n'
        '  a result about.\n'
        '\n'
        'SETTLED — and it heads a run of four. 2.3.24 takes a debt out\n'
        '  of it into the fifth, 2.3.25 makes a quality optional, and\n'
        '  2.3.26 sends it to the sixth where the word हेतु is used.'
    ),
    "2.3.24": (
        'SETTLED — अकर्तर्यृणे पञ्चमी: शताद् बद्धः, सहस्राद् बद्धः.\n'
        '  तृतीयापवादो योगः — it takes the debt out of 2.3.23.\n'
        '\n'
        'SETTLED — अकर्तरीति किम्? शतेन बन्धितः, and the Kāśikā explains\n'
        '  why the same hundred changes case: प्रयोजकत्वाच्च\n'
        '  कर्तृसंज्ञकम् — there it is what SET the binding going, so it\n'
        '  is a कर्तृ and 2.3.18 gives it a third.'
    ),
    "2.3.25": (
        'SETTLED — विभाषा गुणेऽस्त्रियाम्: जाड्याद् बद्धः beside जाड्येन\n'
        '  बद्धः; पाण्डित्याद् मुक्तः beside पाण्डित्येन मुक्तः.\n'
        '\n'
        'SETTLED — two counters. गुणग्रहणं किम्? धनेन कुलम् — wealth is\n'
        '  no quality. अस्त्रियामिति किम्? बुद्ध्या मुक्तः, प्रज्ञया\n'
        '  मुक्तः — feminine, and only the third stands.'
    ),
    "2.3.26": (
        'SETTLED — षष्ठी हेतुप्रयोगे: अन्नस्य हेतोर् वसति. Where the\n'
        '  word हेतु is itself used, the cause takes a sixth, and the\n'
        '  last of the four हेतु rules.'
    ),
    "2.3.27": (
        'SETTLED — सर्वनाम्नस्तृतीया च: with a PRONOUN the cause may take\n'
        '  a third as well as the sixth 2.3.26 gives — केन हेतुना वसति\n'
        '  beside कस्य हेतोर् वसति.\n'
        '\n'
        'SCOPE — निमित्तकारणहेतुषु सर्वासां प्रायदर्शनम्: with निमित्त\n'
        '  and कारण every case is met with — किं निमित्तम्, केन\n'
        '  निमित्तेन, कस्मै निमित्ताय. Recorded, not modelled.'
    ),
    "2.3.28": (
        'SETTLED — अपादाने पञ्चमी: ग्रामादागच्छति, पर्वतादवरोहति,\n'
        '  वृकेभ्यो बिभेति. Which participant is अपादान is 1.4.24\n'
        '  ध्रुवमपायेऽपादानम्, codified.\n'
        '\n'
        'SCOPE — three vārttikas add a fifth where there is no अपादान:\n'
        '  ल्यब्लोपे (प्रासादात् प्रेक्षते), अधिकरणे (आसनात् प्रेक्षते),\n'
        '  and प्रश्नाख्यानयोः. Not modelled.'
    ),
    "2.3.29": (
        'SETTLED — अन्यारादितरर्तेदिक्शब्दाञ्चूत्तरपदाजाहियुक्ते: eight\n'
        '  words, and अन्यो देवदत्तात् is the plain case.\n'
        '\n'
        'SETTLED — अन्य इत्यर्थग्रहणम्, so words of its SENSE come with\n'
        '  it: भिन्नो देवदत्तात्, अर्थान्तरं देवदत्तात्, विलक्षणो\n'
        '  देवदत्तात्. Codified, since a sense-reading admits words the\n'
        '  sūtra does not name.'
    ),
    "2.3.30": (
        'SETTLED — षष्ठ्यतसर्थप्रत्ययेन: with an affix meaning what\n'
        '  अतसुच् means, by 5.3.28 — दक्षिणतो ग्रामस्य, पुरस्ताद्\n'
        '  ग्रामस्य, उपरिष्टाद् ग्रामस्य.'
    ),
    "2.3.31": (
        'SETTLED — एनपा द्वितीया: दक्षिणेन ग्रामम्, and it displaces the\n'
        '  sixth 2.3.30 would have given.\n'
        '\n'
        'SETTLED — षष्ठ्यपीष्यते: the sixth is wanted too — दक्षिणेन\n'
        '  ग्रामस्य — and the Kāśikā gets it by splitting the sūtra,\n'
        '  तदर्थं योगविभागः कर्तव्यः. Both are reported.'
    ),
    "2.3.32": (
        'SETTLED — पृथग्विनानानाभिस्तृतीयाऽन्यतरस्याम्: a third or a\n'
        '  fifth — पृथग् देवदत्तेन beside पृथग् देवदत्तात्.\n'
        '\n'
        'SCOPE — a योगविभाग admits a second as well, and the Kāśikā\n'
        '  quotes verse for it — विना वातं विना वर्षम्. Recorded.'
    ),
    "2.3.33": (
        'SETTLED — करणे च स्तोकाल्पकृच्छ्रकतिपयस्यासत्त्ववचनस्य: a fifth\n'
        '  beside the third — स्तोकाद् मुक्तः beside स्तोकेन मुक्तः.\n'
        '  पञ्चम्यत्र पक्षे विधीयते, तृतीया तु करण इत्येव सिद्धा — the\n'
        '  third was already there and the fifth is what this adds.\n'
        '\n'
        'SETTLED — असत्त्ववचनस्य: only where a QUALITY is meant as the\n'
        '  means and no substance — यदा धर्ममात्रं करणतया विवक्ष्यते न\n'
        '  द्रव्यम्.'
    ),
    "2.3.34": (
        'SETTLED — दूरान्तिकार्थैः षष्ठ्यन्यतरस्याम्: दूरं ग्रामस्य\n'
        '  beside दूरं ग्रामात्. अन्यतरस्यांग्रहणं पञ्चम्यर्थम् — the\n'
        '  option is there for the fifth, इतरथा हि तृतीया पक्षे स्यात्.\n'
        '\n'
        'SETTLED — and with 2.3.35 and 2.3.36 these words take FOUR cases\n'
        '  besides: दूरान्तिकार्थेभ्यश् चतस्रो विभक्तयो भवन्ति —\n'
        '  द्वितीयातृतीयापञ्चमीसप्तम्यः. A field holding one alternative\n'
        '  could not say that, so it holds a tuple.'
    ),
    "2.3.35": (
        'SETTLED — दूरान्तिकार्थेभ्यो द्वितीया च: दूरं ग्रामस्य, दूराद्\n'
        '  ग्रामस्य, दूरेण ग्रामस्य — the च bringing a fifth and a third\n'
        '  in with the second.\n'
        '\n'
        'SETTLED — प्रातिपदिकार्थे विधानम्, and असत्त्ववचनग्रहणं च\n'
        '  अनुवर्तते: the far-and-near word must not name a substance.'
    ),
    "2.3.36": (
        'SETTLED — सप्तम्यधिकरणे च: कटे आस्ते, स्थाल्यां पचति. Which\n'
        '  participant is अधिकरण is 1.4.45 आधारोऽधिकरणम्, codified.\n'
        '\n'
        'SETTLED — the च adds the far-and-near words: दूरे ग्रामस्य,\n'
        '  अन्तिके ग्रामस्य, and that is the fourth of their four cases.'
    ),
    "2.3.37": (
        'SETTLED — यस्य च भावेन भावलक्षणम्: गोषु दुह्यमानासु गतः, went\n'
        '  while the cows were being milked. भावः क्रिया, and प्रसिद्धा\n'
        '  च क्रिया क्रियान्तरं लक्षयति — only a known act can mark\n'
        '  another.\n'
        '\n'
        'SETTLED — भावेनेति किम्? यो जटाभिः, स भुङ्क्ते: matted hair is\n'
        '  no act, and marks nothing.'
    ),
    "2.3.38": (
        'SETTLED — षष्ठी चानादरे: रुदतः प्राव्राजीत् beside रुदति\n'
        '  प्राव्राजीत् — went forth though the man wept, and the\n'
        '  weeping was disregarded. क्रोशन्तम् अनादृत्य प्रव्रजितः.'
    ),
    "2.3.39": (
        'SETTLED — स्वामीश्वराधिपतिदायादसाक्षिप्रतिभूप्रसूतैश्च: seven\n'
        '  words, and each takes a sixth or a seventh — गवां स्वामी\n'
        '  beside गोषु स्वामी, गवां साक्षी beside गोषु साक्षी.'
    ),
    "2.3.40": (
        'SETTLED — आयुक्तकुशलाभ्यां चासेवायाम्: आयुक्तो व्यापारितः,\n'
        '  कुशलो निपुणः. आयुक्तः कटकरणस्य beside आयुक्तः कटकरणे, where\n'
        '  आसेवा तात्पर्यम् — habitual application is meant.\n'
        '\n'
        'SETTLED — आसेवायामिति किम्? आयुक्तो गौः शकटे: an ox harnessed to\n'
        '  a cart is simply in a place, and the seventh there is\n'
        '  2.3.36\'s अधिकरण and not this rule\'s.'
    ),
    "2.3.41": (
        'SETTLED — यतश्च निर्धारणम्: मनुष्याणां क्षत्रियः शूरतमः beside\n'
        '  मनुष्येषु क्षत्रियः शूरतमः. जातिगुणक्रियाभिः समुदायाद्\n'
        '  एकदेशस्य पृथक्करणं निर्धारणम् — the same definition 2.2.10\n'
        '  uses, and that sūtra is why this genitive never compounds.'
    ),
    "2.3.42": (
        'SETTLED — पञ्चमी विभक्ते: माथुराः पाटलिपुत्रकेभ्यः सुकुमारतराः.\n'
        '  षष्ठीसप्तम्यपवादो योगः — it takes the comparing case out of\n'
        '  2.3.41, where the singling-out is between two groups.'
    ),
    "2.3.43": (
        'SETTLED — साधुनिपुणाभ्यामर्चायां सप्तम्यप्रतेः: मातरि साधुः,\n'
        '  पितरि निपुणः.\n'
        '\n'
        'SETTLED — two counters, one per condition. अर्चायामिति किम्?\n'
        '  साधुर्भृत्यो राज्ञः — तत्त्वकथने न भवति, plain statement and\n'
        '  no praise. अप्रतेरिति किम्? साधुर्देवदत्तो मातरं प्रति.'
    ),
    "2.3.44": (
        'SETTLED — प्रसितोत्सुकाभ्यां तृतीया च: केशैः प्रसितः beside\n'
        '  केशेषु प्रसितः, and the same for उत्सुक. प्रसितः प्रसक्तः,\n'
        '  यस्तत्र नित्यमेवावबद्धः — one bound up in a thing for good.'
    ),
    "2.3.45": (
        'SETTLED — नक्षत्रे च लुपि: पुष्येण पायसमश्नीयात् beside पुष्ये.\n'
        '\n'
        'SETTLED — two counters. नक्षत्र इति किम्? पञ्चालेषु वसति.\n'
        '  लुपीति किम्? मघासु ग्रहः — no लुप् there, and the seventh is\n'
        '  an ordinary अधिकरण.'
    ),
    "2.3.46": (
        'SETTLED — प्रातिपदिकार्थलिङ्गपरिमाणवचनमात्रे प्रथमा: the first\n'
        '  case where nothing beyond the stem\'s own meaning is meant,\n'
        '  or its gender, or its measure, or its number.\n'
        '  प्रातिपदिकार्थः सत्ता — the stem-meaning is bare existence.\n'
        '\n'
        'SETTLED — मात्रशब्दः प्रत्येकमभिसंबध्यते: the word मात्र\n'
        '  attaches to each of the four, so it is "nothing but" in every\n'
        '  one of them. That is why anything ADDED — a kāraka, an\n'
        '  address — takes the case away from this rule.'
    ),
    "2.3.47": (
        'SETTLED — सम्बोधने च: हे देवदत्त, हे देवदत्तौ, हे देवदत्ताः.\n'
        '\n'
        'SETTLED — and the Kāśikā says why the sūtra is needed at all:\n'
        '  आभिमुख्यकरणं संबोधनम्, तदधिके प्रातिपदिकार्थे प्रथमा न\n'
        '  प्राप्नोति — calling out ADDS something to the bare\n'
        '  stem-meaning, and 2.3.46 says मात्र, nothing but.'
    ),
    "2.3.48": (
        'SETTLED — सामन्त्रितम्: the first-case form used in calling out\n'
        '  is named आमन्त्रित. It gives no ending; 2.3.47 has already\n'
        '  given one.\n'
        '\n'
        'PENDING — the name is wanted for what other rules do with it,\n'
        '  and none of them is codified: 8.1.72 आमन्त्रितं\n'
        '  पूर्वमविद्यमानवत् treats a preceding आमन्त्रित as though it\n'
        '  were not there. What is held here is the name.'
    ),
    "2.3.49": (
        'SETTLED — एकवचनं संबुद्धिः: the SINGULAR of that आमन्त्रित\n'
        '  bears a further name — हे पटो, हे देवदत्त.\n'
        '\n'
        'PENDING — 6.1.69 एङ्ह्रस्वात् संबुद्धेः drops the ending of a\n'
        '  संबुद्धि, which is what हे पटो shows, and it is not codified.'
    ),
    "2.3.50": (
        'SETTLED — षष्ठी शेषे, and शेष is defined by subtraction:\n'
        '  कर्मादिभ्योऽन्यः प्रातिपदिकार्थव्यतिरिक्तः\n'
        '  स्वस्वामिसंबन्धादिः शेषः — whatever relation is left when\n'
        '  every kāraka has been taken and the bare stem-meaning too.\n'
        '  राज्ञः पुरुषः, पशोः पादः, पितुः पुत्रः.\n'
        '\n'
        'SETTLED — asked LAST in the resolver, and it has to be: a\n'
        '  remainder cannot be computed before the things it is the\n'
        '  remainder of. Same shape as 2.2.23 शेषो बहुव्रीहिः.\n'
        '\n'
        'SETTLED — and this is the genitive 2.2.8 compounds, which is why\n'
        '  राजपुरुषः is the stock example of both sūtras.'
    ),
    "2.3.51": (
        'SETTLED — ज्ञोऽविदर्थस्य करणे: सर्पिषो जानीते, and it is the\n'
        '  INSTRUMENT that takes the sixth — सर्पिषा करणेन प्रवर्तते.\n'
        '\n'
        'OPEN — what अविदर्थ excludes. The Kāśikā gives two readings and\n'
        '  chooses neither: प्रवृत्तिवचनो जानातिरविदर्थः, the verb of\n'
        '  setting about a thing; अथ वा मिथ्याज्ञानवचनः, the verb of\n'
        '  mistaken apprehension. Both are recorded and neither is taken.'
    ),
    "2.3.52": (
        'SETTLED — अधीगर्थदयेशां कर्मणि: मातुरध्येति, मातुः स्मरति,\n'
        '  सर्पिषो दयते, सर्पिष ईष्टे. अधीगर्थाः स्मरणार्थाः.\n'
        '\n'
        'SETTLED — शेषत्वेन विवक्षिते, and both counters turn on it.\n'
        '  कर्मणीति किम्? मातुर्गुणैः स्मरति. शेष इत्येव — मातरं स्मरति\n'
        '  stands too, where the object is meant AS an object.'
    ),
    "2.3.53": (
        'SETTLED — कृञः प्रतियत्ने: सतो गुणान्तराधानं प्रतियत्नः, adding\n'
        '  a quality to what already exists. एधोदकस्योपस्कुरुते.\n'
        '\n'
        'SETTLED — three counters. प्रतियत्न इति किम्? कटं करोति — that\n'
        '  makes the mat rather than improving it. कर्मणीति किम्?\n'
        '  एधोदकस्योपस्कुरुते प्रज्ञया. शेष इत्येव — एधोदकमुपस्कुरुते.'
    ),
    "2.3.54": (
        'SETTLED — रुजार्थानां भाववचनानामज्वरेः: चौरस्य रुजति रोगः,\n'
        '  चौरस्यामयत्यामयः. ज्वर् is excepted by name.\n'
        '\n'
        'SETTLED — भाववचनानाम् narrows it to verbs whose subject is the\n'
        '  action itself, भावकर्तृकाणाम्.'
    ),
    "2.3.55": (
        'SETTLED — आशिषि नाथः: सर्पिषो नाथते, मधुनो नाथते. The\n'
        '  dhātupāṭha gives नाथृ नाधृ याच्ञोपतापैश्वर्याशीःषु and this\n'
        '  takes the आशीस् sense only.\n'
        '\n'
        'SETTLED — आशिषीति किम्? माणवकमुपनाथति.'
    ),
    "2.3.56": (
        'SETTLED — जासिनिप्रहणनाटक्राथपिषां हिंसायाम्: चौरस्योज्जासयति,\n'
        '  वृषलस्योज्जासयति.\n'
        '\n'
        'SETTLED — and the Kāśikā picks the root out of the dhātupāṭha by\n'
        '  hand: the चुरादि जसु हिंसायाम् and जसु ताडने, न दैवादिकस्य\n'
        '  जसु मोक्षणे. Two roots spelt the same, and only one is meant.'
    ),
    "2.3.57": (
        'SETTLED — व्यवहृपणोः समर्थयोः: शतस्य व्यवहरति, शतस्य पणते.\n'
        '  समर्थयोः means समानार्थयोः — the two verbs are taken only\n'
        '  where they mean the same, द्यूते क्रयविक्रयव्यवहारे च.\n'
        '\n'
        'SETTLED — and the Kāśikā heads off a question about the other\n'
        '  पण्: स्तुत्यर्थस्य पणतेराय्प्रत्यय इष्यते, the one meaning\n'
        '  praise takes आय and is not this.'
    ),
    "2.3.58": (
        'SETTLED — दिवस्तदर्थस्य: शतस्य दीव्यति. दिव् in the sense\n'
        '  व्यवहृ and पण् share at 2.3.57, and its object takes a sixth.\n'
        '\n'
        'SETTLED — तदर्थस्येति किम्? ब्राह्मणं दीव्यति, and 2.3.2 gives\n'
        '  the second. योगविभाग उत्तरार्थः — the split is made for the\n'
        '  sūtras that follow.'
    ),
    "2.3.59": (
        'SETTLED — विभाषोपसर्गे: with a preverb the sixth 2.3.58 made\n'
        '  invariable becomes a choice — शतस्य प्रतिदीव्यति beside शतं\n'
        '  प्रतिदीव्यति.'
    ),
    "2.3.60": (
        'SETTLED — द्वितीया ब्राह्मणे: a second in the Brāhmaṇa texts,\n'
        '  where 2.3.58 would have given a sixth.\n'
        '\n'
        'SETTLED — the Kāśikā notes the rule is for the preverb-less\n'
        '  case: सोपसर्गस्य तु छन्दसि व्यवस्थितविभाषयापि सिध्यति.'
    ),
    "2.3.61": (
        'SETTLED — प्रेष्यब्रुवोर्हविषो देवतासम्प्रदाने: the OBLATION\n'
        '  takes a sixth at the call — अग्नये छागस्य हविषो वपाया मेदसः\n'
        '  प्रेष्य.\n'
        '\n'
        'SETTLED — प्रेष्य is picked out precisely: इष्यतेर्दैवादिकस्य\n'
        '  लोण्मध्यमपुरुषस्यैकवचनम्, one form of one root in one class,\n'
        '  and ब्रू is taken in the same setting साहचर्यात्.'
    ),
    "2.3.62": (
        'SETTLED — चतुर्थ्यर्थे बहुलं छन्दसि: in the Veda a sixth stands\n'
        '  where a fourth is meant. पुरुषमृगश्चन्द्रमसः for चन्द्रमसे.\n'
        '\n'
        'SETTLED — बहुलग्रहणं किम्? कृष्णो रात्र्यै — the fourth stands\n'
        '  there, so the बहुल is what admits both.'
    ),
    "2.3.63": (
        'SETTLED — यजेश्च करणे: in the Veda the INSTRUMENT of यज् takes a\n'
        '  sixth — घृतस्य यजते beside घृतेन यजते, सौम्यस्य यजते beside\n'
        '  सोमेन यजते.'
    ),
    "2.3.64": (
        'SETTLED — कृत्वोऽर्थप्रयोगे कालेऽधिकरणे: पञ्चकृत्वोऽह्नो\n'
        '  भुङ्क्ते, द्विरह्नोऽधीते.\n'
        '\n'
        'SETTLED — two counters. कृत्वोऽर्थग्रहणं किम्? अह्नि शेते.\n'
        '  प्रयोगग्रहणं किम्? अहनि भुक्तम् — the sense is there but the\n'
        '  affix is not used, and the rule wants the affix.'
    ),
    "2.3.65": (
        'SETTLED — कर्तृकर्मणोः कृति: भवतः शायिका for the doer, अपां\n'
        '  स्रष्टा and पुरां भेत्ता for the object.\n'
        '\n'
        'SETTLED — कर्तृकर्मणोरिति किम्? शस्त्रेण भेत्ता — an instrument\n'
        '  is neither. कृतीति किम्? तद्धितप्रयोगे मा भूत्.\n'
        '\n'
        'SETTLED — and this is the genitive 2.2.15 and 2.2.16 forbid to\n'
        '  compound. One pāda gives the case, the pāda before it says the\n'
        '  two words may not be joined, and भवतः शायिका appears in both.'
    ),
    "2.3.66": (
        'SETTLED — उभयप्राप्तौ कर्मणि: where BOTH doer and object could\n'
        '  take the sixth, only the object does — आश्चर्यो गवां\n'
        '  दोहोऽगोपालकेन, and the milker falls to a third.\n'
        '  उभयप्राप्ताविति बहुव्रीहिः.\n'
        '\n'
        'SETTLED — and 2.2.14 कर्मणि च is the rule that then keeps that\n'
        '  genitive from compounding, using this very example.'
    ),
    "2.3.67": (
        'SETTLED — क्तस्य च वर्तमाने: राज्ञां मतः, राज्ञां बुद्धः,\n'
        '  राज्ञां पूजितः. 2.3.69 would have refused the sixth and this\n'
        '  gives it back for the present sense.\n'
        '\n'
        'SETTLED — वर्तमान इति किम्? ग्रामं गतः. क्तस्येति किम्? ओदनं\n'
        '  पचमानः.\n'
        '\n'
        'SETTLED — and 2.2.12 क्तेन च पूजायाम् forbids the compound, with\n'
        '  the same three words.'
    ),
    "2.3.68": (
        'SETTLED — अधिकरणवाचिनश्च: इदमेषाम् आसितम्, इदमेषां भुक्तम् — a\n'
        '  क्त naming the PLACE of the act, by 3.4.76.\n'
        '  प्रतिषेधापवादो योगः, a second way past 2.3.69.\n'
        '\n'
        'SETTLED — and 2.2.13 अधिकरणवाचिना च forbids the compound, with\n'
        '  the same example.'
    ),
    "2.3.69": (
        'SETTLED — न लोकाव्ययनिष्ठाखलर्थतृनाम्: the sixth 2.3.65 gives is\n'
        '  refused before these seven. ओदनं पचन्, ओदनं पचमानः.\n'
        '\n'
        'SETTLED — ल is an abbreviation and the Kāśikā spells it out\n'
        '  rather than leaving it to be guessed: ल इति शतृशानचौ\n'
        '  कानच्क्वसू किकिनौ च गृह्यन्ते.\n'
        '\n'
        'SETTLED — 2.3.67 and 2.3.68 are its two exceptions, and both say\n'
        '  so where they stand.'
    ),
    "2.3.70": (
        'SETTLED — अकेनोर्भविष्यदाधमर्ण्ययोः: कटं कारको व्रजति, ग्रामं\n'
        '  गमी, शतं दायी. अक in the future sense, and इन् in the future\n'
        '  or the debt sense.\n'
        '\n'
        'SETTLED — भविष्यदाधमर्ण्ययोरिति किम्? यवानां लावकः — an अक not\n'
        '  in the future sense, and the sixth stands.'
    ),
    "2.3.71": (
        'SETTLED — कृत्यानां कर्तरि वा: भवता कटः कर्तव्यः beside भवतः\n'
        '  कटः कर्तव्यः. What 2.3.65 made invariable is a choice here,\n'
        '  and only for the DOER.\n'
        '\n'
        'SETTLED — कर्तरीति किम्? गेयो माणवकः साम्नाम् — the object keeps\n'
        '  no sixth from this rule.'
    ),
    "2.3.72": (
        'SETTLED — तुल्यार्थैरतुलोपमाभ्यां तृतीयाऽन्यतरस्याम्: तुल्यो\n'
        '  देवदत्तेन beside तुल्यो देवदत्तस्य, सदृशो देवदत्तेन beside\n'
        '  सदृशो देवदत्तस्य.\n'
        '\n'
        'SETTLED — where the third is not taken the sixth comes back on\n'
        '  its own: शेषे विषये तृतीयाविधानात् तया मुक्ते षष्ठ्येव भवति.\n'
        '  So the option is between a rule and 2.3.50, not between two\n'
        '  rules.\n'
        '\n'
        'SETTLED — अतुलोपमाभ्यामिति किम्? तुला and उपमा are excepted by\n'
        '  name though they mean the same.'
    ),
    "2.3.73": (
        'SETTLED — चतुर्थी चाशिष्यायुष्यमद्रभद्रकुशलसुखार्थहितैः: seven\n'
        '  words, in a blessing — आयुष्यं देवदत्ताय भूयात्.\n'
        '\n'
        'SETTLED — चकारो विकल्पानुकर्षणार्थः: the च drags the option down\n'
        '  from 2.3.72, so the sixth stands beside the fourth — and for\n'
        '  the same reason, शेषे चतुर्थीविधानात् तया मुक्ते षष्ठी भवति.\n'
        '\n'
        'SCOPE — अत्रायुष्यादीनां पर्यायग्रहणं कर्तव्यम्, the synonyms of\n'
        '  the seven to be taken in too. Recorded, not modelled.\n'
        '\n'
        'SETTLED — and this closes the pāda: 2.3.1 अनभिहिते has governed\n'
        '  every rule from there to here.'
    ),
}

#: 2.3.48 and 2.3.49 confer names and give no ending, so they answer
#: through `amantrita` rather than through the case resolver.
_NAMES = ("2.3.48", "2.3.49")

for _sutra, _notes in _VIBHAKTI.items():
    register(
        _sutra,
        apply=amantrita if _sutra in _NAMES else vibhakti_for,
        codification=_CODIFICATION,
        notes=_notes,
        # No reuse is declared. 1.4.23 to 1.4.55 decide the kāraka and
        # this section gives it an ending, which is a real dependency in
        # the grammar and not a call in the code: the kāraka is passed
        # in, because deciding it needs the whole clause and not the one
        # word. Declaring it would repeat the mistake 2.2.30 records.
    )


__all__ = ["vibhakti_for"]
