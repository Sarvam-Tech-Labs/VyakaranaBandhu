# -*- coding: utf-8 -*-
"""
The compound section opens — 2.1.2 to 2.1.51.

What is worth testing here is not that each rule fires on its own example;
the provision table makes that nearly tautological. What is worth testing is
the structure the section is built out of, because every piece of it can be
got wrong in a way that still produces right-looking answers:

  * a heading that confers a name can quietly replace the name above it
    (2.1.3, and 1.4.1 would do exactly that if the प्राक् were not read);
  * a rule that restates an earlier one can be written as a second way to
    compound, which makes it idle (2.1.7) or makes it obligatory (2.1.15);
  * an option read off a heading can be written onto each rule instead, and
    then disagree with the heading;
  * a condition on the member the sūtra does *not* name can be dropped, and
    every wrong pair will still compound.

Each of those has its own test below, and each of them was a real defect in
this module before it was one.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.samasa import (
    PROVISIONS, Pair, Samasa, SAMJNAS, names_of, near_misses, resolve,
    saha_supa, samasa_of, samjna_over, tisthadgu,
)
from src.astadhyayi.sutra import REGISTRY
from src.astadhyayi.svara import NOT_PARANGAVAT, parangavat


# ---------------------------------------------------------------------------
# 2.1.3 — the प्राक् that keeps two names alive
# ---------------------------------------------------------------------------


class TheRangeIsWhatRestoresBothNames(unittest.TestCase):
    """
    प्राग्वचनं संज्ञासमावेशार्थम्. Without it 1.4.1 leaves one name and the
    later one, so समास would be conferred on nothing at all.
    """

    def test_a_rule_inside_both_ranges_confers_both_names(self):
        self.assertEqual(
            names_of("2.1.6"), {Samasa.SAMASA, Samasa.AVYAYIBHAVA})

    def test_and_a_pair_that_compounds_gets_both(self):
        got = samasa_of("upa", "kumbha", sense="samīpa")
        self.assertTrue(got.compounds)
        self.assertEqual(got.names, {Samasa.SAMASA, Samasa.AVYAYIBHAVA})

    def test_past_the_inner_heading_only_the_outer_one_reaches(self):
        """
        2.1.22 starts तत्पुरुष and अव्ययीभाव has run out at 2.1.21. If the
        inner range were not bounded, every tatpuruṣa would also be called
        an avyayībhāva — and the two names say opposite things about which
        member's meaning predominates.
        """
        self.assertEqual(
            names_of("2.1.24"), {Samasa.SAMASA, Samasa.TATPURUSA})
        self.assertNotIn(Samasa.AVYAYIBHAVA, names_of("2.1.24"))

    def test_before_the_range_there_is_no_compound_name_at_all(self):
        self.assertEqual(names_of("1.4.1"), frozenset())
        self.assertEqual(names_of("2.1.2"), frozenset())

    def test_the_ranges_do_not_merely_repeat_the_sutra_numbers(self):
        """
        A range whose end was copied from its own start would pass every
        test above. Each heading has to actually govern a stretch.
        """
        for heading in SAMJNAS:
            with self.subTest(heading=heading.sutra):
                self.assertNotEqual(heading.sutra, heading.through)
                self.assertTrue(heading.covers(heading.sutra))
                self.assertTrue(heading.covers(heading.through))

    def test_the_two_anvartha_names_say_opposite_things(self):
        """
        अन्वर्थसंज्ञा — the names are not labels. पूर्वपदार्थप्राधान्यम् for
        the one and उत्तरपदार्थप्रधानः for the other is the whole of what
        distinguishes them, so if both records said the same thing the
        distinction would be lost while every range still looked right.
        """
        by_name = {s.name: s for s in SAMJNAS}
        self.assertEqual(by_name[Samasa.AVYAYIBHAVA].pradhana, "pūrvapada")
        self.assertEqual(by_name[Samasa.TATPURUSA].pradhana, "uttarapada")

    def test_the_avyayibhava_verdict_carries_which_member_predominates(self):
        self.assertEqual(
            samasa_of("upa", "kumbha", sense="samīpa").pradhana, "pūrvapada")


# ---------------------------------------------------------------------------
# 2.1.4 — the yoga split
# ---------------------------------------------------------------------------


class TheSecondMemberIsNormallyANoun(unittest.TestCase):
    def test_a_subanta_compounds_with_a_subanta(self):
        self.assertTrue(saha_supa("sup").allowed)

    def test_a_finite_verb_only_in_vedic(self):
        """सहग्रहणं योगविभागार्थम्, तिङापि सह यथा स्यात् — and स च छन्दस्येव."""
        self.assertTrue(saha_supa("tiṅ", chandas=True).allowed)
        self.assertFalse(saha_supa("tiṅ").allowed)

    def test_the_split_is_recorded_as_a_split_and_not_as_a_second_rule(self):
        granted = saha_supa("tiṅ", chandas=True)
        self.assertTrue(granted.chandas_only)
        self.assertIn("योगविभाग", granted.why)

    def test_neither_of_the_two_is_refused_outright(self):
        self.assertFalse(saha_supa("kṛt").allowed)


# ---------------------------------------------------------------------------
# 2.1.7 and 2.1.15 — two restatements doing opposite work
# ---------------------------------------------------------------------------


class ARestatementIsNotASecondWayToCompound(unittest.TestCase):
    """
    Both name a word and a sense 2.1.6 already covers, and the Kāśikā gives
    different reasons — सादृश्यप्रतिषेधार्थम् against विभाषार्थम्. Written
    as ordinary provisions they would both be idle, and the section would
    lose a prohibition and an option.
    """

    def test_yatha_in_the_sense_of_likeness_compounds_by_nothing(self):
        """
        The defect this test was written for: with 2.1.7 written as a plain
        provision, यथा in सादृश्य still compounded — by 2.1.6, whose list of
        sixteen holds both यथा and सादृश्य. The sūtra exists to forbid
        exactly that, so the rule fired and did nothing.
        """
        got = samasa_of("yathā", "vṛddha", sense="sādṛśya")
        self.assertFalse(got.compounds)
        self.assertEqual(got.by, "2.1.7")

    def test_but_yatha_in_another_sense_does_compound(self):
        got = samasa_of("yathā", "vṛddha", sense="ānupūrvya")
        self.assertTrue(got.compounds)
        self.assertEqual(got.by, "2.1.7")

    def test_the_prohibition_does_not_leak_to_other_words(self):
        """
        2.1.7 confines यथा. It must not stop anything else from being used
        in the sense of similarity — सादृश्य is one of 2.1.6's sixteen and
        stays available to the rest.
        """
        got = samasa_of("upa", "kumbha", sense="sādṛśya")
        self.assertTrue(got.compounds)
        self.assertEqual(got.by, "2.1.6")

    def test_2_1_15_makes_a_compound_optional_rather_than_forbidding_it(self):
        """
        The other restatement, and the opposite outcome: समीप was already in
        2.1.6's list and obligatory there. Restated under 2.1.11 it becomes
        optional, which is the entire point — पुनर्वचनं विभाषार्थम्.
        """
        got = samasa_of("anu", "vana", sense="samīpa", given=["lakṣaṇa"])
        self.assertTrue(got.compounds)
        self.assertEqual(got.by, "2.1.15")
        self.assertTrue(got.optional)

    def test_and_the_same_sense_without_anu_stays_obligatory(self):
        self.assertFalse(
            samasa_of("upa", "kumbha", sense="samīpa").optional)

    def test_the_two_restatements_are_recorded_as_doing_different_work(self):
        by_sutra = {p.sutra: p for p in PROVISIONS}
        self.assertNotEqual(
            by_sutra["2.1.7"].restates, by_sutra["2.1.15"].restates)
        self.assertTrue(by_sutra["2.1.7"].niyama_on)
        self.assertFalse(by_sutra["2.1.15"].niyama_on)


# ---------------------------------------------------------------------------
# 2.1.11 — the option is read off the heading
# ---------------------------------------------------------------------------


class TheOptionComesFromTheHeading(unittest.TestCase):
    def test_everything_below_2_1_11_is_optional(self):
        for provision in PROVISIONS:
            pada, number = provision.sutra.rsplit(".", 1)
            # 2.1.11's heading governs 2.1 and no further. 2.2 has no
            # विभाषा overhead, which is why 2.2.3 has to say
            # अन्यतरस्याम् for itself.
            if pada != "2.1" or int(number) <= 11 or provision.nitya:
                continue
            with self.subTest(sutra=provision.sutra):
                self.assertTrue(provision.optional)

    def test_and_nothing_above_it_is(self):
        for provision in PROVISIONS:
            pada, number = provision.sutra.rsplit(".", 1)
            # The heading is 2.1.11's and governs its own pāda only, which
            # is what this test is about; 2.2 answers to nothing here.
            if pada != "2.1" or int(number) > 11:
                continue
            with self.subTest(sutra=provision.sutra):
                self.assertFalse(provision.optional)

    def test_2_1_21_escapes_the_heading_it_stands_under(self):
        """
        विभाषाधिकारेऽपि नित्यसमास एव अयम्, नहि वाक्येन संज्ञा गम्यते. The
        one exception, and it has a stated reason rather than being an
        oversight — a name cannot be conveyed by the phrase it replaces.
        """
        got = samasa_of("unmatta", "gaṅgā",
                        given=["nadī", "anya-padārtha", "saṃjñā"])
        self.assertTrue(got.compounds)
        self.assertEqual(got.by, "2.1.21")
        self.assertFalse(got.optional)

    def test_2_1_26_escapes_it_too_and_for_the_same_reason(self):
        """
        विभाषाधिकारेऽपि नित्यसमास एवायम्, नहि वाक्येन क्षेपो गम्यते. The
        second exception, arrived at by the identical argument: censure,
        like a proper name, is not something the phrase can carry, so there
        is no alternative for the option to offer.
        """
        got = samasa_of("khaṭvā", "ārūḍha", given=["kta", "kṣepa"],
                        first_vibhakti=2)
        self.assertTrue(got.compounds)
        self.assertEqual(got.by, "2.1.26")
        self.assertFalse(got.optional)

    def test_every_escape_states_why_the_phrase_will_not_do(self):
        """
        This began as a list of one — 2.1.21 — asserted by name, and 2.1.26
        broke it, correctly. A hardcoded roll of exceptions only records
        how many there were on the day it was written; what actually has to
        hold is that no rule escapes the heading silently.

        Both escapes argue the same way, नहि वाक्येन X गम्यते, and that
        phrase is the thing to insist on: a third exception without it is
        an oversight wearing a flag.
        """
        # Scoped to 2.1, where a विभाषा heading is running and a नित्य
        # rule is therefore ESCAPING something. In 2.2 there is no such
        # heading: 2.2.17 to 2.2.20 are obligatory because they say so,
        # with nothing overhead to argue against — so there is no phrase
        # for them to rule out and the demand would be empty.
        exceptions = [p for p in PROVISIONS
                      if p.nitya and p.sutra.startswith("2.1.")]
        self.assertTrue(exceptions)
        for provision in exceptions:
            with self.subTest(sutra=provision.sutra):
                self.assertIn(
                    "नहि वाक्येन", provision.gloss,
                    f"{provision.sutra} is नित्य under a विभाषा heading "
                    f"without saying what the phrase cannot convey")
                self.assertFalse(provision.optional)


# ---------------------------------------------------------------------------
# The conditions on the member the sūtra does not name
# ---------------------------------------------------------------------------


class TheOtherMemberIsConstrainedToo(unittest.TestCase):
    """
    2.1.10, 2.1.19 and 2.1.20 name one word and constrain the other. Written
    without that, any word at all compounds and every case still looks right
    — which is how the omission survived the first draft.
    """

    def test_pari_needs_aksa_salaka_or_a_numeral_before_it(self):
        self.assertTrue(samasa_of(
            "akṣa", "pari", given=["kitava-vyavahāra"]).compounds)
        self.assertTrue(samasa_of(
            "dvi", "pari", given=["kitava-vyavahāra"]).compounds)
        self.assertFalse(samasa_of(
            "devadatta", "pari", given=["kitava-vyavahāra"]).compounds)

    def test_2_1_19_needs_a_numeral_not_merely_a_vamsya(self):
        self.assertTrue(samasa_of("dvi", "muni", given=["vaṃśya"]).compounds)
        self.assertFalse(
            samasa_of("devadatta", "muni", given=["vaṃśya"]).compounds)

    def test_the_numeral_test_is_1_1_23s_and_not_a_second_list(self):
        """
        बहु, गण, वतु and डति are saṃkhyā by 1.1.23 without being numerals,
        and a hand-written list of digits here would miss them. This is the
        DRY claim made testable: the section asks 1.1.23, so it inherits the
        four.
        """
        self.assertTrue(samasa_of("bahu", "muni", given=["vaṃśya"]).compounds)
        self.assertTrue(
            samasa_of("viṃśati", "muni", given=["vaṃśya"]).compounds)

    def test_the_singular_condition_falls_on_aksa_and_salaka_only(self):
        """
        कितवव्यवहारे च एकत्वे अक्षशलाकयोः — the singular is required of
        those two and not of the numerals beside them, or द्विपरि and
        त्रिपरि would be excluded by their own rule.
        """
        self.assertFalse(samasa_of(
            "akṣa", "pari", first_vacana=2,
            given=["kitava-vyavahāra"]).compounds)
        self.assertTrue(samasa_of(
            "dvi", "pari", first_vacana=2,
            given=["kitava-vyavahāra"]).compounds)

    def test_the_ablative_rules_want_the_ablative(self):
        self.assertTrue(
            samasa_of("apa", "trigarta", second_vibhakti=5).compounds)
        self.assertFalse(
            samasa_of("apa", "trigarta", second_vibhakti=2).compounds)
        self.assertFalse(samasa_of("apa", "trigarta").compounds)

    def test_and_2_1_18_wants_the_genitive(self):
        self.assertTrue(
            samasa_of("pāre", "gaṅgā", second_vibhakti=6).compounds)
        self.assertFalse(
            samasa_of("pāre", "gaṅgā", second_vibhakti=5).compounds)


# ---------------------------------------------------------------------------
# 2.1.1 gates the section
# ---------------------------------------------------------------------------


class NothingCompoundsUntilTheWordsAreConnected(unittest.TestCase):
    def test_an_unstated_connection_withholds_the_answer(self):
        got = resolve(Pair("upa", "kumbha", first_sense=("samīpa",),
                           connected=None))
        self.assertFalse(got.compounds)
        self.assertEqual(got.by, "2.1.1")

    def test_words_adjacent_by_accident_do_not_compound(self):
        """
        The paribhāṣā's own counter-examples are all of this shape: two
        words next to each other across a break, with no relation between
        them.
        """
        got = resolve(Pair("upa", "kumbha", first_sense=("samīpa",),
                           connected=False))
        self.assertFalse(got.compounds)
        self.assertEqual(got.by, "2.1.1")

    def test_and_it_is_checked_before_the_rules_not_after(self):
        """
        If the table ran first, an unconnected pair would be reported as
        compounding by 2.1.6 and refused afterwards — the right answer with
        the wrong sūtra on it, which is the failure mode this codification
        keeps meeting.
        """
        got = resolve(Pair("upa", "kumbha", first_sense=("samīpa",),
                           connected=False))
        self.assertNotIn("2.1.6", got.by)


# ---------------------------------------------------------------------------
# 2.1.17 — a closed gaṇa, read from the gaṇapāṭha
# ---------------------------------------------------------------------------


class TheTisthadguFormsAreGivenNotMade(unittest.TestCase):
    def test_the_gana_is_read_from_the_corpus(self):
        forms = tisthadgu()
        self.assertGreater(len(forms), 20)
        self.assertIn("tiṣṭhadgu", forms)

    def test_a_member_of_it_bears_the_name(self):
        got = samasa_of("tiṣṭhadgu", "tiṣṭhadgu")
        self.assertTrue(got.compounds)
        self.assertEqual(got.by, "2.1.17")

    def test_a_word_outside_it_does_not(self):
        self.assertFalse(samasa_of("devadatta", "gaṇa").compounds)

    def test_the_lookup_is_the_one_nipata_uses(self):
        """
        The reader was lifted out of nipata.py rather than copied, and the
        copy in this module had the dictionary keyed wrong — it returned an
        empty gaṇa, so 2.1.17 matched nothing and every test of it passed
        by never reaching the rule. One reader is the fix; this asserts
        both callers still get their gaṇas.
        """
        from src.astadhyayi.formation import gana_items
        from src.astadhyayi.nipata import cadi, pradi

        self.assertEqual(tisthadgu(), gana_items("2.1.17", "tiṣṭhadgu"))
        self.assertEqual(len(pradi()), 22)
        self.assertGreater(len(cadi()), 100)


# ---------------------------------------------------------------------------
# 2.1.2 — an atideśa, and only for accent
# ---------------------------------------------------------------------------


class ParangavatReachesAccentAndNothingElse(unittest.TestCase):
    def test_it_holds_for_accent(self):
        self.assertTrue(parangavat().holds)

    def test_each_kim_in_the_kasika_is_a_condition(self):
        self.assertFalse(parangavat(preceding_is_sup=False).holds)
        self.assertFalse(parangavat(following_is_amantrita=False).holds)

    def test_satva_and_natva_are_refused_by_name(self):
        """
        षत्वणत्वे प्रति पराङ्गवद् न भवति: कूपे सिञ्चन्, चर्म नमन्. Both are
        in the code as data with the sūtra that would have done them, so
        the refusal cites 8.3.59 and 8.4.2 rather than merely declining.
        """
        for operation, sutra in NOT_PARANGAVAT:
            with self.subTest(operation=operation):
                got = parangavat(operation=operation)
                self.assertFalse(got.holds)
                self.assertIn(sutra, got.why)

    def test_the_vat_leaves_the_word_its_own_operations(self):
        """वत्करणं किम्? स्वाश्रयमपि कार्यं यथा स्यात्."""
        self.assertTrue(parangavat().keeps_own)


# ---------------------------------------------------------------------------
# What the section hands on
# ---------------------------------------------------------------------------


class TheSectionMeetsWhatWasCodifiedBefore(unittest.TestCase):
    def test_1_1_41_makes_the_compound_itself_an_avyaya(self):
        """
        अव्ययीभावश्च — the fifth of 1.1.37–41's five ways of being
        indeclinable is the compound this section defines, so the two
        modules describe one thing from two sides.
        """
        from src.astadhyayi.avyaya import avyaya, is_avyaya

        got = avyaya("upakumbham", avyayibhava=True)
        self.assertIsNotNone(got)
        self.assertEqual(got.by, "1.1.41")
        self.assertTrue(is_avyaya("upakumbham", avyayibhava=True))
        # and the compound has to be asserted — the form alone says nothing,
        # since उपकुम्भम् is spelled like any other neuter accusative.
        self.assertFalse(is_avyaya("upakumbham"))

    def test_near_misses_say_what_each_rule_wanted(self):
        missed = dict(near_misses(Pair("apa", "trigarta", connected=True)))
        self.assertIn("2.1.12", missed)
        self.assertTrue(
            any("vibhakti 5" in reason for reason in missed["2.1.12"]),
            missed["2.1.12"])

    def test_every_sutra_of_the_pada_so_far_is_registered(self):
        for number in range(1, 22):
            sutra_id = f"2.1.{number}"
            with self.subTest(sutra=sutra_id):
                self.assertTrue(REGISTRY.has(sutra_id))

    def test_each_provision_belongs_to_a_registered_sutra(self):
        for provision in PROVISIONS:
            with self.subTest(sutra=provision.sutra):
                self.assertTrue(REGISTRY.has(provision.sutra))
                self.assertTrue(samjna_over(provision.sutra))


if __name__ == "__main__":
    unittest.main()


class TheTatpurusaHeadingTakesOver(unittest.TestCase):
    """
    2.1.22 तत्पुरुषः, and the six rules under it.

    The interesting failures here are not "does 2.1.24 fire on कष्टश्रितः".
    They are the ones a second heading makes possible for the first time: a
    pradhāna read from the wrong heading, a case-condition on the member the
    sūtra does *not* name, and an anuvṛtti that has to pass through two
    sūtras without biting.
    """

    def test_the_heading_covers_from_2_1_22_to_2_2_22(self):
        """प्राग्बहुव्रीहेः — up to but not including 2.2.23."""
        heading, = [s for s in SAMJNAS if s.name is Samasa.TATPURUSA]
        self.assertTrue(heading.covers("2.1.24"))
        self.assertTrue(heading.covers("2.2.22"))
        self.assertFalse(heading.covers("2.1.21"))
        self.assertFalse(heading.covers("2.2.23"))

    def test_the_two_headings_say_opposite_things_about_meaning(self):
        """
        उत्तरपदार्थप्रधानस् तत्पुरुषः against पूर्वपदार्थप्राधान्यम्
        अव्ययीभावस्य. That is the whole difference between the two
        compounds, and it is recorded on the names rather than in prose.
        """
        by_name = {s.name: s for s in SAMJNAS}
        self.assertEqual(by_name[Samasa.TATPURUSA].pradhana, "uttarapada")
        self.assertEqual(by_name[Samasa.AVYAYIBHAVA].pradhana, "pūrvapada")

    def test_a_tatpurusa_verdict_reports_its_own_pradhana(self):
        """
        The scar. resolve() asked SAMJNAS specifically for the अव्ययीभाव
        heading, so a तत्पुरुष verdict came back with an empty pradhāna —
        silently wrong for every rule in this section while every
        avyayībhāva test went on passing.
        """
        tp = resolve(Pair("kaṣṭa", "śrita", connected=True, first_vibhakti=2))
        self.assertEqual(tp.pradhana, "uttarapada")
        ab = resolve(Pair("upa", "kumbha", connected=True,
                          first_sense=("samīpa",)))
        self.assertEqual(ab.pradhana, "pūrvapada")

    def test_2_1_24_wants_the_case_on_the_member_it_does_not_name(self):
        """
        द्वितीया श्रितादिभिः names the *second* member and puts the case on
        the first. Every avyayībhāva rule runs the other way round, so
        `Pair` carried no first_vibhakti at all and the check read a field
        that was never there — a condition no pair could meet, which is the
        same family of defect as a test that cannot fail.
        """
        self.assertTrue(
            resolve(Pair("kaṣṭa", "śrita", connected=True,
                         first_vibhakti=2)).compounds)
        self.assertFalse(
            resolve(Pair("kaṣṭa", "śrita", connected=True)).compounds)
        # A sixth-case first member used to compound by nothing, and now
        # makes a genitive tatpuruṣa — 2.2.8 was written after this test.
        # What 2.1.24 wants is the SECOND case, and that is what holds.
        self.assertEqual(
            resolve(Pair("kaṣṭa", "śrita", connected=True,
                         first_vibhakti=6)).by, "2.2.8")

    def test_all_seven_of_2_1_24_and_the_varttika_three(self):
        """The Kāśikā's own worked forms, second member by second member."""
        worked = {
            "śrita": "kaṣṭa", "atīta": "kāntāra", "patita": "naraka",
            "gata": "grāma", "atyasta": "taraṅga", "prāpta": "sukha",
            "āpanna": "sukha",
            # श्रितादिषु गमिगाम्यादीनाम् उपसंख्यानम्
            "gamī": "grāma", "gāmī": "grāma", "bubhukṣu": "odana",
        }
        for second, first in worked.items():
            with self.subTest(word=second):
                verdict = resolve(Pair(first, second, connected=True,
                                       first_vibhakti=2))
                self.assertTrue(verdict.compounds, f"{first} + {second}")
                self.assertEqual(verdict.by, "2.1.24")
                self.assertIn(Samasa.TATPURUSA, verdict.names)

    def test_the_dvitiya_passes_through_2_1_25_and_2_1_27(self):
        """
        स्वयम् and सामि are avyayas naming no thing, so neither can stand in
        the second case: तस्य द्वितीयया सह संबन्धो नोपपद्यते, and
        असत्त्ववाचित्वाद् द्वितीयया नास्ति संबन्धः. The Kāśikā keeps the
        anuvṛtti alive anyway — द्वितीयाग्रहणम् उत्तरार्थम् अनुवर्तते —
        because 2.1.26 and 2.1.28 still need it.

        So these two must compound with no case stated, while 2.1.26 and
        2.1.28 must refuse without one. Writing द्वितीया onto every rule of
        the run breaks the first pair; dropping it breaks the second.
        """
        for word, other in (("svayam", "dhauta"), ("sāmi", "kṛta")):
            with self.subTest(word=word):
                self.assertTrue(
                    resolve(Pair(word, other, connected=True,
                                 given=("kta",))).compounds)
        for word, other, facts in (
                ("khaṭvā", "ārūḍha", ("kta", "kṣepa")),
                ("ahar", "saṃkrānta", ("kāla", "kta"))):
            with self.subTest(word=word):
                self.assertFalse(
                    resolve(Pair(word, other, connected=True,
                                 given=facts)).compounds,
                    f"{word} compounded with no case stated")

    def test_2_1_26_is_obligatory_although_vibhasa_still_governs(self):
        """
        नहि वाक्येन क्षेपो गम्यते — the phrase cannot carry the censure, so
        there is nothing to fall back to and the compound is नित्य even
        under 2.1.11. Its neighbours in the same run are optional, which is
        what makes the exception worth holding.
        """
        censure = resolve(Pair("khaṭvā", "ārūḍha", connected=True,
                               first_vibhakti=2, given=("kta", "kṣepa")))
        self.assertTrue(censure.compounds)
        self.assertEqual(censure.by, "2.1.26")
        self.assertFalse(censure.optional)

        for pair in (Pair("kaṣṭa", "śrita", connected=True, first_vibhakti=2),
                     Pair("sāmi", "kṛta", connected=True, given=("kta",))):
            with self.subTest(by=resolve(pair).by):
                self.assertTrue(resolve(pair).optional)

    def test_without_censure_khatva_compounds_by_nothing(self):
        """क्षेप इति किम्? खट्वाम् आरूढः — a man who climbed onto a bed."""
        plain = resolve(Pair("khaṭvā", "ārūḍha", connected=True,
                             first_vibhakti=2, given=("kta",)))
        self.assertFalse(plain.compounds)

    def test_2_1_29_drops_the_kta_that_2_1_28_requires(self):
        """
        कालाः इति वर्तते, क्तेनेति निवृत्तम् — the time-words carry down and
        the क्त does not. That single difference is why 2.1.29 exists, so
        मुहूर्तसुखम् must form although सुख is no participle, and 2.1.28
        must refuse the very same pair.
        """
        sukha = Pair("muhūrta", "sukha", connected=True, first_vibhakti=2,
                     given=("kāla", "atyanta-saṃyoga"))
        verdict = resolve(sukha)
        self.assertTrue(verdict.compounds)
        self.assertEqual(verdict.by, "2.1.29")

        self.assertTrue(
            all(p.unmet(sukha) for p in PROVISIONS if p.sutra == "2.1.28"),
            "2.1.28 reached a pair with no क्त in it")

    def test_where_both_time_rules_reach_a_pair_the_later_stands(self):
        """
        A time-word, in the second case, with a क्त-form, the hour wholly
        filled: 2.1.28 and 2.1.29 both reach it and 1.4.1 settles it. No
        precedence is written into this section — the same eka_samjna that
        decides 1.4.10 against 1.4.11 decides this.
        """
        both = Pair("sarvarātra", "śobhana", connected=True, first_vibhakti=2,
                    given=("kāla", "kta", "atyanta-saṃyoga"))
        # Scoped to this pāda: the point is which of the two TIME rules
        # takes it, and rules from 2.2 reaching the same pair is a
        # different question that 1.4.1 answers the same way.
        reached = {p.sutra for p in PROVISIONS
                   if p.sutra.startswith("2.1.") and p.applies(both)}
        self.assertEqual(reached, {"2.1.28", "2.1.29"})
        self.assertEqual(resolve(both).by, "2.1.29")

    def test_a_heading_joins_nothing_by_itself(self):
        """
        2.1.22 and 2.1.23 confer names; they compound no pair. A heading
        that quietly formed compounds would make the section's refusals
        meaningless.
        """
        for sutra in ("2.1.22", "2.1.23"):
            with self.subTest(sutra=sutra):
                self.assertEqual(
                    [p for p in PROVISIONS if p.sutra == sutra], [])
                self.assertIn(Samasa.TATPURUSA, names_of(sutra))


class TheTatpurusaByCase(unittest.TestCase):
    """
    2.1.30 to 2.1.40, where the section stops naming senses and starts
    naming cases: third, fourth, fifth, seventh, each with the words it
    pairs with.

    The failure this run makes available for the first time is a rule
    filed the wrong way round. Every earlier तत्पुरुष names the second
    member and puts the case on the first, so a provision written that way
    passes on all of them — and 2.1.39 is the one that runs the other way.
    """

    def test_the_third_case_rules(self):
        """शङ्कुलाखण्डः, धान्यार्थः, मासपूर्वः, अहिहतः, काकपेया, दध्योदनः."""
        worked = [
            ("śaṅkulā", "khaṇḍa", ("guṇavacana", "tatkṛta"), "2.1.30"),
            ("dhānya", "artha", (), "2.1.30"),
            ("māsa", "pūrva", (), "2.1.31"),
            ("māsa", "avara", (), "2.1.31"),
            ("ahi", "hata", ("kartṛ-karaṇa", "kṛdanta"), "2.1.32"),
            ("kāka", "peya", ("kartṛ-karaṇa", "adhikārtha"), "2.1.33"),
            ("dadhi", "odana", ("vyañjana", "anna"), "2.1.34"),
            ("guḍa", "dhānā", ("miśrīkaraṇa", "bhakṣya"), "2.1.35"),
        ]
        for first, second, facts, by in worked:
            with self.subTest(pair=f"{first}+{second}"):
                got = resolve(Pair(first, second, connected=True,
                                   first_vibhakti=3, given=facts))
                self.assertTrue(got.compounds)
                self.assertEqual(got.by, by)
                self.assertIn(Samasa.TATPURUSA, got.names)

    def test_the_fourth_fifth_and_seventh_case_rules(self):
        """यूपदारु, कुबेरबलिः, वृकभयम्, सुखापेतः, स्तोकान्मुक्तः, अक्षशौण्डः."""
        worked = [
            (4, "yūpa", "dāru", ("prakṛti-vikāra",), "2.1.36"),
            (4, "brāhmaṇa", "artha", (), "2.1.36"),
            (4, "kubera", "bali", (), "2.1.36"),
            (5, "vṛka", "bhaya", (), "2.1.37"),
            (5, "vṛka", "bhīta", (), "2.1.37"),
            (5, "sukha", "apeta", ("alpaśaḥ",), "2.1.38"),
            (5, "stoka", "mukta", ("kta",), "2.1.39"),
            (7, "akṣa", "śauṇḍa", (), "2.1.40"),
        ]
        for case, first, second, facts, by in worked:
            with self.subTest(pair=f"{first}+{second}"):
                got = resolve(Pair(first, second, connected=True,
                                   first_vibhakti=case, given=facts))
                self.assertTrue(got.compounds)
                self.assertEqual(got.by, by)

    def test_2_1_39_names_the_first_member_not_the_second(self):
        """
        स्तोकान्तिकदूरार्थकृच्छ्राणि क्तेन — the named words stand in the
        FIFTH case themselves and compound with a क्त-form. Every other
        rule in this run names the second member, so a provision written
        that way passes everywhere else and fails only here.

        It was written that way, and स्तोकान्मुक्तः compounded by nothing.
        """
        self.assertTrue(
            resolve(Pair("stoka", "mukta", connected=True, first_vibhakti=5,
                         given=("kta",))).compounds)
        self.assertFalse(
            resolve(Pair("mukta", "stoka", connected=True, first_vibhakti=5,
                         given=("kta",))).compounds)

    def test_the_arthas_are_open_and_the_synonyms_reach(self):
        """
        …अर्थ in 2.1.39 means "words with that SENSE", so the Kāśikā's own
        अभ्याश and विप्रकृष्ट stand beside अन्तिक and दूर.
        """
        for word in ("antika", "abhyāśa", "dūra", "viprakṛṣṭa", "kṛcchra"):
            with self.subTest(word=word):
                self.assertTrue(
                    resolve(Pair(word, "āgata", connected=True,
                                 first_vibhakti=5,
                                 given=("kta",))).compounds)

    def test_tatkrtena_iti_kim_aksna_kanah(self):
        """
        तत्कृतेनेति किम्? अक्ष्णा काणः — blind IN the eye, not blinded BY
        it. The quality must be one the instrumental brought about, and
        without that stated the rule withholds rather than guessing.
        """
        self.assertFalse(
            resolve(Pair("akṣi", "kāṇa", connected=True, first_vibhakti=3,
                         given=("guṇavacana",))).compounds)

    def test_alpasah_keeps_2_1_38_from_reaching_everything(self):
        """
        अल्पा पञ्चमी समस्यते न सर्वा. प्रासादात् पतितः has the same shape
        as स्वर्गपतितः and does not compound, so the rule asks rather than
        deciding for itself.
        """
        self.assertTrue(
            resolve(Pair("svarga", "patita", connected=True,
                         first_vibhakti=5, given=("alpaśaḥ",))).compounds)
        self.assertFalse(
            resolve(Pair("prāsāda", "patita", connected=True,
                         first_vibhakti=5)).compounds)

    def test_each_rule_wants_its_own_case(self):
        """
        The cases are what tell these rules apart, so a pair offered in
        the wrong one must compound by nothing — not by a neighbour.
        """
        wrong = [
            ("māsa", "pūrva", 2), ("kubera", "bali", 3),
            ("vṛka", "bhaya", 4), ("akṣa", "śauṇḍa", 5),
        ]
        for first, second, case in wrong:
            with self.subTest(pair=f"{first}+{second}", case=case):
                self.assertFalse(
                    resolve(Pair(first, second, connected=True,
                                 first_vibhakti=case)).compounds)

    def test_2_1_32_records_its_bahulam_rather_than_running_it(self):
        """
        सर्वोपाधिव्यभिचारार्थं बहुलग्रहणम् — the word is there so that any
        condition may be departed from. दात्रेण धान्यं लूनवान् meets them
        and does not compound; पादहारकः does not and compounds.

        A rule that may ignore its own conditions cannot be run in either
        direction and be honest, so the flag is set and the resolver still
        asks for the conditions. Recording that it is only part of the
        story is the point.
        """
        bahula = [p for p in PROVISIONS if p.bahula]
        self.assertEqual([p.sutra for p in bahula], ["2.1.32", "2.1.57"])
        for row in bahula:
            with self.subTest(sutra=row.sutra):
                self.assertIn("बहुल", row.gloss)

    def test_the_two_bahulams_are_there_for_different_reasons(self):
        """
        Started as a list of one and 2.1.57 broke it, correctly — the same
        way the नित्य roll broke. What holds is not how many there are but
        that each says what its बहुलम् is FOR, since the Kāśikā gives the
        two different work: सर्वोपाधिव्यभिचारार्थं at 2.1.32, where any
        condition may be departed from, and व्यवस्थार्थम् at 2.1.57, where
        it is settled case by case — always for कृष्णसर्पः, never for
        रामो जामदग्न्यः, either way for नीलोत्पलम्.
        """
        purposes = {p.sutra: p.gloss for p in PROVISIONS if p.bahula}
        self.assertIn("सर्वोपाधिव्यभिचारार्थ", purposes["2.1.32"])
        self.assertIn("व्यवस्थार्थ", purposes["2.1.57"])

    def test_saundadi_is_read_from_the_ganapatha(self):
        """
        Thirteen words, and not retyped here: a list copied into the
        source is a second witness that can drift from the first with
        nothing to notice it. Same reason as 2.1.17's तिष्ठद्गु.
        """
        from src.astadhyayi.corpus import load_ganapatha
        from src.astadhyayi.samasa import SAUNDADI

        gana = next(g for g in load_ganapatha()["2.1.40"]
                    if g.name.startswith("śauṇḍādi"))
        self.assertEqual(SAUNDADI, gana.items)
        self.assertEqual(len(SAUNDADI), 13)
        for word in ("śauṇḍa", "dhūrta", "kitava", "nipuṇa"):
            self.assertIn(word, SAUNDADI)

    def test_every_rule_of_the_run_confers_tatpurusa(self):
        """
        They stand under 2.1.22, so whatever they join is a तत्पुरुष and
        its latter member carries the meaning.
        """
        for number in range(30, 41):
            sutra = f"2.1.{number}"
            with self.subTest(sutra=sutra):
                rows = [p for p in PROVISIONS if p.sutra == sutra]
                self.assertTrue(rows)
                for row in rows:
                    self.assertIs(row.gives, Samasa.TATPURUSA)
                self.assertIn(Samasa.TATPURUSA, names_of(sutra))


class TheSeventhCaseAndThenAgreement(unittest.TestCase):
    """
    2.1.41 to 2.1.51. The locative run finishes, and then the section
    changes footing entirely: 2.1.49 onward pair words not by case at all
    but by समानाधिकरण, the two referring to one thing.
    """

    def test_the_seventh_case_run(self):
        """स्थालीपक्वः, तीर्थध्वाङ्क्षः, मासदेयम्, अरण्येतिलकाः, भस्मनिहुतम्."""
        worked = [
            ("sthālī", "pakva", (), "2.1.41"),
            ("tīrtha", "dhvāṅkṣa", ("dhvāṅkṣa", "kṣepa"), "2.1.42"),
            ("māsa", "deya", ("kṛtya-yat", "ṛṇa"), "2.1.43"),
            ("araṇya", "tilaka", ("saṃjñā",), "2.1.44"),
            ("pūrvāhṇa", "kṛta", ("ahorātra-avayava", "kta"), "2.1.45"),
            ("tatra", "bhukta", ("kta",), "2.1.46"),
            ("bhasman", "huta", ("kta", "kṣepa"), "2.1.47"),
        ]
        for first, second, facts, by in worked:
            with self.subTest(pair=f"{first}+{second}"):
                got = resolve(Pair(first, second, connected=True,
                                   first_vibhakti=7, given=facts))
                self.assertTrue(got.compounds)
                self.assertEqual(got.by, by)

    def test_2_1_44_is_obligatory_for_the_same_reason_2_1_21_is(self):
        """
        नहि वाक्येन संज्ञा गम्यते. A name cannot be conveyed by the phrase
        it replaces, so there is nothing for the option to offer — the
        third escape from 2.1.11, arrived at by the identical argument.
        """
        got = resolve(Pair("araṇya", "tilaka", connected=True,
                           first_vibhakti=7, given=("saṃjñā",)))
        self.assertEqual(got.by, "2.1.44")
        self.assertFalse(got.optional)

    def test_avayava_iti_kim_the_whole_day_is_not_a_part_of_one(self):
        """अवयवग्रहणं किम्? अहनि भुक्तम्, रात्रौ वृत्तम्."""
        self.assertFalse(
            resolve(Pair("ahar", "bhukta", connected=True, first_vibhakti=7,
                         given=("kta",))).compounds)

    def test_the_two_censure_rules_need_the_censure(self):
        """क्षेप इति किम्? तीर्थे ध्वाङ्क्षस्तिष्ठति — a crow at a ford."""
        self.assertFalse(
            resolve(Pair("tīrtha", "dhvāṅkṣa", connected=True,
                         first_vibhakti=7, given=("dhvāṅkṣa",))).compounds)
        self.assertFalse(
            resolve(Pair("bhasman", "huta", connected=True,
                         first_vibhakti=7, given=("kta",))).compounds)

    def test_nipatana_now_carries_its_forms_instead_of_a_flag(self):
        """
        2.1.17 तिष्ठद्गुप्रभृति and 2.1.48 पात्रेसमितादि are both given
        whole — समुदाया एव निपात्यन्ते — and they are different lists.

        The field was a bool wired to one of them, which is a flag that
        stands for one particular answer. It holds the forms now, and both
        rules read theirs from the gaṇapāṭha.
        """
        from src.astadhyayi.samasa import PATRESAMITADI

        rows = {p.sutra: p for p in PROVISIONS if p.nipatana}
        self.assertEqual(sorted(rows), ["2.1.17", "2.1.48", "2.1.72"])
        self.assertEqual(rows["2.1.48"].nipatana, PATRESAMITADI)
        self.assertEqual(len(PATRESAMITADI), 33)

        # Three lists, and no two of them the same — which is the whole
        # reason the field cannot be a flag.
        lists = [row.nipatana for row in rows.values()]
        self.assertEqual(len(lists), len({tuple(x) for x in lists}))
        for sutra, row in rows.items():
            with self.subTest(sutra=sutra):
                self.assertTrue(row.nipatana)

    def test_2_1_48_is_read_from_the_ganapatha_and_stays_open(self):
        """
        अव्यक्तत्वाच्च आकृतिगणोऽयम् — what makes these compounds insulting
        cannot be spelt out, so the list cannot be closed. The file marks
        it open, and that is read rather than asserted here.
        """
        from src.astadhyayi.corpus import load_ganapatha
        from src.astadhyayi.samasa import PATRESAMITADI

        gana = next(g for g in load_ganapatha()["2.1.48"]
                    if g.name.startswith("pātresamitādi"))
        self.assertTrue(gana.open_ended)
        self.assertEqual(PATRESAMITADI, gana.items)

        self.assertTrue(
            resolve(Pair("kūpamaṇḍūkaḥ", "kūpamaṇḍūkaḥ", connected=True,
                         given=("kṣepa",))).compounds)
        self.assertFalse(
            resolve(Pair("devadatta", "devadatta", connected=True,
                         given=("kṣepa",))).compounds)

    def test_the_agreement_rules_pair_by_reference_not_by_case(self):
        """
        2.1.49 to 2.1.51 ask समानाधिकरण instead of a vibhakti — the two
        words refer to one thing, whatever made each of them apt. So no
        case is stated for these and they still compound.
        """
        worked = [
            ("pūrvakāla", "anulipta", ("samānādhikaraṇa",), "2.1.49"),
            ("eka", "śāṭī", ("samānādhikaraṇa",), "2.1.49"),
            # 2.1.58's nine words include पूर्व, and this is that word
            # with a name meant — so both rules reach it. See the test
            # below for which wins and why.
            ("pūrva", "iṣukāmaśamī",
             ("dik", "samānādhikaraṇa", "saṃjñā"), "2.1.50"),
            ("pañcan", "āmra", ("samānādhikaraṇa", "saṃjñā"), "2.1.50"),
        ]
        for first, second, facts, by in worked:
            with self.subTest(pair=f"{first}+{second}"):
                got = resolve(Pair(first, second, connected=True,
                                   given=facts))
                self.assertTrue(got.compounds)
                self.assertEqual(got.by, by)

    def test_samanadhikarana_iti_kim_ekasyah_sati(self):
        """समानाधिकरणेनेति किम्? एकस्याः शाटी — a garment OF one woman."""
        self.assertFalse(
            resolve(Pair("eka", "śāṭī", connected=True)).compounds)

    def test_2_1_50_wants_a_name_and_2_1_51_wants_one_of_three_others(self):
        """
        संज्ञायामिति किम्? उत्तरा वृक्षाः, पञ्च ब्राह्मणाः. Without a name
        2.1.50 does not reach — and 2.1.51 then covers the numeral in
        three other settings instead.
        """
        self.assertFalse(
            resolve(Pair("pañcan", "brāhmaṇa", connected=True,
                         given=("samānādhikaraṇa",))).compounds)
        for fact, by in (("samāhāra", "2.1.51"), ("taddhitārtha", "2.1.51"),
                         ("uttarapada", "2.1.51")):
            with self.subTest(fact=fact):
                got = resolve(Pair("pañcan", "kapāla", connected=True,
                                   given=("samānādhikaraṇa", fact)))
                self.assertTrue(got.compounds)
                self.assertEqual(got.by, by)

    def test_a_direction_word_cannot_be_an_aggregate(self):
        """
        समाहारे दिक्शब्दो न संभवति. 2.1.51's three settings carry
        दिक्संख्ये down from 2.1.50, but only the numeral reaches the
        aggregate — so the समाहार row asks for a saṃkhyā and नothing else.
        """
        rows = [p for p in PROVISIONS
                if p.sutra == "2.1.51" and "samāhāra" in p.requires]
        self.assertEqual(len(rows), 1)
        self.assertTrue(rows[0].samkhya)

    def test_every_worked_input_of_the_pada_offers_actual_words(self):
        """
        A ready-made input exists so the rule can be run by someone who
        does not know what to type. From 2.1.30 the conditions stopped
        naming words and started asserting facts, and the generated inputs
        came out as a form of ticked boxes with nothing to compound —
        runnable only by a reader who did not need it.
        """
        from src.astadhyayi.cases import cases_for

        for number in range(1, 52):
            sutra = f"2.1.{number}"
            if not REGISTRY.has(sutra):
                continue
            for case in cases_for(sutra):
                if "first" not in case.values and "second" not in case.values:
                    continue
                with self.subTest(sutra=sutra, case=case.label):
                    self.assertIn("first", case.values)
                    self.assertIn("second", case.values)


class WhenTwoAgreementRulesReachOnePair(unittest.TestCase):
    """
    2.1.50 दिक्संख्ये संज्ञायाम् and 2.1.58 पूर्वापर… collide on the
    Kāśikā's own examples: पूर्वेषुकामशमी and अपरेषुकामशमी are two of
    2.1.58's nine words with a name meant.

    1.4.1 alone hands it to 2.1.58, being later. The Kāśikā cites the form
    under 2.1.50, which is the narrower rule — it asks for a direction AND
    a name where 2.1.58 asks for neither. That reading is the one taken,
    and it is marked OPEN on the rule: nothing read so far says in as many
    words that 2.1.58 stands off where a name is meant.
    """

    def test_a_name_goes_to_2_1_50_and_anything_else_to_2_1_58(self):
        named = resolve(Pair("pūrva", "iṣukāmaśamī", connected=True,
                             given=("dik", "samānādhikaraṇa", "saṃjñā")))
        self.assertEqual(named.by, "2.1.50")

        ordinary = resolve(Pair("pūrva", "puruṣa", connected=True,
                                given=("samānādhikaraṇa",)))
        self.assertEqual(ordinary.by, "2.1.58")

    def test_the_holding_off_is_recorded_on_the_rule_not_hidden(self):
        """
        A rule kept away from a case it would otherwise reach has to say
        so where the rule is written, or the next reader finds a table
        that quietly disagrees with the sūtra it claims to be.
        """
        row, = [p for p in PROVISIONS if p.sutra == "2.1.58"]
        self.assertEqual(row.refuses, ("saṃjñā",))
        self.assertIn("2.1.50", row.gloss)
