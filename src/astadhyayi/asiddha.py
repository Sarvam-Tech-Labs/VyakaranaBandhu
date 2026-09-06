# -*- coding: utf-8 -*-
"""
असिद्धत्व — 8.2.1, 8.2.2, 8.2.3, 6.4.22 and 6.1.86.

1.4.2 विप्रतिषेधे परं कार्यम् settles which of two competing rules is *done*.
These settle something else and more basic: whether a rule that has been done
is **visible** to another rule at all. सिद्धकार्यं न करोतीत्यर्थः — what is
asiddha does not do the work of something accomplished.

    8.2.1   पूर्वत्रासिद्धम्        the last pāda and a quarter, to what precedes
    8.2.2   नलोपः …                 and a narrowing of it
    8.2.3   न मु ने                 and an exception inside that
    6.4.22  असिद्धवदत्राभात्        6.4.22 to 6.4.175, to each other
    6.1.86  षत्वतुकोरसिद्धः         one substitution, to two operations

**8.2.1 runs in two directions at once**, and the Kāśikā states both. The
whole tripādī is asiddha to the सपादसप्ताध्यायी that precedes it — एतस्याम्
अयं पादोनोऽध्यायोऽसिद्धो भवति — *and*, within the tripādī itself, each later
sūtra is asiddha to each earlier one: इत उत्तरं चोत्तर उत्तरो योगः पूर्वत्र
पूर्वत्रासिद्धो भवति. The second is the part that is easy to miss and does
most of the work.

**It has a purpose stated in two halves**: आदेशलक्षणप्रतिषेधार्थम्
उत्सर्गलक्षणभावार्थं च — so that a substitute shall not serve as the cause of
a further operation, and so that what it replaced shall go on serving as one.

**And three things escape it**, each named by the Kāśikā:

  * the case-endings of the tripādī's own sūtras, for 1.1.49, 1.1.66 and
    1.1.67 — कार्यकालं हि संज्ञापरिभाषम्, a paribhāṣā is invoked at the moment
    it is wanted and so is never 'earlier' than anything;
  * an अपवाद, even a later one, when the general rule is in question —
    अपवादस्य तु परस्यापि उत्सर्गे कर्तव्ये वचनप्रामाण्याद् असिद्धत्वं न भवति;
  * and, going the other way, **1.4.2 itself stops working here**. A later
    rule cannot compete with an earlier one it is invisible to: यत् प्रति
    तस्य असिद्धत्वात् न प्रवर्तते. That is the sharpest consequence in the
    whole family — the grammar's central conflict rule is switched off for
    its last quarter.

**6.4.22 is narrower in a way that matters.** Its अत्र is read as
समानाश्रयत्व: the two operations must have the same locus. व्याश्रयं तु
नासिद्धवद् भवति — where they rest on different things, no asiddhatva.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple

from src.astadhyayi.operations import resolve

#: 8.2.1's scope, which the corpus records: from itself to the last sūtra.
TRIPADI_FROM, TRIPADI_TO = "8.2.1", "8.4.68"
#: What precedes it — सपादसप्ताध्यायी, 'the seven adhyāyas and a quarter'.
SAPADASAPTADHYAYI_TO = "8.1.74"
#: 6.4.22's, आ भात् read as an अभिविधि so that भ is included.
ABHIYA_FROM, ABHIYA_TO = "6.4.22", "6.4.175"


class Why(Enum):
    """Which rule makes a thing invisible, or lets it be seen."""

    PURVATRA = "8.2.1"
    ABHIYA = "6.4.22"
    SATVA_TUK = "6.1.86"
    #: Not asiddha, and the sūtra or principle that says so.
    VISIBLE = "—"


@dataclass(frozen=True)
class Visibility:
    """Whether one rule's work is visible to another, and why."""

    asiddha: bool
    by: str
    why: str


def _order(sutra: str) -> Tuple[int, ...]:
    return tuple(int(p) for p in sutra.split(".") if p.isdigit())


def in_tripadi(sutra: str) -> bool:
    """Does 8.2.1's adhikāra reach this sūtra? 8.2.1 to 8.4.68."""
    return _order(TRIPADI_FROM) <= _order(sutra) <= _order(TRIPADI_TO)


def in_abhiya(sutra: str) -> bool:
    """Does 6.4.22's reach it? 6.4.22 to 6.4.175, भ included."""
    return _order(ABHIYA_FROM) <= _order(sutra) <= _order(ABHIYA_TO)


#: 8.2.2's four. The न्-elision is asiddha in *these* and nowhere else —
#: अत्र सिद्धे सत्यारम्भो नियमार्थः, एतेष्वेव नलोपोऽसिद्धो भवति, नान्यत्र.
NALOPA_ASIDDHA_IN = ("sup", "svara", "saṃjñā", "tuk-before-kṛt")


def visible(
    done: str,
    to: str,
    *,
    same_locus: Optional[bool] = None,
    done_is_apavada: bool = False,
    reading_a_case_ending: bool = False,
    operation: Optional[str] = None,
    done_is_nalopa: bool = False,
    done_is_mu: bool = False,
    applying_nabhava: bool = False,
) -> Visibility:
    """
    Is the work of `done` visible to `to`?

    The question a derivation engine has to ask before every step, and the
    answer is not simply 'has it happened yet'. 8.2.1 makes a whole quarter of
    the grammar invisible backwards, and invisible *within itself* as well.

    `same_locus` is 6.4.22's अत्र, read as समानाश्रयत्व. It is an input
    because whether two operations rest on the same thing is a fact about the
    derivation and not about the two sūtra numbers.
    """
    # 8.2.3 न मु ने — the exception innermost, so it is tried first.
    if done_is_mu and applying_nabhava:
        return Visibility(
            False, "8.2.3",
            "न मु ने — the मु substitute is not asiddha when the नाभाव of "
            "7.3.120 is to be done: मुभावो नाभावे कर्तव्ये नासिद्धो भवति, "
            "किं तर्हि? सिद्ध एव. अमुना.",
        )

    # 8.2.2 — a नियम, so the n-elision is asiddha only in the four named.
    if done_is_nalopa:
        if operation in NALOPA_ASIDDHA_IN:
            return Visibility(
                True, "8.2.2",
                f"नलोपः सुप्स्वरसंज्ञातुग्विधिषु कृति — the न्-elision is "
                f"asiddha in a {operation} operation. राजभिः, not *राजैः; "
                f"पञ्च ब्राह्मण्यः, where 1.1.24's षट् still applies.",
            )
        return Visibility(
            False, "8.2.2",
            "अत्र सिद्धे सत्यारम्भो नियमार्थः — एतेष्वेव नलोपोऽसिद्धो भवति, "
            "नान्यत्र. The sūtra restricts rather than grants: outside those "
            "four the elision is perfectly visible, and so राजीयति, राजायते "
            "and राजाश्व come out right.",
        )

    # 8.2.1's two directions.
    if in_tripadi(done):
        if reading_a_case_ending:
            return Visibility(
                False, "8.2.1",
                "The case-endings of the tripādī's own sūtras are read by "
                "1.1.49, 1.1.66 and 1.1.67 regardless: कार्यकालं हि "
                "संज्ञापरिभाषम् — a paribhāṣā is invoked at the moment it is "
                "wanted, so it is never 'earlier' than what it reads.",
            )
        if done_is_apavada and not in_tripadi(to):
            return Visibility(
                False, "8.2.1",
                "अपवादस्य तु परस्यापि उत्सर्गे कर्तव्ये वचनप्रामाण्याद् "
                "असिद्धत्वं न भवति — an exception is visible even standing "
                "later, when its general rule is in question.",
            )
        if _order(to) < _order(done):
            where = ("earlier in the tripādī" if in_tripadi(to)
                     else "in the सपादसप्ताध्यायी")
            return Visibility(
                True, "8.2.1",
                f"पूर्वत्रासिद्धम् — {done} stands in the tripādī and {to} "
                f"{where}, so the first is invisible to the second: "
                f"सिद्धकार्यं न करोति. Both directions are the sūtra's — "
                f"एतस्याम् अयं पादोनोऽध्यायोऽसिद्धो भवति for the one, and "
                f"इत उत्तरं चोत्तर उत्तरो योगः पूर्वत्र पूर्वत्रासिद्धो भवति "
                f"for the other.",
            )

    # 6.4.22, and its समानाश्रयत्व.
    if in_abhiya(done) and in_abhiya(to):
        if same_locus is False:
            return Visibility(
                False, "6.4.22",
                "अत्रग्रहणं किम्? व्याश्रयं तु नासिद्धवद् भवति — the अत्र is "
                "read as समानाश्रयत्व, so where the two rest on different "
                "things there is no asiddhatva. पपुषः पश्य, चिच्युषः पश्य.",
            )
        if same_locus is None:
            return Visibility(
                False, "6.4.22",
                "असिद्धवदत्राभात् would reach this, but its अत्र is "
                "समानाश्रयत्व and that has not been stated. Whether two "
                "operations rest on the same thing is a fact about the "
                "derivation, so it is an input.",
            )
        return Visibility(
            True, "6.4.22",
            "असिद्धवदत्राभात् — within 6.4.22 to 6.4.175, and on the same "
            "locus, what is done is treated as not done: एधि, शाधि, where "
            "the एत्व and the शाभाव do not bring on 8.2.40's धित्व; आगहि, "
            "जहि, where 6.4.105's लुक् does not follow.",
        )

    return Visibility(
        False, "—",
        "Neither 8.2.1 nor 6.4.22 reaches this pair, so what is done is done "
        "and can be seen.",
    )


def blocks_vipratisedha(first: str, second: str) -> Visibility:
    """
    Does 8.2.1 switch 1.4.2 off for this pair?

    The sharpest consequence in the family, and the Kāśikā states it: a later
    rule cannot enter a विप्रतिषेध with an earlier one it is invisible to —
    येन पूर्वेण लक्षणेन सह स्पर्धते परं लक्षणम्, तत् प्रति तस्यासिद्धत्वाद् न
    प्रवर्तते. So through the last pāda and a quarter, the grammar's central
    conflict rule does not operate, and the earlier rule simply stands.
    """
    later, earlier = ((second, first) if _order(second) > _order(first)
                      else (first, second))
    if in_tripadi(later) and _order(earlier) < _order(later):
        return Visibility(
            True, "8.2.1",
            f"1.4.2 does not settle {first} against {second}. {later} is "
            f"asiddha to {earlier}, so there is no contest to settle and the "
            f"earlier rule stands: विस्फोर्यम्, अवगोर्यम्, where the guṇa is "
            f"not displaced by 8.2.77's lengthening though that stands later.",
        )
    return Visibility(
        False, "1.4.2",
        "Neither is invisible to the other, so 1.4.2 applies in the ordinary "
        "way — whichever is stronger, or failing that the later.",
    )


@dataclass(frozen=True)
class Ekadesa:
    """6.1.86's answer: whether a single substitute is seen by two rules."""

    asiddha: bool
    by: str
    why: str


def ekadesa_visible(operation: str) -> Ekadesa:
    """
    6.1.86 षत्वतुकोरसिद्धः — the एकादेश of 6.1.84 onwards, for two operations.

    The single substitute that 6.1.84 एकः पूर्वपरयोः puts in place of two
    sounds is treated as not made, when a ṣatva or a tuk is in question. Only
    those two: elsewhere it is there.
    """
    if operation in ("ṣatva", "tuk"):
        return Ekadesa(
            True, "6.1.86",
            f"षत्वतुकोरसिद्धः — the single substitute is asiddha for a "
            f"{operation}, so the two sounds it replaced are what those rules "
            f"see.",
        )
    return Ekadesa(
        False, "6.1.86",
        "Only ṣatva and tuk are named, so for anything else the single "
        "substitute stands and is seen. 6.1.85 अन्तादिवच्च has already made "
        "it count as the end of the one and the beginning of the other.",
    )


@dataclass(frozen=True)
class Antadivat:
    """6.1.85's atideśa: what the single substitute counts as."""

    counts_as: Tuple[str, ...]
    by: str
    why: str


def antadivat(*, varna_vidhi: bool = False) -> Antadivat:
    """
    6.1.85 अन्तादिवच्च — the एकादेश counts as the end of one and the start of
    the other.

    Needed because the single substitute of 6.1.84 replaces a *pair*, and so
    belongs to neither of the two words on its own: पूर्वपरसमुदाय एकादेशस्य
    स्थानी. Without this, 1.1.56's sthānivadbhāva would not reach it —
    तत्रावयवयोर् आनुमानिकं स्थानित्वम् — and ब्रह्मबन्धूः could not be treated
    as a prātipadika ending, nor वृक्षौ as a sup-final pada.

    **And not for an operation on sounds.** वर्णाश्रयविधाव् अयम्
    अन्तादिवद्भावो नेष्यते, with three worked cases: खट्वाभिः keeps its भिस्
    against 7.1.9, जुहाव its णल् against 7.1.34, and अस्यै अश्वः its vṛddhi
    against 6.1.109.
    """
    if varna_vidhi:
        return Antadivat(
            (), "6.1.85",
            "वर्णाश्रयविधावयम् अन्तादिवद्भावो नेष्यते — not for an operation "
            "that rests on the sounds themselves: खट्वाभिः, जुहाव, "
            "अस्यै अश्वः.",
        )
    return Antadivat(
        ("end of the first", "beginning of the second"), "6.1.85",
        "अन्तादिवच्च — स पूर्वस्यान्तवद् भवति, परस्यादिवद् भवति. "
        "ब्रह्मबन्धूः is then a prātipadika-final for 4.1.1, and वृक्षौ a "
        "sup-final pada for 1.4.14.",
    )


__all__ = [
    "ABHIYA_FROM",
    "Antadivat",
    "antadivat",
    "ABHIYA_TO",
    "Ekadesa",
    "NALOPA_ASIDDHA_IN",
    "SAPADASAPTADHYAYI_TO",
    "TRIPADI_FROM",
    "TRIPADI_TO",
    "Visibility",
    "Why",
    "blocks_vipratisedha",
    "ekadesa_visible",
    "in_abhiya",
    "in_tripadi",
    "visible",
]
