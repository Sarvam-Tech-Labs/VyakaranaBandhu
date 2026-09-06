# -*- coding: utf-8 -*-
"""
६.३.४६–६० — the first member replaced before a second.

Fifteen rules, five stems, one shape apiece. महत् becomes महा,
द्वि and अष्टन् become द्वा and अष्टा, त्रि becomes त्रयस्, हृदय
becomes हृद्, पाद becomes पद्, and उदक becomes उद. महाराजः,
द्वादश, त्रयोदश, हृल्लेखः, पदातिः, उदधिः.

**AND ALMOST EVERY ONE OF THEM IS FENCED BY ITS ENVIRONMENT AND NOT
BY ITS MEANING.** 6.3.46 wants the second member to be in
apposition, so महत्पुत्रः keeps महत्; 6.3.47 wants a numeral and
not a बहुव्रीहि and not अशीति, so द्वित्राः and द्व्यशीतिः keep
द्वि; 6.3.50 wants लेख, and the vṛtti pins down which लेख —
**लेख इत्यणन्तस्य ग्रहणम् इष्यते। घञि तु हृदयस्य लेखो
हृदयलेखः**.

**AND THAT ONE OBSERVATION SETTLES A PARIBHĀṢĀ FOR THE WHOLE
PĀDA.** **एतदेव लेखग्रहणं ज्ञापकम् उत्तरपदाधिकारे प्रत्ययग्रहणे
तदन्ताग्रहणस्य** — if naming an affix under the उत्तरपद heading
reached everything ending in it, 6.3.50 would not have needed to
say लेख at all. So it does not, and 6.3.17's vṛtti had already
leaned on the same fact.

**AND ONE BOUND IS SUPPLIED ENTIRELY BY A VĀRTTIKA.** 6.3.47–49
say nothing about how large a numeral may be, and द्विशतम् and
अष्टसहस्रम् show they must stop somewhere: **प्राक् शतादिति
वक्तव्यम्**.

**WHAT THIS MODULE DOES NOT DO.** It reports the substitute and
the rule. It does not build the word: that पदोपहतः is then
end-accented by निपातन rather than by 6.2.48, and that उदपेषम्
carries a णमुल् from 3.4.38, are other rules' business.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these fifteen stand, between the पुंवद्भाव run and the
#: shortening of 6.3.61.
ADESA_RUN: Tuple[str, str] = ("6.3.46", "6.3.60")

#: The bound a vārttika supplies for 6.3.47–49, which none of the
#: three states: **प्राक् शतादिति वक्तव्यम्** — below a hundred.
PRAK_SATAT: str = "prāk śatāt"

#: What 6.3.52 names, and what 6.3.53–56 add to it.
PADA_BEFORE: Tuple[str, ...] = ("āji", "āti", "ga", "upahata")

#: 6.3.60's ten, before which उदक becomes उद optionally.
UDA_TEN: Tuple[str, ...] = (
    "mantha", "odana", "saktu", "bindu", "vajra", "bhāra", "hāra",
    "vīvadha", "gāha")

#: The four before which 6.3.58 makes it compulsory.
UDA_FOUR: Tuple[str, ...] = ("peṣam", "vāsa", "vāhana", "dhi")


@dataclass(frozen=True)
class Adesa:
    """One rule of 6.3.46–60: the first member's substitute."""

    sutra: str
    #: The substitute — mahā, dvā, aṣṭā, trayas, hṛd, pad, uda.
    becomes: str = ""
    #: The first members the rule names.
    of: Tuple[str, ...] = ()
    #: What must FOLLOW — a word, an affix, or a class.
    before: Tuple[str, ...] = ()
    #: A named class of second member instead — संख्या, and
    #: चत्वारिंशत्प्रभृति, *from forty upward*.
    uttarapada_gana: str = ""
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ADESA_TABLE: Tuple[Adesa, ...] = (
    Adesa(
        "6.3.46", becomes="mahā", of=("mahat",),
        before=("samānādhikaraṇa", "jātīya"),
        keeps_out="महत्पुत्रः — a genitive, not an apposition; "
                  "अमहान् महान् संपन्नो महद्भूतश्चन्द्रमाः — the "
                  "sense of महत् is secondary there, "
                  "**गौणत्वाद् महदर्थस्य न भवत्यात्वम्**",
        why="आन्महतः समानाधिकरणजातीययोः — महत् becomes महा before "
            "an APPOSITIONAL second member and before जातीय: "
            "**महादेवः, महाब्राह्मणः, महाबाहुः, महाबलः; "
            "महाजातीयः**.\\n\\n"
            "**AND THE WORD समानाधिकरण IS THERE FOR THE बहुव्रीहि "
            "AND NOT FOR THE GENITIVE.** **लक्षणोक्तत्वाद् एवात्र "
            "न भविष्यतीति चेद्, बहुव्रीहावपि न स्यान् महाबाहुरिति। "
            "तदर्थं समानाधिकरणग्रहणं वक्तव्यम्** — one could keep "
            "महत्पुत्रः out by a paribhāṣā, but that would keep "
            "महाबाहुः out too, so the condition is stated"),
    Adesa(
        "6.3.47", becomes="dvā", of=("dvi", "aṣṭan"),
        uttarapada_gana="saṅkhyā", excludes=("bahuvrīhi", "aśīti"),
        keeps_out="पञ्चदश — पञ्चन् is not one of the two; "
                  "द्वैमातुरः — no numeral follows; द्वित्राः, "
                  "द्विदशाः — a बहुव्रीहि; द्व्यशीतिः — अशीति, "
                  "named out; द्विशतम्, अष्टसहस्रम् — at or above "
                  "a hundred, by the vārttika",
        why="द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः — द्वि and "
            "अष्टन् take आ before a NUMERAL, but not in a "
            "बहुव्रीहि and not before अशीति: **द्वादश, "
            "द्वाविंशतिः, द्वात्रिंशत्; अष्टादश, अष्टाविंशतिः, "
            "अष्टात्रिंशत्**.\\n\\n"
            "**AND HOW HIGH IT GOES IS A VĀRTTIKA'S.** **प्राक् "
            "शतादिति वक्तव्यम्। इह मा भूत् — द्विशतम्, "
            "द्विसहस्रम्, अष्टशतम्, अष्टसहस्रम्** — nothing in the "
            "three sūtras says the numeral must be below a "
            "hundred, and the forms show it must"),
    Adesa(
        "6.3.48", becomes="trayas", of=("tri",),
        uttarapada_gana="saṅkhyā", excludes=("bahuvrīhi", "aśīti"),
        keeps_out="त्रैमातुरः — no numeral; त्रिदशाः — a "
                  "बहुव्रीहि; त्र्यशीतिः — अशीति; त्रिशतम्, "
                  "त्रिसहस्रम् — at or above a hundred",
        why="त्रेस्त्रयः — and त्रि becomes त्रयस् in the same "
            "place: **त्रयोदश, त्रयोविंशतिः, त्रयस्त्रिंशत्**. "
            "Everything else carries down from the sūtra before, "
            "the vārttika's **प्राक् शतात्** included"),
    Adesa(
        "6.3.49", becomes="", of=("dvi", "aṣṭan", "tri"),
        uttarapada_gana="catvāriṃśat-prabhṛti",
        excludes=("bahuvrīhi", "aśīti"), optional=True,
        blocks=("6.3.47", "6.3.48"),
        keeps_out="द्विशतम्, अष्टशतम्, त्रिशतम् — still below a "
                  "hundred is wanted",
        why="विभाषा चत्वारिंशत्प्रभृतौ सर्वेषाम् — from चत्वारिंशत् "
            "upward, all three substitutions are OPTIONAL: "
            "**द्विचत्वारिंशत् / द्वाचत्वारिंशत्; त्रिपञ्चाशत् / "
            "त्रयःपञ्चाशत्; अष्टपञ्चाशत् / अष्टापञ्चाशत्**. The "
            "word सर्वेषाम् is what gathers the three earlier "
            "rules under one option — **द्वि अष्टन् त्रि "
            "इत्येतेषां यदुक्तं तद् विभाषा भवति**"),
    Adesa(
        "6.3.50", becomes="hṛd", of=("hṛdaya",),
        before=("lekha", "yat", "aṇ", "lāsa"),
        keeps_out="हृदयलेखः — the लेख formed with घञ्, which this "
                  "rule does not name",
        why="हृदयस्य हृल्लेखयदण्लासेषु — हृदय becomes हृद् before "
            "four things: **हृदयं लिखतीति हृल्लेखः; हृदयस्य "
            "प्रियं हृद्यम्; हृदयस्येदं हार्दम्; हृदयस्य लासो "
            "हृल्लासः**.\\n\\n"
            "**AND WHICH लेख IS MEANT SETTLES A PARIBHĀṢĀ FOR THE "
            "WHOLE PĀDA.** **लेख इत्यणन्तस्य ग्रहणम् इष्यते। घञि "
            "तु हृदयस्य लेखो हृदयलेखः। एतदेव लेखग्रहणं ज्ञापकम् "
            "उत्तरपदाधिकारे प्रत्ययग्रहणे तदन्ताग्रहणस्य** — the "
            "sūtra names यत् and अण् as affixes and लेख as a word. "
            "If naming an affix under this heading reached "
            "everything ending in it, लेख would have been "
            "redundant. Its being there proves it does not — the "
            "fact 6.3.17's vṛtti had already appealed to"),
    Adesa(
        "6.3.51", becomes="hṛd", of=("hṛdaya",),
        before=("śoka", "ṣyañ", "roga"), optional=True,
        why="वा शोकष्यञ्रोगेषु — and optionally before three more: "
            "**हृच्छोकः / हृदयशोकः; सौहार्द्यम् / सौहृदय्यम्; "
            "हृद्रोगः / हृदयरोगः**.\\n\\n"
            "**AND THE OPTION MAY BE DOING NOTHING AT ALL.** "
            "**हृदयशब्देन समानार्थो हृच्छब्दः प्रकृत्यन्तरम् "
            "अस्ति, तेनैव सिद्धे विकल्पविधानं प्रपञ्चार्थम्** — "
            "हृद् is an independent stem of the same meaning, so "
            "both forms were available without any rule, and the "
            "option is stated only to spell the matter out"),
    Adesa(
        "6.3.52", becomes="pad", of=("pāda",), before=PADA_BEFORE,
        why="पादस्य पदाज्यातिगोपहतेषु — पाद becomes पद् before "
            "four: **पादाभ्याम् अजतीति पदाजिः; पादाभ्याम् अततीति "
            "पदातिः; पादाभ्यां गच्छतीति पदगः; पादेनोपहतः "
            "पदोपहतः**.\\n\\n"
            "**AND THE SUBSTITUTE CARRIES AN ACCENT THE ORIGINAL "
            "DID NOT.** **पादशब्दो वृषादित्वाद् आद्युदात्तः, तस्य "
            "स्थाने पदादेश उपदेश एवान्तोदात्तो निपात्यते। तेन "
            "पदोपहत इति** — पाद is accented on its first syllable "
            "by 6.1.203's वृषादि, but पद् is laid down "
            "end-accented in the statement itself, which is how "
            "पदोपहतः comes out as it does instead of by 6.2.48"),
    Adesa(
        "6.3.53", becomes="pad", of=("pāda",), before=("yat",),
        excludes=("tadartha",),
        keeps_out="पाद्यम् — water FOR the feet, which is तदर्थ; "
                  "द्विपाद्यम्, त्रिपाद्यम् — the पाद of 5.1.34, "
                  "a measure and not a limb",
        why="पद्यत्यतदर्थे — and before यत्, where the sense is "
            "NOT for-that-purpose: **पादौ विध्यन्ति पद्याः "
            "शर्कराः; पद्याः कण्टकाः** — gravel that pricks the "
            "feet.\\n\\n"
            "**AND ONLY THE LIMB IS MEANT.** **शरीरावयववचनस्य "
            "पादशब्दस्य ग्रहणम् इह इष्यते** — so 5.1.34's पाद, a "
            "quarter, is untouched. A vārttika adds one more "
            "place: **पद्भाव इके चरतौ उपसंख्यानम् — पादाभ्यां "
            "चरति पदिकः**"),
    Adesa(
        "6.3.54", becomes="pad", of=("pāda",),
        before=("hima", "kāṣin", "hati"),
        why="हिमकाषिहतिषु च — and before three more: **पद्धिमम्; "
            "अथ पत्काषिणो यान्ति; पद्धतिः** — cold in the feet, "
            "those who go grazing the ground, a beaten track"),
    Adesa(
        "6.3.55", becomes="pad", of=("pāda",), before=("śas",),
        result=("ṛc",),
        keeps_out="पादशः कार्षापणं ददाति — quarter by quarter of "
                  "a coin, and no verse in sight",
        why="ऋचः शे — and before शस्, where the पाद is a VERSE's: "
            "**पच्छो गायत्रीं शंसति** — he recites the Gāyatrī "
            "foot by foot. The शस् is 5.4.43's, **पादंपादं "
            "शंसतीति संख्यैकवचनाच्च वीप्सायाम्**"),
    Adesa(
        "6.3.56", becomes="pad", of=("pāda",),
        before=("ghoṣa", "miśra", "śabda", "niṣka"), optional=True,
        why="वा घोषमिश्रशब्देषु — and optionally before three: "
            "**पद्घोषः / पादघोषः; पन्मिश्रः / पादमिश्रः; "
            "पच्छब्दः / पादशब्दः**. A vārttika adds a fourth: "
            "**निष्के चेति वक्तव्यम् — पन्निष्कः, पादनिष्कः**"),
    Adesa(
        "6.3.57", becomes="uda", of=("udaka",), result=("saṃjñā",),
        keeps_out="उदकगिरिः — not a name",
        why="उदकस्योदः संज्ञायाम् — उदक becomes उद where the "
            "compound is a NAME: **उदमेघो नाम यस्य औदमेघिः "
            "पुत्रः; उदवाहो नाम यस्य औदवाहिः पुत्रः**.\\n\\n"
            "**AND A VĀRTTIKA TURNS THE RULE ROUND.** "
            "**संज्ञायाम् उत्तरपदस्य उदकशब्दस्य उदादेशो भवतीति "
            "वक्तव्यम् — लोहितोदः, नीलोदः, क्षीरोदः** — the same "
            "substitute for उदक standing as the SECOND member, "
            "which the sūtra as written cannot reach"),
    Adesa(
        "6.3.58", becomes="uda", of=("udaka",), before=UDA_FOUR,
        why="पेषंवासवाहनधिषु च — and before four more, name or no "
            "name: **उदपेषं पिनष्टि; उदकस्य वास उदवासः; उदकस्य "
            "वाहनम् उदवाहनः; उदकं धीयतेऽस्मिन्नित्युदधिः** — "
            "ground with water, a store of water, a water-cart, "
            "and the sea. The णमुल् of the first is 3.4.38's, "
            "**स्नेहने पिषः**"),
    Adesa(
        "6.3.59", becomes="uda", of=("udaka",), optional=True,
        result=("ekahalādi-pūrayitavya",),
        keeps_out="उदकस्थालम् — स्थ् is two consonants, so not "
                  "एकहलादि; उदकपर्वतः — a mountain is not "
                  "something to be filled",
        why="एकहलादौ पूरयितव्येऽन्यतरस्याम् — optionally, before a "
            "second member that begins with a SINGLE consonant "
            "and names something TO BE FILLED: **उदकुम्भः / "
            "उदककुम्भः; उदपात्रम् / उदकपात्रम्**.\\n\\n"
            "**AND एकहल् IS GLOSSED BEFORE USE.** **एकोऽसहायः, "
            "तुल्यजातीयेनानन्तरेण हला विना, हल् आदिर्यस्य "
            "उत्तरपदस्य तद् एकहलादिः** — one consonant with no "
            "second of its own kind next to it"),
    Adesa(
        "6.3.60", becomes="uda", of=("udaka",), before=UDA_TEN,
        optional=True,
        why="मन्थौदनसक्तुबिन्दुवज्रभारहारवीवधगाहेषु च — and "
            "optionally before nine more: **उदमन्थः / उदकमन्थः; "
            "उदौदनः / उदकौदनः; उदसक्तुः / उदकसक्तुः; उदबिन्दुः / "
            "उदकबिन्दुः; उदवज्रः / उदकवज्रः; उदभारः / उदकभारः; "
            "उदहारः / उदकहारः; उदवीवधः / उदकवीवधः** — and "
            "उदगाहः beside उदकगाहः"),
)


def _reaches(row: Adesa, purvapada: str, before: str,
             uttarapada_gana: str, result: str) -> bool:
    if row.of and purvapada not in row.of:
        return False
    named = row.before or row.uttarapada_gana
    if named and not (before in row.before
                      or (row.uttarapada_gana
                          and uttarapada_gana == row.uttarapada_gana)):
        return False
    if row.result and result not in row.result:
        return False
    if row.excludes and (before in row.excludes
                         or uttarapada_gana in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Adesa, wants: str) -> bool:
    return not wants or wants == row.becomes


def _how_specific(row: Adesa, before: str, uttarapada_gana: str) -> int:
    """
    Naming the following word beats naming the class it falls in.

    Nothing here competes on `blocks`. 6.3.49 records that it makes
    6.3.47 and 6.3.48 optional — **सर्वेषाम्, द्वि अष्टन् त्रि
    इत्येतेषां यदुक्तं तद् विभाषा भवति** — but it cannot be
    reached in the same query as either, because the class it wants
    is चत्वारिंशत्प्रभृति and theirs is संख्या at large. The
    `blocks` field is the record of an argument, not a tie-break.
    """
    return (
        8 * bool(row.before and before in row.before)
        + 5 * bool(row.uttarapada_gana
                   and uttarapada_gana == row.uttarapada_gana)
        + 4 * bool(row.result)
        + 2 * bool(row.of)
    )


@dataclass(frozen=True)
class Substituted:
    """What the run answers: a substitute, and by which rule."""

    becomes: str
    sutra: str
    why: str
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def replaced_by(purvapada: str = "", *, before: str = "",
                uttarapada_gana: str = "", result: str = "",
                wants: str = "") -> Substituted:
    """
    6.3.46–60 — what the first member becomes before a second.

    Nothing answers by default: where no rule is reached the first
    member stands as it is, which is what महत्पुत्रः and
    उदकगिरिः are.
    """
    matched = [
        row for row in ADESA_TABLE
        if _reaches(row, purvapada, before, uttarapada_gana, result)
        and _supplies(row, wants)
    ]
    if not matched:
        return Substituted(
            "", "", "No rule of 6.3.46–60 is reached, so the first "
                    "member stands as it is")
    row = max(matched,
              key=lambda one: _how_specific(one, before, uttarapada_gana))
    return Substituted(row.becomes, row.sutra, row.why,
                       optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Adesa, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ADESA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Adesa", "ADESA_TABLE", "ADESA_RUN", "PRAK_SATAT",
    "PADA_BEFORE", "UDA_TEN", "UDA_FOUR", "Substituted",
    "replaced_by", "provisions_for",
]
