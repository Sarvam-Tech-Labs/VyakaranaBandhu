# -*- coding: utf-8 -*-
"""
Tests for the it-saṃjñā — 1.3.2 to 1.3.9.

The Kāśikā names a worked affix or root for nearly every clause of every rule
in this block, and those are the expectations below. Two of them are load-
bearing beyond their own sūtra:

  जस्     the j goes by 1.3.7 and the s stays by 1.3.4, both in one affix, and
          the nominative plural depends on getting both right.
  डुपचष्  ḍu goes as a pair by 1.3.5, ṣ as a final by 1.3.3 — and something is
          left over that no it-rule removes, which is recorded rather than
          hidden.

1.3.2 is tested against the dhātupāṭha rather than against invented forms,
because that is the only text on disk that actually writes the anunāsika marks.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import itsamjna as I
from src.astadhyayi.adesa import Adesa, substitution_site
from src.astadhyayi.corpus import load_dhatupatha
from src.astadhyayi.varna import ANUNASIKA_MARK, VARGA, is_anunasika


class Halantyam(unittest.TestCase):
    """1.3.3 हलन्त्यम्."""

    def test_the_sivasutra_finals_the_kasika_names(self):
        """अइउण् — णकारः। ऋऌक् — ककारः। एओङ् — ङकारः। ऐऔच् — चकारः।"""
        for form, stem, it in [
            ("aiuṇ", "aiu", "ṇ"),
            ("ṛḷk", "ṛḷ", "k"),
            ("eoṅ", "eo", "ṅ"),
            ("aiauc", "aiau", "c"),
        ]:
            parsed = I.analyze(form)
            self.assertEqual(parsed.stem, stem, form)
            self.assertEqual(parsed.it_letters, {it}, form)
            self.assertEqual(parsed.by("1.3.3")[0].letters, it, form)

    def test_it_agrees_with_the_sivasutra_module(self):
        """
        sivasutra.py strips these finals to resolve pratyāhāras, and has done
        since before this rule was codified. The two must not disagree about
        which letter is indicatory, or a pratyāhāra would resolve one way and
        the grammar read it another.
        """
        from src.astadhyayi.sivasutra import SIVASUTRAS

        for sutra in SIVASUTRAS:
            # The module records the it it stripped. Running 1.3.3 over the
            # same aphorism must name the same letter.
            parsed = I.analyze(sutra.iast.replace(" ", "").lower())
            self.assertEqual(
                parsed.it_letters, {sutra.it},
                f"śivasūtra {sutra.number} {sutra.iast}",
            )
            # The remainder holds the sūtra's sounds in order. It is not
            # equal to them: hayavaraṬ leaves "hayavara" for four phonemes
            # h y v r, the a's being there to make the consonants
            # pronounceable. That is the same उच्चारणार्थ vowel recorded
            # under 1.3.9, showing up in the śivasūtras too.
            cursor = 0
            for sound in sutra.sounds:
                found = parsed.stem.find(sound.phoneme, cursor)
                self.assertGreaterEqual(
                    found, 0,
                    f"śivasūtra {sutra.number}: {sound.phoneme} missing from "
                    f"{parsed.stem!r}",
                )
                cursor = found + len(sound.phoneme)
            leftover = parsed.stem
            for sound in sutra.sounds:
                leftover = leftover.replace(sound.phoneme, "", 1)
            self.assertEqual(
                set(leftover), set(leftover) & {"a"},
                f"śivasūtra {sutra.number}: {leftover!r} is not utterance a",
            )

    def test_a_final_vowel_is_not_an_it(self):
        self.assertEqual(I.analyze("ṭā", I.VIBHAKTI).by("1.3.3"), ())
        self.assertEqual(I.analyze("kta", I.PRATYAYA).by("1.3.3"), ())

    def test_a_digraph_final_goes_whole(self):
        parsed = I.analyze("ghurach", I.PRATYAYA)
        self.assertIn("ch", parsed.it_letters)


class NaVibhaktau(unittest.TestCase):
    """1.3.4 न विभक्तौ तुस्माः — the prohibition on 1.3.3."""

    def test_jas_shows_both_rules_at_once(self):
        """
        4.1.2 जस् — the j is indicatory by 1.3.7 and the s is protected here,
        so the affix is अस् and ब्राह्मण + अस् gives ब्राह्मणाः. Lose either
        half and the nominative plural is wrong.
        """
        parsed = I.analyze("jas", I.VIBHAKTI)
        self.assertEqual(parsed.stem, "as")
        self.assertEqual(parsed.it_letters, {"j"})
        self.assertEqual(parsed.by("1.3.7")[0].letters, "j")
        self.assertEqual(parsed.by("1.3.3"), ())

    def test_the_kasikas_example_of_each_protected_letter(self):
        """टाङसिङसाम् for the t-varga, जस् for s, अपचताम् for m."""
        for form, stem in [("tas", "tas"), ("thas", "thas"),
                           ("tām", "tām"), ("tam", "tam")]:
            self.assertEqual(I.analyze(form, I.VIBHAKTI).stem, stem, form)

    def test_tusma_is_the_whole_t_varga_and_not_the_letter_t(self):
        for sound in VARGA["tu"]:
            self.assertIn(sound, I.TUSMA, sound)
        self.assertIn("s", I.TUSMA)
        self.assertIn("m", I.TUSMA)
        self.assertEqual(len(I.TUSMA), 7)

    def test_outside_a_vibhakti_the_same_letters_are_indicatory(self):
        """
        विभक्ताविति किम्? The Kāśikā answers with यत्, युस्, श्नम्, अत् — all
        non-vibhakti, all losing the letter a vibhakti would keep.
        """
        for form, stem in [("yat", "ya"), ("yus", "yu"),
                           ("śnam", "na"), ("at", "a")]:
            self.assertEqual(I.analyze(form, I.PRATYAYA).stem, stem, form)

    def test_the_prohibition_only_reaches_the_final(self):
        """श्नम् loses its m as a non-vibhakti; its ś goes by 1.3.8 either way."""
        parsed = I.analyze("śnam", I.PRATYAYA)
        self.assertEqual(sorted(parsed.it_letters), ["m", "ś"])


class AdirNituDu(unittest.TestCase):
    """1.3.5 आदिर्ञिटुडवः."""

    def test_the_kasikas_roots(self):
        for form, stem in [("ṭuvepṛ", "vepṛ"), ("ḍukṛñ", "kṛ")]:
            self.assertEqual(I.analyze(form, I.DHATU).stem, stem, form)

    def test_the_opening_is_taken_as_a_pair(self):
        """
        ञि टु डु इत्येतेषां समुदायानाम् — a pair, not a letter. Both characters
        must be in one mark, or 1.3.9 would leave the vowel behind.
        """
        parsed = I.analyze("ḍukṛñ", I.DHATU)
        pair = parsed.by("1.3.5")[0]
        self.assertEqual(pair.letters, "ḍu")
        self.assertEqual((pair.start, pair.end), (0, 2))

    def test_it_is_tried_before_1_3_7_or_the_n_would_go_alone(self):
        """
        ñ is a c-varga letter, so 1.3.7 would take it singly and leave the i.
        This is the ordering constraint the two rules impose on each other.
        """
        parsed = I.analyze("ñimida" + ANUNASIKA_MARK, I.DHATU)
        self.assertEqual(parsed.by("1.3.5")[0].letters, "ñi")
        self.assertEqual(parsed.by("1.3.7"), ())
        self.assertNotIn("i", parsed.stem[:1])

    def test_it_does_not_require_an_affix_unlike_1_3_6_to_1_3_8(self):
        """Its examples are all roots."""
        self.assertEqual(I.analyze("ṭuvepṛ", I.DHATU).stem, "vepṛ")
        self.assertEqual(I.analyze("ṭuvepṛ", I.PLAIN).stem, "vepṛ")

    def test_a_similar_opening_that_is_not_one_of_the_three(self):
        """ṭi, ḍa, ña are not in the list and must not be stripped as pairs."""
        for form in ("ṭivepṛ", "ḍakṛ", "ñavepṛ"):
            self.assertEqual(I.analyze(form, I.DHATU).by("1.3.5"), (), form)


class AffixInitials(unittest.TestCase):
    """1.3.6 षः, 1.3.7 चुटू, 1.3.8 लशक्वतद्धिते."""

    def test_1_3_6_svun(self):
        """3.1.145 शिल्पिनि ष्वुन् — नर्त्तकी."""
        parsed = I.analyze("ṣvun", I.PRATYAYA)
        self.assertEqual(parsed.stem, "vu")
        self.assertEqual(parsed.by("1.3.6")[0].letters, "ṣ")

    def test_1_3_6_needs_an_affix(self):
        """प्रत्ययस्येति किम्? षोडः। षण्डः। षडिकः।"""
        for word in ("ṣoḍaḥ", "ṣaṇḍaḥ"):
            self.assertEqual(I.analyze(word, I.PLAIN).by("1.3.6"), (), word)

    def test_1_3_6_needs_the_s_to_be_initial(self):
        """आदिरित्येव — अविषः। महिषः।"""
        self.assertEqual(I.analyze("aviṣa", I.PRATYAYA).by("1.3.6"), ())

    def test_1_3_7_covers_both_vargas_entire(self):
        """चुटू is two udit terms, so by 1.1.69 ten letters and not two."""
        self.assertEqual(
            I.CUTU, frozenset(VARGA["cu"]) | frozenset(VARGA["ṭu"])
        )
        self.assertEqual(len(I.CUTU), 10)

    def test_1_3_7_the_kasikas_affixes(self):
        for form, stem in [("cphañ", "pha"), ("ñya", "ya"),
                           ("ṭa", "a"), ("ḍa", "a")]:
            self.assertEqual(I.analyze(form, I.PRATYAYA).stem, stem, form)

    def test_1_3_8_the_commonest_affixes_in_the_grammar(self):
        for form, stem in [("lyuṭ", "yu"), ("śap", "a"), ("kta", "ta"),
                           ("khac", "a"), ("ghurac", "ura")]:
            self.assertEqual(I.analyze(form, I.PRATYAYA).stem, stem, form)

    def test_1_3_8_atadhite_is_a_real_exclusion(self):
        """
        The contrast that shows the clause is applied and not ignored: the same
        letters, indicatory in an affix and kept in a taddhita.
        """
        self.assertEqual(I.analyze("ka", I.PRATYAYA).stem, "a")
        self.assertEqual(I.analyze("ka", I.TADDHITA).stem, "ka")
        self.assertEqual(I.analyze("ka", I.TADDHITA).its, ())

    def test_1_3_7_still_applies_to_a_taddhita(self):
        """Only 1.3.8 carries the exclusion; 1.3.6 and 1.3.7 do not."""
        self.assertEqual(I.analyze("ṭa", I.TADDHITA).stem, "a")
        self.assertEqual(I.analyze("ṣvun", I.TADDHITA).by("1.3.6")[0].letters,
                         "ṣ")

    def test_a_taddhita_is_an_affix(self):
        self.assertTrue(I.TADDHITA.pratyaya)
        self.assertTrue(I.VIBHAKTI.pratyaya)


class AnunasikaVowel(unittest.TestCase):
    """1.3.2 उपदेशेऽजनुनासिक इत्, against the dhātupāṭha."""

    def setUp(self):
        self.dhatus = load_dhatupatha()

    def test_the_kasikas_two_examples_are_dhatupatha_entries_2_and_3(self):
        """एध। स्पर्द्ध। — and the local file marks the nasal vowel."""
        edha = self.dhatus["01.0002"]
        spardha = self.dhatus["01.0003"]
        self.assertTrue(edha.upadesa.endswith(ANUNASIKA_MARK), edha.upadesa)
        self.assertEqual(I.analyze(edha.upadesa, I.DHATU).stem, "edh")
        self.assertEqual(I.analyze(spardha.upadesa, I.DHATU).stem, "spardh")

    def test_the_mark_is_attributed_to_1_3_2(self):
        parsed = I.analyze(self.dhatus["01.0002"].upadesa, I.DHATU)
        self.assertEqual([m.by for m in parsed.its], ["1.3.2"])

    def test_a_plain_vowel_is_not_indicatory(self):
        """अनुनासिक इति किम्? सर्वस्याचो मा भूत् — else every vowel would go."""
        self.assertEqual(I.analyze("edha", I.DHATU).by("1.3.2"), ())
        self.assertEqual(I.analyze("bhū", I.DHATU).its, ())

    def test_the_dhatupatha_marks_are_read_as_nasal_vowels(self):
        """
        The loader writes the candrabindu on the vowel rather than as m̐, so
        that 1.1.8's test can answer. A spot check that the two layers agree.
        """
        marked = [
            d for d in self.dhatus.values() if ANUNASIKA_MARK in d.upadesa
        ]
        self.assertGreater(len(marked), 1000)
        for entry in marked[:200]:
            index = entry.upadesa.index(ANUNASIKA_MARK)
            vowel = entry.upadesa[index - 1:index + 1]
            self.assertTrue(is_anunasika(vowel), f"{entry.code} {vowel!r}")

    def test_every_marked_root_loses_the_mark(self):
        for entry in list(self.dhatus.values())[:400]:
            parsed = I.analyze(entry.upadesa, I.DHATU)
            self.assertNotIn(ANUNASIKA_MARK, parsed.stem, entry.code)

    def test_the_scanner_treats_the_mark_as_weightless(self):
        """
        An anunāsika vowel is nasal, not heavy. If the mark were read as a
        nasal consonant the way anusvāra is, every such root would scan wrong.
        """
        from src.chandas.core import scan_phonemes

        plain = [p.text for p in scan_phonemes("edha")]
        nasal = [p.text for p in scan_phonemes("edha" + ANUNASIKA_MARK)]
        self.assertEqual(plain, nasal)


class Lopa(unittest.TestCase):
    """1.3.9 तस्य लोपः."""

    def test_the_whole_mark_goes_not_its_last_sound(self):
        """
        "तस्य"ग्रहणं सर्वलोपार्थम्। अलोऽन्त्यस्य मा भूत् — आदिर्ञिटुडवः इति.
        Under 1.1.52 the elision would take only the i of ḍu.
        """
        parsed = I.analyze("ḍukṛñ", I.DHATU)
        self.assertEqual(parsed.stem, "kṛ")
        self.assertNotIn("ḍ", parsed.stem)
        self.assertNotIn("u", parsed.stem)

    def test_marks_are_removed_from_both_ends_at_once(self):
        parsed = I.analyze("ḍupacaṣ", I.DHATU)
        self.assertEqual([m.by for m in parsed.its], ["1.3.5", "1.3.3"])

    def test_what_the_it_rules_leave_behind_is_recorded_not_hidden(self):
        """
        डुपचष् yields पच, where the root is पच्. The residual a is उच्चारणार्थ
        and belongs to no rule codified here. Asserted as it stands so that
        adding that convention later is a visible change, and so that nobody
        reads the engine as claiming पच.
        """
        self.assertEqual(I.analyze("ḍupacaṣ", I.DHATU).stem, "paca")
        self.assertEqual(I.analyze("ānaṅ", I.PRATYAYA).stem, "āna")
        from src.astadhyayi.sutra import REGISTRY
        self.assertIn("उच्चारणार्थ", REGISTRY.get("1.3.9").notes)

    def test_an_unmarked_form_survives_intact(self):
        self.assertEqual(I.analyze("bhū", I.DHATU).stem, "bhū")
        self.assertEqual(I.stem_of("tas", I.VIBHAKTI), "tas")


class WiredIntoSubstitution(unittest.TestCase):
    """The point of codifying the block: 1.1.55 no longer needs to be told."""

    def test_adesa_derives_its_own_it_letters(self):
        si = Adesa.from_upadesa("śi", I.PRATYAYA)
        self.assertTrue(si.sit)
        self.assertEqual(si.form, "i")
        self.assertFalse(si.anekal)
        self.assertEqual(substitution_site(si).by, "1.1.55")

    def test_a_ngit_substitute_is_recognised_without_being_declared(self):
        anang = Adesa.from_upadesa("ānaṅ", I.PRATYAYA)
        self.assertTrue(anang.ngit)
        self.assertEqual(substitution_site(anang).by, "1.1.53")

    def test_a_form_with_no_it_letters_is_left_alone(self):
        bhu = Adesa.from_upadesa("bhū", I.PRATYAYA)
        self.assertEqual(bhu.form, "bhū")
        self.assertEqual(bhu.its, frozenset())
        self.assertEqual(substitution_site(bhu).by, "1.1.55")   # anekāl

    def test_the_explicit_constructor_still_works(self):
        """A caller who knows the analysis should not have to round-trip."""
        self.assertEqual(
            Adesa("i", frozenset("ś")).sit,
            Adesa.from_upadesa("śi", I.PRATYAYA).sit,
        )


class Registration(unittest.TestCase):
    IDS = tuple(f"1.3.{n}" for n in range(2, 10))

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_all_eight_are_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_upadesa_is_carried_down_from_1_3_2_by_anuvrtti(self):
        """The corpus records it for 1.3.3 through 1.3.8, and it is the
        condition on the whole block."""
        for sutra_id in [f"1.3.{n}" for n in range(3, 9)]:
            carried = " ".join(self.registry.get(sutra_id).anuvrtti)
            self.assertIn("1.3.2", carried, sutra_id)

    def test_the_pada_module_was_discovered_automatically(self):
        import src.astadhyayi.rules as rules
        self.assertIn("adhyaya_1_pada_3", rules.PADAS)


if __name__ == "__main__":
    unittest.main()
