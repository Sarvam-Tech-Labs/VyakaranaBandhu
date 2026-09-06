# -*- coding: utf-8 -*-
"""
2.4.1 to 2.4.31 — the number and gender of a compound.

The expectations are the Kāśikā's own worked forms and its own
*kim* counter-examples, which is where the conditions live. Where a
structural claim is made in the notes — a precedence, a back-reference,
a corpus defect — there is a test that would go red if it stopped being
true.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.samasa import Samasa
from src.astadhyayi.samasalinga import (
    ANGA_KINDS, ARDHARCADI, Compound, GAVASVADI, MASCULINE, NEUTER,
    ekavat, gender,
)


def one(**kwargs):
    return Compound(**kwargs)


class EkavadbhavaAnswersFromTheRightRule(unittest.TestCase):
    """Each rule's own example, routed to that rule and no other."""

    CASES = (
        ("2.4.1", dict(samasa=Samasa.DVIGU, given=("samāhāra",))),
        ("2.4.2", dict(anga_of="prāṇin")),
        ("2.4.2", dict(anga_of="tūrya")),
        ("2.4.2", dict(anga_of="senā")),
        ("2.4.3", dict(people="caraṇa",
                       given=("anuvāda", "aorist-sthā-iṇ"))),
        ("2.4.4", dict(names="kratu", given=("anapuṃsaka",))),
        ("2.4.5", dict(given=("adhyayana-āsanna",))),
        ("2.4.6", dict(jati_of="dravya")),
        ("2.4.7", dict(names="nadī", given=("viśiṣṭaliṅga",))),
        ("2.4.7", dict(names="deśa", given=("viśiṣṭaliṅga",))),
        ("2.4.8", dict(given=("kṣudra-jantu",))),
        ("2.4.9", dict(given=("śāśvatika-virodha",))),
        ("2.4.10", dict(people="śūdra")),
        ("2.4.11", dict(form=GAVASVADI[0])),
        ("2.4.12", dict(group="vṛkṣa")),
        ("2.4.13", dict(given=("vipratiṣiddha",))),
        ("2.4.16", dict(given=("etāvattva", "samīpa"))),
    )

    def test_each_example_fires_its_own_rule(self):
        for sutra, conditions in self.CASES:
            with self.subTest(sutra=sutra, conditions=conditions):
                answer = ekavat(one(**conditions))
                self.assertEqual(answer.by, sutra)
                self.assertTrue(answer.singular)

    def test_the_two_options_are_marked_optional_and_the_rest_are_not(self):
        """
        2.4.12 and 2.4.13 say विभाषा; the obligatory rules do not. A rule
        that lost its option would silently make a choice on Pāṇini's
        behalf, which is the thing this project must never do.
        """
        for sutra, conditions in self.CASES:
            with self.subTest(sutra=sutra):
                answer = ekavat(one(**conditions))
                self.assertEqual(answer.optional,
                                 sutra in ("2.4.12", "2.4.13", "2.4.16"))


class TheProhibitionsAndTheRefusals(unittest.TestCase):
    """
    A प्रतिषेध refusing is that rule ACTING and reports itself. A rule
    that simply does not reach its input reports nothing — conflating
    the two turns a counter-example into a worked one.
    """

    def test_the_two_prohibitions_report_themselves(self):
        kept_out = ekavat(one(form="vāṅmanase"))
        self.assertEqual(kept_out.by, "2.4.14")
        self.assertFalse(kept_out.singular)

        counted = ekavat(one(given=("etāvattva",)))
        self.assertEqual(counted.by, "2.4.15")
        self.assertFalse(counted.singular)

    def test_a_rule_that_does_not_reach_its_input_claims_nothing(self):
        for conditions in (
            dict(samasa=Samasa.DVIGU),                  # not a समाहार
            dict(people="caraṇa"),                      # no अनुवाद
            dict(people="caraṇa", given=("anuvāda",)),  # wrong root/tense
            dict(names="kratu"),                        # neuter rite-names
            dict(jati_of="guṇa"),                       # not a द्रव्यजाति
            dict(jati_of="dravya", given=("prāṇin",)),  # living things
            dict(names="nadī"),                         # one gender
            dict(names="deśa",
                 given=("viśiṣṭaliṅga", "grāma")),      # a village
            dict(people="śūdra", given=("niravasita",)),
            dict(given=("vipratiṣiddha", "adhikaraṇa-vācin")),
            dict(group="phala", member_count=2),        # the vārttika
            dict(),                                     # nothing at all
        ):
            with self.subTest(conditions=conditions):
                answer = ekavat(one(**conditions))
                self.assertEqual(answer.by, "")
                self.assertFalse(answer.singular)

    def test_the_prohibition_wins_over_a_rule_that_would_have_applied(self):
        """
        यथायथमेकवद्भावे प्राप्ते प्रतिषेध आरभ्यते — 2.4.14 is written
        because its members were otherwise caught. वाङ्मनसे would be
        reached by 2.4.6 as a class of non-living things; the
        prohibition has to beat it, not merely coexist with it.
        """
        without = ekavat(one(jati_of="dravya"))
        self.assertEqual(without.by, "2.4.6")
        with_form = ekavat(one(jati_of="dravya", form="vāṅmanase"))
        self.assertEqual(with_form.by, "2.4.14")

    def test_the_option_near_a_count_beats_the_prohibition_of_the_count(self):
        """
        2.4.16 विभाषा समीपे answers 2.4.15's refusal, so it has to be
        read first. Read in numerical order the prohibition would
        swallow it and उपदशं दन्तोष्ठम् would be unreachable.
        """
        self.assertEqual(ekavat(one(given=("etāvattva",))).by, "2.4.15")
        near = ekavat(one(given=("etāvattva", "samīpa")))
        self.assertEqual(near.by, "2.4.16")
        self.assertTrue(near.singular)
        self.assertTrue(near.optional)


class ThePrecedenceChainTheCommentaryStates(unittest.TestCase):
    """
    Three rules and two reversals, each step in the vṛtti's own words.

    2.4.2 makes a द्वन्द्व of animal-limbs count as one always. 2.4.12
    then offers पशु and शकुनि a choice — हस्त्यश्वादिषु परत्वात्
    पशुद्वन्द्वे विभाषयैकवद् भवति, the later rule winning by 1.4.2. Then
    2.4.9's च shuts it again for the animals that are natural enemies:
    तेन पशुशकुनिद्वन्द्वे विरोधिनामनेन नित्यम् एकवद्भावो भवति.
    """

    def test_the_later_option_reopens_what_the_earlier_rule_shut(self):
        by_limb = ekavat(one(anga_of="prāṇin"))
        self.assertEqual(by_limb.by, "2.4.2")
        self.assertFalse(by_limb.optional)

        cattle = ekavat(one(group="paśu"))
        self.assertEqual(cattle.by, "2.4.12")
        self.assertTrue(cattle.optional)

    def test_but_enmity_shuts_it_again(self):
        """अश्वमहिषम्, काकोलूकम् — obligatory, not a choice."""
        for kind in ("paśu", "śakuni"):
            with self.subTest(group=kind):
                enemies = ekavat(
                    one(group=kind, given=("śāśvatika-virodha",)))
                self.assertEqual(enemies.by, "2.4.9")
                self.assertTrue(enemies.singular)
                self.assertFalse(
                    enemies.optional,
                    "2.4.9's च makes it नित्यम्; an option here would "
                    "mean the च had been dropped")

    def test_the_varttika_restricts_whichever_rule_would_have_applied(self):
        """
        बहुप्रकृतिः … न द्विप्रकृतिः, and its eight are NOT a subset of
        2.4.12's ten: फल, सेना, वनस्पति and क्षुद्रजन्तु are named in no
        sūtra of this run. Its own examples say which rules it reaches —
        बदरामलके is 2.4.6's fruit-class and यूकालिक्षे is 2.4.8's small
        creatures. Written as a condition inside 2.4.12's row it covered
        four of the eight and silently missed the other four.
        """
        pairs = (
            ("2.4.6", dict(group="phala", jati_of="dravya")),
            ("2.4.8", dict(group="kṣudrajantu",
                           given=("kṣudra-jantu",))),
        )
        for sutra, conditions in pairs:
            with self.subTest(sutra=sutra):
                self.assertEqual(
                    ekavat(one(member_count=2, **conditions)).by, "",
                    "two of them stay dual, whatever rule would have "
                    "made them one")
                self.assertEqual(
                    ekavat(one(member_count=3, **conditions)).by, sutra)

    def test_a_kind_outside_the_varttika_is_made_one_at_two(self):
        """वृक्ष is in 2.4.12's ten and not among the vārttika's eight."""
        self.assertEqual(
            ekavat(one(group="vṛkṣa", member_count=2)).by, "2.4.12")


class TheClosedListsRefuseAFifthName(unittest.TestCase):
    """
    2.4.2's three अङ्ग are a परिसंख्या — अङ्गशब्दस्य प्रत्येकं
    वाक्यपरिसमाप्त्या त्रीणि वाक्यानि संपद्यन्ते, and न हि चतुर्थं
    वाक्यमस्ति. A fourth kind is refused, not quietly accepted.
    """

    def test_a_kind_of_anga_the_sutra_does_not_name_is_refused(self):
        with self.assertRaises(ValueError):
            ekavat(one(anga_of="ratha"))

    def test_all_three_it_does_name_are_accepted(self):
        for kind in ANGA_KINDS:
            with self.subTest(anga_of=kind):
                self.assertEqual(ekavat(one(anga_of=kind)).by, "2.4.2")

    def test_a_fact_the_pada_does_not_know_is_refused(self):
        with self.assertRaises(ValueError):
            one(given=("not-a-fact",)).has("not-a-fact")


class GenderAsksTheNumberRatherThanRestatingIt(unittest.TestCase):
    """
    स नपुंसकम् has no content of its own: स points back at 2.4.1 to
    2.4.16. So 2.4.17 must ASK that table, and a change in what the
    table answers has to change what 2.4.17 answers.
    """

    def test_the_neuter_follows_whatever_made_it_count_as_one(self):
        for conditions in (
            dict(samasa=Samasa.DVIGU, given=("samāhāra",)),
            dict(anga_of="prāṇin"),
            dict(given=("kṣudra-jantu",)),
            dict(given=("śāśvatika-virodha",)),
        ):
            with self.subTest(conditions=conditions):
                self.assertTrue(ekavat(one(**conditions)).singular)
                self.assertEqual(gender(one(**conditions)).by, "2.4.17")
                self.assertEqual(gender(one(**conditions)).name, NEUTER)

    def test_and_when_the_number_rule_stops_applying_so_does_the_neuter(self):
        """
        The same compound less its one qualifying fact: 2.4.1 no longer
        reaches it, so neither does 2.4.17, and 2.4.26 answers instead.
        A 2.4.17 that had restated the table rather than asking it would
        keep saying neuter here.
        """
        without = one(samasa=Samasa.DVIGU)
        self.assertEqual(ekavat(without).by, "")
        self.assertNotEqual(gender(without).by, "2.4.17")

    def test_a_prohibited_compound_is_not_made_neuter(self):
        """
        2.4.14 keeps वाङ्मनसे from counting as one, so 2.4.17 cannot
        reach it either — the refusal has to carry through.
        """
        kept_out = one(samasa=Samasa.DVANDVA, form="vāṅmanase")
        self.assertEqual(ekavat(kept_out).by, "2.4.14")
        self.assertNotEqual(gender(kept_out).by, "2.4.17")


class TheGenderRulesAnswerFromTheRightRule(unittest.TestCase):

    def test_each_example_fires_its_own_rule(self):
        cases = (
            ("2.4.17", dict(samasa=Samasa.DVIGU, given=("samāhāra",))),
            ("2.4.18", dict(samasa=Samasa.AVYAYIBHAVA)),
            ("2.4.20", dict(samasa=Samasa.TATPURUSA, ends_in="kanthā",
                            given=("saṃjñā", "uśīnara"))),
            ("2.4.21", dict(samasa=Samasa.TATPURUSA, ends_in="upajñā",
                            given=("ācikhyāsā",))),
            ("2.4.21", dict(samasa=Samasa.TATPURUSA, ends_in="upakrama",
                            given=("ācikhyāsā",))),
            ("2.4.22", dict(samasa=Samasa.TATPURUSA, ends_in="chāyā",
                            given=("bāhulya",))),
            ("2.4.23", dict(samasa=Samasa.TATPURUSA, ends_in="sabhā",
                            given=("rājan-pūrva",))),
            ("2.4.23", dict(samasa=Samasa.TATPURUSA, ends_in="sabhā",
                            given=("amanuṣya-pūrva",))),
            ("2.4.24", dict(samasa=Samasa.TATPURUSA, ends_in="sabhā",
                            given=("aśālā",))),
            ("2.4.25", dict(samasa=Samasa.TATPURUSA, ends_in="śālā")),
            ("2.4.29", dict(ends_in="rātra")),
            ("2.4.30", dict(form="apatha")),
            ("2.4.31", dict(form=ARDHARCADI[0])),
        )
        for sutra, conditions in cases:
            with self.subTest(sutra=sutra, conditions=conditions):
                self.assertEqual(gender(one(**conditions)).by, sutra)

    def test_only_2_4_25_is_a_choice(self):
        """
        विभाषा is written once in the gender run. 2.4.22 exists to make
        छाया obligatory where abundance is meant — नित्यार्थमिदं वचनम् —
        so an option there would make that rule pointless.
        """
        chosen = gender(one(samasa=Samasa.TATPURUSA, ends_in="śālā"))
        self.assertTrue(chosen.optional)
        fixed = gender(one(samasa=Samasa.TATPURUSA, ends_in="chāyā",
                           given=("bāhulya",)))
        self.assertEqual(fixed.by, "2.4.22")
        self.assertFalse(fixed.optional)

    def test_2_4_31_gives_both_genders(self):
        """अर्धर्चः and अर्धर्चम् both stand, so one answer is not enough."""
        both = gender(one(form=ARDHARCADI[0]))
        self.assertEqual(both.name, MASCULINE)
        self.assertIn(NEUTER, both.also)

    def test_the_heading_puts_two_tatpurusas_outside_its_run(self):
        """
        2.4.19 अनञ् कर्मधारयः. Both excluded compounds end in सेना, which
        2.4.25 would otherwise have reached, so the exclusion is what is
        being tested and not the absence of a matching rule.
        """
        reached = gender(one(samasa=Samasa.TATPURUSA, ends_in="senā"))
        self.assertEqual(reached.by, "2.4.25")
        for fact in ("nañ", "samānādhikaraṇa"):
            with self.subTest(excluded_by=fact):
                out = gender(one(samasa=Samasa.TATPURUSA, ends_in="senā",
                                 given=(fact,)))
                self.assertEqual(out.by, "")
                self.assertEqual(out.name, "")


class TheRulesThatNameAMemberRatherThanAGender(unittest.TestCase):
    """
    2.4.26, 2.4.27 and 2.4.28 name no gender at all — they say whose
    gender to use. Returning a gender-name would be inventing an answer
    the sūtra does not give.
    """

    def test_2_4_26_gives_the_last_member(self):
        for name in (Samasa.DVANDVA, Samasa.TATPURUSA):
            with self.subTest(samasa=name):
                answer = gender(one(samasa=name))
                self.assertEqual(answer.by, "2.4.26")
                self.assertEqual(answer.slot, "last")
                self.assertFalse(hasattr(answer, "name"))

    def test_2_4_27_and_2_4_28_give_the_first(self):
        self.assertEqual(gender(one(form="aśvavaḍavau")).slot, "first")
        for word in ("hemantaśiśirau", "ahorātre"):
            with self.subTest(form=word):
                answer = gender(one(form=word, given=("chandas",)))
                self.assertEqual(answer.by, "2.4.28")
                self.assertEqual(answer.slot, "first")

    def test_2_4_28_only_holds_in_the_veda(self):
        """छन्दसि is a condition, not decoration."""
        self.assertNotEqual(gender(one(form="hemantaśiśirau")).by, "2.4.28")

    def test_2_4_28_beats_the_masculine_2_4_29_would_have_given(self):
        """
        The Nyāsa: रात्राह्नाहाः पुंसि इति पुंल्लिङ्गत्वे प्राप्ते छन्दसि
        लिङ्गव्यत्यय उक्तः. अहोरात्रे ends in the अह of 2.4.29, so the
        two rules genuinely compete and the order between them is the
        thing being tested.
        """
        outside = gender(one(form="ahorātre", ends_in="aha"))
        self.assertEqual(outside.by, "2.4.29")
        self.assertEqual(outside.name, MASCULINE)
        inside = gender(one(form="ahorātre", ends_in="aha",
                            given=("chandas",)))
        self.assertEqual(inside.by, "2.4.28")

    def test_the_varttika_keeps_2_4_26_off_five_kinds(self):
        """द्विगुप्राप्तापन्नालंपूर्वगतिसमासेषु प्रतिषेधो वक्तव्यः."""
        for kind in ("dvigu", "prāpta", "āpanna", "alam", "gati"):
            with self.subTest(kind=kind):
                out = gender(one(samasa=Samasa.TATPURUSA, kind=kind))
                self.assertEqual(out.by, "")
        # A kind the vārttika does not name is still reached.
        self.assertEqual(
            gender(one(samasa=Samasa.TATPURUSA, kind="ṣaṣṭhī")).by, "2.4.26")


class TheGanasAreReadFromDiskAndNotCopied(unittest.TestCase):
    """
    The property, not the census: a count would go stale the day the
    gaṇapāṭha is corrected, and three of those have had to be replaced
    already.
    """

    def test_both_ganas_have_members_and_their_own_examples_are_in_them(self):
        self.assertTrue(GAVASVADI)
        self.assertIn("gavāśvam", GAVASVADI)
        self.assertTrue(ARDHARCADI)
        self.assertIn("ardharca", ARDHARCADI)

    def test_a_form_outside_the_gana_falls_through(self):
        """
        रूपान्तरे तु नायं विधिर्भवति — गोऽश्वम् is a different shape and
        2.4.11 does not reach it.
        """
        self.assertNotIn("go'śvam", GAVASVADI)
        self.assertEqual(ekavat(one(form="go'śvam")).by, "")


class TwoClaimsInTheNotesThatWouldOtherwiseGoUnchecked(unittest.TestCase):

    def test_the_kasika_on_disk_for_2_4_28_is_the_wrong_sutras_text(self):
        """
        The notes on 2.4.28 record that `reference/` holds, under that
        sūtra, a vṛtti on a छ-affix rule with nothing to do with
        हेमन्तशिशिरौ — which is why the rule is codified from the four
        other witnesses instead. If the corpus is ever corrected this
        goes red, which is exactly when the note should be revisited.
        """
        from src.astadhyayi.corpus import all_commentary_on

        commentaries = all_commentary_on("2.4.28")
        kasika = next((t for name, t in commentaries.items()
                       if "Kāśikā" in name), "")
        self.assertTrue(kasika, "no Kāśikā on disk for 2.4.28 at all")
        self.assertNotIn("हेमन्त", kasika)
        self.assertIn("अपोनप्तृ", kasika)

        # The witnesses it IS codified from do carry the real content.
        others = " ".join(t for name, t in commentaries.items()
                          if "Kāśikā" not in name)
        self.assertIn("हेमन्त", others)

    def test_2_4_1_s_ekavacana_is_not_the_ekavacana_of_1_4_102(self):
        """
        The Nyāsa's argument, and the reason 1.4.102 is named in the
        code without being called. 1.4.102 assigns the first triplet of
        a set of ENDINGS; 2.4.1 confers oneness of MEANING, and answers
        for a compound before any ending exists. The two cannot be the
        same notion, so neither implementation can stand in for the
        other rule.
        """
        answered = ekavat(one(samasa=Samasa.DVIGU, given=("samāhāra",)))
        self.assertTrue(answered.singular)
        # Nothing about a vibhakti or a triplet is decided here: the
        # answer carries no ending, and the compound carried none in.
        self.assertFalse(hasattr(answered, "vibhakti"))
        self.assertFalse(hasattr(Compound(), "vibhakti"))


if __name__ == "__main__":
    unittest.main()
