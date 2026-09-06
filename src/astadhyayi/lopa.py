# -*- coding: utf-8 -*-
"""
लोप — disappearance, and what survives it. 1.1.60 to 1.1.63.

    1.1.60  अदर्शनं लोपः                 non-appearance is called lopa
    1.1.61  प्रत्ययस्य लुक्श्लुलुपः       an affix's, named luk, ślu or lup
    1.1.62  प्रत्ययलोपे प्रत्ययलक्षणम्   what the affix conditioned still applies
    1.1.63  न लुमताङ्गस्य                 except to the aṅga, after a lu-word

The pair 1.1.62–1.1.63 is the substance. An affix can disappear and still leave
its work behind: अग्निचित् keeps the name pada although the sup that earned it
by 1.4.14 is gone. The Kāśikā puts the motive plainly — प्रत्ययनिमित्तं
कार्यमसत्यपि प्रत्यये कथं नु नाम स्यादिति सूत्रमिदमारभ्यते, "so that an
operation occasioned by an affix may somehow hold even when the affix is not
there, this rule is begun."

1.1.63 then takes it back in one case, and the two words that limit it are both
tested by the Kāśikā. Between them they decide whether गर्ग takes vṛddhi.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Optional


class Elision(Enum):
    """
    The kinds of disappearance the grammar distinguishes.

    1.1.60 names the general case and 1.1.61 gives three special names for an
    affix's. The Kāśikā insists the three do not blur into one another:
    अनेकसंज्ञाविधानाच् च तद्भावितग्रहणमिह विज्ञायते ... तेन संज्ञानां संकरो न
    भवति — each name reaches only the elision that rule itself prescribed. So
    these are distinct members and not aliases.
    """

    LOPA = "lopa"       # 1.1.60, the general term
    LUK = "luk"         # 1.1.61
    SLU = "ślu"         # 1.1.61
    LUP = "lup"         # 1.1.61


#: The three whose names contain lu — लुमता in 1.1.63. This is why the sūtra
#: says "by a word having lu" rather than listing them: luk, ślu and lup are
#: exactly the elisions named with that syllable, and a plain lopa is not.
LUMAT: FrozenSet[Elision] = frozenset(
    {Elision.LUK, Elision.SLU, Elision.LUP}
)


def is_lumat(elision: Elision) -> bool:
    """1.1.63's लुमता: was the elision prescribed by a lu-word?"""
    return elision in LUMAT


def names_of_affix_elision() -> FrozenSet[Elision]:
    """1.1.61: the three names an affix's disappearance can bear."""
    return LUMAT


@dataclass(frozen=True)
class Laksana:
    """Whether an affix's conditioning survives its elision, and by which rule."""

    survives: bool
    by: str
    why: str


def pratyaya_laksana(elision: Elision, *, anga: bool = False) -> Laksana:
    """
    1.1.62 with 1.1.63: does an operation occasioned by an elided affix hold?

    Yes by 1.1.62, unless the operation is on the aṅga and the elision was by a
    lu-word, in which case 1.1.63 refuses it. Both restrictions in 1.1.63 are
    real and the Kāśikā tests each:

        लुमतेति किम्? कार्यते। हार्यते।   an ordinary lopa, so 1.1.62 stands
        अङ्गस्येति किम्? पञ्च। सप्त। पयः। साम।   not an aṅga, so it stands too

    and its own examples are गर्गाः, मृष्टः, जुहुतः, where a yaÑ or a śap has
    gone by luk or ślu and the aṅga accordingly takes no guṇa or vṛddhi.
    """
    if anga and is_lumat(elision):
        return Laksana(
            survives=False,
            by="1.1.63",
            why=(
                f"न लुमताङ्गस्य — the elision is {elision.value}, a lu-word, "
                f"and the operation is on the aṅga: गर्गाः, मृष्टः, जुहुतः"
            ),
        )
    if anga:
        return Laksana(
            survives=True,
            by="1.1.62",
            why=(
                "प्रत्ययलक्षणम् — the elision is a plain lopa and not a "
                "lu-word, so 1.1.63 does not reach it: कार्यते, हार्यते"
            ),
        )
    return Laksana(
        survives=True,
        by="1.1.62",
        why=(
            "प्रत्ययलक्षणम् — what the affix occasioned holds although the "
            "affix is gone: अग्निचित् and सोमसुत् are still pada by 1.4.14"
        ),
    )


def adarsana(present: Optional[str]) -> bool:
    """
    1.1.60 अदर्शनं लोपः — non-appearance is lopa.

    Two things the Kāśikā is careful about are carried here. The saṃjñā is of
    the state and not of a word — अर्थस्येयं संज्ञा न शब्दस्य — so this returns
    a fact about an absence rather than naming a string. And the absence must
    be of something that would otherwise have been there:
    प्रसक्तस्यादर्शनं लोपसंज्ञं भवति. `None` is that: a slot with nothing in
    it, as against a slot that was never in question.
    """
    return present is None or present == ""


__all__ = [
    "Elision",
    "LUMAT",
    "Laksana",
    "adarsana",
    "is_lumat",
    "names_of_affix_elision",
    "pratyaya_laksana",
]
