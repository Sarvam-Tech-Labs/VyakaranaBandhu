# -*- coding: utf-8 -*-
"""
५.४ — the स्वार्थिक affixes end, and the compound-final ones begin.

The pāda's first sixty-seven rules carry on what 5.3 began: affixes
that add nothing to what the base already means. From 5.4.68
समासान्ताः the subject changes to the endings a compound takes
BECAUSE it is a compound, and ninety-three rules stand under that one
word.

And one rule of the opening is famous for what it PROVES rather than
what it does.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.samasanta import (ALWAYS_APPLY, SAMASANTA_TABLE,
                                      affix_for, provisions_for)
from src.astadhyayi.sutra import REGISTRY
from tests import unwrapped


class AProhibitionThatProvesWhatItForbids(unittest.TestCase):
    """
    5.4.5 न सामिवचने — and the vṛtti finds a missing rule inside it.
    """

    def test_the_prohibition_is_first_shown_to_be_idle(self):
        """
        **सामिवचने प्रतिषेधानर्थक्यम्, प्रकृत्याभिहितत्वात्** —
        the base already says *half*, and 5.4.4's affix is for
        something not wholly done, so there was nothing to forbid.
        """
        notes = unwrapped(REGISTRY.get("5.4.5").notes)
        self.assertIn("सामिवचने प्रतिषेधानर्थक्यम्", notes)
        self.assertIn("प्रकृत्याभिहितत्वात्", notes)

    def test_and_then_read_as_evidence_of_an_affix_no_rule_gives(self):
        """
        **एवं तर्हि नैवायम् अनत्यन्तगतौ विहितस्य कनः प्रतिषेधः;
        किं तर्हि? स्वार्थिकस्य। केन पुनः स्वार्थिकः कन् विहितः?
        एतदेव ज्ञापकम् — भवति स्वार्थे कन्निति.**

        Nowhere in the grammar is a कन् given in the base's own
        sense. That this rule forbids one is the only evidence that
        it exists — and with it the Mahābhāṣya's own अभिन्नतरकम्
        and बहुतरकम् are accounted for.
        """
        notes = unwrapped(REGISTRY.get("5.4.5").notes)
        self.assertIn("एतदेव ज्ञापकम् — भवति स्वार्थे कन्निति",
                      notes)
        self.assertIn("अभिन्नतरकं भवति", notes)
        self.assertIn("बहुतरकं व्याप्यते", notes)

    def test_and_the_refusal_names_the_rule_that_supplies(self):
        """
        A प्रतिषेध does not govern what it excepts. The answer is
        5.4.4's, with 5.4.5 recorded beside it.
        """
        answer = affix_for(samjna="ktānta", result="anatyantagati",
                           upapada="sāmivacana")
        self.assertEqual(answer.affix, "")
        self.assertEqual(answer.sutra, "5.4.4")
        self.assertEqual(answer.blocked_by, "5.4.5")

    def test_and_the_rule_it_excepts_answers_without_the_upapada(self):
        plain = affix_for(samjna="ktānta", result="anatyantagati")
        self.assertEqual(plain.affix, "kan")
        self.assertEqual(plain.sutra, "5.4.4")
        self.assertEqual(plain.blocked_by, "")


class AnIdleWordReadAsAGeneralPrinciple(unittest.TestCase):
    """
    5.4.14 states *in the feminine* where the affix it builds on is
    given only there.
    """

    def test_the_word_is_shown_to_be_needless_and_then_used(self):
        """
        **स्त्रीग्रहणं किमर्थं यावता णच् स्त्रियामेव विहितः? एवं
        तर्ह्येतज् ज्ञापयति — स्वार्थिकाः प्रत्ययाः प्रकृतितो
        लिङ्गवचनान्यतिवर्तन्तेऽपि इति.**
        """
        notes = unwrapped(REGISTRY.get("5.4.14").notes)
        self.assertIn("स्त्रीग्रहणं किमर्थं", notes)
        self.assertIn("लिङ्गवचनान्यतिवर्तन्तेऽपि", notes)

    def test_and_the_principle_is_used_three_times_in_the_pada(self):
        """
        5.4.22 quotes it of a plural base with a singular derived
        word; 5.4.27's देवता is feminine where देव was masculine;
        and 5.4.31 has a vārttika letting the gender be overridden
        outright.
        """
        self.assertIn("अतिवर्तन्तेऽपि स्वार्थिकाः प्रकृतितो "
                      "लिङ्गवचनानि",
                      unwrapped(REGISTRY.get("5.4.22").notes))
        self.assertEqual(provisions_for("5.4.27")[0].gives, "tal")
        self.assertIn("लिङ्गबाधनं",
                      unwrapped(REGISTRY.get("5.4.31").notes))

    def test_and_gender_from_usage_is_the_other_side_of_it(self):
        """
        Where no affix overrides, the gender still comes from usage
        and not from the derivation: **लोकाश्रयत्वाल् लिङ्गस्य** at
        5.4.100, and at 5.3.88 and 5.3.66 before it.
        """
        for sutra in ("5.4.100", "5.3.88", "5.3.66"):
            with self.subTest(sutra=sutra):
                self.assertIn("लोकाश्रयत्वाल्",
                              unwrapped(REGISTRY.get(sutra).notes))


class WhichAffixesAreObligatory(unittest.TestCase):
    """
    5.4.7's vṛtti lists every स्वार्थिक affix that is not under the
    great option, and names each stretch by its limits.
    """

    def test_the_list_is_held_where_it_can_be_checked(self):
        """
        **अन्येऽपि स्वार्थिका नित्याः प्रत्ययाः स्मर्यन्ते —
        तमबादयः प्राक् कनः, ञ्यादयः प्राग् वुनः, आमादयः प्राङ्
        मयटः, बृहतीजात्यन्ताः समासान्ताश्चेति.**
        """
        notes = unwrapped(REGISTRY.get("5.4.7").notes)
        self.assertIn("तमबादयः प्राक् कनः", notes)
        self.assertIn("समासान्ताश्चेति", notes)
        self.assertGreaterEqual(len(ALWAYS_APPLY), 5)

    def test_and_each_stretch_named_is_a_real_one(self):
        """
        Every limit the list gives is a sūtra of the project, and
        the affixes it names are the affixes those rules give.
        """
        from src.astadhyayi.svarthika import (
            provisions_for as earlier)

        self.assertEqual(earlier("5.3.55")[0].gives, "tamap")
        self.assertEqual(earlier("5.3.112")[0].gives, "ñya")
        self.assertEqual(provisions_for("5.4.1")[0].gives, "vun")
        self.assertEqual(provisions_for("5.4.11")[0].gives, "āmu")
        self.assertEqual(provisions_for("5.4.21")[0].gives, "mayaṭ")
        self.assertEqual(provisions_for("5.4.6")[0].gives, "kan")
        self.assertTrue(provisions_for("5.4.68")[0].heading)

    def test_and_the_reading_that_settles_one_of_them(self):
        """
        **नित्यश्चायं प्रत्ययः, उत्तरत्र विभाषाग्रहणात्** — 5.4.7
        is obligatory because 5.4.8 says *optionally*, and 5.4.40
        is settled the same way by 5.4.41.
        """
        for fixed in ("5.4.7", "5.4.40"):
            with self.subTest(sutra=fixed):
                self.assertIn("नित्यश्चायं प्रत्ययः",
                              unwrapped(REGISTRY.get(fixed).notes))
                self.assertFalse(provisions_for(fixed)[0].optional)
        self.assertTrue(provisions_for("5.4.8")[0].optional)
        self.assertTrue(provisions_for("5.4.41")[0].optional
                        or provisions_for("5.4.41")[0].usage)

    def test_and_a_rule_between_two_options_is_itself_fixed(self):
        """
        **द्वयोर्विभाषयोर्मध्ये नित्या विधय इति** at 5.4.10 — a
        third way of settling the question, and 5.4.9 stands
        between 5.4.8 and 5.4.10.
        """
        self.assertIn("द्वयोर्विभाषयोर्मध्ये नित्या विधय इति",
                      unwrapped(REGISTRY.get("5.4.10").notes))
        self.assertTrue(provisions_for("5.4.8")[0].optional)
        self.assertFalse(provisions_for("5.4.9")[0].optional)
        self.assertTrue(provisions_for("5.4.10")[0].optional)


class TheAffixOfBecoming(unittest.TestCase):
    """
    5.4.50 च्वि, and the three rules after it that widen and
    narrow what it covers.
    """

    def test_the_sense_is_defined_and_each_condition_tested(self):
        """
        **कारणस्य विकाररूपेणाभूतस्य तदात्मना भावोऽभूततद्भावः** —
        a thing coming to be what it was not.
        """
        notes = unwrapped(REGISTRY.get("5.4.50").notes)
        self.assertIn("तदात्मना भावोऽभूततद्भावः", notes)
        for question in ("अभूततद्भाव इति किम्",
                         "कृभ्वस्तियोग इति किम्",
                         "संपद्यकर्तरीति किम्"):
            with self.subTest(question=question):
                self.assertIn(question, notes)

    def test_and_the_third_condition_is_shown_to_do_work(self):
        """
        The vṛtti asks why *of the becoming's agent* is needed when
        the sense gives it, and answers with a case where the
        becoming belongs to a LOCUS: **कारकान्तरसंपत्तौ मा भूत् —
        अदेवगृहे देवगृहे संपद्यते.**
        """
        self.assertIn("कारकान्तरसंपत्तौ मा भूत्",
                      unwrapped(REGISTRY.get("5.4.50").notes))

    def test_and_extent_is_told_apart_from_completeness(self):
        """
        **अथाभिविधेः कार्त्स्न्यस्य च को विशेषः?
        यत्रैकदेशेनापि सर्वा प्रकृतिर्विकारमापद्यते सोऽभिविधिः …
        कार्त्स्न्यं तु सर्वात्मना द्रव्यस्य विकाररूपापत्तौ
        भवति** — every weapon in the army taking fire, against one
        thing changing wholly.
        """
        notes = unwrapped(REGISTRY.get("5.4.53").notes)
        self.assertIn("अथाभिविधेः कार्त्स्न्यस्य च को विशेषः",
                      notes)
        self.assertIn("सर्वं शस्त्रम् अग्निसात्संपद्यते", notes)
        self.assertEqual(provisions_for("5.4.52")[0].result,
                         "kārtsnya")
        self.assertEqual(provisions_for("5.4.53")[0].result,
                         "abhividhi")


class TheEchoOfASound(unittest.TestCase):
    """
    5.4.57 — and the doubling it calls for happens before it.
    """

    def test_the_base_is_defined_in_two_parts(self):
        """
        **यत्र ध्वनावकारादयो वर्णा विशेषरूपेण न व्यज्यन्ते
        सोऽव्यक्तः** — a noise in which no letters can be told
        apart; and the LATTER HALF of the echo must have two vowels.
        """
        notes = unwrapped(REGISTRY.get("5.4.57").notes)
        self.assertIn("विशेषरूपेण न व्यज्यन्ते सोऽव्यक्तः", notes)
        self.assertIn("सुष्ठु न्यूनम् अर्धं द्व्यच्कं संपद्यते",
                      notes)

    def test_and_the_doubling_precedes_the_affix_that_asks_for_it(self):
        """
        **डाचि विवक्षिते द्विर्वचनमेव पूर्वं क्रियते, पश्चात्
        प्रत्ययः** — the affix is only WISHED FOR when the doubling
        is made, and comes after it.
        """
        self.assertIn("डाचि विवक्षिते द्विर्वचनमेव पूर्वं क्रियते",
                      unwrapped(REGISTRY.get("5.4.57").notes))

    def test_and_each_of_the_four_conditions_is_tested(self):
        notes = unwrapped(REGISTRY.get("5.4.57").notes)
        for question in ("अव्यक्तानुकरणादिति किम्",
                         "द्व्यजवरार्धादिति किम्",
                         "अवरग्रहणं किम्",
                         "अनिताविति किम्"):
            with self.subTest(question=question):
                self.assertIn(question, notes)


class WhatALossCountsAs(unittest.TestCase):
    """
    5.4.138 removes a word and the vṛtti says that the removal IS
    the compound-final.
    """

    def test_the_statement(self):
        """
        **स्थानिद्वारेण लोपस्य समासान्तता विज्ञायते** — a loss
        counts as a compound-final through what it stands in place
        of.
        """
        self.assertIn("स्थानिद्वारेण लोपस्य समासान्तता विज्ञायते",
                      unwrapped(REGISTRY.get("5.4.138").notes))

    def test_and_the_rows_record_such_rules_as_substitutions(self):
        """
        Five rules of the closing stretch remove a word rather than
        adding one, and each gives no affix at all.
        """
        removing = {row.sutra for row in SAMASANTA_TABLE
                    if "lopa" in row.adesa}
        for sutra in ("5.4.138", "5.4.139", "5.4.140", "5.4.146",
                      "5.4.148"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, removing)
        for row in SAMASANTA_TABLE:
            if "lopa" in row.adesa and row.gives:
                with self.subTest(sutra=row.sutra):
                    # 5.4.1, 5.4.2 and 5.4.51 give an affix AND
                    # remove the base's ending; the rest only
                    # remove.
                    self.assertIn(row.sutra,
                                  {"5.4.1", "5.4.2", "5.4.51"})

    def test_and_listing_forms_whole_confines_where_they_apply(self):
        """
        5.4.139: **समुदायपाठस्य च प्रयोजनं विषयनियमः —
        स्त्रियामेव, तत्र ङीप्प्रत्यय एव, नान्यदा** — the forms are
        listed with the loss ALREADY MADE, and that is what confines
        it to the feminine and to one feminine affix.
        """
        notes = unwrapped(REGISTRY.get("5.4.139").notes)
        self.assertIn("समुदायपाठस्य च प्रयोजनं विषयनियमः", notes)
        self.assertEqual(provisions_for("5.4.139")[0].result, "strī")


class TheRemainderAndItsRefusals(unittest.TestCase):
    """
    5.4.154 gives कप् to whatever the rules before have not
    reached, and six rules then take it back.
    """

    def test_the_remainder_is_defined(self):
        """
        **यस्माद् बहुव्रीहेः समासान्तो न विहितः स शेषः** — and the
        vṛtti uses that to explain two forms an earlier rule seemed
        to cover: **विशेषे स इष्यते**.
        """
        notes = unwrapped(REGISTRY.get("5.4.154").notes)
        self.assertIn("समासान्तो न विहितः स शेषः", notes)
        self.assertIn("विशेषे स इष्यते", notes)
        self.assertEqual(provisions_for("5.4.154")[0].result,
                         "śeṣa")

    def test_and_the_six_refusals_after_it(self):
        refusing = {row.sutra for row in SAMASANTA_TABLE
                    if row.refuses
                    and int(row.sutra.rsplit(".", 1)[1]) > 154}
        self.assertEqual(refusing,
                         {"5.4.155", "5.4.156", "5.4.157",
                          "5.4.158", "5.4.159", "5.4.160"})
        for sutra in refusing:
            with self.subTest(sutra=sutra):
                self.assertEqual(provisions_for(sutra)[0].gives, "")

    def test_and_one_of_them_refuses_more_than_the_remainder(self):
        """
        **ईयसश्च — सर्वा प्राप्तिः प्रतिषिध्यते**: 5.4.156 refuses
        5.4.154 AND 5.4.153, where the others refuse only what
        reached them.
        """
        self.assertIn("सर्वा प्राप्तिः प्रतिषिध्यते",
                      unwrapped(REGISTRY.get("5.4.156").notes))

    def test_and_a_refusal_answers_by_naming_what_it_blocked(self):
        answer = affix_for(samjna="bahuvrīhi", result="saṃjñā")
        self.assertEqual(answer.affix, "")
        self.assertEqual(answer.blocked_by, "5.4.155")


class TheRulesAreOnRecord(unittest.TestCase):
    """All 160 of the pāda, contiguous, each with a note."""

    def test_all_of_them_are_codified(self):
        have = {sutra.id.number for sutra in REGISTRY.all()
                if sutra.id.adhyaya == 5 and sutra.id.pada == 4}
        self.assertEqual(have, set(range(1, 161)))

    def test_and_the_whole_chapter_is_contiguous(self):
        """
        अध्याय ५ — 136 + 140 + 119 + 160 = 555 sūtras, and every one
        of them codified.
        """
        sizes = {1: 136, 2: 140, 3: 119, 4: 160}
        for pada, size in sizes.items():
            with self.subTest(pada=pada):
                have = {sutra.id.number for sutra in REGISTRY.all()
                        if sutra.id.adhyaya == 5
                        and sutra.id.pada == pada}
                self.assertEqual(have, set(range(1, size + 1)))
        self.assertEqual(sum(sizes.values()), 555)

    def test_and_every_row_names_a_sutra_the_corpus_has(self):
        from src.astadhyayi.corpus import collate

        witnesses = collate()
        for row in SAMASANTA_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertIn(row.sutra, witnesses)

    def test_and_every_exception_points_at_a_rule_of_the_table(self):
        stated = {row.sutra for row in SAMASANTA_TABLE}
        for row in SAMASANTA_TABLE:
            for target in row.excepts:
                with self.subTest(sutra=row.sutra, target=target):
                    if target.startswith("5.4."):
                        self.assertIn(target, stated)
                    else:
                        self.assertTrue(REGISTRY.has(target))
                    self.assertNotEqual(target, row.sutra)

    def test_and_every_row_supplies_or_refuses_something(self):
        """
        Five shapes and no sixth: the heading, the rules that give
        an affix, those that only substitute or remove, the
        refusals, and the forms laid down whole — 5.4.125 and
        5.4.126 lay a compound down with its ending ALREADY made,
        so they name neither an affix nor a substitute.
        """
        laid_only = set()
        for row in SAMASANTA_TABLE:
            with self.subTest(sutra=row.sutra):
                if not (row.heading or row.gives or row.adesa
                        or row.refuses):
                    self.assertTrue(row.nipatana)
                    laid_only.add(row.sutra)
        self.assertEqual(laid_only, {"5.4.125", "5.4.126"})

    def test_and_the_colophon_closes_the_chapter(self):
        self.assertIn("पञ्चमाध्यायस्य चतुर्थः पादः",
                      unwrapped(REGISTRY.get("5.4.160").notes))
        last = max(int(row.sutra.rsplit(".", 1)[1])
                   for row in SAMASANTA_TABLE)
        self.assertEqual(last, 160)


if __name__ == "__main__":
    unittest.main()
