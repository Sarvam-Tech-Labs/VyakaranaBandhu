# -*- coding: utf-8 -*-
"""
3.2.110 to 3.2.122 — WHICH लकार comes, and in what circumstances.

Everything in 3.2 up to here has answered one question: which affix a
root takes when a word stands beside it. These thirteen answer a
different one. They do not add a कृत् affix at all; they say which
tense-ending — लुङ्, लङ्, लिट्, लृट्, लट् — is used, and the
conditions are about TIME and about the situation of speaking:

    3.2.110 लुङ्                    the past, plainly
    3.2.111 अनद्यतने लङ्            the past not of today
    3.2.112 अभिज्ञावचने लृट्         with a word of remembering
    3.2.113 न यदि                   but not with यद्
    3.2.114 विभाषा साकाङ्क्षे        optionally, where more is expected
    3.2.115 परोक्षे लिट्             beyond the speaker's sight
    3.2.116 हशश्वतोर्लङ् च           with two particles, two endings
    3.2.117 प्रश्ने चासन्नकाले        in a question about lately
    3.2.118 लट् स्मे                 with स्म
    3.2.119 अपरोक्षे च               and where it was NOT out of sight
    3.2.120 ननौ पृष्टप्रतिवचने       answering a question, with ननु
    3.2.121 नन्वोर्विभाषा            with न or नु, optionally
    3.2.122 पुरि लुङ् चास्मे          with पुरा, but not with स्म

All of them stand under 3.2.84 भूते, so all are of the past — which
is what makes 3.2.112 remarkable: it gives लृट्, the FUTURE ending,
for a past act. What is being remembered was future to the remembering.

**DEBT — the लकाराः themselves are not codified.** What a लकार IS,
and what it becomes, is settled at 3.4.69 and 3.4.77 and after, none
of which is written yet; 3.4.6 छन्दसि लुङ्लङ्लिटः is not either, and
3.2.105 already had to cite it. So these rules name their endings as
strings and nothing here can ask what an ending is. When 3.4 is
codified this module should be re-read.

**A note on the result types.** `Added` and `NotAdded` are imported
rather than redefined: they are result shapes, not rule
implementations, and a second pair would drift from the first. The
reuse walk keys callees by function object, so importing a dataclass
creates no edge and claims nothing.
"""

from dataclasses import dataclass
from typing import Dict, Tuple

from src.astadhyayi.upapada_krt import Added, NotAdded

#: 3.3.161 and 3.3.162's six senses, and 3.3.163 to 3.3.165's
#: three. Both lists live in `vidhi_krt`, where the affix rules
#: that share them are — one list, one place. Importing a tuple
#: creates no reuse edge, as importing a dataclass does not.
from src.astadhyayi.vidhi_krt import (
    PRAISADI as PRAISADI_SENSES,
    VIDHYADI as VIDHYADI_SENSES,
)

#: 3.2.112's companion, and वचनग्रहणं पर्यायार्थम् — the word वचन is
#: there so that any SYNONYM of remembering counts, not अभिज्ञा alone:
#: अभिजानासि, स्मरसि, बुध्यसे, चेतयसे.
ABHIJNA: Tuple[str, ...] = (
    "abhijānāsi", "smarasi", "budhyase", "cetayase",
)


@dataclass(frozen=True)
class Lakara:
    """One rule choosing a tense-ending, as the conditions it states."""

    sutra: str
    gives: str
    also: str = ""
    #: Which heading the rule stands under. 3.2.84 भूते runs to
    #: 3.2.122; 3.2.123 वर्तमाने opens the present and is the
    #: first rule outside it. Stated per row because the
    #: codification cannot represent a heading that runs.
    time: str = "bhūta"
    #: The word standing beside, where the rule names one.
    beside: Tuple[str, ...] = ()
    #: A companion the rule REFUSES — 3.2.122's अस्मे.
    not_beside: Tuple[str, ...] = ()
    #: अनद्यतन, not of today. None is silence, True requires it.
    anadyatana: object = None
    #: परोक्ष, beyond the speaker's sight. 3.2.119 wants it FALSE,
    #: which is why this is tri-state and not a flag.
    paroksa: object = None
    #: 3.2.117's प्रश्ने and आसन्नकाले.
    question: bool = False
    recent: bool = False
    #: 3.2.120's पृष्टप्रतिवचने — answering something asked.
    answer: bool = False
    #: 3.2.114's साकाङ्क्षे — the speaker expects more to follow.
    #: Tri-state: 3.2.114 requires it, and 3.2.113 requires its
    #: ABSENCE, since the vṛtti marks that rule's ground off as
    #: where nothing further is looked to.
    sakanksa: object = None
    #: 3.2.113 refuses with यद्; 3.2.114 allows it either way, which
    #: is what यदीति नानुवर्तते, उभयत्र विभाषेयम् settles.
    with_yad: object = None
    #: 3.2.113 is the one प्रतिषेध of the run.
    refuses: bool = False
    #: विभाषा — the rule offers rather than requires.
    optional: bool = False

    # --- the future rules, 3.3.4 to 3.3.15 ---------------------------
    #: 3.3.4 wants यावत् and पुरा as निपात and not as case-forms:
    #: निपातयोरिति किम्? यावद् दास्यति तावद् भोक्ष्यते. Tri-state,
    #: since silence about it is not a requirement that it be absent.
    nipata: object = None
    #: 3.3.6's किंवृत्ते — a form of किम् standing beside. The vṛtti
    #: settles its extent by परिसंख्यान rather than by the word:
    #: वृत्तग्रहणेन तद् विभक्त्यन्तं प्रतीयात्, डतरडतमौ च.
    kimvrtta: bool = False
    #: 3.3.6's लिप्सायाम् — the wish to obtain. लिप्सा, लब्धुमिच्छा.
    lipsa: bool = False
    #: 3.3.7's लिप्स्यमानसिद्धौ — that what is wanted will come of it.
    lipsyamana_siddhi: bool = False
    #: 3.3.8 and 3.3.9's लोडर्थलक्षणे — the act is what marks out a
    #: command or the like.
    lodartha: bool = False
    #: 3.3.9's ऊर्ध्वमौहूर्तिके — later than the present hour.
    urdhvamauhurtika: bool = False
    #: 3.3.13's च, which reaches क्रियार्थोपपद as well as शेष.
    #: Tri-state: 3.3.13 answers either way, so silence is not denial.
    kriyartha: object = None
    #: The sense in which the ending is chosen — आशंसा, गर्हा,
    #: चित्रीकरण and the rest. From 3.3.132 to the end of the pāda
    #: nearly every rule turns on one, where 3.2's turned on the
    #: situation of speaking. Any ONE of those listed satisfies it.
    sense: Tuple[str, ...] = ()
    #: 3.3.139 to 3.3.141's क्रियातिपत्ति — the act did not come
    #: off. कुतश्चिद् वैगुण्यादनभिनिर्वृत्तिः क्रियायाः.
    kriyatipatti: bool = False
    #: and their लिङ्निमित्त — that some rule would have given
    #: लिङ् here. A condition about ANOTHER RULE having applied,
    #: which nothing in either pāda had asked before.
    lin_nimitta: bool = False
    #: 3.4.6 to 3.4.8 hold in the Veda only. One-way, as छन्दसि
    #: has been throughout: a Vedic rule must not answer outside,
    #: and a rule silent about it still answers inside.
    chandasi: bool = False
    #: 3.4.2 and 3.4.3 double the verb — क्रियासमभिहारे द्वे
    #: भवतः. Which root is then said AFTER it is 3.4.4's and
    #: 3.4.5's question, answered from `dhatu_sambandha`.
    doubled: bool = False
    why: str = ""


LAKARA: Tuple[Lakara, ...] = (
    Lakara("3.2.110", "luṅ",
           why="लुङ् — भूतेऽर्थे वर्तमानाद् धातोः: अकार्षीत्, अहार्षीत्. "
               "The widest of the run, and everything after it narrows. "
               "SCOPE: वसतेर्लुङ् रात्रिशेषे जागरणसंततौ वक्तव्यः — a "
               "vārttika for वस् of a night passed awake, क्व भवान् "
               "उषितः? अहम् अत्र अवात्सम्"),
    Lakara("3.2.111", "laṅ", anadyatana=True,
           why="अनद्यतने लङ् — अकरोत्, अहरत्. And अनद्यतन is a "
               "बहुव्रीहिनिर्देश, अविद्यमानाद्यतने: 'having no today "
               "in it'. बहुव्रीहिनिर्देशः किमर्थः? अद्य ह्यो वा "
               "अभुक्ष्महि इति व्यामिश्रे मा भूत् — so that a MIXED "
               "case, 'we ate today or yesterday', is not reached. The "
               "compound's form is doing the work of an exclusion. "
               "SCOPE: परोक्षे च लोकविज्ञाते प्रयोक्तुर्दर्शनविषये लङ् "
               "— अरुणद् यवनः साकेतम्, of a famous event the speaker "
               "did not see"),
    Lakara("3.2.112", "lṛṭ", beside=ABHIJNA, anadyatana=True,
           why="अभिज्ञावचने लृट् — अभिजानासि देवदत्त कश्मीरेषु "
               "वत्स्यामः? लङोऽपवादः. AND IT GIVES THE FUTURE ENDING "
               "FOR A PAST ACT: what is remembered was future to the "
               "remembering, so the ending looks forward from inside "
               "the memory. अभिज्ञा स्मृतिः. वचनग्रहणं पर्यायार्थम् — "
               "the word वचन is there so that any synonym counts: "
               "स्मरसि, बुध्यसे, चेतयसे"),
    Lakara("3.2.113", "lṛṭ", beside=ABHIJNA, with_yad=True,
           sakanksa=False, refuses=True,
           why="न यदि — अभिजानासि देवदत्त यत् कश्मीरेष्ववसाम. "
               "पूर्वेण प्राप्तः प्रतिषिध्यते: what 3.2.112 gave is "
               "refused where यद् stands with it. The one प्रतिषेध of "
               "the run. And the vṛtti marks off its ground from the "
               "next rule's: वासमात्रं स्मर्यते, न त्वपरं किंचिल् "
               "लक्ष्यते, तेन उत्तरसूत्रस्य नायं विषयः — here only the "
               "dwelling is remembered and nothing further is looked "
               "to, so 3.2.114 does not reach it"),
    Lakara("3.2.114", "lṛṭ", beside=ABHIJNA, sakanksa=True,
           optional=True,
           why="विभाषा साकाङ्क्षे — and यदीति नानुवर्तते, उभयत्र "
               "विभाषेयम्: यद् does NOT come down, so the option holds "
               "both with it and without. अभिजानासि देवदत्त कश्मीरेषु "
               "वत्स्यामः, तत्रौदनं भोक्ष्यामहे — and with यद् too. "
               "साकाङ्क्ष is the speaker expecting more: "
               "लक्ष्यलक्षणयोः संबन्धे प्रयोक्तुर् आकाङ्क्षा भवति, "
               "वासो लक्षणम्, भोजनं तु लक्ष्यम् — the dwelling is what "
               "marks the time, the eating is what is being placed by "
               "it, and it is the second clause that makes the first "
               "expectant"),
    Lakara("3.2.115", "liṭ", anadyatana=True, paroksa=True,
           why="परोक्षे लिट् — चकार, जहार. AND THE VṚTTI RAISES A "
               "DIFFICULTY ABOUT THE WHOLE NOTION: ननु च धात्वर्थः "
               "सर्वः परोक्ष एव? — is not every verbal meaning out of "
               "sight, since one sees things and not actions? सत्यम् "
               "एतत्, अस्ति तु लोके धात्वर्थेनापि कारकेषु "
               "प्रत्यक्षाभिमानः, स यत्र नास्ति तत् परोक्षम् इत्युच्यते: "
               "true, but people do take themselves to see an act in "
               "its participants, and परोक्ष is where they do not. A "
               "grammatical term defined by what speakers believe "
               "rather than by what is so. And even of oneself: "
               "उत्तमविषयेऽपि चित्तव्याक्षेपात् परोक्षता संभवति — "
               "सुप्तोऽहं किल विललाप, 'asleep, I am told, I wailed'. "
               "SCOPE: अत्यन्तापह्नवे च लिट् — flat denial, नाहं "
               "कलिङ्गान् जगाम"),
    Lakara("3.2.116", "laṅ", also="लिट्", beside=("ha", "śaśvat"),
           anadyatana=True, paroksa=True,
           why="हशश्वतोर्लङ् च — इति ह अकरोत् and इति ह चकार, "
               "शश्वद् अकरोत् and शश्वच् चकार. चकाराल् लिट् च, so both "
               "endings stand where 3.2.115 would have given only the "
               "one"),
    Lakara("3.2.117", "laṅ", also="लिट्", question=True, recent=True,
           anadyatana=True, paroksa=True,
           why="प्रश्ने चासन्नकाले — अगच्छद् देवदत्तः? जगाम देवदत्तः? "
               "Both endings, in a QUESTION about lately. प्रश्न इति "
               "किम्? जगाम देवदत्तः — a statement, and only the one "
               "ending. आसन्नकाल इति किम्? भवन्तं पृच्छामि, जघान कंसं "
               "किल वासुदेवः? — asking about the far past, and the "
               "rule does not reach it"),
    Lakara("3.2.118", "laṭ", beside=("sma",), anadyatana=True,
           paroksa=True,
           why="लट् स्मे — नडेन स्म पुराधीयते. लिटोऽपवादः: the PRESENT "
               "ending for a past act, which स्म alone licenses"),
    Lakara("3.2.119", "laṭ", beside=("sma",), anadyatana=True,
           paroksa=False,
           why="अपरोक्षे च — एवं स्म पिता ब्रवीति, इति स्मोपाध्यायः "
               "कथयति. The same ending with the same companion where "
               "the act was NOT out of sight, which is why परोक्ष has "
               "to be tri-state: 3.2.115 requires it, this rule "
               "requires its absence, and the rest say nothing"),
    Lakara("3.2.120", "laṭ", beside=("nanu",), answer=True,
           why="ननौ पृष्टप्रतिवचने — अकार्षीः कटं देवदत्त? ननु करोमि "
               "भोः. लुङोऽपवादः. AND TWO CONDITIONS STOP RUNNING HERE: "
               "अनद्यतने परोक्षे इति निवृत्तम्, भूतसामान्ये विधिरयम् — "
               "the rule is for the past at large. The fourth "
               "अनुवृत्ति in this pāda ended by the commentary rather "
               "than by the text. पृष्टप्रतिवचन इति किम्? नन्वकार्षीन् "
               "माणवकः"),
    Lakara("3.2.121", "laṭ", beside=("na", "nu"), answer=True,
           optional=True,
           why="नन्वोर्विभाषा — अकार्षीः कटं देवदत्त? न करोमि भोः, or "
               "नाकार्षम्; अहं नु करोमि, or अहं न्वकार्षम्. The option "
               "is real, so both the present and the past ending stand"),
    Lakara("3.2.122", "luṅ", also="लट्", beside=("purā",),
           not_beside=("sma",), anadyatana=True, optional=True,
           why="पुरि लुङ् चास्मे — वसन्तीह पुरा छात्राः, अवात्सुरिह "
               "पुरा छात्राः. अस्म इति किम्? नडेन स्म पुराधीयते — with "
               "स्म it is 3.2.118's. AND THE CONDITION ARRIVES BY A "
               "FROG'S LEAP: अनद्यतनग्रहणम् इह मण्डूकप्लुत्या "
               "अनुवर्तते — अनद्यतन comes down from 3.2.111 by "
               "LEAPING OVER the rules between, which had dropped it. "
               "A running condition that skips rather than flows, and "
               "the first मण्डूकप्लुति this project has met. "
               "ताभ्यां मुक्ते पक्षे यथाविषयम् अन्येऽपि प्रत्यया "
               "भवन्ति: where neither option is taken, still other "
               "endings come — अवसन्, ऊषुः"),
    Lakara("3.2.123", "laṭ", time="vartamāna",
           why="वर्तमाने लट् — पचति, पठति. प्रारब्धोऽपरिसमाप्तश्च "
               "वर्तमानः: what is BEGUN AND NOT FINISHED — the "
               "present defined by an act's own course rather than by "
               "the moment of speaking, which is why it covers what "
               "is under way and not merely what is now. And it is "
               "where 3.2.84's भूते stops: the heading was said to "
               "run as far as this rule, and here it ends because "
               "another time is named"),
    # --- 3.3.4 to 3.3.15 — the FUTURE ---------------------------------
    # भविष्यति runs from 3.3.3 and is dropped at 3.3.16, where the
    # vṛtti says भविष्यतीति निवृत्तम् outright.
    Lakara("3.3.4", "laṭ", time="bhaviṣyat",
           beside=("yāvat", "purā"), nipata=True,
           why="यावत्पुरानिपातयोर्लट् — यावद् भुङ्क्ते, पुरा भुङ्क्ते. "
               "The PRESENT ending used of the future, on nothing but "
               "the company the verb keeps. निपातयोरिति किम्? यावद् "
               "दास्यति तावद् भोक्ष्यते, and करणभूतया पुरा व्रजिष्यति "
               "— where the same two syllables are a case-form rather "
               "than a particle the rule does not reach them. So the "
               "condition is on what PART OF SPEECH the companion is, "
               "which no rule of 3.2 had asked"),
    Lakara("3.3.5", "laṭ", time="bhaviṣyat", optional=True,
           beside=("kadā", "karhi"),
           why="विभाषा कदाकर्ह्योः — कदा भुङ्क्ते, कदा भोक्ष्यते, कदा "
               "भोक्ता: all three stand, which is what विभाषा buys. "
               "The rule before it was नित्य and this one is not, and "
               "nothing in either sūtra says why — only that one "
               "carries विभाषा and the other does not"),
    Lakara("3.3.6", "laṭ", time="bhaviṣyat", optional=True,
           kimvrtta=True, lipsa=True,
           why="किंवृत्ते लिप्सायाम् — कं भवन्तो भोजयन्ति? लिप्सा, "
               "लब्धुमिच्छा प्रार्थनाभिलाषः, the wish to obtain. "
               "लिप्सायामिति किम्? कः पाटलिपुत्रं गमिष्यति — asking "
               "who will go, wanting nothing by it, the रule does not "
               "reach. And किंवृत्त's extent is settled by "
               "परिसंख्यान and not by the word: वृत्तग्रहणेन तद् "
               "विभक्त्यन्तं प्रतीयात्, डतरडतमौ च — the case-inflected "
               "forms of किम्, and डतर and डतम besides"),
    Lakara("3.3.7", "laṭ", time="bhaviṣyat", optional=True,
           lipsyamana_siddhi=True,
           why="लिप्स्यमानसिद्धौ च — यो भक्तं ददाति, स स्वर्गं गच्छति. "
               "अकिंवृत्तार्थोऽयमारम्भः: the rule exists FOR the case "
               "3.3.6 could not reach, where no form of किम् stands. "
               "The vṛtti explains the use rather than the form — "
               "लिप्स्यमानाद् भक्तात् स्वर्गसिद्धिमाचक्षाणो दातारं "
               "प्रोत्साहयति, one urges a giver on by telling him what "
               "his gift will get him"),
    Lakara("3.3.8", "laṭ", time="bhaviṣyat", optional=True,
           lodartha=True,
           why="लोडर्थलक्षणे च — उपाध्यायश्चेदागच्छति, अथ त्वं "
               "छन्दोऽधीष्व. लोडर्थः प्रैषादिर्लक्ष्यते येन: the act "
               "is what MARKS OUT the command, not what is commanded. "
               "उपाध्यायागमनमध्ययनप्रैषस्य लक्षणम् — the teacher's "
               "coming is the sign of the order to study, and the "
               "future ending falls on the sign"),
    Lakara("3.3.9", "liṅ", also="laṭ", time="bhaviṣyat", optional=True,
           lodartha=True, urdhvamauhurtika=True,
           why="लिङ् चोर्ध्वमौहूर्तिके — ऊर्ध्वं मुहूर्ताद् भव "
               "ऊर्ध्वमौहूर्तिकः, later than this hour. "
               "उपाध्यायश्चेदागच्छेत्. चकाराल्लट् च, so both endings "
               "stand, and भविष्यतश्चैतद् विशेषणम् — the hour "
               "qualifies the FUTURE and is not a time of its own. "
               "The compound itself is a निपातन: निपातनात् समासः, "
               "उत्तरपदवृद्धिश्च"),
    Lakara("3.3.13", "lṛṭ", time="bhaviṣyat", kriyartha=None,
           why="लृट् शेषे च — करिष्यति, हरिष्यति. शेषः "
               "क्रियार्थोपपदादन्यः: the REST is whatever the rules "
               "just before did not take, so this rule is defined by "
               "the ones around it and states no condition of its own. "
               "And चकारात् क्रियायां चोपपदे क्रियार्थायाम् — the च "
               "reaches back INTO what was excepted, so लृट् stands "
               "there too: करिष्यामीति व्रजति. A rule that means "
               "'everything else, and also the thing else was defined "
               "against'"),
    Lakara("3.3.15", "luṭ", time="bhaviṣyat", anadyatana=True,
           why="अनद्यतने लुट् — श्वःकर्ता, श्वो भोक्ता. लृटोऽपवादः. "
               "अनद्यतन इति बहुव्रीहिनिर्देशः, तेन व्यामिश्रे न भवति: "
               "अद्य श्वो वा भविष्यति — the compound's form excludes "
               "the MIXED case, exactly as it did at 3.2.111 for the "
               "past. One device, one reason, two tenses apart. "
               "SCOPE: परिदेवने श्वस्तनी भविष्यदर्थे वक्तव्या is a "
               "vārttika for lament — इयं नु कदा गन्ता, यैवं पादौ "
               "निदधाति"),
    # --- 3.3.133 to 3.3.152 — a लकार chosen on a SENSE ----------------
    # From here to the end of the pāda nearly every rule turns on what
    # is meant — hope, blame, disbelief, wonder — where 3.2's turned on
    # the situation of speaking. Each is सर्वलकाराणामपवादः, defeating
    # every ending the tense rules would have given.
    Lakara("3.3.133", "lṛṭ", time="bhaviṣyat", beside=("kṣipra",),
           sense=("āśaṃsā",),
           why="क्षिप्रवचने लृट् — उपाध्यायश्चेत् क्षिप्रमागमिष्यति. "
               "भूतवच्चेत्यस्यायमपवादः, excepting 3.3.132.\n\n"
               "वचनग्रहणं पर्यायार्थम् — the word वचन is there so any "
               "SYNONYM of 'soon' counts: क्षिप्रं शीघ्रमाशु त्वरितम्. "
               "The identical device as 3.2.112's अभिज्ञावचने, and the "
               "identical wording.\n\n"
               "नेति वक्तव्ये लृड्ग्रहणं लुटोऽपि विषये यथा स्यात् — "
               "the rule could have been a plain प्रतिषेध and names "
               "लृट् instead, so that it reaches लुट्'s ground too: "
               "श्वः क्षिप्रमध्येष्यामहे"),
    Lakara("3.3.134", "liṅ", time="bhaviṣyat",
           beside=("āśaṃsāvacana",), sense=("āśaṃsā",),
           why="आशंसावचने लिङ् — उपाध्यायश्चेदागच्छेत्, आशंसे "
               "युक्तोऽधीयीय. भूतवच्चेत्यस्यायमपवादः. The companion "
               "is a word that EXPRESSES the hope, not the hope "
               "itself — आशंसा येनोच्यते तदाशंसावचनम्"),
    Lakara("3.3.139", "lṛṅ", time="bhaviṣyat", kriyatipatti=True,
           lin_nimitta=True,
           why="लिङ्निमित्ते लृङ् क्रियातिपत्तौ — दक्षिणेन "
               "चेदायास्यन्न शकटं पर्याभविष्यत्. "
               "कुतश्चिद् वैगुण्यादनभिनिर्वृत्तिः क्रियायाः "
               "क्रियातिपत्तिः, the act failing of something.\n\n"
               "A CONDITION ABOUT ANOTHER RULE HAVING APPLIED. "
               "लिङ्निमित्त means that some rule — 3.3.156 and the "
               "like — would have given लिङ् here. Nothing in either "
               "pāda had asked that before: every other condition has "
               "been about the act, the speaker or the company, and "
               "this is about the GRAMMAR's own state"),
    Lakara("3.3.140", "lṛṅ", kriyatipatti=True, lin_nimitta=True,
           why="भूते च — दृष्टो मया भवत्पुत्रोऽन्नार्थी, यदि स तेन "
               "दृष्टोऽभविष्यत् तदाभोक्ष्यत; न तु भुक्तवान्. The rule "
               "before gave it for the future and this for the past, "
               "so the ending covers a failed act in either time"),
    Lakara("3.3.142", "laṭ", beside=("api", "jātu"),
           sense=("garhā",),
           why="गर्हायां लडपिजात्वोः — अपि तत्र भवान् वृषलं याजयति; "
               "गर्हामहे, अहोऽन्याय्यमेतत्. गर्हा कुत्सेत्यनर्थान्तरम्.\n\n"
               "AND IT DEFEATS THE TENSE RULES BY BEING LATER. "
               "वर्तमाने लट् उक्तः कालसामान्ये न प्राप्नोतीति विधीयते "
               "— 3.2.123 gives लट् for the present and could not "
               "reach every time; कालविशेषविहितांश्चापि प्रत्ययानयं "
               "परत्वाद् अस्मिन् विषये बाधते, and this defeats the "
               "time-specific endings by standing later. The first "
               "rule of the pāda to win by परत्व rather than by "
               "narrowness"),
    Lakara("3.3.143", "liṅ", also="लट्", beside=("katham",),
           sense=("garhā",), optional=True,
           why="विभाषा कथमि लिङ् च — कथं नाम तत्र भवान् वृषलं "
               "याजयेत्, and by the च याजयति. "
               "विभाषाग्रहणं यथास्वं कालविषये विहितानामबाधनार्थम् — "
               "the option is there so the ordinary tense endings are "
               "NOT defeated, and the vṛtti lists seven forms that "
               "stand together"),
    Lakara("3.3.144", "liṅ", also="लृट्", kimvrtta=True,
           sense=("garhā",),
           why="किंवृत्ते लिङ्लृटौ — को नाम वृषलो यं तत्र भवान् "
               "याजयेत्. सर्वलकाराणामपवादः, and "
               "लिङ्ग्रहणं लटोऽपरिग्रहार्थम् — लिङ् is named so that "
               "लट् is NOT taken in, which the rule before had "
               "allowed"),
    Lakara("3.3.145", "liṅ", also="लृट्",
           sense=("anavakḷpti", "amarṣa"),
           why="अनवक्ऌप्त्यमर्षयोरकिंवृत्तेऽपि — नावकल्पयामि, न "
               "श्रद्दधे, तत्र भवान् नाम वृषलं याजयेत्. "
               "अनवक्ऌप्तिरसंभावना, अमर्षोऽक्षमा — disbelief and "
               "indignation. सर्वलकाराणामपवादः.\n\n"
               "AND यथासंख्यम् IS REFUSED, ON THE SAME GROUND 3.2.29 "
               "USED. बह्वचः पूर्वनिपातो लक्षणव्यभिचारचिह्नम्, तेन "
               "यथासंख्यं न भवति — the LONGER word standing first is "
               "the sign that the counting-off does not apply, since "
               "2.2.34 would have put the shorter first. The identical "
               "argument, the identical rule appealed to, and a pāda "
               "apart"),
    Lakara("3.3.146", "lṛṭ", beside=("kiṃkila", "asti", "bhavati",
                                     "vidyate"),
           sense=("anavakḷpti", "amarṣa"),
           why="किंकिलास्त्यर्थेषु लृट् — किंकिल नाम तत्र भवान् "
               "वृषलं याजयिष्यति. लिङोऽपवादः. अस्त्यर्था "
               "अस्तिभवतिविद्यतयः, three verbs counted as meaning "
               "'is'. लिङ्निमित्तमिह नास्ति तेन लृङ् न भवति — and "
               "because no rule gives लिङ् here, 3.3.139's ending "
               "cannot come either. A rule's absence as a condition"),
    Lakara("3.3.147", "liṅ", beside=("jātu", "yad", "yadā", "yadi"),
           sense=("anavakḷpti", "amarṣa"),
           why="जातुयदोर्लिङ् — जातु तत्र भवान् वृषलं याजयेत्. "
               "लृटोऽपवादः. SCOPE: जातुयदोर्लिङ्विधाने "
               "यदायद्योरुपसंख्यानम् adds यदा and यदि"),
    Lakara("3.3.148", "liṅ", beside=("yac", "yatra"),
           sense=("anavakḷpti", "amarṣa"),
           why="यच्चयत्रयोः — यच्च तत्र भवान् वृषलं याजयेत्. "
               "लृटोऽपवादः, and योगविभाग उत्तरार्थः — split for the "
               "sake of the two rules after, as 3.3.115 was. "
               "यथासंख्यं नेष्यते here too"),
    Lakara("3.3.149", "liṅ", beside=("yac", "yatra"),
           sense=("garhā",),
           why="गर्हायां च — यत्र तत्र भवान् वृषलं याजयेद् ऋद्धो "
               "वृद्धः सन् ब्राह्मणः; गर्हामहे. सर्वलकाराणामपवादः. "
               "The same two companions as 3.3.148 with a different "
               "sense — which is what the योगविभाग bought"),
    Lakara("3.3.150", "liṅ", beside=("yac", "yatra"),
           sense=("citrīkaraṇa",),
           why="चित्रीकरणे च — यच्च तत्र भवान् वृषलं याजयेत्, "
               "आश्चर्यमेतत्. चित्रीकरणमाश्चर्यमद्भुतं विस्मयनीयम्. "
               "The third sense given to one pair of companions in "
               "three sūtras"),
    Lakara("3.3.151", "lṛṭ", sense=("citrīkaraṇa",),
           not_beside=("yadi",),
           why="शेषे लृडयदौ — आश्चर्यं चित्रमद्भुतम्, अन्धो नाम "
               "पर्वतमारोक्ष्यति; बधिरो नाम व्याकरणमध्येष्यते. "
               "शेषः is whatever is not यच् or यत्र, and the rule "
               "REFUSES यदि: अयदाविति किम्? आश्चर्यं यदि स भुञ्जीत. "
               "लिङ्निमित्ताभावादिह लृङ् न भवति"),
    Lakara("3.3.152", "liṅ", beside=("uta", "api"),
           why="उताप्योः समर्थयोर्लिङ् — उत कुर्यात्, अप्यधीयीत, "
               "बाढमध्येष्यत इत्यर्थः. समर्थयोः means the two are "
               "used in ONE sense, बाढम्; समर्थयोरिति किम्? उत दण्डः "
               "पतिष्यति — there they mark a question.\n\n"
               "AND IT ENDS AN OPTION THAT HAD RUN FOR ELEVEN SŪTRAS. "
               "वोताप्योः इति विकल्पो निवृत्तः: 3.3.141 had made "
               "3.3.140's लृङ् optional AS FAR AS THIS RULE, naming it "
               "as the boundary — मर्यादायामयमाङ् नाभिविधौ, the आ "
               "marking a limit and not inclusion. So इतः प्रभृति "
               "भूतेऽपि लिङ्निमित्ते क्रियातिपत्तौ नित्यं लृङ्. An "
               "extent stated by naming its far end, as 3.2.134 and "
               "3.3.56 did"),
    # --- 3.3.153 to 3.3.176 — the लकार of a mood ----------------------
    Lakara("3.3.153", "liṅ", sense=("kāmapravedana",),
           not_beside=("kaccit",),
           why="कामप्रवेदनेऽकच्चिति — कामो मे भुञ्जीत भवान्, "
               "अभिलाषो मे भुञ्जीत भवान्. सर्वलकाराणामपवादः. "
               "स्वाभिप्रायाविष्करणं कामप्रवेदनम्, making one's own "
               "wish known. अकच्चितीति किम्? and the vṛtti answers "
               "with a VERSE — कच्चिज्जीवति ते माता — where कच्चित् "
               "asks after another's welfare and not one's own wish"),
    Lakara("3.3.154", "liṅ", sense=("saṃbhāvanā",),
           beside=("alam",),
           why="संभावनेऽलमिति चेत् सिद्धाप्रयोगे — अपि पर्वतं शिरसा "
               "भिन्द्यात्, अपि द्रोणपाकं भुञ्जीत. "
               "संभावनं क्रियासु योग्यताध्यवसानम्, शक्तिश्रद्धानम् — "
               "trusting that a thing is within someone's power.\n\n"
               "AND THE CONDITION IS THAT A WORD BE UNDERSTOOD AND "
               "NOT SAID. सिद्धश्चेदलमोऽप्रयोगः; क्व चासौ सिद्धः? "
               "यत्र गम्यते चार्थो न चासौ प्रयुज्यते — अलम् must be "
               "meant and NOT uttered. सिद्धाप्रयोग इति किम्? "
               "अलं देवदत्तो हस्तिनं हनिष्यति, where it IS uttered and "
               "the rule fails. A condition on a word's absence, which "
               "nothing in either pāda had asked"),
    Lakara("3.3.155", "liṅ", sense=("saṃbhāvanā",), optional=True,
           not_beside=("yad",),
           why="विभाषा धातौ संभावनवचनेऽयदि — संभावयामि भुञ्जीत भवान्, "
               "संभावयामि भोक्ष्यते भवान्; अवकल्पयामि, श्रद्दधे. "
               "पूर्वेण नित्यप्राप्तौ विकल्पार्थं वचनम् — the rule "
               "before made it obligatory and this offers a choice. "
               "अयदीति किम्? संभावयामि यद् भुञ्जीत भवान्"),
    Lakara("3.3.156", "liṅ", sense=("hetuhetumat",), optional=True,
           why="हेतुहेतुमतोर्लिङ् — दक्षिणेन चेद् यायाद् न शकटं "
               "पर्याभवेत्. हेतुः कारणम्, हेतुमत् फलम्; दक्षिणेन यानं "
               "हेतुः, अपर्याभवनं हेतुमत्.\n\n"
               "THIS IS THE RULE 3.3.139 AND 3.3.140 MEANT BY "
               "लिङ्निमित्त — इत्येवमादिकं लिङो निमित्तम् — so a "
               "condition stated seventeen sūtras earlier is only now "
               "given its content. क्रियातिपत्तौ लृङ् भवति.\n\n"
               "विभाषा चायमिष्यते, भविष्यति च काले, तेन लृडपि भवति. "
               "And लिङिति वर्तमाने पुनर्लिङ्ग्रहणं "
               "कालविशेषप्रतिपत्त्यर्थम् — लिङ् was already running "
               "and is named AGAIN so a particular time is understood, "
               "तेनेह न भवति हन्तीति पलायते, वर्षतीति धावति. A word "
               "repeated to NARROW, where 3.2.106 and 3.2.124 repeated "
               "one to widen and 3.3.44 to cancel"),
    Lakara("3.3.157", "liṅ", also="लोट्", sense=("icchā",),
           why="इच्छार्थेषु लिङ्लोटौ — इच्छामि भुञ्जीत भवान्, इच्छामि "
               "भुङ्क्ता भवान्; कामये, प्रार्थये. "
               "सर्वलकाराणामपवादः. SCOPE: कामप्रवेदन इति वक्तव्यम्, "
               "इह मा भूत् — इच्छन् करोति"),
    Lakara("3.3.159", "liṅ", sense=("icchā-samānakartṛka",),
           why="लिङ् च — भुञ्जीयेतीच्छति, अधीयीयेतीच्छति. "
               "क्रियातिपत्तौ लृङ् भवति. योगविभाग उत्तरार्थः, the "
               "FOURTH split in this pāda made for the rule after — "
               "3.3.115, 3.3.137 and 3.3.148 were the others"),
    Lakara("3.3.160", "liṅ", sense=("icchā",), optional=True,
           time="vartamāna",
           why="इच्छार्थेभ्यो विभाषा वर्तमाने — इच्छति and इच्छेत्, "
               "वष्टि and उश्यात्, कामयते and कामयेत. लटि प्राप्ते "
               "वचनम्: the rule exists because 3.2.123's लट् had the "
               "ground, and it offers लिङ् beside. The FIRST row of "
               "this table with the present as its time since 3.2.123 "
               "itself"),
    Lakara("3.3.161", "liṅ", sense=VIDHYADI_SENSES,
           why="विधिनिमन्त्रणामन्त्रणाधीष्टसंप्रश्नप्रार्थनेषु लिङ् — "
               "कटं कुर्यात्; इह भवान् भुञ्जीत; अधीच्छामो भवन्तम्, "
               "माणवकं भवानुपनयेत्; किं नु खलु भो "
               "व्याकरणमधीयीय. सर्वलकाराणामपवादः.\n\n"
               "Six senses, each glossed: विधिः प्रेरणम्, निमन्त्रणं "
               "नियोगकरणम्, आमन्त्रणं कामचारकरणम्, अधीष्टः "
               "सत्कारपूर्वको व्यापारः, संप्रश्नः संप्रधारणम्, "
               "प्रार्थनं याच्ञा — and the vṛtti distinguishes the "
               "second from the third by whether the thing is BINDING: "
               "निमन्त्रण obliges and आमन्त्रण leaves one free.\n\n"
               "विध्यादयश्च प्रत्ययार्थविशेषणम् — the senses qualify "
               "what the AFFIX means, not the root: विध्यादिविशिष्टेषु "
               "कर्त्रादिषु लिङ् प्रत्ययो भवति"),
    Lakara("3.3.162", "loṭ", sense=VIDHYADI_SENSES,
           why="लोट् च — कटं तावद् भवान् करोतु; अमुत्र भवानास्ताम्; "
               "किं नु खलु भो व्याकरणमध्ययै. योगविभाग उत्तरार्थः, the "
               "fifth such split, and this one is what 3.3.163 then "
               "has to protect the कृत्य affixes from"),
    Lakara("3.3.164", "liṅ", sense=PRAISADI_SENSES,
           urdhvamauhurtika=True,
           why="लिङ् चोर्ध्वमौहूर्तिके — ऊर्ध्वं मुहूर्तादुपरि "
               "मुहूर्तस्य भवान् खलु कटं कुर्यात्. चकाराद् यथाप्राप्तं "
               "च, so what would otherwise come stands as well.\n\n"
               "ऊर्ध्वमौहूर्तिक was 3.3.9's condition too, a hundred "
               "and fifty-five sūtras back and for the same ending. "
               "The pāda's first rule and its last stretch reach for "
               "one word"),
    Lakara("3.3.165", "loṭ", beside=("sma",), sense=PRAISADI_SENSES,
           urdhvamauhurtika=True,
           why="स्मे लोट् — ऊर्ध्वं मुहूर्ताद् भवान् कटं करोतु स्म, "
               "ग्रामं गच्छतु स्म. लिङ्कृत्यानामपवादः — it displaces "
               "BOTH the ending 3.3.164 gives and the कृत्य affixes "
               "3.3.163 gives, which is why it has to name neither"),
    Lakara("3.3.166", "loṭ", beside=("sma",), sense=("adhīṣṭa",),
           why="अधीष्टे च — अङ्ग स्म राजन् माणवकमध्यापय, अङ्ग स्म "
               "राजन्नग्निहोत्रं जुहुधि. लिङोऽपवादः. अधीष्टम् was "
               "glossed at 3.3.161 and is not glossed again — "
               "अधीष्टं व्याख्यातम्, the vṛtti pointing back rather "
               "than repeating"),
    Lakara("3.3.168", "liṅ", beside=("yad",), sense=("kāla",),
           why="लिङ् यदि — कालो यद् भुञ्जीत भवान्, समयो यद् भुञ्जीत, "
               "वेला यद् भुञ्जीत. तुमुनोऽपवादः, so it displaces the "
               "affix 3.3.167 gives on the same companions"),
    Lakara("3.3.172", "liṅ", also="कृत्य", sense=("śakti",),
           why="शकि लिङ् च — भवान् खलु भारं वहेत्, and by the च भवता "
               "खलु भारो वोढव्यः, वहनीयः, वाह्यः. शकीति "
               "प्रकृत्यर्थविशेषणम्, the sense qualifying what the "
               "ROOT means and not what the affix does — the opposite "
               "of 3.3.161's विध्यादयश्च प्रत्ययार्थविशेषणम्, and the "
               "vṛtti marks the difference in both places.\n\n"
               "सामान्यविहितानां पुनर्वचनं लिङा बाधा मा भूदिति — the "
               "कृत्य affixes are stated again so this rule's own "
               "लिङ् shall not displace them. A rule protecting half "
               "of itself from the other half, as 3.3.169 does"),
    Lakara("3.3.173", "liṅ", also="लोट्", sense=("āśis",),
           why="आशिषि लिङ्लोटौ — चिरं जीव्याद् भवान्, चिरं जीवतु "
               "भवान्. आशंसनमाशीः, अप्राप्तस्येष्टस्यार्थस्य "
               "प्राप्तुमिच्छा — the wish for a good thing not yet "
               "had, which is word for word 3.3.132's gloss of "
               "आशंसा. Two words, one definition, forty sūtras apart. "
               "आशिषीति किम्? चिरं जीवति देवदत्तः.\n\n"
               "प्रकृत्यर्थविशेषणं चैतत्, qualifying the root's sense "
               "as 3.3.172's does"),
    Lakara("3.3.175", "luṅ", beside=("māṅ",),
           why="माङि लुङ् — मा कार्षीत्, मा हार्षीत्. "
               "सर्वलकाराणामपवादः.\n\n"
               "AND A FORM IN USE IS CALLED WRONG. कथं मा भवतु तस्य "
               "पापम्, मा भविष्यतीति? असाधुरेवायम् — that is simply "
               "not correct. Then केचिदाहुः — अङिदपरो माशब्दो "
               "विद्यते, तस्यायं प्रयोगः: SOME say there is another "
               "मा, not the one this rule names, and this is its use. "
               "The commentary condemning a form and then recording "
               "a way to save it, without choosing between them"),
    Lakara("3.3.176", "laṅ", also="लुङ्", beside=("sma-māṅ",),
           why="स्मोत्तरे लङ् च — मा स्म करोत्, मा स्म कार्षीत्; मा "
               "स्म हरत्, मा स्म हार्षीत्. चकाराल्लुङ् च, so both "
               "endings stand.\n\n"
               "THE LAST RULE OF THE PĀDA, and the Kāśikā closes here "
               "with its colophon: इति श्रीजयादित्यविरचितायां "
               "काशिकायां वृत्तौ तृतीयाध्यायस्य तृतीयः पादः"),
    # --- 3.4.2 to 3.4.8 — the opening of पाद ४ ------------------------
    # These stand under धातुसंबन्ध from 3.4.1, which is why they can
    # hold in ALL times at once: सर्वेषु कालेषु. No rule of 3.2 or 3.3
    # did that — each of those chose an ending FOR a time.
    Lakara("3.4.2", "loṭ", time="sarva", doubled=True,
           sense=("kriyāsamabhihāra",),
           why="क्रियासमभिहारे लोट् — लुनीहिलुनीहीत्येवायं लुनाति, "
               "and the same with इमौ लुनीतः, इमे लुनन्ति. "
               "पौनःपुन्यं भृशार्थो वा क्रियासमभिहारः, doing a thing "
               "again and again or doing it hard. "
               "सर्वलकाराणामपवादः, and it holds in ALL TIMES: भूते "
               "अलावीत्, भविष्यति लविष्यति. No rule of 3.2 or 3.3 "
               "gave one ending for every time — each of those chose "
               "an ending FOR a time.\n\n"
               "AND THE ENDING IS THEN REPLACED, WHICH THE RULE DOES "
               "NOT SAY. तस्य च लोटो हि स्व इत्येतावादेशौ भवतः, "
               "तध्वंभाविनस्तु वा भवतः — and the vṛtti asks for a "
               "योगविभाग to get it: क्रियासमभिहारे लोड् भवति, ततो "
               "लोटो हिस्वौ, लोडित्येव. Read so, लोड्धर्माणौ हिस्वौ "
               "भवतः — they merely BEHAVE like लोट्, तेनात्मनेपद"
               "परस्मैपदत्वं भेदेनावतिष्ठते, so the distinction of "
               "voice survives the substitution.\n\n"
               "SETTLED — क्रियासमभिहाराभिव्यक्तौ द्विर्वचनमयं "
               "लोडपेक्षते (वा० ८.१.१२): this ending NEEDS the "
               "doubling to show the sense, यङ्प्रत्ययः पुनर् ... "
               "स्वयमेव शक्तत्वाद् नापेक्षते द्विर्वचनम् — where the "
               "affix यङ्, given for that very sense, does not. Two "
               "ways to one meaning, one of them needing help"),
    Lakara("3.4.3", "loṭ", time="sarva", doubled=True, optional=True,
           sense=("samuccaya",),
           why="समुच्चये सामान्यवचनस्य — भ्राष्ट्रमट, मठमट, खदूरमट, "
               "स्थाल्यपिधानमटेत्येवायमटति. अनेकक्रियाध्याहारः "
               "समुच्चयः, several acts taken together.\n\n"
               "अन्यतरस्याम्, and the vṛtti spells out the "
               "alternative in full: अथवा भ्राष्ट्रमटति, मठमटति ... "
               "इत्येवायमटति — the same string of clauses with the "
               "ordinary present ending instead. It then does the "
               "whole paradigm twice over, in both voices, for two "
               "roots. The longest worked example in these three "
               "pādas, and every form of it is the same sentence "
               "with one ending changed"),
    Lakara("3.4.6", "luṅ", also="लङ्, लिट्", time="sarva",
           chandasi=True, optional=True,
           why="छन्दसि लुङ्लङ्लिटः — शकलाङ्गुष्ठकोऽकरत्, अहं तेभ्योऽ"
               "करं नमः (मा०सं० १६.८) for लुङ्; अग्निमद्य होतारम् "
               "(शा०श्रौ० ५.२०.५) अवृणीतायं यजमानः for लङ्; अद्या "
               "ममार (ऋ० १०.५५.५), अद्य म्रियते, for लिट्.\n\n"
               "THREE PAST ENDINGS USED FOR ANY TIME AT ALL, in the "
               "Veda: धातुसंबन्धे सर्वेषु कालेषु. And the vṛtti opens "
               "it further — अन्यतरस्यामिति वर्तते, तेनान्येऽपि "
               "लकारा यथायथं भवन्ति: the option carries down from "
               "3.4.3, so OTHER endings stand too as each fits.\n\n"
               "This is the rule 3.2.105 has been citing since that "
               "block was written, and it could then be recorded and "
               "not run"),
    Lakara("3.4.7", "leṭ", time="sarva", chandasi=True,
           optional=True, lin_nimitta=True,
           why="लिङर्थे लेट् — जोषिषत् (ऋ० २.३५.१), तारिषत् (ऋ० "
               "१.२५.१२), नेता इन्द्रो नेषत् (शा०श्रौ० ७.९.१), पताति "
               "दिद्युत् (ऋ० ७.२५.१), प्रजापतिर् उदधिं च्यावयाति "
               "(तै०सं० ३.५.५.२).\n\n"
               "AND ITS CONDITION IS THE ONE 3.3.139 INTRODUCED. "
               "लिङर्थे, यत्र लिङ् विधीयते विध्यादिः, हेतुहेतुमतोर्"
               "लिङ् इत्येवमादिः — wherever a rule gives लिङ्. The "
               "same appeal to the grammar's own state, and the same "
               "rule cited for it, thirteen sūtras into another "
               "pāda. लेट् is an ending the Veda alone has"),
    Lakara("3.4.8", "leṭ", time="sarva", chandasi=True,
           sense=("upasaṃvāda", "āśaṅkā"),
           why="उपसंवादाशङ्कयोश्च — अहमेव पशूनामीशै (काठ०सं० २५.१); "
               "मदग्रा एव वो ग्रहा गृह्यान्तै (मै०सं० ४.५.८); "
               "नेज्जिह्मायन्त्यो नरकं पताम (ऋ०खिल १०.१०६.१).\n\n"
               "उपसंवादः परिभाषणम्, कर्तव्ये पणबन्धः — a bargain "
               "struck about what is to be done, and the vṛtti gives "
               "the whole shape of one: यदि मे भवानिदं कुर्याद् "
               "अहमपि भवत इदं दास्यामीति. कारणतः कार्यानुसरणं तर्कः, "
               "उत्प्रेक्षा, आशङ्का — inferring the effect from the "
               "cause.\n\n"
               "लिङर्थ एवायं नित्यार्थं तु वचनम्, पूर्वसूत्रेऽन्य"
               "तरस्यामिति वर्तते: the ground is 3.4.7's already and "
               "the rule exists to make it OBLIGATORY, the option "
               "having run there. A rule stated to remove a choice, "
               "as 3.3.66's नित्यम् was"),
)


def lakara_for(
    *,
    time: str = "bhūta",
    beside: str = "",
    anadyatana: bool = False,
    paroksa: bool = False,
    question: bool = False,
    recent: bool = False,
    answer: bool = False,
    sakanksa: bool = False,
    with_yad: bool = False,
    nipata: bool = False,
    kimvrtta: bool = False,
    lipsa: bool = False,
    lipsyamana_siddhi: bool = False,
    lodartha: bool = False,
    urdhvamauhurtika: bool = False,
    kriyartha: bool = False,
    kriyatipatti: bool = False,
    lin_nimitta: bool = False,
    sense: str = "",
    wants: str = "",
    chandasi: bool = False,
    doubled: bool = False,
) -> object:
    """
    Which tense-ending comes — 3.2.110 to 3.2.122, all of them past.

    3.2.110 gives लुङ् for the past at large and every rule after it
    narrows, so the MOST SPECIFIC row answers. 3.2.113 refuses rather
    than gives; what its words then take is 3.2.111's लङ्, so that is
    the rule reported and the प्रतिषेध rides on `blocked_by` — the
    decision 2.3.72 settled and 3.2.23 followed.
    """
    asked = dict(
        anadyatana=anadyatana, paroksa=paroksa, question=question,
        recent=recent, answer=answer, sakanksa=sakanksa,
        with_yad=with_yad, nipata=nipata, kimvrtta=kimvrtta,
        lipsa=lipsa, lipsyamana_siddhi=lipsyamana_siddhi,
        lodartha=lodartha, urdhvamauhurtika=urdhvamauhurtika,
        kriyartha=kriyartha, kriyatipatti=kriyatipatti,
        lin_nimitta=lin_nimitta, sense=sense,
        chandasi=chandasi, doubled=doubled,
    )
    matched = [row for row in LAKARA
               if row.time == time and _reaches(row, beside, asked)]
    refusals = [row for row in matched if row.refuses]
    giving = [row for row in matched if not row.refuses]
    for refusal in refusals:
        giving = [row for row in giving if row.gives != refusal.gives]
    if not giving:
        if refusals:
            best = max(refusals, key=_how_specific)
            return NotAdded(best.sutra, best.why, best.gives)
        return NotAdded(
            "",
            "No rule of this table reaches this. 3.2.110 to 3.2.122 "
            "are of the past, under 3.2.84 भूते; 3.2.123 is of the "
            "present; and 3.3.4 to 3.3.15 are of the future, under "
            "भविष्यति running from 3.3.3")
    if wants:
        # Two rules reaching one ground and giving different
        # endings — 3.3.161's लिङ् and 3.3.162's लोट् on the same
        # six senses, where both forms stand and nothing in the
        # situation is meant to tell them apart. The caller names
        # the one asked after, as four other entry points already
        # let it.
        named = [row for row in giving
                 if row.gives == wants or wants in row.also]
        if named:
            giving = named
    best = max(giving, key=_how_specific)
    return Added(best.gives, best.sutra, best.why, also=best.also,
                 blocked_by=refusals[0].sutra if refusals else "")


#: The conditions that are simply stated or not stated, with what
#: naming one is worth. `_reaches` and `_how_specific` both used to
#: enumerate every field by hand — two lists that had to be kept in
#: step, and the future rules would have made each of them twelve
#: lines. One tuple now feeds both, so a field cannot be added to the
#: filter and forgotten in the ranking.
_PLAIN: Tuple[Tuple[str, int], ...] = (
    ("question", 2), ("recent", 2), ("answer", 2),
    ("kimvrtta", 2), ("lipsa", 2),
    ("kriyatipatti", 3), ("lin_nimitta", 3),
    ("chandasi", 2), ("doubled", 2), ("lipsyamana_siddhi", 2),
    ("lodartha", 2), ("urdhvamauhurtika", 2),
)

#: The tri-state ones, where silence and denial are different things:
#: 3.2.115 requires परोक्ष and 3.2.119 requires its ABSENCE, so a flag
#: could not hold both.
_TRISTATE: Tuple[Tuple[str, int], ...] = (
    ("anadyatana", 1), ("paroksa", 1), ("sakanksa", 2),
    ("with_yad", 2), ("nipata", 2), ("kriyartha", 1),
)


def _how_specific(row: Lakara) -> int:
    """How much a row states. Naming a companion weighs most."""
    return (
        3 * (len(row.beside) > 0) + 2 * (len(row.not_beside) > 0)
        + 2 * (len(row.sense) > 0)
        + sum(w for f, w in _PLAIN if getattr(row, f))
        + sum(w for f, w in _TRISTATE if getattr(row, f) is not None)
    )


def _reaches(row: Lakara, beside: str,
             asked: Dict[str, object]) -> bool:
    """Whether one row covers this situation."""
    if row.beside and beside not in row.beside:
        return False
    if row.sense and asked.get('sense') not in row.sense:
        return False
    if row.not_beside and beside in row.not_beside:
        return False
    for field, _ in _TRISTATE:
        stated = getattr(row, field)
        if stated is not None and bool(stated) != asked[field]:
            return False
    for field, _ in _PLAIN:
        if getattr(row, field) and not asked[field]:
            return False
    return True

def provisions_for(sutra_id: str) -> Tuple[Lakara, ...]:
    """Every row a sūtra of this run states."""
    return tuple(r for r in LAKARA if r.sutra == sutra_id)

# ---------------------------------------------------------------------------
# 3.2.124 to 3.2.133 — what stands in place of लट्
# ---------------------------------------------------------------------------

#: 3.2.129's three senses, and the vṛtti glosses each: ताच्छील्यं
#: तत्स्वभावता, वयः शरीरावस्था यौवनादिः, शक्तिः सामर्थ्यम्.
ANAS_SENSES: Tuple[str, ...] = ("tācchīlya", "vayas", "śakti")


@dataclass(frozen=True)
class LatAdesa:
    """One rule putting शतृ or शानच् where लट् would have stood."""

    sutra: str
    gives: str
    also: str = ""
    of: Tuple[str, ...] = ()
    #: अप्रथमासमानाधिकरणे — agreeing with a word NOT in the first
    #: case. 3.2.125 exists because the first case IS wanted there,
    #: so this is tri-state.
    aprathama: object = None
    sambodhana: bool = False
    #: 3.2.126's लक्षण or हेतु, and they must be क्रियाविषय.
    lakshana_hetu: bool = False
    sense: str = ""
    #: 3.2.130's अकृच्छ्रिणि — the act comes easily to the doer.
    akrcchri: bool = False
    #: 3.2.131's अमित्रे and 3.2.132's यज्ञसंयोगे.
    amitra: bool = False
    yajna: bool = False
    why: str = ""


LAT_ADESA: Tuple[LatAdesa, ...] = (
    LatAdesa("3.2.124", "śatṛ", also="शानच्", aprathama=True,
             why="लटः शतृशानचावप्रथमासमानाधिकरणे — पचन्तं देवदत्तं "
                 "पश्य, पचमानं देवदत्तं पश्य; पचता कृतम्, पचमानेन "
                 "कृतम्. अप्रथमासमानाधिकरण इति किम्? देवदत्तः पचति. "
                 "AND लड्ग्रहणम् अधिकविधानार्थम्: लट् is named again "
                 "though it was running, and what that buys is that "
                 "the substitution reaches BEYOND the stated "
                 "condition — क्वचित् प्रथमासमानाधिकरणेऽपि भवति, सन् "
                 "ब्राह्मणः, विद्यमानो ब्राह्मणः, जुह्वत्, अधीयानः. "
                 "A seventh use of repetition, and the same one "
                 "3.2.106's लिड्ग्रहण made: to WIDEN. SCOPE: माङि "
                 "आक्रोशे, मा पचन्; and केचिद् विभाषाग्रहणम् "
                 "अनुवर्तयन्ति, सा च व्यवस्थिता — some carry down "
                 "3.2.121's विभाषा, read as settled case by case"),
    LatAdesa("3.2.125", "śatṛ", also="शानच्", sambodhana=True,
             why="संबोधने च — हे पचन्, हे पचमान. "
                 "प्रथमासमानाधिकरणार्थ आरम्भः: the rule exists "
                 "BECAUSE the vocative agrees with a first-case word, "
                 "which 3.2.124 shut out. The seventh time this pāda "
                 "writes a rule to reach past the condition of the "
                 "rule before it"),
    LatAdesa("3.2.126", "śatṛ", also="शानच्", lakshana_hetu=True,
             why="लक्षणहेत्वोः क्रियायाः — लक्षणे: शयाना भुञ्जते "
                 "यवनाः, तिष्ठन्तोऽनुशासति गणकाः; हेतौ: अर्जयन् "
                 "वसति, अधीयानो वसति. लक्ष्यते चिह्न्यते येन तत् "
                 "लक्षणम्, जनको हेतुः. क्रियाया इति किम्? "
                 "द्रव्यगुणयोर्मा भूत् — the mark must be an ACT and "
                 "not a thing or a quality: यः कम्पते सोऽश्वत्थः, "
                 "यदुत्प्लवते तल्लघु. AND THE COMPOUND'S ORDER IS "
                 "ITSELF EVIDENCE: लक्षणहेत्वोरिति निर्देशः "
                 "पूर्वनिपातव्यभिचारलिङ्गम् — हेतु should have stood "
                 "first by the rules of compound order, and its not "
                 "doing so is the sign that those rules are departed "
                 "from. The second time in this pāda a compound's own "
                 "form carries an argument, after 3.2.111's बहुव्रीहि"),
    LatAdesa("3.2.128", "śānan", of=("pū", "yaj"),
             why="पूङ्यजोः शानन् — पवमानः, यजमानः. AND A PRATYĀHĀRA "
                 "FORMED ACROSS SŪTRAS: the vṛtti asks how the "
                 "षष्ठीप्रतिषेध of 2.3.69 can apply if these affixes "
                 "are not लादेश at all, and answers तृन्निति "
                 "प्रत्याहारनिर्देशात् — a pratyāhāra तृन् running "
                 "from 3.2.124 to the न of तृन् at 3.2.135. "
                 "क्व संनिविष्टानां प्रत्याहारः? लटः शतृ० इत्यतः "
                 "प्रभृति आ तृनो नकारात्. Not over SOUNDS but over a "
                 "stretch of RULES, which is a use of the device this "
                 "project had not met"),
    LatAdesa("3.2.129", "cānaś", sense="tācchīlya",
             why="ताच्छील्यवयोवचनशक्तिषु चानश् — ताच्छील्ये कतीह "
                 "मण्डयमानाः; वयोवचने कतीह कवचं पर्यस्यमानाः; शक्तौ "
                 "कतीह पचमानाः. ताच्छील्यं तत्स्वभावता, वयः "
                 "शरीरावस्था यौवनादिः, शक्तिः सामर्थ्यम्"),
    LatAdesa("3.2.130", "śatṛ", of=("iṅ", "dhāri"), akrcchri=True,
             why="इङ्धार्योः शत्रकृच्छ्रिणि — अधीयन् पारायणम्, "
                 "धारयन्नुपनिषदम्. अकृच्छ्रः सुखसाध्यो यस्य कर्तुर् "
                 "धात्वर्थः सोऽकृच्छ्री — one for whom the act comes "
                 "easily. अकृच्छ्रिणीति किम्? कृच्छ्रेणाधीते"),
    LatAdesa("3.2.131", "śatṛ", of=("dviṣ",), amitra=True,
             why="द्विषोऽमित्रे — द्विषन्, द्विषन्तौ, द्विषन्तः. "
                 "अमित्रः शत्रुः. अमित्र इति किम्? द्वेष्टि भार्या "
                 "पतिम् — of a wife the rule does not reach"),
    LatAdesa("3.2.132", "śatṛ", of=("su",), yajna=True,
             why="सुञो यज्ञसंयोगे — सर्वे सुन्वन्तः, of those joined "
                 "in a sacrifice. संयोगग्रहणं "
                 "प्रधानकर्तृप्रतिपत्त्यर्थम्, याजकेषु मा भूत् — the "
                 "word संयोग is there so the PRINCIPAL doer is meant "
                 "and not the officiating priests. यज्ञसंयोग इति "
                 "किम्? सुनोति सुराम्"),
    LatAdesa("3.2.133", "śatṛ", of=("arh",), sense="praśaṃsā",
             why="अर्हः प्रशंसायाम् — अर्हन्निह भवान् विद्याम्. "
                 "प्रशंसा स्तुतिः. प्रशंसायामिति किम्? अर्हति चौरो "
                 "वधम् — of what one deserves in the bad sense the "
                 "rule does not reach"),
)


def lat_substitute(root: str = "", *, aprathama: bool = False,
                   sambodhana: bool = False,
                   lakshana_hetu: bool = False, sense: str = "",
                   akrcchri: bool = False, amitra: bool = False,
                   yajna: bool = False) -> object:
    """
    3.2.124 to 3.2.133 — what stands in place of लट्.

    शतृ and शानच् replace the present ending rather than being added
    to a root, so these answer here and not from the affix table. The
    same shape as 3.2.105-108 for लिट्.
    """
    matched = [row for row in LAT_ADESA
               if _lat_reaches(row, root, aprathama, sambodhana,
                               lakshana_hetu, sense, akrcchri, amitra,
                               yajna)]
    if not matched:
        return NotAdded(
            "",
            "No rule of 3.2.124 to 3.2.133 reaches this. They put शतृ "
            "or शानच् where लट् would have stood, and each states the "
            "circumstance in which it does")
    best = max(matched, key=_lat_specific)
    return Added(best.gives, best.sutra, best.why, also=best.also)


def _lat_specific(row: LatAdesa) -> int:
    return (
        3 * (len(row.of) > 0) + (row.aprathama is not None)
        + 2 * row.sambodhana + 2 * row.lakshana_hetu
        + 2 * bool(row.sense) + 2 * row.akrcchri + 2 * row.amitra
        + 2 * row.yajna
    )


def _lat_reaches(row: LatAdesa, root: str, aprathama: bool,
                 sambodhana: bool, lakshana_hetu: bool, sense: str,
                 akrcchri: bool, amitra: bool, yajna: bool) -> bool:
    if row.of and root not in row.of:
        return False
    if row.aprathama is not None and bool(row.aprathama) != aprathama:
        return False
    if row.sambodhana and not sambodhana:
        return False
    if row.lakshana_hetu and not lakshana_hetu:
        return False
    if row.sense and row.sense != sense:
        return False
    if row.akrcchri and not akrcchri:
        return False
    if row.amitra and not amitra:
        return False
    if row.yajna and not yajna:
        return False
    return True


def lat_provisions_for(sutra_id: str) -> Tuple[LatAdesa, ...]:
    """Every row a sūtra of the लट्-substitution run states."""
    return tuple(r for r in LAT_ADESA if r.sutra == sutra_id)


# ---------------------------------------------------------------------------
# 3.2.127 — a संज्ञा, naming the pair
# ---------------------------------------------------------------------------

#: The two affixes 3.2.127 names सत्.
SAT: Tuple[str, ...] = ("śatṛ", "śānac")


def sat_samjna(affix: str = "") -> object:
    """
    3.2.127 तौ सत् — those two bear the name सत्.

    It adds nothing; it names, as 3.2.102 named निष्ठा. And the vṛtti
    is careful about how far the name reaches: तौग्रहणम्
    उपाध्यसंसर्गार्थम्, शतृशानज्मात्रस्य संज्ञा भवति — तौ is said so
    that the NAME attaches to शतृ and शानच् at large and not only to
    them under the conditions of the rules just given. So a शतृ got
    from any rule is सत्, ब्राह्मणस्य कुर्वन्, ब्राह्मणस्य करिष्यन्.

    सत्प्रदेशाः — where the name is used: 2.2.11 and the rest.
    """
    if not affix:
        return NotAdded(
            "",
            "3.2.127 names no affix of its own. Ask it with an affix "
            "and it says whether that affix bears the name सत्")
    if affix not in SAT:
        return NotAdded(
            "",
            "%s does not bear the name सत्. 3.2.127 gives it to शतृ "
            "and शानच् only" % affix)
    return Added(
        affix, "3.2.127",
        "तौ सत् — and तौग्रहणम् उपाध्यसंसर्गार्थम्: the name attaches "
        "to शतृ and शानच् AT LARGE, not only under the conditions of "
        "the rules before, so ब्राह्मणस्य करिष्यन् is सत् too. "
        "सत्प्रदेशाः are 2.2.11 and the rest")


#: 3.3.14's ground, in the vṛtti's own order: obligatory in the first
#: three, optional otherwise. अप्रथमासमानाधिकरणादिषु नित्यम् — the
#: आदि is why this is a tuple and not one condition.
LRT_SAT_NITYA: Tuple[str, ...] = (
    "aprathama-samānādhikaraṇa", "sambodhana", "adhikaraṇa",
)


def lrt_substitute(*, aprathama: bool = False,
                   sambodhana: bool = False,
                   wants: str = "") -> object:
    """
    3.3.14 लृटः सद्वा — शतृ and शानच् standing where लृट् would.

    The rule names its affixes by the NAME 3.2.127 gave them rather
    than by their forms, so this asks 3.2.127 for them: लृटः स्थाने
    सत्संज्ञौ शतृशानचौ वा भवतः. If that रule ever stopped conferring
    the name, this one would stop reaching them, which is what the
    text says and what the code should do.

    व्यवस्थितविभाषेयम् — the option is SETTLED, not free. The vṛtti
    fixes it by pointing at the लट् rules: तेन यथा लटः शतृशानचौ
    तथास्यापि भवतः, अप्रथमासमानाधिकरणादिषु नित्यम्, अन्यत्र विकल्पः.
    So 3.2.124's condition decides whether this rule may be declined,
    and 3.3.14 states no condition of its own at all — it borrows the
    affixes from one rule and the conditions from another.

    करिष्यन्तं देवदत्तं पश्य, करिष्यमाणं देवदत्तं पश्य — obligatory.
    करिष्यन् देवदत्तः beside करिष्यति — प्रथमासमानाधिकरणे विकल्पः.
    """
    named = [affix for affix in SAT
             if isinstance(sat_samjna(affix), Added)]
    if not named:
        return NotAdded(
            "3.3.14",
            "3.3.14 reaches its affixes through the name सत्, and "
            "3.2.127 confers that name on none")
    if wants and wants not in named:
        return NotAdded(
            "",
            "3.3.14 puts in place of लृट् whatever bears the name "
            "सत् — %s does not, by 3.2.127" % wants)

    settled = aprathama or sambodhana
    gives = wants or named[0]
    also = "" if wants else "शानच्"
    why = ("लृटः सद्वा — the two affixes 3.2.127 calls सत् stand in "
           "place of लृट्. The rule names neither of them: it uses "
           "the संज्ञा, so what it reaches is whatever that rule "
           "gives the name to. व्यवस्थितविभाषेयम्, and the vṛtti "
           "settles the option by pointing at the लट् rules — तेन "
           "यथा लटः शतृशानचौ तथास्यापि भवतः. ")
    if settled:
        why += ("अप्रथमासमानाधिकरणादिषु नित्यम्: here it is "
                "OBLIGATORY — करिष्यन्तं देवदत्तं पश्य, करिष्यमाणं "
                "देवदत्तं पश्य, हे करिष्यन्, अर्जयिष्यमाणो वसति. "
                "The condition is 3.2.124's own.")
    else:
        why += ("अन्यत्र विकल्पः: here it may be declined — "
                "प्रथमासमानाधिकरणे विकल्पः, so करिष्यन् देवदत्तः "
                "stands and so does करिष्यति.")
    return Added(gives, "3.3.14", why, also=also)

#: 3.3.141 वोताप्योः — 3.3.140's लृङ् is OPTIONAL, and the rule states
#: how far by naming the sūtra where it stops: मर्यादायामयमाङ्
#: नाभिविधौ, the आ marking a limit and not inclusion. So the option
#: runs to 3.3.151 and 3.3.152 is outside it — इतः प्रभृति ... नित्यं
#: लृङ्.
#:
#: Held as a range because that is exactly what the rule states, and
#: the far end is READ FROM THE NAME rather than counted: the same
#: shape as 3.2.134's आ क्वेः and 3.3.56's यावत् कृत्यल्युटो बहुलम्.
LRN_OPTIONAL_THROUGH = "3.3.151"


def lrn_is_optional(sutra_id: str) -> bool:
    """
    Whether 3.3.140's लृङ् may be declined at a given rule.

    3.3.141 makes it optional from there up to but NOT including
    3.3.152, which the vṛtti settles by reading the आ as मर्यादा — a
    boundary — rather than अभिविधि, inclusion. Two readings of one
    prefix, and the choice changes where the option stops.
    """
    number = int(sutra_id.rsplit(".", 1)[1])
    return 141 <= number <= int(LRN_OPTIONAL_THROUGH.rsplit(".", 1)[1])

# -------------------------------------------------------------------------
# 3.4.77 and 3.4.78 — what a लकार IS, and what it becomes.
#
# This table has named its endings as bare strings since 3.2.110, and
# NORTH_STAR has carried the gap as a debt ever since: nothing could ask
# what one of them was. 3.4.69 said what a लकार DENOTES; these two say
# what the set of them is, and what each becomes.
# -------------------------------------------------------------------------

#: The ten लकाराः, in the order 3.4.77's vṛtti gives them —
#: अक्षरसमाम्नायवदानुपूर्व्या कथ्यन्ते, arranged as the alphabet is,
#: by the vowel each carries. Six are टित् and four ङित्: षट् टितः,
#: चत्वारो ङितः.
#:
#: The mark matters and is not decoration. 3.4.79, codified long
#: before the reading reached this pāda, replaces the टि of an
#: ātmanepada ending after a टित् लकार — which is why लट् gives पचते
#: and not *पचत.
LAKARA_LIST: Tuple[Tuple[str, str], ...] = (
    ("laṭ", "ṭit"),
    ("liṭ", "ṭit"),
    ("luṭ", "ṭit"),
    ("lṛṭ", "ṭit"),
    ("leṭ", "ṭit"),
    ("loṭ", "ṭit"),
    ("laṅ", "ṅit"),
    ("liṅ", "ṅit"),
    ("luṅ", "ṅit"),
    ("lṛṅ", "ṅit"),
)

#: 3.4.78's eighteen substitutes, in the rule's own order: three
#: persons by three numbers, in each of the two voices.
TIN: Tuple[str, ...] = (
    "tip", "tas", "jhi", "sip", "thas", "tha", "mip", "vas", "mas",
    "ta", "ātām", "jha", "thās", "āthām", "dhvam", "iṭ", "vahi",
    "mahiṅ",
)


def lakara_heading(name: str = "") -> object:
    """
    3.4.77 लस्य — the heading under which every rule from here
    replaces a लकार, and the enumeration of the ten.

    लस्येत्ययमधिकारः, अकार उच्चारणार्थः: the अ in the rule is only to
    make it sayable — the third letter of this project met with that
    job, after 3.3.57's द and 3.4.12's ल.

    दश लकारा अनुबन्धविशिष्टा विहिता अर्थविशेषे कालविशेषे च, तेषां
    विशेषकराननुबन्धानुत्सृज्य यत् सामान्यं तद् गृह्यते — ten endings
    were given, each marked and each for a particular sense or time,
    and what this rule takes is the COMMON element with the
    distinguishing marks let go. So one heading governs all ten
    without naming any.
    """
    if name and name not in dict(LAKARA_LIST):
        return NotAdded(
            "3.4.77",
            "%s is not one of the ten लकाराः. They are %s"
            % (name, ", ".join(n for n, _ in LAKARA_LIST)))
    why = (
        "लस्य — लस्येत्ययमधिकारः, यदित ऊर्ध्वमनुक्रमिष्यामः "
        "लस्येत्येवं तद् वेदितव्यम्. THE TEN ARE ENUMERATED HERE, and "
        "the reading of this project has met every one of them "
        "already as a bare string: लट्, लिट्, लुट्, लृट्, लेट्, लोट्, "
        "लङ्, लिङ्, लुङ्, लृङ्. षट् टितः, चत्वारो ङितः — six carry "
        "one mark and four the other, and "
        "अक्षरसमाम्नायवदानुपूर्व्या कथ्यन्ते, they are ordered as the "
        "alphabet is.\n\n"
        "दश लकारा अनुबन्धविशिष्टा विहिता अर्थविशेषे कालविशेषे च, "
        "तेषां विशेषकराननुबन्धानुत्सृज्य यत् सामान्यं तद् गृह्यते — "
        "what the heading takes is the COMMON element with the "
        "distinguishing marks let go, which is why one word governs "
        "all ten without naming any.\n\n"
        "अकार उच्चारणार्थः: the अ is there only to make the rule "
        "sayable — the third letter met with that job, after "
        "3.3.57's द and 3.4.12's ल.\n\n"
        "AND THE HEADING IS KEPT OFF ORDINARY WORDS BY WHAT RUNS "
        "INTO IT. अथ लकारमात्रस्य ग्रहणं कस्माद् न भवति — लुनाति "
        "चूडाल इति? धात्वधिकारोऽनुवर्तते, कर्त्रादयश्च विशेषकाः: the "
        "root-heading carries down and the kāraka words qualify, so "
        "a stray ल in a word is not reached")
    if name:
        mark = dict(LAKARA_LIST)[name]
        why += ("\n\n%s is %s, and the mark is not decoration: "
                "3.4.79 replaces the टि of an ātmanepada ending after "
                "a टित् लकार, which is why लट् gives पचते and not "
                "*पचत." % (name, mark))
    return Added(name or "the ten लकाराः", "3.4.77", why)


def lakara_substitutes(*, lakara: str = "") -> object:
    """
    3.4.78 तिप्तस्झिसिप्थस्थमिब्वस्मस्तातांझथासाथांध्वमिड्वहिमहिङ् —
    the eighteen endings that stand in place of a लकार.

    Three marks, each doing something other than making an ending:
    तिप्सिप्मिपां पकारः स्वरार्थः, the प for the accent; इटष्टकारः
    for 3.4.106 to pick it out; महिङो ङकारः प्रत्याहारग्रहणार्थः, the
    ङ so that तिङ् may be formed as a pratyāhāra — which is the name
    3.4.113 then uses to confer सार्वधातुक.

    So the last letter of the eighteenth substitute is what makes the
    whole set nameable, and a rule of this same pāda depends on it.
    """
    if lakara and lakara not in dict(LAKARA_LIST):
        return NotAdded(
            "3.4.78",
            "%s is not one of the ten लकाराः, so nothing stands in "
            "its place" % lakara)
    return Added(
        ", ".join(TIN), "3.4.78",
        "लस्य तिबादय आदेशा भवन्ति — पचति, पचतः, पचन्ति; पचसे, "
        "पचेथे, पचध्वे; एवमन्येष्वपि लकारेषूदाहार्यम्. Eighteen "
        "substitutes, three persons by three numbers in each of two "
        "voices.\n\n"
        "THREE MARKS, NONE OF THEM MAKING AN ENDING. तिप्सिप्मिपां "
        "पकारः स्वरार्थः — the प for the accent. इटष्टकार इटोऽत् इति "
        "विशेषणार्थः, तिबादिभिरादेशैस्तुल्यत्वाद् न देशविध्यर्थः — "
        "the ट so 3.4.106 can pick that one out, and expressly NOT to "
        "say where it goes. महिङो ङकारस्तिङ् इति "
        "प्रत्याहारग्रहणार्थः — the ङ on the LAST of the eighteen so "
        "that तिङ् may be formed as a pratyāhāra.\n\n"
        "That last is why 3.4.113 can say तिङः ... सार्वधातुकम् at "
        "all: the name of the whole set is made by the final letter "
        "of its final member. 3.4.113 is codified, and was written "
        "long before the reading reached this pāda")
