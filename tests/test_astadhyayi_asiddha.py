# -*- coding: utf-8 -*-
"""
Tests for the paribhāṣās outside adhyāya 1 — 2.1.1, 3.1.94, 6.1.85, 6.1.86,
6.4.22, 8.2.1, 8.2.2 and 8.2.3.

These eight are all rules about rules, and every one of them is usually
paraphrased in a form that loses the part doing the work. The tests are
weighted accordingly: not much on the headline, a great deal on the
qualifications.

  8.2.1   runs in *two* directions, and switches 1.4.2 off
  8.2.2   is a नियम — asiddha in four operations and nowhere else
  6.4.22  needs the two operations to share a locus
  3.1.94  measures sameness of form after the anubandhas are gone
  2.1.1   reaches no वर्णविधि at all
  6.1.85  likewise

A codification that read 8.2.1 as "the tripādī is invisible to what precedes"
and stopped there would pass a headline test and fail the four below it.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.asiddha import (
    ABHIYA_FROM,
    ABHIYA_TO,
    NALOPA_ASIDDHA_IN,
    TRIPADI_FROM,
    TRIPADI_TO,
    antadivat,
    blocks_vipratisedha,
    ekadesa_visible,
    in_abhiya,
    in_tripadi,
    visible,
)
from src.astadhyayi.paribhasa import displaces, samartha
from src.astadhyayi.sources import facts
from src.astadhyayi.sources import all_sutra_ids
from src.astadhyayi.sutra import REGISTRY


class Purvatrasiddham(unittest.TestCase):
    """8.2.1, and the two directions it runs in."""

    def test_the_tripadi_is_invisible_to_what_precedes_it(self):
        self.assertTrue(visible("8.2.31", "6.1.87").asiddha)
        self.assertTrue(visible("8.4.40", "7.1.9").asiddha)

    def test_and_within_itself_each_later_rule_to_each_earlier(self):
        """
        इत उत्तरं चोत्तर उत्तरो योगः पूर्वत्र पूर्वत्रासिद्धो भवति — the half
        of the sūtra that is easy to miss, and the half that does most of the
        work.
        """
        self.assertTrue(visible("8.4.40", "8.2.31").asiddha)
        self.assertTrue(visible("8.3.15", "8.2.1").asiddha)

    def test_but_not_the_other_way_round(self):
        """An earlier rule is perfectly visible to a later one."""
        self.assertFalse(visible("8.2.31", "8.4.40").asiddha)

    def test_and_not_at_all_outside_it(self):
        self.assertFalse(visible("6.1.87", "7.3.101").asiddha)
        self.assertFalse(visible("7.1.9", "8.2.31").asiddha)

    def test_the_scope_is_the_one_the_corpus_records(self):
        """
        Two texts on the same claim: the adhikāra's end is computed here from
        8.4.68, and the corpus records a scope-end for 8.2.1 independently.
        """
        self.assertEqual(facts("8.2.1").scope_end, TRIPADI_TO)
        self.assertTrue(in_tripadi(TRIPADI_FROM))
        self.assertTrue(in_tripadi("8.4.68"))
        self.assertFalse(in_tripadi("8.1.74"))

    def test_and_every_sutra_the_corpus_puts_under_it_is_in_range(self):
        from src.astadhyayi.sources import all_sutra_ids

        under = [s for s in all_sutra_ids()
                 if "8.2.1" in [i.sutra for i in facts(s).adhikara]]
        self.assertGreater(len(under), 250)
        for sutra_id in under:
            self.assertTrue(in_tripadi(sutra_id), sutra_id)


class ItSwitchesOffTheConflictRule(unittest.TestCase):
    """
    The sharpest consequence, and the one a paraphrase always loses.

    येन पूर्वेण लक्षणेन सह स्पर्धते परं लक्षणम्, तत् प्रति तस्यासिद्धत्वात् न
    प्रवर्तते. Through the last quarter of the grammar 1.4.2 does not operate,
    because a rule that cannot be seen cannot compete.
    """

    def test_1_4_2_does_not_settle_a_pair_across_the_boundary(self):
        settled = blocks_vipratisedha("6.1.87", "8.2.77")
        self.assertTrue(settled.asiddha)
        self.assertIn("विस्फोर्यम्", settled.why)

    def test_nor_a_pair_inside_the_tripadi(self):
        self.assertTrue(blocks_vipratisedha("8.2.31", "8.4.40").asiddha)

    def test_but_it_operates_normally_outside(self):
        self.assertFalse(
            blocks_vipratisedha("7.3.101", "7.3.103").asiddha)

    def test_the_order_the_pair_is_given_in_does_not_matter(self):
        for pair in (("6.1.87", "8.2.77"), ("8.2.77", "6.1.87")):
            self.assertTrue(blocks_vipratisedha(*pair).asiddha, pair)

    def test_and_1_4_2_itself_still_says_what_it_says(self):
        """
        The two are codified in different modules and must agree about the
        ordinary case: outside the tripādī, the later of two equal rules.
        """
        from src.astadhyayi.vipratisedha import Rule, vipratisedha

        self.assertEqual(
            vipratisedha([Rule("7.3.101"), Rule("7.3.103")]).winner.sutra,
            "7.3.103",
        )


class WhatEscapes(unittest.TestCase):
    """The two things 8.2.1 does not reach."""

    def test_the_case_endings_of_its_own_sutras_are_read_regardless(self):
        """
        कार्यकालं हि संज्ञापरिभाषम् — a paribhāṣā is invoked at the moment it
        is wanted, so 1.1.49, 1.1.66 and 1.1.67 are never 'earlier' than the
        sūtra whose endings they read.
        """
        seen = visible("8.2.31", "1.1.49", reading_a_case_ending=True)
        self.assertFalse(seen.asiddha)
        self.assertIn("कार्यकालं", seen.why)

    def test_and_an_apavada_is_visible_even_standing_later(self):
        seen = visible("8.2.31", "6.1.87", done_is_apavada=True)
        self.assertFalse(seen.asiddha)
        self.assertIn("वचनप्रामाण्याद्", seen.why)

    def test_without_that_flag_the_same_pair_is_invisible(self):
        """Which is what makes the exemption mean something."""
        self.assertTrue(visible("8.2.31", "6.1.87").asiddha)

    def test_the_three_paribhasas_it_names_are_all_codified(self):
        """
        1.1.49, 1.1.66 and 1.1.67 are the ones the exemption is for, and all
        three were codified long before this sūtra was reached.
        """
        for sutra in ("1.1.49", "1.1.66", "1.1.67"):
            self.assertTrue(REGISTRY.has(sutra), sutra)


class Nalopa(unittest.TestCase):
    """8.2.2 and 8.2.3."""

    def test_it_is_a_niyama_and_not_a_grant(self):
        """
        एतेष्वेव नलोपोऽसिद्धो भवति, नान्यत्र. Four operations, and nowhere
        else — which is the opposite of what "the n-elision is asiddha" would
        suggest.
        """
        for operation in NALOPA_ASIDDHA_IN:
            self.assertTrue(
                visible("8.2.7", "7.1.9", done_is_nalopa=True,
                        operation=operation).asiddha, operation)

    def test_and_outside_those_four_it_is_fully_visible(self):
        """राजीयति, राजायते, राजाश्व — all formed with the elision in view."""
        for operation in ("sandhi", "guṇa", "vṛddhi", None):
            self.assertFalse(
                visible("8.2.7", "6.1.87", done_is_nalopa=True,
                        operation=operation).asiddha, operation)

    def test_there_are_exactly_four(self):
        self.assertEqual(len(NALOPA_ASIDDHA_IN), 4)
        self.assertEqual(
            set(NALOPA_ASIDDHA_IN),
            {"sup", "svara", "saṃjñā", "tuk-before-kṛt"},
        )

    def test_the_mu_substitute_is_visible_to_the_na_elision(self):
        """न मु ने — मुभावो नाभावे कर्तव्ये नासिद्धो भवति, किं तर्हि? सिद्ध एव."""
        seen = visible("8.2.80", "7.3.120", done_is_mu=True,
                       applying_nabhava=True)
        self.assertFalse(seen.asiddha)
        self.assertEqual(seen.by, "8.2.3")

    def test_but_not_otherwise(self):
        self.assertTrue(visible("8.2.80", "7.3.102", done_is_mu=True).asiddha)


class Abhiya(unittest.TestCase):
    """6.4.22, and its समानाश्रयत्व."""

    def test_within_the_range_and_on_one_locus(self):
        seen = visible("6.4.101", "6.4.105", same_locus=True)
        self.assertTrue(seen.asiddha)
        self.assertEqual(seen.by, "6.4.22")

    def test_but_not_on_two(self):
        """व्याश्रयं तु नासिद्धवद् भवति — पपुषः पश्य, चिच्युषः पश्य."""
        seen = visible("6.4.101", "6.4.105", same_locus=False)
        self.assertFalse(seen.asiddha)
        self.assertIn("व्याश्रयं", seen.why)

    def test_and_it_will_not_guess_when_the_locus_is_unstated(self):
        """
        Whether two operations rest on the same thing is a fact about the
        derivation. With it unstated the codification withholds rather than
        assuming, and says which condition was wanting.
        """
        seen = visible("6.4.101", "6.4.105")
        self.assertFalse(seen.asiddha)
        self.assertIn("समानाश्रयत्व", seen.why)

    def test_the_range_includes_the_bha_section(self):
        """आ भात् is an अभिविधि — तेन भाधिकारेऽप्यसिद्धवद् भवति."""
        self.assertTrue(in_abhiya(ABHIYA_FROM))
        self.assertTrue(in_abhiya("6.4.129"))
        self.assertTrue(in_abhiya(ABHIYA_TO))
        self.assertFalse(in_abhiya("6.4.21"))
        self.assertFalse(in_abhiya("7.1.1"))

    def test_and_the_corpus_agrees_where_6_4_129_ends(self):
        """
        6.4.22's range ends where the adhyāya does, and 6.4.129 भस्य is a
        heading inside it whose own end the corpus records.
        """
        from src.astadhyayi.reading import adhikara

        found = adhikara("6.4.129")
        self.assertIsNotNone(found)
        self.assertEqual(found.ends_at, "6.4.175")
        self.assertEqual(ABHIYA_TO, "6.4.175")

    def test_nothing_outside_the_range_is_touched(self):
        self.assertFalse(visible("6.4.10", "6.4.105", same_locus=True).asiddha)


class Ekadesa(unittest.TestCase):
    """6.1.85 and 6.1.86."""

    def test_the_single_substitute_counts_as_both_ends(self):
        counts = antadivat().counts_as
        self.assertEqual(len(counts), 2)
        self.assertIn("end of the first", counts)
        self.assertIn("beginning of the second", counts)

    def test_but_not_for_an_operation_on_sounds(self):
        """वर्णाश्रयविधाव् अयम् अन्तादिवद्भावो नेष्यते."""
        self.assertEqual(antadivat(varna_vidhi=True).counts_as, ())

    def test_and_it_is_asiddha_for_exactly_two_operations(self):
        for operation in ("ṣatva", "tuk"):
            self.assertTrue(ekadesa_visible(operation).asiddha, operation)
        for operation in ("guṇa", "vṛddhi", "dīrgha", "sandhi"):
            self.assertFalse(ekadesa_visible(operation).asiddha, operation)

    def test_the_two_sutras_say_opposite_things_and_both_are_needed(self):
        """
        6.1.85 makes the substitute count as present at both edges; 6.1.86
        makes it count as absent for two operations. Neither subsumes the
        other, and a codification that had only one would be wrong half the
        time.
        """
        self.assertTrue(antadivat().counts_as)
        self.assertTrue(ekadesa_visible("ṣatva").asiddha)


class Samartha(unittest.TestCase):
    """2.1.1."""

    def test_connected_words_are_reached_and_unconnected_are_not(self):
        self.assertTrue(samartha(connected=True).applies)
        self.assertFalse(samartha(connected=False).applies)

    def test_it_will_not_guess(self):
        self.assertFalse(samartha().applies)

    def test_and_it_reaches_no_operation_on_sounds(self):
        """
        पदग्रहणं किम्? वर्णविधौ समर्थपरिभाषा मा भूत्. This is the limit the
        word पद is in the sūtra for, and without it तिष्ठतु दध्यशान would not
        take its yaṇ.
        """
        reached = samartha(padavidhi=False, connected=False)
        self.assertTrue(reached.applies)
        self.assertIn("वर्णविधौ", reached.why)


class Vasarupa(unittest.TestCase):
    """3.1.94, which suspends 1.4.2's doctrine for one section."""

    def test_in_the_krt_section_an_unlike_exception_only_optionally_displaces(self):
        found = displaces(utsarga="3.1.133", apavada="3.1.135",
                          utsarga_affix="ṇvul", apavada_affix="ka")
        self.assertTrue(found.displaces)
        self.assertTrue(found.optional)
        self.assertEqual(found.by, "3.1.94")

    def test_but_a_like_one_displaces_outright(self):
        """
        नानुबन्धकृतम् असारूप्यम् — अण् and क are both अ once the ण् and the
        क् are set aside, so 3.2.3 blocks 3.2.1 and गोदः stands alone.
        """
        found = displaces(utsarga="3.2.1", apavada="3.2.3",
                          utsarga_affix="aṇ", apavada_affix="ka")
        self.assertFalse(found.optional)
        self.assertIn("नानुबन्धकृतम्", found.why)

    def test_the_sameness_is_measured_by_the_it_rules_already_codified(self):
        """
        Which is what makes the test above more than a stipulation: the same
        `analyze` that finds a root's marks for 1.3.12 finds an affix's here.
        """
        from src.astadhyayi.itsamjna import PRATYAYA, analyze

        self.assertEqual(analyze("aṇ", PRATYAYA).stem, "a")
        self.assertEqual(analyze("ka", PRATYAYA).stem, "a")
        self.assertNotEqual(analyze("ṇvul", PRATYAYA).stem,
                            analyze("ka", PRATYAYA).stem)

    def test_not_in_the_feminine_section(self):
        found = displaces(utsarga="3.3.94", apavada="3.3.102")
        self.assertFalse(found.optional)
        self.assertIn("अस्त्रियामिति", found.why)

    def test_and_not_outside_the_krt_section_at_all(self):
        found = displaces(utsarga="4.1.1", apavada="4.1.4")
        self.assertFalse(found.optional)
        self.assertEqual(found.by, "1.4.2")

    def test_nor_for_a_pair_straddling_its_edge(self):
        """
        The sūtra is read under 3.1.91 धातोः, so it says nothing about a pair
        one of which stands outside. An earlier version of the codification
        checked only the exception's position and would have relaxed such a
        pair too.
        """
        found = displaces(utsarga="2.1.1", apavada="3.1.135")
        self.assertFalse(found.optional)
        self.assertEqual(found.by, "1.4.2")

    def test_its_field_is_the_krt_adhikara_the_corpus_records(self):
        from src.astadhyayi.paribhasa import KRT_FROM, KRT_TO
        from src.astadhyayi.reading import adhikara

        found = adhikara(KRT_FROM)
        self.assertIsNotNone(found)
        self.assertEqual(found.ends_at, KRT_TO)


class Registration(unittest.TestCase):
    #: Sūtras codified out of order, each for a stated reason. The first
    #: eight were interpretive rules the earlier work needed. The five after
    #: them were chosen by working backwards from जयति: they are exactly
    #: what that word needs and nothing else, which is a better way to pick
    #: the next rules than going down the list, because the result is
    #: checkable against a derivation rather than against our own examples.
    # 2.1.1 was here while the pāda was a stub reached ahead for its
    # paribhāṣā. The pāda is finished now — 2.1.1 to 2.1.72 — so it is
    # read in order like the rest and belongs to no reached-ahead list.
    # 3.1.94 was here while 3.1 was a stub reached ahead for it. The
    # run has passed through it — 3.1.1 to 3.1.95 — so it is read in
    # order like the rest and belongs to no reached-ahead list.
    # 6.4.22 असिद्धवत्रा भात् was here while 6.4 was a stub
    # reached ahead for the asiddhatva. 6.4.1 to 6.4.33 is read in
    # order now, so it belongs to no reached-ahead list — the same
    # thing that took 3.1.22 and 3.1.32 off it.
    IDS = (
           # 8.2.1, 8.2.2 and 8.2.3 were the first three names on
           # this list — the asiddhatva heading itself, reached
           # ahead of everything because the whole ordering of the
           # work rests on it. पाद ८.२ is read through now, 8.2.1
           # to 8.2.108, so all three are read in order like the
           # rest and come off the list. So does 8.2.66 below.
           # 3.1.68 कर्तरि शप् was reached ahead for the present of
           # पच्; the run has passed through it as well. 3.4.113
           # was here for 7.3.84's sake and 3.4.79 for एधते's;
           # 3.4 is read from 1 to 117 now, so neither was reached
           # ahead of anything and both come off the list. 6.1.78,
           # 6.1.85 and 6.1.86 have gone the same way — 6.1 is read
           # from 1 to 157 now.
           # 7.2.114 मृजेर्वृद्धिः was here while पाद ७.२ was a
           # stub reached ahead for मार्ष्टा; the pāda is read
           # through now — 7.2.1 to 7.2.118 — so it is read in
           # order like the rest and comes off the list.
           # 7.3.84 and 7.3.101 were here while पाद ७.३ was a
           # stub reached ahead for तरति and पचामि; the pāda is
           # read through now — 7.3.1 to 7.3.120 — so both are
           # read in order like the rest and come off the list.
           # 6.1.64 and 6.1.65 were here for नयति and एधते; the run
           # through 6.1 has passed them — 6.1.1 to 6.1.71 — so they
           # are read in order like the rest and come off the list.
           # and what completed the present paradigm of पच्. 6.1.97
           # and 6.1.101 were here too and are read in order now.
           # 7.1.3 झोऽन्तः was here while पाद ७.१ was a stub
           # reached ahead for पचन्ति; the pāda is read through
           # now — 7.1.1 to 7.1.103 — so it is read in order like
           # the rest and comes off the list.
           # 8.3.15 खरवसानयोर्विसर्जनीयः was here, reached ahead
           # for the visarga every स्-final word ends in. पाद ८.३
           # is read through now, 8.3.1 to 8.3.119, so it is read
           # in order like the rest and comes off the list. Its
           # CODE still lives in anga, which is why visarjaniya
           # names it in THE_VISARGA rather than restating it.
           # and what the second gaṇa needed. 2.4.72 was here while 2.4
           # was a stub reached ahead for it; the pāda is finished now —
           # 2.4.1 to 2.4.85 — so it is read in order like the rest and
           # belongs to no reached-ahead list. Same for 2.4.74 below.
           # 8.4.55 खरि च was the last name on this list, reached
           # ahead for the unvoicing every cluster passes through.
           # पाद ८.४ is read through now, 8.4.1 to 8.4.68, so it
           # comes off too — and with it the list is EMPTY. Nothing
           # in the Aṣṭādhyāyī is codified out of its place any
           # more, because every pāda has been read from its start.
           # The tests below are written to stay meaningful when
           # that is so.
           # and the reduplication slice, picked the same way — by working
           # backwards from लोलुवः and मरीमृजः, the two stems 1.1.4 turns
           # on. 6.1.1, 6.1.2 and 6.1.9 were here while 6.1 was a stub
           # reached ahead for them; the pada is being read through from
           # its start now — 6.1.1 to 6.1.44 — so all three are read in
           # order like the rest and belong to no reached-ahead list.
           # 7.4.59, 7.4.60, 7.4.66, 7.4.82, 7.4.83, 7.4.90 and 7.4.91
           # were here too — the seven that rewrite the copy, reached
           # ahead while 7.4 was a stub. पाद ७.४ is read through now,
           # 7.4.1 to 7.4.97, so all seven are read in order like the
           # rest and come off the list. Their CODE still lives apart,
           # in dvirvacana, because it builds the copy rather than
           # naming the operation — which is why abhyasa names them in
           # CODIFIED_APART instead of restating them.
           # and the five that carry लोलुवः the rest of the way: यङ् is
           # added, the stem it makes is itself a root, अच् comes after it
           # and elides the यङ्, and only then can उवङ् reach the ऊ.
           # 3.1.22 and 3.1.32 were here while 3.1 was a stub reached
           # ahead for the लोलुवः run. 3.1.1 to 3.1.32 is read in order
           # now, so they belong to no reached-ahead list.
           # 3.1.134 was reached ahead for the अच् that 1.1.4 turns
           # on. 3.1 is read through now — 1 to 150 — so it belongs
           # to no reached-ahead list either.
           # 6.4.77 इयङुवङौ was here too, reached ahead for
           # लोलुवः. 6.4.1 to 6.4.114 is read in order now, so it
           # belongs to no reached-ahead list either — though its
           # CODE still lives apart, in anga.iyan_uvan, because it
           # builds the form rather than naming the operation.
           )

    def test_the_reached_ahead_list_is_empty_now(self):
        """
        This used to loop over IDS and check each name was codified.
        The list is empty, so the loop would pass by doing nothing —
        which is not a test. What it asserts instead is the fact that
        emptied it: every pāda of the Aṣṭādhyāyī has been read from
        its start, so nothing is codified out of its place any more.

        A name added back here means the work reached ahead again,
        and this fails until the comment above it says why.
        """
        self.assertEqual(self.IDS, ())
        for sutra in self.IDS:  # pragma: no cover - empty by design
            self.assertTrue(REGISTRY.has(sutra), sutra)

    def test_everything_beyond_adhyaya_1_is_reached_ahead_or_in_order(self):
        """
        These eight were once the only sūtras codified beyond adhyāya 1, and
        this test asserted exactly that. It is no longer true — 2.1 is being
        worked through in order — and a snapshot that has to be rewritten
        every time the work advances is not testing anything.

        The property underneath it is what mattered, and it still holds:
        a sūtra outside adhyāya 1 is codified either because it was *reached
        ahead* of its place, being an interpretive rule the earlier work
        needed, or because its pāda is being read through from the start.
        Nothing is codified at random, and this fails if anything is.
        """
        by_pada = {}
        for sutra in REGISTRY.all():
            if sutra.id.adhyaya == 1:
                continue
            by_pada.setdefault(
                (sutra.id.adhyaya, sutra.id.pada), []).append(sutra.id.number)

        reached_ahead = set(self.IDS)
        for (adhyaya, pada), numbers in by_pada.items():
            # The reached-ahead rules are set aside FIRST, and what is
            # left must be the run 1..N. A pāda can be both — 2.4 is
            # read from its start while 2.4.72 and 2.4.74 were reached
            # ahead for लोलुवः — and asking whether the pāda as a whole
            # is contiguous fails every rule in the run because of two
            # rules that were never claimed to be part of it.
            in_order = sorted(
                n for n in numbers
                if f"{adhyaya}.{pada}.{n}" not in reached_ahead)
            run = list(range(1, len(in_order) + 1))
            for n in sorted(numbers):
                sutra_id = f"{adhyaya}.{pada}.{n}"
                if sutra_id in reached_ahead:
                    continue
                with self.subTest(sutra=sutra_id):
                    self.assertEqual(
                        in_order, run,
                        f"{sutra_id} is neither part of a run read from the "
                        f"start of its pāda nor one of the rules reached "
                        f"ahead; if it was picked deliberately, add it to "
                        f"IDS and say why. The pāda's in-order rules are "
                        f"{in_order}, which is not 1..{len(in_order)}.",
                    )

    def test_no_pada_is_left_half_read(self):
        """
        This used to check, of each name on IDS, that its pāda was
        not yet finished — a reached-ahead sūtra whose pāda has since
        been read through is no longer an exception and should come
        off the list. Every name came off, one pāda at a time, and
        the check has nothing left to iterate.

        The property that outlived it: every pāda in the work is
        either untouched or complete, and none is untouched.
        """
        from src.astadhyayi.sources import all_sutra_ids

        in_pada = {}
        for sutra_id in all_sutra_ids():
            adhyaya, pada, _ = (int(p) for p in sutra_id.split("."))
            in_pada.setdefault((adhyaya, pada), []).append(sutra_id)

        self.assertEqual(len(in_pada), 32)
        for key, ids in in_pada.items():
            done = [s for s in ids if REGISTRY.has(s)]
            with self.subTest(pada=key):
                self.assertEqual(len(done), len(ids))

    def test_8_2_1s_record_states_that_it_disables_1_4_2(self):
        notes = REGISTRY.get("8.2.1").notes
        self.assertIn("1.4.2", notes)
        self.assertIn("न प्रवर्तते", notes)

    def test_and_that_the_derivations_are_not_performed(self):
        """
        The Kāśikā works six forms through 8.2.1 and none is derived here.
        Claiming otherwise would be the easiest overclaim in the project, so
        the record has to say what is and is not codified.
        """
        notes = REGISTRY.get("8.2.1").notes
        self.assertIn("SCOPE", notes)
        self.assertIn("engine", notes)

    def test_8_2_3s_record_names_the_nine_uncodified_varttikas(self):
        notes = REGISTRY.get("8.2.3").notes
        self.assertIn("SCOPE", notes)
        for phrase in ("एकादेशस्वरोऽन्तरङ्गः", "सिज्लोप एकादेशे",
                       "श्चुत्वं धुटि"):
            self.assertIn(phrase, notes, phrase)


if __name__ == "__main__":
    unittest.main()
