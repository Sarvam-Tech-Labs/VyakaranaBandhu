# -*- coding: utf-8 -*-
"""
2.4.73 and 2.4.75 to 2.4.85 — the rules that close adhyāya 2.

Expectations are the Kāśikā's worked forms and its *kim*
counter-examples. Two claims here are about a choice Pāṇini made rather
than about an output — श्लु named where लुक् was already running, and
one विभाषा doing two different jobs — and both are held by tests that
would pass on no other reading.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.pratyaya_luk import (
    LE_LUK_ROOTS, LUT_PRATHAMA, Replaced, SICA_LUK_ROOTS,
    SICA_VIBHASA_ROOTS, avyaya_ending, lut_prathama, verbal_luk,
)


class SapAndSlu(unittest.TestCase):

    def test_the_third_gana_takes_slu_and_not_luk(self):
        """
        लुकि प्रकृते श्लुविधानं द्विर्वचनार्थम्. लुक् was already running
        from 2.4.72 and 2.4.75 names a different elision instead —
        because only a श्लु triggers 6.1.10 श्लौ and makes the root
        double. जुहोति and बिभर्ति exist because of that choice, so the
        KIND of elision is the whole content of the rule and asserting
        only that something was elided would miss it.
        """
        answer = verbal_luk(affix="śap", gana="juhotyādi")
        self.assertEqual(answer.by, "2.4.75")
        self.assertTrue(answer.elided)
        self.assertEqual(answer.elision, "ślu")
        self.assertNotEqual(
            answer.elision, "luk",
            "a लुक् here would leave जुहोति undoubled")

    def test_sap_stands_where_no_rule_of_this_run_reaches_it(self):
        answer = verbal_luk(affix="śap")
        self.assertFalse(answer.elided)
        self.assertEqual(answer.by, "")

    def test_2_4_73_gives_the_veda_its_latitude_for_sap(self):
        answer = verbal_luk(affix="śap", chandas=True)
        self.assertEqual(answer.by, "2.4.73")
        self.assertEqual(answer.elision, "luk")

    def test_2_4_76_overrides_2_4_75_in_the_veda(self):
        """
        यत्रोक्तं तत्र न भवति — the vṛtti's first examples for 2.4.76 are
        juhotyādi roots WITHOUT the श्लु: दाति प्रियाणि, धाति देवम्. So
        in the Veda the later rule takes the same input and reverses it.
        """
        outside = verbal_luk(affix="śap", gana="juhotyādi")
        self.assertEqual(outside.by, "2.4.75")
        self.assertTrue(outside.elided)

        inside = verbal_luk(affix="śap", gana="juhotyādi", chandas=True)
        self.assertEqual(inside.by, "2.4.76")
        self.assertFalse(
            inside.elided,
            "2.4.76's own first examples are the ones where it fails")


class SicIsDropped(unittest.TestCase):

    def test_all_five_roots_of_2_4_77_are_reached(self):
        for root in SICA_LUK_ROOTS:
            with self.subTest(root=root):
                answer = verbal_luk(affix="sic", root=root)
                self.assertEqual(answer.by, "2.4.77")
                self.assertTrue(answer.elided)

    def test_all_five_roots_of_2_4_78_are_reached_and_are_a_choice(self):
        for root in SICA_VIBHASA_ROOTS:
            with self.subTest(root=root):
                self.assertEqual(
                    verbal_luk(affix="sic", root=root).by, "2.4.78")

    def test_one_vibhasa_doing_two_different_jobs(self):
        """
        धेटः पूर्वेण नित्ये प्राप्ते विभाषार्थं वचनम्,
        परिशिष्टानामप्राप्ते. धेट् is a घु, so 2.4.77 had already reached
        it and 2.4.78 LOOSENS an obligation; the other four had nothing
        reaching them, so for those the same word GRANTS the elision.
        The test is that धेट् is answered by 2.4.78 and not 2.4.77 —
        the later rule has to win, or the loosening never happens.
        """
        self.assertIn("ghu", SICA_LUK_ROOTS)
        self.assertIn("dheṭ", SICA_VIBHASA_ROOTS)
        self.assertEqual(verbal_luk(affix="sic", root="dheṭ").by, "2.4.78")
        # And a root only 2.4.78 names is likewise answered by it.
        self.assertEqual(verbal_luk(affix="sic", root="chā").by, "2.4.78")

    def test_both_rules_hold_in_the_active_only(self):
        """परस्मैपदेष्विति किम्? अगासाताम्, अघ्रासाताम्."""
        for root in ("bhū", "ghrā"):
            with self.subTest(root=root):
                answer = verbal_luk(affix="sic", root=root,
                                    parasmaipada=False)
                self.assertFalse(answer.elided)
                self.assertEqual(answer.by, "")

    def test_2_4_79_takes_the_middle_ta_only(self):
        """
        थासा साहचर्यादात्मनेपदस्य तशब्दस्य ग्रहणम् — there are two
        endings spelt त and the one meant is the middle, known by the
        company थास् keeps it in. अतनिष्ट यूयम् is the active and stays.
        """
        for ending in ("ta", "thās"):
            with self.subTest(before=ending):
                self.assertEqual(
                    verbal_luk(affix="sic", gana="tanādi",
                               before=ending).by, "2.4.79")

    def test_a_root_no_rule_names_keeps_its_sic(self):
        """अगासीन् नटः, अपासीन् नृपः — गायति and पाति are not the गा and
        पा the vārttika lets in."""
        answer = verbal_luk(affix="sic", root="gai")
        self.assertFalse(answer.elided)
        self.assertEqual(answer.by, "")


class LeIsDropped(unittest.TestCase):

    def test_all_ten_roots_of_2_4_80_are_reached_in_a_mantra(self):
        for root in LE_LUK_ROOTS:
            with self.subTest(root=root):
                answer = verbal_luk(affix="le", root=root, mantra=True)
                self.assertEqual(answer.by, "2.4.80")
                self.assertTrue(answer.elided)

    def test_but_not_outside_one(self):
        """मन्त्रे is a condition, not a note about where it happens."""
        for root in LE_LUK_ROOTS:
            with self.subTest(root=root):
                self.assertFalse(
                    verbal_luk(affix="le", root=root).elided)

    def test_2_4_81_does_not_inherit_the_mantra_condition(self):
        """
        ईहांचक्रे is an ordinary periphrastic perfect. If मन्त्रे carried
        down from 2.4.80, this rule would reach almost nothing.
        """
        answer = verbal_luk(affix="le", root="ām")
        self.assertEqual(answer.by, "2.4.81")
        self.assertTrue(answer.elided)


class TheEndingAfterAnIndeclinable(unittest.TestCase):

    def test_2_4_82_takes_it_away(self):
        answer = avyaya_ending()
        self.assertEqual(answer.by, "2.4.82")
        self.assertTrue(answer.elided)
        self.assertEqual(answer.elision, "luk")

    def test_2_4_83_refuses_that_and_puts_am_there_instead(self):
        answer = avyaya_ending(avyayibhava=True, ends_in_a=True,
                               vibhakti=2)
        self.assertIsInstance(answer, Replaced)
        self.assertEqual(answer.by, "2.4.83")
        self.assertEqual(answer.gives, "am")

    def test_an_avyayibhava_not_ending_in_a_falls_back_to_2_4_82(self):
        """अत इति किम्? अधिस्त्रि, अधिकुमारि."""
        answer = avyaya_ending(avyayibhava=True, vibhakti=2)
        self.assertEqual(answer.by, "2.4.82")
        self.assertTrue(answer.elided)

    def test_the_fifth_case_is_excepted_and_keeps_its_ending(self):
        """
        अपञ्चम्या इति किम्? उपकुम्भादानय. And the consequence the vṛtti
        draws: एतस्मिन् प्रतिषिद्धे पञ्चम्याः श्रवणमेव भवति — with the
        अम् kept off, the fifth ending is actually heard, so it must be
        neither replaced NOR elided.
        """
        answer = avyaya_ending(avyayibhava=True, ends_in_a=True,
                               vibhakti=5)
        self.assertFalse(getattr(answer, "elided", False))
        self.assertEqual(getattr(answer, "gives", ""), "")
        self.assertEqual(answer.by, "")

    def test_2_4_84_loosens_2_4_83_for_two_cases(self):
        """
        पूर्वेण नित्यमम्भावे प्राप्ते वचनमिदम् — the third time in this
        pāda a rule reopens what the one before it shut, after 2.4.44
        over 2.4.43 and 2.4.78 over 2.4.77.
        """
        for case in (3, 7):
            with self.subTest(vibhakti=case):
                answer = avyaya_ending(avyayibhava=True, ends_in_a=True,
                                       vibhakti=case)
                self.assertEqual(answer.by, "2.4.84")
                self.assertEqual(answer.gives, "am")
                self.assertTrue(answer.bahulam)

    def test_and_the_other_cases_stay_with_2_4_83(self):
        for case in (1, 2, 4, 6):
            with self.subTest(vibhakti=case):
                self.assertEqual(
                    avyaya_ending(avyayibhava=True, ends_in_a=True,
                                  vibhakti=case).by, "2.4.83")


class TheLastRuleOfTheAdhyaya(unittest.TestCase):

    def test_one_ending_per_number(self):
        """यथाक्रमम् — कर्ता, कर्तारौ, कर्तारः."""
        for number, ending in LUT_PRATHAMA:
            with self.subTest(number=number):
                answer = lut_prathama(number=number)
                self.assertEqual(answer.by, "2.4.85")
                self.assertEqual(answer.gives, ending)

    def test_the_three_endings_are_distinct(self):
        """
        A table that gave the same ending twice would still pass a test
        that only checked each lookup succeeded.
        """
        given = [ending for _n, ending in LUT_PRATHAMA]
        self.assertEqual(len(set(given)), 3)

    def test_a_number_that_is_not_one_is_refused(self):
        with self.assertRaises(ValueError):
            lut_prathama(number=4)


class TheWholeAdhyayaIsCodified(unittest.TestCase):
    """
    2.1.1 to 2.4.85, all four pādas. Checked as a property over the
    registry rather than as a count, so it stays true as work continues
    and fails the moment a gap opens.
    """

    def test_every_sutra_of_adhyaya_2_is_registered(self):
        from src.astadhyayi.corpus import load_vidyut_sutrapatha
        from src.astadhyayi.sutra import REGISTRY

        mula = load_vidyut_sutrapatha()
        expected = sorted(k for k in mula if k.startswith("2."))
        missing = [k for k in expected if not REGISTRY.has(k)]
        self.assertEqual(missing, [],
                         f"{len(missing)} sūtra(s) of adhyāya 2 uncodified")

    def test_each_pada_is_contiguous_from_one(self):
        from src.astadhyayi.sutra import REGISTRY

        for pada in ("2.1", "2.2", "2.3", "2.4"):
            numbers = sorted(
                int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
                if str(s.id).startswith(pada + "."))
            with self.subTest(pada=pada):
                self.assertTrue(numbers)
                self.assertEqual(numbers,
                                 list(range(1, len(numbers) + 1)))


if __name__ == "__main__":
    unittest.main()
