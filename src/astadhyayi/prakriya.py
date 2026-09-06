# -*- coding: utf-8 -*-
"""
प्रक्रिया — applying rules in sequence, rather than answering one question.

Every rule codified so far answers a question put to it: *is this sound
vṛddhi, does this root take the middle endings, do these two words compound*.
None of them applies itself to a form and hands the result to the next rule.
This is the frame that does, and it is the largest thing the project had not
built.

The engine is small on purpose. What makes a derivation faithful is not the
loop — a loop is twenty lines — but what it consults before each step, and
the north star named the two before the loop existed:

  * **which rule wins** where more than one could act — 1.4.2 विप्रतिषेधे परं
    कार्यम्, with the three cases it does *not* decide (an अपवाद beats its
    उत्सर्ग, a नित्य rule beats an अनित्य one, an अन्तरङ्ग beats a बहिरङ्ग),
    all of which `vipratisedha.py` already knows;
  * **what the previous step is even visible to** — 8.2.1 पूर्वत्रासिद्धम्,
    which is not decoration: it switches 1.4.2 off for the last quarter of
    the grammar, so an engine that consulted only the first would derive the
    tripādī wrongly and confidently.

Both were codified before this file, which is why it can be short.

**The honest scope.** 379 of 3,983 sūtras are codified, and most of them are
saṃjñā and paribhāṣā — rules that *name* and rules about *reading* — because
that is what adhyāya 1 is. The operational rules that actually change a form
live mostly in adhyāyas 6 and 7 and are not codified yet. So this engine can
today derive exactly what the codified operational rules allow, which is the
it-deletion sequence: the eight saṃjñās of 1.3.2–1.3.8 that mark indicatory
letters, and 1.3.9 तस्य लोपः that removes them. डुकृञ् to कृ, in steps, each
step naming its own sūtra.

That is a real derivation and a small one, and both halves of that sentence
matter. The frame is built and tested; the rule set grows as adhyāyas 6 and 7
are codified, and nothing here has to change when it does.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import (
    Any, Callable, FrozenSet, List, Optional, Sequence, Tuple)

from src.astadhyayi.asiddha import blocks_vipratisedha, visible
from src.astadhyayi.vipratisedha import Rule as Candidate
from src.astadhyayi.vipratisedha import Settled, Strength, vipratisedha
from src.normalizer import iast_to_devanagari


# ---------------------------------------------------------------------------
# What is being derived
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Term:
    """
    One piece of the form under derivation, and the names it bears.

    A term is not just a string, because the rules do not act on strings.
    They act on something that is a धातु or a प्रत्यय, that has been given
    names by earlier rules, and that carries indicatory letters not yet
    removed. All of that has to survive from one step to the next or the
    next rule cannot see what it needs.
    """

    text: str
    #: धातु, प्रत्यय, प्रातिपदिक — what kind of piece this is.
    role: str = "form"
    #: The names conferred on it so far, by whichever rules conferred them.
    samjnas: FrozenSet[str] = frozenset()
    #: Indicatory letters found, as (letters, the sūtra that marked them).
    #: Kept apart from `samjnas` because 1.3.9 removes exactly these.
    marked: Tuple[Tuple[str, str], ...] = ()
    #: Whether 1.3.9 has already run on this term.
    stripped: bool = False
    #: The form as the dhātupāṭha enunciates it — डुपचँष् (ḍupacaṣ), not
    #: पच् (pac) — kept beside `text` because two rules do not ask what a
    #: term *is* but what the dhātupāṭha says *about* it, and the file is
    #: indexed by the enunciation. 2.4.72 अदिप्रभृतिभ्यः शपः is one: asked
    #: about अद् (ad) it gets two entries, 01.0064 अदिँ (adi̐, बन्धने) and
    #: 02.0001 अदँ (ada̐, भक्षणे), and elides शप् for both — so अदिँ came
    #: out अत्ति (atti) when it is अदति (adati). Asked about the upadeśa it
    #: gets one entry and the right gaṇa. Empty where the caller gave a
    #: bare name, which is what `verbal_gana` already treats as ambiguous.
    enunciated: str = ""
    #: Which class of the dhātupāṭha this root is read in — "01", "06".
    #: The विकरण rules 3.1.69–3.1.81 name a class and nothing else, and a
    #: root NAME does not settle one: जि (ji) is 01.0642 जि जये and also
    #: 10.0324 जि भाषायाम्, one taking शप् and the other णिच्. Only the
    #: dhātupāṭha's code separates them, so it is carried rather than
    #: looked up. Empty where the caller did not say and the corpus does
    #: not settle it, and then 3.1.68 कर्तरि शप् stands as the उत्सर्ग.
    gana: str = ""
    #: Whether this is still the form as the grammar enunciates it. 1.3.2's
    #: उपदेशे governs the whole it-section, so once an operation has changed
    #: a term the it-rules no longer reach it. Without this the engine
    #: derived जयति and then went on to call its य् an इत्.
    upadesa: bool = True

    def with_mark(self, letters: str, by: str) -> "Term":
        return replace(self, marked=self.marked + ((letters, by),))

    def named(self, name: str) -> "Term":
        return replace(self, samjnas=self.samjnas | {name})

    def altered(self, text: str) -> "Term":
        """
        The term after an operation has changed it.

        It is no longer उपदेश, which is the condition 1.3.2 puts on the
        whole it-section, so the it-rules stop reaching it.
        """
        return replace(self, text=text, upadesa=False)

    def has_mark_by(self, sutra: str) -> bool:
        return any(by == sutra for _, by in self.marked)


@dataclass(frozen=True)
class State:
    """The whole form at one moment of the derivation."""

    terms: Tuple[Term, ...]

    @property
    def surface(self) -> str:
        return "".join(term.text for term in self.terms)

    def replace_term(self, index: int, term: Term) -> "State":
        terms = list(self.terms)
        terms[index] = term
        return State(tuple(terms))

    def insert_term(self, index: int, term: Term) -> "State":
        """
        A rule may add a piece, not only alter one.

        3.1.68 कर्तरि शप् is the first that does: it puts an affix between
        the root and the ending, and the form grows by a term rather than
        changing in place.
        """
        terms = list(self.terms)
        terms.insert(index, term)
        return State(tuple(terms))

    def __str__(self) -> str:
        return self.surface


# ---------------------------------------------------------------------------
# A rule the engine can apply
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Operational:
    """
    A codified rule in the form the engine needs: does it apply, and what
    does it do.

    This is deliberately *not* the same object as the question-answering
    function registered for a sūtra. Those take the caller's assertions and
    return a verdict; these take a state and return a state. A sūtra can
    have both, and 1.3.9 does.
    """

    sutra: str
    #: What the rule does, named from the closed vocabulary in operations.py
    #: so the engine can ask 8.2.1 about it. Empty where the rule confers a
    #: name rather than performing an operation.
    operation: str = ""
    #: What this rule is to a rule it competes with, where the two are not
    #: equally strong. 1.4.2 decides only among equals.
    standing: Strength = Strength.EQUAL
    #: अनवकाश — no other field of application at all.
    anavakasa: bool = False
    what: str = ""
    matches: Callable[[State], bool] = lambda _state: False
    perform: Callable[[State], State] = lambda state: state
    #: Where this rule would act, as something hashable. Two rules are in
    #: विप्रतिषेध only if they would act in the *same* place — एकस्मिन्
    #: युगपत् — so this is what decides whether 1.4.2 is consulted at all.
    #: Rules that leave it constant are treated as contending with each
    #: other, which is the safe default: it asks 1.4.2 rather than assuming
    #: independence.
    site: Callable[[State], Any] = lambda _state: "*"

    def candidate(self) -> Candidate:
        return Candidate(self.sutra, standing=self.standing,
                         anavakasa=self.anavakasa, what=self.what)


# ---------------------------------------------------------------------------
# The trace
# ---------------------------------------------------------------------------


def _both(text: str) -> str:
    """
    A form in both scripts — देवनागरी (IAST) — never IAST alone.

    Every surface form in a trace is what this codification's own
    convention requires paired: the reader who cannot parse अयादि-सन्धि
    from `jeati → jayati` alone can still see जेअति → जयति and place it.
    `text` is empty only for a start state with no terms, which does not
    occur in practice; guarded anyway rather than handed to the
    converter blind.
    """
    if not text:
        return text
    return f"{iast_to_devanagari(text)} ({text})"


@dataclass(frozen=True)
class Step:
    """One rule applied, and why it was that rule."""

    sutra: str
    what: str
    before: str
    after: str
    #: The rules that also applied here and did not win, with 1.4.2's reason.
    against: Tuple[str, ...] = ()
    why: str = ""

    def __str__(self) -> str:
        arrow = (f"{_both(self.before)} → {_both(self.after)}"
                 if self.before != self.after else _both(self.before))
        return f"{self.sutra:9} {arrow:46} {self.what}"


@dataclass(frozen=True)
class Prakriya:
    """A derivation: where it started, every step, and where it stopped."""

    start: State
    steps: Tuple[Step, ...]
    final: State
    #: Why the derivation stopped. "no rule applies" is the ordinary end.
    stopped: str = "no rule applies"

    @property
    def surface(self) -> str:
        return self.final.surface

    def trace(self) -> str:
        lines = [f"{'':9} {_both(self.start.surface)}"]
        lines.extend(str(step) for step in self.steps)
        lines.append(f"{'':9} {_both(self.final.surface)}   [{self.stopped}]")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# The loop
# ---------------------------------------------------------------------------


#: A derivation longer than this has not converged, and returning a truncated
#: trace is better than looping. Real prakriyās run to a few dozen steps.
MAX_STEPS = 60


def derive(
    start: State,
    rules: Sequence[Operational],
    *,
    max_steps: int = MAX_STEPS,
) -> Prakriya:
    """
    Apply rules to a form until none applies.

    At each turn: collect every rule that matches, let 1.4.2 settle it if
    more than one does, apply the winner, and record what it displaced. A
    rule that matches but changes nothing ends the derivation rather than
    spinning — a rule doing nothing forever is the failure mode a loop like
    this has, and it is better to stop and say so.
    """
    state = start
    steps: List[Step] = []
    stopped = "no rule applies"

    for _ in range(max_steps):
        matched = [rule for rule in rules if rule.matches(state)]
        if not matched:
            break

        contending = _at_one_site(matched, state)
        chosen, settled = _settle(contending)
        after = chosen.perform(state)

        if after.surface == state.surface and after == state:
            stopped = (f"{chosen.sutra} matched but changed nothing — "
                       f"stopping rather than repeating it")
            break

        displaced = tuple(s for s in settled.against if s != chosen.sutra)
        steps.append(Step(
            sutra=chosen.sutra,
            what=chosen.what,
            before=state.surface,
            after=after.surface,
            # Only a rule that wanted this same place was displaced. A rule
            # waiting to act somewhere else is not something 1.4.2 beat.
            against=displaced if len(contending) > 1 else (),
            why=settled.why if len(contending) > 1 else "",
        ))
        state = after
    else:
        stopped = f"stopped at the {max_steps}-step cap without converging"

    return Prakriya(start=start, steps=tuple(steps), final=state,
                    stopped=stopped)


def _at_one_site(
    matched: Sequence[Operational], state: State
) -> List[Operational]:
    """
    The rules contending for a single place — the only ones 1.4.2 speaks to.

    Where several places are ready at once the grammar does not say which to
    take first and neither does this: one is taken, the rest are matched
    again next turn, and no rule is credited with having displaced them.
    """
    by_site: dict = {}
    for rule in matched:
        by_site.setdefault(rule.site(state), []).append(rule)
    first = next(iter(by_site))
    return by_site[first]


def _settle(matched: Sequence[Operational]) -> Tuple[Operational, Settled]:
    """Which of the matching rules is done here — 1.4.2, and its exclusions."""
    if len(matched) == 1:
        only = matched[0]
        return only, Settled(only.candidate(), only.sutra,
                             "the only rule that applies")

    blocked = _asiddha_settles(matched)
    if blocked is not None:
        return blocked

    settled = vipratisedha([rule.candidate() for rule in matched])
    winner = settled.winner
    for rule in matched:
        if winner is not None and rule.sutra == winner.sutra:
            return rule, settled
    return matched[-1], settled


def _order_of(sutra: str) -> Tuple[int, ...]:
    return tuple(int(piece) for piece in sutra.split("."))


def _asiddha_settles(
    matched: Sequence[Operational]
) -> Optional[Tuple[Operational, Settled]]:
    """
    8.2.1 पूर्वत्रासिद्धम्, where it takes the case away from 1.4.2 entirely.

    येन पूर्वेण लक्षणेन सह स्पर्धते परं लक्षणम्, तत् प्रति तस्य
    असिद्धत्वाद् न प्रवर्तते — a later rule of the tripādī cannot enter a
    विप्रतिषेध with an earlier one it is invisible to, so there is no
    contest to settle and the earlier rule simply stands.

    This is the half of the north star that was named in this module's own
    docstring and never wired: `can_see` was exported and nothing called
    it. Without it 8.4.55 खरि च reached रुणध् + ति first and gave
    रुणत्ति, where 8.2.40 झषस्तथोर्धोऽधः stands earlier and gives
    रुणद्धि.

    It speaks only where the rules are equally strong. उत्सर्गापवाद and
    the rest are not विप्रतिषेध either, and a rule carrying a standing has
    already been excused by 1.4.2's own terms.
    """
    if any(rule.standing is not Strength.EQUAL or rule.anavakasa
           for rule in matched):
        return None
    ordered = sorted(matched, key=lambda rule: _order_of(rule.sutra))
    earliest, latest = ordered[0], ordered[-1]
    verdict = blocks_vipratisedha(earliest.sutra, latest.sutra)
    if not verdict.asiddha:
        return None
    return earliest, Settled(
        earliest.candidate(), verdict.by, verdict.why,
        against=tuple(rule.sutra for rule in ordered[1:]),
    )


def can_see(done: str, to: str, **conditions) -> bool:
    """
    Whether an earlier step is visible to a later one — 8.2.1, both ways.

    The engine asks this rather than assuming, because for the last quarter
    of the grammar the answer is no: what the tripādī has already done is
    असिद्ध to what it does next, and a rule that read the changed form
    would derive a different word with complete confidence.
    """
    # `visible()` reports असिद्धत्व — its field is true when the earlier
    # work is *hidden*. Reading it as though it meant the opposite would
    # invert the tripādī everywhere, so the negation is spelled out here
    # rather than assumed at each call site.
    return not visible(done, to, **conditions).asiddha


__all__ = [
    "Term", "State", "Operational", "Step", "Prakriya",
    "derive", "can_see", "MAX_STEPS",
]
