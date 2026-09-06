# -*- coding: utf-8 -*-
"""
3.2.21 to 3.2.28 — the rest of the उपपद affixes.

The per-rule coverage is the least of what is here. Four things this
block asserts that the run before it could not:

  * a प्रतिषेध does not govern what it excepts — 3.2.23 refuses ट, and
    the answer names 3.2.1, which supplies the अण्;
  * one word read two ways inside one pāda — 3.2.22's कर्मन् is the
    word itself, 3.2.1's is the kāraka;
  * two conditions that look like one field and are not, which is why
    दृतिहारः came out wrong until they were split;
  * a निपातन stays out of the table, with its own entry point.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.upapada_krt import (
    DIVADI, KIMYATTADBAHU, SABDADI, UPAPADA, VANADI,
    Added, NotAdded, nipatana, provisions_for, upapada_affix,
)


class EachRuleAnswersForItsOwnExample(unittest.TestCase):
    """
    The pāda's coverage — that it runs unbroken, and that every rule
    is in the table or is a निपातन — is asserted ONCE, in the file for
    the last block read. Two copies of it were here and went stale the
    moment 3.2 grew past 28; a third would go stale again. What stays
    here is what only this block can say.
    """

    CASES = (
        ("3.2.21", "ṭa", dict(root="kṛ", beside="divā", role="sup")),
        ("3.2.22", "ṭa", dict(root="kṛ", beside="karman",
                              role="karman", sense="bhṛti")),
        ("3.2.24", "in", dict(root="kṛ", beside="stamba",
                              role="karman", names_a="vrīhi-vatsa")),
        ("3.2.25", "in", dict(root="hṛ", beside="dṛti", role="karman",
                              names_a="paśu")),
        ("3.2.27", "in", dict(root="van", beside="brahman",
                              role="karman", chandasi=True)),
        ("3.2.28", "khaś", dict(root="ej", beside="jana",
                                role="karman", causative=True)),
    )

    def test_every_giving_rule_answers_for_itself(self):
        for sutra, affix, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = upapada_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_all_twenty_seven_of_3_2_21s_companions_are_reached(self):
        for word in DIVADI:
            with self.subTest(word=word):
                self.assertEqual(
                    upapada_affix(root="kṛ", beside=word,
                                  role="sup").by, "3.2.21")

    def test_all_four_of_3_2_27s_roots_are_reached_in_the_veda(self):
        for root in VANADI:
            with self.subTest(root=root):
                self.assertEqual(
                    upapada_affix(root=root, beside="brahman",
                                  role="karman", chandasi=True).by,
                    "3.2.27")


class APratisedhaDoesNotGovernWhatItExcepts(unittest.TestCase):
    """
    3.2.23 is the only प्रतिषेध of the pāda. It refuses 3.2.20's ट for
    nine words — and what those words take is 3.2.1's अण्, which is why
    every form the vṛtti gives here is -कारः and not -करः. So the
    answer must name the rule that SUPPLIES, and carry the refusal
    separately. The same decision 2.3.72 and 2.3.50 settled.
    """

    def test_all_nine_are_refused_the_ta_and_given_the_an(self):
        for word in SABDADI:
            with self.subTest(word=word):
                answer = upapada_affix(
                    root="kṛ", beside=word, role="karman",
                    sense="hetu-tācchīlya-ānulomya")
                self.assertEqual(answer.gives, "aṇ")
                self.assertEqual(
                    answer.by, "3.2.1",
                    "the rule that supplies the affix answers")
                self.assertEqual(answer.blocked_by, "3.2.23")

    def test_without_the_pratisedha_those_words_would_take_the_ta(self):
        """
        The refusal has to be doing work. A word not in the nine, in
        the same three senses, takes ट by 3.2.20 — so the difference
        between the two answers IS 3.2.23.
        """
        answer = upapada_affix(root="kṛ", beside="śoka", role="karman",
                               sense="hetu-tācchīlya-ānulomya")
        self.assertEqual((answer.by, answer.gives), ("3.2.20", "ṭa"))
        self.assertEqual(answer.blocked_by, "")

    def test_a_refusal_is_reported_only_where_it_left_nothing(self):
        """
        The standing rule cuts both ways: a rule must not be named for
        a refusal it did not make, but where refusing is the whole of
        what happened the प्रतिषेध does name itself. Here 3.2.1 always
        catches the word, so 3.2.23 never has to.
        """
        for word in SABDADI:
            with self.subTest(word=word):
                self.assertNotEqual(
                    upapada_affix(root="kṛ", beside=word,
                                  role="karman").by, "3.2.23")


class OneWordReadTwoWaysInsideOnePada(unittest.TestCase):
    """
    3.2.1's कर्मणि is the kāraka; 3.2.22's is स्वरूपग्रहण, the word
    कर्मन् itself standing beside. Nothing in the text marks the
    difference — it is read off what each rule could sensibly mean.
    """

    def test_3_2_22_wants_the_word_and_3_2_1_wants_the_role(self):
        by_word = upapada_affix(root="kṛ", beside="karman",
                                role="karman", sense="bhṛti")
        self.assertEqual(by_word.by, "3.2.22")
        # Any other object in the same sense is 3.2.1's, not 3.2.22's:
        # the WORD is the condition, not the role.
        other = upapada_affix(root="kṛ", beside="kumbha",
                              role="karman", sense="bhṛti")
        self.assertEqual(other.by, "3.2.1")

    def test_the_word_is_held_in_the_companion_list_not_the_role(self):
        """
        Codified so the two readings cannot be confused: कर्मन् appears
        as a companion, never as a role.
        """
        row = provisions_for("3.2.22")[0]
        self.assertEqual(row.beside, ("karman",))

    def test_bhrti_is_needed_or_it_is_not_this_rule(self):
        """भृताविति किम्? कर्मकारः."""
        self.assertEqual(
            upapada_affix(root="kṛ", beside="karman",
                          role="karman").by, "3.2.1")


class TwoQuestionsThatLookedLikeOneField(unittest.TestCase):
    """
    The seventh field-name collision. `sense` was carrying the sense of
    the ACT and what the finished WORD names. 3.2.25 needs both at once
    and that is how it was found.
    """

    def test_3_2_25_needs_the_thing_named(self):
        """पशाविति किम्? दृतिहारः."""
        self.assertEqual(
            upapada_affix(root="hṛ", beside="dṛti", role="karman",
                          names_a="paśu").by, "3.2.25")

    def test_and_carrying_a_waterskin_is_lifting_so_3_2_9_is_out(self):
        """
        दृतिहारः has the long vowel, so the affix is अण् and not
        3.2.9's अच् — because carrying IS उद्यमन, which 3.2.9 refuses.
        With one field the two conditions masked each other and this
        came out *दृतिहरः.
        """
        answer = upapada_affix(root="hṛ", beside="dṛti", role="karman",
                               sense="udyamana")
        self.assertEqual((answer.by, answer.gives), ("3.2.1", "aṇ"))

    def test_both_conditions_can_be_asserted_at_once(self):
        """Which is what a single field made impossible."""
        answer = upapada_affix(root="hṛ", beside="dṛti", role="karman",
                               sense="udyamana", names_a="paśu")
        self.assertEqual(answer.by, "3.2.25")

    def test_the_vartika_condition_of_3_2_24_is_live(self):
        """व्रीहिवत्सयोरिति किम्? स्तम्बकारः — a vārttika that changes
        the output has to be in the table or the counter is untestable."""
        self.assertEqual(
            upapada_affix(root="kṛ", beside="stamba", role="karman",
                          names_a="vrīhi-vatsa").gives, "in")
        self.assertEqual(
            upapada_affix(root="kṛ", beside="stamba",
                          role="karman").gives, "aṇ")


class TheVedicRuleIsOneWay(unittest.TestCase):
    """
    छन्दसि विषये. A Vedic rule must not answer outside the Veda — but
    the rules that say nothing about it still answer inside it, since
    the Veda has the ordinary grammar too and only adds to it.
    """

    def test_3_2_27_does_not_reach_ordinary_usage(self):
        self.assertNotEqual(
            upapada_affix(root="van", beside="brahman",
                          role="karman").by, "3.2.27")

    def test_but_an_ordinary_rule_still_answers_inside_the_veda(self):
        self.assertEqual(
            upapada_affix(root="kṛ", beside="kumbha", role="karman",
                          chandasi=True).by, "3.2.1")


class TheCausativeIsOneWay(unittest.TestCase):
    """
    3.2.28 REQUIRES ण्यन्त, so the bare root gets no खश्. It does not
    follow that silence elsewhere means refusal, and this class once
    asserted that it did — that a rule saying nothing about the
    causative was written for the bare root. Nothing in the text says
    so, and 3.2.39 says the opposite outright: तप दाहे चुरादिः and तप
    संतापे भ्वादिः, द्वयोरपि ग्रहणम्, both roots spelt alike are
    meant. The claim was mine and not Pāṇini's; the condition is
    one-way, like छन्दसि.
    """

    def test_the_bare_root_does_not_get_khas(self):
        """The half that was right: requiring it does exclude."""
        self.assertNotEqual(
            upapada_affix(root="ej", beside="jana", role="karman").by,
            "3.2.28")

    def test_but_silence_about_it_refuses_nothing(self):
        """
        3.2.1 says nothing of the causative and must still answer for
        a causative stem. The rule that caught this is 3.2.39, eleven
        sūtras later — which is the argument for reading a whole run
        before trusting a condition abstracted from one rule of it.
        """
        answer = upapada_affix(root="kṛ", beside="kumbha",
                               role="karman", causative=True)
        self.assertIsInstance(answer, Added)
        self.assertEqual(answer.by, "3.2.1")


class TheNipatanaStaysOutOfTheTable(unittest.TestCase):
    """
    यदिह लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम्. 3.2.26 fixes
    two words outright — one an unexpected shape on the companion, one
    an augment — and a table deriving them would be pretending.
    """

    def test_the_two_the_sutra_states_are_given_as_they_stand(self):
        for word in ("phalegrahi", "ātmambhari"):
            with self.subTest(word=word):
                answer = nipatana(word)
                self.assertEqual(answer.by, "3.2.26")
                self.assertEqual(answer.gives, "in")

    def test_the_ca_gathers_in_two_the_sutra_does_not_name(self):
        """अनुक्तसमुच्चयार्थश्चकारः — कुक्षिम्भरिः, उदरम्भरिः."""
        for word in ("kukṣimbhari", "udarambhari"):
            with self.subTest(word=word):
                self.assertEqual(nipatana(word).by, "3.2.26")
        self.assertIn("अनुक्तसमुच्चयार्थ",
                      nipatana("kukṣimbhari").why)

    def test_it_reaches_nothing_else_and_says_so_without_blame(self):
        answer = nipatana("kumbhakāra")
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "")

    def test_the_table_does_not_try_to_derive_them(self):
        self.assertNotIn("3.2.26", {row.sutra for row in UPAPADA})


class WhatWasDeliberatelyNotCodified(unittest.TestCase):

    def test_3_2_21s_varttika_is_recorded_without_a_row(self):
        """
        किंयत्तद्बहुषु कृञोऽज्विधानम् — but the vṛtti offers a second
        route in the same breath, अथवाजादिषु पाठः करिष्यते, and
        chooses neither. Codifying one would be settling what the
        commentary left open, so all four still answer by 3.2.21.
        """
        from src.astadhyayi.sutra import REGISTRY

        for word in KIMYATTADBAHU:
            with self.subTest(word=word):
                self.assertIn(word, DIVADI)
                self.assertEqual(
                    upapada_affix(root="kṛ", beside=word,
                                  role="sup").gives, "ṭa")
        notes = REGISTRY.get("3.2.21").notes
        self.assertIn("अथवाजादिषु", notes)
        self.assertIn("SCOPE", notes)

    def test_this_block_declares_no_reuse_and_the_notes_say_why(self):
        """
        3.2.28 cites 3.4.113 and 3.2.21 cites the adhyāya-8 rules its
        भास्करः escapes — but both consequences happen downstream of
        choosing the affix, which is all this module does. Declaring
        them would repeat 3.2.3's mistake.
        """
        from src.astadhyayi.sutra import REGISTRY

        for n in range(21, 29):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(REGISTRY.get("3.2.%d" % n).reuses, ())
        self.assertIn("3.4.113", REGISTRY.get("3.2.28").notes)


if __name__ == "__main__":
    unittest.main()
