# -*- coding: utf-8 -*-
"""
६.३.९६–११३ — the alterations that would not group.

The run has no single theme, and what has to be tested is
therefore not a shape but three particular arguments:

**A later rule beating an earlier one by standing later.** 6.3.105
and 6.3.101 both reach कु before a vowel, and the vṛtti settles it
by परत्व alone.

**An option that only gives what was not already due.** 6.3.106's
विभाषा is अप्राप्त: in the sense *a little* 6.3.105 has already
made का compulsory, so the option is about contempt only.

**And a rule whose content is that the grammar does not reach.**
6.3.109 पृषोदरादीनि यथोपदिष्टम् — and the vṛtti then analyses the
words anyway, so what is unlicensed is the operation and not the
form.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.nan_saha_samana import NAN_RUN
from src.astadhyayi.purvapada_vikara import (
    DUK_NINE, KU_SHAPES, PRSODARADI, VIKARA_RUN, VIKARA_TABLE,
    altered, provisions_for)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunFollowsTheOneBeforeIt(unittest.TestCase):
    def test_it_opens_one_sutra_after_the_particles_close(self):
        self.assertEqual(_n(VIKARA_RUN[0])[2], _n(NAN_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_96_to_113(self):
        got = [row.sutra for row in VIKARA_TABLE]
        self.assertEqual(got, ["6.3.%d" % n for n in range(96, 114)])

    def test_every_row_carries_its_reason(self):
        for row in VIKARA_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_every_row_names_what_it_does(self):
        for row in VIKARA_TABLE:
            self.assertTrue(row.becomes, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = altered("aśva", before="pati")
        self.assertEqual((got.becomes, got.sutra), ("", ""))
        self.assertIn("stands as it was", got.why)


class SahaTakesAThirdShapeHere(unittest.TestCase):
    """
    सह has now been given three substitutes in one pāda — स at
    6.3.78, सध्रि at 6.3.95, सध here — and held back once at
    6.3.83. No other stem in the pāda is worked over so often.
    """

    def test_the_third_one_is_vedic_and_conditioned(self):
        row, = provisions_for("6.3.96")
        self.assertEqual(row.becomes, "sadha")
        self.assertTrue(row.chandasi)
        self.assertEqual(
            altered("saha", before="māda", chandasi=True).sutra,
            "6.3.96")

    def test_and_outside_the_veda_it_is_not_reached(self):
        self.assertEqual(altered("saha", before="māda").sutra, "")

    def test_the_other_two_are_in_the_run_before(self):
        from src.astadhyayi.nan_saha_samana import (
            provisions_for as nan_for)

        for code, shape in (("6.3.78", "sa"), ("6.3.95", "sadhri")):
            row, = nan_for(code)
            self.assertEqual(row.becomes, shape, code)


class KuIsGivenThreeShapesAcrossEightSutras(unittest.TestCase):
    """
    कद्, का and कवम् — 6.3.101 to 6.3.108, more rules than any
    other stem of the pāda gets, and the three shapes overlap,
    so that one word can stand in two or three forms at once.
    """

    def test_the_three_shapes_are_these(self):
        got = tuple(dict.fromkeys(
            row.becomes for row in VIKARA_TABLE
            if row.of == ("ku",)))
        self.assertEqual(got, KU_SHAPES)

    def test_eight_sutras_give_them(self):
        got = [row.sutra for row in VIKARA_TABLE
               if row.of == ("ku",)]
        self.assertEqual(got, ["6.3.%d" % n
                               for n in range(101, 109)])

    def test_the_first_wants_a_vowel_and_a_tatpurusa(self):
        row, = provisions_for("6.3.101")
        self.assertEqual(row.before, ("ac",))
        self.assertEqual(row.samasa, "tatpuruṣa")
        self.assertEqual(altered("ku", before="ac").sutra, "")

    def test_and_two_second_members_get_kad_without_either(self):
        for word in ("ratha", "vada"):
            got = altered("ku", before=word)
            self.assertEqual((got.sutra, got.becomes),
                             ("6.3.102", "kad"), word)


class ALaterRuleBeatsAnEarlierOneByStandingLater(unittest.TestCase):
    """
    **अजादावपि परत्वात् कादेश एव भवति। काम्लम्, कोष्णम्** —
    6.3.101 would have given कद् before a vowel and 6.3.105 takes
    it. Nothing in the conditions decides this; only the numbers
    do, and the table has to record it.
    """

    def test_the_earlier_rule_reaches_the_same_ground(self):
        earlier, = provisions_for("6.3.101")
        self.assertEqual(earlier.before, ("ac",))
        self.assertEqual(
            altered("ku", before="ac", samasa="tatpuruṣa").sutra,
            "6.3.101")

    def test_and_the_later_one_takes_it(self):
        got = altered("ku", before="ac", samasa="tatpuruṣa",
                      result="īṣad")
        self.assertEqual((got.sutra, got.becomes), ("6.3.105", "kā"))

    def test_the_later_one_says_what_it_displaces(self):
        row, = provisions_for("6.3.105")
        self.assertEqual(row.blocks, ("6.3.101",))
        self.assertIn("परत्वात्", row.why)


class AnOptionThatOnlyGivesWhatWasNotDue(unittest.TestCase):
    """
    **अप्राप्तविभाषेयम्। ईषदर्थे तु पूर्वविप्रतिषेधेन नित्यं का
    भवति** — 6.3.106's option is about contempt only, because in
    the sense *a little* 6.3.105 has already made का compulsory.
    """

    def test_the_option_is_carried_through(self):
        got = altered("ku", before="puruṣa")
        self.assertEqual(got.sutra, "6.3.106")
        self.assertTrue(got.optional)

    def test_but_in_the_other_sense_it_is_compulsory(self):
        got = altered("ku", before="puruṣa", result="īṣad")
        self.assertEqual(got.sutra, "6.3.105")
        self.assertFalse(got.optional)

    def test_and_the_note_says_which_rule_wins_and_how(self):
        row, = provisions_for("6.3.106")
        self.assertIn("अप्राप्तविभाषेयम्", row.why)
        self.assertIn("पूर्वविप्रतिषेधेन", row.why)


class OneWordCanStandInThreeFormsAtOnce(unittest.TestCase):
    """
    6.3.107 gives कवोष्णम्, and का beside it gives कोष्णम्, and
    6.3.101's कद् gives कदुष्णम् — three forms of one word from
    three rules, none of which displaces the others.
    """

    def test_the_named_substitute_answers(self):
        got = altered("ku", before="uṣṇa")
        self.assertEqual((got.sutra, got.becomes),
                         ("6.3.107", "kavam"))
        self.assertTrue(got.optional)

    def test_and_the_note_gives_all_three_forms(self):
        row, = provisions_for("6.3.107")
        for form in ("कवोष्णम्", "कोष्णम्", "कदुष्णम्"):
            self.assertIn(form, row.why, form)

    def test_the_vedic_road_rule_does_the_same(self):
        row, = provisions_for("6.3.108")
        for form in ("कवपथः", "कापथः", "कुपथः"):
            self.assertIn(form, row.why, form)
        self.assertEqual(row.blocks, ("6.3.104",))


class ARuleWhoseContentIsThatTheGrammarDoesNotReach(
        unittest.TestCase):
    """
    6.3.109 licenses forms no rule describes — **येषु
    लोपागमवर्णविकाराः शास्त्रेण न विहिता दृश्यन्ते च** — and then
    the vṛtti derives them by hand. What is unlicensed is the
    operation, not the form, and the record has to keep both.
    """

    def test_it_names_no_stem_and_no_environment(self):
        row, = provisions_for("6.3.109")
        self.assertEqual(row.of, ())
        self.assertEqual(row.before, ())
        self.assertEqual(row.becomes, "yathopadiṣṭam")

    def test_and_is_reached_only_by_naming_the_gana(self):
        self.assertEqual(altered(gana="pṛṣodarādi").sutra,
                         "6.3.109")
        self.assertEqual(altered("pṛṣodara").sutra, "")

    def test_the_note_analyses_the_words_it_licenses(self):
        row, = provisions_for("6.3.109")
        self.assertEqual(len(PRSODARADI), 3)
        for word, cited in (("pṛṣodara", "पृषदुदरं"),
                            ("balāhaka", "वारिवाहको"),
                            ("jīmūta", "जीवनस्य")):
            self.assertIn(word, PRSODARADI, word)
            self.assertIn(cited, row.why, cited)

    def test_and_it_appeals_to_usage_and_not_to_licence(self):
        row, = provisions_for("6.3.109")
        self.assertIn("शिष्टैरुच्चारितानि", row.why)


class ALossThatLengthensWhatCameBefore(unittest.TestCase):
    """
    6.3.111 is the only rule of the run that reaches outside a
    compound, and it says so: **पूर्वग्रहणम् अनुत्तरपदेऽपि
    पूर्वमात्रस्य दीर्घार्थम्** — 6.3.1's उत्तरपदे is still
    running, and लीढम् is one word.
    """

    def test_it_is_reached_by_the_loss_and_not_by_a_stem(self):
        row, = provisions_for("6.3.111")
        self.assertEqual(row.of, ())
        self.assertEqual(row.result, ("ḍhra-lopa",))
        self.assertEqual(altered(result="ḍhra-lopa").sutra,
                         "6.3.111")

    def test_and_the_note_frees_it_from_the_pada_s_heading(self):
        from src.astadhyayi.aluk import UTTARAPADE_RUN

        row, = provisions_for("6.3.111")
        self.assertIn("अनुत्तरपदेऽपि", row.why)
        self.assertLessEqual(_n(row.sutra), _n(UTTARAPADE_RUN[1]))

    def test_two_roots_get_a_substitute_instead(self):
        for root in ("sah", "vah"):
            got = altered(root, result="ḍhra-lopa")
            self.assertEqual((got.sutra, got.becomes),
                             ("6.3.112", "ot"), root)

    def test_and_that_rule_says_what_it_displaces(self):
        row, = provisions_for("6.3.112")
        self.assertEqual(row.blocks, ("6.3.111",))

    def test_the_word_varna_is_there_to_catch_the_strengthened_vowel(
            self):
        """**वर्णग्रहणं किम्? कृतायामपि वृद्धौ यथा स्यात्** —
        written अत् it would have taken only the short अ, by
        1.1.70."""
        row, = provisions_for("6.3.112")
        self.assertIn("वर्णग्रहणं किम्", row.why)
        self.assertIn("तपरत्वाद्", row.why)
        self.assertTrue(REGISTRY.has("1.1.70"))


class AFormLaidDownIsStillTakenApart(unittest.TestCase):
    """
    6.3.113 lays down three Vedic forms whole, and the vṛtti
    accounts for each of them anyway — a क्त्वा without the ओ, the
    same क्त्वा turned to ध्यै, and a तृच्.
    """

    def test_it_is_the_only_nipatana_of_the_run(self):
        got = {row.sutra for row in VIKARA_TABLE if row.nipatana}
        self.assertEqual(got, {"6.3.113"})

    def test_it_is_vedic_only(self):
        self.assertEqual(altered("sah", result="nigama").sutra,
                         "6.3.113")
        row, = provisions_for("6.3.113")
        self.assertIn("भाषायाम्", row.keeps_out)

    def test_and_the_note_accounts_for_each_of_the_three(self):
        row, = provisions_for("6.3.113")
        for cited in ("ओत्त्वाभावः", "ध्यैभावः", "तृचि"):
            self.assertIn(cited, row.why, cited)


class TheListsAreTheVrttisOwn(unittest.TestCase):
    def test_the_nine_before_which_anya_takes_duk(self):
        self.assertEqual(len(DUK_NINE), 9)
        row, = provisions_for("6.3.99")
        self.assertEqual(row.before, DUK_NINE)
        for word in DUK_NINE:
            self.assertEqual(altered("anya", before=word).sutra,
                             "6.3.99", word)

    def test_and_the_tenth_is_a_separate_sutra_and_optional(self):
        got = altered("anya", before="artha")
        self.assertEqual(got.sutra, "6.3.100")
        self.assertTrue(got.optional)
        self.assertNotIn("artha", DUK_NINE)

    def test_two_cases_keep_the_augment_out(self):
        row, = provisions_for("6.3.99")
        self.assertEqual(row.excludes, ("ṣaṣṭhī", "tṛtīyā"))
        for case in ("ṣaṣṭhī", "tṛtīyā"):
            self.assertEqual(
                altered("anya", before="āśis", result=case).sutra,
                "", case)


class WantsFiltersByTheAlteration(unittest.TestCase):
    def test_asking_for_the_one_it_gives(self):
        self.assertEqual(
            altered("ku", before="pathin", wants="kā").sutra,
            "6.3.104")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            altered("ku", before="pathin", wants="kad").sutra, "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in VIKARA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in VIKARA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.3.114 संहितायाम् opens the
    pāda's last heading and its last twenty-six rules, every one
    of them a lengthening, ending at 6.3.139 where 6.3.1's
    उत्तरपदे runs out.
    """

    def test_the_last_run_of_the_pada_has_landed(self):
        """
        6.3.114 संहितायाम् opens the pāda's last heading. The debt
        is collected, and the claim is the join: it starts one
        sūtra past this run, and it holds only in connected
        speech, which nothing in this run required.
        """
        from src.astadhyayi.dirgha_samhita import (
            SAMHITA_RUN, lengthens)

        self.assertTrue(REGISTRY.has("6.3.114"))
        self.assertTrue(REGISTRY.has("6.3.139"))
        self.assertEqual(_n("6.3.114")[2], _n(VIKARA_RUN[1])[2] + 1)
        self.assertEqual(SAMHITA_RUN, ("6.3.114", "6.3.139"))
        self.assertEqual(
            lengthens(gana="lakṣaṇa", before="karṇa").does,
            "dīrgha")

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 114):
            self.assertTrue(REGISTRY.has("6.3.%d" % n), n)

    def test_and_the_heading_it_will_close_under_is_codified(self):
        from src.astadhyayi.aluk import UTTARAPADE_RUN

        self.assertTrue(REGISTRY.has(UTTARAPADE_RUN[0]))
        self.assertEqual(UTTARAPADE_RUN[1], "6.3.139")


if __name__ == "__main__":
    unittest.main()
