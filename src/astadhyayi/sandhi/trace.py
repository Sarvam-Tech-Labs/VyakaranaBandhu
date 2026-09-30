# -*- coding: utf-8 -*-
"""
A derivation, printed so that a beginner and a scholar can each read it.

Every step names its sūtra, **quotes the sūtra's own text from the corpus** (the
Vidyut edition — never retyped, so the citation cannot drift from the rule it
cites), says what kind of operation it was, what was replaced by what and why,
and lists the further sūtras it leans on. Every Sanskrit form is printed in
both scripts, देवनागरी (iast), in one shape; the reader never has to hold two
scripts in mind at once.
"""

from __future__ import annotations

import re
from functools import lru_cache
from typing import Any, Dict, List

from src.astadhyayi import corpus
from src.astadhyayi.sandhi.engine import Outcome, Step
from src.astadhyayi.sandhi.rule import Via
from src.normalizer import iast_to_devanagari

_TERM = re.compile(r"\{([^{}]+)\}")


def deva(iast: str) -> str:
    """IAST → Devanāgarī, the avagraha included. Pratyāhāra letters are
    written in capitals in IAST (aC, iK); the convertor wants lower case."""
    iast = iast.replace("{", "").replace("}", "")
    return iast_to_devanagari(iast.lower().replace("’", "'")) if iast else ""


def both(iast: str) -> str:
    """A form in both scripts — देवनागरी (iast) — and never in one."""
    iast = iast.replace("{", "").replace("}", "")
    return f"{deva(iast)} ({iast})" if iast else ""


def terms_in_both(text: str) -> str:
    """Print every {term} of a sentence as इक् (ik)."""
    return _TERM.sub(lambda m: both(m.group(1)), text)


@lru_cache(maxsize=None)
def sutra_text(sutra_id: str) -> str:
    """The sūtra as the corpus has it, IAST."""
    found = corpus.load_vidyut_sutrapatha().get(sutra_id)
    return found.text if found else ""


def cite(sutra_id: str) -> str:
    """'6.1.77 इको यणचि (iko yaṇaci)' — the number and the exact words."""
    text = sutra_text(sutra_id)
    return f"{sutra_id} {both(text)}" if text else sutra_id


def _via(via: Via) -> Dict[str, Any]:
    return {"sutra": via.sutra, "text_iast": sutra_text(via.sutra),
            "text_deva": deva(sutra_text(via.sutra)),
            "role": terms_in_both(via.role)}


def step_dict(step: Step) -> Dict[str, Any]:
    d = step.detail
    return {
        "n": step.n,
        "sutra": step.sutra,
        "sutra_iast": sutra_text(step.sutra),
        "sutra_deva": deva(sutra_text(step.sutra)),
        "name": step.name,
        "kind": d.kind,
        "authority": d.authority,
        "varttika": d.varttika,
        "before": step.before, "before_deva": deva(step.before),
        "after": step.after, "after_deva": deva(step.after),
        "sthanin": d.sthanin, "sthanin_deva": deva(d.sthanin),
        "adesa": d.adesa, "adesa_deva": deva(d.adesa),
        "nimitta": terms_in_both(d.nimitta),
        "because": terms_in_both(d.because),
        "via": [_via(v) for v in d.via],
        "option": step.option, "declined": step.declined,
        "against": [{"sutra": a.sutra, "name": a.name, "why": a.why}
                    for a in step.against],
        "words": list(step.words),
        "note": d.note,
    }


def outcome_dict(outcome: Outcome) -> Dict[str, Any]:
    return {
        "surface": outcome.surface,
        "surface_deva": deva(outcome.surface),
        "text": outcome.text(),
        "text_deva": deva(outcome.text()),
        "steps": [step_dict(s) for s in outcome.steps],
        "choices": [{"sutra": s, "taken": t} for s, t in outcome.choices],
        "stopped": outcome.stopped,
        "assumptions": assumptions(outcome),
    }


def render_step(step: Step) -> str:
    d = step.detail
    head = f"{step.n:>2}. {cite(step.sutra)}"
    if d.authority != "sūtra":
        head += f"  [{d.authority}]"
    lines = [head]
    if step.declined:
        lines.append(f"      optional ({step.option}) — NOT applied in this "
                     f"course: {both(step.before)}")
    else:
        arrow = (f"{both(step.before)}  →  {both(step.after)}"
                 if step.before != step.after else both(step.before))
        lines.append(f"      {d.kind}: {arrow}")
        if d.sthanin or d.adesa:
            change = f"{both(d.sthanin)} → {both(d.adesa)}" if d.adesa \
                else f"{both(d.sthanin)} is not changed" \
                if d.kind in ("pratiṣedha", "prakṛtibhāva") \
                else f"{both(d.sthanin)} is lost"
            lines.append(f"      sthānin → ādeśa: {change}")
        if step.option:
            lines.append(f"      an option ({step.option}): this course takes it")
    if d.because:
        lines.append(f"      why: {terms_in_both(d.because)}")
    for via in d.via:
        lines.append(f"      · {cite(via.sutra)} — {terms_in_both(via.role)}")
    for lost in step.against:
        lines.append(f"      ✕ {cite(lost.sutra)} did not apply here — "
                     f"{terms_in_both(lost.why)}")
    return "\n".join(lines)


def assumptions(outcome: Outcome) -> List[str]:
    """What the parser filled in, as sentences — never left silent."""
    lines: List[str] = []
    for word in outcome.start.words:
        for flag, why in word.inferred:
            lines.append(f"assumed for {both(word.given or word.text)}: "
                         f"{flag} — {terms_in_both(why)}")
    return lines


def render(outcome: Outcome, *, title: str = "") -> str:
    out: List[str] = []
    if title:
        out.append(title)
    out.append(f"     {both(outcome.start.text())}")
    out.extend(f"     ({line})" for line in assumptions(outcome))
    for step in outcome.steps:
        out.append(render_step(step))
    result = both(outcome.surface)
    spaced = outcome.text()
    if spaced != outcome.surface:
        result += f"   (the words still standing apart: {both(spaced)})"
    out.append(f"  ⇒  {result}"
               + (f"    [{outcome.stopped}]"
                  if outcome.stopped != "no rule applies" else ""))
    return "\n".join(out)


__all__ = ["assumptions", "both", "cite", "deva", "outcome_dict", "render", "render_step",
           "step_dict", "sutra_text", "terms_in_both"]
