# -*- coding: utf-8 -*-
"""
Two paribhāṣās outside adhyāya 1 — 2.1.1 and 3.1.94.

    2.1.1   समर्थः पदविधिः      every rule about words wants them connected
    3.1.94  वासरूपोऽस्त्रियाम्   and in the kṛt section an exception may only
                                 optionally displace its rule

The second of the two is the more consequential for anything that resolves
rules against each other. 1.4.2's Kāśikā laid down that an अपवाद beats the
उत्सर्ग it excepts, invariably and whatever the order — and `vipratisedha`
carries that. This sūtra suspends it for one large stretch of the grammar: in
the kṛt section, an exception of *dissimilar form* displaces its general rule
only optionally, so both affixes stand and both forms are correct.

The Kāśikā gives the limits of that suspension, and both are worth having:

  * असरूप इति किम्? An exception of the *same* form still blocks invariably,
    and सारूप्य is measured after the anubandhas are set aside —
    नानुबन्धकृतम् असारूप्यम्. That is why 3.2.1's अण् and 3.2.3's क are
    counted alike, both reducing to अ, and the second blocks outright.
  * अस्त्रियाम् किम्? Nor does it hold in the feminine section: 3.3.94's
    क्तिन् is displaced by 3.3.102's अ invariably, and चिकीर्षा is the only
    form.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

#: 3.1.94's field is the कृत् section, which begins at 3.1.91 धातोः and runs
#: to 3.4.117 — the same adhikāra `reading.adhikara` already records.
KRT_FROM, KRT_TO = "3.1.91", "3.4.117"

#: And the स्त्री section it excepts, 3.3.94 onwards, where the ordinary
#: invariable displacement holds.
STRI_FROM, STRI_TO = "3.3.94", "3.3.112"


def _order(sutra: str) -> Tuple[int, ...]:
    return tuple(int(p) for p in sutra.split(".") if p.isdigit())


@dataclass(frozen=True)
class Samartha:
    """Whether a rule about words reaches this pair of them."""

    applies: bool
    by: str
    why: str


def samartha(
    *,
    connected: Optional[bool] = None,
    padavidhi: bool = True,
) -> Samartha:
    """
    2.1.1 समर्थः पदविधिः — every rule about words wants them connected.

    परिभाषेयम्। यः कश्चिद् इह शास्त्रे पदविधिः श्रूयते स सर्वः समर्थो वेदितव्यः.
    The Kāśikā offers the condition two ways: समर्थः शक्तः, able to convey what
    the analytic phrase conveys; or, taking the word as a bahuvrīhi, a rule
    about words that are themselves connected — सम्बद्धार्थानां संसृष्टार्थानां.

    Its counter-examples all have the same shape: two words standing next to
    each other across a break, with no relation between them. कष्टं श्रितः
    compounds; पश्य देवदत्त कष्टम्, श्रितो विष्णुमित्रो गुरुकुलम् does not,
    though कष्टम् and श्रितः are adjacent.

    **And it reaches no वर्णविधि.** पदग्रहणं किम्? वर्णविधौ समर्थपरिभाषा मा
    भूत् — the yaṇ substitution and the tuk happen between unconnected words
    just as readily, which is why तिष्ठतु दध्यशान and तिष्ठतु कुमारीच्छत्रम्
    come out as they do. That limit is the reason the sūtra says पद at all.
    """
    if not padavidhi:
        return Samartha(
            True, "2.1.1",
            "पदग्रहणं किम्? वर्णविधौ समर्थपरिभाषा मा भूत् — this is an "
            "operation on sounds and not on words, so the condition does not "
            "reach it: तिष्ठतु दध्यशान त्वं शाकेन, where the yaṇ comes "
            "between words with nothing to do with each other, and तिष्ठतु "
            "कुमारीच्छत्रं हर देवदत्तात्, where the tuk does.",
        )
    if connected is None:
        return Samartha(
            False, "2.1.1",
            "समर्थः पदविधिः — whether the two words are connected in sense "
            "has not been stated, and no rule about words applies until it "
            "is. It is a fact about the utterance, not about the forms.",
        )
    if connected:
        return Samartha(
            True, "2.1.1",
            "समर्थः पदविधिः — the two are connected, so the rule reaches "
            "them: कष्टं श्रितः, कष्टश्रितः.",
        )
    return Samartha(
        False, "2.1.1",
        "समर्थग्रहणं किम्? The two words stand next to each other and have "
        "nothing to do with each other, so no rule about words reaches them: "
        "पश्य देवदत्त कष्टम्, श्रितो विष्णुमित्रो गुरुकुलम्.",
    )


@dataclass(frozen=True)
class Displacement:
    """Whether an exception displaces its general rule, and how completely."""

    displaces: bool
    optional: bool
    by: str
    why: str


def _strip_anubandhas(affix: str) -> str:
    """
    What is left of an affix once its indicatory letters are set aside.

    नानुबन्धकृतम् असारूप्यम् — a difference made by anubandhas alone is no
    difference of form. The it-analysis of 1.3.2–1.3.9 is what finds them, and
    it is already codified, so it is called rather than repeated.
    """
    from src.astadhyayi.itsamjna import PRATYAYA, analyze

    return analyze(affix, PRATYAYA).stem


def displaces(
    *,
    utsarga: str,
    apavada: str,
    utsarga_affix: Optional[str] = None,
    apavada_affix: Optional[str] = None,
) -> Displacement:
    """
    3.1.94 वासरूपोऽस्त्रियाम् — how completely an exception displaces its rule.

    Outside the kṛt section, and inside the feminine part of it, an अपवाद
    displaces its उत्सर्ग outright; that is 1.4.2's doctrine and
    `vipratisedha` carries it. Within 3.1.91–3.4.117 and outside 3.3.94
    onwards, this sūtra makes the displacement optional where the two affixes
    differ in form — so both stand, and both forms are correct.

    असरूप is measured after the anubandhas are discounted, which is why 3.2.1
    अण् and 3.2.3 क count as alike: both are अ once the ण् and the क् are set
    aside, so the exception blocks invariably and गोदः is the only form.
    """
    def _in(sutra, first, last):
        return _order(first) <= _order(sutra) <= _order(last)

    # Both must stand in the kṛt section: the sūtra is read under 3.1.91
    # धातोः, so it says nothing about a pair outside it — nor about a pair
    # straddling its edge, which is why the utsarga is checked too.
    inside_krt = (_in(apavada, KRT_FROM, KRT_TO)
                  and _in(utsarga, KRT_FROM, KRT_TO))
    inside_stri = _in(apavada, STRI_FROM, STRI_TO)

    if not inside_krt:
        return Displacement(
            True, False, "1.4.2",
            f"{apavada} and {utsarga} do not both stand in the kṛt section, "
            f"so the ordinary "
            f"doctrine holds: an अपवाद displaces its उत्सर्ग outright, and "
            f"1.4.2 does not reach the case — उत्सर्गापवादयोः तुल्यबलता "
            f"नास्ति.",
        )
    if inside_stri:
        return Displacement(
            True, False, "3.1.94",
            "अस्त्रियामिति किम्? In the feminine section the displacement is "
            "invariable after all: 3.3.94's क्तिन् is displaced by 3.3.102's "
            "अ outright, and चिकीर्षा, जिहीर्षा are the only forms.",
        )

    if utsarga_affix and apavada_affix:
        if _strip_anubandhas(utsarga_affix) == _strip_anubandhas(apavada_affix):
            return Displacement(
                True, False, "3.1.94",
                f"असरूप इति किम्? {utsarga_affix} and {apavada_affix} are of "
                f"the same form once their anubandhas are set aside — "
                f"नानुबन्धकृतम् असारूप्यम् — so the exception blocks "
                f"invariably: गोदः, कम्बलदः, and no *गायकः beside them.",
            )

    return Displacement(
        True, True, "3.1.94",
        "वासरूपोऽस्त्रियाम् — in the kṛt section an exception of dissimilar "
        "form displaces its rule only optionally, so both affixes stand: "
        "3.1.135's क beside 3.1.133's ण्वुल् and तृच्, giving विक्षिपः, "
        "विक्षेपकः and विक्षेप्ता all three.",
    )


__all__ = [
    "Displacement",
    "KRT_FROM",
    "KRT_TO",
    "STRI_FROM",
    "STRI_TO",
    "Samartha",
    "displaces",
    "samartha",
]
