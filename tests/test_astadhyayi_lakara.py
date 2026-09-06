# -*- coding: utf-8 -*-
"""
3.2.110 to 3.2.122 — which tense-ending comes, and when.

These are a SIXTH kind of rule in this pāda. They add no कृत् affix;
they choose a लकार, and their conditions are about time and about the
situation of speaking — whether it happened today, whether the speaker
saw it, whether a question is being asked or answered.

What this block asserts that no earlier one could:

  * a rule giving the FUTURE ending for a past act, because what was
    remembered was future to the remembering;
  * two pairs of rules taking OPPOSITE sides of one condition, which
    is why परोक्ष and साकाङ्क्ष are tri-state and not flags;
  * a condition that reaches a rule by LEAPING over the ones between.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.lakara import (
    ABHIJNA, LAKARA, lakara_for, provisions_for,
)
from src.astadhyayi.upapada_krt import Added


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.110", "luṅ", dict()),
        ("3.2.111", "laṅ", dict(anadyatana=True)),
        ("3.2.112", "lṛṭ", dict(beside="abhijānāsi", anadyatana=True)),
        ("3.2.114", "lṛṭ", dict(beside="abhijānāsi", anadyatana=True,
                                sakanksa=True)),
        ("3.2.115", "liṭ", dict(anadyatana=True, paroksa=True)),
        ("3.2.116", "laṅ", dict(beside="ha", anadyatana=True,
                                paroksa=True)),
        ("3.2.117", "laṅ", dict(anadyatana=True, paroksa=True,
                                question=True, recent=True)),
        ("3.2.118", "laṭ", dict(beside="sma", anadyatana=True,
                                paroksa=True)),
        ("3.2.119", "laṭ", dict(beside="sma", anadyatana=True)),
        ("3.2.120", "laṭ", dict(beside="nanu", answer=True)),
        ("3.2.121", "laṭ", dict(beside="na", answer=True)),
        ("3.2.122", "luṅ", dict(beside="purā", anadyatana=True)),
    )

    def test_every_giving_rule_answers_for_itself(self):
        for sutra, ending, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = lakara_for(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, ending)

    def test_the_widest_rule_states_the_least(self):
        """लुङ् for the past at large, and everything after narrows."""
        from src.astadhyayi.lakara import _how_specific

        self.assertEqual(_how_specific(provisions_for("3.2.110")[0]), 0)

    def test_all_four_synonyms_of_remembering_are_reached(self):
        """वचनग्रहणं पर्यायार्थम् — स्मरसि, बुध्यसे, चेतयसे too."""
        self.assertEqual(len(ABHIJNA), 4)
        for word in ABHIJNA:
            with self.subTest(word=word):
                self.assertEqual(
                    lakara_for(beside=word, anadyatana=True).by,
                    "3.2.112")


class TheFutureEndingForAPastAct(unittest.TestCase):
    """
    Every rule here stands under 3.2.84 भूते, so the act is past — and
    3.2.112 gives लृट्, the future ending. What was remembered was
    future to the remembering.
    """

    def test_the_ending_is_the_future_one(self):
        answer = lakara_for(beside="abhijānāsi", anadyatana=True)
        self.assertEqual(answer.gives, "lṛṭ")

    def test_and_every_rule_of_the_run_is_under_the_past_heading(self):
        from src.astadhyayi.upapada_krt import (
            BHUTE_FROM, BHUTE_THROUGH, bhute_heading,
        )

        # Scoped to the pāda the heading belongs to. 3.3.140 भूते च is
        # of the past too and is NOT under 3.2.84 — a time is not a
        # heading, and this test read one as the other for as long as
        # 3.2 held the only past rules.
        past = [r for r in LAKARA
                if r.time == "bhūta" and r.sutra.startswith("3.2.")]
        self.assertTrue(past)
        for row in past:
            with self.subTest(sutra=row.sutra):
                number = int(row.sutra.rsplit(".", 1)[1])
                self.assertTrue(BHUTE_FROM <= number <= BHUTE_THROUGH)
                self.assertEqual(bhute_heading(row.sutra).by, "3.2.84")

        elsewhere = [r for r in LAKARA
                     if r.time == "bhūta"
                     and not r.sutra.startswith("3.2.")]
        self.assertTrue(
            elsewhere,
            "3.3.140 is of the past and outside the heading")
        for row in elsewhere:
            with self.subTest(sutra=row.sutra, outside=True):
                self.assertNotEqual(
                    bhute_heading(row.sutra).by, "3.2.84")

        # And nothing outside the past is under it. 3.2.123 वर्तमाने
        # is the first such rule — which is where the heading was said
        # to stop, so that boundary is the text's own — and the future
        # rules of 3.3 are outside it too, being in another pāda
        # altogether. The times PARTITION the table; no count of them
        # is asserted, because this table has now grown twice.
        outside = [r for r in LAKARA if r.time != "bhūta"]
        self.assertTrue(outside)
        for row in outside:
            with self.subTest(sutra=row.sutra, time=row.time):
                self.assertNotEqual(
                    bhute_heading(row.sutra).by, "3.2.84")

        self.assertIn("3.2.123", [r.sutra for r in outside])
        self.assertEqual(
            {r.time for r in LAKARA} - {"bhūta"},
            {r.time for r in outside})


class APratisedhaThatDoesNotGovern(unittest.TestCase):
    """
    3.2.113 न यदि refuses what 3.2.112 gave. What those sentences take
    instead is 3.2.111's लङ् — अवसाम and not *वत्स्यामः — so that is
    the rule reported and the refusal rides alongside.
    """

    def test_the_supplier_is_named_and_the_refusal_carried(self):
        answer = lakara_for(beside="abhijānāsi", anadyatana=True,
                            with_yad=True)
        self.assertEqual((answer.by, answer.gives), ("3.2.111", "laṅ"))
        self.assertEqual(answer.blocked_by, "3.2.113")

    def test_without_yad_the_future_ending_stands(self):
        answer = lakara_for(beside="abhijānāsi", anadyatana=True)
        self.assertEqual(answer.by, "3.2.112")
        self.assertEqual(answer.blocked_by, "")

    def test_it_is_the_only_pratisedha_of_the_run(self):
        self.assertEqual([r.sutra for r in LAKARA if r.refuses],
                         ["3.2.113"])


class TwoConditionsWithThreeStates(unittest.TestCase):
    """
    परोक्ष and साकाङ्क्ष each have two rules on opposite sides, so
    neither can be a flag: a rule may require the condition, require
    its ABSENCE, or say nothing at all.
    """

    def test_parokse_is_required_by_one_rule_and_refused_by_another(self):
        self.assertTrue(provisions_for("3.2.115")[0].paroksa)
        self.assertIs(provisions_for("3.2.119")[0].paroksa, False)
        self.assertIsNone(provisions_for("3.2.110")[0].paroksa)

    def test_and_both_answer_where_they_should(self):
        """
        3.2.118 and 3.2.119 share the companion स्म and differ only in
        this, so they are the sharpest witness the run has.
        """
        unseen = lakara_for(beside="sma", anadyatana=True, paroksa=True)
        seen = lakara_for(beside="sma", anadyatana=True)
        self.assertEqual(unseen.by, "3.2.118")
        self.assertEqual(seen.by, "3.2.119")
        self.assertEqual(unseen.gives, seen.gives)

    def test_sakanksa_likewise(self):
        """
        3.2.113 refuses only where nothing further is expected — the
        vṛtti says so itself: वासमात्रं स्मर्यते, न त्वपरं किंचिल्
        लक्ष्यते, तेन उत्तरसूत्रस्य नायं विषयः. With expectancy,
        3.2.114's option holds even alongside यद्.
        """
        self.assertIs(provisions_for("3.2.113")[0].sakanksa, False)
        self.assertTrue(provisions_for("3.2.114")[0].sakanksa)

        blocked = lakara_for(beside="abhijānāsi", anadyatana=True,
                             with_yad=True)
        allowed = lakara_for(beside="abhijānāsi", anadyatana=True,
                             with_yad=True, sakanksa=True)
        self.assertEqual(blocked.by, "3.2.111")
        self.assertEqual(allowed.by, "3.2.114")

    def test_and_3_2_114_holds_without_yad_too(self):
        """यदीति नानुवर्तते, उभयत्र विभाषेयम्."""
        self.assertIsNone(provisions_for("3.2.114")[0].with_yad)
        self.assertEqual(
            lakara_for(beside="abhijānāsi", anadyatana=True,
                       sakanksa=True).by, "3.2.114")


class AConditionThatArrivesByLeaping(unittest.TestCase):
    """
    3.2.122's अनद्यतनग्रहणम् इह मण्डूकप्लुत्या अनुवर्तते — the
    condition comes down from 3.2.111 by LEAPING over the rules
    between, which had let it go. The first मण्डूकप्लुति the project
    has met.
    """

    def test_the_rule_carries_the_condition_that_leapt_to_it(self):
        self.assertTrue(provisions_for("3.2.122")[0].anadyatana)
        self.assertEqual(
            lakara_for(beside="purā", anadyatana=True).by, "3.2.122")
        self.assertNotEqual(
            lakara_for(beside="purā").by, "3.2.122")

    def test_the_rules_it_leapt_over_do_not_carry_it(self):
        """
        3.2.120 and 3.2.121 dropped अनद्यतन — अनद्यतने परोक्षे इति
        निवृत्तम् — which is exactly what makes the arrival at 3.2.122
        a leap rather than a flow.
        """
        for sutra in ("3.2.120", "3.2.121"):
            with self.subTest(sutra=sutra):
                self.assertIsNone(provisions_for(sutra)[0].anadyatana)

    def test_the_leap_is_recorded_where_a_reader_will_find_it(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("मण्डूकप्लुत्या", REGISTRY.get("3.2.122").notes)


class ARuleThatNamesACompanionToRefuseIt(unittest.TestCase):
    """
    3.2.122's अस्मे — with स्म it is 3.2.118's rule instead. The second
    of this shape in the pāda, after 3.2.58's अनुदके.
    """

    def test_pura_is_reached_and_sma_is_not(self):
        self.assertEqual(
            lakara_for(beside="purā", anadyatana=True).by, "3.2.122")
        self.assertNotEqual(
            lakara_for(beside="sma", anadyatana=True).by, "3.2.122")

    def test_the_refusal_is_held_in_its_own_field(self):
        row = provisions_for("3.2.122")[0]
        self.assertEqual(row.not_beside, ("sma",))
        self.assertEqual(row.beside, ("purā",))


class TheRulesThatGiveTwoEndings(unittest.TestCase):
    """
    3.2.116 and 3.2.117 give two by their च; 3.2.122 gives two by
    विभाषा. All three carry the second on `also`, as the कृत् rules
    that give two affixes do.
    """

    def test_both_endings_are_reported(self):
        for where, first, second in (
            (dict(beside="ha", anadyatana=True, paroksa=True),
             "laṅ", "लिट्"),
            (dict(anadyatana=True, paroksa=True, question=True,
                  recent=True), "laṅ", "लिट्"),
            (dict(beside="purā", anadyatana=True), "luṅ", "लट्"),
        ):
            with self.subTest(**where):
                answer = lakara_for(**where)
                self.assertEqual(answer.gives, first)
                self.assertEqual(answer.also, second)

    def test_and_where_neither_option_is_taken_others_still_come(self):
        """
        ताभ्यां मुक्ते पक्षे यथाविषयम् अन्येऽपि प्रत्यया भवन्ति —
        अवसन्, ऊषुः. So 3.2.122 offers two and forbids nothing.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("अन्येऽपि प्रत्यया", REGISTRY.get("3.2.122").notes)


class TheDebtThisRunRecords(unittest.TestCase):
    """
    These rules name their endings as strings because nothing here can
    ask what an ending IS. What a लकार is, and what it becomes, is
    settled in 3.4 — none of which is codified.
    """

    def test_all_three_lakara_debts_are_paid(self):
        """
        ALL THREE PAID. 3.4.6 gives the Vedic set for any time; 3.4.69
        says what a लकार DENOTES; 3.4.77 enumerates the ten and says
        which are टित्.

        NORTH_STAR carried these from 3.2.110, where the table began
        naming its endings as bare strings. What the last of them buys
        is a check nothing could run before — every ending the table
        gives, across three pādas, against the rule that lists them.
        """
        from src.astadhyayi.lakara import LAKARA, LAKARA_LIST
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        for sutra in ("3.4.6", "3.4.69", "3.4.77"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, have)

        ten = {name for name, _ in LAKARA_LIST}
        given = {row.gives for row in LAKARA}
        self.assertTrue(given)
        self.assertEqual(given - ten, set())

    def test_and_a_lakara_now_has_a_meaning_and_a_form(self):
        from src.astadhyayi.denoted import lakara_denotes
        from src.astadhyayi.lakara import TIN

        self.assertEqual(lakara_denotes(), ("karman", "kartṛ"))
        self.assertEqual(lakara_denotes(akarmaka=True),
                         ("bhāva", "kartṛ"))
        self.assertEqual(len(TIN), 18)
    def test_and_the_rule_that_cited_it_can_now_be_checked(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.4.6", REGISTRY.get("3.2.105").notes)
        self.assertEqual(
            REGISTRY.get("3.4.6").apply.__name__, "lakara_for")
    def test_and_the_module_says_so(self):
        import src.astadhyayi.lakara as module

        self.assertIn("DEBT", module.__doc__)
        self.assertIn("3.4.77", module.__doc__)

    def test_this_run_declares_no_reuse(self):
        from src.astadhyayi.sutra import REGISTRY

        for n in range(110, 123):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(REGISTRY.get("3.2.%d" % n).reuses, ())


class TheKindsOfRulePartitionThePada(unittest.TestCase):
    """
    The pāda needs several entry points — a rule with conditions, a
    fixed word, a heading, a संज्ञा, a substitution, a tense-ending
    — and the count keeps growing as the reading goes on. What is
    asserted is not the count but that they PARTITION: a rule
    between two kinds, or in none, would sit unread and look
    finished.
    """

    def test_the_kinds_are_disjoint_and_cover_the_pada(self):
        from src.astadhyayi.sutra import REGISTRY

        registered = {str(x.id) for x in REGISTRY.all()
                      if str(x.id).startswith("3.2.")}
        by_apply = {}
        for x in REGISTRY.all():
            if not str(x.id).startswith("3.2."):
                continue
            by_apply.setdefault(x.apply.__name__, set()).add(str(x.id))

        # The set of NAMES is not asserted. It was, and it went stale
        # the moment a seventh and eighth entry point arrived — the
        # same failure a hardcoded range kept producing. What matters
        # is not how many kinds there are but that they PARTITION:
        # every registered sūtra in exactly one, none in two, none in
        # none. That property survives the pāda growing.
        self.assertGreater(len(by_apply), 1)
        seen = set()
        for ids in by_apply.values():
            self.assertEqual(seen & ids, set())
            seen |= ids
        self.assertEqual(seen, registered)

    def test_the_lakara_rules_are_exactly_this_run(self):
        from src.astadhyayi.sutra import REGISTRY

        mine = {str(x.id) for x in REGISTRY.all()
                if x.apply is lakara_for}
        # No range named: the run grew by one when the present was
        # read, and it will grow again. What holds is that the rules
        # answering from this entry point are exactly the rows in its
        # own table.
        self.assertEqual(mine, {r.sutra for r in LAKARA})
        self.assertTrue(mine)

    def test_nothing_of_the_past_falls_through_this_run(self):
        """
        Written expecting a nameless refusal, and there is none to
        have: 3.2.110 states NO condition at all, so it catches every
        past situation whatever. That is a real property of the run
        and not a gap — everything after 3.2.110 narrows, and the
        widest rule is the floor.

        The only way an answer here can name a rule other than the one
        that matched is 3.2.113's प्रतिषेध, and even that lands on a
        supplier rather than on nothing.
        """
        for where in (dict(beside="kumbha", question=True),
                      dict(beside="", sakanksa=True),
                      dict(recent=True, answer=True)):
            with self.subTest(**where):
                answer = lakara_for(**where)
                self.assertIsInstance(answer, Added)
                self.assertTrue(answer.by)

    def test_and_the_only_refusal_still_names_a_supplier(self):
        answer = lakara_for(beside="abhijānāsi", anadyatana=True,
                            with_yad=True)
        self.assertIsInstance(answer, Added)
        self.assertEqual(answer.blocked_by, "3.2.113")


if __name__ == "__main__":
    unittest.main()
