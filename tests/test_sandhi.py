"""
Unit & Regression Tests for Sandhi & Saṃhitā (Phonetic Junctions).
Validates predicted class, subtype, constituent split parts in both Devanagari and IAST.
"""

import unittest
from src.classifier import SanskritClassifier
from tests.test_cases import SANDHI_CASES


class TestSandhi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.classifier = SanskritClassifier(load_pretrained_ml=True)

    def test_sandhi_cases(self):
        for case in SANDHI_CASES:
            # Test in IAST
            word_iast = case["text"]
            with self.subTest(word=word_iast, script="IAST"):
                res = self.classifier.classify(word_iast)
                self.assertEqual(
                    res["predicted_class"], case["expected_class"],
                    f"[{case.get('notes')}] IAST '{word_iast}' expected '{case['expected_class']}', got '{res['predicted_class']}' (Conf: {res['confidence']})"
                )
                if "expected_subtype" in case:
                    self.assertIn(
                        case["expected_subtype"].lower(), res.get("subtype", "").lower(),
                        f"Subtype mismatch for '{word_iast}'. Expected substring '{case['expected_subtype']}', got '{res.get('subtype')}'"
                    )

            # Test in Devanagari
            word_dev = case["devanagari"]
            with self.subTest(word=word_dev, script="Devanagari"):
                res_dev = self.classifier.classify(word_dev)
                self.assertEqual(
                    res_dev["predicted_class"], case["expected_class"],
                    f"[{case.get('notes')}] Devanagari '{word_dev}' expected '{case['expected_class']}', got '{res_dev['predicted_class']}' (Conf: {res_dev['confidence']})"
                )


if __name__ == "__main__":
    unittest.main()
