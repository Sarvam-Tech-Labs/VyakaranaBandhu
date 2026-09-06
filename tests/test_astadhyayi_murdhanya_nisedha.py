# -*- coding: utf-8 -*-
"""
८.३.९०–११९ — the words laid down whole, and the ten refusals.

Thirty sūtras that pull two ways: twenty go on giving the
cerebral and ten take it back. The tests keep the turn in view,
and give a class of its own to the five words laid down whole —
each of which has its plain form standing beside it, which is
what shows how wide the laying-down is.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.murdhanya_nisedha import (
    NIPATANA_FIVE,
    NISEDHA_RUN,
    NISEDHA_TABLE,
    REFUSALS_FROM,
    SRPI_SIX,
    STAMBHU_THREE,
    VIKUSAMI_FOUR,
    also_cerebral,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class FiveWordsLaidDownWhole(unittest.TestCase):
    """8.3.90–94, each with its plain form beside it."""

    def test_each_of_the_five_wants_a_sense(self):
        wanted = {"pratiṣṇāta": ("8.3.90", "sūtra"),
                  "kapiṣṭhala": ("8.3.91", "gotra"),
                  "praṣṭha": ("8.3.92", "agragāmin"),
                  "viṣṭara": ("8.3.93", "vṛkṣa"),
                  "viṣṭāra": ("8.3.94", "chandonāman")}
        self.assertEqual(len(NIPATANA_FIVE), 5)
        for word in NIPATANA_FIVE:
            code, sense = wanted[word]
            got = also_cerebral(word, sense=sense)
            self.assertEqual(got.sutra, code, word)
            self.assertTrue(got.nipatana, word)
            # and without the sense the word is not reached
            self.assertNotEqual(also_cerebral(word).sutra, code,
                                word)

    def test_and_four_of_them_record_the_plain_form_outright(self):
        wanted = {"8.3.90": "प्रतिस्नातम्",
                  "8.3.91": "कपिस्थलम्",
                  "8.3.92": "प्रस्थो व्रीहीणाम्",
                  "8.3.93": "विस्तरः"}
        for code, form in wanted.items():
            self.assertIn(form, provisions_for(code)[0].keeps_out,
                          code)

    def test_and_the_last_of_them_is_made_by_two_sutras_at_once(self):
        # 3.3.34's घञ्, given छन्दोनाम्नि च, and this one, whose
        # four syllables are the same — five adhyāyas apart.
        why = provisions_for("8.3.94")[0].why
        self.assertIn("3.3.34", why)
        self.assertTrue(REGISTRY.has("3.3.34"))


class TheCompoundsAndTheNames(unittest.TestCase):
    """8.3.95–109."""

    def test_a_first_member_and_a_second_named_five_times(self):
        wanted = {("sthira", "gavi-yudhi"): "8.3.95",
                  ("sthala", "vi-ku-śami-pari"): "8.3.96",
                  ("stha", "ambādi"): "8.3.97"}
        for (second, first), code in wanted.items():
            self.assertEqual(
                also_cerebral(second, after=first).sutra, code,
                second)
        self.assertEqual(len(VIKUSAMI_FOUR), 4)

    def test_and_one_of_them_buys_a_case_ending_inside_a_compound(self):
        # सप्तम्या अलुग् भवति — which is why युधिष्ठिर keeps its
        # locative.
        self.assertIn("अलुग्", provisions_for("8.3.95")[0].why)

    def test_and_one_class_is_needed_because_su_is_not_a_preverb(self):
        # सुषामा — सु is a कर्मप्रवचनीय there, so none of
        # 8.3.65–89 could have reached it.
        got = also_cerebral(gana="suṣāmādi")
        self.assertEqual(got.sutra, "8.3.98")
        self.assertIn("कर्मप्रवचनीय",
                      provisions_for("8.3.98")[0].why)

    def test_a_name_before_an_e_and_then_the_same_by_choice(self):
        # हरिषेणः always, रोहिणीषेणः optionally.
        fixed = also_cerebral(before="e", sense="saṃjñā",
                              after="iṇ-ku-a-ga")
        self.assertEqual(fixed.sutra, "8.3.99")
        self.assertFalse(fixed.optional)
        choice = also_cerebral(before="e", sense="saṃjñā",
                               after="nakṣatra")
        self.assertEqual(choice.sutra, "8.3.100")
        self.assertTrue(choice.optional)
        self.assertIn("8.3.99", choice.blocked_by)

    def test_and_three_sutras_in_a_row_are_somebody_elses_opinion(self):
        # एकेषाम् at 8.3.104, carried down through 8.3.105 and
        # 8.3.106 — and the last of the three makes the other
        # two nearly unnecessary.
        for code in ("8.3.104", "8.3.105", "8.3.106"):
            row = provisions_for(code)[0]
            self.assertEqual(row.view, "ekeṣām", code)
            self.assertTrue(row.optional, code)
        self.assertIn("nearly unnecessary",
                      provisions_for("8.3.106")[0].why)

    def test_and_one_of_them_answers_only_a_reader_who_asks(self):
        self.assertEqual(
            also_cerebral(after="pūrvapada", chandasi=True).sutra,
            "")
        self.assertEqual(
            also_cerebral(after="pūrvapada", chandasi=True,
                          view="ekeṣām").sutra, "8.3.106")


class WhereThePadaTurns(unittest.TestCase):
    """8.3.110–119, the ten refusals."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(REFUSALS_FROM, "8.3.110")

    def test_and_everything_from_there_refuses_and_nothing_before_does(self):
        def number(code):
            return int(code.rsplit(".", 1)[1])

        for row in NISEDHA_TABLE:
            if number(row.sutra) < number(REFUSALS_FROM):
                self.assertFalse(row.refuses, row.sutra)
            else:
                self.assertTrue(row.refuses, row.sutra)
        refusing = [row for row in NISEDHA_TABLE if row.refuses]
        self.assertEqual(len(refusing), 10)

    def test_the_widest_of_them_names_six_things_at_once(self):
        # a र-following स्, and सृप्, सृज्, स्पृश्, स्पृह्, the
        # सवनादि.
        self.assertEqual(len(SRPI_SIX), 6)
        for named in SRPI_SIX:
            got = also_cerebral(named)
            self.assertEqual(got.sutra, "8.3.110", named)
            self.assertTrue(got.refuses, named)

    def test_and_one_names_two_things_that_are_reached_two_ways(self):
        # सात् as an affix's स् and a word's head as a
        # substitute's — 8.3.59's two halves.
        for named in ("sāt", "pada-ādi"):
            self.assertEqual(also_cerebral(named).sutra, "8.3.111",
                             named)
        self.assertIn("प्रत्ययसकारत्वात्",
                      provisions_for("8.3.111")[0].why)

    def test_and_one_root_is_on_both_sides_of_a_sense(self):
        # अभिसेधयति गाः of driving; प्रतिषेधयति of forbidding.
        got = also_cerebral("sedh", sense="gati")
        self.assertEqual(got.sutra, "8.3.113")
        self.assertTrue(got.refuses)
        self.assertIn("प्रतिषेधयति",
                      provisions_for("8.3.113")[0].keeps_out)

    def test_and_one_root_is_refused_in_one_shape_only(self):
        # परिसोढा without it, परिषहते with it.
        got = also_cerebral("sah", gana="soḍha")
        self.assertEqual(got.sutra, "8.3.115")
        self.assertIn("परिषहते",
                      provisions_for("8.3.115")[0].keeps_out)

    def test_and_one_refuses_two_earlier_rules_at_once(self):
        self.assertEqual(len(STAMBHU_THREE), 3)
        for root in STAMBHU_THREE:
            got = also_cerebral(root, before="caṅ")
            self.assertEqual(got.sutra, "8.3.116", root)
            self.assertEqual(set(got.blocked_by),
                             {"8.3.67", "8.3.70"}, root)

    def test_and_one_word_has_the_same_sound_twice_and_one_is_spared(self):
        # अभिषसाद — the first स् cerebral and the
        # reduplication's not.
        got = also_cerebral("sad", before="liṭ", gana="para")
        self.assertEqual(got.sutra, "8.3.118")
        self.assertIn("अभिषसाद", provisions_for("8.3.118")[0].why)

    def test_and_the_pada_closes_by_making_a_heading_optional(self):
        # 8.3.63 had made the reach across the augment
        # compulsory; न्यसीदत् beside न्यषीदत्.
        got = also_cerebral(after="ni-vi-abhi", gana="aṭ-vyavāya",
                            chandasi=True)
        self.assertEqual(got.sutra, "8.3.119")
        self.assertTrue(got.optional)
        self.assertIn("8.3.63", got.blocked_by)
        self.assertIn("8.3.8", provisions_for("8.3.119")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A स् none of these rules reaches is left as it was."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = also_cerebral("pac")
        self.assertEqual(got.sutra, "")
        self.assertIn("8.3.55-89", got.why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_closes_the_pada(self):
        self.assertEqual(NISEDHA_RUN, ("8.3.90", "8.3.119"))
        codes = [row.sutra for row in NISEDHA_TABLE]
        self.assertEqual(
            codes, ["8.3.%d" % n for n in range(90, 120)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in NISEDHA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_and_the_whole_pada_is_codified_with_no_gap(self):
        for n in range(1, 120):
            self.assertTrue(REGISTRY.has("8.3.%d" % n), n)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_everything_the_refusals_refuse_is_live(self):
        # 8.3.59, 8.3.63, 8.3.65, 8.3.66, 8.3.67 and 8.3.70 —
        # the six rules the ten refusals of this run hold off.
        for code in ("8.3.59", "8.3.63", "8.3.65", "8.3.66",
                     "8.3.67", "8.3.70"):
            self.assertTrue(REGISTRY.has(code), code)


if __name__ == "__main__":
    unittest.main()
