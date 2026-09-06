# -*- coding: utf-8 -*-
"""
स्थानिवद्भाव — when a substitute counts as what it replaced. 1.1.56 to 1.1.59.

    1.1.56  स्थानिवदादेशोऽनल्विधौ   a substitute is like the substituend,
                                      except where the operation rests on sounds
    1.1.57  अचः परस्मिन् पूर्वविधौ   and a vowel-substitute is so even then,
                                      when caused by what follows and the
                                      operation falls on what precedes
    1.1.58  न पदान्त...               but not for these ten operations
    1.1.59  द्विर्वचनेऽचि             and yet, for reduplication, it is

An exception, an exception to it, and an exception to that. The four have to be
read as one decision, and in an order that is not their numbering: 1.1.59
re-admits reduplication, which 1.1.58 has just excluded, which 1.1.57 had just
allowed, which 1.1.56 had just forbidden.

The motive is stated at the head of the block: स्थान्यादेशयोः पृथक्त्वात्
स्थान्याश्रयं कार्यमादेशे न प्राप्नोतीत्ययमतिदेश आरभ्यते — substituend and
substitute being two things, an operation resting on the one would not reach
the other, so this atideśa is begun. स्थानिना तुल्यं वर्तत इति स्थानिवत्.

1.1.57 is worth reading for its case marking alone. The Kāśikā gives each of
its three words a different reading: अच इति स्थानिनिर्देशः, the genitive names
the substituend by 1.1.49; परस्मिन्निति निमित्तसप्तमी, a locative of cause;
पूर्वविधाविति विषयसप्तमी, a locative of scope. Three cases, three senses, one
sūtra — and only the first is the one 1.1.66 would have supplied.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet

from src.astadhyayi.operations import check_group, resolve


#: 1.1.58's ten. The compound is one long dvandva —
#: पदान्त-द्विर्वचन-वरे-यलोप-स्वर-सवर्ण-अनुस्वार-दीर्घ-जश्-चर्-विधिषु — and the
#: corpus's padaccheda splits it exactly so, which is where these come from.
#: Checked against the vocabulary at import, so a typo here fails on the
#: first import rather than the first time a reader asks about it.
EXCLUDED: FrozenSet[str] = frozenset({
    "padānta",      # कौ स्तः, यौ स्तः, तानि सन्ति
    "dvirvacana",   # दद्ध्यत्र, मद्ध्वत्र — but see 1.1.59
    "vare",         # अप्सु यायावरः
    "yalopa",
    "svara",
    "savarṇa",
    "anusvāra",
    "dīrgha",
    "jaś",
    "car",
})

check_group(EXCLUDED, "1.1.58's excluded operations")


@dataclass(frozen=True)
class Sthanivat:
    """Whether the substitute counts as the substituend, and on what authority."""

    applies: bool
    by: str
    why: str
    #: 1.1.59 alone is an atideśa of form and lasts only for the operation it
    #: enables — रूपातिदेशश्चायं नियतकालः.
    provisional: bool = False


def sthanivat(
    *,
    al_vidhi: bool = False,
    operation: str = "",
    sthanin_is_vowel: bool = False,
    caused_by_following: bool = False,
    purva_vidhi: bool = False,
    dvirvacana_caused_by_vowel: bool = False,
) -> Sthanivat:
    """
    Whether a substitute is treated as what it replaced, here.

    The order below is the order the four sūtras override one another, not
    their numbering. 1.1.59 goes first because it is the innermost exception:
    it re-admits reduplication after 1.1.58 has excluded it.

    `al_vidhi` is the pivot. An operation that rests on a sound as a sound is an
    अल्विधि, and 1.1.56 shuts sthānivadbhāva out of those — न अल्विधिरनल्विधिः.
    1.1.57 then lets vowel-substitutes back in under three conditions, and it
    exists for exactly that: अल्विध्यर्थमिदमारभ्यते.
    """
    # 1.1.59 द्विर्वचनेऽचि — the innermost exception.
    # Refuses a name that is not an operation, rather than taking the
    # other branch: `dirgha` for `dīrgha` used to answer True by 1.1.57.
    named = resolve(operation)

    if named is not None and named.name == "dvirvacana" \
            and dvirvacana_caused_by_vowel:
        return Sthanivat(
            True, "1.1.59",
            "द्विर्वचनेऽचि — a vowel-substitute counts as the vowel it "
            "replaced when a vowel occasions reduplication, and for the "
            "reduplication only: पपतुः, पपुः after the ā of 6.4.64 is elided; "
            "जघ्नतुः after the upadhā-lopa of 6.4.98 leaves nothing to "
            "reduplicate; आटिटत् after the ṇi-lopa",
            provisional=True,
        )

    # 1.1.56 स्थानिवदादेशोऽनल्विधौ — the general grant.
    if not al_vidhi:
        return Sthanivat(
            True, "1.1.56",
            "स्थानिवदादेशोऽनल्विधौ — the operation does not rest on sounds, so "
            "the substitute is treated as the substituend: धात्वादेशो धातुवद् "
            "भवति, so भू replacing अस् by 2.4.52 still counts as a root for "
            "3.1.91 and gives भविता, भवितुम्, भवितव्यम्",
        )

    # 1.1.57 अचः परस्मिन् पूर्वविधौ — the way back in, for al-vidhi.
    if sthanin_is_vowel and caused_by_following and purva_vidhi:
        if named is not None and named.name in EXCLUDED:
            return Sthanivat(
                False, "1.1.58",
                f"न ... {named.devanagari}विधिषु — one of the ten "
                f"operations the "
                f"sūtra names, so 1.1.57 does not reach it: कौ स्तः for "
                f"padānta, दद्ध्यत्र for dvirvacana",
            )
        return Sthanivat(
            True, "1.1.57",
            "अचः परस्मिन् पूर्वविधौ — a vowel-substitute occasioned by what "
            "follows, for an operation on what precedes: पटयति, where the "
            "ṭi-lopa counts as present and 7.2.116 अत उपधायाः therefore does "
            "not lengthen; अवधीत्, where it blocks 7.2.7",
        )

    return Sthanivat(
        False, "1.1.56",
        "अनल्विधौ — the operation rests on sounds and the three conditions of "
        "1.1.57 are not all met, so the substitute is only itself",
    )


def is_sthanivat(**conditions) -> bool:
    return sthanivat(**conditions).applies


__all__ = ["EXCLUDED", "Sthanivat", "is_sthanivat", "sthanivat"]
