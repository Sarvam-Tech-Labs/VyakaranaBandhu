# -*- coding: utf-8 -*-
"""
Tests for प्रगृह्य — 1.1.11 to 1.1.19.

Every worked form the Kāśikā gives across the nine sūtras is here, and so is
every counter-example it offers under a *kim* question. Those counter-examples
matter more than the positive cases: each marks a condition that could be
dropped without any positive example noticing, and one of them (प्राग्नये)
caught a real misreading of एकाच् in the first version of this codification.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.pragrhya import (
    IDUDED,
    IDUT,
    UM,
    blocks_sandhi,
    is_pragrhya,
    pragrhya,
)
from src.astadhyayi.varna import ANUNASIKA_MARK, is_anunasika


class Dvivacana(unittest.TestCase):
    """1.1.11 ईदूदेद्द्विवचनं प्रगृह्यम्."""

    def test_the_kasikas_duals(self):
        for form in ("agnī", "vāyū", "māle", "pacete", "pacethe"):
            found = pragrhya(form, dvivacana=True)
            self.assertIsNotNone(found, form)
            self.assertEqual(found.by, "1.1.11", form)

    def test_idudediti_kim_vrksavatra(self):
        """A dual in au is not among the three finals."""
        self.assertIsNone(pragrhya("vṛkṣau", dvivacana=True))

    def test_dvivacanamiti_kim_kumaryatra(self):
        """ī by itself is not enough — कुमार्यत्र, so कुमारी is not pragṛhya."""
        self.assertIsNone(pragrhya("kumārī"))
        self.assertIsNone(pragrhya("kiśorī"))

    def test_only_the_three_finals(self):
        self.assertEqual(IDUDED, ("ī", "ū", "e"))
        for final in ("a", "ā", "i", "u", "o", "ai", "au"):
            self.assertIsNone(pragrhya("k" + final, dvivacana=True), final)

    def test_the_finals_are_tapara_so_length_matters(self):
        """तपरकरणमसंदेहार्थम् — short i and u are not the same as ī and ū."""
        self.assertIsNone(pragrhya("agni", dvivacana=True))
        self.assertIsNotNone(pragrhya("agnī", dvivacana=True))


class Adas(unittest.TestCase):
    """1.1.12 अदसो मात्."""

    def test_ami_and_amu(self):
        for form in ("amī", "amū"):
            self.assertEqual(pragrhya(form, stem="adas").by, "1.1.12", form)

    def test_adasa_iti_kim(self):
        """अदस इति किम्? शम्यत्र। दाडिम्यत्र। Other stems in ī are untouched."""
        self.assertIsNone(pragrhya("śamī"))
        self.assertIsNone(pragrhya("dāḍimī"))

    def test_the_missing_e_example_is_a_gap_in_the_illustration(self):
        """
        एकारस्य नास्त्युदाहरणम् — the rule admits e, since ईदूदेत् comes down
        from 1.1.11, but no form of अदस् supplies one. The code admits it too.
        """
        self.assertIn("e", IDUDED)
        self.assertEqual(pragrhya("ame", stem="adas").by, "1.1.12")


class Se(unittest.TestCase):
    """1.1.13 शे."""

    def test_it_is_one_named_form(self):
        self.assertEqual(pragrhya("śe").by, "1.1.13")

    def test_nothing_else_is_reached_by_it(self):
        for form in ("se", "śa", "śī"):
            found = pragrhya(form)
            self.assertTrue(found is None or found.by != "1.1.13", form)


class EkacNipata(unittest.TestCase):
    """1.1.14 निपात एकाजनाङ् — the one that caught a misreading."""

    def test_the_bhasyas_single_vowel_particles(self):
        for form in ("a", "i", "u", "ā"):
            found = pragrhya(form, nipata=True)
            self.assertIsNotNone(found, form)
            self.assertEqual(found.by, "1.1.14", form)

    def test_ekajiti_kim_pragnaye(self):
        """
        प्राग्नये वाचमीरय. प्र has one vowel and is not one vowel; the Kāśikā
        glosses एकश्चासावच्चेत्येकाच्, so the particle must BE a single vowel.
        Reading it as "having one vowel" makes प्र pragṛhya and the sandhi in
        प्राग्नये impossible.
        """
        self.assertIsNone(pragrhya("pra", nipata=True))
        self.assertIsNone(pragrhya("ni", nipata=True))
        self.assertIsNone(pragrhya("vi", nipata=True))

    def test_anangiti_kim_odakantat(self):
        """आ उदकान्तात् gives ओदकान्तात् — आङ् is excluded."""
        self.assertIsNone(pragrhya("ā", nipata=True, ang=True))
        self.assertIsNotNone(pragrhya("ā", nipata=True, ang=False))

    def test_nipata_iti_kim_cakaratra(self):
        """चकारात्र, जहारात्र — not particles, so not reached."""
        self.assertIsNone(pragrhya("a"))
        self.assertIsNone(pragrhya("i"))


class OtNipata(unittest.TestCase):
    """1.1.15 ओत्."""

    def test_aho_and_utaho(self):
        for form in ("āho", "utāho"):
            self.assertEqual(pragrhya(form, nipata=True).by, "1.1.15", form)

    def test_it_is_ending_in_o_not_being_o(self):
        """तस्यौकारेण तदन्तविधिः — neither example is a bare o."""
        self.assertEqual(pragrhya("o", nipata=True).by, "1.1.14",
                         "a bare o is one vowel, so 1.1.14 takes it first")
        self.assertEqual(pragrhya("āho", nipata=True).by, "1.1.15")

    def test_nipata_carries_down_from_1_1_14(self):
        self.assertIsNone(pragrhya("āho"))


class Sakalya(unittest.TestCase):
    """1.1.16 and 1.1.17 — optional because an authority is named."""

    def test_the_vocative_before_iti(self):
        found = pragrhya("vāyo", sambuddhi=True, before_iti=True)
        self.assertEqual(found.by, "1.1.16")
        self.assertTrue(found.optional, "शाकल्यग्रहणं विभाषार्थम्")

    def test_all_four_conditions_are_required(self):
        base = dict(sambuddhi=True, before_iti=True)
        self.assertIsNotNone(pragrhya("vāyo", **base))
        # इताविति किम्? वायोऽत्र
        self.assertIsNone(pragrhya("vāyo", sambuddhi=True, before_iti=False))
        # सम्बुद्धाविति किम्? गवित्ययमाह
        self.assertIsNone(pragrhya("vāyo", before_iti=True))
        # अनार्षे — a Vedic passage is excluded
        self.assertIsNone(pragrhya("vāyo", arsa=True, **base))
        # and the final must be o
        self.assertIsNone(pragrhya("vāyā", **base))

    def test_the_particle_un(self):
        found = pragrhya("u", before_iti=True)
        self.assertEqual(found.by, "1.1.17")
        self.assertTrue(found.optional)

    def test_un_inherits_sakalya_from_1_1_16(self):
        """शाकल्यस्येति विभाषार्थम् — the optionality carries over."""
        self.assertIsNone(pragrhya("u", before_iti=True, arsa=True))

    def test_optionality_is_recorded_and_not_only_for_these(self):
        """
        The three optional rules are exactly 1.1.16, 1.1.17 and 1.1.18, and no
        others. A rule marked optional that should not be would licence a wrong
        form as freely as a right one.
        """
        optional = set()
        for form, ctx in [
            ("agnī", dict(dvivacana=True)),
            ("amī", dict(stem="adas")),
            ("śe", {}),
            ("a", dict(nipata=True)),
            ("āho", dict(nipata=True)),
            ("vāyo", dict(sambuddhi=True, before_iti=True)),
            ("u", dict(before_iti=True)),
            (UM, {}),
            ("māmakī", dict(saptami_artha=True)),
        ]:
            found = pragrhya(form, **ctx)
            if found and found.optional:
                optional.add(found.by)
        self.assertEqual(optional, {"1.1.16", "1.1.17", "1.1.18"})


class Um(unittest.TestCase):
    """1.1.18 ऊँ."""

    def test_the_form_is_a_long_nasalised_u(self):
        """दीर्घोऽनुनासिकश्च."""
        self.assertEqual(UM, "ū" + ANUNASIKA_MARK)
        self.assertTrue(is_anunasika(UM), "1.1.8 must recognise it")

    def test_it_is_pragrhya(self):
        self.assertEqual(pragrhya(UM).by, "1.1.18")

    def test_the_three_forms(self):
        """त्रीणि रूपाणि — उ इति, विति, ऊँ इति."""
        self.assertIsNotNone(pragrhya("u", before_iti=True))     # उ इति
        self.assertIsNotNone(pragrhya(UM))                       # ऊँ इति
        # विति is the third, and is what happens when neither applies
        self.assertIsNone(pragrhya("u", before_iti=True, arsa=True))

    def test_a_plain_long_u_is_not_it(self):
        self.assertIsNone(pragrhya("ū"))


class SaptamyArthe(unittest.TestCase):
    """1.1.19 ईदूतौ च सप्तम्यर्थे."""

    def test_the_vedic_locatives(self):
        for form in ("māmakī", "tanū", "gaurī"):
            self.assertEqual(
                pragrhya(form, saptami_artha=True).by, "1.1.19", form
            )

    def test_iduta_iti_kim_e_is_excluded(self):
        """
        Two finals, not three. This is why the sūtra says ईदूतौ where 1.1.11
        said ईदूदेत्.
        """
        self.assertEqual(IDUT, ("ī", "ū"))
        self.assertNotIn("e", IDUT)
        self.assertIsNone(pragrhya("agne", saptami_artha=True))

    def test_the_sakalya_anuvrtti_has_stopped(self):
        """
        शाकल्यस्येतावनार्षे इति निवृत्तम् — so this rule needs no इति, is not
        confined to non-Vedic, and is not optional.
        """
        found = pragrhya("māmakī", saptami_artha=True)
        self.assertFalse(found.optional)
        self.assertIsNotNone(pragrhya("māmakī", saptami_artha=True, arsa=True))


class TheSamjnaAsAWhole(unittest.TestCase):

    def test_nothing_is_pragrhya_without_a_condition(self):
        """
        Every one of the nine needs something the string cannot supply. A form
        with no context given must not acquire the name by accident.
        """
        for form in ("agnī", "vāyū", "māle", "amī", "vāyo", "māmakī", "āho"):
            self.assertFalse(is_pragrhya(form), form)

    def test_the_exceptions_that_need_no_context(self):
        """Two forms are named outright and carry the name by themselves."""
        self.assertTrue(is_pragrhya("śe"))
        self.assertTrue(is_pragrhya(UM))

    def test_blocks_sandhi_reports_the_condition_and_not_the_rule(self):
        """
        6.1.125 is what protects the vowel and is not codified. The helper is
        named so that a caller cannot read it as having applied that rule.
        """
        self.assertTrue(blocks_sandhi("agnī", dvivacana=True))
        self.assertFalse(blocks_sandhi("agni", dvivacana=True))

    def test_every_sutra_of_the_block_is_reachable(self):
        reached = set()
        for form, ctx in [
            ("agnī", dict(dvivacana=True)), ("amī", dict(stem="adas")),
            ("śe", {}), ("a", dict(nipata=True)), ("āho", dict(nipata=True)),
            ("vāyo", dict(sambuddhi=True, before_iti=True)),
            ("u", dict(before_iti=True)), (UM, {}),
            ("māmakī", dict(saptami_artha=True)),
        ]:
            found = pragrhya(form, **ctx)
            self.assertIsNotNone(found, form)
            reached.add(found.by)
        self.assertEqual(reached, {f"1.1.{n}" for n in range(11, 20)})


class Registration(unittest.TestCase):
    IDS = tuple(f"1.1.{n}" for n in range(11, 20))

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_the_opening_nineteen_are_continuous(self):
        for number in range(1, 20):
            self.assertTrue(
                self.registry.has(f"1.1.{number}"), f"1.1.{number} missing"
            )

    def test_the_pragrhya_anuvrtti_runs_through_the_block(self):
        for sutra_id in self.IDS[1:]:
            carried = " ".join(self.registry.get(sutra_id).anuvrtti)
            self.assertIn("1.1.11", carried, sutra_id)

    def test_1_1_14_records_the_misreading_it_corrects(self):
        notes = self.registry.get("1.1.14").notes
        self.assertIn("एकश्चासावच्चेत्येकाच्", notes)
        self.assertIn("प्राग्नये", notes)

    def test_the_samjna_is_registered_once(self):
        from src.astadhyayi.grahana import samjna_source
        self.assertEqual(samjna_source("pragṛhya"), "1.1.11")


if __name__ == "__main__":
    unittest.main()
