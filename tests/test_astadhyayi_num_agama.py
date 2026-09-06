# -*- coding: utf-8 -*-
"""
७.१.५८–८३ — नुम्, the nasal put inside a stem.

Twenty-six sūtras about one augment, supplied for four different
reasons. The tests follow those four, and then the four-layer
stretch at 7.1.78–81 where a refusal, an option and a नित्यम् are
piled on one another.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.num_agama import (
    ABHYASTA_FOUR,
    ASTHYADI,
    DRK_THREE,
    GALAVA,
    MUCADI,
    NUM_RUN,
    NUM_TABLE,
    RADHI_JABHI,
    TRMPHADI,
    num,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheRootThatCarriesIt(unittest.TestCase):
    """7.1.58, and when the nasal actually goes in."""

    def test_an_idit_root_takes_num(self):
        # कुण्डिता, हुण्डिता.
        got = num(gana="idit-dhātu")
        self.assertEqual(got.sutra, "7.1.58")
        self.assertEqual(got.does, "num")

    def test_it_goes_in_while_the_root_is_still_being_taught(self):
        # अयं धातूपदेशावस्थायामेव नुमागमो भवति — and the vṛtti's
        # two proofs are 3.3.103's अ, which wants the heavy penult
        # the नुम् makes, and 3.1.80's complaint about roots with
        # the nasal already attached. Both are codified.
        why = provisions_for("7.1.58")[0].why
        self.assertIn("धातूपदेशावस्थायाम्", why)
        for code in ("3.3.103", "3.1.80"):
            self.assertTrue(REGISTRY.has(code), code)


class TheRootsAndTheirAffixes(unittest.TestCase):
    """7.1.59–69, each root with its own condition."""

    def test_eight_roots_take_it_before_sa(self):
        # मुञ्चति, लुम्पति, विन्दति, सिञ्चति.
        self.assertEqual(len(MUCADI), 8)
        for root in MUCADI:
            self.assertEqual(num(root, before="śa").sutra,
                             "7.1.59", root)

    def test_a_varttika_adds_five_that_had_lost_a_nasal(self):
        # तृम्फ, दृम्फ, गुम्फ, उम्भ, शुम्भ are read with a nasal,
        # 6.4.24 takes it out, and the vārttika puts one back —
        # and having been put in on purpose it cannot go again.
        self.assertEqual(len(TRMPHADI), 5)
        self.assertIn("विधानसामर्थ्याद्",
                      provisions_for("7.1.59")[0].why)
        self.assertTrue(REGISTRY.has("6.4.24"))

    def test_masj_and_nas_take_it_before_a_jhal(self):
        # मङ्क्ता, नंष्टा.
        for root in ("masj", "naś"):
            self.assertEqual(num(root, before="jhal").sutra,
                             "7.1.60", root)

    def test_and_for_masj_it_does_not_go_where_1_1_47_would_put_it(self):
        # मस्जेरन्त्यात् पूर्वं नुममिच्छन्ति — before the last
        # SOUND, so that the cluster may simplify to मग्नः. And
        # 1.1.47, the rule being departed from, is codified.
        # The quoted fragment starts after the junction: the text
        # has मस्जेरन्त्यात्, with मस्जेः and अन्त्यात् run
        # together, so न्त्यात् is where a substring can begin.
        self.assertIn("न्त्यात् पूर्वं",
                      provisions_for("7.1.60")[0].why)
        self.assertTrue(REGISTRY.has("1.1.47"))

    def test_radh_and_jabh_take_it_before_a_vowel(self):
        # रन्धयति, जम्भयति.
        self.assertEqual(RADHI_JABHI, ("radh", "jabh"))
        for root in RADHI_JABHI:
            self.assertEqual(num(root, before="ac").sutra,
                             "7.1.61", root)

    def test_but_radh_refuses_it_before_an_it(self):
        # रधिता, रधितुम्.
        got = num("radh", before="iṭ")
        self.assertEqual(got.sutra, "7.1.62")
        self.assertEqual(got.does, "")
        self.assertIn("7.1.61", got.blocked_by)

    def test_and_the_refusal_lapses_in_the_perfect(self):
        # ररन्धिव, ररन्धिम.
        self.assertNotEqual(num("radh", before="liṭ").sutra,
                            "7.1.62")


class Labh(unittest.TestCase):
    """7.1.64–69, five sūtras for one root."""

    def test_it_takes_num_before_a_vowel(self):
        # लम्भयति, लम्भकः.
        self.assertEqual(num("labh", before="ac").sutra, "7.1.64")

    def test_neither_after_sap_nor_in_the_perfect(self):
        # लभते, लेभे.
        for affix in ("śap", "liṭ"):
            self.assertEqual(num("labh", before=affix).sutra, "",
                             affix)

    def test_a_preverb_changes_which_rule_applies(self):
        # आलम्भ्या by 7.1.65, उपलम्भ्या by 7.1.66 with praise,
        # प्रलम्भः by 7.1.67 before खल् and घञ्.
        self.assertEqual(
            num("labh", upasarga="āṅ", before="ya-ādi").sutra,
            "7.1.65")
        self.assertEqual(
            num("labh", upasarga="upa", before="ya-ādi",
                sense="praśaṃsā").sutra, "7.1.66")
        self.assertEqual(
            num("labh", upasarga="upasarga", before="khal").sutra,
            "7.1.67")

    def test_su_and_dur_alone_refuse_it(self):
        # सुलभम्, दुर्लभम् — and सुप्रलम्भः has another preverb
        # beside them, so they are no longer alone.
        got = num("labh", upasarga="su-dur-kevala", before="khal")
        self.assertEqual(got.sutra, "7.1.68")
        self.assertEqual(got.does, "")
        self.assertIn("7.1.67", got.blocked_by)

    def test_and_before_cin_and_namul_it_is_optional(self):
        # अलाभि beside अलम्भि.
        for affix in ("ciṇ", "ṇamul"):
            got = num("labh", before=affix)
            self.assertEqual(got.sutra, "7.1.69", affix)
            self.assertTrue(got.optional, affix)


class TheStrongCases(unittest.TestCase):
    """7.1.70–73, where the नुम् shapes the declension."""

    def test_a_ugit_stem_takes_it_before_a_strong_ending(self):
        # भवान्, श्रेयान्, पचन्, प्राङ्.
        got = num(gana="ugit-añcati", before="sarvanāmasthāna")
        self.assertEqual(got.sutra, "7.1.70")

    def test_yuj_takes_it_only_outside_a_compound(self):
        # युङ्, and अश्वयुक् without.
        self.assertEqual(
            num("yuj", before="sarvanāmasthāna").sutra, "7.1.71")
        self.assertEqual(
            num("yuj", before="samāsa").sutra, "")

    def test_a_neuter_takes_it_by_a_later_rule(self):
        # यशांसि, कुण्डानि — and परत्वादनेनैव नुम् भवति where a
        # stem is both उगित् and झल्-final.
        got = num(gender="napuṃsaka", gana="jhal-ac-anta",
                  before="sarvanāmasthāna")
        self.assertEqual(got.sutra, "7.1.72")
        self.assertIn("7.1.70", got.blocked_by)

    def test_and_before_a_vowel_initial_case_ending(self):
        # त्रपुणी, जतुनी.
        got = num(gender="napuṃsaka", gana="ik-anta",
                  before="ac-ādi-vibhakti")
        self.assertEqual(got.sutra, "7.1.73")


class TheAsthyadiFour(unittest.TestCase):
    """7.1.75–77 give अनङ् and ई where नुम् would have come."""

    def test_they_take_anan_in_the_oblique_cases(self):
        # अस्थ्ना, दध्ने, सक्थ्ना, अक्ष्णा.
        self.assertEqual(len(ASTHYADI), 4)
        for stem in ASTHYADI:
            got = num(stem, gender="napuṃsaka",
                      before="tṛtīyā-ādi-ac")
            self.assertEqual(got.sutra, "7.1.75", stem)
            self.assertEqual(got.does, "anaṅ", stem)
            self.assertIn("7.1.73", got.blocked_by)

    def test_the_accent_is_part_of_the_rule(self):
        # स्थानिवद्भावादनुदात्तः स्यादित्युदात्तवचनम् — by 1.1.56
        # the substitute would have inherited the toneless
        # quality of what it replaced, so the sūtra says otherwise.
        why = provisions_for("7.1.75")[0].why
        # इति + उदात्तवचनम् is written इत्युदात्तवचनम्, so the
        # substring has to start after the junction.
        self.assertIn("त्युदात्तवचनम्", why)
        self.assertTrue(REGISTRY.has("1.1.56"))

    def test_the_veda_lets_every_condition_lapse(self):
        # अस्थभिः before a consonant, अस्थानि outside the oblique
        # cases, अक्षण्वता with no ending at all.
        got = num("asthi", chandasi=True)
        self.assertEqual(got.sutra, "7.1.76")

    def test_and_the_dual_takes_i_which_beats_the_num(self):
        # अक्षी ते इन्द्र — and the नुम् does not come back.
        got = num("akṣi", before="dvivacana", chandasi=True)
        self.assertEqual(got.sutra, "7.1.77")
        self.assertEqual(got.does, "ī")
        self.assertIn("7.1.73", got.blocked_by)


class FourLayersOnTheSatr(unittest.TestCase):
    """7.1.70 gives it, and three sūtras take it back and forth."""

    def test_a_reduplicated_stem_refuses_it(self):
        # ददत्, दधत्, जक्षत्, जाग्रत्.
        got = num("śatṛ", gana="abhyasta")
        self.assertEqual(got.sutra, "7.1.78")
        self.assertEqual(got.does, "")
        self.assertIn("7.1.70", got.blocked_by)

    def test_the_four_stems_are_all_reduplicated(self):
        self.assertEqual(ABHYASTA_FOUR,
                         ("dā", "dhā", "jakṣ", "jāgṛ"))

    def test_but_a_neuter_makes_the_refusal_optional(self):
        # ददति, ददन्ति कुलानि.
        got = num("śatṛ", gana="abhyasta", gender="napuṃsaka")
        self.assertEqual(got.sutra, "7.1.79")
        self.assertTrue(got.optional)
        self.assertIn("7.1.78", got.blocked_by)

    def test_an_a_final_stem_takes_it_optionally_before_si(self):
        # तुदती beside तुदन्ती.
        got = num("śatṛ", gana="a-varṇa-anta", before="śī")
        self.assertEqual(got.sutra, "7.1.80")
        self.assertTrue(got.optional)

    def test_but_after_sap_and_syan_it_is_compulsory(self):
        # पचन्ती, दीव्यन्ती — and the word नित्यम् is there to
        # end the option that has been governing.
        got = num("śatṛ", gana="śap-śyan", before="śī")
        self.assertEqual(got.sutra, "7.1.81")
        self.assertTrue(got.nitya)
        self.assertFalse(got.optional)
        self.assertIn("7.1.80", got.blocked_by)

    def test_the_two_satr_rules_are_told_apart_by_the_vikarana(self):
        # Both name the शतृ and differ only in what stands in
        # front of it, so the two columns must be read as a
        # conjunction. Read as alternatives, 7.1.81 swallows
        # 7.1.80 and तुदती loses its option.
        for code, gana in (("7.1.80", "a-varṇa-anta"),
                           ("7.1.81", "śap-śyan")):
            row = provisions_for(code)[0]
            self.assertEqual(row.of, ("śatṛ",), code)
            self.assertEqual(row.gana, gana, code)


class GalavasView(unittest.TestCase):
    """7.1.74 records a teacher's opinion without adopting it."""

    def test_a_bhasitapumska_neuter_may_behave_as_a_masculine(self):
        # ग्रामण्या beside ग्रामणिना.
        got = num(gana="bhāṣitapuṃska-ik-anta",
                  gender="napuṃsaka", before="tṛtīyā-ādi-ac")
        self.assertEqual(got.sutra, "7.1.74")
        self.assertEqual(got.does, "puṃvat")
        self.assertTrue(got.optional)

    def test_the_sutra_names_the_teacher(self):
        # Naming a teacher is how a view is recorded as an option
        # rather than adopted, and the module keeps the name.
        self.assertIn("gālava", GALAVA)
        self.assertIn("गालवस्य", provisions_for("7.1.74")[0].why)

    def test_what_it_buys_is_that_two_rules_do_not_apply(self):
        # यथा पुंसि ह्रस्वनुमौ न भवतः — no shortening and no नुम्.
        self.assertIn("ह्रस्वनुमौ न भवतः",
                      provisions_for("7.1.74")[0].why)
        self.assertIn("7.1.73", num(gana="bhāṣitapuṃska-ik-anta",
                                    gender="napuṃsaka",
                                    before="tṛtīyā-ādi-ac"
                                    ).blocked_by)


class TheLastTwo(unittest.TestCase):
    """7.1.82–83, before सु."""

    def test_anaduh_takes_num_before_su(self):
        # अनड्वान्, हे अनड्वन्.
        self.assertEqual(num("anaḍuh", before="su").sutra, "7.1.82")

    def test_three_more_take_it_in_the_veda(self):
        # ईदृङ्, स्ववान्, स्वतवाँः.
        self.assertEqual(len(DRK_THREE), 3)
        for stem in DRK_THREE:
            self.assertEqual(
                num(stem, before="su", chandasi=True).sutra,
                "7.1.83", stem)
            self.assertEqual(num(stem, before="su").sutra, "", stem)


class NothingHappensByDefault(unittest.TestCase):
    """Most stems take no नुम् anywhere."""

    def test_an_unnamed_stem_reaches_nothing(self):
        got = num("pac", before="ac")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(NUM_RUN, ("7.1.58", "7.1.83"))
        codes = [row.sutra for row in NUM_TABLE]
        self.assertEqual(
            codes, ["7.1.%d" % n for n in range(58, 84)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in NUM_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_three_sutras_supply_something_other_than_num(self):
        # 7.1.74's पुंवत्, 7.1.75–76's अनङ्, 7.1.77's ई — they
        # stand in this run because they are about the same stems
        # in the same environment, not because they are नुम्.
        other = sorted({row.sutra for row in NUM_TABLE
                        if row.does != "num"})
        self.assertEqual(
            other, ["7.1.74", "7.1.75", "7.1.76", "7.1.77"])


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_placement_rule_and_the_names_are_live(self):
        # 1.1.47's मिदचोऽन्त्यात् परः puts the नुम् where it
        # goes, and 1.1.43's सुडनपुंसकस्य names the strong
        # endings this run is stated before.
        self.assertTrue(REGISTRY.has("1.1.47"))
        self.assertTrue(REGISTRY.has("1.1.43"))

    def test_what_the_nasal_then_becomes_is_live_now(self):
        # यशांसि needs 8.3.24 नश्चापदान्तस्य झलि for its anusvāra
        # and मुञ्चति needs 8.4.58 अनुस्वारस्य ययि परसवर्णः to
        # turn that anusvāra into the nasal of its own class.
        # Both have landed, so the नुम् this run gives can be
        # followed to the sound actually heard.
        self.assertTrue(REGISTRY.has("8.3.24"))
        self.assertTrue(REGISTRY.has("8.4.58"))


if __name__ == "__main__":
    unittest.main()
