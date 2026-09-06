"""
Unit Tests for Verse Dependency Tree & SVG Anvaya Graph Engine
==============================================================
Tests verse parsing, Kāraka relationship deduction, and SVG rendering.
"""

import unittest
from src.verse_dependency import VerseDependencyEngine


class TestVerseDependency(unittest.TestCase):
    def setUp(self):
        self.engine = VerseDependencyEngine()

    def test_gita_1_1_dependency_tree(self):
        """Tests Bhagavad Gītā 1.1 Kāraka syntactic graph."""
        verse = "धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः । मामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय ॥"
        res = self.engine.build_dependency_tree(verse)
        
        self.assertIn("अकुर्वत", res["root_verb"])
        self.assertGreaterEqual(len(res["nodes"]), 5)
        self.assertGreaterEqual(len(res["edges"]), 4)
        self.assertTrue(res["svg_graph"].startswith("<svg"))
        self.assertIn("🌳 PĀṆINIAN KĀRAKA SYNTACTIC DEPENDENCY TREE", res["svg_graph"])

    def test_raghuvamsha_1_1_dependency_tree(self):
        """Tests Raghuvaṃśa 1.1 verse graph."""
        verse = "वागर्थाविव सम्पृक्तौ वागर्थप्रतिपत्तये । जगतः पितरौ वन्दे पार्वतीपरमेश्वरौ ॥"
        res = self.engine.build_dependency_tree(verse)
        
        self.assertEqual(res["root_verb"], "वन्दे")
        self.assertGreaterEqual(len(res["nodes"]), 5)
        self.assertTrue(res["svg_graph"].startswith("<svg"))


if __name__ == "__main__":
    unittest.main()
