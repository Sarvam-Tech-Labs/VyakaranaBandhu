# -*- coding: utf-8 -*-
"""
3.1.96 to 3.1.132 — the कृत्य affixes, and the forms fixed among them.

Expectations are the Kāśikā's worked forms and its *kim*
counter-examples. The interesting thing to hold here is the अपवाद
chain: three affixes cut into each other in BOTH directions, so a
first-match walk and a last-match walk each give wrong answers, and
only the text's own statements settle it.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.krtya import (
    ETYADI, GADADI, KRTYA, NIPATANA, NOT_RDUPADHA, YUVADI, _how_specific,
    krtya_affix, nipatana, provisions_for,
)


class TheFourAffixes(unittest.TestCase):

    def test_each_rule_answers_for_its_own_example(self):
        cases = (
            ("3.1.96", "tavyat", {}),
            ("3.1.97", "yat", dict(root_ends_in="ac")),
            ("3.1.98", "yat", dict(root_ends_in="pu", penult="a")),
            ("3.1.99", "yat", dict(root="śak")),
            ("3.1.100", "yat", dict(root="gad")),
            ("3.1.106", "kyap", dict(root="vad", upapada=True)),
            ("3.1.107", "kyap", dict(root="bhū", upapada=True,
                                     sense="bhāva")),
            ("3.1.108", "kyap", dict(root="han", upapada=True,
                                     sense="bhāva")),
            ("3.1.109", "kyap", dict(root="stu")),
            ("3.1.110", "kyap", dict(penult="ṛ")),
            ("3.1.111", "kyap", dict(root="khan")),
            ("3.1.112", "kyap", dict(root="bhṛ", sense="not-a-name")),
            ("3.1.113", "kyap", dict(root="mṛj")),
            ("3.1.118", "kyap", dict(root="grah", upasarga="prati",
                                     chandas=True)),
            ("3.1.119", "kyap", dict(root="grah", sense="grah-four")),
            ("3.1.120", "kyap", dict(root="kṛ")),
            ("3.1.124", "ṇyat", dict(root_ends_in="ṛ-or-hal")),
            ("3.1.125", "ṇyat", dict(root_ends_in="u",
                                     sense="āvaśyaka")),
            ("3.1.126", "ṇyat", dict(root="yu")),
        )
        for sutra, affix, where in cases:
            with self.subTest(sutra=sutra, **where):
                answer = krtya_affix(**where)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_only_four_affixes_are_given_in_the_whole_run(self):
        """
        तव्यत् (with तव्य and अनीयर् beside it), यत्, क्यप्, ण्यत्. A
        fifth appearing would mean a row had been miscopied.
        """
        self.assertEqual({row.gives for row in KRTYA},
                         {"tavyat", "yat", "kyap", "ṇyat"})

    def test_every_named_root_of_a_list_rule_is_reached(self):
        for group, sutra, extra in ((GADADI, "3.1.100", {}),
                                    (ETYADI, "3.1.109", {}),
                                    (YUVADI, "3.1.126", {})):
            for root in group:
                with self.subTest(sutra=sutra, root=root):
                    self.assertEqual(
                        krtya_affix(root=root, **extra).by, sutra)

    def test_3_1_96_holds_for_any_root_and_is_the_widest(self):
        """
        Asked with nothing said of the root, only 3.1.96 can answer —
        every other rule of the run states some condition.
        """
        self.assertEqual(krtya_affix().by, "3.1.96")
        self.assertEqual(_how_specific(provisions_for("3.1.96")[0]), 0)

    def test_two_rules_add_a_second_thing_besides_the_affix(self):
        """3.1.106's च gives यत् too; 3.1.108 and 3.1.111 add a sound."""
        self.assertTrue(krtya_affix(root="vad", upapada=True).also)
        self.assertTrue(krtya_affix(root="khan").also)
        self.assertFalse(krtya_affix(root="śak").also)

    def test_the_three_optional_rules_are_marked_so(self):
        optional = {"3.1.113", "3.1.120", "3.1.122"}
        for row in KRTYA:
            with self.subTest(sutra=row.sutra):
                self.assertEqual(row.optional, row.sutra in optional)


class TheApavadaChainCutsBothWays(unittest.TestCase):
    """
    3.1.98 is ण्यतोऽपवादः and 3.1.125 is यतोऽपवादः — यत् takes ground
    from ण्यत् and ण्यत् takes it back. So neither "first match" nor
    "last match" gives the text's answers, and the table follows what
    the vṛtti says of each rule.
    """

    def test_yat_takes_ground_from_nyat(self):
        """
        A labial-final root with a short अ before it would have gone to
        3.1.124 by being consonant-final; 3.1.98 gives it यत् instead.
        """
        self.assertEqual(krtya_affix(root_ends_in="ṛ-or-hal").gives,
                         "ṇyat")
        self.assertEqual(
            krtya_affix(root_ends_in="pu", penult="a").gives, "yat")

    def test_and_nyat_takes_it_back(self):
        """
        A उ-final root is vowel-final and 3.1.97 would give it यत्;
        3.1.125 gives ण्यत् where a thing must be done.
        """
        self.assertEqual(krtya_affix(root_ends_in="u").by, "3.1.96",
                         "with no sense said, neither reaches it")
        self.assertEqual(
            krtya_affix(root_ends_in="u", sense="āvaśyaka").gives,
            "ṇyat")

    def test_3_1_109_is_weighted_to_beat_a_later_rule(self):
        """
        क्यबिति वर्तमाने पुनः क्यब्ग्रहणं बाधकबाधनार्थम् — the affix is
        named a second time so that 3.1.125's ण्यत् cannot displace it.
        A rule repeated to survive a LATER one, which is the reverse of
        the usual reason, so the row carries a weight its conditions
        alone would not give it.
        """
        stu = next(r for r in KRTYA if r.sutra == "3.1.109")
        nyat = next(r for r in KRTYA if r.sutra == "3.1.125")
        self.assertGreater(_how_specific(stu), _how_specific(nyat),
                           "without the extra weight 3.1.125 would win "
                           "and अवश्यस्तुत्यः would be lost")
        self.assertEqual(
            krtya_affix(root="stu", sense="āvaśyaka").by, "3.1.109")


class TheConditionsAreLive(unittest.TestCase):

    def test_3_1_100_needs_no_preverb(self):
        """अनुपसर्ग इति किम्? प्रगाद्यम्, प्रमाद्यम्."""
        self.assertEqual(krtya_affix(root="gad").by, "3.1.100")
        # प्रगाद्यम् is the vṛtti's own counter-form, and it is a ण्यत्
        # form: with the preverb on, गद् is simply a consonant-final
        # root and 3.1.124 answers. "Only 3.1.96 is left" was my
        # assumption, not the text's.
        self.assertEqual(krtya_affix(root="gad", upasarga="pra").by,
                         "3.1.124",
                         "प्रगाद्यम् — the ण्यत् form the vṛtti gives")

    def test_3_1_110_excepts_two_roots_that_have_its_shape(self):
        """अक्ऌपिचृतेरिति किम्? कल्प्यम्, चर्त्यम्."""
        self.assertEqual(krtya_affix(penult="ṛ").by, "3.1.110")
        for root in NOT_RDUPADHA:
            with self.subTest(root=root):
                self.assertNotEqual(
                    krtya_affix(root=root, penult="ṛ").by, "3.1.110")

    def test_3_1_125_needs_its_sense(self):
        """आवश्यक इति किम्? लव्यम्."""
        self.assertEqual(
            krtya_affix(root_ends_in="u", sense="āvaśyaka").by, "3.1.125")
        self.assertNotEqual(krtya_affix(root_ends_in="u").by, "3.1.125")

    def test_3_1_118_holds_in_the_veda_and_after_two_preverbs(self):
        """छन्दसीति किम्? प्रतिग्राह्यम्, अपिग्राह्यम्."""
        for preverb in ("prati", "api"):
            with self.subTest(upasarga=preverb):
                self.assertEqual(
                    krtya_affix(root="grah", upasarga=preverb,
                                chandas=True).by, "3.1.118")
        self.assertNotEqual(
            krtya_affix(root="grah", upasarga="prati").by, "3.1.118")

    def test_the_upapada_rules_need_a_word_beside_them(self):
        """
        सुपीति किम्? वाद्यम्, घातः. And the सुबन्त they want is what
        3.1.92 calls an उपपद, so this run is where that heading first
        does work.
        """
        for root, sense in (("vad", ""), ("bhū", "bhāva"),
                            ("han", "bhāva")):
            with self.subTest(root=root):
                where = dict(root=root)
                if sense:
                    where["sense"] = sense
                self.assertNotEqual(
                    krtya_affix(**where).by,
                    krtya_affix(upapada=True, **where).by)


class TheFormsFixedWhole(unittest.TestCase):
    """
    यदिह लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम् — whatever the
    rules do not reach, the fixing supplies. Seventeen of the run's
    thirty-seven rules do this, and they answer through their own entry
    point because a table that derived them would be pretending.
    """

    def test_each_answers_for_itself_and_names_its_forms(self):
        for sutra in NIPATANA:
            with self.subTest(sutra=sutra):
                answer = nipatana(sutra)
                self.assertEqual(answer.by, sutra)
                self.assertTrue(answer.gives)
                self.assertTrue(answer.why)

    def test_they_speak_about_no_other_rule(self):
        for sutra in ("3.1.96", "3.1.124", "2.1.1"):
            with self.subTest(sutra=sutra):
                self.assertEqual(nipatana(sutra).by, "")

    def test_none_of_them_is_also_in_the_affix_table(self):
        """
        A rule that both fixed a form and added an affix would be
        answered twice, and the two answers could drift apart.
        """
        in_table = {row.sutra for row in KRTYA}
        self.assertEqual(in_table & set(NIPATANA), set())

    def test_the_run_is_covered_by_exactly_one_of_the_two(self):
        """
        Every sūtra from 3.1.96 to 3.1.132 either adds an affix or fixes
        a form. A gap would be a rule nobody had read.
        """
        in_table = {row.sutra for row in KRTYA}
        for n in range(96, 133):
            sutra = f"3.1.{n}"
            with self.subTest(sutra=sutra):
                self.assertEqual(
                    (sutra in in_table) + (sutra in NIPATANA), 1,
                    "each rule belongs to exactly one of the two")

    def test_the_largest_one_fixes_eighteen_forms(self):
        """
        3.1.123 names eighteen Vedic words in a single sūtra — the
        longest in the pāda, and the vṛtti states the principle rather
        than deriving them one by one.
        """
        forms, _why = NIPATANA["3.1.123"]
        self.assertEqual(len(forms), 18)


class TheTableIsWellFormed(unittest.TestCase):

    def test_every_row_names_a_sutra_of_this_run(self):
        for row in KRTYA:
            with self.subTest(sutra=row.sutra):
                self.assertRegex(row.sutra,
                                 r"^3\.1\.(9[6-9]|1[0-2]\d|13[0-2])$")
                self.assertTrue(row.gives)
                self.assertTrue(row.why)

    def test_the_rows_are_in_the_texts_own_order(self):
        def order(sid):
            return tuple(int(p) for p in sid.split("."))

        seen = [order(r.sutra) for r in KRTYA]
        self.assertEqual(seen, sorted(seen))

    def test_the_specificity_scores_are_numbers_and_they_differ(self):
        """
        The same trap as the aorist table's ranking: a sum written with
        an unparenthesised comparison collapses to a bool and every row
        scores alike, leaving the ranking doing nothing.
        """
        scores = [_how_specific(row) for row in KRTYA]
        self.assertTrue(
            all(isinstance(s, int) and not isinstance(s, bool)
                for s in scores),
            "a bool means the sum collapsed into a comparison")
        self.assertGreater(len(set(scores)), 1)


class ThePadaIsComplete(unittest.TestCase):

    def test_3_1_runs_unbroken_from_one_to_one_hundred_and_thirty_two(self):
        """
        The heading at 3.1.95 stops before 3.1.133, so this run closes
        the section it opened. Checked as a property over the registry.
        """
        from src.astadhyayi.sutra import REGISTRY

        numbers = sorted(
            int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
            if str(s.id).startswith("3.1."))
        self.assertEqual([n for n in numbers if n <= 132],
                         list(range(1, 133)))

    def test_the_two_rules_that_use_the_krtya_name_still_hold(self):
        """
        2.1.33 and 2.3.71 invoke कृत्य, and 3.1.95 confers it. Both were
        codified before the heading; the affixes they speak of are now
        here too.
        """
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("2.1.33", "2.3.71", "3.1.95"):
            self.assertTrue(REGISTRY.has(sutra))


if __name__ == "__main__":
    unittest.main()
