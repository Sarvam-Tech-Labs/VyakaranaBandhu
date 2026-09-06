# -*- coding: utf-8 -*-
"""
८.२.४–२२ — the merged vowel's accent, the न् dropped, मतुप्'s व, र् → ल्.

पाद ८.२ opens under 8.2.1 पूर्वत्रासिद्धम्, and the first three
sūtras of the pāda are that heading itself. What follows falls
into four blocks, and this module holds them all.

**THE MERGED VOWEL'S ACCENT.** 8.2.4–6. Where two vowels have
become one, whose accent does it carry? An अनुदात्त after an
उदात्त or स्वरित यण् becomes स्वरित (कुमार्यौ); a single
substitute made WITH an उदात्त is उदात्त (अग्नी, वृक्षैः); and
where the अनुदात्त began a word, the substitute may be either
(सूत्थितः heard two ways).

**THE न् DROPPED.** 8.2.7–8. A प्रातिपदिक word loses its final
न् — राजा, राजभ्याम्, राजता — but not before ङि and not in the
vocative singular: हे राजन्, आर्द्रे चर्मन्.

**मतुप्'s व.** 8.2.9–17. Nine sūtras on when the म् of मतुप्
becomes व्: after म् or अ (किंवान्, शमीवान्), after a झय्
(अग्निचित्वान्), in a name (अहीवती), and in the Veda after इ or
र् (त्रिवती, हरिवः). Six names are laid down whole (8.2.12
आसन्दीवत्, चक्रीवत्, कक्षीवत्…) and two more singly — उदन्वान्
of the ocean and राजन्वान् of good government, against उदकवान्
and राजवान् everywhere else.

**र् BECOMING ल्.** 8.2.18–22. कृप् gives कल्प्ता, a preverb's
र् before अय् gives पलायते, गॄ before यङ् gives निजेगिल्यते —
and 8.2.21 अचि विभाषा is an OPTION that is not free: **इयं तु
व्यवस्थितविभाषा। तेन गल इति प्राण्यङ्गे नित्यं लत्वं भवति, गर
इति विषे नित्यं न भवति** — a throat is always गल and poison is
always गर, and the choice is made by the word and not by the
speaker.

**WHAT THIS MODULE DOES NOT DO.** It says what the word's end
becomes. That the whole tripādī is asiddha to what precedes is
8.2.1's, codified already; the accents these rules assign were
given by 6.1.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
NALOPA_RUN: Tuple[str, str] = ("8.2.4", "8.2.22")

#: The heading the whole pāda stands under, codified already.
ASIDDHA: str = "8.2.1"

#: 8.2.12's six names, laid down whole.
ASANDIVAT_SIX: Tuple[str, ...] = (
    "āsandīvat", "aṣṭhīvat", "cakrīvat", "kakṣīvat",
    "rumaṇvat", "carmaṇvatī")

#: 8.2.21's option is fixed by the word, not by the speaker.
VYAVASTHITA: str = (
    "इयं तु व्यवस्थितविभाषा। तेन गल इति प्राण्यङ्गे नित्यं "
    "लत्वं भवति, गर इति विषे नित्यं न भवति")


@dataclass(frozen=True)
class Antya:
    """One rule of 8.2.4–22: an accent, a loss, or a substitute."""

    sutra: str
    #: `svarita`, `udātta`, `lopa`, `va`, `nuṭ`, `la`,
    #: `nipātana`.
    does: str = ""
    #: The roots or ready-made words named outright.
    of: Tuple[str, ...] = ()
    #: The shape of what the rule reaches.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    sense: Tuple[str, ...] = ()
    #: True where the sūtra only keeps another rule off.
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NALOPA_TABLE: Tuple[Antya, ...] = (
    Antya(
        "8.2.4", does="svarita", gana="udātta-svarita-yaṇ-para",
        why="उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य — after a "
            "यण् that stands for an उदात्त or a स्वरित, a "
            "following अनुदात्त becomes स्वरित: **कुमार्यौ, "
            "कुमार्यः** for the first, **सकृल्ल्व्याशा, "
            "खलप्व्याशा** for the second. The derivation is "
            "worth following: 6.1.161 puts the accent on the ई "
            "of कुमारी, that ई becomes य् by the semivowel "
            "rule, and the य् carries its accent forward onto "
            "what follows"),
    Antya(
        "8.2.5", does="udātta", gana="ekādeśa-udātta",
        keeps_out="पचन्ति, यजन्ति — both vowels are अनुदात्त, "
                  "6.1.186 having taken the ending's accent",
        why="एकादेश उदात्तेनोदात्तः — where an अनुदात्त and an "
            "उदात्त have become ONE vowel, that vowel is "
            "उदात्त: **अग्नी, वायू, वृक्षैः, प्लक्षैः**. And "
            "the counter-example turns on a rule of the "
            "tripādī being invisible to the ordinary grammar — "
            "**पररूपे कर्तव्ये स्वरितस्य असिद्धत्वात्**: in "
            "पचन्ति both vowels are अनुदात्त, so nothing here "
            "applies, and 8.4.66's स्वरित cannot be seen from "
            "where 6.1.97 stands"),
    Antya(
        "8.2.6", does="svarita", gana="ekādeśa-udātta",
        before=("pada-ādi-anudātta",), optional=True,
        blocks=("8.2.5",),
        why="स्वरितो वाऽनुदात्ते पदादौ — but where the अनुदात्त "
            "began a WORD, the merged vowel is स्वरित or "
            "उदात्त, either: **सु उत्थितः → सूत्थितः** heard "
            "two ways, **वि ईक्षते → वीक्षते**, **वसुकः असि → "
            "वसुकोऽसि**. The सु of सूत्थितः is the "
            "कर्मप्रवचनीय of 1.4.94 — **सुः पूजायाम्** — which "
            "is why it counts as a word of its own and its "
            "vowel is the first of a पद"),
    Antya(
        "8.2.7", does="lopa", gana="prātipadika-n-anta",
        keeps_out="अहन्नहिम् — the न् is not a प्रातिपदिक's; "
                  "राजानौ, राजानः — the न् is not last",
        why="नलोपः प्रातिपदिकान्तस्य — a word that is a "
            "प्रातिपदिक loses its final न्: **राजा, राजभ्याम्, "
            "राजभिः, राजता, राजतरः, राजतमः**. This is the rule "
            "that makes राजन् end in आ in the nominative "
            "singular and keeps the न् out of every ending "
            "beginning with a consonant.\\n\\n"
            "**AND BOTH ITS WORDS ARE TESTED.** "
            "**प्रातिपदिकग्रहणं किम्? अहन्नहिम्** — a verb's "
            "न् is not touched; **अन्तग्रहणं किम्? राजानौ, "
            "राजानः** — a न् that is not last is not touched. "
            "And the naming is of an UNCOMPOUNDED stem: "
            "**प्रातिपदिकग्रहणम् असमस्तम् एव 7.1.39 इति "
            "षष्ठ्या लुका निर्दिष्टम्**"),
    Antya(
        "8.2.8", refuses=True, gana="prātipadika-n-anta",
        before=("ṅi", "sambuddhi"), blocks=("8.2.7",),
        why="न ङिसम्बुद्ध्योः — but not before ङि and not in "
            "the vocative singular: **आर्द्रे चर्मन्; लोहिते "
            "चर्मन्; हे राजन्; हे तक्षन्**. The ङि of the "
            "first pair is dropped by 7.1.39's लुक् and the न् "
            "stays all the same.\\n\\n"
            "**AND THE REFUSAL IS READ AS PROOF ABOUT WHAT A "
            "प्रातिपदिक IS.** **एतस्माद् एव नलोपप्रतिषेधवचनाद् "
            "अप्रत्ययः इति प्रत्ययलक्षणेन प्रातिपदिकसंज्ञा न "
            "प्रतिषिध्यते इति ज्ञाप्यते** — with the ending "
            "gone the word would not be a प्रातिपदिक at all, "
            "and the refusal would have nothing to refuse; that "
            "it is stated shows 1.1.62 keeps the name alive"),
    Antya(
        "8.2.9", does="va", gana="ma-a-anta-upadha",
        before=("matup",),
        keeps_out="यववान्, दलिवान् — the यवादि, which the "
                  "sūtra excepts by name",
        why="मादुपधायाश्च मतोर्वोऽयवादिभ्यः — the म् of मतुप् "
            "becomes व् after a stem ending in म् or अ, or "
            "having म् or अ as its penult, but not after the "
            "यवादि: **किंवान्, शंवान्** after म्; **शमीवान्** "
            "after a म् penult; **वृक्षवान्** after अ. The "
            "sūtra's म् and अ are got by reading the word मत् "
            "as naming the affix and मात् as qualifying both "
            "the end and the penult — **मकारावर्णविशिष्टया च "
            "उपधया इत्ययमर्थो भवति**"),
    Antya(
        "8.2.10", does="va", gana="jhay-anta", before=("matup",),
        why="झयः — and after a झय्-final stem: **अग्निचित्वान् "
            "ग्रामः; उदश्वित्वान् घोषः; विद्युत्वान् बलाहकः; "
            "इन्द्रो मरुत्वान्; दृषद्वान् देशः**. The झय् is "
            "every stop, voiced or not, aspirate or not, which "
            "is the widest of the four conditions the run gives "
            "for this one substitute"),
    Antya(
        "8.2.11", does="va", before=("matup",),
        sense=("saṃjñā",),
        why="संज्ञायाम् — and wherever the word is a NAME, "
            "whatever it ends in: **अहीवती, कपीवती, ऋषीवती, "
            "मुनीवती**. All four are ई-final, which neither "
            "8.2.9 nor 8.2.10 reaches, so the sense is doing "
            "the whole work and the shape none of it"),
    Antya(
        "8.2.12", does="nipātana", of=ASANDIVAT_SIX,
        sense=("saṃjñā",), nipatana=True,
        keeps_out="आसनवान् — the ordinary form, in any other "
                  "sense",
        why="आसन्दीवदष्ठीवच्चक्रीवत्कक्षीवद्रुमण्वच्चर्मण्वती — "
            "six names laid down whole: **आसन्दीवान् ग्रामः; "
            "आसन्दीवद् अहिस्थलम्**. The व् itself was already "
            "available — **वत्वं पूर्वेण एव सिद्धम्, "
            "आदेशार्थानि निपातनानि** — so what each निपातन "
            "gives is the STEM: आसन becomes आसन्दी, and "
            "आसनवान् is what stands anywhere else.\\n\\n"
            "**AND THE KĀŚIKĀ RECORDS A SECOND OPINION.** "
            "**अपरे तु आहुः — आसन्दीशब्दोऽपि प्रकृत्यन्तरम् "
            "एव अस्ति** — that आसन्दी is simply another stem "
            "and no substitution is needed at all"),
    Antya(
        "8.2.13", does="nipātana", of=("udanvat",),
        sense=("udadhi", "saṃjñā"), nipatana=True,
        keeps_out="उदकवान् घटः — a pot with water in it, where "
                  "no holding is meant",
        why="उदन्वानुदधौ च — **उदन्वान्** is laid down: उदक "
            "becomes उदन् before मतुप्, in the sense of the "
            "SEA and as a name. **उदन्वान् नाम ऋषिः; यस्मिन् "
            "उदकं धीयते, स एवम् उच्यते**. And the "
            "counter-example is exact about why the pot is "
            "left out — **उदकवान् घटः इत्यत्र तु दधात्यर्थो न "
            "विवक्ष्यते। किं तर्हि? उदकसत्तासम्बन्धसामान्यम्**: "
            "the pot merely HAS water, the sea HOLDS it"),
    Antya(
        "8.2.14", does="nipātana", of=("rājanvat",),
        sense=("saurājya",), nipatana=True,
        keeps_out="राजवान् — a country that merely has a king",
        why="राजन्वान् सौराज्ये — and **राजन्वान्** where GOOD "
            "GOVERNMENT is meant: **शोभनो राजा यस्मिन् इति स "
            "राजन्वान् देशः; राजन्वती पृथ्वी**. Anywhere else "
            "8.2.7 takes the न् off and राजवान् stands. The "
            "pair is the neatest thing in the run: one word "
            "keeps its न् if the king is a good one"),
    Antya(
        "8.2.15", does="va", gana="i-varṇa-repha-anta",
        before=("matup",), chandasi=True,
        why="छन्दसीरः — and in the VEDA after an इ-final or a "
            "र्-final stem: **त्रिवती याज्यानुवाक्या भवति; "
            "अधिपतिवतीर् जुहोति; चरुर् अग्निवाँ इव** for the "
            "first, and **हरिवो मेदिनं त्वा; आरेवान् एतु मा "
            "विशत्; सरस्वतीवान् भारतीवान्** for the second. "
            "The इ-final case is what 8.2.11 gives outside the "
            "Veda only for a name; here it is general"),
    Antya(
        "8.2.16", does="nuṭ", gana="an-anta", before=("matup",),
        chandasi=True,
        why="अनो नुट् — and after an अन्-final stem मतुप् takes "
            "a नुट् in the Veda: **अक्षण्वन्तः कर्णवन्तः "
            "सखायः; अस्थन्वन्तं यद् अनस्था बिभर्ति; अक्षण्वता "
            "लाङ्गलेन; शीर्षण्वती; मूर्धन्वती**. And the "
            "augment blocks the very substitute this run is "
            "about — **नुटोऽसिद्धत्वात् तस्य च वत्वं न "
            "भवति**: with the न् of नुट् invisible, मतुप् is "
            "not after a म् or an अ and stays a म्"),
    Antya(
        "8.2.17", does="nuṭ", gana="n-anta", before=("gha",),
        chandasi=True,
        why="नाद्घस्य — and after a न्-final stem the घ — that "
            "is तर and तम — takes a नुट् in the Veda: "
            "**सुपथिन्तरः; दस्युहन्तमः**. Two vārttikas widen "
            "it: **भूरिदाव्नस् तुड् वक्तव्यः** for "
            "**भूरिदावत्तरः**, a तुक् and not a नुट्; and "
            "**ईद् रथिनः** for **रथीतरः**, where रथिन् takes "
            "ई before the घ — or, the Kāśikā adds, the ई is "
            "simply a मत्वर्थीय affix on रथ itself"),
    Antya(
        "8.2.18", does="la", of=("kṛp",),
        why="कृपो रो लः — the र् of कृप् becomes ल्: **कल्प्ता, "
            "कल्प्तुम्, कल्प्तव्यम्**. Both letters are named "
            "by their bare sound and not by a class — **र इति "
            "श्रुतिसामान्यम् उपादीयते** — so both a plain रेफ "
            "and the र् inside an ऋ are reached, and what comes "
            "out is either a ल् or a ऌ. That is what makes "
            "1.3.93 लुटि च क्ऌपः intelligible: the root is "
            "written with ऌ there because this rule has already "
            "put one in"),
    Antya(
        "8.2.19", does="la", gana="upasarga", before=("ayati",),
        optional=True,
        why="उपसर्गस्यायतौ — the र् of a PREVERB before अय् "
            "becomes ल्: **प्लायते, पलायते**. The Kāśikā works "
            "through what the sūtra's grammar allows at some "
            "length, and settles it with a paribhāṣā: **येन "
            "नाव्यवधानं तेन व्यवहितेऽपि वचनप्रामाण्यात्** — "
            "where a rule tolerates no gap it may still act "
            "across one on the strength of its being stated, "
            "which is how पल्ययते comes out with a whole sound "
            "in between"),
    Antya(
        "8.2.20", does="la", of=("gṝ",), before=("yaṅ",),
        keeps_out="निगीर्यते — a passive and not a यङ्",
        why="ग्रो यङि — the र् of गॄ becomes ल् before यङ्: "
            "**निजेगिल्यते, निजेगिल्येते, निजेगिल्यन्ते** — "
            "the यङ् being 3.1.24's, given of self-reproach.\\n\\n"
            "**AND THE COMMENTARY SPLITS ON WHICH गॄ IS "
            "MEANT.** **केचिद् ग्र इति गिरतेर् गृणातेश् च "
            "सामान्येन ग्रहणम् इच्छन्ति। अपरे तु गिरतेर् एव, "
            "न गृणातेः। गृणातेर् हि यङ् एव नास्ति, "
            "अनभिधानाद् इति** — one party takes both roots, "
            "the other only 'swallow', since 'praise' has no "
            "यङ् anyone uses"),
    Antya(
        "8.2.21", does="la", of=("gṝ",), before=("ac-ādi",),
        optional=True,
        why="अचि विभाषा — and OPTIONALLY before a vowel-initial "
            "affix: **निगिरति, निगिलति; निगरणम्, निगलनम्; "
            "निगारकः, निगालकः**.\\n\\n"
            "**AND THE OPTION IS NOT THE SPEAKER'S.** **इयं तु "
            "व्यवस्थितविभाषा। तेन गल इति प्राण्यङ्गे नित्यं "
            "लत्वं भवति, गर इति विषे नित्यं न भवति** — a throat "
            "is always गल and poison is always गर. The rule "
            "reads as a free choice and is not one; which "
            "alternative holds is settled by the word. And in "
            "निगार्यते the causal's णि is gone but counts as "
            "there, so the option is available at all"),
    Antya(
        "8.2.22", does="la", of=("pari",),
        before=("gha", "aṅka", "yoga"), optional=True,
        why="परेश्च घाङ्कयोः — and the र् of परि before घ and "
            "अङ्क, optionally: **परिघः, पलिघः; पर्यङ्कः, "
            "पल्यङ्कः**. The घ here is the SOUND and not "
            "1.1.22's name for तर and तम — **घ इति "
            "स्वरूपग्रहणम् अत्र इष्यते** — which the run needs "
            "said, 8.2.17 having used the name five sūtras "
            "back. A vārttika adds a third word: **योगे च इति "
            "वक्तव्यम्। परियोगः, पलियोगः**"),
)


def _reaches(row: Antya, word: str, gana: str, before: str,
             sense: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (word in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Antya, word: str, gana: str) -> int:
    """
    A refusal outweighs the rule it refuses, a named word
    outweighs a shape, and a named sense outweighs a shape too.

    8.2.13 and 8.2.14 are why the sense has to weigh: उदन्वान्
    and राजन्वान् differ from उदकवान् and राजवान् in nothing
    else at all.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of and word in row.of)
        + 5 * len(row.sense)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Changed:
    """What the run answers about a word's end."""

    does: str
    sutra: str
    why: str
    refuses: bool = False
    optional: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def in_the_word(word: str = "", *, gana: str = "",
                before: str = "", sense: str = "",
                chandasi: bool = False) -> Changed:
    """
    8.2.4–22 — the merged vowel's accent, the न् dropped,
    मतुप्'s व्, and र् becoming ल्.

    Nothing answers by default. A word none of these rules
    reaches goes on as it stands.
    """
    matched = [
        row for row in NALOPA_TABLE
        if _reaches(row, word, gana, before, sense, chandasi)
    ]
    if not matched:
        return Changed(
            "", "", "No rule of 8.2.4-22 is reached, so the word "
                    "goes on as it stands")
    row = max(matched, key=lambda one: _how_specific(one, word, gana))
    return Changed(row.does, row.sutra, row.why,
                   refuses=row.refuses, optional=row.optional,
                   nipatana=row.nipatana, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Antya, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NALOPA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Antya", "NALOPA_TABLE", "NALOPA_RUN", "ASIDDHA",
    "ASANDIVAT_SIX", "VYAVASTHITA",
    "Changed", "in_the_word", "provisions_for",
]
