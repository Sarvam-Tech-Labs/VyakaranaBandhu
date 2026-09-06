# -*- coding: utf-8 -*-
"""
3.3.56 to 3.3.81 — अच्, अप्, the root-substitutes, and six निपातन.

What this block asserts that no earlier one could:

  * a letter put in a sūtra to keep the sūtra SAYABLE;
  * a rule cancelling a condition that was running, by naming its
    opposite — and another cancelling its own sibling heading;
  * the word ORDER of a sūtra set aside by what makes sense of it;
  * a variant reading recorded and NOT chosen, twenty-three sūtras
    after one was chosen;
  * a निपातन whose whole content is a single sound.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from tests import unwrapped
from src.astadhyayi.bhava_krt import (
    BHAVA_KRT, NIPATANA, bhava_affix, nipatana,
)
from src.astadhyayi.upapada_krt import Added, NotAdded


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.3.56", "ac", dict(root="ci", root_final="i")),
        ("3.3.57", "ap", dict(root="kṛ", root_final="ṝ")),
        ("3.3.58", "ap", dict(root="gam")),
        ("3.3.59", "ap", dict(root="ad", upasarga="vi")),
        ("3.3.60", "ṇa", dict(root="ad", upasarga="ni")),
        ("3.3.61", "ap", dict(root="vyadh")),
        ("3.3.62", "ap", dict(root="svan")),
        ("3.3.63", "ap", dict(root="yam", upasarga="sam")),
        ("3.3.64", "ap", dict(root="gad", upasarga="ni")),
        ("3.3.65", "ap", dict(root="kvaṇ", sense="vīṇā")),
        ("3.3.66", "ap", dict(root="paṇ", parimana=True)),
        ("3.3.67", "ap", dict(root="mad")),
        ("3.3.69", "ap", dict(root="aj", upasarga="sam",
                              names_a="paśu")),
        ("3.3.71", "ap", dict(root="sṛ", sense="prajana")),
        ("3.3.72", "ap", dict(root="hve", upasarga="ni")),
        ("3.3.73", "ap", dict(root="hve", upasarga="āṅ",
                              sense="yuddha")),
        ("3.3.75", "ap", dict(root="hve", bhava=True)),
        ("3.3.76", "ap", dict(root="han", bhava=True)),
        ("3.3.77", "ap", dict(root="han", sense="mūrti")),
        ("3.3.78", "ap", dict(root="han", upasarga="antar",
                              names_a="deśa")),
    )

    def test_every_rule_answers_and_gives_what_it_says(self):
        for sutra, gives, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = bhava_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_the_u_final_half_of_3_3_57_also_answers(self):
        for final in ("u", "ū"):
            with self.subTest(root_final=final):
                self.assertEqual(
                    bhava_affix(root="yu", root_final=final).by, "3.3.57")


class NoCounterExampleReachesTheRuleItCounters(unittest.TestCase):

    COUNTERS = (
        ("3.3.59", dict(root="ad"), "ghāsaḥ"),
        ("3.3.61", dict(root="vyadh", upasarga="ā"), "āvyādhaḥ"),
        ("3.3.65", dict(root="kvaṇ", upasarga="ati"), "atikvāṇaḥ"),
        ("3.3.66", dict(root="paṇ"), "pāṇaḥ"),
        ("3.3.67", dict(root="mad", upasarga="pra"), "pramādaḥ"),
        ("3.3.69", dict(root="aj", upasarga="sam"),
         "samājo brāhmaṇānām"),
        ("3.3.72", dict(root="hve", upasarga="pra"), "prahvāyaḥ"),
        ("3.3.73", dict(root="hve", upasarga="āṅ"), "āhvāyaḥ"),
        ("3.3.78", dict(root="han", upasarga="antar"),
         "antarghāto 'nyaḥ"),
    )

    def test_none_of_them_reaches_it(self):
        for sutra, where, form in self.COUNTERS:
            with self.subTest(sutra=sutra, form=form):
                self.assertNotEqual(bhava_affix(**where).by, sutra)


class ALetterPutThereToKeepTheSutraSayable(unittest.TestCase):
    """
    3.3.57 ॠदोरप् carries two marks and neither does grammar. पित्करणं
    स्वरार्थम् — the प is for the accent. दकारो मुखसुखार्थः, मा भूत्
    तादपि परस्तपरः — the द is so the rule does not read as तपर.
    """

    def test_both_grounds_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.57").notes
        self.assertIn("पित्करणं स्वरार्थम्", notes)
        self.assertIn("मुखसुखार्थः", notes)

    def test_the_rule_still_answers_by_shape_alone(self):
        """
        Neither mark is a condition, so neither is a field: the rule
        reaches by the root's final sound and nothing else.
        """
        row = next(r for r in BHAVA_KRT if r.sutra == "3.3.57")
        self.assertEqual(row.root_final, ("ṝ", "u", "ū"))
        self.assertEqual(row.of, ())


class ThreeWaysToUndoSomethingAlreadyRunning(unittest.TestCase):
    """
    3.3.44 repeats a word to cancel a PRINCIPLE (3.1.94's वासरूप).
    3.3.75 repeats one to cancel a SIBLING HEADING (3.3.19).
    3.3.66 names the CONTRARY of a running word to cancel an option.
    Three rules, three devices, none inferable from the others.
    """

    def test_a_principle_cancelled_by_repetition(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("वासरूपनिरासार्थम्", REGISTRY.get("3.3.44").notes)

    def test_a_sibling_heading_cancelled_by_repetition(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.75").notes
        self.assertIn("भावग्रहणम्", notes)
        self.assertIn("निरासार्थम्", notes)
        self.assertIn("3.3.19", notes)

    def test_an_option_cancelled_by_naming_its_contrary(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.66").notes
        self.assertIn("नित्यग्रहणं विकल्पनिवृत्त्यर्थम्", notes)
        self.assertIn("3.3.62", notes)

    def test_and_the_option_really_does_stop_at_3_3_66(self):
        rows = {r.sutra: r for r in BHAVA_KRT}
        for sutra in ("3.3.62", "3.3.63", "3.3.64", "3.3.65"):
            with self.subTest(sutra=sutra, optional=True):
                self.assertTrue(rows[sutra].optional)
        self.assertFalse(rows["3.3.66"].optional)


class TheWordOrderOfASutraSetAside(unittest.TestCase):
    """
    3.3.76's च stands where it would join the SUBSTITUTE. चकारो
    भिन्नक्रमत्वाद् नादेशेन संबध्यते, किं तर्हि? प्रकृतेन प्रत्ययेन —
    it is taken with the affix instead, and so घञ् stands beside.

    3.2.29 and 3.2.30 read word order as EVIDENCE for a rule's intent.
    This rule sets it aside. Both moves are in the commentary's hands.
    """

    def test_the_reasoning_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = unwrapped(REGISTRY.get("3.3.76").notes)
        self.assertIn("भिन्नक्रमत्वाद्", notes)
        # The full phrase, now that the wrapping is flattened. It was
        # shortened to one word when a line break hid it, which is a
        # weaker test for no reason.
        self.assertIn("किं तर्हि? प्रकृतेन प्रत्ययेन", notes)
        self.assertIn("तेन घञपि भवति", notes)

    def test_and_the_earlier_rules_that_read_order_as_evidence(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.2.29", "3.2.30"):
            with self.subTest(sutra=sutra):
                self.assertIn("लक्षणव्यभिचारचिह्न",
                              REGISTRY.get(sutra).notes)


class AVariantRecordedAndAVariantChosen(unittest.TestCase):
    """
    At 3.3.55 the commentary DECIDED between two readings. At 3.3.78 it
    records one and declines: अन्ये णकारं पठन्ति ... तदपि ग्राह्यमेव.
    Which move it makes is a fact about the case, not about the
    commentary.
    """

    def test_the_one_it_decided(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.55").notes
        self.assertIn("परिशब्द उपपदे भवतेः", notes)
        self.assertIn("GRETIL", notes)

    def test_the_one_it_left_open(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.78").notes
        self.assertIn("अन्ये णकारं पठन्ति", notes)
        self.assertIn("ग्राह्यमेव", notes)

    def test_and_a_second_opinion_about_a_root_likewise(self):
        """3.3.70's अन्ये ग्लहिं प्रकृत्यन्तरमाहुः."""
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("प्रकृत्यन्तरमाहुः", REGISTRY.get("3.3.70").notes)


class SixWordsGivenWhole(unittest.TestCase):
    """
    3.3.68, 3.3.70, 3.3.74 and 3.3.79 to 3.3.81. Six निपातन here
    against four in the whole of 3.2.
    """

    def test_each_fixed_word_answers_from_its_own_rule(self):
        for word, sutra in (
            ("pramada", "3.3.68"), ("sammada", "3.3.68"),
            ("glaha", "3.3.70"), ("āhāva", "3.3.74"),
            ("praghaṇa", "3.3.79"), ("praghāṇa", "3.3.79"),
            ("udghana", "3.3.80"), ("apaghana", "3.3.81"),
        ):
            with self.subTest(word=word):
                answer = nipatana(word)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)

    def test_a_word_not_fixed_is_refused_without_naming_a_rule(self):
        answer = nipatana("pacati")
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "")

    def test_every_entry_carries_its_own_affix(self):
        """
        3.2's निपातन table began with the affix hardcoded for every
        entry and that was wrong within five rules. The lesson is kept
        here from the start, so the affix is per ENTRY.
        """
        for word, (sutra, affix, why) in NIPATANA.items():
            with self.subTest(word=word):
                self.assertTrue(affix)
                self.assertEqual(nipatana(word).gives, affix)

    def test_one_of_them_fixes_a_single_sound(self):
        """
        3.3.70: ग्रहेरप् सिद्ध एव, लत्वार्थं निपातनम् — the affix comes
        anyway by 3.3.58 and the whole निपातन is for र becoming ल.
        """
        answer = nipatana("glaha")
        self.assertIn("लत्वार्थं", answer.why)
        self.assertIn("3.3.58", answer.why)
        self.assertEqual(bhava_affix(root="grah").by, "3.3.58")

    def test_and_one_fixes_three_things_at_once(self):
        self.assertIn("संप्रसारणम्", nipatana("āhāva").why)
        self.assertIn("वृद्धि", nipatana("āhāva").why)

    def test_they_do_not_answer_from_the_table(self):
        fixed = {"3.3.68", "3.3.70", "3.3.74", "3.3.79", "3.3.80",
                 "3.3.81"}
        self.assertEqual(fixed & {r.sutra for r in BHAVA_KRT}, set())


class RulesThatChangeTheRoot(unittest.TestCase):
    """
    Three kinds now: a named substitute for one sound (3.3.41, 3.3.42),
    a named substitute for the whole root (3.3.76, 3.3.77, 3.3.78), and
    a general operation (3.3.72 to 3.3.75's संप्रसारण).
    """

    def test_the_named_substitutes(self):
        by_adesha = {}
        for row in BHAVA_KRT:
            if row.adesha:
                by_adesha.setdefault(row.adesha, set()).add(row.sutra)
        self.assertEqual(by_adesha["ka"], {"3.3.41", "3.3.42"})
        self.assertEqual(by_adesha["vadha"], {"3.3.76"})
        self.assertEqual(by_adesha["ghana"],
                         {"3.3.77", "3.3.78", "3.3.82", "3.3.83"})
        self.assertEqual(by_adesha["gha"], {"3.3.84", "3.3.86"})

    def test_the_general_operation(self):
        vocalised = {r.sutra for r in BHAVA_KRT if r.samprasarana}
        self.assertEqual(vocalised, {"3.3.72", "3.3.73", "3.3.75"})

    def test_no_row_does_both(self):
        for row in BHAVA_KRT:
            with self.subTest(sutra=row.sutra):
                self.assertFalse(row.adesha and row.samprasarana)


class TheHeadingsExtentIsStatedOutright(unittest.TestCase):
    """
    3.3.56's vṛtti says how far 3.3.18 and 3.3.19 reach: भावे, अकर्तरि
    च कारक इति प्रकृतमनुवर्तते यावत् कृत्यल्युटो बहुलम् इति — to
    3.3.113. It NAMES the closing rule rather than giving a number, as
    3.2.134's आ क्वेः did.
    """

    def test_the_extent_is_recorded_where_it_is_stated(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.56").notes
        self.assertIn("यावत् कृत्यल्युटो बहुलम्", notes)
        self.assertIn("3.3.113", notes)

    def test_and_the_rule_it_names_confirms_the_extent(self):
        """
        PAID. 3.3.56 stated the extent fifty-seven sūtras early by
        NAMING the closing rule rather than giving a number, so the
        claim could be recorded and not checked. 3.3.113 says the same
        thing from the other end — भावे अकर्तरि च कारक इति निवृत्तम् —
        and the two now agree in the codification.

        The same shape as 3.2.134's आ क्वेः, which named 3.2.177 and
        was confirmed when that rule was read.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.113", {str(s.id) for s in REGISTRY.all()})
        self.assertIn("निवृत्तम्", REGISTRY.get("3.3.113").notes)
        self.assertIn("3.3.56", REGISTRY.get("3.3.113").notes)

    def test_a_heading_stopping_is_not_the_sense_stopping(self):
        """
        Written first as "no row past 3.3.113 states either heading",
        which 3.3.114 नपुंसके भावे क्तः falsifies one sūtra later.

        निवृत्तम् means the conditions stop RUNNING — later rules must
        SAY them if they want them, and three of the next four do.
        That is what an अधिकार is, and conflating it with the sense
        was the mistake.
        """
        after = {r.sutra: r for r in BHAVA_KRT
                 if int(r.sutra.rsplit(".", 1)[1]) > 113}
        self.assertTrue(after)
        stating = {s for s, r in after.items() if r.bhava}
        self.assertTrue(
            stating,
            "3.3.114 and after state भावे in their own words")
        self.assertIn("3.3.114", stating)

    def test_and_the_closing_is_recorded_at_both_ends(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("निवृत्तम्", REGISTRY.get("3.3.113").notes)
        self.assertIn("3.3.113", REGISTRY.get("3.3.114").notes)

    def test_the_debt_is_now_owed_by_seven_rules(self):
        """
        Not a count of seven: the property is that each of them names
        it, so the set can grow without this going stale.
        """
        from src.astadhyayi.sutra import REGISTRY

        leaning = {str(s.id) for s in REGISTRY.all()
                   if "3.3.113" in s.notes}
        self.assertTrue(
            {"3.2.53", "3.2.153", "3.3.24", "3.3.26", "3.3.43",
             "3.3.44", "3.3.56"} <= leaning)


class TheEntryPointsStillPartition(unittest.TestCase):
    """
    Seven kinds now in this pāda. What matters is not how many but
    that every registered rule falls in exactly one.
    """

    def test_every_rule_is_answered_by_exactly_one_entry_point(self):
        from src.astadhyayi.sutra import REGISTRY

        registered = {str(x.id) for x in REGISTRY.all()
                      if str(x.id).startswith("3.3.")}
        by_apply = {}
        for x in REGISTRY.all():
            if str(x.id).startswith("3.3."):
                by_apply.setdefault(x.apply.__name__, set()).add(
                    str(x.id))
        seen = set()
        for ids in by_apply.values():
            self.assertEqual(seen & ids, set())
            seen |= ids
        self.assertEqual(seen, registered)

    def test_the_pada_still_runs_unbroken_from_its_first_sutra(self):
        from src.astadhyayi.sutra import REGISTRY

        numbers = sorted(
            int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
            if str(s.id).startswith("3.3."))
        self.assertTrue(numbers)
        self.assertEqual(numbers, list(range(1, len(numbers) + 1)))



if __name__ == "__main__":
    unittest.main()
