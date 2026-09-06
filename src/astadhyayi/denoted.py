# -*- coding: utf-8 -*-
"""
३.४.६७–७१ — what an affix DENOTES.

Every rule of 3.2, 3.3 and this pāda so far has answered *which affix
comes*. These five answer a different question: **what the affix, once
it has come, stands for** — the doer, the thing done, or the act
itself.

That is the debt NORTH_STAR has carried since 3.2.110. The लकार table
has named its endings as bare strings — लट्, लङ्, लिट् — and nothing
could ask what one of them IS. **3.4.69 लः कर्मणि च भावे चाकर्मकेभ्यः
answers it**: a लकार denotes the OBJECT, and by its first च the doer
as well; after an intransitive root it denotes the ACT, and by its
second च the doer again. गम्यते ग्रामो देवदत्तेन, गच्छति ग्रामं
देवदत्तः.

The run is built the way the vṛtti reads it. 3.4.67 कर्तरि कृत् is a
heading — कृदुत्पत्तिवाक्यानामयं शेषः, the remainder of every rule
that gives a कृत् affix — and it attaches only where the rule giving
the affix did NOT state a sense of its own: तत्र येष्वर्थादेशो नास्ति
तत्रेदमुपतिष्ठते, अर्थाकाङ्क्षत्वात्. A heading that fills gaps rather
than covering ground, which no अधिकार met before this did.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from src.astadhyayi.upapada_krt import Added, NotAdded

#: The कृत्य affixes and those of like sense, which 3.4.70 holds to
#: the act and the object. क्त and the खल्-sense affixes go with them.
KRTYA_LIKE: Tuple[str, ...] = ("kṛtya", "kta", "khal", "khaṇ", "khac")

#: What a लकार may denote, in the order 3.4.69 gives them: कर्मन् by
#: the rule, कर्तृ by its first च, भाव after an intransitive root, and
#: कर्तृ again by its second च.
LAKARA_DENOTES: Tuple[str, ...] = ("karman", "kartṛ")
LAKARA_DENOTES_AKARMAKA: Tuple[str, ...] = ("bhāva", "kartṛ")


@dataclass(frozen=True)
class Denotes:
    """One rule saying what an affix stands for."""

    sutra: str
    #: What the affix denotes. More than one where a च adds to it.
    means: Tuple[str, ...]
    #: The affixes the rule speaks of. Empty means every कृत् affix.
    of: Tuple[str, ...] = ()
    #: 3.4.69's अकर्मकेभ्यः — only after an intransitive root.
    akarmaka: object = None
    #: 3.4.71's आदिकर्मणि — the affix was given for the FIRST MOMENT
    #: of the act.
    adikarman: bool = False
    #: Whether the rule giving the affix stated a sense of its own.
    #: 3.4.67 attaches only where it did not.
    fills_a_gap: bool = False
    #: The senses of root a rule holds itself to. 3.4.72 wants
    #: motion, 3.4.76 fixity, motion or consuming.
    root_sense: Tuple[str, ...] = ()
    #: 3.4.75 speaks of the उणादि words. It shares its SUBJECT
    #: with 3.3.1 and not its question — that rule asks whether
    #: the word stands, this asks what it denotes — so the two
    #: answer from different entry points.
    unadi: bool = False
    why: str = ""


DENOTES: Tuple[Denotes, ...] = (
    Denotes(
        "3.4.67", ("kartṛ",), fills_a_gap=True,
        why="कर्तरि कृत् — कारकः, कर्ता, नन्दनः, ग्राही, पचः. A "
            "HEADING, and the vṛtti says what kind: "
            "कृदुत्पत्तिवाक्यानामयं शेषः, the remainder of every rule "
            "that gives a कृत् affix.\n\n"
            "AND IT ATTACHES ONLY WHERE THERE IS A GAP. तत्र येष्वर्थ"
            "आदेशो नास्ति तत्रेदमुपतिष्ठते, अर्थाकाङ्क्षत्वात् — it "
            "stands where the rule giving the affix stated NO sense, "
            "because only there is a sense still wanted; न "
            "ख्युन्नादिवाक्येषु, साक्षादर्थनिर्देशे सति तेषां "
            "निराकाङ्क्षत्वात्, and not where one was stated "
            "outright. A heading that FILLS GAPS rather than covering "
            "ground — 3.2.84, 3.3.18 and 3.3.19 all covered every "
            "rule under them"),
    Denotes(
        "3.4.69", LAKARA_DENOTES, of=("la",), akarmaka=False,
        why="लः कर्मणि च भावे चाकर्मकेभ्यः — गम्यते ग्रामो "
            "देवदत्तेन for the object, गच्छति ग्रामं देवदत्तः for the "
            "doer by the first च.\n\n"
            "THIS IS WHAT A लकार DENOTES, and the project has been "
            "carrying the question since 3.2.110: that table names "
            "its endings as bare strings and nothing could ask what "
            "one of them IS.\n\n"
            "ल इत्युत्सृष्टानुबन्धं सामान्यं गृह्यते, "
            "प्रथमाबहुवचनान्तं चैतत् — the ल is taken WITHOUT its "
            "markers and as a plural, so the rule speaks of all ten "
            "लकार at once and not of any one. That is why a single "
            "rule can answer for लट्, लङ्, लिट्, लुङ् and the rest "
            "alike"),
    Denotes(
        "3.4.69", LAKARA_DENOTES_AKARMAKA, of=("la",), akarmaka=True,
        why="लः कर्मणि च भावे चाकर्मकेभ्यः — the second half. "
            "अकर्मकेभ्यो धातुभ्यो भावे भवन्ति, पुनश्चकारात् कर्तरि "
            "च: आस्यते देवदत्तेन for the act, आस्ते देवदत्तः for the "
            "doer.\n\n"
            "AND THE TWO HALVES DO NOT OVERLAP: सकर्मकेभ्यो भावे न "
            "भवन्ति — after a transitive root a लकार never denotes "
            "the act. So transitivity partitions what the ending can "
            "stand for, which is why the row is split in two rather "
            "than listing three senses at once"),
    Denotes(
        "3.4.70", ("bhāva", "karman"), of=KRTYA_LIKE, akarmaka=None,
        why="तयोरेव कृत्यक्तखलर्थाः — कर्तव्यः कटो भवता and भोक्तव्य "
            "ओदनो भवता for the object; आसितव्यं भवता and शयितव्यं "
            "भवता for the act. And so for क्त — कृतः कटो भवता, आसितं "
            "भवता — and for the खल्-sense affixes, ईषत्करः कटो भवता, "
            "ईषदाढ्यंभवं भवता.\n\n"
            "एवकारः कर्तुरपकर्षणार्थः — the एव is there to PULL THE "
            "DOER AWAY, which 3.4.67's heading would otherwise have "
            "supplied. A word spent to undo a heading for one class "
            "of affixes.\n\n"
            "भावे चाकर्मकेभ्य इत्यनुवृत्तेः सकर्मकेभ्यो भावे न भवन्ति "
            "— 3.4.69's restriction carries down, so these too fail "
            "to denote the act after a transitive root"),
    Denotes(
        "3.4.71", ("kartṛ", "bhāva", "karman"), of=("kta",),
        adikarman=True,
        why="आदिकर्मणि क्तः कर्तरि च — प्रकृतः कटं देवदत्तः, he has "
            "begun the mat; and चकाराद् यथाप्राप्तं भावकर्मणोः, so "
            "प्रकृतः कटो देवदत्तेन and प्रकृतं देवदत्तेन stand too.\n\n"
            "आदिभूतः क्रियाक्षण आदिकर्म — the FIRST MOMENT of the "
            "act, तस्मिन्नादिकर्मणि भूतत्वेन विवक्षिते: and the "
            "beginning is spoken of AS PAST, which is what lets a "
            "past affix denote it. A rule that turns on how a moment "
            "is meant rather than on when it was"),
    Denotes(
        "3.4.72", ("kartṛ", "bhāva", "karman"), of=("kta",),
        root_sense=("gati", "śliṣādi"),
        why="गत्यर्थाकर्मकश्लिषशीङ्स्थासवसजनरुहजीर्यतिभ्यश्च — गतो "
            "देवदत्तो ग्रामम् for the doer, गतो देवदत्तेन ग्रामः and "
            "गतं देवदत्तेन by the च. And for each of the eight named "
            "roots the vṛtti gives all three: उपश्लिष्टो गुरुं भवान्, "
            "उपश्लिष्टो गुरुर्भवता, उपश्लिष्टं भवता.\n\n"
            "श्लिषादयः सोपसर्गाः सकर्मका भवन्ति, तदर्थमेषामुपादानम् — "
            "those eight take an object ONLY with a preverb, and that "
            "is why they are named: without one they would already be "
            "reached by अकर्मक. A list justified by what its members "
            "become rather than by what they are"),
    Denotes(
        "3.4.76", ("adhikaraṇa", "kartṛ", "bhāva", "karman"),
        of=("kta",),
        root_sense=("dhrauvya", "gati", "pratyavasāna"),
        why="ध्रौव्यगतिप्रत्यवसानार्थेभ्यश्च — आसितो देवदत्तः, आसितं "
            "तेन, इदमेषामासितम्: the last is the LOCUS, this is the "
            "place they sat. चकाराद् यथाप्राप्तं च, so the earlier "
            "senses stand too.\n\n"
            "AND THE THREE ROOT-SENSES REACH DIFFERENT SETS. "
            "ध्रौव्यार्थेभ्यः कर्तृभावाधिकरणेषु, गत्यर्थेभ्यः "
            "कर्तृकर्मभावाधिकरणेषु, प्रत्यवसानार्थेभ्यः "
            "कर्मभावाधिकरणेषु — three, four and three respectively, "
            "and the rule states none of it.\n\n"
            "SCOPE — कथं भुक्ता ब्राह्मणाः, पीता गाव इति? अकारो "
            "मत्वर्थीयः, भुक्तमेषामस्ति — the brahmins who HAVE eaten, "
            "the cows that HAVE drunk, the ending read as a "
            "possessive rather than as this affix at all. A form "
            "saved by parsing it as something else, which 3.2.53 and "
            "3.3.24 also did"),
    Denotes(
        "3.4.75", ("karman", "karaṇa", "adhikaraṇa"), unadi=True,
        why="ताभ्यामन्यत्रोणादयः — कृषितोऽसौ कृषिः, तनित इति तन्तुः, "
            "वृत्तमिति वर्त्म, चरितं चर्म: the उणादि words denote a "
            "kāraka OTHER than the two just named. "
            "कृत्त्वात् कर्तर्येव प्राप्ताः कर्मादिषु कथ्यन्ते — "
            "3.4.67 would have given them the doer.\n\n"
            "AND ONE WORD REACHES THE FARTHER OF TWO NEIGHBOURS. "
            "ताभ्यामिति संप्रदानप्रत्यवमर्शार्थम्, अन्यथा "
            "ह्यपादानमेव पर्युदस्येत, अनन्तरत्वात् — without it only "
            "the NEARER of the two would be excluded, being adjacent. "
            "3.4.32's अस्य was spent on the same kind of question.\n\n"
            "वर्त्म and चर्म are 3.3.2's own examples: that rule said "
            "they may be SEEN in the past, this says what they "
            "DENOTE. Two halves of one question a pāda and a half "
            "apart, and both codified — but not the same question, "
            "which is why they answer from different places"),
)

#: 3.4.68 — words fixed as denoting the doer where the rules would
#: have given the act or the object.
NIPATANA: Dict[str, Tuple[str, str, str]] = {
    "dāśa": (
        "3.4.73", "sampradāna",
        "दाशगोघ्नौ संप्रदाने — दाशन्ति तस्मा इति दाशः. दाशृ दाने, "
        "ततः पचाद्यच्; स कृत्संज्ञकत्वात् कर्तरि प्राप्तः, संप्रदाने "
        "निपात्यते — 3.4.67 would have made it the doer, and the "
        "fixing puts it in the case of the RECIPIENT instead.",
    ),
    "goghna": (
        "3.4.73", "sampradāna",
        "आगताय तस्मै दातुं गां घ्नन्तीति गोघ्नः, अर्घार्होऽतिथिः — a "
        "guest, one for whom a cow is killed. टगत्र निपात्यते.\n\n"
        "AND THE FIXING ITSELF NARROWS WHO IS MEANT. "
        "निपातनसामर्थ्यादेव गोघ्न ऋत्विगादिरुच्यते, न तु चण्डालादिः "
        "— on the strength of the fixing alone the word means a "
        "priest and not an outcaste. And असत्यपि च गोहनने तस्य "
        "योग्यतया गोघ्न इत्यभिधीयते: it is said even where no cow is "
        "killed, on the strength of his DESERVING it. A word whose "
        "sense has outrun its parts, and the commentary says so.",
    ),
    "bhīma": (
        "3.4.74", "apādāna",
        "भीमादयोऽपादाने — भीमः, भीष्मः, भयानकः, वरुः, चरुः, भूमिः, "
        "रजः, संस्कारः, संक्रन्दनः, प्रपतनः, समुद्रः, स्रुवः, स्रुक्, "
        "खलतिः.\n\n"
        "उणादिप्रत्ययान्ता एते — they are formed with उणादि affixes, "
        "and the vṛtti cites the उणादिपाठ by number: श्याधूसूभ्यो "
        "मक् (प०उ० १.१४५), भियः षुग् वा (प०उ० १.१४८). That text is "
        "on disk and 3.3.1 reads it.\n\n"
        "ताभ्यामन्यत्रोणादयः इति पर्युदासे प्राप्ते निपातनम् "
        "आरभ्यते — 3.4.75 will EXCLUDE this very case, so these are "
        "fixed before the exclusion is stated. A निपातन written to "
        "survive a rule that has not been given yet.",
    ),
    "bhavya": (
        "3.4.68", "kartṛ",
        "भव्यगेयप्रवचनीयोपस्थानीयजन्याप्लाव्यापात्या वा — भवत्यसौ "
        "भव्यः, भव्यमनेनेति वा. तयोरेव कृत्यक्तखलर्थाः इति "
        "भावकर्मणोः प्राप्तयोः कर्ता च वाच्यः पक्ष उच्यते: 3.4.70 "
        "would have held them to the act and the object, and here "
        "the DOER is allowed as an alternative — वा, so both "
        "readings stand.",
    ),
    "geya": (
        "3.4.68", "kartṛ",
        "गेयो माणवकः साम्नाम्, गेयानि माणवकेन सामानीति वा — the boy "
        "who sings the chants, or the chants to be sung by the boy. "
        "One word read both ways, and the rule licenses the first.",
    ),
    "pravacanīya": (
        "3.4.68", "kartṛ",
        "प्रवचनीयो गुरुः स्वाध्यायस्य, प्रवचनीयो गुरुणा स्वाध्याय "
        "इति वा.",
    ),
    "upasthānīya": (
        "3.4.68", "kartṛ",
        "उपस्थानीयोऽन्तेवासी गुरोः, उपस्थानीयः शिष्येण वा गुरुः — "
        "the pupil who attends on the teacher, or the teacher to be "
        "attended on.",
    ),
    "janya": ("3.4.68", "kartṛ",
              "जायतेऽसौ जन्यः, जन्यमनेनेति वा."),
    "āplāvya": ("3.4.68", "kartṛ",
                "आप्लवतेऽसावाप्लाव्यः, आप्लाव्यमनेनेति वा."),
    "āpātya": ("3.4.68", "kartṛ",
               "आपतत्यसावापात्यः, आपात्यमनेनेति वा."),
}


def denotes(affix: str = "", *, akarmaka: bool = False,
            adikarman: bool = False, root_sense: str = "",
            unadi: bool = False,
            sense_stated: bool = False) -> object:
    """
    3.4.67 and 3.4.69 to 3.4.71 — what an affix stands for.

    A different question from every rule before it, which asked WHICH
    affix comes. Pass `affix="la"` for a tense-ending — the rule takes
    ल without its markers and as a plural, so one statement answers
    for every लकार.

    `sense_stated` says whether the rule that GAVE the affix named a
    sense of its own. 3.4.67's heading attaches only where it did not:
    तत्र येष्वर्थादेशो नास्ति तत्रेदमुपतिष्ठते.
    """
    matched = [row for row in DENOTES
               if (not row.of or affix in row.of)
               and (row.akarmaka is None
                    or bool(row.akarmaka) == akarmaka)
               and (not row.adikarman or adikarman)
               and (not row.root_sense
                    or root_sense in row.root_sense)
               and (not row.unadi or unadi)
               and (not row.fills_a_gap or not sense_stated)]
    if not matched:
        if affix and sense_stated:
            return NotAdded(
                "3.4.67",
                "कर्तरि कृत् attaches only where the rule giving the "
                "affix stated NO sense of its own — तत्र येष्वर्थादेशो "
                "नास्ति तत्रेदमुपतिष्ठते, अर्थाकाङ्क्षत्वात्. Here one "
                "was stated, so the heading has nothing to supply")
        return NotAdded(
            "",
            "No rule of 3.4.67 to 3.4.71 says what that affix "
            "denotes. A कृत् affix denotes the doer by 3.4.67 where "
            "its own rule named no sense; a लकार the object or the "
            "act by 3.4.69; and the कृत्य affixes with क्त the act "
            "and the object by 3.4.70")
    best = max(matched, key=_how_specific)
    return Added(", ".join(best.means), best.sutra, best.why)


def _how_specific(row: Denotes) -> int:
    """How much a row states."""
    return (3 * (len(row.of) > 0) + 2 * row.adikarman
            + 3 * (len(row.root_sense) > 0) + 3 * row.unadi
            + (row.akarmaka is not None) + row.fills_a_gap)


def nipatana(word: str = "") -> object:
    """
    3.4.68 भव्यगेयप्रवचनीय… — seven words allowed to denote the DOER
    where 3.4.70 would have held them to the act and the object.

    The rule carries वा, so both readings stand: गेयो माणवकः साम्नाम्
    and गेयानि माणवकेन सामानि alike. Each entry says which two.
    """
    entry = NIPATANA.get(word)
    if entry is None:
        return NotAdded(
            "",
            "3.4.68 fixes seven words as able to denote the doer: "
            + ", ".join(sorted(NIPATANA)))
    sutra, means, why = entry
    return Added(means, sutra, why)


def lakara_denotes(*, akarmaka: bool = False) -> Tuple[str, ...]:
    """
    What a tense-ending stands for — the answer 3.2.110's table could
    not ask for until now.

    After a transitive root: the object, or the doer. After an
    intransitive one: the act, or the doer. The two do not overlap —
    सकर्मकेभ्यो भावे न भवन्ति — so transitivity partitions it.
    """
    return (LAKARA_DENOTES_AKARMAKA if akarmaka else LAKARA_DENOTES)
