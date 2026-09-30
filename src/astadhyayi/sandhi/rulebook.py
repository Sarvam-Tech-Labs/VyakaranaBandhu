# -*- coding: utf-8 -*-
"""
Every rule the engine has, gathered from the family modules.

Discovery is automatic, as in `rules/__init__.py`: a module in `families/` that
defines a module-level `RULES` tuple is picked up by being there. What this
file adds is a check that a rule cannot be registered against a sūtra that does
not exist — every `Rule.sutra` and every `Via.sutra` a rule can produce must be
an id in the Vidyut sūtrapāṭha, so a mistyped number fails at once instead of
printing a citation that points at the wrong rule.
"""

from __future__ import annotations

import importlib
import os
import pkgutil
import re
from functools import lru_cache
from typing import Dict, FrozenSet, List, Tuple

from src.astadhyayi import corpus
from src.astadhyayi import operations
from src.astadhyayi.sandhi import families
from src.astadhyayi.sandhi.rule import Rule


def _modules() -> Tuple[str, ...]:
    return tuple(sorted(
        m.name for m in pkgutil.iter_modules(families.__path__)
        if not m.name.startswith("_")))


@lru_cache(maxsize=1)
def by_family() -> Dict[str, Tuple[Rule, ...]]:
    found: Dict[str, Tuple[Rule, ...]] = {}
    for name in _modules():
        module = importlib.import_module(f"{families.__name__}.{name}")
        rules = getattr(module, "RULES", None)
        if rules:
            found[name] = tuple(rules)
    return found


@lru_cache(maxsize=1)
def all_rules() -> Tuple[Rule, ...]:
    """Every rule, in sūtra order (the order 8.2.1 speaks of)."""
    rules: List[Rule] = []
    for group in by_family().values():
        rules.extend(group)
    rules.sort(key=lambda r: (r.order, r.varttika, r.name))
    return tuple(rules)


@lru_cache(maxsize=1)
def _sources() -> str:
    """The text of every module that could read a word's flags."""
    here = os.path.dirname(os.path.abspath(families.__file__))
    paths = [os.path.join(here, f) for f in sorted(os.listdir(here))
             if f.endswith(".py")]
    paths.append(os.path.join(os.path.dirname(here), "infer.py"))
    parts = []
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            parts.append(handle.read())
    return "\n".join(parts)


def flag_is_read(flag: str) -> bool:
    """
    Whether any rule mentions this flag — `nipata`, or the head of `dhatu:i`.

    A misspelt flag would otherwise switch a rule off without a word: the caller
    writes `nipaata`, no rule reads it, and the vowel is joined as though the
    word were an ordinary one. This asks whether the flag's name appears as a
    quoted word anywhere in the family sources, which is loose (it cannot tell
    a read from a mention) and exactly tight enough to catch a typo.
    """
    head = flag.partition(":")[0]
    return re.search(r"[\"']" + re.escape(head) + r"(?::|[\"'])",
                     _sources()) is not None


def rules_of(*families: str) -> Tuple[Rule, ...]:
    """The rules of the named family modules only, in sūtra order — for a test
    that wants to know what ONE family does, apart from the rest."""
    chosen: List[Rule] = []
    for name in families:
        chosen.extend(by_family()[name])
    chosen.sort(key=lambda r: (r.order, r.varttika, r.name))
    return tuple(chosen)


#: What a family may say of a sūtra in its scope. `rule` is implemented;
#: `partial` is implemented with limits the note states; `support` is a
#: paribhāṣā or saṃjñā the rules lean on and cite (nothing to run); `scope` is
#: deliberately not done and the note says why — the project's own SCOPE
#: marker; `vedic` is Vedic-only.
COVERAGE_STATUS = ("rule", "partial", "support", "scope", "vedic")


def coverage() -> Dict[str, Tuple[Tuple[str, str, str], ...]]:
    """Each family's declared `COVERAGE`: (sūtra, status, note)."""
    found: Dict[str, Tuple[Tuple[str, str, str], ...]] = {}
    for name in _modules():
        module = importlib.import_module(f"{families.__name__}.{name}")
        declared = getattr(module, "COVERAGE", None)
        if declared:
            found[name] = tuple(declared)
    return found


def problems() -> List[str]:
    """Anything wrong with the rulebook itself; empty when it is sound."""
    known = corpus.load_vidyut_sutrapatha()
    out: List[str] = []
    seen: Dict[Tuple[str, str], str] = {}
    for family, group in by_family().items():
        for rule in group:
            if rule.sutra not in known:
                out.append(f"{family}: {rule.name!r} cites {rule.sutra}, "
                           f"which is not a sūtra in the corpus")
            key = (rule.sutra, rule.varttika)
            if key in seen:
                out.append(f"{rule.sutra} is defined in both {seen[key]} and "
                           f"{family}")
            seen[key] = family
            for target, _ in rule.overrides:
                if not target.startswith("@") and target not in known:
                    out.append(f"{rule.sutra} overrides {target}, which is "
                               f"not a sūtra in the corpus")
            if rule.operation and not operations.is_operation(rule.operation):
                out.append(f"{rule.sutra} names the operation "
                           f"{rule.operation!r}, which is not in the "
                           f"vocabulary of operations.py")
    # COVERAGE must be honest: every rule declared, every scope note reasoned.
    declared = coverage()
    for family, group in by_family().items():
        entries = {sutra: (status, note)
                   for sutra, status, note in declared.get(family, ())}
        for rule in group:
            status = entries.get(rule.sutra, ("", ""))[0]
            if status not in ("rule", "partial", "vedic"):
                out.append(f"{family}: rule {rule.sutra} ({rule.name}) is not "
                           f"declared in COVERAGE as rule/partial/vedic")
    for family, entries in declared.items():
        seen_ids = set()
        for sutra, status, note in entries:
            if sutra not in known:
                out.append(f"{family}: COVERAGE names {sutra}, which is not "
                           f"a sūtra in the corpus")
            if status not in COVERAGE_STATUS:
                out.append(f"{family}: COVERAGE {sutra} has status "
                           f"{status!r}, not one of {COVERAGE_STATUS}")
            if status in ("scope", "partial") and len(note.strip()) < 12:
                out.append(f"{family}: COVERAGE {sutra} is {status} but gives "
                           f"no reason — say why")
            seen_ids.add(sutra)
        if len(seen_ids) != len(entries):
            out.append(f"{family}: COVERAGE lists a sūtra twice")
    return out


__all__ = ["COVERAGE_STATUS", "all_rules", "by_family", "coverage",
           "flag_is_read", "problems", "rules_of"]
