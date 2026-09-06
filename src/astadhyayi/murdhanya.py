# -*- coding: utf-8 -*-
"""
८.३.५५–८९ — अपदान्तस्य मूर्धन्यः, and the स् that becomes ष्.

Two headings open one after another and both run to the end of
the pāda. 8.3.55 **अपदान्तस्य मूर्धन्यः** — **पदाधिकारो
निवृत्तः** — takes 8.1.16's पदस्य away and puts NOT-word-final
in its place; and 8.3.57 **इण्कोः** adds what must come before:
**इणः कवर्गात् च**, a vowel other than अ, a semivowel, ह् or a
guttural. Everything to 8.3.119 borrows both.

**WHAT BECOMES ष्.** A स् that is a SUBSTITUTE or belongs to an
AFFIX (8.3.59 सिषेव, अग्निषु, वायुषु) — which is the rule every
locative plural in ि and ु passes through; the स् of शास्, वस्
and घस् (8.3.60 शिष्टः, उषितः, जक्षतुः); and then twenty-five
sūtras naming particular roots after particular preverbs —
सुनोति and eleven more after any preverb (8.3.65 अभिषुणोति),
सद् after any but प्रति (8.3.66 निषीदति), स्तम्भ् (8.3.67
अभिष्टभ्नाति), सेव् and seven more after परि, नि and वि (8.3.70
परिषेवते).

**AND THE SOUND CAN REACH ACROSS SOMETHING.** 8.3.58 lets it
cross a नुम्, a visarga or a शर् — सर्पींषि, यजूंषि — and 8.3.63
प्राक्सितादड्व्यवायेऽपि lets it cross the augment अ of the past
tenses as far as 8.3.70: न्यषीदत्, अभ्यष्टभ्नात्. Without that
heading every imperfect of these roots would lose its cerebral.

**AND EIGHT SŪTRAS ARE ABOUT COMPOUNDS AND NOTHING ELSE.**
8.3.80–86: अङ्गुलिषङ्गः, भीरुष्ठानम्, अग्निष्टोमः, अग्नीषोमौ,
ज्योतिष्टोमः, मातृष्वसा — and मातुःष्वसा beside मातुःस्वसा,
where the first member ends in र् and the option is what the
difference comes to.

**WHAT THIS MODULE DOES NOT DO.** 8.3.90–119 — the words laid
down whole and the ten refusals that close the pāda — belong to
the next module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.ru_anunasika import Joined  # noqa: E402

#: This module's stretch.
MURDHANYA_RUN: Tuple[str, str] = ("8.3.55", "8.3.89")

#: 8.3.55's heading, which takes पदस्य away and runs to the
#: pāda's end.
APADANTA_TO: str = "8.3.119"

#: 8.3.57's heading, which says what must stand before.
INKOH_FROM: str = "8.3.57"

#: 8.3.63's heading, which lets the sound cross the augment —
#: and stops at 8.3.70, the last sūtra to name सित्.
ADVYAVAYA_TO: str = "8.3.70"

#: 8.3.65's eleven, whose स् becomes ष् after any preverb.
#: The sūtra's own compound names eleven and not twelve — the
#: first draft of this module miscounted, and the table said so.
SUNOTI_ELEVEN: Tuple[str, ...] = (
    "sunoti", "suvati", "syati", "stauti", "stobhati", "sthā",
    "senaya", "sedha", "sica", "sañja", "svañja")

#: 8.3.70's eight, after परि, नि and वि.
SEVADI_EIGHT: Tuple[str, ...] = (
    "sev", "sita", "saya", "sivu", "sah", "suṭ", "stu", "svañj")

#: 8.3.71's own subset of those, which may cross the augment.
SIVADI: Tuple[str, ...] = ("sivu", "sah", "suṭ", "stu", "svañj")

#: 8.3.78's three, whose ध् becomes ढ् after an इण्-final stem.
SIDHVAM_THREE: Tuple[str, ...] = ("ṣīdhvam", "luṅ", "liṭ")


@dataclass(frozen=True)
class Murdhanya:
    """One rule of 8.3.55–89: a cerebral, or a स् kept as स्."""

    sutra: str
    #: `ṣa`, `sa`, `ḍha`, `nipātana`.
    does: str = ""
    #: The roots or words named outright.
    of: Tuple[str, ...] = ()
    #: The shape of what the rule reaches.
    gana: str = ""
    #: What must stand before — a preverb, a first member, or
    #: the class of sounds 8.3.57's heading names.
    after: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    sense: Tuple[str, ...] = ()
    #: True of a rule that only opens a heading.
    heading: bool = False
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


MURDHANYA_TABLE: Tuple[Murdhanya, ...] = (
    Murdhanya(
        "8.3.55", does="ṣa", heading=True,
        why="अपदान्तस्य मूर्धन्यः — a heading, and it begins by "
            "cancelling one: **पदाधिकारो निवृत्तः** — 8.1.16's "
            "पदस्य stops here, and NOT-word-final takes its "
            "place. **अपदान्तस्य इति मूर्धन्य इति च एतद् "
            "अधिकृतं वेदितव्यम् आ पादपरिसमाप्तेः**, and the "
            "vṛtti proves it on the rule four sūtras later: "
            "**सिषेव, सुष्वाप, अग्निषु, वायुषु**"),
    Murdhanya(
        "8.3.56", does="ṣa", of=("sah",), gana="sāḍ",
        keeps_out="साडिः — the patronymic of सड, where the root "
                  "is not सह् at all",
        why="सहेः साडः सः — the स् of सह् IN THE FORM साड् "
            "becomes cerebral: **जलाषाट्, तुराषाट्, "
            "पृतनाषाट्**. Both words of the sūtra are tested — "
            "**सहेर् इति किम्? साडिः; साड्ग्रहणं किम्?** — the "
            "first keeping out a word that merely looks like "
            "it, the second confining the rule to the one shape "
            "the root takes in a compound"),
    Murdhanya(
        "8.3.57", does="ṣa", heading=True,
        why="इण्कोः — the second heading, and it says what must "
            "stand BEFORE: **इणः कवर्गात् च इत्येवं तद् "
            "वेदितव्यम्** — a vowel other than अ, a semivowel, "
            "ह्, or a guttural. **सिषेव, अग्निषु, वायुषु, "
            "कर्तृषु**. Every cerebral of the rest of the pāda "
            "wants one of those in front of it, and this is why "
            "the locative plural of अग्नि has a ष् and that of "
            "वृक्ष has not"),
    Murdhanya(
        "8.3.58", does="ṣa", gana="num-visarjanīya-śar-vyavāya",
        after="iṇ-ku",
        why="नुम्विसर्जनीयशर्व्यवायेऽपि — and the cerebral "
            "reaches ACROSS a नुम्, a visarga or a शर्: "
            "**व्यवायशब्दः प्रत्येकम् अभिसम्बध्यते**, the word "
            "'intervention' goes with each of the three. Across "
            "a नुम् — **सर्पींषि, यजूंषि, हवींषि** — which is "
            "how every neuter plural of an इस्-final stem is "
            "made, the नुम् and the anusvāra both standing "
            "between the इ and the ष्"),
    Murdhanya(
        "8.3.59", does="ṣa", gana="ādeśa-pratyaya-sa",
        after="iṇ-ku",
        why="आदेशप्रत्यययोः — a स् that is a SUBSTITUTE or "
            "belongs to an AFFIX becomes cerebral after an इण् "
            "or a guttural: **सिषेव, सुष्वाप** for the "
            "substitute, and **अग्निषु, वायुषु, कर्तृषु** for "
            "the affix. **आदेशप्रत्यययोर् इति षष्ठी भेदेन "
            "सम्बध्यते** — the two genitives are read apart and "
            "not as one compound. This is the rule the whole "
            "locative plural turns on"),
    Murdhanya(
        "8.3.60", does="ṣa", of=("śās", "vas", "ghas"),
        after="iṇ-ku",
        why="शासिवसिघसीनां च — and the स् of शास्, वस् and घस्, "
            "though it is neither a substitute nor an affix: "
            "**अन्वशिषत्, शिष्टः, शिष्टवान्** from the first; "
            "**उषितः, उषितवान्, उषित्वा** from the second; "
            "**जक्षतुः, जक्षुः** from the third. Three roots "
            "added to a rule that otherwise reaches only what "
            "the grammar itself has put there"),
    Murdhanya(
        "8.3.61", does="ṣa", of=("stu", "ṇyanta"),
        after="abhyāsa-iṇ", before=("ṣa-san",),
        why="स्तौतिण्योरेव षण्यभ्यासात् — of स्तु and of the "
            "causals, before a सन् that has a ष् in it, and "
            "only after the reduplicated syllable: "
            "**तुष्टूषति**; and for the causals **सिषेचयिषति, "
            "सिषञ्जयिषति, सुष्वापयिषति**. **सिद्धे सत्य् "
            "आरम्भो नियमार्थः** — the cerebral was available "
            "anyway and the sūtra is there to confine it to "
            "these two, which is what the एव says"),
    Murdhanya(
        "8.3.62", does="sa", of=("svid", "svad", "sah"),
        after="abhyāsa", before=("ṣa-san",), blocks=("8.3.61",),
        why="सः स्विदिस्वदिसहीनां च — but the causals of स्विद्, "
            "स्वद् and सह् keep a plain स्: **सिस्वेदयिषति, "
            "सिस्वादयिषति, सिसाहयिषति**. **सकारस्य सकारवचनम्** "
            "— prescribing स् for स् is idle except as a way of "
            "keeping the cerebral out, which is what it is for, "
            "and it is the same device 8.3.25 used for the म्"),
    Murdhanya(
        "8.3.63", does="ṣa", heading=True,
        why="प्राक्सितादड्व्यवायेऽपि — a third heading, and a "
            "short one: as far as the sūtra that names सित् — "
            "which is 8.3.70 — the cerebral reaches ACROSS the "
            "augment अ, **अपिशब्दाद् अनड्व्यवायेऽपि**, and "
            "across nothing as well. Without it every imperfect "
            "and aorist of these roots would lose its cerebral: "
            "**न्यषीदत्, व्यषीदत्, अभ्यष्टभ्नात्**"),
    Murdhanya(
        "8.3.64", does="ṣa", gana="sthādi", after="abhyāsa",
        why="स्थादिष्वभ्यासेन चाभ्यासस्य — and for the स्थादि "
            "roots of the next sūtra the cerebral reaches "
            "across the REDUPLICATION as well, and reaches the "
            "reduplication's own स् besides. Two things at "
            "once, and the second is what makes तिष्ठति come "
            "out with a ष् in both syllables where the preverb "
            "calls for it"),
    Murdhanya(
        "8.3.65", does="ṣa", of=SUNOTI_ELEVEN, after="upasarga",
        why="उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेध"
            "सिचसञ्जस्वञ्जाम् — the स् of eleven roots becomes "
            "cerebral after a PREVERB — that is, after whatever "
            "in the preverb 8.3.57's heading names: **अभिषुणोति, "
            "अभिषुवति, अभिष्यति, अभिष्टौति, अभिष्ठीवति, "
            "अभिषिञ्चति, अभिषजति, परिष्वजते**. It is the "
            "longest single list in the pāda and the one every "
            "later preverb rule is stated against"),
    Murdhanya(
        "8.3.66", does="ṣa", of=("sad",), after="upasarga",
        keeps_out="प्रतिसीदति — प्रति is excepted by the "
                  "sūtra's own अप्रतेः",
        why="सदिरप्रतेः — and the स् of सद् after a preverb "
            "OTHER THAN प्रति: **निषीदति, विषीदति; न्यषीदत्, "
            "व्यषीदत्; निषसाद, विषसाद**. The imperfects come "
            "through 8.3.63's heading, and the perfects show "
            "the cerebral reaching across the reduplication as "
            "well, which is 8.3.64's"),
    Murdhanya(
        "8.3.67", does="ṣa", of=("stambh",), after="upasarga",
        why="स्तम्भेः — and स्तम्भ्: **अभिष्टभ्नाति, "
            "परिष्टभ्नाति; अभ्यष्टभ्नात्, पर्यष्टभ्नात्; "
            "अभितष्टम्भ, परितष्टम्भ**. The three sets are the "
            "present, the imperfect across the augment, and the "
            "perfect across the reduplication — the same three "
            "kinds of reach the two headings before have given"),
    Murdhanya(
        "8.3.68", does="ṣa", of=("stambh",), after="ava",
        sense=("ālambana", "āvidūrya"), blocks=("8.3.67",),
        why="अवाच्चालम्बनाविदूर्ययोः — and after अव, but only "
            "where SUPPORT or NEARNESS is meant: **आलम्बनम् "
            "आश्रयणम्। अविदूरस्य भाव आविदूर्यम्**. "
            "**अवष्टभ्यास्ते; अवष्टभ्य**. अव is a preverb like "
            "any other, so 8.3.67 would have reached it — the "
            "sūtra exists to put a sense-condition on that one "
            "preverb and no other"),
    Murdhanya(
        "8.3.69", does="ṣa", of=("svan",), after="vi-ava",
        sense=("bhojana",),
        why="वेश्च स्वनो भोजने — and the स् of स्वन् after वि "
            "and अव where EATING is meant: **विष्वणति, "
            "व्यष्वणत्, विषष्वाण; अवष्वणति, अवाष्वणत्**. The "
            "vṛtti glosses the sense narrowly — "
            "**अभ्यवहारक्रियाविशेषोऽभिधीयते** — a particular "
            "way of taking food, and not sound, which is what "
            "the root ordinarily means"),
    Murdhanya(
        "8.3.70", does="ṣa", of=SEVADI_EIGHT, after="pari-ni-vi",
        why="परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम् — the "
            "स् of eight roots becomes cerebral after परि, नि "
            "and वि: **परिषेवते, निषेवते, विषेवते; पर्यषेवत, "
            "न्यषेवत, व्यषेवत**. This is the last sūtra that "
            "names सित्, so 8.3.63's heading — the one that "
            "lets the cerebral cross the augment — stops with "
            "it, and the imperfects above are the last that "
            "come through it as of right"),
    Murdhanya(
        "8.3.71", does="ṣa", of=SIVADI, gana="aṭ-vyavāya",
        after="pari-ni-vi", optional=True, blocks=("8.3.70",),
        why="सिवादीनां वाऽड्व्यवायेऽपि — and for the last five "
            "of those eight the cerebral crosses the augment "
            "only OPTIONALLY: **तथा च एव उदाहृतम्** — the "
            "vṛtti simply points back at the forms it has just "
            "given. With 8.3.63's heading over, what was "
            "compulsory becomes a choice, and the sūtra is the "
            "hinge between the two"),
    Murdhanya(
        "8.3.72", does="ṣa", of=("syand",),
        after="anu-vi-pari-abhi-ni", sense=("aprāṇi",),
        optional=True,
        why="अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु — the स् of "
            "स्यन्द् after five preverbs, OPTIONALLY, and only "
            "where what flows is not alive: **अनुष्यन्दते, "
            "विष्यन्दते, परिष्यन्दते, अभिष्यन्दते तैलम्, "
            "निष्यन्दते**. Oil flows and a beast does not, "
            "which is the whole of the condition"),
    Murdhanya(
        "8.3.73", does="ṣa", of=("skand",), after="vi",
        before=("a-niṣṭhā",), optional=True,
        keeps_out="विस्कन्नः — a निष्ठा, which the sūtra "
                  "excepts",
        why="वेः स्कन्देरनिष्ठायाम् — and स्कन्द् after वि, "
            "optionally, but not in a निष्ठा: **विष्कन्ता, "
            "विस्कन्ता; विष्कन्तुम्, विस्कन्तुम्; विष्कन्तव्यम्, "
            "विस्कन्तव्यम्**. The exception is what keeps the "
            "past participle out, and the option is what makes "
            "both agent nouns stand"),
    Murdhanya(
        "8.3.74", does="ṣa", of=("skand",), after="pari",
        optional=True,
        why="परेश्च — and after परि: **परिष्कन्ता, परिस्कन्ता; "
            "परिष्कन्तुम्; परिष्कन्तव्यम्**. "
            "**पृथग्योगकरणसामर्थ्यात्** — making it a separate "
            "sūtra rather than adding परि to the one before is "
            "what lets the निष्ठा exception NOT be carried "
            "down, so परिष्कण्णः stands where विस्कन्नः does "
            "not"),
    Murdhanya(
        "8.3.75", does="nipātana", of=("pariskanda",),
        sense=("prācyabharata",), blocks=("8.3.74",),
        keeps_out="परिष्कन्दः — anywhere but among the eastern "
                  "Bharatas",
        why="परिस्कन्दः प्राच्यभरतेषु — **परिस्कन्दः** is laid "
            "down WITHOUT the cerebral, as the eastern Bharatas "
            "use it: **पूर्वेण मूर्धन्ये प्राप्ते तदभावो "
            "निपात्यते**. The sūtra before had just given the "
            "ष्, and this takes it away again in one region's "
            "usage — the only geographical condition in the "
            "whole pāda"),
    Murdhanya(
        "8.3.76", does="ṣa", of=("sphur", "sphul"),
        after="nis-ni-vi", optional=True,
        why="स्फुरतिस्फुलत्योर्निर्निविभ्यः — and स्फुर् and "
            "स्फुल् after निस्, नि and वि, optionally: "
            "**निष्ष्फुरति, निस्स्फुरति; निष्फुरति, "
            "निस्फुरति; विष्फुरति, विस्फुरति**. Four forms for "
            "one word, since the doubled and the single स् are "
            "themselves an option of 8.4's"),
    Murdhanya(
        "8.3.77", does="ṣa", of=("skabh",), after="vi",
        blocks=("8.3.76",),
        why="वेः स्कभ्नातेर्नित्यम् — but स्कभ् after वि takes "
            "it ALWAYS: **विष्कभ्नाति, विष्कम्भिता, "
            "विष्कम्भितुम्, विष्कम्भितव्यम्**. The word "
            "नित्यम् is there because everything around it is "
            "optional — three sūtras before and one after — and "
            "without it the option would have been carried down"),
    Murdhanya(
        "8.3.78", does="ḍha", gana="iṇ-anta-aṅga",
        before=SIDHVAM_THREE,
        why="इणः षीध्वंलुङ्लिटां धोऽङ्गात् — and here it is a "
            "ध् and not a स् that goes cerebral: after a stem "
            "ending in इण्, the ध् of षीध्वम् and of the aorist "
            "and perfect endings becomes ढ्: **च्योषीढ्वम्, "
            "प्लोषीढ्वम्; अच्योढ्वम्, अप्लोढ्वम्; चकृढ्वे, "
            "चकृढ्वम्**. One sūtra in the middle of a run about "
            "the स्, and the reason is the same इण् in front"),
    Murdhanya(
        "8.3.79", does="ḍha", gana="iṭ-para", before=SIDHVAM_THREE,
        optional=True, blocks=("8.3.78",),
        why="विभाषेटः — and after an इट् it is OPTIONAL: "
            "**लविषीढ्वम्, लविषीध्वम्; पविषीढ्वम्, "
            "पविषीध्वम्; अलविढ्वम्, अलविध्वम्**. The second of "
            "each pair is what 8.2.25 धि च was stated for — "
            "the aorist's स् goes so that the ध् may be heard "
            "at all — so the two pādas meet in one form"),
    Murdhanya(
        "8.3.80", does="ṣa", of=("saṅga",), after="aṅguli",
        sense=("samāsa",),
        keeps_out="अङ्गुलेः सङ्गम् — no compound, and no "
                  "cerebral",
        why="समासेऽङ्गुलेः सङ्गः — the स् of सङ्ग becomes "
            "cerebral after अङ्गुलि inside a COMPOUND: "
            "**अङ्गुलिषङ्गः; अङ्गुलिषङ्गा यवागूः; अङ्गुलिषङ्गो "
            "गाः सादयति**. Seven sūtras of this kind follow, "
            "each naming one first member and one second, and "
            "each wanting the compound"),
    Murdhanya(
        "8.3.81", does="ṣa", of=("sthāna",), after="bhīru",
        sense=("samāsa",),
        keeps_out="भीरोः स्थानं पश्य — two words and not one",
        why="भीरोः स्थानम् — and स्थान after भीरु: "
            "**भीरुष्ठानम्**. **समास इत्येव** — the compound is "
            "carried down from the sūtra before and is what "
            "tells भीरुष्ठानम् from भीरोः स्थानम्"),
    Murdhanya(
        "8.3.82", does="ṣa", of=("stut", "stoma", "soma"),
        after="agni", sense=("samāsa",),
        keeps_out="अग्निसोमौ where the first member is short — "
                  "अग्नेर् दीर्घात् सोमस्य इष्यते",
        why="अग्नेः स्तुत्स्तोमसोमाः — and स्तुत्, स्तोम and "
            "सोम after अग्नि: **अग्निष्टुत्, अग्निष्टोमः, "
            "अग्नीषोमौ**. The third is different from the "
            "other two — **अग्नेर् दीर्घात् सोमस्य इष्यते** — "
            "the cerebral coming only where अग्नि has been "
            "lengthened, which is why the pair of gods is "
            "अग्नीषोमौ and not *अग्निषोमौ"),
    Murdhanya(
        "8.3.83", does="ṣa", of=("stoma",), after="jyotis-āyus",
        sense=("samāsa",),
        keeps_out="ज्योतिः स्तोमं दर्शयति — two words",
        why="ज्योतिरायुषः स्तोमः — and स्तोम after ज्योतिस् and "
            "आयुस्: **ज्योतिष्टोमः, आयुष्टोमः**. Both first "
            "members end in स्, which by 8.3.15 is a visarga "
            "and by 8.3.57's heading is not an इण् — so the "
            "rule is needed where 8.3.82's was not"),
    Murdhanya(
        "8.3.84", does="ṣa", of=("svasṛ",), after="mātṛ-pitṛ",
        sense=("samāsa",),
        why="मातृपितृभ्यां स्वसा — and स्वसृ after मातृ and "
            "पितृ: **मातृष्वसा, पितृष्वसा**. The ऋ is an इण्, "
            "so 8.3.57's heading is met; what the sūtra adds is "
            "that the स् is neither a substitute nor an affix "
            "and so would not have been reached by 8.3.59"),
    Murdhanya(
        "8.3.85", does="ṣa", of=("svasṛ",),
        after="mātuḥ-pituḥ", sense=("samāsa",), optional=True,
        blocks=("8.3.84",),
        why="मातुःपितुर्भ्यामन्यतरस्याम् — and after the forms "
            "मातुर् and पितुर् it is OPTIONAL: **मातुःष्वसा, "
            "मातुःस्वसा; पितुःष्वसा, पितुःस्वसा**. "
            "**मातुःपितुर् इति रेफान्तयोर् एतद् रूपम्** — "
            "these are the र्-final shapes of the same two "
            "words, and the difference between the two sūtras "
            "is nothing but which shape the first member has"),
    Murdhanya(
        "8.3.86", does="ṣa", of=("stana",), after="abhinis",
        sense=("śabdasaṃjñā",), optional=True,
        why="अभिनिसः स्तनः शब्दसंज्ञायाम् — and स्तन after "
            "अभिनिस्, optionally, where a SOUND is being named: "
            "**अभिनिष्टानो वर्णः, अभिनिस्तानो वर्णः; "
            "अभिनिष्टानो विसर्जनीयः**. The word is a technical "
            "term of the phoneticians, and the sūtra exists for "
            "the grammar's own vocabulary"),
    Murdhanya(
        "8.3.87", does="ṣa", of=("asti",),
        after="upasarga-prādus", before=("yac-para", "ac-para"),
        why="उपसर्गप्रादुर्भ्यामस्तिर्यच्परः — and the स् of "
            "अस् after a preverb or after प्रादुस्, when a य् "
            "or a vowel follows it: **अभिषन्ति, निषन्ति, "
            "विषन्ति, प्रादुःषन्ति; अभिष्यात्, निष्यात्**. Two "
            "conditions on what precedes and two on what "
            "follows, for one of the commonest roots in the "
            "language"),
    Murdhanya(
        "8.3.88", does="ṣa", of=("supi", "sūti", "sama"),
        after="su-vi-nis-dus",
        why="सुविनिर्दुर्भ्यः सुपिसूतिसमाः — and सुपि, सूति and "
            "सम after सु, वि, निर् and दुर्: **सुषुप्तः, "
            "विषुप्तः, निःषुप्तः, दुःषुप्तः**. The first is "
            "स्वप् with its saṃprasāraṇa already made — "
            "**सुपि इति स्वपिः कृतसम्प्रसारणो गृह्यते** — so "
            "the rule reaches a shape the root list does not "
            "have"),
    Murdhanya(
        "8.3.89", does="ṣa", of=("snā",), after="ni-nadī",
        sense=("kauśala",),
        why="निनदीभ्यां स्नातेः कौशले — and the स् of स्ना after "
            "नि and after नदी, where SKILL is meant: "
            "**निष्णातः कटकरणे; निष्णातो रज्जुवर्तने** — expert "
            "at mat-making, expert at rope-twisting. And "
            "**नद्यां स्नातीति नदीष्णः**, where 3.2.4's सुपि "
            "स्थः gives the second member its shape"),
)


def _reaches(row: Murdhanya, root: str, gana: str, after: str,
             before: str, sense: str) -> bool:
    # A heading answers nothing: 8.3.55, 8.3.57 and 8.3.63 are
    # stated of every rule after them and of none in particular.
    if row.heading:
        return False
    # `of` and `gana` CONJOIN: 8.3.71 names five roots AND wants
    # the augment between, and either alone is not the rule.
    if row.of and root not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.after and after != row.after:
        return False
    if row.before and before not in row.before:
        return False
    if row.sense and sense not in row.sense:
        return False
    return True


def _how_specific(row: Murdhanya) -> int:
    """
    A rule that displaces another beats it, a named root beats
    a shape, and a named sense beats both.

    8.3.67 against 8.3.68 is why the sense has to weigh: स्तम्भ्
    takes the cerebral after any preverb, and after अव only
    where support or nearness is meant.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of)
        + 6 * len(row.sense)
        + 4 * bool(row.gana)
        + 4 * bool(row.after)
        + 3 * bool(row.before)
    )


def the_cerebral(root: str = "", *, gana: str = "",
                 after: str = "", before: str = "",
                 sense: str = "") -> Joined:
    """
    8.3.55–89 — the स् that becomes ष्, and the ध् that becomes ढ्.

    Nothing answers by default. 8.3.57's इण्कोः is a condition
    on what stands BEFORE, and a query that does not name it
    still reaches the rules, since the heading is recorded
    rather than enforced.
    """
    matched = [
        row for row in MURDHANYA_TABLE
        if _reaches(row, root, gana, after, before, sense)
    ]
    if not matched:
        return Joined(
            "", "", "No rule of 8.3.55-89 is reached, so the s "
                    "stands as it is")
    row = max(matched, key=_how_specific)
    return Joined(row.does, row.sutra, row.why,
                  optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Murdhanya, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in MURDHANYA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Murdhanya", "MURDHANYA_TABLE", "MURDHANYA_RUN",
    "APADANTA_TO", "INKOH_FROM", "ADVYAVAYA_TO",
    "SUNOTI_ELEVEN", "SEVADI_EIGHT", "SIVADI", "SIDHVAM_THREE",
    "the_cerebral", "provisions_for",
]
