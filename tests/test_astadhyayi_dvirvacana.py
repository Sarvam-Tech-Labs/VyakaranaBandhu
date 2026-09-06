# -*- coding: utf-8 -*-
"""
द्विर्वचन — 6.1.1, 6.1.2, 6.1.9 and the abhyāsa rules of 7.4.

Reduplication is the first operation in this codebase that *builds a new
term* rather than substituting inside one, so the failures available here
are not the ones the rest of the suite guards against. Three kinds, each
with its own test below, and each one a real defect in this module before
it was one:

  * the copy is taken as the wrong stretch of the stem, which shows up
    only on a root whose first syllable is closed (मृज्, not लू);
  * something standing in FRONT of the copy is dropped, which cannot
    happen at all until 6.1.2 admits a vowel-initial root;
  * the abhyāsa rules are run in the wrong order, which produces a form
    that looks plausible and is not attested anywhere.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.dvirvacana import (
    double, first_ekac, is_ekac, is_haladi, reduplicated, shape_abhyasa,
)


class TheStemsTheCommentariesWork(unittest.TestCase):
    """Every one of these is a form the Kāśikā spells out."""

    def test_the_four_of_3_1_22(self):
        """पुनःपुनः पचति, पापच्यते। यायज्यते। जाज्वल्यते। देदीप्यते."""
        for root, stem in (("pac", "pāpacya"), ("yaj", "yāyajya"),
                           ("jval", "jājvalya"), ("dīp", "dedīpya")):
            with self.subTest(root=root):
                self.assertEqual(reduplicated(root).text, stem)

    def test_the_two_stems_1_1_4_turns_on(self):
        """
        लोलुवः and मरीमृजः are 1.1.4's own examples, and both of them are
        this stem with यङ् elided and अच् added. Getting the stem wrong
        would make that prohibition untestable against a real derivation.
        """
        self.assertEqual(reduplicated("lū").text, "lolūya")
        self.assertEqual(reduplicated("mṛj").text, "marīmṛjya")

    def test_the_r_penult_roots_of_7_4_90(self):
        """वरीवृत्यते। वरीवृध्यते। नरीनृत्यते."""
        for root, stem in (("vṛt", "varīvṛtya"), ("vṛdh", "varīvṛdhya"),
                           ("nṛt", "narīnṛtya")):
            with self.subTest(root=root):
                self.assertEqual(reduplicated(root).text, stem)

    def test_6_1_2_keeps_what_stands_before_the_copy(self):
        """
        अटाट्यते. The अ of अट् is not part of the copy and does not move:
        ट्य doubles behind it and the first ट्य becomes टा.

        This is the whole reason `Doubled` carries a head. Modelled as
        (abhyāsa, rest) — which is right for every consonant-initial root,
        and so looks right for a long time — the अ is dropped and the form
        comes out ā.
        """
        got = reduplicated("aṭ")
        self.assertEqual(got.text, "aṭāṭya")
        self.assertEqual(got.head, "a")
        self.assertEqual(got.by, "6.1.2")


class WhichStretchDoubles(unittest.TestCase):

    def test_a_closed_first_syllable_takes_its_closing_consonant(self):
        """
        मृज्य divides मृज् · य, so the copy is मृज् and 7.4.60 has a ज् to
        drop. Divide it मृ · ज्य instead and the copy is already मृ, 7.4.60
        does nothing, and the error is invisible on लू — which has no
        closing consonant to misplace.
        """
        self.assertEqual(first_ekac("mṛjya"), ("mṛj", "ya"))
        self.assertEqual(first_ekac("pacya"), ("pac", "ya"))
        self.assertEqual(first_ekac("lūya"), ("lū", "ya"))

    def test_6_1_1_reads_ekac_as_a_bahuvrihi_and_1_1_14_does_not(self):
        """
        The same word, read two ways, in two rules — and the readings
        disagree on प्र.

        6.1.1's Kāśikā is explicit: एकोऽच् यस्य सोऽयम् एकाच्, a bahuvrīhi,
        "that which HAS one vowel." 1.1.14's is the other: एकश्चासावच् च, a
        karmadhāraya, "it IS one vowel" — and the Kāśikā proves the
        difference there with प्राग्नये वाचमीरय, where प्र has one vowel,
        is not one vowel, and so is not pragṛhya.

        Sharing one implementation between them would be wrong in whichever
        rule lost the argument.
        """
        from src.astadhyayi.pragrhya import _is_single_vowel

        self.assertTrue(is_ekac("pra"))
        self.assertFalse(_is_single_vowel("pra"))

        self.assertTrue(is_ekac("pac"))
        self.assertFalse(is_ekac("jāgṛ"))     # 3.1.22's एकाच इति किम्

    def test_haladi_is_asked_of_the_sivasutras(self):
        """3.1.22's हलादेरिति किम्? भृशम् ईक्षते — ईक्ष् is vowel-initial."""
        self.assertTrue(is_haladi("pac"))
        self.assertTrue(is_haladi("mṛj"))
        self.assertFalse(is_haladi("īkṣ"))
        self.assertFalse(is_haladi("aṭ"))


class TheOrderTheAbhyasaRulesRunIn(unittest.TestCase):
    """
    7.4.66's Kāśikā states the order outright — उः अदत्वे कृते रुगादय
    आगमाः क्रियन्ते — and it is the one thing here that cannot be guessed
    from the finished forms, because two wrong orders produce forms that
    look Sanskrit enough to accept.
    """

    def test_urat_gives_a_plain_a_with_no_r_in_it(self):
        """
        ववृते, ववृधे, शशृधे — the copy's ऋ becomes अ and no र् appears.
        Applying 1.1.51 उरण् रपरः here instead would give वर्, and then
        वर्वृते, which is not the form.
        """
        self.assertEqual(shape_abhyasa("mṛ")[0], "ma")
        self.assertEqual(shape_abhyasa("vṛ")[0], "va")
        self.assertEqual(shape_abhyasa("śṛ")[0], "śa")

    def test_the_r_comes_from_the_augment_and_comes_after(self):
        """
        नर्नर्ति · नरिनर्ति · नरीनर्ति — one abhyāsa न, three augments.
        That triplet is what shows the र् is not from उरत्.
        """
        for augment, expected in (("ruk", "nar"), ("rik", "nari"),
                                  ("rīk", "narī")):
            with self.subTest(augment=augment):
                self.assertEqual(
                    shape_abhyasa("nṛ", rdupadha=True, yan_luk=True,
                                  augment=augment)[0],
                    expected)

    def test_ruk_and_rik_are_refused_outside_the_yan_luk(self):
        """
        7.4.91 says लुकि. 7.4.90's रीक् is for यङ् and यङ्लुक् both, and
        those two are not interchangeable — offering रुक् in the यङ् proper
        would give *मर्मृज्य where the rule allows only मरीमृज्य.
        """
        for augment in ("ruk", "rik"):
            with self.subTest(augment=augment):
                with self.assertRaises(ValueError):
                    shape_abhyasa("mṛ", rdupadha=True, augment=augment)
        self.assertEqual(
            shape_abhyasa("mṛ", rdupadha=True, augment="rīk")[0], "marī")

    def test_7_4_82_takes_the_ik_final_copy_and_7_4_83_the_rest(self):
        """
        गुणो यङ्लुकोः is for an इगन्त copy — लोलूयते, चेचीयते — and
        दीर्घोऽकितः for the others: पापच्यते, यायज्यते. Run दीर्घ on लु and
        the stem is *लूलूय; run गुण on प and it is *पेपच्य.
        """
        self.assertEqual(shape_abhyasa("lū")[0], "lo")     # 7.4.82
        self.assertEqual(shape_abhyasa("cī")[0], "ce")     # 7.4.82
        self.assertEqual(shape_abhyasa("pac")[0], "pā")    # 7.4.60 then 83
        self.assertEqual(shape_abhyasa("yaj")[0], "yā")

    def test_a_kit_augment_stops_the_lengthening(self):
        """अकितः इति किम्? यंयम्यते, रंरम्यते."""
        self.assertEqual(shape_abhyasa("yam", kit=True)[0], "ya")
        self.assertEqual(shape_abhyasa("yam")[0], "yā")

    def test_every_step_names_the_sutra_that_took_it(self):
        """
        The record is the point: a stem that comes out right by accident
        and a stem that comes out right by rule are the same string.
        """
        _, changes = shape_abhyasa("mṛj", rdupadha=True)
        self.assertEqual([c.by for c in changes],
                         ["7.4.60", "7.4.66", "7.4.90"])
        _, changes = shape_abhyasa("lū")
        self.assertEqual([c.by for c in changes], ["7.4.59", "7.4.82"])


class WhatItDoesNotDo(unittest.TestCase):
    """
    The scope, held as a test rather than left in prose — so that closing
    the gap makes something go red and the note gets updated with it.
    """

    def test_a_guttural_copy_is_still_not_palatalised_here(self):
        """
        7.4.62 कुहोश्चुः turns a क or ग in the copy into a palatal, and it
        HAS been codified since — in `abhyasa`, with the rest of the
        अभ्यासस्य heading. What has not changed is this builder: it
        applies the seven rules it holds itself and asks nothing of that
        module, so the stem is still wrong, knowingly, and the च that
        कुहोश्चुः would put there is still a क. The debt has moved from
        the rule to the wiring, and this test now says which.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertTrue(REGISTRY.has("7.4.62"))
        self.assertEqual(reduplicated("kṛt").text, "karīkṛtya")

    def test_the_doubling_itself_records_which_rule_split_the_stem(self):
        self.assertEqual(double("pacya").by, "6.1.9")
        self.assertEqual(double("aṭya").by, "6.1.2")


if __name__ == "__main__":
    unittest.main()
