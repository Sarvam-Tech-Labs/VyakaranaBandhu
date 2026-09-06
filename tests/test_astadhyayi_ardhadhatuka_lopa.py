# -*- coding: utf-8 -*-
"""
६.४.४६–७० — आर्धधातुके, and what the stem loses before it.

A heading inside a heading, and the thing to hold the table to is
that both are read off the vṛttis: अङ्गस्य runs on from 6.4.1 to
the end of adhyāya 7, and आर्धधातुके runs twenty-three sūtras
because 6.4.69 न ल्यपि is where it stops.

After that, three arguments:

**One sūtra that both refuses and bounds.** 6.4.69 is the
heading's stated bound AND a प्रतिषेध of two rules inside it.

**A word said in one shape for the next rule's sake.**
**नेति वक्तव्येऽयादेशवचनमुत्तरार्थम्** — 6.4.55 could have said
*not* and says अय् so that 6.4.56 has something to carry.

**And a case where 6.4.22's असिद्धत्व does NOT reach.**
**असमानाश्रयत्वात्** — the two operations rest on different
things, which is exactly what 6.4.22's अत्र was for.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.anunasika_lopa import NASAL_RUN
from src.astadhyayi.ardhadhatuka_lopa import (
    ARDHADHATUKA_RUN, AY_BEFORE, CINVAT_FOUR, CINVAT_ROOTS,
    GHU_SEVEN, LOPA_RUN, LOSS_TABLE, before_ardhadhatuka,
    provisions_for)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class AHeadingInsideAHeading(unittest.TestCase):
    """
    **आर्धधातुक इत्यधिकारः। न ल्यपि इति प्राग् एतस्मात्** — and
    6.4.1's अङ्गस्य is still running under it, to the end of
    adhyāya 7. Two headings at once, one twenty-three sūtras long
    and one six hundred and thirteen.
    """

    def test_the_inner_heading_stops_where_the_vrtti_says(self):
        self.assertEqual(ARDHADHATUKA_RUN, ("6.4.46", "6.4.68"))
        self.assertEqual(_n("6.4.69")[2],
                         _n(ARDHADHATUKA_RUN[1])[2] + 1)

    def test_and_the_outer_one_is_still_running_under_it(self):
        from src.astadhyayi.anga_dirgha import ANGA_RUN

        self.assertLessEqual(_n(ANGA_RUN[0]),
                             _n(ARDHADHATUKA_RUN[0]))
        self.assertLess(_n(ARDHADHATUKA_RUN[1]), _n(ANGA_RUN[1]))

    def test_this_module_runs_two_sutras_past_the_inner_one(self):
        """6.4.69 ends the heading and 6.4.70 is about the same
        affix, so both belong with the run they close."""
        self.assertEqual(LOPA_RUN[0], ARDHADHATUKA_RUN[0])
        self.assertEqual(LOPA_RUN[1], "6.4.70")

    def test_it_opens_one_sutra_after_the_nasal_run(self):
        self.assertEqual(_n(LOPA_RUN[0])[2], _n(NASAL_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_46_to_70(self):
        got = [row.sutra for row in LOSS_TABLE]
        self.assertEqual(got, ["6.4.%d" % n for n in range(46, 71)])

    def test_every_row_carries_its_reason(self):
        for row in LOSS_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)


class TheHeadingConfersNothing(unittest.TestCase):
    def test_it_never_answers(self):
        row, = provisions_for("6.4.46")
        self.assertTrue(row.heading)
        self.assertEqual(row.does, "")
        self.assertNotEqual(
            before_ardhadhatuka(gana="a-anta").sutra, "6.4.46")

    def test_and_the_rule_it_reads_out_does(self):
        got = before_ardhadhatuka(gana="a-anta")
        self.assertEqual((got.sutra, got.does), ("6.4.48", "lopa"))

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = before_ardhadhatuka("bhū", before="śap")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("stands as it is", got.why)


class OneSutraBothRefusesAndBounds(unittest.TestCase):
    """
    6.4.69 न ल्यपि is the heading's stated bound and a प्रतिषेध
    of 6.4.66 and 6.4.67. Recording only one of the two would lose
    half the sūtra.
    """

    def test_it_is_the_only_refusal_of_the_run(self):
        refusing = {row.sutra for row in LOSS_TABLE if row.refuses}
        self.assertEqual(refusing, {"6.4.69"})

    def test_it_names_the_two_rules_it_refuses(self):
        row, = provisions_for("6.4.69")
        self.assertEqual(row.blocks, ("6.4.66", "6.4.67"))
        for code in row.blocks:
            self.assertTrue(
                _n(code) < _n(row.sutra)
                <= _n(ARDHADHATUKA_RUN[1])[:2] + (
                    _n(ARDHADHATUKA_RUN[1])[2] + 1,), code)

    def test_and_it_is_the_bound_the_heading_was_read_against(self):
        self.assertEqual(_n(ARDHADHATUKA_RUN[1])[2] + 1,
                         _n("6.4.69")[2])
        heading, = provisions_for("6.4.46")
        self.assertIn("न ल्यपि", heading.why)

    def test_the_answer_supplies_nothing(self):
        got = before_ardhadhatuka("mā", gana="ghu", before="lyap")
        self.assertEqual((got.sutra, got.does), ("6.4.69", ""))
        self.assertEqual(got.blocked_by, ("6.4.66", "6.4.67"))

    def test_and_the_two_it_refuses_still_answer_elsewhere(self):
        self.assertEqual(
            before_ardhadhatuka("mā", gana="ghu", before="hal",
                                result="kṅit").sutra, "6.4.66")
        self.assertEqual(
            before_ardhadhatuka("mā", gana="ghu", before="liṅ",
                                result="kṅit").sutra, "6.4.67")


class AWordSaidInOneShapeForTheNextRulesSake(unittest.TestCase):
    """
    **नेति वक्तव्येऽयादेशवचनमुत्तरार्थम्** — 6.4.55 could have
    said *not*, since the णि simply staying gives the same forms.
    It says अय् so that 6.4.56 has a substitute to carry.
    """

    def test_the_note_says_so(self):
        row, = provisions_for("6.4.55")
        self.assertIn("नेति वक्तव्ये", row.why)
        self.assertIn("उत्तरार्थम्", row.why)

    def test_and_the_next_rule_does_carry_it(self):
        first, = provisions_for("6.4.55")
        second, = provisions_for("6.4.56")
        self.assertEqual(first.does, second.does)
        self.assertEqual(first.does, "ay")

    def test_six_affixes_take_the_first_one(self):
        self.assertEqual(len(AY_BEFORE), 6)
        for affix in AY_BEFORE:
            got = before_ardhadhatuka("ṇi", before=affix)
            self.assertEqual((got.sutra, got.does),
                             ("6.4.55", "ay"), affix)

    def test_and_a_third_rule_makes_it_optional(self):
        got = before_ardhadhatuka("ṇi", before="lyap",
                                  result="āp-pūrva")
        self.assertEqual(got.sutra, "6.4.57")
        self.assertTrue(got.optional)


class WhereTheAsiddhatvaDoesNotReach(unittest.TestCase):
    """
    6.4.22's असिद्धवत् is qualified by अत्र, and the vṛtti of
    6.4.56 shows what that word is worth: **ह्रस्वयलोपाल्लोपानाम्
    असिद्धत्वं न भवति असमानाश्रयत्वात्** — the shortening and the
    two elisions rest on the णि, and this substitution rests on
    the ल्यप्.
    """

    def test_the_note_names_the_reason(self):
        row, = provisions_for("6.4.56")
        self.assertIn("असिद्धत्वं न भवति", row.why)
        self.assertIn("असमानाश्रयत्वात्", row.why)

    def test_and_the_heading_it_turns_on_is_codified(self):
        self.assertTrue(REGISTRY.has("6.4.22"))

    def test_and_that_headings_own_note_says_the_same(self):
        """6.4.22 was codified long before this module, and its
        note already carries **अत्रग्रहणं समानाश्रयत्व-
        प्रतिपत्त्यर्थम्** — so the two agree."""
        note = REGISTRY.get("6.4.22").notes
        self.assertIn("समानाश्रयत्व", note)


class TheCausalNiGoesTwoWaysAndStaysOnce(unittest.TestCase):
    """
    6.4.51 drops the णि before an इट्-less affix and 6.4.52 before
    a सेट् निष्ठा, so between them only कारयिता is left standing.
    And 6.4.52's सेट् is what shows 6.4.51 does not reach
    संज्ञपितः either.
    """

    def test_it_goes_without_the_it(self):
        got = before_ardhadhatuka("ṇi")
        self.assertEqual((got.sutra, got.does), ("6.4.51", "lopa"))

    def test_and_with_one_in_a_nistha(self):
        got = before_ardhadhatuka("ṇi", before="niṣṭhā",
                                  result="seṭ")
        self.assertEqual((got.sutra, got.does), ("6.4.52", "lopa"))

    def test_and_the_second_says_what_saying_set_is_worth(self):
        row, = provisions_for("6.4.52")
        self.assertIn("सेड्ग्रहणसामर्थ्याद्", row.why)

    def test_two_more_forms_are_laid_down_whole(self):
        nipatana = {row.sutra for row in LOSS_TABLE if row.nipatana}
        self.assertEqual(nipatana, {"6.4.53", "6.4.54"})
        for code, register in (("6.4.53", "mantra"),
                               ("6.4.54", "yajña")):
            got = before_ardhadhatuka("ṇi", before="tṛc",
                                      result=register)
            self.assertEqual(got.sutra, code, register)
            self.assertTrue(got.nipatana, register)

    def test_and_neither_could_have_been_reached_by_rule(self):
        """The affix has an इट् and is no निष्ठा, so 6.4.51 and
        6.4.52 both fail — which is why they are निपातन."""
        row, = provisions_for("6.4.53")
        self.assertIn("6.4.51", row.why)
        self.assertIn("6.4.52", row.why)


class ARuleThatUndoesAnotherOutranksIt(unittest.TestCase):
    """
    6.4.60 lengthens क्षि in a निष्ठा and 6.4.61 makes it optional
    where abuse or misery is meant. Both reach the same root
    before the same affix, so only `blocks` can order them.
    """

    def test_the_plain_case_is_compulsory(self):
        got = before_ardhadhatuka("kṣi", before="niṣṭhā")
        self.assertEqual(got.sutra, "6.4.60")
        self.assertFalse(got.optional)

    def test_and_the_sense_makes_it_optional(self):
        for sense in ("ākrośa", "dainya"):
            got = before_ardhadhatuka("kṣi", before="niṣṭhā",
                                      result=sense)
            self.assertEqual(got.sutra, "6.4.61", sense)
            self.assertTrue(got.optional, sense)

    def test_and_the_later_one_names_what_it_displaces(self):
        row, = provisions_for("6.4.61")
        self.assertEqual(row.blocks, ("6.4.60",))


class TheLongestSutraOfThePada(unittest.TestCase):
    """
    6.4.62 makes four affixes behave AS THOUGH चिण् were there and
    takes an इट् with it. What the record has to keep is that the
    इट् goes to the AFFIXES and not to the stem, and that the
    vṛtti's own list of प्रयोजनानि is not modelled.
    """

    def test_it_names_four_affixes_and_three_roots(self):
        self.assertEqual(len(CINVAT_FOUR), 4)
        self.assertEqual(CINVAT_ROOTS, ("han", "grah", "dṛś"))
        row, = provisions_for("6.4.62")
        self.assertEqual(row.before, CINVAT_FOUR)
        self.assertEqual(row.of, CINVAT_ROOTS)

    def test_and_a_class_beside_them(self):
        row, = provisions_for("6.4.62")
        self.assertEqual(row.gana, "ac-anta")

    def test_what_it_does_is_a_likeness_and_not_a_substitute(self):
        got = before_ardhadhatuka(gana="ac-anta", before="sya",
                                  result="bhāva")
        self.assertEqual((got.sutra, got.does),
                         ("6.4.62", "ciṇvat"))
        self.assertTrue(got.optional)

    def test_the_note_says_which_thing_takes_the_it(self):
        row, = provisions_for("6.4.62")
        self.assertIn("अङ्गस्य तु लक्ष्यविरोधाद् न क्रियते", row.why)

    def test_and_says_plainly_what_is_not_modelled(self):
        row, = provisions_for("6.4.62")
        self.assertIn("SCOPE", row.why)
        self.assertIn("प्रयोजनानि", row.why)


class TheSevenThatTakeIAndE(unittest.TestCase):
    def test_the_list_is_the_ghu_class_and_six_roots(self):
        self.assertEqual(len(GHU_SEVEN), 7)
        self.assertEqual(GHU_SEVEN[0], "ghu")

    def test_the_same_seven_are_named_by_three_rules(self):
        for code in ("6.4.66", "6.4.67", "6.4.69"):
            row, = provisions_for(code)
            self.assertEqual(row.of, GHU_SEVEN[1:], code)
            self.assertEqual(row.gana, "ghu", code)

    def test_and_the_fourth_rule_names_everyone_else(self):
        row, = provisions_for("6.4.68")
        self.assertEqual(row.excludes, GHU_SEVEN)
        self.assertTrue(row.optional)

    def test_so_one_of_the_seven_is_compulsory_where_others_are_not(
            self):
        firm = before_ardhadhatuka("sthā", gana="ghu",
                                   before="liṅ", result="kṅit")
        self.assertEqual(firm.sutra, "6.4.67")
        self.assertFalse(firm.optional)
        loose = before_ardhadhatuka(gana="ā-anta-saṃyoga-ādi",
                                    before="liṅ", result="kṅit")
        self.assertEqual(loose.sutra, "6.4.68")
        self.assertTrue(loose.optional)


class WantsFiltersByTheOperation(unittest.TestCase):
    def test_asking_for_the_one_it_does(self):
        self.assertEqual(
            before_ardhadhatuka("ṇi", wants="lopa").sutra, "6.4.51")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            before_ardhadhatuka("ṇi", wants="ay").sutra, "")

    def test_a_refusal_supplies_nothing_to_ask_for(self):
        self.assertEqual(
            before_ardhadhatuka("mā", gana="ghu", before="lyap",
                                wants="īt").sutra, "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in LOSS_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in LOSS_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.4.71 लुङ्लङ्लृङ्क्ष्वडुदात्तः
    opens the augment run, and everything from there to 6.4.175 is
    ahead of it, 6.4.77 excepted.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.4.71 opens the augment run. The debt is collected, and
        the claim is the join: it starts one sūtra past this run
        and it ADDS something where this run takes things away.
        """
        from src.astadhyayi.anga_agama import augment_or_yan

        self.assertTrue(REGISTRY.has("6.4.71"))
        self.assertEqual(_n("6.4.71")[2], _n(LOPA_RUN[1])[2] + 1)
        self.assertEqual(augment_or_yan(before="luṅ").does, "aṭ")
        self.assertEqual(
            {row.does for row in LOSS_TABLE} & {"aṭ", "āṭ"}, set())

    def test_and_the_pada_is_complete_now(self):
        # Written as a debt while 6.4.175 was far off; the pāda
        # has been read through, so the claim is the live one.
        self.assertTrue(REGISTRY.has("6.4.175"))
        self.assertFalse(REGISTRY.has("6.4.176"))

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 71):
            self.assertTrue(REGISTRY.has("6.4.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
