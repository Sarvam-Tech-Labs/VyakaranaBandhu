# -*- coding: utf-8 -*-
"""
७.३.४४–५१ — the क of a feminine, and the ठ of a taddhita.

Four of the eight record a named teacher's view rather than
settling one, so the tests ask what naming a teacher does: it
makes a refusal into an option, and it puts one form out of the
language's ordinary reach until a reader asks for it.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.pratyaya_ka import (
    ACARYANAM,
    BHASTRADI,
    ISUS_UK_TA,
    KA_RUN,
    KA_TABLE,
    UDICAM,
    provisions_for,
    the_ka,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheAThatBecomesI(unittest.TestCase):
    """7.3.44, four conditions deep."""

    def test_the_a_before_an_affixs_ka_becomes_i(self):
        # जटिलिका, मुण्डिका, कारिका, हारिका.
        got = the_ka("a-before-pratyaya-ka", before="āp")
        self.assertEqual(got.sutra, "7.3.44")
        self.assertEqual(got.does, "it")

    def test_the_vrtti_tests_all_four_of_its_conditions(self):
        # शका — the क is no affix; पटुका — the अ follows it;
        # गोका — no अ; राका — the आ is long.
        keeps = provisions_for("7.3.44")[0].keeps_out
        for form in ("शका", "पटुका", "गोका", "राका"):
            self.assertIn(form, keeps, form)

    def test_and_argues_that_one_of_them_is_derivable(self):
        # ककारमात्रं प्रत्ययो नास्तीति सामर्थ्यात् — no affix is
        # a bare क, so प्रत्ययस्थ could have been read out of the
        # rule's working. It is written **विस्पष्टार्थम्**.
        self.assertIn("विस्पष्टार्थम्",
                      provisions_for("7.3.44")[0].why)


class WhatNamingATeacherDoes(unittest.TestCase):
    """7.3.46–49 record views rather than settling them."""

    def test_three_refusals_are_the_northerners_and_optional(self):
        # इभ्यका, इभ्यिका; भस्त्रका, भस्त्रिका; खट्वका, खट्विका.
        northern = [row.sutra for row in KA_TABLE
                    if row.view == UDICAM]
        self.assertEqual(northern, ["7.3.46", "7.3.47", "7.3.48"])
        for row in KA_TABLE:
            if row.view == UDICAM:
                self.assertTrue(row.optional, row.sutra)

    def test_naming_them_is_what_makes_it_an_option(self):
        # उदीचांग्रहणं विकल्पार्थम् — both forms stand.
        self.assertIn("विकल्पार्थम्",
                      provisions_for("7.3.46")[0].why)

    def test_six_stems_are_refused_with_or_without_a_nan(self):
        # भस्त्रका, अभस्त्रका; अजका, अनजका; स्वका, अस्वका.
        self.assertEqual(len(BHASTRADI), 6)
        for stem in BHASTRADI:
            got = the_ka(stem, before="āp")
            self.assertEqual(got.sutra, "7.3.47", stem)

    def test_two_of_the_six_can_take_no_nan_and_the_vrtti_says_so(self):
        # एषाद्वे नञ्पूर्वे न प्रयोजयतः.
        self.assertIn("न प्रयोजयतः",
                      provisions_for("7.3.47")[0].why)

    def test_the_teachers_a_answers_only_when_asked_for(self):
        # खट्वाका is a fifth form, and a reader who does not ask
        # for it gets the northerners' refusal instead.
        asked = the_ka(gana="a-bhāṣitapuṃska", before="āp",
                       view=ACARYANAM)
        unasked = the_ka(gana="a-bhāṣitapuṃska", before="āp")
        self.assertEqual(asked.sutra, "7.3.49")
        self.assertEqual(asked.does, "āt")
        self.assertEqual(unasked.sutra, "7.3.48")
        self.assertEqual(unasked.does, "")

    def test_and_the_answer_carries_whose_view_it_is(self):
        self.assertEqual(
            the_ka(gana="a-bhāṣitapuṃska", before="āp",
                   view=ACARYANAM).view, ACARYANAM)


class YaAndSa(unittest.TestCase):
    """7.3.45, named as a specimen and not a list."""

    def test_two_stems_refuse_the_substitution(self):
        # यका, सका.
        for stem in ("yā", "sā"):
            got = the_ka(stem, before="āp")
            self.assertEqual(got.sutra, "7.3.45", stem)
            self.assertEqual(got.does, "", stem)
            self.assertIn("7.3.44", got.blocked_by)

    def test_and_the_naming_is_read_as_a_specimen(self):
        # या सा इति निर्देशोऽतन्त्रम्, यत्तदोरुपलक्षणार्थम् —
        # so यकांयकाम् and तकांतकाम् are refused too, and three
        # vārttikas add उपत्यका, पावकाः and जीवका.
        why = provisions_for("7.3.45")[0].why
        # निर्देशः + अतन्त्रम् joins into निर्देशोऽतन्त्रम्, so
        # the substring has to start after the junction.
        self.assertIn("तन्त्रम्", why)
        self.assertIn("उपत्यका", why)


class TheTaddhitasTha(unittest.TestCase):
    """7.3.50 against 7.3.51."""

    def test_it_becomes_ika(self):
        # आक्षिकः, शालाकिकः, लावणिकः.
        got = the_ka("ṭha", before="taddhita")
        self.assertEqual(got.sutra, "7.3.50")
        self.assertEqual(got.does, "ika")

    def test_but_k_after_four_stem_endings(self):
        # सार्पिष्कः, धानुष्कः, मातृकम्, औदश्वित्कः.
        self.assertEqual(len(ISUS_UK_TA), 4)
        got = the_ka("ṭha", gana="is-us-uk-ta-anta")
        self.assertEqual(got.sutra, "7.3.51")
        self.assertEqual(got.does, "ka")
        self.assertIn("7.3.50", got.blocked_by)

    def test_the_two_are_told_apart_by_the_stem_and_not_the_affix(self):
        # Both name the ठ, so the columns must be read as a
        # conjunction. Read as alternatives, 7.3.51 swallows
        # 7.3.50 and आक्षिकः comes out wrong.
        for code in ("7.3.50", "7.3.51"):
            self.assertEqual(provisions_for(code)[0].of, ("ṭha",),
                             code)
        self.assertEqual(provisions_for("7.3.50")[0].gana, "")
        self.assertEqual(provisions_for("7.3.51")[0].gana,
                         "is-us-uk-ta-anta")

    def test_the_affix_it_reshapes_is_codified(self):
        # 4.4.1's ठक् gives आक्षिकः and 4.4.52's ठञ् लावणिकः.
        for code in ("4.4.1", "4.4.52"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_vrtti_reads_the_rule_two_ways_without_choosing(self):
        # संघातग्रहणे तु प्रत्ययेऽत्रापि संघातग्रहणमेव — whether
        # the whole affix is replaced or only its sound depends
        # on how affixes are read at large.
        self.assertIn("संघातग्रहणम् एव",
                      provisions_for("7.3.50")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A stem with no क and no ठ is untouched by all eight."""

    def test_an_unnamed_thing_reaches_nothing(self):
        got = the_ka("aṇ", before="taddhita")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(KA_RUN, ("7.3.44", "7.3.51"))
        codes = [row.sutra for row in KA_TABLE]
        self.assertEqual(
            codes, ["7.3.%d" % n for n in range(44, 52)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in KA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_feminine_affix_this_run_stands_before_is_live(self):
        # 4.1.4 अजाद्यतष्टाप् supplies the आप् every rule of
        # 7.3.44–49 is stated before, and 5.3.70's कन् the क.
        self.assertTrue(REGISTRY.has("4.1.4"))
        self.assertTrue(REGISTRY.has("5.3.70"))

    def test_but_what_the_ka_then_meets_is_not(self):
        # सार्पिष्कः needs 8.3.59's ष् for its स्, and no पाद of
        # अध्याय ८ is read. When it lands this fails and the note
        # must be rewritten to state the live dependency.
        # 8.3.59 आदेशप्रत्यययोः, which the क् then meets, has
        # landed with पाद ८.३.
        self.assertTrue(REGISTRY.has("8.3.59"))


if __name__ == "__main__":
    unittest.main()
