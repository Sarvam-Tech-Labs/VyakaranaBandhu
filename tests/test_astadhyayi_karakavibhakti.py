# -*- coding: utf-8 -*-
"""
अनभिहिते — 2.3.1 to 2.3.26, which ending a kāraka takes.

The interesting failures here are not "does 2.3.2 give a second". They
are the ones a section of competing rules makes available: a narrow rule
losing to a broad one it was written to displace, a refusal reported as
though the rule had fired, and a closed list quietly accepting a name
that is not on it.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.karakavibhakti import (
    EXPRESSED_BY, Ending, Expressed, vibhakti_for,
)


class TheGateOverTheWholeSection(unittest.TestCase):

    def test_nothing_gets_an_ending_where_something_said_it_already(self):
        """
        अनभिहिते. क्रियते कटः needs no accusative: the verb has said
        कर्म. So do कृतः कटः, शत्यः and प्राप्तोदको ग्रामः, one for each
        of the four.
        """
        for said_by in EXPRESSED_BY:
            with self.subTest(expressed_by=said_by):
                got = vibhakti_for("karman", expressed_by=said_by)
                self.assertIsInstance(got, Expressed)
                self.assertEqual(got.by, "2.3.1")

        self.assertIsInstance(vibhakti_for("karman"), Ending)

    def test_the_list_of_four_is_closed_and_a_fifth_is_refused(self):
        """
        तिङ्कृत्तद्धितसमासैः परिसंख्यानम् — a परिसंख्या, so the list is
        those four and nothing else. A fifth name accepted silently
        would let any caller switch the whole section off.
        """
        self.assertEqual(len(EXPRESSED_BY), 4)
        with self.assertRaises(ValueError):
            vibhakti_for("karman", expressed_by="upasarga")


class WhereRulesCompeteForOneWord(unittest.TestCase):
    """
    Several of these rules exist only to take something away from an
    earlier one, and each says so: द्वितीयापवादो योगः at 2.3.9 and
    2.3.14, तृतीयापवादो योगः at 2.3.24, षष्ठ्यपवादः at 2.3.4.
    """

    def test_2_3_9_and_2_3_10_take_precedence_over_2_3_8(self):
        """
        All three want a word construed with a karmapravacanīya. The
        plain case gives a second; more-than gives a seventh; अप, आङ्
        and परि give a fifth.
        """
        self.assertEqual(vibhakti_for(karmapravacaniya="anu").number, 2)
        self.assertEqual(
            vibhakti_for(karmapravacaniya="upa", adhika=True).number, 7)
        self.assertEqual(vibhakti_for(karmapravacaniya="āṅ").number, 5)
        self.assertEqual(
            vibhakti_for(karmapravacaniya="prati",
                         pratinidhi_pratidana=True).number, 5)

    def test_the_hetu_run_narrows_four_times(self):
        """
        2.3.23 gives a third; 2.3.24 takes a debt out into the fifth;
        2.3.25 makes a quality optional; 2.3.26 sends it to the sixth
        where the word हेतु is used. Each must beat the one before it.
        """
        self.assertEqual(vibhakti_for(hetu=True).by, "2.3.23")
        self.assertEqual(vibhakti_for(hetu=True, rna=True).by, "2.3.24")
        self.assertEqual(vibhakti_for(hetu=True, guna=True).by, "2.3.25")
        self.assertEqual(vibhakti_for(hetu_prayoga=True).by, "2.3.26")

    def test_the_same_hundred_changes_case_with_its_role(self):
        """
        अकर्तरीति किम्? शताद् बद्धः against शतेन बन्धितः. The Kāśikā's
        reason is that in the second the hundred is what SET the binding
        going — प्रयोजकत्वाच्च कर्तृसंज्ञकम् — so it is a कर्तृ and
        2.3.18 gives it a third instead.
        """
        self.assertEqual(
            vibhakti_for(hetu=True, rna=True, akartari=True).number, 5)
        self.assertEqual(vibhakti_for("kartṛ").number, 3)


class TheConditionsThatAreAsked(unittest.TestCase):
    """
    Each of these is a किम् the Kāśikā puts, and each names something no
    form carries — so it is stated, and the rule withholds without it.
    """

    def test_apradhana_iti_kim(self):
        """शिष्येण सहोपाध्यायस्य गौः — the principal one takes no third."""
        got = vibhakti_for(saha_yukta=True, apradhana=False)
        self.assertIsInstance(got, Expressed)
        self.assertIn("अप्रधान", got.why)

    def test_asevayam_iti_kim(self):
        """
        आयुक्तो गौः शकटे — an ox harnessed to a cart is simply in a
        place, and the seventh there is 2.3.36's अधिकरण, not this rule's.

        This lives here and not among the worked inputs because the
        refusal reports `by="2.3.40"`, and a chip whose `by` names its
        own sūtra reads as the rule having fired. That is the fourth
        time that shape has turned up; a refusal belongs where it can be
        asserted as a refusal.
        """
        got = vibhakti_for(holding="āyukta", asevaa=False)
        self.assertIsInstance(got, Expressed)
        self.assertIn("आसेवा", got.why)

    def test_the_far_and_near_words_take_four_cases(self):
        """दूरान्तिकार्थेभ्यश् चतस्रो विभक्तयो भवन्ति, across three rules."""
        got = vibhakti_for(dura_antika=True)
        self.assertEqual(got.by, "2.3.34")
        self.assertEqual(set((got.number,) + got.also), {2, 3, 5, 6, 7})

    def test_astriyam_iti_kim(self):
        """बुद्ध्या मुक्तः — feminine, and only the third stands."""
        self.assertEqual(
            vibhakti_for(hetu=True, guna=True, astri=False).by, "2.3.23")

    def test_anadhvani_iti_kim(self):
        """अध्वानं गच्छति — a road, so no fourth beside the second."""
        road = vibhakti_for("karman", gati_artha=True, adhvan=True)
        self.assertEqual(road.by, "2.3.2")
        self.assertEqual(road.also, ())

    def test_cestayam_iti_kim(self):
        """मनसा पाटलिपुत्रं गच्छति — the mind travels, the man does not."""
        in_mind = vibhakti_for("karman", gati_artha=True, cesta=False)
        self.assertEqual(in_mind.by, "2.3.2")

    def test_atyantasamyoga_iti_kim(self):
        """मासस्य द्विरधीते — part of the month, and not this rule."""
        self.assertIsInstance(
            vibhakti_for(kala_adhvan=True), Expressed)


class WhereTwoEndingsAreOffered(unittest.TestCase):
    """
    Five rules give a choice, and each must report BOTH — an option
    recorded as a single answer is a rule half codified.
    """

    def test_all_five(self):
        both = [
            (vibhakti_for("karman", chandas_hu=True), 3, 2),      # 2.3.3
            (vibhakti_for(kala_adhvan=True,
                          karaka_madhye=True), 7, 5),             # 2.3.7
            (vibhakti_for("karman", gati_artha=True), 2, 4),      # 2.3.12
            (vibhakti_for("karman", manya_karman=True,
                          anadara=True), 4, 2),                   # 2.3.17
            (vibhakti_for(samjna_karman=True), 3, 2),             # 2.3.22
        ]
        for got, first, second in both:
            with self.subTest(by=got.by):
                self.assertTrue(got.optional)
                self.assertEqual(got.number, first)
                self.assertEqual(got.also, (second,))

    def test_2_3_25_offers_a_fifth_beside_the_third(self):
        got = vibhakti_for(hetu=True, guna=True)
        self.assertEqual((got.number, got.also), (5, (3,)))


class TheSenseReadingsAdmitWordsNotNamed(unittest.TestCase):

    def test_alam_brings_prabhu_and_sakta_with_it(self):
        """
        अलमिति पर्याप्त्यर्थग्रहणम् — the word is taken by its SENSE of
        sufficiency, so प्रभुर्मल्लो मल्लाय and शक्तो मल्लो मल्लाय take
        the fourth though the sūtra names neither.
        """
        for word in ("alam", "prabhu", "śakta"):
            with self.subTest(word=word):
                self.assertEqual(vibhakti_for(namas_yoga=word).number, 4)

    def test_and_a_word_outside_the_reading_is_refused(self):
        with self.assertRaises(ValueError):
            vibhakti_for(namas_yoga="hanta")


if __name__ == "__main__":
    unittest.main()
