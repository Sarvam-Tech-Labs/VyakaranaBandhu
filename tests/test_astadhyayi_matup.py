# -*- coding: utf-8 -*-
"""
५.२.१–२८ — a pāda with no heading standing over it.

5.1 was seven headings deep and every rule of it stood under one.
This pāda opens with none: each rule names its own affix and its own
sense, and the senses do not run in families. So the tests here are
not about ranges and displacement — they are about what the vṛtti
says the words MEAN, and about the five rules that lay a whole form
down rather than deriving it.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.matup import (MATUP_TABLE, provisions_for,
                                  what_comes)
from src.astadhyayi.sutra import REGISTRY
from tests import unwrapped


class NoHeadingStandsOverThisPada(unittest.TestCase):
    """
    The difference from 5.1 is structural, and the resolver has to
    show it: a question that reaches no rule reaches nothing.
    """

    def test_the_pada_has_one_heading_and_it_comes_late(self):
        """
        Nothing stands over the first ninety-three rules. 5.2.94
        तदस्यास्त्यस्मिन्निति मतुप् is the pāda's only heading, and
        it governs from there to the end.
        """
        headings = {row.sutra for row in MATUP_TABLE if row.heading}
        self.assertEqual(headings, {"5.2.94"})
        for row in MATUP_TABLE:
            if int(row.sutra.rsplit(".", 1)[1]) < 94:
                with self.subTest(sutra=row.sutra):
                    self.assertFalse(row.heading)

    def test_and_an_unreached_question_gets_no_affix(self):
        """
        Where 5.1 always had a heading to fall back on, here the
        honest answer is that nothing supplies — and the answer says
        so rather than naming a rule.
        """
        answer = what_comes("aśīti", sense="bhavana")
        self.assertEqual(answer.affix, "")
        self.assertEqual(answer.sutra, "")
        self.assertIn("no heading", answer.why)

    def test_and_almost_every_rule_names_a_sense_of_its_own(self):
        """
        In 5.1 a sense was shared by a run of rules and the question
        was which affix won. Here a sense usually belongs to one
        rule, and where two rules DO share one they are the general
        rule and its exceptions.
        """
        shared = {}
        for row in MATUP_TABLE:
            if row.sense:
                shared.setdefault(row.sense, set()).add(row.sutra)
        many = {sense: sutras for sense, sutras in shared.items()
                if len(sutras) > 1}
        alone = [sense for sense, sutras in shared.items()
                 if len(sutras) == 1]
        self.assertGreater(len(alone), len(many))

        # The largest group by far is अस्ति, and it is the one that
        # DOES have a heading over it — 5.2.94, which every rule of
        # it after that point excepts. That is what makes it unlike
        # the rest of the pāda.
        biggest = max(many, key=lambda sense: len(many[sense]))
        self.assertEqual(biggest, "asti")
        for sutra in sorted(many["asti"] - {"5.2.94"}):
            number = int(sutra.rsplit(".", 1)[1])
            if number < 94:
                continue
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                heading = provisions_for("5.2.94")[0]
                if row.gives == heading.gives:
                    # 5.2.95 and 5.2.136 give the heading's OWN
                    # affix, so they restate it rather than
                    # displacing it — and both vṛttis say the
                    # restatement is to shut other affixes out.
                    self.assertIn(sutra, {"5.2.95", "5.2.136"})
                    continue
                # Otherwise the heading, or a rule that in turn
                # displaces it: 5.2.105 excepts 5.2.104, which
                # excepts 5.2.94.
                reached = set(row.excepts)
                for target in row.excepts:
                    reached |= set(provisions_for(target)[0].excepts)
                self.assertIn("5.2.94", reached)

        # And the second-largest, पूरण, has no heading: every rule
        # of it after the first is tied to 5.2.48 by an augment on
        # the affix it gave or by an affix stated in its place.
        for sutra in sorted(many["pūraṇa"] - {"5.2.48"}):
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                if row.gives == provisions_for("5.2.48")[0].gives:
                    self.assertTrue(row.adesa, sutra)
                else:
                    self.assertIn("5.2.48", row.excepts)


class TheCommentaryGlossesRatherThanArgues(unittest.TestCase):
    """
    Where 5.1's vṛttis fixed the limits of headings, 5.2's explain
    what the words in the rules mean — because nothing else will.
    """

    def test_five_words_are_glossed_by_taking_them_apart(self):
        for sutra, gloss in (
                ("5.2.1", "भवन्ति जायन्तेऽस्मिन्निति भवनम्"),
                ("5.2.18", "गावस्तिष्ठन्त्यस्मिन्निति गोष्ठम्"),
                ("5.2.15", "गोः पश्चाद् अनुगु"),
                ("5.2.6", "दृश्यतेऽस्मिन्निति दर्शनः"),
                ("5.2.19", "एकाहेन गम्यत इत्येकाहगमः")):
            with self.subTest(sutra=sutra):
                self.assertIn(gloss,
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_a_word_from_a_board_game_gets_the_longest_gloss(self):
        """
        **अयः प्रदक्षिणम्, अनयः प्रसव्यम्;
        प्रदक्षिणप्रसव्यगामिनां शाराणां यस्मिन् परशारैः पदानाम्
        असमावेशः सोऽयानयः** — the square the opponent's pieces
        cannot reach.
        """
        notes = unwrapped(REGISTRY.get("5.2.9").notes)
        self.assertIn("अयः प्रदक्षिणम्, अनयः प्रसव्यम्", notes)
        self.assertIn("फलकशिरसि स्थित इत्यर्थः", notes)

    def test_and_a_troop_is_defined_before_the_rule_can_apply(self):
        """
        **नानाजातीया अनियतवृत्तय उत्सेधजीविनः संघा व्राताः** — and
        the definition decides the rule's scope: **तेषामेव
        व्रातानाम् अन्यतम उच्यते; यस्त्वन्यस् तदीयेन जीवति, तत्र
        नेष्यते.**
        """
        notes = unwrapped(REGISTRY.get("5.2.21").notes)
        self.assertIn("उत्सेधजीविनः संघा व्राताः", notes)
        self.assertIn("उत्सेधः शरीरम्", notes)
        self.assertTrue(provisions_for("5.2.21")[0].keeps_out)


class FiveFormsLaidDownRatherThanDerived(unittest.TestCase):
    """
    निपातन — and the vṛtti twice says outright that the derivation
    offered is a courtesy.
    """

    def test_every_laid_down_form_says_so_in_the_vrtti(self):
        """
        The property, not the list: a row marked as a निपातन is one
        whose vṛtti uses that word, and there is no other way into
        the column.
        """
        laid = {row.sutra for row in MATUP_TABLE if row.nipatana}
        self.assertGreater(len(laid), 5)
        for sutra in laid:
            with self.subTest(sutra=sutra):
                self.assertIn("निपात्य",
                              unwrapped(REGISTRY.get(sutra).notes))
        for sutra in ("5.2.13", "5.2.14", "5.2.20", "5.2.22",
                      "5.2.23"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, laid)

    def test_and_two_of_them_disclaim_their_own_analysis(self):
        """
        **शालीनकौपीने अधृष्टाकार्ययोः पर्यायौ यथाकथंचिद्
        व्युत्पादयितव्यौ** at 5.2.20, and at 5.2.28 the same of the
        quality-words: **नात्र प्रकृतिप्रत्ययार्थयोर् अभिनिवेशः.**

        The same warning 5.1.59 gave of the numerals, and it is what
        marks a laid-down form off from a derived one.
        """
        self.assertIn("यथाकथंचिद् व्युत्पादयितव्यौ",
                      unwrapped(REGISTRY.get("5.2.20").notes))
        self.assertIn("नात्र प्रकृतिप्रत्ययार्थयोर",
                      unwrapped(REGISTRY.get("5.2.28").notes))
        self.assertIn("नात्रावयवार्थे",
                      unwrapped(REGISTRY.get("5.1.59").notes))

    def test_and_one_of_them_carries_a_whole_contract(self):
        """
        **आगवीनः कर्मकरः, यो गवा भृतः कर्म करोति आ तस्य गोः
        प्रत्यर्पणात्** — a hired man who works for a cow, UNTIL
        the cow is handed over. The आ of the compound is the term.
        """
        row = provisions_for("5.2.14")[0]
        self.assertTrue(row.nipatana)
        self.assertEqual(row.pre, "āṅ")
        self.assertEqual(row.of, ("go",))
        self.assertIn("आ तस्य गोः प्रत्यर्पणात्",
                      unwrapped(REGISTRY.get("5.2.14").notes))

    def test_and_a_cerebral_sound_is_evidence_of_a_sense(self):
        """
        5.2.13's अवष्टब्धे: **आविदूर्ये हि मूर्धन्यो विधीयते** —
        8.3.68 gives the cerebral only in the sense of NEARNESS, so
        the spelling of the word in the sūtra proves what the rule
        is about.
        """
        self.assertIn("आविदूर्ये हि मूर्धन्यो विधीयते",
                      unwrapped(REGISTRY.get("5.2.13").notes))
        self.assertEqual(provisions_for("5.2.13")[0].sense,
                         "avaṣṭabdha")


class ACompoundWhoseMembersDoNotAgree(unittest.TestCase):
    """
    5.2.5 सर्वचर्मणः — the *all* belongs to the affix's sense and
    not to the leather, so the two words have no relation and are
    compounded anyway.
    """

    def test_the_vrtti_names_the_irregularity(self):
        """
        **सर्वशब्दश्चात्र प्रत्ययार्थेन कृतेन संबध्यते, न चर्मणा।
        तत्रायम् असमर्थसमासो द्रष्टव्यः; सर्वश्चर्मणा कृत इत्येतस्मिन्
        वाक्यार्थे वृत्तिः** — the compound holds the sense of the
        whole sentence and not of its own two parts.
        """
        notes = unwrapped(REGISTRY.get("5.2.5").notes)
        self.assertIn("असमर्थसमासो द्रष्टव्यः", notes)
        self.assertIn("वाक्यार्थे वृत्तिः", notes)

    def test_and_the_rule_still_gives_two_affixes(self):
        answer = what_comes("sarvacarman", sense="kṛta",
                            case="tṛtīyā")
        self.assertEqual(answer.affix, "kha")
        self.assertEqual(answer.also_gives, ("khañ",))


class WhereAConjunctionPilesAffixesUp(unittest.TestCase):
    """
    5.2.16 gives two and 5.2.17 adds a third by a च, so one base
    ends with three forms.
    """

    def test_the_later_rule_keeps_both_of_the_earlier(self):
        two = provisions_for("5.2.16")[0]
        three = provisions_for("5.2.17")[0]
        self.assertEqual(two.gives, "yat")
        self.assertEqual(two.also_gives, ("kha",))
        self.assertEqual(three.gives, "cha")
        self.assertEqual(three.also_gives, ("yat", "kha"))
        self.assertEqual(three.excepts, ("5.2.16",))

    def test_and_both_rules_serve_the_same_sense(self):
        for sutra in ("5.2.15", "5.2.16", "5.2.17"):
            with self.subTest(sutra=sutra):
                self.assertEqual(provisions_for(sutra)[0].sense,
                                 "alaṃgāmī")

    def test_and_asking_for_one_of_the_three_reaches_the_rule(self):
        for affix in ("cha", "yat", "kha"):
            with self.subTest(affix=affix):
                answer = what_comes("abhyamitra", sense="alaṃgāmī",
                                    case="dvitīyā", wants=affix)
                self.assertEqual(answer.sutra, "5.2.17")


class PartOfARuleCarriesOnWithoutTheRest(unittest.TestCase):
    """
    5.2.24 names two senses in one breath and 5.2.25 takes only one
    of them down.
    """

    def test_the_maxim_is_quoted_where_it_is_used(self):
        """
        **मूलग्रहणम् अनुवर्तते, न पाकग्रहणम्,
        एकयोगनिर्दिष्टानाम् अप्येकदेशोऽनुवर्तते** — even of things
        named in a single rule, a PART may carry on alone.
        """
        self.assertIn("एकयोगनिर्दिष्टानाम् अप्येकदेशोऽनुवर्तते",
                      unwrapped(REGISTRY.get("5.2.25").notes))

    def test_and_the_rows_show_which_part_carried(self):
        senses = {row.sense for row in provisions_for("5.2.24")}
        self.assertEqual(senses, {"pāka", "mūla"})
        self.assertEqual(provisions_for("5.2.25")[0].sense, "mūla")
        self.assertEqual(provisions_for("5.2.25")[0].excepts,
                         ("5.2.24",))


class TheRulesAreOnRecord(unittest.TestCase):
    """All 140 of the pāda, contiguous, each with a note."""

    def test_all_of_them_are_codified(self):
        have = {sutra.id.number for sutra in REGISTRY.all()
                if sutra.id.adhyaya == 5 and sutra.id.pada == 2}
        self.assertEqual(have, set(range(1, 141)))

    def test_and_every_row_names_a_sutra_the_corpus_has(self):
        from src.astadhyayi.corpus import collate

        witnesses = collate()
        for row in MATUP_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertIn(row.sutra, witnesses)

    def test_and_every_exception_points_at_a_rule_of_the_table(self):
        stated = {row.sutra for row in MATUP_TABLE}
        for row in MATUP_TABLE:
            for target in row.excepts:
                with self.subTest(sutra=row.sutra, target=target):
                    self.assertIn(target, stated)
                    self.assertNotEqual(target, row.sutra)

    def test_and_a_row_that_gives_nothing_lays_a_form_down(self):
        """
        Every rule here supplies something, and where the `gives`
        column is empty it is because the whole FORM was laid down
        instead of an affix being named.
        """
        for row in MATUP_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(row.gives or row.nipatana)

    def test_and_the_yathasankhya_rules_state_a_row_apiece(self):
        """
        Where a rule matches affixes to bases in order, each pairing
        is a row of its own — otherwise the table would have to be
        read alongside the sūtra to be understood.
        """
        for sutra in ("5.2.9", "5.2.10", "5.2.24", "5.2.27"):
            with self.subTest(sutra=sutra):
                rows = provisions_for(sutra)
                self.assertGreater(len(rows), 1)
                # Each pairing is distinguished by what it applies
                # to AND what it means, since 5.2.24 pairs two gaṇas
                # with two senses and names no individual word.
                pairs = [(row.of, row.gana, row.sense)
                         for row in rows]
                self.assertEqual(len(pairs), len(set(pairs)))



class OneSutraCarryingEightSupplements(unittest.TestCase):
    """
    5.2.29 gives one affix to four preverbs and then the vārttikas
    pile on, each with an affix of its own for a different sense.
    """

    def test_the_supplements_are_on_record(self):
        notes = unwrapped(REGISTRY.get("5.2.29").notes)
        for varttika in ("रजस्युपसंख्यानम्", "संघाते कटज्",
                         "विस्तारे पटज्", "द्वित्वे गोयुगच्",
                         "षट्त्वे षड्गवच्", "विकारे स्नेहे तैलच्"):
            with self.subTest(varttika=varttika):
                self.assertIn(varttika, notes)

    def test_and_one_of_them_repeats_a_sense_from_the_first_rule(self):
        """
        **भवने क्षेत्र इक्ष्वादिभ्यः शाकटशाकिनौ** — the same sense
        5.2.1 opened the pāda with, twenty-eight rules later and
        with different affixes.
        """
        self.assertIn("भवने क्षेत्र इक्ष्वादिभ्यः",
                      unwrapped(REGISTRY.get("5.2.29").notes))
        self.assertEqual(provisions_for("5.2.1")[0].sense, "bhavana")

    def test_and_the_rule_itself_gathers_a_fourth_preverb_by_a_ca(self):
        row = provisions_for("5.2.29")[0]
        self.assertEqual(row.of, ("sam", "pra", "ud", "vi"))
        self.assertIn("चकाराद् वेश्च",
                      unwrapped(REGISTRY.get("5.2.29").notes))


class ThreeRulesForTheShapeOfANose(unittest.TestCase):
    """
    5.2.31 to 5.2.33 — seven affixes in three rules, all for a nose
    that is flat, and all under the naming-heading.
    """

    def test_the_three_share_a_sense_and_a_condition(self):
        for sutra in ("5.2.31", "5.2.32", "5.2.33"):
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                self.assertEqual(row.sense, "nata")
                self.assertEqual(row.of_samjna, "nāsikā")
                self.assertEqual(row.result, "saṃjñā")

    def test_and_the_word_names_the_nose_and_then_the_man(self):
        """
        **तद्योगाद् नासिकापि, पुरुषोऽपि तथोच्यते** — the affix is
        given for the FLATNESS, and the nose and its owner take the
        name by association.
        """
        self.assertIn("तद्योगाद् नासिकापि, पुरुषोऽपि तथोच्यते",
                      unwrapped(REGISTRY.get("5.2.31").notes))

    def test_and_a_use_outside_the_rule_is_sent_to_comparison(self):
        """
        **कथं निबिडाः केशाः, निबिडं वस्त्रम्? उपमानाद् भविष्यति** —
        thick hair is not covered and is not made an exception; it
        is explained as a figure instead.
        """
        self.assertIn("उपमानाद् भविष्यति",
                      unwrapped(REGISTRY.get("5.2.32").notes))

    def test_and_the_last_of_them_substitutes_as_well_as_supplies(self):
        row = provisions_for("5.2.33")[0]
        self.assertEqual(row.adesa, "cika-ci")
        self.assertEqual(row.gives, "inac")
        self.assertIn("piṭac", row.also_gives)
        answer = what_comes("ni", sense="nata", result="saṃjñā",
                            samjna="nāsikā", wants="inac")
        self.assertEqual(answer.sutra, "5.2.33")
        self.assertEqual(answer.adesa, "cika-ci")

    def test_and_a_supplement_corrects_the_scope_of_another(self):
        """
        **क्लिन्नस्य चिल्पिल्लश्चास्य चक्षुषी** gives a form for
        running eyes, and the vṛtti at once withdraws its *of him*:
        **अस्येत्यनेन नार्थः; चक्षुषोरेवाभिधाने प्रत्यय इष्यते.**
        """
        notes = unwrapped(REGISTRY.get("5.2.33").notes)
        self.assertIn("अस्येत्यनेन नार्थः", notes)
        self.assertIn("चक्षुषोरेवाभिधाने प्रत्यय इष्यते", notes)


class AHeadingThatBlocksAnOperation(unittest.TestCase):
    """
    5.2.34 stands under संज्ञायाम्, and the vṛtti uses that heading
    for two separate jobs.
    """

    def test_it_makes_the_two_senses_definite(self):
        """
        **संज्ञाधिकाराच्च नियतविषयमासन्नारूढं गम्यते** — not any
        nearness, but the ground at a mountain's foot.
        """
        self.assertIn("नियतविषयमासन्नारूढं गम्यते",
                      unwrapped(REGISTRY.get("5.2.34").notes))
        senses = {row.sense for row in provisions_for("5.2.34")}
        self.assertEqual(senses, {"āsanna", "ārūḍha"})

    def test_and_it_stops_a_shortening_that_would_otherwise_apply(self):
        """
        **प्रत्ययस्थात् कात् पूर्वस्य इति इत्वमत्र न भवति,
        संज्ञाधिकारादेव** — 7.3.44 would shorten the आ before the
        क, and the naming-heading is what keeps उपत्यका as it is.
        """
        self.assertIn("इत्वमत्र न भवति, संज्ञाधिकारादेव",
                      unwrapped(REGISTRY.get("5.2.34").notes))


class MeasureAndExtentAreNotTheSame(unittest.TestCase):
    """
    5.2.37 gives three affixes for प्रमाण and 5.2.39 another for
    परिमाण, and a kārikā explains why both words are needed.
    """

    def test_the_three_measure_affixes_are_divided_by_a_verse(self):
        """
        **प्रथमश्च द्वितीयश्च ऊर्ध्वमाने मतौ मम** — the first two
        for HEIGHT, and **मात्रच् पुनरविशेषेण** for any measure.
        """
        row = provisions_for("5.2.37")[0]
        self.assertEqual(row.gives, "dvayasac")
        self.assertEqual(row.also_gives, ("daghnac", "mātrac"))
        notes = unwrapped(REGISTRY.get("5.2.37").notes)
        self.assertIn("ऊर्ध्वमाने मतौ मम", notes)
        self.assertIn("मात्रच् पुनरविशेषेण", notes)

    def test_and_the_later_rule_states_its_word_though_one_is_running(self):
        """
        **प्रमाणग्रहणेऽनुवर्तमाने परिमाणग्रहणं प्रमाणपरिमाणयोर्
        भेदात्** — and the kārikā's reason is kept with the rule.
        """
        self.assertIn("डावतावर्थवैशेष्यान्",
                      unwrapped(REGISTRY.get("5.2.39").notes))
        self.assertEqual(provisions_for("5.2.37")[0].sense,
                         "pramāṇa")
        self.assertEqual(provisions_for("5.2.39")[0].sense,
                         "parimāṇa")

    def test_and_a_substitution_proves_an_affix_nobody_enjoined(self):
        """
        5.2.40 replaces the व of वतुप् after किम् and इदम् — but no
        rule had given those two the affix. **एतदेव चादेशविधानं
        ज्ञापकं किमिदंभ्यां वतुप् प्रत्ययो भवतीति**: the
        substitution is the evidence that it does.
        """
        notes = unwrapped(REGISTRY.get("5.2.40").notes)
        self.assertIn("एतदेव चादेशविधानं ज्ञापकं", notes)
        self.assertEqual(provisions_for("5.2.40")[0].gives, "vatup")
        self.assertEqual(provisions_for("5.2.40")[0].adesa, "gha")

    def test_and_a_number_used_in_contempt_is_kept_out(self):
        """
        5.2.41 says संख्यापरिमाणे and not just संख्यायाम्, and the
        vṛtti gives the reason: **क्षेपे हि परिच्छेदो नास्ति —
        केयमेषां संख्या दशानाम्.**
        """
        notes = unwrapped(REGISTRY.get("5.2.41").notes)
        self.assertIn("क्षेपे हि परिच्छेदो नास्ति", notes)
        self.assertIn("केयमेषां संख्या दशानाम्",
                      provisions_for("5.2.41")[0].keeps_out)


class WhyARuleNamesTheAffixItReplaces(unittest.TestCase):
    """
    5.2.43 could have given अयज् outright and instead makes it a
    SUBSTITUTE for तयप्. The vṛtti says what turns on that.
    """

    def test_the_reason_is_what_the_substitute_inherits(self):
        """
        **तयग्रहणं स्थानिनिर्देशार्थम्; अन्यथा प्रत्ययान्तरमयज्
        विज्ञायेत** — and then **त्रयी गतिरिति तयनिबन्धन ईकारो न
        स्यात्**, the feminine ई that hangs on तय would be lost,
        and 1.1.33 would not apply.
        """
        notes = unwrapped(REGISTRY.get("5.2.43").notes)
        self.assertIn("तयग्रहणं स्थानिनिर्देशार्थम्", notes)
        self.assertIn("तयनिबन्धन ईकारो न स्यात्", notes)

    def test_and_the_rows_record_it_as_a_substitution(self):
        for sutra in ("5.2.43", "5.2.44"):
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                self.assertEqual(row.adesa, "ayaj")
                self.assertEqual(row.excepts, ("5.2.42",))
        self.assertTrue(provisions_for("5.2.43")[0].optional)
        self.assertFalse(provisions_for("5.2.44")[0].optional)


class ConditionsThatAreNowhereInTheRule(unittest.TestCase):
    """
    5.2.45 and 5.2.47 each carry restrictions no word of the sūtra
    states, and each vṛtti says where they come from.
    """

    def test_the_first_gets_its_two_from_the_word_iti(self):
        """
        **इतिकरणो विवक्षार्थ इत्युक्तम्, तत इदं सर्वं लभ्यते** —
        that the excess be of the same kind, and the thing exceeded
        a hundred or a thousand. A kārikā sums both.
        """
        notes = unwrapped(REGISTRY.get("5.2.45").notes)
        self.assertIn("समानजातीये प्रकृत्यर्थे", notes)
        self.assertIn("शतसहस्रयोश्चेष्यते", notes)
        self.assertIn("अधिके समानजाताविष्टं शतसहस्रयोः", notes)

    def test_and_the_second_has_four_of_them(self):
        """
        **गुणस्येति चैकत्वं विवक्षितम्**, **भूयसश्च वाचिकायाः
        संख्यायाः**, **गुणशब्दः समानावयववचनः**, and **निमान इति
        किम्?** — one kind of part, more than one, parts of equal
        size, and a price rather than a proportion.
        """
        notes = unwrapped(REGISTRY.get("5.2.47").notes)
        for condition in ("गुणस्येति चैकत्वं विवक्षितम्",
                          "भूयसश्च वाचिकायाः",
                          "गुणशब्दः समानावयववचनः",
                          "निमान इति किम्"):
            with self.subTest(condition=condition):
                self.assertIn(condition, notes)

    def test_and_the_affix_names_the_whole_rather_than_the_part(self):
        """
        Twice over. 5.2.42: **सामर्थ्यादवयवी प्रत्ययार्थो
        विज्ञायते**. 5.2.47: **भागेऽपि तु विधीयमानः प्रत्ययः
        प्राधान्येन भागवन्तमाचष्टे**.
        """
        self.assertIn("अवयवी प्रत्ययार्थो विज्ञायते",
                      unwrapped(REGISTRY.get("5.2.42").notes))
        self.assertIn("प्राधान्येन भागवन्तमाचष्टे",
                      unwrapped(REGISTRY.get("5.2.47").notes))


class TheOrdinalsAndWhatFillsACount(unittest.TestCase):
    """
    5.2.48 and 5.2.49 — and the ordinal is defined by what its
    arrival BRINGS ABOUT, not by what it completes.
    """

    def test_the_definition_excludes_a_pot_five_handfuls_fill(self):
        """
        **यस्मिन्नुपसंजाते अन्या संख्या संपद्यते, स प्रत्ययार्थः**
        — so **इह न भवति — पञ्चानां मुष्टिकानां पूरणो घटः**.
        """
        notes = unwrapped(REGISTRY.get("5.2.48").notes)
        self.assertIn("अन्या संख्या संपद्यते", notes)
        self.assertIn("पञ्चानां मुष्टिकानां पूरणो घटः",
                      provisions_for("5.2.48")[0].keeps_out)

    def test_and_the_insert_rule_creates_the_case_it_needs(self):
        """
        **नान्तादिति पञ्चमी डट आगमसंबन्धे षष्ठीं प्रकल्पयति** — an
        आगम belongs TO something, so the ablative in the rule is
        turned into the genitive that relation requires.
        """
        self.assertIn("आगमसंबन्धे षष्ठीं प्रकल्पयति",
                      unwrapped(REGISTRY.get("5.2.49").notes))
        row = provisions_for("5.2.49")[0]
        self.assertEqual(row.adesa, "maṭ")
        self.assertEqual(row.gives, provisions_for("5.2.48")[0].gives)

    def test_and_both_of_its_conditions_have_a_counter_example(self):
        self.assertIn("विंशः", provisions_for("5.2.49")[0].keeps_out)
        self.assertIn("एकादशः",
                      provisions_for("5.2.49")[0].keeps_out)
        plain = what_comes(samjna="saṃkhyā", sense="pūraṇa",
                           case="ṣaṣṭhī")
        inserted = what_comes(samjna="saṃkhyā", stem_final="n",
                              sense="pūraṇa", case="ṣaṣṭhī")
        self.assertEqual(plain.sutra, "5.2.48")
        self.assertEqual(inserted.sutra, "5.2.49")
        self.assertEqual(plain.adesa, "")
        self.assertEqual(inserted.adesa, "maṭ")



class ARuleThatOnlyAddsProvesTheRuleThatGave(unittest.TestCase):
    """
    Four times in this stretch the Kāśikā reads an affix out of a
    rule that merely adds to it. The pattern is the same each time:
    5.2.48 gives the ordinal affix after a NUMERAL, and here are
    words that are not numerals with augments enjoined on that very
    affix — so they must have had it.
    """

    def test_the_reading_is_made_at_four_places(self):
        for sutra, phrase in (
                ("5.2.51", "कतिपयशब्दो न संख्या"),
                ("5.2.52", "पूगसंघशब्दयोरसंख्यात्वाद्"),
                ("5.2.57", "मासादयः संख्याशब्दा न भवन्ति"),
                ("5.2.60", "इदमेव लुग्वचनं ज्ञापकं तद्विधानस्य")):
            with self.subTest(sutra=sutra):
                notes = unwrapped(REGISTRY.get(sutra).notes)
                self.assertIn(phrase, notes)
                self.assertIn("ज्ञापक", notes)

    def test_and_the_fourth_reads_it_out_of_a_REMOVAL(self):
        """
        5.2.60 is the sharpest of the four: no rule gives a chapter
        or a section the affix, and this rule takes it away. **केन
        पुनरध्यायानुवाकयोः प्रत्ययः? इदमेव लुग्वचनं ज्ञापकं
        तद्विधानस्य** — an elision is evidence of what it elides.
        """
        notes = unwrapped(REGISTRY.get("5.2.60").notes)
        self.assertIn("केन पुनरध्यायानुवाकयोः प्रत्ययः", notes)
        self.assertIn("विकल्पेन च लुगयमिष्यते", notes)
        self.assertTrue(provisions_for("5.2.60")[0].optional)

    def test_and_a_substitution_did_the_same_ten_rules_earlier(self):
        """
        5.2.40 read वतुप् out of a substitution in its व. Four
        augments, one elision and one substitution — six rules in
        this pāda whose real content is what they presuppose.
        """
        self.assertIn("एतदेव चादेशविधानं ज्ञापकं",
                      unwrapped(REGISTRY.get("5.2.40").notes))


class TheAugmentsOnOneAffix(unittest.TestCase):
    """
    5.2.49 to 5.2.58 — seven rules adding seven different augments
    to the one ordinal affix, and the rows have to show it is the
    same affix throughout.
    """

    def test_every_one_of_them_gives_the_affix_of_5_2_48(self):
        base = provisions_for("5.2.48")[0].gives
        for sutra in ("5.2.49", "5.2.50", "5.2.51", "5.2.52",
                      "5.2.53", "5.2.56", "5.2.57", "5.2.58"):
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                self.assertEqual(row.gives, base)
                self.assertTrue(row.adesa)
                self.assertEqual(row.sense, "pūraṇa")

    def test_and_the_two_that_replace_it_are_told_apart(self):
        """
        5.2.54 and 5.2.55 give तीय instead — a different affix, not
        an augment — and both are exceptions to 5.2.48 itself.
        """
        for sutra in ("5.2.54", "5.2.55"):
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                self.assertEqual(row.gives, "tīya")
                self.assertEqual(row.excepts, ("5.2.48",))

    def test_and_one_augment_is_optional_and_two_are_not(self):
        """
        **विंशत्यादिभ्यः इति विकल्पेन प्राप्ते नित्यार्थम्** —
        5.2.56 makes it a choice and 5.2.57 and 5.2.58 fix it.
        """
        self.assertTrue(provisions_for("5.2.56")[0].optional)
        for sutra in ("5.2.57", "5.2.58"):
            with self.subTest(sutra=sutra):
                self.assertFalse(provisions_for(sutra)[0].optional)
                self.assertEqual(provisions_for(sutra)[0].excepts,
                                 ("5.2.56",))
        self.assertIn("विकल्पेन प्राप्ते नित्यार्थम्",
                      unwrapped(REGISTRY.get("5.2.58").notes))

    def test_and_the_list_means_the_ordinary_words(self):
        """
        **विंशत्यादयो लौकिकाः संख्याशब्दा गृह्यन्ते, न
        पङ्क्त्यादिसूत्रसंनिविष्टाः** — not the ones 5.1.59 laid
        down, because a rule naming those could not reach compounds
        ending in them, and एकविंशति would be lost.
        """
        notes = unwrapped(REGISTRY.get("5.2.56").notes)
        self.assertIn("लौकिकाः संख्याशब्दा गृह्यन्ते", notes)
        self.assertIn("विंशतिप्रभृतिभ्यो न स्यात्", notes)
        self.assertTrue(REGISTRY.has("5.1.59"))


class OneAffixThroughADozenSenses(unittest.TestCase):
    """
    कन् from 5.2.64 to 5.2.78 — skilled at it, wanting it, intent
    on it, born with it, about to take it, lately off it, acting so,
    seeking by it, chief of them. One affix, and the sense changes
    at every rule.
    """

    def test_the_run_gives_one_affix_over_many_senses(self):
        run = [row for row in MATUP_TABLE
               if 63 <= int(row.sutra.rsplit(".", 1)[1]) <= 78]
        senses = {row.sense for row in run if row.sense}
        self.assertGreater(len(senses), 8)
        giving_kan = {row.sutra for row in run if row.gives == "kan"}
        self.assertGreater(len(giving_kan), 8)

    def test_and_where_another_affix_breaks_in_it_is_an_exception(self):
        """
        5.2.67's ठक् and 5.2.76's two are the only other affixes in
        the run, and each row names what it displaces.
        """
        for sutra in ("5.2.67", "5.2.76"):
            with self.subTest(sutra=sutra):
                for row in provisions_for(sutra):
                    self.assertNotEqual(row.gives, "kan")
                    self.assertTrue(row.excepts)

    def test_and_the_one_that_carries_a_condition_says_what_it_is(self):
        """
        5.2.67's आद्यून is not a base but a further condition on
        what the affix reports: **आद्यून इति
        प्रत्ययार्थविशेषणम्** — and without it, उदरकः by 5.2.66.
        """
        self.assertIn("आद्यून इति प्रत्ययार्थविशेषणम्",
                      unwrapped(REGISTRY.get("5.2.67").notes))
        general = what_comes(samjna="svāṅga", sense="prasita",
                             case="saptamī")
        special = what_comes("udara", sense="prasita",
                             case="saptamī", result="ādyūna")
        self.assertEqual(general.affix, "kan")
        self.assertEqual(special.affix, "ṭhak")
        self.assertEqual(special.sutra, "5.2.67")

    def test_and_the_carried_affix_is_named_where_it_could_be_doubted(self):
        """
        5.2.68 stands right after a ठक् rule, and the vṛtti says
        which affix carries: **कन् प्रत्यय इत्येव स्वर्यते, न
        ठक्.**
        """
        self.assertIn("कन् प्रत्यय इत्येव स्वर्यते, न ठक्",
                      unwrapped(REGISTRY.get("5.2.68").notes))
        self.assertEqual(provisions_for("5.2.68")[0].gives, "kan")


class AnAffixOnAWordAnAffixAlreadyMade(unittest.TestCase):
    """
    5.2.77 takes a word already built by an ordinal affix and gives
    it another — optionally removing the first.
    """

    def test_the_base_is_itself_a_derived_word(self):
        row = provisions_for("5.2.77")[0]
        self.assertEqual(row.of_samjna, "pūraṇānta")
        self.assertEqual(row.sense, "svārtha")
        self.assertTrue(row.optional)
        self.assertIn("तावतां पूरणं तावतिथम्",
                      unwrapped(REGISTRY.get("5.2.77").notes))

    def test_and_the_supplement_moves_the_sense_to_the_reader(self):
        """
        The rule gives द्विकं ग्रहणम्, the READING; the vārttika
        gives षट्को देवदत्तः, the READER — **पूरणप्रत्ययस्य च
        नित्यं लुक्**, and there the removal is not optional.
        """
        notes = unwrapped(REGISTRY.get("5.2.77").notes)
        self.assertIn("षट्को देवदत्तः", notes)
        self.assertIn("पूरणप्रत्ययस्य च नित्यं लुक्", notes)

    def test_and_the_word_iti_confines_it_to_a_text(self):
        """
        **इतिकरणो विवक्षार्थः; तेन ग्रन्थविषयमेव ग्रहणं
        विज्ञायते, नान्यविषयम्** — the same job इति did at 5.1.16
        and 5.2.45.
        """
        self.assertIn("ग्रन्थविषयमेव ग्रहणं विज्ञायते",
                      unwrapped(REGISTRY.get("5.2.77").notes))
        for sutra in ("5.1.16", "5.2.45", "5.2.77"):
            with self.subTest(sutra=sutra):
                self.assertIn("इतिकरणो",
                              unwrapped(REGISTRY.get(sutra).notes))



class TheRuleForHavingSomething(unittest.TestCase):
    """
    5.2.94 तदस्यास्त्यस्मिन्निति मतुप् — and the word इति in it is
    what keeps the affix from meaning bare possession.
    """

    def test_the_seven_grounds_are_named_in_a_verse(self):
        """
        **भूमनिन्दाप्रशंसासु नित्ययोगेऽतिशायने । संसर्गे
        ऽस्तिविवक्षायां भवन्ति मतुबादयः ॥** — abundance, blame,
        praise, constant connection, excess, contact, and the bare
        wish to say *it is there*. Seven, and mere having is not
        among them.
        """
        notes = unwrapped(REGISTRY.get("5.2.94").notes)
        self.assertIn("भूमनिन्दाप्रशंसासु नित्ययोगेऽतिशायने",
                      notes)
        self.assertIn("भवन्ति मतुबादयः", notes)
        self.assertIn("इतिकरणाद् विषयनियमः", notes)

    def test_and_each_ground_has_its_own_example(self):
        notes = unwrapped(REGISTRY.get("5.2.94").notes)
        for form in ("गोमान्", "कुष्ठी", "रूपवती कन्या",
                     "क्षीरिणो वृक्षाः", "उदरिणी कन्या",
                     "दण्डी", "अस्तिमान्"):
            with self.subTest(form=form):
                self.assertIn(form, notes)

    def test_and_the_rule_governs_to_the_end_of_what_is_codified(self):
        row = provisions_for("5.2.94")[0]
        self.assertTrue(row.heading)
        self.assertEqual(row.gives, "matup")
        self.assertEqual(row.sense, "asti")
        answer = what_comes("go", sense="asti", case="prathamā")
        self.assertEqual(answer.affix, "matup")
        self.assertEqual(answer.sutra, "5.2.94")

    def test_and_a_rule_restated_to_shut_others_out(self):
        """
        5.2.95 gives मतुप् after a list the rule before already
        covered. **रसादिभ्यः पुनर्वचनम् अन्यनिवृत्त्यर्थम्; अन्ये
        मत्वर्थीया मा भूवन्** — a restatement whose whole content is
        the exclusion of affixes it does not name.
        """
        notes = unwrapped(REGISTRY.get("5.2.95").notes)
        self.assertIn("पुनर्वचनम् अन्यनिवृत्त्यर्थम्", notes)
        self.assertIn("अन्ये मत्वर्थीया मा भूवन्", notes)
        self.assertEqual(provisions_for("5.2.95")[0].gives,
                         provisions_for("5.2.94")[0].gives)

    def test_and_an_option_that_gathers_rather_than_chooses(self):
        """
        5.2.96 and 5.2.97 say अन्यतरस्याम् and the vṛtti says what
        it does: **अन्यतरस्यांग्रहणेन मतुप् समुच्चीयते न तु
        प्रत्ययो विकल्प्यते; तस्माद् अकारान्तेभ्य इनिठनौ प्रत्ययौ न
        भवतः.** So both forms stand AND two other affixes are shut
        out — which a plain option would not have done.
        """
        self.assertIn("मतुप् समुच्चीयते न तु प्रत्ययो विकल्प्यते",
                      unwrapped(REGISTRY.get("5.2.97").notes))
        for sutra in ("5.2.96", "5.2.97"):
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                self.assertEqual(row.gives, "lac")
                self.assertEqual(row.also_gives, ("matup",))
                self.assertTrue(row.optional)

    def test_and_the_limb_rule_has_two_conditions_beyond_its_words(self):
        """
        **प्राणिस्थादिति किम्?** शिखावान् प्रदीपः — a lamp's
        flame-crest. And a vārttika narrows it further:
        **प्राण्यङ्गादिति वक्तव्यम्, इह मा भूत् — चिकीर्षावान्** —
        a wish is IN a living thing but is not a LIMB of one.
        """
        notes = unwrapped(REGISTRY.get("5.2.96").notes)
        self.assertIn("प्राण्यङ्गादिति वक्तव्यम्", notes)
        self.assertIn("शिखावान् प्रदीपः",
                      provisions_for("5.2.96")[0].keeps_out)
        self.assertIn("चिकीर्षावान्",
                      provisions_for("5.2.96")[0].keeps_out)


class AWordWhoseDerivationIsDeclaredNotToMatter(unittest.TestCase):
    """
    5.2.93 gives six derivations of इन्द्रिय and then says the
    derivation is not fixed.
    """

    def test_the_rule_offers_six_and_binds_to_none(self):
        """
        **रूढिरेषा चक्षुरादीनां करणानाम्; तथा च व्युत्पत्तेर्
        अनियमं दर्शयति** — the word is the settled name of the
        senses, and the rule SHOWS that its derivation is free.
        """
        notes = unwrapped(REGISTRY.get("5.2.93").notes)
        self.assertIn("रूढिरेषा चक्षुरादीनां करणानाम्", notes)
        self.assertIn("व्युत्पत्तेरनियमं दर्शयति", notes)
        self.assertIn("सति संभवे व्युत्पत्तिर् अन्यथापि कर्तव्या",
                      notes)

    def test_and_each_of_the_six_is_free_of_the_others(self):
        """
        **वाशब्दः प्रत्येकम् अभिसंबध्यमानो विकल्पानां
        स्वातन्त्र्यं दर्शयति** — the वा goes with each severally.
        """
        self.assertIn("विकल्पानां स्वातन्त्र्यं दर्शयति",
                      unwrapped(REGISTRY.get("5.2.93").notes))
        self.assertTrue(provisions_for("5.2.93")[0].nipatana)

    def test_and_the_pada_declines_to_choose_a_third_time(self):
        """
        5.2.50 kept two readings of a rule, 5.2.92 keeps four of a
        word, 5.2.93 keeps six. **सर्वं चैतत् प्रमाणम्.**
        """
        self.assertIn("सर्वं चैतत् प्रमाणम्",
                      unwrapped(REGISTRY.get("5.2.92").notes))
        notes = unwrapped(REGISTRY.get("5.2.92").notes)
        for reading in ("जन्मान्तरशरीरम्", "क्षेत्रियं विषम्",
                        "क्षेत्रियाणि तृणानि",
                        "क्षेत्रियः पारदारिकः"):
            with self.subTest(reading=reading):
                self.assertIn(reading, notes)


class TwoRulesThatTeachAGeneralPrinciple(unittest.TestCase):
    """
    5.2.86 gives इनि after पूर्व and 5.2.87 after a stem ending in
    it. That the second is needed is the evidence for a paribhāṣā.
    """

    def test_the_split_is_read_as_a_jnapaka(self):
        """
        **योगद्वयेन चानेन पूर्वादिनिः सपूर्वाच्चेति परिभाषाद्वयं
        ज्ञाप्यते** — **व्यपदेशिवद्भावोऽप्रातिपदिकेन** and
        **ग्रहणवता प्रातिपदिकेन तदन्तविधिर्नास्ति**.
        """
        notes = unwrapped(REGISTRY.get("5.2.87").notes)
        self.assertIn("परिभाषाद्वयं ज्ञाप्यते", notes)
        self.assertIn("ग्रहणवता प्रातिपदिकेन तदन्तविधिर्नास्ति",
                      notes)

    def test_and_the_same_principle_was_read_from_5_1_20(self):
        """
        There it was **निष्कादिष्वसमासग्रहणं ज्ञापकं पूर्वत्र
        तदन्ताप्रतिषेधस्य** — the same paribhāṣā, reached from a
        rule that said असमासे where it need not have.
        """
        self.assertIn("ज्ञापकं पूर्वत्र तदन्ताप्रतिषेधस्य",
                      unwrapped(REGISTRY.get("5.1.20").notes))

    def test_and_the_rows_record_the_difference_they_turn_on(self):
        named = provisions_for("5.2.86")[0]
        ending = provisions_for("5.2.87")[0]
        self.assertEqual(named.of, ("pūrva",))
        self.assertEqual(named.uttarapada, "")
        self.assertEqual(ending.of, ())
        self.assertEqual(ending.uttarapada, "pūrva")


class ASenseSuppliedBecauseTheAffixDemandsOne(unittest.TestCase):
    """
    5.2.86's अनेन reports an AGENT, and an agent cannot exist
    without an action — so one has to be supplied from outside.
    """

    def test_the_vrtti_says_the_action_is_supplied(self):
        """
        **न च क्रियामन्तरेण कर्ता संभवतीति यां कांचित् क्रियाम्
        अध्याहृत्य प्रत्ययो विधेयः** — *having gone, or eaten, or
        drunk before*, and the rule names none of them.
        """
        notes = unwrapped(REGISTRY.get("5.2.86").notes)
        self.assertIn("न च क्रियामन्तरेण कर्ता संभवतीति", notes)
        self.assertIn("क्रियामध्याहृत्य", notes)

    def test_and_the_rule_after_it_supplies_the_action_in_the_word(self):
        """
        By 5.2.87 the action IS in the base — कृतपूर्वी, भुक्तपूर्वी
        — so the two rules differ in exactly what 5.2.86 had to
        supply from nowhere.
        """
        self.assertIn("कृतपूर्वी कटम्",
                      unwrapped(REGISTRY.get("5.2.87").notes))
        self.assertIn("पूर्वं गतमनेन भुक्तं पीतं वा",
                      unwrapped(REGISTRY.get("5.2.86").notes))

    def test_and_a_time_condition_is_read_into_another(self):
        """
        5.2.85: **इनिठनोः समानकालग्रहणम्; अद्य भुक्ते श्राद्धे
        श्वः श्राद्धिक इति प्रयोगो मा भूत्** — the eating and the
        naming must be of one time, and no word of the rule says so.
        """
        notes = unwrapped(REGISTRY.get("5.2.85").notes)
        self.assertIn("इनिठनोः समानकालग्रहणम्", notes)
        self.assertIn("श्वः श्राद्धिक इति प्रयोगो मा भूत्", notes)


class AWordPulledBackwardFromTheNextRule(unittest.TestCase):
    """
    5.2.81 has no word for *name* in it, and the vṛtti takes one
    from 5.2.82.
    """

    def test_the_borrowing_is_stated_and_its_effect_given(self):
        """
        **उत्तरसूत्राद् इह संज्ञाग्रहणम् अपकृष्यते; तेनायं
        प्रकारनियमः सर्वो लभ्यते** — अपकर्ष, a word dragged
        BACKWARD, where अनुवृत्ति carries forward. It is what makes
        द्वितीयक and चतुर्थक settled names of particular fevers
        rather than any illness of a second day.
        """
        notes = unwrapped(REGISTRY.get("5.2.81").notes)
        self.assertIn("उत्तरसूत्राद् इह संज्ञाग्रहणम् अपकृष्यते",
                      notes)
        self.assertIn("प्रकारनियमः सर्वो लभ्यते", notes)
        self.assertEqual(provisions_for("5.2.82")[0].result,
                         "prāya-saṃjñā")

    def test_and_the_case_is_left_to_the_sense_to_settle(self):
        """
        **अर्थलभ्या समर्थविभक्तिः** — the rule names a time and a
        cause and no case at all, each taking the case its own sense
        wants.
        """
        self.assertIn("अर्थलभ्या समर्थविभक्तिः",
                      unwrapped(REGISTRY.get("5.2.81").notes))
        self.assertEqual(provisions_for("5.2.81")[0].case, "")



class OneWordThatGathersRatherThanChooses(unittest.TestCase):
    """
    अन्यतरस्याम् enters at 5.2.96 and is carried to the end of the
    pāda — and everywhere it does the same unexpected job.
    """

    def test_the_carried_word_gathers_the_general_affix(self):
        """
        **अन्यतरस्यांग्रहणं मतुप्समुच्चयार्थं सर्वत्रैव
        अनुवर्तते** — so a rule giving लच् or इलच् or ण leaves
        मतुप् standing beside it rather than replacing it, and the
        rows carry मतुप् in `also_gives`.
        """
        self.assertIn("मतुप्समुच्चयार्थं सर्वत्रैव अनुवर्तते",
                      unwrapped(REGISTRY.get("5.2.99").notes))
        for sutra in ("5.2.99", "5.2.100", "5.2.101", "5.2.115",
                      "5.2.117"):
            with self.subTest(sutra=sutra):
                for row in provisions_for(sutra):
                    self.assertIn("matup", row.also_gives)

    def test_and_at_one_rule_the_two_affixes_change_places(self):
        """
        5.2.136 बलादिभ्यो मतुबन्यतरस्याम् gives मतुप् OUTRIGHT and
        the carried word then gathers the इनि instead:
        **अन्यतरस्यांग्रहणेन प्रकृत इनिः समुच्चीयते.**
        """
        row = provisions_for("5.2.136")[0]
        self.assertEqual(row.gives, "matup")
        self.assertEqual(row.also_gives, ("ini",))
        self.assertIn("प्रकृत इनिः समुच्चीयते",
                      unwrapped(REGISTRY.get("5.2.136").notes))

    def test_and_where_a_word_is_a_settled_name_it_stops(self):
        """
        5.2.108: **रूढिशब्दावेतौ; रूढिषु मतुप् पुनर्न
        विकल्प्यते** — द्युम and द्रुम are settled names, and there
        the gathering does not happen.
        """
        row = provisions_for("5.2.108")[0]
        self.assertEqual(row.also_gives, ())
        self.assertIn("रूढिषु मतुप् पुनर्न विकल्प्यते",
                      unwrapped(REGISTRY.get("5.2.108").notes))

    def test_and_where_the_sense_forbids_it_it_stops_too(self):
        """
        5.2.98's वत्सल means AFFECTIONATE and not *having a calf*.
        **न चायमर्थो मतुपि संभवतीति नित्यं लजेव भवति** — मतुप्
        cannot carry that sense, so there is no pair to gather.
        """
        for row in provisions_for("5.2.98"):
            with self.subTest(stem=row.of):
                self.assertEqual(row.also_gives, ())
        notes = unwrapped(REGISTRY.get("5.2.98").notes)
        self.assertIn("न चायमर्थो मतुपि संभवतीति", notes)
        self.assertIn("न ह्यत्र वत्सार्थोंऽसार्थो वा विद्यते",
                      notes)

    def test_and_one_rule_says_the_word_twice_over_for_two_jobs(self):
        """
        5.2.109 asks why अन्यतरस्याम् is stated when one is already
        running. **मतुप्समुच्चयार्थं तदित्युक्तम्; अनेन त्विनिठनौ
        प्राप्येते; ततश्च आतूरूप्यं भवति** — the carried one
        gathers मतुप्, the stated one lets इनि and ठन् in, and four
        forms stand.
        """
        row = provisions_for("5.2.109")[0]
        self.assertEqual(row.gives, "va")
        self.assertEqual(row.also_gives, ("ini", "ṭhan", "matup"))
        self.assertIn("अनेन त्विनिठनौ प्राप्येते",
                      unwrapped(REGISTRY.get("5.2.109").notes))


class ARuleStatedForSomethingItDoesNotGive(unittest.TestCase):
    """
    Five rules of this stretch give an affix that was coming anyway,
    and each vṛtti says what the rule is really for.
    """

    def test_each_of_them_names_its_own_purpose(self):
        for sutra, purpose in (
                ("5.2.102", "बाधा मा भूदिति"),
                ("5.2.118", "नित्यग्रहणं मतुपो बाधनार्थम्"),
                ("5.2.128", "सिद्धे प्रत्यये पुनर्वचनं ठनादिबाधनार्थम्"),
                ("5.2.129", "कुगर्थमेवेदं वचनम्"),
                ("5.2.130", "सिद्धे सति नियमार्थं वचनम्")):
            with self.subTest(sutra=sutra):
                self.assertIn(purpose,
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_one_more_shuts_out_affixes_it_does_not_name(self):
        """
        5.2.95 and 5.2.131 both restate what was already given, and
        both do it to keep a rival affix away —
        **अन्ये मत्वर्थीया मा भूवन्** and
        **इह क्षेपे मतुब्बाधनार्थं वचनम्**.
        """
        self.assertIn("अन्ये मत्वर्थीया मा भूवन्",
                      unwrapped(REGISTRY.get("5.2.95").notes))
        self.assertIn("क्षेपे मतुब्बाधनार्थं वचनम्",
                      unwrapped(REGISTRY.get("5.2.131").notes))

    def test_and_the_insert_rule_gives_nothing_but_the_insert(self):
        """
        5.2.129: वात and अतिसार are both diseases and had इनि from
        5.2.128, so the rule's whole content is the कुक्.
        """
        row = provisions_for("5.2.129")[0]
        self.assertEqual(row.gives, provisions_for("5.2.128")[0].gives)
        self.assertEqual(row.adesa, "kuk")
        self.assertEqual(row.excepts, ("5.2.128",))


class WhatTheWholeWordMustName(unittest.TestCase):
    """
    Four rules of the closing stretch turn on what the DERIVED word
    names rather than on the base — a kind, a student, a place, a
    name — and each has its own counter-example.
    """

    def test_the_four_and_their_counter_examples(self):
        for sutra, result, kept_out in (
                ("5.2.133", "jāti", "हस्तवान् पुरुषः"),
                ("5.2.134", "brahmacārin", "वर्णवान्"),
                ("5.2.135", "deśa", "पुष्करवान् हस्ती"),
                ("5.2.137", "saṃjñā", "सोमवान्")):
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                self.assertEqual(row.result, result)
                self.assertIn(kept_out, row.keeps_out)

    def test_and_asking_without_the_condition_reaches_another_rule(self):
        """
        हस्त is a stem in short अ, so 5.2.115 reaches it — and only
        the *kind* condition sends the question to 5.2.133.
        """
        kind = what_comes("hasta", sense="asti", result="jāti")
        self.assertEqual(kind.sutra, "5.2.133")
        self.assertEqual(kind.affix, "ini")
        self.assertEqual(kind.also_gives, ())

        plain = what_comes("hasta", stem_final="a", sense="asti")
        self.assertEqual(plain.sutra, "5.2.115")
        self.assertIn("matup", plain.also_gives)


class OneWordCarryingEightSupplements(unittest.TestCase):
    """
    5.2.122 बहुलं छन्दसि — and the vṛtti ends by saying that all of
    it comes out of that one word.
    """

    def test_the_supplements_are_recorded_and_accounted_for(self):
        notes = unwrapped(REGISTRY.get("5.2.122").notes)
        for varttika in ("मर्मणश्च", "शृङ्गवृन्दाभ्यामारकन्",
                         "फलबर्हाभ्यामिनज्", "बलादूलच्",
                         "पर्वमरुद्भ्यां तन्"):
            with self.subTest(varttika=varttika):
                self.assertIn(varttika, notes)
        self.assertIn("तदेतत् सर्वं बहुलग्रहणेन सम्पद्यते", notes)

    def test_and_one_of_them_is_for_what_a_man_cannot_bear(self):
        """
        **शीतोष्णतृप्रेभ्यस्तद् न सहत इत्यालुज्** — शीतालुः is not
        one who HAS cold but one who cannot stand it, which is the
        possessive section turned inside out.
        """
        notes = unwrapped(REGISTRY.get("5.2.122").notes)
        self.assertIn("तद् न सहत इत्यालुज्", notes)
        self.assertIn("शीतालुः", notes)

    def test_and_another_is_for_what_a_man_lacks(self):
        """
        **अर्थात् तदभाव इनिः** — अर्थी is one who WANTS, against
        अर्थवान् who has. The same word appears again at 5.2.135
        with the same sense: **अर्थाच्चासन्निहिते**.
        """
        self.assertIn("अर्थात् तदभाव इनिः",
                      unwrapped(REGISTRY.get("5.2.122").notes))
        self.assertIn("अर्थाच्चासन्निहिते",
                      unwrapped(REGISTRY.get("5.2.135").notes))


class TheLastRulesOfThePada(unittest.TestCase):
    """
    5.2.138 gives seven affixes at once, and 5.2.140 closes the
    quarter.
    """

    def test_the_widest_rule_of_the_pada(self):
        """
        **कंशंभ्यां बभयुस्तितुतयसः** — seven affixes for two words,
        and fourteen forms. No other sūtra of the pāda gives so
        many.
        """
        row = provisions_for("5.2.138")[0]
        self.assertEqual(len(row.also_gives) + 1, 7)
        widest = max(
            (len(r.also_gives) + 1 for r in MATUP_TABLE if r.gives),
            default=0)
        self.assertEqual(widest, 7)
        self.assertEqual(row.of, ("kam", "śam"))

    def test_and_a_letter_of_one_affix_name_is_accounted_for(self):
        """
        **सकारः पदसंज्ञार्थः, तेनानुस्वारपरसवर्णौ सिद्धौ भवतः;
        संज्ञायां हि असत्यां कम्यः शम्य इति स्यात्** — without the
        स the nasal would not become अनुस्वार and the forms would
        come out wrong.
        """
        notes = unwrapped(REGISTRY.get("5.2.138").notes)
        self.assertIn("सकारः पदसंज्ञार्थः", notes)
        self.assertIn("कम्यः शम्य इति स्यात्", notes)
        self.assertIn("सकारः पदसंज्ञार्थः",
                      unwrapped(REGISTRY.get("5.2.123").notes))

    def test_and_the_last_rule_uses_a_word_that_is_not_the_pronoun(self):
        """
        **अहमिति शब्दान्तरमहंकारे वर्तते** — a different word,
        meaning self-regard. **अहंयुः, अहंकारवानित्यर्थः.**
        """
        notes = unwrapped(REGISTRY.get("5.2.140").notes)
        self.assertIn("अहमिति शब्दान्तरमहंकारे वर्तते", notes)
        self.assertIn("अहंकारवानित्यर्थः", notes)

    def test_and_the_colophon_closes_the_pada(self):
        self.assertIn("पञ्चमाध्यायस्य द्वितीयः पादः",
                      unwrapped(REGISTRY.get("5.2.140").notes))
        last = max(int(row.sutra.rsplit(".", 1)[1])
                   for row in MATUP_TABLE)
        self.assertEqual(last, 140)


if __name__ == "__main__":
    unittest.main()
