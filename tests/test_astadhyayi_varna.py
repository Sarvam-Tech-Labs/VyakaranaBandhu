# -*- coding: utf-8 -*-
"""
Tests for the varṇa layer and the phonetic saṃjñās 1.1.7–1.1.10.

The expectations here are the commentaries' own worked examples wherever the
commentaries supply one — the Kāśikā's discriminating sets on 1.1.9, its blocked
pairs on 1.1.10, its nine saṃyoga words on 1.1.7, the bhāṣya's argument about
anusvāra on 1.1.8. Where a test asserts something not stated in a source, it
asserts a structural property (a partition, an equivalence relation, agreement
between two modules) that would break under a wrong table rather than a value
transcribed from the same place the code got it.
"""

from __future__ import annotations

import itertools
import unittest

from src.astadhyayi import varna as V
from src.astadhyayi.rules import adhyaya_1_pada_1 as R
from src.astadhyayi.sivasutra import resolve
from src.chandas.core import scan_phonemes


class SiksaTable(unittest.TestCase):
    """The place and effort tables, against the verse they came from."""

    def test_every_hal_and_ac_is_placed(self):
        """
        The Śikṣā must reach every sound the śivasūtras enumerate. If a varga or
        a verse quarter were dropped, some haL would have no place.
        """
        for sound in resolve("haL").sounds:
            self.assertIsNotNone(V.varna(sound), f"{sound} has no sthāna")
        for sound in resolve("aC").sounds:
            self.assertIsNotNone(V.varna(sound), f"{sound} has no sthāna")

    def test_the_consonants_are_partitioned_three_ways_by_the_kaumudi(self):
        """
        कादयो मावसानाः स्पर्शाः / यणोऽन्तःस्थाः / शल ऊष्माणः together cover haL
        exactly once. Two independent things have to be right for this to hold:
        the varga table, and the śivasūtra resolution of yaṆ and śaL.
        """
        hal = frozenset(resolve("haL").sounds)
        self.assertEqual(len(hal), 33)
        self.assertEqual(V.SPARSA | V.ANTAHSTHA | V.USMAN, hal)
        self.assertEqual(V.SPARSA & V.ANTAHSTHA, frozenset())
        self.assertEqual(V.SPARSA & V.USMAN, frozenset())
        self.assertEqual(V.ANTAHSTHA & V.USMAN, frozenset())

    def test_khar_and_has_partition_the_consonants(self):
        """
        खरो विवाराः श्वासा अघोषाश्च / हशः संवारा नादा घोषाश्च — voiced against
        voiceless, and between them the whole of haL. A wrong it-marker anywhere
        in śivasūtras 8–14 shows up here as an overlap or a gap.
        """
        khar = frozenset(resolve("khaR").sounds)
        has = frozenset(resolve("haŚ").sounds)
        self.assertEqual(khar | has, frozenset(resolve("haL").sounds))
        self.assertEqual(khar & has, frozenset())

    def test_alpaprana_and_mahaprana_also_partition_the_consonants(self):
        """
        वर्गाणां प्रथमतृतीयपञ्चमा यणश्चाल्पप्राणाः against
        वर्गाणां द्वितीयचतुर्थौ शलश्च महाप्राणाः — a second, independent
        partition of the same 33. It uses the varga table by position, so a
        varga listed in the wrong order would break this and not the previous.
        """
        hal = frozenset(resolve("haL").sounds)
        self.assertEqual(V.ALPAPRANA | V.MAHAPRANA, hal)
        self.assertEqual(V.ALPAPRANA & V.MAHAPRANA, frozenset())
        self.assertEqual(len(V.MAHAPRANA), 14)   # 2 per varga + śaL

    def test_the_aspirates_are_the_mahapranas(self):
        """A sanity anchor on the varga ordering that does not go through a
        pratyāhāra: every consonant written with an h is mahāprāṇa."""
        for group in V.VARGA.values():
            for sound in group:
                aspirated = sound.endswith("h") and len(sound) > 1
                self.assertEqual(
                    aspirated, sound in V.MAHAPRANA, f"{sound}"
                )

    def test_each_sound_records_the_verse_quarter_that_placed_it(self):
        self.assertEqual(
            V.varna("k").siksa, "akuhavisarjanīyānāṃ kaṇṭhaḥ"
        )
        self.assertEqual(V.varna("ṣ").siksa, "ṛṭuraṣāṇāṃ mūrdhā")
        self.assertEqual(V.varna("v").siksa, "vakārasya dantoṣṭham")
        # every quarter is used — a row nothing points at would be dead data
        used = {v.siksa for v in V.VARNAS.values()}
        self.assertEqual(used, {row[0] for row in V.SIKSA_STHANA})

    def test_short_a_is_vivrta_in_derivation_and_samvrta_only_in_speech(self):
        """
        ह्रस्वस्यावर्णस्य प्रयोगे संवृतम् । प्रक्रियादशायां तु विवृतमेव ।

        This is not decorative. If short a were saṃvṛta during derivation it
        would not share an effort with ā, they would not be savarṇa, and
        6.1.101 अकः सवर्णे दीर्घः could never lengthen a + a.
        """
        self.assertIs(V.varna("a").abhyantara, V.Abhyantara.VIVRTA)
        self.assertIs(
            V._abhyantara_of("a", derivational=False), V.Abhyantara.SAMVRTA
        )
        self.assertTrue(V.savarna("a", "ā"))


class Savarna(unittest.TestCase):
    """1.1.9 तुल्यास्यप्रयत्नं सवर्णम्."""

    def test_kasika_asyagrahana_k_c_t_t_p_are_not_savarna(self):
        """
        आस्यग्रहणं किम्? कचटतपानां भिन्नस्थानानां तुल्यप्रयत्नानां मा भूत्।

        The Kāśikā's reason for naming place: these five share an effort and
        must still be kept apart. Drop the sthāna test and every pair passes.
        """
        for a, b in itertools.combinations("kcṭtp", 2):
            self.assertFalse(V.savarna(a, b), f"{a}~{b}")
            self.assertIs(
                V.varna(a).abhyantara, V.varna(b).abhyantara,
                "the premise: they do share an effort",
            )

    def test_kasika_prayatnagrahana_i_c_y_s_are_not_savarna(self):
        """
        प्रयत्नग्रहणं किम्? इचुयशानां तुल्यस्थानानां भिन्नजातीयानां मा भूत्।

        The mirror case: all four are tālavya and must still be kept apart.
        """
        for a, b in itertools.combinations(["i", "c", "y", "ś"], 2):
            self.assertFalse(V.savarna(a, b), f"{a}~{b}")
            self.assertIs(
                V.varna(a).sthana, V.varna(b).sthana,
                "the premise: they do share a place",
            )

    def test_a_savarna_class_of_a_stop_is_exactly_its_varga(self):
        """वर्ग्यो वर्ग्येण सवर्णः (Āpiśali, quoted by the Kāśikā)."""
        for group in V.VARGA.values():
            for sound in group:
                self.assertEqual(
                    frozenset(V.savarnas_of(sound)), frozenset(group), sound
                )

    def test_repha_and_the_usmans_have_no_savarna_among_the_varnas(self):
        """
        रेफोष्मणां सवर्णा न सन्ति.

        Read in its place: the Kāśikā is counting how many sub-varieties each
        sound has — eighteen kinds of a, twelve of ṛ, two of the semivowels
        bar r — and says r and the ūṣmans have none. So the claim is about the
        varṇas proper. The ayogavāhas are a separate question, kept below.
        """
        proper = frozenset(resolve("haL").sounds) | frozenset(resolve("aC").sounds)
        proper |= {long for base in V.VOWEL_VARNA.values() for long in base}
        for sound in ["r"] + sorted(V.USMAN):
            self.assertEqual(
                frozenset(V.savarnas_of(sound)) & proper, {sound}, sound
            )

    def test_visarga_comes_out_savarna_with_h_which_no_source_settles(self):
        """
        The one collision the Śikṣā's own assignments produce: visarga is
        placed कण्ठ alongside h by अकुहविसर्जनीयानां कण्ठः, and both are
        īṣadvivṛta if visarga is counted an ūṣman, as the Prātiśākhyas do.

        Nothing local rules on it. The ayogavāhas sit outside the
        akṣarasamāmnāya, so the tradition may simply not be assigning them the
        saṃjñā at all. Asserted as it currently stands so that the day a source
        settles the question, this test is what fails and forces the record to
        be updated — see the OPEN note on 1.1.9.
        """
        self.assertEqual(V.savarnas_of("h"), ("h", V.VISARGA))
        self.assertIs(V.varna("h").sthana, V.varna(V.VISARGA).sthana)
        # the other two ayogavāhas each sit at a place of their own, so they
        # collide with nothing
        self.assertEqual(V.savarnas_of(V.JIHVAMULIYA), (V.JIHVAMULIYA,))
        self.assertEqual(V.savarnas_of(V.UPADHMANIYA), (V.UPADHMANIYA,))

    def test_external_effort_is_not_a_criterion(self):
        """
        k kh g gh ṅ differ in voice, aspiration and nasality and are savarṇa
        all the same — which is what makes 8.4.58 parasavarṇa possible.
        """
        self.assertTrue(V.savarna("k", "g"))    # voice
        self.assertTrue(V.savarna("k", "kh"))   # aspiration
        self.assertTrue(V.savarna("k", "ṅ"))    # nasality
        self.assertNotEqual(V.varna("k").bahya, V.varna("g").bahya)

    def test_the_three_dimensions_the_kasika_says_are_ignored(self):
        """
        स्वरानुनासिक्यकालभिन्नस्य ग्रहणं भवति (Kāśikā on 1.1.69) — accent,
        nasality and duration are all disregarded by savarṇatva.
        """
        self.assertTrue(V.savarna("a", "ā"))                      # kāla
        self.assertTrue(V.savarna("ā", V.nasalize("ā")))          # ānunāsikya
        self.assertTrue(V.savarna("i", "ī"))
        self.assertTrue(V.savarna("ṛ", "ṝ"))

    def test_savarna_is_an_equivalence_relation(self):
        """
        Reflexive, symmetric, transitive. Nothing in the sources says so in
        those words, but the vārttika could easily have broken transitivity —
        it joins two classes with different places — so it is worth proving
        that the ṛ/ḷ extension merges the classes cleanly instead of leaving a
        ragged edge.
        """
        sounds = sorted(V.VARNAS)
        for a in sounds:
            self.assertTrue(V.savarna(a, a), f"reflexive: {a}")
        for a, b in itertools.combinations(sounds, 2):
            self.assertEqual(
                V.savarna(a, b), V.savarna(b, a), f"symmetric: {a}~{b}"
            )
        for a, b, c in itertools.combinations(sounds, 3):
            if V.savarna(a, b) and V.savarna(b, c):
                self.assertTrue(V.savarna(a, c), f"transitive: {a}~{b}~{c}")

    def test_the_r_l_varttika_changes_an_answer(self):
        """
        ऋकारऌकारयोः सवर्णसञ्ज्ञा विधेया. ṛ is mūrdhanya and ḷ dantya, so the
        sūtra by itself will not join them: the vārttika is doing work, not
        restating. Every ṛ-length must reach every ḷ-length.
        """
        for a in V.VOWEL_VARNA["ṛ"]:
            for b in V.VOWEL_VARNA["ḷ"]:
                self.assertTrue(V.savarna(a, b), f"{a}~{b} with vārttika")
                self.assertFalse(
                    V.savarna(a, b, varttika=False), f"{a}~{b} without"
                )
        self.assertIsNot(V.varna("ṛ").sthana, V.varna("ḷ").sthana)

    def test_savarna_of_an_unknown_sound_is_false_not_an_error(self):
        self.assertFalse(V.savarna("q", "k"))
        self.assertFalse(V.savarna("k", "q"))


class NaAjjhalau(unittest.TestCase):
    """1.1.10 नाज्झलौ."""

    def test_no_vowel_is_savarna_with_a_consonant(self):
        vowels = [s for s in V.VARNAS if V.varna(s).svara]
        consonants = [s for s in V.VARNAS if not V.varna(s).svara]
        for a in vowels:
            for b in consonants:
                self.assertFalse(V.savarna(a, b), f"{a}~{b}")

    def test_under_the_kasikas_fourfold_reading_it_rescues_its_own_examples(self):
        """
        The Kāśikā names अवर्णहकारौ (दण्डहस्तः) and इवर्णशकारौ (दधिशीतम्). Those
        are savarṇa-but-for-1.1.10 only if īṣadvivṛta has collapsed into
        vivṛta — the fourfold count the same commentary gives on 1.1.9. The
        pairs below are computed from the feature table, so finding the Kāśikā's
        two inside them is a check on the table and not a restatement of it.
        """
        rescued = {
            frozenset(p) for p in V.blocked_by_na_ajjhalau(V.FOURFOLD)
        }
        self.assertIn(frozenset({"a", "h"}), rescued)
        self.assertIn(frozenset({"i", "ś"}), rescued)
        # and the ones that follow by the same logic
        self.assertIn(frozenset({"ṛ", "ṣ"}), rescued)
        self.assertIn(frozenset({"ḷ", "s"}), rescued)
        self.assertIn(frozenset({"u", V.UPADHMANIYA}), rescued)
        # every rescued pair is one vowel and one consonant, by construction
        for pair in V.blocked_by_na_ajjhalau(V.FOURFOLD):
            self.assertNotEqual(
                V.varna(pair[0]).svara, V.varna(pair[1]).svara, pair
            )

    def test_under_the_fivefold_reading_it_rescues_nothing(self):
        """
        On the Kaumudī's count the efforts have already parted every such pair,
        so the niṣedha is idle. Recorded because it is a real consequence of
        choosing that scheme, not because it is desirable.
        """
        self.assertEqual(V.blocked_by_na_ajjhalau(V.FIVEFOLD), ())

    def test_the_two_schemes_differ_only_over_the_usmans(self):
        differing = [
            s for s in V.VARNAS
            if V.effort(s, V.FIVEFOLD) is not V.effort(s, V.FOURFOLD)
        ]
        self.assertEqual(
            frozenset(differing),
            V.USMAN | {V.VISARGA, V.JIHVAMULIYA, V.UPADHMANIYA},
        )


class Anunasika(unittest.TestCase):
    """1.1.8 मुखनासिकावचनोऽनुनासिकः."""

    def test_exactly_the_five_varga_nasals_among_the_plain_sounds(self):
        self.assertEqual(
            [s for s in V.VARNAS if V.is_anunasika(s)],
            list(V.ANUNASIKA_STOPS),
        )

    def test_anusvara_is_not_anunasika(self):
        """
        नासिकावचनः अनुनासिकः इति इयति उच्यमाने यमानुस्वाराणाम् एव प्रसज्येत —
        मुख is in the sūtra precisely to keep anusvāra out. Its place is the
        nose alone, so it fails the mouth half.
        """
        self.assertFalse(V.is_anunasika(V.ANUSVARA))
        self.assertTrue(V.varna(V.ANUSVARA).nasika)
        self.assertFalse(V.varna(V.ANUSVARA).mukha)

    def test_the_pure_mouth_sounds_are_not_anunasika_either(self):
        """मुखवचनः अनुनासिकः इति इयति उच्यमाने कचटतपानाम् एव प्रसज्येत —
        the nose half excludes exactly these."""
        for sound in "kcṭtp":
            self.assertFalse(V.is_anunasika(sound))
            self.assertTrue(V.varna(sound).mukha)
            self.assertFalse(V.varna(sound).nasika)

    def test_a_marked_vowel_is_anunasika(self):
        """
        The Kāśikā's own illustration is 6.1.126 आङोऽनुनासिकश्छन्दसि with आँ.
        A vowel is mouth-uttered already; the mark adds the nose.
        """
        self.assertFalse(V.is_anunasika("ā"))
        self.assertTrue(V.is_anunasika(V.nasalize("ā")))
        self.assertTrue(V.is_anunasika(V.nasalize("y")))
        self.assertIs(
            V.varna(V.nasalize("ā")).sthana, V.varna("ā").sthana,
            "nasality is laid over a place, it does not change it",
        )

    def test_nasalizing_is_idempotent(self):
        self.assertEqual(V.nasalize(V.nasalize("ā")), V.nasalize("ā"))


class Samyoga(unittest.TestCase):
    """1.1.7 हलोऽनन्तराः संयोगः."""

    #: The Kāśikā's worked examples, with the conjunct it names for each.
    KASIKA = [
        ("agniḥ", ["gn"]),
        ("aśvaḥ", ["śv"]),
        ("karṇaḥ", ["rṇ"]),
        ("indraḥ", ["ndr"]),
        ("candraḥ", ["ndr"]),
        ("mandraḥ", ["ndr"]),
        ("uṣṭraḥ", ["ṣṭr"]),
        ("rāṣṭram", ["ṣṭr"]),
        ("bhrāṣṭram", ["bhr", "ṣṭr"]),
    ]

    def test_the_kasikas_examples(self):
        for word, expected in self.KASIKA:
            got = [g.text for g in R.samyogas(word)]
            self.assertEqual(got, expected, word)

    def test_two_consonants_are_enough(self):
        """जातौ चेदं बहुवचनम्, तेन द्वयोर्बहूनां च संयोगसंज्ञा सिद्धा भवति।"""
        pairs = [len(g) for g in R.samyogas("agniḥ")]
        self.assertEqual(pairs, [2])
        self.assertEqual([len(g) for g in R.samyogas("indraḥ")], [3])

    def test_a_single_consonant_is_not_a_samyoga(self):
        self.assertEqual(R.samyogas("kamalam"), ())
        self.assertEqual(R.samyogas("gajaḥ"), ())

    def test_a_vowel_breaks_a_run(self):
        self.assertEqual([g.text for g in R.samyogas("kaṭaka")], [])
        self.assertEqual([g.text for g in R.samyogas("takra")], ["kr"])

    def test_anusvara_and_visarga_neither_join_nor_split(self):
        """
        Neither is in haL, so neither can be a member; and the gloss makes only
        vowels interrupt, so neither breaks a run either.
        """
        self.assertEqual(R.samyogas("kaṃsaḥ"), ())
        self.assertEqual([g.text for g in R.samyogas("saṃskṛtam")], ["sk"])
        self.assertEqual([g.text for g in R.samyogas("duḥkham")], [])

    def test_the_extent_locates_the_conjunct_in_the_text(self):
        """
        8.2.23 संयोगान्तस्य लोपः needs to know where a conjunct ends, so the
        offsets have to be usable to slice the original string.
        """
        for word, _ in self.KASIKA:
            for group in R.samyogas(word):
                self.assertEqual(word[group.start:group.end], group.text)

    def test_every_member_is_a_hal(self):
        hal = frozenset(resolve("haL").sounds)
        for word, _ in self.KASIKA:
            for group in R.samyogas(word):
                for sound in group.sounds:
                    self.assertIn(sound, hal, f"{sound} in {word}")

    def test_it_agrees_with_the_prosody_engine_on_what_a_phoneme_is(self):
        """
        The saṃjñā and the metre engine must segment identically, or a verse
        could scan one way and parse another. Both go through scan_phonemes,
        and this checks that the reuse is real rather than a parallel copy.
        """
        for word, _ in self.KASIKA:
            consonants = [p.text for p in scan_phonemes(word)
                          if p.kind == "consonant"]
            from_groups = [s for g in R.samyogas(word) for s in g.sounds]
            for sound in from_groups:
                self.assertIn(sound, consonants, word)


class Registration(unittest.TestCase):
    """The four sūtras are on the record, with what the record requires."""

    IDS = ("1.1.7", "1.1.8", "1.1.9", "1.1.10")

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_each_carries_a_verified_mula_reading_with_a_locator(self):
        """
        The record refuses a VERIFIED reading without a citation, so this is
        really a check that register() wired the corpus in for these four.
        """
        from src.astadhyayi.sutra import Source, Status

        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            mula = sutra.reading(Source.MULA)
            self.assertIsNotNone(mula, f"{sutra_id} has no mūla reading")
            self.assertIs(mula.status, Status.VERIFIED, sutra_id)
            self.assertTrue(mula.locator, sutra_id)
            self.assertTrue(mula.text, sutra_id)

    def test_the_devanagari_matches_the_corpus_not_the_codification(self):
        """Each entry must carry the sūtra as the witnesses have it."""
        expected = {
            "1.1.7": "हलोऽनन्तराः संयोगः",
            "1.1.8": "मुखनासिकावचनोऽनुनासिकः",
            "1.1.9": "तुल्यास्यप्रयत्नं सवर्णम्",
            "1.1.10": "नाज्झलौ",
        }
        for sutra_id, text in expected.items():
            self.assertEqual(self.registry.get(sutra_id).devanagari, text)

    def test_the_sandhyaksara_finding_is_recorded_with_its_reasoning(self):
        """
        e~ai was first recorded here as an open question on the ground that no
        rule turned on it. That was wrong, and 1.1.69 is what proved it. The
        record has to carry the corrected answer AND how it was reached, or the
        next reader repeats the mistake.
        """
        notes = self.registry.get("1.1.9").notes
        self.assertNotIn("OPEN", notes)
        self.assertIn("सन्ध्यक्षराणां", notes)
        self.assertIn("1.1.69", notes)
        self.assertFalse(V.savarna("e", "ai"), "the state the note describes")
        self.assertFalse(V.savarna("o", "au"))

    def test_every_note_marks_each_finding_settled_or_open(self):
        """
        The notes are the working record. Every sūtra must reach at least one
        finding and say whether it is settled or still open — notes that only
        describe, without ever concluding, are the failure mode this guards
        against. Supporting paragraphs under a marked finding need no marker of
        their own.
        """
        BLANK = chr(10) * 2
        for sutra_id in ("1.1.1", "1.1.2", "1.1.3", "1.1.7", "1.1.8",
                         "1.1.9", "1.1.10", "1.1.68", "1.1.69", "1.1.70",
                         "1.1.71"):
            notes = self.registry.get(sutra_id).notes
            self.assertTrue(notes.strip(), f"{sutra_id} has no notes")
            marked = [
                para for para in notes.split(BLANK)
                if para.startswith(("SETTLED", "OPEN", "SCOPE",
                                    "IMPLEMENTATION"))
            ]
            self.assertTrue(
                marked, f"{sutra_id}: no paragraph declares SETTLED or OPEN"
            )


if __name__ == "__main__":
    unittest.main()
