# -*- coding: utf-8 -*-
"""
A sandhi engine that derives every junction from the Aṣṭādhyāyī and cites the
sūtra for every step.

    >>> from src.astadhyayi.sandhi import sandhi
    >>> result = sandhi("iti ādi")
    >>> result.surface
    'ityādi'
    >>> print(result.trace())

Nothing here looks a junction up. Each step is a sūtra applied to the form, the
sūtra's own text is quoted from the corpus, and each choice the grammar makes
— which sūtra wins where two apply (1.4.2), what a tripādī rule may and may not
see (8.2.1), which sound is nearest (1.1.50) — is asked of the rule that makes
it, not decided in the loop. `README.md` in this directory says how.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from src.astadhyayi.sandhi import trace as _trace
from src.astadhyayi.sandhi.engine import Outcome, Step, derive
from src.astadhyayi.sandhi.parse import SandhiInputError, parse, to_iast
from src.astadhyayi.sandhi.rule import Rule
from src.astadhyayi.sandhi.rulebook import all_rules
from src.astadhyayi.sandhi.segs import (
    ANGA, PADA, SAMASA, UPASARGA, State, Word)


@dataclass(frozen=True)
class SandhiResult:
    """What a junction gives — every form the grammar allows, each derived."""

    start: State
    outcomes: Tuple[Outcome, ...]
    #: Things the caller should know that are not part of any derivation — a
    #: flag no rule reads, which would otherwise change nothing without a word.
    warnings: Tuple[str, ...] = ()

    @property
    def surface(self) -> str:
        """The first form: every option taken, joined without spaces."""
        return self.outcomes[0].surface

    @property
    def surfaces(self) -> Tuple[str, ...]:
        """Every distinct form, in the order the derivations were run."""
        seen: List[str] = []
        for outcome in self.outcomes:
            if outcome.surface not in seen:
                seen.append(outcome.surface)
        return tuple(seen)

    def trace(self) -> str:
        parts = []
        for index, outcome in enumerate(self.outcomes, 1):
            title = (f"── derivation {index} of {len(self.outcomes)} ──"
                     if len(self.outcomes) > 1 else "")
            parts.append(_trace.render(outcome, title=title))
        text = "\n\n".join(parts)
        if self.warnings:
            text += "\n\n" + "\n".join(f"  ! {w}" for w in self.warnings)
        return text

    def to_dict(self) -> Dict[str, Any]:
        return {
            "input": self.start.text(),
            "input_deva": _trace.deva(self.start.text()),
            "surfaces": list(self.surfaces),
            "surfaces_deva": [_trace.deva(s) for s in self.surfaces],
            "warnings": list(self.warnings),
            "outcomes": [_trace.outcome_dict(o) for o in self.outcomes],
        }


def sandhi(
    spec: Union[str, Sequence[Union[str, Word]]],
    *,
    boundary: str = PADA,
    veda: bool = False,
    pause: bool = True,
    infer: bool = True,
    rules: Optional[Sequence[Rule]] = None,
) -> SandhiResult:
    """
    Join the words of `spec`, deriving each change from its sūtra.

    `rules` restricts the derivation to a chosen set of rules (see
    `rulebook.rules_of`); by default every rule of every family is used.
    """
    start = parse(spec, boundary=boundary, veda=veda, pause=pause,
                  infer=infer)
    return SandhiResult(
        start=start,
        outcomes=derive(start, all_rules() if rules is None else rules),
        warnings=_unread_flags(start))


def _unread_flags(state: State) -> Tuple[str, ...]:
    """A flag the caller gave that no rule reads: said, never silent."""
    from src.astadhyayi.sandhi.rulebook import flag_is_read

    out = []
    for word in state.words:
        for flag in sorted(word.flags):
            if not flag_is_read(flag):
                out.append(f"the flag {flag!r} on {word.given or word.text!r} "
                           f"is read by no rule, so it changes nothing — "
                           f"is it misspelt?")
    return tuple(out)


join = sandhi

__all__ = ["ANGA", "PADA", "SAMASA", "SandhiInputError", "SandhiResult",
           "Step", "UPASARGA", "Word", "join", "sandhi", "to_iast"]
