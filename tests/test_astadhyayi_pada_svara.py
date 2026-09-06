# -*- coding: utf-8 -*-
"""
Tests for 6.1.158–223 — the accent, and what the परिभाषा governing it
can and cannot stop.

Four things here are not like anything the project has met before.

**A heading that is a परिभाषा and supplies nothing.** 6.1.158 does not
put an accent anywhere; it clears every OTHER syllable out of the way
of whichever rule speaks. It is the only heading of the pāda that
supplies neither an operation nor a name.

**And a rule that breaks it outright.** 6.1.200 gives कर्तवै TWO
accents at once, and the vṛtti names 6.1.158 as the reason the word
युगपत् had to be said.

**And one question answered three ways.** Whether प्रत्ययलक्षण holds
in accent rules: 6.1.191 and 6.1.198 say yes, 6.1.197 and 6.1.199 say
no, and 6.1.204 exists to prove it does not hold universally.

**And a maxim used in one place and refused in another.** स्वरविधौ
व्यञ्जनमविद्यमानवत् is what puts the accent on a vowel in a
consonant-final compound at 6.1.223 — and 6.1.176 names the नुट् for
the express purpose of denying it.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.pada_svara import (
    ACCENT_TABLE, AKRTIGANA, EKAVARJA_VERSE, SVARA_RUN,
    VYANJANAM_AVIDYAMANAVAT, WHICH_WINS, accent_of, ekavarja,
    provisions_for)
from src.astadhyayi.sutra import REGISTRY


def _order(sutra_id):
    return tuple(int(p) for p in sutra_id.split("."))


class TheHeadingIsAParibhasaAndSuppliesNothing(unittest.TestCase):
    def test_it_covers_the_rest_of_the_pada(self):
        self.assertEqual(SVARA_RUN, ("6.1.158", "6.1.223"))
        held = sorted(r.sutra for r in ACCENT_TABLE)
        self.assertEqual(held,
                         sorted("6.1.%d" % n for n in range(158, 224)))

    def test_it_puts_no_accent_anywhere(self):
        row = provisions_for("6.1.158")[0]
        self.assertTrue(row.heading)
        self.assertEqual(row.puts, "")
        self.assertEqual(row.where, "")

    def test_it_is_never_the_answer(self):
        for kwargs in ({}, {"before": "dhātu"}, {"marker": "cit"}):
            self.assertNotEqual(accent_of(**kwargs).sutra, "6.1.158",
                                kwargs)

    def test_the_vrtti_calls_it_a_paribhasa_in_so_many_words(self):
        self.assertIn("परिभाषेयं स्वरविधिविषया",
                      provisions_for("6.1.158")[0].why)

    def test_what_it_excepts_is_whichever_rule_speaks(self):
        """
        कः पुनरेको वर्ज्यते? यस्यासौ स्वरो विधीयते — the maxim does
        not choose a syllable. That is why it cannot be the answer
        to a question and why the report is a separate call.
        """
        self.assertIn("यस्यासौ स्वरो विधीयते",
                      provisions_for("6.1.158")[0].why)
        answer = ekavarja()
        self.assertEqual(answer.sutra, "6.1.158")
        self.assertEqual(answer.puts, "anudātta")


class FourAccentsCompeteAndOneWordCancelsThree(unittest.TestCase):
    """
    आगमस्य विकारस्य प्रकृतेः प्रत्ययस्य च। An augment has an accent,
    a substitute has one, the base has one and the affix has one —
    and एकवर्जम् is what stops all four sounding at once.
    """

    def test_the_verse_is_recorded_in_two_halves(self):
        self.assertEqual(len(EKAVARJA_VERSE), 2)
        self.assertIn("आगमस्य", EKAVARJA_VERSE[0])
        # निवृत्त्यर्थम् + एकवर्जम् joins, so the fragment
        # has to carry the junction.
        self.assertIn("निवृत्त्यर्थमेकवर्जं", EKAVARJA_VERSE[1])

    def test_both_halves_are_in_the_note(self):
        why = provisions_for("6.1.158")[0].why
        for half in EKAVARJA_VERSE:
            self.assertIn(half, why)

    def test_the_line_that_orders_them_is_recorded_too(self):
        self.assertIn("बाधको भवति", WHICH_WINS)
        self.assertIn("सतिशिष्टेन", provisions_for("6.1.158")[0].why)

    def test_the_report_carries_both_the_verse_and_the_ordering(self):
        answer = ekavarja()
        for half in EKAVARJA_VERSE:
            self.assertIn(half, answer.why)
        self.assertIn("बाधको भवति", answer.why)


class OneRuleBreaksTheParibhasaThatGovernsIt(unittest.TestCase):
    """
    6.1.200 अन्तश्च तवै युगपत् gives one word two accents at the same
    time, and the vṛtti names 6.1.158 as the reason युगपत् is said.
    """

    def test_it_is_the_only_row_that_puts_two(self):
        both = [r.sutra for r in ACCENT_TABLE if r.where == "ādi-anta"]
        self.assertEqual(both, ["6.1.200"])

    def test_and_it_names_the_heading_it_breaks(self):
        row = provisions_for("6.1.200")[0]
        self.assertIn("6.1.158", row.blocks)
        self.assertNotIn(row.sutra, row.blocks)

    def test_the_answer_reports_both_places_at_once(self):
        answer = accent_of(before="tavai")
        self.assertEqual(answer.sutra, "6.1.200")
        self.assertEqual(answer.where, "ādi-anta")

    def test_the_note_says_why_the_word_had_to_be_said(self):
        why = provisions_for("6.1.200")[0].why
        self.assertIn("युगपद्ग्रहणं पर्यायनिवृत्त्यर्थम्", why)
        self.assertIn("एकवर्जमिति वचनाद्", why)

    def test_no_other_rule_of_the_pada_names_the_heading(self):
        naming = [r.sutra for r in ACCENT_TABLE
                  if "6.1.158" in r.blocks]
        self.assertEqual(naming, ["6.1.200"])


class OneQuestionAnsweredThreeWays(unittest.TestCase):
    """
    Whether प्रत्ययलक्षण holds — whether an affix leaves its accent
    behind when it is elided. The pāda does not settle it once; it
    settles it rule by rule, and one rule exists only to say that it
    is not settled.
    """

    def test_two_rules_say_the_accent_survives(self):
        for code, phrase in (("6.1.191", "प्रत्ययलक्षणेनाप्ययं स्वर"),
                             ("6.1.198", "प्रत्ययलक्षणमत्रेष्यते")):
            self.assertIn(phrase, provisions_for(code)[0].why, code)

    def test_two_others_say_it_does_not(self):
        for code in ("6.1.197", "6.1.199"):
            self.assertIn("प्रत्ययलक्षण", provisions_for(code)[0].why,
                          code)
            self.assertIn("नेष्यते", provisions_for(code)[0].why, code)

    def test_and_one_rule_exists_only_to_prove_it_is_not_universal(self):
        """
        6.1.204 would be idle if the maxim held everywhere, and the
        vṛtti reads its idleness as the ज्ञापक.
        """
        why = provisions_for("6.1.204")[0].why
        self.assertIn("एतदेव ज्ञापयति", why)
        self.assertIn("स्वरविधौ प्रत्ययलक्षणं न भवतीति", why)

    def test_each_of_the_four_records_the_form_that_decides_it(self):
        for code, form in (("6.1.191", "सर्वस्तोमः"),
                           ("6.1.198", "सर्पिरागच्छ"),
                           ("6.1.197", "गर्गाः"),
                           ("6.1.199", "पथिप्रियः")):
            self.assertIn(form, provisions_for(code)[0].why, code)


class AMaximUsedInOnePlaceAndRefusedInAnother(unittest.TestCase):
    def test_the_maxim_is_recorded(self):
        self.assertIn("व्यञ्जनमविद्यमानवत्", VYANJANAM_AVIDYAMANAVAT)

    def test_the_last_rule_leans_on_it(self):
        self.assertIn("व्यञ्जनमविद्यमानवद्",
                      provisions_for("6.1.223")[0].why)

    def test_and_one_rule_names_an_augment_to_deny_it(self):
        """
        6.1.176 could have left the नुट् to the maxim. Naming it is
        what makes a consonant count, and मरुत्वान् is the form that
        turns on it.
        """
        why = provisions_for("6.1.176")[0].why
        self.assertIn("नाश्रीयते", why)
        self.assertIn("मरुत्वान्", provisions_for("6.1.176")[0].keeps_out)


class TheMarkersDoMostOfTheWork(unittest.TestCase):
    """
    Six markers, six placements, and each rule displaces 3.1.3's
    default accent on the affix.
    """

    MARKERS = {
        "cit": ("6.1.163", "udātta", "anta"),
        "ñit-nit": ("6.1.197", "udātta", "ādi"),
        "tit": ("6.1.185", "svarita", ""),
        "lit": ("6.1.193", "udātta", "pratyayāt-pūrva"),
        "rit": ("6.1.217", "udātta", "upottama"),
    }

    def test_each_marker_reaches_its_own_rule(self):
        for marker, (code, puts, where) in self.MARKERS.items():
            answer = accent_of(marker=marker)
            self.assertEqual(answer.sutra, code, marker)
            self.assertEqual(answer.puts, puts, marker)
            self.assertEqual(answer.where, where, marker)

    def test_only_one_of_them_gives_a_svarita(self):
        svarita = [r.sutra for r in ACCENT_TABLE if r.puts == "svarita"]
        self.assertEqual(svarita, ["6.1.185"])

    def test_a_marker_no_rule_names_reaches_nothing(self):
        self.assertEqual(accent_of(marker="ṅit").sutra, "")

    def test_one_affix_carrying_two_markers_is_settled_by_a_rule(self):
        """
        च्फञ् has a च् and a ञ्, and 6.1.163's and 6.1.197's accents
        would contradict. 6.1.164 is stated to give the च् its way,
        and the reason is that the ञ् still has 7.2.117's vṛddhi to
        do while the च् would have nothing left.
        """
        answer = accent_of(marker="cit", before="taddhita")
        self.assertEqual(answer.sutra, "6.1.164")
        self.assertEqual(answer.blocked_by, ("6.1.197",))
        self.assertIn("किमर्थमिदम्", provisions_for("6.1.164")[0].why)


class TheAccentIsPlacedFiveDifferentWays(unittest.TestCase):
    def test_all_five_placements_are_present(self):
        places = {r.where for r in ACCENT_TABLE if r.where}
        self.assertEqual(
            places,
            {"anta", "ādi", "upottama", "pratyayāt-pūrva", "ādi-anta",
             "matoḥ-pūrva-āt", "anywhere"})

    def test_the_penult_placement_needs_three_syllables(self):
        """
        उपोत्तम is defined at 6.1.180 — त्रिप्रभृतीनाम् अन्त्यम्
        उत्तमम्, तत्समीपे च यत् तद् उपोत्तमम् — and 6.1.218 leans on
        the same definition to keep दधत् out.
        """
        self.assertIn("त्रिप्रभृतीनाम्",
                      provisions_for("6.1.180")[0].why)
        self.assertIn("दधत्", provisions_for("6.1.218")[0].keeps_out)

    def test_counting_back_from_the_affix_is_a_separate_placement(self):
        for code in ("6.1.192", "6.1.193"):
            self.assertEqual(provisions_for(code)[0].where,
                             "pratyayāt-pūrva", code)


class OneFormCanTakeFourAccents(unittest.TestCase):
    """
    6.1.196 — the इट्, the ending, or the first syllable, and with
    6.1.193's a fourth. तेनैते चत्वारः स्वराः पर्यायेण भवन्ति.
    """

    def test_the_rule_answers_and_is_a_choice(self):
        answer = accent_of(before="thal-seṭ")
        self.assertEqual(answer.sutra, "6.1.196")
        self.assertTrue(answer.optional)

    def test_the_note_counts_the_alternatives(self):
        self.assertIn("चत्वारः स्वराः",
                      provisions_for("6.1.196")[0].why)

    def test_the_fourth_comes_from_the_rule_it_stands_beside(self):
        self.assertEqual(provisions_for("6.1.193")[0].marker, "lit")
        self.assertIn("ययाथ", provisions_for("6.1.196")[0].keeps_out)


class TwoListsAreDefinedByExclusion(unittest.TestCase):
    """
    आकृतिगण. उञ्छादि at 6.1.160 and वृषादि at 6.1.203, and the second
    says the membership rule outright — अविहितमाद्युदात्तत्वं वृषादिषु
    द्रष्टव्यम्. The same shape as 6.1.157's पारस्करप्रभृति.
    """

    def test_both_are_named(self):
        self.assertEqual(AKRTIGANA, ("uñchādi", "vṛṣādi"))

    def test_each_answers_by_its_own_rule(self):
        self.assertEqual(accent_of(gana="uñchādi").sutra, "6.1.160")
        self.assertEqual(accent_of(gana="vṛṣādi").sutra, "6.1.203")

    def test_they_place_the_accent_at_opposite_ends(self):
        self.assertEqual(provisions_for("6.1.160")[0].where, "anta")
        self.assertEqual(provisions_for("6.1.203")[0].where, "ādi")

    def test_the_second_states_the_membership_rule(self):
        # वृषादिः + आकृतिगणः joins into वृषादिराकृतिगणः, so
        # the fragment has to carry the junction here too.
        why = provisions_for("6.1.203")[0].why
        self.assertIn("वृषादिराकृतिगणः", why)
        self.assertIn("अविहितमाद्युदात्तत्वं", why)

    def test_and_the_pada_holds_a_third_list_of_that_shape(self):
        """
        6.1.157's पारस्करप्रभृति is the same device in the सुट्
        section, and the two are worth seeing together.
        """
        from src.astadhyayi.sut import provisions_for as sut_rows

        self.assertIn("प्रभृतिराकृतिगणः", sut_rows("6.1.157")[0].why)


class ASenseCanBeWhatDecides(unittest.TestCase):
    def test_two_rules_name_one_word_each_and_differ_only_by_sense(self):
        first = provisions_for("6.1.201")[0]
        second = provisions_for("6.1.202")[0]
        self.assertEqual(first.where, second.where)
        self.assertEqual(first.blocks, second.blocks)
        self.assertNotEqual(first.result, second.result)

    def test_each_answers_only_in_its_own_sense(self):
        self.assertEqual(
            accent_of("kṣaya", result="nivāsa").sutra, "6.1.201")
        self.assertEqual(
            accent_of("jaya", result="karaṇa").sutra, "6.1.202")

    def test_the_wrong_sense_reaches_neither(self):
        self.assertEqual(accent_of("kṣaya", result="karaṇa").sutra, "")
        self.assertEqual(accent_of("kṣaya").sutra, "")

    def test_a_participle_is_accented_by_which_karaka_it_names(self):
        """
        6.1.207 — आशित accents its first syllable of the EATER, and
        keeps 6.2.144's end-accent of the food and of the eating.
        One form, three कारक, two accents.
        """
        answer = accent_of("āśita", result="kartṛ")
        self.assertEqual(answer.sutra, "6.1.207")
        self.assertEqual(answer.blocked_by, ("6.2.144",))
        self.assertEqual(accent_of("āśita").sutra, "")


class TheCorpusConditionsRunBothWays(unittest.TestCase):
    def test_two_rules_want_the_vedic_corpus(self):
        vedic = [r.sutra for r in ACCENT_TABLE if r.chandasi]
        self.assertEqual(vedic, ["6.1.170", "6.1.178", "6.1.209"])

    def test_one_wants_a_mantra_in_particular(self):
        in_mantra = [r.sutra for r in ACCENT_TABLE if r.mantra]
        self.assertEqual(in_mantra, ["6.1.210"])

    def test_and_exactly_one_wants_the_language_NOT_to_be_vedic(self):
        ordinary = [r.sutra for r in ACCENT_TABLE if r.bhasayam]
        self.assertEqual(ordinary, ["6.1.181"])

    def test_that_one_loosens_what_the_rule_before_it_fixed(self):
        fixed = accent_of(gana="ṣaṭ", before="jhalādi-vibhakti")
        self.assertEqual(fixed.sutra, "6.1.180")
        self.assertFalse(fixed.optional)

        loose = accent_of(gana="ṣaṭ", before="jhalādi-vibhakti",
                          bhasayam=True)
        self.assertEqual(loose.sutra, "6.1.181")
        self.assertTrue(loose.optional)
        self.assertEqual(loose.blocked_by, ("6.1.180",))

    def test_and_the_mantra_rule_fixes_what_the_corpus_rule_loosened(self):
        loose = accent_of("juṣṭa", chandasi=True)
        self.assertEqual(loose.sutra, "6.1.209")
        self.assertTrue(loose.optional)

        fixed = accent_of("juṣṭa", mantra=True)
        self.assertEqual(fixed.sutra, "6.1.210")
        self.assertFalse(fixed.optional)
        self.assertEqual(fixed.blocked_by, ("6.1.209",))


class ARefusalNamesWhatItTakesTheAccentFrom(unittest.TestCase):
    def setUp(self):
        self.refusing = [r for r in ACCENT_TABLE if r.refuses]

    def test_there_are_three_of_them(self):
        self.assertEqual([r.sutra for r in self.refusing],
                         ["6.1.175", "6.1.182", "6.1.183", "6.1.184"])

    def test_none_names_itself(self):
        for row in self.refusing:
            self.assertNotIn(row.sutra, row.blocks, row.sutra)

    def test_each_names_a_rule_that_comes_before_it(self):
        for row in self.refusing:
            self.assertTrue(row.blocks, row.sutra)
            for blocked in row.blocks:
                self.assertLess(_order(blocked), _order(row.sutra),
                                "%s names %s" % (row.sutra, blocked))

    def test_a_refusal_reports_no_accent_and_no_place(self):
        answer = accent_of("div", before="jhalādi-vibhakti")
        self.assertEqual(answer.sutra, "6.1.183")
        self.assertEqual(answer.puts, "")
        self.assertEqual(answer.where, "")
        self.assertEqual(answer.blocked_by, ("6.1.168", "6.1.171"))

    def test_and_it_does_not_govern_what_it_excepts(self):
        """
        दिवा and दिवे are vowel-initial, so 6.1.171 still gives them
        the accent and 6.1.183 has nothing to say about them.
        """
        elsewhere = accent_of("div", before="asarvanāmasthāna")
        self.assertEqual(elsewhere.sutra, "6.1.171")
        self.assertEqual(elsewhere.puts, "udātta")

    def test_asking_for_an_accent_never_returns_a_refusal(self):
        asked = accent_of("div", before="jhalādi-vibhakti",
                          wants="udātta")
        self.assertEqual(asked.sutra, "")


class TheSectionIsWhereItSaysItIs(unittest.TestCase):
    def test_every_rule_here_is_registered_against_this_resolver(self):
        for row in ACCENT_TABLE:
            self.assertEqual(REGISTRY.get(row.sutra).apply.__name__,
                             "accent_of", row.sutra)

    def test_the_whole_pada_is_contiguous(self):
        """
        6.1.1 to 6.1.223, with no gap. The first pāda of अध्याय ६
        read end to end.
        """
        for n in range(1, 224):
            self.assertTrue(REGISTRY.has("6.1.%d" % n), n)

    def test_and_the_next_pada_has_begun_on_this_rule(self):
        """
        6.2.1 बहुव्रीहौ प्रकृत्या पूर्वपदम् is codified now, and
        what it opens is the exceptions to 6.1.223 — the last rule
        of THIS table. The debt this test was written as is paid,
        and what replaces it is the dependency: the next pāda has
        nothing to except unless this one supplied something.
        """
        self.assertTrue(REGISTRY.has("6.2.1"))
        self.assertEqual(accent_of(before="samāsa").sutra, "6.1.223")
        self.assertIn("6.1.223",
                      REGISTRY.get("6.2.1").notes)


class NothingAnswersByDefault(unittest.TestCase):
    def test_an_unreached_question_gets_nothing(self):
        answer = accent_of(before="hal")
        self.assertEqual(answer.sutra, "")
        self.assertEqual(answer.puts, "")

    def test_and_the_message_says_the_heading_speaks_for_no_rule(self):
        self.assertIn("6.1.158", accent_of(before="hal").why)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in ACCENT_TABLE:
            self.assertGreater(len(row.why), 100, row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in ACCENT_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_module_does_not_mark_the_syllable(self):
        """
        `accent_of` says which rule puts the accent and where. It
        does not write it: the corpus is accented already, and
        `svara` holds what an उदात्त, an अनुदात्त and a स्वरित are.
        """
        answer = accent_of(before="dhātu")
        self.assertEqual(answer.puts, "udātta")
        self.assertEqual(answer.where, "anta")
        self.assertNotIn("पचति", str(answer.where))

    def test_the_pada_that_holds_the_exceptions_is_complete(self):
        """
        6.1.223 समासस्य says a compound is end-accented and 6.2 is
        nothing but the exceptions to it. The debt is collected:
        6.2.144, which 6.1.207 is stated against, is codified, so
        the citation can be ASKED instead of asserted — and what
        comes back is the accent 6.1.207 said it would lose to.
        """
        from src.astadhyayi.uttarapada_svara import second_member

        self.assertEqual(accent_of(before="samāsa").sutra, "6.1.223")
        self.assertIn("6.2.144", provisions_for("6.1.207")[0].blocks)
        got = second_member(affix="ghañ", purvapada_gana="gati")
        self.assertEqual(got.sutra, "6.2.144")
        self.assertEqual(got.where, "anta")


if __name__ == "__main__":
    unittest.main()
