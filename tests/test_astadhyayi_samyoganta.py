# -*- coding: utf-8 -*-
"""
८.२.२३–४१ — संयोगान्तस्य लोपः, and the consonant at a word's end.

Two blocks: seven sūtras that take a sound away and twelve that
change one. The class that matters most is the first, where a
single sūtra's vṛtti works three orderings against three other
rules and gets three different answers — which is the whole
point of 8.2.1 in one place.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.samyoganta import (
    CHANGES_FROM,
    DRUH_FOUR,
    SAMYOGA_RUN,
    SAMYOGA_TABLE,
    THREE_ANSWERS,
    VRASCADI_EIGHT,
    at_the_end,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheClustersLoss(unittest.TestCase):
    """8.2.23–24, and the ordering the vṛtti settles."""

    def test_a_cluster_final_word_loses_its_last_sound(self):
        # गोमान्, यवमान्, कृतवान्.
        got = at_the_end(gana="saṃyoga-anta", before="pada-anta")
        self.assertEqual(got.sutra, "8.2.23")
        self.assertEqual(got.does, "lopa")

    def test_and_one_sutra_gets_three_answers_from_one_heading(self):
        # रुत्वं परम् अपि असिद्धत्वात् — 8.2.66 is later and
        # invisible; जश्त्वे तु न अप्राप्ते — 8.2.39 displaces
        # it; and a semivowel is बहिरङ्ग and leaves no cluster.
        for fragment in ("रुत्वं परम्", "जश्त्वे तु",
                         "बहिरङ्गलक्षणस्य"):
            self.assertIn(fragment, THREE_ANSWERS, fragment)
        self.assertIn("जश्त्वे तु", provisions_for("8.2.23")[0].why)

    def test_and_all_three_of_the_rules_it_weighs_are_codified(self):
        for code in ("8.2.1", "8.2.39", "8.2.66"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_but_a_cluster_with_an_r_loses_its_s_instead(self):
        # गोभिरक्षाः — and without it 8.2.23 would leave अक्षार्.
        got = at_the_end(gana="repha-saṃyoga-anta",
                         before="pada-anta")
        self.assertEqual(got.sutra, "8.2.24")
        self.assertIn("8.2.23", got.blocked_by)


class TheAoristsFourLosses(unittest.TestCase):
    """8.2.25–28, four places one स् goes."""

    def test_each_of_the_four_has_its_own_environment(self):
        wanted = {("sic", "dha-ādi"): "8.2.25",
                  ("jhal-anta-sic", "jhal"): "8.2.26",
                  ("hrasva-anta-aṅga", "jhal"): "8.2.27",
                  ("iṭ-anta", "īṭ"): "8.2.28"}
        for (gana, before), code in wanted.items():
            got = at_the_end(gana=gana, before=before)
            self.assertEqual(got.sutra, code, gana)
            self.assertEqual(got.does, "lopa", gana)

    def test_and_one_of_them_saves_a_sound_that_would_never_be_heard(self):
        # यद्य् अत्र सकारलोपो न स्यात् … न धकारः श्रूयेत.
        why = provisions_for("8.2.25")[0].why
        self.assertIn("न धकारः श्रूयेत", why)

    def test_and_from_there_on_it_is_the_aorists_s_that_is_meant(self):
        # इतः प्रभृति सिचः सकारस्य लोप इष्यते — which is why
        # पयो धावति is untouched.
        self.assertIn("इतः प्रभृति",
                      provisions_for("8.2.25")[0].why)
        self.assertIn("पयो धावति",
                      provisions_for("8.2.25")[0].keeps_out)

    def test_and_one_shows_the_ordering_the_other_way_round(self):
        # अवात्ताम् — the loss is invisible to 7.4.49, so the
        # त् is made first and only then does the स् go.
        why = provisions_for("8.2.26")[0].why
        self.assertIn("7.4.49", why)
        self.assertTrue(REGISTRY.has("7.4.49"))

    def test_and_a_clusters_head_goes_too(self):
        # लग्नः, साधुलक्, तट्, तष्टः.
        got = at_the_end(gana="sa-ka-saṃyoga-ādi",
                         before="pada-anta")
        self.assertEqual(got.sutra, "8.2.29")
        self.assertIn("सङि", provisions_for("8.2.29")[0].why)


class WhereTheRunTurns(unittest.TestCase):
    """8.2.30 onwards, where sounds change instead of going."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(CHANGES_FROM, "8.2.30")

    def test_and_everything_before_it_takes_a_sound_away(self):
        def number(code):
            return int(code.rsplit(".", 1)[1])

        for row in SAMYOGA_TABLE:
            if number(row.sutra) < number(CHANGES_FROM):
                self.assertEqual(row.does, "lopa", row.sutra)
            else:
                self.assertNotEqual(row.does, "lopa", row.sutra)

    def test_a_palatal_becomes_a_guttural(self):
        # पक्ता, ओदनपक्, वाक्.
        for after in ("jhal", "pada-anta"):
            got = at_the_end(gana="cu", before=after)
            self.assertEqual(got.sutra, "8.2.30", after)
            self.assertEqual(got.does, "ku", after)


class TheFiveSoundsOfOneH(unittest.TestCase):
    """8.2.31–35, where ह् becomes five different things."""

    def test_a_bare_h_becomes_dha(self):
        # सोढा, वोढा, जलाषाट्.
        got = at_the_end(gana="ha", before="jhal")
        self.assertEqual(got.sutra, "8.2.31")
        self.assertEqual(got.does, "ḍha")

    def test_but_a_d_initial_root_gives_gha_instead(self):
        # दग्धा, गोधुक् — and लेढा keeps the ढ्.
        got = at_the_end("da-ādi-dhātu", gana="ha", before="jhal")
        self.assertEqual(got.sutra, "8.2.32")
        self.assertEqual(got.does, "gha")
        self.assertIn("लेढा", provisions_for("8.2.32")[0].keeps_out)

    def test_and_the_first_draft_let_a_bare_h_reach_that_rule(self):
        # 8.2.32 wants a root that begins with द् AND has a ह्,
        # so it carries no `gana` at all — the of/gana columns
        # are alternatives everywhere else in this table.
        row = provisions_for("8.2.32")[0]
        self.assertEqual(row.gana, "")
        self.assertEqual(row.of, ("da-ādi-dhātu",))
        self.assertEqual(
            at_the_end(gana="ha", before="jhal").sutra, "8.2.31")

    def test_four_roots_take_the_gha_only_optionally(self):
        # द्रोग्धा beside द्रोढा; मित्रध्रुक् beside मित्रध्रुट्.
        self.assertEqual(len(DRUH_FOUR), 4)
        for root in DRUH_FOUR:
            got = at_the_end(root, before="jhal")
            self.assertEqual(got.sutra, "8.2.33", root)
            self.assertTrue(got.optional, root)

    def test_and_none_of_the_four_could_have_reached_8_2_32(self):
        # None begins with द्, so the option is between this
        # rule and 8.2.31, which the note says outright.
        self.assertIn("None of the four begins with",
                      provisions_for("8.2.33")[0].why)

    def test_nah_gives_dha_and_ah_gives_tha(self):
        # नद्धम्, उपानत्; इदम् आत्थ.
        self.assertEqual(
            at_the_end("nah", before="jhal").does, "dha")
        self.assertEqual(
            at_the_end("āh", before="jhal").does, "tha")

    def test_and_the_tha_is_chosen_to_keep_a_later_rule_out(self):
        # आदेशान्तरकरणं 8.2.40 इत्यस्य निवृत्त्यर्थम् — a ढ्
        # would have been turned into ध् by that rule.
        self.assertIn("8.2.40", provisions_for("8.2.35")[0].why)

    def test_and_a_varttika_gives_the_veda_a_fifth_sound(self):
        # हृग्रहोर् भश् छन्दसि हस्य.
        self.assertIn("भश् छन्दसि",
                      provisions_for("8.2.35")[0].why)


class TheRest(unittest.TestCase):
    """8.2.36–41."""

    def test_seven_roots_and_two_shapes_become_sa(self):
        # व्रष्टा, मूलवृट्, यष्टा, राट्.
        self.assertEqual(len(VRASCADI_EIGHT), 7)
        for root in VRASCADI_EIGHT:
            self.assertEqual(
                at_the_end(root, before="jhal").sutra, "8.2.36",
                root)
        self.assertEqual(
            at_the_end(gana="cha-śa-anta",
                       before="pada-anta").sutra, "8.2.36")

    def test_the_aspiration_moves_to_the_front_of_a_syllable(self):
        # बोद्धा — and the vṛtti counts four sounds replaced
        # against four replacing.
        got = at_the_end(gana="ekāc-jhaṣ-anta-baś", before="dhva")
        self.assertEqual(got.sutra, "8.2.37")
        self.assertEqual(got.does, "bhaṣ")
        self.assertIn("चत्वारो बशः",
                      provisions_for("8.2.37")[0].why)

    def test_and_dadh_does_it_before_four_more_sounds(self):
        # धत्तः, धत्थः, धत्से, धद्ध्वम्.
        for after in ("ta", "tha", "sa", "dhva"):
            got = at_the_end("dadh", before=after)
            self.assertEqual(got.sutra, "8.2.38", after)
        self.assertIn("8.2.40",
                      at_the_end("dadh", before="ta").blocked_by)

    def test_a_jhal_at_a_words_end_goes_voiced(self):
        # वागत्र, त्रिष्टुबत्र — and वस्ता is kept out.
        got = at_the_end(gana="jhal-anta", before="pada-anta")
        self.assertEqual(got.sutra, "8.2.39")
        self.assertEqual(got.does, "jaś")
        self.assertIn("वस्ता", provisions_for("8.2.39")[0].keeps_out)

    def test_and_a_t_after_a_jhas_becomes_dha(self):
        # लब्धा, दोग्धा, लेढा — दध् excepted by name.
        got = at_the_end(gana="jhaṣ", before="ta")
        self.assertEqual(got.sutra, "8.2.40")
        self.assertEqual(got.does, "dha")

    def test_and_sa_and_dha_become_ka_before_an_s(self):
        # पेक्ष्यति, लेक्ष्यति — the ढ् being 8.2.31's own.
        got = at_the_end(gana="ṣa-ḍha", before="sa")
        self.assertEqual(got.sutra, "8.2.41")
        self.assertEqual(got.does, "ka")
        self.assertIn("8.2.31", provisions_for("8.2.41")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A sound none of these rules reaches stands as it is."""

    def test_an_unnamed_sound_reaches_nothing(self):
        got = at_the_end(gana="ac-anta", before="ac")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(SAMYOGA_RUN, ("8.2.23", "8.2.41"))
        codes = [row.sutra for row in SAMYOGA_TABLE]
        self.assertEqual(
            codes, ["8.2.%d" % n for n in range(23, 42)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in SAMYOGA_TABLE:
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

    def test_the_rules_these_orderings_weigh_are_live(self):
        # 8.2.1's asiddhatva, 7.4.49's त्, and 7.3.97's option.
        for code in ("8.2.1", "7.4.49", "7.3.97"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_what_the_sounds_then_meet_has_landed(self):
        # 8.4.41 ष्टुना ष्टुः and 8.4.53 झलां जश् झशि take the
        # ढ् of सोढा and the ष् of मूलवृट् the rest of the way,
        # and both are codified — so a सūtra of this run that
        # gives an intermediate sound can be followed to the one
        # actually heard.
        self.assertTrue(REGISTRY.has("8.4.41"))
        self.assertTrue(REGISTRY.has("8.4.53"))


if __name__ == "__main__":
    unittest.main()
