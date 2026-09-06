# -*- coding: utf-8 -*-
"""
६.४.९६–११४ — the losses that make a Sanskrit present tense.

Most of the finite verb's shape is in this run, so the tests are
about the arguments rather than the entries.

**One affix in five shapes.** हि becomes धि, or is dropped, or
stands — across five sūtras that are not five in a row, 6.4.104
standing in the middle of them about something else.

**A pair told apart only by नित्यम्.** 6.4.107 and 6.4.108 do the
same thing to the same sound before the same affixes, and the
whole difference is one word.

**And a class that is sometimes an alternative to a named stem and
sometimes a conjunction with one.** 6.4.101's हुझल्भ्यः is a
dvandva; 6.4.108's करोतेः stands with a उ-affix carried down. A
table that read the two the same way gets कुर्वः for सुन्वः.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.anga_agama import AGAMA_RUN
from src.astadhyayi.sarvadhatuka_lopa import (
    DHI_CHANDASI, GAMA_FIVE, SARVA_RUN, SARVA_TABLE,
    before_sarvadhatuka, provisions_for)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunFollowsTheOneBeforeIt(unittest.TestCase):
    def test_it_opens_one_sutra_after_the_augment_run(self):
        self.assertEqual(_n(SARVA_RUN[0])[2],
                         _n(AGAMA_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_96_to_114(self):
        got = [row.sutra for row in SARVA_TABLE]
        self.assertEqual(got, ["6.4.%d" % n
                               for n in range(96, 115)])

    def test_every_row_carries_its_reason(self):
        for row in SARVA_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = before_sarvadhatuka("kṛ", before="tip")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("stands as it is", got.why)


class OneAffixInFiveShapes(unittest.TestCase):
    """
    हि becomes धि after हु and a झल् (6.4.101), and after five
    roots in the Veda (6.4.102), and where it is not ङित् (6.4.103);
    it is dropped after an अ (6.4.105) and after a उ-affix
    (6.4.106); and everywhere else it stands.

    Five sūtras, and NOT five in a row: 6.4.104 चिणो लुक् stands
    in the middle of them and is about something else. Asserting
    a contiguous block would have been asserting something false
    about the text.
    """

    def test_five_rules_are_about_it_and_they_are_not_in_a_row(
            self):
        about_hi = [row.sutra for row in SARVA_TABLE
                    if "hi" in row.before]
        self.assertEqual(about_hi, ["6.4.101", "6.4.102",
                                    "6.4.103", "6.4.105",
                                    "6.4.106"])
        # 6.4.104 sits between them and is about the affix after
        # चिण्, so the हि rules are a block with a hole in it.
        between, = provisions_for("6.4.104")
        self.assertEqual(between.before, ("ciṇ",))

    def test_three_make_it_dhi(self):
        got = {row.sutra for row in SARVA_TABLE
               if row.does == "dhi"}
        self.assertEqual(got, {"6.4.101", "6.4.102", "6.4.103"})

    def test_and_two_drop_it(self):
        for query, code in (
                ({"gana": "a-anta"}, "6.4.105"),
                ({"gana": "u-pratyaya-anta"}, "6.4.106")):
            got = before_sarvadhatuka(before="hi", **query)
            self.assertEqual((got.sutra, got.does),
                             (code, "lopa"), code)

    def test_the_vedic_one_says_another_rule_cannot_reach_it(self):
        """
        **शृणुधीत्यत्र धिभावविधानसामर्थ्याद् उतश्च प्रत्ययाद्० न
        भवति** — 6.4.106 would have dropped the हि after शृणु
        altogether, and 6.4.102's giving it a shape shows it does
        not.
        """
        row, = provisions_for("6.4.102")
        self.assertIn("धिभावविधानसामर्थ्याद्", row.why)
        self.assertIn("śṛṇu", DHI_CHANDASI)
        got = before_sarvadhatuka("śṛṇu", before="hi",
                                  chandasi=True)
        self.assertEqual(got.sutra, "6.4.102")

    def test_and_the_last_of_them_turns_on_a_marker_not_being_there(
            self):
        row, = provisions_for("6.4.103")
        self.assertEqual(row.result, ("aṅit",))
        self.assertIn("पित्त्वेनास्याङित्त्वम्", row.why)


class APairToldApartOnlyByNityam(unittest.TestCase):
    """
    6.4.107 drops the उ of a उ-affix optionally before व् and म्;
    6.4.108 does the same for कृ and says नित्यम्. Nothing else
    separates them, so the table has to weigh the word.
    """

    def test_they_act_on_the_same_sound_before_the_same_affixes(
            self):
        loose, = provisions_for("6.4.107")
        firm, = provisions_for("6.4.108")
        self.assertEqual(loose.does, firm.does)
        self.assertEqual(loose.before, firm.before)
        self.assertEqual(loose.gana, firm.gana)

    def test_and_only_one_of_them_names_a_stem(self):
        loose, = provisions_for("6.4.107")
        firm, = provisions_for("6.4.108")
        self.assertEqual(loose.of, ())
        self.assertEqual(firm.of, ("kṛ",))

    def test_the_option_answers_for_the_class(self):
        got = before_sarvadhatuka(gana="u-pratyaya-anta",
                                  before="va")
        self.assertEqual(got.sutra, "6.4.107")
        self.assertTrue(got.optional)
        self.assertFalse(got.nitya)

    def test_and_the_compulsory_one_for_the_stem(self):
        got = before_sarvadhatuka("kṛ", gana="u-pratyaya-anta",
                                  before="va")
        self.assertEqual(got.sutra, "6.4.108")
        self.assertTrue(got.nitya)
        self.assertFalse(got.optional)

    def test_the_note_carries_what_the_form_then_escapes(self):
        """**न भकुर्छुराम् इति प्रतिषिध्यते** — कुर्वः would
        otherwise be lengthened by 8.2.77, and 8.2.79 names कुर्
        out."""
        row, = provisions_for("6.4.108")
        for cited in ("8.2.77", "8.2.79", "1.1.58"):
            self.assertIn(cited, row.why, cited)

    def test_and_those_two_rules_have_since_landed(self):
        # Written as a debt when neither was codified. 8.2.77
        # हलि च lengthens the इक् before a र् or व्, and 8.2.79
        # न भकुर्छुराम् names कुर् out of it — so कुर्वः can be
        # asked against the rule that spares it, and both are
        # in पाद ८.२.
        for code in ("8.2.77", "8.2.79"):
            self.assertTrue(REGISTRY.has(code), code)


class AClassIsSometimesAnAlternativeAndSometimesNot(
        unittest.TestCase):
    """
    6.4.101 हुझल्भ्यः is a dvandva in the ablative — हु OR a
    झल्-final stem. 6.4.108 करोतेः names a stem and takes the
    उ-affix by anuvṛtti — कृ AND the class. Reading the two the
    same way gives कुर्वः where सुन्वः belongs.
    """

    def test_the_conjunctive_ones_are_marked(self):
        got = {row.sutra for row in SARVA_TABLE if row.and_gana}
        self.assertEqual(got, {"6.4.108", "6.4.109", "6.4.110"})

    def test_either_half_reaches_the_alternative_one(self):
        for query in ({"stem": "hu"}, {"gana": "jhal-anta"}):
            got = before_sarvadhatuka(before="hi",
                                      result="hal-ādi", **query)
            self.assertEqual(got.sutra, "6.4.101", query)

    def test_but_both_halves_are_wanted_by_the_conjunctive_one(
            self):
        self.assertEqual(
            before_sarvadhatuka("kṛ", before="va").sutra, "")
        self.assertEqual(
            before_sarvadhatuka("kṛ", gana="u-pratyaya-anta",
                                before="va").sutra, "6.4.108")

    def test_and_the_class_alone_falls_to_the_option(self):
        self.assertEqual(
            before_sarvadhatuka(gana="u-pratyaya-anta",
                                before="va").sutra, "6.4.107")


class TheRulesThatMakeThePresentTense(unittest.TestCase):
    """
    6.4.111 takes the अ of श्न and of अस्; 6.4.112 takes the आ of
    श्ना and of a reduplicated stem; 6.4.113 makes that same आ
    into ई before a consonant. Between them, the seventh and ninth
    classes and the verb *to be*.
    """

    def test_the_seventh_class_and_the_verb_to_be(self):
        for query in ({"gana": "śna"}, {"stem": "as"}):
            got = before_sarvadhatuka(
                before="sārvadhātuka", part="a", result="kṅit",
                **query)
            self.assertEqual((got.sutra, got.does),
                             ("6.4.111", "lopa"), query)

    def test_the_ninth_class_loses_its_a_before_a_vowel(self):
        got = before_sarvadhatuka("śnā", before="sārvadhātuka",
                                  part="ā", result="kṅit")
        self.assertEqual((got.sutra, got.does), ("6.4.112", "lopa"))

    def test_and_shortens_it_to_i_before_a_consonant(self):
        got = before_sarvadhatuka(gana="śnā-abhyasta",
                                  before="sārvadhātuka", part="ā",
                                  result="hal-ādi")
        self.assertEqual((got.sutra, got.does), ("6.4.113", "īt"))

    def test_the_ghu_class_is_kept_out_of_the_second_of_those(self):
        row, = provisions_for("6.4.113")
        self.assertEqual(row.excludes, ("ghu",))
        self.assertIn("दत्तः", row.keeps_out)

    def test_and_one_rule_reaches_an_affix_that_is_gone(self):
        """
        **सार्वधातुकग्रहणं किम्? भूतपूर्वेऽपि सार्वधातुके यथा
        स्यात् — कुरु** — the हि has already been dropped by
        6.4.106, and 6.4.110 still has to reach what once stood
        before one.
        """
        row, = provisions_for("6.4.110")
        self.assertIn("भूतपूर्वेऽपि", row.why)


class TheWholeAoristPassiveIsOneRule(unittest.TestCase):
    """
    6.4.104 चिणो लुक् — and अकारि, अहारि, अलावि, अपाचि are the
    whole of the Sanskrit aorist passive third singular.
    """

    def test_it_is_the_only_luk_of_the_run(self):
        got = {row.sutra for row in SARVA_TABLE
               if row.does == "luk"}
        self.assertEqual(got, {"6.4.104"})

    def test_it_names_no_stem_at_all(self):
        row, = provisions_for("6.4.104")
        self.assertEqual(row.of, ())
        self.assertEqual(row.gana, "")

    def test_and_the_luk_does_not_reach_past_the_ending(self):
        """
        **तलोपस्यासिद्धत्वात् तरप्तमपोर् न लुग् भवति** — the तिप्
        is gone and 6.4.22 hides that, so the तरप् is no longer
        *after चिण्*.
        """
        row, = provisions_for("6.4.104")
        # The fragment begins after the junction: तलोपस्य +
        # असिद्धत्वात् swallows the अ.
        self.assertIn("सिद्धत्वात्", row.why)
        self.assertIn("विषयभेदाद्", row.why)
        self.assertTrue(REGISTRY.has("6.4.22"))


class WhatIsKeptOutIsNamed(unittest.TestCase):
    def test_five_roots_lose_a_penult_and_one_affix_is_excepted(
            self):
        self.assertEqual(len(GAMA_FIVE), 5)
        row, = provisions_for("6.4.98")
        self.assertEqual(row.of, GAMA_FIVE)
        self.assertEqual(row.excludes, ("aṅ",))
        self.assertEqual(
            before_sarvadhatuka("gam", before="ac", result="aṅ"
                                ).sutra, "")

    def test_and_the_first_rule_of_the_run_excepts_two_preverbs(
            self):
        row, = provisions_for("6.4.96")
        self.assertEqual(row.excludes, ("dvi-upasarga",))
        self.assertIn("समुपच्छादः", row.keeps_out)

    def test_and_says_what_its_own_existence_sets_aside(self):
        row, = provisions_for("6.4.96")
        self.assertIn("वचनसामर्थ्याद्", row.why)
        for cited in ("6.4.22", "1.1.56"):
            self.assertIn(cited, row.why, cited)


class WantsFiltersByTheOperation(unittest.TestCase):
    def test_asking_for_the_one_it_does(self):
        self.assertEqual(
            before_sarvadhatuka(before="ciṇ", wants="luk").sutra,
            "6.4.104")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            before_sarvadhatuka(before="ciṇ", wants="lopa").sutra,
            "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in SARVA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in SARVA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)

    def test_and_the_two_codified_before_the_pada_survive(self):
        for code in ("6.4.22", "6.4.77"):
            self.assertTrue(REGISTRY.has(code), code)
            self.assertGreater(len(REGISTRY.get(code).notes), 200,
                               code)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.4.115 भियोऽन्यतरस्याम् opens
    the next stretch, and 6.4.115 to 6.4.175 is ahead.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.4.115 भियोन्यतरस्याम् opens the perfect's ए and the
        loss of its copy. The debt is collected, and the claim is
        the join: it starts one sūtra past this run, and where
        this run takes a sound away that run takes a whole
        syllable.
        """
        from src.astadhyayi.abhyasa_lopa import in_the_perfect

        self.assertTrue(REGISTRY.has("6.4.115"))
        self.assertEqual(_n("6.4.115")[2], _n(SARVA_RUN[1])[2] + 1)
        self.assertEqual(
            in_the_perfect(before="liṭ", result="kṅit").does,
            "et-abhyāsalopa")
        self.assertEqual(
            {row.does for row in SARVA_TABLE} & {"et-abhyāsalopa"},
            set())

    def test_and_the_pada_is_complete_now(self):
        # Written as a debt while 6.4.175 was ahead; the pāda has
        # been read through, so the claim is the live one.
        self.assertTrue(REGISTRY.has("6.4.175"))
        self.assertFalse(REGISTRY.has("6.4.176"))

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 115):
            self.assertTrue(REGISTRY.has("6.4.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
