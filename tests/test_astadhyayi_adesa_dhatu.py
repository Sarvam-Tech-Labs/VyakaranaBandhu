# -*- coding: utf-8 -*-
"""
2.4.32 to 2.4.57 — one thing standing in for another.

The expectations are the Kāśikā's worked forms and its *kim*
counter-examples. Three of the rules exist only to make a split, and the
vṛtti says in each case what the split buys; those claims are held by
tests that undo the split and check the answer changes, because a claim
about what a rule PREVENTS cannot be tested by running the rule.
"""

import dataclasses
import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.adesa_dhatu import (
    ARDHADHATUKA_FROM, ARDHADHATUKA_THROUGH, RULES, Rule, in_the_heading,
    rules_for, substitute,
)

#: 2.4.35's condition, asserted for every rule the heading governs.
AD = ("ārdhadhātuka",)


class EachRuleReplacesWhatItSays(unittest.TestCase):

    CASES = (
        ("2.4.36", "ad", "jagdhi", dict(before="lyap")),
        ("2.4.36", "ad", "jagdhi", dict(before="kit-t")),
        ("2.4.37", "ad", "ghasḷ", dict(before="luṅ")),
        ("2.4.37", "ad", "ghasḷ", dict(before="san")),
        ("2.4.38", "ad", "ghasḷ", dict(before="ghañ")),
        ("2.4.38", "ad", "ghasḷ", dict(before="ap")),
        ("2.4.40", "ad", "ghasḷ", dict(before="liṭ")),
        ("2.4.41", "veñ", "vayi", dict(before="liṭ")),
        ("2.4.42", "han", "vadha", dict(before="liṅ")),
        ("2.4.43", "han", "vadha", dict(before="luṅ")),
        ("2.4.45", "iṇ", "gā", dict(before="luṅ")),
        ("2.4.46", "iṇ", "gami", dict(before="ṇi")),
        ("2.4.47", "iṇ", "gami", dict(before="san")),
        ("2.4.48", "iṅ", "gami", dict(before="san")),
        ("2.4.49", "iṅ", "gāṅ", dict(before="liṭ")),
        ("2.4.50", "iṅ", "gāṅ", dict(before="luṅ")),
        ("2.4.50", "iṅ", "gāṅ", dict(before="lṛṅ")),
        ("2.4.51", "iṅ", "gāṅ", dict(before="ṇi-san")),
        ("2.4.51", "iṅ", "gāṅ", dict(before="ṇi-caṅ")),
        ("2.4.52", "as", "bhū", {}),
        ("2.4.53", "brū", "vaci", {}),
        ("2.4.54", "cakṣiṅ", "khyāñ", {}),
        ("2.4.55", "cakṣiṅ", "khyāñ", dict(before="liṭ")),
        ("2.4.56", "aj", "vī", {}),
        ("2.4.57", "aj", "vī", dict(before="lyuṭ")),
    )

    def test_each_gives_the_substitute_its_sutra_names(self):
        for sutra, of, gives, where in self.CASES:
            with self.subTest(sutra=sutra, of=of, **where):
                answer = substitute(of, given=AD, **where)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_the_options_are_marked_and_the_obligatory_ones_are_not(self):
        """
        Five rules of this run say अन्यतरस्याम्, विभाषा or वा, and one
        says बहुलम्. A rule that lost its option would make a choice on
        Pāṇini's behalf; one that gained a spurious one would offer a
        form the grammar does not.
        """
        optional = {"2.4.40", "2.4.41", "2.4.44", "2.4.50", "2.4.51",
                    "2.4.55", "2.4.57"}
        for sutra, of, _gives, where in self.CASES:
            with self.subTest(sutra=sutra):
                answer = substitute(of, given=AD, **where)
                self.assertEqual(answer.optional, sutra in optional)

    def test_bahulam_is_not_the_same_claim_as_optional(self):
        """
        2.4.39 says बहुलम् where अन्यतरस्याम् would have given the option
        alone, and the vṛtti asks why: कार्यान्तरार्थं बहुलग्रहणम् — it
        carries other effects, one of which is named. So the two are
        recorded as different fields, not one.
        """
        veda = substitute("ad", chandas=True, given=AD)
        self.assertEqual(veda.by, "2.4.39")
        self.assertTrue(veda.bahulam)
        perfect = substitute("ad", before="liṭ", given=AD)
        self.assertTrue(perfect.optional)
        self.assertFalse(perfect.bahulam)

    def test_a_rule_that_does_not_reach_its_input_claims_nothing(self):
        for of, where in (
            ("ad", dict(before="yak")),          # तीति किम्? अद्यते
            ("iṇ", dict(before="ṇi", sense="bodhana")),   # अबोधने
            ("iṇ", dict(before="san", sense="bodhana")),
            ("aj", dict(before="ghañ")),         # अघञपोरिति किम्?
            ("aj", dict(before="ap")),
            ("pac", {}),                         # a root this run ignores
        ):
            with self.subTest(of=of, **where):
                answer = substitute(of, given=AD, **where)
                self.assertEqual(answer.by, "")
                self.assertEqual(answer.gives, "")


class TheThreeYogavibhagas(unittest.TestCase):
    """
    A योगविभाग is a rule split where one would have served, and each of
    the three here is a claim about what the table would do WITHOUT the
    split. Running the rule cannot test that, so each test performs the
    merge the vṛtti argues against and checks the answer changes.
    """

    @staticmethod
    def _without(sutra_id):
        """The table with one sūtra's rows removed."""
        return tuple(r for r in RULES if r.sutra != sutra_id)

    @staticmethod
    def _resolve(rows, of, **where):
        """The same last-match-wins walk, over a doctored table."""
        slot = where.get("before", "")
        found = None
        for rule in rows:
            if of not in rule.of:
                continue
            if rule.atmanepada and not where.get("atmanepada"):
                continue
            if rule.chandas:
                continue
            if rule.before and slot not in rule.before:
                continue
            found = rule
        return found

    def test_2_4_43_is_split_so_the_option_misses_the_benedictive(self):
        """
        आत्मनेपदेषु लुङि विकल्पो यथा स्याल्लिङि मा भूत्. With the split,
        the middle-voice benedictive is obligatory; merge 2.4.43 into
        2.4.42 by letting 2.4.44 name both tenses, and वध्यात् becomes
        a choice — which is what the vṛtti says must not happen.
        """
        kept = substitute("han", before="liṅ", atmanepada=True, given=AD)
        self.assertEqual(kept.by, "2.4.42")
        self.assertFalse(
            kept.optional,
            "the benedictive is obligatory; that is what the split buys")

        merged = self._without("2.4.44") + (
            dataclasses.replace(
                [r for r in RULES if r.sutra == "2.4.44"][0],
                before=("luṅ", "liṅ")),
        )
        would_be = self._resolve(merged, "han", before="liṅ",
                                 atmanepada=True)
        self.assertTrue(
            would_be.optional,
            "without the split the benedictive would become optional, "
            "which is exactly the outcome लिङि मा भूत् rules out")

    def test_2_4_47_is_split_so_that_2_4_48_takes_san_only(self):
        """
        इङश्चेति सन्येव यथा स्यात्. इङ् before णि must reach nothing;
        merge 2.4.47 back into 2.4.46 by letting 2.4.48 carry णि too,
        and it starts answering.
        """
        self.assertEqual(substitute("iṅ", before="san", given=AD).by,
                         "2.4.48")
        self.assertEqual(substitute("iṅ", before="ṇi", given=AD).by, "",
                         "इङ् before णि is reached by no rule, which is "
                         "what the split is for")

        merged = self._without("2.4.48") + (
            dataclasses.replace(
                [r for r in RULES if r.sutra == "2.4.48"][0],
                before=("san", "ṇi")),
        )
        self.assertIsNotNone(
            self._resolve(merged, "iṅ", before="ṇi"),
            "without the split इङ् before णि would be replaced too")

    def test_2_4_45_repeats_lun_so_the_option_does_not_carry_down(self):
        """
        लुङीति वर्तमाने पुनर्लुङ्ग्रहणम् आत्मनेपदेष्वन्यतरस्याम् इत्येतद्
        मा भूत्. इण् → गा must be obligatory in BOTH padas — इह तु
        अविशेषेण नित्यं च भवति, अगात् and अगायि. If 2.4.44's option had
        carried, the middle would have become a choice.
        """
        for middle in (False, True):
            with self.subTest(atmanepada=middle):
                answer = substitute("iṇ", before="luṅ", atmanepada=middle,
                                    given=AD)
                self.assertEqual(answer.by, "2.4.45")
                self.assertFalse(
                    answer.optional,
                    "अविशेषेण नित्यं च भवति — obligatory in both padas")

    def test_the_option_at_2_4_44_still_reaches_the_aorist(self):
        """The other half of the same claim: the split must not cost
        the aorist its option either."""
        aorist = substitute("han", before="luṅ", atmanepada=True, given=AD)
        self.assertEqual(aorist.by, "2.4.44")
        self.assertTrue(aorist.optional)


class TheLastMatchingRowWins(unittest.TestCase):
    """
    1.4.2 विप्रतिषेधे परं कार्यम्. Three times in this run a rule is
    written to make optional what the rule just before made obligatory —
    पूर्वेण नित्ये प्राप्ते विकल्प उच्यते — so taking the FIRST match
    would make all three options unreachable.
    """

    def test_each_later_option_beats_the_earlier_obligation(self):
        for earlier, later, of, where in (
            ("2.4.43", "2.4.44", "han",
             dict(before="luṅ", atmanepada=True)),
            ("2.4.54", "2.4.55", "cakṣiṅ", dict(before="liṭ")),
            ("2.4.56", "2.4.57", "aj", dict(before="lyuṭ")),
        ):
            with self.subTest(earlier=earlier, later=later):
                answer = substitute(of, given=AD, **where)
                self.assertEqual(answer.by, later)
                self.assertTrue(answer.optional)
                # And the earlier rule really would have matched.
                self.assertTrue(
                    any(r.sutra == earlier for r in rules_for(earlier)))


class TheHeadingAt2435(unittest.TestCase):

    def test_it_governs_from_2_4_36_through_2_4_57(self):
        """
        आर्धधातुक इत्यधिकारोऽयम् ण्यक्षत्रियार्षञितः इति यावत् — up to
        2.4.58, so the last rule it reaches is 2.4.57.
        """
        self.assertTrue(in_the_heading(ARDHADHATUKA_FROM))
        self.assertTrue(in_the_heading(ARDHADHATUKA_THROUGH))
        self.assertFalse(in_the_heading("2.4.35"))
        self.assertFalse(in_the_heading("2.4.58"))

    def test_the_three_pronoun_rules_are_outside_it(self):
        """
        2.4.32 to 2.4.34 stand BEFORE the heading, so they answer
        without आर्धधातुक being asserted at all. A heading that had
        swallowed them would make इदम् unanswerable.
        """
        for of, where in (("idam", dict(before_vibhakti=3)),
                          ("etad", dict(before="tra")),
                          ("idam", dict(before="2"))):
            with self.subTest(of=of, **where):
                answer = substitute(of, given=("anvādeśa",), **where)
                self.assertNotEqual(answer.by, "")
                self.assertFalse(in_the_heading(answer.by))

    def test_every_rule_it_governs_withholds_until_it_is_asserted(self):
        """
        The heading is a condition, not a comment. Each governed rule
        answers with it and refuses without it — and it is checked over
        the table rather than a hand-list, so a row added later is
        covered without editing this test.
        """
        for rule in RULES:
            if not in_the_heading(rule.sutra) or rule.chandas:
                continue
            where = {"before": rule.before[0]} if rule.before else {}
            if rule.atmanepada:
                where["atmanepada"] = True
            with self.subTest(sutra=rule.sutra):
                self.assertNotEqual(
                    substitute(rule.of[0], given=AD, **where).by, "")
                self.assertEqual(
                    substitute(rule.of[0], **where).by, "",
                    f"{rule.sutra} answered without आर्धधातुक being "
                    f"asserted, so 2.4.35 is not doing anything")


class TheFactsAreClosed(unittest.TestCase):

    def test_a_fact_this_run_does_not_know_is_refused(self):
        with self.assertRaises(ValueError):
            substitute("ad", before="luṅ", given=("not-a-fact",))

    def test_anvadesa_is_required_and_not_assumed(self):
        """
        नेह पश्चादुच्चारणमात्रमन्वादेशः — a second utterance is not a
        second MENTION, so the fact has to be asserted. देवदत्तं भोजय,
        इमं च यज्ञदत्तम् is the vṛtti's counter.
        """
        self.assertEqual(substitute("idam", before_vibhakti=3).by, "")
        self.assertEqual(
            substitute("idam", before_vibhakti=3,
                       given=("anvādeśa",)).by, "2.4.32")


class TheTableIsWellFormed(unittest.TestCase):
    """
    Properties, not a census: a count would go stale the next time a
    row is added, and three such tests have had to be replaced already.
    """

    def test_every_row_names_a_sutra_of_this_run_and_a_substitute(self):
        for rule in RULES:
            with self.subTest(sutra=rule.sutra):
                self.assertRegex(rule.sutra, r"^2\.4\.(3[2-9]|4\d|5[0-7])$")
                self.assertTrue(rule.of)
                self.assertTrue(rule.gives)
                self.assertTrue(rule.why, "every row says why, in the "
                                          "commentary's own words")

    def test_every_sutra_of_the_run_has_at_least_one_row(self):
        """2.4.35 has none, being a heading; every other one has."""
        for n in range(32, 58):
            sutra = f"2.4.{n}"
            with self.subTest(sutra=sutra):
                if sutra == "2.4.35":
                    self.assertEqual(rules_for(sutra), ())
                else:
                    self.assertTrue(rules_for(sutra))

    def test_the_rows_are_in_the_texts_own_order(self):
        """
        Order is load-bearing here — the last match wins — so a row
        moved out of sūtra order would silently change three answers.
        """
        def order(sid):
            return tuple(int(p) for p in sid.split("."))

        seen = [order(r.sutra) for r in RULES]
        self.assertEqual(seen, sorted(seen))

    def test_a_rule_is_frozen(self):
        with self.assertRaises(dataclasses.FrozenInstanceError):
            RULES[0].gives = "something else"     # type: ignore[misc]

    def test_rule_is_the_type_the_table_holds(self):
        self.assertTrue(all(isinstance(r, Rule) for r in RULES))


if __name__ == "__main__":
    unittest.main()
