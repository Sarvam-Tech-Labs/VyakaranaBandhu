# -*- coding: utf-8 -*-
"""
४.१.७६ and ४.१.८२–९१ — what has to be in place before a taddhita can
be given.

Three headings and four rules on elision, and none of them gives an
affix in a sense. They are the scaffolding: 4.1.76 names what the
affixes are called, 4.1.82 says which word one attaches to, 4.1.83
says which affix comes when nothing else is said, and 4.1.88–91 say
what happens when one comes and does not show.

Only after all of that does 4.1.92 तस्यापत्यम् begin to say in what
senses — which is why the rules from there on can name a sense and no
affix at all.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.sutra import REGISTRY
from tests import unwrapped


class TwoHeadingsOverOneRange(unittest.TestCase):
    """
    4.1.1 says what the affixes attach TO and 4.1.76 says what they
    are CALLED, and both run to the end of अध्याय ५. The pair is the
    whole frame of two chapters.
    """

    def test_they_run_to_the_same_sutra(self):
        from src.astadhyayi.sup import nominal_base
        from src.astadhyayi.taddhita import taddhita_heading

        self.assertEqual(nominal_base().through,
                         taddhita_heading().through)

    def test_and_that_sutra_is_the_last_of_adhyaya_5(self):
        from src.astadhyayi.corpus import collate
        from src.astadhyayi.taddhita import taddhita_heading

        last = max(int(key.rsplit(".", 1)[1]) for key in collate()
                   if key.startswith("5.4."))
        self.assertEqual(taddhita_heading().through, "5.4.%d" % last)

    def test_the_name_it_confers(self):
        from src.astadhyayi.taddhita import taddhita_heading

        self.assertEqual(taddhita_heading().names, "taddhita")
        self.assertEqual(taddhita_heading().by, "4.1.76")

    def test_the_plural_is_read_as_a_scope(self):
        """
        बहुवचनमनुक्ततद्धितपरिग्रहार्थम् — the name is given in the
        plural so that affixes never stated in these two chapters
        fall under it. A grammatical number doing the work of a
        clause.
        """
        from src.astadhyayi.taddhita import taddhita_heading

        why = unwrapped(taddhita_heading().why)
        self.assertIn("बहुवचनमनुक्ततद्धितपरिग्रहार्थम्", why)

    def test_and_the_two_headings_feed_each_other(self):
        """
        1.2.46 makes a taddhita-formed word a प्रातिपदिक, which is
        what lets 4.1.1 govern the NEXT affix after it. The naming
        rule and the base rule are not merely parallel; each is what
        keeps the other going.
        """
        notes = unwrapped(REGISTRY.get("4.1.76").notes)
        self.assertIn("1.2.46", notes)
        self.assertIn("तद्धितप्रदेशाः", notes)


class OneSutraDoingTheWorkOfThreeHeadings(unittest.TestCase):
    """
    4.1.82 समर्थानां प्रथमाद्वा. त्रयमप्यधिक्रियते समर्थानामिति च,
    प्रथमादिति च, वेति च — and each of the three is shown by what
    would go wrong without it.
    """

    def test_it_contributes_three_words(self):
        from src.astadhyayi.taddhita import SAMARTHA_WORDS, samartha

        self.assertEqual(len(SAMARTHA_WORDS), 3)
        self.assertEqual(samartha().words, SAMARTHA_WORDS)

    def test_each_word_has_its_own_counter_example(self):
        notes = unwrapped(REGISTRY.get("4.1.82").notes)
        for question in ("समर्थानामिति किम्", "प्रथमादिति किम्",
                         "वेति किम्"):
            with self.subTest(question=question):
                self.assertIn(question, notes)

    def test_unconnected_words_are_refused(self):
        from src.astadhyayi.taddhita import samartha

        answer = samartha(connected=False)
        self.assertIn("कम्बल उपगोः", answer.why)
        self.assertEqual(answer.by, "4.1.82")

    def test_and_so_is_a_word_that_is_not_the_first(self):
        from src.astadhyayi.taddhita import samartha

        answer = samartha(position=2)
        self.assertIn("प्रथमान्ताद् मा भूत्", answer.why)

    def test_the_heading_stops_where_its_words_stop_meaning_anything(self):
        """
        स्वार्थिकेषु ह्यस्योपयोगो नास्ति, विकल्पोऽपि तत्रानवस्थितः.
        Past 5.3.1 the affixes add no sense of their own, so there is
        nothing for *the first of the connected words* to select. A
        heading bounded not by a topic but by the point at which its
        own words become empty.
        """
        from src.astadhyayi.taddhita import samartha

        self.assertEqual(samartha().through, "5.3.1")
        self.assertIn("स्वार्थिकेषु ह्यस्योपयोगो नास्ति",
                      unwrapped(REGISTRY.get("4.1.82").notes))

    def test_and_the_sutra_it_stops_at_exists(self):
        from src.astadhyayi.corpus import collate

        self.assertIn("5.3.1", collate())


class ADefaultThatLetsTheRulesStateOnlyASense(unittest.TestCase):
    """
    4.1.83 प्राग्दीव्यतोऽण्. Every rule from 4.1.92 on names a sense
    and no affix, and this is why.
    """

    def test_the_default_affix_and_its_range(self):
        from src.astadhyayi.taddhita import default_affix

        answer = default_affix()
        self.assertEqual(answer.gives, "aṇ")
        self.assertEqual(answer.by, "4.1.83")

    def test_the_boundary_is_a_word_lifted_out_of_the_rule_it_stops_at(self):
        """
        तदेकदेशो दीव्यच्छब्दोऽवधित्वेन गृह्यते — 4.4.2 तेन दीव्यति is
        the rule, and one word of it is used as the marker. 4.1.87
        does the same with 5.2.1.
        """
        from src.astadhyayi.taddhita import default_affix

        why = unwrapped(default_affix().why)
        self.assertIn("तदेकदेशो दीव्यच्छब्दोऽवधित्वेन गृह्यते", why)
        self.assertIn("प्राग् भवनसंशब्दनात्",
                      unwrapped(REGISTRY.get("4.1.87").notes))

    def test_and_both_boundary_rules_exist_in_the_corpus(self):
        from src.astadhyayi.corpus import collate

        for boundary in ("4.4.2", "5.2.1"):
            with self.subTest(sutra=boundary):
                self.assertIn(boundary, collate())

    def test_three_readings_offered_and_none_chosen(self):
        why = unwrapped(REGISTRY.get("4.1.83").notes)
        self.assertIn("अधिकारः, परिभाषा, विधिर्वेति", why)

    def test_the_rules_it_serves_name_a_sense_and_no_affix(self):
        """
        The payoff. 4.1.92 तस्यापत्यम् is three syllables and names
        no affix; the vṛtti at 4.1.82 calls such rules
        लक्षणवाक्यानि. That only works because 4.1.83 has supplied
        one in advance.
        """
        from src.astadhyayi.corpus import collate

        rule = collate().get("4.1.92")
        self.assertIsNotNone(rule)
        for witness in rule.witnesses.values():
            with self.subTest(witness=witness):
                self.assertNotIn("aṇ", witness.split())


class TheAffixesThatExceptTheDefault(unittest.TestCase):
    """
    4.1.84 to 4.1.87, and each is stated against something.
    """

    def test_each_named_ground_gives_its_own_affix(self):
        from src.astadhyayi.taddhita import prag_divyatah_affix

        for ground, affix, sutra in (
            ("aśvapatyādi", "aṇ", "4.1.84"),
            ("dity-adity-āditya-paty-uttarapada", "ṇya", "4.1.85"),
            ("utsādi", "añ", "4.1.86"),
            ("strī", "nañ", "4.1.87"),
            ("puṃs", "snañ", "4.1.87"),
        ):
            with self.subTest(ground=ground):
                answer = prag_divyatah_affix(ground)
                self.assertEqual(answer.gives, affix)
                self.assertEqual(answer.by, sutra)

    def test_an_unnamed_ground_falls_to_the_default(self):
        """
        And the fall-through IS the reuse. The relation between an
        अपवाद and the उत्सर्ग it excepts is not a citation but a
        reaching-for: asked about a ground none of these four names,
        the code returns 4.1.83's own answer, so the four declare it.
        """
        from src.astadhyayi.taddhita import default_affix, prag_divyatah_affix

        fallen = prag_divyatah_affix("upagu")
        self.assertEqual(fallen.by, "4.1.83")
        self.assertEqual(fallen.why, default_affix().why)

    def test_and_all_four_declare_it(self):
        for sutra in ("4.1.84", "4.1.85", "4.1.86", "4.1.87"):
            with self.subTest(sutra=sutra):
                self.assertIn("4.1.83", REGISTRY.get(sutra).reuses)

    def test_a_rule_stated_against_a_rule_not_yet_given(self):
        """
        4.1.84 gives the default affix to a list, which by itself
        says nothing. पत्युत्तरपदाद् ण्यं वक्ष्यति, तस्यापवादः — the
        NEXT rule would take these words away, so this holds them
        back against a rule that has not been stated. A प्रतिषेध
        aimed forward.
        """
        from src.astadhyayi.taddhita import default_affix, prag_divyatah_affix

        holding = prag_divyatah_affix("aśvapatyādi")
        self.assertEqual(holding.gives, default_affix().gives)
        self.assertEqual(holding.excepts, ("4.1.85",))
        self.assertIn("वक्ष्यति", unwrapped(REGISTRY.get("4.1.84").notes))

    def test_and_one_beats_the_default_and_its_exceptions_together(self):
        from src.astadhyayi.taddhita import prag_divyatah_affix

        answer = prag_divyatah_affix("utsādi")
        self.assertEqual(set(answer.excepts), {"4.1.83", "4.1.85"})
        self.assertIn("अणस्तदपवादानां च बाधकः",
                      unwrapped(REGISTRY.get("4.1.86").notes))

    def test_one_affix_serving_four_senses(self):
        """
        स्त्रीषु भवं, स्त्रीणां समूहः, स्त्रीभ्य आगतं, स्त्रीभ्यो
        हितं — all स्त्रैणम्. The affix does not change with the
        sense, which is exactly what 4.1.83's default made possible.
        """
        notes = unwrapped(REGISTRY.get("4.1.87").notes)
        for sense in ("स्त्रीषु भवं", "स्त्रीणां समूहः",
                      "स्त्रीभ्य आगतं", "स्त्रीभ्यो हितं"):
            with self.subTest(sense=sense):
                self.assertIn(sense, notes)


class DerivedAndThenNotAppearing(unittest.TestCase):
    """
    4.1.88 to 4.1.91. लुक् is what lets a form be built and then
    removed, so that a word may mean what no part of it says.
    """

    def test_the_affix_is_dropped_after_a_numeral_compound(self):
        from src.astadhyayi.taddhita import elision

        answer = elision()
        self.assertTrue(answer.holds)
        self.assertEqual(answer.by, "4.1.88")

    def test_but_not_where_a_patronymic_is_meant(self):
        from src.astadhyayi.taddhita import elision

        answer = elision(apatya=True)
        self.assertFalse(answer.holds)
        self.assertIn("द्वैदेवदत्तिः", answer.why)

    def test_the_word_left_behind_means_what_no_part_of_it_says(self):
        notes = unwrapped(REGISTRY.get("4.1.88").notes)
        self.assertIn("पञ्चसु कपालेषु संस्कृतः पञ्चकपालः", notes)

    def test_and_the_rule_names_the_affix_not_the_compound(self):
        """
        उपचारेण तु लक्षणया द्विगुनिमित्तभूतः प्रत्यय एव द्विगुः,
        तस्य लुग् भवति — the affix CAUSED by a numeral compound is
        itself called one, by transfer, and that is what is elided.
        A look-alike is then kept out by asking what caused what.
        """
        notes = unwrapped(REGISTRY.get("4.1.88").notes)
        self.assertIn("द्विगुनिमित्तभूतः प्रत्यय एव द्विगुः", notes)
        self.assertIn("न तस्य द्विगुत्वं निमित्तम्", notes)

    def test_an_elision_refused_before_a_vowel(self):
        from src.astadhyayi.taddhita import elision

        answer = elision(gotra=True, before_ac=True)
        self.assertFalse(answer.holds)
        self.assertEqual(answer.by, "4.1.89")

    def test_an_affix_elided_before_it_is_formed(self):
        """
        बुद्धिस्थेऽनुत्पन्न एव युवप्रत्ययस्य लुग् भवति,
        तस्मिन्निवृत्ते सति यो यतः प्राप्नोति स ततो भवति — what is
        elided is something merely INTENDED, and once it is gone
        whatever else would have applied applies. A derivation
        blocked by running it and removing the result.
        """
        from src.astadhyayi.taddhita import elision

        answer = elision(yuvan=True, before_ac=True)
        self.assertTrue(answer.holds)
        self.assertEqual(answer.by, "4.1.90")
        self.assertIn("बुद्धिस्थेऽनुत्पन्न एव", answer.why)

    def test_and_optionally_for_two_of_them(self):
        from src.astadhyayi.taddhita import elision

        for affix in ("phak", "phiñ"):
            with self.subTest(affix=affix):
                answer = elision(yuvan=True, before_ac=True, of=affix)
                self.assertEqual(answer.by, "4.1.91")
                self.assertTrue(answer.optional)

    def test_the_obligatory_one_is_not_optional(self):
        from src.astadhyayi.taddhita import elision

        self.assertFalse(elision(yuvan=True, before_ac=True).optional)


class TheScaffoldingIsInPlaceBefore4_1_92(unittest.TestCase):
    """
    The point of the whole run. Four things have to be settled before
    a rule can say तस्यापत्यम् and nothing else, and all four are
    settled in the sixteen sūtras before it.
    """

    def test_all_four_are_codified_and_all_precede_it(self):
        for sutra in ("4.1.76", "4.1.82", "4.1.83", "4.1.88"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))
                self.assertLess(int(sutra.rsplit(".", 1)[1]), 92)

    def test_and_the_pada_runs_unbroken_to_them(self):
        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 1}
        self.assertEqual(have, set(range(1, max(have) + 1)))
        self.assertGreaterEqual(max(have), 91)


if __name__ == "__main__":
    unittest.main()

class AHeadingThatFacesBothWays(unittest.TestCase):
    """
    4.1.92 तस्यापत्यम् is read with the affixes stated BEFORE it as
    well as after — पूर्वैरुत्तरैश्च प्रत्ययैरभिसंबध्यते. Every
    heading the project has met governed forward only.
    """

    FORWARD_ONLY = ("3.2.84", "3.3.18", "3.4.67", "4.1.1", "4.1.3",
                    "4.1.14", "4.1.76", "4.1.82", "4.1.83")

    def test_the_rule_names_no_affix(self):
        """
        Three syllables and no affix in them. The test reads the
        sūtra off the corpus rather than trusting the note.
        """
        from src.astadhyayi.corpus import collate

        rule = collate()["4.1.92"]
        for witness in rule.witnesses.values():
            with self.subTest(witness=witness):
                self.assertLessEqual(len(witness.split()), 2)

    def test_and_the_answer_it_gives_carries_none(self):
        from src.astadhyayi.apatya import apatya_sense

        self.assertEqual(apatya_sense().gives, "")
        self.assertEqual(apatya_sense().by, "4.1.92")

    def test_it_says_it_reaches_backward(self):
        from src.astadhyayi.apatya import apatya_sense

        why = unwrapped(apatya_sense().why)
        self.assertIn("पूर्वैरुत्तरैश्च प्रत्ययैर् अभिसंबध्यते", why)

    def test_and_the_rules_before_it_really_are_patronymics(self):
        """
        The claim is checkable. 4.1.85 and 4.1.86 were stated six and
        seven sūtras before the sense-rule, and their own examples —
        दैत्यः, औत्सः — are among the ones 4.1.92's vṛtti lists.
        """
        from src.astadhyayi.apatya import apatya_sense

        why = unwrapped(apatya_sense().why)
        for form in ("दैत्यः", "औत्सः", "स्त्रैणः", "पौंस्नः"):
            with self.subTest(form=form):
                self.assertIn(form, why)
        for sutra in ("4.1.85", "4.1.86", "4.1.87"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))

    def test_every_earlier_heading_ran_one_way(self):
        """
        Not decoration: if some earlier heading had also reached
        backward, this one would not be worth remarking on. Each of
        those is codified and none of their notes claims it.
        """
        for heading in self.FORWARD_ONLY:
            with self.subTest(heading=heading):
                self.assertTrue(REGISTRY.has(heading))
                self.assertNotIn("पूर्वैरुत्तरैश्च",
                                 unwrapped(REGISTRY.get(heading).notes))


class TwoRulesThatProvideNothing(unittest.TestCase):
    """
    4.1.93 and 4.1.94 give no affix and restrict everything after
    them. One says how many a lineage may take, the other says what
    the young-descendant affix is added to.
    """

    def test_neither_gives_an_affix(self):
        from src.astadhyayi.apatya import only_one

        for answer in (only_one(), only_one(kind="yuvan"),
                       only_one(feminine=True)):
            with self.subTest(by=answer.by):
                self.assertEqual(answer.gives, "")

    def test_one_affix_for_a_lineage_however_far_it_runs(self):
        """
        योऽपि व्यवहितेन जनितः, सोऽपि प्रथमप्रकृतेरपत्यं भवत्येव — a
        descendant born at any remove is still the descendant of the
        FIRST base, which is what stops the affixes accumulating.
        """
        from src.astadhyayi.apatya import only_one

        answer = only_one()
        self.assertEqual(answer.by, "4.1.93")
        self.assertIn("प्रथमप्रकृतेरपत्यं भवत्येव",
                      unwrapped(answer.why))
        self.assertIn("तत्पुत्रोऽपि गार्ग्यः", unwrapped(answer.why))

    def test_the_young_affix_is_added_to_the_lineage_form(self):
        from src.astadhyayi.apatya import only_one

        answer = only_one(kind="yuvan")
        self.assertEqual(answer.by, "4.1.94")
        self.assertIn("न परमप्रकृत्यनन्तरयुवभ्यः",
                      unwrapped(answer.why))

    def test_a_sutra_split_because_neither_whole_reading_works(self):
        """
        तस्माद् योगविभागः कर्तव्यः. Read as a restriction it leaves
        the feminine unrestricted; read as giving an affix it leaves
        the feminine with none at all. Both failures are on record,
        and so is what the split changes: युवसंज्ञैव प्रतिषिध्यते —
        what the second half refuses is the NAME.
        """
        from src.astadhyayi.apatya import only_one

        why = unwrapped(only_one(feminine=True).why)
        self.assertIn("तस्माद् योगविभागः कर्तव्यः", why)
        self.assertIn("स्त्रियामनियमः प्राप्नोति", why)
        self.assertIn("युवसंज्ञैव प्रतिषिध्यते", why)


class AConditionThatIsNothingInTheWord(unittest.TestCase):
    """
    Seven rules of this run turn on WHOSE FAMILY is meant — भार्गव,
    वात्स्य, आग्रायण, ब्राह्मण, कौशिक, आङ्गिरस, त्रैगर्त, काश्यप —
    and nothing in the word says which. No rule earlier in the
    project has a condition of that kind.

    The set is read off the table, which is why it noticed when two
    more arrived at 4.1.117 and 4.1.124.
    """

    def test_exactly_seven_rules_state_one(self):
        from src.astadhyayi.apatya import APATYA

        stated = {row.sutra for row in APATYA if row.among}
        self.assertEqual(
            stated,
            {"4.1.102", "4.1.106", "4.1.107", "4.1.108", "4.1.111",
             "4.1.117", "4.1.124"})

    def test_and_one_word_is_reached_by_three_of_them(self):
        """
        विकर्ण takes अण् among the Vātsyas (4.1.117), ढक् among the
        Kāśyapas (4.1.124), and इञ् elsewhere by 4.1.95. One word,
        three families, three affixes, and nothing in the word to
        tell them apart.
        """
        from src.astadhyayi.apatya import apatya_affix

        self.assertEqual(
            apatya_affix("vikarṇa", among="vātsya").gives, "aṇ")
        self.assertEqual(
            apatya_affix("vikarṇa", among="kāśyapa").gives, "ḍhak")
        self.assertIn("वैकर्णिः",
                      unwrapped(REGISTRY.get("4.1.124").notes))

    def test_the_same_word_takes_different_affixes_by_family(self):
        """
        शारद्वतायनः if a Bhārgava is meant, शारद्वतः otherwise —
        same word, same sense, different family. The resolver has to
        give two different answers to two queries that differ in
        nothing else.
        """
        from src.astadhyayi.apatya import apatya_affix

        inside = apatya_affix("śaradvat", among="bhārgava",
                              kind="gotra")
        outside = apatya_affix("śaradvat", among="vātsya",
                               kind="gotra")
        self.assertEqual(inside.by, "4.1.102")
        self.assertNotEqual(outside.by, "4.1.102")

    def test_and_the_lineage_outranks_everything_else_stated(self):
        from src.astadhyayi.apatya import _how_specific, provisions_for

        by_family = provisions_for("4.1.111")[0]
        by_list = provisions_for("4.1.110")[0]
        self.assertGreater(_how_specific(by_family),
                           _how_specific(by_list))

    def test_each_of_the_five_records_the_form_it_leaves_behind(self):
        """
        A rule stated of one family does not refuse the others; it
        simply does not reach them, and the vṛtti gives the form that
        stands instead. शारद्वतोऽन्यः, माधव एवान्यः, कापेयः,
        वातण्डः, भार्गिरन्यः.
        """
        for sutra, form in (("4.1.102", "शारद्वतोऽन्यः"),
                            ("4.1.106", "माधव एवान्यः"),
                            ("4.1.107", "कापेयः"),
                            ("4.1.108", "वातण्डः"),
                            ("4.1.111", "भार्गिरन्यः")):
            with self.subTest(sutra=sutra):
                self.assertIn(form,
                              unwrapped(REGISTRY.get(sutra).notes))


class AReadingSettledByAProperName(unittest.TestCase):
    """
    4.1.104's अनृष्यानन्तर्ये can be read two ways, and one of them
    makes कौशिको विश्वामित्रः wrong. The vṛtti says the other MUST
    therefore be right.
    """

    def test_both_readings_and_the_name_are_on_record(self):
        notes = unwrapped(REGISTRY.get("4.1.104").notes)
        self.assertIn("अनृषिभ्योऽनन्तरे भवतीति", notes)
        self.assertIn("कौशिको विश्वामित्र इति दुष्यति", notes)
        self.assertIn("अवश्यं चैतदेवं विज्ञेयम्", notes)

    def test_the_rule_answers_for_its_own_list(self):
        from src.astadhyayi.apatya import apatya_affix

        answer = apatya_affix(gana="bidādi", kind="gotra")
        self.assertEqual(answer.by, "4.1.104")
        self.assertEqual(answer.gives, "añ")


class AHeadingOverriddenByCapacity(unittest.TestCase):
    """
    4.1.100 stands under गोत्र, and 4.1.93 allows a lineage only one
    affix — so under the heading as carried it could give nothing.
    सामर्थ्याद् यूनि प्रत्ययो विज्ञायते: it is read as being about
    the YOUNG descendant instead, because it could not otherwise act.
    """

    def test_the_row_is_stated_of_the_young_descendant(self):
        from src.astadhyayi.apatya import provisions_for

        row, = provisions_for("4.1.100")
        self.assertEqual(row.kind, "yuvan")

    def test_though_the_heading_it_stands_under_says_otherwise(self):
        notes = unwrapped(REGISTRY.get("4.1.100").notes)
        self.assertIn("ननु च गोत्र इति वर्तते", notes)
        self.assertIn("सामर्थ्याद् यूनि प्रत्ययो विज्ञायते", notes)

    def test_and_the_rule_it_would_have_broken_is_codified(self):
        """
        The argument only works because 4.1.93 really does allow one
        affix. If that rule were not on record the reasoning would be
        unattached.
        """
        from src.astadhyayi.apatya import only_one

        self.assertTrue(REGISTRY.has("4.1.93"))
        self.assertIn("एक एव प्रत्ययो भवति",
                      unwrapped(only_one().why))

    def test_the_same_argument_is_used_again_ten_sutras_later(self):
        self.assertIn("सामर्थ्याद् यूनि प्रत्ययो विज्ञायते",
                      unwrapped(REGISTRY.get("4.1.110").notes))


class AListThatAddsRatherThanExcepts(unittest.TestCase):
    """
    Every गण in this pāda until 4.1.112 carves an exception out of
    another rule. शिवादि holds a word that is in two OTHER lists as
    well, समावेशार्थम् — so that all three affixes may apply.
    """

    def test_the_note_records_the_three_forms(self):
        notes = unwrapped(REGISTRY.get("4.1.112").notes)
        self.assertIn("समावेशार्थम्", notes)
        for form in ("गाङ्गः", "गाङ्गायनिः", "गाङ्गेयः"):
            with self.subTest(form=form):
                self.assertIn(form, notes)

    def test_and_one_member_is_there_for_the_opposite_reason(self):
        """
        तक्षन् is in the list to BEAT one rule and expressly not
        another: ण्यप्रत्ययस्य तु बाधो नेष्यते, so ताक्ष्णः and
        ताक्षण्यः both stand. One membership beating one rule and
        sparing another.
        """
        notes = unwrapped(REGISTRY.get("4.1.112").notes)
        self.assertIn("ण्यप्रत्ययस्य तु बाधो नेष्यते", notes)
        self.assertIn("ताक्षण्यः", notes)

    def test_a_double_membership_licensing_two_forms(self):
        """
        4.1.108's वतण्ड is in गर्गादि and in शिवादि, and outside the
        family that rule names BOTH affixes stand —
        अनाङ्गिरसे तूभयत्र पाठसामर्थ्यात् प्रत्ययद्वयमपि भवति.
        """
        notes = unwrapped(REGISTRY.get("4.1.108").notes)
        self.assertIn("पाठसामर्थ्यात् प्रत्ययद्वयमपि भवति", notes)


class TheSectionEndsWhereAnEarlierRuleSaidItWould(unittest.TestCase):
    """
    4.1.98's vṛtti names 4.1.112 as where the गोत्र heading stops,
    fourteen sūtras before it gets there — and 4.1.112's own vṛtti
    says गोत्र इति निवृत्तम्.
    """

    def test_the_earlier_rule_names_the_later_one(self):
        self.assertIn("गोत्राधिकारश्च शिवादिभ्योऽण् इति यावत्",
                      unwrapped(REGISTRY.get("4.1.98").notes))

    def test_and_the_later_one_says_the_heading_has_stopped(self):
        self.assertIn("गोत्र इति निवृत्तम्",
                      unwrapped(REGISTRY.get("4.1.112").notes))

    def test_no_row_after_it_states_the_lineage_sense(self):
        """
        The check that makes the pair mean something: if a row past
        4.1.112 still held itself to गोत्र, the heading would not
        have stopped.
        """
        from src.astadhyayi.apatya import APATYA

        after = [row for row in APATYA
                 if int(row.sutra.rsplit(".", 1)[1]) >= 112]
        self.assertTrue(after)
        for row in after:
            with self.subTest(sutra=row.sutra):
                self.assertEqual(row.kind, "")


class AnElisionThatBuysADifferentAffix(unittest.TestCase):
    """
    4.1.109. Once the यञ् is gone, 4.1.73 reaches the bare word and
    gives ङीन् — a rule that removes an affix so that another may
    come.
    """

    def test_the_elision_holds_in_that_lineage_only(self):
        from src.astadhyayi.apatya import NotNamed, feminine_luk

        self.assertEqual(feminine_luk(among="āṅgirasa").by, "4.1.109")
        self.assertIsInstance(feminine_luk(among="traigarta"),
                              NotNamed)

    def test_and_the_affix_that_arrives_is_the_feminine_section_s(self):
        from src.astadhyayi.apatya import feminine_luk
        from src.astadhyayi.stri import stri_affix

        why = unwrapped(feminine_luk().why)
        self.assertIn("शार्ङ्गरवादिपाठाद् ङीन् भवति", why)
        self.assertEqual(stri_affix(gana="śārṅgaravādi").gives, "ṅīn")

    def test_it_is_4_1_90s_move_from_the_other_end(self):
        """
        4.1.90 elides an affix before it is formed so that whatever
        else applies may apply — तस्मिन्निवृत्ते सति यो यतः
        प्राप्नोति स ततो भवति. This elides one already formed, for
        the same purpose, and cites the same clause.
        """
        from src.astadhyayi.apatya import feminine_luk
        from src.astadhyayi.taddhita import elision

        clause = "तस्मिन्निवृत्ते सति यो यतः प्राप्नोति स ततो भवति"
        self.assertIn(clause, unwrapped(feminine_luk().why))
        self.assertIn(clause,
                      unwrapped(elision(yuvan=True,
                                        before_ac=True).why))


class ThePatronymicRunAnswersEveryGroundItStates(unittest.TestCase):
    """
    Every row of the table has to be reachable, and the answer has to
    come back by the row's own sūtra. A row no query can reach is a
    rule the project has written down and cannot run.
    """

    def test_every_row_is_reachable_by_what_it_states(self):
        from src.astadhyayi.apatya import APATYA, apatya_affix

        for row in APATYA:
            # `wants` is part of the question, not a crutch: two rules
            # may state the same ground and give different affixes —
            # 4.1.129's ढ्रक् and 4.1.130's आरक् of गोधा, 4.1.132's
            # छण् and 4.1.133's ढक् of पितृष्वसृ — and both are right.
            where = {"wants": row.gives}
            if row.of:
                where["stem"] = row.of[0]
            if row.gana:
                where["gana"] = row.gana
            if row.stem_final:
                where["stem_final"] = row.stem_final
            if row.marked:
                where["marked"] = row.marked
            if row.kind:
                where["kind"] = row.kind
            if row.among:
                where["among"] = row.among
            if row.pre:
                where["pre"] = row.pre
            if row.dvyac:
                where["dvyac"] = True
            if row.stri_pratyaya:
                where["stri_pratyaya"] = True
            if row.of_samjna:
                where["samjna"] = row.of_samjna
            if row.authority:
                where["authority"] = row.authority
            if row.attitude:
                where["attitude"] = row.attitude
            if row.janapada:
                where["janapada"] = True
            with self.subTest(sutra=row.sutra, **where):
                answer = apatya_affix(**where)
                self.assertEqual(answer.by, row.sutra)
                self.assertEqual(answer.gives, row.gives)

    def test_and_an_unstated_ground_falls_to_the_default(self):
        from src.astadhyayi.apatya import apatya_affix
        from src.astadhyayi.taddhita import default_affix

        fallen = apatya_affix("upagu")
        self.assertEqual(fallen.by, "4.1.83")
        self.assertEqual(fallen.gives, default_affix().gives)

    def test_the_fall_through_is_declared_where_it_can_be(self):
        for sutra in ("4.1.95", "4.1.96", "4.1.112"):
            with self.subTest(sutra=sutra):
                self.assertIn("4.1.83", REGISTRY.get(sutra).reuses)

    def test_every_row_belongs_to_a_codified_sutra(self):
        from src.astadhyayi.apatya import APATYA

        for row in APATYA:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(REGISTRY.has(row.sutra))

class TwoNamesForOneDescendant(unittest.TestCase):
    """
    4.1.162–167. गोत्र from the grandson onward, युवन् while an elder
    of the line is living — and then two rules that make the choice
    turn on nothing grammatical at all.
    """

    def test_the_two_names_and_the_condition_between_them(self):
        from src.astadhyayi.apatya import descendant_name

        self.assertEqual(descendant_name().name, "gotra")
        self.assertEqual(descendant_name().by, "4.1.162")
        self.assertEqual(
            descendant_name(elder_alive=True).name, "yuvan")
        self.assertEqual(
            descendant_name(elder_alive=True).by, "4.1.163")

    def test_the_son_is_outside_the_name(self):
        from src.astadhyayi.apatya import descendant_name

        answer = descendant_name(generation=2)
        self.assertEqual(answer.name, "")
        self.assertIn("कौञ्जिः", answer.why)

    def test_a_word_s_case_changed_to_move_a_boundary(self):
        """
        4.1.162 counts from the grandson; 4.1.163 has to count from
        one further down, and the vṛtti gets it by rereading a case
        ending — षष्ठ्या विपरिणम्यते ... तेन चतुर्थादारभ्य युवसंज्ञा
        विधीयते.
        """
        from src.astadhyayi.apatya import descendant_name

        why = unwrapped(descendant_name(elder_alive=True).why)
        self.assertIn("षष्ठ्या विपरिणम्यते", why)
        self.assertIn("चतुर्थादारभ्य", why)

    def test_a_brother_needs_his_own_rule_because_he_is_no_ancestor(self):
        from src.astadhyayi.apatya import descendant_name

        answer = descendant_name(elder_alive=True, elder="bhrātṛ")
        self.assertEqual(answer.by, "4.1.164")
        self.assertIn("अकारणत्वात्", unwrapped(answer.why))

    def test_and_kinship_is_defined_by_ritual(self):
        """
        सप्तमपुरुषावधयः सपिण्डाः, and those for whom
        उभयत्र दशाहानि कुलस्यान्नं न भुज्यते. The grammar cites a
        law-book to fix a grammatical condition.
        """
        from src.astadhyayi.apatya import descendant_name

        why = unwrapped(descendant_name(elder_alive=True,
                                        elder="sapiṇḍa").why)
        self.assertIn("सप्तमपुरुषावधयः सपिण्डाः", why)
        self.assertIn("कुलस्यान्नं न भुज्यते", why)

    def test_one_rule_for_honour_and_one_for_scorn(self):
        """
        4.1.166 gives the YOUNG name to an elder out of respect;
        4.1.167 gives the LINEAGE name to a young man out of
        contempt. Two adjacent rules moving the same pair of names in
        opposite directions, and both optional.
        """
        from src.astadhyayi.apatya import descendant_name

        respect = descendant_name(attitude="pūjā")
        scorn = descendant_name(attitude="kutsā")
        self.assertEqual((respect.by, respect.name),
                         ("4.1.166", "yuvan"))
        self.assertEqual((scorn.by, scorn.name), ("4.1.167", "gotra"))
        self.assertTrue(respect.optional)
        self.assertTrue(scorn.optional)
        self.assertNotEqual(respect.name, scorn.name)

    def test_and_the_second_option_is_really_a_refusal(self):
        from src.astadhyayi.apatya import descendant_name

        why = unwrapped(descendant_name(attitude="kutsā").why)
        self.assertIn("निवृत्तिप्रधानो विकल्पः", why)
        self.assertIn("प्रतिपक्षाभावात्", why)

    def test_the_name_was_used_before_it_was_conferred(self):
        """
        4.1.93 एको गोत्रे turns on a name 4.1.162 confers — sixty-nine
        sūtras later. The vṛtti points at it: गोत्रप्रदेशाः.
        """
        from src.astadhyayi.apatya import descendant_name

        self.assertIn("एको गोत्रे", unwrapped(descendant_name().why))
        self.assertTrue(REGISTRY.has("4.1.93"))


class ASectionActingAsABarrier(unittest.TestCase):
    """
    4.1.174 ते तद्राजाः. Its pronoun reaches the affixes from 4.1.168
    and no further — न तु पूर्वे, **गोत्रयुवसंज्ञाकाण्डेन
    व्यवहितत्वात्**, because the naming section stands in the way.
    """

    def test_the_name_and_where_it_is_spent(self):
        from src.astadhyayi.apatya import tadraja

        self.assertEqual(tadraja().name, "tadrāja")
        self.assertEqual(tadraja().by, "4.1.174")
        self.assertIn("2.4.62", unwrapped(tadraja().why))

    def test_the_barrier_is_named(self):
        why = unwrapped(tadraja_why())
        self.assertIn("गोत्रयुवसंज्ञाकाण्डेन व्यवहितत्वात्", why)
        self.assertIn("न तु पूर्वे", why)

    def test_and_the_barrier_is_a_real_run_of_codified_rules(self):
        """
        The argument only works if 4.1.162–167 really do sit between
        4.1.168 and everything earlier. Six rules, all codified, all
        conferring a name rather than giving an affix.
        """
        from src.astadhyayi.apatya import APATYA

        barrier = ["4.1.%d" % n for n in range(162, 168)]
        for sutra in barrier:
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))
        gives = {row.sutra for row in APATYA}
        self.assertEqual(set(barrier) & gives, set())

    def test_anuvrtti_has_now_been_stopped_four_different_ways(self):
        """
        By a word (3.4.99's नित्यम्), read backward (4.1.18's
        सर्वत्र), carried half-way (4.1.27), and here blocked by a
        whole section. Each is on record in its own rule's notes.
        """
        for sutra, phrase in (
            ("3.4.99", "विकल्पनिवृत्त्यर्थम्"),
            ("4.1.18", "उत्तरसूत्रादिहापकृष्यते"),
            ("4.1.27", "नाव्ययग्रहणम्"),
            ("4.1.174", "व्यवहितत्वात्"),
        ):
            with self.subTest(sutra=sutra):
                self.assertIn(phrase,
                              unwrapped(REGISTRY.get(sutra).notes))


class RulesInsideTheSectionThatMakeNoDescendant(unittest.TestCase):
    """
    4.1.145 and 4.1.161 both stand under तस्यापत्यम् and both give an
    affix with no descendant-sense at all — अपत्यार्थोऽत्र नास्त्येव.
    """

    def test_both_say_so_in_the_same_words(self):
        for sutra in ("4.1.145", "4.1.161"):
            with self.subTest(sutra=sutra):
                self.assertIn("अपत्यार्थोऽत्र नास्त्येव",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_one_of_them_offers_a_check(self):
        """
        तथा च मानुषा इति बहुषु न लुग् भवति — the plural keeps the
        affix, which a descendant-affix would not. The claim is
        testable against 2.4.62's elision rather than merely asserted.
        """
        self.assertIn("बहुषु न लुग् भवति",
                      unwrapped(REGISTRY.get("4.1.161").notes))

    def test_the_section_they_stand_in_is_about_descendants(self):
        from src.astadhyayi.apatya import apatya_sense

        self.assertEqual(apatya_sense().by, "4.1.92")
        self.assertIn("तस्यापत्यम्", unwrapped(apatya_sense().why))


class ARuleBrokenSoItsBreachMayCarryInformation(unittest.TestCase):
    """
    4.1.150. 2.2.34 puts the word with fewer vowels first in a
    dvandva, and this rule puts the longer one there —
    **अल्पाच्तरस्यापूर्वनिपातो लक्षणव्यभिचारचिह्नम्**, and the breach
    is the sign that 1.3.10's *taken in order* does not apply.
    """

    def test_the_argument_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.1.150").notes)
        self.assertIn("अल्पाच्तरस्यापूर्वनिपातो", notes)
        self.assertIn("लक्षणव्यभिचारचिह्नम्", notes)
        self.assertIn("यथासंख्यमिह न भवति", notes)

    def test_and_the_rule_it_breaks_exists(self):
        from src.astadhyayi.corpus import collate

        self.assertIn("2.2.34", collate())
        self.assertIn("1.3.10", collate())

    def test_the_two_words_really_are_in_the_wrong_order(self):
        """
        The claim is about the sūtra's own text: फाण्टाहृति has four
        vowels and मिमत three, and the shorter one stands second.
        """
        from src.astadhyayi.corpus import collate

        rule = collate()["4.1.150"]
        for witness in rule.witnesses.values():
            with self.subTest(witness=witness):
                # GRETIL writes ḍ where Vidyut writes ṭ, so the test
                # is about the ORDER of the two words and not about a
                # letter the editions disagree on.
                self.assertLess(witness.index("hāṇḍ"
                                              if "ḍāh" in witness
                                              else "hāṇṭ"),
                                witness.index("mimatā"))


class FiveWaysOfSayingOptionally(unittest.TestCase):
    """
    4.1.160: उदीचां, प्राचाम्, अन्यतरस्याम्, बहुलम् — सर्व एते
    विकल्पार्थाः, **तेषामेकेनैव सिध्यति**. So the surplus is read as
    two other things instead.
    """

    def test_the_admission_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.1.160").notes)
        self.assertIn("सर्व एते विकल्पार्थाः", notes)
        self.assertIn("तेषामेकेनैव सिध्यति", notes)

    def test_and_the_surplus_is_given_two_readings(self):
        notes = unwrapped(REGISTRY.get("4.1.160").notes)
        self.assertIn("पूजार्थम्", notes)
        self.assertIn("वैचित्र्यार्थम्", notes)

    def test_the_same_naming_is_read_three_ways_in_the_project(self):
        """
        आचार्यग्रहणं पूजार्थम् at 3.4.18 and 4.1.130; and
        आचार्यग्रहणं वैचित्र्यार्थम् at 4.1.153. One move, three
        readings, and 4.1.160 gives both at once.
        """
        for sutra in ("3.4.18", "4.1.130"):
            with self.subTest(sutra=sutra):
                self.assertIn("पूजार्थम्",
                              unwrapped(REGISTRY.get(sutra).notes))
        self.assertIn("वैचित्र्यार्थम्",
                      unwrapped(REGISTRY.get("4.1.153").notes))


class TheElisionsThatCloseThePada(unittest.TestCase):
    """
    4.1.176–178, and the last of the three ends on a ज्ञापक about a
    rule two chapters away.
    """

    def test_the_affix_goes_in_the_feminine_and_not_otherwise(self):
        from src.astadhyayi.apatya import tadraja_luk

        self.assertTrue(tadraja_luk(feminine=True, of="avanti").holds)
        self.assertFalse(tadraja_luk(of="avanti").holds)

    def test_and_the_general_rule_reaches_any_a_affix(self):
        from src.astadhyayi.apatya import tadraja_luk

        answer = tadraja_luk(feminine=True, affix="añ")
        self.assertTrue(answer.holds)
        self.assertEqual(answer.by, "4.1.177")

    def test_but_three_groups_are_refused(self):
        from src.astadhyayi.apatya import tadraja_luk

        for where in (dict(gana="bhargādi"), dict(gana="yaudheyādi"),
                      dict(of="prācya")):
            with self.subTest(**where):
                answer = tadraja_luk(feminine=True, **where)
                self.assertFalse(answer.holds)
                self.assertEqual(answer.by, "4.1.178")

    def test_and_the_refusal_proves_a_rule_two_chapters_away(self):
        """
        कस्य पुनरकारस्य प्रत्ययस्य यौधेयादिभ्यो लुक् प्राप्तः
        प्रतिषिध्यते? पाञ्चमिकस्याञः — 5.3.117's. **एतदेव
        विज्ञापयति**: a refusal can only be refusing something, so
        4.1.177 must reach that far. And the fruit is a third rule
        entirely.
        """
        from src.astadhyayi.apatya import tadraja_luk
        from src.astadhyayi.corpus import collate

        why = unwrapped(tadraja_luk(feminine=True,
                                    gana="yaudheyādi").why)
        self.assertIn("एतदेव विज्ञापयति", why)
        self.assertIn("पाञ्चमिकस्य", why)
        self.assertIn("पर्श्वाद्यणो लुगिति", why)
        self.assertIn("5.3.117", collate())


class TheFirstPadaOfTheFourthAdhyayaIsFinished(unittest.TestCase):
    """
    4.1.1 to 4.1.178, checked against the corpus rather than a count.
    """

    def test_the_pada_matches_the_text_on_disk(self):
        from src.astadhyayi.corpus import collate

        codified = {s.id.number for s in REGISTRY.all()
                    if s.id.adhyaya == 4 and s.id.pada == 1}
        in_corpus = {int(key.rsplit(".", 1)[1]) for key in collate()
                     if key.startswith("4.1.")}
        self.assertEqual(codified, in_corpus)

    def test_and_so_does_every_pada_of_the_third_adhyaya(self):
        """
        Kept beside it because the two chapters divide the work:
        अध्याय ३ gives every affix after a ROOT and 4.1 opens the
        affixes after a STEM.
        """
        from src.astadhyayi.corpus import collate

        for pada in (1, 2, 3, 4):
            with self.subTest(pada="3.%d" % pada):
                codified = {s.id.number for s in REGISTRY.all()
                            if s.id.adhyaya == 3 and s.id.pada == pada}
                in_corpus = {
                    int(key.rsplit(".", 1)[1]) for key in collate()
                    if key.startswith("3.%d." % pada)}
                self.assertEqual(codified, in_corpus)

    def test_every_row_of_every_table_belongs_to_a_codified_sutra(self):
        from src.astadhyayi.apatya import APATYA
        from src.astadhyayi.stri import STRI_TABLE

        for table in (APATYA, STRI_TABLE):
            for row in table:
                with self.subTest(sutra=row.sutra):
                    self.assertTrue(REGISTRY.has(row.sutra))


def tadraja_why():
    """4.1.174's reasoning, wherever it is recorded."""
    from src.astadhyayi.apatya import tadraja

    return tadraja().why
