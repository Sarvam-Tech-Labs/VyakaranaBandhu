# -*- coding: utf-8 -*-
"""
४.३.१–३० — the affixes of TIME, and then the senses come back.

4.2 ended by inverting itself. Its first ninety-one rules named a
case-relation and a sense and left the affix to 4.1.83; from 4.2.93 the
rules named only their BASES, and 4.2.93's vṛtti promised that the
senses and the cases would be stated later — **तेषामतः प्रभृत्यर्थाः
समर्थविभक्तयश्च पुरस्ताद् वक्ष्यन्ते**.

This pāda keeps the promise, and 4.3.25 तत्र जातः is where it is kept:
**अणादयो घादयश्च प्रत्ययाः प्रकृताः, तेषामतः प्रभृत्यर्थाः
समर्थविभक्तयश्च निर्दिश्यन्ते** — the affixes are already in hand, and
from here the meanings and the cases are named for them. Its examples
are the outputs of 4.2.93, 4.2.94 and 4.2.95 in order, and `born_in`
answers it by CALLING `in_sense`, because *यथाविहितम्* — *as already
prescribed* — is the whole of what the rule says about which affix.

Before that, 4.3.11 कालाट् ठञ् opens a heading of its own, and its
vṛtti states where it stops: **तत्र जातः इति प्रागतः कालाधिकारः**.
The eighth range in two pādas with both ends written down.

And 4.3.1 records the end of the last one. **देशाधिकारो निवृत्तः** —
the country-heading that entered at 4.2.119 has lapsed, and the vṛtti
of the first rule of the new pāda says so before saying anything else.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: काल heads TWO stretches of this pāda, and each end is stated a
#: different way.
#:
#: The first is bounded in ADVANCE by the rule that opens it —
#: 4.3.11's vṛtti says **तत्र जातः इति प्रागतः कालाधिकारः**, so it
#: runs up to but not including 4.3.25. The second begins when 4.3.43
#: कालात् names the word again in a sūtra of its own, and is closed
#: from BEHIND by 4.3.53's **कालादिति निवृत्तम्**, so its last rule
#: is 4.3.52. One word, two ranges, and both kinds of statement.
KALA_RUNS: Tuple[Tuple[str, str], ...] = (
    ("4.3.11", "4.3.24"),
    ("4.3.43", "4.3.52"),
)

#: The first of them, kept under its own name because the rest of
#: this module and its tests were written when there was only one.
KALA_RUN: Tuple[str, str] = KALA_RUNS[0]

#: The three recensions the vṛtti on 4.3.22 cites, one for each of the
#: three forms it says the rule and its neighbours produce. Held as
#: data because the claim — **तदेवं त्रीणि रूपाणि भवन्ति** — is a
#: claim about attested texts and not about the grammar.
HEMANTA_FORMS: Tuple[Tuple[str, str, str], ...] = (
    ("हैमन्तिकम्", "taittirīya-saṃhitā", "४.४.११.१"),
    ("हैमन्तम्", "paippalāda-saṃhitā", "१७.२९.११"),
    ("हैमनम्", "śaunaka-saṃhitā", "१५.४.१४"),
)


#: The pupils 4.3.104 reaches, as the vṛtti names them — four of
#: Kalāpin and nine of Vaiśampāyana. Held as data because the rule's
#: argument turns on what is in them: **प्रत्यक्षकारिणो गृह्यन्ते,
#: न तु व्यवहिताः शिष्यशिष्याः**, only the DIRECT pupils, and the
#: proof offered is that कलापी stands in the second list and has a
#: rule of his own at 4.3.108 — which would achieve nothing if the
#: pupils of a pupil were already in.
KALAPI_PUPILS: Tuple[str, ...] = ("हरिद्रु", "छगली", "तुम्बुरु", "उलप")
VAISAMPAYANA_PUPILS: Tuple[str, ...] = (
    "आलम्बि", "पलङ्ग", "कमल", "ऋचाभ", "आरुणि", "ताण्ड्य",
    "श्यामायन", "कठ", "कलापी")

#: The rules 4.3.155 points at. **ञिद् यो विकारावयवप्रत्ययः,
#: तदन्तात् प्रातिपदिकादञ्** — from a base ending in a ञित् affix
#: given in these two senses, अञ् again; and the vṛtti does not leave
#: the reader to work out which affixes those are, it lists the rules.
#:
#: Held as data because the list is a claim that can fail: every rule
#: named has to give an affix marked with ञ्, or the condition would
#: not reach what the vṛtti says it reaches.
NIT_AFFIX_RULES: Tuple[str, ...] = (
    "4.3.139", "4.3.142", "4.3.154", "4.3.157", "4.3.159", "4.3.168")

#: And चरक is Vaiśampāyana's own name — **चरक इति वैशंपायनस्याख्या,
#: तत्संबन्धेन सर्वे तदन्तेवासिनश्चरका इत्युच्यन्ते** — which is why
#: 4.3.107 can elide after it and reach the whole school at once.
CARAKA_IS: str = "vaiśampāyana"


@dataclass(frozen=True)
class Kala:
    """One rule of 4.3.1–30: a base, a time, and what comes."""

    sutra: str
    #: What the affix is, or "" where the rule gives none — either
    #: because it enjoins a SUBSTITUTE instead, or because it says
    #: यथाविहितम् and leaves the affix to the rules already in hand.
    gives: str = ""
    #: The other affixes the same rule gives. 4.3.1 gives three at
    #: once and 4.3.23 two, so one string will not hold them. Kept
    #: apart from `gives` so that the first-named affix stays the
    #: one the rule is known by.
    also_gives: Tuple[str, ...] = ()
    of: Tuple[str, ...] = ()
    gana: str = ""
    #: शेष to 4.3.24, and जात from 4.3.25.
    sense: str = ""
    #: A SECOND sense the same row answers under, on equal terms.
    #: 4.3.66's च makes भव and व्याख्यान govern together —
    #: **भवव्याख्यानयोर्युगपदधिकारः** — so 4.3.67 to 4.3.73 are each
    #: stated once for both. Deliberately worth nothing in the
    #: ranking: a rule under two headings is not narrower than one
    #: under a single heading, only reachable from two directions.
    also_sense: str = ""
    #: The case the base stands in. सप्तमी, from 4.3.25 तत्र.
    case: str = ""
    #: A further condition on WHAT the result is — 4.3.12's श्राद्ध,
    #: 4.3.13's रोग and आतप, 4.3.9's सांप्रतिक.
    result: str = ""
    #: A name the grammar has already given the base, or a class it
    #: belongs to: कालविशेष, ऋतु, नक्षत्र, अव्यय, संज्ञा.
    of_samjna: str = ""
    #: What stands in front — 4.3.5's four words, 4.3.6's direction.
    pre: str = ""
    #: What the base ends in. 4.3.6 and 4.3.7 both want अर्ध at the
    #: end of a compound whose first member is a direction.
    stem_final: str = ""
    #: Which register the rule is confined to — छन्दसि for the Veda
    #: at 4.3.19–21 and 4.3.106, भाषा for the spoken language at
    #: 4.3.143 and 4.3.144, and "" for the rules that hold in both.
    #:
    #: One column and not two flags. A rule belongs to one register,
    #: the other, or neither, and two booleans would let a row claim
    #: both — the same reason बह्वच् and द्व्यच् share `vowels`.
    usage: str = ""
    #: The PENULTIMATE sound. 4.3.137 कोपधाच्च is stated on it, and
    #: उपधा is not the final: a base whose penultimate is क does not
    #: end in क. The same column `sense_taddhita` needed at 4.2.132.
    upadha: str = ""
    #: True where the rule REFUSES. 4.3.130 न दण्डमाणवान्तेवासिषु is
    #: the only one in this pāda.
    refuses: bool = False
    #: How many vowels the base has — बह्वच् at 4.3.67, द्व्यच् at
    #: 4.3.72, एकाच् in the counter-example between them. One column
    #: and not two booleans, because the two rules are the halves of
    #: one question: बह्वच इति किम्? **द्व्यचष्ठकं वक्ष्यति**.
    vowels: str = ""
    #: The accent the base must carry. 4.3.67 wants अन्तोदात्त, and
    #: its counter-example turns on a compound-accent placed by a
    #: quite different rule — संहिताशब्दो हि गतिस्वरेणाद्युदात्तः.
    accent: str = ""
    #: The rule whose affixes this one BORROWS. Two rules of this
    #: pāda do it, in opposite directions: 4.3.80 गोत्रादङ्कवत्
    #: reaches ninety-seven sūtras FORWARD to a rule not yet
    #: codified, and 4.3.100 जनपदिनां जनपदवत् reaches BACKWARD to
    #: 4.2.124, which is codified — so one can only be named and the
    #: other is executed.
    borrows_from: str = ""
    #: What the borrower asks the other rule, as (field, value)
    #: pairs. **सर्वग्रहणं प्रकृत्यतिदेशार्थम्** — 4.3.100's *all* is
    #: there so that the BASE is borrowed too and not only the affix,
    #: and handing the other resolver a different संज्ञा is what that
    #: comes to in code.
    #:
    #: 4.3.80 needs more than a संज्ञा: it asks under a different
    #: SENSE and a different CASE as well, because the affixes it
    #: borrows are given in तस्येदम् and it is stated in आगत.
    borrow_query: Tuple[Tuple[str, str], ...] = ()
    #: What the rule puts in place of the base. 4.3.2, 4.3.3 and
    #: 4.3.29 give a substitute and no affix of their own.
    replaces: str = ""
    #: The affix in whose presence the substitution happens. 4.3.2
    #: says **तस्मिन्** and means the खञ् *directly enjoined*, not
    #: the छ the previous rule's च dragged in.
    before: str = ""
    #: An आगम the same rule adds — तुट् at 4.3.15, 4.3.23, 4.3.24.
    augment: str = ""
    #: A sound the rule drops in the same act — 4.3.22's तकारलोप.
    drops: str = ""
    #: True where the rule takes the affix AWAY rather than giving
    #: one. 4.3.34–37 are लुक् rules, and 1.2.49 makes the feminine
    #: affix go with it.
    elides: bool = False
    #: True where the removal is लुप् and not लुक्. The two are not
    #: the same: **लुकि प्राप्ते लुपो विधाने युक्तवद्भावे
    #: स्त्रीप्रत्ययश्रवणे च विशेषः** — under लुप् 1.2.51 makes what
    #: is left agree with the word the affix was on, and the feminine
    #: affix is still heard. हरीतक्याः फलानि **हरीतक्यः**: the
    #: gender follows the original and the number follows what is
    #: denoted.
    lup: bool = False
    #: बहुलम् — VARIOUSLY, which is not विभाषा. 4.3.37 says it, and
    #: 4.3.36's vṛtti says the three rules before it are
    #: **बहुलग्रहणस्यायं प्रपञ्चः**, an unfolding of that one word.
    #: So an option and a variousness are related here and still not
    #: the same thing, and the table keeps them in separate columns.
    bahulam: bool = False
    optional: bool = False
    #: Whose reading this is, where the vṛtti attributes it. 4.3.27
    #: reports that **केचित्** carry the संज्ञा heading to 4.3.38.
    authority: str = ""
    excepts: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


KALA_TABLE: Tuple[Kala, ...] = (
    Kala("4.3.1", sense="śeṣa", gives="khañ", also_gives=("cha", "aṇ"),
         of=("yuṣmad", "asmad"), optional=True,
         why="युष्मदस्मदोरन्यतरस्यां खञ् च. **देशाधिकारो निवृत्तः** — "
             "the country-heading that opened at 4.2.119 has lapsed, "
             "and the first vṛtti of the new pāda says so before it "
             "says anything else.\n\n"
             "चकाराच् छश्च, and **अन्यतरस्यांग्रहणाद् यथाप्राप्तम्** "
             "lets अण् in besides: **तदेते त्रयः प्रत्यया भवन्ति**. "
             "यौष्माकीणः, आस्माकीनः; युष्मदीयः, अस्मदीयः; यौष्माकः, "
             "आस्माकः.\n\n"
             "**AND यथासंख्य FAILS BECAUSE THE NUMBERS DO NOT MATCH.** "
             "तत्र **वैषम्याद् यथासंख्यं न भवति** — two bases and "
             "three affixes, so 1.3.10's pairing cannot run and each "
             "base takes all three. 4.2.80 paired seventeen with "
             "seventeen; here two against three pairs with nothing"),
    Kala("4.3.2", of=("yuṣmad",), replaces="yuṣmāka", before="khañ",
         sense="śeṣa",
         why="तस्मिन्नणि च युष्माकास्माकौ. **तस्मिन्निति साक्षाद् "
             "विहितः खञ् निर्दिश्यते, न चकारानुकृष्टश्छः** — *that* "
             "means the खञ् the last rule ENJOINED, not the छ its च "
             "dragged in. A pronoun in a rule picking out one of two "
             "affixes by how each of them got there.\n\n"
             "यौष्माकीणः, यौष्माकः. तस्मिन्नणि चेति किम्? युष्मदीयः "
             "— where the छ came instead, and no substitute with it",
         keeps_out="युष्मदीयः"),
    Kala("4.3.2", of=("asmad",), replaces="asmāka", before="khañ",
         sense="śeṣa",
         why="तस्मिन्नणि च युष्माकास्माकौ, the अस्मद् half. "
             "आस्माकीनः, आस्माकः.\n\n"
             "**निमित्तयोरादेशौ प्रति यथासंख्यं कस्माद् न भवति?** If "
             "यथासंख्य pairs the two bases with the two substitutes, "
             "why does it not also pair them with the two affixes "
             "खञ् and अण्? **योगविभागः करिष्यते** — the rule is read "
             "as two: *in that खञ्, these two substitutes for these "
             "two words*, and then *and in अण् too*. A split made to "
             "stop a correspondence from running where it should not",
         keeps_out="अस्मदीयः"),
    Kala("4.3.3", of=("yuṣmad",), replaces="tavaka", before="khañ",
         of_samjna="ekavacana", sense="śeṣa",
         why="तवकममकावेकवचने. तावकीनः, तावकः. तस्मिन्नणि चेत्येव — "
             "त्वदीयः.\n\n"
             "**AND A TECHNICAL TERM IS READ UNTECHNICALLY TO ESCAPE A "
             "PARIBHĀṢĀ.** ननु च **न लुमताङ्गस्य** [1.1.63] इति "
             "प्रत्ययलक्षणप्रतिषेधाद् एकवचनपरता युष्मदस्मदोर्न "
             "संभवति? — the singular ending is gone, and 1.1.63 "
             "forbids treating an affix as present once it is; so the "
             "word cannot be *followed by a singular* at all. Two "
             "answers are offered. **वचनात् प्रत्ययलक्षणं भविष्यति**: "
             "the rule's own statement restores it. Or better — "
             "**नैवेदं प्रत्ययग्रहणम्, किं तर्हि? अन्वर्थग्रहणम्**: "
             "एकवचन here is not the NAME of an affix but the words "
             "read for their meaning, *denoting one thing*. A term "
             "the grammar defined, taken in this one rule the way "
             "anyone would take it",
         keeps_out="त्वदीयः"),
    Kala("4.3.3", of=("asmad",), replaces="mamaka", before="khañ",
         of_samjna="ekavacana", sense="śeṣa",
         why="तवकममकावेकवचने, the अस्मद् half. मामकीनः, मामकः. "
             "**निमित्तयोस्तु यथासंख्यं पूर्ववदेव न भवति** — and the "
             "pairing is stopped between the two causes here for the "
             "same reason as in the rule before",
         keeps_out="मदीयः"),
    Kala("4.3.4", of=("ardha",), gives="yat", sense="śeṣa",
         excepts=("4.1.83",),
         why="अर्धाद् यत्, अणोऽपवादः. अर्ध्यम्.\n\n"
             "**सपूर्वपदाट् ठञ् वक्तव्यः** — a vārttika gives ठञ् "
             "instead where something stands in front: बालेयार्धिकम्, "
             "गौतमार्धिकम्. The same word, and the affix decided by "
             "whether it is alone"),
    Kala("4.3.5", of=("ardha",), gives="yat", sense="śeṣa",
         pre="para-avara-adhama-uttama",
         why="परावराधमोत्तमपूर्वाच्च. परार्ध्यम्, अवरार्ध्यम्, "
             "अधमार्ध्यम्, उत्तमार्ध्यम्.\n\n"
             "**पूर्वग्रहणं किम्?** Why say *preceded by*, when "
             "अर्धात् carries over and the four could simply have "
             "been named? Because **परावरशब्दौ अदिग्ग्रहणावपि स्तः** "
             "— पर and अवर are also ordinary words, परं सुखम्, अवरं "
             "सुखम्, and on THAT reading they are direction-words "
             "besides. **तत्र कृतार्थत्वाद् दिक्छब्दपक्षे परेण "
             "ठञ्यतौ स्याताम्**: the next rule would then give ठञ् as "
             "well. The one word पूर्व secures यत् alone"),
    Kala("4.3.6", pre="dik", stem_final="ardha", gives="ṭhañ",
         also_gives=("yat",), sense="śeṣa", excepts=("4.1.83",),
         why="दिक्पूर्वपदाट् ठञ् च, अणोऽपवादः. पौर्वार्धिकम् beside "
             "पूर्वार्ध्यम्; दाक्षिणार्धिकम् beside दक्षिणार्ध्यम्.\n\n"
             "**पदग्रहणं स्वरूपविधिनिवारणार्थम्** — *word* is there "
             "so the rule is not read as being about the शब्द दिश् "
             "itself. The identical argument as 4.2.107's, and the "
             "identical word doing it"),
    Kala("4.3.7", pre="dik", stem_final="ardha", gives="añ",
         also_gives=("ṭhañ",), sense="śeṣa",
         of_samjna="grāma-janapada-ekadeśa", excepts=("4.3.6",),
         why="ग्रामजनपदैकदेशादञ्ठञौ, **यतोऽपवादौ** — both of them "
             "beat the यत् of the rule before. इमे खल्वस्माकं "
             "ग्रामस्य जनपदस्य वा पौर्वार्धाः, पौर्वार्धिकाः; "
             "दाक्षिणार्धाः, दाक्षिणार्धिकाः.\n\n"
             "A PART of a village or of a district, named by the "
             "direction it lies in — and two affixes for it, with no "
             "option stated, so both stand"),
    Kala("4.3.8", of=("madhya",), gives="ma", sense="śeṣa",
         excepts=("4.1.83",),
         why="मध्यान्मः, अणोऽपवादः. मध्यमः.\n\n"
             "Two vārttikas ride with it. **आदेश्चेति वक्तव्यम्** — "
             "आदिम, the first one, on the same pattern. And "
             "**अवोऽधसोर्लोपश्च**: from अव and अधस् with the "
             "final dropped, अवमम् and अधमम्. Three of the "
             "commonest ordinals in the language, and the grammar "
             "makes them by one affix and two supplements"),
    Kala("4.3.9", of=("madhya",), gives="a", sense="śeṣa",
         result="sāmpratika", excepts=("4.3.8",),
         why="अ साम्प्रतिके, मस्यापवादः. The sense is glossed with "
             "five words at once: **सांप्रतिकं न्याय्यं युक्तम् "
             "उचितं सममुच्यते** — fitting, proper, apt, becoming, "
             "even.\n\n"
             "नातिदीर्घं नातिह्रस्वं **मध्यं काष्ठम्** — a stick "
             "neither too long nor too short. नात्युत्कृष्टो "
             "नात्यवकृष्टो **मध्यो वैयाकरणः** — a grammarian neither "
             "outstanding nor bad. मध्या स्त्री. The affix is a bare "
             "अ and the whole rule is two syllables long"),
    Kala("4.3.10", of=("dvīpa",), gives="yañ", sense="śeṣa",
         of_samjna="anusamudra", excepts=("4.2.133", "4.2.134"),
         why="द्वीपादनुसमुद्रं यञ्. An island NEAR THE SEA — "
             "समुद्रसमीपे यो द्वीपः. **कच्छादिपाठाद् अणो "
             "मनुष्यवुञश्चापवादः**: द्वीप is in 4.2.133's कच्छादि "
             "list, so this rule has to beat both that rule's अण् "
             "and 4.2.134's वुञ्.\n\n"
             "द्वैप्यम्, and a line quoted for it — द्वैप्यं "
             "भवन्तोऽनुचरन्ति चक्रम्. अनुसमुद्रमिति किम्? द्वैपकम्, "
             "which is 4.2.134's form; **द्वैपमन्यत्**, and "
             "4.2.133's for everything else. One word with three "
             "affixes decided by three rules in two pādas",
         keeps_out="द्वैपकम्, द्वैपम्"),
    Kala("4.3.11", of_samjna="kāla", gives="ṭhañ", sense="śeṣa",
         excepts=("4.1.83", "4.2.114"),
         why="कालाट् ठञ्, अणोऽपवादः; **वृद्धात् तु छं परत्वाद् "
             "बाधते**, and it beats 4.2.114's छ by standing later. "
             "मासिकः, आर्धमासिकः, सांवत्सरिकः.\n\n"
             "**AND A FIGURATIVE TIME IS STILL A TIME.** "
             "यथाकथंचिद् **गुणवृत्त्यापि काले वर्तमानात् प्रत्यय "
             "इष्यते** — the affix is wanted even from a word that "
             "denotes a time only by transferring a quality to it. "
             "कादम्बपुष्पिकम्, *of the kadamba-blossom season*; "
             "ब्रैहिपलालिकम्, *of the rice-straw season*. The season "
             "is named by what happens in it.\n\n"
             "**तत्र जातः इति प्रागतः कालाधिकारः** — and the vṛtti "
             "says where the heading stops: up to 4.3.25 and not "
             "into it"),
    Kala("4.3.12", of=("śarad",), gives="ṭhañ", sense="śeṣa",
         result="śrāddha", excepts=("4.3.16",),
         why="श्राद्धे शरदः, ऋत्वणोऽपवादः. शारदिकं श्राद्धम्; "
             "**शारदमन्यत्**.\n\n"
             "**श्राद्ध इति च कर्म गृह्यते, न श्रद्धावान् पुरुषः, "
             "अनभिधानात्** — श्राद्ध here is the RITE and not a man "
             "of faith, *because that is not how the word is used*. "
             "A meaning excluded on the ground of usage rather than "
             "of any rule",
         keeps_out="शारदं दधि"),
    Kala("4.3.13", of=("śarad",), gives="ṭhañ", sense="śeṣa",
         result="roga-ātapa", optional=True, excepts=("4.3.16",),
         why="विभाषा रोगातपयोः, शरद इत्येव; ऋत्वणोऽपवादः. शारदिको "
             "रोगः beside शारदो रोगः; शारदिक आतपः beside शारद "
             "आतपः — the autumn fever and the autumn heat. "
             "रोगातपयोरिति किम्? शारदं दधि",
         keeps_out="शारदं दधि"),
    Kala("4.3.14", of=("niśā", "pradoṣa"), gives="ṭhañ", sense="śeṣa",
         optional=True, excepts=("4.3.11",),
         why="निशाप्रदोषाभ्यां च. **कालाट् ठञ् इति नित्ये ठञि "
             "प्राप्ते विकल्प उच्यते** — 4.3.11 gave the ठञ् without "
             "an option, so the option is spoken against it. "
             "नैशिकम् beside नैशम्; प्रादोषिकम् beside प्रादोषम्"),
    Kala("4.3.15", of=("śvas",), gives="ṭhañ", also_gives=("ṭyu", "ṭyul"),
         sense="śeṣa", optional=True, augment="tuṭ",
         excepts=("4.3.11",),
         why="श्वसस्तुट् च, विभाषेत्येव. शौवस्तिकः — the ठञ् with तुट् "
             "prefixed to it.\n\n"
             "**AND THE OPTION LEAVES ROOM FOR THREE MORE AFFIXES.** "
             "त्यप् is given from the same word by 4.2.105 "
             "ऐषमोह्यःश्वसोऽन्यतरस्याम्, and **एताभ्यां मुक्ते "
             "ट्युट्युलावपि भवतः** — where both of those are let go, "
             "the ट्यु and ट्युल् of 4.3.23 come. शौवस्तिकः, श्वस्त्यः, "
             "श्वस्तनः: three forms of *of tomorrow*, from three "
             "rules in two pādas"),
    Kala("4.3.16", gana="saṃdhivelādi", gives="aṇ", sense="śeṣa",
         excepts=("4.3.11", "4.2.114"),
         why="संधिवेलाद्यृतुनक्षत्रेभ्योऽण्, the संधिवेलादि member; "
             "ठञोऽपवादः. सांधिवेलम्, सांध्यम्.\n\n"
             "**अण्ग्रहणं वृद्धाच्छस्य बाधनार्थम्** — the default "
             "named in order to beat 4.2.114, which would otherwise "
             "have taken the ground by standing later than 4.3.11 "
             "does not. **The default named to beat its beater**, the "
             "same instrument as 4.2.110's and 4.2.132's.\n\n"
             "A गणसूत्र rides with the list: **संवत्सरात् "
             "फलपर्वणोः** — सांवत्सरं फलम्, सांवत्सरं पर्व, from "
             "संवत्सर when a fruit or a festival is meant"),
    Kala("4.3.16", of_samjna="ṛtu", gives="aṇ", sense="śeṣa",
         excepts=("4.3.11", "4.2.114"),
         why="संधिवेलाद्यृतुनक्षत्रेभ्योऽण्, the ऋतु member — a word "
             "naming a SEASON. ग्रैष्मम्, शैशिरम्. The rule reaches "
             "them **कालवृत्तिभ्यः**, only as words that denote a "
             "time, which is what ties it to 4.3.11's heading"),
    Kala("4.3.16", of_samjna="nakṣatra", gives="aṇ", sense="śeṣa",
         excepts=("4.3.11", "4.2.114"),
         why="संधिवेलाद्यृतुनक्षत्रेभ्योऽण्, the नक्षत्र member — a "
             "word naming a LUNAR MANSION. तैषम्, पौषम्. The names "
             "of the months are made this way, from the mansion the "
             "full moon stands in"),
    Kala("4.3.17", of=("prāvṛṣ",), gives="eṇya", sense="śeṣa",
         excepts=("4.3.16",),
         why="प्रावृष एण्यः, ऋत्वणोऽपवादः. **प्रावृषेण्यो बलाहकः** — "
             "the cloud of the rains, and the word survives in "
             "poetry long after the grammar that made it"),
    Kala("4.3.18", of=("varṣā",), gives="ṭhak", sense="śeṣa",
         excepts=("4.3.16",),
         why="वर्षाभ्यष्ठक्, ऋत्वणोऽपवादः. वार्षिकं वासः, "
             "वार्षिकमनुलेपनम् — the cloak for the rains and the "
             "ointment for them"),
    Kala("4.3.19", of=("varṣā",), gives="ṭhañ", sense="śeṣa",
         usage="chandasi", excepts=("4.3.18",),
         why="छन्दसि ठञ्, ठकोऽपवादः. **स्वरे भेदः** — and the "
             "difference between the two affixes is in the ACCENT "
             "and nowhere else, since ठक् and ठञ् both become इक. "
             "नभश्च नभस्यश्च **वार्षिकावृतू** (तैत्तिरीयसंहिता "
             "४.४.११.१)"),
    Kala("4.3.20", of=("vasanta",), gives="ṭhañ", sense="śeṣa",
         usage="chandasi", excepts=("4.3.16",),
         why="वसन्ताच्च, छन्दसीत्येव; ऋत्वणोऽपवादः. मधुश्च माधवश्च "
             "**वासन्तिकावृतू** (तैत्तिरीयसंहिता ४.४.११.१) — the "
             "same verse of the same recension that the last rule "
             "was quoted from, and the next one too"),
    Kala("4.3.21", of=("hemanta",), gives="ṭhañ", sense="śeṣa",
         usage="chandasi", excepts=("4.3.16",),
         why="हेमन्ताच्च, छन्दसीत्येव. सहश्च सहस्यश्च "
             "**हैमन्तिकावृतू** (तैत्तिरीयसंहिता ४.४.११.१).\n\n"
             "**योगविभाग उत्तरार्थः** — and the rule is split off "
             "from the one before it only so that the NEXT rule has "
             "something to be stated of"),
    Kala("4.3.22", of=("hemanta",), gives="aṇ", sense="śeṣa", drops="t",
         why="सर्वत्राण् च तलोपश्च. हैमनं वासः, हैमनमुपलेपनम् — the "
             "अण् with the त of हेमन्त dropped in the same act.\n\n"
             "**सर्वत्रग्रहणं छन्दोऽधिकारनिवृत्त्यर्थम्** — "
             "*everywhere* is there to cancel the Vedic heading, and "
             "the vṛtti presses the point: ननु च छन्दसीति "
             "नानुवर्तिष्यते? If it simply would not have carried, "
             "why spend a word? **सैवाननुवृत्तिः शब्देनाख्यायते "
             "प्रयत्नाधिक्येन पूर्वसूत्रेऽपि संबन्धार्थम्** — the "
             "not-carrying is SAID, with deliberate extra effort, so "
             "that it reaches back and touches the previous rule too. "
             "हैमन्तिकमिति हि भाषायामपि ठञं स्मरन्ति.\n\n"
             "**AND THE च GATHERS A SECOND अण् THAT IS NOT THIS "
             "ONE.** अथाण्चेति चकारः किमर्थः? अण्, **यथाप्राप्तं च "
             "ऋत्वण्** — this rule's अण् and 4.3.16's, both. कः "
             "पुनरनयोरणोर्विशेषः? **ऋत्वणि हि तकारलोपो नास्ति** — "
             "the season-अण् drops no त, हैमन्ती पङ्क्तिः. Two "
             "affixes of the same shape told apart by what else "
             "happens beside them"),
    Kala("4.3.23", of=("sāyam", "ciram", "prāhṇe", "prage"), gives="ṭyu",
         also_gives=("ṭyul",), sense="śeṣa", augment="tuṭ",
         why="सायंचिरम्प्राह्णेप्रगेऽव्ययेभ्यष्ट्युट्युलौ तुट् च, "
             "कालादित्येव. सायंतनम्, चिरंतनम्, प्राह्णेतनम्, "
             "प्रगेतनम्.\n\n"
             "**AND THREE OF THE FOUR SHAPES ARE MADE BY THE RULE "
             "ITSELF.** सायम् is already an indeclinable ending in "
             "म्, so the affix would have come anyway; but the "
             "म-ending of the सायशब्द — from स्यति in the sense of "
             "ENDING, दिवसावसानं सायः — is **प्रत्ययसन्नियोगेन "
             "निपात्यते**, laid down together with the affix. So is "
             "चिर's, and so is the ए of प्राह्णे and प्रगे. A rule "
             "that gives an affix and makes the words it attaches to"),
    Kala("4.3.23", of_samjna="avyaya", gives="ṭyu", also_gives=("ṭyul",),
         sense="śeṣa", augment="tuṭ",
         why="सायंचिरम्प्राह्णेप्रगेऽव्ययेभ्यष्ट्युट्युलौ तुट् च, the "
             "अव्ययेभ्यः member — from any indeclinable that denotes "
             "a time. दोषातनम्, दिवातनम्.\n\n"
             "Four vārttikas ride with the rule. "
             "**चिरपरुत्परारिभ्यस्त्नो वक्तव्यः** — चिरत्नम्, "
             "परुत्नम्, परारित्नम्. **प्रगस्त छन्दसि गलोपश्च**: "
             "प्रत्नम् (ऋग्वेद १.३६.४), where the ग goes and the "
             "word is one of the oldest in the language. "
             "**अग्रपश्चाड्डिमच्** — अग्रिमम्, पश्चिमम्. And "
             "**अन्ताच्चेति वक्तव्यम्** — अन्तिमम्. Between them "
             "they account for *first*, *last*, and *western*"),
    Kala("4.3.24", of=("pūrvāhṇa", "aparāhṇa"), gives="ṭyu",
         also_gives=("ṭyul",), sense="śeṣa", augment="tuṭ",
         optional=True, excepts=("4.3.11",),
         why="विभाषा पूर्वाह्णापराह्णाभ्याम्. **कालाट् ठञ् इति ठञि "
             "प्राप्ते वचनम्, पक्षे सोऽपि भवति** — 4.3.11 had the "
             "ground, so on the other side of the option its ठञ् "
             "comes back: पूर्वाह्णेतनम् and आपराह्णिकम् both.\n\n"
             "**AND THE CASE-ENDING SURVIVES INSIDE THE COMPOUND.** "
             "**घकालतनेषु कालनाम्नः** [6.3.17] इति सप्तम्या अलुक् — "
             "before these affixes a time-word keeps its locative, "
             "which is why the form is पूर्वाह्णेतनम् and not "
             "पूर्वाह्णतनम्. यदा तु न सप्तमी समर्थविभक्तिः — "
             "पूर्वाह्णः सोढोऽस्य — **तदा पूर्वाह्णतन इति "
             "भवितव्यम्**: change the relation and the ending goes. "
             "The visible form reports which case-relation was meant"),
    Kala("4.3.25", case="saptamī", sense="jāta",
         why="तत्र जातः.\n\n"
             "**AND THE PROMISE MADE AT 4.2.93 IS KEPT.** "
             "**अणादयो घादयश्च प्रत्ययाः प्रकृताः, तेषामतः "
             "प्रभृत्यर्थाः समर्थविभक्तयश्च निर्दिश्यन्ते** — the "
             "affixes from अण् onward and from घ onward are already "
             "in hand, and from here the SENSES they carry and the "
             "CASES they attach in are named for them. 4.2.93's "
             "vṛtti said this would happen, in nearly the same "
             "words, fifty-eight sūtras ago.\n\n"
             "So the rule names no affix. **यथाविहितं प्रत्ययो "
             "भवति** — whichever was already prescribed. Its "
             "examples are the outputs of 4.2.93, 4.2.94 and 4.2.95 "
             "read off in order: स्रुघ्ने जातः स्रौघ्नः, माथुरः, "
             "औत्सः, औदपानः; राष्ट्रियः, अवारपारीणः; शाकलिकः, "
             "माकलिकः; ग्राम्यः, ग्रामीणः; कात्रेयकः, औम्भेयकः"),
    Kala("4.3.26", of=("prāvṛṣ",), gives="ṭhap", case="saptamī",
         sense="jāta", excepts=("4.3.17",),
         why="प्रावृषष्ठप्, एण्यस्यापवादः. प्रावृषि जातः प्रावृषिकः.\n\n"
             "**पकारः स्वरार्थः** — the प is for the accent and for "
             "nothing else; ठ् alone would have made the same इक"),
    Kala("4.3.27", of=("śarad",), gives="vuñ", case="saptamī",
         sense="jāta", of_samjna="saṃjñā", excepts=("4.3.16",),
         why="संज्ञायां शरदो वुञ्, ऋत्वणोऽपवादः, **समुदायेन चेत् "
             "संज्ञा गम्यते** — if the NAME is understood from the "
             "whole and not from the parts. शारदका दर्भाः, शारदका "
             "मुद्गाः: a particular grass and a particular bean, and "
             "the word is the name of the kind. संज्ञायामिति किम्? "
             "शारदं सस्यम्.\n\n"
             "**संज्ञाधिकारं केचित् कृतलब्धक्रीतकुशलाः इति यावद् "
             "अनुवर्तयन्ति** — and SOME carry the संज्ञा heading all "
             "the way to 4.3.38. A range with both ends stated and "
             "an authority named for it, which is not the same as a "
             "range the tradition agrees on",
         authority="kecit", keeps_out="शारदं सस्यम्"),
    Kala("4.3.28", gana="pūrvāhṇādi", gives="vun", case="saptamī",
         sense="jāta", of_samjna="saṃjñā",
         excepts=("4.3.24", "4.3.16", "4.3.14", "4.1.83"),
         why="पूर्वाह्णापराह्णार्द्रामूलप्रदोषावस्करादद्वुन्, "
             "संज्ञायां गम्यमानायाम्. And the vṛtti pairs each base "
             "with the rule it beats: पूर्वाह्णकः, अपराह्णकः against "
             "4.3.24; आर्द्रकः, मूलकः **नक्षत्राणोऽपवादः** against "
             "4.3.16; प्रदोषकः against 4.3.14; अवस्करकः "
             "**औत्सर्गिकस्याणोऽपवादः** against 4.1.83. Six bases and "
             "four different rules displaced.\n\n"
             "**असंज्ञायां तु यथाप्राप्तं ठञादय एव भवन्ति** — and "
             "where no name is meant, each of those four takes its "
             "ground back",
         keeps_out="पौर्वाह्णिकम्"),
    Kala("4.3.29", of=("pathin",), gives="vun", replaces="pantha",
         case="saptamī", sense="jāta", excepts=("4.1.83",),
         why="पथः पन्थ च, अणोऽपवादः. पथि जातः **पन्थकः** — the affix "
             "and the substitute **प्रत्ययसन्नियोगेन**, in one act, "
             "so that neither stands without the other"),
    Kala("4.3.30", of=("amāvāsyā",), gives="vun", case="saptamī",
         sense="jāta", optional=True, excepts=("4.3.16",),
         why="अमावास्याया वा. अमावास्यकः beside आमावास्यः — "
             "अमावास्या is in 4.3.16's संधिवेलादि list, so the अण् "
             "stands on the other side of the option.\n\n"
             "**एकदेशविकृतस्यानन्यत्वात्** — *a thing altered in one "
             "part is not a different thing* — the rule reaches "
             "अमावस्या as well: अमावस्यकः, आमावस्यः. A named maxim "
             "doing the work that a second entry in the rule would "
             "otherwise have had to do"),
    Kala("4.3.31", of=("amāvāsyā",), gives="a", case="saptamī",
         sense="jāta",
         why="अ च. **पूर्वेण वुन्नणोः प्राप्तयोरयं तृतीयः प्रत्ययो "
             "विधीयते** — two affixes were already available and this "
             "is a THIRD. With the variant spelling the last rule let "
             "in, the count comes to six: अमावास्यः, अमावास्यकः, "
             "आमावास्यः; अमावस्यः, अमावस्यकः, आमावस्यः. Three affixes "
             "times two shapes of one word, and the second shape is "
             "there only because एकदेशविकृतस्यानन्यत्वात्"),
    Kala("4.3.32", of=("sindhu", "apakara"), gives="kan", case="saptamī",
         sense="jāta", excepts=("4.2.133", "4.2.134", "4.1.83"),
         why="सिन्ध्वपकराभ्यां कन्. सिन्धुकः, अपकरकः. "
             "**सिन्धुशब्दः कच्छादिः, ततोऽणि मनुष्यवुञि च प्राप्ते "
             "विधानम्** — सिन्धु is in 4.2.133's list, so this rule "
             "has 4.2.133's अण् and 4.2.134's वुञ् to beat; from "
             "अपकर it beats only the general default"),
    Kala("4.3.33", of=("sindhu",), gives="aṇ", case="saptamī",
         sense="jāta", excepts=("4.3.32",),
         why="अणञौ च, यथासंख्यम्; the सिन्धु half. सैन्धवः. "
             "**पूर्वेण कनि प्राप्ते वचनम्** — the last rule gave "
             "कन् on this ground, so these two are spoken against it "
             "and all three stand"),
    Kala("4.3.33", of=("apakara",), gives="añ", case="saptamī",
         sense="jāta", excepts=("4.3.32",),
         why="अणञौ च, the अपकर half. आपकरः. Two bases and two "
             "affixes, matched in order — 1.3.10's यथासंख्य running "
             "where 4.3.1's could not, because here the counts are "
             "equal"),
    Kala("4.3.34", gana="śraviṣṭhādi", of_samjna="nakṣatra",
         case="saptamī", sense="jāta", elides=True,
         why="श्रविष्ठाफल्गुन्यनुराधास्वातितिष्यपुनर्वसुहस्तविशाखाषाढा"
             "बहुलाल्लुक्. श्रविष्ठासु जातः **श्रविष्ठः** — the affix "
             "given and then taken away, and what is left is the "
             "mansion's own name used of the person born under it. "
             "फल्गुनः, अनुराधः, स्वातिः, तिष्यः, पुनर्वसुः, हस्तः, "
             "विशाखः, अषाढः, बहुलः.\n\n"
             "**AND THE FEMININE AFFIX GOES WITH IT.** तस्मिन् "
             "स्त्रीप्रत्ययस्यापि **लुक् तद्धितलुकि** [1.2.49] इति "
             "लुग् भवति — श्रविष्ठा is feminine, and when the "
             "taddhita goes the feminine affix goes too, by a rule "
             "stated for exactly this.\n\n"
             "**AND THEN A DIFFERENT RULE PUTS ONE BACK.** A vārttika "
             "adds three words in the feminine — "
             "**लुक्प्रकरणे चित्रारेवतीरोहिणीभ्यः स्त्रियामुपसंख्यानम्** "
             "— चित्रायां जाता चित्रा, रेवती, रोहिणी; and "
             "**स्त्रीप्रत्ययस्य लुकि कृते गौरादित्वाद् ङीष्**: once "
             "1.2.49 has removed the feminine affix, 4.1.41 supplies "
             "another, because the stem is in the गौरादि list. An "
             "affix elided and a different one given in its place.\n\n"
             "Two more vārttikas: **फल्गुन्यषाढाभ्यां टानौ** — "
             "फल्गुनी, अषाढा; and **श्रविष्ठाषाढाभ्यां छणपि** — "
             "श्राविष्ठीयः, आषाढीयः"),
    Kala("4.3.35", stem_final="sthāna", case="saptamī", sense="jāta",
         elides=True,
         why="स्थानान्तगोशालखरशालाच्च, the स्थानान्त half. गोस्थाने "
             "जातो **गोस्थानः**; अश्वस्थानः"),
    Kala("4.3.35", of=("gośāla", "kharaśāla"), case="saptamī",
         sense="jāta", elides=True,
         why="स्थानान्तगोशालखरशालाच्च, the two named words. गोशालः, "
             "खरशालः — the cow-shed and the donkey-shed, and a person "
             "born in one is called by the shed's own name"),
    Kala("4.3.36", of=("vatsaśālā", "abhijit", "aśvayuj", "śatabhiṣaj"),
         case="saptamī", sense="jāta", elides=True, optional=True,
         why="वत्सशालाभिजिदश्वयुक्छतभिषजो वा. वत्सशालायां जातो "
             "वत्सशालः beside वात्सशालः; अभिजित् beside आभिजितः; "
             "अश्वयुक् beside आश्वयुजः; शतभिषक् beside शातभिषजः.\n\n"
             "**बहुलग्रहणस्यायं प्रपञ्चः** — and the vṛtti reads this "
             "rule, and the two before it, as an UNFOLDING of the one "
             "word बहुलम् in the rule that follows. Three rules "
             "spelling out what a single word of the fourth would "
             "have covered"),
    Kala("4.3.37", of_samjna="nakṣatra", case="saptamī", sense="jāta",
         elides=True, bahulam=True,
         why="नक्षत्रेभ्यो बहुलम्. रोहिणः beside रौहिणः; मृगशिराः "
             "beside मार्गशीर्षः.\n\n"
             "**बहुलम् IS NOT विभाषा.** An option says the affix may "
             "come or not; *variously* says it happens in some places "
             "and not others without the rule undertaking to say "
             "which. The three rules before this one are the vṛtti's "
             "own unfolding of it, and even together they do not "
             "exhaust it"),
    Kala("4.3.38", case="saptamī",
         sense="kṛta-labdha-krīta-kuśala",
         why="कृतलब्धक्रीतकुशलाः, तत्रेत्येव. स्रुघ्ने कृतो वा लब्धो "
             "वा क्रीतो वा कुशलो वा **स्रौघ्नः**; माथुरः, राष्ट्रियः. "
             "Four senses in one rule, and one affix for all four.\n\n"
             "**AND THE GRAMMAR DISTINGUISHES WHAT THE WORLD DOES "
             "NOT.** ननु च यद् यत्र कृतं जातमपि तत् तत्र भवति, यच्च "
             "यत्र क्रीतं लब्धमपि तत् तत्रैव भवति, **किमर्थं "
             "भेदेनोपादानं क्रियते?** — whatever was made somewhere "
             "was also born there, and whatever was bought there was "
             "also got there, so why name them separately? "
             "**शब्दार्थस्य भिन्नत्वाद् वस्तुमात्रेण क्रीतं लब्धं "
             "भवति, शब्दार्थस्तु भिद्यत एव** — as a matter of FACT a "
             "thing bought is a thing got; the meanings of the WORDS "
             "are different all the same. The grammar is about what "
             "is said and not about what is the case"),
    Kala("4.3.39", case="saptamī", sense="prāya-bhava",
         why="प्रायभवः, तत्रेत्येव. **प्रायशब्दः साकल्यस्य "
             "किंचिन्न्यूनतामाह** — प्राय says *a little short of the "
             "whole*. स्रुघ्ने प्रायेण बाहुल्येन भवति स्रौघ्नः.\n\n"
             "**AND THE VṚTTI CALLS THE RULE POINTLESS.** "
             "**प्रायभवग्रहणमनर्थकम्, तत्रभवेन कृतार्थत्वात्** — "
             "naming *mostly-there* achieves nothing, because 4.3.53 "
             "तत्र भवः covers it already. अनित्यभवः प्रायभव इति "
             "चेद्, **मुक्तसंशयेन तुल्यम्**: and if you answer that "
             "प्रायभव means *not-always-there*, that comes to the "
             "same as the plain case with the doubt taken out. A "
             "commentary on a rule concluding that the rule was not "
             "needed, and codifying it anyway"),
    Kala("4.3.40", of=("upajānu", "upakarṇa", "upanīvi"), gives="ṭhak",
         case="saptamī", sense="prāya-bhava", excepts=("4.1.83",),
         why="उपजान्वुपकर्णोपनीवेष्ठक्, अणोऽपवादः. औपजानुकः, "
             "औपकर्णिकः, औपनीविकः — what is mostly about the knee, "
             "the ear, the waistband. Three अव्ययीभाव compounds, and "
             "the affix given to them as wholes"),
    Kala("4.3.41", case="saptamī", sense="saṃbhūta",
         why="संभूते, तत्रेत्येव. स्रुघ्ने संभवति स्रौघ्नः.\n\n"
             "**A SENSE NARROWED BY WHAT THE NEIGHBOURS ALREADY "
             "TOOK.** **अवक्ऌप्तिः प्रमाणानतिरेकश्च संभवत्यर्थ इह "
             "गृह्यते, नोत्पत्तिः सत्ता वा, जातभवाभ्यां गतत्वात्** — "
             "संभव here is *fitting in*, not exceeding the measure of "
             "the place; it is NOT arising and NOT being, because "
             "4.3.25 जात and 4.3.53 भव have those already. A word's "
             "range settled by subtracting its neighbours"),
    Kala("4.3.42", of=("kośa",), gives="ḍhañ", case="saptamī",
         sense="saṃbhūta", excepts=("4.1.83",),
         why="कोशाड्ढञ्, अणोऽपवादः. कोशे संभूतं **कौशेयं वस्त्रम्** — "
             "silk, what is produced in a cocoon.\n\n"
             "**रूढिरेषा, तेन क्रिमौ न भवति, खड्गकोशाच्च** — the word "
             "is CONVENTIONAL, fixed on the cloth; so it is not used "
             "of the worm that lives in the cocoon, nor of anything "
             "in a sword-sheath, though कोश names that too. Two "
             "exclusions, neither by a rule and both by usage"),
    Kala("4.3.43", of_samjna="kāla", case="saptamī",
         sense="sādhu-puṣpyat-pacyamāna",
         why="कालात् साधुपुष्प्यत्पच्यमानेषु. Three senses at once, "
             "and an example for each: हेमन्ते साधुर् **हैमनः "
             "प्राकारः**, a rampart that does well in winter; वसन्ते "
             "पुष्प्यन्ति **वासन्त्यः कुन्दलताः**, jasmine that "
             "flowers in spring; शरदि पच्यन्ते **शारदाः शालयः**, rice "
             "that ripens in autumn. शैशिरमनुलेपनम्, ग्रैष्म्यः "
             "पाटलाः, ग्रैष्मा यवाः.\n\n"
             "**AND काल IS NAMED A SECOND TIME.** The word headed "
             "4.3.11 to 4.3.24 and stopped; here it is spoken afresh "
             "in a sūtra of its own, and carries again as far as "
             "4.3.52, where the rule after records that it is over"),
    Kala("4.3.44", of_samjna="kāla", case="saptamī", sense="upta",
         why="उप्ते च, तत्रेत्येव कालादिति च. हेमन्त उप्यन्ते "
             "**हैमन्ता यवाः**; ग्रैष्मा व्रीहयः — barley sown in "
             "winter and rice sown in summer.\n\n"
             "**योगविभाग उत्तरार्थः** — and the rule is split off "
             "from the last only so that the next has something to be "
             "stated of. The third time in this pāda"),
    Kala("4.3.45", of=("āśvayujī",), gives="vuñ", case="saptamī",
         sense="upta", excepts=("4.3.11",),
         why="आश्वयुज्या वुञ्, ठञोऽपवादः. आश्वयुज्यामुप्ता "
             "**आश्वयुजका माषाः** — beans sown at the Āśvayujī full "
             "moon.\n\n"
             "**अश्विनीभ्यां युक्ता पौर्णमासी आश्वयुजी** — the full "
             "moon joined to the two Aśvinī stars; "
             "अश्विनीपर्यायोऽश्वयुक्शब्दः, अश्वयुज् being another "
             "name for that mansion. The base is itself a derived "
             "word, and the vṛtti derives it before using it"),
    Kala("4.3.46", of=("grīṣma", "vasanta"), gives="vuñ", case="saptamī",
         sense="upta", optional=True, excepts=("4.3.16",),
         why="ग्रीष्मवसन्तादन्यतरस्याम्, ऋत्वणोऽपवादः. ग्रैष्मकम् "
             "beside ग्रैष्मं सस्यम्; वासन्तकम् beside वासन्तम्"),
    Kala("4.3.47", of_samjna="kāla", case="saptamī", sense="deya-ṛṇa",
         why="देयमृणे, तत्रेत्येव कालादिति च. **यद् देयमृणं चेत् तद् "
             "भवति** — the affix comes only if what is to be given is "
             "a DEBT. मासे देयमृणं मासिकम्; आर्धमासिकम्, "
             "सांवत्सरिकम्. ऋण इति किम्? **मासे देया भिक्षा** — alms "
             "to be given monthly are not a debt, and take nothing",
         keeps_out="मासे देया भिक्षा"),
    Kala("4.3.48", of=("kalāpin", "aśvattha", "yavabusa"), gives="vun",
         case="saptamī", sense="deya-ṛṇa", excepts=("4.1.83",),
         why="कलाप्यश्वत्थयवबुसाद् वुन्, कालादित्येव. कलापकम्, "
             "अश्वत्थकम्, यवबुसकम्.\n\n"
             "**AND THREE SEASONS ARE NAMED BY WHAT HAPPENS IN THEM.** "
             "**कलाप्यादयः शब्दाः साहचर्यात् काले वर्तन्ते** — these "
             "words denote times by the COMPANY THEY KEEP, and the "
             "vṛtti unpacks each: यस्मिन् काले मयूराः कलापिनो भवन्ति "
             "स कलापी, the season when the peacocks have their "
             "tail-fans; यस्मिन्नश्वत्थाः फलन्ति सोऽश्वत्थः, when the "
             "fig trees bear; यस्मिन् यवबुसं संपद्यते स "
             "यवबुसशब्देनोच्यते, when the barley-chaff comes. 4.3.11 "
             "allowed a figurative time-word by गुणवृत्ति; this names "
             "the mechanism"),
    Kala("4.3.49", of=("grīṣma", "avarasama"), gives="vuñ",
         case="saptamī", sense="deya-ṛṇa", excepts=("4.3.16", "4.3.11"),
         why="ग्रीष्मावरसमाद् वुञ्, अण्ठञोरपवादः. ग्रीष्मे देयमृणं "
             "ग्रैष्मकम्; आवरसमकम्. **प्रत्ययान्तरकरणं वृद्ध्यर्थम्** "
             "— a different affix is given for the sake of the "
             "वृद्धि, which the affix already available would not "
             "have brought. समाशब्दो वर्षपर्यायः, समा being another "
             "word for a year"),
    Kala("4.3.50", of=("saṃvatsara", "āgrahāyaṇī"), gives="ṭhañ",
         also_gives=("vuñ",), case="saptamī", sense="deya-ṛṇa",
         why="संवत्सराग्रहायणीभ्यां ठञ् च. सांवत्सरिकम् and "
             "सांवत्सरकम्; आग्रहायणिकम् and आग्रहायणकम्.\n\n"
             "**वेति वक्तव्ये ठञ्ग्रहणम्** — why name ठञ् when वा "
             "would have said the same? Because संवत्सर is in "
             "4.3.16's गणसूत्र **संवत्सरात् फलपर्वणोः**, and where "
             "the फल is meant AS A DEBT the ठञ् has to beat that "
             "rule's अण्. An affix named rather than an option "
             "spoken, because the two do not have the same reach"),
    Kala("4.3.51", of_samjna="kāla", case="saptamī",
         sense="vyāharati-mṛgaḥ",
         why="व्याहरति मृगः, तत्रेत्येव कालादिति च. निशायां व्याहरति "
             "मृगो **नैशः**, नैशिकः; प्रादोषः, प्रादोषिकः. A whole "
             "rule for the time at which a deer calls.\n\n"
             "मृग इति किम्? **निशायां व्याहरत्युलूकः** — the owl "
             "calls at night too, and gets nothing",
         keeps_out="निशायां व्याहरत्युलूकः"),
    Kala("4.3.52", of_samjna="kāla", case="prathamā", sense="soḍha",
         why="तदस्य सोढम्, कालादित्येव. **सोढं जितमभ्यस्तमित्यर्थः** "
             "— borne, conquered, practised. निशासहचरितमध्ययनं निशा, "
             "तत् सोढमस्य छात्रस्य **नैशः**, नैशिकः: the study that "
             "goes with the night is called *the night*, and the "
             "student who has mastered it is नैश.\n\n"
             "The base stands in the NOMINATIVE here — तदिति "
             "प्रथमासमर्थात् — and the relation to the person is the "
             "genitive of अस्य. The first rule since 4.3.25 to change "
             "the case, and the next rule repeats तत्र in order to "
             "change it back"),
    Kala("4.3.53", case="saptamī", sense="bhava",
         why="तत्र भवः. स्रुघ्ने भवः स्रौघ्नः; माथुरः, राष्ट्रियः.\n\n"
             "**कालादिति निवृत्तम्** — and काल, which had been "
             "carrying since 4.3.43, is over. The second of its two "
             "ranges in this pāda, and this one is closed from "
             "outside by the rule that comes after it, where the "
             "first was bounded in advance by the rule that opened "
             "it.\n\n"
             "**सत्ता भवत्यर्थो गृह्यते न जन्म, तत्र जातः इति "
             "गतार्थत्वात्** — भव is BEING and not birth, because "
             "4.3.25 has birth already. The same subtraction 4.3.41 "
             "made, and made against the same two rules.\n\n"
             "**पुनस्तत्रग्रहणं तदस्येति निवृत्त्यर्थम्** — and तत्र "
             "is said AGAIN in order to cancel the last rule's "
             "तदस्य. A word repeated not to be carried but to push "
             "another word out"),
    Kala("4.3.54", gana="digādi", gives="yat", case="saptamī",
         sense="bhava", excepts=("4.1.83", "4.2.114"),
         why="दिगादिभ्यो यत्, **अणश्छस्य चापवादः**. दिशि भवं दिश्यम्; "
             "वर्ग्यम्.\n\n"
             "**मुखजघनशब्दयोरशरीरावयवार्थः पाठः** — मुख and जघन are "
             "in the list for the sense that is NOT a body-part, "
             "since the next rule covers body-parts anyway: "
             "सेनामुख्यम्, the van of an army, and सेनाजघन्यम्, its "
             "rear. Two entries read for what the neighbouring rule "
             "does not reach — the same shape as 4.2.127's"),
    Kala("4.3.55", of_samjna="śarīra-avayava", gives="yat",
         case="saptamī", sense="bhava", excepts=("4.1.83",),
         why="शरीरावयवाच्च, अणोऽपवादः. **शरीरं प्राणिकायः** — a body "
             "is a living thing's frame. दन्तेषु भवं **दन्त्यम्**; "
             "**कर्ण्यम्**; **ओष्ठ्यम्**.\n\n"
             "And those three words are the phonetic terms *dental*, "
             "*of the ear* and *labial*: the śikṣā texts name the "
             "places of articulation with affixes this rule gives"),
    Kala("4.3.56",
         of=("dṛti", "kukṣi", "kalaśi", "vasti", "asti", "ahi"),
         gives="ḍhañ", case="saptamī", sense="bhava",
         excepts=("4.3.55",),
         why="दृतिकुक्षिकलशिवस्त्यस्त्यहेर्ढञ्. दृतौ भवं दार्तेयम्; "
             "कौक्षेयम्, कालशेयम्, वास्तेयम्, आस्तेयम्; "
             "**आहेयमजरं विषम्**, the snake's venom that does not "
             "age.\n\n"
             "**अस्तिशब्दः प्रातिपदिकम्, न तिङन्तम्** — the अस्ति in "
             "the rule is a NOMINAL STEM and not the finite verb it "
             "is written exactly like. A warning the reader needs "
             "and could not have supplied"),
    Kala("4.3.57", of=("grīvā",), gives="aṇ", also_gives=("ḍhañ",),
         case="saptamī", sense="bhava", excepts=("4.3.55",),
         why="ग्रीवाभ्योऽण् च, **शरीरावयवाद् यतोऽपवादः**. ग्रीवासु "
             "भवं ग्रैवम्, ग्रैवेयम्.\n\n"
             "**ग्रीवाशब्दो धमनीवचनः, तासां बहुत्वाद् बहुवचनं "
             "कृतम्** — ग्रीवा names the ARTERIES of the neck, and "
             "they are many, which is why the sūtra puts the word in "
             "the plural. A grammatical number explained by anatomy"),
    Kala("4.3.58", of=("gambhīra",), gives="ñya", case="saptamī",
         sense="bhava", excepts=("4.1.83",),
         why="गम्भीराञ्ञ्यः, अणोऽपवादः. गम्भीरे भवं **गाम्भीर्यम्** — "
             "depth, and the word for the quality is made by asking "
             "what is IN the deep.\n\n"
             "**बहिर्देवपञ्चजनेभ्यश्चेति वक्तव्यम्** — a vārttika "
             "adds three: बाह्यम्, दैव्यम्, पाञ्चजन्यम्"),
    Kala("4.3.59", of_samjna="avyayībhāva", gana="parimukhādi",
         gives="ñya", case="saptamī", sense="bhava",
         excepts=("4.1.83",),
         why="अव्ययीभावाच्च, अणोऽपवादः. परिमुखं भवं **पारिमुख्यम्**; "
             "पारिहनव्यम्.\n\n"
             "**न च सर्वस्मादव्ययीभावाद् भवति; किं तर्हि? "
             "परिमुखादेः** — not from every अव्ययीभाव but from the "
             "परिमुखादि list; औपकूलम् is what stands otherwise. And "
             "**परिमुखादीनां च गणपाठस्यैतदेव प्रयोजनम्**: that list "
             "exists in the गणपाठ for this rule and for nothing "
             "else. **तेषां विशेषणमव्ययीभावग्रहणम्** — so the word "
             "अव्ययीभाव qualifies the LIST rather than being the "
             "ground the rule stands on",
         keeps_out="औपकूलम्"),
    Kala("4.3.60", pre="antar", of_samjna="avyayībhāva", gives="ṭhañ",
         case="saptamī", sense="bhava", excepts=("4.1.83",),
         why="अन्तःपूर्वपदाट् ठञ्, अणोऽपवादः. **अन्तःशब्दो "
             "विभक्त्यर्थे समस्यते** — अन्तर् compounds in the sense "
             "of a case-ending. आन्तर्वेश्मिकम्, आन्तर्गेहिकम्.\n\n"
             "**AND THIRTEEN VĀRTTIKAS RIDE WITH IT, GATHERED INTO "
             "TWO ŚLOKAS.** समानशब्दाट् ठञ् — सामानिकम्; तदादेश्च — "
             "सामानग्रामिकम्; **अध्यात्मादिभ्यश्च** — आध्यात्मिकम्, "
             "आधिदैविकम्, आधिभौतिकम्, the three classical sources of "
             "affliction, and अध्यात्मादिराकृतिगणः, an open list. "
             "ऊर्ध्वंदमाच्च and ऊर्ध्वदेहाच्च — और्ध्वदेहिकम्, the "
             "rites for the departed. लोकोत्तरपदाच्च — ऐहलौकिकम्, "
             "पारलौकिकम्, of this world and the next. "
             "मुखपार्श्वतसोरीयः, जनपरयोः कुक् च, मध्यशब्दादीयः, "
             "मण्मीयौ, **मध्यो मध्यं दिनण् चास्मात्** — माध्यन्दिनम्, "
             "which is the name of a Yajurveda recension; स्थाम्नो "
             "लुक् — **अश्वत्थामा**; अजिनान्ताच्च — वृकाजिनः.\n\n"
             "Four of these were read at 4.2.138 as गणसूत्र of the "
             "गहादि list, and are read again here. The same "
             "supplement stated at two rules, because two rules give "
             "affixes the words could take"),
    Kala("4.3.61", pre="pari-anu", stem_final="grāma",
         of_samjna="avyayībhāva", gives="ṭhañ", case="saptamī",
         sense="bhava", excepts=("4.1.83",),
         why="ग्रामात् पर्यनुपूर्वात्, अव्ययीभावादित्येव; अणोऽपवादः. "
             "पारिग्रामिकः, आनुग्रामिकः — what is in the country "
             "round the village, and what is in the country along it"),
    Kala("4.3.62", of=("jihvāmūla", "aṅguli"), gives="cha",
         case="saptamī", sense="bhava", excepts=("4.3.55",),
         why="जिह्वामूलाङ्गुलेश्छः, **यतोऽपवादः** — it beats 4.3.55's "
             "यत्, which would have reached both words as parts of "
             "the body. जिह्वामूलीयम्, अङ्गुलीयम्; and the first of "
             "those is the phoneticians' name for the जिह्वामूलीय "
             "sound, made at the root of the tongue"),
    Kala("4.3.63", stem_final="varga", gives="cha", case="saptamī",
         sense="bhava", excepts=("4.1.83",),
         why="वर्गान्ताच्च, अणोऽपवादः. कवर्गीयम्, चवर्गीयम् — and "
             "these are the standard names for the rows of the "
             "alphabet, made by asking what is IN the row"),
    Kala("4.3.64", stem_final="varga", gives="yat", also_gives=("kha",),
         optional=True, result="aśabda", case="saptamī", sense="bhava",
         excepts=("4.3.63",),
         why="अशब्दे यत्खावन्यतरस्याम्, वर्गान्तादित्येव. "
             "**छे प्राप्ते वचनं पक्षे सोऽपि भवति** — the last rule "
             "had the ground, so on the other side of the option its "
             "छ comes back and there are three forms: वासुदेववर्ग्यः, "
             "वासुदेववर्गीणः, वासुदेववर्गीयः; युधिष्ठिरवर्ग्यः, "
             "युधिष्ठिरवर्गीणः, युधिष्ठिरवर्गीयः.\n\n"
             "अशब्द इति किम्? **कवर्गीयो वर्णः** — where the वर्ग is "
             "a row of SOUNDS the option does not apply and only छ "
             "stands. The grammar reserves one form for talking about "
             "itself",
         keeps_out="कवर्गीयो वर्णः"),
    Kala("4.3.65", of=("karṇa", "lalāṭa"), gives="kan", result="alaṃkāra",
         case="saptamī", sense="bhava", excepts=("4.3.55",),
         why="कर्णललाटात् कनलंकारे, यतोऽपवादः. **कर्णिका**, "
             "**ललाटिका** — the ear-ornament and the forehead-"
             "ornament. अलंकार इति किम्? कर्ण्यम्, ललाट्यम्, which "
             "are what 4.3.55 gives for anything else in an ear",
         keeps_out="कर्ण्यम्, ललाट्यम्"),
    Kala("4.3.66", of_samjna="vyākhyātavya-nāman", case="ṣaṣṭhī",
         sense="vyākhyāna",
         why="तस्य व्याख्यान इति च व्याख्यातव्यनाम्नः. "
             "**व्याख्यायतेऽनेनेति व्याख्यानम्** — an EXPOSITION is "
             "what a thing is expounded by; व्याख्यातव्यस्य नाम "
             "व्याख्यातव्यनाम, the name of the thing to be expounded. "
             "सुपां व्याख्यानः **सौपो ग्रन्थः**, the book that "
             "expounds the nominal endings; तैङः, कार्तः.\n\n"
             "व्याख्यातव्यनाम्न इति किम्? पाटलिपुत्रस्य व्याख्यानी "
             "सुकोसला — Sukosalā expounds Pāṭaliputra, telling how "
             "the city is laid out, **न तु पाटलिपुत्रं "
             "व्याख्यातव्यनाम**: a city is not the NAME of something "
             "to be expounded, and gets nothing",
         keeps_out="पाटलिपुत्रस्य व्याख्यानी सुकोसला"),
    Kala("4.3.66", of_samjna="vyākhyātavya-nāman", case="saptamī",
         sense="bhava",
         why="तस्य व्याख्यान इति **च** व्याख्यातव्यनाम्नः, the half "
             "the conjunction brings. सुप्सु भवं सौपम्; तैङम्, "
             "कार्तम्.\n\n"
             "**AND A च THAT GATHERS THE PREVIOUS SENTENCE'S "
             "MEANING.** वाक्यार्थसमीपे चकारः श्रूयमाणः "
             "**पूर्ववाक्यार्थमेव समुच्चिनोति** — heard beside the "
             "meaning of a sentence, the च joins the meaning of the "
             "sentence BEFORE, which is 4.3.53 तत्र भवः. So both "
             "senses govern from here.\n\n"
             "**भवव्याख्यानयोर्युगपदधिकारोऽपवादविधानार्थः, "
             "कृतनिर्देशौ हि तौ** — the two headings are made to run "
             "SIMULTANEOUSLY so that the seven exceptions after them "
             "can be stated once for both instead of twice"),
    Kala("4.3.67", of_samjna="vyākhyātavya-nāman", vowels="bahvac",
         accent="antodātta", gives="ṭhañ", sense="vyākhyāna",
         also_sense="bhava", excepts=("4.1.83",),
         why="बह्वचोऽन्तोदात्ताट् ठञ्, अणोऽपवादः. षात्वणत्विकम्, "
             "नातानतिकम् — books on ष-substitution and ण-substitution, "
             "and on न-forms; **समासस्वरेणान्तोदात्ताः प्रकृतयः**, "
             "the bases carry the final accent by the compound-accent "
             "rule.\n\n"
             "बह्वच इति किम्? **द्व्यचष्ठकं वक्ष्यति** — 4.3.72 will "
             "give ठक् for a two-vowel base, and एकाच् is what the "
             "counter-examples show: सौपम्, तैङम्, कार्तम्. "
             "अन्तोदात्तादिति किम्? **संहितायाः सांहितम्**, where "
             "संहिताशब्दो हि गतिस्वरेणाद्युदात्तः — the accent falls "
             "at the front, placed by a rule about preverbs",
         keeps_out="सौपम्, सांहितम्"),
    Kala("4.3.68", of_samjna="kratu", gives="ṭhañ", sense="vyākhyāna",
         also_sense="bhava", excepts=("4.1.83",),
         why="क्रतुयज्ञेभ्यश्च, the क्रतु half; अणोऽपवादः. "
             "अग्निष्टोमस्य व्याख्यानस्तत्र भवो वा **आग्निष्टोमिकः**; "
             "वाजपेयिकः, राजसूयिकः. **अनन्तोदात्तार्थ आरम्भः** — the "
             "rule is begun for the bases whose accent is NOT final, "
             "which the last rule could not reach"),
    Kala("4.3.68", of_samjna="yajña", gives="ṭhañ", sense="vyākhyāna",
         also_sense="bhava", excepts=("4.1.83",),
         why="क्रतुयज्ञेभ्यश्च, the यज्ञ half. पाकयज्ञिकः, "
             "नावयज्ञिकः.\n\n"
             "**क्रतुभ्य इत्येव सिद्धे यज्ञग्रहणमसोमयागेभ्योऽपि यथा "
             "स्यात्** — क्रतु alone would have done for the soma "
             "sacrifices; *sacrifice* is named as well so that the "
             "rites which are NOT soma-offerings come in too. "
             "पाञ्चौदनिकः, दाशौदनिकः. **बहुवचनं "
             "स्वरूपविधिनिरासार्थम्**: the plural is there so the "
             "rule is not read as being about the words themselves"),
    Kala("4.3.69", of_samjna="ṛṣi", gives="ṭhañ", result="adhyāya",
         sense="vyākhyāna", also_sense="bhava", excepts=("4.1.83",),
         why="अध्यायेष्वेवर्षेः, अणोऽपवादः. वसिष्ठस्य व्याख्यानस्तत्र "
             "भवो वा **वासिष्ठिकोऽध्यायः**; वैश्वामित्रिकः.\n\n"
             "**ऋषिशब्दाः प्रवरनामधेयानि** — the seer-words here are "
             "the names invoked in the प्रवर. And "
             "**व्याख्यातव्यनाम्न इत्यनुवर्तते, तत्साहचर्याद् "
             "ऋषिशब्दैर्ग्रन्थ उच्यते**: because *the name of what is "
             "to be expounded* carries over, a seer's name here means "
             "his BOOK. अध्यायेष्विति किम्? **वासिष्ठी ऋक्** — a "
             "single verse is not a lesson",
         keeps_out="वासिष्ठी ऋक्"),
    Kala("4.3.70", of=("pauroḍāśa", "puroḍāśa"), gives="ṣṭhan",
         sense="vyākhyāna", also_sense="bhava", excepts=("4.1.83",),
         why="पौरोडाशपुरोडाशात् ष्ठन्. **पुरोडाशाः पिष्टपिण्डाः**, "
             "the flour-cakes; तेषां संस्कारको मन्त्रः पौरोडाशः, the "
             "verse that consecrates them — and the book on THAT is "
             "पौरोडाशिकः, पौरोडाशिकी. From the cakes' own word, "
             "पुरोडाशिकः, पुरोडाशिकी. **षकारो ङीषर्थः**, the ष् is "
             "there for the feminine, as at 4.2.99"),
    Kala("4.3.71", of=("chandas",), gives="yat", also_gives=("aṇ",),
         sense="vyākhyāna", also_sense="bhava", excepts=("4.3.72",),
         why="छन्दसो यदणौ. **द्व्यच इति ठकि प्राप्ते वचनम्** — छन्दस् "
             "has two vowels, so 4.3.72 would have given ठक्; these "
             "two are spoken against it. छन्दस्यः (तैत्तिरीयसंहिता "
             "१.६.११.४), छान्दसः (कौषीतकिगृह्य १४१.३४) — and both "
             "forms are cited from texts rather than constructed"),
    Kala("4.3.72", vowels="dvyac", of_samjna="vyākhyātavya-nāman",
         gives="ṭhak", sense="vyākhyāna", also_sense="bhava",
         excepts=("4.1.83", "4.3.67"),
         why="द्व्यजृद्ब्राह्मणर्क्प्रथमाध्वरपुरश्चरणनामाख्याताट् ठक्, "
             "the द्व्यच् member; अणादेरपवादः. ऐष्टिकः, पाशुकः — "
             "books on the इष्टि and on the animal offering"),
    Kala("4.3.72", stem_final="ṛ", of_samjna="vyākhyātavya-nāman",
         gives="ṭhak", sense="vyākhyāna", also_sense="bhava",
         excepts=("4.1.83",),
         why="द्व्यजृद्..., the ऋदन्त member. चातुर्होतृकः, "
             "पाञ्चहोतृकः — the books of the four priests and of the "
             "five"),
    Kala("4.3.72",
         of=("brāhmaṇa", "ṛc", "prathama", "adhvara", "puraścaraṇa",
             "nāman", "ākhyāta"),
         gives="ṭhak", sense="vyākhyāna", also_sense="bhava",
         excepts=("4.1.83",),
         why="द्व्यजृद्..., the seven named words. ब्राह्मणिकः, "
             "आर्चिकः, प्राथमिकः, आध्वरिकः, पौरश्चरणिकः.\n\n"
             "**नामाख्यातग्रहणं संघातविगृहीतार्थम्** — *noun* and "
             "*verb* are named so that the rule reaches them "
             "separately AND as a compound: नामिकः, आख्यातिकः, and "
             "**नामाख्यातिकः**. A book on nouns, a book on verbs, and "
             "a book on both"),
    Kala("4.3.73", gana="ṛgayanādi", gives="aṇ", sense="vyākhyāna",
         also_sense="bhava", excepts=("4.3.67", "4.3.72"),
         why="अणृगयनादिभ्यः, ठञादेरपवादः. आर्गयनः, पादव्याख्यानः. "
             "**अण्ग्रहणं बाधकबाधनार्थम्** — the default named to "
             "beat its beater, the fourth time in three pādas; "
             "वास्तुविद्यः is what it saves.\n\n"
             "And the list is a catalogue of the sciences: "
             "ऋगयन, पदव्याख्यान, छन्दोमान, छन्दोभाषा, छन्दोविचिति, "
             "न्याय, पुनरुक्त, **निरुक्त**, **व्याकरण**, निगम, "
             "वास्तुविद्या, अङ्गविद्या, क्षत्रविद्या, उत्पात, उत्पाद, "
             "संवत्सर, मुहूर्त, निमित्त, **उपनिषद्**, **शिक्षा** — "
             "and grammar itself is the ninth entry"),
    Kala("4.3.74", case="pañcamī", sense="āgata",
         why="तत आगतः. स्रुघ्नादागतः स्रौघ्नः; माथुरः, राष्ट्रियः. "
             "The case changes to the ablative and the affix stays "
             "यथाविहितम्.\n\n"
             "**तत इति मुख्यमपादानं विवक्षितं यत् तदिह गृह्यते, न "
             "नान्तरीयकम्** — the ablative meant is the PRINCIPAL "
             "point of departure and not one that merely came along "
             "with it. स्रुघ्नादागच्छन् वृक्षमूलादागत इति: a man "
             "coming from Srughna also comes from the foot of some "
             "tree, and no affix follows from the tree",
         keeps_out="वृक्षमूलादागतः"),
    Kala("4.3.75", of_samjna="āyasthāna", gives="ṭhak", case="pañcamī",
         sense="āgata", excepts=("4.1.83",),
         why="ठगायस्थानेभ्यः, अणोऽपवादः; **छं तु परत्वाद् बाधते**, "
             "and 4.2.114's छ beats it by standing later. "
             "**आय इति स्वामिग्राह्यो भाग उच्यते, स "
             "यस्मिन्नुत्पद्यते तदायस्थानम्** — आय is the share the "
             "owner takes, and a place where it arises is an "
             "आयस्थान: a revenue-office. शुल्कशालाया आगतः "
             "**शौल्कशालिकः**, from the customs-house; आकरिकम्, from "
             "the mine. **बहुवचनं स्वरूपविधिनिरासार्थम्**"),
    Kala("4.3.76", gana="śuṇḍikādi", gives="aṇ", case="pañcamī",
         sense="āgata", excepts=("4.3.75",),
         why="शुण्डिकादिभ्योऽण्, **आयस्थानठकोऽपवादः**. शुण्डिकादागतः "
             "शौण्डिकः; कार्कणः. **अण्ग्रहणं बाधकबाधनार्थम्** — the "
             "default named to beat its beater again, three sūtras "
             "after the last time; औदपानः is what it saves"),
    Kala("4.3.77", of_samjna="vidyā-yoni-saṃbandha", gives="vuñ",
         case="pañcamī", sense="āgata", excepts=("4.1.83",),
         why="विद्यायोनिसंबन्धेभ्यो वुञ्, अणोऽपवादः; छं तु परत्वाद् "
             "बाधते. **विद्यायोनिकृतः संबन्धो येषां ते "
             "विद्यायोनिसंबन्धाः** — those whose connection is made "
             "either by LEARNING or by BIRTH. उपाध्यायादागतम् "
             "**औपाध्यायकम्**, शैष्यकम्, आचार्यकम् — from the "
             "teacher, the pupil, the preceptor; and मातामहकः, "
             "पैतामहकः, मातुलकः — from the mother's father, the "
             "father's father, the mother's brother. One rule for the "
             "two kinds of kinship a person can have"),
    Kala("4.3.78", of_samjna="vidyā-yoni-saṃbandha", stem_final="ṛ",
         gives="ṭhañ", case="pañcamī", sense="āgata",
         excepts=("4.3.77",),
         why="ऋतष्ठञ्, विद्यायोनिसंबन्धेभ्य इत्येव; वुञोऽपवादः. "
             "होतुरागतं **हौतृकम्**, पौतृकम्; भ्रातृकम्, स्वासृकम्, "
             "मातृकम्. **तपरकरणं मुखसुखार्थम्** — the त appended to "
             "the ऋ is there for ease of pronunciation and takes "
             "nothing out. विद्यायोनिभ्यामन्यत्र **सावित्रम्**",
         keeps_out="सावित्रम्"),
    Kala("4.3.79", of=("pitṛ",), gives="yat", also_gives=("ṭhañ",),
         case="pañcamī", sense="āgata", excepts=("4.3.78",),
         why="पितुर्यच्च. पितुरागतं **पित्र्यम्** by the यत्, and "
             "**पैतृकम्** by the च, which brings the ठञ् of the last "
             "rule along. One word taking two affixes where the "
             "general rule for its class gave one"),
    Kala("4.3.80", of_samjna="gotra-pratyayānta", case="pañcamī",
         sense="āgata", borrows_from="4.3.127",
         borrow_query=(("samjna", "gotra-caraṇa"),
                       ("sense", "idam"), ("case", "ṣaṣṭhī")),
         why="गोत्रादङ्कवत्. **अपत्याधिकारादन्यत्र लौकिकं गोत्रम् "
             "अपत्यमात्रं गृह्यते** — outside the descendant section "
             "गोत्र has its everyday sense, any offspring at all; the "
             "same reading 4.2.39 took.\n\n"
             "**AN अतिदेश REACHING NINETY-SEVEN SŪTRAS FORWARD.** "
             "अङ्कग्रहणेन **तस्येदमर्थसामान्यं लक्ष्यते** — the word "
             "*brand* stands for the general sense *this belongs to "
             "that*, so **तस्माद् वुञप्यतिदिश्यते नाणेव**: the वुञ् "
             "is borrowed too and not only the अण् of 4.3.127 "
             "सङ्घाङ्कलक्षणेष्वञ्यञिञामण्. औपगवानामङ्कः औपगवकः, and "
             "so औपगवेभ्य आगतम् औपगवकम्; कापटवकम्, नाडायनकम्, "
             "चारायणकम्.\n\n"
             "**AND WHAT COMES BACK IS NOT THE AFFIX THE RULE "
             "NAMES.** 4.3.127 gives अण् from a base ending in अञ्, "
             "यञ् or इञ्, and औपगव ends in none of those — it ends in "
             "अण् itself. So the rule that actually answers is "
             "4.3.126 गोत्रचरणाद् वुञ्, which is precisely why the "
             "vṛtti has to say **तस्माद् वुञप्यतिदिश्यते नाणेव**.\n\n"
             "While 4.3.127 stood uncodified this row could only name "
             "it, and a test held the shortfall open by asserting that "
             "rule was absent. It is present now, and the borrowing "
             "runs"),
    Kala("4.3.81", of_samjna="hetu-manuṣya", gives="rūpya",
         optional=True, case="pañcamī", sense="āgata",
         why="हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः. **हेतुः कारणम्**; "
             "समादागतं समरूप्यम् beside समीयम्, विषमरूप्यम् beside "
             "विषमीयम् — and the second form of each is 4.2.138's छ, "
             "**गहादित्वात्**. From men: देवदत्तरूप्यम्, "
             "यज्ञदत्तरूप्यम्, beside दैवदत्तम्, याज्ञदत्तम्.\n\n"
             "**मनुष्यग्रहणमहेत्वर्थम्** — *man* is named for the "
             "case where the man is not the CAUSE of the coming"),
    Kala("4.3.82", of_samjna="hetu-manuṣya", gives="mayaṭ",
         case="pañcamī", sense="āgata",
         why="मयट् च. सममयम्, विषममयम्; देवदत्तमयम्, यज्ञदत्तमयम्. "
             "**टकारो ङीबर्थः** — the ट् is for the feminine, सममयी. "
             "\n\n"
             "**योगविभागो यथासंख्यनिरासार्थः** — and the rule is "
             "split off from the last in order to STOP a "
             "correspondence: read as one rule, two affixes against "
             "two grounds would have paired in order, and neither "
             "affix would have reached both. The fifth योगविभाग of "
             "this pāda, and the second of them made for this reason"),
    Kala("4.3.83", case="pañcamī", sense="prabhavati",
         why="प्रभवति, तत इत्येव. **प्रभवति प्रकाशते, प्रथमत "
             "उपलभ्यत इत्यर्थः** — rises, shows itself, is first "
             "found. हिमवतः प्रभवति **हैमवती गङ्गा**, the Ganges that "
             "rises from the Himālaya; **दारदी सिन्धुः**, the Indus "
             "from Darada"),
    Kala("4.3.84", of=("vidūra",), gives="ñya", case="pañcamī",
         sense="prabhavati", excepts=("4.1.83",),
         why="विदूराञ्ञ्यः, अणोऽपवादः. विदूरात् प्रभवति **वैदूर्यो "
             "मणिः** — the beryl.\n\n"
             "**AND AN OBJECTION ANSWERED WITH A KĀRIKĀ.** ननु च "
             "वालवायादसौ प्रभवति, न विदूरात्, तत्र तु संस्क्रियते? — "
             "the stone comes from Bālavāya and is only CUT at "
             "Vidūra. एवं तर्हि: **वालवायो विदूरं च प्रकृत्यन्तरमेव "
             "वा / न वै तत्रेति चेद् ब्रूयाज्जित्वरीवदुपाचरेत्** — "
             "either Bālavāya and Vidūra are two different bases, or, "
             "if someone insists the stone is not from there, let him "
             "treat the word as he treats जित्वरी. A verse offering a "
             "choice of two ways out and recommending neither"),
    Kala("4.3.85", case="dvitīyā", sense="gacchati", result="pathi-dūta",
         why="तद् गच्छति पथिदूतयोः. स्रुघ्नं गच्छति **स्रौघ्नः पन्था "
             "दूतो वा**; माथुरः. The base stands in the ACCUSATIVE "
             "here — तदिति द्वितीयासमर्थात् — the fourth case this "
             "pāda has used.\n\n"
             "**तत्स्थेषु गच्छत्सु पन्था गच्छतीत्युच्यते** — a road "
             "is said to *go* because what is on it goes; अथ वा "
             "**स्रुघ्नप्राप्तिः पथो गमनम्**, or else a road's going "
             "just is its reaching Srughna. Two readings of a "
             "metaphor, and the rule works on either.\n\n"
             "पथिदूतयोरिति किम्? **स्रुघ्नं गच्छति सार्थः** — a "
             "caravan really does go, and gets nothing",
         keeps_out="स्रुघ्नं गच्छति सार्थः"),
    Kala("4.3.86", case="dvitīyā", sense="abhiniṣkrāmati",
         result="dvāra",
         why="अभिनिष्क्रामति द्वारम्, तदित्येव. **आभिमुख्येन "
             "निष्क्रामति** — goes out FACING it. स्रुघ्नमभिनिष्क्रामति "
             "कान्यकुब्जद्वारं **स्रौघ्नम्**, the gate of Kanyakubja "
             "that opens toward Srughna; माथुरम्, राष्ट्रियम्.\n\n"
             "**द्वारमभिनिष्क्रमणक्रियायां करणं प्रसिद्धम्, तदिह "
             "स्वातन्त्र्येण विवक्ष्यते** — a gate is ordinarily the "
             "INSTRUMENT of going out, and here it is spoken of as "
             "the agent, **तथा साध्वसिश्छिनत्ति** — as one says *the "
             "good sword cuts*. द्वारमिति किम्? "
             "स्रुघ्नमभिनिष्क्रामति पुरुषः",
         keeps_out="स्रुघ्नमभिनिष्क्रामति पुरुषः"),
    Kala("4.3.87", case="dvitīyā", sense="adhikṛtya-kṛta",
         result="grantha",
         why="अधिकृत्य कृते ग्रन्थे, तदित्येव. **अधिकृत्य, प्रस्तुत्य, "
             "आगूर्येत्यर्थः** — taking as its subject, introducing, "
             "undertaking. सुभद्रामधिकृत्य कृतो ग्रन्थः **सौभद्रः**; "
             "गैरिमित्रः, यायातः. ग्रन्थ इति किम्? "
             "सुभद्रामधिकृत्य कृतः प्रासादः — a palace built in her "
             "honour is not a book.\n\n"
             "**लुबाख्यायिकाभ्यः प्रत्ययस्य बहुलम्** — and for the "
             "romances the affix is VARIOUSLY dropped, so the title "
             "is the heroine's own name: **वासवदत्ता**, सुमनोत्तरा, "
             "**उर्वशी**. न च भवति — भैमरथी, where it stands",
         keeps_out="सुभद्रामधिकृत्य कृतः प्रासादः"),
    Kala("4.3.88", gana="śiśukrandādi", gives="cha", case="dvitīyā",
         sense="adhikṛtya-kṛta", result="grantha", excepts=("4.1.83",),
         why="शिशुक्रन्दयमसभद्वन्द्वेन्द्रजननादिभ्यश्छः, अणोऽपवादः. "
             "शिशूनां क्रन्दनं शिशुक्रन्दः, तमधिकृत्य कृतो ग्रन्थः "
             "**शिशुक्रन्दीयः**; यमसभीयः. From a द्वन्द्व — "
             "अग्निकाश्यपीयः, श्येनकपोतीयः, **शब्दार्थसंबन्धीयं "
             "प्रकरणम्**, and **वाक्यपदीयम्**, which is Bhartṛhari's "
             "book made by this rule. इन्द्रजननीयम्, "
             "प्रद्युम्नागमनीयम्.\n\n"
             "**इन्द्रजननादिराकृतिगणः प्रयोगतोऽनुसर्तव्यः, "
             "प्रातिपदिकेषु न पठ्यते** — that list is open and is to "
             "be followed FROM USAGE; it is not written out in the "
             "गणपाठ at all. And a vārttika refuses one kind: "
             "**द्वन्द्वे देवासुरादिभ्यः प्रतिषेधः** — दैवासुरम्, "
             "राक्षोऽसुरम्, गौणमुख्यम्",
         keeps_out="दैवासुरम्"),
    Kala("4.3.89", case="prathamā", sense="nivāsa",
         why="सोऽस्य निवासः. **निवसन्त्यस्मिन्निवासो देश उच्यते** — a "
             "निवास is the place people live in. स्रुघ्नो निवासोऽस्य "
             "**स्रौघ्नः**; माथुरः, राष्ट्रियः. The base is "
             "प्रथमासमर्थ and the relation is the genitive of अस्य, "
             "the same shape as 4.3.52's"),
    Kala("4.3.90", case="prathamā", sense="abhijana",
         why="अभिजनश्च, सोऽस्येत्येव. **अभिजनः पूर्वबान्धवः** — the "
             "forebears; तत्संबन्धाद् देशोऽप्यभिजन इत्युच्यते, "
             "**यस्मिन् पूर्वबान्धवैरुषितम्**, the place they lived "
             "in. तस्माद् इह देशवाचिनः प्रत्ययः, न बन्धुभ्यः, "
             "**निवासप्रत्यासत्तेः** — so the affix comes from the "
             "PLACE-word and not from the kinsmen, because the last "
             "rule was about a place and this one stands next to it. "
             "स्रुघ्नोऽभिजनोऽस्य स्रौघ्नः.\n\n"
             "**निवासाभिजनयोः को विशेषः? यत्र संप्रत्युष्यते स "
             "निवासः, यत्र पूर्वैरुषितं सोऽभिजनः** — where one lives "
             "NOW and where one's forebears lived. Two rules, "
             "identical outputs, and the difference is entirely in "
             "which fact about a person is being reported.\n\n"
             "**योगविभाग उत्तरार्थः**, and the split is for the sake "
             "of what follows"),
    Kala("4.3.91", of_samjna="parvata", result="āyudhajīvin",
         gives="cha", case="prathamā", sense="abhijana",
         why="आयुधजीविभ्यश्छः पर्वते, सोऽस्याभिजन इति वर्तते. "
             "**आयुधजीविभ्य इति तादर्थ्ये चतुर्थी, पर्वत इति "
             "प्रकृतिविशेषणम्** — the dative is *for the sake of*, so "
             "the WEAPON-BEARERS are what the word is to denote, and "
             "*mountain* qualifies the base instead. हृद्गोलः पर्वतो "
             "ऽभिजन एषामायुधजीविनां **हृद्गोलीयाः**; अन्धकवर्तीयाः, "
             "रोहितगिरीयाः.\n\n"
             "Two counter-examples, one for each condition. "
             "आयुधजीविभ्य इति किम्? **आर्क्षोदा ब्राह्मणाः**, "
             "brahmins and not soldiers. पर्वत इति किम्? "
             "**सांकाश्यका आयुधजीविनः**, soldiers whose ancestral "
             "place is not a mountain",
         keeps_out="आर्क्षोदा ब्राह्मणाः, सांकाश्यका आयुधजीविनः"),
    Kala("4.3.92", gana="śaṇḍikādi", gives="ñya", case="prathamā",
         sense="abhijana", excepts=("4.1.83",),
         why="शण्डिकादिभ्यो ञ्यः, अणादेरपवादः. शाण्डिक्यः, "
             "सार्वसेन्यः"),
    Kala("4.3.93", gana="sindhvādi", gives="aṇ", case="prathamā",
         sense="abhijana", excepts=("4.2.134",),
         why="सिन्धुतक्षशिलादिभ्योऽणञौ, the सिन्ध्वादि half; "
             "यथासंख्यम्. **आदिशब्दः प्रत्येकमभिसंबध्यते** — "
             "*and-the-rest* attaches to each of the two lists "
             "separately. सैन्धवः, वार्णवः.\n\n"
             "**ये तु कच्छादिषु पठ्यन्ते सिन्धुवर्णुप्रभृतयः, "
             "तेभ्यस्तत एवाणि सिद्धे मनुष्यवुञो बाधनार्थं वचनम्** — "
             "the first few of this list are in 4.2.133's कच्छादि "
             "already, so the अण् was coming from there; the rule is "
             "spoken to keep 4.2.134's वुञ् out"),
    Kala("4.3.93", gana="takṣaśilādi", gives="añ", case="prathamā",
         sense="abhijana", excepts=("4.1.83",),
         why="सिन्धुतक्षशिलादिभ्योऽणञौ, the तक्षशिलादि half. "
             "ताक्षशिलः, वात्सोद्धरणः — and Takṣaśilā heads a list "
             "of fourteen places"),
    Kala("4.3.94", of=("tūdī",), gives="ḍhak", case="prathamā",
         sense="abhijana", excepts=("4.1.83",),
         why="तूदीशलातुरवर्मतीकूचवाराड्ढक्छण्ढञ्यकः, यथासंख्यम्; "
             "अणोऽपवादः. तूदी takes ढक्: **तौदेयः**.\n\n"
             "Four bases and four affixes matched in order — the "
             "tightest correspondence in this pāda, where 4.3.1's "
             "two against three could not run at all and 4.3.33's "
             "two against two barely had to"),
    Kala("4.3.94", of=("śalātura",), gives="chaṇ", case="prathamā",
         sense="abhijana", excepts=("4.1.83",),
         why="तूदीशलातुर..., the second of the four. **शालातुरीयः** — "
             "*of Śalātura*, which is the word by which Pāṇini is "
             "known, and it is made by his own rule"),
    Kala("4.3.94", of=("varmatī",), gives="ḍhañ", case="prathamā",
         sense="abhijana", excepts=("4.1.83",),
         why="तूदीशलातुर..., the third of the four. **वार्मतेयः**"),
    Kala("4.3.94", of=("kūcavāra",), gives="yak", case="prathamā",
         sense="abhijana", excepts=("4.1.83",),
         why="तूदीशलातुर..., the fourth of the four. **कौचवार्यः**"),
    Kala("4.3.95", case="prathamā", sense="bhakti",
         why="भक्तिः. **समर्थविभक्तिः प्रत्ययार्थश्चानुवर्तते; "
             "अभिजन इति निवृत्तम्** — the case and the relation carry "
             "over from 4.3.89 and the ancestral home lapses. "
             "**भज्यते सेव्यत इति भक्तिः** — devotion is what one is "
             "devoted to. स्रुघ्नो भक्तिरस्य स्रौघ्नः; माथुरः, "
             "राष्ट्रियः.\n\n"
             "A one-word sūtra, and everything else in it is carried"),
    Kala("4.3.96", of_samjna="acitta", gives="ṭhak", case="prathamā",
         sense="bhakti", excepts=("4.1.83", "4.2.114"),
         why="अचित्तादेशकालाट् ठक्, अणोऽपवादः; **वृद्धाच् छं परत्वाद् "
             "बाधते**. अपूपो भक्तिरस्य **आपूपिकः**, the man who is "
             "devoted to cakes; शाष्कुलिकः, पायसिकः.\n\n"
             "Three conditions and a counter-example for each. "
             "अचित्तादिति किम्? दैवदत्तः — Devadatta is a person and "
             "not an unthinking thing. अदेशादिति किम्? स्रौघ्नः. "
             "अकालादिति किम्? ग्रैष्मः. The rule takes what is "
             "neither sentient, nor a place, nor a time",
         keeps_out="दैवदत्तः, स्रौघ्नः, ग्रैष्मः"),
    Kala("4.3.97", of=("mahārāja",), gives="ṭhañ", case="prathamā",
         sense="bhakti", excepts=("4.1.83",),
         why="महाराजाट् ठञ्, अणोऽपवादः. महाराजो भक्तिरस्य "
             "**माहाराजिकः**. **प्रत्ययान्तरकरणं स्वरार्थम्** — a "
             "different affix is given for the sake of the accent, "
             "the same reason 4.3.49 gave one"),
    Kala("4.3.98", of=("vāsudeva", "arjuna"), gives="vun",
         case="prathamā", sense="bhakti", excepts=("4.3.99",),
         why="वासुदेवार्जुनाभ्यां वुन्, छाणोरपवादः. वासुदेवो "
             "भक्तिरस्य **वासुदेवकः**; अर्जुनकः.\n\n"
             "**AND A PRINCIPLE TAUGHT BY THE ORDER OF TWO WORDS.** "
             "ननु च वासुदेवशब्दाद् गोत्रक्षत्रियाख्येभ्यः इति वुञस् "
             "त्येव, न चात्र वुन्वुञोर्विशेषो विद्यते, किमर्थं "
             "वासुदेवग्रहणम्? — the next rule gives वुञ् from a "
             "kṣatriya name and there is no difference between वुन् "
             "and वुञ् here, so why name Vāsudeva at all? "
             "**संज्ञैषा देवताविशेषस्य न क्षत्रियाख्या**: it is the "
             "name of a GOD and not of a kṣatriya.\n\n"
             "And then the order. **अल्पाच्तरम्** [2.2.34] and "
             "**अजाद्यदन्तम्** [2.2.33] should both have put अर्जुन "
             "first in the compound. Not doing so **ज्ञापयति — "
             "अभ्यर्हितं पूर्वं निपततीति**: the more venerated goes "
             "first. A general principle of compounding taught by a "
             "rule declining to obey two others"),
    Kala("4.3.99", of_samjna="gotra-kṣatriya-ākhyā", gives="vuñ",
         bahulam=True, case="prathamā", sense="bhakti",
         excepts=("4.1.83", "4.2.114"),
         why="गोत्रक्षत्रियाख्येभ्यो बहुलं वुञ्, अणोऽपवादः; वृद्धाच् "
             "छं परत्वाद् बाधते. ग्लुचुकायनिर्भक्तिरस्य "
             "**ग्लौचुकायनकः**; औपगवकः, कापटवकः; and from kṣatriya "
             "names नाकुलकः, साहदेवकः, साम्बकः.\n\n"
             "**आख्याग्रहणं प्रसिद्धक्षत्रियशब्दपरिग्रहार्थम्, "
             "यथाकथंचित् क्षत्रियवृत्तिभ्यो मा भूत्** — *name* is "
             "there to take in the WELL-KNOWN kṣatriya words and keep "
             "out anything that merely behaves like one. And "
             "**बहुलग्रहणात् क्वचिदप्रवृत्तिरेव**: because the rule "
             "says *variously*, in some places it simply does not "
             "apply — पाणिनो भक्तिरस्य **पाणिनीयः**, पौरवीयः",
         keeps_out="पाणिनीयः, पौरवीयः"),
    Kala("4.3.100", of_samjna="janapadin", borrows_from="4.2.124",
         borrow_query=(("samjna", "janapada-vṛddha"),),
         case="prathamā", sense="bhakti",
         why="जनपदिनां जनपदवत् सर्वं जनपदेन समानशब्दानां बहुवचने. "
             "**जनपदिनो जनपदस्वामिनः क्षत्रियाः** — the kṣatriyas who "
             "own a district, named by the same word as the district. "
             "अङ्गा जनपदो भक्तिरस्य आङ्गकः, and तद्वद् **अङ्गाः "
             "क्षत्रिया भक्तिरस्य आङ्गकः**.\n\n"
             "**AN अतिदेश REACHING BACKWARD, AND THIS ONE CAN BE "
             "RUN.** 4.2.124's section is where the affixes come "
             "from — ये प्रत्यया विहिताः, ते जनपदिभ्योऽस्मिन्नर्थे "
             "ऽतिदिश्यन्ते. That rule is codified, so the code "
             "answers by asking it, where 4.3.80's forward-reaching "
             "अतिदेश can still only name what it means.\n\n"
             "**सर्वग्रहणं प्रकृत्यतिदेशार्थम्** — *all* is there so "
             "that the BASE is borrowed too and not only the affix, "
             "**स च द्व्येकयोः प्रयोजयति**: it does its work in the "
             "singular and the dual. मद्रस्यापत्यं माद्रः by 4.1.170, "
             "and स भक्तिरस्य — **प्रकृतिनिर्ह्रासे कृते मद्रकः**, "
             "the base cut back and 4.2.131's कन् given.\n\n"
             "**बहुवचनग्रहणं समानशब्दताविषयलक्षणार्थम्** — the plural "
             "marks the DOMAIN in which the two words are the same, "
             "not the number the rule applies in; अन्यथा हि यत्रैव "
             "समानशब्दता तत्रैवातिदेशः स्याद्, एकवचनद्विवचनयोर्न "
             "स्यात्. So वाङ्गो वाङ्गौ वा भक्तिरस्य **वाङ्गकः**.\n\n"
             "जनपदेन समानशब्दानामिति किम्? अनुषण्डो जनपदः, पौरवो "
             "राजा, स भक्तिरस्य **पौरवीयः**",
         keeps_out="पौरवीयः"),
    Kala("4.3.101", case="tṛtīyā", sense="prokta",
         why="तेन प्रोक्तम्. **प्रकर्षेणोक्तं प्रोक्तमित्युच्यते, न "
             "तु कृतम्, कृते ग्रन्थे इत्यनेन गतार्थत्वात्** — "
             "प्रोक्त is *set forth*, and NOT *made*, because 4.3.116 "
             "has making already. The same subtraction 4.3.41 and "
             "4.3.53 made of each other, now across fifteen sūtras.\n\n"
             "**अन्येन कृता, माथुरेण प्रोक्ता माथुरी वृत्तिः** — a "
             "commentary composed by someone else and expounded by "
             "the man of Mathurā. पाणिनीयम्, आपिशलम्, काशकृत्स्नम्: "
             "the three grammars named by their teachers"),
    Kala("4.3.102", gana="tittiryādi", gives="chaṇ", case="tṛtīyā",
         sense="prokta", excepts=("4.1.83",),
         why="तित्तिरिवरतन्तुखण्डिकोखाच्छण्, अणोऽपवादः. तित्तिरिणा "
             "प्रोक्तमधीयते **तैत्तिरीयाः** — and that is the name of "
             "a whole recension of the Yajurveda. वारतन्तवीयाः, "
             "खाण्डिकीयाः, औखीयाः.\n\n"
             "**छन्दसि चायमिष्यते** — and the affix is wanted for the "
             "Veda: तित्तिरिणा प्रोक्तः श्लोक इत्यत्र न भवति, it does "
             "not apply to an ordinary verse he set forth, because "
             "4.3.106's छन्दसि is carried back into it",
         keeps_out="तित्तिरिणा प्रोक्तः श्लोकः"),
    Kala("4.3.103", of=("kāśyapa", "kauśika"), of_samjna="ṛṣi",
         gives="ṇini", case="tṛtīyā", sense="prokta",
         excepts=("4.2.114",),
         why="काश्यपकौशिकाभ्यामृषिभ्यां णिनिः, छस्यापवादः. **णकार "
             "उत्तरत्र वृद्ध्यर्थः** — the ण् is for the "
             "strengthening in the rules that follow. काश्यपेन "
             "प्रोक्तं कल्पमधीयते **काश्यपिनः**; कौशिकिनः.\n\n"
             "ऋषिभ्यामिति किम्? **इदानींतनेन गोत्रकाश्यपेन प्रोक्तं "
             "काश्यपीयम्** — set forth by a present-day man of the "
             "Kāśyapa line and not by the seer. The same word, and "
             "which affix it takes depends on which man is meant",
         keeps_out="काश्यपीयम्"),
    Kala("4.3.104", of_samjna="kalāpi-antevāsin", gives="ṇini",
         case="tṛtīyā", sense="prokta", excepts=("4.2.114",),
         why="कलापिवैशंपायनान्तेवासिभ्यश्च, the Kalāpin half; "
             "अणोऽपवादः, छं तु परत्वाद् बाधते. Four pupils — "
             "**हरिद्रुः, छगली, तुम्बुरुः, उलप** — and हारिद्रविणः, "
             "तौम्बुरविणः, औलपिनः; छगलिनो ढिनुकं वक्ष्यति"),
    Kala("4.3.104", of_samjna="vaiśampāyana-antevāsin", gives="ṇini",
         case="tṛtīyā", sense="prokta", excepts=("4.2.114",),
         why="कलापिवैशंपायनान्तेवासिभ्यश्च, the Vaiśampāyana half. "
             "Nine pupils — आलम्बिः, पलङ्गः, कमलः, ऋचाभः, आरुणिः, "
             "ताण्ड्यः, श्यामायनः, कठः, कलापी — and आलम्बिनः, "
             "पालङ्गिनः, कामलिनः, आर्चाभिनः, आरुणिनः, ताण्डिनः, "
             "श्यामायनिनः.\n\n"
             "**AND ONLY THE DIRECT PUPILS, PROVED FROM THE LISTS "
             "THEMSELVES.** प्रत्यक्षकारिणो गृह्यन्ते, **न तु "
             "व्यवहिताः शिष्यशिष्याः** — pupils of pupils are out; "
             "कुतः? **कलापिखाडायनग्रहणात्**. कलापी is in this very "
             "list as Vaiśampāyana's pupil, so his own pupils would "
             "already be covered were the rule transitive — and yet "
             "4.3.108 gives him a rule of his own. कठ likewise is in "
             "the list and his pupil खाडायन is read in 4.3.106's. "
             "**तदेतत् प्रत्यक्षकारिग्रहणस्य लिङ्गम्**: two "
             "redundancies that are only redundant on the wrong "
             "reading, and together they settle it.\n\n"
             "Three verses list the thirteen, and "
             "**चरक इति वैशंपायनस्याख्या, तत्संबन्धेन सर्वे "
             "तदन्तेवासिनश्चरका इत्युच्यन्ते** — चरक is "
             "Vaiśampāyana's own name, and by it the whole school is "
             "called the Carakas"),
    Kala("4.3.105", gives="ṇini", result="purāṇa-prokta-brāhmaṇa-kalpa",
         case="tṛtīyā", sense="prokta",
         why="पुराणप्रोक्तेषु ब्राह्मणकल्पेषु. "
             "**प्रत्ययार्थविशेषणमेतत्** — it qualifies what the "
             "affix denotes. **पुराणेन चिरन्तनेन मुनिना प्रोक्ताः**, "
             "set forth by an ANCIENT sage. भाल्लविनः, शाट्यायनिनः, "
             "ऐतरेयिणः; and among the kalpas पैङ्गी कल्पः, "
             "आरुणपराजी.\n\n"
             "**AND THE GRAMMAR DATES ITS OWN TEXTS BY WHAT PEOPLE "
             "SAY.** पुराणप्रोक्तेष्विति किम्? **याज्ञवल्कानि "
             "ब्राह्मणानि**, आश्मरथः कल्पः — and why are those out? "
             "**याज्ञवल्क्यादयोऽचिरकाला इत्याख्यानेषु वार्ता, तया "
             "व्यवहरति सूत्रकारः**: the story goes in the "
             "traditions that Yājñavalkya and the rest are recent, "
             "and the sūtra-maker goes by that. A grammatical rule "
             "resting on a chronology the grammar does not itself "
             "establish.\n\n"
             "**पुराण इति निपातनात् तुडभावः** — the shape पुराण is "
             "laid down here without the तुट् that would otherwise "
             "come; **न चात्यन्तबाधैव, तेन पुरातनमित्यपि भवति**, and "
             "the other form is not thereby forbidden",
         keeps_out="याज्ञवल्कानि ब्राह्मणानि"),
    Kala("4.3.106", gana="śaunakādi", gives="ṇini", usage="chandasi",
         case="tṛtīyā", sense="prokta", excepts=("4.1.83", "4.2.114"),
         why="शौनकादिभ्यश्छन्दसि, छाणोरपवादः. शौनकेन प्रोक्तमधीयते "
             "**शौनकिनः** (कौषीतकिसूत्र ८५.८); **वाजसनेयिनः** "
             "(आपस्तम्बश्रौत १.८.१२) — and that is how the "
             "Vājasaneyins are named. छन्दसीति किम्? **शौनकीया "
             "शिक्षा**, which is a treatise and not scripture.\n\n"
             "**कठशाठ इत्यत्र पठ्यते; तत् संघातार्थम्, केवलाद् धि "
             "लुकं वक्ष्यति** — the compound कठशाठ is in the list for "
             "the compound's sake only, since from कठ alone the next "
             "rule elides. काठशाठिनः",
         keeps_out="शौनकीया शिक्षा"),
    Kala("4.3.107", of=("kaṭha", "caraka"), case="tṛtīyā",
         sense="prokta", elides=True,
         why="कठचरकाल्लुक्. कठेन प्रोक्तमधीयते **कठाः**; **चरकाः** — "
             "the affix given and taken away, so the school is called "
             "by its teacher's own name. From कठ what goes is "
             "4.3.104's णिनि and from चरक the अण्. छन्दसीत्येव — "
             "काठाः, चारकाः.\n\n"
             "And चरक is Vaiśampāyana's name, so this one rule names "
             "the whole school that the list of nine belongs to"),
    Kala("4.3.108", of=("kalāpin",), gives="aṇ", case="tṛtīyā",
         sense="prokta", excepts=("4.3.104",),
         why="कलापिनोऽण्. **वैशंपायनान्तेवासित्वाद् णिनेरपवादः** — "
             "कलापी is in the list of nine, so this beats the णिनि "
             "that rule would have given. कलापिना प्रोक्तमधीयते "
             "**कालापाः**.\n\n"
             "The form needs a vārttika: 6.4.164 इनण्यनपत्ये would "
             "have kept the stem whole, and "
             "**नान्तस्य टिलोपे ... कलापि ... उपसंख्यानम्** drops "
             "the टि instead.\n\n"
             "अथाण्ग्रहणं किम्, यथाप्राप्तमित्येव सिद्धम्? "
             "**अधिकविधानार्थम्** — the affix is named to give MORE "
             "than would have come: तेन माथुरी वृत्तिः, सौलभानि "
             "ब्राह्मणानि, and the like are got by it"),
    Kala("4.3.109", of=("chagalin",), gives="ḍhinuk", case="tṛtīyā",
         sense="prokta", excepts=("4.3.104",),
         why="छगलिनो ढिनुक्. **कलाप्यन्तेवासित्वाद् णिनेरपवादः** — "
             "छगली is in the list of four. छगलिना प्रोक्तमधीयते "
             "**छागलेयिनः**"),
    Kala("4.3.110", of=("pārāśarya", "śilāli"), gives="ṇini",
         result="bhikṣu-naṭa-sūtra", case="tṛtīyā", sense="prokta",
         why="पाराशर्यशिलालिभ्यां भिक्षुनटसूत्रयोः. **णिनिरिहानुवर्तते, "
             "न ढिनुक्** — the णिनि carries and the last rule's affix "
             "does not. यथासंख्यम्, and **सूत्रशब्दः "
             "प्रत्येकमभिसंबध्यते**: *aphorisms* attaches to each, so "
             "it is the BEGGARS' aphorisms and the ACTORS'. "
             "पाराशरिणो **भिक्षवः**; शैलालिनो **नटाः**.\n\n"
             "भिक्षुनटसूत्रयोरिति किम्? पाराशरम्, शैलालम्",
         keeps_out="पाराशरम्, शैलालम्"),
    Kala("4.3.111", of=("karmanda", "kṛśāśva"), gives="ini",
         result="bhikṣu-naṭa-sūtra", case="tṛtīyā", sense="prokta",
         excepts=("4.1.83",),
         why="कर्मन्दकृशाश्वादिनिः, भिक्षुनटसूत्रयोरित्येव; "
             "अणोऽपवादः; यथासंख्यम्. कर्मन्दिनो भिक्षवः; कृशाश्विनो "
             "नटाः. भिक्षुनटसूत्रयोरित्येव — कार्मन्दम्, कार्शाश्वम्",
         keeps_out="कार्मन्दम्, कार्शाश्वम्"),
    Kala("4.3.112", case="tṛtīyā", sense="ekadik",
         why="तेनैकदिक्. **एकदिक् तुल्यदिक्, समानदिगित्यर्थः** — "
             "lying in the same direction as that. सुदाम्ना एकदिक् "
             "**सौदामनी विद्युत्**, the lightning that is on a line "
             "with Sudāman; हैमवती, त्रैककुदी, पैलुमूली.\n\n"
             "**तेनेति प्रकृते पुनः समर्थविभक्तिग्रहणं "
             "छन्दोऽधिकारनिवृत्त्यर्थम्** — तेन was already carrying, "
             "and it is said AGAIN in order to cancel the Vedic "
             "heading. A word repeated to push another out, as at "
             "4.3.53"),
    Kala("4.3.113", gives="tasi", case="tṛtīyā", sense="ekadik",
         why="तसिश्च. **पूर्वेण घादिष्वणादिषु च प्राप्तेष्वयमपरः "
             "प्रत्ययो विधीयते** — the last rule had घ and अण् and "
             "the rest available, and this gives one more besides. "
             "सुदामतः, हिमवत्तः, पिलुमूलतः. "
             "**स्वरादिपाठादव्ययत्वम्**: the result is indeclinable "
             "because तसि is read in the स्वरादि list"),
    Kala("4.3.114", of=("uras",), gives="yat", also_gives=("tasi",),
         case="tṛtīyā", sense="ekadik", excepts=("4.1.83",),
         why="उरसो यच्च, अणोऽपवादः. उरसैकदिग् **उरस्यः** by the यत्, "
             "and **उरस्तः** by the च, which brings the last rule's "
             "तसि along"),
    Kala("4.3.115", case="tṛtīyā", sense="upajñāta",
         why="उपज्ञाते, तेनेत्येव. **विनोपदेशेन ज्ञातमुपज्ञातम्, "
             "स्वयमभिसंबुद्धमित्यर्थः** — known WITHOUT being taught, "
             "found out for oneself. पाणिनिनोपज्ञातं **पाणिनीयम् "
             "अकालकं व्याकरणम्**, the grammar without tenses that "
             "Pāṇini worked out himself; काशकृत्स्नं गुरुलाघवम्, "
             "आपिशलं दुष्करणम्"),
    Kala("4.3.116", case="tṛtīyā", sense="kṛta", result="grantha",
         why="कृते ग्रन्थे, तेनेत्येव. वररुचिना कृता **वाररुचाः "
             "श्लोकाः**; हैकुपादो ग्रन्थः, भैकुराटो ग्रन्थः, जालूकः. "
             "ग्रन्थ इति किम्? **तक्षकृतः प्रासादः**.\n\n"
             "**उत्पादितं कृतम्, विद्यमानमेव ज्ञातमुपज्ञातम् "
             "इत्ययमनयोर्विशेषः** — what is MADE is brought into "
             "being; what is DISCOVERED was already there and came to "
             "be known. Two rules a sūtra apart, and the difference "
             "between them is whether the thing existed first",
         keeps_out="तक्षकृतः प्रासादः"),
    Kala("4.3.117", of_samjna="saṃjñā", case="tṛtīyā", sense="kṛta",
         why="संज्ञायाम्. **समुदायेन चेत् संज्ञा ज्ञायते** — if the "
             "NAME is known from the whole. मक्षिकाभिः कृतं "
             "**माक्षिकम्**; कार्मुकम्, सारघम्, पौत्तिकम् — "
             "**मधुनः संज्ञा एताः**, and all four are names for kinds "
             "of honey, each called after what made it"),
    Kala("4.3.118", gana="kulālādi", gives="vuñ", of_samjna="saṃjñā",
         case="tṛtīyā", sense="kṛta", excepts=("4.1.83",),
         why="कुलालादिभ्यो वुञ्. **तेन, कृते, संज्ञायामिति चैतत् "
             "सर्वमनुवर्तते** — the instrumental, the making and the "
             "name all carry. कौलालकम्, वारुडकम्"),
    Kala("4.3.119", gana="kṣudrādi", gives="añ", of_samjna="saṃjñā",
         case="tṛtīyā", sense="kṛta", excepts=("4.1.83",),
         why="क्षुद्राभ्रमरवटरपादपादञ्, अणोऽपवादः; **स्वरे विशेषः**, "
             "and the two differ only in the accent. क्षुद्राभिः "
             "कृतं **क्षौद्रम्**, honey made by the small bees; "
             "भ्रामरम्, वाटरम्, पादपम् — and these too are honeys, "
             "named by which bee made them"),
    Kala("4.3.120", case="ṣaṣṭhī", sense="idam",
         why="तस्येदम्. उपगोरिदम् **औपगवम्**; कापटवम्, राष्ट्रियम्, "
             "अवारपारीणम्.\n\n"
             "**अणादयः पञ्च महोत्सर्गाः, घादयश्च प्रत्यया यथाविहितं "
             "विधीयन्ते** — five GREAT general rules stand behind "
             "this one, and the affixes come as already prescribed.\n\n"
             "**AND EVERYTHING BUT THE RELATION IS LEFT OUT OF "
             "ACCOUNT.** प्रकृतिप्रत्ययार्थयोः **षष्ठ्यर्थमात्रं "
             "तत्संबन्धिमात्रं च विवक्षितम्, यदपरं "
             "लिङ्गसंख्याप्रत्यक्षपरोक्षादिकं तत् सर्वमविवक्षितम्** — "
             "only the genitive relation and the fact of being "
             "related are meant; gender, number, whether the thing is "
             "before one's eyes or out of sight, all of it is not "
             "meant. The widest sense in the taddhita section, and "
             "the vṛtti says what it costs.\n\n"
             "**अनन्तरादिष्वनभिधानाद् न भवति** — and it does not "
             "reach देवदत्तस्यानन्तरम्, because that is not how the "
             "language says it. Three vārttikas add particular "
             "shapes: संवहेस्तुरणिट् च — **सांवहित्रम्**; अग्नीधः "
             "शरणे रञ् भं च — **आग्नीध्रम्**; समिधामाधाने षेण्यण् — "
             "**सामिधेन्यो मन्त्रः**, सामिधेनी ऋक्",
         keeps_out="देवदत्तस्यानन्तरम्"),
    Kala("4.3.121", of=("ratha",), gives="yat", case="ṣaṣṭhī",
         sense="idam", excepts=("4.1.83",),
         why="रथाद् यत्, अणोऽपवादः. रथस्येदं **रथ्यम्**, चक्रं वा युगं "
             "वा — a wheel or a yoke.\n\n"
             "**रथाङ्ग एवेष्यते नान्यत्र, अनभिधानात्** — only of a "
             "PART of the chariot and nowhere else, because that is "
             "not how the word is used. And a Mahābhāṣya vārttika on "
             "1.1.72, **रथसीताहलेभ्यो यद्विधौ**, adds that the rule "
             "reaches compounds ending in these words: परमरथ्यम्, "
             "उत्तमरथ्यम्"),
    Kala("4.3.122", pre="patra", of=("ratha",), gives="añ",
         case="ṣaṣṭhī", sense="idam", excepts=("4.3.121",),
         why="पत्रपूर्वादञ्, पूर्वस्य यतोऽपवादः. **पतन्ति तेनेति "
             "पत्रम्** — a पत्र is what one travels by, a mount. "
             "आश्वरथं चक्रम्, औष्ट्ररथम्, गार्दभरथम्: the wheel of a "
             "horse-chariot, a camel-chariot, a donkey-chariot"),
    Kala("4.3.123", of_samjna="patra", gives="añ", case="ṣaṣṭhī",
         sense="idam", excepts=("4.1.83",),
         why="पत्राध्वर्युपरिषदश्च, अणोऽपवादः. **पत्रं वाहनम्** — a "
             "mount; and a vārttika reads **पत्राद् वाह्ये**, only of "
             "what is CARRIED by it. अश्वस्येदं वहनीयम् **आश्वम्**; "
             "औष्ट्रम्, गार्दभम्. And from the two named words, "
             "आध्वर्यवम्, पारिषदम् — what belongs to the Adhvaryu "
             "priest and to the assembly"),
    Kala("4.3.124", of=("hala", "sīra"), gives="ṭhak", case="ṣaṣṭhī",
         sense="idam", excepts=("4.1.83",),
         why="हलसीराट् ठक्, अणोऽपवादः. हलस्येदं **हालिकम्**; "
             "सैरिकम् — what belongs to the plough"),
    Kala("4.3.125", of_samjna="dvandva", gives="vun",
         result="vaira-maithunika", case="ṣaṣṭhī", sense="idam",
         excepts=("4.1.83", "4.2.114"),
         why="द्वन्द्वाद् वुन् वैरमैथुनिकयोः, अणोऽपवादः; छं तु "
             "परत्वाद् बाधते. The two conditions qualify what the "
             "affix denotes: a FEUD or an INTERMARRIAGE between the "
             "two families the dvandva names.\n\n"
             "वैरे — **बाभ्रव्यशालङ्कायनिका**, the feud of the "
             "Bābhravyas and the Śālaṅkāyanas; **काकोलूकिका**, of "
             "crows and owls. मैथुनिकायाम् — अत्रिभरद्वाजिका, "
             "कुत्सकुशिकिका; **विवहनं मैथुनिका**.\n\n"
             "**वैरस्य नपुंसकत्वेऽप्यमी स्वभावतः स्त्रीलिङ्गाः** — "
             "though वैर is neuter these forms are feminine by their "
             "own nature. A vārttika refuses one kind: **वैरे "
             "देवासुरादिभ्यः प्रतिषेधः**, दैवासुरम्, राक्षोऽसुरं "
             "वैरम् — the same refusal 4.3.88 needed, and for the "
             "same list",
         keeps_out="दैवासुरं वैरम्"),
    Kala("4.3.126", of_samjna="gotra-caraṇa", gives="vuñ",
         case="ṣaṣṭhī", sense="idam", excepts=("4.1.83", "4.2.114"),
         why="गोत्रचरणाद् वुञ्, अणोऽपवादः; छं तु परत्वाद् बाधते. "
             "From a lineage — ग्लौचुकायनकम्, **औपगवकम्**. And a "
             "vārttika narrows the other half: **चरणाद् "
             "धर्माम्नाययोरिष्यते**, from a Vedic SCHOOL only when "
             "its rule of life or its tradition is meant — काठकम्, "
             "कालापकम्, मौदकम्, पैप्पलादकम्.\n\n"
             "This is the rule 4.3.80's अतिदेश actually reaches. It "
             "names अङ्कवत् and so points at 4.3.127, but the words "
             "its examples are built on end in अण् and not in "
             "अञ्/यञ्/इञ् — which is why the vṛtti there insists "
             "**तस्माद् वुञप्यतिदिश्यते नाणेव**"),
    Kala("4.3.127", of_samjna="añ-yañ-iñ-anta", gives="aṇ",
         case="ṣaṣṭhī", sense="idam", excepts=("4.3.126",),
         why="संघाङ्कलक्षणेष्वञ्यञिञामण्, पूर्वस्य वुञोऽपवादः. Three "
             "kinds of base and three conditions on what the affix "
             "denotes — a BODY of men, a BRAND, a MARK — and a "
             "vārttika adds a fourth: **घोषग्रहणमत्र कर्तव्यम्**, a "
             "settlement. **तेन वैषम्याद् यथासंख्यं न भवति**: with "
             "four against three the pairing cannot run, so every "
             "base takes every sense. बैदः संघः, बैदोऽङ्कः, बैदं "
             "लक्षणम्, बैदो घोषः; गार्गः, दाक्षः likewise.\n\n"
             "**अङ्कलक्षणयोः को विशेषः?** — what separates a brand "
             "from a mark? **लक्षणं लक्ष्यस्यैव चिह्नभूतं स्वं**, a "
             "mark is the thing's own and belongs to it, यथा विद्या "
             "बिदानाम्; **अङ्कस्तु गवादिस्थोऽपि गवादीनां स्वं न "
             "भवति**, a brand stands ON the cattle and is not "
             "theirs.\n\n"
             "**णित्करणं ङीबर्थं पुंवद्भावप्रतिषेधार्थं च** — the ण् "
             "is for the feminine ङीप् and to stop 6.3.34 from "
             "treating that feminine as a masculine: बैदी विद्यास्य "
             "बैदीविद्यः.\n\n"
             "AND THIS IS THE RULE 4.3.80 REACHES FORWARD TO. That "
             "debt was written as the exact shortfall — a test "
             "asserting this sūtra was NOT codified — and it collects "
             "itself here"),
    Kala("4.3.128", of=("śākala",), gives="aṇ", optional=True,
         result="saṃgha-aṅka-lakṣaṇa-ghoṣa", case="ṣaṣṭhī",
         sense="idam", excepts=("4.3.126",),
         why="शाकलाद् वा, वुञोऽपवादः. शाकल्येन प्रोक्तमधीयते शाकलाः, "
             "तेषां संघः **शाकलः** beside **शाकलकः**; शाकलोऽङ्कः "
             "beside शाकलकोऽङ्कः, and so for the mark and the "
             "settlement. Four conditions and two forms under each"),
    Kala("4.3.129", gana="chandogādi", gives="ñya",
         result="dharma-āmnāya", case="ṣaṣṭhī", sense="idam",
         excepts=("4.3.126", "4.1.83"),
         why="छन्दोगौक्थिकयाज्ञिकबह्वृचनटाञ् ञ्यः, वुञणोरपवादः. "
             "**संघादयो निवृत्ताः, सामान्येन विधानम्** — the four "
             "conditions of 4.3.127 have lapsed and the rule is "
             "general.\n\n"
             "But **चरणाद् धर्माम्नाययोः, तत्साहचर्याद् नटशब्दादपि "
             "धर्माम्नाययोरेव भवति** — the school-vārttika's "
             "restriction carries by association even to नट, which is "
             "not a school. छान्दोग्यम्, औक्थिक्यम्, याज्ञिक्यम्, "
             "बाह्वृच्यम्, **नाट्यम्** — the word for dramatic art, "
             "made by this rule. अन्यत्र छान्दोगं कुलम्",
         keeps_out="छान्दोगं कुलम्"),
    Kala("4.3.130", of_samjna="gotra-caraṇa", gives="vuñ",
         result="daṇḍamāṇava-antevāsin",
         case="ṣaṣṭhī", sense="idam", refuses=True,
         why="न दण्डमाणवान्तेवासिषु. **दण्डप्रधाना माणवा दण्डमाणवाः**, "
             "boys carrying staves; अन्तेवासिनः शिष्याः, pupils. "
             "Where THEY are what is meant the affix does not come. "
             "गौकक्षाः दण्डमाणवा अन्तेवासिनो वा; दाक्षाः, माहकाः.\n\n"
             "**गोत्रग्रहणमिहानुवर्तते, तेन वुञ्प्रतिषेधो विज्ञायते** "
             "— the lineage-word carries into this rule, and that is "
             "how one knows it is 4.3.126's वुञ् that is refused and "
             "not some other affix. The pāda's only प्रतिषेध, and it "
             "identifies its target by what it inherits",
         keeps_out="गौकक्षाः दण्डमाणवाः"),
    Kala("4.3.131", gana="raivatikādi", gives="cha", case="ṣaṣṭhī",
         sense="idam", excepts=("4.3.126",),
         why="रैवतिकादिभ्यश्छः. **गोत्रप्रत्ययान्ता एते, ततः पूर्वेण "
             "वुञि प्राप्ते छविधानार्थं वचनम्** — every member of "
             "this list already ends in a lineage-affix, so 4.3.126 "
             "had them; the rule exists to give छ instead. "
             "रैवतिकीयः, स्वापिशीयः"),
    Kala("4.3.132", of=("kaupiñjala", "hāstipada"), gives="aṇ",
         case="ṣaṣṭhī", sense="idam", excepts=("4.3.126",),
         why="कौपिञ्जलहास्तिपदादण्, **गोत्रवुञोऽपवादः, "
             "गोत्राधिकारात्** — an exception to the lineage-वुञ्, "
             "and it is one because the lineage-heading is still "
             "running. कौपिञ्जलः, हास्तिपदः"),
    Kala("4.3.133", of=("ātharvaṇika",), gives="aṇ", drops="ika",
         case="ṣaṣṭhī", sense="idam", excepts=("4.3.126",),
         why="आथर्वणिकस्येकलोपश्च, अणित्येव; **चरणवुञोऽपवादः**. The "
             "अण् and the loss of the इक in one act: "
             "आथर्वणिकस्यायम् **आथर्वणो धर्म आम्नायो वा** — and the "
             "school-vārttika's restriction to a rule of life or a "
             "tradition holds here too"),
    Kala("4.3.134", case="ṣaṣṭhī", sense="vikāra",
         why="तस्य विकारः. **प्रकृतेरवस्थान्तरं विकारः** — a "
             "modification is the source-material in another state.\n\n"
             "**किमिहोदाहरणम्?** — what is left for this rule to work "
             "on? **अप्राण्याद्युदात्तमवृद्धम्, यस्य च नान्यत् "
             "प्रतिपदं विधानम्**: something not animate, not "
             "initially accented, not वृद्ध, and not covered by a rule "
             "of its own. अश्मनो विकार **आश्मनः**, आश्मः; भास्मनः, "
             "मार्त्तिकः.\n\n"
             "**तस्यप्रकरणे तस्येति पुनर्वचनं शैषिकनिवृत्त्यर्थम्** — "
             "तस्य is said again, inside a section that already had "
             "it, to cancel the शैष heading. The same instrument as "
             "4.3.53's and 4.3.112's, and the third time in this "
             "pāda that a word is repeated to push another out.\n\n"
             "**विकारावयवयोर्घादयो न भवन्ति** — and the घ-affixes do "
             "not reach these two senses: हालः, सैरः"),
    Kala("4.3.135", of_samjna="prāṇi-oṣadhi-vṛkṣa", case="ṣaṣṭhī",
         sense="avayava", also_sense="vikāra",
         why="अवयवे च प्राण्योषधिवृक्षेभ्यः. From words for LIVING "
             "THINGS, HERBS and TREES, in the sense of a PART — and "
             "by the च in the sense of a modification as well. "
             "कपोतस्य विकारोऽवयवो वा **कापोतः**; मायूरः, तैत्तिरः; "
             "मौर्वं काण्डम्, मौर्वं भस्म; कारीरं काण्डम्.\n\n"
             "**AND THE SAME FORMULA AS 4.3.66, WORD FOR WORD.** कथं "
             "द्वयमप्यधिक्रियते तस्य विकारः, अवयवे च "
             "प्राण्योषधिवृक्षेभ्य इति? **विकारावयवयोर्युगपदधिकारो "
             "ऽपवादविधानार्थः, कृतनिर्देशौ हि तौ** — the two headings "
             "are made to run SIMULTANEOUSLY so that the exceptions "
             "after them can be stated once for both. 4.3.66 said "
             "exactly this of भव and व्याख्यान, sixty-nine sūtras "
             "back, in the same words.\n\n"
             "**इत उत्तरे प्रत्ययाः प्राण्योषधिवृक्षेभ्यो "
             "विकारावयवयोर्भवन्ति, अन्येभ्यस्तु विकारमात्रे** — from "
             "here on the affixes reach both senses for these three "
             "classes and only the modification for anything else"),
    Kala("4.3.136", gana="bilvādi", gives="aṇ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava",
         excepts=("4.3.154", "4.3.143"),
         why="बिल्वादिभ्योऽण्, **यथायोगमञ्मयटोरपवादः**. बिल्वस्य "
             "विकारोऽवयवो वा **बैल्वः**.\n\n"
             "**गवेधुकाशब्दोऽत्र पठ्यते, ततः कोपधादेव सिद्धे "
             "मयड्बाधनार्थं ग्रहणम्** — गवेधुका is in the list "
             "although the next rule's कोपध would have given it अण् "
             "anyway; it is read here to beat the मयट् of 4.3.143. An "
             "entry that adds nothing where it stands and everything "
             "eight sūtras later"),
    Kala("4.3.137", upadha="k", gives="aṇ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava", excepts=("4.3.139",),
         why="कोपधाच्च, अञोऽपवादः. तर्कु — **तार्कवम्**; तित्तिडीक — "
             "तैत्तिडीकम्; माण्डूकम्, दार्दुरूकम्, माधूकम्.\n\n"
             "The penultimate again, and the same reason as 4.2.132's: "
             "तर्कु does not END in क, it ends in उ and has क before "
             "it. A column that would have been wrong as `stem_final`"),
    Kala("4.3.138", of=("trapu", "jatu"), gives="aṇ", augment="ṣuk",
         case="ṣaṣṭhī", sense="vikāra", excepts=("4.3.139",),
         why="त्रपुजतुनोः षुक्, **ओरञोऽपवादः**. The अण् with षुक् "
             "added to the base in the same act: त्रपुणो विकारः "
             "**त्रापुषम्**; **जातुषम्**.\n\n"
             "**अप्राण्यादित्वाद् नावयवे** — and not in the sense of "
             "a PART, because neither word names a living thing, a "
             "herb or a tree. The condition 4.3.135 set, doing work "
             "three sūtras later"),
    Kala("4.3.139", stem_final="u", gives="añ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava", excepts=("4.1.83",),
         why="ओरञ्, अणोऽपवादः. **अनुदात्तादेरन्यदिहोदाहरणम्** — the "
             "example has to be something whose first vowel is NOT "
             "unaccented, since the next rule takes those. "
             "दैवदारवम्, भाद्रदारवम्"),
    Kala("4.3.140", accent="anudāttādi", gives="añ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava", excepts=("4.1.83",),
         why="अनुदात्तादेश्च, अणोऽपवादः. दाधित्थम्, कापित्थम्, "
             "माहित्थम् — from bases whose FIRST vowel is unaccented, "
             "where 4.2.109 wanted the accent on the last"),
    Kala("4.3.141", gana="palāśādi", gives="añ", optional=True,
         case="ṣaṣṭhī", sense="vikāra", also_sense="avayava",
         why="पलाशादिभ्यो वा. पालाशम्, खादिरम्, यावासम्.\n\n"
             "**उभयत्र विभाषेयम्** — the option works in both "
             "directions at once: **पलाशखदिरशिंशपास्पन्दनानाम् "
             "अनुदात्तादित्वात् प्राप्ते, अन्येषामप्राप्ते** — for "
             "four members of the list the affix was already coming "
             "by the last rule and the option lets it go; for the "
             "rest it was not coming and the option brings it. One "
             "word doing opposite work on one list"),
    Kala("4.3.142", of=("śamī",), gives="ṭlañ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava", excepts=("4.3.140",),
         why="शम्यष्ट्लञ्, अञोऽपवादः. **शामीलं भस्म**, ash of the "
             "śamī wood; **शामीली स्रुक्**, a ladle of it — and the "
             "ट् is what brings the feminine ending on the second"),
    Kala("4.3.143", gives="mayaṭ", optional=True, usage="bhāṣā",
         result="abhakṣya-ācchādana", case="ṣaṣṭhī", sense="vikāra",
         also_sense="avayava",
         why="मयड्वैतयोर्भाषायामभक्ष्याच्छादनयोः. From ANY base, "
             "optionally, in the spoken language, where the thing is "
             "neither food nor clothing. अश्ममयम् beside आश्मनम्; "
             "मूर्वामयम् beside मौर्वम्.\n\n"
             "Three conditions and a counter-example each. भाषायामिति "
             "किम्? **बैल्वः खादिरो वा यूपः** (आपस्तम्बश्रौत "
             "१८.१.८) — a Vedic sacrificial post. अभक्ष्याच्छादनयोरिति "
             "किम्? **मौद्गः सूपः**, bean soup, and "
             "**कार्पासमाच्छादनम्**, cotton cloth.\n\n"
             "एतयोरित्यनेन किम्, यावता विकारावयवौ प्रकृतावेव? — why "
             "name the two senses when they were carrying anyway? "
             "**ये विशेषप्रत्ययाः प्राणिरजतादिभ्योऽञ् इत्येवमादयस् "
             "तद्विषयेऽपि यथा स्यात्** — so that the option reaches "
             "even where a special affix has been given: कपोतमयम् "
             "beside कापोतम्, लोहमयम् beside लौहम्",
         keeps_out="बैल्वो यूपः, मौद्गः सूपः, कार्पासमाच्छादनम्"),
    Kala("4.3.144", of_samjna="vṛddha", gives="mayaṭ", usage="bhāṣā",
         result="abhakṣya-ācchādana", case="ṣaṣṭhī", sense="vikāra",
         also_sense="avayava", excepts=("4.3.143",),
         why="नित्यं वृद्धशरादिभ्यः, भाषायामभक्ष्याच्छादनयोरित्येव. "
             "From a वृद्ध base and from the शरादि list the मयट् is "
             "FIXED where the last rule made it optional. आम्रमयम्, "
             "शालमयम्, शाकमयम्; शरमयम्, दर्भमयम्, मृन्मयम्.\n\n"
             "**नित्यग्रहणं किम्, यावतारम्भसामर्थ्यादेव नित्यं "
             "भविष्यति?** — why say *always*, when the mere fact of "
             "stating the rule would have made it fixed? "
             "**एकाचो नित्यं मयटमिच्छन्ति, तदनेन क्रियते** — because "
             "a one-vowel base is wanted to take मयट् always too, and "
             "the word does that: **त्वङ्मयम्, स्रङ्मयम्, "
             "वाङ्मयम्** — and the last of those is the ordinary word "
             "for literature"),
    Kala("4.3.145", of=("go",), gives="mayaṭ", result="purīṣa",
         case="ṣaṣṭhī", sense="idam",
         why="गोश्च पुरीषे. **गोमयम्** — cow-dung. पुरीष इति किम्? "
             "**गव्यं पयः**.\n\n"
             "**पुरीषं न विकारो नाप्यवयवः, तस्येदंविषये विधानम्** — "
             "dung is neither a modification of the cow nor a part of "
             "her, so the rule is stated back in 4.3.120's sense and "
             "not in the two that have been running. "
             "**विकारावयवयोस्तु गोपयसोर्यतं वक्ष्यति** — for those "
             "two 4.3.160 will give यत् instead. A rule reaching back "
             "over the heading it sits inside",
         keeps_out="गव्यं पयः"),
    Kala("4.3.146", of=("piṣṭa",), gives="mayaṭ", case="ṣaṣṭhī",
         sense="vikāra", excepts=("4.1.83",),
         why="पिष्टाच्च, अणोऽपवादः. **पिष्टमयं भस्म** — and the मयट् "
             "is fixed here, where 4.3.143 made it optional"),
    Kala("4.3.147", of=("piṣṭa",), gives="kan", of_samjna="saṃjñā",
         case="ṣaṣṭhī", sense="vikāra", excepts=("4.3.146",),
         why="संज्ञायां कन्, मयटोऽपवादः. **पिष्टकः** — a cake, where "
             "the whole word is a NAME and not a description"),
    Kala("4.3.148", of=("vrīhi",), gives="mayaṭ", result="puroḍāśa",
         case="ṣaṣṭhī", sense="vikāra", excepts=("4.3.136",),
         why="व्रीहेः पुरोडाशे, बिल्वाद्यणोऽपवादः. **व्रीहिमयः "
             "पुरोडाशः** — the sacrificial cake of rice; "
             "**व्रैहमन्यत्**, and anything else takes the अण् of "
             "4.3.136, since व्रीहि is in that list",
         keeps_out="व्रैहम्"),
    Kala("4.3.149", of=("tila", "yava"), gives="mayaṭ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava",
         why="असंज्ञायां तिलयवाभ्याम्. तिलमयम्, यवमयम्.\n\n"
             "असंज्ञायामिति किम्? **तैलम्**, sesame OIL, and "
             "**यावकः** by 5.4.29 यावादिभ्यः कन् — both of them "
             "names, and so outside a rule stated for what is not a "
             "name. The condition of 4.3.147 read the other way round, "
             "two sūtras later",
         keeps_out="तैलम्, यावकः"),
    Kala("4.3.150", vowels="dvyac", usage="chandasi", gives="mayaṭ",
         case="ṣaṣṭhī", sense="vikāra", also_sense="avayava",
         why="द्व्यचश्छन्दसि. **भाषायां मयडुक्तः, छन्दस्यप्राप्तो "
             "विधीयते** — 4.3.143 gave the मयट् for the spoken "
             "language, where it could not reach the Veda; this rule "
             "supplies what was therefore unavailable there.\n\n"
             "Three quotations, one from each of three recensions: "
             "**यस्य पर्णमयी जुहूर्भवति** (तैत्तिरीयसंहिता "
             "३.५.७.१); **दर्भमयं वासो भवति** (मैत्रायणीसंहिता "
             "१.११.८); **शरमयं बर्हिर्भवति** (आपस्तम्बश्रौत ९.७.५)"),
    Kala("4.3.151", of_samjna="utvat", gives="mayaṭ", vowels="dvyac",
         usage="chandasi", case="ṣaṣṭhī", sense="vikāra", refuses=True,
         why="नोत्वद्वर्ध्रबिल्वात्, the उत्वत् half. **द्व्यचश्छन्दसि "
             "इति प्राप्तः प्रतिषिध्यते** — what the last rule gave "
             "is taken back for a base containing उ. **मौञ्जं "
             "शिक्यम्** (तैत्तिरीयसंहिता ५.१.१०.५); **गार्मुतं "
             "चरुम्** (तैत्तिरीयसंहिता २.४.४.१).\n\n"
             "**तपरकरणं तत्कालार्थम्** — the त appended to the उ "
             "confines it to that quantity: धूममयान्यभ्राणि stands, "
             "because its ऊ is long. And **मतुब्निर्देशस्तदन्तविधि"
             "निरासार्थः**: the rule says *having* उ rather than "
             "*ending in* it, so 1.1.72 does not extend it — "
             "वैणवी यष्टिः would otherwise have come in",
         keeps_out="धूममयान्यभ्राणि"),
    Kala("4.3.151", of=("vardhra", "bilva"), gives="mayaṭ",
         vowels="dvyac", usage="chandasi", case="ṣaṣṭhī",
         sense="vikāra", refuses=True,
         why="नोत्वद्वर्ध्रबिल्वात्, the two named words. **वार्ध्री "
             "बालप्रग्रथिता भवति** (आपस्तम्बश्रौत १८.१०.२३); "
             "**बैल्वो ब्रह्मवर्चसकामेन कार्यः** (मैत्रायणीसंहिता "
             "३.९.३) — and both forms are quoted from the texts the "
             "refusal is stated for"),
    Kala("4.3.152", gana="tālādi", gives="aṇ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava",
         excepts=("4.3.143", "4.3.154"),
         why="तालादिभ्योऽण्, **मयडादीनामपवादः**. **तालं धनुः** — a "
             "bow of palm-wood, and a गणसूत्र **तालाद् धनुषि** "
             "confines that first entry to a bow. बार्हिणम्, "
             "ऐन्द्रालिशम्"),
    Kala("4.3.153", of_samjna="jātarūpa", gives="aṇ", result="parimāṇa",
         case="ṣaṣṭhī", sense="vikāra", excepts=("4.3.143",),
         why="जातरूपेभ्यः परिमाणे, मयडादीनामपवादः. **जातरूपं "
             "सुवर्णम्** — gold; and **बहुवचननिर्देशात् तद्वाचिनः "
             "सर्वे गृह्यन्ते**, the plural in the rule takes in every "
             "word for it. हाटको निष्कः, हाटकं कार्षापणम्; "
             "जातरूपम्, तापनीयम्.\n\n"
             "परिमाण इति किम्? **यष्टिरियं हाटकमयी** — a golden "
             "STAFF is no measure, and takes the मयट् back",
         keeps_out="यष्टिरियं हाटकमयी"),
    Kala("4.3.154", of_samjna="prāṇin", gives="añ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava", excepts=("4.3.143",),
         why="प्राणिरजतादिभ्योऽञ्, the प्राणिन् half; अणादीनामपवादः. "
             "कापोतम्, मायूरम्, तैत्तिरम् — and this is the affix "
             "4.3.135 promised when it named living things",
         keeps_out="बैल्वमयम्"),
    Kala("4.3.154", gana="rajatādi", gives="añ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava", excepts=("4.3.143",),
         why="प्राणिरजतादिभ्योऽञ्, the रजतादि half. राजतम्, सैसम्, "
             "**लौहम्**.\n\n"
             "**रजतादिषु येऽनुदात्तादयः पठ्यन्ते रजतकण्टकारप्रभृतयः, "
             "तेभ्योऽञि सिद्धे पुनर्वचनं मयड्बाधनार्थम्** — several "
             "members of the list have an unaccented first vowel and "
             "so had the अञ् from 4.3.140 already; they are read again "
             "here to beat the मयट्. The same shape as गवेधुका in "
             "4.3.136's list"),
    Kala("4.3.155", of_samjna="ñit-pratyayānta", gives="añ",
         case="ṣaṣṭhī", sense="vikāra", also_sense="avayava",
         excepts=("4.3.143",),
         why="ञितश्च तत्प्रत्ययात्, अञित्येव; मयटोऽपवादः. **ञिद् यो "
             "विकारावयवप्रत्ययः, तदन्तात् प्रातिपदिकादञ्** — from a "
             "base ending in a ञित् affix given in these two senses, "
             "the अञ् again.\n\n"
             "**AND THE VṚTTI LISTS THE RULES ITS CONDITION POINTS "
             "AT.** ओरञ् [4.3.139], शम्याष्ट्लञ् [4.3.142], "
             "प्राणिरजतादिभ्योऽञ् [4.3.154], उष्ट्राद् वुञ् "
             "[4.3.157], एण्या ढञ् [4.3.159], "
             "कंसीयपरशव्ययोर्यञञौ [4.3.168] — six rules named by "
             "number, and every one of them gives an affix marked "
             "with ञ्. दैवदारवस्य विकारो दैवदारवम्; पालाशस्य "
             "पालाशम्; कापोतस्य कापोतम्; कांस्यस्य कांस्यम्.\n\n"
             "ञित इति किम्? **बैल्वमयम्**. तत्प्रत्ययादिति किम्? "
             "**बैदमयम्** — where the ञित् affix was given in some "
             "OTHER sense",
         keeps_out="बैल्वमयम्, बैदमयम्"),
    Kala("4.3.156", of_samjna="parimāṇa", case="ṣaṣṭhī", sense="vikāra",
         borrows_from="5.1.18",
         borrow_query=(("sense", "ārhīya"), ("case", "tṛtīyā")),
         why="क्रीतवत् परिमाणात्, अणादीनामपवादः. **प्राग्वतेष्ठञ् "
             "इत्यत आरभ्य क्रीतार्थे ये प्रत्ययाः परिमाणाद् "
             "विहिताः, ते विकारेऽतिदिश्यन्ते** — the affixes given "
             "from a measure in the sense *bought for* are borrowed "
             "into the sense *a modification of*.\n\n"
             "निष्केण क्रीतं नैष्किकम्, and so निष्कस्य विकारो "
             "**नैष्किकः**; शतेन क्रीतं शत्यम् and शतस्य विकारः "
             "शत्यः; साहस्रः. **संख्यापि परिमाणग्रहणेन गृह्यते, न "
             "रूढिपरिमाणमेव** — a NUMBER counts as a measure too and "
             "not only a measure properly so called.\n\n"
             "**वतिः सर्वसादृश्यार्थः** — the वति takes in EVERY "
             "likeness, so even 5.1.28's elision comes along: "
             "द्विसहस्रः, द्विसाहस्रः; द्विनिष्कः, द्विनैष्किकः. The "
             "same words 4.2.34 used, and the third अतिदेश of this "
             "pāda to reach forward — this one into a quarter not "
             "codified yet, so the row names it and no more"),
    Kala("4.3.157", of=("uṣṭra",), gives="vuñ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava", excepts=("4.3.154",),
         why="उष्ट्राद् वुञ्, **प्राण्यञोऽपवादः**. उष्ट्रस्य विकारो "
             "ऽवयवो वा **औष्ट्रकः** — and वुञ् is one of the six "
             "ञित् affixes 4.3.155 reaches for"),
    Kala("4.3.158", of=("umā", "ūrṇā"), gives="vuñ", optional=True,
         case="ṣaṣṭhī", sense="vikāra", also_sense="avayava",
         why="उमोर्णयोर्वा. औमकम् beside औमम्; और्णकम् beside "
             "और्णम् — flax and wool"),
    Kala("4.3.159", of=("eṇī",), gives="ḍhañ", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava", excepts=("4.3.154",),
         why="एण्या ढञ्, प्राण्यञोऽपवादः. **ऐणेयं मांसम्** — the "
             "flesh of the doe. **पुंसस्त्वञेव भवति**: from the male "
             "it is the plain अञ्, एणस्य मांसम् **ऐणम्**. One affix "
             "for the female of a species and another for the male",
         keeps_out="ऐणम्"),
    Kala("4.3.160", of=("go", "payas"), gives="yat", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava",
         why="गोपयसोर्यत्. **गव्यम्**, पयस्यम् — and this is the rule "
             "4.3.145 named when it said dung was neither of these "
             "two senses.\n\n"
             "**सर्वत्र गोरजादिप्रसङ्गे यत् अस्त्येव, मयड्विषये तु "
             "विधीयते** — a vārttika on 4.1.85 gives यत् from गो "
             "wherever अज् and the rest would come; this rule is "
             "stated for the ground the मयट् would otherwise have had"),
    Kala("4.3.161", of=("dru",), gives="yat", case="ṣaṣṭhī",
         sense="vikāra", also_sense="avayava", excepts=("4.3.139",),
         why="द्रोश्च, ओरञोऽपवादः. **द्रव्यम्** — a thing, and the "
             "word for MATTER in the philosophies is made by asking "
             "what wood is turned into"),
    Kala("4.3.162", of=("dru",), gives="vayas", result="māna",
         case="ṣaṣṭhī", sense="vikāra", excepts=("4.3.161",),
         why="माने वयः, यतोऽपवादः. **द्रुवयम्** — a wooden measure, "
             "and माने is a particular kind of modification, so the "
             "condition is on what the result IS"),
    Kala("4.3.163", result="phala", case="ṣaṣṭhī", sense="vikāra",
         also_sense="avayava", elides=True,
         why="फले लुक्. **विकारावयवयोरुत्पन्नस्य फले तद्विशेषे "
             "विवक्षिते लुग् भवति** — where the FRUIT is what is "
             "meant, the affix given in these two senses goes. "
             "आमलक्याः फलम् **आमलकम्**; कुवलम्, बदरम्.\n\n"
             "**फलितस्य वृक्षस्य फलमवयवो भवति विकारश्च, पल्लवितस्येव "
             "पल्लवः** — a fruit is both a PART of the tree that "
             "bore it and a MODIFICATION of it, as a shoot is of what "
             "has shot. Which is why one rule can be stated of both "
             "senses at once"),
    Kala("4.3.164", gana="plakṣādi", gives="aṇ", result="phala",
         case="ṣaṣṭhī", sense="vikāra", also_sense="avayava",
         excepts=("4.3.154", "4.3.163"),
         why="प्लक्षादिभ्योऽण्, फल इत्येव; अञोऽपवादः. "
             "**विधानसामर्थ्यात् तस्य न लुग् भवति** — and the last "
             "rule's elision does not touch it, because a rule stated "
             "for a ground would achieve nothing if what it gave were "
             "removed at once. प्लाक्षम्, नैयग्रोधम्"),
    Kala("4.3.165", of=("jambū",), gives="aṇ", optional=True,
         result="phala", case="ṣaṣṭhī", sense="vikāra",
         excepts=("4.3.154",),
         why="जम्ब्वा वा, फल इत्येव; अञोऽपवादः. **अत्राणो "
             "विधानसामर्थ्याल् लुग् न भवति, अञस्तु भवत्येव** — the "
             "अण् this rule gives escapes 4.3.163's elision by the "
             "same argument, and the अञ् that comes on the other side "
             "of the option does not. **जाम्बवानि फलानि** beside "
             "**जम्बूनि**"),
    Kala("4.3.166", of=("jambū",), result="phala", case="ṣaṣṭhī",
         sense="vikāra", optional=True, elides=True, lup=True,
         why="लुप् च, वेत्येव. जम्ब्वाः फलं **जम्बूः फलम्**, जम्बु "
             "फलम्, जाम्बवमिति वा.\n\n"
             "**AND लुप् IS NOT लुक्. युक्तवद्भावे विशेषः** — under "
             "लुप् what is left agrees by 1.2.51 with the word the "
             "affix stood on, and the feminine ending is heard; "
             "under लुक् it is not. Two ways of taking an affix away "
             "that leave different words.\n\n"
             "A vārttika adds the grains: **लुप्प्रकरणे "
             "फलपाकशुषामुपसंख्यानम्** — व्रीहयः, यवाः, माषाः, "
             "मुद्गाः, तिलाः, plants that wither when their fruit "
             "ripens. And **पुष्पमूलेषु बहुलम्**: variously of "
             "flowers and roots — मल्लिकायाः पुष्पं मल्लिका, "
             "बिदार्या मूलं बिदारी; न च भवति पाटलानि पुष्पाणि"),
    Kala("4.3.167", gana="harītakyādi", result="phala", case="ṣaṣṭhī",
         sense="vikāra", elides=True, lup=True, excepts=("4.3.163",),
         why="हरीतक्यादिभ्यश्च, फले. हरीतक्याः फलं **हरीतकी**; "
             "कोशातकी, नखरजनी.\n\n"
             "**AND HERE THE DIFFERENCE BETWEEN THE TWO REMOVALS IS "
             "SPELT OUT.** लुकि प्राप्ते लुपो विधाने **युक्तवद्भावे "
             "स्त्रीप्रत्ययश्रवणे च विशेषः** — 4.3.163's लुक् was "
             "already available, and लुप् is enjoined instead because "
             "the two differ in 1.2.51's agreement and in whether the "
             "feminine affix is still heard.\n\n"
             "**अत्र च व्यक्तिर्युक्तवद्भावेनेष्यते, वचनं "
             "त्वभिधेयवदेव भवति** — the GENDER follows the word the "
             "affix stood on and the NUMBER follows what is denoted: "
             "हरीतक्याः फलानि **हरीतक्यः**, feminine because the tree "
             "is, plural because the fruits are"),
    Kala("4.3.168", of=("kaṃsīya", "paraśavya",), gives="yañ",
         also_gives=("añ",), case="ṣaṣṭhī", sense="vikāra",
         elides=True,
         why="कंसीयपरशव्ययोर्यञञौ लुक् च, यथासंख्यम्. The two bases "
             "are themselves derived — कंसीयः by 5.1.1 प्राक्क्रीताच् "
             "छः and परशव्यः by 5.1.2 उगवादिभ्यो यत् — and the affix "
             "that made each is removed in the same act that gives "
             "the new one. कंसीयस्य विकारः **कांस्यः**; परशव्यस्य "
             "**पारशवः**.\n\n"
             "**प्रातिपदिकाधिकाराद् धातुप्रत्ययस्य न लुग् भवति** — "
             "and the removal reaches a nominal affix only, since the "
             "heading is about प्रातिपदिक. "
             "**परशव्यशब्दादनुदात्तादित्वादेवाञि सिद्धे लुगर्थं "
             "वचनम्**: the अञ् was already coming to परशव्य by "
             "4.3.140, so the rule is spoken for the sake of the "
             "elision.\n\n"
             "And the vṛtti refuses an alternative derivation. ननु च "
             "यस्येति [6.4.148] इति लोपे कृते **हलस्तद्धितस्य** "
             "[6.4.150] इति यलोपो भविष्यति? **नैतदस्ति; ईतीति तत्र "
             "वर्तते** — that rule carries ईति from its own "
             "neighbourhood and so drops य only before ई. The pāda "
             "ends here: इति काशिकायां वृत्तौ चतुर्थाध्यायस्य "
             "तृतीयः पादः"),
)


@dataclass(frozen=True)
class BornIn:
    """The affix given in a time or a birthplace, and by which rule."""

    gives: str
    by: str
    why: str
    also_gives: Tuple[str, ...] = ()
    case: str = ""
    optional: bool = False
    #: True where the answer is that the affix GOES. 4.3.34–37.
    elided: bool = False
    #: True where the removal was लुप् rather than लुक् — so 1.2.51
    #: keeps the gender of the word the affix stood on.
    lopped: bool = False
    #: The rule that REFUSED, where a प्रतिषेध took the affix away
    #: and another rule answered instead. The standing decision at
    #: 2.3.72: a rule that excepts does not thereby govern, so the
    #: answer comes by the supplier and carries the refuser's id.
    blocked_by: str = ""
    replaces: str = ""
    augment: str = ""
    drops: str = ""
    excepts: Tuple[str, ...] = ()


def _reaches(row: Kala, stem: str, gana: str, sense: str, case: str,
             result: str, samjna: str, pre: str, stem_final: str,
             usage: str, before: str, vowels: str,
             accent: str, upadha: str, elided: bool) -> bool:
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.sense and sense and sense not in (row.sense, row.also_sense):
        return False
    if row.case and case and case != row.case:
        return False
    if row.result and result != row.result:
        return False
    if row.of_samjna and samjna != row.of_samjna:
        return False
    if row.pre and pre != row.pre:
        return False
    if row.stem_final and stem_final != row.stem_final:
        return False
    if row.usage and usage != row.usage:
        return False
    if row.upadha and upadha != row.upadha:
        return False
    if row.before and before != row.before:
        return False
    if row.vowels and vowels != row.vowels:
        return False
    if row.accent and accent != row.accent:
        return False
    if elided and not row.elides:
        # Asking after the form the affix has GONE from. 4.3.165
        # and 4.3.166 are stated of one word in one sense and
        # differ in nothing else, so only the question can tell
        # them apart. It filters and does not rank: a rule that
        # removes is not a narrower one that gives.
        return False
    return True


def _supplies(row: Kala, wants: str) -> bool:
    """
    Whether the row gives the affix asked for. A rule that gives
    several gives each of them: 4.3.1 answers for खञ्, छ and अण्
    alike, and asking after only the first would lose the other two.
    """
    return (not wants
            or wants == row.gives
            or wants in row.also_gives)


def _how_specific(row: Kala) -> int:
    """
    A named base is the narrowest thing these rules state; the sense
    and the case are the widest, since both are headings carried over
    whole stretches of the pāda.
    """
    return (
        6 * bool(row.of)
        + 5 * bool(row.of_samjna)
        + 4 * bool(row.gana)
        + 4 * bool(row.pre)
        + 3 * bool(row.result)
        + 3 * bool(row.before)
        + 2 * bool(row.stem_final)
        + 2 * bool(row.sense)
        + 1 * bool(row.case)
        + 3 * bool(row.vowels)
        + 3 * bool(row.accent)
        + 3 * bool(row.upadha)
        + 3 * bool(row.usage)
    )


def born_in(stem: str = "", *, gana: str = "", sense: str = "śeṣa",
            case: str = "", result: str = "", samjna: str = "",
            pre: str = "", stem_final: str = "", usage: str = "",
            before: str = "", vowels: str = "", accent: str = "",
            upadha: str = "", elided: bool = False,
            wants: str = "") -> BornIn:
    """
    4.3.1–30 — the affix given from a word of TIME, and then from a
    word of place in the sense *born there*.

    Where a rule names no affix the answer comes from elsewhere, and
    from two different elsewheres. 4.3.25 तत्र जातः says
    **यथाविहितम्**, *as already prescribed*, and this function asks
    `in_sense` for the शेष affix and reports what it gives. Anything
    else with no affix of its own is enjoining a SUBSTITUTE, and the
    answer says so instead.
    """
    matched = [
        row for row in KALA_TABLE
        if _reaches(row, stem, gana, sense, case, result, samjna,
                    pre, stem_final, usage, before, vowels, accent,
                    upadha, elided)
        and _supplies(row, wants)
    ]
    if not matched:
        from src.astadhyayi.sense_taddhita import in_sense

        fallen = in_sense(stem, gana=gana, sense=sense or "śeṣa",
                          result=result, samjna=samjna, pre=pre,
                          stem_final=stem_final, wants=wants)
        return BornIn(fallen.gives, fallen.by, fallen.why, case=case)
    row = max(matched, key=_how_specific)
    if row.borrows_from:
        # An अतिदेश takes over what another rule gives. Where that
        # rule is not codified yet the answer names it rather than
        # pretending to have its affixes — 4.3.80 points forward and
        # is in that state; 4.3.100 points back and is not.
        from src.astadhyayi.krita import (
            fit_for, provisions_for as _krita_rows)
        from src.astadhyayi.sense_taddhita import (
            in_sense, provisions_for as _in_sense_rows)
        from src.astadhyayi.sutra import REGISTRY

        if not REGISTRY.has(row.borrows_from):
            return BornIn("", row.sutra, row.why, case=row.case,
                          excepts=row.excepts)
        asked = {"gana": gana, "case": case, "sense": sense,
                 "samjna": samjna, "result": result, "wants": wants}
        asked.update(dict(row.borrow_query))
        if _in_sense_rows(row.borrows_from):
            lent = in_sense(stem, gana=asked["gana"], sense="śeṣa",
                            desa=True, samjna=asked["samjna"],
                            wants=asked["wants"])
        elif _krita_rows(row.borrows_from):
            # 4.3.156 alone, and the third destination this branch
            # has needed. Asking `born_in` for it would recurse
            # straight back into the row now asking, which is the
            # crash 4.3.80 produced the day ITS target arrived.
            got = fit_for(stem, gana=asked["gana"],
                          sense=asked["sense"], case=asked["case"],
                          samjna=asked["samjna"],
                          result=asked["result"], pre=pre,
                          wants=asked["wants"])
            lent = BornIn(got.affix, got.sutra, got.why,
                          case=got.case)
        else:
            lent = born_in(stem, gana=asked["gana"], case=asked["case"],
                           sense=asked["sense"], samjna=asked["samjna"],
                           result=asked["result"], wants=asked["wants"])
        return BornIn(
            lent.gives, row.sutra,
            row.why + "\n\nThe affix is borrowed from %s: %s"
            % (lent.by, lent.why), case=row.case)
    if row.replaces and not row.gives:
        # 4.3.2 and 4.3.3 give no affix at all. What they enjoin is
        # a substitute, and only in the presence of an affix another
        # rule gave: तस्मिन् खञि अणि च.
        return BornIn("", row.sutra, row.why, case=row.case,
                      replaces=row.replaces, excepts=row.excepts)
    if row.refuses:
        # 4.3.130 न दण्डमाणवान्तेवासिषु takes the वुञ् away where
        # 4.3.126 would have given it. गोत्रग्रहणमिहानुवर्तते, तेन
        # वुञ्प्रतिषेधो विज्ञायते — the refusal is of that affix and
        # of nothing else, so the answer names the rule it refuses.
        supplying = [other for other in matched
                     if not other.refuses and other.gives]
        if supplying:
            beaten = max(supplying, key=_how_specific)
            return BornIn("", beaten.sutra, row.why, case=row.case,
                          blocked_by=row.sutra,
                          excepts=(row.sutra,))
        return BornIn("", row.sutra, row.why, case=row.case)
    if row.elides:
        # 4.3.34–37 take the affix away. What is elided is whatever
        # the earlier rules gave, so the answer names no affix and
        # says by which rule it went.
        return BornIn("", row.sutra, row.why, case=row.case,
                      optional=row.optional, elided=True,
                      lopped=row.lup, excepts=row.excepts)
    if not row.gives:
        # 4.3.25 तत्र जातः names a case and a sense and no affix,
        # because **यथाविहितम्** — whichever affix was already
        # prescribed. The शेष rules of 4.2 are what prescribed them,
        # so the answer is theirs and this rule reports it.
        from src.astadhyayi.sense_taddhita import in_sense

        prescribed = in_sense(stem, gana=gana, sense="śeṣa",
                              result=result, samjna=samjna, pre=pre,
                              stem_final=stem_final, wants=wants)
        return BornIn(
            prescribed.gives, row.sutra,
            row.why + "\n\nThe affix is यथाविहितम्, whichever was "
            "already prescribed — here " + prescribed.by + ": "
            + prescribed.why,
            case=row.case, optional=row.optional)
    return BornIn(row.gives, row.sutra, row.why,
                  also_gives=row.also_gives, case=row.case,
                  optional=row.optional, replaces=row.replaces,
                  augment=row.augment, drops=row.drops,
                  excepts=row.excepts)


def kala_run(nth: int = 1) -> BornIn:
    """
    How far काल carries, and it carries twice.

    The FIRST range is bounded in advance by the rule that opens it:
    4.3.11's vṛtti says **तत्र जातः इति प्रागतः कालाधिकारः**, so it
    stops before 4.3.25 and 4.3.24 is the last rule inside.

    The SECOND begins where 4.3.43 कालात् names the word again, and
    is closed from behind: 4.3.53's vṛtti opens **कालादिति
    निवृत्तम्**, so 4.3.52 is the last rule inside that one.

    Ranges nine and ten in two pādas with both ends written down —
    and between them they use both ways of stating an end, on the
    same word, forty sūtras apart.
    """
    opens, closes = KALA_RUNS[nth - 1]
    said = ("its opening rule names where it stops — **तत्र जातः इति "
            "प्रागतः कालाधिकारः**" if nth == 1 else
            "the rule AFTER it records that it is over — **कालादिति "
            "निवृत्तम्**, said by 4.3.53")
    return BornIn(
        "", opens,
        "काल carries from %s to %s, and %s" % (opens, closes, said))


def desa_lapsed() -> BornIn:
    """
    4.3.1's first words: **देशाधिकारो निवृत्तः**.

    The country-heading entered at 4.2.119 and ran to the end of that
    pāda, and the vṛtti on the first rule of this one records that it
    has stopped before it says anything else about the rule. A range
    whose closing is stated from OUTSIDE it, by the text that comes
    after — which is a different kind of evidence from a vṛtti saying
    where its own heading will end.
    """
    from src.astadhyayi.sense_taddhita import DESA_RUN

    return BornIn(
        "", "4.3.1",
        "**देशाधिकारो निवृत्तः** — the देश heading, which ran from "
        "%s to %s, has lapsed. 4.2.119's vṛtti said where it began "
        "and 4.3.1's says that it is over" % DESA_RUN)


def provisions_for(sutra_id: str) -> Tuple[Kala, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in KALA_TABLE if row.sutra == sutra_id)
