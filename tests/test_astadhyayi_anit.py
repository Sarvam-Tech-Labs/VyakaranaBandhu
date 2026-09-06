# -*- coding: utf-8 -*-
"""
७.२.८–३४ — where the इट् does NOT come, stated before it is given.

The whole point of the run is its position: 7.2.35 gives the
augment and stands after all twenty-seven of these. So the tests
start there — what the module answers when no rule is reached is
`iṭ`, not silence — and then follow the two kinds of refusal, the
निष्ठा heading, and the lexical block inside it.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.anit import (
    ANIT_RUN,
    ANIT_TABLE,
    CHANDASI_ISLANDS,
    DANTA_SEVEN,
    KRADI_EIGHT,
    NIPATANA_EIGHT,
    NISTHA_FROM,
    NISTHA_TO,
    RUSYAMADI,
    THE_RULE_ITSELF,
    TITUTRA,
    no_it,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheRunIsStatedBeforeItsRule(unittest.TestCase):
    """7.2.35 gives the इट्, and stands after all of these."""

    def test_the_default_answer_is_the_augment_and_not_silence(self):
        # A root no rule of the run names takes the इट् by
        # 7.2.35, so the resolver says so rather than shrugging.
        got = no_it("pac", before="niṣṭhā")
        self.assertEqual(got.does, "iṭ")
        self.assertEqual(got.sutra, "")
        self.assertIn("7.2.35", got.why)

    def test_the_rule_itself_stands_after_the_whole_run(self):
        self.assertEqual(THE_RULE_ITSELF, "7.2.35")
        self.assertEqual(ANIT_RUN, ("7.2.8", "7.2.34"))
        self.assertGreater(int(THE_RULE_ITSELF.rsplit(".", 1)[1]),
                           int(ANIT_RUN[1].rsplit(".", 1)[1]))


class TheRefusalsThatTurnOnTheAffix(unittest.TestCase):
    """7.2.8–13."""

    def test_a_vas_initial_krt_affix_refuses_it(self):
        # ईश्वरः, दीप्रः, भस्म, याच्ञा.
        got = no_it(before="vaś-kṛt")
        self.assertEqual(got.sutra, "7.2.8")
        self.assertEqual(got.does, "")

    def test_ten_more_affixes_refuse_it(self):
        # तन्तिः, सक्तुः, पत्त्रम्, हस्तः, धूर्तः.
        self.assertEqual(len(TITUTRA), 10)
        for affix in TITUTRA:
            self.assertEqual(no_it(before=affix).sutra, "7.2.9",
                             affix)

    def test_the_ta_meant_is_the_unadis_and_not_the_nisthas(self):
        # औणादिकस्यैव तशब्दस्य ग्रहणमिष्यते, न पुनः क्तस्य —
        # हसितम् keeps its इट् in the निष्ठा.
        self.assertIn("न पुनः क्तस्य",
                      provisions_for("7.2.9")[0].why)

    def test_eight_roots_refuse_it_in_the_perfect(self):
        # चकृव, ससृव, तुष्टुव, शुश्रुव.
        self.assertEqual(len(KRADI_EIGHT), 8)
        for root in KRADI_EIGHT:
            self.assertEqual(no_it(root, before="liṭ").sutra,
                             "7.2.13", root)

    def test_and_that_is_a_restriction_and_not_a_fresh_refusal(self):
        # सिद्धे सत्यारम्भो नियमार्थः — these eight and no others,
        # which is what gives बिभिदिव its इट्.
        self.assertIn("नियमार्थः", provisions_for("7.2.13")[0].why)
        self.assertEqual(no_it("bhid", before="liṭ").does, "iṭ")


class TheRefusalThatTurnsOnTheRoot(unittest.TestCase):
    """7.2.10, the widest of the twenty-seven."""

    def test_a_one_syllable_anudatta_root_refuses_it(self):
        # दाता, नेता, स्तोता, कर्ता, हर्ता.
        got = no_it(gana="ekāc-anudātta")
        self.assertEqual(got.sutra, "7.2.10")
        self.assertEqual(got.does, "")

    def test_the_vrtti_answers_which_roots_with_two_verses(self):
        # के पुनरुपदेशेऽनुदात्ताः? ये तथा गणे पठ्यन्ते — and then
        # the अनिट्कारिका verses set them out.
        why = provisions_for("7.2.10")[0].why
        self.assertIn("के पुनर्", why)
        self.assertIn("अनिट् स्वरान्तो भवति", why)

    def test_it_turns_on_the_root_and_says_so(self):
        # प्रकृत्याश्रयोऽयं प्रतिषेधः — as against 7.2.8 and
        # 7.2.9, which turn on the affix.
        self.assertIn("प्रकृत्याश्रयोऽयं",
                      provisions_for("7.2.10")[0].why)
        self.assertEqual(provisions_for("7.2.10")[0].before, ())


class TheNisthaHeading(unittest.TestCase):
    """From 7.2.14 the word निष्ठा governs, and the vṛtti says how far."""

    def test_the_heading_opens_and_closes_where_the_vrtti_says(self):
        # निष्ठायामित्यधिकार आर्धधातुकस्येड् वलादेः इति यावत्.
        self.assertEqual(NISTHA_FROM, "7.2.14")
        self.assertEqual(NISTHA_TO, "7.2.34")
        self.assertEqual(NISTHA_TO, ANIT_RUN[1])

    def test_every_rule_inside_it_wants_the_nistha(self):
        def number(code):
            return int(code.rsplit(".", 1)[1])

        for row in ANIT_TABLE:
            if not (number(NISTHA_FROM) <= number(row.sutra)
                    <= number(NISTHA_TO)):
                continue
            # 7.2.32 and 7.2.34 lay down whole words and name no
            # environment; every other rule of the stretch does.
            if row.sutra in ("7.2.32", "7.2.34"):
                continue
            self.assertEqual(row.before, ("niṣṭhā",), row.sutra)

    def test_an_option_elsewhere_becomes_a_refusal_here(self):
        # विधूतः, गूढः, वृद्धः — 7.2.15 turns every optional इट्
        # into a refused one, in the निष्ठा alone.
        got = no_it(gana="vibhāṣā-iṭ", before="niṣṭhā")
        self.assertEqual(got.sutra, "7.2.15")
        self.assertEqual(got.does, "")

    def test_and_the_split_from_the_next_sutra_teaches_a_principle(self):
        # यदुपाधेर्विभाषा तदुपाधेः प्रतिषेध इति — where an option
        # is given under a condition, the refusal that follows
        # holds under that condition only. Which is how विदितः
        # keeps its इट्.
        self.assertIn("यद् उपाधेर् विभाषा",
                      provisions_for("7.2.16")[0].why)

    def test_the_adit_refusal_is_optional_in_two_senses(self):
        # मिन्नमनेन, मेदितमनेन.
        plain = no_it(gana="ādit", before="niṣṭhā")
        both = no_it(gana="ādit", before="niṣṭhā",
                     sense="bhāva-ādikarman")
        self.assertEqual(plain.sutra, "7.2.16")
        self.assertFalse(plain.optional)
        self.assertEqual(both.sutra, "7.2.17")
        self.assertTrue(both.optional)
        self.assertIn("7.2.16", both.blocked_by)


class TheLexicalBlock(unittest.TestCase):
    """7.2.18–30, where the grammar turns into a word list."""

    def test_eight_forms_are_matched_with_eight_senses(self):
        # क्षुब्धो मन्थः but क्षुभितं मन्थेन.
        self.assertEqual(len(NIPATANA_EIGHT), 8)
        for form, _sense in NIPATANA_EIGHT:
            got = no_it(form, before="niṣṭhā")
            self.assertEqual(got.sutra, "7.2.18", form)
            self.assertTrue(got.nipatana, form)

    def test_and_the_pairing_is_one_to_one(self):
        # Each form answers with its OWN sense and no other.
        for form, sense in NIPATANA_EIGHT:
            self.assertEqual(no_it(form, before="niṣṭhā").does,
                             sense, form)

    def test_the_senses_are_all_distinct(self):
        senses = [sense for _, sense in NIPATANA_EIGHT]
        self.assertEqual(len(set(senses)), len(senses))

    def test_a_sense_is_what_licenses_each_of_the_rest(self):
        # कष्टं व्याकरणम् but कषितं सुवर्णम्; घुष्टा रज्जुः but
        # अवघुषितं वाक्यम्; धृष्टः but धर्षितः.
        wanted = {
            ("kaṣ", "kṛcchra-gahana"): "7.2.22",
            ("ghuṣ", "a-viśabdana"): "7.2.23",
            ("dhṛṣ", "vaiyātya"): "7.2.19",
            ("vṛt", "adhyayana"): "7.2.26",
        }
        for (root, sense), code in wanted.items():
            self.assertEqual(
                no_it(root, before="niṣṭhā", sense=sense).sutra,
                code, root)
            self.assertEqual(
                no_it(root, before="niṣṭhā").does, "iṭ", root)

    def test_two_words_are_laid_down_the_same_way(self):
        # दृढः and परिवृढः — पूर्वेण तुल्यमेतत्, and the ह्-loss
        # is laid down in both to escape 8.2.1's असिद्धत्व.
        for root, sense in (("dṛḍha", "sthūla-bala"),
                            ("parivṛḍha", "prabhu")):
            got = no_it(root, before="niṣṭhā", sense=sense)
            self.assertTrue(got.nipatana, root)
        self.assertIn("पूर्वेण तुल्यम्",
                      provisions_for("7.2.21")[0].why)

    def test_a_preverb_is_what_licenses_two_more(self):
        # समर्णः, न्यर्णः, व्यर्णः by 7.2.24; अभ्यर्णा सेना by
        # 7.2.25, and only where nearness is meant.
        for preverb in ("sam", "ni", "vi"):
            self.assertEqual(
                no_it("ard", upasarga=preverb,
                      before="niṣṭhā").sutra, "7.2.24", preverb)
        self.assertEqual(
            no_it("ard", upasarga="abhi", before="niṣṭhā",
                  sense="āvidūrya").sutra, "7.2.25")
        self.assertEqual(no_it("ard", before="niṣṭhā").does, "iṭ")

    def test_two_lists_are_optional_rather_than_refused(self):
        # दान्तः beside दमितः; रुष्टः beside रुषितः.
        self.assertEqual(len(DANTA_SEVEN), 7)
        self.assertEqual(len(RUSYAMADI), 5)
        for root in DANTA_SEVEN:
            got = no_it(root, gana="ṇyanta", before="niṣṭhā")
            self.assertEqual(got.sutra, "7.2.27", root)
            self.assertTrue(got.optional, root)
        for root in RUSYAMADI:
            got = no_it(root, before="niṣṭhā")
            self.assertEqual(got.sutra, "7.2.28", root)
            self.assertTrue(got.optional, root)

    def test_a_later_option_wins_over_an_earlier_refusal(self):
        # संघुष् would have been refused outright by 7.2.23 even
        # where declaring is meant; परत्वाद् अयम् एव विकल्पः.
        got = no_it("saṃghuṣ", before="niṣṭhā")
        self.assertEqual(got.sutra, "7.2.28")
        self.assertTrue(got.optional)


class TheVedicEnd(unittest.TestCase):
    """7.2.31–34, and two rules that GIVE the augment."""

    def test_hvr_becomes_hru_in_the_veda(self):
        # ह्रुतस्य चाह्रुतस्य च.
        got = no_it("hvṛ", before="niṣṭhā", chandasi=True)
        self.assertEqual(got.sutra, "7.2.31")

    def test_and_one_word_is_laid_down_to_undo_that(self):
        # अपरिह्वृताः सनुयाम वाजम् — a निपातन whose whole content
        # is that the sūtra before does not apply.
        got = no_it("aparihvṛta", chandasi=True)
        self.assertEqual(got.sutra, "7.2.32")
        self.assertIn("7.2.31", got.blocked_by)

    def test_two_rules_of_the_run_supply_the_it_instead(self):
        # 7.2.33's ह्वरितः of Soma, and 7.2.34's nineteen Vedic
        # forms — the only places in twenty-seven sūtras where
        # the augment is given rather than refused.
        supplying = sorted({row.sutra for row in ANIT_TABLE
                            if row.supplies})
        self.assertEqual(supplying, ["7.2.33", "7.2.34"])
        for code, query in (("7.2.33", {"root": "hvṛ",
                                        "before": "niṣṭhā",
                                        "sense": "soma"}),
                            ("7.2.34", {"root": "grasita"})):
            got = no_it(chandasi=True, **query)
            self.assertEqual(got.sutra, code)
            self.assertEqual(got.does, "iṭ", code)

    def test_the_vedic_list_has_nineteen_forms(self):
        self.assertEqual(len(CHANDASI_ISLANDS), 19)
        self.assertIn("uttabhita", CHANDASI_ISLANDS)

    def test_uttabhita_is_named_with_its_preverb_on_purpose(self):
        # निपातनसामर्थ्यादन्योपसर्गपूर्वः स्तभितशब्दो न भवति —
        # available with उत् and with nothing else.
        self.assertIn("न भवति", provisions_for("7.2.34")[0].why)

    def test_none_of_the_vedic_rules_reaches_outside_the_veda(self):
        for row in ANIT_TABLE:
            if not row.chandasi:
                continue
            query = {}
            if row.of:
                query["root"] = row.of[0]
            if row.before:
                query["before"] = row.before[0]
            if row.sense:
                query["sense"] = row.sense
            self.assertNotEqual(no_it(**query).sutra, row.sutra,
                                row.sutra)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        codes = [row.sutra for row in ANIT_TABLE]
        self.assertEqual(
            codes, ["7.2.%d" % n for n in range(8, 35)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in ANIT_TABLE:
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

    def test_the_rule_the_whole_run_is_stated_before_is_live(self):
        # Written as a debt: 7.2.35 आर्धधातुकस्येड् वलादेः gives
        # the augment all twenty-seven of these refuse, and was
        # not yet codified. It has landed, so the run's default
        # answer can now be checked against the rule itself
        # rather than against this module's own note.
        from src.astadhyayi.it_agama import the_it

        self.assertTrue(REGISTRY.has(THE_RULE_ITSELF))
        self.assertEqual(
            the_it(before="val-ādi-ārdhadhātuka").sutra,
            THE_RULE_ITSELF)
        self.assertEqual(no_it("pac", before="niṣṭhā").does, "iṭ")

    def test_and_the_niṣṭhā_that_governs_half_of_it_is_live(self):
        # 1.1.26 क्तक्तवतू निष्ठा names the affix, and 3.2.102's
        # निष्ठा supplies it. Both are codified, so the run's
        # environment can be asked of the engine.
        self.assertTrue(REGISTRY.has("1.1.26"))
        self.assertTrue(REGISTRY.has("3.2.102"))


if __name__ == "__main__":
    unittest.main()
