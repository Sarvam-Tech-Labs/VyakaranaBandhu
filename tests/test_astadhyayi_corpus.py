# -*- coding: utf-8 -*-
"""
Structural integrity of the Aṣṭādhyāyī data, checked across all 3,983 sūtras.

These are not coverage tests. Each one asserts something that must be true of
the Aṣṭādhyāyī itself, so a failure means either the parser is wrong or the
source data is — both worth knowing:

  * anuvṛtti flows FORWARD. A word is carried down from an earlier sūtra into
    a later one, never the reverse. Any back-reference is an error.
  * an adhikāra governs from where it stands onward, so it can never be filed
    under a sūtra that precedes it, and its scope must end after it begins.
  * every cross-reference must point at a sūtra that exists.
  * the eight adhyāyas have four pādas each and the numbering has no holes.

The suite skips itself when reference/ has not been fetched, so a clean
checkout still runs green.
"""

import unittest
from typing import Tuple

from src.astadhyayi import corpus
from src.astadhyayi.sources import (
    VIBHAKTI_NAMES,
    all_sutra_ids,
    facts,
)
from src.astadhyayi.sutra import SutraType


def key(sutra_id: str) -> Tuple[int, int, int]:
    return tuple(int(p) for p in sutra_id.split("."))  # type: ignore[return-value]


class CorpusTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.ids = all_sutra_ids()
        except (corpus.CorpusUnavailable, KeyError) as error:
            raise unittest.SkipTest(str(error))
        cls.known = set(cls.ids)
        cls.facts = {i: facts(i) for i in cls.ids}


class TestSutraNumbering(CorpusTestCase):
    def test_the_work_has_eight_adhyayas_of_four_padas(self):
        seen = {(k[0], k[1]) for k in map(key, self.ids)}
        self.assertEqual(
            sorted(seen), [(a, p) for a in range(1, 9) for p in range(1, 5)]
        )

    def test_every_pada_is_numbered_from_one_without_gaps(self):
        by_pada = {}
        for sutra_id in self.ids:
            adhyaya, pada, number = key(sutra_id)
            by_pada.setdefault((adhyaya, pada), []).append(number)
        gaps = []
        for (adhyaya, pada), numbers in sorted(by_pada.items()):
            numbers.sort()
            if numbers != list(range(1, len(numbers) + 1)):
                expected = set(range(1, max(numbers) + 1))
                gaps.append(f"{adhyaya}.{pada}: missing {sorted(expected - set(numbers))}")
        self.assertEqual(gaps, [], "\n".join(gaps))

    def test_the_traditional_total(self):
        # Editions differ by a few; this pins the count we actually hold so a
        # silent change to the data cannot pass unnoticed.
        self.assertEqual(len(self.ids), 3983)


class TestAnuvrtti(CorpusTestCase):
    """
    Anuvṛtti is continuation: a word persists from an earlier sūtra into later
    ones. A reference pointing forward, or at itself, would be incoherent.
    """

    def test_anuvrtti_always_points_backward(self):
        violations = []
        for sutra_id in self.ids:
            for item in self.facts[sutra_id].anuvrtti:
                if key(item.from_sutra) >= key(sutra_id):
                    violations.append(
                        f"{sutra_id} carries {item.word} from {item.from_sutra} "
                        f"— which is not earlier"
                    )
        self.assertEqual(violations[:20], [], f"{len(violations)} violations")

    def test_every_anuvrtti_source_exists(self):
        missing = {
            f"{sid} <- {item.from_sutra}"
            for sid in self.ids
            for item in self.facts[sid].anuvrtti
            if item.from_sutra not in self.known
        }
        self.assertEqual(sorted(missing)[:20], [], f"{len(missing)} dangling")

    def test_anuvrtti_is_actually_present_in_the_work(self):
        # A sanity floor: continuation is pervasive in the Aṣṭādhyāyī, so a
        # parser returning almost nothing would be silently broken.
        with_anuvrtti = [i for i in self.ids if self.facts[i].anuvrtti]
        self.assertGreater(len(with_anuvrtti), 1000)

    def test_1_1_3_carries_the_two_samjnas_defined_before_it(self):
        carried = {i.from_sutra: i.word for i in self.facts["1.1.3"].anuvrtti}
        self.assertEqual(set(carried), {"1.1.1", "1.1.2"})


class TestAdhikara(CorpusTestCase):
    """A heading governs forward from where it stands."""

    def test_an_adhikara_never_precedes_itself(self):
        violations = []
        for sutra_id in self.ids:
            for item in self.facts[sutra_id].adhikara:
                if key(item.sutra) > key(sutra_id):
                    violations.append(
                        f"{sutra_id} is governed by {item.sutra}, which comes later"
                    )
        self.assertEqual(violations[:20], [], f"{len(violations)} violations")

    def test_every_adhikara_source_exists(self):
        missing = {
            item.sutra
            for sid in self.ids
            for item in self.facts[sid].adhikara
            if item.sutra not in self.known
        }
        self.assertEqual(sorted(missing), [])

    def test_a_scope_ends_after_it_begins(self):
        bad = [
            f"{f.id} -> {f.scope_end}"
            for f in self.facts.values()
            if f.scope_end and key(f.scope_end) <= key(f.id)
        ]
        self.assertEqual(bad, [])

    def test_every_scope_end_exists(self):
        missing = [
            f"{f.id} -> {f.scope_end}"
            for f in self.facts.values()
            if f.scope_end and f.scope_end not in self.known
        ]
        self.assertEqual(missing, [])

    def test_the_tripadi_scope(self):
        # 8.2.1 pūrvatrāsiddham governs to the end of the work. Everything in
        # its scope is asiddha with respect to what precedes — the single most
        # consequential adhikāra for any prakriyā engine.
        tripadi = self.facts["8.2.1"]
        self.assertEqual(tripadi.type, SutraType.ADHIKARA)
        self.assertEqual(tripadi.scope_end, "8.4.68")
        self.assertEqual(max(self.ids, key=key), "8.4.68")

    def test_the_ekasamjna_scope(self):
        # 1.4.1 ā kaḍārād ekā saṃjñā governs to 2.2.38.
        self.assertEqual(self.facts["1.4.1"].scope_end, "2.2.38")


class TestPadaccheda(CorpusTestCase):
    def test_every_word_carries_a_legal_case_and_number(self):
        bad = []
        for sutra_id in self.ids:
            for pada in self.facts[sutra_id].padas:
                if pada.vibhakti not in VIBHAKTI_NAMES:
                    bad.append(f"{sutra_id}: {pada.word} vibhakti={pada.vibhakti}")
                if pada.vacana not in (0, 1, 2, 3):
                    bad.append(f"{sutra_id}: {pada.word} vacana={pada.vacana}")
        self.assertEqual(bad[:20], [], f"{len(bad)} bad markings")

    def test_an_avyaya_carries_no_number(self):
        # vibhakti 0 marks an indeclinable; a number on it would be incoherent.
        bad = [
            f"{sid}: {p.word}"
            for sid in self.ids
            for p in self.facts[sid].padas
            if p.vibhakti == 0 and p.vacana not in (0,)
        ]
        self.assertEqual(bad[:20], [])

    def test_nearly_every_sutra_is_split(self):
        # A padaccheda is given for the whole work; a parser silently returning
        # empties would show up here.
        unsplit = [i for i in self.ids if not self.facts[i].padas]
        self.assertLess(len(unsplit), 50, f"{len(unsplit)} sūtras have no split")

    def test_case_marking_carries_grammatical_weight(self):
        # 1.1.3's इकः is a genitive, and by 1.1.49 that genitive means "in place
        # of". If the case were dropped the sūtra would be misread as naming
        # what guṇa/vṛddhi are replaced BY.
        ikah = next(p for p in self.facts["1.1.3"].padas if p.word.startswith("इक"))
        self.assertEqual(ikah.vibhakti, 6)
        self.assertEqual(ikah.case_name, "ṣaṣṭhī")
        # 1.1.71's सह is an indeclinable and must not be given a case.
        saha = next(p for p in self.facts["1.1.71"].padas if p.word == "सह")
        self.assertEqual(saha.vibhakti, 0)


class TestSutraTypes(CorpusTestCase):
    def test_every_sutra_has_a_recognised_type(self):
        self.assertTrue(all(isinstance(f.type, SutraType) for f in self.facts.values()))

    def test_the_type_distribution_matches_the_source(self):
        counts = {}
        for f in self.facts.values():
            counts[f.type] = counts.get(f.type, 0) + 1
        # vidhi rules vastly predominate; saṃjñā and paribhāṣā are the small
        # closed classes the rest of the machine is built from.
        self.assertEqual(counts[SutraType.VIDHI], 3629)
        self.assertEqual(counts[SutraType.SAMJNA], 200)
        self.assertEqual(counts[SutraType.ATIDESA], 67)
        self.assertEqual(counts[SutraType.ADHIKARA], 64)
        self.assertEqual(counts[SutraType.PARIBHASA], 23)
        self.assertEqual(sum(counts.values()), 3983)

    def test_known_types_are_right(self):
        for sutra_id, expected in [
            ("1.1.1", SutraType.SAMJNA),      # vṛddhi saṃjñā
            ("1.1.2", SutraType.SAMJNA),      # guṇa saṃjñā
            ("1.1.3", SutraType.PARIBHASA),   # where guṇa/vṛddhi land
            ("1.1.49", SutraType.PARIBHASA),  # ṣaṣṭhī sthāneyogā
            ("1.4.1", SutraType.ADHIKARA),    # ā kaḍārād ekā saṃjñā
            ("8.2.1", SutraType.ADHIKARA),    # pūrvatrāsiddham
            ("1.2.1", SutraType.ATIDESA),     # ṅit-hood extended
        ]:
            self.assertEqual(self.facts[sutra_id].type, expected, sutra_id)


class TestTextAgreesWithTheWitnesses(CorpusTestCase):
    """
    data.json is a third witness to the sūtra text, independent of the two
    already collated. Where all three agree the text is about as secure as it
    can get; where data.json parts company with both, that is worth knowing.
    """

    def test_data_json_is_a_third_witness_agreeing_with_vidyut(self):
        """
        data.json gives Devanāgarī; Vidyut gives SLP1. Rendering the former to
        IAST with the project's own transliterator makes them directly
        comparable — and reuses machinery already under test rather than
        inventing a second romanisation here.
        """
        from src.normalizer import devanagari_to_iast

        collated = corpus.collate()
        agree, differ = 0, []
        for sutra_id in self.ids:
            entry = collated.get(sutra_id)
            if not entry or "vidyut" not in entry.witnesses:
                continue
            ours = corpus._normalize(devanagari_to_iast(self.facts[sutra_id].devanagari))
            theirs = corpus._normalize(entry.witnesses["vidyut"])
            # Anusvāra is written ṃ by one and ṁ/homorganic by the other; that
            # is orthography, not a difference in the text.
            if corpus._nasal_insensitive(ours) == corpus._nasal_insensitive(theirs):
                agree += 1
            else:
                differ.append(sutra_id)
        checked = agree + len(differ)
        self.assertGreater(checked, 3900)
        # Two independently maintained editions, compared letter for letter
        # through a third piece of code. Anything below a high rate would mean
        # one of the three is wrong.
        self.assertGreater(
            agree / checked,
            0.90,
            f"only {agree}/{checked} agree; first divergences: {differ[:10]}",
        )

    def test_a_known_gretil_error_is_caught_by_the_third_witness(self):
        """
        1.3.7 is cuṭū; GRETIL reads duṭū. With data.json as a third witness the
        majority is unambiguous, which is the point of holding three.
        """
        from src.normalizer import devanagari_to_iast

        third = corpus._normalize(devanagari_to_iast(self.facts["1.3.7"].devanagari))
        witnesses = corpus.collate()["1.3.7"].witnesses
        self.assertTrue(third.startswith("cuṭū") or third.startswith("cuṭu"), third)
        self.assertIn("duṭū", witnesses["gretil"])
        self.assertIn("cuṭū", witnesses["vidyut"])

    def test_devanagari_is_present_for_every_sutra(self):
        empty = [i for i in self.ids if not self.facts[i].devanagari.strip()]
        self.assertEqual(empty, [])

    def test_1_1_1_reads_as_expected_in_all_three_witnesses(self):
        collated = corpus.collate()["1.1.1"]
        self.assertEqual(collated.classify(), "identical")
        self.assertEqual(self.facts["1.1.1"].devanagari, "वृद्धिरादैच्")


class TestCommentaryCoverage(CorpusTestCase):
    """What the commentaries actually cover, so a record's slots are honest."""

    def test_kashika_covers_the_whole_work(self):
        kashika = corpus.load_commentary("kashika")
        covered = sum(
            1 for i in self.ids if corpus.commentary_key(i) in kashika
        )
        self.assertGreater(covered / len(self.ids), 0.95)

    def test_mahabhasya_covers_only_part_of_the_work(self):
        # Patañjali comments selectively. A record claiming bhāṣya everywhere
        # would be wrong, which is why the slot goes ABSENT where he is silent.
        bhasya = corpus.load_mahabhasya()
        self.assertGreater(len(bhasya), 1000)
        self.assertLess(len(bhasya), len(self.ids))

    def test_a_sutra_patanjali_passes_over_is_reported_absent(self):
        from src.astadhyayi.sources import mahabhasya_reading
        from src.astadhyayi.sutra import Status

        commented = mahabhasya_reading("1.1.1")
        self.assertEqual(commented.status, Status.VERIFIED)
        self.assertIn("Kielhorn", commented.locator)
        silent = mahabhasya_reading("1.1.2")
        self.assertEqual(silent.status, Status.ABSENT)
        self.assertFalse(silent.locator)

class Varttikas(unittest.TestCase):
    """
    Kātyāyana's supplements — 921 of them, and unused until they were looked
    for. Two are already load-bearing in the codification.
    """

    def setUp(self):
        self.varttikas = corpus.load_varttikas()

    def test_the_collection_loads(self):
        total = sum(len(v) for v in self.varttikas.values())
        self.assertEqual(total, 921)
        self.assertGreater(len(self.varttikas), 500)

    def test_every_varttika_attaches_to_a_real_sutra(self):
        known = set(all_sutra_ids())
        for sutra_id in self.varttikas:
            self.assertIn(sutra_id, known, sutra_id)

    def test_the_rl_savarnatva_varttika_is_here(self):
        """
        ऋऌवर्णयोर्मिथः सावर्ण्यं वाच्यम् — cited on 1.1.9 from the Mahābhāṣya
        before this collection was read. Finding it here independently is a
        check on both.
        """
        texts = [v.text for v in corpus.varttikas_on("1.1.9")]
        self.assertTrue(
            any("सावर्ण्यं" in t for t in texts), texts
        )

    def test_the_pratyayalaksana_varttika_on_1_1_62(self):
        """वर्णाश्रये नास्ति प्रत्ययलक्षणम् — a restriction the Kāśikā on that
        sūtra does not give, and the reason the collection was worth reading."""
        texts = [v.text for v in corpus.varttikas_on("1.1.62")]
        self.assertTrue(any("वर्णाश्रये" in t for t in texts), texts)

    def test_a_sutra_with_no_varttika_returns_nothing(self):
        self.assertEqual(corpus.varttikas_on("1.1.1"), ())

    def test_they_reach_the_record_as_a_source_of_their_own(self):
        import src.astadhyayi.rules  # noqa: F401
        from src.astadhyayi.sutra import REGISTRY, Source, Status

        with_varttika = REGISTRY.get("1.1.9").reading(Source.VARTTIKA)
        self.assertIs(with_varttika.status, Status.VERIFIED)
        self.assertTrue(with_varttika.locator)
        self.assertIn("सावर्ण्यं", with_varttika.text)

        without = REGISTRY.get("1.1.1").reading(Source.VARTTIKA)
        self.assertIs(
            without.status, Status.ABSENT,
            "the collection is complete, so silence is absence and not a "
            "book still unread",
        )


class Subcommentaries(unittest.TestCase):
    """
    Five further commentaries that were on disk and unconsulted: the Nyāsa, the
    Padamañjarī, the Siddhāntakaumudī, the Tattvabodhinī, the Bālamanoramā.
    """

    #: Measured coverage, as a floor. These are lower bounds, not targets.
    FLOORS = {
        "kashika": 0.99, "vasu_english": 0.99, "kaumudi": 0.95,
        "nyaas": 0.80, "padamanjari": 0.80, "balamanorama": 0.70,
        "tattvabodhini": 0.60,
    }

    def test_each_covers_at_least_what_was_measured(self):
        total = len(list(all_sutra_ids()))
        for name, floor in self.FLOORS.items():
            loaded = corpus.load_commentary(name)
            filled = sum(
                1 for v in loaded.values()
                if isinstance(v, str) and v.strip()
            )
            self.assertGreaterEqual(
                filled / total, floor, f"{name} covers only {filled}/{total}"
            )

    def test_they_all_speak_on_1_1_9(self):
        for name in self.FLOORS:
            text = corpus.commentary_on("1.1.9", name)
            self.assertTrue(text, name)

    def test_they_reach_the_record(self):
        import src.astadhyayi.rules  # noqa: F401
        from src.astadhyayi.sutra import REGISTRY, Source, Status

        verified = {
            r.source for r in REGISTRY.get("1.1.9").readings
            if r.status is Status.VERIFIED
        }
        for source in (Source.NYASA, Source.PADAMANJARI, Source.KAUMUDI,
                       Source.TATTVABODHINI, Source.BALAMANORAMA):
            self.assertIn(source, verified, source)

    def test_silence_is_recorded_as_absent_not_pending(self):
        """
        A commentary that is here and says nothing has been consulted. Calling
        that PENDING would mean the book is still on the shelf.
        """
        import src.astadhyayi.rules  # noqa: F401
        from src.astadhyayi.sutra import REGISTRY, Status

        for sutra in REGISTRY.all():
            for reading in sutra.readings:
                if reading.status is Status.PENDING:
                    self.assertIn(
                        reading.source.value,
                        ("sharma", "joshi_roodbergen", "abhyankar_shukla",
                         "benson"),
                        f"{sutra.id}: {reading.source.value} is on disk and "
                        f"should not be pending",
                    )


class Prayogas(unittest.TestCase):
    """Attested forms from literature — 5,377 across 1,712 sūtras."""

    def test_the_collection_loads_and_says_what_it_refused(self):
        """
        The file has flaws of its own: 35 entries name a work and a verse but
        no word, and two attach to sūtras that do not exist — 3.5.35 when no
        adhyāya has a fifth pāda, and 6.3.161 when 6.3 ends at 139, carrying
        one attestation each. 37 entries go in all, and seven sūtras lose
        every attestation they had. The drop is counted rather than silent.
        """
        loaded = corpus.load_prayogas()
        self.assertEqual(sum(len(v) for v in loaded.values()), 5377 - 37)
        self.assertEqual(len(loaded), 1712 - 7)
        self.assertEqual(len(corpus.PRAYOGA_DROPPED), 37)
        self.assertEqual(
            sorted(d for d in corpus.PRAYOGA_DROPPED if "no such" in d),
            ["3.5.35: no such sūtra", "6.3.161: no such sūtra"],
        )

    def test_every_attestation_names_a_work_and_a_place(self):
        for entries in list(corpus.load_prayogas().values())[:200]:
            for entry in entries:
                self.assertTrue(entry.word, entry)
                self.assertTrue(entry.work, entry)
                self.assertTrue(entry.locator, entry)

    def test_they_attach_to_real_sutras(self):
        known = set(all_sutra_ids())
        for sutra_id in corpus.load_prayogas():
            self.assertIn(sutra_id, known, sutra_id)

    def test_1_1_5_is_attested_by_a_kit_form(self):
        """
        मृदितकिसलयः in the Kirātārjunīya. मृदित is मृद् + क्त, and क्त is kit,
        so 1.1.5 forbids the guṇa — the very case codified for that sūtra,
        found in a poem.
        """
        words = [p.word for p in corpus.prayogas_on("1.1.5")]
        self.assertIn("मृदितकिसलयः", words)

    def test_a_sutra_with_no_attestation_returns_nothing(self):
        self.assertEqual(corpus.prayogas_on("1.1.71"), ())




class TwoWitnessesMayDisagreeOnlyInEncoding(unittest.TestCase):
    """
    GRETIL writes ṝ as ṛ plus a combining macron; Vidyut uses the
    precomposed letter. Three sūtras — कॄ धान्ये at 3.3.30, and 7.2.38
    and 8.3.10 — were reported as DIVERGENT witnesses to texts that
    agree exactly, and the reading told anyone who looked to "check
    before relying on this text".

    The point of carrying two independent witnesses is that a
    divergence means something. A guard that cries wolf makes the real
    warnings get skimmed, so this asserts the property rather than the
    three sūtras: no pair of witnesses may be called divergent when
    composing them under NFC makes them equal.
    """

    def test_no_divergence_is_an_encoding_difference(self):
        import unicodedata

        from src.astadhyayi.corpus import collate

        offenders = []
        for sutra_id, collated in collate().items():
            if collated.classify() != "divergent":
                continue
            texts = list(collated.witnesses.values())
            if len(texts) != 2:
                continue
            if (unicodedata.normalize("NFC", texts[0])
                    == unicodedata.normalize("NFC", texts[1])):
                offenders.append(sutra_id)
        self.assertEqual(offenders, [])

    def test_the_three_that_were_wrong_now_agree(self):
        from src.astadhyayi.corpus import collate

        collated = collate()
        for sutra_id in ("3.3.30", "7.2.38", "8.3.10"):
            with self.subTest(sutra=sutra_id):
                self.assertEqual(collated[sutra_id].classify(),
                                 "identical")

    def test_and_real_divergences_are_still_reported(self):
        """
        The fix must not have flattened the collation into agreement.
        3.3.55 is a genuine one: GRETIL reads प्रौ where Vidyut and the
        Kāśikā read परौ, which is a different preverb.
        """
        from src.astadhyayi.corpus import collate

        collated = collate()
        self.assertEqual(collated["3.3.55"].classify(), "divergent")
        self.assertIn("prau", collated["3.3.55"].witnesses["gretil"])
        self.assertIn("parau", collated["3.3.55"].witnesses["vidyut"])


if __name__ == "__main__":
    unittest.main()
