# -*- coding: utf-8 -*-
"""
७.४.१३–२४ — the क of a compound, the अङ् aorist, and शीङ्.

Twelve sūtras in three small groups. 7.4.13–15 shorten a long
vowel before क — ज्ञका, कुमारिका — and then refuse it before
कप् (बहुकुमारीकः) and make the refusal optional for an आप् stem
(बहुखट्वाकः beside बहुखट्वकः). 7.4.16–20 are the अङ् aorist:
ऋ takes guṇa and दृश् becomes दर्श् (अकरत्, अदर्शत्), and three
roots take augments — आस्थत्, अपप्तत्, अवोचत्. 7.4.21–24 are
about य्: शीङ् takes guṇa before a सार्वधातुक (शेते) and अयङ्
before a क्ङित् य् (शय्यते), and ऊह् and इ shorten after a
preverb (समुह्यते, उदियात्).

**AND अवोचत् IS ONE OF THE ODDEST FORMS IN THE LANGUAGE.**
7.4.20 वच उम् gives वच् an उम् before the अङ् aorist, and what
comes out is अवोचत् — a form with no visible relation to its
root, built by an augment inserted in the middle and then merged
with the vowel before it.

**WHAT THIS MODULE DOES NOT DO.** It says what the stem does.
That the aorist takes अङ् at all is 3.1.52's, and the क and कप्
come from 5.3.70 and 5.4.153.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
ANGI_RUN: Tuple[str, str] = ("7.4.13", "7.4.24")

#: Where the run turns from the क to the aorist, and then to य्.
ANGI_FROM: str = "7.4.16"
YI_FROM: str = "7.4.21"

#: 7.4.17–20's four roots, each with its own augment or
#: substitute before अङ्: आस्थत्, अश्वत्, अपप्तत्, अवोचत्.
ANGI_FOUR: Tuple[Tuple[str, str], ...] = (
    ("as", "thuk"), ("śvi", "a"), ("pat", "pum"), ("vac", "um"))


@dataclass(frozen=True)
class Angi:
    """One rule of 7.4.13–24: a shortening, a substitute, an augment."""

    sutra: str
    #: `hrasva`, `guṇa`, `ayaṅ`, or the augment's name — "" if
    #: refused.
    does: str = ""
    #: The roots or stems named outright.
    of: Tuple[str, ...] = ()
    #: The stem class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: The preverb the stem must carry.
    upasarga: str = ""
    #: True where the rule supplies an आगम.
    augment: bool = False
    refuses: bool = False
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ANGI_TABLE: Tuple[Angi, ...] = (
    Angi(
        "7.4.13", does="hrasva", gana="aṇ-anta", before=("ka",),
        keeps_out="गोका, नौका — the vowel is no अण्; राका, धाका "
                  "— Uṇādi forms, and **उणादयो बहुलम्**",
        why="केऽणः — a long अण् vowel shortens before क: "
            "**ज्ञका; कुमारिका; किशोरिका**. And the क reached is "
            "the one WITH its markers, which the refusal in the "
            "next sūtra proves — **न कपि इति प्रतिषेधसामर्थ्यात् "
            "कनोऽपि सानुबन्धकस्य ग्रहणम् इह भवति**"),
    Angi(
        "7.4.14", refuses=True, gana="aṇ-anta", before=("kap",),
        blocks=("7.4.13",),
        why="न कपि — but not before कप्: **बहुकुमारीकः, "
            "बहुवधूकः, बहुलक्ष्मीकः**. And 1.2.48's shortening "
            "does not reach there either, the कप् being added to "
            "the second member before the compound is made — "
            "**स्त्रीप्रत्ययान्तसमासप्रातिपदिकं न भवति**"),
    Angi(
        "7.4.15", does="hrasva", gana="āp-anta", before=("kap",),
        optional=True, blocks=("7.4.14",),
        why="आपोऽन्यतरस्याम् — and for an आप्-final stem the "
            "refusal is only half: **बहुखट्वाकः, बहुखट्वकः; "
            "बहुमालाकः, बहुमालकः**"),
    Angi(
        "7.4.16", does="guṇa", gana="ṛ-varṇa-anta", of=("dṛś",),
        before=("aṅ",),
        why="ऋदृशोऽङि गुणः — an ऋ-final root and दृश् take guṇa "
            "before the अङ् aorist: **शकलाङ्गुष्ठकोऽकरत्; अहं "
            "तेभ्योऽकरं नमः; असरत्, आरत्, जरा**; and for दृश् "
            "**अदर्शत्, अदर्शताम्, अदर्शन्**"),
    Angi(
        "7.4.17", does="thuk", of=("as",), before=("aṅ",),
        augment=True,
        why="अस्यतेस्थुक् — अस् takes the augment थुक् before "
            "अङ्: **आस्थत्, आस्थताम्, आस्थन्**. The अस् meant "
            "is **असु क्षेपणे**, the throwing-root, and not the "
            "अस् of being — this run's four rules each name one "
            "root and give it one thing"),
    Angi(
        "7.4.18", does="a", of=("śvi",), before=("aṅ",),
        why="श्वयतेरः — and श्वि becomes अ: **अश्वत्, अश्वताम्, "
            "अश्वन्**. A substitute and not an augment, unlike "
            "the two rules on either side of it, and the "
            "shortest of the four"),
    Angi(
        "7.4.19", does="pum", of=("pat",), before=("aṅ",),
        augment=True,
        why="पतः पुम् — and पत् takes पुम्: **अपप्तत्, "
            "अपप्तताम्, अपप्तन्**. The म् is a marker and the "
            "प् is what goes in, put before the last vowel by "
            "1.1.47 — so पत् becomes प्पत् and then, with the "
            "reduplication, अपप्तत्"),
    Angi(
        "7.4.20", does="um", of=("vac",), before=("aṅ",),
        augment=True,
        why="वच उम् — and वच् takes उम्: **अवोचत्, अवोचताम्, "
            "अवोचन्**.\\n\\n"
            "**AND WHAT COMES OUT HAS NO VISIBLE RELATION TO ITS "
            "ROOT.** The उम् is put inside the stem by 1.1.47, "
            "the vowels merge, and वच् + अङ् gives अवोचत् — one "
            "of the language's oddest aorists, and the reason it "
            "is odd is stated in three syllables"),
    Angi(
        "7.4.21", does="guṇa", of=("śīṅ",),
        before=("sārvadhātuka",),
        keeps_out="शिश्ये — the perfect, and no सार्वधातुक",
        why="शीङः सार्वधातुके गुणः — शीङ् takes guṇa before a "
            "सार्वधातुक: **शेते, शयाते, शेरते**. 1.1.5 would "
            "have refused it, the endings being ङित्; the sūtra "
            "exists to reach past that refusal, and शिश्ये in "
            "the perfect shows what the root does without it"),
    Angi(
        "7.4.22", does="ayaṅ", of=("śīṅ",), before=("ya-kṅit",),
        keeps_out="शिश्ये — no य्; शेयम् — the affix is not "
                  "क्ङित्",
        why="अयङ् यि क्ङिति — and अयङ् before a क्ङित् affix "
            "beginning with य्: **शय्यते, शाशय्यते, प्रशय्य, "
            "उपशय्य**"),
    Angi(
        "7.4.23", does="hrasva", of=("ūh",), upasarga="upasarga",
        before=("ya-kṅit",),
        keeps_out="ऊह्यते — no preverb; समीह्यते — a different "
                  "root; समूहितम् — no य्; समूह्योऽयमर्थः — the "
                  "affix is not क्ङित्",
        why="उपसर्गाद्ध्रस्व ऊहतेः — ऊह् shortens after a preverb "
            "before a क्ङित् य्: **समुह्यते, समुह्य गतः; "
            "अभ्युह्यते, अभ्युह्य गतः**. And the अण् of 7.4.13 "
            "is still running, so ओह्यते and समोह्यते are out"),
    Angi(
        "7.4.24", does="hrasva", of=("i",), upasarga="upasarga",
        before=("liṅ",),
        keeps_out="ईयात् — no preverb; समेयात् — the vowel is no "
                  "अण्",
        why="एतेर्लिङि — and इ shortens after a preverb in the "
            "optative: **उदियात्, समियात्, अन्वियात्**. The "
            "lengthening of 7.4.25 has already been done and "
            "this undoes it — **आशिषि लिङि अकृत्सार्वधातुकयोः "
            "इति दीर्घत्वे कृते ह्रस्वोऽनेन भवति**"),
)


def _reaches(row: Angi, root: str, gana: str, before: str,
             upasarga: str) -> bool:
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.upasarga and upasarga != row.upasarga:
        return False
    return True


def _how_specific(row: Angi, root: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, a named
    root beats a class, and a named preverb beats both.

    7.4.13 against 7.4.14 and 7.4.15 is what needs the first: one
    shortens before क, one refuses it before कप्, and one makes
    the refusal half.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.of and root in row.of)
        + 6 * bool(row.upasarga)
        + 5 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.before)
    )


@dataclass(frozen=True)
class Done:
    """What the run answers: a change, an augment, or a refusal."""

    does: str
    sutra: str
    why: str
    augment: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def to_the_stem(root: str = "", *, gana: str = "",
                before: str = "", upasarga: str = "") -> Done:
    """
    7.4.13–24 — before क, in the अङ् aorist, and before य्.

    Nothing answers by default. Three small groups of rules, and
    a stem outside all three is untouched.
    """
    matched = [row for row in ANGI_TABLE
               if _reaches(row, root, gana, before, upasarga)]
    if not matched:
        return Done(
            "", "", "No rule of 7.4.13-24 is reached, so nothing "
                    "happens to the stem")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Done("" if row.refuses else row.does, row.sutra,
                row.why, augment=row.augment,
                optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Angi, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ANGI_TABLE if row.sutra == sutra_id)


__all__ = [
    "Angi", "ANGI_TABLE", "ANGI_RUN", "ANGI_FROM", "YI_FROM",
    "ANGI_FOUR", "Done", "to_the_stem", "provisions_for",
]
