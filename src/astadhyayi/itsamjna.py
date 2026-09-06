# -*- coding: utf-8 -*-
"""
इत् — the indicatory letters, 1.3.2 to 1.3.9.

An upadeśa form carries letters that are not part of it. They say how the form
behaves and then disappear. Eight sūtras decide which letters those are:

    1.3.2  उपदेशेऽजनुनासिक इत्     a nasalised vowel, in upadeśa
    1.3.3  हलन्त्यम्                a final consonant
    1.3.4  न विभक्तौ तुस्माः        but not t-varga, s or m in a vibhakti
    1.3.5  आदिर्ञिटुडवः            initial ñi, ṭu, ḍu
    1.3.6  षः प्रत्ययस्य            initial ṣ of an affix
    1.3.7  चुटू                     initial c-varga or ṭ-varga of an affix
    1.3.8  लशक्वतद्धिते             initial l, ś or k-varga of a non-taddhita affix
    1.3.9  तस्य लोपः                and the it is dropped

Every one of them is conditioned on उपदेशे, carried down from 1.3.2 by
anuvṛtti — the corpus records it as such for 1.3.3 through 1.3.8. Outside the
enunciation there are no it-letters at all: अग्निचित् ends in t and keeps it.
That is why `Upadesa` has to be constructed deliberately; there is no function
here that takes a running word and strips letters off it.

The analysis reports which sūtra marked each letter, because the sūtras
disagree in instructive ways — 1.3.4 exists only to stop 1.3.3, and जस् shows
both at once: the j goes by 1.3.7 and the s stays by 1.3.4.

What this unblocks: `adesa.Adesa.its` was until now supplied by hand, with a
note saying it could not be derived without these rules. It can now.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet, List, Optional, Tuple

from src.chandas.core import scan_phonemes
from src.astadhyayi.varna import ANUNASIKA_MARK, VARGA


# ---------------------------------------------------------------------------
# What kind of thing is being enunciated
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Context:
    """
    What the form is, since half the rules ask.

    A vibhakti and a taddhita are both affixes, so those two imply `pratyaya`
    and the constructor does not make the caller say it twice.
    """

    pratyaya: bool = False
    vibhakti: bool = False
    taddhita: bool = False
    dhatu: bool = False

    def __post_init__(self) -> None:
        if self.vibhakti or self.taddhita:
            object.__setattr__(self, "pratyaya", True)


DHATU = Context(dhatu=True)
PRATYAYA = Context(pratyaya=True)
VIBHAKTI = Context(vibhakti=True)
TADDHITA = Context(taddhita=True)
PLAIN = Context()


# ---------------------------------------------------------------------------
# The letters the ādi rules look for
# ---------------------------------------------------------------------------

#: 1.3.5 आदिर्ञिटुडवः — three two-letter openings, not three letters. That
#: matters twice over: ñ alone would otherwise be caught by 1.3.7, and 1.3.9
#: has to drop both letters, which is why it says तस्य and not अलः.
NITUDU: Tuple[str, ...] = ("ñi", "ṭu", "ḍu")

#: 1.3.4 न विभक्तौ तुस्माः — tu (the t-varga), s, m.
TUSMA: FrozenSet[str] = frozenset(VARGA["tu"]) | {"s", "m"}

#: 1.3.7 चुटू — the c-varga and the ṭ-varga.
CUTU: FrozenSet[str] = frozenset(VARGA["cu"]) | frozenset(VARGA["ṭu"])

#: 1.3.8 लशक्वतद्धिते — l, ś, and the k-varga.
LASAKU: FrozenSet[str] = frozenset(VARGA["ku"]) | {"l", "ś"}


# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ItMark:
    """One indicatory letter, where it sat, and which sūtra marked it."""

    letters: str
    start: int
    end: int
    by: str
    why: str


@dataclass(frozen=True)
class Upadesa:
    """A form as enunciated, with its it-letters found and removed."""

    form: str
    context: Context
    its: Tuple[ItMark, ...] = ()
    #: What is left after 1.3.9 तस्य लोपः.
    stem: str = ""

    @property
    def it_letters(self) -> FrozenSet[str]:
        """The bare it-letters, for callers that only want the anubandhas."""
        return frozenset(
            mark.letters.rstrip(ANUNASIKA_MARK) or mark.letters
            for mark in self.its
        )

    def marked_with(self, letter: str) -> bool:
        """Is this form ṅit, śit, ñit...?"""
        return letter in self.it_letters

    def by(self, sutra_id: str) -> Tuple[ItMark, ...]:
        return tuple(m for m in self.its if m.by == sutra_id)


# ---------------------------------------------------------------------------
# The analysis
# ---------------------------------------------------------------------------


def analyze(form: str, context: Context = PLAIN) -> Upadesa:
    """
    Find the it-letters of an upadeśa form and remove them.

    The order below is the order the rules constrain each other in, not the
    order they are numbered:

      1.3.5 first among the initial rules, because ñi and ṭu and ḍu are two
        letters each and ñ and ṭ would otherwise be taken singly by 1.3.7.
      1.3.3 then 1.3.4, since 1.3.4 is a prohibition on what 1.3.3 would
        otherwise reach — पूर्वेण प्राप्तायामित्संज्ञायां ... प्रतिषेध उच्यते.
      1.3.2 is independent of both; a nasalised vowel can sit anywhere.

    Nothing is stripped from a form that is not an upadeśa. There is no
    argument for that here because `Context` cannot express it: constructing an
    `Upadesa` at all is the claim that the form is one.
    """
    marks: List[ItMark] = []
    phonemes = scan_phonemes(form)
    claimed = set()

    def claim(start: int, end: int) -> bool:
        span = set(range(start, end))
        if span & claimed:
            return False
        claimed.update(span)
        return True

    # --- 1.3.5 आदिर्ञिटुडवः -------------------------------------------------
    for opening in NITUDU:
        if form.startswith(opening) and claim(0, len(opening)):
            marks.append(ItMark(
                opening, 0, len(opening), "1.3.5",
                f"आदिर्ञिटुडवः — the opening {opening} is indicatory entire, "
                f"and 1.3.9 drops both letters",
            ))
            break

    # --- the single-letter ādi rules ---------------------------------------
    if phonemes:
        first = phonemes[0]
        rule: Optional[Tuple[str, str]] = None
        if context.pratyaya and first.text == "ṣ":
            rule = ("1.3.6", "षः प्रत्ययस्य — an affix's initial ṣ")
        elif context.pratyaya and first.text in CUTU:
            rule = ("1.3.7", "चुटू — an affix's initial c-varga or ṭ-varga")
        elif (
            context.pratyaya
            and not context.taddhita
            and first.text in LASAKU
        ):
            rule = (
                "1.3.8",
                "लशक्वतद्धिते — l, ś or k-varga opening an affix that is not "
                "a taddhita",
            )
        if rule and claim(first.start, first.start + len(first.text)):
            marks.append(ItMark(
                first.text, first.start, first.start + len(first.text),
                rule[0], rule[1],
            ))

    # --- 1.3.3 हलन्त्यम्, with 1.3.4 न विभक्तौ तुस्माः ----------------------
    if phonemes:
        last = phonemes[-1]
        if last.kind == "consonant":
            if context.vibhakti and last.text in TUSMA:
                pass    # 1.3.4 forbids it
            elif claim(last.start, last.start + len(last.text)):
                marks.append(ItMark(
                    last.text, last.start, last.start + len(last.text),
                    "1.3.3", "हलन्त्यम् — the final consonant of an upadeśa",
                ))

    # --- 1.3.2 उपदेशेऽजनुनासिक इत् -----------------------------------------
    for phoneme in phonemes:
        if phoneme.kind != "vowel":
            continue
        end = phoneme.start + len(phoneme.text)
        nasal = form[end:end + len(ANUNASIKA_MARK)] == ANUNASIKA_MARK
        if not nasal:
            continue
        end += len(ANUNASIKA_MARK)
        if claim(phoneme.start, end):
            marks.append(ItMark(
                form[phoneme.start:end], phoneme.start, end, "1.3.2",
                "उपदेशेऽजनुनासिक इत् — a nasalised vowel in the enunciation. "
                "The nasality is not written in the sūtras themselves; "
                "प्रतिज्ञानुनासिक्याः पाणिनीयाः, the Pāṇinīyas hold it by "
                "declaration, and the dhātupāṭha marks it.",
            ))

    marks.sort(key=lambda m: m.start)
    return Upadesa(
        form=form,
        context=context,
        its=tuple(marks),
        stem=lopa(form, marks),
    )


def lopa(form: str, marks: List[ItMark]) -> str:
    """
    1.3.9 तस्य लोपः — the it is dropped.

    तस्य is deliberate. The Kāśikā says "तस्य"ग्रहणं सर्वलोपार्थम्, अलोऽन्त्यस्य
    मा भूत् — the word is there so that the WHOLE of the it goes, and 1.1.52
    does not cut it down to the last sound. Without it, आदिर्ञिटुडवः would drop
    only the i of ñi. So this removes each marked span entire, and that is a
    codified interaction with 1.1.52 rather than a convenience.
    """
    out, cursor = [], 0
    for mark in sorted(marks, key=lambda m: m.start):
        out.append(form[cursor:mark.start])
        cursor = mark.end
    out.append(form[cursor:])
    return "".join(out)


def its_of(form: str, context: Context = PLAIN) -> FrozenSet[str]:
    """The it-letters alone — what `adesa.Adesa` wants."""
    return analyze(form, context).it_letters


def stem_of(form: str, context: Context = PLAIN) -> str:
    """The form with its it-letters gone."""
    return analyze(form, context).stem


def strip_its(form: str, *, dhatu: bool = True, pratyaya: bool = False,
              vibhakti: bool = False, taddhita: bool = False) -> str:
    """
    1.3.9 तस्य लोपः, over a whole enunciated form — what the playground can
    drive.

    `lopa` takes the ItMark spans `analyze` found, which no web form can hand
    back. This does the two steps together: find the marks, then drop them.
    डुकृञ् comes out कृ, and the whole marked span goes and not merely its
    last letter — 1.3.9's तस्य is the it-saṃjñā's bearer entire.
    """
    context = Context(pratyaya=pratyaya, vibhakti=vibhakti,
                      taddhita=taddhita, dhatu=dhatu)
    return lopa(form, analyze(form, context).its)


__all__ = [
    "strip_its",
    "CUTU",
    "Context",
    "DHATU",
    "ItMark",
    "LASAKU",
    "NITUDU",
    "PLAIN",
    "PRATYAYA",
    "TADDHITA",
    "TUSMA",
    "Upadesa",
    "VIBHAKTI",
    "analyze",
    "its_of",
    "lopa",
    "stem_of",
]
