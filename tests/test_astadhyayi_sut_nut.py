# -*- coding: utf-8 -*-
"""
७.१.५१–५७ — असुक्, सुट्, नुट्, and the one stem that is replaced.

सुट् and नुट् divide the genitive plural between them, and the
tests are written to show where the line falls and what falls off
it: राज्ञाम् takes neither, and त्रि escapes both by being
rebuilt as त्रय.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.sut_nut import (
    AGAMA_RUN,
    AGAMA_TABLE,
    ASVADI_FOUR,
    NUT_THREE,
    SAT_AND_CATUR,
    WHAT_THEY_WANT,
    provisions_for,
    takes,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheAsuk(unittest.TestCase):
    """7.1.51, and the two vārttikas that halve its sense."""

    def test_four_stems_take_asuk_before_kyac(self):
        # अश्वस्यति वडवा, क्षीरस्यति माणवकः.
        self.assertEqual(len(ASVADI_FOUR), 4)
        for stem in ASVADI_FOUR:
            got = takes("kyac", stem=stem, sense="ātma-prīti")
            self.assertEqual(got.sutra, "7.1.51", stem)
            self.assertEqual(got.does, "asuk", stem)

    def test_wanting_for_another_reaches_nothing(self):
        # अश्वीयति, क्षीरीयति — no असुक्.
        self.assertEqual(takes("kyac", stem="aśva").sutra, "")

    def test_two_varttikas_split_the_sense_in_half(self):
        # अश्ववृषयोर्मैथुनेच्छायाम् and क्षीरलवणयोर्लालसायाम् —
        # the mare and the cow want mating, the boy and the camel
        # crave. Outside those two senses there is no असुक् even
        # where the wanting is one's own.
        self.assertEqual(len(WHAT_THEY_WANT), 2)
        senses = dict(WHAT_THEY_WANT)
        self.assertEqual(senses["aśva-vṛṣa"], "maithuna-icchā")
        self.assertEqual(senses["kṣīra-lavaṇa"], "lālasā")

    def test_the_chandas_heading_has_stopped_by_here(self):
        # छन्दसीत्यतः प्रभृति निवृत्तम् — this is the vṛtti's own
        # way of closing the heading 7.1.38 opened, and no rule
        # of this run needs the Veda except the two that say so.
        vedic = [row.sutra for row in AGAMA_TABLE if row.chandasi]
        self.assertEqual(vedic, ["7.1.56", "7.1.57"])
        self.assertIn("निवृत्तम्", provisions_for("7.1.51")[0].why)


class TheGenitivePlural(unittest.TestCase):
    """7.1.52 and 7.1.54–57 divide it between सुट् and नुट्."""

    def test_an_a_final_pronoun_takes_sut(self):
        # सर्वेषाम्, येषाम्, तासाम्.
        got = takes("ām", after="a-varṇa-sarvanāma")
        self.assertEqual(got.sutra, "7.1.52")
        self.assertEqual(got.does, "suṭ")

    def test_a_short_vowel_nadi_or_ap_stem_takes_nut(self):
        # वृक्षाणाम्, कुमारीणाम्, खट्वानाम्.
        got = takes("ām", after="hrasva-nadī-āp")
        self.assertEqual(got.sutra, "7.1.54")
        self.assertEqual(got.does, "nuṭ")

    def test_the_rule_names_three_shapes_of_stem(self):
        self.assertEqual(
            NUT_THREE, ("hrasva-anta", "nadī-anta", "āp-anta"))

    def test_a_numeral_takes_it_too(self):
        # षण्णाम्, पञ्चानाम्, चतुर्णाम्.
        self.assertEqual(SAT_AND_CATUR, ("ṣaṭ", "catur"))
        got = takes("ām", after="ṣaṭ-catur")
        self.assertEqual(got.sutra, "7.1.55")

    def test_catur_had_to_be_named_because_it_is_no_sat(self):
        # रेफान्तायाः संख्यायाः षट्संज्ञा न विहिता — a र्-final
        # numeral was kept out of the षट् name on purpose, or
        # 7.1.22 would have dropped its जस्. So it comes back by
        # name here, and 7.1.22 is codified to be escaped from.
        self.assertIn("षट्संज्ञा न विहिता",
                      provisions_for("7.1.55")[0].why)
        self.assertTrue(REGISTRY.has("7.1.22"))

    def test_a_long_vowel_stem_takes_neither(self):
        # राज्ञाम् — no सुट् and no नुट्, which is what the two
        # rules between them leave.
        got = takes("ām", after="an-anta")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class TheOneStemThatIsReplaced(unittest.TestCase):
    """7.1.53 is not an augment rule at all."""

    def test_tri_becomes_traya(self):
        # त्रयाणाम्.
        got = takes("ām", stem="tri")
        self.assertEqual(got.sutra, "7.1.53")
        self.assertEqual(got.does, "traya")
        self.assertFalse(got.augment)

    def test_and_it_beats_the_nut_it_would_have_taken(self):
        # त्रि ends in a short vowel, so 7.1.54 reaches it and
        # would have given *त्रीणाम् in the language.
        got = takes("ām", stem="tri", after="hrasva-nadī-āp")
        self.assertEqual(got.sutra, "7.1.53")
        self.assertIn("7.1.54", got.blocked_by)

    def test_every_other_rule_of_the_run_is_an_augment(self):
        replaced = [row.sutra for row in AGAMA_TABLE
                    if not row.augment]
        self.assertEqual(replaced, ["7.1.53"])


class TheVedicTwo(unittest.TestCase):
    """7.1.56 and 7.1.57, each for its own reason."""

    def test_sri_and_gramani_take_the_nut_in_the_veda(self):
        # श्रीणाम्, सूतग्रामणीनाम्.
        for stem in ("śrī", "grāmaṇī"):
            got = takes("ām", stem=stem, chandasi=True)
            self.assertEqual(got.sutra, "7.1.56", stem)

    def test_sri_needed_the_rule_because_its_nadi_name_is_optional(self):
        # 1.4.5's वामि makes श्री a नदी only half the time, so
        # 7.1.54 would have reached it only half the time —
        # तत्र नित्यार्थं वचनम्. And 1.4.5 is codified.
        self.assertIn("1.4.5", provisions_for("7.1.56")[0].why)
        self.assertTrue(REGISTRY.has("1.4.5"))

    def test_go_takes_it_at_a_verse_quarters_end(self):
        # विद्मा हि त्वा गोपतिं शूर गोनाम्.
        got = takes("ām", stem="go", before="pāda-anta",
                    chandasi=True)
        self.assertEqual(got.sutra, "7.1.57")

    def test_and_the_metrical_condition_actually_bites(self):
        # गवां गोत्रम् उदसृजो यदङ्गिरः — not at a quarter's end.
        self.assertNotEqual(
            takes("ām", stem="go", chandasi=True).sutra, "7.1.57")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(AGAMA_RUN, ("7.1.51", "7.1.57"))
        codes = [row.sutra for row in AGAMA_TABLE]
        self.assertEqual(
            codes, ["7.1.%d" % n for n in range(51, 58)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in AGAMA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_names_these_rules_lean_on_are_live(self):
        # 1.1.27's सर्वनाम् for 7.1.52, 1.4.3's नदी and 1.4.5's
        # वामि for 7.1.54 and 7.1.56, 1.1.24's षट् for 7.1.55.
        for code in ("1.1.27", "1.4.3", "1.4.5", "1.1.24"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_what_the_nut_then_meets_is_not_codified_yet(self):
        # वृक्षाणाम् needs 8.4.2's ण् for the nasal the नुट्
        # supplies, and 6.4.3's lengthening before it. The
        # lengthening is live; the retroflexion is not. When
        # 8.4.2 lands this assertion fails and the note must be
        # rewritten to state the live dependency.
        self.assertTrue(REGISTRY.has("6.4.3"))
        # 8.4.2 अट्कुप्वाङ्नुम्व्यवायेऽपि, which the नुट् then
        # meets, has landed with पाद ८.४.
        self.assertTrue(REGISTRY.has("8.4.2"))


if __name__ == "__main__":
    unittest.main()
