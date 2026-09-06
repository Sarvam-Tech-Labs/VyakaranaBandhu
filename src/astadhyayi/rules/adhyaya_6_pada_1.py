# -*- coding: utf-8 -*-
"""अध्याय ६, पाद १ — the एकादेश, and what sees it."""

from __future__ import annotations

from src.astadhyayi.asiddha import antadivat, ekadesa_visible
from src.astadhyayi.anga import (
    akah_savarne_dirghah, ato_gune, ayadi, dhatvadeh)
from src.astadhyayi.abhyasta import stated
from src.astadhyayi.agama_lopa import operates
from src.astadhyayi.atva import becomes_a
from src.astadhyayi.ekadesa import one_for_both
from src.astadhyayi.pada_svara import accent_of
from src.astadhyayi.prakrtibhava import stands_open
from src.astadhyayi.samhita import joins
from src.astadhyayi.sut import sut_for
from src.astadhyayi.dvirvacana import for_sutra
from src.astadhyayi.samprasarana import vocalises
from src.astadhyayi.sources import register




_DOUBLING = (
    "Runs the whole reduplication and reports for this sūtra alone: the "
    "finished stem, which rule split it, and what each abhyāsa rule "
    "then did to the copy."
)

register(
    '6.1.1',
    reuses=('1.1.71',),
    apply=for_sutra('6.1.1'),
    codification=_DOUBLING,
    notes=(
        'SETTLED — an अधिकार, and the Kāśikā says which three words it\n'
        '  carries: एकाचः, द्वे, प्रथमस्य. Everything from here to the\n'
        '  संप्रसारण rules is read with them. जजागार, पपाच, इयाय, आर.\n'
        '\n'
        'SETTLED — एकाच् is a BAHUVRĪHI here, and the Kāśikā spells the\n'
        '  compound out to make sure: एकोऽच् यस्य सोऽयम् एकाच्, that which\n'
        '  HAS one vowel. 1.1.14 reads the same word the other way, as a\n'
        '  karmadhāraya — it IS one vowel — and proves the difference with\n'
        '  प्राग्नये वाचमीरय, where प्र has one vowel, is not one vowel, and\n'
        '  so is not pragṛhya. Two readings, two tests, and neither\n'
        '  implementation can serve the other rule. Held by a test.\n'
        '\n'
        'SETTLED — प्रथमस्य picks the opening portion, and the portion runs\n'
        '  through the consonants that CLOSE the first syllable but not\n'
        '  through the one that opens the next. मृज्य divides मृज् · य, so\n'
        '  7.4.60 has a ज् to drop; divide it मृ · ज्य and the copy is\n'
        '  already मृ and the error hides on every open-syllable root.'
    ),
)

register(
    '6.1.2',
    reuses=('1.1.71',),
    apply=for_sutra('6.1.2'),
    codification=_DOUBLING,
    notes=(
        'SETTLED — प्रथमद्विर्वचनापवादोऽयम्, an exception to 6.1.1: for a\n'
        '  vowel-initial root it is the SECOND one-vowelled portion that\n'
        '  doubles. अटिटिषति, अशिशिषति, अरिरिषति.\n'
        '\n'
        'SETTLED — and so something stands in FRONT of the copy, which no\n'
        '  consonant-initial root ever produces. अटाट्यते: the अ of अट् is\n'
        '  not part of the copy and does not move, ट्य doubles behind it,\n'
        '  and the first ट्य becomes टा.\n'
        '\n'
        'SCAR — the split was modelled as (abhyāsa, rest), which is right\n'
        '  for every root 3.1.22 admits without its vārttika and so looked\n'
        '  right for as long as only those were tried. There was nowhere to\n'
        '  keep the अ and it was dropped: अटाट्य came out ā.\n'
        '\n'
        'SCOPE — the Kāśikā\'s discussion of स्थानिवद्भाव under this sūtra —\n'
        '  whether the इट् of अरिरिषति counts as a द्विर्वचननिमित्त — is not\n'
        '  modelled. It turns on 1.1.59, which is codified, but the सन्\n'
        '  forms it concerns are not.'
    ),
)

register(
    '6.1.9',
    apply=for_sutra('6.1.9'),
    codification=_DOUBLING,
    notes=(
        'SETTLED — सन्नन्तस्य यङन्तस्य च धातोरवयवस्य द्वे भवतः: after सन्\n'
        '  and after यङ् the root doubles. पिपक्षति, अरिरिषति for the one;\n'
        '  पापच्यते, यायज्यते, अटाट्यते, प्रोर्णोनूयते for the other.\n'
        '\n'
        'SETTLED — धातोरनभ्यासस्य is read down from 6.1.8, and the Kāśikā\n'
        '  presses the second word: अनभ्यासस्येत्येव — जुगुप्सिषते,\n'
        '  लोलूयिषते. A part that is ALREADY a copy does not double again,\n'
        '  which is what stops the rule running away on a यङन्त stem that\n'
        '  then takes सन्.\n'
        '\n'
        'SETTLED — only सन् and यङ् are named here. The लिट् doubling is\n'
        '  6.1.8\'s and the चङ् doubling 6.1.11\'s; neither is codified, so\n'
        '  nothing in this module should be read as reduplicating for them.'
    ),
)

register(
    '6.1.85',
    apply=antadivat,
    codification=(
        'antadivat(varna_vidhi=...) -> what the single substitute counts as.'
    ),
    notes=(
        'SETTLED — an atideśa made necessary by what 6.1.84 does. The\n'
        '  single substitute replaces a *pair* — पूर्वपरसमुदाय एकादेशस्य\n'
        '  स्थानी — and so belongs to neither word on its own; the two\n'
        '  members are its sthānin only by inference, तत्रावयवयोर्\n'
        "  आनुमानिकं स्थानित्वम्, and 1.1.56's sthānivadbhāva does not\n"
        '  reach it. Hence this: it counts as the end of the first and\n'
        '  the beginning of the second.\n'
        '\n'
        'SETTLED — what that buys is stated: ब्रह्मबन्धूः can then be a\n'
        '  prātipadika-final for 4.1.1, and वृक्षौ a sup-final pada for\n'
        '  1.4.14. Both of those saṃjñās are codified.\n'
        '\n'
        'SETTLED — वर्णाश्रयविधाव् अयम् अन्तादिवद्भावो नेष्यते, with\n'
        '  three worked cases: खट्वाभिः keeps its भिस् against 7.1.9,\n'
        '  जुहाव its णल् against 7.1.34, and अस्यै अश्वः its vṛddhi\n'
        '  against 6.1.109.'
    ),
)


register(
    '6.1.86',
    apply=ekadesa_visible,
    codification=(
        'ekadesa_visible(operation) -> whether the single substitute is seen, for that operation.'
    ),
    notes=(
        'SETTLED — and narrowly. The एकादेश is treated as not made for a\n'
        '  ṣatva and for a tuk, and for nothing else; elsewhere 6.1.85\n'
        '  has just made it count as both an end and a beginning, and it\n'
        '  is fully there.'
    ),
)


register(
    '6.1.78',
    reuses=('1.1.71', '1.3.10'),
    apply=ayadi,
    codification=(
        'ayadi(stem, before_vowel=...) -> the stem with एच् replaced, paired '
        'with its substitute by 1.3.10.'
    ),
    related=('1.1.1', '1.1.2', '1.3.10', '6.1.77', '7.3.84'),
    notes=(
        'SETTLED — एचः स्थाने अचि परतः अय् अव् आय् आव् इत्येते आदेशा\n'
        '  यथासंख्यं भवन्ति: चयनम्, लवनम्, चायकः, लावकः. The अचि is read\n'
        '  down from 6.1.77 इको यणचि.\n'
        '\n'
        'SETTLED — and the pairing is 1.3.10 यथासंख्यम् अनुदेशः समानाम्,\n'
        '  which the Kāśikā names in so many words. Four go to four, in\n'
        '  order: ए→अय्, ओ→अव्, ऐ→आय्, औ→आव्. The codification does not\n'
        '  write those four pairs out. It hands both lists to 1.3.10 and\n'
        '  takes what comes back, so the correspondence is derived and would\n'
        '  fail loudly if either list were mis-copied — 1.3.10 refuses lists\n'
        '  of unequal length rather than pairing what it can.\n'
        '\n'
        'SETTLED — this is the rule that finishes जयति. 7.3.84 has made\n'
        '  जि into जे, and the अ of शप् follows: ए before a vowel is अय्,\n'
        '  so जे + अ + ति is जयति. Two rules, from two different adhyāyas,\n'
        '  and neither can produce the word alone.'
    ),
)


for _sutra, _why in (
    ('6.1.64',
     'SETTLED — धातोरादेः षकारस्य स्थाने सकारादेशो भवति: षह gives सहते,\n'
     '  षिच gives सिञ्चति.\n'
     '\n'
     'SETTLED — both conditions are tested by the Kāśikā and both are\n'
     '  codified. धातुग्रहणं किम्? षोडश, षण्डः are not roots and keep\n'
     '  their ष्. आदेरिति किम्? कषति, लषति — the ष् is not initial.'),
    ('6.1.65',
     'SETTLED — धातोरादेः is read down: धातोरादेः णकारस्य नकार आदेशो\n'
     '  भवति. णीञ् gives नयति, णम gives नमति, णह gives नह्यति.\n'
     '\n'
     'SETTLED — and the Kāśikā adds a limit worth having: सुब्धातोः अयम्\n'
     '  अपि न इष्यते — a denominative built on the noun णकार is not\n'
     '  reached, so णकारीयति keeps its ण्.'),
):
    register(
        _sutra,
        apply=dhatvadeh,
        codification=(
            'dhatvadeh(root, dhatu=...) -> the root with its initial ष् or '
            'ण् replaced, and which of the two sūtras acted.'
        ),
        related=('8.3.59', '8.4.14'),
        notes=(
            _why + '\n'
            '\n'
            'SETTLED — why enunciate a root with a sound you then replace?\n'
            '  The Kāśikā answers for both: the ṣ- and ṇ-forms are taught so\n'
            '  that LATER rules have something to point at — 8.3.59\n'
            '  आदेशप्रत्ययोः for षत्व, 8.4.14 for णत्व. Being ṣopadeśa or\n'
            '  ṇopadeśa is a property a root carries by how it is\n'
            '  enunciated, and the enunciation is then undone. The mark\n'
            '  outlives the letter, as शप्\'s श् does.\n'
            '\n'
            'NOTE — the logic was already in pada.py, where the pada rules\n'
            '  needed it, and is not written twice. What was missing was the\n'
            '  registration: two sūtras were being applied by a private\n'
            '  helper that no reader could cite and no test could reach.'
        ),
    )


register(
    '6.1.101',
    apply=akah_savarne_dirghah,
    codification=(
        'akah_savarne_dirghah(first, second) -> the long vowel put in place '
        'of the two.'
    ),
    related=('1.1.9', '6.1.97'),
    notes=(
        'SETTLED — अकः सवर्णे अचि परतः पूर्वपरयोः स्थाने दीर्घ एकादेशो\n'
        '  भवति: दण्डाग्रम्, दधीन्द्रः, मधूदके.\n'
        '\n'
        'SETTLED — both conditions are the Kāśikā\'s. अक इति किम्? अग्नये.\n'
        '  सवर्ण इति किम्? दध्यत्र — इ and अ are not of one kind, so यण्\n'
        '  applies there instead.\n'
        '\n'
        'NOTE — whether two sounds are सवर्ण is not decided here. 1.1.9\n'
        '  तुल्यास्यप्रयत्नं सवर्णम् decides it and is codified; this asks.\n'
        '\n'
        'SCAR — that asking went wrong first time. 1.1.9\'s function answers\n'
        '  with a plain bool, and reading it as a record —\n'
        '  getattr(verdict, "savarna", False) — took the default every time,\n'
        '  so the rule silently never fired. A wrong answer would have been\n'
        '  louder than none.'
    ),
)


register(
    '6.1.97',
    apply=ato_gune,
    codification=(
        'ato_gune(first, second) -> the later of the two sounds, standing '
        'for both.'
    ),
    related=('1.1.2', '1.4.2', '6.1.101'),
    notes=(
        'SETTLED — अकारात् अपदान्तात् गुणे परतः पूर्वपरयोः स्थाने\n'
        '  पररूपम् एकादेशो भवति. The *later* form stands: पचन्ति, यजन्ति.\n'
        '\n'
        'SETTLED — अत इति किम्? यान्ति, वान्ति. गुण इति किम्? अपचे, अयजे.\n'
        '  Which vowels are गुण is 1.1.2\'s business, and is asked.\n'
        '\n'
        'SETTLED — the Kāśikā names the relationship rather than leaving it\n'
        '  to be worked out: अकः सवर्णे दीर्घस्य अपवादः. Both rules reach\n'
        '  the अ + अ of पच + अन्ति, and 6.1.101 would give पचान्ति. This is\n'
        '  the second commentary-attested अपवाद in the engine\'s rule set,\n'
        '  after 7.1.3 against 1.3.7, and both are settled the way 1.4.2\n'
        '  says such a clash is NOT settled — by the exception defeating\n'
        '  its उत्सर्ग, whatever the numbers say.'
    ),
)


_STATED = (
    'stated(root, before=..., part=..., sound=..., at=..., '
    'chandasi=...) -> what a rule of 6.1.3–12 names, orders or '
    'refuses, and which rule it takes the form away from.'
)

_VOCALISES = (
    'vocalises(root, before=..., pre=..., result=..., uttarapada=..., '
    'samasa=..., chandasi=..., already=..., wants=...) -> whether the '
    'semivowel gives up its consonant here, and by which rule.'
)

register(
    '6.1.3',
    apply=stated,
    codification=_STATED,
    notes=(
        "SETTLED — न न्द्राः संयोगादयः — and the rule needs 6.1.2's\n"
        '  द्वितीयस्य carried down: **द्वितीयस्येति वर्तते**. Of a\n'
        '  vowel-initial root it is the SECOND one-vowelled portion that\n'
        '  doubles, and where that portion opens on a cluster beginning न्,\n'
        '  द् or र्, that consonant is left out of the copy. **उन्दिदिषति,\n'
        '  अड्डिडिषति, अर्चिचिषति**.\n'
        '\n'
        'SETTLED — **AND BOTH CONDITIONS ARE SHOWN BY WHAT FAILS THEM.**\n'
        '  **न्द्रा इति किम्? ईचिक्षिषते** — the cluster there opens on क्\n'
        '  and the copy keeps it. **संयोगादय इति किम्? प्राणिणिषति** — the ण्\n'
        "  of अन् is no cluster's head, so it doubles, and 8.4.21's उभौ\n"
        '  साभ्यासस्य then makes both ण्.\n'
        '\n'
        'SETTLED — **AND WHY अजादेः IS READ IN A SECOND WAY.** The plain\n'
        '  reading gives दिद्रासति. **केचिदजादेरित्यपि पञ्चम्यन्तं\n'
        '  कर्मधारयमनुवर्तयन्ति। तस्य प्रयोजनम् — इन्दिद्रीयिषति** — read\n'
        '  अजादेः as *from what the initial vowel is*, and the refusal\n'
        '  reaches only the consonant immediately after that vowel. In\n'
        '  इन्द्रीय the न् is that consonant and is dropped; the द् and र्\n'
        '  are not, and double.\n'
        '\n'
        'SETTLED — **AND FOUR SUPPLEMENTS EXTEND IT.** ब् is added to the\n'
        '  three — **उब्जिजिषति** — but only if उब्जि is taught with a\n'
        '  penultimate ब् in the first place. A र् followed by य् is exempt:\n'
        "  **अरार्यते**. ईर्ष्यति doubles its third, and the vārttika's own\n"
        '  commentators cannot agree whether *third* counts consonants\n'
        '  (ईर्ष्यियिषति) or one-vowelled portions (ईर्ष्यिषिषति). And for\n'
        '  denominatives the last word is **यथेष्टं नामधातुषु** —\n'
        '  पुपुत्रीयिषति, पुतित्रीयिषति, पुत्रीयियिषति, all of them'
    ),
)

register(
    '6.1.4',
    apply=stated,
    codification=_STATED,
    notes=(
        'SETTLED — पूर्वोऽभ्यासः — the first of the two is the अभ्यास, and\n'
        '  this is the term every rule from 7.4.58 onward is addressed to.\n'
        '  **पपाच, पिपक्षति, पापच्यते, जुहोति, अपीपचत्**.\n'
        '\n'
        'SETTLED — **AND A NOMINATIVE IS READ AS A GENITIVE TO GET IT.**\n'
        '  6.1.1 supplied द्वे in the nominative. **द्वे इति प्रथमान्तं\n'
        '  यदनुवर्तते, तदर्थादिह षष्ठ्यन्तं जायते** — the sense of THIS rule\n'
        '  turns it into *of the two*, since पूर्व is first only with respect\n'
        '  to something. The case a word carries down is not always the case\n'
        '  it is read in'
    ),
)

register(
    '6.1.5',
    apply=stated,
    codification=_STATED,
    notes=(
        'SETTLED — उभे अभ्यस्तम् — the two together are the अभ्यस्त. **ददति,\n'
        '  ददत्, दधतु**.\n'
        '\n'
        'SETTLED — **AND उभे IS SAID SO THAT ONE ACCENT FALLS ONCE.** द्वे\n'
        '  was already carrying. **उभेग्रहणं समुदायसंज्ञाप्रतिपत्त्यर्थम्** —\n'
        '  it makes the name belong to the whole and not to each half.\n'
        '  **उभेग्रहणं किम्? नेनिजतीत्यत्र अभ्यस्तानामादिः इति समुदाय\n'
        '  उदात्तत्वं यथा स्यात् प्रत्येकं पर्यायेण वा मा भूत्**: with the\n'
        '  name on the pair, 6.1.189 puts the उदात्त on the first vowel of\n'
        '  the pair, once. Name each half and the accent could land in either\n'
        '  half, or in both by turns.\n'
        '\n'
        'SETTLED — **AND THE NAME EARNS TWO MORE RULES.** 7.1.4 puts अत् for\n'
        '  झ after an अभ्यस्त — दद + झि gives ददति — and 6.4.112 gives ददत्.\n'
        '  Neither would reach a form whose halves were named separately'
    ),
)

register(
    '6.1.6',
    apply=stated,
    codification=_STATED,
    notes=(
        'SETTLED — जक्षित्यादयः षट् — seven roots are CALLED अभ्यस्त without\n'
        '  any rule having doubled them. **जक्षति, जाग्रति, दरिद्रति, चकासति,\n'
        '  शासति, दीध्यते, वेव्यते**.\n'
        '\n'
        "SETTLED — **AND THE SŪTRA'S COUNT AND THE VṚTTI'S DISAGREE.** The\n"
        '  rule says षट्, six. The vṛtti names the run by its two ends —\n'
        '  **जक्ष भक्षहसनयोः इत्यतः प्रभृति वेवीङ् वेतिना तुल्ये इति यावत्**\n'
        '  — and then states the count that run actually gives: **सेयं\n'
        '  सप्तानां धातूनाम् अभ्यस्तसंज्ञा विधीयते**, of SEVEN roots. It does\n'
        '  not reconcile them. A boundary named by its ends is the harder\n'
        '  evidence, and the commentary leaves the number in the sūtra\n'
        '  standing.\n'
        '\n'
        'SETTLED — **AND THE NAME IS WHAT THESE ROOTS ARE FOR.** Being\n'
        "  अभ्यस्त gets them 6.1.189's accent on the first syllable; and\n"
        '  दीध्यत्, the शतृ participle, is refused the नुम् augment by 7.1.78\n'
        '  नाभ्यस्ताच्छतुः for the same reason. A saṃjñā doing work no\n'
        '  operation of this section does'
    ),
)

register(
    '6.1.7',
    apply=stated,
    codification=_STATED,
    notes=(
        "SETTLED — तुजादीनां दीर्घोऽभ्यासस्य — the copy's vowel comes out\n"
        '  long: **तूतुजानः, मामहानः, दाधान, मीमाय, दाधार, तूताव**.\n'
        '\n'
        'SETTLED — **AND आदि HERE MEANS *AND THE LIKE*, NOT *AND WHAT\n'
        '  FOLLOWS*.** There is no तुजादि list anywhere. **तुजादीनामिति\n'
        '  प्रकार आदिशब्दः। कश्च प्रकारः? तुजेर्दीर्घोऽभ्यासस्य न विहितः,\n'
        '  दृश्यते च** — the kind is: *forms whose copy is long where no rule\n'
        '  made it so, and which are nevertheless attested*. The rule is\n'
        '  written to admit what the corpus shows rather than to generate it.\n'
        '\n'
        'SETTLED — **AND IT IS BOUNDED BY WHERE IT IS FOUND.** **दीर्घश्च\n'
        '  एषां छन्दसि प्रत्ययविशेष एव दृश्यते, ततोऽन्यत्र न भवति** — only in\n'
        '  the Vedic corpus and only before certain affixes. तुतोज, in\n'
        '  ordinary speech, keeps its short vowel'
    ),
)

register(
    '6.1.8',
    apply=stated,
    codification=_STATED,
    notes=(
        'SETTLED — लिटि धातोरनभ्यासस्य — before लिट्, a root that is not\n'
        '  already a copy doubles, first portion or second according to 6.1.1\n'
        '  and 6.1.2. **पपाच, पपाठ, प्रोर्णुनाव**.\n'
        '\n'
        'SETTLED — **AND धातोः IS IN THE RULE FOR ONE CASE ONLY.** Nothing\n'
        '  stands between root and perfect ending, so the word looks idle.\n'
        '  **लिट् सार्वधातुकम्** by 3.4.117 in some places, and then a विकरण\n'
        '  does intervene: श्रु with श्नु is शृणु, and शृणु is not a धातु.\n'
        '  **सस्वांसो विशृण्विरे, इम इन्द्राय सुन्विरे** — no doubling there.\n'
        '\n'
        'SETTLED — **AND अनभ्यासस्य KEEPS THE INTENSIVE OUT.** नोनूयते has\n'
        '  doubled already under यङ्, so its perfect **नोनाव** does not\n'
        '  double again; likewise **संमिमिक्षुः**. The word carries down\n'
        '  through 6.1.9, 6.1.10 and 6.1.11, and is why जुगुप्सिषते and\n'
        '  लोलूयिषते stand as they are.\n'
        '\n'
        'SETTLED — **AND IN THE छन्दस् THE WHOLE THING IS OPTIONAL.**\n'
        '  **द्विर्वचनप्रकरणे छन्दसि वेति वक्तव्यम्** — याचिषामहे beside\n'
        '  यियाचिषामहे, दाति beside ददाति, धातु beside दधातु. And जागृ\n'
        '  specifically: **यो जागार** beside जजागार'
    ),
)

register(
    '6.1.10',
    apply=stated,
    codification=_STATED,
    notes=(
        'SETTLED — श्लौ — where श्लु has taken the शप् away, the root\n'
        '  doubles: **जुहोति, बिभेति, जिह्रेति**. श्लु is the mark of the\n'
        '  third class, and the doubling is what the class sounds like.\n'
        '  **अनभ्यासस्य** carries down from 6.1.8 here as everywhere in the\n'
        '  run'
    ),
)

register(
    '6.1.11',
    apply=stated,
    codification=_STATED,
    notes=(
        'SETTLED — चङि — before the चङ् of the reduplicated aorist:\n'
        '  **अपीपचत्, अपीपठत्, आटिटत्, आशिशत्, आर्दिदत्**.\n'
        '\n'
        'SETTLED — **AND THE ORDER OF FOUR OPERATIONS IS FORCED.** **पचादीनां\n'
        '  ण्यन्तानां चङि कृते णिलोप उपधाह्रस्वत्वं द्विर्वचनमित्येषां\n'
        '  कार्याणां प्रवृत्तिक्रमः** — drop the णि by 6.4.51, shorten the\n'
        '  penult by 7.4.1, THEN double. Double first and the shortening\n'
        '  comes after the copy is made; the short vowel is then स्थानिवत् to\n'
        "  the long one, counts as heavy, and 7.4.93's सन्वद्भाव — which\n"
        '  wants a LIGHT vowel after the copy — never fires.\n'
        '\n'
        'SETTLED — **AND THE SHORTENING IS NOT स्थानिवत् HERE.** 1.1.57 holds\n'
        '  the substitute to be like the original only for an operation on\n'
        '  what stands BEFORE it. **यो ह्यनादिष्टादचः पूर्वस्तस्य विधिं प्रति\n'
        '  स्थानिवद्भावो भवति। न चास्मिन् कार्याणां क्रमेण अनादिष्टादचः\n'
        '  पूर्वोऽभ्यासो भवति** — with this order the copy is not before an\n'
        '  unsubstituted vowel at all, so the shortened vowel counts as short\n'
        '  and सन्वद्भाव applies. आशीशमत् is the form that decides it.\n'
        '\n'
        'SETTLED — **AND आटिटत् GOES THE OTHER WAY BY THE SAME MAXIM.** There\n'
        '  1.1.59 द्विर्वचनेऽचि makes the substitution स्थानिवत् so that the\n'
        '  SECOND one-vowelled portion, टि, is what doubles'
    ),
)

register(
    '6.1.12',
    apply=stated,
    codification=_STATED,
    notes=(
        'SETTLED — दाश्वान् साह्वान् मीढ्वांश्च — three forms laid down\n'
        '  whole, in the Vedic corpus and in ordinary speech alike: **छन्दसि\n'
        '  भाषायां च अविशेषेण निपात्यन्ते**. Each is क्वसु on a root that\n'
        '  ought to have doubled, and does not.\n'
        '\n'
        'SETTLED — **दाश्वान्** from दाशृ: no doubling and no इट् —\n'
        '  **दाश्वांसो दाशुषः सुतम्**. **साह्वान्** from षह्: parasmaipada, a\n'
        '  lengthened penult, no doubling, no इट् — **साह्वान् बलाहकः**.\n'
        '  **मीढ्वान्** from मिह्: no doubling, no इट्, a lengthened penult,\n'
        '  and ह् → ढ् — **मीढ्वस्तोकाय तनयाय मृड**.\n'
        '\n'
        'SETTLED — **AND THE SINGULAR IN THE RULE IS NOT MEANT.**\n'
        '  **एकवचनमतन्त्रम्** — the plural forms do not double either.\n'
        '\n'
        'SETTLED — **AND FOUR SUPPLEMENTS ADD DOUBLINGS THIS SECTION\n'
        '  OTHERWISE HAS NO PLACE FOR.** क before कृञ् and क्लिद् — **चक्रम्,\n'
        '  चिक्लिदम्**. चर्, चल्, पत् and वद् before अच्, with आक् added to\n'
        '  the copy — **चराचरः, चलाचलः, पतापतः, वदावदः** — and that augment\n'
        "  is itself the proof that 7.4.60's हलादिः शेषः does not run here,\n"
        '  since **हलादिशेषे हि सति आगमस्य आदेशस्य च विशेषो नास्ति**. The\n'
        '  same optionally, so चरः पुरुषः and चलो रथः stand too. हन् before\n'
        '  अच् takes आक् and turns its ह् into घ् — **घनाघनः**. And पाटि\n'
        '  before अच् drops the णि, takes उक्, and lengthens — **पाटूपटः**'
    ),
)

register(
    '6.1.13',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — ष्यङः संप्रसारणं पुत्रपत्योस्तत्पुरुषे — and the section\n'
        "  opens on a base that is not a root at all. ष्यङ् is 4.1.78's\n"
        '  feminine affix, and its य् vocalises when पुत्र or पति follows in\n'
        '  a तत्पुरुष: **कारीषगन्धीपुत्रः, कारीषगन्धीपतिः**.\n'
        '\n'
        'SETTLED — **AND THE HEADING IS DECLARED HERE.** **संप्रसारणमिति\n'
        '  चाधिक्रियते विभाषा परेः इति यावत्** — the word governs to 6.1.44\n'
        '  and no further. Thirty-two sūtras, and this is the first.\n'
        '\n'
        'SETTLED — **AND THE RULE NAMES ONE SEMIVOWEL AMONG SEVERAL.**\n'
        '  कारीषगन्ध्या has more than one यण् in it, and only the ष्यङ्\n'
        '  vocalises: **ष्यङन्ते च यद्यप्यन्ये यणः सन्ति, तथापि ष्यङ एव\n'
        '  संप्रसारणम् — निर्दिश्यमानस्यादेशा भवन्ति**. What a rule POINTS AT\n'
        '  is what a substitute replaces.\n'
        '\n'
        'SETTLED — **AND A FEMININE AFFIX IS READ BY ITS OWN PARIBHĀṢĀ.** The\n'
        '  ordinary maxim would make ष्यङ् mean the whole word beginning with\n'
        '  what it was added to; but **न स्त्रीप्रत्यये चानुपसर्जने** holds\n'
        '  instead, so a feminine affix means only what ENDS in it. Hence\n'
        '  **परमकारीषगन्धीपुत्रः** does vocalise — and\n'
        '  **अतिकारीषगन्ध्यापुत्रः** does not, the base there being उपसर्जन.\n'
        '\n'
        'SETTLED — **AND THE FOLLOWING WORD MUST BE THAT WORD ALONE.**\n'
        '  **पुत्रपत्योः केवलयोरुत्तरपदयोरिदं संप्रसारणम्, तदादौ तदन्ते च न\n'
        '  भवति** — कारीषगन्ध्यापुत्रकुलम् and कारीषगन्ध्यापरमपुत्रः both\n'
        '  stay unvocalised. And तत्पुरुषे matters: कारीषगन्ध्यापतिरयं ग्रामः\n'
        '  is a बहुव्रीहि and keeps its य्'
    ),
)

register(
    '6.1.14',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — बन्धुनि बहुव्रीहौ — the same vocalisation before बन्धु,\n'
        '  and now the compound must be a बहुव्रीहि: **कारीषगन्ध्या बन्धुरस्य\n'
        '  कारीषगन्धीबन्धुः**. Where it is a तत्पुरुष — कारीषगन्ध्याया बन्धुः\n'
        '  — the य् stands.\n'
        '\n'
        "SETTLED — **A GENDER IN THE RULE IS THE WORD-FORM'S, NOT THE\n"
        "  WORD'S.** बन्धुनि is neuter and बन्धु is masculine. **बन्धुनीति\n"
        '  नपुंसकलिङ्गनिर्देशः शब्दरूपापेक्षया, पुँल्लिङ्गाभिधेयस्त्वयं\n'
        '  बन्धुशब्दः** — the sūtra is naming a shape, and a shape has no\n'
        '  gender of its own.\n'
        '\n'
        'SETTLED — **AND A SUPPLEMENT ADDS THREE MORE, OPTIONALLY.**\n'
        '  **मातच्मातृकमातृषु वा** — कारीषगन्धीमातः beside कारीषगन्ध्यामातः.\n'
        '  Two things fall out of it: the चित् of मातच् puts the accent at\n'
        "  the end and so overrides 6.2.1's बहुव्रीहि accent, and मातृ and\n"
        "  मातृक being listed SEPARATELY shows that 5.4.153's कप् is itself\n"
        '  optional here'
    ),
)

register(
    '6.1.15',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — वचिस्वपियजादीनां किति — and the ष्यङ् of the two rules\n'
        '  before drops away. Eleven roots: वच्, स्वप्, and the यजादि that\n'
        '  close the भ्वादि gaṇa — **यजादयो यज देवपूजासंगतिकरणदानेषु इत्यतः\n'
        '  प्रभृति आगणान्ताः**. Before a कित् affix each vocalises: **उक्तः,\n'
        '  सुप्तः, इष्टः, उप्तः, ऊढः, उषितः, उतः, संवीतः, आहूतः, उदितः,\n'
        '  शूनः**.\n'
        '\n'
        'SETTLED — **AND NAMING A ROOT IS NOT NAMING ITS SHAPE.** **धातोः\n'
        '  स्वरूपग्रहणे तत्प्रत्यये कार्यं विज्ञायते** — where a rule names a\n'
        '  particular root rather than saying धातोः, the operation holds only\n'
        '  before an affix that comes AFTER A ROOT. So वाच्यति and वाचिकः do\n'
        '  not vocalise: क्यच् is given after a सुबन्त and ठक् after a\n'
        '  प्रातिपदिक, whatever वाच् may be in itself'
    ),
)

register(
    '6.1.16',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च\n'
        '  — nine more roots, and the च carries किति down from the rule\n'
        '  before, so these vocalise before EITHER marker. **गृहीतः,\n'
        '  गृह्णाति; जीनः, जिनाति; विद्धः, विध्यति; उशितः, उष्टः; विचितः,\n'
        '  विचति; वृक्णः, वृश्चति; पृष्टः, पृच्छति; भृष्टः, भृज्जति**.\n'
        '\n'
        'SETTLED — **AND ONE OF THE NINE IS ITSELF A SUBSTITUTE.** वयि is\n'
        '  what 2.4.41 puts in for वेञ् before लिट्, and वेञ् is already in\n'
        "  6.1.15's list — so why name it? **लिटि तस्य वेञः इति प्रतिषेधो\n"
        '  वक्ष्यते** — 6.1.40 will REFUSE वेञ् in the perfect, and by\n'
        '  स्थानिवद्भाव the refusal would reach वयि too. Naming वयि here\n'
        '  fixes it on the giving side and off the refusing side: **वयेर्विधौ\n'
        '  ग्रहणं प्रतिषेधे चाग्रहणम्**.\n'
        '\n'
        "SETTLED — **AND A ROOT'S GAṆA CAN WIDEN THE AFFIXES THAT COUNT.**\n"
        '  व्यच is कुटादि by a vārttika on 1.2.1, so every affix after it but\n'
        '  a णित् or ञित् is treated as ङित् — **उद्विचिता, उद्विचितुम्,\n'
        '  उद्विचितव्यम्**'
    ),
)

register(
    '6.1.17',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — लिट्यभ्यासस्योभयेषाम् — and now the vocalisation lands not\n'
        "  on the root but on the COPY. Both lists, 6.1.15's and 6.1.16's,\n"
        '  before लिट्: **उवाच, सुष्वाप, इयाज, उवाप; जग्राह, जिज्यौ, उवाय,\n'
        '  विव्याध, उवाश, विव्याच, वव्रश्च**.\n'
        '\n'
        'SETTLED — **AND THE RULE IS FOR THE NON-कित् HALF OF लिट्.**\n'
        '  **अकिदर्थं चेदमभ्यासस्य संप्रसारणं विधीयते** — where the perfect\n'
        '  ending IS कित्, 6.1.15 has already vocalised the root, and the\n'
        '  copy is taken from what is already vocalised: ऊचतुः, ऊचुः. The\n'
        '  order is settled by **पुनःप्रसङ्गविज्ञानात्** — vocalise, then\n'
        '  double.\n'
        '\n'
        'SETTLED — **AND उभयेषाम् IS SAID ONLY TO BEAT 7.4.60.** The\n'
        '  अनुवृत्ति already carried both lists, so the word is idle as a\n'
        '  list: **अधिकारादेवोभयेषां ग्रहणे सिद्धे पुनरुभयेषामिति वचनं\n'
        '  हलादिशेषम् अपि बाधित्वा संप्रसारणमेव यथा स्यात्**. In व्यध् + णल्\n'
        '  the copy is व्य, and हलादिः शेषः would strike the य् out before\n'
        '  anything could vocalise it. The idle word says: vocalise anyway'
    ),
)

register(
    '6.1.18',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — स्वापेश्चङि — and the root named is the CAUSATIVE,\n'
        '  **स्वापेरिति स्वपेर्ण्यन्तस्य ग्रहणम्**. Before चङ्: **असूषुपत्,\n'
        '  असूषुपताम्, असूषुपन्**.\n'
        '\n'
        'SETTLED — **AND THE FIVE STEPS ARE IN ONE ORDER ONLY.**\n'
        '  **द्विर्वचनात् पूर्वमत्र संप्रसारणम्** — vocalise first, then guṇa\n'
        '  the light penult, then 7.4.1 shortens it before चङ्, then the\n'
        '  doubling, then 7.4.94 lengthens the copy. Take them in any other\n'
        '  order and the form is not reached.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI ADMITS IT CANNOT TELL WHAT CARRIES.**\n'
        '  **कितीति निवृत्तम्, ङितीति केवलमिहानुवर्तत इत्येतद्\n'
        '  दुर्विज्ञानम्** — किति has lapsed; whether ङिति alone still runs\n'
        '  is *hard to know*. A commentary saying so in as many words is\n'
        '  worth keeping'
    ),
)

register(
    '6.1.19',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — स्वपिस्यमिव्येञां यङि — three roots before यङ्:\n'
        '  **सोषुप्यते, सेसिम्यते, वेवीयते**. स्वप् and व्येञ् are already in\n'
        "  6.1.15's list, but that rule wants a कित् affix and यङ् is not one"
    ),
)

register(
    '6.1.20',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — न वशः — the first refusal of the section. वश् is one of\n'
        "  6.1.16's nine and would vocalise before the ङित् यङ्; here it does\n"
        '  not: **वावश्यते, वावश्येते, वावश्यन्ते**.\n'
        '\n'
        'SETTLED — **AND THE PROHIBITION DOES NOT GOVERN WHAT IT EXCEPTS.**\n'
        '  Outside यङ् the giving rule stands untouched — उष्टः and उशन्ति\n'
        "  are 6.1.16's, and this rule has nothing to say about them"
    ),
)

register(
    '6.1.21',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — चायः की — and the rule substitutes a finished form instead\n'
        '  of ordering a vocalisation. Before यङ्: **चेकीयते, चेकीयेते,\n'
        '  चेकीयन्ते**.\n'
        '\n'
        'SETTLED — **AND THE LONG ई IN THE SŪTRA IS FOR A CASE THE SŪTRA DOES\n'
        '  NOT MENTION.** **दीर्घोच्चारणं यङ्लुगर्थम्** — with यङ् present,\n'
        '  7.4.25 would lengthen a short इ anyway and कि would have served;\n'
        '  but where the यङ् is dropped there is nothing to lengthen, and the\n'
        '  निष्ठा would come out **चेकितः** instead of **चेकीतः**. The vowel\n'
        '  is written long for the form the rule is silent about'
    ),
)

register(
    '6.1.22',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — स्फायः स्फी निष्ठायाम् — **स्फीतः, स्फीतवान्**.\n'
        '\n'
        'SETTLED — **AND निष्ठायाम् IS ITSELF A HEADING.**\n'
        '  **निष्ठायामित्येतदधिक्रियते लिड्यङोश्च इति प्रागेतस्मात्\n'
        '  सूत्रात्** — the word governs the seven rules from here to 6.1.28,\n'
        '  and stops where 6.1.29 names two other affixes. A heading inside a\n'
        '  heading, and both of them declared by the vṛtti rather than by a\n'
        '  word.\n'
        '\n'
        'SETTLED — **AND स्फाती भवति IS NOT A COUNTER-EXAMPLE.**\n'
        '  **स्फातीभवतीत्येतदपि क्तिन्नन्तस्यैव रूपम्, न निष्ठान्तस्य** — the\n'
        '  ई there is the feminine of the क्तिन् form, not a निष्ठा at all'
    ),
)

register(
    '6.1.23',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — स्त्यः प्रपूर्वस्य — **प्रस्तीतः, प्रस्तीतवान्**, and both\n'
        '  स्त्यै and ष्ट्यै are meant, the two having the same shape स्त्या.\n'
        '\n'
        "SETTLED — **AND THE VOCALISATION UNDOES A LATER RULE'S CONDITION.**\n"
        '  8.2.43 turns the त of निष्ठा into न after a root that has a यण्\n'
        '  and ends in आ. Vocalise the य् and the root no longer has one:\n'
        '  **संप्रसारणे कृते यण्वत्त्वं विहतमिति निष्ठानत्वं न भवति**. What\n'
        "  is left is 8.2.54's optional म — प्रस्तीमः.\n"
        '\n'
        'SETTLED — **AND पूर्वस्य IS SAID SO THAT प्र NEED NOT BE ADJACENT.**\n'
        '  प्रस्त्यः would have done for प्र alone. The compound is read as a\n'
        '  बहुव्रीहि — **प्रः पूर्वो यस्य धातूपसर्गसमुदायस्य स प्रपूर्वः** —\n'
        '  that whole of root-and-preverbs which has प्र first. So\n'
        '  **प्रसंस्तीतः** is reached with सम् standing between'
    ),
)

register(
    '6.1.24',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — द्रवमूर्तिस्पर्शयोः श्यः — and a SENSE decides it.\n'
        '  द्रवमूर्ति is a liquid gone stiff: **शीनं घृतम्, शीना वसा, शीनं\n'
        '  मेदः** — **द्रवावस्थायाः काठिन्यं गतम्**.\n'
        '\n'
        'SETTLED — **AND THE TWO SENSES PART COMPANY LATER IN THE BOOK.**\n'
        '  8.2.47 श्योऽस्पर्शे turns the त into न where the sense is NOT\n'
        '  touch, which is why the congealed thing is शीनम् and the cold\n'
        '  thing is शीतम् — **शीतो वायुः, शीतमुदकम्** — from the very same\n'
        '  vocalisation. One rule here, two forms there'
    ),
)

register(
    '6.1.25',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — प्रतेश्च — the same root after प्रति, and now no sense is\n'
        '  required: **प्रतिशीनः, प्रतिशीनवान्**. The vṛtti says why the rule\n'
        '  exists at all — **द्रवमूर्तिस्पर्शाभ्यामन्यत्रापि यथा स्यादिति\n'
        '  सूत्रारम्भः**: to reach the cases the rule before cannot'
    ),
)

register(
    '6.1.26',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — विभाषाभ्यवपूर्वस्य — after अभि or अव the vocalisation is a\n'
        '  choice: **अभिशीनम्, अभिश्यानम्; अवशीनम्, अवश्यानम्**.\n'
        '\n'
        'SETTLED — **AND THE CHOICE REACHES THE SENSES 6.1.24 MADE FIXED.**\n'
        '  **द्रवमूर्तिस्पर्शविवक्षायामपि विकल्पो भवति** — अभिशीनं घृतम्\n'
        '  beside अभिश्यानं घृतम्. **सेयम् उभयत्रविभाषा द्रष्टव्या**: an\n'
        '  option that both supplies where nothing did and loosens what was\n'
        '  obligatory.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI REFUSES TO SETTLE ONE QUESTION.** Some\n'
        '  read पूर्व as keeping समभिश्यान and समवश्यान out. The Kāśikā\n'
        '  answers **तस्मादत्र भवितव्यमेव** — the option ought to hold there\n'
        '  too; and if it is not wanted, **यत्नान्तरमास्थेयम्**, some other\n'
        '  device must be found, and another use for पूर्व stated. A\n'
        '  commentary declining to paper over a gap'
    ),
)

register(
    '6.1.27',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — शृतं पाके — the whole form is laid down: **शृतं क्षीरम्,\n'
        '  शृतं हविः**, and the root may be causative or not.\n'
        '\n'
        'SETTLED — **AND THE OPTION IS SETTLED BY WHAT THE WORD IS USED OF.**\n'
        '  **व्यवस्थितविभाषा चेयम्, तेन क्षीरहविषोर्नित्यं शृभावो भवति,\n'
        '  अन्यत्र न भवति** — always for milk and oblation, never elsewhere.\n'
        '  And पाके is in the rule to SHOW that field: **पाकग्रहणं\n'
        '  निपातनविषयप्रदर्शनार्थम्**.\n'
        '\n'
        'SETTLED — **AND A SECOND CAUSATIVE IS SHUT OUT.** **श्रपितं क्षीरं\n'
        '  देवदत्तेन यज्ञदत्तेन** is not wanted — where one man has another\n'
        '  cook the milk the form stays श्रपित. But श्रा being intransitive,\n'
        '  both the reflexive and the plain agent give शृतम्: **शृतं क्षीरं\n'
        '  स्वयमेव, शृतं क्षीरं देवदत्तेन**'
    ),
)

register(
    '6.1.28',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — प्यायः पी — **पीनं मुखम्, पीनौ बाहू, पीनमुरः**.\n'
        '\n'
        'SETTLED — **AND THIS OPTION TOO IS SETTLED, AND SETTLED THE OTHER\n'
        '  WAY ROUND.** **इयमपि व्यवस्थितविभाषैव। तेनानुपसर्गस्य नित्यं भवति,\n'
        '  सोपसर्गस्य तु नैव भवति** — always without a preverb, never with\n'
        '  one: आप्यानश्चन्द्रमाः. Where 6.1.27 fixed the option by the\n'
        '  OBJECT spoken of, this one fixes it by whether a preverb stands\n'
        '  there.\n'
        '\n'
        'SETTLED — **AND ONE PREVERB IS PULLED BACK IN.**\n'
        '  **आङ्पूर्वस्यान्धूधसोर्भवत्येव** — with आङ् before it and अन्धु or\n'
        '  ऊधस् in the compound, the substitute returns: **आपीनोऽन्धुः,\n'
        '  आपीनमूधः**'
    ),
)

register(
    '6.1.29',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — लिड्यङोश्च — the same substitute before लिट् and यङ्, and\n'
        '  **विभाषेति निवृत्तम्**: the option of the rule before has lapsed,\n'
        '  so here it is fixed. **आपिप्ये, आपिप्याते, आपिप्यिरे; आपेपीयते,\n'
        '  आपेपीयेते, आपेपीयन्ते**.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTE COMES BEFORE THE DOUBLING THAT\n'
        "  PRECEDES IT.** पी is ordered by a later rule than 6.1.8's doubling\n"
        '  and so wins on परत्व; and then the doubling happens anyway, by\n'
        '  **पुनःप्रसङ्गविज्ञानात्** — a rule that has been set aside once is\n'
        '  allowed to apply again. पी → पिपी → पिप्ये by 6.4.82. The same\n'
        '  maxim 6.1.17 used, in the opposite direction'
    ),
)

register(
    '6.1.30',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — विभाषा श्वेः — **शुशाव, शिश्वाय; शुशुवतुः, शिश्वियतुः;\n'
        '  शोशूयते, शेश्वीयते**.\n'
        '\n'
        'SETTLED — **AND THE ONE OPTION DOES TWO DIFFERENT THINGS.** **यङि\n'
        '  संप्रसारणमप्राप्तं विभाषा विधीयते, लिटि तु किति यजादित्वाद् नित्यं\n'
        '  प्राप्तम्** — before यङ् nothing reached श्वि at all, so the\n'
        '  option SUPPLIES; before लिट् 6.1.15 already reached it as a यजादि\n'
        '  root, so the option LOOSENS. **तत्र सर्वत्र विकल्पो भवतीत्येष\n'
        '  उभयत्रविभाषा**.\n'
        '\n'
        'SETTLED — **AND REFUSING THE ROOT REFUSES THE COPY WITH IT.** **यदा\n'
        '  च धातोर्न भवति, तदा लिट्यभ्यासस्योभयेषाम् इत्यभ्यासस्यापि न भवति**\n'
        '  — this is what makes शिश्वाय possible. Take the option away and\n'
        '  6.1.17 would vocalise the copy and give शुश्वाय, which is not a\n'
        '  form'
    ),
)

register(
    '6.1.31',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — णौ च संश्चङोः — before णि with सन् or चङ् after it, the\n'
        '  same choice: **शुशावयिषति, शिश्वाययिषति; अशूशवत्, अशिश्वयत्**.\n'
        '\n'
        'SETTLED — **AND THIS IS WHERE THE MAXIM IS CITED.** **संप्रसारणं\n'
        '  संप्रसारणाश्रयं च बलीयो भवति** — vocalisation and whatever rests\n'
        '  on it are stronger. Vṛddhi here is अन्तरङ्ग and would ordinarily\n'
        '  go first; **अन्तरङ्गमपि वृद्ध्यादिकं संप्रसारणेन बाध्यते**, and\n'
        '  the vṛddhi and the आव् come afterwards.\n'
        '\n'
        "SETTLED — **AND ONE RULE ELSEWHERE IS READ AS A ज्ञापक.** 7.4.80's\n"
        '  ओः पुयण्ज्यपरे presupposes a उ to work on in the copy — **एतद्\n'
        '  वचनं ज्ञापकं णौ कृतस्थानिवद्भावस्य** — so what णि caused counts as\n'
        '  what it replaced, and it is शु that doubles'
    ),
)

register(
    '6.1.32',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — ह्वः संप्रसारणम् — **जुहावयिषति, अजूहवत्**, and this one\n'
        '  is NOT a choice.\n'
        '\n'
        'SETTLED — **AND THE IDLE WORD IS WHAT DROPS THE OPTION.**\n'
        '  संप्रसारणम् was already carrying by अनुवृत्ति. **संप्रसारणमिति\n'
        '  वर्तमाने पुनः संप्रसारणमित्युक्तं विभाषेत्यस्य निवृत्त्यर्थम्** —\n'
        '  saying it again is how the rule sheds the विभाषा it would\n'
        '  otherwise have inherited from 6.1.31. A word that adds nothing to\n'
        '  the sense, and everything to the force.\n'
        '\n'
        'SETTLED — **AND THE MAXIM KEEPS AN AUGMENT OUT.** 7.3.37 would give\n'
        '  ह्वा the augment युक् before णि; **संप्रसारणस्य बलीयस्त्वात्\n'
        '  प्रागेव युग् न भवति** — vocalise first and there is no आ left for\n'
        '  the augment to attach to.\n'
        '\n'
        'SETTLED — **AND SPLITTING THIS FROM THE NEXT RULE IS ITSELF A\n'
        '  SIGNAL.** The two could have been one. **पृथग्योगकरणम्\n'
        '  अनभ्यस्तनिमित्तप्रत्ययव्यवधाने संप्रसारणाभावज्ञापनार्थम्** — where\n'
        '  an affix that causes no doubling stands between, there is no\n'
        '  vocalisation: ह्वायकीयति, and its desiderative जिह्वायकीयिषति'
    ),
)

register(
    '6.1.33',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — अभ्यस्तस्य च — and the genitive does not agree with ह्वः.\n'
        '  **अभ्यस्तस्य यो ह्वयतिः। कश्चाभ्यस्तस्य ह्वयतिः? कारणम्** — the\n'
        '  ह्वयति that BRINGS ABOUT an अभ्यस्त, not one that is already\n'
        '  inside it. So the vocalisation happens BEFORE the doubling:\n'
        '  **जुहाव, जोहूयते, जुहूषति**.\n'
        '\n'
        "SETTLED — **AND 6.1.5's NAME IS WHAT THE RULE LEANS ON.** अभ्यस्त is\n"
        '  both copies together, so vocalising the root before the split\n'
        '  gives both — and no separate rule for the copy is needed here as\n'
        '  6.1.17 was needed there'
    ),
)

register(
    '6.1.34',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — बहुलं छन्दसि — in the Vedic corpus the same root vocalises\n'
        '  variously: **इन्द्राग्नी हुवे, देवीं सरस्वतीं हुवे**, but also\n'
        '  **ह्वयामि विश्वान् देवान्**.\n'
        '\n'
        'SETTLED — **AND बहुलम् IS NOT विभाषा.** An option gives two forms\n'
        '  for one condition; बहुलम् says the rule is found sometimes\n'
        '  present, sometimes absent, and the corpus is the only evidence for\n'
        "  which. Here हुवे needs 2.4.73's own बहुलं छन्दसि to drop the शप्\n"
        '  first, and then the vocalisation and उवङ्'
    ),
)

register(
    '6.1.35',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — चायः की — the substitute of 6.1.21 again, now in the\n'
        '  छन्दस् and without the यङ् that rule required: **न्यन्यं चिक्युर्न\n'
        '  नि चिक्युरन्यम्**, forms in the उस् of लिट्. And sometimes not at\n'
        '  all — **अग्निर्ज्योतिर्निचाय्य**'
    ),
)

register(
    '6.1.36',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — अपस्पृधेथामानृचुरानृहुश्चिच्युषेतित्याजश्राताः\n'
        '  श्रितमाशीराशीर्ताः — nine forms laid down whole, each with its\n'
        '  irregularity named.\n'
        '\n'
        'SETTLED — **अपस्पृधेथाम्**: from स्पर्ध in लङ्, the र् vocalised and\n'
        '  the अ dropped — **इन्द्रश्च विष्णो यदपस्पृधेथाम्**. In ordinary\n'
        '  speech अस्पर्धेथाम्. A second reading takes अप as the preverb and\n'
        "  the missing अट् as 6.4.75's, and then the counter-example is\n"
        '  अपास्पर्धेथाम्.\n'
        '\n'
        'SETTLED — **आनृचुः, आनृहुः**: from अर्च् and अर्ह् in लिट्, and the\n'
        '  derivation runs through four other rules — 7.4.66 for the अ,\n'
        '  7.4.70 for its lengthening, 7.4.71 for the नुट्.\n'
        '\n'
        'SETTLED — **चिच्युषे**: the COPY vocalised, and no इट्. Ordinarily\n'
        '  चुच्युविषे. **तित्याज**: the copy again, for तत्याज.\n'
        '\n'
        'SETTLED — **श्राताः, श्रितम्, आशीः, आशीर्तः**: all from श्रीञ्. The\n'
        '  vṛtti reports a division of territory — **सोमेषु बहुषु श्राभाव एव,\n'
        '  अन्यत्र श्रिभावः** — and then immediately reports a verse against\n'
        '  it, **यदि श्रातो जुहोतन**, with श्रात in the singular and no soma.\n'
        '  Its answer is that the plural श्राताः in the sūtra is not meant\n'
        '  strictly: **बहुवचनस्याविवक्षितत्वाद् उपसंग्रहो द्रष्टव्यः**'
    ),
)

register(
    '6.1.37',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — न संप्रसारणे संप्रसारणम् — where one semivowel has been\n'
        '  vocalised, the one before it is not. व्यध् has both व् and य्, and\n'
        '  only the य् goes.\n'
        '\n'
        'SETTLED — **AND THE RULE IS THE PROOF OF ITS OWN ORDER.** No giving\n'
        '  rule says WHICH semivowel of a cluster vocalises. **एकयोगलक्षणमपि\n'
        '  संप्रसारणमत एव वचनात् प्रथमं परस्य यणः क्रियते, पूर्वस्य च\n'
        '  प्रसक्तं प्रतिषिध्यते** — this very prohibition settles it,\n'
        '  because if the FIRST were the one vocalised there would never be a\n'
        '  semivowel standing before a vocalised one, and the rule would\n'
        '  forbid nothing.\n'
        '\n'
        'SETTLED — **AND THE WORD IS REPEATED TO REACH ACROSS A GAP.** **पुनः\n'
        '  संप्रसारणग्रहणं विदेशस्थस्यापि संप्रसारणस्य प्रतिषेधो यथा स्यात्**\n'
        '  — the two need not be adjacent. 6.4.133 vocalises the व् of युवन्\n'
        '  and the य् stays: यूनः, यूना. And the long ऊ that swallowed the\n'
        '  two उ-sounds is no help to the objector — a single substitute for\n'
        '  two vowels is not स्थानिवत् by 1.1.58, and even if it were,\n'
        '  **व्यवधानम् एतावद् आश्रयिष्यते**, it is still something standing\n'
        '  between.\n'
        '\n'
        'SETTLED — **AND TWO SUPPLEMENTS ADD WHAT THE RULE DOES NOT.** **ऋचि\n'
        '  त्रेरुत्तरपदादिलोपश्छन्दसि** — तिस्र ऋचो यस्मिन् is तृचं सूक्तम्,\n'
        '  with the ऋ of ऋच् gone too, and only of a metre: त्र्यृचं कर्म\n'
        '  otherwise. And **रयेर्मतौ बहुलम्** — आ रेवानेतु नो विशः beside\n'
        '  रयिमान् पुष्टिवर्धनः'
    ),
)

register(
    '6.1.38',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — लिटि व्यो यः — of the substitute वय्, the य् does not\n'
        '  vocalise in the perfect: **उवाय, ऊयतुः, ऊयुः**. The व् does, by\n'
        '  6.1.16, and that is what makes ऊयतुः.\n'
        '\n'
        'SETTLED — **AND लिटि IS SAID FOR THE RULES AFTER IT.**\n'
        '  **लिड्ग्रहणमुत्तरार्थम्** — वय् takes no other affix, so the word\n'
        '  is idle here; it is put in so that 6.1.39 and 6.1.40 can carry it'
    ),
)

register(
    '6.1.39',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — वश्चास्यान्यतरस्यां किति — and the substitute is a\n'
        '  CONSONANT, the only such row in the section: व् may stand for the\n'
        '  य् of वय् before a कित् perfect ending. **ऊवतुः, ऊवुः** beside\n'
        '  **ऊयतुः, ऊयुः**.\n'
        '\n'
        'SETTLED — **AND PATAÑJALI SAYS THE RULE IS UNNECESSARY.**\n'
        '  अन्यतरस्यां किति वेञः would have done: refuse the vocalisation and\n'
        '  वेञ् gives ववतुः, ववुः; allow it and वे → उ → उवङ् by 6.1.77 gives\n'
        '  ऊवतुः, ऊवुः; and वय्, whose य् 6.1.38 never vocalises, gives\n'
        '  ऊयतुः, ऊयुः. **तथा सर्वाणि त्रीणि रूपाणि वश्चास्येत्यनुक्त्वैव\n'
        '  सिद्धानि** — all three forms, without this rule'
    ),
)

register(
    '6.1.40',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — वेञः — in the perfect वेञ् does not vocalise, and neither\n'
        '  does its copy: **ववौ, ववतुः, ववुः**.\n'
        '\n'
        'SETTLED — **AND THE REFUSAL HAS TO REACH TWO RULES.** **किति\n'
        '  यजादित्वाद् धातोः प्राप्तम्, अकित्यपि लिट्यभ्यासस्योभयेषाम्\n'
        '  इत्यभ्यासस्य, अत उभयं प्रतिषिध्यते** — 6.1.15 would take the root\n'
        '  before a कित् ending and 6.1.17 the copy before the rest, so the\n'
        '  one refusal has to cover both. And this is the prohibition 6.1.16\n'
        '  was careful to keep वयि out of'
    ),
)

register(
    '6.1.41',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — ल्यपि च — and before ल्यप् too: **प्रवाय, उपवाय**.\n'
        '  **पृथग्योगकरणमुत्तरार्थम्** — the rule is split off from 6.1.40 so\n'
        '  that only ल्यप्, and not लिट्, carries into the three that follow'
    ),
)

register(
    '6.1.42',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        "SETTLED — ज्यश्च — **प्रज्याय, उपज्याय**. ज्या is one of 6.1.16's\n"
        "  nine and ल्यप् is कित् by 1.1.5's reading of it, so the\n"
        '  vocalisation would otherwise hold'
    ),
)

register(
    '6.1.43',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — व्यश्च — **प्रव्याय, उपव्याय**, and again **योगविभाग\n'
        '  उत्तरार्थः**: the rule is kept separate so that व्येञ् alone\n'
        '  carries into 6.1.44'
    ),
)

register(
    '6.1.44',
    apply=vocalises,
    codification=_VOCALISES,
    notes=(
        'SETTLED — विभाषा परेः — after परि the refusal is a choice, so the\n'
        '  vocalisation comes back in one of the two forms: **परिवीय यूपम्,\n'
        '  परिव्याय**. The last rule the heading reaches.\n'
        '\n'
        'SETTLED — **AND THE VOCALISED FORM SETS OFF A CONTEST TWO PĀDAS\n'
        '  AWAY.** With परि · वी, 6.1.71 would give the तुक् augment after a\n'
        '  short vowel; **स हलः इति दीर्घत्वेन परत्वाद् बाध्यते** — 6.4.2\n'
        '  lengthens instead, and wins on परत्व. परिवीय, not *परिवित्य'
    ),
)


_BECOMES_A = (
    'becomes_a(root, before=..., result=..., pre=..., final=..., '
    'chandasi=...) -> whether आ is put in for the root\'s final '
    'diphthong, and by which rule of the आकार heading.'
)

_OPERATES = (
    'operates(stem, before=..., after=..., upadha=..., accent=..., '
    'chandasi=..., wants=...) -> what 6.1.58–71 puts in, puts in '
    'place, or takes out here.'
)

register(
    '6.1.45',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — आदेच उपदेशेऽशिति — a root whose final in the धातुपाठ is an\n'
        '  एच् has आ put in its place, and धातोः carries down from 6.1.8.\n'
        '  **ग्लाता, ग्लातुम्, ग्लातव्यम्; निशाता, निशातुम्, निशातव्यम्**.\n'
        '\n'
        'SETTLED — **AND THE HEADING IS DECLARED HERE, ENDING ON ITS OWN LAST\n'
        '  RULE.** **आकाराधिकारस्त्वयं नित्यं स्मयतेः इति यावत्** — the आकार\n'
        '  governs to 6.1.57. Every प्राक् heading of adhyāyas 4 and 5 was\n'
        '  bounded by a word lifted out of the rule AFTER its last; this one\n'
        '  names its last rule, and that rule is a member of the run rather\n'
        '  than its neighbour.\n'
        '\n'
        'SETTLED — **AND उपदेशे IS WHAT KEEPS चेता OUT.** The condition is on\n'
        '  the shape the धातुपाठ taught, not on the shape standing here: चि\n'
        '  and स्तु end in इ and उ there, and the ए and ओ of चेता and स्तोता\n'
        '  are guṇa arrived at later.\n'
        '\n'
        'SETTLED — **AND अशिति IS A प्रसज्यप्रतिषेध, WHICH MOVES THE\n'
        '  SUBSTITUTION EARLIER.** **अशितीति प्रसज्यप्रतिषेधोऽयम्।\n'
        '  तेनैतदात्वमनैमित्तिकं प्रागेव प्रत्ययोत्पत्तेर्भवति** — the आ is\n'
        '  not caused by what follows, so it is already there when an affix\n'
        "  arrives. 3.1.136's क wants a root in आ and finds one: **सुग्लः,\n"
        "  सुम्लः**; so does 3.3.128's युच्: **सुग्लानः, सुम्लानः**.\n"
        '\n'
        'SETTLED — **AND शित् IS READ AS शिदादि, OR THE PERFECT IS LOST.**\n'
        '  एश् has its श् at the end and would block the substitution on the\n'
        '  plain reading, leaving जग्ले and मम्ले unreachable. **नैवं\n'
        '  विज्ञायते — शकार इद् यस्य सोऽयं शिदिति। किं तर्हि? श एव इत्\n'
        '  शित्**, and then **यस्मिन् विधिस्तदादावल्ग्रहणे** confines the\n'
        '  refusal to affixes that BEGIN with श्'
    ),
)

register(
    '6.1.46',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — न व्यो लिटि — व्येञ् keeps its diphthong in the perfect:\n'
        '  **संविव्याय, संविव्ययिथ**.\n'
        '\n'
        'SETTLED — **AND THE FORM IT LEAVES STANDING IS BUILT BY TWO OTHER\n'
        '  RULES.** The copy is vocalised by 6.1.17 लिट्यभ्यासस्योभयेषाम्,\n'
        "  and the vṛddhi in संविव्याय is 7.2.115's अचो ञ्णिति before the\n"
        '  णित् णल्. The refusal removes one operation and leaves the rest of\n'
        '  the derivation where it was'
    ),
)

register(
    '6.1.47',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — स्फुरतिस्फुलत्योर्घञि — before घञ् these two give आ where\n'
        '  guṇa would have given ओ: **विस्फारः, विस्फालः**, not विस्फोरः and\n'
        '  विस्फोलः. And 8.3.76 makes the स् optionally ष् after वि, so\n'
        '  **विष्फारः, विष्फालः** stand beside them'
    ),
)

register(
    '6.1.48',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — क्रीङ्जीनां णौ — three roots before णि: **क्रापयति,\n'
        '  अध्यापयति, जापयति**.\n'
        '\n'
        'SETTLED — **AND THE प् THAT APPEARS IS A CONSEQUENCE OF THE आ, NOT\n'
        '  OF THIS RULE.** 7.3.36 gives the augment पुक् to a root ending in\n'
        '  आ before णि; the substitution here is what makes these roots end\n'
        '  in आ. Three rules deep, and none of the three mentions the प्'
    ),
)

register(
    '6.1.49',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — सिध्यतेरपारलौकिके — before णि, and only where what is\n'
        '  brought about is NOT for the next world: **अन्नं साधयति, ग्रामं\n'
        '  साधयति**.\n'
        '\n'
        'SETTLED — **AND THE COUNTER-EXAMPLE IS ARGUED, NOT ASSERTED.** In\n'
        '  तपस्तापसं सेधयति the root means a particular knowledge, **स च\n'
        '  ज्ञानविशेष उत्पन्नः परलोके जन्मान्तरे फलम् अभ्युदयलक्षणम् उपसंहरन्\n'
        '  परलोकप्रयोजनो भवति** — the knowledge gathers its fruit in another\n'
        '  birth, so its purpose is of that world and the substitution is\n'
        '  withheld.\n'
        '\n'
        'SETTLED — **AND THE REFUSAL DOES NOT REACH ONE STEP FURTHER.** Why\n'
        '  then is **अन्नं साधयति ब्राह्मणेभ्यो दास्यामीति** not caught, the\n'
        '  food being cooked for a gift whose fruit is in the next world?\n'
        '  **सिध्यतेरत्रार्थो निष्पत्तिः... तस्य यद् दानं तत् पारलौकिकम्, न\n'
        '  पुनः सिद्धिरेवेति न आत्वं पर्युदस्यते** — the root means only the\n'
        '  getting-ready; it is the GIVING that is for the next world, and\n'
        '  the rule reaches only what the root itself does. **साक्षात्\n'
        '  परलोकप्रयोजने च सिध्यर्थे कृतावकाशं वचनम् एवंविषयं नावगाहते.**\n'
        '\n'
        'SETTLED — **AND THE SHAPE OF THE WORD IN THE RULE PICKS THE ROOT.**\n'
        '  सिध्यतेः is written with श्यन्, which is the दिवादि root; **षिधु\n'
        '  गत्याम् इत्यस्य भौवादिकस्य निवृत्त्यर्थः**, and the भ्वादि root of\n'
        '  the same shape is left out'
    ),
)

register(
    '6.1.50',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — मीनातिमिनोतिदीङां ल्यपि च — before ल्यप्, and by the च\n'
        '  before whatever else the आकार section reaches: **प्रमाता,\n'
        '  प्रमातव्यम्, प्रमातुम्, प्रमाय; निमाता, निमाय; उपदाता, उपदाय**.\n'
        '\n'
        'SETTLED — **AND उपदेशे CARRIES DOWN, WHICH DECIDES WHICH AFFIXES THE\n'
        '  ROOTS CAN TAKE AT ALL.** **उपदेश एवात्वविधानाद् इवर्णान्तलक्षणः\n'
        '  प्रत्ययो न भवति, आकारान्तलक्षणश्च भवति** — since the आ is there in\n'
        '  the धातुपाठ itself, a rule that wants a root ending in इ or ई\n'
        '  never finds one, and a rule that wants आ always does. So घञ् and\n'
        '  युच् give **उपदायो वर्तते, ईषदुपदानम्**, and the affixes for\n'
        '  इ-final roots do not apply'
    ),
)

register(
    '6.1.51',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — विभाषा लीयतेः — **विलाता, विलातुम्, विलातव्यम्, विलाय**\n'
        '  beside **विलेता, विलेतुम्, विलेतव्यम्, विलीय**. Both लीङ् of the\n'
        '  दिवादि and ली of the क्र्यादि are meant.\n'
        '\n'
        'SETTLED — **AND THE OPTION IS SETTLED BY THE SENSE.** **लियो\n'
        '  व्यवस्थितविभाषाविज्ञानात् सिद्धम्** — in the senses of coaxing,\n'
        '  cheating and putting to shame the substitution is fixed before णि:\n'
        '  **कस्त्वामुल्लापयते, श्येनो वर्तिकामुल्लापयते**.\n'
        '\n'
        'SETTLED — **AND A SUPPLEMENT KEEPS TWO AFFIXES OUT.** **निमिमीलियां\n'
        '  खलचोः प्रतिषेधो वक्तव्यः** — before खल् and अच् the substitution\n'
        '  fails for नि, मि, मी and ली: **ईषन्निमयः, ईषत्प्रमयः, ईषद्विलयः**'
    ),
)

register(
    '6.1.52',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — खिदेश्छन्दसि — in the Vedic corpus the option reaches खिद्\n'
        '  as well: **चित्तं चखाद** beside **चित्तं चिखेद**. Outside it there\n'
        '  is no choice and no substitution'
    ),
)

register(
    '6.1.53',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — अपगुरो णमुलि — after अप and before णमुल्: **अपगारमपगारम्**\n'
        "  beside **अपगोरमपगोरम्**. The णमुल् is 3.4.22's, given for repeated\n"
        '  action, and the word is doubled with it. 3.4.53 gives the same\n'
        '  affix in **अस्यपगारं युध्यन्ते**'
    ),
)

register(
    '6.1.54',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — चिस्फुरोर्णौ — before णि, optionally: **चापयति, चाययति;\n'
        '  स्फारयति, स्फोरयति**. स्फुर् is here for the second time in the\n'
        '  section — 6.1.47 took it before घञ् and made it fixed, and this\n'
        '  rule takes it before णि and makes it a choice'
    ),
)

register(
    '6.1.55',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — प्रजने वीयतेः — before णि, in the sense of conceiving:\n'
        '  **पुरोवातो गाः प्रवापयति** beside **प्रवाययति**, which the vṛtti\n'
        '  glosses **गर्भं ग्राहयति**. And it says what the sense-word\n'
        '  covers: **प्रजनो हि जन्मन उपक्रमो गर्भग्रहणम्** — the beginning of\n'
        '  a birth, the taking of an embryo. वी has five senses in the\n'
        '  धातुपाठ and only this one is reached'
    ),
)

register(
    '6.1.56',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — बिभेतेर्हेतुभये — before णि, where the fear comes STRAIGHT\n'
        '  from the causative agent: **मुण्डो भापयते, जटिलो भापयते** beside\n'
        '  भीषयते.\n'
        '\n'
        'SETTLED — **AND हेतु IS THE TECHNICAL WORD, NOT THE ORDINARY ONE.**\n'
        "  **हेतुरिह पारिभाषिकः स्वतन्त्रस्य प्रयोजकः** — 1.4.55's हेतु, the\n"
        '  one who sets the independent agent going. Where the fear is caused\n'
        '  by an instrument instead, the rule does not reach it.\n'
        '\n'
        'SETTLED — **AND THE TWO SIDES OF THE OPTION TAKE DIFFERENT\n'
        '  AUGMENTS.** 7.3.40 gives षुक् to भी before णि, and **स चात्वपक्षे\n'
        '  न भवति** — not on the side where the आ was put in. The rule there\n'
        '  names भी with its ई written in, and there is no ई left'
    ),
)

register(
    '6.1.57',
    apply=becomes_a,
    codification=_BECOMES_A,
    notes=(
        'SETTLED — नित्यं स्मयतेः — the same condition as the rule before,\n'
        '  the same affix, the same sense — and no choice: **मुण्डो\n'
        '  विस्मापयते, जटिलो विस्मापयते**.\n'
        '\n'
        'SETTLED — **AND THE WORD नित्यम् IS WHAT DROPS THE OPTION.**\n'
        '  **नित्यग्रहणाद् विभाषेति निवृत्तम्** — the विभाषा that has carried\n'
        '  since 6.1.51 stops here, and it stops because one word says so.\n'
        '  The same device 6.1.32 used by repeating संप्रसारणम्.\n'
        '\n'
        'SETTLED — **AND THE SENSE-WORD IS STRETCHED TO FIT.** भय carries\n'
        '  down, but smiling is not fear. **भयशब्देन धात्वर्थसामान्याद् इह\n'
        '  स्मयतेरर्थोऽभिधीयते। न हि मुख्ये भये स्मयतेर्वृत्तिरस्ति** — the\n'
        '  word stands for *whatever this root means*, since it plainly\n'
        '  cannot mean fear here.\n'
        '\n'
        "SETTLED — **AND THIS RULE IS THE HEADING'S OWN BOUND.**\n"
        '  **आकाराधिकारस्त्वयं नित्यं स्मयतेः इति यावत्** — 6.1.45 names this\n'
        '  sūtra as where the आकार stops, and the rule is inside the run it\n'
        '  bounds'
    ),
)

register(
    '6.1.58',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — सृजिदृशोर्झल्यमकिति — before an affix beginning with a झल्\n'
        '  and not marked क्, these two take the augment अम्: **स्रष्टा,\n'
        '  स्रष्टुम्, स्रष्टव्यम्; द्रष्टा, द्रष्टुम्, द्रष्टव्यम्**.\n'
        '\n'
        'SETTLED — **AND IT IS AN अपवाद OF THE GUṆA.**\n'
        '  **लघूपधगुणापवादोऽयममागमः** — 7.3.86 would have given सर्ज् and\n'
        '  दर्श्, and the augment displaces it. Not a second operation but\n'
        '  one instead of another.\n'
        '\n'
        'SETTLED — **AND ONE LATER RULE STILL APPLIES, AFTERWARDS.**\n'
        '  **अस्राक्षीत्, अद्राक्षीत् — सिचि वृद्धिः अमि कृते भवति, पूर्वं तु\n'
        "  बाध्यते** — 7.2.1's vṛddhi takes effect ONCE the अम् is in, and\n"
        '  not before. The augment beats the guṇa outright and merely delays\n'
        '  the vṛddhi.\n'
        '\n'
        'SETTLED — **AND NAMING THE ROOTS RESTRICTS WHICH AFFIXES COUNT.**\n'
        '  **धातोः स्वरूपग्रहणे तत्प्रत्यये कार्यविज्ञानात्** — the rule\n'
        '  names सृज् and दृश् rather than saying धातोः, so it reaches only\n'
        '  affixes given after a ROOT. **रज्जुसृड्भ्याम्, देवदृग्भ्याम्** are\n'
        '  untouched'
    ),
)

register(
    '6.1.59',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — अनुदात्तस्य च ऋदुपधस्यान्यतरस्याम् — the same augment,\n'
        '  optionally, for a root the धातुपाठ marked अनुदात्त with ऋ for its\n'
        '  penult: **त्रप्ता, तर्पिता, तर्प्ता; द्रप्ता, दर्पिता, दर्प्ता**.\n'
        '\n'
        'SETTLED — **AND THREE FORMS COME FROM TWO OPTIONS CROSSING.** तृप्\n'
        '  and दृप् are रधादि, so 7.2.45 makes their इट् a choice as well.\n'
        '  **अनुदात्तोपदेशः पुनरमर्थ एव** — being अनुदात्त in the धातुपाठ is\n'
        '  what this rule turns on, and the इट् has its own reason. Two\n'
        '  independent options, three attested forms.\n'
        '\n'
        'SETTLED — **AND उपदेशे CARRIES DOWN FROM 6.1.45.** That is what\n'
        '  makes वर्ढा a counter-example: वृहू is उदात्त where the धातुपाठ\n'
        '  taught it, whatever it looks like here'
    ),
)

register(
    '6.1.60',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — शीर्षंश्छन्दसि — in the Vedic corpus **शीर्षन्** is laid\n'
        '  down as a word of its own, meaning what शिरस् means: **शीर्ष्णा हि\n'
        '  तत्र सोमं क्रीतं हरन्ति; यत्ते शीर्ष्णो दौर्भाग्यम्**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI REFUSES TO CALL IT A SUBSTITUTE, WITH AN\n'
        '  ARGUMENT.** **शीर्षन्निति शब्दान्तरं शिरःशब्देन समानार्थं छन्दसि\n'
        '  विषये निपात्यते, न पुनरयमादेशः शिरःशब्दस्य, सोऽपि हि छन्दसि\n'
        '  प्रयुज्यत एव** — शिरस् is used in the corpus TOO, so neither word\n'
        '  can be standing in for the other. Both are simply there. The next\n'
        '  rule is an आदेश and this one is not, and the difference is settled\n'
        '  by what the corpus contains'
    ),
)

register(
    '6.1.61',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — ये च तद्धिते — before a taddhita affix beginning with य्,\n'
        "  शिरस् is replaced by शीर्षन्: **शीर्षण्यः स्वरः**, with 4.3.55's\n"
        "  यत् and 6.4.168's प्रकृतिभाव keeping the अन् standing.\n"
        '\n'
        'SETTLED — **AND THE RULE NAMES NO BASE, SO THE BASE IS ARGUED IN.**\n'
        '  **आदेशोऽयमिष्यते। स कथम्? तद्धित इति हि परं निमित्तमुपादीयते, स\n'
        '  तदनुरूपां प्रकृतिं शिरःशब्दम् आक्षिपति** — only what FOLLOWS is\n'
        '  stated, and what follows draws in the base it fits. A substitution\n'
        '  whose स्थानिन् is inferred rather than named, one rule after a\n'
        '  निपातन whose vṛtti argued that nothing was being substituted at\n'
        '  all.\n'
        '\n'
        'SETTLED — **AND A SUPPLEMENT MAKES IT A CHOICE IN ONE SENSE.** **वा\n'
        '  केशेषु** — **शीर्षण्याः केशाः** beside **शिरस्याः केशाः**'
    ),
)

register(
    '6.1.62',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — अचि शीर्षः — before a taddhita beginning with a vowel the\n'
        '  substitute is शीर्ष, without the न्: **हास्तिशीर्षिः,\n'
        '  स्थौलशीर्षम्**.\n'
        '\n'
        'SETTLED — **AND THE MISSING न् IS THE WHOLE POINT.** **शीर्षन्भावे\n'
        '  हि अन् इति प्रकृतिभावः स्यात्** — with शीर्षन् here, 6.4.167 would\n'
        '  hold the अन् in place and the forms would come out wrong. The two\n'
        '  rules give two shapes of one word because two later rules treat\n'
        '  them differently.\n'
        '\n'
        'SETTLED — **AND THE FEMININE OF हास्तिशीर्षि IS A PROBLEM THE VṚTTI\n'
        '  LEAVES HALF OPEN.** ष्यङ् begins with य्, so 6.1.61 would turn the\n'
        '  शीर्ष back into शीर्षन् and give **हास्तिशीर्षण्या**, which is not\n'
        '  wanted. **कर्तव्योऽत्र यत्नः** — an effort has to be made here —\n'
        '  and the way out offered is that the इ of the इञ् is dropped by\n'
        '  6.4.148 and its स्थानिवद्भाव stands between the शीर्ष and the य्,\n'
        '  so the earlier rule cannot reach'
    ),
)

register(
    '6.1.63',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — पद्दन्नोमास्हृन्निश्असन्यूषन्दोषन्यकञ्शकन्नुदन्नासञ्\n'
        '  छस्प्रभृतिषु — thirteen stems and thirteen substitutes, paired off\n'
        '  यथासंख्यम् before शस् and the endings after it. **निपदश्चतुरो जहि;\n'
        '  या दतो धावते; सूकरस्त्वा खनन्नसा; हृदा पूतं मनसा जातवेदो; यूष्ण\n'
        '  आसेचनानि; उद्नो दिव्यस्य; आसनि किं लभे मधूनि**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI REPORTS A DISAGREEMENT WITHOUT SETTLING\n'
        '  IT.** **केचिदत्र छन्दसीत्यनुवर्तयन्ति। अपरे पुनर्\n'
        '  अविशेषेणेच्छन्ति** — some carry छन्दसि down from 6.1.60 and\n'
        '  confine the rule to the corpus; others want it everywhere, and\n'
        '  quote a verse of ordinary Sanskrit for it:\n'
        '  **व्यायामक्षुण्णगात्रस्य पद्भ्यामुद्वर्तितस्य च**. And a third\n'
        '  party carries अन्यतरस्याम् down from 6.1.59 instead, **तेन\n'
        '  पादादयोऽपि प्रयुज्यन्ते**, so that both shapes stand.\n'
        '\n'
        'SETTLED — **AND प्रभृति IS READ AS A KIND, NOT AS A LIST.**\n'
        '  **शस्प्रभृतिष्विति प्रकारार्थे प्रभृतिशब्दः** — which is how **शला\n'
        '  दोषणी** is reached, where the ending is not one of the run at all.\n'
        '\n'
        'SETTLED — **AND THREE SUPPLEMENTS ADD THREE MORE PAIRS.** **पदादिषु\n'
        '  मांस्पृत्स्नूनामुपसंख्यानम्** — **मांस्पचन्याः, पृत्सु मर्त्यम्,\n'
        '  अधि स्नुषु**. A fourth confines the नस् of नासिका to यत्, तस् and\n'
        '  क्षुद्र — **नस्यम्, नस्तः, नःक्षुद्रः** — and a fifth keeps it off\n'
        '  **नासिक्यो वर्णः, नासिक्यं नगरम्**'
    ),
)

register(
    '6.1.66',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — लोपो व्योर्वलि — a व् or य् is dropped before a consonant\n'
        '  other than य्, and **धातोः** has lapsed: **धातोरिति प्रकृतं यत्\n'
        '  तद् धात्वादेरिति पुनर्धातुग्रहणाद् निवृत्तम्। तेन धातोरधातोश्च**.\n'
        '  So the rule reaches a root and a non-root alike — **दिदिवान्,\n'
        '  ऊतम्, क्नूतम्; गौधेरः; पचेरन्, यजेरन्; जीरदानुः**.\n'
        '\n'
        'SETTLED — **AND THE WORD लोप STANDS FIRST TO FIX AN ORDER.**\n'
        '  **पूर्वं लोपग्रहणं किम्? वेरपृक्तलोपात् पूर्वं वलि लोपो यथा\n'
        "  स्यात्** — this removal has to happen before 6.1.67's, or कण्डू\n"
        '  and लोलू are not reached: **कण्डूयतेः क्विप् — कण्डूः; लोलूयतेः —\n'
        '  लोलूः**. Where a word stands in a rule, and not only what it says.\n'
        '\n'
        'SETTLED — **AND ONE ROOT IS PROTECTED BY THE WAY IT IS TAUGHT.**\n'
        '  **व्रश्चादीनामुपदेशसामर्थ्याद् वलि लोपो न भवति** — had the व् been\n'
        '  meant to go, the root would have been taught as रश्च्. And that\n'
        '  argument has to be made because the removal is अन्तरङ्ग where the\n'
        '  संप्रसारण and the हलादिशेष that give वृश्चति and वव्रश्च are\n'
        '  बहिरङ्ग'
    ),
)

register(
    '6.1.67',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — वेरपृक्तस्य — the affix वि, reduced to a single sound, is\n'
        '  dropped. **वेरिति क्विबादयो विशेषाननुबन्धानुत्सृज्य सामान्येन\n'
        '  गृह्यन्ते** — क्विप्, क्विन् and ण्वि are all meant, their markers\n'
        '  set aside: **ब्रह्महा, भ्रूणहा; घृतस्पृक्, तैलस्पृक्; अर्धभाक्,\n'
        '  पादभाक्, तुरीयभाक्**.\n'
        '\n'
        'SETTLED — **AND AN AFFIX THAT VANISHES STILL DOES ITS WORK.** By\n'
        '  1.1.62 the removal leaves the mark of the affix behind, which is\n'
        '  the whole reason these affixes are given: a root cannot become a\n'
        '  nominal stem except through one'
    ),
)

register(
    '6.1.68',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल् — after a\n'
        '  consonant, or a long ङी or आप्, the single consonant left of सु,\n'
        '  ति or सि is dropped: **राजा, तक्षा; कुमारी, गौरी; खट्वा;\n'
        '  अबिभर्भवान्; अभिनोऽत्र**.\n'
        '\n'
        'SETTLED — **AND सि IS THE ENDING AND NOT THE AORIST MARKER.** **तिपा\n'
        '  सहचरितस्य सिशब्दस्य ग्रहणात् सिचो ग्रहणं नास्ति** — it keeps\n'
        '  company with ति, and that decides which सि is meant. अभैत्सीत्\n'
        '  keeps its स्.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI ARGUES IN VERSE WHY THE RULE IS STATED AT\n'
        "  ALL.** 8.2.23's संयोगान्तलोप would seem to do the work. Four forms\n"
        '  say otherwise, and the vṛtti sets them in a śloka: **संयोगान्तस्य\n'
        '  लोपे हि नलोपादिर्न सिध्यति। रात् तु ते नैव लोपः स्याद् धलस्तस्माद्\n'
        '  विधीयते॥** — 8.2.23 is असिद्ध, so राजा would never lose its न्;\n'
        '  उखास्रत् is not पदान्त, so the द् would not be reached; अभिनोऽत्र\n'
        "  needs a रु for 6.1.113 to work on; and 8.2.24's रात् सस्य would\n"
        '  confine the loss to a स्, leaving अबिभर्भवान् out'
    ),
)

register(
    '6.1.69',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — एङ् ह्रस्वात् सम्बुद्धेः — in the vocative singular the\n'
        '  consonant of the ending is dropped after ए or ओ and after a short\n'
        '  vowel: **हे अग्ने, हे वायो; हे देवदत्त, हे नदि, हे वधु, हे\n'
        '  कुण्ड**.\n'
        '\n'
        'SETTLED — **AND अपृक्तम् DOES NOT CARRY HERE — PROVED BY THE RULE\n'
        '  BEFORE SAYING IT TWICE.** **अपृक्तमिति नाधिक्रियते। तथा च\n'
        '  पूर्वसूत्रे पुनरपृक्तग्रहणं कृतम्** — 6.1.67 had already supplied\n'
        '  the word and 6.1.68 states it again, and that redundancy is the\n'
        '  evidence that it stops there. The inverse of the idle-word\n'
        '  argument: a word repeated EARLIER shows it is absent LATER.\n'
        '\n'
        'SETTLED — **AND हे कुण्ड IS WHY IT MATTERS.** The ending there is\n'
        "  7.1.24's अम्, which is two sounds and no अपृक्त. Only the म् is\n"
        "  taken, the अ having merged with the stem's by 6.1.107. Read\n"
        '  अपृक्तम् into this rule and हे कुण्ड is unreachable.\n'
        '\n'
        'SETTLED — **AND एङ् IS SAID BECAUSE THE GUṆA WINS FIRST.**\n'
        '  **एङ्ग्रहणं क्रियते संबुद्धिगुणबलीयस्त्वात्** — 7.3.108 has\n'
        '  already made अग्नि into अग्ने by the time this rule looks, so a\n'
        '  rule speaking only of short vowels would find none'
    ),
)

register(
    '6.1.70',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — शेश्छन्दसि बहुलम् — in the Vedic corpus the शि of the\n'
        '  neuter plural is dropped variously: **या क्षेत्रा, या वना** beside\n'
        '  **यानि क्षेत्राणि, यानि वनानि**. Both shapes are found in the\n'
        '  corpus, which is what बहुलम् records and what an option would not'
    ),
)

register(
    '6.1.71',
    apply=operates,
    codification=_OPERATES,
    notes=(
        'SETTLED — ह्रस्वस्य पिति कृति तुक् — a root ending in a short vowel\n'
        '  takes the augment तुक् before a कृत् affix marked प्: **अग्निचित्,\n'
        '  सोमसुत्; प्रकृत्य, प्रहृत्य, उपस्तुत्य**.\n'
        '\n'
        'SETTLED — **AND A SHORTENING MADE ELSEWHERE DOES NOT COUNT AS\n'
        '  SHORT.** In **ग्रामणि ब्राह्मणकुलम्** the vowel has been\n'
        '  shortened, and still there is no तुक्: **ह्रस्वस्य बहिरङ्गस्य\n'
        '  असिद्धत्वात् तुग् न भवति** — what is बहिरङ्ग counts as not having\n'
        '  happened when something अन्तरङ्ग is to take effect. The same maxim\n'
        '  6.1.66 had to argue against, used here the other way'
    ),
)


_JOINS = (
    'joins(stem, before=..., after=..., result=..., chandasi=...) -> '
    'what happens where two sounds meet in संहिता, and which rule of '
    '6.1.72–83 does it.'
)

register(
    '6.1.72',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — संहितायाम् — **अधिकारोऽयम् अनुदात्तं पदमेकवर्जम् इति\n'
        '  यावत्। प्रागेतस्मात् सूत्रादित उत्तरं यद् वक्ष्यामः\n'
        '  संहितायामित्येवं तद् वेदितव्यम्** — everything from here to\n'
        '  6.1.157 holds only where the two sounds are spoken in one unbroken\n'
        '  flow.\n'
        '\n'
        'SETTLED — **AND THE CONDITION IS SHOWN BY WHAT FAILS IT.**\n'
        '  **वक्ष्यति इको यणचि — दध्यत्र, मध्वत्र। संहितायामिति किम्? दधि\n'
        '  अत्र, मधु अत्र** — the same two words, and with a pause between\n'
        '  them nothing happens at all. The longest heading of the pāda, and\n'
        '  its condition is not a grammatical category but a manner of\n'
        '  speaking'
    ),
)

register(
    '6.1.73',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — छे च — a short vowel takes the augment तुक् before छ, and\n'
        '  ह्रस्वस्य तुक् carries down from 6.1.71: **इच्छति, यच्छति**.\n'
        '  8.4.40 then makes the त् a च्.\n'
        '\n'
        'SETTLED — **AND WHAT TAKES THE AUGMENT IS THE VOWEL, NOT THE WORD\n'
        '  ENDING IN IT.** **ह्रस्व एवात्रागमी, न तु तदन्तः** — and the\n'
        '  difference is visible in **चिच्छिदतुः, चिच्छिदुः**, where the त्\n'
        '  survives. Being an augment of the इ, it is not part of the copy\n'
        "  चि, so 7.4.60's हलादिः शेषः has nothing to strike: **नावयवावयवः\n"
        '  समुदायावयवो भवति** — a part of a part is not a part of the whole'
    ),
)

register(
    '6.1.74',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — आङ्माङोश्च — for आङ् in its four senses and for the\n'
        '  prohibitive माङ्, the augment before छ: **ईषच्छाया, आच्छादयति,\n'
        '  आच्छायम्; माच् छैत्सीत्, माच् छिदत्**.\n'
        '\n'
        'SETTLED — **AND THE RULE FIXES WHAT A LATER RULE WILL LOOSEN.**\n'
        '  **पदान्ताद् वा इति विकल्पे प्राप्ते नित्यं तुगागमो भवति** — 6.1.76\n'
        '  has not been stated yet and would make the augment a choice after\n'
        '  a पदान्त long vowel; this rule says it is fixed for these two. An\n'
        '  अपवाद pointing FORWARD.\n'
        '\n'
        'SETTLED — **AND THE ङ् OF आङ् AND माङ् IS WHAT NARROWS THEM.**\n'
        '  **ङिद्विशिष्टग्रहणं किम्? आ छाया, आच् छाया। प्रमा छन्दः, प्रमाच्\n'
        '  छन्दः** — the आ of recollection and the noun प्रमा are not the आङ्\n'
        '  and माङ् the rule names, so for them the augment falls back to\n'
        "  6.1.76's option"
    ),
)

register(
    '6.1.75',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — दीर्घात् — a long vowel too: **ह्रीच्छति, म्लेच्छति,\n'
        '  अपचाच्छायते, विचाच्छायते**. And the augment belongs to the long\n'
        '  vowel itself, on the same reading 6.1.73 was given — **पूर्वस्य\n'
        '  तस्यैव दीर्घस्य**'
    ),
)

register(
    '6.1.76',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — पदान्ताद् वा — where the long vowel ends a पद the augment\n'
        '  is a choice: **कुटीच्छाया, कुटीछाया; कुवलीच्छाया, कुवलीछाया**.\n'
        '\n'
        'SETTLED — **AND THIS IS A पदान्त RULE AND NOT A पदविधि.** The\n'
        "  augment attaches at the end of a पद, so 2.1.1's समर्थः पदविधिः\n"
        '  does not apply and the two words need not be construed together at\n'
        '  all: **तिष्ठतु कुमारीच्छत्रं हर देवदत्तस्य** takes the augment\n'
        '  though कुमारी and छत्रम् belong to different clauses.\n'
        '\n'
        'SETTLED — **AND A SUPPLEMENT ADDS A VEDIC LIST.** **विश्वजनादीनां\n'
        '  छन्दसि वा तुगागमो भवतीति वक्तव्यम्** — **विश्वजनच्छत्रम्,\n'
        '  विश्वजनछत्रम्**'
    ),
)

register(
    '6.1.77',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — इको यणचि — an इक् becomes the matching semivowel before a\n'
        '  vowel: **दध्यत्र, मध्वत्र, कर्त्रर्थम्, हर्त्रर्थम्, लाकृतिः**.\n'
        '\n'
        'SETTLED — **AND A SECOND HEADING OPENS HERE, INSIDE THE FIRST.**\n'
        '  **अचीति चायमधिकारः संप्रसारणाच्च इति यावत्** — the word *before a\n'
        '  vowel* governs from here to 6.1.108. संहिता is bounded by the\n'
        '  words of a rule OUTSIDE its run; this one by the words of a rule\n'
        "  that is a member of it, as 6.1.45's आकार was bounded by 6.1.57.\n"
        '\n'
        'SETTLED — **AND A SUPPLEMENT GIVES IT PRECEDENCE OVER THE\n'
        '  LENGTHENING.** **इकः प्लुतपूर्वस्य सवर्णदीर्घबाधनार्थं यणादेशो\n'
        '  वक्तव्यः** — after a प्लुत vowel the semivowel wins even where the\n'
        '  two are savarṇa: **भो३ इ इन्द्रम्** gives **भो३यिन्द्रम्**'
    ),
)

register(
    '6.1.79',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — वान्तो यि प्रत्यये — of the four substitutes 6.1.78 gives\n'
        '  for an एच्, the two that END in व् — अव् and आव् — come also\n'
        '  before an affix beginning with य्: **बाभ्रव्यः, माण्डव्यः,\n'
        '  शङ्कव्यं दारु, पिचव्यः कार्पासः, नाव्यो ह्रदः**.\n'
        '\n'
        'SETTLED — **AND WHICH TWO ARE MEANT IS SETTLED BY THE SHAPE OF THE\n'
        '  WORD.** Naming the substitutes that end in व् is how the rule\n'
        '  names the vowels they replace, ओ and औ, without naming them.\n'
        '\n'
        'SETTLED — **AND TWO SUPPLEMENTS ADD गो BEFORE यूति.** **गोर्यूतौ\n'
        '  छन्दसि** — **गव्यूतिमुक्षतम्** in the corpus, गोयूतिः outside it;\n'
        '  and **अध्वपरिमाणे च** — **गव्यूतिमात्रमध्वानं गतः**, where the\n'
        '  word is a measure of road'
    ),
)

register(
    '6.1.80',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — धातोस्तन्निमित्तस्यैव — and the rule supplies nothing. It\n'
        '  NARROWS 6.1.79: for a ROOT, the substitution holds only where the\n'
        '  diphthong was itself brought about by that य-affix. **लव्यम्,\n'
        '  पव्यम्; अवश्यलाव्यम्, अवश्यपाव्यम्** — लू takes यत्, the affix\n'
        '  causes the guṇa, and the ओ so produced becomes अव्.\n'
        '\n'
        'SETTLED — **AND धातोः IS SAID SO THAT A STEM IS LEFT ALONE.**\n'
        '  **धातोरिति किम्? प्रातिपदिकस्य नियमो मा भूत्। तत्र को दोषः?\n'
        '  बाभ्रव्य इत्यत्रैव स्यात्, इह न स्याद् गव्यं नाव्यम्** — गो and नौ\n'
        '  have their diphthongs from the start, and a restriction reaching\n'
        '  stems would lose both.\n'
        '\n'
        'SETTLED — **AND THE एवकार RESTRICTS THE ROOT, NOT THE CAUSE.**\n'
        '  **एवकारकरणं किम्? धात्ववधारणं यथा स्यात्, तन्निमित्तावधारणं मा\n'
        '  भूत्। तन्निमित्तस्य हि धातोश्चाधातोश्च भवति** — read the other way\n'
        '  it would say *only what the affix caused*, and बाभ्रव्यः would be\n'
        '  lost. One word, two readings, and the wrong one loses a form the\n'
        '  right one keeps'
    ),
)

register(
    '6.1.81',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — क्षय्यजय्यौ शक्यार्थे — two forms laid down whole, with\n'
        '  अय् for the ए before यत्, and only where the sense is *able to\n'
        '  be*: **शक्यः क्षेतुं क्षय्यः, शक्यो जेतुं जय्यः**. Where the sense\n'
        '  is obligation the ordinary forms stand'
    ),
)

register(
    '6.1.82',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — क्रय्यस्तदर्थे — the same substitution for क्री, and only\n'
        '  in the sense of being put out FOR that, for buying: **क्रय्यो गौः,\n'
        '  क्रय्यः कम्बलः**, and the vṛtti glosses it **क्रयार्थं यः\n'
        '  प्रसारितः, स उच्यते**. **क्रेयं नो धान्यम्, न चास्ति क्रय्यम्**\n'
        '  sets the two senses against each other in one sentence'
    ),
)

register(
    '6.1.83',
    apply=joins,
    codification=_JOINS,
    notes=(
        'SETTLED — भय्यप्रवय्ये च छन्दसि — two more laid down, for the\n'
        '  corpus: **भय्यं किलासीत्; वत्सतरी प्रवय्या**.\n'
        '\n'
        'SETTLED — **AND EACH CARRIES AN ODDITY OF ITS OWN.** भय्यम् takes\n'
        "  its यत् in the ABLATIVE sense by 3.3.113's कृत्यल्युटो बहुलम् —\n"
        '  **बिभेत्यस्मादिति भय्यम्**, that from which one fears. And\n'
        '  **प्रवय्या इति स्त्रियामेव निपातनम्** — the form is laid down in\n'
        '  the feminine alone, प्रवेयम् standing elsewhere.\n'
        '\n'
        'SETTLED — **AND A SUPPLEMENT ADDS A THIRD.** **ह्रदय्या आप\n'
        "  उपसंख्यानम्** — **ह्रदय्या आपः**, water of a pool, with 4.4.110's\n"
        '  यत्'
    ),
)


_ONE_FOR_BOTH = (
    'one_for_both(stem, after=..., before=..., result=..., '
    'teacher=..., chandasi=...) -> which single substitute stands '
    'for the earlier sound and the later one together.'
)

register(
    '6.1.84',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — एकः पूर्वपरयोः — **अधिकारोऽयम्। ख्यत्यात् परस्य इति\n'
        '  प्रागेतस्मात् सूत्रादित उत्तरं यद् वक्ष्यामस्तत्र पूर्वस्य परस्य\n'
        '  द्वयोरपि स्थान एकादेशो भवति** — from here to 6.1.111, one\n'
        '  substitute stands in the room of the earlier sound and the later\n'
        '  one together. **खट्वेन्द्रः**: the ए replaces the आ and the इ at\n'
        '  once.\n'
        '\n'
        'SETTLED — **AND पूर्वपर IS SAID SO THAT THE SUBSTITUTION HAS ONE\n'
        '  PLACE AND NOT TWO.** **पूर्वपरग्रहणं द्वयोरपि\n'
        '  युगपदादेशप्रतिपत्त्यर्थम्, एकस्यैव हि स्यात्, नोभे सप्तमीपञ्चम्यौ\n'
        '  युगपत् प्रकल्पिके भवत इति** — 6.1.87 has आत् in the ablative and\n'
        '  अचि in the locative; 1.1.67 would send the substitution to what\n'
        '  FOLLOWS the आ and 1.1.66 to what PRECEDES the vowel, and the two\n'
        '  cases cannot both take effect. The word makes them one place.\n'
        '\n'
        'SETTLED — **AND एक IS SAID SO THAT THERE IS ONE SUBSTITUTE AND NOT\n'
        '  TWO.** **एकग्रहणं पृथगादेशनिवृत्त्यर्थम्, स्थानिभेदाद्धि\n'
        '  भिन्नादिषु नत्ववद् द्वावादेशौ स्याताम्** — two different स्थानिन्\n'
        '  would otherwise take two different substitutes, as they do under\n'
        '  the न् rules. Two words, two failures they prevent, and the\n'
        '  commentary states each'
    ),
)

register(
    '6.1.87',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — आद् गुणः — where अ or आ stands before a vowel, one guṇa\n'
        '  replaces both: **तवेदम्, खट्वेन्द्रः, मालेन्द्रः; तवोदकम्,\n'
        '  खट्वोदकम्; तवर्श्यः, खट्वर्श्यः; तवल्कारः, खट्वल्कारः**.\n'
        '\n'
        'SETTLED — **AND THE ऌ CASE NEEDS 1.1.51 TO FINISH IT.** **ऌकारस्य\n'
        '  स्थाने योऽण् तस्य लपरत्वमिष्यते** — the guṇa of ऌ is अ, and\n'
        "  1.1.51's उरण् रपरः is read as putting a ल् after it, exactly as it\n"
        '  puts a र् after the अ that replaces ऋ. **तवल्कारः**, and not\n'
        '  *तवकारः.\n'
        '\n'
        'SETTLED — **AND THIS IS THE RULE THE WHOLE SECTION IS AN EXCEPTION\n'
        '  CHAIN AGAINST.** 6.1.88, 6.1.91, 6.1.94, 6.1.96, 6.1.97 and\n'
        '  6.1.102 each displace it in their own case, and 6.1.89 displaces\n'
        '  one of THOSE'
    ),
)

register(
    '6.1.88',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — वृद्धिरेचि — where the later sound is an एच्, vṛddhi\n'
        '  instead of guṇa: **ब्रह्मैडका, खट्वैडका; ब्रह्मौदनः, खट्वौदनः;\n'
        '  ब्रह्मौपगवः, खट्वौपगवः**. The vṛtti names the relation rather than\n'
        '  leaving it to be worked out — **आद्गुणस्यापवादः**'
    ),
)

register(
    '6.1.89',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — एत्येधत्यूठ्सु — vṛddhi before the ए of एति, the एध् of\n'
        '  एधति, and the ऊठ्: **उपैति, उपैषि, उपैमि; उपैधते, प्रैधते;\n'
        '  प्रष्ठौहः, प्रष्ठौहा**.\n'
        '\n'
        'SETTLED — **AND THE एच् OF THE RULE BEFORE QUALIFIES ONE OF THE\n'
        '  THREE ONLY.** **तदेतदेज्ग्रहणम् एतेरेव विशेषणम्, न पुनरेधतेः,\n'
        '  अव्यभिचारादूठश्चासंभवात्** — एधति always has its diphthong and ऊठ्\n'
        '  can never have one, so only एति needs saying that its ए is one.\n'
        '\n'
        'SETTLED — **AND WHICH RULE IT IS AN EXCEPTION TO IS SETTLED BY A\n'
        '  MAXIM.** For the ऊठ् it displaces 6.1.87; for the other two it\n'
        "  displaces 6.1.94's पररूप — but NOT 6.1.95's, though that is a\n"
        '  पररूप too: **येन नाप्राप्ते यो विधिरारभ्यते स तस्य बाधको भवति**,\n'
        '  or **पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते नोत्तरान्**. An\n'
        '  exception stated earlier reaches only what stands nearest. So **उप\n'
        '  आ इत** is **उपेतः** and not *उपैतः*, the later rule standing'
    ),
)

register(
    '6.1.90',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — आटश्च — after the augment आट्, vṛddhi before any vowel:\n'
        '  **ऐक्षिष्ट, ऐक्षत, ऐक्षिष्यत; औभीत्, औब्जीत्**. **एचीति\n'
        '  निवृत्तम्** — the एच् of 6.1.88 has lapsed.\n'
        '\n'
        'SETTLED — **AND THE च IS WHAT MAKES IT REACH FURTHER.**\n'
        '  **चकारोऽधिकविधानार्थः, उसि, ओमाङोश्च इति पररूपबाधनार्थः** — the\n'
        '  word is there to displace the पररूप of 6.1.95 and 6.1.96 as well\n'
        '  as the guṇa: **औस्रीयत्, औङ्कारीयत्, औढीयत्**'
    ),
)

register(
    '6.1.91',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — उपसर्गादृति धातौ — after a preverb ending in अ or आ and\n'
        '  before a root beginning with ऋ, vṛddhi: **उपार्च्छति, प्रार्च्छति,\n'
        '  उपार्ध्नोति**. **आद्गुणापवादः**.\n'
        '\n'
        'SETTLED — **AND उपसर्ग IS A RELATIVE NAME, NOT A LIST.**\n'
        '  **यत्क्रियायुक्ताः प्रादयस्तं प्रति गत्युपसर्गसंज्ञकाः** — प्र is\n'
        '  a preverb only with respect to the action it is joined to. In\n'
        '  **प्रर्च्छको देशः** it is not, and the rule does not reach.\n'
        '\n'
        'SETTLED — **AND धातु IS SAID THOUGH उपसर्ग IMPLIES IT.**\n'
        '  **उपसर्गग्रहणादेव धातुग्रहणे सिद्धे धातुग्रहणं\n'
        "  शाकलनिवृत्त्यर्थम्** — the word is put in to keep 6.1.128's ऋत्यकः\n"
        "  from offering Śākalya's non-junction here.\n"
        '\n'
        'SETTLED — **AND THE त् IN ऋति IS FOR THE RULE AFTER.** **तपरकरणं\n'
        '  किम्? उप ॠकारीयति उपर्कारीयति** — only a SHORT ऋ, and no ordinary\n'
        '  root begins with a long one, so the restriction only bites on the\n'
        '  denominatives 6.1.92 will take'
    ),
)

register(
    '6.1.92',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — वा सुप्यापिशलेः — where the ऋ-initial root is a\n'
        '  denominative made from a सुबन्त, the vṛddhi is a choice,\n'
        '  **आपिशलेराचार्यस्य मतेन**: **उपार्षभीयति, उपर्षभीयति;\n'
        '  उपाल्कारीयति, उपल्कारीयति**.\n'
        '\n'
        'SETTLED — **AND THE NAME IS FOR HONOUR AND NOTHING ELSE.**\n'
        '  **आपिशलिग्रहणं पूजार्थम्। वेति ह्युच्यत एव** — the वा already\n'
        '  makes it optional, and naming the teacher adds no force. The first\n'
        '  of four ācāryas named in this pāda, and three of the four are\n'
        '  named for this reason.\n'
        '\n'
        'SETTLED — **AND ऌ IS READ IN WITH ऋ.** **ऋकारऌकारयोः सावर्ण्यविधिः\n'
        '  इति ऋतीति ऌकारोऽपि गृह्यते** — which is what reaches उपल्कारीयति'
    ),
)

register(
    '6.1.93',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — ओतोऽम्शसोः — where a stem ending in ओ meets the accusative\n'
        '  अम् or शस्, आ stands for both: **गां पश्य, गाः पश्य; द्यां पश्य,\n'
        '  द्याः पश्य**.\n'
        '\n'
        'SETTLED — **AND IT DISPLACES A VṚDDHI THAT HAS NOT BEEN STATED\n'
        '  YET.** 7.1.90 makes the सर्वनामस्थान endings णित् after these\n'
        '  stems, which would give vṛddhi. **तेन नाप्राप्तायां वृद्धौ\n'
        '  अयमाकारो विधीयमानस्तां बाधते** — the substitute is laid down\n'
        '  against a vṛddhi that would otherwise reach, and so displaces it.\n'
        '\n'
        'SETTLED — **AND WHICH अम् IS MEANT IS SETTLED BY ITS COMPANY.**\n'
        '  **अमिति द्वितीयैकवचनं गृह्यते, शसा साहचर्यात्, सुपीति चाधिकारात्**\n'
        '  — it keeps company with शस् and the सुप् heading is carrying, so\n'
        '  the tense-ending अम् is not reached'
    ),
)

register(
    '6.1.94',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — एङि पररूपम् — after a preverb in अ or आ and before a root\n'
        '  beginning with ए or ओ, the LATER form stands for both: **उपेलयति,\n'
        '  प्रेलयति; उपोषति, प्रोषति**. **वृद्धिरेचि इत्यस्यापवादः**.\n'
        '\n'
        'SETTLED — **AND FOUR SUPPLEMENTS EXTEND IT WELL BEYOND ROOTS.**\n'
        '  **शकन्ध्वादिषु पररूपं वक्तव्यम्** — **शकन्धुः, कुलटा**; **सीमन्तः\n'
        '  केशेषु**, and where the sense is not hair, **सीमान्तः**. **एवे\n'
        '  चानियोगे** — **इहेव, अद्येव**, but **इहैव भव** where the sense IS\n'
        '  command. **ओत्वोष्ठयोः समासे वा** — **स्थूलोतुः, स्थूलौतुः;\n'
        '  बिम्बोष्ठी, बिम्बौष्ठी**, and outside a compound the vṛddhi is\n'
        '  fixed: **देवदत्तौष्ठं पश्य**. And **एमन्नादिषु छन्दसि** — **अपां\n'
        '  त्वेमन्, अपां त्वोद्मन्**'
    ),
)

register(
    '6.1.95',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — ओमाङोश्च — before ओम् and before the preverb आङ्, the\n'
        '  later form again: **कोमित्यवोचत्, योमित्यवोचत्; अद्योढा, कदोढा,\n'
        '  तदोढा**.\n'
        '\n'
        'SETTLED — **AND IT DISPLACES TWO DIFFERENT RULES.** Against the\n'
        '  vṛddhi of 6.1.88, and against the lengthening of 6.1.101 where the\n'
        '  two are savarṇa: **आ ऋश्यात् अर्श्यात्, अद्य अर्श्यात्\n'
        '  अद्यर्श्यात्** — one substitute, two उत्सर्ग.\n'
        '\n'
        'SETTLED — **AND IT IS THE RULE 6.1.89 CANNOT REACH.** The maxim\n'
        '  about a forward-stated exception is stated at 6.1.89 precisely so\n'
        '  that this rule stands, and उपेतः is not *उपैतः*'
    ),
)

register(
    '6.1.96',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — उस्यपदान्तात् — before the ending उस्, where the अ does\n'
        '  not end a पद, the later form: **भिन्द्युः, छिन्द्युः; अदुः,\n'
        '  अयुः**. **आद्गुणापवादः**.\n'
        '\n'
        'SETTLED — **AND अपदान्तात् IS ARGUED TO BE IDLE, AND THEN SAVED.**\n'
        '  The affix उस् can never follow a पद at all — it is added to a stem\n'
        '  that has not yet become one — so the word looks empty. Read उस् as\n'
        '  the SOUNDS उस् rather than the affix and it earns its place: **का\n'
        '  उस्रा कोस्रा, का उषिता कोषिता**, where the पदान्त अ takes the guṇa\n'
        '  instead'
    ),
)

register(
    '6.1.98',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — अव्यक्तानुकरणस्यात इतौ — where a word imitating an\n'
        '  inarticulate sound ends in अत् and इति follows, the later form\n'
        '  stands: **पटिति, घटिति, झटिति, छमिति**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI DEFINES THE TWO HALVES OF THE TERM.**\n'
        '  **अव्यक्तम् अपरिस्फुटवर्णम्, तदनुकरणं परिस्फुटवर्णमेव। केनचित्\n'
        '  सादृश्येन तदव्यक्तमनुकरोति** — the sound imitated has no distinct\n'
        '  letters and the imitation has nothing else. The word is articulate\n'
        '  speech standing for what is not.\n'
        '\n'
        'SETTLED — **AND A SUPPLEMENT KEEPS THE ONE-SYLLABLE CASES OUT.**\n'
        '  **अनेकाच इति वक्तव्यम्** — **श्रदिति** stays, and **घटदिति** in\n'
        '  the verse is read as a द-final imitation rather than as this rule\n'
        '  failing'
    ),
)

register(
    '6.1.99',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — नाम्रेडितस्यान्त्यस्य तु वा — where the imitation has been\n'
        '  doubled by 8.1.4, the later form does NOT stand for its अत् — and\n'
        '  for the final त् alone it stands optionally: **पटत्पटदिति** beside\n'
        '  **पटत्पटेति करोति**.\n'
        '\n'
        'SETTLED — **AND WHAT THE DOUBLED WORD IS TAKEN TO IMITATE DECIDES\n'
        '  IT.** **यदा तु समुदायानुकरणं तदा भवत्येव पूर्वेण पररूपम् —\n'
        '  पटत्पटिति करोति** — read the pair as one imitation and the rule\n'
        '  before applies untouched. One form, two analyses, and both are\n'
        '  attested'
    ),
)

register(
    '6.1.100',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — नित्यमाम्रेडिते डाचि — with the affix डाच् after the\n'
        '  doubled imitation, the later form is FIXED, and now for the final\n'
        '  त् and the following consonant: **पटपटा करोति, दमदमा करोति**.\n'
        '\n'
        'SETTLED — **AND THE DOUBLING HAPPENS BEFORE THE ELISION.** 5.4.57\n'
        '  gives डाच्; a vārttika on 8.1.12 doubles the word; **तच्च टिलोपात्\n'
        '  पूर्वमेवेष्यते** — and that doubling is wanted BEFORE the टि is\n'
        '  dropped, or there would be nothing left to double'
    ),
)

register(
    '6.1.102',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — प्रथमयोः पूर्वसवर्णः — before the endings of the first and\n'
        '  second cases, the long vowel HOMOGENEOUS WITH THE EARLIER sound\n'
        '  stands for both: **अग्नी, वायू; वृक्षाः, प्लक्षाः; वृक्षान्,\n'
        '  प्लक्षान्**.\n'
        '\n'
        'SETTLED — **AND प्रथमा IS READ AS COVERING TWO CASES.**\n'
        '  **प्रथमाशब्दो विभक्तिविशेषे रूढः, तत्साहचर्याद् द्वितीयापि\n'
        '  प्रथमेत्युक्ता** — the accusative is called *first* by keeping\n'
        '  company with the nominative.\n'
        '\n'
        'SETTLED — **AND THE EXCEPTION CHAIN IS WORKED OUT HERE IN FULL.**\n'
        "  6.1.97's पररूप would give वृक्षः for वृक्ष + अस्, and it does\n"
        "  displace 6.1.101's lengthening — but not THIS rule,\n"
        '  **पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते** — because an exception\n'
        '  stated earlier reaches only what stands nearest to it.\n'
        '\n'
        'SETTLED — **AND EACH WORD OF THE RULE ANSWERS A QUESTION.**\n'
        '  **पूर्वसवर्णग्रहणं किम्? अग्नी इत्यत्र पक्षे परसवर्णो मा भूत्** —\n'
        "  so that the LATER sound's homogeneous vowel is not an option.\n"
        '  **दीर्घग्रहणं किम्? त्रिमात्रे स्थानिनि\n'
        '  त्रिमात्रादेशनिवृत्त्यर्थम्** — so that a three-mora स्थानिन् does\n'
        '  not give a three-mora substitute'
    ),
)

register(
    '6.1.103',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — तस्माच्छसो नः पुंसि — after the long vowel THAT rule gave,\n'
        '  the स् of शस् becomes न् in the masculine: **वृक्षान्, अग्नीन्,\n'
        '  वायून्, कर्तॄन्**.\n'
        '\n'
        'SETTLED — **AND तस्मात् IS WHAT KEEPS गाः OUT.** The long vowel of\n'
        '  गाः comes from 6.1.93 and not from the rule before, so the न् does\n'
        '  not follow: **एतांश्चरतो गाः पश्य**.\n'
        '\n'
        'SETTLED — **AND A WORD THAT IS MASCULINE IN SENSE BUT FEMININE IN\n'
        '  FORM IS NOT REACHED.** चञ्चा for a man keeps its feminine shape by\n'
        "  1.2.51's लुपि युक्तवद् व्यक्तिवचने, **तेन नत्वं न भवति — चञ्चाः\n"
        "  पश्य, वध्रिकाः पश्य**. The rule turns on the शब्द's gender, not\n"
        "  the thing's"
    ),
)

register(
    '6.1.104',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — नादिचि — after अ or आ, and before a first- or second-case\n'
        '  ending beginning with a vowel other than अ, the homogeneous long\n'
        '  vowel does NOT stand: **वृक्षौ, प्लक्षौ; खट्वे, कुण्डे**. What\n'
        '  answers instead is 6.1.87 and 6.1.88, whose ordinary work the\n'
        '  refusal leaves untouched'
    ),
)

register(
    '6.1.105',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — दीर्घाज्जसि च — and after a long vowel the same refusal,\n'
        '  before जस् as well as before an इच्: **कुमार्यौ, कुमार्यः;\n'
        "  ब्रह्मबन्ध्वौ, ब्रह्मबन्ध्वः**. What stands instead is 6.1.77's\n"
        '  semivowel'
    ),
)

register(
    '6.1.106',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — वा छन्दसि — in the Vedic corpus the refusal of the rule\n'
        '  before is itself a choice, so the long vowel comes back:\n'
        '  **मारुतीश्चतस्रः पिण्डीः** beside **मारुत्यश्चतस्रः पिण्ड्यः**;\n'
        '  **वाराही उपानहा** beside **वाराह्यौ उपानह्यौ**'
    ),
)

register(
    '6.1.107',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — अमि पूर्वः — before the ending अम्, the EARLIER form\n'
        '  stands for both: **वृक्षम्, प्लक्षम्; अग्निम्, वायुम्**.\n'
        '\n'
        'SETTLED — **AND पूर्व IS SAID SO THAT THE VOWEL DOES NOT GROW.**\n'
        '  **पूर्वग्रहणं किम्? पूर्व एव यथा स्यात्, पूर्वसवर्णोऽन्तरतमो मा\n'
        '  भूदिति, कुमारीमित्यत्र हि त्रिमात्रः स्यात्** — the earlier form\n'
        '  ITSELF, not the homogeneous vowel nearest to it; otherwise the ई\n'
        '  of कुमारीम् would come out three morae long, being substituted for\n'
        '  ई and अ together'
    ),
)

register(
    '6.1.108',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — संप्रसारणाच्च — after a vocalised semivowel the earlier\n'
        '  form again: **इष्टम्, उप्तम्, गृहीतम्**. And this is the rule\n'
        '  whose words bound the अचि heading opened at 6.1.77.\n'
        '\n'
        'SETTLED — **AND THE RULE IS WHAT MAKES संप्रसारण WORTH DOING AT\n'
        '  ALL.** **संप्रसारणविधानसामर्थ्याद् विगृहीतस्य श्रवणे प्राप्ते\n'
        '  पूर्वत्वं विधीयते** — without it, वप् + त would be उ · अप् · त,\n'
        '  and 6.1.77 would turn the उ back into व् and undo the whole\n'
        '  operation. **परपूर्वत्वविधाने सत्यर्थवत् संप्रसारणविधानम्.**\n'
        '\n'
        'SETTLED — **AND IT DOES NOT REACH A JUNCTION MADE LATER.**\n'
        '  **अन्तरङ्गे चाचि कृतार्थं वचनमिति बाह्ये पश्चात् संनिपतिते\n'
        '  पूर्वत्वं न भवति** — शकह्वौ, शकह्वर्थम्'
    ),
)

register(
    '6.1.109',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — एङः पदान्तादति — where ए or ओ ends a पद and a short अ\n'
        '  follows, the earlier form stands: **अग्नेऽत्र, वायोऽत्र**.\n'
        "  **अयवादेशयोरयमपवादः** — an exception to 6.1.78's अय् and अव्.\n"
        '\n'
        'SETTLED — **AND THE त् OF अति IS WHAT KEEPS वायवायाहि OUT.**\n'
        '  **तपरकरणं किम्? वायवायाहि** — a long आ following is not reached,\n'
        '  and 6.1.78 takes it'
    ),
)

register(
    '6.1.110',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — ङसिङसोश्च — and before the ablative and genitive singular,\n'
        '  whether or not the ए or ओ ends a पद: **अग्नेरागच्छति,\n'
        '  वायोरागच्छति; अग्नेः स्वम्, वायोः स्वम्**. **अपदान्तार्थ आरम्भः**\n'
        '  — the rule exists for exactly the case the one before it could not\n'
        '  reach'
    ),
)

register(
    '6.1.111',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — ऋत उत् — after a ऋ-final stem and before the same two\n'
        '  endings, उ stands for both: **होतुरागच्छति, होतुः स्वम्**. The\n'
        '  last rule the एकादेश heading reaches.\n'
        '\n'
        'SETTLED — **AND THE उ TAKES A र् AFTER IT THOUGH IT REPLACES TWO\n'
        '  SOUNDS.** **द्वयोः षष्ठीनिर्दिष्टयोः स्थाने यः स\n'
        '  लभतेऽन्यतरव्यपदेशम्** — a substitute standing for two things named\n'
        '  in the genitive may be called the substitute of either. So\n'
        "  1.1.51's उरण् रपरः reaches it, the र् is put in, and 8.2.24's रात्\n"
        '  सस्य then drops the स्'
    ),
)

register(
    '6.1.112',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — ख्यत्यात् परस्य — after सखि and पति with their इ already\n'
        '  turned into य्, the same उ for the अ of the ending:\n'
        '  **सख्युरागच्छति, सख्युः स्वम्; पत्युरागच्छति, पत्युः स्वम्**. And\n'
        "  this rule's words are what bound the एकादेश heading.\n"
        '\n'
        'SETTLED — **AND THE ODD SHAPE IN THE RULE REACHES TWO MORE WORDS.**\n'
        '  ख्य covers खी and त्य covers ती, so the denominatives reach it\n'
        '  too: सखीयति gives **सख्युः**, लूनीयति gives **लून्युः** — and the\n'
        "  न् of लूनी counts as the त् it replaced, 8.2.44's substitution\n"
        '  being असिद्ध by 8.2.1.\n'
        '\n'
        'SETTLED — **AND NAMING SHAPES RATHER THAN WORDS IS WHAT KEEPS\n'
        '  COMPOUNDS OUT.** **विकृतनिर्देशादेवेह न भवति — अतिसखेरागच्छति** —\n'
        "  1.4.13's घि is refused to सखि alone and not to what ends in it, so\n"
        '  the compound never shows the ख्य the rule names'
    ),
)

register(
    '6.1.113',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — अतो रोरप्लुतादप्लुते — where रु stands between a short अ\n'
        '  and a short अ, उ replaces it: **वृक्षोऽत्र, प्लक्षोऽत्र**.\n'
        '\n'
        'SETTLED — **AND IT DISPLACES A RULE OF THE त्रिपादी WITHOUT BEING\n'
        '  BLOCKED BY IT.** 8.3.17 would give य् instead.\n'
        '  **रुत्वमप्याश्रयत्वात् पूर्वत्रासिद्धम् इत्यसिद्धं न भवति** — the\n'
        '  रु this rule leans on comes from 8.2.66, which is itself in the\n'
        '  त्रिपादी; being what the rule RESTS ON rather than what it is\n'
        '  stated against, it is not held back by 8.2.1.\n'
        '\n'
        'SETTLED — **AND अप्लुत IS SAID TWICE FOR TWO REASONS.**\n'
        '  **अप्लुतादिति किम्? सुस्रोत३ अत्र न्वसि। अप्लुत इति किम्? तिष्ठतु\n'
        '  पय अ३श्विन्** — a prolated vowel on either side takes the rule\n'
        '  away, and there **प्लुतस्य असिद्धत्वाद् उत्वं प्राप्नोति** unless\n'
        '  both are said'
    ),
)

register(
    '6.1.114',
    apply=one_for_both,
    codification=_ONE_FOR_BOTH,
    notes=(
        'SETTLED — हशि च — and before a soft consonant the same उ for रु:\n'
        '  **पुरुषो याति, पुरुषो हसति, पुरुषो ददाति**. The one rule of the\n'
        '  pāda that acts before a consonant rather than a vowel'
    ),
)


_STANDS_OPEN = (
    'stands_open(stem, after=..., before=..., result=..., '
    'teacher=..., chandasi=..., yajusi=...) -> which rule of '
    '6.1.115–134 holds the junction open, and what it leaves.'
)

register(
    '6.1.115',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — प्रकृत्यान्तःपादमव्यपरे — where ए or ओ meets a short अ\n'
        '  inside a Vedic पाद, and no व् or य् follows that अ, both stand as\n'
        '  they are: **ते अग्ने अश्वमायुञ्जन्; उपप्रयन्तो अध्वरम्; शिरो\n'
        '  अपश्यम्; सुजाते अश्वसूनृते**.\n'
        '\n'
        'SETTLED — **AND प्रकृति IS DEFINED BEFORE IT IS USED.**\n'
        '  **प्रकृतिरिति स्वभावः कारणं वाभिधीयते** — the sounds keep their\n'
        '  own nature, or their character as causes: **स्वभावेनावतिष्ठते,\n'
        '  कारणात्मना वा भवति, न विकारमापद्यते**. The first rule of the pāda\n'
        '  that says nothing happens.\n'
        '\n'
        'SETTLED — **AND पाद MEANS A VEDIC FOOT AND NOT A VERSE-LINE.**\n'
        '  **पादशब्देन च ऋक्पादस्यैव ग्रहणमिष्यते, न तु श्लोकपादस्य** — and\n'
        '  the case is settled by **कया मती कुत एतास एतेऽर्चन्ति**, where the\n'
        "  junction falls at the foot's edge and the rule fails.\n"
        '\n'
        'SETTLED — **AND SOME READ THE RULE WITH A न् AND MEAN SOMETHING MUCH\n'
        '  LARGER.** **केचिदिदं सूत्रं नान्तःपादमव्यपर इति पठन्ति, ते\n'
        '  संहितायामिह यदुच्यते तस्य सर्वस्य प्रतिषेधं वर्णयन्ति** — on that\n'
        '  reading the rule refuses EVERYTHING 6.1.72 opened. The vṛtti\n'
        '  reports it without adopting it'
    ),
)

register(
    '6.1.116',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च — seven words\n'
        '  that hold the junction open THOUGH a व् or य् follows their अ,\n'
        '  which is the one thing 6.1.115 refuses on: **नो अव्यात्; मित्रमहो\n'
        '  अवद्यात्; मा शिवासो अवक्रमुः; ते नो अव्रताः; शतधारो अयं मणिः; ते\n'
        '  नो अवन्तु पितरः; कुशिकासो अवस्यवः**. A list stated for no other\n'
        '  reason than to defeat one word of the rule before'
    ),
)

register(
    '6.1.117',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — यजुष्युरः — in the Yajurveda the word उरस् keeps its ओ and\n'
        '  the अ after it: **उरो अन्तरिक्षम्**.\n'
        '\n'
        'SETTLED — **AND THE RULE EXISTS BECAUSE THAT CORPUS HAS NO\n'
        '  VERSE-FEET.** **यजुषि पादानामभावाद् अनन्तःपादार्थं वचनम्** —\n'
        '  6.1.115 wants a position inside a पाद, and there are none to be\n'
        '  inside, so the whole run from here to 6.1.121 is stated over again\n'
        '  for prose.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI REPORTS A SECOND READING OF THE RULE\n'
        '  ITSELF.** **अपरे यजुष्युरो इति सूत्रं पठन्ति** — some read उरो as\n'
        '  the vocative of उरु rather than as उरस् with its स् gone, and cite\n'
        '  **उरो अन्तरिक्षे सजूः** for it'
    ),
)

register(
    '6.1.118',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे — six\n'
        '  more for the Yajurveda: **आपो अस्मान् मातरः शुन्धयन्तु; जुषाणो\n'
        '  अप्तुराज्यस्य; वृष्णो अंशुभ्यां गभस्तिपूतः; वर्षिष्ठे अधि नाके;\n'
        '  अम्बे अम्बाले अम्बिके**, the last two only where अम्बिका follows.\n'
        '\n'
        'SETTLED — **AND BEING LISTED HERE KEEPS ANOTHER RULE OFF THEM.**\n'
        '  **अस्मादेव निपातनाद् अम्बार्थनद्योर्ह्रस्वः इति ह्रस्वत्वं न\n'
        '  भवति** — 7.3.107 would shorten a vocative in अम्बा, and the words\n'
        '  are cited here in their long form, so it does not'
    ),
)

register(
    '6.1.119',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — अङ्ग इत्यादौ च — and where अङ्गे is followed by अङ्गे,\n'
        '  both the ए and the अ stand: **ऐन्द्रः प्राणो अङ्गेअङ्गे अदीध्यत्;\n'
        '  ऐन्द्रः प्राणो अङ्गेअङ्गे निदीध्यत्**. The rule holds the junction\n'
        '  open twice over in one phrase'
    ),
)

register(
    '6.1.120',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — अनुदात्ते च कुधपरे — in the Yajurveda, where the short अ\n'
        '  is अनुदात्त and a guttural or a ध follows it, the junction stands\n'
        '  open: **अयं नो अग्निः; अयं सो अध्वरः**. Two conditions at once,\n'
        '  one on the accent of the vowel and one on what comes after it, and\n'
        '  the vṛtti gives a counter-example for each'
    ),
)

register(
    '6.1.121',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — अवपथासि च — and before the word अवपथाः with its अ\n'
        '  अनुदात्त: **त्री रुद्रेभ्यो अवपथाः**.\n'
        '\n'
        'SETTLED — **AND WHERE THAT WORD IS ACCENTED DECIDES IT.** The अ is\n'
        "  अनुदात्त by 8.1.28's तिङ्ङतिङः; put यद् in front and 8.1.30's\n"
        '  निपातैर्यद्यदिहन्त… refuses that निघात, the accent returns, and\n'
        "  the junction closes: **यद्रुद्रेभ्योऽवपथाः**. One word's accent,\n"
        '  and the sandhi goes the other way'
    ),
)

register(
    '6.1.122',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — सर्वत्र विभाषा गोः — after गो the short अ may stand open,\n'
        '  and सर्वत्र means in ordinary speech as well as in the corpus:\n'
        '  **गोऽग्रम्, गो अग्रम्**; and in the corpus **अपशवो वा अन्ये\n'
        '  गोअश्वेभ्यः, पशवो गोअश्वान्**. The one प्रकृतिभाव rule of the run\n'
        '  that is not confined to the Veda'
    ),
)

register(
    '6.1.123',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — अवङ् स्फोटायनस्य — and instead of holding the junction\n'
        '  open, स्फोटायन puts अवङ् in for the ओ of गो before any vowel:\n'
        '  **गवाग्रम्, गवाजिनम्, गवौदनम्** beside **गोऽग्रम्, गोऽजिनम्,\n'
        '  गवोदनम्**. **अतीति निवृत्तम्** — the short अ of the rule before\n'
        '  has lapsed, so this one reaches every vowel.\n'
        '\n'
        'SETTLED — **AND THE NAME IS FOR HONOUR, NOT FOR THE OPTION.**\n'
        '  **स्फोटायनग्रहणं पूजार्थम्, विभाषेत्येव हि वर्तते** — the विभाषा\n'
        '  was already carrying. The second of four ācāryas named in this\n'
        '  pāda and the second whose name adds nothing but respect.\n'
        '\n'
        'SETTLED — **AND THE OPTION IS SETTLED WHERE IT MATTERS.**\n'
        '  **व्यवस्थितविभाषेयम्, तेन गवाक्ष इत्यत्र नित्यमवङ् भवति** — in\n'
        '  गवाक्ष the substitute is fixed.\n'
        '\n'
        'SETTLED — **AND THE SUBSTITUTE CARRIES ITS OWN ACCENT.**\n'
        '  **आद्युदात्तश्चायमादेशो निपात्यते**, and that accent survives in a\n'
        "  बहुव्रीहि — **गवाग्रः** — where elsewhere 6.1.223's compound-final\n"
        '  उदात्त would displace it'
    ),
)

register(
    '6.1.124',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — इन्द्रे च नित्यम् — before a vowel of the word इन्द्र the\n'
        '  substitute is FIXED: **गवेन्द्रः, गवेन्द्रयज्ञस्वरः**. The word\n'
        '  नित्यम् is what takes the option away, as नित्यम् did at 6.1.57\n'
        '  and 6.1.100 — and the vṛtti notes that **नित्य** is not read here\n'
        '  by everyone'
    ),
)

register(
    '6.1.125',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — प्लुतप्रगृह्या अचि — a प्लुत vowel and a प्रगृह्य one\n'
        '  stand open before any vowel: **देवदत्त३ अत्र न्वसि; अग्नी इति,\n'
        '  वायू इति, खट्वे इति, माले इति**.\n'
        '\n'
        'SETTLED — **AND THE त्रिपादी IS NOT असिद्ध HERE.** प्लुत is laid\n'
        '  down in the last three pādas and 8.2.1 would make it invisible to\n'
        '  a rule of this one. **आश्रयादत्र प्लुतः सिद्धः** — being what the\n'
        '  rule RESTS on rather than what it works against, it counts.\n'
        '\n'
        'SETTLED — **AND अचि IS SAID AGAIN THOUGH IT WAS ALREADY CARRYING.**\n'
        '  **पुनरज्ग्रहणम् आदेशनिमित्तस्याचः परिग्रहार्थम्** — the vowel must\n'
        '  be the one that would CAUSE the change. In जानु उ अस्य the\n'
        '  following अ is no cause of the lengthening, so the lengthening\n'
        '  happens anyway.\n'
        '\n'
        'SETTLED — **AND नित्यम् CARRIES DOWN FROM 6.1.124 TO KEEP ŚĀKALYA\n'
        '  OFF.** **नित्यग्रहणमिहानुवर्तते। प्लुतप्रगृह्याणां नित्यमयमेव\n'
        '  प्रकृतिभावो यथा स्याद् इकोऽसवर्णे इत्येतन् मा भूत्** — otherwise\n'
        '  6.1.127 would offer a shortened form beside it'
    ),
)

register(
    '6.1.126',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — आङोऽनुनासिकश्छन्दसि — in the corpus the preverb आ becomes\n'
        '  nasalised before a vowel, and stands open: **अभ्र आँ अपः; गभीर आँ\n'
        '  उग्रपुत्रे जिघांसतः**. And **केचिद् आङोऽनुनासिकश्छन्दसि बहुलम्\n'
        '  इत्यधीयते** — some read बहुलम् into it, which is what admits\n'
        '  **इन्द्रो बाहुभ्यामातरत्**'
    ),
)

register(
    '6.1.127',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च — शाकल्य holds that an इक्\n'
        '  before an unlike vowel stands open, AND is shortened if it was\n'
        '  long: **दधि अत्र, मधु अत्र, कुमारि अत्र, किशोरि अत्र** beside\n'
        '  **दध्यत्र, मध्वत्र, कुमार्यत्र**.\n'
        '\n'
        'SETTLED — **AND THE NAME IS FOR HONOUR AGAIN.** **शाकल्यस्य ग्रहणं\n'
        '  पूजार्थम्। आरम्भसामर्थ्यादेव हि यणादेशेन सह विकल्पः सिद्धः** — the\n'
        "  rule's mere existence beside 6.1.77 already makes the two\n"
        '  alternatives.\n'
        '\n'
        'SETTLED — **AND TWO SUPPLEMENTS KEEP IT OUT OF TWO PLACES.**\n'
        '  **सिन्नित्यसमासयोः शाकलप्रतिषेधो वक्तव्यः** — before a सित् affix\n'
        '  (**ऋत्वियः**) and in a fixed compound (**व्याकरणम्,\n'
        '  कुमार्यर्थम्**). And **ईषाअक्षादिषु छन्दसि प्रकृतिभावमात्रं\n'
        '  वक्तव्यम्** — **इषा अक्षो हिरण्ययः; पथा अगमन्**, where the\n'
        '  junction stands open WITHOUT the shortening'
    ),
)

register(
    '6.1.128',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — ऋत्यकः — and before ऋ the same, now for an अक् and not\n'
        '  only an इक्: **खट्व ऋश्यः, माल ऋश्यः, कुमारि ऋश्यः, होतृ ऋश्यः**.\n'
        '\n'
        'SETTLED — **AND THE RULE IS STATED FOR TWO THINGS THE ONE BEFORE IT\n'
        '  COULD NOT DO.** **सवर्णार्थमनिगर्थं च वचनम्** — it reaches a\n'
        '  savarṇa pair, which 6.1.127 excluded, and it reaches अ and आ,\n'
        '  which are not इक् at all'
    ),
)

register(
    '6.1.129',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — अप्लुतवदुपस्थिते — before the इति of a पदपाठ, a प्लुत\n'
        "  vowel is treated LIKE a non-प्लुत one, so 6.1.125's प्रकृतिभाव\n"
        '  does not hold and the junction closes: **सुश्लोक३ इति सुश्लोकेति;\n'
        '  सुमङ्गल३ इति सुमङ्गलेति**.\n'
        '\n'
        'SETTLED — **AND उपस्थित IS DEFINED AS A THING THE ṚṢIS DID NOT DO.**\n'
        '  **उपस्थितं नाम अनार्ष इतिकरणः, समुदायाद् अवच्छिद्य पदं येन\n'
        '  स्वरूपेऽवस्थाप्यते** — the इति that a later analyst puts after a\n'
        '  word to cut it out of the line and hold it in its own shape. The\n'
        '  rule is about the पदपाठ and not about the text.\n'
        '\n'
        'SETTLED — **AND वत् IS SAID RATHER THAN अप्लुतः.** **वत्करणं किम्?\n'
        '  अप्लुत इत्युच्यमाने प्लुत एव प्रतिषिध्यते** — say the प्लुत IS\n'
        '  non-प्लुत and it ceases to be one, and then a vowel that is both\n'
        '  प्लुत and प्रगृह्य would lose its length as well: **अग्नी३ इति,\n'
        '  वायू३ इति**. *Treated like* keeps the length and takes only the\n'
        '  प्रकृतिभाव'
    ),
)

register(
    '6.1.130',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — ई३ चाक्रवर्मणस्य — चाक्रवर्मण holds that a प्लुत ई३ before\n'
        '  a vowel is treated like a non-प्लुत one: **अस्तु हीत्यब्रूताम्**\n'
        '  beside **अस्ति ही३ इत्यब्रूताम्**; **चिनु हीदम्** beside **चिनु\n'
        '  ही३ इदम्**.\n'
        '\n'
        'SETTLED — **AND THIS NAME IS NOT FOR HONOUR.** **चाक्रवर्मणग्रहणं\n'
        '  विकल्पार्थम्** — the name is what MAKES the rule a choice, where\n'
        '  the other three teachers of this pāda are named **पूजार्थम्**\n'
        '  beside a वा that already said it. One word of commentary, and the\n'
        '  four names stop being one thing.\n'
        '\n'
        'SETTLED — **AND IT IS AN उभयत्रविभाषा.** **तदुपस्थिते निवृत्त्यर्थम्\n'
        '  अनुपस्थिते प्राप्त्यर्थम्** — before इति it LOOSENS what 6.1.129\n'
        "  made fixed; elsewhere it SUPPLIES against 6.1.125's प्रकृतिभाव.\n"
        '  And **ईकारादन्यत्राप्ययमप्लुतवद्भाव इष्यते** — **वशा३ इयम्,\n'
        '  वशेयम्**'
    ),
)

register(
    '6.1.131',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — दिव उत् — where दिव् is a पद, उ stands for its final:\n'
        '  **द्युकामः, द्युमान्, विमलद्यु दिनम्, द्युभ्याम्, द्युभिः**.\n'
        '\n'
        'SETTLED — **AND WHICH दिव् IS MEANT IS SETTLED BY A MAXIM ABOUT\n'
        '  MARKERS.** **दिव इति प्रातिपदिकं गृह्यते न धातुः,\n'
        '  सानुबन्धकत्वात्**, and **निरनुबन्धकग्रहणात्** — a word cited\n'
        '  without markers means the one that has none. The root is दिवु, so\n'
        "  it is not reached, and 6.4.19's ऊठ् gives **अक्षद्यूभ्याम्**\n"
        '  instead.\n'
        '\n'
        'SETTLED — **AND THE त् IN उत् IS WHAT KEEPS THAT ऊठ् OFF HERE TOO.**\n'
        '  **तपरकरणमूठो निवृत्त्यर्थम्** — a SHORT उ, since ऊठ् is stated\n'
        '  later and would otherwise win on परत्व'
    ),
)

register(
    '6.1.132',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — एतत्तदोः सुलोपोऽकोरनञ्समासे हलि — the nominative singular\n'
        '  स् of एतद् and तद् is dropped before a consonant: **एष ददाति, स\n'
        '  ददाति; एष भुङ्क्ते, स भुङ्क्ते**.\n'
        '\n'
        'SETTLED — **AND अकोः IS NEEDED BECAUSE OF A MAXIM.**\n'
        '  **तन्मध्यपतितस्तद्ग्रहणेन गृह्यते** — a form with something\n'
        '  inserted INTO it is still reached by the name of the thing it was\n'
        '  inserted into, so एषक and सक would count as एतद् and तद् despite\n'
        '  the क. The refusal is stated to stop that: **एषको ददाति, सको\n'
        '  ददाति**.\n'
        '\n'
        'SETTLED — **AND अनञ्समासे TURNS ON WHERE THE MEANING SITS.**\n'
        '  **उत्तरपदार्थप्रधानत्वाद् नञ्समासस्यैतत्तदोरेवात्र संबद्धः\n'
        '  सुशब्दः** — in a नञ् compound the second member carries the sense,\n'
        "  so the स् there really is एतद्'s and would be dropped; the rule\n"
        '  says it is not: **अनेषो ददाति, असो ददाति**'
    ),
)

register(
    '6.1.133',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — स्यश्छन्दसि बहुलम् — in the corpus the nominative singular\n'
        '  ending is variously dropped after स्य before a consonant: **उत स्य\n'
        '  वाजी क्षिपणिं तुरण्यति; एष स्य ते पवत इन्द्र सोमः** — and **न च\n'
        '  भवति — यत्र स्यो निपतेत्**'
    ),
)

register(
    '6.1.134',
    apply=stands_open,
    codification=_STANDS_OPEN,
    notes=(
        'SETTLED — सोऽचि लोपे चेत् पादपूरणम् — the ending of सस् is dropped\n'
        '  before a vowel, IF dropping it fills out the foot: **सेदु राजा\n'
        '  क्षयति चर्षणीनाम्; सौषधीरनुरुध्यसे**. A condition on the METRE,\n'
        '  and the only one in the pāda.\n'
        '\n'
        'SETTLED — **AND अचि IS SAID FOR CLARITY RATHER THAN FOR FORCE.**\n'
        '  **अचीति विस्पष्टार्थम्** — before a consonant the syllable count\n'
        '  would not change and the metre would gain nothing; it is the\n'
        '  sandhi with a vowel that shortens the line.\n'
        '\n'
        "SETTLED — **AND SOME READ पाद AS A ŚLOKA'S FOOT TOO.**\n"
        '  **पादग्रहणेनात्र श्लोकपादस्यापि ग्रहणं केचिदिच्छन्ति**, and then\n'
        '  the verse **सैष दाशरथी रामः सैष राजा युधिष्ठिरः** is reached as\n'
        '  well. 6.1.115 took पाद the other way, and the two readings stand\n'
        '  side by side in one pāda'
    ),
)


_SUT_FOR = (
    'sut_for(stem, pre=..., result=..., uttarapada=..., agent=..., '
    'across=..., mantra=...) -> which rule of 6.1.135–157 puts the '
    'augment स् in before a क्.'
)

register(
    '6.1.135',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — सुट् कात् पूर्वः — **अधिकारोऽयम्, पारस्करप्रभृतीनि च\n'
        '  संज्ञायाम् इति यावत्। इत उत्तरं यद् वक्ष्यामस्तत्र सुडिति कात्\n'
        '  पूर्व इति चैतदधिकृतं वेदितव्यम्** — every rule to 6.1.157 is read\n'
        '  with *the augment स् before the क्*. **संस्कर्ता, संस्कर्तुम्,\n'
        '  संस्कर्तव्यम्**. And the heading is bounded by its own last rule,\n'
        "  as 6.1.45's आकार was.\n"
        '\n'
        'SETTLED — **AND कात् पूर्वः IS SAID TO SHOW THE AUGMENT IS NOT PART\n'
        '  OF THE ROOT.** **कात् पूर्वग्रहणं सुटोऽभक्तत्वज्ञापनार्थम्** — and\n'
        '  four things follow. **तथाहि संस्कृषीष्ट संस्क्रियत इति\n'
        '  संयोगादिलक्षणाविड्गुणौ न भवतः**: the root is not cluster-initial,\n'
        "  so 7.4.10's condition fails and neither the इट् nor the guṇa\n"
        '  comes.\n'
        '\n'
        'SETTLED — **AND THEN AN OBJECTION, AND ITS ANSWER.** **तिङ्ङतिङः इति\n'
        '  निघातोऽपि तर्हि न प्राप्नोति, सुटा व्यवहितत्वात्?** — if the स्\n'
        '  really stands apart, does it not also stand BETWEEN and block\n'
        "  8.1.28's accent rule? **स्वरविधौ व्यञ्जनमविद्यमानवद् इति वचनाद्\n"
        '  नास्ति व्यवधानम्**: where an accent is concerned a consonant\n'
        '  counts as absent.\n'
        '\n'
        'SETTLED — **AND A THIRD CASE GOES THE OTHER WAY.** **संचस्करतुः,\n'
        '  संचस्करुरिति गुणः कथम्? तन्मध्यपतितस्तद्ग्रहणेन गृह्यते इति** —\n'
        '  there the guṇa DOES reach, because a form with something inserted\n'
        '  into it is still named by what it was inserted into.\n'
        '\n'
        'SETTLED — **AND THE ट् IS FOR A RULE THREE ADHYĀYAS LATER.**\n'
        '  **टित्करणं सुट्स्तुस्वञ्जाम् इत्यत्र विशेषणार्थम्** — 8.3.70 names\n'
        '  this augment by that marker'
    ),
)

register(
    '6.1.136',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — अडभ्यासव्यवायेऽपि — the augment goes in before the क् even\n'
        '  where the अट् of the imperfect or the reduplicated syllable stands\n'
        '  between: **समस्करोत्, समस्कार्षीत्; संचस्कार, परिचस्कार**.\n'
        '\n'
        "SETTLED — **AND THE RULE IS NOT PĀṆINI'S.** It is made out of two\n"
        '  vārttikas, **अड्व्यवाय उपसंख्यानम्** and **अभ्यासव्यवाये च**, read\n'
        '  together as one sūtra.\n'
        '\n'
        'SETTLED — **AND IT IS NEEDED BECAUSE OF WHAT 6.1.135 ESTABLISHED.**\n'
        '  The objection: **पूर्वं धातुरुपसर्गेण युज्यते** — root and preverb\n'
        '  join first, so the सुट् is already in when the अट् and the\n'
        '  doubling arrive; why say this? Because **अभक्तश्च सुडित्युक्तम्,\n'
        '  ततः सकारादुत्तरावडभ्यासावनिष्टे देशे स्याताम्** — the augment\n'
        '  standing apart, the अट् and the copy would land AFTER it, in the\n'
        '  wrong place. The rule puts them before it and the augment back in\n'
        '  front of the क्'
    ),
)

register(
    '6.1.137',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — संपर्युपेभ्यः करोतौ भूषणे — after सम्, परि or उप, before\n'
        '  करोति, in the sense of ADORNING: **संस्कर्ता, परिष्कर्ता,\n'
        '  उपस्कर्ता**.\n'
        '\n'
        "SETTLED — **AND TWO LATER RULES FINISH THE FORMS.** 8.3.70's षत्व\n"
        '  makes the स् a ष् after परि and उप; and a supplement, **संपुंकानां\n'
        '  सत्वम्**, turns the म् of सम् into a स् with the vowel before it\n'
        '  nasalised.\n'
        '\n'
        'SETTLED — **AND THE SENSE-CONDITION IS ADMITTED TO LEAK.**\n'
        '  **संपूर्वस्य क्वचिदभूषणेऽपि सुडिष्यते, संस्कृतमन्नमिति** — after\n'
        '  सम् the augment is wanted sometimes where the sense is NOT\n'
        '  adorning, and the vṛtti says so rather than stretching भूषण to\n'
        '  cover cooked food'
    ),
)

register(
    '6.1.138',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — समवाये च — and in the sense of coming together: **तत्र नः\n'
        '  संस्कृतम्; तत्र नः परिष्कृतम्; तत्र न उपस्कृतम्**, which the vṛtti\n'
        '  glosses **समुदितम्**. **समवायः समुदायः** — the word means an\n'
        '  aggregate, and the three preverbs of the rule before carry down'
    ),
)

register(
    '6.1.139',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — उपात् प्रतियत्नवैकृतवाक्याध्याहारेषु — after उप alone, in\n'
        '  three further senses, and the vṛtti defines each before using it.\n'
        '\n'
        'SETTLED — **प्रतियत्न**: **सतो गुणान्तराधानम् आधिक्याय वृद्धस्य वा\n'
        '  तादवस्थ्याय समीहा** — putting a further quality into something\n'
        '  that already exists, to increase it or to hold it as it is.\n'
        '  **एधोदकस्योपस्कुरुते; काण्डं गुडस्य उपस्कुरुते**.\n'
        '\n'
        "SETTLED — **वैकृत**: **विकृतमेव वैकृतम्**, with 5.4.38's प्रज्ञादि\n"
        '  अण् adding nothing. **उपस्कृतं भुङ्क्ते, उपस्कृतं गच्छति**.\n'
        '\n'
        'SETTLED — **वाक्याध्याहार**: **गम्यमानार्थस्य वाक्यस्य\n'
        '  स्वरूपेणोपादानम्** — putting into words a sentence that was only\n'
        '  implied. **उपस्कृतं जल्पति, उपस्कृतमधीते**'
    ),
)

register(
    '6.1.140',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — किरतौ लवने — before किरति and in the sense of reaping:\n'
        '  **उपस्कारं मद्रका लुनन्ति; उपस्कारं काश्मीरका लुनन्ति** —\n'
        '  **विक्षिप्य लुनन्ति**, they scatter as they cut. And **णमुलत्र\n'
        '  वक्तव्यः**, the affix in these forms being णमुल्'
    ),
)

register(
    '6.1.141',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — हिंसायां प्रतेश्च — and after प्रति as well as उप, where\n'
        '  harm is meant: **उपस्कीर्णं हन्त ते वृषल भूयात्; प्रतिस्कीर्णं\n'
        '  हन्त ते वृषल भूयात्** — the vṛtti glossing it **तथा ते वृषल\n'
        '  विक्षेपो भूयाद् यथा हिंसाम् अनुबध्नाति**, a scattering that\n'
        '  carries harm with it'
    ),
)

register(
    '6.1.142',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — अपाच्चतुष्पाच्छकुनिष्वालेखने — after अप, of a four-footed\n'
        '  animal or a bird scratching the ground: **अपस्किरते वृषभो हृष्टः;\n'
        '  अपस्किरते कुक्कुटो भक्ष्यार्थी; अपस्किरते श्वा आश्रयार्थी** —\n'
        '  **आलिख्य विक्षिपति**, it scrapes and throws.\n'
        '\n'
        'SETTLED — **AND THE THREE REASONS FOR SCRATCHING ARE THEMSELVES A\n'
        '  CONDITION.** **हर्षजीविकाकुलायकरणेष्विति वक्तव्यम्** — out of\n'
        '  gladness, for food, or to make a nest, and no other. The same\n'
        '  three are what give the root its ātmanepada by a vārttika on\n'
        '  1.3.21, so one condition serves two rules'
    ),
)

register(
    '6.1.143',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — कुस्तुम्बुरूणि जातिः — the word is laid down with its\n'
        '  सुट्, and only where a SPECIES is meant: **कुस्तुम्बुरुर् नाम\n'
        '  ओषधिजातिर्धान्यकम्**, coriander, and its seeds besides.\n'
        '\n'
        'SETTLED — **AND THE GENDER IN THE RULE IS NOT MEANT.**\n'
        '  **सूत्रनिर्देशे नपुंसकलिङ्गमविवक्षितम्** — the word is cited in\n'
        '  the neuter and is not confined to it'
    ),
)

register(
    '6.1.144',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — अपरस्पराः क्रियासातत्ये — laid down with its सुट् where an\n'
        '  action goes on without a break: **अपरस्पराः सार्था गच्छन्ति** —\n'
        '  **सन्ततमविच्छेदेन गच्छन्ति**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI STOPS TO EXPLAIN A WORD IN ITS OWN\n'
        '  GLOSS.** **किमिदं सातत्यमिति? सततस्य भावः सातत्यम्। कथं सततम्?** —\n'
        '  how is it सतत and not संतत? By a verse listing four places a nasal\n'
        '  or a vowel drops: **लुम्पेदवश्यमः कृत्ये तुं काममनसोरपि। समो वा\n'
        '  हितततयोर् मांसस्य पचि युड्घञोः॥** — the म् of सम् goes optionally\n'
        '  before हित and तत, which gives सहित and सतत'
    ),
)

register(
    '6.1.145',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — गोष्पदं सेवितासेवितप्रमाणेषु — laid down with its सुट् and\n'
        '  its ष्, in three senses: land cows go over — **गोष्पदो देशः**;\n'
        '  land they do not — **अगोष्पदान्यरण्यानि**; and a measure —\n'
        '  **गोष्पदमात्रं क्षेत्रम्, गोष्पदपूरं वृष्टो देवः**, where **नात्र\n'
        '  गोष्पदं स्वार्थप्रतिपादनार्थम् उपादीयते; किं तर्हि? क्षेत्रस्य\n'
        '  वृष्टेश्च परिच्छेत्तुम् इयत्ताम्**.\n'
        '\n'
        'SETTLED — **AND असेवित IS ARGUED FOR, AGAINST AN OBVIOUS\n'
        '  OBJECTION.** Why state it, when न गोष्पद gives अगोष्पद? Because a\n'
        '  नञ् compound means what is LIKE the thing and not it: **यत्र तु\n'
        '  सेवितप्रसङ्गोऽस्ति तत्रैव स्याद् अगोष्पदमिति, यत्र त्वत्यन्तासंभव\n'
        '  एव तत्र न स्यात्** — so अगोष्पद would reach only land cows COULD\n'
        '  graze and do not. **यानि हि महान्त्यरण्यानि येषु\n'
        '  गवामत्यन्तासंभवस्तान्येवमुच्यन्ते**: the word is stated to reach\n'
        '  the deep forests where they never could'
    ),
)

register(
    '6.1.146',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — आस्पदं प्रतिष्ठायाम् — laid down where a standing or a\n'
        '  position is meant: **आस्पदमनेन लब्धम्**. And the sense is defined\n'
        '  before it is used — **आत्मयापनाय स्थानं प्रतिष्ठा**, the place by\n'
        '  which one keeps oneself going'
    ),
)

register(
    '6.1.147',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — आश्चर्यमनित्ये — laid down where what is wonderful is\n'
        '  meant, and the vṛtti derives the sense from the word: **अनित्यतया\n'
        '  विषयभूतया अद्भुतत्वमिह लक्ष्यते** — what astonishes does so by\n'
        '  being uncommon. **आश्चर्यं यदि स भुञ्जीत; आश्चर्यं यदि सोऽधीयीत**\n'
        "  — **चित्रमद्भुतम्**. The यत् is a vārttika's on 3.1.100 and the\n"
        "  सुट् is this rule's"
    ),
)

register(
    '6.1.148',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — वर्चस्केऽवस्करः — laid down for excrement, and the vṛtti\n'
        '  reads the sense-word out: **कुत्सितं वर्चो वर्चस्कम् अन्नमलम्**.\n'
        "  The word is किरति with अव and 3.3.57's अप् in the passive sense —\n"
        '  **अवकीर्यत इत्यवस्करोऽन्नमलम्** — and **तत्संबन्धाद् देशोऽपि\n'
        '  तथोच्यते**, the place too by association'
    ),
)

register(
    '6.1.149',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — अपस्करो रथाङ्गम् — laid down for a part of a chariot:\n'
        '  **अपस्करो रथावयवः**. The same root and the same 3.3.57 as the rule\n'
        '  before, and only the preverb and the sense differ'
    ),
)

register(
    '6.1.150',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — विष्किरः शकुनिर्विकिरो वा — laid down for a bird, and\n'
        '  optionally, विकिर standing beside it: **सर्वे शकुनयो भक्ष्या\n'
        "  विष्किराः कुक्कुटादृते**. The affix is 3.1.135's क.\n"
        '\n'
        'SETTLED — **AND THE SECOND WORD IS IN THE RULE TO CONFINE IT.**\n'
        '  **विष्किरो वा शकुनाविति वा ग्रहणादेव सुड्विकल्पे सिद्धे\n'
        '  विकिरग्रहणम् इह तस्यापि शकुनेरन्यत्र प्रयोगो मा भूत्** — the वा\n'
        '  alone would have given both forms; naming विकिर as well is what\n'
        '  stops THAT word being used of anything but a bird'
    ),
)

register(
    '6.1.151',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — ह्रस्वाच्चन्द्रोत्तरपदे मन्त्रे — in a मन्त्र, after a\n'
        '  short vowel, before चन्द्र standing as the second member of a\n'
        '  compound: **सुश्चन्द्र युष्मान्**.\n'
        '\n'
        'SETTLED — **AND उत्तरपद MEANS WHAT IT MEANS IN A COMPOUND.**\n'
        '  **उत्तरपदं समास एव भवतीति प्रसिद्धम्** — not merely *the word\n'
        '  after*, which is why **शुक्रमसि चन्द्रमसि** is untouched'
    ),
)

register(
    '6.1.152',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        "SETTLED — प्रतिष्कशश्च कशेः — before कश् with प्रति and 3.1.134's\n"
        '  अच्, laid down with its सुट् and its ष्: **ग्राममद्य प्रवेक्ष्यामि\n'
        '  भव मे त्वं प्रतिष्कशः** — **वार्तापुरुषः, सहायः, पुरोयायी वा**, a\n'
        '  messenger or one who goes ahead.\n'
        '\n'
        'SETTLED — **AND NAMING THE ROOT IS WHAT FIXES THE PREVERB.**\n'
        '  **कशेरिति धातोरुपादानं तदुपसर्गस्य प्रतेः प्रतिपत्त्यर्थम्। तेन\n'
        '  धात्वन्तरोपसर्गाद् न भवति** — the प्रति of the rule is the one\n'
        '  joined to THIS root, so a प्रति on some other root gets nothing'
    ),
)

register(
    '6.1.153',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — प्रस्कण्वहरिश्चन्द्रावृषी — two names laid down, and only\n'
        '  of the ṛṣis who bear them: **प्रस्कण्व ऋषिः; हरिश्चन्द्र ऋषिः**.\n'
        '  And the second is here for a reason 6.1.151 makes plain —\n'
        '  **हरिश्चन्द्रग्रहणम् अमन्त्रार्थम्**: that rule would have given\n'
        '  it already in a मन्त्र, and this one reaches it elsewhere'
    ),
)

register(
    '6.1.154',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — मस्करमस्करिणौ वेणुपरिव्राजकयोः — two words यथासंख्यम्, a\n'
        '  bamboo and a wandering mendicant: **मस्करो वेणुः; मस्करी\n'
        '  परिव्राजकः**. On the plain reading मकर is **अव्युत्पन्नं\n'
        '  प्रातिपदिकम्**, a stem with no derivation, and the सुट् is simply\n'
        '  laid down.\n'
        '\n'
        'SETTLED — **AND A SECOND READING DERIVES BOTH AND GETS A GLOSS OUT\n'
        '  OF IT.** **केचित् पुनरत्र माङ्युपपदे करोतेः करणे अच्प्रत्ययमपि\n'
        "  निपातयन्ति** — मा + कृ with 3.1.134's अच् in the instrumental\n"
        '  sense: **मा क्रियते येन प्रतिषिध्यते, स मस्करो वेणुः**, the staff\n'
        '  by which one forbids. And with इनि in the sense of habit,\n'
        '  **माकरणशीलो मस्करी कर्मापवादित्वात् परिव्राजक उच्यते** — one whose\n'
        '  way is *do not*, and the vṛtti puts his words in: **स ह्येवमाह —\n'
        '  मा कुरुत कर्माणि, शान्तिर्वः श्रेयसीति**.\n'
        '\n'
        'SETTLED — **AND वेणु IS AN INSTANCE AND NOT A LIMIT.** **वेणुग्रहणं\n'
        '  च प्रदर्शनार्थम् अन्यत्रापि भवति — मस्करो दण्ड इति**'
    ),
)

register(
    '6.1.155',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — कास्तीराजस्तुन्दे नगरे — two city names laid down:\n'
        '  **कास्तीरं नाम नगरम्; अजस्तुन्दं नाम नगरम्**. The vṛtti gives each\n'
        '  an etymology and then sets it aside: **ईषत्तीरमस्य, अजस्येव\n'
        '  तुन्दमस्येति व्युत्पत्तिरेव क्रियते, नगरं तु वाच्यमेतयोः** — the\n'
        '  derivation is made out, but what the words MEAN is a city, and\n'
        '  that has to be stated'
    ),
)

register(
    '6.1.156',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — कारस्करो वृक्षः — laid down for the tree of that name,\n'
        "  with 3.2.21's ट: **कारस्करो वृक्षः**.\n"
        '\n'
        'SETTLED — **AND SOME DO NOT READ IT AS A SŪTRA AT ALL.** **केचिदिदं\n'
        '  सूत्रं नाधीयते, पारस्करप्रभृतिष्वेव कारस्करो वृक्ष इति पठन्ति** —\n'
        "  they take the word to be a member of the next rule's list instead,\n"
        '  and the list does hold it'
    ),
)

register(
    '6.1.157',
    apply=sut_for,
    codification=_SUT_FOR,
    notes=(
        'SETTLED — पारस्करप्रभृतीनि च संज्ञायाम् — a list of names laid down\n'
        '  with their सुट्, and the rule whose words bound the heading opened\n'
        '  at 6.1.135: **पारस्करो देशः; रथस्पा नदी; किष्कुः प्रमाणम्;\n'
        '  किष्किन्धा गुहा**.\n'
        '\n'
        'SETTLED — **AND TWO OF THE LIST NEED A SOUND DROPPED AS WELL.**\n'
        '  **करपत्योश्चोरदेवतयोः सुट् तलोपश्च** — तद् + कर gives\n'
        '  **तस्करश्चोरः** and बृहत् + पति gives **बृहस्पतिर्देवता**, each\n'
        '  losing its त्; and only in those two senses.\n'
        '\n'
        'SETTLED — **AND ONE SUPPLEMENT PUTS THE AUGMENT ON A FINITE VERB.**\n'
        '  **प्रात्तुम्पतौ गवि कर्तरि** — **प्रस्तुम्पति गौः**, and the\n'
        '  condition is WHO THE AGENT IS. Nothing else in the pāda conditions\n'
        '  an augment on that.\n'
        '\n'
        'SETTLED — **AND THE LIST IS AN आकृतिगण, DEFINED BY EXCLUSION.**\n'
        '  **पारस्करप्रभृतिराकृतिगणः। अविहितलक्षणः सुट् पारस्करप्रभृतिषु\n'
        '  द्रष्टव्यः** — whatever सुट् no rule accounts for belongs here, so\n'
        '  the list cannot be closed. **प्रायश्चित्तम्, प्रायश्चित्तिः** come\n'
        "  in that way, and with them the Mahābhāṣya's own **प्रायस्य\n"
        '  चित्तिचित्तयोः सुडस्कारो वा**'
    ),
)


_ACCENT_OF = (
    'accent_of(stem, gana=..., marker=..., before=..., after=..., '
    'result=..., samjna=..., stri=..., chandasi=..., mantra=..., '
    'bhasayam=...) -> which syllable takes the accent, and which '
    'rule of 6.1.158–223 puts it there.'
)

register(
    '6.1.158',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अनुदात्तं पदमेकवर्जम् — **परिभाषेयं स्वरविधिविषया।\n'
        '  यत्रान्यः स्वर उदात्तः स्वरितो वा विधीयते, तत्रानुदात्तं पदमेकं\n'
        '  वर्जयित्वा भवति** — one syllable of a word takes the accent that\n'
        '  is taught and every other is अनुदात्त.\n'
        '\n'
        'SETTLED — **AND WHICH ONE IS EXCEPTED IS THE ONE THE RULE NAMES.**\n'
        '  **कः पुनरेको वर्ज्यते? यस्यासौ स्वरो विधीयते** — the maxim does\n'
        '  not choose a syllable; it clears the rest out of the way of\n'
        '  whichever rule speaks.\n'
        '\n'
        'SETTLED — **AND एकवर्जम् IS SAID TO CANCEL FOUR COMPETING CLAIMS.**\n'
        '  **आगमस्य विकारस्य प्रकृतेः प्रत्ययस्य च।\n'
        '  पृथक्स्वरनिवृत्त्यर्थमेकवर्जं पदस्वरः॥** — an augment has its own\n'
        "  accent (7.1.98's आम् in चत्वारः), a substitute has one (अनङ् in\n"
        '  अस्थनि), the base has one (गोपायति), the affix has one\n'
        '  (कर्तव्यम्); and each of the four displaces one of the others\n'
        '  somewhere.\n'
        '\n'
        'SETTLED — **AND WHICH OF THEM WINS IS SETTLED BY FIVE THINGS.**\n'
        '  **परनित्यान्तरङ्गापवादैः स्वरैर्व्यवस्था सतिशिष्टेन च। यो हि\n'
        '  यस्मिन् सति शिष्यते, स तस्य बाधको भवति** — the later, the\n'
        '  invariable, the inner, the exception, and the one taught IN THE\n'
        '  PRESENCE of another. The chain **लुनाति, लुनीतः, लुनीतस्तराम्**\n'
        '  shows the last of the five three times over'
    ),
)

register(
    '6.1.159',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — कर्षात्वतो घञोऽन्त उदात्तः — a घञ् stem from कृष् or with\n'
        '  a long आ in it takes the accent on its last syllable: **कर्षः,\n'
        '  पाकः, त्यागः, रागः, दायः, धायः**. **ञ्नित्यादिर्नित्यम्\n'
        '  इत्यस्यापवादः** — an exception to 6.1.197, which would put it on\n'
        '  the first.\n'
        '\n'
        'SETTLED — **AND THE ODD SHAPE कर्ष IS WHAT PICKS THE ROOT.** **कर्ष\n'
        '  इति विकृतनिर्देशः कृषतेर्निवृत्त्यर्थः** — written with its guṇa,\n'
        '  it names the भ्वादि root and leaves the तुदादि one out'
    ),
)

register(
    '6.1.160',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — उञ्छादीनां च — a list, end-accented: **उञ्छः, म्लेच्छः,\n'
        '  जञ्जः, जल्पः, जपः, वधः, युगः**. Some are घञ् stems and would have\n'
        "  taken 6.1.197's accent; some are अप् stems and would have taken\n"
        "  the root's.\n"
        '\n'
        'SETTLED — **AND HALF THE LIST IS CONFINED BY A SENSE.** **गरो\n'
        '  दूष्ये** — गर is end-accented only of poison; **वेगवेदवेष्टबन्धाः\n'
        '  करणे** — those four only as instruments, and **भाव आद्युदात्ता\n'
        '  एव**; **वर्तनिः स्तोत्रे**, **श्वभ्रे दरः**, **साम्बतापौ\n'
        '  भावगर्हायाम्**. A list whose members each carry their own\n'
        '  condition'
    ),
)

register(
    '6.1.161',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अनुदात्तस्य च यत्रोदात्तलोपः — where an उदात्त is dropped\n'
        '  before an अनुदात्त, that अनुदात्त takes the accent at its first\n'
        '  syllable: **कुमारी** from कुमार꣡ + ई॒, **पथः, पथा, पथे**,\n'
        '  **कुमुद्वान्, नड्वान्, वेतस्वान्**.\n'
        '\n'
        'SETTLED — **AND अनुदात्तस्य IS SAID TO PUT IT AT THE FIRST AND NOT\n'
        '  THE LAST.** **तदेतद् अनुदात्तग्रहणम् आदेरनुदात्तस्य उदात्तार्थम्।\n'
        '  अन्त इति हि प्रकृतत्वाद् अन्तस्य स्यात्** — अन्त is carrying from\n'
        '  6.1.159, so without this word the accent would land on the wrong\n'
        '  end.\n'
        '\n'
        'SETTLED — **AND A SVARITA CANNOT SET THE RULE OFF.** An objector\n'
        '  offers प्रासङ्ग्यः, where a स्वरित य displaced an उदात्त.\n'
        '  **नैतदस्ति, स्वरिते हि विधीयमाने परिशिष्टम् अनुदात्तम्, तत् कुतः\n'
        '  उदात्तलोपः?** — where a स्वरित is taught, 6.1.158 makes the rest\n'
        '  अनुदात्त, so there was never an उदात्त to lose'
    ),
)

register(
    '6.1.162',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — धातोः — a root takes the accent on its last syllable:\n'
        '  **पचति, पठति, ऊर्णोति, गोपायति, याति**. **अन्त इत्येव** — the word\n'
        '  carries down from 6.1.159, and this is the accent every later rule\n'
        '  of the section is stated against'
    ),
)

register(
    '6.1.163',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — चितः — a stem made by an affix, augment or substitute\n'
        '  marked च् takes the accent at its end: **भङ्गुरम्, भासुरम्,\n'
        "  मेदुरम्** with 3.2.161's घुरच्; **कुण्डिनाः** with 2.4.70's\n"
        '  कुण्डिनच्.\n'
        '\n'
        "SETTLED — **AND THE END MEANT IS THE WHOLE WORD'S.** **चिति प्रत्यये\n"
        '  प्रकृतिप्रत्ययसमुदायस्यान्त उदात्त इष्यते** — which is what makes\n'
        '  **बहुपटवः** and **उच्चकैः** work, the affixes बहुच् and अकच् being\n'
        '  put in at the FRONT and in the MIDDLE and the accent still landing\n'
        '  at the end'
    ),
)

register(
    '6.1.164',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — तद्धितस्य — and a taddhita stem marked च् likewise:\n'
        "  **कौञ्जायनाः, भौञ्जायनाः** with 4.1.98's च्फञ्.\n"
        '\n'
        'SETTLED — **AND THE RULE EXISTS TO SETTLE A CONTEST BETWEEN TWO\n'
        '  MARKERS.** **किमर्थमिदम्? परमपि ञित्स्वरं बाधित्वा\n'
        '  अन्तोदात्तत्वमेव यथा स्यात्** — च्फञ् has both a च् and a ञ्, and\n'
        "  6.1.197's ञित् accent stands LATER. The rule gives the च् its way,\n"
        "  and the reason is that the ञ् still has 7.2.117's vṛddhi to do\n"
        '  while the च् would have nothing left'
    ),
)

register(
    '6.1.165',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — कितः — and a taddhita marked क् too: **नाडायनः, चारायणः**\n'
        "  with 4.1.99's फक्; **आक्षिकः, शालाकिकः** with 4.4.1's ठक्"
    ),
)

register(
    '6.1.166',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — तिसृभ्यो जसः — **तिस्रस्तिष्ठन्ति**, and the accent\n'
        '  displaces the स्वरित 8.2.4 would give.\n'
        '\n'
        'SETTLED — **AND जसः IS SAID FOR A CASE THE WORD ITSELF DOES NOT\n'
        '  HAVE.** तिसृ is plural only, and of its seven plural cases the\n'
        "  accusative is 6.1.174's and the five consonant-initial ones are\n"
        "  6.1.179's — so जस् is the only one left and naming it looks idle.\n"
        '  **जस्ग्रहणम् उपसमस्तार्थम् एक इच्छन्ति** — it is there for the\n'
        '  compound, where singular and dual endings do occur: **अतितिस्रौ**'
    ),
)

register(
    '6.1.167',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — चतुरः शसि — **चतुरः पश्य**, the accent on तु. And the\n'
        '  feminine is kept out twice over: **चतस्रादेश आद्युदात्तनिपातनाद्\n'
        '  यणादेशस्य च पूर्वविधौ स्थानिवत्त्वाद् अयं स्वरो न भवति**'
    ),
)

register(
    '6.1.168',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — सावेकाचस्तृतीयादिर्विभक्तिः — where the stem is\n'
        '  one-syllabled AS IT STANDS IN THE LOCATIVE PLURAL, the endings\n'
        '  from the third case on take the accent: **वाचा, वाग्भ्याम्,\n'
        '  वाग्भिः, वाग्भ्यः; याता, याद्भ्याम्**.\n'
        '\n'
        'SETTLED — **AND सौ IS THE LOCATIVE PLURAL AND NOT THE NOMINATIVE.**\n'
        '  **साविति सप्तमीबहुवचनस्य सुशब्दस्य ग्रहणम्** — which is what keeps\n'
        '  त्वया and त्वयि out, one-syllabled though their stems look'
    ),
)

register(
    '6.1.169',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अन्तोदात्तादुत्तरपदादन्यतरस्यामनित्यसमासे — in a compound\n'
        '  that can be unloosened, and whose second member is one-syllabled\n'
        '  and end-accented, the same endings take the accent optionally:\n'
        '  **परमवाचा** beside **परमवाचा**, **परमत्वचा** beside **परमत्वचा**.\n'
        '  **यदा विभक्तिरुदात्ता न भवति, तदा समासान्तोदात्तत्वमेव** — on the\n'
        '  other side 6.1.223 takes it.\n'
        '\n'
        'SETTLED — **AND नित्य IS ACCENTED IN THE SŪTRA TO NAME A HEADING.**\n'
        '  **नित्यशब्दः स्वर्यते। तेन नित्याधिकारविहितः समासः पर्युदस्यते** —\n'
        "  a compound made under 2.2.19's नित्य heading is what is excepted,\n"
        '  and a compound that is नित्य merely for having no analysis still\n'
        '  takes the option: **अवाचा ब्राह्मणेन**'
    ),
)

register(
    '6.1.170',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अञ्चेश्छन्दस्यसर्वनामस्थानम् — in the corpus, after a stem\n'
        '  in अञ्च् the weak endings take the accent: **इन्द्रो दधीचो\n'
        '  अस्थभिः**. It displaces 6.1.222, which would have put it on the\n'
        '  syllable before.\n'
        '\n'
        'SETTLED — **AND असर्वनामस्थान IS SAID TO REACH ONE MORE ENDING.**\n'
        '  **तृतीयादिरिति वर्तमाने शसोऽपि परिग्रहार्थम्\n'
        '  असर्वनामस्थानग्रहणम्** — तृतीयादि was carrying and would have left\n'
        '  the accusative plural out: **प्रतीचो बाहून् प्रति भङ्ध्येषाम्**'
    ),
)

register(
    '6.1.171',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — ऊडिदम्पदाद्यप्पुम्रैद्युभ्यः — after seven bases the weak\n'
        '  endings take the accent: **प्रष्ठौहः, प्रष्ठौहा; आभ्याम्, एभिः;\n'
        '  पदश्चतुरो जहि; अपः पश्य, अद्भिः; पुंसः, पुम्भ्याम्; रायः पश्य;\n'
        '  दिवः, दिवा**.\n'
        '\n'
        'SETTLED — **AND पदादि MEANS A STRETCH AND NOT A WORD.** **पदादयः\n'
        "  पद्दन्नोमास् इत्येवमादयो निश्पर्यन्ता इह गृह्यन्ते** — 6.1.63's\n"
        '  list as far as निश्, and no further: **असन्प्रभृतिभ्यो\n'
        '  विभक्तिरनुदात्तैव भवति**, so आसनि and उदनि keep their endings\n'
        '  unaccented'
    ),
)

register(
    '6.1.172',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अष्टनो दीर्घात् — after the LONG form of अष्टन् the weak\n'
        '  endings take the accent: **अष्टाभिः, अष्टाभ्यः, अष्टासु**, against\n'
        '  अष्टभिः and अष्टसु.\n'
        '\n'
        'SETTLED — **AND दीर्घात् IS READ AS TWO ज्ञापक AT ONCE.** **इदमेव\n'
        '  दीर्घग्रहणम् अष्टन आत्वविकल्पं ज्ञापयति, कृतात्वस्य च षट्संज्ञां\n'
        "  ज्ञापयति** — 7.2.84's आ would be fixed and the word would be there\n"
        '  whatever, so the condition is idle unless the lengthening is\n'
        '  OPTIONAL; and it is idle again unless the lengthened form is a षट्\n'
        "  and would otherwise take 6.1.179's accent"
    ),
)

register(
    '6.1.173',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — शतुरनुमो नद्यजादी — after an end-accented शतृ participle\n'
        '  without its नुम्, the feminine ई and the vowel-initial weak\n'
        '  endings take the accent: **तुदती, नुदती, लुनती, पुनती; तुदता,\n'
        '  नुदता**.\n'
        '\n'
        'SETTLED — **AND THE PARTICIPLE IS END-ACCENTED BY A CHAIN OF THREE\n'
        '  RULES.** 6.1.186 makes the शतृ अनुदात्त after a root taught with\n'
        '  अ; 8.2.5 makes the single substitute उदात्त where one of the two\n'
        '  was; and **तस्य पूर्वत्रासिद्धत्वं नेष्यते** — 8.2.1 is not\n'
        '  applied to it, or the participle would not be end-accented and\n'
        '  this rule would have nothing to work on.\n'
        '\n'
        'SETTLED — **AND A SUPPLEMENT ADDS TWO MORE.**\n'
        '  **बृहन्महतोरुपसंख्यानम्** — **बृहती, महती; बृहता, महता**'
    ),
)

register(
    '6.1.174',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — उदात्तयणो हल्पूर्वात् — where a semivowel stands for an\n'
        '  उदात्त vowel and a consonant stands before it, the same endings\n'
        '  take the accent: **कर्त्री, हर्त्री, प्रलवित्री; कर्त्रा,\n'
        '  हर्त्रा**. The तृच् stems are end-accented and the तृन् ones are\n'
        '  not, which is the whole of the difference.\n'
        '\n'
        'SETTLED — **AND A SUPPLEMENT EXTENDS IT TO A NASAL.** **नकारग्रहणं\n'
        '  कर्तव्यम्** — **वाक्पत्नी इयं कन्या**, where what precedes is no\n'
        '  semivowel at all'
    ),
)

register(
    '6.1.175',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — न उङ्धात्वोः — but not where the semivowel stands for the\n'
        "  feminine ऊङ् or for a root's own final: **ब्रह्मबन्ध्वा,\n"
        '  ब्रह्मबन्ध्वे; सकृल्ल्वा, खलप्वे**.\n'
        '\n'
        "SETTLED — **AND WHAT STANDS INSTEAD IS 8.2.4's स्वरित.**\n"
        '  **उदात्तत्वे प्रतिषिद्धे उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य\n'
        '  इति विभक्तिः स्वर्यते** — the refusal does not leave the ending\n'
        '  unaccented; it hands it to the general rule'
    ),
)

register(
    '6.1.176',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — ह्रस्वनुड्भ्यां मतुप् — मतुप् takes the accent after an\n'
        '  end-accented stem ending in a light vowel, or after the augment\n'
        '  नुट्: **अग्निमान्, वायुमान्, कर्तृमान्; अक्षण्वता, शीर्षण्वता**.\n'
        '\n'
        'SETTLED — **AND THIS IS WHERE स्वरविधौ व्यञ्जनमविद्यमानवत् IS\n'
        '  REFUSED.** **अत्र च स्वरविधौ व्यञ्जनमविद्यमानवद् इत्येषा परिभाषा\n'
        '  नाश्रीयते नुड्ग्रहणात्** — naming the नुट् separately is only\n'
        '  worth doing if a consonant DOES count, and that is why\n'
        '  **मरुत्वान्** is out. The same maxim 6.1.223 leans on, denied\n'
        '  here.\n'
        '\n'
        'SETTLED — **AND TWO SUPPLEMENTS PULL IT BOTH WAYS.** **रेशब्दाच्च\n'
        '  मतुप उदात्तत्वं वक्तव्यम्** — **आ रेवान्**; and **त्रेश्च\n'
        '  प्रतिषेधो वक्तव्यः** — **त्रिवतीः**'
    ),
)

register(
    '6.1.177',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — नामन्यतरस्याम् — and the genitive plural नाम् optionally:\n'
        '  **अग्नीनाम्** beside **अग्नीनाम्**, **वायूनाम्**, **कर्तॄणाम्**.\n'
        '\n'
        'SETTLED — **AND ह्रस्व IS READ AS *SHORT BEFORE मतुप्*, NOT AS\n'
        '  *SHORT HERE*.** The vowels in those forms are long, so the\n'
        '  condition looks unmet. **मतुबग्रहणं च तेन मतुपा ह्रस्वो\n'
        '  विशेष्यते** — मतुप् carries down and the condition is on the shape\n'
        '  the stem HAS before that affix. Read it the other way and तिसृणाम्\n'
        '  and चतसृणाम् are reached instead, which is not wanted'
    ),
)

register(
    '6.1.178',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — ङ्याश्छन्दसि बहुलम् — in the corpus, नाम् takes the accent\n'
        '  variously after the feminine ई: **देवसेनानाम् अभिभञ्जतीनाम्;\n'
        '  बह्वीनां पिता**. And sometimes not — which is what बहुलम् records'
    ),
)

register(
    '6.1.179',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — षट्त्रिचतुर्भ्यो हलादिः — after the numerals called षट्,\n'
        '  and after त्रि and चतुर्, a consonant-initial ending takes the\n'
        '  accent: **षड्भिः, षड्भ्यः, पञ्चानाम्, षण्णाम्, सप्तानाम्; त्रिभिः,\n'
        '  त्रयाणाम्; चतुर्णाम्**.\n'
        '\n'
        'SETTLED — **AND अन्तोदात्तात् LAPSES HERE.** **अन्तोदात्तादित्येतद्\n'
        '  निवृत्तम्** — पञ्चन् and नवन् are first-accented and the rule\n'
        '  reaches them anyway, which it could not if the condition still ran'
    ),
)

register(
    '6.1.180',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — झल्युपोत्तमम् — where the ending begins with a झल्, the\n'
        '  accent goes to the syllable before the last: **पञ्चभिः, सप्तभिः,\n'
        '  तिसृभिः, चतुर्भिः**.\n'
        '\n'
        'SETTLED — **AND उपोत्तम IS DEFINED BEFORE IT IS USED.**\n'
        '  **त्रिप्रभृतीनाम् अन्त्यम् उत्तमम्, तत्समीपे च यत् तद् उपोत्तमम्**\n'
        '  — the word itself requires three syllables, and that is why षड्भिः\n'
        '  falls back to 6.1.179'
    ),
)

register(
    '6.1.181',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — विभाषा भाषायाम् — in ordinary speech the rule before is a\n'
        '  choice: **पञ्चभिः** beside **पञ्चभिः**, **सप्तभिः**, **तिसृभिः**,\n'
        '  **चतुर्भिः**. In the corpus it is fixed, and this is the only rule\n'
        '  of the pāda whose condition is that the language is NOT Vedic'
    ),
)

register(
    '6.1.182',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — न गोश्वन्सावर्णराडङ्क्रुङ्कृद्भ्यः — after seven bases\n'
        '  everything from 6.1.168 on is refused: **गवा, गवे, गोभ्याम्; शुना,\n'
        '  शुने; येभ्यः, तेभ्यः, केभ्यः; राजा; प्राञ्चा, प्राङ्भ्याम्;\n'
        '  क्रुञ्चा; कृता**.\n'
        '\n'
        'SETTLED — **AND अङ् IS NAMED WITH ITS न् TO CONFINE THE REFUSAL.**\n'
        '  **अङ् अञ्चतिः क्विन्नन्तस्तस्य सनकारस्य ग्रहणं विषयावधारणार्थम्,\n'
        '  यत्रास्य नलोपो नास्ति तत्र प्रतिषेधो यथा स्यात्** — where 6.4.30\n'
        '  keeps the न्, the refusal bites; where the न् is gone, **प्राचा,\n'
        '  प्राचे, प्राग्भ्याम्** take the accent'
    ),
)

register(
    '6.1.183',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — दिवो झल् — after दिव् a झल्-initial ending is not\n'
        '  accented: **द्युभ्याम्, द्युभिः**. The refusal reaches two rules\n'
        '  at once, since दिव् is named in 6.1.171 and is one-syllabled for\n'
        '  6.1.168'
    ),
)

register(
    '6.1.184',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — नृ चान्यतरस्याम् — and after नृ the same refusal is a\n'
        '  choice: **नृभ्याम्, नृभिः, नृभ्यः, नृषु** beside the accented\n'
        '  forms'
    ),
)

register(
    '6.1.185',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — तित् स्वरितम् — an affix marked त् takes the स्वरित, and\n'
        '  this is the first rule of the pāda that gives one: **चिकीर्ष्यम्,\n'
        "  जिहीर्ष्यम्** with यत्; **कार्यम्, हार्यम्** with 3.1.124's ण्यत्.\n"
        '  **प्रत्ययाद्युदात्तस्यापवादः** — an exception to 3.1.3, which\n'
        "  would put an उदात्त on the affix's first syllable instead"
    ),
)

register(
    '6.1.186',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — तास्यनुदात्तेङ्ङिदद्रुपदेशाल्लसार्वधातुकमनुदात्तमह्न्विङोः\n'
        '  — a सार्वधातुक ending is unaccented after the तास् of the\n'
        '  periphrastic future, after a root the धातुपाठ marked अनुदात्त or\n'
        '  ङित्, and after one taught ending in अ: **कर्ता, कर्तारौ; आस्ते,\n'
        '  वस्ते; सूते, शेते; तुदतः, पचतः, पठतः**.\n'
        '\n'
        'SETTLED — **AND A ROOT TAKING शप् COUNTS AS TAUGHT WITH AN अ.**\n'
        '  **अनुबन्धस्यानैकान्तिकत्वाद् अकारान्तोपदेश एव शप्** — the श् and\n'
        '  प् being markers, what is left is the अ. **पचमानः, यजमानः**.\n'
        '\n'
        "SETTLED — **AND THIS ACCENT DISPLACES 6.1.163's.**\n"
        '  **चित्स्वरोऽप्यनेन लसार्वधातुकानुदात्तत्वेन परत्वाद् बाध्यते** —\n'
        '  being later, it wins'
    ),
)

register(
    '6.1.187',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — आदिः सिचोऽन्यतरस्याम् — a सिच् aorist may take the accent\n'
        '  on its first syllable: **मा हि कार्ष्टाम्** beside **मा हि\n'
        '  कार्ष्टाम्**; **मा हि लाविष्टाम्** beside **मा हि लाविष्टाम्**.\n'
        '\n'
        'SETTLED — **AND THE च् OF सिच् IS WHAT PUTS THE OTHER ACCENT ON THE\n'
        '  AUGMENT.** **सिचश्चित्करणाद् आगमानुदात्तत्वं हि बाध्यते** — an\n'
        "  augment is unaccented as a rule, and 6.1.163's चित् accent\n"
        '  overrides it, so the इट् of लाविष्टाम् can carry the accent'
    ),
)

register(
    '6.1.188',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — स्वपादिहिंसामच्यनिटि — स्वप् and its list, and हिंस्, may\n'
        '  take the accent on the first syllable before a vowel-initial\n'
        '  सार्वधातुक ending without इट्: **स्वपन्ति, श्वसन्ति, हिंसन्ति**\n'
        '  beside the middle-accented forms 3.1.3 gives'
    ),
)

register(
    '6.1.189',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अभ्यस्तानामादिः — and for an अभ्यस्त the same accent is\n'
        '  FIXED: **ददति, ददतु, दधति, जक्षति, जाग्रति**. **आदिरिति वर्तमाने\n'
        '  पुनरादिग्रहणं नित्यार्थम्** — आदि was already carrying, and saying\n'
        '  it again is how the rule sheds the option of the one before. The\n'
        '  same device 6.1.32 and 6.1.57 used.\n'
        '\n'
        "SETTLED — **AND THIS IS THE RULE 6.1.5's उभे WAS SAID FOR.** The\n"
        '  name अभ्यस्त belongs to the two copies TOGETHER, so the accent\n'
        '  falls once, on the first vowel of the pair'
    ),
)

register(
    '6.1.190',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अनुदात्ते च — and before an ending that has no उदात्त in\n'
        '  it at all: **ददाति, जहाति, दधाति, जिहीते, मिमीते**. **अनजाद्यर्थ\n'
        '  आरम्भः** — the rule exists for the consonant-initial endings the\n'
        '  one before could not reach.\n'
        '\n'
        'SETTLED — **AND अनुदात्ते IS READ AS A बहुव्रीहि.** **अनुदात्त इति\n'
        '  बहुव्रीहिनिर्देशो लोपयणादेशार्थः** — *that in which there is no\n'
        '  उदात्त*, so a form whose ending has been partly dropped or turned\n'
        '  into a semivowel is still reached: **मा हि स्म दधात्; दधात्यत्र**'
    ),
)

register(
    '6.1.191',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — सर्वस्य सुपि — सर्व takes the accent on its first syllable\n'
        '  before a case-ending: **सर्वः, सर्वौ, सर्वे**.\n'
        '\n'
        'SETTLED — **AND HERE प्रत्ययलक्षण DOES HOLD.**\n'
        '  **प्रत्ययलक्षणेनाप्ययं स्वर इष्यते — सर्वस्तोमः** — the ending is\n'
        '  gone and the accent stays, which 6.1.197 and 6.1.199 both refuse\n'
        '  to allow. Three rules of this pāda answer one question three ways'
    ),
)

register(
    '6.1.192',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वं पिति —\n'
        '  nine roots take the accent on the syllable BEFORE the ending,\n'
        '  where that ending is पित्: **बिभेति, जिह्रेति, बिभर्ति, जुहोति,\n'
        '  ममत्तु, जजनत्, दधनत्, दरिद्राति, जागर्ति**. An exception to\n'
        '  6.1.189, and the first rule of the pāda to put the accent by\n'
        '  counting back from the affix'
    ),
)

register(
    '6.1.193',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — लिति — and before any affix marked ल्, the syllable before\n'
        "  it: **चिकीर्षकः, जिहीर्षकः** with 3.1.133's ण्वुल्; **भौरिकिविधम्,\n"
        "  ऐषुकारिभक्तम्** with 4.2.54's विधल् and भक्तल्"
    ),
)

register(
    '6.1.194',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — आदिर्णमुल्यन्यतरस्याम् — before णमुल् the first syllable\n'
        '  may take it: **लोलूयंलोलूयम्** beside **लोलूयंलोलूयम्**. And the\n'
        "  other side is 6.1.193's, the affix being लित्. The rule reaches\n"
        '  only the doubled absolutives, 8.1.3 having made the second copy\n'
        '  unaccented'
    ),
)

register(
    '6.1.195',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अचः कर्तृयकि — a root taught ending in a vowel may take\n'
        '  the accent on its first syllable before the passive यक् used\n'
        '  reflexively: **लूयते केदारः स्वयमेव** beside **लूयते**;\n'
        '  **स्तीर्यते** beside **स्तीर्यते**.\n'
        '\n'
        'SETTLED — **AND THREE ROOTS COUNT AS VOWEL-FINAL THAT ARE NOT.**\n'
        '  **जनादीनाम् उपदेश एवात्वं द्रष्टव्यम्। तत्राप्ययं स्वर इष्यते** —\n'
        "  जन्, सन् and खन् take 6.4.43's आ, and the long vowel is treated as\n"
        '  theirs from the धातुपाठ: **जायते, सायते, खायते**'
    ),
)

register(
    '6.1.196',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — थलि च सेटीडन्तो वा — before a थल् with its इट्, the accent\n'
        '  may be on the इट्, on the ending, or on the first syllable — and\n'
        "  with 6.1.193's fourth alternative **तेनैते चत्वारः स्वराः पर्यायेण\n"
        '  भवन्ति**: **लुलविथ, लुलविथ, लुलविथ, लुलविथ**. One form and four\n'
        '  accentuations, which is the largest option in the pāda and among\n'
        '  the largest in the book'
    ),
)

register(
    '6.1.197',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — ञ्नित्यादिर्नित्यम् — whatever is made by an affix marked\n'
        '  ञ् or न् takes the accent on its first syllable, invariably:\n'
        "  **गार्ग्यः, वात्स्यः** with 4.1.105's यञ्; **वासुदेवकः, अर्जुनकः**\n"
        "  with 4.3.98's वुन्. **प्रत्ययस्वरापवादोऽयं योगः**.\n"
        '\n'
        'SETTLED — **AND HERE प्रत्ययलक्षण DOES NOT HOLD.**\n'
        '  **प्रत्ययलक्षणमत्र नेष्यते, तेन गर्गाः, बिदाः, चञ्चा इत्यत्र यञि\n'
        '  कनि च लुप्ते न भवति** — the affix elided, its accent goes with it,\n'
        "  where 6.1.191's did not"
    ),
)

register(
    '6.1.198',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — आमन्त्रितस्य च — a vocative takes the accent on its first\n'
        '  syllable: **देवदत्त, देवदत्तौ, देवदत्ताः**, displacing the\n'
        '  end-accent 6.2.148 would give.\n'
        '\n'
        'SETTLED — **AND HERE प्रत्ययलक्षण HOLDS AGAIN, AGAINST 1.1.63.**\n'
        '  **लुमतापि लुप्ते प्रत्ययलक्षणमत्रेष्यते** — even where a लुक्,\n'
        '  लुप् or श्लु took the affix away: **सर्पिरागच्छ, सप्तागच्छत**.\n'
        '  Three rules, three answers, and the pāda does not reconcile them'
    ),
)

register(
    '6.1.199',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — पथिमथोः सर्वनामस्थाने — before a strong ending these two\n'
        '  take the accent on the first syllable: **पन्थाः, पन्थानौ, पन्थानः;\n'
        '  मन्थाः, मन्थानौ, मन्थानः**. Both are औणादिक इनि stems and\n'
        '  end-accented by 3.1.3.\n'
        '\n'
        'SETTLED — **AND प्रत्ययलक्षण IS REFUSED HERE TOO.**\n'
        '  **प्रत्ययलक्षणमत्रापि नेष्यते। पथिप्रियः** — in the compound the\n'
        '  word keeps its own end-accent instead'
    ),
)

register(
    '6.1.200',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अन्तश्च तवै युगपत् — an infinitive in तवै takes the accent\n'
        '  on its FIRST and LAST syllables AT ONCE: **कर्तवै, हर्तवै**.\n'
        '\n'
        'SETTLED — **AND युगपत् IS SAID AGAINST THE PARIBHĀṢĀ THAT GOVERNS\n'
        '  IT.** **युगपद्ग्रहणं पर्यायनिवृत्त्यर्थम्। एकवर्जमिति वचनाद्\n'
        '  यौगपद्यं न स्यात्** — 6.1.158 allows one accent to a word, so\n'
        '  without this word the two would have been alternatives. The one\n'
        '  rule of the pāda that breaks its own heading, and the heading is\n'
        '  named as the reason it had to'
    ),
)

register(
    '6.1.201',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — क्षयो निवासे — क्षय takes the accent on its first syllable\n'
        '  where it means a dwelling: **क्षये जागृहि प्रपश्यन्** —\n'
        "  **क्षियन्ति निवसन्त्यस्मिन्निति क्षयः**. The word is 3.3.118's घ\n"
        "  stem and would have taken the affix's accent"
    ),
)

register(
    '6.1.202',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — जयः करणम् — and जय where it means what one wins BY:\n'
        '  **जयोऽश्वः** — **जयन्ति तेनेति जयः**. The same घ and the same\n'
        '  displacement as the rule before, and the two are told apart by\n'
        '  nothing but the sense'
    ),
)

register(
    '6.1.203',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — वृषादीनां च — a list, first-accented: **वृषः, जनः, ज्वरः,\n'
        '  ग्रहः, हयः, गयः, नयः, अंशः, वेदः, सूदः, गुहा, मन्त्रः, शान्तिः,\n'
        '  कामः, यामः, आरा, धारा, कारा, कल्पः, पादः**.\n'
        '\n'
        'SETTLED — **AND TWO OF ITS MEMBERS CARRY A CONDITION.** **शमरणौ\n'
        '  संज्ञायां संमतौ भावकर्मणोः** — शम in the abstract sense and रण in\n'
        '  the object sense; and **वहो गोचरादिषु**.\n'
        '\n'
        'SETTLED — **AND THE LIST IS AN आकृतिगण.** **वृषादिराकृतिगणः।\n'
        '  अविहितमाद्युदात्तत्वं वृषादिषु द्रष्टव्यम्** — whatever\n'
        '  first-syllable accent no rule accounts for belongs here, exactly\n'
        "  as 6.1.157's पारस्करप्रभृति took whatever सुट् no rule explained.\n"
        '  Two lists of that shape in one pāda'
    ),
)

register(
    '6.1.204',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — संज्ञायामुपमानम् — a word used as a LIKENESS and serving\n'
        '  as a name takes the accent on its first syllable: **चञ्चा,\n'
        '  वर्ध्रिका, खरकुटी, दासी**.\n'
        '\n'
        "SETTLED — **AND THE RULE'S EXISTENCE IS THE ज्ञापक THAT प्रत्ययलक्षण\n"
        '  IS NOT UNIVERSAL IN ACCENT.** The कन् of 5.3.96 is dropped by\n'
        '  5.3.98, and 1.1.62 would have kept its first-syllable accent\n'
        '  behind. **यद्येवं किमर्थम् इदम् उच्यते? प्रत्ययलक्षणेन सिद्धम्\n'
        '  आद्युदात्तत्वम्? एतदेव ज्ञापयति क्वचिद् इह स्वरविधौ प्रत्ययलक्षणं\n'
        '  न भवतीति** — a rule that would be idle if the maxim held\n'
        '  everywhere, and so proves it does not'
    ),
)

register(
    '6.1.205',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — निष्ठा च द्व्यजनात् — a two-syllabled निष्ठा participle\n'
        '  serving as a name takes the accent on its first syllable, unless\n'
        '  that syllable holds an आ: **दत्तः, गुप्तः, बुद्धः**. Four\n'
        '  conditions, and the vṛtti gives a counter-example for each'
    ),
)

register(
    '6.1.206',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — शुष्कधृष्टौ — two words first-accented, and **असंज्ञार्थ\n'
        '  आरम्भः** — the rule exists because they are NOT names and 6.1.205\n'
        '  could not reach them: **शुष्कः, धृष्टः**'
    ),
)

register(
    '6.1.207',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — आशितः कर्ता — आशित takes the accent on its first syllable\n'
        '  where it names the one who has EATEN: **आशितो देवदत्तः**. Where\n'
        "  the same form names the food or the eating it keeps 6.2.144's\n"
        '  end-accent. One participle, three कारक, two accents'
    ),
)

register(
    '6.1.208',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — रिक्ते विभाषा — रिक्त optionally: **रिक्तः** beside\n'
        '  **रिक्तः**. And where it IS a name, **संज्ञायां पूर्वविप्रतिषेधेन\n'
        '  नित्यमाद्युदात्तः** — 6.1.205 wins by being stated earlier, and\n'
        '  the accent is fixed'
    ),
)

register(
    '6.1.209',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — जुष्टार्पिते च छन्दसि — two words optionally\n'
        '  first-accented in the corpus: **जुष्टः** beside **जुष्टः**,\n'
        '  **अर्पितः** beside **अर्पितः**'
    ),
)

register(
    '6.1.210',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — नित्यं मन्त्रे — and in a मन्त्र the same two are fixed:\n'
        '  **जुष्टं देवानाम्; अर्पितं पितॄणाम्**.\n'
        '\n'
        'SETTLED — **AND THE VṚTTI REPORTS A DISSENT AND A VERSE AGAINST\n'
        '  ITSELF.** **केचिदत्र जुष्ट इत्येतदेवानुवर्तयन्ति। अर्पितशब्दस्य\n'
        '  विभाषा मन्त्रेऽपीच्छन्ति** — some carry only जुष्ट down and want\n'
        '  अर्पित optional even in a मन्त्र, and quote **शंकवोऽर्पिताः**\n'
        '  where it is end-accented in one'
    ),
)

register(
    '6.1.211',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — युष्मदस्मदोर्ङसि — the genitive singular forms take the\n'
        '  accent on the first syllable: **तव स्वम्, मम स्वम्**. Both stems\n'
        '  are end-accented by their औणादिक affix, and 8.2.5 would have put\n'
        '  the accent on the second syllable of तव'
    ),
)

register(
    '6.1.212',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — ङयि च — and the dative singular: **तुभ्यम्, मह्यम्**.\n'
        '  **पृथग्योगकरणं यथासंख्यशङ्कानिवृत्त्यर्थम्** — stated as a second\n'
        "  sūtra rather than joined to the first, so that 1.3.10's pairing\n"
        '  does not give the genitive to one stem and the dative to the other'
    ),
)

register(
    '6.1.213',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — यतोऽनावः — a two-syllabled यत् stem takes the accent on\n'
        "  its first syllable: **चेयम्, जेयम्** with 3.1.97's यत्;\n"
        "  **कण्ठ्यम्, ओष्ठ्यम्** with 5.1.6's. **तित्स्वरितम्\n"
        "  इत्यस्यापवादः** — an exception to 6.1.185's स्वरित"
    ),
)

register(
    '6.1.214',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — ईडवन्दवृशंसदुहां ण्यतः — five roots before ण्यत्:\n'
        '  **ईड्यम्, वन्द्यम्, वार्यम्, शंस्यम्, दोह्या धेनुः**.\n'
        '\n'
        'SETTLED — **AND ण्यत् IS NOT REACHED BY THE यत् OF THE RULE\n'
        '  BEFORE.** **द्व्यनुबन्धकत्वाद् ण्यतो यद्ग्रहणेन ग्रहणं नास्ति** —\n'
        "  having two markers, it is not named by the word यत्, so 6.1.185's\n"
        '  स्वरित would have stood and this rule is stated against it'
    ),
)

register(
    '6.1.215',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — विभाषा वेण्विन्धानयोः — two words optionally\n'
        '  first-accented: **वेणुः** beside **वेणुः**; **इन्धानः** beside two\n'
        '  other accentuations.\n'
        '\n'
        'SETTLED — **AND THE SECOND WORD WOULD NEVER HAVE HAD IT.** Read as a\n'
        '  चानश् stem इन्धान is end-accented by 6.1.163; read as a शानच् stem\n'
        '  it is middle-accented by 6.1.161. **तदेवम् इन्धाने सर्वथाप्राप्तम्\n'
        '  आद्युदात्तत्वं पक्षे विधीयते** — no analysis gives it a\n'
        '  first-syllable accent, and the rule supplies one.\n'
        '\n'
        'SETTLED — **AND THE OPTION LAPSES WHERE THE WORD IS A LIKENESS.**\n'
        '  **वेणुरिव वेणुरित्युपमानं यदा संज्ञा भवति, तदा संज्ञायामुपमानम्\n'
        '  इति नित्यम् आद्युदात्तत्वम् इष्यते**'
    ),
)

register(
    '6.1.216',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — त्यागरागहासकुहश्वठक्रथानाम् — six words optionally\n'
        '  first-accented: **त्यागः, रागः, हासः, कुहः, श्वठः, क्रथः**, each\n'
        '  beside its end-accented form. The first three are घञ् stems and\n'
        "  take 6.1.159's accent on the other side; the last three are अच्\n"
        '  stems'
    ),
)

register(
    '6.1.217',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — उपोत्तमं रिति — a stem made by an affix marked र् takes\n'
        '  the accent on the syllable before its last: **करणीयम्, हरणीयम्**\n'
        "  with 3.1.96's अनीयर्; **पटुजातीयः, मृदुजातीयः** with 5.3.19's\n"
        '  जातीयर्. And उपोत्तम requires three syllables, as it did at\n'
        '  6.1.180'
    ),
)

register(
    '6.1.218',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — चङ्यन्यतरस्याम् — a चङ् aorist may take the accent on its\n'
        '  penult: **मा हि चीकरताम्** beside **मा हि चीकरताम्**. The other\n'
        '  side is the चित् accent of चङ् itself'
    ),
)

register(
    '6.1.219',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — मतोः पूर्वमात् संज्ञायां स्त्रियाम् — the आ before मतुप्\n'
        '  takes the accent where the word is a feminine NAME: **उदुम्बरावती,\n'
        "  पुष्करावती, वीरणावती, शरावती**, the lengthening being 6.3.120's.\n"
        '  Four conditions, and the vṛtti gives a counter-example for each'
    ),
)

register(
    '6.1.220',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — अन्तोऽवत्याः — a name ending in अवती takes the accent on\n'
        '  its last syllable: **अजिरवती, खदिरवती, हंसवती, कारण्डवती**. The\n'
        '  ङीप् is पित् and would have been unaccented.\n'
        '\n'
        'SETTLED — **AND अवती IS WRITTEN WITH ITS अ FOR A REASON.** **अवत्या\n'
        '  इति किमुच्यते, न वत्या इत्येवमुच्येत? नैवं शक्यम्, इहापि स्यात् —\n'
        '  राजवती। स्वरविधौ नलोपस्यासिद्धत्वाद् नायमवतीशब्दः** — the न् of\n'
        '  राजन् is dropped by a rule of the त्रिपादी, and 8.2.1 makes that\n'
        '  invisible here, so the word is still राजन्वती and is not reached.\n'
        '  **वत्वं पुनराश्रयात् सिद्धम्** — the म् becoming व् IS visible,\n'
        '  being what the rule rests on'
    ),
)

register(
    '6.1.221',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — ईवत्याः — and a feminine name ending in ईवती takes the\n'
        '  accent on its last syllable likewise: **अहीवती, कृषीवती,\n'
        '  मुनीवती**. The rule before it named अवती with its अ for a reason\n'
        '  and this one names ईवती with its ई for the same one — the shape is\n'
        '  what is reached, not the affix that made it'
    ),
)

register(
    '6.1.222',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — चौ — before the अञ्च् whose न् has been dropped, the word\n'
        '  in front takes the accent on its last syllable: **दधीचः पश्य,\n'
        '  दधीचा, दधीचे; मधूचः, मधूचा**. **उदात्तनिवृत्तिस्वरापवादोऽयम्**.\n'
        '  And a supplement confines it — **चावतद्धित इति वक्तव्यम्**'
    ),
)

register(
    '6.1.223',
    apply=accent_of,
    codification=_ACCENT_OF,
    notes=(
        'SETTLED — समासस्य — a compound takes the accent on its last\n'
        '  syllable: **राजपुरुषः, ब्राह्मणकम्बलः, कन्यास्वनः, पटहशब्दः,\n'
        '  नदीघोषः; राजपृषत्, ब्राह्मणसमित्**. **नानापदस्वरस्यापवादः** — the\n'
        '  several words each had an accent and the compound has one.\n'
        '\n'
        'SETTLED — **AND A CONSONANT-FINAL COMPOUND STILL HAS ITS ACCENT ON A\n'
        '  VOWEL.** **स्वरविधौ व्यञ्जनमविद्यमानवद् इति\n'
        '  हलन्तेऽप्यन्तोदात्तत्वं भवति** — the same maxim 6.1.176 refused,\n'
        '  used here without argument. And this rule closes the pāda: the\n'
        "  exceptions to it are 6.2's whole business"
    ),
)


__all__ = [
    'akah_savarne_dirghah',
    'ato_gune',
    'dhatvadeh',
    'antadivat',
    'ekadesa_visible',
    'stated',
    'vocalises',
    'becomes_a',
    'operates',
    'joins',
    'one_for_both',
    'stands_open',
    'sut_for',
    'accent_of',
]
