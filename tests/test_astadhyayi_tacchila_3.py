# -*- coding: utf-8 -*-
"""
3.2.156 to 3.2.177 — the rest of the heading, and its last rule.

Completing this run closes 3.2.134's span from both ends, since that
heading names 3.2.177 rather than a number as its far edge.

What this block asserts that no earlier one could:

  * a rule that exists BECAUSE a principle is suspended, closing an
    argument opened thirty-one sūtras earlier;
  * two rules corroborating each other across fourteen, the forms of
    one being the evidence the other appealed to;
  * conditions about a STEM already built rather than about the root;
  * a question settled स्वभावात्, from the nature of the case rather
    than from anything the text states.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.tacchila import (
    BHRAJADI, NAMYADI, TACCHILA, TACCHILA_FROM, TACCHILA_THROUGH,
    provisions_for, tacchila_affix, tacchila_heading,
)
from src.astadhyayi.upapada_krt import Added


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.156", "ini", dict(root="ju", upasarga="pra")),
        ("3.2.157", "ini", dict(root="ji")),
        ("3.2.158", "āluc", dict(root="day")),
        ("3.2.159", "ru", dict(root="dheṭ")),
        ("3.2.160", "kmarac", dict(root="ghas")),
        ("3.2.161", "ghurac", dict(root="bhañj")),
        ("3.2.162", "kurac", dict(root="vid")),
        ("3.2.163", "kvarap", dict(root="iṇ")),
        ("3.2.164", "kvarap", dict(root="gam")),
        ("3.2.165", "ūka", dict(root="jāgṛ")),
        ("3.2.166", "ūka", dict(root="yaj", yan_anta=True)),
        ("3.2.167", "ra", dict(root="kam")),
        ("3.2.168", "u", dict(root="bhikṣ", san_anta=True)),
        ("3.2.169", "u", dict(root="iṣ")),
        ("3.2.170", "u", dict(kya_anta=True, chandasi=True)),
        ("3.2.171", "kikin", dict(root="gam", chandasi=True)),
        ("3.2.172", "najiṅ", dict(root="svap")),
        ("3.2.173", "āru", dict(root="vand")),
        ("3.2.174", "kru", dict(root="bhī")),
        ("3.2.175", "varac", dict(root="īś")),
        ("3.2.176", "varac", dict(root="yā", yan_anta=True)),
        ("3.2.177", "kvip", dict(root="vidyut")),
    )

    def test_every_rule_of_the_run_answers_for_itself(self):
        for sutra, gives, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                # Named by affix: this run shares roots freely, so a
                # rule is reached by saying which affix is wanted.
                answer = tacchila_affix(wants=gives, **where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_all_eight_of_the_last_rules_roots_are_reached(self):
        """
        Asked by AFFIX, because several of these roots are named by
        other rules of the run too — भास् by 3.2.161, जु by 3.2.156.
        Sharing is the norm here, and a per-rule claim that ignores it
        is simply false.
        """
        for root in BHRAJADI:
            with self.subTest(root=root):
                self.assertEqual(
                    tacchila_affix(root=root, wants="kvip").by,
                    "3.2.177")

    def test_all_seven_of_3_2_167s_are_too(self):
        for root in NAMYADI:
            with self.subTest(root=root):
                self.assertEqual(
                    tacchila_affix(root=root, wants="ra").by,
                    "3.2.167")


class TheHeadingIsClosedFromBothEnds(unittest.TestCase):
    """
    3.2.134's आ क्वेः names 3.2.177 as its far edge rather than giving
    a number. While that rule was unread the extent could be stated
    but not checked; reading it closes the span.
    """

    def test_every_rule_the_heading_covers_is_codified(self):
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        for n in range(TACCHILA_FROM, TACCHILA_THROUGH + 1):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertIn("3.2.%d" % n, have)

    def test_and_the_named_edge_is_the_rule_it_names(self):
        self.assertEqual(TACCHILA_THROUGH, 177)
        self.assertEqual(tacchila_heading("3.2.177").by, "3.2.134")

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

    def test_the_general_rule_it_leans_on_is_codified(self):
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        for sutra in ("3.2.75", "3.2.76", "3.1.94", "3.2.146"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, have)

    def test_the_argument_is_recorded_with_both_of_its_ends(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.177").notes
        self.assertIn("3.2.146", notes)
        self.assertIn("3.2.76", notes)
        self.assertIn("वासरूप", notes)

    def test_and_the_qualification_comes_once_more(self):
        """अथ तु प्रायिकम् एतत्, ततस् तस्यैवायं प्रपञ्चः."""
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("प्रायिकम्", REGISTRY.get("3.2.177").notes)


class TwoRulesCorroboratingEachOther(unittest.TestCase):
    """
    3.2.153 asked whether its refusal was needed when 3.2.167 would
    displace the युच् anyway, and answered that वासरूप could have let
    both stand. The pair it cited as evidence — कम्रा beside कमना,
    कम्प्रा beside कम्पना — are 3.2.167's OWN forms.
    """

    def test_the_roots_of_the_cited_forms_are_this_rules(self):
        for root in ("kam", "kamp"):
            with self.subTest(root=root):
                self.assertIn(root, provisions_for("3.2.167")[0].of)
                self.assertEqual(
                    tacchila_affix(root=root, wants="ra").by,
                    "3.2.167")

    def test_and_each_rule_names_the_other(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.2.167", REGISTRY.get("3.2.153").notes)
        self.assertIn("3.2.153", REGISTRY.get("3.2.167").notes)


class ConditionsAboutAStemAlreadyBuilt(unittest.TestCase):
    """
    3.2.166 and 3.2.176 want a यङन्त, 3.2.168 a सन्नन्त, 3.2.170 a
    क्यन्त. Every condition before these was about the root itself.
    """

    def test_each_wants_its_stem_and_refuses_the_bare_root(self):
        for where, sutra in (
            (dict(root="yaj", yan_anta=True), "3.2.166"),
            (dict(root="yā", yan_anta=True), "3.2.176"),
            (dict(root="bhikṣ", san_anta=True), "3.2.168"),
        ):
            with self.subTest(sutra=sutra):
                self.assertEqual(tacchila_affix(**where).by, sutra)
                bare = {k: v for k, v in where.items()
                        if k == "root"}
                self.assertNotEqual(
                    tacchila_affix(**bare).by, sutra)

    def test_3_2_170_needs_the_veda_as_well(self):
        """छन्दसीति किम्? मित्रीयिता."""
        self.assertEqual(
            tacchila_affix(kya_anta=True, chandasi=True).by, "3.2.170")
        self.assertNotEqual(
            tacchila_affix(kya_anta=True).by, "3.2.170")

    def test_and_3_2_172_is_where_that_vedic_condition_stops(self):
        """छन्दसीति निवृत्तम् — the eighth in this pāda."""
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("निवृत्तम्", REGISTRY.get("3.2.172").notes)
        self.assertFalse(provisions_for("3.2.172")[0].chandasi)
        self.assertEqual(tacchila_affix(root="svap").by, "3.2.172")


class SettledFromTheNatureOfTheCase(unittest.TestCase):
    """
    स्वभावात् — twice in two rules. At 3.2.161 it decides that the
    affix names the thing acted on, wood being broken rather than
    breaking; at 3.2.162 it picks between two roots spelt alike. A
    justification from how the world is, where every other root
    ambiguity in this pāda was settled from the text.
    """

    def test_both_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.2.161", "3.2.162"):
            with self.subTest(sutra=sutra):
                self.assertIn("स्वभावात्", REGISTRY.get(sutra).notes)

    def test_and_the_other_kind_of_argument_is_still_in_use(self):
        """
        3.2.157 settles क्षि and प्रसू from the text as usual, so the
        two kinds stand side by side in one run rather than one having
        replaced the other.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("क्षि", REGISTRY.get("3.2.157").notes)


class AMarkerWrittenToDefeatALaterRule(unittest.TestCase):
    """
    3.2.171's किकिनौ are marked कित् though 1.2.5 would give that
    anyway — because 7.4.11 prescribes a guṇa exactly where a
    prohibition would otherwise reach, तस्यापि बाधनार्थं कित्त्वम्.
    """

    def test_the_argument_names_both_rules(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.171").notes
        self.assertIn("1.2.5", notes)
        self.assertIn("7.4.11", notes)

    def test_and_a_marker_meaning_nothing_is_recorded_as_such(self):
        """
        The तकार of आत् is मुखसुखार्थ — for ease of saying, and
        restricting nothing. The same kind of mark as 3.2.141's उ.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("मुखसुखार्थ", REGISTRY.get("3.2.171").notes)
        self.assertIn("उच्चारणार्थः", REGISTRY.get("3.2.141").notes)


class ANipatanaInsideTheTable(unittest.TestCase):
    """
    3.2.164 गत्वरश्च. What is fixed is the nasal's loss; the affix is
    prescribed as everywhere else. So it stays in the table rather
    than going to the fixed-word lookup — the same division 3.2.71
    made, धातूपपदसमुदाया निपात्यन्ते, प्रत्ययस्तु विधीयत एव.
    """

    def test_it_is_tabled_and_not_looked_up(self):
        from src.astadhyayi.upapada_krt import nipatana

        self.assertTrue(provisions_for("3.2.164"))
        fixed = {s for s, _a, _w
                 in nipatana.__globals__["NIPATANA"].values()}
        self.assertNotIn("3.2.164", fixed)

    def test_and_the_split_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.164").notes
        self.assertIn("अनुनासिकलोपः", notes)
        self.assertIn("3.2.71", notes)


class NamingTheAffixWhereTwoRulesShareARoot(unittest.TestCase):
    """
    स्था is named by 3.2.139 and by 3.2.175, and the vṛtti gives
    स्थास्नुः under the one and स्थावरः under the other. `wants` is
    how the caller says which is meant — the idiom the उपपद table and
    the लिट् substitutes already use.
    """

    def test_naming_the_affix_reaches_the_rule_that_gives_it(self):
        self.assertEqual(
            tacchila_affix(root="sthā", wants="varac").by, "3.2.175")
        self.assertEqual(
            tacchila_affix(root="sthā", wants="ksnu").by, "3.2.139")

    def test_and_leaving_it_out_still_answers(self):
        answer = tacchila_affix(root="sthā")
        self.assertIsInstance(answer, Added)
        self.assertIn(answer.by, ("3.2.139", "3.2.175"))

    def test_this_run_declares_no_reuse(self):
        from src.astadhyayi.sutra import REGISTRY

        for n in range(156, 178):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(REGISTRY.get("3.2.%d" % n).reuses, ())


if __name__ == "__main__":
    unittest.main()
