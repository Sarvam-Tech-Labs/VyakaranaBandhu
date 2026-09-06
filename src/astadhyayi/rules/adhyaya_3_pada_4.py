# -*- coding: utf-8 -*-
"""
अध्याय ३, पाद ४ — an affix out of its time, and the tense-endings.

Two rules of this pāda were codified long before the reading reached it,
because derivations elsewhere stopped without them: 3.4.113 confers the
सार्वधातुक name that 7.3.84 needs, and 3.4.79 turns a correct pada choice
into a correct word. They are left where they are, and the pāda is now
being read from its first sūtra.
"""

from __future__ import annotations

from src.astadhyayi.anga import (
    ardhadhatuka, sarvadhatuka, tit_atmanepada,
)
from src.astadhyayi.denoted import denotes
from src.astadhyayi.denoted import nipatana as denoted_nipatana
from src.astadhyayi.dhatu_sambandha import (
    anuprayoga, dhatu_sambandha, nipatana, tumartha_affix,
)
from src.astadhyayi.ktva_namul import ktva_namul
from src.astadhyayi.lakara import (
    lakara_for, lakara_heading, lakara_substitutes,
)
from src.astadhyayi.tin_adesha import behaves_as, tin_adesha
from src.astadhyayi.vidhi_krt import vidhi_affix
from src.astadhyayi.sources import register
from src.astadhyayi.unadi import unadi


register(
    '3.4.113',
    apply=sarvadhatuka,
    samjna='सार्वधातुक',
    codification=(
        'sarvadhatuka(tin=..., sit=...) -> whether the affix bears the name.'
    ),
    related=('1.3.8', '1.3.9', '3.1.67', '3.1.68', '7.3.84'),
    notes=(
        'SETTLED — तिङः शितश्च प्रत्ययाः सार्वधातुकसंज्ञा भवन्ति: भवति,\n'
        '  नयति, स्वपिति, रोदिति for the तिङ्, and पवमानः, यजमानः for the\n'
        '  शित्.\n'
        '\n'
        'SETTLED — codified because a derivation stops without it. शप् is\n'
        '  शित् and takes the name here; 7.3.84 then gives guṇa *before a\n'
        '  sārvadhātuka*, and without this rule शप् is not one and जयति\n'
        '  never gets its ए. The Kāśikā points at the same dependency from\n'
        '  the other side — सार्वधातुकप्रदेशाः: सार्वधातुके यक् and the\n'
        '  rest.\n'
        '\n'
        'NOTE — the श् that brings the name is itself an इत् by 1.3.8 and\n'
        '  is removed by 1.3.9, which is why शप् surfaces as a bare अ. The\n'
        '  name outlives the letter that conferred it, and a derivation has\n'
        '  to carry it forward: the engine keeps it on the term rather than\n'
        '  re-reading it off a form where it no longer appears.'
    ),
)


register(
    '3.4.79',
    apply=tit_atmanepada,
    codification=(
        'tit_atmanepada(ending, tit_lakara=...) -> the ātmanepada ending '
        'with its टि replaced by ए.'
    ),
    related=('1.1.64', '1.3.12', '3.4.78'),
    notes=(
        'SETTLED — टितो लकारस्य स्थाने यानि आत्मनेपदानि तेषां टेः\n'
        '  एकारादेशो भवति. लट् is टित्, so its त becomes ते: एधते, पचते.\n'
        '  The टि is 1.1.64\'s — from the last vowel to the end — which for\n'
        '  त is the अ alone.\n'
        '\n'
        'SETTLED — the Kāśikā stops the rule reaching too far, and the\n'
        '  question is a good one: इह कस्माद् न भवति पचमानो यजमानः? Those\n'
        '  end in आन and are middle in sense, so why no ए? Because\n'
        '  प्रकृतैः तिबादिभिः आत्मनेपदानि विशेष्यन्ते — the ātmanepada\n'
        '  meant are the eighteen substitutes of 3.4.78, not शानच्.\n'
        '\n'
        'SETTLED — it is what turns a correct pada choice into a correct\n'
        '  word. 1.3.12 makes एध् ātmanepada, 3.4.78 gives त, and without\n'
        '  this the derivation stops at एधत.'
    ),
)


__all__ = [
    'tit_atmanepada',
    'sarvadhatuka',
]


# -------------------------------------------------------------------------
# 3.4.1 to 3.4.12 — धातुसंबन्ध, and what stands under it.
#
# The pāda opens on a licence rather than a rule: where two root-senses
# stand in a relation, an affix given for the wrong TIME is correct
# anyway. Everything to 3.4.8 stands under that, which is why those
# rules hold सर्वेषु कालेषु — in every time at once — where each rule
# of 3.2 and 3.3 chose an ending FOR a time.
# -------------------------------------------------------------------------

_SAMBANDHA_LINE = (
    'dhatu_sambandha(related=..., taddhita=...) -> whether an affix out '
    'of its proper time stands, and why.'
)

_ANUPRAYOGA_LINE = (
    'anuprayoga(gathered=..., kashadi=...) -> which root is to be said '
    'after, and whether the rule prescribes it or merely restricts it.'
)

_LAKARA_LINE = (
    'lakara_for(time=..., chandasi=..., doubled=..., sense=..., '
    'lin_nimitta=...) -> which tense-ending comes, and by which rule. '
    'The same table 3.2.110 onward answer from.'
)

_TUMARTHA_LINE = (
    'tumartha_affix(beside=..., wants=...) -> which affix comes in the '
    'sense of तुमुन् in the Veda.'
)

_FIXED_LINE = (
    'nipatana(word) -> a Vedic form the grammar fixes outright, with '
    'what the vṛtti says is being fixed in it.'
)

_RULES = {
    "3.4.1": "SETTLED — धातुसंबन्धे प्रत्ययाः, AND THE PĀDA OPENS ON A QUESTION\n  NEITHER 3.2 NOR 3.3 ASKED. Where two root-senses stand in a\n  relation of qualifier and qualified, अयथाकालोक्ता अपि प्रत्ययाः\n  साधवो भवन्ति — affixes stated for the WRONG TIME are correct:\n  अग्निष्टोमयाज्यस्य पुत्रो जनिता, the first word of the past and\n  the second of the future.\n\nSETTLED — broader than 3.3.131's transfers, which lent one NAMED\n  tense's affixes to a NAMED time. Nothing is lent here: the\n  ordinary affix is simply not wrong.\n\nSETTLED — AND ONLY ONE WAY ROUND. विशेषणं गुणत्वाद्\n  विशेष्यकालमनुरुध्यते, तेन विपर्ययो न भवति — the QUALIFIER\n  accommodates the qualified's time, being subordinate, and not\n  the reverse. An asymmetry the rule does not state.\n\nSETTLED — प्रत्ययाधिकारे पुनः प्रत्ययग्रहणम्: the word प्रत्यय is\n  repeated though the section is already about affixes, SO THAT\n  affixes given OUTSIDE the root section are reached — गोमान्\n  आसीत्, गोमान् भविता, a तद्धित given for the present standing in\n  another time. A repetition that WIDENS, the fifth use of that\n  device after 3.2.106, 3.2.124, 3.3.44 and 3.3.156.",
    "3.4.2": 'SETTLED — क्रियासमभिहारे लोट्, सर्वलकाराणामपवादः, and it holds IN\n  ALL TIMES AT ONCE: सर्वेषु कालेषु — भूते अलावीत्, भविष्यति\n  लविष्यति. No rule of 3.2 or 3.3 gave one ending for every time;\n  each of those chose an ending FOR a time. That is what standing\n  under 3.4.1 buys.\n\nSETTLED — AND THE ENDING IS THEN REPLACED, WHICH THE RULE DOES\n  NOT SAY. तस्य च लोटो हि स्व इत्येतावादेशौ भवतः, and the vṛtti\n  asks for a योगविभाग to get it. Read so, लोड्धर्माणौ हिस्वौ\n  भवतः — they merely BEHAVE like लोट्, तेनात्मनेपदपरस्मैपदत्वं\n  भेदेनावतिष्ठते, so the distinction of voice survives the\n  substitution. A योगविभाग asked for in order to keep a property\n  from being lost, which none of the five before it was.\n\nSETTLED — क्रियासमभिहाराभिव्यक्तौ द्विर्वचनमयं लोडपेक्षते (वा०\n  ८.१.१२): this ending NEEDS the doubling to show the sense,\n  where यङ्, given for that same sense, स्वयमेव शक्तत्वाद्\n  नापेक्षते द्विर्वचनम्. Two routes to one meaning and only one\n  self-sufficient. 3.1.22 यङ् is codified.',
    "3.4.3": 'SETTLED — समुच्चये सामान्यवचनस्य, अन्यतरस्याम्.\n  अनेकक्रियाध्याहारः समुच्चयः.\n\nSETTLED — AND THE VṚTTI WRITES OUT THE LONGEST WORKED EXAMPLE IN\n  THESE FOUR PĀDAS: the whole paradigm twice over, in both\n  voices, for two roots, and then the alternative reading with\n  the ordinary present ending — अथवा भ्राष्ट्रमटति, मठमटति ...\n  इत्येवायमटति. Every form of it is the same sentence with one\n  ending changed, which is the only way to show what an option\n  over a whole paradigm comes to.',
    "3.4.4": 'SETTLED — यथाविध्यनुप्रयोगः, AND IT ASKS SOMETHING NO RULE OF 3.2\n  OR 3.3 ASKED: given that a rule has doubled a verb, WHICH root\n  is said after it. यस्माद् धातोर्लोड् विहितः, स एव\n  धातुरनुप्रयोक्तव्यः — the same one. लुनीहिलुनीहीत्येवायं\n  लुनाति, and छिनत्तीति नानुप्रयुज्यते.\n\nSETTLED — धातुसंबन्धे प्रत्ययविधानादनुप्रयोगः सिद्ध एव,\n  यथाविध्यर्थं तु वचनम्: that SOMETHING is said after follows\n  from 3.4.1 already, and what this rule adds is WHICH. A rule\n  stated for half of what it appears to say.',
    "3.4.5": "SETTLED — समुच्चयेऽन्यतरस्याम्: where several acts are gathered,\n  one root COVERING them all — ओदनं भुङ्क्ष्व, सक्तून् पिब,\n  धानाः खाद इत्येवायमभ्यवहरति. सर्वविशेषानुप्रयोगनिवृत्त्यर्थं\n  वचनम्.\n\nSETTLED — AND A REMARK THAT IS NOT ABOUT GRAMMAR AT ALL. लाघवं च\n  लौकिके शब्दव्यवहारे नाद्रियते — BREVITY IS NOT A CONSIDERATION\n  IN ORDINARY SPEECH. The tradition prizes brevity in the sūtras\n  above almost everything, and here it says the value does not\n  apply to the language the sūtras describe. Recorded because it\n  is a statement about the grammar's own method, made in\n  passing.",
    "3.4.6": 'SETTLED — छन्दसि लुङ्लङ्लिटः, AND A DEBT CARRIED SINCE 3.2 IS\n  PAID. 3.2.105 cited this rule and could only record it; it is\n  codified now and the citation can be run. One of the three\n  3.4 debts NORTH_STAR has been carrying.\n\nSETTLED — THREE PAST ENDINGS USED FOR ANY TIME AT ALL, in the\n  Veda: धातुसंबन्धे सर्वेषु कालेषु. लुङ् — अहं तेभ्योऽकरं नमः\n  (मा०सं० १६.८); लङ् — अवृणीतायं यजमानः (शा०श्रौ० ५.२०.५); लिट्\n  — अद्या ममार (ऋ० १०.५५.५), glossed अद्य म्रियते, a perfect\n  meaning a present.\n\nSETTLED — and the option carries down: अन्यतरस्यामिति वर्तते,\n  तेनान्येऽपि लकारा यथायथं भवन्ति — OTHER endings stand too, as\n  each fits. The rule names three and licenses more.',
    "3.4.7": "SETTLED — लिङर्थे लेट्, छन्दसि. लेट् is an ending the Veda alone\n  has, and this is the first rule of the project to give it.\n\nSETTLED — AND ITS CONDITION IS THE ONE 3.3.139 INTRODUCED.\n  लिङर्थे, यत्र लिङ् विधीयते विध्यादिः, हेतुहेतुमतोर्लिङ्\n  इत्येवमादिः — wherever a rule gives लिङ्. The same appeal to\n  the grammar's own state, and the same rule cited for it,\n  thirteen sūtras into another pāda. 3.3.156 is codified, so the\n  condition can be checked from here.",
    "3.4.8": "SETTLED — उपसंवादाशङ्कयोश्च. उपसंवादः परिभाषणम्, कर्तव्ये\n  पणबन्धः — a bargain about what is to be done, and the vṛtti\n  gives the whole shape of one: यदि मे भवानिदं कुर्याद् अहमपि\n  भवत इदं दास्यामीति.\n\nSETTLED — लिङर्थ एवायं नित्यार्थं तु वचनम्: the ground is\n  3.4.7's already and the rule exists to make it OBLIGATORY, the\n  option having run there. A rule stated to remove a choice, as\n  3.3.66's नित्यम् was — and by naming no new condition, only a\n  narrower sense.",
    "3.4.9": 'SETTLED — तुमर्थे सेसेनसेअसेन्... — FIFTEEN AFFIXES IN ONE RULE,\n  each with its Vedic passage: वक्षे रायः; ता वामेषे रथानाम् (ऋ०\n  ५.६६.३); क्रत्वे दक्षाय जीवसे (शौ०सं० ६.१९.२); वायवे पिबध्यै\n  (ऋ० ७.९२.२); दशमे मासि सूतवे (ऋ० १०.१८४.३). More affixes than\n  any single rule of 3.2 or 3.3 gave.\n\nSETTLED — AND THE VṚTTI PROVES WHAT तुमर्थ MEANS RATHER THAN\n  ASSERTING IT, in four steps. तुमर्थो भावः — कथं ज्ञायते?\n  वचनसामर्थ्यात् तावदयं कर्तुरपकृष्यते; न चान्यस्मिन्नर्थे\n  तुमुन्नादिश्यते; अनिर्दिष्टार्थाश्च प्रत्ययाः स्वार्थे भवन्ति\n  (परि० ११३); स्वार्थश्च धातूनां भाव एव. A paribhāṣā cited BY\n  NUMBER to settle what one word of a rule means.\n\nSCAR — TWO PAIRS DIFFER IN ACCENT ALONE: स्वरे विशेषः of असे\n  against असेन्, and of अध्यै against अध्यैन्. The sūtrapāṭha on\n  disk is unaccented, so both are recorded and neither can be\n  checked — the boundary five rules of 3.3 ran into, met again\n  in the first dozen rules of this pāda.',
    "3.4.10": "SETTLED — प्रयै रोहिष्यै अव्यथिष्यै च, three निपातन and TWO\n  DIFFERENT AFFIXES between them: प्रपूर्वस्य यातेः कैप्रत्ययः,\n  रुहेरिष्यैप्रत्ययः, व्यथेर्नञ्पूर्वस्येष्यैप्रत्ययः. Which is\n  why each entry carries its own affix — the correction 3.2's\n  निपातन table needed within five rules of being written, kept\n  here from the start.\n\nSETTLED — and one of the three is a NEGATED stem: व्यथ् with नञ्\n  before it, so what is fixed is not a root but a root already\n  denied. अव्यथिष्यै (काठ०सं० ३.७), अव्यथनाय.",
    "3.4.11": 'SETTLED — दृशे विख्ये च, two निपातन with one affix: दृशेः\n  केप्रत्ययः. दृशे विश्वाय सूर्यम् (ऋ० १.५०.१), द्रष्टुम्;\n  विख्ये त्वा हरामि, विख्यातुम्.\n\nSETTLED — and the second rests on ख्या, which 3.2.7 had to note\n  is NOT a root of the dhātupāṭha at all but what चक्षिङ् becomes\n  by 2.4.54. Both those rules are codified, so a fixed word here\n  stands on a substitution settled two adhyāyas back.',
    "3.4.12": 'SETTLED — शकि णमुल्कमुलौ, छन्दसि, in the sense of तुमुन्: अग्निं\n  वै देवा विभाजं नाशक्नुवन् (मै०सं० १.६.४), विभक्तुम्.\n\nSETTLED — THREE MARKS, EACH DOING SOMETHING DIFFERENT, AND TWO\n  OF THEM OPPOSITE. णकारो वृद्ध्यर्थः — the ण for the\n  strengthening; ककारो गुणवृद्धिप्रतिषेधार्थः — the क to FORBID\n  both strengthenings; लकारः स्वरार्थः — the ल for the accent.\n  So two affixes differing in one letter do contrary things to\n  the root, and the letter they share does neither.',
    "3.4.13": "SETTLED — ईश्वरे तोसुन्कसुनौ: ईश्वरोऽभिचरितोः, ईश्वरो विलिखः,\n  ईश्वरो वितृदः. Two affixes, and the vṛtti's three examples\n  divide between them without the rule saying which goes where —\n  no यथासंख्यम् and no other ground stated, so the codification\n  offers both and records the silence.",
    "3.4.14": 'SETTLED — कृत्यार्थे तवैकेन्केन्यत्वनः, छन्दसि. कृत्यानामर्थो\n  भावकर्मणी, so this is NOT the तुमुन् sense the rules before it\n  had.\n\nSETTLED — AND ONE AFFIX IS GIVEN TWICE, IN TWO SENSES. तुमर्थे\n  छन्दसीति सयादिसूत्रेऽपि तवै विहितः, तस्य तुमर्थादन्यत्र कारके\n  विधिर्द्रष्टव्यः — तवै was already given at 3.4.9 in the sense\n  of तुमुन्, so ITS statement here must be for some other kāraka.\n  A rule read as being about only PART of what it lists, and the\n  reason is that the rest would be redundant. The same ground\n  3.3.107 used to pick between two roots spelt alike.',
    "3.4.15": "SETTLED — अवचक्षे च, a निपातन: रिपुणा नावचक्षे (मा०सं० १७.९३),\n  नावख्यातव्यमित्यर्थः. अवपूर्वाच् चक्षिङ एश् प्रत्ययो निपात्यते.\n  A fixed word standing in the middle of a run and sharing the\n  run's condition — the कृत्य sense from 3.4.14 — rather than\n  being self-contained as most निपातन are.",
    "3.4.16": "SETTLED — भावलक्षणे स्थेण्कृञ्वदिचरिहुतमिजनिभ्यस्तोसुन्, eight\n  roots with their passages: आ संस्थातोर्वेद्यां शेरते (काठ०सं०\n  ११.६); पुरा सूर्यस्योदेतोराधेयः (काठ०सं० ८.३); आ तमितोरासीत\n  (तै०ब्रा० १.४.४.५); आ विजनितोः संभवाम (तै०सं० २.५.१.५).\n\nSETTLED — भावो लक्ष्यते येन तस्मिन्नर्थे: the root's sense is\n  what MARKS OUT a state, so the word comes to mean 'until' or\n  'before' and not the act itself. प्रकृत्यर्थविशेषणं\n  भावलक्षणग्रहणम् — qualifying the ROOT's sense, the distinction\n  3.3.161 and 3.3.172 drew between the two kinds of semantic\n  condition.",
    "3.4.17": "SETTLED — सृपितृदोः कसुन्: पुरा क्रूरस्य विसृपो विरप्शिन् (तै०सं०\n  १.१.९.३); पुरा जत्रुभ्य आतृदः (ऋ० ८.१.१२). Two roots taking the\n  other of 3.4.13's pair, in the same sense as the rule before.",
    "3.4.18": "SETTLED — अलंखल्वोः प्रतिषेधयोः प्राचां क्त्वा, AND A RULE GIVEN\n  ON A NAMED SCHOOL'S AUTHORITY — प्राचामाचार्याणां मतेन, the\n  teachers of the EAST. Nothing in 3.2 or 3.3 attributed a rule\n  this way.\n  प्राचांग्रहणं विकल्पार्थम् — and naming them is itself what\n  makes it optional, the other usage standing too: अलं रोदनेन.\n\nSETTLED — BOTH conditions tested. अलंखल्वोरिति किम्? मा कार्षीः.\n  प्रतिषेधयोरिति किम्? अलंकारः — where अलम् means ornament and\n  not 'enough'. The two words must be there AND be forbidding.\n\nSCOPE — वासरूपविधिश्चेत् पूजार्थम्: if 3.1.94 is invoked here it\n  is FOR HONOURING THE TEACHERS and not for the grammar. A\n  principle cited as a courtesy, which nothing else in these four\n  pādas does.",
    "3.4.19": "SETTLED — उदीचां माङो व्यतीहारे: अपमित्य याचते, अपमित्य हरति.\n  The NORTHERN teachers this time, and उदीचांग्रहणात् तु\n  यथाप्राप्तमपि भवति — याचित्वापमयते. Two adjacent rules, two\n  schools, the same device in both.\n  अपूर्वकालत्वादप्राप्तः क्त्वा विधीयते: the affix is given where\n  3.4.21 could not reach, the borrowing not being the earlier act.\n\nSETTLED — AND A ज्ञापक FROM HOW THE ROOT IS SPELT. मेङः\n  कृतात्वस्यायं निर्देशः कृतो ज्ञापनार्थः — the rule writes मा,\n  the shape मेङ् takes AFTER its vowel-change, and that spelling\n  tells us नानुबन्धकृतमनेजन्तत्वम्: a marker does not make a stem\n  count as not-ending-in-a-diphthong. तेन दाधा घ्वदाप् इति\n  दैपोऽपि प्रतिषेधो भवति — so 1.1.20's exclusion reaches दैप्.\n  A spelling in one rule settling the membership of a class three\n  adhyāyas back, and 1.1.20 is codified. The third ज्ञापक of this\n  project drawn from orthography, after 3.2.182's and 3.3.16's.",
    "3.4.20": 'SETTLED — परावरयोगे च: अप्राप्य नदीं पर्वतः स्थितः; अतिक्रम्य तु\n  पर्वतं नदी स्थिता.\n  परेण पूर्वस्य योगे गम्यमानेऽवरेण च परस्य — the earlier thing\n  tied to what is FURTHER, or the later to what is NEARER, and\n  the vṛtti says which is qualified by which in each case.\n  A condition about how two things are PLACED, where every\n  condition of these four pādas has been about an act, a sense, a\n  form or a speaker.',
    "3.4.21": 'SETTLED — समानकर्तृकयोः पूर्वकाले, THE RULE THE RUN STANDS ON:\n  भुक्त्वा व्रजति. Its two conditions carry a long way forward.\n\nSETTLED — शक्तिशक्तिमतोर्भेदस्याविवक्षितत्वात् समानकर्तृकता: the\n  sameness of doer holds because the difference between a POWER\n  and WHAT HAS IT is not meant to be marked. A philosophical\n  ground offered for a grammatical condition, and the first of\n  its kind in this reading.\n\nSETTLED — द्विवचनमतन्त्रम्: the DUAL in the rule is not binding,\n  so more than two acts are reached — स्नात्वा पीत्वा भुक्त्वा\n  दत्त्वा व्रजति. The same reading 3.3.18 gave its own masculine\n  singular, and both are cases of a grammatical form inside a\n  rule not meaning what that form means anywhere else.\n\nSCOPE — आस्यं व्यादाय स्वपिति, चक्षुः संमील्य हसति\n  इत्युपसंख्यानम्, अपूर्वकालत्वात्: two forms where the acts are\n  SIMULTANEOUS and the affix comes anyway.',
    "3.4.22": 'SETTLED — आभीक्ष्ण्ये णमुल् च: भोजंभोजं व्रजति, पायंपायं व्रजति.\n\nSETTLED — AND NEITHER AFFIX SHOWS THE SENSE ALONE.\n  द्विर्वचनसहितौ क्त्वाणमुलावाभीक्ष्ण्यं द्योतयतः, न केवलौ —\n  only WITH the doubling, आभीक्ष्ण्ये द्वे भवतः (वा० ८.१.१२)\n  supplying it. The same vārttika 3.4.2 needed for the same\n  reason: an affix that cannot carry its own sense.',
    "3.4.23": 'SETTLED — न यद्यनाकाङ्क्षे: यदयं भुङ्क्ते ततः पठति. यत्र\n  पूर्वोत्तरे क्रिये स्तः, तच्चेद् वाक्यं न परं किञ्चिदाकाङ्क्षति.\n  अनाकाङ्क्ष इति किम्? यदयं भुक्त्वा व्रजति अधीत एव ततः परम्.\n\nSETTLED — A प्रतिषेध REACHING BACKWARD PAST ITS NEIGHBOUR.\n  णमुलनन्तरः, क्त्वा तु पूर्वसूत्रविहितोऽपि प्रतिषिध्यते — णमुल्\n  is given in the rule immediately before, but क्त्वा comes from\n  3.4.21, and BOTH are refused. 3.3.45 showed the nearest word\n  losing to a further one in an अनुवृत्ति; this shows a refusal\n  reaching past its neighbour to take in an earlier rule as well.\n\nSETTLED — and the refusal NAMES ITSELF, refusing being the whole\n  of what it does: the case 3.2.23 marked off as the one where a\n  प्रतिषेध may be reported.',
    "3.4.24": 'SETTLED — विभाषाग्रेप्रथमपूर्वेषु, अप्राप्तविभाषेयम्.\n  विभाषाग्रहणमेताभ्यां मुक्ते लडादयोऽपि यथा स्युः — the option is\n  there so the ordinary endings may come instead.\n\nSETTLED — AND A SEVENTH SUSPENSION OF 3.1.94, ON A GROUND NONE OF\n  THE SIX USED. ननु च वासरूप इति भविष्यति? — could that principle\n  not have let them stand beside anyway? — क्त्वाणमुलौ यत्र सह\n  विधीयेते तत्र वासरूपविधिर्नास्तीत्येतदनेन ज्ञाप्यते: WHEREVER\n  THESE TWO AFFIXES ARE GIVEN TOGETHER the principle does not\n  hold, तेनाभीक्ष्ण्ये लडादयो न भवन्ति.\n  The six before it bounded the suspension by SECTION — the\n  तच्छीलादि run, the क्रियार्थ ground, the feminine section and\n  what follows it. This bounds it by a PAIR OF AFFIXES, wherever\n  in the grammar they happen to occur together.\n\nSCOPE — उपपदसमासः कस्माद् न भवति? अमैव यत्तुल्यविधानम् उपपदं तत्\n  समस्यते, नान्यदिति: no compound forms here, on the strength of\n  a word in 2.2.19.',
    "3.4.25": "SETTLED — कर्मणि भृत्यादिषु खमुञ्, आक्रोशे: चोरंकारमाक्रोशति.\n  From here the companion is the OBJECT of the act and not a\n  particle, which is what कर्मणि brings down.\n\nSETTLED — AND THE ACT THE RULE NAMES IS NOT DONE. चोरकरणम्\n  आक्रोशसंपादनार्थमेव, न त्वसौ चोरः क्रियते — the 'making' is only\n  for the abusing, and nobody is actually made a thief. A rule\n  whose form says one thing and whose sense is another, and the\n  vṛtti has to say so outright.",
    "3.4.26": "SETTLED — स्वादुमि णमुल्: स्वादुंकारं भुङ्क्ते.\n\nSETTLED — ONE SPELLING IN THE RULE DOING THREE THINGS. स्वादुमीति\n  मकारान्तनिपातनम्, and the vṛtti lists what the fixed म-final\n  shape buys: ईकाराभावार्थम्, no feminine ई; च्व्यन्तस्यापि\n  मकारार्थम्, a च्वि-stem gets the म too; दीर्घाभावार्थं च, no\n  lengthening. 3.4.12 had three MARKS each doing one thing; this\n  is one choice carrying three consequences.\n\nSETTLED — AND 3.4.21's PHILOSOPHICAL GROUND IS USED THE OTHER WAY\n  ROUND. That rule held समानकर्तृकता BECAUSE\n  शक्तिशक्तिमतोर्भेदस्याविवक्षितत्वात्; this one says न चास्मिन्\n  प्रकरणे शक्तिशक्तिमतोर्भेदो विवक्ष्यते, समानकर्तृकत्वं हि\n  विरुध्यते — the distinction is not drawn here BECAUSE drawing it\n  would contradict the condition. The same ground reached for\n  twice, five sūtras apart, and pointed in opposite directions.\n\nSCOPE — वासरूपेण क्त्वापि भवति, स्वादुं कृत्वा भुङ्क्ते: and\n  3.1.94 lets क्त्वा stand beside, the suspension 3.4.24\n  establishes reaching only where the two affixes are given\n  TOGETHER.",
    "3.4.27": "SETTLED — कर्मण्यन्यथैवंकथमित्थंसु, सिद्धाप्रयोगश्चेत्.\n\nSETTLED — AND THE CONDITION IS THAT THE ROOT ADD NOTHING. कथं\n  पुनरसौ सिद्धाप्रयोगः? निरर्थकत्वाद् न प्रयोगमर्हतीत्येवमेव\n  प्रयुज्यते: 'made' contributes no meaning and is used only as a\n  matter of form — अन्यथा भुङ्क्त इति यावानर्थः, तावानेव\n  अन्यथाकारं भुङ्क्त इति गम्यते, the compound means exactly what\n  the two words meant.\n  3.3.154 made a condition of a WORD being meant and not said;\n  this makes one of a ROOT adding nothing to what is said. Two\n  conditions about absence, and neither is about a form.\n\nSETTLED — सिद्धाप्रयोग इति किम्? अन्यथा कृत्वा शिरो भुङ्क्ते,\n  where the making is real.",
    "3.4.28": "SETTLED — यथातथयोरसूयाप्रतिवचने: यथाकारमहं भोक्ष्ये तथाकारमहम्,\n  किं तवानेन?\n  यद्यसूयन् पृच्छति प्रतिवक्ति तत्र प्रतिवचनम् — the condition is\n  on ANSWERING somebody who asks in resentment, so it is about a\n  whole exchange and not about one speaker. The nearest thing to\n  it in these pādas is 3.2.120's पृष्टप्रतिवचन, and that wanted\n  only that an answer be given.",
    "3.4.29": "SETTLED — कर्मणि दृशिविदोः साकल्ये: कन्यादर्शं वरयति, यायाः\n  कन्याः पश्यति तास्ता वरयति.\n  साकल्य is exhaustiveness of the OBJECTS and not of the act:\n  साकल्य इति किम्? ब्राह्मणं दृष्ट्वा भोजयति, where one brahmin\n  is seen and fed.\n\nSETTLED — and the vṛtti gives THREE senses for विद् before\n  settling that all are reached: यंयं ब्राह्मणं जानाति लभते\n  विचारयति वा. A root ambiguity resolved by taking every reading\n  rather than choosing — the opposite of 3.3.30's अनभिधानात् and\n  3.3.107's redundancy argument.",
    "3.4.30": "SETTLED — यावति विन्दजीवोः: यावद्वेदं भुङ्क्ते, यावज्जीवमधीते.\n  The compound means 'as much as' with one root and 'as long as'\n  with the other, and the rule says neither — the vṛtti gets both\n  by paraphrasing each separately.",
    "3.4.31": 'SETTLED — चर्मोदरयोः पूरेः: चर्मपूरं स्तृणाति, उदरपूरं भुङ्क्ते.',
    "3.4.32": "SETTLED — वर्षप्रमाण ऊलोपश्चास्यान्यतरस्याम्: गोष्पदपूरं and\n  गोष्पदप्रं वृष्टो देवः — rain measured by what it fills.\n\nSETTLED — AND ONE WORD SAYS WHICH OF TWO ADJACENT THINGS THE\n  OPERATION TOUCHES. अस्यग्रहणं किमर्थम्? उपपदस्य मा भूत् — अस्य\n  is there so the vowel-loss falls on the ROOT and not on the\n  companion: मूषिकाबिलपूरं keeps its own ऊ and only the root's\n  goes. A word spent entirely on scope.",
    "3.4.33": "SETTLED — चेलार्थेषु क्नूयेर्ण्यन्तस्य वर्षप्रमाणे: चेलक्नोपं\n  वृष्टो देवः.\n  The companion is named BY SENSE — चेलार्थेषु, words meaning\n  cloth — so the three the vṛtti gives are examples and not a\n  list, as 3.2.5's गण members were.",
    "3.4.34": 'SETTLED — निमूलसमूलयोः कषः: निमूलकाषं कषति.\n\nSETTLED — AND THE VṚTTI MARKS THE START OF A GROUP HERE. इतः\n  प्रभृति कषादीन् यान् वक्ष्यति, तत्र कषादिषु\n  यथाविध्यनुप्रयोगः — from this rule on the roots named form a\n  class called कषादि, and 3.4.46 will require the SAME root to be\n  said after each. A group defined by where a run BEGINS rather\n  than by a list, and named after its first member.\n  DEBT — 3.4.46 is not codified, so the class is recorded and its\n  consequence cannot be run.',
    "3.4.35": 'SETTLED — शुष्कचूर्णरूक्षेषु पिषः: शुष्कपेषं पिनष्टि. And each is\n  glossed by DROPPING the affix — शुष्कं पिनष्टीत्यर्थः — which\n  is the सिद्धाप्रयोग reading of 3.4.27 met again without being\n  named as one.',
    "3.4.36": 'SETTLED — समूलाकृतजीवेषु हन्कृञ्ग्रहः, यथासंख्यम्: समूलघातं\n  हन्ति, अकृतकारं करोति, जीवग्राहं गृह्णाति. Three companions\n  bound to three roots, so the row holds pairs and the lists may\n  not be crossed — the device 3.2.5 established and 3.3.37\n  stretched to three lists at once.',
    "3.4.37": "SETTLED — करणे हनः. From here the run divides by WHICH kāraka the\n  companion is, where 3.4.25 to 3.4.36 all wanted the object.\n\nSETTLED — AND AN EARLIER RULE IS MADE TO WIN OVER A LATER ONE.\n  3.4.48 gives णमुल् for roots meaning HARM, so this rule is\n  needless for those — अहिंसार्थोऽयमारम्भः. But पूर्वविप्रतिषेधेन\n  हन्तेर्हिंसार्थस्यापि प्रत्ययोऽनेनैवेष्यते: by PRIOR\n  CONTRADICTION the affix comes by THIS rule even in that sense,\n  असिघातं हन्ति.\n  परत्व — a later rule winning — was 3.3.142's ground.\n  पूर्वविप्रतिषेध is its reverse and has to be asked for. The\n  resolver reaches the same answer by specificity, so the two\n  grounds agree here without having to, and that is recorded\n  rather than relied on.",
    "3.4.38": 'SETTLED — स्नेहने पिषः. स्निह्यते येन तत् स्नेहनम् — what one\n  moistens with, so the sense qualifies the KARAṆA and not the\n  act.',
    "3.4.39": 'SETTLED — हस्ते वर्तिग्रहोः. हस्त इत्यर्थग्रहणम् — the word is\n  taken BY SENSE, so कर and पाणि are reached too and the three\n  forms given are examples rather than a list. The same reading\n  3.3.33 and 3.4.33 gave their own companions.',
    "3.4.40": "SETTLED — स्वे पुषः, and स्व इत्यर्थग्रहणम् again — with the\n  vṛtti giving the word's whole range:\n  आत्मात्मीयज्ञातिधनवचनः स्वशब्दः, oneself, one's own, one's kin,\n  one's wealth. Seven examples running across four senses of one\n  word, and the rule says none of them.",
    "3.4.41": 'SETTLED — अधिकरणे बन्धः: चक्रबन्धं बध्नाति, चोरकबन्धं\n  बध्नाति, चोरके बध्नातीत्यर्थः.',
    "3.4.42": 'SETTLED — संज्ञायाम्: क्रौञ्चबन्धं बध्नाति, मयूरिकाबन्धम्.\n  बन्धविशेषाणां नामधेयान्येतानि — names of particular knots. The\n  same root as the rule before and NO kāraka named: what carries\n  this one is that the whole word is a name.',
    "3.4.43": 'SETTLED — जीवपुरुषयोर्नशिवहोः, यथासंख्यम्: जीवनाशं नश्यति,\n  पुरुषवाहं वहति, पुरुषः प्रेष्यो भूत्वा वहतीत्यर्थः.\n  कर्तरीति किम्? जीवेन नष्टः, पुरुषेणोढः — the same two words as\n  the MEANS, and the rule does not reach them.',
    "3.4.44": 'SETTLED — ऊर्ध्वे शुषिपूरोः, कर्तृग्रहणम् running down from\n  3.4.43: ऊर्ध्वशोषं शुष्यति, ऊर्ध्वं शुष्यतीत्यर्थः.',
    "3.4.45": 'SETTLED — उपमाने कर्मणि च, and by the च the AGENT as well:\n  घृतनिधायं निहितः, घृतमिव निहितः; अजकनाशं नष्टः, अजक इव नष्टः.\n  उपमीयतेऽनेनेत्युपमानम्.\n  3.2.79 and 3.2.101 had उपमान as a ROLE the companion plays;\n  here it is the kāraka itself, which is why it sits in this run\n  beside करण and अधिकरण.',
    "3.4.46": 'SETTLED — कषादिषु यथाविध्यनुप्रयोगः, AND THE DEBT 3.4.34\n  RECORDED IS PAID. That rule said इतः प्रभृति कषादीन् यान्\n  वक्ष्यति — from there the roots named form the कषादि class,\n  called after its first member — and this is the rule that\n  governs them.\n  A class defined by where a run BEGINS. Every gaṇa met before\n  this was a list, and two of them are on disk.\n\nSETTLED — AND IT IS RESTRICTIVE AND NOT PRESCRIPTIVE. ननु\n  धातुसंबन्धे प्रत्ययविधानादनुप्रयोगः सिद्ध एव? — that SOMETHING\n  is said after follows from 3.4.1 already. यथाविधीति नियमार्थं\n  वचनम्: the statement is for the RESTRICTION, that it be the\n  same root and no other. Word for word the argument 3.4.4 made\n  about itself, twenty-two sūtras earlier, and the two rules do\n  the same work for two different runs.',
    "3.4.47": "SETTLED — उपदंशस्तृतीयायाम्. FROM HERE THE RULES DIVIDE BY THE\n  COMPANION'S CASE-ENDING rather than by its role — a condition\n  on the SURFACE FORM of the companion, which no pāda before this\n  used.\n  And 3.4.47 shows why it must be the case and not the kāraka:\n  मूलकादि चोपदंशेः कर्म, भुजेः करणम् — the same word is the\n  OBJECT of one verb and the MEANS of the other, so no single\n  role could have been named.\n\nSETTLED — AND 3.4.24's SUSPENSION IS QUALIFIED FROM INSIDE.\n  सर्वस्मिन्नेवात्र णमुल्प्रकरणे क्रियाभेदे सति वासरूपविधिना\n  क्त्वापि भवति: throughout this णमुल् section क्त्वा stands\n  beside by 3.1.94 WHERE THE ACTS DIFFER — मूलकेनोपदश्य भुङ्क्ते.\n  3.4.24 had said the principle does not hold wherever the two\n  affixes are given together; this says it holds again once the\n  acts are distinct. The seventh suspension, bounded from inside\n  twenty-three sūtras later, and the bound is a condition on the\n  situation rather than on the rules.\n\nSCOPE — अत्र विकल्पेनोपपदसमासः, 2.2.21 being codified, so both\n  the compounded and the uncompounded form are given for each\n  example.",
    "3.4.48": "SETTLED — हिंसार्थानां च समानकर्मकाणाम्. हिंसा प्राण्युपघातः.\n  समानकर्मकाणामिति किम्? चोरं दण्डेनोपहत्य गोपालको गाः कालयति —\n  the thief is struck while the cattle are driven, so the objects\n  differ.\n  3.4.21's condition was one DOER for both acts; this is one\n  OBJECT, and it is stated afresh rather than inherited — the two\n  are independent, and a rule needing the second says so.",
    "3.4.49": 'SETTLED — सप्तम्यां चोपपीडरुधकर्षः, and by the च the third case\n  too, so three forms stand for each example.\n\nSETTLED — उपशब्दः प्रत्येकमभिसंबध्यते: the उप is to be joined to\n  EACH of the three roots separately, which the compound in the\n  rule does not show and only the examples reveal.\n  And कर्षतेरिदं ग्रहणम्, न कृषतेः — the root meant is the one\n  meaning to drag and not the one meaning to plough. Two roots\n  spelt alike, settled by simply naming which, where 3.2.162 used\n  स्वभावात्, 3.3.30 अनभिधानात् and 3.3.107 redundancy.',
    "3.4.50": 'SETTLED — समासत्तौ. समासत्तिः सन्निकर्षः, and the vṛtti sets the\n  scene: युद्धसंरम्भादत्यन्तं सन्निकृष्यन्त इत्यर्थः — in the\n  fury of a fight they come to close quarters, and so seize each\n  other by the hair.',
    "3.4.51": "SETTLED — प्रमाणे. प्रमाणमायामः, दैर्घ्यम् — the measure meant is\n  LENGTH in particular, which the word alone does not say and the\n  examples (two fingers, three fingers) confirm. 3.3.20's\n  परिमाणाख्या had been widened by आख्या to take in number; this\n  is narrowed by a gloss to take in only extension.",
    "3.4.52": 'SETTLED — अपादाने परीप्सायाम्. परीप्सा त्वरा.\n\nSETTLED — AND THE VṚTTI PAINTS THE HASTE RATHER THAN GLOSSING IT:\n  एवं नाम त्वरते यदवश्यं कर्तव्यमपि नापेक्षते,\n  शय्योत्त्थानमात्रमाद्रियते — such is his hurry that he does not\n  attend even to what must be done, and cares for nothing but\n  getting out of bed. परीप्सायामिति किम्? आसनादुत्त्थाय गच्छति.',
    "3.4.53": 'SETTLED — द्वितीयायां च, and the scene again: एवं नाम त्वरते यद्\n  आयुधग्रहणमपि नाद्रियते, लोष्टादिकं यत् किञ्चिदासन्नं तद्\n  गृह्णाति — in such haste that he does not stop for a weapon and\n  snatches up whatever clod is nearest. Two rules in a row\n  glossed by dramatising the sense.',
    "3.4.54": 'SETTLED — स्वाङ्गेऽध्रुवे: अक्षिनिकाणं जल्पति, भ्रूविक्षेपं\n  कथयति. अध्रुव इति किम्? उत्क्षिप्य शिरः कथयति.\n\nSETTLED — AND अध्रुव IS DEFINED BY WHAT SURVIVES ITS LOSS:\n  यस्मिन्नङ्गे छिन्नेऽपि प्राणी न म्रियते तदध्रुवम् — a limb\n  whose cutting off does not kill. A grammatical condition\n  defined by a fact about bodies, and स्वाङ्ग itself quoted from\n  another rule: अद्रवं मूर्तिमत्स्वाङ्गम्.',
    "3.4.55": "SETTLED — परिक्लिश्यमाने च. परिक्लेशः सर्वतो विबाधनम्, दुःखनम्,\n  and कृत्स्नमुरः पीडयन्तो युध्यन्ते — the whole chest crushed.\n  ध्रुवार्थोऽयमारम्भः: the rule exists for the limbs 3.4.54's\n  अध्रुव shut out, so the pair covers the body between them.",
    "3.4.56": "SETTLED — विशिपतिपदिस्कन्दां व्याप्यमानासेव्यमानयोः.\n\nSETTLED — TWO SENSES, AND THE DOUBLING FALLS ON DIFFERENT WORDS\n  IN EACH. द्रव्ये व्याप्तिः, क्रियायामासेवा, so\n  असमासपक्षे व्याप्यमानतायां द्रव्यवचनस्य द्विर्वचनम्,\n  आसेव्यमानतायां तु क्रियावचनस्य: गेहंगेहम् अनुप्रवेशमास्ते for\n  the one, गेहम् अनुप्रवेशमनुप्रवेशमास्ते for the other. The\n  vṛtti quotes a verse — सुप्सु वीप्सा, तिङ्क्षु नित्यता — and\n  cites 8.1.4, which is not codified.\n\nSETTLED — AND THE RULE IS ASKED WHY IT EXISTS AT ALL. ननु\n  चाभीक्ष्ण्ये णमुल् विहित एव, आसेवा चाभीक्ष्ण्यमेव — 3.4.22\n  gives the affix for repetition already.\n  क्त्वानिवृत्त्यर्थमिति चेत्, न, इष्टत्वात् तस्य: not to keep\n  क्त्वा out, since that IS wanted. द्वितीयोपपदार्थं तर्हि वचनम्,\n  उपपदसमासः पक्षे यथा स्यात् — it is for the second case, so that\n  the compound may optionally form. A rule whose only work is to\n  license a compound, as 3.3.116's was.",
    "3.4.57": 'SETTLED — अस्यतितृषोः क्रियान्तरे कालेषु. क्रियामन्तरयति\n  क्रियान्तरः — an act INTERRUPTING another: अद्य पाययित्वा\n  द्व्यहम् अतिक्रम्य पुनः पाययति.\n\nSETTLED — THREE CONDITIONS, THREE COUNTERS, and the last is\n  argued. कालेष्विति किम्? योजनमत्यस्य गाः पाययति — and the\n  reason: अध्वकर्मकमत्यसनं व्यवधायकम्, न कालकर्मकम्, an interval\n  of ROAD interrupts and an interval of time does not. A\n  distinction between two kinds of interval that the rule states\n  only by naming one of them.',
    "3.4.58": 'SETTLED — नाम्न्यादिशिग्रहोः: नामादेशमाचष्टे, नामग्राहमाचष्टे.\n  Two roots, one companion, and no ground given for either — one\n  of the very few rules in these four pādas the vṛtti passes\n  without comment.',
    "3.4.59": "SETTLED — अव्यये यथाभिप्रेताख्याने कृञः क्त्वाणमुलौ, and the\n  vṛtti stages it: ब्राह्मण पुत्रस्ते जातः; किं तर्हि वृषल नीचैः\n  कृत्याचक्षे? — 'a son is born to you, brahmin!' 'Why then,\n  wretch, do you tell it in a LOW voice?' उच्चैर्नाम प्रियम्\n  आख्येयम्. And the converse for bad news.\n\nSETTLED — TWO WORDS OF THE RULE, EACH SPENT ON SOMETHING OTHER\n  THAN ITS OWN AFFIX. क्त्वाग्रहणं ... समासार्थं वचनम् — क्त्वा\n  is named for the COMPOUND, since 2.2.22 needs 2.2.21's\n  condition read into it. And णमुलधिकारे पुनर्णमुल्ग्रहणं\n  तुल्यकक्षत्वज्ञापनार्थम्: णमुल् is named again, though the\n  section is about it, to show the two stand at the SAME LEVEL —\n  तेनोत्तरत्र द्वयोरप्यनुवृत्तिर्भविष्यति, so both carry down\n  together.\n  A sixth use of repeating a running word: it has widened\n  (3.2.106, 3.2.124, 3.4.1), fenced off (3.1.141, 3.2.14),\n  cancelled (3.3.44, 3.3.75), narrowed (3.3.156) — and now made\n  two things EQUAL.",
    "3.4.60": "SETTLED — तिर्यच्यपवर्गे: तिर्यक्कृत्य गतः, समाप्य गत इत्यर्थः.\n  अपवर्गः समाप्तिः. अपवर्ग इति किम्? तिर्यक् कृत्वा काष्ठं गतः.\n\nSETTLED — AND A RULE ABOUT HOW A RULE MAY NAME A WORD.\n  तिर्यचीति शब्दानुकरणम् — the rule's word is an IMITATION of\n  the word it speaks of; न च प्रकृतिवदनुकरणेन भवितव्यम्,\n  अनुक्रियमाणरूपविनाशप्रसङ्गात्: an imitation must not behave\n  like its original, or the shape being imitated would be\n  destroyed. 2.4.33 and 1.1.12 are cited, and 1.1.12 is codified.\n  A principle about the metalanguage rather than about Sanskrit.",
    "3.4.61": "SETTLED — स्वाङ्गे तस्प्रत्यये कृभ्वोः: मुखतःकृत्य गतः,\n  पृष्ठतोभूय गतः.\n\nSCAR — यथासंख्यम् IS REFUSED ON AN ACCENT THE CORPUS CANNOT\n  SHOW. यथासंख्यमत्र नेष्यते, अस्वरितत्वात् — the counting-off\n  does not apply because the rule is not marked with a svarita.\n  3.2.29 refused it on the ORDER of the rule's words and 3.3.145\n  on the same ground; this refuses it on an accent, and the\n  sūtrapāṭha on disk is unaccented. Recorded and unverifiable —\n  the boundary NORTH_STAR §7 states, met for the seventh time.\n\nSETTLED — THREE CONDITIONS, THREE COUNTERS, EACH REMOVING A\n  DIFFERENT WORD. स्वाङ्ग इति किम्? सर्वतः कृत्वा गतः.\n  तस्ग्रहणं किम्? मुखीकृत्य गतः. प्रत्ययग्रहणं किम्? मुखे\n  तस्यतीति मुखतः — where the तस् is not an AFFIX but part of a\n  root, the rule does not reach. The third of the three turns on\n  a homograph, which is a use of प्रत्ययग्रहण this project has\n  not met.",
    "3.4.62": 'SETTLED — नाधार्थप्रत्यये च्व्यर्थे. Four companions and two\n  roots, and the vṛtti writes out all twenty-four forms.\n  प्रत्ययग्रहणं किम्? हिरुक् कृत्वा, पृथक् कृत्वा.\n  च्व्यर्थ इति किम्? नाना कृत्वा काष्ठानि गतः.\n\nSETTLED — TWO HALVES OF ONE COMPOUND READ TWO DIFFERENT WAYS.\n  धार्थमर्थग्रहणम्, ना पुनरेक एव — the धा is taken BY SENSE and\n  the ना is one particular affix, 5.2.27 giving it. So a single\n  compound in the rule names a class by one half and an\n  individual by the other.',
    "3.4.63": "SETTLED — तूष्णीमि भुवः. भूग्रहणं कृञो निवृत्त्यर्थम् — भू is\n  named to STOP कृ, which had been running from 3.4.61. A root\n  named not for itself but to exclude another, which is what\n  3.2.14's धातुग्रहण did for an affix.",
    "3.4.64": "SETTLED — अन्वच्यानुलोम्ये: अन्वग्भूयास्ते.\n  आनुलोम्यमनुलोमता, अनुकूलत्वम्, परचित्तानुविधानम् — three\n  glosses in a row, each further from the word than the last, and\n  the third is not a synonym at all but a description: falling in\n  with another's mind. आनुलोम्य इति किम्? अन्वग् भूत्वा तिष्ठति.",
    "3.4.65": 'SETTLED — शकधृषज्ञाग्लाघटरभलभक्रमसहार्हास्त्यर्थेषु तुमुन्.\n  अक्रियार्थोपपदार्थोऽयमारम्भः — the rule exists for a companion\n  that is NOT an act done for the sake of another, which is what\n  3.3.10 required. A rule defined by the condition it DROPS, as\n  3.2.17 and 3.3.7 were.',
    "3.4.66": 'SETTLED — पर्याप्तिवचनेष्वलमर्थेषु. पर्याप्तिरन्यूनता.\n\nSETTLED — TWO CONDITIONS AND TWO COUNTERS THAT CROSS.\n  पर्याप्तिवचनेष्विति किम्? अलं कृत्वा — a word of that family but\n  not in the sense of sufficiency. अलमर्थेष्विति किम्?\n  पर्याप्तं भुङ्क्ते — sufficiency, but not a word of the family.\n  Each counter-example fails the condition the other satisfies,\n  which is the neatest demonstration in these four pādas that two\n  conditions are independent.\n\nSETTLED — पूर्वसूत्रे शकिग्रहणमनलमर्थम्, शक्यमेवं कर्तुमिति: the\n  rule before names शक् for a sense OUTSIDE this one, so the two\n  divide that root between them.',
    "3.4.67": 'SETTLED — कर्तरि कृत्, AND THE QUESTION CHANGES. Every rule of\n  3.2, 3.3 and this pāda so far has answered WHICH AFFIX COMES.\n  From here the rules say what an affix, once it has come, STANDS\n  FOR.\n\nSETTLED — कृदुत्पत्तिवाक्यानामयं शेषः: the heading is the\n  REMAINDER of every rule that gives a कृत् affix.\n\nSETTLED — AND IT ATTACHES ONLY WHERE THERE IS A GAP. तत्र\n  येष्वर्थादेशो नास्ति तत्रेदमुपतिष्ठते, अर्थाकाङ्क्षत्वात् — it\n  stands where the rule giving the affix stated NO sense, because\n  only there is a sense still wanted; न ख्युन्नादिवाक्येषु,\n  साक्षादर्थनिर्देशे सति तेषां निराकाङ्क्षत्वात्.\n  A heading that FILLS GAPS rather than covering ground. 3.2.84,\n  3.3.18 and 3.3.19 all reached every rule under them; this one\n  reaches only the rules that left room for it, and the\n  codification therefore takes whether a sense was stated as an\n  input.',
    "3.4.68": 'SETTLED — भव्यगेयप्रवचनीयोपस्थानीयजन्याप्लाव्यापात्या वा, seven\n  words allowed to denote the DOER where 3.4.70 would have held\n  them to the act and the object: तयोरेव कृत्यक्तखलर्थाः इति\n  भावकर्मणोः प्राप्तयोः कर्ता च वाच्यः पक्ष उच्यते.\n  The वा keeps both readings: गेयो माणवकः साम्नाम् and गेयानि\n  माणवकेन सामानि alike — one word read two ways, and the rule\n  licenses the reading that would otherwise be shut out.',
    "3.4.69": 'SETTLED — लः कर्मणि च भावे चाकर्मकेभ्यः, AND THE SECOND OF THE\n  THREE लकार DEBTS IS PAID. NORTH_STAR has carried it since\n  3.2.110: that table names its endings as bare strings and\n  nothing could ask what one of them IS. This says what they\n  DENOTE.\n\nSETTLED — गम्यते ग्रामो देवदत्तेन for the object, गच्छति ग्रामं\n  देवदत्तः for the doer by the first च; and after an intransitive\n  root, आस्यते देवदत्तेन for the act, आस्ते देवदत्तः for the doer\n  by the second. सकर्मकेभ्यो भावे न भवन्ति — so transitivity\n  PARTITIONS what the ending can stand for, and the codification\n  splits the rule into two rows rather than listing three senses.\n\nSETTLED — AND ONE RULE ANSWERS FOR ALL TEN ENDINGS. ल\n  इत्युत्सृष्टानुबन्धं सामान्यं गृह्यते, प्रथमाबहुवचनान्तं चैतत्\n  — the ल is taken WITHOUT its markers and as a PLURAL, so the\n  rule speaks of every लकार at once and of no one of them. That\n  is why लट्, लङ्, लिट्, लुङ् and the rest need no separate\n  statement.\n\nDEBT — 3.4.77 remains, and with it what a लकार BECOMES.',
    "3.4.70": "SETTLED — तयोरेव कृत्यक्तखलर्थाः: कर्तव्यः कटो भवता for the\n  object, आसितव्यं भवता for the act; and so for क्त and for the\n  खल्-sense affixes.\n\nSETTLED — एवकारः कर्तुरपकर्षणार्थः: the एव is there to PULL THE\n  DOER AWAY, which 3.4.67's heading would otherwise have\n  supplied. A word spent to undo a heading for one class of\n  affixes — and 3.4.68 then lets seven particular words back in.\n  Three rules in a row adjusting one another.\n\nSETTLED — भावे चाकर्मकेभ्य इत्यनुवृत्तेः सकर्मकेभ्यो भावे न\n  भवन्ति: 3.4.69's restriction carries down.",
    "3.4.71": 'SETTLED — आदिकर्मणि क्तः कर्तरि च: प्रकृतः कटं देवदत्तः, he has\n  BEGUN the mat; and चकाराद् यथाप्राप्तं भावकर्मणोः, so प्रकृतः\n  कटो देवदत्तेन and प्रकृतं देवदत्तेन stand too.\n\nSETTLED — आदिभूतः क्रियाक्षण आदिकर्म, तस्मिन्नादिकर्मणि\n  भूतत्वेन विवक्षिते: the FIRST MOMENT of the act, and the\n  beginning is SPOKEN OF AS PAST, which is what lets a past affix\n  denote it. A rule turning on how a moment is meant rather than\n  on when it was — विवक्षा again, which NORTH_STAR §7 records as\n  an input and not something a form can settle.',
    "3.4.72": 'SETTLED — गत्यर्थाकर्मकश्लिषशीङ्स्थासवसजनरुहजीर्यतिभ्यश्च: गतो\n  देवदत्तो ग्रामम् for the doer, and by the च गतो देवदत्तेन ग्रामः\n  and गतं देवदत्तेन. All three given for each of the eight named\n  roots.\n\nSETTLED — AND THE LIST IS JUSTIFIED BY WHAT ITS MEMBERS BECOME.\n  श्लिषादयः सोपसर्गाः सकर्मका भवन्ति, तदर्थमेषामुपादानम् — those\n  eight take an object ONLY with a preverb, and that is why they\n  are named: without one they would already be reached by\n  अकर्मक. A list whose members are there for what they turn into.',
    "3.4.73": 'SETTLED — दाशगोघ्नौ संप्रदाने, two निपातन. दाशृ दाने, ततः\n  पचाद्यच्; स कृत्संज्ञकत्वात् कर्तरि प्राप्तः, संप्रदाने\n  निपात्यते — 3.4.67 would have made the word denote the DOER,\n  and the fixing puts it in the case of the recipient instead.\n\nSETTLED — AND THE FIXING ITSELF NARROWS WHO IS MEANT.\n  निपातनसामर्थ्यादेव गोघ्न ऋत्विगादिरुच्यते, न तु चण्डालादिः: on\n  the strength of the fixing ALONE the word means a priest and\n  not an outcaste. And असत्यपि च गोहनने तस्य योग्यतया गोघ्न\n  इत्यभिधीयते — it is used even where no cow is killed, on the\n  strength of his deserving one. A word whose sense has outrun\n  its parts, and the commentary says so rather than deriving it.',
    "3.4.74": "SETTLED — भीमादयोऽपादाने, fourteen words fixed.\n  उणादिप्रत्ययान्ता एते, and the vṛtti CITES THE उणादिपाठ BY\n  NUMBER: श्याधूसूभ्यो मक् (प०उ० १.१४५), भियः षुग् वा (प०उ०\n  १.१४८). That text is on disk and 3.3.1 reads it, so the\n  citation is checkable — which is exactly what holding a locator\n  instead of restating an affix was for.\n\nSETTLED — AND IT IS WRITTEN TO SURVIVE A RULE NOT YET GIVEN.\n  ताभ्यामन्यत्रोणादयः इति पर्युदासे प्राप्ते निपातनमारभ्यते:\n  3.4.75 will EXCLUDE this very case, so these are fixed before\n  the exclusion is stated. 3.3.119 was an exception stated two\n  sūtras before the rule it excepted; this is the same shape at\n  one sūtra's distance.",
    "3.4.75": "SETTLED — ताभ्यामन्यत्रोणादयः: the उणादि words denote a kāraka\n  OTHER than those two — कृषितोऽसौ कृषिः, तनित इति तन्तुः,\n  वृत्तमिति वर्त्म, चरितं चर्म.\n  कृत्त्वात् कर्तर्येव प्राप्ताः कर्मादिषु कथ्यन्ते — 3.4.67 would\n  have given them the doer, and this puts them in the object and\n  the rest.\n\nSETTLED — AND ONE WORD IS THERE TO REACH THE FARTHER OF TWO.\n  ताभ्यामिति संप्रदानप्रत्यवमर्शार्थम्, अन्यथा ह्यपादानमेव\n  पर्युदस्येत, अनन्तरत्वात् — without it only the NEARER of the\n  two would be excluded, being adjacent. A word spent on which of\n  two neighbours a reference reaches, as 3.4.32's अस्य was.\n\nSETTLED — वर्त्म and चर्म are 3.3.2's own examples, and this rule\n  says what they DENOTE where that one said they may be seen in\n  the past. The two halves of one question, a pāda and a half\n  apart, and both codified.",
    "3.4.76": "SETTLED — ध्रौव्यगतिप्रत्यवसानार्थेभ्यश्च: आसितो देवदत्तः, आसितं\n  तेन, इदमेषामासितम् — the last being the LOCUS, the place they\n  sat. चकाराद् यथाप्राप्तं च.\n\nSETTLED — AND THE THREE ROOT-SENSES REACH DIFFERENT SETS.\n  ध्रौव्यार्थेभ्यः कर्तृभावाधिकरणेषु, गत्यर्थेभ्यः\n  कर्तृकर्मभावाधिकरणेषु, प्रत्यवसानार्थेभ्यः कर्मभावाधिकरणेषु —\n  three, four and three respectively, and the rule states none of\n  it. Recorded rather than codified as three rows, since what the\n  rule gives is one list and the division is the vṛtti's reading.\n\nSCOPE — कथं भुक्ता ब्राह्मणाः, पीता गाव इति? अकारो मत्वर्थीयः,\n  भुक्तमेषामस्ति — the brahmins who HAVE eaten, the ending read\n  as a possessive and not as this affix at all. A form saved by\n  parsing it as something else, which 3.2.53 and 3.3.24 did too.",
    "3.4.77": "SETTLED — लस्य, AND THE LAST OF THE THREE लकार DEBTS IS PAID.\n  NORTH_STAR has carried them since 3.2.110: that table names its\n  endings as bare strings, and nothing could ask what one of them\n  IS. 3.4.6 gave the Vedic set, 3.4.69 said what one DENOTES, and\n  this ENUMERATES them and says what the name covers.\n\nSETTLED — दश लकारा अनुबन्धविशिष्टा विहिता अर्थविशेषे कालविशेषे\n  च, तेषां विशेषकराननुबन्धानुत्सृज्य यत् सामान्यं तद् गृह्यते:\n  ten were given, each marked and each for a particular sense or\n  time, and the heading takes the COMMON element with the marks\n  let go. षट् टितः, चत्वारो ङितः, and\n  अक्षरसमाम्नायवदानुपूर्व्या कथ्यन्ते — ordered as the alphabet\n  is: लट्, लिट्, लुट्, लृट्, लेट्, लोट्, लङ्, लिङ्, लुङ्, लृङ्.\n\nSETTLED — AND EVERY ENDING THIS PROJECT HAS GIVEN IS ONE OF THE\n  TEN. The लकार table spans 3.2.110 to 3.4.8 and names seven of\n  them; a test now checks the set it gives against the set this\n  rule enumerates. That check was impossible until now, and it is\n  the first time two and a half pādas of work could be validated\n  against a single later rule.\n\nSETTLED — अकार उच्चारणार्थः, the अ only to make the rule sayable:\n  the third letter met with that job, after 3.3.57's द and\n  3.4.12's ल.\n  And the heading is kept off ordinary words by what runs into\n  it: अथ लकारमात्रस्य ग्रहणं कस्माद् न भवति — लुनाति चूडाल इति?\n  धात्वधिकारोऽनुवर्तते, कर्त्रादयश्च विशेषकाः.",
    "3.4.78": 'SETTLED — तिप्तस्झिसिप्थस्थमिब्वस्मस्तातांझथासाथांध्वमिड्वहिमहिङ्,\n  eighteen substitutes: three persons by three numbers in each of\n  two voices. पचति, पचतः, पचन्ति; पचसे, पचेथे, पचध्वे; एवम्\n  अन्येष्वपि लकारेषूदाहार्यम्.\n\nSETTLED — THREE MARKS, NONE OF THEM MAKING AN ENDING.\n  तिप्सिप्मिपां पकारः स्वरार्थः — the प for the accent.\n  इटष्टकार इटोऽत् इति विशेषणार्थः, तिबादिभिरादेशैस्तुल्यत्वाद् न\n  देशविध्यर्थः — the ट so 3.4.106 can pick that one out, and\n  EXPRESSLY NOT to say where it goes, which the commentary has to\n  rule out because the mark would ordinarily mean that.\n  महिङो ङकारस्तिङ् इति प्रत्याहारग्रहणार्थः — the ङ on the LAST\n  of the eighteen so that तिङ् may be formed as a pratyāhāra.\n\nSETTLED — AND THAT LAST LETTER IS WHAT 3.4.113 STANDS ON. That\n  rule confers the name सार्वधातुक on तिङः शितश्च, and the name\n  of the whole set is made by the final letter of its final\n  member. 3.4.113 was codified long before the reading reached\n  this pāda, because 7.3.84 could not strengthen without it — so\n  a rule written early rests on a letter only now read.',
}

_SAMBANDHA = ("3.4.1",)
_ANUPRAYOGA = ("3.4.4", "3.4.5", "3.4.46")
_TUMARTHA = ("3.4.9", "3.4.12", "3.4.13", "3.4.14", "3.4.16",
             "3.4.17")
_FIXED = ("3.4.10", "3.4.11", "3.4.15")

#: 3.4.18 to 3.4.24 — क्त्वा and णमुल्, the affixes of the prior
#: act. A run of its own, held together by 3.4.21's two
#: conditions.
_KTVA = tuple("3.4.%d" % _n for _n in range(18, 65)
              if "3.4.%d" % _n not in _ANUPRAYOGA)

#: 3.4.65 and 3.4.66 give तुमुन् on companions that are not
#: acts, so they answer from the same place 3.3's तुमुन् rules
#: do.
_VIDHI = ("3.4.65", "3.4.66")

_VIDHI_LINE = (
    'vidhi_affix(sense=..., beside=..., wants=...) -> which कृत् affix '
    'comes in a sense of enjoining, deserving, ability or sufficiency.'
)

#: 3.4.67 and 3.4.69 to 3.4.71 answer a question no rule before
#: them asked: not WHICH affix comes but what the affix, once it
#: has come, STANDS FOR. 3.4.69 is where a लकार finally gets a
#: meaning, which the table of 3.2.110 could never ask for.
_DENOTES = ("3.4.67", "3.4.69", "3.4.70", "3.4.71",
            "3.4.72", "3.4.75", "3.4.76")
_DENOTED_FIXED = ("3.4.68", "3.4.73", "3.4.74")

#: 3.4.77 and 3.4.78 are what the लकार table has been missing
#: since 3.2.110: the enumeration of the ten, and the eighteen
#: that stand in their place. They answer from `lakara`, the
#: module that could not ask.
_LAKARA_ITSELF = ("3.4.77",)
_LAKARA_TIN = ("3.4.78",)

_LAKARA_ITSELF_LINE = (
    'lakara_heading(name=...) -> the ten लकाराः, which are टित् and '
    'which ङित्, and what the heading covers.'
)

_LAKARA_TIN_LINE = (
    'lakara_substitutes(lakara=...) -> the eighteen endings that stand '
    'in place of a लकार, and what each of their three marks is for.'
)

_UNADI_LINE = (
    'unadi(word, past=..., samjna=...) -> whether an उणादि word stands, '
    'and which sūtra of the उणादिपाठ the Kāśikā cites for it.'
)

_DENOTES_LINE = (
    'denotes(affix, akarmaka=..., adikarman=..., sense_stated=...) -> '
    'what the affix stands for — the doer, the thing done, or the act.'
)

_DENOTED_FIXED_LINE = (
    'nipatana(word) -> a word fixed as able to denote the doer where '
    'the rules would have held it to the act and the object.'
)

_KTVA_LINE = (
    'ktva_namul(beside=..., root=..., samana_kartrka=..., purvakala=..., '
    'abhiksnya=..., paravara=..., vyatihara=..., anakanksa=..., wants=...) '
    '-> which affix of the prior act comes, and by which rule.'
)

_DISPATCH = (
    (_SAMBANDHA, dhatu_sambandha, _SAMBANDHA_LINE),
    (_ANUPRAYOGA, anuprayoga, _ANUPRAYOGA_LINE),
    (_TUMARTHA, tumartha_affix, _TUMARTHA_LINE),
    (_FIXED, nipatana, _FIXED_LINE),
    (_KTVA, ktva_namul, _KTVA_LINE),
    (_VIDHI, vidhi_affix, _VIDHI_LINE),
    (_DENOTED_FIXED, denoted_nipatana, _DENOTED_FIXED_LINE),
    (_DENOTES, denotes, _DENOTES_LINE),
    (_LAKARA_ITSELF, lakara_heading, _LAKARA_ITSELF_LINE),
    (_LAKARA_TIN, lakara_substitutes, _LAKARA_TIN_LINE),
)

#: 3.4.7's condition is the one 3.3.139 introduced and 3.3.156 supplies;
#: 3.4.11's second word rests on the substitution 2.4.54 makes; 3.4.2
#: contrasts itself with 3.1.22's यङ्. All three are citations of a
#: settled fact and not calls, so they stay in the notes and are not
#: declared — the reuse guard is right to want a call first.
_REUSES = {}

for _sutra, _notes in _RULES.items():
    _apply, _line = lakara_for, _LAKARA_LINE
    for _which, _fn, _describes in _DISPATCH:
        if _sutra in _which:
            _apply, _line = _fn, _describes
            break
    register(
        _sutra,
        apply=_apply,
        codification=_line,
        notes=_notes,
        reuses=_REUSES.get(_sutra, ()),
    )


_RULES_TIN = {
    '3.4.80': (
        'SETTLED — थासः से. टित इत्येव: the rule names no लकार and\n'
        "  takes six of the ten from 3.4.79's word. पचसे, पेचिषे,\n"
        '  पक्तासे, पक्ष्यसे — one substitution shown in four tenses,\n'
        '  which is the vṛtti demonstrating what a class-word reaches\n'
        '  rather than listing it.\n'
        '\n'
        'NOTE — the divergence here is real and shallow. GRETIL reads\n'
        '  थासः से and Vidyut थासस्से, the same words with the sandhi\n'
        '  written out. The collation calls it divergent because the\n'
        '  classifier compares word-forms; nothing turns on it.'
    ),
    '3.4.81': (
        'SETTLED — लिटस्तझयोरेशिरेच्, यथासंख्यम् by 1.3.10: त takes एश्\n'
        '  and झ takes इरेच्. पेचे, पेचाते, पेचिरे; लेभे, लेभाते,\n'
        '  लेभिरे.\n'
        '\n'
        'SETTLED — two marks in one rule, doing two different jobs.\n'
        '  शकारः सर्वादेशार्थः — the श् so that 1.1.55 अनेकाल्शित्\n'
        '  सर्वस्य makes the substitute replace the WHOLE ending and not\n'
        '  merely its last sound. चकारः स्वरार्थः — the च् for the\n'
        '  accent. Neither letter is ever heard, and each is there for a\n'
        '  different rule to find.'
    ),
    '3.4.82': (
        'SETTLED — परस्मैपदानां णलतुसुस्थलथुसणल्वमाः: the nine active\n'
        '  endings of 3.4.78 give way to nine others in the perfect.\n'
        '  पपाच, पेचतुः, पेचुः; पेचिथ, पेचथुः, पेच; पपाच, पेचिव,\n'
        '  पेचिम.\n'
        '\n'
        'SETTLED — one of the nine is given twice. णल् stands at the\n'
        '  third singular and again at the first, so पपाच is both *he\n'
        '  cooked* and *I cooked*: nine members, eight shapes. The rule\n'
        '  does not remark on it; the paradigm simply has a hole where a\n'
        '  distinction would be.\n'
        '\n'
        'SETTLED — लकारः स्वरार्थः, णकारो वृद्ध्यर्थः. The ण् is what\n'
        '  makes 7.2.115 अचो ञ्णिति apply, so पच् becomes पाच् because\n'
        '  of a letter that is never spoken.\n'
        '\n'
        "NOTE — the nine are read off 3.4.78's own list rather than\n"
        '  retyped, so the count is taken from the enumeration. GRETIL\n'
        '  writes प्रस्मैपदानाम् for परस्मैपदानाम्, a plain slip; Vidyut\n'
        '  has it right.'
    ),
    '3.4.83': (
        'SETTLED — विदो लटो वा. After विद ज्ञाने the PRESENT endings may\n'
        "  wear the perfect's shapes: वेद, विदतुः, विदुः, and equally\n"
        '  वेत्ति, वित्तः, विदन्ति. A present sense in a perfect form,\n'
        '  and both stand.\n'
        '\n'
        "SETTLED — and this rule's वा outlives it by sixteen sūtras. The\n"
        '  vṛtti carries it to 3.4.85, 3.4.86, 3.4.97 and 3.4.98, each\n'
        '  time reading it as व्यवस्थितविभाषा — an option DISTRIBUTED\n'
        '  over cases rather than free within any one. 3.4.99 then\n'
        '  spends the word नित्यम् for no other purpose than to stop it.\n'
        '  An option carried by inference has to be cancelled expressly,\n'
        '  because nothing else would show where it ended.'
    ),
    '3.4.84': (
        'SETTLED — ब्रुवः पञ्चानामादित आहो ब्रुवः. After ब्रू the FIRST\n'
        '  FIVE of the nine take the perfect endings, and तत्सन्नियोगेन\n'
        '  the root becomes आह् in the same act: आह, आहतुः, आहुः, आत्थ,\n'
        '  आहथुः. Not ब्रवीति, ब्रूतः, ब्रुवन्ति.\n'
        '\n'
        'SETTLED — the count breaks the paradigm in the middle.\n'
        '  पञ्चानामिति किम्? ब्रूथ — the sixth is outside the five and\n'
        '  keeps its own shape, so a speaker says आत्थ and ब्रूथ in one\n'
        '  breath. आदित इति किम्? परेषां मा भूत्.\n'
        '\n'
        'SETTLED — the root is named twice in a rule of four words.\n'
        '  ब्रुव इति पुनर्वचनं स्थान्यर्थम्, परस्मैपदानामेव हि स्यात्:\n'
        '  the first ब्रुवः marks the domain, the second is what आह्\n'
        '  REPLACES. Without the repetition the substitution would land\n'
        '  on परस्मैपदानाम्, the nearest genitive to hand — the same\n'
        "  hazard 1.1.49's षष्ठी स्थानेयोगा exists to manage."
    ),
    '3.4.85': (
        'SETTLED — लोटो लङ्वत्, अतिदेशोयम्. One word borrows a whole\n'
        "  rule-set: तामादयस्सलोपश्च, 3.4.101's four substitutes and\n"
        "  3.4.99's elision reach the imperative because it is made to\n"
        '  count as an imperfect. पचताम्, पचतम्, पचत, पचाव, पचाम.\n'
        '\n'
        'SETTLED — and what does NOT carry is the interesting part.\n'
        '  अडाटौ कस्माद् न भवतः, तथा झेर्जुसादेशः? The augment and\n'
        "  Śākaṭāyana's जुस् stay behind, or यान्तु and वान्तु would\n"
        "  come out *अयुः-shaped. The answer given is that 3.4.83's option\n"
        '  is still running: विदो लटो वा इत्यतो वाग्रहणमनुवर्तते, सा च\n'
        '  व्यवस्थितविभाषा भविष्यति — an अतिदेश bounded by an option\n'
        '  borrowed from two sūtras back.\n'
        '\n'
        'SETTLED — 3.4.111 fences the same boundary from the other end,\n'
        '  twenty-six sūtras on, and by a different argument: it says\n'
        '  लङ् expressly so that only a लङ् GIVEN as one is meant, लङ्वद्\n'
        '  भावेन यस्तस्य मा भूत्. One fact held down twice, by two\n'
        '  kinds of reasoning, and neither citing the other.'
    ),
    '3.4.86': (
        'SETTLED — एरुः. The इ of a लोट् ending becomes उ: पचतु,\n'
        '  पचन्तु — which is the whole audible difference between *he\n'
        '  cooks* and *let him cook*.\n'
        '\n'
        'SETTLED — a vārttika asks for two exceptions and gets two\n'
        '  answers. हिन्योरुत्वप्रतिषेधो वक्तव्यः (म०भा० ३.४.८६ वा० १)\n'
        '  wants हि and नि kept out; न वोच्चारणसामर्थ्यात् — those two\n'
        '  were GIVEN as हि and नि by 3.4.87 and 3.4.89, and the act of\n'
        "  giving them in that shape protects them. Or else 3.4.83's वा\n"
        '  still runs. Two grounds offered for one result, and the vṛtti\n'
        '  does not choose between them.'
    ),
    '3.4.87': (
        'SETTLED — सेर्ह्यपिच्च. The लोट् सि becomes हि, and is अपित्:\n'
        '  लुनीहि, पुनीहि, राध्नुहि, तक्ष्णुहि.\n'
        '\n'
        'SETTLED — the second half is a DENIAL of something inherited.\n'
        '  स्थानिवद्भावात् पित्त्वं प्राप्तं प्रतिषिध्यते: सिप् carries\n'
        '  a प्, and 1.1.56 would hand that mark to हि along with the\n'
        '  position it takes. The rule takes it back, and the fruit is\n'
        '  लुनीहि — a पित् substitute would have been neither कित् nor\n'
        '  ङित् and the weakening would not have come. A rule half of\n'
        '  which exists to cancel a general principle.'
    ),
    '3.4.88': (
        'SETTLED — वा छन्दसि, अपित्त्वं विकल्प्यते. In the Veda the हि\n'
        '  of 3.4.87 is optionally पित् again: युयोध्यस्मज्जुहुराणमेनः\n'
        '  (ऋ० १.१८९.१), and प्रीणाहि beside प्रीणीहि (काठ०सं० ४०.१२)\n'
        '  shows both readings standing in the transmitted texts.\n'
        '\n'
        'NOTE — a rule whose entire content is to loosen the rule\n'
        '  immediately before it. The pāda has three of these now —\n'
        "  3.4.83's वा, this, and 3.4.96 — and each is a different\n"
        '  shape of the same move: state a thing, then say where it\n'
        '  does not hold.'
    ),
    '3.4.89': (
        'SETTLED — मेर्निः. The लोट् मि becomes नि: पचानि, पठानि.\n'
        '\n'
        'SETTLED — उत्वलोपयोरपवादः, one rule excepting two. It keeps\n'
        '  3.4.86 from giving उ and keeps the elision of इ off as well,\n'
        '  and the two it excepts are three sūtras apart in opposite\n'
        '  directions. The EXCEPTS table holds the relation, because it\n'
        '  is a relation between rules and not a property of one.'
    ),
    '3.4.90': (
        'SETTLED — आमेतः. The ए of a लोट् ending becomes आम्: पचताम्,\n'
        '  पचेताम्, पचन्ताम्.\n'
        '\n'
        "NOTE — the ए it works on is 3.4.79's. टित आत्मनेपदानां टेरे put\n"
        '  it there, so this rule operates on the output of a rule\n'
        '  eleven sūtras back that was codified long before the reading\n'
        '  reached this pāda. The order in which the project met them is\n'
        '  the reverse of the order in which they apply.'
    ),
    '3.4.91': (
        'SETTLED — सवाभ्यां वामौ, आमोऽपवादः. After a स and after a व\n'
        '  the लोट् ए becomes व and अम् respectively, यथासंख्यम्:\n'
        '  पचस्व, पचध्वम्.\n'
        '\n'
        'SETTLED — the condition is a SOUND and not a category. What\n'
        '  precedes is a स only because 3.4.80 has already turned थास्\n'
        '  into से, so this rule reaches its first case through a\n'
        '  substitution made eleven sūtras earlier. Rules of this run\n'
        "  read each other's output, which is why they have to be held\n"
        '  in one table.'
    ),
    '3.4.92': (
        'SETTLED — आडुत्तमस्य पिच्च. The first-person लोट् takes आट् in\n'
        '  front and becomes पित्: करवाणि, करवाव, करवाम; करवै,\n'
        '  करवावहै, करवामहै. The आ is what makes an imperative *let me*\n'
        '  audibly longer than the indicative beside it.'
    ),
    '3.4.93': (
        'SETTLED — एत ऐ, आमोऽपवादः. In the first person the लोट् ए\n'
        '  becomes ऐ: करवै, करवावहै, करवामहै. The second rule of three\n'
        '  sūtras to except 3.4.90.\n'
        '\n'
        'SETTLED — a form saved by WHEN an operation becomes available.\n'
        '  इह कस्माद् न भवति — पचावेदम्, यजावेदम्? बहिरङ्गलक्षणत्वाद्\n'
        '  गुणस्य: the ए there is made by a guṇa that depends on the\n'
        '  next word, so it is बहिरङ्ग and counts as not yet there for\n'
        '  this rule to work on. Not a condition the rule states — a\n'
        '  principle about ordering, doing the work of one.'
    ),
    '3.4.94': (
        'SETTLED — लेटोऽडाटौ, पर्यायेण. The Vedic subjunctive takes अट्\n'
        '  or आट् in front, by turns: जोषिषत् (ऋ० २.३५.१), तारिषत्\n'
        '  (ऋ० १.२५.१२), मन्दिषत् for the short; पताति दिद्युत्\n'
        '  (ऋ० ७.२५.१), उदधिं च्यावयाति (तै०सं० ३.५.५.२) for the long.\n'
        '\n'
        'NOTE — every example in this stretch is cited to a text on\n'
        '  disk. The लेट् has no forms outside the Veda, so the vṛtti\n'
        '  cannot make one up, and the citations are what the rule has\n'
        '  instead of a paradigm.'
    ),
    '3.4.95': (
        'SETTLED — आत ऐ. The आ of a लेट् ending becomes ऐ, and only in\n'
        '  one cell of the paradigm: प्रथमपुरुषमध्यमपुरुषात्मनेपद-\n'
        '  द्विवचनयोः, the third and second person ātmanepada DUAL.\n'
        '  मन्त्रयैते, मन्त्रयैथे, करवैते, करवैथे.\n'
        '\n'
        "SETTLED — आटः कस्माद् न भवति? विधानसामर्थ्यात्. 3.4.94's आट्\n"
        '  supplies the same आ, and if this rule worked on that one it\n'
        '  would have nothing of its own to do; the fact that it was\n'
        '  stated at all is the argument that it is not about that आ.\n'
        "  A rule's existence used as evidence for its scope."
    ),
    '3.4.96': (
        'SETTLED — वैतोऽन्यत्र. The लेट् ए optionally becomes ऐ: सप्ताहानि\n'
        '  शासै, अहमेव पशूनामीशै (काठ०सं० २५.१), मदग्रा एव वो ग्रहा\n'
        '  गृह्यान्तै and मद्देवत्यान्येव वः पात्राण्युच्यान्तै\n'
        '  (तै०सं० ६.४.७.२). And न च भवति — यत्र क्व च ते मनो दक्षं\n'
        '  दधस उत्तरम् (ऋ० ६.१६.१७) keeps its ए.\n'
        '\n'
        'SETTLED — अन्यत्र looks exactly ONE RULE BACK.\n'
        '  अन्यत्रेत्यनन्तरो विधिरपेक्ष्यते, आत ऐ इत्येतद्विषयं\n'
        "  वर्जयित्वा: 'elsewhere' is not 'anywhere else in the grammar'\n"
        "  but 'outside what the sūtra immediately before covers'.\n"
        "  अन्यत्रेति किम्? मन्त्रयैते, मन्त्रयैथे — 3.4.95's own\n"
        '  examples, which this rule would otherwise make optional and\n'
        '  so undo. A word of scope whose range is a single neighbour.'
    ),
    '3.4.97': (
        'SETTLED — इतश्च लोपः परस्मैपदेषु. The इ of a लेट् active ending\n'
        '  is dropped: जोषिषत्, तारिषत्, मन्दिषत्. And वानुवृत्तेः पक्षे\n'
        "  श्रवणमपि भवति — 3.4.83's option is still running fourteen\n"
        '  sūtras later, so the इ is also HEARD: पताति दिद्युत्, उदधिं\n'
        '  च्यावयाति.\n'
        '\n'
        'SETTLED — परस्मैपदग्रहणमिड्वहिमहिङां मा भूत्. The word\n'
        '  परस्मैपदेषु is in the rule to keep the elision off इट्, वहि\n'
        '  and महिङ्, the three ātmanepada endings that also carry an इ.\n'
        '  A condition stated to protect three items of an eighteen-item\n'
        '  list from a rule that speaks of a letter rather than of\n'
        '  endings.'
    ),
    '3.4.98': (
        'SETTLED — स उत्तमस्य. The स् of a लेट् first-person ending is\n'
        '  optionally dropped: करवाव, करवाम beside करवावः, करवामः.\n'
        '  उत्तमग्रहणं पुरुषान्तरे मा भूत्.\n'
        '\n'
        "NOTE — this is the last rule 3.4.83's वा reaches. It has been\n"
        '  carried by inference through fifteen sūtras and the very next\n'
        '  rule spends a word to end it.'
    ),
    '3.4.99': (
        'SETTLED — नित्यं ङितः. After a ङित् लकार the first-person स् is\n'
        '  ALWAYS dropped: अपचाव, अपचाम.\n'
        '\n'
        'SETTLED — नित्यग्रहणं विकल्पनिवृत्त्यर्थम्, and this is the\n'
        '  finding of the run. The word नित्यम् is in the rule for one\n'
        "  purpose only: TO KILL AN OPTION IT DOES NOT STATE. 3.4.83's वा\n"
        '  has been running by anuvṛtti since sixteen sūtras back,\n'
        '  picked up at 3.4.85, 3.4.86, 3.4.97 and 3.4.98, and one\n'
        '  syllable here stops it.\n'
        '\n'
        '  An option carried by INFERENCE has to be cancelled\n'
        '  EXPRESSLY, because nothing else would show that it had ended.\n'
        '  Anuvṛtti runs until something blocks it, so silence here would\n'
        '  have meant the option continued — the cost of a mechanism that\n'
        '  carries words forward for free is that stopping one costs a\n'
        '  word. Where 3.4.85 turned that same वा into a\n'
        '  व्यवस्थितविभाषा, this refuses even that.'
    ),
    '3.4.100': (
        'SETTLED — इतश्च. After a ङित् लकार the इ goes too, always:\n'
        '  अपचत्, अपाक्षीत्. This is what makes an imperfect audibly one\n'
        '  — अपचत् against पचति is the augment at one end and this\n'
        '  elision at the other.\n'
        '\n'
        'SETTLED — परस्मैपदेष्वित्येव, carried from 3.4.97: अपचावहि,\n'
        '  अपचामहि keep their इ. The same word doing the same protective\n'
        '  work three sūtras on, and for the same three endings.'
    ),
    '3.4.101': (
        'SETTLED — तस्थस्थमिपां तांतंतामः, यथासंख्यम्. Four of the\n'
        '  eighteen give way to four others after a ङित् लकार:\n'
        '  अपचताम्, अपचतम्, अपचत, अपचम्; अपाक्ताम्, अपाक्तम्, अपाक्त,\n'
        '  अपाक्षम्.\n'
        '\n'
        'NOTE — the four are the two duals, the second plural and the\n'
        '  first singular: not a natural class in the paradigm. The rule\n'
        '  makes no attempt to call them one. It lists them, and lists\n'
        '  what they become.'
    ),
    '3.4.102': (
        'SETTLED — लिङः सीयुट्. Every लिङ् ending takes सीयुट् in front:\n'
        '  पचेत, पचेयाताम्, पचेरन्; पक्षीष्ट, पक्षीयास्ताम्, पक्षीरन्.\n'
        '\n'
        'SETTLED — टकारो देशविध्यर्थः, उकार उच्चारणार्थः. The ट् so that\n'
        '  1.1.46 आद्यन्तौ टकितौ puts the augment at the FRONT, the उ\n'
        '  only to make it sayable. Two letters of a four-letter augment\n'
        '  doing no work in the word.'
    ),
    '3.4.103': (
        'SETTLED — यासुट् परस्मैपदेषूदात्तो ङिच्च, सीयुटोऽपवादः. In the\n'
        '  active a लिङ् takes यासुट् instead: कुर्यात्, कुर्याताम्,\n'
        '  कुर्युः. The accent is stated because आगमानुदात्तत्वे\n'
        '  प्राप्ते — an augment would otherwise be unaccented.\n'
        '\n'
        'SETTLED — the ङित् is said REDUNDANTLY, and the redundancy is\n'
        '  the information. स्थानिवद्भावादेव लिङादेशस्य ङित्त्वे सिद्धे\n'
        '  यासुटो ङिद्वचनं ज्ञापनार्थम्: the substitute is already ङित्\n'
        "  by standing in a ङित् लकार's place, so saying it again here\n"
        '  must be teaching something else — लकाराश्रयङित्त्वमादेशानां न\n'
        '  भवति, a substitute does NOT inherit ङित्त्व from the लकार it\n'
        '  replaces. The fruit is अचिनवम्, अकरवम्, which keep a guṇa\n'
        '  that inherited ङित्त्व would have forbidden. A rule that says\n'
        '  too much, and what it teaches is read off the excess.\n'
        '\n'
        'SETTLED — and the mark lands on the ENDING, not the augment:\n'
        '  ङित्त्वं तु लिङ एव विधीयते, तत्र तत्कार्याणां संभवाद्\n'
        '  नागमस्य. Only there is there anything for it to do. 3.4.104\n'
        '  makes the same move for the same augment one sūtra later.'
    ),
    '3.4.104': (
        'SETTLED — किदाशिषि. Where the लिङ् is a benediction, यासुट् is\n'
        '  कित् instead of ङित्: उच्यात्, उच्यास्ताम्, उच्यासुः;\n'
        '  जागर्यात्, जागर्यास्ताम्, जागर्यासुः. आशिषीति किम्? वच्यात्,\n'
        '  जागृयात् — the same roots without the blessing.\n'
        '\n'
        'SETTLED — the two marks mostly agree, and the rule exists for\n'
        '  the narrow place where they do not.\n'
        '  गुणवृद्धिप्रतिषेधस्तुल्यः — both forbid strengthening — and\n'
        '  संप्रसारणं जागर्तेर्गुणे च विशेषः is the whole difference:\n'
        '  vowel-replacement for वच्, and a guṇa for जागृ. Which is why\n'
        '  वच् gives उच्यात् here and वच्यात् elsewhere.\n'
        '\n'
        'SETTLED — प्रत्ययस्यैवेदं कित्त्वम्, नागमस्य, प्रयोजनाभावात्.\n'
        '  The same reasoning as 3.4.103 and stated as briefly: a mark is\n'
        '  put where it can act.'
    ),
    '3.4.105': (
        'SETTLED — झस्य रन्, झोऽन्तापवादः. The लिङ् झ becomes रन्:\n'
        '  पचेरन्, यजेरन्, कृषीरन्. 7.1.3 would have made it अन्त, and\n'
        '  this reaches it first.'
    ),
    '3.4.106': (
        'SETTLED — इटोऽत्. The लिङ् इट् becomes अत्: पचेय, यजेय, कृषीय,\n'
        '  हृषीय.\n'
        '\n'
        'SETTLED — two small questions, both about what a letter IS.\n'
        '  तकारस्येत्संज्ञाप्रतिषेधः प्राप्नोति — 1.3.4 न विभक्तौ\n'
        '  तुस्माः would deny the त् its it-hood, so is it part of the\n'
        '  substitute? नैवायमादेशावयवस्तकारः, मुखसुखार्थ उच्चार्यते: it\n'
        '  is neither an इत् nor a member, spoken only to make अत्\n'
        '  pronounceable, so the question does not arise.\n'
        '\n'
        'SETTLED — and WHICH इट्? आगमस्येटो ग्रहणं न भवति,\n'
        '  अर्थवद्ग्रहणे नानर्थकस्य (परि० १४): the ENDING इट् of 3.4.78\n'
        '  and not the augment of the same name, because a term names\n'
        '  what has meaning. Two things wearing one name, told apart by\n'
        '  a paribhāṣā — the same hazard that keeps splitting field\n'
        '  names in this codebase, met in the grammar itself.'
    ),
    '3.4.107': (
        'SETTLED — सुट् तिथोः. The त and थ of a लिङ् take सुट्:\n'
        '  कृषीष्ट, कृषीयास्ताम्; कृषीष्ठाः, कृषीयास्थाम्. तकार इकार\n'
        '  उच्चारणार्थः.\n'
        '\n'
        'SETTLED — and it does not collide with 3.4.102, for a reason\n'
        '  worth keeping. तकारथकारावागमिनौ, लिङ् तद्विशेषणम्; सीयुटस्तु\n'
        '  लिङेवागमी — the two augments attach to DIFFERENT THINGS. सुट्\n'
        '  attaches to the ending, with लिङ् only qualifying it; सीयुट्\n'
        '  attaches to the लिङ् itself. तेन भिन्नविषयत्वात् सुटा बाधनं\n'
        '  न भवति: two rules that look as though they compete for one\n'
        '  word are not competing at all, because their grounds differ.\n'
        '  That distinction is what the `kind` field on these rows\n'
        '  records, and it is the reason an आगम and an आदेश are not\n'
        '  ranked against each other.'
    ),
    '3.4.108': (
        'SETTLED — झेर्जुस्, झोऽन्तापवादः. The लिङ् झि becomes जुस्:\n'
        '  पचेयुः, यजेयुः. The second rule three sūtras apart to except\n'
        '  the same 7.1.3, and the first of five in this pāda to give\n'
        '  जुस्.'
    ),
    '3.4.109': (
        'SETTLED — सिजभ्यस्तविदिभ्यश्च, अलिङर्थ आरम्भः — begun for what\n'
        '  is NOT a लिङ्. झि becomes जुस् after सिच्, after a\n'
        '  reduplicated stem, and after विद्: अकार्षुः, अहार्षुः;\n'
        '  अबिभयुः, अजिह्रयुः, अजागरुः; अविदुः.\n'
        '\n'
        'SETTLED — अभ्यस्तविदिग्रहणमसिजर्थम्. The second and third items\n'
        '  are named because they are the cases WITHOUT a सिच्, so the\n'
        '  list is not three parallel conditions but one condition and\n'
        '  two exemptions from it. A list whose members do not have the\n'
        "  same standing — the same shape as 3.4.72's eight roots."
    ),
    '3.4.110': (
        'SETTLED — आतः, with सिच् carried down. After a long आ: अदुः,\n'
        '  अधुः, अस्थुः. तकारो मुखसुखार्थः.\n'
        '\n'
        'SETTLED — पूर्वेणैव सिद्धे नियमार्थं वचनम्. 3.4.109 would\n'
        '  already have covered these, so the rule is stated to RESTRICT\n'
        '  and not to provide: आत एव सिज्लुगन्ताद्, नान्यस्मात्. The\n'
        '  proof is अभूवन्, where प्रत्ययलक्षणेन जुस् प्राप्तः\n'
        '  प्रतिषिध्यते. And a restriction bites only on its own kind —\n'
        '  तुल्यजातीयापेक्षत्वाद् नियमस्य — so a सिच् still audible\n'
        '  gives जुस् as before: अकार्षुः, अहार्षुः.\n'
        '\n'
        'SETTLED — कथमाभ्यामानन्तर्यम्? सिचो लुकि कृते प्रत्ययलक्षणेन\n'
        '  सिचोऽनन्तरः, श्रुत्या चाकारान्तादिति. The ending counts as\n'
        '  standing next to BOTH at once: to the सिच् by the rule that\n'
        "  keeps an elided affix's effect, and to the आ by what is\n"
        '  actually heard. Two kinds of adjacency in one word.'
    ),
    '3.4.111': (
        'SETTLED — लङः शाकटायनस्यैव. After a long आ the imperfect झि\n'
        '  becomes जुस् in the view of the आचार्य Śākaṭāyana: अयुः,\n'
        '  अवुः. अन्येषां मते — अयान्, अवान्.\n'
        '\n'
        'SETTLED — a NAMED INDIVIDUAL, where 3.4.18 and 3.4.19 named\n'
        '  schools. प्राचाम् and उदीचाम् were the grammarians of east and\n'
        '  north; this is one man, cited by name, and carried into\n'
        '  3.4.112. Three attributions in one pāda, and this is the only\n'
        '  one to a person.\n'
        '\n'
        'SETTLED — लङ् is said though ङितः is already running. ननु ङित\n'
        '  इत्यनुवर्तते, अत्र लङेवाकारान्तादनन्तरो ङित् संभवति नान्यः —\n'
        '  no other ङित् can stand there — तत्किं लङ्ग्रहणेन, then what\n'
        '  is the naming of लङ् for? एवं तर्हि\n'
        '  लङेव यो लङ् विहितस्तस्य यथा स्यात्, लङ्वद्भावेन यस्तस्य मा\n'
        '  भूत्: so that only a लङ् GIVEN as one is meant, and not a\n'
        '  लोट् behaving as one by 3.4.85. यान्तु, वान्तु — and by the\n'
        '  same argument 3.4.109 does not reach a लोट् either: बिभ्यतु,\n'
        '  जाग्रतु, विदन्तु. A word spent to say how far an अतिदेश\n'
        '  carries.\n'
        '\n'
        'SETTLED — एवकार उत्तरार्थः, and it is collected four sūtras\n'
        '  later. The एव in शाकटायनस्यैव does nothing here; 3.4.115 and\n'
        '  3.4.116 use it to make a name REPLACE another instead of\n'
        '  joining it — समावेशश्चैवकारानुवृत्तेर्न भवति. A syllable\n'
        '  placed in one rule for another rule to spend.'
    ),
    '3.4.112': (
        'SETTLED — द्विषश्च. And after द्विष्, on the same authority:\n'
        '  अद्विषुः. अन्येषां मते — अद्विषन्.\n'
        '\n'
        'NOTE — the named teacher carries into a second rule, which is\n'
        '  how a citation becomes a section. 3.4.18 and 3.4.19 did the\n'
        '  same for their two schools, one rule each; this is one\n'
        '  teacher over two.'
    ),
    '3.4.114': (
        'SETTLED — आर्धधातुकं शेषः. Every affix given after a root that\n'
        '  3.4.113 did not name: लविता, लवितुम्, लवितव्यम्.\n'
        '\n'
        'SETTLED — the rule is defined by SUBTRACTION, so the code\n'
        '  subtracts. शेषः is the remainder, and there is exactly one\n'
        '  thing it is the remainder of, so `ardhadhatuka` asks\n'
        '  `sarvadhatuka` and takes the name that rule did not give.\n'
        '  3.4.113 has stood alone in this project since it was codified\n'
        "  for 7.3.84's sake; its companion turns out to be defined by\n"
        '  it in one word.\n'
        '\n'
        'SETTLED — धातोरित्येव holds it to affixes given AFTER A ROOT,\n'
        '  and the vṛtti marks the edge with four forms that are not:\n'
        '  वृक्षत्वम्, वृक्षतास्ति — त्व and तल् come after a nominal;\n'
        '  लूभ्याम्, लूभिः — case-endings come after a stem, though that\n'
        '  stem is लू; and जुगुप्सते, where सन् is given to MAKE a root\n'
        '  and not after one.'
    ),
    '3.4.115': (
        'SETTLED — लिट् च, सार्वधातुकसंज्ञाया अपवादः. A perfect ending is\n'
        '  आर्धधातुक though 3.4.113 has already called it सार्वधातुक,\n'
        '  being तिङ्: पेचिथ, शेकिथ, जग्ले, मम्ले.\n'
        '\n'
        'SETTLED — and the rule needed a borrowed syllable to work at\n'
        '  all. ननु चैकसंज्ञाधिकारादन्यत्र समावेशो भवति? सत्यमेतत् —\n'
        '  outside the one-name-only heading two names normally CO-APPLY,\n'
        '  so this rule would have added आर्धधातुक without removing\n'
        '  सार्वधातुक. इह त्वेवकारोऽनुवर्तते, स नियमं करिष्यति: the एव\n'
        '  carried down from 3.4.111 makes it restrictive.\n'
        '\n'
        "  3.4.111's vṛtti had already said एवकार उत्तरार्थः — the एव is\n"
        '  there for what follows. Four sūtras later, this is what\n'
        '  follows. A word put in one rule and spent in another, and\n'
        '  both ends of the transaction stated in the commentary.'
    ),
    '3.4.116': (
        'SETTLED — लिङाशिषि, सार्वधातुकसंज्ञाया अपवादः. A benedictive is\n'
        '  आर्धधातुक: लविषीष्ट, पविषीष्ट. आशिषीति किम्? लुनीयात्,\n'
        '  पुनीयात् keep the other name.\n'
        '\n'
        'SETTLED — समावेशश्चैवकारानुवृत्तेर्न भवति, the same borrowed एव\n'
        '  doing the same work one sūtra on. 3.4.104 also singled out\n'
        '  the benedictive लिङ्, twelve sūtras back, for a different\n'
        '  purpose — the same cell of the paradigm named twice in one\n'
        '  pāda by two unrelated rules.'
    ),
    '3.4.117': (
        'SETTLED — छन्दसि उभयथा. In the Veda an affix is BOTH\n'
        '  सार्वधातुक and आर्धधातुक.\n'
        '\n'
        'SETTLED — and it does not attach to the nearest rule alone.\n'
        '  किं लिङेवानन्तरः संबध्यते? नैतदस्ति, सर्वमेव प्रकरणमपेक्ष्यैतद्\n'
        '  उच्यते — it reaches the whole section, तिङ्शिदादि. The vṛtti\n'
        '  proves it by taking one example from each rule of the run:\n'
        "  वर्धन्तु त्वा सुष्टुतयः (ऋ० ७.९९.७) takes ārdhadhātuka's\n"
        '  णिलोप where वर्धयन्तु was due; स्वस्तये नावमिवारुहेम\n'
        '  (ऋ० १०.१७८.२) keeps the sārvadhātuka, so अस् does not become\n'
        '  भू; ससवांसो विशृण्विरे (ऋ० ४.८.६) and इम इन्द्राय सुन्विरे\n'
        '  (ऋ० ७.३२.४) make a PERFECT sārvadhātuka against 3.4.115.\n'
        '\n'
        'SETTLED — and one form takes an operation from EACH name at\n'
        '  once. उप स्थेयाम शरणा बृहन्त (ऋ० ६.४७.८):\n'
        '  सार्वधातुकत्वाल् लिङः सलोपः, आर्धधातुकत्वादेत्वम् — the\n'
        '  elision because it is one, the ए because it is the other.\n'
        '  उभयथा is not a choice between two readings but both applying\n'
        '  to one word.\n'
        '\n'
        'SETTLED — and the pāda closes by saying what all of this\n'
        '  amounts to: व्यत्ययो बहुलम् इत्यस्यैवायं प्रपञ्चः, it is\n'
        '  3.1.85 spelled out. अध्याय ३ ends by pointing back at a rule\n'
        '  of its own first pāda.'
    ),
}

_TIN_ADESA = tuple(
    "3.4.%d" % n for n in list(range(80, 85)) + list(range(86, 113))
)
_ATIDESA = ("3.4.85",)
_ARDHA = ("3.4.114", "3.4.115", "3.4.116", "3.4.117")

_TIN_ADESA_LINE = (
    'tin_adesha(of, lakara=..., pada=..., person=..., root=..., '
    'after=..., chandasi=..., sense=..., wants=...) -> what stands in '
    'place of one of the eighteen endings, or what is put before it.'
)

_ATIDESA_LINE = (
    'behaves_as(lakara) -> which लकार a लकार is made to count as, and '
    'which of that one\'s operations do not carry.'
)

_ARDHA_LINE = (
    'ardhadhatuka(tin=..., sit=..., lakara=..., sense=..., '
    'chandasi=..., after_a_root=...) -> whether the affix bears the '
    'name 3.4.114 defines as the remainder of 3.4.113.'
)

#: 3.4.114 is the plainest reuse this project has had: शेषः means the
#: remainder, and there is one thing it is the remainder OF. The code
#: asks 3.4.113 and takes the name that rule did not give, which is
#: what the sūtra says in one word.
_REUSES_TIN = {
    "3.4.114": ("3.4.113",),
    "3.4.115": ("3.4.113",),
    "3.4.116": ("3.4.113",),
    "3.4.117": ("3.4.113",),
}

for _sutra, _notes in _RULES_TIN.items():
    if _sutra in _ATIDESA:
        _apply, _line = behaves_as, _ATIDESA_LINE
    elif _sutra in _ARDHA:
        _apply, _line = ardhadhatuka, _ARDHA_LINE
    else:
        _apply, _line = tin_adesha, _TIN_ADESA_LINE
    register(
        _sutra,
        apply=_apply,
        codification=_line,
        notes=_notes,
        reuses=_REUSES_TIN.get(_sutra, ()),
    )
