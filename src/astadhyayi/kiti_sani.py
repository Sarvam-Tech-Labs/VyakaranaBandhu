# -*- coding: utf-8 -*-
"""
७.४.४१–५७ — दा becomes दद्, तास् and अस् lose their स्, and सन्.

Seventeen sūtras. 7.4.41–47 finish the कित् block: शा and छा take
इ optionally (निशितम् beside निशातम्), धा becomes हि (हितः,
हित्वा), and दा becomes दद् (दत्तः) or, after a vowel-final
preverb, plain त् (प्रत्तम्). 7.4.48–52 take away the स् of अप्,
तास् and अस् — अद्भिः, कर्तासि, कर्तारौ, कर्ताहे. And 7.4.54–57
give eight roots an इस् before सन्, three an ई, and मुच् an
optional guṇa.

**AND ONE SUBSTITUTE'S LAST SOUND IS ARGUED FOR IN A VERSE.**
7.4.46's दद् is written with a त् at the end and read with a थ्,
and the vṛtti sets out what each choice would cost: **तान्ते
दोषो दीर्घत्वं स्याद् दान्ते दोषो निष्ठानत्वम्। धान्ते दोषो
धत्वप्राप्तिस्थान्तेऽदोषस् तस्मात् थान्तम्** — four candidates,
three of them producing a wrong form, and the fourth chosen for
producing none.

**AND ONE LOSS LEAVES A WORD THAT IS ALL AFFIX.** 7.4.50 drops
the स् of अस् before a स्-initial ending, and in व्यतिसे what is
left of the stem is nothing at all: **अस्तेर् अकारसकारयोर्
लुप्तयोः से इति प्रत्ययमात्रम् एतत् पदम्** — which is why
8.3.111's ष् does not come.

**WHAT THIS MODULE DOES NOT DO.** It says what the stem becomes.
That the desiderative takes सन् is 3.1.7's, and the निष्ठा's
own affix 3.2.102's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
KITI_RUN: Tuple[str, str] = ("7.4.41", "7.4.57")

#: Where the run turns to the desiderative.
SANI_FROM: str = "7.4.54"

#: 7.4.54's eight, whose vowel becomes इस् before सन्.
MI_MA_EIGHT: Tuple[str, ...] = (
    "mī", "mā", "ghu", "rabh", "labh", "śak", "pat", "pad")

#: 7.4.55's three, which take ई instead.
AP_JNAP_RDH: Tuple[str, ...] = ("āp", "jñap", "ṛdh")

#: 7.4.45's five Vedic forms, laid down whole.
SUDHITADI: Tuple[str, ...] = (
    "sudhita", "vasudhita", "nemadhita", "dhiṣva", "dhiṣīya")

#: What the vṛtti's verse settles about 7.4.46's substitute.
THANTAM: str = (
    "तान्ते दोषो दीर्घत्वं स्याद् दान्ते दोषो निष्ठानत्वम्। "
    "धान्ते दोषो धत्वप्राप्तिस् थान्तेऽदोषस् तस्मात् थान्तम्")


@dataclass(frozen=True)
class Kiti:
    """One rule of 7.4.41–57: a substitute, a loss, or a guṇa."""

    sutra: str
    #: `it`, `hi`, `dad`, `ta`, `lopa`, `ha`, `is`, `īt`, `guṇa`.
    does: str = ""
    #: The roots or stems named outright.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: The preverb the stem must carry.
    upasarga: str = ""
    #: A further condition on the stem.
    result: Tuple[str, ...] = ()
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


KITI_TABLE: Tuple[Kiti, ...] = (
    Kiti(
        "7.4.41", does="it", of=("śā", "chā"),
        before=("ta-ādi-kit",), optional=True, blocks=("7.4.40",),
        why="शाछोरन्यतरस्याम् — शा and छा take इ OPTIONALLY "
            "before a त-initial कित्: **निशितम्, निशातम्; "
            "अवच्छितम्, अवच्छातम्**. A vārttika makes it "
            "compulsory of a VOW — **श्यतेरित्त्वं व्रते "
            "नित्यम्। संशितव्रतः** — and a verse settles that "
            "the two options do not combine: **मिथस्ते न "
            "विभाष्यन्ते गवाक्षः संशितव्रतः**"),
    Kiti(
        "7.4.42", does="hi", of=("dhā",), before=("ta-ādi-kit",),
        blocks=("7.4.40",),
        why="दधातेर्हिः — धा becomes हि before a त-initial कित्: "
            "**हितः, हितवान्, हित्वा**. 7.4.40 had given the "
            "आ-final roots an इ; this replaces the whole root "
            "instead, and the two rules are told apart by "
            "nothing but which of them names धा"),
    Kiti(
        "7.4.43", does="hi", of=("hā",), before=("ktvā",),
        keeps_out="हात्वा — जिहीति and not जहाति, which the "
                  "sūtra's own form names",
        why="जहातेश्च क्त्वि — and हा before क्त्वा: **हित्वा "
            "राज्यं वनं गतः; हित्वा गच्छति**. The हा meant is "
            "जहाति and not जिहीते — **जहातेर् निदेशाज् जिहीतेर् "
            "न भवति**"),
    Kiti(
        "7.4.44", does="hi", of=("hā",), before=("ktvā",),
        chandasi=True, optional=True, blocks=("7.4.43",),
        why="विभाषा छन्दसि — and in the Veda it is optional: "
            "**हित्वा शरीरं यातव्यम्; हात्वा**. What the sūtra "
            "before made compulsory the Veda may leave undone, "
            "and both forms then stand — the ordinary shape of "
            "a छन्दसि option in this pāda"),
    Kiti(
        "7.4.45", does="nipātana", of=SUDHITADI, chandasi=True,
        nipatana=True,
        why="सुधितवसुधितनेमधितधिष्वधिषीय च — five Vedic forms "
            "laid down: **गर्भं माता सुधितम्** where सुहितम् was "
            "due; **वसुधितमग्नौ जुहोति** for वसुहितम्; "
            "**नेमधिता बाधन्ते** for नेमहिता. Each is धा with "
            "the इ of 7.4.42 refused and an इट् given instead, "
            "and धिष्व takes a third thing besides — no "
            "reduplication"),
    Kiti(
        "7.4.46", does="dad", of=("dā",), gana="ghu",
        before=("ta-ādi-kit",), blocks=("7.4.40",),
        keeps_out="धीतः, धीतवान् — the root is धेट् and not दा; "
                  "दातं बर्हिः, अवदातं मुखम् — दाप् and दैप्, "
                  "which are not घु",
        why="दो दद् घोः — the घु-named दा becomes दद् before a "
            "त-initial कित्: **दत्तः, दत्तवान्, दत्तिः**.\\n\\n"
            "**AND THE SUBSTITUTE'S LAST SOUND IS ARGUED FOR IN "
            "A VERSE.** **अयम् आदेशस् थान्त इष्यते** — written "
            "with a त् and read with a थ्, and the verse sets "
            "out what each choice would cost: **तान्ते दोषो "
            "दीर्घत्वं स्याद् दान्ते दोषो निष्ठानत्वम्। धान्ते "
            "दोषो धत्वप्राप्तिस् थान्तेऽदोषस् तस्मात् थान्तम्** "
            "— four candidates, three producing a wrong form and "
            "the fourth chosen for producing none"),
    Kiti(
        "7.4.47", does="ta", of=("dā",), gana="ghu",
        upasarga="ac-anta-upasarga", before=("ta-ādi-kit",),
        blocks=("7.4.46",),
        keeps_out="निर्दत्तम्, दुर्दत्तम् — the preverb does not "
                  "end in a vowel; दधि दत्तम्, मधु दत्तम् — no "
                  "preverb at all",
        why="अच उपसर्गात्तः — but after a VOWEL-FINAL preverb it "
            "becomes plain त्: **प्रत्तम्, अवत्तम्, नीत्तम्, "
            "परीत्तम्**. The ablative would put the substitute "
            "at the stem's head, and the vṛtti answers by "
            "reading अचः twice — **अचः इत्येतद् "
            "द्विरावर्तयितव्यम्**, once for the preverb and once "
            "for what is replaced"),
    Kiti(
        "7.4.48", does="ta", of=("ap",), before=("bha-ādi",),
        keeps_out="अप्सु — the ending does not begin with भ्",
        why="अपो भि — अप् becomes अत् before a भ्-initial ending: "
            "**अद्भिः, अद्भ्यः**. A vārttika adds four more "
            "words for the Veda — **स्ववःस्वतवसोर् मास उषसश्च "
            "तकारादेश इष्यते छन्दसि: स्ववद्भिः, स्वतवद्भिः, "
            "माद्भिः, समुषद्भिः**"),
    Kiti(
        "7.4.49", does="ta", gana="s-anta",
        before=("sa-ādi-ārdhadhātuka",),
        keeps_out="वक्ष्यति — the stem does not end in स्; "
                  "घासः, वासः — the affix does not begin with "
                  "स्; आस्से, वस्से — a सार्वधातुक",
        why="सः स्यार्द्धधातुके — a स्-final stem becomes "
            "त्-final before a स्-initial ārdhadhātuka: "
            "**वत्स्यति, अवत्स्यत्, विवत्सति, जिघत्सति**"),
    Kiti(
        "7.4.50", does="lopa", of=("tās", "as"),
        before=("sa-ādi",),
        why="तासस्त्योर्लोपः — तास् and अस् lose their स् before "
            "a स्-initial affix: **कर्तासि, कर्तासे; त्वमसि, "
            "व्यतिसे**.\\n\\n"
            "**AND WHAT IS LEFT OF अस् IN व्यतिसे IS NOTHING AT "
            "ALL.** **अस्तेर् अकारसकारयोर् लुप्तयोः से इति "
            "प्रत्ययमात्रम् एतत् पदम्** — a word that is all "
            "affix, which is why 8.3.111's ष् does not come"),
    Kiti(
        "7.4.51", does="lopa", of=("tās", "as"),
        before=("ra-ādi",),
        why="रि च — and before a र्-initial affix: **कर्तारौ, "
            "कर्तारः; अध्येतारौ, अध्येतारः**. The र् is the "
            "one 7.1.94's अनङ् put there, so this rule works on "
            "what a पाद back supplied — and only for तास् and "
            "अस्, carried down from the sūtra before"),
    Kiti(
        "7.4.52", does="ha", of=("tās", "as"), before=("e",),
        why="ह एति — and before ए their स् becomes ह्: "
            "**कर्ताहे; व्यतिहे**. A substitute where the two "
            "rules before had a loss, and the ए is the "
            "first-person singular आत्मनेपद ending — one sound "
            "for one sound, and the last of the three rules "
            "about तास् and अस्"),
    Kiti(
        "7.4.53", does="lopa", of=("dīdhī", "vevī"),
        before=("ya-ādi", "i-varṇa-ādi"),
        keeps_out="आदीध्यनम्, आवेव्यनम् — the affix begins with "
                  "neither य् nor an इ-sound",
        why="यीवर्णयोर्दीधीवेव्योः — दीधी and वेवी lose their "
            "last vowel before a य्-initial or इ-initial affix: "
            "**आदीध्य गतः, आवेव्य गतः, आदीध्यते, आवेव्यते** for "
            "the य्; **आदीधिता, आवेविता; आदीधीत, आवेवीत** for "
            "the इ"),
    Kiti(
        "7.4.54", does="is", of=MI_MA_EIGHT, before=("sa-ādi-san",),
        keeps_out="दास्यति — no सन्; पिपतिषति — the affix does "
                  "not begin with स्",
        why="सनि मीमाघुरभलभशकपतपदामच इस् — eight stems' vowel "
            "becomes इस् before a स्-initial सन्: **मित्सति, "
            "प्रमित्सति; मित्सते, अपमित्सते; दित्सति, धित्सति; "
            "आरिप्सते, आलिप्सते; शिक्षति; पित्सति, प्रपित्सते**. "
            "Both roots of the shape मी are meant, and घु takes "
            "in both दा and धा"),
    Kiti(
        "7.4.55", does="īt", of=AP_JNAP_RDH,
        before=("sa-ādi-san",), blocks=("7.4.54",),
        keeps_out="प्राप्स्यति — no सन्; जिज्ञपयिषति, अर्दिधिषति "
                  "— the सन् has an इट् in front and does not "
                  "begin with स्",
        why="आप्ज्ञप्यृधामीत् — आप्, ज्ञपि and ऋध् take ई "
            "instead: **आपीप्सति; ज्ञीप्सति; ईर्त्सति**. ज्ञपि "
            "has two vowels, and the vṛtti orders the two "
            "operations — **णेः पूर्वविप्रतिषेधेन लोपः, "
            "इतरस्य तु ईत्वम्**"),
    Kiti(
        "7.4.56", does="it", of=("dambh",), before=("sa-ādi-san",),
        optional=True, blocks=("7.4.54",),
        keeps_out="दिदम्भिषति — the सन् has an इट् in front",
        why="दम्भ इच्च — and दम्भ् takes इ, and by the च the "
            "long ई as well: **धिप्सति, धीप्सति**. The च "
            "carries down 7.4.55's ईत् while the sūtra states "
            "इत् of its own, so one rule gives two forms — and "
            "**सि इत्येव** keeps दिदम्भिषति out, its सन् "
            "having an इट् in front"),
    Kiti(
        "7.4.57", does="guṇa", of=("muc",), before=("sa-ādi-san",),
        result=("akarmaka",), optional=True,
        keeps_out="मुमुक्षति वत्सं देवदत्तः — the verb has an "
                  "object, and no guṇa comes",
        why="मुचोऽकर्मकस्य गुणो वा — मुच् takes guṇa OPTIONALLY "
            "before a स्-initial सन् where it has no object: "
            "**मोक्षते वत्सः स्वयम् एव, मुमुक्षते वत्सः स्वयम् "
            "एव**. What is really made optional is 1.2.10's "
            "refusal of the कित् marking — **हलन्ताच् च इति "
            "कित्त्वप्रतिषेधो विकल्प्यते** — and the guṇa "
            "follows from that"),
)


def _reaches(row: Kiti, root: str, gana: str, before: str,
             upasarga: str, result: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.upasarga and upasarga != row.upasarga:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Kiti, root: str, gana: str) -> int:
    """
    A rule that names what it displaces beats it, a named
    preverb beats a named root, and a named root beats a class.

    7.4.46 against 7.4.47 is what needs the preverb: दत्तः and
    प्रत्तम् differ in nothing else.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.upasarga)
        + 6 * bool(row.of and root in row.of)
        + 4 * bool(row.result)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Became:
    """What the run answers: the stem's new shape, or its loss."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_kit(root: str = "", *, gana: str = "",
               before: str = "", upasarga: str = "",
               result: str = "", chandasi: bool = False) -> Became:
    """
    7.4.41–57 — before a कित्, before a स्, and before सन्.

    Nothing answers by default. A root none of these seventeen
    names goes into the form as it stands.
    """
    matched = [
        row for row in KITI_TABLE
        if _reaches(row, root, gana, before, upasarga, result,
                    chandasi)
    ]
    if not matched:
        return Became(
            "", "", "No rule of 7.4.41-57 is reached, so the "
                    "stem stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Became(row.does, row.sutra, row.why,
                  optional=row.optional, nipatana=row.nipatana,
                  blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Kiti, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in KITI_TABLE if row.sutra == sutra_id)


__all__ = [
    "Kiti", "KITI_TABLE", "KITI_RUN", "SANI_FROM",
    "MI_MA_EIGHT", "AP_JNAP_RDH", "SUDHITADI", "THANTAM",
    "Became", "before_kit", "provisions_for",
]
