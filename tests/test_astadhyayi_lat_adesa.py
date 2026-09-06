# -*- coding: utf-8 -*-
"""
3.2.123 to 3.2.133 — the present, and what replaces it.

3.2.123 वर्तमाने लट् is where 3.2.84's भूते heading stops: the block
boundary is the text's own. Then 3.2.124–133 put शतृ and शानच् in
लट्'s place — a substitution, as 3.2.105–108 are for लिट् — and
3.2.127 NAMES the pair, as 3.2.102 named निष्ठा.

What this block asserts that no earlier one could:

  * a heading ending exactly where a rule names another time;
  * a pratyāhāra whose members are RULES rather than sounds;
  * a compound's own word-order taken as evidence about the rule;
  * a term REUSED from an earlier rule rather than split from it.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.lakara import (
    LAT_ADESA, SAT, lakara_for, lat_provisions_for, lat_substitute,
    sat_samjna,
)
from src.astadhyayi.upapada_krt import Added, NotAdded


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.124", "śatṛ", dict(aprathama=True)),
        ("3.2.125", "śatṛ", dict(sambodhana=True)),
        ("3.2.126", "śatṛ", dict(lakshana_hetu=True)),
        ("3.2.128", "śānan", dict(root="pū")),
        ("3.2.129", "cānaś", dict(sense="tācchīlya")),
        ("3.2.130", "śatṛ", dict(root="iṅ", akrcchri=True)),
        ("3.2.131", "śatṛ", dict(root="dviṣ", amitra=True)),
        ("3.2.132", "śatṛ", dict(root="su", yajna=True)),
        ("3.2.133", "śatṛ", dict(root="arh", sense="praśaṃsā")),
    )

    def test_every_substituting_rule_answers_for_itself(self):
        for sutra, gives, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = lat_substitute(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_the_first_three_give_both_affixes(self):
        """लटः शतृशानचौ — the two together, so both must be reported."""
        for where in (dict(aprathama=True), dict(sambodhana=True),
                      dict(lakshana_hetu=True)):
            with self.subTest(**where):
                answer = lat_substitute(**where)
                self.assertEqual(answer.gives, "śatṛ")
                self.assertEqual(answer.also, "शानच्")

    def test_it_refuses_what_no_rule_reaches_without_blaming_one(self):
        answer = lat_substitute(root="kṛ")
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "")


class AHeadingEndingWhereAnotherTimeIsNamed(unittest.TestCase):
    """
    3.2.84 भूते was said to run as far as 3.2.122. 3.2.123 वर्तमाने लट्
    is the first rule outside it, and it is outside because it names
    another time — not because a count ran out.
    """

    def test_the_present_answers_only_under_its_own_time(self):
        present = lakara_for(time="vartamāna")
        self.assertEqual((present.by, present.gives), ("3.2.123", "laṭ"))

    def test_and_the_past_rules_are_not_reached_under_it(self):
        """
        Asking for the present must not hand back a past ending, and
        asking for the past must not hand back the present one.
        """
        self.assertEqual(lakara_for().by, "3.2.110")
        self.assertNotEqual(lakara_for(time="vartamāna").by, "3.2.110")
        self.assertNotEqual(
            lakara_for(beside="sma", anadyatana=True).by, "3.2.123")

    def test_the_boundary_is_the_headings_own(self):
        from src.astadhyayi.upapada_krt import (
            BHUTE_THROUGH, bhute_heading,
        )

        self.assertEqual(BHUTE_THROUGH, 122)
        self.assertEqual(bhute_heading("3.2.122").by, "3.2.84")
        self.assertIsInstance(bhute_heading("3.2.123"), NotAdded)


class SubstitutionAndNotAddition(unittest.TestCase):
    """
    शतृ and शानच् stand in लट्'s PLACE. They are not added to a root,
    so they answer from their own entry point — the same shape
    3.2.105–108 have for लिट्.
    """

    def test_these_rules_answer_from_the_substitution_entry_point(self):
        from src.astadhyayi.sutra import REGISTRY

        for n in list(range(124, 127)) + list(range(128, 134)):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(
                    REGISTRY.get("3.2.%d" % n).apply.__name__,
                    "lat_substitute")

    def test_and_the_affix_table_does_not_hold_them(self):
        from src.astadhyayi.upapada_krt import UPAPADA

        tabled = {row.sutra for row in UPAPADA}
        for n in range(123, 134):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertNotIn("3.2.%d" % n, tabled)


class ASeventhUseOfRepetition(unittest.TestCase):
    """
    लड्ग्रहणम् अधिकविधानार्थम् — लट् is named again though it was
    running, and what that buys is that the substitution reaches
    BEYOND the stated condition: क्वचित् प्रथमासमानाधिकरणेऽपि भवति,
    सन् ब्राह्मणः, अधीयानः.

    The same job 3.2.106's लिड्ग्रहण did, so widening is attested
    twice and is not a one-off reading.
    """

    def test_the_argument_is_recorded_where_a_reader_will_find_it(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.124").notes
        self.assertIn("अधिकविधानार्थम्", notes)
        self.assertIn("3.2.106", notes)

    def test_and_the_widening_is_a_scar_not_a_condition(self):
        """
        What the repetition licenses — सन् ब्राह्मणः agreeing with a
        FIRST-case word — is exactly what the rule's stated condition
        excludes. There is no condition to codify it as, so the code
        follows the rule as written and the note carries the rest.
        """
        self.assertIs(lat_provisions_for("3.2.124")[0].aprathama, True)
        self.assertNotEqual(
            lat_substitute(aprathama=False).by, "3.2.124")


class APratyaharaWhoseMembersAreRules(unittest.TestCase):
    """
    3.2.128. The vṛtti asks how 2.3.69's षष्ठीप्रतिषेध can apply if
    these affixes are not लादेश at all, and answers तृन्निति
    प्रत्याहारनिर्देशात् — a pratyāhāra तृन् running from 3.2.124 to
    the न of तृन् at 3.2.135. The device that abbreviates a span of
    SOUNDS, used on a span of the grammar itself.
    """

    def test_the_span_is_recorded_with_both_of_its_ends(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.128").notes
        self.assertIn("प्रत्याहार", notes)
        self.assertIn("3.2.124", notes)
        self.assertIn("3.2.135", notes)

    def test_and_both_ends_are_real_sutras_of_this_pada(self):
        """
        A span is only a span if its ends exist. This stood as a debt
        while 3.2.135 was unread: the near end was codified and the
        far one was not, so the pratyāhāra could be recorded but not
        checked. Reading the तच्छीलादि run paid it, and the test went
        red — which is what a debt written as a test is for.

        Both ends are now real sūtras of this pāda, and the span they
        bound holds every rule between them.
        """
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        self.assertIn("3.2.124", have)
        self.assertIn("3.2.135", have)
        for n in range(124, 136):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertIn("3.2.%d" % n, have)


class ACompoundsOrderAsEvidence(unittest.TestCase):
    """
    लक्षणहेत्वोरिति निर्देशः पूर्वनिपातव्यभिचारलिङ्गम् — हेतु should
    have stood first by the rules governing which member of a compound
    comes first, and its not doing so is the SIGN that those rules are
    departed from. The second time in this pāda a compound's own form
    carries an argument, after 3.2.111's बहुव्रीहि.
    """

    def test_both_arguments_from_form_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("पूर्वनिपातव्यभिचारलिङ्गम्",
                      REGISTRY.get("3.2.126").notes)
        self.assertIn("बहुव्रीहिनिर्देश",
                      REGISTRY.get("3.2.111").notes)

    def test_the_mark_must_be_an_act(self):
        """क्रियाया इति किम्? द्रव्यगुणयोर्मा भूत्."""
        self.assertEqual(
            lat_substitute(lakshana_hetu=True).by, "3.2.126")
        self.assertNotEqual(lat_substitute().by, "3.2.126")


class ASecondSamjnaRule(unittest.TestCase):
    """
    3.2.127 तौ सत्. It names and adds nothing, as 3.2.102 named
    निष्ठा — so naming is a settled kind now rather than a one-off.
    """

    def test_both_affixes_bear_the_name_and_nothing_else_does(self):
        for affix in SAT:
            with self.subTest(affix=affix):
                answer = sat_samjna(affix)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, "3.2.127")
        self.assertEqual(SAT, ("śatṛ", "śānac"))

    def test_an_affix_outside_the_pair_is_refused(self):
        answer = sat_samjna("ṇvul")
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "")

    def test_the_name_attaches_at_large_and_the_note_says_why(self):
        """
        तौग्रहणम् उपाध्यसंसर्गार्थम्, शतृशानज्मात्रस्य संज्ञा भवति —
        तौ is said so the name does NOT pick up the conditions of the
        rules just before it. ब्राह्मणस्य करिष्यन् is सत् too.

        A word written to STOP a condition attaching, which is the
        mirror of 3.2.78's सुब्ग्रहण stopping a preverb.
        """
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.127").notes
        self.assertIn("तौग्रहणम्", notes)
        self.assertIn("उपाध्यसंसर्गार्थम्", notes)
        self.assertIn("करिष्यन्", notes)


class ATermReusedRatherThanSplit(unittest.TestCase):
    """
    3.2.129's ताच्छील्य is glossed तत्स्वभावता — word for word what
    3.2.78 and 3.2.11 were given. So the field is SHARED.

    The opposite call from 3.1.149's समभिहार, which had to be kept
    apart from 3.1.22's because the vṛtti glossed the two differently.
    Whether to share a name is decided by the commentary's gloss and
    not by the word being the same.
    """

    def test_the_same_value_reaches_both_rules(self):
        from src.astadhyayi.upapada_krt import upapada_affix

        self.assertEqual(
            lat_substitute(sense="tācchīlya").by, "3.2.129")
        self.assertEqual(
            upapada_affix(root="bhuj", beside="uṣṇa", role="sup",
                          sense="tācchīlya").by, "3.2.78")

    def test_and_the_reason_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.129").notes
        self.assertIn("तत्स्वभावता", notes)
        self.assertIn("3.1.149", notes)


class TheConditionsOfThisRunAreLive(unittest.TestCase):

    def test_each_named_condition_is_needed(self):
        for where, sutra in (
            (dict(root="iṅ", akrcchri=True), "3.2.130"),
            (dict(root="dviṣ", amitra=True), "3.2.131"),
            (dict(root="su", yajna=True), "3.2.132"),
            (dict(root="arh", sense="praśaṃsā"), "3.2.133"),
        ):
            with self.subTest(sutra=sutra):
                self.assertEqual(lat_substitute(**where).by, sutra)
                bare = dict(where)
                for key in ("akrcchri", "amitra", "yajna", "sense"):
                    bare.pop(key, None)
                self.assertNotEqual(lat_substitute(**bare).by, sutra)

    def test_3_2_125_reaches_past_what_3_2_124_shut_out(self):
        """
        प्रथमासमानाधिकरणार्थ आरम्भः — the seventh time in this pāda a
        rule exists for what the rule before it excluded.
        """
        self.assertEqual(lat_substitute(sambodhana=True).by, "3.2.125")
        self.assertNotEqual(
            lat_substitute(aprathama=True).by, "3.2.125")


if __name__ == "__main__":
    unittest.main()
