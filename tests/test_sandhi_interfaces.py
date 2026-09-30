# -*- coding: utf-8 -*-
"""
The ways a person reaches the sandhi engine: the command line, the module, and
the server's JSON. The derivations themselves are tested elsewhere; what is
tested here is that each door gives the same answer, in both scripts, and that
a bad input is an answer and not a crash.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

import server
from src.astadhyayi.sandhi import sandhi
from src.astadhyayi.sandhi import split as S


def run(*args):
    return subprocess.run(
        [sys.executable, *args], capture_output=True, text=True,
        encoding="utf-8", timeout=180)


class Payload(unittest.TestCase):

    def test_the_server_payload_is_the_engines_own_dict(self):
        payload = server._sandhi_payload("iti ādi")
        self.assertEqual(payload, sandhi("iti ādi").to_dict())
        # 8.4.47 lets the sounds of ity + ā be doubled: four forms, and the
        # one nothing was doubled in comes first.
        self.assertEqual(payload["surfaces"][0], "ityādi")
        self.assertEqual(payload["surfaces_deva"][0], "इत्यादि")
        self.assertIn("ityyādi", payload["surfaces"])

    def test_the_payload_is_json(self):
        json.dumps(server._sandhi_payload("haras iha"), ensure_ascii=False)

    def test_every_step_carries_its_sutra_in_both_scripts(self):
        step = server._sandhi_payload("iti ādi")["outcomes"][0]["steps"][0]
        self.assertEqual(step["sutra"], "6.1.77")
        self.assertEqual(step["sutra_iast"], "iko yaṇaci")
        self.assertEqual(step["sutra_deva"], "इको यणचि")
        self.assertTrue(step["via"])

    def test_options_arrive_as_separate_outcomes(self):
        payload = server._sandhi_payload("haras iha")
        self.assertEqual(len(payload["outcomes"]), 2)

    def test_a_bad_input_is_an_answer(self):
        payload = server._sandhi_payload("kaXa iti")
        self.assertEqual(payload["kind"], "input")
        self.assertIn("'X'", payload["error"])

    def test_the_boundary_and_the_pause_are_passed_through(self):
        self.assertEqual(
            server._sandhi_payload("ne a", boundary="anga")["surfaces"],
            ["naya"])
        loose = server._sandhi_payload("rāmas", pause=False)
        self.assertNotEqual(loose["surfaces"], ["rāmaḥ"])


class SplitInterfaces(unittest.TestCase):
    """The same index, reached from the server and the command line."""

    @classmethod
    def setUpClass(cls):
        cls.index = S.Index.build(finals=["a", "i", "d", "r", "s", "u"],
                                  initials=["a", "ā", "i", "r", "c", "u"],
                                  contexts=("a", "i"))

    def test_the_server_payload_lists_proved_splits(self):
        with mock.patch.object(S, "_DEFAULT_INDEX", self.index), \
                mock.patch.object(S, "default_lexicon",
                                  return_value=S.Lexicon(["iti", "ādi"])):
            payload = server._sandhi_split_payload("ityādi")
        self.assertTrue(payload["validated"])
        self.assertEqual(payload["splits"][0]["words"], ["iti", "ādi"])
        self.assertEqual(payload["splits"][0]["words_deva"], ["इति", "आदि"])
        self.assertEqual(
            payload["splits"][0]["derivation"]["steps"][0]["sutra"], "6.1.77")
        json.dumps(payload, ensure_ascii=False)

    def test_without_a_word_list_the_answer_says_it_is_unvalidated(self):
        with mock.patch.object(S, "_DEFAULT_INDEX", self.index), \
                mock.patch.object(S, "default_lexicon", return_value=None):
            payload = server._sandhi_split_payload("ityādi")
        self.assertFalse(payload["validated"])
        self.assertIn("none is validated", payload["note"])
        self.assertFalse(any(s["validated"] for s in payload["splits"]))

    def test_a_bad_input_is_an_answer(self):
        with mock.patch.object(S, "_DEFAULT_INDEX", self.index):
            payload = server._sandhi_split_payload("kaXa")
        self.assertEqual(payload["kind"], "input")

    def test_the_cli_reads_the_cached_index_and_prints_the_derivation(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = os.path.join(tmp, "index.json")
            lexicon = os.path.join(tmp, "words.txt")
            with open(cache, "w", encoding="utf-8") as handle:
                json.dump(self.index.to_json(S.fingerprint()), handle,
                          ensure_ascii=False)
            with open(lexicon, "w", encoding="utf-8") as handle:
                handle.write("iti\nādi\n")
            done = subprocess.run(
                [sys.executable, "cli.py", "--sandhi-split", "ityādi",
                 "--lexicon", lexicon],
                capture_output=True, text=True, encoding="utf-8",
                timeout=180, env={**os.environ, "SANDHI_INDEX_CACHE": cache})
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertIn("इति (iti) + आदि (ādi)", done.stdout)
        self.assertIn("6.1.77 इको यणचि (iko yaṇaci)", done.stdout)


class CommandLine(unittest.TestCase):

    def test_the_cli_prints_the_trace(self):
        done = run("cli.py", "--sandhi", "iti ādi")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertIn("6.1.77 इको यणचि (iko yaṇaci)", done.stdout)
        self.assertIn("इत्यादि (ityādi)", done.stdout)

    def test_the_cli_can_print_json(self):
        done = run("cli.py", "--sandhi", "iti ādi", "--sandhi-json")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(json.loads(done.stdout)["surfaces"][0], "ityādi")

    def test_a_bad_input_is_refused_with_a_reason_and_a_status(self):
        done = run("cli.py", "--sandhi", "hare 'va")
        self.assertEqual(done.returncode, 1)
        self.assertIn("already joined", done.stderr)

    def test_the_module_entry_point_agrees_with_the_cli(self):
        cli = run("cli.py", "--sandhi", "vāc pati")
        mod = run("-m", "src.astadhyayi.sandhi", "vāc pati")
        self.assertEqual(mod.returncode, 0, mod.stderr)
        self.assertEqual(cli.stdout, mod.stdout)


if __name__ == "__main__":
    unittest.main()
