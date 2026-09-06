# -*- coding: utf-8 -*-
"""
८.१.१–१५ — सर्वस्य द्वे, the heading अध्याय ८ opens on.

Fifteen sūtras, and almost every one of them names a SENSE
rather than a form. The tests take the senses one by one, and
the class that matters most is the one about what the doubled
pair then counts as — a बहुव्रीहि by two rules and a कर्मधारय
by the heading that displaces them.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.amredita import (
    ADHIKARA_TO,
    AMANTRITA_FIVE,
    DVANDVA_FIVE,
    DVE_RUN,
    DVE_TABLE,
    PADA_PURANA,
    SAMIPYA_THREE,
    doubles,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheHeadingItself(unittest.TestCase):
    """8.1.1, and what it settles before anything is doubled."""

    def test_the_heading_stops_before_the_next_one(self):
        # प्राक् पदस्य इत्यतः — 8.1.16 opens पदस्य and this
        # heading does not reach it.
        self.assertEqual(DVE_RUN, ("8.1.1", "8.1.15"))
        self.assertEqual(ADHIKARA_TO, "8.1.15")
        self.assertIn("प्राक् पदस्य",
                      provisions_for("8.1.1")[0].why)

    def test_and_it_settles_what_the_second_copy_is(self):
        # ये शब्दतश् च अर्थतश् च उभयथा अन्तरतमे — nearest in
        # sound AND in sense, both at once, which is what stops
        # the substitution rule putting any word for any other.
        why = provisions_for("8.1.1")[0].why
        self.assertIn("शब्दतश्", why)
        self.assertIn("अर्थतश्", why)
        self.assertIn("उभयथा", why)

    def test_and_this_doubling_is_not_the_one_adhyaya_seven_used(self):
        # 6.1.1 एकाचो द्वे प्रथमस्य copies ONE syllable; सर्वस्य
        # द्वे copies the whole word. Both are codified, and the
        # note says in so many words that they share a name and
        # nothing else.
        self.assertTrue(REGISTRY.has("6.1.1"))
        self.assertIn("6.1.1", provisions_for("8.1.1")[0].why)

    def test_but_a_pure_heading_answers_nothing(self):
        # 8.1.1 and 8.1.11 are both stated of everything that
        # follows and of nothing in particular. Neither is
        # reachable, and a query in the sense 8.1.1 governs is
        # answered by the rule that names that sense.
        for row in DVE_TABLE:
            if not row.heading:
                continue
            self.assertNotEqual(
                doubles(sense="nitya").sutra, row.sutra, row.sutra)
            self.assertNotEqual(
                doubles(gana="guṇavacana", sense="prakāra").sutra,
                row.sutra, row.sutra)


class TheNameAndTheAccent(unittest.TestCase):
    """8.1.2–3, which turn two words into one."""

    def test_the_later_copy_is_called_amredita(self):
        # चौरचौर, वृषलवृषल, दस्योदस्यो.
        got = doubles(gana="dvirukta-para")
        self.assertEqual(got.sutra, "8.1.2")
        self.assertEqual(got.does, "saṃjñā")

    def test_and_the_name_reaches_a_rule_a_pada_later(self):
        # आम्रेडितप्रदेशाः — आम्रेडितं भर्त्सने इत्येवमादयः. That
        # rule has landed with पाद ८.२, so the name given here
        # and the प्लुत that uses it can be asked of the engine
        # together: one pāda doubles the word and the next
        # lengthens the copy.
        self.assertIn("8.2.95", provisions_for("8.1.2")[0].why)
        self.assertTrue(REGISTRY.has("8.2.95"))

    def test_and_what_carries_that_name_loses_its_accent(self):
        # भुङ्क्तेभुङ्क्ते, पशून्पशून् — one high tone across
        # the pair, which is what makes it one word to the ear.
        got = doubles(gana="āmreḍita")
        self.assertEqual(got.sutra, "8.1.3")
        self.assertEqual(got.does, "anudātta")


class TheSensesThatDouble(unittest.TestCase):
    """8.1.4–8, where the sense is the whole rule."""

    def test_constancy_and_distribution_both_double(self):
        # पचतिपचति of constancy; ग्रामोग्रामो रमणीयः of
        # distribution.
        for sense in ("nitya", "vīpsā"):
            got = doubles(sense=sense)
            self.assertEqual(got.sutra, "8.1.4", sense)
            self.assertEqual(got.does, "dve", sense)

    def test_and_the_vrtti_says_where_constancy_can_live(self):
        # तिङ्षु नित्यता अव्ययकृत्सु च, because आभीक्ष्ण्यं
        # क्रियाधर्मः — constancy is a property of an action.
        why = provisions_for("8.1.4")[0].why
        self.assertIn("क्रियाधर्मः", why)
        self.assertIn("अनुपरमन्", why)

    def test_pari_doubles_of_exclusion_and_not_of_anything_else(self):
        # परिपरि त्रिगर्तेभ्यो वृष्टो देवः; ओदनं परिषिञ्चति.
        got = doubles("pari", sense="varjana")
        self.assertEqual(got.sutra, "8.1.5")
        self.assertIn("परिषिञ्चति",
                      provisions_for("8.1.5")[0].keeps_out)
        self.assertNotEqual(doubles("pari").sutra, "8.1.5")

    def test_and_a_compound_has_said_the_exclusion_already(self):
        # समासे तु तेनैव उक्तत्वाद् वर्जनस्य नैव भवति —
        # परित्रिगर्तं वृष्टो देवः cannot double at all.
        why = provisions_for("8.1.5")[0].why
        self.assertIn("उक्तत्वाद्", why)
        # वर्जने + असमासे elides the अ, so the quoted fragment
        # has to begin after the अवग्रह: वर्जनेऽसमासे.
        self.assertIn("समासे वा", why)

    def test_four_preverbs_double_to_fill_a_metrical_quarter(self):
        # प्रप्रायम् अग्निः, संसमिद् युवसे, उपोप मे, नो दुदु.
        self.assertEqual(PADA_PURANA, ("pra", "sam", "upa", "ud"))
        for word in PADA_PURANA:
            got = doubles(word, sense="pāda-pūraṇa", chandasi=True)
            self.assertEqual(got.sutra, "8.1.6", word)

    def test_and_the_veda_is_read_out_of_the_rules_own_sense(self):
        # सामर्थ्यात् छन्दसि एव एतद् विधानम् — no word in the
        # sūtra says छन्दसि, and ordinary speech has no quarters.
        self.assertIn("सामर्थ्यात्", provisions_for("8.1.6")[0].why)
        self.assertNotEqual(
            doubles("pra", sense="pāda-pūraṇa").sutra, "8.1.6")

    def test_three_words_double_of_nearness_and_not_of_height(self):
        # उपर्युपरि ग्रामम्; उपरि शिरसो घटं धारयति.
        self.assertEqual(len(SAMIPYA_THREE), 3)
        for word in SAMIPYA_THREE:
            self.assertEqual(
                doubles(word, sense="sāmīpya").sutra, "8.1.7", word)
        self.assertIn("औत्तराधर्य",
                      provisions_for("8.1.7")[0].keeps_out)

    def test_a_vocative_doubles_in_five_senses_at_a_sentences_head(self):
        # माणवक३ माणवक of envy, and four more.
        self.assertEqual(len(AMANTRITA_FIVE), 5)
        for sense in AMANTRITA_FIVE:
            got = doubles(gana="āmantrita", position="vākya-ādi",
                          sense=sense)
            self.assertEqual(got.sutra, "8.1.8", sense)
        self.assertNotEqual(
            doubles(gana="āmantrita", sense="asūyā").sutra, "8.1.8")

    def test_and_all_five_are_the_speakers_and_none_the_hearers(self):
        # एते च प्रयोक्तृधर्माः, न अभिधेयधर्माः — nothing about
        # the boy makes the vocative double.
        self.assertIn("प्रयोक्तृधर्माः",
                      provisions_for("8.1.8")[0].why)


class WhatThePairCountsAs(unittest.TestCase):
    """8.1.9–11, a बहुव्रीहि twice and then a कर्मधारय."""

    def test_eka_and_distress_both_act_like_a_bahuvrihi(self):
        # एकैकम् अक्षरं पठति; गतगतः, नष्टनष्टः.
        self.assertEqual(doubles("eka").like, "bahuvrīhi")
        self.assertEqual(doubles(sense="ābādha").like, "bahuvrīhi")

    def test_and_the_likeness_buys_two_things_and_not_five(self):
        # सुब्लोपपुंवद्भावौ, and NOT the pronoun refusal, the
        # accent or the compound endings — एकैकस्मै keeps its
        # pronoun ending, and 1.1.29 is codified.
        why = provisions_for("8.1.9")[0].why
        self.assertIn("सुब्लोपपुंवद्भावौ", why)
        self.assertIn("आतिदेशिके", why)
        self.assertTrue(REGISTRY.has("1.1.29"))

    def test_but_from_the_next_sutra_it_is_a_karmadharaya(self):
        # पटुपटुः, पटुपट्वी, कालककालिका — and the accent besides.
        for row in DVE_TABLE:
            if row.sutra in ("8.1.9", "8.1.10"):
                self.assertEqual(row.like, "bahuvrīhi", row.sutra)
            elif row.like:
                self.assertEqual(row.like, "karmadhāraya", row.sutra)

    def test_and_that_heading_buys_one_thing_more(self):
        # सुब्लोपपुंवद्भावान्तोदात्तत्वानि — the accent on the
        # last syllable is what 8.1.9's likeness did not give.
        why = provisions_for("8.1.11")[0].why
        # पुंवद्भाव + अन्तोदात्तत्व merges its two vowels, so
        # the fragment begins inside the second word.
        self.assertIn("न्तोदात्तत्वानि", why)
        self.assertIn("6.3.42", why)
        self.assertTrue(REGISTRY.has("6.3.42"))

    def test_and_every_rule_after_it_carries_the_likeness(self):
        def number(code):
            return int(code.rsplit(".", 1)[1])

        for row in DVE_TABLE:
            if number(row.sutra) > number("8.1.11"):
                self.assertEqual(row.like, "karmadhāraya", row.sutra)


class TheLastFour(unittest.TestCase):
    """8.1.12–15, a quality, an ease, and two laid-down words."""

    def test_a_quality_word_doubles_of_a_sort(self):
        # पटुपटुः — अपरिपूर्णगुण, not quite clever.
        got = doubles(gana="guṇavacana", sense="prakāra")
        self.assertEqual(got.sutra, "8.1.12")
        self.assertIn("अपरिपूर्णगुण",
                      provisions_for("8.1.12")[0].why)

    def test_and_it_does_not_displace_the_affix_that_says_the_same(self):
        # जातीयरः अनेन द्विर्वचनेन बाधनं न इष्यते — पटुजातीयः
        # stands beside पटुपटुः, on an option borrowed forward
        # from the sūtra after.
        self.assertIn("जातीयरः", provisions_for("8.1.12")[0].why)

    def test_two_words_double_optionally_of_ease(self):
        # प्रियप्रियेण ददाति; प्रियः पुत्रः.
        for word in ("priya", "sukha"):
            got = doubles(word, sense="akṛcchra")
            self.assertEqual(got.sutra, "8.1.13", word)
            self.assertTrue(got.optional, word)
        self.assertIn("सुखो रथः",
                      provisions_for("8.1.13")[0].keeps_out)

    def test_one_word_is_laid_down_with_a_gender_it_had_no_claim_to(self):
        # यथायथम् — the doubling AND the neuter, neither of
        # which any rule supplies.
        got = doubles("yathāyatham", sense="yathāsva")
        self.assertEqual(got.sutra, "8.1.14")
        self.assertTrue(got.nipatana)
        self.assertIn("नपुंसकलिङ्गता",
                      provisions_for("8.1.14")[0].why)

    def test_and_the_last_takes_three_departures_in_one_word(self):
        # द्विशब्दस्य द्विर्वचनम्, पूर्वपदस्य आम्भावः, अत्वं च
        # उत्तरपदस्य — द्वि doubled gives द्वन्द्वम्.
        got = doubles("dvandvam", sense="rahasya")
        self.assertEqual(got.sutra, "8.1.15")
        self.assertTrue(got.nipatana)
        why = provisions_for("8.1.15")[0].why
        for departure in ("द्विर्वचनम्", "आम्भावः", "अत्वं"):
            self.assertIn(departure, why, departure)

    def test_and_only_one_of_its_five_senses_is_what_it_means(self):
        # रहस्यं द्वन्द्वशब्दवाच्यम्, इतरे विषयभूताः.
        self.assertEqual(len(DVANDVA_FIVE), 5)
        self.assertEqual(DVANDVA_FIVE[0], "rahasya")
        self.assertIn("विषयभूताः", provisions_for("8.1.15")[0].why)
        for sense in DVANDVA_FIVE:
            self.assertEqual(
                doubles("dvandvam", sense=sense).sutra, "8.1.15",
                sense)


class NothingHappensByDefault(unittest.TestCase):
    """A word no rule of the run names is said once."""

    def test_an_unnamed_word_in_no_named_sense_reaches_nothing(self):
        got = doubles("vṛkṣa")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")
        self.assertIn("said once", got.why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_opens_the_adhyaya(self):
        codes = [row.sutra for row in DVE_TABLE]
        self.assertEqual(
            codes, ["8.1.%d" % n for n in range(1, 16)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in DVE_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_the_rules_reached_ahead_in_this_adhyaya_survive(self):
        # 8.2.1, 8.2.2, 8.2.3, 8.2.66, 8.3.15 and 8.4.55 were
        # codified long before अध्याय ८ was read in order, and
        # this pāda's own module must not disturb them.
        for code in ("8.2.1", "8.2.2", "8.2.3", "8.2.66",
                     "8.3.15", "8.4.55"):
            self.assertTrue(REGISTRY.has(code), code)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_everything_this_run_stands_on_is_live(self):
        # 6.1.1's syllable doubling, which this one is not;
        # 1.1.29's pronoun refusal, which 8.1.9's likeness does
        # not carry; and 6.3.42's पुंवद्भाव, which 8.1.11's does.
        for code in ("6.1.1", "1.1.29", "6.3.42"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_headings_this_run_stops_before_have_landed(self):
        # 8.1.16 पदस्य opens a heading that reaches to 8.3.55,
        # and 8.1.74 closes the pāda. Both are codified, so
        # this run's own bound — प्राक् पदस्य इत्यतः — can be
        # asked of the registry rather than only asserted.
        self.assertTrue(REGISTRY.has("8.1.16"))
        self.assertTrue(REGISTRY.has("8.1.74"))
        # 8.3.55 अपदान्तस्य मूर्धन्यः, where 8.1.16's पदस्य
        # finally stops, has landed too — so the heading this
        # run stops before can be asked end to end.
        self.assertTrue(REGISTRY.has("8.3.55"))


if __name__ == "__main__":
    unittest.main()
