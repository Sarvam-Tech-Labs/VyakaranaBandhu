# -*- coding: utf-8 -*-
"""
Tests for the Aṣṭādhyāyī codification.

The śivasūtra tests are the important ones: they check that every standard
pratyāhāra falls out of the fourteen sūtras by 1.1.71 with its traditional
membership and count. Because those values are fixed by the system rather than
by any editor's opinion, this layer is verifiable without consulting a book —
which is why the rest is built on top of it.
"""

import unittest

from src.astadhyayi.sivasutra import (
    SIVASUTRAS,
    SOUND_ORDER,
    PratyaharaError,
    denotes,
    is_ambiguous,
    resolve,
    resolve_all,
    sounds,
)
from src.astadhyayi.sutra import (
    REGISTRY,
    Reading,
    Source,
    Status,
    SutraId,
    SutraType,
)
from src.astadhyayi.rules.adhyaya_1_pada_1 import VRDDHI, is_vrddhi


class TestSivasutras(unittest.TestCase):
    def test_there_are_fourteen(self):
        self.assertEqual(len(SIVASUTRAS), 14)
        self.assertEqual([s.number for s in SIVASUTRAS], list(range(1, 15)))

    def test_the_akshara_samamnaya_lists_the_expected_sounds(self):
        # 43 slots because ha is listed twice; 42 distinct varṇas.
        self.assertEqual(len(SOUND_ORDER), 43)
        self.assertEqual(len(set(SOUND_ORDER)), 42)
        self.assertEqual(SOUND_ORDER[:3], ("a", "i", "u"))
        self.assertEqual(SOUND_ORDER[-1], "h")

    def test_it_markers(self):
        self.assertEqual(
            [s.it for s in SIVASUTRAS],
            ["ṇ", "k", "ṅ", "c", "ṭ", "ṇ", "m", "ñ", "ṣ", "ś", "v", "y", "r", "l"],
        )


class TestPratyaharaDerivation(unittest.TestCase):
    """Every standard pratyāhāra, derived and checked against its known value."""

    def test_vowel_pratyaharas(self):
        self.assertEqual(sounds("aC"), ("a", "i", "u", "ṛ", "ḷ", "e", "o", "ai", "au"))
        self.assertEqual(sounds("iK"), ("i", "u", "ṛ", "ḷ"))
        self.assertEqual(sounds("aK"), ("a", "i", "u", "ṛ", "ḷ"))
        self.assertEqual(sounds("eṄ"), ("e", "o"))
        self.assertEqual(sounds("aiC"), ("ai", "au"))
        self.assertEqual(sounds("eC"), ("e", "o", "ai", "au"))

    def test_consonant_pratyaharas(self):
        self.assertEqual(sounds("śaL"), ("ś", "ṣ", "s", "h"))
        self.assertEqual(sounds("jaŚ"), ("j", "b", "g", "ḍ", "d"))
        self.assertEqual(sounds("yaṆ"), ("y", "v", "r", "l"))
        self.assertEqual(sounds("ñaM"), ("ñ", "m", "ṅ", "ṇ", "n"))
        self.assertEqual(sounds("yaM"), ("y", "v", "r", "l", "ñ", "m", "ṅ", "ṇ", "n"))
        self.assertEqual(
            sounds("khaY"), ("kh", "ph", "ch", "ṭh", "th", "c", "ṭ", "t", "k", "p")
        )

    def test_traditional_counts(self):
        # aL = every varṇa (42); haL = every consonant (33); vaL = every
        # consonant but y (32); jhaL = the stops, sibilants and h (24).
        self.assertEqual(len(resolve("aL")), 42)
        self.assertEqual(len(resolve("haL")), 33)
        self.assertEqual(len(resolve("vaL")), 32)
        self.assertEqual(len(resolve("jhaL")), 24)
        self.assertEqual(len(resolve("aC")), 9)

    def test_ha_is_counted_once_though_listed_twice(self):
        # Śivasūtra 14 repeats ha so that pratyāhāras closing in L reach it.
        # It is the same sound, so it must not be double-counted.
        self.assertEqual(resolve("haL").sounds.count("h"), 1)
        self.assertEqual(resolve("aL").sounds.count("h"), 1)

    def test_val_excludes_ya_but_includes_ha(self):
        self.assertNotIn("y", resolve("vaL").sounds)
        self.assertIn("h", resolve("vaL").sounds)

    def test_an_is_reported_ambiguous_not_silently_chosen(self):
        # Ṇ closes both śivasūtra 1 and 6, so aṆ has two readings.
        self.assertTrue(is_ambiguous("aṆ"))
        readings = resolve_all("aṆ")
        self.assertEqual(len(readings), 2)
        self.assertEqual(readings[0].sounds, ("a", "i", "u"))       # 1.1.69's reading
        self.assertEqual(readings[1].to_sutra, 6)
        # The wider reading runs to the Ṇ of śivasūtra 6: the nine vowels plus
        # h, y, v, r, l.
        self.assertEqual(
            readings[1].sounds,
            ("a", "i", "u", "ṛ", "ḷ", "e", "o", "ai", "au", "h", "y", "v", "r", "l"),
        )

    def test_unambiguous_pratyaharas_have_one_reading(self):
        for name in ("aC", "iK", "aiC", "haL", "śaL", "jhaL"):
            self.assertFalse(is_ambiguous(name), name)

    def test_derivation_records_its_provenance(self):
        aic = resolve("aiC")
        self.assertEqual(aic.from_sutra, 4)
        self.assertEqual(aic.to_sutra, 4)
        hal = resolve("haL")
        self.assertEqual(hal.from_sutra, 5)   # the ha of śivasūtra 5, not 14
        self.assertEqual(hal.to_sutra, 14)

    def test_membership(self):
        self.assertTrue(denotes("aC", "ai"))
        self.assertFalse(denotes("aC", "k"))
        self.assertTrue(denotes("haL", "k"))
        self.assertFalse(denotes("haL", "a"))

    def test_rejects_impossible_pratyaharas(self):
        with self.assertRaises(PratyaharaError):
            resolve("zZ")           # no such initial
        with self.assertRaises(PratyaharaError):
            resolve("aQ")           # not an it-marker
        with self.assertRaises(PratyaharaError):
            resolve("a")            # too short


class TestSutraId(unittest.TestCase):
    def test_parse_and_render(self):
        self.assertEqual(str(SutraId.parse("1.1.1")), "1.1.1")
        self.assertEqual(SutraId.parse("6.4.22").sort_key, (6, 4, 22))

    def test_rejects_out_of_range(self):
        for bad in ("9.1.1", "1.5.1", "1.1.0", "1.1"):
            with self.assertRaises(ValueError, msg=bad):
                SutraId.parse(bad)

    def test_tripadi_boundary(self):
        # The tripādī begins at 8.2.1; its rules are asiddha to what precedes.
        self.assertFalse(SutraId.parse("8.1.1").in_tripadi)
        self.assertTrue(SutraId.parse("8.2.1").in_tripadi)
        self.assertTrue(SutraId.parse("8.4.68").in_tripadi)


class TestSourceDiscipline(unittest.TestCase):
    """The schema must make an unattributed claim impossible to record."""

    def test_verified_reading_requires_a_locator(self):
        with self.assertRaises(ValueError):
            Reading(source=Source.KATRE, status=Status.VERIFIED, text="…")

    def test_pending_reading_must_stay_empty(self):
        with self.assertRaises(ValueError):
            Reading(
                source=Source.SHARMA,
                status=Status.PENDING,
                note="what Sharma probably says",
            )

    def test_pending_slot_is_allowed_when_empty(self):
        r = Reading(source=Source.SHARMA, status=Status.PENDING, locator="vol. 2")
        self.assertEqual(r.status, Status.PENDING)


class TestSutra111(unittest.TestCase):
    def test_registered(self):
        self.assertIn("1.1.1", REGISTRY)
        sutra = REGISTRY.get("1.1.1")
        self.assertEqual(sutra.devanagari, "वृद्धिरादैच्")
        self.assertEqual(sutra.type, SutraType.SAMJNA)

    def test_vrddhi_is_a_ai_au(self):
        self.assertEqual(VRDDHI, ("ā", "ai", "au"))

    def test_the_definition_is_derived_from_the_sivasutras(self):
        # If 1.1.71 or the śivasūtras changed, this must change with them —
        # the point of deriving rather than hardcoding.
        self.assertEqual(VRDDHI[1:], resolve("aiC").sounds)

    def test_is_vrddhi(self):
        for sound in ("ā", "ai", "au"):
            self.assertTrue(is_vrddhi(sound), sound)
        for sound in ("a", "i", "e", "o", "ī", "ū", "k"):
            self.assertFalse(is_vrddhi(sound), sound)

    def test_guna_sounds_are_not_vrddhi(self):
        # 1.1.2 adeṅ guṇaḥ names a, e, o guṇa — disjoint from vṛddhi.
        for sound in ("a", "e", "o"):
            self.assertFalse(is_vrddhi(sound), sound)

    def test_coverage_reports_what_is_still_unread(self):
        coverage = REGISTRY.get("1.1.1").coverage()
        # Read: the sūtra text (two witnesses) and the Mahābhāṣya, both of
        # which are in reference/ with locators.
        for source in ("mūla", "mahabhasya", "kasika", "vasu"):
            self.assertIn(source, coverage["verified"], source)
        # Still outstanding: the works that need the printed books.
        for source in ("sharma", "joshi_roodbergen", "abhyankar_shukla"):
            self.assertIn(source, coverage["pending"], source)
        # Katre is a third case and must not be confused with either. The
        # volume is downloaded; its OCR destroyed the English, and the
        # archive.org item has no better text derivative. So it is not waiting
        # for a reader, it is waiting for a legible copy — and the record has
        # to say which, or someone will go looking for it again.
        self.assertIn("katre", coverage["unreadable"])
        self.assertNotIn("katre", coverage.get("pending", []))
        katre = REGISTRY.get("1.1.1").reading(Source.KATRE)
        self.assertTrue(katre.note, "an unreadable slot must explain itself")
        self.assertFalse(katre.text, "and cannot pretend to a quotation")
        # Benson's Kārakāhnika covers 1.4.23–55 and never reaches 1.1.1.
        self.assertIn("benson", coverage["absent"])

    def test_the_rule_is_executable(self):
        sutra = REGISTRY.get("1.1.1")
        self.assertTrue(sutra.is_codified)
        self.assertTrue(sutra.apply("ai"))
        self.assertFalse(sutra.apply("i"))


if __name__ == "__main__":
    unittest.main()


class TestReferenceCorpus(unittest.TestCase):
    """
    Guards the local reference copies. Skipped when reference/ has not been
    fetched, so the suite still runs on a clean checkout.
    """

    @classmethod
    def setUpClass(cls):
        from src.astadhyayi import corpus
        cls.corpus = corpus
        try:
            cls.gretil = corpus.load_gretil_sutrapatha()
            cls.vidyut = corpus.load_vidyut_sutrapatha()
        except corpus.CorpusUnavailable as error:
            raise unittest.SkipTest(str(error))

    def test_slp1_to_iast(self):
        s = self.corpus.slp1_to_iast
        self.assertEqual(s("vfdDirAdEc"), "vṛddhirādaic")
        self.assertEqual(s("adeN guRaH"), "adeṅ guṇaḥ")
        self.assertEqual(s("iko guRavfdDI"), "iko guṇavṛddhī")
        self.assertEqual(s("saMskftam"), "saṃskṛtam")

    def test_both_witnesses_carry_the_whole_work(self):
        self.assertGreater(len(self.vidyut), 3900)
        self.assertGreater(len(self.gretil), 3900)
        for sutra_id in ("1.1.1", "1.4.1", "6.1.77", "8.4.68"):
            self.assertIn(sutra_id, self.vidyut, sutra_id)

    def test_1_1_1_is_corroborated_by_both(self):
        self.assertEqual(self.vidyut["1.1.1"].text, "vṛddhirādaic")
        self.assertEqual(self.gretil["1.1.1"].text, "vṛddhir ād-aic")
        self.assertTrue(self.corpus.collate()["1.1.1"].corroborated)

    def test_gretil_hyphens_give_the_padaccheda(self):
        self.assertEqual(self.gretil["1.1.1"].padaccheda, ("vṛddhir", "ād", "aic"))
        self.assertEqual(self.gretil["1.1.3"].padaccheda, ("iko", "guṇa", "vṛddhī"))

    def test_collation_classes(self):
        collated = self.corpus.collate()
        self.assertEqual(collated["1.1.1"].classify(), "identical")
        self.assertEqual(collated["1.1.2"].classify(), "identical")
        # A known GRETIL data-entry error must NOT be absorbed as a sandhi
        # variant — prayarnaṃ for prayatnaṃ is a different word.
        self.assertEqual(collated["1.1.9"].classify(), "divergent")
        self.assertEqual(collated["1.3.7"].classify(), "divergent")   # duṭū / cuṭū

    def test_mahabhasya_is_addressable_with_kielhorn_locators(self):
        bhasya = self.corpus.load_mahabhasya()
        self.assertGreater(len(bhasya), 1000)
        self.assertIn("1.1.1", bhasya)
        segment = bhasya["1.1.1"][0]
        self.assertIn("Kielhorn", segment.locator)
        self.assertIn("1.1.1", segment.locator)
        self.assertTrue(segment.text)
