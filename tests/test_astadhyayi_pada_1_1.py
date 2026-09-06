# -*- coding: utf-8 -*-
"""
Tests for the rest of 1.1 — 1.1.28 to 1.1.48, and 1.1.56 to 1.1.59.

Three decision procedures, and what makes each one a test rather than a
restatement is the ORDER its branches are tried in. Each block has at least one
sūtra that can never fire if the order is wrong:

  1.1.28  relieves a prohibition 1.1.29 has not made yet
  1.1.42  must be tried before 1.1.43, or a neuter śi loses a name it has
  1.1.59  re-admits what 1.1.58 excluded from what 1.1.57 allowed

Those three are the tests that matter here. The rest are the commentaries'
worked forms.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import samjna as S
from src.astadhyayi.adesa import (
    AgamaSite,
    agama_site,
    antaratama,
    hrasva_of_ec,
    insert_agama,
    samprasarana,
)
from src.astadhyayi.avyaya import avyaya, is_avyaya
from src.astadhyayi.corpus import gana_for
from src.astadhyayi.samjna import Samasa, sarvanaman
from src.astadhyayi.sivasutra import resolve
from src.astadhyayi.sthanivat import EXCLUDED, sthanivat


class SarvanamanQualified(unittest.TestCase):
    """1.1.28 to 1.1.36."""

    def test_the_three_compounds_that_withdraw_the_name(self):
        for samasa, by in [(Samasa.BAHUVRIHI, "1.1.29"),
                           (Samasa.TRTIYA, "1.1.30"),
                           (Samasa.DVANDVA, "1.1.31")]:
            found = sarvanaman("sarva", samasa=samasa)
            self.assertFalse(found.applies, samasa)
            self.assertEqual(found.by, by, samasa)

    def test_1_1_28_must_be_tried_before_1_1_29(self):
        """
        A directional bahuvrīhi IS a bahuvrīhi. Test 1.1.29 first and 1.1.28
        can never fire, and उत्तरपूर्वस्यै becomes impossible.
        """
        found = sarvanaman("pūrva", samasa=Samasa.DIK_BAHUVRIHI)
        self.assertEqual(found.by, "1.1.28")
        self.assertTrue(found.applies)
        self.assertTrue(found.optional)

    def test_1_1_32_relaxes_1_1_31_only_before_jas(self):
        without = sarvanaman("katara", samasa=Samasa.DVANDVA)
        before = sarvanaman("katara", samasa=Samasa.DVANDVA, before_jas=True)
        self.assertEqual(without.by, "1.1.31")
        self.assertFalse(without.optional)
        self.assertEqual(before.by, "1.1.32")
        self.assertTrue(before.optional)

    def test_1_1_33_mostly_reaches_words_the_gana_does_not_hold(self):
        """
        Six of the seven have no claim to the name otherwise, which is what
        separates this sūtra from 1.1.34 to 1.1.36. नेम is the exception — it
        IS in sarvādi, so for it this sūtra relaxes a name 1.1.27 already gave,
        exactly as 1.1.34 does for पूर्व. An earlier version of this test
        asserted all seven were outside the gaṇa and was wrong.
        """
        outside = [w for w in S.PRATHAMADI if not S.is_sarvanaman(w)]
        inside = [w for w in S.PRATHAMADI if S.is_sarvanaman(w)]
        self.assertEqual(inside, ["nema"])
        self.assertEqual(len(outside), 5)
        for word in S.PRATHAMADI:
            found = sarvanaman(word, before_jas=True)
            self.assertEqual(found.by, "1.1.33", word)
            self.assertTrue(found.optional, word)

    def test_nema_has_the_name_unconditionally_when_jas_is_not_in_play(self):
        """Being in the gaṇa, it falls back on 1.1.27 like पूर्व does."""
        self.assertEqual(sarvanaman("nema").by, "1.1.27")
        self.assertEqual(sarvanaman("prathama").by, "")

    def test_1_1_33_taya_is_an_affix_not_a_word(self):
        """द्वितये beside द्वितयाः — the test is on the ending."""
        self.assertEqual(sarvanaman("dvitaya", before_jas=True).by, "1.1.33")
        self.assertEqual(sarvanaman("tritaya", before_jas=True).by, "1.1.33")

    def test_1_1_34_relaxes_a_name_the_gana_already_gave(self):
        """
        The seven ARE in sarvādi, so 1.1.27 grants the name outright and this
        makes it optional before jas. The Gaṇapāṭha annotates them with this
        sūtra, which is the evidence that they are meant to be in both places.
        """
        for word in S.PURVADI:
            self.assertTrue(S.is_sarvanaman(word), word)
            plain = sarvanaman(word)
            self.assertEqual(plain.by, "1.1.27", word)
            self.assertFalse(plain.optional, word)
            relaxed = sarvanaman(word, before_jas=True, vyavastha=True)
            self.assertEqual(relaxed.by, "1.1.34", word)
            self.assertTrue(relaxed.optional, word)

    def test_1_1_34_needs_both_semantic_conditions(self):
        """व्यवस्थायाम् and असंज्ञायाम् — placing a thing, and not a name."""
        self.assertEqual(
            sarvanaman("pūrva", before_jas=True, vyavastha=False).by, "1.1.27"
        )
        self.assertEqual(
            sarvanaman("pūrva", before_jas=True, vyavastha=True,
                       is_name=True).by,
            "1.1.27",
        )

    def test_1_1_35_sva(self):
        self.assertEqual(sarvanaman("sva", before_jas=True).by, "1.1.35")
        self.assertEqual(
            sarvanaman("sva", before_jas=True,
                       means_kin_or_wealth=True).by,
            "1.1.27",
        )

    def test_1_1_36_antara(self):
        self.assertEqual(
            sarvanaman("antara", before_jas=True,
                       bahiryoga_or_upasamvyana=True).by,
            "1.1.36",
        )
        self.assertEqual(sarvanaman("antara", before_jas=True).by, "1.1.27")

    def test_a_word_outside_the_gana_gets_nothing(self):
        found = sarvanaman("rāma")
        self.assertFalse(found.applies)
        self.assertEqual(found.by, "")


class Avyaya(unittest.TestCase):
    """1.1.37 to 1.1.41."""

    def test_svaradi_by_the_gana(self):
        self.assertEqual(avyaya("svar").by, "1.1.37")
        self.assertEqual(avyaya("prātar").by, "1.1.37")

    def test_both_ganas_are_akrti_so_absence_proves_nothing(self):
        """
        स्वरादि and चादि are open lists. A word in one is certainly avyaya; a
        word absent may still be, and the result says which case it is.
        """
        self.assertTrue(gana_for("1.1.37").open_ended)
        self.assertTrue(gana_for("1.4.57").open_ended)
        listed = avyaya("ca", nipata=True)
        self.assertTrue(listed.certain)
        unlisted = avyaya("kacit", nipata=True)
        self.assertFalse(unlisted.certain)
        self.assertEqual(unlisted.by, "1.1.37")

    def test_1_1_38_needs_the_defective_paradigm(self):
        """असर्वविभक्तिरिति किम्? औपगवः, औपगवौ, औपगवाः."""
        self.assertEqual(
            avyaya("tatra", taddhita_final=True, sarvavibhakti=False).by,
            "1.1.38",
        )
        self.assertIsNone(
            avyaya("aupagava", taddhita_final=True, sarvavibhakti=True)
        )

    def test_1_1_38_needs_the_taddhita(self):
        """तद्धितः इति किम्? एकः, द्वौ, बहवः."""
        self.assertIsNone(avyaya("eka", sarvavibhakti=False))

    def test_1_1_39_resolves_ec_rather_than_listing_it(self):
        for final in resolve("eC").sounds:
            self.assertEqual(
                avyaya("vak" + final, krt_final=True).by, "1.1.39", final
            )
        self.assertEqual(avyaya("svāduṃkāram", krt_final=True).by, "1.1.39")

    def test_1_1_39_reaches_no_other_final(self):
        self.assertIsNone(avyaya("kṛta", krt_final=True))

    def test_1_1_40_the_three_affixes(self):
        for affix in S.__dict__.get("KTVA", ()) or ("ktvā", "tosun", "kasun"):
            self.assertEqual(avyaya("x", krt_affix=affix).by, "1.1.40", affix)

    def test_1_1_41_avyayibhava(self):
        self.assertEqual(avyaya("upāgni", avyayibhava=True).by, "1.1.41")

    def test_nothing_is_avyaya_without_a_ground(self):
        self.assertFalse(is_avyaya("rāma"))
        self.assertFalse(is_avyaya("kṛtvā"))     # needs the affix named


class Sarvanamasthana(unittest.TestCase):
    """1.1.42 and 1.1.43."""

    def test_si_by_1_1_42(self):
        self.assertEqual(S.sarvanamasthana("śi").by, "1.1.42")

    def test_si_keeps_the_name_in_a_neuter(self):
        """
        नपुंसके न विधिर्न प्रतिषेधः, तेन जसः शेः सर्वनामस्थानसंज्ञा पूर्वेण
        भवत्येव. 1.1.43's exception is not a prohibition, so it cannot take
        away what 1.1.42 gave. Test suṬ first and this comes back empty.
        """
        found = S.sarvanamasthana("śi", napumsaka=True)
        self.assertIsNotNone(found)
        self.assertEqual(found.by, "1.1.42")

    def test_sut_by_1_1_43_outside_the_neuter(self):
        for affix in S.SUT:
            self.assertEqual(
                S.sarvanamasthana(affix).by, "1.1.43", affix
            )
            self.assertIsNone(
                S.sarvanamasthana(affix, napumsaka=True), affix
            )

    def test_sut_is_the_first_five_of_4_1_2(self):
        self.assertEqual(S.SUT, ("su", "au", "jas", "am", "auṭ"))

    def test_sutiti_kim_rajnah_pasya(self):
        """The sixth ending is outside the five."""
        self.assertIsNone(S.sarvanamasthana("ṅas"))


class Vibhasa(unittest.TestCase):
    """1.1.44 न वेति विभाषा."""

    def test_two_things_one_name(self):
        self.assertIs(S.vibhasa("na"), S.Vibhasa.PRATISEDHA)
        self.assertIs(S.vibhasa("vā"), S.Vibhasa.VIKALPA)
        self.assertIsNone(S.vibhasa("ca"))

    def test_it_is_the_name_every_optional_rule_so_far_reports(self):
        """
        1.1.28, 1.1.32 and 1.1.33 to 1.1.36 all say विभाषा, so every `optional`
        already returned by the sarvanāman decision is this saṃjñā at work.
        """
        optional = [
            sarvanaman("pūrva", samasa=Samasa.DIK_BAHUVRIHI),
            sarvanaman("katara", samasa=Samasa.DVANDVA, before_jas=True),
            sarvanaman("prathama", before_jas=True),
            sarvanaman("sva", before_jas=True),
        ]
        for found in optional:
            self.assertTrue(found.optional, found.by)
        self.assertIsNotNone(S.vibhasa("vā"))


class SamprasaranaAndPlacement(unittest.TestCase):
    """1.1.45 to 1.1.48."""

    def test_samprasarana_is_a_relation(self):
        """यज् gives इष्टम्, वप् उप्तम्, ग्रह् गृहीतम् — y to i, v to u, r to ṛ."""
        self.assertTrue(samprasarana("y", "i"))
        self.assertTrue(samprasarana("v", "u"))
        self.assertTrue(samprasarana("r", "ṛ"))
        self.assertTrue(samprasarana("l", "ḷ"))

    def test_both_classes_are_resolved_not_listed(self):
        for before in resolve("yaṆ").sounds:
            for after in resolve("iK").sounds:
                self.assertTrue(samprasarana(before, after))
        self.assertFalse(samprasarana("y", "a"))
        self.assertFalse(samprasarana("k", "i"))

    def test_agama_placement_by_its_marks(self):
        self.assertIs(agama_site(frozenset("ṭ")), AgamaSite.ADI)
        self.assertIs(agama_site(frozenset("k")), AgamaSite.ANTA)
        self.assertIs(agama_site(frozenset("m")), AgamaSite.AFTER_LAST_VOWEL)
        self.assertIsNone(agama_site(frozenset("ś")))

    def test_the_three_sites_are_distinct(self):
        self.assertEqual(insert_agama("lū", "X", AgamaSite.ADI), "Xlū")
        self.assertEqual(insert_agama("lū", "X", AgamaSite.ANTA), "lūX")
        self.assertEqual(
            insert_agama("vidh", "X", AgamaSite.AFTER_LAST_VOWEL), "viXdh"
        )

    def test_a_mit_augment_goes_after_the_last_vowel_not_the_last_sound(self):
        """That is the whole difference between 1.1.47 and 1.1.46's kit."""
        self.assertEqual(
            insert_agama("rudh", "na", AgamaSite.AFTER_LAST_VOWEL), "runadh"
        )
        self.assertEqual(
            insert_agama("rudh", "na", AgamaSite.ANTA), "rudhna"
        )

    def test_1_1_48_is_computed_by_1_1_50_and_not_tabulated(self):
        """रै gives अतिरि, नौ अतिनु, गो उपगु."""
        for vowel, expected in [("e", "i"), ("ai", "i"),
                                ("o", "u"), ("au", "u")]:
            self.assertEqual(hrasva_of_ec(vowel), expected, vowel)
            self.assertEqual(
                antaratama(vowel, list(resolve("iK").sounds)),
                (expected,),
                f"{vowel}: 1.1.50 must reach it unaided",
            )

    def test_1_1_48_reaches_only_the_diphthongs(self):
        """एच इति किम्? अतिखट्वः, अतिमालः."""
        for vowel in ("a", "ā", "i", "ī", "u", "ū", "ṛ"):
            self.assertIsNone(hrasva_of_ec(vowel), vowel)


class Sthanivadbhava(unittest.TestCase):
    """1.1.56 to 1.1.59."""

    THREE = dict(al_vidhi=True, sthanin_is_vowel=True,
                 caused_by_following=True, purva_vidhi=True)

    def test_the_general_grant(self):
        """भू replacing अस् is still a root for 3.1.91: भविता."""
        found = sthanivat(al_vidhi=False)
        self.assertTrue(found.applies)
        self.assertEqual(found.by, "1.1.56")

    def test_an_al_vidhi_is_shut_out_by_default(self):
        found = sthanivat(al_vidhi=True)
        self.assertFalse(found.applies)
        self.assertEqual(found.by, "1.1.56")

    def test_1_1_57_lets_a_vowel_substitute_back_in(self):
        found = sthanivat(**self.THREE)
        self.assertTrue(found.applies)
        self.assertEqual(found.by, "1.1.57")

    def test_all_three_of_1_1_57s_conditions_are_required(self):
        for drop in ("sthanin_is_vowel", "caused_by_following", "purva_vidhi"):
            conditions = dict(self.THREE)
            conditions[drop] = False
            found = sthanivat(**conditions)
            self.assertFalse(found.applies, drop)
            self.assertEqual(found.by, "1.1.56", drop)

    def test_1_1_58_excludes_ten_operations(self):
        self.assertEqual(len(EXCLUDED), 10)
        for operation in EXCLUDED:
            found = sthanivat(operation=operation, **self.THREE)
            self.assertFalse(found.applies, operation)
            self.assertEqual(found.by, "1.1.58", operation)

    def test_an_operation_not_in_the_list_still_gets_1_1_57(self):
        """
        This test was written with operation="vrddhi" — no macron — and it
        passed, but not for the reason it gave. The string matched nothing
        at all, so the rule fell through to 1.1.57 because it recognised
        no operation, rather than because वृद्धि is genuinely outside
        1.1.58's ten. Naming the operation from a closed vocabulary is what
        turned that up.
        """
        found = sthanivat(operation="vṛddhi", **self.THREE)
        self.assertTrue(found.applies)
        self.assertEqual(found.by, "1.1.57")

    def test_a_misspelt_operation_is_refused_rather_than_answered(self):
        """
        The defect this vocabulary exists for. `dirgha` for `dīrgha` used to
        return True by 1.1.57 — the opposite verdict, under a different
        sūtra — because nothing checked the string it was given.
        """
        from src.astadhyayi.operations import UnknownOperation

        with self.assertRaises(UnknownOperation):
            sthanivat(operation="dirgha", **self.THREE)
        with self.assertRaises(UnknownOperation):
            sthanivat(operation="nonsense", **self.THREE)

        # and the correctly spelled one still gives the other answer
        spelled = sthanivat(operation="dīrgha", **self.THREE)
        self.assertFalse(spelled.applies)
        self.assertEqual(spelled.by, "1.1.58")

    def test_1_1_59_must_be_tried_before_1_1_58(self):
        """
        1.1.58 excludes dvirvacana and 1.1.59 puts it back. Test them in
        numerical order and 1.1.59 can never fire, and पपतुः is underivable.
        """
        blocked = sthanivat(operation="dvirvacana", **self.THREE)
        self.assertEqual(blocked.by, "1.1.58")
        self.assertFalse(blocked.applies)

        restored = sthanivat(operation="dvirvacana",
                             dvirvacana_caused_by_vowel=True, **self.THREE)
        self.assertEqual(restored.by, "1.1.59")
        self.assertTrue(restored.applies)

    def test_1_1_59_alone_is_provisional(self):
        """रूपातिदेशश्चायं नियतकालः — it expires when the reduplication is done."""
        restored = sthanivat(operation="dvirvacana",
                             dvirvacana_caused_by_vowel=True, **self.THREE)
        self.assertTrue(restored.provisional)
        for other in (sthanivat(al_vidhi=False), sthanivat(**self.THREE)):
            self.assertFalse(other.provisional, other.by)

    def test_every_result_names_a_sutra(self):
        for conditions in [dict(al_vidhi=False), dict(al_vidhi=True),
                           self.THREE,
                           dict(operation="padānta", **self.THREE),
                           dict(operation="dvirvacana",
                                dvirvacana_caused_by_vowel=True)]:
            self.assertTrue(sthanivat(**conditions).by.startswith("1.1."))


class Tadantavidhi(unittest.TestCase):
    """1.1.72 येन विधिस्तदन्तस्य."""

    def test_a_qualifier_reaches_what_ends_in_it(self):
        """3.3.56 एरच् gives चयः and जयः from चि and जि."""
        from src.astadhyayi.grahana import tadantavidhi

        self.assertTrue(tadantavidhi("i", "ci"))
        self.assertTrue(tadantavidhi("i", "ji"))
        self.assertFalse(tadantavidhi("i", "ka"))

    def test_and_its_own_form_too(self):
        """स्वस्य च रूपस्य — read down from 1.1.68."""
        from src.astadhyayi.grahana import tadantavidhi

        self.assertTrue(tadantavidhi("i", "i"))

    def test_it_reaches_what_the_term_denotes_not_its_letters(self):
        """
        3.1.125 ओरावश्यके has a non-tapara उ, so 1.1.69 gives it ū as well and
        लू is reached. Comparing letters alone would miss it, and the first
        version of this codification did.
        """
        from src.astadhyayi.grahana import tadantavidhi

        self.assertTrue(tadantavidhi("u", "lū"))
        self.assertTrue(tadantavidhi("u", "lu"))

    def test_a_tapara_qualifier_narrows_it_again(self):
        """1.1.70 propagates through: उत् reaches लु and not लू."""
        from src.astadhyayi.grahana import tadantavidhi

        self.assertTrue(tadantavidhi("ut", "lu"))
        self.assertFalse(tadantavidhi("ut", "lū"))

    def test_katyayanas_exception(self):
        """
        समासप्रत्ययविधौ प्रतिषेधः — no extension in a rule about compounds or
        affixes, or 2.1.24 would compound कष्टं परमश्रितः and 4.1.99 would
        make सौत्रनाडिः.
        """
        from src.astadhyayi.grahana import tadantavidhi

        self.assertFalse(
            tadantavidhi("i", "ci", samasa_or_pratyaya_vidhi=True)
        )
        self.assertTrue(
            tadantavidhi("i", "i", samasa_or_pratyaya_vidhi=True),
            "its own form survives the exception",
        )

    def test_it_compares_sounds_and_not_characters(self):
        from src.astadhyayi.grahana import tadanta

        self.assertTrue(tadanta("bh", "labh"))
        self.assertFalse(tadanta("h", "labh"))


class Vrddha(unittest.TestCase):
    """1.1.73 to 1.1.75."""

    def test_1_1_73_asks_1_1_1_whether_the_first_vowel_is_a_vrddhi(self):
        from src.astadhyayi.rules.adhyaya_1_pada_1 import is_vrddhi

        for word in ("śālīya", "mālīya", "aupagavīya", "kāpaṭavīya"):
            found = S.vrddha(word)
            self.assertEqual(found.by, "1.1.73", word)
            self.assertTrue(is_vrddhi(S.first_vowel(word)), word)

    def test_1_1_73_wants_the_FIRST_vowel(self):
        """आदिरिति किम्? — a vṛddhi elsewhere does not count."""
        self.assertEqual(S.first_vowel("kṛtaudana"), "ṛ")
        self.assertIsNone(S.vrddha("kṛtaudana"))

    def test_1_1_73_is_optional_for_a_proper_name(self):
        """वा नामधेयस्य — देवदत्तीयाः beside दैवदत्ताः."""
        self.assertTrue(S.vrddha("śālīya", is_name=True).optional)
        self.assertFalse(S.vrddha("śālīya").optional)

    def test_1_1_74_is_the_tail_of_the_sarvadi_gana(self):
        tail = S.tyadadi()
        self.assertEqual(tail[0], "tyad")
        self.assertEqual(tail[-1], "kim")
        self.assertEqual(len(tail), 12)
        for word in tail:
            self.assertTrue(S.is_sarvanaman(word), word)

    def test_1_1_74_does_not_use_the_first_vowel_condition(self):
        """
        इह तु न संबध्यते — the anuvṛtti skips this sūtra and resumes at the
        next. So तद् and किम् are vṛddha though neither begins with a vṛddhi.
        """
        for word in ("tad", "kim", "idam", "eka"):
            found = S.vrddha(word)
            self.assertEqual(found.by, "1.1.74", word)
        from src.astadhyayi.rules.adhyaya_1_pada_1 import is_vrddhi
        self.assertFalse(is_vrddhi(S.first_vowel("tad")))
        self.assertFalse(is_vrddhi(S.first_vowel("kim")))

    def test_1_1_75_resumes_the_condition_with_eng(self):
        for word in ("eṇīpacana", "bhojakaṭa", "gonarda"):
            found = S.vrddha(word, praci_desa=True)
            self.assertEqual(found.by, "1.1.75", word)

    def test_1_1_75_needs_the_place(self):
        """प्राचामिति किम्? and देश इति किम्?"""
        self.assertIsNone(S.vrddha("eṇīpacana"))

    def test_1_1_75_engiti_kim_read_through_the_nyasa(self):
        """
        आहिच्छत्रः and कान्यकुब्जः are the DERIVATIVES. The Nyāsa gives the
        bases — अहिच्छत्रकान्यकुब्जशब्दाभ्याम् अण् एव भवति — and those begin
        with a, so neither 1.1.75 nor 1.1.73 reaches them. Passing the
        derivative instead returns 1.1.73, which is the mistake this test
        exists to pin down.
        """
        for base in ("ahicchatra", "kanyakubja"):
            self.assertEqual(S.first_vowel(base), "a", base)
            self.assertIsNone(S.vrddha(base, praci_desa=True), base)
        self.assertEqual(S.vrddha("āhicchatra").by, "1.1.73")

    def test_eng_is_resolved_and_not_listed(self):
        for vowel in resolve("eṄ").sounds:
            # not "ka": "e" + "ka" is eka, which tyadādi already holds
            self.assertEqual(
                S.vrddha(vowel + "ṇīpacana", praci_desa=True).by,
                "1.1.75", vowel,
            )


class PadaComplete(unittest.TestCase):
    """The whole of 1.1."""

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_all_seventy_five_sutras_of_1_1_are_codified(self):
        missing = [n for n in range(1, 76)
                   if not self.registry.has(f"1.1.{n}")]
        self.assertEqual(missing, [], f"1.1 is short of: {missing}")

    def test_every_one_is_executable_and_says_what_it_computes(self):
        for number in range(1, 76):
            sutra = self.registry.get(f"1.1.{number}")
            self.assertTrue(callable(sutra.apply), sutra.id)
            self.assertTrue(sutra.codification, sutra.id)

    def test_every_one_carries_notes_with_a_finding(self):
        from src.astadhyayi.report import findings

        for number in range(1, 76):
            sutra = self.registry.get(f"1.1.{number}")
            marked = findings(sutra.notes)
            self.assertTrue(marked, f"{sutra.id} reaches no finding")

    def test_every_one_carries_a_verified_mula_with_a_locator(self):
        from src.astadhyayi.sutra import Source, Status

        for number in range(1, 76):
            reading = self.registry.get(f"1.1.{number}").reading(Source.MULA)
            self.assertIs(reading.status, Status.VERIFIED, number)
            self.assertTrue(reading.locator, number)

    def test_the_pada_agrees_with_the_corpus_on_its_own_length(self):
        """
        1.1 has 75 sūtras. An earlier version of this test said 71, which is
        where the codification stopped rather than where the pāda does — and
        1.1.72 येन विधिस्तदन्तस्य, the tadantavidhi paribhāṣā, was being missed
        because of it.
        """
        from src.astadhyayi.sources import all_sutra_ids

        in_corpus = [s for s in all_sutra_ids() if s.startswith("1.1.")]
        self.assertEqual(len(in_corpus), 75)


if __name__ == "__main__":
    unittest.main()
