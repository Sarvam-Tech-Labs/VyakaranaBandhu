# -*- coding: utf-8 -*-
"""
3.3.82 to 3.3.113 — हन् with its substitutes, the feminine affixes,
and the rule that closes the two headings.

What this block asserts that no earlier one could:

  * a rule naming its roots by a संज्ञā conferred three adhyāyas back,
    and the resolver ASKING that rule for them;
  * a whole sūtra existing for an accent and nothing else;
  * a commentary answering "why is the wording like that?" with
    "for variety";
  * an ambiguity between two roots settled from REDUNDANCY rather
    than from sense;
  * a debt six rules had been carrying, paid.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.bhava_krt import (
    BHAVA_KRT, BHIDADI, bhava_affix, krtya_lyut_bahulam, nipatana,
)
from src.astadhyayi.upapada_krt import Added, NotAdded


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.3.82", "ap", dict(root="han", upasarga="vi",
                              karaka="karaṇa")),
        ("3.3.83", "ka", dict(root="han", upasarga="stamba",
                              karaka="karaṇa")),
        ("3.3.84", "ap", dict(root="han", upasarga="pari",
                              karaka="karaṇa")),
        ("3.3.86", "ap", dict(root="han", upasarga="sam",
                              sense="praśaṃsā", names_a="gaṇa")),
        ("3.3.88", "ktri", dict(root="pac", marked="ḍvit")),
        ("3.3.89", "athuc", dict(root="vep", marked="ṭvit")),
        ("3.3.90", "naṅ", dict(root="yaj")),
        ("3.3.91", "nan", dict(root="svap")),
        ("3.3.92", "ki", dict(root="ḍudāñ", upasarga="pra")),
        ("3.3.93", "ki", dict(root="ḍudhāñ", karaka="adhikaraṇa")),
        ("3.3.94", "ktin", dict(root="kṛ", stri=True)),
        ("3.3.95", "ktin", dict(root="sthā", stri=True, bhava=True)),
        ("3.3.96", "ktin", dict(root="vṛṣ", stri=True, bhava=True,
                                mantra=True)),
        ("3.3.98", "kyap", dict(root="vraj", stri=True, bhava=True)),
        ("3.3.99", "kyap", dict(root="sam-aj", stri=True,
                                samjna=True)),
        ("3.3.100", "śa", dict(root="kṛñ", stri=True)),
        ("3.3.102", "a", dict(root="cikīrṣ", stri=True,
                              pratyayanta=True)),
        ("3.3.103", "a", dict(root="kuṇḍ", stri=True, gurumat=True,
                              hal_final=True)),
        ("3.3.104", "aṅ", dict(root="vidā", stri=True)),
        ("3.3.105", "aṅ", dict(root="cint", stri=True)),
        ("3.3.106", "aṅ", dict(root="dā", stri=True, root_final="ā",
                               upasarga="pra")),
        ("3.3.107", "yuc", dict(root="ās", stri=True)),
        ("3.3.108", "ṇvul", dict(root="pra-chard", names_a="roga")),
        ("3.3.109", "ṇvul", dict(root="bhañj", samjna=True)),
        ("3.3.110", "iñ", dict(root="kṛ", sense="paripraśna")),
        ("3.3.111", "ṇvuc", dict(root="bhakṣ", sense="ṛṇa")),
        ("3.3.112", "ani", dict(root="kṛ", upasarga="nañ",
                                sense="ākrośa")),
        # --- 3.3.114 onward: the neuter and the masculine ---------
        ("3.3.114", "kta", dict(root="has", napumsaka=True,
                                bhava=True, wants="kta")),
        ("3.3.115", "lyuṭ", dict(root="has", napumsaka=True,
                                 bhava=True, wants="lyuṭ")),
        ("3.3.116", "lyuṭ", dict(root="pā", napumsaka=True,
                                 bhava=True, sense="sukha",
                                 karaka="karman")),
        ("3.3.117", "lyuṭ", dict(root="duh", karaka="karaṇa")),
        ("3.3.118", "gha", dict(root="kṛ", pum=True, samjna=True,
                                karaka="karaṇa")),
        ("3.3.120", "ghañ", dict(root="tṝ", upasarga="ava", pum=True,
                                 samjna=True, karaka="karaṇa")),
        ("3.3.121", "ghañ", dict(root="bandh", pum=True, samjna=True,
                                 karaka="karaṇa", hal_final=True)),
        ("3.3.125", "gha", dict(root="khan", karaka="karaṇa")),
        ("3.3.126", "khal", dict(root="kṛ", isadadi=True)),
        ("3.3.127", "khal", dict(root="kṛñ", isadadi=True,
                                 karaka="kartṛ")),
        ("3.3.128", "yuc", dict(root="pā", isadadi=True,
                                root_final="ā")),
        ("3.3.129", "yuc", dict(root="sad", isadadi=True,
                                gati_artha=True, chandasi=True)),
        ("3.3.130", "yuc", dict(root="yudh", gati_artha=True,
                                chandasi=True)),
    )

    def test_every_rule_answers_and_gives_what_it_says(self):
        for sutra, gives, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = bhava_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)


class NoCounterExampleReachesTheRuleItCounters(unittest.TestCase):

    COUNTERS = (
        ("3.3.83", dict(root="han", upasarga="stamba"), "stambaghātaḥ"),
        ("3.3.86", dict(root="han", upasarga="sam"), "saṃghātaḥ"),
        ("3.3.92", dict(root="pac", upasarga="pra"), "not a ghu root"),
        ("3.3.92", dict(root="ḍudāñ"), "no preverb"),
        ("3.3.103", dict(root="bhaj", stri=True, hal_final=True),
         "bhaktiḥ"),
        ("3.3.103", dict(root="nī", stri=True, gurumat=True),
         "nītiḥ"),
        ("3.3.110", dict(root="kṛ"), "kṛtiḥ"),
        ("3.3.112", dict(root="mṛ", sense="ākrośa"),
         "mṛtis te vṛṣala bhūyāt"),
        ("3.3.112", dict(root="kṛ", upasarga="nañ"), "akṛtis tasya"),
    )

    def test_none_of_them_reaches_it(self):
        for sutra, where, form in self.COUNTERS:
            with self.subTest(sutra=sutra, form=form):
                self.assertNotEqual(bhava_affix(**where).by, sutra)


class ARuleNamingItsRootsByASamjna(unittest.TestCase):
    """
    3.3.92 and 3.3.93 want a root called घु, and 1.1.20 दाधा घ्वदाप्
    confers that name. The rows list no roots — the resolver asks. The
    same treatment 3.3.14 gave 3.2.127's सत्.
    """

    def test_the_rows_list_no_roots(self):
        for sutra in ("3.3.92", "3.3.93"):
            with self.subTest(sutra=sutra):
                row = next(r for r in BHAVA_KRT if r.sutra == sutra)
                self.assertEqual(row.of, ())
                self.assertTrue(row.ghu)

    def test_and_the_class_really_comes_from_1_1_20(self):
        from src.astadhyayi.samjna import ghu_roots, is_ghu

        self.assertTrue(ghu_roots())
        for root in ghu_roots():
            with self.subTest(root=root):
                self.assertTrue(is_ghu(root))
                self.assertEqual(
                    bhava_affix(root=root, upasarga="pra").by,
                    "3.3.92")

    def test_a_root_outside_the_class_is_not_reached(self):
        from src.astadhyayi.samjna import is_ghu

        self.assertFalse(is_ghu("pac"))
        self.assertNotEqual(
            bhava_affix(root="pac", upasarga="pra").by, "3.3.92")

    def test_and_the_dependence_is_declared(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("1.1.20", REGISTRY.get("3.3.92").reuses)


class AWholeSutraForAnAccent(unittest.TestCase):
    """
    3.3.96's affix comes from 3.3.94 already — सर्वत्र सर्वधातुभ्यः
    सामान्येन विहित एव क्तिन्, उदात्तार्थं वचनम्. The rule exists to
    make it उदात्त in a mantra.

    The fifth accent-only statement of the pāda and the first that is
    a whole sūtra: 3.3.57's प, 3.3.58's निश्चि, 3.3.91's न and
    3.3.111's whole affix were the others.
    """

    def test_the_ground_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.96").notes
        self.assertIn("उदात्तार्थं वचनम्", notes)

    def test_the_affix_is_the_one_3_3_94_already_gives(self):
        general = bhava_affix(root="vṛṣ", stri=True)
        in_mantra = bhava_affix(root="vṛṣ", stri=True, bhava=True,
                                mantra=True)
        self.assertEqual(general.by, "3.3.94")
        self.assertEqual(in_mantra.by, "3.3.96")
        self.assertEqual(general.gives, in_mantra.gives)

    def test_all_five_accent_only_statements_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra, phrase in (
            ("3.3.57", "स्वरार्थम्"),
            ("3.3.58", "स्वरार्थम्"),
            ("3.3.91", "स्वरार्थः"),
            ("3.3.96", "उदात्तार्थं"),
            ("3.3.111", "स्वरार्थम्"),
        ):
            with self.subTest(sutra=sutra):
                self.assertIn(phrase, REGISTRY.get(sutra).notes)

    def test_and_none_of_them_can_be_checked_against_the_corpus(self):
        """
        The sūtrapāṭha on disk is unaccented, which NORTH_STAR §7
        states as a boundary. So five claims are recorded and none is
        verifiable — worth asserting, because a claim that cannot fail
        should be known not to.
        """
        from src.astadhyayi.corpus import load_vidyut_sutrapatha

        text = load_vidyut_sutrapatha()["3.3.96"].text
        for mark in ("॑", "॒", "̀", "́"):
            with self.subTest(mark=repr(mark)):
                self.assertNotIn(mark, text)


class WhyIsTheWordingLikeThat(unittest.TestCase):
    """
    3.3.96's cases do not construe as written —
    प्रकृतिप्रत्यययोर्विभक्तिविपरिणामेन संबन्धः. Asked why, the vṛtti
    answers वैचित्र्यार्थम्, for variety. Not an argument, and honest.
    """

    def test_the_question_and_the_answer_are_both_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.96").notes
        self.assertIn("विभक्तिविपरिणामेन", notes)
        self.assertIn("वैचित्र्यार्थम्", notes)


class AnAmbiguitySettledFromRedundancy(unittest.TestCase):
    """
    3.3.107 has two roots spelt श्रन्थ. The क्र्यादि one is meant, and
    the ground is not the sense: ण्यन्तत्वेनैव सिद्धत्वात् — the
    चुरादि one would ALREADY be covered by the rule's own ण्यन्त half,
    so reading it there makes the rule say nothing new.

    Elsewhere this project settled such a case from the sense
    (3.2.162's साहचर्यात्) or from usage (3.3.30's अनभिधानात्). This is
    a third ground.
    """

    def test_the_reasoning_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.107").notes
        self.assertIn("ण्यन्तत्वेनैव सिद्धत्वात्", notes)

    def test_and_the_same_ground_is_used_again_in_one_varttika(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("घट्ट", REGISTRY.get("3.3.107").notes)

    def test_the_four_grounds_are_on_record_where_they_belong(self):
        """
        Written first as three, with साहचर्यात् put at 3.2.162 — which
        says स्वभावात्. Two different grounds merged into one wrong
        citation, and the test caught it because it named the place.
        """
        from src.astadhyayi.sutra import REGISTRY

        for phrase, sutras in (
            ("साहचर्यात्", ("3.2.59", "3.2.61")),
            ("स्वभावात्", ("3.2.161", "3.2.162")),
            ("अनभिधानात्", ("3.3.30",)),
            ("सिद्धत्वात्", ("3.3.107",)),
        ):
            for sutra in sutras:
                with self.subTest(ground=phrase, sutra=sutra):
                    self.assertIn(phrase, REGISTRY.get(sutra).notes)

    def test_and_3_3_107_now_names_the_other_three_correctly(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.107").notes
        for sutra in ("3.2.59", "3.2.161", "3.3.30"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, notes)
        self.assertNotIn("3.2.162's साहचर्यात्", notes)


class TheFifthVasarupaSuspensionStatesItsOwnLimit(unittest.TestCase):
    """
    3.2.146, 3.2.177, 3.3.10 and 3.3.44 each suspended 3.1.94 over
    ground the commentary marked out by argument. 3.3.107 bounds it in
    the rule's own words: वासरूपप्रतिषेधश्च
    स्त्रीप्रकरणविषयस्यैवोत्सर्गापवादस्य.
    """

    def test_the_bounded_one_says_where_it_stops(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.107").notes
        self.assertIn("स्त्रीप्रकरणविषयस्यैव", notes)

    def test_and_the_four_before_it_are_all_still_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.2.146", "3.2.177", "3.3.10", "3.3.44"):
            with self.subTest(sutra=sutra):
                self.assertIn("वासरूप", REGISTRY.get(sutra).notes)


class ThreeGanasOnDiskAndOneCopiedByHand(unittest.TestCase):
    """
    The गणपाठ keys गम्यादि to 3.3.3, भिदादि to 3.3.104 and संपदादि to
    3.3.108. 3.2.5 and 3.2.15 taught that the corpus is the authority
    for its own lists; 3.3.3 was typed out anyway and lost a member.
    """

    def test_both_lists_now_come_from_the_corpus(self):
        from src.astadhyayi.corpus import load_ganapatha
        from src.astadhyayi.unadi import GAMYADI

        ganas = load_ganapatha()
        from_corpus = tuple(
            item for gana in ganas.get("3.3.3", ())
            for item in gana.items)
        self.assertEqual(GAMYADI, from_corpus)
        self.assertTrue(GAMYADI)

        bhid = tuple(item for gana in ganas.get("3.3.104", ())
                     for item in gana.items)
        self.assertEqual(BHIDADI, bhid)
        self.assertTrue(BHIDADI)

    def test_every_member_of_bhidadi_reaches_its_rule(self):
        for root in BHIDADI:
            with self.subTest(root=root):
                self.assertEqual(
                    bhava_affix(root=root, stri=True).by, "3.3.104")

    def test_the_scar_names_the_two_rules_that_taught_it(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.104").notes
        self.assertIn("3.2.5", notes)
        self.assertIn("3.3.3", notes)


class FourMoreWordsGivenWhole(unittest.TestCase):
    """3.3.85, 3.3.87, 3.3.97 and 3.3.101."""

    def test_each_answers_from_its_own_rule(self):
        for word, sutra in (("parvatopaghna", "3.3.85"),
                            ("nigha", "3.3.87"),
                            ("ūti", "3.3.97"),
                            ("icchā", "3.3.101")):
            with self.subTest(word=word):
                self.assertEqual(nipatana(word).by, sutra)

    def test_one_of_them_fixes_six_words_for_six_reasons(self):
        why = nipatana("ūti").why
        for ground in ("ऊठ्", "lengthen", "स्वरार्थ"):
            with self.subTest(ground=ground):
                self.assertIn(ground, why)

    def test_and_3_3_96_pointed_forward_to_one_of_them(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("इच्छा", REGISTRY.get("3.3.96").notes)
        self.assertIn("3.3.96", REGISTRY.get("3.3.101").notes)


class EveryRowOfTheTableIsExercised(unittest.TestCase):
    """
    A row added without a worked case fails here.

    ONE copy, in the newest block's file, reading EVERY block's cases.
    It has now been moved twice for the same reason — a check naming a
    subset of the work goes stale as soon as there is more work — so
    the fix is not to move it again but to have it read the lot.
    """

    def _covered(self):
        from tests.test_astadhyayi_bhava_krt import (
            EachRuleAnswersForItsOwnExample as First,
        )
        from tests.test_astadhyayi_bhava_krt_2 import (
            EachRuleAnswersForItsOwnExample as Second,
        )
        from tests.test_astadhyayi_bhava_krt_3 import (
            EachRuleAnswersForItsOwnExample as Third,
        )

        covered = {sutra for sutra, _ in First.CASES}
        for block in (Second, Third,
                      EachRuleAnswersForItsOwnExample):
            covered |= {sutra for sutra, _, _ in block.CASES}
        return covered

    def test_the_table_and_the_worked_cases_cover_the_same_rules(self):
        self.assertEqual(self._covered(),
                         {r.sutra for r in BHAVA_KRT})

    def test_and_that_is_every_rule_registered_to_this_entry_point(self):
        from src.astadhyayi.sutra import REGISTRY

        registered = {str(x.id) for x in REGISTRY.all()
                      if x.apply is bhava_affix}
        self.assertEqual(registered, {r.sutra for r in BHAVA_KRT})


class TheHeadingEndsWhereItSaidItWould(unittest.TestCase):
    """
    3.3.113 closes the two headings. It does NOT end the run — rules
    after it go on giving affixes on the same ground, and simply have
    to state their conditions rather than inheriting them.
    """

    def test_the_table_continues_past_it(self):
        numbers = [int(r.sutra.rsplit(".", 1)[1]) for r in BHAVA_KRT]
        self.assertTrue(numbers)
        self.assertGreater(
            max(numbers), 113,
            "the run does not stop at 3.3.113 — only the headings do")

    def test_and_3_3_113_answers_from_its_own_entry_point(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertEqual(REGISTRY.get("3.3.113").apply.__name__,
                         "krtya_lyut_bahulam")
        self.assertNotIn("3.3.113", {r.sutra for r in BHAVA_KRT})

    def test_it_is_asked_for_a_kind_and_not_for_a_condition(self):
        answer = krtya_lyut_bahulam("kṛtya-kāraka")
        self.assertIsInstance(answer, Added)
        self.assertIsInstance(krtya_lyut_bahulam("bhāva"), NotAdded)


if __name__ == "__main__":
    unittest.main()
