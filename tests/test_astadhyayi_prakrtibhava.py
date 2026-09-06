# -*- coding: utf-8 -*-
"""
Tests for 6.1.115–134 — where a junction is held open.

Three things here are new.

**Four ācāryas are named, and three of the four names do nothing.**
The vṛtti says so each time: आपिशलिग्रहणं पूजार्थम्, स्फोटायनग्रहणं
पूजार्थम्, शाकल्यस्य ग्रहणं पूजार्थम् — the वा already made each rule
optional. And then चाक्रवर्मणग्रहणं विकल्पार्थम्, where the name IS
the option. The distinction is invisible from the sūtras and has to
be carried from the commentary.

**A condition can fail because a corpus has no such thing.** 6.1.115
wants a position inside a verse-foot, and the Yajurveda has none:
यजुषि पादानामभावाद् अनन्तःपादार्थं वचनम्. Five rules are stated over
again for prose for no other reason.

**And पाद is read two ways in one pāda.** 6.1.115 takes it as a Vedic
foot and NOT a śloka's; 6.1.134's vṛtti reports that some take it as
a śloka's too, and quotes a verse.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.prakrtibhava import (
    AVYADI, PRAKRTIBHAVA_TABLE, TEACHERS, YAJUSI_WORDS, named_teachers,
    provisions_for, stands_open)
from src.astadhyayi.sutra import REGISTRY


class FourAcaryasAndOnlyOneOfTheNamesDoesAnything(unittest.TestCase):
    def test_there_are_four_of_them_across_the_pada(self):
        self.assertEqual(len(TEACHERS), 4)
        self.assertEqual(named_teachers(), TEACHERS)

    def test_three_names_are_recorded_as_honour(self):
        honour = [name for name, _sutra, why in TEACHERS
                  if "पूजार्थम्" in why]
        self.assertEqual(honour,
                         ["Āpiśali", "Sphoṭāyana", "Śākalya"])

    def test_and_the_fourth_is_recorded_as_making_the_option(self):
        force = [(name, sutra) for name, sutra, why in TEACHERS
                 if "विकल्पार्थम्" in why]
        self.assertEqual(force, [("Cākravarmaṇa", "6.1.130")])

    def test_the_note_on_each_says_which_it_is(self):
        for code in ("6.1.123", "6.1.127"):
            self.assertIn("पूजार्थम्", provisions_for(code)[0].why, code)
        self.assertIn("विकल्पार्थम्",
                      provisions_for("6.1.130")[0].why)

    def test_every_named_rule_is_optional_whatever_the_name_does(self):
        """
        The distinction is about WHY each is optional, not whether.
        All four are.
        """
        for row in PRAKRTIBHAVA_TABLE:
            if row.teacher:
                self.assertTrue(row.optional, row.sutra)

    def test_a_teachers_rule_is_out_of_reach_until_he_is_named(self):
        self.assertEqual(stands_open("go", before="ac").sutra, "")
        self.assertEqual(
            stands_open("go", before="ac", teacher="Sphoṭāyana").sutra,
            "6.1.123")

    def test_and_naming_the_wrong_teacher_reaches_nothing(self):
        self.assertEqual(
            stands_open("go", before="ac", teacher="Śākalya").sutra, "")


class ACorpusWithoutVerseFeetNeedsItsOwnRules(unittest.TestCase):
    """
    6.1.115 turns on a POSITION, and the Yajurveda has no positions of
    that kind. Five rules are restated for it, and the flag has to be
    separate from the general Vedic one or the distinction vanishes.
    """

    def test_the_general_vedic_rule_wants_a_position(self):
        row = provisions_for("6.1.115")[0]
        self.assertEqual(row.result, "antaḥpāda")
        self.assertTrue(row.chandasi)
        self.assertFalse(row.yajusi)

    def test_the_yajurveda_rules_want_no_position_at_all(self):
        yajusi = [r for r in PRAKRTIBHAVA_TABLE if r.yajusi]
        self.assertEqual([r.sutra for r in yajusi],
                         ["6.1.117", "6.1.118", "6.1.119", "6.1.120",
                          "6.1.121"])
        for row in yajusi:
            self.assertEqual(row.result, "", row.sutra)
            self.assertFalse(row.chandasi, row.sutra)

    def test_the_note_says_why_they_had_to_be_restated(self):
        self.assertIn("पादानामभावाद्", provisions_for("6.1.117")[0].why)

    def test_naming_the_general_corpus_does_not_reach_them(self):
        self.assertEqual(
            stands_open("uras", before="at", chandasi=True).sutra, "")

    def test_but_naming_that_corpus_does(self):
        self.assertEqual(
            stands_open("uras", before="at", yajusi=True).sutra,
            "6.1.117")

    def test_the_list_it_carries_is_six_words(self):
        self.assertEqual(len(YAJUSI_WORDS), 6)
        for word in YAJUSI_WORDS:
            self.assertEqual(
                stands_open(word, before="at", yajusi=True).sutra,
                "6.1.118", word)


class ASevenWordListDefeatsOneWordOfTheRuleBefore(unittest.TestCase):
    """
    6.1.115 refuses where a व् or य् follows the अ. 6.1.116 lists
    seven words that hold the junction open anyway — and every one of
    them has exactly that व् or य्. A list stated for no other reason.
    """

    def test_there_are_seven(self):
        self.assertEqual(len(AVYADI), 7)

    def test_it_names_the_rule_it_defeats(self):
        row = provisions_for("6.1.116")[0]
        self.assertEqual(row.blocks, ("6.1.115",))
        self.assertNotIn(row.sutra, row.blocks)

    def test_both_rules_want_the_same_position(self):
        self.assertEqual(provisions_for("6.1.115")[0].result,
                         provisions_for("6.1.116")[0].result)

    def test_and_the_list_is_what_tells_them_apart(self):
        self.assertEqual(
            stands_open(after="eṅ", before="avyādi",
                        result="antaḥpāda", chandasi=True).sutra,
            "6.1.116")
        self.assertEqual(
            stands_open(after="eṅ", before="at", result="antaḥpāda",
                        chandasi=True).sutra, "6.1.115")

    def test_the_note_records_the_reading_the_vrtti_declines(self):
        """
        Some read the rule with a न् and make it refuse everything
        6.1.72 opened. The Kāśikā reports that without adopting it,
        and a note that dropped it would lose a whole alternative
        grammar of the pāda.
        """
        why = provisions_for("6.1.115")[0].why
        self.assertIn("केचिदिदं सूत्रं", why)
        self.assertIn("सर्वस्य प्रतिषेधं", why)


class PadaIsReadTwoWaysInOnePada(unittest.TestCase):
    def test_the_first_rule_takes_it_as_a_vedic_foot_only(self):
        self.assertIn("न तु श्लोकपादस्य",
                      provisions_for("6.1.115")[0].why)

    def test_and_the_last_reports_the_other_reading(self):
        self.assertIn("श्लोकपादस्यापि",
                      provisions_for("6.1.134")[0].why)

    def test_both_rules_turn_on_the_word(self):
        self.assertEqual(provisions_for("6.1.115")[0].result,
                         "antaḥpāda")
        self.assertEqual(provisions_for("6.1.134")[0].result,
                         "pādapūraṇa")


class TwoRulesPutSomethingInInsteadOfHoldingTheGapOpen(unittest.TestCase):
    """
    6.1.123 and 6.1.124 are the odd pair: they stand among rules that
    say nothing happens, and they substitute अवङ्. One is a choice and
    one is not, and नित्यम् is what separates them.
    """

    def test_they_are_the_only_two_that_substitute(self):
        substituting = [r.sutra for r in PRAKRTIBHAVA_TABLE
                        if r.does == "avaṅ"]
        self.assertEqual(substituting, ["6.1.123", "6.1.124"])

    def test_one_is_a_choice_and_the_other_is_not(self):
        self.assertTrue(
            stands_open("go", before="ac",
                        teacher="Sphoṭāyana").optional)
        self.assertFalse(stands_open("go", before="indra").optional)

    def test_the_fixed_one_names_the_optional_one(self):
        row = provisions_for("6.1.124")[0]
        self.assertEqual(row.blocks, ("6.1.123",))
        self.assertIn("नित्यम्", row.why)

    def test_the_optional_one_is_settled_where_it_matters(self):
        row = provisions_for("6.1.123")[0]
        self.assertTrue(row.vyavasthita)
        self.assertIn("गवाक्ष", row.why)

    def test_and_the_rule_before_them_holds_the_gap_open_instead(self):
        answer = stands_open("go", before="at")
        self.assertEqual(answer.sutra, "6.1.122")
        self.assertEqual(answer.does, "prakṛtibhāva")
        self.assertTrue(answer.optional)


class ThePlutaRulesUndoOneAnother(unittest.TestCase):
    """
    6.1.125 holds a प्लुत open; 6.1.129 says it is treated like a
    non-प्लुत before the इति of a पदपाठ, so the junction closes;
    6.1.130 makes THAT a choice. Three rules deep, and the third is
    an उभयत्रविभाषा working in both directions at once.
    """

    def test_the_first_holds_it_open(self):
        answer = stands_open(after="pluta-pragṛhya", before="ac")
        self.assertEqual(answer.sutra, "6.1.125")
        self.assertEqual(answer.does, "prakṛtibhāva")

    def test_the_second_closes_it_and_names_the_first(self):
        answer = stands_open(after="pluta", before="upasthita")
        self.assertEqual(answer.sutra, "6.1.129")
        self.assertEqual(answer.does, "aplutavat")
        self.assertEqual(answer.blocked_by, ("6.1.125",))

    def test_the_third_is_reached_only_by_naming_its_teacher(self):
        self.assertEqual(stands_open(after="ī3", before="ac").sutra, "")
        answer = stands_open(after="ī3", before="ac",
                             teacher="Cākravarmaṇa")
        self.assertEqual(answer.sutra, "6.1.130")
        self.assertTrue(answer.optional)

    def test_the_note_says_it_works_in_both_directions(self):
        why = provisions_for("6.1.130")[0].why
        self.assertIn("निवृत्त्यर्थम्", why)
        self.assertIn("प्राप्त्यर्थम्", why)

    def test_and_the_second_says_why_it_is_vat_and_not_a_change(self):
        self.assertIn("वत्करणं किम्",
                      provisions_for("6.1.129")[0].why)


class TheThreeLopaRulesAreDistinct(unittest.TestCase):
    def test_they_are_the_three_expected(self):
        dropping = [r.sutra for r in PRAKRTIBHAVA_TABLE
                    if r.does == "su-lopa"]
        self.assertEqual(dropping, ["6.1.132", "6.1.133", "6.1.134"])

    def test_the_first_holds_in_ordinary_speech(self):
        answer = stands_open("etad", before="hal")
        self.assertEqual(answer.sutra, "6.1.132")
        self.assertFalse(answer.chandasi)

    def test_the_other_two_need_the_corpus(self):
        for stem, before in (("sya", "hal"), ("sa", "ac")):
            self.assertEqual(stands_open(stem, before=before).sutra, "",
                             stem)

    def test_and_the_last_needs_a_metrical_condition_besides(self):
        self.assertEqual(
            stands_open("sa", before="ac", chandasi=True).sutra, "")
        self.assertEqual(
            stands_open("sa", before="ac", result="pādapūraṇa",
                        chandasi=True).sutra, "6.1.134")

    def test_the_first_records_the_maxim_that_forced_one_of_its_words(self):
        """
        तन्मध्यपतितस्तद्ग्रहणेन गृह्यते — एषक would count as एतद्
        despite the क, so अकोः has to be stated to keep it out.
        """
        why = provisions_for("6.1.132")[0].why
        self.assertIn("तन्मध्यपतित", why)
        self.assertIn("एषको ददाति", why)


class TheSectionIsWhereItSaysItIs(unittest.TestCase):
    def test_the_rows_are_the_twenty(self):
        held = sorted(r.sutra for r in PRAKRTIBHAVA_TABLE)
        self.assertEqual(held,
                         sorted("6.1.%d" % n for n in range(115, 135)))

    def test_every_rule_here_is_registered_against_this_resolver(self):
        for row in PRAKRTIBHAVA_TABLE:
            self.assertEqual(REGISTRY.get(row.sutra).apply.__name__,
                             "stands_open", row.sutra)

    def test_the_pada_is_contiguous_through_it(self):
        for n in range(1, 135):
            self.assertTrue(REGISTRY.has("6.1.%d" % n), n)

    def test_no_row_names_itself_on_what_it_displaces(self):
        for row in PRAKRTIBHAVA_TABLE:
            self.assertNotIn(row.sutra, row.blocks, row.sutra)


class NothingAnswersByDefault(unittest.TestCase):
    def test_an_unreached_question_gets_nothing(self):
        answer = stands_open(after="hal", before="hal")
        self.assertEqual(answer.sutra, "")
        self.assertEqual(answer.does, "")

    def test_and_the_message_says_the_ordinary_rules_take_it(self):
        self.assertIn("6.1.72", stands_open(after="hal",
                                            before="hal").why)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in PRAKRTIBHAVA_TABLE:
            self.assertGreater(len(row.why), 120, row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in PRAKRTIBHAVA_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_accent_section_landed_and_bounds_the_heading(self):
        """
        6.1.158 अनुदात्तं पदमेकवर्जम् is codified now — the debt this
        test was written as, paid — and with it the whole run to
        6.1.223. Its words are what bound 6.1.72's संहिता, so the
        heading this table is read under now has a codified bound at
        both ends.
        """
        from src.astadhyayi.samhita import SAMHITA_MARKER, SAMHITA_RUN

        self.assertTrue(REGISTRY.has("6.1.158"))
        self.assertTrue(REGISTRY.has("6.1.223"))
        self.assertEqual(SAMHITA_MARKER, "6.1.158")
        self.assertTrue(REGISTRY.has(SAMHITA_RUN[0]))
        self.assertTrue(REGISTRY.has(SAMHITA_RUN[1]))

    def test_the_sut_run_this_section_stops_before_landed(self):
        """
        6.1.135 सुट् कात् पूर्वः is codified now, in `sut` — the
        debt this test was written as, paid. The boundary is what
        has to keep holding: this table stops at 6.1.134.
        """
        self.assertTrue(REGISTRY.has("6.1.135"))
        self.assertEqual(provisions_for("6.1.135"), ())
        self.assertEqual(REGISTRY.get("6.1.135").apply.__module__,
                         "src.astadhyayi.sut")

    def test_both_of_the_rules_these_notes_lean_on_have_landed(self):
        """
        Written as the exact shortfall, when neither was codified.
        7.3.107 अम्बार्थनद्योर्ह्रस्वः — which shortens the very
        vocatives 6.1.118 lists — landed with पाद ७.३, and 8.1.30,
        which gives अवपथाः its accent back at 6.1.121, with
        पाद ८.१. Both halves can be asked of the engine now, and
        each note still has to name the rule it leans on.
        """
        self.assertTrue(REGISTRY.has("7.3.107"))
        self.assertTrue(REGISTRY.has("8.1.30"))
        self.assertIn("7.3.107", provisions_for("6.1.118")[0].why)
        self.assertIn("8.1.30", provisions_for("6.1.121")[0].why)


if __name__ == "__main__":
    unittest.main()
