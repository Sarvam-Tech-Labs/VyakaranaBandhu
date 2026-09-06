# -*- coding: utf-8 -*-
"""
Where the codification stands.

Run it:  python -m src.astadhyayi.report            the summary
         python -m src.astadhyayi.report --open     just the open questions
         python -m src.astadhyayi.report --full     every sūtra in detail
         python -m src.astadhyayi.report 1.1.9      one sūtra in detail

The point is to be honest rather than encouraging. It counts what is actually
codified against the whole text, shows which sources have been read for each
sūtra and which have not, and collects every question still marked OPEN so that
nothing quietly stays unresolved because it was written down once and forgotten.
"""

from __future__ import annotations

import sys
from typing import Dict, List, Tuple

import src.astadhyayi.rules  # noqa: F401  — importing populates the registry
from src.astadhyayi.sources import all_sutra_ids, facts
from src.astadhyayi.sutra import REGISTRY, Source, Status

BAR_WIDTH = 44


def _bar(done: int, total: int, width: int = BAR_WIDTH) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "·" * (width - filled)


def findings(notes: str) -> List[Tuple[str, str]]:
    """The marked paragraphs of a note, as (marker, text)."""
    out = []
    for para in notes.split("\n\n"):
        stripped = para.strip()
        for marker in ("SETTLED", "OPEN", "SCOPE", "IMPLEMENTATION"):
            if stripped.startswith(marker):
                body = stripped[len(marker):].lstrip(" —-")
                out.append((marker, " ".join(body.split())))
                break
    return out


def summary() -> str:
    total = len(all_sutra_ids())
    done = REGISTRY.all()
    lines = [
        "",
        "  Aṣṭādhyāyī — codification status",
        "  " + "─" * 62,
        f"  {len(done)} of {total} sūtras codified   {_bar(len(done), total)}"
        f"  {100 * len(done) / total:.2f}%",
        "",
    ]

    # Which sources have been read, across everything codified.
    read: Dict[str, int] = {}
    blocked: Dict[str, str] = {}
    for sutra in done:
        for status, sources in sutra.coverage().items():
            for source in sources:
                if status == Status.VERIFIED.value:
                    read[source] = read.get(source, 0) + 1
                elif status == Status.UNREADABLE.value:
                    blocked.setdefault(source, "")
    for sutra in done:
        for reading in sutra.readings:
            if reading.status is Status.UNREADABLE and reading.source.value in blocked:
                blocked[reading.source.value] = reading.note
    if read:
        lines.append("  Sources read, by sūtra:")
        for source in sorted(read, key=lambda s: -read[s]):
            lines.append(f"    {source:<28} {read[source]:>3} / {len(done)}")
        lines.append("")
    if blocked:
        lines.append("  Here but unreadable — needs a better copy, not a reader:")
        for source, why in sorted(blocked.items()):
            lines.append(f"    {source}")
            for chunk in _wrap(why, 62):
                lines.append(f"      {chunk}")
        lines.append("")
    unread = [
        s.value for s in Source
        if s.value not in read and s.value not in blocked
    ]
    if unread:
        lines.append("  Not consulted anywhere yet:")
        lines.append(f"    {', '.join(unread)}")
        lines.append("")

    counts: Dict[str, int] = {}
    for sutra in done:
        for marker, _ in findings(sutra.notes):
            counts[marker] = counts.get(marker, 0) + 1
    lines.append(
        "  Findings: "
        + ", ".join(f"{n} {m.lower()}" for m, n in sorted(counts.items()))
    )
    lines.append("")

    lines.append("  Codified:")
    for sutra in done:
        marks = dict(findings(sutra.notes))
        flag = " ←  open" if "OPEN" in marks else ""
        lines.append(f"    {str(sutra.id):<9} {sutra.devanagari}{flag}")
    lines.append("")
    return "\n".join(lines)


def open_questions() -> str:
    lines = ["", "  Still open", "  " + "─" * 62]
    found = False
    for sutra in REGISTRY.all():
        for marker, body in findings(sutra.notes):
            if marker not in ("OPEN", "SCOPE"):
                continue
            found = True
            lines.append("")
            lines.append(f"  {sutra.id}  [{marker}]  {sutra.devanagari}")
            for chunk in _wrap(body, 66):
                lines.append(f"      {chunk}")
    if not found:
        lines.append("  nothing outstanding.")
    lines.append("")
    return "\n".join(lines)


def _wrap(text: str, width: int) -> List[str]:
    words, out, line = text.split(), [], ""
    for word in words:
        if len(line) + len(word) + 1 > width:
            out.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        out.append(line)
    return out


def detail(sutra_id: str) -> str:
    sutra = REGISTRY.get(sutra_id)
    fact = facts(sutra_id)
    lines = [
        "",
        f"  {sutra.id}  {sutra.devanagari}",
        f"  {' ' * len(str(sutra.id))}  {sutra.iast}",
        "  " + "─" * 62,
        f"  type       {fact.type_label or sutra.type.name}",
        f"  padaccheda {' / '.join(str(p) for p in fact.padas)}",
    ]
    if sutra.anuvrtti:
        lines.append(f"  anuvṛtti   {', '.join(sutra.anuvrtti)}")
    if sutra.adhikara:
        lines.append(f"  adhikāra   {sutra.adhikara}")
    if sutra.related:
        lines.append(f"  related    {', '.join(sutra.related)}")
    lines.append("")
    lines.append(f"  codified   {sutra.codification}")
    lines.append("")
    lines.append("  sources")
    for status, sources in sorted(sutra.coverage().items()):
        lines.append(f"    {status:<10} {', '.join(sorted(sources))}")
    marks = findings(sutra.notes)
    if marks:
        lines.append("")
        lines.append("  findings")
        for marker, body in marks:
            lines.append(f"    [{marker}]")
            for chunk in _wrap(body, 62):
                lines.append(f"      {chunk}")
    lines.append("")
    return "\n".join(lines)


def full() -> str:
    return "".join(detail(str(s.id)) for s in REGISTRY.all())


def main(argv: List[str]) -> int:
    args = argv[1:]
    if not args:
        print(summary())
    elif args[0] == "--open":
        print(open_questions())
    elif args[0] == "--full":
        print(full())
    else:
        for sutra_id in args:
            print(detail(sutra_id))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
