# -*- coding: utf-8 -*-
"""अध्याय २, पाद १ — the compound section opens, 2.1.1 to 2.1.29."""

from __future__ import annotations

from src.astadhyayi.paribhasa import samartha
from src.astadhyayi.samasa import PROVISIONS, dvigu, saha_supa, samasa_of
from src.astadhyayi.samasa import names_of as samasa_names_of
from src.astadhyayi.sources import register
from src.astadhyayi.svara import parangavat



register(
    '2.1.1',
    apply=samartha,
    codification=(
        'samartha(connected=..., padavidhi=...) -> whether a rule about words reaches this pair of them.'
    ),
    notes=(
        'SETTLED — परिभाषेयम्, and the widest one outside adhyāya 1: यः\n'
        '  कश्चिद् इह शास्त्रे पदविधिः श्रूयते स सर्वः समर्थो वेदितव्यः.\n'
        '  Every rule about words in the whole grammar is read with this\n'
        '  condition attached.\n'
        '\n'
        'SETTLED — समर्थ is glossed twice over and the Kāśikā offers both\n'
        '  without choosing. समर्थः शक्तः — able to convey what the\n'
        '  analytic phrase conveys. Or, as a bahuvrīhi: समर्थानां पदानां\n'
        '  सम्बद्धार्थानां संसृष्टार्थानां विधिः, a rule about words that\n'
        '  are themselves connected in sense.\n'
        '\n'
        'SETTLED — six counter-examples in the Kāśikā, one per compound\n'
        '  rule, and all of the same shape: two words adjacent across a\n'
        '  break with no relation between them. कष्टं श्रितः compounds;\n'
        '  पश्य देवदत्त कष्टम्, श्रितो विष्णुमित्रो गुरुकुलम् does not.\n'
        '\n'
        'SETTLED — and पद is in the sūtra for a reason: पदग्रहणं किम्?\n'
        '  वर्णविधौ समर्थपरिभाषा मा भूत्. The condition reaches no\n'
        '  operation on sounds, so the yaṇ of तिष्ठतु दध्यशान and the tuk\n'
        '  of तिष्ठतु कुमारीच्छत्रम् happen between words with nothing to\n'
        '  do with each other. That limit is codified.\n'
        '\n'
        'SCOPE — whether two words are connected in sense is a fact about\n'
        '  the utterance and not about the forms, so it is an input. With\n'
        '  it unstated the codification withholds the rule rather than\n'
        '  guessing.'
    ),
)


# ---------------------------------------------------------------------------
# 2.1.2 — an atideśa that is not about compounds at all
# ---------------------------------------------------------------------------


register(
    '2.1.2',
    apply=parangavat,
    codification=(
        'parangavat(preceding_is_sup=..., following_is_amantrita=..., '
        'operation=...) -> whether the subanta counts as a limb of the '
        'vocative after it.'
    ),
    notes=(
        'SETTLED — तादात्म्यातिदेशोऽयम्, and the Kāśikā puts it more\n'
        '  strongly than "as if": सुबन्तम् आमन्त्रितम् अनुप्रविशति, the\n'
        '  subanta enters into the vocative. What it is for is 6.1.198\n'
        '  आमन्त्रितस्य च, which makes a vocative initially udātta — the\n'
        '  atideśa carries that back over the preceding word, so\n'
        '  कुण्डेनाटन् and मद्राणां राजन् are accented as one.\n'
        '\n'
        'SETTLED — every word of the sūtra is answered by a किम् in the\n'
        '  Kāśikā, and all six are codified as conditions. The two that\n'
        '  are easy to miss: अङ्गग्रहणं किम्? so that it becomes a *limb*\n'
        '  and not one mass — otherwise both words would take the initial\n'
        '  udātta, यथा मृत्पिण्डीभूतः स्वरं लभेत. And वत्करणं किम्?\n'
        '  स्वाश्रयमपि कार्यं यथा स्यात्, the वत् leaves the word its own\n'
        '  operations besides.\n'
        '\n'
        'SETTLED — स्वर इति किम्? is the limit that makes the rule\n'
        '  codifiable rather than open: the atideśa reaches accent and\n'
        '  nothing else. षत्वणत्वे प्रति पराङ्गवद् न भवति, so कूपे सिञ्चन्\n'
        '  keeps its s against 8.3.59 and चर्म नमन् its n against 8.4.2.\n'
        '  Both refusals are in the code as data, not as prose.\n'
        '\n'
        'SCOPE — five vārttikas stand on this sūtra and none is codified:\n'
        '  षष्ठ्यामन्त्रितकारकवचनम्, the उपसंख्यान for a word in apposition,\n'
        '  पूर्वाङ्गवच्चेति वक्तव्यम् running the atideśa the other way,\n'
        '  अव्ययानां न, and अव्ययीभावस्य त्विष्यते against it. They join the\n'
        '  921.\n'
        '\n'
        'NOTE — the code lives in svara.py, not with the compounds. The\n'
        '  sūtra sits in this pāda but has nothing to do with समास; it is\n'
        '  an accent rule, and it belongs with the accent rules.'
    ),
)


# ---------------------------------------------------------------------------
# 2.1.3 to 2.1.5 — the three headings
# ---------------------------------------------------------------------------


register(
    '2.1.3',
    apply=samasa_names_of,
    codification=(
        'names_of(sutra_id) -> which compound names a rule in this range '
        'confers. A set, not one name.'
    ),
    samjna='समास',
    notes=(
        'SETTLED — an अधिकार over everything to 2.2.38 कडाराः कर्मधारये:\n'
        '  कडारसंशब्दनात् प्राग् यानित ऊर्ध्वम् अनुक्रमिष्यामः, ते\n'
        '  समाससंज्ञा वेदितव्याः.\n'
        '\n'
        'SETTLED — and the Kāśikā says why it is phrased as a range rather\n'
        '  than as a plain saṃjñā: प्राग्वचनं संज्ञासमावेशार्थम्. Without\n'
        '  it 1.4.1 would allow only one name, and the later at that, so\n'
        '  अव्ययीभाव would displace समास outright — leaving समास conferred\n'
        '  on nothing and every rule that says समासे with no reach.\n'
        '\n'
        'SETTLED — this is the fourth device of its kind the codification\n'
        '  has met: 1.4.55 च, 1.4.56 प्राक्, 1.4.60 च, and now this. They\n'
        '  are one device and are one piece of code. The Kāśikā closes\n'
        '  with समासप्रदेशाः — तृतीयासमासे इत्येवमादयः, the places that\n'
        '  use the name, which is what would have had nothing to use.'
    ),
)


register(
    '2.1.4',
    apply=saha_supa,
    codification=(
        'saha_supa(second_is="sup"|"tiṅ", chandas=...) -> what may stand as '
        'the second member, and on whose authority.'
    ),
    notes=(
        'SETTLED — सुप्, सह and सुपा are all three carried down: सुबिति\n'
        '  सहेति सुपेति च त्रयमप्यधिकृतं वेदितव्यम्. Read as one yoga the\n'
        '  rule is that a subanta compounds with a subanta, and that is\n'
        '  the reading every rule of the section is built on.\n'
        '\n'
        'SETTLED — but the Kāśikā splits it: सहग्रहणं योगविभागार्थम्,\n'
        '  तिङापि सह यथा स्यात्. सह standing alone licenses a *tiṅanta* as\n'
        '  second member — अनुव्यचलत्, अनुप्रावर्षत् — which is the one\n'
        '  place in the whole section where the second word is not a noun.\n'
        '\n'
        'SETTLED — the Kaumudī supplies the limit the Kāśikā leaves\n'
        '  implicit, and both halves of its sentence matter:\n'
        '  योगविभागस्य इष्टसिद्ध्यर्थत्वात् — the split is made because it\n'
        '  is wanted, not because the words demand it — and स च छन्दस्येव,\n'
        '  it is Vedic. The codification grants the split only for छन्दस्.\n'
        '\n'
        'SETTLED — and the Kaumudī draws the consequence that makes the\n'
        '  whole section usable downstream: समासत्वात् प्रातिपदिकत्वम्. A\n'
        '  compound is a prātipadika by 1.2.46, so it takes endings again\n'
        '  and can itself be a member of the next compound.\n'
        '\n'
        'SCOPE — one vārttika, इवेन समासो विभक्त्यलोपश्च, uncodified.'
    ),
)


register(
    '2.1.5',
    reuses=('1.4.1', '2.1.1'),
    apply=samasa_of,
    codification=(
        'samasa_of(first, second, sense=..., given=...) -> whether the pair '
        'compounds, under which names, by which rule.'
    ),
    samjna='अव्ययीभाव',
    notes=(
        'SETTLED — a second अधिकार inside the first, running to 2.1.21.\n'
        '  Whatever the rules below confer, they confer अव्ययीभाव.\n'
        '\n'
        'SETTLED — and the Kāśikā reads content out of the name itself:\n'
        '  अन्वर्थसंज्ञा चेयं महती पूर्वपदार्थप्राधान्यम् अव्ययीभावस्य\n'
        '  दर्शयति. The Mahābhāṣya asks the question the length provokes —\n'
        '  किमर्थं महती संज्ञा क्रियते — and the answer is that the name is\n'
        '  not a label but a statement: what the compound means is what its\n'
        '  *first* member means. उपकुम्भम् is a nearness, not a pot. That\n'
        '  is recorded on the name in SAMJNAS and not left in prose,\n'
        '  because it is the whole of what distinguishes this compound from\n'
        '  the तत्पुरुष whose name says the opposite.\n'
        '\n'
        'SETTLED — 1.1.41 अव्ययीभावश्च closes the circle: the compound this\n'
        '  heading names is itself an अव्यय, so 2.4.82 will elide its\n'
        '  ending. The two modules already meet there.'
    ),
)


# ---------------------------------------------------------------------------
# 2.1.6 to 2.1.21 — generated from samasa.PROVISIONS
# ---------------------------------------------------------------------------


_NOTES = {
    '2.1.7': (
        'SETTLED — यथा compounds when similarity is *not* what is meant:\n'
        '  यथावृद्धं ब्राह्मणानामन्त्रयस्व, invite the elders in order of\n'
        '  age. Against it यथा देवदत्तस्तथा यज्ञदत्तः, which stays a\n'
        '  sentence.\n'
        '\n'
        'SETTLED — and the Kāśikā catches that the rule grants nothing:\n'
        '  यथार्थे यद् अव्ययम् इति पूर्वेणैव सिद्धे समासे वचनम् इदम्\n'
        '  सादृश्यप्रतिषेधार्थम्. 2.1.6 already holds both यथा and सादृश्य\n'
        '  in its list of sixteen, so the compound was available; what this\n'
        '  sūtra does is take one sense *away*.\n'
        '\n'
        'SCAR — codified first as an ordinary provision, which made it a\n'
        '  second way to compound and left यथा in the sense of similarity\n'
        '  compounding by 2.1.6 — the exact case the sūtra exists to\n'
        '  forbid. A restating rule that only adds is a restating rule that\n'
        '  does nothing. It now narrows, and the section can refuse.'
    ),
    '2.1.15': (
        'SETTLED — अनु compounds with a word naming a mark when nearness is\n'
        '  meant: समया समीपम्, अनुवनम् अशनिर्गतः. Two counters, one for\n'
        '  each word of the condition: वनं समया has no अनु, and वृक्षम् अनु\n'
        '  विद्योतते विद्युत् has अनु in another sense.\n'
        '\n'
        'SETTLED — like 2.1.7 this restates what 2.1.6 already grants, and\n'
        '  the Kāśikā names a different purpose: इत्येव सिद्धे पुनर्वचनं\n'
        '  विभाषार्थम्. Not to narrow the sense but to move the rule under\n'
        '  2.1.11, so what was obligatory becomes optional. Two sūtras of\n'
        '  the same surface shape doing opposite work, which is why the\n'
        '  table records `restates` rather than merely noting the overlap.'
    ),
    '2.1.17': (
        'SETTLED — तिष्ठद्ग्वादयः समुदाया एव निपात्यन्ते: these are not\n'
        '  made by any rule but given whole, and the name is conferred on a\n'
        '  finished word rather than on a pair to be joined. तिष्ठद्गु is a\n'
        '  time of day — तिष्ठन्ति गावो यस्मिन् काले दोहनाय.\n'
        '\n'
        'SETTLED — the च is अवधारणार्थ and shuts the list: अपरः समासो न\n'
        '  भवति, so no परमतिष्ठद्गु. A closed gaṇa, unusually.\n'
        '\n'
        'NOTE — the 34 members are read from the gaṇapāṭha, not typed here.\n'
        '  The reader that fetches them was lifted out of nipata.py so that\n'
        '  both sections use one.'
    ),
    '2.1.18': (
        'SETTLED — पारे and मध्ये with a sixth case: पारेगङ्गम्,\n'
        '  मध्येगङ्गम्.\n'
        '\n'
        'SETTLED — it is an अपवाद with its own escape. षष्ठीसमासे प्राप्ते\n'
        '  तदपवादः अव्ययीभाव आरभ्यते: the genitive tatpuruṣa was already\n'
        '  available and this displaces it — but वावचनात् षष्ठीसमासोऽपि\n'
        '  पक्षे अभ्यनुज्ञायते, the वा admits it back, so गङ्गापारम् stands\n'
        '  beside पारेगङ्गम्.\n'
        '\n'
        'SETTLED — and the ए is not a case-ending but निपातित along with\n'
        '  the rule: तत्सन्नियोगेन चानयोः एकारान्तत्वं निपात्यते. पारे here\n'
        '  is not a locative; it is how the word is given.'
    ),
    '2.1.21': (
        'SETTLED — a river-name with a word, for a third thing\'s sake,\n'
        '  when the whole is a proper name: उन्मत्तगङ्गं नाम देशः, the\n'
        '  country called Mad-Ganges — neither the madness nor the river\n'
        '  but the place. Two counters, one per condition: कृष्णवेण्णा has\n'
        '  no third thing, and शीघ्रगङ्गो देशः is a description rather\n'
        '  than a name.\n'
        '\n'
        'SETTLED — and it escapes the heading it stands under:\n'
        '  विभाषाधिकारेऽपि नित्यसमास एव अयम्, नहि वाक्येन संज्ञा गम्यते.\n'
        '  A name is not conveyed by a phrase, so where 2.1.11 would offer\n'
        '  the analytic alternative there is no alternative to offer. This\n'
        '  is the one provision in the table that sets `nitya`, and it sets\n'
        '  it for a reason the commentary states rather than for tidiness.'
    ),
}


def _note(sutra, provisions):
    if sutra in _NOTES:
        return _NOTES[sutra]
    first = provisions[0]
    note = 'SETTLED — ' + first.gloss
    if not note.endswith('.'):
        note += '.'
    worked = [p.example for p in provisions if p.example]
    against = [p.counter for p in provisions if p.counter]
    if worked:
        note += ' Worked as ' + '; '.join(dict.fromkeys(worked)) + '.'
    if against:
        note += ' Against it: ' + '; '.join(dict.fromkeys(against)) + '.'
    if first.optional:
        note += (' Optional, and not by its own word — 2.1.11 विभाषा is a'
                 ' heading, and this stands under it.')
    return note


register(
    '2.1.11',
    apply=samasa_of,
    codification=(
        'Provision.optional -> read off this heading rather than repeated '
        'on each rule below it.'
    ),
    notes=(
        'SETTLED — विभाषेत्ययमधिकारो वेदितव्यः: everything from 2.1.12 on\n'
        '  is optional, so अपत्रिगर्तं वृष्टो देवः and अप त्रिगर्तेभ्यः\n'
        '  both stand.\n'
        '\n'
        'NOTE — codified as a property computed from the heading, not as a\n'
        '  flag repeated on ten provisions. The text states it once and the\n'
        '  table reads it once; a repeated flag could disagree with the\n'
        '  heading, and this cannot.\n'
        '\n'
        'SETTLED — 2.1.21 escapes it, and says why. See its note.'
    ),
)


register(
    '2.1.22',
    reuses=('1.4.1', '2.1.1'),
    apply=samasa_of,
    codification=(
        'The तत्पुरुष heading, recorded in samasa.SAMJNAS with the range it '
        'covers and what the name asserts; names_of(sutra) reads it back.'
    ),
    samjna='तत्पुरुष',
    notes=(
        'SETTLED — a heading, running प्राग्बहुव्रीहेः: from here to\n'
        '  2.2.22, whatever the rules below confer, they confer तत्पुरुष.\n'
        '  यानित ऊर्ध्वम् अनुक्रमिष्यामः, तत्पुरुषसंज्ञास्ते वेदितव्याः. It\n'
        '  joins nothing itself; 2.1.24 is the first rule that does.\n'
        '\n'
        'SETTLED — पूर्वाचार्यसंज्ञा चेयं महती. Unlike अव्ययीभाव this name\n'
        '  is not one Pāṇini coined but one he took over whole, and the\n'
        '  Kāśikā says why that matters: तदङ्गीकरणम् उपाधेरपि तदीयस्य\n'
        '  परिग्रहार्थम् — adopting the name adopts the qualification that\n'
        '  came with it, उत्तरपदार्थप्रधानस् तत्पुरुषः. The meaning of the\n'
        '  *latter* member predominates, exactly the opposite of\n'
        '  अव्ययीभाव, and कष्टश्रितः is a person resorted and not a\n'
        '  hardship. Recorded as `pradhana` on the name rather than left\n'
        '  in prose, because it is what tells the two compounds apart.\n'
        '\n'
        'SCAR — resolve() read the pradhāna by asking specifically for the\n'
        '  अव्ययीभाव heading, so every तत्पुरुष verdict would have come\n'
        '  back with an empty one. It now asks whichever heading in force\n'
        '  states a pradhāna, which is the arrangement the two names were\n'
        '  already recorded for.'
    ),
)

register(
    '2.1.23',
    apply=samasa_names_of,
    codification=(
        "names_of('2.1.23') -> {samāsa, tatpuruṣa}, the heading read off "
        "the range. No provision: द्विगु is a name conferred elsewhere, "
        "and this sūtra only adds तत्पुरुष to whatever bears it."
    ),
    samjna='तत्पुरुष',
    notes=(
        'SETTLED — द्विगुश्च: a द्विगु is called तत्पुरुष as well. This\n'
        '  joins no pair; it extends a name to compounds another rule has\n'
        '  already formed.\n'
        '\n'
        'SETTLED — and the Mahābhāṣya gives the reason the extension is\n'
        '  wanted at all: द्विगोस् तत्पुरुषत्वे समासान्ताः प्रयोजनम्. The\n'
        '  समासान्त affixes of 5.4 are prescribed for a तत्पुरुष, so\n'
        '  without this sūtra a द्विगु would not receive them —\n'
        '  पञ्चराजम्, दशराजम्, द्व्यहः, त्र्यहः, पञ्चगवम्, दशगवम्.\n'
        '\n'
        'SETTLED — the compound the name is given to is 2.1.51\n'
        '  तद्धितार्थोत्तरपदसमाहारे च, which IS codified: a numeral with\n'
        '  a word agreeing with it, before a taddhita sense, before a\n'
        '  further member, or where an aggregate is meant. पञ्चपूली,\n'
        '  पञ्चकपालः, पञ्चगवधनः.\n'
        '\n'
        'SCAR — this note said द्विगु is defined at 2.1.52\n'
        '  तद्धितार्थोत्तरपदसमाहारे च, which pairs the right number with\n'
        '  the wrong sūtra. 2.1.51 is that text and forms the compound;\n'
        '  2.1.52 संख्यापूर्वो द्विगुः is what NAMES it. Written from\n'
        '  memory of the tradition rather than from the सूत्रपाठ in\n'
        '  front of me, and it stood until the pāda was read in order.\n'
        '\n'
        'PENDING — 2.1.52 संख्यापूर्वो द्विगुः is not codified, so nothing\n'
        '  yet bears the name द्विगु for this sūtra to extend, and the\n'
        '  समासान्त affixes of 5.4 that the extension exists for are not\n'
        '  codified either. What this registration holds is the\n'
        '  name-extension and its purpose, not a test that any द्विगु\n'
        '  actually receives an affix.'
    ),
)


_grouped = {}
for _provision in PROVISIONS:
    _grouped.setdefault(_provision.sutra, []).append(_provision)

for _sutra in sorted(_grouped, key=lambda s: int(s.rsplit('.', 1)[1])):
    _provisions = _grouped[_sutra]
    register(
        _sutra,
        apply=samasa_of,
        codification=' · '.join(
            dict.fromkeys(p.describe() for p in _provisions)),
        notes=_note(_sutra, _provisions),
    )


__all__ = [
    'samartha',
    'parangavat',
    'saha_supa',
    'samasa_of',
]


register(
    '2.1.52',
    reuses=('1.1.23', '1.4.1', '2.1.1', '2.1.51'),
    apply=dvigu,
    codification=(
        'dvigu(pair) -> the द्विगु name where 2.1.51 formed the compound '
        'and its first member is a numeral, or nothing.'
    ),
    samjna='द्विगु',
    notes=(
        'SETTLED — तद्धितार्थोत्तरपदसमाहारे चेत्यत्र यः संख्यापूर्वः\n'
        '  समासः स द्विगुसंज्ञो भवति: the 2.1.51 compound with a numeral\n'
        '  first bears this further name. तद्धितार्थे पञ्चकपालः,\n'
        '  उत्तरपदे पञ्चनावप्रियः, समाहारे पञ्चपूली.\n'
        '\n'
        'SETTLED — it forms nothing. 2.1.51 makes the compound; this only\n'
        '  names it, and 2.1.23 द्विगुश्च then adds तत्पुरुष on top. Until\n'
        '  this sūtra was codified, 2.1.23 had nothing bearing the name to\n'
        '  reach — a name-extension with no name under it.\n'
        '\n'
        'SETTLED — whether the first member is a numeral is 1.1.23\n'
        '  बहुगणवतुडति संख्या, which is codified, so it is asked rather\n'
        '  than tested here.\n'
        '\n'
        'PENDING — the name is wanted for what other rules do with it, and\n'
        '  none of those is codified: 4.1.21 द्विगोः gives पञ्चपूली its\n'
        '  ङीप्, 4.1.88 द्विगोर्लुगनपत्ये drops the affix of पञ्चकपालः,\n'
        '  5.4.99 नावो द्विगोः supplies the ending of पञ्चनावप्रियः. What\n'
        '  is held here is the name and the reason for it, not any of its\n'
        '  consequences.'
    ),
)


register(
    '2.2.23',
    reuses=('1.4.1', '2.1.1'),
    apply=samasa_of,
    codification=(
        'The बहुव्रीहि heading, recorded in samasa.SAMJNAS with the range '
        'it covers and what the name asserts; names_of(sutra) reads it back.'
    ),
    samjna='बहुव्रीहि',
    notes=(
        'SETTLED — शेषो बहुव्रीहिः, and शेष is defined by what it is NOT:\n'
        '  उपयुक्तादन्यः शेषः। कश्च शेषः? यत्रान्यः समासो नोक्तः —\n'
        '  wherever no other compound has been stated. So the name is the\n'
        '  remainder of the whole section, which is why it can be given\n'
        '  before the rules that form them.\n'
        '\n'
        'SETTLED — शेष इति किम्? उन्मत्तगङ्गम्, लोहितगङ्गम् — 2.1.21 named\n'
        '  those already, so they are not left over and are not बहुव्रीहि.\n'
        '\n'
        'SETTLED — the fourth of the five pradhānas, and the one that is\n'
        '  neither member: 2.2.24 अन्यपदार्थे says the compound means a\n'
        '  THIRD thing. चित्रगुः is a man, not a cow and not a dappling.\n'
        '  With this the table is complete — पूर्वपद for अव्ययीभाव,\n'
        '  उत्तरपद for तत्पुरुष, अन्यपदार्थ for बहुव्रीहि, उभयपदार्थ for\n'
        '  द्वन्द्व.\n'
        '\n'
        'SCOPE — 2.2.30 to 2.2.38 decide which member is spoken FIRST,\n'
        '  which is a question this table does not answer at all: it says\n'
        '  whether a pair compounds and under what name, not what order\n'
        '  the words come out in. Recorded as the next thing to build\n'
        '  rather than half-modelled here.'
    ),
)
