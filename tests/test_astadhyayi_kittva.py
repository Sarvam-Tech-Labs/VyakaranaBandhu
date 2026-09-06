# -*- coding: utf-8 -*-
"""
Tests for 1.2.1 to 1.2.26 — कित्त्व and ङित्त्व by atideśa.

Same shape as the pada-block tests: a table of the forms the Kāśikā works out,
each paired where it gives one with the counter-example that fails the sūtra's
own condition. A rule that fires for its example and not for its
counter-example is being tested; a rule that only fires for its example is not.

Beyond that, this block is mostly *computed* rather than listed, and those are
the tests that can actually fail in an interesting way:

  the shapes    असंयोगान्त, इगन्त, रलन्त, नोपध, व्युपध, झलादि are pratyāhāras
                applied to positions, so each has a right answer the Kāśikā's
                counter-examples pin down
  कुटादि        a run in the dhātupāṭha between two ends the Kāśikā names
  the marks     क्त्वा is kit and तिप् is पित् by the it-rules already codified,
                so nothing here is told which affixes are which
  घु            1.1.20's six roots, read from where they were already settled
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import formation
from src.astadhyayi.kittva import (
    PROVISIONS,
    Formation,
    already,
    behaves_as,
    kutadi,
    near_misses,
    provisions_for,
    resolve,
)
from src.astadhyayi.corpus import load_dhatupatha
from src.astadhyayi.pada import entries_for, root_key
from src.astadhyayi.samjna import ghu_roots
from src.astadhyayi.sutra import REGISTRY


#: (sūtra, the form, the formation, what it behaves as, by which sūtra)
WORKED = [
    # 1.2.1 – 1.2.4, made to behave as ṅit
    ("1.2.1", "utkuṭitā", dict(root="kuṭ", affix="tṛc", given=["seṭ"]),
     ("ṅit",), "1.2.1"),
    ("1.2.1", "utpuṭitā", dict(root="puṭ", affix="tṛc", given=["seṭ"]),
     ("ṅit",), "1.2.1"),
    ("1.2.1", "utkoṭayati", dict(root="kuṭ", affix="ṇic", ending="ṇic"),
     (), None),
    ("1.2.1", "vicitā", dict(root="vyac", affix="tṛc", given=["seṭ"]),
     ("ṅit",), "1.2.1v1"),
    ("1.2.1", "uruvyacāḥ", dict(root="vyac", affix="tṛc", sense="anas"),
     (), None),
    ("1.2.2", "udvijitā", dict(root="vij", affix="tṛc", given=["seṭ"]),
     ("ṅit",), "1.2.2"),
    ("1.2.2", "udvejanam", dict(root="vij", affix="lyuṭ"), (), None),
    ("1.2.4", "kurutaḥ", dict(root="kṛ", affix="sārvadhātuka", ending="tas"),
     ("ṅit",), "1.2.4"),
    ("1.2.4", "kurvanti", dict(root="kṛ", affix="sārvadhātuka", ending="jhi"),
     ("ṅit",), "1.2.4"),
    ("1.2.4", "karoti", dict(root="kṛ", affix="sārvadhātuka", ending="tip"),
     (), None),

    # 1.2.5 – 1.2.17, made to behave as kit
    ("1.2.5", "bibhidatuḥ", dict(root="bhid", affix="liṭ", ending="atus"),
     ("kit",), "1.2.5"),
    ("1.2.5", "cicchidatuḥ", dict(root="chid", affix="liṭ", ending="atus"),
     ("kit",), "1.2.5"),
    ("1.2.5", "ījatuḥ", dict(root="yaj", affix="liṭ", ending="atus"),
     ("kit",), "1.2.5"),
    ("1.2.5", "sasraṃse", dict(root="srans", affix="liṭ", ending="atus"),
     (), None),
    ("1.2.5", "dadhvaṃse", dict(root="dhvans", affix="liṭ", ending="atus"),
     (), None),
    ("1.2.5", "bibheditha", dict(root="bhid", affix="liṭ", given=["pit"]),
     (), None),
    ("1.2.6", "babhūva", dict(root="bhū", affix="liṭ", ending="atus"),
     ("kit",), "1.2.6"),
    ("1.2.6", "babhūvitha", dict(root="bhū", affix="liṭ", given=["pit"]),
     ("kit",), "1.2.6"),
    ("1.2.6", "samīdhe", dict(root="indh", affix="liṭ", ending="atus"),
     ("kit",), "1.2.6"),
    ("1.2.7", "mṛḍitvā", dict(root="mṛḍ", affix="ktvā", given=["seṭ"]),
     ("kit",), "1.2.7"),
    ("1.2.7", "uṣitvā", dict(root="vas", affix="ktvā", given=["seṭ"]),
     ("kit",), "1.2.7"),
    ("1.2.8", "gṛhītvā", dict(root="grah", affix="ktvā", given=["seṭ"]),
     ("kit",), "1.2.8"),
    ("1.2.8", "jighṛkṣati", dict(root="grah", affix="san"), ("kit",), "1.2.8"),
    ("1.2.8", "suṣupsati", dict(root="svap", affix="san"), ("kit",), "1.2.8"),
    ("1.2.9", "cicīṣati", dict(root="ci", affix="san"), ("kit",), "1.2.9"),
    ("1.2.9", "tuṣṭūṣati", dict(root="stu", affix="san"), ("kit",), "1.2.9"),
    ("1.2.9", "cikīrṣati", dict(root="kṛ", affix="san"), ("kit",), "1.2.9"),
    ("1.2.9", "pipāsati", dict(root="pā", affix="san"), (), None),
    ("1.2.9", "tiṣṭhāsati", dict(root="sthā", affix="san"), (), None),
    ("1.2.9", "śiśayiṣate", dict(root="śī", affix="san", given=["seṭ"]),
     (), None),
    ("1.2.10", "bibhitsati", dict(root="bhid", affix="san"), ("kit",), "1.2.10"),
    ("1.2.10", "bubhutsate", dict(root="budh", affix="san"), ("kit",), "1.2.10"),
    ("1.2.10", "yiyakṣate", dict(root="yaj", affix="san"), (), None),
    ("1.2.10", "vivartiṣate", dict(root="vṛt", affix="san", given=["seṭ"]),
     (), None),
    ("1.2.11", "bhitsīṣṭa",
     dict(root="bhid", affix="liṅ", given=["ātmanepada"]), ("kit",), "1.2.11"),
    ("1.2.11", "abuddha",
     dict(root="budh", affix="sic", given=["ātmanepada"]), ("kit",), "1.2.11"),
    ("1.2.11", "yakṣīṣṭa",
     dict(root="yaj", affix="liṅ", given=["ātmanepada"]), (), None),
    ("1.2.11", "ceṣīṣṭa",
     dict(root="ci", affix="liṅ", given=["ātmanepada"]), (), None),
    ("1.2.11", "asrākṣīt", dict(root="sṛj", affix="sic"), (), None),
    ("1.2.12", "kṛṣīṣṭa",
     dict(root="kṛ", affix="liṅ", given=["ātmanepada"]), ("kit",), "1.2.12"),
    ("1.2.12", "ahṛta",
     dict(root="hṛ", affix="sic", given=["ātmanepada"]), ("kit",), "1.2.12"),
    ("1.2.12", "variṣīṣṭa",
     dict(root="vṛ", affix="liṅ", given=["ātmanepada", "seṭ"]), (), None),
    ("1.2.14", "āhata",
     dict(root="han", affix="sic", given=["ātmanepada"]), ("kit",), "1.2.14"),
    ("1.2.15", "udāyata",
     dict(root="yam", affix="sic", sense="gandhana", given=["ātmanepada"]),
     ("kit",), "1.2.15"),
    ("1.2.15", "udāyaṃsta pādam",
     dict(root="yam", affix="sic", given=["ātmanepada"]), (), None),
    ("1.2.17", "upāsthita",
     dict(root="sthā", affix="sic", given=["ātmanepada"]), ("kit",), "1.2.17"),
    ("1.2.17", "adita",
     dict(root="ḍudāñ", affix="sic", given=["ātmanepada"]), ("kit",), "1.2.17"),
    ("1.2.17", "adhita",
     dict(root="ḍudhāñ", affix="sic", given=["ātmanepada"]), ("kit",), "1.2.17"),

    # 1.2.18 – 1.2.26, and here it is denied
    ("1.2.18", "devitvā", dict(root="div", affix="ktvā", given=["seṭ"]),
     (), "1.2.18"),
    ("1.2.18", "vartitvā", dict(root="vṛt", affix="ktvā", given=["seṭ"]),
     (), "1.2.18"),
    ("1.2.18", "kṛtvā", dict(root="kṛ", affix="ktvā"), ("kit",), "1.3.8"),
    ("1.2.18", "hṛtvā", dict(root="hṛ", affix="ktvā"), ("kit",), "1.3.8"),
    ("1.2.19", "śayitaḥ", dict(root="śī", affix="niṣṭhā", given=["seṭ"]),
     (), "1.2.19"),
    ("1.2.19", "pradharṣitaḥ",
     dict(root="dhṛṣ", affix="niṣṭhā", given=["seṭ"]), (), "1.2.19"),
    ("1.2.19", "svinnaḥ", dict(root="svid", affix="niṣṭhā"), ("kit",), "1.3.8"),
    ("1.2.20", "marṣitaḥ",
     dict(root="mṛṣ", affix="niṣṭhā", sense="titikṣā", given=["seṭ"]),
     (), "1.2.20"),
    ("1.2.22", "pavitaḥ", dict(root="pū", affix="niṣṭhā", given=["seṭ"]),
     (), "1.2.22"),
]

#: Marked वा or विभाषा — both readings stand.
OPTIONAL = [
    ("1.2.3", "prorṇuvitā / prorṇavitā",
     dict(root="ūrṇu", affix="tṛc", given=["seṭ"])),
    ("1.2.13", "saṃgaṃsīṣṭa / saṃgasīṣṭa",
     dict(root="gam", affix="liṅ", given=["ātmanepada"])),
    ("1.2.16", "upāyata / upāyaṃsta kanyām",
     dict(root="yam", affix="sic", sense="upayamana", given=["ātmanepada"])),
    ("1.2.21", "dyutitam / dyotitam",
     dict(root="dyut", affix="niṣṭhā", sense="bhāva-ādikarman",
          given=["seṭ"])),
    ("1.2.23", "grathitvā / granthitvā",
     dict(root="granth", affix="ktvā", given=["seṭ"])),
    ("1.2.24", "vacitvā / vañcitvā",
     dict(root="vañc", affix="ktvā", given=["seṭ"])),
    ("1.2.25", "tṛṣitvā / tarṣitvā",
     dict(root="tṛṣ", affix="ktvā", given=["seṭ"])),
    ("1.2.26", "dyutitvā / dyotitvā",
     dict(root="dyut", affix="ktvā", given=["seṭ"])),
    ("1.2.26", "lilikhiṣati / lilekhiṣati",
     dict(root="likh", affix="san", given=["seṭ"])),
]


class WorkedForms(unittest.TestCase):
    def test_each_worked_form_comes_out_as_the_kasika_says(self):
        for sutra, form, use, expected, by in WORKED:
            with self.subTest(sutra=sutra, form=form):
                verdict = behaves_as(**use)
                self.assertEqual(verdict.behaves, expected,
                                 f"{sutra} {form}: {verdict.by} — {verdict.why}")
                if by is not None:
                    self.assertIn(by, verdict.by, f"{sutra} {form}")

    def test_every_optional_rule_offers_both(self):
        for sutra, form, use in OPTIONAL:
            with self.subTest(sutra=sutra, form=form):
                verdict = behaves_as(**use)
                self.assertTrue(verdict.optional, f"{sutra} {form}")
                self.assertIn(sutra, verdict.by, form)

    def test_the_table_covers_the_block(self):
        tested = {row[0] for row in WORKED} | {row[0] for row in OPTIONAL}
        untested = [f"1.2.{n}" for n in range(1, 27) if f"1.2.{n}" not in tested]
        # 1.2.6's vārttika and 1.2.7's second reason are covered elsewhere in
        # this file; these five have no worked form of their own here.
        self.assertEqual(untested, [])


class Shapes(unittest.TestCase):
    """
    The predicates the block is built on, against the commentary's own pairs.

    Every one of these is a pratyāhāra applied to a position. A predicate that
    is too wide passes its example and fails its counter-example, so the pairs
    are what makes them checkable at all.
    """

    def test_asamyoganta_1_2_5(self):
        for root in ("bhid", "chid", "yaj", "ci"):
            self.assertTrue(formation.is_asamyoganta(root), root)
        for root in ("srans", "dhvans"):
            self.assertFalse(formation.is_asamyoganta(root), root)

    def test_the_corpus_writes_those_two_roots_with_a_plain_n(self):
        """
        The counter-examples only work if the roots are found. This dhātupāṭha
        writes स्रंसु as `sransu̐`, the same convention that writes वञ्चु as
        `vancu̐`, and the anusvāra spelling has to reach the same answer.
        """
        entries = load_dhatupatha()
        self.assertEqual(entries["01.0857"].upadesa, "sransu̐")
        self.assertEqual(entries["01.0858"].upadesa, "dhvansu̐")
        self.assertFalse(formation.is_asamyoganta("sraṃs"))

    def test_ik_final_1_2_9(self):
        for root in ("ci", "stu", "kṛ"):
            self.assertTrue(formation.ends_in(root, "iK"), root)
        for root in ("pā", "sthā"):
            self.assertFalse(formation.ends_in(root, "iK"), root)

    def test_ik_then_consonant_1_2_10(self):
        """
        समीपवचनोऽन्तशब्दः — अन्त means 'near'. भिद् and बुध् have an इक् before
        their final; यज् has अ, which is not one.
        """
        for root in ("bhid", "budh"):
            self.assertTrue(formation.ik_before_final_consonant(root), root)
        self.assertFalse(formation.ik_before_final_consonant("yaj"))

    def test_the_shape_conditions_of_1_2_23_and_1_2_26(self):
        self.assertTrue(formation.penult_is("granth", "n"))
        self.assertFalse(formation.penult_is("reph", "n"))
        for root in ("dyut", "likh"):
            self.assertTrue(formation.ends_in(root, "raL"), root)
            self.assertTrue(formation.penult_is(root, "u", "i"), root)
        self.assertFalse(formation.ends_in("div", "raL"))
        self.assertFalse(formation.penult_is("vṛt", "u", "i"))

    def test_jhaladi_turns_on_the_it_augment_alone(self):
        """
        चिचीषति and शिशयिषते differ in nothing but the इट्. सन् begins with स्,
        and under सेट् it begins with इ — one condition, both of the Kāśikā's
        forms.
        """
        self.assertTrue(Formation("ci", "san").jhaladi)
        self.assertFalse(Formation("śī", "san", given=("seṭ",)).jhaladi)


class ReadRatherThanListed(unittest.TestCase):
    def test_kutadi_is_a_run_between_the_two_ends_the_kasika_names(self):
        """कुट कौटिल्ये इत्येतदारभ्य यावत् कुङ् शब्दे."""
        entries = load_dhatupatha()
        self.assertEqual(entries["06.0093"].upadesa, "kuṭa̐")
        self.assertEqual(entries["06.0093"].artha, "kOwilye")
        self.assertEqual(entries["06.0136"].upadesa, "kuṅ")
        self.assertEqual(entries["06.0136"].artha, "Sabde")

        gana = kutadi()
        self.assertEqual(gana[0], "kuṭ")
        self.assertEqual(gana[-1], "ku")
        self.assertGreater(len(gana), 40)

    def test_a_root_outside_the_run_is_outside_the_rule(self):
        """लिख् is 06.0092, one entry before कुट, and gets nothing."""
        self.assertNotIn("likh", kutadi())
        self.assertEqual(
            behaves_as("likh", "tṛc", given=["seṭ"]).behaves, ()
        )

    def test_the_affix_marks_come_from_the_it_rules_already_codified(self):
        """
        क्त्वा and the निष्ठा pair are kit by 1.3.8 before this block says
        anything, and तिप् is पित् by 1.3.3. Nothing here lists them.
        """
        self.assertEqual(already(Formation("x", "ktvā")), ("k",))
        self.assertEqual(already(Formation("x", "niṣṭhā")), ("k",))
        self.assertTrue(Formation("x", "sārvadhātuka", ending="tip").pit)
        self.assertFalse(Formation("x", "sārvadhātuka", ending="tas").pit)
        self.assertFalse(Formation("x", "sārvadhātuka", ending="jhi").pit)

    def test_1_2_17_takes_its_six_roots_from_1_1_20(self):
        """घु is दाधा घ्वदाप्, settled long before this pāda was reached."""
        named = provisions_for("1.2.17")[0].roots
        for root in ghu_roots():
            self.assertIn(root, named, root)
        self.assertIn("sthā", named)
        # दाप् and दैप् are excluded by 1.1.20 itself and must not creep in.
        self.assertNotIn("dāp", [root_key(r) for r in named])

    def test_no_provision_names_a_root_the_dhatupatha_does_not_have(self):
        unknown = sorted({
            root for provision in PROVISIONS for root in provision.roots
            if root != "gāṅ" and not entries_for(root)
        })
        self.assertEqual(unknown, [])


class Precedence(unittest.TestCase):
    """
    1.2.18's prohibition is drawn forward past 1.2.7 and 1.2.8 —
    तस्यायं पुरस्तादपकर्षः — so it does not reach what they settled.
    """

    def test_the_seven_roots_of_1_2_7_keep_their_kit_though_set(self):
        for root in ("mṛḍ", "mṛd", "gudh", "kuṣ", "kliś", "vad", "vas"):
            verdict = behaves_as(root, "ktvā", given=["seṭ"])
            self.assertEqual(verdict.behaves, ("kit",), root)
            self.assertIn("1.2.7", verdict.by, root)

    def test_the_six_of_1_2_8_likewise(self):
        for root in ("rud", "vid", "muṣ", "grah", "svap", "prach"):
            verdict = behaves_as(root, "ktvā", given=["seṭ"])
            self.assertEqual(verdict.behaves, ("kit",), root)
            self.assertIn("1.2.8", verdict.by, root)

    def test_an_ordinary_set_ktva_loses_it(self):
        """
        Which is what makes the two exemptions above mean something. लिख् is
        not on this list though it is a seṭ क्त्वा: it satisfies 1.2.26 and so
        keeps the kit-ness optionally — लिखित्वा, लेखित्वा — which is the
        Kāśikā's own pair.
        """
        for root in ("div", "vṛt", "eṣ"):
            self.assertEqual(
                behaves_as(root, "ktvā", given=["seṭ"]).behaves, (), root
            )

    def test_three_of_1_2_7s_roots_would_have_been_optional_by_1_2_26(self):
        """
        गुध-कुष-क्लिशीनां तु … विकल्पे प्राप्ते नित्यार्थं वचनम्. All three
        satisfy 1.2.26's three shape conditions, so being named earlier is
        what makes their kit-ness invariable rather than optional.
        """
        for root in ("gudh", "kuṣ", "kliś"):
            self.assertTrue(formation.ends_in(root, "raL"), root)
            self.assertTrue(formation.penult_is(root, "u", "i"), root)
            self.assertTrue(formation.begins_with(root_key(root), "haL"), root)
            self.assertFalse(behaves_as(root, "ktvā", given=["seṭ"]).optional)

    def test_and_so_would_three_of_1_2_8s(self):
        """रुद-विद-मुषीणां … विकल्पे प्राप्ते नित्यार्थं ग्रहणम्."""
        for root in ("rud", "vid", "muṣ"):
            self.assertTrue(formation.ends_in(root, "raL"), root)
            self.assertTrue(formation.penult_is(root, "u", "i"), root)
            self.assertFalse(behaves_as(root, "ktvā", given=["seṭ"]).optional)

    def test_a_form_can_be_ngit_and_have_its_kit_denied_at_once(self):
        """
        The two marks are separate and are settled separately. A seṭ क्त्वा
        after a कुटादि root is made ṅit by 1.2.1 while 1.2.18 withdraws the
        kit-ness it had by 1.3.8 — neither answer cancels the other. कड् is
        the root to try it on rather than कुट्, since कुट् also satisfies
        1.2.26 and would keep the kit-ness optionally.
        """
        verdict = behaves_as("kaḍ", "ktvā", given=["seṭ"])
        self.assertIn("ṅit", verdict.behaves)
        self.assertNotIn("kit", verdict.behaves)
        self.assertIn("1.2.1", verdict.by)
        self.assertIn("1.2.18", verdict.by)


class Transparency(unittest.TestCase):
    def test_a_rule_that_nearly_fired_is_reported(self):
        wanting = dict(near_misses(Formation("yam", "sic", sense="gandhana")))
        self.assertIn("1.2.15", wanting)
        self.assertEqual(wanting["1.2.15"], ("ātmanepada not stated",))

    def test_and_disappears_once_the_fact_is_supplied(self):
        form = Formation("yam", "sic", sense="gandhana", given=("ātmanepada",))
        self.assertNotIn("1.2.15", dict(near_misses(form)))
        self.assertIn("1.2.15", resolve(form).by)

    def test_the_verdict_reports_what_the_affix_already_carried(self):
        verdict = behaves_as("div", "ktvā", given=["seṭ"])
        self.assertEqual(verdict.already_marked, ("k",))
        self.assertEqual(verdict.behaves, ())
        self.assertIn("1.2.18", verdict.blocked)


class Registration(unittest.TestCase):
    def test_1_2_1_to_1_2_26_are_all_codified(self):
        missing = [f"1.2.{n}" for n in range(1, 27) if not REGISTRY.has(f"1.2.{n}")]
        self.assertEqual(missing, [])

    def test_each_record_carries_the_conditions_it_tests(self):
        for number in range(1, 27):
            sutra = f"1.2.{number}"
            line = REGISTRY.get(sutra).codification
            for provision in provisions_for(sutra):
                self.assertIn(provision.describe(), line, sutra)

    def test_the_open_question_about_thal_is_recorded(self):
        """
        बिभेदिथ shows थल् counts as पित्, and nothing in its spelling says so.
        3.4.82 is not codified, so where that पित्त्व comes from is unsettled
        and the record has to say it rather than quietly taking it as input.
        """
        notes = REGISTRY.get("1.2.5").notes
        self.assertIn("OPEN", notes)
        self.assertIn("बिभेदिथ", notes)
        self.assertIn("3.4.82", notes)

    def test_the_anuvrtti_of_akit_runs_from_1_2_18(self):
        """
        The corpus records न and सेट् as carried from 1.2.18 through the
        denials, which is the same window the codification uses.
        """
        from src.astadhyayi.sources import facts

        for number in range(19, 23):
            carried = {item.from_sutra for item in facts(f"1.2.{number}").anuvrtti}
            self.assertIn("1.2.18", carried, f"1.2.{number}")

    def test_every_denial_yields_only_where_the_kasika_says(self):
        """
        Only 1.2.18 is drawn forward, and only past 1.2.7 and 1.2.8. If a
        later denial silently yielded too, forms it should deny would keep
        their kit-ness and nothing would flag it.
        """
        yielding = {
            p.sutra: p.yields_to for p in PROVISIONS if p.yields_to
        }
        self.assertEqual(yielding, {"1.2.18": ("1.2.7", "1.2.8")})


if __name__ == "__main__":
    unittest.main()
