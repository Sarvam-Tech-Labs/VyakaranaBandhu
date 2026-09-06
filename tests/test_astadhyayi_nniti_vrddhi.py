# -*- coding: utf-8 -*-
"""
७.२.११५–११८ — vṛddhi before a ञित् or णित्, closing the pāda.

Four sūtras and one operation: the tests ask WHICH vowel each
of them strengthens, and then which of the three wins on a stem
all three reach.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.nniti_vrddhi import (
    CODIFIED_APART,
    KIT_TADDHITAS,
    NNIT_RUN,
    NNIT_TABLE,
    TADDHITA_FROM,
    provisions_for,
    vrddhi_before,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class WhichVowelIsStrengthened(unittest.TestCase):
    """The four rules differ in WHERE, not in what."""

    def test_a_vowel_final_stem_strengthens_its_last(self):
        # कारः, हारः, गौः, सखायौ, जैत्रम्.
        got = vrddhi_before("ñit", gana="ac-anta")
        self.assertEqual(got.sutra, "7.2.115")
        self.assertEqual(got.where, "antya-ac")

    def test_and_an_a_in_the_penult_is_strengthened_too(self):
        # पाकः, त्यागः, पाचयति, पाठकः.
        got = vrddhi_before("ñit", part="upadhā-a")
        self.assertEqual(got.sutra, "7.2.116")
        self.assertEqual(got.where, "upadhā-a")

    def test_but_a_taddhita_strengthens_the_first(self):
        # गार्ग्यः, दाक्षिः, औपगवः.
        got = vrddhi_before("ñit", taddhita=True)
        self.assertEqual(got.sutra, "7.2.117")
        self.assertEqual(got.where, "acām-ādi")

    def test_every_rule_of_the_run_does_the_same_thing(self):
        for row in NNIT_TABLE:
            self.assertEqual(row.does, "vṛddhi", row.sutra)

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(TADDHITA_FROM, "7.2.117")


class TheTaddhitaRuleDisplacesTheOthers(unittest.TestCase):
    """त्वाष्ट्रः and जागतः are why the sūtra is needed."""

    def test_it_names_both_the_rules_it_beats(self):
        # अचामादेर्वृद्धिरन्त्योपधालक्षणां वृद्धिं बाधते — त्वष्टृ
        # would have strengthened its ऋ and जगत् its penult.
        blocks = provisions_for("7.2.117")[0].blocks
        self.assertEqual(set(blocks), {"7.2.115", "7.2.116"})

    def test_and_it_wins_on_a_stem_all_three_reach(self):
        # A vowel-final stem before a ñit taddhita: 7.2.115 and
        # 7.2.117 both apply, and the language has गार्ग्यः.
        got = vrddhi_before("ñit", gana="ac-anta", taddhita=True)
        self.assertEqual(got.sutra, "7.2.117")
        self.assertIn("7.2.115", got.blocked_by)

    def test_outside_a_taddhita_the_general_rules_stand(self):
        self.assertEqual(
            vrddhi_before("ñit", gana="ac-anta").sutra, "7.2.115")


class TheKitTaddhita(unittest.TestCase):
    """7.2.118, and why a कित् affix needs saying at all."""

    def test_the_first_vowel_is_strengthened_before_a_kit(self):
        # नाडायनः, चारायणः, आक्षिकः, शालाकिकः.
        got = vrddhi_before("kit", taddhita=True)
        self.assertEqual(got.sutra, "7.2.118")
        self.assertEqual(got.where, "acām-ādi")

    def test_the_two_affixes_it_is_worked_on_are_codified(self):
        # फक् 4.1.99 and ठक् 4.4.1 — the rule is stated about
        # affixes another adhyāya supplies.
        self.assertEqual(len(KIT_TADDHITAS), 2)
        for named, code in KIT_TADDHITAS:
            self.assertTrue(REGISTRY.has(code), (named, code))

    def test_the_kit_marking_is_what_makes_the_sutra_necessary(self):
        # 1.1.5's क्ङिति refuses an इक्-conditioned strengthening,
        # and both affixes are कित् for other reasons. Stating
        # the vṛddhi on the FIRST vowel puts it out of reach.
        self.assertIn("1.1.5", provisions_for("7.2.118")[0].why)
        self.assertTrue(REGISTRY.has("1.1.5"))

    def test_a_kit_affix_that_is_no_taddhita_reaches_nothing(self):
        self.assertEqual(vrddhi_before("kit").sutra, "")


class NothingHappensByDefault(unittest.TestCase):
    """An affix that is none of the three strengthens nothing."""

    def test_an_unmarked_affix_reaches_nothing(self):
        got = vrddhi_before("śap", gana="ac-anta")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")
        self.assertEqual(got.where, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry, and the pāda is closed."""

    def test_the_run_closes_the_pada(self):
        self.assertEqual(NNIT_RUN, ("7.2.115", "7.2.118"))
        codes = [row.sutra for row in NNIT_TABLE]
        self.assertEqual(
            codes, ["7.2.%d" % n for n in range(115, 119)])
        self.assertFalse(REGISTRY.has("7.2.119"))

    def test_one_sutra_of_the_stretch_is_codified_elsewhere(self):
        # 7.2.114 मृजेर्वृद्धिः lives in anga.mrjer_vrddhi, where
        # it was read long before this pāda, and a patch that
        # appends to the file must not disturb it.
        self.assertEqual(CODIFIED_APART, ("7.2.114",))
        self.assertTrue(REGISTRY.has("7.2.114"))
        self.assertNotIn("7.2.114", [r.sutra for r in NNIT_TABLE])
        self.assertGreater(len(REGISTRY.get("7.2.114").notes), 200)

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in NNIT_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_pada_seven_two_is_complete(self):
        for n in range(1, 119):
            self.assertTrue(REGISTRY.has("7.2.%d" % n), n)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_what_the_vrddhi_actually_is_comes_from_elsewhere(self):
        # 1.1.1 वृद्धिरादैच् says which sounds it is, and for ऋ
        # 1.1.50 and 1.1.51 build the आर् in two steps — which is
        # what 7.2.114 was codified apart to exercise. All live.
        for code in ("1.1.1", "1.1.50", "1.1.51"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_the_pada_after_this_one_is_open_but_not_finished(self):
        # पाद ७.३ opens on देविकादि and runs 120 sūtras. It has
        # been opened since this was written, and 7.3.1's own
        # आ is the first thing that qualifies 7.2.117. What is
        # still ahead is the end of it: 7.3.120 closes the pāda.
        # पाद ७.३ has been read through since — 7.3.1 to
        # 7.3.120 — so the whole of it can be asked of the
        # engine. 7.4.1 opens the pāda that is still ahead.
        self.assertTrue(REGISTRY.has("7.3.1"))
        self.assertTrue(REGISTRY.has("7.3.120"))
        # 7.4.1 has landed too, and with it the last pāda of
        # the adhyāya. Nothing of अध्याय ७ is ahead any more.
        self.assertTrue(REGISTRY.has("7.4.1"))


if __name__ == "__main__":
    unittest.main()
