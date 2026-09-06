# -*- coding: utf-8 -*-
"""
७.२.१–७ — वृद्धि in the सिच् aorist, and where it stops.

Seven sūtras opening अध्याय ७'s second pāda. The first gives an
इक्-final stem vṛddhi before सिच् in the परस्मैपद — अचैषीत्,
अकार्षीत्, अहार्षीत् — and the six after it argue about how far
that reaches: to a र्- or ल्-final stem's अ (अक्षारीत्), to वद्
and व्रज् and every consonant-final root (अवादीत्, अपाक्षीत्),
and then NOT where the सिच् has an इट् in front of it (अदेवीत्).

**AND THE FIRST SŪTRA HAS TO BEAT AN INNER RULE TO APPLY AT
ALL.** guṇa is अन्तरङ्ग and would come first, leaving nothing for
the vṛddhi to work on. **अन्तरङ्गम् अपि गुणम् एषां वृद्धिर्
वचनाद् बाधते** — the vṛddhi displaces it by the mere fact of
having been stated, since otherwise the statement would be idle.
The vṛtti repeats the argument at 7.2.4 and again at 7.2.5.

**AND ONE OF THE SEVEN IS AN OPTION AND ONE A DOUBLE OPTION.**
7.2.7 makes the refusal optional for a light अ after a
consonant — अकणीत् beside अकाणीत् — and 7.2.6 makes ऊर्णु's
refusal optional on top of 1.2.3's own option, so प्रौर्णवीत्,
प्रौर्णावीत् and प्रौर्णुवीत् all stand.

**WHAT THIS MODULE DOES NOT DO.** It says whether the vṛddhi
comes. Whether the aorist takes सिच् at all is 3.1.44's, and
whether the इट् is there is 7.2.35's and what follows it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch, opening पाद ७.२.
VRDDHI_RUN: Tuple[str, str] = ("7.2.1", "7.2.7")

#: 7.2.5's list, which refuses the vṛddhi before an इट्-initial
#: सिच्: ह्-final, म्-final and य्-final stems, and five roots.
HMYANTA: Tuple[str, ...] = ("h-anta", "m-anta", "y-anta")
FIVE_ROOTS: Tuple[str, ...] = ("kṣaṇ", "śvas", "jāgṛ", "ṇi", "śvi")

#: And the एदित् roots that go with them: रगे, कखे.
EDIT: Tuple[str, ...] = ("rage", "kakhe")

#: The two roots 7.2.3 names beside every consonant-final stem.
VADA_VRAJA: Tuple[str, ...] = ("vad", "vraj")

#: The maxim the vṛtti uses three times over, to let a stated
#: vṛddhi displace the guṇa that would come first.
ANTARANGA: str = (
    "अन्तरङ्गम् अपि गुणम् एषां वृद्धिर् वचनाद् बाधते")


@dataclass(frozen=True)
class Vrddhi:
    """One rule of 7.2.1–7: vṛddhi before सिच्, or the refusal."""

    sutra: str
    #: The stem class the rule reaches.
    gana: str = ""
    #: The roots named outright.
    of: Tuple[str, ...] = ()
    #: What part of the stem is strengthened.
    part: str = ""
    #: What must follow — सिच्, and whether it has an इट्.
    before: Tuple[str, ...] = ()
    #: परस्मैपद or आत्मनेपद.
    pada: str = ""
    refuses: bool = False
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


VRDDHI_TABLE: Tuple[Vrddhi, ...] = (
    Vrddhi(
        "7.2.1", gana="ik-anta", before=("sic",), pada="parasmaipada",
        keeps_out="अच्योष्ट, अप्लोष्ट — आत्मनेपद, and the vṛddhi "
                  "does not come",
        why="सिचि वृद्धिः परस्मैपदेषु — an इक्-final stem takes "
            "vṛddhi before a सिच् followed by a परस्मैपद ending: "
            "**अचैषीत्, अनैषीत्, अलावीत्, अपावीत्, अकार्षीत्, "
            "अहार्षीत्**.\\n\\n"
            "**AND IT HAS TO BEAT AN INNER RULE TO APPLY AT "
            "ALL.** guṇa is अन्तरङ्ग and would come first, "
            "leaving no इक् to strengthen. **अन्तरङ्गम् अपि "
            "गुणम् एषां वृद्धिर् वचनाद् बाधते** — the vṛddhi "
            "displaces it by the mere fact of having been "
            "stated, since a statement that could never apply "
            "would be idle. The vṛtti makes the same argument "
            "again at 7.2.4 and at 7.2.5.\\n\\n"
            "**AND WHERE THE vṛddhi IS REFUSED SOMETHING ELSE "
            "GETS IN.** **न्यनुवीद्, न्यधुवीद् इत्यत्र "
            "कुटादित्वाद् ङित्वे सति प्रतिषिद्धायां वृद्धाव् "
            "उवङादेशः क्रियते** — the कुटादि roots are ङित् by "
            "1.2.1, 1.1.5 then refuses the vṛddhi, and 6.4.77's "
            "उवङ् takes the space"),
    Vrddhi(
        "7.2.2", gana="r-l-anta", part="a", before=("sic",),
        pada="parasmaipada", blocks=("7.2.7",),
        keeps_out="न्यखोरीत्, न्यमीलीत् — the vowel is not अ; "
                  "मा भवानटीत्, मा भवानशीत् — the stem ends in "
                  "neither र् nor ल्; अवभ्रीत्, अश्वल्लीत् — the "
                  "र् and ल् are in the stem but not at its end",
        why="अतो र्लान्तस्य — and the अ of a stem ending in र् or "
            "ल् takes it, that अ standing NEXT to the final: "
            "**अक्षारीत्, अत्सारीत्, अज्वालीत्, अह्मालीत्**. "
            "**अतो हलादेर्लघोः इति विकल्पस्यायम् अपवादः** — an "
            "exception to 7.2.7's option, so here the vṛddhi is "
            "compulsory. And अन्तग्रहणम् is what keeps अवभ्रीत् "
            "out: **अत्र यौ रेफलकाराव् अङ्गस्यान्तौ, न तावतः "
            "समीपौ**"),
    Vrddhi(
        "7.2.3", gana="hal-anta", of=VADA_VRAJA, part="ac",
        before=("sic",), pada="parasmaipada", blocks=("7.2.7",),
        why="वदव्रजहलन्तस्याचः — and the vowel of वद्, व्रज् and "
            "of any CONSONANT-final stem: **अवादीत्, अव्राजीत्; "
            "अपाक्षीत्, अभैत्सीत्, अच्छैत्सीत्, अरौत्सीत्**. "
            "वद् and व्रज् are named to shut out 7.2.7's option, "
            "**विकल्पबाधनार्थम्**.\\n\\n"
            "**AND हलन्त IS SAID TO CATCH A CLUSTER AND NOT ONE "
            "CONSONANT.** Split the sūtra and हलन्तग्रहणम् is "
            "unnecessary; kept, it is **हल्समुदायपरिग्रहार्थम्** "
            "— **अराङ्क्षीत्, असाङ्क्षीत्** need the vowel to be "
            "reached across TWO consonants, and **येन "
            "नाव्यवधानं तेन व्यवहितेऽपि** by itself lets only "
            "one stand between"),
    Vrddhi(
        "7.2.4", refuses=True, gana="hal-anta", before=("iṭ-sic",),
        blocks=("7.2.3",),
        keeps_out="अलावीत् — the stem does not end in a consonant, "
                  "and 7.2.1's vṛddhi stands",
        why="नेटि — but a consonant-final stem does NOT take it "
            "where the सिच् has an इट् in front: **अदेवीत्, "
            "असेवीत्, अकोषीत्, अमोषीत्**.\\n\\n"
            "**AND THE OBJECTION IS THAT EVERY STEM IS "
            "CONSONANT-FINAL BY THEN.** guṇa and the अव् "
            "substitution would have made लू into लाव्, so "
            "अलावीत् should be refused too. **नैतद् एवम्। "
            "अन्तरङ्गम् अपि गुणं वचनारम्भसामर्थ्यात् सिचि "
            "वृद्धिर् बाधते इत्युक्तम्** — the same answer as at "
            "7.2.1, and the vṛtti says so by citing itself"),
    Vrddhi(
        "7.2.5", refuses=True, gana="hmy-anta", of=FIVE_ROOTS + EDIT,
        before=("iṭ-sic",), pada="parasmaipada",
        blocks=("7.2.1", "7.2.7"),
        why="ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम् — and neither do "
            "ह्-final, म्-final and य्-final stems, nor क्षण्, "
            "श्वस्, जागृ, णि, श्वि, nor the एदित् roots: "
            "**अग्रहीत्, अस्यमीत्, अवमीत्, अव्ययीत्, अक्षणीत्, "
            "अश्वसीत्, अजागरीत्, औनयीत्, अश्वयीत्; अरगीत्, "
            "अकखीत्**.\\n\\n"
            "**AND THE LIST DOES TWO DIFFERENT JOBS AT ONCE.** "
            "For the ह्म्य-final stems and क्षण् and श्वस् and "
            "the एदित् roots it refuses 7.2.7's OPTION; for "
            "जागृ, णि and श्वि it refuses 7.2.1's vṛddhi, which "
            "7.2.4 could not reach because they are not "
            "consonant-final. **सा च नेटि इति न प्रतिषिध्यते** "
            "— and naming णि and श्वि proves that guṇa has not "
            "come first, or they would be य्-final already and "
            "the naming idle"),
    Vrddhi(
        "7.2.6", refuses=True, of=("ūrṇu",), before=("iṭ-sic",),
        pada="parasmaipada", optional=True, blocks=("7.2.1",),
        why="ऊर्णोतेर्विभाषा — and ऊर्णु refuses it OPTIONALLY: "
            "**प्रौर्णवीत्, प्रौर्णावीत्**.\\n\\n"
            "**AND IT IS AN OPTION ON TOP OF ANOTHER OPTION.** "
            "1.2.3's **विभाषोर्णोः** already makes ऊर्णु's affix "
            "ङित् or not. On the अङित् side this sūtra then "
            "gives two forms; on the ङित् side 1.1.5 refuses "
            "both guṇa and vṛddhi and the उवङ् comes instead — "
            "**प्रौर्णुवीत्**. Three forms out of two options, "
            "and the vṛtti sets them out in that order"),
    Vrddhi(
        "7.2.7", refuses=True, gana="hal-ādi", part="laghu-a",
        before=("iṭ-sic",), pada="parasmaipada", optional=True,
        blocks=("7.2.1",),
        keeps_out="अदेवीत्, असेवीत् — the vowel is not अ; "
                  "मा भवानशीत्, मा भवानटीत् — the stem does not "
                  "BEGIN with a consonant; अतक्षीत्, अरक्षीत् — "
                  "the अ is not light; अचकासीत् — two consonants "
                  "stand between",
        why="अतो हलादेर्लघोः — and a LIGHT अ in a stem that "
            "begins with a consonant refuses it optionally: "
            "**अकणीत्, अकाणीत्; अरणीत्, अराणीत्**. Three "
            "conditions, and the vṛtti gives a counter-example "
            "for each.\\n\\n"
            "**AND ITS अतः IS NEEDED FOR A REASON THAT HAS "
            "NOTHING TO DO WITH ITS OWN EXAMPLES.** Drop it and "
            "अचः must be carried down instead; then the vṛddhi "
            "is अच्-conditioned and not इक्-conditioned, and "
            "1.1.5's क्ङिति refusal — which only stops an "
            "इक्-conditioned operation — would not reach "
            "न्यकुटीत् and न्यपुटीत्. **तत्राज्लक्षणा वृद्धिर् "
            "इग्लक्षणा न भवति इति क्ङिति च इति प्रतिषेधो न "
            "स्यात्**"),
)


def _reaches(row: Vrddhi, stem: str, gana: str, before: str,
             part: str, pada: str) -> bool:
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.part and part and part != row.part:
        return False
    if row.pada and pada != row.pada:
        return False
    return True


def _how_specific(row: Vrddhi, stem: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, and a named
    root beats a named class.

    7.2.1 against 7.2.4, 7.2.5, 7.2.6 and 7.2.7 is what needs it:
    one rule gives the vṛddhi and four take it back, two of them
    only in part.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of and stem in row.of)
        + 5 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.part)
        + 3 * bool(row.before)
        + 2 * bool(row.pada)
    )


@dataclass(frozen=True)
class Strengthened:
    """What the run answers: the vṛddhi, or its refusal."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def vrddhi(stem: str = "", *, gana: str = "", before: str = "",
           part: str = "", pada: str = "") -> Strengthened:
    """
    7.2.1–7 — whether the सिच् aorist strengthens its stem.

    Nothing answers by default, and the default is not *no
    vṛddhi*: it is that no rule of this run has been reached at
    all, which is what an आत्मनेपद aorist and a non-सिच् aorist
    both come to.
    """
    matched = [
        row for row in VRDDHI_TABLE
        if _reaches(row, stem, gana, before, part, pada)
    ]
    if not matched:
        return Strengthened(
            "", "", "No rule of 7.2.1-7 is reached, so this run "
                    "says nothing about the stem")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Strengthened("" if row.refuses else "vṛddhi", row.sutra,
                        row.why, optional=row.optional,
                        blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Vrddhi, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in VRDDHI_TABLE if row.sutra == sutra_id)


__all__ = [
    "Vrddhi", "VRDDHI_TABLE", "VRDDHI_RUN", "HMYANTA",
    "FIVE_ROOTS", "EDIT", "VADA_VRAJA", "ANTARANGA",
    "Strengthened", "vrddhi", "provisions_for",
]
