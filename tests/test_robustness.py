"""
Unit & Regression Tests for Normalization, Script Parity, and Robustness.
Validates whitespace trimming, daṇḍas, verse numbering, and punctuation resilience.
"""

import unittest
from src.classifier import SanskritClassifier
from src.normalizer import clean_text, is_devanagari, devanagari_to_iast, iast_to_devanagari
from tests.test_cases import ROBUSTNESS_CASES


class TestRobustness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.classifier = SanskritClassifier(load_pretrained_ml=True)

    def test_clean_text_robustness(self):
        for case in ROBUSTNESS_CASES:
            inp = case["input"]
            with self.subTest(input=inp):
                if "expected_clean" in case:
                    cleaned = clean_text(inp)
                    self.assertEqual(cleaned, case["expected_clean"])
                if "expected_class" in case:
                    res = self.classifier.classify(inp)
                    self.assertEqual(res["predicted_class"], case["expected_class"])

    def test_empty_and_whitespace_inputs(self):
        empty_samples = ["", "   ", "\n\t", "।।।", "॥ १ ॥"]
        for s in empty_samples:
            with self.subTest(sample=repr(s)):
                res = self.classifier.classify(s)
                self.assertIn(res.get("predicted_class"), ("None", "Empty Input"))

    def test_devanagari_iast_roundtrip(self):
        sample_words = ["rāmaḥ", "vidyālayaḥ", "dharmakṣetram", "vṛkṣapatitam", "phalamapi"]
        for w in sample_words:
            dev = iast_to_devanagari(w)
            iast_back = devanagari_to_iast(dev)
            self.assertEqual(w, iast_back, f"Roundtrip mismatch: '{w}' -> '{dev}' -> '{iast_back}'")


if __name__ == "__main__":
    unittest.main()
