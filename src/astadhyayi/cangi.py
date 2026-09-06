# -*- coding: utf-8 -*-
"""
७.४.१–१२ — the चङ् aorist's shortening, and the perfect's guṇa.

पाद ७.४ opens on the reduplicated aorist. 7.4.1 shortens the
penult of a causal stem before चङ् — अचीकरत्, अजीहरत्, अलीलवत् —
and the four sūtras after it argue about which stems that reaches
and what they take instead: पिब loses its penult altogether
(अपीप्यत्), तिष्ठ takes an इ (अतिष्ठिपत्), जिघ्र takes one
optionally, and an ऋ becomes a plain ऋ (अचीकृतत्).

**AND THE ORDER AGAINST THE REDUPLICATION IS SETTLED TWICE.**
The shortening and the doubling both want to go first. In
अचीकरत् the shortening wins by being later; in मा भवान् अटिटत्
the doubling is compulsory and should win, and then there would
be no penult left to shorten. The answer is a ज्ञापक: **ओणेः
ऋदित्करणं ज्ञापकं नित्यम् अपि द्विर्वचनम् उपधाह्रस्वत्वेन
बाध्यते इति** — marking ओण् as ऋदित् at 7.4.2 would be pointless
unless the shortening beat the doubling even there.

**AND THEN FOUR SŪTRAS TURN TO THE PERFECT.** 7.4.10–12 give an
ऋ-final root guṇa in the लिट् — सस्वरतुः, सस्मरतुः — and make
three roots' vowel optionally short: विशश्रतुः beside विशशरतुः.
7.4.9 stands between, laying down दिगि for दय् in the perfect.

**WHAT THIS MODULE DOES NOT DO.** It says what the stem's vowel
becomes. That the aorist takes चङ् at all is 3.1.48's, and the
reduplication itself is 6.1.1's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch, opening पाद ७.४.
CANGI_RUN: Tuple[str, str] = ("7.4.1", "7.4.12")

#: Where the run turns from the aorist to the perfect.
LITI_FROM: str = "7.4.9"

#: 7.4.3's seven, whose shortening is optional.
BHRAJADI: Tuple[str, ...] = (
    "bhrāj", "bhās", "bhāṣ", "dīp", "jīv", "mīl", "pīḍ")

#: 7.4.12's three, whose perfect vowel is optionally short.
SR_DR_PR: Tuple[str, ...] = ("śṝ", "dṝ", "pṝ")

#: What the vṛtti reads out of 7.4.2's ऋदित् marking, to settle
#: the shortening against the reduplication.
JNAPAKA: str = (
    "ओणेः ऋदित्करणं ज्ञापकं नित्यम् अपि द्विर्वचनम् "
    "उपधाह्रस्वत्वेन बाध्यते इति")


@dataclass(frozen=True)
class Cangi:
    """One rule of 7.4.1–12: the vowel before चङ् or in the perfect."""

    sutra: str
    #: `hrasva`, `lopa`, `it`, `ṛt`, `guṇa`, `digi` — "" if refused.
    does: str = ""
    #: The roots named outright.
    of: Tuple[str, ...] = ()
    #: The root class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What part of the stem is affected.
    part: str = ""
    #: True where the reduplication's own vowel changes too.
    abhyasa: bool = False
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


CANGI_TABLE: Tuple[Cangi, ...] = (
    Cangi(
        "7.4.1", does="hrasva", part="upadhā", before=("caṅ-ṇi",),
        why="णौ चङ्युपधाया ह्रस्वः — the penult of a causal stem "
            "shortens before चङ्: **अचीकरत्, अजीहरत्, अलीलवत्, "
            "अपीपवत्**.\\n\\n"
            "**AND THE ORDER AGAINST THE REDUPLICATION IS SETTLED "
            "TWICE OVER.** In अचीकरत् the shortening wins by "
            "being later — **परत्वाद् उपधाह्रस्वत्वम्, तत्र कृते "
            "द्विर्वचनम्**. In मा भवान् अटिटत् the doubling is "
            "compulsory and should win, and then the penult "
            "would be gone before the shortening could reach it. "
            "**नैष दोषः। ओणेः ऋदित्करणं ज्ञापकं नित्यम् अपि "
            "द्विर्वचनम् उपधाह्रस्वत्वेन बाध्यते इति** — marking "
            "ओण् as ऋदित् in the next sūtra would be idle "
            "otherwise"),
    Cangi(
        "7.4.2", refuses=True, gana="a-glopi-śās-ṛdit",
        before=("caṅ-ṇi",), blocks=("7.4.1",),
        why="नाग्लोपिशास्वृदिताम् — but a stem that has lost a "
            "vowel, and शास्, and the ऋदित् roots, do NOT "
            "shorten: **अममालत्, अमामतरत्, अत्यरराजत्, "
            "अन्वलुलोमत्; अशशासत्; अबबाधत्, अययाचत्, "
            "अडुढौकत्**. Where the vowel alone is lost 1.1.56 "
            "would have saved the form anyway; the sūtra is for "
            "where a consonant goes with it — **हलचोरादेशे तु न "
            "सिध्यतीति तदर्थम् एतद् वचनम्**"),
    Cangi(
        "7.4.3", does="hrasva", of=BHRAJADI, part="upadhā",
        before=("caṅ-ṇi",), optional=True, blocks=("7.4.2",),
        why="भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम् — seven roots "
            "shorten OPTIONALLY: **अबिभ्रजत्, अबभ्राजत्; "
            "अबीभसत्, अबभासत्; अदीदिपत्, अदिदीपत्; अजीजिवत्, "
            "अजिजीवत्; अमीमिलत्, अमिमीलत्; अपीपिडत्, "
            "अपिपीडत्**. The vṛtti rejects one reading of the "
            "list outright — **भ्राजभासोर् ऋदित्करणम् "
            "अपाणिनीयम्** — and a vārttika adds कण and वण"),
    Cangi(
        "7.4.4", does="lopa", of=("pib",), part="upadhā",
        before=("caṅ-ṇi",), abhyasa=True, blocks=("7.4.1",),
        why="लोपः पिबतेरीच्चाभ्यासस्य — पिब loses its penult "
            "altogether and its reduplication takes ई: "
            "**अपीप्यत्, अपीप्यताम्, अपीप्यन्**. That the "
            "doubling happens at all after the loss is read out "
            "of another rule — **ओः पुयण् वचनं ज्ञापकं णौ "
            "स्थानिवद्भावस्य**"),
    Cangi(
        "7.4.5", does="it", of=("tiṣṭh",), part="upadhā",
        before=("caṅ-ṇi",), blocks=("7.4.1",),
        why="तिष्ठतेरित् — and तिष्ठ's penult becomes इ: "
            "**अतिष्ठिपत्, अतिष्ठिपताम्, अतिष्ठिपन्**. The stem "
            "named is तिष्ठ and not स्था, so 7.3.78's "
            "substitution has already been made when this rule "
            "reaches — one पाद's output being the next one's "
            "input, named by its finished shape"),
    Cangi(
        "7.4.6", does="it", of=("jighr",), part="upadhā",
        before=("caṅ-ṇi",), optional=True, blocks=("7.4.1",),
        why="जिघ्रतेर्वा — and जिघ्र's OPTIONALLY: **अजिघ्रिपत्, "
            "अजिघ्रिपताम्, अजिघ्रिपन्; अजिघ्रपत्, अजिघ्रपताम्, "
            "अजिघ्रपन्**"),
    Cangi(
        "7.4.7", does="ṛt", part="ṛ-varṇa", before=("caṅ-ṇi",),
        optional=True, blocks=("7.4.1",),
        why="उर्ऋत् — an ऋ in the penult optionally becomes a "
            "plain ऋ: **अचिकीर्तत्, अचीकृतत्; अववर्तत्, "
            "अवीवृतत्; अममार्जत्, अमीमृजत्**.\\n\\n"
            "**AND IT BEATS THREE INNER RULES BY BEING STATED AT "
            "ALL.** **वचनसामर्थ्याद् अन्तरङ्गा अपि इररारो "
            "बाध्यन्ते** — the इर्, अर् and आर् substitutions are "
            "अन्तरङ्ग and would come first, and the sūtra would "
            "be idle if they did. The तपर is what keeps the "
            "substitute short even for a long ॠ"),
    Cangi(
        "7.4.8", does="ṛt", part="ṛ-varṇa", before=("caṅ-ṇi",),
        chandasi=True, blocks=("7.4.7",),
        why="नित्यं छन्दसि — and in the Veda it is COMPULSORY: "
            "**अवीवृधत् पुरोडाशेन; अवीवृधताम्; अवीवृधन्**. The "
            "option of the sūtra before does not reach there"),
    Cangi(
        "7.4.9", does="digi", of=("day",), before=("liṭ",),
        why="दयतेर्दिगि लिटि — दय् becomes दिगि in the perfect: "
            "**अवदिग्ये, अवदिग्याते, अवदिग्यिरे**. The दय् meant "
            "is दीङ् and not **दय दाने**, which takes आम् in the "
            "perfect instead. And the substitute displaces the "
            "reduplication — **दिग्यादेशेन द्विर्वचनस्य बाधनम् "
            "इष्यते**"),
    Cangi(
        "7.4.10", does="guṇa", gana="ṛ-anta-saṃyoga-ādi",
        before=("liṭ",),
        keeps_out="चिक्षियतुः — not ऋ-final; चक्रतुः, चक्रुः — no "
                  "cluster at the head; स्मृतः, स्मृतवान् — no "
                  "perfect",
        why="ऋतश्च संयोगादेर्गुणः — an ऋ-final root BEGINNING "
            "with a cluster takes guṇa in the perfect: "
            "**सस्वरतुः, सस्वरुः; दध्वरतुः, दध्वरुः; सस्मरतुः, "
            "सस्मरुः**. It is stated so as to reach even where "
            "1.1.5 refuses — **प्रतिषेधविषयेऽपि गुणो यथा "
            "स्यात्** — and where vṛddhi could come instead, "
            "vṛddhi wins by prior contradiction: **सस्वार, "
            "सस्मार**"),
    Cangi(
        "7.4.11", does="guṇa", of=("ṛcch", "ṛ"), gana="ṝ-anta",
        before=("liṭ",),
        why="ऋच्छत्यॄताम् — and ऋच्छ्, ऋ and the ॠ-final roots: "
            "**आनर्च्छ, आनर्च्छतुः; आरतुः, आरुः; निचकरतुः, "
            "निजगरतुः**. For ऋच्छ् the guṇa was never available "
            "and for the ॠ-final roots it was refused, so the "
            "sūtra does two different things at once. And "
            "vṛddhi still wins where it can: **निचकार, "
            "निजगार**"),
    Cangi(
        "7.4.12", does="hrasva", of=SR_DR_PR, before=("liṭ",),
        optional=True, blocks=("7.4.11",),
        why="शृदॄप्रां ह्रस्वो वा — three roots' vowel is "
            "OPTIONALLY short in the perfect: **विशश्रतुः, "
            "विशशरतुः; विदद्रतुः, विददरतुः; निपप्रतुः, "
            "निपपरतुः**. **ह्रस्ववचनम् इत्वोत्वनिवृत्त्यर्थम्** "
            "— *short* is said rather than a substitute, to keep "
            "the इ and उ of other rules out. And some reject the "
            "sūtra outright, deriving the short forms from three "
            "separate roots श्रा, द्रा and प्रा instead"),
)


def _reaches(row: Cangi, root: str, gana: str, before: str,
             part: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.part and part and part != row.part:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Cangi, root: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, and a named
    root beats a named class.

    7.4.1 against the six that follow it is what needs both: one
    rule shortens every causal penult, one refuses it outright,
    and four give particular stems something else instead.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of and root in row.of)
        + 5 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.part)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Shaped:
    """What the run answers: the vowel's change, or its refusal."""

    does: str
    sutra: str
    why: str
    abhyasa: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_cang(root: str = "", *, gana: str = "",
                before: str = "", part: str = "",
                chandasi: bool = False) -> Shaped:
    """
    7.4.1–12 — the vowel before चङ्, and in the perfect.

    Nothing answers by default. A root outside a causal aorist
    and outside the perfect takes nothing from these twelve.
    """
    matched = [
        row for row in CANGI_TABLE
        if _reaches(row, root, gana, before, part, chandasi)
    ]
    if not matched:
        return Shaped(
            "", "", "No rule of 7.4.1-12 is reached, so the "
                    "stem's vowel stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Shaped("" if row.refuses else row.does, row.sutra,
                  row.why, abhyasa=row.abhyasa,
                  optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Cangi, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in CANGI_TABLE if row.sutra == sutra_id)


__all__ = [
    "Cangi", "CANGI_TABLE", "CANGI_RUN", "LITI_FROM",
    "BHRAJADI", "SR_DR_PR", "JNAPAKA", "Shaped", "before_cang",
    "provisions_for",
]
