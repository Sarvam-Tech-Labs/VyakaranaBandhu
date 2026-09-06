# -*- coding: utf-8 -*-
"""
७.३.३२–४३ — हन् before a ञित्, and what the causal puts in.

The heading changes twice inside twelve sūtras, so the tests
follow that: the end of the उत्तरपद run, the two rules about
चिण् and a कृत्, and then the causal's augments — every one of
which the vṛtti says goes BEFORE the ending, for a reason three
pādas on.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.nau_agama import (
    ARTI_SIX,
    NAU_FROM,
    NAU_RUN,
    NAU_TABLE,
    PURVANTA,
    SA_CHA_SEVEN,
    UTTARAPADA_ENDS_AT,
    before_ni,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class WhereTheHeadingEnds(unittest.TestCase):
    """7.3.32 closes the उत्तरपद run and starts this one."""

    def test_it_is_the_bound_the_earlier_vrtti_named(self):
        from src.astadhyayi.uttarapada_vrddhi import UTTARAPADA_TO

        # 7.3.10's vṛtti said हनस्तोऽचिण्णलोः इति प्रागेतस्मात्,
        # and this module names the same sūtra as its start.
        self.assertEqual(UTTARAPADA_ENDS_AT, "7.3.32")
        self.assertEqual(NAU_RUN[0], UTTARAPADA_ENDS_AT)
        self.assertEqual(int(UTTARAPADA_TO.rsplit(".", 1)[1]) + 1,
                         int(NAU_RUN[0].rsplit(".", 1)[1]))

    def test_two_words_of_the_heading_fall_away(self):
        # तद्धितेष्विति निवृत्तम्। तत्संबद्धं कितीत्यपि — the
        # taddhita goes and the कित् with it.
        self.assertIn("निवृत्तम्", provisions_for("7.3.32")[0].why)

    def test_han_becomes_t_before_a_nit(self):
        # घातयति, घातकः, घातो वर्तते.
        got = before_ni("han", before="ñit")
        self.assertEqual(got.sutra, "7.3.32")
        self.assertEqual(got.does, "t")

    def test_but_not_before_cin_or_nal(self):
        # अघानि, जघान.
        for affix in ("ciṇ", "ṇal"):
            self.assertNotEqual(
                before_ni("han", before=affix).sutra, "7.3.32",
                affix)


class BeforeCinAndAKrt(unittest.TestCase):
    """7.3.33–35, one rule and two refusals."""

    def test_an_a_final_stem_takes_a_yuk(self):
        # अदायि, अधायि; दायः, धायकः.
        got = before_ni(gana="ā-anta", before="ciṇ")
        self.assertEqual(got.sutra, "7.3.33")
        self.assertEqual(got.does, "yuk")
        self.assertTrue(got.augment)

    def test_a_udatta_m_final_root_refuses_the_vrddhi(self):
        # अशमि, शमकः, दमः — and the rule refused is 7.2.116's,
        # which is codified.
        got = before_ni(gana="udātta-upadeśa-m-anta",
                        before="ciṇ")
        self.assertEqual(got.sutra, "7.3.34")
        self.assertEqual(got.does, "")
        self.assertIn("7.2.116", got.blocked_by)
        self.assertTrue(REGISTRY.has("7.2.116"))

    def test_the_vrtti_has_to_say_what_is_refused(self):
        # किं चोक्तम्? अत उपधायाः इति वृद्धिः — the sūtra says
        # only *what is said*, and the vṛtti supplies the rule.
        self.assertIn("किं चोक्तम्",
                      provisions_for("7.3.34")[0].why)

    def test_and_two_roots_refuse_it_by_name(self):
        # अजनि, जनकः; अवधि, वधकः.
        for root in ("jan", "vadh"):
            got = before_ni(root, before="ciṇ")
            self.assertEqual(got.sutra, "7.3.35", root)
            self.assertEqual(got.does, "", root)


class TheCausalsAugments(unittest.TestCase):
    """7.3.36–43, where णौ alone governs."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(NAU_FROM, "7.3.36")
        self.assertIn("सर्वं निवृत्तम्",
                      provisions_for("7.3.36")[0].why)

    def test_six_roots_and_every_a_final_stem_take_a_puk(self):
        # अर्पयति, ह्रेपयति, क्नोपयति, दापयति.
        self.assertEqual(len(ARTI_SIX), 6)
        for root in ARTI_SIX:
            got = before_ni(root, before="ṇi")
            self.assertEqual(got.sutra, "7.3.36", root)
            self.assertEqual(got.does, "puk", root)
        self.assertEqual(
            before_ni(gana="ā-anta", before="ṇi").sutra, "7.3.36")

    def test_seven_more_take_a_yuk(self):
        # निशाययति, ह्वाययति, पाययति.
        self.assertEqual(len(SA_CHA_SEVEN), 7)
        for root in SA_CHA_SEVEN:
            self.assertEqual(before_ni(root, before="ṇi").sutra,
                             "7.3.37", root)

    def test_every_augment_of_the_run_goes_before_the_ending(self):
        # एतेऽपि पूर्वान्ता एव क्रियन्ते — and the reason is a
        # rule three pādas on: only so does the reduplicated
        # aorist shorten the right vowel, अदीदपत्, अपीपलत्.
        self.assertIn("पूर्वान्ता", PURVANTA)
        self.assertIn("पूर्वान्तकरणम्",
                      provisions_for("7.3.36")[0].why)

    def test_and_they_are_marked_as_augments_and_not_substitutes(self):
        augments = sorted({row.sutra for row in NAU_TABLE
                           if row.augment})
        self.assertEqual(
            augments,
            ["7.3.33", "7.3.36", "7.3.37", "7.3.38", "7.3.39",
             "7.3.40"])


class WhereASenseLicensesIt(unittest.TestCase):
    """7.3.38–40 and 7.3.42, four rules turning on a meaning."""

    def test_va_takes_a_juk_only_of_shaking(self):
        # पक्षेणोपवाजयति — and आवापयति केशान् otherwise.
        self.assertEqual(
            before_ni("vā", before="ṇi",
                      sense="vidhūnana").sutra, "7.3.38")
        self.assertNotEqual(
            before_ni("vā", before="ṇi").sutra, "7.3.38")

    def test_li_and_la_only_of_melting_and_optionally(self):
        # घृतं विलीनयति; जतु विलापयति otherwise.
        for root in ("lī", "lā"):
            got = before_ni(root, before="ṇi",
                            sense="sneha-vipātana")
            self.assertEqual(got.sutra, "7.3.39", root)
            self.assertTrue(got.optional, root)

    def test_bhi_only_where_the_frightener_is_the_cause(self):
        # मुण्डो भीषयते; कुञ्चिकयैनं भाययति otherwise, the key
        # being no agent — नात्र हेतुः प्रयोजको भयकारणम्.
        got = before_ni("bhī", before="ṇi", sense="hetu-bhaya")
        self.assertEqual(got.sutra, "7.3.40")
        self.assertEqual(got.does, "ṣuk")
        # The कुञ्चिका counter-example is carried in keeps_out
        # and the reason in the why: an ई read into the root, so
        # that भापयते does not take the augment too.
        self.assertIn("प्रयोजको",
                      provisions_for("7.3.40")[0].keeps_out)
        self.assertIn("षुग्निवृत्त्यर्थः",
                      provisions_for("7.3.40")[0].why)

    def test_sad_becomes_t_only_where_no_motion_is_meant(self):
        # पुष्पाणि शातयति; गाः शादयति गोपालकः otherwise.
        self.assertEqual(
            before_ni("śad", before="ṇi", sense="a-gati").sutra,
            "7.3.42")
        self.assertNotEqual(
            before_ni("śad", before="ṇi").sutra, "7.3.42")


class TheLastTwo(unittest.TestCase):
    """7.3.41 and 7.3.43, one plain and one optional."""

    def test_sphay_becomes_sphav(self):
        got = before_ni("sphāy", before="ṇi")
        self.assertEqual(got.sutra, "7.3.41")
        self.assertEqual(got.does, "v")
        self.assertFalse(got.optional)

    def test_and_ruh_becomes_rop_optionally(self):
        # व्रीहीन् रोपयति, व्रीहीन् रोहयति.
        got = before_ni("ruh", before="ṇi")
        self.assertEqual(got.sutra, "7.3.43")
        self.assertEqual(got.does, "p")
        self.assertTrue(got.optional)


class NothingHappensByDefault(unittest.TestCase):
    """Most roots take the causal with no augment at all."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = before_ni("pac", before="ṇi")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(NAU_RUN, ("7.3.32", "7.3.43"))
        codes = [row.sutra for row in NAU_TABLE]
        self.assertEqual(
            codes, ["7.3.%d" % n for n in range(32, 44)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in NAU_TABLE:
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

    def test_the_causal_this_run_is_stated_before_is_live(self):
        # 3.1.26 हेतुमति च supplies the णि, and 7.2.116 is the
        # vṛddhi two of these rules refuse. Both codified.
        self.assertTrue(REGISTRY.has("3.1.26"))
        self.assertTrue(REGISTRY.has("7.2.116"))

    def test_but_the_aorist_the_augments_are_placed_for_is_not(self):
        # पुकः पूर्वान्तकरणम् अदीदपदित्यत्रोपधाह्रस्वो यथा स्यात्
        # — the placement is for 7.4.1's सन्वल्लघुनि, and no पाद
        # of 7.4 is read. When 7.4.1 lands this fails.
        # 7.4.1 णौ चङ्युपधाया ह्रस्वः has landed, so the
        # placement this sūtra argues for can be checked against
        # the rule it is argued for: अदीदपत् wants the पुक् put
        # at the stem's end so the penult shortens.
        self.assertTrue(REGISTRY.has("7.4.1"))


if __name__ == "__main__":
    unittest.main()
