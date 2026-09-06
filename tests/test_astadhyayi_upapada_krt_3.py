# -*- coding: utf-8 -*-
"""
3.2.29 to 3.2.47 — the rest of खश्, and the खच् run.

What this block asserts that neither run before it could:

  * यथासंख्यम् cuts BOTH ways inside one run — refused at 3.2.29,
    bound at 3.2.36 and 3.2.41 — so no default can be right and the
    licensed pairings must be stated per rule;
  * 3.2.29 needs a set that is neither paired nor the full product,
    which is what forced the pairing out of two special cases keyed on
    sūtra id and into a field;
  * 3.2.43 reaches अभयंकरः by ASKING 1.1.72, and the test makes the
    answer depend on that rule rather than on a suffix test here;
  * one rule gives two affixes at once, and both must be reported.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.upapada_krt import (
    ASURYA_LALATA, BHRADI, MEGHADI, NADI_MUSTI, NASIKA_STANA,
    PUR_SARVA, SARVAKULADI, UPAPADA, Added, NotAdded, nipatana,
    provisions_for, upapada_affix,
)


class EachRuleAnswersForItsOwnExample(unittest.TestCase):
    """
    The pāda's coverage is asserted ONCE, in the file for the last
    block read. Two copies stood here and went stale when 3.2 grew
    past 47 — the same failure this project had recorded one block
    earlier and then repeated, which is the argument for the rule
    being mechanical rather than remembered.
    """

    CASES = (
        ("3.2.29", "khaś", dict(root="dheṭ", beside="stana",
                                role="karman")),
        ("3.2.30", "khaś", dict(root="dhmā", beside="nāḍī",
                                role="karman")),
        ("3.2.31", "khaś", dict(root="vah", beside="kūla",
                                role="karman", upasarga="ud")),
        ("3.2.32", "khaś", dict(root="lih", beside="abhra",
                                role="karman")),
        ("3.2.33", "khaś", dict(root="pac", beside="prastha",
                                role="karman")),
        ("3.2.34", "khaś", dict(root="pac", beside="nakha",
                                role="karman")),
        ("3.2.35", "khaś", dict(root="tud", beside="arus",
                                role="karman")),
        ("3.2.36", "khaś", dict(root="dṛś", beside="asūrya",
                                role="karman")),
        ("3.2.38", "khac", dict(root="vad", beside="priya",
                                role="karman")),
        ("3.2.39", "khac", dict(root="tap", beside="para",
                                role="karman")),
        ("3.2.40", "khac", dict(root="yam", beside="vāc",
                                role="karman", sense="vrata")),
        ("3.2.41", "khac", dict(root="dṝ", beside="pur",
                                role="karman")),
        ("3.2.42", "khac", dict(root="kaṣ", beside="kūla",
                                role="karman")),
        ("3.2.43", "khac", dict(root="kṛ", beside="bhaya",
                                role="karman")),
        ("3.2.44", "aṇ", dict(root="kṛ", beside="kṣema",
                              role="karman")),
        ("3.2.45", "khac", dict(root="bhū", beside="āśita", role="sup",
                                sense="karaṇa-bhāva")),
        ("3.2.46", "khac", dict(root="vṛ", beside="pati", role="sup",
                                sense="saṃjñā")),
        ("3.2.47", "khac", dict(root="gam", beside="suta", role="sup",
                                sense="saṃjñā")),
    )

    def test_every_giving_rule_answers_for_itself(self):
        for sutra, affix, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = upapada_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_the_list_rules_reach_every_member_they_name(self):
        for group, sutra, extra in (
            (NADI_MUSTI, "3.2.30", dict(root="dhmā", role="karman")),
            (SARVAKULADI, "3.2.42", dict(root="kaṣ", role="karman")),
            (MEGHADI, "3.2.43", dict(root="kṛ", role="karman")),
        ):
            for word in group:
                with self.subTest(sutra=sutra, word=word):
                    self.assertEqual(
                        upapada_affix(beside=word, **extra).by, sutra)
        for root in BHRADI:
            with self.subTest(sutra="3.2.46", root=root):
                self.assertEqual(
                    upapada_affix(root=root, beside="pati", role="sup",
                                  sense="saṃjñā").by, "3.2.46")


class YathasankhyamCutsBothWaysInsideOneRun(unittest.TestCase):
    """
    3.2.5 and 3.2.13 required the one-to-one pairing. 3.2.29 REFUSES
    it — यथासंख्यमत्र नेष्यते — and 3.2.36, seven rules later, requires
    it again. So no default can be right, and the licensed set has to
    be stated rule by rule.
    """

    def test_3_2_29_licenses_a_set_that_is_neither_paired_nor_full(self):
        """
        स्तने धेटः, नासिकायां तु ध्मश्च धेटश्च. Three combinations of
        the four — which is exactly what neither of the two readings
        the pāda uses elsewhere would give.
        """
        self.assertEqual(len(NASIKA_STANA), 3)
        for beside, root in NASIKA_STANA:
            with self.subTest(pair=(beside, root)):
                self.assertEqual(
                    upapada_affix(root=root, beside=beside,
                                  role="karman").by, "3.2.29")
        # The fourth combination is the one the vṛtti withholds.
        self.assertNotEqual(
            upapada_affix(root="dhmā", beside="stana",
                          role="karman").by, "3.2.29")

    def test_3_2_36_binds_crosswise_seven_rules_later(self):
        for beside, root in ASURYA_LALATA:
            with self.subTest(pair=(beside, root)):
                self.assertEqual(
                    upapada_affix(root=root, beside=beside,
                                  role="karman").by, "3.2.36")
        for beside, root in (("asūrya", "tap"), ("lalāṭa", "dṛś")):
            with self.subTest(crossed=(beside, root)):
                self.assertNotEqual(
                    upapada_affix(root=root, beside=beside,
                                  role="karman").by, "3.2.36")

    def test_3_2_41_binds_crosswise_too(self):
        for beside, root in PUR_SARVA:
            with self.subTest(pair=(beside, root)):
                self.assertEqual(
                    upapada_affix(root=root, beside=beside,
                                  role="karman").by, "3.2.41")
        self.assertNotEqual(
            upapada_affix(root="sah", beside="pur", role="karman").by,
            "3.2.41")

    def test_3_2_30_by_contrast_licenses_the_full_product(self):
        """नाडीमुष्ट्योश्च — both roots with every one of the words."""
        for root in ("dhmā", "dheṭ"):
            for word in NADI_MUSTI:
                with self.subTest(root=root, word=word):
                    self.assertEqual(
                        upapada_affix(root=root, beside=word,
                                      role="karman").by, "3.2.30")

    def test_the_pairing_is_a_field_and_not_a_special_case(self):
        """
        It was two branches keyed on sūtra id while only 3.2.5 and
        3.2.13 needed it. Five rules and one non-uniform set later,
        that would not have held — so the rows carry their own pairs
        and the matcher knows nothing about which sūtra it is looking
        at.
        """
        import inspect

        from src.astadhyayi import upapada_krt

        source = inspect.getsource(upapada_krt._reaches)
        self.assertIn("row.pairs", source)
        for sutra in ("3.2.5", "3.2.13", "3.2.29", "3.2.36", "3.2.41"):
            with self.subTest(sutra=sutra):
                self.assertNotIn('"%s"' % sutra, source)
                self.assertTrue(provisions_for(sutra)[0].pairs)


class TadantavidhiIsAskedOfTheRuleThatOwnsIt(unittest.TestCase):
    """
    उपपदविधौ भयादिग्रहणं तदन्तविधिं प्रयोजयति. Naming भय in a rule of
    this kind reaches what ENDS in भय, and 1.1.72 येन विधिस्तदन्तस्य is
    what says so. It is codified, so it is asked — not approximated
    with `beside.endswith(...)`, which would be a second statement of
    a rule that already exists.
    """

    def test_abhaya_is_reached_and_1_1_72_is_why(self):
        from src.astadhyayi.grahana import tadantavidhi

        self.assertTrue(tadantavidhi("bhaya", "abhaya"))
        self.assertEqual(
            upapada_affix(root="kṛ", beside="abhaya",
                          role="karman").by, "3.2.43")

    def test_a_word_1_1_72_does_not_reach_is_not_reached_here(self):
        from src.astadhyayi.grahana import tadantavidhi

        self.assertFalse(tadantavidhi("bhaya", "kumbha"))
        self.assertNotEqual(
            upapada_affix(root="kṛ", beside="kumbha",
                          role="karman").by, "3.2.43")

    def test_the_extension_is_held_to_the_rule_the_vrtti_flags(self):
        """
        3.2.42's सर्व and कूल carry no such note, so a word merely
        ending in one of them must not be swept in. The vṛtti attaches
        तदन्तविधि to this rule and the codification follows it rather
        than generalising.
        """
        self.assertTrue(provisions_for("3.2.43")[0].tadanta)
        for sutra in ("3.2.42", "3.2.30", "3.2.35"):
            with self.subTest(sutra=sutra):
                self.assertFalse(provisions_for(sutra)[0].tadanta)
        self.assertNotEqual(
            upapada_affix(root="kaṣ", beside="mahākūla",
                          role="karman").by, "3.2.42")

    def test_the_reuse_is_declared_and_it_is_the_only_one_here(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertEqual(REGISTRY.get("3.2.43").reuses, ("1.1.72",))
        for n in list(range(29, 43)) + list(range(44, 48)):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(REGISTRY.get("3.2.%d" % n).reuses, ())


class OneRuleGivesTwoAffixes(unittest.TestCase):
    """
    3.2.44 क्षेमप्रियमद्रेऽण् च — चकारात् खच्च, so क्षेमकारः and
    क्षेमंकरः both stand. Asking the rule has to show the pair, as
    3.1.147's did.
    """

    def test_both_affixes_are_reported(self):
        answer = upapada_affix(root="kṛ", beside="kṣema", role="karman")
        self.assertEqual(answer.gives, "aṇ")
        self.assertEqual(answer.also, "खच्")

    def test_the_an_is_named_to_keep_3_2_20s_ta_out(self):
        """
        वेति वक्तव्ये पुनरण्ग्रहणं हेत्वादिषु टप्रतिषेधार्थम् — वा
        would have been shorter, and अण् is written instead so the ट
        cannot come in the three senses. Without the naming, प्रिय in
        those senses would take 3.2.20's ट.
        """
        answer = upapada_affix(root="kṛ", beside="priya", role="karman",
                               sense="hetu-tācchīlya-ānulomya")
        self.assertEqual((answer.by, answer.gives), ("3.2.44", "aṇ"))
        # and a word 3.2.44 does not name still takes the ṭa there
        self.assertEqual(
            upapada_affix(root="kṛ", beside="śoka", role="karman",
                          sense="hetu-tācchīlya-ānulomya").gives, "ṭa")


class TheConditionsOfThisRunAreLive(unittest.TestCase):

    def test_3_2_31_wants_its_preverb_rather_than_refusing_one(self):
        """
        उदि — unlike 3.2.3 and 3.2.8, which refuse a preverb, this
        names one as a condition.
        """
        self.assertEqual(
            upapada_affix(root="vah", beside="kūla", role="karman",
                          upasarga="ud").by, "3.2.31")
        self.assertNotEqual(
            upapada_affix(root="vah", beside="kūla",
                          role="karman").by, "3.2.31")

    def test_3_2_40_needs_its_vow(self):
        """व्रत इति किम्? वाग्यामः."""
        self.assertEqual(
            upapada_affix(root="yam", beside="vāc", role="karman",
                          sense="vrata").by, "3.2.40")
        self.assertNotEqual(
            upapada_affix(root="yam", beside="vāc",
                          role="karman").by, "3.2.40")

    def test_3_2_46_needs_its_name(self):
        """संज्ञायामिति किम्? कुटुम्बभारः."""
        self.assertNotEqual(
            upapada_affix(root="bhṛ", beside="kuṭumba", role="sup").by,
            "3.2.46")

    def test_3_2_39_takes_both_roots_where_3_2_28_took_only_one(self):
        """
        द्वयोरपि ग्रहणम् — तप of the curādi class and तप of the
        bhvādi are both meant here, so unlike 3.2.28 the rule does not
        turn on the causative. Two rules of one pāda taking opposite
        views of one ambiguity.
        """
        self.assertEqual(
            upapada_affix(root="tap", beside="para", role="karman").by,
            "3.2.39")
        self.assertEqual(
            upapada_affix(root="tap", beside="para", role="karman",
                          causative=True).by, "3.2.39")
        self.assertFalse(provisions_for("3.2.39")[0].causative)
        self.assertTrue(provisions_for("3.2.28")[0].causative)


class TheSecondNipatanaJoinsTheFirst(unittest.TestCase):

    def test_all_three_of_3_2_37_are_given_as_they_stand(self):
        for word in ("ugrampaśya", "irammada", "pāṇindhama"):
            with self.subTest(word=word):
                self.assertEqual(nipatana(word).by, "3.2.37")

    def test_panindhama_shows_why_they_had_to_be_fixed(self):
        """
        पाणयो ध्मायन्त एष्विति — the companion is the PLACE and not the
        object, so no rule of the खश् run, all of which want an object,
        could have reached it.
        """
        self.assertIn("पाणयो", nipatana("pāṇindhama").why)
        self.assertNotEqual(
            upapada_affix(root="dhmā", beside="pāṇi",
                          role="adhikaraṇa").by, "3.2.37")

    def test_it_still_refuses_what_it_does_not_hold(self):
        answer = nipatana("priyaṃvada")
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "")


if __name__ == "__main__":
    unittest.main()
