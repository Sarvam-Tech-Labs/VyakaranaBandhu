# -*- coding: utf-8 -*-
"""
८.१.१६–५० — three headings, the निघात, and twenty refusals of it.

The tests take the pāda's shape rather than its numbering: the
headings that answer nothing, the four enclitics, the rule the
whole spoken language turns on, and then the long list of
particles that spare a verb its accent — ending on the pair
8.1.37–38, where a refusal of a refusal comes out as an
assertion and the vṛtti has to say so in words.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.nighata import (
    APADADAU_TO,
    CA_VA_FIVE,
    NIGHATA_RUN,
    NIGHATA_TABLE,
    NIPATA_NINE,
    PADASYA_TO,
    PADAT_TO,
    PUJA_FOUR,
    THE_NIGHATA,
    after_a_pada,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)

#: What a plain finite verb after a noun is asked with.
TIN = {"gana": "tiṅ", "after": "a-tiṅ"}


class ThreeHeadingsAtOnce(unittest.TestCase):
    """8.1.16–18, none of which ends where the pāda does."""

    def test_each_heading_reaches_a_different_place(self):
        # पदस्य to 8.3.55, पदात् to 8.1.68, and the third to the
        # end of the pāda. No two of the three stop together.
        self.assertEqual(PADASYA_TO, "8.3.55")
        self.assertEqual(PADAT_TO, "8.1.68")
        self.assertEqual(APADADAU_TO, "8.1.74")
        self.assertEqual(len({PADASYA_TO, PADAT_TO, APADADAU_TO}), 3)

    def test_the_third_carries_three_words_and_not_one(self):
        # अनुदात्तम् इति च, सर्वम् इति च, अपादादाव् इति च।
        # एतत् त्रयम् अधिकृतम्.
        why = provisions_for("8.1.18")[0].why
        self.assertIn("एतत् त्रयम्", why)
        self.assertIn("आ पादपरिसमाप्तेः", why)

    def test_and_the_genitive_of_the_first_is_read_two_ways(self):
        # क्वचित् स्थानषष्ठी क्वचिद् अवयवषष्ठी — sometimes what
        # a substitute stands for, sometimes the whole a part
        # belongs to.
        why = provisions_for("8.1.16")[0].why
        self.assertIn("स्थानषष्ठी", why)
        self.assertIn("अवयवषष्ठी", why)

    def test_but_none_of_the_three_answers_anything(self):
        for row in NIGHATA_TABLE:
            if not row.heading:
                continue
            for query in (TIN, {"gana": "āmantrita",
                                "after": "pada",
                                "position": "a-pādādi"}):
                self.assertNotEqual(
                    after_a_pada(**query).sutra, row.sutra, row.sutra)

    def test_and_the_headings_are_exactly_the_first_three_rows(self):
        headings = [row.sutra for row in NIGHATA_TABLE if row.heading]
        self.assertEqual(headings, ["8.1.16", "8.1.17", "8.1.18"])


class TheVocativeAndTheEnclitics(unittest.TestCase):
    """8.1.19–26, four substitutes and three refusals."""

    def test_a_vocative_after_a_word_is_toneless_throughout(self):
        # पचसि देवदत्त; देवदत्त पचसि keeps its accent.
        got = after_a_pada(gana="āmantrita", after="pada",
                           position="a-pādādi")
        self.assertEqual(got.sutra, "8.1.19")
        self.assertEqual(got.does, "anudātta")
        self.assertNotEqual(
            after_a_pada(gana="āmantrita",
                         position="a-pādādi").sutra, "8.1.19")

    def test_and_a_varttika_confines_it_to_one_sentence(self):
        # समानवाक्ये निघातयुष्मदस्मदादेशा वक्तव्याः — ओदनं पच
        # तव भविष्यति keeps तव, the clauses being two.
        why = provisions_for("8.1.19")[0].why
        self.assertIn("समानवाक्ये", why)
        self.assertIn("तव भविष्यति", why)

    def test_four_sutras_give_eight_enclitics(self):
        # वाम्, नौ; वस्, नस्; ते, मे; त्वा, मा.
        wanted = {"dvivacana": ("8.1.20", "vām-nau"),
                  "bahuvacana": ("8.1.21", "vas-nas"),
                  "ekavacana": ("8.1.22", "te-me"),
                  "ekavacana-dvitīyā": ("8.1.23", "tvā-mā")}
        for case, (code, does) in wanted.items():
            got = after_a_pada(gana="yuṣmad-asmad", case=case,
                               after="pada", position="a-pādādi")
            self.assertEqual(got.sutra, code, case)
            self.assertEqual(got.does, does, case)

    def test_and_none_of_the_four_has_to_say_they_are_toneless(self):
        # 8.1.18's अनुदात्तम् supplies it, which is what an
        # अधिकार is for.
        for code in ("8.1.20", "8.1.21", "8.1.22", "8.1.23"):
            self.assertNotIn("अनुदात्त",
                             provisions_for(code)[0].why, code)

    def test_the_accusative_singular_is_left_out_on_purpose(self):
        # द्वितीयान्तस्य आदेशान्तरविधानसामर्थ्यात् — because
        # the next sūtra gives it something else.
        self.assertIn("आदेशान्तरविधानसामर्थ्यात्",
                      provisions_for("8.1.22")[0].why)

    def test_and_three_sutras_take_all_four_back(self):
        # 8.1.24 with the five particles, 8.1.25 with a verb of
        # seeing, 8.1.26 optionally after a नाम-headed
        # nominative. Each blocks all four.
        for code in ("8.1.24", "8.1.25", "8.1.26"):
            row = provisions_for(code)[0]
            self.assertTrue(row.refuses, code)
            self.assertEqual(
                set(row.blocks),
                {"8.1.20", "8.1.21", "8.1.22", "8.1.23"}, code)

    def test_the_five_particles_each_keep_the_enclitic_off(self):
        # ग्रामस् तव च स्वम्, and four more.
        self.assertEqual(len(CA_VA_FIVE), 5)
        for particle in CA_VA_FIVE:
            got = after_a_pada(gana="yuṣmad-asmad",
                               case="dvivacana", after="pada",
                               joined=particle,
                               position="a-pādādi")
            self.assertEqual(got.sutra, "8.1.24", particle)
            self.assertTrue(got.refuses, particle)

    def test_and_seeing_means_knowing_and_not_the_eye(self):
        # दर्शनं ज्ञानम्। आलोचनं चक्षुर्विज्ञानम्.
        why = provisions_for("8.1.25")[0].why
        self.assertIn("दर्शनं ज्ञानम्", why)
        self.assertIn("चक्षुर्विज्ञानम्", why)


class TheNighataItself(unittest.TestCase):
    """8.1.28, and 8.1.27 just in front of it."""

    def test_a_finite_verb_after_a_non_verb_loses_its_accent(self):
        # देवदत्तः पचति.
        got = after_a_pada(**TIN)
        self.assertEqual(got.sutra, THE_NIGHATA)
        self.assertEqual(got.sutra, "8.1.28")
        self.assertEqual(got.does, "anudātta")

    def test_and_both_words_of_the_sutra_do_work(self):
        # तिङ् इति किम्? नीलम् उत्पलम्। अतिङः इति किम्? भवति
        # पचति.
        keeps = provisions_for("8.1.28")[0].keeps_out
        self.assertIn("नीलम् उत्पलम्", keeps)
        self.assertIn("भवति पचति", keeps)

    def test_the_gotradi_words_are_toneless_after_a_verb_instead(self):
        # पचति गोत्रम्; पचतिपचति गोत्रम्, where the doubling is
        # 8.1.4's and the two runs of the pāda meet.
        for sense in ("kutsana", "ābhīkṣṇya"):
            got = after_a_pada(gana="gotrādi", after="tiṅ",
                               sense=sense)
            self.assertEqual(got.sutra, "8.1.27", sense)
        self.assertTrue(REGISTRY.has("8.1.4"))

    def test_and_almost_everything_after_it_is_a_refusal_of_it(self):
        def number(code):
            return int(code.rsplit(".", 1)[1])

        after = [row for row in NIGHATA_TABLE
                 if number(row.sutra) > number(THE_NIGHATA)]
        self.assertEqual(len(after), 22)
        holding_off = [row for row in after
                       if THE_NIGHATA in row.blocks]
        self.assertEqual(len(holding_off), 20)


class TheRefusals(unittest.TestCase):
    """8.1.29–36 and 8.1.39–50, the particles that spare a verb."""

    def test_the_periphrastic_future_keeps_its_accent(self):
        # श्वः कर्ता.
        got = after_a_pada(gana="luṭ", after="a-tiṅ")
        self.assertEqual(got.sutra, "8.1.29")
        self.assertTrue(got.refuses)
        self.assertIn(THE_NIGHATA, got.blocked_by)

    def test_nine_particles_spare_it_by_name(self):
        # यत्, यदि, हन्त, कुवित्, नेत्, चेत्, चण्, कच्चित्, यत्र.
        self.assertEqual(len(NIPATA_NINE), 9)
        for particle in NIPATA_NINE:
            got = after_a_pada(joined=particle, **TIN)
            self.assertEqual(got.sutra, "8.1.30", particle)
            self.assertTrue(got.refuses, particle)

    def test_and_five_more_spare_it_only_in_a_named_sense(self):
        # नह of remonstrance, सत्यम् of a question, अङ्ग and हि
        # where nothing contrary is meant, ननु of asking leave.
        wanted = {("naha", "pratyārambha"): "8.1.31",
                  ("satyam", "praśna"): "8.1.32",
                  ("aṅga", "aprātilomya"): "8.1.33",
                  ("hi", "aprātilomya"): "8.1.34",
                  ("nanu", "anujñaiṣaṇā"): "8.1.43"}
        for (particle, sense), code in wanted.items():
            got = after_a_pada(joined=particle, sense=sense, **TIN)
            self.assertEqual(got.sutra, code, particle)
            # and without the sense the refusal does not come
            self.assertNotEqual(
                after_a_pada(joined=particle, **TIN).sutra, code,
                particle)

    def test_the_veda_spares_more_than_one_verb_at_a_time(self):
        # अनृतं हि मत्तो वदति, पाप्मा एनं विपुनाति — neither
        # toneless; and sometimes one only.
        got = after_a_pada(joined="hi", chandasi=True, **TIN)
        self.assertEqual(got.sutra, "8.1.35")
        self.assertIn("कदाचिद् एकं", provisions_for("8.1.35")[0].why)

    def test_and_four_more_spare_it_in_praise(self):
        # तु, पश्य, पश्यत, अह.
        self.assertEqual(len(PUJA_FOUR), 4)
        for particle in PUJA_FOUR:
            got = after_a_pada(joined=particle, sense="pūjā", **TIN)
            self.assertEqual(got.sutra, "8.1.39", particle)

    def test_and_aho_twice_over_in_two_senses(self):
        # अहो in praise compulsorily, अहो elsewhere optionally.
        self.assertEqual(
            after_a_pada(joined="aho", sense="pūjā", **TIN).sutra,
            "8.1.40")
        elsewhere = after_a_pada(joined="aho", sense="śeṣa", **TIN)
        self.assertEqual(elsewhere.sutra, "8.1.41")
        self.assertTrue(elsewhere.optional)

    def test_and_two_sutras_want_the_particle_to_stand_first(self):
        # जातु and the किम्-form with चित् — अपूर्वम्.
        self.assertEqual(
            after_a_pada(joined="jātu", position="a-pūrva",
                         **TIN).sutra, "8.1.47")
        self.assertEqual(
            after_a_pada(gana="kiṃvṛtta", after="a-tiṅ",
                         joined="cit", position="a-pūrva").sutra,
            "8.1.48")
        self.assertNotEqual(
            after_a_pada(joined="jātu", **TIN).sutra, "8.1.47")

    def test_and_the_kim_form_is_read_more_narrowly_than_yadvrtta(self):
        # किम्वृत्तग्रहणेन तद्विभक्त्यन्तं प्रतीयात्, डतरडतमौ च
        # प्रत्ययौ — which is why कतरश्चित् is in the list.
        self.assertIn("डतरडतमौ", provisions_for("8.1.48")[0].why)

    def test_the_pada_has_two_sesa_vibhasas_and_they_do_the_same_thing(self):
        # 8.1.41 for अहो and 8.1.50 for आहो/उताहो — each takes
        # back what the sūtra just before it had confined.
        for code in ("8.1.41", "8.1.50"):
            row = provisions_for(code)[0]
            self.assertTrue(row.optional, code)
            self.assertTrue(row.refuses, code)


class ARefusalOfARefusal(unittest.TestCase):
    """8.1.36–38, the pair the resolver most easily gets wrong."""

    def test_yavat_and_yatha_spare_the_verb(self):
        # यावद् भुङ्क्ते; यथा अधीते.
        for particle in ("yāvat", "yathā"):
            got = after_a_pada(joined=particle, **TIN)
            self.assertEqual(got.sutra, "8.1.36", particle)
            self.assertTrue(got.refuses, particle)

    def test_but_in_praise_and_next_to_it_the_verb_is_toneless(self):
        # यावत् पचति शोभनम् — the refusal is itself refused.
        got = after_a_pada(joined="yāvat", sense="pūjā",
                           position="anantara", **TIN)
        self.assertEqual(got.sutra, "8.1.37")
        self.assertEqual(got.does, "anudātta")
        self.assertFalse(got.refuses)
        self.assertIn("8.1.36", got.blocked_by)

    def test_and_the_vrtti_spells_the_double_negative_out(self):
        # न अनुदात्तं न भवति। किं तर्हि? अनुदात्तम् एव.
        self.assertIn("किं तर्हि? अनुदात्तम् एव",
                      provisions_for("8.1.37")[0].why)

    def test_a_preverb_in_the_gap_does_not_break_it(self):
        # यावत् प्रपचति शोभनम् — the sūtra exists for that gap
        # and for no other.
        got = after_a_pada(joined="yāvat", sense="pūjā",
                           position="upasarga-vyapeta", **TIN)
        self.assertEqual(got.sutra, "8.1.38")
        self.assertIn("उपसर्गव्यवधानार्थोऽयम्",
                      provisions_for("8.1.38")[0].why)

    def test_but_a_whole_word_in_the_gap_does(self):
        # यावद् देवदत्तः पचति शोभनम् — neither 8.1.37 nor
        # 8.1.38 is reached, and 8.1.36 spares the verb again.
        got = after_a_pada(joined="yāvat", sense="pūjā", **TIN)
        self.assertEqual(got.sutra, "8.1.36")
        self.assertTrue(got.refuses)

    def test_and_puja_is_said_twice_over_on_purpose(self):
        # पूजायाम् इति वर्तमाने पुनः पूजायाम् इत्युच्यते
        # निघातप्रतिषेधार्थम् — at 8.1.37 it belongs to an
        # assertion, and at 8.1.39 to a refusal.
        self.assertIn("पुनः पूजायाम्",
                      provisions_for("8.1.39")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A word none of these rules reaches keeps its accent."""

    def test_an_unnamed_word_reaches_nothing(self):
        got = after_a_pada(gana="subanta")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")
        self.assertIn("adhyaya 6", got.why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(NIGHATA_RUN, ("8.1.16", "8.1.50"))
        codes = [row.sutra for row in NIGHATA_TABLE]
        self.assertEqual(
            codes, ["8.1.%d" % n for n in range(16, 51)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in NIGHATA_TABLE:
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

    def test_the_accents_this_run_takes_away_are_live(self):
        # 6.1.198's आमन्त्रिताद्युदात्त, which 8.1.19 displaces,
        # and 6.1.161, which 8.1.29's note appeals to.
        for code in ("6.1.198", "6.1.161"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_half_of_what_that_heading_reaches_has_landed(self):
        # 8.1.16 पदस्य runs to 8.3.55. 8.2.23 संयोगान्तस्य लोपः,
        # the rule the vṛtti proves the heading on, has landed
        # with पाद ८.२; 8.3.55, where the heading stops, has not.
        # When it lands this fails and the note must state the
        # live edge.
        # And 8.3.55, where 8.1.16's पदस्य stops, has landed
        # too — so the whole span of the heading this run opens
        # can be asked, from 8.1.16 to 8.3.55.
        self.assertTrue(REGISTRY.has("8.2.23"))
        self.assertTrue(REGISTRY.has("8.3.55"))


if __name__ == "__main__":
    unittest.main()
