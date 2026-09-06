# -*- coding: utf-8 -*-
"""
Tests for 1.4.1 to 1.4.22 — the two paribhāṣās, and the nominal saṃjñās.

The two rules the pāda opens with are not about Sanskrit but about the rules,
and they are the most consequential things codified so far: 1.4.1 governs 1,163
sūtras and 1.4.2 is quoted more than any other. Both are easy to get subtly
wrong in the same direction — by reading them as 'the later one wins' and
stopping there — so most of what follows tests the qualifications rather than
the headline.

For 1.4.2 the qualification is उत्सर्गापवादनित्यानित्यान्तरङ्गबहिरङ्गेषु
तुल्यबलता नास्ति: three whole families of conflict where the sūtra does not
apply and the earlier rule may perfectly well win. A codification that compared
sūtra numbers and nothing else would pass every test built from the headline
and fail every real case in those families.

For 1.4.1 the qualification is अनवकाशा: not simply the later name, but the one
with nowhere else to go.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.nominal import (
    BHA,
    GURU,
    LAGHU,
    PADA,
    anga,
    ghi,
    nadi,
    pada_or_bha,
    vacana,
    weight,
)
from src.astadhyayi.sources import all_sutra_ids, facts
from src.astadhyayi.sutra import REGISTRY
from src.astadhyayi.vipratisedha import (
    Rule,
    Strength,
    eka_samjna,
    governs,
    vipratisedha,
)


class Vipratisedha(unittest.TestCase):
    """1.4.2 विप्रतिषेधे परं कार्यम्, and the three families it excludes."""

    def test_of_two_equal_rules_the_later_is_done(self):
        """
        The Kāśikā's own example. 7.3.101 has a scope of its own (वृक्षाभ्याम्)
        and so does 7.3.103 (वृक्षेषु); both reach वृक्षेभ्यः, and there the
        later is done.
        """
        settled = vipratisedha([Rule("7.3.101"), Rule("7.3.103")])
        self.assertEqual(settled.winner.sutra, "7.3.103")
        self.assertEqual(settled.by, "1.4.2")

    def test_order_of_presentation_does_not_matter(self):
        for pair in ([Rule("7.3.101"), Rule("7.3.103")],
                     [Rule("7.3.103"), Rule("7.3.101")]):
            self.assertEqual(vipratisedha(pair).winner.sutra, "7.3.103")

    def test_an_earlier_apavada_beats_a_later_general_rule(self):
        """
        This is the case the headline reading gets backwards, and it is not a
        rare one: उत्सर्गापवादयोः is the first of the three families the
        Kāśikā excludes. An exception standing earlier still wins.
        """
        settled = vipratisedha([
            Rule("6.1.10", standing=Strength.APAVADA),
            Rule("7.1.20"),
        ])
        self.assertEqual(settled.winner.sutra, "6.1.10")
        self.assertNotEqual(settled.by, "1.4.2")
        self.assertIn("excluded", settled.by)

    def test_the_same_for_nitya_and_antaranga(self):
        for standing in (Strength.NITYA, Strength.ANTARANGA):
            with self.subTest(standing=standing.value):
                settled = vipratisedha([
                    Rule("3.1.1", standing=standing), Rule("8.4.1"),
                ])
                self.assertEqual(settled.winner.sutra, "3.1.1")
                self.assertIn("excluded", settled.by)

    def test_the_exclusion_is_quoted_in_the_reason(self):
        """
        A reader who is told only 'the earlier one won' has been given the
        outcome and not the principle, and this sūtra is quoted often enough
        that the principle is the point.
        """
        settled = vipratisedha([
            Rule("6.1.10", standing=Strength.APAVADA), Rule("7.1.20"),
        ])
        self.assertIn("तुल्यबलता", settled.why)
        self.assertIn("बलवतैव", settled.why)

    def test_it_names_what_lost(self):
        settled = vipratisedha([Rule("7.3.101"), Rule("7.3.103")])
        self.assertEqual(settled.against, ("7.3.101",))

    def test_one_rule_alone_is_no_conflict(self):
        settled = vipratisedha([Rule("7.3.101")])
        self.assertEqual(settled.winner.sutra, "7.3.101")
        self.assertEqual(settled.by, "—")
        self.assertEqual(vipratisedha([]).winner, None)


class EkaSamjna(unittest.TestCase):
    """1.4.1 आ कडारादेका संज्ञा."""

    def test_of_two_names_the_later_stands(self):
        settled = eka_samjna([Rule("1.4.10", what=LAGHU),
                              Rule("1.4.11", what=GURU)])
        self.assertEqual(settled.winner.what, GURU)
        self.assertEqual(settled.by, "1.4.1")

    def test_but_a_rule_with_nowhere_else_to_go_stands_first(self):
        """
        या परा, अनवकाशा च — two readings, not one. An अनवकाश rule that lost
        to a later one would have no field at all, so it is tried first even
        against a later competitor.
        """
        settled = eka_samjna([
            Rule("1.4.18", what=BHA, anavakasa=True),
            Rule("1.4.19", what="other"),
        ])
        self.assertEqual(settled.winner.what, BHA)
        self.assertIn("अनवकाशा", settled.why)

    def test_its_scope_runs_from_itself_to_2_2_38(self):
        self.assertTrue(governs("1.4.1"))
        self.assertTrue(governs("1.4.10"))
        self.assertTrue(governs("2.2.38"))
        self.assertFalse(governs("2.2.39"))
        self.assertFalse(governs("1.3.93"))

    def test_the_corpus_agrees_that_it_governs_this_pada(self):
        """
        Two texts on the same claim. The scope is computed from the two
        endpoints the sūtra names; the corpus records, per sūtra, which
        adhikāra it falls under. They must not disagree.
        """
        for number in range(1, 23):
            sutra_id = f"1.4.{number}"
            headings = [item.sutra for item in facts(sutra_id).adhikara]
            self.assertIn("1.4.1", headings, sutra_id)
            self.assertTrue(governs(sutra_id), sutra_id)

    def test_and_that_it_stops_where_it_says(self):
        beyond = [s for s in all_sutra_ids()
                  if not governs(s)
                  and "1.4.1" in [i.sutra for i in facts(s).adhikara]]
        self.assertEqual(beyond, [])


class Nadi(unittest.TestCase):
    """1.4.3 to 1.4.6."""

    def test_a_long_i_or_u_final_meaning_a_woman(self):
        for word in ("kumārī", "gaurī", "lakṣmī", "brahmabandhū", "yavāgū"):
            self.assertEqual(nadi(word).name, "nadī", word)

    def test_yu_iti_kim(self):
        """मात्रे, दुहित्रे — neither ends in ī or ū."""
        for word in ("mātṛ", "duhitṛ"):
            self.assertIsNone(nadi(word).name, word)

    def test_stryakhya_iti_kim(self):
        """ग्रामणीः, सेनानीः, खलपूः — the right finals, the wrong meaning."""
        for word in ("grāmaṇī", "senānī", "khalapū"):
            self.assertIsNone(nadi(word, stri_akhya=False).name, word)

    def test_the_prohibition_and_its_exception(self):
        for word in ("śrī", "bhrū"):
            outcome = nadi(word, iyan_uvan_place=True)
            self.assertIsNone(outcome.name, word)
            self.assertEqual(outcome.by, "1.4.4")
        self.assertEqual(
            nadi("strī", iyan_uvan_place=True, is_stri=True).name, "nadī")

    def test_before_am_the_prohibition_lifts_optionally(self):
        outcome = nadi("śrī", iyan_uvan_place=True, before_am=True)
        self.assertEqual(outcome.name, "nadī")
        self.assertEqual(outcome.by, "1.4.5")
        self.assertTrue(outcome.optional)

    def test_a_short_vowel_reaches_it_only_before_a_ngit(self):
        self.assertIsNone(nadi("mati").name)
        outcome = nadi("mati", before_ngit=True)
        self.assertEqual(outcome.by, "1.4.6")
        self.assertTrue(outcome.optional)


class Ghi(unittest.TestCase):
    """1.4.7 to 1.4.9, and where शेष meets 1.4.1."""

    def test_the_remainder(self):
        for word in ("agni", "vāyu", "kṛti", "dhenu"):
            self.assertEqual(ghi(word).name, "ghi", word)

    def test_sakhi_is_excepted_by_name(self):
        self.assertIsNone(ghi("sakhi").name)

    def test_pati_only_in_a_compound(self):
        self.assertIsNone(ghi("pati").name)
        self.assertEqual(ghi("pati", in_compound=True).by, "1.4.8")
        self.assertTrue(ghi("pati", chandas_with_genitive=True).optional)

    def test_a_word_that_reached_nadi_is_out_of_the_remainder(self):
        """
        स्त्र्याख्यं च यन् न नदीसंज्ञकं स शेषः — the Kāśikā's second clause,
        and it is 1.4.1 doing the work. मति is घि ordinarily and नदी before a
        ṅit affix, and one name only may stand.
        """
        self.assertEqual(ghi("mati", stri_akhya=True).name, "ghi")
        excluded = ghi("mati", stri_akhya=True, before_ngit=True)
        self.assertIsNone(excluded.name)
        self.assertEqual(excluded.instead_of, ("1.4.6",))

    def test_and_a_word_that_did_not_stays_in(self):
        """अग्नि is not स्त्र्याख्य, so 1.4.6 never reaches it either way."""
        self.assertEqual(ghi("agni", before_ngit=True).name, "ghi")


class Weight(unittest.TestCase):
    """1.4.10 to 1.4.12 — and the Kāśikā's own worked example of 1.4.1."""

    def test_a_short_vowel_is_light(self):
        for vowel in ("a", "i", "u", "ṛ"):
            self.assertEqual(weight(vowel).name, LAGHU, vowel)

    def test_a_long_one_is_heavy_with_no_condition(self):
        for vowel in ("ā", "ī", "e", "ai", "au"):
            outcome = weight(vowel)
            self.assertEqual(outcome.name, GURU, vowel)
            self.assertEqual(outcome.by, "1.4.12")

    def test_a_short_one_before_a_conjunct_is_heavy_and_not_also_light(self):
        """
        संयोगपरस्य ह्रस्वस्य लघुसंज्ञा प्राप्नोति गुरुसंज्ञा च। एका संज्ञेति
        वचनाद् गुरुसंज्ञैव भवति — शिक्षा and भिक्षा.
        """
        outcome = weight("i", before_conjunct=True)
        self.assertEqual(outcome.name, GURU)
        self.assertEqual(outcome.by, "1.4.11")
        self.assertEqual(outcome.instead_of, ("1.4.10",))

    def test_the_resolution_is_1_4_1s_and_says_so(self):
        """
        Not written into the rule but performed by `eka_samjna`, so that the
        record shows what displaced what. A hard-coded answer would give the
        same form and lose the reason.
        """
        self.assertIn("एका संज्ञा", weight("i", before_conjunct=True).why)
        self.assertIn("सन्वद्भाव", weight("i", before_conjunct=True).why)


class PadaAndBha(unittest.TestCase):
    """1.4.14 to 1.4.20."""

    def test_what_ends_in_a_nominal_or_verbal_ending(self):
        self.assertEqual(
            pada_or_bha("brāhmaṇāḥ", ends_in_sup_or_tin=True).name, PADA)

    def test_before_an_ordinary_sup_affix(self):
        outcome = pada_or_bha("rājan", sup_affix="bhyām")
        self.assertEqual(outcome.name, PADA)
        self.assertEqual(outcome.by, "1.4.17")

    def test_but_not_before_a_sarvanamasthana(self):
        """असर्वनामस्थान इति किम्? राजानौ, राजानः."""
        self.assertIsNone(
            pada_or_bha("rājan", sup_affix="au", sarvanamasthana=True).name)

    def test_a_ya_or_vowel_initial_one_gives_bha_instead(self):
        for affix in ("ya", "i"):
            outcome = pada_or_bha("gārga", sup_affix=affix)
            self.assertEqual(outcome.name, BHA, affix)
            self.assertEqual(outcome.by, "1.4.18", affix)
            self.assertEqual(outcome.instead_of, ("1.4.17",), affix)

    def test_that_conflict_is_an_apavada_and_not_a_vipratisedha(self):
        """
        पूर्वेण पदसंज्ञायां प्राप्तायां तदपवादो भसंज्ञा विधीयते. Both are
        saṃjñās under 1.4.1, so the resolution is एका संज्ञा — and the record
        names 1.4.18, not 1.4.2.
        """
        outcome = pada_or_bha("gārga", sup_affix="ya")
        self.assertNotIn("1.4.2", outcome.by)
        self.assertIn("तदपवादो", outcome.why)

    def test_a_t_or_s_final_before_a_matvartha(self):
        self.assertEqual(pada_or_bha("yaśas", matvartha=True).name, BHA)
        self.assertEqual(pada_or_bha("vidyut", matvartha=True).name, BHA)

    def test_tasav_iti_kim(self):
        """तक्षवान् ग्रामः — the final is neither त् nor स्."""
        self.assertIsNone(pada_or_bha("takṣan", matvartha=True).name)


class Anga(unittest.TestCase):
    """1.4.13, which 613 later sūtras wait on."""

    def test_what_a_suffix_is_prescribed_after(self):
        outcome = anga("kṛ", "tṛc", prescribed_from="kṛ")
        self.assertEqual(outcome.name, "kṛ")
        self.assertEqual(outcome.by, "1.4.13")

    def test_a_suffix_merely_following_is_not_enough(self):
        """विधिग्रहणं किम्? स्त्री इयती."""
        self.assertIsNone(anga("strī", "iyatī").name)

    def test_nor_a_suffix_that_has_gone(self):
        """लुप्तप्रत्यये मा भूत् — श्र्यर्थम्, भ्र्वर्थम्."""
        self.assertIsNone(anga("śrī", "", prescribed_from="śrī").name)

    def test_the_scope_it_feeds_is_real(self):
        """
        6.4.1 अङ्गस्य governs to 7.4.97, and that is why this saṃjñā matters
        rather than being one name among eight. The corpus records the range.
        """
        from src.astadhyayi.reading import governs as scope_of

        governed = scope_of("6.4.1")
        self.assertEqual(governed[0], "6.4.1")
        self.assertEqual(governed[-1], "7.4.97")
        self.assertGreater(len(governed), 600)


class Vacana(unittest.TestCase):
    """1.4.21 and 1.4.22."""

    def test_the_three_numbers(self):
        self.assertEqual(vacana(1).name, "ekavacana")
        self.assertEqual(vacana(2).name, "dvivacana")
        self.assertEqual(vacana(3).name, "bahuvacana")
        self.assertEqual(vacana(17).name, "bahuvacana")

    def test_the_two_sutras_split_them_as_panini_does(self):
        """
        Not one rule but two, and the plural comes first. 1.4.21 takes the
        many and 1.4.22 the two and the one — paired respectively, which is
        1.3.10 again.
        """
        self.assertEqual(vacana(3).by, "1.4.21")
        self.assertEqual(vacana(2).by, "1.4.22")
        self.assertEqual(vacana(1).by, "1.4.22")

    def test_the_record_says_the_number_is_the_karakas(self):
        """
        कर्मादयोऽप्यपरे विभक्तीनाम् अर्था वाच्याः, तदीये बहुत्वे बहुवचनम् —
        which is what makes these two the bridge into the kāraka section that
        begins at 1.4.23.
        """
        notes = REGISTRY.get("1.4.21").notes
        self.assertIn("कर्मादयो", notes)
        self.assertIn("1.4.23", notes)


class Registration(unittest.TestCase):
    def test_1_4_1_to_1_4_22_are_codified(self):
        missing = [f"1.4.{n}" for n in range(1, 23) if not REGISTRY.has(f"1.4.{n}")]
        self.assertEqual(missing, [])

    def test_the_contradiction_at_1_4_20_is_recorded_as_open(self):
        """
        उभयसंज्ञान्यपि gives the अयस्मय group both names, and 1.4.20 stands
        inside 1.4.1's scope, where one name only is allowed. Recorded rather
        than resolved.
        """
        notes = REGISTRY.get("1.4.20").notes
        self.assertIn("OPEN", notes)
        self.assertIn("उभयसंज्ञान्यपीति", notes)
        self.assertIn("1.4.1", notes)

    def test_1_4_2s_record_states_the_qualification(self):
        notes = REGISTRY.get("1.4.2").notes
        self.assertIn("तुल्यबलविरोध", notes)
        self.assertIn("उत्सर्गापवाद", notes)
        self.assertIn("SCOPE", notes)


if __name__ == "__main__":
    unittest.main()
