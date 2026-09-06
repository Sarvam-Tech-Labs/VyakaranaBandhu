# -*- coding: utf-8 -*-
"""
७.१.९–३३ — what the case ending becomes.

Twenty-five sūtras, and between them they are most of how a noun
declines. भिस् becomes ऐस् and वृक्ष + भिस् is वृक्षैः; टा ङसि ङस्
become इन आत् स्य and the same stem gives वृक्षेण, वृक्षात्,
वृक्षस्य; ङे becomes य and it is वृक्षाय. Nothing here is a sound
change — each is one ending swapped for another, and the शिष्ट
forms of the language fall out of the swaps.

**AND THE PRONOUNS TAKE THE SAME ENDINGS AND THEN TAKE THEM
BACK.** 7.1.14–17 give a सर्वनामन् स्मै, स्मात्, स्मिन् and शी
where an ordinary stem had य, आत्, इ and अस् — सर्वस्मै beside
वृक्षाय — and 7.1.16 then makes nine of those pronouns optional,
so पूर्वस्मात् and पूर्वात् both stand. The nine are not a class
but a list, and the vṛtti gives both forms of each.

**AND युष्मद् AND अस्मद् GET SEVEN SŪTRAS TO THEMSELVES.**
7.1.27–33: अश्, अम्, न, भ्यम्, अत्, अत् again, आकम् — तव, तुभ्यम्,
त्वम्, युष्मान्, युष्मभ्यम्, त्वत्, युष्माकम्. Two words, and
their declension is stated ending by ending because no rule of the
ordinary kind reaches them.

**WHAT THIS MODULE DOES NOT DO.** It says what the ending becomes.
That the ending was there at all is 4.1.2's, and what happens to
the stem in front of it is अध्याय ६'s and 7.3's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
SUP_RUN: Tuple[str, str] = ("7.1.9", "7.1.33")

#: 7.1.9's अतः heads the run — **अत इत्यधिकारो जसः शी इति यावत्**,
#: so it reaches to 7.1.17 and no further.
ATAH_RUN: Tuple[str, str] = ("7.1.9", "7.1.17")

#: The युष्मद्/अस्मद् block, stated ending by ending.
YUSMAD_RUN: Tuple[str, str] = ("7.1.27", "7.1.33")

#: 7.1.12's three, matched one to one.
TA_NASI_NAS: Tuple[Tuple[str, str], ...] = (
    ("ṭā", "ina"), ("ṅasi", "āt"), ("ṅas", "sya"))

#: 7.1.15's two, likewise.
NASI_NI: Tuple[Tuple[str, str], ...] = (
    ("ṅasi", "smāt"), ("ṅi", "smin"))

#: 7.1.16's nine, where the pronoun's own ending is optional.
PURVADI_NINE: Tuple[str, ...] = (
    "pūrva", "para", "avara", "dakṣiṇa", "uttara", "apara",
    "adhara", "sva", "antara")

#: 7.1.25's five, which take अद्ड्: कतरत्, कतमत्, इतरत्,
#: अन्यतरत्, अन्यत्.
DATARADI_FIVE: Tuple[str, ...] = (
    "ḍatara", "ḍatama", "itara", "anyatara", "anya")

#: The two words 7.1.27–33 is entirely about.
THE_TWO: Tuple[str, ...] = ("yuṣmad", "asmad")


@dataclass(frozen=True)
class Sup:
    """One rule of 7.1.9–33: an ending swapped for another."""

    sutra: str
    #: What the ending becomes, or `luk` where it is dropped.
    does: str = ""
    #: The endings the rule names.
    of: Tuple[str, ...] = ()
    #: Where the naming is one to one.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: The stem class: a-anta, āp-anta, napuṃsaka, sarvanāma, ṣaṭ.
    after: str = ""
    #: The stems named outright.
    stem: Tuple[str, ...] = ()
    #: A further condition on the ending — its case, or that a
    #: सुट् has already come.
    case: str = ""
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    bahulam: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


SUP_TABLE: Tuple[Sup, ...] = (
    Sup(
        "7.1.9", does="ais", of=("bhis",), after="a-anta",
        keeps_out="अग्निभिः, वायुभिः — the stem does not end in "
                  "अ; खट्वाभिः, मालाभिः — the तपर shuts out the "
                  "long आ",
        why="अतो भिस ऐस् — after an अ-final stem भिस् becomes ऐस्: "
            "**वृक्षैः, प्लक्षैः, अतिजरसैः**.\\n\\n"
            "**AND ONE OF ITS EXAMPLES IS THERE TO BREAK A "
            "PARIBHĀṢĀ.** अतिजरसैः has जरा shortened to जरस् by "
            "6.4.4's क्रम, so the अ the rule needs was made by the "
            "very compound that would then destroy it. "
            "**संनिपातलक्षणो विधिरनिमित्तं तद्विघातस्य इति "
            "परिभाषेयम् अनित्या** — the maxim is not universal, "
            "and 3.1.14's **कष्टाय क्रमणे** is where Pāṇini shows "
            "it. A verse settles the order against एत्व: "
            "**कृतेऽप्येत्वे भौतपूर्व्याद् ऐस् तु नित्यस्तथा "
            "सति**.\\n\\n"
            "**AND ITS अतः IS A HEADING.** **अत इत्यधिकारो जसः "
            "शी इति यावत्** — every rule to 7.1.17 wants an "
            "अ-final stem"),
    Sup(
        "7.1.10", does="ais", of=("bhis",), chandasi=True,
        bahulam=True, blocks=("7.1.9",),
        why="बहुलं छन्दसि — and in the Veda the ऐस् is बहुलम्, so "
            "it reaches what 7.1.9 could not and fails where "
            "7.1.9 would have held: **अत इत्युक्तम् अनतोऽपि "
            "भवति नद्यैः इति। अतो न भवति — देवेभिः सर्वेभिः "
            "प्रोक्तम्**. Both halves of बहुलम् shown in one "
            "line"),
    Sup(
        "7.1.11", refuses=True, of=("bhis",),
        stem=("idam", "adas"), excludes=("ka",),
        blocks=("7.1.9",),
        keeps_out="इमकैः, अमुकैः — a क has come between, and the "
                  "refusal lapses",
        why="नेदमदसोरकोः — but इदम् and अदस् do NOT take ऐस्, "
            "unless a क stands in them: **एभिः, अमीभिः**.\\n\\n"
            "**AND THE अकोः IS ITSELF A ज्ञापक.** **अकोरित्येतद् "
            "एव प्रतिषेधवचनं ज्ञापकं तन्मध्यपतितस्तद्ग्रहणेन "
            "गृह्यते इति** — a word with something inserted in "
            "the middle is still that word, which is why the "
            "sūtra has to say *without a क* at all. Stated as a "
            "प्रतिषेध rather than as a नियम **इदमदसोः कादिति**, "
            "because a नियम could be read backwards and would "
            "then lose सर्वकैः"),
    Sup(
        "7.1.12", pairs=TA_NASI_NAS,
        of=tuple(one for one, _ in TA_NASI_NAS), after="a-anta",
        keeps_out="सख्या, पत्या — इ-final stems, which 1.4.7 "
                  "keeps out of the अ-run",
        why="टाङसिङसामिनात्स्याः — after an अ-final stem टा ङसि "
            "ङस् become इन आत् स्य, one to one: **वृक्षेण, "
            "प्लक्षेण; वृक्षात्, प्लक्षात्; वृक्षस्य, "
            "प्लक्षस्य**. And where 7.1.9's अतिजरसैः went "
            "through, अतिजरसिना is not settled — **अतिजरसिन "
            "अतिजरसाद् इति केचिद् इच्छन्ति। यथा तु भाष्ये तथा "
            "नैतद् इष्यते**"),
    Sup(
        "7.1.13", does="ya", of=("ṅe",), after="a-anta",
        keeps_out="सख्ये, पत्ये — again not अ-final",
        why="ङेर्यः — and ङे, the dative singular, becomes य: "
            "**वृक्षाय, प्लक्षाय**. The lengthening in वृक्षाय "
            "is 7.3.102's, and it happens although the य that "
            "conditions it is the very thing the अ made "
            "possible — **संनिपातलक्षणो विधिः० इति परिभाषेयम् "
            "अनित्या, तेन दीर्घो भवति**, the same maxim 7.1.9 "
            "had to break"),
    Sup(
        "7.1.14", does="smai", of=("ṅe",), after="sarvanāma",
        blocks=("7.1.13",),
        keeps_out="भवते — भवत् is no सर्वनामन्, and the ordinary "
                  "य stands",
        why="सर्वनाम्नः स्मै — after an अ-final PRONOUN the ङे "
            "becomes स्मै instead: **सर्वस्मै, विश्वस्मै, "
            "यस्मै, तस्मै, कस्मै**.\\n\\n"
            "**AND IT HAS TO BE DONE BEFORE 2.4.32's अश्.** In "
            "अथोऽत्रास्मै the अन्वादेश would give एकादेश first "
            "and the स्मै would never be reached; "
            "**अन्तरङ्गत्वाद् एकादेशात् पूर्वं स्मैभावः "
            "क्रियते, पश्चाद् एकादेशः** — the inner operation "
            "goes in first"),
    Sup(
        "7.1.15", pairs=NASI_NI,
        of=tuple(one for one, _ in NASI_NI), after="sarvanāma",
        keeps_out="भवतः, भवति — not a pronoun; वृक्षात्, वृक्षे — "
                  "not a pronoun either, and 7.1.12 supplies "
                  "those",
        why="ङसिङ्योः स्मात्स्मिनौ — and ङसि and ङि become स्मात् "
            "and स्मिन्, one to one: **सर्वस्मात्, यस्मात्, "
            "कस्मात्; सर्वस्मिन्, यस्मिन्, अन्यस्मिन्**"),
    Sup(
        "7.1.16", pairs=NASI_NI, of=("ṅasi", "ṅi"),
        stem=PURVADI_NINE, after="sarvanāma", optional=True,
        blocks=("7.1.15",),
        keeps_out="त्यस्मात्, त्यस्मिन् — त्यद् is a pronoun but "
                  "not one of the nine, so 7.1.15 stands",
        why="पूर्वादिभ्यो नवभ्यो वा — but after NINE of the "
            "pronouns the स्मात् and स्मिन् are optional, and "
            "the ordinary ending stands beside them: "
            "**पूर्वस्मात्, पूर्वात्; पूर्वस्मिन्, पूर्वे; "
            "परस्मात्, परात्; स्वस्मात्, स्वात्; अन्तरस्मात्, "
            "अन्तरात्**. The vṛtti gives both forms of all nine "
            "and then asks **नवभ्य इति किम्?** — त्यस्मात्, "
            "which is not one of them"),
    Sup(
        "7.1.17", does="śī", of=("jas",), after="sarvanāma",
        why="जसः शी — and जस् becomes शी: **सर्वे, विश्वे, ये, "
            "के, ते**. The ई is written long for the sūtra that "
            "follows and not for this one — **दीर्घोच्चारणम् "
            "उत्तरार्थम्**, which is how त्रपुणी and जतुनी come "
            "out"),
    Sup(
        "7.1.18", does="śī", of=("auṅ",), after="āp-anta",
        why="औङ आपः — after an आप्-final stem the dual औङ् "
            "becomes शी: **खट्वे तिष्ठतः, खट्वे पश्य, बहुराजे, "
            "कारीषगन्ध्ये**.\\n\\n"
            "**AND TWO VERSES ARGUE ABOUT ITS ङ्.** **ङकारः "
            "सामान्यग्रहणार्थः, औटोऽपि ग्रहणं यथा स्यात्** — the "
            "marker is there so that औट् is caught too. The "
            "objection: a ङित् substitute would then bring ङित् "
            "effects with it. The answer: **ङित्त्वे विद्याद् "
            "वर्णनिर्देशमात्रं** — here the ङ् only identifies a "
            "sound, and a sound-naming ङ् carries nothing"),
    Sup(
        "7.1.19", does="śī", of=("auṅ",), after="napuṃsaka",
        why="नपुंसकाच्च — and after a NEUTER stem: **कुण्डे "
            "तिष्ठतः, कुण्डे पश्य; दधिनी, मधुनी; त्रपुणी, "
            "जतुनी**. The शी would have triggered 6.4.148's "
            "इ-loss, and a vārttika stops it — **श्यां प्रतिषेधो "
            "वक्तव्यः**"),
    Sup(
        "7.1.20", does="śi", of=("jas", "śas"), after="napuṃsaka",
        keeps_out="कुण्डशो ददाति, वनशः प्रविशन्ति — शस् the "
                  "taddhita of 5.4.43, not the accusative plural",
        why="जश्शसोः शिः — after a neuter stem जस् and शस् become "
            "शि: **कुण्डानि तिष्ठन्ति, कुण्डानि पश्य; दधीनि, "
            "मधूनि; त्रपूणि, जतूनि**. And the शस् meant is the "
            "one that keeps company with जस् — **जसा "
            "सहचरितस्य शसो ग्रहणात्**, so the taddhita शस् is "
            "out"),
    Sup(
        "7.1.21", does="auś", of=("jas", "śas"), stem=("aṣṭan",),
        case="kṛta-ātva", blocks=("7.1.22",),
        keeps_out="अष्ट तिष्ठन्ति — the अष्टन् that has not taken "
                  "7.2.84's आ, and so is not this word; "
                  "प्रियाष्टानः — likewise",
        why="अष्टाभ्य औश् — अष्टा takes औश् for जस् and शस्: "
            "**अष्टौ तिष्ठन्ति, अष्टौ पश्य**. And the अष्टन् "
            "meant is the one that has ALREADY taken its आ — "
            "**कृताकारोऽष्टन्शब्दो गृह्यते** — which the vṛtti "
            "then reads back as a ज्ञापक that 7.2.84's आ is "
            "optional at all.\\n\\n"
            "**AND IT DISPLACES ONE RULE AND NOT THE OTHER.** "
            "**षड्भ्यो लुक् इत्यस्यायम् अपवादः, नाप्राप्ते "
            "तस्मिन् इदम् आरभ्यते** — 7.1.22 is set aside. But "
            "2.4.71's सुप् elision is not, **तस्मिन् प्राप्ते "
            "चाप्राप्ते च**, and so अष्टपुत्रः stands"),
    Sup(
        "7.1.22", does="luk", of=("jas", "śas"), after="ṣaṭ",
        keeps_out="प्रियषषः, प्रियपञ्चानः — the numeral is "
                  "subordinate in the compound, and the rule "
                  "wants it in front",
        why="षड्भ्यो लुक् — after a षट्-named numeral जस् and शस् "
            "are simply dropped: **षट् तिष्ठन्ति, षट् पश्य; "
            "पञ्च, सप्त, नव, दश**. And it reaches a compound "
            "that ENDS in one — **षट्प्रधानात् तदन्तादपि भवति। "
            "परमषट्, उत्तमषट्**"),
    Sup(
        "7.1.23", does="luk", of=("su", "am"), after="napuṃsaka",
        why="स्वमोर्नपुंसकात् — after a neuter stem सु and अम् are "
            "dropped: **दधि तिष्ठति, दधि पश्य; मधु; त्रपु; "
            "जतु**.\\n\\n"
            "**AND THE LOSS BEATS 7.2.102's त्यदादि SUBSTITUTION "
            "IN तद् ब्राह्मणकुलम्.** The reason given is not "
            "order but strength: **लुको हि निमित्तम् अतोऽम् इति "
            "लक्षणान्तरेण विहन्यते, न पुनस् त्यदाद्यत्वेनैव** — "
            "and **यस्य च लक्षणान्तरेण निमित्तं विहन्यते न तद् "
            "अनित्यं भवति**"),
    Sup(
        "7.1.24", does="am", of=("su", "am"), after="a-anta-napuṃsaka",
        blocks=("7.1.23",),
        why="अतोऽम् — but after an अ-final neuter they become अम् "
            "instead of going: **कुण्डं तिष्ठति, कुण्डं पश्य; "
            "वनम्, पीठम्**. And it is अम् and not a bare म् for "
            "a reason the vṛtti gives in four words — "
            "**दीर्घत्वं प्राप्नोति**, 7.3.102 would have "
            "lengthened the stem before a consonant-initial "
            "ending"),
    Sup(
        "7.1.25", does="aḍḍ", of=("su", "am"), stem=DATARADI_FIVE,
        blocks=("7.1.24",),
        keeps_out="नेमं तिष्ठति, नेमं पश्य — नेम is a pronoun but "
                  "not one of the five",
        why="अद्ड् डतरादिभ्यः पञ्चभ्यः — and after five of the "
            "pronouns they become अद्ड्: **कतरत्, कतमत्, इतरत्, "
            "अन्यतरत्, अन्यत्**.\\n\\n"
            "**AND THE ड् IS THERE TO STOP TWO DIFFERENT "
            "THINGS.** **डित्करणं किम्? कतरत् तिष्ठतीत्यत्र "
            "पूर्वसवर्णदीर्घो मा भूत्** — and asked why a plain "
            "त् substitute would not do, the vṛtti answers "
            "**हे कतरद् इति संबुद्धेर्लोपो मा भूत्**. A verse "
            "sums both: **अद्ड्डित्त्वाड् डतरादीनां न लोपो नापि "
            "दीर्घता**"),
    Sup(
        "7.1.26", refuses=True, of=("su", "am"), stem=("itara",),
        chandasi=True, blocks=("7.1.25",),
        keeps_out="इतरत् काष्ठम्, इतरत् कुड्यम् — outside the "
                  "Veda the अद्ड् stands",
        why="नेतराच्छन्दसि — but इतर does not take the अद्ड् in "
            "the Veda: **मृतम् इतरम् आण्डम् अवापद्यत; "
            "वार्त्रघ्नम् इतरम्**.\\n\\n"
            "**AND IT IS PUT AS A REFUSAL RATHER THAN JOINED TO "
            "THE RULE BEFORE, FOR THE SAKE OF ONE WORD.** "
            "**अतोऽम् इत्यस्माद् अनन्तरम् इतराच्छन्दसि इति "
            "वक्तव्ये नेतराच्छन्दसि इति वचनं योगविभागार्थम्। "
            "एकतराद् धि सर्वत्र छन्दसि भाषायां प्रतिषेध "
            "इष्यते** — एकतरम् is refused everywhere, and only a "
            "split sūtra can say so"),
    Sup(
        "7.1.27", does="aś", of=("ṅas",), stem=THE_TWO,
        why="युष्मदस्मद्भ्यां ङसोऽश् — after युष्मद् and अस्मद् "
            "the genitive singular becomes अश्: **तव स्वम्, मम "
            "स्वम्**. The श् makes it replace the whole ending "
            "and not its first sound — **शित्करणं "
            "सर्वादेशार्थम्** — and if it did not, 7.2.89's "
            "योऽचि would not be reached"),
    Sup(
        "7.1.28", does="am", of=("ṅe", "prathamā", "dvitīyā"),
        stem=THE_TWO,
        why="ङे प्रथमयोरम् — and ङे, the nominative and the "
            "accusative all become अम्: **तुभ्यं दीयते, मह्यं "
            "दीयते; त्वम्, अहम्, युवाम्, आवाम्, यूयम्, वयम्; "
            "त्वाम्, माम्**. **ङे इत्यविभक्तिकोऽयं निर्देशः** — "
            "the ङे in the sūtra carries no case ending of its "
            "own, which is how one word can name both an ending "
            "and two whole विभक्तिs"),
    Sup(
        "7.1.29", does="na", of=("śas",), stem=THE_TWO,
        why="शसो न — the accusative plural becomes न: **युष्मान् "
            "ब्राह्मणान्, युष्मान् ब्राह्मणीः, अस्मान् "
            "ब्राह्मणीः, युष्मान् कुलानि, अस्मान् कुलानि** — the "
            "same form whatever the gender of what it stands "
            "beside"),
    Sup(
        "7.1.30", does="bhyam", of=("bhyas",), stem=THE_TWO,
        why="भ्यसो भ्यम् — भ्यस् becomes भ्यम्: **युष्मभ्यं "
            "दीयते, अस्मभ्यं दीयते**.\\n\\n"
            "**AND A PARIBHĀṢĀ SAVES IT FROM 7.3.103's ए.** "
            "After the substitution and 7.2.90's loss the stem "
            "ends before a झल्, and बहुवचने झल्येत् would give "
            "*युष्मेभ्यम्. **अङ्गवृत्ते पुनर्वृत्ताव् अविधिर् "
            "निष्ठितस्य** — a stem already finished with is not "
            "operated on again. Some read the substitute as "
            "अभ्यम् to reach the same end, and the vṛtti says "
            "which readings need which"),
    Sup(
        "7.1.31", does="at", of=("bhyas",), stem=THE_TWO,
        case="pañcamī",
        why="पञ्चम्या अत् — and the ABLATIVE भ्यस् becomes अत्: "
            "**युष्मद् गच्छन्ति, अस्मद् गच्छन्ति**. The same "
            "ending twice over, once as a dative and once as an "
            "ablative, and the two go different ways"),
    Sup(
        "7.1.32", does="at", of=("ṅasi",), stem=THE_TWO,
        case="pañcamī-ekavacana",
        why="एकवचनस्य च — and so does the ablative SINGULAR: "
            "**त्वद् गच्छन्ति, मद् गच्छन्ति**. Two words, and "
            "everything else is carried over: the अत् and the "
            "पञ्चमी from 7.1.31, and युष्मदस्मद्भ्याम् from "
            "7.1.27, four sūtras back. The shortest rule of the "
            "block, and the one that shows how much anuvṛtti the "
            "run is carrying by the time it ends"),
    Sup(
        "7.1.33", does="ākam", of=("sām",), stem=THE_TWO,
        case="āgata-suṭ",
        why="साम आकम् — the genitive plural becomes आकम्: "
            "**युष्माकम्, अस्माकम्**.\\n\\n"
            "**AND THE ENDING IS NAMED WITH AN AUGMENT IT HAS "
            "NOT GOT YET.** साम् is आम् with 7.1.52's सुट् in "
            "it, and the vṛtti asks the obvious question — "
            "**न ह्यादेशविधानकाले सुड् विद्यते?** The answer is "
            "that naming it so is what STOPS the सुट् coming "
            "later: **तस्यैव तु भाविनः सुटो निवृत्त्यर्थम्**. "
            "Once आकम् is in, the stem ends in अ and 7.1.52 "
            "would supply a second सुट्; the स् is already inside "
            "the thing replaced, so it does not"),
)


def _reaches(row: Sup, ending: str, after: str, stem: str,
             case: str, chandasi: bool) -> bool:
    if row.pairs and ending and ending not in dict(row.pairs):
        return False
    if row.of and ending and ending not in row.of:
        return False
    if row.stem and stem not in row.stem:
        return False
    if row.after and after != row.after:
        return False
    if row.case and case != row.case:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.excludes and case in row.excludes:
        return False
    return True


def _becomes(row: Sup, ending: str) -> str:
    """The substitute, where the rule matches one to one."""
    for named, shape in row.pairs:
        if named == ending:
            return shape
    return row.does


def _supplies(row: Sup, ending: str, wants: str) -> bool:
    if not wants:
        return True
    return wants == _becomes(row, ending) and not row.refuses


def _how_specific(row: Sup, ending: str, after: str,
                  stem: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, a named stem
    beats a named class, and a class named in the query beats one
    the row happens to carry.

    7.1.23, 7.1.24, 7.1.25 and 7.1.26 are the four that need all
    of it: the neuter drops सु and अम्, an अ-final neuter turns
    them into अम् instead, five pronouns turn them into अद्ड्, and
    इतर in the Veda refuses even that.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.stem and stem in row.stem)
        + 6 * bool(row.pairs and _becomes(row, ending) != row.does)
        + 5 * bool(row.after and after == row.after)
        + 4 * bool(row.case)
        + 3 * bool(row.of and ending in row.of)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Formed:
    """What the run answers: the ending's new shape, or its loss."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def case_ending(ending: str = "", *, after: str = "",
                stem: str = "", case: str = "",
                chandasi: bool = False,
                wants: str = "") -> Formed:
    """
    7.1.9–33 — what the case ending becomes.

    Nothing answers by default, and that is the ordinary case: an
    ending no rule of this run names goes into the word as it is,
    which is how भ्याम् and सुप् and ओस् survive untouched.
    """
    matched = [
        row for row in SUP_TABLE
        if _reaches(row, ending, after, stem, case, chandasi)
        and _supplies(row, ending, wants)
    ]
    if not matched:
        return Formed(
            "", "", "No rule of 7.1.9-33 is reached, so the "
                    "ending stands as it is")
    row = max(matched,
              key=lambda one: _how_specific(one, ending, after, stem))
    return Formed("" if row.refuses else _becomes(row, ending),
                  row.sutra, row.why, optional=row.optional,
                  blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Sup, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SUP_TABLE if row.sutra == sutra_id)


__all__ = [
    "Sup", "SUP_TABLE", "SUP_RUN", "ATAH_RUN", "YUSMAD_RUN",
    "TA_NASI_NAS", "NASI_NI", "PURVADI_NINE", "DATARADI_FIVE",
    "THE_TWO", "Formed", "case_ending", "provisions_for",
]
