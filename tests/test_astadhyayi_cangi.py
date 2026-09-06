# -*- coding: utf-8 -*-
"""
७.४.१–१२ — the चङ् aorist's shortening, and the perfect's guṇa.

पाद ७.४ opens on one rule and five that qualify it, so the tests
follow that shape — and the class that matters most is the one
about the order against the reduplication, which the vṛtti
settles twice by two different arguments.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.cangi import (
    BHRAJADI,
    CANGI_RUN,
    CANGI_TABLE,
    JNAPAKA,
    LITI_FROM,
    SR_DR_PR,
    before_cang,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheShortening(unittest.TestCase):
    """7.4.1, and how it is ordered against the doubling."""

    def test_a_causal_penult_shortens_before_cang(self):
        # अचीकरत्, अजीहरत्, अलीलवत्, अपीपवत्.
        got = before_cang(part="upadhā", before="caṅ-ṇi")
        self.assertEqual(got.sutra, "7.4.1")
        self.assertEqual(got.does, "hrasva")

    def test_the_order_is_settled_by_two_different_arguments(self):
        # परत्वाद् उपधाह्रस्वत्वम् for अचीकरत्, and a ज्ञापक for
        # मा भवान् अटिटत्, where the doubling is compulsory and
        # would otherwise win.
        why = provisions_for("7.4.1")[0].why
        self.assertIn("परत्वाद्", why)
        self.assertIn("ज्ञापकं", why)

    def test_the_jnapaka_is_read_out_of_the_next_sutras_list(self):
        # ओणेः ऋदित्करणं ज्ञापकम् — marking ओण् as ऋदित् at
        # 7.4.2 would be idle unless the shortening beat the
        # doubling even where the doubling is compulsory.
        self.assertIn("ऋदित्करणं", JNAPAKA)
        self.assertIn("बाध्यते", JNAPAKA)


class WhatQualifiesIt(unittest.TestCase):
    """7.4.2–8, one refusal and five substitutes."""

    def test_three_classes_refuse_it_outright(self):
        # अममालत्, अशशासत्, अबबाधत्.
        got = before_cang(gana="a-glopi-śās-ṛdit",
                          before="caṅ-ṇi")
        self.assertEqual(got.sutra, "7.4.2")
        self.assertEqual(got.does, "")
        self.assertIn("7.4.1", got.blocked_by)

    def test_and_the_refusal_is_for_where_a_consonant_goes_too(self):
        # हलचोरादेशे तु न सिध्यतीति तदर्थम् एतद् वचनम् — where
        # only the vowel is lost, 1.1.56 would have saved the
        # form anyway, and that rule is codified.
        self.assertIn("हलचोरादेशे",
                      provisions_for("7.4.2")[0].why)
        self.assertTrue(REGISTRY.has("1.1.56"))

    def test_seven_roots_shorten_only_optionally(self):
        # अबिभ्रजत् beside अबभ्राजत्.
        self.assertEqual(len(BHRAJADI), 7)
        for root in BHRAJADI:
            got = before_cang(root, part="upadhā",
                              before="caṅ-ṇi")
            self.assertEqual(got.sutra, "7.4.3", root)
            self.assertTrue(got.optional, root)

    def test_and_the_vrtti_rejects_one_reading_of_that_list(self):
        # भ्राजभासोर् ऋदित्करणम् अपाणिनीयम् — reading the first
        # two as ऋदित् would put them under 7.4.2 instead.
        self.assertIn("अपाणिनीयम्",
                      provisions_for("7.4.3")[0].why)

    def test_three_stems_take_something_else_instead(self):
        # अपीप्यत्, अतिष्ठिपत्, अजिघ्रिपत्.
        wanted = {"pib": ("7.4.4", "lopa"),
                  "tiṣṭh": ("7.4.5", "it"),
                  "jighr": ("7.4.6", "it")}
        for root, (code, does) in wanted.items():
            got = before_cang(root, part="upadhā",
                              before="caṅ-ṇi")
            self.assertEqual(got.sutra, code, root)
            self.assertEqual(got.does, does, root)

    def test_and_only_pib_changes_its_reduplication_too(self):
        # अपीप्यत् — the ई is the abhyāsa's, not the stem's.
        changing = [row.sutra for row in CANGI_TABLE
                    if row.abhyasa]
        self.assertEqual(changing, ["7.4.4"])

    def test_an_r_penult_becomes_a_plain_r_optionally(self):
        # अचीकृतत् beside अचिकीर्तत्.
        got = before_cang(part="ṛ-varṇa", before="caṅ-ṇi")
        self.assertEqual(got.sutra, "7.4.7")
        self.assertTrue(got.optional)

    def test_and_it_beats_three_inner_rules_by_being_stated(self):
        # वचनसामर्थ्याद् अन्तरङ्गा अपि इररारो बाध्यन्ते.
        self.assertIn("वचनसामर्थ्याद्",
                      provisions_for("7.4.7")[0].why)

    def test_but_in_the_veda_it_is_compulsory(self):
        # अवीवृधत् पुरोडाशेन.
        got = before_cang(part="ṛ-varṇa", before="caṅ-ṇi",
                          chandasi=True)
        self.assertEqual(got.sutra, "7.4.8")
        self.assertFalse(got.optional)
        self.assertIn("7.4.7", got.blocked_by)


class ThenThePerfect(unittest.TestCase):
    """7.4.9–12, where the run turns."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(LITI_FROM, "7.4.9")

    def test_everything_from_there_wants_the_perfect(self):
        def number(code):
            return int(code.rsplit(".", 1)[1])

        for row in CANGI_TABLE:
            if number(row.sutra) >= number(LITI_FROM):
                self.assertEqual(row.before, ("liṭ",), row.sutra)

    def test_day_becomes_digi_and_displaces_the_reduplication(self):
        # अवदिग्ये — दिग्यादेशेन द्विर्वचनस्य बाधनम् इष्यते.
        got = before_cang("day", before="liṭ")
        self.assertEqual(got.sutra, "7.4.9")
        self.assertIn("द्विर्वचनस्य बाधनम्",
                      provisions_for("7.4.9")[0].why)

    def test_a_cluster_initial_r_final_root_takes_guna(self):
        # सस्वरतुः, दध्वरतुः, सस्मरतुः.
        got = before_cang(gana="ṛ-anta-saṃyoga-ādi",
                          before="liṭ")
        self.assertEqual(got.sutra, "7.4.10")
        self.assertEqual(got.does, "guṇa")

    def test_and_it_reaches_past_a_refusal(self):
        # प्रतिषेधविषयेऽपि गुणो यथा स्यात् — 1.1.5 would have
        # refused it, and vṛddhi still wins where it can.
        why = provisions_for("7.4.10")[0].why
        self.assertIn("प्रतिषेधविषयेऽपि", why)
        self.assertIn("सस्वार", why)

    def test_three_more_roots_take_it_for_two_reasons(self):
        # आनर्च्छ, आरतुः, निचकरतुः — for ऋच्छ् the guṇa was
        # never available and for the ॠ-final roots refused.
        self.assertEqual(before_cang("ṛcch", before="liṭ").sutra,
                         "7.4.11")
        self.assertIn("never available",
                      provisions_for("7.4.11")[0].why)

    def test_and_three_are_optionally_short_instead(self):
        # विशश्रतुः beside विशशरतुः.
        self.assertEqual(SR_DR_PR, ("śṝ", "dṝ", "pṝ"))
        for root in SR_DR_PR:
            got = before_cang(root, before="liṭ")
            self.assertEqual(got.sutra, "7.4.12", root)
            self.assertTrue(got.optional, root)
            self.assertIn("7.4.11", got.blocked_by, root)

    def test_and_some_reject_that_sutra_outright(self):
        # केचिदेतत् सूत्रं प्रत्याचक्षते — deriving the short
        # forms from three separate roots श्रा, द्रा and प्रा
        # instead, which the note records rather than settling.
        why = provisions_for("7.4.12")[0].why
        self.assertIn("reject the sūtra outright", why)
        self.assertIn("श्रा", why)


class NothingHappensByDefault(unittest.TestCase):
    """A root outside both environments is untouched."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = before_cang("pac", before="śap")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_opens_the_pada(self):
        self.assertEqual(CANGI_RUN, ("7.4.1", "7.4.12"))
        codes = [row.sutra for row in CANGI_TABLE]
        self.assertEqual(
            codes, ["7.4.%d" % n for n in range(1, 13)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in CANGI_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_the_rules_codified_apart_in_this_pada_survive(self):
        # 7.4.59, 7.4.60, 7.4.66, 7.4.82, 7.4.83, 7.4.90 and
        # 7.4.91 were registered long before this pāda was read,
        # through a loop over a dict. A splice ahead of that
        # machinery must not disturb them.
        for n in (59, 60, 66, 82, 83, 90, 91):
            self.assertTrue(REGISTRY.has("7.4.%d" % n), n)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_aorist_and_the_doubling_this_run_orders_are_live(self):
        # 3.1.48 णिश्रिद्रुस्रुभ्यः कर्तरि चङ् supplies the चङ्,
        # and 6.1.1 एकाचो द्वे प्रथमस्य the reduplication these
        # rules are ordered against. Both codified.
        self.assertTrue(REGISTRY.has("3.1.48"))
        self.assertTrue(REGISTRY.has("6.1.1"))

    def test_and_the_rest_of_this_pada_has_since_been_read(self):
        # 7.4.58 अत्र लोपोऽभ्यासस्य opens the last heading of the
        # adhyāya — अभ्यासस्य, running to 7.4.97 — and both ends
        # of it are now codified, in `abhyasa.py`. This test was
        # written as the debt and states the live dependency now.
        self.assertTrue(REGISTRY.has("7.4.58"))
        self.assertTrue(REGISTRY.has("7.4.97"))


if __name__ == "__main__":
    unittest.main()
