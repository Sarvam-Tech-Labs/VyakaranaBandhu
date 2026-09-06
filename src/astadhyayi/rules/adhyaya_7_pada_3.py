# -*- coding: utf-8 -*-
"""अध्याय ७, पाद ३ — guṇa before a sārvadhātuka or ārdhadhātuka."""

from __future__ import annotations

from src.astadhyayi.anga import ato_dirgho_yani, guna_before_affix
from src.astadhyayi.dirgha_sup import before_ending
from src.astadhyayi.kutva import guttural
from src.astadhyayi.sarvadhatuke_guna import before_sarvadhatuka
from src.astadhyayi.nau_agama import before_ni
from src.astadhyayi.pratyaya_ka import the_ka
from src.astadhyayi.siti import before_sit
from src.astadhyayi.uttarapada_vrddhi import uttarapada_vrddhi
from src.astadhyayi.sources import register

_UTTARAPADA_VRDDHI = (
    'uttarapada_vrddhi(stem, gana=..., purvapada=..., '
    'uttarapada=..., before=..., sense=...) -> where the taddhita '
    'vrddhi falls, by rule of 7.3.1-31.'
)

register(
    '7.3.1',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — देविकाशिंशपादित्यवाड्दीर्घसत्रश्रेयसामात् — five stems\n'
        "  take a plain आ where the first vowel's vṛddhi was due: **दाविकम्\n"
        '  उदकम्; शांशपश्चमसः; दीर्घसात्रम्**. And it reaches the uttarapada\n'
        '  vṛddhi of 7.3.14 as well — **पूर्वदाविकः**, where **प्राचां\n'
        '  ग्रामनगराणाम् इत्युत्तरपदवृद्धिः, साप्याकार एव भवति**'
    ),
)

register(
    '7.3.2',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — केकयमित्त्रययुप्रलयानां यादेरियः — and three stems turn\n'
        "  their य into इय: **कैकेयः** from 4.1.168's अञ्; **मैत्रेयिकया\n"
        "  श्लाघते** from 5.1.134's वुञ्; **प्रालेयम् उदकम्**"
    ),
)

register(
    '7.3.3',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — न य्वाभ्यां पदान्ताभ्याम् पूर्वौ तु ताभ्यामैच् — a stem\n'
        '  whose first vowel stands after a word-final य् or व् takes NO\n'
        '  vṛddhi, and an ऐ or औ is put in FRONT of that य् or व् instead:\n'
        '  **वैयसनम्, वैयाकरणः** for the य्; **सौवश्वः** for the व्.\n'
        '\n'
        'SETTLED — **AND THE REFUSAL IS STATED TO FIX WHERE THE AUGMENT\n'
        '  GOES.** **प्रतिषेधवचनम् ऐचोर् विषयप्रक्ऌप्त्यर्थम्, इह मा भूत् —\n'
        '  दाध्यश्विः, माध्वश्विः** — there the य् and व् are not what the\n'
        '  first vowel follows, and no augment comes'
    ),
)

register(
    '7.3.4',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — द्वारादीनां च — and the द्वारादि stems: **दौवारिकः,\n'
        '  दौवारपालम्; सौवरः; वैयल्कशः; सौवस्तिकः; सौवः**. The rule reaches a\n'
        '  compound BEGINNING with one of them — **तदादिविधिश्चात्र भवति** —\n'
        '  and the vṛtti rejects one reading of the list outright:\n'
        '  **स्वाध्याय इति केचित् पठन्ति, तद् अनर्थकम्**'
    ),
)

register(
    '7.3.5',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — न्यग्रोधस्य च केवलस्य — and न्यग्रोध ALONE:\n'
        '  **नैयग्रोधश्चमसः**. Whether the sūtra restricts or provides\n'
        '  depends on how the word is derived — **न्यग्रोहतीति न्यग्रोध इति\n'
        '  व्युत्पत्तिपक्षे नियमार्थम्, अव्युत्पत्तिपक्षे विध्यर्थम्**'
    ),
)

register(
    '7.3.6',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — न कर्मव्यतिहारे — but where RECIPROCAL action is meant,\n'
        '  neither the refusal nor the augment holds: **व्यावक्रोशी,\n'
        '  व्यावलेखी, व्यावचर्ची, व्यावहासी वर्तते**. **प्रतिषेधागमयोर् अयं\n'
        '  प्रतिषेधः** — one refusal cancelling two things at once, and the\n'
        '  ordinary vṛddhi comes back'
    ),
)

register(
    '7.3.7',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — स्वागतादीनां च — and seven stems likewise: **स्वागतिकः,\n'
        '  स्वाध्वरिकः, स्वाङ्गिः, व्याङ्गिः, व्याडिः, व्यावहारिकः,\n'
        '  स्वापतेयः**. व्यवहार is named although 7.3.6 would seem to reach\n'
        '  it, because **व्यवहारशब्दोऽयं लौकिके वृत्ते वर्तते, न तु\n'
        '  कर्मव्यतिहारे**; and स्वपति is named because **द्वारादिषु\n'
        '  स्वशब्दपाठाद् अत्र प्राप्तिः**'
    ),
)

register(
    '7.3.8',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — श्वादेरिञि — and a stem beginning श्वन् before इञ्:\n'
        '  **श्वाभस्त्रिः, श्वादंष्ट्रिः**. That श्वन् is in the द्वारादि\n'
        '  list and the compound-initial reading is available there is what\n'
        '  this sūtra proves — **तत्र च तदादिविधिर् भवतीत्येतद् एव वचनं\n'
        '  ज्ञापकम्**. A vārttika widens इञ् to every इ-initial affix:\n'
        '  **श्वागणिकः, श्वायूथिकः**'
    ),
)

register(
    '7.3.9',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — पदान्तस्यान्यतरस्याम् — and OPTIONALLY where such a stem\n'
        '  ends in पद: **श्वापदम्, शौवापदम्**. The sūtra before had refused\n'
        '  the vṛddhi outright before इञ्; here the refusal is only half, so\n'
        '  both forms stand and the language keeps the shorter'
    ),
)

register(
    '7.3.10',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — उत्तरपदस्य — a heading: **उत्तरपदस्येत्ययम् अधिकारः,\n'
        '  हनस्तोऽचिण्णलोः इति प्रागेतस्मात्** — from here to 7.3.31 the\n'
        '  vṛddhi falls on the SECOND member of a compound.\n'
        '\n'
        'SETTLED — **AND IT IS THERE FOR THREE REASONS AT ONCE.** Some rules\n'
        '  of the run have no ablative to read the second member out of —\n'
        '  **जे प्रोष्ठपदानाम्** is one; where there is one the heading is\n'
        "  **विस्पष्टार्थम्**; and it lets 6.2.105's **उत्तरपदवृद्धौ सर्वं\n"
        "  च** name this stretch's vṛddhi as a thing with a name"
    ),
)

register(
    '7.3.11',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — अवयवादृतोः — a season-word as second member takes the\n'
        '  vṛddhi after a word for a PART of it: **पूर्ववार्षिकम्,\n'
        "  पूर्वहैमनम्, अपरवार्षिकम्, अपरहैमनम्**. The compound is 2.2.1's\n"
        "  एकदेशिसमास and the affix 4.3.18's ठक्, and the rule reaches a\n"
        '  compound ENDING in a season — **ऋतोर् वृद्धिमद्विधाव् अवयवानाम्\n'
        '  इति तदन्तविधिः**'
    ),
)

register(
    '7.3.12',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — सुसर्वार्धाज्जनपदस्य — a country-name as second member\n'
        '  takes it after सु, सर्व and अर्ध: **सुपाञ्चालकः, सर्वपाञ्चालकः,\n'
        "  अर्धपाञ्चालकः**. The affix is 4.2.124's वुञ्, and a vārttika adds\n"
        '  the direction-words to the three: **सुसर्वार्धदिक्शब्देभ्यो\n'
        '  जनपदस्य**'
    ),
)

register(
    '7.3.13',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — दिशोऽमद्राणाम् — and after a DIRECTION-word, मद्र\n'
        '  excepted: **पूर्वपाञ्चालकः, अपरपाञ्चालकः, दक्षिणपाञ्चालकः**'
    ),
)

register(
    '7.3.14',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — प्राचां ग्रामनगराणाम् — and a village or a town of the\n'
        '  EASTERN country after a direction-word: **पूर्वैषुकामशमः,\n'
        '  पूर्वकार्ष्णमृत्तिकः** for the villages; **पूर्वपाटलिपुत्रकः,\n'
        '  पूर्वकान्यकुब्जः** for the towns. A town is a village for\n'
        "  grammar's purposes and both are named all the same,\n"
        '  **संबन्धभेदप्रतिपत्त्यर्थम्** — to show which of the two relations\n'
        '  the compound expresses'
    ),
)

register(
    '7.3.15',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — संख्यायाः संवत्सरसंख्यस्य च — and संवत्सर, or another\n'
        '  numeral, after a numeral: **द्विसांवत्सरिकः; द्विषाष्टिकः,\n'
        '  द्विसाप्ततिकः**. 7.3.17 would have covered संवत्सर, and naming it\n'
        '  here is **परिमाणग्रहणे कालपरिमाणस्याग्रहणार्थम्** — so that\n'
        '  *measure* in that sūtra shall not mean a measure of time'
    ),
)

register(
    '7.3.16',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — वर्षस्याभविष्यति — and वर्ष after a numeral, where the\n'
        '  taddhita is NOT in a future sense: **द्विवार्षिकः, त्रिवार्षिकः**.\n'
        '  And the exception is narrower than it looks — **अधीष्टभृतयोर्\n'
        '  अभविष्यतीति प्रतिषेधो न भवति। गम्यते हि तत्र भविष्यत्ता, न तु\n'
        "  तद्धितार्थः**, a future merely understood is not the affix's own\n"
        '  sense'
    ),
)

register(
    '7.3.17',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — परिमाणान्तस्यासंज्ञाशाणयोः — and a measure-word after a\n'
        '  numeral, where it is neither a NAME nor शाण: **द्विकौडविकः,\n'
        '  द्विसौवर्णिकम्, द्विनैष्किकम्**'
    ),
)

register(
    '7.3.18',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — जे प्रोष्ठपदानाम् — प्रोष्ठपदा as second member takes it\n'
        '  where BIRTH is meant: **प्रोष्ठपादो माणवकः**. This is the sūtra\n'
        "  7.3.10's heading was needed for, there being no ablative to read\n"
        '  the second member out of. And the plural is why the synonym counts\n'
        '  too — **पर्यायोऽपि गृह्यते, भद्रपाद इति**'
    ),
)

register(
    '7.3.19',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — हृद्भगसिन्ध्वन्ते पूर्वपदस्य च — where the compound ends\n'
        '  in हृद्, भग or सिन्धु, BOTH members take the vṛddhi: **सौहार्दम्,\n'
        '  सौहार्द्यम्; सौभाग्यम्, दौर्भाग्यम्; सौभागिनेयः, दौर्भागिनेयः**.\n'
        '  Six rules from here do the same, and the Veda is let off: **महते\n'
        '  सौभगाय — छन्दसि सर्वविधीनां विकल्पितत्वात्**'
    ),
)

register(
    '7.3.20',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — अनुशतिकादीनां च — and the अनुशतिकादि stems: **आनुशातिकम्,\n'
        '  आनुहौडिकः, आनुसांवरणम्, आनुसांवत्सरिकः, आङ्गारवैणवः, आसिहात्यम्**.\n'
        "  The list's own readings are disputed — **अस्यहत्य इति केचित्\n"
        '  पठन्ति... अस्यहेतिर् इत्येवमपरे पठन्ति** — and the vṛtti records\n'
        '  the variants rather than choosing'
    ),
)

register(
    '7.3.21',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — देवताद्वंद्वे च — and a द्वन्द्व of deities:\n'
        '  **आग्निमारुतीं पृश्निम् आलभेत; आग्निमारुतं कर्म**. But only one\n'
        '  that belongs to a hymn or an oblation — **यो देवताद्वन्द्वः\n'
        '  सूक्तहविःसंबन्धी, तत्रायं विधिः**'
    ),
)

register(
    '7.3.22',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — नेन्द्रस्य परस्य — but a FOLLOWING इन्द्र does not take\n'
        '  it: **सौमेन्द्रः, आग्नेन्द्रः**.\n'
        '\n'
        'SETTLED — **AND THE REFUSAL IS READ AS PROOF ABOUT THE ORDER OF THE\n'
        '  WHOLE GRAMMAR.** इन्द्र has two vowels; 6.4.148 takes the first\n'
        '  away before the taddhita and the rest merges with what precedes,\n'
        '  so no vṛddhi could have applied and the refusal is idle as it\n'
        '  stands. **तदेदं प्रतिषेधवचनं ज्ञापकम् — बहिरङ्गम् अपि\n'
        '  पूर्वोत्तरपदयोः पूर्वं कार्यं भवति पश्चाद् एकादेशः** — the two\n'
        "  members' own operations are done first and the merger after, which\n"
        '  is what makes पूर्वैषुकामशमः come out at all'
    ),
)

register(
    '7.3.23',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — दीर्घाच्च वरुणस्य — and वरुण after a member ending in a\n'
        '  LONG vowel: **ऐन्द्रावरुणम्, मैत्रावरुणम्**'
    ),
)

register(
    '7.3.24',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — प्राचां नगरान्ते — and where an EASTERN compound ends in\n'
        '  नगर, both members take it: **सौह्मनागरः, पौण्ड्रनागरः**'
    ),
)

register(
    '7.3.25',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — जङ्गलधेनुवलजान्तस्य विभाषितमुत्तरम् — where the compound\n'
        '  ends in जङ्गल, धेनु or वलज, the FIRST member takes the vṛddhi and\n'
        '  the second takes it OPTIONALLY: **कौरुजङ्गलम्, कौरुजाङ्गलम्;\n'
        '  वैश्वधेनवम्, वैश्वधैनवम्; सौवर्णवलजः, सौवर्णवालजः**'
    ),
)

register(
    '7.3.26',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — अर्धात् परिमाणस्य पूर्वस्य तु वा — a measure-word after\n'
        '  अर्ध takes it, and अर्ध itself OPTIONALLY: **आर्धद्रौणिकम्,\n'
        '  अर्धद्रौणिकम्; आर्धकौडविकम्, अर्धकौडविकम्**'
    ),
)

register(
    '7.3.27',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — नातः परस्य — but a measure BEGINNING with a short अ does\n'
        '  not take it after अर्ध, and अर्ध still takes its own optionally:\n'
        '  **अर्धप्रस्थिकः, आर्धप्रस्थिकः; अर्धकंसिकः, आर्धकंसिकः**.\n'
        '\n'
        'SETTLED — **AND THE तपर IS THERE FOR A RULE FOUR PĀDAS BACK.**\n'
        "  Refuse the vṛddhi to अर्धखारी and 6.3.39's **वृद्धिनिमित्तस्य च\n"
        '  तद्धितस्यारक्तविकारे** would no longer see the taddhita as a\n'
        '  vṛddhi-cause, and the पुंवद्भाव it refuses would come through in\n'
        '  अर्धखारीभार्यः'
    ),
)

register(
    '7.3.28',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        "SETTLED — प्रवाहणस्य ढे — प्रवाहण's second member takes it before ढ,\n"
        '  and its first optionally: **प्रावाहणेयः, प्रवाहणेयः**. The ढक् is\n'
        "  4.1.123's"
    ),
)

register(
    '7.3.29',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — तत्प्रत्ययस्य च — and the same word WITH its ढक् already\n'
        '  on it, before a further taddhita: **प्रावाहणेयिः, प्रवाहणेयिः;\n'
        '  प्रावाहणेयकम्, प्रवाहणेयकम्**. The sūtra exists because the outer\n'
        "  taddhita's vṛddhi could not be made optional by appealing to the ढ\n"
        '  — **बाह्यतद्धितनिमित्ता वृद्धिर् ढाश्रयेण विकल्पेन बाधितुम्\n'
        '  अशक्येति सूत्रारम्भः**'
    ),
)

register(
    '7.3.30',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — नञः शुचीश्वरक्षेत्रज्ञकुशलनिपुणानाम् — five stems after\n'
        '  नञ् take it, and the नञ् optionally: **अशौचम्, आशौचम्;\n'
        '  अनैश्वर्यम्, आनैश्वर्यम्; अक्षैत्रज्ञ्यम्, आक्षैत्रज्ञ्यम्;\n'
        '  अकौशलम्, आकौशलम्; अनैपुणम्, आनैपुणम्**. Some read the first\n'
        "  member's vṛddhi as one that would never have come at all, 5.1.121\n"
        '  refusing the abstract affix after a नञ्-compound in the first\n'
        '  place'
    ),
)

register(
    '7.3.31',
    apply=uttarapada_vrddhi,
    codification=_UTTARAPADA_VRDDHI,
    notes=(
        'SETTLED — यथातथयथापुरयोः पर्यायेण — and two more take it BY TURNS\n'
        '  with the नञ्, one or the other and never both: **आयथातथ्यम्,\n'
        '  अयाथातथ्यम्; आयथापुर्यम्, अयाथापुर्यम्**.\n'
        '\n'
        'SETTLED — **AND THE WORDS ARE READ AS TWO DIFFERENT COMPOUNDS IN TWO\n'
        "  PLACES.** In 5.1.124's ब्राह्मणादि list they are नञ्-compounds; in\n"
        '  this sūtra they are अव्ययीभाव compounds by 2.1.7, **तथा\n'
        '  नपुंसकाश्रयं ह्रस्वत्वं कृतम्**. The Bhāṣya reads them a third\n'
        "  way, as 2.1.4's सुप्सुपा. This closes the उत्तरपद heading"
    ),
)

_BEFORE_NI = (
    'before_ni(root, gana=..., before=..., sense=...) -> what goes '
    'in before the causal, and what han becomes, by rule of '
    '7.3.32-43.'
)

register(
    '7.3.32',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — हनस्तोऽचिण्णलोः — हन् becomes त् before a ञित् or णित्\n'
        '  that is neither चिण् nor णल्: **घातयति, घातकः, साधुघाती,\n'
        '  घातंघातम्, घातो वर्तते**.\n'
        '\n'
        'SETTLED — **AND TWO WORDS OF THE HEADING FALL AWAY HERE.**\n'
        '  **तद्धितेष्विति निवृत्तम्। तत्संबद्धं कितीत्यपि** — the taddhita\n'
        '  condition goes and the कित् with it, since that was there only for\n'
        "  the taddhitas' sake. **ञ्णितीति वर्तते** is what is left, and this\n"
        "  is where 7.3.10's उत्तरपद heading ends.\n"
        '\n'
        "SETTLED — **AND THE RULE IS ABOUT A ROOT'S OWN AFFIX.** **धातोः\n"
        '  कार्यम् उच्यमानं धातोः प्रत्यये विज्ञायते** — so वार्त्रघ्नम् is\n'
        '  untouched, its ञित् belonging to a noun'
    ),
)

register(
    '7.3.33',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — आतो युक् चिण्कृतोः — an आ-final stem takes the augment\n'
        '  युक् before चिण् and before a ञित् or णित् कृत्: **अदायि, अधायि;\n'
        '  दायः, दायकः, धायः, धायकः**'
    ),
)

register(
    '7.3.34',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — नोदात्तोपदेशस्य मान्तस्यानाचमेः — but a म्-final root that\n'
        "  is उदात्त as it is taught does not take 7.2.116's vṛddhi before\n"
        '  चिण् or a कृत्, आचम् excepted: **अशमि, अतमि, अदमि; शमकः, तमकः,\n'
        '  दमकः; शमः, तमः, दमः**. **किं चोक्तम्? अत उपधायाः इति वृद्धिः** —\n'
        '  the vṛtti has to say which of the earlier rules the *what is said*\n'
        '  refers to. And उपदेशे is what gets शमी and दमी while keeping यामकः\n'
        '  out'
    ),
)

register(
    '7.3.35',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — जनिवध्योश्च — and जन् and वध्: **अजनि, जनकः, प्रजनः; अवधि,\n'
        '  वधकः, वधः**. The वध् meant is the consonant-final root that exists\n'
        '  in its own right, **वधिः प्रकृत्यन्तरं व्यञ्जनान्तोऽस्ति तस्यायं\n'
        '  प्रतिषेधो विधीयते** — the वध that replaces हन् ends in अ and would\n'
        '  never have taken the vṛddhi'
    ),
)

register(
    '7.3.36',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — अर्त्तिह्रीब्लीरीक्नूयीक्ष्माय्यातां पुङ्णौ — six roots\n'
        '  and every आ-final stem take पुक् before णि: **अर्पयति, ह्रेपयति,\n'
        '  व्लेपयति, रेपयति, क्नोपयति, क्ष्मापयति; दापयति, धापयति**. Two\n'
        '  roots of the shape ऋ are both meant, and two of the shape री.\n'
        '\n'
        'SETTLED — **AND THE AUGMENT IS PUT BEFORE THE ENDING FOR A REASON\n'
        '  THREE PĀDAS ON.** **पुकः पूर्वान्तकरणम् अदीदपद् इत्यत्रोपधाह्रस्वो\n'
        '  यथा स्यात्** — only so does the reduplicated aorist shorten the\n'
        '  right vowel.\n'
        '\n'
        'SETTLED — **AND THE HEADING CHANGES HERE.** **सर्वं निवृत्तम्,\n'
        '  अङ्गस्येति वर्तते** — everything the pāda has been carrying falls\n'
        '  away, and णौ alone governs the rest of the run'
    ),
)

register(
    '7.3.37',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — शाच्छासाह्वाव्यावेपां युक् — seven roots take युक् before\n'
        '  णि: **निशाययति, अवच्छाययति, अवसाययति, ह्वाययति, संव्याययति,\n'
        '  वाययति, पाययति**. The पा meant takes in the drying-root as well,\n'
        '  **पाग्रहणे पै ओवै शोषणे इत्यस्यापीह ग्रहणम् इच्छन्ति**, but not\n'
        '  the protecting one. And two vārttikas add more: **लुगागमस्तु तस्य\n'
        '  वक्तव्यः** giving पालयति, and **धूञ्प्रीञोर् नुग् वक्तव्यः**\n'
        '  giving धूनयति and प्रीणयति'
    ),
)

register(
    '7.3.38',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — वो विधूनने जुक् — वा takes जुक् before णि where SHAKING is\n'
        '  meant: **पक्षेणोपवाजयति**. Without that sense it is **आवापयति\n'
        '  केशान्**, and the root there is the drying one — **पै ओवै शोषणे\n'
        '  इत्येतस्यैतद् रूपम्**, a different word of the same shape'
    ),
)

register(
    '7.3.39',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — लीलोर्नुग्लुकावन्यतरस्यां स्नेहविपातने — ली and ला take\n'
        '  नुक् and लुक् OPTIONALLY before णि where MELTING is meant: **घृतं\n'
        '  विलीनयति, घृतं विलाययति; विलालयति, विलापयति**. The ली is written\n'
        '  with an ई read into it, so that the नुक् reaches only the ई-final\n'
        '  root and not the one 6.1.51 has already turned into ला'
    ),
)

register(
    '7.3.40',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — भियो हेतुभये षुक् — भी takes षुक् before णि where the\n'
        "  FRIGHTENER is himself the fear's occasion: **मुण्डो भीषयते; जटिलो\n"
        '  भीषयते**. Again an ई is read into the root, **कृतात्वस्य\n'
        '  षुग्निवृत्त्यर्थः** — else भापयते would take it too'
    ),
)

register(
    '7.3.41',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — स्फायो वः — स्फाय् becomes व before णि: **स्फावयति**. One\n'
        '  root, one substitute, and no condition beyond the affix — the\n'
        '  shortest sūtra of the run, and the only one the vṛtti has nothing\n'
        '  to argue about'
    ),
)

register(
    '7.3.42',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — शदेरगतौ तः — शद् becomes त् before णि where MOTION is NOT\n'
        '  meant: **पुष्पाणि शातयति**, he makes the flowers fall. **अगताविति\n'
        '  किम्? गाः शादयति गोपालकः** — the herdsman DRIVES his cattle, and\n'
        '  there the change does not come'
    ),
)

register(
    '7.3.43',
    apply=before_ni,
    codification=_BEFORE_NI,
    notes=(
        'SETTLED — रुहः पोऽन्यतरस्याम् — and रुह् becomes प OPTIONALLY:\n'
        '  **व्रीहीन् रोपयति, व्रीहीन् रोहयति**. Both forms stand, and the\n'
        '  option is the last thing the pāda says about the causal before it\n'
        "  turns to the feminine's क"
    ),
)


_THE_KA = (
    'the_ka(what, gana=..., before=..., view=...) -> what the '
    'affix k and the taddhita tha become, by rule of 7.3.44-51.'
)

register(
    '7.3.44',
    apply=the_ka,
    codification=_THE_KA,
    notes=(
        'SETTLED — प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः — the अ before an\n'
        "  AFFIX's क becomes इ before आप्, unless that आप् follows a सुप्:\n"
        '  **जटिलिका, मुण्डिका, कारिका, हारिका; एतिकाश्चरन्ति**.\n'
        '\n'
        'SETTLED — **AND THE WORD प्रत्ययस्थ IS ARGUED TO BE DERIVABLE.**\n'
        '  **ककारमात्रं प्रत्ययो नास्तीति सामर्थ्यात् प्रत्ययस्थस्य ग्रहणं\n'
        '  शक्यते विज्ञातुम्** — no affix is a bare क, so the qualification\n'
        "  could have been read out of the rule's own working. It is written\n"
        '  all the same, **स्थग्रहणं विस्पष्टार्थम्**'
    ),
)

register(
    '7.3.45',
    apply=the_ka,
    codification=_THE_KA,
    notes=(
        'SETTLED — न यासयोः — but not for या and सा: **यका, सका**. And the\n'
        '  two are named as a specimen and not a list — **या सा इति\n'
        '  निर्देशोऽतन्त्रम्, यत्तदोर् उपलक्षणार्थम् एतत्** — so यकांयकाम्\n'
        '  and तकांतकाम् are refused too. Three vārttikas add more:\n'
        '  **यासयोरित्त्वप्रतिषेधे त्यकन उपसंख्यानम्** giving उपत्यका;\n'
        '  **पावकादीनां छन्दसि** giving पावकाः; and **आशिषि च** giving जीवका,\n'
        '  नन्दका, भवका'
    ),
)

register(
    '7.3.46',
    apply=the_ka,
    codification=_THE_KA,
    notes=(
        'SETTLED — उदीचामातः स्थाने यकपूर्वायाः — and in the NORTHERN\n'
        "  teachers' view, an अ that stands in place of a long आ and has a य\n"
        '  or a क before it: **इभ्यका, इभ्यिका; क्षत्रियका, क्षत्रियिका;\n'
        '  चटकका, चटकिका; मूषिकका, मूषिकिका**.\n'
        '\n'
        'SETTLED — **AND NAMING THE TEACHERS IS WHAT MAKES IT AN OPTION.**\n'
        '  **उदीचांग्रहणं विकल्पार्थम्** — both forms stand, and the sūtra\n'
        '  records a view rather than settling one'
    ),
)

register(
    '7.3.47',
    apply=the_ka,
    codification=_THE_KA,
    notes=(
        'SETTLED — भस्त्रैषाऽजाज्ञाद्वास्वानञ्पूर्वाणामपि — and six stems,\n'
        '  with or without a नञ् before them: **भस्त्रका, भस्त्रिका; एषका,\n'
        '  एषिका; अजका, अजिका; ज्ञका, ज्ञिका; द्वके, द्विके; स्वका, स्विका**.\n'
        '  Two of the six can take no नञ् — **एषाद्वे नञ्पूर्वे न प्रयोजयतः**\n'
        '  — and the vṛtti works out why, from which ending the compound\n'
        '  would take on either order of operations'
    ),
)

register(
    '7.3.48',
    apply=the_ka,
    codification=_THE_KA,
    notes=(
        'SETTLED — अभाषितपुंस्काच्च — and an अ supplied after a stem with no\n'
        '  masculine of its own: **खट्वका, खट्विका; अखट्वका, अखट्विका;\n'
        '  परमखट्वका, परमखट्विका**. In a बहुव्रीहि it applies only where the\n'
        '  कप् has shortened the vowel, and the vṛtti separates the two\n'
        '  readings of अखट्वा carefully'
    ),
)

register(
    '7.3.49',
    apply=the_ka,
    codification=_THE_KA,
    notes=(
        "SETTLED — आदाचार्याणाम् — and in the TEACHERS' view that same अ\n"
        '  becomes आ: **खट्वाका, अखट्वाका, परमखट्वाका**. A fifth form beside\n'
        '  the four the sūtras before allow, and again a view recorded rather\n'
        '  than adopted'
    ),
)

register(
    '7.3.50',
    apply=the_ka,
    codification=_THE_KA,
    notes=(
        "SETTLED — ठस्येकः — a taddhita's ठ becomes इक: **आक्षिकः, शालाकिकः**\n"
        "  from 4.4.1's ठक्; **लावणिकः** from 4.4.52's ठञ्.\n"
        '\n'
        'SETTLED — **AND THE ठ REPLACED IS THE WHOLE AFFIX OR JUST ITS SOUND,\n'
        '  ACCORDING TO HOW AFFIXES ARE READ.** **ठगादिषु यदि वर्णमात्रं\n'
        '  प्रत्ययः, उच्चारणार्थोऽकारः, तदेहाप्यकार उच्चारणार्थः...\n'
        '  संघातग्रहणे तु प्रत्यये अत्रापि संघातग्रहणम् एव** — the rule works\n'
        '  either way, and the vṛtti sets out both. The Uṇādi कण्ठ keeps its\n'
        '  ठ, **उणादयो बहुलम्**'
    ),
)

register(
    '7.3.51',
    apply=the_ka,
    codification=_THE_KA,
    notes=(
        'SETTLED — इसुसुक्तान्तात् कः — but after a stem ending in इस्, उस्,\n'
        '  an उक् vowel or त्, the ठ becomes क: **सार्पिष्कः; धानुष्कः,\n'
        '  याजुष्कः; नैषादकर्षुकः, मातृकम्, पैतृकम्; औदश्वित्कः, शाकृत्कः,\n'
        '  याकृत्कः**. A vārttika adds one more: **दोष उपसंख्यानम्। दौष्कः**'
    ),
)


_GUTTURAL = (
    'guttural(root, gana=..., before=..., sense=..., abhyasa=...) '
    '-> whether a c or j becomes a guttural, by rule of '
    '7.3.52-69.'
)

register(
    '7.3.52',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — चजोः कु घिन्ण्यतोः — a च् or ज् becomes the corresponding\n'
        '  guttural before a घित् affix and before ण्यत्: **पाकः, त्यागः,\n'
        '  रागः** for the घित्; **पाक्यम्, वाक्यम्, रेक्यम्** for the ण्यत्.\n'
        "  Which guttural exactly is 1.1.50's business — the nearest one"
    ),
)

register(
    '7.3.53',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — न्यङ्क्वादीनां च — and a list of nouns already so made:\n'
        '  **न्यङ्कुः, मद्गुः, भृगुः; दूरेपाकः, फलेपाकः**. Each is worked\n'
        '  back to the Uṇādi affix that built it — **नावञ्चेः**, **मिमस्जिभ्य\n'
        '  उः**, **प्रथिम्रदिभ्रस्जां संप्रसारणं सलोपश्च** — and the vṛtti\n'
        '  notes that some read क्षणेपाक into the list as well'
    ),
)

register(
    '7.3.54',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        "SETTLED — हो हन्तेर्ञ्णिन्नेषु — हन्'s ह् becomes a guttural before\n"
        '  a ञित् affix and before न्: **घातयति, घातकः, साधुघाती, घातो\n'
        '  वर्तते** for the ञित्; **घ्नन्ति, घ्नन्तु, अघ्नन्** for the न्.\n'
        '\n'
        'SETTLED — **AND WHETHER THE न् MUST STAND IMMEDIATELY AFTER IS\n'
        '  ANSWERED CAREFULLY.** **तच्चानन्तर्यं संनिपातकृतम् आश्रीयते।\n'
        '  स्थानिवद्भावशास्त्रकृतं तु यद् अनानन्तर्यं तद् अविघातकम्,\n'
        '  वचनसामर्थ्यात्** — an interval made by the sounds themselves stops\n'
        "  the rule; one made by a substitution's counting as its original\n"
        '  does not'
    ),
)

register(
    '7.3.55',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — अभ्यासाच्च — and after a reduplication: **जिघांसति,\n'
        "  जङ्घन्यते, अहं जघन**. The reduplication must be हन्'s own —\n"
        '  **अभ्यासनिमित्ते प्रत्यये हन्तेरङ्गस्य योऽभ्यासस्तस्माद् एवैतत्\n'
        '  कुत्वम्**'
    ),
)

register(
    '7.3.56',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        "SETTLED — हेरचङि — and हि's ह् after a reduplication, except in the\n"
        '  चङ् aorist: **प्रजिघीषति, प्रजेघीयते, प्रजिघाय**.\n'
        '\n'
        'SETTLED — **AND THE EXCEPTION IS SHOWN TO BE UNNECESSARY AND KEPT\n'
        '  FOR WHAT IT PROVES.** **अचङीति शक्यम् अकर्तुम्** — in the चङ् the\n'
        '  stem is not हि but the causal, so the rule could not have reached.\n'
        '  **तत् क्रियते ज्ञापकार्थम्। एतद् ज्ञाप्यते — हेरचङीति चङोऽन्यत्र\n'
        '  हेर् ण्यधिकस्यापि कुत्वं भवति** — outside the चङ् the change\n'
        '  reaches a हि that has a णि on it, which is what gets प्रजिघाययिषति'
    ),
)

register(
    '7.3.57',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        "SETTLED — सन्लिटोर्जेः — जि's ज् becomes a guttural after its\n"
        '  reduplication, before सन् and the perfect: **जिगीषति, जिगाय**'
    ),
)

register(
    '7.3.58',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        "SETTLED — विभाषा चेः — and चि's च् OPTIONALLY: **चिचीषति, चिकीषति;\n"
        '  चिचाय, चिकाय**. The sūtra before had made the change compulsory\n'
        '  for जि in the same two environments; here it is a choice, and both\n'
        '  forms of each stand'
    ),
)

register(
    '7.3.59',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — न क्वादेः — but a root that BEGINS with a guttural keeps\n'
        '  its own: **कूजो वर्तते; खर्जः; गर्जः; कूज्यं भवता; खर्ज्यम्,\n'
        '  गर्ज्यं भवता**'
    ),
)

register(
    '7.3.60',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — अजिवृज्योश्च — and अज् and व्रज्: **समाजः, उदाजः;\n'
        '  परिव्राजः, परिव्राज्यम्**. There is no example of अज् before\n'
        '  ण्यत्, 2.4.56 having replaced it with वी there — **अजेस्तु\n'
        '  अजेर्व्यघञपोः इति वीभावस्य विधानाद् ण्यति नास्त्युदाहरणम्**'
    ),
)

register(
    '7.3.61',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — भुजन्युब्जौ पाण्युपतापयोः — भुज and न्युब्ज are laid down\n'
        '  as a HAND and an AILMENT: **भुज्यतेऽनेनेति भुजः पाणिः; न्युब्जिताः\n'
        '  शेरतेऽस्मिन्निति न्युब्ज उपतापो रोगः**. For the first the guṇa is\n'
        '  refused as well, both being **निपात्यते** together'
    ),
)

register(
    '7.3.62',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — प्रयाजानुयाजौ यज्ञाङ्गे — प्रयाज and अनुयाज are laid down\n'
        '  as PARTS OF A RITE: **पञ्च प्रयाजाः; पञ्च अनुयाजाः**. And the two\n'
        '  are named as a specimen — **प्रदर्शनार्थम्, अन्यत्राप्येवंप्रकारे\n'
        '  कुत्वं न भवति** — so एकादशोपयाजाः, पत्नीसंयाजाः and ऋतुयाजैः all\n'
        '  come out the same way'
    ),
)

register(
    '7.3.63',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — वञ्चेर्गतौ — वञ्च् keeps its च् where GOING is meant:\n'
        '  **वञ्च्यं वञ्चन्ति वणिजः**, the traders travel a road that can be\n'
        '  travelled. **गताविति किम्? वङ्कं काष्ठम्। कुटिलम् इत्यर्थः** —\n'
        '  crooked wood, where the guttural comes'
    ),
)

register(
    '7.3.64',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — ओक उचः के — ओकस् is laid down from उच् before क, with both\n'
        '  the guttural and the guṇa: **न्योकः शकुन्तः; न्योको गृहम्**.\n'
        '\n'
        'SETTLED — **AND IT IS BUILT ON क RATHER THAN घञ् FOR THE ACCENT.**\n'
        '  **किमर्थं पुनर् अयं घञ्येव न व्युत्पाद्यते? स्वरार्थम्,\n'
        '  अन्तोदात्तोऽयम् इष्यते, घञि सत्याद्युदात्तः स्यात्** — the word is\n'
        '  wanted with its accent at the end, and a घञ् would have put it at\n'
        '  the front'
    ),
)

register(
    '7.3.65',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — ण्य आवश्यके — the change is refused before ण्य where\n'
        '  NECESSITY is meant: **अवश्यपाच्यम्, अवश्यवाच्यम्, अवश्यरेच्यम्**.\n'
        '  Six sūtras from here refuse it before this affix alone, and every\n'
        '  one of them turns on a sense'
    ),
)

register(
    '7.3.66',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — यजयाचरुचप्रवचर्चश्च — and for five roots: **याज्यम्,\n'
        '  याच्यम्, रोच्यम्, प्रवाच्यम्, अर्च्यम्**. प्रवच is named for the\n'
        '  sake of a technical term — **प्रवाच्यो नाम पाठविशेषोपलक्षितो\n'
        '  ग्रन्थोऽस्ति** — or, on another reading, to restrict the next\n'
        "  sūtra's refusal to that one preverb"
    ),
)

register(
    '7.3.67',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — वचोऽशब्दसंज्ञायाम् — and for वच् where the word is NOT a\n'
        '  technical term: **वाच्यमाह; अवाच्यमाह**. One sound between what is\n'
        '  said and what a grammar calls a sentence'
    ),
)

register(
    '7.3.68',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — प्रयोज्यनियोज्यौ शक्यार्थे — प्रयोज्य and नियोज्य are laid\n'
        '  down of what CAN be employed or enjoined: **शक्यः प्रयोक्तुं\n'
        '  प्रयोज्यः; शक्यो नियोक्तुं नियोज्यः**'
    ),
)

register(
    '7.3.69',
    apply=guttural,
    codification=_GUTTURAL,
    notes=(
        'SETTLED — भोज्यं भक्ष्ये — and भोज्य of FOOD: **भोज्य ओदनः; भोज्या\n'
        '  यवागूः**. **इह भक्ष्यम् अभ्यवहार्यमात्रम्** — anything swallowed,\n'
        '  and not the narrower sense the word has elsewhere'
    ),
)


_BEFORE_SIT = (
    'before_sit(root, gana=..., before=..., pada=..., chandasi=...) '
    '-> what the stem becomes before a sit, by rule of '
    '7.3.70-83.'
)

register(
    '7.3.70',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — घोर्लोपो लेटि वा — a घु root OPTIONALLY loses its vowel\n'
        '  before लेट्: **दधद् रत्नानि दाशुषे; सोमो ददद् गन्धर्वाय**. And वा\n'
        '  is said **विस्पष्टार्थम्** — someone might have feared that a loss\n'
        '  stated at all would displace ददात्, which comes by another road'
    ),
)

register(
    '7.3.71',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — ओतः श्यनि — an ओ-final stem loses it before श्यन्:\n'
        '  **निश्यति, अवच्छ्यति, अवद्यति, अवस्यति**. Four roots and four\n'
        '  forms, and each of the four is an ओ-final root of the दिवादि\n'
        '  class, which is where the श्यन् comes from at all'
    ),
)

register(
    '7.3.72',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — क्सस्याचि — the क्स affix loses its vowel before a\n'
        '  vowel-initial ending: **अधुक्षाताम्, अधुक्षाथाम्, अधुक्षि**'
    ),
)

register(
    '7.3.73',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — लुग्वा दुहदिहलिहगुहामात्मनेपदे दन्त्ये — four roots\n'
        '  OPTIONALLY drop the whole क्स in the आत्मनेपद before a dental:\n'
        '  **अदुग्ध, अधुक्षत; अदुग्धाः, अधुक्षथाः; अदिग्ध, अधिक्षत; अलीढ,\n'
        '  अलिक्षत; न्यगूढ, न्यघुक्षत**. लुक् is said rather than लोप\n'
        '  **सर्वादेशार्थम्, तच्च वह्यर्थम्** — so that अदुह्वहि may come\n'
        '  out, where dropping the last sound only would leave the wrong\n'
        '  thing behind'
    ),
)

register(
    '7.3.74',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — शमामष्टानां दीर्घः श्यनि — eight roots lengthen before\n'
        '  श्यन्: **शाम्यति, ताम्यति, दाम्यति, श्राम्यति, भ्राम्यति,\n'
        '  क्षाम्यति, क्लाम्यति, माद्यति**'
    ),
)

register(
    '7.3.75',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — ष्ठिवुक्लम्याचमां शिति — and three roots before any शित्:\n'
        '  **ष्ठीवति, क्लामति, आचामति**. क्लम् is named again although 7.3.74\n'
        '  has it, **शबर्थम्** — for the शप् conjugation, which श्यन् did not\n'
        '  reach'
    ),
)

register(
    '7.3.76',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — क्रमः परस्मैपदेषु — क्रम् lengthens before a शित् followed\n'
        '  by a परस्मैपद ending: **क्रामति, क्रामतः, क्रामन्ति**.\n'
        '\n'
        'SETTLED — **AND उत्क्राम KEEPS ITS LENGTH THOUGH ITS ENDING IS\n'
        '  GONE.** 1.1.63 should have stopped the rule reaching once the हि\n'
        '  is elided; **न च हौ क्रमिर् अङ्गम्। किं तर्हि? शपि** — the stem\n'
        '  the rule works on is the one before the शप्, not the one before\n'
        '  the हि, so the prohibition does not bite'
    ),
)

register(
    '7.3.77',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — इषुगमियमां छः — इष्, गम् and यम् take a छ् before a शित्:\n'
        '  **इच्छति, गच्छति, यच्छति**. The इष् meant is the उदित् one, and\n'
        '  readers who do not so read it carry अचि down from 7.3.72 instead —\n'
        '  **तत् च प्रधानम् अज्ग्रहणं शितीत्यनेन विशेष्यत इति वर्णयन्ति**'
    ),
)

register(
    '7.3.78',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — पाघ्राध्मास्थाम्नादाण्दृश्यर्त्तिसर्त्तिशदसदां\n'
        '  पिबजिघ्रधमतिष्ठमनयच्छपश्यर्च्छधौशीयसीदाः — eleven roots and eleven\n'
        '  stems, matched ONE TO ONE: **पिबति, जिघ्रति, धमति, तिष्ठति, मनति,\n'
        '  यच्छति, पश्यति, ऋच्छति, धावति, शीयते, सीदति**. The longest\n'
        '  यथासंख्यम् of the pāda, and crossing any pair is not Sanskrit.\n'
        '\n'
        'SETTLED — **AND THE vṛtti ARGUES ABOUT पिब TWICE OVER.** The light\n'
        '  penult should take guṇa; **अङ्गवृत्ते पुनर्वृत्ताव् अविधिर्\n'
        '  निष्ठितस्य** stops it. And whether the substitute is आ-final and\n'
        '  आद्युदात्त is a second question the vṛtti raises in the same\n'
        '  breath'
    ),
)

register(
    '7.3.79',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — ज्ञाजनोर्जा — ज्ञा and जन् become जा before a शित्:\n'
        '  **जानाति, जायते**. The जन् meant is the दैवादिक one, **जनेर्\n'
        '  दैवादिकस्य ग्रहणम्**'
    ),
)

register(
    '7.3.80',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — प्वादीनां ह्रस्वः — the प्वादि roots shorten before a\n'
        '  शित्: **पुनाति, लुनाति, स्तृणाति**.\n'
        '\n'
        'SETTLED — **AND WHERE THE LIST ENDS IS DISPUTED.** **केचिद्\n'
        '  इच्छन्ति** it runs from पूञ् to प्ली, the वृत् of the धातुपाठ\n'
        '  marking the end of both the ल्वादि and the प्वादि; **अपरे तु...\n'
        '  आगणान्ताः प्वादय इति**, to the end of the whole class. On the\n'
        "  second reading जानाति would shorten too, and 7.3.79's जा is what\n"
        '  saves it'
    ),
)

register(
    '7.3.81',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — मीनातेर्निगमे — and मी shortens in the Veda: **प्रमिणन्ति\n'
        '  व्रतानि**, they transgress the vows. **निगम इति किम्? प्रमीणाति**\n'
        '  — outside the Veda the long vowel stands, and निगम is the word\n'
        '  used for the Veda where छन्दसि would have done'
    ),
)

register(
    '7.3.82',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        "SETTLED — मिदेर्गुणः — मिद्'s इ takes guṇa before a शित्: **मेद्यति,\n"
        "  मेद्यतः, मेद्यन्ति**. **शितीत्येव — मिद्यते** — the passive's यक्\n"
        '  is no शित्, so the vowel stays short there, and one root shows\n'
        '  both forms side by side'
    ),
)

register(
    '7.3.83',
    apply=before_sit,
    codification=_BEFORE_SIT,
    notes=(
        'SETTLED — जुसि च — and an इक्-final stem takes guṇa before जुस्:\n'
        '  **अजुहवुः, अबिभयुः, अबिभरुः**.\n'
        '\n'
        'SETTLED — **AND WHY चिनुयुः HAS NONE IS WORKED OUT IN FULL.** Two\n'
        '  ङित्-conditions are in play there, one from the सार्वधातुक and one\n'
        '  from the यासुट्. This rule displaces the first, having nowhere\n'
        '  else to apply against it — **नाप्राप्ते... प्रतिषेधे जुसि गुण\n'
        '  आरभ्यमाणस्तम् एव बाधते** — but not the second, which it meets in a\n'
        '  place where it could have applied anyway, **तत्र हि प्राप्ते\n'
        '  चाप्राप्ते चारभ्यत इति**'
    ),
)


register(
    '7.3.84',
    reuses=('1.1.2', '1.1.3', '1.1.4'),
    apply=guna_before_affix,
    codification=(
        'guna_before_affix(stem, sarvadhatuka=..., ardhadhatuka=...) -> the '
        'stem after guṇa, and the rules that decided each part of it.'
    ),
    related=('1.1.3', '1.1.50', '1.1.51', '3.1.68', '3.4.113', '7.3.82'),
    notes=(
        'SETTLED — सार्वधातुक आर्धधातुके च प्रत्यये परत इगन्तस्य अङ्गस्य\n'
        '  गुणो भवति. Worked as तरति, नयति, भवति for the sārvadhātuka and\n'
        '  कर्ता, चेता, स्तोता for the ārdhadhātuka.\n'
        '\n'
        'SETTLED — the condition, and what it prevents. The Kāśikā asks\n'
        '  सार्वधातुकार्धधातुकयोरिति किम्? and answers अग्नित्वम्,\n'
        '  अग्निकाम्यति: the affix there is neither, and अग्नि keeps its इ.\n'
        '  It adds the reason the sūtra does not simply say "before an\n'
        '  affix" — यदि हि प्रत्यये ङिति वोच्येत, इहापि स्यात्.\n'
        '\n'
        'SETTLED — this sūtra says गुणः and names no target. What supplies\n'
        '  it is 1.1.3 इको गुणवृद्धी, and the Kāśikā writes the target in\n'
        '  as इगन्तस्य अङ्गस्य when glossing. So the codification does not\n'
        '  decide where the substitution lands; it asks 1.1.3, and asks\n'
        '  1.1.50 which of अ, ए, ओ goes there. Both are already codified,\n'
        '  and the verdict names them.\n'
        '\n'
        'SCAR — only the WORD गुणः is read down from 7.3.82. That sūtra is\n'
        '  मिदेर्गुणः and its own scope is the root मिद् — मेद्यति — so it\n'
        '  is not a general guṇa rule that this one merely extends. Reading\n'
        '  the anuvṛtti field as though the scope came with the word would\n'
        '  have made 7.3.82 do work it does not do.'
    ),
)


register(
    '7.3.101',
    apply=ato_dirgho_yani,
    reuses=('1.1.71',),
    codification=(
        'ato_dirgho_yani(stem, ending, sarvadhatuka=...) -> the aṅga with '
        'its final अ lengthened.'
    ),
    related=('1.1.71', '3.4.113'),
    notes=(
        'SETTLED — अकारान्तस्य अङ्गस्य दीर्घो भवति यञादौ सार्वधातुके\n'
        '  परतः: पचामि, पचावः, पचामः.\n'
        '\n'
        'SETTLED — both conditions are tested by the Kāśikā and both are\n'
        '  codified. अत इति किम्? चिनुवः, चिनुमः — the aṅga is not अ-final.\n'
        '  यञीति किम्? पचतः, पचथः — त् and थ् are not यञ्.\n'
        '\n'
        'NOTE — यञ् is resolved through 1.1.71 rather than written out, and\n'
        '  it reaches further than one might guess: eleven sounds, ending\n'
        '  झ् and भ्, because its marker ञ् closes the eighth śivasūtra and\n'
        '  not the sixth. Listing it by hand would very likely have listed\n'
        '  nine.'
    ),
)

_BEFORE_SARVADHATUKA = (
    'before_sarvadhatuka(root, gana=..., before=..., result=..., '
    'chandasi=...) -> whether the vowel is strengthened and what '
    'augment comes, by rule of 7.3.85-100.'
)

register(
    '7.3.85',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — जाग्रोऽविचिण्णल्ङित्सु — जागृ takes guṇa except before वि,\n'
        '  चिण्, णल् and a ङित्: **जागरयति, जागरकः, साधुजागरी, जागरो वर्तते;\n'
        '  जागरितः, जागरितवान्**.\n'
        '\n'
        'SETTLED — **AND THE GUṆA IS STATED SO THAT THE vṛddhi SHALL NOT\n'
        '  COME.** **वृद्धिविषये प्रतिषेधविषये च यथा स्याद् इति जागर्तेर् अयं\n'
        "  गुण आरभ्यते** — once the guṇa is in, 7.2.116's vṛddhi has no अ in\n"
        '  the penult to work on. **यदि हि स्याद् अनर्थक एव गुणः स्यात्** —\n'
        '  and the exception for चिण् and णल् would be idle besides'
    ),
)

register(
    '7.3.86',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — पुगन्तलघूपधस्य च — a stem ending in पुक् and one with a\n'
        '  LIGHT penult take guṇa before a सार्वधातुक or an आर्धधातुक:\n'
        '  **व्लेपयति, ह्रेपयति, क्नोपयति** for the first; **भेदनम्, छेदनम्,\n'
        '  भेत्ता, छेत्ता** for the second. This is why so many verbal nouns\n'
        '  have an ए where the root has an इ.\n'
        '\n'
        'SETTLED — **AND A VERSE ASKS HOW भेत्ता IS POSSIBLE AT ALL.**\n'
        '  **संयोगे गुरुसंज्ञायां गुणो भेत्तुर् न सिध्यति** — with the\n'
        '  cluster of the affix after it the penult is heavy and not light.\n'
        "  The answer is read out of 3.2.140 and 1.2.10's marking the क्नु\n"
        '  and सन् as कित्, which would be pointless unless the guṇa reached\n'
        '  across a cluster'
    ),
)

register(
    '7.3.87',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — नाभ्यस्तस्याचि पिति सार्वधातुके — but a REDUPLICATED stem\n'
        '  with a light penult does not take it before a vowel-initial पित्\n'
        '  सार्वधातुक: **नेनिजानि, वेविजानि, परिवेविषाणि; अनेनिजम्,\n'
        '  अवेविजम्**. A vārttika lets the Veda off — **बहुलं छन्दसीति\n'
        '  वक्तव्यम्**, which is how जुजोषत् comes out'
    ),
)

register(
    '7.3.88',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — भूसुवोस्तिङि — भू and सू do not take guṇa before a तिङ्:\n'
        '  **अभूत्, अभूः, अभूवम्; सुवै, सुवावहै, सुवामहै**. The सू meant is\n'
        '  the one whose विकरण is elided, the other being kept from the guṇa\n'
        '  by its own ङित् विकरण anyway.\n'
        '\n'
        'SETTLED — **AND WHY बोभवीति KEEPS ITS GUṆA IS ANSWERED FROM A RULE A\n'
        '  PĀDA AWAY.** **ज्ञापकात्, यद् अयं बोभूतु इति गुणाभावार्थं निपातनं\n'
        '  करोति** — 7.4.65 lays down बोभूतु expressly without guṇa, and\n'
        '  would not need to if this refusal reached there'
    ),
)

register(
    '7.3.89',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — उतो वृद्धिर्लुकि हलि — an उ-final stem takes VṚDDHI before\n'
        '  a consonant-initial पित् सार्वधातुक where the विकरण has been\n'
        '  elided: **यौति, यौषि, यौमि; नौति; स्तौति, स्तौषि, स्तौमि**. In अपि\n'
        '  स्तुयाद् राजानम् the ending is ङित् and so not पित्, and no vṛddhi\n'
        '  comes'
    ),
)

register(
    '7.3.90',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — ऊर्णोतेर्विभाषा — and ऊर्णु takes it OPTIONALLY:\n'
        '  **प्रोर्णौति, प्रोर्णोति; प्रोर्णौषि, प्रोर्णोषि; प्रोर्णौमि,\n'
        '  प्रोर्णोमि**'
    ),
)

register(
    '7.3.91',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — गुणोऽपृक्ते — but where that ending is a single sound the\n'
        '  change is guṇa and not vṛddhi: **प्रौर्णोत्, प्रौर्णोः**.\n'
        '\n'
        'SETTLED — **AND THE WORD अपृक्त IS ITSELF A ज्ञापक.** हलि was\n'
        '  already running, so naming the single-sound ending adds nothing\n'
        '  unless a paribhāṣā is being taught: **तेनैव ज्ञाप्यते भवत्येषा\n'
        '  परिभाषा — यस्मिन् विधिस्तदादावल्ग्रहणे इति**'
    ),
)

register(
    '7.3.92',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — तृणह इम् — तृणह् takes the augment इम् before a\n'
        '  consonant-initial पित् सार्वधातुक: **तृणेढि, तृणेक्षि, तृणेह्मि,\n'
        '  अतृणेट्**. The तृणह् meant is the one that HAS its श्नम् —\n'
        '  **आगतश्नम्को गृह्यते, श्नमि कृत इमागमो यथा स्यात्** — so the two\n'
        '  augments go in one after the other'
    ),
)

register(
    '7.3.93',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — ब्रुव ईट् — ब्रू takes ईट् before a consonant-initial पित्\n'
        '  सार्वधातुक: **ब्रवीति, ब्रवीषि, ब्रवीमि, अब्रवीत्**'
    ),
)

register(
    '7.3.94',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — यङो वा — and after यङ् it is optional: **शाकुनिको लालपीति;\n'
        '  दुन्दुभिर्वावदीति; त्रिधा बद्धो वृषभो रोरवीति**'
    ),
)

register(
    '7.3.95',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — तुरुस्तुशम्यमः सार्वधातुके — five roots take it\n'
        '  optionally: **उत्तौति, उत्तवीति; उपरौति, उपरवीति; उपस्तौति,\n'
        '  उपस्तवीति; शाम्यध्वम्, शमीध्वम्; अभ्यमति, अभ्यमीति**. The तु is a\n'
        '  root known only from this sūtra — **तु इति सौत्रोऽयं धातुः** — and\n'
        '  the Āpiśalas read the whole rule as Vedic'
    ),
)

register(
    '7.3.96',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — अस्तिसिचोऽपृक्ते — अस् and a सिच्-final stem take ईट्\n'
        '  before a single-sound सार्वधातुक: **आसीत्, आसीः; अकार्षीत्,\n'
        '  असावीत्, अलावीत्, अपावीत्**. A vārttika refuses the ईट् to आह् and\n'
        '  भू — **आहिभुवोर् ईटि प्रतिषेधः** — so आत्थ and अभूत् stand'
    ),
)

register(
    '7.3.97',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — बहुलं छन्दसि — and in the Veda it is बहुलम्: **आप एवेदं\n'
        '  सलिलं सर्वम् आः** for आसीत्; **गोभिर् अक्षाः; प्रत्यञ्चम् अत्साः**\n'
        '  for the सिच्. The Vedic freedom goes further than the augment —\n'
        '  **छान्दसत्वाद् माङ्योगेऽप्यडागमो भवति**, and the सिच् loses its\n'
        '  इट् besides'
    ),
)

register(
    '7.3.98',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        'SETTLED — रुदश्च पञ्चभ्यः — and the five रुदादि roots: **अरोदीत्,\n'
        '  अरोदीः; अस्वपीत्; अश्वसीत्; प्राणीत्; अजक्षीत्**. The same five\n'
        '  7.2.76 gave an इट् before a वल्-initial सार्वधातुक — one list, two\n'
        '  augments, two pādas apart'
    ),
)

register(
    '7.3.99',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        "SETTLED — अड्गार्ग्यगालवयोः — and in GĀRGYA's and GĀLAVA's view they\n"
        '  take अट् instead: **अरोदत्, अरोदः; अस्वपत्; अश्वसत्; प्राणत्;\n'
        '  अजक्षत्**.\n'
        '\n'
        'SETTLED — **AND NAMING THE TWO IS NOT TO MARK A DISSENT.**\n'
        '  **गार्ग्यगालवयोर्ग्रहणं पूजार्थम्** — it is done in their honour,\n'
        '  which is a different thing from the views recorded at 7.1.74 and\n'
        '  7.2.63, where the naming makes the rule an option in the language'
    ),
)

register(
    '7.3.100',
    apply=before_sarvadhatuka,
    codification=_BEFORE_SARVADHATUKA,
    notes=(
        "SETTLED — अदः सर्वेषाम् — and अद् takes it in EVERY teacher's view:\n"
        '  **आदत्, आदः**. The contrast with the sūtra before is the whole\n'
        '  content: there two teachers, here all of them, and the augment the\n'
        '  same'
    ),
)


_BEFORE_ENDING = (
    'before_ending(stem, gana=..., before=..., gender=...) -> '
    'what the stem and the ending become, by rule of '
    '7.3.101-120.'
)

register(
    '7.3.102',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — सुपि च — and before such a CASE ending: **वृक्षाय,\n'
        '  प्लक्षाय; वृक्षाभ्याम्, प्लक्षाभ्याम्**. This is the lengthening\n'
        "  7.1.13's ङेर्यः needed and could not state, being about the ending\n"
        '  and not the stem'
    ),
)

register(
    '7.3.103',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — बहुवचने झल्येत् — and becomes ए before a झल्-initial\n'
        '  PLURAL case ending: **वृक्षेभ्यः, प्लक्षेभ्यः; वृक्षेषु,\n'
        '  प्लक्षेषु**'
    ),
)

register(
    '7.3.104',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — ओसि च — and before ओस्: **वृक्षयोः स्वम्, प्लक्षयोः स्वम्;\n'
        '  वृक्षयोर् निधेहि, प्लक्षयोर् निधेहि**. The ओस् is the ending of\n'
        '  two cases at once, the genitive and the locative dual, and the\n'
        '  vṛtti gives an example of each rather than leaving the reader to\n'
        '  supply the second'
    ),
)

register(
    '7.3.105',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — आङि चापः — an आप्-final stem becomes ए before the\n'
        '  instrumental singular and before ओस्: **खट्वया, मालया; खट्वयोः,\n'
        "  मालयोः; बहुराजया, कारीषगन्ध्यया**. आङ् is the older teachers' name\n"
        '  for that ending — **आङिति पूर्वाचार्यनिर्देशेन तृतीयैकवचनं\n'
        '  गृह्यते**'
    ),
)

register(
    '7.3.106',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — सम्बुद्धौ च — and in the vocative singular: **हे खट्वे; हे\n'
        '  बहुराजे; हे कारीषगन्ध्ये**. **आप इति वर्तते** — the आप् is carried\n'
        "  down from the sūtra before, so a stem whose आ is a root's own is\n"
        '  not reached, and this is the first of the four rules the vocative\n'
        '  gets'
    ),
)

register(
    '7.3.107',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — अम्बाऽर्थनद्योर्ह्रस्वः — the words for MOTHER and the नदी\n'
        '  stems shorten in the vocative: **हे अम्ब, हे अक्क, हे अल्ल; हे\n'
        '  कुमारि, हे शार्ङ्गरवि, हे ब्रह्मबन्धु, हे वीरबन्धु**. Two\n'
        '  vārttikas add the exceptions and then make them optional in the\n'
        '  Veda, and a third takes in the तल्-final stems: **तलो ह्रस्वो वा\n'
        '  ङिसंबुद्ध्योः**'
    ),
)

register(
    '7.3.108',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — ह्रस्वस्य गुणः — a short-final stem takes guṇa in the\n'
        '  vocative: **हे अग्ने, हे वायो, हे पटो**.\n'
        '\n'
        'SETTLED — **AND IT CANNOT REACH THE STEMS THE SŪTRA BEFORE\n'
        '  SHORTENED.** हे कुमारि and हे ब्रह्मबन्धु keep their short vowels\n'
        '  — **ह्रस्वविधानसामर्थ्याद् गुणो न भवति**, the shortening would be\n'
        '  pointless if the guṇa followed it. And the vṛtti proves it from\n'
        '  how Pāṇini would have written the pair otherwise: **यदि गुण इष्टः\n'
        '  स्यात्, अम्बार्थानां ह्रस्व इत्युक्त्वा नदीह्रस्वयोर् गुण इत्येवं\n'
        '  ब्रूयात्**'
    ),
)

register(
    '7.3.109',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — जसि च — and before जस्: **अग्नयः, वायवः, पटवः, धेनवः,\n'
        '  बुद्धयः**. A vārttika makes everything from here to 7.4.1 optional\n'
        '  in the Veda — **इतः प्रकरणात् प्रभृति छन्दसि वेति वक्तव्यम्** —\n'
        '  which is how अम्बे beside अम्ब and शतक्रत्वः beside शतक्रतवः both\n'
        '  stand'
    ),
)

register(
    '7.3.110',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — ऋतो ङिसर्वनामस्थानयोः — an ऋ-final stem takes guṇa before\n'
        '  ङि and before a strong ending: **मातरि, पितरि, भ्रातरि, कर्तरि**;\n'
        '  **कर्तारौ, कर्तारः, मातरौ, पितरौ**'
    ),
)

register(
    '7.3.111',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — घेर्ङिति — a घि stem takes guṇa before a ङित् ending:\n'
        '  **अग्नये, वायवे; अग्नेर् आगच्छति, वायोर् आगच्छति; अग्नेः स्वम्,\n'
        '  वायोः स्वम्**'
    ),
)

register(
    '7.3.112',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — आण्नद्याः — after a नदी stem the ङित् ending takes the\n'
        '  augment आट्: **कुमार्यै, ब्रह्मबन्ध्वै; कुमार्याः,\n'
        '  ब्रह्मबन्ध्वाः**. From here the run is about the ENDING and not\n'
        '  the stem'
    ),
)

register(
    '7.3.113',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — याडापः — and after an आप् stem, याट्: **खट्वायै,\n'
        '  बहुराजायै, कारीषगन्ध्यायै; खट्वायाः, बहुराजायाः**. And whether\n'
        '  अतिखट्वा takes it turns on when the lengthening is done: **अकृते\n'
        '  दीर्घे ङ्याब्ग्रहणेऽदीर्घः इति वचनाद् याडागमो न भवति, कृते तु\n'
        '  लाक्षणिकत्वात्** — before it, no; after it, yes'
    ),
)

register(
    '7.3.114',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — सर्वनाम्नः स्याड्ढ्रस्वश्च — after an आप्-final PRONOUN\n'
        '  the ending takes स्याट् AND the stem shortens: **सर्वस्यै,\n'
        '  विश्वस्यै, यस्यै, तस्यै, कस्यै; सर्वस्याः, यस्याः, कस्याः**. Two\n'
        '  operations in one sūtra, and the shortening is what makes the\n'
        '  स्याट् audible'
    ),
)

register(
    '7.3.115',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — विभाषा द्वितीयातृतीयाभ्याम् — and after द्वितीय and तृतीय\n'
        '  it is OPTIONAL, with the same shortening: **द्वितीयस्यै,\n'
        '  द्वितीयायै; तृतीयस्यै, तृतीयायै**'
    ),
)

register(
    '7.3.116',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — ङेराम्नद्याम्नीभ्यः — after a नदी stem, an आप् stem and\n'
        '  नी, the locative singular ङि becomes आम्: **कुमार्याम्, गौर्याम्,\n'
        '  ब्रह्मबन्ध्वाम्** for the नदी; **खट्वायाम्, बहुराजायाम्** for the\n'
        '  आप्; **राजन्याम्, सेनान्याम्, ग्रामण्याम्** for नी'
    ),
)

register(
    '7.3.117',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — इदुद्भ्याम् — and after an इ or उ that is a नदी:\n'
        '  **कृत्याम्, धेन्वाम्**. The sūtra before had reached the नदी stems\n'
        '  by that name; this one names the two vowels, and what it adds is\n'
        "  the stems that are नदी by 1.4.6's option rather than by 1.4.3"
    ),
)

register(
    '7.3.118',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — औत् — and after an इ or उ that is NEITHER a नदी nor a घि,\n'
        '  the ङि becomes औ: **सख्यौ, पत्यौ**. The sūtra is one word, and\n'
        '  what it reaches is what the two rules before it left'
    ),
)

register(
    '7.3.119',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — अच्च घेः — and after a घि stem the ङि becomes औ AND the\n'
        "  घि's own vowel becomes अ: **अग्नौ, वायौ, कृतौ, धेनौ, पटौ**. The\n"
        "  तपर keeps the feminine's टाप् out. Some read this and the sūtra\n"
        '  before as ONE rule — **औदच्च घेरिति येषाम् एकम् एवेदं सूत्रम्** —\n'
        '  and then the औ is the main provision and the अ an afterthought to\n'
        '  it'
    ),
)

register(
    '7.3.120',
    apply=before_ending,
    codification=_BEFORE_ENDING,
    notes=(
        'SETTLED — आङो नाऽस्त्रियाम् — and after a घि stem the instrumental\n'
        '  singular becomes ना, except in the feminine: **अग्निना, वायुना,\n'
        '  पटुना**. The sūtra says *not feminine* rather than *masculine* on\n'
        '  purpose — **पुंसि इति नोक्तम् — अमुना ब्राह्मणकुलेन**, since a\n'
        '  neuter needs it too. This closes पाद ७.३: **इति श्रीवामनविरचितायां\n'
        '  काशिकायां वृत्तौ सप्तमाध्यायस्य तृतीयः पादः**'
    ),
)


__all__ = [
    'ato_dirgho_yani',
    'before_ending',
    'before_ni',
    'before_sarvadhatuka',
    'before_sit',
    'guna_before_affix',
    'guttural',
    'the_ka',
    'uttarapada_vrddhi',
]
