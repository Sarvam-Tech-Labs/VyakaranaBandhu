# -*- coding: utf-8 -*-
"""
५.३.१–२७ — प्राग्दिशो विभक्तिः, and a heading that names rather than
supplies.

Six headings of this project have been bounded by lifting a word out
of the rule they stop at, and all six supplied an AFFIX. This one
supplies a saṃjñā and gives nothing at all — and with it the समर्थ
heading that has governed since 2.1.1 lapses, because these affixes
add nothing to what the base already means.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.sutra import REGISTRY
from src.astadhyayi.svarthika import (SVARTHIKA_TABLE, VIBHAKTI_MARKER,
                                      VIBHAKTI_RUN, WHY_THE_NAME,
                                      in_own_sense, provisions_for,
                                      vibhakti_run)
from tests import unwrapped


class AHeadingThatSuppliesAName(unittest.TestCase):
    """
    5.3.1 is bounded exactly as the affix-headings were, and gives
    nothing.
    """

    def test_it_is_bounded_by_a_word_from_the_rule_it_stops_at(self):
        """
        **प्रागेतस्माद् दिक्संशब्दनाद् यानित ऊर्ध्वम्
        अनुक्रमिष्यामो विभक्तिसंज्ञास्ते वेदितव्याः** — the same
        device 4.1.83, 4.4.1, 4.4.75, 5.1.1 and 5.1.18 used, and
        the word lifted is दिक् out of 5.3.27.
        """
        self.assertEqual(VIBHAKTI_MARKER, "5.3.27")
        self.assertEqual(VIBHAKTI_RUN, ("5.3.1", "5.3.26"))
        self.assertTrue(REGISTRY.has(VIBHAKTI_MARKER))
        self.assertIn("दिक्संशब्दनाद्",
                      unwrapped(REGISTRY.get("5.3.1").notes))

    def test_and_it_gives_no_affix(self):
        row = provisions_for("5.3.1")[0]
        self.assertTrue(row.heading)
        self.assertEqual(row.gives, "")
        self.assertEqual(row.also_gives, ())
        self.assertEqual(vibhakti_run().affix, "")

    def test_and_nothing_answers_by_default_because_of_that(self):
        """
        Every heading before this one could be the fall-back when no
        rule was reached. This one cannot, and the resolver says so
        rather than naming a rule.
        """
        answer = in_own_sense("vṛkṣa", case="pañcamī")
        self.assertEqual(answer.affix, "")
        self.assertEqual(answer.sutra, "")
        self.assertIn("NAME and not an affix", answer.why)

    def test_and_the_name_is_given_for_two_stated_consequences(self):
        """
        **तसिलादीनां विभक्तित्वे प्रयोजनं त्यदादिविधयः, इदमो
        विभक्तिस्वरश्च** — a saṃjñā is worth giving only for what
        follows from it, and the vṛtti names both.
        """
        notes = unwrapped(REGISTRY.get("5.3.1").notes)
        self.assertIn("त्यदादिविधयः", notes)
        self.assertIn("इदमो विभक्तिस्वर", notes)
        self.assertEqual(len(WHY_THE_NAME), 2)
        for reason in WHY_THE_NAME:
            with self.subTest(reason=reason):
                self.assertTrue(reason.strip())

    def test_and_one_of_the_two_is_used_by_a_rule_of_the_section(self):
        """
        5.3.8 replaces one affix by another of the same shape, and
        says why: **तसेस्तसिल्वचनं स्वरार्थं विभक्त्यर्थं च** — for
        the accent and for the NAME. The two reasons 5.3.1 gave,
        put to work seven rules later.
        """
        notes = unwrapped(REGISTRY.get("5.3.8").notes)
        self.assertIn("स्वरार्थं विभक्त्यर्थं च", notes)
        self.assertEqual(provisions_for("5.3.8")[0].gives, "tasil")
        self.assertEqual(provisions_for("5.3.8")[0].adesa, "tasi")


class WhereTheSamarthaHeadingStops(unittest.TestCase):
    """
    2.1.1 समर्थः पदविधिः has governed since the second chapter. It
    lapses here, and the vṛtti says exactly why.
    """

    def test_the_reason_is_that_the_affixes_add_no_meaning(self):
        """
        **अतः परं स्वार्थिकाः प्रत्ययाः, तेषु समर्थाधिकारः
        प्रथमग्रहणं च प्रतियोग्यपेक्षत्वाद् नोपयुज्यत इति द्वयमपि
        निवृत्तम्** — a word can only be *construed with* something
        if there is a something, and a स्वार्थिक affix adds none.
        """
        notes = unwrapped(REGISTRY.get("5.3.1").notes)
        self.assertIn("स्वार्थिकाः प्रत्ययाः", notes)
        self.assertIn("द्वयमपि निवृत्तम्", notes)
        self.assertIn("प्रतियोग्यपेक्षत्वाद्", notes)

    def test_and_the_one_word_that_does_carry_on(self):
        """
        **वावचनं तु वर्तत एव, तेन विकल्पेन तसिलादयो भवन्ति** — so
        कुतः stands beside कस्मात्, and the ordinary case-ending is
        never displaced outright.
        """
        self.assertIn("वावचनं तु वर्तत एव",
                      unwrapped(REGISTRY.get("5.3.1").notes))
        self.assertIn("कस्मात्",
                      unwrapped(REGISTRY.get("5.3.1").notes))

    def test_and_no_row_of_the_section_states_a_second_word(self):
        """
        In 4.1 to 5.2 a row's `case` was the relation the base bore
        to another word. Here it is a condition on the base itself —
        which ending it carries — and no row names anything for the
        base to be construed with.
        """
        for row in SVARTHIKA_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertIn(row.case,
                              ("", "pañcamī", "saptamī", "ṣaṣṭhī",
                               "saptamī-prathamā",
                               "saptamī-pañcamī-prathamā"))


class TheBasesTheWholeSectionWorksOn(unittest.TestCase):
    """
    5.3.2 names them, and every rule of the stretch that names none
    of its own inherits them.
    """

    def test_the_numerals_are_kept_out_by_name(self):
        row = provisions_for("5.3.2")[0]
        self.assertIn("dvi", row.excludes)
        self.assertIn("dvyādi", row.excludes)
        self.assertIn("द्वाभ्याम्", row.keeps_out)

    def test_and_an_ordinary_noun_reaches_nothing(self):
        """
        **प्रकृतिपरिसंख्यानं किम्?** वृक्षात्, वृक्षे — the rule
        names its bases so that ordinary nouns get their ordinary
        endings and no affix of this section.
        """
        self.assertIn("वृक्षात्", provisions_for("5.3.2")[0].keeps_out)
        self.assertEqual(in_own_sense("vṛkṣa", case="saptamī").affix,
                         "")

    def test_and_one_base_is_named_though_it_need_not_be(self):
        """
        **सर्वनामत्वादेव सिद्धे किमो ग्रहणं द्व्यादिपर्युदासात्** —
        किम् is a सर्वनामन् already; it is named because the
        exclusion of द्वि and the rest would otherwise have taken it
        out with them.
        """
        self.assertIn("सर्वनामत्वादेव सिद्धे किमो ग्रहणं",
                      unwrapped(REGISTRY.get("5.3.2").notes))

    def test_and_another_is_read_as_a_numeral(self):
        """
        **बहुग्रहणे संख्याग्रहणम्; इह न भवति — बहोः सूपात्** — बहु
        is taken in its NUMERAL sense, so *from much soup* gets
        nothing.
        """
        notes = unwrapped(REGISTRY.get("5.3.2").notes)
        self.assertIn("बहुग्रहणे संख्याग्रहणम्", notes)
        self.assertIn("बहोः सूपात्",
                      provisions_for("5.3.2")[0].keeps_out)


class SubstitutionsYokedToTheAffixesTheyPrecede(unittest.TestCase):
    """
    Four rules of the opening replace a base, and each says what
    kind of replacement it is.
    """

    def test_two_of_them_replace_the_whole_word(self):
        """
        **शकारः सर्वादेशार्थः** at 5.3.3 and 5.3.5 — the श in the
        substitute's name is what makes 1.1.55 replace the whole
        word instead of its last sound.
        """
        for sutra, adesa in (("5.3.3", "iś"), ("5.3.5", "aś")):
            with self.subTest(sutra=sutra):
                self.assertEqual(provisions_for(sutra)[0].adesa,
                                 adesa)
                self.assertIn("शकारः सर्वादेशार्थः",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_two_are_conditioned_on_the_affix_that_follows(self):
        """
        5.3.4 before र and थ, 5.3.6 before द — and the second is the
        one that shows why the condition is *an affix of THIS
        section*: **सर्वं ददातीति सर्वदा ब्राह्मणी** is a verb.
        """
        self.assertEqual(provisions_for("5.3.4")[0].before, "r-th")
        self.assertEqual(provisions_for("5.3.6")[0].before, "d")
        self.assertIn("सर्वं ददातीति सर्वदा ब्राह्मणी",
                      provisions_for("5.3.6")[0].keeps_out)

    def test_and_the_substitution_shows_in_the_answer(self):
        etarhi = in_own_sense("idam", case="saptamī", result="kāla")
        self.assertEqual(etarhi.affix, "rhil")
        self.assertEqual(etarhi.sutra, "5.3.16")
        replacing = in_own_sense("idam", before="r-th")
        self.assertEqual(replacing.adesa, "eta-ita")
        self.assertEqual(replacing.sutra, "5.3.4")


class AWordDraggedBackwardInsteadOfForward(unittest.TestCase):
    """
    अनुवृत्ति carries a word forward. 5.3.12 takes one BACKWARD out
    of the rule after it — and 5.2.81 did the same.
    """

    def test_the_borrowing_is_stated(self):
        """
        **त्रलमपि केचिदिच्छन्ति; तत् कथम्? उत्तरसूत्राद् वावचनं
        पुरस्तादपकृष्यते** — some want कुत्र as well, and the
        *optionally* of 5.3.13 is pulled back to allow it.
        """
        notes = unwrapped(REGISTRY.get("5.3.12").notes)
        self.assertIn("उत्तरसूत्राद् वावचनं पुरस्तादपकृष्यते", notes)
        self.assertTrue(provisions_for("5.3.12")[0].optional)

    def test_and_the_other_place_it_happened(self):
        """
        5.2.81 pulled संज्ञा backward from 5.2.82 —
        **उत्तरसूत्राद् इह संज्ञाग्रहणम् अपकृष्यते**. Two
        instances, both from the immediately following rule.
        """
        self.assertIn("उत्तरसूत्राद् इह संज्ञाग्रहणम् अपकृष्यते",
                      unwrapped(REGISTRY.get("5.2.81").notes))


class ARuleTheCommentaryCallsIdle(unittest.TestCase):
    """
    5.3.19 gives दा after तद्, which 5.3.15 has already given it.
    """

    def test_the_vrtti_says_so_and_does_not_explain_it_away(self):
        """
        **तदो दावचनमनर्थकम्, विहितत्वात्** — and nothing follows.
        Elsewhere a needless statement is read as a ज्ञापक; here it
        is simply left standing as needless.
        """
        self.assertIn("तदो दावचनमनर्थकम्, विहितत्वात्",
                      unwrapped(REGISTRY.get("5.3.19").notes))
        self.assertIn("tad", provisions_for("5.3.15")[0].of)
        self.assertEqual(provisions_for("5.3.15")[0].gives, "dā")

    def test_and_the_rule_still_has_its_own_affix_to_give(self):
        """
        The दा is idle; the दानीम् the च brings in is not, and
        asking for it reaches this rule and no other.
        """
        row = provisions_for("5.3.19")[0]
        self.assertEqual(row.also_gives, ("dānīm",))
        answer = in_own_sense("tad", case="saptamī", result="kāla",
                              wants="dānīm")
        self.assertEqual(answer.sutra, "5.3.19")


class TheRulesAreOnRecord(unittest.TestCase):
    """All 119 of the pāda, contiguous, each with a note."""

    def test_all_of_them_are_codified(self):
        have = {sutra.id.number for sutra in REGISTRY.all()
                if sutra.id.adhyaya == 5 and sutra.id.pada == 3}
        self.assertEqual(have, set(range(1, 120)))

    def test_and_every_row_names_a_sutra_the_corpus_has(self):
        from src.astadhyayi.corpus import collate

        witnesses = collate()
        for row in SVARTHIKA_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertIn(row.sutra, witnesses)

    def test_and_every_exception_points_at_a_rule_of_the_table(self):
        stated = {row.sutra for row in SVARTHIKA_TABLE}
        for row in SVARTHIKA_TABLE:
            for target in row.excepts:
                with self.subTest(sutra=row.sutra, target=target):
                    self.assertIn(target, stated)
                    self.assertNotEqual(target, row.sutra)

    def test_every_row_supplies_something_and_there_are_four_kinds(self):
        """
        The heading, which gives a NAME; the rules that give an
        affix; the four that only replace a base; and 5.3.2, which
        gives neither — it names the BASES the whole section works
        on, and is carried down by अनुवृत्ति to every rule that
        states none of its own.

        That fourth shape is why 5.3.2 has to be in the table at all
        rather than being folded into the heading: the exclusion of
        the numerals lives on it, and so do the two remarks about
        why किम् and बहु are named.
        """
        bare = set()
        for row in SVARTHIKA_TABLE:
            with self.subTest(sutra=row.sutra):
                if not (row.heading or row.gives or row.adesa
                        or row.nipatana):
                    self.assertTrue(row.of or row.of_samjna
                                    or row.result)
                    bare.add(row.sutra)
        # 5.3.2 names the BASES the section works on; 5.3.119 names
        # the affixes of the eight rules before it. Both supply
        # something, and neither supplies an affix.
        self.assertEqual(bare, {"5.3.2", "5.3.119"})
        self.assertTrue(provisions_for("5.3.2")[0].excludes)
        self.assertEqual(provisions_for("5.3.119")[0].result,
                         "tadrāja")

    def test_and_the_laid_down_forms_say_so_in_the_vrtti(self):
        laid = {row.sutra for row in SVARTHIKA_TABLE if row.nipatana}
        for sutra in ("5.3.17", "5.3.22"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, laid)
        for sutra in laid:
            with self.subTest(sutra=sutra):
                self.assertIn("निपात्य",
                              unwrapped(REGISTRY.get(sutra).notes))



class ASecondHeadingThatDoesSupplyAnAffix(unittest.TestCase):
    """
    5.3.70 प्रागिवात्कः — bounded the same way 5.3.1 was, and giving
    क where that gave a name.
    """

    def test_it_is_bounded_and_it_closes_where_a_vrtti_says(self):
        """
        **प्रागेतस्मादिवसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामः,
        कप्रत्ययस्तेष्वधिकृतो वेदितव्यः**, and at 5.3.95
        **प्रागिवीयस्य पूर्णोऽवधिः** — the seventh time the project
        has met that formula.
        """
        from src.astadhyayi.svarthika import KA_MARKER, KA_RUN

        self.assertEqual(KA_RUN, ("5.3.70", "5.3.95"))
        self.assertEqual(KA_MARKER, "5.3.96")
        self.assertEqual(provisions_for("5.3.70")[0].gives, "ka")
        self.assertTrue(provisions_for("5.3.70")[0].heading)
        self.assertIn("प्रागिवीयस्य पूर्णोऽवधिः",
                      unwrapped(REGISTRY.get("5.3.95").notes))

    def test_and_the_two_headings_of_the_pada_differ_in_kind(self):
        """
        One supplies a NAME and one an AFFIX, and both are bounded
        by the same device. The difference shows in what the
        resolver can fall back on: nothing for the first, and the
        heading's क for the second.
        """
        from src.astadhyayi.svarthika import KA_RUN

        naming = provisions_for(VIBHAKTI_RUN[0])[0]
        supplying = provisions_for(KA_RUN[0])[0]
        self.assertTrue(naming.heading and supplying.heading)
        self.assertEqual(naming.gives, "")
        self.assertTrue(supplying.gives)

    def test_and_the_affix_it_carries_answers_a_dozen_senses(self):
        """
        अज्ञात, कुत्सित, अनुकम्पा, अल्प, ह्रस्व — one affix, and
        the sense changing at almost every rule.
        """
        for sense in ("ajñāta", "kutsita", "anukampā", "alpa",
                      "hrasva"):
            with self.subTest(sense=sense):
                answer = in_own_sense(result=sense)
                self.assertEqual(answer.affix, "ka")

    def test_and_a_finite_verb_is_kept_out_of_it(self):
        """
        **तिङन्तादयं प्रत्ययो नेष्यते, अकजिष्यते; तिङश्च
        इत्यनुवृत्तम् उत्तरसूत्रेणैव संबन्धनीयम्** — the *and after
        a finite verb* carried down from 5.3.56 attaches to 5.3.71
        and not to the heading.
        """
        notes = unwrapped(REGISTRY.get("5.3.70").notes)
        self.assertIn("तिङन्तादयं प्रत्ययो नेष्यते", notes)
        self.assertIn("उत्तरसूत्रेणैव संबन्धनीयम्", notes)


class ASubstitutionThatUndoesARestriction(unittest.TestCase):
    """
    5.3.58 confines two affixes to quality-words; 5.3.60 to 5.3.65
    then apply them to five things that are not quality-words, and
    the vṛtti says how.
    """

    def test_the_restriction_is_stated_and_its_scope_given(self):
        """
        **इष्ठन्नीयसुनावजादी सामान्येन विहितौ, तयोरयं
        विषयनियमः क्रियते** — and **एवकार इष्टतोऽवधारणार्थः,
        प्रत्ययनियमोऽयं न प्रकृतिनियम इति**: it restricts the
        AFFIX, so a quality-word may still take the others.
        """
        notes = unwrapped(REGISTRY.get("5.3.58").notes)
        self.assertIn("विषयनियमः क्रियते", notes)
        self.assertIn("प्रत्ययनियमोऽयं न प्रकृतिनियम इति", notes)
        self.assertIn("पाचकतरः",
                      provisions_for("5.3.58")[0].keeps_out)

    def test_and_the_substitutions_are_read_as_undoing_it(self):
        """
        **ननु च प्रशस्यशब्दस्य अगुणवचनत्वाद् अजादी न संभवतः? एवं
        तर्हि आदेशविधानसामर्थ्यात् तद्विषयो नियमो न प्रवर्तते —
        एवमुत्तरेष्वपि योगेषु विज्ञेयम्.** One reading, and the
        vṛtti says it holds of every rule after it.
        """
        notes = unwrapped(REGISTRY.get("5.3.60").notes)
        self.assertIn("आदेशविधानसामर्थ्यात् तद्विषयो नियमो न "
                      "प्रवर्तते", notes)
        self.assertIn("एवमुत्तरेष्वपि योगेषु विज्ञेयम्", notes)

    def test_and_the_last_of_them_reads_it_out_of_an_elision(self):
        """
        5.3.65 removes a possessive affix before those two —
        **इदमेव वचनं ज्ञापकम् अजादिसद्भावस्य**, which is the same
        move 5.2.60 made out of a लुक्.
        """
        self.assertIn("इदमेव वचनं ज्ञापकम् अजादिसद्भावस्य",
                      unwrapped(REGISTRY.get("5.3.65").notes))
        self.assertIn("इदमेव लुग्वचनं ज्ञापकं तद्विधानस्य",
                      unwrapped(REGISTRY.get("5.2.60").notes))

    def test_and_every_one_of_the_six_is_a_substitution(self):
        for sutra in ("5.3.60", "5.3.61", "5.3.62", "5.3.63",
                      "5.3.64", "5.3.65"):
            with self.subTest(sutra=sutra):
                for row in provisions_for(sutra):
                    self.assertEqual(row.gives, "")
                    self.assertTrue(row.adesa)
                    self.assertEqual(row.before, "ajādi")


class WhatTheseAffixesActuallyDo(unittest.TestCase):
    """
    5.3.55 states it, and three later rules show the consequence.
    """

    def test_the_statement(self):
        """
        **प्रकृत्यर्थविशेषणं च स्वार्थिकानां द्योत्यं भवति** — a
        qualification of the base's own meaning is what these
        affixes MAKE MANIFEST. 5.3.66 repeats it: **स्वार्थिकाश्च
        प्रत्ययाः प्रकृत्यर्थविशेषस्य द्योतका भवन्ति.**
        """
        self.assertIn("प्रकृत्यर्थविशेषणं च स्वार्थिकानां द्योत्यं",
                      unwrapped(REGISTRY.get("5.3.55").notes))
        self.assertIn("प्रकृत्यर्थविशेषस्य द्योतका भवन्ति",
                      unwrapped(REGISTRY.get("5.3.66").notes))

    def test_and_the_gender_still_comes_from_usage(self):
        """
        **स्वार्थिकत्वेऽपि पुँल्लिङ्गता, लोकाश्रयत्वाल्
        लिङ्गस्य** at 5.3.88 — कुटी is feminine and कुटीर is not,
        though the affix added nothing. 5.3.66 says the same of a
        neuter.
        """
        self.assertIn("लोकाश्रयत्वाल् लिङ्गस्य",
                      unwrapped(REGISTRY.get("5.3.88").notes))
        self.assertIn("लोकाश्रयत्वाल् लिङ्गस्य",
                      unwrapped(REGISTRY.get("5.3.66").notes))

    def test_and_the_slightness_is_of_the_quality_not_the_thing(self):
        """
        5.3.91: **यस्य गुणस्य हि भावाद् द्रव्ये शब्दनिवेशः, तस्य
        तनुत्वे प्रत्ययः** — and the vṛtti works all four bases
        out. अश्वतर is a mule: less of a HORSE because sired
        otherwise, not a smaller horse.
        """
        notes = unwrapped(REGISTRY.get("5.3.91").notes)
        self.assertIn("यस्य गुणस्य हि भावाद् द्रव्ये शब्दनिवेशः",
                      notes)
        self.assertIn("तस्य तनुत्वम् अन्यपितृकता", notes)
        self.assertIn("भारवहने मन्दशक्तिता", notes)

    def test_and_5_3_47_uses_the_same_argument_for_contempt(self):
        """
        **यस्य गुणस्य सद्भावाद् द्रव्ये शब्दनिवेशः, तस्य कुत्सायां
        प्रत्ययः** — a grammarian skilled but ill-behaved is not
        called वैयाकरणपाश, the contempt being of something other
        than his grammar.
        """
        self.assertIn("तस्य कुत्सायां प्रत्ययः",
                      unwrapped(REGISTRY.get("5.3.47").notes))


class TheCrowAndThePalmFruit(unittest.TestCase):
    """
    5.3.106 — and the vṛtti takes a proverb apart to show what the
    compound carries and what the affix does.
    """

    def test_the_figure_is_worked_out_in_full(self):
        """
        **काकस्यागमनं यादृच्छिकम्, तालस्य पतनं च; तेन तालेन पतता
        काकस्य वधः कृतः** — and the two comparisons are divided:
        **तत्र प्रथमे समासः, द्वितीये प्रत्ययः**.
        """
        notes = unwrapped(REGISTRY.get("5.3.106").notes)
        self.assertIn("काकस्यागमनं यादृच्छिकम्", notes)
        self.assertIn("तत्र प्रथमे समासः, द्वितीये प्रत्ययः", notes)
        self.assertIn("अतर्कितोपनतं चित्रीकरणमुच्यते", notes)

    def test_and_the_compound_exists_only_because_this_rule_does(self):
        """
        **समासश्चायमस्मादेव ज्ञापकात्, नह्यस्यापरं लक्षणमस्ति** —
        no rule makes काकताल a compound; that this rule takes one
        as its base is the evidence that it exists. The ज्ञापक
        device pointed at a COMPOUND rather than an affix.
        """
        self.assertIn("समासश्चायमस्मादेव ज्ञापकात्",
                      unwrapped(REGISTRY.get("5.3.106").notes))
        self.assertEqual(provisions_for("5.3.106")[0].of_samjna,
                         "iva-samāsa")


class ThePadaOpensAndClosesWithAName(unittest.TestCase):
    """
    5.3.1 gives the name विभक्ति and 5.3.119 the name तद्राज, and
    each says where the name is USED.
    """

    def test_both_name_rules_give_their_reason(self):
        """
        5.3.1: **तसिलादीनां विभक्तित्वे प्रयोजनं त्यदादिविधयः,
        इदमो विभक्तिस्वरश्च**. 5.3.119: **तद्राजप्रदेशाः —
        तद्राजस्य बहुषु० इत्येवमादयः**. A saṃjñā is worth giving
        only for what follows from it, and both rules say what.
        """
        self.assertIn("प्रयोजनं त्यदादिविधयः",
                      unwrapped(REGISTRY.get("5.3.1").notes))
        self.assertIn("तद्राजप्रदेशाः",
                      unwrapped(REGISTRY.get("5.3.119").notes))

    def test_and_the_closing_name_covers_the_rules_it_says(self):
        """
        **पूगाञ् ञ्योऽग्रामणीपूर्वात् इत्यतः प्रभृति ये प्रत्ययाः,
        ते तद्राजसंज्ञा भवन्ति** — 5.3.112 to 5.3.118, and every
        one of those rows carries that result.
        """
        for number in range(112, 119):
            sutra = "5.3.%d" % number
            with self.subTest(sutra=sutra):
                for row in provisions_for(sutra):
                    self.assertEqual(row.result, "tadrāja")
        self.assertEqual(provisions_for("5.3.111")[0].result, "iva")

    def test_and_the_last_rule_gives_no_affix_of_its_own(self):
        row = provisions_for("5.3.119")[0]
        self.assertEqual(row.gives, "")
        self.assertEqual(row.adesa, "")
        self.assertFalse(row.heading)
        self.assertEqual(row.result, "tadrāja")

    def test_and_the_colophon_closes_the_pada(self):
        self.assertIn("पञ्चमाध्यायस्य तृतीयः पादः",
                      unwrapped(REGISTRY.get("5.3.119").notes))
        last = max(int(row.sutra.rsplit(".", 1)[1])
                   for row in SVARTHIKA_TABLE)
        self.assertEqual(last, 119)


if __name__ == "__main__":
    unittest.main()
