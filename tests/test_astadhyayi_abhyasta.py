# -*- coding: utf-8 -*-
"""
Tests for 6.1.3–12 — the two names, the four triggers, two refusals.

Three things here are worth holding down. The section is SPLIT across
two modules on purpose: `dvirvacana` runs the reduplication and owns
6.1.1, 6.1.2 and 6.1.9, and this table states what the rules SAY. So
the first tests are that the split is clean and that neither module
claims the other's sūtras.

The second is 6.1.6, where the rule says six and the vṛtti names
seven. The project's standing practice is to record what the
commentary actually gives rather than smoothing the number away, and
that has to be visible from the code, not only from a note.

The third is 6.1.5's उभे — a word that adds nothing to the sense and
decides where an accent falls.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.abhyasta import (
    ABHYASTA_TABLE, JAKSHITYADI, NDRA, TRIGGERS, provisions_for,
    stated, triggers)
from src.astadhyayi.sutra import REGISTRY

#: The three the reduplication engine owns, and this table must not.
ENGINE_OWNS = ("6.1.1", "6.1.2", "6.1.9")


class TheSplitBetweenTheTwoModulesIsClean(unittest.TestCase):
    def test_this_table_holds_nine_of_the_ten(self):
        held = sorted(row.sutra for row in ABHYASTA_TABLE)
        self.assertEqual(
            held,
            ["6.1.10", "6.1.11", "6.1.12", "6.1.3", "6.1.4", "6.1.5",
             "6.1.6", "6.1.7", "6.1.8"])

    def test_and_states_nothing_the_engine_owns(self):
        for code in ENGINE_OWNS:
            self.assertEqual(provisions_for(code), (), code)

    def test_the_engine_still_serves_those_three(self):
        for code in ENGINE_OWNS:
            self.assertTrue(REGISTRY.has(code), code)
            served = REGISTRY.get(code).apply
            self.assertEqual(served.__module__,
                             "src.astadhyayi.dvirvacana", code)

    def test_and_this_table_serves_the_other_nine(self):
        for row in ABHYASTA_TABLE:
            served = REGISTRY.get(row.sutra).apply
            self.assertEqual(served.__name__, "stated", row.sutra)

    def test_the_ten_together_are_contiguous(self):
        for n in range(1, 13):
            self.assertTrue(REGISTRY.has("6.1.%d" % n), n)


class TheTwoNamesLandOnDifferentThings(unittest.TestCase):
    """
    6.1.4 names the first copy; 6.1.5 names the pair. Two rules, two
    parts, and every abhyāsa rule from 7.4.58 on depends on the
    difference.
    """

    def test_the_copy_alone_is_the_abhyasa(self):
        answer = stated(part="pūrva")
        self.assertEqual(answer.sutra, "6.1.4")
        self.assertEqual(answer.names, "abhyāsa")

    def test_the_two_together_are_the_abhyasta(self):
        answer = stated(part="ubhe")
        self.assertEqual(answer.sutra, "6.1.5")
        self.assertEqual(answer.names, "abhyasta")

    def test_neither_of_them_orders_an_operation(self):
        for part in ("pūrva", "ubhe"):
            self.assertEqual(stated(part=part).does, "", part)

    def test_a_part_neither_rule_names_reaches_neither(self):
        self.assertEqual(stated(part="uttara").sutra, "")

    def test_the_idle_word_that_decides_an_accent_is_recorded(self):
        """
        द्वे was already carrying into 6.1.5, so उभे adds nothing to
        the sense. What it adds is that the name belongs to the pair,
        which is why 6.1.189's उदात्त falls once.
        """
        why = provisions_for("6.1.5")[0].why
        self.assertIn("समुदायसंज्ञाप्रति", why)
        self.assertIn("6.1.189", why)


class TheRuleSaysSixAndTheVrttiNamesSeven(unittest.TestCase):
    """
    जक्षित्यादयः षट्. The Kāśikā bounds the run by its two ends —
    जक्ष to वेवीङ् — and then states the count that run gives:
    सप्तानां धातूनाम्. It does not reconcile them, and neither does
    this table.
    """

    def test_the_constant_holds_the_count_the_vrtti_gives(self):
        self.assertEqual(len(JAKSHITYADI), 7)

    def test_and_the_note_records_the_disagreement_rather_than_hiding_it(self):
        why = provisions_for("6.1.6")[0].why
        self.assertIn("सप्तानां धातूनाम्", why)
        self.assertIn("षट्", why)

    def test_every_one_of_the_seven_reaches_the_rule(self):
        for root in JAKSHITYADI:
            answer = stated(root)
            self.assertEqual(answer.sutra, "6.1.6", root)
            self.assertEqual(answer.names, "abhyasta", root)

    def test_the_name_is_given_with_no_doubling_ordered(self):
        self.assertEqual(stated("jakṣ").does, "")

    def test_a_root_outside_the_seven_gets_no_name(self):
        self.assertEqual(stated("pac").sutra, "")


class TheFourTriggersAreStatedHereAndOneIsNot(unittest.TestCase):
    """
    The debt written as the exact shortfall. सन् and यङ् are 6.1.9's
    and belong to `dvirvacana`; this table must NOT answer for them,
    and the day someone adds a row for them without moving the
    engine's registration this fails.
    """

    def test_three_of_the_triggers_answer_here(self):
        for affix, code in (("liṭ", "6.1.8"), ("ślu", "6.1.10"),
                            ("caṅ", "6.1.11")):
            answer = stated(before=affix)
            self.assertEqual(answer.sutra, code, affix)
            self.assertEqual(answer.does, "dvirvacana", affix)

    def test_but_the_two_the_engine_owns_do_not(self):
        for affix in ("san", "yaṅ"):
            self.assertEqual(stated(before=affix).sutra, "", affix)

    def test_the_list_still_names_all_five(self):
        """
        The section is not describable without them: अनभ्यासस्य
        carries from 6.1.8 through all four rules, and that one word
        is why जुगुप्सिषते does not double twice.
        """
        self.assertEqual(triggers(), TRIGGERS)
        self.assertEqual(set(TRIGGERS),
                         {"liṭ", "san", "yaṅ", "ślu", "caṅ"})

    def test_and_the_carried_word_is_recorded_where_it_is_stated(self):
        self.assertIn("अनभ्यासस्य", provisions_for("6.1.8")[0].why)

    def test_an_affix_no_rule_names_calls_for_nothing(self):
        self.assertEqual(stated(before="lyap").sutra, "")


class ARefusalNamesWhatItTakesTheFormFrom(unittest.TestCase):
    def setUp(self):
        self.refusing = [r for r in ABHYASTA_TABLE if r.refuses]

    def test_there_are_two_of_them(self):
        self.assertEqual([r.sutra for r in self.refusing],
                         ["6.1.3", "6.1.12"])

    def test_neither_names_itself(self):
        for row in self.refusing:
            self.assertNotIn(row.sutra, row.blocks, row.sutra)

    def test_each_names_a_codified_rule_that_comes_before_it(self):
        for row in self.refusing:
            self.assertTrue(row.blocks, row.sutra)
            for blocked in row.blocks:
                self.assertTrue(REGISTRY.has(blocked), blocked)
                self.assertLess(int(blocked.split(".")[2]),
                                int(row.sutra.split(".")[2]),
                                "%s names %s" % (row.sutra, blocked))

    def test_one_of_them_points_across_the_module_boundary(self):
        """
        6.1.3 refuses part of what 6.1.2 gives, and 6.1.2 is the
        engine's. A dependency that crosses two modules is exactly
        the one a table can record wrongly without noticing.
        """
        answer = stated(sound="n", at="saṃyogādi")
        self.assertEqual(answer.sutra, "6.1.3")
        self.assertEqual(answer.blocked_by, ("6.1.2",))
        self.assertEqual(REGISTRY.get("6.1.2").apply.__module__,
                         "src.astadhyayi.dvirvacana")

    def test_and_the_other_points_inside_this_table(self):
        answer = stated("dāś", before="kvasu")
        self.assertEqual(answer.sutra, "6.1.12")
        self.assertEqual(answer.blocked_by, ("6.1.8",))
        self.assertEqual(provisions_for("6.1.8")[0].does, "dvirvacana")

    def test_a_refusal_reports_no_operation(self):
        self.assertEqual(stated("dāś", before="kvasu").does, "")
        self.assertTrue(stated("dāś", before="kvasu").refuses)


class BothConditionsOfTheFirstRefusalHaveToHold(unittest.TestCase):
    """
    न्द्रा इति किम्? ईचिक्षिषते. संयोगादय इति किम्? प्राणिणिषति.
    The vṛtti gives one counter-example for each half, and a table
    that dropped either condition would still pass a test that only
    checked the positive case.
    """

    def test_the_sound_has_to_be_one_of_the_three(self):
        self.assertEqual(NDRA, ("n", "d", "r"))
        for sound in NDRA:
            self.assertEqual(stated(sound=sound, at="saṃyogādi").sutra,
                             "6.1.3", sound)

    def test_a_fourth_sound_is_not_refused(self):
        self.assertEqual(stated(sound="k", at="saṃyogādi").sutra, "")

    def test_and_it_has_to_open_a_cluster(self):
        self.assertEqual(stated(sound="n", at="ajādi").sutra, "")
        self.assertEqual(stated(sound="n").sutra, "")

    def test_the_note_carries_both_counter_examples(self):
        why = provisions_for("6.1.3")[0].why
        self.assertIn("ईचिक्षिषते", why)
        self.assertIn("प्राणिणिषति", why)


class TheVedicLengtheningIsOutOfReachWithoutTheCorpus(unittest.TestCase):
    def test_it_answers_nothing_in_ordinary_speech(self):
        self.assertEqual(stated("tuj").sutra, "")

    def test_but_does_once_the_corpus_is_named(self):
        answer = stated("tuj", chandasi=True)
        self.assertEqual(answer.sutra, "6.1.7")
        self.assertEqual(answer.does, "dīrgha")
        self.assertTrue(answer.chandasi)

    def test_it_is_the_only_row_that_lengthens(self):
        lengthening = [r.sutra for r in ABHYASTA_TABLE
                       if r.does == "dīrgha"]
        self.assertEqual(lengthening, ["6.1.7"])

    def test_the_note_says_the_run_has_no_list(self):
        """
        तुजादीनामिति प्रकार आदिशब्दः — आदि here means *and the like*,
        not *and what follows in the gaṇa*. There is nothing to
        enumerate, and the table must not pretend there is.
        """
        why = provisions_for("6.1.7")[0].why
        self.assertIn("प्रकार आदिशब्दः", why)
        self.assertEqual(provisions_for("6.1.7")[0].of, ("tuj",))


class AskingForOneThingDoesNotGetAnother(unittest.TestCase):
    def test_asking_for_a_doubling_never_returns_a_naming_rule(self):
        self.assertEqual(stated(part="pūrva", wants="dvirvacana").sutra,
                         "")

    def test_asking_for_a_name_never_returns_an_operation(self):
        self.assertEqual(stated(before="liṭ", wants="abhyasta").sutra,
                         "")

    def test_asking_for_a_doubling_never_returns_a_refusal(self):
        asked = stated("dāś", before="kvasu", wants="dvirvacana")
        self.assertEqual(asked.sutra, "")

    def test_asking_for_the_name_by_its_own_word_reaches_it(self):
        self.assertEqual(stated(part="ubhe", wants="abhyasta").sutra,
                         "6.1.5")


class NothingAnswersByDefault(unittest.TestCase):
    def test_an_empty_question_reaches_nothing(self):
        self.assertEqual(stated().sutra, "")

    def test_and_the_message_says_what_the_heading_carries_instead(self):
        """
        6.1.1 is an अधिकार, but it supplies three WORDS — एकाचः, द्वे,
        प्रथमस्य — and not an operation. So unlike every heading the
        project has met in the taddhita pādas, there is nothing for
        it to answer with.
        """
        self.assertIn("प्रथमस्य", stated().why)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in ABHYASTA_TABLE:
            self.assertGreater(len(row.why), 120, row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in ABHYASTA_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)

    def test_a_refusal_records_what_it_keeps_out(self):
        for row in ABHYASTA_TABLE:
            if row.refuses:
                self.assertGreater(len(row.keeps_out), 20, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_module_does_not_reduplicate(self):
        """
        `stated` reports what a rule says. Building जुहोति out of हु
        is `dvirvacana.for_sutra`, and the two are kept apart on
        purpose — an answer here that carried a finished stem would
        mean the split had quietly collapsed.
        """
        answer = stated(before="ślu")
        self.assertEqual(answer.does, "dvirvacana")
        self.assertNotIn("juhoti", str(answer))

    def test_the_accent_rule_the_two_names_feed_landed(self):
        """
        6.1.189 अभ्यस्तानामादिः is what makes 6.1.5's उभे matter
        — the accent falls once, on the first vowel of the PAIR —
        and it is codified now. The debt this test was written as
        is paid, and what replaces it is the live dependency: that
        rule turns on the name this table gives.
        """
        from src.astadhyayi.pada_svara import provisions_for as svara

        self.assertTrue(REGISTRY.has("6.1.189"))
        self.assertIn("6.1.189", provisions_for("6.1.5")[0].why)
        self.assertEqual(svara("6.1.189")[0].gana, "abhyasta")
        self.assertIn("6.1.5", svara("6.1.189")[0].why)


if __name__ == "__main__":
    unittest.main()
