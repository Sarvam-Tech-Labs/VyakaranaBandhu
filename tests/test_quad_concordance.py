"""
Unit & Integration Tests for Quad-Tradition Concordance & Reconciliation Engine
Verifies 4-Pillar harmony across Pāṇini, Mahābhāṣya, Harināmāmṛta, and Bāla-Toṣaṇī.
"""

import unittest
from src.subanta_engine import SubantaEngine
from src.quad_concordance import QuadConcordanceEngine


class TestQuadConcordance(unittest.TestCase):

    def setUp(self):
        self.subanta_engine = SubantaEngine()
        self.quad_engine = QuadConcordanceEngine(self.subanta_engine)

    def test_epistemological_matrix(self):
        """Tests that the foundational 4-way comparative epistemology dictionary is complete."""
        matrix = self.quad_engine.get_epistemological_matrix()
        self.assertGreaterEqual(len(matrix), 6)
        concepts = [row["concept"] for row in matrix]
        self.assertIn("Nominal Base / Stem", concepts)
        self.assertIn("Case Affixes (21 SUP)", concepts)
        self.assertIn("Marker Letter Cleanup", concepts)
        self.assertIn("Rule Conflict Resolution", concepts)
        self.assertIn("Stem Gradation", concepts)
        self.assertIn("Realized Word Form", concepts)

    def test_quad_concordance_rama_instrumental(self):
        """Tests 4-Pillar Concordance for rāmeṇa (Tṛtīyā Ekavacana)."""
        res = self.quad_engine.generate_quad_concordance("rāma", "masculine", vibhakti_idx=2, vacana_idx=0)
        self.assertEqual(res["final_pada_iast"], "rāmeṇa")
        self.assertEqual(res["final_pada_devanagari"], "रामेण")
        self.assertIn("Ekam Sat", res["grand_verdict"])
        
        # Verify 4-pillar fields in steps
        steps = res["concordance_steps"]
        self.assertGreaterEqual(len(steps), 3)
        for st in steps:
            self.assertIn("p1_astadhyayi", st)
            self.assertIn("p2_mahabhashya", st)
            self.assertIn("p3_harinamamrita", st)
            self.assertIn("p4_bala_toshani", st)
            self.assertIn("reconciliation_verdict", st)

    def test_quad_concordance_sakhi_genitive(self):
        """Tests 4-Pillar Concordance for irregular noun sakhi (sakhyuḥ)."""
        res = self.quad_engine.generate_quad_concordance("sakhi", "masculine", vibhakti_idx=5, vacana_idx=0)
        self.assertEqual(res["final_pada_iast"], "sakhyuḥ")
        self.assertEqual(res["final_pada_devanagari"], "सख्युः")
        self.assertIn("Sakhya-Rasa", str(res["concordance_steps"]))

    def test_quad_concordance_reverse_analysis(self):
        """Tests reverse Quad-Tradition brief generation for an inflected pada."""
        res = self.quad_engine.analyze_quad_concordance("rāmeṇa")
        self.assertEqual(res["pada"], "rāmeṇa")
        self.assertGreaterEqual(res["total_readings"], 1)
        reading = res["analyses"][0]
        self.assertEqual(reading["stem_iast"], "rāma")
        self.assertIn("quad_concordance", reading)
        self.assertIn("Ekam Sat", reading["quad_concordance"]["grand_verdict"])


if __name__ == "__main__":
    unittest.main()
