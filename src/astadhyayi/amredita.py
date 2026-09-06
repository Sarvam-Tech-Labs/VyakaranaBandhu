# -*- coding: utf-8 -*-
"""
८.१.१–१५ — सर्वस्य द्वे, and the word said twice.

अध्याय ८ opens on a heading of two words. **सर्वस्येति च द्वे
इति च एतद् अधिकृतं वेदितव्यम्** — everything from 8.1.1 down to
just before 8.1.16 पदस्य is about a whole word being said twice
over. And the Kāśikā settles at once what the second copy IS:
**के द्वे भवतः? ये शब्दतश् च अर्थतश् च उभयथा अन्तरतमे** —
nearest in sound AND in sense, so that one पचति gives two, and
neither is a different word.

**WHAT IS DOUBLED, AND IN WHAT SENSE.** Almost every rule of the
run names a sense and not a form: constancy or distribution
(8.1.4 पचतिपचति, ग्रामोग्रामः), exclusion (8.1.5 परिपरि
त्रिगर्तेभ्यः), filling out a metrical quarter (8.1.6 प्रप्रायम्
अग्निः), nearness (8.1.7 उपर्युपरि), envy or approval or anger
or contempt or threat in a vocative (8.1.8 माणवक३ माणवक),
distress (8.1.10 गतगतः), a sort or likeness (8.1.12 पटुपटुः),
and ease (8.1.13 प्रियप्रियेण ददाति). The sense is the rule,
and the table has a column for it.

**AND THE SECOND COPY GETS A NAME AND AN ACCENT.** 8.1.2 तस्य
परमाम्रेडितम् calls the later of the two आम्रेडित and 8.1.3
अनुदात्तं च takes its accent away — which is what makes
भुङ्क्तेभुङ्क्ते one word to the ear rather than two.

**AND THE PAIR IS TOLD TO BEHAVE LIKE A COMPOUND — TWICE, AND
DIFFERENTLY.** 8.1.9 एकं बहुव्रीहिवत् and 8.1.10 आबाधे च make
their pairs act like a बहुव्रीहि; 8.1.11 कर्मधारयवद् उत्तरेषु
makes every pair after it act like a कर्मधारय instead. What that
buys is named in each place: **सुब्लोपपुंवद्भावौ** for the
first, and **सुब्लोपपुंवद्भावान्तोदात्तत्वानि** for the second
— which is how पटु plus पटु gives पटुपटुः and not *पटुःपटुः,
and how the feminine comes out पटुपट्वी.

**WHAT THIS MODULE DOES NOT DO.** It says what doubles and what
the pair counts as. The compound's own operations are अध्याय
२'s and the accent's are 6.1's; 8.1.16 पदस्य, which opens the
heading this run stops before, belongs to the next module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch — and the whole of the सर्वस्य द्वे
#: heading, which stops before 8.1.16.
DVE_RUN: Tuple[str, str] = ("8.1.1", "8.1.15")

#: Where the heading opened by 8.1.1 stops.
ADHIKARA_TO: str = "8.1.15"

#: 8.1.6's four, doubled only to fill out a metrical quarter.
PADA_PURANA: Tuple[str, ...] = ("pra", "sam", "upa", "ud")

#: 8.1.7's three, doubled of nearness in time or place.
SAMIPYA_THREE: Tuple[str, ...] = ("upari", "adhi", "adhas")

#: 8.1.8's five senses, all of them the speaker's and none of
#: them the thing spoken of — **एते च प्रयोक्तृधर्माः, न
#: अभिधेयधर्माः**.
AMANTRITA_FIVE: Tuple[str, ...] = (
    "asūyā", "sammati", "kopa", "kutsana", "bhartsana")

#: 8.1.15's five, in which द्वन्द्वम् is laid down.
DVANDVA_FIVE: Tuple[str, ...] = (
    "rahasya", "maryādāvacana", "vyutkramaṇa",
    "yajñapātraprayoga", "abhivyakti")


@dataclass(frozen=True)
class Dve:
    """One rule of 8.1.1–15: a doubling, a name, or an accent."""

    sutra: str
    #: `dve`, `saṃjñā`, `anudātta`, `nipātana`.
    does: str = ""
    #: The words named outright.
    of: Tuple[str, ...] = ()
    #: The word class instead.
    gana: str = ""
    #: The senses in which the rule speaks. Almost every rule
    #: here has one, and for most of them it is the whole rule.
    sense: Tuple[str, ...] = ()
    #: Where in the sentence the word must stand.
    position: str = ""
    #: What the doubled pair then counts as: `bahuvrīhi` by
    #: 8.1.9 and 8.1.10, `karmadhāraya` by 8.1.11's heading.
    like: str = ""
    #: True of a rule that only opens a heading. Nothing reaches
    #: one — 8.1.1 and 8.1.11 are both stated of everything that
    #: follows and of nothing in particular.
    heading: bool = False
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


DVE_TABLE: Tuple[Dve, ...] = (
    Dve(
        "8.1.1", does="dve", heading=True,
        why="सर्वस्य द्वे — the heading अध्याय ८ opens on: "
            "**सर्वस्येति च द्वे इति च एतद् अधिकृतं वेदितव्यम्। "
            "इत उत्तरं यद् वक्ष्यामः प्राक् पदस्य इत्यतः** — "
            "everything down to just before 8.1.16 is about a "
            "WHOLE word being said twice.\\n\\n"
            "**AND THE VṚTTI SETTLES AT ONCE WHAT THE TWO ARE.** "
            "**के द्वे भवतः? ये शब्दतश् च अर्थतश् च उभयथा "
            "अन्तरतमे** — nearest in sound and nearest in sense, "
            "both at once, so that **एकस्य पचतिशब्दस्य द्वौ "
            "पचतिशब्दौ भवतः**. Without that the substitution "
            "rule would let any word stand for any other. "
            "पचतिपचति; ग्रामोग्रामो रमणीयः.\\n\\n"
            "**AND सर्वस्य IS THE WORD THAT MAKES IT A WHOLE "
            "WORD.** The doubling of 6.1.1, which every "
            "reduplicated stem in अध्याय ७ came from, copies ONE "
            "syllable; this copies everything. The two rules "
            "share a name and nothing else"),
    Dve(
        "8.1.2", does="saṃjñā", gana="dvirukta-para",
        why="तस्य परमाम्रेडितम् — of what has been said twice, "
            "the LATER of the two is called आम्रेडित: **चौरचौर३, "
            "वृषलवृषल३, दस्योदस्यो३ घातयिष्यामि त्वा**. The name "
            "is what the next rule and 8.2.95 आम्रेडितं भर्त्सने "
            "speak to, and it is given to the second copy alone "
            "— the first stays an ordinary word"),
    Dve(
        "8.1.3", does="anudātta", gana="āmreḍita",
        why="अनुदात्तं च — and what is called आम्रेडित is "
            "अनुदात्त throughout: **भुङ्क्तेभुङ्क्ते, "
            "पशून्पशून्**. This is what makes a doubled word one "
            "thing to the ear rather than two: the second copy "
            "has no accent of its own left, so the pair carries "
            "a single high tone between them"),
    Dve(
        "8.1.4", does="dve", sense=("nitya", "vīpsā"),
        why="नित्यवीप्सयोः — a word doubles in the sense of "
            "CONSTANCY or of DISTRIBUTION: **पचतिपचति, "
            "जल्पतिजल्पति; भुक्त्वाभुक्त्वा व्रजति; "
            "लुनीहिलुनीहि इत्येवायं लुनाति**.\\n\\n"
            "**AND THE VṚTTI HAS TO SAY WHERE CONSTANCY CAN "
            "LIVE.** **केषु नित्यता? तिङ्षु नित्यता अव्ययकृत्सु "
            "च** — in finite verbs and in indeclinable kṛt "
            "forms, and the reason is that constancy is a "
            "property of an ACTION: **आभीक्ष्ण्यं च क्रियाधर्मः। "
            "यां क्रियां कर्ता प्राधान्येन अनुपरमन् करोति तन् "
            "नित्यम्** — what the agent goes on doing without "
            "stopping. वीप्सा wants a noun instead, and gives "
            "ग्रामोग्रामो रमणीयः"),
    Dve(
        "8.1.5", does="dve", of=("pari",), sense=("varjana",),
        keeps_out="ओदनं परिषिञ्चति — परि of pouring round and "
                  "not of leaving out",
        why="परेर्वर्जने — परि doubles in the sense of LEAVING "
            "OUT: **परिपरि त्रिगर्तेभ्यो वृष्टो देवः; परिपरि "
            "सौवीरेभ्यः; परिपरि सर्वसेनेभ्यः** — it rained "
            "everywhere except on the Trigartas. **वर्जनं "
            "परिहारः**.\\n\\n"
            "**AND A VĀRTTIKA MAKES IT OPTIONAL OUTSIDE A "
            "COMPOUND AND IMPOSSIBLE INSIDE ONE.** "
            "**परेर्वर्जनेऽसमासे वा इति वक्तव्यम्** — परि "
            "त्रिगर्तेभ्यः stands beside the doubled form; and "
            "in a compound it cannot come at all, **समासे तु "
            "तेनैव उक्तत्वाद् वर्जनस्य नैव भवति**, since "
            "परित्रिगर्तं वृष्टो देवः has already said the "
            "exclusion by compounding"),
    Dve(
        "8.1.6", does="dve", of=PADA_PURANA,
        sense=("pāda-pūraṇa",), chandasi=True,
        keeps_out="प्र देवं देव्या धिया — the quarter is full "
                  "without the doubling",
        why="प्रसमुपोदः पादपूरणे — प्र, सम्, उप and उद् double "
            "to FILL OUT a metrical quarter, and only if the "
            "doubling is what fills it: **द्विर्वचनेन चेत् पादः "
            "पूर्यते**. **प्रप्रायम् अग्निर् भरतस्य शृण्वे; "
            "संसमिद् युवसे वृषन्; उपोप मे परा मृश; किं नो दुदु "
            "हर्षसे दातवा उ**. The vṛtti reads the restriction "
            "to the Veda out of the rule's own sense rather "
            "than out of a word in it — **सामर्थ्यात् "
            "छन्दसि एव एतद् विधानम्**, since ordinary speech "
            "has no quarters to fill"),
    Dve(
        "8.1.7", does="dve", of=SAMIPYA_THREE,
        sense=("sāmīpya",),
        keeps_out="उपरि चन्द्रमाः — height and not nearness; "
                  "उपरि शिरसो घटं धारयति — above the head, "
                  "which is औत्तराधर्य and not प्रत्यासत्ति",
        why="उपर्यध्यधसः सामीप्ये — उपरि, अधि and अधस् double "
            "in the sense of NEARNESS: **उपर्युपरि दुःखम्; "
            "उपर्युपरि ग्रामम्; अध्यधि ग्रामम्; अधोऽधो "
            "नगरम्**. **सामीप्यं प्रत्यासत्तिः कालकृता देशकृता "
            "च** — nearness made by time or by place, either "
            "one. The pot held over the head is the sharpest "
            "counter-case: उपरि is there in its plain sense of "
            "ABOVE, and no doubling comes"),
    Dve(
        "8.1.8", does="dve", gana="āmantrita",
        position="vākya-ādi", sense=AMANTRITA_FIVE,
        why="वाक्यादेरामन्त्रितस्यासूयासम्मतिकोपकुत्सन"
            "भर्त्सनेषु — a VOCATIVE at the head of a sentence "
            "doubles in five senses: envy, approval, anger, "
            "contempt and threat. **माणवक३ माणवक, अभिरूपक३ "
            "अभिरूपक रिक्तं त आभिरूप्यम्** of envy.\\n\\n"
            "**AND ALL FIVE ARE THE SPEAKER'S AND NONE OF THEM "
            "THE THING SPOKEN OF.** **एते च प्रयोक्तृधर्माः, न "
            "अभिधेयधर्माः** — nothing about the boy makes the "
            "vocative double; what does is the mood of whoever "
            "is calling him. And वाक्य is defined for the "
            "occasion: **एकार्थः पदसमूहः वाक्यम्**, a group of "
            "words with one meaning"),
    Dve(
        "8.1.9", does="dve", of=("eka",), like="bahuvrīhi",
        why="एकं बहुव्रीहिवत् — एक said twice behaves like a "
            "बहुव्रीहि: **एकैकम् अक्षरं पठति; एकैकया आहुत्या "
            "जुहोति**. **बहुव्रीहिवत्त्वे प्रयोजनं "
            "सुब्लोपपुंवद्भावौ** — the case ending of the first "
            "member goes and the feminine reverts to the "
            "masculine, which is the whole of what the "
            "comparison buys.\\n\\n"
            "**AND THE LIKENESS IS NOT A MEMBERSHIP.** "
            "**सर्वनामसंज्ञाप्रतिषेधस्वरसमासान्ताः "
            "समासाधिकारविहिते बहुव्रीहौ विज्ञायन्ते। तेन "
            "आतिदेशिके बहुव्रीहौ न भवन्ति** — the pronoun "
            "refusal of 1.1.29, the accent and the compound "
            "endings belong to a real बहुव्रीहि and not to one "
            "made by a likeness, so एकैकस्मै keeps the pronoun "
            "ending"),
    Dve(
        "8.1.10", does="dve", sense=("ābādha",), like="bahuvrīhi",
        why="आबाधे च — and in the sense of DISTRESS: **गतगतः, "
            "नष्टनष्टः, पतितपतितः**, and in the feminine "
            "**गतगता, नष्टनष्टा, पतितपतिता**, the pair again "
            "behaving like a बहुव्रीहि. **आबाधनम् आबाधः, पीडा "
            "प्रयोक्तृधर्मः, न अभिधेयधर्मः** — the pain is the "
            "speaker's, as the five senses of 8.1.8 were: "
            "**प्रियस्य चिरगमनादिना पीड्यमानः कश्चिद् एवं "
            "प्रयुङ्क्ते**, someone worn down by a loved one's "
            "long absence says गतगतः"),
    Dve(
        "8.1.11", like="karmadhāraya", heading=True,
        why="कर्मधारयवद् उत्तरेषु — and from here on the "
            "doublings behave like a कर्मधारय instead: **इत "
            "उत्तरेषु द्विर्वचनेषु कर्मधारयवत् कार्यं भवति "
            "इत्येतद् वेदितव्यम्**. What it buys is one thing "
            "more than 8.1.9's likeness: **सुब्लोपपुंवद्भावान्त"
            "ोदात्तत्वानि** — the case ending goes (पटुपटुः, "
            "मृदुमृदुः), the feminine reverts (पटुपट्वी, "
            "कालककालिका), and the accent falls on the last "
            "syllable (पटुपटुः).\\n\\n"
            "**AND THE REVERSION REACHES A क-FINAL STEM "
            "BECAUSE OF THE LIKENESS AND NOT IN SPITE OF IT.** "
            "**कोपधाया अपि हि कर्मधारयवद्भावात् 6.3.42 इति "
            "पुंवद्भावो भवति** — कालककालिका comes out that way "
            "only because the pair counts as a कर्मधारय for "
            "that rule's purposes too"),
    Dve(
        "8.1.12", does="dve", gana="guṇavacana",
        sense=("prakāra",), like="karmadhāraya",
        why="प्रकारे गुणवचनस्य — a QUALITY-word doubles in the "
            "sense of a SORT: **पटुपटुः, मृदुमृदुः, "
            "पण्डितपण्डितः**, which the vṛtti glosses "
            "**अपरिपूर्णगुण इत्यर्थः** — not quite clever, "
            "said of the lesser when the fuller is the "
            "measure. **प्रकारो भेदः सादृश्यं च**, and it is "
            "the likeness and not the difference that is taken "
            "here.\\n\\n"
            "**AND IT DOES NOT DISPLACE THE AFFIX THAT SAYS THE "
            "SAME THING.** **जातीयरः अनेन द्विर्वचनेन बाधनं न "
            "इष्यते** — पटुजातीयः and मृदुजातीयः stand beside "
            "the doubled forms, and the option is carried down "
            "from the sūtra after: **वक्ष्यमाणम् अन्यतरस्यां"
            "ग्रहणम्**"),
    Dve(
        "8.1.13", does="dve", of=("priya", "sukha"),
        sense=("akṛcchra",), like="karmadhāraya", optional=True,
        keeps_out="प्रियः पुत्रः, सुखो रथः — the plain senses, "
                  "where nothing doubles",
        why="अकृच्छ्रे प्रियसुखयोरन्यतरस्याम् — प्रिय and सुख "
            "double OPTIONALLY where ease is to be conveyed: "
            "**प्रियप्रियेण ददाति; सुखसुखेन ददाति**, beside "
            "प्रियेण ददाति and सुखेन ददाति. **कृच्छ्रं दुःखम्, "
            "तदभावः अकृच्छ्रम्** — and the sense is "
            "**अखिद्यमानो ददाति**, he gives without being put "
            "out. It is this sūtra's अन्यतरस्याम् that the rule "
            "before borrows to keep पटुजातीयः alive"),
    Dve(
        "8.1.14", does="nipātana", of=("yathāyatham",),
        sense=("yathāsva",), like="karmadhāraya", nipatana=True,
        why="यथास्वे यथायथम् — **यथायथम्** is laid down in the "
            "sense of यथास्व: **यो य आत्मा, यद् यद् आत्मीयम्, "
            "तत् तद् यथास्वम्**. Two things are given at once "
            "— **यथाशब्दस्य द्विर्वचनं नपुंसकलिङ्गता च "
            "निपात्यते**, the doubling of यथा and the neuter "
            "gender, neither of which any rule would supply. "
            "**ज्ञाताः सर्वे पदार्था यथायथम्**, each according "
            "to its own nature; **सर्वेषां तु यथायथम्**, each "
            "according to what is his"),
    Dve(
        "8.1.15", does="nipātana", of=("dvandvam",),
        sense=DVANDVA_FIVE, like="karmadhāraya", nipatana=True,
        why="द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्र"
            "प्रयोगाभिव्यक्तिषु — **द्वन्द्वम्** is laid down "
            "in five senses, and THREE separate departures go "
            "into the one word: **द्विशब्दस्य द्विर्वचनम्, "
            "पूर्वपदस्य आम्भावः, अत्वं च उत्तरपदस्य "
            "निपात्यते** — द्वि is doubled, the first member "
            "takes आम् and the second becomes अ.\\n\\n"
            "**AND ONLY ONE OF THE FIVE SENSES IS WHAT THE WORD "
            "MEANS.** **तत्र रहस्यं द्वन्द्वशब्दवाच्यम्, इतरे "
            "विषयभूताः** — secrecy is what द्वन्द्वम् SAYS, and "
            "the other four are occasions on which it is said. "
            "**द्वन्द्वं मन्त्रयन्ते** of secrecy; **आचतुरं ही "
            "इमे पशवो द्वन्द्वं मिथुनीयन्ति** of a limit not "
            "overstepped"),
)


def _reaches(row: Dve, word: str, gana: str, sense: str,
             position: str, chandasi: bool) -> bool:
    # A rule that only opens a heading is stated of everything
    # after it and of nothing in particular. 8.1.1 and 8.1.11
    # are both of that kind, and neither answers a query.
    if row.heading:
        return False
    named = row.of or row.gana
    if named and not (word in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.position and position != row.position:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Dve, word: str, gana: str) -> int:
    """
    A named word beats a word class, and a named sense beats
    neither — because almost every rule here has one.

    8.1.5 against 8.1.4 is what needs the word to weigh most:
    परि in the sense of exclusion is doubled by its own rule
    and not by the general one, and both would otherwise be
    reached by a query that named a sense alone.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of and word in row.of)
        + 5 * bool(row.position)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * len(row.sense)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Doubled:
    """What the run answers: a doubling, a name, or an accent."""

    does: str
    sutra: str
    why: str
    #: What the pair then counts as, where a rule says.
    like: str = ""
    optional: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def doubles(word: str = "", *, gana: str = "", sense: str = "",
            position: str = "", chandasi: bool = False) -> Doubled:
    """
    8.1.1–15 — what is said twice, and in what sense.

    Nothing answers by default. A word no rule of the run names,
    in a sense none of them speaks of, is said once.
    """
    matched = [
        row for row in DVE_TABLE
        if _reaches(row, word, gana, sense, position, chandasi)
    ]
    if not matched:
        return Doubled(
            "", "", "No rule of 8.1.1-15 is reached, so the word "
                    "is said once")
    row = max(matched, key=lambda one: _how_specific(one, word, gana))
    return Doubled(row.does, row.sutra, row.why, like=row.like,
                   optional=row.optional, nipatana=row.nipatana,
                   blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Dve, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in DVE_TABLE if row.sutra == sutra_id)


__all__ = [
    "Dve", "DVE_TABLE", "DVE_RUN", "ADHIKARA_TO",
    "PADA_PURANA", "SAMIPYA_THREE", "AMANTRITA_FIVE",
    "DVANDVA_FIVE",
    "Doubled", "doubles", "provisions_for",
]
