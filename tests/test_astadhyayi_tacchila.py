# -*- coding: utf-8 -*-
"""
3.2.134 to 3.2.140 — habit, office, and doing well.

3.2.134 आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु is the pāda's second
heading and the first whose extent is given by NAMING its last rule
rather than by a number.

What this block asserts that no earlier one could:

  * a heading bounded by a rule-name, inclusive at both ends;
  * a running condition read from the NEXT rule's निवृत्ति, without
    which one root lost a form;
  * three senses conferred together, none of them an input, because
    no rule of the run divides on which.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.tacchila import (
    ALAMKRNADI, GLADI, TACCHILA, TACCHILA_FROM, TACCHILA_SENSES,
    TACCHILA_THROUGH, TRASADI, provisions_for, tacchila_affix,
    tacchila_heading,
)
from src.astadhyayi.upapada_krt import Added, NotAdded


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.135", "tṛn", dict(root="kṛ")),
        ("3.2.136", "iṣṇuc", dict(root="sah")),
        ("3.2.137", "iṣṇuc", dict(root="dhṛ", causative=True,
                                  chandasi=True)),
        ("3.2.138", "iṣṇuc", dict(root="bhū", chandasi=True)),
        ("3.2.139", "ksnu", dict(root="ji")),
        ("3.2.140", "knu", dict(root="gṛdh")),
    )

    def test_every_rule_of_the_run_answers_for_itself(self):
        for sutra, gives, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = tacchila_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_the_widest_rule_reaches_a_root_no_other_does(self):
        """सर्वधातुभ्यः — and everything after it is narrower."""
        from src.astadhyayi.tacchila import _how_specific

        self.assertEqual(tacchila_affix(root="pac").by, "3.2.135")
        self.assertEqual(_how_specific(provisions_for("3.2.135")[0]), 0)

    def test_every_named_root_of_a_list_rule_is_reached(self):
        for group, sutra in ((ALAMKRNADI, "3.2.136"),
                             (TRASADI, "3.2.140")):
            for root in group:
                with self.subTest(sutra=sutra, root=root):
                    self.assertEqual(
                        tacchila_affix(root=root).by, sutra)

    def test_3_2_139_reaches_its_three_and_the_one_its_ca_adds(self):
        """ग्लास्नुः, जिष्णुः, स्थास्नुः — and भूष्णुः by the च."""
        self.assertEqual(GLADI, ("glā", "ji", "sthā", "bhū"))
        for root in GLADI:
            with self.subTest(root=root):
                self.assertEqual(
                    tacchila_affix(root=root).by, "3.2.139")


class AHeadingBoundedByARuleName(unittest.TestCase):
    """
    आ क्वेः — as far as the क्विप् of 3.2.177, and अभिविधौ चायम् आङ्,
    the आ inclusive. The first heading in this project whose end is
    given by naming its last rule rather than by a number.
    """

    def test_it_adds_nothing(self):
        self.assertEqual(tacchila_heading().gives, "")
        self.assertEqual(tacchila_heading().by, "3.2.134")

    def test_it_covers_from_itself_to_the_rule_it_names(self):
        self.assertEqual((TACCHILA_FROM, TACCHILA_THROUGH), (134, 177))
        for sutra in ("3.2.134", "3.2.140", "3.2.177"):
            with self.subTest(sutra=sutra):
                self.assertEqual(tacchila_heading(sutra).by, "3.2.134")

    def test_and_stops_on_both_sides(self):
        for sutra in ("3.2.133", "3.2.178", "3.3.1"):
            with self.subTest(sutra=sutra):
                self.assertIsInstance(
                    tacchila_heading(sutra), NotAdded)

    def test_the_rows_under_the_heading_fall_under_it(self):
        """The table and the heading do NOT have the same extent, and the
        difference is worth keeping. 3.2.178 to 3.2.186 live in this
        module because they are affix rules of like shape — a choice
        about where code goes. आ क्वेः ends at 3.2.177 — a fact about
        the text. These tests once asserted the two coincide.

        The vṛtti muddies it further: at 3.2.178 it still says
        ताच्छीलिकेषु, reading the senses as continuing past the point
        the heading formally stops. Recorded rather than resolved."""
        under = [r for r in TACCHILA
                 if TACCHILA_FROM
                 <= int(r.sutra.rsplit(".", 1)[1]) <= TACCHILA_THROUGH]
        self.assertTrue(under)
        for row in under:
            with self.subTest(sutra=row.sutra):
                self.assertEqual(
                    tacchila_heading(row.sutra).by, "3.2.134")

        beyond = [r for r in TACCHILA
                  if int(r.sutra.rsplit(".", 1)[1]) > TACCHILA_THROUGH]
        self.assertTrue(beyond, "the table should hold rules past the "
                                "heading — 3.2.178 onward")
        for row in beyond:
            with self.subTest(sutra=row.sutra, outside=True):
                self.assertNotEqual(
                    tacchila_heading(row.sutra).by, "3.2.134")

    def test_the_far_end_is_real_and_the_span_is_closed(self):
        """
        A span is only a span if its ends exist. This stood as a debt
        while 3.2.177 was unread — the heading names that rule rather
        than a number, so its extent could be stated but not checked.

        Reading the rest of the heading paid it, and the test went red,
        which is what a debt written as a test is for. Both ends are
        now real, and every rule between them is codified.
        """
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        for n in range(TACCHILA_FROM, TACCHILA_THROUGH + 1):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertIn("3.2.%d" % n, have)


class ThreeSensesConferredTogether(unittest.TestCase):
    """
    तच्छील, तद्धर्म and तत्साधुकारिन्. The vṛtti separates them —
    habit, office, doing well — and the interesting pair is the first
    two: a man may have the duty without the inclination.

    None of them is an input, because no rule of the run divides on
    which. That is a fact about the run and worth asserting: a caller
    given a choice the grammar does not offer would be misled.
    """

    def test_the_three_are_named_in_the_vrttis_order(self):
        self.assertEqual(
            TACCHILA_SENSES,
            ("tacchīla", "taddharma", "tatsādhukārin"))

    def test_no_rule_of_the_run_divides_on_the_headings_three(self):
        """
        Narrowed from what it first said. The original claim was that
        no row states a sense at all, and that held only while
        3.2.135-140 were the whole run: 3.2.148 and 3.2.151 reach by
        the ROOT's meaning — motion, sound, anger, adorning — which is
        a different question from the three the heading confers.

        What holds, and what the test was always about, is that none
        of तच्छील, तद्धर्म and तत्साधुकारिन् is ever a condition. They
        are conferred together on everything under the heading, so
        there is nothing for a caller to choose between.
        """
        stated = {r.sense for r in TACCHILA if r.sense}
        for sense in TACCHILA_SENSES:
            with self.subTest(sense=sense):
                self.assertNotIn(sense, stated)
        # and the senses that ARE stated are about the root's meaning
        self.assertEqual(stated, {"calana-śabda", "krodha-bhūṣā"})

    def test_and_the_heading_records_the_distinction(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.134").notes
        self.assertIn("स्वभावतः", notes)
        self.assertIn("स्वधर्मे", notes)
        self.assertIn("साधु करोति", notes)


class AConditionReadFromTheNextRule(unittest.TestCase):
    """
    3.2.137's छन्दसि runs on into 3.2.138 and stops only at 3.2.139,
    which says so itself — छन्दसीति निवृत्तम्. The condition on
    3.2.138 is therefore knowable only by reading FORWARD.
    """

    def test_the_same_root_divides_by_register(self):
        """भविष्णुः in the Veda, भूष्णुः outside."""
        vedic = tacchila_affix(root="bhū", chandasi=True)
        ordinary = tacchila_affix(root="bhū")
        self.assertEqual((vedic.by, vedic.gives), ("3.2.138", "iṣṇuc"))
        self.assertEqual((ordinary.by, ordinary.gives),
                         ("3.2.139", "ksnu"))

    def test_and_without_the_condition_one_form_was_lost(self):
        """
        3.2.138 and 3.2.139 both name भू and state the same amount
        otherwise, so they tied and the earlier row won on table
        order. The condition is what separates them.
        """
        self.assertTrue(provisions_for("3.2.138")[0].chandasi)
        self.assertFalse(provisions_for("3.2.139")[0].chandasi)
        self.assertIn("bhū", provisions_for("3.2.138")[0].of)
        self.assertIn("bhū", provisions_for("3.2.139")[0].of)

    def test_the_reason_is_recorded_where_it_can_be_found(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("छन्दसि विषये", REGISTRY.get("3.2.138").notes)
        self.assertIn("निवृत्तम्", REGISTRY.get("3.2.139").notes)


class TheCommentaryTeachesAsWellAsExplains(unittest.TestCase):
    """
    3.2.139's marker is ग and not क, and the vṛtti draws three
    consequences from that — then puts all three into a verse. The
    first कारिका this project has met in the Kāśikā.
    """

    def test_the_verse_and_its_three_consequences_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.139").notes
        self.assertIn("गिच् चायं प्रत्ययः, न कित्", notes)
        self.assertIn("क्स्नोर्गित्त्वान्न", notes)
        self.assertIn("1.1.5", notes)
        self.assertIn("7.2.11", notes)


class TheConditionsOfThisRunAreLive(unittest.TestCase):

    def test_the_causative_rule_needs_its_causative(self):
        self.assertEqual(
            tacchila_affix(root="dhṛ", causative=True,
                           chandasi=True).by, "3.2.137")
        self.assertNotEqual(
            tacchila_affix(root="dhṛ", chandasi=True).by, "3.2.137")

    def test_and_silence_about_a_condition_refuses_nothing(self):
        """
        3.2.135 says nothing of the Veda or the causative, so it must
        still answer where either is asserted — the one-way reading
        3.2.39 established.
        """
        self.assertEqual(
            tacchila_affix(root="pac", chandasi=True).by, "3.2.135")
        self.assertEqual(
            tacchila_affix(root="pac", causative=True).by, "3.2.135")

    def test_this_run_declares_no_reuse(self):
        from src.astadhyayi.sutra import REGISTRY

        for n in range(134, 141):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(REGISTRY.get("3.2.%d" % n).reuses, ())


if __name__ == "__main__":
    unittest.main()
