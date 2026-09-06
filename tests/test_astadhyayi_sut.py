# -*- coding: utf-8 -*-
"""
Tests for 6.1.135–157 — सुट् कात् पूर्वः.

Three things are worth holding down here.

**A phrase whose consequences run in two directions.** कात् पूर्वः is
stated to show the augment is not part of the root — and the vṛtti
then works out that a guṇa does NOT reach it in one place and DOES in
another, and that an accent reaches it in a third. Four consequences
of one phrase, and they do not all point the same way.

**A heading bounded by its own last rule.** The second in this pāda
after 6.1.45's आकार, against three bounded from outside.

**And a list defined by exclusion.** 6.1.157's गण is an आकृतिगण:
अविहितलक्षणः सुट् पारस्करप्रभृतिषु द्रष्टव्यः — whatever सुट् no rule
accounts for belongs to it, so it cannot be closed.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.sut import (
    PARASKARADI, SUT_MARKER, SUT_RUN, SUT_TABLE, WHY_KAT_PURVAH,
    provisions_for, sut_for, sut_run)
from src.astadhyayi.sutra import REGISTRY


def _order(sutra_id):
    return tuple(int(p) for p in sutra_id.split("."))


class TheHeadingIsBoundedByItsOwnLastRule(unittest.TestCase):
    def test_the_marker_is_a_member_of_the_run(self):
        self.assertEqual(SUT_MARKER, SUT_RUN[1])
        self.assertTrue(provisions_for(SUT_MARKER))

    def test_the_vrtti_names_that_rule_by_its_own_words(self):
        self.assertIn("पारस्करप्रभृतीनि च संज्ञायाम् इति यावत्",
                      provisions_for("6.1.135")[0].why)

    def test_it_is_the_second_heading_of_the_pada_built_that_way(self):
        """
        6.1.45's आकार was the first. The other three — संहिता, अचि
        and एकः पूर्वपरयोः — divide two ways between them, so the
        pāda has both shapes and the distinction is real.
        """
        from src.astadhyayi.atva import ATVA_MARKER, ATVA_RUN
        from src.astadhyayi.ekadesa import EKADESA_MARKER, EKADESA_RUN
        from src.astadhyayi.samhita import (
            ACI_MARKER, ACI_RUN, SAMHITA_MARKER, SAMHITA_RUN)

        inside = [(ATVA_MARKER, ATVA_RUN), (ACI_MARKER, ACI_RUN),
                  (SUT_MARKER, SUT_RUN)]
        outside = [(SAMHITA_MARKER, SAMHITA_RUN),
                   (EKADESA_MARKER, EKADESA_RUN)]
        for marker, run in inside:
            self.assertEqual(marker, run[1], marker)
        for marker, run in outside:
            self.assertGreater(_order(marker), _order(run[1]), marker)

    def test_the_heading_supplies_nothing(self):
        self.assertEqual(provisions_for("6.1.135")[0].does, "")
        for kwargs in ({}, {"pre": "sam"}, {"result": "bhūṣaṇa"}):
            self.assertNotEqual(sut_for(**kwargs).sutra, "6.1.135",
                                kwargs)

    def test_the_report_names_the_bound_and_the_consequences(self):
        answer = sut_run()
        self.assertEqual(answer.sutra, "6.1.135")
        self.assertIn("6.1.157", answer.why)


class OnePhraseWithFourConsequences(unittest.TestCase):
    """
    कात् पूर्वग्रहणं सुटोऽभक्तत्वज्ञापनार्थम्. The augment stands
    apart from the root — and the vṛtti draws out what follows, in
    both directions.
    """

    def test_there_are_four_and_each_names_the_rule_it_bears_on(self):
        self.assertEqual(len(WHY_KAT_PURVAH), 4)
        for rule, _consequence in WHY_KAT_PURVAH:
            self.assertRegex(rule, r"^\d\.\d\.\d+$")

    def test_they_do_not_all_point_the_same_way(self):
        """
        The guṇa is refused in one place and granted in another, and
        the two are told apart by different maxims. A record that
        kept only the refusal would be half the argument.
        """
        consequences = [text for _rule, text in WHY_KAT_PURVAH]
        joined = " ".join(consequences)
        self.assertIn("no इट् and no guṇa", joined)
        self.assertIn("DOES take its guṇa", joined)

    def test_the_maxims_the_two_sides_rest_on_are_both_recorded(self):
        why = provisions_for("6.1.135")[0].why
        self.assertIn("स्वरविधौ व्यञ्जनमविद्यमानवद्", why)
        self.assertIn("तन्मध्यपतितस्तद्ग्रहणेन गृह्यते", why)

    def test_and_the_marker_it_carries_is_for_a_later_rule(self):
        # 8.3.70 परिनिविभ्यः… is what the ट् marker is put there
        # for, and it has landed with पाद ८.३ — so the reason the
        # marker exists can be asked of the registry.
        self.assertIn("टित्करणं", provisions_for("6.1.135")[0].why)
        self.assertTrue(REGISTRY.has("8.3.70"))


class TheSupplementRuleHasAConditionOfItsOwn(unittest.TestCase):
    """
    6.1.136 says only that the augment survives an intervener. Give
    it no condition and it would state nothing and answer every
    question the table is asked.
    """

    def test_it_is_the_only_row_of_its_shape(self):
        with_across = [r.sutra for r in SUT_TABLE if r.across]
        self.assertEqual(with_across, ["6.1.136"])

    def test_it_is_unreachable_without_an_intervener_named(self):
        self.assertEqual(sut_for("pac").sutra, "")
        self.assertEqual(sut_for().sutra, "")

    def test_and_reachable_with_either_of_the_two(self):
        for intervener in ("aṭ", "abhyāsa"):
            self.assertEqual(sut_for(across=intervener).sutra,
                             "6.1.136", intervener)

    def test_a_third_intervener_reaches_nothing(self):
        self.assertEqual(sut_for(across="upasarga").sutra, "")

    def test_the_note_records_that_the_rule_is_not_paninis(self):
        why = provisions_for("6.1.136")[0].why
        self.assertIn("अड्व्यवाय उपसंख्यानम्", why)
        self.assertIn("अभ्यासव्यवाये च", why)


class ASenseTellsSixRulesApart(unittest.TestCase):
    """
    6.1.137 through 6.1.142 all name करोति or किरति with a preverb.
    Nothing but the sense separates them, so the sense has to
    outweigh both the root and the preverb in the score.
    """

    SENSES = {
        "6.1.137": ("kṛ", "sam", "bhūṣaṇa"),
        "6.1.138": ("kṛ", "upa", "samavāya"),
        "6.1.139": ("kṛ", "upa", "pratiyatna"),
        "6.1.140": ("kṝ", "upa", "lavana"),
        "6.1.141": ("kṝ", "prati", "hiṃsā"),
    }

    def test_each_answers_only_in_its_own_sense(self):
        for code, (root, pre, sense) in self.SENSES.items():
            answer = sut_for(root, pre=pre, result=sense)
            self.assertEqual(answer.sutra, code,
                             "%s %s %s" % (root, pre, sense))

    def test_two_of_them_share_a_root_and_a_preverb_exactly(self):
        first = provisions_for("6.1.138")[0]
        second = provisions_for("6.1.139")[0]
        self.assertEqual(first.of, second.of)
        self.assertIn("upa", first.pre)
        self.assertIn("upa", second.pre)
        self.assertNotEqual(first.result, second.result)

    def test_no_sense_at_all_reaches_none_of_them(self):
        self.assertEqual(sut_for("kṛ", pre="upa").sutra, "")

    def test_and_a_sense_none_of_them_names_reaches_none_either(self):
        self.assertEqual(
            sut_for("kṛ", pre="upa", result="gamana").sutra, "")

    def test_the_first_admits_its_own_sense_condition_leaks(self):
        """
        संपूर्वस्य क्वचिदभूषणेऽपि सुडिष्यते, संस्कृतमन्नमिति — the
        augment is wanted after सम् sometimes where the sense is NOT
        adorning, and the vṛtti says so rather than stretching the
        word to cover cooked food.
        """
        # संस्कृतम् + अन्नम् + इति joins into संस्कृतमन्नमिति, so
        # the fragment has to stop before the last junction.
        self.assertIn("संस्कृतमन्नम",
                      provisions_for("6.1.137")[0].why)


class AnAgentCanBeWhatDecides(unittest.TestCase):
    def test_two_rows_turn_on_who_the_agent_is(self):
        with_agent = [(r.sutra, r.agent) for r in SUT_TABLE if r.agent]
        self.assertEqual(with_agent,
                         [("6.1.142", "catuṣpād-śakuni"),
                          ("6.1.150", "śakuni")])

    def test_a_man_scratching_the_ground_reaches_nothing(self):
        self.assertEqual(
            sut_for("kṝ", pre="apa", result="ālekhana").sutra, "")

    def test_but_a_four_footed_animal_or_a_bird_does(self):
        self.assertEqual(
            sut_for("kṝ", pre="apa", result="ālekhana",
                    agent="catuṣpād-śakuni").sutra, "6.1.142")

    def test_and_the_three_reasons_for_it_serve_a_second_rule(self):
        """
        हर्षजीविकाकुलायकरणेषु — out of gladness, for food, or to make
        a nest. The same three give the root its ātmanepada by a
        vārttika on 1.3.21, which IS codified.
        """
        why = provisions_for("6.1.142")[0].why
        # करणेषु + इति joins into करणेष्विति, so the fragment
        # stops before the ending.
        self.assertIn("हर्षजीविकाकुलायकरणेष्", why)
        self.assertIn("1.3.21", why)
        self.assertTrue(REGISTRY.has("1.3.21"))


class MostOfTheSectionLaysAWordDownWhole(unittest.TestCase):
    def test_the_niptana_rows_outnumber_the_augment_rows(self):
        laid_down = [r.sutra for r in SUT_TABLE
                     if r.does == "nipātana"]
        inserted = [r.sutra for r in SUT_TABLE if r.does == "suṭ"]
        self.assertGreater(len(laid_down), len(inserted))

    def test_almost_every_one_is_confined_by_a_sense_or_an_agent(self):
        loose = [r.sutra for r in SUT_TABLE
                 if r.does == "nipātana"
                 and not (r.result or r.agent or r.pre or r.samjna)]
        self.assertEqual(loose, ["6.1.154"])

    def test_and_that_one_is_confined_by_what_the_word_means(self):
        """
        मस्कर and मस्करिन् are told apart from मकर by their SENSE and
        not by any condition a query can carry: the rule pairs two
        words with two meanings यथासंख्यम्, and the counter-example
        is the same shape without the augment.
        """
        row = provisions_for("6.1.154")[0]
        self.assertIn("मकरो ग्राहः", row.keeps_out)
        self.assertIn("यथासंख्यम्", row.why)

    def test_each_records_the_form_its_condition_keeps_out(self):
        for row in SUT_TABLE:
            if row.does == "nipātana":
                self.assertGreater(len(row.keeps_out), 4, row.sutra)


class TheLastListCannotBeClosed(unittest.TestCase):
    """
    आकृतिगण. The membership rule is *whatever no other rule
    explains*, so the tuple here is a sample and not a census — and
    the note has to say which it is.
    """

    def test_the_note_states_the_membership_rule(self):
        why = provisions_for("6.1.157")[0].why
        # प्रभृतिः + आकृतिगणः joins into प्रभृतिराकृतिगणः, so the
        # fragment has to carry the junction.
        self.assertIn("प्रभृतिराकृतिगणः", why)
        self.assertIn("अविहितलक्षणः सुट्", why)

    def test_every_member_listed_reaches_the_rule(self):
        for word in PARASKARADI:
            self.assertEqual(sut_for(word).sutra, "6.1.157", word)

    def test_two_of_them_need_a_sound_dropped_besides(self):
        why = provisions_for("6.1.157")[0].why
        self.assertIn("सुट् तलोपश्च", why)
        self.assertIn("तस्करश्चोरः", why)

    def test_one_supplement_puts_the_augment_on_a_finite_verb(self):
        """
        प्रात्तुम्पतौ गवि कर्तरि — प्रस्तुम्पति गौः, and the
        condition is WHO THE AGENT IS. Nothing else in the pāda
        conditions an augment on a verb form at all.
        """
        why = provisions_for("6.1.157")[0].why
        self.assertIn("प्रस्तुम्पति गौः", why)
        self.assertIn("प्रतुम्पति वनस्पतिः",
                      provisions_for("6.1.157")[0].keeps_out)


class OneRuleHoldsInAMantraAlone(unittest.TestCase):
    def test_it_is_the_only_such_row(self):
        in_mantra = [r.sutra for r in SUT_TABLE if r.mantra]
        self.assertEqual(in_mantra, ["6.1.151"])

    def test_it_is_out_of_reach_otherwise(self):
        self.assertEqual(sut_for(uttarapada="candra").sutra, "")

    def test_and_reachable_once_the_mantra_is_named(self):
        answer = sut_for(uttarapada="candra", mantra=True)
        self.assertEqual(answer.sutra, "6.1.151")
        self.assertTrue(answer.mantra)

    def test_the_note_says_uttarapada_means_what_it_means_in_a_compound(self):
        self.assertIn("उत्तरपदं समास एव भवतीति प्रसिद्धम्",
                      provisions_for("6.1.151")[0].why)

    def test_and_a_second_rule_exists_for_what_stands_outside_a_mantra(self):
        """
        हरिश्चन्द्रग्रहणम् अमन्त्रार्थम् — 6.1.151 would have given
        the word inside a मन्त्र already, so 6.1.153 names it for
        everywhere else.
        """
        self.assertIn("अमन्त्रार्थम्", provisions_for("6.1.153")[0].why)


class TheSectionIsWhereItSaysItIs(unittest.TestCase):
    def test_the_rows_are_the_twenty_three(self):
        held = sorted(r.sutra for r in SUT_TABLE)
        self.assertEqual(held,
                         sorted("6.1.%d" % n for n in range(135, 158)))

    def test_every_rule_here_is_registered_against_this_resolver(self):
        for row in SUT_TABLE:
            self.assertEqual(REGISTRY.get(row.sutra).apply.__name__,
                             "sut_for", row.sutra)

    def test_the_pada_is_contiguous_to_the_end_of_the_sut_run(self):
        for n in range(1, 158):
            self.assertTrue(REGISTRY.has("6.1.%d" % n), n)

    def test_no_row_names_itself_on_what_it_extends(self):
        for row in SUT_TABLE:
            self.assertNotIn(row.sutra, row.blocks, row.sutra)


class NothingAnswersByDefault(unittest.TestCase):
    def test_an_unreached_question_gets_nothing(self):
        answer = sut_for("gam", pre="sam")
        self.assertEqual(answer.sutra, "")
        self.assertEqual(answer.does, "")

    def test_and_the_message_says_what_the_heading_supplies(self):
        self.assertIn("6.1.135", sut_for("gam", pre="sam").why)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in SUT_TABLE:
            self.assertGreater(len(row.why), 120, row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in SUT_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_module_still_does_not_build_the_word(self):
        """
        `sut_for` says which rule inserts the augment. Turning
        परिस्कर्ता into परिष्कर्ता is 8.3.70's and turning the म् of
        सम् into a स् is a supplement on 8.3.5, and both of those
        have since been codified. What has not changed is this
        module: it names the rule that puts the augment in and does
        not carry the word any further, so परिष्कर्ता is still not
        something it returns. The debt has moved from the rules to
        the wiring.
        """
        for code in ("8.3.70", "8.3.5"):
            self.assertTrue(REGISTRY.has(code), code)
        answer = sut_for("kṛ", pre="pari", result="bhūṣaṇa")
        self.assertEqual(answer.does, "suṭ")
        self.assertNotIn("pariṣkartā", str(answer))

    def test_the_accent_section_that_closes_the_pada_landed_too(self):
        """
        6.1.158 to 6.1.223 is codified now — the debt this test was
        written as, paid. What has to keep holding is that this
        table stops where its heading does: 6.1.157 is its last row
        and 6.1.158 belongs to another module.
        """
        self.assertTrue(REGISTRY.has("6.1.157"))
        self.assertTrue(REGISTRY.has("6.1.223"))
        self.assertEqual(provisions_for("6.1.158"), ())
        self.assertEqual(REGISTRY.get("6.1.158").apply.__module__,
                         "src.astadhyayi.pada_svara")


if __name__ == "__main__":
    unittest.main()
