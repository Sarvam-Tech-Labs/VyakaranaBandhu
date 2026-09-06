# -*- coding: utf-8 -*-
"""
८.३.५५–८९ — अपदान्तस्य मूर्धन्यः, and the स् that becomes ष्.

Two headings open one after another and both run to the pāda's
end, and a third runs seven sūtras. The tests keep all three in
view, because almost every rule of the run is unintelligible
without them — and 8.3.63 in particular, which is the only
reason the imperfects of these roots keep their cerebral.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.murdhanya import (
    ADVYAVAYA_TO,
    APADANTA_TO,
    INKOH_FROM,
    MURDHANYA_RUN,
    MURDHANYA_TABLE,
    SEVADI_EIGHT,
    SIDHVAM_THREE,
    SIVADI,
    SUNOTI_ELEVEN,
    provisions_for,
    the_cerebral,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class ThreeHeadings(unittest.TestCase):
    """8.3.55, 8.3.57 and 8.3.63."""

    def test_the_first_of_them_cancels_an_earlier_one(self):
        # पदाधिकारो निवृत्तः — 8.1.16's पदस्य stops here.
        self.assertEqual(APADANTA_TO, "8.3.119")
        why = provisions_for("8.3.55")[0].why
        self.assertIn("पदाधिकारो निवृत्तः", why)
        self.assertTrue(REGISTRY.has("8.1.16"))

    def test_the_second_says_what_must_stand_before(self):
        # इणः कवर्गात् च — which is why अग्निषु has a ष् and
        # वृक्षेषु has not.
        self.assertEqual(INKOH_FROM, "8.3.57")
        self.assertIn("कवर्गात्", provisions_for("8.3.57")[0].why)

    def test_and_the_third_stops_in_the_middle_of_the_run(self):
        # प्राक् सितात् — 8.3.70 is the last sūtra to name सित्.
        self.assertEqual(ADVYAVAYA_TO, "8.3.70")
        self.assertIn("सित्", provisions_for("8.3.70")[0].why)

    def test_and_none_of_the_three_answers_anything(self):
        headings = [row.sutra for row in MURDHANYA_TABLE
                    if row.heading]
        self.assertEqual(headings, ["8.3.55", "8.3.57", "8.3.63"])
        for code in headings:
            self.assertNotEqual(
                the_cerebral(gana="ādeśa-pratyaya-sa",
                             after="iṇ-ku").sutra, code, code)


class WhatBecomesCerebral(unittest.TestCase):
    """8.3.56–62."""

    def test_the_rule_the_whole_locative_plural_turns_on(self):
        # अग्निषु, वायुषु, कर्तृषु — and सिषेव for the
        # substitute half.
        got = the_cerebral(gana="ādeśa-pratyaya-sa",
                           after="iṇ-ku")
        self.assertEqual(got.sutra, "8.3.59")
        self.assertEqual(got.does, "ṣa")
        self.assertIn("षष्ठी भेदेन",
                      provisions_for("8.3.59")[0].why)

    def test_and_it_reaches_across_three_things(self):
        # सर्पींषि, यजूंषि — across the नुम् and its anusvāra.
        got = the_cerebral(gana="num-visarjanīya-śar-vyavāya",
                           after="iṇ-ku")
        self.assertEqual(got.sutra, "8.3.58")
        self.assertIn("प्रत्येकम्",
                      provisions_for("8.3.58")[0].why)

    def test_three_roots_are_added_that_the_rule_would_not_reach(self):
        # शिष्टः, उषितः, जक्षतुः — neither a substitute nor an
        # affix among them.
        for root in ("śās", "vas", "ghas"):
            self.assertEqual(
                the_cerebral(root, after="iṇ-ku").sutra,
                "8.3.60", root)

    def test_and_one_pair_prescribes_a_sound_for_itself(self):
        # सिस्वेदयिषति — सकारस्य सकारवचनम्, which is the same
        # device 8.3.25 used for the म्.
        got = the_cerebral("svid", after="abhyāsa",
                           before="ṣa-san")
        self.assertEqual(got.sutra, "8.3.62")
        self.assertEqual(got.does, "sa")
        self.assertIn("8.3.61", got.blocked_by)
        self.assertIn("सकारवचनम्", provisions_for("8.3.62")[0].why)


class TheRootsAfterPreverbs(unittest.TestCase):
    """8.3.64–77, the longest stretch of the run."""

    def test_eleven_roots_take_it_after_any_preverb(self):
        # अभिषुणोति, अभिष्यति, अभिषिञ्चति, परिष्वजते.
        self.assertEqual(len(SUNOTI_ELEVEN), 11)
        for root in SUNOTI_ELEVEN:
            got = the_cerebral(root, after="upasarga")
            self.assertEqual(got.sutra, "8.3.65", root)

    def test_and_three_more_have_rules_of_their_own(self):
        # सद् after any but प्रति, स्तम्भ्, and स्वन् of eating.
        self.assertEqual(
            the_cerebral("sad", after="upasarga").sutra, "8.3.66")
        self.assertEqual(
            the_cerebral("stambh", after="upasarga").sutra,
            "8.3.67")
        self.assertEqual(
            the_cerebral("svan", after="vi-ava",
                         sense="bhojana").sutra, "8.3.69")

    def test_and_one_preverb_gets_a_sense_condition_of_its_own(self):
        # अव with स्तम्भ् — only of support or nearness.
        for sense in ("ālambana", "āvidūrya"):
            got = the_cerebral("stambh", after="ava", sense=sense)
            self.assertEqual(got.sutra, "8.3.68", sense)
            self.assertIn("8.3.67", got.blocked_by, sense)

    def test_eight_roots_take_it_after_three_preverbs(self):
        # परिषेवते, निषेवते, विषेवते.
        self.assertEqual(len(SEVADI_EIGHT), 8)
        for root in SEVADI_EIGHT:
            self.assertEqual(
                the_cerebral(root, after="pari-ni-vi").sutra,
                "8.3.70", root)

    def test_and_five_of_those_eight_lose_the_augments_reach(self):
        # With 8.3.63's heading over, what was compulsory
        # becomes a choice.
        self.assertEqual(len(SIVADI), 5)
        for root in SIVADI:
            got = the_cerebral(root, gana="aṭ-vyavāya",
                               after="pari-ni-vi")
            self.assertEqual(got.sutra, "8.3.71", root)
            self.assertTrue(got.optional, root)
            self.assertIn("8.3.70", got.blocked_by, root)

    def test_and_one_rule_says_always_because_everything_round_it_does_not(self):
        # विष्कभ्नाति — नित्यम् against three optional rules
        # before and one after.
        got = the_cerebral("skabh", after="vi")
        self.assertEqual(got.sutra, "8.3.77")
        self.assertFalse(got.optional)
        for code in ("8.3.72", "8.3.73", "8.3.74", "8.3.76"):
            self.assertTrue(provisions_for(code)[0].optional, code)

    def test_and_one_takes_it_away_again_in_one_regions_usage(self):
        # परिस्कन्दः प्राच्यभरतेषु — the only geographical
        # condition in the pāda.
        got = the_cerebral("pariskanda", sense="prācyabharata")
        self.assertEqual(got.sutra, "8.3.75")
        self.assertIn("8.3.74", got.blocked_by)
        senses = {s for row in MURDHANYA_TABLE for s in row.sense}
        self.assertIn("prācyabharata", senses)


class ADhAmongTheS(unittest.TestCase):
    """8.3.78–79, where a ध् goes cerebral instead."""

    def test_the_dh_of_three_endings_becomes_dha(self):
        # च्योषीढ्वम्, अच्योढ्वम्, चकृढ्वे.
        self.assertEqual(len(SIDHVAM_THREE), 3)
        for ending in SIDHVAM_THREE:
            got = the_cerebral(gana="iṇ-anta-aṅga", before=ending)
            self.assertEqual(got.sutra, "8.3.78", ending)
            self.assertEqual(got.does, "ḍha", ending)

    def test_and_after_an_it_it_is_optional_and_meets_pada_two(self):
        # लविषीढ्वम् beside लविषीध्वम् — the second of the pair
        # is what 8.2.25 धि च was stated for.
        got = the_cerebral(gana="iṭ-para", before="liṭ")
        self.assertEqual(got.sutra, "8.3.79")
        self.assertTrue(got.optional)
        self.assertIn("8.2.25", provisions_for("8.3.79")[0].why)
        self.assertTrue(REGISTRY.has("8.2.25"))


class TheCompounds(unittest.TestCase):
    """8.3.80–89, one first member and one second."""

    def test_each_of_them_names_a_pair(self):
        wanted = {("saṅga", "aṅguli"): "8.3.80",
                  ("sthāna", "bhīru"): "8.3.81",
                  ("soma", "agni"): "8.3.82",
                  ("stoma", "jyotis-āyus"): "8.3.83",
                  ("svasṛ", "mātṛ-pitṛ"): "8.3.84"}
        for (second, first), code in wanted.items():
            got = the_cerebral(second, after=first,
                               sense="samāsa")
            self.assertEqual(got.sutra, code, second)

    def test_and_one_of_them_wants_a_lengthened_first_member(self):
        # अग्नेर् दीर्घात् सोमस्य इष्यते — which is why the pair
        # of gods is अग्नीषोमौ.
        self.assertIn("दीर्घात्", provisions_for("8.3.82")[0].why)

    def test_and_the_same_two_words_differ_only_in_their_shape(self):
        # मातृष्वसा compulsorily, मातुःष्वसा by choice.
        fixed = the_cerebral("svasṛ", after="mātṛ-pitṛ",
                             sense="samāsa")
        choice = the_cerebral("svasṛ", after="mātuḥ-pituḥ",
                              sense="samāsa")
        self.assertFalse(fixed.optional)
        self.assertTrue(choice.optional)
        self.assertIn("8.3.84", choice.blocked_by)

    def test_and_the_run_ends_on_a_sense_and_a_second_sutra_borrowed(self):
        # निष्णातः कटकरणे of skill, and नदीष्णः through
        # 3.2.4's सुपि स्थः, which is codified.
        got = the_cerebral("snā", after="ni-nadī",
                           sense="kauśala")
        self.assertEqual(got.sutra, "8.3.89")
        self.assertIn("3.2.4", provisions_for("8.3.89")[0].why)
        self.assertTrue(REGISTRY.has("3.2.4"))


class NothingHappensByDefault(unittest.TestCase):
    """A स् none of these rules reaches stands as it is."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = the_cerebral("pac", after="upasarga")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(MURDHANYA_RUN, ("8.3.55", "8.3.89"))
        codes = [row.sutra for row in MURDHANYA_TABLE]
        self.assertEqual(
            codes, ["8.3.%d" % n for n in range(55, 90)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in MURDHANYA_TABLE:
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

    def test_everything_this_run_appeals_to_is_live(self):
        # 8.1.16's heading, which 8.3.55 cancels; 8.2.25's धि च,
        # which 8.3.79 meets; and 3.2.4's सुपि स्थः.
        for code in ("8.1.16", "8.2.25", "3.2.4"):
            self.assertTrue(REGISTRY.has(code), code)


if __name__ == "__main__":
    unittest.main()
