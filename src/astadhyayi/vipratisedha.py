# -*- coding: utf-8 -*-
"""
The two paribhāṣās the fourth pāda opens with — 1.4.1 and 1.4.2.

    1.4.1  आ कडारादेका संज्ञा      up to 2.2.38, only one name applies
    1.4.2  विप्रतिषेधे परं कार्यम्   in a conflict, the later operation

These are not rules about Sanskrit. They are rules about the rules, and every
block codified before this one has been quietly obeying the second of them
while calling it 'the later sūtra wins'. Codifying it properly makes that
citable — and, more usefully, makes visible the large qualification the Kāśikā
attaches, which the hand-rolled version did not have.

**1.4.2 is only for rules of equal strength.** विप्रतिषेध is defined by a
vārttika as तुल्यबलविरोध, and the Kāśikā spells out where that does *not*
hold: उत्सर्गापवादनित्यानित्यान्तरङ्गबहिरङ्गेषु तुल्यबलता नास्ति इति नायम्
अस्य योगस्य विषयः। बलवतैव तत्र भवितव्यम्. Where one rule is an exception to
the other, or invariable where the other is contingent, or inner where the
other is outer, they are not equally strong, this sūtra has no application,
and the stronger wins — which may perfectly well be the earlier one. Reading
1.4.2 as a bare 'later wins' gets those three families backwards.

**1.4.1 is a restriction, not a grant.** Names ordinarily co-apply —
अन्यत्र संज्ञासमावेशात् — and this confines the stretch from here to 2.2.38
to one name at a time. Which one? या परा, अनवकाशा च: the later, and the one
that has no other opportunity. The Kāśikā's own example is 1.4.10 and 1.4.11:
a short vowel before a conjunct answers both लघु and गुरु, and एकसंज्ञा leaves
only गुरु, which is why अततक्षत् does not get 7.4.93's सन्वद्भाव.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Sequence, Tuple

#: 1.4.1's own scope, which the corpus records: from here to कडाराः कर्मधारये.
EKASAMJNA_FROM, EKASAMJNA_TO = "1.4.1", "2.2.38"


class Strength(Enum):
    """
    Why one rule may beat another other than by standing later.

    The four the Kāśikā names at 1.4.2, as the cases where तुल्यबलता is
    absent. Each is a relation between two rules and not a property of one, so
    it is stated of the pair.
    """

    #: तुल्यबल — equally strong, and only here does 1.4.2 apply.
    EQUAL = "tulyabala"
    #: उत्सर्गापवाद — the exception beats the general rule it excepts.
    APAVADA = "apavāda"
    #: नित्यानित्य — the rule that would apply either way beats the one that
    #: would be lost if the other went first.
    NITYA = "nitya"
    #: अन्तरङ्गबहिरङ्ग — the rule whose causes lie nearer beats the outer one.
    ANTARANGA = "antaraṅga"
    #: पूर्वविप्रतिषेध — not a kind of strength at all but a declaration.
    #: Where the received forms need the EARLIER rule and 1.4.2 would give
    #: the later, a vārttika or the vṛtti says so in as many words and the
    #: order is reversed for that pair alone. The Kāśikā on 6.4.48 is the
    #: plainest instance: **वृद्धिदीर्घाभ्यामतो लोपः पूर्वविप्रतिषेधेन** —
    #: 7.2.115's vṛddhi and 7.3.101's lengthening both stand later, and
    #: the अ is elided all the same, which is why कथयति has no आ.
    PURVA = "pūrvavipratiṣedha"


@dataclass(frozen=True)
class Rule:
    """A rule as a candidate in a conflict: its number and its standing."""

    sutra: str
    #: What this rule is to the *other* one, where they are not equally
    #: strong. `None` or EQUAL means 1.4.2 decides.
    standing: Strength = Strength.EQUAL
    #: अनवकाश — a rule with no other field of application at all. 1.4.1 gives
    #: it the name where two would otherwise apply.
    anavakasa: bool = False
    what: str = ""


@dataclass(frozen=True)
class Settled:
    """Which rule prevails, and on what principle."""

    winner: Optional[Rule]
    by: str
    why: str
    #: The rules that lost, so a reader can see what was in contention.
    against: Tuple[str, ...] = ()


def _order(sutra: str) -> Tuple[int, ...]:
    return tuple(int(part) for part in sutra.split(".") if part.isdigit())


def vipratisedha(candidates: Sequence[Rule]) -> Settled:
    """
    1.4.2 विप्रतिषेधे परं कार्यम् — which of two conflicting rules is done.

    The definition first, because it decides whether the sūtra applies at all:
    यत्र द्वौ प्रसङ्गौ अन्यार्थौ एकस्मिन् युगपत् प्राप्नुतः स तुल्यबलविरोधो
    विप्रतिषेधः — two rules, each with a field of its own, both reaching one
    place at once. The Kāśikā's example is 7.3.101 and 7.3.103: each has its
    own scope, वृक्षाभ्याम् for the one and वृक्षेषु for the other, and both
    reach वृक्षेभ्यः. There the later is done.

    Where the two are *not* equally strong the sūtra says nothing and the
    stronger prevails, whether it stands earlier or later.
    """
    ranked = [c for c in candidates]
    if not ranked:
        return Settled(None, "—", "Nothing in contention.")
    if len(ranked) == 1:
        return Settled(ranked[0], "—",
                       "One rule only, so no विप्रतिषेध to settle.")

    stronger = [c for c in ranked if c.standing is not Strength.EQUAL]
    if stronger:
        winner = stronger[0]
        named = {
            Strength.APAVADA: (
                "उत्सर्गापवादयोः — an exception beats the rule it excepts, and "
                "1.4.2 does not reach the case"),
            Strength.NITYA: (
                "नित्यानित्ययोः — the invariable rule beats the contingent "
                "one, and 1.4.2 does not reach the case"),
            Strength.ANTARANGA: (
                "अन्तरङ्गबहिरङ्गयोः — the rule whose causes lie nearer beats "
                "the outer one, and 1.4.2 does not reach the case"),
            Strength.PURVA: (
                "पूर्वविप्रतिषेधेन — the earlier rule is done, the tradition "
                "having said so of this pair in as many words"),
        }[winner.standing]
        return Settled(
            winner, "1.4.2 (excluded)",
            f"{named}. उत्सर्गापवादनित्यानित्यान्तरङ्गबहिरङ्गेषु तुल्यबलता "
            f"नास्तीति नायमस्य योगस्य विषयः। बलवतैव तत्र भवितव्यम्.",
            against=tuple(c.sutra for c in ranked if c is not winner),
        )

    winner = max(ranked, key=lambda c: _order(c.sutra))
    return Settled(
        winner, "1.4.2",
        "विप्रतिषेधे परं कार्यम् — the two are of equal strength, each with a "
        "field of its own, and both reach here at once; so the later is done. "
        "तुल्यबलविरोधो विप्रतिषेधः.",
        against=tuple(c.sutra for c in ranked if c is not winner),
    )


def eka_samjna(candidates: Sequence[Rule]) -> Settled:
    """
    1.4.1 आ कडारादेका संज्ञा — which single name applies.

    Names ordinarily co-apply; from here to 2.2.38 they do not, and the one
    that stands is या परा, अनवकाशा च — the later, or the one with nowhere else
    to apply. The Kāśikā's example is the pair 1.4.10 ह्रस्वं लघु and 1.4.11
    संयोगे गुरु, both of which reach a short vowel before a conjunct: गुरु
    stands, being later, and so शिक्षा and भिक्षा are गुरु and not लघु.
    """
    ranked = [c for c in candidates]
    if not ranked:
        return Settled(None, "—", "No name in contention.")
    if len(ranked) == 1:
        return Settled(ranked[0], "—", "One name only; nothing to restrict.")

    without_scope = [c for c in ranked if c.anavakasa]
    if len(without_scope) == 1:
        winner = without_scope[0]
        return Settled(
            winner, "1.4.1",
            "अनवकाशा — of the two, this one has no other field of application "
            "at all, so it is the one that stands: का पुनरसौ? या परानवकाशा च.",
            against=tuple(c.sutra for c in ranked if c is not winner),
        )

    winner = max(ranked, key=lambda c: _order(c.sutra))
    return Settled(
        winner, "1.4.1",
        "एका संज्ञा — one name only, and the later of them: अन्यत्र "
        "संज्ञासमावेशान् नियमार्थं वचनम्, एकैव संज्ञा भवति. Elsewhere names "
        "co-apply; this stretch is the exception.",
        against=tuple(c.sutra for c in ranked if c is not winner),
    )


def _rules(written: Sequence[str]) -> List[Rule]:
    """
    Read `8.2.31`, `6.1.10:apavāda`, `1.4.18:anavakāśa` from plain strings.

    The relation between two rules — which is the exception, which the inner
    one — is a judgement about the pair and not a property of either, so it
    has to be stated. A form can only hand back strings, and this is how they
    say it.
    """
    standings = {
        "apavāda": Strength.APAVADA, "nitya": Strength.NITYA,
        "antaraṅga": Strength.ANTARANGA, "tulyabala": Strength.EQUAL,
    }
    out: List[Rule] = []
    for text in written:
        sutra, *tags = [p.strip() for p in str(text).split(":") if p.strip()]
        standing, anavakasa = Strength.EQUAL, False
        for tag in tags:
            if tag in standings:
                standing = standings[tag]
            elif tag in ("anavakāśa", "anavakasa"):
                anavakasa = True
        out.append(Rule(sutra, standing=standing, anavakasa=anavakasa,
                        what=sutra))
    return out


def vipratisedha_of(candidates: Sequence[str]) -> Settled:
    """1.4.2 from written rule names — see `_rules` for the tags."""
    return vipratisedha(_rules(candidates))


def eka_samjna_of(candidates: Sequence[str]) -> Settled:
    """1.4.1 from written rule names — see `_rules` for the tags."""
    return eka_samjna(_rules(candidates))


def governs(sutra_id: str) -> bool:
    """Does 1.4.1's restriction reach this sūtra? From 1.4.1 to 2.2.38."""
    return _order(EKASAMJNA_FROM) <= _order(sutra_id) <= _order(EKASAMJNA_TO)


__all__ = [
    "EKASAMJNA_FROM",
    "EKASAMJNA_TO",
    "Rule",
    "Settled",
    "Strength",
    "eka_samjna",
    "eka_samjna_of",
    "governs",
    "vipratisedha",
    "vipratisedha_of",
]
