# -*- coding: utf-8 -*-
"""
2.4.58 to 2.4.71 — affixes added and then taken away.

Expectations are the Kāśikā's worked forms and its *kim*
counter-examples. Two claims in the notes are about something other
than the rule that states them — a ज्ञापन landing on 2.4.60, and a
gaṇa on disk that the codification refuses to use — and both are held
here, since neither can be checked by running the rule it belongs to.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.anga import Elided
from src.astadhyayi.taddhita_luk import (
    ATRYADI, GOPAVANADI, NYADI_STEMS, PAILADI, Renamed, TAULVALYADI,
    TIKAKITAVADI, UPAKADI, YASKADI, sup_luk, taddhita_luk,
)


class TheYuvanAffixIsDropped(unittest.TestCase):
    """2.4.58 to 2.4.60, so that father and son are called alike."""

    def test_each_rule_answers_for_its_own_example(self):
        cases = (
            ("2.4.58", dict(descendant="yuvan", stem_kind="ṇya",
                            affix="iñ")),
            ("2.4.59", dict(descendant="yuvan", stem=PAILADI[0])),
            ("2.4.60", dict(descendant="yuvan", affix="iñ",
                            region="prāc")),
        )
        for sutra, where in cases:
            with self.subTest(sutra=sutra):
                answer = taddhita_luk(**where)
                self.assertEqual(answer.by, sutra)
                self.assertTrue(answer.elided)
                self.assertEqual(answer.elision, "luk")

    def test_all_four_stem_kinds_of_2_4_58_are_reached(self):
        for kind in NYADI_STEMS:
            for affix in ("aṇ", "iñ"):
                with self.subTest(stem_kind=kind, affix=affix):
                    self.assertEqual(
                        taddhita_luk(descendant="yuvan", stem_kind=kind,
                                     affix=affix).by, "2.4.58")

    def test_a_stem_kind_the_sutra_does_not_name_is_not_reached(self):
        self.assertEqual(
            taddhita_luk(descendant="yuvan", stem_kind="brāhmaṇa-gotra",
                         affix="iñ").by, "")

    def test_2_4_60_holds_among_the_easterners_only(self):
        """प्राचामिति किम्? दाक्षिः पिता, दाक्षायणः पुत्रः."""
        self.assertEqual(
            taddhita_luk(descendant="yuvan", affix="iñ").by, "",
            "without a region 2.4.60 must not fire — that is what "
            "प्राचाम् is for")

    def test_it_is_not_optional(self):
        """
        गोत्रविशेषणं प्राग्ग्रहणम्, न विकल्पार्थम्. The other reading was
        available and the vṛtti rejects it by name, so an optional
        answer here would be the misreading it warns against.
        """
        answer = taddhita_luk(descendant="yuvan", affix="iñ",
                              region="prāc")
        self.assertTrue(answer.elided)
        self.assertFalse(getattr(answer, "optional", False))


class TheJnapanaAt2466(unittest.TestCase):
    """
    A claim stated at one sūtra about a different one.

    भरत is already among the प्राच्, so 2.4.66 naming both is redundant
    — and the vṛtti reads the redundancy as teaching: भरताः प्राच्या
    एव, तेषां पुनर्ग्रहणं ज्ञापनार्थम् — अन्यत्र प्राग्ग्रहणे भरतग्रहणं
    न भवति. What it teaches lands on 2.4.60, so running 2.4.66 cannot
    check it.
    """

    def test_2_4_60_does_not_reach_the_bharatas(self):
        """आर्जुनिः पिता, आर्जुनायनः पुत्रः — the two stay different."""
        answer = taddhita_luk(descendant="yuvan", affix="iñ",
                              region="bharata")
        self.assertFalse(
            answer.elided,
            "if 2.4.60 reached the Bharatas, आर्जुनायनः would collapse "
            "into आर्जुनिः and the ज्ञापन would have bought nothing")
        self.assertEqual(answer.by, "", "no rule acted, so none is named")

    def test_but_2_4_66_itself_does_reach_them(self):
        """
        The other half: the ज्ञापन must not cost 2.4.66 the Bharatas it
        actually names. युधिष्ठिराः, अर्जुनाः.
        """
        answer = taddhita_luk(descendant="gotra", affix="iñ", bahvac=True,
                              region="bharata", plural=True)
        self.assertEqual(answer.by, "2.4.66")
        self.assertTrue(answer.elided)

    def test_and_the_easterners_are_reached_by_both(self):
        self.assertEqual(
            taddhita_luk(descendant="yuvan", affix="iñ",
                         region="prāc").by, "2.4.60")
        self.assertEqual(
            taddhita_luk(descendant="gotra", affix="iñ", bahvac=True,
                         region="prācya", plural=True).by, "2.4.66")


class TheThreeConditionsOfThePluralRun(unittest.TestCase):
    """
    बहुषु, अस्त्रियाम् and तेनैव run through 2.4.62 to 2.4.70, and the
    Kāśikā gives a counter for each. A form can fail any one alone, so
    each is checked alone and each refusal says which one failed.
    """

    WORKED = dict(affix="tadrāja", plural=True)

    def test_all_three_together_give_the_elision(self):
        answer = taddhita_luk(**self.WORKED)
        self.assertEqual(answer.by, "2.4.62")
        self.assertTrue(answer.elided)

    def test_each_one_removed_refuses_on_its_own(self):
        for broken, why in (
            (dict(affix="tadrāja"), "बहुष्विति किम्? आङ्गः"),
            (dict(affix="tadrāja", plural=True, feminine=True),
             "अस्त्रियामिति किम्? आङ्ग्यः स्त्रियः"),
            (dict(affix="tadrāja", plural=True, by_that_affix=False),
             "तेनैवग्रहणं किम्? प्रियवाङ्गाः"),
        ):
            with self.subTest(why=why):
                answer = taddhita_luk(**broken)
                self.assertFalse(answer.elided)
                self.assertEqual(answer.by, "",
                                 "no rule acted, so none is named")

    def test_they_hold_for_every_rule_of_the_run_and_not_just_2_4_62(self):
        """
        The three are carried down, so a rule further along must fail
        them too. Checked over several rules rather than asserted of
        one, since anuvṛtti is the claim being tested.
        """
        further = (
            dict(descendant="gotra", stem=YASKADI[0]),
            dict(descendant="gotra", affix="yañ"),
            dict(descendant="gotra", stem=ATRYADI[0]),
            dict(stem=UPAKADI[0]),
        )
        for where in further:
            with self.subTest(**where):
                self.assertTrue(taddhita_luk(plural=True, **where).elided)
                self.assertFalse(taddhita_luk(**where).elided)
                self.assertFalse(
                    taddhita_luk(plural=True, feminine=True, **where).elided)


class ThePluralRunAnswersFromTheRightRule(unittest.TestCase):

    def test_each_rule_answers_for_its_own_example(self):
        cases = (
            ("2.4.62", dict(affix="tadrāja")),
            ("2.4.63", dict(descendant="gotra", stem=YASKADI[0])),
            ("2.4.64", dict(descendant="gotra", affix="yañ")),
            ("2.4.64", dict(descendant="gotra", affix="añ")),
            ("2.4.66", dict(descendant="gotra", affix="iñ", bahvac=True,
                            region="prācya")),
            ("2.4.68", dict(stem=TIKAKITAVADI[0], dvandva=True)),
            ("2.4.69", dict(stem=UPAKADI[0])),
            ("2.4.70", dict(stem="āgastya")),
        )
        for sutra, where in cases:
            with self.subTest(sutra=sutra):
                self.assertEqual(taddhita_luk(plural=True, **where).by,
                                 sutra)

    def test_all_six_rsis_of_2_4_65_are_reached(self):
        for name in ATRYADI:
            with self.subTest(stem=name):
                self.assertEqual(
                    taddhita_luk(descendant="gotra", stem=name,
                                 plural=True).by, "2.4.65")

    def test_2_4_66_needs_many_syllables(self):
        """बह्वच इति किम्? बैकयः, पौष्पयः."""
        self.assertEqual(
            taddhita_luk(descendant="gotra", affix="iñ", region="prācya",
                         plural=True).by, "",
            "without बह्वच् the rule must not reach it")

    def test_the_gotra_condition_at_2_4_64_is_live(self):
        """गोत्र इत्येव — द्वैप्याः and औत्साश्छात्राः keep their affix."""
        self.assertEqual(
            taddhita_luk(affix="yañ", plural=True).by, "",
            "यञ् in another sense is not a gotra affix")


class TheTwoProhibitions(unittest.TestCase):
    """
    A प्रतिषेध refusing is that rule ACTING, so it reports itself — the
    same standing as 2.4.14 and 2.4.15. And each must be read BEFORE
    the rule it refuses, or it could never fire.
    """

    def test_2_4_61_refuses_what_2_4_60_would_have_given(self):
        without = taddhita_luk(descendant="yuvan", affix="iñ",
                               region="prāc")
        self.assertEqual(without.by, "2.4.60")
        self.assertTrue(without.elided)

        refused = taddhita_luk(descendant="yuvan", stem=TAULVALYADI[0],
                               affix="iñ", region="prāc")
        self.assertEqual(refused.by, "2.4.61")
        self.assertFalse(refused.elided)
        self.assertEqual(refused.elision, "")

    def test_2_4_67_refuses_what_2_4_64_would_have_given(self):
        without = taddhita_luk(descendant="gotra", affix="añ", plural=True)
        self.assertEqual(without.by, "2.4.64")
        self.assertTrue(without.elided)

        refused = taddhita_luk(descendant="gotra", stem=GOPAVANADI[0],
                               affix="añ", plural=True)
        self.assertEqual(refused.by, "2.4.67")
        self.assertFalse(refused.elided)


class TheGopavanadiOnDiskIsNotWhatIsCodified(unittest.TestCase):
    """
    The second defective gaṇa this pāda has turned up.

    The file holds eleven entries, one of them the bare string "1" — a
    parse artifact — with spelling variants beside it. The vṛtti fixes
    the extent at eight, names them, and says what the surplus is:
    परिशिष्टानां हरितादीनां प्रमादपाठः, ते हि चतुर्थे बिदादिषु पठ्यन्ते,
    तेभ्यश्च बहुषु लुग् भवत्येव. Reading the file straight would have
    made this prohibition block the very forms the commentary says it
    must allow.
    """

    @staticmethod
    def _on_disk():
        from src.astadhyayi.samasa import _gana

        return _gana("2.4.67", "gopavanādi")

    def test_the_codified_list_is_the_vrttis_eight(self):
        self.assertEqual(len(GOPAVANADI), 8,
                         "एतावन्त एवाष्टौ गोपवनादयः")

    def test_the_disk_list_still_disagrees(self):
        """
        If the corpus is ever corrected this goes red, which is exactly
        when the note should be revisited rather than left standing.
        """
        disk = self._on_disk()
        self.assertNotEqual(
            tuple(sorted(disk)), tuple(sorted(GOPAVANADI)),
            "the gaṇapāṭha now agrees with the vṛtti — reread the note "
            "on 2.4.67 and take the list from disk if it is right")

    def test_the_disk_list_carries_a_parse_artifact(self):
        """
        The concrete defect, named. A bare "1" is not a word in any
        reading, so this is a corpus error and not a variant.
        """
        self.assertIn("1", self._on_disk())
        self.assertNotIn("1", GOPAVANADI)

    def test_the_words_the_vrtti_excludes_do_take_the_elision(self):
        """
        हरिताः, किंदासाः — the point of refusing the longer list. These
        are बिदादि words, so 2.4.64's अञ् reaches them and 2.4.67 must
        not stand in the way.
        """
        for word in ("harita", "kiṃdāsa"):
            with self.subTest(stem=word):
                self.assertNotIn(word, GOPAVANADI)
                answer = taddhita_luk(descendant="gotra", stem=word,
                                      affix="añ", plural=True)
                self.assertEqual(answer.by, "2.4.64")
                self.assertTrue(answer.elided)


class TheDvandvaSplitBetween2468And2469(unittest.TestCase):
    """
    अद्वन्द्वग्रहणं द्वन्द्वाधिकारनिवृत्त्यर्थम् — अद्वन्द्वे is there to
    cancel the heading 2.4.68 set up. Three words are in both lists,
    and for those the elision divides: obligatory inside a द्वन्द्व by
    the earlier rule, a choice outside it by the later one.
    """

    def test_2_4_69_holds_outside_a_dvandva(self):
        answer = taddhita_luk(stem=UPAKADI[0], plural=True)
        self.assertEqual(answer.by, "2.4.69")
        self.assertTrue(answer.elided)

    def test_and_inside_one_the_earlier_rule_takes_it(self):
        """तेषां पूर्वेण नित्यमेव लुग् भवति, अद्वन्द्वे त्वनेन विकल्पः."""
        answer = taddhita_luk(stem=UPAKADI[0], dvandva=True, plural=True)
        self.assertEqual(answer.by, "2.4.68")
        self.assertTrue(answer.elided)


class TheOneRuleThatReplacesAsWellAsElides(unittest.TestCase):

    def test_2_4_70_carries_the_new_stem(self):
        """यथासंख्यम् — each of the two to its own substitute."""
        for stem, becomes in (("āgastya", "agasti"),
                              ("kauṇḍinya", "kuṇḍinac")):
            with self.subTest(stem=stem):
                answer = taddhita_luk(stem=stem, plural=True)
                self.assertEqual(answer.by, "2.4.70")
                self.assertIsInstance(answer, Renamed)
                self.assertEqual(answer.stem, becomes)

    def test_no_other_rule_carries_one(self):
        """
        The substitute lives on `Renamed` and not on `Elided`, which is
        shared with 2.4.72 and should not grow a field one caller uses.
        """
        answer = taddhita_luk(affix="tadrāja", plural=True)
        self.assertIsInstance(answer, Elided)
        self.assertNotIsInstance(answer, Renamed)


class SupLukStandsApart(unittest.TestCase):

    def test_it_holds_for_a_root_and_for_a_stem(self):
        for becomes, example in (("dhātu", "पुत्रीयति"),
                                 ("prātipadika", "राजपुरुषः")):
            with self.subTest(becomes=becomes):
                answer = sup_luk(becomes=becomes)
                self.assertEqual(answer.by, "2.4.71")
                self.assertTrue(answer.elided)
                self.assertEqual(answer.elision, "luk")

    def test_an_ordinary_word_keeps_its_ending(self):
        """धातुप्रातिपदिकयोरिति किम्? वृक्षः, प्लक्षः."""
        answer = sup_luk()
        self.assertFalse(answer.elided)
        self.assertEqual(answer.by, "")

    def test_it_is_a_luk_and_not_a_lopa(self):
        """
        Which elision it is decides what 1.1.63 न लुमताङ्गस्य will and
        will not let through, so the kind is carried and not dropped.
        """
        self.assertEqual(sup_luk(becomes="prātipadika").elision, "luk")


class TheListsAreReadNotCounted(unittest.TestCase):
    """Properties, not a census — three such tests have gone stale."""

    def test_the_disk_ganas_have_members_and_hold_their_own_examples(self):
        for gana, example in ((PAILADI, "paila"),
                              (TAULVALYADI, "taulvali"),
                              (YASKADI, "yaska")):
            with self.subTest(example=example):
                self.assertTrue(gana)
                self.assertIn(example, gana)

    def test_the_two_lists_read_from_the_sutra_are_closed(self):
        """
        2.4.65's six and 2.4.58's four stand in the sūtras themselves,
        so they are fixed and a member outside them is not reached.
        """
        self.assertEqual(len(ATRYADI), 6)
        self.assertEqual(len(NYADI_STEMS), 4)

    def test_tikakitavadi_holds_finished_compounds(self):
        """
        The rule is about a द्वन्द्व, so what the gaṇa names is the
        द्वन्द्व and not its members — the same shape as 2.4.11.
        """
        self.assertTrue(TIKAKITAVADI)
        self.assertTrue(
            any(form.endswith("āḥ") for form in TIKAKITAVADI),
            "these should be finished plurals, तिककितवाः and the rest")


if __name__ == "__main__":
    unittest.main()
