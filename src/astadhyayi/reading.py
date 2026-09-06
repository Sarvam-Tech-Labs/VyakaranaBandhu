# -*- coding: utf-8 -*-
"""
Two rules about how a rule is read — 1.3.10 and 1.3.11.

    1.3.10  यथासंख्यमनुदेशः समानाम्   equal lists correspond in order
    1.3.11  स्वरितेनाधिकारः            a svarita marks a governing heading

They sit together because both are about the text rather than about language,
and both are invisible in the written sūtra. 1.3.10 governs how two lists in
one rule line up; 1.3.11 says that a word is a heading — governing every sūtra
after it until its scope runs out — and that the mark saying so is a svarita
that the manuscripts do not write.

`nirdesa` in adesa.py is the third rule of this kind, reading a word's case to
decide where an operation lands. It lives there because it is inseparable from
substitution; these two are not tied to any one operation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple

from src.astadhyayi.sources import all_sutra_ids, facts


# ---------------------------------------------------------------------------
# 1.3.10 यथासंख्यमनुदेशः समानाम्
# ---------------------------------------------------------------------------


def yathasamkhya(
    uddesin: Sequence[str], anudesin: Sequence[str]
) -> Optional[Tuple[Tuple[str, str], ...]]:
    """
    Pair two lists in a rule, in order — but only when they are the same length.

    संख्याशब्देनात्र क्रमो लक्ष्यते: the word "number" here indicates ORDER, and
    the Kāśikā spells the condition out — समानां समसंख्यानां समं परिपठितानाम्,
    of equal number and equally enumerated. Then प्रथमात् प्रथमः, द्वितीयाद्
    द्वितीयः: the first with the first, the second with the second.

    4.3.94 तूदीशलातुरवर्मतीकूचवाराड् ढक्छण्ढञ्यकः names four places and four
    affixes, so they pair off: तौदेयः, शालातुरीयः, वार्मतेयः, कौचवार्यः.

    समानामिति किम्? 1.4.90 लक्षणेत्थंभूताख्यानभागवीप्सासु प्रतिपर्यनवः gives
    five senses against three words. Unequal, so no respective pairing — each
    of the three holds for any of the five. Returning None rather than a
    truncated zip is the whole point: a silent `zip` would drop two senses and
    give an answer that looks right.
    """
    if len(uddesin) != len(anudesin) or not uddesin:
        return None
    return tuple(zip(uddesin, anudesin))


def pairs_respectively(sutra_id: str, first: Sequence[str],
                       second: Sequence[str]) -> bool:
    """Whether this sūtra's two lists are of equal number, and so pair off."""
    return yathasamkhya(first, second) is not None


# ---------------------------------------------------------------------------
# 1.3.11 स्वरितेनाधिकारः
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Adhikara:
    """A heading, and how far its authority runs."""

    sutra_id: str
    devanagari: str
    label: str
    ends_at: Optional[str]

    @property
    def governs_to_end(self) -> bool:
        """A heading with no recorded end runs to the end of the text."""
        return self.ends_at is None


def _key(sutra_id: str) -> Tuple[int, int, int]:
    return tuple(int(part) for part in sutra_id.split("."))    # type: ignore


def adhikara(sutra_id: str) -> Optional[Adhikara]:
    """
    Is this sūtra a heading, and how far does it reach?

    स्वरितो नाम स्वरविशेषो वर्णधर्मः। तेन चिह्नेनाधिकारो वेदितव्यः — a svarita
    is a quality of a sound, and by that mark a heading is known. The mark is
    not written: प्रतिज्ञास्वरिताः पाणिनीयाः, the Pāṇinīyas hold the svarita by
    declaration, exactly as they hold the anunāsika of 1.3.2.

    So the mark cannot be read off the text, and the scope has to come from the
    tradition. The corpus carries it: it records a type and a scope-end for each
    heading, and the six the Kāśikā names — 3.1.1, 3.1.91, 4.1.1, 6.4.1,
    6.4.129, 8.1.16 — are all there.
    """
    fact = facts(sutra_id)
    label = fact.type_label or ""
    if "अधिकार" not in label and not fact.scope_end:
        return None
    return Adhikara(
        sutra_id=sutra_id,
        devanagari=fact.devanagari,
        label=label,
        ends_at=fact.scope_end,
    )


def is_adhikara(sutra_id: str) -> bool:
    return adhikara(sutra_id) is not None


def governs(sutra_id: str) -> Tuple[str, ...]:
    """Every sūtra a heading's authority reaches, itself included."""
    heading = adhikara(sutra_id)
    if heading is None:
        return ()
    start = _key(sutra_id)
    end = _key(heading.ends_at) if heading.ends_at else None
    return tuple(
        other for other in all_sutra_ids()
        if start <= _key(other) and (end is None or _key(other) <= end)
    )


def headings_over(sutra_id: str) -> Tuple[str, ...]:
    """
    The headings in force where this sūtra stands.

    Read from the corpus's own record rather than by scanning every heading's
    range — the corpus marks, for each of the 3,498 sūtras that fall under one,
    which heading it is under.
    """
    return tuple(item.sutra for item in facts(sutra_id).adhikara)


def all_adhikaras() -> Tuple[Adhikara, ...]:
    """Every heading in the text, in order."""
    found: List[Adhikara] = []
    for sutra_id in all_sutra_ids():
        heading = adhikara(sutra_id)
        if heading is not None:
            found.append(heading)
    return tuple(found)


__all__ = [
    "Adhikara",
    "adhikara",
    "all_adhikaras",
    "governs",
    "headings_over",
    "is_adhikara",
    "pairs_respectively",
    "yathasamkhya",
]
