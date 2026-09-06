# -*- coding: utf-8 -*-
"""
७.३.१–३१ — the taddhita vṛddhi qualified, and the second member.

पाद ७.२ ended by giving the FIRST vowel of a stem vṛddhi before
a taddhita. This pāda opens by qualifying that in nine sūtras
and then moves the operation to the second member of a compound
for twenty-two more.

**THE FIRST NINE ARE ALL ABOUT ONE RULE.** देविका and four
others take a plain आ where the vṛddhi was due (दाविकम्); केकय,
मित्रयु and प्रलय turn their य into इय (कैकेयः, प्रालेयम्); and
a stem beginning य् or व् at the end of a word takes NO vṛddhi
but gets an ऐ or औ put in FRONT instead — वैयाकरणः, सौवश्वः.
Then four sūtras take even that back, for reciprocal action
(व्यावक्रोशी), for स्वागत and its like, and for श्वन् before इञ्.

**AND THEN उत्तरपदस्य GOVERNS FOR TWENTY-TWO SŪTRAS.** 7.3.10's
vṛtti says how far: **उत्तरपदस्येत्ययम् अधिकारः, हनस्तोऽचिण्णलोः
इति प्रागेतस्मात्** — to 7.3.31. Inside it the vṛddhi falls on
the SECOND member of a compound and not the first: पूर्ववार्षिकम्,
सुपाञ्चालकः, द्विसांवत्सरिकः, प्रोष्ठपादः. And from 7.3.19 six
rules give it to BOTH members at once — सौहार्दम्, सौभाग्यम्,
आनुशातिकम्, आग्निमारुतम्.

**AND ONE REFUSAL IS READ AS PROOF ABOUT THE ORDER OF THE WHOLE
GRAMMAR.** 7.3.22 refuses the vṛddhi to a following इन्द्र —
सौमेन्द्रः — and the vṛtti points out that the vṛddhi could not
have applied anyway, the इ having been lost first. That the
refusal is stated at all shows the operations on the two members
are done BEFORE the vowels merge: **बहिरङ्गम् अपि पूर्वोत्तरपदयोः
पूर्वं कार्यं भवति पश्चाद् एकादेशः**.

**WHAT THIS MODULE DOES NOT DO.** It says where the vṛddhi falls
and where it does not. Which sound the strengthened vowel is
comes from 1.1.1, and the taddhita itself from अध्याय ४ and ५.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
VRDDHI_RUN: Tuple[str, str] = ("7.3.1", "7.3.31")

#: Where उत्तरपदस्य starts governing, and where the vṛtti says
#: it stops — **हनस्तोऽचिण्णलोः इति प्रागेतस्मात्**.
UTTARAPADA_FROM: str = "7.3.10"
UTTARAPADA_TO: str = "7.3.31"

#: 7.3.1's five, which take a plain आ instead.
DEVIKADI: Tuple[str, ...] = (
    "devikā", "śiṃśapā", "dityavāh", "dīrghasatra", "śreyas")

#: 7.3.2's three, whose य becomes इय.
KEKAYADI: Tuple[str, ...] = ("kekaya", "mitrayu", "pralaya")

#: 7.3.7's seven, which keep the vṛddhi 7.3.3 and 7.3.4 refused.
SVAGATADI: Tuple[str, ...] = (
    "svāgata", "svadhvara", "svaṅga", "vyaṅga", "vyaḍa",
    "vyavahāra", "svapati")

#: 7.3.19's three word-endings, where BOTH members strengthen.
HRD_BHAGA_SINDHU: Tuple[str, ...] = ("hṛd", "bhaga", "sindhu")

#: 7.3.25's three, where the second member's vṛddhi is optional.
JANGALADI: Tuple[str, ...] = ("jaṅgala", "dhenu", "valaja")

#: 7.3.30's five after नञ्, where the FIRST member's is optional.
SUCI_FIVE: Tuple[str, ...] = (
    "śuci", "īśvara", "kṣetrajña", "kuśala", "nipuṇa")

#: What 7.3.22's refusal is read as proving about rule order.
BAHIRANGA: str = (
    "बहिरङ्गम् अपि पूर्वोत्तरपदयोः पूर्वं कार्यं भवति "
    "पश्चाद् एकादेशः")


@dataclass(frozen=True)
class Vrddhi:
    """One rule of 7.3.1–31: where the taddhita's vṛddhi falls."""

    sutra: str
    #: `vṛddhi`, `āt`, `iy`, `aic` — or "" where it is refused.
    does: str = "vṛddhi"
    #: Which member the operation falls on.
    where: str = "uttarapada"
    #: The stems named outright.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: What the first member must be.
    purvapada: str = ""
    #: What the second member must be.
    uttarapada: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow, or what sense is shut out.
    excludes: Tuple[str, ...] = ()
    #: The sense the rule wants.
    sense: str = ""
    refuses: bool = False
    optional: bool = False
    #: True where the FIRST member's vṛddhi is the optional half.
    purva_optional: bool = False
    heading: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


VRDDHI_TABLE: Tuple[Vrddhi, ...] = (
    Vrddhi(
        "7.3.1", does="āt", where="acām-ādi", of=DEVIKADI,
        before=("ñit", "ṇit", "kit"), blocks=("7.2.117",),
        why="देविकाशिंशपादित्यवाड्दीर्घसत्रश्रेयसामात् — five "
            "stems take a plain आ where the first vowel's vṛddhi "
            "was due: **दाविकम् उदकम्; शांशपश्चमसः; "
            "दीर्घसात्रम्**. And it reaches the uttarapada "
            "vṛddhi of 7.3.14 as well — **पूर्वदाविकः**, where "
            "**प्राचां ग्रामनगराणाम् इत्युत्तरपदवृद्धिः, "
            "साप्याकार एव भवति**"),
    Vrddhi(
        "7.3.2", does="iy", where="ya-ādi", of=KEKAYADI,
        before=("ñit", "ṇit", "kit"), blocks=("7.2.117",),
        why="केकयमित्त्रययुप्रलयानां यादेरियः — and three stems "
            "turn their य into इय: **कैकेयः** from 4.1.168's "
            "अञ्; **मैत्रेयिकया श्लाघते** from 5.1.134's वुञ्; "
            "**प्रालेयम् उदकम्**"),
    Vrddhi(
        "7.3.3", refuses=True, does="aic", where="pūrva-āgama",
        gana="y-v-pada-anta-pūrva", before=("ñit", "ṇit", "kit"),
        blocks=("7.2.117",),
        keeps_out="न्रार्थिः — no य् or व्; याष्टीकः, यातः — the "
                  "य् is not at a word's end",
        why="न य्वाभ्यां पदान्ताभ्याम् पूर्वौ तु ताभ्यामैच् — a "
            "stem whose first vowel stands after a word-final य् "
            "or व् takes NO vṛddhi, and an ऐ or औ is put in "
            "FRONT of that य् or व् instead: **वैयसनम्, "
            "वैयाकरणः** for the य्; **सौवश्वः** for the व्.\\n\\n"
            "**AND THE REFUSAL IS STATED TO FIX WHERE THE "
            "AUGMENT GOES.** **प्रतिषेधवचनम् ऐचोर् "
            "विषयप्रक्ऌप्त्यर्थम्, इह मा भूत् — दाध्यश्विः, "
            "माध्वश्विः** — there the य् and व् are not what "
            "the first vowel follows, and no augment comes"),
    Vrddhi(
        "7.3.4", refuses=True, does="aic", where="pūrva-āgama",
        gana="dvāra-ādi", before=("ñit", "ṇit", "kit"),
        blocks=("7.2.117",),
        why="द्वारादीनां च — and the द्वारादि stems: "
            "**दौवारिकः, दौवारपालम्; सौवरः; वैयल्कशः; "
            "सौवस्तिकः; सौवः**. The rule reaches a compound "
            "BEGINNING with one of them — **तदादिविधिश्चात्र "
            "भवति** — and the vṛtti rejects one reading of the "
            "list outright: **स्वाध्याय इति केचित् पठन्ति, तद् "
            "अनर्थकम्**"),
    Vrddhi(
        "7.3.5", refuses=True, does="aic", where="pūrva-āgama",
        of=("nyagrodha",), before=("ñit", "ṇit", "kit"),
        excludes=("samāsa",), blocks=("7.2.117",),
        keeps_out="न्याग्रोधमूलाः शालयः — न्यग्रोध is not alone, "
                  "and the rule wants it केवल",
        why="न्यग्रोधस्य च केवलस्य — and न्यग्रोध ALONE: "
            "**नैयग्रोधश्चमसः**. Whether the sūtra restricts or "
            "provides depends on how the word is derived — "
            "**न्यग्रोहतीति न्यग्रोध इति व्युत्पत्तिपक्षे "
            "नियमार्थम्, अव्युत्पत्तिपक्षे विध्यर्थम्**"),
    Vrddhi(
        "7.3.6", refuses=True, does="", where="none",
        sense="karma-vyatihāra", before=("ñit", "ṇit", "kit"),
        blocks=("7.3.3", "7.3.4"),
        why="न कर्मव्यतिहारे — but where RECIPROCAL action is "
            "meant, neither the refusal nor the augment holds: "
            "**व्यावक्रोशी, व्यावलेखी, व्यावचर्ची, व्यावहासी "
            "वर्तते**. **प्रतिषेधागमयोर् अयं प्रतिषेधः** — one "
            "refusal cancelling two things at once, and the "
            "ordinary vṛddhi comes back"),
    Vrddhi(
        "7.3.7", refuses=True, does="", where="none",
        of=SVAGATADI, before=("ñit", "ṇit", "kit"),
        blocks=("7.3.3", "7.3.4"),
        why="स्वागतादीनां च — and seven stems likewise: "
            "**स्वागतिकः, स्वाध्वरिकः, स्वाङ्गिः, व्याङ्गिः, "
            "व्याडिः, व्यावहारिकः, स्वापतेयः**. व्यवहार is "
            "named although 7.3.6 would seem to reach it, "
            "because **व्यवहारशब्दोऽयं लौकिके वृत्ते वर्तते, न "
            "तु कर्मव्यतिहारे**; and स्वपति is named because "
            "**द्वारादिषु स्वशब्दपाठाद् अत्र प्राप्तिः**"),
    Vrddhi(
        "7.3.8", refuses=True, does="", where="none",
        gana="śvan-ādi", before=("iñ",), blocks=("7.3.4",),
        why="श्वादेरिञि — and a stem beginning श्वन् before इञ्: "
            "**श्वाभस्त्रिः, श्वादंष्ट्रिः**. That श्वन् is in "
            "the द्वारादि list and the compound-initial reading "
            "is available there is what this sūtra proves — "
            "**तत्र च तदादिविधिर् भवतीत्येतद् एव वचनं "
            "ज्ञापकम्**. A vārttika widens इञ् to every "
            "इ-initial affix: **श्वागणिकः, श्वायूथिकः**"),
    Vrddhi(
        "7.3.9", refuses=True, does="", where="none",
        gana="śvan-ādi", uttarapada="pada", optional=True,
        blocks=("7.3.8",),
        why="पदान्तस्यान्यतरस्याम् — and OPTIONALLY where such a "
            "stem ends in पद: **श्वापदम्, शौवापदम्**. The "
            "sūtra before had refused the vṛddhi outright "
            "before इञ्; here the refusal is only half, so both "
            "forms stand and the language keeps the shorter"),
    Vrddhi(
        "7.3.10", heading=True, does="", where="uttarapada",
        why="उत्तरपदस्य — a heading: **उत्तरपदस्येत्ययम् "
            "अधिकारः, हनस्तोऽचिण्णलोः इति प्रागेतस्मात्** — "
            "from here to 7.3.31 the vṛddhi falls on the SECOND "
            "member of a compound.\\n\\n"
            "**AND IT IS THERE FOR THREE REASONS AT ONCE.** Some "
            "rules of the run have no ablative to read the "
            "second member out of — **जे प्रोष्ठपदानाम्** is "
            "one; where there is one the heading is "
            "**विस्पष्टार्थम्**; and it lets 6.2.105's "
            "**उत्तरपदवृद्धौ सर्वं च** name this stretch's "
            "vṛddhi as a thing with a name"),
    Vrddhi(
        "7.3.11", uttarapada="ṛtu", purvapada="avayava",
        before=("ñit", "ṇit", "kit"),
        keeps_out="पौर्ववार्षिकम् — the first member is not a "
                  "PART of the season but the whole of it in "
                  "another compound",
        why="अवयवादृतोः — a season-word as second member takes "
            "the vṛddhi after a word for a PART of it: "
            "**पूर्ववार्षिकम्, पूर्वहैमनम्, अपरवार्षिकम्, "
            "अपरहैमनम्**. The compound is 2.2.1's एकदेशिसमास "
            "and the affix 4.3.18's ठक्, and the rule reaches a "
            "compound ENDING in a season — **ऋतोर् वृद्धिमद्"
            "विधाव् अवयवानाम् इति तदन्तविधिः**"),
    Vrddhi(
        "7.3.12", uttarapada="janapada",
        purvapada="su-sarva-ardha", before=("ñit", "ṇit", "kit"),
        why="सुसर्वार्धाज्जनपदस्य — a country-name as second "
            "member takes it after सु, सर्व and अर्ध: "
            "**सुपाञ्चालकः, सर्वपाञ्चालकः, अर्धपाञ्चालकः**. The "
            "affix is 4.2.124's वुञ्, and a vārttika adds the "
            "direction-words to the three: "
            "**सुसर्वार्धदिक्शब्देभ्यो जनपदस्य**"),
    Vrddhi(
        "7.3.13", uttarapada="janapada", purvapada="diś",
        excludes=("madra",), before=("ñit", "ṇit", "kit"),
        keeps_out="पौर्वपञ्चालकः — the first member is not a "
                  "direction in that compound; पौर्वमद्रः — "
                  "मद्र, named out",
        why="दिशोऽमद्राणाम् — and after a DIRECTION-word, मद्र "
            "excepted: **पूर्वपाञ्चालकः, अपरपाञ्चालकः, "
            "दक्षिणपाञ्चालकः**"),
    Vrddhi(
        "7.3.14", uttarapada="grāma-nagara", purvapada="diś",
        sense="prācām", before=("ñit", "ṇit", "kit"),
        why="प्राचां ग्रामनगराणाम् — and a village or a town of "
            "the EASTERN country after a direction-word: "
            "**पूर्वैषुकामशमः, पूर्वकार्ष्णमृत्तिकः** for the "
            "villages; **पूर्वपाटलिपुत्रकः, पूर्वकान्यकुब्जः** "
            "for the towns. A town is a village for grammar's "
            "purposes and both are named all the same, "
            "**संबन्धभेदप्रतिपत्त्यर्थम्** — to show which of "
            "the two relations the compound expresses"),
    Vrddhi(
        "7.3.15", uttarapada="saṃvatsara-saṃkhyā",
        purvapada="saṃkhyā", before=("ñit", "ṇit", "kit"),
        why="संख्यायाः संवत्सरसंख्यस्य च — and संवत्सर, or "
            "another numeral, after a numeral: "
            "**द्विसांवत्सरिकः; द्विषाष्टिकः, द्विसाप्ततिकः**. "
            "7.3.17 would have covered संवत्सर, and naming it "
            "here is **परिमाणग्रहणे कालपरिमाणस्याग्रहणार्थम्** "
            "— so that *measure* in that sūtra shall not mean a "
            "measure of time"),
    Vrddhi(
        "7.3.16", uttarapada="varṣa", purvapada="saṃkhyā",
        excludes=("bhaviṣyat",), before=("ñit", "ṇit", "kit"),
        keeps_out="त्रैवर्षिकं धान्यम् — grain for three years to "
                  "come, where the taddhita's own sense is future",
        why="वर्षस्याभविष्यति — and वर्ष after a numeral, where "
            "the taddhita is NOT in a future sense: "
            "**द्विवार्षिकः, त्रिवार्षिकः**. And the exception "
            "is narrower than it looks — **अधीष्टभृतयोर् "
            "अभविष्यतीति प्रतिषेधो न भवति। गम्यते हि तत्र "
            "भविष्यत्ता, न तु तद्धितार्थः**, a future merely "
            "understood is not the affix's own sense"),
    Vrddhi(
        "7.3.17", uttarapada="parimāṇa", purvapada="saṃkhyā",
        excludes=("saṃjñā", "śāṇa"), before=("ñit", "ṇit", "kit"),
        why="परिमाणान्तस्यासंज्ञाशाणयोः — and a measure-word "
            "after a numeral, where it is neither a NAME nor "
            "शाण: **द्विकौडविकः, द्विसौवर्णिकम्, "
            "द्विनैष्किकम्**"),
    Vrddhi(
        "7.3.18", uttarapada="proṣṭhapadā", sense="jāta",
        before=("ñit", "ṇit", "kit"),
        keeps_out="प्रौष्ठपदो मेघः — born under the stars is one "
                  "thing, occurring in that month another",
        why="जे प्रोष्ठपदानाम् — प्रोष्ठपदा as second member "
            "takes it where BIRTH is meant: **प्रोष्ठपादो "
            "माणवकः**. This is the sūtra 7.3.10's heading was "
            "needed for, there being no ablative to read the "
            "second member out of. And the plural is why the "
            "synonym counts too — **पर्यायोऽपि गृह्यते, "
            "भद्रपाद इति**"),
    Vrddhi(
        "7.3.19", where="both", gana="hṛd-bhaga-sindhu-anta",
        before=("ñit", "ṇit", "kit"),
        why="हृद्भगसिन्ध्वन्ते पूर्वपदस्य च — where the compound "
            "ends in हृद्, भग or सिन्धु, BOTH members take the "
            "vṛddhi: **सौहार्दम्, सौहार्द्यम्; सौभाग्यम्, "
            "दौर्भाग्यम्; सौभागिनेयः, दौर्भागिनेयः**. Six rules "
            "from here do the same, and the Veda is let off: "
            "**महते सौभगाय — छन्दसि सर्वविधीनां "
            "विकल्पितत्वात्**"),
    Vrddhi(
        "7.3.20", where="both", gana="anuśatika-ādi",
        before=("ñit", "ṇit", "kit"),
        why="अनुशतिकादीनां च — and the अनुशतिकादि stems: "
            "**आनुशातिकम्, आनुहौडिकः, आनुसांवरणम्, "
            "आनुसांवत्सरिकः, आङ्गारवैणवः, आसिहात्यम्**. The "
            "list's own readings are disputed — **अस्यहत्य इति "
            "केचित् पठन्ति... अस्यहेतिर् इत्येवमपरे पठन्ति** — "
            "and the vṛtti records the variants rather than "
            "choosing"),
    Vrddhi(
        "7.3.21", where="both", gana="devatā-dvandva",
        before=("ñit", "ṇit", "kit"),
        keeps_out="स्कान्दविशाखः, ब्राह्मप्रजापत्यम् — a "
                  "देवताद्वन्द्व not belonging to a hymn or an "
                  "oblation",
        why="देवताद्वंद्वे च — and a द्वन्द्व of deities: "
            "**आग्निमारुतीं पृश्निम् आलभेत; आग्निमारुतं कर्म**. "
            "But only one that belongs to a hymn or an oblation "
            "— **यो देवताद्वन्द्वः सूक्तहविःसंबन्धी, तत्रायं "
            "विधिः**"),
    Vrddhi(
        "7.3.22", refuses=True, does="", where="none",
        uttarapada="indra", before=("ñit", "ṇit", "kit"),
        blocks=("7.3.21",),
        keeps_out="ऐन्द्राग्नम् — इन्द्र is the FIRST member and "
                  "takes the vṛddhi like any other",
        why="नेन्द्रस्य परस्य — but a FOLLOWING इन्द्र does not "
            "take it: **सौमेन्द्रः, आग्नेन्द्रः**.\\n\\n"
            "**AND THE REFUSAL IS READ AS PROOF ABOUT THE ORDER "
            "OF THE WHOLE GRAMMAR.** इन्द्र has two vowels; "
            "6.4.148 takes the first away before the taddhita "
            "and the rest merges with what precedes, so no "
            "vṛddhi could have applied and the refusal is idle "
            "as it stands. **तदेदं प्रतिषेधवचनं ज्ञापकम् — "
            "बहिरङ्गम् अपि पूर्वोत्तरपदयोः पूर्वं कार्यं भवति "
            "पश्चाद् एकादेशः** — the two members' own operations "
            "are done first and the merger after, which is what "
            "makes पूर्वैषुकामशमः come out at all"),
    Vrddhi(
        "7.3.23", refuses=True, does="", where="none",
        uttarapada="varuṇa", purvapada="dīrgha-anta",
        before=("ñit", "ṇit", "kit"), blocks=("7.3.21",),
        keeps_out="आग्निवारुणीम् अनड्वाहीम् आलभेत — the first "
                  "member does not end long, 6.3.28 having "
                  "refused the आ",
        why="दीर्घाच्च वरुणस्य — and वरुण after a member ending "
            "in a LONG vowel: **ऐन्द्रावरुणम्, मैत्रावरुणम्**"),
    Vrddhi(
        "7.3.24", where="both", uttarapada="nagara-anta",
        sense="prācām", before=("ñit", "ṇit", "kit"),
        keeps_out="माद्रनगरः — मद्रनगर is in the north and not "
                  "the east",
        why="प्राचां नगरान्ते — and where an EASTERN compound "
            "ends in नगर, both members take it: **सौह्मनागरः, "
            "पौण्ड्रनागरः**"),
    Vrddhi(
        "7.3.25", where="pūrva", gana="jaṅgala-dhenu-valaja-anta",
        before=("ñit", "ṇit", "kit"), optional=True,
        why="जङ्गलधेनुवलजान्तस्य विभाषितमुत्तरम् — where the "
            "compound ends in जङ्गल, धेनु or वलज, the FIRST "
            "member takes the vṛddhi and the second takes it "
            "OPTIONALLY: **कौरुजङ्गलम्, कौरुजाङ्गलम्; "
            "वैश्वधेनवम्, वैश्वधैनवम्; सौवर्णवलजः, "
            "सौवर्णवालजः**"),
    Vrddhi(
        "7.3.26", uttarapada="parimāṇa", purvapada="ardha",
        before=("ñit", "ṇit", "kit"), purva_optional=True,
        keeps_out="आर्धक्रोशिकम् — क्रोश is a distance and not a "
                  "measure of the kind meant",
        why="अर्धात् परिमाणस्य पूर्वस्य तु वा — a measure-word "
            "after अर्ध takes it, and अर्ध itself OPTIONALLY: "
            "**आर्धद्रौणिकम्, अर्धद्रौणिकम्; आर्धकौडविकम्, "
            "अर्धकौडविकम्**"),
    Vrddhi(
        "7.3.27", refuses=True, does="", where="none",
        uttarapada="a-parimāṇa", purvapada="ardha",
        before=("ñit", "ṇit", "kit"), purva_optional=True,
        blocks=("7.3.26",),
        keeps_out="आर्धकौडविकः — कुडव does not begin with a "
                  "short अ; अर्धखारी — the आ is long, and the "
                  "तपर shuts it out",
        why="नातः परस्य — but a measure BEGINNING with a short अ "
            "does not take it after अर्ध, and अर्ध still takes "
            "its own optionally: **अर्धप्रस्थिकः, आर्धप्रस्थिकः; "
            "अर्धकंसिकः, आर्धकंसिकः**.\\n\\n"
            "**AND THE तपर IS THERE FOR A RULE FOUR PĀDAS "
            "BACK.** Refuse the vṛddhi to अर्धखारी and 6.3.39's "
            "**वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे** would "
            "no longer see the taddhita as a vṛddhi-cause, and "
            "the पुंवद्भाव it refuses would come through in "
            "अर्धखारीभार्यः"),
    Vrddhi(
        "7.3.28", of=("pravāhaṇa",), before=("ḍha",),
        purva_optional=True,
        why="प्रवाहणस्य ढे — प्रवाहण's second member takes it "
            "before ढ, and its first optionally: "
            "**प्रावाहणेयः, प्रवाहणेयः**. The ढक् is 4.1.123's"),
    Vrddhi(
        "7.3.29", of=("pravāhaṇeya",), before=("taddhita",),
        purva_optional=True,
        why="तत्प्रत्ययस्य च — and the same word WITH its ढक् "
            "already on it, before a further taddhita: "
            "**प्रावाहणेयिः, प्रवाहणेयिः; प्रावाहणेयकम्, "
            "प्रवाहणेयकम्**. The sūtra exists because the outer "
            "taddhita's vṛddhi could not be made optional by "
            "appealing to the ढ — **बाह्यतद्धितनिमित्ता "
            "वृद्धिर् ढाश्रयेण विकल्पेन बाधितुम् अशक्येति "
            "सूत्रारम्भः**"),
    Vrddhi(
        "7.3.30", of=SUCI_FIVE, purvapada="nañ",
        before=("ñit", "ṇit", "kit"), purva_optional=True,
        why="नञः शुचीश्वरक्षेत्रज्ञकुशलनिपुणानाम् — five stems "
            "after नञ् take it, and the नञ् optionally: "
            "**अशौचम्, आशौचम्; अनैश्वर्यम्, आनैश्वर्यम्; "
            "अक्षैत्रज्ञ्यम्, आक्षैत्रज्ञ्यम्; अकौशलम्, "
            "आकौशलम्; अनैपुणम्, आनैपुणम्**. Some read the "
            "first member's vṛddhi as one that would never have "
            "come at all, 5.1.121 refusing the abstract affix "
            "after a नञ्-compound in the first place"),
    Vrddhi(
        "7.3.31", of=("yathātatha", "yathāpura"), purvapada="nañ",
        before=("ñit", "ṇit", "kit"), optional=True,
        blocks=("7.3.30",),
        why="यथातथयथापुरयोः पर्यायेण — and two more take it "
            "BY TURNS with the नञ्, one or the other and never "
            "both: **आयथातथ्यम्, अयाथातथ्यम्; आयथापुर्यम्, "
            "अयाथापुर्यम्**.\\n\\n"
            "**AND THE WORDS ARE READ AS TWO DIFFERENT "
            "COMPOUNDS IN TWO PLACES.** In 5.1.124's ब्राह्मणादि "
            "list they are नञ्-compounds; in this sūtra they are "
            "अव्ययीभाव compounds by 2.1.7, **तथा नपुंसकाश्रयं "
            "ह्रस्वत्वं कृतम्**. The Bhāṣya reads them a third "
            "way, as 2.1.4's सुप्सुपा. This closes the "
            "उत्तरपद heading"),
)


def _reaches(row: Vrddhi, stem: str, gana: str, purvapada: str,
             uttarapada: str, before: str, sense: str) -> bool:
    if row.heading:
        return False
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.purvapada and purvapada != row.purvapada:
        return False
    if row.uttarapada and uttarapada != row.uttarapada:
        return False
    if row.before and before not in row.before:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.excludes and (uttarapada in row.excludes
                         or sense in row.excludes):
        return False
    return True


def _how_specific(row: Vrddhi, stem: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, a named
    stem beats a named class, and a named second member beats a
    named first.

    7.3.3 to 7.3.9 are the stretch that needs all of it: one
    refusal with an augment attached, and four sūtras that take
    the refusal and the augment away together.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of and stem in row.of)
        + 6 * bool(row.uttarapada)
        + 5 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.purvapada)
        + 4 * bool(row.sense)
        + 2 * bool(row.before)
    )


@dataclass(frozen=True)
class Strengthened:
    """What the run answers: the operation, and where it falls."""

    does: str
    where: str
    sutra: str
    why: str
    optional: bool = False
    purva_optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def uttarapada_vrddhi(stem: str = "", *, gana: str = "",
                      purvapada: str = "", uttarapada: str = "",
                      before: str = "", sense: str = ""
                      ) -> Strengthened:
    """
    7.3.1–31 — where the taddhita's vṛddhi falls, and where not.

    Nothing answers by default, and the default is not *no
    vṛddhi*: 7.2.117 has already given it to the first vowel, and
    this run is the list of places where that is qualified.
    """
    matched = [
        row for row in VRDDHI_TABLE
        if _reaches(row, stem, gana, purvapada, uttarapada,
                    before, sense)
    ]
    if not matched:
        return Strengthened(
            "", "", "", "No rule of 7.3.1-31 is reached, so "
                        "7.2.117 stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Strengthened(row.does, row.where, row.sutra, row.why,
                        optional=row.optional,
                        purva_optional=row.purva_optional,
                        blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Vrddhi, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in VRDDHI_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Vrddhi", "VRDDHI_TABLE", "VRDDHI_RUN", "UTTARAPADA_FROM",
    "UTTARAPADA_TO", "DEVIKADI", "KEKAYADI", "SVAGATADI",
    "HRD_BHAGA_SINDHU", "JANGALADI", "SUCI_FIVE", "BAHIRANGA",
    "Strengthened", "uttarapada_vrddhi", "provisions_for",
]
