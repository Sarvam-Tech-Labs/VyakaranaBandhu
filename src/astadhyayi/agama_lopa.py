# -*- coding: utf-8 -*-
"""
६.१.५८–७१ — what is put in, what is put in place, and what goes.

Fourteen rules and four different kinds of operation, and the pāda
does not separate them. An augment (6.1.58, 6.1.59, 6.1.71), a
substitute (6.1.61, 6.1.62, 6.1.63), a form laid down whole (6.1.60),
and five removals (6.1.66–6.1.70). 6.1.64 and 6.1.65 stand inside the
run and are codified in `anga` as `dhatvadeh`.

**THE PAIR THE SECTION IS WORTH READING FOR IS 6.1.60 AND 6.1.61.**
They give the same word in the same shape, and one is a निपातन and
the other an आदेश. 6.1.60's vṛtti refuses to make शीर्षन् a substitute
for शिरस् and says why: **न पुनरयमादेशः शिरःशब्दस्य, सोऽपि हि छन्दसि
प्रयुज्यत एव** — both words are found in the corpus, so neither can
be standing in for the other. 6.1.61's vṛtti then argues the base
INTO the rule, which names none: **तद्धित इति हि परं निमित्तम्
उपादीयते, स तदनुरूपां प्रकृतिं शिरःशब्दम् आक्षिपति** — the rule
mentions only what FOLLOWS, and what follows drags in the base that
fits it. Two sūtras apart, and the evidence for each is different in
kind.

**AND ONE WORD'S PLACE IN A RULE FIXES AN ORDER.** 6.1.66 could have
been व्योर्वलि लोपः. **पूर्वं लोपग्रहणं किम्? वेरपृक्तलोपात् पूर्वं
वलि लोपो यथा स्यात्** — putting लोप first is what makes this removal
happen before 6.1.67's. कण्डू and लोलू are the forms that decide it.

**AND A WORD REPEATED IN AN EARLIER RULE PROVES IT DOES NOT CARRY TO
A LATER.** 6.1.68 says अपृक्तम्, which 6.1.67 had already supplied.
6.1.69's vṛtti reads that redundancy backwards: **अपृक्तमिति
नाधिक्रियते। तथा च पूर्वसूत्रे पुनरपृक्तग्रहणं कृतम्** — the word is
NOT in force here, and the proof is that the rule before had to say
it again. The inverse of the idle-word argument, and the same
machinery.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule acts and what
it puts in or takes out. It does not build राजा out of राजन् — that
wants 6.4.8, 8.2.7 and the संयोगान्त rules, none of them codified.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

#: 6.1.63's thirteen, यथासंख्यम् — each stem with the substitute that
#: stands for it before शस् and the endings after it. The rule lists
#: them in two runs of thirteen and pairs them off in order, which is
#: the whole of what यथासंख्यम् means.
PADADI: Dict[str, str] = {
    "pāda": "pad",
    "danta": "dat",
    "nāsikā": "nas",
    "māsa": "mās",
    "hṛdaya": "hṛd",
    "niśā": "niś",
    "asṛj": "asan",
    "yūṣa": "yūṣan",
    "doṣan": "doṣan",
    "yakṛt": "yakan",
    "śakṛt": "śakan",
    "udaka": "udan",
    "āsya": "āsan",
}

#: And three more from a vārttika: **पदादिषु मांस्पृत्स्नूनाम्
#: उपसंख्यानम्**. मांस्पचन्याः for मांसपचन्याः, पृत्सु for पृतनासु,
#: अधि स्नुषु for अधि सानुषु.
PADADI_VARTIKA: Dict[str, str] = {
    "māṃsa": "māṃs",
    "pṛtanā": "pṛt",
    "sānu": "snu",
}

#: 6.1.68's verse — why the rule is stated at all, when 8.2.23's
#: संयोगान्तलोप looks as though it would do the same work.
#:
#:     संयोगान्तस्य लोपे हि नलोपादिर्न सिध्यति।
#:     रात् तु ते नैव लोपः स्याद् धलस्तस्माद् विधीयते॥
WHY_THE_HAL_IS_STATED: Tuple[str, ...] = (
    "राजा — 8.2.23 is असिद्ध, so the न् would never drop",
    "उखास्रत् — the द् is not पदान्त, so 8.2.39 would not reach it",
    "अभिनोऽत्र — 6.1.113's उत्व wants a रु to work on",
    "अबिभर्भवान् — 8.2.24's रात् सस्य confines the loss to a स्",
)


@dataclass(frozen=True)
class Change:
    """One rule of 6.1.58–71: what it puts in, in place, or takes out."""

    sutra: str
    #: What kind of operation: āgama, ādeśa, lopa, or nipātana.
    does: str = ""
    #: The stems or roots the rule names.
    of: Tuple[str, ...] = ()
    #: What follows: jhal-akit, ya-taddhita, ac-taddhita,
    #: śas-prabhṛti, val, pit-kṛt, sambuddhi, su-ti-si.
    before: str = ""
    #: What must precede — hal, ṅī, āp at 6.1.68; eṅ, hrasva at
    #: 6.1.69; hrasva at 6.1.71.
    after: Tuple[str, ...] = ()
    #: The penultimate sound the root must have — ऋ at 6.1.59.
    upadha: str = ""
    #: The accent the धातुपाठ gave it — अनुदात्त at 6.1.59.
    accent: str = ""
    #: What is put in, where the rule adds something: अम्, तुक्.
    gives: str = ""
    #: What is put in place of what, where the rule substitutes.
    adesa: str = ""
    #: True where the substitute depends on WHICH stem asked, and is
    #: read off a mapping rather than written in the row. 6.1.63
    #: alone: thirteen names and thirteen substitutes paired
    #: यथासंख्यम्, which a single column could not hold without
    #: splitting one rule into thirteen rows.
    by_mapping: bool = False
    #: What is taken out, where the rule removes: व्/य्, the वि affix,
    #: सु/ति/सि, the हल् of a vocative, शि.
    drops: str = ""
    optional: bool = False
    chandasi: bool = False
    bahulam: bool = False
    #: True where the form is laid down whole rather than derived —
    #: 6.1.60, and the vṛtti insists on the difference.
    nipatana: bool = False
    #: The rule this one displaces, by ITS own number.
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


CHANGE_TABLE: Tuple[Change, ...] = (
    Change(
        "6.1.58", does="āgama", of=("sṛj", "dṛś"), before="jhal-akit",
        gives="am", blocks=("7.3.86",),
        keeps_out="सर्जनम्, दर्शनम् — the affix does not begin on a "
                  "झल्; सृष्टः, दृष्टः — it is कित्; रज्जुसृड्भ्याम् "
                  "— the affix is not one a धातु takes",
        why="सृजिदृशोर्झल्यमकिति — before an affix beginning with a "
            "झल् and not marked क्, these two take the augment अम्: "
            "**स्रष्टा, स्रष्टुम्, स्रष्टव्यम्; द्रष्टा, द्रष्टुम्, "
            "द्रष्टव्यम्**.\\n\\n"
            "**AND IT IS AN अपवाद OF THE GUṆA.** "
            "**लघूपधगुणापवादोऽयममागमः** — 7.3.86 would have given "
            "सर्ज् and दर्श्, and the augment displaces it. Not a "
            "second operation but one instead of another.\\n\\n"
            "**AND ONE LATER RULE STILL APPLIES, AFTERWARDS.** "
            "**अस्राक्षीत्, अद्राक्षीत् — सिचि वृद्धिः अमि कृते "
            "भवति, पूर्वं तु बाध्यते** — 7.2.1's vṛddhi takes effect "
            "ONCE the अम् is in, and not before. The augment beats "
            "the guṇa outright and merely delays the vṛddhi.\\n\\n"
            "**AND NAMING THE ROOTS RESTRICTS WHICH AFFIXES COUNT.** "
            "**धातोः स्वरूपग्रहणे तत्प्रत्यये कार्यविज्ञानात्** — "
            "the rule names सृज् and दृश् rather than saying धातोः, "
            "so it reaches only affixes given after a ROOT. "
            "**रज्जुसृड्भ्याम्, देवदृग्भ्याम्** are untouched"),
    Change(
        "6.1.59", does="āgama", before="jhal-akit", upadha="ṛ",
        accent="anudātta", gives="am", optional=True,
        keeps_out="वर्ढा — वृहू is उदात्त in the धातुपाठ; भेत्ता, "
                  "छेत्ता — the penult is not ऋ; तर्पणम् — no झल्; "
                  "तृप्तः — कित्",
        why="अनुदात्तस्य च ऋदुपधस्यान्यतरस्याम् — the same augment, "
            "optionally, for a root the धातुपाठ marked अनुदात्त "
            "with ऋ for its penult: **त्रप्ता, तर्पिता, तर्प्ता; "
            "द्रप्ता, दर्पिता, दर्प्ता**.\\n\\n"
            "**AND THREE FORMS COME FROM TWO OPTIONS CROSSING.** "
            "तृप् and दृप् are रधादि, so 7.2.45 makes their इट् a "
            "choice as well. **अनुदात्तोपदेशः पुनरमर्थ एव** — being "
            "अनुदात्त in the धातुपाठ is what this rule turns on, and "
            "the इट् has its own reason. Two independent options, "
            "three attested forms.\\n\\n"
            "**AND उपदेशे CARRIES DOWN FROM 6.1.45.** That is what "
            "makes वर्ढा a counter-example: वृहू is उदात्त where the "
            "धातुपाठ taught it, whatever it looks like here"),
    Change(
        "6.1.60", does="nipātana", of=("śiras",), adesa="śīrṣan",
        chandasi=True, nipatana=True,
        keeps_out="शिरः, in ordinary speech, where the other word is "
                  "the only one",
        why="शीर्षंश्छन्दसि — in the Vedic corpus **शीर्षन्** is laid "
            "down as a word of its own, meaning what शिरस् means: "
            "**शीर्ष्णा हि तत्र सोमं क्रीतं हरन्ति; यत्ते शीर्ष्णो "
            "दौर्भाग्यम्**.\\n\\n"
            "**AND THE VṚTTI REFUSES TO CALL IT A SUBSTITUTE, WITH "
            "AN ARGUMENT.** **शीर्षन्निति शब्दान्तरं शिरःशब्देन "
            "समानार्थं छन्दसि विषये निपात्यते, न पुनरयमादेशः "
            "शिरःशब्दस्य, सोऽपि हि छन्दसि प्रयुज्यत एव** — शिरस् is "
            "used in the corpus TOO, so neither word can be standing "
            "in for the other. Both are simply there. The next rule "
            "is an आदेश and this one is not, and the difference is "
            "settled by what the corpus contains"),
    Change(
        "6.1.61", does="ādeśa", of=("śiras",), before="ya-taddhita",
        adesa="śīrṣan",
        keeps_out="शिरस्यति — the य there is क्यच् and no taddhita",
        why="ये च तद्धिते — before a taddhita affix beginning with "
            "य्, शिरस् is replaced by शीर्षन्: **शीर्षण्यः स्वरः**, "
            "with 4.3.55's यत् and 6.4.168's प्रकृतिभाव keeping the "
            "अन् standing.\\n\\n"
            "**AND THE RULE NAMES NO BASE, SO THE BASE IS ARGUED "
            "IN.** **आदेशोऽयमिष्यते। स कथम्? तद्धित इति हि परं "
            "निमित्तमुपादीयते, स तदनुरूपां प्रकृतिं शिरःशब्दम् "
            "आक्षिपति** — only what FOLLOWS is stated, and what "
            "follows draws in the base it fits. A substitution "
            "whose स्थानिन् is inferred rather than named, one rule "
            "after a निपातन whose vṛtti argued that nothing was "
            "being substituted at all.\\n\\n"
            "**AND A SUPPLEMENT MAKES IT A CHOICE IN ONE SENSE.** "
            "**वा केशेषु** — **शीर्षण्याः केशाः** beside "
            "**शिरस्याः केशाः**"),
    Change(
        "6.1.62", does="ādeśa", of=("śiras",), before="ac-taddhita",
        adesa="śīrṣa",
        why="अचि शीर्षः — before a taddhita beginning with a vowel "
            "the substitute is शीर्ष, without the न्: "
            "**हास्तिशीर्षिः, स्थौलशीर्षम्**.\\n\\n"
            "**AND THE MISSING न् IS THE WHOLE POINT.** "
            "**शीर्षन्भावे हि अन् इति प्रकृतिभावः स्यात्** — with "
            "शीर्षन् here, 6.4.167 would hold the अन् in place and "
            "the forms would come out wrong. The two rules give two "
            "shapes of one word because two later rules treat them "
            "differently.\\n\\n"
            "**AND THE FEMININE OF हास्तिशीर्षि IS A PROBLEM THE "
            "VṚTTI LEAVES HALF OPEN.** ष्यङ् begins with य्, so "
            "6.1.61 would turn the शीर्ष back into शीर्षन् and give "
            "**हास्तिशीर्षण्या**, which is not wanted. "
            "**कर्तव्योऽत्र यत्नः** — an effort has to be made "
            "here — and the way out offered is that the इ of the "
            "इञ् is dropped by 6.4.148 and its स्थानिवद्भाव stands "
            "between the शीर्ष and the य्, so the earlier rule "
            "cannot reach"),
    Change(
        "6.1.63", does="ādeśa", of=tuple(PADADI) + tuple(PADADI_VARTIKA),
        before="śas-prabhṛti", by_mapping=True,
        keeps_out="पादौ ते प्रतिपीड्यौ, नासिके ते कृशे — the strong "
                  "endings, where the full stems stand",
        why="पद्दन्नोमास्हृन्निश्असन्यूषन्दोषन्यकञ्शकन्नुदन्नासञ् "
            "छस्प्रभृतिषु — thirteen stems and thirteen substitutes, "
            "paired off यथासंख्यम् before शस् and the endings after "
            "it. **निपदश्चतुरो जहि; या दतो धावते; सूकरस्त्वा "
            "खनन्नसा; हृदा पूतं मनसा जातवेदो; यूष्ण आसेचनानि; उद्नो "
            "दिव्यस्य; आसनि किं लभे मधूनि**.\\n\\n"
            "**AND THE VṚTTI REPORTS A DISAGREEMENT WITHOUT SETTLING "
            "IT.** **केचिदत्र छन्दसीत्यनुवर्तयन्ति। अपरे पुनर् "
            "अविशेषेणेच्छन्ति** — some carry छन्दसि down from 6.1.60 "
            "and confine the rule to the corpus; others want it "
            "everywhere, and quote a verse of ordinary Sanskrit for "
            "it: **व्यायामक्षुण्णगात्रस्य पद्भ्यामुद्वर्तितस्य च**. "
            "And a third party carries अन्यतरस्याम् down from 6.1.59 "
            "instead, **तेन पादादयोऽपि प्रयुज्यन्ते**, so that both "
            "shapes stand.\\n\\n"
            "**AND प्रभृति IS READ AS A KIND, NOT AS A LIST.** "
            "**शस्प्रभृतिष्विति प्रकारार्थे प्रभृतिशब्दः** — which "
            "is how **शला दोषणी** is reached, where the ending is "
            "not one of the run at all.\\n\\n"
            "**AND THREE SUPPLEMENTS ADD THREE MORE PAIRS.** "
            "**पदादिषु मांस्पृत्स्नूनामुपसंख्यानम्** — "
            "**मांस्पचन्याः, पृत्सु मर्त्यम्, अधि स्नुषु**. A fourth "
            "confines the नस् of नासिका to यत्, तस् and क्षुद्र — "
            "**नस्यम्, नस्तः, नःक्षुद्रः** — and a fifth keeps it "
            "off **नासिक्यो वर्णः, नासिक्यं नगरम्**"),
    Change(
        "6.1.66", does="lopa", before="val", drops="v-or-y",
        keeps_out="ऊय्यते, क्नूय्यते — a य् follows, and य् is not "
                  "in वल्; वृश्चति — व्रश्च् is taught with its व्",
        why="लोपो व्योर्वलि — a व् or य् is dropped before a "
            "consonant other than य्, and **धातोः** has lapsed: "
            "**धातोरिति प्रकृतं यत् तद् धात्वादेरिति पुनर्धातुग्रहणाद् "
            "निवृत्तम्। तेन धातोरधातोश्च**. So the rule reaches a "
            "root and a non-root alike — **दिदिवान्, ऊतम्, क्नूतम्; "
            "गौधेरः; पचेरन्, यजेरन्; जीरदानुः**.\\n\\n"
            "**AND THE WORD लोप STANDS FIRST TO FIX AN ORDER.** "
            "**पूर्वं लोपग्रहणं किम्? वेरपृक्तलोपात् पूर्वं वलि लोपो "
            "यथा स्यात्** — this removal has to happen before "
            "6.1.67's, or कण्डू and लोलू are not reached: "
            "**कण्डूयतेः क्विप् — कण्डूः; लोलूयतेः — लोलूः**. Where "
            "a word stands in a rule, and not only what it "
            "says.\\n\\n"
            "**AND ONE ROOT IS PROTECTED BY THE WAY IT IS TAUGHT.** "
            "**व्रश्चादीनामुपदेशसामर्थ्याद् वलि लोपो न भवति** — had "
            "the व् been meant to go, the root would have been "
            "taught as रश्च्. And that argument has to be made "
            "because the removal is अन्तरङ्ग where the संप्रसारण "
            "and the हलादिशेष that give वृश्चति and वव्रश्च are "
            "बहिरङ्ग"),
    Change(
        "6.1.67", does="lopa", before="apṛkta", drops="vi",
        keeps_out="दर्विः, जागृविः — the affix there is विन् and is "
                  "more than one sound",
        why="वेरपृक्तस्य — the affix वि, reduced to a single sound, "
            "is dropped. **वेरिति क्विबादयो विशेषाननुबन्धानुत्सृज्य "
            "सामान्येन गृह्यन्ते** — क्विप्, क्विन् and ण्वि are all "
            "meant, their markers set aside: **ब्रह्महा, भ्रूणहा; "
            "घृतस्पृक्, तैलस्पृक्; अर्धभाक्, पादभाक्, "
            "तुरीयभाक्**.\\n\\n"
            "**AND AN AFFIX THAT VANISHES STILL DOES ITS WORK.** By "
            "1.1.62 the removal leaves the mark of the affix behind, "
            "which is the whole reason these affixes are given: a "
            "root cannot become a nominal stem except through one"),
    Change(
        "6.1.68", does="lopa", before="su-ti-si",
        after=("hal", "ṅī", "āp"), drops="apṛkta-hal",
        keeps_out="ग्रामणीः, सेनानीः — no हल्, ङी or आप् before it; "
                  "निष्कौशाम्बिः, अतिखट्वः — the vowel is not long; "
                  "भिनत्ति — the ending is more than one sound",
        why="हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल् — after a "
            "consonant, or a long ङी or आप्, the single consonant "
            "left of सु, ति or सि is dropped: **राजा, तक्षा; "
            "कुमारी, गौरी; खट्वा; अबिभर्भवान्; अभिनोऽत्र**.\\n\\n"
            "**AND सि IS THE ENDING AND NOT THE AORIST MARKER.** "
            "**तिपा सहचरितस्य सिशब्दस्य ग्रहणात् सिचो ग्रहणं "
            "नास्ति** — it keeps company with ति, and that decides "
            "which सि is meant. अभैत्सीत् keeps its स्.\\n\\n"
            "**AND THE VṚTTI ARGUES IN VERSE WHY THE RULE IS STATED "
            "AT ALL.** 8.2.23's संयोगान्तलोप would seem to do the "
            "work. Four forms say otherwise, and the vṛtti sets them "
            "in a śloka: **संयोगान्तस्य लोपे हि नलोपादिर्न सिध्यति। "
            "रात् तु ते नैव लोपः स्याद् धलस्तस्माद् विधीयते॥** — "
            "8.2.23 is असिद्ध, so राजा would never lose its न्; "
            "उखास्रत् is not पदान्त, so the द् would not be reached; "
            "अभिनोऽत्र needs a रु for 6.1.113 to work on; and "
            "8.2.24's रात् सस्य would confine the loss to a स्, "
            "leaving अबिभर्भवान् out"),
    Change(
        "6.1.69", does="lopa", before="sambuddhi", after=("eṅ", "hrasva"),
        drops="hal",
        keeps_out="हे कतरत् — the substitute is अद्ड्, whose डित् "
                  "takes the अ away, so nothing short stands before "
                  "the ending",
        why="एङ् ह्रस्वात् सम्बुद्धेः — in the vocative singular the "
            "consonant of the ending is dropped after ए or ओ and "
            "after a short vowel: **हे अग्ने, हे वायो; हे देवदत्त, "
            "हे नदि, हे वधु, हे कुण्ड**.\\n\\n"
            "**AND अपृक्तम् DOES NOT CARRY HERE — PROVED BY THE RULE "
            "BEFORE SAYING IT TWICE.** **अपृक्तमिति नाधिक्रियते। तथा "
            "च पूर्वसूत्रे पुनरपृक्तग्रहणं कृतम्** — 6.1.67 had "
            "already supplied the word and 6.1.68 states it again, "
            "and that redundancy is the evidence that it stops "
            "there. The inverse of the idle-word argument: a word "
            "repeated EARLIER shows it is absent LATER.\\n\\n"
            "**AND हे कुण्ड IS WHY IT MATTERS.** The ending there is "
            "7.1.24's अम्, which is two sounds and no अपृक्त. Only "
            "the म् is taken, the अ having merged with the stem's by "
            "6.1.107. Read अपृक्तम् into this rule and हे कुण्ड is "
            "unreachable.\\n\\n"
            "**AND एङ् IS SAID BECAUSE THE GUṆA WINS FIRST.** "
            "**एङ्ग्रहणं क्रियते संबुद्धिगुणबलीयस्त्वात्** — "
            "7.3.108 has already made अग्नि into अग्ने by the time "
            "this rule looks, so a rule speaking only of short "
            "vowels would find none"),
    Change(
        "6.1.70", does="lopa", before="śi", drops="śi",
        chandasi=True, bahulam=True,
        keeps_out="यानि क्षेत्राणि, in the same corpus and with the "
                  "शि standing",
        why="शेश्छन्दसि बहुलम् — in the Vedic corpus the शि of the "
            "neuter plural is dropped variously: **या क्षेत्रा, या "
            "वना** beside **यानि क्षेत्राणि, यानि वनानि**. Both "
            "shapes are found in the corpus, which is what बहुलम् "
            "records and what an option would not"),
    Change(
        "6.1.71", does="āgama", before="pit-kṛt", after=("hrasva",),
        gives="tuk",
        keeps_out="आलूय, ग्रामणीः — the vowel is not short; कृतम्, "
                  "हृतम् — the affix is not पित्; पटुतरः, पटुतमः — "
                  "तरप् and तमप् are taddhitas and no कृत्",
        why="ह्रस्वस्य पिति कृति तुक् — a root ending in a short "
            "vowel takes the augment तुक् before a कृत् affix marked "
            "प्: **अग्निचित्, सोमसुत्; प्रकृत्य, प्रहृत्य, "
            "उपस्तुत्य**.\\n\\n"
            "**AND A SHORTENING MADE ELSEWHERE DOES NOT COUNT AS "
            "SHORT.** In **ग्रामणि ब्राह्मणकुलम्** the vowel has "
            "been shortened, and still there is no तुक्: "
            "**ह्रस्वस्य बहिरङ्गस्य असिद्धत्वात् तुग् न भवति** — "
            "what is बहिरङ्ग counts as not having happened when "
            "something अन्तरङ्ग is to take effect. The same maxim "
            "6.1.66 had to argue against, used here the other way"),
)


@dataclass(frozen=True)
class Operation:
    """What the resolver answers with."""

    does: str
    sutra: str
    why: str
    #: What is added, where the rule adds.
    gives: str = ""
    #: What stands in place of what, where the rule substitutes.
    adesa: str = ""
    #: What is taken out, where the rule removes.
    drops: str = ""
    optional: bool = False
    chandasi: bool = False
    bahulam: bool = False
    nipatana: bool = False
    #: The rule this one displaces, with THAT rule's number.
    blocked_by: Tuple[str, ...] = ()


def _reaches(row: Change, stem: str, before: str, after: str,
             upadha: str, accent: str, chandasi: bool) -> bool:
    if row.chandasi and not chandasi:
        return False
    if row.of and stem not in row.of:
        return False
    if row.before and before != row.before:
        return False
    if row.after and after not in row.after:
        return False
    if row.upadha and upadha != row.upadha:
        return False
    if row.accent and accent != row.accent:
        return False
    return True


def _supplies(row: Change, wants: str) -> bool:
    return not wants or wants == row.does


def _how_specific(row: Change) -> int:
    """
    A named stem beats a condition on the shape of what surrounds it.

    The accent counts above the affix because 6.1.58 and 6.1.59 share
    their affix condition exactly and are told apart by nothing else:
    the first names two roots, the second names an accent and a
    penult and no root at all.
    """
    return (
        8 * bool(row.of)
        + 4 * bool(row.upadha)
        + 4 * bool(row.accent)
        + 3 * bool(row.before)
        + 2 * bool(row.after)
    )


def operates(stem: str = "", *, before: str = "", after: str = "",
             upadha: str = "", accent: str = "", chandasi: bool = False,
             wants: str = "") -> Operation:
    """
    6.1.58–71 — what is put in, put in place, or taken out.

    `wants` filters by the KIND of operation — āgama, ādeśa, lopa,
    nipātana — which is worth having here because the section mixes
    all four and a question about one is not answered by another.

    Nothing supplies by default: this stretch has no heading of its
    own, the आकार of 6.1.45 having stopped at 6.1.57.
    """
    matched = [
        row for row in CHANGE_TABLE
        if _reaches(row, stem, before, after, upadha, accent, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Operation(
            "", "", "No rule of 6.1.58–71 is reached. The stretch "
                    "has no heading of its own — 6.1.45's आकार "
                    "stopped at 6.1.57 — so nothing answers by "
                    "default")
    row = max(matched, key=_how_specific)
    adesa = stands_for(stem) if row.by_mapping else row.adesa
    return Operation(
        row.does, row.sutra, row.why, gives=row.gives,
        adesa=adesa, drops=row.drops, optional=row.optional,
        chandasi=row.chandasi, bahulam=row.bahulam,
        nipatana=row.nipatana, blocked_by=row.blocks)


def stands_for(stem: str) -> str:
    """
    6.1.63's substitute for one stem, or the empty string.

    The pairing is यथासंख्यम् — thirteen names and thirteen
    substitutes read off against each other in order — so the table
    is a mapping and not two lists, and a stem cannot silently lose
    its partner.
    """
    return PADADI.get(stem, PADADI_VARTIKA.get(stem, ""))


def provisions_for(sutra_id: str) -> Tuple[Change, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in CHANGE_TABLE if row.sutra == sutra_id)
