# -*- coding: utf-8 -*-
"""अध्याय ८, पाद ४ — a झल् hardening before a खर्."""

from __future__ import annotations

from src.astadhyayi.anga import khari_ca
from src.astadhyayi.natva import the_cerebral_n
from src.astadhyayi.stutva import at_the_junction
from src.astadhyayi.sources import register


register(
    '8.4.55',
    apply=khari_ca,
    reuses=('1.1.71',),
    codification=(
        'khari_ca(sound, following) -> the सپर्श replaced by its चर्.'
    ),
    related=('1.1.71', '8.2.1'),
    notes=(
        'SETTLED — खरि च परतो झलां चरादेशो भवति: भेत्ता, भेत्तुम्,\n'
        '  भेत्तव्यम्, युयुत्सते. And अत्ति, which is why the engine wanted\n'
        '  it: अद् + ति has a voiced द् meeting a voiceless त्.\n'
        '\n'
        'NOTE — which sound replaces which is not tabulated here. चर् is\n'
        '  the first member of each varga, and varna.VARGA already holds\n'
        '  the vargas in the alphabet\'s own order, so the substitute is\n'
        '  read off the row the sound stands in. A table mapping द् to त्,\n'
        '  ध् to त्, ब् to प् would be that same fact written twice.\n'
        '\n'
        'NOTE — it stands in the tripādī, so what it does is असिद्ध to\n'
        '  everything before 8.2.1.'
    ),
)


_THE_CEREBRAL_N = (
    'the_cerebral_n(root, gana=..., after=..., before=..., '
    'sense=..., chandasi=...) -> the n that becomes cerebral and '
    'where it does not, by rule of 8.4.1-39.'
)

register(
    '8.4.1',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — रषाभ्यां नो णः समानपदे — a न् after a र् or a ष् becomes\n'
        '  ण्, provided the two stand in the SAME WORD: **आस्तीर्णम्,\n'
        '  विशीर्णम्, अवगूर्णम्** after the र्, and **कुष्णाति, पुष्णाति,\n'
        '  मुष्णाति** after the ष्. **षग्रहणम् उत्तरार्थम्** — the ष् is\n'
        "  named for the sūtras that follow, since 8.4.41's ष्टुत्व would\n"
        '  have given the cerebral here anyway. This is the rule the whole\n'
        '  pāda opens on and the last seven sūtras of the run take back'
    ),
)

register(
    '8.4.2',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — अट्कुप्वाङ्नुम्व्यवायेऽपि — and it reaches ACROSS five\n'
        '  things: a vowel, a guttural, a labial, आङ् and a नुम्. Across the\n'
        '  vowel — **करणम्, हरणम्, किरिणा, गिरिणा, कुरुणा, गुरुणा**; across\n'
        '  the guttural — **अर्केण, मूर्खेण, गर्गेण, अर्घेण**. Without it\n'
        '  करणम् would have a plain न्, the र् and the न् being two sounds\n'
        '  apart, and so would half the instrumentals in the language'
    ),
)

register(
    '8.4.3',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — पूर्वपदात् संज्ञायामगः — and across a COMPOUND SEAM where\n'
        '  a NAME is being made, unless a ग stands between: **द्रुणसः,\n'
        "  वार्ध्रीणसः, खरणसः, शूर्पणखा**. 8.4.1's समानपदे would have stopped\n"
        '  it at the seam, so the rule is what lets a compound count as one\n'
        '  word for this purpose — and only for a name. **केचिद् एतद्\n'
        '  नियमार्थं वर्णयन्ति**, some read it as a restriction instead'
    ),
)

register(
    '8.4.4',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः — and the न्\n'
        '  of वन after six named first members, in a name: **पुरगावणम्,\n'
        '  मिश्रकावणम्, सिध्रकावणम्, शारिकावणम्, कोटरावणम्, अग्रेवणम्**. The\n'
        '  condition of the sūtra before is carried down — **पूर्वपदात्\n'
        '  संज्ञायाम् इति वर्तते** — and what is new is only the list and the\n'
        '  one word it acts on'
    ),
)

register(
    '8.4.5',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED —\n'
        '  प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपियूक्षाभ्योऽसंज्ञायामपि —\n'
        '  and after ten more, whether a name is being made or not: **प्रवणे\n'
        '  यष्टव्यम्; निर्वणे प्रतिधीयते; अन्तर्वणे; शरवणम्; इक्षुवणम्;\n'
        '  प्लक्षवणम्; आम्रवणम्**. The असंज्ञायाम् अपि is what takes the\n'
        "  sūtra out of 8.4.3's condition, and it is the only place in the\n"
        '  run where the name is not wanted'
    ),
)

register(
    '8.4.6',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — विभाषौषधिवनस्पतिभ्यः — and after a word for a HERB or a\n'
        '  TREE, optionally: **दूर्वावणम्, दूर्वावनम्; मूर्वावणम्; शिरीषवणम्,\n'
        '  शिरीषवनम्**. Three sūtras in a row on one word, each with its own\n'
        '  list, and this the only one of the three that leaves a choice'
    ),
)

register(
    '8.4.7',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — अह्नोऽदन्तात् — the न् of अह्न after an अ-final first\n'
        "  member: **पूर्वाह्णः, अपराह्णः**. The word itself is 5.4.88's\n"
        '  substitute for अहन्, and the अदन्तात् is what keeps निरह्नः and\n'
        '  दुरह्नः out — which is why the two halves of a day have a cerebral\n'
        '  and a day counted from something has not'
    ),
)

register(
    '8.4.8',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — वाहनमाहितात् — and the न् of वाहन after a word for WHAT IS\n'
        '  LOADED on it: **इक्षुवाहणम्, शरवाहणम्, दर्भवाहणम्**. **वाहने यद्\n'
        '  आरोपितम् उह्यते तद् आहितम् उच्यते**. A cart carrying sugar-cane\n'
        '  takes the cerebral and a cart belonging to someone does not, which\n'
        '  is a distinction of relation and not of form'
    ),
)

register(
    '8.4.9',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — पानं देशे — and the न् of पान where a COUNTRY is named:\n'
        '  **क्षीरं पानं येषां ते क्षीरपाणा उशीनराः** — the Uśīnaras, whose\n'
        "  drink is milk. **पीयत इति पानम्**, by 3.3.113's कृत्यल्युटो बहुलम्\n"
        '  in the sense of the object. And the vṛtti notes it is seen of\n'
        '  PEOPLE as well as of places'
    ),
)

register(
    '8.4.10',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — वा भावकरणयोः — and where पान names the ACT or the\n'
        '  INSTRUMENT, optionally: **क्षीरपाणं वर्तते, क्षीरपानम्; सुरापाणम्,\n'
        '  सुरापानम्; क्षीरपाणः कंसः, क्षीरपानः**. One word, three senses,\n'
        '  three sūtras — the country compulsorily, the act and the vessel by\n'
        '  choice'
    ),
)

register(
    '8.4.11',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — प्रातिपदिकान्तनुम्विभक्तिषु च — and a न् that ends a STEM,\n'
        '  or belongs to a नुम्, or belongs to an ENDING, takes it\n'
        "  optionally: **माषवापिणौ, माषवापिनौ** at a stem's end; **माषवापाणि,\n"
        '  माषवापानि** in a नुम्; and in an ending likewise. Three quite\n'
        '  different places for the same sound, and one option over all of\n'
        '  them'
    ),
)

register(
    '8.4.12',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — एकाजुत्तरपदे णः — but where the SECOND MEMBER has only one\n'
        '  vowel it is compulsory: **वृत्रहणौ, वृत्रहणः; क्षीरपाणि;\n'
        '  सुरापाणि**. What was a choice one sūtra back is fixed here, and\n'
        '  the condition is as mechanical as any in the work — count the\n'
        '  vowels of the second member'
    ),
)

register(
    '8.4.13',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — कुमति च — and where the second member HAS A GUTTURAL in\n'
        '  it: **वस्त्रयुगिणौ, वस्त्रयुगिणः; स्वर्गकामिणौ; वृषगामिणौ;\n'
        '  वस्त्रयुगाणि**. The guttural is what 8.4.2 had already said the\n'
        '  cerebral reaches across, so the two rules read each other: one\n'
        '  lets it cross a guttural inside a word and this makes it\n'
        '  compulsory across a seam'
    ),
)

register(
    '8.4.14',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — उपसर्गादसमासेऽपि णोपदेशस्य — the न् of a root TAUGHT WITH\n'
        '  A ण् becomes ण् after a preverb, **असमासेऽपि समासेऽपि** —\n'
        '  compounded or not: **प्रणमति, परिणमति; प्रणायकः, परिणायकः**. **ण\n'
        '  उपदेशे यस्य असौ णोपदेशः** — नम् is written णम् in the root list,\n'
        '  and this is what that spelling is for. Every प्रणाम and परिणाम in\n'
        '  the language comes from here'
    ),
)

register(
    '8.4.15',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — हिनुमीना — and the न् of हिनु and मीना: **प्रहिणोति,\n'
        '  प्रहिणुतः; प्रमीणाति, प्रमीणीतः**. The two are named in their\n'
        '  conjugated shapes and the rule still reaches them where those\n'
        '  shapes have been altered — **विकृतस्य अपि भवति, अजादेशस्य\n'
        '  स्थानिवत्त्वात्**'
    ),
)

register(
    '8.4.16',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        "SETTLED — आनि लोट् — and the न् of आनि where it is the IMPERATIVE'S\n"
        '  ending: **प्रवपाणि, परिवपाणि; प्रयाणि, परियाणि**. The\n'
        '  counter-example is the same four syllables meaning something else\n'
        '  — प्रवपानि मांसानि, the cut meats — where आनि is a case ending and\n'
        '  no cerebral comes'
    ),
)

register(
    '8.4.17',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED —\n'
        '  नेर्गदनदपतपदघुमास्यतिहन्तियातिवातिद्रातिप्सातिवपतिवहतिशाम्यतिचिनोतिदेग्धिषु\n'
        '  च — and the न् of नि before seventeen named roots: **प्रणिगदति,\n'
        '  परिणिगदति; प्रणिनदति; प्रणिपतति; प्रणिपद्यते**. The preverb whose\n'
        '  न् is changed is itself the second of two, प्र or परि standing in\n'
        '  front — which is why the sūtra needs उपसर्गात् carried down as\n'
        '  well as its own नेः'
    ),
)

register(
    '8.4.18',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — शेषे विभाषाऽकखादावषान्त उपदेशे — and before any OTHER\n'
        '  root, optionally, provided it does not begin with क् or ख् and\n'
        '  does not end in ष् as it is taught: **प्रणिपचति, प्रनिपचति;\n'
        '  प्रणिभिनत्ति, प्रनिभिनत्ति**. Three conditions on the following\n'
        '  root and one option over them, which is as close as the pāda comes\n'
        '  to a general rule about नि'
    ),
)

register(
    '8.4.19',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — अनितेः — and the न् of अन्: **प्राणिति, पराणिति**. The\n'
        "  root is अन् 'to breathe', and this is where प्राण and every word\n"
        '  made from it gets its cerebral'
    ),
)

register(
    '8.4.20',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        "SETTLED — अन्तः — and even at a WORD'S END: **हे प्राण्, हे पराण्**.\n"
        '  **पदान्तस्य इति प्रतिषेधस्य अपवादोऽयम्** — 8.4.37 will refuse the\n'
        '  cerebral to every word-final न्, and this one word is taken out of\n'
        '  that refusal seventeen sūtras before it is stated'
    ),
)

register(
    '8.4.21',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — उभौ साभ्यासस्य — and where अन् has been reduplicated, BOTH\n'
        '  of its न् sounds become ण्: **प्राणिणिषति, प्राणिणत्; पराणिणिषति, पराणिणत्**.\n'
        '  The vṛtti works out why the sūtra is needed at all — with\n'
        '  **पूर्वत्रासिद्धीयम् अद्विर्वचने** in force, a cerebral already\n'
        '  made would not be copied, so the second ण् has to be given\n'
        '  outright'
    ),
)

register(
    '8.4.22',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — हन्तेरत्पूर्वस्य — and the न् of हन् when a SHORT अ stands\n'
        '  before it: **प्रहण्यते, परिहण्यते; प्रहणनम्, परिहणनम्**. Both\n'
        '  conditions are tested — प्रघ्नन्ति has lost the अ altogether, and\n'
        '  प्राघानि has a long one, which the तपर keeps out'
    ),
)

register(
    '8.4.23',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — वमोर्वा — and before a व् or a म् it is optional:\n'
        '  **प्रहण्वः, प्रहन्वः; परिहण्वः, परिहन्वः; प्रहण्मः, प्रहन्मः**.\n'
        '  The forms are the dual and plural of the first person, so one\n'
        '  paradigm has the cerebral fixed in some cells and optional in two'
    ),
)

register(
    '8.4.24',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — अन्तरदेशे — and after अन्तर्, provided no PLACE is meant:\n'
        '  **अन्तर्हण्यते; अन्तर्हणनं वर्तते**. A place called अन्तर्हनन\n'
        '  keeps its plain न्. अन्तर् is not a preverb, which is why हन्\n'
        '  needs a rule of its own here after having had one at 8.4.22'
    ),
)

register(
    '8.4.25',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — अयनं च — and the न् of अयन after अन्तर्, again not of a\n'
        '  place: **अन्तरयणं वर्तते; अन्तरयणं शोभनम्**. The sense-condition\n'
        '  is carried down from the sūtra before and does the same work on a\n'
        '  different word'
    ),
)

register(
    '8.4.26',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — छन्दस्यृदवग्रहात् — and in the VEDA after an ऋ-final first\n'
        '  member that the pada text separates: **नृमणाः, पितृयाणम्** —\n'
        '  **अत्र हि नृऽमनाः, पितृऽयानम् इति ऋकारोऽवगृह्यते**. The condition\n'
        '  is about how the word is RECITED, not about how it is made, which\n'
        '  is a kind of condition found nowhere else in the work'
    ),
)

register(
    '8.4.27',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — नश्च धातुस्थोरुषुभ्यः — and the न् of नस् after a cause\n'
        '  standing IN THE ROOT, and after उरु and षु, in the Veda: **अग्ने\n'
        '  रक्षा णः; शिक्षा णो अस्मिन्**. The enclitic नस् is a word of its\n'
        "  own, so 8.4.1's समानपदे could not have reached it — the whole\n"
        '  sūtra is a way round that condition'
    ),
)

register(
    '8.4.28',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — उपसर्गाद् बहुलम् — and after a preverb, VARIOUSLY: **प्रणः\n'
        '  शूद्रः; प्रणो राजा** — and **न च भवति — प्र नो मुञ्चतम्**.\n'
        '  **बहुलग्रहणाद् भाषायाम् अपि भवति** — बहुलम् here does something\n'
        '  the Vedic rules around it do not: it carries the rule into the\n'
        '  spoken language, **प्रणसं मुखम्**'
    ),
)

register(
    '8.4.29',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — कृत्यचः — and a न् inside a कृत् AFFIX, standing after a\n'
        '  vowel: **प्रयाणम्, परियाणम्; प्रमाणम्, परिमाणम्**. The vṛtti lists\n'
        '  the affixes that can bring one — **अन, मान, अनीय, अनि, इनि** and\n'
        "  the निष्ठा's substitute — which is a way of saying that कृत् here\n"
        '  is a much smaller class than it sounds. Every प्रमाण and परिमाण\n'
        '  comes from this'
    ),
)

register(
    '8.4.30',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — णेर्विभाषा — but where the कृत् has been added to a CAUSAL\n'
        '  stem it is optional: **प्रयापणम्, प्रयापनम्; परियापणम्, परियापनम्;\n'
        '  प्रयाप्यमाणम्, प्रयाप्यमानम्**. The णि itself is a ण् and might\n'
        '  have been thought to make the cerebral certain; the sūtra says the\n'
        '  opposite'
    ),
)

register(
    '8.4.31',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — हलश्चेजुपधात् — and where the root begins with a consonant\n'
        '  and has an इच् in its penult, optionally: **प्रकोपणम्, प्रकोपनम्;\n'
        '  परिकोपणम्, परिकोपनम्**. Two conditions on the root, and between\n'
        '  this sūtra and the one before, most of what 8.4.29 gave\n'
        '  compulsorily is turned back into a choice'
    ),
)

register(
    '8.4.32',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — इजादेः सनुमः — but where the root begins with an इच् and\n'
        '  has a नुम् in it, the cerebral is compulsory again: **प्रेङ्खणम्,\n'
        '  परेङ्खणम्; प्रेङ्गणम्, परेङ्गणम्; प्रोम्भणम्**. **हल इति वर्तते।\n'
        '  तेन इह सामर्थ्यात् तदन्तविधिः** — the consonant-final condition is\n'
        "  carried down and read of the root's END"
    ),
)

register(
    '8.4.33',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — वा निंसनिक्षनिन्दाम् — and the न् of निंस्, निक्ष् and\n'
        '  निन्द् optionally: **प्रणिंसनम्, प्रनिंसनम्; प्रणिक्षणम्,\n'
        '  प्रनिक्षणम्; प्रणिन्दनम्, प्रनिन्दनम्**. All three are णोपदेश\n'
        '  roots, so 8.4.14 would have made the cerebral compulsory — and\n'
        '  this is what makes it a choice'
    ),
)

register(
    '8.4.34',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — न भाभूपूकमिगमिप्यायीवेपाम् — and here the refusals begin:\n'
        "  the कृत्'s न् does NOT become ण् after these seven: **प्रभानम्,\n"
        '  परिभानम्; प्रभवनम्, परिभवनम्; प्रपवनम्, परिपवनम्**. Six sūtras of\n'
        '  refusal close the run, and this is the only one of them that names\n'
        '  roots'
    ),
)

register(
    '8.4.35',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — षात् पदान्तात् — nor after a ष् that ENDS A WORD:\n'
        '  **निष्पानम्, दुष्पानम्, सर्पिष्पानम्, यजुष्पानम्**. Both words are\n'
        '  tested, and the compound is read as a locative — **पदे अन्तः\n'
        '  पदान्त इति सप्तमीसमासोऽयम्** — so what is refused is the ष्\n'
        '  standing at the end of a word and not a word ending in ष्'
    ),
)

register(
    '8.4.36',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — नशेः षान्तस्य — nor of नश् IN ITS ष्-FINAL SHAPE:\n'
        '  **प्रनष्टः, परिनष्टः**. And अन्तग्रहण widens it to what was once\n'
        '  ष्-final and no longer is — **षान्तभूतपूर्वमात्रस्य अपि यथा\n'
        '  स्यात्** — for प्रनङ्क्ष्यति, where the ष् has already become\n'
        '  something else'
    ),
)

register(
    '8.4.37',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — पदान्तस्य — nor of a न् that ENDS a word: **वृक्षान्,\n'
        '  प्लक्षान्, अरीन्, गिरीन्**. This is the widest of the six refusals\n'
        '  and the one that keeps every accusative plural in the language\n'
        '  from coming out with a cerebral. 8.4.20 had taken one word out of\n'
        '  it seventeen sūtras earlier'
    ),
)

register(
    '8.4.38',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — पदव्यवायेऽपि — nor where a WHOLE WORD stands between the\n'
        '  र् and the न्: **माषकुम्भवापेन; चतुरङ्गयोगेन; प्रावनद्धम्; प्र गां\n'
        "  नयामः; परि गां नयामः**. This is 8.4.1's समानपदे said again from\n"
        '  the other side — the first sūtra of the pāda wanted one word and\n'
        '  the thirty-eighth refuses where there are two'
    ),
)

register(
    '8.4.39',
    apply=the_cerebral_n,
    codification=_THE_CEREBRAL_N,
    notes=(
        'SETTLED — क्षुभ्नादिषु च — nor in the क्षुभ्नादि class:\n'
        '  **क्षुभ्नाति; नृनमनः**. The refusal reaches the altered shapes too\n'
        '  — **अजादेशस्य स्थानिवद्भावाद् इह अपि प्रतिषेधो भवति — क्षुभ्नीतः,\n'
        '  क्षुभ्नन्ति** — and the second example is one 8.4.3 would have\n'
        '  reached across a compound seam. With it the cerebral न् is\n'
        '  finished and the pāda turns to the cerebral of everything else'
    ),
)


_AT_THE_JUNCTION = (
    'at_the_junction(word, gana=..., after=..., before=..., '
    'sense=..., view=...) -> the assimilations, the doubling and '
    'the close of the work, by rule of 8.4.40-68.'
)

register(
    '8.4.40',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — स्तोः श्चुना श्चुः — a स् or a त-वर्ग meeting a श् or a\n'
        '  च-वर्ग takes their class. And the Kāśikā at once says what one\n'
        '  might expect and is not so — **स्तोःश्चुना इति यथासंख्यम् अत्र न\n'
        '  इष्यते** — the two pairs are NOT matched one to one: a स् becomes\n'
        '  श् whether the cause is a श् or a palatal stop, and a त-वर्ग\n'
        '  becomes a palatal either way. This is the rule तच्छिवः and रामश्च\n'
        '  are made by'
    ),
)

register(
    '8.4.41',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — ष्टुना ष्टुः — and meeting a ष् or a ट-वर्ग they take THAT\n'
        '  class: **वृक्षष्षण्डे, प्लक्षष्षण्डे** for the ष्,\n'
        '  **वृक्षष्टीकते** for the cerebral stop. **अत्र अपि तथैव\n'
        '  संख्यातानुदेशाभावः** — the same refusal to match the pairs one to\n'
        '  one, said again in one clause. स्तोः is carried down from the\n'
        '  sūtra before'
    ),
)

register(
    '8.4.42',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — न पदान्ताट्टोरनाम् — but NOT after a ट-वर्ग that ends a\n'
        '  word, except before नाम्: **श्वलिट् साये; मधुलिट् तरति**. All\n'
        '  three of its words are tested, and the exception for नाम् is what\n'
        '  makes षण्णाम् come out as it does. The Kāśikā thinks the exception\n'
        '  too narrow — **अत्यल्पम् इदम् उच्यते**'
    ),
)

register(
    '8.4.43',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — तोः षि — nor of a त-वर्ग before a ष्: **अग्निचित् षण्डे;\n'
        '  भवान् षण्डे; महान् षण्डे**. 8.4.41 would have made the त् a ट्,\n'
        '  and this keeps it out — which is why a त्-final word before a\n'
        '  ष्-initial one is heard unchanged where before a ट्-initial one it\n'
        '  is not'
    ),
)

register(
    '8.4.44',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — शात् — nor of a त-वर्ग AFTER a श्: **प्रश्नः, विश्नः**.\n'
        '  तोः is carried down from the sūtra before, and what is new is that\n'
        "  the cause stands in front rather than behind — so 8.4.40's palatal\n"
        '  does not come and प्रश्नः keeps its न्'
    ),
)

register(
    '8.4.45',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — यरोऽनुनासिकेऽनुनासिको वा — a word-final यर् OPTIONALLY\n'
        '  becomes the answering nasal before a nasal: **वाङ् नयति, वाग्\n'
        '  नयति; श्वलिण् नयति, श्वलिड् नयति; अग्निचिन् नयति, अग्निचिद् नयति;\n'
        '  त्रिष्टुम् नयति, त्रिष्टुब् नयति**. Four pairs, one for each class\n'
        '  of stop, and the option is what makes both readings of every such\n'
        '  junction correct'
    ),
)

register(
    '8.4.46',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — अचो रहाभ्यां द्वे — a यर् after a र् or a ह् that itself\n'
        '  follows a VOWEL is doubled: **अर्क्कः, मर्क्कः; ब्रह्म्मा;\n'
        '  अपह्न्नुते**. This and the next are the two doubling rules the\n'
        '  manuscripts almost never write out, and the three sūtras after\n'
        '  them are three teachers saying so'
    ),
)

register(
    '8.4.47',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — अनचि च — and a यर् after ANY vowel, provided no vowel\n'
        '  follows it: **दद्ध्यत्र, मद्ध्वत्र**. A vārttika restates it with\n'
        '  two pratyāhāras — **यणो मयो द्वे भवतः** — and the Kāśikā records a\n'
        '  disagreement about which of the two cases is ablative and which\n'
        '  genitive, which changes what the rule reaches'
    ),
)

register(
    '8.4.48',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — नादिन्याक्रोशे पुत्रस्य — but पुत्र is not doubled before\n'
        '  आदिनी where ABUSE is meant: **पुत्रादिनी त्वम् असि पापे** — you\n'
        '  child-eater, you wretch. **आक्रोश इति किम्? तत्त्वकथने द्विर्वचनं\n'
        '  भवत्य् एव** — said as a plain statement of fact the doubling\n'
        '  comes, and the word is then पुत्त्रादिनी'
    ),
)

register(
    '8.4.49',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — शरोऽचि — nor is a शर् doubled before a vowel: **कर्षति,\n'
        '  वर्षति; आदर्शः, अक्षदर्शः**. 8.4.46 would have doubled the ष् of\n'
        '  कर्षति, the र् standing in front of it after a vowel, and this\n'
        '  keeps it out'
    ),
)

register(
    '8.4.50',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        "SETTLED — त्रिप्रभृतिषु शाकटायनस्य — and in ŚĀKAṬĀYANA'S view there\n"
        '  is no doubling where three or more consonants already stand\n'
        '  together: **इन्द्रः, चन्द्रः, मन्द्रः, राष्ट्रम्, भ्राष्ट्रम्**.\n'
        '  The first of three teachers, and the narrowest of the three\n'
        '  refusals'
    ),
)

register(
    '8.4.51',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        "SETTLED — सर्वत्र शाकल्यस्य — and in ŚĀKALYA'S view there is none\n"
        '  ANYWHERE: **अर्कः, मर्कः, ब्रह्मा, अपह्नुते**. This is the reading\n'
        "  the manuscripts in fact follow, and the four words are 8.4.46's\n"
        '  own examples given back without their doubling — which is as plain\n'
        '  a way as the Kāśikā has of saying which teacher won'
    ),
)

register(
    '8.4.52',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        "SETTLED — दीर्घादाचार्याणाम् — and in the TEACHERS' view there is\n"
        '  none after a long vowel: **दात्रम्, पात्रम्, मूत्रम्, सूत्रम्**.\n'
        '  Three sūtras, three namings, three different measures of the same\n'
        "  refusal — and the grammar's own rule stands between them without\n"
        '  ever being withdrawn'
    ),
)

register(
    '8.4.53',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — झलां जश् झशि — a झल् becomes the answering जश् before a\n'
        '  झश्: **लब्धा, लब्धुम्, लब्धव्यम्; दोग्धा, दोग्धुम्; बोद्धा,\n'
        '  बोद्धुम्**. This is what voices the first half of every such\n'
        '  cluster, and 8.2.40 had already made the second half aspirate — so\n'
        "  लभ् plus त becomes लब्ध through two pādas' worth of rules"
    ),
)

register(
    '8.4.54',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — अभ्यासे चर्च — in the REDUPLICATION a झल् becomes the\n'
        '  answering चर्, and by the च a जश् as well: **चिखनिषति,\n'
        '  चिच्छित्सति, टिठकारयिषति, तिष्ठासति, बुभूषति, जिघत्सति,\n'
        '  डुढौकिषते**. And where the copy already has a चर् it keeps it —\n'
        '  **प्रकृतिचरां प्रकृतिचरो भवन्ति — चिचीषति, टिटीकिषते**. Every\n'
        '  reduplicated stem in the language passes through this rule and\n'
        '  through 7.4.60 together'
    ),
)

register(
    '8.4.56',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — वाऽवसाने — and at a PAUSE a झल् becomes चर् OPTIONALLY:\n'
        '  **वाक्, वाग्; त्वक्, त्वग्; श्वलिट्, श्वलिड्; त्रिष्टुप्,\n'
        '  त्रिष्टुब्**. **झलां चर् इति वर्तते**. This is why a Sanskrit word\n'
        '  quoted alone may be heard two ways, and why the lexica differ with\n'
        '  themselves about which form to print'
    ),
)

register(
    '8.4.57',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — अणोऽप्रगृह्यस्यानुनासिकः — and an अण् that is not प्रगृह्य\n'
        '  optionally goes NASAL at a pause: **दधिँ, दधि; मधुँ, मधु; कुमारीँ,\n'
        '  कुमारी**. The nasalised vowel at the end of an isolated word is a\n'
        '  feature of recitation the written language has almost no way to\n'
        '  show, and this is the sūtra that prescribes it'
    ),
)

register(
    '8.4.58',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — अनुस्वारस्य ययि परसवर्णः — an anusvāra before a यय्\n'
        "  becomes the nasal OF THAT SOUND'S OWN CLASS: **शङ्किता, उञ्छिता,\n"
        '  कुण्डिता, नन्दिता, कम्पिता**. Five words for five classes, and\n'
        '  this is why a nasal inside a Sanskrit word always agrees with what\n'
        '  follows it — which the writing system then records with five\n'
        '  different letters'
    ),
)

register(
    '8.4.59',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — वा पदान्तस्य — but a word-final anusvāra does it only\n'
        '  OPTIONALLY: **तङ् कथञ् चित्रपक्षण् डयमानन् नभःस्थम् पुरुषोऽवधीत्**\n'
        '  beside **तं कथं चित्रपक्षं डयमानं नभःस्थं पुरुषोऽवधीत्**. One line\n'
        '  given twice over, every nasal in it assimilated in the first and\n'
        '  left as an anusvāra in the second — the clearest illustration in\n'
        '  the pāda'
    ),
)

register(
    '8.4.60',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — तोर्लि — a त-वर्ग before a ल् becomes ल्: **अग्निचिल्\n'
        '  लुनाति; सोमसुल् लुनाति; भवाँल् लुनाति; महाँल् लुनाति**. The last\n'
        '  two show the nasalised ल् that a न् becomes, which no other rule\n'
        '  of the work provides and which the writing shows with a\n'
        '  candrabindu'
    ),
)

register(
    '8.4.61',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — उदः स्थास्तम्भोः पूर्वस्य — after उद्, the स् of स्था and\n'
        '  स्तम्भ् takes the class of what stands BEFORE it: **उत्त्थाता,\n'
        '  उत्त्थातुम्, उत्त्थातव्यम्; उत्तम्भिता, उत्तम्भितुम्**. Everywhere\n'
        '  else in the pāda a sound takes the class of what FOLLOWS, and this\n'
        '  is the one rule that reverses the direction'
    ),
)

register(
    '8.4.62',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — झयो होऽन्यतरस्याम् — and a ह् after a झय् optionally takes\n'
        '  the class of what precedes: **वाग्घसति, वाग् हसति; श्वलिड् ढसति;\n'
        '  अग्निचिद्धसति; सोमसुद्धसति; त्रिष्टुब्भसति**. It is the same\n'
        '  backward direction as the sūtra before, and this time over a whole\n'
        '  class of sounds'
    ),
)

register(
    '8.4.63',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — शश्छोऽटि — and a श् after a झय् with an अट् after it\n'
        '  optionally becomes छ्: **वाक्छेते, वाक् शेते; अग्निचिच्छेते;\n'
        '  सोमसुच्छेते; श्वलिट् छेते**. अन्यतरस्याम् is carried down from the\n'
        '  sūtra before, which is how three optional rules in a row are\n'
        '  stated with one word between them'
    ),
)

register(
    '8.4.64',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — हलो यमां यमि लोपः — a यम् after a consonant is optionally\n'
        '  DROPPED before another यम्: in शय्या there are two य् and a third\n'
        '  made by the doubling, **तत्र मध्यमस्य वा लोपो भवति** — the middle\n'
        '  one goes, or does not: **शय्या, शय्य्या**. The rule is about what\n'
        '  the doubling of 8.4.46–47 has just produced, and about nothing\n'
        '  else'
    ),
)

register(
    '8.4.65',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — झरो झरि सवर्णे — and a झर् after a consonant before a\n'
        '  HOMOGENEOUS झर्: in प्रत्तम् there are three त् and a fourth from\n'
        '  the doubling, **तत्र मध्यमस्य मध्यमयोर् वा लोपो भवति** — one may\n'
        '  go or two. This and the sūtra before are what keep the written\n'
        '  language from having to show clusters four and five sounds deep'
    ),
)

register(
    '8.4.66',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — उदात्तादनुदात्तस्य स्वरितः — an अनुदात्त after an उदात्त\n'
        '  becomes स्वरित: **गार्ग्यः, वात्स्यः; पचति, पठति**. And the vṛtti\n'
        '  points out what the asiddhatva of the tripādī does here — **अस्य\n'
        '  स्वरितस्य असिद्धत्वाद् 6.1.158 अनुदात्तं पदम् एकवर्जम् इत्येतद् न\n'
        '  प्रवर्तते** — the स्वरित this rule makes is invisible to the rule\n'
        '  that would have made everything else toneless, so both accents are\n'
        '  heard'
    ),
)

register(
    '8.4.67',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम् — but not where an\n'
        '  उदात्त or a स्वरित FOLLOWS, in the view of everyone EXCEPT Gārgya,\n'
        '  Kāśyapa and Gālava: **पूर्वेण प्राप्तः प्रतिषिध्यते**. The sūtra\n'
        '  is the only place in the work where teachers are named to be\n'
        '  excluded rather than followed, and the three named are the ones\n'
        '  who would have let the स्वरित come'
    ),
)

register(
    '8.4.68',
    apply=at_the_junction,
    codification=_AT_THE_JUNCTION,
    notes=(
        'SETTLED — अ अ इति — and the Aṣṭādhyāyī ends on two syllables.\n'
        '  **एकोऽत्र विवृतः, अपरः संवृतः। तत्र विवृतस्य संवृतः क्रियते** — of\n'
        '  the two अ written here the first is OPEN and the second CLOSED,\n'
        '  and the open one is replaced by the closed. **वृक्षः, प्लक्षः**.\n'
        '\n'
        'SETTLED — **AND WHAT IT UNDOES IS SOMETHING THE GRAMMAR ITSELF PUT\n'
        '  THERE.** **इह शास्त्रे कार्यार्थम् अकारो विवृतः प्रतिज्ञातः, तस्य\n'
        '  तथाभूतस्य एव प्रयोगो मा भूद् इति संवृतप्रतिज्ञानम्** — the अ of\n'
        '  अइउण् was declared open so that it could count as homogeneous with\n'
        '  आ and the whole machinery of सवर्ण could work; and the last rule\n'
        '  of the work closes it again so that nothing is ever actually\n'
        '  SPOKEN that way. The book begins by making a sound up and ends by\n'
        '  taking it back'
    ),
)


__all__ = [
    'at_the_junction',
    'khari_ca',
    'the_cerebral_n',
]
