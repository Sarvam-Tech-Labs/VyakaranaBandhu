# -*- coding: utf-8 -*-
"""
3.3.16 to 3.3.37 — the घञ् run.

What this block asserts that no earlier one could:

  * यथासंख्यम् binding THREE lists at once, not two;
  * a rule reaching FORWARD by saying 'all', because an अपवाद
    otherwise displaces only what precedes it;
  * a heading dropped with nothing put in its place;
  * two rows carrying one sūtra number, because a vārttika changes
    the output for one of that sūtra's four roots;
  * two conditions on different axes, which one field cannot hold.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.bhava_krt import BHAVA_KRT, bhava_affix
from src.astadhyayi.upapada_krt import Added, NotAdded


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.3.16", dict(root="ruj")),
        ("3.3.16", dict(root="spṛś", sense="upatāpa")),
        ("3.3.17", dict(root="sṛ", sense="sthira")),
        ("3.3.18", dict(root="pac", bhava=True)),
        ("3.3.19", dict(root="pra-as", akartari_karake=True,
                        samjna=True)),
        ("3.3.20", dict(root="kṛ", parimana=True)),
        ("3.3.21", dict(root="iṅ")),
        ("3.3.22", dict(root="ru", upasarga="sam")),
        ("3.3.23", dict(root="yu", upasarga="sam")),
        ("3.3.24", dict(root="bhū")),
        ("3.3.25", dict(root="kṣu", upasarga="vi")),
        ("3.3.26", dict(root="nī", upasarga="ud")),
        ("3.3.27", dict(root="dru", upasarga="pra")),
        ("3.3.28", dict(root="pū", upasarga="nis")),
        ("3.3.29", dict(root="gṝ", upasarga="ud")),
        ("3.3.30", dict(root="kṝ", upasarga="ud", names_a="dhānya")),
        ("3.3.31", dict(root="stu", upasarga="sam", sense="yajña")),
        ("3.3.32", dict(root="stṝ", upasarga="pra")),
        ("3.3.33", dict(root="stṝ", upasarga="vi", sense="prathana")),
        ("3.3.34", dict(root="stṝ", upasarga="vi",
                        names_a="chandonāman")),
        ("3.3.35", dict(root="grah", upasarga="ud")),
        ("3.3.36", dict(root="grah", upasarga="sam", sense="muṣṭi")),
        ("3.3.37", dict(root="nī", upasarga="pari", sense="dyūta")),
    )

    def test_every_rule_answers_and_gives_ghan(self):
        for sutra, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = bhava_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, "ghañ")


class NoCounterExampleReachesTheRuleItCounters(unittest.TestCase):
    """
    Every किम् question the vṛtti asks, put back to the resolver. Each
    must fail to reach the rule it was raised against — the check that
    a condition is doing work rather than sitting in the row.
    """

    COUNTERS = (
        ("3.3.16", dict(root="spṛś"), "sparśo devadattaḥ"),
        ("3.3.17", dict(root="sṛ"), "sartā"),
        ("3.3.22", dict(root="ru"), "ravaḥ"),
        ("3.3.23", dict(root="yu", upasarga="pra"), "prayavaḥ"),
        ("3.3.24", dict(root="bhū", upasarga="pra"), "prabhavaḥ"),
        ("3.3.25", dict(root="kṣu"), "kṣavaḥ"),
        ("3.3.30", dict(root="kṝ", upasarga="ud"), "bhaikṣyotkaraḥ"),
        ("3.3.31", dict(root="stu", upasarga="sam"),
         "saṃstavaś chātrayoḥ"),
        ("3.3.32", dict(root="stṝ", upasarga="pra", sense="yajña"),
         "barhiṣprastaraḥ"),
        ("3.3.33", dict(root="stṝ", upasarga="vi"), "tṛṇavistaraḥ"),
        ("3.3.33", dict(root="stṝ", upasarga="vi", sense="prathana",
                        about="śabda"), "vistaro vacasām"),
        ("3.3.36", dict(root="grah", upasarga="sam"),
         "saṃgraho dhānyasya"),
        ("3.3.37", dict(root="nī", upasarga="pari"), "pariṇayaḥ"),
        ("3.3.20", dict(root="ci", upasarga="nis"), "niścayaḥ"),
    )

    def test_none_of_them_reaches_it(self):
        for sutra, where, form in self.COUNTERS:
            with self.subTest(sutra=sutra, form=form):
                self.assertNotEqual(bhava_affix(**where).by, sutra)


class TwoRowsForOneSutra(unittest.TestCase):
    """
    3.3.16's vārttika स्पृश उपताप changes the OUTPUT for one of the
    sūtra's four roots, so it is a row and not a note — the rule 3.2.24
    established. The two rows carry one sūtra number between them,
    because one sūtra is what they are.
    """

    def test_the_sutra_has_two_rows_and_they_differ_by_sense(self):
        rows = [r for r in BHAVA_KRT if r.sutra == "3.3.16"]
        self.assertEqual(len(rows), 2)
        self.assertEqual({bool(r.sense) for r in rows}, {True, False})

    def test_the_varttika_is_needed_or_the_counter_cannot_be_tested(self):
        self.assertEqual(
            bhava_affix(root="spṛś", sense="upatāpa").by, "3.3.16")
        self.assertIsInstance(bhava_affix(root="spṛś"), NotAdded)

    def test_and_the_three_plain_roots_want_no_sense(self):
        for root in ("pad", "ruj", "viś"):
            with self.subTest(root=root):
                self.assertEqual(bhava_affix(root=root).by, "3.3.16")

    def test_the_scar_about_accent_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.16").notes
        self.assertIn("स्वरे विशेषः", notes)
        self.assertIn("3.2.24", notes)


class YathasankhyamBindingThreeLists(unittest.TestCase):
    """
    3.2.5 and 3.2.13 bound two lists of words; 3.2.186 bound a kāraka
    to a kind of being. 3.3.37 binds preverb, root AND sense together,
    which is why its row holds triples.
    """

    def test_the_bound_combinations_stand(self):
        self.assertEqual(
            bhava_affix(root="nī", upasarga="pari", sense="dyūta").by,
            "3.3.37")
        self.assertEqual(
            bhava_affix(root="i", upasarga="ni", sense="abhreṣa").by,
            "3.3.37")

    def test_and_the_lists_may_not_be_crossed(self):
        """
        The whole point of यथासंख्यम्. Crossing gives forms the rule
        does not license, in either direction and on either axis.
        """
        for where in (
            dict(root="i", upasarga="pari", sense="dyūta"),
            dict(root="nī", upasarga="ni", sense="abhreṣa"),
            dict(root="nī", upasarga="pari", sense="abhreṣa"),
            dict(root="i", upasarga="ni", sense="dyūta"),
        ):
            with self.subTest(**where):
                self.assertNotEqual(bhava_affix(**where).by, "3.3.37")

    def test_the_earlier_rule_binds_only_two(self):
        self.assertEqual(bhava_affix(root="pū", upasarga="nis").by,
                         "3.3.28")
        self.assertEqual(bhava_affix(root="lū", upasarga="abhi").by,
                         "3.3.28")
        for where in (dict(root="lū", upasarga="nis"),
                      dict(root="pū", upasarga="abhi")):
            with self.subTest(**where):
                self.assertNotEqual(bhava_affix(**where).by, "3.3.28")

    def test_three_lists_is_recorded_as_new(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.37").notes
        self.assertIn("3.2.186", notes)
        self.assertIn("3.2.5", notes)


class ThreeThingsToDoWithAPreverb(unittest.TestCase):
    """
    3.3.22 wants one without saying which, 3.3.23 names one, 3.3.24
    refuses one — three rules in a row, three uses of one category.
    """

    def test_wanting_any_preverb(self):
        for upasarga in ("sam", "upa"):
            with self.subTest(upasarga=upasarga):
                self.assertEqual(
                    bhava_affix(root="ru", upasarga=upasarga).by,
                    "3.3.22")
        self.assertIsInstance(bhava_affix(root="ru"), NotAdded)

    def test_naming_one(self):
        self.assertEqual(bhava_affix(root="yu", upasarga="sam").by,
                         "3.3.23")
        self.assertNotEqual(bhava_affix(root="yu", upasarga="pra").by,
                            "3.3.23")

    def test_refusing_one(self):
        self.assertEqual(bhava_affix(root="śri").by, "3.3.24")
        self.assertNotEqual(bhava_affix(root="śri", upasarga="pra").by,
                            "3.3.24")

    def test_the_three_uses_are_distinct_fields_in_the_table(self):
        rows = {r.sutra: r for r in BHAVA_KRT}
        self.assertTrue(rows["3.3.22"].any_upasarga)
        self.assertFalse(rows["3.3.22"].upasarga)
        self.assertTrue(rows["3.3.23"].upasarga)
        self.assertFalse(rows["3.3.23"].any_upasarga)
        self.assertIsNotNone(rows["3.3.24"].no_upasarga)


class TwoConditionsOnDifferentAxes(unittest.TestCase):
    """
    3.3.33 wants the sense to be spreading AND what is spread not to
    be speech. Written on one axis the two cancel, and विस्तरो वचसाम्
    could not be tested at all.
    """

    def test_the_sense_alone_is_not_enough(self):
        self.assertIsInstance(
            bhava_affix(root="stṝ", upasarga="vi"), NotAdded)

    def test_the_sense_with_the_wrong_subject_is_refused(self):
        self.assertNotEqual(
            bhava_affix(root="stṝ", upasarga="vi", sense="prathana",
                       about="śabda").by, "3.3.33")

    def test_both_together_answer(self):
        self.assertEqual(
            bhava_affix(root="stṝ", upasarga="vi",
                       sense="prathana").by, "3.3.33")

    def test_the_row_keeps_them_apart(self):
        row = next(r for r in BHAVA_KRT if r.sutra == "3.3.33")
        self.assertEqual(row.sense, ("prathana",))
        self.assertEqual(row.not_about, ("śabda",))
        self.assertEqual(row.not_sense, ())


class TheWidestRuleIsTheFloor(unittest.TestCase):
    """
    3.3.18 भावे reaches every root, so everything after it narrows and
    the most specific row must win — the shape 3.2.1 and 3.2.110 had.
    """

    def test_bhave_answers_where_nothing_narrower_does(self):
        answer = bhava_affix(root="tyaj", bhava=True)
        self.assertEqual(answer.by, "3.3.18")

    def test_and_loses_wherever_something_narrower_reaches(self):
        answer = bhava_affix(root="iṅ", bhava=True)
        self.assertEqual(answer.by, "3.3.21")

    def test_it_states_the_least_of_any_row(self):
        from src.astadhyayi.bhava_krt import _bhava_specific

        floor = next(r for r in BHAVA_KRT if r.sutra == "3.3.18")
        for row in BHAVA_KRT:
            if row.sutra == "3.3.18":
                continue
            with self.subTest(sutra=row.sutra):
                self.assertGreater(_bhava_specific(row),
                                   _bhava_specific(floor))

    def test_the_debt_3_3_11_owed_is_paid(self):
        """
        3.3.11 named the भाववचन affixes by pointing forward. 3.3.18 is
        codified now, so the class can be reached rather than named.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.18", {str(s.id) for s in REGISTRY.all()})
        self.assertEqual(bhava_affix(root="pac", bhava=True).by,
                         "3.3.18")


class AHeadingDroppedWithNothingPutInItsPlace(unittest.TestCase):
    """
    भविष्यति ran from 3.3.3 and stops at 3.3.16. What replaces it is
    not another heading but a statement the sūtras cannot make:
    इत उत्तरं त्रिष्वपि कालेषु प्रत्ययाः.
    """

    def test_the_heading_run_stops_before_the_ghan_run(self):
        """
        The अधिकार भविष्यति runs 3.3.3 to 3.3.15 and stops — which is
        what the codification must show. Rules further on DO speak of
        the future (3.3.133, 3.3.134, 3.3.139), because they say so
        themselves; a heading stopping is not the time stopping, the
        same distinction 3.3.113 and 3.3.114 forced.
        """
        from src.astadhyayi.lakara import LAKARA

        under = [int(r.sutra.rsplit(".", 1)[1]) for r in LAKARA
                 if r.time == "bhaviṣyat"
                 and int(r.sutra.rsplit(".", 1)[1]) < 16]
        self.assertTrue(under)
        self.assertEqual(sorted(under), sorted(set(under)))

        beyond = [r.sutra for r in LAKARA
                  if r.time == "bhaviṣyat"
                  and int(r.sutra.rsplit(".", 1)[1]) > 15]
        self.assertTrue(
            beyond,
            "rules after the heading still speak of the future — they "
            "state it rather than inheriting it")

    def test_and_where_it_stops_is_recorded_at_both_ends(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.16", REGISTRY.get("3.3.3").notes)
        self.assertIn("निवृत्तम्", REGISTRY.get("3.3.16").notes)


class ARuleReachingForwardBySayingAll(unittest.TestCase):
    """
    3.3.20's सर्वग्रहणम् exists to defeat अप्, which comes at 3.3.57 —
    and it is needed because पुरस्तादपवादन्यायेन an अपवाद displaces
    only what PRECEDES it.
    """

    def test_the_reason_is_recorded_with_the_rule_it_reaches(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.20").notes
        self.assertIn("पुरस्तादपवादन्यायेन", notes)
        self.assertIn("3.3.57", notes)

    def test_and_now_the_rule_it_reaches_forward_to_exists(self):
        """
        PAID. This was written as a failing assertion — 3.3.57 was not
        codified, so 3.3.20's सर्वग्रहण could be recorded and not
        checked. Codifying the अप् run turned it red on schedule.

        What can be checked now is that the two really do compete: with
        a measure named, 3.3.20 wins over the affix it was written to
        defeat, and without one that affix stands.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.57", {str(s.id) for s in REGISTRY.all()})
        self.assertEqual(
            bhava_affix(root="kṛ", root_final="ṝ").by, "3.3.57")
        self.assertEqual(
            bhava_affix(root="kṛ", root_final="ṝ",
                        parimana=True).by, "3.3.20")


class TheDebtThatKeepsBeingIncurred(unittest.TestCase):
    """
    3.3.113 कृत्यल्युटो बहुलम् is the commentary's standing answer for
    a form a run does not give. Two rules of 3.2 leaned on it; four
    more of this pāda do. It is codified in this very pāda.
    """

    def test_every_rule_that_leans_on_it_says_so(self):
        from src.astadhyayi.sutra import REGISTRY

        leaning = [str(s.id) for s in REGISTRY.all()
                   if "3.3.113" in s.notes]
        self.assertIn("3.2.53", leaning)
        self.assertIn("3.2.153", leaning)
        self.assertIn("3.3.24", leaning)
        self.assertIn("3.3.26", leaning)

    def test_and_it_is_codified_now(self):
        """
        PAID, and this is the largest collection so far. Six rules of
        two pādas sent a form here that their own run would not give,
        and a seventh cited it for how far two headings reach.

        What can be checked now is that the rule really does what they
        leaned on it for: it licenses affixes BEYOND where they were
        prescribed, and says so in those words.
        """
        from src.astadhyayi.bhava_krt import krtya_lyut_bahulam
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.113", {str(s.id) for s in REGISTRY.all()})
        answer = krtya_lyut_bahulam()
        self.assertEqual(answer.by, "3.3.113")
        # ततोऽन्यत्रापि — sandhi has swallowed the independent अ,
        # so match from inside the word. The scar that keeps
        # coming back in test substrings.
        self.assertIn("न्यत्रापि भवन्ति", answer.why)

    def test_and_it_licenses_three_distinct_kinds_of_going_beyond(self):
        """
        The vṛtti keeps them apart, so the codification does too — a
        कृत्य affix appearing for another kāraka, ल्युट् appearing for
        भाव and the reverse, and other कृत् affixes departing from what
        they should denote.
        """
        from src.astadhyayi.bhava_krt import (
            KRTYA_LYUT_BAHULAM, krtya_lyut_bahulam,
        )
        from src.astadhyayi.upapada_krt import Added, NotAdded

        self.assertEqual(len(KRTYA_LYUT_BAHULAM), 3)
        for group in KRTYA_LYUT_BAHULAM:
            with self.subTest(group=group):
                self.assertIsInstance(krtya_lyut_bahulam(group), Added)
        self.assertIsInstance(
            krtya_lyut_bahulam("something-else"), NotAdded)

    def test_but_it_still_resolves_nothing(self):
        """
        बहुलम् is not a condition and the entry point does not pretend
        it is — the same refusal 3.3.1 makes about the उणादि affixes at
        the other end of the pāda. The two rules bracket it.
        """
        from src.astadhyayi.bhava_krt import krtya_lyut_bahulam
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("बहुलम्", krtya_lyut_bahulam().why)
        self.assertIn("बहुलम्", REGISTRY.get("3.3.1").notes)
        self.assertIn("3.3.1", REGISTRY.get("3.3.113").notes)


if __name__ == "__main__":
    unittest.main()
