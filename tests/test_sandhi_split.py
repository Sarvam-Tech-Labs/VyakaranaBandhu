# -*- coding: utf-8 -*-
"""
Splitting by synthesis: from the joined form back to the words, every answer
proved by re-deriving the joined form with the forward engine.

The property that matters is the round trip: join two words, split the result
with a lexicon that knows them, and the original pair must come back — and
every split returned, whoever proposed it, must actually derive the text. The
second guards soundness (a split is never merely plausible), the first
completeness (the index that proposes splits was built by running the grammar,
so it should miss nothing the grammar can make).
"""

from __future__ import annotations

import unittest

from src.astadhyayi.sandhi import sandhi
from src.astadhyayi.sandhi.harness import joined
from src.astadhyayi.sandhi.split import (
    Index, Lexicon, pausal_forms, split)

FINALS = ["a", "ā", "i", "ī", "u", "e", "o", "ai", "au", "ṛ", "d", "t", "c",
          "k", "g", "r", "s", "m", "n", "ṃ", "h", "ś"]
INITIALS = ["a", "ā", "i", "u", "e", "ai", "o", "au", "ṛ", "c", "ś", "t", "k",
            "g", "p", "r", "d", "n", "m", "y", "v", "h", "s", "j", "b"]

PAIRS = [
    ("iti", "ādi"), ("dadhi", "atra"), ("madhu", "atra"), ("deva", "indra"),
    ("agni", "indra"), ("hare", "ava"), ("rāmas", "atra"), ("manas", "ratha"),
    ("punar", "ramate"), ("vāc", "pati"), ("kṛṣṇa", "aikya"), ("mahā", "ṛṣi"),
    ("haras", "iha"), ("rāmas", "ca"), ("gaṅgā", "udakam"), ("tad", "ca"),
]


class SplitBySynthesis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.index = Index.build(finals=FINALS, initials=INITIALS,
                                contexts=("a", "ā", "i", "u"))

    def test_the_index_is_the_grammars_own_output(self):
        """No entry was typed: every region came out of a derivation."""
        self.assertGreater(self.index.size, 500)
        self.assertIn("ā", self.index.regions)          # a+a, a+ā, ā+a ...
        finals = {e.final for e in self.index.regions["ā"]}
        self.assertIn("a", finals)

    def test_the_round_trip_recovers_the_pair(self):
        for first, second in PAIRS:
            for surface in sandhi([first, second]).surfaces:
                lexicon = Lexicon(list(pausal_forms(first))
                                  + list(pausal_forms(second)))
                found = split(surface, lexicon=lexicon, index=self.index)
                words = [s.words for s in found]
                expected = {(a, b) for a in pausal_forms(first)
                            for b in pausal_forms(second)}
                self.assertTrue(
                    expected & set(words),
                    f"{first} + {second} = {surface}: split gave {words}, "
                    f"wanted one of {sorted(expected)}")

    def test_every_split_returned_really_derives_the_text(self):
        for first, second in PAIRS:
            surface = sandhi([first, second]).surfaces[0]
            for found in split(surface, index=self.index, limit=60):
                self.assertEqual(joined(found.outcome.surface),
                                 joined(surface), found.words)
                for _, outcome in found.alternatives:
                    self.assertEqual(joined(outcome.surface), joined(surface))

    def test_the_derivation_comes_with_the_split(self):
        found = split("ityādi", lexicon=Lexicon(["iti", "ādi"]),
                      index=self.index)
        self.assertEqual(found[0].words, ("iti", "ādi"))
        steps = [s.sutra for s in found[0].outcome.steps]
        self.assertEqual(steps[0], "6.1.77")
        # the first derivation is the one in which nothing was doubled
        self.assertEqual(found[0].outcome.surface, "ityādi")
        self.assertIn("6.1.77 इको यणचि (iko yaṇaci)", found[0].trace())

    def test_a_visarga_is_restored_from_its_sutras(self):
        found = split("rāmo'tra", lexicon=Lexicon(["rāmaḥ", "atra"]),
                      index=self.index)
        self.assertEqual(found[0].words, ("rāmaḥ", "atra"))
        self.assertEqual(found[0].underlying, ("rāmas", "atra"))

    def test_one_split_with_several_underlying_finals_is_one_split(self):
        found = split("vākpati",
                      lexicon=Lexicon(list(pausal_forms("vāc")) + ["pati"]),
                      index=self.index)
        self.assertEqual(len(found), 1)
        finals = {found[0].underlying[0]} | {u[0] for u, _ in
                                             found[0].alternatives}
        self.assertTrue({"vāc", "vāk"} <= finals, finals)

    def test_without_a_lexicon_nothing_is_claimed_to_be_validated(self):
        found = split("ityādi", index=self.index)
        self.assertTrue(found)
        self.assertFalse(any(s.validated for s in found))
        self.assertTrue(any(s.words == ("iti", "ādi") for s in found))

    def test_a_split_where_nothing_changed_is_marked_as_such(self):
        found = split("rāmakṛṣṇa", index=self.index)
        plain = [s for s in found if s.words == ("rāma", "kṛṣṇa")]
        self.assertTrue(plain)
        self.assertFalse(plain[0].changed)

    def test_require_change_drops_them(self):
        found = split("rāmakṛṣṇa", index=self.index, require_change=True)
        self.assertFalse(any(s.words == ("rāma", "kṛṣṇa") for s in found))

    def test_a_lexicon_that_does_not_know_the_words_returns_nothing(self):
        self.assertEqual(
            split("ityādi", lexicon=Lexicon(["aśva", "gaja"]),
                  index=self.index), [])

    def test_devanagari_input_is_accepted(self):
        found = split("इत्यादि", lexicon=Lexicon(["iti", "ādi"]),
                      index=self.index)
        self.assertEqual(found[0].words, ("iti", "ādi"))

    def test_the_result_serialises(self):
        import json
        found = split("vākpati", lexicon=Lexicon(["vāg", "pati"]),
                      index=self.index)
        json.dumps(found[0].to_dict(), ensure_ascii=False)


if __name__ == "__main__":
    unittest.main()
