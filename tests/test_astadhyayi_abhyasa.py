# -*- coding: utf-8 -*-
"""
७.४.५८–९७ — अभ्यासस्य, the heading that closes the adhyāya.

Forty sūtras, seven of them codified long ago inside the
reduplication itself. The tests take the run in the order the
Kāśikā does — what the copy loses, what it changes, what it
takes before लिट्, before श्लु, before सन् and before यङ् — and
end on 7.4.93, the rule the whole causal aorist turns on.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.abhyasa import (
    ABHYASA_RUN,
    ABHYASA_TABLE,
    ADHIKARA_TO,
    ARTI_PIPARTI,
    ATRA,
    BHRNADI_THREE,
    CAR_PHAL,
    CODIFIED_APART,
    JAPADI_SIX,
    NIJADI_THREE,
    NIPATANA_EIGHTEEN,
    SMRADI_SEVEN,
    SRAVATI_SIX,
    VANCU_EIGHT,
    VESTI_CESTI,
    in_the_copy,
    provisions_for,
)
from src.astadhyayi.kiti_sani import AP_JNAP_RDH, MI_MA_EIGHT
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheHeadingItself(unittest.TestCase):
    """7.4.58, which does two things at once."""

    def test_the_copy_goes_in_the_environment_just_left_behind(self):
        # मित्सति, दित्सति, आरिप्सते.
        for root in ("mī", "rabh", "āp"):
            got = in_the_copy(root, before="sa-ādi-san")
            self.assertEqual(got.sutra, "7.4.58", root)
            self.assertEqual(got.does, "lopa", root)

    def test_that_environment_is_exactly_what_7_4_54_to_57_named(self):
        # अत्र = सनि मीमा… इत्यादि मुचोऽकर्मकस्य इति यावत्. The
        # eight and the three are not written out again — they
        # are the same tuples the earlier module holds.
        self.assertEqual(ATRA[:len(MI_MA_EIGHT)], MI_MA_EIGHT)
        self.assertEqual(
            ATRA[len(MI_MA_EIGHT):len(MI_MA_EIGHT) + 3],
            AP_JNAP_RDH)
        self.assertEqual(ATRA[-2:], ("dambh", "muc"))

    def test_and_the_sutra_opens_a_heading_to_the_end_of_the_adhyaya(self):
        # अभ्यासस्य इत्येतच् च अधिकृतं वेदितव्यम् आ
        # अध्यायपरिसमाप्तेः.
        why = provisions_for("7.4.58")[0].why
        self.assertIn("अध्यायपरिसमाप्तेः", why)
        self.assertEqual(ADHIKARA_TO, "7.4.97")
        self.assertEqual(ABHYASA_RUN, ("7.4.58", "7.4.97"))

    def test_and_atra_is_there_to_fence_the_loss_in(self):
        # विषयावधारणार्थम् — the loss could have been packed into
        # 7.4.54, and is stated apart so the heading does not
        # carry it down.
        self.assertIn("विषयावधारणार्थम्",
                      provisions_for("7.4.58")[0].why)


class WhatTheCopyLoses(unittest.TestCase):
    """7.4.61, the शेष rule that displaces 7.4.60."""

    def test_the_khay_a_sar_stands_before_is_what_remains(self):
        # चुश्च्योतिषति, तिष्ठासति, पिस्पन्दिषते.
        got = in_the_copy(gana="śar-pūrva-khay")
        self.assertEqual(got.sutra, "7.4.61")
        self.assertEqual(got.does, "śeṣa")
        self.assertIn("7.4.60", got.blocked_by)

    def test_and_both_words_of_the_sutra_are_tested(self):
        # शर्पूर्वाः इति किम्? पपाच। खयः इति किम्? सस्नौ.
        keeps = provisions_for("7.4.61")[0].keeps_out
        self.assertIn("पपाच", keeps)
        self.assertIn("सस्नौ", keeps)

    def test_and_a_varttika_widens_sar_to_khar(self):
        # उचिच्छिषति — the तुक् is अन्तरङ्ग and the copy is then
        # त्छ्, whose त् is a खर् and not a शर्.
        why = provisions_for("7.4.61")[0].why
        self.assertIn("खर्पूर्वाः", why)
        self.assertIn("अन्तरङ्ग", why)


class WhatTheCopyChanges(unittest.TestCase):
    """7.4.62–64, one rule and the two that refuse it."""

    def test_a_guttural_or_h_becomes_a_palatal(self):
        # चकार, जगाम, जहार.
        got = in_the_copy(gana="ku-ha")
        self.assertEqual(got.sutra, "7.4.62")
        self.assertEqual(got.does, "cu")

    def test_but_not_of_kav_before_yan(self):
        # कोकूयते उष्ट्रः — and not *चोकूयते.
        got = in_the_copy("kav", gana="ku-ha", before="yaṅ")
        self.assertEqual(got.sutra, "7.4.63")
        self.assertTrue(got.refuses)
        self.assertEqual(got.does, "")
        self.assertIn("7.4.62", got.blocked_by)

    def test_and_the_root_is_named_by_its_conjugated_shape(self):
        # कवतेः इति विकरणनिर्देशः कौतेः कुवतेश्च निवृत्त्यर्थः —
        # so कौति and कुवति keep their palatal, चोकूयते.
        self.assertIn("विकरणनिर्देशः",
                      provisions_for("7.4.63")[0].why)

    def test_and_not_of_krs_before_yan_in_the_veda(self):
        # करिकृष्यते यज्ञकुणपः.
        got = in_the_copy("kṛṣ", gana="ku-ha", before="yaṅ",
                          chandasi=True)
        self.assertEqual(got.sutra, "7.4.64")
        self.assertTrue(got.refuses)

    def test_but_outside_the_veda_the_palatal_stands(self):
        # चरीकृष्यते कृषीवलः — one root, one affix, and only the
        # register telling the two forms apart.
        got = in_the_copy("kṛṣ", gana="ku-ha", before="yaṅ")
        self.assertEqual(got.sutra, "7.4.62")
        self.assertEqual(got.does, "cu")

    def test_eighteen_vedic_forms_are_laid_down_whole(self):
        self.assertEqual(len(NIPATANA_EIGHTEEN), 18)
        for form in NIPATANA_EIGHTEEN:
            got = in_the_copy(form, chandasi=True)
            self.assertEqual(got.sutra, "7.4.65", form)
            self.assertTrue(got.nipatana, form)

    def test_and_the_vrtti_offers_three_derivations_and_picks_none(self):
        # धारयतेः, धृङो वा; श्लौ, यङ्लुकि वा.
        why = provisions_for("7.4.65")[0].why
        self.assertIn("धृङो वा", why)
        self.assertIn("यङ्लुकि वा", why)


class BeforeThePerfect(unittest.TestCase):
    """7.4.67–74, where लिट् governs almost everything."""

    def test_two_roots_take_samprasarana(self):
        # विदिद्युते, सुष्वापयिषति.
        for root in ("dyut", "svāpi"):
            got = in_the_copy(root)
            self.assertEqual(got.sutra, "7.4.67", root)
            self.assertEqual(got.does, "saṃprasāraṇa", root)

    def test_and_the_vrtti_adds_a_condition_the_sutra_does_not_state(self):
        # अभ्यासनिमित्तेन प्रत्ययेन आनन्तर्ये सति — which is why
        # स्वापकीयति does not take it.
        row = provisions_for("7.4.67")[0]
        self.assertIn("आनन्तर्ये सति", row.why)
        self.assertIn("स्वापकीयति", row.keeps_out)

    def test_vyath_takes_it_in_the_perfect_and_saves_its_ya(self):
        # विव्यथे — 7.4.60 was about to drop the य्.
        got = in_the_copy("vyath", before="liṭ")
        self.assertEqual(got.sutra, "7.4.68")
        self.assertIn("7.4.60", got.blocked_by)
        self.assertIn("हलादिः शेषेण",
                      provisions_for("7.4.68")[0].why)

    def test_and_the_v_is_not_touched_because_of_a_refusal(self):
        # न संप्रसारणे संप्रसारणम् — 6.1.37, which is codified.
        self.assertIn("6.1.37", provisions_for("7.4.68")[0].why)
        self.assertTrue(REGISTRY.has("6.1.37"))

    def test_in_lengthens_before_a_kit_perfect_only(self):
        # ईयतुः, ईयुः; इयाय where the ending is not कित्.
        self.assertEqual(
            in_the_copy("iṇ", before="liṭ-kit").sutra, "7.4.69")
        self.assertNotEqual(
            in_the_copy("iṇ", before="liṭ").sutra, "7.4.69")

    def test_and_that_form_exists_at_all_only_by_sthanivadbhava(self):
        # इणो यण् इति यणादेशे कृते स्थानिवद्भावाद् द्विर्वचनम् —
        # 6.4.81 is codified, and without it इ + अतुस् has no
        # syllable to copy.
        self.assertIn("स्थानिवद्भावाद्",
                      provisions_for("7.4.69")[0].why)
        self.assertTrue(REGISTRY.has("6.4.81"))

    def test_an_initial_a_lengthens_and_what_follows_takes_nut(self):
        # आट, आटतुः; आनङ्ग, आनञ्ज.
        got = in_the_copy(gana="a-ādi", before="liṭ")
        self.assertEqual(got.sutra, "7.4.70")
        self.assertEqual(got.does, "dīrgha")
        after = in_the_copy(gana="dvi-hal", before="liṭ",
                            part="para")
        self.assertEqual(after.sutra, "7.4.71")
        self.assertEqual(after.does, "nuṭ")

    def test_and_the_lengthening_is_stated_against_a_merger(self):
        # अतो गुणे पररूपत्वस्य अपवादः — 6.1.97, which is
        # codified, would have swallowed the copy.
        self.assertIn("पररूपत्वस्य",
                      provisions_for("7.4.70")[0].why)
        self.assertTrue(REGISTRY.has("6.1.97"))

    def test_the_nut_reaches_what_follows_and_not_the_copy(self):
        # It is the one rule of the heading that names its own
        # target, and a question about the copy must not reach
        # it.
        self.assertNotEqual(
            in_the_copy(gana="dvi-hal", before="liṭ").sutra,
            "7.4.71")

    def test_and_asnoti_takes_it_too_but_asnati_does_not(self):
        # व्यानशे; आश, आशतुः, आशुः.
        got = in_the_copy("aśnoti", before="liṭ", part="para")
        self.assertEqual(got.sutra, "7.4.72")
        self.assertIn("अश्नातेर्", provisions_for("7.4.72")[0].why)

    def test_bhu_gives_the_commonest_perfect_in_the_language(self):
        # बभूव — and not *बुभूव.
        got = in_the_copy("bhavati", before="liṭ")
        self.assertEqual(got.sutra, "7.4.73")
        self.assertEqual(got.does, "a")

    def test_and_one_vedic_form_costs_three_departures_at_once(self):
        # ससूव स्थविरं विपश्चिताम् — a परस्मैपद ending on an
        # आत्मनेपद root, a वुक्, and अ for the copy.
        got = in_the_copy("sasūva", chandasi=True)
        self.assertEqual(got.sutra, "7.4.74")
        self.assertTrue(got.nipatana)
        why = provisions_for("7.4.74")[0].why
        for departure in ("परस्मैपदं", "वुगागमः", "अत्वं"):
            self.assertIn(departure, why, departure)
        self.assertIn("सुषुवे", provisions_for("7.4.74")[0].keeps_out)


class BeforeSlu(unittest.TestCase):
    """7.4.75–78, guṇa for three and इ for five."""

    def test_three_roots_take_guna(self):
        # नेनेक्ति, वेवेक्ति, वेवेष्टि.
        self.assertEqual(len(NIJADI_THREE), 3)
        for root in NIJADI_THREE:
            got = in_the_copy(root, before="ślu")
            self.assertEqual(got.sutra, "7.4.75", root)
            self.assertEqual(got.does, "guṇa", root)

    def test_and_the_count_of_three_is_said_for_the_next_sutra(self):
        # त्रिग्रहणम् उत्तरार्थम्.
        self.assertIn("उत्तरार्थम्",
                      provisions_for("7.4.75")[0].why)

    def test_and_it_is_what_stops_bhrn_being_read_as_a_class(self):
        # भृञ् heads the root list, and without the borrowed
        # count भृञादि would swallow जहाति.
        self.assertEqual(len(BHRNADI_THREE), 3)
        for root in BHRNADI_THREE:
            got = in_the_copy(root, before="ślu")
            self.assertEqual(got.sutra, "7.4.76", root)
            self.assertEqual(got.does, "it", root)
        self.assertIn("जहाति",
                      provisions_for("7.4.76")[0].keeps_out)

    def test_two_more_are_added_by_their_finished_forms(self):
        # इयर्ति भूमम्; पिपर्ति सोमम्.
        self.assertEqual(ARTI_PIPARTI, ("ṛ", "pṝ"))
        for root in ARTI_PIPARTI:
            self.assertEqual(
                in_the_copy(root, before="ślu").sutra, "7.4.77")

    def test_and_the_veda_both_widens_the_list_and_declines_it(self):
        # विवष्टि, विवक्ति, सिषक्ति on roots no rule names; and
        # ददाति, जजनत् where the इ was due and does not come.
        got = in_the_copy("vaś", before="ślu", chandasi=True)
        self.assertEqual(got.sutra, "7.4.78")
        self.assertTrue(got.optional)
        keeps = provisions_for("7.4.78")[0].keeps_out
        self.assertIn("ददाति", keeps)

    def test_but_a_named_root_still_beats_the_bahulam(self):
        # भृञ् in the Veda is still 7.4.76's, not 7.4.78's.
        self.assertEqual(
            in_the_copy("bhṛñ", before="ślu", chandasi=True).sutra,
            "7.4.76")


class BeforeSan(unittest.TestCase):
    """7.4.79–81, the rules the desiderative is heard by."""

    def test_an_a_final_copy_becomes_i(self):
        # पिपक्षति, यियक्षति, तिष्ठासति, पिपासति.
        got = in_the_copy(gana="a-anta", before="san")
        self.assertEqual(got.sutra, "7.4.79")
        self.assertEqual(got.does, "it")

    def test_and_the_tapara_keeps_the_yan_stems_copy_out(self):
        # पापचिषते — the copy's आ is long.
        self.assertIn("पापचिषते",
                      provisions_for("7.4.79")[0].keeps_out)

    def test_a_u_final_copy_becomes_i_in_three_followings(self):
        # पिपविषते, यियविषति, जिजावयिषति.
        for after in ("pa-varga-a-para", "yaṇ-a-para",
                      "ja-a-para"):
            got = in_the_copy(gana="u-anta", before="san",
                              result=after)
            self.assertEqual(got.sutra, "7.4.80", after)

    def test_and_that_sutra_is_read_as_proof_of_an_order(self):
        # एतदेव पुयण्ज्यपरे इति वचनं ज्ञापकम् — the three
        # conditions would be idle unless the copy were already
        # there when the rule ran.
        self.assertIn("ज्ञापकम्", provisions_for("7.4.80")[0].why)

    def test_six_roots_take_it_only_optionally(self):
        # सिस्रावयिषति beside सुस्रावयिषति.
        self.assertEqual(len(SRAVATI_SIX), 6)
        for root in SRAVATI_SIX:
            got = in_the_copy(root, gana="u-anta", before="san",
                              result="yaṇ-a-para")
            self.assertEqual(got.sutra, "7.4.81", root)
            self.assertTrue(got.optional, root)
            self.assertIn("7.4.80", got.blocked_by, root)

    def test_and_the_option_is_of_exactly_one_of_the_three_cases(self):
        # All six fall under the यण् with अ after it, and none
        # of them under the प-वर्ग or the ज्.
        for after in ("pa-varga-a-para", "ja-a-para"):
            self.assertEqual(
                in_the_copy("sru", gana="u-anta", before="san",
                            result=after).sutra, "7.4.80", after)


class BeforeYan(unittest.TestCase):
    """7.4.84–89, the augments and the vowel after the copy."""

    def test_eight_roots_take_nik(self):
        # वनीवच्यते, सनीस्रस्यते, पनीपत्यते.
        self.assertEqual(len(VANCU_EIGHT), 8)
        for root in VANCU_EIGHT:
            for affix in ("yaṅ", "yaṅ-luk"):
                got = in_the_copy(root, before=affix)
                self.assertEqual(got.sutra, "7.4.84", (root, affix))
                self.assertEqual(got.does, "nīk", root)

    def test_a_nasal_final_stem_takes_nuk(self):
        # तन्तन्यते, जङ्गम्यते, यंयम्यते.
        got = in_the_copy(gana="anunāsika-anta", before="yaṅ")
        self.assertEqual(got.sutra, "7.4.85")
        self.assertEqual(got.does, "nuk")

    def test_and_the_nuk_is_written_for_an_anusvara(self):
        # नुक् इत्येतद् अनुस्वारोपलक्षणार्थम् — which is why
        # यंयम्यते shows one where no झल् follows.
        self.assertIn("अनुस्वारोपलक्षणार्थं",
                      provisions_for("7.4.85")[0].why)

    def test_eight_more_roots_take_it_by_name(self):
        # जञ्जप्यते, दन्दह्यते, बम्भज्यते; चञ्चूर्यते, पम्फुल्यते.
        self.assertEqual(len(JAPADI_SIX), 6)
        for root in JAPADI_SIX:
            self.assertEqual(
                in_the_copy(root, before="yaṅ").sutra, "7.4.86")
        for root in CAR_PHAL:
            self.assertEqual(
                in_the_copy(root, before="yaṅ").sutra, "7.4.87")

    def test_and_two_of_the_six_are_written_short_on_purpose(self):
        # दश is दंशि, named so the न् goes in the यङ्लुक् too,
        # and पश is a root the sūtras alone attest.
        why = provisions_for("7.4.86")[0].why
        self.assertIn("नकारलोपार्थम्", why)
        self.assertIn("सौत्रो", why)

    def test_car_and_phal_also_change_the_vowel_after_the_copy(self):
        # चञ्चूर्यते — the उ is not the copy's.
        got = in_the_copy("car", before="yaṅ-luk", part="para")
        self.assertEqual(got.sutra, "7.4.88")
        self.assertEqual(got.does, "ut")

    def test_and_a_question_about_the_copy_does_not_reach_that_rule(self):
        # 7.4.87 and 7.4.88 name the same two roots before the
        # same affix and differ in nothing but which piece they
        # touch. The first draft let 7.4.88 answer for the copy.
        self.assertEqual(
            in_the_copy("car", before="yaṅ-luk").sutra, "7.4.87")

    def test_the_same_u_comes_before_a_ta_initial_affix(self):
        # चरणं चूर्तिः; प्रफुल्तिः.
        got = in_the_copy("car", before="ta-ādi", part="para")
        self.assertEqual(got.sutra, "7.4.89")
        self.assertEqual(got.does, "ut")

    def test_and_there_the_heading_itself_is_set_aside(self):
        # वचनसामर्थ्याद् इह न अभिसम्बध्यते — there is no copy in
        # चूर्तिः at all, so a sūtra that could not apply under
        # its own heading is read without it.
        self.assertIn("अभिसम्बध्यते",
                      provisions_for("7.4.89")[0].why)

    def test_an_r_final_stem_takes_the_three_augments_in_the_yanluk(self):
        # चर्कर्ति, चरिकर्ति, चरीकर्ति.
        got = in_the_copy(gana="ṛ-anta", before="yaṅ-luk")
        self.assertEqual(got.sutra, "7.4.92")
        self.assertEqual(got.does, "ruk-rik-rīk")
        self.assertTrue(got.optional)

    def test_and_the_two_that_gave_them_to_a_penult_are_codified(self):
        # 7.4.90 रीगृदुपधस्य च and 7.4.91 रुग्रिकौ च लुकि were
        # registered inside the reduplication long ago; 7.4.92
        # adds the stem that ENDS in ऋ.
        for code in ("7.4.90", "7.4.91"):
            self.assertTrue(REGISTRY.has(code), code)


class TheCausalAorist(unittest.TestCase):
    """7.4.93–97, the rules अचीकरत् is made by."""

    def test_the_copy_acts_as_if_san_followed(self):
        # अचीकरत्, अपीपचत्, अपीपवत्.
        got = in_the_copy(before="caṅ-para-ṇi",
                          result="laghu-anaglopa")
        self.assertEqual(got.sutra, "7.4.93")
        self.assertEqual(got.does, "sanvat")

    def test_and_the_vrtti_names_which_rules_are_borrowed(self):
        # सन्यतः इत्युक्तम्, चङ्परेऽपि तथा; ओः पुयण्ज्यपरे
        # इत्युक्तम्, चङ्परेऽपि तथा.
        why = provisions_for("7.4.93")[0].why
        self.assertIn("7.4.79", why)
        self.assertIn("7.4.80", why)

    def test_and_a_light_copy_then_lengthens(self):
        # अचीकरत्, अजीहरत् — the ई made twice over.
        got = in_the_copy(gana="laghu-abhyāsa",
                          before="caṅ-para-ṇi",
                          result="laghu-anaglopa")
        self.assertEqual(got.sutra, "7.4.94")
        self.assertEqual(got.does, "dīrgha")

    def test_and_each_of_the_four_conditions_is_tested_by_removal(self):
        # अबिभ्रजत्, अततक्षत्, अहं पपच, अचकमत, अचकथत्.
        keeps = provisions_for("7.4.94")[0].keeps_out
        for form in ("अबिभ्रजत्", "अततक्षत्", "अचकमत", "अचकथत्"):
            self.assertIn(form, keeps, form)

    def test_seven_roots_take_a_short_a_instead_of_both(self):
        # असस्मरत्, अददरत्, अपप्रथत्.
        self.assertEqual(len(SMRADI_SEVEN), 7)
        for root in SMRADI_SEVEN:
            got = in_the_copy(root, before="caṅ-para-ṇi",
                              result="laghu-anaglopa")
            self.assertEqual(got.sutra, "7.4.95", root)
            self.assertEqual(got.does, "at", root)
            self.assertEqual(set(got.blocked_by),
                             {"7.4.93", "7.4.94"}, root)

    def test_and_the_tapara_is_what_keeps_the_length_off(self):
        # तपरकरणसामर्थ्याद् अति कृते दीर्घो लघोः इत्येतद् अपि न
        # भवति — अददरत् and not *अदादरत्.
        self.assertIn("तपरकरणसामर्थ्याद्",
                      provisions_for("7.4.95")[0].why)

    def test_two_roots_take_it_only_optionally(self):
        # अववेष्टत् beside अविवेष्टत्.
        for root in VESTI_CESTI:
            got = in_the_copy(root, before="caṅ-para-ṇi",
                              result="laghu-anaglopa")
            self.assertEqual(got.sutra, "7.4.96", root)
            self.assertTrue(got.optional, root)

    def test_and_the_adhyaya_closes_on_one_root_and_two_forms(self):
        # अजीगणत्, and by the च अजगणत्.
        got = in_the_copy("gaṇ", before="caṅ-para-ṇi",
                          result="laghu-anaglopa")
        self.assertEqual(got.sutra, "7.4.97")
        self.assertEqual(got.does, "ī")
        self.assertTrue(got.optional)
        self.assertIn("चतुर्थः पादः",
                      provisions_for("7.4.97")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A copy none of these rules reaches is left alone."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = in_the_copy("pac", before="śap")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")

    def test_and_the_answer_says_what_shaped_it_instead(self):
        # 7.4.59 and 7.4.60, which are codified apart.
        got = in_the_copy("pac", before="śap")
        self.assertIn("7.4.59", got.why)
        self.assertIn("7.4.60", got.why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_table_holds_the_run_minus_what_was_codified_apart(self):
        codes = [row.sutra for row in ABHYASA_TABLE]
        expected = ["7.4.%d" % n for n in range(58, 98)
                    if "7.4.%d" % n not in CODIFIED_APART]
        self.assertEqual(codes, expected)
        self.assertEqual(len(CODIFIED_APART), 7)

    def test_the_seven_codified_apart_are_registered_all_the_same(self):
        # They live in the reduplication itself, and the whole
        # heading is covered only because both halves are.
        for code in CODIFIED_APART:
            self.assertTrue(REGISTRY.has(code), code)

    def test_every_sutra_of_the_heading_is_registered(self):
        for n in range(58, 98):
            self.assertTrue(REGISTRY.has("7.4.%d" % n), n)

    def test_every_row_carries_real_notes(self):
        for row in ABHYASA_TABLE:
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_nothing_in_the_table_restates_the_seven(self):
        for row in ABHYASA_TABLE:
            self.assertNotIn(row.sutra, CODIFIED_APART, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_adhyaya_is_closed_and_the_pada_is_whole(self):
        # 7.1.1 to 7.4.97, every sūtra of अध्याय ७.
        missing = [
            "7.%d.%d" % (pada, n)
            for pada, last in ((1, 103), (2, 118), (3, 120), (4, 97))
            for n in range(1, last + 1)
            if not REGISTRY.has("7.%d.%d" % (pada, n))
        ]
        self.assertEqual(missing, [])

    def test_and_the_last_adhyaya_has_been_opened_since(self):
        # 8.1.1 सर्वस्य द्वे opens it, and it doubles a WHOLE
        # word where 6.1.1 — the rule this pāda's copies all
        # come from — doubles one syllable. Both are codified,
        # so the two can be told apart by asking. 8.4.68 अ अ,
        # which closes the whole work, is still ahead.
        self.assertTrue(REGISTRY.has("8.1.1"))
        self.assertTrue(REGISTRY.has("6.1.1"))
        # 8.4.68 अ अ इति closes the work and is codified too, so
        # there is nothing left for this note to owe.
        self.assertTrue(REGISTRY.has("8.4.68"))


if __name__ == "__main__":
    unittest.main()
