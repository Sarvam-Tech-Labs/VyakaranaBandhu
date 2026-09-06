"""
Unit & Regression Tests for 'Both' (Compounds with Internal Sandhi Mutations).
Validates dual presence of compounding structure + phonetic transformation.
"""

import unittest
from src.classifier import SanskritClassifier
from tests.test_cases import BOTH_CASES


class TestBoth(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.classifier = SanskritClassifier(load_pretrained_ml=True)

    def test_both_cases(self):
        for case in BOTH_CASES:
            # Test in IAST
            word_iast = case["text"]
            with self.subTest(word=word_iast, script="IAST"):
                res = self.classifier.classify(word_iast)
                self.assertEqual(
                    res["predicted_class"], case["expected_class"],
                    f"[{case.get('notes')}] IAST '{word_iast}' expected '{case['expected_class']}', got '{res['predicted_class']}' (Conf: {res['confidence']})"
                )
                self.assertGreaterEqual(res.get("confidence", 0), 0.80)
                self.assertTrue(res.get("padacheda"), f"Padacheda missing for '{word_iast}'")
                self.assertTrue("+" in res.get("subtype", "") or "Samāsa" in res.get("subtype", ""), f"Subtype invalid for '{word_iast}': {res.get('subtype')}")

            # Test in Devanagari
            word_dev = case["devanagari"]
            with self.subTest(word=word_dev, script="Devanagari"):
                res_dev = self.classifier.classify(word_dev)
                self.assertEqual(
                    res_dev["predicted_class"], case["expected_class"],
                    f"[{case.get('notes')}] Devanagari '{word_dev}' expected '{case['expected_class']}', got '{res_dev['predicted_class']}' (Conf: {res_dev['confidence']})"
                )
                self.assertGreaterEqual(res_dev.get("confidence", 0), 0.80)
                self.assertTrue(res_dev.get("padacheda"), f"Padacheda missing for '{word_dev}'")


if __name__ == "__main__":
    unittest.main()
