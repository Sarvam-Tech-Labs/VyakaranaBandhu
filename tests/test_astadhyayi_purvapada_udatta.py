# -*- coding: utf-8 -*-
"""
Tests for 6.2.64–110 — the accent PLACED in the first member.

Four things carry this stretch.

**A heading whose two words stop in different places.** आदिः governs
to 6.2.91 and उदात्तः to 6.2.137, and 6.2.64's own vṛtti says both.
The pāda did the same at 6.2.1, where प्रकृत्या stopped at 6.2.63 and
पूर्वपदम् ran to 6.2.110 — the same device twice.

**A placement that appears once and nowhere else.** 6.2.83's
अन्त्यात् पूर्वम् — the syllable before the last of the first member.

**A fourth heading opening inside the third.** 6.2.106 turns बहुव्रीहि
into an अधिकार running to 6.2.120.

**And the section is built the other way round from 6.2.1–63.** There
the second member was what nearly every rule named; here the first is
as often, so the score has to weight them the other way and the two
modules cannot share one.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.purvapada_udatta import (
    ADI_RUN, ANTA_RUN, BAHUVRIHI_RUN, PLACED_TABLE, UDATTA_RUN,
    placed_on, placement_runs, provisions_for)
from src.astadhyayi.sutra import REGISTRY


def _order(sutra_id):
    return tuple(int(p) for p in sutra_id.split("."))


class OneHeadingWithTwoDifferentReaches(unittest.TestCase):
    def test_the_placement_word_stops_before_the_accent_word(self):
        self.assertEqual(ADI_RUN[0], UDATTA_RUN[0])
        self.assertLess(_order(ADI_RUN[1]), _order(UDATTA_RUN[1]))

    def test_the_vrtti_bounds_both_in_one_breath(self):
        why = provisions_for("6.2.64")[0].why
        self.assertIn("प्राग् अन्ताधिकारात्", why)
        self.assertIn("प्रकृत्या भगालम् इति यावत्", why)

    def test_the_second_placement_takes_over_where_the_first_stops(self):
        self.assertEqual(_order(ANTA_RUN[0])[2],
                         _order(ADI_RUN[1])[2] + 1)
        self.assertIn("6.2.64", provisions_for("6.2.92")[0].blocks)

    def test_and_the_accent_word_outlives_them_both(self):
        self.assertLess(_order(ANTA_RUN[1]), _order(UDATTA_RUN[1]))

    def test_the_pada_did_the_same_thing_at_its_opening(self):
        """
        6.2.1's प्रकृत्या stopped at 6.2.63 while its पूर्वपदम् ran
        to 6.2.110. The same device twice, and the second time with
        the placement word rather than the scope word.
        """
        from src.astadhyayi.purvapada_svara import (
            PRAKRTYA_RUN, PURVAPADA_RUN)

        self.assertLess(_order(PRAKRTYA_RUN[1]),
                        _order(PURVAPADA_RUN[1]))
        self.assertEqual(PURVAPADA_RUN[1], ANTA_RUN[1])

    def test_the_report_carries_all_four_runs(self):
        answer = placement_runs()
        for named in (ADI_RUN[1], ANTA_RUN[1], UDATTA_RUN[1],
                      BAHUVRIHI_RUN[0]):
            self.assertIn(named, answer.why, named)


class TheTwoPureHeadingsSupplyNothing(unittest.TestCase):
    def test_neither_is_ever_the_answer(self):
        for kwargs in ({}, {"uttarapada": "pura"},
                       {"result": "yukta"}):
            self.assertNotIn(placed_on(**kwargs).sutra,
                             ("6.2.64", "6.2.92"), kwargs)

    def test_but_the_third_heading_is_also_a_rule(self):
        """
        6.2.106 states बहुव्रीहि as a heading AND places an accent
        for विश्व, so it has to stay reachable where the other two
        do not.
        """
        row = provisions_for("6.2.106")[0]
        self.assertTrue(row.heading)
        self.assertTrue(row.of)
        answer = placed_on("viśva", samasa="bahuvrīhi", samjna=True)
        self.assertEqual(answer.sutra, "6.2.106")

    def test_the_two_pure_ones_state_only_where(self):
        for code in ("6.2.64", "6.2.92"):
            row = provisions_for(code)[0]
            self.assertTrue(row.heading, code)
            self.assertEqual(row.of, (), code)
            self.assertEqual(row.uttarapada, (), code)
            self.assertTrue(row.where, code)


class ThreePlacementsAndOneOfThemAppearsOnce(unittest.TestCase):
    def test_all_three_are_present(self):
        places = {r.where for r in PLACED_TABLE if r.where}
        self.assertEqual(places, {"ādi", "anta", "antyāt-pūrva"})

    def test_the_third_is_stated_by_one_rule_only(self):
        odd = [r.sutra for r in PLACED_TABLE
               if r.where == "antyāt-pūrva"]
        self.assertEqual(odd, ["6.2.83"])

    def test_it_displaces_the_rule_before_it_for_a_longer_word(self):
        short = placed_on("kāśa", uttarapada="ja")
        self.assertEqual(short.sutra, "6.2.82")
        self.assertEqual(short.where, "ādi")

        long = placed_on("bahvac", uttarapada="ja")
        self.assertEqual(long.sutra, "6.2.83")
        self.assertEqual(long.where, "antyāt-pūrva")
        self.assertEqual(long.blocked_by, ("6.2.82",))

    def test_and_it_records_the_form_too_short_for_it(self):
        self.assertIn("दग्धजानि",
                      provisions_for("6.2.83")[0].keeps_out)

    def test_the_two_runs_hold_their_own_placements(self):
        first, last = (int(s.split(".")[2]) for s in ADI_RUN)
        for row in PLACED_TABLE:
            n = int(row.sutra.split(".")[2])
            if row.refuses or row.where == "antyāt-pūrva":
                continue
            if first <= n <= last:
                self.assertEqual(row.where, "ādi", row.sutra)
            else:
                self.assertEqual(row.where, "anta", row.sutra)


class AFourthHeadingOpensInsideTheThird(unittest.TestCase):
    def test_it_opens_where_the_vrtti_says(self):
        self.assertEqual(BAHUVRIHI_RUN, ("6.2.106", "6.2.120"))
        self.assertIn("प्राग् अव्ययीभावसंज्ञानात्",
                      provisions_for("6.2.106")[0].why)

    def test_it_opens_inside_the_anta_run(self):
        self.assertLessEqual(_order(ANTA_RUN[0]),
                             _order(BAHUVRIHI_RUN[0]))

    def test_and_it_closes_outside_this_module(self):
        """
        The बहुव्रीहि run reaches 6.2.120 and this table stops at
        6.2.110, so five of its rules belong to the next one.
        """
        held = max(int(r.sutra.split(".")[2]) for r in PLACED_TABLE)
        self.assertEqual(held, 110)
        self.assertGreater(_order(BAHUVRIHI_RUN[1]), _order("6.2.110"))

    def test_every_rule_of_it_inside_this_table_names_the_compound(self):
        for n in range(106, 111):
            row = provisions_for("6.2.%d" % n)[0]
            self.assertEqual(row.samasa, "bahuvrīhi", row.sutra)


class TheSectionIsBuiltTheOtherWayRound(unittest.TestCase):
    """
    6.2.1–63 named the second member almost every time. Here the
    first is as often what a rule turns on — सर्व, विश्व, नदी, पाप, a
    direction-word — so the two tables cannot share one score.
    """

    def test_many_rows_name_a_first_member(self):
        naming_first = [r for r in PLACED_TABLE if r.of]
        self.assertGreaterEqual(len(naming_first), 12)

    def test_two_rules_name_a_first_member_against_one_second(self):
        for code in ("6.2.100", "6.2.101"):
            row = provisions_for(code)[0]
            self.assertEqual(row.uttarapada, ("pura",), code)
            self.assertTrue(row.of, code)

    def test_and_the_first_member_decides_between_them(self):
        self.assertEqual(
            placed_on("ariṣṭa", uttarapada="pura").sutra, "6.2.100")
        self.assertEqual(
            placed_on("hāstina", uttarapada="pura",
                      result="prācām").sutra, "6.2.101")

    def test_a_first_member_neither_names_falls_to_the_general_rule(self):
        self.assertEqual(
            placed_on("kāñcī", uttarapada="pura",
                      result="prācām").sutra, "6.2.99")


class ARefusalNamesWhatItTakesTheAccentFrom(unittest.TestCase):
    def setUp(self):
        self.refusing = [r for r in PLACED_TABLE if r.refuses]

    def test_there_are_two(self):
        self.assertEqual([r.sutra for r in self.refusing],
                         ["6.2.91", "6.2.101"])

    def test_neither_names_itself_and_each_names_an_earlier_rule(self):
        for row in self.refusing:
            self.assertNotIn(row.sutra, row.blocks, row.sutra)
            for blocked in row.blocks:
                self.assertLess(_order(blocked), _order(row.sutra),
                                row.sutra)

    def test_a_refusal_reports_no_placement(self):
        answer = placed_on("bhūta", uttarapada="arma")
        self.assertEqual(answer.sutra, "6.2.91")
        self.assertEqual(answer.where, "")
        self.assertEqual(answer.blocked_by, ("6.2.90",))

    def test_and_it_does_not_govern_what_it_excepts(self):
        elsewhere = placed_on("datta", uttarapada="arma")
        self.assertEqual(elsewhere.sutra, "6.2.90")
        self.assertEqual(elsewhere.where, "ādi")

    def test_asking_for_a_placement_returns_the_rule_that_gives_it(self):
        """
        A refusal is never offered as a giver. Ask which rule PLACES
        the accent here and the answer is 6.2.90, which does; ask
        what happens and the answer is 6.2.91, which takes it away.
        Two questions, two right answers, and the second is the one
        the reader wants.
        """
        gives = placed_on("bhūta", uttarapada="arma", wants="ādi")
        self.assertEqual(gives.sutra, "6.2.90")
        happens = placed_on("bhūta", uttarapada="arma")
        self.assertEqual(happens.sutra, "6.2.91")
        self.assertEqual(happens.where, "")


class OneRuleWinsAgainstALaterOneByStandingFirst(unittest.TestCase):
    """
    6.2.86 and 6.2.123 both reach छात्रिशालम्, and the vṛtti settles
    it by पूर्वविप्रतिषेध — the earlier rule takes it. Recorded on
    `blocks`, with the later rule's number.
    """

    def test_the_rule_it_beats_comes_after_it(self):
        row = provisions_for("6.2.86")[0]
        self.assertEqual(row.blocks, ("6.2.123",))
        self.assertGreater(_order(row.blocks[0]), _order(row.sutra))

    def test_the_note_names_the_principle(self):
        self.assertIn("पूर्वविप्रतिषेधेन",
                      provisions_for("6.2.86")[0].why)

    def test_and_the_rule_it_beats_is_now_there_to_be_beaten(self):
        """
        6.2.123 is codified, so the claim stops being about an
        absence. It answers for शाला in a neuter तत्पुरुष and puts
        the accent on the SECOND member's first syllable — which is
        exactly the accent 6.2.86 takes छात्रिशालम् away from, by
        being the earlier rule.
        """
        from src.astadhyayi.uttarapada_svara import second_member

        got = second_member("śālā", samasa="tatpuruṣa",
                            result="napuṃsaka")
        self.assertEqual(got.sutra, "6.2.123")
        self.assertEqual(got.where, "ādi")
        self.assertEqual(provisions_for("6.2.86")[0].blocks,
                         ("6.2.123",))


class WhatARuleExceptsIsHeldSeparately(unittest.TestCase):
    def test_several_rows_except_by_name(self):
        excepting = [r.sutra for r in PLACED_TABLE if r.excludes]
        self.assertGreaterEqual(len(excepting), 6)

    def test_an_excepted_word_takes_the_rule_away(self):
        self.assertEqual(
            placed_on("indra", uttarapada="prastha").sutra, "6.2.87")
        self.assertEqual(
            placed_on("vṛddha", uttarapada="prastha").sutra, "")

    def test_and_the_next_rule_exists_for_exactly_what_was_excepted(self):
        self.assertIn("वृद्धार्थ आरम्भः",
                      provisions_for("6.2.88")[0].why)
        self.assertEqual(provisions_for("6.2.88")[0].blocks,
                         ("6.2.87",))

    def test_each_such_rule_records_the_form_it_keeps_out(self):
        for row in PLACED_TABLE:
            if row.excludes:
                self.assertGreater(len(row.keeps_out), 10, row.sutra)


class TheSectionIsWhereItSaysItIs(unittest.TestCase):
    def test_the_rows_are_the_forty_seven(self):
        held = sorted(r.sutra for r in PLACED_TABLE)
        self.assertEqual(held,
                         sorted("6.2.%d" % n for n in range(64, 111)))

    def test_every_rule_here_is_registered_against_this_resolver(self):
        for row in PLACED_TABLE:
            self.assertEqual(REGISTRY.get(row.sutra).apply.__name__,
                             "placed_on", row.sutra)

    def test_the_pada_is_contiguous_as_far_as_it_goes(self):
        for n in range(1, 111):
            self.assertTrue(REGISTRY.has("6.2.%d" % n), n)


class NothingAnswersByDefault(unittest.TestCase):
    def test_an_unreached_question_gets_nothing(self):
        answer = placed_on(uttarapada="hasta")
        self.assertEqual(answer.sutra, "")
        self.assertEqual(answer.where, "")

    def test_and_the_message_names_the_rule_that_stands_instead(self):
        self.assertIn("6.1.223", placed_on(uttarapada="hasta").why)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in PLACED_TABLE:
            self.assertGreater(len(row.why), 100, row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in PLACED_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_rest_of_the_pada_has_landed(self):
        """
        6.2.111 उत्तरपदादिः takes the second member and the whole
        rest of the pāda — आ पादपरिसमाप्तेः. The shortfall this was
        written as is paid, and the claim is now the join: this
        module's अन्तः stops at 6.2.110 and the next run starts at
        6.2.111.
        """
        from src.astadhyayi.uttarapada_svara import UTTARAPADA_RUN

        self.assertTrue(REGISTRY.has("6.2.111"))
        self.assertTrue(REGISTRY.has("6.2.199"))
        self.assertEqual(ANTA_RUN[1], "6.2.110")
        self.assertEqual(UTTARAPADA_RUN, ("6.2.111", "6.2.199"))

    def test_the_three_rules_these_notes_lean_on_have_landed(self):
        """
        6.2.121 bounds the बहुव्रीहि run, and 6.2.167 and 6.2.172
        are what 6.2.110 and 6.2.108 give way to. All three are
        codified, so each citation is now checked against the rule
        rather than against its absence — and 6.2.121's bound is
        checked by arithmetic: the run stops one sūtra before it.
        """
        from src.astadhyayi.uttarapada_svara import second_member

        self.assertIn("6.2.167", provisions_for("6.2.110")[0].why)
        self.assertIn("6.2.172", provisions_for("6.2.108")[0].blocks)
        self.assertEqual(
            second_member("mukha", result="svāṅga",
                          samasa="bahuvrīhi").sutra, "6.2.167")
        self.assertEqual(
            second_member(purvapada="nañ", samasa="bahuvrīhi").sutra,
            "6.2.172")
        self.assertEqual(_order(BAHUVRIHI_RUN[1])[2] + 1,
                         _order("6.2.121")[2])

    def test_the_module_does_not_count_syllables(self):
        """
        6.2.83's *many vowels* and 6.2.90's *two or three* are
        conditions the query carries, not ones the code works out —
        so a first member the caller does not describe reaches
        neither.
        """
        self.assertEqual(placed_on("upasara", uttarapada="ja").sutra,
                         "")
        self.assertEqual(placed_on("bahvac", uttarapada="ja").sutra,
                         "6.2.83")


if __name__ == "__main__":
    unittest.main()
