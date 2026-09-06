# -*- coding: utf-8 -*-
"""
Tests for the substitution paribhāṣās — 1.1.49 to 1.1.52.

The Kāśikā on 1.1.50 is unusually generous: it names the four kinds of nearness,
gives a worked example of each, ranks them, and then explains the superlative
with a fifth example. Nearly every expectation below is one of those, which is
the point — the algorithm was written to satisfy the commentary's cases, and if
it drifts these fail.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import adesa as A
from src.astadhyayi import varna as V
from src.astadhyayi.rules.adhyaya_1_pada_1 import GUNA, IK_ALL, VRDDHI
from src.astadhyayi.sources import all_sutra_ids, facts


class SasthiSthaneyoga(unittest.TestCase):
    """1.1.49 षष्ठी स्थानेयोगा."""

    def test_it_reads_the_genitive_off_the_corpus(self):
        self.assertEqual(A.sthanin_padas("1.1.3"), ("इकः",))
        self.assertEqual(A.sthanin_padas("1.1.51"), ("उः",))
        self.assertEqual(A.sthanin_padas("8.2.80"), ("अदसः", "असेः", "दः"))

    def test_a_sutra_with_no_genitive_names_no_sthanin(self):
        """6.1.101 अकः सवर्णे दीर्घः — अकः is genitive, so this is a check that
        the reading is real; 1.1.1 has none."""
        self.assertEqual(A.sthanin_padas("1.1.1"), ())
        self.assertEqual(A.sthanin_padas("1.1.9"), ())

    def test_it_is_executable_across_the_whole_text(self):
        """
        The codification is worth having only if it works on all 3,983 sūtras
        rather than on a few hand-marked ones. Every genitive it reports must
        actually be a pada of that sūtra.
        """
        with_sthanin = 0
        for sutra_id in all_sutra_ids():
            padas = A.sthanin_padas(sutra_id)
            if not padas:
                continue
            with_sthanin += 1
            words = {p.word for p in facts(sutra_id).padas}
            for pada in padas:
                self.assertIn(pada, words, sutra_id)
        # A substantial minority of the grammar states substitutions.
        self.assertGreater(with_sthanin, 800)
        self.assertLess(with_sthanin, 3000)


class Antaratama(unittest.TestCase):
    """1.1.50 स्थानेऽन्तरतमः — the Kāśikā's four dimensions, one by one."""

    def test_sthanatah_place(self):
        """
        6.1.101 अकः सवर्णे दीर्घः, दण्डाग्रम् — of two a's, the long ā, which is
        kaṇṭhya as they are.
        """
        self.assertEqual(A.antaratama("a", ["ā", "ī", "ū"]), ("ā",))

    def test_gunatah_quality_at_7_3_52(self):
        """
        चजोः कु घिण्ण्यतोः, पाकः त्यागः रागः. The Kāśikā spells the reasoning
        out: चकारस्याल्पप्राणस्याघोषस्य तादृश एव ककारो भवति, जकारस्य घोषवतोऽ-
        ल्पप्राणस्य तादृश एव गकारः — c is unaspirated and voiceless so k, j is
        voiced and unaspirated so g. Place cannot decide this; quality does.
        """
        kavarga = list(V.VARGA["ku"])
        self.assertEqual(A.antaratama("c", kavarga), ("k",))
        self.assertEqual(A.antaratama("j", kavarga), ("g",))
        self.assertEqual(A.antaratama("ch", kavarga), ("kh",))
        self.assertEqual(A.antaratama("jh", kavarga), ("gh",))
        self.assertEqual(A.antaratama("ñ", kavarga), ("ṅ",))

    def test_pramanatah_measure_at_8_2_80(self):
        """अदसोऽसेर्दादु दो मः, अमुष्मै अमूभ्याम् — ह्रस्वस्य ह्रस्वः,
        दीर्घस्य दीर्घः. Among sounds alike in place and quality, duration."""
        self.assertEqual(A.nearness("u", "u").pramana, True)
        self.assertEqual(A.nearness("u", "ū").pramana, False)
        self.assertEqual(A.antaratama("u", ["u", "ū"]), ("u",))
        self.assertEqual(A.antaratama("ū", ["u", "ū"]), ("ū",))

    def test_arthatah_is_absent_and_says_so(self):
        """
        The fourth dimension needs a semantics this project has not got. It is
        recorded as missing rather than approximated.
        """
        self.assertIsNone(A.nearness("a", "ā").artha)

    def test_place_outranks_measure_the_ceta_stota_case(self):
        """
        चेता। स्तोता। प्रमाणतोऽकारो गुणः प्राप्तः, तत्र स्थानत आन्तर्यादेकारौकारौ
        भवतः.

        This is the decisive case. i and a are both hrasva, so measure argues
        for a; i and e share tālu, so place argues for e; place wins. If the
        ranking were the other way round both this and the whole guṇa series
        would come out wrong.
        """
        self.assertEqual(A.antaratama("i", list(GUNA)), ("e",))
        self.assertEqual(A.antaratama("u", list(GUNA)), ("o",))
        # the premise: measure really would have chosen a
        self.assertTrue(A.nearness("i", "a").pramana)
        self.assertFalse(A.nearness("i", "e").pramana)

    def test_the_superlative_is_a_count_the_vagghasati_case(self):
        """
        तमब्ग्रहणं किम्? वाग्घसति। ... तमब्ग्रहणाद् ये सोष्माणो नादवन्तश्च ते
        भवन्ति चतुर्थाः.

        h is both breathy and voiced. The aspirate matches one, the voiced
        unaspirate matches the other, and the voiced aspirate matches both — so
        it wins only because matches are counted.
        """
        kavarga = list(V.VARGA["ku"])
        self.assertEqual(A.antaratama("h", kavarga), ("gh",))
        scores = {n.candidate: n.guna_shared for n in A.ranked("h", kavarga)}
        self.assertGreater(scores["gh"], scores["g"])
        self.assertGreater(scores["gh"], scores["kh"])
        self.assertGreater(scores["g"], scores["k"])

    def test_a_tie_is_reported_rather_than_broken(self):
        """
        Silently picking one of two equals would hide the places where a further
        provision is needed, which is precisely where the interesting sūtras
        live.
        """
        self.assertEqual(A.antaratama("k", ["k", "k"]), ("k", "k"))
        self.assertEqual(A.antaratama("k", []), ())

    def test_an_unknown_sound_is_skipped_not_guessed_at(self):
        self.assertEqual(A.antaratama("k", ["q"]), ())
        self.assertIsNone(A.nearness("q", "k"))

    def test_a_sound_is_nearest_to_itself(self):
        for sound in sorted(V.VARNAS):
            self.assertIn(
                sound, A.antaratama(sound, sorted(V.VARNAS)), sound
            )


class UranRaparah(unittest.TestCase):
    """1.1.51 उरण् रपरः."""

    def test_r_is_appended_only_for_r_varna(self):
        """उरिति किम्? खेयम्। गेयम्."""
        self.assertEqual(A.raparatva("ṛ", "a"), "ar")
        self.assertEqual(A.raparatva("ṝ", "ā"), "ār")
        self.assertEqual(A.raparatva("i", "e"), "e")
        self.assertEqual(A.raparatva("u", "o"), "o")

    def test_only_an_an_substitute_takes_the_r(self):
        """अण्ग्रहणं किम्? सुधातुरकङ् च — सौधातकिः, where an affix replaces ṛ."""
        self.assertEqual(A.raparatva("ṛ", "akaṅ"), "akaṅ")
        self.assertEqual(A.raparatva("ṛ", "k"), "k")

    def test_1_1_50_chooses_a_for_r_without_being_told_to(self):
        """
        The division of labour: this sūtra assumes an aṆ has already arisen.
        ṛ shares no articulator with a, e or o, but it is two articulators from
        a and three from each of e and o, so अन्तरतम reaches a on its own.
        """
        self.assertEqual(A.antaratama("ṛ", list(GUNA)), ("a",))
        self.assertEqual(A.antaratama("ṛ", list(VRDDHI)), ("ā",))
        self.assertEqual(
            V.varna("ṛ").places & V.varna("a").places, frozenset()
        )


class GunaVrddhiCorrespondence(unittest.TestCase):
    """
    What the note on 1.1.3 deferred: which guṇa or vṛddhi replaces which iK.

    These are the correspondences every Sanskrit primer prints as a table. Here
    none of them is written down — each is computed from the Śikṣā's places, the
    ranking in 1.1.50, and 1.1.51. Getting the familiar table out is the check.
    """

    GUNA_TABLE = {"i": "e", "ī": "e", "u": "o", "ū": "o",
                  "ṛ": "ar", "ṝ": "ar", "ḷ": "al", "ḹ": "al"}
    VRDDHI_TABLE = {"i": "ai", "ī": "ai", "u": "au", "ū": "au",
                    "ṛ": "ār", "ṝ": "ār", "ḷ": "āl", "ḹ": "āl"}

    def test_the_guna_series(self):
        for vowel, expected in self.GUNA_TABLE.items():
            self.assertEqual(A.guna_of(vowel), expected, vowel)

    def test_the_vrddhi_series(self):
        for vowel, expected in self.VRDDHI_TABLE.items():
            self.assertEqual(A.vrddhi_of(vowel), expected, vowel)

    def test_nothing_in_the_table_is_hardcoded_anywhere(self):
        """
        A guard against the obvious shortcut. The candidates come from 1.1.1
        and 1.1.2, which are themselves derived from the śivasūtras, and the
        choice is made by comparison — so no source file should contain the
        pairing as a literal.
        """
        import pathlib

        for path in pathlib.Path("src/astadhyayi").rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            for pair in ('"i": "e"', "'i': 'e'", '"u": "o"', "'u': 'o'"):
                self.assertNotIn(pair, text, f"{path} tabulates the answer")

    def test_every_ik_vowel_gets_both(self):
        for vowel in IK_ALL:
            self.assertIsNotNone(A.guna_of(vowel), vowel)
            self.assertIsNotNone(A.vrddhi_of(vowel), vowel)

    def test_the_l_case_completed_by_katyayana(self):
        """
        ḷ gives अल् and आल्, and it takes a vārttika to get there: लपर इति
        वक्तव्यम् on this sūtra. An earlier version of this test asserted the
        bare a and ā, because the vārttika collection had not been read.
        """
        self.assertEqual(A.guna_of("ḷ"), "al")
        self.assertEqual(A.vrddhi_of("ḷ"), "āl")
        self.assertEqual(A.guna_of("ḹ"), "al")

    def test_the_lapara_varttika_changes_an_answer(self):
        """Without it the sūtra alone gives only the vowel."""
        self.assertEqual(A.raparatva("ḷ", "a"), "al")
        self.assertEqual(A.raparatva("ḷ", "a", varttika=False), "a")
        # and it does not disturb the ṛ case, which is the sūtra's own
        self.assertEqual(A.raparatva("ṛ", "a"), "ar")
        self.assertEqual(A.raparatva("ṛ", "a", varttika=False), "ar")

    def test_l_takes_l_exactly_where_r_takes_r(self):
        for short, expected in (("ṛ", "r"), ("ḷ", "l")):
            self.assertTrue(A.guna_of(short).endswith(expected), short)
            self.assertTrue(A.vrddhi_of(short).endswith(expected), short)

    def test_guna_and_vrddhi_of_the_same_vowel_never_coincide(self):
        for vowel in ("i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ"):
            self.assertNotEqual(A.guna_of(vowel), A.vrddhi_of(vowel), vowel)


class AloAntyasya(unittest.TestCase):
    """1.1.52 अलोऽन्त्यस्य."""

    def test_the_kasikas_example_id_gonyah(self):
        """1.2.50 इद् गोण्याः — पञ्चगोणिः. Only the final ī goes."""
        self.assertEqual(A.replace_antya("goṇī", "i"), "goṇi")

    def test_it_takes_the_last_sound_and_not_the_last_character(self):
        """
        A digraph must not be split. Segmentation is the prosody engine's, so
        this also checks that the reuse is real.
        """
        self.assertEqual(A.antya("vāk"), "k")
        self.assertEqual(A.antya("labh"), "bh")
        self.assertEqual(A.replace_antya("labh", "p"), "lap")
        self.assertEqual(A.antya("gau"), "au")
        self.assertEqual(A.replace_antya("gau", "o"), "go")

    def test_the_stem_survives(self):
        """Which is the whole point — without the rule the whole form would go."""
        for word, sub in [("goṇī", "i"), ("vāk", "g"), ("labh", "p")]:
            self.assertTrue(
                A.replace_antya(word, sub).startswith(word[0]), word
            )
            self.assertTrue(A.replace_antya(word, sub).endswith(sub), word)

    def test_an_empty_form_yields_the_substitute(self):
        self.assertEqual(A.replace_antya("", "a"), "a")
        self.assertIsNone(A.antya(""))


class Registration(unittest.TestCase):
    IDS = ("1.1.49", "1.1.50", "1.1.51", "1.1.52")

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_with_an_executable_rule(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)
            self.assertTrue(sutra.codification, sutra_id)

    def test_the_anuvrtti_from_1_1_49_is_recorded_where_the_corpus_has_it(self):
        """1.1.51 and 1.1.52 both read षष्ठी and स्थाने in from 1.1.49."""
        for sutra_id in ("1.1.51", "1.1.52"):
            carried = " ".join(self.registry.get(sutra_id).anuvrtti)
            self.assertIn("1.1.49", carried, sutra_id)

    def test_the_l_question_is_closed_and_the_varttika_cited(self):
        """
        It stood OPEN until the vārttika collection was read. The record must
        show the answer and where it came from, or the next reader cannot tell
        a settled point from a guess.
        """
        notes = self.registry.get("1.1.51").notes
        self.assertNotIn("OPEN", notes)
        self.assertIn("लपर इति वक्तव्यम्", notes)

    def test_the_varttika_is_in_the_apparatus_for_this_sutra(self):
        from src.astadhyayi.sutra import Source, Status

        reading = self.registry.get("1.1.51").reading(Source.VARTTIKA)
        self.assertIs(reading.status, Status.VERIFIED)
        self.assertIn("लपर", reading.text)


if __name__ == "__main__":
    unittest.main()
