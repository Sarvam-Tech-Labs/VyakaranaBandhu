# -*- coding: utf-8 -*-
"""
७.२.७९–११३ — before an ending: the optative, and the pronouns.

The run has two halves and a heading inside a heading, and the
tests follow that shape: the सार्वधातुक rules, the विभक्ति
heading, the मपर्यन्तस्य heading inside it, and then इदम्, which
six sūtras take apart piece by piece.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.vibhaktau import (
    BEFORE_RUN,
    BEFORE_TABLE,
    MAPARYANTA_FROM,
    THE_TWO,
    TRI_CATUR,
    TYADADI,
    VIBHAKTI_FROM,
    VIBHAKTI_TO,
    before_ending,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


def _n(code):
    return int(code.rsplit(".", 1)[1])


class TheSarvadhatukaFive(unittest.TestCase):
    """7.2.79–83, before the विभक्ति heading opens."""

    def test_the_optative_loses_a_s_that_is_not_last(self):
        # कुर्यात्, कुर्वीत — and कुर्युः keeps its स्.
        got = before_ending("liṅ", part="an-antya-s",
                            before="sārvadhātuka")
        self.assertEqual(got.sutra, "7.2.79")
        self.assertEqual(got.does, "sa-lopa")

    def test_the_s_meant_is_named_and_not_left_open(self):
        # कः पुनरनन्त्यो लिङः सकारः? यो यासुट्सुट्सीयुटाम् — the
        # three augments' स् and no other.
        self.assertIn("यासुट्सुट्सीयुटाम्",
                      provisions_for("7.2.79")[0].why)

    def test_ya_becomes_iy_after_an_a_final_stem(self):
        # पचेत्, पचेताम्, पचेयुः.
        got = before_ending("yā", gana="a-anta",
                            before="sārvadhātuka")
        self.assertEqual(got.sutra, "7.2.80")
        self.assertEqual(got.does, "iy")

    def test_and_so_does_a_nit_endings_a(self):
        # पचेते, पचेथे, यजेताम्.
        self.assertEqual(
            before_ending(gana="a-anta", part="ā-of-ṅit",
                          before="sārvadhātuka").sutra, "7.2.81")

    def test_the_nit_is_read_as_a_comparison(self):
        # ङित इव ङिद्वदिति — read the other way, 1.3.12 would
        # give an आत्मनेपद ending where none belongs.
        why = provisions_for("7.2.81")[0].why
        self.assertIn("ङित इव ङिद्वद्", why)
        self.assertTrue(REGISTRY.has("1.3.12"))

    def test_ana_takes_a_muk_and_after_as_becomes_i(self):
        # पचमानः, यजमानः; आसीनो यजते.
        self.assertEqual(
            before_ending(part="a", before="āna").sutra, "7.2.82")
        self.assertEqual(
            before_ending("ās", before="āna").sutra, "7.2.83")


class TheVibhaktiHeading(unittest.TestCase):
    """7.2.84 opens it and 7.2.113 closes it."""

    def test_the_heading_runs_where_the_vrtti_says(self):
        # मृजेर्वृद्धिः इत्यतः प्राग् विभक्त्यधिकारः — 7.2.114 is
        # the bound, so the heading ends at 7.2.113.
        self.assertEqual(VIBHAKTI_FROM, "7.2.84")
        self.assertEqual(VIBHAKTI_TO, "7.2.113")
        self.assertEqual(VIBHAKTI_TO, BEFORE_RUN[1])
        self.assertTrue(REGISTRY.has("7.2.114"))

    def test_astan_takes_a_before_an_ending(self):
        # अष्टाभिः, अष्टानाम्, अष्टासु.
        got = before_ending("aṣṭan", before="vibhakti")
        self.assertEqual(got.sutra, "7.2.84")
        self.assertTrue(got.optional)

    def test_and_the_option_is_read_out_of_two_other_sutras(self):
        # 6.1.172 says *after a LONG अष्टन्* and 7.1.21 names the
        # one that HAS its आ; neither wording would be needed if
        # the आ were compulsory. Both are codified.
        why = provisions_for("7.2.84")[0].why
        self.assertIn("ज्ञापितम्", why)
        for code in ("6.1.172", "7.1.21"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_rai_becomes_ra_before_a_consonant(self):
        # राभ्याम्, राभिः — and रायौ before a vowel.
        self.assertEqual(
            before_ending("rai", before="hal-vibhakti").sutra,
            "7.2.85")
        self.assertNotEqual(
            before_ending("rai", before="ac-vibhakti").sutra,
            "7.2.85")


class ThePronounsDeclinedBySubstitution(unittest.TestCase):
    """7.2.86–98, thirteen sūtras for two words."""

    def test_they_take_a_before_an_unreplaced_ending(self):
        # युष्माभिः, अस्माभिः.
        for stem in THE_TWO:
            got = before_ending(stem, before="vibhakti")
            self.assertEqual(got.sutra, "7.2.86", stem)
            self.assertEqual(got.does, "ā", stem)

    def test_and_y_before_a_vowel_initial_one(self):
        # त्वया, मया, युवयोः.
        for stem in THE_TWO:
            self.assertEqual(
                before_ending(stem, before="ac-vibhakti").sutra,
                "7.2.89", stem)

    def test_and_are_dropped_in_every_other_case(self):
        # त्वम्, तुभ्यम्, तव, युष्माकम्.
        got = before_ending("yuṣmad", before="śeṣa")
        self.assertEqual(got.sutra, "7.2.90")
        self.assertEqual(got.does, "lopa")

    def test_the_maparyanta_heading_bounds_every_substitute(self):
        # मपर्यन्तस्येत्ययमधिकारः — without it 7.2.92 would reach
        # युवकाम् and 7.2.97 would replace the whole word.
        self.assertEqual(MAPARYANTA_FROM, "7.2.91")
        row, = provisions_for("7.2.91")
        self.assertTrue(row.heading)
        self.assertIn("अधिकारः", row.why)

    def test_and_the_heading_itself_supplies_nothing(self):
        # A heading that named a substitute would answer queries
        # meant for the rules under it.
        self.assertEqual(provisions_for("7.2.91")[0].does, "")
        self.assertNotEqual(
            before_ending("yuṣmad", before="vibhakti").sutra,
            "7.2.91")

    def test_every_substitute_under_it_reaches_only_to_the_m(self):
        under = [row for row in BEFORE_TABLE
                 if _n("7.2.91") < _n(row.sutra) <= _n("7.2.98")]
        self.assertEqual(len(under), 7)
        for row in under:
            self.assertEqual(row.part, "ma-paryanta", row.sutra)

    def test_each_ending_gets_its_own_pair(self):
        # युवाम्, यूयम्, त्वम्, तुभ्यम्, तव, त्वाम्.
        wanted = {
            ("dvivacana", None): ("7.2.92", "yuva"),
            (None, "jas"): ("7.2.93", "yūya"),
            (None, "su"): ("7.2.94", "tva"),
            (None, "ṅayi"): ("7.2.95", "tubhya"),
            (None, "ṅasi-ṣaṣṭhī"): ("7.2.96", "tava"),
            ("ekavacana", None): ("7.2.97", "tva"),
        }
        for (number, ending), (code, shape) in wanted.items():
            got = before_ending("yuṣmad", part="ma-paryanta",
                                number=number or "",
                                before=ending or "")
            self.assertEqual(got.sutra, code, (number, ending))
            self.assertEqual(got.does, shape, (number, ending))

    def test_two_of_them_name_a_sense_and_not_an_ending(self):
        # द्विवचने इत्यर्थग्रहणम् and एकवचने इत्यर्थनिर्देशः —
        # which is what gets अतियुवाम् and अतित्वाम्, where the
        # compound's own number is a different one.
        for code in ("7.2.92", "7.2.97"):
            row, = provisions_for(code)
            self.assertTrue(row.number, code)
            self.assertEqual(row.before, (), code)

    def test_and_one_reaches_past_the_case_endings_altogether(self):
        # त्वदीयः, त्वत्पुत्रः — before an affix or a second
        # compound member, which the विभक्ति heading had shut out.
        got = before_ending("yuṣmad", part="ma-paryanta",
                            number="ekavacana", before="pratyaya")
        self.assertEqual(got.sutra, "7.2.98")


class TheNumeralsAndJara(unittest.TestCase):
    """7.2.99–101."""

    def test_two_numerals_change_in_the_feminine(self):
        # तिस्रः, चतस्रः.
        self.assertEqual(len(TRI_CATUR), 2)
        for stem, shape in TRI_CATUR:
            got = before_ending(stem, gender="strī",
                                before="vibhakti")
            self.assertEqual(got.sutra, "7.2.99", stem)
            self.assertEqual(got.does, shape, stem)

    def test_and_not_outside_it(self):
        # त्रयः, चत्वारः, त्रीणि.
        self.assertNotEqual(
            before_ending("tri", before="vibhakti").sutra, "7.2.99")

    def test_their_r_becomes_ra_before_a_vowel(self):
        # तिस्रस्तिष्ठन्ति, चतस्रः पश्य.
        got = before_ending("tisṛ", part="ṛ",
                            before="ac-vibhakti")
        self.assertEqual(got.sutra, "7.2.100")
        self.assertEqual(got.does, "r")

    def test_jara_becomes_jaras_optionally(self):
        # जरसा दन्ताः शीर्यन्ते, जरया दन्ताः शीर्यन्ते.
        got = before_ending("jarā", before="ac-vibhakti")
        self.assertEqual(got.sutra, "7.2.101")
        self.assertTrue(got.optional)

    def test_and_not_before_a_consonant(self):
        # जराभ्याम्, जराभिः.
        self.assertNotEqual(
            before_ending("jarā", before="hal-vibhakti").sutra,
            "7.2.101")


class TheDemonstratives(unittest.TestCase):
    """7.2.102–113, and the six sūtras that take इदम् apart."""

    def test_the_tyadadi_stems_take_a(self):
        # सः, यः, एषः, अयम्, असौ, द्वौ.
        self.assertEqual(len(TYADADI), 7)
        for stem in TYADADI:
            self.assertEqual(
                before_ending(stem, before="vibhakti").does, "a",
                stem)

    def test_the_list_is_closed_at_dvi(self):
        # द्विपर्यन्तानां त्यदादीनामत्वमिष्यते — भवान् is out.
        self.assertEqual(TYADADI[-1], "dvi")
        self.assertNotEqual(
            before_ending("bhavat", before="vibhakti").sutra,
            "7.2.102")

    def test_kim_takes_three_different_shapes(self):
        # कः before an ending, कुतः before त, क्व before अति.
        self.assertEqual(
            before_ending("kim", before="vibhakti").does, "ka")
        self.assertEqual(
            before_ending("kim", before="ta-ādi-vibhakti").does,
            "ku")
        self.assertEqual(
            before_ending("kim", before="ati").does, "kva")

    def test_and_the_last_two_displace_the_first(self):
        for code in ("7.2.104", "7.2.105"):
            self.assertIn("7.2.103",
                          provisions_for(code)[0].blocks)

    def test_adas_takes_au_and_loses_its_ending(self):
        # असौ — two operations in one sūtra.
        got = before_ending("adas", part="s", before="su")
        self.assertEqual(got.sutra, "7.2.107")
        self.assertEqual(got.does, "au")
        self.assertTrue(got.deletes_ending)

    def test_no_other_rule_of_the_run_deletes_an_ending(self):
        deleting = [row.sutra for row in BEFORE_TABLE
                    if row.deletes_ending]
        self.assertEqual(deleting, ["7.2.107"])

    def test_six_sutras_take_idam_apart_piece_by_piece(self):
        # Its last sound, its द् twice, its इद् three times.
        wanted = {
            ("antya", "su", ""): "7.2.108",
            ("d", "vibhakti", ""): "7.2.109",
            ("d", "su", ""): "7.2.110",
            ("id", "su", "puṃs"): "7.2.111",
            ("id", "āp-vibhakti", ""): "7.2.112",
            ("id", "hal-vibhakti", ""): "7.2.113",
        }
        for (part, ending, gender), code in wanted.items():
            got = before_ending("idam", part=part, before=ending,
                                gender=gender)
            self.assertEqual(got.sutra, code, (part, ending))

    def test_the_masculine_and_the_feminine_go_different_ways(self):
        # अयं ब्राह्मणः by 7.2.111, इयं ब्राह्मणी by 7.2.110.
        masculine = before_ending("idam", part="id", before="su",
                                  gender="puṃs")
        feminine = before_ending("idam", part="d", before="su")
        self.assertEqual(masculine.does, "ay")
        self.assertEqual(feminine.does, "y")
        self.assertIn("7.2.110", masculine.blocked_by)


class NothingHappensByDefault(unittest.TestCase):
    """वृक्ष and अग्नि go into every case unchanged."""

    def test_an_unnamed_stem_reaches_nothing(self):
        got = before_ending("vṛkṣa", before="vibhakti")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(BEFORE_RUN, ("7.2.79", "7.2.113"))
        codes = [row.sutra for row in BEFORE_TABLE]
        self.assertEqual(
            codes, ["7.2.%d" % n for n in range(79, 114)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in BEFORE_TABLE:
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

    def test_the_endings_this_run_stands_before_are_live(self):
        # 4.1.2 supplies every ending named here, and 7.1.27–33
        # is where युष्मद् and अस्मद् got the substitutes this
        # run then reshapes the stem for. All codified.
        self.assertTrue(REGISTRY.has("4.1.2"))
        for n in range(27, 34):
            self.assertTrue(REGISTRY.has("7.1.%d" % n), n)

    def test_and_the_sandhi_these_forms_need_has_landed(self):
        # असौ needs 8.2.80 अदसोऽसेर्दादु दो मः for its कच्-form
        # and एभिः needs 8.2.66's रुँ. Both are codified now, so
        # every sound of अदस् but its first can be accounted
        # for — this run reshapes the stem and that one rebuilds
        # what follows the द्.
        self.assertTrue(REGISTRY.has("8.2.66"))
        self.assertTrue(REGISTRY.has("8.2.80"))


if __name__ == "__main__":
    unittest.main()
