# -*- coding: utf-8 -*-
"""
६.४.११५–१२८ — the ए of the perfect, and the copy that goes with it.

Two things carry this run.

**One rule does two things at once.** 6.4.120 replaces a vowel AND
deletes a syllable, and neither happens without the other. पेचुः
is what पपचुः became, and a codification that recorded only the ए
would leave the copy standing.

**And six sūtras argue about who else gets it.** 6.4.122's four
roots are named for three different reasons, and the vṛtti says
which for each — so the record has to keep the reasons, not just
the roots.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.abhyasa_lopa import (
    ABHYASA_RUN, ETVA_TABLE, FOUR_CONDITIONS, NO_ETVA,
    OPTIONAL_THREE, PHANADI, WHY_FOUR_MORE, in_the_perfect,
    provisions_for)
from src.astadhyayi.sarvadhatuka_lopa import SARVA_RUN
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunFollowsTheOneBeforeIt(unittest.TestCase):
    def test_it_opens_one_sutra_after_the_present_tense_run(self):
        self.assertEqual(_n(ABHYASA_RUN[0])[2],
                         _n(SARVA_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_115_to_128(self):
        got = [row.sutra for row in ETVA_TABLE]
        self.assertEqual(got, ["6.4.%d" % n
                               for n in range(115, 129)])

    def test_every_row_carries_its_reason(self):
        for row in ETVA_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = in_the_perfect("bhū", before="liṭ")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("reduplication stands", got.why)


class OneRuleDoesTwoThingsAtOnce(unittest.TestCase):
    """
    6.4.120 replaces the अ with ए AND drops the reduplication.
    Recording only the vowel would leave *पपेचुः, which is not a
    word, so the operation has to be one name and not two.
    """

    def test_the_operation_names_both_halves(self):
        row, = provisions_for("6.4.120")
        self.assertEqual(row.does, "et-abhyāsalopa")

    def test_and_eight_rules_share_that_one_operation(self):
        got = [row.sutra for row in ETVA_TABLE
               if row.does == "et-abhyāsalopa"]
        self.assertEqual(got, ["6.4.119"] + ["6.4.%d" % n
                                             for n in range(120,
                                                            126)])

    def test_the_plain_case_is_reached(self):
        got = in_the_perfect(before="liṭ", result="kṅit")
        self.assertEqual((got.sutra, got.does),
                         ("6.4.120", "et-abhyāsalopa"))

    def test_and_the_first_of_the_eight_says_why_the_whole_copy_goes(
            self):
        """**शिदयं लोपः। तेन सर्वस्याभ्यासस्य भवति** — the loss
        is a शित्, so 1.1.55 takes the whole syllable and not
        merely its last sound."""
        row, = provisions_for("6.4.119")
        self.assertIn("शिदयं लोपः", row.why)
        self.assertTrue(REGISTRY.has("1.1.55"))


class FourConditionsAndFourCounterExamples(unittest.TestCase):
    """
    6.4.120 states four conditions and the vṛtti tests three of
    them with a form apiece: दिदिवतुः for the vowel, शश्रमिथ for
    the single consonants, ररासे for the tapara.
    """

    def test_the_four_are_recorded(self):
        self.assertEqual(len(FOUR_CONDITIONS), 4)
        for one in ("anādeśādi", "ekahal-madhya", "liṭi"):
            self.assertIn(one, FOUR_CONDITIONS, one)

    def test_and_three_of_them_have_a_counter_example(self):
        row, = provisions_for("6.4.120")
        for form in ("दिदिवतुः", "ररासे", "शश्रमिथ"):
            self.assertIn(form, row.keeps_out, form)

    def test_the_fourth_is_the_affix_itself(self):
        row, = provisions_for("6.4.120")
        self.assertEqual(row.before, ("liṭ",))

    def test_and_each_of_the_three_is_in_the_excludes(self):
        row, = provisions_for("6.4.120")
        for one in ("ādeś-ādi", "anekahal-madhya", "dīrgha"):
            self.assertIn(one, row.excludes, one)
        for one in row.excludes:
            self.assertEqual(
                in_the_perfect(before="liṭ", result=one).sutra,
                "", one)


class FourRootsNamedForThreeDifferentReasons(unittest.TestCase):
    """
    **तरतेर् गुणार्थं वचनम्। फलिभजोर् आदेशाद्यर्थम्। त्रपेर्
    अनेकहल्मध्यार्थम्** — तॄ for a guṇa, फल् and भज् for beginning
    with a substitute, त्रप् for having two consonants. The
    reasons are the content of the sūtra, not decoration on it.
    """

    def test_the_four_and_their_reasons_are_recorded(self):
        self.assertEqual(len(WHY_FOUR_MORE), 4)
        reasons = {reason for _, reason in WHY_FOUR_MORE}
        self.assertEqual(reasons, {"guṇa", "ādeś-ādi",
                                   "anekahal-madhya"})

    def test_and_two_of_them_share_a_reason(self):
        sharing = [root for root, reason in WHY_FOUR_MORE
                   if reason == "ādeś-ādi"]
        self.assertEqual(sharing, ["phal", "bhaj"])

    def test_the_note_gives_all_three_reasons(self):
        row, = provisions_for("6.4.122")
        for cited in ("गुणार्थं", "आदेशाद्यर्थम्",
                      "अनेकहल्मध्यार्थम्"):
            self.assertIn(cited, row.why, cited)

    def test_and_each_reason_is_a_condition_6_4_120_would_fail(
            self):
        wider, = provisions_for("6.4.120")
        for _, reason in WHY_FOUR_MORE:
            if reason == "guṇa":
                continue
            self.assertIn(reason, wider.excludes, reason)

    def test_so_the_rule_has_to_name_what_it_displaces(self):
        row, = provisions_for("6.4.122")
        self.assertEqual(row.blocks, ("6.4.120", "6.4.121"))
        for root, _ in WHY_FOUR_MORE:
            got = in_the_perfect(root, before="liṭ", result="kṅit")
            self.assertEqual(got.sutra, "6.4.122", root)


class AndOneRootSetsAsideACarriedCondition(unittest.TestCase):
    """
    6.4.123 राधो हिंसायाम् takes राध्, which has a long आ and no
    short one — **अत इत्येतद् इहोपस्थितं तपरत्वकृतम् अपास्य
    कालविशेषम् असंभवाद् अवर्णमात्रं प्रतिपादयति**. The tapara that
    6.4.120 carried has to be dropped or the rule reaches nothing.
    """

    def test_the_note_says_the_tapara_is_set_aside(self):
        row, = provisions_for("6.4.123")
        self.assertIn("तपरत्वकृतम्", row.why)
        self.assertIn("असंभवाद्", row.why)

    def test_and_the_sense_is_the_whole_of_the_condition(self):
        row, = provisions_for("6.4.123")
        self.assertEqual(row.result, ("hiṃsā",))
        self.assertIn("रराधतुः", row.keeps_out)

    def test_it_answers_where_the_sense_is_given(self):
        got = in_the_perfect("rādh", before="liṭ", result="hiṃsā")
        self.assertEqual(got.sutra, "6.4.123")

    def test_and_not_where_it_is_not(self):
        self.assertEqual(
            in_the_perfect("rādh", before="liṭ").sutra, "")


class NineMoreTakeItOptionallyAndFourClassesNotAtAll(
        unittest.TestCase):
    def test_three_and_seven_take_it_optionally(self):
        self.assertEqual(len(OPTIONAL_THREE), 3)
        self.assertEqual(len(PHANADI), 7)
        for root in OPTIONAL_THREE:
            got = in_the_perfect(root, before="liṭ")
            self.assertEqual(got.sutra, "6.4.124", root)
            self.assertTrue(got.optional, root)
        got = in_the_perfect(gana="phaṇādi", before="liṭ")
        self.assertEqual(got.sutra, "6.4.125")
        self.assertTrue(got.optional)

    def test_and_four_classes_are_refused(self):
        self.assertEqual(len(NO_ETVA), 4)
        row, = provisions_for("6.4.126")
        self.assertTrue(row.refuses)
        self.assertEqual(row.blocks, ("6.4.120", "6.4.121"))

    def test_the_refusal_answers_with_nothing(self):
        for stem in ("śas", "dad"):
            got = in_the_perfect(stem, before="liṭ")
            self.assertEqual((got.sutra, got.does),
                             ("6.4.126", ""), stem)

    def test_and_the_last_of_the_four_is_not_a_class_of_roots(self):
        """An अ that GUṆA made, which is a fact about the vowel
        and not about the root it sits in."""
        self.assertIn("guṇa", NO_ETVA)
        row, = provisions_for("6.4.126")
        self.assertIn("विशशरतुः", row.why)


class TwoStemsAtTheEndAndOneOfThemVaries(unittest.TestCase):
    """
    6.4.127 and 6.4.128 leave the perfect behind: both make an
    न्-final stem into a त्-final one, and the second says
    बहुलम् — every form given twice over.
    """

    def test_both_give_the_same_substitute(self):
        for code in ("6.4.127", "6.4.128"):
            row, = provisions_for(code)
            self.assertEqual(row.does, "tṛ", code)

    def test_the_first_has_two_conditions_facing_opposite_ways(
            self):
        """**असौ** is about what FOLLOWS and **अनञः** about what
        PRECEDES, in one compound."""
        row, = provisions_for("6.4.127")
        self.assertEqual(row.excludes, ("su", "nañ"))
        self.assertIn("अर्वा", row.keeps_out)
        self.assertIn("अनर्वाणौ", row.keeps_out)

    def test_and_the_second_is_bahulam_and_not_optional(self):
        row, = provisions_for("6.4.128")
        self.assertTrue(row.bahulam)
        self.assertFalse(row.optional)
        got = in_the_perfect("maghavan")
        self.assertEqual(got.sutra, "6.4.128")
        self.assertTrue(got.bahulam)

    def test_and_its_note_gives_every_form_twice(self):
        row, = provisions_for("6.4.128")
        self.assertIn("न च भवति", row.why)
        for form in ("मघवान्", "मघवा", "मघोनः"):
            self.assertIn(form, row.why, form)


class OneRootIsWorkedOverFourTimes(unittest.TestCase):
    """
    जहाति takes इ before a consonant (6.4.116), आ before हि
    (6.4.117), and nothing at all before a य् (6.4.118) — three
    different things in three consecutive sūtras, and 6.4.116 was
    split off from 6.4.115 to make it possible.
    """

    def test_three_rules_name_it_and_do_three_things(self):
        got = {row.sutra: row.does for row in ETVA_TABLE
               if row.of == ("hā",)}
        self.assertEqual(got, {"6.4.116": "it", "6.4.117": "ā",
                               "6.4.118": "lopa"})

    def test_and_the_first_says_why_it_stands_alone(self):
        row, = provisions_for("6.4.116")
        self.assertIn("पृथग्योगकरणम्", row.why)
        self.assertIn("उत्तरार्थम्", row.why)

    def test_each_is_told_apart_by_what_follows(self):
        for query, code in (
                ({"before": "sārvadhātuka", "result": "hal-ādi"},
                 "6.4.116"),
                ({"before": "hi"}, "6.4.117"),
                ({"before": "sārvadhātuka", "result": "ya-ādi"},
                 "6.4.118")):
            got = in_the_perfect("hā", **query)
            self.assertEqual(got.sutra, code, query)

    def test_and_the_rule_it_was_split_from_names_another_root(
            self):
        earlier, = provisions_for("6.4.115")
        self.assertEqual(earlier.of, ("bhī",))
        self.assertTrue(earlier.optional)


class WantsFiltersByTheOperation(unittest.TestCase):
    def test_asking_for_the_one_it_does(self):
        self.assertEqual(
            in_the_perfect(before="liṭ", result="kṅit",
                           wants="et-abhyāsalopa").sutra, "6.4.120")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            in_the_perfect(before="liṭ", result="kṅit",
                           wants="lopa").sutra, "")

    def test_a_refusal_supplies_nothing_to_ask_for(self):
        self.assertEqual(
            in_the_perfect("śas", before="liṭ",
                           wants="et-abhyāsalopa").sutra, "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in ETVA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in ETVA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.4.129 भस्य opens the pāda's
    last heading — **आ अध्यायपरिसमाप्तेः**, to 6.4.175 — and
    every one of those forty-seven sūtras is ahead.
    """

    def test_the_last_heading_of_the_pada_picks_up_where_this_stops(self):
        # This was written as a debt: 6.4.129 भस्य was ahead. It
        # has landed, and the claim is now the live join — the
        # heading opens on the sūtra after this run's last, and
        # runs to 6.4.175, which has landed too.
        self.assertTrue(REGISTRY.has("6.4.129"))
        self.assertEqual(_n("6.4.129")[2],
                         _n(ABHYASA_RUN[1])[2] + 1)

    def test_and_the_pada_is_complete(self):
        self.assertTrue(REGISTRY.has("6.4.175"))
        self.assertFalse(REGISTRY.has("6.4.176"))

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 129):
            self.assertTrue(REGISTRY.has("6.4.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
