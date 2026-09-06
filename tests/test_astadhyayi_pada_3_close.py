# -*- coding: utf-8 -*-
"""
3.3.131 to 3.3.176 — the close of अध्याय ३ पाद ३.

With these the pāda is complete: 176 sūtras, contiguous.

What this block asserts that no earlier one could:

  * a condition about ANOTHER RULE having applied;
  * a condition on a word being MEANT and NOT SAID;
  * a rule protecting half of itself from its own other half;
  * an अनुवृत्ति with a single word cut out of it;
  * a commentary conceding that a stretch of the grammar need not
    have been written;
  * the वासरूप suspension fenced off at both ends.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from tests import unwrapped
from src.astadhyayi.lakara import LAKARA, lakara_for, lrn_is_optional
from src.astadhyayi.tense_transfer import (
    TRANSFER, tense_transfer, transferred_extent,
)
from src.astadhyayi.upapada_krt import Added, NotAdded
from src.astadhyayi.vidhi_krt import (
    VIDHI_KRT, stated_against_a_lakara, vidhi_affix,
)


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    LAKARA_CASES = (
        ("3.3.133", "lṛṭ", dict(time="bhaviṣyat", beside="kṣipra",
                                sense="āśaṃsā")),
        ("3.3.134", "liṅ", dict(time="bhaviṣyat",
                                beside="āśaṃsāvacana",
                                sense="āśaṃsā")),
        ("3.3.139", "lṛṅ", dict(time="bhaviṣyat", kriyatipatti=True,
                                lin_nimitta=True)),
        ("3.3.140", "lṛṅ", dict(kriyatipatti=True, lin_nimitta=True)),
        ("3.3.142", "laṭ", dict(beside="api", sense="garhā")),
        ("3.3.143", "liṅ", dict(beside="katham", sense="garhā")),
        ("3.3.144", "liṅ", dict(kimvrtta=True, sense="garhā")),
        ("3.3.145", "liṅ", dict(sense="anavakḷpti")),
        ("3.3.146", "lṛṭ", dict(beside="kiṃkila", sense="amarṣa")),
        ("3.3.147", "liṅ", dict(beside="jātu", sense="amarṣa")),
        ("3.3.148", "liṅ", dict(beside="yac", sense="anavakḷpti")),
        ("3.3.149", "liṅ", dict(beside="yac", sense="garhā")),
        ("3.3.150", "liṅ", dict(beside="yac", sense="citrīkaraṇa")),
        ("3.3.151", "lṛṭ", dict(sense="citrīkaraṇa")),
        ("3.3.152", "liṅ", dict(beside="uta")),
        ("3.3.153", "liṅ", dict(sense="kāmapravedana")),
        ("3.3.154", "liṅ", dict(sense="saṃbhāvanā", beside="alam")),
        ("3.3.155", "liṅ", dict(sense="saṃbhāvanā")),
        ("3.3.156", "liṅ", dict(sense="hetuhetumat")),
        ("3.3.157", "liṅ", dict(sense="icchā")),
        ("3.3.159", "liṅ", dict(sense="icchā-samānakartṛka")),
        ("3.3.160", "liṅ", dict(time="vartamāna", sense="icchā")),
        ("3.3.161", "liṅ", dict(sense="vidhi")),
        ("3.3.162", "loṭ", dict(sense="vidhi", wants="loṭ")),
        ("3.3.164", "liṅ", dict(sense="praiṣa",
                                urdhvamauhurtika=True)),
        ("3.3.165", "loṭ", dict(sense="praiṣa", beside="sma",
                                urdhvamauhurtika=True)),
        ("3.3.166", "loṭ", dict(sense="adhīṣṭa", beside="sma")),
        ("3.3.168", "liṅ", dict(sense="kāla", beside="yad")),
        ("3.3.172", "liṅ", dict(sense="śakti")),
        ("3.3.173", "liṅ", dict(sense="āśis")),
        ("3.3.175", "luṅ", dict(beside="māṅ")),
        ("3.3.176", "laṅ", dict(beside="sma-māṅ")),
    )

    VIDHI_CASES = (
        ("3.3.158", "tumun", dict(sense="icchā", samana_kartrka=True)),
        ("3.3.163", "kṛtya", dict(sense="praiṣa")),
        ("3.3.167", "tumun", dict(beside="kāla")),
        ("3.3.169", "kṛtya", dict(sense="arha")),
        ("3.3.170", "ṇini", dict(sense="ādhamarṇya")),
        ("3.3.171", "kṛtya", dict(sense="āvaśyaka", wants="kṛtya")),
        ("3.3.174", "ktic", dict(sense="āśis", samjna=True)),
    )

    def test_every_lakara_rule_answers_for_itself(self):
        for sutra, gives, where in self.LAKARA_CASES:
            with self.subTest(sutra=sutra, **where):
                answer = lakara_for(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_every_krt_rule_answers_for_itself(self):
        for sutra, gives, where in self.VIDHI_CASES:
            with self.subTest(sutra=sutra, **where):
                answer = vidhi_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_every_transfer_rule_answers_for_itself(self):
        for sutra, where, allows in (
            ("3.3.131", dict(like="vartamāna"), True),
            ("3.3.132", dict(like="bhūta", sense="āśaṃsā"), True),
            ("3.3.135", dict(like="anadyatana",
                             sense="kriyāprabandha"), False),
            ("3.3.136", dict(like="anadyatana",
                             sense="deśa-maryādā"), False),
            ("3.3.137", dict(like="anadyatana",
                             sense="kāla-maryādā"), False),
            ("3.3.138", dict(like="anadyatana",
                             sense="kāla-maryādā-para"), False),
        ):
            with self.subTest(sutra=sutra, **where):
                answer = tense_transfer(**where)
                self.assertEqual(answer.by, sutra)
                self.assertIsInstance(
                    answer, Added if allows else NotAdded)


class AConditionAboutAnotherRuleHavingApplied(unittest.TestCase):
    """
    3.3.139's लिङ्निमित्त — that some rule would have given लिङ् here.
    Every other condition in these two pādas has been about the act,
    the speaker, the company or the form; this is about the GRAMMAR'S
    own state.

    And its content arrives seventeen sūtras later, at 3.3.156.
    """

    def test_the_condition_is_needed(self):
        self.assertEqual(
            lakara_for(time="bhaviṣyat", kriyatipatti=True,
                       lin_nimitta=True).by, "3.3.139")
        self.assertNotEqual(
            lakara_for(time="bhaviṣyat", kriyatipatti=True).by,
            "3.3.139")

    def test_and_the_rule_that_supplies_it_is_named_at_both_ends(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.156", REGISTRY.get("3.3.139").notes)
        self.assertIn("3.3.139", REGISTRY.get("3.3.156").notes)

    def test_that_rule_really_gives_the_ending_in_question(self):
        self.assertEqual(lakara_for(sense="hetuhetumat").gives, "liṅ")

    def test_and_a_rule_notes_where_no_such_rule_applies(self):
        """3.3.146's लिङ्निमित्तमिह नास्ति तेन लृङ् न भवति."""
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("लिङ्निमित्तमिह नास्ति",
                      REGISTRY.get("3.3.146").notes)


class AConditionOnAWordBeingMeantAndNotSaid(unittest.TestCase):
    """
    3.3.154 wants अलम् UNDERSTOOD and not uttered — सिद्धश्चेदलमोऽ
    प्रयोगः, यत्र गम्यते चार्थो न चासौ प्रयुज्यते.
    """

    def test_the_ground_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.154").notes
        self.assertIn("सिद्धाप्रयोग", notes)
        self.assertIn("न चासौ प्रयुज्यते", notes)

    def test_and_the_counter_example_is_the_word_uttered(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("अलं देवदत्तो हस्तिनं हनिष्यति",
                      REGISTRY.get("3.3.154").notes)


class ARuleProtectingHalfOfItself(unittest.TestCase):
    """
    3.3.169, 3.3.172 and 3.3.174 each give two things, and each states
    one of them so that the OTHER — given by the same rule — shall not
    displace it.
    """

    def test_all_three_record_it(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra, phrase in (
            ("3.3.169", "तेन बाधा मा भूदिति"),
            ("3.3.172", "लिङा बाधा मा भूदिति"),
            ("3.3.174", "क्तिचा बाधा मा भूदिति"),
        ):
            with self.subTest(sutra=sutra):
                # Matched against the unwrapped note: these phrases are
                # long enough to fall across a line break, which has
                # cost three tests already.
                self.assertIn(
                    phrase, unwrapped(REGISTRY.get(sutra).notes))

    def test_and_each_really_gives_two_things(self):
        rows = {r.sutra: r for r in VIDHI_KRT}
        for sutra in ("3.3.169", "3.3.174"):
            with self.subTest(sutra=sutra):
                self.assertTrue(rows[sutra].also)
        row = next(r for r in LAKARA if r.sutra == "3.3.172")
        self.assertTrue(row.also)


class AnAnuvrttiWithOneWordCutOut(unittest.TestCase):
    """
    3.3.138 inherits all of 3.3.137 EXCEPT one word, which it replaces
    — अवरस्मिन्वर्जं पूर्वमनुवर्तते. The codification cannot represent
    a running condition at all, so every row states its own; what this
    rule adds is that a running condition can be inherited MINUS a
    part.
    """

    def test_the_two_rules_differ_in_exactly_that_word(self):
        rows = {r.sutra: r for r in TRANSFER}
        self.assertEqual(rows["3.3.137"].like, rows["3.3.138"].like)
        self.assertEqual(rows["3.3.137"].for_time,
                         rows["3.3.138"].for_time)
        self.assertNotEqual(rows["3.3.137"].sense,
                            rows["3.3.138"].sense)

    def test_and_only_the_later_one_is_optional(self):
        rows = {r.sutra: r for r in TRANSFER}
        self.assertFalse(rows["3.3.137"].optional)
        self.assertTrue(rows["3.3.138"].optional)

    def test_the_ground_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("अवरस्मिन्वर्जं",
                      REGISTRY.get("3.3.138").notes)


class AGrammarConcedingItNeedNotHaveBeenWritten(unittest.TestCase):
    """
    3.3.131's vṛtti: for a reader who holds that the WORD is
    present-tense and the other time comes from the SENTENCE, तादृशं
    वाक्यार्थप्रतिपत्तारं प्रति प्रकरणमिदं नारभ्यते — this whole
    section is not undertaken.
    """

    def test_the_concession_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("प्रकरणमिदं नारभ्यते",
                      REGISTRY.get("3.3.131").notes)

    def test_but_the_rules_are_codified_anyway(self):
        """
        The rules are in the text, so they are in the codification.
        Recording that a commentary thinks a section dispensable is
        not a licence to leave it out.
        """
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        for row in TRANSFER:
            with self.subTest(sutra=row.sutra):
                self.assertIn(row.sutra, have)


class TheTransferCarriesEverything(unittest.TestCase):
    """
    3.3.131's वत्करणं सर्वसादृश्यार्थम् — an affix keeps the
    conditions it had in its own time. And 3.3.132 at once limits it:
    सामान्यातिदेशे विशेषानतिदेशात्, a general transfer does not carry
    the special cases.
    """

    def test_the_extent_transferred_is_named_at_both_ends(self):
        first, last = transferred_extent()
        self.assertEqual((first, last), ("3.2.123", "3.3.1"))

    def test_and_both_ends_are_codified_so_the_claim_is_checkable(self):
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        for sutra in transferred_extent():
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, have)

    def test_the_limit_on_it_is_recorded_one_sutra_later(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("विशेषानतिदेशात्",
                      REGISTRY.get("3.3.132").notes)


class TheVasarupaSuspensionFencedOffAtBothEnds(unittest.TestCase):
    """
    3.3.107 holds the suspension of 3.1.94 WITHIN the feminine
    section — स्त्रीप्रकरणविषयस्यैव. 3.3.163 establishes that AFTER
    that section the principle is not obligatory — स्त्र्यधिकारात्
    परेण वासरूपविधिर्नावश्यं भवति. Between them the two rules bound it
    from either side.

    Six suspensions now, and this test holds all six together so a
    seventh has somewhere to go.
    """

    def test_all_six_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.2.146", "3.2.177", "3.3.10", "3.3.44",
                      "3.3.107", "3.3.163"):
            with self.subTest(sutra=sutra):
                self.assertIn("वासरूप", REGISTRY.get(sutra).notes)

    def test_the_two_that_bound_it_say_which_side(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("स्त्रीप्रकरणविषयस्यैव",
                      REGISTRY.get("3.3.107").notes)
        self.assertIn("स्त्र्यधिकारात् परेण",
                      REGISTRY.get("3.3.163").notes)

    def test_two_later_rules_lean_on_the_general_one(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.3.167", "3.3.169"):
            with self.subTest(sutra=sutra):
                self.assertIn("वासरूप", REGISTRY.get(sutra).notes)

    def test_and_the_rules_stated_against_a_lakara_are_read_not_listed(self):
        self.assertEqual(
            stated_against_a_lakara(),
            tuple(r.sutra for r in VIDHI_KRT if r.against_lakara))
        self.assertIn("3.3.163", stated_against_a_lakara())


class AnExtentStatedByNamingItsFarEnd(unittest.TestCase):
    """
    3.3.141's option runs to a NAMED sūtra, and the boundary EXCLUDES
    it — मर्यादायामयमाङ् नाभिविधौ. The fourth extent of this kind:
    3.2.134's आ क्वेः, 3.3.56's यावत् कृत्यल्युटो बहुलम्, 3.3.131's
    इत्यारभ्य ... यावत्, and this.
    """

    def test_the_option_holds_up_to_the_named_rule(self):
        for sutra in ("3.3.141", "3.3.145", "3.3.151"):
            with self.subTest(sutra=sutra):
                self.assertTrue(lrn_is_optional(sutra))

    def test_and_stops_at_it_rather_than_after_it(self):
        self.assertFalse(lrn_is_optional("3.3.152"))
        self.assertFalse(lrn_is_optional("3.3.140"))

    def test_the_reading_that_settles_it_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.141").notes
        self.assertIn("मर्यादायामयमाङ् नाभिविधौ", notes)
        self.assertIn("3.3.152", notes)

    def test_and_the_rule_at_the_boundary_says_so_from_its_side(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("विकल्पो निवृत्तः",
                      REGISTRY.get("3.3.152").notes)


class ThePadaIsComplete(unittest.TestCase):
    """
    176 sūtras, contiguous, each answered by exactly one entry point.
    The corpus says where it ends, not a number chosen here.
    """

    def test_it_runs_unbroken_from_its_first_sutra(self):
        from src.astadhyayi.sutra import REGISTRY

        numbers = sorted(
            int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
            if str(s.id).startswith("3.3."))
        self.assertTrue(numbers)
        self.assertEqual(numbers, list(range(1, len(numbers) + 1)))

    def test_and_the_corpus_says_where_it_ends(self):
        import io
        import json

        d = json.load(io.open("reference/commentary/kashika.json",
                              encoding="utf-8"))
        self.assertTrue(d.get("33176"))
        self.assertFalse(d.get("33177"))

    def test_every_rule_is_answered_by_exactly_one_entry_point(self):
        from src.astadhyayi.sutra import REGISTRY

        registered = {str(x.id) for x in REGISTRY.all()
                      if str(x.id).startswith("3.3.")}
        by_apply = {}
        for x in REGISTRY.all():
            if str(x.id).startswith("3.3."):
                by_apply.setdefault(x.apply.__name__, set()).add(
                    str(x.id))
        seen = set()
        for ids in by_apply.values():
            self.assertEqual(seen & ids, set())
            seen |= ids
        self.assertEqual(seen, registered)

    def test_the_two_pada_of_this_adhyaya_that_are_done_are_whole(self):
        """
        3.2 and 3.3 both complete, and each ends where its own
        colophon does. No range is named: the property is that the
        numbers run from one without a gap.
        """
        from src.astadhyayi.sutra import REGISTRY

        for pada in ("3.2.", "3.3."):
            with self.subTest(pada=pada):
                numbers = sorted(
                    int(str(s.id).rsplit(".", 1)[1])
                    for s in REGISTRY.all()
                    if str(s.id).startswith(pada))
                self.assertEqual(numbers,
                                 list(range(1, len(numbers) + 1)))


class WhatTheWholePadaLeavesOpen(unittest.TestCase):
    """Debts, asserted so that paying them is noticed."""

    def test_all_three_lakara_debts_are_paid(self):
        """
        ALL THREE PAID. 3.4.6 gives the Vedic set for any time; 3.4.69
        says what a लकार DENOTES; 3.4.77 enumerates the ten and says
        which are टित्.

        NORTH_STAR carried these from 3.2.110, where the table began
        naming its endings as bare strings. What the last of them buys
        is a check nothing could run before — every ending the table
        gives, across three pādas, against the rule that lists them.
        """
        from src.astadhyayi.lakara import LAKARA, LAKARA_LIST
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        for sutra in ("3.4.6", "3.4.69", "3.4.77"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, have)

        ten = {name for name, _ in LAKARA_LIST}
        given = {row.gives for row in LAKARA}
        self.assertTrue(given)
        self.assertEqual(given - ten, set())

    def test_and_a_lakara_now_has_a_meaning_and_a_form(self):
        from src.astadhyayi.denoted import lakara_denotes
        from src.astadhyayi.lakara import TIN

        self.assertEqual(lakara_denotes(), ("karman", "kartṛ"))
        self.assertEqual(lakara_denotes(akarmaka=True),
                         ("bhāva", "kartṛ"))
        self.assertEqual(len(TIN), 18)
    def test_and_the_rule_that_cited_it_can_now_be_checked(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.4.6", REGISTRY.get("3.2.105").notes)
        self.assertEqual(
            REGISTRY.get("3.4.6").apply.__name__, "lakara_for")
    def test_and_the_table_now_names_seven_endings(self):
        endings = {r.gives for r in LAKARA}
        self.assertGreaterEqual(len(endings), 7)
        for ending in ("liṅ", "loṭ", "lṛṅ", "luṅ"):
            with self.subTest(ending=ending):
                self.assertIn(ending, endings)

    def test_the_accent_claims_of_this_pada_cannot_be_checked(self):
        """
        Five rules were read as existing for an accent alone, and the
        sūtrapāṭha on disk is unaccented. NORTH_STAR §7 states the
        boundary; this asserts it still holds.
        """
        from src.astadhyayi.corpus import load_vidyut_sutrapatha

        texts = load_vidyut_sutrapatha()
        for sutra in ("3.3.57", "3.3.91", "3.3.96", "3.3.111"):
            with self.subTest(sutra=sutra):
                for mark in ("॑", "॒"):
                    self.assertNotIn(mark, texts[sutra].text)


if __name__ == "__main__":
    unittest.main()
