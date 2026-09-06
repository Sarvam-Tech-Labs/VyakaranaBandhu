# -*- coding: utf-8 -*-
"""
Tests for 1.4.56 to 1.4.110 — the particles, the endings, and the close.

The thing worth testing hardest here is the opposite of what the kāraka block
needed. There, 1.4.1 एका संज्ञा was the mechanism and the tests had to show one
name displacing another. Here the section is written to *escape* 1.4.1, twice
and with a named device each time, and the tests have to show names standing
together — because a codification that returned a single name would pass every
one-condition test and lose the whole point of the section.

The two devices, in the Kāśikā's words:

    1.4.56   प्राग्वचनं संज्ञासमावेशार्थम्
    1.4.60   चकारः संज्ञासमावेशार्थः

and against them, the yogavibhāga at 1.4.60 that does the reverse — splitting
गति off so that everything from 1.4.61 gets it *without* उपसर्ग.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.nipata import (
    PROVISIONS,
    Name,
    Particle,
    cadi,
    in_nipata_range,
    names_of,
    placement,
    pradi,
    sakshatprabhrti,
    uryadi,
)
from src.astadhyayi.sutra import REGISTRY
from src.astadhyayi.vibhakti import (
    ATMANEPADA_ENDINGS,
    MADHYAMA,
    PARASMAIPADA_ENDINGS,
    PRATHAMA,
    UTTAMA,
    ending_facts,
    endings_of,
    juncture,
    person_for,
)

N, U, G, K = Name.NIPATA, Name.UPASARGA, Name.GATI, Name.KARMAPRAVACANIYA


class NamesCoApply(unittest.TestCase):
    """The point of the section: these four names stand together."""

    def test_a_prefix_with_a_verb_takes_three_names_at_once(self):
        """
        प्र construed with a verb is निपात by 1.4.58, उपसर्ग by 1.4.59, and
        गति by 1.4.60's च. All three, not the latest of them.
        """
        verdict = names_of("pra", kriya_yoga=True)
        self.assertEqual(verdict.names, frozenset({N, U, G}))
        self.assertIn("1.4.59", verdict.by)

    def test_and_the_verdict_says_why_that_is_allowed(self):
        """
        Under 1.4.1 it should not be. A reader who knows that rule and sees
        three names needs to be told which device is at work.
        """
        why = names_of("pra", kriya_yoga=True).why
        self.assertIn("संज्ञासमावेशार्थ", why)
        self.assertIn("1.4.1", why)

    def test_without_a_verb_the_prefix_is_only_a_particle(self):
        """
        क्रियायोगे is the whole of 1.4.59, and प्रनायको देशः shows it.

        The citation names 1.4.56 as well as 1.4.58, and that is the range
        doing its work: 1.4.56 gives the निपात name by *being* a range and
        contributes no condition, so it would otherwise go unmentioned and a
        reader would see a name with no rule behind it.
        """
        verdict = names_of("pra")
        self.assertEqual(verdict.names, frozenset({N}))
        self.assertEqual(verdict.by, ("1.4.56", "1.4.58"))

    def test_a_karmapravacaniya_is_a_particle_too(self):
        verdict = names_of("anu", sense="lakṣaṇa")
        self.assertIn(K, verdict.names)
        self.assertIn(N, verdict.names)

    def test_the_same_word_is_upasarga_or_karmapravacaniya_by_one_condition(self):
        """
        अनु with a verb is an उपसर्ग; अनु without one, marking a sign, is a
        कर्मप्रवचनीय. The section turns on क्रियायोगे and nothing else.
        """
        with_verb = names_of("anu", kriya_yoga=True)
        self.assertIn(U, with_verb.names)
        self.assertNotIn(K, with_verb.names)

        without = names_of("anu", sense="lakṣaṇa")
        self.assertIn(K, without.names)
        self.assertNotIn(U, without.names)


class TheYogavibhaga(unittest.TestCase):
    """
    1.4.60's split, which does the reverse of its own च.

    उत्तरत्र गतिसंज्ञैव यथा स्यात्, उपसर्गसंज्ञा मा भूत् — from 1.4.61 on,
    गति and *not* उपसर्ग, because ऊरीस्यात् would otherwise take 8.3.87's
    ṣatva. This is the test that a codification treating 1.4.59 and 1.4.61 as
    the same shape would fail.
    """

    def test_uryadi_gets_gati_but_not_upasarga(self):
        verdict = names_of("ūrī", kriya_yoga=True)
        self.assertIn(G, verdict.names)
        self.assertNotIn(U, verdict.names)

    def test_while_pradi_gets_both(self):
        self.assertIn(U, names_of("pra", kriya_yoga=True).names)

    def test_and_the_same_for_every_later_provision_in_the_section(self):
        """
        Structural: no provision from 1.4.61 to 1.4.79 may give उपसर्ग, or the
        split has been undone somewhere.
        """
        for provision in PROVISIONS:
            number = int(provision.sutra.rsplit(".", 1)[1])
            if 61 <= number <= 79:
                self.assertNotIn(U, provision.gives, provision.sutra)


class ReadRatherThanListed(unittest.TestCase):
    def test_the_four_ganas_come_from_the_ganapatha(self):
        self.assertEqual(len(pradi()), 22)
        self.assertEqual(pradi()[0], "pra")
        self.assertEqual(pradi()[-1], "upa")
        self.assertGreater(len(cadi()), 150)
        self.assertEqual(cadi()[0], "ca")
        self.assertEqual(uryadi()[0], "ūrī")
        self.assertEqual(sakshatprabhrti()[0], "sākṣāt")

    def test_pradi_is_exactly_the_twenty_two_upasargas(self):
        """
        Which is the fact 1.4.59 depends on: the gaṇa is closed, and the
        prefixes of the language are its members and no others.
        """
        for prefix in ("pra", "parā", "apa", "sam", "anu", "ava", "nis",
                       "vi", "ni", "adhi", "api", "ati", "su", "ud", "abhi",
                       "prati", "pari", "upa"):
            self.assertIn(prefix, pradi(), prefix)
        self.assertNotIn("ūrī", pradi())


class WorkedForms(unittest.TestCase):
    """One per sūtra where the Kāśikā gives a form."""

    def test_the_gati_sutras(self):
        for sutra, form, asserted in [
            ("1.4.61", "ūrīkṛtya", dict(form="ūrī", kriya_yoga=True)),
            ("1.4.62", "khāṭkṛtya",
             dict(form="khāṭ", kriya_yoga=True, anukarana=True)),
            ("1.4.63", "satkṛtya",
             dict(form="sat", kriya_yoga=True, sense="ādara")),
            ("1.4.64", "alaṃkṛtya",
             dict(form="alam", kriya_yoga=True, sense="bhūṣaṇa")),
            ("1.4.67", "puraskṛtya", dict(form="puras", kriya_yoga=True)),
            ("1.4.68", "astaṃgatya", dict(form="astam", kriya_yoga=True)),
            ("1.4.71", "tirobhūya",
             dict(form="tiras", kriya_yoga=True, sense="antardhi")),
        ]:
            with self.subTest(sutra=sutra, form=form):
                verdict = names_of(**asserted)
                self.assertIn(G, verdict.names)
                self.assertIn(sutra, verdict.by)

    def test_1_4_62_needs_both_of_its_conditions(self):
        """
        अनुकरणं *च अनितिपरम्*. An earlier draft of the provision had neither
        condition, and it then fired for every word construed with a verb.
        """
        self.assertEqual(
            names_of("khāṭ", kriya_yoga=True, anukarana=True,
                     followed_by_iti=True).names,
            frozenset(),
        )
        self.assertEqual(names_of("khāṭ", kriya_yoga=True).names, frozenset())

    def test_the_karmapravacaniya_sutras(self):
        for sutra, asserted in [
            ("1.4.84", dict(form="anu", sense="lakṣaṇa")),
            ("1.4.85", dict(form="anu", sense="tṛtīyārtha")),
            ("1.4.86", dict(form="anu", sense="hīna")),
            ("1.4.87", dict(form="upa", sense="adhika")),
            ("1.4.88", dict(form="apa", sense="varjana")),
            ("1.4.89", dict(form="āṅ", sense="maryādā")),
            ("1.4.92", dict(form="prati", sense="pratinidhi")),
            ("1.4.93", dict(form="adhi", sense="anarthaka")),
            ("1.4.94", dict(form="su", sense="pūjā")),
            ("1.4.95", dict(form="ati", sense="atikramaṇa")),
            ("1.4.96", dict(form="api", sense="garhā")),
            ("1.4.97", dict(form="adhi", sense="īśvara")),
        ]:
            with self.subTest(sutra=sutra):
                verdict = names_of(**asserted)
                self.assertIn(K, verdict.names)
                self.assertIn(sutra, verdict.by)

    def test_1_4_90_is_the_sutra_1_3_10_refuses_to_pair(self):
        """
        Three words against five senses. 1.3.10's codification returns None
        for unequal lists, and this is the case it does that for — the two
        sūtras were codified ninety apart and have to agree.
        """
        from src.astadhyayi.reading import yathasamkhya

        provision = next(p for p in PROVISIONS if p.sutra == "1.4.90")
        self.assertEqual(len(provision.words), 3)
        self.assertIsNone(
            yathasamkhya(provision.words,
                         provision.senses + ("itthaṃbhūtākhyāna",)),
        )
        for word in provision.words:
            self.assertIn(K, names_of(word, sense="lakṣaṇa").names, word)


class Placement(unittest.TestCase):
    """1.4.80 to 1.4.82."""

    def test_before_the_root(self):
        self.assertEqual(placement(Particle("pra"))[0], "1.4.80")

    def test_after_it_only_in_the_veda(self):
        self.assertEqual(
            placement(Particle("pra", after_dhatu=True))[0], "1.4.80")
        self.assertEqual(
            placement(Particle("pra", after_dhatu=True, chandas=True))[0],
            "1.4.81")

    def test_and_apart_from_it_only_in_the_veda(self):
        self.assertEqual(
            placement(Particle("pra", separated=True, chandas=True))[0],
            "1.4.82")


class Endings(unittest.TestCase):
    """1.4.99 to 1.4.104, which do nothing separately."""

    def test_the_eighteen_are_indexed_by_position(self):
        for ending, pada, person, number in [
            ("tip", "parasmaipada", PRATHAMA, "ekavacana"),
            ("tas", "parasmaipada", PRATHAMA, "dvivacana"),
            ("jhi", "parasmaipada", PRATHAMA, "bahuvacana"),
            ("sip", "parasmaipada", MADHYAMA, "ekavacana"),
            ("mip", "parasmaipada", UTTAMA, "ekavacana"),
            ("ta", "ātmanepada", PRATHAMA, "ekavacana"),
            ("thās", "ātmanepada", MADHYAMA, "ekavacana"),
            ("mahiṅ", "ātmanepada", UTTAMA, "bahuvacana"),
        ]:
            with self.subTest(ending=ending):
                found = ending_facts(ending)
                self.assertEqual(found.pada, pada)
                self.assertEqual(found.person, person)
                self.assertEqual(found.number, number)
                self.assertTrue(found.vibhakti)

    def test_there_are_nine_of_each(self):
        self.assertEqual(len(endings_of(pada="parasmaipada")), 9)
        self.assertEqual(len(endings_of(pada="ātmanepada")), 9)
        self.assertEqual(sum(len(r) for r in PARASMAIPADA_ENDINGS), 9)
        self.assertEqual(sum(len(r) for r in ATMANEPADA_ENDINGS), 9)

    def test_three_rows_of_three_and_no_repeats(self):
        """
        त्रीणि त्रीणि, and the whole rule is in the arrangement — so the
        arrangement is what to check.
        """
        flat = [e for row in PARASMAIPADA_ENDINGS + ATMANEPADA_ENDINGS
                for e in row]
        self.assertEqual(len(flat), 18)
        self.assertEqual(len(set(flat)), 18)
        for row in PARASMAIPADA_ENDINGS + ATMANEPADA_ENDINGS:
            self.assertEqual(len(row), 3)

    def test_1_4_99_names_what_1_3_12_had_been_using(self):
        """
        The name परस्मैपद is used at 1.3.12, ninety sūtras before it is given
        here. Both blocks are codified, so the two spellings must agree or one
        of them is talking about nothing.
        """
        from src.astadhyayi.pada import Pada

        self.assertEqual(Pada.PARASMAIPADA.value, "parasmaipada")
        self.assertEqual(Pada.ATMANEPADA.value, "ātmanepada")
        self.assertEqual(ending_facts("tip").pada, Pada.PARASMAIPADA.value)
        self.assertEqual(ending_facts("ta").pada, Pada.ATMANEPADA.value)


class Persons(unittest.TestCase):
    """1.4.105 to 1.4.108."""

    def test_the_three_ordinary_cases(self):
        self.assertEqual(person_for(upapada="yuṣmad").person, MADHYAMA)
        self.assertEqual(person_for(upapada="asmad").person, UTTAMA)
        self.assertEqual(person_for().person, PRATHAMA)

    def test_the_pronoun_need_not_be_uttered(self):
        """
        स्थानिनि, glossed प्रयुज्यमानेऽप्यप्रयुज्यमानेऽपि. पचसि alone is second
        person, and that is the clause that makes it so.
        """
        self.assertIn("अप्रयुज्यमाने", person_for(upapada="yuṣmad").why)

    def test_and_must_be_co_referential(self):
        self.assertEqual(
            person_for(upapada="yuṣmad", coreferential=False).person, PRATHAMA)

    def test_the_joke_at_1_4_106(self):
        """
        एहि मन्ये ओदनं भोक्ष्यसे. The main verb takes the second person and
        मन् the first — मध्यमोत्तमयोः प्राप्तयोर् उत्तममध्यमौ विधीयेते, the
        two exchanged — and मन्ये stays singular.
        """
        main = person_for(upapada="manya", prahasa=True)
        self.assertEqual(main.person, MADHYAMA)
        self.assertEqual(main.by, "1.4.106")

        manyate = person_for(upapada="manya", prahasa=True, is_manyati=True)
        self.assertEqual(manyate.person, UTTAMA)
        self.assertTrue(manyate.singular)

    def test_and_only_in_derision(self):
        """प्रहासे इति किम्? एहि मन्यसे ओदनं भोक्ष्ये."""
        self.assertEqual(
            person_for(upapada="manya", prahasa=False).person, PRATHAMA)


class TheClose(unittest.TestCase):
    """1.4.109 and 1.4.110."""

    def test_the_closest_proximity_is_samhita(self):
        found = juncture(gap_matras=0.5)
        self.assertEqual(found.name, "saṃhitā")
        self.assertEqual(found.by, "1.4.109")

    def test_and_a_wider_gap_is_not(self):
        """
        परशब्दोऽतिशये वर्तते — the *closest*, measured at half a mātrā. A rule
        that accepted any proximity would make 1.2.39 apply everywhere.
        """
        self.assertEqual(juncture(gap_matras=2.0).name, "")

    def test_stopping_is_avasana(self):
        self.assertEqual(juncture(stopped=True).name, "avasāna")

    def test_1_4_109_defines_what_1_2_39_was_already_using(self):
        """
        स्वरितात् संहितायाम् is codified and uses the name; this gives it.
        Ninety sūtras apart, and the record at 1.4.109 says so.
        """
        self.assertIn("1.2.39", REGISTRY.get("1.4.109").notes)
        self.assertTrue(REGISTRY.has("1.2.39"))


class AdhyayaOneIsComplete(unittest.TestCase):
    def test_every_sutra_of_the_first_adhyaya_is_codified(self):
        missing = [
            f"{pada}.{n}"
            for pada, count in (("1.1", 75), ("1.2", 73), ("1.3", 93),
                                ("1.4", 110))
            for n in range(1, count + 1)
            if not REGISTRY.has(f"{pada}.{n}")
        ]
        self.assertEqual(missing, [])

    def test_that_is_351_sutras(self):
        first = [s for s in REGISTRY.all() if s.id.adhyaya == 1]
        self.assertEqual(len(first), 351)

    def test_the_range_sutras_stop_where_they_say(self):
        self.assertTrue(in_nipata_range("1.4.57"))
        self.assertTrue(in_nipata_range("1.4.96"))
        self.assertFalse(in_nipata_range("1.4.97"))

    def test_and_1_4_97_is_outside_it_on_purpose(self):
        """
        अधिरीश्वरे is the limit 1.4.56 names, so it stands outside — the
        कर्मप्रवचनीय name reaches it and the निपात heading does not.
        """
        provision = next(p for p in PROVISIONS if p.sutra == "1.4.97")
        self.assertEqual(provision.gives, frozenset({K}))


if __name__ == "__main__":
    unittest.main()
