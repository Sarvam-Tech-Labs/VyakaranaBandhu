# -*- coding: utf-8 -*-
"""
The derivation loop for sandhi — and what it asks before every step.

The loop is short. What makes a derivation *faithful* is what it consults, and
the two questions were codified long before this file:

  * **Who may see what** — 8.2.1 पूर्वत्रासिद्धम्. Every rule is handed a `View`
    (see `segs`): the row of sounds as that rule, and no other, is entitled to
    see it. The engine never lets a rule read the row directly.
  * **Who wins where two rules reach one place** — first the अपवाद relations
    each rule declares (`Rule.overrides`, each with the tradition's reason);
    then 8.2.1 again, because a later rule of the tripādī cannot enter a
    विप्रतिषेध with an earlier one it is invisible to; and only then 1.4.2
    विप्रतिषेधे परं कार्यम्, for what is left. Both of the last two are
    `asiddha.blocks_vipratisedha` and `vipratisedha.vipratisedha`, asked and
    not re-implemented.

**Options fork the derivation.** A विभाषा is not a coin the engine tosses: both
courses are correct, so both are returned, each with its own trace. When the
rule that wins a place is optional the engine follows it, and *also* follows
the course that declines it — remembering, as `State.declined`, that this rule
was offered at this place and refused, so it is not offered again.

**What it does not decide.** Where two applications lie in different places
the grammar says nothing about their order (both hold at once, युगपत्), and
neither does this: the leftmost is taken first, the others are found again on
the next turn. That is a reading order and it is stated as one; it changes no
result, since the two do not touch a common sound.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Dict, List, Optional, Sequence, Tuple

from src.astadhyayi.asiddha import blocks_vipratisedha
from src.astadhyayi.sandhi.rule import (
    Application, Detail, Edit, Rule)
from src.astadhyayi.sandhi.segs import Seg, State, View
from src.astadhyayi.vipratisedha import Rule as Candidate
from src.astadhyayi.vipratisedha import vipratisedha

#: A derivation longer than this has not converged. Real sandhi runs to a
#: handful of steps; returning a truncated trace beats looping.
MAX_STEPS = 60
#: The most alternatives one input may yield. Options multiply, and a caller
#: who gave a whole verse should be told it was cut, not made to wait.
MAX_OUTCOMES = 64


@dataclass(frozen=True)
class Displaced:
    """A rule that could have applied here and did not, and why."""

    sutra: str
    name: str
    why: str
    #: True where the rule merely stands LATER in the tripādī (8.2.1). It has
    #: not lost anything: it acts next, on what the earlier rule leaves, if it
    #: still applies. It is kept out of a step's `against`.
    deferred: bool = False
    #: The displaced rule's identity (`Rule.key`): a vārttika and the sūtra it
    #: stands on share a number and are two rules.
    key: str = ""
    #: True where an explicit `overrides` declared the displacement — the only
    #: kind a refusal (a प्रतिषेध) carries forward as "not offered here again".
    named: bool = False
    #: Who displaced it, as a reader should be told (a vārttika is labelled).
    by: str = ""


@dataclass(frozen=True)
class Step:
    """One rule applied — or, for an option, offered and declined."""

    n: int
    sutra: str
    name: str
    detail: Detail
    before: str
    after: str
    #: Word indexes the step touched, so a reader can see which junction.
    words: Tuple[int, ...]
    against: Tuple[Displaced, ...] = ()
    #: "" for an ordinary step; the option's kind for a taken option; and
    #: "declined" for the course that refused it.
    option: str = ""
    declined: bool = False

    @property
    def sutras(self) -> Tuple[str, ...]:
        return (self.sutra,) + tuple(v.sutra for v in self.detail.via)


@dataclass(frozen=True)
class Outcome:
    """One complete derivation: where it began, every step, where it stopped."""

    start: State
    final: State
    steps: Tuple[Step, ...]
    #: (sūtra, taken) for each option met on the way.
    choices: Tuple[Tuple[str, bool], ...] = ()
    stopped: str = "no rule applies"

    @property
    def surface(self) -> str:
        return self.final.joined()

    def text(self) -> str:
        """The result with a space where words still stand apart, as spoken."""
        return self.final.text(final=True)


# ---------------------------------------------------------------------------
# Finding what applies
# ---------------------------------------------------------------------------


def collect(state: State, rules: Sequence[Rule]
            ) -> List[Tuple[Rule, Application]]:
    """
    Every (rule, application) the state offers, each rule asked through its
    own View.

    An application that would change a sound the rule can see only through its
    past is not offered. That is 8.2.1 doing its work, not a fault: the rule
    already had its chance at that place — before the later rule changed it —
    and to act on it now would be to act on a sound that, for this rule,
    was never made.
    """
    found: List[Tuple[Rule, Application]] = []
    for rule in rules:
        if rule.vedic and not state.veda:
            continue
        view = View(state, rule.sutra, rule.consumes, rule.operation)
        for app in rule.find(view):
            if (rule.key, app.site) in state.declined or app.hidden:
                continue
            found.append((rule, app))
    return found


def _position(state: State, app: Application) -> int:
    index = {seg.uid: i for i, seg in enumerate(state.segs)}
    return min((index[uid] for uid in app.site if uid in index),
               default=len(state.segs))


def _group(state: State, found: List[Tuple[Rule, Application]]
           ) -> List[Tuple[Rule, Application]]:
    """The applications contending for the leftmost place."""
    first = min(found, key=lambda ra: (_position(state, ra[1]),
                                       ra[0].order))
    sites = set(first[1].site)
    return [ra for ra in found if sites & set(ra[1].site)]


# ---------------------------------------------------------------------------
# Who wins
# ---------------------------------------------------------------------------


def _pick(earlier: Tuple[Rule, Application], later: Tuple[Rule, Application]
          ) -> Tuple[Tuple[Rule, Application], Displaced]:
    """8.2.1, then 1.4.2, between two rules of equal standing."""
    first, second = earlier[0], later[0]
    verdict = blocks_vipratisedha(first.sutra, second.sutra)
    if verdict.asiddha:
        return earlier, Displaced(
            second.sutra, second.name,
            f"{second.sutra} stands later in the tripādī, so it is asiddha to "
            f"{first.sutra}; {first.sutra} acts first and {second.sutra} "
            f"acts on what it leaves (8.2.1 पूर्वत्रासिद्धम्)", deferred=True,
            key=second.key, by=first.label)
    settled = vipratisedha([
        Candidate(first.sutra, standing=first.standing, what=first.name),
        Candidate(second.sutra, standing=second.standing, what=second.name),
    ])
    if settled.winner is not None and settled.winner.sutra == first.sutra:
        return earlier, Displaced(second.sutra, second.name,
                                  f"{settled.by} — {settled.why}",
                                  key=second.key, by=first.label)
    return later, Displaced(first.sutra, first.name,
                            f"{settled.by} — {settled.why}",
                            key=first.key, by=second.label)


def _same_place(a: Application, b: Application) -> bool:
    """Two applications reach one place if they share a sound."""
    return bool(set(a.site) & set(b.site))


def settle(group: List[Tuple[Rule, Application]]
           ) -> Tuple[Tuple[Rule, Application], List[Displaced]]:
    """
    Which contender is done here, and what it displaced.

    **Overrides are per place, and only the undefeated count.** A rule that
    overrides another displaces it where the two reach the SAME sounds — not
    across a whole connected group, which is how a vārttika that lifts the hold
    of one vowel would also have lifted the hold of a neighbour it has nothing
    to do with. And a rule that has itself been displaced displaces nothing: in
    a chain of exceptions (6.1.88 excepts 6.1.87, 6.1.94 excepts 6.1.88, 6.1.89
    excepts 6.1.94) what the third does to the second no longer matters once the
    third has been set aside by the fourth. That is decided as an argument is:
    a rule with no undefeated attacker stands; one attacked by a standing rule
    falls; repeat. Whatever a cycle leaves unsettled is left to 8.2.1 and 1.4.2.
    """
    n = len(group)
    attackers: List[List[int]] = [[] for _ in range(n)]
    reasons: Dict[Tuple[int, int], str] = {}
    for i, (rule, app) in enumerate(group):
        for j, (other, other_app) in enumerate(group):
            if i == j:
                continue
            why = other.overrides_rule(rule)
            if why and _same_place(app, other_app):
                attackers[i].append(j)
                reasons[(i, j)] = why
    standing: set = set()
    fallen: Dict[int, int] = {}
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if i in standing or i in fallen:
                continue
            if all(j in fallen for j in attackers[i]):
                # A defeated rule defeats nothing; but if an attacker was defeated by
                # a standing rule with active edits (an apavādāpavāda), the original
                # utsarga does not revive to contest the conqueror.
                conqueror = None
                for j in attackers[i]:
                    killer = fallen.get(j)
                    if (killer is not None and killer in standing
                            and group[killer][1].edits):
                        conqueror = killer
                        break
                if conqueror is not None:
                    fallen[i] = conqueror
                    reasons[(i, conqueror)] = (
                        f"{group[conqueror][0].label} defeats {group[j][0].label}, "
                        f"which defeats it"
                    )
                    changed = True
                else:
                    standing.add(i)
                    changed = True
            else:
                winner = next((j for j in attackers[i] if j in standing), None)
                if winner is not None:
                    fallen[i] = winner
                    changed = True
    displaced: List[Displaced] = []
    for i, killer in fallen.items():
        rule = group[i][0]
        other = group[killer][0]
        displaced.append(Displaced(
            rule.sutra, rule.name,
            f"{other.label} displaces it — {reasons[(i, killer)]}",
            key=rule.key, named=True, by=other.label))
    survivors = [item for i, item in enumerate(group) if i not in fallen]
    ordered = sorted(survivors, key=lambda ra: ra[0].order)
    best = ordered[0]
    for other in ordered[1:]:
        best, lost = _pick(best, other)
        displaced.append(lost)
    return best, displaced


# ---------------------------------------------------------------------------
# Doing it
# ---------------------------------------------------------------------------


def apply(state: State, rule: Rule, app: Application) -> State:
    """The state after `rule` has made `app`'s edits."""
    segs = list(state.segs)
    uid = state.next_uid
    for edit in sorted(app.edits, key=lambda e: e.start, reverse=True):
        old = tuple(segs[edit.start:edit.end])
        anchor = old[0].w if old else segs[max(edit.start - 1, 0)].w
        made: List[Seg] = []
        for k, spec in enumerate(edit.new):
            made.append(Seg(
                uid=uid, s=spec.s,
                w=spec.w if spec.w is not None else anchor,
                lw=spec.lw, marks=spec.marks, made_by=rule.sutra,
                # The history belongs to the first sound only, so a substitute
                # of several sounds (अय्) does not put its sthānin back twice
                # when a viewer looks through it.
                prior=old if k == 0 else (), show=spec.show))
            uid += 1
        segs[edit.start:edit.end] = made
    return replace(state, segs=tuple(segs), next_uid=uid)


def _words_touched(state: State, app: Application) -> Tuple[int, ...]:
    by_uid = {seg.uid: seg for seg in state.segs}
    words = set()
    for uid in app.site:
        seg = by_uid.get(uid)
        if seg is not None:
            words.add(seg.w)
            if seg.lw is not None:
                words.add(seg.lw)
    return tuple(sorted(words))


def _fingerprint(state: State) -> Tuple:
    # Provenance is part of the state: *rāmas* and the `s` that 8.3.34 makes
    # out of a visarga out of a रु out of it are the same letters and NOT the
    # same form, since 8.2.1 shows different rules different pasts.
    return (tuple((s.s, s.w, s.lw, tuple(sorted(s.marks)), s.show, s.made_by)
                  for s in state.segs),
            tuple(sorted(state.declined)))


def derive(
    start: State,
    rules: Sequence[Rule],
    *,
    max_steps: int = MAX_STEPS,
    max_outcomes: int = MAX_OUTCOMES,
) -> Tuple[Outcome, ...]:
    """
    Apply rules to a form until none applies — once for every course the
    options allow.

    The first outcome returned follows every option taken; the others follow
    the refusals, in the order the options were met.
    """
    outcomes: List[Outcome] = []
    #: (state, steps, choices, fingerprints seen)
    pending: List[Tuple[State, Tuple[Step, ...],
                        Tuple[Tuple[str, bool], ...], Tuple]]
    pending = [(start, (), (), (_fingerprint(start),))]

    while pending and len(outcomes) < max_outcomes:
        state, steps, choices, seen = pending.pop()
        stopped = "no rule applies"
        while True:
            if len(steps) >= max_steps:
                stopped = f"stopped at the {max_steps}-step cap"
                break
            found = collect(state, rules)
            if not found:
                break
            (rule, app), displaced = settle(_group(state, found))

            if app.optional:
                # The refusal is a course of its own, taken up afterwards.
                refused = replace(
                    state, declined=state.declined | {(rule.key, app.site)})
                note = Step(
                    n=len(steps) + 1, sutra=rule.sutra, name=rule.name,
                    detail=app.detail, before=state.text(),
                    after=state.text(), words=_words_touched(state, app),
                    against=tuple(d for d in displaced if not d.deferred),
                    option=app.optional, declined=True)
                pending.append((refused, steps + (note,),
                                choices + ((rule.sutra, False),),
                                seen + (_fingerprint(refused),)))
                choices = choices + ((rule.sutra, True),)

            after = apply(state, rule, app)
            if not app.edits:
                # A rule that refuses another: nothing changes, and neither it
                # nor the rules it displaced are offered at this place again.
                # Only what the refusal NAMES stays refused: a rule it
                # displaced by 1.4.2 or 8.2.1, not by an `overrides`, may
                # still have its turn (6.1.104 refuses the general rule for
                # one case and leaves it standing for the next).
                refused_here = {(rule.key, app.site)} | {
                    (d.key, app.site) for d in displaced if d.named}
                after = replace(after,
                                declined=after.declined | refused_here)
            steps = steps + (Step(
                n=len(steps) + 1, sutra=rule.sutra, name=rule.name,
                detail=app.detail, before=state.text(), after=after.text(),
                words=_words_touched(state, app),
                against=tuple(d for d in displaced if not d.deferred),
                option=app.optional),)
            key = _fingerprint(after)
            if key in seen:
                stopped = (f"{rule.sutra} returned the form to one already "
                           f"reached — stopping rather than cycling")
                state = after
                break
            seen = seen + (key,)
            state = after
        outcomes.append(Outcome(start=start, final=state, steps=steps,
                                choices=choices, stopped=stopped))

    # `pending` is LIFO: the option taken was followed first and the refusals
    # after, so `outcomes` already runs "everything taken" first.
    return tuple(outcomes)


__all__ = ["Displaced", "MAX_OUTCOMES", "MAX_STEPS", "Outcome", "Step",
           "apply", "collect", "derive", "settle"]
