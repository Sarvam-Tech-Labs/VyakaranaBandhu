# -*- coding: utf-8 -*-
"""
3.2.94 to 3.2.109 — and the pāda now needs FOUR kinds of entry point.

  a table row      a rule with conditions that adds an affix
  a fixed word     3.2.109 and the four before it, given whole
  a heading        3.2.84, which confers a condition and adds nothing
  a संज्ञा rule    3.2.102, which NAMES an affix rather than adding one
  a substitution   3.2.105–108, which replace लिट् rather than add

What this block asserts that no earlier one could:

  * a rule that names an affix and asks another rule which affixes
    bear the name — and whose two refusal shapes differ accordingly;
  * a rule that is the systematic undoing of the four before it;
  * a fifth and sixth use of repetition, neither of them any of the
    three the pāda had already shown.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.upapada_krt import (
    SADADI_LIT, Added, NotAdded, lit_substitute, nipatana, nistha,
    provisions_for, upapada_affix,
)


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.94", "kvanip", dict(root="dṛś", beside="meru",
                                  role="karman", past=True)),
        ("3.2.95", "kvanip", dict(root="yudh", beside="rājan",
                                  role="karman", past=True)),
        ("3.2.96", "kvanip", dict(root="yudh", beside="saha",
                                  past=True)),
        ("3.2.97", "ḍa", dict(root="jan", beside="upasara",
                              role="adhikaraṇa", past=True)),
        ("3.2.98", "ḍa", dict(root="jan", beside="buddhi",
                              role="apādāna", past=True)),
        ("3.2.99", "ḍa", dict(root="jan", beside="pra", upasarga="pra",
                              sense="saṃjñā", past=True)),
        ("3.2.100", "ḍa", dict(root="jan", beside="puṃs",
                               upasarga="anu", role="karman",
                               past=True)),
        ("3.2.101", "ḍa", dict(root="jan", beside="a", attested=True,
                               past=True)),
        ("3.2.103", "ṅvanip", dict(root="yaj", past=True)),
        ("3.2.104", "atṛn", dict(root="jṝ", past=True)),
    )

    def test_every_tabled_rule_answers_for_itself(self):
        for sutra, affix, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = upapada_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)


class ASamjnaRuleThatAsksAnotherWhichAffixesItMeans(unittest.TestCase):
    """
    3.2.102 निष्ठा says the affix bearing that NAME comes in the past.
    It adds nothing. Which affixes bear the name is 1.1.26 क्तक्तवतू
    निष्ठा's business, and that rule is codified, so it is asked.
    """

    def test_it_answers_for_an_affix_that_bears_the_name(self):
        answer = nistha("kta")
        self.assertIsInstance(answer, Added)
        self.assertEqual(answer.by, "3.2.102")

    def test_the_membership_comes_from_1_1_26(self):
        from src.astadhyayi.samjna import is_nistha

        for affix in ("kta", "ktavatu"):
            with self.subTest(affix=affix):
                self.assertTrue(is_nistha(affix))
                self.assertEqual(nistha(affix).by, "3.2.102")
        self.assertFalse(is_nistha("ṇvul"))

    def test_the_two_refusals_have_different_shapes(self):
        """
        An affix that bears no such name is refused WITHOUT naming
        this rule — 1.1.26 is what withheld the name, and a rule must
        not be reported for a refusal it did not make. But a निष्ठा
        outside the past IS refused by this rule, since refusing is
        then the whole of what it does.
        """
        not_a_nistha = nistha("ṇvul")
        self.assertIsInstance(not_a_nistha, NotAdded)
        self.assertEqual(not_a_nistha.by, "")

        wrong_tense = nistha("kta", past=False)
        self.assertIsInstance(wrong_tense, NotAdded)
        self.assertEqual(wrong_tense.by, "3.2.102")

    def test_the_reuse_is_declared(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertEqual(REGISTRY.get("3.2.102").reuses, ("1.1.26",))

    def test_the_circularity_the_vrtti_answers_is_recorded(self):
        """
        इतरेतराश्रयत्वाद् अप्रसिद्धिः — the name needs the affixes and
        the affixes need the name. भाविनी संज्ञा विज्ञायते.
        """
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.102").notes
        self.assertIn("इतरेतराश्रय", notes)
        self.assertIn("भाविनी", notes)


class ARuleThatUndoesTheFourBeforeIt(unittest.TestCase):
    """
    3.2.101 अन्येष्वपि दृश्यते, and the vṛtti takes each of 3.2.97 to
    3.2.100 in turn and shows its condition departed from. The third
    open rule of the pāda, after 3.2.75 and 3.2.76.
    """

    def test_it_is_held_to_attested_forms_like_the_other_two(self):
        self.assertTrue(provisions_for("3.2.101")[0].attested)
        self.assertEqual(
            upapada_affix(root="jan", beside="a", attested=True,
                          past=True).by, "3.2.101")
        # without the attestation it must not reach past the four
        self.assertNotEqual(
            upapada_affix(root="jan", beside="a", past=True).by,
            "3.2.101")

    def test_and_the_four_it_undoes_still_answer_for_themselves(self):
        for sutra, where in (
            ("3.2.97", dict(beside="upasara", role="adhikaraṇa")),
            ("3.2.98", dict(beside="buddhi", role="apādāna")),
            ("3.2.100", dict(beside="puṃs", upasarga="anu",
                             role="karman")),
        ):
            with self.subTest(sutra=sutra):
                self.assertEqual(
                    upapada_affix(root="jan", past=True, **where).by,
                    sutra)

    def test_the_vrttis_four_departures_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.101").notes
        # Each of these is quoted as the vṛtti joins it: the
        # negated conditions carry अपि and sandhi with it.
        for phrase in ("असप्तम्याम्", "जातावपि", "असंज्ञायामपि",
                       "अकर्मण्यपि"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, notes)


class WhatStandsInPlaceOfLit(unittest.TestCase):
    """
    3.2.105–108 do not add an affix to a root; they put लिट् where the
    past is meant and then substitute for it. So they answer from
    their own entry point.
    """

    def test_the_veda_gets_lit_and_its_two_substitutes(self):
        answer = lit_substitute(chandasi=True)
        self.assertEqual((answer.by, answer.gives), ("3.2.105", "liṭ"))
        self.assertIn("कानच्", answer.also)
        self.assertIn("क्वसु", answer.also)

    def test_three_roots_get_kvasu_in_ordinary_speech(self):
        for root in SADADI_LIT:
            with self.subTest(root=root):
                answer = lit_substitute(root)
                self.assertEqual((answer.by, answer.gives),
                                 ("3.2.108", "kvasu"))

    def test_and_the_option_not_taken_leaves_the_ordinary_forms(self):
        """तेन मुक्ते यथाप्राप्तं प्रत्यया भवन्ति — उपासदत्, उपससाद."""
        self.assertIn("लिट्", lit_substitute("sad").also)

    def test_it_reaches_nothing_else(self):
        answer = lit_substitute("kṛ")
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "")

    def test_3_2_105_records_why_it_is_said_at_all(self):
        """
        3.4.6 gives लिट् in the Veda already. धातुसंबन्धे स विधिः, अयं
        त्वविशेषेण — two rules giving the same thing, told apart by
        what each is ABOUT rather than by what each produces.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.4.6", REGISTRY.get("3.2.105").notes)


class TwoMoreUsesOfRepetition(unittest.TestCase):
    """
    The pāda had shown three — to defeat (3.2.44, 3.2.77), to end an
    अनुवृत्ति (3.2.78), to narrow (3.2.93). This block adds two.
    """

    def test_3_2_94_repeats_to_shut_out_the_other_affixes(self):
        """
        अन्येभ्योऽपि दृश्यन्ते इति क्वनिपि सिद्धे पुनर्वचनं
        प्रत्ययान्तरनिवृत्त्यर्थम् — 3.2.75 gives क्वनिप् already, and
        this is said to keep the rest of that rule's list away.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("प्रत्ययान्तरनिवृत्त्यर्थम्",
                      REGISTRY.get("3.2.94").notes)

    def test_3_2_106_repeats_to_widen_what_a_rule_reaches(self):
        """
        लिड्ग्रहणं किम्? लिण्मात्रस्य यथा स्यात् — naming लिट् again
        makes the substitution reach EVERY लिट्, including one given
        much later.
        """
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.106").notes
        self.assertIn("लिण्मात्रस्य", notes)


class TheThreeFixedWordsDoNotShareAnAffix(unittest.TestCase):
    """
    3.2.109 उपेयिवाननाश्वाननूचानश्च. Two fix क्वसु and the third fixes
    कानच्, which is why each entry in the lookup carries its own affix
    rather than the entry point assuming one.
    """

    def test_two_fix_one_affix_and_the_third_another(self):
        self.assertEqual(nipatana("upeyivān").gives, "kvasu")
        self.assertEqual(nipatana("anāśvān").gives, "kvasu")
        self.assertEqual(nipatana("anūcāna").gives, "kānac")
        for word in ("upeyivān", "anāśvān", "anūcāna"):
            with self.subTest(word=word):
                self.assertEqual(nipatana(word).by, "3.2.109")

    def test_the_preverb_is_recorded_as_inessential(self):
        """न चात्रोपसर्गस्तन्त्रम् — समीयिवान्, ईयिवान् stand too."""
        # न + च + अत्र + उपसर्गः joins to चात्रोपसर्गस्तन्त्रम्,
        # and the initial उ is gone: अत्र + उ gives ओ.
        self.assertIn("चात्रोपसर्गस्तन्त्रम्",
                      nipatana("upeyivān").why)


class ThePadaHasSeveralKindsOfRule(unittest.TestCase):
    """
    That the kinds PARTITION the pāda — disjoint and covering — is
    asserted in `test_astadhyayi_lakara.py`, the file for the block
    last read. It lived here while there were five kinds and went
    stale the moment a sixth arrived, which is the fifth time a census
    has done that. It now moves with the reading, and nothing here
    counts the kinds.
    """

    def test_the_pada_runs_unbroken_from_its_first_sutra(self):
        """Named endpoint deliberately absent — a range is a census."""
        from src.astadhyayi.sutra import REGISTRY

        numbers = sorted(
            int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
            if str(s.id).startswith("3.2."))
        self.assertTrue(numbers)
        self.assertEqual(numbers, list(range(1, len(numbers) + 1)))


if __name__ == "__main__":
    unittest.main()
