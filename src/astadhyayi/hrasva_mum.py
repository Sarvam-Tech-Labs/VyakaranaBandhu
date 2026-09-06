# -*- coding: utf-8 -*-
"""
६.३.६१–७२ — the first member shortened, and the मुम् put into it.

Two operations, and the join between them is the point.

**Six rules shorten.** An इक्-final feminine that is not ङी-ending
goes short before a second member on Gālava's authority (6.3.61);
एक goes short before a taddhita and before a second member
(6.3.62); a ङी- or आप्-ending stem goes short variously in a name
and in the Veda (6.3.63) and before त्व (6.3.64); three stems go
short before three second members, matched one to one (6.3.65);
and anything that is not an indeclinable goes short before a
खित् (6.3.66).

**And then मुम् is put in, in the very same place.** 6.3.67 gives
अरुस्, द्विषत् and every vowel-final stem a मुम् before a खित् —
अरुंतुदः, द्विषंतपः, कालिंमन्या — and the two rules do not fight:
**मुमा ह्रस्वो न बाध्यते, अन्यथा हि ह्रस्वशासनम् अनर्थकं स्यात्**.
The shortening runs first and the मुम् is added to what it left,
and the vṛtti proves it from 6.3.67's own wording: **अन्तग्रहणं
किम्? कृताजन्तकार्यप्रतिपत्त्यर्थम्। अतो ह्रस्वे कृते मुम्
भवति**.

**AND ONE AUGMENT IS TOLD TO BEHAVE LIKE AN ENDING.** 6.3.68 gives
a one-vowelled इच्-final stem अम् instead, **अम्प्रत्ययवच्च** —
and the vṛtti says what that buys: **अम्प्रत्ययवच्चेत्यतिदेशाद्
आत्वपूर्वसवर्णगुणेयङुवङादेशा भवन्ति**. Calling it *like the
accusative singular* imports five rules at once, which is why
गाम्मन्यः and श्रियंमन्यः come out as they do.

**WHAT THIS MODULE DOES NOT DO.** It reports what happens and by
which rule. It does not carry the operation out: which vowel goes
short, and what अम् then becomes after the atideśa, belong to the
rules 6.3.68 imports.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these twelve stand, between the substitutions of 6.3.46–60
#: and 6.3.73's नञ्.
HRASVA_RUN: Tuple[str, str] = ("6.3.61", "6.3.72")

#: 6.3.65's three pairs, matched one to one by यथासंख्यम्. Crossing
#: them reaches nothing: इष्टका goes only with चित.
YATHASAMKHYAM: Tuple[Tuple[str, str], ...] = (
    ("iṣṭakā", "cita"), ("iṣīkā", "tūla"), ("mālā", "bhārin"))

#: What 6.3.61's option does NOT reach, though its conditions are
#: met — the vṛtti calls the option व्यवस्थितविभाषा and names them.
GALAVA_KEEPS_OUT: Tuple[str, ...] = (
    "kārīṣagandhī", "śrī", "bhrū", "kāṇḍībhūta", "vṛṣalībhūta")

#: The five rules 6.3.68's अम्प्रत्ययवत् imports at once:
#: **आत्वपूर्वसवर्णगुणेयङुवङादेशा भवन्ति**.
AM_ATIDESA: Tuple[str, ...] = (
    "ātva", "pūrvasavarṇa", "guṇa", "iyaṅ", "uvaṅ")

#: The three stems 6.3.67 gives मुम् to, the third being a class.
MUM_STEMS: Tuple[str, ...] = ("arus", "dviṣat", "ac-anta")


@dataclass(frozen=True)
class Change:
    """One rule of 6.3.61–72: what is done to the first member."""

    sutra: str
    #: hrasva — its final goes short; mum, am — an augment is put
    #: in; nipātana — the whole word is laid down.
    does: str = ""
    #: The first members the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of first member instead.
    stem: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: Where the rule matches a stem to a following word one for
    #: one — यथासंख्यम् — the pairs, and nothing crossed.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    optional: bool = False
    bahulam: bool = False
    #: True where the form is laid down whole rather than derived.
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


HRASVA_TABLE: Tuple[Change, ...] = (
    Change(
        "6.3.61", does="hrasva", stem="ik-anta-aṅī", optional=True,
        excludes=GALAVA_KEEPS_OUT,
        keeps_out="खट्वापादः, मालापादः — not इक्-final; "
                  "गार्गीपुत्रः, वात्सीपुत्रः — ङी-ending, which "
                  "the sūtra shuts out; कारीषगन्धीपुत्रः — the "
                  "option is व्यवस्थित and does not fall here; "
                  "श्रीकुलम्, भ्रूकुलम् — इयङुवङ्भाविन्; "
                  "काण्डीभूतम् — an अव्यय",
        why="इको ह्रस्वोऽङ्यो गालवस्य — an इक्-final feminine that "
            "is NOT ङी-ending goes short before a second member, "
            "on Gālava's authority: **ग्रामणिपुत्रः / "
            "ग्रामणीपुत्रः; ब्रह्मबन्धुपुत्रः / "
            "ब्रह्मबन्धूपुत्रः**.\\n\\n"
            "**AND NAMING THE ĀCĀRYA IS HONOUR AND NOT OPTION.** "
            "**गालवग्रहणं पूजार्थम्। अन्यतरस्यामिति हि वर्तते** — "
            "the option was already running from 6.3.44, so "
            "Gālava's name adds nothing to the grammar and "
            "everything to the record. The same distinction 6.1.92 "
            "and 6.1.130 turned on.\\n\\n"
            "**AND THE OPTION IS SETTLED AND NOT FREE.** "
            "**व्यवस्थितविभाषा चेयम्। तेनेह न भवति — "
            "कारीषगन्धीपुत्र इति। इयङुवङ्भाविनाम् अव्ययानां च न "
            "भवति। श्रीकुलम्, भ्रूकुलम्, काण्डीभूतम्** — a विभाषा "
            "that holds in some places and not in others, with the "
            "places named"),
    Change(
        "6.3.62", does="hrasva", of=("eka",),
        before=("taddhita", "uttarapada"),
        why="एक तद्धिते च — एक goes short before a taddhita and "
            "before a second member: **एकस्या आगतम् एकरूप्यम्, "
            "एकमयम्; एकस्या भाव एकत्वम्, एकता**; and for the "
            "second member, **एकस्याः क्षीरम् एकक्षीरम्, "
            "एकदुग्धम्**.\\n\\n"
            "**AND THE SHORTENING IS WHAT SHOWS THE WORD IS TAKEN "
            "WITH ITS GENDER.** **लिङ्गिविशिष्टस्य ग्रहणम् "
            "एकशब्दह्रस्वत्वं प्रयोजयति। अचा हि गृह्यमाणम् अत्र "
            "विशेष्यते, न पुनरज् गृह्यमाणेनेति** — a rule that "
            "shortens a vowel must be naming a word that HAS one "
            "to shorten, so एका and not the bare stem एक"),
    Change(
        "6.3.63", does="hrasva", stem="ṅī-āp", bahulam=True,
        result=("saṃjñā", "chandas"),
        keeps_out="नान्दीकरः, नान्दीघोषः, नान्दीविशालः — names, and "
                  "no shortening; फाल्गुनीपौर्णमासी, जगतीछन्दः — "
                  "in the Veda, and none either; लोमकागृहम्, "
                  "लोमकाषण्डम् — आप्-ending in a name, and none",
        why="ङ्यापोः संज्ञाछन्दसोर्बहुलम् — a ङी- or आप्-ending "
            "stem goes short VARIOUSLY where the compound is a "
            "name and in the Veda: **रेवतिपुत्रः, रोहिणिपुत्रः, "
            "भरणिपुत्रः** for the ङी in a name; **कुमारिदा, "
            "उर्विदा** for the ङी in the Veda; **शिलवहम्, "
            "शिलप्रस्थम्** for the आप् in a name; **अजक्षीरेण "
            "जुहोति** for the आप् in the Veda. And बहुलम् is not "
            "an option: the vṛtti pairs every example with a "
            "**न च भवति** of the same shape"),
    Change(
        "6.3.64", does="hrasva", stem="ṅī-āp", before=("tva",),
        bahulam=True,
        why="त्वे च — and before त्व, variously: **तद् अजाया "
            "भावोऽजत्वम्, अजात्वम्; तद् रोहिण्या भावो रोहिणित्वम्, "
            "रोहिणीत्वम्**. The vṛtti notes where the examples "
            "have to come from: **संज्ञायाम् असंभवाच् "
            "छन्दस्येवोदाहरणानि भवन्ति** — an abstract noun in त्व "
            "cannot also be a name, so only the Veda supplies "
            "them"),
    Change(
        "6.3.65", does="hrasva", pairs=YATHASAMKHYAM,
        of=tuple(one for one, _ in YATHASAMKHYAM),
        before=tuple(two for _, two in YATHASAMKHYAM),
        why="इष्टकेषीकामालानां चिततूलभारिषु — three stems go short "
            "before three second members, matched ONE TO ONE: "
            "**इष्टकचितम्; इषीकतूलम्; मालभारिणी कन्या** — built of "
            "bricks, a tuft of reed, a girl wearing a garland. "
            "यथासंख्यम्, so इष्टका goes with चित and with nothing "
            "else.\\n\\n"
            "**AND NAMING THE THREE REACHES WHAT ENDS IN THEM.** "
            "**इष्टकादिभ्यस् तदन्तस्यापि ग्रहणं भवति — "
            "पक्वेष्टकचितम्, मुञ्जेषीकतूलम्, उत्पलमालभारिणी "
            "कन्या** — which is the opposite of what 6.3.50's "
            "लेखग्रहण established for an AFFIX named under this "
            "heading. A word named here does reach what ends in "
            "it; an affix named here does not"),
    Change(
        "6.3.66", does="hrasva", stem="anavyaya", before=("khit",),
        excludes=("avyaya",), blocks=(),
        keeps_out="दोषामन्यमहः, दिवामन्या रात्रिः — दोषा and दिवा "
                  "are indeclinables",
        why="खित्यनव्ययस्य — before a खित्, anything that is NOT "
            "an indeclinable goes short: **कालिंमन्या, "
            "हरिणिंमन्या** — she who thinks herself a black "
            "antelope.\\n\\n"
            "**AND THE MUM OF THE NEXT SŪTRA DOES NOT DISPLACE "
            "IT.** **मुमा ह्रस्वो न बाध्यते, अन्यथा हि "
            "ह्रस्वशासनम् अनर्थकं स्यात्** — if the augment won, "
            "this rule would never apply at all, so both act and "
            "the shortening acts first.\\n\\n"
            "**AND SAYING अनव्ययस्य IS WHAT SHOWS खित् MEANS "
            "खिदन्त.** **अनव्ययस्येत्येतद् एव ज्ञापकम् इह "
            "खिदन्तग्रहणस्य** — an indeclinable could only be the "
            "first member, so the खित् the rule speaks of must be "
            "the second member ENDING in one"),
    Change(
        "6.3.67", does="mum", of=("arus", "dviṣat"),
        stem="ac-anta", before=("khit",), excludes=("avyaya",),
        keeps_out="विद्वन्मन्यः — विद्वस् is none of the three; "
                  "दोषामन्यमहः, दिवामन्या रात्रिः — indeclinables, "
                  "still excepted",
        why="अरुर्द्विषदजन्तस्य मुम् — अरुस्, द्विषत् and any "
            "VOWEL-FINAL stem take the augment मुम् before a "
            "खित्, an indeclinable excepted: **अरुंतुदः, "
            "द्विषंतपः; कालिंमन्या** — one who probes a wound, one "
            "who scorches his enemies.\\n\\n"
            "**AND THE WORD अन्त IS THERE TO FIX THE ORDER.** "
            "**अन्तग्रहणं किम्? कृताजन्तकार्यप्रतिपत्त्यर्थम्। अतो "
            "ह्रस्वे कृते मुम् भवति** — saying अजन्त rather than "
            "अच् makes the rule speak of a stem AFTER whatever was "
            "due to its final vowel has happened. So 6.3.66 "
            "shortens कालिनी to कालि and the मुम् is put into that"),
    Change(
        "6.3.68", does="am", stem="ic-anta-ekāc", before=("khit",),
        blocks=("6.3.67",),
        keeps_out="त्वङ्मन्यः — त्वच् is not इच्-final; "
                  "लेखाभ्रुंमन्यः — more than one vowel",
        why="इच एकाचोऽम्प्रत्ययवच्च — a one-vowelled इच्-final "
            "stem takes अम् instead, and that अम् behaves like the "
            "accusative singular: **गांमन्यः; स्त्रींमन्यः, "
            "स्त्रियंमन्यः; नरंमन्यः; श्रियंमन्यः; भ्रुवंमन्यः**. "
            "**अमिति हि द्विरावर्तते** — the word अम् is read "
            "twice over, once as the augment and once as what it "
            "is likened to.\\n\\n"
            "**AND THE LIKENESS IMPORTS FIVE RULES AT ONCE.** "
            "**अम्प्रत्ययवच्चेत्यतिदेशाद् "
            "आत्वपूर्वसवर्णगुणेयङुवङादेशा भवन्ति** — the आ, the "
            "single-vowel replacement, the guṇa, the इयङ् and the "
            "उवङ् all follow, which is what makes गाम्मन्यः and "
            "श्रियंमन्यः the shapes they are.\\n\\n"
            "**AND ONE FORM IS LEFT UNSETTLED.** **अथेह कथं "
            "भवितव्यम्, श्रियम् आत्मानं ब्राह्मणकुलं मन्यत "
            "इत्युपक्रम्य श्रिमन्यम् इति भवितव्यम् इति भाष्ये** — "
            "the Mahābhāṣya's reading, and the vṛtti records it "
            "without resolving it"),
    Change(
        "6.3.69", does="mum", of=("vāc", "pur"), nipatana=True,
        before=("yama", "dara"),
        pairs=(("vāc", "yama"), ("pur", "dara")),
        why="वाचंयमपुरन्दरौ च — two words laid down whole: "
            "**वाचंयम आस्ते; पुरं दारयतीति पुरंदरः** — one who "
            "holds his speech, and the breaker of forts. Neither "
            "is derived: **इत्येतौ निपात्येते**"),
    Change(
        "6.3.70", does="mum", of=("satya", "agada"),
        before=("kāra",),
        why="कारे सत्यागदस्य — सत्य and अगद take मुम् before कार: "
            "**सत्यं करोतीति, सत्यस्य वा कारः सत्यंकारः; "
            "एवमगदंकारः** — an earnest-money pledge, and the "
            "making of a medicine.\\n\\n"
            "**AND FOUR VĀRTTIKAS ADD FOUR MORE.** "
            "**अस्तुसत्यागदस्य कार इति वक्तव्यम् — अस्तुंकारः**; "
            "**भक्षस्य छन्दसि कारे मुम् वक्तव्यः — भक्षंकारः**, "
            "and not outside the Veda — **छन्दसीति किम्? "
            "भक्षकारः**; **धेनोर्भव्यायां मुम् वक्तव्यः — "
            "धेनुंभव्या**; and **लोकस्य पृणे मुम् वक्तव्यः — "
            "लोकंपृणा**"),
    Change(
        "6.3.71", does="mum", of=("śyena", "tila"),
        before=("pāta",), result=("ña",),
        keeps_out="श्येनपातः — no ञ, so no मुम्",
        why="श्येनतिलस्य पाते ञे — श्येन and तिल take मुम् before "
            "पात, but only where a ञ affix follows: "
            "**श्येनपातोऽस्यां क्रियायां श्यैनंपाता; तैलंपाता** — "
            "the swoop of a hawk, the pressing of sesame. The "
            "condition is on what comes AFTER the second member, "
            "not on the second member itself"),
    Change(
        "6.3.72", does="mum", of=("rātri",), before=("kṛt",),
        optional=True,
        why="रात्रेः कृति विभाषा — रात्रि takes मुम् optionally "
            "before a कृत्-formed second member: **रात्रिंचरः / "
            "रात्रिचरः; रात्रिमटः / रात्र्यटः** — one who goes "
            "about by night.\\n\\n"
            "**AND THE OPTION ONLY GIVES WHAT WAS NOT ALREADY "
            "DUE.** **अप्राप्तविभाषेयम्। खिति हि नित्यं मुम् "
            "भवति। रात्रिंमन्यः** — before a खित् the मुम् is "
            "compulsory by 6.3.67, so this विभाषा can only be "
            "about the कृदन्तs that are not खित्"),
)


def _reaches(row: Change, purvapada: str, stem: str, before: str,
             result: str) -> bool:
    if row.pairs and (purvapada, before) not in row.pairs:
        return False
    named = row.of or row.stem
    if named and not (purvapada in row.of
                      or (row.stem and stem == row.stem)):
        return False
    if row.before and before not in row.before:
        return False
    if row.result and result not in row.result:
        return False
    if row.excludes and (purvapada in row.excludes
                         or stem in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Change, wants: str) -> bool:
    return not wants or wants == row.does


def _how_specific(row: Change, purvapada: str, stem: str) -> int:
    """
    A rule that names what it displaces outranks it, and a named
    stem beats a named class.

    6.3.68 is the case. It and 6.3.67 both act before a खित्, and
    6.3.67's class अजन्त contains 6.3.68's इजन्त एकाच् entirely —
    गो is vowel-final and one-vowelled at once. Only 6.3.68's
    saying so puts it first.
    """
    return (
        4 * len(row.blocks)
        + 6 * bool(row.pairs)
        + 5 * bool(row.of and purvapada in row.of)
        + 3 * bool(row.stem and stem == row.stem)
        + 2 * bool(row.result)
        + 2 * bool(row.before)
    )


@dataclass(frozen=True)
class Adjusted:
    """What the run answers: what is done, and by which rule."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    bahulam: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def adjusts(purvapada: str = "", *, stem: str = "",
            before: str = "", result: str = "",
            wants: str = "") -> Adjusted:
    """
    6.3.61–72 — what is shortened or put in before a second member.

    Nothing answers by default: where no rule is reached the first
    member stands with its own length and no augment.
    """
    matched = [
        row for row in HRASVA_TABLE
        if _reaches(row, purvapada, stem, before, result)
        and _supplies(row, wants)
    ]
    if not matched:
        return Adjusted(
            "", "", "No rule of 6.3.61–72 is reached, so the first "
                    "member keeps its own length and takes no "
                    "augment")
    row = max(matched,
              key=lambda one: _how_specific(one, purvapada, stem))
    return Adjusted(row.does, row.sutra, row.why,
                    optional=row.optional, bahulam=row.bahulam,
                    nipatana=row.nipatana, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Change, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in HRASVA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Change", "HRASVA_TABLE", "HRASVA_RUN", "YATHASAMKHYAM",
    "GALAVA_KEEPS_OUT", "AM_ATIDESA", "MUM_STEMS", "Adjusted",
    "adjusts", "provisions_for",
]
