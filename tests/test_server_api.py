"""
Integration Tests for Server Endpoints
======================================
Tests all REST API endpoints served by the classifier and morphological engines.
"""

import unittest
import json
from src.classifier import SanskritClassifier
from src.subanta_engine import SubantaEngine
from src.tinanta_engine import TinantaEngine
from src.krdanta_taddhita import KrdantaTaddhitaEngine
from src.verse_dependency import VerseDependencyEngine
from src.dossier_exporter import DossierExporter


from src.quad_concordance import QuadConcordanceEngine


class TestAllApiEngines(unittest.TestCase):
    def setUp(self):
        self.classifier = SanskritClassifier(load_pretrained_ml=True)
        self.subanta = SubantaEngine()
        self.tinanta = TinantaEngine()
        self.krdanta = KrdantaTaddhitaEngine()
        self.verse_dep = VerseDependencyEngine()
        self.dossier = DossierExporter()
        self.concordance = QuadConcordanceEngine()

    def test_classify_simplex_and_compounds(self):
        res1 = self.classifier.classify("rāmaḥ")
        self.assertEqual(res1["predicted_class"], "None")
        
        res2 = self.classifier.classify("nīlotpalam")
        self.assertEqual(res2["predicted_class"], "Both")

    def test_subanta_generation_and_concordance(self):
        res = self.subanta.generate_shabdarupa("rāma", "masculine")
        self.assertEqual(res["stem_iast"], "rāma")
        self.assertEqual(len(res["table"]), 8)

        conc = self.concordance.generate_quad_concordance("rāma", "masculine", 2, 0)
        self.assertEqual(conc["final_pada_devanagari"], "रामेण")
        self.assertGreaterEqual(len(conc["concordance_steps"]), 1)

    def test_tinanta_conjugation(self):
        res = self.tinanta.generate_conjugation("bhū", "lat", "parasmaipada")
        self.assertEqual(res["table"][0]["forms"][0]["devanagari"], "भवति")

    def test_krdanta_and_taddhita(self):
        k_res = self.krdanta.derive_krdanta("kṛ", "ktva")
        self.assertEqual(k_res["derived_stem_devanagari"], "कृत्वा")

        t_res = self.krdanta.derive_taddhita("dharma", "thak")
        self.assertEqual(t_res["derived_stem_devanagari"], "धार्मिक")

    def test_verse_dependency_and_anvaya(self):
        v = "वागर्थाविव सम्पृक्तौ वागर्थप्रतिपत्तये । जगतः पितरौ वन्दे पार्वतीपरमेश्वरौ ॥"
        tree = self.verse_dep.build_dependency_tree(v)
        self.assertEqual(tree["root_verb"], "वन्दे")
        self.assertTrue(tree["svg_graph"].startswith("<svg"))

    def test_dossier_brief_export(self):
        d = self.dossier.export_subanta_dossier("rāmeṇa", "markdown")
        self.assertEqual(d["format"], "markdown")
        self.assertIn("PĀṆINIAN LEGAL DEFENSE", d["content"])


if __name__ == "__main__":
    unittest.main()
