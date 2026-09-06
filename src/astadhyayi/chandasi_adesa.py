# -*- coding: utf-8 -*-
"""
७.१.३४–५० — four rules of the language, then thirteen of the Veda.

7.1.34–37 finish the ordinary substitutions: णल् becomes औ after
an आ-final stem (पपौ, तस्थौ), तु and हि take तातङ् in a blessing
(जीवताद् भवान्), शतृ becomes वसु after विद् (विद्वान्), and क्त्वा
becomes ल्यप् in a compound (प्रकृत्य, प्रहृत्य).

**AND THEN THE VEDA TAKES OVER FOR THIRTEEN SŪTRAS.** From 7.1.38
the word छन्दसि governs, and the vṛtti says how far — **छन्दोऽधिकार
आज्जसेरसुक् इति यावत्**, to 7.1.50 and no further. Inside it the
grammar loosens: 7.1.39 सुपां सुलुक्० lets ANY case ending stand
for any other, and two vārttikas widen even that — **सुपां सुपो
भवन्ति**, **तिङां तिङो भवन्ति**. One sūtra, and the whole Vedic
declension and conjugation are let off the hook.

**THE VEDIC RULES ARE NOT OPTIONS.** Each names a form the Veda
actually has and says what the ordinary grammar would have given
instead — **अदुह्र**, अदुहत being what was due; **वारयध्वात्**,
वारयध्वम् being due; **कृणुतात्**, कृणुत being due. The Kāśikā
writes इति प्राप्ते after each, and the module keeps that as the
`instead_of` column: what the rule displaces is part of the rule.

**WHAT THIS MODULE DOES NOT DO.** It does not decide whether a
given passage is छन्दस्. That is a fact about the text, and the
caller supplies it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
CHANDAS_RUN: Tuple[str, str] = ("7.1.34", "7.1.50")

#: Where छन्दसि starts governing, and where the vṛtti says it
#: stops — **छन्दोऽधिकार आज्जसेरसुक् इति यावत्**.
CHANDAS_FROM: str = "7.1.38"
CHANDAS_TO: str = "7.1.50"

#: 7.1.39's ten substitutes, any of which may stand for any सुप्.
SUP_TEN: Tuple[str, ...] = (
    "su", "luk", "pūrvasavarṇa", "ā", "āt", "śe", "yā", "ḍā",
    "ḍyā", "yāc", "āl")

#: The two vārttikas that widen 7.1.39 past what it says.
WIDENED_BY: Tuple[str, ...] = (
    "सुपां सुपो भवन्तीति वक्तव्यम्",
    "तिङां तिङो भवन्तीति वक्तव्यम्")

#: 7.1.45's four substitutes for the imperative's त.
TAP_FOUR: Tuple[str, ...] = ("tap", "tanap", "tan", "than")

#: 7.1.49's स्नात्वी and its like — a class named by its first
#: member, **प्रकारार्थोऽयमादिशब्दः**.
SNATVYADI: Tuple[str, ...] = ("snātvī", "pītvī")


@dataclass(frozen=True)
class Vedic:
    """One rule of 7.1.34–50: a substitute, an augment, or a form."""

    sutra: str
    #: What is supplied, or `nipātana` where a whole word is laid
    #: down.
    does: str = ""
    #: What the rule acts on.
    of: Tuple[str, ...] = ()
    #: The root or stem it must follow.
    root: Tuple[str, ...] = ()
    #: The stem class instead.
    after: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: The sense the rule wants.
    sense: str = ""
    #: Only in a compound, and only one with no नञ् in front.
    samasa: str = ""
    #: What the ordinary grammar would have given — the Kāśikā's
    #: own **इति प्राप्ते**.
    instead_of: str = ""
    augment: bool = False
    optional: bool = False
    chandasi: bool = False
    bahulam: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


VEDIC_TABLE: Tuple[Vedic, ...] = (
    Vedic(
        "7.1.34", does="au", of=("ṇal",), after="ā-anta",
        why="आत औ णलः — after an आ-final stem the perfect's णल् "
            "becomes औ: **पपौ, तस्थौ, जग्लौ, मम्लौ**.\\n\\n"
            "**AND THE ORDER OF FOUR OPERATIONS IS SETTLED BY "
            "TWO REASONS, NOT ONE.** **अत्रौत्वम् एकादेशः "
            "स्थानिवद्भावो द्विर्वचनम् इत्यनेन क्रमेण कार्याणि "
            "क्रियन्ते** — the औ goes in first for having nowhere "
            "else to apply, **अनवकाशत्वात्**, and the एकादेश "
            "beats the reduplication for being later, "
            "**परत्वात्**"),
    Vedic(
        "7.1.35", does="tātaṅ", of=("tu", "hi"), sense="āśis",
        optional=True,
        keeps_out="ग्रामं गच्छतु भवान्, गच्छ त्वम् — an order and "
                  "not a blessing",
        why="तुह्योस्तातङाशिष्यन्यतरस्याम् — तु and हि optionally "
            "become तातङ् where a BLESSING is meant: **जीवताद् "
            "भवान्, जीवतात् त्वम्** beside **जीवतु भवान्, जीव "
            "त्वम्**.\\n\\n"
            "**AND ITS ङ् DOES TWO JOBS AND IS ARGUED OVER FOR "
            "BOTH.** **ङित्करणं गुणवृद्धिप्रतिषेधार्थम् इति "
            "सर्वादेशस्तातङ् भवति** — the marker stops 1.1.5's "
            "strengthening, which shows the substitute replaces "
            "the whole ending; and **ङित् च पिद् न भवति**, so "
            "7.3.93's ईट् does not come and ब्रूताद् भवान् "
            "stands. Two verses then ask whether a ङित् can be "
            "an अन्त्यविधि at all: **तातङो ङित्त्वसामर्थ्याद् "
            "नायम् अन्त्यविधिः स्मृतः**"),
    Vedic(
        "7.1.36", does="vasu", of=("śatṛ",), root=("vid",),
        why="विदेः शतुर्वसुः — after विद् the शतृ becomes वसु: "
            "**विद्वान्, विद्वांसौ, विद्वांसः**.\\n\\n"
            "**AND ITS उ IS THERE FOR A RULE THREE PĀDAS BACK.** "
            "**स्थानिवद्भावाद् उगित्कार्ये सिद्धे वसोर् "
            "उकारकरणं वसोः संप्रसारणम् इत्यत्र क्वसोरपि "
            "सामान्यग्रहणार्थम्** — the substitute could have "
            "been वस्, and is वसु so that 6.4.131 may catch क्वसु "
            "as well. And **एकानुबन्धकग्रहणे न द्व्यनुबन्धकस्य** "
            "is set aside here, or the उ would be pointless. "
            "Some read अन्यतरस्याम् in: **विदन्, विदन्तौ, "
            "विदन्तः**"),
    Vedic(
        "7.1.37", does="lyap", of=("ktvā",), samasa="an-añ-pūrva",
        keeps_out="कृत्वा, हृत्वा — no compound; अकृत्वा, "
                  "परमकृत्वा — a नञ् or its like in front",
        why="समासेऽनञ्पूर्वे क्त्वो ल्यप् — in a compound whose "
            "first member is not नञ्, क्त्वा becomes ल्यप्: "
            "**प्रकृत्य, प्रहृत्य, पार्श्वतःकृत्य, नानाकृत्य, "
            "द्विधाकृत्य**.\\n\\n"
            "**AND अनञ् MEANS MORE THAN नञ्.** **अनञ् इति "
            "नञोऽन्यद् अनञ् नञ्सदृशम् अव्ययं परिगृह्यते** — an "
            "indeclinable LIKE नञ्, which is how परमकृत्वा and "
            "उत्तमकृत्वा are kept out too, though neither has a "
            "नञ् in it. And स्नात्वाकालकः keeps its क्त्वा by "
            "2.1.72's निपातन"),
    Vedic(
        "7.1.38", does="ktvā", of=("ktvā",), samasa="an-añ-pūrva",
        chandasi=True, optional=True, blocks=("7.1.37",),
        why="क्त्वाऽपि छन्दसि — but in the Veda the क्त्वा may "
            "STAY: **कृष्णं वासो यजमानं परिधापयित्वा; "
            "प्रत्यञ्चम् अर्कं प्रत्यर्पयित्वा** — and the अपि "
            "lets ल्यप् stand too, **उद्धृत्य जुहुयात्**.\\n\\n"
            "**AND IT IS NOT PUT AS वा FOR A REASON.** **वा "
            "छन्दसीति नोक्तं सर्वोपाधिव्यभिचारार्थम्** — said as "
            "an option it would have varied only the one thing; "
            "said so, every condition of 7.1.37 may lapse, and "
            "the ल्यप् reaches a NON-compound: **अर्च्य तान् "
            "देवान् गतः**.\\n\\n"
            "**AND THE छन्दस् HEADING BEGINS HERE.** "
            "**छन्दोऽधिकार आज्जसेरसुक् इति यावत्** — thirteen "
            "sūtras, ending at 7.1.50"),
    Vedic(
        "7.1.39", does="sup-ādeśa", of=("sup",), chandasi=True,
        instead_of="पन्थानः, दक्षिणायाम्, चर्मणि, धीत्या",
        why="सुपां सुलुक्पूर्वसवर्णाऽऽच्छेयाडाड्यायाजालः — in the "
            "Veda ANY case ending may be replaced by सु, लुक्, "
            "the preceding vowel's own long, आ, आत्, शे, या, डा, "
            "ड्या, याच् or आल्: **ऋजवः सन्तु पन्थाः** where "
            "पन्थानः was due; **लोहिते चर्मन्** for चर्मणि; "
            "**धीती, मती, सुष्टुती** for धीत्या, मत्या, "
            "सुष्ट्युत्या.\\n\\n"
            "**AND TWO VĀRTTIKAS WIDEN IT PAST WHAT IT SAYS.** "
            "**सुपां सुपो भवन्तीति वक्तव्यम्** — any nominal "
            "ending for any other, **धुरि दक्षिणायाः** for "
            "दक्षिणायाम्; and **तिङां तिङो भवन्तीति वक्तव्यम्** "
            "— any verbal ending for any other, **ये अश्वयूपाय "
            "तक्षति** for तक्षन्ति. One sūtra and two vārttikas, "
            "and the whole Vedic declension and conjugation are "
            "let off"),
    Vedic(
        "7.1.40", does="maś", of=("am",), chandasi=True,
        instead_of="अवधम्, अक्रमम्",
        why="अमो मश् — the मिप्-substitute अम् becomes मश् in the "
            "Veda: **वधीं वृत्रम्; क्रमीं वृक्षस्य शाखाम्**. The "
            "श् makes it replace the whole ending — **शित्करणं "
            "सर्वादेशार्थम्**, since a bare म् for a म् could "
            "only have been about the anusvāra. And 6.4.75's "
            "बहुलम् is why there is no अट् augment"),
    Vedic(
        "7.1.41", does="lopa", of=("ta",), after="ātmanepada",
        chandasi=True, instead_of="अदुहत, दुग्धाम्, शेते",
        keeps_out="उत्सं दुहन्ति कलशम् — परस्मैपद, and the त् "
                  "stays; तत्र आत्मानम् अनृतं कुरुते — outside "
                  "the Veda",
        why="लोपस्त आत्मनेपदेषु — in the Veda the त् of an "
            "आत्मनेपद ending is dropped: **देवा अदुह्र** for "
            "अदुहत; **दुहाम् अश्विभ्यां पयो अघ्न्येयम्** for "
            "दुग्धाम्; **दक्षिणतः पुमान् स्त्रियम् उपशये** for "
            "शेते. This is what finishes 7.1.8's अदुह्र — the झ "
            "became अत्, took रुट्, and now loses its त्"),
    Vedic(
        "7.1.42", does="dhvāt", of=("dhvam",), chandasi=True,
        instead_of="वारयध्वम्",
        why="ध्वमो ध्वात् — ध्वम् becomes ध्वात् in the Veda: "
            "**अन्तरेवोष्माणं वारयध्वात्**, where वारयध्वम् was "
            "due"),
    Vedic(
        "7.1.43", does="nipātana", of=("yajadhvam",),
        before=("enam",), chandasi=True, nipatana=True,
        instead_of="यजध्वम् एनम्",
        why="यजध्वैनमिति च — यजध्वैनम् is laid down whole before "
            "एनम्: **यजध्वैनं प्रियमेधाः**. Two things are "
            "निपातित at once — **मकारलोपो निपात्यते वकारस्य च "
            "यकारः** — the म् goes and the व् becomes य्, and "
            "यजध्वम् एनम् was what the grammar owed"),
    Vedic(
        "7.1.44", does="tāt", of=("ta",), chandasi=True,
        instead_of="कृणुत, खनत, संसृजत, गमयत",
        why="तस्य तात् — the imperative's second-person plural त "
            "becomes तात् in the Veda: **गात्रं गात्रम् अस्यानूनं "
            "कृणुतात्; ऊवध्यगोहं पार्थिवं खनतात्; अस्ना रक्षः "
            "संसृजतात्; सूर्यं चक्षुर्गमयतात्** — four in one "
            "verse, and the vṛtti names what each displaces"),
    Vedic(
        "7.1.45", does="tap-tanap-tan-than", of=("ta",),
        chandasi=True, instead_of="शृणुत, सुनुत, धत्त, जुषत, इच्छत",
        why="तप्तनप्तनथनाश्च — and the same त may become तप्, "
            "तनप्, तन or थन: **शृणोत ग्रावाणः** and **सुनोता** "
            "for तप्; **सं वरत्रा दधातन** for तनप्; **जुजुष्टन** "
            "for तन; **यदिष्ठन** for थन. **पित्करणम् "
            "अङित्त्वार्थम्** — the प् markers are there only to "
            "stop the substitutes counting as ङित्"),
    Vedic(
        "7.1.46", does="iṭ", of=("masi",), chandasi=True,
        augment=True, instead_of="उद्दीपयामः, भञ्जयामः, वसामः",
        why="इदन्तो मसि — मस् takes an इ and ends in it, in the "
            "Veda: **पुनस्त्वोद् दीपयामसि; शलभान् भञ्जयामसि; "
            "त्वयि रात्रि वसामसि**. The rule is put as *ending "
            "in इ* rather than as an augment — **मसः "
            "सकारान्तस्य इकारागमो भवति, स च तस्यान्तो भवति। "
            "तद्ग्रहणेन गृह्यत इत्यर्थः** — so that a rule "
            "naming मसि catches it"),
    Vedic(
        "7.1.47", does="yak", of=("ktvā",), samasa="an-añ-pūrva",
        chandasi=True, augment=True, instead_of="दत्त्वा",
        why="क्त्वो यक् — क्त्वा takes the augment यक् in the "
            "Veda: **दत्त्वाय सविता धियः**, where दत्त्वा was "
            "due. And the vṛtti asks why it is not put next to "
            "7.1.38, which is also about क्त्वा: **समास इति "
            "तत्रानुवर्तते** — the compound condition is carried "
            "here from 7.1.37 and would have been lost"),
    Vedic(
        "7.1.48", does="nipātana", of=("iṣṭvīnam",), chandasi=True,
        nipatana=True, instead_of="इष्ट्वा",
        why="इष्ट्वीनमिति च — इष्ट्वीनम् is laid down whole: "
            "**इष्ट्वीनं देवान्**, where इष्ट्वा देवान् was due. "
            "The ईनम् replaces the last part of यज् + क्त्वा, "
            "and the च takes in more than is said — "
            "**पीत्वीनम् इत्यपीष्यते। चकारस्यानुक्तसमुच्चयार्थ"
            "त्वात् सिद्धम्**"),
    Vedic(
        "7.1.49", does="nipātana", of=SNATVYADI, chandasi=True,
        nipatana=True, instead_of="स्नात्वा, पीत्वा",
        why="स्नात्व्यादयश्च — स्नात्वी and its like are laid "
            "down whole: **स्नात्वी मलादिव; पीत्वी सोमस्य "
            "वावृधे**. And the आदि is not a list but a kind — "
            "**प्रकारार्थोऽयम् आदिशब्दः**, so the class is open"),
    Vedic(
        "7.1.50", does="asuk", of=("jas",), after="a-varṇa-anta",
        chandasi=True, augment=True,
        instead_of="ब्राह्मणाः, सोम्याः",
        why="आज्जसेरसुक् — after an अ-final stem the जस् takes "
            "the augment असुक् in the Veda: **ब्राह्मणासः पितरः "
            "सोम्यासः**, where ब्राह्मणाः सोम्याः was due.\\n\\n"
            "**AND IT CLOSES THE छन्दस् HEADING.** The vṛtti had "
            "said at 7.1.38 that the heading runs **आज्जसेरसुक् "
            "इति यावत्**, and here it ends. It also settles one "
            "order on the way: in **ये पूर्वासो य उपरासः** the "
            "असुक् might have let 7.1.17's शी apply afresh, and "
            "**सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितम् एव** "
            "— what was once set aside stays set aside"),
)


def _reaches(row: Vedic, what: str, root: str, after: str,
             before: str, sense: str, samasa: str,
             chandasi: bool) -> bool:
    if row.of and what and what not in row.of:
        return False
    if row.root and root not in row.root:
        return False
    if row.after and after != row.after:
        return False
    if row.before and before not in row.before:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.samasa and samasa != row.samasa:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Vedic, what: str, root: str) -> int:
    """
    A rule that names what it displaces beats it, a named root
    beats a named class, and the Veda beats the language.

    7.1.37 and 7.1.38 are the pair that needs it: one turns
    क्त्वा into ल्यप् in a compound, and the other lets the
    क्त्वा stay — but only in the Veda.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.root and root in row.root)
        + 6 * bool(row.before)
        + 5 * bool(row.sense)
        + 4 * bool(row.after)
        + 4 * bool(row.samasa)
        + 3 * bool(row.of and what in row.of)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Given:
    """What the run answers: a substitute, an augment, or a form."""

    does: str
    sutra: str
    why: str
    instead_of: str = ""
    augment: bool = False
    optional: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def in_the_veda(what: str = "", *, root: str = "", after: str = "",
                before: str = "", sense: str = "",
                samasa: str = "", chandasi: bool = False,
                wants: str = "") -> Given:
    """
    7.1.34–50 — the last ordinary substitutions, and the Vedic ones.

    Nothing answers by default. Ask without `chandasi=True` and the
    thirteen Vedic rules are all out of reach, which is the point
    of the heading.
    """
    matched = [
        row for row in VEDIC_TABLE
        if _reaches(row, what, root, after, before, sense, samasa,
                    chandasi)
        and (not wants or wants == row.does)
    ]
    if not matched:
        return Given(
            "", "", "No rule of 7.1.34-50 is reached, so nothing "
                    "is supplied")
    row = max(matched, key=lambda one: _how_specific(one, what, root))
    return Given(row.does, row.sutra, row.why,
                 instead_of=row.instead_of, augment=row.augment,
                 optional=row.optional, nipatana=row.nipatana,
                 blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Vedic, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in VEDIC_TABLE if row.sutra == sutra_id)


__all__ = [
    "Vedic", "VEDIC_TABLE", "CHANDAS_RUN", "CHANDAS_FROM",
    "CHANDAS_TO", "SUP_TEN", "WIDENED_BY", "TAP_FOUR",
    "SNATVYADI", "Given", "in_the_veda", "provisions_for",
]
