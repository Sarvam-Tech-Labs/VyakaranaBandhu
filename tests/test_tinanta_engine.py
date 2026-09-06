"""
Unit Tests for Pāṇinian & Harināmāmṛta Tiṅanta Engine
======================================================
Tests verbal conjugations across 10 Lakāras, Gaṇas, and Voice paradigms.
"""

import unittest
from src.tinanta_engine import TinantaEngine


class TestTinantaEngine(unittest.TestCase):
    def setUp(self):
        self.engine = TinantaEngine()

    def test_bhu_lat_parasmaipada(self):
        """Tests standard Bhvādi root bhū in Laṭ (Present)."""
        res = self.engine.generate_conjugation("bhū", "lat", "parasmaipada")
        self.assertEqual(res["root_devanagari"], "भू")
        self.assertEqual(res["table"][0]["forms"][0]["devanagari"], "भवति")
        self.assertEqual(res["table"][0]["forms"][2]["devanagari"], "भवन्ति")
        self.assertEqual(res["table"][1]["forms"][0]["devanagari"], "भवसि")
        self.assertEqual(res["table"][2]["forms"][0]["devanagari"], "भवामि")

    def test_gam_lat_parasmaipada(self):
        """Tests root gam with cha-ādeśa (7.3.77)."""
        res = self.engine.generate_conjugation("gam", "lat", "parasmaipada")
        self.assertEqual(res["table"][0]["forms"][0]["devanagari"], "गच्छति")
        self.assertEqual(res["table"][2]["forms"][0]["devanagari"], "गच्छामि")

    def test_kr_lat_parasmaipada_and_atmanepada(self):
        """Tests Tanādi root kṛ in both voices."""
        p_res = self.engine.generate_conjugation("kṛ", "lat", "parasmaipada")
        self.assertEqual(p_res["table"][0]["forms"][0]["devanagari"], "करोति")
        self.assertEqual(p_res["table"][0]["forms"][2]["devanagari"], "कुर्वन्ति")

        a_res = self.engine.generate_conjugation("kṛ", "lat", "atmanepada")
        self.assertEqual(a_res["table"][0]["forms"][0]["devanagari"], "कुरुते")
        self.assertEqual(a_res["table"][1]["forms"][0]["devanagari"], "कुरुषे")

    def test_as_lat_parasmaipada(self):
        """Tests Adādi copula root as (to be/exist)."""
        res = self.engine.generate_conjugation("as", "lat", "parasmaipada")
        self.assertEqual(res["table"][0]["forms"][0]["devanagari"], "अस्ति")
        self.assertEqual(res["table"][0]["forms"][2]["devanagari"], "सन्ति")
        self.assertEqual(res["table"][2]["forms"][0]["devanagari"], "अस्मि")

    def test_bhu_future_lrt(self):
        """Tests Simple Future Lṛṭ (3.3.13)."""
        res = self.engine.generate_conjugation("bhū", "lrt", "parasmaipada")
        self.assertEqual(res["table"][0]["forms"][0]["devanagari"], "भविष्यति")
        self.assertEqual(res["table"][2]["forms"][0]["devanagari"], "भविष्यामि")

    def test_bhu_imperfect_lan(self):
        """Tests Imperfect Past Laṅ (3.2.111)."""
        res = self.engine.generate_conjugation("bhū", "lan", "parasmaipada")
        self.assertEqual(res["table"][0]["forms"][0]["devanagari"], "अभवत्")
        self.assertEqual(res["table"][0]["forms"][2]["devanagari"], "अभवन्")

    def test_tinanta_prakriya_trace(self):
        """Tests step-by-step sūtra derivation for bhavati."""
        res = self.engine.derive_prakriya("bhū", "lat", "parasmaipada", 0, 0)
        self.assertEqual(res["final_form_devanagari"], "भवति")
        self.assertGreaterEqual(len(res["derivation_steps"]), 4)


if __name__ == "__main__":
    unittest.main()
