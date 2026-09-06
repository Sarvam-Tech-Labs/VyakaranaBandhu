# -*- coding: utf-8 -*-
"""
3.1.1 to 3.1.31 — what an affix is, and the affixes that make a root.

Expectations are the Kāśikā's worked forms and its *kim*
counter-examples. Three pairs of rules in this run reach the same base
in the same sense and are told apart only by something the sūtras say
and a first draft of the table did not carry; each pair is held here,
because collapsing them is a fault a worked example alone would not
show — one of the two simply stops being reachable while every form the
table does produce stays correct.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.pratyaya import (
    NOT_AFFIXES, accent_of, in_the_affix_section, named_affix, position_of,
)
from src.astadhyayi.sanadi import (
    AYADI, GUPADI, LUPADI, MUNDADI, SANADI, SATYADI, ayadi_optional,
    provisions_for, sanadi_affix,
)


class WhatAnAffixIs(unittest.TestCase):

    def test_3_1_1_names_it(self):
        answer = named_affix()
        self.assertTrue(answer.is_affix)
        self.assertEqual(answer.by, "3.1.1")

    def test_the_five_the_vrtti_excludes_are_refused_with_a_reason(self):
        """प्रकृत्युपपदोपाधिविकारागमान् वर्जयित्वा."""
        for name, _gloss in NOT_AFFIXES:
            with self.subTest(prescribes=name):
                answer = named_affix(prescribes=name)
                self.assertFalse(answer.is_affix)
                self.assertEqual(answer.by, "", "no rule acted")
                self.assertIn(name, answer.why,
                              "the refusal says which of the five it is")

    def test_something_that_is_neither_is_refused_outright(self):
        with self.assertRaises(ValueError):
            named_affix(prescribes="samāsa")

    def test_the_heading_runs_to_the_end_of_adhyaya_5(self):
        """आ पञ्चमाध्यायपरिसमाप्तेः, and starting at the NEXT rule."""
        self.assertTrue(in_the_affix_section("3.1.5"))
        self.assertTrue(in_the_affix_section("4.1.2"))
        self.assertTrue(in_the_affix_section("5.4.160"))
        self.assertFalse(in_the_affix_section("3.1.1"),
                         "the heading rules are not inside their own range")
        self.assertFalse(in_the_affix_section("6.1.1"))


class EachOfTheFourHeadingsReportsItself(unittest.TestCase):
    """
    One function answered all four and named only 3.1.1, so asking
    3.1.2 came back citing a rule that had not acted. The case guard
    caught it; these hold the fix.
    """

    def test_3_1_2_answers_about_position(self):
        answer = position_of()
        self.assertEqual(answer.by, "3.1.2")
        self.assertEqual(answer.position, "after")

    def test_3_1_3_answers_about_accent(self):
        answer = accent_of()
        self.assertEqual(answer.by, "3.1.3")
        self.assertEqual(answer.accent, "ādyudātta")

    def test_3_1_4_excepts_it_and_is_read_first(self):
        """
        पूर्वस्यायमपवादः. Read after the rule it excepts, the general
        rule would answer for everything and this could never fire.
        """
        for excepted in (dict(sup=True), dict(pit=True)):
            with self.subTest(**excepted):
                answer = accent_of(**excepted)
                self.assertEqual(answer.by, "3.1.4")
                self.assertEqual(answer.accent, "anudātta")


class ThreePairsToldApartByWhatTheSutrasSay(unittest.TestCase):
    """
    Each pair reaches the same base in the same sense. Collapsing one
    does not produce a wrong form — it makes the second rule
    unreachable while everything the table still answers stays right,
    which is why each needs a test of its own.
    """

    def test_3_1_8_and_3_1_9_are_alternatives_not_rivals(self):
        """
        पुत्रीयति and पुत्रकाम्यति both stand, so both rules must be
        reachable on the same input. Naming the affix says which is
        being asked about.
        """
        shared = dict(is_root=False, sense="icchā")
        self.assertEqual(sanadi_affix("putra", **shared).by, "3.1.8")
        self.assertEqual(
            sanadi_affix("putra", affix="kyac", **shared).by, "3.1.8")
        self.assertEqual(
            sanadi_affix("putra", affix="kāmyac", **shared).by, "3.1.9")

    def test_3_1_10_and_3_1_11_divide_by_the_role_compared(self):
        """
        Both mean behaving LIKE something. 3.1.10 takes the thing
        compared as the object — पुत्रीयति छात्रम्; 3.1.11 says कर्तुः
        outright — श्येनायते. A yes-or-no flag lost the distinction and
        3.1.11 became unreachable.
        """
        shared = dict(is_root=False, sense="ācāra")
        obj = sanadi_affix("putra", upamana="karman", **shared)
        self.assertEqual(obj.by, "3.1.10")
        self.assertEqual(obj.gives, "kyac")

        agent = sanadi_affix("śyena", upamana="kartṛ", **shared)
        self.assertEqual(agent.by, "3.1.11")
        self.assertEqual(agent.gives, "kyaṅ")

    def test_neither_reaches_without_a_comparison_at_all(self):
        self.assertEqual(
            sanadi_affix("putra", is_root=False, sense="ācāra").by, "")

    def test_3_1_26_beats_3_1_25_where_the_sense_is_named(self):
        """
        पच् is read in the TENTH class as well as the first, so 3.1.25
        reaches it and answered first — though 3.1.26 हेतुमति च is the
        rule that speaks about causing. विशेष over सामान्य: a rule that
        names the sense asked for beats one that names none.
        """
        from src.astadhyayi.pada import verbal_gana

        self.assertIn("10", verbal_gana("pac"),
                      "the collision is real, not contrived")
        self.assertEqual(sanadi_affix("pac", sense="hetumat").by, "3.1.26")
        # And with no sense asked, the general rule still answers.
        self.assertEqual(sanadi_affix("pac").by, "3.1.25")


class TheAffixesThatMakeARoot(unittest.TestCase):

    def test_each_rule_answers_for_its_own_example(self):
        cases = (
            ("3.1.5", "san", dict(base="gup",
                                  sense="nindā-kṣamā-vyādhipratīkāra")),
            ("3.1.6", "san", dict(base="mān")),
            ("3.1.7", "san", dict(base="kṛ", sense="icchā")),
            ("3.1.12", "kyaṅ", dict(base="śīghra", is_root=False,
                                    sense="bhū")),
            ("3.1.13", "kyaṣ", dict(base="lohita", is_root=False,
                                    sense="bhū")),
            ("3.1.14", "kyaṅ", dict(base="kaṣṭa", is_root=False,
                                    sense="kramaṇa")),
            ("3.1.15", "kyaṅ", dict(base="romantha", is_root=False,
                                    sense="varti-cara")),
            ("3.1.16", "kyaṅ", dict(base="bāṣpa", is_root=False,
                                    sense="udvamana")),
            ("3.1.17", "kyaṅ", dict(base="śabda", is_root=False,
                                    sense="karaṇa")),
            ("3.1.18", "kyaṅ", dict(base="sukha", is_root=False,
                                    sense="kartṛvedanā")),
            ("3.1.19", "kyac", dict(base="namas", is_root=False,
                                    sense="karaṇa")),
            ("3.1.20", "ṇiṅ", dict(base="cīvara", is_root=False,
                                   sense="karaṇa")),
            ("3.1.21", "ṇic", dict(base="muṇḍa", is_root=False,
                                   sense="karaṇa")),
            ("3.1.23", "yaṅ", dict(base="kram", sense="kauṭilya")),
            ("3.1.24", "yaṅ", dict(base="lup", sense="bhāvagarhā")),
            ("3.1.25", "ṇic", dict(base="satya", is_root=False)),
            ("3.1.25", "ṇic", dict(base="cur")),
            ("3.1.26", "ṇic", dict(base="pac", sense="hetumat")),
            ("3.1.27", "yak", dict(base="kaṇḍūñ")),
            ("3.1.28", "āya", dict(base="gupū")),
            ("3.1.29", "īyaṅ", dict(base="ṛti")),
            ("3.1.30", "ṇiṅ", dict(base="kam")),
        )
        for sutra, affix, where in cases:
            base = where.pop("base")
            with self.subTest(sutra=sutra, base=base):
                answer = sanadi_affix(base, **where)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_every_named_word_of_a_list_rule_is_reached(self):
        """
        The lists the sūtras state themselves — checked over the list
        rather than by naming members, so a corrected list is covered.
        """
        for word in MUNDADI:
            with self.subTest(sutra="3.1.21", base=word):
                self.assertEqual(
                    sanadi_affix(word, is_root=False,
                                 sense="karaṇa").by, "3.1.21")
        for word in SATYADI:
            with self.subTest(sutra="3.1.25", base=word):
                self.assertEqual(
                    sanadi_affix(word, is_root=False).by, "3.1.25")
        for word in LUPADI:
            with self.subTest(sutra="3.1.24", base=word):
                self.assertEqual(
                    sanadi_affix(word, sense="bhāvagarhā").by, "3.1.24")
        for word in GUPADI:
            with self.subTest(sutra="3.1.28", base=word):
                self.assertEqual(sanadi_affix(word).by, "3.1.28")

    def test_3_1_5_holds_to_its_three_senses(self):
        """
        निन्दाक्षमाव्याधिप्रतीकारेषु सन्निष्यते, अन्यत्र यथाप्राप्तं
        प्रत्यया भवन्ति — गोपयति, तेजयति stand outside it.
        """
        self.assertEqual(
            sanadi_affix("gup",
                         sense="nindā-kṣamā-vyādhipratīkāra").by, "3.1.5")
        self.assertNotEqual(sanadi_affix("gup").by, "3.1.5")

    def test_the_base_shifts_from_root_to_word_at_3_1_8(self):
        """
        सुपः is where the run leaves roots for finished words, and it
        stays on words to 3.1.21. Asking a word of a root-rule, or the
        other way round, must reach nothing.
        """
        self.assertEqual(sanadi_affix("kṛ", sense="icchā").by, "3.1.7")
        self.assertEqual(
            sanadi_affix("kṛ", is_root=False, sense="icchā").by, "3.1.8",
            "3.1.7 wants a root and 3.1.8 a word, so the SAME base in "
            "the same sense answers from different rules depending on "
            "which it is said to be — that is what सुपः changed")

        # And a rule keyed to a named list is not reached across the
        # divide at all: 3.1.21's ten are words, and asking one as a
        # root reaches nothing.
        self.assertEqual(
            sanadi_affix("muṇḍa", is_root=False, sense="karaṇa").by,
            "3.1.21")
        self.assertEqual(
            sanadi_affix("muṇḍa", sense="karaṇa").by, "")

    def test_the_two_nitya_rules_are_marked_and_the_rest_are_not(self):
        """
        3.1.23 and 3.1.24 say नित्यम्, and it narrows the SCOPE rather
        than removing an option — नित्यग्रहणं विषयनियमार्थम्. Carried as
        its own field, not as the absence of `optional`.
        """
        for base, sense in (("kram", "kauṭilya"), ("lup", "bhāvagarhā")):
            with self.subTest(base=base):
                self.assertTrue(sanadi_affix(base, sense=sense).nitya)
        self.assertFalse(sanadi_affix("kṛ", sense="icchā").nitya)

    def test_the_rules_saying_va_are_the_ones_marked_optional(self):
        """
        वा at 3.1.7, carried down through 3.1.11, and again at 3.1.19
        where the vṛtti reads एतेभ्यो वा क्यच् प्रत्ययो भवति. Six rules,
        and no others.
        """
        optional = {"3.1.7", "3.1.8", "3.1.9", "3.1.10", "3.1.11",
                    "3.1.19"}
        for row in SANADI:
            with self.subTest(sutra=row.sutra):
                self.assertEqual(row.optional, row.sutra in optional)


class TheRuleAboutThreeOtherRules(unittest.TestCase):
    """3.1.31 आयादय आर्धधातुके वा adds no affix; it speaks about three."""

    def test_it_reaches_all_three_and_only_those(self):
        for affix in AYADI:
            with self.subTest(affix=affix):
                answer = ayadi_optional(affix, ardhadhatuka=True)
                self.assertEqual(answer.by, "3.1.31")
                self.assertTrue(answer.optional)
        self.assertEqual(ayadi_optional("san", ardhadhatuka=True).by, "")

    def test_it_holds_before_an_ardhadhatuka_only(self):
        answer = ayadi_optional("āya")
        self.assertEqual(answer.by, "")
        self.assertFalse(answer.optional)

    def test_the_three_are_the_affixes_of_3_1_28_to_3_1_30(self):
        """
        आयादयः is आय and what follows it, which the vṛtti reads as those
        three rules — so the tuple is checked against the table rather
        than written twice.
        """
        given = tuple(provisions_for(s)[0].gives
                      for s in ("3.1.28", "3.1.29", "3.1.30"))
        self.assertEqual(given, AYADI)


class TheTableIsWellFormed(unittest.TestCase):

    def test_every_row_names_a_sutra_of_this_run_and_an_affix(self):
        for row in SANADI:
            with self.subTest(sutra=row.sutra):
                self.assertRegex(row.sutra, r"^3\.1\.([5-9]|1\d|2[0-9]|30)$")
                self.assertTrue(row.gives)
                self.assertTrue(row.why)
                self.assertIn(row.base, ("dhātu", "prātipadika"))

    def test_3_1_22_is_not_in_the_table(self):
        """
        Its conditions are phonological and `yan` already asks them.
        Two statements of one rule is the thing the DRY rule forbids.
        """
        self.assertEqual(provisions_for("3.1.22"), ())

    def test_3_1_25_is_two_rows_because_it_names_two_bases(self):
        """
        Thirteen STEMS and a class of ROOTS. Written as one row the
        named list shut the class out and चुर् reached nothing.
        """
        rows = provisions_for("3.1.25")
        self.assertEqual(len(rows), 2)
        self.assertEqual({r.base for r in rows},
                         {"prātipadika", "dhātu"})

    def test_the_rows_are_in_the_texts_own_order(self):
        def order(sid):
            return tuple(int(p) for p in sid.split("."))

        seen = [order(r.sutra) for r in SANADI]
        self.assertEqual(seen, sorted(seen))


if __name__ == "__main__":
    unittest.main()
