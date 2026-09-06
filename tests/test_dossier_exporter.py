"""
Unit Tests for Dossier Exporter
===============================
Tests Markdown, HTML, and JSON dossier report export.
"""

import unittest
from src.dossier_exporter import DossierExporter


class TestDossierExporter(unittest.TestCase):
    def setUp(self):
        self.exporter = DossierExporter()

    def test_markdown_export(self):
        """Tests Markdown legal brief export."""
        res = self.exporter.export_subanta_dossier("rāmeṇa", "markdown")
        self.assertEqual(res["format"], "markdown")
        self.assertIn("PĀṆINIAN LEGAL DEFENSE", res["content"])
        self.assertIn("रामेण", res["content"])
        self.assertIn("Mahābhāṣya Dialectic", res["content"])

    def test_html_export(self):
        """Tests printable HTML legal brief export."""
        res = self.exporter.export_subanta_dossier("rāmaḥ", "html")
        self.assertEqual(res["format"], "html")
        self.assertTrue(res["content"].startswith("<!DOCTYPE html>"))
        self.assertIn("PĀṆINIAN SANSKRIT JURISPRUDENCE COURT", res["content"])

    def test_json_export(self):
        """Tests JSON export format."""
        res = self.exporter.export_subanta_dossier("rāmeṇa", "json")
        self.assertEqual(res["format"], "json")
        self.assertIn('"pada": "rāmeṇa"', res["content"])


if __name__ == "__main__":
    unittest.main()
