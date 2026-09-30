# -*- coding: utf-8 -*-
"""
The data under data/sandhi/ stays checkable.

Every gold case carries a quotation from the source it came from, and every
catalogue entry a sūtra text copied from the corpus. This runs the validator
over them all, so a quotation that is not really in its source — or a sūtra
number that is not a sūtra — cannot get into the repository unnoticed.
"""

from __future__ import annotations

import glob
import importlib.util
import os
import unittest

_SPEC = importlib.util.spec_from_file_location(
    "sandhi_data_validate",
    os.path.join(os.path.dirname(__file__), "..", "tools",
                 "sandhi_data_validate.py"))
V = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(V)

GOLD = sorted(glob.glob("data/sandhi/gold/*.json"))
CATALOGUE = sorted(glob.glob("data/sandhi/catalogue/*.json"))


class Validator(unittest.TestCase):
    """The validator itself must be able to reject."""

    def test_it_rejects_a_fabricated_quotation_a_bad_id_and_a_bad_letter(self):
        import json, tempfile
        bad = [{
            "id": "t-1", "family": "ac_yan_ayadi", "input": ["dadhi", "atraX"],
            "boundary": "pada", "outputs": ["dadhyatra"],
            "sutras": ["6.1.999"], "confidence": "certain", "notes": "",
            "source": {"work": "kashika", "sutra": "6.1.77", "locator": "x",
                       "quote": "दध्यत्र। सर्वथा कल्पितम्"}}]
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "t.gold.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(bad, handle, ensure_ascii=False)
            problems = V.validate_paths([path])
        text = "\n".join(problems)
        self.assertIn("NOT a verbatim substring", text)
        self.assertIn("unknown id", text)
        self.assertIn("outside the project IAST alphabet", text)

    def test_it_accepts_a_real_case(self):
        import json, tempfile
        good = [{
            "id": "t-2", "family": "ac_yan_ayadi", "input": ["dadhi", "atra"],
            "boundary": "pada", "outputs": ["dadhyatra"],
            "sutras": ["6.1.77"], "confidence": "certain", "notes": "",
            "source": {"work": "kashika", "sutra": "6.1.77", "locator": "x",
                       "quote": "दध्यत्र। मध्वत्र। कर्त्रर्थम्"}}]
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "t.gold.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(good, handle, ensure_ascii=False)
            self.assertEqual(V.validate_paths([path]), [])


@unittest.skipUnless(GOLD or CATALOGUE, "no data files yet")
class DataFiles(unittest.TestCase):

    def test_every_data_file_validates(self):
        problems = V.validate_paths(GOLD + CATALOGUE)
        self.assertEqual(problems, [], "\n".join(problems[:30]))


if __name__ == "__main__":
    unittest.main()
