# -*- coding: utf-8 -*-
"""
Tests for 1.1.60 to 1.1.67 — disappearance, parts of a form, and case-reading.

The centrepiece is `nirdesa`. With 1.1.49, 1.1.66 and 1.1.67 codified, a sūtra's
own case marking says where its operation falls, and 6.1.77 इको यणचि can be read
out of the corpus without being told anything: इकः sixth, so it is what gets
replaced; अचि seventh, so the substitution falls on what precedes the aC. That
is the traditional analysis of the rule, arrived at from the text.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.adesa import (
    PANCAMI,
    SAPTAMI,
    SASTHI,
    Side,
    nirdesa,
    operates_on,
    saptami_padas,
    ti,
    upadha,
)
from src.astadhyayi.lopa import (
    Elision,
    LUMAT,
    adarsana,
    is_lumat,
    names_of_affix_elision,
    pratyaya_laksana,
)
from src.astadhyayi.sources import all_sutra_ids, facts


class Adarsana(unittest.TestCase):
    """1.1.60 अदर्शनं लोपः."""

    def test_an_empty_slot_is_a_lopa(self):
        self.assertTrue(adarsana(None))
        self.assertTrue(adarsana(""))

    def test_something_present_is_not(self):
        self.assertFalse(adarsana("a"))
        self.assertFalse(adarsana("kta"))


class AffixElision(unittest.TestCase):
    """1.1.61 प्रत्ययस्य लुक्श्लुलुपः."""

    def test_the_three_names(self):
        self.assertEqual(
            names_of_affix_elision(),
            frozenset({Elision.LUK, Elision.SLU, Elision.LUP}),
        )

    def test_they_are_distinct_and_not_aliases(self):
        """
        अनेकसंज्ञाविधानाच् च तद्भावितग्रहणमिह विज्ञायते ... तेन संज्ञानां संकरो
        न भवति — each name reaches only the elision it itself prescribed. If
        these were aliases, 1.1.63 could not be stated.
        """
        self.assertEqual(len({e.value for e in Elision}), 4)
        self.assertNotEqual(Elision.LUK, Elision.SLU)
        self.assertNotEqual(Elision.SLU, Elision.LUP)

    def test_a_plain_lopa_is_not_one_of_them(self):
        self.assertNotIn(Elision.LOPA, names_of_affix_elision())


class PratyayaLaksana(unittest.TestCase):
    """1.1.62 with 1.1.63."""

    def test_the_conditioning_survives_an_ordinary_elision(self):
        """अग्निचित्, सोमसुत् — still pada by 1.4.14 though the sup is gone."""
        result = pratyaya_laksana(Elision.LOPA)
        self.assertTrue(result.survives)
        self.assertEqual(result.by, "1.1.62")

    def test_lumata_and_anga_together_defeat_it(self):
        """गर्गाः, मृष्टः, जुहुतः — no guṇa or vṛddhi for the aṅga."""
        for elision in (Elision.LUK, Elision.SLU, Elision.LUP):
            result = pratyaya_laksana(elision, anga=True)
            self.assertFalse(result.survives, elision)
            self.assertEqual(result.by, "1.1.63", elision)

    def test_lumateti_kim_karyate(self):
        """
        लुमतेति किम्? कार्यते। हार्यते। An ordinary lopa on the aṅga: 1.1.63
        does not reach it, so the conditioning stands.
        """
        result = pratyaya_laksana(Elision.LOPA, anga=True)
        self.assertTrue(result.survives)
        self.assertEqual(result.by, "1.1.62")

    def test_angasyeti_kim_panca(self):
        """
        अङ्गस्येति किम्? पञ्च। सप्त। पयः। साम। Not an operation on the aṅga,
        so a lu-word elision does not stop it either.
        """
        for elision in (Elision.LUK, Elision.SLU, Elision.LUP):
            result = pratyaya_laksana(elision, anga=False)
            self.assertTrue(result.survives, elision)
            self.assertEqual(result.by, "1.1.62", elision)

    def test_both_restrictions_are_needed(self):
        """Neither alone suffices; only the two together block."""
        blocked = [
            (e, a)
            for e in Elision
            for a in (True, False)
            if not pratyaya_laksana(e, anga=a).survives
        ]
        self.assertEqual(
            sorted((e.value, a) for e, a in blocked),
            [("luk", True), ("lup", True), ("ślu", True)],
        )

    def test_lumat_is_derived_from_the_names_not_listed_again(self):
        for elision in Elision:
            self.assertEqual(
                is_lumat(elision), "lu" in elision.value, elision
            )
        self.assertEqual(LUMAT, names_of_affix_elision())


class Ti(unittest.TestCase):
    """1.1.64 अचोऽन्त्यादि टि."""

    def test_the_kasikas_examples(self):
        self.assertEqual(ti("agnicit"), "it")
        self.assertEqual(ti("somasut"), "ut")
        self.assertEqual(ti("ātām"), "ām")
        self.assertEqual(ti("āthām"), "ām")

    def test_it_is_the_vowel_and_what_follows_not_the_vowel_alone(self):
        """तदादि शब्दरूपम् — इत् and not इ."""
        self.assertEqual(ti("agnicit"), "it")
        self.assertNotEqual(ti("agnicit"), "i")

    def test_a_final_vowel_gives_just_that_vowel(self):
        self.assertEqual(ti("pace"), "e")
        self.assertEqual(ti("rāma"), "a")

    def test_a_diphthong_counts_as_one_vowel(self):
        self.assertEqual(ti("gau"), "au")
        self.assertEqual(ti("nai"), "ai")

    def test_a_form_with_no_vowel_has_no_ti(self):
        self.assertEqual(ti("k"), "")
        self.assertEqual(ti(""), "")


class Upadha(unittest.TestCase):
    """1.1.65 अलोऽन्त्यात् पूर्व उपधा."""

    def test_the_kasikas_roots(self):
        for root, expected in [("pac", "a"), ("paṭh", "a"), ("bhid", "i"),
                               ("chid", "i"), ("budh", "u"), ("yudh", "u"),
                               ("vṛt", "ṛ"), ("vṛdh", "ṛ")]:
            self.assertEqual(upadha(root), expected, root)

    def test_it_is_one_sound_and_not_everything_before_the_last(self):
        """अल इति किम्? समुदायात् पूर्वस्य मा भूत्."""
        self.assertEqual(upadha("bhid"), "i")
        self.assertEqual(len(upadha("bhid")), 1)
        self.assertEqual(upadha("somasut"), "u")

    def test_a_digraph_counts_as_one_sound(self):
        self.assertEqual(upadha("labh"), "a")
        self.assertEqual(upadha("paṭh"), "a")

    def test_a_form_of_one_sound_has_no_upadha(self):
        self.assertIsNone(upadha("a"))
        self.assertIsNone(upadha("k"))
        self.assertIsNone(upadha(""))

    def test_ti_and_upadha_do_not_overlap_for_a_consonant_final_root(self):
        """
        For पच् the ṭi is अच् and the upadhā is अ — the upadhā is inside the
        ṭi here, which is fine: they are different names for different
        purposes, not a partition.
        """
        self.assertEqual(ti("pac"), "ac")
        self.assertEqual(upadha("pac"), "a")


class ReadingACase(unittest.TestCase):
    """1.1.49, 1.1.66 and 1.1.67 as one reading of a sūtra."""

    def test_iko_yanaci_reads_itself(self):
        """
        6.1.77 इको यणचि. Two cases, two paribhāṣās, and between them the whole
        analysis: इकः is what is replaced, and the operation falls on what
        precedes the aC. दधि + उदकम् gives दध्युदकम्.
        """
        reading = {item.word: (item.side, item.by) for item in nirdesa("6.1.77")}
        self.assertEqual(reading["इकः"], (Side.IN_PLACE_OF, "1.1.49"))
        self.assertEqual(reading["अचि"], (Side.PRECEDING, "1.1.66"))

    def test_tin_atinah_reads_itself(self):
        """8.1.28 तिङ्ङतिङः — अतिङः is fifth, so the tiṅ that FOLLOWS."""
        reading = {item.word: (item.side, item.by) for item in nirdesa("8.1.28")}
        self.assertEqual(reading["अतिङः"], (Side.FOLLOWING, "1.1.67"))

    def test_the_three_cases_map_to_three_distinct_sides(self):
        sides = {SASTHI: Side.IN_PLACE_OF, SAPTAMI: Side.PRECEDING,
                 PANCAMI: Side.FOLLOWING}
        self.assertEqual(len(set(sides.values())), 3)

    def test_only_the_three_cases_are_read(self):
        """
        A first-case or instrumental word is not addressed by any of the three
        paribhāṣās and must not be assigned a side.
        """
        for sutra_id in ("1.1.1", "1.1.9", "1.1.63"):
            for item in nirdesa(sutra_id):
                self.assertIn(item.vibhakti, (SASTHI, SAPTAMI, PANCAMI),
                              f"{sutra_id} {item.word}")

    def test_it_runs_over_the_whole_text(self):
        """
        Worth having only if it works on all 3,983 sūtras. Every word it
        reports must be a pada of that sūtra, and every side must have a rule.
        """
        seen = {side: 0 for side in Side}
        for sutra_id in all_sutra_ids():
            words = {p.word for p in facts(sutra_id).padas}
            for item in nirdesa(sutra_id):
                self.assertIn(item.word, words, sutra_id)
                self.assertTrue(item.by.startswith("1.1."), sutra_id)
                seen[item.side] += 1
        # The three unconditional readings all occur in quantity.
        for side in (Side.IN_PLACE_OF, Side.PRECEDING, Side.FOLLOWING):
            self.assertGreater(seen[side], 100, f"{side} barely occurs")
        # The fourth does not, and must not: 1.2.43 reads the first case only
        # in a rule that makes a compound — समास इति समासविधायि शास्त्रं
        # गृह्यते — so a bare sweep never produces it.
        self.assertEqual(seen[Side.UPASARJANA], 0)

    def test_the_fourth_reading_needs_to_be_asked_for(self):
        """
        1.2.43 is the only one of the four that is conditioned. 2.1.24 is a
        compound rule and its द्वितीया is the upasarjana; without the flag the
        same sūtra yields nothing, because a first-case word elsewhere is not
        one.
        """
        asked = nirdesa("2.1.24", samasa_vidhi=True)
        self.assertEqual(
            [(n.word, n.side, n.by) for n in asked],
            [("द्वितीया", Side.UPASARJANA, "1.2.43")],
        )
        self.assertEqual(nirdesa("2.1.24"), ())

    def test_saptami_padas_agrees_with_nirdesa(self):
        for sutra_id in ("6.1.77", "1.1.4", "1.1.62", "6.3.25"):
            from_nirdesa = tuple(
                item.word for item in nirdesa(sutra_id)
                if item.side is Side.PRECEDING
            )
            self.assertEqual(saptami_padas(sutra_id), from_nirdesa, sutra_id)

    def test_operates_on_reports_the_sides_in_order(self):
        self.assertEqual(
            operates_on("6.1.77"), (Side.IN_PLACE_OF, Side.PRECEDING)
        )
        self.assertEqual(operates_on("8.1.28"), (Side.FOLLOWING,))


class Registration(unittest.TestCase):
    IDS = tuple(f"1.1.{n}" for n in range(60, 68))

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_the_run_to_1_1_71_is_continuous(self):
        for number in range(60, 72):
            self.assertTrue(
                self.registry.has(f"1.1.{number}"), f"1.1.{number} missing"
            )

    def test_1_1_64_records_that_its_sasthi_is_not_1_1_49s(self):
        """
        अच इति निर्धारणे षष्ठी — a genitive of selection, not of substitution.
        The one exception so far to 1.1.49, and it has to be findable or a
        reader will apply the wrong paribhāṣā.
        """
        notes = self.registry.get("1.1.64").notes
        self.assertIn("निर्धारणे", notes)
        self.assertIn("1.1.49", notes)

    def test_1_1_66_records_the_adjacency_it_does_not_implement(self):
        notes = self.registry.get("1.1.66").notes
        self.assertIn("निर्दिष्टग्रहणमानन्तर्यार्थम्", notes)

    def test_the_new_samjnas_are_registered(self):
        from src.astadhyayi.grahana import samjna_source

        self.assertEqual(samjna_source("lopa"), "1.1.60")
        self.assertEqual(samjna_source("ṭi"), "1.1.64")
        self.assertEqual(samjna_source("upadhā"), "1.1.65")


if __name__ == "__main__":
    unittest.main()
