# -*- coding: utf-8 -*-
"""
७.१.३४–५० — four rules of the language, then thirteen of the Veda.

The tests are built around the heading: 7.1.38 opens छन्दसि and
7.1.50 closes it, and everything between is out of reach unless
the caller says the passage is Vedic. The Kāśikā's own **इति
प्राप्ते** — what the ordinary grammar would have given — is kept
as a column and asserted, not summarised.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.chandasi_adesa import (
    CHANDAS_FROM,
    CHANDAS_RUN,
    CHANDAS_TO,
    SNATVYADI,
    SUP_TEN,
    TAP_FOUR,
    VEDIC_TABLE,
    WIDENED_BY,
    in_the_veda,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheLastOrdinaryRules(unittest.TestCase):
    """7.1.34–37, before the Veda takes over."""

    def test_nal_becomes_au_after_an_a_final_stem(self):
        # पपौ, तस्थौ, जग्लौ, मम्लौ.
        got = in_the_veda("ṇal", after="ā-anta")
        self.assertEqual(got.sutra, "7.1.34")
        self.assertEqual(got.does, "au")

    def test_tu_and_hi_take_tatan_in_a_blessing(self):
        # जीवताद् भवान् beside जीवतु भवान्.
        for ending in ("tu", "hi"):
            got = in_the_veda(ending, sense="āśis")
            self.assertEqual(got.sutra, "7.1.35", ending)
            self.assertTrue(got.optional, ending)

    def test_and_not_in_an_order(self):
        # ग्रामं गच्छतु भवान्.
        self.assertNotEqual(in_the_veda("tu").sutra, "7.1.35")

    def test_satr_becomes_vasu_after_vid(self):
        # विद्वान्, विद्वांसौ, विद्वांसः.
        got = in_the_veda("śatṛ", root="vid")
        self.assertEqual(got.sutra, "7.1.36")
        self.assertEqual(got.does, "vasu")

    def test_the_rule_its_u_was_written_for_is_live(self):
        # वसोरुकारकरणं क्वसोरपि सामान्यग्रहणार्थम् — the substitute
        # is वसु and not वस् so that 6.4.131 may catch क्वसु too.
        self.assertTrue(REGISTRY.has("6.4.131"))
        self.assertIn("6.4.131", provisions_for("7.1.36")[0].why)

    def test_ktva_becomes_lyap_in_a_compound(self):
        # प्रकृत्य, प्रहृत्य, द्विधाकृत्य.
        got = in_the_veda("ktvā", samasa="an-añ-pūrva")
        self.assertEqual(got.sutra, "7.1.37")
        self.assertEqual(got.does, "lyap")

    def test_and_not_outside_one(self):
        # कृत्वा, हृत्वा.
        self.assertEqual(in_the_veda("ktvā").sutra, "")


class TheHeading(unittest.TestCase):
    """छन्दसि, and how far the vṛtti says it reaches."""

    def test_the_veda_opens_at_the_sutra_the_vrtti_names(self):
        # छन्दोऽधिकार आज्जसेरसुक् इति यावत् — 7.1.38 to 7.1.50.
        self.assertEqual(CHANDAS_FROM, "7.1.38")
        self.assertEqual(CHANDAS_TO, "7.1.50")
        self.assertEqual(CHANDAS_RUN, ("7.1.34", "7.1.50"))

    def test_every_rule_inside_it_wants_the_veda(self):
        for row in VEDIC_TABLE:
            if CHANDAS_FROM <= row.sutra <= CHANDAS_TO:
                self.assertTrue(row.chandasi, row.sutra)

    def test_and_no_rule_before_it_does(self):
        for row in VEDIC_TABLE:
            if row.sutra < CHANDAS_FROM:
                self.assertFalse(row.chandasi, row.sutra)

    def test_the_veda_lets_the_ktva_stay(self):
        # परिधापयित्वा — and outside the Veda 7.1.37's ल्यप् is
        # compulsory.
        got = in_the_veda("ktvā", samasa="an-añ-pūrva",
                          chandasi=True)
        self.assertEqual(got.sutra, "7.1.38")
        self.assertIn("7.1.37", got.blocked_by)


class TheLoosestRuleInTheBook(unittest.TestCase):
    """7.1.39, and the two vārttikas that widen it further."""

    def test_any_ending_may_stand_for_any_other(self):
        # ऋजवः सन्तु पन्थाः, where पन्थानः was due.
        got = in_the_veda("sup", chandasi=True)
        self.assertEqual(got.sutra, "7.1.39")
        self.assertIn("पन्थानः", got.instead_of)

    def test_it_names_eleven_substitutes(self):
        # सु लुक् पूर्वसवर्ण आ आत् शे या डा ड्या याच् आल्.
        self.assertEqual(len(SUP_TEN), 11)
        self.assertIn("luk", SUP_TEN)
        self.assertIn("pūrvasavarṇa", SUP_TEN)

    def test_two_varttikas_widen_it_past_what_it_says(self):
        # सुपां सुपो भवन्ति reaches any nominal ending for any
        # other, and तिङां तिङो भवन्ति the verbal endings too —
        # which the sūtra itself never mentions.
        self.assertEqual(len(WIDENED_BY), 2)
        self.assertIn("तिङां तिङो", WIDENED_BY[1])
        why = provisions_for("7.1.39")[0].why
        for varttika in WIDENED_BY:
            self.assertIn(varttika.split()[0], why)


class WhatTheOrdinaryGrammarWouldHaveGiven(unittest.TestCase):
    """The Kāśikā's इति प्राप्ते, kept as a column."""

    def test_every_vedic_substitution_records_what_it_displaces(self):
        # A Vedic rule is only intelligible against the form that
        # was due, so the ones that replace something must say
        # what. The निपातन rules record it too; only the ones
        # that supply an augment to an unchanged word need not.
        for row in VEDIC_TABLE:
            if row.chandasi and row.does not in ("ktvā",):
                self.assertTrue(row.instead_of, row.sutra)

    def test_the_atmanepada_t_goes_and_that_finishes_a_form(self):
        # 7.1.8's अदुह्र is not finished until here: the झ became
        # अत् by 7.1.5, took रुट् by 7.1.8, and loses its त् now.
        got = in_the_veda("ta", after="ātmanepada", chandasi=True)
        self.assertEqual(got.sutra, "7.1.41")
        self.assertIn("अदुहत", got.instead_of)
        self.assertTrue(REGISTRY.has("7.1.8"))

    def test_dhvam_becomes_dhvat(self):
        # वारयध्वात्, where वारयध्वम् was due.
        got = in_the_veda("dhvam", chandasi=True)
        self.assertEqual(got.sutra, "7.1.42")
        self.assertIn("वारयध्वम्", got.instead_of)


class TheImperativeT(unittest.TestCase):
    """7.1.44 and 7.1.45 both reach it, and both are the Veda's."""

    def test_it_may_become_tat(self):
        # कृणुतात्, खनतात्, संसृजतात्, गमयतात्.
        got = in_the_veda("ta", chandasi=True, wants="tāt")
        self.assertEqual(got.sutra, "7.1.44")

    def test_or_one_of_four_others(self):
        # शृणोत, सुनोता, दधातन, जुजुष्टन, यदिष्ठन.
        self.assertEqual(TAP_FOUR, ("tap", "tanap", "tan", "than"))
        got = in_the_veda("ta", chandasi=True,
                          wants="tap-tanap-tan-than")
        self.assertEqual(got.sutra, "7.1.45")

    def test_the_two_rules_genuinely_overlap(self):
        # Both name the same त in the same Veda, and neither
        # blocks the other. Asked without saying which substitute
        # is wanted, the resolver can only pick one — so the
        # query has to name it, and the test says so rather than
        # pretending the rules are disjoint.
        for code in ("7.1.44", "7.1.45"):
            row = provisions_for(code)[0]
            self.assertEqual(row.of, ("ta",), code)
            self.assertTrue(row.chandasi, code)
            self.assertEqual(row.blocks, (), code)


class TheWordsLaidDown(unittest.TestCase):
    """7.1.43, 7.1.48, 7.1.49 — निपातन in the Veda."""

    def test_yajadhvainam_is_laid_down_before_enam(self):
        # यजध्वैनं प्रियमेधाः — two changes at once.
        got = in_the_veda("yajadhvam", before="enam", chandasi=True)
        self.assertEqual(got.sutra, "7.1.43")
        self.assertTrue(got.nipatana)

    def test_and_only_before_enam(self):
        self.assertNotEqual(
            in_the_veda("yajadhvam", chandasi=True).sutra, "7.1.43")

    def test_istvinam_is_laid_down_whole(self):
        got = in_the_veda("iṣṭvīnam", chandasi=True)
        self.assertEqual(got.sutra, "7.1.48")
        self.assertTrue(got.nipatana)

    def test_snatvi_names_an_open_class(self):
        # प्रकारार्थोऽयमादिशब्दः — a kind, not a closed list.
        self.assertEqual(SNATVYADI, ("snātvī", "pītvī"))
        for word in SNATVYADI:
            self.assertEqual(
                in_the_veda(word, chandasi=True).sutra, "7.1.49",
                word)


class TheAugments(unittest.TestCase):
    """7.1.46, 7.1.47, 7.1.50 supply rather than replace."""

    def test_three_rules_supply_an_augment(self):
        supplied = [row.sutra for row in VEDIC_TABLE if row.augment]
        self.assertEqual(supplied, ["7.1.46", "7.1.47", "7.1.50"])

    def test_the_jas_takes_asuk_after_an_a_final_stem(self):
        # ब्राह्मणासः पितरः सोम्यासः.
        got = in_the_veda("jas", after="a-varṇa-anta",
                          chandasi=True)
        self.assertEqual(got.sutra, "7.1.50")
        self.assertTrue(got.augment)

    def test_the_ktva_takes_yak_only_when_that_is_what_is_wanted(self):
        # दत्त्वाय — and 7.1.38 reaches the same query, the two
        # rules being about the same क्त्वा in the same Veda.
        got = in_the_veda("ktvā", samasa="an-añ-pūrva",
                          chandasi=True, wants="yak")
        self.assertEqual(got.sutra, "7.1.47")
        self.assertTrue(got.augment)


class OutsideTheVedaNothingHappens(unittest.TestCase):
    """The heading's whole force, asked as a question."""

    def test_no_vedic_rule_is_reached_without_the_flag(self):
        for row in VEDIC_TABLE:
            if not row.chandasi:
                continue
            query = {}
            if row.of:
                query["what"] = row.of[0]
            if row.after:
                query["after"] = row.after
            if row.before:
                query["before"] = row.before[0]
            if row.samasa:
                query["samasa"] = row.samasa
            self.assertNotEqual(
                in_the_veda(**query).sutra, row.sutra, row.sutra)

    def test_and_an_unnamed_thing_reaches_nothing_at_all(self):
        got = in_the_veda("ghañ", chandasi=True)
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        codes = [row.sutra for row in VEDIC_TABLE]
        self.assertEqual(
            codes, ["7.1.%d" % n for n in range(34, 51)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in VEDIC_TABLE:
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

    def test_the_affixes_this_run_reshapes_are_live(self):
        # 3.2.124's शतृ becomes वसु here, 3.4.21's क्त्वा becomes
        # ल्यप्, and 6.4.131 is what 7.1.36's उ was written for.
        # All three are codified.
        for code in ("3.2.124", "3.4.21", "6.4.131"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_the_rules_these_forms_then_meet_are_not(self):
        # 7.1.35's ब्रूताद् भवान् turns on 7.3.93's ईट् not
        # coming, and 7.1.40's वधीम् on 6.4.75's बहुलम् stopping
        # the अट्. Neither is read yet; when either lands this
        # assertion fails and the note must state the live edge.
        # 7.3.93's ईट् has landed with पाद ७.३, so ब्रूताद्
        # भवान् can be asked against the rule 7.1.35's ङित्
        # holds off. 7.4.1 is still ahead.
        self.assertTrue(REGISTRY.has("7.3.93"))
        self.assertTrue(REGISTRY.has("6.4.75"))
        # पाद ७.४ has been read through since, so both forms
        # this test names stand against a complete अध्याय ७.
        self.assertTrue(REGISTRY.has("7.4.1"))


if __name__ == "__main__":
    unittest.main()
