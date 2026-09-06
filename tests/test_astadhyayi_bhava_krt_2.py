# -*- coding: utf-8 -*-
"""
3.3.38 to 3.3.55 — the rest of the घञ् rules.

What this block asserts that no earlier one could:

  * a condition read BACKWARD out of a rule not yet stated —
    सिंहावलोकितन्याय, the lion's backward glance;
  * an अनुवृत्ति in which the NEAREST word loses to a further one;
  * वासरूप suspended by repeating a word rather than by a ज्ञापक;
  * a rule that replaces a sound of the root as well as adding to it;
  * a condition carved out of a definition the rule does not give;
  * a commentary deciding between two witnesses to the mūla.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.bhava_krt import BHAVA_KRT, bhava_affix
from src.astadhyayi.upapada_krt import Added


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.3.38", "ghañ", dict(root="i", upasarga="pari",
                                sense="anupātyaya")),
        ("3.3.39", "ghañ", dict(root="śī", upasarga="vi",
                                sense="paryāya")),
        ("3.3.40", "ghañ", dict(root="ci", sense="hastādāna")),
        ("3.3.41", "ghañ", dict(root="ci", sense="nivāsa")),
        ("3.3.42", "ghañ", dict(root="ci", sense="saṅgha")),
        ("3.3.43", "ṇac", dict(sense="karmavyatihāra", stri=True)),
        ("3.3.44", "inuṇ", dict(sense="abhividhi", bhava=True)),
        ("3.3.45", "ghañ", dict(root="grah", upasarga="ava",
                                sense="ākrośa")),
        ("3.3.46", "ghañ", dict(root="grah", upasarga="pra",
                                sense="lipsā")),
        ("3.3.47", "ghañ", dict(root="grah", upasarga="pari",
                                sense="yajña")),
        ("3.3.48", "ghañ", dict(root="vṛ", upasarga="ni",
                                names_a="dhānya")),
        ("3.3.49", "ghañ", dict(root="śri", upasarga="ud")),
        ("3.3.50", "ghañ", dict(root="ru", upasarga="āṅ")),
        ("3.3.51", "ghañ", dict(root="grah", upasarga="ava",
                                sense="varṣapratibandha")),
        ("3.3.52", "ghañ", dict(root="grah", upasarga="pra",
                                names_a="vaṇij")),
        ("3.3.53", "ghañ", dict(root="grah", upasarga="pra",
                                names_a="raśmi")),
        ("3.3.54", "ghañ", dict(root="vṛ", upasarga="pra",
                                sense="ācchādana")),
        ("3.3.55", "ghañ", dict(root="bhū", upasarga="pari",
                                sense="avajñāna")),
    )

    def test_every_rule_answers_and_gives_what_it_says(self):
        for sutra, gives, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = bhava_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_the_run_gives_more_than_one_affix(self):
        """
        Which is why the entry point is not called `ghan_affix`. 3.3.43
        gives णच् and 3.3.44 इनुण्, both on the same ground — and the
        rules after give अच् and अप् besides.

        The property, not the set: this once named the three affixes
        the table then held, and went red when it held five.
        """
        gives = {r.gives for r in BHAVA_KRT}
        self.assertIn("ghañ", gives)
        self.assertGreater(len(gives), 1)
        self.assertEqual(
            {r.gives for r in BHAVA_KRT if r.sutra == "3.3.43"},
            {"ṇac"})
        self.assertEqual(
            {r.gives for r in BHAVA_KRT if r.sutra == "3.3.44"},
            {"inuṇ"})


class NoCounterExampleReachesTheRuleItCounters(unittest.TestCase):

    COUNTERS = (
        ("3.3.38", dict(root="i", upasarga="pari"), "kālasya paryayaḥ"),
        ("3.3.39", dict(root="śī", upasarga="vi"), "viśayaḥ"),
        ("3.3.40", dict(root="ci", sense="hastādāna", steya=True),
         "phalapracayaś cauryeṇa"),
        ("3.3.41", dict(root="ci"), "cayaḥ"),
        ("3.3.43", dict(sense="karmavyatihāra"), "vyatipāko vartate"),
        ("3.3.45", dict(root="grah", upasarga="ava"),
         "avagrahaḥ padasya"),
        ("3.3.46", dict(root="grah", upasarga="pra"),
         "pragraho devadattasya"),
        ("3.3.48", dict(root="vṛ", upasarga="ni"), "nivarā kanyā"),
        ("3.3.54", dict(root="vṛ", upasarga="pra"), "pravarā gauḥ"),
        ("3.3.55", dict(root="bhū", upasarga="pari"),
         "sarvato bhavanaṃ paribhavaḥ"),
    )

    def test_none_of_them_reaches_it(self):
        for sutra, where, form in self.COUNTERS:
            with self.subTest(sutra=sutra, form=form):
                self.assertNotEqual(bhava_affix(**where).by, sutra)


class AConditionReadBackwardOutOfARuleNotYetStated(unittest.TestCase):
    """
    सिंहावलोकितन्याय — the lion's backward glance. 3.3.50's विभाषा is
    read BACK into 3.3.49, so a word not yet uttered conditions a rule
    already given.

    Three facts about how conditions travel are now on record and none
    follows from position: 3.2.122's मण्डूकप्लुति vaults FORWARD over
    rules that had dropped a condition; this looks BACKWARD; and
    3.3.45's नानन्तर इनुण् has the nearest word lose to a further one.
    """

    def test_the_borrowing_rule_is_optional(self):
        rows = {r.sutra: r for r in BHAVA_KRT}
        self.assertTrue(rows["3.3.49"].optional)
        self.assertTrue(rows["3.3.50"].optional)

    def test_and_where_it_borrowed_from_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.49").notes
        self.assertIn("सिंहावलोकित", notes)
        self.assertIn("3.3.50", notes)

    def test_the_lender_records_being_spent_twice(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.49", REGISTRY.get("3.3.50").notes)

    def test_all_three_ways_a_condition_travels_are_recorded(self):
        """
        Each was found in a different rule and none is a special case
        of another. If a fourth turns up, this is where it belongs.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("मण्डूकप्लुति", REGISTRY.get("3.2.122").notes)
        self.assertIn("सिंहावलोकित", REGISTRY.get("3.3.49").notes)
        self.assertIn("नानन्तर", REGISTRY.get("3.3.45").notes)


class TheNearestWordLoses(unittest.TestCase):
    """
    3.3.44 gives इनुण् and stands immediately before 3.3.45. What
    3.3.45 carries down is not that but घञ्, from further back:
    दृष्टानुवृत्तिसामर्थ्याद् घञनुवर्तते, नानन्तर इनुण्.
    """

    def test_the_nearer_affix_is_not_the_one_carried(self):
        self.assertEqual(
            bhava_affix(root="grah", upasarga="ava",
                        sense="ākrośa").gives, "ghañ")
        self.assertEqual(
            bhava_affix(sense="abhividhi", bhava=True).gives, "inuṇ")

    def test_and_the_ground_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.45").notes
        self.assertIn("दृष्टानुवृत्तिसामर्थ्याद्", notes)


class VasarupaSuspendedByRepeatingAWord(unittest.TestCase):
    """
    Three suspensions so far argued from a ज्ञापक — 3.2.146, 3.2.177,
    3.3.10. 3.3.44 does it by saying भाव again when भावे was already
    running: पुनर्भावग्रहणं वासरूपनिरासार्थम्.
    """

    def test_the_rule_records_the_repetition_and_its_purpose(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.44").notes
        self.assertIn("पुनर्भावग्रहणं", notes)
        self.assertIn("वासरूपनिरासार्थम्", notes)

    def test_it_names_the_three_that_used_a_jnapaka_instead(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.44").notes
        for sutra in ("3.2.146", "3.2.177", "3.3.10"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, notes)

    def test_and_the_suspension_is_not_total(self):
        """ल्युटा तु समावेश इष्यते, by 3.3.113."""
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.113", REGISTRY.get("3.3.44").notes)

    def test_the_condition_running_from_3_3_18_still_reaches_it(self):
        """
        भावे is repeated, not replaced — so the row states it, and
        without it the rule does not answer.
        """
        self.assertEqual(
            bhava_affix(sense="abhividhi", bhava=True).by, "3.3.44")
        self.assertNotEqual(
            bhava_affix(sense="abhividhi").by, "3.3.44")


class FourSensesInOneRule(unittest.TestCase):
    """
    3.3.41 names निवास, चिति, शरीर and उपसमाधान. One string cannot
    hold alternatives, which is why the field is a tuple — a migration
    made for this rule and not for tidiness.
    """

    def test_each_of_the_four_reaches_it(self):
        for sense in ("nivāsa", "citi", "śarīra", "upasamādhāna"):
            with self.subTest(sense=sense):
                self.assertEqual(
                    bhava_affix(root="ci", sense=sense).by, "3.3.41")

    def test_and_none_of_them_is_needed_by_any_other_row(self):
        row = next(r for r in BHAVA_KRT if r.sutra == "3.3.41")
        self.assertEqual(len(row.sense), 4)

    def test_a_sense_outside_the_four_does_not_reach_it(self):
        self.assertNotEqual(
            bhava_affix(root="ci", sense="saṅgha").by, "3.3.41")

    def test_the_scar_about_intention_is_recorded(self):
        """महान् काष्ठनिचयः — बहुत्वमत्र विवक्षितं नोपसमाधानम्."""
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("विवक्षितं", REGISTRY.get("3.3.41").notes)


class AConditionCarvedOutOfADefinition(unittest.TestCase):
    """
    3.3.42 names one half of a definition in order to exclude it, and
    what is left is the other half — a definition the rule never gives
    and only the commentary carries.
    """

    def test_the_definition_and_both_halves_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.42").notes
        self.assertIn("प्राणिनां समुदायः संघः", notes)
        self.assertIn("एकधर्मसमावेशेन", notes)
        self.assertIn("औत्तराधर्येण", notes)

    def test_two_counters_fail_for_two_different_reasons(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.42").notes
        self.assertIn("सूकरनिचयः", notes)
        self.assertIn("प्राणिविषयत्वात्", notes)


class ACommentaryDecidingBetweenTwoWitnesses(unittest.TestCase):
    """
    GRETIL reads प्रौ at 3.3.55, Vidyut परौ — different preverbs, not a
    spelling. The Kāśikā settles it: परिशब्द उपपदे भवतेः, परिभावः.

    Comparing two mūla texts could never have decided this. It is the
    first time in the project that a commentary has picked a reading.
    """

    def test_the_witnesses_really_do_diverge(self):
        from src.astadhyayi.corpus import collate

        collated = collate()["3.3.55"]
        self.assertEqual(collated.classify(), "divergent")
        self.assertIn("prau", collated.witnesses["gretil"])
        self.assertIn("parau", collated.witnesses["vidyut"])

    def test_the_registered_text_follows_the_commentary(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("परौ", REGISTRY.get("3.3.55").devanagari)

    def test_and_the_ground_for_choosing_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.55").notes
        self.assertIn("परिशब्द उपपदे भवतेः", notes)
        self.assertIn("GRETIL", notes)

    def test_the_rule_the_commentary_gives_forms_for_is_the_one_kept(self):
        """
        परिभावः has परि in it. If the mūla read प्रौ the rule could not
        give that form, which is the whole argument.
        """
        self.assertEqual(
            bhava_affix(root="bhū", upasarga="pari",
                        sense="avajñāna").by, "3.3.55")
        self.assertNotEqual(
            bhava_affix(root="bhū", upasarga="pra",
                        sense="avajñāna").by, "3.3.55")


class OneSpellingTakenOverTwoRoots(unittest.TestCase):
    """
    सामान्येन ग्रहणम् / द्वयोरपि ग्रहणम् — the commentary's standing
    move where one spelling names two roots. Three times in twenty
    sūtras here, after 3.2.39 used it in the pāda before.
    """

    def test_all_three_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra, root in (("3.3.28", "पूङ्पूञोः"),
                            ("3.3.29", "गृ"),
                            ("3.3.48", "वृङ्वृञोः")):
            with self.subTest(sutra=sutra):
                notes = REGISTRY.get(sutra).notes
                self.assertIn(root, notes)
                self.assertIn("ग्रहणम्", notes)

    def test_and_the_corpus_says_why_the_move_is_needed(self):
        """
        The dhātupāṭha really does carry doubled names — this is not a
        commentarial habit but a fact about the root list.
        """
        from src.astadhyayi.corpus import load_dhatupatha

        names = [d.upadesa for d in load_dhatupatha().values()]
        self.assertGreater(len(names) - len(set(names)), 100)



if __name__ == "__main__":
    unittest.main()
