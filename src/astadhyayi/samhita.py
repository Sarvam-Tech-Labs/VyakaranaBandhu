# -*- coding: utf-8 -*-
"""
६.१.७२–८३ — संहितायाम्, and two headings inside one another.

**संहितायाम्** opens the longest stretch of the pāda. Everything from
6.1.72 to 6.1.157 holds only where two sounds are spoken in an
unbroken flow — **संहितायामिति किम्? दधि अत्र, मधु अत्र**. Speak
them apart and no rule of eighty-six fires.

And five sūtras later a SECOND heading opens inside it. 6.1.77's
vṛtti: **अचीति चायमधिकारः संप्रसारणाच्च इति यावत्** — the word *before
a vowel* governs from 6.1.77 to 6.1.108. Both are bounded the same
way, by the words of the rule each stops before: संहिता by
**अनुदात्तं पदमेकवर्जम्** at 6.1.158, and अचि by **संप्रसारणाच्च**
at 6.1.108 — which is a member. Two headings, two kinds of bound.

**AND A RULE FIXES WHAT A LATER RULE WILL MAKE OPTIONAL.** 6.1.74's
vṛtti says outright: **पदान्ताद् वा इति विकल्पे प्राप्ते नित्यं
तुगागमो भवति** — the augment is obligatory for आङ् and माङ् against
an option 6.1.76 has not yet stated. An अपवाद pointing forward, which
the project met once before at 5.1.21.

**AND THE AUGMENT ATTACHES TO A SOUND, NOT TO A WORD.** 6.1.73:
**ह्रस्व एवात्रागमी, न तु तदन्तः** — the short VOWEL takes the तुक्,
not the portion ending in it. So in **चिच्छिदतुः** the त् is not part
of the copy चि, and 7.4.60's हलादिः शेषः does not strike it out:
**नावयवावयवः समुदायावयवो भवति**, a part of a part is not a part of
the whole.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule of 6.1.72–83
acts and what it puts in. It does not join the two words: turning
दधि + अत्र into दध्यत्र needs the substitution actually performed,
and 8.4.40's श्चुत्व turns 6.1.73's त् into च्. Neither is codified.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where संहितायाम् governs. 6.1.72's vṛtti bounds it by the words of
#: the rule it stops before: **अधिकारोऽयम् अनुदात्तं पदमेकवर्जम् इति
#: यावत्** — so the run ends at 6.1.157 and 6.1.158 is the marker.
SAMHITA_RUN: Tuple[str, str] = ("6.1.72", "6.1.157")
SAMHITA_MARKER: str = "6.1.158"

#: And the heading that opens inside it, five sūtras later. 6.1.77:
#: **अचीति चायमधिकारः संप्रसारणाच्च इति यावत्** — and here the rule
#: named is a MEMBER of the run, as 6.1.57 was of the आकार.
ACI_RUN: Tuple[str, str] = ("6.1.77", "6.1.108")
ACI_MARKER: str = "6.1.108"

#: The four senses आङ् carries at 6.1.74, which is what the ङित्
#: picks out: **ईषदर्थे, क्रियायोगे, मर्यादायाम्, अभिविधौ**. Read
#: without them, आ छाया would fall under the option of 6.1.76.
ANG_SENSES: Tuple[str, ...] = (
    "īṣad", "kriyāyoga", "maryādā", "abhividhi",
)

#: What a part of a part is not. Cited at 6.1.73 to keep 7.4.60 off
#: the augment.
NAVAYAVA: str = "नावयवावयवः समुदायावयवो भवति"


@dataclass(frozen=True)
class Junction:
    """One rule of 6.1.72–83: what happens where two sounds meet."""

    sutra: str
    #: What the rule does: tuk, yaṇ, vānta, nipātana, or nothing
    #: where it is only a heading or a restriction.
    does: str = ""
    #: The words or roots the rule names.
    of: Tuple[str, ...] = ()
    #: What follows — छ, a vowel, a य-initial affix, यत्.
    before: str = ""
    #: What precedes — a short vowel, a long one, a long one at the
    #: end of a पद.
    after: str = ""
    #: The sense the form must carry — शक्य at 6.1.81, तदर्थ at
    #: 6.1.82.
    result: str = ""
    #: What is put in or put in place.
    gives: str = ""
    #: True where the rule only NARROWS one before it and supplies
    #: nothing of its own — 6.1.80.
    restricts: Tuple[str, ...] = ()
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    heading: bool = False
    #: The rule this one displaces or fixes, by ITS own number.
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


SAMHITA_TABLE: Tuple[Junction, ...] = (
    Junction(
        "6.1.72", heading=True,
        keeps_out="दधि अत्र, मधु अत्र — spoken apart, and no rule of "
                  "the eighty-six fires",
        why="संहितायाम् — **अधिकारोऽयम् अनुदात्तं पदमेकवर्जम् इति "
            "यावत्।  प्रागेतस्मात् सूत्रादित उत्तरं यद् वक्ष्यामः "
            "संहितायामित्येवं तद् वेदितव्यम्** — everything from here "
            "to 6.1.157 holds only where the two sounds are spoken "
            "in one unbroken flow.\\n\\n"
            "**AND THE CONDITION IS SHOWN BY WHAT FAILS IT.** "
            "**वक्ष्यति इको यणचि — दध्यत्र, मध्वत्र। संहितायामिति "
            "किम्? दधि अत्र, मधु अत्र** — the same two words, and "
            "with a pause between them nothing happens at all. The "
            "longest heading of the pāda, and its condition is not "
            "a grammatical category but a manner of speaking"),
    Junction(
        "6.1.73", does="tuk", before="cha", after="hrasva", gives="tuk",
        why="छे च — a short vowel takes the augment तुक् before छ, "
            "and ह्रस्वस्य तुक् carries down from 6.1.71: "
            "**इच्छति, यच्छति**. 8.4.40 then makes the त् a च्.\\n\\n"
            "**AND WHAT TAKES THE AUGMENT IS THE VOWEL, NOT THE WORD "
            "ENDING IN IT.** **ह्रस्व एवात्रागमी, न तु तदन्तः** — "
            "and the difference is visible in **चिच्छिदतुः, "
            "चिच्छिदुः**, where the त् survives. Being an augment of "
            "the इ, it is not part of the copy चि, so 7.4.60's "
            "हलादिः शेषः has nothing to strike: "
            "**नावयवावयवः समुदायावयवो भवति** — a part of a part is "
            "not a part of the whole"),
    Junction(
        "6.1.74", does="tuk", of=("āṅ", "māṅ"), before="cha",
        gives="tuk", blocks=("6.1.76",),
        keeps_out="आ छाया, प्रमा छन्दः — the आ of recollection and "
                  "the प्रमा of 3.3.106 are neither आङ् nor माङ्",
        why="आङ्माङोश्च — for आङ् in its four senses and for the "
            "prohibitive माङ्, the augment before छ: **ईषच्छाया, "
            "आच्छादयति, आच्छायम्; माच् छैत्सीत्, माच् छिदत्**.\\n\\n"
            "**AND THE RULE FIXES WHAT A LATER RULE WILL LOOSEN.** "
            "**पदान्ताद् वा इति विकल्पे प्राप्ते नित्यं तुगागमो "
            "भवति** — 6.1.76 has not been stated yet and would make "
            "the augment a choice after a पदान्त long vowel; this "
            "rule says it is fixed for these two. An अपवाद pointing "
            "FORWARD.\\n\\n"
            "**AND THE ङ् OF आङ् AND माङ् IS WHAT NARROWS THEM.** "
            "**ङिद्विशिष्टग्रहणं किम्? आ छाया, आच् छाया। प्रमा "
            "छन्दः, प्रमाच् छन्दः** — the आ of recollection and the "
            "noun प्रमा are not the आङ् and माङ् the rule names, so "
            "for them the augment falls back to 6.1.76's option"),
    Junction(
        "6.1.75", does="tuk", before="cha", after="dīrgha", gives="tuk",
        why="दीर्घात् — a long vowel too: **ह्रीच्छति, म्लेच्छति, "
            "अपचाच्छायते, विचाच्छायते**. And the augment belongs to "
            "the long vowel itself, on the same reading 6.1.73 was "
            "given — **पूर्वस्य तस्यैव दीर्घस्य**"),
    Junction(
        "6.1.76", does="tuk", before="cha", after="padānta-dīrgha",
        gives="tuk", optional=True,
        why="पदान्ताद् वा — where the long vowel ends a पद the "
            "augment is a choice: **कुटीच्छाया, कुटीछाया; "
            "कुवलीच्छाया, कुवलीछाया**.\\n\\n"
            "**AND THIS IS A पदान्त RULE AND NOT A पदविधि.** The "
            "augment attaches at the end of a पद, so 2.1.1's "
            "समर्थः पदविधिः does not apply and the two words need "
            "not be construed together at all: **तिष्ठतु "
            "कुमारीच्छत्रं हर देवदत्तस्य** takes the augment though "
            "कुमारी and छत्रम् belong to different clauses.\\n\\n"
            "**AND A SUPPLEMENT ADDS A VEDIC LIST.** "
            "**विश्वजनादीनां छन्दसि वा तुगागमो भवतीति वक्तव्यम्** — "
            "**विश्वजनच्छत्रम्, विश्वजनछत्रम्**"),
    Junction(
        "6.1.77", does="yaṇ", before="ac", gives="yaṇ", heading=True,
        keeps_out="कुमारीन्द्रः — the vowels are savarṇa, and 6.1.101 "
                  "lengthens instead",
        why="इको यणचि — an इक् becomes the matching semivowel before "
            "a vowel: **दध्यत्र, मध्वत्र, कर्त्रर्थम्, हर्त्रर्थम्, "
            "लाकृतिः**.\\n\\n"
            "**AND A SECOND HEADING OPENS HERE, INSIDE THE FIRST.** "
            "**अचीति चायमधिकारः संप्रसारणाच्च इति यावत्** — the word "
            "*before a vowel* governs from here to 6.1.108. संहिता "
            "is bounded by the words of a rule OUTSIDE its run; this "
            "one by the words of a rule that is a member of it, as "
            "6.1.45's आकार was bounded by 6.1.57.\\n\\n"
            "**AND A SUPPLEMENT GIVES IT PRECEDENCE OVER THE "
            "LENGTHENING.** **इकः प्लुतपूर्वस्य सवर्णदीर्घबाधनार्थं "
            "यणादेशो वक्तव्यः** — after a प्लुत vowel the semivowel "
            "wins even where the two are savarṇa: **भो३ इ इन्द्रम्** "
            "gives **भो३यिन्द्रम्**"),
    Junction(
        "6.1.79", does="vānta", before="ya-pratyaya", gives="av-āv",
        keeps_out="रैयति — ऐ is not one of the two that end in व्; "
                  "गोभ्याम्, नौभ्याम् — no य्; गोयानम्, नौयानम् — "
                  "य् but no affix",
        why="वान्तो यि प्रत्यये — of the four substitutes 6.1.78 "
            "gives for an एच्, the two that END in व् — अव् and "
            "आव् — come also before an affix beginning with य्: "
            "**बाभ्रव्यः, माण्डव्यः, शङ्कव्यं दारु, पिचव्यः "
            "कार्पासः, नाव्यो ह्रदः**.\\n\\n"
            "**AND WHICH TWO ARE MEANT IS SETTLED BY THE SHAPE OF "
            "THE WORD.** Naming the substitutes that end in व् is "
            "how the rule names the vowels they replace, ओ and औ, "
            "without naming them.\\n\\n"
            "**AND TWO SUPPLEMENTS ADD गो BEFORE यूति.** "
            "**गोर्यूतौ छन्दसि** — **गव्यूतिमुक्षतम्** in the "
            "corpus, गोयूतिः outside it; and **अध्वपरिमाणे च** — "
            "**गव्यूतिमात्रमध्वानं गतः**, where the word is a "
            "measure of road"),
    Junction(
        "6.1.80", restricts=("6.1.79",), before="ya-pratyaya",
        keeps_out="उपोयते, औयत, लौयमानिः, पौयमानिः — the ओ and औ "
                  "there were not caused by the य-affix",
        why="धातोस्तन्निमित्तस्यैव — and the rule supplies nothing. "
            "It NARROWS 6.1.79: for a ROOT, the substitution holds "
            "only where the diphthong was itself brought about by "
            "that य-affix. **लव्यम्, पव्यम्; अवश्यलाव्यम्, "
            "अवश्यपाव्यम्** — लू takes यत्, the affix causes the "
            "guṇa, and the ओ so produced becomes अव्.\\n\\n"
            "**AND धातोः IS SAID SO THAT A STEM IS LEFT ALONE.** "
            "**धातोरिति किम्? प्रातिपदिकस्य नियमो मा भूत्। तत्र को "
            "दोषः? बाभ्रव्य इत्यत्रैव स्यात्, इह न स्याद् गव्यं "
            "नाव्यम्** — गो and नौ have their diphthongs from the "
            "start, and a restriction reaching stems would lose "
            "both.\\n\\n"
            "**AND THE एवकार RESTRICTS THE ROOT, NOT THE CAUSE.** "
            "**एवकारकरणं किम्? धात्ववधारणं यथा स्यात्, "
            "तन्निमित्तावधारणं मा भूत्। तन्निमित्तस्य हि धातोश्चा"
            "धातोश्च भवति** — read the other way it would say *only "
            "what the affix caused*, and बाभ्रव्यः would be lost. "
            "One word, two readings, and the wrong one loses a form "
            "the right one keeps"),
    Junction(
        "6.1.81", does="nipātana", of=("kṣi", "ji"), before="yat",
        result="śakya", gives="ay", nipatana=True,
        keeps_out="क्षेयं पापम्, जेयो वृषलः — there the sense is "
                  "what MUST be done, not what CAN be",
        why="क्षय्यजय्यौ शक्यार्थे — two forms laid down whole, with "
            "अय् for the ए before यत्, and only where the sense is "
            "*able to be*: **शक्यः क्षेतुं क्षय्यः, शक्यो जेतुं "
            "जय्यः**. Where the sense is obligation the ordinary "
            "forms stand"),
    Junction(
        "6.1.82", does="nipātana", of=("krī",), before="yat",
        result="tadartha", gives="ay", nipatana=True,
        keeps_out="क्रेयं नो धान्यम् — corn we mean to buy, which is "
                  "not corn put out for sale",
        why="क्रय्यस्तदर्थे — the same substitution for क्री, and "
            "only in the sense of being put out FOR that, for "
            "buying: **क्रय्यो गौः, क्रय्यः कम्बलः**, and the vṛtti "
            "glosses it **क्रयार्थं यः प्रसारितः, स उच्यते**. "
            "**क्रेयं नो धान्यम्, न चास्ति क्रय्यम्** sets the two "
            "senses against each other in one sentence"),
    Junction(
        "6.1.83", does="nipātana", of=("bhī", "vī"), before="yat",
        gives="ay", nipatana=True, chandasi=True,
        keeps_out="भेयम्, प्रवेयम् — in ordinary speech",
        why="भय्यप्रवय्ये च छन्दसि — two more laid down, for the "
            "corpus: **भय्यं किलासीत्; वत्सतरी प्रवय्या**.\\n\\n"
            "**AND EACH CARRIES AN ODDITY OF ITS OWN.** भय्यम् takes "
            "its यत् in the ABLATIVE sense by 3.3.113's "
            "कृत्यल्युटो बहुलम् — **बिभेत्यस्मादिति भय्यम्**, that "
            "from which one fears. And **प्रवय्या इति स्त्रियामेव "
            "निपातनम्** — the form is laid down in the feminine "
            "alone, प्रवेयम् standing elsewhere.\\n\\n"
            "**AND A SUPPLEMENT ADDS A THIRD.** "
            "**ह्रदय्या आप उपसंख्यानम्** — **ह्रदय्या आपः**, water "
            "of a pool, with 4.4.110's यत्"),
)


@dataclass(frozen=True)
class Joined:
    """What the resolver answers with."""

    does: str
    sutra: str
    why: str
    gives: str = ""
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    #: Where a rule fixes or displaces another, that rule's number.
    blocked_by: Tuple[str, ...] = ()
    #: The rules that NARROW the one that answered, each with its own
    #: number. 6.1.80 supplies nothing and so is never the answer;
    #: it is reported here on 6.1.79's, which is where it bites.
    narrowed_by: Tuple[str, ...] = ()


def _reaches(row: Junction, stem: str, before: str, after: str,
             result: str, chandasi: bool) -> bool:
    # A heading that also states a rule stays in play — 6.1.77 is
    # both, as 6.1.45 was. One that states none does not: 6.1.72 has
    # no condition of its own and would otherwise match every
    # question ever asked.
    if row.heading and not row.does:
        return False
    # A row that only NARROWS another supplies nothing, so it is
    # never the answer. 6.1.80 is reported on `narrows` instead.
    if row.restricts:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.of and stem not in row.of:
        return False
    if row.before and before != row.before:
        return False
    if row.after and after != row.after:
        return False
    if row.result and result != row.result:
        return False
    return True


def _supplies(row: Junction, wants: str) -> bool:
    return not wants or wants == row.does


def _how_specific(row: Junction) -> int:
    """
    A named word beats a condition on the shape of the sounds.

    What precedes counts above what follows, because the three तुक्
    rules share their `before` exactly — छ — and are told apart by
    nothing else: 6.1.73 by a short vowel, 6.1.75 by a long one,
    6.1.76 by a long one ending a पद.
    """
    return (
        8 * bool(row.of)
        + 5 * bool(row.result)
        + 4 * bool(row.after)
        + 3 * bool(row.before)
    )


def joins(stem: str = "", *, before: str = "", after: str = "",
          result: str = "", chandasi: bool = False,
          wants: str = "") -> Joined:
    """
    6.1.72–83 — what happens where two sounds meet in संहिता.

    Every answer here is conditional on the two being spoken
    together: 6.1.72 is a heading and supplies nothing, so what
    escapes the rules escapes the section, and speaking the words
    apart takes all eighty-six rules away at once.
    """
    matched = [
        row for row in SAMHITA_TABLE
        if _reaches(row, stem, before, after, result, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Joined(
            "", "", "No rule of 6.1.72–83 is reached. 6.1.72 is a "
                    "heading and supplies nothing — it states the "
                    "condition every rule to 6.1.157 is read under, "
                    "not an operation")
    row = max(matched, key=_how_specific)
    narrowed = tuple(one.sutra for one in SAMHITA_TABLE
                     if row.sutra in one.restricts)
    return Joined(row.does, row.sutra, row.why, gives=row.gives,
                  optional=row.optional, chandasi=row.chandasi,
                  nipatana=row.nipatana, blocked_by=row.blocks,
                  narrowed_by=narrowed)


def samhita_run() -> Joined:
    """
    How far संहितायाम् governs, and the heading that opens inside it.

    **अधिकारोऽयम् अनुदात्तं पदमेकवर्जम् इति यावत्** for the first;
    **अचीति चायमधिकारः संप्रसारणाच्च इति यावत्** for the second.
    """
    opens, closes = SAMHITA_RUN
    inner_opens, inner_closes = ACI_RUN
    return Joined(
        "", opens,
        "संहितायाम् governs from %s to %s, bounded by the words of "
        "%s; and अचि opens inside it at %s and runs to %s, bounded "
        "by the words of %s — which is a MEMBER of its run where the "
        "outer marker is not"
        % (opens, closes, SAMHITA_MARKER, inner_opens, inner_closes,
           ACI_MARKER))


def provisions_for(sutra_id: str) -> Tuple[Junction, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SAMHITA_TABLE if row.sutra == sutra_id)
