# -*- coding: utf-8 -*-
"""
४.४.१–३० — प्राग्वहतेष्ठक्, and the senses are actions.

4.1.83 put अण् over the taddhita section up to the rule that names
दीव्यति. This pāda opens one sūtra earlier by putting ठक् over
everything from here to 4.4.76. The two headings meet at the join, and
this file tests that the join really is where both rules say it is.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.sutra import REGISTRY
from tests import unwrapped


class TwoHeadingsMeetingAtOneJoin(unittest.TestCase):
    """
    4.1.83 प्राग्दीव्यतोऽण् runs up to the rule that names दीव्यति;
    4.4.1 प्राग्वहतेष्ठक् runs up to the rule that names वहति. The
    first of those rules is 4.4.2, so the two headings are the two
    halves of one division of the taddhita section.
    """

    def test_the_thak_heading_names_where_it_stops(self):
        """
        And the marker is not the last rule. 4.4.76 supplies the word
        वहति that bounds the heading; 4.4.75 opens यत् inside that
        range; so 4.4.74 is the last rule ठक् governs, and that rule
        says so — **ठकः पूर्णोऽवधिः**.
        """
        from src.astadhyayi.thak import (THAK_MARKER, THAK_RUN,
                                         thak_run)

        self.assertEqual(THAK_RUN, ("4.4.1", "4.4.74"))
        self.assertEqual(THAK_MARKER, "4.4.76")
        self.assertEqual(thak_run().by, "4.4.1")
        self.assertEqual(thak_run().gives, "ṭhak")
        self.assertIn(THAK_MARKER, thak_run().why)

    def test_and_the_marker_is_two_sutras_past_the_last_rule(self):
        from src.astadhyayi.thak import THAK_MARKER, THAK_RUN

        last = int(THAK_RUN[1].rsplit(".", 1)[1])
        marker = int(THAK_MARKER.rsplit(".", 1)[1])
        self.assertEqual(marker - last, 2)
        self.assertIn("ठकः पूर्णोऽवधिः",
                      unwrapped(REGISTRY.get("4.4.74").notes))

    def test_and_what_stands_between_them_is_another_heading(self):
        """
        The reason the two come apart. Nothing in the project had
        shown that a heading's marker and its last rule could differ
        until a second heading opened inside the first.
        """
        from src.astadhyayi.thak import YAT_RUN, provisions_for, yat_run

        opener = provisions_for("4.4.75")[0]
        self.assertTrue(opener.heading)
        self.assertEqual(opener.gives, "yat")
        self.assertEqual(YAT_RUN[0], "4.4.75")
        self.assertEqual(yat_run().gives, "yat")

    def test_and_the_an_heading_stops_at_the_rule_after_it(self):
        """
        The join. 4.1.83's boundary is the sūtra that names दीव्यति,
        and that sūtra is 4.4.2 — one past where ठक् takes over.
        """
        from src.astadhyayi.taddhita import default_affix

        self.assertEqual(default_affix().by, "4.1.83")
        self.assertEqual(default_affix().gives, "aṇ")
        self.assertIn("दीव्यति", unwrapped(REGISTRY.get("4.4.2").notes))
        self.assertIn("4.4.2", default_affix().why)

    def test_and_both_are_bounded_the_same_way(self):
        """
        **तदेकदेशो दीव्यच्छब्दोऽवधित्वेन गृह्यते** — 4.1.83's
        boundary is set by lifting ONE WORD out of the sūtra it stops
        at. 4.4.1 does the same with वहति out of 4.4.76.
        """
        # दीव्यच्छब्दः + अवधित्वेन is दीव्यच्छब्दोऽवधित्वेन,
        # and the initial अ is gone. Sandhi, fifteenth time.
        self.assertIn("ऽवधित्वेन गृह्यते", default_why())
        opening = unwrapped(REGISTRY.get("4.4.1").notes)
        # ...संशब्दनात् + यान् voices the final: संशब्दनाद् यान्.
        self.assertIn("प्रागेतस्माद् वहतिसंशब्दनाद्", opening)
        self.assertIn("तद्वहति रथयुगप्रासङ्गम्", opening)

    def test_and_the_boundary_rule_is_codified_now(self):
        """
        4.1.83's docstring has named 4.4.2 as its boundary since the
        patronymics were written, and until this pāda was opened that
        rule was only a citation. It is codified now, so the claim can
        be checked from both sides instead of read from one.
        """
        from src.astadhyayi.thak import provisions_for

        self.assertTrue(REGISTRY.has("4.4.2"))
        self.assertEqual({row.sense for row in provisions_for("4.4.2")},
                         {"dīvyati", "khanati", "jayati", "jita"})
        self.assertIn("दीव्यति", default_why())

    def test_and_the_rule_each_stops_at_is_in_the_corpus(self):
        from src.astadhyayi.corpus import collate

        for sutra in ("4.4.2", "4.4.76"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, collate())

    def test_and_the_boundary_rule_has_arrived(self):
        """
        The exact shortfall, collected. 4.4.76 was not codified when
        the heading was written and the test said so; it is codified
        now, and the borrowing of its word can be checked against the
        rule itself.
        """
        from src.astadhyayi.thak import provisions_for

        self.assertTrue(REGISTRY.has("4.4.76"))
        self.assertIn("वहति", unwrapped(REGISTRY.get("4.4.76").notes))

    def test_and_the_marker_rule_is_governed_by_the_other_heading(self):
        """
        A sūtra used as a boundary-post by one section and governed
        by another: 4.4.76 supplies the word that bounds ठक्, and
        itself gives यत्.
        """
        from src.astadhyayi.thak import provisions_for

        self.assertEqual(provisions_for("4.4.76")[0].gives, "yat")
        self.assertNotEqual(provisions_for("4.4.76")[0].gives, "ṭhak")

    def test_and_the_third_heading_reaches_out_of_the_chapter(self):
        """
        4.1.83 bounded अण् with a word from 4.4.2; 4.4.1 bounded ठक्
        with a word from 4.4.76; 4.4.75 bounds यत् with a word from
        5.1.5. The same device three times, and the third crosses a
        chapter.

        The debt this test was carrying — that 5.1.5 lay outside
        what was codified — has been paid, so the assertion turns
        round: the marker is codified now, and it must be the rule
        the heading said it was.
        """
        from src.astadhyayi.corpus import collate
        from src.astadhyayi.krita import provisions_for
        from src.astadhyayi.thak import YAT_MARKER, YAT_RUN

        self.assertEqual(YAT_MARKER, "5.1.5")
        self.assertIn("5.1.5", collate())
        self.assertTrue(REGISTRY.has("5.1.5"))

        marker = provisions_for("5.1.5")[0]
        self.assertEqual(marker.sense, "hita")
        self.assertEqual(marker.case, "caturthī")
        self.assertTrue(marker.borrows)
        self.assertEqual(marker.gives, "")
        self.assertIn("हितसंशब्दनाद्",
                      unwrapped(REGISTRY.get("4.4.75").notes))

    def test_and_the_marker_is_a_sense_and_never_an_affix(self):
        """
        Why every one of these headings is bounded by a sense-word
        and not by the affix that actually displaces it — which is
        the question 5.1.1 puts and answers.

        **अर्थोऽवधित्वेन गृहीतः, न प्रत्ययः; तेन प्राक् ठञः छ इति
        नोक्तम्.** So the four markers are दीव्यति, वहति, हित and
        क्रीत, each of them the sense a rule names, and not one of
        them an affix.
        """
        from src.astadhyayi.corpus import collate
        from src.astadhyayi.krita import CHA_MARKER
        from src.astadhyayi.thak import THAK_MARKER, YAT_MARKER

        self.assertIn("अर्थोऽवधित्वेन गृहीतः, न प्रत्ययः",
                      unwrapped(REGISTRY.get("5.1.1").notes))
        witnesses = collate()
        for marker, word in ((THAK_MARKER, "vahati"),
                             (YAT_MARKER, "hita"),
                             (CHA_MARKER, "krīta")):
            with self.subTest(marker=marker):
                self.assertIn(marker, witnesses)
                self.assertTrue(
                    any(word in text for text
                        in witnesses[marker].witnesses.values()),
                    marker)

    def test_and_the_second_heading_closes_the_way_the_first_did(self):
        """
        **यतः पूर्णोऽवधिः, अतः परमन्यः प्रत्ययोऽधिक्रियते** at
        4.4.144 — word for word what 4.4.74 said of ठक्. So this
        heading's marker is 5.1.5 and its last rule is 4.4.144,
        because 5.1.1 opens छ inside the range.

        Twice in one pāda, and the second time settles it: the gap
        between a heading's MARKER and its LAST RULE is how these
        headings nest, not an irregularity at one of them.
        """
        from src.astadhyayi.thak import YAT_MARKER, YAT_RUN

        self.assertEqual(YAT_RUN, ("4.4.75", "4.4.144"))
        self.assertNotEqual(YAT_RUN[1], YAT_MARKER)
        for sutra in ("4.4.74", "4.4.144"):
            with self.subTest(sutra=sutra):
                self.assertIn("पूर्णोऽवधिः",
                              unwrapped(REGISTRY.get(sutra).notes))
                self.assertIn("अतः परमन्यः प्रत्यय",
                              unwrapped(REGISTRY.get(sutra).notes))


def default_why():
    from src.astadhyayi.taddhita import default_affix

    return default_affix().why


class TheHeadingAnswersWhereNothingNarrowerDoes(unittest.TestCase):
    """
    Every rule of this pāda names its own action, and only the
    heading does not. So a query that names no action is asking after
    the heading — which is the whole point of प्राग्वहतेष्ठक्.
    """

    def test_asking_nothing_reaches_the_heading(self):
        from src.astadhyayi.thak import by_means_of

        self.assertEqual(by_means_of().by, "4.4.1")
        self.assertEqual(by_means_of().gives, "ṭhak")

    def test_and_so_does_an_action_no_rule_names(self):
        from src.astadhyayi.thak import by_means_of

        self.assertEqual(by_means_of(sense="paśyati").by, "4.4.1")
        self.assertEqual(by_means_of(sense="paśyati").gives, "ṭhak")

    def test_and_only_the_headings_name_no_action(self):
        """
        Two of them now: 4.4.1 for ठक् and 4.4.75 for यत्. Every
        other row states the action its rule is about.
        """
        from src.astadhyayi.thak import THAK_TABLE

        headings = {row.sutra for row in THAK_TABLE if row.heading}
        self.assertEqual(headings, {"4.4.1", "4.4.75"})
        for row in THAK_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(row.sense or row.heading)

    def test_and_the_two_headings_do_not_compete(self):
        """
        They govern different stretches, so no query reaches both.
        4.4.1 answers where nothing narrower does; 4.4.75 is reached
        by asking after its own affix.
        """
        from src.astadhyayi.thak import by_means_of

        self.assertEqual(by_means_of().by, "4.4.1")
        self.assertEqual(by_means_of(wants="yat").by, "4.4.75")

    def test_and_the_exceptions_really_displace_it(self):
        from src.astadhyayi.thak import by_means_of

        for stem, sense, affix in (("gopuccha", "tarati", "ṭhañ"),
                                   ("nau", "tarati", "ṭhan"),
                                   ("ākarṣa", "carati", "ṣṭhal"),
                                   ("cūrṇa", "saṃsṛṣṭa", "ini")):
            with self.subTest(stem=stem):
                answer = by_means_of(stem, sense=sense)
                self.assertEqual(answer.gives, affix)
                self.assertNotEqual(answer.by, "4.4.1")


class ATaddhitaForegroundsTheMeans(unittest.TestCase):
    """
    4.4.2's **क्रियाप्रधानत्वेऽपि चाख्यातस्य तद्धितः स्वभावात्
    साधनप्रधानः** — though a finite verb foregrounds the ACTION, a
    taddhita by its nature foregrounds the MEANS. The clearest
    statement in the section of what its affixes are for.
    """

    def test_the_statement_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.4.2").notes)
        self.assertIn("क्रियाप्रधानत्वेऽपि चाख्यातस्य", notes)
        self.assertIn("तद्धितः स्वभावात् साधनप्रधानः", notes)

    def test_and_the_case_is_the_instrument_and_never_the_agent(self):
        """
        **सर्वत्र करणे तृतीया समर्थविभक्तिः**, and देवदत्तेन जितम्
        gets nothing — **अनभिधानात्**, on the ground of usage that
        this project has met four times now.
        """
        notes = unwrapped(REGISTRY.get("4.4.2").notes)
        self.assertIn("सर्वत्र करणे तृतीया समर्थविभक्तिः", notes)
        self.assertIn("अनभिधानात्", notes)

    def test_and_each_case_is_opened_by_a_rule_that_names_it(self):
        """
        Four so far, and each is spoken in its own words at the rule
        that introduces it: the instrumental for a means, the
        accusative for what one moves along, the genitive for what is
        due, the nominative for what a man deals in.
        """
        from src.astadhyayi.thak import provisions_for

        opened = {"4.4.1": "tṛtīyā", "4.4.28": "dvitīyā",
                  "4.4.47": "ṣaṣṭhī", "4.4.51": "prathamā"}
        for sutra, case in opened.items():
            with self.subTest(sutra=sutra):
                self.assertEqual(provisions_for(sutra)[0].case, case)

    def test_and_the_instrumental_is_the_one_the_heading_carries(self):
        """
        Not the commonest for ever — but it is the case the heading
        itself states, and the one every rule holds until 4.4.28
        changes it in its own words.
        """
        from src.astadhyayi.thak import THAK_TABLE, provisions_for

        self.assertEqual(provisions_for("4.4.1")[0].case, "tṛtīyā")
        early = [row for row in THAK_TABLE
                 if int(row.sutra.rsplit(".", 1)[1]) < 28]
        for row in early:
            with self.subTest(sutra=row.sutra):
                self.assertEqual(row.case, "tṛtīyā")

    def test_and_the_rules_that_change_it_say_so(self):
        for sutra, word in (("4.4.28", "द्वितीयासमर्थविभक्तिः"),
                            ("4.4.47", "षष्ठीसमर्थात्"),
                            ("4.4.51", "प्रथमासमर्थाद्")):
            with self.subTest(sutra=sutra):
                self.assertIn(word,
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_the_rule_that_changes_it_explains_how_it_can(self):
        """
        वृत् is intransitive, so an accusative with it needs
        defending: **क्रियाविशेषणमकर्मकाणामपि कर्म भवति**.
        """
        notes = unwrapped(REGISTRY.get("4.4.28").notes)
        self.assertIn("वृतिरकर्मकः", notes)
        self.assertIn("क्रियाविशेषणमकर्मकाणामपि कर्म भवति", notes)


class OneRuleFourSensesAndTwoOfThemOneForm(unittest.TestCase):
    """
    4.4.2 names four: दीव्यति, खनति, जयति, जितम्. Three are finite
    verbs and the fourth a participle; and two of them give the same
    word from the same base.
    """

    def test_the_four_are_four_rows(self):
        from src.astadhyayi.thak import provisions_for

        rows = provisions_for("4.4.2")
        self.assertEqual({row.sense for row in rows},
                         {"dīvyati", "khanati", "jayati", "jita"})

    def test_and_all_four_give_the_heading_s_affix(self):
        from src.astadhyayi.thak import provisions_for

        for row in provisions_for("4.4.2"):
            with self.subTest(sense=row.sense):
                self.assertEqual(row.gives, "ṭhak")

    def test_and_two_of_them_are_reached_separately(self):
        from src.astadhyayi.thak import by_means_of

        for sense in ("dīvyati", "jayati"):
            with self.subTest(sense=sense):
                self.assertEqual(by_means_of(sense=sense).by, "4.4.2")

    def test_and_the_same_word_answers_both(self):
        """
        अक्षैर्दीव्यति आक्षिकः and अक्षैर्जयति आक्षिकः — one form for
        the man who plays with dice and the man who wins with them.
        """
        notes = unwrapped(REGISTRY.get("4.4.2").notes)
        self.assertIn("अक्षैर्दीव्यति", notes)
        self.assertIn("अक्षैर्जयति", notes)


class AWordSplitByWhichOfItsSensesIsMeant(unittest.TestCase):
    """
    Two rules of this run turn on a homonym, and each resolves it a
    different way. 4.4.18's कुटिलिका means both a crooked movement
    and a smith's rod, and BOTH readings take the affix. 4.4.24's
    लवण means both the substance salt and the quality of saltiness,
    and only one of them causes the elision.
    """

    def test_one_word_gives_two_men(self):
        notes = unwrapped(REGISTRY.get("4.4.18").notes)
        self.assertIn("कुटिलिका वक्रगतिः", notes)
        self.assertIn("कर्माराणामायुधकर्षणी", notes)
        self.assertIn("कौटिलिको मृगः", notes)
        self.assertIn("कौटिलिकः कर्मारः", notes)

    def test_and_the_other_word_is_split_by_the_elision(self):
        notes = unwrapped(REGISTRY.get("4.4.24").notes)
        self.assertIn("द्रव्यवाची लवणशब्दो लुकं प्रयोजयति", notes)
        self.assertIn("न गुणवाची", notes)

    def test_and_only_the_second_removes_the_affix(self):
        from src.astadhyayi.thak import by_means_of, provisions_for

        self.assertTrue(provisions_for("4.4.24")[0].elides)
        self.assertFalse(provisions_for("4.4.18")[0].elides)

        gone = by_means_of("lavaṇa", sense="saṃsṛṣṭa", elided=True)
        self.assertEqual(gone.by, "4.4.24")
        self.assertTrue(gone.elided)
        self.assertEqual(gone.gives, "")

    def test_and_both_elisions_here_are_conditional(self):
        """
        Two rules of the pāda remove an affix, and neither does it
        unconditionally: 4.4.24 only where the base names a
        substance, 4.4.79 only on one side of an option that the
        rule's mere existence creates.
        """
        from src.astadhyayi.thak import THAK_TABLE, provisions_for

        eliding = {row.sutra for row in THAK_TABLE if row.elides}
        self.assertEqual(eliding, {"4.4.24", "4.4.79",
                                   "4.4.125", "4.4.126"})
        self.assertTrue(provisions_for("4.4.79")[0].optional)
        self.assertIn("वचनसामर्थ्यात् पक्षे लुग् विधीयते",
                      unwrapped(REGISTRY.get("4.4.79").notes))

    def test_and_the_two_late_ones_remove_a_possessive(self):
        """
        4.4.125 and 4.4.126 do not remove the affix they give — they
        remove the मतुप् the BASE already carried, in the same act.
        **लुक् च मतोरिति प्रकृतिनिर्ह्रासः.**
        """
        from src.astadhyayi.thak import provisions_for

        for sutra in ("4.4.125", "4.4.126"):
            with self.subTest(sutra=sutra):
                self.assertTrue(provisions_for(sutra)[0].elides)
                self.assertTrue(provisions_for(sutra)[0].gives)
        self.assertIn("लुक् च मतोरिति प्रकृतिनिर्ह्रासः",
                      unwrapped(REGISTRY.get("4.4.125").notes))


class AnAffixThatMayNotBeLeftOff(unittest.TestCase):
    """
    4.4.20's नित्यम् is not the ordinary *always*.
    **नित्यग्रहणं स्वातन्त्र्यनिवृत्त्यर्थम्; तेन त्र्यन्तं नित्यं
    मप्प्रत्ययान्तमेव भवति, विषयान्तरे न प्रयोक्तव्यम्** — a stem
    ending in that क्त्रि may not be used ANYWHERE without this
    affix. Not a rule about when an affix comes, but about a word
    that cannot stand alone.
    """

    def test_the_argument_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.4.20").notes)
        self.assertIn("नित्यग्रहणं स्वातन्त्र्यनिवृत्त्यर्थम्", notes)
        self.assertIn("विषयान्तरे न प्रयोक्तव्यम्", notes)

    def test_and_the_affix_it_points_at_is_codified(self):
        """
        **ड्वितः क्त्रिः** [3.3.88] — the त्रि meant is that rule's,
        and the condition would name nothing without it.
        """
        self.assertTrue(REGISTRY.has("3.3.88"))
        self.assertIn("3.3.88", unwrapped(REGISTRY.get("4.4.20").notes))

    def test_and_the_word_it_makes_is_the_common_one(self):
        self.assertIn("कृत्रिमम्",
                      unwrapped(REGISTRY.get("4.4.20").notes))

    def test_and_the_row_states_the_condition_as_a_class(self):
        from src.astadhyayi.thak import provisions_for

        row = provisions_for("4.4.20")[0]
        self.assertEqual(row.of_samjna, "ktri-anta")
        self.assertEqual(row.gives, "map")
        self.assertEqual(row.of, ())


class AKarikaThatCorrectsItsOwnCount(unittest.TestCase):
    """
    4.4.7's verse counts the ष-initial affixes of the ठक् section at
    six, and then says the count is of rule-STATEMENTS:
    **विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु सप्त** — the affixes
    are seven, because one of the six rules gives two.
    """

    def test_the_verse_and_its_correction_are_on_record(self):
        notes = unwrapped(REGISTRY.get("4.4.7").notes)
        self.assertIn("षितः षडेते ठगधिकारे", notes)
        self.assertIn("विधिवाक्यापेक्षं च षट्त्वम्", notes)
        self.assertIn("प्रत्ययास्तु सप्त", notes)

    def test_and_the_six_bases_are_held_as_data(self):
        from src.astadhyayi.thak import SIT_AFFIX_BASES

        self.assertEqual(len(SIT_AFFIX_BASES), 6)
        self.assertEqual(len(set(SIT_AFFIX_BASES)), 6)

    def test_and_the_ones_codified_so_far_give_a_sa_affix(self):
        """
        Three of the six are reached; each must give an affix
        beginning with ष्, or the verse would be counting something
        else. The rest will be checked as they arrive.
        """
        from src.astadhyayi.thak import provisions_for

        reached = {"4.4.9": "ākarṣa", "4.4.10": "parpādi",
                   "4.4.16": "bhastrādi"}
        for sutra, base in reached.items():
            with self.subTest(sutra=sutra, base=base):
                self.assertTrue(REGISTRY.has(sutra))
                affix = provisions_for(sutra)[0].gives
                self.assertTrue(affix.startswith("ṣ"), affix)

    def test_and_the_bases_named_match_the_rules_reached(self):
        from src.astadhyayi.thak import (SIT_AFFIX_BASES,
                                         provisions_for)

        self.assertIn("ākarṣa", SIT_AFFIX_BASES)
        self.assertIn("parpādi", SIT_AFFIX_BASES)
        self.assertIn("bhastrādi", SIT_AFFIX_BASES)
        self.assertEqual(provisions_for("4.4.9")[0].of, ("ākarṣa",))
        self.assertEqual(provisions_for("4.4.10")[0].gana, "parpādi")
        self.assertEqual(provisions_for("4.4.16")[0].gana, "bhastrādi")


class OneEntryReadAsACompoundAndAsItsParts(unittest.TestCase):
    """
    **संघातविगृहीतार्थम्** — twice in two consecutive rules. 4.4.12's
    धनुर्दण्ड gives three forms and 4.4.13's क्रयविक्रय gives three:
    the compound and each of its members.
    """

    def test_both_rules_state_the_device(self):
        for sutra in ("4.4.12", "4.4.13"):
            with self.subTest(sutra=sutra):
                self.assertIn("संघातविगृहीतार्थम्",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_each_gives_three_forms(self):
        notes = unwrapped(REGISTRY.get("4.4.12").notes)
        for form in ("धानुर्दण्डिकः", "धानुष्कः", "दाण्डिकः"):
            with self.subTest(form=form):
                self.assertIn(form, notes)

        notes = unwrapped(REGISTRY.get("4.4.13").notes)
        for form in ("क्रयविक्रयिकः", "क्रयिकः", "विक्रयिकः"):
            with self.subTest(form=form):
                self.assertIn(form, notes)

    def test_and_the_row_keeps_the_members_the_rule_names(self):
        from src.astadhyayi.thak import provisions_for

        self.assertEqual(provisions_for("4.4.13")[0].of,
                         ("vasna", "kraya", "vikraya"))


class TheKarikaCountCollected(unittest.TestCase):
    """
    4.4.7's verse said six ष-initial affixes from six grounds and then
    corrected itself — **विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु
    सप्त**, six statements but seven affixes. 4.4.31 is the statement
    that gives two, so the correction can now be checked rather than
    read.
    """

    def test_the_rule_that_makes_the_count_seven_is_codified(self):
        from src.astadhyayi.thak import provisions_for

        rows = provisions_for("4.4.31")
        self.assertEqual(len(rows), 2)
        self.assertEqual({row.gives for row in rows},
                         {"ṣṭhan", "ṣṭhac"})

    def test_and_both_of_its_affixes_begin_with_that_letter(self):
        from src.astadhyayi.thak import provisions_for

        for row in provisions_for("4.4.31"):
            with self.subTest(gives=row.gives):
                self.assertTrue(row.gives.startswith("ṣ"))

    def test_and_it_names_the_verse_it_completes(self):
        self.assertIn("प्रत्ययास्तु सप्त",
                      unwrapped(REGISTRY.get("4.4.31").notes))
        self.assertIn("प्रत्ययास्तु सप्त",
                      unwrapped(REGISTRY.get("4.4.7").notes))

    def test_and_five_of_the_six_grounds_are_now_codified(self):
        """
        आकर्ष, पर्पादि, भस्त्रादि, कुसीद-सूत्र and किशरादि are
        reached; आवसथ lies past 4.4.60. Each of the five must give an
        affix beginning with ष्.
        """
        from src.astadhyayi.thak import provisions_for

        reached = {"4.4.9": "ākarṣa", "4.4.10": "parpādi",
                   "4.4.16": "bhastrādi", "4.4.31": "kusīda-sūtra",
                   "4.4.53": "kiśarādi"}
        for sutra in reached:
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))
                for row in provisions_for(sutra):
                    self.assertTrue(row.gives.startswith("ṣ"), row.gives)

    def test_and_the_sixth_has_arrived(self):
        """
        आवसथ was the one ground the verse names that had not been
        reached, and the test said so as the exact shortfall. 4.4.74
        is codified now, so all six can be checked at once.
        """
        from src.astadhyayi.thak import SIT_AFFIX_BASES, provisions_for

        self.assertIn("āvasatha", SIT_AFFIX_BASES)
        self.assertTrue(REGISTRY.has("4.4.74"))
        self.assertEqual(provisions_for("4.4.74")[0].gives, "ṣṭhal")

    def test_and_now_all_six_grounds_give_a_sa_affix(self):
        """
        The verse's whole claim, checkable at last: six statements,
        every one of them giving an affix that begins with ष्.
        """
        from src.astadhyayi.thak import SIT_AFFIX_BASES, provisions_for

        rules = {"4.4.9": "ākarṣa", "4.4.10": "parpādi",
                 "4.4.16": "bhastrādi", "4.4.31": "kusīda-sūtra",
                 "4.4.53": "kiśarādi", "4.4.74": "āvasatha"}
        self.assertEqual(set(rules.values()), set(SIT_AFFIX_BASES))
        self.assertEqual(len(rules), 6)
        affixes = []
        for sutra in rules:
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))
                for row in provisions_for(sutra):
                    self.assertTrue(row.gives.startswith("ṣ"), row.gives)
                    affixes.append(row.gives)
        # प्रत्ययास्तु सप्त — seven affixes from six statements.
        self.assertEqual(len(affixes), 7)


class ANameReachesItsSynonymsAndItsSpecies(unittest.TestCase):
    """
    4.4.35: **स्वरूपस्य पर्यायाणां तद्विशेषाणां च ग्रहणमिहेष्यते** —
    the word itself, the words that mean the same, and the words for
    KINDS of the thing. Three words in the rule and a whole
    vocabulary of hunters out of them.
    """

    def test_the_principle_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.4.35").notes)
        self.assertIn("स्वरूपस्य पर्यायाणां तद्विशेषाणां च", notes)

    def test_and_all_three_kinds_of_example_are_given(self):
        notes = unwrapped(REGISTRY.get("4.4.35").notes)
        self.assertIn("पाक्षिकः", notes)      # the word itself
        self.assertIn("शाकुनिकः", notes)      # a synonym
        self.assertIn("मायूरिकः", notes)      # a species
        self.assertIn("तैत्तिरिकः", notes)

    def test_and_the_rule_names_only_three_words(self):
        from src.astadhyayi.thak import provisions_for

        self.assertEqual(provisions_for("4.4.35")[0].of,
                         ("pakṣin", "matsya", "mṛga"))


class TwoIdiomsTheVrttiHasToExplain(unittest.TestCase):
    """
    4.4.46 gives two words whose meanings no derivation could supply.
    लालाटिकः is the servant who never comes near — because
    **सर्वावयवेभ्यो ललाटं दूरे दृश्यते**, the forehead is what is
    seen from farthest off. कौक्कुटिकः is the monk who walks watching
    the small patch his foot will fall on.
    """

    def test_both_explanations_are_on_record(self):
        notes = unwrapped(REGISTRY.get("4.4.46").notes)
        self.assertIn("सर्वावयवेभ्यो ललाटं दूरे दृश्यते", notes)
        self.assertIn("स्वामिनः कार्येषु नोपतिष्ठते", notes)
        self.assertIn("पादविक्षेपदेशे चक्षुः संयम्य गच्छति", notes)

    def test_and_the_rule_restricts_what_is_denoted(self):
        """
        **संज्ञाग्रहणमभिधेयनियमार्थम्, न तु रूढ्यर्थम्** — the word
        *name* narrows what may be meant; it does not make the form
        conventional.
        """
        from src.astadhyayi.thak import provisions_for

        self.assertIn("संज्ञाग्रहणमभिधेयनियमार्थम्",
                      unwrapped(REGISTRY.get("4.4.46").notes))
        self.assertEqual(provisions_for("4.4.46")[0].result, "saṃjñā")

    def test_and_the_two_bases_are_both_named(self):
        from src.astadhyayi.thak import provisions_for

        self.assertEqual(provisions_for("4.4.46")[0].of,
                         ("lalāṭa", "kukkuṭī"))


class OneWordMadeTwiceInTwoSenses(unittest.TestCase):
    """
    धानुष्कः is produced twice in this pāda: at 4.4.12 by an entry
    read as a compound AND its members, in the sense *lives by it*;
    and at 4.4.57 in the sense *that is his weapon*. One who lives by
    the bow against one who fights with it.
    """

    def test_both_rules_produce_it(self):
        for sutra in ("4.4.12", "4.4.57"):
            with self.subTest(sutra=sutra):
                self.assertIn("धानुष्कः",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_the_two_senses_are_different(self):
        from src.astadhyayi.thak import provisions_for

        self.assertEqual(provisions_for("4.4.12")[0].sense, "jīvati")
        self.assertEqual(provisions_for("4.4.57")[0].sense, "praharaṇa")

    def test_and_the_answers_come_by_different_rules(self):
        from src.astadhyayi.thak import by_means_of

        lives = by_means_of(gana="vetanādi", sense="jīvati")
        fights = by_means_of(sense="praharaṇa", case="prathamā")
        self.assertEqual(lives.by, "4.4.12")
        self.assertEqual(fights.by, "4.4.57")
        self.assertEqual(lives.gives, fights.gives)

    def test_and_the_second_rule_says_so(self):
        self.assertIn("4.4.12", unwrapped(REGISTRY.get("4.4.57").notes))


class TwoSensesTheWorldKeepsApart(unittest.TestCase):
    """
    4.4.50's अवक्रय against 4.4.47's धर्म्य. **नन्ववक्रयोऽपि
    धर्म्यमेव? नैतदस्ति; लोकपीडया धर्मातिक्रमेणाप्यवक्रयो भवति** —
    is rent not also what is DUE? No: rent can be exacted to the
    people's hurt and in defiance of right.
    """

    def test_the_objection_and_the_answer_are_recorded(self):
        notes = unwrapped(REGISTRY.get("4.4.50").notes)
        self.assertIn("नन्ववक्रयोऽपि धर्म्यमेव", notes)
        self.assertIn("लोकपीडया धर्मातिक्रमेणाप्यवक्रयो भवति", notes)

    def test_and_the_two_rules_give_the_same_affix(self):
        """
        Which is why the question had to be settled by argument: the
        forms are identical and only the sense divides them.
        """
        from src.astadhyayi.thak import provisions_for

        self.assertEqual(provisions_for("4.4.47")[0].gives,
                         provisions_for("4.4.50")[0].gives)
        self.assertEqual(provisions_for("4.4.47")[0].case,
                         provisions_for("4.4.50")[0].case)

    def test_and_the_same_examples_appear_under_both(self):
        for form in ("शौल्कशालिक", "आकरिक", "आपणिक", "गौल्मिक"):
            with self.subTest(form=form):
                self.assertIn(form,
                              unwrapped(REGISTRY.get("4.4.47").notes))
                self.assertIn(form,
                              unwrapped(REGISTRY.get("4.4.50").notes))

    def test_and_the_senses_still_answer_apart(self):
        from src.astadhyayi.thak import by_means_of

        self.assertEqual(by_means_of(case="ṣaṣṭhī",
                                     sense="dharmya").by, "4.4.47")
        self.assertEqual(by_means_of(case="ṣaṣṭhī",
                                     sense="avakraya").by, "4.4.50")


class AQualifierAbsorbedIntoTheWord(unittest.TestCase):
    """
    **पण्यमिति विशेषणं तद्धितवृत्तावन्तर्भूतम्, अतः पण्यशब्दो न
    प्रयुज्यते** at 4.4.51, and **शिल्पं तद्धितवृत्तावन्तर्भवति** at
    4.4.55. The qualifier is taken up INTO the derived word, so
    saying it again would be saying it twice.
    """

    def test_both_rules_state_it(self):
        self.assertIn("तद्धितवृत्तावन्तर्भूतम्",
                      unwrapped(REGISTRY.get("4.4.51").notes))
        self.assertIn("तद्धितवृत्तावन्तर्भवति",
                      unwrapped(REGISTRY.get("4.4.55").notes))

    def test_and_the_second_adds_what_the_base_word_stands_for(self):
        """
        **मृदङ्गवादने वर्तमानो मृदङ्गशब्दः प्रत्ययमुत्पादयति** — the
        drum's name here stands for the PLAYING of it, and it is that
        which takes the affix.
        """
        self.assertIn("मृदङ्गवादने वर्तमानो मृदङ्गशब्दः",
                      unwrapped(REGISTRY.get("4.4.55").notes))

    def test_and_both_take_the_nominative_and_the_genitive_sense(self):
        from src.astadhyayi.thak import provisions_for

        for sutra in ("4.4.51", "4.4.55"):
            with self.subTest(sutra=sutra):
                self.assertEqual(provisions_for(sutra)[0].case,
                                 "prathamā")


class ThreeTermsOfPhilosophyFixedByUsage(unittest.TestCase):
    """
    4.4.60 makes आस्तिक, नास्तिक and दैष्टिक — and the vṛtti insists
    the rule is not about merely having an opinion. **न च
    मतिसत्तामात्रे प्रत्यय इष्यते**, and what each word means is got
    **अभिधानशक्तिस्वभावात्**, from the nature of what the words can
    denote.
    """

    def test_the_three_are_all_produced_by_one_rule(self):
        from src.astadhyayi.thak import provisions_for

        row = provisions_for("4.4.60")[0]
        self.assertEqual(row.of, ("asti", "nāsti", "diṣṭa"))
        self.assertEqual(row.sense, "mati")

    def test_and_the_restriction_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.4.60").notes)
        self.assertIn("न च मतिसत्तामात्रे प्रत्यय इष्यते", notes)
        self.assertIn("परलोकोऽस्तीति यस्य मतिरस्ति", notes)
        self.assertIn("प्रमाणानुपातिनी यस्य मतिः", notes)

    def test_and_the_ground_of_it_is_named(self):
        # तदेतद् + अभिधान is तदेतदभिधान; the initial अ is gone.
        self.assertIn("तदेतदभिधानशक्तिस्वभावाल् लभ्यते",
                      unwrapped(REGISTRY.get("4.4.60").notes))

    def test_and_the_bases_are_not_ordinary_stems(self):
        """
        **अस्तिनास्तिशब्दौ निपातौ, वचनसामर्थ्याद् वा आख्याताद्
        वाक्याच् च प्रत्ययः** — the first two are particles, or else
        the affix comes from a finite verb and from a sentence. The
        vārttikas on 4.4.1 had already allowed both.
        """
        notes = unwrapped(REGISTRY.get("4.4.60").notes)
        self.assertIn("अस्तिनास्तिशब्दौ निपातौ", notes)
        self.assertIn("आख्याताद् वाक्याच् च प्रत्ययः", notes)
        self.assertIn("वाक्यादेतत् प्रत्ययविधानम्",
                      unwrapped(REGISTRY.get("4.4.1").notes))


class ThreeGreatHeadingsBoundedOneWay(unittest.TestCase):
    """
    4.1.83 प्राग्दीव्यतोऽण्, 4.4.1 प्राग्वहतेष्ठक्, 4.4.75
    प्राग्घिताद् यत् — three headings over the taddhita section, each
    bounded by lifting one word out of the sūtra it stops at. The
    third reaches out of the chapter.
    """

    def test_all_three_are_codified_and_so_are_their_markers(self):
        from src.astadhyayi.corpus import collate
        from src.astadhyayi.thak import THAK_MARKER, YAT_MARKER

        for sutra in ("4.1.83", "4.4.1", "4.4.75"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))
        self.assertTrue(REGISTRY.has("4.4.2"))
        self.assertTrue(REGISTRY.has(THAK_MARKER))
        self.assertIn(YAT_MARKER, collate())
        self.assertTrue(REGISTRY.has(YAT_MARKER))

    def test_and_each_names_the_word_it_lifted(self):
        self.assertIn("दीव्यति",
                      unwrapped(REGISTRY.get("4.4.1").notes))
        self.assertIn("वहतिसंशब्दनाद्",
                      unwrapped(REGISTRY.get("4.4.1").notes))
        self.assertIn("हितसंशब्दनाद्",
                      unwrapped(REGISTRY.get("4.4.75").notes))

    def test_and_the_ranges_are_contiguous(self):
        """
        अण् to 4.4.1, ठक् 4.4.1–74, यत् 4.4.75 onward. No gap and no
        overlap in what actually governs.
        """
        from src.astadhyayi.thak import THAK_RUN, YAT_RUN

        self.assertEqual(int(THAK_RUN[1].rsplit(".", 1)[1]) + 1,
                         int(YAT_RUN[0].rsplit(".", 1)[1]))

    def test_and_only_the_third_leaves_the_chapter(self):
        from src.astadhyayi.thak import THAK_MARKER, YAT_MARKER

        self.assertTrue(THAK_MARKER.startswith("4."))
        self.assertTrue(YAT_MARKER.startswith("5."))


class TwoRulesGroundedInAnotherText(unittest.TestCase):
    """
    4.4.71 and 4.4.73 both take their condition from outside the
    grammar. The first applies at a place or hour **शास्त्रेण
    प्रतिषिद्धौ**, forbidden for study; the second to a mendicant
    whose distance from the village is fixed by rule.
    """

    def test_the_first_names_what_forbids(self):
        notes = unwrapped(REGISTRY.get("4.4.71").notes)
        self.assertIn("शास्त्रेण प्रतिषिद्धौ", notes)
        self.assertIn("श्माशानिकः", notes)

    def test_and_the_second_quotes_the_rule_it_depends_on(self):
        notes = unwrapped(REGISTRY.get("4.4.73").notes)
        # वस्तव्यम् + इति is वस्तव्यमिति; the virāma goes.
        self.assertIn("ग्रामात् क्रोशे वस्तव्यमिति शास्त्रम्",
                      notes)
        # निकटवासः + तत्र is निकटवासस्तत्र.
        self.assertIn("यस्य शास्त्रतो निकटवासस्तत्रायं विधिः",
                      notes)

    def test_and_the_ordinary_case_is_excluded(self):
        """
        अदेशकालादिति किम्? स्रुघ्नेऽधीते — an ordinary place and an
        ordinary hour get nothing. The rule exists only for what the
        other text forbids.
        """
        from src.astadhyayi.thak import provisions_for

        self.assertEqual(provisions_for("4.4.71")[0].of_samjna,
                         "adeśa-akāla")
        self.assertIn("स्रुघ्नेऽधीते",
                      unwrapped(REGISTRY.get("4.4.71").notes))


class ANegationMovedFromInstrumentToAction(unittest.TestCase):
    """
    4.4.83's अधनुषा. The objection: the exclusion is idle, since
    **न हि धनुषा पद्य इत्युक्ते विवक्षितोऽर्थः प्रतीयते** — the words
    would not convey the meaning anyway. The answer moves it:
    **धनुष्प्रतिषेधेन व्यधनक्रिया विशेष्यते**, it qualifies the ACT,
    restricting the rule to a piercing in which a bow could not be
    the instrument.
    """

    def test_the_objection_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.4.83").notes)
        self.assertIn("विवक्षितोऽर्थः प्रतीयते", notes)

    def test_and_the_answer_relocates_the_negation(self):
        notes = unwrapped(REGISTRY.get("4.4.83").notes)
        self.assertIn("धनुष्प्रतिषेधेन व्यधनक्रिया विशेष्यते", notes)
        self.assertIn("यस्यां धनुष्करणं न संभाव्यत इति", notes)

    def test_and_what_the_relocation_keeps_out(self):
        """
        **तेनेह न भवति — चौरं विध्यति, शत्रुं विध्यति** — a man shot
        at gets no derived word, which the exclusion as first stated
        would not have prevented.
        """
        from src.astadhyayi.thak import provisions_for

        self.assertIn("चौरं विध्यति",
                      unwrapped(REGISTRY.get("4.4.83").notes))
        self.assertEqual(provisions_for("4.4.83")[0].result,
                         "adhanuṣā")


class WordsWhoseMeaningIsAWholeDescription(unittest.TestCase):
    """
    Four rules of this block make words the commentary has to unpack
    at length, because nothing in the parts gives the sense.
    """

    def test_the_word_for_a_student(self):
        """
        **गुरुकार्येष्ववहितस्तच्छिद्रावरणप्रवृत्तश्छत्रशीलः
        शिष्यश्छात्रः** — from *umbrella*, one whose habit is to
        COVER his teacher's faults.
        """
        self.assertIn("तच्छिद्रावरणप्रवृत्तश्छत्रशीलः",
                      unwrapped(REGISTRY.get("4.4.62").notes))

    def test_the_word_that_counts_a_pupil_s_mistakes(self):
        notes = unwrapped(REGISTRY.get("4.4.63").notes)
        self.assertIn("परीक्षाकाले पठतः स्खलितम्", notes)
        self.assertIn("उदात्ते कर्तव्ये योऽनुदात्तं करोति",
                      unwrapped(REGISTRY.get("4.4.64").notes))

    def test_the_word_for_a_state_of_mud(self):
        notes = unwrapped(REGISTRY.get("4.4.87").notes)
        self.assertIn("नातिद्रवो", notes)
        self.assertIn("नातिशुष्क", notes)

    def test_and_the_word_for_a_cow_given_against_a_debt(self):
        notes = unwrapped(REGISTRY.get("4.4.89").notes)
        # धेनुः + उत्तमर्णाय is धेनुरुत्तमर्णाय.
        self.assertIn("धेनुरुत्तमर्णाय ऋणप्रदानाद् दोहनार्थं दीयते",
                      notes)
        self.assertIn("पीतदुग्धेति यस्याः प्रसिद्धिः", notes)

    def test_and_all_four_rules_are_reachable(self):
        from src.astadhyayi.thak import by_means_of

        answers = {
            by_means_of(gana="chatrādi", sense="śīla").by,
            by_means_of(sense="karma-adhyayane-vṛtta").by,
            by_means_of("pada", sense="dṛśya").by,
            by_means_of("dhenu", sense="dohana-dattā",
                        result="saṃjñā").by,
        }
        self.assertEqual(answers,
                         {"4.4.62", "4.4.63", "4.4.87", "4.4.89"})


class OneAffixTwoSensesAcrossAPada(unittest.TestCase):
    """
    4.4.81 हलसीराट् ठक् repeats 4.3.124 word for word — the same two
    bases and the same affix, in the sense *what belongs to a plough*
    there and *the ox that draws one* here.
    """

    def test_both_rules_are_codified(self):
        for sutra in ("4.3.124", "4.4.81"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))

    def test_and_they_give_the_same_affix_from_the_same_bases(self):
        from src.astadhyayi.kala_taddhita import provisions_for as kala
        from src.astadhyayi.thak import provisions_for as thak

        earlier = kala("4.3.124")[0]
        later = thak("4.4.81")[0]
        self.assertEqual(earlier.gives, later.gives)
        self.assertEqual(earlier.of, later.of)

    def test_and_the_senses_differ(self):
        from src.astadhyayi.kala_taddhita import provisions_for as kala
        from src.astadhyayi.thak import provisions_for as thak

        self.assertEqual(kala("4.3.124")[0].sense, "idam")
        self.assertEqual(thak("4.4.81")[0].sense, "vahati")

    def test_and_the_later_rule_names_the_earlier(self):
        self.assertIn("4.3.124", unwrapped(REGISTRY.get("4.4.81").notes))


class EveryRowIsReachableAndBelongsToARule(unittest.TestCase):
    """
    A row no query can reach is a rule the project has written down
    and cannot run.
    """

    def test_every_row_answers_by_its_own_sutra(self):
        from src.astadhyayi.thak import THAK_TABLE, by_means_of

        for row in THAK_TABLE:
            where = {}
            if row.of:
                where["stem"] = row.of[0]
            if row.gana:
                where["gana"] = row.gana
            if row.sense:
                where["sense"] = row.sense
            if row.case:
                where["case"] = row.case
            if row.result:
                where["result"] = row.result
            if row.of_samjna:
                where["samjna"] = row.of_samjna
            if row.upadha:
                where["upadha"] = row.upadha
            if row.vowels:
                where["vowels"] = row.vowels
            if row.pre:
                where["pre"] = row.pre
            if row.stem_final:
                where["stem_final"] = row.stem_final
            if row.usage:
                where["usage"] = row.usage
            if row.elides:
                where["elided"] = True
            if row.gives:
                where["wants"] = row.gives
            with self.subTest(sutra=row.sutra, **where):
                self.assertEqual(by_means_of(**where).by, row.sutra)

    def test_every_affix_a_rule_also_gives_is_reachable_too(self):
        from src.astadhyayi.thak import THAK_TABLE, by_means_of

        asked = 0
        for row in THAK_TABLE:
            for affix in row.also_gives:
                where = {"sense": row.sense, "wants": affix}
                if row.of:
                    where["stem"] = row.of[0]
                if row.usage:
                    where["usage"] = row.usage
                if row.result:
                    where["result"] = row.result
                with self.subTest(sutra=row.sutra, wants=affix):
                    answer = by_means_of(**where).by
                    if answer != row.sutra:
                        # 4.4.116 restates यत् for अग्र precisely so
                        # that 4.4.117 shall NOT displace it —
                        # **ताभ्यां बाधा मा भूदिति पुनर्विधीयते** —
                        # so that affix answering by the earlier rule
                        # is the rule working, not a gap.
                        self.assertLess(
                            int(answer.rsplit(".", 1)[1]),
                            int(row.sutra.rsplit(".", 1)[1]))
                        self.assertEqual(
                            by_means_of(**where).gives, affix)
                    asked += 1
        self.assertGreaterEqual(asked, 2)

    def test_every_row_belongs_to_a_codified_sutra(self):
        from src.astadhyayi.thak import THAK_TABLE

        for row in THAK_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(REGISTRY.has(row.sutra))

    def test_and_the_pada_is_contiguous_as_far_as_it_is_read(self):
        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 4}
        self.assertEqual(have, set(range(1, max(have) + 1)))

    def test_and_every_rule_read_so_far_has_a_row(self):
        from src.astadhyayi.thak import THAK_TABLE

        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 4}
        stated = {int(row.sutra.rsplit(".", 1)[1]) for row in THAK_TABLE}
        self.assertEqual(stated, have)


if __name__ == "__main__":
    unittest.main()
