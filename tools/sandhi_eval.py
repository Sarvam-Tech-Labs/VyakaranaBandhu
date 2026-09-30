#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run the sandhi engine over a file of cases and report what did not match.

    python3 tools/sandhi_eval.py data/sandhi/gold/hal_assimilation.gold.json
    python3 tools/sandhi_eval.py some_dataset.jsonl --sample 5000 --show 30
    python3 tools/sandhi_eval.py a.jsonl b.jsonl --json misses.json

Files are the gold schema (a JSON list) or the normalised external-dataset
schema (JSON lines): both are described in `src/astadhyayi/sandhi/harness.py`.
A miss is a lead and not a verdict — the dataset may be wrong, or under-specified
(see the harness on visarga), or the engine may be. The report clusters misses
by junction and by the steps the engine took so they can be read as patterns.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.astadhyayi.sandhi import harness  # noqa: E402


def load(path):
    if path.endswith(".jsonl"):
        return list(harness.load_jsonl(path))
    return harness.load_gold(path)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("files", nargs="+")
    parser.add_argument("--limit", type=int, default=None,
                        help="stop after this many cases per file")
    parser.add_argument("--sample", type=int, default=None,
                        help="evaluate a random sample of this many cases")
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--show", type=int, default=15,
                        help="how many misses to print")
    parser.add_argument("--boundary", default="pada",
                        help="junction kind for rows that do not say: pada "
                             "(separate words), anga (inside a word), samasa, "
                             "upasarga")
    parser.add_argument("--ignore-avagraha", action="store_true",
                        help="compare with the avagraha dropped from both sides, "
                             "for datasets that write it for an elided a "
                             "(off by default)")
    parser.add_argument("--norm-nasal", action="store_true",
                        help="normalize alternative anunāsika spellings (e.g. 'm̐' to '̐')")
    parser.add_argument("--json", metavar="OUT",
                        help="write every kept miss to this file")
    args = parser.parse_args(argv)

    everything = 0
    kept = []
    for path in args.files:
        cases = load(path)
        if args.sample and len(cases) > args.sample:
            cases = random.Random(args.seed).sample(cases, args.sample)
        summary = harness.evaluate(cases, limit=args.limit,
                                   default_boundary=args.boundary,
                                   ignore_avagraha=args.ignore_avagraha,
                                   norm_nasal=args.norm_nasal)
        print(f"== {path}")
        print(summary.report(show=args.show))
        print()
        everything += summary.total - summary.matched
        kept.extend(summary.misses)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump([{"id": r.id, "verdict": r.verdict, "words": r.words,
                        "expected": r.expected, "got": r.got,
                        "steps": r.steps, "detail": r.detail}
                       for r in kept], handle, ensure_ascii=False, indent=1)
    return 1 if everything else 0


if __name__ == "__main__":
    raise SystemExit(main())
