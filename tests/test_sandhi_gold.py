# -*- coding: utf-8 -*-
"""
The engine against answers somebody else decided.

`data/sandhi/gold/*.gold.json` holds test cases extracted from the classical
sources on disk — the Kāśikā, the Siddhāntakaumudī and Laghusiddhāntakaumudī, the
Bālamanoramā, Tattvabodhinī and Bhāṣya — each with a verbatim quotation of the
passage it came from, checked by a validator and audited by an agent that did not
write it. The engine's own tests were written by the people who wrote the
engine; these were not, which is what makes a pass here mean something.

**A case either matches or is a recorded mismatch, with a reason.**
`data/sandhi/known_mismatches.json` lists the cases the engine does not (yet)
match, each with a kind and a reason, in the project's own spirit: *a limitation
that is recorded is not a failure; a limitation that is hidden is.* Three things
are then tested, and the third is the one that keeps the list honest:

  1. every case not on the list matches;
  2. every entry on the list has a reason of a known kind;
  3. every entry on the list **still mismatches** — so when the work advances
     and a case starts to pass, this fails until the entry is removed. A
     tolerance that could never notice it was no longer needed would be a
     table of excuses.
"""

from __future__ import annotations

import glob
import json
import os
import unittest

from src.astadhyayi.sandhi import harness

GOLD = sorted(glob.glob("data/sandhi/gold/*.gold.json"))
KNOWN_PATH = "data/sandhi/known_mismatches.json"
KINDS = ("engine-gap", "gold-error", "scope", "underspecified")


def known():
    if not os.path.exists(KNOWN_PATH):
        return {}
    with open(KNOWN_PATH, encoding="utf-8") as handle:
        return json.load(handle)


def cases():
    out = []
    for path in GOLD:
        for row in harness.load_gold(path):
            out.append((os.path.basename(path), row))
    return out


@unittest.skipUnless(GOLD, "no gold files in data/sandhi/gold yet")
class GoldCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.known = known()
        cls.results = {row["id"]: (name, row, harness.run_case(row))
                       for name, row in cases()}

    def test_the_gold_has_unique_ids(self):
        ids = [row["id"] for _, row in cases()]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_case_matches_or_is_a_recorded_mismatch(self):
        failures = []
        for cid, (name, row, result) in self.results.items():
            if not result.ok and cid not in self.known \
                    and row.get("confidence") != "uncertain":
                failures.append(
                    f"{cid} [{result.verdict}] {' + '.join(result.words)}: "
                    f"expected {list(result.expected)}, engine "
                    f"{list(result.got)}"
                    + (f" ({result.detail})" if result.detail else "")
                    + f" steps {'→'.join(result.steps)}")
        self.assertEqual(
            failures, [],
            f"{len(failures)} of {len(self.results)} gold cases neither "
            f"match nor are recorded in {KNOWN_PATH}:\n  "
            + "\n  ".join(failures[:40]))

    def test_every_recorded_mismatch_has_a_reason_of_a_known_kind(self):
        for cid, entry in self.known.items():
            self.assertIn(cid, self.results, f"{cid} is not a gold case")
            self.assertIn(entry.get("kind"), KINDS, cid)
            self.assertGreater(len(entry.get("reason", "").strip()), 15, cid)

    def test_every_recorded_mismatch_still_mismatches(self):
        now_passing = [cid for cid in self.known
                       if cid in self.results and self.results[cid][2].ok]
        self.assertEqual(
            now_passing, [],
            "these cases now match — remove them from "
            f"{KNOWN_PATH}: {now_passing}")


if __name__ == "__main__":
    unittest.main()
