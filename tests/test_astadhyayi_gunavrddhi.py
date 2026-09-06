# -*- coding: utf-8 -*-
"""
Tests for the guṇa/vṛddhi prohibitions — 1.1.4, 1.1.5, 1.1.6.

These three close the run 1.1.1–1.1.10 and exercise almost everything under it
at once. A single call to `guna_or_none("i", affix=kta)` puts to work: the
śivasūtras, 1.1.71 resolving eṄ, 1.1.2 naming the candidates, 1.1.3 fixing the
class, 1.1.9's feature table, 1.1.50 choosing e over a, 1.3.8 finding the k of
क्त, and 1.1.5 vetoing the lot. If any of them is wrong, चितः comes out चेतः.

The Kāśikā argues each prohibition by asking what a word in it excludes and
answering with a form; those questions and answers are the tests.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.adesa import (
    Adesa,
    DIDHI_VEVI_IT,
    KNIT,
    guna_of,
    guna_or_none,
    guna_vrddhi_blocked,
    vrddhi_of,
    vrddhi_or_none,
)
from src.astadhyayi.itsamjna import PRATYAYA
from src.astadhyayi.rules.adhyaya_1_pada_1 import IK_ALL


class DhatuLopa(unittest.TestCase):
    """1.1.4 न धातुलोप आर्धधातुके."""

    def test_both_conditions_are_required(self):
        self.assertIsNotNone(
            guna_vrddhi_blocked("u", ardhadhatuka=True, dhatu_lopa=True)
        )
        self.assertIsNone(
            guna_vrddhi_blocked("u", ardhadhatuka=True, dhatu_lopa=False)
        )
        self.assertIsNone(
            guna_vrddhi_blocked("u", ardhadhatuka=False, dhatu_lopa=True)
        )
        self.assertIsNone(guna_vrddhi_blocked("u"))

    def test_ardhadhatuke_iti_kim_roravīti(self):
        """
        आर्धधातुके इति किम्? त्रिधा बद्धो वृषभो रोरवीति — a sārvadhātuka, so
        the prohibition does not reach and the guṇa stands.
        """
        self.assertEqual(
            guna_or_none("u", ardhadhatuka=False, dhatu_lopa=True), "o"
        )

    def test_it_names_1_1_4_when_it_fires(self):
        blocked = guna_vrddhi_blocked("u", ardhadhatuka=True, dhatu_lopa=True)
        self.assertEqual(blocked.by, "1.1.4")
        self.assertIn("धातुलोपे", blocked.why)

    def test_it_blocks_vrddhi_as_well_as_guna(self):
        """गुणवृद्धी comes down from 1.1.3 as a dvandva; both are forbidden."""
        conditions = dict(ardhadhatuka=True, dhatu_lopa=True)
        self.assertIsNone(guna_or_none("u", **conditions))
        self.assertIsNone(vrddhi_or_none("u", **conditions))


class Knit(unittest.TestCase):
    """1.1.5 क्ङिति च."""

    def setUp(self):
        self.kta = Adesa.from_upadesa("kta", PRATYAYA)

    def test_the_marks_are_derived_from_the_affix_not_asserted(self):
        """
        क्त is kit because 1.3.8 makes its k indicatory. Nothing here says so;
        the it-rules find it. This is the join between the two blocks.
        """
        self.assertEqual(self.kta.its, {"k"})
        self.assertEqual(self.kta.form, "ta")

    def test_citah_the_kasikas_first_example(self):
        """
        चितः — ci + kta. Guṇa would give चेतः. Everything in the chain has to
        be right for this one assertion to hold.
        """
        self.assertEqual(guna_of("i"), "e", "the operation that is forbidden")
        self.assertIsNone(guna_or_none("i", affix=self.kta))
        self.assertEqual(
            guna_vrddhi_blocked("i", affix=self.kta).by, "1.1.5"
        )

    def test_the_kasikas_whole_series(self):
        """चितः, स्तुतः, भिन्नः, मृष्टः — i, u and ṛ stems alike."""
        for vowel in ("i", "u", "ṛ"):
            self.assertIsNone(guna_or_none(vowel, affix=self.kta), vowel)
            self.assertIsNone(vrddhi_or_none(vowel, affix=self.kta), vowel)

    def test_a_non_kit_affix_lets_the_operation_through(self):
        """शप् is śit and pit, neither of which is in क्ङिति."""
        sap = Adesa.from_upadesa("śap", PRATYAYA)
        self.assertEqual(sorted(sap.its), ["p", "ś"])
        self.assertEqual(guna_or_none("i", affix=sap), "e")

    def test_ngit_as_well_as_kit(self):
        self.assertIsNone(
            guna_or_none("i", affix=Adesa("nu", frozenset("ṅ")))
        )

    def test_g_counts_by_cartva(self):
        """गकारोऽप्यत्र चर्त्वभूतो निर्दिश्यते."""
        self.assertIn("g", KNIT)
        self.assertIsNone(
            guna_or_none("i", affix=Adesa("snu", frozenset("g")))
        )

    def test_knit_holds_exactly_the_three_letters(self):
        self.assertEqual(KNIT, frozenset({"k", "ṅ", "g"}))

    def test_no_affix_means_no_prohibition_from_this_sutra(self):
        self.assertEqual(guna_or_none("i"), "e")


class DidhiVeviIt(unittest.TestCase):
    """1.1.6 दीधीवेवीटाम्."""

    def test_the_three_named_items(self):
        for item in DIDHI_VEVI_IT:
            blocked = guna_vrddhi_blocked("i", item=item)
            self.assertIsNotNone(blocked, item)
            self.assertEqual(blocked.by, "1.1.6", item)

    def test_it_is_a_list_and_not_a_class(self):
        """Nothing groups two roots and an augment but this sūtra."""
        self.assertEqual(len(DIDHI_VEVI_IT), 3)
        for other in ("bhū", "kṛ", "dīdh", "vev", "i"):
            self.assertIsNone(guna_vrddhi_blocked("i", item=other), other)

    def test_an_unnamed_item_passes(self):
        self.assertEqual(guna_or_none("i", item="bhū"), "e")


class IkahGovernsAllThree(unittest.TestCase):
    """
    इकः and गुणवृद्धी come down from 1.1.3 into every one of the three, and
    the Kāśikā insists on it twice: इक इत्येव — अभाजि, रागः under 1.1.4;
    इकः इत्येव — कामयते under 1.1.5.
    """

    def test_a_target_outside_ik_is_never_blocked(self):
        kta = Adesa.from_upadesa("kta", PRATYAYA)
        for vowel in ("a", "ā", "e", "o", "ai", "au"):
            self.assertIsNone(
                guna_vrddhi_blocked(vowel, affix=kta), vowel
            )
            self.assertIsNone(
                guna_vrddhi_blocked(
                    vowel, ardhadhatuka=True, dhatu_lopa=True
                ), vowel,
            )
            self.assertIsNone(
                guna_vrddhi_blocked(vowel, item="dīdhī"), vowel
            )

    def test_every_ik_vowel_is_blockable(self):
        kta = Adesa.from_upadesa("kta", PRATYAYA)
        for vowel in IK_ALL:
            self.assertIsNotNone(
                guna_vrddhi_blocked(vowel, affix=kta), vowel
            )

    def test_nothing_is_blocked_for_a_sound_outside_the_inventory(self):
        self.assertIsNone(guna_vrddhi_blocked("q", item="dīdhī"))


class Precedence(unittest.TestCase):
    """Which prohibition is reported when more than one applies."""

    def test_the_earlier_sutra_is_named(self):
        """
        Not a claim about the grammar — all three forbid the same thing, so
        which one is cited makes no difference to the result. It is a claim
        about the report being stable, which matters when a derivation is read
        back.
        """
        kta = Adesa.from_upadesa("kta", PRATYAYA)
        blocked = guna_vrddhi_blocked(
            "i", affix=kta, ardhadhatuka=True, dhatu_lopa=True, item="dīdhī"
        )
        self.assertEqual(blocked.by, "1.1.4")

    def test_the_outcome_is_the_same_whichever_fires(self):
        kta = Adesa.from_upadesa("kta", PRATYAYA)
        for conditions in [
            dict(affix=kta),
            dict(ardhadhatuka=True, dhatu_lopa=True),
            dict(item="iṭ"),
        ]:
            self.assertIsNone(guna_or_none("i", **conditions), conditions)


class TheWholeChain(unittest.TestCase):
    """
    What one call actually exercises, end to end.

    This is the integration test for everything codified so far: without the
    veto the answer is the ordinary guṇa, computed from the śivasūtras through
    1.1.71, 1.1.2, 1.1.3, 1.1.9's features, 1.1.50 and 1.1.51; with it, nothing.
    """

    def test_the_guna_series_survives_when_nothing_forbids_it(self):
        for vowel, expected in [("i", "e"), ("u", "o"), ("ṛ", "ar")]:
            self.assertEqual(guna_or_none(vowel), expected, vowel)

    def test_and_the_vrddhi_series(self):
        for vowel, expected in [("i", "ai"), ("u", "au"), ("ṛ", "ār")]:
            self.assertEqual(vrddhi_or_none(vowel), expected, vowel)

    def test_a_kit_affix_suppresses_the_whole_series(self):
        kta = Adesa.from_upadesa("kta", PRATYAYA)
        for vowel in ("i", "u", "ṛ"):
            self.assertIsNone(guna_or_none(vowel, affix=kta), vowel)
            self.assertIsNone(vrddhi_or_none(vowel, affix=kta), vowel)

    def test_guna_of_is_unaffected_by_the_prohibitions(self):
        """
        The unconditioned functions must keep answering what the operation
        would be, or a caller could not tell 'forbidden' from 'not applicable'.
        """
        self.assertEqual(guna_of("i"), "e")
        self.assertEqual(vrddhi_of("i"), "ai")


class Registration(unittest.TestCase):
    IDS = ("1.1.4", "1.1.5", "1.1.6")

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_all_three_read_ikah_and_gunavrddhi_from_1_1_3(self):
        for sutra_id in self.IDS:
            carried = " ".join(self.registry.get(sutra_id).anuvrtti)
            self.assertIn("1.1.3", carried, sutra_id)

    def test_1_1_5_and_1_1_6_read_na_from_1_1_4(self):
        for sutra_id in ("1.1.5", "1.1.6"):
            carried = " ".join(self.registry.get(sutra_id).anuvrtti)
            self.assertIn("1.1.4", carried, sutra_id)

    def test_the_opening_run_is_now_continuous(self):
        for number in range(1, 11):
            self.assertTrue(
                self.registry.has(f"1.1.{number}"), f"1.1.{number} missing"
            )

    def test_the_two_uncodified_provisions_on_1_1_5_are_recorded(self):
        notes = self.registry.get("1.1.5").notes
        self.assertIn("SCOPE", notes)
        self.assertIn("मृजेरजादौ", notes)
        self.assertIn("यासुट्", notes)


if __name__ == "__main__":
    unittest.main()
