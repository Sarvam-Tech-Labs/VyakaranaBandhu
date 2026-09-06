# -*- coding: utf-8 -*-
"""
Tests for 1.2.33 to 1.2.40 — how the three accents are actually recited.

These eight are unlike anything codified before them in one respect: they work
over a *sequence*. 1.2.39 asks what came earlier in the phrase and 1.2.40 what
comes next, and neither question can be put to a vowel on its own. So the tests
are over phrases, and the interesting failures are the ones where a rule reads
the wrong direction or reaches past its own window.

The Kāśikā gives a counter-example for nearly every condition, and those pairs
are what the table below holds. Where it gives none — 1.2.38, which concerns
one line of one text — the test says so rather than inventing one.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.svara import (
    Accent,
    Recitation,
    Register,
    ekasruti,
    recite,
)
from src.astadhyayi.sources import facts
from src.astadhyayi.sutra import REGISTRY

U, N, S = Accent.UDATTA, Accent.ANUDATTA, Accent.SVARITA
E, SN = Register.EKASRUTI, Register.SANNATARA


def registers(accents, **where):
    return tuple(r.register for r in recite(accents, Recitation(**where)))


def sutras(accents, **where):
    return tuple(r.by for r in recite(accents, Recitation(**where)))


class Ekasruti(unittest.TestCase):
    """1.2.33 and 1.2.34 — the settings where the three collapse into one."""

    def test_calling_from_a_distance_flattens_the_whole_sentence(self):
        """
        आगच्छ भो माणवक देवदत्त३. एकश्रुति वाक्यं भवति — the rule is over the
        sentence, so every syllable goes, not only the accented ones.
        """
        self.assertEqual(
            registers([U, N, S, N], setting="dūrāt-sambuddhi"),
            (E, E, E, E),
        )

    def test_near_at_hand_the_three_stand(self):
        """
        दूरादिति किम्? The same words spoken close by keep their accents, and
        that is the only thing the sūtra's first word does.
        """
        self.assertNotIn(E, registers([U, N, S, N]))

    def test_the_rite_flattens_too(self):
        self.assertTrue(ekasruti([U, N, S], Recitation(setting="yajña")))

    def test_but_not_a_japa_a_nyunkha_or_a_saman(self):
        """
        Three exceptions, and each is there for a reason the Kāśikā gives.
        The नयूङ्खs in particular are sixteen ओकारs of which केचिदुदात्ताः
        केचिदनुदात्ताः — flattening them would erase what they are.
        """
        for exception in ("japa", "nyunkha", "saman"):
            with self.subTest(exception=exception):
                where = Recitation(setting="yajña", **{exception: True})
                self.assertFalse(ekasruti([U, N, S], where))
                self.assertNotIn(E, registers([U, N, S], setting="yajña",
                                              **{exception: True}))

    def test_the_vasatkara_is_raised_instead(self):
        """
        उच्चैस्तरां वा वषट्कारः — higher than an udātta, and the option is
        against 1.2.34's one tone rather than against the ordinary accents,
        since inside the rite that is what it would otherwise have had.
        """
        said = recite([U], Recitation(setting="yajña", vasatkara=True))
        self.assertEqual(said[0].register, Register.UCCAISTARAM)
        self.assertEqual(said[0].by, "1.2.35")
        self.assertTrue(said[0].optional)

    def test_the_veda_is_optional(self):
        """पक्षान्तरे त्रैस्वर्यमेव भवति — on the other reading all three stand."""
        said = recite([U, N], Recitation(setting="chandas"))
        self.assertEqual(tuple(r.register for r in said), (E, E))
        self.assertTrue(all(r.optional for r in said))

    def test_and_the_rite_is_not(self):
        """The contrast is the point: 1.2.34 is invariable, 1.2.36 is not."""
        said = recite([U, N], Recitation(setting="yajña"))
        self.assertFalse(any(r.optional for r in said))


class Subrahmanya(unittest.TestCase):
    """1.2.37 and 1.2.38 — the one setting that keeps its accents."""

    def test_it_blocks_both_of_the_rules_that_would_flatten_it(self):
        """
        तत्र यज्ञकर्मणि इति विभाषा छन्दसि इति चैकश्रुतिः प्राप्ता प्रतिषिध्यते —
        the prohibition names both, so it has to be tested before either.
        """
        self.assertNotIn(E, registers([U, N, S], setting="subrahmaṇyā"))
        self.assertFalse(ekasruti([U, N, S], Recitation(setting="subrahmaṇyā")))

    def test_a_svarita_there_is_raised_to_udatta(self):
        """स्वरितस्य तूदात्तः — सुब्रह्मण्योम् इन्द्रागच्छ."""
        said = recite([U, S, N], Recitation(setting="subrahmaṇyā"))
        self.assertEqual(said[1].register, Register.UDATTA)
        self.assertEqual(said[1].by, "1.2.37")

    def test_but_in_deva_and_brahman_it_is_lowered(self):
        """देवब्रह्मणोरनुदात्तः — देवा ब्रह्माण आगच्छत."""
        for word in ("deva", "brahman"):
            with self.subTest(word=word):
                said = recite([S, U], Recitation(setting="subrahmaṇyā",
                                                 words=(word, "x")))
                self.assertEqual(said[0].register, Register.ANUDATTA)
                self.assertEqual(said[0].by, "1.2.38")

    def test_the_exception_reaches_only_those_two_words(self):
        """
        Which is what makes 1.2.38 an exception rather than a replacement of
        1.2.37. Any other word of the same invocation still goes up.
        """
        said = recite([S], Recitation(setting="subrahmaṇyā", words=("indra",)))
        self.assertEqual(said[0].register, Register.UDATTA)
        self.assertEqual(said[0].by, "1.2.37")

    def test_a_syllable_that_is_not_a_svarita_is_untouched_either_way(self):
        said = recite([U, N], Recitation(setting="subrahmaṇyā",
                                         words=("deva", "deva")))
        self.assertEqual(tuple(r.register for r in said),
                         (Register.UDATTA, Register.ANUDATTA))


class OverASequence(unittest.TestCase):
    """
    1.2.39 and 1.2.40 — the two that need neighbours.

    These are the tests that can catch a rule reading the wrong way, which is
    the mistake most available here: both sūtras are about an anudātta beside
    a higher tone, and they differ in which side.
    """

    def test_1_2_39_looks_backward(self):
        """
        इमं मे गङ्गे यमुने सरस्वति शुतुद्रि — everything after the svarita on
        मे runs at one tone. What is *before* it does not.
        """
        said = registers([U, S, N, N, N], samhita=True)
        self.assertEqual(said, (Register.UDATTA, Register.SVARITA, E, E, E))

    def test_and_only_in_continuous_speech(self):
        """
        संहिताग्रहणं किम्? अवग्रहे मा भूत् — इमं। मे। गङ्गे। यमुने। सरस्वति।
        Said word by word, each anudātta keeps itself.
        """
        self.assertNotIn(E, registers([U, S, N, N, N]))

    def test_an_anudatta_before_the_svarita_is_untouched_by_it(self):
        """The window opens at the svarita and not before."""
        said = recite([N, S, N], Recitation(samhita=True))
        self.assertNotEqual(said[0].register, E)
        self.assertEqual(said[2].register, E)

    def test_1_2_40_looks_forward(self):
        """
        उदात्तः परो यस्मात् स उदात्तपरः — the anudātta *before* the high tone.
        Both of the Kāśikā's examples, one for each half of the compound.
        """
        self.assertEqual(registers([N, U]), (SN, Register.UDATTA))
        self.assertEqual(registers([N, S]), (SN, Register.SVARITA))

    def test_and_not_backward(self):
        """An anudātta after an udātta, with nothing following, is not sannatara."""
        self.assertEqual(registers([U, N]), (Register.UDATTA, Register.ANUDATTA))

    def test_the_last_syllable_has_nothing_after_it(self):
        """An off-by-one here would read past the end of the phrase."""
        self.assertEqual(registers([U, N])[-1], Register.ANUDATTA)
        self.assertEqual(registers([N])[0], Register.ANUDATTA)

    def test_1_2_39_takes_precedence_over_1_2_40_where_both_reach(self):
        """
        In continuous speech, an anudātta both following a svarita and
        preceding an udātta is claimed by 1.2.39, which is why the Kāśikā's
        सरस्वति example has शुतुद्रि after it and still reads as one tone.
        """
        said = recite([S, N, U], Recitation(samhita=True))
        self.assertEqual(said[1].register, E)
        self.assertEqual(said[1].by, "1.2.39")

    def test_an_empty_phrase_is_answered_and_not_crashed_on(self):
        self.assertEqual(recite([], Recitation()), ())


class EveryVerdictIsAccountable(unittest.TestCase):
    def test_each_syllable_names_a_sutra_and_gives_a_reason(self):
        for where in (Recitation(),
                      Recitation(setting="dūrāt-sambuddhi"),
                      Recitation(setting="yajña"),
                      Recitation(setting="chandas"),
                      Recitation(setting="subrahmaṇyā"),
                      Recitation(samhita=True)):
            for said in recite([U, N, S, N], where):
                self.assertTrue(said.by, where)
                self.assertGreater(len(said.why), 20, where)

    def test_the_registers_are_six_and_only_three_are_accents(self):
        """
        एकश्रुति, सन्नतर and उच्चैस्तराम् are not accents. 1.2.29–1.2.31 named
        three, and these eight sūtras add three more ways of saying them, so
        the return type has to be wider than `Accent` or the distinction is
        lost.
        """
        self.assertEqual(len(Register), 6)
        named_by_1_2_29_to_31 = {"udātta", "anudātta", "svarita"}
        added = {r.value for r in Register} - named_by_1_2_29_to_31
        self.assertEqual(added, {"ekaśruti", "sannatara", "uccaistarām"})


class Registration(unittest.TestCase):
    def test_the_whole_of_1_2_1_to_1_2_46_is_codified(self):
        missing = [f"1.2.{n}" for n in range(1, 47) if not REGISTRY.has(f"1.2.{n}")]
        self.assertEqual(missing, [])

    def test_1_2_40_is_the_only_one_that_does_not_carry_ekasruti(self):
        """
        Seven of the eight carry एकश्रुति from 1.2.33; 1.2.40 carries
        अनुदात्तानाम् from 1.2.39 instead, which is why it prescribes a
        register rather than the absence of one. The corpus's anuvṛtti, which
        nobody here wrote, records exactly that split.
        """
        def carries(sutra_id, word):
            return any(item.word.startswith(word)
                       for item in facts(sutra_id).anuvrtti)

        for number in range(34, 40):
            self.assertTrue(carries(f"1.2.{number}", "एकश्रुति"), f"1.2.{number}")
        self.assertFalse(carries("1.2.40", "एकश्रुति"))
        self.assertTrue(carries("1.2.40", "अनुदात्तानाम्"))

    def test_the_records_say_what_is_taken_as_given(self):
        """
        Two of these sūtras act on a svarita that 8.4.66 produces, and 8.4.66
        is not codified. Both records have to say so, since otherwise a reader
        would take the input for a derivation.
        """
        for sutra_id in ("1.2.37", "1.2.39"):
            notes = REGISTRY.get(sutra_id).notes
            self.assertIn("8.4.66", notes, sutra_id)

    def test_the_sambuddhi_of_1_2_33_is_not_the_samjna_of_2_3_49(self):
        """
        The Kāśikā says न एकवचनं सम्बुद्धिः in as many words. A reader who has
        met the other saṃjñā will assume this is it, so the record has to
        distinguish them.
        """
        notes = REGISTRY.get("1.2.33").notes
        self.assertIn("2.3.49", notes)
        self.assertIn("एकवचनं सम्बुद्धिः", notes)


if __name__ == "__main__":
    unittest.main()
