"""
Unit & Regression Tests for Complete Multi-word Verses & Shlokas.
Validates verse tokenization, word counts, and individual constituent predictions.
"""

import unittest
from src.classifier import SanskritClassifier
from tests.test_cases import VERSE_CASES


class TestVerses(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.classifier = SanskritClassifier(load_pretrained_ml=True)

    def test_full_verses(self):
        for case in VERSE_CASES:
            verse_name = case["name"]
            verse_text = case["verse"]
            with self.subTest(verse=verse_name):
                res = self.classifier.classify(verse_text)
                
                # 1. Verse Structure & Metadata
                self.assertTrue(res.get("is_verse"), f"'{verse_name}' should be recognized as a complete verse.")
                self.assertEqual(
                    res["token_count"], case["expected_token_count"],
                    f"'{verse_name}' token count mismatch. Expected {case['expected_token_count']}, got {res['token_count']}."
                )

                # 2. Class Summary Distribution
                if "expected_class_summary" in case:
                    self.assertEqual(
                        res.get("class_summary"), case["expected_class_summary"],
                        f"'{verse_name}' class summary mismatch. Expected {case['expected_class_summary']}, got {res.get('class_summary')}."
                    )

                # 3. Syntactic Prose Order (Anvaya)
                if "expected_anvaya" in case:
                    self.assertEqual(
                        res.get("anvaya"), case["expected_anvaya"],
                        f"'{verse_name}' Anvaya mismatch. Expected '{case['expected_anvaya']}', got '{res.get('anvaya')}'."
                    )

                # 4. Full Padacheda Chain
                self.assertTrue(
                    len(res.get("full_padacheda", "")) > 10,
                    f"Full Padacheda pipeline for '{verse_name}' should be non-empty."
                )

                # 5. Exhaustive Per-Token Verification (Class, Padacheda, Prakṛti-Pratyaya)
                if "expected_tokens" in case:
                    tokens_by_word = {tok["input_text"]: tok for tok in res.get("token_results", [])}
                    for tok_word, exp_details in case["expected_tokens"].items():
                        self.assertIn(tok_word, tokens_by_word, f"Token '{tok_word}' missing from results of '{verse_name}'")
                        actual_tok = tokens_by_word[tok_word]

                        # Assert Morphological Category
                        if "class" in exp_details:
                            self.assertEqual(
                                actual_tok["predicted_class"], exp_details["class"],
                                f"In verse '{verse_name}', token '{tok_word}' expected class '{exp_details['class']}', got '{actual_tok['predicted_class']}'"
                            )

                        # Assert Padacheda
                        if "padacheda" in exp_details:
                            self.assertTrue(
                                exp_details["padacheda"] in actual_tok.get("padacheda", ""),
                                f"In verse '{verse_name}', token '{tok_word}' expected Padacheda containing '{exp_details['padacheda']}', got '{actual_tok.get('padacheda')}'"
                            )

                        # Assert Prakṛti-Pratyaya Formula
                        if "prakriti_pratyaya" in exp_details:
                            actual_pp = actual_tok.get("prakriti_pratyaya", {}).get("formula_dev", "")
                            self.assertEqual(
                                actual_pp, exp_details["prakriti_pratyaya"],
                                f"In verse '{verse_name}', token '{tok_word}' expected Prakṛti-Pratyaya '{exp_details['prakriti_pratyaya']}', got '{actual_pp}'"
                            )


if __name__ == "__main__":
    unittest.main()
