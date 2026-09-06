# -*- coding: utf-8 -*-
"""
६.४.११५–१२८ — the ए of the perfect, and the copy that goes with it.

Fourteen rules, and eight of them do one thing: where a root has a
single अ between two single consonants, the perfect makes that अ
an ए and DROPS THE REDUPLICATION ALTOGETHER. पचति gives पेचतुः,
not *पपचतुः; यम् gives येमुः; रम् gives रेणुः. One rule replaces
a vowel and deletes a syllable at the same time, and 6.4.120 is
that rule.

**AND THE CONDITIONS ON IT ARE FOUR AND EVERY ONE IS TESTED.**
**अनादेशादेः** — the stem must not begin with a substitute:
दिदिवतुः keeps its copy. **एकहल्मध्ये** — one consonant on each
side and no more: शश्रमिथ keeps its copy. **अतः** with a tapara —
the short अ only: ररासे keeps its copy. And लिटि — the perfect
alone.

**AND THEN SIX SŪTRAS ARGUE ABOUT WHO ELSE GETS IT.** 6.4.122
names four roots that the conditions would have missed and says
why each: **तरतेर् गुणार्थं वचनम्। फलिभजोर् आदेशाद्यर्थम्। त्रपेर्
अनेकहल्मध्यार्थम्** — one for its guṇa, two for beginning with a
substitute, one for having two consonants. 6.4.123 adds राध् in
one sense; 6.4.124 and 6.4.125 add nine more optionally; and
6.4.126 refuses the whole thing for three classes.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule acts and
what it gives. It does not reduplicate: that पच् has a copy to
lose is 6.1.8's doing, and this run only says when it goes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these fourteen stand, closing before 6.4.129's भस्य.
ABHYASA_RUN: Tuple[str, str] = ("6.4.115", "6.4.128")

#: The four conditions on 6.4.120, each with its own
#: counter-example in the vṛtti.
FOUR_CONDITIONS: Tuple[str, ...] = (
    "anādeśādi", "ekahal-madhya", "ataḥ-tapara", "liṭi")

#: 6.4.122's four, and the reason the vṛtti gives for each:
#: **तरतेर् गुणार्थम्। फलिभजोर् आदेशाद्यर्थम्। त्रपेर्
#: अनेकहल्मध्यार्थम्**.
WHY_FOUR_MORE: Tuple[Tuple[str, str], ...] = (
    ("tṝ", "guṇa"), ("phal", "ādeś-ādi"), ("bhaj", "ādeś-ādi"),
    ("trap", "anekahal-madhya"))

#: 6.4.124's three and 6.4.125's seven, which take it optionally.
OPTIONAL_THREE: Tuple[str, ...] = ("jṝ", "bhram", "tras")
PHANADI: Tuple[str, ...] = (
    "phaṇ", "rāj", "bhrāj", "bhrāś", "bhlāś", "syam", "svan")

#: 6.4.126's three classes, for which the whole thing is refused.
NO_ETVA: Tuple[str, ...] = ("śas", "dad", "v-ādi", "guṇa")


@dataclass(frozen=True)
class Etva:
    """One rule of 6.4.115–128: the ए, or the copy, or both."""

    sutra: str
    #: it, ā, lopa, et, tṛ — and `et-abhyāsalopa` where the ए and
    #: the loss of the copy are one rule's doing.
    does: str = ""
    #: The stems the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of stem instead.
    gana: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    bahulam: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ETVA_TABLE: Tuple[Etva, ...] = (
    Etva(
        "6.4.115", does="it", of=("bhī",), before=("sārvadhātuka",),
        result=("kṅit", "hal-ādi"), optional=True,
        keeps_out="बिभ्यति — the affix begins with a vowel; "
                  "बिभेति — neither कित् nor ङित्; भीयते — no "
                  "सार्वधातुक",
        why="भियोऽन्यतरस्याम् — भी takes इ OPTIONALLY before a "
            "consonant-initial कित् or ङित् सार्वधातुक: "
            "**बिभितः / बिभीतः; बिभिथः / बिभीथः; बिभिवः / "
            "बिभीवः; बिभिमः / बिभीमः**"),
    Etva(
        "6.4.116", does="it", of=("hā",), before=("sārvadhātuka",),
        result=("kṅit", "hal-ādi"), optional=True,
        keeps_out="जहति — a vowel-initial affix; जहाति — neither "
                  "कित् nor ङित्; हीयते, जेहीयते — no सार्वधातुक",
        why="जहातेश्च — and जहाति likewise: **जहितः / जहीतः; "
            "जहिथः / जहीथः**. Stated apart for what follows: "
            "**पृथग्योगकरणम् उत्तरार्थम्**"),
    Etva(
        "6.4.117", does="ā", of=("hā",), before=("hi",),
        optional=True,
        why="आ च हौ — and before हि, जहाति takes आ at its end, "
            "and इ optionally beside it: **जहाहि, जहिहि, "
            "जहीहि** — three forms, the आ from this rule, the इ "
            "from 6.4.116 carried down, and the ई from neither"),
    Etva(
        "6.4.118", does="lopa", of=("hā",),
        before=("sārvadhātuka",), result=("kṅit", "ya-ādi"),
        why="लोपो यि — and before a य्-initial कित् or ङित् "
            "सार्वधातुक the आ of जहाति is simply DROPPED: "
            "**जह्यात्, जह्याताम्, जह्युः**"),
    Etva(
        "6.4.119", does="et-abhyāsalopa", gana="ghu", of=("as",),
        before=("hi",),
        why="घ्वसोरेद्धावभ्यासलोपश्च — the घु class and अस् take "
            "ए before हि, and the reduplication goes with it: "
            "**देहि, धेहि**; and for अस्, **एधि**.\\n\\n"
            "**AND अस् GETS THERE BY A DIFFERENT ROAD.** "
            "**अस्तेः श्नसोरल्लोपः इत्यकारलोपः** — 6.4.111 has "
            "already taken its अ, so what this rule gives it is "
            "the ए and the loss of the copy. And the loss is a "
            "शित्: **शिदयं लोपः। तेन सर्वस्याभ्यासस्य भवति** — so "
            "1.1.55 makes it take the WHOLE reduplicated syllable "
            "and not merely its last sound"),
    Etva(
        "6.4.120", does="et-abhyāsalopa", before=("liṭ",),
        result=("kṅit",),
        excludes=("ādeś-ādi", "anekahal-madhya", "dīrgha"),
        keeps_out="दिदिवतुः, दिदिवुः — the अ is not the only "
                  "vowel; ररासे, ररासाते — the tapara wants a "
                  "SHORT अ; शश्रमिथ — two consonants on one side",
        why="अत एकहल्मध्येऽनादेशादेर्लिटि — where a stem does NOT "
            "begin with a substitute, and a short अ stands "
            "BETWEEN TWO SINGLE CONSONANTS, the perfect makes "
            "that अ an ए and drops the reduplication: **रेणतुः, "
            "रेणुः; येमतुः, येमुः; पेचतुः, पेचुः; देमतुः, "
            "देमुः**.\\n\\n"
            "**AND ONE RULE DOES TWO THINGS AT ONCE.** The vowel "
            "is replaced AND the copied syllable is deleted, and "
            "neither happens without the other. This is why the "
            "Sanskrit perfect of a light root looks nothing like "
            "a reduplication: पेचुः is what पपचुः became"),
    Etva(
        "6.4.121", does="et-abhyāsalopa", before=("thal",),
        result=("seṭ",),
        excludes=("ādeś-ādi", "anekahal-madhya", "dīrgha"),
        keeps_out="पपक्थ — the थल् has no इट्; दिदेविथ — the "
                  "vowel is not अ; शश्रमिथ, तत्सरिथ — two "
                  "consonants on one side",
        why="थलि च सेटि — and the same before थल् WITH an इट्: "
            "**पेचिथ, शेकिथ**.\\n\\n"
            "**AND THE WORD थल् IS SAID FOR CLARITY AND NOT FROM "
            "NEED.** **थल्ग्रहणं विस्पष्टार्थम्। अक्ङिदर्थम् "
            "एतद् वचनम् इत्यन्यस्येटोऽसंभवात्** — the rule is "
            "stated because थल् is not कित्, and no other affix "
            "of the perfect takes an इट् anyway, so naming it "
            "adds only plainness"),
    Etva(
        "6.4.122", does="et-abhyāsalopa",
        of=tuple(one for one, _ in WHY_FOUR_MORE),
        before=("liṭ", "thal"), result=("kṅit", "seṭ"),
        blocks=("6.4.120", "6.4.121"),
        why="तॄफलभजत्रपश्च — and four roots the conditions would "
            "have missed: **तेरतुः, तेरुः, तेरिथ; फेलतुः, फेलुः, "
            "फेलिथ; भेजतुः, भेजुः, भेजिथ; त्रेपे, त्रेपाते, "
            "त्रेपिरे**.\\n\\n"
            "**AND THE VṚTTI SAYS WHY EACH OF THE FOUR IS "
            "NAMED.** **तरतेर् गुणार्थं वचनम्। फलिभजोर् "
            "आदेशाद्यर्थम्। त्रपेर् अनेकहल्मध्यार्थम्** — तॄ for "
            "the guṇa that would have to happen first, फल् and "
            "भज् because they begin with a substitute, and त्रप् "
            "because it has two consonants before the vowel. Four "
            "roots, three different reasons, all in one line"),
    Etva(
        "6.4.123", does="et-abhyāsalopa", of=("rādh",),
        before=("liṭ", "thal"), result=("hiṃsā",),
        blocks=("6.4.120",),
        keeps_out="रराधतुः, रराधुः, रराधिथ — no injury meant",
        why="राधो हिंसायाम् — and राध् where INJURY is meant: "
            "**अपरेधतुः, अपरेधुः, अपरेधिथ**.\\n\\n"
            "**AND THE tapara IS SET ASIDE HERE.** **अत "
            "इत्येतद् इहोपस्थितं तपरत्वकृतम् अपास्य कालविशेषम् "
            "असंभवाद् अवर्णमात्रं प्रतिपादयति** — राध् has a long "
            "आ and no short one, so the tapara that 6.4.120 "
            "carried has to be dropped or the rule would reach "
            "nothing"),
    Etva(
        "6.4.124", does="et-abhyāsalopa", of=OPTIONAL_THREE,
        before=("liṭ", "thal"), optional=True,
        blocks=("6.4.120", "6.4.121"),
        why="वा जॄभ्रमुत्रसाम् — and three roots OPTIONALLY: "
            "**जेरतुः / जजरतुः; जेरिथ / जजरिथ; भ्रेमतुः / "
            "बभ्रमतुः; भ्रेमिथ / बभ्रमिथ; त्रेसतुः / तत्रसतुः; "
            "त्रेसिथ / तत्रसिथ** — each with the copy gone and "
            "each with it kept"),
    Etva(
        "6.4.125", does="et-abhyāsalopa", gana="phaṇādi",
        before=("liṭ", "thal"), optional=True,
        blocks=("6.4.120", "6.4.121"),
        why="फणां च सप्तानाम् — and the seven फणादि roots, also "
            "optionally: **फेणतुः / पफणतुः; रेजतुः / रराजतुः; "
            "भ्रेजे / बभ्राजे**. Seven roots and one option, and "
            "the vṛtti works each pair out"),
    Etva(
        "6.4.126", refuses=True, of=("śas", "dad"), gana="v-ādi",
        blocks=("6.4.120", "6.4.121"),
        why="न शसददवादिगुणानाम् — but not for शस्, not for दद्, "
            "not for the व-initial roots, and not for an अ that "
            "GUṆA made: **विशशसतुः, विशशसुः, विशशसिथ; दददे, "
            "दददाते, दददिरे; ववमतुः, ववमुः, ववमिथ; विशशरतुः, "
            "विशशरुः, विशशरिथ; लुलविथ, पुपविथ**. Four classes "
            "kept out at once, and the last of them is not a "
            "class of roots at all but a class of vowels — an अ "
            "that was not there in the root"),
    Etva(
        "6.4.127", does="tṛ", of=("arvan",),
        excludes=("su", "nañ"),
        keeps_out="अर्वा — a सु follows; अनर्वाणौ, अनर्वाणः — a "
                  "नञ् precedes",
        why="अर्वणस्त्रसावनञः — अर्वन् becomes अर्वत् unless a सु "
            "follows it or a नञ् precedes: **अर्वन्तौ, अर्वन्तः; "
            "अर्वन्तम्, अर्वतः; अर्वता, अर्वद्भ्याम्, "
            "अर्वद्भिः; अर्वती; आर्वतम्**. Two conditions in one "
            "compound, one about what comes after and one about "
            "what comes before"),
    Etva(
        "6.4.128", does="tṛ", of=("maghavan",), bahulam=True,
        why="मघवा बहुलम् — and मघवन् becomes मघवत् VARIOUSLY: "
            "**मघवान्, मघवन्तौ, मघवन्तः; मघवता; मघवती; "
            "माघवतम्**, and **न च भवति — मघवा, मघवानौ, मघवानः; "
            "मघोनः, मघोना, मघवभ्याम्; मघोनी; माघवनम्**. Every "
            "form given twice over, which is what बहुलम् means "
            "here and not an option between two shapes of one "
            "word"),
)


def _reaches(row: Etva, stem: str, gana: str, before: str,
             result: str) -> bool:
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.result and result not in row.result:
        return False
    if row.excludes and (stem in row.excludes
                         or gana in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Etva, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.does and not row.refuses


def _how_specific(row: Etva, stem: str, gana: str) -> int:
    """
    A refusal beats what it refuses, a rule that names what it
    displaces beats it, and a named stem beats a named class.

    6.4.120 reaches every light root in the perfect; 6.4.122 to
    6.4.125 each name stems the conditions would have missed, and
    6.4.126 names three classes out. Nothing but `blocks` orders
    the four against the two they extend.
    """
    return (
        12 * (0 if row.refuses else len(row.blocks))
        + 10 * bool(row.refuses)
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.before)
    )


@dataclass(frozen=True)
class Made:
    """What the run answers: the ए, or the copy, or both."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    bahulam: bool = False
    blocked_by: Tuple[str, ...] = ()


def in_the_perfect(stem: str = "", *, gana: str = "",
                   before: str = "", result: str = "",
                   wants: str = "") -> Made:
    """
    6.4.115–128 — the ए of the perfect and the copy that goes.

    Nothing answers by default: where no rule is reached the
    reduplication stands and the vowel is unchanged, which is what
    पपाच and बभूव are.
    """
    matched = [
        row for row in ETVA_TABLE
        if _reaches(row, stem, gana, before, result)
        and _supplies(row, wants)
    ]
    if not matched:
        return Made(
            "", "", "No rule of 6.4.115–128 is reached, so the "
                    "reduplication stands and the vowel is "
                    "unchanged")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Made("" if row.refuses else row.does, row.sutra, row.why,
                optional=row.optional, bahulam=row.bahulam,
                blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Etva, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ETVA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Etva", "ETVA_TABLE", "ABHYASA_RUN", "FOUR_CONDITIONS",
    "WHY_FOUR_MORE", "OPTIONAL_THREE", "PHANADI", "NO_ETVA",
    "Made", "in_the_perfect", "provisions_for",
]
