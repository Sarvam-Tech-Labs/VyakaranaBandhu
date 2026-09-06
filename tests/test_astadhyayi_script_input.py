# -*- coding: utf-8 -*-
"""
Both scripts are accepted wherever the playground takes a word.

There is no reason a reader who thinks in Devanāgarī should have to
transliterate by hand before asking a question. The rules are written in IAST
because the dhātupāṭha and the gaṇapāṭha on disk are, so the conversion happens
at the one boundary where input arrives — and what the rule was actually asked
is echoed back, so the reader can always see what was understood.

The tests that matter here are the two ways this can go wrong quietly:

  * a Devanāgarī input that gives a *different answer* from its IAST twin,
    which would make the feature a trap rather than a convenience;
  * a non-Sanskrit value being transliterated anyway — a sūtra number, a
    sense-name, an asserted condition. Those are not words and must survive
    untouched, or the rule that reads them silently stops matching.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.cases import cases_for
from src.astadhyayi.playground import run, spec_for, to_iast
from src.astadhyayi.sutra import REGISTRY
from src.normalizer import iast_to_devanagari


class TheConversionItself(unittest.TestCase):
    def test_ordinary_words(self):
        for written, expected in [
            ("विश्", "viś"), ("कृ", "kṛ"), ("भू", "bhū"), ("स्था", "sthā"),
            ("डुकृञ्", "ḍukṛñ"), ("गॄ", "gṝ"), ("वृक्ष", "vṛkṣa"),
            ("प्र", "pra"), ("क्त्वा", "ktvā"), ("सन्", "san"),
            ("ब्राह्मणाः", "brāhmaṇāḥ"),
        ]:
            self.assertEqual(to_iast(written), expected, written)

    def test_the_anunasika_vowel_keeps_the_dhatupathas_convention(self):
        """
        आसँ comes out of the general transliterator as āsam̐, and the
        dhātupāṭha writes āsa̐ — the mark on the vowel, because 1.3.2 asks
        whether a *vowel* is anunāsika and m̐ reads as a consonant. Left
        unconverted the root is simply not found.
        """
        self.assertEqual(to_iast("आसँ"), "āsa̐")
        self.assertEqual(to_iast("वसँ"), "vasa̐")

        from src.astadhyayi.corpus import load_dhatupatha

        entries = load_dhatupatha()
        self.assertEqual(entries["02.0011"].upadesa, to_iast("आसँ"))

    def test_what_is_not_devanagari_is_left_exactly_alone(self):
        """
        The values that are *not* Sanskrit words outnumber the ones that are:
        sūtra numbers, sense-names, asserted conditions, tag words. Touching
        any of them would make its rule stop matching, silently.
        """
        for text in ("8.2.31", "gandhana", "akarmaka", "vṛddha",
                     "kartrabhiprāya-kriyāphala", "diksamāsa-bahuvrīhi",
                     "1.4.10", "", "sup"):
            self.assertEqual(to_iast(text), text, text)

    def test_mixed_input_converts_only_the_devanagari(self):
        """
        1.2.65's members are written `stem:tag`, and a reader may well type
        the stem in one script and the tag in the other.
        """
        self.assertEqual(to_iast("गार्ग्य:vṛddha"), "gārgya:vṛddha")
        self.assertEqual(to_iast("गो:strī:herd"), "go:strī:herd")


class TheSameAnswerEitherWay(unittest.TestCase):
    """The property that makes this a convenience rather than a trap."""

    PAIRS = [
        ("1.3.17", {"root": "विश्", "upasargas": ["नि"]},
         {"root": "viś", "upasargas": ["ni"]}),
        ("1.3.12", {"root": "आसँ"}, {"root": "āsa̐"}),
        ("1.2.9", {"root": "चि", "affix": "सन्"},
         {"root": "ci", "affix": "san"}),
        ("1.4.59", {"form": "प्र", "kriya_yoga": True},
         {"form": "pra", "kriya_yoga": True}),
        ("1.1.20", {"root": "डुदाञ्"}, {"root": "ḍudāñ"}),
        ("1.2.64", {"words": ["वृक्ष", "वृक्ष"]},
         {"words": ["vṛkṣa", "vṛkṣa"]}),
        ("1.2.65", {"words": ["गार्ग्य:vṛddha", "गार्ग्य:yuvan"]},
         {"words": ["gārgya:vṛddha", "gārgya:yuvan"]}),
    ]

    def test_each_pair_agrees(self):
        for sutra_id, written, transliterated in self.PAIRS:
            with self.subTest(sutra=sutra_id):
                one = run(sutra_id, dict(written))
                other = run(sutra_id, dict(transliterated))
                self.assertTrue(one["ok"], one.get("error"))
                self.assertEqual(one["result"], other["result"])

    def test_a_pratyahara_resolves_from_either_script(self):
        """
        And here is the one thing Devanāgarī cannot carry. A pratyāhāra is
        written aC, iK, haL — capital for the marker letter — and that casing
        is the only thing saying *which* letter is the marker. अच् is just अ
        followed by च्; the script has no way to mark one of them.

        It resolves anyway, to exactly the same sounds, because the resolver
        finds the marker in the śivasūtras rather than in the spelling. What
        differs is only the term echoed back, and a reader who typed अच् and
        sees `ac` has lost nothing they had.
        """
        written = run("1.1.68", {"term": "अच्"})["result"]
        transliterated = run("1.1.68", {"term": "aC"})["result"]
        self.assertEqual(written["sounds"], transliterated["sounds"])
        self.assertEqual(written["term"], "ac")
        self.assertEqual(transliterated["term"], "aC")

    def test_and_the_devanagari_one_actually_fires_the_rule(self):
        """
        Two wrong answers agreeing is not agreement. Each pair has to reach
        the sūtra it is filed under.
        """
        for sutra_id, written, _ in self.PAIRS:
            result = run(sutra_id, dict(written)).get("result")
            by = result.get("by") if isinstance(result, dict) else None
            if by is None:
                continue
            with self.subTest(sutra=sutra_id):
                self.assertIn(sutra_id, str(by))

    def test_every_curated_input_survives_a_round_trip(self):
        """
        The broadest form of the same check: take each worked input, render
        every text value into Devanāgarī, feed it back, and require the same
        answer. This sweeps the whole codification rather than eight pairs.
        """
        from src.normalizer import is_devanagari

        checked = 0
        for sutra in REGISTRY.all():
            sutra_id = str(sutra.id)
            kinds = {f.name: f.kind for f in spec_for(sutra_id).fields}
            for case in cases_for(sutra_id):
                rewritten, touched = {}, False
                for name, value in case.values.items():
                    # Only a plain word can be rendered back — a sūtra number
                    # or a sense-name is not Sanskrit and would come out as
                    # nonsense in either direction.
                    if kinds.get(name) == "text" and isinstance(value, str) \
                            and value and value.isascii() is False \
                            and not any(ch.isdigit() for ch in value) \
                            and "-" not in value and ":" not in value:
                        candidate = iast_to_devanagari(value)
                        if is_devanagari(candidate) and \
                                to_iast(candidate) == value:
                            rewritten[name] = candidate
                            touched = True
                            continue
                    rewritten[name] = value
                if not touched:
                    continue
                checked += 1
                with self.subTest(sutra=sutra_id, case=case.label):
                    self.assertEqual(
                        run(sutra_id, rewritten).get("result"),
                        run(sutra_id, dict(case.values)).get("result"),
                    )
        self.assertGreater(checked, 40)


class TheReaderCanSeeWhatWasUnderstood(unittest.TestCase):
    def test_the_call_is_echoed_in_iast(self):
        """
        A silent conversion is worse than none — if the transliteration is
        wrong the reader needs to be able to see that, not guess it from a
        surprising answer.
        """
        called = run("1.3.17", {"root": "विश्", "upasargas": ["नि"]})["called"]
        self.assertIn("viś", called)
        self.assertIn("ni", called)
        self.assertNotIn("विश्", called)


if __name__ == "__main__":
    unittest.main()
