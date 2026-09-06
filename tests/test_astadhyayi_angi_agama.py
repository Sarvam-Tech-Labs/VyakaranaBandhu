# -*- coding: utf-8 -*-
"""
७.४.१३–२४ — the क of a compound, the अङ् aorist, and शीङ्.

Three small groups in twelve sūtras, and the tests take them in
turn. The odd one out is अवोचत्, where an augment goes inside the
stem and what comes out has no visible relation to its root.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.angi_agama import (
    ANGI_FOUR,
    ANGI_FROM,
    ANGI_RUN,
    ANGI_TABLE,
    YI_FROM,
    provisions_for,
    to_the_stem,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class BeforeTheKa(unittest.TestCase):
    """7.4.13–15."""

    def test_a_long_an_vowel_shortens_before_ka(self):
        # ज्ञका, कुमारिका, किशोरिका.
        got = to_the_stem(gana="aṇ-anta", before="ka")
        self.assertEqual(got.sutra, "7.4.13")
        self.assertEqual(got.does, "hrasva")

    def test_but_not_before_kap(self):
        # बहुकुमारीकः, बहुवधूकः, बहुलक्ष्मीकः.
        got = to_the_stem(gana="aṇ-anta", before="kap")
        self.assertEqual(got.sutra, "7.4.14")
        self.assertEqual(got.does, "")
        self.assertIn("7.4.13", got.blocked_by)

    def test_and_the_refusal_proves_which_ka_the_rule_reaches(self):
        # न कपि इति प्रतिषेधसामर्थ्यात् कनोऽपि सानुबन्धकस्य
        # ग्रहणम् इह भवति — the क reached is the one WITH its
        # markers, or the refusal would have nothing to refuse.
        self.assertIn("प्रतिषेधसामर्थ्यात्",
                      provisions_for("7.4.13")[0].why)

    def test_an_ap_final_stem_makes_that_refusal_half(self):
        # बहुखट्वाकः beside बहुखट्वकः.
        got = to_the_stem(gana="āp-anta", before="kap")
        self.assertEqual(got.sutra, "7.4.15")
        self.assertTrue(got.optional)
        self.assertIn("7.4.14", got.blocked_by)


class TheAngAorist(unittest.TestCase):
    """7.4.16–20, one guṇa and four named roots."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(ANGI_FROM, "7.4.16")

    def test_an_r_final_root_and_drs_take_guna(self):
        # अकरत्, असरत्, आरत्, जरा; अदर्शत्.
        self.assertEqual(
            to_the_stem(gana="ṛ-varṇa-anta", before="aṅ").sutra,
            "7.4.16")
        self.assertEqual(
            to_the_stem("dṛś", before="aṅ").sutra, "7.4.16")

    def test_four_roots_each_get_one_thing(self):
        # आस्थत्, अश्वत्, अपप्तत्, अवोचत्.
        self.assertEqual(len(ANGI_FOUR), 4)
        wanted = {"as": ("7.4.17", "thuk"),
                  "śvi": ("7.4.18", "a"),
                  "pat": ("7.4.19", "pum"),
                  "vac": ("7.4.20", "um")}
        for root, (code, does) in wanted.items():
            got = to_the_stem(root, before="aṅ")
            self.assertEqual(got.sutra, code, root)
            self.assertEqual(got.does, does, root)

    def test_three_of_the_four_are_augments_and_one_is_not(self):
        # श्वि becomes अ; the other three take something in.
        augments = [row.sutra for row in ANGI_TABLE
                    if row.augment]
        self.assertEqual(augments, ["7.4.17", "7.4.19", "7.4.20"])

    def test_avocat_has_no_visible_relation_to_its_root(self):
        # The उम् goes inside the stem by 1.1.47, the vowels
        # merge, and वच् + अङ् gives अवोचत् — which the note
        # says in so many words, and 1.1.47 is codified.
        why = provisions_for("7.4.20")[0].why
        self.assertIn("1.1.47", why)
        self.assertIn("अवोचत्", why)
        self.assertTrue(REGISTRY.has("1.1.47"))


class BeforeAYa(unittest.TestCase):
    """7.4.21–24, four rules about य्."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(YI_FROM, "7.4.21")

    def test_sin_takes_guna_before_a_sarvadhatuka(self):
        # शेते, शयाते, शेरते; शिश्ये in the perfect.
        got = to_the_stem("śīṅ", before="sārvadhātuka")
        self.assertEqual(got.sutra, "7.4.21")
        self.assertEqual(got.does, "guṇa")

    def test_and_ayan_before_a_knit_ya(self):
        # शय्यते, प्रशय्य, उपशय्य.
        got = to_the_stem("śīṅ", before="ya-kṅit")
        self.assertEqual(got.sutra, "7.4.22")
        self.assertEqual(got.does, "ayaṅ")

    def test_uh_and_i_shorten_after_a_preverb(self):
        # समुह्यते; उदियात्, समियात्.
        self.assertEqual(
            to_the_stem("ūh", upasarga="upasarga",
                        before="ya-kṅit").sutra, "7.4.23")
        self.assertEqual(
            to_the_stem("i", upasarga="upasarga",
                        before="liṅ").sutra, "7.4.24")

    def test_and_neither_without_one(self):
        # ऊह्यते, ईयात्.
        self.assertNotEqual(
            to_the_stem("ūh", before="ya-kṅit").sutra, "7.4.23")
        self.assertNotEqual(
            to_the_stem("i", before="liṅ").sutra, "7.4.24")

    def test_the_last_one_undoes_a_lengthening_just_made(self):
        # दीर्घत्वे कृते ह्रस्वोऽनेन भवति — 7.4.25 lengthens and
        # this shortens again, and that rule is codified.
        self.assertIn("दीर्घत्वे कृते",
                      provisions_for("7.4.24")[0].why)
        self.assertTrue(REGISTRY.has("7.4.25"))


class NothingHappensByDefault(unittest.TestCase):
    """A stem outside all three groups is untouched."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = to_the_stem("pac", before="aṅ")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(ANGI_RUN, ("7.4.13", "7.4.24"))
        codes = [row.sutra for row in ANGI_TABLE]
        self.assertEqual(
            codes, ["7.4.%d" % n for n in range(13, 25)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in ANGI_TABLE:
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

    def test_the_aorist_and_the_affixes_this_run_names_are_live(self):
        # 3.1.52 अस्यतिवक्तिख्यातिभ्योऽङ् supplies the अङ्,
        # 5.3.70's कन् the क, and 5.4.153 the कप्.
        for code in ("3.1.52", "5.3.70", "5.4.153"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_abhyasa_heading_has_since_been_read(self):
        # 7.4.58 opens अभ्यासस्य, the adhyāya's last heading, and
        # 7.4.97 closes it. Both are codified now, and with them
        # every sūtra of पाद ७.४.
        for n in range(1, 98):
            self.assertTrue(REGISTRY.has("7.4.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
