# -*- coding: utf-8 -*-
"""
६.३.११४–१३९ — संहितायाम्, and the pāda's last twenty-five rules.

One operation throughout, so nothing is decided by what the rules
do. What decides is where they stop and what they turn on, and
four things are worth holding the table to:

**A heading about the CONDITION of speech.** 6.3.114 is the only
one of the pāda's four that is neither a position nor an
operation, and its counter-example is the same line said apart.

**A register that tightens and then leaps.** No condition, then
संज्ञा, then छन्दस्, then मन्त्र, then ऋच् — and then 6.3.134 back
to मन्त्र, with 6.3.135's **ऋचीति वर्तते** reaching across it.

**Two rules that give up on describing themselves.** 6.3.137 and
6.3.109, the same shape twenty-eight sūtras apart.

**And a pāda that closes by settling a conflict with its own
earlier self** — 6.3.139 against 6.3.61, on सकृद्गतौ विप्रतिषेधे
यद्बाधितं तद्बाधितमेव.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.dirgha_samhita import (
    DIRGHA_TABLE, KARNA_EXCEPT, KIMSULAKADI, KOTARADI, KVIP_ROOTS,
    MANTRA_FOUR, RCI_EIGHT, SAMHITA_RUN, SARADI, SVAN_VARTIKA,
    lengthens, provisions_for)
from src.astadhyayi.purvapada_vikara import VIKARA_RUN
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunClosesThePada(unittest.TestCase):
    def test_it_opens_one_sutra_after_the_run_before(self):
        self.assertEqual(_n(SAMHITA_RUN[0])[2],
                         _n(VIKARA_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_114_to_139(self):
        got = [row.sutra for row in DIRGHA_TABLE]
        self.assertEqual(got, ["6.3.%d" % n
                               for n in range(114, 140)])

    def test_it_ends_where_the_padas_first_heading_ends(self):
        from src.astadhyayi.aluk import UTTARAPADE_RUN

        self.assertEqual(SAMHITA_RUN[1], UTTARAPADE_RUN[1])
        self.assertEqual(SAMHITA_RUN[1], "6.3.139")

    def test_every_row_carries_its_reason(self):
        for row in DIRGHA_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)


class OneOperationThroughout(unittest.TestCase):
    """
    Every rule of the run lengthens, and none does anything else.
    A row with a different operation would mean the run has been
    read as wider than it is.
    """

    def test_every_rule_but_the_heading_lengthens(self):
        for row in DIRGHA_TABLE:
            if row.heading:
                self.assertEqual(row.does, "", row.sutra)
            else:
                self.assertEqual(row.does, "dīrgha", row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = lengthens("aśva", before="pati")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("keeps the length it had", got.why)

    def test_and_the_heading_never_answers(self):
        row, = provisions_for("6.3.114")
        self.assertTrue(row.heading)
        self.assertNotEqual(
            lengthens(gana="lakṣaṇa", before="karṇa").sutra,
            "6.3.114")


class TheRegisterTightensAndThenLeapsOverASutra(unittest.TestCase):
    """
    6.3.115–130 ask nothing about where the words are said;
    6.3.126 adds छन्दस्; 6.3.131 adds मन्त्र; 6.3.133 adds ऋच्.
    But it does not simply tighten and stay tight. 6.3.134 इकः
    सुञि goes back to **मन्त्रविषये**, standing between two
    verse-rules — and 6.3.135 then opens **ऋचीति वर्तते**,
    carrying the narrower condition ACROSS it. A frog's leap, and
    a plain *never widens* would have hidden it.

    And the pāda's last three sūtras drop the register
    altogether: 6.3.137, 6.3.138 and 6.3.139 are general again.
    """

    ORDER = ("", "chandas", "mantra", "ṛc")

    def _register(self, row):
        if "ṛc" in row.result:
            return "ṛc"
        if "mantra" in row.result:
            return "mantra"
        return "chandas" if row.chandasi else ""

    def test_the_register_tightens_twice_and_then_loosens_once(
            self):
        """
        मन्त्र at 6.3.131, ऋच् at 6.3.133 — and then 6.3.134 back
        to मन्त्र. The sequence is not sorted, and asserting that
        it were would be asserting something false about the
        text.
        """
        got = [self._register(row) for row in DIRGHA_TABLE
               if not row.heading
               and _n("6.3.131") <= _n(row.sutra) <= _n("6.3.136")]
        self.assertEqual(got, ["mantra", "mantra", "ṛc", "mantra",
                               "ṛc", "ṛc"])
        self.assertNotEqual(
            [self.ORDER.index(one) for one in got],
            sorted(self.ORDER.index(one) for one in got))

    def test_so_one_anuvrtti_leaps_over_a_sutra(self):
        """
        6.3.135's vṛtti opens **ऋचीति वर्तते**, and the sūtra
        immediately before it is मन्त्र and not ऋच्. The
        verse-condition therefore comes from 6.3.133, two sūtras
        back, across one that does not carry it.
        """
        skipped, = provisions_for("6.3.134")
        self.assertEqual(skipped.result, ("mantra",))
        for code in ("6.3.133", "6.3.135"):
            row, = provisions_for(code)
            self.assertEqual(row.result, ("ṛc",), code)

    def test_and_the_ones_that_carry_a_condition_down_say_so(self):
        for code, cited in (("6.3.132", "मन्त्र इति वर्तते"),
                            ("6.3.136", "ऋचीत्येव")):
            row, = provisions_for(code)
            self.assertIn(cited, row.why, code)

    def test_but_the_padas_last_three_rules_drop_it_again(self):
        """
        6.3.137, 6.3.138 and 6.3.139 ask for no register at all,
        so the run does not simply narrow to a point: it narrows
        and then opens out for its last three sūtras.
        """
        for code in ("6.3.137", "6.3.138", "6.3.139"):
            row, = provisions_for(code)
            self.assertEqual(self._register(row), "", code)
        self.assertEqual(
            lengthens(gana="samprasāraṇa-anta").sutra, "6.3.139")

    def test_the_vedic_rules_are_not_reached_outside_the_veda(self):
        self.assertEqual(lengthens("aṣṭan", result="saṃjñā").sutra,
                         "6.3.125")
        self.assertEqual(
            lengthens("aṣṭan", chandasi=True).sutra, "6.3.126")

    def test_a_mantra_rule_wants_the_register_said(self):
        self.assertEqual(lengthens("soma", before="matup").sutra,
                         "")
        self.assertEqual(
            lengthens("soma", before="matup",
                      result="mantra").sutra, "6.3.131")

    def test_and_so_does_a_verse_rule(self):
        self.assertEqual(lengthens("tu").sutra, "")
        self.assertEqual(lengthens("tu", result="ṛc").sutra,
                         "6.3.133")


class TheHeadingReadsItsOwnExampleOutFromFarAhead(unittest.TestCase):
    """
    6.3.114's vṛtti quotes **वक्ष्यति द्व्यचोऽतस्तिङः इति** — a
    sūtra twenty-one further on — and the line it quotes is the
    line 6.3.135 itself is about. So the heading and its example
    have to agree, or one of the two is wrongly read.
    """

    def test_the_heading_names_the_sutra_it_quotes(self):
        row, = provisions_for("6.3.114")
        self.assertIn("द्व्यचोऽतस्तिङः", row.why)

    def test_and_that_sutra_is_inside_the_run(self):
        self.assertTrue(REGISTRY.has("6.3.135"))
        self.assertLessEqual(_n(SAMHITA_RUN[0]), _n("6.3.135"))
        self.assertLessEqual(_n("6.3.135"), _n(SAMHITA_RUN[1]))

    def test_and_both_quote_the_same_line(self):
        heading, = provisions_for("6.3.114")
        example, = provisions_for("6.3.135")
        for word in ("विद्मा", "गोपतिं"):
            self.assertIn(word, heading.why, word)
            self.assertIn(word, example.why, word)


class OneGlossIsCarriedAcrossAPada(unittest.TestCase):
    """
    6.3.115's लक्षण is the brand cut in a beast's ear, and the
    vṛtti gives the same gloss 6.2.112's did — **यत् पशूनां
    ...ज्ञापनार्थं दात्राकारादि क्रियते, तद् इह लक्षणं गृह्यते**.
    Two pādas apart, one term, and the record has to keep them
    agreeing.
    """

    def test_both_notes_give_the_gloss(self):
        from src.astadhyayi.uttarapada_svara import (
            provisions_for as accent_for)

        here, = provisions_for("6.3.115")
        there, = accent_for("6.2.112")
        for cited in ("पशूनां", "लक्षणं गृह्यते"):
            self.assertIn(cited, here.why, cited)
            self.assertIn(cited, there.why, cited)

    def test_and_this_one_says_where_it_came_from(self):
        here, = provisions_for("6.3.115")
        self.assertIn("6.2.112", here.why)

    def test_the_nine_exceptions_are_kept_out(self):
        self.assertEqual(len(KARNA_EXCEPT), 9)
        for word in KARNA_EXCEPT:
            self.assertEqual(
                lengthens(word, gana="lakṣaṇa",
                          before="karṇa").sutra, "", word)


class TwoGanasMatchedOneToOne(unittest.TestCase):
    """
    6.3.117 — कोटरादि before वन, किंशुलकादि before गिरि, and
    crossing them reaches nothing.
    """

    def test_each_pairing_is_reached(self):
        for gana, follows in (("koṭarādi", "vana"),
                              ("kiṃśulakādi", "giri")):
            got = lengthens(gana=gana, before=follows,
                            result="saṃjñā")
            self.assertEqual(got.sutra, "6.3.117",
                             "%s / %s" % (gana, follows))

    def test_and_neither_crossing_is(self):
        for gana, follows in (("koṭarādi", "giri"),
                              ("kiṃśulakādi", "vana")):
            self.assertEqual(
                lengthens(gana=gana, before=follows,
                          result="saṃjñā").sutra, "",
                "%s / %s" % (gana, follows))

    def test_the_two_lists_are_disjoint(self):
        self.assertEqual(set(KOTARADI) & set(KIMSULAKADI), set())
        self.assertGreater(len(KOTARADI), 3)
        self.assertGreater(len(KIMSULAKADI), 3)


class ARuleNamedBecauseTheWiderOneCannotReachIt(unittest.TestCase):
    """
    6.3.119 wants MANY vowels, and शर, अहि, कपि, मुनि have two.
    6.3.120 names them for exactly that reason, so the two lists
    must not overlap in the property either rule turns on.
    """

    def test_the_wider_rule_turns_on_a_count(self):
        row, = provisions_for("6.3.119")
        self.assertEqual(row.result, ("bahvac-saṃjñā",))

    def test_and_the_narrower_names_its_stems(self):
        row, = provisions_for("6.3.120")
        self.assertEqual(row.gana, "śarādi")
        self.assertEqual(len(SARADI), 9)

    def test_both_act_before_the_same_affix_in_the_same_sense(self):
        for code, query in (
                ("6.3.119", {"result": "bahvac-saṃjñā",
                             "before": "matup"}),
                ("6.3.120", {"gana": "śarādi", "result": "saṃjñā",
                             "before": "matup"})):
            got = lengthens(**query)
            self.assertEqual(got.sutra, code, code)

    def test_and_the_ajiradi_words_are_kept_out_of_the_wider_one(
            self):
        self.assertEqual(
            lengthens(result="bahvac-saṃjñā", before="matup",
                      gana="ajirādi").sutra, "")


class TwoRulesGiveUpOnDescribingThemselves(unittest.TestCase):
    """
    6.3.137 अन्येषामपि दृश्यते and 6.3.109 पृषोदरादीनि — the same
    shape twenty-eight sūtras apart, and both appeal to attested
    usage rather than to a condition.
    """

    def test_this_one_names_no_stem_and_no_environment(self):
        row, = provisions_for("6.3.137")
        self.assertEqual(row.of, ())
        self.assertEqual(row.before, ())
        self.assertEqual(lengthens(gana="anyeṣām-api").sutra,
                         "6.3.137")

    def test_and_the_other_is_the_same_shape(self):
        from src.astadhyayi.purvapada_vikara import (
            provisions_for as vikara_for)

        other, = vikara_for("6.3.109")
        self.assertEqual(other.of, ())
        self.assertEqual(other.before, ())

    def test_both_appeal_to_what_the_learned_say(self):
        from src.astadhyayi.purvapada_vikara import (
            provisions_for as vikara_for)

        here, = provisions_for("6.3.137")
        other, = vikara_for("6.3.109")
        self.assertIn("शिष्टप्रयोगाद्", here.why)
        self.assertIn("शिष्टैरुच्चारितानि", other.why)

    def test_and_a_varttika_makes_one_corner_of_it_exact(self):
        """**शुनो दन्तदंष्ट्राकर्ण...** — seven second members
        named for श्वन् alone, so at least that much is
        decidable."""
        self.assertEqual(len(SVAN_VARTIKA), 7)
        row, = provisions_for("6.3.137")
        for word in ("श्वादन्तः", "श्वापदः"):
            self.assertIn(word, row.why, word)


class TheListsAreTheVrttisOwn(unittest.TestCase):
    def test_seven_roots_with_kvip(self):
        self.assertEqual(len(KVIP_ROOTS), 7)
        row, = provisions_for("6.3.116")
        self.assertEqual(row.before, KVIP_ROOTS)
        for root in KVIP_ROOTS:
            self.assertEqual(
                lengthens(before=root, result="kvip").sutra,
                "6.3.116", root)

    def test_four_stems_in_a_mantra(self):
        self.assertEqual(len(MANTRA_FOUR), 4)
        for word in MANTRA_FOUR:
            self.assertEqual(
                lengthens(word, before="matup",
                          result="mantra").sutra, "6.3.131", word)

    def test_eight_particles_in_a_verse(self):
        self.assertEqual(len(RCI_EIGHT), 8)
        for word in RCI_EIGHT:
            self.assertEqual(lengthens(word, result="ṛc").sutra,
                             "6.3.133", word)


class ThePadaClosesBySettlingAConflictWithItself(unittest.TestCase):
    """
    6.3.139 lengthens कारीषगन्धी and 6.3.61 would have shortened
    it. The vṛtti answers twice — **व्यवस्थितविभाषा हि सा**, and
    then **सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितम् एव** — and
    the two modules have to agree, since 6.3.61's own table
    already names कारीषगन्धी as a word its option does not reach.
    """

    def test_the_last_sutra_names_the_rule_it_beats(self):
        row, = provisions_for("6.3.139")
        self.assertEqual(row.blocks, ("6.3.61",))
        self.assertLess(_n("6.3.61"), _n(row.sutra))

    def test_and_the_beaten_rule_already_kept_the_word_out(self):
        from src.astadhyayi.hrasva_mum import (
            GALAVA_KEEPS_OUT, adjusts)

        self.assertIn("kārīṣagandhī", GALAVA_KEEPS_OUT)
        self.assertEqual(
            adjusts("kārīṣagandhī", stem="ik-anta-aṅī").sutra, "")

    def test_the_note_gives_both_answers_the_vrtti_gives(self):
        row, = provisions_for("6.3.139")
        self.assertIn("व्यवस्थितविभाषा", row.why)
        self.assertIn("सकृद्", row.why)

    def test_and_the_padas_first_heading_is_still_running_at_it(
            self):
        row, = provisions_for("6.3.139")
        self.assertIn("उत्तरपद इति वर्तते", row.why)


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in DIRGHA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in DIRGHA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class ThePadaIsComplete(unittest.TestCase):
    """
    All 139 of पाद ६.३, in seven modules: the अलुक् run, the
    द्वन्द्व substitutions, पुंवद्भाव, the five stems replaced,
    the shortening and the augments, नञ्/सह/समान, the alterations
    that would not group, and this.
    """

    def test_every_sutra_of_the_pada_is_codified(self):
        for n in range(1, 140):
            self.assertTrue(REGISTRY.has("6.3.%d" % n), n)

    def test_and_the_headings_it_opened_all_close_inside_it(self):
        from src.astadhyayi.aluk import ALUK_RUN, UTTARAPADE_RUN

        for span in (ALUK_RUN, UTTARAPADE_RUN, SAMHITA_RUN):
            self.assertEqual(span[0].rsplit(".", 1)[0], "6.3")
            self.assertLessEqual(_n(span[1]), _n("6.3.139"))

    def test_and_the_pada_that_follows_has_opened(self):
        """
        6.4.1 अङ्गस्य is the bound 6.3.1's उत्तरपदे was read
        against — **उत्तरपदाधिकारः प्रागङ्गाधिकारात्** — and it
        has landed. The debt this pāda left was its own stated
        bound, and the bound is now a rule that can be asked.
        """
        from src.astadhyayi.anga_dirgha import ANGA_RUN

        self.assertTrue(REGISTRY.has("6.4.1"))
        self.assertEqual(ANGA_RUN[0], "6.4.1")

    def test_and_the_pada_after_it_has_been_opened(self):
        """6.4.1's own bound is the end of adhyāya 7. This was
        written as a debt when none of adhyāya 7 was codified;
        पाद ७.१ is complete now, so the claim is the live edge —
        the heading reaches into a pāda that can be asked, and
        stops short of 7.4.97, which cannot be yet."""
        self.assertTrue(REGISTRY.has("7.1.1"))
        self.assertTrue(REGISTRY.has("7.1.103"))
        # 7.4.97 has landed, and with it 6.4.1's अङ्गस्य
        # heading reaches its own stated end — **अधिकारोऽयम् आ
        # सप्तमाध्यायपरिसमाप्तेः**. The heading's whole span,
        # six hundred and thirteen sūtras, can be asked now.
        self.assertTrue(REGISTRY.has("7.4.97"))


if __name__ == "__main__":
    unittest.main()
