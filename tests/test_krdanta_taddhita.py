"""
Unit Tests for Kṛdanta & Taddhitānta Derivative Engine
======================================================
Tests primary verbal derivatives (Kṛt) and secondary nominal derivatives (Taddhita).
"""

import unittest
from src.krdanta_taddhita import KrdantaTaddhitaEngine


class TestKrdantaTaddhita(unittest.TestCase):
    def setUp(self):
        self.engine = KrdantaTaddhitaEngine()

    def test_krdanta_ktva_and_lyap(self):
        """Tests Ktvā vs Lyap substitution (3.4.21 vs 7.1.37)."""
        # Bare root takes ktvā -> kṛtvā
        k_res = self.engine.derive_krdanta("kṛ", "ktva")
        self.assertEqual(k_res["derived_stem_devanagari"], "कृत्वा")
        self.assertTrue(k_res["is_avyaya"])

        # Prefixed root automatically converts ktvā to lyap -> samgatya
        l_res = self.engine.derive_krdanta("gam", "ktva", upasarga="sam")
        self.assertIn("gatya", l_res["derived_stem_iast"])

    def test_krdanta_tumun_infinitive(self):
        """Tests Tumun infinitive (3.3.158)."""
        res = self.engine.derive_krdanta("gam", "tumun")
        self.assertEqual(res["derived_stem_devanagari"], "गन्तुम्")
        self.assertTrue(res["is_avyaya"])

    def test_krdanta_participles_kta_ktavatu_satr(self):
        """Tests participial nominal stems."""
        kta = self.engine.derive_krdanta("kṛ", "kta")
        self.assertEqual(kta["derived_stem_devanagari"], "कृत")

        ktavatu = self.engine.derive_krdanta("kṛ", "ktavatu")
        self.assertEqual(ktavatu["derived_stem_devanagari"], "कृतवत्")

        satr = self.engine.derive_krdanta("dṛś", "satr")
        self.assertEqual(satr["derived_stem_devanagari"], "पश्यत्")

    def test_taddhita_thak_adi_vriddhi(self):
        """Tests Ṭhak relational suffix with Ādivṛddhi (4.4.2 & 7.2.118)."""
        res = self.engine.derive_taddhita("dharma", "thak")
        self.assertEqual(res["derived_stem_devanagari"], "धार्मिक")
        self.assertEqual(res["derived_stem_iast"], "dhārmika")

    def test_taddhita_an_patronymic(self):
        """Tests Aṇ patronymic with Ādivṛddhi (4.1.92 & 7.2.117)."""
        res = self.engine.derive_taddhita("vasudeva", "an")
        self.assertEqual(res["derived_stem_devanagari"], "वासुदेव")
        self.assertEqual(res["derived_stem_iast"], "vāsudeva")

    def test_taddhita_matup_possessive(self):
        """Tests Matup / Vatup (5.2.94 & 8.2.9)."""
        res = self.engine.derive_taddhita("dhī", "matup")
        self.assertEqual(res["derived_stem_devanagari"], "धीमत्")

    def test_taddhita_tva_abstract(self):
        """Tests Tva abstract neuter suffix (5.1.119)."""
        res = self.engine.derive_taddhita("kṛṣṇa", "tva")
        self.assertEqual(res["derived_stem_devanagari"], "कृष्णत्व")


if __name__ == "__main__":
    unittest.main()
