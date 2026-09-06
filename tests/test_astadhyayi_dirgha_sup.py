# -*- coding: utf-8 -*-
"""
७.३.१०१–१२० — the अ lengthened, and the case ending's augments.

The pāda ends where a noun's declension does, so the tests walk
it: the अ-final stem's own vowel, the four rules the vocative
gets, and then five augments to the ending — the last five sūtras
of the pāda all answering for one ङि.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.dirgha_sup import (
    AMBA_NADI,
    AUGMENTS_FROM,
    CODIFIED_APART,
    DIRGHA_RUN,
    DIRGHA_TABLE,
    NGI_FIVE,
    before_ending,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


def _n(code):
    return int(code.rsplit(".", 1)[1])


class TheAFinalStemsOwnVowel(unittest.TestCase):
    """7.3.101–104."""

    def test_it_lengthens_before_a_y_or_nasal_sarvadhatuka(self):
        # पचामि, पचावः, पचामः.
        got = before_ending(gana="a-anta",
                            before="yañ-ādi-sārvadhātuka")
        self.assertEqual(got.sutra, "7.3.101")
        self.assertEqual(got.does, "dīrgha")

    def test_and_before_such_a_case_ending(self):
        # वृक्षाय, वृक्षाभ्याम् — the lengthening 7.1.13's ङेर्यः
        # needed and could not state.
        got = before_ending(gana="a-anta", before="yañ-ādi-sup")
        self.assertEqual(got.sutra, "7.3.102")
        self.assertTrue(REGISTRY.has("7.1.13"))

    def test_but_becomes_e_before_a_jhal_initial_plural(self):
        # वृक्षेभ्यः, वृक्षेषु.
        got = before_ending(gana="a-anta",
                            before="jhal-ādi-bahuvacana-sup")
        self.assertEqual(got.sutra, "7.3.103")
        self.assertEqual(got.does, "et")
        self.assertIn("7.3.102", got.blocked_by)

    def test_and_before_os(self):
        # वृक्षयोः स्वम्.
        self.assertEqual(
            before_ending(gana="a-anta", before="os").sutra,
            "7.3.104")


class TheVocativesFourRules(unittest.TestCase):
    """7.3.105–108, and the argument at the end of them."""

    def test_an_ap_final_stem_becomes_e(self):
        # हे खट्वे, हे बहुराजे.
        got = before_ending(gana="āp-anta", before="sambuddhi")
        self.assertEqual(got.sutra, "7.3.106")
        self.assertEqual(got.does, "et")

    def test_two_classes_shorten_instead(self):
        # हे अम्ब; हे कुमारि, हे ब्रह्मबन्धु.
        self.assertEqual(AMBA_NADI, ("ambā-artha", "nadī-anta"))
        got = before_ending(gana="ambā-artha-nadī",
                            before="sambuddhi")
        self.assertEqual(got.sutra, "7.3.107")
        self.assertEqual(got.does, "hrasva")

    def test_and_a_short_final_stem_takes_guna(self):
        # हे अग्ने, हे वायो, हे पटो.
        got = before_ending(gana="hrasva-anta",
                            before="sambuddhi")
        self.assertEqual(got.sutra, "7.3.108")
        self.assertEqual(got.does, "guṇa")
        self.assertIn("7.3.107", got.blocked_by)

    def test_the_guna_cannot_reach_the_stems_just_shortened(self):
        # ह्रस्वविधानसामर्थ्याद् गुणो न भवति — the shortening
        # would be pointless if the guṇa followed it. And the
        # vṛtti proves it from how Pāṇini would have written the
        # pair otherwise.
        why = provisions_for("7.3.108")[0].why
        self.assertIn("ह्रस्वविधानसामर्थ्याद्", why)
        self.assertIn("ब्रूयात्", why)

    def test_a_short_final_stem_takes_guna_before_jas_too(self):
        # अग्नयः, वायवः, धेनवः.
        self.assertEqual(
            before_ending(gana="hrasva-anta", before="jas").sutra,
            "7.3.109")

    def test_and_the_veda_is_let_off_from_here_on(self):
        # इतः प्रकरणात् प्रभृति छन्दसि वेति वक्तव्यम् — which is
        # how अम्बे stands beside अम्ब and शतक्रत्वः beside
        # शतक्रतवः.
        self.assertIn("इतः प्रकरणात्",
                      provisions_for("7.3.109")[0].why)


class TheStemsThatTakeGuna(unittest.TestCase):
    """7.3.110–111."""

    def test_an_r_final_stem_before_ni_and_a_strong_ending(self):
        # मातरि, पितरि; कर्तारौ, कर्तारः.
        for affix in ("ṅi", "sarvanāmasthāna"):
            self.assertEqual(
                before_ending(gana="ṛ-anta", before=affix).sutra,
                "7.3.110", affix)

    def test_and_a_ghi_stem_before_a_nit_ending(self):
        # अग्नये, वायवे, अग्नेः स्वम्.
        got = before_ending(gana="ghi", before="ṅit")
        self.assertEqual(got.sutra, "7.3.111")
        self.assertEqual(got.does, "guṇa")


class TheAugmentsToTheEnding(unittest.TestCase):
    """7.3.112–115, where the run stops being about the stem."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(AUGMENTS_FROM, "7.3.112")

    def test_everything_from_there_to_the_stya_supplies_an_augment(self):
        for row in DIRGHA_TABLE:
            if _n(AUGMENTS_FROM) <= _n(row.sutra) <= _n("7.3.115"):
                self.assertTrue(row.augment, row.sutra)

    def test_a_nadi_stem_gives_the_ending_an_at(self):
        # कुमार्यै, ब्रह्मबन्ध्वै.
        got = before_ending(gana="nadī-anta", before="ṅit")
        self.assertEqual(got.sutra, "7.3.112")
        self.assertEqual(got.does, "āṭ")

    def test_an_ap_stem_a_yat(self):
        # खट्वायै, बहुराजायै.
        got = before_ending(gana="āp-anta", before="ṅit")
        self.assertEqual(got.sutra, "7.3.113")
        self.assertEqual(got.does, "yāṭ")

    def test_and_a_pronoun_a_syat_with_the_stem_shortened(self):
        # सर्वस्यै, यस्यै, कस्यै — two operations in one sūtra.
        got = before_ending(gana="sarvanāma-āp", before="ṅit")
        self.assertEqual(got.sutra, "7.3.114")
        self.assertEqual(got.does, "syāṭ")
        self.assertTrue(got.also_shortens)
        self.assertIn("7.3.113", got.blocked_by)

    def test_two_words_make_that_optional(self):
        # द्वितीयस्यै beside द्वितीयायै.
        for stem in ("dvitīya", "tṛtīya"):
            got = before_ending(stem, before="ṅit")
            self.assertEqual(got.sutra, "7.3.115", stem)
            self.assertTrue(got.optional, stem)
            self.assertTrue(got.also_shortens, stem)


class FiveAnswersForOneNgi(unittest.TestCase):
    """7.3.116–120, the last five sūtras of the pāda."""

    def test_each_stem_gets_its_own_answer(self):
        # कुमार्याम्, कृत्याम्, सख्यौ, अग्नौ, अग्निना.
        self.assertEqual(len(NGI_FIVE), 5)
        wanted = {
            ("nadī-āp-nī", "ṅi", ""): ("7.3.116", "ām"),
            ("id-ud-nadī", "ṅi", ""): ("7.3.117", "ām"),
            ("id-ud", "ṅi", ""): ("7.3.118", "au"),
            ("ghi", "ṅi", ""): ("7.3.119", "au-ac"),
            ("ghi", "āṅ", "a-strī"): ("7.3.120", "nā"),
        }
        for (gana, affix, gender), (code, does) in wanted.items():
            got = before_ending(gana=gana, before=affix,
                                gender=gender)
            self.assertEqual(got.sutra, code, gana)
            self.assertEqual(got.does, does, gana)

    def test_the_ghi_rule_also_changes_the_stems_own_vowel(self):
        # अग्नौ, वायौ — the ङि becomes औ AND the घि's vowel अ.
        got = before_ending(gana="ghi", before="ṅi")
        self.assertTrue(got.also_shortens)
        self.assertIn("7.3.118", got.blocked_by)

    def test_and_some_read_the_last_two_as_one_rule(self):
        # औदच्च घेरिति येषामेकमेवेदं सूत्रम् — and then the औ is
        # the main provision and the अ an afterthought.
        self.assertIn("एकम् एवेदं",
                      provisions_for("7.3.119")[0].why)

    def test_the_last_sutra_says_not_feminine_and_not_masculine(self):
        # पुंसि इति नोक्तम् — अमुना ब्राह्मणकुलेन, a neuter
        # needing the rule too. कृत्या and धेन्वा are out.
        self.assertEqual(provisions_for("7.3.120")[0].gender,
                         "a-strī")
        self.assertIn("पुंसि इति नोक्तम्",
                      provisions_for("7.3.120")[0].why)
        self.assertNotEqual(
            before_ending(gana="ghi", before="āṅ",
                          gender="strī").sutra, "7.3.120")


class NothingHappensByDefault(unittest.TestCase):
    """राजभिः takes nothing from this run."""

    def test_an_unnamed_stem_reaches_nothing(self):
        got = before_ending(gana="n-anta", before="bhis")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry, and the pāda is closed."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(DIRGHA_RUN, ("7.3.101", "7.3.120"))
        codes = [row.sutra for row in DIRGHA_TABLE]
        self.assertEqual(
            codes, ["7.3.%d" % n for n in range(101, 121)])

    def test_one_sutra_of_the_run_was_codified_long_before(self):
        # 7.3.101 अतो दीर्घो यञि was registered while पाद ७.३ was
        # a stub, and a patch that splices ahead of it must not
        # disturb it.
        self.assertEqual(CODIFIED_APART, ("7.3.101",))
        self.assertTrue(REGISTRY.has("7.3.101"))
        self.assertGreater(len(REGISTRY.get("7.3.101").notes), 200)

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in DIRGHA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_pada_seven_three_is_complete(self):
        for n in range(1, 121):
            self.assertTrue(REGISTRY.has("7.3.%d" % n), n)
        self.assertFalse(REGISTRY.has("7.3.121"))


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_names_this_run_leans_on_are_live(self):
        # 1.4.3's नदी, 1.4.7's घि, 1.1.27's सर्वनामन् and
        # 4.1.4's आप् are the four classes every rule of
        # 7.3.105–120 turns on. All codified.
        for code in ("1.4.3", "1.4.7", "1.1.27", "4.1.4"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_last_pada_of_the_adhyaya_has_been_read(self):
        # Written as a debt: neither end of पाद ७.४ was codified.
        # Both have landed. 7.4.1 opens the pāda and 7.4.97 is
        # where 6.4.1's अङ्गस्य heading finally ends, four pādas
        # after it was opened — the longest heading in the book,
        # and it can be asked end to end now.
        self.assertTrue(REGISTRY.has("7.4.1"))
        self.assertTrue(REGISTRY.has("7.4.97"))


if __name__ == "__main__":
    unittest.main()
