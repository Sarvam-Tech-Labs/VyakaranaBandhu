# -*- coding: utf-8 -*-
"""
७.२.१–७ — vṛddhi in the सिच् aorist, and where it stops.

One rule gives it and four take it back, two of them only in
part. The tests follow that shape, and the class that matters
most is the one about the maxim the vṛtti uses three times to
let a stated vṛddhi beat the guṇa that would come first.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.sici_vrddhi import (
    ANTARANGA,
    EDIT,
    FIVE_ROOTS,
    HMYANTA,
    VADA_VRAJA,
    VRDDHI_RUN,
    VRDDHI_TABLE,
    provisions_for,
    vrddhi,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheRuleThatGivesIt(unittest.TestCase):
    """7.2.1, and what it has to beat."""

    def test_an_ik_final_stem_takes_vrddhi(self):
        # अचैषीत्, अकार्षीत्, अहार्षीत्.
        got = vrddhi(gana="ik-anta", before="sic",
                     pada="parasmaipada")
        self.assertEqual(got.sutra, "7.2.1")
        self.assertEqual(got.does, "vṛddhi")

    def test_the_atmanepada_is_out(self):
        # अच्योष्ट, अप्लोष्ट.
        got = vrddhi(gana="ik-anta", before="sic",
                     pada="ātmanepada")
        self.assertNotEqual(got.sutra, "7.2.1")

    def test_the_maxim_that_lets_it_apply_is_recorded(self):
        # अन्तरङ्गमपि गुणमेषां वृद्धिर्वचनाद् बाधते — guṇa is the
        # inner rule and would leave no इक् to strengthen; the
        # vṛddhi wins by having been stated at all.
        self.assertIn("वचनाद् बाधते", ANTARANGA)
        self.assertIn("वचनाद् बाधते", provisions_for("7.2.1")[0].why)

    def test_and_the_vrtti_uses_it_again_two_sutras_later(self):
        # नैतदेवम्। अन्तरङ्गमपि गुणं वचनारम्भसामर्थ्यात् सिचि
        # वृद्धिर्बाधत इत्युक्तम् — 7.2.4 raises the same
        # objection and answers it by citing 7.2.1.
        self.assertIn("वचनारम्भसामर्थ्यात्",
                      provisions_for("7.2.4")[0].why)


class WhatWidensIt(unittest.TestCase):
    """7.2.2 and 7.2.3 reach past the इक्."""

    def test_an_r_or_l_final_stems_a_takes_it(self):
        # अक्षारीत्, अज्वालीत्.
        got = vrddhi(gana="r-l-anta", part="a", before="sic",
                     pada="parasmaipada")
        self.assertEqual(got.sutra, "7.2.2")

    def test_and_it_beats_the_option_that_would_have_applied(self):
        # अतो हलादेर्लघोः इति विकल्पस्यायमपवादः — so अक्षारीत्
        # has no अक्षरीत् beside it.
        self.assertIn("7.2.7", provisions_for("7.2.2")[0].blocks)
        self.assertFalse(
            vrddhi(gana="r-l-anta", part="a", before="sic",
                   pada="parasmaipada").optional)

    def test_two_roots_and_every_consonant_final_stem_take_it(self):
        # अवादीत्, अव्राजीत्, अपाक्षीत्, अरौत्सीत्.
        self.assertEqual(VADA_VRAJA, ("vad", "vraj"))
        for root in VADA_VRAJA:
            self.assertEqual(
                vrddhi(root, before="sic",
                       pada="parasmaipada").sutra, "7.2.3", root)
        self.assertEqual(
            vrddhi(gana="hal-anta", part="ac", before="sic",
                   pada="parasmaipada").sutra, "7.2.3")

    def test_halanta_is_said_to_catch_a_cluster(self):
        # अराङ्क्षीत्, असाङ्क्षीत् — येन नाव्यवधानं तेन by itself
        # lets only one sound stand between.
        self.assertIn("हल्समुदायपरिग्रहार्थम्",
                      provisions_for("7.2.3")[0].why)


class WhatTakesItBack(unittest.TestCase):
    """7.2.4–7, all four turning on the इट्."""

    def test_an_it_before_the_sic_refuses_it(self):
        # अदेवीत्, असेवीत्.
        got = vrddhi(gana="hal-anta", before="iṭ-sic")
        self.assertEqual(got.sutra, "7.2.4")
        self.assertEqual(got.does, "")
        self.assertIn("7.2.3", got.blocked_by)

    def test_three_stem_shapes_and_five_roots_refuse_it_too(self):
        # अग्रहीत्, अजागरीत्, औनयीत्, अश्वयीत्.
        self.assertEqual(len(HMYANTA), 3)
        self.assertEqual(len(FIVE_ROOTS), 5)
        for root in FIVE_ROOTS + EDIT:
            got = vrddhi(root, before="iṭ-sic",
                         pada="parasmaipada")
            self.assertEqual(got.sutra, "7.2.5", root)
            self.assertEqual(got.does, "", root)

    def test_that_list_does_two_different_jobs_at_once(self):
        # For ह्म्य-final stems it refuses 7.2.7's OPTION; for
        # जागृ, णि and श्वि it refuses 7.2.1's vṛddhi, which
        # 7.2.4 could not reach — they are not consonant-final.
        blocks = provisions_for("7.2.5")[0].blocks
        self.assertEqual(set(blocks), {"7.2.1", "7.2.7"})

    def test_urnu_refuses_it_optionally(self):
        # प्रौर्णवीत्, प्रौर्णावीत्.
        got = vrddhi("ūrṇu", before="iṭ-sic", pada="parasmaipada")
        self.assertEqual(got.sutra, "7.2.6")
        self.assertTrue(got.optional)

    def test_and_that_option_sits_on_top_of_another(self):
        # 1.2.3's विभाषोर्णोः is what makes the affix ङित् or
        # not, and only on the अङित् side does this rule speak.
        # Three forms out of two options, and 1.2.3 is codified.
        self.assertIn("1.2.3", provisions_for("7.2.6")[0].why)
        self.assertTrue(REGISTRY.has("1.2.3"))

    def test_a_light_a_after_a_consonant_refuses_it_optionally(self):
        # अकणीत्, अकाणीत्.
        got = vrddhi(gana="hal-ādi", part="laghu-a",
                     before="iṭ-sic", pada="parasmaipada")
        self.assertEqual(got.sutra, "7.2.7")
        self.assertTrue(got.optional)

    def test_its_atah_is_needed_for_a_reason_of_its_own(self):
        # Drop it and the vṛddhi becomes अच्-conditioned, and
        # 1.1.5's क्ङिति refusal — which only stops an
        # इक्-conditioned operation — would not reach न्यकुटीत्.
        self.assertIn("इग्लक्षणा न भवति",
                      provisions_for("7.2.7")[0].why)
        self.assertTrue(REGISTRY.has("1.1.5"))


class NothingHappensByDefault(unittest.TestCase):
    """The run says nothing about an aorist it does not name."""

    def test_an_unnamed_stem_reaches_nothing(self):
        got = vrddhi("pac")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")

    def test_and_that_is_not_the_same_as_a_refusal(self):
        # 7.2.4 says no vṛddhi and names the rule it holds off;
        # the default says only that no rule was reached.
        silent = vrddhi("pac")
        refused = vrddhi(gana="hal-anta", before="iṭ-sic")
        self.assertEqual(silent.does, refused.does)
        self.assertEqual(silent.blocked_by, ())
        self.assertNotEqual(refused.blocked_by, ())


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_opens_the_pada(self):
        self.assertEqual(VRDDHI_RUN, ("7.2.1", "7.2.7"))
        codes = [row.sutra for row in VRDDHI_TABLE]
        self.assertEqual(codes, ["7.2.%d" % n for n in range(1, 8)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in VRDDHI_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_the_rule_codified_apart_still_has_its_own_notes(self):
        # 7.2.114 मृजेर्वृद्धिः was registered long before this
        # pāda was read, and a patch that appends to the file
        # must not disturb it.
        self.assertTrue(REGISTRY.has("7.2.114"))
        self.assertGreater(len(REGISTRY.get("7.2.114").notes), 200)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_names_this_run_leans_on_are_live(self):
        # 1.1.1's वृद्धिरादैच् is what the operation IS, 1.1.5's
        # क्ङिति is what 7.2.7's अतः protects, and 1.2.3's
        # विभाषोर्णोः is the option 7.2.6 sits on. All live.
        for code in ("1.1.1", "1.1.5", "1.2.3"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_the_aorist_that_supplies_the_sic_is_live_too(self):
        # 3.1.43 च्लि लुङि and 3.1.44 च्लेः सिच् give the affix
        # every one of these seven rules is stated before, and
        # 2.4.77–78's सिज्लुक् takes it away again for the
        # गातिस्था roots. All four are codified.
        for code in ("3.1.43", "3.1.44", "2.4.77", "2.4.78"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_what_the_it_then_meets_has_landed(self):
        # अदेवीत् and अकोषीत् need 8.2.28 इट ईटि to lose their
        # सिच्, and that rule has landed with पाद ८.२ — the
        # last of the aorist's four स्-losses, and the one that
        # wants an इट् before and an ईट् after.
        self.assertTrue(REGISTRY.has("8.2.28"))


if __name__ == "__main__":
    unittest.main()
