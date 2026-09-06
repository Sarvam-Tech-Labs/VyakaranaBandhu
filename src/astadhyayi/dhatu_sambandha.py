# -*- coding: utf-8 -*-
"""
३.४.१, ४–५ and ९–१२ — an affix out of its proper time, which root to
repeat, and the Vedic infinitives.

अध्याय ३ पाद ४ opens on a question none of the pāda before it asked.
3.4.1 धातुसंबन्धे प्रत्ययाः says that where two root-senses stand in a
relation of qualifier and qualified, **affixes stated for the wrong
time are correct anyway** — अयथाकालोक्ता अपि प्रत्ययाः साधवो भवन्ति.
अग्निष्टोमयाज्यस्य पुत्रो जनिता: the first word is of the past and the
second of the future, and they stand together.

That is broader than the transfers of 3.3.131, which lent one named
tense's affixes to a named time. Here nothing is lent: the ordinary
affix simply is not wrong. And the vṛtti extends it past the verb —
प्रत्ययाधिकारे पुनः प्रत्ययग्रहणम् — so that even a तद्धित given for
the present stands in another time: गोमान् आसीत्, गोमान् भविता.

3.4.4 and 3.4.5 then ask something no rule of 3.2 or 3.3 asked at all:
given that a rule has doubled a verb, WHICH root is to be said after
it. यथाविध्यनुप्रयोगः — the same one; or, where several acts are
gathered, one that covers them all.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from src.astadhyayi.upapada_krt import Added, NotAdded


@dataclass(frozen=True)
class Tumartha:
    """One rule giving an affix in the sense of तुमुन्, in the Veda."""

    sutra: str
    gives: Tuple[str, ...]
    #: 3.4.12 wants शक् standing beside; the others want nothing.
    beside: Tuple[str, ...] = ()
    #: The roots the rule names, where it names any.
    of: Tuple[str, ...] = ()
    #: 3.4.14 gives its affixes in the sense of the कृत्य affixes
    #: — कृत्यानामर्थो भावकर्मणी — and not of तुमुन्.
    krtya_artha: bool = False
    #: 3.4.16 and 3.4.17's भावलक्षण — the root's sense is what
    #: MARKS OUT a state, as in पुरा सूर्यस्योदेतोः, before sunrise.
    bhava_laksana: bool = False
    why: str = ""


#: 3.4.9's twelve, given as one list because the rule does — and the
#: vṛtti marks two pairs that differ in ACCENT alone (असे/असेन्,
#: अध्यै/अध्यैन्), which the unaccented sūtrapāṭha cannot show.
SAYADI: Tuple[str, ...] = (
    "se", "sen", "ase", "asen", "kse", "kasen", "adhyai", "adhyain",
    "kadhyai", "kadhyain", "śadhyai", "śadhyain", "tavai", "taveṅ",
    "taven",
)

TUMARTHA: Tuple[Tumartha, ...] = (
    Tumartha(
        "3.4.9", SAYADI,
        why="तुमर्थे सेसेनसेअसेन्क्सेकसेनध्यैअध्यैन्कध्यैकध्यैन्"
            "शध्यैशध्यैन्तवैतवेङ्तवेनः — fifteen affixes in one rule, "
            "each with its Vedic passage: वक्षे रायः; ता वामेषे "
            "रथानाम् (ऋ० ५.६६.३); क्रत्वे दक्षाय जीवसे (शौ०सं० "
            "६.१९.२); प्रेषे भगाय (तै०सं० १.२.११.१); वायवे पिबध्यै "
            "(ऋ० ७.९२.२); दशमे मासि सूतवे (ऋ० १०.१८४.३).\n\n"
            "AND THE VṚTTI PROVES WHAT तुमर्थ MEANS RATHER THAN "
            "ASSERTING IT. तुमर्थो भावः — कथं ज्ञायते? The argument "
            "runs: वचनसामर्थ्यात् तावदयं कर्तुरपकृष्यते, the very "
            "fact of the statement pulls it away from the agent; न "
            "चान्यस्मिन्नर्थे तुमुन्नादिश्यते, and तुमुन् is given in "
            "no other sense; अनिर्दिष्टार्थाश्च प्रत्ययाः स्वार्थे "
            "भवन्ति (परि० ११३), an affix whose sense is unstated has "
            "its own; स्वार्थश्च धातूनां भाव एव. Four steps, one "
            "paribhāṣā, to establish what a single word of the rule "
            "means.\n\n"
            "SCAR — TWO PAIRS DIFFER IN ACCENT ALONE: स्वरे विशेषः "
            "of असे against असेन्, and of अध्यै against अध्यैन्. The "
            "sūtrapāṭha on disk is unaccented, so the distinction is "
            "recorded and cannot be checked — the same boundary five "
            "rules of 3.3 ran into"),
    Tumartha(
        "3.4.12", ("ṇamul", "kamul"), beside=("śak",),
        why="शकि णमुल्कमुलौ — अग्निं वै देवा विभाजं नाशक्नुवन् "
            "(मै०सं० १.६.४), विभक्तुमित्यर्थः; अपलुम्पं नाशक्नोत् "
            "(मै०सं० १.६.५), अपलोप्तुमित्यर्थः.\n\n"
            "THREE MARKS, AND EACH DOES SOMETHING DIFFERENT. णकारो "
            "वृद्ध्यर्थः — the ण for the strengthening; ककारो "
            "गुणवृद्धिप्रतिषेधार्थः — the क to FORBID both "
            "strengthenings; लकारः स्वरार्थः — the ल for the accent. "
            "So two affixes differing in one letter do opposite "
            "things to the root, and a third letter they share does "
            "neither"),
    Tumartha(
        "3.4.13", ("tosun", "kasun"), beside=("īśvara",),
        why="ईश्वरे तोसुन्कसुनौ — ईश्वरोऽभिचरितोः, अभिचरितुम्; "
            "ईश्वरो विलिखः, विलेखितुम्; ईश्वरो वितृदः, वितर्दितुम्. "
            "Two affixes, and the vṛtti's three examples divide "
            "between them without the rule saying which goes where"),
    Tumartha(
        "3.4.14", ("tavai", "ken", "kenya", "tvan"), krtya_artha=True,
        why="कृत्यार्थे तवैकेन्केन्यत्वनः — अन्वेतवै (ऋ० ७.४४.५), "
            "अन्वेतव्यम्; नावगाहे, नावगाहितव्यम्; दिदृक्षेण्यः (ऋ० "
            "१.१४६.५), दिदृक्षितव्यम्; कर्त्वं हविः (शौ०सं० १.४.३), "
            "कर्तव्यम். कृत्यानामर्थो भावकर्मणी.\n\n"
            "AND ONE AFFIX IS GIVEN TWICE, IN TWO SENSES. तुमर्थे "
            "छन्दसीति सयादिसूत्रेऽपि तवै विहितः, तस्य तुमर्थादन्यत्र "
            "कारके विधिर्द्रष्टव्यः — तवै was already given at 3.4.9 "
            "in the sense of तुमुन्, so ITS statement here is for "
            "some other kāraka. A rule read as being about only part "
            "of what it lists"),
    Tumartha(
        "3.4.16", ("tosun",), of=("sthā", "iṇ", "kṛñ", "vad", "car",
                                  "hu", "tam", "jan"),
        bhava_laksana=True,
        why="भावलक्षणे स्थेण्कृञ्वदिचरिहुतमिजनिभ्यस्तोसुन् — आ "
            "संस्थातोर्वेद्यां शेरते (काठ०सं० ११.६), आ समाप्तेः; पुरा "
            "सूर्यस्योदेतोराधेयः (काठ०सं० ८.३); पुरा वत्सानाम् "
            "अपाकर्तोः (काठ०सं० ३१.१५); आ तमितोरासीत (तै०ब्रा० "
            "१.४.४.५); आ विजनितोः संभवाम (तै०सं० २.५.१.५).\n\n"
            "भावो लक्ष्यते येन तस्मिन्नर्थे — the root's sense is what "
            "MARKS OUT a state, so the word means 'until' or 'before' "
            "and not the act itself. प्रकृत्यर्थविशेषणं "
            "भावलक्षणग्रहणम्, qualifying the root's sense as 3.3.172's "
            "शकि did"),
    Tumartha(
        "3.4.17", ("kasun",), of=("sṛp", "tṛd"), bhava_laksana=True,
        why="सृपितृदोः कसुन् — पुरा क्रूरस्य विसृपो विरप्शिन् (तै०सं० "
            "१.१.९.३); पुरा जत्रुभ्य आतृदः (ऋ० ८.१.१२). Two roots "
            "taking the other of 3.4.13's pair, in the same sense as "
            "the rule before"),
)

#: 3.4.10 and 3.4.11 — five words given whole, all Vedic. Each carries
#: its own affix, as the निपातन of 3.2 and 3.3 learned to.
NIPATANA: Dict[str, Tuple[str, str, str]] = {
    "prayai": (
        "3.4.10", "kai",
        "प्रयै रोहिष्यै अव्यथिष्यै — प्रपूर्वस्य यातेः कैप्रत्ययः: "
        "प्रयै देवेभ्यः (ऋ० १.१४२.६), प्रयातुम्.",
    ),
    "rohiṣyai": (
        "3.4.10", "iṣyai",
        "रुहेरिष्यैप्रत्ययः — अपामोषधीनां रोहिष्यै (तै०सं० "
        "१.३.१०.२), रोहणाय.",
    ),
    "avyathiṣyai": (
        "3.4.10", "iṣyai",
        "व्यथेर्नञ्पूर्वस्येष्यैप्रत्ययः — अव्यथिष्यै (काठ०सं० ३.७), "
        "अव्यथनाय. The root takes the negative particle BEFORE it, "
        "so what is fixed is a whole negated stem.",
    ),
    "avacakṣe": (
        "3.4.15", "eś",
        "अवचक्षे च — रिपुणा नावचक्षे (मा०सं० १७.९३), "
        "नावख्यातव्यमित्यर्थः. अवपूर्वाच् चक्षिङ एश् प्रत्ययो "
        "निपात्यते, and the sense is the कृत्य one running from "
        "3.4.14 — so a fixed word in the middle of a run of rules, "
        "sharing their condition.",
    ),
    "dṛśe": (
        "3.4.11", "ke",
        "दृशे विख्ये च — दृशेः केप्रत्ययः: दृशे विश्वाय सूर्यम् (ऋ० "
        "१.५०.१), द्रष्टुम्.",
    ),
    "vikhye": (
        "3.4.11", "ke",
        "विख्ये त्वा हरामि, विख्यातुम्. The second of the pair, and "
        "the root is ख्या — which 3.2.7 had to note is not a root of "
        "the dhātupāṭha at all but what चक्षिङ् becomes by 2.4.54.",
    ),
}


def dhatu_sambandha(*, related: bool = False,
                    taddhita: bool = False) -> object:
    """
    3.4.1 धातुसंबन्धे प्रत्ययाः — an affix stated for the wrong time
    is correct anyway, where two root-senses stand in a relation.

    धात्वर्थानां संबन्धो धातुसंबन्धः, विशेषणविशेष्यभावः: one act
    qualifies the other. तस्मिन् सत्ययथाकालोक्ता अपि प्रत्ययाः साधवो
    भवन्ति — and only in one direction: विशेषणं गुणत्वाद्
    विशेष्यकालमनुरुध्यते, तेन विपर्ययो न भवति, the QUALIFIER follows
    the qualified's time and not the reverse.

    Broader than 3.3.131's transfers, which lent one named tense's
    affixes to a named time. Nothing is lent here: the ordinary affix
    is simply not wrong.
    """
    if not related:
        return NotAdded(
            "3.4.1",
            "धातुसंबन्धे — the licence holds only where two "
            "root-senses stand in a relation of qualifier and "
            "qualified. Without one, an affix out of its time is "
            "just out of its time")
    why = ("धातुसंबन्धे प्रत्ययाः — अयथाकालोक्ता अपि प्रत्ययाः साधवो "
           "भवन्ति: अग्निष्टोमयाज्यस्य पुत्रो जनिता, the first word "
           "of the past and the second of the future. कृतः कटः श्वो "
           "भविता; भावि कृत्यमासीत्.\n\n"
           "AND ONLY ONE WAY ROUND. विशेषणं गुणत्वाद् "
           "विशेष्यकालमनुरुध्यते, तेन विपर्ययो न भवति — the "
           "QUALIFIER accommodates the qualified's time, being "
           "subordinate, and not the reverse. An asymmetry the rule "
           "does not state.")
    if taddhita:
        why += ("\n\nप्रत्ययाधिकारे पुनः प्रत्ययग्रहणम् "
                "अधात्वधिकारविहिता अपि प्रत्ययास्तद्धिता "
                "धातुसंबन्धे सति कालभेदे साधवो यथा स्युरिति — the "
                "word प्रत्यय is repeated, though the section is "
                "about affixes, SO THAT AFFIXES GIVEN OUTSIDE THE "
                "ROOT SECTION are reached too: गोमान् आसीत्, गोमान् "
                "भविता, where a तद्धित given for the present stands "
                "in another time. A repetition that widens, as "
                "3.2.106's and 3.2.124's did.")
    return Added("(any, out of its time)", "3.4.1", why)


def anuprayoga(*, gathered: bool = False,
               kashadi: bool = False) -> object:
    """
    3.4.4, 3.4.5 and 3.4.46 — which root is to be said AFTER.

    A question no rule of 3.2 or 3.3 asked. 3.4.2 and 3.4.3 double a
    verb; these two say what follows it.

    3.4.4 यथाविध्यनुप्रयोगः: यस्माद् धातोर्लोड् विहितः, स एव
    धातुरनुप्रयोक्तव्यः — the SAME root. लुनीहिलुनीहीत्येवायं लुनाति,
    and छिनत्तीति नानुप्रयुज्यते.

    3.4.5 समुच्चयेऽन्यतरस्याम्: where several acts are gathered, one
    root COVERING them all — ओदनं भुङ्क्ष्व, सक्तून् पिब, धानाः खाद
    इत्येवायम् अभ्यवहरति, three particular acts answered by one
    general word for taking food.
    """
    if kashadi:
        return Added(
            "the same root", "3.4.46",
            "कषादिषु यथाविध्यनुप्रयोगः — निमूलसमूलयोः इत्येतदारभ्य "
            "कषादयः, एतेषु यथाविध्यनुप्रयोगो भवति: यस्माद् धातोर् "
            "णमुल् प्रत्ययो भवति, स एवानुप्रयोक्तव्यः.\n\n"
            "THE CLASS IS DEFINED BY WHERE A RUN BEGINS. 3.4.34 said "
            "इतः प्रभृति कषादीन् यान् वक्ष्यति — from that rule on, "
            "the roots named form the कषादि class, called after its "
            "first member. Every gaṇa met before this was a LIST, and "
            "two of them are on disk; this one is an extent.\n\n"
            "AND THE RULE IS RESTRICTIVE, NOT PRESCRIPTIVE. ननु "
            "धातुसंबन्धे प्रत्ययविधानादनुप्रयोगः सिद्ध एव? — that "
            "SOMETHING is said after follows from 3.4.1 already, as "
            "3.4.4's vṛtti had said of its own rule. "
            "यथाविधीति नियमार्थं वचनम्: the statement is for the "
            "RESTRICTION, that it be the same root and no other. The "
            "identical shape as 3.4.4, twenty-two sūtras on, and for "
            "the identical reason")

    if gathered:
        return Added(
            "sāmānyavacana", "3.4.5",
            "समुच्चयेऽन्यतरस्याम् — सामान्यवचनस्य धातोरनुप्रयोगः "
            "कर्तव्यः: ओदनं भुङ्क्ष्व, सक्तून् पिब, धानाः खाद "
            "इत्येवायमभ्यवहरति. सर्वविशेषानुप्रयोगनिवृत्त्यर्थं "
            "वचनम् — stated to stop every particular being repeated. "
            "And लाघवं च लौकिके शब्दव्यवहारे नाद्रियते: BREVITY IS "
            "NOT A CONSIDERATION IN ORDINARY SPEECH, which is the "
            "grammar declining to apply to usage a value it applies "
            "to itself")
    return Added(
        "the same root", "3.4.4",
        "यथाविध्यनुप्रयोगः — यस्माद् धातोर्लोड् विहितः, स एव "
        "धातुरनुप्रयोक्तव्यः: लुनीहिलुनीहीत्येवायं लुनाति, and "
        "छिनत्तीति नानुप्रयुज्यते.\n\n"
        "धातुसंबन्धे प्रत्ययविधानादनुप्रयोगः सिद्ध एव, यथाविध्यर्थं "
        "तु वचनम् — that SOMETHING is said after follows from 3.4.1 "
        "already; what this rule adds is WHICH. A rule stated for "
        "half of what it appears to say")


def tumartha_affix(*, beside: str = "", root: str = "",
                   krtya_artha: bool = False,
                   bhava_laksana: bool = False,
                   wants: str = "") -> object:
    """
    3.4.9 and 3.4.12 — affixes in the sense of तुमुन्, in the Veda.

    Both are छन्दसि only, which is codified one-way as it was through
    3.2 and 3.3: a Vedic rule must not answer outside, and a rule
    silent about the Veda still answers inside it.
    """
    matched = [row for row in TUMARTHA
               if (not row.beside or beside in row.beside)
               and (not row.of or root in row.of)
               and (not row.krtya_artha or krtya_artha)
               and (not row.bhava_laksana or bhava_laksana)
               and (not wants or wants in row.gives)]
    if not matched:
        return NotAdded(
            "",
            "No rule of this run gives that in the sense of तुमुन्. "
            "3.4.9 gives fifteen affixes and 3.4.12 two more where "
            "शक् stands beside — all of them in the Veda only")
    best = max(matched,
               key=lambda row: (3 * (len(row.beside) > 0)
                                + 3 * (len(row.of) > 0)
                                + 2 * row.krtya_artha
                                + 2 * row.bhava_laksana))
    return Added(wants or best.gives[0], best.sutra, best.why)


def nipatana(word: str = "") -> object:
    """
    3.4.10 and 3.4.11 — five Vedic words given whole.

    Each entry carries its own affix, which the निपातन tables of 3.2
    and 3.3 both had to learn: 3.4.10 fixes कै for one word and इष्यै
    for two others, and one of the three is a NEGATED stem.
    """
    entry = NIPATANA.get(word)
    if entry is None:
        return NotAdded(
            "",
            "No rule of this run fixes that word. The ones it fixes "
            "are " + ", ".join(sorted(NIPATANA)))
    sutra, affix, why = entry
    return Added(affix, sutra, why)
