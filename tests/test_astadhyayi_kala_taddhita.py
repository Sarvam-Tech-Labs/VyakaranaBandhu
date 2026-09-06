# -*- coding: utf-8 -*-
"""
४.३.१–३० — the affixes of TIME, and then the senses come back.

4.2 spent its last fifty-three rules handing out affixes by naming
only their bases, and its vṛtti promised the meanings would follow.
This file tests that the promise is kept where the commentary says it
is kept, and that the code keeps it the way the commentary says —
by asking the earlier rules rather than by repeating their answers.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.sutra import REGISTRY
from tests import unwrapped


class AHeadingRecordedAsOverFromOutsideItself(unittest.TestCase):
    """
    4.3.1's first three words, before it says anything about its own
    rule: **देशाधिकारो निवृत्तः**.

    Every range this project has recorded so far was bounded by the
    vṛtti of the rule that OPENED it, saying in advance where it would
    stop. This one is closed from outside, by the text that comes
    after — a different kind of evidence, and one that can be checked
    against the range the other module holds.
    """

    def test_the_statement_is_on_record(self):
        self.assertIn("देशाधिकारो निवृत्तः",
                      unwrapped(REGISTRY.get("4.3.1").notes))

    def test_and_it_agrees_with_the_range_the_other_pada_holds(self):
        from src.astadhyayi.kala_taddhita import desa_lapsed
        from src.astadhyayi.sense_taddhita import DESA_RUN

        said = desa_lapsed()
        self.assertEqual(said.by, "4.3.1")
        self.assertIn(DESA_RUN[0], said.why)
        self.assertIn(DESA_RUN[1], said.why)

    def test_and_the_rule_that_closes_it_is_the_one_before_this(self):
        """
        The heading's last rule and this pāda's first are neighbours.
        If they were not, one of the two claims would be wrong.
        """
        from src.astadhyayi.sense_taddhita import DESA_RUN

        self.assertEqual(DESA_RUN[1], "4.2.145")
        self.assertTrue(REGISTRY.has("4.2.145"))
        self.assertTrue(REGISTRY.has("4.3.1"))

    def test_and_no_rule_of_this_pada_carries_the_heading(self):
        """
        The claim has a consequence in the table: nothing here may be
        conditioned on the base naming a country.

        Asked of the whole field and not as a substring, because
        **एकदेश is not देश**. 4.3.7 is stated of a ग्रामैकदेश, one
        PART of a village, and the three syllables it shares with the
        lapsed heading mean something else entirely. A substring test
        called that a country and was wrong.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        for row in KALA_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertNotIn("deśa", row.of_samjna.split("-"))
                self.assertFalse(getattr(row, "desa", False))

    def test_and_the_syllables_survive_where_the_heading_does_not(self):
        """
        The collision is worth stating rather than stepping around.
        4.3.7's एकदेश and 4.2.119's देश are written the same and are
        not the same word, and nothing but the meaning separates them.

        Asked for as जनपदैकदेश, because in the rule the word stands
        in a compound and the sandhi swallows its first vowel — पद +
        एकदेश is पदैकदेश, and a search for एकदेश finds nothing.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        part = provisions_for("4.3.7")[0]
        self.assertIn("deśa", part.of_samjna)
        self.assertIn("ekadeśa", part.of_samjna)
        self.assertIn("जनपदैकदेश", unwrapped(REGISTRY.get("4.3.7").notes))


class YathasankhyaFailsWhenTheNumbersDoNotMatch(unittest.TestCase):
    """
    4.3.1 gives three affixes and names two bases. **वैषम्याद्
    यथासंख्यं न भवति** — 1.3.10's matching-in-order cannot run over
    unequal counts, so each base takes all three.
    """

    def test_the_argument_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.1").notes)
        self.assertIn("वैषम्याद् यथासंख्यं न भवति", notes)
        self.assertIn("तदेते त्रयः प्रत्यया भवन्ति", notes)

    def test_and_the_counts_really_are_unequal(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        row = provisions_for("4.3.1")[0]
        self.assertEqual(len(row.of), 2)
        self.assertEqual(len((row.gives,) + row.also_gives), 3)

    def test_and_the_rule_that_would_have_matched_them_exists(self):
        self.assertTrue(REGISTRY.has("1.3.10"))

    def test_and_the_pada_before_had_them_equal(self):
        """
        4.2.80 paired seventeen affixes with seventeen lists and the
        matching ran. The contrast is what makes this rule's failure
        worth stating.
        """
        self.assertIn("सप्तदश", unwrapped(REGISTRY.get("4.2.80").notes))


class APronounPickingOutOneOfTwoAffixes(unittest.TestCase):
    """
    4.3.2's तस्मिन्. **साक्षाद् विहितः खञ् निर्दिश्यते, न
    चकारानुकृष्टश्छः** — *that* reaches the affix the previous rule
    ENJOINED, not the one its च dragged in.

    Which is exactly why the table keeps `gives` and `also_gives`
    apart. If the three affixes of 4.3.1 sat in one field there would
    be nothing for this rule's demonstrative to pick out.
    """

    def test_the_distinction_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.2").notes)
        self.assertIn("साक्षाद् विहितः खञ् निर्दिश्यते", notes)
        self.assertIn("न चकारानुकृष्टश्छः", notes)

    def test_and_the_table_draws_it_the_same_way(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        earlier = provisions_for("4.3.1")[0]
        self.assertEqual(earlier.gives, "khañ")
        self.assertIn("cha", earlier.also_gives)

        for row in provisions_for("4.3.2"):
            with self.subTest(replaces=row.replaces):
                self.assertEqual(row.before, "khañ")

    def test_and_the_substitution_does_not_happen_before_the_other(self):
        """
        युष्मदीयः is the counter-example: there the छ came instead,
        and no substitute with it.
        """
        from src.astadhyayi.kala_taddhita import born_in

        picked = born_in("yuṣmad", sense="śeṣa", before="khañ")
        self.assertEqual(picked.by, "4.3.2")
        self.assertEqual(picked.replaces, "yuṣmāka")

        loose = born_in("yuṣmad", sense="śeṣa")
        self.assertEqual(loose.by, "4.3.1")
        self.assertEqual(loose.replaces, "")

    def test_and_the_rule_gives_no_affix_of_its_own(self):
        from src.astadhyayi.kala_taddhita import born_in, provisions_for

        for row in provisions_for("4.3.2"):
            with self.subTest(replaces=row.replaces):
                self.assertEqual(row.gives, "")
        self.assertEqual(born_in("asmad", sense="śeṣa",
                                 before="khañ").gives, "")


class ATechnicalTermReadUntechnically(unittest.TestCase):
    """
    4.3.3's एकवचने. 1.1.63 forbids treating an elided affix as still
    present, so the base cannot be *followed by a singular* at all —
    and the answer is that एकवचन here is not the grammar's name for
    an ending but the two words read for what they mean.
    """

    def test_the_objection_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.3").notes)
        self.assertIn("न लुमताङ्गस्य", notes)
        self.assertIn("प्रत्ययलक्षणप्रतिषेधाद्", notes)

    def test_and_both_answers_are_recorded(self):
        notes = unwrapped(REGISTRY.get("4.3.3").notes)
        self.assertIn("वचनात् प्रत्ययलक्षणं भविष्यति", notes)
        self.assertIn("नैवेदं प्रत्ययग्रहणम्", notes)
        self.assertIn("अन्वर्थग्रहणम्", notes)

    def test_and_both_rules_the_argument_turns_on_are_codified(self):
        """
        1.1.63 is the paribhāṣā raising the objection and 1.4.102 is
        what gave एकवचन its technical sense. Neither claim can be
        checked without the other rule being in the registry.
        """
        for sutra in ("1.1.63", "1.4.102"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))


class TheKalaHeadingWithBothEndsStated(unittest.TestCase):
    """
    4.3.11's vṛtti: **तत्र जातः इति प्रागतः कालाधिकारः** — काल
    carries up to 4.3.25 and not into it. The eighth range in two
    pādas with both ends written down.
    """

    def test_the_range_is_named(self):
        from src.astadhyayi.kala_taddhita import KALA_RUN, kala_run

        self.assertEqual(KALA_RUN, ("4.3.11", "4.3.24"))
        self.assertEqual(kala_run().by, "4.3.11")
        self.assertIn("4.3.24", kala_run().why)

    def test_and_the_opening_rule_says_where_it_stops(self):
        self.assertIn("तत्र जातः इति प्रागतः कालाधिकारः",
                      unwrapped(REGISTRY.get("4.3.11").notes))

    def test_the_boundary_is_visible_in_the_senses(self):
        """
        Everything inside the range is still शेष, carried from
        4.2.92; the rule the range stops before opens जात. If a row
        of the table disagreed, the boundary would be decorative.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        for row in KALA_TABLE:
            number = int(row.sutra.rsplit(".", 1)[1])
            with self.subTest(sutra=row.sutra):
                if number <= 24:
                    self.assertEqual(row.sense, "śeṣa")
                else:
                    self.assertNotEqual(row.sense, "śeṣa")

    def test_and_the_senses_named_after_it_are_named_one_by_one(self):
        """
        Past the boundary the pāda stops carrying शेष and starts
        naming a sense per rule. जात first, then eight more.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        named = {row.sense for row in KALA_TABLE
                 if int(row.sutra.rsplit(".", 1)[1]) > 24}
        self.assertIn("jāta", named)
        self.assertGreaterEqual(len(named), 8)
        self.assertNotIn("śeṣa", named)

    def test_and_the_sense_it_carries_was_opened_two_pada_back(self):
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertTrue(REGISTRY.has("4.2.92"))
        self.assertEqual(provisions_for("4.2.92")[0].sense, "śeṣa")


class ThePromiseKeptFiftyEightSutrasLater(unittest.TestCase):
    """
    4.2.93's vṛtti said the senses and the cases would be stated
    later — **पुरस्ताद् वक्ष्यन्ते**. 4.3.25 says they are being
    stated now — **निर्दिश्यन्ते** — and names no affix, because
    यथाविहितम्, whichever was already prescribed.

    So the code answers 4.3.25 by ASKING the rule that prescribed it.
    """

    def test_both_halves_of_the_promise_are_on_record(self):
        self.assertIn("पुरस्ताद् वक्ष्यन्ते",
                      unwrapped(REGISTRY.get("4.2.93").notes))
        made_good = unwrapped(REGISTRY.get("4.3.25").notes)
        self.assertIn("समर्थविभक्तयश्च निर्दिश्यन्ते", made_good)
        self.assertIn("यथाविहितं प्रत्ययो भवति", made_good)

    def test_and_the_rule_names_no_affix(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        row = provisions_for("4.3.25")[0]
        self.assertEqual(row.gives, "")
        self.assertEqual(row.also_gives, ())
        self.assertEqual(row.case, "saptamī")
        self.assertEqual(row.sense, "jāta")

    def test_and_the_answer_is_the_earlier_rule_s_own(self):
        """
        The vṛtti's examples are the outputs of 4.2.93, 4.2.94 and
        4.2.95 read off in order. Asking 4.3.25 about those bases has
        to give back exactly what asking those rules gives.
        """
        from src.astadhyayi.kala_taddhita import born_in
        from src.astadhyayi.sense_taddhita import in_sense

        for stem in ("rāṣṭra", "avārapāra", "grāma"):
            with self.subTest(stem=stem):
                born = born_in(stem, case="saptamī", sense="jāta")
                prescribed = in_sense(stem, sense="śeṣa")
                self.assertEqual(born.by, "4.3.25")
                self.assertEqual(born.gives, prescribed.gives)
                self.assertIn(prescribed.by, born.why)

    def test_and_the_two_bases_really_do_take_different_affixes(self):
        """
        If every base fell to one default the reuse would prove
        nothing. राष्ट्र takes 4.2.93's घ and ग्राम 4.2.94's य.
        """
        from src.astadhyayi.kala_taddhita import born_in

        self.assertEqual(born_in("rāṣṭra", case="saptamī",
                                 sense="jāta").gives, "gha")
        self.assertEqual(born_in("grāma", case="saptamī",
                                 sense="jāta").gives, "ya")

    def test_and_the_reuse_is_declared(self):
        declared = REGISTRY.get("4.3.25").reuses
        for sutra in ("4.2.93", "4.2.94", "4.2.95"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, declared)


class TheDefaultNamedToBeatItsBeater(unittest.TestCase):
    """
    4.3.16's **अण्ग्रहणं वृद्धाच्छस्य बाधनार्थम्** — the affix that
    would have come anyway, named so that 4.2.114's छ does not take
    the ground. The third rule in two pādas to spend a word this way.
    """

    def test_the_argument_is_on_record_here(self):
        self.assertIn("अण्ग्रहणं वृद्धाच्छस्य बाधनार्थम्",
                      unwrapped(REGISTRY.get("4.3.16").notes))

    def test_and_two_earlier_rules_spent_a_word_the_same_way(self):
        """
        Each names a DIFFERENT rival, which is why each had to say it
        separately. 4.2.110 puts the principle in a word of its own;
        4.2.132 names अण् so it beats 4.2.119's ठञ् where a base is
        both क-penultimate and उ-final; this rule names it against
        4.2.114's छ.
        """
        self.assertIn("बाधकबाधनार्थम्",
                      unwrapped(REGISTRY.get("4.2.110").notes))
        self.assertIn("अण्ग्रहणमुवर्णान्तादपि यथा स्यात्",
                      unwrapped(REGISTRY.get("4.2.132").notes))
        self.assertIn("अण्ग्रहणं वृद्धाच्छस्य बाधनार्थम्",
                      unwrapped(REGISTRY.get("4.3.16").notes))

    def test_and_the_rivals_they_name_are_three_different_rules(self):
        """
        The rule 4.2.132's note names was not codified when that note
        was written. It is now, and the claim can be checked.
        """
        from src.astadhyayi.sense_taddhita import provisions_for as sense

        self.assertTrue(REGISTRY.has("4.2.119"))
        self.assertEqual(sense("4.2.119")[0].gives, "ṭhañ")
        self.assertEqual(sense("4.2.114")[0].gives, "cha")

    def test_and_all_three_really_give_the_default(self):
        from src.astadhyayi.kala_taddhita import provisions_for as kala
        from src.astadhyayi.sense_taddhita import provisions_for as sense
        from src.astadhyayi.taddhita import default_affix

        self.assertEqual(sense("4.2.110")[0].gives, default_affix().gives)
        self.assertEqual(sense("4.2.132")[0].gives, default_affix().gives)
        for row in kala("4.3.16"):
            with self.subTest(on=row.of_samjna or row.gana):
                self.assertEqual(row.gives, default_affix().gives)

    def test_and_the_rule_they_are_all_beating_gives_something_else(self):
        from src.astadhyayi.sense_taddhita import provisions_for
        from src.astadhyayi.taddhita import default_affix

        beaten = provisions_for("4.2.114")[0]
        self.assertEqual(beaten.gives, "cha")
        self.assertNotEqual(beaten.gives, default_affix().gives)


class ThreeRecensionsForThreeForms(unittest.TestCase):
    """
    4.3.22's **तदेवं त्रीणि रूपाणि भवन्ति**, and the vṛtti cites each
    of the three from a different Vedic recension. A claim about
    attested texts, not about the grammar — so it is held as data.
    """

    def test_three_forms_and_three_texts(self):
        from src.astadhyayi.kala_taddhita import HEMANTA_FORMS

        self.assertEqual(len(HEMANTA_FORMS), 3)
        self.assertEqual(len({form for form, _, _ in HEMANTA_FORMS}), 3)
        self.assertEqual(len({text for _, text, _ in HEMANTA_FORMS}), 3)
        for form, text, place in HEMANTA_FORMS:
            with self.subTest(form=form):
                self.assertTrue(place)

    def test_and_each_form_is_quoted_in_the_notes(self):
        from src.astadhyayi.kala_taddhita import HEMANTA_FORMS

        notes = unwrapped(REGISTRY.get("4.3.22").notes)
        self.assertIn("तदेवं त्रीणि रूपाणि भवन्ति", notes)
        for form, _, _ in HEMANTA_FORMS:
            with self.subTest(form=form):
                self.assertIn(form, notes)

    def test_and_the_rules_that_make_them_differ_as_the_vrtti_says(self):
        """
        **ऋत्वणि हि तकारलोपो नास्ति** — two affixes of identical
        shape, and only one of them drops the त.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        this = provisions_for("4.3.22")[0]
        season = [row for row in provisions_for("4.3.16")
                  if row.of_samjna == "ṛtu"][0]
        self.assertEqual(this.gives, season.gives)
        self.assertEqual(this.drops, "t")
        self.assertEqual(season.drops, "")

    def test_and_the_third_form_comes_from_the_vedic_rule(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        vedic = provisions_for("4.3.21")[0]
        self.assertEqual(vedic.usage, "chandasi")
        self.assertEqual(vedic.gives, "ṭhañ")
        self.assertIn("हैमन्तिकमिति हि भाषायामपि ठञं स्मरन्ति",
                      unwrapped(REGISTRY.get("4.3.22").notes))


class AnOptionChainRatherThanACompetition(unittest.TestCase):
    """
    4.3.15: **एताभ्यां मुक्ते ट्युट्युलावपि भवतः** — where both
    earlier options are let go, two more affixes come. Three words
    for *of tomorrow* from three rules in two pādas, and the options
    hand on to each other rather than fighting.
    """

    def test_the_chain_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.15").notes)
        self.assertIn("एताभ्यां मुक्ते ट्युट्युलावपि भवतः", notes)
        self.assertIn("श्वस्त्यः", notes)
        self.assertIn("शौवस्तिकः", notes)

    def test_and_the_two_other_rules_exist(self):
        self.assertTrue(REGISTRY.has("4.2.105"))
        self.assertTrue(REGISTRY.has("4.3.23"))

    def test_and_this_rule_carries_the_affixes_it_hands_on_to(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        row = provisions_for("4.3.15")[0]
        self.assertTrue(row.optional)
        self.assertEqual(row.gives, "ṭhañ")
        self.assertEqual(row.augment, "tuṭ")
        for affix in ("ṭyu", "ṭyul"):
            with self.subTest(affix=affix):
                self.assertIn(affix, row.also_gives)

    def test_and_the_rule_they_come_from_gives_the_same_two(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        handed_on = provisions_for("4.3.23")[0]
        self.assertEqual(handed_on.gives, "ṭyu")
        self.assertIn("ṭyul", handed_on.also_gives)
        self.assertEqual(handed_on.augment, "tuṭ")


class AnAnuvrttiReportedWithAnAuthority(unittest.TestCase):
    """
    4.3.27: **संज्ञाधिकारं केचित् कृतलब्धक्रीतकुशलाः इति यावद्
    अनुवर्तयन्ति** — SOME carry the संज्ञा heading to 4.3.38.

    A range with both ends stated is not the same thing as a range
    the tradition agrees on, and the row records whose reading it is
    rather than adopting it.
    """

    def test_the_attribution_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.27").notes)
        self.assertIn("संज्ञाधिकारं केचित्", notes)
        self.assertIn("कृतलब्धक्रीतकुशलाः", notes)

    def test_and_the_row_names_whose_reading_it_is(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.27")[0].authority, "kecit")

    def test_and_it_is_the_only_row_here_that_needs_one(self):
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        attributed = {row.sutra for row in KALA_TABLE if row.authority}
        self.assertEqual(attributed, {"4.3.27"})

    def test_and_the_undisputed_carry_is_taken_without_one(self):
        """
        4.3.28 relies on the same heading one rule later, which
        nobody disputes, so its row states the condition and names no
        authority for it.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        next_rule = provisions_for("4.3.28")[0]
        self.assertEqual(next_rule.of_samjna, "saṃjñā")
        self.assertEqual(next_rule.authority, "")


class ARuleThatMakesTheWordsItAttachesTo(unittest.TestCase):
    """
    4.3.23 names four words and then adds *and from indeclinables*.
    Three of the four are already indeclinable, so the naming is not
    for the affix — it is for the SHAPE, laid down together with the
    affix: **प्रत्ययसन्नियोगेन निपात्यते**.
    """

    def test_the_argument_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.23").notes)
        self.assertIn("ततोऽव्ययत्वादेव सिद्धः प्रत्ययः", notes)
        self.assertIn("प्रत्ययसन्नियोगेन निपात्यते", notes)
        self.assertIn("दिवसावसानं सायः", notes)

    def test_and_the_table_states_both_grounds(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        rows = provisions_for("4.3.23")
        self.assertEqual(len(rows), 2)
        named, general = rows
        self.assertEqual(len(named.of), 4)
        self.assertEqual(general.of, ())
        self.assertEqual(general.of_samjna, "avyaya")

    def test_and_the_general_ground_really_answers_without_a_name(self):
        from src.astadhyayi.kala_taddhita import born_in

        answer = born_in(sense="śeṣa", samjna="avyaya")
        self.assertEqual(answer.by, "4.3.23")
        self.assertEqual(answer.gives, "ṭyu")


class OneWordHeadingTwoRanges(unittest.TestCase):
    """
    काल heads two stretches of this pāda, and each end is stated a
    different way. The first is bounded in ADVANCE — 4.3.11's vṛtti
    says **तत्र जातः इति प्रागतः कालाधिकारः**. The second is closed
    from BEHIND — 4.3.53's opens **कालादिति निवृत्तम्**.
    """

    def test_both_ranges_are_held(self):
        from src.astadhyayi.kala_taddhita import KALA_RUN, KALA_RUNS

        self.assertEqual(KALA_RUNS,
                         (("4.3.11", "4.3.24"), ("4.3.43", "4.3.52")))
        self.assertEqual(KALA_RUN, KALA_RUNS[0])

    def test_and_they_do_not_overlap(self):
        (first_open, first_close), (next_open, _) = (
            __import__("src.astadhyayi.kala_taddhita",
                       fromlist=["KALA_RUNS"]).KALA_RUNS)
        self.assertLess(int(first_close.rsplit(".", 1)[1]),
                        int(next_open.rsplit(".", 1)[1]))
        self.assertLess(int(first_open.rsplit(".", 1)[1]),
                        int(first_close.rsplit(".", 1)[1]))

    def test_each_end_is_stated_in_its_own_way(self):
        from src.astadhyayi.kala_taddhita import kala_run

        ahead = kala_run(1)
        self.assertEqual(ahead.by, "4.3.11")
        self.assertIn("प्रागतः कालाधिकारः", ahead.why)
        self.assertIn("तत्र जातः इति प्रागतः कालाधिकारः",
                      unwrapped(REGISTRY.get("4.3.11").notes))

        behind = kala_run(2)
        self.assertEqual(behind.by, "4.3.43")
        self.assertIn("कालादिति निवृत्तम्", behind.why)
        self.assertIn("कालादिति निवृत्तम्",
                      unwrapped(REGISTRY.get("4.3.53").notes))

    def test_and_the_second_range_begins_because_the_word_is_said_again(
            self):
        """
        The first range ended, so the second cannot be anuvṛtti. It
        begins because 4.3.43 कालात् puts the word back in a sūtra of
        its own.
        """
        from src.astadhyayi.corpus import collate

        self.assertTrue(collate()["4.3.43"].witnesses)
        opening = [w for w in collate()["4.3.43"].witnesses.values()][0]
        self.assertTrue(opening.startswith("kālāt"))
        self.assertIn("काल IS NAMED A SECOND TIME",
                      unwrapped(REGISTRY.get("4.3.43").notes))

    def test_every_row_inside_a_range_carries_the_word(self):
        """
        A range that nothing in the table observes would be a claim
        with no consequence. Every rule of the second stretch either
        states काल in its own row or names its own bases instead.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE, KALA_RUNS

        opens, closes = (int(end.rsplit(".", 1)[1])
                         for end in KALA_RUNS[1])
        inside = [row for row in KALA_TABLE
                  if opens <= int(row.sutra.rsplit(".", 1)[1]) <= closes]
        self.assertEqual(len(inside), 10)
        for row in inside:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(row.of_samjna == "kāla" or row.of)


class MatchingInOrderFailsAndThenRuns(unittest.TestCase):
    """
    1.3.10's यथासंख्य pairs things named together with results named
    together. 4.3.1 could not use it — **वैषम्याद्** — because two
    bases faced three affixes. 4.3.33 can: two and two.
    """

    def test_the_failure_and_the_success_are_both_recorded(self):
        self.assertIn("वैषम्याद् यथासंख्यं न भवति",
                      unwrapped(REGISTRY.get("4.3.1").notes))
        self.assertIn("यथासंख्य", unwrapped(REGISTRY.get("4.3.33").notes))

    def test_and_the_counts_are_what_the_argument_says(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        unequal = provisions_for("4.3.1")[0]
        self.assertNotEqual(len(unequal.of),
                            len((unequal.gives,) + unequal.also_gives))

        matched = provisions_for("4.3.33")
        self.assertEqual(len(matched), 2)
        for row in matched:
            with self.subTest(gives=row.gives):
                self.assertEqual(len(row.of), 1)
        self.assertEqual(len({row.gives for row in matched}), 2)

    def test_and_each_base_gets_the_affix_paired_with_it(self):
        from src.astadhyayi.kala_taddhita import born_in

        for stem, affix in (("sindhu", "aṇ"), ("apakara", "añ")):
            with self.subTest(stem=stem):
                answer = born_in(stem, case="saptamī", sense="jāta",
                                 wants=affix)
                self.assertEqual(answer.by, "4.3.33")
                self.assertEqual(answer.gives, affix)

    def test_and_the_unequal_rule_gives_every_base_every_affix(self):
        from src.astadhyayi.kala_taddhita import born_in, provisions_for

        row = provisions_for("4.3.1")[0]
        for stem in row.of:
            for affix in (row.gives,) + row.also_gives:
                with self.subTest(stem=stem, affix=affix):
                    self.assertEqual(
                        born_in(stem, sense="śeṣa", wants=affix).by,
                        "4.3.1")


class AnAffixElidedAndAnotherPutInItsPlace(unittest.TestCase):
    """
    4.3.34. The taddhita goes by लुक्; 1.2.49 लुक् तद्धितलुकि takes
    the feminine affix with it; and then, for three words a vārttika
    adds, **गौरादित्वाद् ङीष्** supplies a different feminine affix.
    Three rules acting on one word in sequence.
    """

    def test_the_three_steps_are_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.34").notes)
        self.assertIn("लुक् तद्धितलुकि", notes)
        self.assertIn("स्त्रीप्रत्ययस्य लुकि कृते गौरादित्वाद् ङीष्",
                      notes)
        self.assertIn("चित्रारेवतीरोहिणीभ्यः", notes)

    def test_and_all_three_rules_are_codified(self):
        for sutra in ("1.2.49", "4.1.41"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))

    def test_and_the_rule_that_supplies_the_replacement_gives_ngis(self):
        from src.astadhyayi.stri import stri_affix

        supplied = stri_affix(gana="gaurādi")
        self.assertEqual(supplied.by, "4.1.41")
        self.assertEqual(supplied.gives, "ṅīṣ")

    def test_and_the_row_says_the_affix_goes(self):
        from src.astadhyayi.kala_taddhita import born_in, provisions_for

        row = provisions_for("4.3.34")[0]
        self.assertTrue(row.elides)
        self.assertEqual(row.gives, "")

        answer = born_in(gana="śraviṣṭhādi", samjna="nakṣatra",
                         case="saptamī", sense="jāta")
        self.assertEqual(answer.by, "4.3.34")
        self.assertTrue(answer.elided)
        self.assertEqual(answer.gives, "")


class VariouslyIsNotOptionally(unittest.TestCase):
    """
    4.3.37's बहुलम् against 4.3.36's वा. An option makes both forms
    correct wherever it reaches; *variously* says the elision happens
    in some places and not others without saying which — which is why
    three rules can spell out particular cases and the word still has
    work left.
    """

    def test_the_two_are_in_separate_columns(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        various = provisions_for("4.3.37")[0]
        self.assertTrue(various.bahulam)
        self.assertFalse(various.optional)

        optional = provisions_for("4.3.36")[0]
        self.assertTrue(optional.optional)
        self.assertFalse(optional.bahulam)

    def test_and_variousness_is_used_where_no_list_could_serve(self):
        """
        Two rules of the pāda say बहुलम्, and both use it for the
        same thing: a scatter the grammar declines to enumerate.
        4.3.37 will not say which mansions elide; 4.3.99 will not
        say which lineage-names are exempt — **बहुलग्रहणात्
        क्वचिदप्रवृत्तिरेव**, and पाणिनीयः is the example.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        various = {row.sutra for row in KALA_TABLE if row.bahulam}
        self.assertEqual(various, {"4.3.37", "4.3.99"})
        for row in KALA_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertFalse(row.bahulam and row.optional)
        self.assertIn("बहुलग्रहणात् क्वचिदप्रवृत्तिरेव",
                      unwrapped(REGISTRY.get("4.3.99").notes))

    def test_and_the_vrtti_relates_the_two(self):
        """
        **बहुलग्रहणस्यायं प्रपञ्चः** — the three rules before 4.3.37
        are read as an unfolding of its one word.
        """
        self.assertIn("बहुलग्रहणस्यायं प्रपञ्चः",
                      unwrapped(REGISTRY.get("4.3.36").notes))

    def test_and_the_elision_run_is_contiguous(self):
        """
        4.3.34 to 4.3.37 are one run and the property worth checking
        is that it has no gaps. 4.3.107 elides too, seventy sūtras
        later and in a different sense, which is why the test states
        the run rather than counting the rules.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        eliding = sorted({int(row.sutra.rsplit(".", 1)[1])
                          for row in KALA_TABLE if row.elides})
        run = [n for n in eliding if n <= 40]
        self.assertEqual(run, list(range(min(run), max(run) + 1)))
        self.assertEqual(run, [34, 35, 36, 37])

    def test_and_the_later_elision_is_in_another_sense(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertTrue(provisions_for("4.3.107")[0].elides)
        self.assertEqual(provisions_for("4.3.107")[0].sense, "prokta")
        self.assertEqual(provisions_for("4.3.37")[0].sense, "jāta")


class TheWordsDifferWhereTheFactsDoNot(unittest.TestCase):
    """
    4.3.38 names four senses, and the objection is that they overlap
    in fact: whatever was bought somewhere was also got there. The
    answer is that **शब्दार्थस्य भिन्नत्वात्** — the meanings of the
    WORDS differ, whatever the facts do.
    """

    def test_the_objection_and_the_answer_are_both_recorded(self):
        notes = unwrapped(REGISTRY.get("4.3.38").notes)
        self.assertIn("किमर्थं भेदेनोपादानं क्रियते", notes)
        self.assertIn("शब्दार्थस्य भिन्नत्वाद्", notes)
        self.assertIn("वस्तुमात्रेण क्रीतं लब्धं भवति", notes)

    def test_and_the_four_senses_are_one_row_with_one_affix(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        rows = provisions_for("4.3.38")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].sense, "kṛta-labdha-krīta-kuśala")
        self.assertEqual(rows[0].gives, "")

    def test_and_the_affix_is_still_whichever_was_prescribed(self):
        from src.astadhyayi.kala_taddhita import born_in
        from src.astadhyayi.sense_taddhita import in_sense

        for stem in ("rāṣṭra", "grāma"):
            with self.subTest(stem=stem):
                made = born_in(stem, case="saptamī",
                               sense="kṛta-labdha-krīta-kuśala")
                self.assertEqual(made.by, "4.3.38")
                self.assertEqual(made.gives,
                                 in_sense(stem, sense="śeṣa").gives)


class ASenseNarrowedBySubtractingItsNeighbours(unittest.TestCase):
    """
    4.3.41's संभूत is *fitting in*, **नोत्पत्तिः सत्ता वा,
    जातभवाभ्यां गतत्वात्** — not arising and not being, because two
    other rules have those. One of the two is fourteen sūtras ahead.
    """

    def test_the_subtraction_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.41").notes)
        self.assertIn("नोत्पत्तिः सत्ता वा", notes)
        self.assertIn("जातभवाभ्यां गतत्वात्", notes)

    def test_and_the_two_rules_subtracted_really_hold_those_senses(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.25")[0].sense, "jāta")
        self.assertEqual(provisions_for("4.3.53")[0].sense, "bhava")
        self.assertEqual(provisions_for("4.3.41")[0].sense, "saṃbhūta")

    def test_and_the_later_rule_makes_the_same_subtraction(self):
        """
        4.3.53 subtracts back: **सत्ता भवत्यर्थो गृह्यते न जन्म,
        तत्र जातः इति गतार्थत्वात्**. Two rules dividing one region
        of meaning between them, and each naming the other.
        """
        notes = unwrapped(REGISTRY.get("4.3.53").notes)
        self.assertIn("सत्ता भवत्यर्थो गृह्यते न जन्म", notes)
        self.assertIn("गतार्थत्वात्", notes)

    def test_and_the_three_senses_stay_apart_in_the_table(self):
        from src.astadhyayi.kala_taddhita import born_in

        answers = {sense: born_in("rāṣṭra", case="saptamī", sense=sense).by
                   for sense in ("jāta", "saṃbhūta", "bhava")}
        self.assertEqual(answers,
                         {"jāta": "4.3.25", "saṃbhūta": "4.3.41",
                          "bhava": "4.3.53"})


class AWordRepeatedInOrderToPushAnotherOut(unittest.TestCase):
    """
    4.3.52 takes its base in the NOMINATIVE, the only rule since
    4.3.25 to do so. 4.3.53 says तत्र again — **पुनस्तत्रग्रहणं
    तदस्येति निवृत्त्यर्थम्** — not because the word had lapsed but
    so that the last rule's तदस्य goes.
    """

    def test_the_odd_case_is_in_the_table(self):
        """
        Six case-relations are used past 4.3.25, and the locative is
        the one that carries. 4.3.52 is the FIRST rule to leave it,
        and the empty string is the rows that state no case because
        two headings carry over them.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        cases = {row.case for row in KALA_TABLE
                 if int(row.sutra.rsplit(".", 1)[1]) >= 25}
        self.assertEqual(
            cases,
            {"saptamī", "prathamā", "ṣaṣṭhī", "pañcamī", "dvitīyā",
             "tṛtīyā", ""})

        nominative = sorted(
            {int(row.sutra.rsplit(".", 1)[1]) for row in KALA_TABLE
             if row.case == "prathamā"})
        self.assertEqual(min(nominative), 52)

    def test_and_the_locative_is_the_only_one_stated_twice(self):
        """
        Not the commonest — past 4.3.90 it is not even that. What
        makes it the one that CARRIES is that it is the only case
        this pāda states a second time, at 4.3.53, and it does that
        in order to push another case out.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        opens = {}
        for row in sorted(KALA_TABLE,
                          key=lambda r: int(r.sutra.rsplit(".", 1)[1])):
            if not row.case:
                continue
            opens.setdefault(row.case, []).append(row.sutra)

        restated = {case for case, rules in opens.items()
                    if "4.3.53" in rules}
        self.assertEqual(restated, {"saptamī"})
        self.assertIn("पुनस्तत्रग्रहणं तदस्येति निवृत्त्यर्थम्",
                      unwrapped(REGISTRY.get("4.3.53").notes))

    def test_and_the_reason_for_the_repetition_is_recorded(self):
        notes = unwrapped(REGISTRY.get("4.3.53").notes)
        self.assertIn("पुनस्तत्रग्रहणं तदस्येति निवृत्त्यर्थम्", notes)

    def test_and_the_case_really_is_changed_back(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.52")[0].case, "prathamā")
        self.assertEqual(provisions_for("4.3.53")[0].case, "saptamī")
        self.assertEqual(provisions_for("4.3.54")[0].case, "saptamī")


class ACommentaryCallingItsOwnRulePointless(unittest.TestCase):
    """
    4.3.39: **प्रायभवग्रहणमनर्थकम्, तत्रभवेन कृतार्थत्वात्** —
    naming *mostly-there* achieves nothing, because 4.3.53 covers it.
    And the defence offered is turned away too.
    """

    def test_the_verdict_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.39").notes)
        self.assertIn("प्रायभवग्रहणमनर्थकम्", notes)
        self.assertIn("तत्रभवेन कृतार्थत्वात्", notes)
        self.assertIn("मुक्तसंशयेन तुल्यम्", notes)

    def test_and_the_rule_said_to_cover_it_exists_and_does(self):
        from src.astadhyayi.kala_taddhita import born_in

        self.assertTrue(REGISTRY.has("4.3.53"))
        mostly = born_in("rāṣṭra", case="saptamī", sense="prāya-bhava")
        being = born_in("rāṣṭra", case="saptamī", sense="bhava")
        self.assertEqual(mostly.gives, being.gives)

    def test_and_the_rule_is_codified_all_the_same(self):
        """
        A rule the tradition calls unnecessary is still a rule of the
        text, and the codification records the verdict rather than
        acting on it.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertTrue(provisions_for("4.3.39"))
        self.assertEqual(provisions_for("4.3.39")[0].sense, "prāya-bhava")


class SeasonsNamedByWhatHappensInThem(unittest.TestCase):
    """
    4.3.48's three bases are not time-words at all: **कलाप्यादयः
    शब्दाः साहचर्यात् काले वर्तन्ते** — they denote times by the
    company they keep. 4.3.11 allowed this by गुणवृत्ति and gave an
    example; this rule names the mechanism.
    """

    def test_the_mechanism_is_named_here(self):
        notes = unwrapped(REGISTRY.get("4.3.48").notes)
        self.assertIn("साहचर्यात् काले वर्तन्ते", notes)
        self.assertIn("मयूराः कलापिनो भवन्ति", notes)

    def test_and_the_earlier_rule_had_allowed_it_without_naming_it(self):
        notes = unwrapped(REGISTRY.get("4.3.11").notes)
        self.assertIn("गुणवृत्त्यापि काले वर्तमानात्", notes)
        self.assertIn("कादम्बपुष्पिकम्", notes)

    def test_and_the_two_rules_are_in_the_same_region_of_the_pada(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.11")[0].of_samjna, "kāla")
        self.assertEqual(provisions_for("4.3.48")[0].sense, "deya-ṛṇa")
        self.assertTrue(provisions_for("4.3.48")[0].of)


class TwoHeadingsGoverningAtOnce(unittest.TestCase):
    """
    4.3.66's च reaches BACKWARD — **वाक्यार्थसमीपे चकारः श्रूयमाणः
    पूर्ववाक्यार्थमेव समुच्चिनोति** — so भव and व्याख्यान run
    together. And the vṛtti says what the overlap is for:
    **भवव्याख्यानयोर्युगपदधिकारोऽपवादविधानार्थः, कृतनिर्देशौ हि तौ**.

    Every range this project has recorded until now DISPLACED the one
    before it. These two are made to coincide, on purpose, so that
    the exceptions after them need stating once instead of twice.
    """

    def test_the_conjunction_and_its_purpose_are_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.66").notes)
        self.assertIn("पूर्ववाक्यार्थमेव समुच्चिनोति", notes)
        self.assertIn("भवव्याख्यानयोर्युगपदधिकार", notes)
        self.assertIn("कृतनिर्देशौ हि तौ", notes)

    def test_and_the_sentence_it_reaches_back_to_is_codified(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertTrue(REGISTRY.has("4.3.53"))
        self.assertEqual(provisions_for("4.3.53")[0].sense, "bhava")

    def test_the_rule_itself_states_both_senses_and_both_cases(self):
        """
        व्याख्यान takes the genitive — तस्य — and भव keeps the
        locative it was stated with. One rule, two grounds.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        rows = provisions_for("4.3.66")
        self.assertEqual(len(rows), 2)
        self.assertEqual({(row.sense, row.case) for row in rows},
                         {("vyākhyāna", "ṣaṣṭhī"), ("bhava", "saptamī")})

    def test_and_every_exception_after_it_answers_under_both(self):
        """
        The economy the vṛtti claims is checkable: each of the seven
        rules from 4.3.67 to 4.3.73 must be reachable by asking for
        either sense, or it would have needed stating twice.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE, born_in

        under_both = [row for row in KALA_TABLE if row.also_sense]
        pairs = {frozenset((row.sense, row.also_sense))
                 for row in under_both}
        self.assertEqual(
            pairs,
            {frozenset(("vyākhyāna", "bhava")),
             frozenset(("avayava", "vikāra"))})

        for row in under_both:
            for sense in (row.sense, row.also_sense):
                where = {"sense": sense, "wants": row.gives}
                if row.of:
                    where["stem"] = row.of[0]
                if row.gana:
                    where["gana"] = row.gana
                if row.of_samjna:
                    where["samjna"] = row.of_samjna
                if row.result:
                    where["result"] = row.result
                if row.stem_final:
                    where["stem_final"] = row.stem_final
                if row.vowels:
                    where["vowels"] = row.vowels
                if row.accent:
                    where["accent"] = row.accent
                if row.upadha:
                    where["upadha"] = row.upadha
                if row.usage:
                    where["usage"] = row.usage
                with self.subTest(sutra=row.sutra, sense=sense):
                    self.assertEqual(born_in(**where).by, row.sutra)

    def test_and_the_pada_does_this_twice_in_the_same_words(self):
        """
        4.3.66 said **भवव्याख्यानयोर्युगपदधिकारोऽपवादविधानार्थः,
        कृतनिर्देशौ हि तौ** of भव and व्याख्यान. 4.3.135 says it of
        विकार and अवयव, sixty-nine sūtras later, with only the two
        names changed. Twice in one pāda and nowhere else so far.
        """
        first = unwrapped(REGISTRY.get("4.3.66").notes)
        second = unwrapped(REGISTRY.get("4.3.135").notes)
        self.assertIn("भवव्याख्यानयोर्युगपदधिकार", first)
        self.assertIn("विकारावयवयोर्युगपदधिकार", second)
        for notes in (first, second):
            with self.subTest():
                self.assertIn("ऽपवादविधानार्थः", notes)
                self.assertIn("कृतनिर्देशौ हि तौ", notes)

    def test_and_each_pair_opens_where_the_vrtti_says(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual({(row.sense, row.case)
                          for row in provisions_for("4.3.66")},
                         {("vyākhyāna", "ṣaṣṭhī"), ("bhava", "saptamī")})
        opened = provisions_for("4.3.135")[0]
        self.assertEqual(opened.sense, "avayava")
        self.assertEqual(opened.also_sense, "vikāra")
        self.assertEqual(provisions_for("4.3.134")[0].sense, "vikāra")

    def test_and_the_second_sense_buys_no_specificity(self):
        """
        A rule under two headings is not NARROWER than one under a
        single heading — only reachable from two directions. If
        `also_sense` scored in the ranking it would start beating
        rules that state more.
        """
        from src.astadhyayi.kala_taddhita import Kala, _how_specific

        plain = Kala("x", sense="bhava")
        doubled = Kala("x", sense="vyākhyāna", also_sense="bhava")
        self.assertEqual(_how_specific(plain), _how_specific(doubled))


class ThePadaUsesFiveCaseRelations(unittest.TestCase):
    """
    From 4.3.25 the rules name the relation their base stands in, and
    over sixty-six sūtras they name five different ones — locative,
    nominative, genitive, ablative, accusative — each opened by a rule
    that says so in its own words.
    """

    def test_each_case_is_opened_by_a_rule_that_states_it(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        opened = {
            "4.3.25": "saptamī",
            "4.3.52": "prathamā",
            "4.3.66": "ṣaṣṭhī",
            "4.3.74": "pañcamī",
            "4.3.85": "dvitīyā",
        }
        for sutra, case in opened.items():
            with self.subTest(sutra=sutra):
                cases = {row.case for row in provisions_for(sutra)}
                self.assertIn(case, cases)

    def test_and_the_words_that_state_them_are_in_the_notes(self):
        for sutra, word in (("4.3.52", "प्रथमासमर्थात्"),
                            ("4.3.66", "षष्ठीसमर्थ"),
                            ("4.3.74", "ABLATIVE"),
                            ("4.3.85", "द्वितीयासमर्थात्")):
            with self.subTest(sutra=sutra):
                self.assertIn(word, unwrapped(REGISTRY.get(sutra).notes))

    def test_and_they_keep_the_answers_apart(self):
        from src.astadhyayi.kala_taddhita import born_in

        answers = {
            born_in("rāṣṭra", case="saptamī", sense="bhava").by,
            born_in(case="pañcamī", sense="āgata").by,
            born_in(case="dvitīyā", sense="gacchati",
                    result="pathi-dūta").by,
            born_in(case="prathamā", sense="nivāsa").by,
        }
        self.assertEqual(answers,
                         {"4.3.53", "4.3.74", "4.3.85", "4.3.89"})


class AnAtidesaReachingForwardAgain(unittest.TestCase):
    """
    4.3.80 गोत्रादङ्कवत् borrows from 4.3.127, which is ninety-seven
    sūtras ahead and not codified. The row names it and the answer
    says whose affixes are meant rather than pretending to have them.

    The same shape as 4.2.34's debt, which collected itself when
    4.3.11 arrived — and this test is written so this one will too.
    """

    def test_the_atidesa_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.80").notes)
        self.assertIn("तस्येदमर्थसामान्यं लक्ष्यते", notes)
        self.assertIn("तस्माद् वुञप्यतिदिश्यते नाणेव", notes)

    def test_and_the_row_names_what_it_borrows_from(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        row = provisions_for("4.3.80")[0]
        self.assertEqual(row.borrows_from, "4.3.127")
        self.assertEqual(row.gives, "")

    def test_the_rule_it_borrows_from_has_arrived(self):
        """
        It lay ahead when this rule was codified, and the test said so
        as the exact shortfall. It is codified now, in the same pāda,
        forty-seven sūtras later.
        """
        from src.astadhyayi.corpus import collate

        self.assertIn("4.3.127", collate())
        self.assertTrue(REGISTRY.has("4.3.127"))

    def test_and_the_borrowing_now_names_where_it_asks(self):
        """
        Running it showed the row had to say WHICH sense it borrows
        under. Without that it asked its own question again and
        matched itself.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        asked = dict(provisions_for("4.3.80")[0].borrow_query)
        self.assertEqual(asked["sense"], "idam")
        self.assertEqual(asked["case"], "ṣaṣṭhī")
        self.assertNotEqual(asked["sense"],
                            provisions_for("4.3.80")[0].sense)

    def test_and_the_project_has_kept_this_kind_of_promise_before(self):
        from src.astadhyayi.sense_taddhita import provisions_for

        self.assertEqual(provisions_for("4.2.34")[0].borrows_from,
                         "4.3.11")
        self.assertTrue(REGISTRY.has("4.3.11"))


class FiveYogavibhagasForThreePurposes(unittest.TestCase):
    """
    A योगविभाग splits one rule into two. This pāda does it five
    times, and not always for the same reason: 4.3.21, 4.3.44 and
    4.3.90 are उत्तरार्थ, for the sake of what follows; 4.3.2's and
    4.3.82's are to stop 1.3.10's matching-in-order from running.
    """

    def test_all_five_are_on_record(self):
        for sutra in ("4.3.2", "4.3.21", "4.3.44", "4.3.82", "4.3.90"):
            with self.subTest(sutra=sutra):
                self.assertIn("योगविभाग",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_three_are_for_the_sake_of_what_follows(self):
        for sutra in ("4.3.21", "4.3.44", "4.3.90"):
            with self.subTest(sutra=sutra):
                self.assertIn("योगविभाग उत्तरार्थः",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_two_are_to_stop_a_correspondence(self):
        self.assertIn("यथासंख्यं कस्माद् न भवति",
                      unwrapped(REGISTRY.get("4.3.2").notes))
        self.assertIn("योगविभागो यथासंख्यनिरासार्थः",
                      unwrapped(REGISTRY.get("4.3.82").notes))

    def test_and_the_rule_they_are_stopping_is_codified(self):
        self.assertTrue(REGISTRY.has("1.3.10"))

    def test_and_the_pair_that_would_have_matched_gives_both_affixes(self):
        """
        4.3.81 and 4.3.82 are stated of the same two grounds. Split,
        each affix reaches both; read as one rule, the pairing would
        have given one affix to each ground.
        """
        from src.astadhyayi.kala_taddhita import born_in, provisions_for

        first = provisions_for("4.3.81")[0]
        second = provisions_for("4.3.82")[0]
        self.assertEqual(first.of_samjna, second.of_samjna)
        self.assertNotEqual(first.gives, second.gives)
        for affix, sutra in ((first.gives, "4.3.81"),
                             (second.gives, "4.3.82")):
            with self.subTest(affix=affix):
                self.assertEqual(
                    born_in(case="pañcamī", sense="āgata",
                            samjna="hetu-manuṣya", wants=affix).by,
                    sutra)


class TwoRulesWithIdenticalOutputs(unittest.TestCase):
    """
    4.3.89 सोऽस्य निवासः and 4.3.90 अभिजनश्च produce the same word
    from the same base. **यत्र संप्रत्युष्यते स निवासः, यत्र
    पूर्वैरुषितं सोऽभिजनः** — the whole difference is which fact
    about a person is being reported.
    """

    def test_the_distinction_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.90").notes)
        self.assertIn("निवासाभिजनयोः को विशेषः", notes)
        self.assertIn("यत्र संप्रत्युष्यते स निवासः", notes)
        self.assertIn("यत्र पूर्वैरुषितं सोऽभिजनः", notes)

    def test_and_the_two_really_do_produce_the_same_form(self):
        from src.astadhyayi.kala_taddhita import born_in

        now = born_in("rāṣṭra", case="prathamā", sense="nivāsa")
        before = born_in("rāṣṭra", case="prathamā", sense="abhijana")
        self.assertNotEqual(now.by, before.by)
        self.assertEqual(now.gives, before.gives)

    def test_and_the_affix_comes_from_a_place_word_not_a_kinsman(self):
        """
        **तस्माद् इह देशवाचिनः प्रत्ययः, न बन्धुभ्यः,
        निवासप्रत्यासत्तेः** — अभिजन means the forebears, but the
        affix is taken from the PLACE, because the rule stands next
        to one about a place.
        """
        notes = unwrapped(REGISTRY.get("4.3.90").notes)
        self.assertIn("न बन्धुभ्यः", notes)
        self.assertIn("निवासप्रत्यासत्तेः", notes)


class AListFollowedFromUsageAndWrittenNowhere(unittest.TestCase):
    """
    4.3.88's इन्द्रजननादि: **आकृतिगणः प्रयोगतोऽनुसर्तव्यः,
    प्रातिपदिकेषु न पठ्यते** — open, to be followed from actual
    usage, and not written out in the गणपाठ at all.
    """

    def test_the_claim_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.88").notes)
        # इन्द्रजननादिः + आकृतिगणः is इन्द्रजननादिराकृतिगणः, and
        # the independent आ is gone. Sandhi, eleventh time.
        self.assertIn("प्रयोगतोऽनुसर्तव्यः", notes)
        self.assertIn("इन्द्रजननादिराकृतिगणः", notes)
        self.assertIn("प्रातिपदिकेषु न पठ्यते", notes)

    def test_and_the_list_the_rule_names_first_is_on_disk(self):
        """
        शिशुक्रन्दादि is in the गणपाठ; इन्द्रजननादि is what is not.
        The row is keyed by the first, which is the one that can be
        checked.
        """
        from src.astadhyayi.corpus import load_ganapatha
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.88")[0].gana,
                         "śiśukrandādi")
        lists = load_ganapatha()
        self.assertTrue(lists)

    def test_and_the_vrtti_notices_the_refusal_becomes_unnecessary(self):
        """
        A vārttika refuses the देवासुरादि compounds, and the vṛtti
        then observes that if the list is an आकृतिगण the refusal need
        not have been stated: **ततश्छप्रत्ययस्यादर्शनात्**.
        """
        notes = unwrapped(REGISTRY.get("4.3.88").notes)
        self.assertIn("देवासुरादिभ्यः प्रतिषेधः", notes)
        self.assertIn("प्रपञ्चार्थमेषां ग्रहणम्", notes)


class AWorkedExampleThatCanNowBeRun(unittest.TestCase):
    """
    `reading.yathasamkhya` implements 1.3.10's pairing-in-order and
    named 4.3.94 as its worked example — four places against four
    affixes — when that rule was not yet codified. It is codified
    now, as four rows, so the example can be checked instead of read.
    """

    def test_the_helper_names_this_rule(self):
        import inspect

        from src.astadhyayi.reading import yathasamkhya

        self.assertIn("4.3.94", inspect.getdoc(yathasamkhya))
        self.assertTrue(REGISTRY.has("4.3.94"))

    def test_and_the_rule_really_states_four_against_four(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        rows = provisions_for("4.3.94")
        self.assertEqual(len(rows), 4)
        bases = [row.of[0] for row in rows]
        affixes = [row.gives for row in rows]
        self.assertEqual(len(set(bases)), 4)
        self.assertEqual(len(set(affixes)), 4)

    def test_and_the_helper_pairs_them_the_way_the_table_does(self):
        from src.astadhyayi.kala_taddhita import provisions_for
        from src.astadhyayi.reading import yathasamkhya

        rows = provisions_for("4.3.94")
        bases = [row.of[0] for row in rows]
        affixes = [row.gives for row in rows]
        self.assertEqual(yathasamkhya(bases, affixes),
                         tuple(zip(bases, affixes)))

    def test_and_it_refuses_the_rule_that_could_not_pair(self):
        """
        4.3.1 names two bases against three affixes, and the vṛtti
        says **वैषम्याद् यथासंख्यं न भवति**. The helper must return
        nothing for it — a truncated pairing would look like an
        answer.
        """
        from src.astadhyayi.kala_taddhita import provisions_for
        from src.astadhyayi.reading import yathasamkhya

        row = provisions_for("4.3.1")[0]
        self.assertIsNone(
            yathasamkhya(list(row.of),
                         [row.gives] + list(row.also_gives)))


class BothHalvesOfTheSameInstrument(unittest.TestCase):
    """
    Two अतिदेश twenty sūtras apart, pointing opposite ways. 4.3.80
    गोत्रादङ्कवत् reaches ninety-seven sūtras FORWARD to a rule not
    yet codified, so its answer can only name what it means. 4.3.100
    जनपदिनां जनपदवत् reaches BACKWARD to 4.2.124, which is codified,
    so its answer is fetched.
    """

    def test_both_rows_name_what_they_borrow_from(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.80")[0].borrows_from,
                         "4.3.127")
        self.assertEqual(provisions_for("4.3.100")[0].borrows_from,
                         "4.2.124")

    def test_one_points_forward_and_one_back(self):
        """
        Both targets are codified now — the forward one arrived in
        this same pāda, forty-seven sūtras after the rule that names
        it.
        """
        self.assertGreater(int("4.3.127".rsplit(".", 1)[1]), 80)
        self.assertLess(int("4.2.124".split(".")[1]), 3)
        self.assertTrue(REGISTRY.has("4.3.127"))
        self.assertTrue(REGISTRY.has("4.2.124"))

    def test_and_the_forward_one_now_runs_too(self):
        """
        The debt was written as the exact shortfall — a test asserting
        4.3.127 was absent — and it collected itself when that rule
        was codified. Running it then found a real fault: the row was
        asking under its OWN sense, so it matched itself.
        """
        from src.astadhyayi.kala_taddhita import born_in

        ahead = born_in(case="pañcamī", sense="āgata",
                        samjna="gotra-pratyayānta")
        self.assertEqual(ahead.by, "4.3.80")
        self.assertTrue(ahead.gives)

    def test_and_what_comes_back_is_not_the_affix_it_names(self):
        """
        **तस्माद् वुञप्यतिदिश्यते नाणेव.** 4.3.80 says अङ्कवत् and so
        names 4.3.127, which gives अण् — but its own examples are
        built on words ending in अण् already, which that rule cannot
        reach. 4.3.126's वुञ् is what answers, and the vṛtti says so.
        """
        from src.astadhyayi.kala_taddhita import born_in, provisions_for

        ahead = born_in(case="pañcamī", sense="āgata",
                        samjna="gotra-pratyayānta")
        self.assertEqual(ahead.gives, "vuñ")
        self.assertEqual(provisions_for("4.3.127")[0].gives, "aṇ")
        self.assertNotEqual(ahead.gives,
                            provisions_for("4.3.127")[0].gives)
        self.assertIn("4.3.126", ahead.why)
        self.assertIn("तस्माद् वुञप्यतिदिश्यते नाणेव",
                      unwrapped(REGISTRY.get("4.3.80").notes))

    def test_and_the_backward_one_still_runs(self):
        from src.astadhyayi.kala_taddhita import born_in
        from src.astadhyayi.sense_taddhita import in_sense

        behind = born_in(case="prathamā", sense="bhakti",
                         samjna="janapadin")
        self.assertEqual(behind.by, "4.3.100")
        self.assertEqual(
            behind.gives,
            in_sense(samjna="janapada-vṛddha", desa=True,
                     sense="śeṣa").gives)
        self.assertEqual(behind.gives, "vuñ")
        self.assertIn("4.2.124", behind.why)

    def test_and_the_borrowed_base_is_what_all_is_there_for(self):
        """
        **सर्वग्रहणं प्रकृत्यतिदेशार्थम्** — *all* is in the rule so
        that the BASE is borrowed too, which is what handing the
        other resolver a different संज्ञा amounts to.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        row = provisions_for("4.3.100")[0]
        self.assertEqual(row.of_samjna, "janapadin")
        self.assertEqual(dict(row.borrow_query)["samjna"],
                         "janapada-vṛddha")
        self.assertNotEqual(row.of_samjna,
                            dict(row.borrow_query)["samjna"])
        self.assertIn("सर्वग्रहणं प्रकृत्यतिदेशार्थम्",
                      unwrapped(REGISTRY.get("4.3.100").notes))


class APrincipleTaughtByWordOrder(unittest.TestCase):
    """
    4.3.98 puts वासुदेव before अर्जुन in a dvandva, and two
    compounding rules say अर्जुन should come first. Declining to obey
    either, the rule **ज्ञापयति — अभ्यर्हितं पूर्वं निपततीति**: the
    more venerated goes first.
    """

    def test_the_jnapaka_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.98").notes)
        self.assertIn("ज्ञापयति", notes)
        self.assertIn("अभ्यर्हितं पूर्वं निपततीति", notes)

    def test_and_the_two_rules_it_disobeys_are_codified(self):
        for sutra in ("2.2.33", "2.2.34"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))
                self.assertIn(sutra,
                              unwrapped(REGISTRY.get("4.3.98").notes))

    def test_and_the_order_in_the_row_is_the_order_in_the_rule(self):
        """
        The evidence is the order itself, so the row has to keep it.
        A set would have thrown the whole argument away.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.98")[0].of,
                         ("vāsudeva", "arjuna"))

    def test_and_the_other_question_the_rule_raises_is_answered(self):
        """
        Why name वासुदेव at all, when the next rule gives an
        equivalent affix? **संज्ञैषा देवताविशेषस्य न क्षत्रियाख्या**
        — it is a god's name, so that rule never reached it.
        """
        notes = unwrapped(REGISTRY.get("4.3.98").notes)
        self.assertIn("किमर्थं वासुदेवग्रहणम्", notes)
        self.assertIn("संज्ञैषा देवताविशेषस्य न क्षत्रियाख्या", notes)
        self.assertTrue(REGISTRY.has("4.3.99"))


class DirectPupilsOnlyProvedFromTheListsThemselves(unittest.TestCase):
    """
    4.3.104 reaches the pupils of two teachers. **प्रत्यक्षकारिणो
    गृह्यन्ते, न तु व्यवहिताः शिष्यशिष्याः** — and the proof is
    **कलापिखाडायनग्रहणात्**: two names would be redundant on the
    other reading, and are not on this one.
    """

    def test_the_lists_are_held_as_data(self):
        from src.astadhyayi.kala_taddhita import (KALAPI_PUPILS,
                                                  VAISAMPAYANA_PUPILS)

        self.assertEqual(len(KALAPI_PUPILS), 4)
        self.assertEqual(len(VAISAMPAYANA_PUPILS), 9)

    def test_and_the_argument_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.104").notes)
        self.assertIn("प्रत्यक्षकारिणो गृह्यन्ते", notes)
        self.assertIn("न तु व्यवहिताः शिष्यशिष्याः", notes)
        self.assertIn("कलापिखाडायनग्रहणात्", notes)

    def test_and_the_first_redundancy_really_is_one(self):
        """
        कलापी is IN the list of nine — so his own pupils would need
        no rule if the reach were transitive — and 4.3.108 gives him
        a rule of his own anyway.
        """
        from src.astadhyayi.kala_taddhita import (VAISAMPAYANA_PUPILS,
                                                  provisions_for)

        self.assertIn("कलापी", VAISAMPAYANA_PUPILS)
        own = provisions_for("4.3.108")[0]
        self.assertEqual(own.of, ("kalāpin",))
        self.assertIn("4.3.104", own.excepts)

    def test_and_the_second_redundancy_too(self):
        """
        कठ is in the same list, and his pupil खाडायन is read
        separately in 4.3.106's गण — which would be pointless if
        pupils of pupils came in by 4.3.104.
        """
        from src.astadhyayi.kala_taddhita import VAISAMPAYANA_PUPILS

        self.assertIn("कठ", VAISAMPAYANA_PUPILS)
        self.assertIn("खाडायन",
                      unwrapped(REGISTRY.get("4.3.104").notes))
        self.assertIn("तदेतत् प्रत्यक्षकारिग्रहणस्य लिङ्गम्",
                      unwrapped(REGISTRY.get("4.3.104").notes))

    def test_and_the_teacher_has_a_second_name_that_reaches_the_school(
            self):
        """
        **चरक इति वैशंपायनस्याख्या** — so 4.3.107, which elides after
        चरक, reaches the whole school the list of nine belongs to.
        """
        from src.astadhyayi.kala_taddhita import (CARAKA_IS,
                                                  provisions_for)

        self.assertEqual(CARAKA_IS, "vaiśampāyana")
        self.assertIn("caraka", provisions_for("4.3.107")[0].of)
        self.assertTrue(provisions_for("4.3.107")[0].elides)


class AGrammarDatingItsOwnTexts(unittest.TestCase):
    """
    4.3.105 restricts its affix to what an ANCIENT sage set forth,
    and the vṛtti explains the exclusions by chronology:
    **याज्ञवल्क्यादयोऽचिरकाला इत्याख्यानेषु वार्ता, तया व्यवहरति
    सूत्रकारः** — the story goes that they are recent, and the
    sūtra-maker goes by that.
    """

    def test_the_appeal_to_tradition_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.105").notes)
        self.assertIn("याज्ञवल्क्यादयोऽचिरकाला", notes)
        self.assertIn("इत्याख्यानेषु वार्ता", notes)
        self.assertIn("तया व्यवहरति सूत्रकारः", notes)

    def test_and_the_condition_is_on_what_the_affix_denotes(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        row = provisions_for("4.3.105")[0]
        self.assertEqual(row.result, "purāṇa-prokta-brāhmaṇa-kalpa")
        self.assertEqual(row.gives, "ṇini")
        self.assertIn("प्रत्ययार्थविशेषणमेतत्",
                      unwrapped(REGISTRY.get("4.3.105").notes))

    def test_and_the_excluded_text_is_named(self):
        self.assertIn("याज्ञवल्कानि ब्राह्मणानि",
                      unwrapped(REGISTRY.get("4.3.105").notes))


class MadeAgainstDiscovered(unittest.TestCase):
    """
    4.3.115 उपज्ञाते and 4.3.116 कृते ग्रन्थे stand one apart, and
    the vṛtti separates them: **उत्पादितं कृतम्, विद्यमानमेव ज्ञातम्
    उपज्ञातम्** — what is made is brought into being, what is
    discovered was already there.
    """

    def test_the_distinction_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.116").notes)
        self.assertIn("उत्पादितं कृतम्", notes)
        # ज्ञातम् + उपज्ञातम् is ज्ञातमुपज्ञातम्; the virāma goes.
        self.assertIn("विद्यमानमेव ज्ञातमुपज्ञातम्", notes)

    def test_and_discovering_is_glossed_as_finding_out_unaided(self):
        notes = unwrapped(REGISTRY.get("4.3.115").notes)
        self.assertIn("विनोपदेशेन ज्ञातमुपज्ञातम्", notes)
        # स्वयमभिसंबुद्धम् + इत्यर्थः swallows the virāma.
        self.assertIn("स्वयमभिसंबुद्धमित्यर्थः", notes)

    def test_and_the_two_senses_stay_apart_in_the_table(self):
        from src.astadhyayi.kala_taddhita import born_in

        found = born_in(case="tṛtīyā", sense="upajñāta")
        made = born_in(case="tṛtīyā", sense="kṛta", result="grantha")
        self.assertEqual(found.by, "4.3.115")
        self.assertEqual(made.by, "4.3.116")

    def test_and_the_grammar_itself_is_the_worked_example(self):
        """
        पाणिनिनोपज्ञातं **पाणिनीयमकालकं व्याकरणम्** — the tenseless
        grammar Pāṇini found out for himself. A rule of the text
        describing the text.
        """
        self.assertIn("पाणिनीयमकालकं व्याकरणम्",
                      unwrapped(REGISTRY.get("4.3.115").notes))


class TheWidestSenseAndWhatItCosts(unittest.TestCase):
    """
    4.3.120 तस्येदम्. **अणादयः पञ्च महोत्सर्गाः** — five great
    general rules stand behind it — and the vṛtti says what the
    breadth costs: everything but the relation is left out of
    account.
    """

    def test_the_five_general_rules_are_named(self):
        self.assertIn("अणादयः पञ्च महोत्सर्गाः",
                      unwrapped(REGISTRY.get("4.3.120").notes))

    def test_and_what_is_not_meant_is_listed(self):
        notes = unwrapped(REGISTRY.get("4.3.120").notes)
        self.assertIn("षष्ठ्यर्थमात्रं तत्संबन्धिमात्रं च विवक्षितम्",
                      notes)
        self.assertIn("लिङ्गसंख्याप्रत्यक्षपरोक्षादिकं", notes)
        self.assertIn("सर्वमविवक्षितम्", notes)

    def test_and_usage_still_keeps_something_out(self):
        """
        **अनन्तरादिष्वनभिधानाद् न भवति** — the widest sense in the
        section still stops where the language does not say it. The
        same ground 4.3.12 gave, a hundred and eight sūtras earlier.
        """
        # अनन्तरादिषु + अनभिधानात् swallows the initial अ, so
        # the standalone word is not there to search for.
        self.assertIn("अनन्तरादिष्वनभिधानाद् न भवति",
                      unwrapped(REGISTRY.get("4.3.120").notes))
        self.assertIn("अनभिधानात्",
                      unwrapped(REGISTRY.get("4.3.12").notes))

    def test_and_it_names_no_affix_of_its_own(self):
        from src.astadhyayi.kala_taddhita import born_in, provisions_for

        row = provisions_for("4.3.120")[0]
        self.assertEqual(row.gives, "")
        self.assertEqual(row.case, "ṣaṣṭhī")
        self.assertEqual(born_in(case="ṣaṣṭhī", sense="idam").by,
                         "4.3.120")


class OneRegisterOrTheOtherOrNeither(unittest.TestCase):
    """
    छन्दसि confines a rule to the Veda and भाषा to the spoken
    language, and a rule is in one, the other, or neither. One column
    with three values rather than two flags, on the argument that put
    बह्वच् and द्व्यच् together: two booleans would let a row claim
    both.
    """

    def test_both_registers_are_used_and_named(self):
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        used = {row.usage for row in KALA_TABLE if row.usage}
        self.assertEqual(used, {"chandasi", "bhāṣā"})

    def test_and_each_is_opened_by_a_rule_that_states_it(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.19")[0].usage, "chandasi")
        self.assertEqual(provisions_for("4.3.143")[0].usage, "bhāṣā")
        self.assertIn("छन्दसि", unwrapped(REGISTRY.get("4.3.19").notes))
        # भाषायाम् + अभक्ष्य is भाषायामभक्ष्य, so the standalone
        # word survives only in the counter-example question.
        self.assertIn("भाषायामिति किम्",
                      unwrapped(REGISTRY.get("4.3.143").notes))

    def test_and_the_vedic_rule_has_a_spoken_counterexample(self):
        """
        भाषायामिति किम्? **बैल्वः खादिरो वा यूपः** — a Vedic
        sacrificial post is what the spoken-language rule cannot
        reach, and the counter-example is quoted from a Śrauta text.
        """
        notes = unwrapped(REGISTRY.get("4.3.143").notes)
        self.assertIn("भाषायामिति किम्", notes)
        self.assertIn("बैल्वः खादिरो वा यूपः", notes)

    def test_and_the_register_separates_the_answers(self):
        from src.astadhyayi.kala_taddhita import born_in

        spoken = born_in(sense="vikāra", case="ṣaṣṭhī",
                         usage="bhāṣā", result="abhakṣya-ācchādana")
        self.assertEqual(spoken.by, "4.3.143")
        self.assertEqual(spoken.gives, "mayaṭ")

        anywhere = born_in(sense="vikāra", case="ṣaṣṭhī",
                           result="abhakṣya-ācchādana")
        self.assertNotEqual(anywhere.by, "4.3.143")


class TheSameFormulaTwiceInOnePada(unittest.TestCase):
    """
    **विकारावयवयोर्युगपदधिकारोऽपवादविधानार्थः, कृतनिर्देशौ हि तौ** at
    4.3.135, and 4.3.66 said the identical thing of भव and व्याख्यान
    sixty-nine sūtras earlier. Two headings deliberately overlapped so
    that their exceptions need stating once — twice in one pāda and
    nowhere else in the project so far.
    """

    def test_the_second_pair_is_opened_by_a_conjunction_too(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        opened = provisions_for("4.3.135")[0]
        self.assertEqual(opened.sense, "avayava")
        self.assertEqual(opened.also_sense, "vikāra")
        self.assertEqual(provisions_for("4.3.134")[0].sense, "vikāra")

    def test_and_the_run_under_it_answers_under_either(self):
        from src.astadhyayi.kala_taddhita import KALA_TABLE, born_in

        run = [row for row in KALA_TABLE
               if row.also_sense == "vikāra" or row.sense == "vikāra"
               and row.also_sense]
        self.assertGreaterEqual(len(run), 6)

    def test_and_the_condition_the_opener_sets_does_work_later(self):
        """
        **अप्राण्यादित्वाद् नावयवे** — 4.3.138 is refused the PART
        sense because neither of its bases names a living thing, a
        herb or a tree. The condition 4.3.135 stated, biting three
        sūtras on.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.138")[0].sense, "vikāra")
        self.assertEqual(provisions_for("4.3.138")[0].also_sense, "")
        self.assertIn("अप्राण्यादित्वाद् नावयवे",
                      unwrapped(REGISTRY.get("4.3.138").notes))

    def test_and_the_opener_says_what_holds_from_here_on(self):
        self.assertIn("इत उत्तरे प्रत्ययाः",
                      unwrapped(REGISTRY.get("4.3.135").notes))
        self.assertIn("अन्येभ्यस्तु विकारमात्रे",
                      unwrapped(REGISTRY.get("4.3.135").notes))


class OneOptionDoingOppositeWork(unittest.TestCase):
    """
    4.3.141 पलाशादिभ्यो वा. **उभयत्र विभाषेयम्** — for four members
    of the list the affix was already coming by the rule before and
    the option lets it go; for the rest it was not coming and the
    option brings it. The same word denying and granting, depending
    which entry it lands on.
    """

    def test_the_argument_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.141").notes)
        self.assertIn("उभयत्र विभाषेयम्", notes)
        # ...स्पन्दनानाम् + अनुदात्तादि swallows the initial अ.
        self.assertIn("नामनुदात्तादित्वात् प्राप्ते", notes)
        self.assertIn("अन्येषामप्राप्ते", notes)

    def test_and_the_rule_it_leans_on_gives_the_same_affix(self):
        """
        The four members were reached by 4.3.140 अनुदात्तादेश्च, and
        that rule must give what this one gives, or letting it go
        would change the form rather than remove it.
        """
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.140")[0].gives,
                         provisions_for("4.3.141")[0].gives)
        self.assertEqual(provisions_for("4.3.140")[0].accent,
                         "anudāttādi")

    def test_and_only_this_rule_is_optional_in_the_run(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertTrue(provisions_for("4.3.141")[0].optional)
        for sutra in ("4.3.139", "4.3.140", "4.3.142"):
            with self.subTest(sutra=sutra):
                self.assertFalse(provisions_for(sutra)[0].optional)


class ARefusalThatNamesItsTargetByInheritance(unittest.TestCase):
    """
    4.3.130 न दण्डमाणवान्तेवासिषु names no affix in its own words.
    **गोत्रग्रहणमिहानुवर्तते, तेन वुञ्प्रतिषेधो विज्ञायते** — the
    lineage-word carries into it, and that is how one knows it is
    4.3.126's वुञ् that is withheld and nothing else.
    """

    def test_the_argument_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.130").notes)
        self.assertIn("गोत्रग्रहणमिहानुवर्तते", notes)
        self.assertIn("वुञ्प्रतिषेधो विज्ञायते", notes)

    def test_and_the_row_refuses_the_affix_that_rule_gives(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        refusal = provisions_for("4.3.130")[0]
        supplier = provisions_for("4.3.126")[0]
        self.assertTrue(refusal.refuses)
        self.assertEqual(refusal.gives, supplier.gives)
        self.assertEqual(refusal.of_samjna, supplier.of_samjna)

    def test_and_the_answer_comes_by_the_supplier(self):
        from src.astadhyayi.kala_taddhita import born_in

        answer = born_in(sense="idam", case="ṣaṣṭhī",
                         samjna="gotra-caraṇa",
                         result="daṇḍamāṇava-antevāsin")
        self.assertEqual(answer.by, "4.3.126")
        self.assertEqual(answer.blocked_by, "4.3.130")
        self.assertEqual(answer.gives, "")

    def test_and_every_refusal_here_names_what_it_withholds(self):
        """
        The pāda has two. 4.3.130 identifies its target by the word
        it INHERITS; 4.3.151 takes back what the rule immediately
        before it gave. Both name the affix in their row, so both
        have a supplier to answer by — which is the property that
        matters, and the one that survives a third arriving.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        refusing = [row for row in KALA_TABLE if row.refuses]
        self.assertEqual({row.sutra for row in refusing},
                         {"4.3.130", "4.3.151"})
        for row in refusing:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(row.gives)

    def test_and_the_second_one_takes_back_its_neighbour_s_gift(self):
        """
        **द्व्यचश्छन्दसि इति प्राप्तः प्रतिषिध्यते** — 4.3.151 refuses
        precisely what 4.3.150 gave, one sūtra earlier, on the same
        two conditions.
        """
        from src.astadhyayi.kala_taddhita import born_in, provisions_for

        given = provisions_for("4.3.150")[0]
        taken = provisions_for("4.3.151")[0]
        self.assertEqual(given.gives, taken.gives)
        self.assertEqual(given.vowels, taken.vowels)
        self.assertEqual(given.usage, taken.usage)

        answer = born_in(sense="vikāra", case="ṣaṣṭhī",
                         samjna="utvat", vowels="dvyac",
                         usage="chandasi")
        self.assertEqual(answer.by, "4.3.150")
        self.assertEqual(answer.blocked_by, "4.3.151")


class ARuleReachingBackOverItsOwnHeading(unittest.TestCase):
    """
    4.3.145 गोश्च पुरीषे sits inside the विकार/अवयव headings and is
    stated in neither: **पुरीषं न विकारो नाप्यवयवः, तस्येदंविषये
    विधानम्** — dung is neither a modification of the cow nor a part
    of her, so the rule reaches back to 4.3.120's sense.
    """

    def test_the_reasoning_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.145").notes)
        self.assertIn("पुरीषं न विकारो नाप्यवयवः", notes)
        self.assertIn("तस्येदंविषये विधानम्", notes)

    def test_and_the_row_states_the_older_sense(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertEqual(provisions_for("4.3.145")[0].sense, "idam")
        self.assertEqual(provisions_for("4.3.120")[0].sense, "idam")
        self.assertEqual(provisions_for("4.3.144")[0].sense, "vikāra")

    def test_and_the_rule_it_names_has_arrived(self):
        """
        **विकारावयवयोस्तु गोपयसोर्यतं वक्ष्यति** — for those two
        senses 4.3.160 gives यत् instead. That rule was not codified
        when this one was, and the test said so as the exact
        shortfall; it is codified now, fifteen sūtras on.
        """
        from src.astadhyayi.corpus import collate

        self.assertIn("गोपयसोर्यतं वक्ष्यति",
                      unwrapped(REGISTRY.get("4.3.145").notes))
        self.assertIn("4.3.160", collate())
        self.assertTrue(REGISTRY.has("4.3.160"))

    def test_and_the_two_rules_divide_one_word_between_them(self):
        """
        गो takes मयट् for dung by 4.3.145 and यत् for a modification
        or a part by 4.3.160. One base, two rules, and the sense is
        the whole of what separates them.
        """
        from src.astadhyayi.kala_taddhita import born_in

        dung = born_in("go", sense="idam", case="ṣaṣṭhī",
                       result="purīṣa")
        self.assertEqual(dung.by, "4.3.145")
        self.assertEqual(dung.gives, "mayaṭ")

        made_of = born_in("go", sense="vikāra", case="ṣaṣṭhī")
        self.assertEqual(made_of.by, "4.3.160")
        self.assertEqual(made_of.gives, "yat")


class TwoWaysOfTakingAnAffixAway(unittest.TestCase):
    """
    4.3.167: **लुकि प्राप्ते लुपो विधाने युक्तवद्भावे
    स्त्रीप्रत्ययश्रवणे च विशेषः** — लुक् was already available and
    लुप् is enjoined instead, because under लुप् 1.2.51 makes what is
    left agree with the word the affix stood on and the feminine
    affix is still heard.

    The clearest statement of that distinction the project has met,
    and the reason the table needed a second column for removal.
    """

    def test_the_distinction_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.167").notes)
        self.assertIn("युक्तवद्भावे स्त्रीप्रत्ययश्रवणे च विशेषः",
                      notes)
        self.assertIn("लुकि प्राप्ते", notes)

    def test_and_the_rule_that_had_the_lukacute_is_codified(self):
        from src.astadhyayi.kala_taddhita import provisions_for

        self.assertTrue(provisions_for("4.3.163")[0].elides)
        self.assertFalse(provisions_for("4.3.163")[0].lup)
        self.assertIn("4.3.163", provisions_for("4.3.167")[0].excepts)

    def test_and_the_two_removals_are_in_separate_columns(self):
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        removing = [row for row in KALA_TABLE if row.elides]
        lopped = {row.sutra for row in removing if row.lup}
        self.assertEqual(lopped, {"4.3.166", "4.3.167"})
        for row in removing:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(row.elides or not row.lup)

    def test_and_the_answer_says_which_removal_it_was(self):
        from src.astadhyayi.kala_taddhita import born_in

        luk = born_in(sense="vikāra", case="ṣaṣṭhī", result="phala",
                      elided=True)
        self.assertEqual(luk.by, "4.3.163")
        self.assertTrue(luk.elided)
        self.assertFalse(luk.lopped)

        lup = born_in(sense="vikāra", case="ṣaṣṭhī",
                      gana="harītakyādi", result="phala", elided=True)
        self.assertEqual(lup.by, "4.3.167")
        self.assertTrue(lup.lopped)

    def test_and_gender_and_number_part_company(self):
        """
        **अत्र च व्यक्तिर्युक्तवद्भावेनेष्यते, वचनं त्वभिधेयवदेव
        भवति** — हरीतक्याः फलानि **हरीतक्यः**: feminine because the
        tree is, plural because the fruits are.
        """
        notes = unwrapped(REGISTRY.get("4.3.167").notes)
        self.assertIn("व्यक्तिर्युक्तवद्भावेनेष्यते", notes)
        self.assertIn("वचनं त्वभिधेयवदेव भवति", notes)
        self.assertTrue(REGISTRY.has("1.2.51"))


class AConditionStatedAbstractlyAndThenEnumerated(unittest.TestCase):
    """
    4.3.155 is stated of any base ending in a ञित् affix given in
    these two senses — and the vṛtti does not leave the reader to work
    out which affixes those are. It names six rules by number.

    Which makes the condition checkable: every rule listed must give
    an affix marked with ञ्, or the rule would not reach what the
    vṛtti says it reaches.
    """

    def test_the_six_rules_are_held_as_data(self):
        from src.astadhyayi.kala_taddhita import NIT_AFFIX_RULES

        self.assertEqual(len(NIT_AFFIX_RULES), 6)
        self.assertEqual(len(set(NIT_AFFIX_RULES)), 6)

    def test_and_every_one_of_them_is_codified(self):
        from src.astadhyayi.kala_taddhita import NIT_AFFIX_RULES

        for sutra in NIT_AFFIX_RULES:
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))

    def test_and_every_one_of_them_gives_a_nit_affix(self):
        """
        The claim the list makes. अञ्, ट्लञ्, वुञ्, ढञ्, यञ् — each
        carries the ञ् that 4.3.155's condition is stated on.
        """
        from src.astadhyayi.kala_taddhita import (NIT_AFFIX_RULES,
                                                  provisions_for)

        for sutra in NIT_AFFIX_RULES:
            affixes = {row.gives for row in provisions_for(sutra)
                       if row.gives}
            affixes |= {a for row in provisions_for(sutra)
                        for a in row.also_gives}
            with self.subTest(sutra=sutra, gives=sorted(affixes)):
                self.assertTrue(affixes)
                self.assertTrue(any("ñ" in a for a in affixes))

    def test_and_every_one_of_them_is_in_these_two_senses(self):
        """
        **विकारावयवप्रत्ययः** — the affix has to have been given in
        the modification or the part sense. A ञित् affix from
        anywhere else does not count, which is what तत्प्रत्ययात्
        says and बैदमयम् shows.
        """
        from src.astadhyayi.kala_taddhita import (NIT_AFFIX_RULES,
                                                  provisions_for)

        for sutra in NIT_AFFIX_RULES:
            senses = {row.sense for row in provisions_for(sutra)}
            senses |= {row.also_sense for row in provisions_for(sutra)}
            with self.subTest(sutra=sutra):
                self.assertTrue(senses & {"vikāra", "avayava"})
        self.assertIn("बैदमयम्",
                      unwrapped(REGISTRY.get("4.3.155").notes))


class AThirdAtidesaReachingForward(unittest.TestCase):
    """
    4.3.156 क्रीतवत् परिमाणात् borrows a whole section of the fifth
    chapter — **प्राग्वतेष्ठञ् इत्यत आरभ्य क्रीतार्थे ये प्रत्ययाः
    परिमाणाद् विहिताः, ते विकारेऽतिदिश्यन्ते** — and
    **वतिः सर्वसादृश्यार्थः**, in the same words 4.2.34 used.
    """

    def test_the_borrowing_is_on_record(self):
        notes = unwrapped(REGISTRY.get("4.3.156").notes)
        self.assertIn("ते विकारेऽतिदिश्यन्ते", notes)
        self.assertIn("वतिः सर्वसादृश्यार्थः", notes)

    def test_and_the_same_words_were_used_two_padas_back(self):
        self.assertIn("सर्वसादृश्यपरिग्रहार्थम्",
                      unwrapped(REGISTRY.get("4.2.34").notes))

    def test_and_the_borrowing_now_reaches_a_rule_that_exists(self):
        """
        The debt is paid. 5.1.18 opens the section this rule borrows,
        and it is codified — so the अतिदेश stops naming its target
        and starts fetching from it.

        The vṛtti's own examples are the check, and each comes from a
        different rule of that section: निष्कस्य विकारो **नैष्किकः**
        by 5.1.20's ठक्, शतस्य विकारः **शत्यः** by 5.1.21's, and a
        bare measure by the ठञ् of 5.1.18 itself, since 5.1.19 keeps
        परिमाण out of its ठक्.
        """
        from src.astadhyayi.corpus import collate
        from src.astadhyayi.kala_taddhita import born_in, provisions_for

        self.assertEqual(provisions_for("4.3.156")[0].borrows_from,
                         "5.1.18")
        self.assertIn("5.1.18", collate())
        self.assertTrue(REGISTRY.has("5.1.18"))

        answer = born_in(sense="vikāra", case="ṣaṣṭhī",
                         samjna="parimāṇa")
        self.assertEqual(answer.by, "4.3.156")
        self.assertEqual(answer.gives, "ṭhañ")

        for stem, gana, extra, affix in (
                ("niṣka", "niṣkādi", {}, "ṭhak"),
                ("śata", "", {"result": "aśata"}, "ṭhan")):
            with self.subTest(stem=stem):
                got = born_in(stem, gana=gana, sense="vikāra",
                              case="ṣaṣṭhī", samjna="parimāṇa",
                              **extra)
                self.assertEqual(got.by, "4.3.156")
                self.assertEqual(got.gives, affix)

    def test_and_the_affix_it_fetches_is_named_in_the_answer(self):
        """
        An अतिदेश answers with its OWN id, since the borrowing is
        what it does — but the rule it borrowed from has to be
        visible, or the answer would hide where the affix came from.
        """
        from src.astadhyayi.kala_taddhita import born_in

        answer = born_in("niṣka", gana="niṣkādi", sense="vikāra",
                         case="ṣaṣṭhī", samjna="parimāṇa")
        self.assertEqual(answer.by, "4.3.156")
        self.assertIn("The affix is borrowed from 5.1.20",
                      answer.why)

    def test_and_a_likeness_takes_in_the_elision_too(self):
        """
        **वतिः सर्वसादृश्यार्थः** — the वति takes in EVERY likeness,
        so 5.1.28's removal of the affix is borrowed along with the
        affixes: द्विनिष्कः beside द्विनैष्किकः.

        The borrowed answer therefore has no affix in it, and that is
        the rule working rather than a gap.
        """
        from src.astadhyayi.kala_taddhita import born_in

        answer = born_in("niṣka", gana="niṣkādi", pre="dvi-tri",
                         sense="vikāra", case="ṣaṣṭhī",
                         samjna="parimāṇa")
        self.assertEqual(answer.by, "4.3.156")
        self.assertEqual(answer.gives, "")
        self.assertIn("The affix is borrowed from 5.1.30",
                      answer.why)
        self.assertIn("वतिः सर्वसादृश्यार्थः",
                      unwrapped(REGISTRY.get("4.3.156").notes))

    def test_and_a_number_counts_as_a_measure(self):
        self.assertIn("संख्यापि परिमाणग्रहणेन गृह्यते",
                      unwrapped(REGISTRY.get("4.3.156").notes))


class ThePadaIsFinished(unittest.TestCase):
    """
    अध्याय ४ पाद ३ — all 168, and the Kāśikā's colophon closes it.
    """

    def test_all_of_it_is_codified(self):
        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 3}
        self.assertEqual(have, set(range(1, 169)))

    def test_and_the_corpus_agrees_on_how_many_there_are(self):
        """
        Checked against the collation and not against a typed count.
        """
        from src.astadhyayi.corpus import collate

        in_corpus = {int(k.rsplit(".", 1)[1]) for k in collate()
                     if k.startswith("4.3.")}
        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 3}
        self.assertEqual(have, in_corpus)

    def test_and_the_colophon_is_on_the_last_rule(self):
        self.assertIn("चतुर्थाध्यायस्य तृतीयः पादः",
                      unwrapped(REGISTRY.get("4.3.168").notes))

    def test_and_every_rule_of_it_has_a_row(self):
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        stated = {int(row.sutra.rsplit(".", 1)[1]) for row in KALA_TABLE}
        self.assertEqual(stated, set(range(1, 169)))

    def test_and_the_pada_used_six_case_relations(self):
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        cases = {row.case for row in KALA_TABLE if row.case}
        self.assertEqual(len(cases), 6)


class EveryRowIsReachableAndBelongsToARule(unittest.TestCase):
    """
    A row no query can reach is a rule the project has written down
    and cannot run.
    """

    def test_every_row_answers_by_its_own_sutra(self):
        from src.astadhyayi.kala_taddhita import KALA_TABLE, born_in

        for row in KALA_TABLE:
            where = {"sense": row.sense}
            if row.of:
                where["stem"] = row.of[0]
            if row.gana:
                where["gana"] = row.gana
            if row.case:
                where["case"] = row.case
            if row.result:
                where["result"] = row.result
            if row.of_samjna:
                where["samjna"] = row.of_samjna
            if row.pre:
                where["pre"] = row.pre
            if row.stem_final:
                where["stem_final"] = row.stem_final
            if row.usage:
                where["usage"] = row.usage
            if row.before:
                where["before"] = row.before
            if row.vowels:
                where["vowels"] = row.vowels
            if row.accent:
                where["accent"] = row.accent
            if row.upadha:
                where["upadha"] = row.upadha
            if row.elides:
                where["elided"] = True
            if row.gives:
                where["wants"] = row.gives
            with self.subTest(sutra=row.sutra, **where):
                answer = born_in(**where)
                if row.refuses:
                    # A प्रतिषेध answers by the rule that supplies,
                    # with its own id on `excepts`. 4.3.130 refuses
                    # 4.3.126's वुञ् and says so by inheriting the
                    # word that names it.
                    self.assertIn(row.sutra, answer.excepts)
                    self.assertEqual(answer.gives, "")
                    continue
                self.assertEqual(answer.by, row.sutra)
                if row.elides:
                    # 4.3.34–37 take the affix away, so there is
                    # nothing for the answer to name.
                    self.assertTrue(answer.elided)
                    self.assertEqual(answer.gives, "")

    def test_every_affix_a_rule_also_gives_is_reachable_too(self):
        """
        4.3.1 gives three affixes and 4.3.23 two. Asking after the
        second or third has to reach the same rule, or the rule is
        only half codified.
        """
        from src.astadhyayi.kala_taddhita import KALA_TABLE, born_in

        asked = 0
        for row in KALA_TABLE:
            for affix in row.also_gives:
                where = {"sense": row.sense, "wants": affix}
                if row.of:
                    where["stem"] = row.of[0]
                if row.of_samjna:
                    where["samjna"] = row.of_samjna
                if row.pre:
                    where["pre"] = row.pre
                if row.stem_final:
                    where["stem_final"] = row.stem_final
                if row.result:
                    where["result"] = row.result
                if row.vowels:
                    where["vowels"] = row.vowels
                if row.accent:
                    where["accent"] = row.accent
                with self.subTest(sutra=row.sutra, wants=affix):
                    self.assertEqual(born_in(**where).by, row.sutra)
                    asked += 1
        self.assertGreater(asked, 4)

    def test_every_row_belongs_to_a_codified_sutra(self):
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        for row in KALA_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(REGISTRY.has(row.sutra))

    def test_and_the_pada_is_contiguous_as_far_as_it_is_read(self):
        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 3}
        self.assertEqual(have, set(range(1, max(have) + 1)))

    def test_and_every_rule_read_so_far_has_a_row(self):
        from src.astadhyayi.kala_taddhita import KALA_TABLE

        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 3}
        stated = {int(row.sutra.rsplit(".", 1)[1]) for row in KALA_TABLE}
        self.assertEqual(stated, have)


if __name__ == "__main__":
    unittest.main()
