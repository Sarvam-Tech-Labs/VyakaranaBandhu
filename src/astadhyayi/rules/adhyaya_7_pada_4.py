# -*- coding: utf-8 -*-
r"""अध्याय ७, पाद ४ — what happens to the reduplicated copy."""

from __future__ import annotations

from src.astadhyayi.dvirvacana import for_sutra
from src.astadhyayi.abhyasa import in_the_copy
from src.astadhyayi.angi_agama import to_the_stem
from src.astadhyayi.cangi import before_cang
from src.astadhyayi.dirgha_yaki import before_ya
from src.astadhyayi.kiti_sani import before_kit
from src.astadhyayi.sources import register

_CODIFICATION = (
    "Runs the whole reduplication and reports for this sūtra alone: the "
    "finished stem, whether this rule was among those that acted, and "
    "what each of them did."
)

_BEFORE_CANG = (
    'before_cang(root, gana=..., before=..., part=..., chandasi=...) '
    '-> the stem vowel before cang and in the perfect, by rule of '
    '7.4.1-12.'
)

register(
    '7.4.1',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        'SETTLED — णौ चङ्युपधाया ह्रस्वः — the penult of a causal stem\n'
        '  shortens before चङ्: **अचीकरत्, अजीहरत्, अलीलवत्, अपीपवत्**.\n'
        '\n'
        'SETTLED — **AND THE ORDER AGAINST THE REDUPLICATION IS SETTLED TWICE\n'
        '  OVER.** In अचीकरत् the shortening wins by being later — **परत्वाद्\n'
        '  उपधाह्रस्वत्वम्, तत्र कृते द्विर्वचनम्**. In मा भवान् अटिटत् the\n'
        '  doubling is compulsory and should win, and then the penult would\n'
        '  be gone before the shortening could reach it. **नैष दोषः। ओणेः\n'
        '  ऋदित्करणं ज्ञापकं नित्यम् अपि द्विर्वचनम् उपधाह्रस्वत्वेन बाध्यते\n'
        '  इति** — marking ओण् as ऋदित् in the next sūtra would be idle\n'
        '  otherwise'
    ),
)

register(
    '7.4.2',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        'SETTLED — नाग्लोपिशास्वृदिताम् — but a stem that has lost a vowel,\n'
        '  and शास्, and the ऋदित् roots, do NOT shorten: **अममालत्,\n'
        '  अमामतरत्, अत्यरराजत्, अन्वलुलोमत्; अशशासत्; अबबाधत्, अययाचत्,\n'
        '  अडुढौकत्**. Where the vowel alone is lost 1.1.56 would have saved\n'
        '  the form anyway; the sūtra is for where a consonant goes with it —\n'
        '  **हलचोरादेशे तु न सिध्यतीति तदर्थम् एतद् वचनम्**'
    ),
)

register(
    '7.4.3',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        'SETTLED — भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम् — seven roots shorten\n'
        '  OPTIONALLY: **अबिभ्रजत्, अबभ्राजत्; अबीभसत्, अबभासत्; अदीदिपत्,\n'
        '  अदिदीपत्; अजीजिवत्, अजिजीवत्; अमीमिलत्, अमिमीलत्; अपीपिडत्,\n'
        '  अपिपीडत्**. The vṛtti rejects one reading of the list outright —\n'
        '  **भ्राजभासोर् ऋदित्करणम् अपाणिनीयम्** — and a vārttika adds कण and\n'
        '  वण'
    ),
)

register(
    '7.4.4',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        'SETTLED — लोपः पिबतेरीच्चाभ्यासस्य — पिब loses its penult altogether\n'
        '  and its reduplication takes ई: **अपीप्यत्, अपीप्यताम्, अपीप्यन्**.\n'
        '  That the doubling happens at all after the loss is read out of\n'
        '  another rule — **ओः पुयण् वचनं ज्ञापकं णौ स्थानिवद्भावस्य**'
    ),
)

register(
    '7.4.5',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        "SETTLED — तिष्ठतेरित् — and तिष्ठ's penult becomes इ: **अतिष्ठिपत्,\n"
        '  अतिष्ठिपताम्, अतिष्ठिपन्**. The stem named is तिष्ठ and not स्था,\n'
        "  so 7.3.78's substitution has already been made when this rule\n"
        "  reaches — one पाद's output being the next one's input, named by\n"
        '  its finished shape'
    ),
)

register(
    '7.4.6',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        "SETTLED — जिघ्रतेर्वा — and जिघ्र's OPTIONALLY: **अजिघ्रिपत्,\n"
        '  अजिघ्रिपताम्, अजिघ्रिपन्; अजिघ्रपत्, अजिघ्रपताम्, अजिघ्रपन्**'
    ),
)

register(
    '7.4.7',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        'SETTLED — उर्ऋत् — an ऋ in the penult optionally becomes a plain ऋ:\n'
        '  **अचिकीर्तत्, अचीकृतत्; अववर्तत्, अवीवृतत्; अममार्जत्, अमीमृजत्**.\n'
        '\n'
        'SETTLED — **AND IT BEATS THREE INNER RULES BY BEING STATED AT ALL.**\n'
        '  **वचनसामर्थ्याद् अन्तरङ्गा अपि इररारो बाध्यन्ते** — the इर्, अर्\n'
        '  and आर् substitutions are अन्तरङ्ग and would come first, and the\n'
        '  sūtra would be idle if they did. The तपर is what keeps the\n'
        '  substitute short even for a long ॠ'
    ),
)

register(
    '7.4.8',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        'SETTLED — नित्यं छन्दसि — and in the Veda it is COMPULSORY:\n'
        '  **अवीवृधत् पुरोडाशेन; अवीवृधताम्; अवीवृधन्**. The option of the\n'
        '  sūtra before does not reach there'
    ),
)

register(
    '7.4.9',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        'SETTLED — दयतेर्दिगि लिटि — दय् becomes दिगि in the perfect:\n'
        '  **अवदिग्ये, अवदिग्याते, अवदिग्यिरे**. The दय् meant is दीङ् and\n'
        '  not **दय दाने**, which takes आम् in the perfect instead. And the\n'
        '  substitute displaces the reduplication — **दिग्यादेशेन\n'
        '  द्विर्वचनस्य बाधनम् इष्यते**'
    ),
)

register(
    '7.4.10',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        'SETTLED — ऋतश्च संयोगादेर्गुणः — an ऋ-final root BEGINNING with a\n'
        '  cluster takes guṇa in the perfect: **सस्वरतुः, सस्वरुः; दध्वरतुः,\n'
        '  दध्वरुः; सस्मरतुः, सस्मरुः**. It is stated so as to reach even\n'
        '  where 1.1.5 refuses — **प्रतिषेधविषयेऽपि गुणो यथा स्यात्** — and\n'
        '  where vṛddhi could come instead, vṛddhi wins by prior\n'
        '  contradiction: **सस्वार, सस्मार**'
    ),
)

register(
    '7.4.11',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        'SETTLED — ऋच्छत्यॄताम् — and ऋच्छ्, ऋ and the ॠ-final roots:\n'
        '  **आनर्च्छ, आनर्च्छतुः; आरतुः, आरुः; निचकरतुः, निजगरतुः**. For\n'
        '  ऋच्छ् the guṇa was never available and for the ॠ-final roots it\n'
        '  was refused, so the sūtra does two different things at once. And\n'
        '  vṛddhi still wins where it can: **निचकार, निजगार**'
    ),
)

register(
    '7.4.12',
    apply=before_cang,
    codification=_BEFORE_CANG,
    notes=(
        "SETTLED — शृदॄप्रां ह्रस्वो वा — three roots' vowel is OPTIONALLY\n"
        '  short in the perfect: **विशश्रतुः, विशशरतुः; विदद्रतुः, विददरतुः;\n'
        '  निपप्रतुः, निपपरतुः**. **ह्रस्ववचनम् इत्वोत्वनिवृत्त्यर्थम्** —\n'
        '  *short* is said rather than a substitute, to keep the इ and उ of\n'
        '  other rules out. And some reject the sūtra outright, deriving the\n'
        '  short forms from three separate roots श्रा, द्रा and प्रा instead'
    ),
)


_TO_THE_STEM_7_4 = (
    'to_the_stem(root, gana=..., before=..., upasarga=...) -> what '
    'happens before ka, in the ang aorist and before ya, by rule '
    'of 7.4.13-24.'
)

register(
    '7.4.13',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — केऽणः — a long अण् vowel shortens before क: **ज्ञका;\n'
        '  कुमारिका; किशोरिका**. And the क reached is the one WITH its\n'
        '  markers, which the refusal in the next sūtra proves — **न कपि इति\n'
        '  प्रतिषेधसामर्थ्यात् कनोऽपि सानुबन्धकस्य ग्रहणम् इह भवति**'
    ),
)

register(
    '7.4.14',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — न कपि — but not before कप्: **बहुकुमारीकः, बहुवधूकः,\n'
        "  बहुलक्ष्मीकः**. And 1.2.48's shortening does not reach there\n"
        '  either, the कप् being added to the second member before the\n'
        '  compound is made — **स्त्रीप्रत्ययान्तसमासप्रातिपदिकं न भवति**'
    ),
)

register(
    '7.4.15',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — आपोऽन्यतरस्याम् — and for an आप्-final stem the refusal is\n'
        '  only half: **बहुखट्वाकः, बहुखट्वकः; बहुमालाकः, बहुमालकः**'
    ),
)

register(
    '7.4.16',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — ऋदृशोऽङि गुणः — an ऋ-final root and दृश् take guṇa before\n'
        '  the अङ् aorist: **शकलाङ्गुष्ठकोऽकरत्; अहं तेभ्योऽकरं नमः; असरत्,\n'
        '  आरत्, जरा**; and for दृश् **अदर्शत्, अदर्शताम्, अदर्शन्**'
    ),
)

register(
    '7.4.17',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — अस्यतेस्थुक् — अस् takes the augment थुक् before अङ्:\n'
        '  **आस्थत्, आस्थताम्, आस्थन्**. The अस् meant is **असु क्षेपणे**,\n'
        "  the throwing-root, and not the अस् of being — this run's four\n"
        '  rules each name one root and give it one thing'
    ),
)

register(
    '7.4.18',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — श्वयतेरः — and श्वि becomes अ: **अश्वत्, अश्वताम्,\n'
        '  अश्वन्**. A substitute and not an augment, unlike the two rules on\n'
        '  either side of it, and the shortest of the four'
    ),
)

register(
    '7.4.19',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — पतः पुम् — and पत् takes पुम्: **अपप्तत्, अपप्तताम्,\n'
        '  अपप्तन्**. The म् is a marker and the प् is what goes in, put\n'
        '  before the last vowel by 1.1.47 — so पत् becomes प्पत् and then,\n'
        '  with the reduplication, अपप्तत्'
    ),
)

register(
    '7.4.20',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — वच उम् — and वच् takes उम्: **अवोचत्, अवोचताम्, अवोचन्**.\n'
        '\n'
        'SETTLED — **AND WHAT COMES OUT HAS NO VISIBLE RELATION TO ITS\n'
        '  ROOT.** The उम् is put inside the stem by 1.1.47, the vowels\n'
        "  merge, and वच् + अङ् gives अवोचत् — one of the language's oddest\n"
        '  aorists, and the reason it is odd is stated in three syllables'
    ),
)

register(
    '7.4.21',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — शीङः सार्वधातुके गुणः — शीङ् takes guṇa before a\n'
        '  सार्वधातुक: **शेते, शयाते, शेरते**. 1.1.5 would have refused it,\n'
        '  the endings being ङित्; the sūtra exists to reach past that\n'
        '  refusal, and शिश्ये in the perfect shows what the root does\n'
        '  without it'
    ),
)

register(
    '7.4.22',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — अयङ् यि क्ङिति — and अयङ् before a क्ङित् affix beginning\n'
        '  with य्: **शय्यते, शाशय्यते, प्रशय्य, उपशय्य**'
    ),
)

register(
    '7.4.23',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — उपसर्गाद्ध्रस्व ऊहतेः — ऊह् shortens after a preverb\n'
        '  before a क्ङित् य्: **समुह्यते, समुह्य गतः; अभ्युह्यते, अभ्युह्य\n'
        '  गतः**. And the अण् of 7.4.13 is still running, so ओह्यते and\n'
        '  समोह्यते are out'
    ),
)

register(
    '7.4.24',
    apply=to_the_stem,
    codification=_TO_THE_STEM_7_4,
    notes=(
        'SETTLED — एतेर्लिङि — and इ shortens after a preverb in the\n'
        '  optative: **उदियात्, समियात्, अन्वियात्**. The lengthening of\n'
        '  7.4.25 has already been done and this undoes it — **आशिषि लिङि\n'
        '  अकृत्सार्वधातुकयोः इति दीर्घत्वे कृते ह्रस्वोऽनेन भवति**'
    ),
)


_BEFORE_YA = (
    'before_ya(stem, gana=..., before=..., sense=..., chandasi=...) '
    '-> the stem vowel before ya, cvi and kyac, by rule of '
    '7.4.25-40.'
)

register(
    '7.4.25',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — अकृत्सार्वधातुकयोर्दीर्घः — a vowel-final stem lengthens\n'
        "  before a क्ङित् य् that is neither a कृत्'s nor a सार्वधातुक's:\n"
        '  **भृशायते, सुखायते, दुःखायते; चीयते, चेचीयते; स्तूयते, तोष्टूयते;\n'
        '  चीयात्, स्तूयात्**'
    ),
)

register(
    '7.4.26',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — च्वौ च — and before च्वि: **शुचीकरोति, शुचीभवति,\n'
        '  शुचीस्यात्; पटूकरोति, पटूभवति, पटूस्यात्**'
    ),
)

register(
    '7.4.27',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — रीङ् ऋतः — an ऋ-final stem takes रीङ् instead:\n'
        '  **मात्रीयति, मात्रीयते; पित्रीयति, पित्रीयते; चेक्रीयते;\n'
        '  मात्रीभूतः**. And क्ङिति has lapsed here — **क्ङिति इत्येतन्\n'
        '  निवृत्तम्** — so पित्र्यम् comes out too'
    ),
)

register(
    '7.4.28',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — रिङ् शयग्लिङ्क्षु — but रिङ् before श, यक् and the\n'
        '  optative: **आद्रियते, आध्रियते** for the श; **क्रियते, ह्रियते**\n'
        '  for the यक्; **क्रियात्, ह्रियात्** for the optative. **रिङ्वचनं\n'
        '  दीर्घनिवृत्त्यर्थम्** — a short substitute stated so that the\n'
        '  lengthening shall not come'
    ),
)

register(
    '7.4.29',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — गुणोऽर्तिसंयोगाद्योः — and ऋ, and an ऋ-final root\n'
        '  beginning with a cluster, take guṇa: **अर्यते, अर्यात्; स्मर्यते,\n'
        '  स्मर्यात्**. संस्क्रियते has none, its सुट् being either असिद्ध or\n'
        '  no part of the stem — **बहिरङ्गलक्षणस्य असिद्धत्वाद् अभक्तत्वाद्\n'
        '  वा**'
    ),
)

register(
    '7.4.30',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — यङि च — and before यङ्: **अरार्यते, सास्वर्यते,\n'
        '  दाध्वर्यते, सास्मर्यते**. A vārttika adds a form for हन् in the\n'
        '  sense of harming — **हन्तेर्हिंसायां यङि घ्नीभावो वक्तव्यः।\n'
        '  जेघ्नीयते** — as against जङ्घन्यते in any other'
    ),
)

register(
    '7.4.31',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — ई घ्राध्मोः — घ्रा and ध्मा become ई before यङ्:\n'
        '  **जेघ्रीयते, देध्मीयते**. Both roots end in आ and 7.4.25 would\n'
        '  have lengthened it to no purpose; the substitute is a different\n'
        '  vowel and not a longer one, which is the whole content of the rule'
    ),
)

register(
    '7.4.32',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — अस्य च्वौ — an अ-final stem becomes ई before च्वि:\n'
        '  **शुक्लीभवति, शुक्लीस्यात्; खट्वीकरोति, खट्वीस्यात्**'
    ),
)

register(
    '7.4.33',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — क्यचि च — and before क्यच्: **पुत्रीयति, घटीयति, खट्वीयति,\n'
        '  मालीयति**. **अकृत्सार्वधातुकयोर्दीर्घः इत्यस्य अपवादः** — an\n'
        '  exception to the lengthening, and stated as a sūtra of its own\n'
        '  **उत्तरार्थम्**, for the six rules that follow'
    ),
)

register(
    '7.4.34',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — अशनायोदन्यधनाया बुभुक्षापिपासागर्द्धेषु — three forms laid\n'
        '  down against three senses: **अशनायति** of HUNGER, **उदन्यति** of\n'
        '  THIRST, **धनायति** of GREED. Each has its ordinary ई-form beside\n'
        '  it in any other sense, and उदन्य changes the whole word —\n'
        '  **उदकशब्दस्य उदन्नादेशो निपात्यते**'
    ),
)

register(
    '7.4.35',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — न च्छन्दस्यपुत्रस्य — in the Veda an अ-final stem takes\n'
        '  NEITHER the lengthening nor the ई before क्यच्, पुत्र excepted:\n'
        '  **मित्रयुः, संस्वेदयुः; देवाञ् जिगाति सुम्नयुः**. **किं चोक्तम्?\n'
        '  दीर्घत्वम् ईत्वं च** — the vṛtti has to say which two rules the\n'
        '  *what is said* means'
    ),
)

register(
    '7.4.36',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति — four Vedic forms\n'
        '  laid down, each against what was due: **अवियोना दुरस्युः** where\n'
        '  दुष्टीयति was owed; **द्रविणस्युर् विपन्यया** for द्रविणीयति;\n'
        '  **वृषण्यति** for वृषीयति; **रिषण्यति** for रिष्टीयति'
    ),
)

register(
    '7.4.37',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — अश्वाघस्यात् — अश्व and अघ take आ before क्यच् in the\n'
        '  Veda: **अश्वायन्तो मघवन्; मा त्वा वृका अघायवो विदन्**. And this आ\n'
        "  is itself read as proof that 7.4.35's refusal covers the\n"
        '  lengthening — **एतद् एव आत्ववचनं ज्ञापकं न च्छन्दस्यपुत्रस्य इति\n'
        '  दीर्घप्रतिषेधो भवतीति**'
    ),
)

register(
    '7.4.38',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — देवसुम्नयोर्यजुषि काठके — and देव and सुम्न take it in the\n'
        "  Kāṭhaka's यजुस् alone: **देवायते यजमानाय; सुम्नायन्तो हवामहे**.\n"
        '  Two conditions on one form, and the vṛtti tests each'
    ),
)

register(
    '7.4.39',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — कव्यध्वरपृतनस्यर्चि लोपः — कवि, अध्वर and पृतना lose their\n'
        '  last vowel before क्यच् in a ऋच्: **कव्यन्तः सुमनसः; अध्वर्यन्तः;\n'
        '  पृतन्यन्तस् तिष्ठन्ति**'
    ),
)

register(
    '7.4.40',
    apply=before_ya,
    codification=_BEFORE_YA,
    notes=(
        'SETTLED — द्यतिस्यतिमास्थामित्ति किति — द्यति, स्यति, मा and स्था\n'
        '  take इ before a त-initial कित्: **निर्दितः, निर्दितवान्; अवसितः,\n'
        '  अवसितवान्; मितः, मितवान्; स्थितः, स्थितवान्**'
    ),
)


_BEFORE_KIT = (
    'before_kit(root, gana=..., before=..., upasarga=..., '
    'result=..., chandasi=...) -> what the stem becomes before a '
    'kit, a s and san, by rule of 7.4.41-57.'
)

register(
    '7.4.41',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — शाछोरन्यतरस्याम् — शा and छा take इ OPTIONALLY before a\n'
        '  त-initial कित्: **निशितम्, निशातम्; अवच्छितम्, अवच्छातम्**. A\n'
        '  vārttika makes it compulsory of a VOW — **श्यतेरित्त्वं व्रते\n'
        '  नित्यम्। संशितव्रतः** — and a verse settles that the two options\n'
        '  do not combine: **मिथस्ते न विभाष्यन्ते गवाक्षः संशितव्रतः**'
    ),
)

register(
    '7.4.42',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — दधातेर्हिः — धा becomes हि before a त-initial कित्:\n'
        '  **हितः, हितवान्, हित्वा**. 7.4.40 had given the आ-final roots an\n'
        '  इ; this replaces the whole root instead, and the two rules are\n'
        '  told apart by nothing but which of them names धा'
    ),
)

register(
    '7.4.43',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — जहातेश्च क्त्वि — and हा before क्त्वा: **हित्वा राज्यं\n'
        '  वनं गतः; हित्वा गच्छति**. The हा meant is जहाति and not जिहीते —\n'
        '  **जहातेर् निदेशाज् जिहीतेर् न भवति**'
    ),
)

register(
    '7.4.44',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — विभाषा छन्दसि — and in the Veda it is optional: **हित्वा\n'
        '  शरीरं यातव्यम्; हात्वा**. What the sūtra before made compulsory\n'
        '  the Veda may leave undone, and both forms then stand — the\n'
        '  ordinary shape of a छन्दसि option in this pāda'
    ),
)

register(
    '7.4.45',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — सुधितवसुधितनेमधितधिष्वधिषीय च — five Vedic forms laid\n'
        '  down: **गर्भं माता सुधितम्** where सुहितम् was due; **वसुधितमग्नौ\n'
        '  जुहोति** for वसुहितम्; **नेमधिता बाधन्ते** for नेमहिता. Each is धा\n'
        '  with the इ of 7.4.42 refused and an इट् given instead, and धिष्व\n'
        '  takes a third thing besides — no reduplication'
    ),
)

register(
    '7.4.46',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — दो दद् घोः — the घु-named दा becomes दद् before a\n'
        '  त-initial कित्: **दत्तः, दत्तवान्, दत्तिः**.\n'
        '\n'
        "SETTLED — **AND THE SUBSTITUTE'S LAST SOUND IS ARGUED FOR IN A\n"
        '  VERSE.** **अयम् आदेशस् थान्त इष्यते** — written with a त् and read\n'
        '  with a थ्, and the verse sets out what each choice would cost:\n'
        '  **तान्ते दोषो दीर्घत्वं स्याद् दान्ते दोषो निष्ठानत्वम्। धान्ते\n'
        '  दोषो धत्वप्राप्तिस् थान्तेऽदोषस् तस्मात् थान्तम्** — four\n'
        '  candidates, three producing a wrong form and the fourth chosen for\n'
        '  producing none'
    ),
)

register(
    '7.4.47',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — अच उपसर्गात्तः — but after a VOWEL-FINAL preverb it\n'
        '  becomes plain त्: **प्रत्तम्, अवत्तम्, नीत्तम्, परीत्तम्**. The\n'
        "  ablative would put the substitute at the stem's head, and the\n"
        '  vṛtti answers by reading अचः twice — **अचः इत्येतद्\n'
        '  द्विरावर्तयितव्यम्**, once for the preverb and once for what is\n'
        '  replaced'
    ),
)

register(
    '7.4.48',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — अपो भि — अप् becomes अत् before a भ्-initial ending:\n'
        '  **अद्भिः, अद्भ्यः**. A vārttika adds four more words for the Veda\n'
        '  — **स्ववःस्वतवसोर् मास उषसश्च तकारादेश इष्यते छन्दसि: स्ववद्भिः,\n'
        '  स्वतवद्भिः, माद्भिः, समुषद्भिः**'
    ),
)

register(
    '7.4.49',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — सः स्यार्द्धधातुके — a स्-final stem becomes त्-final\n'
        '  before a स्-initial ārdhadhātuka: **वत्स्यति, अवत्स्यत्, विवत्सति,\n'
        '  जिघत्सति**'
    ),
)

register(
    '7.4.50',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — तासस्त्योर्लोपः — तास् and अस् lose their स् before a\n'
        '  स्-initial affix: **कर्तासि, कर्तासे; त्वमसि, व्यतिसे**.\n'
        '\n'
        'SETTLED — **AND WHAT IS LEFT OF अस् IN व्यतिसे IS NOTHING AT ALL.**\n'
        '  **अस्तेर् अकारसकारयोर् लुप्तयोः से इति प्रत्ययमात्रम् एतत् पदम्**\n'
        "  — a word that is all affix, which is why 8.3.111's ष् does not\n"
        '  come'
    ),
)

register(
    '7.4.51',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — रि च — and before a र्-initial affix: **कर्तारौ, कर्तारः;\n'
        "  अध्येतारौ, अध्येतारः**. The र् is the one 7.1.94's अनङ् put there,\n"
        '  so this rule works on what a पाद back supplied — and only for तास्\n'
        '  and अस्, carried down from the sūtra before'
    ),
)

register(
    '7.4.52',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — ह एति — and before ए their स् becomes ह्: **कर्ताहे;\n'
        '  व्यतिहे**. A substitute where the two rules before had a loss, and\n'
        '  the ए is the first-person singular आत्मनेपद ending — one sound for\n'
        '  one sound, and the last of the three rules about तास् and अस्'
    ),
)

register(
    '7.4.53',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — यीवर्णयोर्दीधीवेव्योः — दीधी and वेवी lose their last\n'
        '  vowel before a य्-initial or इ-initial affix: **आदीध्य गतः, आवेव्य\n'
        '  गतः, आदीध्यते, आवेव्यते** for the य्; **आदीधिता, आवेविता; आदीधीत,\n'
        '  आवेवीत** for the इ'
    ),
)

register(
    '7.4.54',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        "SETTLED — सनि मीमाघुरभलभशकपतपदामच इस् — eight stems' vowel becomes\n"
        '  इस् before a स्-initial सन्: **मित्सति, प्रमित्सति; मित्सते,\n'
        '  अपमित्सते; दित्सति, धित्सति; आरिप्सते, आलिप्सते; शिक्षति; पित्सति,\n'
        '  प्रपित्सते**. Both roots of the shape मी are meant, and घु takes\n'
        '  in both दा and धा'
    ),
)

register(
    '7.4.55',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — आप्ज्ञप्यृधामीत् — आप्, ज्ञपि and ऋध् take ई instead:\n'
        '  **आपीप्सति; ज्ञीप्सति; ईर्त्सति**. ज्ञपि has two vowels, and the\n'
        '  vṛtti orders the two operations — **णेः पूर्वविप्रतिषेधेन लोपः,\n'
        '  इतरस्य तु ईत्वम्**'
    ),
)

register(
    '7.4.56',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — दम्भ इच्च — and दम्भ् takes इ, and by the च the long ई as\n'
        "  well: **धिप्सति, धीप्सति**. The च carries down 7.4.55's ईत् while\n"
        '  the sūtra states इत् of its own, so one rule gives two forms — and\n'
        '  **सि इत्येव** keeps दिदम्भिषति out, its सन् having an इट् in front'
    ),
)

register(
    '7.4.57',
    apply=before_kit,
    codification=_BEFORE_KIT,
    notes=(
        'SETTLED — मुचोऽकर्मकस्य गुणो वा — मुच् takes guṇa OPTIONALLY before\n'
        '  a स्-initial सन् where it has no object: **मोक्षते वत्सः स्वयम्\n'
        '  एव, मुमुक्षते वत्सः स्वयम् एव**. What is really made optional is\n'
        "  1.2.10's refusal of the कित् marking — **हलन्ताच् च इति\n"
        '  कित्त्वप्रतिषेधो विकल्प्यते** — and the guṇa follows from that'
    ),
)

_IN_THE_COPY = (
    'in_the_copy(root, gana=..., before=..., part=..., result=..., '
    'chandasi=...) -> what happens to the reduplicated copy, by '
    'rule of 7.4.58-97.'
)

register(
    '7.4.58',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — अत्र लोपोऽभ्यासस्य — in the environment just left behind\n'
        '  the copy goes altogether: **सनि मीमाघुरभलभशकपतपदाम् इति यावत्\n'
        '  मुचोऽकर्मकस्य इति**, which is 7.4.54–57. मित्सति, दित्सति,\n'
        '  आरिप्सते — the reduplication is made and then taken away, and what\n'
        '  is left has only the इस् those rules gave.\n'
        '\n'
        'SETTLED — **AND THE SŪTRA OPENS THE LAST HEADING OF THE ADHYĀYA.**\n'
        '  **अभ्यासस्य इत्येतच् च अधिकृतं वेदितव्यम् आ अध्यायपरिसमाप्तेः। इत\n'
        '  उत्तरं यद् वक्ष्यामः अभ्यासस्य इत्येवं तद् वेदितव्यम्** —\n'
        '  everything from 7.4.59 to 7.4.97 is about the copy, and none of\n'
        '  the forty sūtras has to say so again. The Kāśikā proves the\n'
        '  heading on the very next rule: 7.4.59 ह्रस्वः is one word, and it\n'
        '  is the copy that shortens — डुढौकिषते, तुत्रौकिषते.\n'
        '\n'
        'SETTLED — **AND अत्र IS IN THE SŪTRA TO FENCE THE LOSS IN.** The\n'
        '  loss could have been packed into 7.4.54 itself — **इत्येवं सिद्धे\n'
        '  यद् अत्रग्रहणम् इह क्रियते, तद् विषयावधारणार्थम्** — and it is\n'
        '  stated separately so that HERE and nowhere later is where the copy\n'
        '  goes. Without it the heading would carry the loss down with it'
    ),
)

register(
    '7.4.61',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — शर्पूर्वाः खयः — of the copy the खय् that a शर् stands\n'
        '  before are what remain, and the other consonants go: **शर्पूर्वाः\n'
        '  खयः शिष्यन्ते, अन्ये हलो लुप्यन्ते**. श्च्युत् gives\n'
        '  **चुश्च्योतिषति**, स्था **तिष्ठासति**, स्पन्द् **पिस्पन्दिषते** —\n'
        '  in each the copy keeps its SECOND consonant and drops the first,\n'
        '  which is exactly what 7.4.60 would not have done.\n'
        '\n'
        'SETTLED — **AND A VĀRTTIKA WIDENS शर् TO खर्.** **खर्पूर्वाः खय इति\n'
        '  वक्तव्यम्** — for उचिच्छिषति, where उच्छ् takes its तुक् first,\n'
        '  being अन्तरङ्ग, and the copy is then त्छ्; त् is a खर् and not a\n'
        '  शर्, so without the vārttika 7.4.60 would keep the त् and the form\n'
        '  would be heard with one'
    ),
)

register(
    '7.4.62',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — कुहोश्चुः — a guttural or ह् in the copy becomes the\n'
        '  answering palatal: **चकार, चखान, जगाम, जघान**, and for ह् **जहार,\n'
        '  जिहीर्षति, जहौ**. This is why a reduplicated perfect almost never\n'
        '  begins with the sound its root begins with, and why the copy of\n'
        '  गम् is ज and not ग'
    ),
)

register(
    '7.4.63',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — न कवतेर्यङि — but NOT of कव् before यङ्: **कोकूयते\n'
        '  उष्ट्रः, कोकूयते स्वरः**, where 7.4.62 would have given *चोकूयते.\n'
        '  The root is named by its conjugated shape — **कवतेः इति\n'
        '  विकरणनिर्देशः कौतेः कुवतेश्च निवृत्त्यर्थः** — so that कौति and\n'
        '  कुवति, which look the same in the root list, are left out and keep\n'
        '  their palatal: **चोकूयते**'
    ),
)

register(
    '7.4.64',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — कृषेश्छन्दसि — and not of कृष् before यङ् IN THE VEDA:\n'
        '  **करिकृष्यते यज्ञकुणपः**. The pair is the cleanest test of a\n'
        '  छन्दसि refusal anywhere in the pāda — करिकृष्यते in the Veda\n'
        '  against चरीकृष्यते in the spoken language, one and the same root,\n'
        '  one and the same affix, and only the register telling them apart'
    ),
)

register(
    '7.4.65',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — दाधर्तिदर्धर्ति…आगनीगन्तीति च — eighteen Vedic forms laid\n'
        '  down whole: **दाधर्ति, दर्धर्ति, दर्धर्षि, बोभूतु, तेतिक्ते,\n'
        '  अलर्षि, आपनीफणत्, संसनिष्यदत्, करिक्रत्, कनिक्रदत्, भरिभ्रत्,\n'
        '  दविध्वतः, दविद्युतत्, तरित्रतः, सरीसृपतम्, वरीवृजत्, मर्मृज्य,\n'
        '  आगनीगन्ति**.\n'
        '\n'
        'SETTLED — **EACH IS TAKEN APART IN THE VṚTTI, AND THE FIRST THREE\n'
        '  SHOW THE METHOD.** **दाधर्ति दर्धर्ति दर्धर्षि इति धारयतेः, धृङो\n'
        '  वा श्लौ यङ्लुकि वा अभ्यासस्य दीर्घत्वं णिलोपश्च** — from धारि or\n'
        '  from धृङ्, in the श्लु or in the यङ्लुक्, with the copy lengthened\n'
        '  and the णि lost. Three derivations are offered and none is chosen,\n'
        '  because a निपातन does not need one: the form is given, and the\n'
        '  grammar is only asked to make room for it'
    ),
)

register(
    '7.4.67',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — द्युतिस्वाप्योः सम्प्रसारणम् — the copy of द्युत् and of\n'
        '  स्वापि takes saṃprasāraṇa: **विदिद्युते, व्यदिद्युतत्,\n'
        '  विदिद्योतिषते, विदेद्युत्यते**; and **सुष्वापयिषति**. The स्वापि\n'
        '  meant is the causal — **स्वापिः ण्यन्तो गृह्यते** — and the vṛtti\n'
        '  adds a condition the sūtra does not state: **तस्य अभ्यासनिमित्तेन\n'
        '  प्रत्ययेन आनन्तर्ये सति सम्प्रसारणम् इष्यते**, the affix that\n'
        '  caused the reduplication must stand next to the stem'
    ),
)

register(
    '7.4.68',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — व्यथो लिटि — and the copy of व्यथ् in the perfect:\n'
        '  **विव्यथे, विव्यथाते, विव्यथिरे**. The rule is stated for what it\n'
        '  saves: 7.4.60 was about to drop the य् as a later consonant —\n'
        '  **हलादिः शेषेण यकारस्य निवृत्तौ प्राप्तायां सम्प्रसारणं क्रियते**\n'
        '  — and the saṃprasāraṇa turns it into इ instead. The व् is not\n'
        '  touched, because 6.1.37 refuses a saṃprasāraṇa inside a\n'
        '  saṃprasāraṇa'
    ),
)

register(
    '7.4.69',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — दीर्घ इणः किति — the copy of इण् lengthens before a कित्\n'
        '  perfect: **ईयतुः, ईयुः**. The derivation runs backwards through\n'
        '  6.4.81: **इणो यण् इति यणादेशे कृते स्थानिवद्भावाद् द्विर्वचनम्** —\n'
        '  इ becomes य्, the substitute stands for what it replaced, and so\n'
        '  there is a vowel there to copy at all. Without स्थानिवद्भाव इ +\n'
        '  अतुस् would have no syllable to reduplicate'
    ),
)

register(
    '7.4.70',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — अत आदेः — an अ at the START of the copy lengthens in the\n'
        '  perfect: **आट, आटतुः, आटुः**. It is stated against a rule that\n'
        '  would otherwise have merged the two vowels — **अतो गुणे\n'
        '  पररूपत्वस्य अपवादः** — for अट् + अ + अट् would give अटतुः by\n'
        '  6.1.97 and the copy would vanish into the root. Length keeps it\n'
        '  visible, and every ordinary परस्मैपद perfect of an अ-initial root\n'
        '  shows it'
    ),
)

register(
    '7.4.71',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — तस्मान्नुड् द्विहलः — after that lengthened अ, a stem of\n'
        '  TWO consonants takes नुट्: **आनङ्ग, आनङ्गतुः, आनङ्गुः; आनञ्ज,\n'
        '  आनञ्जतुः, आनञ्जुः**. The rule reaches not the copy but what stands\n'
        '  after it, which is why it is the one sūtra of the heading that has\n'
        '  to name its own target. And ऋ counts as carrying a consonant —\n'
        '  **ऋकारैकदेशो रेफो हल्ग्रहणेन गृह्यते** — so ऋध् too: **आनृधतुः,\n'
        '  आनृधुः**'
    ),
)

register(
    '7.4.72',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — अश्नोतेश्च — and अश्नोति takes it too: **व्यानशे,\n'
        '  व्यानशाते, व्यानशिरे**. The root is named by its fifth-class shape\n'
        '  on purpose — **अश्नोतेः इति विकरणनिर्देशः अश्नातेर् मा भूत् इति**\n'
        "  — so that the ninth-class अश् 'eat' is not reached, and it keeps\n"
        '  the plain आश'
    ),
)

register(
    '7.4.73',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — भवतेरः — the copy of भू becomes अ in the perfect: **बभूव,\n'
        '  बभूवतुः, बभूवुः**. Without it the copy would be बु and the\n'
        '  commonest perfect in the language would read *बुभूव. The root is\n'
        '  again named by its conjugated shape — **भवतेः इति\n'
        '  कृतविकरणनिर्देशाद्** — which the vṛtti uses to keep out **अनुबभूवे\n'
        '  कम्बलो देवदत्तेन**, where the sense is not the ordinary one'
    ),
)

register(
    '7.4.74',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — ससूवेति निगमे — **ससूव** is laid down for the Veda: **ससूव\n'
        '  स्थविरं विपश्चिताम्**. Three things are given at once and none of\n'
        '  them would come otherwise — **सूतेर् लिटि परस्मैपदं वुगागमः\n'
        '  अभ्यासस्य च अत्वं निपात्यते**: a root that takes आत्मनेपद is given\n'
        '  a परस्मैपद ending, a वुक् is put in, and the copy becomes अ. The\n'
        '  spoken language keeps सुषुवे, and the two forms sit side by side\n'
        '  in the vṛtti as the measure of what a निपातन costs'
    ),
)

register(
    '7.4.75',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — निजां त्रयाणां गुणः श्लौ — the copy of णिज्, विज् and\n'
        '  विष्लृ takes guṇa when श्लु follows: **नेनेक्ति, वेवेक्ति,\n'
        '  वेवेष्टि**. **त्रिग्रहणम् उत्तरार्थम्** — saying THREE is not\n'
        '  needed here, since the root list marks just these three, and it is\n'
        '  said for the next sūtra, which borrows the word and needs it'
    ),
)

register(
    '7.4.76',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — भृञामित् — the copy of भृञ्, माङ् and ओहाङ् becomes इ when\n'
        '  श्लु follows: **बिभर्ति, मिमीते, जिहीते**. The THREE carried down\n'
        '  from the sūtra before is doing real work: भृञ् is first in the\n'
        '  root list and भृञादि could have been read as a whole class, and\n'
        '  the count stops it at three — which is how **जहाति** keeps its अ'
    ),
)

register(
    '7.4.77',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — अर्तिपिपर्त्योश्च — and the copy of ऋ and of पॄ: **इयर्ति\n'
        '  भूमम्; पिपर्ति सोमम्**. The two are named by their finished\n'
        '  third-person forms, अर्ति and पिपर्ति, and not by their root\n'
        '  shapes — the same device 7.4.63, 7.4.72 and 7.4.73 use, and here\n'
        '  it settles which of the several roots written ऋ and पॄ is meant'
    ),
)

register(
    '7.4.78',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — बहुलं छन्दसि — and in the Veda the इ comes VARIOUSLY\n'
        '  before श्लु, on roots no other rule names: **पूर्णां विवष्टि**\n'
        '  from वश्, **जनिमा विवक्ति** from वच्, **वत्सं न माता सिषक्ति**\n'
        '  from सच्, **जघर्ति सोमम्**. And बहुलम् cuts the other way too —\n'
        '  **न च भवति। ददाति इत्येवं ब्रूयात्। जजनदिन्द्रम्** — so that the\n'
        '  Veda both extends the rule past its list and declines it where the\n'
        '  list would have given it'
    ),
)

register(
    '7.4.79',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — सन्यतः — before सन् a SHORT-अ-final copy becomes इ:\n'
        '  **पिपक्षति, यियक्षति, तिष्ठासति, पिपासति**. This is the rule the\n'
        '  whole desiderative is heard by, and the तपर in अतः is what keeps\n'
        "  पापचिषते — the यङ् stem's long-आ copy — out of its reach"
    ),
)

register(
    '7.4.80',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — ओः पुयण्ज्यपरे — and a उ-final copy becomes इ before सन्\n'
        '  when what follows is a प-वर्ग sound, a यण् or ज् with अ-वर्ण after\n'
        '  it: **पिपविषते, पिपावयिषति, बिभावयिषति** for the first,\n'
        '  **यियविषति, यियावयिषति, रिरावयिषति, लिलावयिषति** for the second,\n'
        '  and **जिजावयिषति** for the third, from the root जु the sūtras\n'
        '  alone attest.\n'
        '\n'
        'SETTLED — **AND THE SŪTRA IS READ AS PROOF OF SOMETHING ELSE.**\n'
        '  **एतदेव पुयण्ज्यपरे इति वचनं ज्ञापकम्** — the three conditions\n'
        '  would be idle unless the reduplication were already in place when\n'
        '  this rule ran, so the order of the two is settled by the sūtra\n'
        '  having anything to say at all'
    ),
)

register(
    '7.4.81',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — स्रवतिशृणोतिद्रवतिप्रवतिप्लवतिच्यवतीनां वा — but for these\n'
        '  six the इ comes only OPTIONALLY: **सिस्रावयिषति, सुस्रावयिषति;\n'
        '  शिश्रावयिषति, शुश्रावयिषति; दिद्रावयिषति, दुद्रावयिषति;\n'
        '  पिप्रावयिषति, पुप्रावयिषति; पिप्लावयिषति, पुप्लावयिषति;\n'
        '  चिच्यावयिषति, चुच्यावयिषति**. All six are named by their\n'
        "  conjugated forms and all six fall under 7.4.80's यण् with अ after\n"
        "  it, so the sūtra is a विभाषा of exactly one of that rule's three\n"
        '  cases'
    ),
)

register(
    '7.4.84',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम् — the copy of\n'
        '  these eight takes नीक् before यङ् and before the यङ्लुक्:\n'
        '  **वनीवच्यते, वनीवञ्चीति; सनीस्रस्यते, सनीस्रंसीति; दनीध्वस्यते,\n'
        '  दनीध्वंसीति; बनीभ्रस्यते, बनीभ्रंसीति; चनीकस्यते, चनीकसीति;\n'
        '  पनीपत्यते, पनीपतीति; पनीपद्यते, पनीपदीति; चनीस्कद्यते**. Each pair\n'
        '  is the same stem twice over, once with the यङ् heard and once with\n'
        '  it dropped, and the augment is indifferent to which'
    ),
)

register(
    '7.4.85',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — नुगतोऽनुनासिकान्तस्य — the अ-final copy of a nasal-final\n'
        '  stem takes नुक् before यङ् and the यङ्लुक्: **तन्तन्यते, तन्तनीति;\n'
        '  जङ्गम्यते, जङ्गमीति; यंयम्यते, यंयमीति; रंरम्यते, रंरमीति**.\n'
        '\n'
        'SETTLED — **AND THE नुक् IS WRITTEN FOR AN ANUSVĀRA.** **नुक्\n'
        '  इत्येतद् अनुस्वारोपलक्षणार्थं द्रष्टव्यम्। स्थानिना हि आदेशो\n'
        '  लक्ष्यते** — the न् is named because the anusvāra that actually\n'
        '  appears is its substitute, which is why **यंयम्यते** shows one\n'
        '  even where no झल् follows and 8.3.23 would not have given it'
    ),
)

register(
    '7.4.86',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — जपजभदहदशभञ्जपशां च — and the copy of these six:\n'
        '  **जञ्जप्यते, जञ्जपीति; जञ्जभ्यते; दन्दह्यते, दन्दहीति; दन्दश्यते,\n'
        '  दन्दशीति; बम्भज्यते, बम्भञ्जीति; पम्पश्यते**. Two of the six are\n'
        '  written short on purpose: दश is the root दंश् — **दश इति दंशिः अयं\n'
        '  नकारलोपार्थम् एव निर्दिष्टः। तेन यङ्लुक्यपि नकारलोपो भवति** — and\n'
        '  पश is a root the sūtras alone attest, **पश इति सौत्रो धातुः**,\n'
        '  which is why it is written with no marker at all'
    ),
)

register(
    '7.4.87',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — चरफलोश्च — and the copy of चर् and फल्: **चञ्चूर्यते,\n'
        '  चञ्चूरीति; पम्फुल्यते, पम्फुलीति**. The two are taken out of the\n'
        '  list before them because the next sūtra needs them by themselves —\n'
        '  they alone go on to change the vowel that follows the copy as well\n'
        '  as the copy itself'
    ),
)

register(
    '7.4.88',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — उत् परस्यातः — and the अ that stands AFTER the copy of चर्\n'
        '  and फल् becomes उ: **चञ्चूर्यते, चञ्चूरीति; पम्फुल्यते,\n'
        '  पम्फुलीति**. Both words in the sūtra are tested — **परस्य इति\n'
        '  किम्? अभ्यासस्य मा भूत्। अतः इति किम्? अलोऽन्त्यस्य मा भूत्** —\n'
        '  and the तपर is there for a third reason: **चञ्चूर्ति, पम्फुलीति\n'
        '  इत्यत्र लघूपधगुणनिवृत्त्यर्थम्**, to keep the light-penult guṇa\n'
        '  off'
    ),
)

register(
    '7.4.89',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — ति च — and the same उ before a त-initial affix: **चरणं\n'
        '  चूर्तिः; ब्रह्मणश् चूर्तिः; प्रफुल्तिः; प्रफुल्ताः सुमनसः**. Here\n'
        '  the heading itself is set aside — **यङ्यङ्लुकोः, अभ्यासस्य इति च\n'
        '  अनुवर्तमानम् अपि वचनसामर्थ्याद् इह न अभिसम्बध्यते** — for there is\n'
        '  no reduplication in चूर्तिः at all, and a sūtra that could not\n'
        '  apply under its own heading is read without it'
    ),
)

register(
    '7.4.92',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        "SETTLED — ऋतश्च — an ऋ-FINAL stem's copy takes रुक्, रिक् or रीक् in\n"
        '  the यङ्लुक् too: **चर्कर्ति, चरिकर्ति, चरीकर्ति; जर्हर्ति,\n'
        '  जरिहर्ति, जरीहर्ति**. 7.4.90 and 7.4.91 had given the three to a\n'
        '  stem with ऋ in the PENULT; this adds the stem that ends in one,\n'
        '  and the तपर keeps किर् out — **किरतेश् चाकर्ति**. The vṛtti quotes\n'
        '  a verse about how hard the whole चर्करीत class is to place:\n'
        '  **किरतिं चर्करीतान्तं पचति इत्यत्र यो नयेत्, प्राप्तिज्ञं तम् अहं\n'
        '  मन्ये**'
    ),
)

register(
    '7.4.93',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — सन्वल्लघुनि चङ्परेऽनग्लोपे — where a light root-syllable\n'
        '  follows, and the णि has चङ् after it, and no vowel has been lost,\n'
        '  the copy does whatever it would do BEFORE सन्. Three rules are\n'
        '  borrowed at once and the vṛtti names them: 7.4.79 सन्यतः gives\n'
        '  **अचीकरत्, अपीपचत्**; 7.4.80 ओः पुयण्ज्यपरे gives **अपीपवत्,\n'
        "  अलीलवत्, अजीजवत्**; and 7.4.81's option carries over as well. This\n"
        '  is the sūtra the causal aorist turns on — every अचीकरत्-shaped\n'
        '  form in the language is made by it together with the one after'
    ),
)

register(
    '7.4.94',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — दीर्घो लघोः — and a LIGHT copy then lengthens, under the\n'
        '  same four conditions: **अचीकरत्, अजीहरत्, अलीलवत्, अपीपचत्**. The\n'
        "  ई of every one of those is made twice over — इ by 7.4.93's\n"
        '  borrowed सन्यतः and long by this — and the vṛtti tests each\n'
        '  condition by taking it away, which is the cleanest set of\n'
        '  counter-examples in the pāda'
    ),
)

register(
    '7.4.95',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — अत् स्मृदृत्वरप्रथम्रदस्तॄस्पशाम् — but the copy of these\n'
        '  seven becomes a SHORT अ instead: **असस्मरत्, अददरत्, अतत्वरत्,\n'
        '  अपप्रथत्, अमम्रदत्, अतस्तरत्, अपस्पशत्**. It displaces both rules\n'
        '  before it, and the vṛtti says so of each in turn: **सन्वद्भावाद्\n'
        '  इत्त्वं प्राप्तम् अनेन बाध्यते**, and **तपरकरणसामर्थ्याद् अति कृते\n'
        '  दीर्घो लघोः इत्येतद् अपि न भवति** — the तपर would be idle if the\n'
        '  length could come afterwards, so it cannot: **अददरत्**'
    ),
)

register(
    '7.4.96',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — विभाषा वेष्टिचेष्ट्योः — and for वेष्ट् and चेष्ट् the अ\n'
        '  comes only OPTIONALLY: **अववेष्टत्, अविवेष्टत्; अचचेष्टत्,\n'
        '  अचिचेष्टत्**. The second of each pair is what 7.4.93 gives on its\n'
        '  own. The vṛtti notes the order — **अभ्यासह्रस्वत्वे कृते अत्त्वं\n'
        '  पक्षे भवति** — the copy is shortened first and the अ then replaces\n'
        '  what is there'
    ),
)

register(
    '7.4.97',
    apply=in_the_copy,
    codification=_IN_THE_COPY,
    notes=(
        'SETTLED — ई च गणः — and the copy of गण् becomes ई: **अजीगणत्**, with\n'
        "  the च carrying 7.4.95's अत् down so that **अजगणत्** stands beside\n"
        '  it. With this the अभ्यासस्य heading closes and so does the adhyāya\n'
        '  — **इति श्रीवामनविरचितायां काशिकायां वृत्तौ सप्तमाध्यायस्य चतुर्थः\n'
        '  पादः**'
    ),
)


#: Every one of these is addressed to the अभ्यास and to nothing else, so
#: they are one resolver over one term. Each sūtra's own worked root is in
#: cases.py; the record of which of them fired is on the returned Doubled.
_ABHYASA = {
    "7.4.59": (
        ("1.1.9", "1.1.48", "1.1.50", "1.2.27"),
        'SETTLED — ह्रस्वो भवति अभ्यासस्य: the copy carries a short vowel\n'
        '  whatever the root had. दुढौकिषते, तुत्रौकिषते.\n'
        '\n'
        'SETTLED — which vowel counts as the short one is not this rule to\n'
        '  say, and it is not tabulated here. `hrasva_of` asks 1.1.48 for\n'
        '  the diphthongs, and for the rest takes the savarṇa (1.1.9) that\n'
        '  measures one mātrā (1.2.27), with 1.1.50 breaking the tie ṝ\n'
        '  leaves between ṛ and ḷ. 1.2.47 needed the same answer and had\n'
        '  been carrying a nine-row table for it; the table is gone.\n'
        '\n'
        'SCOPE — the vārttika अभ्यासस्य अनचि, which gives चराचरः and\n'
        '  चलाचलः and suspends 7.4.60 along with it, is not modelled.'
    ),
    "7.4.60": (
        (),
        'SETTLED — अभ्यासस्य हलादिः शिष्यते, अनादिर्लुप्यते: of the copy the\n'
        '  initial consonant stays and every later one goes. पपाच, पपाठ,\n'
        '  जग्लौ, मम्लौ, आट.\n'
        '\n'
        'SETTLED — the rule is what makes the copy shorter than the root,\n'
        '  and it only has work to do where the first syllable is closed.\n'
        '  मृज् gives मृ; लू gives लू and nothing happens. A wrong split of\n'
        '  the stem is therefore invisible on लू and shows on मृज्.\n'
        '\n'
        'OPEN — the Kāśikā records two readings of शेष, one taking the\n'
        '  remaining as what is prescribed and one taking the dropping as\n'
        '  what is prescribed — आदिशेषनिमित्तोऽयम् against अपरे तु ब्रुवते.\n'
        '  Nothing in this codification turns on which, so neither is taken.'
    ),
    "7.4.66": (
        ("1.1.9",),
        'SETTLED — ऋवर्णान्तस्य अभ्यासस्य अकारादेशः: ववृते, ववृधे, शशृधे.\n'
        '  The अ is plain — there is no र् in any of those three.\n'
        '\n'
        'SETTLED — and the Kāśikā states the ORDER, which is the one thing\n'
        '  here that cannot be read off the finished forms: उः अदत्वे कृते\n'
        '  रुगादय आगमाः क्रियन्ते, once अ has replaced the ऋ, then the\n'
        '  augments are made. Its own नर्नर्ति · नरिनर्ति · नरीनर्ति is the\n'
        '  proof — one copy न, three augments रुक् रिक् रीक्.\n'
        '\n'
        'SCAR — read the other way, 1.1.51 उरण् रपरः turns the अ into अर्\n'
        '  and मृ becomes मर्, and then a second application of 7.4.60 is\n'
        '  needed to take the र् off again. Two invented steps that cancel,\n'
        '  arriving at the right answer by the wrong road. ववृते settles\n'
        '  it: रपर there would give वर्वृते.'
    ),
    "7.4.82": (
        (),
        'SETTLED — यङि यङ्लुकि च इगन्तस्य अभ्यासस्य गुणः: चेचीयते,\n'
        '  लोलूयते, जोहवीति. लु becomes लो, which is how लोलूय gets its ओ.\n'
        '\n'
        'SETTLED — it runs before 7.4.83 and not after. Both reach an\n'
        '  इक्-final copy; गुण is the narrower and takes it, and once the\n'
        '  vowel is ओ the lengthening has nothing left to do. Run दीर्घ\n'
        '  first and the stem is *लूलूय.'
    ),
    "7.4.83": (
        (),
        'SETTLED — दीर्घोऽकितः, in the यङ् and the यङ्लुक् both: पापच्यते,\n'
        '  यायज्यते.\n'
        '\n'
        'SETTLED — अकितः इति किम्? यंयम्यते, रंरम्यते, where a कित् augment\n'
        '  has come into the copy. Taken as a parameter: whether an augment\n'
        '  is कित् is a fact about the augment, and the ones that would\n'
        '  supply it here are not codified.\n'
        '\n'
        'SETTLED — the Kāśikā draws a paribhāṣā out of the word अकितः:\n'
        '  अभ्यासविकारेष्वपवादा न उत्सर्गान् विधीन् बाधन्ते, in the copy an\n'
        '  exception does not shut the general rules out. That is the same\n'
        '  principle 7.4.66 uses to put the augments after उरत्.\n'
        '\n'
        'OPEN — why it does not also lengthen the अ that 7.4.66 leaves, so\n'
        '  that मरीमृज्य is not *मारीमृज्य. The reading taken here is that\n'
        '  the augment comes first, on 7.4.66\'s own अदत्वे कृते; whether\n'
        '  the rule is instead blocked outright is not settled from what is\n'
        '  on disk.'
    ),
    "7.4.90": (
        (),
        'SETTLED — ऋदुपधस्य अङ्गस्य योऽभ्यासः, तस्य रीगागमो भवति\n'
        '  यङ्यङ्लुकोः परतः: वरीवृत्यते, वरीवृध्यते, नरीनृत्यते.\n'
        '\n'
        'SETTLED — रीक् is कित्, so 1.1.46 आद्यन्तौ टकितौ puts it at the END\n'
        '  of the copy. म plus री is मरी, which is how मरीमृज्य is built.\n'
        '\n'
        'SETTLED — the vārttika widens it: रीगृत्वत इति वक्तव्यम्, for a\n'
        '  root merely CONTAINING ऋ rather than having it for its penult,\n'
        '  so वरीवृश्च्यते and परीपृच्छ्यते are reached. That wider reading\n'
        '  is the one codified, since it is what the Kāśikā asks for.'
    ),
    "7.4.91": (
        (),
        'SETTLED — रुक् and रिक् for the same copy, and रीक् too by the च:\n'
        '  नर्नर्ति, नरिनर्ति, नरीनर्ति; वर्वर्ति, वरिवर्ति, वरीवर्ति. The\n'
        '  उ of रुक् is उच्चारणार्थ, so the augment is a bare र्.\n'
        '\n'
        'SETTLED — लुकि. These two belong to the यङ्लुक् and 7.4.90\'s रीक्\n'
        '  to both, so asking for रुक् in the यङ् proper is refused rather\n'
        '  than quietly allowed: it would give *मर्मृज्य where the rule\n'
        '  offers only मरीमृज्य.\n'
        '\n'
        'SETTLED — मर्मृज्यमानास इत्युपसंख्यानम्, and so मर्मृज्यते: रुक् is\n'
        '  admitted to one यङन्त form by name. Recorded, not modelled — an\n'
        '  उपसंख्यान for a single form is not a rule this resolver can\n'
        '  carry without inviting *वर्वृत्यते beside it.'
    ),
}

for _sutra, (_reuses, _notes) in _ABHYASA.items():
    register(
        _sutra,
        apply=for_sutra(_sutra),
        codification=_CODIFICATION,
        notes=_notes,
        reuses=_reuses,
    )


__all__ = [
    'before_cang',
    'before_kit',
    'before_ya',
    'for_sutra',
    'in_the_copy',
    'to_the_stem',
]
