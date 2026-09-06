# -*- coding: utf-8 -*-
"""
७.३.७०–८३ — before a शित्, and the guṇa that closes the run.

Most of the present tense's strangeness is here, so the tests
walk the forms: पिबति from पा, तिष्ठति from स्था, पश्यति from
दृश्, गच्छति from गम्, जानाति from ज्ञा, पुनाति from पू.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.siti import (
    CODIFIED_APART,
    DUHADI,
    ISU_GAM_YAM,
    PIBADI,
    SAMADI_EIGHT,
    SITI_RUN,
    SITI_TABLE,
    before_sit,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheLossesFirst(unittest.TestCase):
    """7.3.70–73."""

    def test_a_ghu_root_loses_its_vowel_before_let_optionally(self):
        # दधद् रत्नानि दाशुषे; सोमो ददद् गन्धर्वाय.
        got = before_sit(gana="ghu", before="leṭ")
        self.assertEqual(got.sutra, "7.3.70")
        self.assertTrue(got.optional)

    def test_an_o_final_stem_loses_it_before_syan(self):
        # निश्यति, अवच्छ्यति, अवद्यति, अवस्यति.
        got = before_sit(gana="o-anta", before="śyan")
        self.assertEqual(got.sutra, "7.3.71")
        self.assertEqual(got.does, "lopa")

    def test_the_ksa_affix_loses_its_vowel_before_a_vowel(self):
        # अधुक्षाताम्, अधुक्षि — and अधुक्षत् before a consonant.
        self.assertEqual(before_sit("ksa", before="ac").sutra,
                         "7.3.72")
        self.assertNotEqual(
            before_sit("ksa", before="hal").sutra, "7.3.72")

    def test_four_roots_drop_the_whole_ksa_optionally(self):
        # अदुग्ध beside अधुक्षत; अलीढ beside अलिक्षत.
        self.assertEqual(DUHADI, ("duh", "dih", "lih", "guh"))
        for root in DUHADI:
            got = before_sit(root, before="dantya",
                             pada="ātmanepada")
            self.assertEqual(got.sutra, "7.3.73", root)
            self.assertEqual(got.does, "luk", root)
            self.assertTrue(got.optional, root)

    def test_and_luk_is_said_rather_than_lopa_for_one_form(self):
        # लुग्ग्रहणं सर्वादेशार्थम्, तच्च वह्यर्थम् — dropping the
        # last sound only would have left the wrong thing in
        # अदुह्वहि.
        self.assertIn("वह्यर्थम्",
                      provisions_for("7.3.73")[0].why)


class TheLengthenings(unittest.TestCase):
    """7.3.74–76."""

    def test_eight_roots_lengthen_before_syan(self):
        # शाम्यति, ताम्यति, भ्राम्यति, माद्यति.
        self.assertEqual(len(SAMADI_EIGHT), 8)
        for root in SAMADI_EIGHT:
            got = before_sit(root, before="śyan")
            self.assertEqual(got.sutra, "7.3.74", root)
            self.assertEqual(got.does, "dīrgha", root)

    def test_three_more_before_any_sit(self):
        # ष्ठीवति, क्लामति, आचामति.
        for root in ("ṣṭhivu", "klami", "ācam"):
            self.assertEqual(before_sit(root, before="śit").sutra,
                             "7.3.75", root)

    def test_klam_is_named_twice_and_the_vrtti_says_why(self):
        # क्लमिग्रहणं शबर्थम् — 7.3.74 reached it before श्यन्
        # only, and this rule adds the शप् conjugation.
        self.assertIn("klam", SAMADI_EIGHT)
        self.assertIn("शबर्थम्", provisions_for("7.3.75")[0].why)

    def test_kram_lengthens_only_in_the_parasmaipada(self):
        # क्रामति; आक्रमत आदित्यः otherwise.
        self.assertEqual(
            before_sit("kram", before="śit",
                       pada="parasmaipada").sutra, "7.3.76")
        self.assertNotEqual(
            before_sit("kram", before="śit",
                       pada="ātmanepada").sutra, "7.3.76")

    def test_and_utkrama_keeps_its_length_though_its_ending_is_gone(self):
        # न च हौ क्रमिरङ्गम्। किं तर्हि? शपि — 1.1.63 should have
        # stopped the rule, and does not, because the stem the
        # rule works on is the one before the शप्.
        self.assertIn("किं तर्हि? शपि",
                      provisions_for("7.3.76")[0].why)
        self.assertTrue(REGISTRY.has("1.1.63"))


class TheSubstitutions(unittest.TestCase):
    """7.3.77–79, and the largest यथासंख्यम् of the pāda."""

    def test_three_roots_take_a_ch(self):
        # इच्छति, गच्छति, यच्छति.
        self.assertEqual(ISU_GAM_YAM, ("iṣ", "gam", "yam"))
        for root in ISU_GAM_YAM:
            got = before_sit(root, before="śit")
            self.assertEqual(got.sutra, "7.3.77", root)
            self.assertEqual(got.does, "cha", root)

    def test_eleven_roots_get_eleven_stems_one_to_one(self):
        # पिबति, जिघ्रति, तिष्ठति, पश्यति, सीदति.
        self.assertEqual(len(PIBADI), 11)
        for root, stem in PIBADI:
            got = before_sit(root, before="śit")
            self.assertEqual(got.sutra, "7.3.78", root)
            self.assertEqual(got.does, stem, root)

    def test_a_crossed_pairing_reaches_nothing(self):
        # पा gives पिब and not तिष्ठ.
        self.assertEqual(
            before_sit("pā", before="śit", wants="tiṣṭha").sutra,
            "")

    def test_the_eleven_stems_are_all_distinct(self):
        stems = [stem for _, stem in PIBADI]
        self.assertEqual(len(set(stems)), len(stems))

    def test_the_vrtti_argues_about_pibas_guna(self):
        # अङ्गवृत्ते पुनर्वृत्तावविधिर्निष्ठितस्य — the light
        # penult should have taken guṇa, and a maxim stops it.
        self.assertIn("निष्ठितस्य",
                      provisions_for("7.3.78")[0].why)

    def test_jna_and_jan_become_ja(self):
        # जानाति, जायते — and the जन् meant is the दैवादिक one.
        for root in ("jñā", "jan"):
            got = before_sit(root, before="śit")
            self.assertEqual(got.sutra, "7.3.79", root)
            self.assertEqual(got.does, "jā", root)


class TheShortenings(unittest.TestCase):
    """7.3.80–81, and a disputed list."""

    def test_the_pvadi_roots_shorten(self):
        # पुनाति, लुनाति, स्तृणाति.
        got = before_sit(gana="pū-ādi", before="śit")
        self.assertEqual(got.sutra, "7.3.80")
        self.assertEqual(got.does, "hrasva")

    def test_where_the_list_ends_is_disputed_and_recorded(self):
        # केचिदिच्छन्ति one bound, अपरे तु another — and on the
        # second reading जानाति would shorten, the जा of the
        # sūtra before being what saves it.
        why = provisions_for("7.3.80")[0].why
        self.assertIn("केचिद् इच्छन्ति", why)
        self.assertIn("अपरे तु", why)

    def test_mi_shortens_in_the_veda_only(self):
        # प्रमिणन्ति व्रतानि; प्रमीणाति otherwise.
        self.assertEqual(
            before_sit("mī", before="śit", chandasi=True).sutra,
            "7.3.81")
        self.assertNotEqual(
            before_sit("mī", before="śit").sutra, "7.3.81")


class TheGunaThatClosesTheRun(unittest.TestCase):
    """7.3.82–83, and the rule after them."""

    def test_mid_takes_guna_before_a_sit(self):
        # मेद्यति; मिद्यते in the passive, whose यक् is no शित्.
        got = before_sit("mid", before="śit")
        self.assertEqual(got.sutra, "7.3.82")
        self.assertEqual(got.does, "guṇa")

    def test_an_ik_final_stem_takes_it_before_jus(self):
        # अजुहवुः, अबिभयुः, अबिभरुः.
        got = before_sit(gana="ik-anta", before="jus")
        self.assertEqual(got.sutra, "7.3.83")
        self.assertEqual(got.does, "guṇa")

    def test_why_cinuyuh_has_none_is_worked_out_in_full(self):
        # Two ङित् conditions are in play, and this rule
        # displaces only the one it has nowhere else to meet.
        why = provisions_for("7.3.83")[0].why
        self.assertIn("प्राप्ते चाप्राप्ते च", why)

    def test_the_rule_the_run_clears_the_way_for_is_codified_apart(self):
        # 7.3.84 सार्वधातुकार्धधातुकयोः was registered long
        # before this pāda was read, and a patch that splices
        # ahead of it must not disturb it.
        self.assertEqual(CODIFIED_APART, ("7.3.84",))
        self.assertTrue(REGISTRY.has("7.3.84"))
        self.assertNotIn("7.3.84", [r.sutra for r in SITI_TABLE])
        self.assertGreater(len(REGISTRY.get("7.3.84").notes), 200)


class NothingHappensByDefault(unittest.TestCase):
    """पच् and पठ् go into the present unchanged."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = before_sit("pac", before="śit")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(SITI_RUN, ("7.3.70", "7.3.83"))
        codes = [row.sutra for row in SITI_TABLE]
        self.assertEqual(
            codes, ["7.3.%d" % n for n in range(70, 84)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in SITI_TABLE:
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

    def test_the_sit_affixes_this_run_stands_before_are_live(self):
        # 3.1.68's शप्, 3.1.69's श्यन् and 3.1.81's श्ना are the
        # three शित् affixes every rule here is stated before,
        # and 3.1.70 is the option that keeps भ्रमति standing.
        for code in ("3.1.68", "3.1.69", "3.1.70", "3.1.81"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_but_the_end_of_the_pada_is_still_ahead(self):
        # 7.3.84 closes this run's business, and 7.3.85 to
        # 7.3.120 follow it — thirty-six sūtras this module does
        # not reach. When 7.3.85 lands this assertion fails.
        # Written as a debt: thirty-six sūtras stood between
        # this run and the end of the pāda. All of them have
        # landed, so the claim is now the live one — 7.3.120
        # closes the pāda and 7.4.1 opens the next.
        self.assertTrue(REGISTRY.has("7.3.85"))
        self.assertTrue(REGISTRY.has("7.3.120"))
        # 7.4.1 has landed since, and with it the pāda it
        # opens, so nothing of अध्याय ७ stands ahead of this run.
        self.assertTrue(REGISTRY.has("7.4.1"))


if __name__ == "__main__":
    unittest.main()
