# -*- coding: utf-8 -*-
"""
3.2.141 to 3.2.155 — घिनुण्, वुञ्, युच्, उकञ् and षाकन्.

All still under 3.2.134's heading, so all of habit, office or doing
well. What this block asserts that no earlier one could:

  * a principle codified elsewhere being SUSPENDED for a whole
    heading, on a ज्ञापक three separate rules appeal to;
  * and the suspension being general rather than absolute, which the
    commentary says outright and the code cannot express;
  * a root picked out of a homograph pair by which CLASS it belongs
    to, twice on the same ground;
  * rules that name no root at all and reach by meaning.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.tacchila import (
    JALPADI, JVADI, KASADI, LASADI, NINDADI, SAMADI, SUDADI,
    TACCHILA,
    provisions_for, tacchila_affix, tacchila_heading,
)
from src.astadhyayi.upapada_krt import Added


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.141", "ghinuṇ", dict(root="śam")),
        ("3.2.142", "ghinuṇ", dict(root="dviṣ")),
        ("3.2.143", "ghinuṇ", dict(root="las", upasarga="vi")),
        ("3.2.144", "ghinuṇ", dict(root="laṣ", upasarga="apa")),
        ("3.2.145", "ghinuṇ", dict(root="lap", upasarga="pra")),
        ("3.2.146", "vuñ", dict(root="nind")),
        ("3.2.147", "vuñ", dict(root="kruś", upasarga="ā")),
        ("3.2.148", "yuc", dict(akarmaka=True, sense="calana-śabda")),
        ("3.2.149", "yuc", dict(anudattet=True, hal_adi=True,
                                akarmaka=True)),
        ("3.2.150", "yuc", dict(root="jval")),
        ("3.2.151", "yuc", dict(root="krudh", sense="krodha-bhūṣā")),
        ("3.2.154", "ukañ", dict(root="kam")),
        ("3.2.155", "ṣākan", dict(root="jalp")),
    )

    def test_every_giving_rule_answers_for_itself(self):
        for sutra, gives, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = tacchila_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_every_named_root_is_reached_by_a_rule_that_names_it(self):
        """
        The property is NOT that each list rule exclusively owns its
        members — thirteen pairs of rules in this run share a root,
        so that was never true. What holds is that a named root is
        answered by a rule which names it.

        Most of the sharing resolves on other conditions: 3.2.143 to
        3.2.145 each want a particular preverb, and 3.2.138 wants the
        Veda where 3.2.139 does not. What is left is a handful of
        genuine ties, and those are the समावेश the commentary allows.
        """
        naming = {}
        for row in TACCHILA:
            for root in row.of:
                naming.setdefault(root, set()).add(row.sutra)
        self.assertTrue(naming)
        for root, sutras in sorted(naming.items()):
            with self.subTest(root=root):
                answer = tacchila_affix(root=root)
                self.assertIn(
                    answer.by, sutras | {"3.2.135"},
                    "%s is named by %s but answered by %s"
                    % (root, sorted(sutras), answer.by))

    def test_sharing_a_root_is_common_here_and_not_a_defect(self):
        """
        Recorded as a fact about the run: a reader who assumed each
        rule owned its list would be surprised, and so was this test.
        """
        from itertools import combinations

        named = {r.sutra: set(r.of) for r in TACCHILA if r.of}
        shared = [(a, b) for a, b in combinations(sorted(named), 2)
                  if named[a] & named[b]]
        self.assertGreater(len(shared), 5)

    def test_three_roots_are_named_by_two_rules_at_once(self):
        """
        लष्, पत् and पद् stand in both 3.2.150 and 3.2.154, and the
        vṛtti gives forms from EACH — लषणः, पतनः, पदनः on the one
        side; अपलाषुकम्, प्रपातुका, उपपादुकम् on the other.

        That is the क्वचित् समावेश इष्यत एव the commentary allows
        when it calls the suspension of वासरूप only general. The
        resolver can name one rule, so it names the earlier; the
        second form is real and the code cannot offer it, which is
        why 3.2.154's note carries the overlap.
        """
        shared = sorted(set(JVADI) & set(LASADI))
        self.assertEqual(shared, ["laṣ", "pad", "pat"])
        for root in shared:
            with self.subTest(root=root):
                self.assertIn(root, provisions_for("3.2.150")[0].of)
                self.assertIn(root, provisions_for("3.2.154")[0].of)
                # one answer comes back, and it is a real rule
                self.assertIn(tacchila_affix(root=root).by,
                              ("3.2.150", "3.2.154"))

    def test_every_rule_of_the_run_falls_under_the_heading(self):
        for n in range(141, 156):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(
                    tacchila_heading("3.2.%d" % n).by, "3.2.134")


class APrincipleSuspendedForAWholeHeading(unittest.TestCase):
    """
    Three rules appeal to one ज्ञापक — ताच्छीलिकेषु वासरूपविधिर्
    नास्ति — and 3.2.146 argues it out: ण्वुल् would have given the
    same form as वुञ्, so prescribing वुञ् cannot be for the form's
    sake and must be saying something else.

    3.1.94 वाऽसरूपोऽस्त्रियाम् IS codified, and its own notes record
    that it suspends the अपवाद principle for the कृत् section. This
    heading then suspends that suspension.
    """

    def test_the_rule_being_suspended_is_codified(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.1.94", {str(s.id) for s in REGISTRY.all()})

    def test_three_rules_appeal_to_the_same_jnapaka(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.2.146", "3.2.150", "3.2.153"):
            with self.subTest(sutra=sutra):
                self.assertIn("वासरूप", REGISTRY.get(sutra).notes)
        self.assertIn("3.1.94", REGISTRY.get("3.2.146").notes)

    def test_the_resolver_gives_one_answer_and_that_is_now_the_reason(self):
        """
        Nothing in the code had to change: a ranked table already
        picks one winner. What the ज्ञापक supplies is WHY one answer
        is right here — the text says the rivals do not stand, rather
        than the table merely declining to offer them.
        """
        answer = tacchila_affix(root="nind")
        self.assertIsInstance(answer, Added)
        self.assertEqual(answer.gives, "vuñ")

    def test_but_the_suspension_is_general_and_not_absolute(self):
        """
        प्रायिकं चैतद् ज्ञापकम्, क्वचित् समावेश इष्यत एव — and the
        vṛtti gives pairs that do stand together. The code cannot
        offer two affixes at once here, so this is a SCAR and is
        recorded as one rather than quietly ignored.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("प्रायिकं", REGISTRY.get("3.2.150").notes)
        self.assertIn("समावेशो दृश्यते", REGISTRY.get("3.2.153").notes)


class TwoRefusalsThatDoNotGovern(unittest.TestCase):
    """
    3.2.152 न यः and 3.2.153 सूददीपदीक्षश्च refuse युच्. What those
    roots take instead is 3.2.135's तृन् — which is the form the vṛtti
    gives — so that rule is named and the प्रतिषेध rides alongside.
    """

    def test_the_supplier_is_named_and_the_refusal_carried(self):
        for where, refuser in (
            (dict(y_final=True, anudattet=True, hal_adi=True,
                  akarmaka=True), "3.2.152"),
            (dict(root="sūd", anudattet=True, hal_adi=True,
                  akarmaka=True), "3.2.153"),
        ):
            with self.subTest(refuser=refuser):
                answer = tacchila_affix(**where)
                self.assertEqual((answer.by, answer.gives),
                                 ("3.2.135", "tṛn"))
                self.assertEqual(answer.blocked_by, refuser)

    def test_without_the_refusal_the_yuc_would_have_stood(self):
        """The refusals have to be doing work, or they say nothing."""
        answer = tacchila_affix(anudattet=True, hal_adi=True,
                                akarmaka=True)
        self.assertEqual((answer.by, answer.gives), ("3.2.149", "yuc"))
        self.assertEqual(answer.blocked_by, "")

    def test_all_three_of_3_2_153s_roots_are_refused(self):
        for root in SUDADI:
            with self.subTest(root=root):
                answer = tacchila_affix(root=root, anudattet=True,
                                        hal_adi=True, akarmaka=True)
                self.assertEqual(answer.blocked_by, "3.2.153")

    def test_3_2_153_is_needed_because_the_suspension_is_partial(self):
        """
        The vṛtti asks why a refusal is wanted at all when 3.2.167
        would displace the युच् anyway, and answers वासरूपेण युजपि
        प्राप्नोति — it could still have stood BESIDE. So this rule
        exists precisely because वासरूप is only generally suspended.
        """
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.153").notes
        self.assertIn("3.2.167", notes)
        self.assertIn("वासरूपेण", notes)


class ARootPickedOutByItsClass(unittest.TestCase):
    """
    लुग्विकरणत्वात् — a root that loses its class-marker cannot be
    identified by it, so it cannot be the one a rule names. Used at
    3.2.142 for पृची and again at 3.2.145 for वस्, four rules apart.
    """

    def test_both_arguments_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.2.142", "3.2.145"):
            with self.subTest(sutra=sutra):
                self.assertIn("लुग्विकरणत्वात्",
                              REGISTRY.get(sutra).notes)

    def test_and_3_2_142_settles_four_before_giving_any_form(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.142").notes
        for probe in ("पृची", "परिदेवि", "क्षिप्", "युज्"):
            with self.subTest(probe=probe):
                self.assertIn(probe, notes)


class APreverbNamedAndAPreverbNot(unittest.TestCase):
    """
    3.2.143 to 3.2.145 each name WHICH preverb; 3.2.147 wants any one
    at all. Two different conditions, and the second needed a field of
    its own rather than a list of twenty-two.
    """

    def test_a_named_preverb_is_required_exactly(self):
        self.assertEqual(
            tacchila_affix(root="las", upasarga="vi").by, "3.2.143")
        self.assertNotEqual(
            tacchila_affix(root="las", upasarga="pra").by, "3.2.143")

    def test_and_3_2_147_takes_whichever_stands(self):
        for upasarga in ("ā", "pari", "pra"):
            with self.subTest(upasarga=upasarga):
                self.assertEqual(
                    tacchila_affix(root="dev", upasarga=upasarga).by,
                    "3.2.147")

    def test_but_still_needs_one(self):
        """उपसर्ग इति किम्? देवयिता, क्रोष्टा."""
        self.assertNotEqual(
            tacchila_affix(root="dev").by, "3.2.147")

    def test_the_two_conditions_are_separate_fields(self):
        self.assertEqual(
            provisions_for("3.2.143")[0].which_upasarga, ("vi",))
        self.assertTrue(provisions_for("3.2.147")[0].any_upasarga)
        self.assertEqual(
            provisions_for("3.2.147")[0].which_upasarga, ())

    def test_3_2_144_borrows_the_preverb_of_the_rule_before(self):
        """चकाराद् वौ च — अपलाषी and विलाषी both."""
        for upasarga in ("apa", "vi"):
            with self.subTest(upasarga=upasarga):
                self.assertEqual(
                    tacchila_affix(root="laṣ", upasarga=upasarga).by,
                    "3.2.144")


class RulesThatNameNoRoot(unittest.TestCase):
    """
    3.2.148 reaches whatever MEANS motion or sound; 3.2.151 whatever
    means anger or adorning. The condition is on the sense, so words
    beyond those the vṛtti lists are covered — रोषणः and भूषणः stand
    beside the two roots named.
    """

    def test_they_answer_with_no_root_given_at_all(self):
        self.assertEqual(
            tacchila_affix(akarmaka=True,
                           sense="calana-śabda").by, "3.2.148")
        self.assertEqual(provisions_for("3.2.148")[0].of, ())

    def test_and_3_2_148_needs_its_intransitive(self):
        """अकर्मकादिति किम्? पठिता विद्याम्."""
        self.assertNotEqual(
            tacchila_affix(sense="calana-śabda").by, "3.2.148")

    def test_3_2_151_reaches_beyond_the_roots_it_names(self):
        """
        क्रुधमण्डार्थेभ्यः — of the MEANING, so a root the sūtra does
        not name is reached where it carries the sense.
        """
        row = provisions_for("3.2.151")[0]
        self.assertEqual(row.sense, "krodha-bhūṣā")
        self.assertEqual(
            tacchila_affix(root="krudh",
                           sense="krodha-bhūṣā").by, "3.2.151")


class MarkersDoingUnrelatedJobs(unittest.TestCase):
    """
    3.2.141's घिनुण् carries three marks and the vṛtti gives each a
    different purpose — one of them purely mechanical, merely making
    the consonant sayable. 3.2.155's ष is written for the feminine two
    adhyāyas away.
    """

    def test_the_three_jobs_are_recorded_separately(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.141").notes
        for probe in ("कुत्वार्थः", "उच्चारणार्थः", "वृद्ध्यर्थः"):
            with self.subTest(probe=probe):
                self.assertIn(probe, notes)

    def test_and_3_2_155s_marker_serves_another_adhyaya(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("ङीषर्थः", REGISTRY.get("3.2.155").notes)


class TheScarThisRunRecords(unittest.TestCase):
    """
    सूदेर् युचि प्रतिषिद्धे कथं मधुसूदनः? The vṛtti offers three
    explanations and settles on none — and one of them leans on
    3.3.113, the same uncodified rule 3.2.53 had to lean on.
    """

    def test_the_scar_is_marked_as_one(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.153").notes
        self.assertIn("SCAR", notes)
        self.assertIn("3.3.113", notes)

    def test_and_that_rule_is_codified_now(self):
        """
        PAID. The second of three assertions in three files that
        3.3.113 was not yet written. All three went red together.
        """
        from src.astadhyayi.bhava_krt import krtya_lyut_bahulam
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.113", {str(s.id) for s in REGISTRY.all()})
        self.assertEqual(krtya_lyut_bahulam().by, "3.3.113")

    def test_this_run_declares_no_reuse(self):
        from src.astadhyayi.sutra import REGISTRY

        for n in range(141, 156):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(REGISTRY.get("3.2.%d" % n).reuses, ())


if __name__ == "__main__":
    unittest.main()
