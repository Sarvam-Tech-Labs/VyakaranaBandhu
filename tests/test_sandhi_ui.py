# -*- coding: utf-8 -*-
"""
The Sandhi page renders what the engine says — every sūtra cited is a link, both
scripts appear, options show as separate derivations, and nothing in the data
can inject markup. There is no browser here, so ui/app.js is loaded into Node
with a stub DOM and `renderSandhi` is called on real engine output.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import unittest

from src.astadhyayi.sandhi import sandhi
from src.astadhyayi.sandhi import split as S

CASES = ("iti ādi", "haras iha", "praś~na", "manas ratha", "rāmaḥ atra")


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class SandhiPage(unittest.TestCase):

    def test_the_page_renders_real_derivations_and_real_splits(self):
        payloads = {text: sandhi(text).to_dict() for text in CASES}
        index = S.Index.build(finals=["a", "i", "d", "r", "s"],
                              initials=["a", "ā", "i", "r", "c"],
                              contexts=("a", "i"))
        splits = []
        for text, words in (("ityādi", ["iti", "ādi"]),
                            ("punāramate", ["punaḥ", "ramate"])):
            found = S.split(text, lexicon=S.Lexicon(words), index=index)
            self.assertTrue(found, text)
            splits.append({"input": text, "validated": True, "total": 1,
                           "splits": [f.to_dict() for f in found], "note": ""})
        unvalidated = S.split("ityādi", index=index, limit=5)
        splits.append({"input": "ityādi", "validated": False, "total": 5,
                       "splits": [f.to_dict() for f in unvalidated],
                       "note": "no word list"})
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "payloads.json")
            split_path = os.path.join(tmp, "splits.json")
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(payloads, handle, ensure_ascii=False)
            with open(split_path, "w", encoding="utf-8") as handle:
                json.dump(splits, handle, ensure_ascii=False)
            done = subprocess.run(
                ["node", "tests/js/sandhi_render_check.js", path, split_path],
                capture_output=True, text=True, encoding="utf-8", timeout=120)
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertNotIn("FAIL", done.stdout)
        self.assertIn("markup in data is escaped", done.stdout)
        self.assertIn("markup in split data is escaped", done.stdout)
        self.assertIn("an empty split result is explained", done.stdout)


class Wiring(unittest.TestCase):

    def test_the_route_the_link_and_the_page_all_exist(self):
        with open("ui/index.html", encoding="utf-8") as handle:
            html = handle.read()
        with open("ui/app.js", encoding="utf-8") as handle:
            js = handle.read()
        self.assertIn('data-route="sandhi"', html)
        self.assertIn('id="page-sandhi"', html)
        self.assertIn('data-page="sandhi"', html)
        self.assertIn('"sandhi"', js.split("const ROUTES")[1].split("\n")[0])
        self.assertIn("initSandhi();", js)

    def test_every_id_the_script_reads_is_in_the_page(self):
        with open("ui/index.html", encoding="utf-8") as handle:
            html = handle.read()
        for element in ("sandhi-form", "sandhi-text", "sandhi-boundary",
                        "sandhi-pause", "sandhi-veda", "sandhi-submit",
                        "sandhi-examples", "sandhi-output",
                        "sandhi-split-form", "sandhi-split-text",
                        "sandhi-split-submit", "sandhi-split-examples",
                        "sandhi-split-changed", "sandhi-split-output"):
            self.assertIn(f'id="{element}"', html, element)


if __name__ == "__main__":
    unittest.main()
