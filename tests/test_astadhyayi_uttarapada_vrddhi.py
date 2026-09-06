# -*- coding: utf-8 -*-
"""
७.३.१–३१ — the taddhita vṛddhi qualified, and the second member.

The pāda opens by qualifying a rule stated in the pāda before,
so the first class asserts that relation. Then the heading, the
rules that move the operation to the second member, the six that
give it to both, and the refusal that is read as proof about the
order of the whole grammar.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.uttarapada_vrddhi import (
    BAHIRANGA,
    DEVIKADI,
    JANGALADI,
    KEKAYADI,
    SUCI_FIVE,
    SVAGATADI,
    UTTARAPADA_FROM,
    UTTARAPADA_TO,
    VRDDHI_RUN,
    VRDDHI_TABLE,
    provisions_for,
    uttarapada_vrddhi,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class ThePadaOpensOnTheOneBefore(unittest.TestCase):
    """7.3.1–5 all qualify 7.2.117, which is codified."""

    def test_the_rule_they_qualify_is_live(self):
        # 7.2.117 तद्धितेष्वचामादेः gives the FIRST vowel of a
        # stem vṛddhi before a taddhita; this run is where that
        # is taken back, five sūtras deep.
        self.assertTrue(REGISTRY.has("7.2.117"))
        qualifying = [row.sutra for row in VRDDHI_TABLE
                      if "7.2.117" in row.blocks]
        self.assertEqual(
            qualifying, ["7.3.%d" % n for n in range(1, 6)])

    def test_five_stems_take_a_plain_a_instead(self):
        # दाविकम्, शांशपश्चमसः, दीर्घसात्रम्.
        self.assertEqual(len(DEVIKADI), 5)
        for stem in DEVIKADI:
            got = uttarapada_vrddhi(stem, before="ñit")
            self.assertEqual(got.sutra, "7.3.1", stem)
            self.assertEqual(got.does, "āt", stem)

    def test_and_three_turn_their_ya_into_iya(self):
        # कैकेयः, मैत्रेयिकया, प्रालेयम्.
        self.assertEqual(len(KEKAYADI), 3)
        for stem in KEKAYADI:
            got = uttarapada_vrddhi(stem, before="ñit")
            self.assertEqual(got.sutra, "7.3.2", stem)
            self.assertEqual(got.does, "iy", stem)

    def test_a_word_final_y_or_v_takes_an_augment_in_front(self):
        # वैयाकरणः, सौवश्वः — no vṛddhi, and an ऐ or औ put in
        # BEFORE the semivowel instead.
        got = uttarapada_vrddhi(gana="y-v-pada-anta-pūrva",
                                before="ñit")
        self.assertEqual(got.sutra, "7.3.3")
        self.assertEqual(got.does, "aic")
        self.assertEqual(got.where, "pūrva-āgama")

    def test_the_refusal_is_stated_to_fix_the_augments_place(self):
        # प्रतिषेधवचनमैचोर्विषयप्रक्ऌप्त्यर्थम् — दाध्यश्विः has
        # a य् too, and no augment comes there.
        self.assertIn("विषयप्रक्ऌप्त्यर्थम्",
                      provisions_for("7.3.3")[0].why)


class AndFourSutrasTakeThatBack(unittest.TestCase):
    """7.3.6–9, each undoing the refusal AND the augment."""

    def test_reciprocal_action_cancels_both_at_once(self):
        # व्यावक्रोशी — प्रतिषेधागमयोरयं प्रतिषेधः.
        got = uttarapada_vrddhi(sense="karma-vyatihāra",
                                before="ñit")
        self.assertEqual(got.sutra, "7.3.6")
        self.assertEqual(set(got.blocked_by), {"7.3.3", "7.3.4"})
        self.assertEqual(got.does, "")

    def test_seven_stems_do_the_same(self):
        # स्वागतिकः, व्याडिः, व्यावहारिकः, स्वापतेयः.
        self.assertEqual(len(SVAGATADI), 7)
        for stem in SVAGATADI:
            got = uttarapada_vrddhi(stem, before="ñit")
            self.assertEqual(got.sutra, "7.3.7", stem)

    def test_vyavahara_is_named_although_the_sutra_before_reaches_it(self):
        # व्यवहारशब्दोऽयं लौकिके वृत्ते वर्तते, न तु
        # कर्मव्यतिहारे — its sense is worldly dealing.
        self.assertIn("vyavahāra", SVAGATADI)
        self.assertIn("लौकिके वृत्ते",
                      provisions_for("7.3.7")[0].why)

    def test_svan_before_in_is_refused_and_pada_optionally(self):
        # श्वाभस्त्रिः; श्वापदम् beside शौवापदम्.
        self.assertEqual(
            uttarapada_vrddhi(gana="śvan-ādi", before="iñ").sutra,
            "7.3.8")
        got = uttarapada_vrddhi(gana="śvan-ādi",
                                uttarapada="pada")
        self.assertEqual(got.sutra, "7.3.9")
        self.assertTrue(got.optional)


class TheUttarapadaHeading(unittest.TestCase):
    """7.3.10 opens it and 7.3.31 closes it."""

    def test_the_heading_runs_where_the_vrtti_says(self):
        # उत्तरपदस्येत्ययमधिकारः, हनस्तोऽचिण्णलोः इति
        # प्रागेतस्मात् — 7.3.32 is the bound.
        self.assertEqual(UTTARAPADA_FROM, "7.3.10")
        self.assertEqual(UTTARAPADA_TO, "7.3.31")
        self.assertEqual(UTTARAPADA_TO, VRDDHI_RUN[1])

    def test_the_heading_supplies_nothing_of_its_own(self):
        row, = provisions_for("7.3.10")
        self.assertTrue(row.heading)
        self.assertEqual(row.does, "")

    def test_and_is_unreachable(self):
        # A heading that answered queries would take them from
        # the rules under it.
        for query in ({"before": "ñit"},
                      {"purvapada": "avayava",
                       "uttarapada": "ṛtu", "before": "ñit"}):
            self.assertNotEqual(
                uttarapada_vrddhi(**query).sutra, "7.3.10", query)

    def test_the_operation_falls_on_the_second_member(self):
        # पूर्ववार्षिकम्, सुपाञ्चालकः, द्विसांवत्सरिकः.
        wanted = {
            ("avayava", "ṛtu"): "7.3.11",
            ("su-sarva-ardha", "janapada"): "7.3.12",
            ("diś", "janapada"): "7.3.13",
            ("saṃkhyā", "saṃvatsara-saṃkhyā"): "7.3.15",
            ("saṃkhyā", "varṣa"): "7.3.16",
            ("saṃkhyā", "parimāṇa"): "7.3.17",
        }
        for (first, second), code in wanted.items():
            got = uttarapada_vrddhi(purvapada=first,
                                    uttarapada=second,
                                    before="ñit")
            self.assertEqual(got.sutra, code, (first, second))
            self.assertEqual(got.where, "uttarapada", code)

    def test_one_of_them_has_no_first_member_to_read_it_out_of(self):
        # जे प्रोष्ठपदानाम् — this is the sūtra the heading was
        # needed for, there being no ablative in it.
        row, = provisions_for("7.3.18")
        self.assertEqual(row.purvapada, "")
        self.assertEqual(row.uttarapada, "proṣṭhapadā")
        self.assertEqual(
            uttarapada_vrddhi(uttarapada="proṣṭhapadā",
                              sense="jāta", before="ñit").sutra,
            "7.3.18")

    def test_and_a_sense_is_what_licenses_three_of_them(self):
        # प्रोष्ठपादो माणवकः of birth; पूर्वैषुकामशमः and
        # सौह्मनागरः of the eastern country.
        for code, sense in (("7.3.18", "jāta"),
                            ("7.3.14", "prācām"),
                            ("7.3.24", "prācām")):
            self.assertEqual(provisions_for(code)[0].sense, sense,
                             code)


class WhereBothMembersStrengthen(unittest.TestCase):
    """7.3.19–24, and the two refusals inside them."""

    def test_six_rules_give_it_to_both(self):
        both = [row.sutra for row in VRDDHI_TABLE
                if row.where == "both"]
        self.assertEqual(
            both, ["7.3.19", "7.3.20", "7.3.21", "7.3.24"])

    def test_three_word_endings_take_it_on_both(self):
        # सौहार्दम्, सौभाग्यम्, दौर्भाग्यम्.
        got = uttarapada_vrddhi(gana="hṛd-bhaga-sindhu-anta",
                                before="ñit")
        self.assertEqual(got.sutra, "7.3.19")
        self.assertEqual(got.where, "both")

    def test_a_deity_dvandva_too_but_not_a_following_indra(self):
        # आग्निमारुतं कर्म; but सौमेन्द्रः, आग्नेन्द्रः.
        self.assertEqual(
            uttarapada_vrddhi(gana="devatā-dvandva",
                              before="ñit").sutra, "7.3.21")
        got = uttarapada_vrddhi(uttarapada="indra", before="ñit")
        self.assertEqual(got.sutra, "7.3.22")
        self.assertEqual(got.does, "")
        self.assertIn("7.3.21", got.blocked_by)

    def test_that_refusal_is_read_as_proof_about_rule_order(self):
        # The vṛddhi could not have applied anyway, इन्द्र's इ
        # being lost first. That the refusal is stated at all
        # shows the members' own operations come BEFORE the
        # merger — which is what makes पूर्वैषुकामशमः possible.
        why = provisions_for("7.3.22")[0].why
        self.assertIn("ज्ञापकम्", why)
        self.assertIn("बहिरङ्गम्", BAHIRANGA)
        self.assertIn("पश्चाद् एकादेशः", BAHIRANGA)
        self.assertTrue(REGISTRY.has("6.4.148"))

    def test_and_varuna_after_a_long_vowel_is_refused_too(self):
        # ऐन्द्रावरुणम्, मैत्रावरुणम्.
        got = uttarapada_vrddhi(uttarapada="varuṇa",
                                purvapada="dīrgha-anta",
                                before="ñit")
        self.assertEqual(got.sutra, "7.3.23")
        self.assertIn("7.3.21", got.blocked_by)


class TheOptionalHalves(unittest.TestCase):
    """7.3.25–31, where one member's vṛddhi is a choice."""

    def test_three_endings_make_the_second_members_optional(self):
        # कौरुजङ्गलम्, कौरुजाङ्गलम्.
        self.assertEqual(JANGALADI, ("jaṅgala", "dhenu", "valaja"))
        got = uttarapada_vrddhi(
            gana="jaṅgala-dhenu-valaja-anta", before="ñit")
        self.assertEqual(got.sutra, "7.3.25")
        self.assertTrue(got.optional)
        self.assertEqual(got.where, "pūrva")

    def test_and_four_rules_make_the_first_members_optional(self):
        # आर्धद्रौणिकम् beside अर्धद्रौणिकम्; प्रावाहणेयः beside
        # प्रवाहणेयः; अशौचम् beside आशौचम्.
        optional_first = [row.sutra for row in VRDDHI_TABLE
                          if row.purva_optional]
        self.assertEqual(
            optional_first,
            ["7.3.26", "7.3.27", "7.3.28", "7.3.29", "7.3.30"])

    def test_a_measure_beginning_with_a_short_a_is_refused(self):
        # अर्धप्रस्थिकः — and the तपर is there for 6.3.39's sake.
        got = uttarapada_vrddhi(purvapada="ardha",
                                uttarapada="a-parimāṇa",
                                before="ñit")
        self.assertEqual(got.sutra, "7.3.27")
        self.assertEqual(got.does, "")
        self.assertTrue(got.purva_optional)
        self.assertIn("6.3.39", provisions_for("7.3.27")[0].why)
        self.assertTrue(REGISTRY.has("6.3.39"))

    def test_five_stems_after_nan_take_it_and_the_nan_optionally(self):
        # अशौचम्, अनैश्वर्यम्, अकौशलम्, अनैपुणम्.
        self.assertEqual(len(SUCI_FIVE), 5)
        for stem in SUCI_FIVE:
            got = uttarapada_vrddhi(stem, purvapada="nañ",
                                    before="ñit")
            self.assertEqual(got.sutra, "7.3.30", stem)
            self.assertTrue(got.purva_optional, stem)

    def test_and_two_more_take_it_by_turns(self):
        # आयथातथ्यम्, अयाथातथ्यम् — one or the other, never both.
        for stem in ("yathātatha", "yathāpura"):
            got = uttarapada_vrddhi(stem, purvapada="nañ",
                                    before="ñit")
            self.assertEqual(got.sutra, "7.3.31", stem)
            self.assertTrue(got.optional, stem)
            self.assertIn("7.3.30", got.blocked_by)

    def test_the_two_words_are_read_as_different_compounds_twice(self):
        # ब्राह्मणादि has them as नञ्-compounds, this sūtra as
        # अव्ययीभाव ones by 2.1.7, and the Bhāṣya a third way.
        why = provisions_for("7.3.31")[0].why
        self.assertIn("2.1.7", why)
        self.assertIn("2.1.4", why)


class NothingHappensByDefault(unittest.TestCase):
    """7.2.117 stands where this run says nothing."""

    def test_an_unnamed_stem_reaches_nothing(self):
        got = uttarapada_vrddhi("garga", before="ñit")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")

    def test_and_the_answer_defers_to_the_pada_before(self):
        self.assertIn("7.2.117",
                      uttarapada_vrddhi("garga", before="ñit").why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(VRDDHI_RUN, ("7.3.1", "7.3.31"))
        codes = [row.sutra for row in VRDDHI_TABLE]
        self.assertEqual(
            codes, ["7.3.%d" % n for n in range(1, 32)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in VRDDHI_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_the_two_rules_codified_apart_survive(self):
        # 7.3.84 and 7.3.101 were registered long before this
        # pāda was read, and a patch that splices ahead of them
        # must not disturb them.
        for code in ("7.3.84", "7.3.101"):
            self.assertTrue(REGISTRY.has(code), code)
            self.assertGreater(len(REGISTRY.get(code).notes), 200,
                               code)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_taddhitas_this_run_qualifies_are_live(self):
        # 4.1.168's अञ् gives कैकेयः, 4.2.124's वुञ् gives
        # सुपाञ्चालकः, 4.4.1's ठक् gives आक्षिकः, and 7.2.117 is
        # the vṛddhi all of it qualifies. All codified.
        for code in ("4.1.168", "4.2.124", "4.4.1", "7.2.117"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_the_rest_of_this_pada_is_read_now(self):
        # Written as a debt when neither was codified. 7.3.32
        # हनस्तोऽचिण्णलोः — the bound this run's heading names —
        # and 7.3.52's कुत्व have both landed, so the heading's
        # own end can be asked of the engine. 7.4.1 is still
        # ahead, and when it lands this fails.
        self.assertTrue(REGISTRY.has("7.3.32"))
        self.assertTrue(REGISTRY.has("7.3.52"))
        # 7.4.1 has landed too, so the whole adhyāya stands
        # behind this run's heading rather than half of it.
        self.assertTrue(REGISTRY.has("7.4.1"))


if __name__ == "__main__":
    unittest.main()
