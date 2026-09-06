# -*- coding: utf-8 -*-
"""
६.२.६४–११० — आदिरुदात्तः and अन्तः, and the first member is now GIVEN
an accent rather than left with one.

6.2.1–63 let the first member KEEP whatever accent it had. From
6.2.64 the pāda stops preserving and starts placing: **आदिरुदात्त
इत्येतदधिकृतम्। इत उत्तरं यद् वक्ष्यामस्तत्र पूर्वपदस्यादिरुदात्तो
भवति** — its FIRST syllable takes an उदात्त, whatever it had before.
And at 6.2.92 the placement moves: **अन्त इत्यधिकृतम्... पूर्वपदस्यान्त
उदात्तो भवति** — the LAST syllable instead.

**AND THE TWO WORDS OF ONE HEADING STOP IN DIFFERENT PLACES.**
6.2.64's own vṛtti says so: **आदिरिति प्राग् अन्ताधिकारात्। उदात्त
इति प्रकृत्या भगालम् इति यावत्** — आदिः governs to 6.2.91, and उदात्तः
runs on past this module's end to 6.2.137. The same shape 6.2.1 had,
where प्रकृत्या stopped at 6.2.63 and पूर्वपदम् ran to 6.2.110.

**AND A THIRD PLACEMENT APPEARS ONCE.** 6.2.83 अन्त्यात् पूर्वं
बह्वचः — the syllable BEFORE the last of a first member of more than
two vowels. Neither the first nor the last, and stated for one
following word alone.

**AND A FOURTH HEADING OPENS INSIDE THIS ONE.** 6.2.106's vṛtti:
**बहुव्रीहावित्येतद् अधिक्रियते प्राग् अव्ययीभावसंज्ञानात्** — from
6.2.106 to 6.2.120 every rule is read as being about a बहुव्रीहि, and
the bound is 6.2.121's word अव्ययीभावे.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule places the
accent and where in the first member. It does not count syllables:
6.2.83's *before the last* and 6.2.90's *two or three vowels* are
conditions the query carries, not ones the code works out.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where आदिः governs — from 6.2.64 to 6.2.91, on the vṛtti's own
#: bound: **आदिरिति प्राग् अन्ताधिकारात्**.
ADI_RUN: Tuple[str, str] = ("6.2.64", "6.2.91")

#: And where अन्तः does, from 6.2.92: **प्राग् उत्तरपदादिः
#: इत्येतस्माद् अयम् अधिकारो वेदितव्यः**.
ANTA_RUN: Tuple[str, str] = ("6.2.92", "6.2.110")

#: And the word उदात्तः, which outlives both: **उदात्त इति प्रकृत्या
#: भगालम् इति यावत्** — to 6.2.137, past the end of this module.
UDATTA_RUN: Tuple[str, str] = ("6.2.64", "6.2.137")

#: And a heading of a different kind opening inside them. 6.2.106:
#: **बहुव्रीहावित्येतद् अधिक्रियते प्राग् अव्ययीभावसंज्ञानात्**.
BAHUVRIHI_RUN: Tuple[str, str] = ("6.2.106", "6.2.120")


@dataclass(frozen=True)
class Placed:
    """One rule of 6.2.64–110: where in the first member it goes."""

    sutra: str
    #: ādi, anta, or antyāt-pūrva — the syllable before the last.
    where: str = ""
    #: The first members the rule names.
    of: Tuple[str, ...] = ()
    #: A named class of first member instead.
    gana: str = ""
    #: The words that must FOLLOW.
    uttarapada: Tuple[str, ...] = ()
    #: A named class of second member instead — घोषादि, गोत्र,
    #: अन्तेवासिन्, पूग.
    uttarapada_gana: str = ""
    #: What the second member must END IN — अक, अण्, णिनि.
    uttarapada_affix: str = ""
    samasa: str = ""
    case: str = ""
    result: str = ""
    #: What the rule keeps out of its own class.
    excludes: Tuple[str, ...] = ()
    #: True where the word must be a NAME.
    samjna: bool = False
    refuses: bool = False
    optional: bool = False
    heading: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


PLACED_TABLE: Tuple[Placed, ...] = (
    Placed(
        "6.2.64", where="ādi", heading=True,
        why="आदिरुदात्तः — **आदिरुदात्त इत्येतदधिकृतम्। इत उत्तरं यद् "
            "वक्ष्यामस्तत्र पूर्वपदस्यादिरुदात्तो भवतीत्येवं तद् "
            "वेदितव्यम्** — from here the first member's FIRST "
            "SYLLABLE takes the accent, whatever accent it had. "
            "**स्तूपेशाणः, मुकुटेकार्षापणम्, याज्ञिकाश्वः, "
            "वैयाकरणहस्ती, दृषदिमाषकः**.\\n\\n"
            "**AND THE HEADING'S TWO WORDS STOP IN DIFFERENT "
            "PLACES.** **आदिरिति प्राग् अन्ताधिकारात्। उदात्त इति "
            "प्रकृत्या भगालम् इति यावत्** — आदिः to 6.2.91, where "
            "अन्तः takes over; उदात्तः all the way to 6.2.137. The "
            "same shape 6.2.1 had, and the second time the pāda "
            "splits one sūtra's reach in two"),
    Placed(
        "6.2.65", where="ādi", case="saptamī", result="dharmya",
        excludes=("haraṇa",),
        keeps_out="स्तम्बेरमः — no customary due meant",
        why="सप्तमीहारिणौ धर्म्येऽहरणे — a locative first member, or "
            "one naming the TAKER, before a word for what is due by "
            "custom, and not before हरण: **स्तूपेशाणः, "
            "मुकुटेकार्षापणम्, हलेद्विपदिका, दृषदिमाषकः; "
            "याज्ञिकाश्वः, वैयाकरणहस्ती, मातुलाश्वः**.\\n\\n"
            "**AND BOTH SENSE-WORDS ARE GLOSSED BEFORE USE.** "
            "**हारीति देयं यः स्वीकरोति सोऽभिधीयते** — the one who "
            "takes what is to be given; **धर्म्यमित्याचारनियतं देयम् "
            "उच्यते** — what custom has settled shall be given. And "
            "the custom itself is named: **स्तूपादिषु शाणादि "
            "दातव्यम्, याज्ञिकादीनाम् अश्वादि**"),
    Placed(
        "6.2.66", where="ādi", result="yukta",
        why="युक्ते च — where the compound names one SET TO a task, "
            "which the vṛtti glosses **युक्त इति समाहितः, कर्तव्ये "
            "तत्परो यः**: **गोबल्लवः, अश्वबल्लवः, गोमणिन्दः, "
            "गोसंख्यः**"),
    Placed(
        "6.2.67", where="ādi", uttarapada=("adhyakṣa",), optional=True,
        why="विभाषाध्यक्षे — before अध्यक्ष, optionally: "
            "**गवाध्यक्षः, अश्वाध्यक्षः**, each beside its "
            "end-accented form"),
    Placed(
        "6.2.68", where="ādi", of=("pāpa",), result="śilpin",
        optional=True,
        keeps_out="पापस्य नापितः — the genitive compound, which the "
                  "rule does not reach",
        why="पापं च शिल्पिनि — पाप before a craftsman-word, "
            "optionally: **पापनापितः, पापकुलालः**.\\n\\n"
            "**AND THE COMPOUND HAS TO BE THE ONE 2.1.54 MAKES BY "
            "NAME.** **पापाणके कुत्सितैः इति पापशब्दस्य प्रतिपदोक्तः "
            "समानाधिकरणसमास इति षष्ठीसमासे न भवति** — the "
            "appositional compound, not the genitive one"),
    Placed(
        "6.2.69", where="ādi", uttarapada_gana="gotra-antevāsin",
        result="kṣepa",
        why="गोत्रान्तेवासिमाणवब्राह्मणेषु क्षेपे — before a word for "
            "a lineage or a pupil, and before माणव or ब्राह्मण, "
            "where ABUSE is meant: **जङ्घावात्स्यः** — one who "
            "becomes a Vātsya by giving away his shanks; "
            "**भार्यासौश्रुतः, कुमारीदाक्षाः, कम्बलचारायणीयाः, "
            "ओदनपाणिनीयाः, भिक्षामाणवः**. Each names a man by what "
            "he took to get where he is"),
    Placed(
        "6.2.70", where="ādi", uttarapada=("maireya",),
        result="aṅga",
        keeps_out="परममैरेयः — not an ingredient; पुष्पासवः — not "
                  "मैरेय",
        why="अङ्गानि मैरेये — before मैरेय, where the first member "
            "names an INGREDIENT of it: **गुडमैरेयः, मधुमैरेयः** — "
            "the liquor made of molasses, the liquor made of honey"),
    Placed(
        "6.2.71", where="ādi", of=("bhaktākhyā",), result="tadartha",
        keeps_out="समाशशालयः — समाश names an act and not a thing; "
                  "भिक्षाप्रियः — a बहुव्रीहि, and end-accented",
        why="भक्ताख्यास्तदर्थेषु — a word for FOOD before a word for "
            "what holds it: **भिक्षाकंसः, श्राणाकंसः, भाजीकंसः**. "
            "**भक्तमन्नम्, तदाख्यास्तद्वाचिनः शब्दाः** — the vṛtti "
            "reads the compound of the sūtra out before using it"),
    Placed(
        "6.2.72", where="ādi",
        uttarapada=("go", "biḍāla", "siṃha", "saindhava"),
        result="upamāna",
        keeps_out="परमसिंहः — no likeness meant",
        why="गोबिडालसिंहसैन्धवेषूपमाने — before four words used as a "
            "LIKENESS: **धान्यगवः** — grain heaped in the shape of a "
            "cow; **भिक्षाबिडालः, तृणसिंहः, सक्तुसैन्धवः**. And the "
            "vṛtti leaves the likeness to be worked out case by "
            "case: **उपमानार्थोऽपि यथासंभवं यथाप्रसिद्धि च "
            "योजयितव्यः**"),
    Placed(
        "6.2.73", where="ādi", uttarapada_affix="aka",
        result="jīvikārtha",
        keeps_out="रमणीयकर्ता — the affix is not अक; इक्षुभक्षिकां मे "
                  "धारयसि — no livelihood meant",
        why="अके जीविकार्थे — before a stem in अक where the compound "
            "names a LIVELIHOOD: **दन्तलेखकः, नखलेखकः, "
            "अवस्करशोधकः** — men who live by scratching teeth, by "
            "trimming nails, by cleaning drains"),
    Placed(
        "6.2.74", where="ādi", uttarapada_affix="aka",
        result="krīḍā-prācām",
        keeps_out="जीवपुत्रप्रचायिका — a northern game; "
                  "पुष्पप्रचायिका — a turn taken, not a game",
        why="प्राचां क्रीडायाम् — before the same stem where an "
            "EASTERN game is named: **उद्दालकपुष्पभञ्जिका, "
            "वीरणपुष्पप्रचायिका, शालभञ्जिका**. A rule whose "
            "condition is where in the country the word is used"),
    Placed(
        "6.2.75", where="ādi", uttarapada_affix="aṇ", result="niyukta",
        keeps_out="काण्डलावः, शरलावः — no appointment meant",
        why="अणि नियुक्ते — before a stem in अण् where the compound "
            "names one APPOINTED to a charge: **छत्रधारः, तूणीरधारः, "
            "कमण्डलुग्राहः**.\\n\\n"
            "**AND नियुक्त IS NOT युक्त.** "
            "**नियुक्तोऽधिकृतः, स च कस्मिंश्चित् कर्तव्ये तत्परो न "
            "भवतीति नियुक्ते इत्यनेन न सिध्यति** — one put in charge "
            "is not thereby one set to a task, so 6.2.66 does not "
            "cover it"),
    Placed(
        "6.2.76", where="ādi", uttarapada_affix="aṇ", result="śilpin",
        excludes=("kṛñ",),
        keeps_out="कुम्भकारः, अयस्कारः — the affix is on कृञ्, which "
                  "the rule excepts",
        why="शिल्पिनि चाकृञः — before a stem in अण् naming a "
            "CRAFTSMAN, so long as the affix is not on कृञ्: "
            "**तन्तुवायः, तुन्नवायः, वालवायः**"),
    Placed(
        "6.2.77", where="ādi", uttarapada_affix="aṇ", samjna=True,
        excludes=("kṛñ",),
        keeps_out="रथकारो नाम ब्राह्मणः — a name, but the affix is on "
                  "कृञ्",
        why="संज्ञायां च — and where the compound is a NAME: "
            "**तन्तुवायो नाम कीटः, वालवायो नाम पर्वतः**. The कृञ् "
            "exception carries down"),
    Placed(
        "6.2.78", where="ādi", of=("go", "tanti", "yava"),
        uttarapada=("pāla",),
        keeps_out="वत्सपालः — not one of the three; गोरक्षः — not "
                  "पाल",
        why="गोतन्तियवं पाले — three first members before पाल: "
            "**गोपालः, तन्तिपालः, यवपालः**. "
            "**अनियुक्तार्थ आरम्भः** — the rule exists for the "
            "cowherd who was not APPOINTED one, whom 6.2.75 could "
            "not reach"),
    Placed(
        "6.2.79", where="ādi", uttarapada_affix="ṇini",
        why="णिनि — before a stem in णिनि: **पुष्पहारी, फलहारी, "
            "पर्णहारी**. The shortest sūtra of the section, and the "
            "widest"),
    Placed(
        "6.2.80", where="ādi", of=("upamāna",),
        uttarapada_affix="ṇini", result="śabdārtha-prakṛti",
        keeps_out="वृकवञ्ची, वृकप्रेक्षी — the root does not name a "
                  "sound; गर्दभोच्चारी, कोकिलाभिव्याहारी — a preverb "
                  "stands there and the root alone does not give the "
                  "sense",
        why="उपमानं शब्दार्थप्रकृतावेव — where the first member is a "
            "LIKENESS, the rule before holds only if the root names "
            "a SOUND and does so of itself: **उष्ट्रक्रोशी, "
            "ध्वाङ्क्षरावी, खरनादी**.\\n\\n"
            "**AND THE एवकार RESTRICTS THE LIKENESS AND NOT THE "
            "ROOT.** **एवकारकरणम् उपमानावधारणार्थम्। "
            "शब्दार्थप्रकृतौ त्वनुपमानम् उपमानं चाद्युदात्तं भवति** "
            "— where the root does name a sound, likeness or not, "
            "the accent comes: **सिंहविनर्दी, पुष्कलजल्पी**"),
    Placed(
        "6.2.81", where="ādi", gana="yuktārohyādi",
        keeps_out="वृक्षारोही, युक्ताध्यायी",
        why="युक्तारोह्यादयश्च — a list of whole compounds: "
            "**युक्तारोही, आगतरोही, आगतयोधी, आगतवञ्ची; क्षीरहोता, "
            "भगिनीभर्ता; ग्रामगोधुक्, अश्वत्रिरात्रः, "
            "एकशितिपात्**.\\n\\n"
            "**AND WHAT THE LIST IS FOR IS DISPUTED.** "
            "**एते णिन्नन्ता णिनि इत्यस्यैवोदाहरणार्थं पठ्यन्ते। "
            "पूर्वोत्तरपदनियमार्था इति केचित्** — some take the "
            "णिनि-final members to be mere examples of 6.2.79 and "
            "the list to be confining which first and second members "
            "that rule reaches"),
    Placed(
        "6.2.82", where="ādi", uttarapada=("ja",),
        of=("kāśa", "tuṣa", "bhrāṣṭra", "vaṭa"),
        why="दीर्घकाशतुषभ्राष्ट्रवटं जे — before ज, for a first "
            "member ending in a long vowel and for four named words: "
            "**कुटीजः, शमीजः; काशजः, तुषजः, भ्राष्ट्रजः, वटजः**"),
    Placed(
        "6.2.83", where="antyāt-pūrva", uttarapada=("ja",),
        of=("bahvac",), blocks=("6.2.82",),
        keeps_out="दग्धजानि तृणानि — the first member has too few "
                  "vowels",
        why="अन्त्यात् पूर्वं बह्वचः — and where the first member has "
            "MANY VOWELS, it is the syllable before the last that "
            "takes the accent: **उपसरजः, मन्दुरजः, आमलकीजः, "
            "वडवाजः**. Neither the first syllable nor the last — the "
            "only rule of the pāda so far to place an accent "
            "anywhere else"),
    Placed(
        "6.2.84", where="ādi", uttarapada=("grāma",),
        excludes=("nivasat",),
        keeps_out="दाक्षिग्रामः, माहकिग्रामः — the first member names "
                  "who LIVES there",
        why="ग्रामेऽनिवसन्तः — before ग्राम, where the first member "
            "does NOT name who lives there: **मल्लग्रामः, "
            "वणिग्ग्रामः** — with ग्राम meaning a body of men; "
            "**देवग्रामः** — the village a god owns"),
    Placed(
        "6.2.85", where="ādi", uttarapada_gana="ghoṣādi",
        why="घोषादिषु च — before a list of second members: "
            "**दाक्षिघोषः, दाक्षिकटः, दाक्षिह्रदः, दाक्षिबदरी, "
            "दाक्ष्यश्वत्थः, आश्रममुनिः**.\\n\\n"
            "**AND WHETHER THE RULE BEFORE'S CONDITION CARRIES IS "
            "DISPUTED.** **यान्यत्र निवासनामधेयानि तेषु "
            "निवसद्वाचीन्यपि पूर्वपदान्याद्युदात्तानि भवन्ति। "
            "अनिवसन्त इति नानुवर्तयन्ति केचित्। अपरे पुनरनुवर्तयन्ति** "
            "— some let the words for dwellings take the accent even "
            "where the first member names who lives there, and some "
            "do not"),
    Placed(
        "6.2.86", where="ādi", gana="chātryādi", uttarapada=("śālā",),
        blocks=("6.2.123",),
        why="छात्र्यादयः शालायाम् — a list of first members before "
            "शाला: **छात्रिशाला, ऐलिशाला, भाण्डिशाला**.\\n\\n"
            "**AND IT WINS AGAINST A LATER RULE BY BEING STATED "
            "EARLIER.** **यदा शालान्तस्तत्पुरुषो नपुंसकलिङ्गो भवति, "
            "तदापि तत्पुरुषे शालायां नपुंसके इत्येतस्मात् "
            "पूर्वविप्रतिषेधेन पूर्वपदमाद्युदात्तं भवति** — 6.2.123 "
            "would place the accent otherwise, and the earlier rule "
            "takes it: **छात्रिशालम्**"),
    Placed(
        "6.2.87", where="ādi", uttarapada=("prastha",),
        excludes=("vṛddha", "karkyādi"),
        keeps_out="दाक्षिप्रस्थः — a वृद्ध first member; "
                  "कर्कीप्रस्थः, मघीप्रस्थः — of the कर्क्यादि list",
        why="प्रस्थेऽवृद्धमकर्क्यादीनाम् — before प्रस्थ, for a first "
            "member that is not वृद्ध and not on the कर्क्यादि list: "
            "**इन्द्रप्रस्थः, कुण्डप्रस्थः, ह्रदप्रस्थः, "
            "सुवर्णप्रस्थः**"),
    Placed(
        "6.2.88", where="ādi", gana="mālādi", uttarapada=("prastha",),
        blocks=("6.2.87",),
        why="मालादीनां च — and a list of first members before प्रस्थ: "
            "**मालाप्रस्थः, शालाप्रस्थः**. **वृद्धार्थ आरम्भः** — "
            "the rule exists for exactly the वृद्ध words the one "
            "before it excepted, and two of the list are वृद्ध only "
            "by 1.1.75's एङ् प्राचां देशे"),
    Placed(
        "6.2.89", where="ādi", uttarapada=("nagara",),
        excludes=("mahat", "nava", "udīcām"),
        keeps_out="महानगरम्, नवनगरम् — the two excepted words; "
                  "नदीनगरम्, कान्तीनगरम् — northern names",
        why="अमहन्नवं नगरेऽनुदीचाम् — before नगर, for a first member "
            "that is neither महत् nor नव, and not a northern name: "
            "**सुह्मनगरम्, पुण्ड्रनगरम्**. Three conditions and a "
            "counter-example for each"),
    Placed(
        "6.2.90", where="ādi", uttarapada=("arma",),
        excludes=("mahat", "nava"),
        keeps_out="बृहदर्मम् — the first member does not end in अ; "
                  "कपिञ्जलार्मम् — too many vowels; महार्मम्, "
                  "नवार्मम् — the two words carried down",
        why="अर्मे चावर्णं द्व्यच् त्र्यच् — before अर्म, for a first "
            "member ending in अ or आ and having two or three vowels: "
            "**दत्तार्मम्, गुप्तार्मम्, कुक्कुटार्मम्, "
            "वायसार्मम्**. And **अमहन्नवमित्येव** — the two words "
            "the rule before excepted carry down"),
    Placed(
        "6.2.91", refuses=True, uttarapada=("arma",),
        of=("bhūta", "adhika", "saṃjīva", "madra", "aśman", "kajjala"),
        blocks=("6.2.90",),
        why="न भूताधिकसंजीवमद्राश्मकज्जलम् — six first members are "
            "refused what the rule before gives: **भूतार्मम्, "
            "अधिकार्मम्, संजीवार्मम्, मद्रार्मम्, अश्मार्मम्, "
            "कज्जलार्मम्**, and **समासान्तोदात्तत्वमेवात्र भवति** — "
            "6.1.223 takes them back.\\n\\n"
            "**AND TWO OF THE SIX ARE NAMED FOR THE COMPOUND OF "
            "THEM.** **मद्राश्मग्रहणं संघातविगृहीतार्थम्** — for "
            "**मद्राश्मार्मम्** as well as for each apart. And a "
            "supplement adds a Vedic list to the आदि section as a "
            "whole: **आद्युदात्तप्रकरणे दिवोदासादीनां "
            "छन्दस्युपसंख्यानम्** — **दिवोदासं वध्र्यश्वाय "
            "दाशुषे**"),
    Placed(
        "6.2.92", where="anta", heading=True, blocks=("6.2.64",),
        why="अन्तः — **अन्त इत्यधिकृतम्। इत उत्तरं यद् "
            "वक्ष्यामस्तत्र पूर्वपदस्यान्त उदात्तो भवति** — from "
            "here it is the LAST syllable of the first member, where "
            "6.2.64 gave the first. The placement moves and the "
            "scope does not: पूर्वपद still governs.\\n\\n"
            "**AND THE RUN IS BOUNDED BY THE NEXT SCOPE-WORD.** "
            "**प्राग् उत्तरपदादिः इत्येतस्माद् अयम् अधिकारो "
            "वेदितव्यः** — to 6.2.110, where 6.2.111 takes the "
            "second member and the rest of the pāda"),
    Placed(
        "6.2.93", where="anta", of=("sarva",), result="guṇakārtsnya",
        keeps_out="परमश्वेतः — the first member is not सर्व; "
                  "सर्वसौवर्णः — no QUALITY is meant; सर्वश्वेतः "
                  "meaning whitest of all — no WHOLENESS",
        why="सर्वं गुणकार्त्स्न्ये — सर्व where a QUALITY is meant "
            "IN FULL: **सर्वश्वेतः, सर्वकृष्णः, सर्वमहान्**. Three "
            "words of the rule and three counter-examples, and the "
            "third turns on a supplement that lets तर be dropped in "
            "the compound: **गुणात्तरेण समासस्तरलोपश्च वक्तव्यः**"),
    Placed(
        "6.2.94", where="anta", uttarapada=("giri", "nikāya"),
        samjna=True,
        keeps_out="परमगिरिः, ब्राह्मणनिकायः — not names",
        why="संज्ञायां गिरिनिकाययोः — before गिरि or निकाय where the "
            "compound is a NAME: **अञ्जनागिरिः, भञ्जनागिरिः; "
            "शापिण्डिनिकायः, मौण्डिनिकायः**"),
    Placed(
        "6.2.95", where="anta", uttarapada=("kumārī",), result="vayas",
        keeps_out="परमकुमारी — no age meant",
        why="कुमार्यां वयसि — before कुमारी where an AGE is meant: "
            "**वृद्धकुमारी, जरत्कुमारी**. And the vṛtti is careful "
            "about which sense of कुमारी is in play: "
            "**कुमारीशब्दः पुंसा सहासंप्रयोगमात्रं प्रवृत्तिनिमित्तम् "
            "उपादाय प्रयुक्तः** — the word used of a woman "
            "unmarried, whatever her years"),
    Placed(
        "6.2.96", where="anta", uttarapada=("udaka",),
        result="akevala",
        keeps_out="शीतोदकम्, उष्णोदकम् — water and nothing in it",
        why="उदकेऽकेवले — before उदक where the water is MIXED, "
            "**अकेवलं मिश्रम्**: **गुडोदकम्, तिलोदकम्**. And the "
            "single substitute is then उदात्त or स्वरित by 8.2.6"),
    Placed(
        "6.2.97", where="anta", samasa="dvigu", result="kratu",
        keeps_out="अतिरात्रः — no द्विगु; बिल्वसप्तरात्रः — no "
                  "sacrifice named",
        why="द्विगौ क्रतौ — before a द्विगु naming a SACRIFICE: "
            "**गर्गत्रिरात्रः, चरकत्रिरात्रः, "
            "कुसुरविन्दसप्तरात्रः**"),
    Placed(
        "6.2.98", where="anta", uttarapada=("sabhā",),
        result="napuṃsaka",
        keeps_out="ब्राह्मणसेनम् — not सभा; राजसभा, ब्राह्मणसभा — not "
                  "neuter; रमणीयसभं ब्राह्मणकुलम् — neuter, but not "
                  "by the rule that makes सभा so",
        why="सभायां नपुंसके — before सभा where the compound is "
            "NEUTER: **गोपालसभम्, पशुपालसभम्, स्त्रीसभम्, "
            "दासीसभम्**. And the neuter meant is the one 2.4.23 "
            "gives सभा by name: "
            "**सभायां प्रतिपदोक्तमिह नपुंसकलिङ्गं गृह्यते**"),
    Placed(
        "6.2.99", where="anta", uttarapada=("pura",), result="prācām",
        keeps_out="शिवपुरम् — not an eastern name",
        why="पुरे प्राचाम् — before पुर in an EASTERN name: "
            "**ललाटपुरम्, काञ्चीपुरम्, शिवदत्तपुरम्, कार्णिपुरम्, "
            "नार्मपुरम्**. And the condition is on where the NAME "
            "belongs and not on where the city stands, which is why "
            "शिवपुरम् is left with the compound accent"),
    Placed(
        "6.2.100", where="anta", of=("ariṣṭa", "gauḍa"),
        uttarapada=("pura",),
        why="अरिष्टगौडपूर्वे च — and where अरिष्ट or गौड stands "
            "FIRST: **अरिष्टपुरम्, गौडपुरम्**. And पूर्वे is what "
            "lets a third word come between: "
            "**पूर्वग्रहणं किम्? इहापि यथा स्यात् — अरिष्टश्रितपुरम्, "
            "गौडभृत्यपुरम्**"),
    Placed(
        "6.2.101", refuses=True,
        of=("hāstina", "phalaka", "mārdeya"), uttarapada=("pura",),
        blocks=("6.2.99",),
        why="न हास्तिनफलकमार्देयाः — three first members are refused "
            "what 6.2.99 gives: **हास्तिनपुरम्, फलकपुरम्, "
            "मार्देयपुरम्**"),
    Placed(
        "6.2.102", where="anta",
        of=("kusūla", "kūpa", "kumbha", "śālā"), uttarapada=("bila",),
        keeps_out="सर्पबिलम् — not one of the four; कुसूलस्वामी — not "
                  "बिल",
        why="कुसूलकूपकुम्भशालं बिले — four first members before बिल: "
            "**कुसूलबिलम्, कूपबिलम्, कुम्भबिलम्, शालाबिलम्**"),
    Placed(
        "6.2.103", where="anta", of=("dikśabda",),
        uttarapada_gana="grāma-janapada-ākhyāna",
        why="दिक्शब्दा ग्रामजनपदाख्यानचानराटेषु — a direction-word "
            "before a village-name, a country-name, a title, or "
            "चानराट: **पूर्वेषुकामशमी; पूर्वपञ्चालाः; पूर्वाधिरामम्, "
            "पूर्वयायातम्; पूर्वचानराटम्**.\\n\\n"
            "**AND शब्द IS SAID TO REACH A DIRECTION-WORD USED OF "
            "TIME.** **शब्दग्रहणं कालवाचिनोऽपि दिक्शब्दस्य "
            "परिग्रहार्थम्** — पूर्व and अपर are directions by shape "
            "even where they mean earlier and later"),
    Placed(
        "6.2.104", where="anta", of=("dikśabda",),
        uttarapada_gana="ācāryopasarjana-antevāsin",
        keeps_out="पूर्वशिष्याः — the pupil is not named from a "
                  "teacher; पूर्वपाणिनीयं शास्त्रम् — the work, not "
                  "the pupils",
        why="आचार्योपसर्जनश्चान्तेवासिनि — and before a word for "
            "pupils named after their teacher: **पूर्वपाणिनीयाः, "
            "अपरपाणिनीयाः, पूर्वकाशकृत्स्नाः**"),
    Placed(
        "6.2.105", where="anta", of=("sarva", "dikśabda"),
        uttarapada=("vṛddha",),
        keeps_out="सर्वभासः, सर्वकारकः — the vṛddhi there is not the "
                  "one 7.3.10 heads",
        why="उत्तरपदवृद्धौ सर्वं च — before a second member that has "
            "taken the vṛddhi 7.3.10 heads, for सर्व and for a "
            "direction-word: **सर्वपाञ्चालकः, पूर्वपाञ्चालकः, "
            "उत्तरपाञ्चालकः**"),
    Placed(
        "6.2.106", where="anta", samasa="bahuvrīhi", of=("viśva",),
        samjna=True, heading=True,
        keeps_out="विश्वे च ते देवा विश्वदेवाः — a द्वन्द्व; विश्वे "
                  "देवा अस्य विश्वदेवः — a बहुव्रीहि but no name",
        why="बहुव्रीहौ विश्वं संज्ञायाम् — विश्व in a बहुव्रीहि that "
            "is a NAME: **विश्वदेवः, विश्वयशाः, विश्वमहान्**. "
            "**पूर्वपदप्रकृतिस्वरत्वेनाद्युदात्तत्वं प्राप्तम्** — "
            "6.2.1 would have kept its own accent, and this displaces "
            "that.\\n\\n"
            "**AND बहुव्रीहि BECOMES A HEADING HERE.** "
            "**बहुव्रीहावित्येतद् अधिक्रियते प्राग् "
            "अव्ययीभावसंज्ञानात्** — from 6.2.106 to 6.2.120 every "
            "rule is read as being about a बहुव्रीहि, bounded by "
            "6.2.121's word अव्ययीभावे. A fourth heading inside a "
            "pāda that already had three"),
    Placed(
        "6.2.107", where="anta", samasa="bahuvrīhi",
        uttarapada=("udara", "aśva", "iṣu"), samjna=True,
        why="उदराश्वेषुषु — before three words, in a बहुव्रीहि that "
            "is a name: **वृकोदरः, दामोदरः; हर्यश्वः, यौवनाश्वः; "
            "सुवर्णपुङ्खेषुः, महेषुः**"),
    Placed(
        "6.2.108", where="anta", samasa="bahuvrīhi",
        uttarapada=("udara", "aśva", "iṣu"), result="kṣepa",
        blocks=("6.2.172",),
        why="क्षेपे — and before the same three where ABUSE is meant, "
            "name or no name: **कुण्डोदरः, घटोदरः; कटुकाश्वः, "
            "स्पन्दिताश्वः; अनिघातेषुः, चलाचलेषुः**. And where a नञ् "
            "or a सु stands first, 6.2.172 wins **विप्रतिषेधेन**: "
            "**अनुदरः, सूदरः**"),
    Placed(
        "6.2.109", where="anta", samasa="bahuvrīhi", of=("nadī",),
        uttarapada=("bandhu",),
        keeps_out="ब्रह्मबन्धुः — the first member is no नदी; "
                  "गार्गीप्रियः — the second is not बन्धु",
        why="नदी बन्धुनि — a नदी-final first member before बन्धु, in "
            "a बहुव्रीहि: **गार्गीबन्धुः, वात्सीबन्धुः**. Both "
            "conditions are shown by what fails them: ब्रह्मबन्धुः "
            "has no नदी first member and keeps ब्रह्मन्'s own "
            "first-syllable accent, and गार्गीप्रियः has no बन्धु"),
    Placed(
        "6.2.110", where="anta", samasa="bahuvrīhi",
        uttarapada_affix="niṣṭhā-upasarga-pūrva", optional=True,
        keeps_out="प्रसेचकमुखः — not a निष्ठा; शुष्कमुखः — no preverb "
                  "before it",
        why="निष्ठोपसर्गपूर्वमन्यतरस्याम् — a निष्ठा first member "
            "with a preverb before it, in a बहुव्रीहि, optionally: "
            "**प्रधौतमुखः, प्रक्षालितपादः**, in three accentuations "
            "between them.\\n\\n"
            "**AND WHICH THE THIRD IS DEPENDS ON WHAT THE SECOND "
            "MEMBER NAMES.** **यदि मुखशब्दः स्वाङ्गवाची तदा पक्षे "
            "मुखं स्वाङ्गम् इत्येतद् भवति, न चेत् "
            "पूर्वपदप्रकृतिस्वरत्वेन गतिरनन्तरः इत्येतद् भवति** — a "
            "part of the body takes 6.2.167, anything else takes "
            "6.2.49"),
)


@dataclass(frozen=True)
class Accented:
    """What the resolver answers with."""

    where: str
    sutra: str
    why: str
    optional: bool = False
    #: Where a rule displaces or refuses another, that rule's number.
    blocked_by: Tuple[str, ...] = ()


def _reaches(row: Placed, purvapada: str, gana: str, uttarapada: str,
             uttarapada_gana: str, uttarapada_affix: str,
             samasa: str, case: str, result: str,
             samjna: bool) -> bool:
    if row.heading and not (row.of or row.uttarapada or row.samasa):
        # 6.2.64 and 6.2.92 state only where the accent goes. 6.2.106
        # is a heading AND a rule, so it stays in play.
        return False
    if row.samjna and not samjna:
        return False
    if row.of and purvapada not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.uttarapada and uttarapada not in row.uttarapada:
        return False
    if row.uttarapada_gana and uttarapada_gana != row.uttarapada_gana:
        return False
    if row.uttarapada_affix and uttarapada_affix != row.uttarapada_affix:
        return False
    if row.samasa and samasa != row.samasa:
        return False
    if row.case and case != row.case:
        return False
    if row.result and result != row.result:
        return False
    if row.excludes and (purvapada in row.excludes
                         or uttarapada in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Placed, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.where and not row.refuses


def _how_specific(row: Placed) -> int:
    """
    A refusal beats what it refuses, and a named first member beats a
    named second one here.

    That is the reverse of 6.2.1–63, and the section is built the
    other way round: there the second member was what almost every
    rule named, here it is often the first — सर्व, विश्व, नदी, a
    direction-word — and 6.2.100 and 6.2.101 both name a first member
    against the same second one.
    """
    return (
        10 * bool(row.refuses)
        + 8 * bool(row.of)
        + 7 * bool(row.result)
        + 6 * bool(row.uttarapada)
        + 5 * bool(row.uttarapada_affix)
        + 4 * bool(row.uttarapada_gana)
        + 4 * bool(row.case)
        + 3 * bool(row.samjna)
        + 2 * bool(row.samasa)
        + 2 * bool(row.gana)
    )


def placed_on(purvapada: str = "", *, gana: str = "",
              uttarapada: str = "", uttarapada_gana: str = "",
              uttarapada_affix: str = "", samasa: str = "",
              case: str = "", result: str = "", samjna: bool = False,
              wants: str = "") -> Accented:
    """
    6.2.64–110 — where in the first member the accent is placed.

    Nothing answers by default: where no rule is reached, 6.1.223
    stands and the accent is at the end of the whole compound.
    """
    matched = [
        row for row in PLACED_TABLE
        if _reaches(row, purvapada, gana, uttarapada, uttarapada_gana,
                    uttarapada_affix, samasa, case, result, samjna)
        and _supplies(row, wants)
    ]
    if not matched:
        return Accented(
            "", "", "No rule of 6.2.64–110 is reached, so 6.1.223 "
                    "समासस्य stands and the accent is at the end of "
                    "the compound")
    row = max(matched, key=_how_specific)
    return Accented("" if row.refuses else row.where, row.sutra,
                    row.why, optional=row.optional,
                    blocked_by=row.blocks)


def placement_runs() -> Accented:
    """
    The three runs open over this stretch, and where each stops.

    **आदिरिति प्राग् अन्ताधिकारात्। उदात्त इति प्रकृत्या भगालम् इति
    यावत्** for the first two, and **प्राग् उत्तरपदादिः इत्येतस्माद्
    अयम् अधिकारो वेदितव्यः** for the third.
    """
    return Accented(
        "ādi", ADI_RUN[0],
        "आदिः governs %s–%s and अन्तः %s–%s, while the word उदात्तः "
        "of the same sūtra runs on to %s — past both. And "
        "बहुव्रीहि opens a fourth run at %s, bounded by %s's word "
        "अव्ययीभावे"
        % (ADI_RUN[0], ADI_RUN[1], ANTA_RUN[0], ANTA_RUN[1],
           UDATTA_RUN[1], BAHUVRIHI_RUN[0], "6.2.121"))


def provisions_for(sutra_id: str) -> Tuple[Placed, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in PLACED_TABLE if row.sutra == sutra_id)
