# -*- coding: utf-8 -*-
"""
Running the engine against cases from outside — gold from the commentaries and
whole datasets from other people's work — and saying what a mismatch means.

The point of an external case is that **somebody else decided its answer**. So
a pass proves something the engine's own tests cannot, and a miss is a lead:
it may be an engine fault, a wrong or under-specified case, or a place the
engine deliberately does not go. The harness does not decide which. It reports
the miss with everything needed to decide, and clusters misses so a hundred
thousand rows read as thirty patterns rather than as a hundred thousand.

**What "matches" means.**

* Outputs are compared *joined*: spaces and hyphens removed, the avagraha
  written ``'``. A source that prints ``rāmo 'tra`` and an engine that returns
  ``rāmo'tra`` agree.
* A case lists the forms its source accepts. The engine must produce **every
  one** of them (a source may list only one of several options, so an extra form
  from the engine is not a miss)...
* ...except for a **counter-example** (a case showing a rule must NOT apply) and a case
  marked ``exhaustive``, where the engine's set must equal the case's: an
  engine that also produces the joined form has over-applied.

**Under-specified inputs.** Datasets give words in their *pausal* form — with a
final visarga where the grammar starts from स् or र्. The engine reads a visarga as
स् (see `parse`); a word from र् would then be wrong through no fault of the
engine. So a row whose words end in visarga is tried under each reading
(`final:s`, `final:r`, at most three such words) and counts as matching if any
does — and the reading that matched is *recorded*, so it is a stated allowance
and not a hidden one.
"""

from __future__ import annotations

import itertools
import json
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple

from src.astadhyayi.sandhi import SandhiInputError, sandhi
from src.astadhyayi.sandhi.parse import boundary_kind
from src.astadhyayi.sandhi.segs import PADA, Word
from src.astadhyayi.varna import VISARGA

#: The most visarga-final words tried under both readings in one row.
MAX_VARIANT_WORDS = 3


def joined(text: str, *, ignore_avagraha: bool = False,
           norm_nasal: bool = False) -> str:
    """
    A form as it is compared: NFC, no spaces or hyphens, avagraha as '.

    `ignore_avagraha` drops the avagraha altogether, for a dataset that writes it
    for an elided अ (`vā'mutra`) where the engine, given the separate words,
    derives `vāmutra` (6.1.101). It is a statement about the dataset's spelling,
    so it is opt-in and off by default.
    `norm_nasal` normalizes alternative representations of anunāsika (such as
    a following 'm̐' vs candrabindu on the preceding vowel).
    """
    text = unicodedata.normalize("NFC", text).replace("’", "'")
    if norm_nasal:
        text = text.replace("m̐", "̐")
    drop = " -·'" if ignore_avagraha else " -·"
    return "".join(c for c in text if c not in drop)


@dataclass(frozen=True)
class CaseResult:
    id: str
    ok: bool
    #: match | missing | extra | error | skipped
    verdict: str
    expected: Tuple[str, ...]
    got: Tuple[str, ...]
    #: Which reading of the underspecified visarga matched, "" if none needed.
    reading: str = ""
    #: The sūtras of the derivation that matched (else the first), for
    #: clustering.
    steps: Tuple[str, ...] = ()
    #: For a row that names the sūtra it illustrates: whether the derivation
    #: cites it, in a step or among the sūtras a step leans on. None where the
    #: row names no sūtra. This tests the citation, not only the form.
    cited: Optional[bool] = None
    detail: str = ""
    words: Tuple[str, ...] = ()
    junction: Tuple[str, str] = ("", "")


def _flags_of(case: Dict[str, Any]) -> Dict[int, Tuple[str, ...]]:
    raw = case.get("flags") or {}
    return {int(k): tuple(v) for k, v in raw.items()}


def _words(case: Dict[str, Any], readings: Dict[int, str]) -> List[Word]:
    flags = _flags_of(case)
    out: List[Word] = []
    for index, text in enumerate(case["input"]):
        f = set(flags.get(index, ()))
        if index in readings:
            f.add(f"final:{readings[index]}")
        out.append(Word(text=text, given=text, flags=frozenset(f)))
    return out


def _visarga_words(case: Dict[str, Any]) -> List[int]:
    return [i for i, w in enumerate(case["input"])
            if len(w) > 1 and w.endswith(VISARGA)
            and not any(f.startswith("final:")
                        for f in _flags_of(case).get(i, ()))]


def _readings(case: Dict[str, Any]) -> Iterator[Dict[int, str]]:
    marked = _visarga_words(case)
    if not marked or len(marked) > MAX_VARIANT_WORDS:
        yield {}
        return
    for combo in itertools.product("sr", repeat=len(marked)):
        yield dict(zip(marked, combo))


def _junction(case: Dict[str, Any]) -> Tuple[str, str]:
    words = case["input"]
    if len(words) != 2:
        return ("", "")
    return (words[0][-1:], words[1][:1])


def expected_forms(case: Dict[str, Any], *,
                   ignore_avagraha: bool = False,
                   norm_nasal: bool = False) -> Tuple[str, ...]:
    """The forms a case accepts, joined, from either schema."""
    if "outputs" in case:
        forms = case["outputs"]
    else:
        forms = [case["output"]]
    return tuple(dict.fromkeys(joined(f, ignore_avagraha=ignore_avagraha,
                                      norm_nasal=norm_nasal)
                               for f in forms if f))


def run_case(case: Dict[str, Any], *, rules=None,
             default_boundary: str = PADA,
             ignore_avagraha: bool = False,
             norm_nasal: bool = False) -> CaseResult:
    """
    One case against the engine.

    `default_boundary` is the junction kind for a row that does not say
    (`boundary` absent or "unknown"): a corpus of words inside words — the
    SandhiKosh *internal* corpus — is `anga`; one of separate words is `pada`.
    """
    cid = str(case.get("id", "?"))
    expected = expected_forms(case, ignore_avagraha=ignore_avagraha,
                              norm_nasal=norm_nasal)

    def j(text: str) -> str:
        return joined(text, ignore_avagraha=ignore_avagraha, norm_nasal=norm_nasal)
    words = tuple(case.get("input") or ())
    junction = _junction(case)
    if not words or not expected:
        return CaseResult(cid, False, "skipped", expected, (), words=words,
                          junction=junction, detail="no input or no output")
    strict = bool(case.get("counter_example") or case.get("exhaustive"))
    try:
        boundary = boundary_kind(case.get("boundary")) \
            if case.get("boundary") not in (None, "unknown") \
            else boundary_kind(default_boundary)
    except SandhiInputError:
        boundary = PADA

    best: Optional[CaseResult] = None
    for reading in _readings(case):
        try:
            result = sandhi(_words(case, reading), boundary=boundary,
                            veda=bool(case.get("veda") or case.get("vedic")),
                            rules=rules)
        except SandhiInputError as exc:
            return CaseResult(cid, False, "error", expected, (), words=words,
                              junction=junction, detail=str(exc))
        except Exception as exc:                       # an engine fault
            return CaseResult(cid, False, "error", expected, (), words=words,
                              junction=junction,
                              detail=f"{type(exc).__name__}: {exc}")
        got = tuple(dict.fromkeys(j(s) for s in result.surfaces))
        chosen = next((o for o in result.outcomes
                       if j(o.surface) in expected), result.outcomes[0])
        steps = tuple(s.sutra for s in chosen.steps if not s.declined)
        cited = _cited(case.get("rule"), chosen)
        label = ",".join(f"{i}={r}" for i, r in sorted(reading.items()))
        if strict:
            ok = set(got) == set(expected)
            verdict = "match" if ok else (
                "extra" if set(expected) <= set(got) else "missing")
        else:
            ok = set(expected) <= set(got)
            verdict = "match" if ok else "missing"
        candidate = CaseResult(cid, ok, verdict, expected, got, label, steps,
                               cited=cited, words=words, junction=junction)
        if ok:
            return candidate
        if best is None:
            best = candidate
    assert best is not None
    return best


_SUTRA_ID = re.compile(r"^[1-8]\.[1-4]\.\d{1,3}$")


def _cited(label: Any, outcome) -> Optional[bool]:
    """Whether `outcome` cites the sūtra `label` names (None if it names none)."""
    if not isinstance(label, str) or not _SUTRA_ID.match(label.strip()):
        return None
    wanted = label.strip()
    named = set()
    for step in outcome.steps:
        named.add(step.sutra)
        named.update(v.sutra for v in step.detail.via)
        named.update(a.sutra for a in step.against)
    return wanted in named


def load_jsonl(path: str) -> Iterator[Dict[str, Any]]:
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def load_gold(path: str) -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


@dataclass
class Summary:
    total: int = 0
    by_verdict: Counter = field(default_factory=Counter)
    #: (left final, right initial) → verdict counts, two-word rows only
    by_junction: Dict[Tuple[str, str], Counter] = field(
        default_factory=lambda: defaultdict(Counter))
    #: a short signature of the engine's steps → verdict counts
    by_steps: Dict[Tuple[str, ...], Counter] = field(
        default_factory=lambda: defaultdict(Counter))
    misses: List[CaseResult] = field(default_factory=list)
    readings_used: Counter = field(default_factory=Counter)
    #: Rows that name a sūtra: (matched, cited) → count, over matching rows.
    citation: Counter = field(default_factory=Counter)
    #: The labelled sūtras the derivation did not cite, on rows that matched.
    uncited: Counter = field(default_factory=Counter)

    def add(self, result: CaseResult, keep: int = 500) -> None:
        self.total += 1
        self.by_verdict[result.verdict] += 1
        if result.junction != ("", ""):
            self.by_junction[result.junction][result.verdict] += 1
        self.by_steps[result.steps][result.verdict] += 1
        if result.reading:
            self.readings_used[result.reading] += 1
        if result.cited is not None and result.ok:
            self.citation[result.cited] += 1
            if not result.cited:
                self.uncited[result.id] += 1
        if not result.ok and len(self.misses) < keep:
            self.misses.append(result)

    @property
    def matched(self) -> int:
        return self.by_verdict["match"]

    def rate(self) -> float:
        return self.matched / self.total if self.total else 0.0

    def worst_junctions(self, n: int = 20
                        ) -> List[Tuple[Tuple[str, str], int, int]]:
        rows = [(j, c["match"], sum(c.values()) - c["match"])
                for j, c in self.by_junction.items()]
        rows.sort(key=lambda r: (-r[2], r[0]))
        return [r for r in rows if r[2]][:n]

    def report(self, show: int = 15) -> str:
        lines = [f"{self.total} cases: "
                 + ", ".join(f"{v} {k}" for k, v in
                             sorted(self.by_verdict.items())),
                 f"match rate {self.rate():.1%}"]
        if self.citation:
            good, bad = self.citation[True], self.citation[False]
            lines.append(
                f"citation: of {good + bad} matching rows that name a sūtra, "
                f"{good} cite it ({good / (good + bad):.1%})")
        if self.readings_used:
            lines.append("visarga readings that were needed: "
                         + ", ".join(f"{k}×{v}" for k, v in
                                     self.readings_used.most_common(5)))
        worst = self.worst_junctions()
        if worst:
            lines.append("junctions with the most misses "
                         "(left final, right initial: matched / missed):")
            lines.extend(f"  {a!r:>6} + {b!r:<6} {m:>6} / {x}"
                         for (a, b), m, x in worst)
        if self.misses:
            lines.append(f"first {min(show, len(self.misses))} misses:")
            for r in self.misses[:show]:
                lines.append(
                    f"  [{r.verdict}] {r.id}: {' + '.join(r.words)}  "
                    f"expected {list(r.expected)}  engine {list(r.got)}"
                    + (f"  ({r.detail})" if r.detail else "")
                    + (f"  steps {'→'.join(r.steps)}" if r.steps else ""))
        return "\n".join(lines)


def evaluate(cases: Iterable[Dict[str, Any]], *, limit: Optional[int] = None,
             rules=None, default_boundary: str = PADA,
             ignore_avagraha: bool = False,
             norm_nasal: bool = False) -> Summary:
    summary = Summary()
    for count, case in enumerate(cases):
        if limit is not None and count >= limit:
            break
        summary.add(run_case(case, rules=rules,
                             default_boundary=default_boundary,
                             ignore_avagraha=ignore_avagraha,
                             norm_nasal=norm_nasal))
    return summary


__all__ = ["CaseResult", "Summary", "evaluate", "expected_forms", "joined",
           "load_gold", "load_jsonl", "run_case"]
