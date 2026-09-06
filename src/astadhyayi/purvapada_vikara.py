# -*- coding: utf-8 -*-
"""
६.३.९६–११३ — the remaining alterations of the first member.

Eighteen rules and no single theme, which is itself the fact worth
recording: this is where the pāda puts what would not group. सह
becomes सध once more, in the Veda only; अप् becomes ई after three
things and ऊ after one; अन्य takes a दुक् before nine words; and
कु — the particle of contempt — becomes कद्, का or कवम् across
eight sūtras, more than any other stem in the pāda.

**AND THEN ONE RULE LICENSES WHAT NO RULE DESCRIBES.** 6.3.109
पृषोदरादीनि यथोपदिष्टम् — **येषु लोपागमवर्णविकाराः शास्त्रेण न
विहिता दृश्यन्ते च, तानि यथोपदिष्टानि साधूनि भवन्ति** — words in
which a sound has been dropped, added or changed with no rule
behind it are correct as the learned use them, and the vṛtti then
derives half a dozen of them by hand: पृषदुदरं यस्य पृषोदरम्;
वारिवाहको बलाहकः; जीवनस्य मूतो जीमूतः. A rule of the grammar
whose content is that the grammar does not reach here.

**AND THREE OF THEM ARE ABOUT A LOSS THAT LENGTHENS.** 6.3.111
ढ्रलोपे पूर्वस्य दीर्घोऽणः — where a ढ् or a र् is dropped, the
vowel before it goes long: लीढम्, मीढम्, नीरक्तम्, प्राता
राजक्रयः. Then 6.3.112 makes it ओ instead for सह् and वह् —
सोढा, वोढा — and 6.3.113 lays down three Vedic forms whole.

**WHAT THIS MODULE DOES NOT DO.** It reports the alteration and
the rule. It does not perform the loss: which ढ् goes, and by what
rule, is 8.3.13's business, and this run only says what happens to
the vowel once it has.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these eighteen stand, between the नञ्/सह/समान run and
#: 6.3.114's संहितायाम्.
VIKARA_RUN: Tuple[str, str] = ("6.3.96", "6.3.113")

#: 6.3.99's nine, before which अन्य takes a दुक्.
DUK_NINE: Tuple[str, ...] = (
    "āśis", "āśā", "āsthā", "āsthita", "utsuka", "ūti", "kāraka",
    "rāga", "cha")

#: The three substitutes कु takes, and the eight sūtras that give
#: them — more rules than any other stem in the pāda gets.
KU_SHAPES: Tuple[str, ...] = ("kad", "kā", "kavam")

#: What 6.3.109's vṛtti derives by hand, to show the rule is not a
#: licence to invent: **पृषदुदरं यस्य पृषोदरम्; वारिवाहको
#: बलाहकः; जीवनस्य मूतो जीमूतः**.
PRSODARADI: Tuple[str, ...] = ("pṛṣodara", "balāhaka", "jīmūta")


@dataclass(frozen=True)
class Vikara:
    """One rule of 6.3.96–113: what happens to the first member."""

    sutra: str
    #: The substitute or augment, or `dīrgha` where a vowel is
    #: lengthened, or `yathopadiṣṭam` where nothing is prescribed
    #: and usage decides.
    becomes: str = ""
    #: The first members the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of first member instead — उपसर्ग.
    gana: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: The further condition — a sense, a register, a shape.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    samasa: str = ""
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


VIKARA_TABLE: Tuple[Vikara, ...] = (
    Vikara(
        "6.3.96", becomes="sadha", of=("saha",),
        before=("māda", "stha"), chandasi=True,
        why="सध मादस्थयोश्छन्दसि — in the Veda सह becomes सध "
            "before माद and स्थ: **सधमादो द्युम्निनीरापः; "
            "सधस्थाः** — the waters that rejoice together, the "
            "places where they stand together. The third shape सह "
            "takes in this pāda, after स at 6.3.78 and सध्रि at "
            "6.3.95"),
    Vikara(
        "6.3.97", becomes="īt", of=("dvi", "antar"),
        gana="upasarga", before=("ap",), excludes=("sam", "a-varṇa"),
        keeps_out="समापं नाम देवयजनम् — the vārttika **समाप ईत्वे "
                  "प्रतिषेधो वक्तव्यः**; प्रापम्, परापम् — the "
                  "other vārttika, **ईत्वम् अनवर्णात्**",
        why="द्व्यन्तरुपसर्गेभ्योऽप ईत् — अप् becomes ई after "
            "द्वि, after अन्तर्, and after an उपसर्ग: **द्वीपम्, "
            "अन्तरीपम्; नीपम्, वीपम्, समीपम्** — an island, a "
            "place between waters, water near at hand.\\n\\n"
            "**AND उपसर्ग IS SAID FOR SOMETHING WIDER THAN "
            "उपसर्ग.** **अप्शब्दं प्रति क्रियायोगाभावाद् "
            "उपसर्गग्रहणं प्राद्युपलक्षणार्थम्** — nothing here is "
            "joined to a verb, so nothing here is strictly an "
            "उपसर्ग at all; the word stands for the प्रादि list"),
    Vikara(
        "6.3.98", becomes="ūt", of=("anu",), before=("ap",),
        result=("deśa",),
        keeps_out="अन्वीपम् — no region meant, and 6.3.97's ई "
                  "stands instead",
        why="ऊदनोर्देशे — and after अनु it becomes ऊ, where a "
            "REGION is meant: **अनूपो देशः** — a watery country. "
            "**दीर्घोच्चारणम् अवग्रहार्थम्। अनु ऊपोऽनूप इति** — "
            "the substitute is written long so that the word may "
            "be resolved as अनु + ऊप"),
    Vikara(
        "6.3.99", becomes="duk", of=("anya",), before=DUK_NINE,
        excludes=("ṣaṣṭhī", "tṛtīyā"),
        why="अषष्ठ्यतृतीयास्थस्यान्यस्य दुक् — अन्य takes the "
            "augment दुक् before nine words, provided it is not "
            "standing in a genitive or an instrumental: **अन्या "
            "आशीः अन्यदाशीः; अन्या आशा अन्यदाशा; अन्य आस्थितः "
            "अन्यदास्थितः; अन्य उत्सुकः अन्यदुत्सुकः; अन्या ऊतिः "
            "अन्यदूतिः; अन्यः कारकः अन्यत्कारकः; अन्यो रागः "
            "अन्यद्रागः; अन्यस्मिन् भवोऽन्यदीयः**"),
    Vikara(
        "6.3.100", becomes="duk", of=("anya",), before=("artha",),
        optional=True,
        why="अर्थे विभाषा — and before अर्थ, optionally: "
            "**अन्यदर्थः / अन्यार्थः**"),
    Vikara(
        "6.3.101", becomes="kad", of=("ku",), before=("ac",),
        samasa="tatpuruṣa",
        keeps_out="कूष्ट्रो राजा — a बहुव्रीहि; कुब्राह्मणः, "
                  "कुपुरुषः — the second member does not begin "
                  "with a vowel",
        why="कोः कत् तत्पुरुषेऽचि — कु becomes कद् in a तत्पुरुष "
            "before a second member beginning with a VOWEL: "
            "**कदजः, कदश्वः, कदुष्ट्रः, कदन्नम्** — a wretched "
            "goat, a wretched horse. A vārttika adds one more: "
            "**कद्भावे त्रावुपसंख्यानम् — कुत्सितास्त्रयः "
            "कत्त्रयः**"),
    Vikara(
        "6.3.102", becomes="kad", of=("ku",),
        before=("ratha", "vada"),
        why="रथवदयोश्च — and before रथ and वद, vowel or no vowel: "
            "**कद्रथः, कद्वदः** — a poor chariot, a poor speaker"),
    Vikara(
        "6.3.103", becomes="kad", of=("ku",), before=("tṛṇa",),
        result=("jāti",),
        keeps_out="कुतृणानि — **कुत्सितानि तृणानि**, bad grasses "
                  "and not a species",
        why="तृणे च जातौ — and before तृण where a SPECIES is "
            "named: **कत्तृणा नाम जातिः** — the plant so called, "
            "and not merely poor grass"),
    Vikara(
        "6.3.104", becomes="kā", of=("ku",),
        before=("pathin", "akṣa"),
        why="का पथ्यक्षयोः — कु becomes का before पथिन् and अक्ष: "
            "**कापथः, काक्षः** — a bad road, a bad eye"),
    Vikara(
        "6.3.105", becomes="kā", of=("ku",), result=("īṣad",),
        blocks=("6.3.101",),
        why="ईषदर्थे च — and wherever कु means A LITTLE: "
            "**कामधुरम्, कालवणम्** — slightly sweet, slightly "
            "salt.\\n\\n"
            "**AND IT BEATS THE VOWEL RULE BY STANDING LATER.** "
            "**अजादावपि परत्वात् कादेश एव भवति। काम्लम्, कोष्णम्** "
            "— before a vowel 6.3.101 would have given कद्, and "
            "this rule takes it"),
    Vikara(
        "6.3.106", becomes="kā", of=("ku",), before=("puruṣa",),
        optional=True,
        why="विभाषा पुरुषे — and before पुरुष, optionally: "
            "**कापुरुषः / कुपुरुषः** — a wretch.\\n\\n"
            "**AND THE OPTION ONLY GIVES WHAT WAS NOT ALREADY "
            "DUE.** **अप्राप्तविभाषेयम्। ईषदर्थे तु "
            "पूर्वविप्रतिषेधेन नित्यं का भवति। ईषत्पुरुषः "
            "कापुरुषः** — in the sense *a little* 6.3.105 has "
            "already made का compulsory, and the earlier rule "
            "wins, so this विभाषा is only about the sense of "
            "contempt"),
    Vikara(
        "6.3.107", becomes="kavam", of=("ku",), before=("uṣṇa",),
        optional=True,
        why="कवं चोष्णे — before उष्ण, कु becomes कवम्, and का "
            "optionally beside it: **कवोष्णम्, कोष्णम्, "
            "कदुष्णम्** — lukewarm, in three forms. The कद् of "
            "the third is 6.3.101's, उष्ण beginning with a vowel"),
    Vikara(
        "6.3.108", becomes="kavam", of=("ku",), before=("pathin",),
        chandasi=True, optional=True, blocks=("6.3.104",),
        why="पथि च छन्दसि — and before पथिन् in the Veda, कवम् "
            "and का both, optionally: **कवपथः, कापथः, कुपथः** — "
            "three forms again, and the third is कु unaltered"),
    Vikara(
        "6.3.109", becomes="yathopadiṣṭam", gana="pṛṣodarādi",
        why="पृषोदरादीनि यथोपदिष्टम् — **पृषोदरप्रकाराणि "
            "शब्दरूपाणि, येषु लोपागमवर्णविकाराः शास्त्रेण न "
            "विहिता दृश्यन्ते च, तानि यथोपदिष्टानि साधूनि "
            "भवन्ति** — words in which a sound has been dropped, "
            "added or altered with no rule behind it are correct "
            "as the learned use them: **यानि यानि यथोपदिष्टानि "
            "शिष्टैरुच्चारितानि प्रयुक्तानि, तानि तथैवानुगन्तव्यानि**.\\n\\n"
            "**AND THE VṚTTI THEN DERIVES THEM BY HAND ANYWAY.** "
            "**पृषदुदरं यस्य पृषोदरम्** — with the त् dropped; "
            "**वारिवाहको बलाहकः** — with ब् for the first word and "
            "ल् for the second's र्; **जीवनस्य मूतो जीमूतः**. So "
            "the rule licenses the forms without pretending they "
            "are opaque: each is analysed, and only the operation "
            "is unlicensed"),
    Vikara(
        "6.3.110", becomes="ahan", of=("ahna",),
        gana="saṅkhyā-vi-sāya-pūrva", before=("ṅi",), optional=True,
        why="संख्याविसायपूर्वस्याह्नस्याहन्नन्यतरस्यां ङौ — where "
            "अह्न follows a numeral, वि or साय, it optionally "
            "becomes अहन् before the locative ending: **द्व्यह्नि "
            "/ द्व्यहनि; त्र्यह्नि / त्र्यहनि; व्यह्नि / व्यहनि; "
            "सायाह्नि / सायाहनि**.\\n\\n"
            "**AND NAMING वि AND साय TEACHES SOMETHING ELSE.** "
            "**एकदेशिसमासः पूर्वादिभ्योऽन्यस्यापि भवतीत्येतद् एव "
            "विसायपूर्वस्याह्नस्य ग्रहणं ज्ञापकम्** — a compound "
            "of a part with its whole is not confined to the "
            "पूर्वादि words, and this rule's naming वि and साय is "
            "what shows it"),
    Vikara(
        "6.3.111", becomes="dīrgha", result=("ḍhra-lopa",),
        excludes=("aṇ-anya",),
        keeps_out="आतृढम्, आवृढम् — the vowel before the loss is "
                  "not an अण्",
        why="ढ्रलोपे पूर्वस्य दीर्घोऽणः — where a ढ् or a र् is "
            "dropped, the अण् vowel before it goes LONG: "
            "**लीढम्, मीढम्, उपगूढम्, मूढः** for the ढ्; "
            "**नीरक्तम्, अग्नी रथः, इन्दू रथः, पुना रक्तं वासः, "
            "प्राता राजक्रयः** for the र्.\\n\\n"
            "**AND पूर्वस्य IS SAID SO THE RULE REACHES OUTSIDE A "
            "COMPOUND.** **पूर्वग्रहणम् अनुत्तरपदेऽपि पूर्वमात्रस्य "
            "दीर्घार्थम्** — 6.3.1's उत्तरपदे is still running, "
            "and saying *of what precedes* is what frees the rule "
            "from it. लीढम् is one word"),
    Vikara(
        "6.3.112", becomes="ot", of=("sah", "vah"),
        result=("ḍhra-lopa",), blocks=("6.3.111",),
        keeps_out="ऊढः, ऊढवान् — the vowel is not an अवर्ण",
        why="सहिवहोरोदवर्णस्य — but for सह् and वह् it is ओ and "
            "not a lengthening, and only for an अ or आ: **सोढा, "
            "सोढुम्, सोढव्यम्; वोढा, वोढुम्, वोढव्यम्**.\\n\\n"
            "**AND THE WORD वर्ण IS THERE TO CATCH THE STRENGTHENED "
            "VOWEL TOO.** **वर्णग्रहणं किम्? कृतायाम् अपि वृद्धौ "
            "यथा स्यात्। उदवोढाम्, उदवोढम्। तादपि परस्तपरः, "
            "तपरत्वाद् आकारस्य ग्रहणं न स्यात्** — written अत् the "
            "rule would have taken only the short अ, by 1.1.70; "
            "written अवर्ण it takes the आ that वृद्धि has made"),
    Vikara(
        "6.3.113", becomes="nipātana", of=("sah",),
        result=("nigama",), nipatana=True,
        keeps_out="सोढ्वा, सोढा — the ordinary forms, **इति "
                  "भाषायाम्**",
        why="साढ्यै साढ्वा साढेति निगमे — three forms of सह् are "
            "laid down whole for the Veda: **साढ्यै समन्तात्; "
            "साढ्वा शत्रून्; साढा**.\\n\\n"
            "**AND THE VṚTTI TAKES EACH APART ANYWAY.** **सहेः "
            "क्त्वाप्रत्यय ओत्त्वाभावः। पक्षे क्त्वाप्रत्ययस्य "
            "ध्यैभावः। साढेति तृचि रूपम् एतत्** — साढ्वा is क्त्वा "
            "with 6.3.112's ओ not applying, साढ्यै is the same "
            "क्त्वा turned to ध्यै, and साढा is तृच्. Laid down, "
            "and still accounted for"),
)


def _reaches(row: Vikara, purvapada: str, gana: str, before: str,
             samasa: str, result: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (purvapada in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.samasa and samasa != row.samasa:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.excludes and (purvapada in row.excludes
                         or before in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Vikara, wants: str) -> bool:
    return not wants or wants == row.becomes


def _how_specific(row: Vikara, purvapada: str, gana: str,
                  before: str) -> int:
    """
    A rule that names what it displaces outranks it, and naming
    the following word beats naming a sense.

    6.3.105 needs the first: it and 6.3.101 both reach कु before a
    vowel, and only **परत्वात् कादेश एव भवति** puts it first.
    6.3.98 needs the second the other way round: it and 6.3.97
    both reach अप्, and 6.3.98 wins by naming अनु outright where
    6.3.97 has only the class.
    """
    return (
        4 * len(row.blocks)
        + 6 * bool(row.of and purvapada in row.of)
        + 5 * bool(row.before and before in row.before)
        + 4 * bool(row.result)
        + 3 * bool(row.gana and gana == row.gana)
        + 2 * bool(row.samasa)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Altered:
    """What the run answers: an alteration, and by which rule."""

    becomes: str
    sutra: str
    why: str
    optional: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def altered(purvapada: str = "", *, gana: str = "",
            before: str = "", samasa: str = "", result: str = "",
            chandasi: bool = False, wants: str = "") -> Altered:
    """
    6.3.96–113 — what else happens to the first member.

    Nothing answers by default: where no rule is reached the first
    member stands as it was.
    """
    matched = [
        row for row in VIKARA_TABLE
        if _reaches(row, purvapada, gana, before, samasa, result,
                    chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Altered(
            "", "", "No rule of 6.3.96–113 is reached, so the "
                    "first member stands as it was")
    row = max(matched, key=lambda one: _how_specific(
        one, purvapada, gana, before))
    return Altered(row.becomes, row.sutra, row.why,
                   optional=row.optional, nipatana=row.nipatana,
                   blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Vikara, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in VIKARA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Vikara", "VIKARA_TABLE", "VIKARA_RUN", "DUK_NINE",
    "KU_SHAPES", "PRSODARADI", "Altered", "altered",
    "provisions_for",
]
