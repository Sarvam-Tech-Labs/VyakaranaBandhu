# -*- coding: utf-8 -*-
"""अध्याय ३, पाद १ — the paribhāṣā that suspends the utsarga-apavāda doctrine."""

from __future__ import annotations

from src.astadhyayi.paribhasa import displaces
from src.astadhyayi.anga import sap
from src.astadhyayi.sanadi import dhatu_by, pacadi, yan
from src.astadhyayi.pratyaya import accent_of, named_affix, position_of
from src.astadhyayi.sanadi import ayadi_optional, sanadi_affix
from src.astadhyayi.sources import register
from src.astadhyayi.krtya import NIPATANA as _krtya_nipatana
from src.astadhyayi.krt_agent import agent_affix
from src.astadhyayi.krtya import krtya_affix
from src.astadhyayi.krtya import nipatana as krtya_nipatana
from src.astadhyayi.vikarana import (
    dhatoh_heading, karmavat, krt, krtya, upapada,
    vedic_latitude,
    vikarana,
)
from src.astadhyayi.tense_affix import (
    anuprayoga, cli_becomes, cli_slot, nipatana, sarvadhatuke_yak,
    tense_affix,
)



register(
    '3.1.94',
    reuses=('1.3.2', '1.3.9'),
    apply=displaces,
    codification=(
        'displaces(utsarga=..., apavada=...) -> whether the exception displaces its rule outright or only optionally.'
    ),
    notes=(
        "SETTLED — and it bears directly on 1.4.2. That sūtra's Kāśikā\n"
        '  laid down that an अपवाद beats its उत्सर्ग invariably, whatever\n'
        '  the order, because the two are not तुल्यबल. This one suspends\n'
        '  that for the whole kṛt section: there an exception of\n'
        '  *dissimilar form* displaces only optionally, and both affixes\n'
        "  stand. 3.1.135's क beside 3.1.133's ण्वुल् and तृच् gives\n"
        '  विक्षिपः, विक्षेपकः and विक्षेप्ता all three.\n'
        '\n'
        'SETTLED — असरूप इति किम्? An exception of the *same* form still\n'
        '  blocks outright, and sameness is measured after the anubandhas\n'
        "  are set aside: नानुबन्धकृतम् असारूप्यम्. 3.2.1's अण् and\n"
        "  3.2.3's क are both अ once the ण् and the क् are gone, so गोदः\n"
        "  and कम्बलदः stand alone. The codification calls 1.3.2–1.3.9's\n"
        '  it-analysis to strip them rather than listing which affixes\n'
        '  count as alike.\n'
        '\n'
        'SETTLED — अस्त्रियामिति किम्? Nor in the feminine section:\n'
        "  3.3.94's क्तिन् is displaced by 3.3.102's अ outright, and\n"
        '  चिकीर्षा, जिहीर्षा are the only forms.\n'
        '\n'
        'SETTLED — the field is the kṛt section, 3.1.91 धातोः to 3.4.117,\n'
        '  which `reading.adhikara` already records from the corpus. Both\n'
        '  rules of the pair must stand in it, since a sūtra read under\n'
        '  धातोः says nothing about a pair straddling its edge.'
    ),
)


register(
    '3.1.68',
    apply=sap,
    codification=(
        'sap(kartari=..., sarvadhatuka_follows=...) -> whether शप् comes '
        'after the root.'
    ),
    related=('1.3.3', '1.3.8', '1.3.9', '3.1.67', '3.4.113', '7.3.84'),
    notes=(
        'SETTLED — कर्तृवाचिनि सार्वधातुके परतो धातोः शप् प्रत्ययो भवति:\n'
        '  भवति, पचति. This is the अ that stands between root and ending in\n'
        '  the commonest present forms, and it is the first affix this\n'
        '  codification adds to a form rather than merely names.\n'
        '\n'
        'SETTLED — both its letters are indicatory and the Kāśikā says what\n'
        '  each is for: पकारः स्वरार्थः, शकारः सार्वधातुकसंज्ञार्थः. The प्\n'
        '  is for accent; the श् is there to bring 3.4.113. Neither survives\n'
        '  1.3.9, so what is left is a bare अ — an affix that is nothing but\n'
        '  a vowel, whose whole grammatical character was carried by two\n'
        '  letters that are then thrown away.\n'
        '\n'
        'SETTLED — कर्तरि is a real condition, not a formality. Where the\n'
        '  sārvadhātuka denotes not the agent but the action or the object,\n'
        '  3.1.67 gives यक् instead: क्रियते कटः, गम्यते ग्रामः.'
    ),
)


__all__ = [
    'displaces',
]


register(
    '3.1.22',
    reuses=('1.1.71', '6.1.1', '6.1.9'),
    apply=yan,
    codification=(
        'yan(root, kriyasamabhihara=..., sopasarga=...) -> the यङन्त stem '
        'and how it was built, or which condition refused it.'
    ),
    notes=(
        'SETTLED — पौनःपुन्यं भृशार्थो वा क्रियासमभिहारः, doing a thing\n'
        '  again and again or doing it hard: पुनःपुनः पचति gives पापच्यते,\n'
        '  भृशं ज्वलति gives जाज्वल्यते. देदीप्यते, यायज्यते.\n'
        '\n'
        'SETTLED — three conditions, and the Kāśikā tests each. धातोरिति\n'
        '  किम्? भृशं प्राटति — सोपसर्गाद् उत्पत्तिर्मा भूत्. एकाच इति\n'
        '  किम्? भृशं जागर्ति. हलादेरिति किम्? भृशम् ईक्षते.\n'
        '\n'
        'SETTLED — एकाच् here is a बहुव्रीहि, having one vowel, which is\n'
        '  6.1.1\'s reading and not 1.1.14\'s. The two rules read the same\n'
        '  word oppositely and disagree on प्र.\n'
        '\n'
        'SETTLED — the sense is a parameter because no form carries it, and\n'
        '  the Kāśikā shows why that is not a shortcoming: भृशं शोभते and\n'
        '  भृशं रोचते are refused अनभिधानात्, on usage alone. A rule cannot\n'
        '  be asked to see that.\n'
        '\n'
        'SCOPE — the vārttika adds seven roots that fail एकाच् or हलादि —\n'
        '  सूचिसूत्रिमूत्र्यट्यर्त्यशूर्णोतीनां ग्रहणम् — giving सोसूच्यते,\n'
        '  अटाट्यते, अरार्यते, प्रोर्णोनूयते. They are named in\n'
        '  VARTTIKA_ROOTS; only अटि reaches a stem, the rest wanting work\n'
        '  on the root before the doubling that is not codified.'
    ),
)

register(
    '3.1.32',
    reuses=('1.3.1',),
    apply=dhatu_by,
    codification=(
        'dhatu_by(stem, sanadyanta=...) -> that the stem bears the name '
        'धातु, and which of the two rules conferred it.'
    ),
    samjna='धातु',
    notes=(
        'SETTLED — सनादयोऽन्ते येषां ते सनाद्यन्ताः: a stem ending in one\n'
        '  of the सनादि affixes is itself a root. चिकीर्षति, पुत्रीयति,\n'
        '  पुत्रकाम्यति.\n'
        '\n'
        'SETTLED — two rules confer this one name and the codification asks\n'
        '  both: 1.3.1 भूवादयो धातवः for what the dhātupāṭha lists, and this\n'
        '  for what the grammar builds. लू is a root by the first, लोलूय by\n'
        '  the second and only by the second — it is in no list.\n'
        '\n'
        'SETTLED — and that is what 1.1.4 turns on. If लोलूय is a धातु then\n'
        '  the यङ् inside it is a धात्वेकदेश, and the Kāśikā\'s opening line\n'
        '  there — धात्वेकदेशो धातुः — makes eliding the यङ् an eliding of\n'
        '  the root. Without this sūtra 1.1.4 would have nothing to bite on\n'
        '  and लोलुवः would come out लोलवः.\n'
        '\n'
        'SCOPE — only यङ् among the सनादि affixes is codified, so a stem in\n'
        '  सन् or in क्यच् is not built here even though this rule names it.'
    ),
)

register(
    '3.1.134',
    apply=pacadi,
    codification=(
        'pacadi(stem, yananta=...) -> that अच् comes after this stem, on '
        'the पचादि gaṇa read from the gaṇapāṭha.'
    ),
    notes=(
        'SETTLED — त्रिभ्यो गणेभ्यस्त्रयः प्रत्यया यथासंख्यं भवन्ति: three\n'
        '  classes and three affixes paired in order — नन्द्यादि takes ल्यु,\n'
        '  ग्रहादि takes णिनि, पचादि takes अच्. The gaṇapāṭha on disk has\n'
        '  all three, 25 and 26 and 36 entries.\n'
        '\n'
        'SETTLED — पचादि is marked open-ended in that file, an आकृतिगण, and\n'
        '  that is what lets a यङन्त stem in. The Kāśikā on 1.1.4 says so\n'
        '  outright: लोलूयादिभ्यो यङन्तेभ्यः पचाद्यचि विहिते.\n'
        '\n'
        'SETTLED — नन्दिग्रहिपचादयश्च न धातुपाठतः संनिविष्टा गृह्यन्ते.\n'
        '  These are not dhātupāṭha entries but stems drawn out of\n'
        '  prātipadika lists, which is why membership is a lookup.\n'
        '\n'
        'SCOPE — only the third gaṇa and its अच् are codified. ल्यु and\n'
        '  णिनि are recognised in the record and not applied.'
    ),
)

# -------------------------------------------------------------------------
# 3.1.1 to 3.1.31 — what an affix is, and the affixes that
# make a new root.
# -------------------------------------------------------------------------

_HEADING = (
    'named_affix(kind=..., sup=..., pit=...) -> whether the name प्रत्यय '
    'reaches it, where it stands, and how it is accented.'
)
_SANADI = (
    'sanadi_affix(base, is_root=..., sense=...) -> which सनादि affix '
    'is added, and by which rule.'
)
_AYADI = (
    'ayadi_optional(affix, ardhadhatuka=...) -> whether 3.1.31 makes '
    'this one optional.'
)

_OPENING = {
    '3.1.1': 'SETTLED — प्रत्ययः is an अधिकार, and the largest in the grammar:\n  आ पञ्चमाध्यायपरिसमाप्तेः. Whatever is enumerated from 3.1.5 to\n  the end of adhyāya 5 bears the name without a rule saying so\n  again. प्रत्ययशब्दः संज्ञात्वेनाधिक्रियते.\n\nSETTLED — but NOT everything a rule in that range names. The vṛtti\n  excludes five kinds outright: प्रकृत्युपपदोपाधिविकारागमान्\n  वर्जयित्वा. A rule adding an affix also names the base, sometimes\n  a word that must stand beside it, a condition, a change, an\n  augment — and none of those is the affix. The exclusion is\n  codified as a list rather than left to be inferred, because\n  inferring it is exactly what a reader cannot do.\n\nSETTLED — the vṛtti points forward to show the heading working:\n  वक्ष्यति तव्यत्तव्यानीयरः (3.1.96), कर्त्तव्यम्, करणीयम्. And it\n  names where the name is USED — प्रत्ययप्रदेशाः — 1.1.62\n  प्रत्ययलोपे प्रत्ययलक्षणम् and the rest.',
    '3.1.2': 'SETTLED — परश्च: an affix stands AFTER the root or the stem, never\n  before. कर्तव्यम्, तैत्तिरीयम्. अयमप्यधिकारो योगे योग उपतिष्ठते,\n  परिभाषा वा — heading or paribhāṣā, either way it reaches every\n  rule that follows.\n\nSETTLED — चकारः पुनरस्यैव समुच्चयार्थः, तेन उणादिषु परत्वं न\n  विकल्प्यते. The च joins this to 3.1.1 rather than offering an\n  alternative to it, and the point of that is the उणादि section,\n  where the affixes are least regular and the position could\n  otherwise have been thought open.',
    '3.1.3': "SETTLED — आद्युदात्तश्च: the accent falls on the affix's FIRST\n  vowel. कर्तव्यम्, तैत्तिरीयम्.\n\nSETTLED — and the vṛtti says why a rule was needed at all:\n  अनियतस्वरप्रत्ययप्रसङ्गे अनेकाक्षु च प्रत्ययेषु देशस्यानियमे सति\n  वचनमिदम् आदेरुदात्तार्थम् — with an affix of more than one\n  syllable there is nothing to say WHICH syllable takes it. The\n  rule fixes a place, not a fact.",
    '3.1.4': 'SETTLED — अनुदात्तौ सुप्पितौ: the सुप् endings and anything marked\n  with प् are unaccented. दृषदौ, दृषदः; पचति, पठति.\n\nSETTLED — पूर्वस्यायमपवादः, an exception to 3.1.3 and not a\n  separate topic. Codified before it for that reason: an अपवाद\n  read after the rule it excepts can never fire, which is the same\n  ordering 2.4.16 needed against 2.4.15.',
    '3.1.5': 'SETTLED — गुप्तिज्किद्भ्यः सन्: जुगुप्सते, तितिक्षते, चिकित्सति.\n  प्रत्ययसंज्ञा चाधिकृतैव — the name comes from 3.1.1 and is not\n  restated, which is what an अधिकार is for.\n\nSETTLED — a vārttika holds it to three senses:\n  निन्दाक्षमाव्याधिप्रतीकारेषु सन्निष्यते, अन्यत्र यथाप्राप्तं\n  प्रत्यया भवन्ति — blame, forbearance, warding off disease. In any\n  other sense the ordinary affixes come: गोपयति, तेजयति,\n  सङ्केतयति. Codified as a condition, since without it the rule\n  would swallow those.\n\nSETTLED — गुपादिष्वनुबन्धकरणमात्मनेपदार्थम्: the marks written on\n  the roots in the sūtra are there for the middle endings, not for\n  identifying which root is meant.',
    '3.1.6': "SETTLED — मान्बधदान्शान्भ्यो दीर्घश्चाभ्यासस्य: मीमांसते, बीभत्सते,\n  दीदांसते, शीशांसते. The rule adds the affix AND lengthens the\n  reduplicated syllable's इ, so the row carries both.\n\nSETTLED — a sense is wanted here too: अत्रापि सन्नर्थविशेष इष्यते —\n  मानेर्जिज्ञासायाम्, बधेर्वैरूप्ये, दानेरार्जवे, शानेर्निशाने. One\n  sense per root. Without it मानयति, बाधयति, दानयति, निशानयति.",
    '3.1.7': "SETTLED — धातोः कर्मणः समानकर्तृकादिच्छायां वा: कर्तुमिच्छति,\n  चिकीर्षति; जिहीर्षति. Four conditions, and the vṛtti gives a\n  counter for every one — धातोरिति किम्? प्राचिकीर्षत्. कर्मण इति\n  किम्? गमनेनेच्छति. समानकर्तृकादिति किम्? देवदत्तस्य भोजनमिच्छति\n  यज्ञदत्तः. इच्छायामिति किम्? कर्तुं जानाति.\n\nSETTLED — कर्मत्वं समानकर्तृकत्वं च धातोरर्थद्वारकम्. A root is not\n  literally an object or an agent; it is so THROUGH its meaning,\n  and the vṛtti says as much rather than letting the reader trip\n  over it.\n\nSETTLED — and this सन् is आर्धधातुक where 3.1.5's and 3.1.6's are\n  not: धातोरिति विधानादत्र सन आर्धधातुकसंज्ञा भवति, न पूर्वत्र. The\n  word धातोः is what makes the difference, because 3.4.114's शेष\n  turns on what the affix is added to. Three rules add the same\n  affix and only one of them makes it आर्धधातुक.\n  वावचनाद् वाक्यमपि भवति: the वा leaves the phrase standing too.",
    '3.1.8': "SETTLED — सुप आत्मनः क्यच्: आत्मनः पुत्रमिच्छति, पुत्रीयति. The base\n  shifts here from a root to a finished WORD, which is what सुपः\n  says, and the run stays on words until 3.1.22.\n\nSETTLED — सुब्ग्रहणं किम्? महान्तं पुत्रमिच्छति — a phrase takes no\n  affix. आत्मन इति किम्? राज्ञः पुत्रमिच्छति: the wish must be for\n  what is one's own.\n\nSETTLED — ककारो नः क्ये इति सामान्यग्रहणार्थः. The क् is marked so\n  that 1.4.15 can name क्यच्, क्यङ् and क्यष् together as क्य, and\n  चकारस्तदविघातार्थः, the च so the marking is not undone.",
    '3.1.9': 'SETTLED — काम्यच्च: आत्मनः पुत्रमिच्छति, पुत्रकाम्यति; वस्त्रकाम्यति.\n\nSETTLED — योगविभाग उत्तरत्र क्यचोऽनुवृत्त्यर्थः. The rule is split\n  off so that क्यच् and NOT काम्यच् carries down to 3.1.10 — the\n  same device this project met three times in 2.4, and the same\n  kind of claim: about what the split prevents.\n\nSETTLED — ककारस्येत्संज्ञा प्रयोजनाभावान् न भवति. The क् of काम्यच्\n  is not an इत् at all, having nothing to do; alternatively the\n  affix is read as a चकारादि. Recorded as the vṛtti leaves it,\n  with both readings.',
    '3.1.10': "SETTLED — उपमानादाचारे: पुत्रमिवाचरति, पुत्रीयति छात्रम्;\n  प्रावारीयति कम्बलम्. क्यजनुवर्तते, न काम्यच् — which is what\n  3.1.9's split bought.\n\nSETTLED — आचारक्रियायाः प्रत्ययार्थत्वात् तदपेक्षयैवोपमानस्य\n  कर्मता. The thing compared is an object only in relation to the\n  behaving, which is what the affix means — not an object of the\n  sentence's verb. A vārttika adds the locative: प्रासादीयति\n  कुट्याम्, पर्यङ्कीयति मञ्चके.",
    '3.1.11': 'SETTLED — कर्तुः क्यङ् सलोपश्च: श्येन इवाचरति काकः, श्येनायते;\n  कुमुदं पुष्करायते. Here the comparison is with the AGENT where\n  3.1.10 took the object, so the two divide the ground between\n  them.\n\nSETTLED — अन्वाचयशिष्टः सलोपः: the स-elision is added on and is\n  not a condition, तदभावेऽपि क्यङ् भवत्येव — the affix comes\n  whether or not there is a स to drop.\n\nSETTLED — and the elision is a व्यवस्थितविभाषा, an option that is\n  settled differently for different words rather than free:\n  ओजसोऽप्सरसो नित्यं पयसस्तु विभाषया. ओजायते and अप्सरायते always,\n  पयायते beside पयस्यते.\n\nSETTLED — सलोपविधौ च कर्तुरिति स्थानषष्ठी संपद्यते, तत्र\n  अलोऽन्त्यनियमे सति. Being a genitive of substitution it reaches\n  the LAST sound only, by 1.1.52 — so हंसायते and सारसायते keep\n  their स, the स there not being final.',
    '3.1.12': 'SETTLED — भृशादिभ्यो भुव्यच्वेर्लोपश्च हलः: अभृशो भृशो भवति,\n  भृशायते; शीघ्रायते. The sense is अभूततद्भाव — becoming what one\n  was not. Read from the gaṇapāṭha on disk.\n\nSETTLED — अच्वेः is a प्रतिषेध the vṛtti admits is redundant, and\n  keeps for a reason: यावता भवतियोगे च्विर्विधीयते, तेन\n  उक्तार्थत्वात् च्व्यन्तेभ्यो न क्यङ् भविष्यति — तत्सदृशप्रतिपत्त्यर्थं\n  तर्हि च्विप्रतिषेधः क्रियते. Stated to fix the pattern by showing\n  its edge. Recorded, since it is the same form of argument as\n  the ज्ञापनs met in 2.4.',
    '3.1.13': "SETTLED — लोहितादिडाज्भ्यः क्यष्: लोहितायति, लोहितायते; and after\n  a डाच्-final, पटपटायति. Read from disk, and आकृतिगणश्चायम् — the\n  list is open.\n\nSETTLED — the vārttika divides 3.1.12's affix from this one BY the\n  list: लोहितडाज्भ्यः क्यष्वचनम्, भृशादिष्वितराणि — what is read in\n  लोहितादि takes क्यङ्, what is not read there takes क्यष्. So\n  वर्मायति, निद्रायति, करुणायति, कृपायति go by this rule.\n\nSETTLED — ककारः सामान्यग्रहणार्थः अनुबध्यते, and the vṛtti gives\n  the proof that it can be nothing else: नहि पठितानां मध्ये\n  नकारान्तः शब्दोऽस्ति — no member of the list ends in न्, so the\n  क् cannot be there for 1.4.15's sake in this rule alone; it is\n  marked to let all three क्य affixes be named together.",
    '3.1.14': 'SETTLED — कष्टाय क्रमणे: कष्टाय कर्मणे क्रामति, कष्टायते. The word\n  stands in the fourth case, and क्रमण here is अनार्जव, striving\n  that is not straightforward. क्यङ् अनुवर्तते, न क्यष्.\n\nSCOPE — अत्यल्पमिदमुच्यते, says the vṛtti of the sūtra itself: too\n  little is stated. A vārttika widens it to six words in the sense\n  कण्वचिकीर्षा — सत्रायते, कक्षायते, कृच्छ्रायते, गहनायते.\n  Recorded; the six are not codified as a list of their own.',
    '3.1.15': 'SETTLED — कर्मणो रोमन्थतपोभ्यां वर्तिचरोः, यथाक्रमम्: रोमन्थं\n  वर्तयति, रोमन्थायते गौः; तपश्चरति, तपस्यति. Two words, two\n  senses, paired in order.\n\nSETTLED — two vārttikas. हनुचलन इति वक्तव्यम् narrows the first to\n  the moving of the jaw, so कीटो रोमन्थं वर्तयति is out; तपसः\n  परस्मैपदं च gives the second the active endings, which is why\n  तपस्यति and not तपस्यते.',
    '3.1.16': 'SETTLED — बाष्पोष्मभ्यामुद्वमने: बाष्पमुद्वमति, बाष्पायते;\n  ऊष्मायते. A vārttika adds फेन — फेनायते.',
    '3.1.17': "SETTLED — शब्दवैरकलहाभ्रकण्वमेघेभ्यः करणे: शब्दं करोति, शब्दायते;\n  वैरायते, कलहायते, अभ्रायते, कण्वायते, मेघायते.\n\nSCOPE — two vārttikas add eleven more words: सुदिनायते,\n  दुर्दिनायते, नीहारायते, and eight beginning अटायते. Recorded as\n  additions to the sūtra's six rather than folded into them.",
    '3.1.18': 'SETTLED — सुखादिभ्यः कर्तृवेदनायाम्: सुखं वेदयते, सुखायते;\n  दुःखायते. वेदना is अनुभव, feeling it oneself. Read from disk.\n\nSETTLED — कर्तृग्रहणं किम्? सुखं वेदयते प्रसाधको देवदत्तस्य. The\n  feeling must belong to the one who feels it; where it is\n  produced FOR another the rule does not reach.',
    '3.1.19': 'SETTLED — नमोवरिवश्चित्रङः क्यच्, and each of the three in its own\n  sense: नमसः पूजायाम्, नमस्यति देवान्; वरिवसः परिचर्यायाम्,\n  वरिवस्यति गुरून्; चित्रङ आश्चर्ये, चित्रीयते.\n\nSETTLED — ङकार आत्मनेपदार्थः on the THIRD word only, which is why\n  चित्रीयते takes the middle and नमस्यति does not. The mark sits\n  on the base, not on the affix, and reaches only what carries it.',
    '3.1.20': 'SETTLED — पुच्छभाण्डचीवरात् णिङ्, and vārttikas give each its sense:\n  पुच्छाद् उदसने पर्यसने वा — उत्पुच्छयते, परिपुच्छयते; भाण्डात्\n  समाचयने — संभाण्डयते; चीवरादर्जने परिधाने वा — संचीवरयते भिक्षुः.\n\nSETTLED — two marks, two jobs, and the vṛtti names both: णकारः\n  सामान्यग्रहणार्थः णेरनिटि (6.4.51) इति, so that every णि can be\n  named together; ङकार आत्मनेपदार्थः, for the middle endings.',
    '3.1.21': "SETTLED — मुण्डमिश्रश्लक्ष्णलवणव्रतवस्त्रहलकलकृततूस्तेभ्यो णिच्:\n  मुण्डं करोति, मुण्डयति; मिश्रयति, श्लक्ष्णयति, लवणयति. Ten words\n  named in the sūtra itself, and several with a sense the vārttikas\n  supply — व्रताद् भोजने तन्निवृत्तौ च, वस्त्रात् समाच्छादने.\n\nSETTLED — हलिकल्योरदन्तत्वनिपातनं सन्वद्भावप्रतिषेधार्थम्. हलि and\n  कलि are given in the sūtra as a-final though they are not, and\n  the reason is downstream: it keeps 7.4.93's सन्वद्भाव away, so\n  अजहलत् and अचकलत् and not the reduplicated forms it would give.\n  A shape written into a rule to control what a later rule does.",
    '3.1.23': "SETTLED — नित्यं कौटिल्ये गतौ: कुटिलं क्रामति, चङ्क्रम्यते;\n  दन्द्रम्यते. Only of a root that MEANS going — गतिवचनाद् धातोः.\n\nSETTLED — नित्यग्रहणं विषयनियमार्थम्, and that is not what नित्यम्\n  usually does. It does not remove an option; it fixes the SCOPE:\n  गतिवचनान्नित्यं कौटिल्य एव भवति, न तु क्रियासमभिहारे — from a\n  going-root the affix comes for crookedness only, and 3.1.22's\n  repetition no longer reaches it. भृशं क्रामति has no यङ्.\n  Codified as a scope-narrowing and not as an obligation.",
    '3.1.24': 'SETTLED — लुपसदचरजपजभदहदशगॄभ्यो भावगर्हायाम्: गर्हितं लुम्पति,\n  लोलुप्यते; सासद्यते, चञ्चूर्यते, जञ्जप्यते, दन्दह्यते.\n\nSETTLED — भावग्रहणं किम्? साधनगर्हायां मा भूत् — मन्त्रं जपति\n  वृषलः. It is the ACT that is blamed, not who does it, and\n  without भाव the rule would have reached a censure of the agent.\n\nSETTLED — नित्यग्रहणं विषयनियमार्थम् carries down from 3.1.23 and\n  does the same work here: from these eight the affix comes for\n  blame ONLY, so भृशं लुम्पति has none.',
    '3.1.25': 'SETTLED — सत्यापपाशरूपवीणातूलश्लोकसेनालोमत्वचवर्मवर्णचूर्णचुरादिभ्यो\n  णिच्: सत्यमाचष्टे, सत्यापयति; विपाशयति, निरूपयति, उपवीणयति,\n  अनुतूलयति, उपश्लोकयति, अभिषेणयति, अनुलोमयति, संवर्मयति.\n\nSETTLED — the sūtra names TWO different bases and they are codified\n  as two rows. The thirteen before चुरादि are STEMS; चुरादि is the\n  tenth class of the dhātupāṭha and its members are ROOTS. Written\n  as one row with both conditions the named list shut the class\n  out and चुर् reached nothing — caught while smoke-testing.\n\nSETTLED — चुरादि is read from the corpus by its class code, as\n  2.4.72 reads the second class, and both now ask one helper. A\n  copied list would be a second statement of what the dhātupāṭha\n  already says.\n\nSETTLED — a vārttika gives three of them an आपुक्: अर्थमाचष्टे,\n  अर्थापयति; वेदापयति. And आपुग्वचनसामर्थ्यात् टिलोपो न भवति — the\n  augment being stated at all shows the टि is not to be dropped.',
    '3.1.26': 'SETTLED — हेतुमति च: कटं कारयति, ओदनं पाचयति. And the vṛtti defines\n  both terms rather than leaving them: हेतुः स्वतन्त्रस्य कर्तुः\n  प्रयोजकः — the cause is what sets the independent agent going;\n  तदीयो व्यापारः प्रेषणादिलक्षणो हेतुमान् — and what the affix means\n  is that prompting, not the causer.\n\nSCOPE — two vārttikas. तत्करोतीत्युपसंख्यानम् gives सूत्रयति. The\n  आख्यान rule is larger — आख्यानात् कृतस्तदाचष्ट इति णिच् कृल्लुक्\n  प्रकृतिप्रत्यापत्तिः प्रकृतिवच्च कारकम् — a णिच् after a कृत्-form,\n  the कृत् then dropped, the base restored, and the case-roles kept\n  as they were: कंसवधमाचष्टे, कंसं घातयति. Four operations in one\n  vārttika; recorded, not modelled.',
    '3.1.27': 'SETTLED — कण्ड्वादिभ्यो यक्: कण्डूयति, कण्डूयते. Read from disk.\n\nSETTLED — द्विविधाः कण्ड्वादयः, धातवः प्रातिपदिकानि च — the list\n  holds both roots and stems, and the vṛtti settles which is meant\n  by WHERE the rule stands: धात्वधिकाराद् धातुभ्य एव प्रत्ययो\n  विधीयते, न तु प्रातिपदिकेभ्यः. Position in the text deciding a\n  reading the words leave open.\n\nSETTLED — the क् is marked to keep guṇa off, गुणप्रतिषेधार्थः; and\n  ञित्त्वात् 1.3.72 gives कण्डूञ् the middle where the fruit falls\n  to the agent.',
    '3.1.28': "SETTLED — गुपूधूपविच्छिपणिपनिभ्य आयः: गोपायति, धूपायति, विच्छायति,\n  पणायति, पनायति.\n\nSETTLED — पण् is taken in the sense of praising only, and the\n  argument is one of company: स्तुत्यर्थेन पनिना साहचर्यात् तदर्थः\n  पणिः प्रत्ययमुत्पादयति, न व्यवहारार्थः — पन् beside it means to\n  praise, so पण् is read the same way and शतस्य पणते is untouched.\n  The same form of argument as 2.4.79's थासा साहचर्यात्.\n\nSETTLED — अनुबन्धश्च केवले चरितार्थः: the marks on the roots did\n  their work on the bare roots, so they do not carry over — the\n  आय-stem takes no middle endings.",
    '3.1.29': "SETTLED — ऋतेरीयङ्: ऋतीयते, ऋतीयेते, ऋतीयन्ते. ऋति is a सौत्र root,\n  one the sūtra itself supplies rather than the dhātupāṭha, in the\n  sense of loathing. ङकार आत्मनेपदार्थः.\n\nSETTLED — and the rule is written though the form was already\n  obtainable: ऋतेश्छङिति सिद्धे ईयङ्वचनं ज्ञापनार्थम् — a rule\n  stated where it was not needed, TEACHING that the आयादि affixes\n  do not come after affixes prescribed to a root. The third\n  ज्ञापन this project has codified, after 2.4.36's ल्यप् and\n  2.4.66's भरत, and the same shape: what it teaches lands\n  somewhere other than where it is said.",
    '3.1.30': 'SETTLED — कमेर्णिङ्: कामयते, कामयेते, कामयन्ते. णकारो वृद्ध्यर्थः,\n  ङकार आत्मनेपदार्थः — two marks, two jobs, and the vṛtti names\n  each, as at 3.1.20.',
    '3.1.31': "SETTLED — आयादय आर्धधातुके वा. आयादयः is आय and what follows it,\n  which the vṛtti takes as the affixes of 3.1.28, 3.1.29 and\n  3.1.30 — so this rule speaks ABOUT three earlier rules rather\n  than adding a fourth affix, and has its own entry point for\n  that reason.\n\nSETTLED — गोप्ता beside गोपायिता, अर्तिता beside ऋतीयिता, कमिता\n  beside कामयिता; and it reaches the nominal derivatives too,\n  गुप्तिः beside गोपाया.\n\nSETTLED — नित्यं प्रत्ययप्रसङ्गे तदुत्पत्तिः आर्धधातुकविषये\n  विकल्प्यते. The affix was obligatory, and what is made optional\n  is the ADDING of it, not anything about the affix itself.\n  तत्र यथायथं प्रत्यया भवन्ति: on the side where it is not added,\n  the ordinary affixes come to the bare root.\n\nSCOPE — whether an affix is आर्धधातुक is 3.4.114's question and is\n  not codified; it is passed in, as at 2.4.35. The debt is the\n  same one and is recorded in both places.",
}

#: 3.1.1 to 3.1.4 say what an affix IS; 3.1.31 speaks about three
#: affixes rather than adding one. Everything between adds one.
#: Each of the four answers its own question and reports itself. One
#: function serving all four named only 3.1.1, so asking 3.1.2 came back
#: citing a rule that had not acted — the same fault as a refusal
#: reporting the wrong rule, caught by the case guard.
_HEADINGS = {
    "3.1.1": ("named_affix", "is it an affix at all?"),
    "3.1.2": ("position_of", "where does it stand?"),
    "3.1.3": ("accent_of", "how is it accented?"),
    "3.1.4": ("accent_of", "and the exception to that"),
}
_ENTRY = {"named_affix": named_affix, "position_of": position_of,
          "accent_of": accent_of}
_LINES = {
    "named_affix": _HEADING,
    "position_of": ("position_of() -> where an affix stands, and by "
                    "which rule."),
    "accent_of": ("accent_of(sup=..., pit=...) -> how an affix is "
                  "accented, and by which rule."),
}

for _sutra, _notes in _OPENING.items():
    if _sutra in _HEADINGS:
        _fn = _HEADINGS[_sutra][0]
        _apply, _line = _ENTRY[_fn], _LINES[_fn]
    elif _sutra == "3.1.31":
        _apply, _line = ayadi_optional, _AYADI
    else:
        _apply, _line = sanadi_affix, _SANADI
    register(
        _sutra,
        apply=_apply,
        codification=_line,
        notes=_notes,
        # No reuse is declared across this run. 3.1.22 यङ् has its own
        # function, `yan`, and 3.1.23 and 3.1.24 add the same affix on
        # quite different grounds — a shared affix is not a shared rule,
        # and neither row runs that code. 3.1.25 asks the dhātupāṭha
        # through `verbal_gana`, which is corpus access and not one rule
        # running another.
    )

# -------------------------------------------------------------------------
# 3.1.33 to 3.1.67 — the affix a lakāra brings with it.
# -------------------------------------------------------------------------

_TENSE = (
    'tense_affix(lakara=..., root=...) -> which affix stands between '
    'root and endings, and by which rule.'
)
_ANUPRAYOGA = (
    'anuprayoga(after_am=...) -> which second verb follows the आम्.'
)
_CLI_SLOT = 'cli_slot() -> the placeholder 3.1.43 opens.'
_CLI = (
    'cli_becomes(root, voice=..., pada=...) -> what च्लि becomes, '
    'and by which rule.'
)
_YAK = (
    'sarvadhatuke_yak(voice=...) -> whether यक् comes, and by which '
    'rule.'
)

_LAKARA = {
    '3.1.33': "SETTLED — स्यतासी लृलुटोः, यथासंख्यम्: स्य for लृ and तासि for\n  लुट्. करिष्यति, अकरिष्यत्; श्वः कर्ता.\n\nSETTLED — लृ is written without marks and stands for BOTH लृट् and\n  लृङ्: लृरूपम् उत्सृष्टानुबन्धं सामान्यम् एकमेव. One syllable\n  covering two lakāras, which is why अकरिष्यत् needs no rule of\n  its own.\n\nSETTLED — इदित्करणम् अनुनासिकलोपप्रतिबन्धार्थम्. The इ of तासि is\n  marked to STOP 6.4.37's elision of a nasal, so मन्ता and\n  संगन्ता keep theirs. A mark added to prevent a later rule, as at\n  2.4.54 and 3.1.21.",
    '3.1.34': 'SETTLED — सिब्बहुलं लेटि: जोषिषत्, तारिषत्, मन्दिषत्; and न च\n  भवति पताति दिद्युत्, उदधिं च्यावयाति.\n\nSETTLED — बहुलम् and not अन्यतरस्याम्. Both are attested and\n  neither is offered as a choice, which is the distinction this\n  project has carried since 2.4.39: an option is something the\n  speaker may take, बहुलम् is a report of usage.',
    '3.1.35': 'SETTLED — कास्प्रत्ययादाममन्त्रे लिटि: कासाञ्चक्रे, and after any\n  affix-final stem लोलूयाञ्चके. अमन्त्र इति किम्? कृष्णो नोनाव.\n\nSETTLED — प्रत्ययात् is what carries the whole सनादि run into the\n  perfect. 3.1.5 to 3.1.31 made stems, 3.1.32 called them roots,\n  and this gives those roots a perfect they could not otherwise\n  have had — लोलूय is the very stem the लोलुवः derivation built.\n  Three widely separated rules and one form passing through all\n  of them.\n\nSCOPE — a vārttika reads कास् as अनेकाच्, चुलुम्पाद्यर्थम्, to\n  reach polysyllabic roots; another gives four properties of the\n  आम् in a verse. Recorded, not modelled.',
    '3.1.36': 'SETTLED — इजादेश्च गुरुमतोऽनृच्छः: ईहाञ्चक्रे, ऊहाञ्चक्रे. Three\n  conditions and a counter for each — इजादेरिति किम्? ततक्ष,\n  ररक्ष. गुरुमत इति किम्? इयज, उवप. अनृच्छ इति किम्? आनर्च्छ.\n\nSETTLED — ऋच्छ् meets both conditions and is excepted BY NAME,\n  which is why the exception has to be stated at all. Codified as\n  a refusal inside the rule rather than as a missing condition.\n\nSCOPE — a vārttika adds ऊर्णु to the exception, प्रोर्णुनाव;\n  another proposes ऊर्णोर्णुवद्भाव instead and gives its own\n  reasons. Recorded with both readings, as the vṛtti leaves them.',
    '3.1.37': 'SETTLED — दयायासश्च: दयाञ्चक्रे, पलायाञ्चक्रे, आसाञ्चक्रे.',
    '3.1.38': "SETTLED — उषविदजागृभ्योऽन्यतरस्याम्: ओषाञ्चकार beside उवोष,\n  विदाञ्चकार beside विवेद, जागराञ्चकार beside जजागार.\n\nSETTLED — विदेरदन्तत्वप्रतिज्ञानाद् आमि गुणो न भवति: विद् is\n  taken as a-final by declaration, and that is what keeps guṇa\n  from the आम् form. The same device as 3.1.21's हलि and कलि — a\n  shape asserted in order to control a later rule.",
    '3.1.39': 'SETTLED — भीह्रीभृहुवां श्लुवच्च: बिभयाञ्चकार beside बिभाय,\n  जुहवाञ्चकार beside जुहाव. The option carries down from 3.1.38.\n\nSETTLED — श्लुवत् is not left to be looked up: the vṛtti asks and\n  answers it in one breath — किं पुनस्तत्? द्वित्वम् इत्त्वं च,\n  the doubling and the इ. So the row carries what the likeness\n  amounts to and not merely the word.\n  The श्लु itself is 2.4.75, codified.',
    '3.1.40': 'SETTLED — कृञ् चानुप्रयुज्यते लिटि: पाचयाञ्चकार, पाचयाम्बभूव,\n  पाचयामास. कृञ् is a प्रत्याहार — कृञिति प्रत्याहारेण कृभ्वस्तयो\n  गृह्यन्ते — so all three auxiliaries serve.\n\nSETTLED — AND THAT NAMING KEEPS 2.4.52 OFF. तत्सामर्थ्यादस्तेर्भूभावो न भवति: अस्तेर्भूः would have turned अस् into भू\n  and पाचयामास could never be formed. The rule is not prohibited —\n  it is displaced by the fact that THIS rule would be pointless if\n  it applied. Held by a test, since the claim is about a rule in\n  another adhyāya and running 3.1.40 cannot check it.\n',
    '3.1.41': 'SETTLED — विदाङ्कुर्वन्त्वित्यन्यतरस्याम्, a निपातन. The vṛtti\n  unpacks what is fixed whole — विदेर्लोटि आम्प्रत्ययः, गुणाभावः,\n  लोटो लुक्, कृञश्च लोट्परस्यानुप्रयोगः: four things at once.\n  विदाङ्कुर्वन्तु beside विदन्तु.\n\nSETTLED — इतिकरणः प्रदर्शनार्थः, न केवलं प्रथमपुरुषबहुवचनम्. The\n  इति shows a specimen and does not confine the rule to the one\n  form given: विदाङ्करोतु, विदाङ्कुरुतात्, विदाङ्कुरु and the rest\n  all follow. A form quoted in a sūtra standing for its whole\n  paradigm.',
    '3.1.42': 'SETTLED — a निपातन of several Vedic forms at once, and the vṛtti\n  sorts out which rule each suspends: आम् in the aorist for three\n  ण्यन्त roots, आम् with doubling and कुत्व for चि, आम् in the\n  benedictive for पू, and आम् with गुणाभाव for विद्. अकः, क्रियात्\n  and अक्रन् are the auxiliaries each takes.\n\nSCOPE — the forms are recorded as the sūtra fixes them and are not\n  derived. A निपातन is by definition what the rules do not reach.',
    '3.1.43': 'SETTLED — च्लि लुङि, a placeholder. It creates the slot that\n  3.1.44 to 3.1.66 fill, and describes nothing: इकार उच्चारणार्थः,\n  चकारः स्वरार्थः — the इ only to make it sayable, the च for the\n  accent. Nothing of it survives into any form.\n\nSETTLED — and the vṛtti declines to give an example, saying where\n  the examples belong: अस्य सिजादीन् आदेशान् वक्ष्यति,\n  तत्रैवोदाहरिष्यामः. Codified as the rule that opens the slot,\n  with its own entry point, rather than as one that makes a form.',
    '3.1.44': 'SETTLED — च्लेः सिच्: अकार्षीत्, अहार्षीत्. The default, and every\n  rule after it is an अपवाद — which is why the table takes the\n  LAST matching row and this one matches unconditionally.\n\nSETTLED — the reason for the च is given: आगमानुदात्तत्वं हि\n  प्रत्ययस्वरम् इव चित्स्वरम् अपि बाधेत, so the mark is written on\n  both the स्थानिन् and the आदेश — द्विश्चकारोऽनुबध्यते.\n\nSCOPE — a vārttika makes the सिच् a choice for six roots:\n  अस्प्राक्षीत्, अस्पार्क्षीत्, अस्पृक्षत्. Three forms apiece;\n  recorded, not modelled.',
    '3.1.45': 'SETTLED — शल इगुपधादनिटः क्सः: अधुक्षत्, अलिक्षत्. Three\n  conditions and the vṛtti gives a counter for each — शल इति\n  किम्? अभैत्सीत्, अच्छैत्सीत्. इगुपधादिति किम्? अधाक्षीत्.\n  अनिट इति किम्? अकोषीत्, अमोषीत्.',
    '3.1.46': "SETTLED — श्लिष आलिङ्गने: आश्लिक्षत् कन्यां देवदत्तः.\n\nSETTLED — and it RESTRICTS rather than grants: अत्र नियमार्थमेतत्.\n  श्लिष् already met 3.1.45's three conditions, so without this\n  rule it would take क्स in every sense; the rule confines it to\n  embracing. आलिङ्गन इति किम्? समाश्लिषज्जतु काष्ठम् — of glue\n  sticking to wood the क्स does not come. A नियम is the opposite\n  of a विधि and is codified as a condition, not as a new grant.",
    '3.1.47': 'SETTLED — न दृशः, a प्रतिषेध against 3.1.45.\n\nSETTLED — and the vṛtti says what happens once it is out of the\n  way: अस्मिन् प्रतिषिद्धे इरितो वा इत्यङ्सिचौ भवतः — 3.1.57\n  answers instead and BOTH forms stand, अदर्शत् and अद्राक्षीत्.\n  A prohibition whose effect is not silence but a different rule\n  becoming reachable.',
    '3.1.48': 'SETTLED — णिश्रिद्रुस्रुभ्यः कर्तरि चङ्, सिजपवादश्चङ् विधीयते:\n  अचीकरत्, अशिश्रियत्, अदुद्रुवत्, असुस्रुवत्. कर्तरीति किम्?\n  अकारयिषातां कटौ देवदत्तेन.\n\nSETTLED — two marks, two later rules, and the vṛtti names both:\n  ङकारो गुणवृद्धिप्रतिषेधार्थः, and चकारः 6.1.11 चङि इति\n  विशेषणार्थः — the च so that the reduplication rule can pick this\n  substitute out by name.\n\nSCOPE — a vārttika adds कम्, and divides by whether 3.1.31 left\n  the णिङ् in place: अचकमत without it, अचीकमत with, the second\n  taking सन्वद्भाव. Recorded; it turns on a rule already codified\n  at 3.1.31 and on 7.4.93, which is not.',
    '3.1.49': 'SETTLED — विभाषा धेट्श्व्योः: अदधत्, अशिश्वियत्.\n\nSETTLED — and on the other side of the option the सिच् comes and\n  is then elided by 2.4.78 विभाषा घ्राधेट्शाच्छासः — अधात् beside\n  अधासीत्. Two optional rules in different adhyāyas meeting on one\n  root, and both are codified.\n  अङोऽप्यत्र विकल्प इष्यते: the vṛtti wants अङ् in the mix for\n  श्वि as well — अश्वत्, अश्वयीत्.',
    '3.1.50': "SETTLED — गुपेश्छन्दसि, optionally: अजूगुपतम्. यत्र आयप्रत्ययो\n  नास्ति, तत्रायं विधिः — only where 3.1.28's आय is not there.\n\nSETTLED — and the vṛtti states the ordinary-speech position as the\n  complement: भाषायां तु चङन्तं वर्जयित्वा शिष्टं रूपत्रयं भवति —\n  outside the Veda the चङ् form is the one that does NOT stand,\n  and the other three do.",
    '3.1.51': 'SETTLED — नोनयतिध्वनयत्येलयत्यर्दयतिभ्यः, a प्रतिषेध against\n  3.1.48 in the Veda: काममूनयीः, मा त्वाग्निर्ध्वनयीत्. In\n  ordinary speech the चङ् does come — औनिनत्, अदिध्वनत्, ऐलिलत्,\n  आर्दिदत्. So the prohibition is confined to छन्दस् and the\n  refusal carries that condition.',
    '3.1.52': 'SETTLED — अस्यतिवक्तिख्यातिभ्योऽङ्: पर्यास्थत्, अवोचत्, आख्यत्.\n  कर्तरीति किम्? पर्यासिषातां गावौ वत्सेन.\n\nSETTLED — अस् is named though it was already reachable, and the\n  vṛtti says what the repetition buys: अस्यतेः पुषादिपाठादेव अङि\n  सिद्धे पुनर्ग्रहणम् आत्मनेपदार्थम् — 3.1.55 confines itself to\n  the active, so naming अस् here is what gets the middle,\n  पर्यास्थत, पर्यास्थेताम्. A rule stated where it seemed not to\n  be needed, doing other work — the shape met at 2.4.36 and\n  3.1.29.\n\nSETTLED — two of the three are themselves substitutes: वच् may be\n  what ब्रू became by 2.4.53, and ख्या what चक्षिङ् became by\n  2.4.54. Both those rules are codified, and this one acts on what\n  they produced.',
    '3.1.53': 'SETTLED — लिपिसिचिह्वश्च: अलिपत्, असिचत्, आह्वत्.\n  पृथग्योग उत्तरार्थः — split off so that 3.1.54 can reach these\n  three alone and not everything 3.1.52 reached.',
    '3.1.54': 'SETTLED — आत्मनेपदेष्वन्यतरस्याम्, पूर्वेण प्राप्ते\n  विभाषारभ्यते: 3.1.53 had made it obligatory and this makes it a\n  choice in the middle. अलिपत beside अलिप्त, असिचत beside असिक्त,\n  अह्वत beside अह्वास्त. The middle itself comes from 1.3.72,\n  which is codified.',
    '3.1.55': "SETTLED — पुषादिद्युताद्यॢदितः परस्मैपदेषु: अपुषत्, अद्युतत्,\n  अश्वितत्, अगमत्, अशकत्. परस्मैपदेष्विति किम्? व्यद्योतिष्ट,\n  अलोटिष्ट.\n\nSETTLED — WHICH पुषादि is stated, because the name is read in more\n  than one place: पुषादिर् दिवाद्यन्तर्गणो गृह्यते, न\n  भ्वादिक्र्याद्यन्तर्गणः — the sub-gaṇa inside the FOURTH class,\n  not the ones inside the first and ninth. One name, three lists,\n  and the vṛtti picks. Same shape as 2.4.58's कौरव्य.\n\nSETTLED — the sūtra names three groups and they are codified as\n  two rows, because they are not found the same way. ऌदित् is\n  written on the root in the dhātupāṭha, so it is READ: गम्ऌ and\n  शक्ऌ are found by asking 1.3.2 उपदेशेऽजनुनासिक इत्, which is\n  codified, rather than by a second parser over the same\n  upadeśas.\n\nSCOPE — पुषादि and द्युतादि are sub-gaṇas the gaṇapāṭha on disk\n  holds no members for, so those must be asserted by the caller.\n  The gap is in the corpus and is recorded here rather than\n  papered over with a hand-copied list.",
    '3.1.56': 'SETTLED — सर्तिशास्त्यर्तिभ्यश्च: असरत्, अशिषत्, आरत्.\n\nSETTLED — पृथग्योगकरणम् आत्मनेपदार्थम्, split off so the middle is\n  reached: समरन्त. And चकारः परस्मैपदेष्वित्यनुकर्षणार्थः, तच्च\n  उत्तरत्र उपयोगं यास्यति — the च drags परस्मैपदेषु down, and the\n  vṛtti notes its use is felt further on, at 3.1.57.',
    '3.1.57': "SETTLED — इरितो वा: अभिदत् beside अभैत्सीत्, अच्छिदत् beside\n  अच्छैत्सीत्. परस्मैपदेष्वित्येव, carried by 3.1.56's च —\n  अभित्त and अच्छित्त keep the सिच्.\n\nSETTLED — इरित् is read from the corpus, not asserted. भिदिर् and\n  छिदिर् carry the mark in the dhātupāṭha, and 1.3.2 is what makes\n  it an इत्, so that rule is asked.\n\nSETTLED — and this is the rule 3.1.47 hands दृश् to once the क्स\n  is refused, which is why both अदर्शत् and अद्राक्षीत् stand.",
    '3.1.58': 'SETTLED — जॄस्तम्भुम्रुचुम्लुचुग्रुचुग्लुचुग्लुञ्चुश्विभ्यश्च,\n  वेति वर्तते: अजरत् beside अजारीत्, अस्तभत् beside अस्तम्भीत्.\n  स्तम्भु is a सौत्र root, one the sūtra supplies itself, as ऋति\n  is at 3.1.29.\n\nSETTLED — the vṛtti notes that ग्लुचु and ग्लुञ्चु would give the\n  same three forms from either alone, and says why both are read:\n  अर्थभेदात् — they differ in sense. A list member kept for its\n  meaning and not for its form.',
    '3.1.59': 'SETTLED — कृमृदृरुहिभ्यश्छन्दसि: अकरत्, अमरत्, अदरत्, आरुहत्.\n  छन्दसीति किम्? अकार्षीत्, अमृत, अदारीत्, अरुक्षत् — outside the\n  Veda each of the four takes something else, and the four are\n  different somethings.',
    '3.1.60': 'SETTLED — चिण् ते पदः: उदपादि सस्यम्, समपादि भैक्षम्. From here\n  to 3.1.66 the substitute is चिण्.\n\nSETTLED — and WHICH त is meant is settled by what the rule can do:\n  सामर्थ्यात् आत्मनेपदैकवचनं गृह्यते — the middle third-person\n  singular. त इति किम्? उदपत्साताम्, उदपत्सत, where the ending is\n  a different त-form. The same kind of narrowing 2.4.79 needed,\n  and settled the same way.',
    '3.1.61': 'SETTLED — दीपजनबुधपूरितायिप्यायिभ्योऽन्यतरस्याम्: अदीपि beside\n  अदीपिष्ट, अजनि beside अजनिष्ट, अबोधि beside अबुद्ध.\n  चिण् त इति वर्तते, both carried down from 3.1.60.',
    '3.1.62': 'SETTLED — अचः कर्मकर्तरि: अकारि कटः स्वयमेव beside अकृत कटः\n  स्वयमेव. अच इति किम्? अभेदि काष्ठं स्वयमेव. कर्मकर्तरीति किम्?\n  अकारि कटो देवदत्तेन.\n\nSETTLED — प्राप्तविभाषेयम्: an option over what an option had\n  already made available. The three kinds of विभाषा are a\n  distinction the commentaries keep, and this is the one where the\n  thing was reachable anyway.',
    '3.1.63': 'SETTLED — दुहश्च: अदोहि गौः स्वयमेव beside अदुग्ध गौः स्वयमेव.\n  दुह् is consonant-final, so 3.1.62 could not have reached it —\n  the rule exists because of that one condition.\n  कर्मकर्तरीत्येव: अदोहि गौर्गोपालकेन is another matter.',
    '3.1.64': 'SETTLED — न रुधः, a प्रतिषेध: अन्ववारुद्ध गौः स्वयमेव.\n  कर्मकर्तरीत्येव, so outside that the चिण् still comes —\n  अन्ववारोधि गौर्गोपालकेन.',
    '3.1.65': 'SETTLED — तपोऽनुतापे च, नेति वर्तते: the prohibition carried down\n  from 3.1.64. अनुतापः पश्चात्तापः, remorse.\n\nSETTLED — and naming the sense WIDENS the refusal rather than\n  narrowing it: तस्य ग्रहणम् अकर्मकर्त्रर्थम्, तत्र हि\n  भावकर्मणोरपि प्रतिषेधो भवति — with अनुताप stated, the चिण् is\n  refused for भाव and कर्मन् too, not only for कर्मकर्तृ.\n  अतप्त तपस्तापसः, अन्ववातप्त पापेन कर्मणा. A condition that looks\n  like a restriction and works as an extension.',
    '3.1.66': 'SETTLED — चिण् भावकर्मणोः: अशायि भवता for the act; अकारि कटो\n  देवदत्तेन and अहारि भारो यज्ञदत्तेन for the object.\n  चिण्ग्रहणं विस्पष्टार्थम् — the affix is named again only for\n  clarity, being already in force from 3.1.60.',
    '3.1.67': "SETTLED — सार्वधातुके यक्: आस्यते भवता, शय्यते भवता; क्रियते कटः,\n  गम्यते ग्रामः. ककारो गुणवृद्धिप्रतिषेधार्थः.\n\nSETTLED — a vārttika reaches कर्मकर्तृ and gives its ground as a\n  conflict settled by strength: यग्निवधाने कर्मकर्तर्युपसंख्यानम्,\n  विप्रतिषेधाद्धि यकः शपो बलीयस्त्वम् — where both यक् and 3.1.68's\n  शप् could come, यक् is the stronger. क्रियते कटः स्वयमेव,\n  पच्यत ओदनः स्वयमेव. 3.1.68 is codified, so the two meet.\n\nSETTLED — and this is where the विकरण run begins, which 3.1.68\n  कर्तरि शप् continues. That rule was reached ahead for the\n  present paradigm of पच्; the run has now caught up with it.",
}

#: Five questions across this run, each answered by the rule that
#: asks it. 3.1.43 opens the च्लि slot, 3.1.44 to 3.1.66 fill it,
#: 3.1.40 is about what follows the आम्, and 3.1.67 begins the विकरण.
_NIPATANA_LINE = ("nipatana(sutra) -> the forms a निपातन rule fixes "
                  "whole, and by which rule.")
_BY_ENTRY = {"3.1.40": (anuprayoga, _ANUPRAYOGA),
             "3.1.41": (nipatana, _NIPATANA_LINE),
             "3.1.42": (nipatana, _NIPATANA_LINE),
             "3.1.43": (cli_slot, _CLI_SLOT),
             "3.1.67": (sarvadhatuke_yak, _YAK)}
_CLI_RULES = tuple("3.1.%d" % n for n in range(44, 67))

for _sutra, _notes in _LAKARA.items():
    if _sutra in _BY_ENTRY:
        _apply, _line = _BY_ENTRY[_sutra]
    elif _sutra in _CLI_RULES:
        _apply, _line = cli_becomes, _CLI
    else:
        _apply, _line = tense_affix, _TENSE
    register(
        _sutra,
        apply=_apply,
        codification=_line,
        notes=_notes,
        # 3.1.55 and 3.1.57 turn on marks the dhātupāṭha writes on the
        # root, and 1.3.2 उपदेशेऽजनुनासिक इत् is what makes those marks
        # its — so `root_its` asks that rule rather than parsing the
        # upadeśas again. That is one rule running another and is
        # declared. Nothing else here is: 2.4.52 being kept off by
        # 3.1.40 is displacement, not a call, and the substitutes 3.1.52
        # acts on were made by rules in another adhyāya and arrive as
        # the root it is given.
        reuses=(("1.3.2",) if _sutra in ("3.1.55", "3.1.57") else ()),
    )

# -------------------------------------------------------------------------
# 3.1.69 to 3.1.93 — the class-marker, and the headings after.
# -------------------------------------------------------------------------

_VIKARANA = (
    'vikarana(root, gana=..., sense=...) -> which class-marker the '
    'root takes, and by which rule.'
)
_VEDIC = (
    'vedic_latitude(lakara=...) -> what the Veda does with the markers.'
)
_KARMAVAT = (
    'karmavat(root, tulyakriya=...) -> whether the agent is treated '
    'as an object, and what follows from it.'
)
_DHATOH = 'dhatoh_heading() -> the अधिकार and its extent.'
_UPAPADA = ('upapada(in_locative=...) -> whether the name उपपद reaches '
            'it, and by which rule.')
_KRT = ('krt(affix=..., is_tin=...) -> whether the name कृत् reaches '
        'it, and by which rule.')

_MARKERS = {
    '3.1.95': 'SETTLED — कृत्याः is an अधिकार over 3.1.96 to 3.1.132, and the range\n  is given by naming the rule it STOPS BEFORE: प्राक् एतस्मात्\n  ण्वुल्संशब्दनात्, before 3.1.133 ण्वुल्तृचौ. The vṛtti gives no\n  example and says where they belong — तत्रैवोदाहरिष्यामः.\n\nSETTLED — कृत्याः is PLURAL, and the Nyāsa gives two readings:\n  बहुत्वात् संज्ञिनाम्, the things named being many; or\n  अनुक्तकृत्प्रत्ययसंग्रहार्थम्, to gather in कृत् affixes not\n  separately listed — on which reading a vārttika adding केलिमर is\n  not needed. Recorded with both, as the Nyāsa leaves them.\n\nSETTLED — कृत्यप्रदेशाः: 2.1.33 कृत्यैरधिकार्थवचने and 2.3.71\n  कृत्यानां कर्तरि वा are where the name is used, and BOTH are\n  codified. This heading is what those two rules of adhyāya 2 were\n  waiting on — the name they invoke is conferred here.',
    '3.1.69': "SETTLED — दिवादिभ्यः श्यन्, शपोऽपवादः: दीव्यति, सीव्यति. The\n  fourth class of the dhātupāṭha, read from the corpus by its\n  code rather than listed here.\n\nSETTLED — two marks, two jobs, and the vṛtti names both: नकारः\n  स्वरार्थः, शकारः सार्वधातुकार्थः — the न् for the accent, the\n  श् so that 1.4.13's सार्वधातुक reaches what follows it.",
    '3.1.70': 'SETTLED — वा भ्राशभ्लाशभ्रमुक्रमुक्लमुत्रसित्रुटिलषः: भ्राश्यते\n  beside भ्राशते, भ्राम्यति beside भ्रमति, त्रस्यति beside त्रसति.\n\nSETTLED — उभयत्र विभाषेयम्, and भ्रमु is read TWICE in the\n  dhātupāṭha — अनवस्थाने and चलने — द्वयोरपि ग्रहणम्, both\n  readings are meant. The first sign in this run that a root\n  name does not pick out one entry.',
    '3.1.71': 'SETTLED — यसोऽनुपसर्गात्: यस्यति beside यसति. यसु is दैवादिक, so\n  3.1.69 would have given it श्यन् obligatorily; this makes it a\n  choice — तस्मान्नित्यं श्यनि प्राप्ते विकल्प उच्यते.\n  अनुपसर्गादिति किम्? आयस्यति, प्रयस्यति.',
    '3.1.72': 'SETTLED — संयसश्च: संयस्यति beside संयसति. सोपसर्गार्थ आरम्भः —\n  the rule exists only because 3.1.71 had shut preverbs out, and\n  this lets one back in. Two rules to say what one could not.',
    '3.1.73': 'SETTLED — स्वादिभ्यः श्नुः, शपोऽपवादः: सुनोति, चिनोति. The fifth\n  class, read from the corpus.',
    '3.1.74': 'SETTLED — श्रुवः शृ च: शृणोति, शृणुतः, शृण्वन्ति. The marker\n  comes and the root changes shape with it, तत्संनियोगेन — two\n  operations in one rule, as at 3.1.80.',
    '3.1.75': 'SETTLED — अक्षोऽन्यतरस्याम्: अक्ष्णोति beside अक्षति. अक्षू is\n  भौवादिकः, a first-class root, so without this rule it would\n  simply have taken शप् — the option is between श्नु and शप्,\n  not between श्नु and nothing.',
    '3.1.76': 'SETTLED — तनूकरणे तक्षः: तक्ष्णोति काष्ठम् beside तक्षति काष्ठम्.\n  तनूकरण इति किम्? संतक्षति वाग्भिः — of cutting someone with\n  words the marker does not come.\n\nSETTLED — and the vṛtti says why a sense is stated at all:\n  अनेकार्थत्वाद् धातूनां विशेषणोपादानम् — roots have many senses,\n  so a rule that wants one says which.',
    '3.1.77': 'SETTLED — तुदादिभ्यः शः, शपोऽपवादः: तुदति, नुदति. The sixth\n  class. शकारः सार्वधातुकसंज्ञार्थः.',
    '3.1.78': 'SETTLED — रुधादिभ्यः श्नम्, शपोऽपवादः: रुणद्धि, भिनत्ति. The\n  seventh class.\n\nSETTLED — and this marker goes INSIDE the root, not after it:\n  मकारो देशविध्यर्थः — the म् says WHERE, and by 1.1.47\n  मिदचोऽन्त्यात् परः it is placed after the last vowel. The only\n  विकरण of the run that is an infix, and the mark is what makes\n  it one. शकारः 6.4.23 श्नान्नलोपः इति विशेषणार्थः.',
    '3.1.79': 'SETTLED — तनादिकृञ्भ्य उः, शपोऽपवादः: तनोति, सनोति, क्षणोति;\n  and करोति.\n\nSETTLED — कृ IS ALREADY IN तनादि, and the naming is not for the\n  marker: तनादिपाठादेव उप्रत्यये सिद्धे करोतेरुपादानं नियमार्थम्,\n  अन्यत् तनादिकार्यं मा भूत्. It RESTRICTS — so that the other\n  things done to तनादि roots are not done to कृ. The one the\n  vṛtti names is 2.4.79 तनादिभ्यस्तथासोः, whose optional elision\n  of सिच् must not reach it: अकृत, अकृथाः. A rule here reaching\n  back to restrict one codified two pādas earlier, and both are\n  codified, so the pair can be tested together.',
    '3.1.80': "SETTLED — धिन्विकृण्व्योर अ च: धिनोति, कृणोति. The उ comes and\n  the root's final becomes अ — two operations in one rule.\n\nSETTLED — अतो लोपस्य स्थानिवद्भावाद् गुणो न भवति: that अ is then\n  dropped, and being स्थानिवत् by 1.1.56 it keeps guṇa away. A\n  sound doing work after it has gone, exactly as at 2.4.42.",
    '3.1.81': 'SETTLED — क्र्यादिभ्यः श्ना, शपोऽपवादः: क्रीणाति, प्रीणाति. The\n  ninth class. शकारः सार्वधातुकसंज्ञार्थः.',
    '3.1.82': 'SETTLED — स्तन्भुस्तुन्भुस्कन्भुस्कुन्भुस्कुञ्भ्यः श्नुश्च:\n  स्तभ्नाति beside स्तभ्नोति. BOTH markers, not a choice between\n  a marker and none — the च adds श्नु to the श्ना carried down.\n\nSETTLED — आद्याश्चत्वारो धातवः सौत्राः, the first four supplied\n  by the sūtra itself and found in no dhātupāṭha. And the vṛtti\n  draws a general conclusion from their marks:\n  उदित्त्वप्रतिज्ञानात् सौत्राणाम् अपि धातूनां सर्वार्थत्वं\n  विज्ञायते, नैतद्विकरणविषयत्वम् एव — a सौत्र root is a root for\n  every purpose, not only for the rule that supplies it.',
    '3.1.83': 'SETTLED — हलः श्नः शानज्झौ: मुषाण, पुषाण. हल इति किम्? क्रीणीहि.\n  हाविति किम्? मुष्णाति. Both conditions are live.\n\nSETTLED — श्नः is written as a स्थानिनिर्देश आदेशसंप्रत्ययार्थः:\n  naming what is REPLACED, so that शानच् is understood as a\n  substitute. इतरथा हि प्रत्ययान्तरम् एव सर्वविषयं विज्ञायेत —\n  otherwise it would have read as another affix altogether, good\n  everywhere. The wording chosen to fix how the rule is read.',
    '3.1.84': "SETTLED — छन्दसि शायजपि: गृभाय जिह्वया मधु. शानचपि, so both\n  substitutes stand in the Veda — बधान देव. The अपि adds this\n  one beside 3.1.83's rather than replacing it.",
    '3.1.85': 'SETTLED — व्यत्ययो बहुलम्. व्यतिगमनं व्यत्ययो व्यतिहारः: in the\n  Veda the class-markers are interchanged — भेदति where भिनत्ति\n  was due, मरन्ति where म्रियन्ते. And the vṛtti sorts the kinds:\n  विषयान्तरे विधानम्, क्वचिद् द्विविकरणता, क्वचित् त्रिविकरणता —\n  one marker for another, sometimes two at once, sometimes three.\n\nSETTLED — बहुलग्रहणं सर्वविधिव्यभिचारार्थम्, and a verse the\n  vṛtti quotes extends it far past the विकरणs — to case and\n  finite endings, voice, gender, person, tense, sounds, accent,\n  agent and यङ्. This is a licence and not a rule with an output:\n  nothing here can be derived, only recognised, and it is\n  codified as such rather than given a form to produce.',
    '3.1.86': "SETTLED — लिङ्याशिष्यङ्, शपोऽपवादः: उपस्थेयम्, गमेम, वोचेम,\n  विदेयम्, शकेयम्, आरुहेयम् — in the Veda, before a benedictive\n  लिङ्. A vārttika adds दृश्: दृशेयम्.\n\nSETTLED — and the rule needs 3.4.117 छन्दस्युभयथा to work at all:\n  that gives the Vedic लिङ् the name सार्वधातुक as well, and\n  without it no विकरण could stand before it. Recorded because the\n  dependency is not visible in this sūtra's own words.",
    '3.1.87': "SETTLED — कर्मवत् कर्मणा तुल्यक्रियः. कर्मस्थया क्रियया\n  तुल्यक्रियः कर्ता कर्मवद् भवति: where the agent's action is\n  like the object's — the wood as good as splitting itself — the\n  agent takes what belongs to an object,\n  कर्माश्रयाणि कार्याणि प्रतिपद्यते.\n\nSETTLED — and the vṛtti NAMES what follows rather than leaving\n  'treated as an object' to be worked out:\n  यगात्मनेपदचिण्चिण्वद्भावाः प्रयोजनम् — four things. भिद्यते\n  काष्ठं स्वयमेव, अभेदि काष्ठं स्वयमेव, कारिष्यते कटः स्वयमेव.\n  Three of the four are rules of the run just codified, 3.1.62 to\n  3.1.67, so this is where that section is put to work.\n\nSETTLED — वत्करणं स्वाश्रयम् अपि यथा स्यात्: the वत् is there so\n  the transfer also reaches what belongs to the agent in its own\n  right — भिद्यते कुसूलेन. A comparison-word doing more than\n  comparing.\n\nSETTLED — कर्तरि from 3.1.68 is carried down and re-cased:\n  कर्तृग्रहणम् इह अनुवृत्तं प्रथमया विपरिणम्यते. What was a\n  locative there is a nominative here, which is what makes the\n  agent the SUBJECT of this rule rather than its condition.",
    '3.1.88': 'SETTLED — तपस्तपःकर्मकस्यैव: तप्यते तपस्तापसः, अतप्त तपस्तापसः.\n  तपःकर्मकस्यैवेति किम्? उत्तपति सुवर्णं सुवर्णकारः.\n\nSETTLED — पूर्वेणाप्राप्तः कर्मवद्भावो विधीयते: 3.1.87 could not\n  have reached it, so this GRANTS rather than restricts, despite\n  the एव. And the vṛtti explains why by separating two acts:\n  क्रियाभेदाद् विध्यर्थम् एतत् — austerities torment the ascetic,\n  and the ascetic performs them. One root, two directions.',
    '3.1.89': "SETTLED — न दुहस्नुनमां यक्चिणौ: दुग्धे गौः स्वयमेव, प्रस्नुते\n  गौः स्वयमेव, नमते दण्डः स्वयमेव. Two of कर्मवद्भाव's four\n  effects are refused; the middle endings and चिण्वद्भाव stand.\n\nSETTLED — and only ONE is newly refused for दुह्: दुहेरनेन यक्\n  प्रतिषिध्यते, चिण् तु 3.1.63 दुहश्च इति पूर्वम् एव विभाषितः —\n  its चिण् was already a choice, so the prohibition adds nothing\n  there. A rule whose reach differs root by root because of what\n  an earlier rule had already done.\n\nSCOPE — a vārttika adds णि-stems, श्रन्थ्, ग्रन्थ्, ब्रू, and\n  middle and intransitive roots to the prohibition, with a form\n  apiece. Recorded, not modelled.",
    '3.1.90': "SETTLED — कुषिरजोः प्राचां श्यन् परस्मैपदं च: कुष्यति पादः\n  स्वयमेव, रज्यति वस्त्रं स्वयमेव. यगात्मनेपदयोरपवादौ — श्यन् in\n  place of the यक् 3.1.67 would have given, and the ACTIVE in\n  place of the middle: two of कर्मवद्भाव's four effects displaced\n  at once.\n\nSETTLED — प्राचांग्रहणं विकल्पार्थम्: naming the eastern teachers\n  is how the option is expressed. And it is a व्यवस्थितविभाषा —\n  settled by where one is rather than chosen: तेन लिट्लिङोः\n  स्यादिविषये च न भवतः. चुकुषे, कोषिषीष्ट, कोषिष्यते keep the\n  middle. The third व्यवस्थितविभाषा this project has met, after\n  3.1.11 and 2.1.11's bounded विभाषा.",
    '3.1.91': "SETTLED — धातोः is an अधिकार to the end of adhyāya 3: आ\n  तृतीयाध्यायपरिसमाप्तेः. Everything enumerated from here is added\n  after a ROOT.\n\nSETTLED — the vṛtti raises the objection that the word is\n  redundant, 3.1.22's धातोः being still in force —\n  धातुग्रहणम् अनर्थकम्, यङ्विधौ धात्वधिकारात् — and answers it\n  twice. कृदुपपदसंज्ञार्थं तर्हि: the heading is needed so that\n  3.1.92's उपपद and 3.1.93's कृत् hold HERE and not earlier.\n  And आर्धधातुकसंज्ञार्थं च द्वितीयं धातुग्रहणं कर्तव्यम् — a\n  second धातोः is wanted so 3.4.114's आर्धधातुक reaches what is\n  prescribed after a root and not after a stem: इह मा भूत्\n  लूभ्यां लूभिः. A word defended by naming what would go wrong.",
    '3.1.92': 'SETTLED — तत्रोपपदं सप्तमीस्थम्: what a rule of this section\n  states in the LOCATIVE is called उपपद, a word that must stand\n  beside. 3.2.1 कर्मण्यण् states कर्मणि so, and कुम्भकारः is\n  formed.\n\nSETTLED — स्थग्रहणं सूत्रेषु सप्तमीनिर्देशप्रतिपत्त्यर्थम्:\n  without स्थ the name would attach only where a locative is\n  actually heard, and rules carrying one down by anuvṛtti would\n  be left out — स्तम्बेरमः, कर्णेजपः. स्थग्रहणात्तु सर्वत्र भवति.\n\nSETTLED — and the name is अन्वर्थ, read for what it means:\n  गुरुसंज्ञाकरणम् अन्वर्थसंज्ञाविज्ञाने सति\n  समर्थपरिभाषाव्यापारार्थम् — a heavy name is chosen so that\n  2.1.1 समर्थः पदविधिः has something to act on, and पश्य कुम्भम्,\n  करोति कटम् get no affix. 2.1.1 is codified, and this is the\n  second time this project has met a rule written so that it\n  could reach.',
    '3.1.93': 'SETTLED — कृदतिङ्: in the धातोः section an affix that is not a\n  तिङ् bears the name कृत् — कर्तव्यम्, करणीयम्. अतिङिति किम्?\n  चीयात्, स्तूयात्, which are तिङ् endings and keep the name\n  1.4.104 gives them.\n\nSETTLED — कृत्प्रदेशाः: where the name is used, beginning with\n  1.2.46 कृत्तद्धितसमासाश्च, which is codified. That rule is what\n  makes a कृत्-final word a प्रातिपदिक, so this name is how the\n  whole of adhyāya 3 hands its output to the nominal system.\n\nSETTLED — and it opens the कृत्य section: 3.1.95 कृत्याः is the\n  next heading, with 3.1.94 वाऽसरूपोऽस्त्रियाम् between them,\n  reached ahead long ago.',
}

#: Six questions across this run. 3.1.69 to 3.1.84 add a marker,
#: 3.1.85 and 3.1.86 are what the Veda does with them, 3.1.87 to
#: 3.1.90 transfer an agent's treatment, and the last three are
#: headings that each confer a different name.
_KRTYA = ("krtya(affix=..., sutra_id=...) -> whether the name "
          "कृत्य reaches it, and by which rule.")
_ENTRY = {"3.1.85": (vedic_latitude, _VEDIC),
          "3.1.95": (krtya, _KRTYA),
          "3.1.86": (vedic_latitude, _VEDIC),
          "3.1.91": (dhatoh_heading, _DHATOH),
          "3.1.92": (upapada, _UPAPADA),
          "3.1.93": (krt, _KRT)}
_KARMAVAT_RULES = ("3.1.87", "3.1.88", "3.1.89", "3.1.90")

for _sutra, _notes in _MARKERS.items():
    if _sutra in _ENTRY:
        _apply, _line = _ENTRY[_sutra]
    elif _sutra in _KARMAVAT_RULES:
        _apply, _line = karmavat, _KARMAVAT
    else:
        _apply, _line = vikarana, _VIKARANA
    register(
        _sutra,
        apply=_apply,
        codification=_line,
        notes=_notes,
        # Which class a root is read in is a corpus question, and
        # `verbal_gana` is how it is asked — the same helper 2.4.72 and
        # 3.1.25 use. That is corpus access, not one rule running
        # another. 3.1.79's restriction of 2.4.79 and 3.1.87's four
        # effects are dependencies in the grammar that this run states
        # rather than runs.
        #
        # 3.1.83 is different: हलः is a pratyāhāra, and 1.1.71
        # आदिरन्त्येन सहेता is what makes a pratyāhāra denote anything.
        # A hand-written vowel list stood here until it was replaced by
        # asking that rule, so the call is real and is declared.
        reuses=(("1.1.71",) if _sutra == "3.1.83" else ()),
    )

# -------------------------------------------------------------------------
# 3.1.96 to 3.1.132 — the कृत्य affixes, and the forms fixed
# among them.
# -------------------------------------------------------------------------

_KRTYA_LINE = (
    'krtya_affix(root, ends_in=..., sense=...) -> which कृत्य affix '
    'is added, and by which rule.'
)
_NIPATANA_KRTYA = (
    'nipatana(sutra_id) -> the forms a निपातन rule of this run fixes '
    'whole, and in what sense.'
)

_KRTYA_RULES = {
    '3.1.96': 'SETTLED — तव्यत्तव्यानीयरः: कर्तव्यम्, करणीयम्. Three affixes at\n  once, after ANY root, and every rule of the run after this cuts\n  into its ground. तकाररेफौ स्वरार्थौ — the त् and र् for the\n  accent, which is the only difference between तव्यत् and तव्य.\n\nSCOPE — three vārttikas: वसेस्तव्यत् कर्तरि णिच्च (वास्तव्यः),\n  केलिमर उपसंख्यानम् (पचेलिमा माषाः, भिदेलिमानि काष्ठानि), and\n  कर्मकर्तरि चायम् इष्यते. The Nyāsa at 3.1.95 argues the second\n  is unnecessary if कृत्याः is read as gathering unlisted affixes.',
    '3.1.97': 'SETTLED — अचो यत्: गेयम्, पेयम्, चेयम्, जेयम्.\n\nSETTLED — and the vṛtti asks why अच् is said at all, since 3.1.124\n  gives ण्यत् to consonant-final roots anyway:\n  अज्ग्रहणं किं यावता हलन्ताण् ण्यतं वक्ष्यति? The answer is that\n  it reaches a root which USED to end in a vowel —\n  अजन्तभूतपूर्वादपि यथा स्यात्: दित्स्यम्, धित्स्यम्. A condition\n  stated to catch what a form no longer looks like.\n\nSCOPE — two vārttikas add five roots (तक्यम्, शस्यम्, चत्यम्,\n  यत्यम्, जन्यम्) and give हन् a choice with a वध substitute:\n  वध्यम् beside घात्यम्. Recorded.',
    '3.1.98': 'SETTLED — पोरदुपधात्, ण्यतोऽपवादः: शप्यम्, लभ्यम्. यत् taking\n  ground back from 3.1.124, and the vṛtti names the relation.\n  पोरिति किम्? पाक्यम्, वाक्यम्. अदुपधादिति किम्? कोप्यम्,\n  गोप्यम्.\n\nSETTLED — तपरकरणं तत्कालार्थम्: the अ is written with a त् so\n  that only a SHORT one counts — आप्यम् has a long आ and is out.',
    '3.1.99': 'SETTLED — शकिसहोश्च: शक्यम्, सह्यम्. Both end in consonants and\n  3.1.124 would have given them ण्यत्, so this is the same\n  अपवाद as 3.1.98 — by name this time rather than by shape.',
    '3.1.100': "SETTLED — गदमदचरयमश्चानुपसर्गे: गद्यम्, मद्यम्, चर्यम्, यम्यम्.\n  अनुपसर्ग इति किम्? प्रगाद्यम्, प्रमाद्यम्.\n\nSETTLED — यम् was reachable already, and the vṛtti says what\n  naming it buys: यमेः पूर्वेणैव सिद्धे अनुपसर्गनियमार्थं\n  वचनम् — it is named to be RESTRICTED to preverbless use, not to\n  be given the affix. The same shape as 3.1.79's कृ and 3.1.52's\n  अस्, and the third time in this pāda.\n\nSCOPE — a vārttika gives चर् with आ, of a place but not a teacher:\n  आचर्यो देशः, but आचार्य उपनेता. Recorded.",
    '3.1.101': 'SETTLED — a निपातन of three forms in three senses, यथासंख्यम्:\n  अवद्यं पापम् but अनुद्यम् अन्यत्; पण्यः कम्बलः but पाण्यम्\n  अन्यत्; शतेन वर्या but वृत्या अन्या. Each with its own\n  counter-form, which is how a निपातन shows its bounds.',
    '3.1.102': 'SETTLED — वह्यं करणम्: वहत्यनेनेति वह्यं शकटम्, the cart one is\n  carried by — यत् in the instrument sense. करण इति किम्?\n  वाह्यम् अन्यत्.',
    '3.1.103': 'SETTLED — अर्यः स्वामिवैश्ययोः: अर्यः स्वामी, अर्यो वैश्यः, where\n  ण्यत् was due. स्वामिवैश्ययोरिति किम्? आर्यो ब्राह्मणः — the\n  same root gives a different word in a third sense.\n\nSETTLED — and a vārttika splits the two senses by ACCENT:\n  स्वामिन्यन्तोदात्तत्वं च वक्तव्यम्. 6.1.213 यतोऽनावः would have\n  made both initially accented; the vārttika gives the first a\n  final accent instead, so the two are told apart by nothing but\n  that.',
    '3.1.104': 'SETTLED — उपसर्या काल्या प्रजने: प्राप्तकाला काल्या, ready in\n  season — उपसर्या गौः, उपसर्या वडवा. प्रजनः प्रजननम्,\n  प्रथमगर्भग्रहणम्. काल्या प्रजन इति किम्? उपसार्या शरदि मधुरा.',
    '3.1.105': 'SETTLED — अजर्यं संगतम्: न जीर्यतीत्यजर्यम्, a friendship that\n  does not wear out — अजर्यं नोऽस्तु संगतम्. संगतमिति किम्?\n  अजरिता कम्बलः.',
    '3.1.106': "SETTLED — वदः सुपि क्यप् च: ब्रह्मोद्यम् beside ब्रह्मवद्यम्,\n  सत्योद्यम् beside सत्यवद्यम्. The च adds यत्, so BOTH forms\n  stand — a rule giving two affixes at once, as 3.1.96 does.\n  सुपीति किम्? वाद्यम्. अनुपसर्ग इत्येव: प्रवाद्यम्.\n\nSETTLED — and this is where 3.1.92's उपपद starts doing work: the\n  सुबन्त that must stand beside is named in the locative, which is\n  exactly what that heading calls an उपपद.",
    '3.1.107': 'SETTLED — भुवो भावे: ब्रह्मभूयं गतः, देवभूयं गतः.\n  यत् तु नानुवर्तते — the यत् 3.1.106 added does NOT carry down,\n  so क्यप् alone here. A word from the rule before that is\n  deliberately not inherited.\n\nSETTLED — भावग्रहणम् उत्तरार्थम्: the word भावे is stated for the\n  sake of the rule AFTER this one, not for this one. Recorded\n  because it explains why the condition is worded here at all.',
    '3.1.108': 'SETTLED — हनस्त च: ब्रह्महत्या, अश्वहत्या — क्यप् and a त put at\n  the end. सुपीत्येव: घातः. अनुपसर्ग इत्येव: प्राघातो वर्तते.\n\nSETTLED — and the vṛtti gives an unusual reason why ण्यत् does not\n  step in: ण्यत् तु भावे न भवति अनभिधानात् — not because a rule\n  forbids it but because usage does not have it. A ground of a\n  different kind from the rest of this run, and worth keeping as\n  such rather than reworded into a condition.',
    '3.1.109': "SETTLED — एतिस्तुशास्वृदृजुषः क्यप्: इत्यः, स्तुत्यः, शिष्यः,\n  वृत्यः, आदृत्यः, जुष्यः. सुप्यनुपसर्गे भावे इति निवृत्तम् —\n  the three conditions carried from 3.1.106 stop here,\n  सामान्येन विधानम् एतत्.\n\nSETTLED — क्यप् IS SAID AGAIN THOUGH IT WAS RUNNING, and the\n  vṛtti says why: क्यबिति वर्तमाने पुनः क्यब्ग्रहणं\n  बाधकबाधनार्थम् — to defeat 3.1.125's ण्यत् where the two would\n  meet, अवश्यस्तुत्यः. A rule repeated so that a LATER rule\n  cannot displace it, which is the reverse of the usual reason\n  for repetition, and is why this row is weighted above its\n  conditions in the table.\n\nSETTLED — वृग्रहणे वृञो ग्रहणम् इष्यते, न वृङः: of the two roots\n  written वृ only one is meant. वार्या ऋत्विजः is the other.\n\nSCOPE — a vārttika gives शंस्, दुह् and गुह् a choice: शस्यम्\n  beside शंस्यम्, दुह्यम् beside दोह्यम्. Recorded.",
    '3.1.110': "SETTLED — ऋदुपधाच्चाकॢपिचृतेः: वृत्यम्, वृध्यम्.\n  अक्ऌपिचृतेरिति किम्? कल्प्यम्, चर्त्यम् — two roots with the\n  right shape, excepted by name.\n\nSETTLED — तपरकरणम् keeps it to the SHORT ऋ, so कृत् 'to praise'\n  takes ण्यत् instead: कीर्त्यम्.\n\nSCOPE — two vārttikas give सृज् ण्यत् with पाणि and with समव:\n  पाणिसर्ग्या रज्जुः, समवसर्ग्या. Recorded.",
    '3.1.111': "SETTLED — ई च खनः: खेयम् — क्यप् and an ई put at the end.\n\nSETTLED — दीर्घनिर्देशः प्रश्लेषार्थः: the ई is written LONG so\n  that two are read in it, and the second is there to block\n  6.4.43's आ. A long vowel in a sūtra standing for two, in order\n  to stop a later rule — the same device as 3.1.83's\n  स्थानिनिर्देश, and worth recording because nothing in the\n  surface says so.",
    '3.1.112': 'SETTLED — भृञोऽसंज्ञायाम्: भृत्याः कर्मकराः, those to be\n  maintained — भर्तव्या इत्यर्थः. असंज्ञायामिति किम्? भार्यो नाम\n  क्षत्रियः.\n\nSCOPE — a vārttika makes it a choice with सम्: संभृत्याः beside\n  संभार्याः. And two verse-vārttikas work out how भार्या is\n  reached in the feminine despite the प्रतिषेध, by the भाव\n  heading. Recorded, not modelled.',
    '3.1.113': 'SETTLED — मृजेर्विभाषा: परिमृज्यः beside परिमार्ग्यः.\n  ऋदुपधत्वात् प्राप्तविभाषेयम् — 3.1.110 had already reached मृज्\n  by its ऋ penult, so this is an option laid over something\n  already available. The second प्राप्तविभाषा in this adhyāya,\n  after 3.1.62.',
    '3.1.114': 'SETTLED — a निपातन of seven forms under क्यप्, each suspending\n  something different: a उत्व for one, a रुट् augment for another,\n  a कुत्व for a third. राजसूयः क्रतुः, सूर्यः, मृषोद्यम्, रुच्यः,\n  कुप्यम्, कृष्टपच्यम्, अव्यथ्यम्.\n  मृषापूर्वस्य वदतेः पक्षे यति प्राप्ते नित्यं क्यब् निपात्यते —\n  one of the seven is fixed precisely to remove a choice.',
    '3.1.115': 'SETTLED — भिद्योद्ध्यौ नदे: भिनत्ति कूलं भिद्यः, उज्झत्युदकम्\n  उद्ध्यः, the second with a धत्व. नद इति किम्? भेत्ता, उज्झिता.',
    '3.1.116': 'SETTLED — पुष्यसिद्ध्यौ नक्षत्रे: पुष्यन्त्यस्मिन्नर्था इति\n  पुष्यः — and in the LOCATIVE sense, which is what makes them\n  names of lunar mansions. नक्षत्र इति किम्? पोषणम्, सेधनम्.',
    '3.1.117': 'SETTLED — विपूयविनीयजित्या मुञ्जकल्कहलिषु, यथासंख्यम्: विपूयो\n  मुञ्जः but विपव्यम् अन्यत्; विनीयः कल्कः; जित्यो हलिः. In the\n  OBJECT sense, where यत् was due.',
    '3.1.118': 'SETTLED — प्रत्यपिभ्यां ग्रहेश्छन्दसि: प्रतिगृह्यम्, अपिगृह्यम्.\n  छन्दसीति किम्? प्रतिग्राह्यम्, अपिग्राह्यम् — outside the Veda\n  the ण्यत् comes instead.',
    '3.1.119': "SETTLED — पदास्वैरिबाह्यापक्ष्येषु च: प्रगृह्यं पदम्, गृह्यका\n  इमे, ग्रामगृह्या सेना. Four senses, and the vṛtti glosses each\n  — अस्वैरी परतन्त्रः, one not his own master; बाह्या is what\n  lies outside a village or town.\n\nSETTLED — स्त्रीलिङ्गनिर्देशाद् अन्यत्र न भवति: one of the four is\n  written in the feminine, and that wording confines it. A\n  gender in a sūtra acting as a condition, as at 3.1.101's वर्या.",
    '3.1.120': 'SETTLED — विभाषा कृवृषोः: कृत्यम् beside कार्यम्, वृष्यम् beside\n  वर्ष्यम्.\n\nSETTLED — and the two are reached from OPPOSITE sides, which the\n  vṛtti sets out: करोतेर्ण्यति प्राप्ते, वर्षतेर् ऋदुपधत्वाद्\n  नित्ये क्यपि प्राप्ते विभाषारभ्यते — for कृ the option opens\n  against ण्यत्, for वृष् against an obligatory क्यप्. One\n  विभाषा doing two different jobs, as 2.4.78 did.',
    '3.1.121': 'SETTLED — युग्यं च पत्रे: पतत्यनेनेति पत्रम्, a draught animal —\n  युग्यो गौः, युग्यो अश्वः, with a कुत्व. पत्र इति किम्? योग्यम्\n  अन्यत्.',
    '3.1.122': "SETTLED — अमावस्यदन्यतरस्याम्: अमावास्या beside अमावस्या, the\n  new-moon day — सह वसतोऽस्मिन् काले सूर्यचन्द्रमसौ. अमा means\n  'together', and the affix is ण्यत् in the locative sense of\n  time.\n\nSETTLED — the option is NOT about the affix but about the\n  strengthening: तत्रान्यतरस्यां वृद्ध्यभावो निपात्यते. And the\n  vṛtti draws a consequence — एकदेशविकृतस्यानन्यत्वात्, a thing\n  altered in one part is not another thing, so 4.3.30's\n  अमावास्याया वा reaches the shorter form as well.",
    '3.1.123': 'SETTLED — a निपातन of eighteen Vedic forms at once, and the vṛtti\n  states the principle rather than deriving them:\n  यदिह लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम् — whatever the\n  rules do not reach, the fixing supplies. It then works several\n  out anyway, naming what each suspends: a आद्यन्तविपर्यय for the\n  first, a षत्व, a दीर्घ with no तुक् for the second.',
    '3.1.124': "SETTLED — ऋहलोर्ण्यत्: कार्यम्, हार्यम्, धार्यम्; वाक्यम्,\n  पाक्यम्. पञ्चम्यर्थे षष्ठी — the genitive read as an ablative,\n  'after a root ending in ऋ or in a consonant'.\n\nSETTLED — and this is the rule 3.1.98, 3.1.99 and 3.1.103 were\n  each taking ground from. It is stated late though it is the\n  general one, which is why those three could be written as\n  अपवाद before it was given.",
    '3.1.125': "SETTLED — ओरावश्यके, यतोऽपवादः: लाव्यम्, पाव्यम्.\n  अवश्यंभाव आवश्यकम्, what must be done. आवश्यक इति किम्? लव्यम्.\n  Here ण्यत् takes ground BACK from 3.1.97, so the two affixes cut\n  across each other in both directions.\n\nSETTLED — the vṛtti raises an objection against reading आवश्यक as\n  a मात्र meaning — आवश्यके द्योत्ये इति चेत् स्वरसमासानुपपत्तिः,\n  the accent and the compound of अवश्यलाव्यम् would not come out —\n  and answers it from 2.1.72's मयूरव्यंसकादि, which is codified.",
    '3.1.126': 'SETTLED — आसुयुवपिरपिलपित्रपिचमश्च, यतोऽपवादः: आसाव्यम् from आ +\n  सु, then याव्यम्, वाप्यम्, राप्यम्, लाप्यम्, त्राप्यम्,\n  आचाम्यम्. अनुक्तसमुच्चयार्थश्चकारः, and the vṛtti adds दभ् on\n  that च: दाभ्यम्.',
    '3.1.127': "SETTLED — आनाय्योऽनित्ये: आनाय्यो दक्षिणाग्निः, with ण्यत् and an\n  आय substitute. रूढिरेषा — the form is fixed to ONE fire and not\n  to the kind, and the vṛtti works out which: the one brought from\n  the गार्हपत्य and sharing a source with the आहवनीय, since only\n  that one's source is variable.",
    '3.1.128': 'SETTLED — प्रणाय्योऽसंमतौ: प्रणाय्यश्चोरः, one held in no regard.\n  संमननं संमतिः, संमतता पूजा. असंमताविति किम्? प्रणेयोऽन्यः.\n\nSETTLED — and the vṛtti meets a scriptural counter-example head\n  on: a passage uses प्रणाय्य of a pupil one WOULD teach, which\n  looks like the opposite sense. It answers by taking संमति as\n  desire — निष्कामतया असंमतिः, one without wants. A commentary\n  defending a rule against a text rather than the other way\n  round, and recorded as such.',
    '3.1.129': 'SETTLED — पाय्यसान्नाय्यनिकाय्यधाय्या\n  मानहविर्निवाससामिधेनीषु, यथासंख्यम्: पाय्यं मानम् but मेयम्\n  अन्यत्; सान्नाय्यं हविः but सन्नेयम् अन्यत्. Four forms, four\n  senses, and each with its own counter.',
    '3.1.130': 'SETTLED — क्रतौ कुण्डपाय्यसंचाय्यौ: कुण्डेन पीयतेऽस्मिन् सोम इति\n  कुण्डपाय्यः क्रतुः — in the locative sense, with a युक्, and a\n  तृतीयान्त उपपद. संचाय्यः likewise, with ण्यत् and an आय.',
    '3.1.131': 'SETTLED — अग्नौ परिचाय्योपचाय्यसमूह्याः: the first two with ण्यत्\n  and an आय substitute, the third with संप्रसारण and a long vowel.\n  अग्नाविति किम्? परिचेयम्, उपचेयम्, संवाह्यम् — three forms and\n  three different counters.',
    '3.1.132': "SETTLED — चित्याग्निचित्ये च: चीयतेऽसौ चित्योऽग्निः; and\n  अग्निचयनम् एव अग्निचित्या, the second in the भाव sense with a य\n  and a तुक्, तेनान्तोदात्तत्वं भवति — which is what gives it a\n  final accent. अग्नावित्येव: चेयम् अन्यत्.\n\nSETTLED — and this closes 3.1.95's heading. 3.1.133 ण्वुल्तृचौ is\n  the rule that heading was defined by stopping before.",
}

#: Seventeen of the thirty-seven fix forms rather than adding an
#: affix, and answer through their own entry point. A निपातन is by
#: definition what the rules do not reach, so a table that tried to
#: derive them would be pretending.
_KRTYA_NIPATANA = tuple(sorted(_krtya_nipatana))

#: What each shape-rule asks, now that it asks instead of
#: restating. 3.1.98 turns on both a वर्ग and a penult.
_KRTYA_REUSES = {
    "3.1.97": ("1.1.71",),
    "3.1.98": ("1.1.69", "1.1.65"),
    "3.1.110": ("1.1.65",),
    "3.1.124": ("1.1.71",),
    "3.1.125": ("1.1.71",),
}

for _sutra, _notes in _KRTYA_RULES.items():
    if _sutra in _KRTYA_NIPATANA:
        _apply, _line = krtya_nipatana, _NIPATANA_KRTYA
    else:
        _apply, _line = krtya_affix, _KRTYA_LINE
    register(
        _sutra,
        apply=_apply,
        codification=_line,
        notes=_notes,
        # The अपवाद chain among यत्, क्यप् and ण्यत् is precedence,
        # which the specificity ranking expresses, and 3.1.109's
        # बाधकबाधन is a weight on one row — neither is one rule running
        # another's code.
        #
        # But the SHAPES these rules turn on are decided elsewhere and
        # are now asked rather than restated, so those calls are
        # declared. 1.1.71 for अच् and हल्, which are pratyāhāras;
        # 1.1.69 अणुदित्सवर्णस्य for 3.1.98's पु, which is not one but
        # a वर्ग reached through savarṇatva; 1.1.65 अलोऽन्त्यात्पूर्व
        # उपधा for the penultimate two rules turn on.
        reuses=_KRTYA_REUSES.get(_sutra, ()),
    )

# -------------------------------------------------------------------------
# 3.1.133 to 3.1.150 — the agent affixes, and the close.
# -------------------------------------------------------------------------

_AGENT_LINE = (
    'agent_affix(root, upasarga=..., sense=...) -> which agent affix '
    'is added, and by which rule.'
)

_AGENT_RULES = {
    '3.1.133': "SETTLED — ण्वुल्तृचौ: कारकः and कर्ता, हारकः and हर्ता.\n  सर्वधातुभ्यः — after EVERY root, so this is the widest rule of\n  the run and everything after it is an अपवाद. It is also the\n  rule 3.1.95's कृत्य heading was defined by stopping before.\n\nSETTLED — चकारः सामान्यग्रहणार्थः: the च is there so that तृ can\n  be named in general later, at 5.3.59 तुश्छन्दसि and 6.4.154\n  तुरिष्ठेमेयस्सु. A mark in one rule written for the sake of two\n  others three adhyāyas away.",
    '3.1.135': "SETTLED — इगुपधज्ञाप्रीकिरः कः: विक्षिपः, विलिखः, बुधः, कृशः;\n  and the three named roots ज्ञः, प्रियः, किरः.\n\nSETTLED — इगुपध is not restated here. It is two codified rules\n  together — 1.1.65 अलोऽन्त्यात्पूर्व उपधा for WHICH sound is the\n  penultimate, and the pratyāhāra इक् for whether it falls in that\n  span — so both are asked. The Kāśikā's own four examples come\n  out right, and पच् falls outside.\n  And the same asking explains why three roots have to be NAMED:\n  ज्ञा's penult is ञ्, no इक् at all.",
    '3.1.136': "SETTLED — आतश्चोपसर्गे: प्रस्थः, सुग्लः, सुम्लः. णस्यापवादः — an\n  exception to the ण that 3.1.141 gives every आ-final root.\n\nSETTLED — whether a preverb is present is 1.4.59 उपसर्गाः\n  क्रियायोगे's question, and that rule is codified, so it is\n  asked. Five rules of this run turn on it — three wanting one,\n  two refusing one — and a hand-kept list of the twenty-two would\n  have to be corrected in two places.",
    '3.1.137': 'SETTLED — पाघ्राध्माधेट्दृशः शः: उत्पिबः, उज्जिघ्रः, उद्धमः,\n  उद्धयः, उत्पश्यः.\n\nSETTLED — उपसर्ग इति केचिन् नानुवर्तयन्ति: some teachers do not\n  carry the preverb down and read पश्यः on its own. Recorded as a\n  reading the vṛtti reports rather than one it settles.\n  A vārttika keeps a name out: व्याघ्रः.',
    '3.1.138': 'SETTLED — अनुपसर्गाल्लिम्पविन्दधारिपारिवेद्युदेजिचेतिसातिसाहिभ्यश्च:\n  लिम्पः, विन्दः, धारयः, पारयः, वेदयः. अनुपसर्गादिति किम्?\n  प्रलिपः. सातिः सौत्रो धातुः, one the sūtra supplies itself.\n\nSCOPE — two vārttikas keep proper names: नौ लिम्पेः gives\n  निलिम्पा नाम देवाः, and गवादिषु विन्देः संज्ञायाम् gives\n  गोविन्दः, अरविन्दः. Recorded.',
    '3.1.139': 'SETTLED — ददातिदधात्योर्विभाषा: ददः beside दायः, दधः beside\n  धायः. णस्यापवादः. अनुपसर्गादित्येव: प्रदः, प्रधः.',
    '3.1.140': "SETTLED — ज्वलितिकसन्तेभ्यो णः: ज्वालः beside ज्वलः, चालः beside\n  चलः. अचोऽपवादः. इतिशब्द आद्यर्थः. अनुपसर्गादित्येव: प्रज्वलः.\n\nSETTLED — THE GAṆA IS A STRETCH, NOT A LIST. ज्वल इत्येवमादिभ्यः\n  कस इत्येवमन्तेभ्यः — the vṛtti gives it by naming both ends, and\n  the dhātupāṭha reads ज्वल at 01.0916 and कस् at 01.0996 with the\n  vṛtti's own चल at 01.0924 between them. So the bound is read off\n  the corpus by its codes. A copied list would be a second\n  statement of a span the data already holds.\n\nSCOPE — a vārttika adds तन्: अवतानः. Recorded.",
    '3.1.141': "SETTLED — श्यादव्यधास्रुसंस्र्वतीणवसाऽवहृलिहश्लिषश्वसश्च: दायः,\n  धायः, व्याधः, आस्रावः, अत्यायः, अवसायः, अवहारः, लेहः, श्लेषः,\n  श्वासः. अनुपसर्गादिति विभाषेति च निवृत्तम् — both conditions\n  running from the rules before are dropped here.\n\nSETTLED — श्यै IS NAMED THOUGH IT WAS ALREADY REACHED, and the\n  vṛtti says why: आकारान्तत्वादेव श्यायतेः प्रत्यये सिद्धे\n  पुनर्वचनं बाधकबाधनार्थम् — it is आ-final and this rule covers\n  it, so the naming is to DEFEAT 3.1.136's क where a preverb\n  stands: उपसर्गे कं बाधित्वायमेव भवति, अवश्यायः, प्रतिश्यायः.\n  The second rule in this pāda repeated to survive another, after\n  3.1.109 — and codified the same way, as a weight on one row\n  rather than as a condition it does not have.",
    '3.1.142': 'SETTLED — दुन्योरनुपसर्गे: दुनोतीति दावः, नयतीति नायः.\n  अनुपसर्ग इति किम्? प्रदवः, प्रणयः.',
    '3.1.143': "SETTLED — विभाषा ग्रहः: ग्राहः beside ग्रहः. अचोऽपवादः.\n\nSETTLED — व्यवस्थितविभाषा चेयम्, and the vṛtti settles both\n  sides by MEANING rather than leaving a choice: जलचरे नित्यं\n  ग्राहः — of the water-creature always the long form; ज्योतिषि\n  नेष्यते, तत्र ग्रह एव — of the planet only the short one. The\n  fourth व्यवस्थितविभाषा this project has met, after 3.1.11,\n  3.1.90 and 2.1.11's bounded विभाषा.\n\nSCOPE — a vārttika adds भू: भावः beside भवः. Recorded.",
    '3.1.144': 'SETTLED — गेहे कः: गृहं वेश्म, of a house.\n  तात्स्थ्याद् दाराश्च — and by the thing that stands in it the\n  word reaches a household too: गृह्णन्तीति गृहा दाराः. A word\n  extended to what the thing contains, which the vṛtti names as a\n  principle rather than listing the sense separately.',
    '3.1.145': "SETTLED — शिल्पिनि ष्वुन्, of a craftsman.\n\nSETTLED — a vārttika holds it to three roots BY COUNTING them:\n  नृतिखनिरञ्जिभ्यः परिगणनं कर्तव्यम् — नर्तकः, खनकः, रजकः, and\n  their feminines नर्तकी, खनकी, रजकी. परिगणन is the same device\n  as a परिसंख्या: a closed list where the sūtra's own wording\n  would have been open. रञ्जेरनुनासिकलोपश्च gives रजक its shape.",
    '3.1.146': 'SETTLED — गस्थकन्: गाथकः, गाथिका, of one who sings for a living.',
    '3.1.147': 'SETTLED — ण्युट् च: गायनः, गायनी. चकारेण ग इत्यनुकृष्यते — the च\n  drags गै down from the rule before, so one root takes two\n  affixes and both forms stand.\n\nSETTLED — योगविभाग उत्तरार्थः: the split from 3.1.146 is for the\n  rule AFTER, since 3.1.148 needs the ण्युट् and not the थकन्.\n  Codified as one row carrying `also`, since asking either sūtra\n  should show the pair.',
    '3.1.148': 'SETTLED — हश्च व्रीहिकालयोः, and two senses with two derivations:\n  हायना नाम व्रीहयः, जहत्युदकम् इति कृत्वा — the rice that leaves\n  the water behind; and हायनः संवत्सरः, जिहीते भावान् इति कृत्वा —\n  the year that goes.\n\nSETTLED — जहाति and जिहीते are BOTH meant: two roots written\n  alike, and the vṛtti takes one for each sense. Codified as two\n  rows for that reason, as 3.1.25 and 3.1.48 were.',
    '3.1.149': 'SETTLED — प्रुसृल्वः समभिहारे वुन्: प्रवकः, सरकः, लवकः.\n\nSETTLED — समभिहार DOES NOT MEAN HERE WHAT IT MEANT AT 3.1.22.\n  There the vṛtti glossed it पौनःपुन्यं भृशार्थो वा, again and\n  again or intensely. Here: समभिहारग्रहणेनात्र साधुकारित्वं\n  लक्ष्यते, doing a thing WELL — and it draws the consequence\n  out, सकृदपि यः सुष्ठु करोति तत्र भवति, बहुशो यो दुष्टं करोति\n  तत्र न भवति: once done well is enough, often done badly is not.\n  One word, two senses, and the two rules must not share a field\n  — the same care the field-name collisions have needed.',
    '3.1.150': 'SETTLED — आशिषि च: जीवतात् जीवकः, नन्दतात् नन्दकः. धातुमात्रात्,\n  after any root at all, so the pāda closes as it opened at\n  3.1.133 — with a rule that reaches everything.\n\nSETTLED — आशीः प्रार्थनाविशेषः, स चेह क्रियाविषयः: the wish is\n  about the ACT and not the thing — अमुष्याः क्रियायाः कर्ता\n  भवेद् इत्येवम् आशास्यते, may he be the doer of it.\n  This is the last rule of the pāda; the Kāśikā closes here.',
}

#: What each rule of this run asks of a rule already codified.
#: 1.1.65 and 1.1.71 between them give 3.1.135 its इगुपध; 1.4.59 gives
#: the five preverb rules their condition. Both are calls, not
#: citations — the code would be wrong without them.
_AGENT_REUSES = {
    "3.1.135": ("1.1.65", "1.1.71"),
    "3.1.136": ("1.4.59",),
    "3.1.137": ("1.4.59",),
    "3.1.138": ("1.4.59",),
    "3.1.140": ("1.4.59",),
    "3.1.142": ("1.4.59",),
}

for _sutra, _notes in _AGENT_RULES.items():
    register(
        _sutra,
        apply=agent_affix,
        codification=_AGENT_LINE,
        notes=_notes,
        reuses=_AGENT_REUSES.get(_sutra, ()),
    )
