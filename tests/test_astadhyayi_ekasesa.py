# -*- coding: utf-8 -*-
"""
Tests for 1.2.47 to 1.2.73 — the close of the second pāda.

Four unlike things end up here, and each needs a different kind of test.

  1.2.47–1.2.50   operations on a stem, so the test is the output form
  1.2.51–1.2.52   what a लुप्-form carries over, so gender and number
  1.2.53–1.2.57   five sūtras that prescribe nothing at all
  1.2.58–1.2.73   number, and which of several coordinated words survives

The अशिष्य five are the odd ones. They withdraw teachings rather than give
them, and one of them withdraws a rule Pāṇini himself gave two sūtras earlier.
There is no form to check, so what is tested is that the codification does not
pretend otherwise — and that the four positions it records are the four the
Kāśikā attributes.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.ekasesa import (
    NAPUMSAKA,
    PUMS,
    STRI,
    Word,
    ekasesa,
    is_tyadadi,
    number_for,
    sarvadi,
    tyadadi,
)
from src.astadhyayi.luk import ASISYA, asisya, hrasva, is_asisya, yuktavat
from src.astadhyayi.sutra import REGISTRY


class Shortening(unittest.TestCase):
    """1.2.47 to 1.2.50, most specific first."""

    def test_a_neuter_stem_shortens_its_final(self):
        self.assertEqual(hrasva("atirai", napumsaka=True).form, "atiri")
        self.assertEqual(hrasva("atinau", napumsaka=True).form, "atinu")

    def test_but_only_a_neuter_and_only_a_stem(self):
        """नपुंसक इति किम्? ग्रामणीः, सेनानीः — masculine, and untouched."""
        for stem in ("grāmaṇī", "senānī"):
            outcome = hrasva(stem)
            self.assertEqual(outcome.form, stem)
            self.assertFalse(outcome.changed)

    def test_a_subordinate_go_or_feminine_shortens_too(self):
        self.assertEqual(
            hrasva("citragū", upasarjana=True, ends_in_go=True).form, "citragu")
        self.assertEqual(
            hrasva("atikhaṭvā", upasarjana=True, stri_pratyaya=True).form,
            "atikhaṭva")

    def test_but_not_where_the_feminine_is_the_head(self):
        """उपसर्जनस्येति किम्? राजकुमारी."""
        outcome = hrasva("rājakumārī", stri_pratyaya=True)
        self.assertEqual(outcome.form, "rājakumārī")
        self.assertFalse(outcome.changed)

    def test_a_dropped_taddhita_drops_the_feminine_instead(self):
        """पूर्वेण ह्रस्वत्वे प्राप्ते लुग् विधीयते — 1.2.49 displaces 1.2.48."""
        outcome = hrasva("āmalakī", upasarjana=True, stri_pratyaya=True,
                         taddhita_luk=True)
        self.assertEqual(outcome.form, "āmalak")
        self.assertEqual(outcome.by, "1.2.49")

    def test_and_goni_displaces_that_in_turn(self):
        """पूर्वेण लुकि प्राप्ते इकारो विधीयते — 1.2.50 over 1.2.49."""
        outcome = hrasva("goṇī", upasarjana=True, stri_pratyaya=True,
                         taddhita_luk=True, ends_in_goni=True)
        self.assertEqual(outcome.form, "goṇi")
        self.assertEqual(outcome.by, "1.2.50")

    def test_the_four_are_tested_in_the_order_the_kasika_argues_for(self):
        """
        Each of the last three says of the one before it पूर्वेण … प्राप्ते,
        'where the earlier would have applied'. So the same stem under
        successively more conditions must give successively later sūtras, and
        never the other way round.
        """
        stem = dict(stem="goṇī", upasarjana=True, stri_pratyaya=True)
        self.assertEqual(hrasva(**stem).by, "1.2.48")
        self.assertEqual(hrasva(**stem, taddhita_luk=True).by, "1.2.49")
        self.assertEqual(
            hrasva(**stem, taddhita_luk=True, ends_in_goni=True).by, "1.2.50")


class Yuktavat(unittest.TestCase):
    """1.2.51 and 1.2.52."""

    def test_a_lup_form_keeps_the_gender_and_number_it_had(self):
        """पञ्चालाः, masculine plural of the people, so of the country too."""
        carried = yuktavat(gender=PUMS, number=3)
        self.assertEqual((carried.gender, carried.number), (PUMS, 3))
        self.assertEqual(carried.by, "1.2.51")

    def test_but_not_under_luk(self):
        """
        लुपीति किम्? लुकि मा भूत् — लवणः सूपः, लवणा यवागूः, लवणं शाकम्. The two
        elisions are different saṃjñās and only one is meant.
        """
        self.assertEqual(yuktavat(gender=PUMS, number=3, lup=False).by, "—")

    def test_the_qualifiers_follow(self):
        self.assertEqual(yuktavat(gender=PUMS, number=3, qualifier=True).by,
                         "1.2.52")

    def test_except_the_class_word_and_what_agrees_with_it(self):
        """
        अजातेरिति किम्? पञ्चालाः जनपदः. And the exception spreads —
        जातिद्वारेण यानि विशेषणानि तेषामपि युक्तवद्भावो न भवति.
        """
        carried = yuktavat(gender=PUMS, number=3, qualifier=True, jati=True)
        self.assertIsNone(carried.number)
        self.assertEqual(carried.by, "1.2.52")


class Asisya(unittest.TestCase):
    """1.2.53 to 1.2.57 — five sūtras that prescribe nothing."""

    def test_there_are_five_and_each_names_a_reason(self):
        self.assertEqual(len(ASISYA), 5)
        for entry in ASISYA:
            self.assertTrue(entry.reason, entry.sutra)
            self.assertTrue(entry.whose, entry.sutra)
            self.assertGreater(len(entry.explanation), 100, entry.sutra)

    def test_they_cover_1_2_53_to_1_2_57_exactly(self):
        self.assertEqual(
            sorted(entry.sutra for entry in ASISYA),
            ["1.2.53", "1.2.54", "1.2.55", "1.2.56", "1.2.57"],
        )

    def test_1_2_53_withdraws_a_rule_panini_gave_two_sutras_earlier(self):
        """
        Which is the striking thing about it, and the Kāśikā says so at 1.2.51
        itself: तदीयमेवेदं सूत्रम्, तथा चास्य प्रत्याख्यानं भविष्यति — the sūtra
        is the earlier teachers' and will be rejected.
        """
        entry = asisya("yuktadbhāva")[0]
        self.assertEqual(entry.sutra, "1.2.53")
        self.assertIn("1.2.51", entry.whose)
        self.assertIn("तदीयमेवेदं सूत्रम्", REGISTRY.get("1.2.51").notes)

    def test_two_of_them_share_a_reason_and_the_sutra_says_so(self):
        """तुल्यशब्दो हेत्वनुकर्षणार्थः — the तुल्यम् carries 1.2.56's ground over."""
        for topic in ("how-a-compound-divides-its-meaning",
                      "the-definitions-of-today-and-of-upasarjana"):
            self.assertIn("अर्थस्यान्यप्रमाणत्वात्", asisya(topic)[0].reason)

    def test_four_of_the_five_are_aimed_at_the_earlier_teachers(self):
        aimed = [e for e in ASISYA if "पूर्वाचार्य" in e.whose
                 or "1.2.51" in e.whose or "4.2.8" in e.whose]
        self.assertEqual(len(aimed), 4)

    def test_the_odd_one_out_argues_instead_of_asserting(self):
        """
        1.2.55 is the only one that gives an argument rather than a ground,
        and the argument is falsifiable on its face: if the word named the
        connection it would lapse when the connection did.
        """
        entry = asisya("the-argument-for-it")[0]
        self.assertEqual(entry.sutra, "1.2.55")
        self.assertIn("दृश्यते", entry.explanation)

    def test_an_unknown_topic_gets_nothing_rather_than_a_guess(self):
        self.assertEqual(asisya("compound-formation"), ())
        self.assertFalse(is_asisya("compound-formation"))

    def test_the_record_says_it_performs_nothing(self):
        notes = REGISTRY.get("1.2.53").notes
        self.assertIn("IMPLEMENTATION", notes)
        self.assertIn("declines to prescribe", notes)


class Numbers(unittest.TestCase):
    """1.2.58 to 1.2.63."""

    def test_a_class_name_for_one_may_take_the_plural(self):
        verdict = number_for(counted=1, jati=True)
        self.assertEqual(verdict.numbers, (1, 3))
        self.assertTrue(verdict.optional)

    def test_but_not_with_a_numeral(self):
        """संख्याप्रयोगे प्रतिषेधः — एको व्रीहिः संपन्नः सुभिक्षं करोति."""
        self.assertEqual(
            number_for(counted=1, jati=True, with_numeral=True).numbers, (1,))

    def test_and_not_for_a_word_that_names_no_class(self):
        """देवदत्तः, यज्ञदत्तः."""
        self.assertEqual(number_for(counted=1).numbers, (1,))

    def test_asmad_may_take_the_plural_for_one_or_two(self):
        self.assertEqual(number_for(counted=1, asmad=True).numbers, (1, 3))
        self.assertEqual(number_for(counted=2, asmad=True).numbers, (2, 3))

    def test_the_star_rules_name_particular_stars(self):
        """
        Which is most of what they do. फल्गुन्यौ माणविके and पुनर्वसू माणवकौ
        are both counter-examples about the same words used of people, so a
        codification that only asked 'is a pair of stars meant' would pass
        its examples and fail its counter-examples.
        """
        self.assertEqual(
            number_for(counted=2, star="phalgunī", nakshatra=True).numbers,
            (2, 3))
        self.assertEqual(number_for(counted=2, star="phalgunī").numbers, (2,))
        self.assertEqual(
            number_for(counted=2, star="punarvasū", nakshatra=True).numbers,
            (2,))

    def test_the_vedic_singular_is_two_sutras_differing_only_in_the_star(self):
        for star, sutra in (("punarvasū", "1.2.61"), ("viśākhā", "1.2.62")):
            verdict = number_for(counted=2, star=star, nakshatra=True,
                                 chandas=True)
            self.assertEqual(verdict.numbers, (1, 2), star)
            self.assertEqual(verdict.by, sutra, star)

    def test_and_only_in_the_veda(self):
        """छन्दसीति किम्? पुनर्वसू इति, outside it, keeps the dual."""
        self.assertEqual(
            number_for(counted=2, star="punarvasū", nakshatra=True).numbers,
            (2,))

    def test_tisya_and_punarvasu_make_three_and_take_the_dual(self):
        verdict = number_for(counted=3, nakshatra=True,
                             dvandva_of=("tiṣya", "punarvasū"))
        self.assertEqual(verdict.numbers, (2,))
        self.assertEqual(verdict.by, "1.2.63")
        self.assertFalse(verdict.optional, "नित्यग्रहणं विकल्पनिवृत्त्यर्थम्")

    def test_but_not_of_boys_of_those_names(self):
        """तिष्यश्च माणवकः पुनर्वसू माणवकौ तिष्यपुनर्वसवो माणवकाः."""
        self.assertEqual(
            number_for(counted=3, dvandva_of=("tiṣya", "punarvasū")).numbers,
            (3,))


class Tyadadi(unittest.TestCase):
    """1.2.72's group is read off 1.1.27's gaṇa, not listed."""

    def test_it_is_the_tail_of_sarvadi_from_tyad(self):
        self.assertEqual(len(sarvadi()), 35)
        self.assertEqual(sarvadi()[23], "tyad")
        self.assertEqual(tyadadi(), sarvadi()[23:])
        self.assertEqual(len(tyadadi()), 12)
        self.assertEqual(tyadadi()[-1], "kim")

    def test_the_twelve_are_the_pronouns_and_the_two_numerals(self):
        self.assertEqual(
            tyadadi(),
            ("tyad", "tad", "yad", "etad", "idam", "adas", "eka", "dvi",
             "yuṣmad", "asmad", "bhavatu", "kim"),
        )

    def test_a_sarvadi_word_before_tyad_is_not_one(self):
        """सर्व and विश्व are सर्वादि but not त्यदादि, which is the point of the name."""
        for word in ("sarva", "viśva", "ubha", "pūrva"):
            self.assertIn(word, sarvadi(), word)
            self.assertFalse(is_tyadadi(word), word)


class Ekasesa(unittest.TestCase):
    """1.2.64 to 1.2.73 — which of several coordinated words remains."""

    def test_two_of_the_same_form_leave_one(self):
        verdict = ekasesa([Word("vṛkṣa"), Word("vṛkṣa")])
        self.assertEqual(verdict.remaining.form, "vṛkṣa")
        self.assertEqual(verdict.number, 2)
        self.assertEqual(verdict.by, "1.2.64")

    def test_three_of_the_same_form_leave_one_in_the_plural(self):
        self.assertEqual(ekasesa([Word("vṛkṣa")] * 3).number, 3)

    def test_two_of_different_form_leave_both(self):
        """सरूपाणामिति किम्? प्लक्षन्यग्रोधाः."""
        self.assertIsNone(
            ekasesa([Word("plakṣa"), Word("nyagrodha")]).remaining)

    def test_the_words_must_stand_in_one_case(self):
        """एकविभक्ताविति किम्? पयः पयो जरयति."""
        verdict = ekasesa([Word("payas", case=1), Word("payas", case=2)])
        self.assertIsNone(verdict.remaining)
        self.assertEqual(verdict.by, "1.2.64")

    def test_the_gotra_name_survives_its_descendant(self):
        verdict = ekasesa([
            Word("gārgya", gotra="vṛddha"),
            Word("gārgya", form="gārgyāyaṇa", gotra="yuvan"),
        ])
        self.assertEqual(verdict.remaining.form, "gārgya")
        self.assertEqual(verdict.by, "1.2.65")

    def test_1_2_65_needs_all_four_of_its_words(self):
        """
        वृद्ध, यूना, तल्लक्षण and एव each earn a counter-example in the
        Kāśikā, and a codification that dropped any one of them would still
        pass गार्ग्यौ.
        """
        yuvan = Word("gārgya", form="gārgyāyaṇa", gotra="yuvan")
        for label, pair in [
            ("garga is not vṛddha",
             [Word("garga", form="garga"), yuvan]),
            ("both vṛddha",
             [Word("gārgya", gotra="vṛddha"), Word("gārgya", gotra="vṛddha")]),
            ("different stems",
             [Word("gārgya", gotra="vṛddha"),
              Word("vātsya", form="vātsyāyana", gotra="yuvan")]),
            ("another difference besides",
             [Word("bhāgavitti", gotra="vṛddha", other_difference=True),
              Word("bhāgavitti", form="bhāgavittika", gotra="yuvan",
                   other_difference=True)]),
        ]:
            with self.subTest(label):
                self.assertNotEqual(ekasesa(pair).by, "1.2.65", label)

    def test_a_feminine_elder_survives_and_takes_the_masculine_form(self):
        verdict = ekasesa([
            Word("gārgya", form="gārgī", gender=STRI, gotra="vṛddha"),
            Word("gārgya", form="gārgyāyaṇa", gotra="yuvan"),
        ])
        self.assertEqual(verdict.by, "1.2.66")
        self.assertEqual(verdict.remaining.gender, STRI)
        self.assertEqual(verdict.behaves_as, PUMS)

    def test_otherwise_the_masculine_survives(self):
        verdict = ekasesa([
            Word("brāhmaṇa"),
            Word("brāhmaṇa", form="brāhmaṇī", gender=STRI),
        ])
        self.assertEqual(verdict.remaining.gender, PUMS)
        self.assertEqual(verdict.by, "1.2.67")

    def test_1_2_67s_three_counter_examples(self):
        for label, pair in [
            ("kukkuṭamayūryau — different stems",
             [Word("kukkuṭa"), Word("mayūra", form="mayūrī", gender=STRI)]),
            ("indrendrāṇyau — a second difference, by 4.1.48",
             [Word("indra"),
              Word("indra", form="indrāṇī", gender=STRI,
                   other_difference=True)]),
        ]:
            with self.subTest(label):
                self.assertIsNone(ekasesa(pair).remaining, label)

    def test_the_kinship_pairs_are_paired_respectively(self):
        """भ्रातृपुत्रौ स्वसृदुहितृभ्याम् — यथासंख्यम्, which is 1.3.10's."""
        for keeps, drops in (("bhrātṛ", "svasṛ"), ("putra", "duhitṛ")):
            verdict = ekasesa([
                Word(keeps, kinship=keeps),
                Word(drops, kinship=drops, gender=STRI),
            ])
            self.assertEqual(verdict.remaining.kinship, keeps)
            self.assertEqual(verdict.by, "1.2.68")

    def test_and_not_paired_across(self):
        """
        भ्रातृ against दुहितृ is not what the sūtra says. यथासंख्यम् pairs
        first with first and second with second, and getting that wrong is
        the mistake 1.3.10 exists to prevent.
        """
        verdict = ekasesa([
            Word("bhrātṛ", kinship="bhrātṛ"),
            Word("duhitṛ", kinship="duhitṛ", gender=STRI),
        ])
        self.assertNotEqual(verdict.by, "1.2.68")

    def test_the_neuter_survives_and_may_go_singular(self):
        verdict = ekasesa([
            Word("śukla"), Word("śukla", gender=STRI),
            Word("śukla", gender=NAPUMSAKA),
        ])
        self.assertEqual(verdict.by, "1.2.69")
        self.assertEqual(verdict.number, 1)
        self.assertTrue(verdict.optional)

    def test_but_three_neuters_together_do_not(self):
        """अनपुंसकेनेति किम्? शुक्लानि, and एकवच् च इति न भवति."""
        verdict = ekasesa([Word("śukla", gender=NAPUMSAKA)] * 3)
        self.assertEqual(verdict.by, "1.2.64")
        self.assertEqual(verdict.number, 3)

    def test_the_two_optional_kinship_pairs(self):
        for keeps, drops, sutra in (("pitṛ", "mātṛ", "1.2.70"),
                                    ("śvaśura", "śvaśrū", "1.2.71")):
            verdict = ekasesa([
                Word(keeps, kinship=keeps),
                Word(drops, kinship=drops, gender=STRI),
            ])
            self.assertEqual(verdict.by, sutra)
            self.assertTrue(verdict.optional, sutra)

    def test_a_tyadadi_word_survives_against_anything_and_not_optionally(self):
        verdict = ekasesa([Word("tad"), Word("devadatta")])
        self.assertEqual(verdict.remaining.stem, "tad")
        self.assertEqual(verdict.by, "1.2.72")
        self.assertFalse(verdict.optional)

    def test_of_two_tyadadi_the_later_in_the_gana_survives(self):
        """
        त्यदादीनां मिथो यद् यत् परं तत् तच्छिष्यते. 'Later' means later in
        1.1.27's list, which is checkable: यद् comes after तद् and किम् after
        यद्, so स च यश्च gives यौ and यश्च कश्च gives कौ.
        """
        self.assertEqual(ekasesa([Word("tad"), Word("yad")]).remaining.stem,
                         "yad")
        self.assertEqual(ekasesa([Word("yad"), Word("kim")]).remaining.stem,
                         "kim")
        self.assertLess(tyadadi().index("tad"), tyadadi().index("yad"))
        self.assertLess(tyadadi().index("yad"), tyadadi().index("kim"))

    def test_the_feminine_survives_for_a_herd_of_grown_domestic_animals(self):
        herd = dict(gramya=True, pasu=True, sangha=True)
        verdict = ekasesa([
            Word("go", gender=STRI, **herd), Word("go", **herd),
        ])
        self.assertEqual(verdict.remaining.gender, STRI)
        self.assertEqual(verdict.by, "1.2.73")

    def test_and_each_of_its_five_conditions_is_load_bearing(self):
        """
        Four counter-examples in the Kāśikā and one in the vārttika, and each
        falls back to 1.2.67 rather than to nothing — रुरव इमे and अश्वा इमे
        are masculine plurals, which is what 1.2.67 gives.
        """
        base = dict(gramya=True, pasu=True, sangha=True)
        for label, change in [
            ("wild — रुरव इमे", dict(gramya=False)),
            ("not animals — ब्राह्मणाः", dict(pasu=False)),
            ("not a herd — एतौ गावौ चरतः", dict(sangha=False)),
            ("young — वत्सा इमे", dict(taruna=True)),
            ("single-hoofed — अश्वा इमे", dict(aneka_shapha=False)),
        ]:
            with self.subTest(label):
                where = {**base, **change}
                verdict = ekasesa([
                    Word("x", gender=STRI, **where), Word("x", **where),
                ])
                self.assertEqual(verdict.by, "1.2.67", label)
                self.assertEqual(verdict.remaining.gender, PUMS, label)

    def test_a_single_word_has_nothing_to_retain(self):
        self.assertEqual(ekasesa([Word("vṛkṣa")]).by, "—")
        self.assertIsNone(ekasesa([]).remaining)


class Registration(unittest.TestCase):
    def test_the_second_pada_is_complete(self):
        missing = [f"1.2.{n}" for n in range(1, 74) if not REGISTRY.has(f"1.2.{n}")]
        self.assertEqual(missing, [])

    def test_and_so_is_the_whole_of_adhyaya_one_but_for_the_fourth_pada(self):
        for pada, count in (("1.1", 75), ("1.2", 73), ("1.3", 93)):
            missing = [n for n in range(1, count + 1)
                       if not REGISTRY.has(f"{pada}.{n}")]
            self.assertEqual(missing, [], pada)

    def test_1_2_68_records_that_it_calls_1_3_10(self):
        """
        The pairing is यथासंख्यम् and that rule is already codified, so it is
        called rather than repeated. The record should say so, since a reader
        checking whether the codification duplicates itself needs to see it.
        """
        self.assertIn("1.3.10", REGISTRY.get("1.2.68").notes)

    def test_1_2_72_records_that_its_gana_is_read_from_1_1_27(self):
        notes = REGISTRY.get("1.2.72").notes
        self.assertIn("1.1.27", notes)
        self.assertIn("twenty-fourth", notes)


if __name__ == "__main__":
    unittest.main()
