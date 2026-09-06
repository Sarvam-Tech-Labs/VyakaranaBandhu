# -*- coding: utf-8 -*-
"""
3.1.69 to 3.1.95 — the class-marker, and the headings that follow it.

Expectations are the Kāśikā's worked forms and its *kim*
counter-examples. Two things here are held that running a rule cannot
show: a restriction this pāda places on a rule two pādas back, and a
class-ambiguity the table must report rather than resolve.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.vikarana import (
    BHRASADI, BY_CLASS, DHINVADI, DUHADI, KARMAVAT_EFFECTS, KRTYA_THROUGH,
    STAMBHVADI, dhatoh_heading, in_the_dhatoh_section,
    in_the_krtya_section, karmavat, krt, krtya, upapada, vedic_latitude,
    vikarana,
)


class TheClassesAreReadFromTheCorpus(unittest.TestCase):
    """
    Six of the ten dhātupāṭha classes decide their marker here, and the
    class is asked of the corpus — never listed. `verbal_gana` was
    written for 2.4.72's अदादि and reused for 3.1.25's चुरादि; this run
    brings it to nine of the ten.
    """

    def test_each_class_takes_the_marker_its_sutra_gives(self):
        from src.astadhyayi.pada import verbal_gana

        witnesses = {"04": "div", "05": "ṣuñ", "06": "tud",
                     "07": "rudh", "08": "tan", "09": "ḍukrīñ"}
        for code, gives, sutra in BY_CLASS:
            root = witnesses[code]
            with self.subTest(gana=code, root=root):
                self.assertIn(code, verbal_gana(root),
                              "the witness must really be of that class")
                answer = vikarana(root, gana=code)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_the_six_markers_are_all_different(self):
        """
        A table that gave two classes the same marker would still pass
        a test that only checked each lookup succeeded.
        """
        self.assertEqual(len({g for _c, g, _s in BY_CLASS}), 6)

    def test_a_root_of_no_named_class_keeps_sap(self):
        """
        Everything here is an अपवाद of 3.1.68 कर्तरि शप्, so what none
        of them reaches keeps शप् — and is told so by name.
        """
        answer = vikarana("bhū", gana="01")
        self.assertEqual(answer.by, "")
        self.assertIn("3.1.68", answer.why)


class AClassAmbiguityIsReportedNotResolved(unittest.TestCase):
    """
    The dhātupāṭha reads one spelling in several places, in different
    senses, and the marker follows the reading. रुध् is read in the
    fourth class and the seventh and takes a different marker in each,
    so answering from the root alone would be the table choosing on
    Pāṇini's behalf.
    """

    def test_rudh_really_is_read_in_two_classes(self):
        from src.astadhyayi.pada import verbal_gana

        self.assertTrue({"04", "07"} <= verbal_gana("rudh"),
                        "the ambiguity is real, not contrived")

    def test_asked_without_a_class_it_says_so(self):
        answer = vikarana("rudh")
        self.assertEqual(answer.by, "", "no rule acted, so none is named")
        self.assertIn("more than one class", answer.why)

    def test_asked_with_one_it_answers_from_that_one(self):
        self.assertEqual(vikarana("rudh", gana="07").gives, "śnam")
        self.assertEqual(vikarana("rudh", gana="04").gives, "śyan")

    def test_a_class_the_root_is_not_read_in_is_refused(self):
        answer = vikarana("rudh", gana="09")
        self.assertEqual(answer.by, "")
        self.assertIn("not read in class", answer.why)

    def test_an_unambiguous_root_needs_no_class(self):
        """तुद् is read in the sixth only, so nothing has to be said."""
        self.assertEqual(vikarana("tud").by, "3.1.77")


class TheRulesThatNameRootsOutright(unittest.TestCase):

    def test_each_answers_for_its_own_example(self):
        cases = (
            ("3.1.70", "śyan", dict(root="bhramu")),
            ("3.1.71", "śyan", dict(root="yas")),
            ("3.1.72", "śyan", dict(root="yas", upasarga="sam")),
            ("3.1.74", "śnu", dict(root="śru")),
            ("3.1.75", "śnu", dict(root="akṣ")),
            ("3.1.76", "śnu", dict(root="takṣ", sense="tanūkaraṇa")),
            ("3.1.79", "u", dict(root="kṛ")),
            ("3.1.80", "u", dict(root="dhinvi")),
            ("3.1.82", "śnā", dict(root="stanbhu")),
        )
        for sutra, gives, where in cases:
            with self.subTest(sutra=sutra, **where):
                answer = vikarana(**where)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_every_named_root_of_a_list_rule_is_reached(self):
        for group, sutra in ((BHRASADI, "3.1.70"), (STAMBHVADI, "3.1.82"),
                             (DHINVADI, "3.1.80")):
            for root in group:
                with self.subTest(sutra=sutra, root=root):
                    self.assertEqual(vikarana(root).by, sutra)

    def test_3_1_71_needs_no_preverb_and_3_1_72_needs_one(self):
        """अनुपसर्गादिति किम्? आयस्यति — with any preverb but सम्."""
        self.assertEqual(vikarana("yas").by, "3.1.71")
        self.assertEqual(vikarana("yas", upasarga="sam").by, "3.1.72")
        with_other = vikarana("yas", upasarga="ā")
        self.assertEqual(with_other.by, "3.1.69",
                         "the option is gone and 3.1.69 is obligatory")

    def test_3_1_76_needs_its_sense(self):
        """तनूकरण इति किम्? संतक्षति वाग्भिः."""
        self.assertEqual(
            vikarana("takṣ", sense="tanūkaraṇa").by, "3.1.76")
        self.assertEqual(vikarana("takṣ").by, "")

    def test_the_optional_rules_are_marked_and_the_rest_are_not(self):
        optional = {"3.1.70", "3.1.71", "3.1.72", "3.1.75", "3.1.76"}
        for where in (dict(root="bhramu"), dict(root="akṣ"),
                      dict(root="takṣ", sense="tanūkaraṇa"),
                      dict(root="śru"), dict(root="stanbhu"),
                      dict(root="tud")):
            answer = vikarana(**where)
            with self.subTest(sutra=answer.by):
                self.assertEqual(answer.optional,
                                 answer.by in optional)

    def test_two_rules_do_a_second_thing_besides_adding_a_marker(self):
        """
        3.1.74 changes श्रु's shape and 3.1.80 makes the final अ. Both
        are stated in the same sūtra as the marker, तत्संनियोगेन, so
        both are carried on the answer.
        """
        self.assertTrue(vikarana("śru").also)
        self.assertTrue(vikarana("dhinvi").also)
        self.assertFalse(vikarana("tud").also)


class WhatThreePointOneSeventyNineRestricts(unittest.TestCase):
    """
    कृ is in तनादि already, so naming it adds no marker:
    तनादिपाठादेव उप्रत्यये सिद्धे करोतेरुपादानं नियमार्थम्, अन्यत्
    तनादिकार्यं मा भूत्. The rule it holds off is 2.4.79, codified two
    pādas earlier — so the claim can be checked on that rule and not
    only asserted here.
    """

    def test_kr_is_already_of_the_eighth_class(self):
        from src.astadhyayi.pada import verbal_gana

        self.assertIn("08", verbal_gana("kṛ"),
                      "if कृ were not in तनादि the naming would be a "
                      "grant and the नियम reading would collapse")

    def test_and_takes_the_same_marker_the_class_takes(self):
        by_class = next(g for c, g, _s in BY_CLASS if c == "08")
        self.assertEqual(vikarana("kṛ").gives, by_class)

    def test_the_rule_it_holds_off_is_real_and_reaches_its_class(self):
        """
        2.4.79 तनादिभ्यस्तथासोः optionally elides सिच् after a तनादि
        root. That it fires for तन् is what makes 3.1.79's restriction
        of it mean something.
        """
        from src.astadhyayi.pratyaya_luk import verbal_luk

        answer = verbal_luk(affix="sic", gana="tanādi", before="ta")
        self.assertEqual(answer.by, "2.4.79")
        self.assertTrue(answer.elided)


class TheVedicLatitude(unittest.TestCase):

    def test_3_1_85_is_a_licence_with_no_output(self):
        """
        व्यत्ययो बहुलम् — nothing here can be derived, only recognised,
        so the answer names the rule and gives no affix.
        """
        answer = vedic_latitude()
        self.assertEqual(answer.by, "3.1.85")
        self.assertEqual(answer.gives, "")

    def test_3_1_86_does_give_one(self):
        answer = vedic_latitude(lakara="liṅ")
        self.assertEqual(answer.by, "3.1.86")
        self.assertEqual(answer.gives, "aṅ")


class KarmavadbhavaIsATransfer(unittest.TestCase):

    def test_3_1_87_names_all_four_effects(self):
        """
        यगात्मनेपदचिण्चिण्वद्भावाः प्रयोजनम् — the vṛtti names them
        rather than leaving "treated as an object" to be worked out, so
        the answer carries them.
        """
        answer = karmavat()
        self.assertEqual(answer.by, "3.1.87")
        self.assertEqual(answer.effects, KARMAVAT_EFFECTS)
        self.assertEqual(len(KARMAVAT_EFFECTS), 4)

    def test_three_of_the_four_are_rules_already_codified(self):
        """
        This is where 3.1.62 to 3.1.67 are put to work, so those rules
        must be reachable for the transfer to mean anything.
        """
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.1.66", "3.1.67"):
            self.assertTrue(REGISTRY.has(sutra))

    def test_it_needs_the_actions_to_be_alike(self):
        self.assertEqual(karmavat(tulyakriya=False).by, "")

    def test_3_1_88_grants_despite_its_eva(self):
        """
        पूर्वेणाप्राप्तः कर्मवद्भावो विधीयते — 3.1.87 could not have
        reached तप्, so this adds rather than narrows.
        """
        self.assertEqual(karmavat("tap", object_of_tap=True).by, "3.1.88")
        self.assertEqual(karmavat("tap").by, "")

    def test_3_1_89_refuses_two_of_the_four_and_keeps_two(self):
        for root in DUHADI:
            with self.subTest(root=root):
                answer = karmavat(root)
                self.assertEqual(answer.by, "3.1.89")
                self.assertEqual(answer.refused, ("yak", "ciṇ"))
                self.assertEqual(answer.effects,
                                 ("ātmanepada", "ciṇvadbhāva"))
                self.assertEqual(
                    set(answer.refused) | set(answer.effects),
                    set(KARMAVAT_EFFECTS),
                    "refused and kept must together be the four")

    def test_3_1_90_displaces_two_effects_rather_than_refusing_them(self):
        answer = karmavat("kuṣ", pracam=True)
        self.assertEqual(answer.by, "3.1.90")
        self.assertEqual(answer.effects, ("śyan", "parasmaipada"))

    def test_and_it_is_a_vyavasthitavibhasa(self):
        """
        तेन लिट्लिङोः स्यादिविषये च न भवतः — settled by where one is,
        not chosen. चुकुषे, कोषिषीष्ट, कोषिष्यते keep the middle.
        """
        for lakara in ("liṭ", "liṅ", "lṛṭ", "lṛṅ"):
            with self.subTest(lakara=lakara):
                self.assertEqual(
                    karmavat("kuṣ", pracam=True, lakara=lakara).by, "")

    def test_without_the_easterners_view_it_does_not_apply(self):
        self.assertNotEqual(karmavat("kuṣ").by, "3.1.90")


class TheThreeHeadingsAndTheFourth(unittest.TestCase):

    def test_3_1_91_runs_to_the_end_of_adhyaya_3(self):
        """आ तृतीयाध्यायपरिसमाप्तेः."""
        answer = dhatoh_heading()
        self.assertEqual(answer.by, "3.1.91")
        self.assertTrue(in_the_dhatoh_section("3.2.1"))
        self.assertTrue(in_the_dhatoh_section("3.4.117"))
        self.assertFalse(in_the_dhatoh_section("3.1.91"),
                         "a heading is not inside its own range")
        self.assertFalse(in_the_dhatoh_section("4.1.1"))

    def test_3_1_92_needs_the_locative(self):
        self.assertEqual(upapada(in_locative=True).by, "3.1.92")
        self.assertEqual(upapada().by, "")

    def test_3_1_93_names_everything_but_a_tin(self):
        self.assertEqual(krt().by, "3.1.93")
        self.assertEqual(krt(is_tin=True).by, "")

    def test_3_1_95_stops_before_the_rule_it_names(self):
        """
        प्राक् एतस्मात् ण्वुल्संशब्दनात् — the range is given by naming
        3.1.133, which is therefore the first rule OUTSIDE it.
        """
        self.assertEqual(krtya().by, "3.1.95")
        self.assertEqual(KRTYA_THROUGH, "3.1.132")
        self.assertTrue(in_the_krtya_section("3.1.96"))
        self.assertTrue(in_the_krtya_section("3.1.132"))
        self.assertFalse(in_the_krtya_section("3.1.133"))
        self.assertEqual(krtya(sutra_id="3.1.133").by, "")

    def test_the_two_rules_that_use_the_name_are_codified(self):
        """
        कृत्यप्रदेशाः — 2.1.33 and 2.3.71 invoke the name, and both were
        codified before the heading that confers it. This heading is
        what they were waiting on.
        """
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("2.1.33", "2.3.71"):
            self.assertTrue(REGISTRY.has(sutra))


if __name__ == "__main__":
    unittest.main()
