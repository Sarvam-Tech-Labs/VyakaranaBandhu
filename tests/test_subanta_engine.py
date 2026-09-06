"""
Unit and Regression Tests for the Pāṇinian Subanta (Śabdarūpa) Engine
Verifies forward Śabdarūpa matrix generation, Sūtra annotations, and reverse Subanta analysis.
"""

import unittest
from src.subanta_engine import SubantaEngine


class TestSubantaEngine(unittest.TestCase):

    def setUp(self):
        self.engine = SubantaEngine()

    def test_ajanta_a_masculine_rama(self):
        """Tests Akārānta Puṃliṅga (rāma) generation across 8 cases."""
        res = self.engine.generate_shabdarupa("rāma", "masculine")
        self.assertEqual(res["stem_iast"], "rāma")
        self.assertEqual(res["stem_devanagari"], "राम")
        self.assertEqual(res["gender"], "masculine")

        table = res["table"]
        # Prathamā: rāmaḥ, rāmau, rāmāḥ
        self.assertEqual(table[0]["forms"][0]["iast"], "rāmaḥ")
        self.assertEqual(table[0]["forms"][0]["devanagari"], "रामः")
        self.assertEqual(table[0]["forms"][1]["iast"], "rāmau")
        self.assertEqual(table[0]["forms"][2]["iast"], "rāmāḥ")

        # Tṛtīyā: rāmeṇa (Ṇatva 8.4.1), rāmābhyām, rāmaiḥ
        self.assertEqual(table[2]["forms"][0]["iast"], "rāmeṇa")
        self.assertEqual(table[2]["forms"][0]["devanagari"], "रामेण")
        self.assertEqual(table[2]["forms"][2]["iast"], "rāmaiḥ")

        # Ṣaṣṭhī: rāmasya, rāmayoḥ, rāmāṇām (Ṇatva 8.4.1)
        self.assertEqual(table[5]["forms"][0]["iast"], "rāmasya")
        self.assertEqual(table[5]["forms"][2]["iast"], "rāmāṇām")
        self.assertEqual(table[5]["forms"][2]["devanagari"], "रामाणाम्")

        # Saptamī: rāme, rāmayoḥ, rāmeṣu
        self.assertEqual(table[6]["forms"][0]["iast"], "rāme")
        self.assertEqual(table[6]["forms"][2]["iast"], "rāmeṣu")

    def test_ajanta_a_neuter_phala(self):
        """Tests Akārānta Napuṃsakaliṅga (phala) generation."""
        res = self.engine.generate_shabdarupa("phala", "neuter")
        table = res["table"]
        # Prathamā: phalam, phale, phalāni
        self.assertEqual(table[0]["forms"][0]["iast"], "phalam")
        self.assertEqual(table[0]["forms"][1]["iast"], "phale")
        self.assertEqual(table[0]["forms"][2]["iast"], "phalāni")
        self.assertEqual(table[0]["forms"][2]["devanagari"], "फलानि")

        # Dvitīyā: phalam, phale, phalāni
        self.assertEqual(table[1]["forms"][0]["iast"], "phalam")
        self.assertEqual(table[1]["forms"][2]["iast"], "phalāni")

        # Tṛtīyā: phalena, phalābhyām, phalaiḥ
        self.assertEqual(table[2]["forms"][0]["iast"], "phalena")
        self.assertEqual(table[2]["forms"][2]["iast"], "phalaiḥ")

    def test_ajanta_aa_feminine_lata(self):
        """Tests Ākārānta Strīliṅga (latā) generation."""
        res = self.engine.generate_shabdarupa("latā", "feminine")
        table = res["table"]
        # Prathamā: latā, late, latāḥ
        self.assertEqual(table[0]["forms"][0]["iast"], "latā")
        self.assertEqual(table[0]["forms"][1]["iast"], "late")
        self.assertEqual(table[0]["forms"][2]["iast"], "latāḥ")

        # Dvitīyā: latām, late, latāḥ
        self.assertEqual(table[1]["forms"][0]["iast"], "latām")

        # Tṛtīyā: latayā, latābhyām, latābhiḥ
        self.assertEqual(table[2]["forms"][0]["iast"], "latayā")
        self.assertEqual(table[2]["forms"][2]["iast"], "latābhiḥ")

        # Caturthī: latāyai
        self.assertEqual(table[3]["forms"][0]["iast"], "latāyai")

        # Ṣaṣṭhī: latāyāḥ, latayoḥ, latānām
        self.assertEqual(table[5]["forms"][0]["iast"], "latāyāḥ")
        self.assertEqual(table[5]["forms"][2]["iast"], "latānām")

    def test_ajanta_i_masculine_hari(self):
        """Tests Ikārānta Puṃliṅga (hari) generation."""
        res = self.engine.generate_shabdarupa("hari", "masculine")
        table = res["table"]
        # Prathamā: hariḥ, harī, harayaḥ
        self.assertEqual(table[0]["forms"][0]["iast"], "hariḥ")
        self.assertEqual(table[0]["forms"][1]["iast"], "harī")
        self.assertEqual(table[0]["forms"][2]["iast"], "harayaḥ")

        # Tṛtīyā: hariṇā (Ṇatva)
        self.assertEqual(table[2]["forms"][0]["iast"], "hariṇā")
        self.assertEqual(table[2]["forms"][0]["devanagari"], "हरिणा")

        # Caturthī: haraye
        self.assertEqual(table[3]["forms"][0]["iast"], "haraye")

        # Ṣaṣṭhī: hareḥ, haryoḥ, harīṇām
        self.assertEqual(table[5]["forms"][0]["iast"], "hareḥ")
        self.assertEqual(table[5]["forms"][2]["iast"], "harīṇām")

    def test_ajanta_ii_feminine_nadi(self):
        """Tests Īkārānta Strīliṅga (nadī) generation."""
        res = self.engine.generate_shabdarupa("nadī", "feminine")
        table = res["table"]
        # Prathamā: nadī, nadyau, nadyaḥ
        self.assertEqual(table[0]["forms"][0]["iast"], "nadī")
        self.assertEqual(table[0]["forms"][1]["iast"], "nadyau")
        self.assertEqual(table[0]["forms"][2]["iast"], "nadyaḥ")

        # Dvitīyā: nadīm, nadyau, nadīḥ
        self.assertEqual(table[1]["forms"][0]["iast"], "nadīm")
        self.assertEqual(table[1]["forms"][2]["iast"], "nadīḥ")

        # Saptamī: nadyām, nadyoḥ, nadīṣu
        self.assertEqual(table[6]["forms"][0]["iast"], "nadyām")
        self.assertEqual(table[6]["forms"][2]["iast"], "nadīṣu")

    def test_ajanta_u_masculine_guru(self):
        """Tests Ukārānta Puṃliṅga (guru) generation."""
        res = self.engine.generate_shabdarupa("guru", "masculine")
        table = res["table"]
        # Prathamā: guruḥ, gurū, guravaḥ
        self.assertEqual(table[0]["forms"][0]["iast"], "guruḥ")
        self.assertEqual(table[0]["forms"][1]["iast"], "gurū")
        self.assertEqual(table[0]["forms"][2]["iast"], "guravaḥ")

        # Tṛtīyā: guruṇā
        self.assertEqual(table[2]["forms"][0]["iast"], "guruṇā")

        # Caturthī: gurave
        self.assertEqual(table[3]["forms"][0]["iast"], "gurave")

    def test_ajanta_ri_masculine_pitr(self):
        """Tests Ṛkārānta Puṃliṅga (pitṛ) generation."""
        res = self.engine.generate_shabdarupa("pitṛ", "masculine")
        table = res["table"]
        # Prathamā: pitā, pitarau, pitaraḥ
        self.assertEqual(table[0]["forms"][0]["iast"], "pitā")
        self.assertEqual(table[0]["forms"][1]["iast"], "pitarau")
        self.assertEqual(table[0]["forms"][2]["iast"], "pitaraḥ")

        # Dvitīyā: pitaram, pitarau, pitṝn
        self.assertEqual(table[1]["forms"][0]["iast"], "pitaram")
        self.assertEqual(table[1]["forms"][2]["iast"], "pitṝn")

        # Tṛtīyā: pitrā
        self.assertEqual(table[2]["forms"][0]["iast"], "pitrā")

    def test_sarvanama_tad(self):
        """Tests Pronoun (tad) generation across genders."""
        res_m = self.engine.generate_shabdarupa("tad", "masculine")
        tab_m = res_m["table"]
        # Masculine: saḥ, tau, te
        self.assertEqual(tab_m[0]["forms"][0]["iast"], "saḥ")
        self.assertEqual(tab_m[0]["forms"][1]["iast"], "tau")
        self.assertEqual(tab_m[0]["forms"][2]["iast"], "te")
        # Caturthī: tasmai
        self.assertEqual(tab_m[3]["forms"][0]["iast"], "tasmai")

        res_f = self.engine.generate_shabdarupa("tad", "feminine")
        tab_f = res_f["table"]
        # Feminine: sā, te, tāḥ
        self.assertEqual(tab_f[0]["forms"][0]["iast"], "sā")
        self.assertEqual(tab_f[0]["forms"][1]["iast"], "te")
        self.assertEqual(tab_f[0]["forms"][2]["iast"], "tāḥ")

    def test_reverse_subanta_analysis(self):
        """Tests reverse morphological parsing of inflected padas."""
        # Test 1: rāmāya -> rāma, masculine, Caturthī Ekavacana
        res1 = self.engine.analyze_subanta("rāmāya")
        self.assertTrue(any(r["stem_iast"] == "rāma" and "Caturthī" in r["vibhakti"] for r in res1))

        # Test 2: rāmeṣu -> rāma, masculine, Saptamī Bahuvacana
        res2 = self.engine.analyze_subanta("rāmeṣu")
        self.assertTrue(any(r["stem_iast"] == "rāma" and "Saptamī" in r["vibhakti"] for r in res2))

        # Test 3: phalāni -> phala, neuter, Prathamā / Dvitīyā Bahuvacana
        res3 = self.engine.analyze_subanta("phalāni")
        self.assertTrue(any(r["stem_iast"] == "phala" and "Bahuvacana" in r["vacana"] for r in res3))

        # Test 4: tava -> yuṣmad, common, Ṣaṣṭhī Ekavacana
        res4 = self.engine.analyze_subanta("tava")
        self.assertTrue(any(r["stem_iast"] == "yuṣmad" and "Ṣaṣṭhī" in r["vibhakti"] for r in res4))

    def test_irregular_sakhi_mahabhashya(self):
        """Tests irregular noun sakhi (M. Friend) analyzed in Mahābhāṣya."""
        res = self.engine.generate_shabdarupa("sakhi", "masculine")
        tab = res["table"]
        # Prathamā: sakhā, sakhāyau, sakhāyaḥ
        self.assertEqual(tab[0]["forms"][0]["iast"], "sakhā")
        self.assertEqual(tab[0]["forms"][1]["iast"], "sakhāyau")
        self.assertEqual(tab[0]["forms"][2]["iast"], "sakhāyaḥ")
        # Dvitīyā: sakhāyam, sakhāyau, sakhīn
        self.assertEqual(tab[1]["forms"][0]["iast"], "sakhāyam")
        self.assertEqual(tab[1]["forms"][2]["iast"], "sakhīn")
        # Ṣaṣṭhī: sakhyuḥ, sakhyoḥ, sakhīnām
        self.assertEqual(tab[5]["forms"][0]["iast"], "sakhyuḥ")
        self.assertEqual(tab[5]["forms"][2]["iast"], "sakhīnām")
        # Saptamī: sakhyau
        self.assertEqual(tab[6]["forms"][0]["iast"], "sakhyau")

    def test_diphthong_go_mahabhashya(self):
        """Tests diphthong noun go (M. Cow/Bull) analyzed in Mahābhāṣya."""
        res = self.engine.generate_shabdarupa("go", "masculine")
        tab = res["table"]
        # Prathamā: gauḥ, gāvau, gāvaḥ
        self.assertEqual(tab[0]["forms"][0]["iast"], "gauḥ")
        self.assertEqual(tab[0]["forms"][1]["iast"], "gāvau")
        self.assertEqual(tab[0]["forms"][2]["iast"], "gāvaḥ")
        # Dvitīyā: gām, gāvau, gāḥ
        self.assertEqual(tab[1]["forms"][0]["iast"], "gām")
        self.assertEqual(tab[1]["forms"][2]["iast"], "gāḥ")

    def test_prakriya_derivation_and_stem_grade(self):
        """Tests step-by-step derivation tracer and tri-grade stem assessment."""
        # Test Strong Grade (Sarvanāmasthāna): rāma + jas -> rāmāḥ
        prak1 = self.engine.derive_prakriya("rāma", "masculine", vibhakti_idx=0, vacana_idx=2)
        self.assertEqual(prak1["final_pada_iast"], "rāmāḥ")
        self.assertIn("Sarvanāmasthāna", prak1["stem_grade"]["grade"])
        self.assertIn("Sapādasaptādhyāyī", prak1["derivation_steps"][0]["regime"])

        # Test Retroflexion Tripādī: rāma + ṭā -> rāmeṇa
        prak2 = self.engine.derive_prakriya("rāma", "masculine", vibhakti_idx=2, vacana_idx=0)
        self.assertEqual(prak2["final_pada_iast"], "rāmeṇa")
        # Verify Ṇatva step in Tripādī
        natva_step = [s for s in prak2["derivation_steps"] if "Ṇatva" in s["stage"]]
        self.assertTrue(len(natva_step) > 0)
        self.assertIn("Tripādī", natva_step[0]["regime"])

    def test_legal_defense_mahabhashya_dialectic(self):
        """Tests legal brief generation and Mahābhāṣya dialectical resolution."""
        defense = self.engine.generate_legal_defense("rāma", "neuter", "Tṛtīyā (3rd)", "Ekavacana (Singular)", "rāmeṇa")
        self.assertIn("Puṃvad-bhāva", defense["mahabhashya_dialectic"]["siddhanta"])
        self.assertIn("SIDDHA", defense["verdict"])

    def test_harinamamrita_vyakarana_lens(self):
        """Tests Bṛhat-Harināmāmṛta-Vyākaraṇa (HNV) and Bāla-Toṣaṇī Ṭīkā mappings."""
        prak = self.engine.derive_prakriya("rāma", "masculine", vibhakti_idx=2, vacana_idx=0)
        hnv = prak["hnv_prakriya"]
        self.assertIn("rāma", hnv["narayana_base"])
        self.assertIn("Sarveśvarānta", hnv["stem_nature"])
        self.assertIn("Viṣṇubhakti", hnv["visnubhakti_category"])
        self.assertIn("Trivikrama", hnv["sanketa_operation"])
        self.assertIn("rāmeṇa", hnv["completed_visnupada"])
        self.assertIn("Bāla-Toṣaṇī", hnv["bala_toshani_exegesis"])

        # Test Visarga Yugala-Svarūpa exegesis
        prak_nom = self.engine.derive_prakriya("rāma", "masculine", vibhakti_idx=0, vacana_idx=0)
        self.assertIn("Yugala-Svarūpa", prak_nom["hnv_prakriya"]["bala_toshani_exegesis"])

        # Test Sakhyuḥ Sakhya-Rasa exegesis
        prak_sakhi = self.engine.derive_prakriya("sakhi", "masculine", vibhakti_idx=5, vacana_idx=0)
        self.assertIn("Sakhya-Rasa", prak_sakhi["hnv_prakriya"]["bala_toshani_exegesis"])

        defense = self.engine.generate_legal_defense("rāma", "masculine", "Tṛtīyā (3rd)", "Ekavacana (Singular)", "rāmeṇa")
        hnv_lens = defense["hnv_lens"]
        self.assertIn("Viṣṇupada", hnv_lens["philosophical_siddhanta"])
        self.assertIn("Bāla-Toṣaṇī", hnv_lens["treatise"])


if __name__ == "__main__":
    unittest.main()

