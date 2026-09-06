# -*- coding: utf-8 -*-
"""
५.१.१–३० — three headings in thirty sūtras.

छ from 5.1.1, ठञ् from 5.1.18, ठक् from 5.1.19 inside the ठञ्. The
chapter before opened one heading to a pāda; this one opens three
before its thirtieth rule, and the third is bounded by आ instead of
प्राक्, so it takes in the sūtra that names it rather than stopping
short of it. This file tests that each of the three governs exactly
what its own vṛtti says it governs, and that where a rule names a
sense and no affix, the fall-through really falls where it should.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.krita import (
    ARHIYA_MARKER, ARHIYA_RUN, ARHIYA_SENSES, CHA_MARKER, CHA_RUN,
    CHA_SENSES, KRITA_TABLE, LATER_SENSES, MEASURES, TADANTA_ALUKI,
    BHAVA_SENSES, PADA_SENSES, THAN_MARKER, THAN_SENSES,
    VATI_SENSES, arhiya_run, cha_run, fit_for, provisions_for,
    than_run)
from src.astadhyayi.sutra import REGISTRY
from tests import unwrapped


class ThreeHeadingsInThirtySutras(unittest.TestCase):
    """
    The densest stretch of प्राक्-headings in the grammar, and the
    one place where a heading is enjoined INSIDE another heading as
    its own exception.
    """

    def test_the_first_heading_names_where_it_stops(self):
        """
        **प्रागेतस्मात् क्रीतसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामः,
        छप्रत्ययस्तेष्वधिकृतो वेदितव्यः** — छ for every sense named
        before the rule that says क्रीत.
        """
        self.assertEqual(CHA_MARKER, "5.1.37")
        self.assertEqual(cha_run().affix, "cha")
        self.assertEqual(cha_run().sutra, "5.1.1")
        self.assertIn(CHA_MARKER, cha_run().why)
        self.assertTrue(provisions_for("5.1.1")[0].heading)

    def test_and_its_marker_is_twenty_sutras_past_its_end(self):
        """
        The widest of the four gaps between a heading's marker and
        its last rule — and 5.1.17 says exactly why: **छयतोः
        पूर्णोऽवधिः। इतः परमन्यः प्रत्ययो विधीयते.**

        Not a census of the gap but the reason for it: 5.1.18 opens
        another heading inside the range, so छ cannot reach 5.1.36.
        """
        self.assertEqual(CHA_RUN, ("5.1.1", "5.1.17"))
        self.assertNotEqual(CHA_RUN[1], CHA_MARKER)
        self.assertLess(int(CHA_RUN[1].rsplit(".", 1)[1]),
                        int(CHA_MARKER.rsplit(".", 1)[1]))

        closing = unwrapped(REGISTRY.get("5.1.17").notes)
        self.assertIn("छयतोः पूर्णोऽवधिः", closing)
        self.assertIn("इतः परमन्यः प्रत्ययो विधीयते", closing)

        opener = int(CHA_RUN[1].rsplit(".", 1)[1]) + 1
        self.assertTrue(provisions_for("5.1.%d" % opener)[0].heading)

    def test_and_the_formula_is_the_one_the_chapter_before_used(self):
        """
        4.4.74 closed ठक् with **ठकः पूर्णोऽवधिः, अतः परमन्यः
        प्रत्ययो विधीयते**; 4.4.144 closed यत् with the same words;
        5.1.17 closes both छ and यत् with them again.

        Three times, so it is the Kāśikā's way of closing a heading
        and not an accident at one of them.
        """
        for sutra in ("4.4.74", "4.4.144", "5.1.17"):
            with self.subTest(sutra=sutra):
                notes = unwrapped(REGISTRY.get(sutra).notes)
                self.assertIn("पूर्णोऽवधिः", notes)
                self.assertIn("परमन्यः प्रत्यय", notes)

    def test_and_a_heading_is_bounded_by_a_sense_never_by_an_affix(self):
        """
        5.1.1's vṛtti raises the alternative and rejects it:
        **अर्थोऽवधित्वेन गृहीतः, न प्रत्ययः; तेन प्राक् ठञः छ इति
        नोक्तम्** — the rule could have said *before the ठञ्*, since
        5.1.18 is where छ actually stops, and it does not.

        So no marker in the project is an affix-name.
        """
        notes = unwrapped(REGISTRY.get("5.1.1").notes)
        self.assertIn("अर्थोऽवधित्वेन गृहीतः, न प्रत्ययः", notes)
        self.assertIn("प्राक् ठञः छ इति नोक्तम्", notes)

    def test_the_second_heading_opens_where_the_first_leaves_off(self):
        """
        प्राग्वतेष्ठञ् — and its marker is 5.1.115, the rule that
        says वति. The last rule is deliberately not fixed yet: three
        headings have now shown that a marker and a last rule need
        not be the same sūtra, so claiming one before reading the
        stretch would be a guess.
        """
        self.assertEqual(THAN_MARKER, "5.1.115")
        self.assertEqual(than_run().affix, "ṭhañ")
        self.assertEqual(than_run().sutra, "5.1.18")
        self.assertTrue(provisions_for("5.1.18")[0].heading)

        first, last = CHA_RUN
        self.assertEqual(int(last.rsplit(".", 1)[1]) + 1,
                         int(than_run().sutra.rsplit(".", 1)[1]))

    def test_the_third_heading_takes_in_its_own_limit(self):
        """
        Every other great heading says प्राक् and stops SHORT of the
        rule that names it. 5.1.19 says आ, and the vṛtti draws the
        consequence: **अभिविधावयमाकारः, तेनार्हत्यर्थेऽपि ठग्
        भवत्येव** — ठक् applies in the sense of अर्हति too.
        """
        self.assertEqual(ARHIYA_MARKER, "5.1.63")
        self.assertEqual(arhiya_run().affix, "ṭhak")
        self.assertIn(ARHIYA_MARKER, arhiya_run().why)

        notes = unwrapped(REGISTRY.get("5.1.19").notes)
        self.assertIn("अभिविधावयमाकारः", notes)
        self.assertIn("र्हत्यर्थेऽपि ठग् भवत्येव", notes)

    def test_but_it_still_runs_on_past_the_marker_it_takes_in(self):
        """
        Taking the marker IN is not the same as ending there. Eight
        rules stand past 5.1.63 still naming अर्हति, and 5.1.71
        closes the account in the formula: **आर्हीयाणां ठगादीनां
        पूर्णोऽवधिः। अतः परं प्राग्वतीयष्ठञेव भवति.**

        So the gap between a heading's marker and its last rule
        holds of this one too. What is peculiar to it is the
        INCLUSION, not the coincidence.
        """
        self.assertEqual(ARHIYA_RUN, ("5.1.19", "5.1.71"))
        self.assertNotEqual(ARHIYA_RUN[1], ARHIYA_MARKER)
        self.assertLess(int(ARHIYA_MARKER.rsplit(".", 1)[1]),
                        int(ARHIYA_RUN[1].rsplit(".", 1)[1]))

        closing = unwrapped(REGISTRY.get("5.1.71").notes)
        self.assertIn("आर्हीयाणां ठगादीनां पूर्णोऽवधिः", closing)
        self.assertIn("प्राग्वतीयष्ठञेव भवति", closing)

        for sutra in ("5.1.64", "5.1.66", "5.1.71"):
            with self.subTest(sutra=sutra):
                self.assertEqual(provisions_for(sutra)[0].sense,
                                 "arhati")

    def test_and_a_fifth_heading_carries_a_condition_and_no_affix(self):
        """
        5.1.78 कालात् supplies nothing: it says only that the base
        must be a word for TIME. **कालादित्यधिकारः। यदित ऊर्ध्वम्
        अनुक्रमिष्यामः कालादित्येवं तद् वेदितव्यम्.**

        That is why it can stand inside the ठञ् heading without
        competing with it — every rule under it still gives ठञ्
        unless it says otherwise.
        """
        from src.astadhyayi.krita import (KALA_MARKER, KALA_RUN,
                                          kala_run)

        row = provisions_for("5.1.78")[0]
        self.assertTrue(row.heading)
        self.assertEqual(row.gives, "")
        self.assertEqual(row.of_samjna, "kāla")
        self.assertEqual(kala_run().affix, "")
        self.assertEqual(KALA_RUN, ("5.1.78", "5.1.96"))

        under = fit_for(samjna="kāla", sense="nirvṛtta",
                        case="tṛtīyā")
        self.assertEqual(under.affix, "ṭhañ")
        self.assertEqual(under.sutra, "5.1.79")

    def test_and_that_heading_closes_the_way_all_the_others_did(self):
        """
        5.1.78 names 5.1.97 as its boundary — **कालादित्यधिकारो
        व्युष्टादिभ्योऽण् इति यावत्** — and 5.1.96 stops one short:
        **कालाधिकारस्य पूर्णोऽवधिः। अतः परं सामान्येन
        प्रत्ययविधानम्.** The fifth heading, the fifth time.
        """
        from src.astadhyayi.krita import KALA_MARKER, KALA_RUN

        self.assertEqual(KALA_MARKER, "5.1.97")
        self.assertNotEqual(KALA_RUN[1], KALA_MARKER)
        self.assertIn("व्युष्टादिभ्योऽण् इति यावत्",
                      unwrapped(REGISTRY.get("5.1.78").notes))
        self.assertIn("कालाधिकारस्य पूर्णोऽवधिः",
                      unwrapped(REGISTRY.get("5.1.96").notes))

        # And the rule past the boundary has a base that is not a
        # time-word at all, which is why the heading stops there.
        self.assertEqual(provisions_for(KALA_MARKER)[0].of_samjna, "")
        self.assertEqual(provisions_for(KALA_RUN[1])[0].of_samjna,
                         "kāla")

    def test_and_it_stands_inside_the_heading_it_excepts(self):
        """
        **ठञधिकारमध्ये तदपवादः ठग् विधीयते** — a heading enjoined in
        the MIDDLE of another heading, as its exception. So the ठक्
        range lies wholly inside the ठञ् one, and the ठक् rule
        records the ठञ् rule as what it excepts.
        """
        self.assertEqual(provisions_for("5.1.19")[0].excepts,
                         ("5.1.18",))
        self.assertIn("ठञधिकारमध्ये तदपवादः ठग् विधीयते",
                      unwrapped(REGISTRY.get("5.1.19").notes))

        opens = int(ARHIYA_RUN[0].rsplit(".", 1)[1])
        than = int(than_run().sutra.rsplit(".", 1)[1])
        marker = int(THAN_MARKER.rsplit(".", 1)[1])
        self.assertLess(than, opens)
        self.assertLess(int(ARHIYA_RUN[1].rsplit(".", 1)[1]), marker)


class WhatEachHeadingCovers(unittest.TestCase):
    """
    A rule that names no sense of its own is not free of sense: it
    serves the senses of ITS heading. **प्राक्क्रीतीयेष्वर्थेषु**
    and **आर्हीयेष्वर्थेषु** are two different phrases for two
    different sets, and the vṛttis use whichever belongs.
    """

    def test_a_sense_of_the_first_heading_never_reaches_the_second(self):
        """
        गोपुच्छ is kept out of 5.1.19's ठक्, so it falls back — and
        it must fall back to the ठञ् of 5.1.18, which is the vṛtti's
        own counter-example **गौपुच्छिकम्**, not to the छ of 5.1.1,
        whose senses it is not asked under.
        """
        answer = fit_for("gopuccha", sense="ārhīya", case="tṛtīyā")
        self.assertEqual(answer.affix, "ṭhañ")
        self.assertEqual(answer.sutra, "5.1.18")

    def test_and_the_two_measures_the_third_heading_keeps_out(self):
        """
        संख्या and परिमाण by name — but being kept out of ठक् is not
        the same as falling back to ठञ्.

        A measure has no other rule, so प्रास्थिकम् is ठञ्. A
        NUMERAL has 5.1.22 waiting for it, so पञ्चकः is कन् — and
        the vṛtti's ठञ् example for a numeral, **षाष्टिकम्**, is one
        that 5.1.22 ALSO excludes, षष्टि ending in ति. Two
        exclusions deep before the heading is reached.
        """
        self.assertEqual(provisions_for("5.1.19")[0].excludes,
                         ("gopuccha", "saṃkhyā", "parimāṇa"))

        measure = fit_for(samjna="parimāṇa", sense="ārhīya",
                          case="tṛtīyā")
        self.assertEqual(measure.affix, "ṭhañ")
        self.assertEqual(measure.sutra, "5.1.18")

        numeral = fit_for(samjna="saṃkhyā", sense="ārhīya",
                          case="tṛtīyā")
        self.assertEqual(numeral.affix, "kan")
        self.assertEqual(numeral.sutra, "5.1.22")
        self.assertIn("षाष्टिकम्",
                      unwrapped(REGISTRY.get("5.1.19").notes))
        self.assertIn("साप्ततिकम्",
                      unwrapped(REGISTRY.get("5.1.22").notes))

    def test_and_an_unnamed_price_reaches_the_third_heading(self):
        """Anything not excepted takes ठक् — नैष्किकम्, पाणिकम्."""
        answer = fit_for("pāṇi", sense="ārhīya", case="tṛtīyā")
        self.assertEqual(answer.affix, "ṭhak")
        self.assertEqual(answer.sutra, "5.1.19")

    def test_the_four_kinds_of_measurement_are_told_apart(self):
        """
        The rule excepts two of four, so the four have to be
        distinguishable: **भेदगणनं संख्या; गुरुत्वमानमुन्मानम्;
        आयाममानं प्रमाणम्; आरोहपरिणाहमानं परिमाणम्.**

        The property, not the count: the two the rule names are
        excluded and the two it does not name are not.
        """
        named = {name for name, _ in MEASURES}
        excluded = set(provisions_for("5.1.19")[0].excludes)
        self.assertTrue(excluded & named)
        self.assertEqual(named - excluded - {"unmāna", "pramāṇa"},
                         set())
        self.assertNotIn("unmāna", excluded)
        self.assertNotIn("pramāṇa", excluded)

    def test_the_senses_split_at_the_boundary_the_vrtti_draws(self):
        """
        छ covers हित, तदर्थ and तदस्य-स्यात्; ठञ् and ठक् cover
        आर्हीय. No sense belongs to both, and every sense a row of
        the table names belongs to one of them.
        """
        self.assertEqual(set(CHA_SENSES) & set(ARHIYA_SENSES), set())
        stated = {row.sense for row in KRITA_TABLE if row.sense}
        self.assertEqual(stated - set(PADA_SENSES), set())

    def test_and_the_split_follows_the_sutra_numbers(self):
        """
        Which set a row belongs to is decided by where it STANDS, and
        the boundary is 5.1.17 — so no rule up to there names an
        आर्हीय sense and none after it names a छ sense.
        """
        for row in KRITA_TABLE:
            if not row.sense:
                continue
            number = int(row.sutra.rsplit(".", 1)[1])
            with self.subTest(sutra=row.sutra):
                if number <= int(CHA_RUN[1].rsplit(".", 1)[1]):
                    self.assertIn(row.sense, CHA_SENSES)
                elif number <= 114:
                    self.assertIn(row.sense, THAN_SENSES)
                elif number <= 118:
                    self.assertIn(row.sense, VATI_SENSES)
                else:
                    self.assertIn(row.sense, BHAVA_SENSES)


class ARuleThatNamesASenseAndNoAffix(unittest.TestCase):
    """
    5.1.5, 5.1.12 and 5.1.16 say **यथाविहितम्** — as already
    enjoined. The affix comes from whatever rule the base itself
    answers to, and the resolver executes that by asking again with
    the sense dropped. A fall-through IS the reuse.
    """

    def test_what_makes_a_rule_one_that_borrows(self):
        """
        It names a SENSE and gives no affix — and nothing else in
        the table does both, so the property picks out exactly the
        rules that say यथाविहितम् without any of them being listed.
        """
        for row in KRITA_TABLE:
            with self.subTest(sutra=row.sutra):
                if row.borrows:
                    self.assertTrue(row.sense)
                    self.assertEqual(row.gives, "")
                    self.assertEqual(row.also_gives, ())
                    self.assertFalse(row.lup)
                elif (row.sense and not row.lup
                        and not row.refuses and row.gives == ""):
                    # 5.1.59 alone: it lays ten words down ready-made
                    # rather than giving an affix to a base. (5.1.121
                    # also names a sense and gives nothing, and it is
                    # excluded above — a refusal supplies nothing by
                    # definition.)
                    self.assertEqual(row.sutra, "5.1.59")

    def test_where_a_sense_is_opened_by_a_fall_through_and_where_not(self):
        """
        Every sense the छ heading covers is opened by a rule that
        names it and leaves the affix **यथाविहितम्** — because in
        that stretch the affix really does vary with the base: छ by
        the heading, यत् by 5.1.2, either by 5.1.4.

        Past the division at 5.1.37 that stops being true. Where one
        affix serves every base, the rule simply names it: 5.1.42
        तस्येश्वरः and 5.1.43 तत्र विदितः give their two affixes to
        their two words outright, and so do most of the rules after
        5.1.71. So the fall-through is not a formula the section
        repeats — it is used where it does work.
        """
        borrowing = {row.sutra for row in KRITA_TABLE if row.borrows}
        for sutra in ("5.1.5", "5.1.12", "5.1.16"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, borrowing)

        named = {row.sense for row in KRITA_TABLE if row.borrows}
        self.assertEqual(set(CHA_SENSES) - named, set())
        self.assertEqual(
            set(ARHIYA_SENSES) - {"ārhīya"} - named,
            {"īśvara", "vidita"})

        for sutra, sense in (("5.1.42", "īśvara"),
                             ("5.1.43", "vidita"),
                             ("5.1.72", "vartayati"),
                             ("5.1.79", "nirvṛtta")):
            with self.subTest(sutra=sutra):
                rows = provisions_for(sutra)
                self.assertEqual({row.sense for row in rows}, {sense})
                for row in rows:
                    self.assertTrue(row.gives)
                    self.assertFalse(row.borrows)

    def test_and_the_one_fall_through_past_the_division(self):
        """
        5.1.80 तमधीष्टो भृतो भूतो भावी is the only rule after 5.1.71
        that names senses and no affix — and it names FOUR at once,
        which is exactly the case where the affix cannot be fixed in
        advance.
        """
        late = {row.sutra for row in KRITA_TABLE
                if row.borrows
                and int(row.sutra.rsplit(".", 1)[1]) > 71}
        self.assertEqual(late, {"5.1.80"})
        self.assertEqual(provisions_for("5.1.80")[0].sense,
                         "adhīṣṭādi")

    def test_and_no_rule_before_the_division_states_an_affix_alone(self):
        """
        The other half of 5.1.37's statement: from 5.1.19 to 5.1.36
        the rules give AFFIXES and name neither a sense nor a case,
        because both are still to be stated.
        """
        for row in KRITA_TABLE:
            number = int(row.sutra.rsplit(".", 1)[1])
            if not 19 <= number <= 36 or row.heading:
                continue
            with self.subTest(sutra=row.sutra):
                self.assertEqual(row.sense, "")
                self.assertEqual(row.case, "")
                self.assertTrue(row.gives or row.lup)

    def test_and_the_fall_through_reaches_the_heading(self):
        """
        वत्सेभ्यो हितो गोधुक् **वत्सीयः** — वत्स is in no list and
        no class, so the sense-rule falls through to 5.1.1's छ, and
        the answer says it was borrowed.
        """
        answer = fit_for("vatsa", sense="hita", case="caturthī")
        self.assertEqual(answer.affix, "cha")
        self.assertEqual(answer.sutra, "5.1.1")
        self.assertTrue(answer.borrowed)
        self.assertEqual(answer.case, "caturthī")

    def test_and_a_base_with_a_rule_of_its_own_needs_no_fall(self):
        """
        गव्यम् and हविष्यम् are the vṛtti's own examples under
        5.1.5, and both are गवादि — so 5.1.2 names them directly and
        answers without the fall-through being needed at all.

        The flag records the path, so it must be OFF here and on for
        वत्स. That difference is the whole content of यथाविहितम्: it
        does something only where nothing else does.
        """
        answer = fit_for("gav", gana="gavādi", sense="hita",
                         case="caturthī")
        self.assertEqual(answer.affix, "yat")
        self.assertEqual(answer.sutra, "5.1.2")
        self.assertFalse(answer.borrowed)

        heading = fit_for("vatsa", sense="hita", case="caturthī")
        self.assertTrue(heading.borrowed)

    def test_and_an_optional_rule_keeps_its_option(self):
        """
        अपूप्यम्, अपूपीयम् — 5.1.4 gives यत् optionally, and the
        answer must arrive with the option intact rather than with
        one of the two forms silently chosen.
        """
        answer = fit_for("apūpa", gana="apūpādi", sense="hita",
                         case="caturthī")
        self.assertEqual(answer.affix, "yat")
        self.assertEqual(answer.sutra, "5.1.4")
        self.assertTrue(answer.optional)

    def test_and_a_fall_through_cannot_fall_into_another(self):
        """
        The second pass excludes the borrowing rows, so no query can
        bounce from one यथाविहितम् to the next. Every sense-rule
        lands on a rule that actually names an affix, or on a
        heading.
        """
        for sense, case in (("hita", "caturthī"),
                            ("tadartha", "caturthī"),
                            ("tadasya-syāt", "prathamā")):
            with self.subTest(sense=sense):
                answer = fit_for("vatsa", sense=sense, case=case,
                                 samjna="vikṛti")
                self.assertTrue(answer.borrowed)
                self.assertNotIn(answer.sutra,
                                 ("5.1.5", "5.1.12", "5.1.16"))
                self.assertTrue(answer.affix)

    def test_and_the_borrowed_case_is_the_borrowing_rule_s(self):
        """
        5.1.16's base stands in the NOMINATIVE where 5.1.5's and
        5.1.12's stand in the dative. The affix is fetched from
        elsewhere; the case is not, and must survive the fall.
        """
        answer = fit_for("prākāra", sense="tadasya-syāt",
                         case="prathamā")
        self.assertTrue(answer.borrowed)
        self.assertEqual(answer.case, "prathamā")
        self.assertEqual(provisions_for("5.1.16")[0].case, "prathamā")
        self.assertEqual(provisions_for("5.1.5")[0].case, "caturthī")


class OneWordUnderTwoRules(unittest.TestCase):
    """
    नाभि stands in the गवादि list and is also a part of the body, so
    two rules reach it — and only one of them changes its shape.
    """

    def test_the_gana_entry_substitutes_and_the_other_does_not(self):
        """
        **नाभिशब्दो यत्प्रत्ययमुत्पादयति, नभं चादेशमापद्यते** —
        नभ्योऽक्षः by 5.1.2. But **गवादिषु यता सन्नियुक्तो नभभावो
        ऽत्र न भवति**: under 5.1.6 the substitution does not happen,
        and the form is नाभ्यं तैलम्.

        Same affix, different rule, and the difference is visible
        only in the substitute.
        """
        as_gana = fit_for("nābhi", gana="gavādi", sense="hita",
                          case="caturthī")
        as_limb = fit_for("nābhi", samjna="śarīrāvayava",
                          sense="hita", case="caturthī")
        self.assertEqual(as_gana.affix, as_limb.affix)
        self.assertEqual(as_gana.affix, "yat")
        self.assertEqual(as_gana.sutra, "5.1.2")
        self.assertEqual(as_limb.sutra, "5.1.6")
        self.assertEqual(as_gana.adesa, "nabha")
        self.assertEqual(as_limb.adesa, "")

    def test_and_the_other_substituting_entry_behaves_the_same_way(self):
        """ऊधसोऽनङ् च — ऊधन्यः, the same double duty."""
        answer = fit_for("ūdhas", gana="gavādi", sense="hita",
                         case="caturthī")
        self.assertEqual(answer.affix, "yat")
        self.assertEqual(answer.adesa, "anaṅ")

    def test_and_a_gana_entry_may_carry_an_option_instead(self):
        """
        **शुनः संप्रसारणं वा च दीर्घत्वम्** — शुन्यम्, शून्यम्. The
        entry gives a choice and no substitute, where the two before
        gave a substitute and no choice.
        """
        answer = fit_for("śvan", gana="gavādi", sense="hita",
                         case="caturthī")
        self.assertEqual(answer.affix, "yat")
        self.assertTrue(answer.optional)
        self.assertEqual(answer.adesa, "")
        self.assertIn("चकारस्यानुक्तसमुच्चयार्थत्वाद्",
                      unwrapped(REGISTRY.get("5.1.2").notes))


class WhereAnEarlierRuleBeatsALaterOne(unittest.TestCase):
    """
    पूर्वविप्रतिषेध twice in this block, and both times the vṛtti
    says so in as many words.
    """

    def test_three_words_are_kept_by_the_rule_that_stands_first(self):
        """
        **तत्र सर्वत्र पूर्वविप्रतिषेधेन यत् प्रत्यय एवेष्यते** —
        सनङ्गव्यं चर्म against 5.1.15, चरव्यास्तण्डुलाः against
        5.1.4, सक्तव्या धानाः against the अन्नविकार entry.
        """
        notes = unwrapped(REGISTRY.get("5.1.2").notes)
        self.assertIn("पूर्वविप्रतिषेधेन यत् प्रत्यय एवेष्यते",
                      notes)
        for form in ("सनङ्गव्यं चर्म", "चरव्यास्तण्डुलाः",
                     "सक्तव्या धानाः"):
            with self.subTest(form=form):
                self.assertIn(form, notes)

    def test_and_a_shoe_s_leather_goes_to_the_earlier_rule_too(self):
        """
        **चर्मण्यपि प्रकृतित्वेन विवक्षिते पूर्वविप्रतिषेधाद् अयमेव
        इष्यते** — औपानह्यं चर्म by 5.1.14, not by 5.1.15, though
        5.1.15 names leather and stands later.
        """
        notes = unwrapped(REGISTRY.get("5.1.14").notes)
        self.assertIn("पूर्वविप्रतिषेधाद् अयमेव", notes)
        self.assertIn("औपानह्यं चर्म", notes)
        answer = fit_for("upānah", sense="tadartha", case="caturthī")
        self.assertEqual(answer.affix, "ñya")
        self.assertEqual(answer.sutra, "5.1.14")


class ARuleThatRefusesWhatItWouldOtherwiseGive(unittest.TestCase):
    """
    5.1.21's **अशते** and 5.1.7's **अनभिधानात्** — two different
    grounds for a form not existing.
    """

    def test_the_affix_is_refused_where_it_would_say_nothing_new(self):
        """
        **प्रत्ययार्थोऽत्र संघः शतमेव वस्तुतः प्रकृत्यर्थाद् न
        भिद्यते** — where the group meant IS the hundred, what the
        affix would report is what the base already says.
        """
        notes = unwrapped(REGISTRY.get("5.1.21").notes)
        self.assertIn("प्रकृत्यर्थाद् न भिद्यते", notes)
        self.assertEqual(provisions_for("5.1.21")[0].result, "aśata")

        allowed = fit_for("śata", sense="ārhīya", case="tṛtīyā",
                          result="aśata")
        self.assertEqual(allowed.affix, "ṭhan")
        self.assertEqual(allowed.also_gives, ("yat",))
        self.assertEqual(allowed.sutra, "5.1.21")

    def test_and_a_different_hundred_is_not_refused(self):
        """
        **शतप्रतिषेधेऽन्यशतत्वेऽप्रतिषेधः** — शत्यं शाटकशतम् stands,
        because **वाक्येन ह्यत्र प्रत्ययार्थस्य तत्त्वं गम्यते, न
        श्रुत्या**: the identity is got from the sentence and not
        from the word's own sound.
        """
        notes = unwrapped(REGISTRY.get("5.1.21").notes)
        self.assertIn("शतप्रतिषेधेऽन्यशतत्वेऽप्रतिषेधः", notes)
        self.assertIn("वाक्येन ह्यत्र प्रत्ययार्थस्य तत्त्वं गम्यते",
                      notes)

    def test_and_two_words_take_nothing_at_all(self):
        """
        5.1.7 names वृष and ब्रह्मन्, and yet वृष्णे हितम् and
        ब्राह्मणेभ्यो हितम् take no affix whatever — not even the
        heading's छ, **अनभिधानात्**.

        So the two words in the rule are the plant and the sacred
        word, not the bull and the priest, and the rule's own
        counter-examples say which.
        """
        notes = unwrapped(REGISTRY.get("5.1.7").notes)
        self.assertIn("अनभिधानात्", notes)
        self.assertIn("छप्रत्ययोऽपि न भवति", notes)
        self.assertIn("वृष्णे हितम्", provisions_for("5.1.7")[0].keeps_out)


class WhereTheAffixIsTakenAway(unittest.TestCase):
    """
    5.1.28 to 5.1.30 — and the removal is लुक्, so nothing of the
    affix's gender or number survives it.
    """

    def test_what_makes_a_rule_one_that_removes(self):
        """
        Every लुक् of this pāda follows a COMPOUND — अध्यर्ध before
        the base, or a द्विगु, or द्वि and त्रि. So a removing rule
        names what stands in front and gives nothing of its own.
        """
        for row in KRITA_TABLE:
            if row.lup:
                with self.subTest(sutra=row.sutra):
                    self.assertEqual(row.gives, "")
                    self.assertTrue(row.pre)
                    self.assertFalse(row.borrows)
        self.assertTrue(any(row.lup for row in KRITA_TABLE))

    def test_and_the_one_that_removes_and_gives_at_once(self):
        """
        5.1.55 कुलिजाल्लुक्खौ च is the exception to that shape: the
        elision is one of FOUR alternatives, not the whole rule.
        **अन्यतरस्यांग्रहणानुवृत्त्या लुगपि विकल्प्यते; ठञः पक्षे
        श्रवणं भवति। तेन चातूरूप्यं संपद्यते.**
        """
        row = provisions_for("5.1.55")[0]
        self.assertTrue(row.lup)
        self.assertTrue(row.optional)
        self.assertEqual(row.also_gives, ("kha", "ṣṭhan"))
        self.assertIn("चातूरूप्यं संपद्यते",
                      unwrapped(REGISTRY.get("5.1.55").notes))
        self.assertIn("त्रैरूप्यं संपद्यते",
                      unwrapped(REGISTRY.get("5.1.36").notes))

    def test_and_the_first_of_them_is_obligatory_and_the_others_not(self):
        """
        **पूर्वेण लुकि नित्ये प्राप्ते विकल्प्यते** — 5.1.28 makes
        it obligatory and the two after it turn it into a choice.
        That is what अध्यर्धकार्षापणम् beside अध्यर्धकार्षापणिकम्
        is.
        """
        self.assertFalse(provisions_for("5.1.28")[0].optional)
        for sutra in ("5.1.29", "5.1.30", "5.1.31"):
            with self.subTest(sutra=sutra):
                self.assertTrue(provisions_for(sutra)[0].optional)
                self.assertEqual(provisions_for(sutra)[0].excepts,
                                 ("5.1.28",))
        self.assertIn("पूर्वेण लुकि नित्ये प्राप्ते विकल्प्यते",
                      unwrapped(REGISTRY.get("5.1.29").notes))

    def test_and_the_removal_answers_with_no_affix(self):
        answer = fit_for(pre="dvigu", sense="ārhīya", case="tṛtīyā",
                         result="asaṃjñā")
        self.assertTrue(answer.lup)
        self.assertEqual(answer.affix, "")
        self.assertEqual(answer.sutra, "5.1.28")

    def test_and_a_name_is_kept_out_of_the_removal(self):
        """
        **असंज्ञायामिति किम्?** पाञ्चलोहितिकम् — and the word
        असंज्ञा qualifies the DERIVED form, not the base:
        **प्रत्ययान्तस्य विशेषणमसंज्ञाग्रहणम्.**
        """
        notes = unwrapped(REGISTRY.get("5.1.28").notes)
        self.assertIn("प्रत्ययान्तस्य विशेषणमसंज्ञाग्रहणम्", notes)
        self.assertEqual(provisions_for("5.1.28")[0].result,
                         "asaṃjñā")


class ARuleThatGivesNothingButAnInsert(unittest.TestCase):
    """
    5.1.23 वतोरिड्वा — the affix is already settled by 5.1.22, and
    all this rule adds is an आगम.
    """

    def test_it_names_the_affix_only_to_put_something_before_it(self):
        """
        **वत्वन्तस्य संख्यात्वात् कन् सिद्ध एव, तस्य त्वनेन वा
        इडागमो विधीयते** — तावतिकः beside तावत्कः, and the two
        differ by the insert alone.
        """
        row = provisions_for("5.1.23")[0]
        self.assertEqual(row.gives, provisions_for("5.1.22")[0].gives)
        self.assertEqual(row.augment, "iṭ")
        self.assertTrue(row.optional)
        self.assertIn("कन् सिद्ध एव",
                      unwrapped(REGISTRY.get("5.1.23").notes))

    def test_and_a_word_in_vatu_reaches_it(self):
        answer = fit_for(stem_final="vatu", sense="ārhīya",
                         case="tṛtīyā")
        self.assertEqual(answer.sutra, "5.1.23")
        self.assertEqual(answer.augment, "iṭ")
        self.assertTrue(answer.optional)

    def test_and_the_numeral_rule_excludes_two_endings(self):
        """
        **अतिशदन्ताया इति किम्?** साप्ततिकम्, चात्वारिंशत्कम् — and
        the excluded ति is the one that MEANS something, so कतिकः
        stands: **अर्थवतस्तिशब्दस्य ग्रहणाद् डतेः पर्युदासो न
        भवति.**
        """
        notes = unwrapped(REGISTRY.get("5.1.22").notes)
        self.assertIn("अर्थवतस्तिशब्दस्य ग्रहणाद्", notes)
        self.assertIn("कतिकः", notes)
        self.assertEqual(provisions_for("5.1.22")[0].of_samjna,
                         "saṃkhyā")


class AConditionThatTravelsAndOneThatDoesNot(unittest.TestCase):
    """
    5.1.20's असमासे is carried to 5.1.21 by a च and stops there —
    and the vārttika it makes inferable governs the whole heading.
    """

    def test_the_two_rules_that_forbid_a_compound(self):
        forbidding = {row.sutra for row in KRITA_TABLE
                      if row.compounded == "no"}
        self.assertEqual(forbidding, {"5.1.20", "5.1.21"})
        self.assertIn("चकारोऽसमास इत्यनुकर्षणार्थः",
                      unwrapped(REGISTRY.get("5.1.21").notes))

    def test_and_a_compound_falls_back_to_the_heading(self):
        """द्विनैष्किकम् — the ठञ् and not 5.1.20's ठक्."""
        plain = fit_for("niṣka", gana="niṣkādi", sense="ārhīya",
                        case="tṛtīyā")
        compounded = fit_for("niṣka", gana="niṣkādi", sense="ārhīya",
                             case="tṛtīyā", compounded="yes")
        self.assertEqual(plain.sutra, "5.1.20")
        self.assertEqual(compounded.sutra, "5.1.19")
        self.assertEqual(plain.affix, compounded.affix)

    def test_and_saying_it_here_tells_you_it_was_not_meant_there(self):
        """
        **निष्कादिष्वसमासग्रहणं ज्ञापकं पूर्वत्र
        तदन्ताप्रतिषेधस्य** — a ज्ञापक, and the three rules it lets
        through are named: गव्यम्/सुगव्यम् by 5.1.2, यवापूप्यम् by
        5.1.4, राजदन्त्यम् by 5.1.6.
        """
        notes = unwrapped(REGISTRY.get("5.1.20").notes)
        self.assertIn("ज्ञापकं पूर्वत्र तदन्ताप्रतिषेधस्य", notes)
        for form in ("सुगव्यम्", "यवापूप्यम्", "राजदन्त्यम्"):
            with self.subTest(form=form):
                self.assertIn(form, notes)

    def test_and_the_varttika_it_yields_is_held_where_it_can_be_reused(self):
        """
        **प्राग् वतेः संख्यापूर्वपदानां तदन्तग्रहणमलुकि** decides
        four rules of this block and reaches to 5.1.72, so it is
        held as a constant rather than restated.
        """
        self.assertIn("संख्यापूर्वपदानां", TADANTA_ALUKI)
        self.assertIn("मलुकि", TADANTA_ALUKI)
        self.assertIn(TADANTA_ALUKI,
                      unwrapped(REGISTRY.get("5.1.20").notes))

    def test_and_an_elided_base_is_out_of_its_reach(self):
        """
        **लुगन्तायास्तु प्रकृतेर्नेष्यते** — द्विशूर्पेण क्रीतम् is
        द्विशौर्पिकम् by the heading and not शौर्पम् by 5.1.26,
        because द्विशूर्पम् has already had its affix removed.
        """
        notes = unwrapped(REGISTRY.get("5.1.20").notes)
        self.assertIn("लुगन्तायास्तु प्रकृतेर्नेष्यते", notes)
        self.assertIn("द्विशौर्पिकम्", notes)


class TheRulesAreOnRecord(unittest.TestCase):
    """All 136 of the pāda, contiguous, each with a note."""

    def test_all_of_them_are_codified(self):
        have = {sutra.id.number for sutra in REGISTRY.all()
                if sutra.id.adhyaya == 5 and sutra.id.pada == 1}
        self.assertEqual(have, set(range(1, 137)))

    def test_and_every_row_names_a_sutra_the_corpus_has(self):
        from src.astadhyayi.corpus import collate

        witnesses = collate()
        for row in KRITA_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertIn(row.sutra, witnesses)

    def test_and_every_exception_points_at_a_rule_that_exists(self):
        """
        An अपवाद names what it displaces, and the target must be a
        real sūtra of this table — otherwise the record would claim
        a competition that is not there.
        """
        stated = {row.sutra for row in KRITA_TABLE}
        for row in KRITA_TABLE:
            for target in row.excepts:
                with self.subTest(sutra=row.sutra, target=target):
                    self.assertIn(target, stated)
                    self.assertNotEqual(target, row.sutra)

    def test_and_an_exception_may_point_forward(self):
        """
        An अपवाद usually displaces what stands before it, and in
        this pāda all but one do. The exception is 5.1.21, whose
        vṛtti says **कनोऽपवादः** — and कन् is given by 5.1.22, one
        sūtra LATER.

        Which is not a slip. शत is a numeral, so 5.1.22 would take
        it wherever that rule stood; an अपवाद displaces whatever
        would otherwise apply, and where it stands relative to the
        general rule does not enter into it.
        """
        forward = {
            (row.sutra, target)
            for row in KRITA_TABLE for target in row.excepts
            if int(target.rsplit(".", 1)[1])
            > int(row.sutra.rsplit(".", 1)[1])
        }
        self.assertEqual(forward, {("5.1.21", "5.1.22")})
        self.assertIn("कनोऽपवादः",
                      unwrapped(REGISTRY.get("5.1.21").notes))
        self.assertEqual(provisions_for("5.1.22")[0].gives, "kan")

    def test_and_a_heading_row_gives_an_affix_and_names_no_sense(self):
        """
        What makes a row a heading: it supplies the affix for a whole
        stretch and states no sense of its own, leaving each rule
        under it to name one.
        """
        headings = {row.sutra for row in KRITA_TABLE if row.heading}
        self.assertEqual(headings,
                         {"5.1.1", "5.1.18", "5.1.19", "5.1.78",
                          "5.1.120"})
        for row in KRITA_TABLE:
            if row.heading:
                with self.subTest(sutra=row.sutra):
                    self.assertFalse(row.of)
                    self.assertFalse(row.gana)
                    # An affix OR a condition, and 5.1.78 is the one
                    # that carries a condition instead.
                    self.assertTrue(row.gives or row.of_samjna)

        # Four of the five name no sense, since a heading normally
        # leaves each rule under it to say what it is for. 5.1.120
        # is the exception, and for the reason that makes it the
        # heading that is not displaced: it carries 5.1.119's भाव
        # down with it, so there is nothing left for the rules under
        # it to add but their own affixes.
        naming = {row.sutra for row in KRITA_TABLE
                  if row.heading and row.sense}
        self.assertEqual(naming, {"5.1.120"})



class AnAffixSavedByBeingEnjoinedWhereItIs(unittest.TestCase):
    """
    5.1.28 removes the आर्हीय affix after अध्यर्ध-compounds and
    द्विगुs. Three later rules give affixes after exactly those
    compounds — so each would be removed the instant it arrived, and
    each is kept by the same argument.
    """

    def test_the_argument_is_made_three_times_in_the_pada(self):
        """
        **विधानसामर्थ्याद् अस्य लुङ् न भवति** at 5.1.32,
        **विधानसामर्थ्याद् अनयोर्लुग् न भवति** at 5.1.54, and
        **पुनर्विधानसामर्थ्याद् … लुग् न भवति** at 5.1.57 — where
        the third saves itself not by being enjoined but by being
        enjoined AGAIN, since its case and sense were both carried
        down already.
        """
        for sutra in ("5.1.32", "5.1.54", "5.1.57"):
            with self.subTest(sutra=sutra):
                notes = unwrapped(REGISTRY.get(sutra).notes)
                self.assertIn("सामर्थ्या", notes)
                self.assertIn("लु", notes)
                self.assertFalse(provisions_for(sutra)[0].lup)

    def test_and_each_of_the_three_names_the_compound_it_survives(self):
        """
        The argument only works because the rule is given after the
        very compound 5.1.28 names. So each of the three states an
        अध्यर्ध or a द्विगु in front, exactly as 5.1.28 does.
        """
        eliser = provisions_for("5.1.28")
        fronts = {row.pre for row in eliser}
        self.assertEqual(fronts, {"adhyardha", "dvigu"})
        for sutra in ("5.1.32", "5.1.54"):
            with self.subTest(sutra=sutra):
                self.assertIn(provisions_for(sutra)[0].pre, fronts)

    def test_and_the_restated_rule_says_why_it_restates(self):
        """
        5.1.57 asks the question against itself: **समर्थविभक्तिः
        प्रत्ययार्थश्च पूर्वसूत्रादेवानुवर्तिष्यते, किमर्थं
        पुनरनयोरुपादानम्? पुनर्विधानार्थम्.**
        """
        notes = unwrapped(REGISTRY.get("5.1.57").notes)
        self.assertIn("किमर्थं पुनरनयोरुपादानम्", notes)
        self.assertIn("पुनर्विधानार्थम्", notes)
        self.assertIn("द्विषाष्टिकः", notes)


class TheVrttiCountsTheFormsItLeaves(unittest.TestCase):
    """
    Where several rules apply in alternation the Kāśikā adds them up
    — त्रैरूप्यम् at 5.1.36 and 5.1.54, चातूरूप्यम् at 5.1.55.
    """

    def test_three_forms_where_a_conjunction_keeps_the_rule_before(self):
        """
        5.1.36 gives अण् and its च keeps 5.1.35's यत्, and 5.1.35's
        other half is the heading's ठञ् removed — **तेन त्रैरूप्यं
        संपद्यते**: द्वैशाणम्, द्विशाण्यम्, द्विशाणम्.
        """
        row = provisions_for("5.1.36")[0]
        self.assertEqual(row.gives, "aṇ")
        self.assertEqual(row.also_gives, ("yat",))
        self.assertTrue(row.optional)
        self.assertEqual(provisions_for("5.1.35")[0].gives, "yat")
        self.assertIn("त्रैरूप्यं संपद्यते",
                      unwrapped(REGISTRY.get("5.1.36").notes))

    def test_and_four_where_the_elision_is_one_of_the_alternatives(self):
        """
        5.1.55's लुक् is optional, the ठञ् is heard in another half,
        and ख and ष्ठन् make the rest — **चातूरूप्यं संपद्यते**.

        The difference from 5.1.54 is exactly that: there the two
        affixes ESCAPE the elision, here the elision is one of the
        choices.
        """
        four = provisions_for("5.1.55")[0]
        three = provisions_for("5.1.54")[0]
        self.assertTrue(four.lup)
        self.assertFalse(three.lup)
        self.assertTrue(four.optional and three.optional)
        self.assertIn("चातूरूप्यं संपद्यते",
                      unwrapped(REGISTRY.get("5.1.55").notes))


class TheSameFormFromThreeDifferentRules(unittest.TestCase):
    """
    सार्वभौमः and पार्थिवः are given three times over — 5.1.41,
    5.1.42, 5.1.43 — and only the sense and the case divide them.
    """

    def test_the_three_give_the_same_two_affixes_to_the_same_two_words(self):
        for sutra in ("5.1.41", "5.1.42", "5.1.43"):
            with self.subTest(sutra=sutra):
                rows = provisions_for(sutra)
                self.assertEqual([row.gives for row in rows],
                                 ["aṇ", "añ"])
                self.assertEqual([row.of for row in rows],
                                 [("sarvabhūmi",), ("pṛthivī",)])

    def test_and_what_separates_them_is_the_sense_and_the_case(self):
        senses = {sutra: provisions_for(sutra)[0].sense
                  for sutra in ("5.1.41", "5.1.42", "5.1.43")}
        self.assertEqual(len(set(senses.values())), 3)
        self.assertEqual(provisions_for("5.1.41")[0].case, "ṣaṣṭhī")
        self.assertEqual(provisions_for("5.1.42")[0].case, "ṣaṣṭhī")
        self.assertEqual(provisions_for("5.1.43")[0].case, "saptamī")

        for sense, case, sutra in (("nimitta", "ṣaṣṭhī", "5.1.41"),
                                   ("īśvara", "ṣaṣṭhī", "5.1.42"),
                                   ("vidita", "saptamī", "5.1.43")):
            with self.subTest(sense=sense):
                answer = fit_for("sarvabhūmi", sense=sense, case=case)
                self.assertEqual(answer.sutra, sutra)
                self.assertEqual(answer.affix, "aṇ")

    def test_and_the_middle_one_restates_its_case_to_cut_the_sense(self):
        """
        5.1.42 is inside a run of genitives and says तस्य anyway.
        **षष्ठीप्रकरणे पुनः षष्ठीसमर्थविभक्तिनिर्देशः प्रत्ययार्थस्य
        निवृत्तये** — otherwise *lord* would have been read as a
        further qualification of *omen*, the way *meeting* and
        *portent* were: **अन्यथा संयोगोत्पाताविव ईश्वरोऽपि
        प्रत्ययार्थस्य निमित्तस्य विशेषणं संभाव्येत.**
        """
        notes = unwrapped(REGISTRY.get("5.1.42").notes)
        self.assertIn("प्रत्ययार्थस्य निवृत्तये", notes)
        self.assertIn("निमित्तस्य विशेषणं संभाव्येत", notes)


class TheCommentaryRefusesToChooseARoad(unittest.TestCase):
    """
    5.1.50 admits two readings of one sūtra and takes both.
    """

    def test_both_readings_are_recorded(self):
        """
        **सूत्रार्थद्वयमपि चैतद् आचार्येण शिष्याः प्रतिपादिताः।
        तदुभयमपि ग्राह्यम्** — a stem ending in भार preceded by a
        वंशादि word, OR the वंशादि words themselves when they are a
        load. वांशभारिकः and वांशिकः.
        """
        notes = unwrapped(REGISTRY.get("5.1.50").notes)
        self.assertIn("सूत्रार्थद्वयमपि", notes)
        self.assertIn("तदुभयमपि ग्राह्यम्", notes)
        self.assertIn("अपरा वृत्तिः", notes)
        for form in ("वांशभारिकः", "वांशिकः"):
            with self.subTest(form=form):
                self.assertIn(form, notes)

    def test_and_each_reading_brings_its_own_counter_examples(self):
        """
        Both readings are tested by the same two questions — भारात्
        and वंशादिभ्यः — and the answers differ: वंशं हरति for the
        first word, and व्रीहिभारं हरति against भारभूतान् व्रीहीन्
        वहति for the second.
        """
        row = provisions_for("5.1.50")[0]
        self.assertEqual(row.gana, "vaṃśādi")
        self.assertEqual(row.uttarapada, "bhāra")
        self.assertIn("वंशं हरति", row.keeps_out)
        self.assertIn("व्रीहिभारं हरति", row.keeps_out)

    def test_and_the_three_verbs_are_told_apart(self):
        """
        **हरति देशान्तरं प्रापयति चोरयति वा; वहति उत्क्षिप्य
        धारयति; आवहति उत्पादयति** — carries off or steals, holds up
        and bears, brings about.
        """
        notes = unwrapped(REGISTRY.get("5.1.50").notes)
        for gloss in ("देशान्तरं प्रापयति", "उत्क्षिप्य",
                      "उत्पादयति"):
            with self.subTest(gloss=gloss):
                self.assertIn(gloss, notes)


class TheGrammarNamesItself(unittest.TestCase):
    """
    5.1.58 gives कन् after a numeral for, among other things, a work
    of sūtras — and the vṛtti's example is this book.
    """

    def test_the_rule_that_makes_the_astadhyayi_the_astadhyayi(self):
        """
        **अष्टावध्यायाः परिमाणमस्य सूत्रस्य अष्टकं पाणिनीयम्** — a
        work of sūtras eight chapters in measure is *the eight of
        Pāṇini*. दशकं वैयाघ्रपदीयम्, त्रिकं काशकृत्स्नम्.
        """
        notes = unwrapped(REGISTRY.get("5.1.58").notes)
        self.assertIn("अष्टकं पाणिनीयम्", notes)
        self.assertIn("दशकं वैयाघ्रपदीयम्", notes)
        self.assertEqual(provisions_for("5.1.58")[0].gives, "kan")

    def test_and_a_work_of_sutras_is_not_merely_a_group(self):
        """
        **ननु चाध्यायसमूहः सूत्रसंघ एव भवति? नैतदस्ति।
        प्राणिसमूहे संघशब्दो रूढः** — *group* is settled usage for a
        collection of LIVING things, so the fourth setting is not
        already covered by the second.
        """
        notes = unwrapped(REGISTRY.get("5.1.58").notes)
        self.assertIn("प्राणिसमूहे संघशब्दो रूढः", notes)

    def test_and_the_numerals_themselves_are_laid_down_ready_made(self):
        """
        5.1.59 lays ten of them down rather than deriving them, and
        warns against reading meaning into the parts:
        **नात्रावयवार्थेऽभिनिवेष्टव्यम्.** The proof is that पङ्क्ति
        also means a plain row — पिपीलिकापङ्क्तिः, an ant's file,
        where there is no *five* whatever.
        """
        row = provisions_for("5.1.59")[0]
        self.assertEqual(row.gives, "")
        self.assertFalse(row.borrows)
        notes = unwrapped(REGISTRY.get("5.1.59").notes)
        self.assertIn("निपातनात् सिद्धम्", notes)
        self.assertIn("नात्रावयवार्थे", notes)
        self.assertIn("पिपीलिकापङ्क्तिः", notes)
        self.assertIn("उदाहरणमात्रमेतत्", notes)


class TwoUsesOfOneLocative(unittest.TestCase):
    """
    5.1.62's ब्राह्मणे — and the vṛtti distinguishes a locative that
    says what a word MEANS from one that confines a rule to a body of
    text.
    """

    def test_the_distinction_is_drawn_and_its_consequence_stated(self):
        """
        **अभिधेयसप्तम्येषा, न विषयसप्तमी। तेन मन्त्रभाषयोरपि
        भवति** — so the form occurs in mantra and in ordinary speech
        as well, which a विषयसप्तमी would have forbidden.
        """
        notes = unwrapped(REGISTRY.get("5.1.62").notes)
        self.assertIn("अभिधेयसप्तम्येषा, न विषयसप्तमी", notes)
        self.assertIn("मन्त्रभाषयोरपि", notes)

    def test_and_a_rule_that_really_is_confined_says_chandasi(self):
        """
        Four rules of the pāda are restricted to a register, and
        every one of them says छन्दसि in the sūtra itself. 5.1.62
        says ब्राह्मणे and is NOT restricted — which is the whole
        point of the distinction the vṛtti draws.
        """
        confined = {row.sutra for row in KRITA_TABLE if row.usage}
        for row in KRITA_TABLE:
            if row.usage:
                with self.subTest(sutra=row.sutra):
                    self.assertEqual(row.usage, "chandasi")
        self.assertIn("5.1.61", confined)
        self.assertNotIn("5.1.62", confined)
        self.assertEqual(provisions_for("5.1.62")[0].usage, "")
        self.assertEqual(provisions_for("5.1.62")[0].result,
                         "brāhmaṇa")


class TheHeadingReachesItsOwnWord(unittest.TestCase):
    """
    5.1.63 तदर्हति — the sūtra 5.1.19 was named from, and the one
    heading of the five that reaches its marker instead of stopping
    short of it. It does not END there; it takes it in and runs on.
    """

    def test_no_heading_anywhere_has_its_marker_for_its_last_rule(self):
        """
        छ's marker stands twenty sūtras past its last rule, ठक्'s
        two past, यत्'s two pādas past, काल's one past — and the
        आर्हीय one stands eight sūtras BEFORE its last rule, which
        is the same gap running the other way.

        The property is that the two are never the same sūtra, and
        the reason differs: a प्राक्-heading stops short because
        another heading opens inside its range, and this one runs on
        because its own sense keeps being named.
        """
        from src.astadhyayi.krita import KALA_MARKER, KALA_RUN
        from src.astadhyayi.thak import (THAK_MARKER, THAK_RUN,
                                         YAT_MARKER, YAT_RUN)

        for run, marker in ((CHA_RUN, CHA_MARKER),
                            (ARHIYA_RUN, ARHIYA_MARKER),
                            (KALA_RUN, KALA_MARKER),
                            (THAK_RUN, THAK_MARKER),
                            (YAT_RUN, YAT_MARKER)):
            with self.subTest(heading=run[0]):
                self.assertNotEqual(run[1], marker)

        # And this is the one where the marker comes FIRST.
        self.assertLess(int(ARHIYA_MARKER.rsplit(".", 1)[1]),
                        int(ARHIYA_RUN[1].rsplit(".", 1)[1]))
        self.assertGreater(int(CHA_MARKER.rsplit(".", 1)[1]),
                           int(CHA_RUN[1].rsplit(".", 1)[1]))
        self.assertTrue(REGISTRY.has(ARHIYA_MARKER))

    def test_and_the_affix_applies_at_the_marker_itself(self):
        """
        **तेनार्हत्यर्थेऽपि ठग् भवत्येव** — श्वेतच्छत्रमर्हति
        **श्वैतच्छत्रिकः**, and the ठक् that reaches it is 5.1.19's
        own, fetched through this rule's यथाविहितम्.
        """
        answer = fit_for("śvetacchatra", sense="arhati",
                         case="dvitīyā")
        self.assertEqual(answer.affix, "ṭhak")
        self.assertEqual(answer.sutra, ARHIYA_RUN[0])
        self.assertTrue(answer.borrowed)
        self.assertEqual(answer.case, "dvitīyā")

    def test_and_the_sense_it_names_is_in_the_headings_own_set(self):
        self.assertIn("arhati", ARHIYA_SENSES)
        self.assertTrue(provisions_for("5.1.63")[0].borrows)
        self.assertEqual(provisions_for("5.1.63")[0].sense, "arhati")



class TheSensesPastTheArhiyaSection(unittest.TestCase):
    """
    **अतः परं प्राग्वतीयष्ठञेव भवति** — from 5.1.72 on it is the ठञ्
    of 5.1.18 alone, so a sense named after that must not be answered
    by the ठक् of 5.1.19.
    """

    def test_the_two_sets_do_not_overlap(self):
        self.assertEqual(set(ARHIYA_SENSES) & set(LATER_SENSES),
                         set())
        self.assertEqual(set(THAN_SENSES),
                         set(ARHIYA_SENSES) | set(LATER_SENSES))
        self.assertEqual(set(CHA_SENSES) & set(THAN_SENSES), set())

    def test_and_the_later_ones_fall_back_on_the_second_heading(self):
        """
        Where no rule of the stretch is reached, an आर्हीय sense
        answers ठक् and a later one answers ठञ् — which is the
        difference 5.1.71 states.
        """
        early = fit_for("kaścit", sense="arhati", case="dvitīyā")
        late = fit_for("kaścit", sense="vartayati", case="dvitīyā")
        self.assertEqual(early.sutra, "5.1.19")
        self.assertEqual(early.affix, "ṭhak")
        self.assertEqual(late.sutra, "5.1.18")
        self.assertEqual(late.affix, "ṭhañ")

    def test_and_every_sense_a_row_names_belongs_to_one_of_the_sets(self):
        known = set(PADA_SENSES)
        for row in KRITA_TABLE:
            if row.sense:
                with self.subTest(sutra=row.sutra):
                    self.assertIn(row.sense, known)


class ThreeWordsThatAreMeasuresAndNotThings(unittest.TestCase):
    """
    पात्र, पाद and भाग each look like an everyday word and are read
    as units instead, and each time the vṛtti says so.
    """

    def test_the_three_are_each_glossed_away_from_the_obvious_sense(self):
        for sutra, phrase in (
                ("5.1.46", "पात्रशब्दः परिमाणवाची"),
                ("5.1.34", "प्राण्यङ्गस्य स इष्यते, इदं तु परिमाणम्"),
                ("5.1.49", "भागशब्दोऽपि रूपकार्धस्य वाचकः")):
            with self.subTest(sutra=sutra):
                self.assertIn(phrase,
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_the_measure_reading_keeps_a_rule_away(self):
        """
        6.3.53 पद्यत्यतदर्थे would turn पाद into पद् before this
        very affix. It does not, and the reason is the reading:
        अध्यर्धपाद्यम् and not अध्यर्धपद्यम्.
        """
        self.assertIn("अध्यर्धपद्यम्",
                      provisions_for("5.1.34")[0].keeps_out)
        self.assertIn("अध्यर्धपाद्यम्",
                      unwrapped(REGISTRY.get("5.1.34").notes))

    def test_and_the_same_word_is_a_measure_twice_over(self):
        """
        पात्र is read as a measure at 5.1.46 and again at 5.1.68,
        forty rules and two senses apart — **पात्रं परिमाणमप्यस्ति**.
        """
        self.assertIn("पात्रं परिमाणमप्यस्ति",
                      unwrapped(REGISTRY.get("5.1.68").notes))
        self.assertEqual(provisions_for("5.1.46")[0].of, ("pātra",))
        self.assertEqual(provisions_for("5.1.68")[0].of, ("pātra",))


class WhatTheWordNityaQualifies(unittest.TestCase):
    """
    5.1.64 and 5.1.76 both say नित्यम्, and both vṛttis say the same
    thing about it: **नित्यग्रहणं प्रत्ययार्थविशेषणम्** — it
    qualifies what the AFFIX REPORTS, not how often the rule applies.
    """

    def test_the_gloss_is_given_at_both_places(self):
        for sutra in ("5.1.64", "5.1.76"):
            with self.subTest(sutra=sutra):
                self.assertIn("नित्यग्रहणं प्रत्ययार्थविशेषणम्",
                              unwrapped(REGISTRY.get(sutra).notes))
                self.assertEqual(provisions_for(sutra)[0].result,
                                 "nitya")

    def test_and_it_lapses_where_the_next_rule_says_so(self):
        """
        **नित्यमिति निवृत्तम्** at 5.1.66 — so the word governs
        exactly two rules and the third drops it.
        """
        self.assertIn("नित्यमिति निवृत्तम्",
                      unwrapped(REGISTRY.get("5.1.66").notes))
        self.assertEqual(provisions_for("5.1.66")[0].result, "")

    def test_and_the_second_of_them_answers_a_different_rule(self):
        """
        पथिकः by 5.1.75 where the going is occasional, पान्थः by
        5.1.76 where it is constant — and the second substitutes the
        base's shape in the same act. **नित्यमिति किम्? पथिकः.**
        """
        occasional = fit_for("pathin", sense="gacchati",
                             case="dvitīyā")
        constant = fit_for("pathin", sense="gacchati",
                           case="dvitīyā", result="nitya")
        self.assertEqual(occasional.sutra, "5.1.75")
        self.assertEqual(constant.sutra, "5.1.76")
        self.assertEqual(constant.adesa, "panthan")
        self.assertEqual(occasional.adesa, "")
        self.assertIn("पथिकः", provisions_for("5.1.76")[0].keeps_out)


class AnOptionThatHardensWhereTheThingHasAMind(unittest.TestCase):
    """
    5.1.88 makes the elision one of three choices; 5.1.89 makes it
    obligatory where what is meant is a living thing.
    """

    def test_the_later_rule_removes_the_choice_the_earlier_gave(self):
        """
        **पूर्वेण विकल्पे प्राप्ते वचनम्** — द्विवर्षो दारकः, a
        two-year-old child, against द्विवर्षीणो व्याधिः, where an
        illness has no mind and keeps all three forms.
        """
        loose = provisions_for("5.1.88")[0]
        fixed = provisions_for("5.1.89")[0]
        self.assertTrue(loose.optional)
        self.assertFalse(fixed.optional)
        self.assertTrue(fixed.lup)
        self.assertEqual(fixed.excepts, ("5.1.88",))
        self.assertEqual(fixed.result, "cittavat")
        self.assertIn("पूर्वेण विकल्पे प्राप्ते वचनम्",
                      unwrapped(REGISTRY.get("5.1.89").notes))

    def test_and_the_counter_example_is_the_one_without_a_mind(self):
        self.assertIn("द्विवर्षीणो व्याधिः",
                      provisions_for("5.1.89")[0].keeps_out)
        answer = fit_for(uttarapada="varṣa", pre="dvigu",
                         samjna="kāla", sense="nirvṛttādi",
                         case="dvitīyā", result="cittavat")
        self.assertTrue(answer.lup)
        self.assertEqual(answer.sutra, "5.1.89")


class OneWordThatFreesARuleFromItsHeading(unittest.TestCase):
    """
    5.1.95 stands under कालात् and is about sacrifices, not times.
    The word आख्या is what gets it out.
    """

    def test_the_vrtti_says_what_the_word_is_for(self):
        """
        **आख्याग्रहणम् अकालादपि यज्ञवाचिनो यथा स्यादिति। इतरथा हि
        कालाधिकाराद् एकाहद्वादशाहप्रभृतय एव यज्ञा गृह्येरन्** —
        without it only sacrifices NAMED FROM their length would
        have been reached.
        """
        notes = unwrapped(REGISTRY.get("5.1.95").notes)
        self.assertIn("आख्याग्रहणम्", notes)
        self.assertIn("एकाहद्वादशाहप्रभृतय एव यज्ञा गृह्येरन्",
                      notes)

    def test_and_the_row_records_the_class_and_not_the_time(self):
        row = provisions_for("5.1.95")[0]
        self.assertEqual(row.of_samjna, "yajña-ākhyā")
        self.assertNotEqual(row.of_samjna, "kāla")
        answer = fit_for(samjna="yajña-ākhyā", sense="dakṣiṇā",
                         case="ṣaṣṭhī")
        self.assertEqual(answer.sutra, "5.1.95")
        self.assertEqual(answer.affix, "ṭhañ")


class TheCommentaryRefusesToChooseASecondTime(unittest.TestCase):
    """
    5.1.50 kept two readings of a sūtra; 5.1.94 does it again, and
    this time the two readings put the base in different cases.
    """

    def test_both_readings_are_recorded_and_both_are_authoritative(self):
        """
        **पूर्वत्र ब्रह्मचारी प्रत्ययार्थः, उत्तरत्र ब्रह्मचर्यमेव।
        उभयमपि प्रमाणम्, उभयथा सूत्रप्रणयनात्** — on one reading the
        derived word names the STUDENT, on the other the STUDY.
        """
        notes = unwrapped(REGISTRY.get("5.1.94").notes)
        self.assertIn("अपरा वृत्तिः", notes)
        self.assertIn("उभयमपि प्रमाणम्", notes)
        self.assertIn("मासिको ब्रह्मचारी", notes)
        self.assertIn("मासिकं ब्रह्मचर्यम्", notes)

    def test_and_the_two_places_use_the_same_phrase(self):
        """
        Both vṛttis introduce the second reading with **अपरा
        वृत्तिः**, and both refuse to decide.
        """
        for sutra in ("5.1.50", "5.1.94"):
            with self.subTest(sutra=sutra):
                self.assertIn("अपरा वृत्तिः",
                              unwrapped(REGISTRY.get(sutra).notes))



class SixHeadingsAndNotOneEndsWhereItPoints(unittest.TestCase):
    """
    **ठञः पूर्णोऽवधिः** at 5.1.114 — after 4.4.74 of ठक्, 4.4.144 of
    यत्, 5.1.17 of छ and यत् together, 5.1.71 of the आर्हीय ठक्, and
    5.1.96 of काल. Six headings, six closings, six gaps.
    """

    def test_the_second_heading_of_this_pada_closes_one_short(self):
        """
        The narrowest gap of the six, and the plainest reason:
        5.1.115 gives वति itself, so the heading named from that
        word cannot reach the rule that gives it.
        """
        from src.astadhyayi.krita import THAN_RUN

        self.assertEqual(THAN_RUN, ("5.1.18", "5.1.114"))
        self.assertEqual(THAN_MARKER, "5.1.115")
        self.assertEqual(int(THAN_RUN[1].rsplit(".", 1)[1]) + 1,
                         int(THAN_MARKER.rsplit(".", 1)[1]))
        self.assertIn("ठञः पूर्णोऽवधिः",
                      unwrapped(REGISTRY.get("5.1.114").notes))
        self.assertIn(THAN_MARKER, than_run().why)

    def test_and_the_formula_appears_at_all_six(self):
        """
        Not a count of the headings but the property that makes them
        one kind of thing: each closing rule says the limit is
        complete, and each names what takes over.
        """
        for sutra in ("4.4.74", "4.4.144", "5.1.17", "5.1.71",
                      "5.1.96", "5.1.114"):
            with self.subTest(sutra=sutra):
                self.assertIn("पूर्णोऽवधिः",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_every_heading_range_ends_at_a_rule_that_says_so(self):
        """
        The ranges are not asserted from the sūtra numbering: each
        one ends where a vṛtti closes it, and the test reads the
        closing off the rule the range names.
        """
        from src.astadhyayi.krita import (ARHIYA_RUN, KALA_RUN,
                                          THAN_RUN)
        from src.astadhyayi.thak import THAK_RUN, YAT_RUN

        for run in (CHA_RUN, THAN_RUN, ARHIYA_RUN, KALA_RUN,
                    THAK_RUN, YAT_RUN):
            with self.subTest(heading=run[0]):
                self.assertTrue(REGISTRY.has(run[1]))
                self.assertIn("पूर्णोऽवधिः",
                              unwrapped(REGISTRY.get(run[1]).notes))


class ARuleStatedOnlyToNarrowWhatWasAlreadyDue(unittest.TestCase):
    """
    5.1.113 ऐकागारिकट् — the affix was coming anyway from 5.1.109,
    and the rule exists to shut a case out.
    """

    def test_the_vrtti_asks_why_the_rule_is_there_and_answers(self):
        """
        **किमर्थमिदं निपात्यते, यावता प्रयोजनमित्येव सिद्धष्ठञ्?
        चौरे नियमार्थं वचनम्** — so that **एकागारं प्रयोजनमस्य
        भिक्षोः** does not get the word. A रूढि fixed by a rule.
        """
        notes = unwrapped(REGISTRY.get("5.1.113").notes)
        self.assertIn("चौरे नियमार्थं वचनम्", notes)
        self.assertIn("भिक्षोरिति", notes)
        self.assertEqual(provisions_for("5.1.113")[0].result, "caura")
        self.assertIn("भिक्षुः",
                      provisions_for("5.1.113")[0].keeps_out)

    def test_and_the_rule_it_narrows_gives_the_same_affix_class(self):
        """
        5.1.109 gives ठञ् for *its occasion*; 5.1.113 lays down a
        form for one particular occasion. The narrowing is real
        only because the wider rule reaches the same base.
        """
        wide = fit_for("kaścit", sense="prayojana", case="prathamā")
        narrow = fit_for("ekāgāra", sense="prayojana",
                         case="prathamā", result="caura")
        self.assertEqual(wide.sutra, "5.1.109")
        self.assertEqual(narrow.sutra, "5.1.113")
        self.assertNotEqual(wide.affix, narrow.affix)

    def test_and_another_rule_is_fixed_by_usage_instead(self):
        """
        5.1.103's कार्मुकम् is used of a bow and of nothing else —
        and no word in the rule says so. **धनुषोऽन्यत्र न भवति,
        अनभिधानात्**: the limit is in the language, not the sūtra.

        Two ways of narrowing, one sūtra apart in kind: 5.1.113
        states the restriction, 5.1.103 leaves it to usage.
        """
        notes = unwrapped(REGISTRY.get("5.1.103").notes)
        self.assertIn("धनुषोऽन्यत्र न भवति, अनभिधानात्", notes)
        self.assertEqual(provisions_for("5.1.103")[0].result,
                         "dhanus")


class TwoAffixesTheVrttiRefusesToPairOff(unittest.TestCase):
    """
    यथासंख्यम् matches affixes to bases in order — except where the
    vṛtti says it does not, and this pāda says so twice.
    """

    def test_at_5_1_98_the_pairing_is_refused_outright(self):
        """
        **दीयते कार्यमित्येतयोरर्थयोः प्रत्येकम् अभिसंबन्धः,
        यथासंख्यं नेष्यते** — each affix with each sense.
        """
        notes = unwrapped(REGISTRY.get("5.1.98").notes)
        self.assertIn("यथासंख्यं नेष्यते", notes)
        row = provisions_for("5.1.98")[0]
        self.assertEqual(row.of, ("yathākathāca", "hasta"))
        self.assertEqual(row.gives, "ṇa")
        self.assertEqual(row.also_gives, ("yat",))

    def test_and_at_5_1_69_it_is_refused_by_a_hint(self):
        """
        There the refusal is inferred from the ORDER of the words:
        **दक्षिणाशब्दस्याल्पाच्तरस्यापूर्वनिपातेन
        लक्षणव्यभिचारचिह्नेन यथासंख्याभावं सूचयति** — the shorter
        word should have come first, and its not doing so is the
        breach that signals the point.
        """
        self.assertIn("यथासंख्याभावं सूचयति",
                      unwrapped(REGISTRY.get("5.1.69").notes))

    def test_and_where_it_holds_the_rows_are_written_apart(self):
        """
        Where यथासंख्यम् does hold, one sūtra states two rows, each
        with its own base and its own affix — 5.1.10, 5.1.41,
        5.1.51, 5.1.71.
        """
        for sutra in ("5.1.10", "5.1.41", "5.1.51", "5.1.71"):
            with self.subTest(sutra=sutra):
                rows = provisions_for(sutra)
                self.assertEqual(len(rows), 2)
                self.assertNotEqual(rows[0].gives, rows[1].gives)
                self.assertNotEqual(rows[0].of, rows[1].of)


class AWholeRuleForOneWordMeaningMomentary(unittest.TestCase):
    """
    5.1.114 आकालिकड् — an affix, a substitution and a sense, all
    laid down together for a word the vṛtti has to explain twice.
    """

    def test_the_rule_does_three_things_at_once(self):
        """
        **समानकालशब्दस्य आकालशब्द आदेशः** and **इकट् प्रत्ययश्च
        निपात्यते**, and **आद्यन्तयोश्चैतद् विशेषणम्** — the sense
        qualifies the beginning and the end together.
        """
        row = provisions_for("5.1.114")[0]
        self.assertEqual(row.gives, "ikaṭ")
        self.assertEqual(row.adesa, "ākāla")
        self.assertEqual(row.of, ("samānakāla",))
        self.assertEqual(row.sense, "ādyanta")

    def test_and_the_gloss_is_what_the_word_actually_means(self):
        """
        **जन्मना तुल्यकालविनाशा; उत्पादानन्तरं विनाशिनी इत्यर्थः** —
        whose ending is of one time with its beginning, perishing
        the instant it arises. The vṛtti's example is lightning.
        """
        notes = unwrapped(REGISTRY.get("5.1.114").notes)
        self.assertIn("जन्मना तुल्यकालविनाशा", notes)
        self.assertIn("उत्पादानन्तरं विनाशिनी", notes)
        self.assertIn("आकालिकी विद्युत्", notes)

    def test_and_a_varttika_adds_two_more_affixes_to_it(self):
        """**आकालाट् ठंश्च; चात् ठञ् च** — three in all."""
        row = provisions_for("5.1.114")[0]
        self.assertEqual(row.also_gives, ("ṭhan", "ṭhañ"))
        self.assertIn("आकालाट् ठंश्च",
                      unwrapped(REGISTRY.get("5.1.114").notes))



class OneAffixForFourRelations(unittest.TestCase):
    """
    वति from 5.1.115 to 5.1.118 — likeness, comparison, desert, and
    a preverb's own sense, all with one affix.
    """

    def test_the_four_senses_are_served_by_the_same_affix(self):
        for sense in VATI_SENSES:
            rows = [row for row in KRITA_TABLE if row.sense == sense]
            with self.subTest(sense=sense):
                self.assertTrue(rows)
                for row in rows:
                    self.assertEqual(row.gives, "vati")

    def test_and_the_cases_differ_where_the_senses_do(self):
        """
        तृतीया for a likeness of action, सप्तमी and षष्ठी together
        for *as there* and *as his*, द्वितीया for desert — and
        5.1.118 names no case at all, since a preverb has none.
        """
        self.assertEqual(provisions_for("5.1.115")[0].case, "tṛtīyā")
        self.assertEqual({row.case for row in provisions_for("5.1.116")},
                         {"saptamī", "ṣaṣṭhī"})
        self.assertEqual(provisions_for("5.1.117")[0].case, "dvitīyā")
        self.assertEqual(provisions_for("5.1.118")[0].case, "")

    def test_and_the_first_of_them_wants_an_action_and_says_so(self):
        """
        **क्रियाग्रहणं किम्? गुणद्रव्यतुल्ये मा भूत्** — पुत्रेण
        तुल्यः स्थूलः takes nothing, the likeness being of a
        quality.
        """
        self.assertEqual(provisions_for("5.1.115")[0].result,
                         "kriyā")
        self.assertIn("गुणद्रव्यतुल्ये मा भूत्",
                      unwrapped(REGISTRY.get("5.1.115").notes))
        self.assertIn("पुत्रेण तुल्यः स्थूलः",
                      provisions_for("5.1.115")[0].keeps_out)


class AHeadingThatStandsBesideItsExceptions(unittest.TestCase):
    """
    5.1.120 आ च त्वात् — and this is the one heading of the seven
    that is NOT displaced by the rules under it.
    """

    def test_the_vrtti_says_that_is_why_the_rule_exists(self):
        """
        **अपवादैः सह समावेशार्थं वचनम्** — stated so that त्व and
        तल् come TOGETHER WITH what would otherwise displace them,
        and **त्वतलौ सर्वत्र भवत एव**.
        """
        notes = unwrapped(REGISTRY.get("5.1.120").notes)
        self.assertIn("अपवादैः सह समावेशार्थं वचनम्", notes)
        self.assertIn("त्वतलौ सर्वत्र भवत एव",
                      unwrapped(REGISTRY.get("5.1.122").notes))
        self.assertTrue(provisions_for("5.1.120")[0].heading)

    def test_and_four_forms_stand_where_one_rule_would_give_one(self):
        """
        प्रथिमा by 5.1.122, पार्थवम् by the general अण्, and
        पृथुत्वम् and पृथुता by the heading — and the option in
        5.1.122 is for that: **वावचनम् अणादेः समावेशार्थम्**.
        """
        special = fit_for("pṛthu", gana="pṛthvādi", sense="bhāva",
                          case="ṣaṣṭhī")
        self.assertEqual(special.affix, "imanic")
        self.assertTrue(special.optional)
        self.assertIn("वावचनम् अणादेः समावेशार्थम्",
                      unwrapped(REGISTRY.get("5.1.122").notes))

        plain = fit_for("aśva", sense="bhāva", case="ṣaṣṭhī")
        self.assertEqual(plain.affix, "tva")
        self.assertEqual(plain.also_gives, ("tal",))

    def test_and_its_marker_and_last_rule_are_the_same_sutra(self):
        """
        The only heading of the seven where they coincide — and
        because nothing follows: 5.1.136 ends the pāda, so there is
        no room for another heading to open inside the range or for
        the sense to run on past the marker.
        """
        from src.astadhyayi.krita import TVA_MARKER, TVA_RUN, tva_run

        self.assertEqual(TVA_RUN, ("5.1.120", "5.1.136"))
        self.assertEqual(TVA_MARKER, TVA_RUN[1])
        self.assertEqual(tva_run().affix, "tva")
        self.assertEqual(tva_run().also_gives, ("tal",))

        last = max(int(row.sutra.rsplit(".", 1)[1])
                   for row in KRITA_TABLE)
        self.assertEqual(int(TVA_RUN[1].rsplit(".", 1)[1]), last)


class ThePadaHasOneRefusal(unittest.TestCase):
    """
    5.1.121, and it refuses the special affixes while leaving the
    heading's two standing.
    """

    def test_the_answer_names_what_supplies_and_records_the_refusal(self):
        """
        A प्रतिषेध does not govern what it excepts. अपतित्वम् and
        अपतिता come by 5.1.119, and 5.1.121 is what kept the rest
        away.
        """
        answer = fit_for("apati", pre="nañ", sense="bhāva",
                         case="ṣaṣṭhī")
        self.assertEqual(answer.affix, "tva")
        self.assertEqual(answer.also_gives, ("tal",))
        self.assertEqual(answer.sutra, "5.1.119")
        self.assertEqual(answer.blocked_by, "5.1.121")

    def test_and_it_is_the_only_one(self):
        refusing = {row.sutra for row in KRITA_TABLE if row.refuses}
        self.assertEqual(refusing, {"5.1.121"})
        self.assertEqual(provisions_for("5.1.121")[0].gives, "")

    def test_and_each_of_its_three_conditions_has_a_counter_example(self):
        """
        **नञ्पूर्वादिति किम्?** बार्हस्पत्यम् — no negative.
        **तत्पुरुषादिति किम्?** आपटवम् — a बहुव्रीहि.
        **अचतुरादिभ्य इति किम्?** आलस्यम् — one of the eight
        excepted words.
        """
        notes = unwrapped(REGISTRY.get("5.1.121").notes)
        for question in ("नञ्पूर्वादिति किम्",
                         "तत्पुरुषादिति किम्",
                         "अचतुरादिभ्य इति किम्"):
            with self.subTest(question=question):
                self.assertIn(question, notes)
        self.assertEqual(len(provisions_for("5.1.121")[0].excludes),
                         8)


class AnAffixNamedWhereARefusalWouldHaveDone(unittest.TestCase):
    """
    5.1.136 ends the pāda, and it ends it on a point of technique.
    """

    def test_naming_the_affix_shuts_out_one_a_refusal_would_leave(self):
        """
        **नेति वक्तव्ये त्ववचनं तलो बाधनार्थम्** — the rule could
        have said *not छ*, and 5.1.119's त्व would have come anyway;
        but so would its तल्. Naming त्व leaves one affix where a
        प्रतिषेध would have left two.
        """
        notes = unwrapped(REGISTRY.get("5.1.136").notes)
        self.assertIn("नेति वक्तव्ये त्ववचनं तलो बाधनार्थम्", notes)

        officiant = fit_for("brahman", samjna="hotrā",
                            sense="bhāva-karman", case="ṣaṣṭhī")
        self.assertEqual(officiant.affix, "tva")
        self.assertEqual(officiant.also_gives, ())
        self.assertEqual(officiant.sutra, "5.1.136")

    def test_and_the_ordinary_word_keeps_both(self):
        """
        **यस्तु जातिशब्दो ब्राह्मणपर्यायो ब्रह्मन्शब्दः, ततस्
        त्वतलौ भवत एव** — ब्रह्मत्वम् AND ब्रह्मता, where the word
        is not the officiant's title.
        """
        ordinary = fit_for("brahman", sense="bhāva", case="ṣaṣṭhī")
        self.assertEqual(ordinary.also_gives, ("tal",))
        self.assertNotEqual(ordinary.sutra, "5.1.136")
        self.assertIn("ततस्त्वतलौ भवत एव",
                      unwrapped(REGISTRY.get("5.1.136").notes))

    def test_and_the_colophon_closes_the_pada(self):
        notes = unwrapped(REGISTRY.get("5.1.136").notes)
        self.assertIn("पञ्चमाध्यायस्य प्रथमः पादः", notes)
        self.assertIn("भवनावधिकयोर्नञ्स्नञोरधिकारः समाप्तः", notes)


class SevenHeadingsInOnePada(unittest.TestCase):
    """
    छ, ठञ्, ठक्, काल, वति's stretch, त्व — the densest concentration
    of headings anywhere in the grammar, and no two of the same kind.
    """

    def test_each_heading_is_bounded_in_its_own_way(self):
        """
        Three by प्राक् and stopping short; one by आ and taking its
        marker in; one carrying a condition and no affix; one
        standing beside its exceptions instead of being beaten.
        """
        from src.astadhyayi.krita import (ARHIYA_RUN, KALA_RUN,
                                          THAN_RUN, TVA_RUN)

        headings = {row.sutra for row in KRITA_TABLE if row.heading}
        self.assertEqual(headings,
                         {"5.1.1", "5.1.18", "5.1.19", "5.1.78",
                          "5.1.120"})

        # A heading supplies an affix, or a condition, or both.
        for sutra in headings:
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                self.assertTrue(row.gives or row.of_samjna)
                # 5.1.120 alone names a sense, carrying 5.1.119's
                # भाव down — which is why it is also the one
                # heading its exceptions do not displace.
                if row.sense:
                    self.assertEqual(row.sutra, "5.1.120")

        # And each range lies inside the pāda and ends at a rule.
        for run in (CHA_RUN, THAN_RUN, ARHIYA_RUN, KALA_RUN,
                    TVA_RUN):
            with self.subTest(heading=run[0]):
                self.assertTrue(REGISTRY.has(run[0]))
                self.assertTrue(REGISTRY.has(run[1]))
                self.assertLessEqual(
                    int(run[0].rsplit(".", 1)[1]),
                    int(run[1].rsplit(".", 1)[1]))

    def test_and_the_nested_ones_really_do_nest(self):
        """
        ठक् and काल both lie wholly inside ठञ्, and ठक् is enjoined
        as its exception while काल merely conditions it.
        """
        from src.astadhyayi.krita import (ARHIYA_RUN, KALA_RUN,
                                          THAN_RUN)

        outer = (int(THAN_RUN[0].rsplit(".", 1)[1]),
                 int(THAN_RUN[1].rsplit(".", 1)[1]))
        for inner in (ARHIYA_RUN, KALA_RUN):
            with self.subTest(inner=inner[0]):
                lo = int(inner[0].rsplit(".", 1)[1])
                hi = int(inner[1].rsplit(".", 1)[1])
                self.assertGreaterEqual(lo, outer[0])
                self.assertLessEqual(hi, outer[1])

        self.assertEqual(provisions_for("5.1.19")[0].excepts,
                         ("5.1.18",))
        self.assertEqual(provisions_for("5.1.78")[0].excepts, ())


if __name__ == "__main__":
    unittest.main()
