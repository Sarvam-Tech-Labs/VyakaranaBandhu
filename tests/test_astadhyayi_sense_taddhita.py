# -*- coding: utf-8 -*-
"""
४.२.१–२१ — a case-relation and a sense, and the affix understood.

अध्याय ४ पाद १ spent 178 sūtras on ONE sense and named its affix in
nearly every rule. This pāda changes the shape: each rule states a
CASE and a SENSE, and lets 4.1.83's default supply the affix unless it
has reason to speak. Eight of these twenty-one name no affix at all.

That is what 4.1.82 was for, and this file tests the two halves
against each other.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.sutra import REGISTRY
from tests import unwrapped


class ANewShapeOfRule(unittest.TestCase):
    """
    The claim is countable: this pāda leans on the default where the
    one before it named an affix nearly every time.
    """

    def test_many_rules_here_name_no_affix(self):
        from src.astadhyayi.sense_taddhita import SENSE_TABLE

        silent = [row.sutra for row in SENSE_TABLE
                  if not row.gives and not row.elides]
        self.assertGreaterEqual(len(silent), 6)

    def test_and_each_of_those_answers_by_the_default(self):
        from src.astadhyayi.sense_taddhita import (SENSE_TABLE,
                                                   in_sense,
                                                   provisions_for)
        from src.astadhyayi.taddhita import default_affix

        for row in SENSE_TABLE:
            if row.gives or row.elides:
                continue
            where = {"case": row.case, "sense": row.sense}
            if row.result:
                where["result"] = row.result
            if row.of_samjna:
                where["samjna"] = row.of_samjna
            if row.gana:
                where["gana"] = row.gana
            if row.of:
                where["stem"] = row.of[0]
            with self.subTest(sutra=row.sutra):
                answer = in_sense(**where)
                self.assertEqual(answer.by, row.sutra)
                if row.borrows_from:
                    # 4.2.34 names no affix either, and does NOT
                    # fall to the default: it is an अतिदेश, and it
                    # takes whatever the rules it points at give.
                    from src.astadhyayi.kala_taddhita import born_in

                    lent = born_in(where.get("stem", ""),
                                   sense="śeṣa",
                                   samjna=where.get("samjna", ""))
                    self.assertEqual(answer.gives, lent.gives)
                    self.assertNotEqual(answer.gives,
                                        default_affix().gives)
                    continue
                if row.affix_from:
                    # 4.2.140 names no affix either, and does NOT
                    # fall to the default: it enjoins a substitute
                    # and leaves an earlier rule's affix standing.
                    # आदेशमात्रमिह विधेयम्.
                    leaned_on = provisions_for(row.affix_from)[0]
                    self.assertEqual(answer.gives, leaned_on.gives)
                    self.assertNotEqual(answer.gives,
                                        default_affix().gives)
                    continue
                self.assertEqual(answer.gives, default_affix().gives)

    def test_the_fall_through_is_declared(self):
        for sutra in ("4.2.1", "4.2.3", "4.2.7", "4.2.10", "4.2.14",
                      "4.2.16"):
            with self.subTest(sutra=sutra):
                self.assertIn("4.1.83", REGISTRY.get(sutra).reuses)

    def test_and_the_heading_that_makes_it_possible_is_codified(self):
        """
        4.1.82 समर्थानां प्रथमाद्वा says the affix attaches to the
        FIRST of the connected words; these rules say which
        connection, in which case, and in what sense. Neither works
        alone.
        """
        from src.astadhyayi.taddhita import samartha

        self.assertTrue(REGISTRY.has("4.1.82"))
        self.assertEqual(samartha().words[0], "samarthānām")


class TwoCaseRunsWithBothEndsStated(unittest.TestCase):
    """
    4.2.1's vṛtti names 4.2.12 as where the instrumental stops, and
    4.2.14's names 4.2.20 for the locative. **Both ends of both ranges
    are stated**, which is not true of most anuvṛtti.
    """

    def test_each_run_names_where_it_stops(self):
        from src.astadhyayi.sense_taddhita import CASE_RUNS

        self.assertEqual(
            CASE_RUNS,
            (("tṛtīyā", "4.2.1", "4.2.12"),
             ("saptamī", "4.2.14", "4.2.20")))

    def test_and_the_opening_rule_says_so_in_its_own_notes(self):
        self.assertIn("द्वैपवैयाघ्रादञ् इति यावत्",
                      unwrapped(REGISTRY.get("4.2.1").notes))
        self.assertIn("क्षीराड् ढञ् इति यावत्",
                      unwrapped(REGISTRY.get("4.2.14").notes))

    def test_every_rule_inside_a_run_states_that_run_s_case(self):
        """
        The check that makes the ranges mean something: if a rule
        between 4.2.1 and 4.2.12 held a different case, the stated
        boundary would be wrong.
        """
        from src.astadhyayi.sense_taddhita import CASE_RUNS, SENSE_TABLE

        for named, opens, closes in CASE_RUNS:
            low = int(opens.rsplit(".", 1)[1])
            high = int(closes.rsplit(".", 1)[1])
            for row in SENSE_TABLE:
                number = int(row.sutra.rsplit(".", 1)[1])
                if not low <= number <= high or not row.case:
                    continue
                with self.subTest(sutra=row.sutra, run=named):
                    self.assertEqual(row.case, named)

    def test_and_a_case_the_run_does_not_carry_is_refused(self):
        from src.astadhyayi.sense_taddhita import case_run

        answer = case_run("caturthī")
        self.assertIn("carries two", answer.why)

    def test_the_rules_named_as_boundaries_are_codified(self):
        for sutra in ("4.2.1", "4.2.12", "4.2.14", "4.2.20"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))


class OneWordSeparatingTwoRules(unittest.TestCase):
    """
    4.2.3 and 4.2.4 share their base, their case and their sense. One
    gives an affix and the other takes it away, and अविशेषे is the
    whole difference.
    """

    def test_the_two_rows_differ_in_exactly_one_field(self):
        from src.astadhyayi.sense_taddhita import provisions_for

        giving, = provisions_for("4.2.3")
        eliding, = provisions_for("4.2.4")
        self.assertEqual(
            (giving.case, giving.sense, giving.result, giving.of_samjna),
            (eliding.case, eliding.sense, eliding.result,
             eliding.of_samjna))
        self.assertFalse(giving.unspecified)
        self.assertTrue(eliding.unspecified)
        self.assertFalse(giving.elides)
        self.assertTrue(eliding.elides)

    def test_and_the_resolver_tells_them_apart(self):
        from src.astadhyayi.sense_taddhita import in_sense

        where = dict(case="tṛtīyā", sense="yukta", result="kāla",
                     samjna="nakṣatra")
        self.assertEqual(in_sense(**where).by, "4.2.3")
        self.assertFalse(in_sense(**where).elided)
        dropped = in_sense(unspecified=True, **where)
        self.assertEqual(dropped.by, "4.2.4")
        self.assertTrue(dropped.elided)
        self.assertEqual(dropped.gives, "")


class WhereTheGrammarNeedsAnotherScience(unittest.TestCase):
    """
    4.2.3 cannot be applied without knowing what it means for a time
    to be *joined with a star*, and the vṛtti supplies it rather than
    leaving the rule unusable.
    """

    def test_the_astronomical_gloss_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.2.3").notes)
        self.assertIn("कथं पुनर्नक्षत्रेण", notes)
        self.assertIn("चन्द्रमसि वर्तमानाः", notes)

    def test_and_two_other_rules_define_their_own_terms(self):
        """
        4.2.10 defines *wrapped* — covered on every side with no part
        bare — and 4.2.16 defines both *food* and *preparing*. None
        of the three definitions is in a sūtra.
        """
        self.assertIn("यस्य न कश्चिदवयवो",
                      unwrapped(REGISTRY.get("4.2.10").notes))
        notes = unwrapped(REGISTRY.get("4.2.16").notes)
        self.assertIn("खरविशदमभ्यवहार्यं भक्षम्", notes)
        self.assertIn("सत उत्कर्षाधानं संस्कारः", notes)

    def test_and_one_rule_turns_on_a_vow(self):
        notes = unwrapped(REGISTRY.get("4.2.15").notes)
        self.assertIn("शास्त्रितो नियम", notes)
        self.assertIn("स्थण्डिले शेते ब्रह्मदत्तः", notes)


class TwoRulesOneAffixOneSenseAndTheyStillDiffer(unittest.TestCase):
    """
    4.2.18's vṛtti asks why the rule is needed when 4.4.1 gives the
    same affix in the same sense, and answers by a difference in the
    SITUATION rather than in the grammar.
    """

    def test_the_question_and_the_answer_are_both_recorded(self):
        notes = unwrapped(REGISTRY.get("4.2.18").notes)
        self.assertIn("तेनैव सिद्धम्", notes)
        self.assertIn("दधिकृतमेव", notes)
        self.assertIn("केवलमाधारभूतम्", notes)

    def test_and_the_rule_it_is_measured_against_exists(self):
        from src.astadhyayi.corpus import collate

        self.assertIn("4.4.1", collate())


class ASilentLetterKeepingAnAffixOutOfALaterRule(unittest.TestCase):
    """
    4.2.9's ड्. Without it, 6.2.156 would catch the two affixes and
    अवामदेव्यम् would take the wrong accent.
    """

    def test_the_argument_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.2.9").notes)
        self.assertIn("डित्करणं किमर्थम्", notes)
        self.assertIn("अनयोर्ग्रहणं मा भूत्", notes)

    def test_and_the_rule_it_is_kept_out_of_exists(self):
        from src.astadhyayi.corpus import collate

        self.assertIn("6.2.156", collate())

    def test_the_affix_carries_the_mark(self):
        from src.astadhyayi.sense_taddhita import in_sense

        answer = in_sense("vāmadeva", case="tṛtīyā", sense="dṛṣṭa",
                          result="sāman")
        self.assertEqual(answer.by, "4.2.9")
        self.assertTrue(answer.gives.startswith("ḍ"))


class ARuleStatedForWhatItPrevents(unittest.TestCase):
    """
    4.2.11: मत्वर्थीयेनैव सिद्धे वचनमणो निवृत्त्यर्थम् — the affix was
    available anyway, so the rule exists only to keep the default out.
    """

    def test_the_reason_is_on_record(self):
        self.assertIn("वचनमणो निवृत्त्यर्थम्",
                      unwrapped(REGISTRY.get("4.2.11").notes))

    def test_and_the_project_has_met_the_shape_before(self):
        """
        4.1.84 gave the default affix to a list and was read the same
        way — पत्युत्तरपदाद् ण्यं वक्ष्यति, तस्यापवादः — except that
        there the thing prevented had not yet been stated.
        """
        self.assertIn("वक्ष्यति", unwrapped(REGISTRY.get("4.1.84").notes))
        self.assertIn("4.1.84", unwrapped(REGISTRY.get("4.2.11").notes))

    def test_the_rule_still_gives_its_own_affix(self):
        from src.astadhyayi.sense_taddhita import in_sense

        answer = in_sense("pāṇḍukambala", case="tṛtīyā",
                          sense="parivṛta", result="ratha")
        self.assertEqual(answer.by, "4.2.11")
        self.assertEqual(answer.gives, "ini")


class EveryRowIsReachableAndBelongsToARule(unittest.TestCase):
    """
    A row no query can reach is a rule the project has written down
    and cannot run.
    """

    def test_every_row_answers_by_its_own_sutra(self):
        from src.astadhyayi.sense_taddhita import SENSE_TABLE, in_sense

        for row in SENSE_TABLE:
            where = {}
            if row.of:
                where["stem"] = row.of[0]
            if row.gana:
                where["gana"] = row.gana
            if row.case:
                where["case"] = row.case
            if row.sense:
                where["sense"] = row.sense
            if row.result:
                where["result"] = row.result
            if row.of_samjna:
                where["samjna"] = row.of_samjna
            if row.unspecified:
                where["unspecified"] = True
            if row.stem_final:
                where["stem_final"] = row.stem_final
            if row.dvyac:
                where["dvyac"] = True
            if row.pre:
                where["pre"] = row.pre
            if row.accent:
                where["accent"] = row.accent
            if row.marked:
                where["marked"] = row.marked
            if row.upadha:
                where["upadha"] = row.upadha
            if row.ends_with:
                where["ends_with"] = row.ends_with[0]
            if row.desa:
                where["desa"] = True
            if row.gives:
                where["wants"] = row.gives
            with self.subTest(sutra=row.sutra, **where):
                answer = in_sense(**where)
                if row.refuses:
                    # A प्रतिषेध answers by the rule that supplies,
                    # with its own id on `excepts` — unless refusing
                    # is all it did, in which case it answers by
                    # itself with no affix. The same carve-out the
                    # case-runner knows, and the same reason.
                    if answer.excepts:
                        self.assertIn(row.sutra, answer.excepts)
                    else:
                        self.assertEqual(answer.by, row.sutra)
                        self.assertEqual(answer.gives, "")
                    continue
                self.assertEqual(answer.by, row.sutra)

    def test_every_row_belongs_to_a_codified_sutra(self):
        from src.astadhyayi.sense_taddhita import SENSE_TABLE

        for row in SENSE_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(REGISTRY.has(row.sutra))

    def test_and_the_pada_is_contiguous_as_far_as_it_is_read(self):
        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 2}
        self.assertEqual(have, set(range(1, max(have) + 1)))



class FourRangesWithBothEndsStated(unittest.TestCase):
    """
    Two case-runs and two sense-runs, and the vṛtti of the rule that
    opens each names the rule that closes it. Most anuvṛtti in this
    project has had to be inferred from where a rule stops making
    sense.
    """

    def test_the_sense_runs_are_named(self):
        from src.astadhyayi.sense_taddhita import SENSE_RUNS

        self.assertEqual(
            SENSE_RUNS,
            (("devatā", "4.2.24", "4.2.35"),
             ("samūha", "4.2.37", "4.2.51"),
             ("adhīte-veda", "4.2.59", "4.2.65"),
             ("cāturarthika", "4.2.67", "4.2.91")))

    def test_and_the_fourth_is_a_run_of_four_senses_at_once(self):
        """
        4.2.67 to 4.2.70 state four senses, and 4.2.70's च gathers
        them — चकारः पूर्वेषां त्रयाणामर्थानामिह सन्निधानार्थः, तेन
        उत्तरेषु चत्वारोऽप्यर्थाः संबध्यन्ते. Every rule to 4.2.91
        then gives an affix in whichever fits, and the tradition
        names the whole body of them after the NUMBER.
        """
        from src.astadhyayi.sense_taddhita import (
            CATURARTHIKA, provisions_for)

        self.assertEqual(len(CATURARTHIKA), 4)
        stated = [provisions_for("4.2.%d" % n)[0].result
                  for n in range(67, 71)]
        self.assertEqual(tuple(stated), CATURARTHIKA)
        self.assertIn("चत्वारोऽप्यर्थाः संबध्यन्ते",
                      unwrapped(REGISTRY.get("4.2.70").notes))

    def test_and_a_range_is_stated_of_an_affix_too(self):
        """
        4.2.71's अञधिकारः प्राक् सुवास्त्वादिभ्योऽणः — the sixth
        stated range in the pāda, and the first of an AFFIX rather
        than of a case or a sense. Both ends are codified.
        """
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertIn("अञधिकारः प्राक् सुवास्त्वादिभ्योऽणः",
                      unwrapped(REGISTRY.get("4.2.71").notes))
        self.assertEqual(provisions_for("4.2.71")[0].gives, "añ")
        self.assertEqual(provisions_for("4.2.77")[0].gives, "aṇ")

    def test_and_each_opening_rule_records_its_own_boundary(self):
        self.assertIn("महाराजप्रोष्ठपदाट् ठञ् इति यावत्",
                      unwrapped(REGISTRY.get("4.2.24").notes))
        self.assertIn("इनित्रकट्यचश्च इति यावत्",
                      unwrapped(REGISTRY.get("4.2.37").notes))

    def test_and_the_closing_rule_says_it_is_the_end(self):
        """
        The third run's boundary is recorded from the other side:
        4.2.65's own note says the studying-sense stops there. Both
        ends of a range are worth having, and here one end is stated
        by the rule that opens it and the other by the rule that
        closes it.
        """
        for sutra in ("4.2.51", "4.2.65"):
            with self.subTest(sutra=sutra):
                self.assertIn("stops",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_every_rule_inside_a_sense_run_states_that_sense(self):
        from src.astadhyayi.sense_taddhita import SENSE_RUNS, SENSE_TABLE

        for named, opens, closes in SENSE_RUNS:
            low = int(opens.rsplit(".", 1)[1])
            high = int(closes.rsplit(".", 1)[1])
            for row in SENSE_TABLE:
                number = int(row.sutra.rsplit(".", 1)[1])
                if not low <= number <= high or not row.sense:
                    continue
                with self.subTest(sutra=row.sutra, run=named):
                    self.assertEqual(row.sense, named)

    def test_a_sense_the_pada_does_not_bound_is_refused(self):
        from src.astadhyayi.sense_taddhita import sense_run

        self.assertIn("states two", sense_run("bhāva").why)


class ASutraSplitToPreventAPairing(unittest.TestCase):
    """
    4.2.28. Two affixes and two bases in one rule would have been
    matched one to one by 1.3.10; dividing the sūtra is what lets
    both affixes reach both words.
    """

    def test_the_reason_is_on_record(self):
        self.assertIn("योगविभागः सङ्ख्यातानुदेशपरिहारार्थः",
                      unwrapped(REGISTRY.get("4.2.28").notes))

    def test_and_both_affixes_really_do_reach_both_words(self):
        from src.astadhyayi.sense_taddhita import in_sense

        for stem in ("aponaptṛ", "apāṃnaptṛ"):
            for affix, sutra in (("gha", "4.2.27"), ("cha", "4.2.28")):
                with self.subTest(stem=stem, affix=affix):
                    answer = in_sense(stem, case="prathamā",
                                      sense="devatā", wants=affix)
                    self.assertEqual(answer.by, sutra)

    def test_the_project_has_met_the_purpose_by_another_instrument(self):
        """
        4.1.150 achieved the same thing by BREAKING a compounding
        rule and letting the breach be the signal. Two instruments,
        one purpose, a pāda apart — and both notes name it.
        """
        self.assertIn("यथासंख्यमिह न भवति",
                      unwrapped(REGISTRY.get("4.1.150").notes))
        self.assertIn("4.1.150", unwrapped(REGISTRY.get("4.2.28").notes))


class AnExtensionReachingForward(unittest.TestCase):
    """
    4.2.34 कालेभ्यो भववत् borrows the affixes 4.3.11 onward will give
    — rules not yet stated — and वत्करणं सर्वसादृश्यपरिग्रहार्थम्
    says the borrowing is TOTAL.
    """

    def test_the_rules_it_borrows_from_lie_ahead(self):
        """
        They lay ahead when this rule was codified and the test said
        so, as the exact shortfall. They are codified now, and the
        assertion that was waiting for them can be made.
        """
        from src.astadhyayi.corpus import collate

        self.assertIn("4.3.11", collate())
        self.assertTrue(REGISTRY.has("4.3.11"))
        self.assertEqual(int("4.3.11".rsplit(".", 1)[1]), 11)

    def test_and_the_borrowing_is_now_executed_rather_than_described(self):
        """
        मासो देवतास्य **मासिकम्** — the ठञ् 4.3.11 gives, not the
        अण् this rule would have fallen to while those rules were
        missing.
        """
        from src.astadhyayi.kala_taddhita import born_in
        from src.astadhyayi.sense_taddhita import in_sense, provisions_for
        from src.astadhyayi.taddhita import default_affix

        self.assertEqual(provisions_for("4.2.34")[0].borrows_from,
                         "4.3.11")
        borrowed = in_sense(case="prathamā", sense="devatā",
                            samjna="kāla")
        self.assertEqual(borrowed.by, "4.2.34")
        self.assertEqual(borrowed.gives,
                         born_in(sense="śeṣa", samjna="kāla").gives)
        self.assertEqual(borrowed.gives, "ṭhañ")
        self.assertNotEqual(borrowed.gives, default_affix().gives)

    def test_and_the_likeness_is_total_and_not_one_affix(self):
        """
        **सर्वसादृश्यपरिग्रहार्थम्.** प्रावृषेण्यम् is among the
        examples, and that affix comes from 4.3.17 and not from
        4.3.11 — so the borrowing has to be of whatever those rules
        give, base by base, and not of a single named affix.
        """
        from src.astadhyayi.sense_taddhita import in_sense

        rains = in_sense("prāvṛṣ", case="prathamā", sense="devatā",
                         samjna="kāla")
        self.assertEqual(rains.by, "4.2.34")
        self.assertEqual(rains.gives, "eṇya")
        self.assertIn("4.3.17", rains.why)
        self.assertIn("प्रावृषेण्यम्",
                      unwrapped(REGISTRY.get("4.2.34").notes))

    def test_the_borrowing_is_stated_to_be_total(self):
        notes = unwrapped(REGISTRY.get("4.2.34").notes)
        self.assertIn("वत्करणं सर्वसादृश्यपरिग्रहार्थम्", notes)

    def test_and_the_only_other_atidesa_met_was_bounded(self):
        """
        3.4.85's लोटो लङ्वत् had its borrowing cut short by an option
        carried from two sūtras back — अडाटौ कस्माद् न भवतः. This one
        is stated to take everything.
        """
        self.assertIn("अडाटौ कस्माद् न भवतः",
                      unwrapped(REGISTRY.get("3.4.85").notes))


class TheMostCompleteNipatana(unittest.TestCase):
    """
    4.2.36. समर्थविभक्तिः प्रत्ययः प्रत्ययार्थोऽनुबन्ध इति सर्वं
    निपातनाद् विज्ञेयम् — case, affix, sense and marks are all read
    backward off the forms given.
    """

    def test_the_claim_is_on_record(self):
        self.assertIn("सर्वं निपातनाद् विज्ञेयम्",
                      unwrapped(REGISTRY.get("4.2.36").notes))

    def test_and_the_row_states_no_case_and_no_sense(self):
        """
        The check that makes it more than a remark: every other row
        of this pāda states a case or a sense or both, and this one
        states neither, because there is nothing to state.
        """
        from src.astadhyayi.sense_taddhita import provisions_for

        row, = provisions_for("4.2.36")
        self.assertEqual(row.case, "")
        self.assertEqual(row.sense, "")
        self.assertEqual(row.of_samjna, "nipātana")

    def test_only_two_rows_state_neither_a_case_nor_a_sense(self):
        """
        And the two are the same kind of thing. 4.2.36 states nothing
        because everything is read backward off the fixed forms;
        4.2.66 states nothing because it RESTRICTS a class of words
        already formed rather than giving an affix to a base. Neither
        is a provision, which is why neither has a ground.
        """
        from src.astadhyayi.sense_taddhita import SENSE_TABLE

        bare = [row.sutra for row in SENSE_TABLE
                if not row.case and not row.sense]
        self.assertEqual(bare, ["4.2.36", "4.2.66"])
        self.assertIn("सर्वं निपातनाद् विज्ञेयम्",
                      unwrapped(REGISTRY.get("4.2.36").notes))
        self.assertIn("तद्विषयाण्येव भवन्ति",
                      unwrapped(REGISTRY.get("4.2.66").notes))


class AnExampleComputedBySubtraction(unittest.TestCase):
    """
    4.2.37's vṛtti asks किमिहोदाहरणम् and answers with a list of what
    the example must NOT be — because every ordinary base is claimed
    by some later rule of its own section.
    """

    def test_the_four_exclusions_are_recorded(self):
        notes = unwrapped(REGISTRY.get("4.2.37").notes)
        self.assertIn("किमिहोदाहरणम्", notes)
        self.assertIn("चित्तवद् आद्युदात्तम् अगोत्रम्", notes)
        for sutra in ("4.2.39", "4.2.40", "4.2.44", "4.2.47"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, notes)

    def test_and_all_four_are_codified_now(self):
        """
        PAID. The debt was written as the exact shortfall — two of
        the four subtracted rules were still ahead — and it failed
        the moment 4.2.44 and 4.2.47 arrived.

        What the four exclude can now be checked rather than quoted:
        each of them really does state one of the grounds the vṛtti
        subtracts.
        """
        from src.astadhyayi.sense_taddhita import provisions_for

        for sutra in ("4.2.39", "4.2.40", "4.2.44", "4.2.47"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))
        self.assertEqual(provisions_for("4.2.44")[0].of_samjna,
                         "anudāttādi")
        self.assertEqual(provisions_for("4.2.47")[0].of_samjna,
                         "acitta")
        self.assertTrue(provisions_for("4.2.39")[0].gana)
        self.assertTrue(provisions_for("4.2.40")[0].of)


class OneWordTechnicalInsideItsSectionAndOrdinaryOutside(unittest.TestCase):
    """
    4.2.39's गोत्र. अपत्याधिकारादन्यत्र लौकिकं गोत्रं गृह्यते
    अपत्यमात्रम्, न तु पौत्रप्रभृत्येव — outside the section that
    defined it, the word carries its everyday meaning.
    """

    def test_the_technical_sense_was_conferred_earlier(self):
        from src.astadhyayi.apatya import descendant_name

        self.assertEqual(descendant_name().name, "gotra")
        self.assertEqual(descendant_name().by, "4.1.162")

    def test_and_this_rule_says_it_does_not_apply_here(self):
        notes = unwrapped(REGISTRY.get("4.2.39").notes)
        self.assertIn("लौकिकं गोत्रं गृह्यते", notes)
        self.assertIn("न तु पौत्रप्रभृत्येव", notes)

    def test_the_boundary_is_the_section_itself(self):
        """
        अपत्याधिकारादन्यत्र — *outside the descendant heading*. The
        name holds where that heading runs and not beyond.
        """
        self.assertIn("अपत्याधिकारादन्यत्र",
                      unwrapped(REGISTRY.get("4.2.39").notes))
        self.assertTrue(REGISTRY.has("4.1.92"))


class TheUpadhaIsNotTheFinal(unittest.TestCase):
    """
    Six rules of 4.2.119–145 are stated on the PENULTIMATE sound —
    कोपध, योपध, रोपध, खोपध. 1.1.65 defines उपधा as the sound before
    the last, so a base whose उपधा is क does not END in क, and a
    table that stored the two in one column would answer for words
    the rule never reaches.
    """

    def test_the_run_really_does_turn_on_the_penultimate(self):
        from src.astadhyayi.sense_taddhita import SENSE_TABLE

        on_upadha = {row.sutra for row in SENSE_TABLE if row.upadha}
        self.assertEqual(
            on_upadha,
            {"4.2.121", "4.2.123", "4.2.132", "4.2.141"})

    def test_and_no_row_confuses_it_with_the_final(self):
        from src.astadhyayi.sense_taddhita import SENSE_TABLE

        for row in SENSE_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertFalse(row.upadha and row.stem_final)

    def test_a_k_final_base_does_not_reach_the_k_penultimate_rule(self):
        """
        The failure the column exists to prevent. 4.2.132 कोपधादण्
        must not answer for a base that merely ENDS in क.
        """
        from src.astadhyayi.sense_taddhita import in_sense

        reached = in_sense(sense="śeṣa", desa=True, upadha="k")
        self.assertEqual(reached.by, "4.2.132")
        missed = in_sense(sense="śeṣa", desa=True, stem_final="k")
        self.assertNotEqual(missed.by, "4.2.132")

    def test_and_the_grammar_defines_the_term_elsewhere(self):
        self.assertTrue(REGISTRY.has("1.1.65"))


class AWordReadTwiceIsAWordThatLapsed(unittest.TestCase):
    """
    4.2.119's argument about anuvṛtti, which is the cleanest evidence
    for where a word stops that this project has met: वृद्धादिति
    नानुवर्तते, **उत्तरसूत्रे पुनर्वृद्धग्रहणात्**.
    """

    def test_the_argument_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.2.119").notes)
        self.assertIn("वृद्धादिति नानुवर्तते", notes)
        self.assertIn("उत्तरसूत्रे पुनर्वृद्धग्रहणात्", notes)

    def test_and_the_table_is_built_the_way_the_argument_says(self):
        """
        The claim is checkable: 4.2.119 must state no वृद्ध condition
        and 4.2.120 must state one, or the argument has no premise.
        """
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertEqual(provisions_for("4.2.119")[0].of_samjna, "")
        self.assertIn("vṛddha", provisions_for("4.2.120")[0].of_samjna)

    def test_and_an_affix_given_in_a_pair_is_named_again(self):
        """
        The same rule's second argument. 4.2.116 and 4.2.117 gave ठञ्
        and ञिठ together, so ठञ् cannot be carried on by itself:
        ठञ्ञिठयोः प्रकरणे ठञः केवलस्यानुवृत्तिर्न लभ्यते.
        """
        from src.astadhyayi.sense_taddhita import provisions_for

        notes = unwrapped(REGISTRY.get("4.2.119").notes)
        self.assertIn("ठञः केवलस्यानुवृत्तिर्न लभ्यत", notes)
        self.assertEqual(provisions_for("4.2.116")[0].gives, "ṭhañ")
        self.assertEqual(provisions_for("4.2.117")[0].gives, "ṭhañ")
        self.assertEqual(provisions_for("4.2.119")[0].gives, "ṭhañ")


class ARuleThatAddsNothingAndThereforeRestricts(unittest.TestCase):
    """
    पूर्वेणैव सिद्धे नियमार्थं वचनम् — twice in this run, and both
    times the premise is checkable: the earlier rule must really
    reach the ground the later one is stated on.
    """

    def test_both_niyamas_are_on_record(self):
        for sutra, earlier in (("4.2.120", "ठञि"), ("4.2.135", "वुञि")):
            with self.subTest(sutra=sutra):
                notes = unwrapped(REGISTRY.get(sutra).notes)
                self.assertIn("नियमार्थं वचनम्", notes)
                self.assertIn("पूर्वेणैव", notes)
                self.assertIn(earlier, notes)

    def test_and_the_earlier_rule_really_reaches_that_ground(self):
        """
        4.2.119 must give ठञ् on 4.2.120's own ground, and 4.2.134
        must give वुञ् on 4.2.135's, or neither restriction has
        anything to restrict.
        """
        from src.astadhyayi.sense_taddhita import in_sense

        without = in_sense(sense="śeṣa", stem_final="u", desa=True)
        self.assertEqual(without.by, "4.2.119")
        self.assertEqual(without.gives, "ṭhañ")

        general = in_sense(sense="śeṣa", gana="kacchādi",
                           result="manuṣya-tatstha")
        self.assertEqual(general.by, "4.2.134")
        self.assertEqual(general.gives, "vuñ")

    def test_and_the_restricted_form_gives_the_same_affix(self):
        """
        A नियम narrows the ground and keeps the affix. If the two
        differed it would be an अपवाद instead, and the argument the
        vṛtti makes would not hold.
        """
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertEqual(provisions_for("4.2.119")[0].gives,
                         provisions_for("4.2.120")[0].gives)
        self.assertEqual(provisions_for("4.2.134")[0].gives,
                         provisions_for("4.2.135")[0].gives)


class ARuleThatEnjoinsOnlyASubstitute(unittest.TestCase):
    """
    4.2.140 राज्ञः क च. **आदेशमात्रमिह विधेयम्, प्रत्ययस्तु वृद्धाच्छ
    इत्येव सिद्धः** — only the substitute is enjoined; the छ was
    already 4.2.114's. The row says so by naming that rule instead of
    repeating its affix, which is the fall-through this project has
    used since 4.1.84, applied for the first time to a rule that
    supplies no affix at all.
    """

    def test_the_row_names_no_affix(self):
        from src.astadhyayi.sense_taddhita import provisions_for

        row = provisions_for("4.2.140")[0]
        self.assertEqual(row.gives, "")
        self.assertEqual(row.affix_from, "4.2.114")
        self.assertTrue(row.along_with)

    def test_and_the_answer_is_the_other_rule_s_own_affix(self):
        from src.astadhyayi.sense_taddhita import (in_sense,
                                                   provisions_for)

        answer = in_sense(sense="śeṣa", stem="rājan", samjna="vṛddha")
        self.assertEqual(answer.by, "4.2.140")
        self.assertEqual(answer.gives, provisions_for("4.2.114")[0].gives)
        self.assertIn(provisions_for("4.2.114")[0].why, answer.why)
        self.assertIn("क", answer.along_with)

    def test_and_it_is_not_the_general_default(self):
        """
        The affix left standing is 4.2.114's छ, not 4.1.83's अण्. If
        the fall-through went to the default the answer would be
        wrong in exactly the way the vṛtti warns against.
        """
        from src.astadhyayi.taddhita import default_affix
        from src.astadhyayi.sense_taddhita import in_sense

        answer = in_sense(sense="śeṣa", stem="rājan", samjna="vṛddha")
        self.assertNotEqual(answer.gives, default_affix().gives)
        self.assertEqual(answer.gives, "cha")

    def test_and_the_word_qualifies_for_that_rule(self):
        """
        4.2.114 wants a वृद्ध base, and राजन् is one by 1.1.73 —
        which is why the affix was there to be left standing.
        """
        self.assertTrue(REGISTRY.has("1.1.73"))
        self.assertIn("वृद्धाच्छ इत्येव सिद्धः",
                      unwrapped(REGISTRY.get("4.2.140").notes))


class TheMaximOfButtermilkForKaundinya(unittest.TestCase):
    """
    4.2.125's अपि. **तक्रकौण्डिन्यन्यायेन बाधा मा विज्ञायीति
    समुच्चीयते** — telling the servants to give buttermilk to
    Kauṇḍinya does not cancel the milk everyone else was getting.
    """

    def test_the_maxim_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.2.125").notes)
        self.assertIn("तक्रकौण्डिन्यन्यायेन", notes)
        self.assertIn("बाधा मा विज्ञायीति समुच्चीयते", notes)

    def test_and_the_question_it_answers_is_recorded_too(self):
        notes = unwrapped(REGISTRY.get("4.2.125").notes)
        self.assertIn("अपिग्रहणं किम्", notes)
        self.assertIn("यावता वृद्धात् पूर्वेणैव सिद्धम्", notes)

    def test_and_the_two_rules_give_the_same_affix(self):
        """
        Why the maxim was needed at all: both rules give वुञ्, so
        whether the later one REPLACES the earlier or joins it makes
        no difference to any form. The question can only be settled
        by argument, and the commentary settles it.
        """
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertEqual(provisions_for("4.2.124")[0].gives, "vuñ")
        self.assertEqual(provisions_for("4.2.125")[0].gives, "vuñ")

    def test_and_the_domain_word_keeps_a_borrowed_plural_out(self):
        """
        विषयग्रहणमनन्यत्रभावार्थम् — the plural has to be the word's
        own, not one coming from 1.2.64's एकशेष.
        """
        notes = unwrapped(REGISTRY.get("4.2.125").notes)
        self.assertIn("विषयग्रहणमनन्यत्रभावार्थम्", notes)
        self.assertIn("जनपदैकशेषबहुत्वे मा भूत्", notes)
        self.assertTrue(REGISTRY.has("1.2.64"))


class ARuleReachingForwardToProtectItsGround(unittest.TestCase):
    """
    4.2.124 names a district's BOUNDARY for one reason:
    **बाधकबाधनार्थम्**, to beat what would have beaten it —
    गर्तोत्तरपदाच्छं बाधित्वा वुञेव जनपदावधेर्भवति. The rule it
    reaches for stands thirteen sūtras later.
    """

    def test_the_reason_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.2.124").notes)
        self.assertIn("किमर्थं तर्हि अवधिग्रहणम्", notes)
        self.assertIn("बाधकबाधनार्थम्", notes)
        self.assertIn("गर्तोत्तरपदाच्छं बाधित्वा", notes)

    def test_and_the_rule_it_reaches_for_is_codified(self):
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertTrue(REGISTRY.has("4.2.137"))
        self.assertEqual(provisions_for("4.2.137")[0].gives, "cha")
        self.assertIn("garta", provisions_for("4.2.137")[0].ends_with)

    def test_and_the_row_declares_the_exception(self):
        from src.astadhyayi.sense_taddhita import provisions_for

        boundary = [row for row in provisions_for("4.2.124")
                    if "avadhi" in row.of_samjna]
        self.assertEqual(len(boundary), 1)
        self.assertIn("4.2.137", boundary[0].excepts)


class ListEntriesReadForOtherRules(unittest.TestCase):
    """
    Two gaṇas of this run hold entries that add nothing where they
    stand. 4.2.127's पाथेय is there to make a word a COUNTRY-word for
    4.2.121; 4.2.133's कच्छ and विजापक are there for 4.2.134 and
    because 4.2.132 covered them already.
    """

    def test_the_widening_entry_is_recorded(self):
        notes = unwrapped(REGISTRY.get("4.2.127").notes)
        self.assertIn("सामर्थ्याददेशार्थं ग्रहणम्", notes)
        self.assertIn("अदेशार्थः", notes)
        self.assertTrue(REGISTRY.has("4.2.121"))

    def test_the_forward_looking_entries_are_recorded(self):
        notes = unwrapped(REGISTRY.get("4.2.133").notes)
        self.assertIn("तस्य मनुष्यतत्स्थयोर्वुञर्थः पाठः", notes)
        self.assertIn("इह ग्रहणमुत्तरार्थम्", notes)

    def test_and_the_rules_they_are_read_for_exist(self):
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertEqual(provisions_for("4.2.134")[0].gana, "kacchādi")
        self.assertEqual(provisions_for("4.2.133")[0].gana, "kacchādi")
        self.assertEqual(provisions_for("4.2.132")[0].upadha, "k")

    def test_and_the_later_rule_really_beats_the_list(self):
        """
        कच्छ is in 4.2.133's list and 4.2.133 gives अण्; 4.2.134 must
        take that ground away when a man is meant, or the entry would
        have been read for nothing.
        """
        from src.astadhyayi.sense_taddhita import in_sense

        plain = in_sense(sense="śeṣa", desa=True, gana="kacchādi")
        self.assertEqual(plain.by, "4.2.133")
        self.assertEqual(plain.gives, "aṇ")

        of_a_man = in_sense(sense="śeṣa", gana="kacchādi",
                            result="manuṣya-tatstha")
        self.assertEqual(of_a_man.by, "4.2.134")
        self.assertEqual(of_a_man.gives, "vuñ")


class AnOptionThatWorksForOneWordOnly(unittest.TestCase):
    """
    4.2.130 विभाषा कुरुयुगन्धराभ्याम्. कुरु is in 4.2.133's list and
    takes अण् by that rule whatever this one says, **तत्र वचनादणपि
    भविष्यति** — so **सैषा युगन्धरार्था विभाषा**, the option is
    really for the second word.
    """

    def test_the_reasoning_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.2.130").notes)
        self.assertIn("जनपदशब्दावेतौ", notes)
        self.assertIn("तत्र वचनादणपि भविष्यति", notes)
        self.assertIn("सैषा युगन्धरार्था विभाषा", notes)

    def test_and_the_rule_the_option_is_spoken_against_exists(self):
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertTrue(REGISTRY.has("4.2.125"))
        self.assertIn("4.2.125", provisions_for("4.2.130")[0].excepts)
        self.assertFalse(provisions_for("4.2.125")[0].optional)
        self.assertTrue(provisions_for("4.2.130")[0].optional)

    def test_and_the_fixed_affix_for_a_man_is_untouched(self):
        """
        4.2.134 is not in the option's way: from कुरु the वुञ् stays
        fixed when a man or what stands in him is meant.
        """
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertFalse(provisions_for("4.2.134")[0].optional)
        self.assertIn("कौरवको मनुष्यः",
                      unwrapped(REGISTRY.get("4.2.130").notes))


class ASeventhRangeWithBothEndsStated(unittest.TestCase):
    """
    देश enters at 4.2.119 ओर्देशे and the vṛttis of a dozen later
    rules open with **देश इत्येव**, the last of them on 4.2.145. Two
    case-runs, four sense-runs and this: seven bounded ranges in one
    pāda, where most anuvṛtti in this project has had to be inferred.
    """

    def test_the_range_is_named(self):
        from src.astadhyayi.sense_taddhita import DESA_RUN, desa_run

        self.assertEqual(DESA_RUN, ("4.2.119", "4.2.145"))
        self.assertEqual(desa_run().by, "4.2.119")
        self.assertIn("4.2.145", desa_run().why)

    def test_and_both_ends_are_codified(self):
        for sutra in ("4.2.119", "4.2.145"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))

    def test_every_row_that_carries_desa_lies_inside_it(self):
        from src.astadhyayi.sense_taddhita import DESA_RUN, SENSE_TABLE

        opens, closes = (int(end.rsplit(".", 1)[1]) for end in DESA_RUN)
        for row in SENSE_TABLE:
            if not row.desa:
                continue
            number = int(row.sutra.rsplit(".", 1)[1])
            with self.subTest(sutra=row.sutra):
                self.assertGreaterEqual(number, opens)
                self.assertLessEqual(number, closes)

    def test_and_the_first_rule_of_the_range_names_the_country(self):
        self.assertIn("देश इति किम्",
                      unwrapped(REGISTRY.get("4.2.119").notes))

    def test_and_the_pada_closes_where_the_range_does(self):
        """
        4.2.145 is both the last rule the देश heading reaches and the
        last rule of the pāda, and the Kāśikā says so in its colophon.
        """
        from src.astadhyayi.sense_taddhita import DESA_RUN

        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 2}
        self.assertEqual(max(have), 145)
        self.assertEqual(DESA_RUN[1], "4.2.145")
        self.assertIn("चतुर्थाध्यायस्य द्वितीयः पादः",
                      unwrapped(REGISTRY.get("4.2.145").notes))


if __name__ == "__main__":
    unittest.main()
