# -*- coding: utf-8 -*-
"""
What the web UI needs from the codification, in JSON-ready shapes.

Four things: a list to browse, one sūtra in full, the graph of what a sūtra
depends on, and a way to run its rule. The first three are here; running is in
playground.py.

The graph is the part worth explaining. A sūtra in the Aṣṭādhyāyī is not a
self-contained statement — it is read together with words carried down from
earlier sūtras, under a heading that may be pages back, and against
cross-references that the codification records by hand. Three different kinds
of dependency, and a reader needs to see which is which:

    anuvṛtti   a word from an earlier sūtra is read into this one. The corpus
               records these for all 3,983, with the word and its source.
    adhikāra   a heading whose scope this sūtra falls under.
    related    a cross-reference the codification added — the sūtra this one
               overrides, feeds, or is tested against.

The first two are the grammar's own; the third is ours, and is marked as such.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from src.astadhyayi.corpus import commentary_on
from src.astadhyayi.glosses import gloss_for
from src.astadhyayi.cases import cases_for
from src.astadhyayi.playground import jsonable, spec_for
from src.astadhyayi.report import findings
from src.astadhyayi.sources import all_sutra_ids, facts
from src.astadhyayi.sutra import REGISTRY, Source, Status


def _codified() -> Dict[str, Any]:
    return {str(sutra.id): sutra for sutra in REGISTRY.all()}


def catalogue() -> Dict[str, Any]:
    """Everything codified, in reading order, with enough to build a list."""
    rows = []
    for sutra in REGISTRY.all():
        found = findings(sutra.notes)
        marks = [marker for marker, _ in found]
        rows.append({
            "id": str(sutra.id),
            "devanagari": sutra.devanagari,
            "iast": sutra.iast,
            "type": facts(str(sutra.id)).type_label or sutra.type.name,
            "open": "OPEN" in marks,
            "scope": "SCOPE" in marks,
            "findings": len(marks),
            # The unresolved findings in full, not just a count. The list marks
            # these with a dot, and a dot that has to be explained is not
            # transparent — the reader should be able to see WHAT is open
            # without leaving the list.
            "outstanding": [
                {"marker": marker, "text": text}
                for marker, text in found
                if marker in ("OPEN", "SCOPE")
            ],
        })
    total = len(all_sutra_ids())
    return {
        "sutras": rows,
        "codified": len(rows),
        "total": total,
        "pada_complete": _complete_padas(),
    }


def _complete_padas() -> List[str]:
    """Which pādas are codified end to end — worth showing as a milestone."""
    by_pada: Dict[str, List[str]] = {}
    for sutra_id in all_sutra_ids():
        adhyaya, pada, _ = sutra_id.split(".")
        by_pada.setdefault(f"{adhyaya}.{pada}", []).append(sutra_id)
    done = _codified()
    return [
        pada for pada, members in by_pada.items()
        if all(member in done for member in members)
    ]


def _gloss(sutra_id: str) -> Dict[str, str]:
    written = gloss_for(sutra_id)
    return {
        "plain": written.plain if written else "",
        "example": written.example if written else "",
        "sutrartha": commentary_on(sutra_id, "sutrartha_english") or "",
    }


def _kind(sutra_id: str) -> Optional[Dict[str, str]]:
    from src.astadhyayi.glosses import kind_of

    kind = kind_of(sutra_id)
    if kind is None:
        return None
    return {"label": kind.label, "plain": kind.plain}


def detail(sutra_id: str) -> Dict[str, Any]:
    """One sūtra, with everything the record holds about it."""
    sutra = REGISTRY.get(sutra_id)
    fact = facts(sutra_id)
    spec = spec_for(sutra_id)

    return {
        "id": sutra_id,
        "devanagari": sutra.devanagari,
        "iast": sutra.iast,
        "type": fact.type_label or sutra.type.name,
        "summary": fact.summary,
        # For a reader meeting the rule for the first time: our own plain
        # sentence with the terms in both scripts, a worked form, and the
        # sūtrārtha from the corpus beside it where there is one. The last is
        # a source and is attributed; the first two are not.
        # Before the gloss, for a reader who does not yet know what a
        # saṃjñā rule *is*. Written per kind rather than per sūtra: the
        # question "why does a grammar open by naming three vowels" has one
        # answer for all 200 of them.
        "kind": _kind(sutra_id),
        "gloss": _gloss(sutra_id),
        "padaccheda": [
            {
                "word": pada.word,
                "case": pada.case_name,
                "vibhakti": pada.vibhakti,
                "vacana": pada.vacana,
                "display": str(pada),
            }
            for pada in fact.padas
        ],
        "anuvrtti": [
            {"word": item.word, "from": item.from_sutra}
            for item in fact.anuvrtti
        ],
        "adhikara": [
            {"sutra": item.sutra, "text": getattr(item, "text", "")}
            for item in fact.adhikara
        ],
        "related": list(sutra.related),
        "codification": sutra.codification,
        "findings": [
            {"marker": marker, "text": text}
            for marker, text in findings(sutra.notes)
        ],
        "sources": [
            {
                "source": reading.source.value,
                "status": reading.status.value,
                "locator": reading.locator,
                "text": reading.text,
                "note": reading.note,
            }
            for reading in sutra.readings
        ],
        "playground": {
            "function": spec.function,
            "doc": spec.doc,
            "runnable": spec.runnable,
            "note": spec.note,
            "fields": [
                {
                    "name": field.name,
                    "label": field.label,
                    "hint": field.hint,
                    "kind": field.kind,
                    # Through the serialiser: a default can be a frozenset
                    # (Adesa.its) or an Enum, and neither survives json.dumps.
                    "default": jsonable(field.default),
                    "options": list(field.options),
                    "group": field.group,
                }
                for field in spec.fields
            ],
            # Ready-made inputs. A form with eight empty boxes cannot be used
            # by someone meeting the rule for the first time — they would have
            # to know the answer to fill it in.
            "cases": [
                {
                    "label": case.label,
                    "kind": case.kind,
                    "note": case.note,
                    "values": {k: jsonable(v) for k, v in case.values.items()},
                }
                for case in cases_for(sutra_id)
            ],
        },
    }


# ---------------------------------------------------------------------------
# The dependency graph
# ---------------------------------------------------------------------------

_ANUVRTTI = "anuvṛtti"
_ADHIKARA = "adhikāra"
_RELATED = "related"


def _node(sutra_id: str, done: Dict[str, Any]) -> Dict[str, Any]:
    try:
        fact = facts(sutra_id)
        devanagari = fact.devanagari
    except Exception:                       # noqa: BLE001 — an id we cannot resolve
        devanagari = ""
    return {
        "id": sutra_id,
        "devanagari": devanagari,
        "codified": sutra_id in done,
    }


#: A walk this long means something has gone wrong in the data. The corpus
#: is transitive, so the frontier is normally empty after two rounds.
_MAX_ROUNDS = 12


def graph(sutra_id: str) -> Dict[str, Any]:
    """
    Everything this sūtra hangs on — the whole ancestry, in one call.

    Anuvṛtti and adhikāra point backward: a sūtra is read with words from
    earlier ones, under headings that precede it, so following them walks up
    the text. `related` is not directional in the same way and is followed
    only from the root, or the graph fills with the whole pāda.

    There is no depth parameter, and the reason is worth recording. There
    was one, offering 1, 2 and 3, and it was close to inert: the corpus's
    adhikāra field already lists *every* heading over a sūtra rather than
    the nearest, so one step reaches the top of the chain and a second finds
    nothing. Across the codified sūtras, depth 2 added no node for 220 of
    379 and depth 3 for 311. Where it did change the picture it was by
    drawing edges between ancestors already on screen — 2.1.6 from 4 edges
    to 10 across the same five nodes — which reads as an explosion of new
    information when none has arrived.

    So the walk simply runs until the frontier is empty. Each edge carries
    `cross`: false where it touches the root, true where it links two of its
    ancestors to each other. That is the distinction the depth control was
    accidentally exposing, and it is one a reader can be shown by name.
    """
    done = _codified()
    nodes: Dict[str, Dict[str, Any]] = {}
    edges: List[Dict[str, str]] = []
    seen_edges = set()

    def add_edge(source: str, target: str, kind: str, label: str = "") -> None:
        key = (source, target, kind, label)
        if key in seen_edges:
            return
        seen_edges.add(key)
        edges.append({
            "from": source, "to": target, "kind": kind, "label": label,
            # An edge between two ancestors, neither of them the sūtra the
            # reader asked about. Useful, and much the larger number, so the
            # page hides them until asked.
            "cross": source != sutra_id and target != sutra_id,
        })

    frontier = [sutra_id]
    nodes[sutra_id] = dict(_node(sutra_id, done), root=True, distance=0)

    for step in range(_MAX_ROUNDS):
        next_frontier: List[str] = []
        for current in frontier:
            try:
                fact = facts(current)
            except Exception:               # noqa: BLE001
                continue

            for item in fact.anuvrtti:
                source = item.from_sutra
                if source not in nodes:
                    nodes[source] = dict(
                        _node(source, done), root=False, distance=step + 1
                    )
                    next_frontier.append(source)
                add_edge(source, current, _ANUVRTTI, item.word)

            for item in fact.adhikara:
                source = item.sutra
                if source == current:
                    continue
                if source not in nodes:
                    nodes[source] = dict(
                        _node(source, done), root=False, distance=step + 1
                    )
                    next_frontier.append(source)
                add_edge(source, current, _ADHIKARA, "")

            if step == 0 and current in done:
                for other in done[current].related:
                    if other not in nodes:
                        nodes[other] = dict(
                            _node(other, done), root=False, distance=1
                        )
                    add_edge(current, other, _RELATED, "")

        frontier = next_frontier
        if not frontier:
            break

    return {
        "root": sutra_id,
        "nodes": list(nodes.values()),
        "edges": edges,
        "cross_links": sum(1 for edge in edges if edge["cross"]),
        "kinds": {
            _ANUVRTTI: "a word carried down into this sūtra",
            _ADHIKARA: "a heading whose scope this falls under",
            _RELATED: "a cross-reference recorded by the codification",
        },
    }


def dependents(sutra_id: str) -> List[Dict[str, str]]:
    """
    The other way round: which sūtras read a word down from this one.

    Cheap enough to do exhaustively — the corpus holds anuvṛtti for all 3,983 —
    and it is the question a reader actually asks of a sūtra like 1.1.49,
    whose whole point is what it governs.
    """
    out = []
    for other in all_sutra_ids():
        for item in facts(other).anuvrtti:
            if item.from_sutra == sutra_id:
                out.append({"id": other, "word": item.word})
    return out


__all__ = ["catalogue", "dependents", "detail", "graph"]
