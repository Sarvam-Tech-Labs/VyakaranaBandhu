# -*- coding: utf-8 -*-
"""
८.२.६२–८१ — क्विन्, the रुँ, अहन्, and what अदस् becomes.

Twenty sūtras, and 8.2.66 ससजुषो रुँः — the one every reader
knows, since it is what turns every final स् into the visarga
one actually hears — was codified long before this pāda was
read, inside `anga`. It is named in `CODIFIED_APART` and not
restated.

**WHAT A WORD ENDS IN.** 8.2.62–65: a word from a root that
took क्विन् ends in a guttural (घृतस्पृक्, ऋत्विक्), नश् does
so optionally (जीवनक् beside जीवनट्), and a म्-final root's word
ends in न् — प्रशान्, and before a म् or व् अगन्म, जगन्वान्.

**अहन् TWICE OVER.** 8.2.68 gives it रुँ (अहोभ्याम्, अहोभिः)
and 8.2.69 a plain र् where no case ending follows (अहर् ददाति,
अहर् भुङ्क्ते) — and the vṛtti reads the sūtra's own spelling
as proof: **नलोपम् अकृत्वा निर्देशो ज्ञापकः**, अहन् is written
with its न् so that 8.2.7 shall not take it off.

**AND THE VEDA TAKES BOTH ROADS AT ONCE.** 8.2.70–71: अम्नस्,
ऊधस्, अवस् and भुवस् as a महाव्याहृति may end in रुँ or in र्,
**उभयथा** — अम्न एव beside अम्नर् एव, ऊध एव beside ऊधर् एव.

**AND अदस् IS REBUILT FROM THE INSIDE.** 8.2.80 puts a उ after
the द् and turns the द् into म् — अमुम्, अमू, अमुना — and
8.2.81 makes it ई in the plural: अमी, अमीभिः, अमीषाम्. Neither
sound of अदस् survives into any of those forms except the अ.

**WHAT THIS MODULE DOES NOT DO.** It says what the word's end
becomes. What the रुँ then turns into — the visarga, or a ऊ, or
nothing — is 8.3's, and 6.1.113 and 6.1.114 are what carry it
there.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.nalopa_matup import Changed  # noqa: E402

#: This module's stretch.
RU_RUN: Tuple[str, str] = ("8.2.62", "8.2.81")

#: Codified long before the pāda was read, inside `anga`:
#: 8.2.66 ससजुषो रुँः. Nothing here restates it.
CODIFIED_APART: Tuple[str, ...] = ("8.2.66",)

#: 8.2.67's three, laid down whole.
AVAYAH_THREE: Tuple[str, ...] = (
    "avayāḥ", "śvetavāḥ", "puroḍāḥ")

#: 8.2.70's three, which the Veda takes both ways.
UBHAYATHA_THREE: Tuple[str, ...] = ("amnas", "ūdhas", "avas")

#: 8.2.72's four, whose word ends in द्.
VASU_FOUR: Tuple[str, ...] = ("vasu", "sraṃs", "dhvaṃs", "anaḍuh")

#: 8.2.79's three, which refuse the lengthening.
BHA_KUR_CHUR: Tuple[str, ...] = ("bha", "kur", "chur")


@dataclass(frozen=True)
class Ru:
    """One rule of 8.2.62–81: what a word's last sound becomes."""

    sutra: str
    #: `ku`, `na`, `ru`, `ra`, `da`, `dīrgha`, `u-ma`, `ī-ma`,
    #: `nipātana`.
    does: str = ""
    #: The words or roots named outright.
    of: Tuple[str, ...] = ()
    #: The shape of the word instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: True where the sūtra only keeps another rule off.
    refuses: bool = False
    #: True where the rule allows two forms at once — either
    #: **वा** or the Veda's **उभयथा**.
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


RU_TABLE: Tuple[Ru, ...] = (
    Ru(
        "8.2.62", does="ku", gana="kvin-pratyaya",
        why="क्विन्प्रत्ययस्य कुः — a word whose root took "
            "क्विन् ends in a GUTTURAL, wherever it ends: "
            "**घृतस्पृक्** from स्पृश् by 3.2.58, and so for "
            "every other क्विन्-formation. **क्विन् प्रत्ययो "
            "यस्माद् धातोः स क्विन्प्रत्ययः** — the name is of "
            "the whole word and not of the affix, which is why "
            "the guttural lands on the LAST sound and not "
            "where the affix was. **पदस्येति वर्तते**, and "
            "**सर्वत्र पदान्ते कुत्वम् इष्यते**"),
    Ru(
        "8.2.63", does="ku", of=("naś",), optional=True,
        why="नशेर्वा — and नश् does so only optionally: **सा वै "
            "जीवनगाहुतिः; सा वै जीवनडाहुतिः** — **जीवस्य नाशो "
            "जीवनक्, जीवनट्**, both standing. The word is नश् "
            "with the क्विप् of the सम्पदादि class, and the "
            "option is against 8.3's cerebralisation: "
            "**षत्वे प्राप्ते कुत्वविकल्पः**, so where the "
            "guttural does not come a ष् does, and the two "
            "alternatives are ट् and क् rather than क् and "
            "nothing"),
    Ru(
        "8.2.64", does="na", gana="ma-anta-dhātu",
        keeps_out="भित् — the root does not end in म्",
        why="मो नो धातोः — a word from a म्-final ROOT ends in "
            "न्: **प्रशान्, प्रतान्, प्रदान्** — शम्, तन् and "
            "दम् with the क्विप्, lengthened by 6.4.15. And the "
            "न् this rule makes is invisible to the rule that "
            "would drop it — **नत्वस्य असिद्धत्वान् नलोपो न "
            "भवति** — so 8.2.7 cannot reach it and the word "
            "keeps a न् it was given four sūtras earlier in "
            "the same pāda"),
    Ru(
        "8.2.65", does="na", gana="ma-anta-dhātu",
        before=("ma", "va"),
        why="म्वोश्च — and before a म् or a व्. **अगन्म तमसस् "
            "पारम्; अगन्व** — गम् in the imperfect with the "
            "class sign dropped by 2.4.73's बहुलं छन्दसि; and "
            "**जगन्वान्**, by 7.2.68's option. The condition is "
            "not a word's end at all, which is why the sūtra "
            "has to be stated apart from the one before"),
    Ru(
        "8.2.67", does="nipātana", of=AVAYAH_THREE,
        nipatana=True,
        why="अवयाःश्वेतवाःपुरोडाश्च — three words laid down "
            "whole: **अवयाः** from यज् with अव, **श्वेतवाः** "
            "from वह् with श्वेत, **पुरोडाः** from दाश् with "
            "पुरस्. Each takes the ण्विन् of 3.2.71–72 and then "
            "the substitution of श्वेतवहादि, and what the "
            "निपातन gives is the स् at the end, which the रुँ "
            "of 8.2.66 then works on"),
    Ru(
        "8.2.68", does="ru", of=("ahan",),
        why="अहन् — the word अहन् takes रुँ: **अहोभ्याम्, "
            "अहोभिः**.\\n\\n"
            "**AND THE SŪTRA'S OWN SPELLING IS READ AS "
            "PROOF.** **नलोपम् अकृत्वा निर्देशो ज्ञापकः — "
            "नलोपाभावो यथा स्याद् इति** — Pāṇini writes अहन् "
            "with its न् still on, and could have written अहः; "
            "that he did not shows the न्-loss of 8.2.7 is not "
            "to come here. **दीर्घाहा निदाघः; हे दीर्घाहोऽत्र** "
            "are what the ज्ञापक buys"),
    Ru(
        "8.2.69", does="ra", of=("ahan",), before=("a-sup",),
        blocks=("8.2.68",),
        keeps_out="अहोभ्याम्, अहोभिः — a सुप् follows, and the "
                  "रुँ of the sūtra before stands",
        why="रोऽसुपि — and a plain र् where no case ending "
            "follows: **अहर् ददाति; अहर् भुङ्क्ते**. The "
            "objection and its answer are worth the space: one "
            "might say a सुप् IS there by 1.1.62, having been "
            "dropped — **ननु च अत्र अपि प्रत्ययलक्षणेन सुब् "
            "अस्ति?** — and the reply is that it is not, on a "
            "principle stated earlier in the work"),
    Ru(
        "8.2.70", does="ru", of=UBHAYATHA_THREE, chandasi=True,
        optional=True,
        why="अम्नरूधरवरित्युभयथा छन्दसि — and in the Veda "
            "अम्नस्, ऊधस् and अवस् go BOTH WAYS, with a रुँ or "
            "with a plain र्: **अम्न एव** beside **अम्नर् "
            "एव**, **ऊध एव** beside **ऊधर्**, **अवः** beside "
            "**अवर्**. उभयथा is the rarest kind of option in "
            "the work — not a choice between doing and not "
            "doing, but between two substitutes that differ "
            "only in what happens to them afterwards"),
    Ru(
        "8.2.71", does="ru", of=("bhuvas",),
        gana="mahāvyāhṛti", chandasi=True, optional=True,
        keeps_out="भुवो विश्वेषु सवनेषु यज्ञियः — not the "
                  "महाव्याहृति, and the option does not come",
        why="भुवश्च महाव्याहृतेः — and भुवस् where it is the "
            "MAHĀVYĀHṚTI, either way: **भुव इत्य् अन्तरिक्षम्; "
            "भुवर् इत्य् अन्तरिक्षम्** — the second of the "
            "three great utterances भूर् भुवः स्वः. Anywhere "
            "else the option does not come, and the vṛtti "
            "quotes a ṛc where भुवस् is an ordinary verb"),
    Ru(
        "8.2.72", does="da", of=VASU_FOUR,
        why="वसुस्रंसुध्वंस्वनडुहां दः — a वसु-final word, and "
            "स्रंस्, ध्वंस् and अनडुह्, end in द्.\\n\\n"
            "**AND THE VṚTTI HAS TO SAY WHICH OF THE FOUR THE "
            "स् CARRIED DOWN FROM 8.2.66 QUALIFIES.** **तेन "
            "सम्भवाद् व्यभिचाराच् च वसुर् एव विशेष्यते, न "
            "स्रंसुध्वंसू व्यभिचाराभावाद्, असम्भवाच् च न "
            "अनडुह्शब्दः** — वसु alone is qualified by it, "
            "since वसु may or may not end in स्; स्रंस् and "
            "ध्वंस् always do, so qualifying them would say "
            "nothing; and अनडुह् never does, so it cannot be "
            "qualified at all"),
    Ru(
        "8.2.73", does="da", gana="sa-anta-a-asti",
        before=("tip",),
        keeps_out="चकाः — a क्विप् and not a तिप्; आप एवेदं "
                  "सलिलं सर्वम् आः — the root IS अस्",
        why="तिप्यनस्तेः — before तिप् a स्-final word takes "
            "द्, unless the root is अस्: **अचकाद् भवान्; "
            "अन्वशाद् भवान्**. Both conditions are tested, and "
            "the second is tested with a Vedic form of अस् in "
            "the imperfect — **आ इत्य् अस्तेर् लङि तिपि** — "
            "where the word ends in स् and the द् does not come"),
    Ru(
        "8.2.74", does="ru", gana="sa-anta-dhātu",
        before=("sip",), optional=True,
        why="सिपि धातो रुर्वा — and before सिप् a स्-final word "
            "FROM A ROOT takes रुँ, or else द्: **अचकास् त्वम्, "
            "अचकात् त्वम्; अन्वशास् त्वम्, अन्वशात् त्वम्**. "
            "**धातुग्रहणं च उत्तरार्थं रुग्रहणं च** — both "
            "words are said with the next sūtra in view, which "
            "borrows them and gives them to a द्-final word"),
    Ru(
        "8.2.75", does="ru", gana="da-anta-dhātu",
        before=("sip",), optional=True,
        why="दश्च — and a द्-final word from a root, before "
            "सिप्, the same way: **अभिनस् त्वम्, अभिनत् त्वम्; "
            "अच्छिनस् त्वम्, अच्छिनत् त्वम्**. The pair of "
            "sūtras is the neatest borrowing in the pāda — one "
            "says धातोः and रुः so that the other need say "
            "only दः, and the two together cover both endings "
            "before one affix"),
    Ru(
        "8.2.76", does="dīrgha", gana="ra-va-anta-dhātu",
        keeps_out="अबिभर् भवान् — the ि is the reduplication's "
                  "and not the penult",
        why="र्वोरुपधाया दीर्घ इकः — the इक् PENULT of a word "
            "from a र्-final or व्-final root lengthens: "
            "**गीः, धूः, पूः, आशीः**. **वकारग्रहणम् "
            "उत्तरार्थम्** — the व् is said for the two sūtras "
            "after; here only the र् does any work. And "
            "उपधाग्रहणम् is what keeps the reduplication's "
            "vowel out of reach in अबिभर् भवान्"),
    Ru(
        "8.2.77", does="dīrgha", gana="ra-va-anta-dhātu",
        before=("hal",),
        keeps_out="दिवम् इच्छति दिव्यति; चतुर इच्छति चतुर्यति — "
                  "the words are not from roots at all",
        why="हलि च — and before a हल्, whether or not a word "
            "ends there: **आस्तीर्णम्, विस्तीर्णम्, विशीर्णम्, "
            "अवगूर्णम्** for the र्, and **दीव्यति, सीव्यति** "
            "for the व् — which is the first place वकारग्रहणम् "
            "earns its keep. **धातोर् इत्येव** is what keeps "
            "the denominatives out"),
    Ru(
        "8.2.78", does="dīrgha", gana="ra-va-upadha-hal-para",
        before=("hal",),
        keeps_out="चिरिणोति, जिरिणोति — the र् has no हल् after "
                  "it",
        why="उपधायां च — and where the र् or व् is itself the "
            "PENULT with a हल् after it, the इक् before THAT "
            "lengthens: **हूर्छिता, मूर्छिता, ऊर्विता, "
            "धूर्विता** — from हुर्छा, मुर्छा, उर्वी, धुर्वी. "
            "The rule reaches one sound further back than the "
            "two before it, which is what the whole of its "
            "wording is for"),
    Ru(
        "8.2.79", refuses=True, of=BHA_KUR_CHUR,
        blocks=("8.2.76", "8.2.77", "8.2.78"),
        keeps_out="प्रतिदीव्ना, प्रतिदीव्ने — a भ, but its र् "
                  "or व् is not final, so the refusal does not "
                  "reach it",
        why="न भकुर्छुराम् — but not of a भ, and not of कुर् or "
            "छुर्: **धुरं वहति धुर्यः; धुरि साधुर् धुर्यः; "
            "दिव्यम्; कुर्यात्; छुर्यात्**. The भ must be one "
            "whose र् or व् is FINAL — **रेफवकाराभ्यां "
            "भविशेषणं किम्? प्रतिदीव्ना** — so the refusal is "
            "narrower than it reads, and it takes back all "
            "three of the lengthening rules at once"),
    Ru(
        "8.2.80", does="u-ma", of=("adas",),
        gana="a-sa-anta",
        why="अदसोऽसेर्दादु दो मः — in अदस्, every sound after "
            "the द् except a final स् becomes उ, and the द् "
            "itself becomes म्: **अमुम्, अमू, अमून्; अमुना, "
            "अमूभ्याम्**. The उ takes the length of what it "
            "replaces — **भाव्यमानेन अपि उकारेण सवर्णानां "
            "ग्रहणम् इष्यते** — so a one-mātrā sound gives a "
            "short उ and a two-mātrā one a long ऊ, which is "
            "how अमू and अमुना come from one rule"),
    Ru(
        "8.2.81", does="ī-ma", of=("adas",), gana="bahuvacana",
        blocks=("8.2.80",),
        why="एत ईद्बहुवचने — and the ए after that द् becomes ई "
            "in the PLURAL, the द् becoming म् as before: "
            "**अमी, अमीभिः, अमीभ्यः, अमीषाम्, अमीषु**. "
            "**बहुवचन इत्यर्थनिर्देशोऽयम्** — the word names "
            "the SENSE of plurality and not the grammatical "
            "plural ending, because अमी has no ending left to "
            "be plural with. With this the reshaping of अदस् "
            "is finished, and not one of its own sounds but "
            "the first is left"),
)


def _reaches(row: Ru, word: str, gana: str, before: str,
             chandasi: bool) -> bool:
    # `of` and `gana` CONJOIN. 8.2.80 and 8.2.81 both name अदस्
    # and differ only in the शेष they add, so an alternative
    # reading would let a bare `bahuvacana` answer for any word
    # at all.
    if row.of and word not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.before and before not in row.before:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Ru) -> int:
    """
    A refusal outweighs the rules it refuses, and a displacer
    outweighs what it displaces.

    8.2.68 against 8.2.69 is what needs the last part: अहन्
    takes a रुँ before an ending and a plain र् without one,
    and the two rules name the same word.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of)
        + 4 * bool(row.gana)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


def the_word_end(word: str = "", *, gana: str = "",
                 before: str = "",
                 chandasi: bool = False) -> Changed:
    """
    8.2.62–81 — क्विन्, the रुँ, अहन्, and what अदस् becomes.

    Nothing answers by default. 8.2.66 ससजुषो रुँः, which would
    answer for almost every स्-final word, is codified apart and
    is not in this table.
    """
    matched = [
        row for row in RU_TABLE
        if _reaches(row, word, gana, before, chandasi)
    ]
    if not matched:
        return Changed(
            "", "", "No rule of 8.2.62-81 is reached, so the word "
                    "ends as it stands")
    row = max(matched, key=_how_specific)
    return Changed(row.does, row.sutra, row.why,
                   refuses=row.refuses, optional=row.optional,
                   nipatana=row.nipatana, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Ru, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in RU_TABLE if row.sutra == sutra_id)


__all__ = [
    "Ru", "RU_TABLE", "RU_RUN", "CODIFIED_APART",
    "AVAYAH_THREE", "UBHAYATHA_THREE", "VASU_FOUR",
    "BHA_KUR_CHUR",
    "the_word_end", "provisions_for",
]
