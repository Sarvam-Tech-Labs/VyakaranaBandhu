# -*- coding: utf-8 -*-
"""
The yaṇ family of the sandhi engine: 6.1.77–83, and what the yaṇ brings on —
8.2.23, 8.2.29, 8.4.46–54, 8.4.64.

**Where the expectations come from.** Each test names its source in its
docstring: the Kāśikā's own examples and counter-examples (*X iti kim?*), the
Laghusiddhāntakaumudī's lines for *sudhī + upāsya* and its neighbours (the
Kaumudī on 8.2.23 for the forms the Laghu on disk has lost letters from —
*मद्ध्वरिः*, *धात्रंशः*), and the vārttikas as the corpus has them.

**What "capable of failing" means here.** Where a result could come out right by
luck the test also asserts the *steps* (sūtra ids, in order), and where a rule is
said to be load-bearing a test takes it out of the rulebook and shows the form
that then results — the vārttika of 8.2.23 (सुदुपास्य would lose its य्), the
option of 8.4.51 (nothing would be undoubled), the Kaumudī's reading of 6.1.79
(गयूति). The rules are run from the family's own rulebook plus
`ac_ekadesa` (which 6.1.77 competes with), so what is asserted is what THESE
rules do; the Laghu-shaped tests at the end use the whole rulebook.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import replace

from src.astadhyayi import corpus
from src.astadhyayi.anga import AYAV, ec, jhalam_jas_jhasi, yan_sandhi
from src.astadhyayi.reading import yathasamkhya
from src.astadhyayi.sandhi import rulebook, sandhi, trace
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi.engine import derive
from src.astadhyayi.sandhi.families import ac_yan_ayadi as fam
from src.astadhyayi.sandhi.parse import parse
from src.astadhyayi.sandhi.rule import (
    PRAKRTIBHAVA, VARTTIKA, Application, Detail, remark, rule, site)
from src.astadhyayi.sandhi.segs import PRAKRTYA

MINE = rulebook.rules_of("ac_yan_ayadi")
WITH_EKADESA = rulebook.rules_of("ac_yan_ayadi", "ac_ekadesa")
#: This family with the two whose rules a visarga-final or a consonant-final
#: word meets (8.2.66, 8.3.15, 8.3.19; 8.2.39). Named by family so that a
#: family added later cannot change what these tests are about.
WITH_VISARGA = rulebook.rules_of("ac_yan_ayadi", "visarga_ru")
WITH_HAL = rulebook.rules_of("ac_yan_ayadi", "visarga_ru", "hal_assimilation")

#: The sūtras of the family's scope, as the task states them.
SCOPE = (
    "6.1.77", "6.1.78", "6.1.79", "6.1.80", "6.1.81", "6.1.82", "6.1.83",
    "8.4.46", "8.4.47", "8.4.48", "8.4.49", "8.4.50", "8.4.51", "8.4.52",
    "8.4.53", "8.4.54", "8.4.64", "8.2.23", "8.2.29",
    "1.1.9", "1.1.10", "1.1.50", "1.1.51", "1.1.52", "1.1.66", "1.1.67",
    "1.1.69", "1.1.70", "1.3.10")


def run(text, rules=MINE, **kw):
    return sandhi(text, rules=rules, **kw)


def taken(outcome):
    """The steps that were done — not the notes of an option declined."""
    return [s for s in outcome.steps if not s.declined]


def ids(outcome):
    return [s.sutra for s in taken(outcome)]


def surfaces(text, rules=MINE, **kw):
    return set(run(text, rules, **kw).surfaces)


def outcome_of(result, surface):
    """The first derivation that ends in `surface`."""
    return next(o for o in result.outcomes if o.surface == surface)


def in_order(wanted, got):
    """`wanted` occurs in `got` as a subsequence."""
    it = iter(got)
    return all(any(w == g for g in it) for w in wanted)


def deviz(text):
    """A form with its final visarga read as the स् the parser read it as.

    A word that ends in a visarga is read as ending in स् (8.2.66; the parser
    says so in the trace), and it is turned back into a visarga only by the
    rules of the visarga family, which a run of THIS family's rules alone does
    not include. The assertions below that concern a visarga-final word are
    made in that reading, on both sides."""
    return text.replace("ḥ", "s")


def norm(text):
    text = re.sub(r"<<|>>|<!|!>", "", text or "")
    text = re.sub(r"\[\[[^\]]*\]\]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def without(rules, sutra, *, authority=None, varttika=None):
    """The rulebook with one rule taken out — to see what it was doing."""
    def gone(r):
        if r.sutra != sutra:
            return False
        if authority is not None and r.authority != authority:
            return False
        return varttika is None or r.varttika == varttika
    return tuple(r for r in rules if not gone(r))


# ---------------------------------------------------------------------------
# What the module says it covers, and whether it is true
# ---------------------------------------------------------------------------


class Coverage(unittest.TestCase):

    def test_the_rulebook_is_sound(self):
        self.assertEqual(rulebook.problems(), [])

    def test_coverage_names_every_sutra_of_the_scope_and_no_other(self):
        declared = [sutra for sutra, _, _ in fam.COVERAGE]
        self.assertEqual(sorted(declared), sorted(set(declared)),
                         "a sūtra is declared twice")
        self.assertEqual(set(declared), set(SCOPE))

    def test_every_rule_is_declared_as_implemented(self):
        status = {sutra: st for sutra, st, _ in fam.COVERAGE}
        for rule in fam.RULES:
            self.assertIn(status[rule.sutra], ("rule", "partial", "vedic"),
                          rule.sutra)

    def test_a_sutra_marked_scope_or_support_has_no_rule(self):
        """Not claiming what is not done: a SCOPE sūtra runs nothing."""
        ruled = {r.sutra for r in fam.RULES}
        for sutra, st, note in fam.COVERAGE:
            if st in ("scope", "support"):
                self.assertNotIn(sutra, ruled, sutra)
        self.assertEqual(
            {s for s, st, _ in fam.COVERAGE if st == "scope"},
            {"8.4.48", "8.4.49"})

    def test_a_scope_or_partial_note_gives_a_reason(self):
        for sutra, st, note in fam.COVERAGE:
            if st in ("scope", "partial"):
                self.assertGreater(len(note.strip()), 30, (sutra, note))

    def test_a_vedic_rule_is_marked_vedic(self):
        vedic = {(r.sutra, r.varttika) for r in fam.RULES if r.vedic}
        self.assertEqual({s for s, _ in vedic}, {"6.1.79", "6.1.83"})
        self.assertEqual(
            sum(1 for r in fam.RULES if r.sutra == "6.1.83"),
            sum(1 for r in fam.RULES if r.sutra == "6.1.83" and r.vedic))

    def test_every_rule_carries_the_family_tag_its_kind_is_known_by(self):
        for rule in fam.RULES:
            if rule.sutra.startswith("6.1."):
                self.assertIn("ac", rule.families, rule.sutra)
            else:
                self.assertIn("hal", rule.families, rule.sutra)

    def test_the_rules_stand_in_the_sutra_order_8_2_1_speaks_of(self):
        orders = [r.order for r in rulebook.all_rules()]
        self.assertEqual(orders, sorted(orders))

    def test_every_sutra_the_module_names_is_a_sutra_of_the_corpus(self):
        """A number typed in the source — in a Via, an override, a docstring —
        is checked against the Vidyut sūtrapāṭha, not trusted."""
        import inspect
        known = corpus.load_vidyut_sutrapatha()
        text = inspect.getsource(fam)
        named = set(re.findall(r"(?<![\d.])[1-8]\.[1-4]\.\d{1,3}(?![\d.])",
                               text))
        self.assertGreater(len(named), 30)
        for sutra in sorted(named):
            self.assertIn(sutra, known, sutra)

    def test_the_numbers_typed_for_sutras_outside_the_scope_are_the_ones_meant(self):
        """The sūtras this family cites but does not own are typed as numbers
        in its source, so each is checked here against its own words in the
        corpus (a mistyped digit once printed the wrong sūtra)."""
        known = corpus.load_vidyut_sutrapatha()
        for sutra, words in (("6.1.101", "akaḥ savarṇe dīrghaḥ"),
                             ("6.1.125", "plutapragṛhyā aci nityam"),
                             ("8.2.24", "rātsasya"),
                             ("8.3.19", "lopaḥ śākalyasya"),
                             ("1.1.10", "nājjhalau"),
                             ("1.1.51", "uraṇ raparaḥ"),
                             ("1.1.52", "alo’ntyasya")):
            self.assertEqual(known[sutra].text, words, sutra)

    def test_the_supports_the_coverage_says_are_cited_are_cited(self):
        """COVERAGE says 1.1.50, 1.1.51, 1.1.52, 1.1.66, 1.1.67, 1.1.69 and
        1.3.10 are cited by steps, and 1.1.10 and 1.1.70 by none. Over a battery
        of derivations, that is what the steps say — so a note that claimed a
        citation nothing makes would fail here."""
        battery = ("sudhī upāsya", "dhātṛ aṃśa", "ḷ ākṛti", "hari anubhava",
                   "ke ete", "go~yam", "gomānt", "takṣ", "iti ādi",
                   "thi{abhyasa}~ṣṭhāsati")
        cited = set()
        for text in battery:
            for outcome in run(text).outcomes:
                for step in outcome.steps:
                    cited.update(step.sutras)
        cited.update(v.sutra for o in derive(
            PlutapurvasyaIkah.state("bho{pluta} i indra"), WITH_EKADESA)
            for step in o.steps for v in step.detail.via)
        statuses = {sutra: st for sutra, st, _ in fam.COVERAGE}
        for sutra in ("1.1.9", "1.1.50", "1.1.51", "1.1.52", "1.1.66",
                      "1.1.67", "1.1.69", "1.3.10"):
            self.assertEqual(statuses[sutra], "support", sutra)
            self.assertIn(sutra, cited, sutra)
        for sutra in ("1.1.10", "1.1.70"):
            self.assertEqual(statuses[sutra], "support", sutra)
            self.assertNotIn(sutra, cited, sutra)

    def test_1_1_10_is_asked_inside_the_projects_savarna(self):
        """No step of this family turns on 1.1.10, but it is what keeps a यण्
        from being savarṇa to the इक् it replaces (and ह् from अ): asked."""
        from src.astadhyayi.varna import savarna
        self.assertFalse(savarna("i", "y"))
        self.assertFalse(savarna("u", "v"))
        self.assertFalse(savarna("a", "h"))
        self.assertTrue(savarna("i", "ī"))


class Sources(unittest.TestCase):
    """Every word of the tradition the module quotes is on disk, where it says."""

    def test_every_quotation_is_a_substring_of_its_commentary(self):
        for name, (sutra, work, quote) in fam.SOURCES.items():
            text = norm(corpus.commentary_on(sutra, work))
            self.assertTrue(text, (name, sutra, work))
            self.assertIn(norm(quote), text, (name, sutra, work))

    def test_the_quotation_check_can_fail(self):
        """A quotation with one word changed — Śākalya's *न भवति* made *भवति* —
        is not in the commentary, so the check above would have caught it."""
        text = norm(corpus.commentary_on("8.4.51", "kashika"))
        changed = norm(fam._quote("sakalya")).replace(" न भवति", " भवति")
        self.assertNotEqual(changed, norm(fam._quote("sakalya")))
        self.assertNotIn(changed, text)
        self.assertIn(norm(fam._quote("sakalya")), text)

    def test_the_varttikas_are_the_corpus_own_words(self):
        expected = {
            fam.VT_GOR_YUTAU: "6.1.79", fam.VT_ADHVA: "6.1.79",
            fam.VT_HRADAYYA: "6.1.83", fam.VT_ARSA: "6.1.83",
            fam.VT_YANAH: "8.2.23", fam.VT_MAYO: "8.4.47"}
        for text, sutra in expected.items():
            self.assertIn(text, [v.text for v in corpus.varttikas_on(sutra)],
                          (sutra, text))
        self.assertIn(norm(fam.VT_PLUTA),
                      norm(corpus.commentary_on("6.1.77", "kashika")))

    def test_a_varttika_rule_says_so_and_a_sutra_rule_does_not(self):
        marked = [r for r in fam.RULES if r.authority == VARTTIKA]
        self.assertEqual(
            {r.varttika for r in marked},
            {fam.VT_PLUTA, fam.VT_GOR_YUTAU, fam.VT_ADHVA, fam.VT_HRADAYYA,
             fam.VT_ARSA, fam.VT_YANAH, fam.VT_MAYO})
        for rule in fam.RULES:
            if rule.authority != VARTTIKA:
                self.assertEqual(rule.authority, "sūtra")

    def test_a_reason_in_overrides_quotes_the_tradition(self):
        """The reasons are built from the checked quotations, so each holds one."""
        for rule in fam.RULES:
            for target, why in rule.overrides:
                self.assertTrue(
                    any(q in why for _, _, q in fam.SOURCES.values()),
                    (rule.sutra, target, why))

    def test_the_words_of_every_step_are_the_corpus_words(self):
        known = corpus.load_vidyut_sutrapatha()
        for text, kw in (("sudhī upāsya", {}), ("madhu ari", {}),
                         ("hari anubhava", {}), ("go~ya", {}),
                         ("go-yūtiḥ{adhvaparimana}", {})):
            for outcome in run(text, rulebook.all_rules(), **kw).outcomes:
                for step in trace.outcome_dict(outcome)["steps"]:
                    self.assertEqual(step["sutra_iast"],
                                     known[step["sutra"]].text)
                    for via in step["via"]:
                        self.assertEqual(via["text_iast"],
                                         known[via["sutra"]].text)


# ---------------------------------------------------------------------------
# 6.1.77 इको यणचि
# ---------------------------------------------------------------------------


class IkoYanaci(unittest.TestCase):

    def test_the_kasikas_examples(self):
        """Kāśikā on 6.1.77: दध्यत्र। मध्वत्र। कर्त्रर्थम्। हर्त्रर्थम्। लाकृतिः."""
        for given, first in (("dadhi atra", "dadhyatra"),
                             ("madhu atra", "madhvatra"),
                             ("kartṛ artham", "kartrartham"),
                             ("hartṛ artham", "hartrartham"),
                             ("ḷ ākṛtiḥ", "lākṛtiḥ")):
            result = run(given)
            self.assertEqual(deviz(result.surface), deviz(first), given)
            self.assertEqual(result.outcomes[0].steps[0].sutra, "6.1.77", given)

    def test_each_ik_has_its_own_yan_and_the_project_agrees(self):
        """1.1.50 picks the yaṇ; `anga.yan_sandhi` is the same sūtra asked as a
        question, and the step must say the sound it says."""
        checked = 0
        for ik in ("i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ"):
            for vowel in ("a", "ā", "e", "o", "ai", "au"):
                expected = yan_sandhi(ik, vowel).result
                if expected is None:
                    continue
                first = run(f"{ik} {vowel}").outcomes[0].steps[0]
                self.assertEqual(first.sutra, "6.1.77", (ik, vowel))
                self.assertEqual(first.detail.adesa, expected, (ik, vowel))
                checked += 1
        self.assertGreater(checked, 40)

    def test_the_step_names_the_sutras_that_made_it_land(self):
        """Which side (1.1.66), which yaṇ (1.1.50) and, for a long इक्, why the
        long ई is an इक् at all (1.1.69) — asked of the corpus, not retyped."""
        step = run("sudhī upāsya").outcomes[0].steps[0]
        self.assertEqual([v.sutra for v in step.detail.via],
                         ["1.1.69", "1.1.66", "1.1.50"])
        short = run("dadhi atra").outcomes[0].steps[0]
        self.assertEqual([v.sutra for v in short.detail.via],
                         ["1.1.66", "1.1.50"])

    def test_the_r_varna_takes_no_repha_because_the_yan_is_not_an_an(self):
        """Laghu: धातृ + अंशः. 1.1.51 would add र् after an अण् put for ṛ; the
        yaṇ र् is not an अण्, so धात्रंशः, and never *धात्र्रंशः*."""
        result = run("dhātṛ aṃśa")
        step = result.outcomes[0].steps[0]
        self.assertEqual(step.detail.adesa, "r")
        self.assertIn("1.1.51", [v.sutra for v in step.detail.via])
        self.assertIn("dhātraṃśa", result.surfaces)
        for surface in result.surfaces:
            self.assertNotIn("rr", surface)

    def test_the_l_varna_takes_no_l_either(self):
        """Kāśikā: लाकृतिः. The vārttika लपर would add ल् after an अण् put for
        ḷ; the yaṇ ल् is not one, so लाकृति and not *लाल्कृति*."""
        step = run("ḷ ākṛti").outcomes[0].steps[0]
        self.assertEqual(step.detail.adesa, "l")
        self.assertIn("1.1.51", [v.sutra for v in step.detail.via])
        self.assertEqual(surfaces("ḷ ākṛti"), {"lākṛti"})

    def test_a_consonant_after_is_no_reason(self):
        """अचि इति किम्? दधि करोति (Nyāsa on 6.1.77)."""
        result = run("dadhi karoti")
        self.assertEqual(result.surfaces, ("dadhikaroti",))
        self.assertEqual(result.outcomes[0].steps, ())

    def test_where_the_two_vowels_are_alike_the_later_rule_takes_the_place(self):
        """दधीन्द्रः — 6.1.77 reaches it, 6.1.101 stands later and is done, by
        1.4.2 (Kāśikā on 6.1.101: सवर्ण इति किम्? दध्यत्र)."""
        result = run("dadhi indra", WITH_EKADESA)
        self.assertEqual(result.surfaces, ("dadhīndra",))
        step = result.outcomes[0].steps[0]
        self.assertEqual(step.sutra, "6.1.101")
        self.assertIn("6.1.77", [a.sutra for a in step.against])

    def test_only_an_ik_takes_the_yan(self):
        """इकः: run alone, 6.1.77 leaves every vowel that is not an इक् — an
        अ, आ, ए, ओ, ऐ, औ — where it is; 6.1.78 and the rest are not in the
        book, so nothing else could have hidden a yaṇ made for them."""
        alone = (fam.iko_yanaci,)
        for first in ("a", "ā", "e", "o", "ai", "au"):
            for second in ("a", "i", "u", "e", "au"):
                result = run(f"{first} {second}", alone)
                self.assertEqual(result.outcomes[0].steps, (),
                                 (first, second))

    def test_a_consonant_alike_to_the_ik_is_no_ac(self):
        """Kaumudī on 1.1.10: तेन दधीत्यस्य हरति शीतलं षष्ठं सान्द्रमित्येतेषु परेषु
        यणादिकं न — the ह्, श्, ष्, स् are savarṇa to a vowel by place and effort
        and are not an अच् (नाज्झलौ), so 6.1.77 has nothing to reach; and
        Kāśikā on 1.1.10: दण्डहस्तः, दधिशीतम् — nor does 6.1.101 join them."""
        for given, done in (("dadhi harati", "dadhiharati"),
                            ("dadhi śītalam", "dadhiśītalam"),
                            ("dadhi ṣaṣṭham", "dadhiṣaṣṭham"),
                            ("dadhi sāndram", "dadhisāndram"),
                            ("daṇḍa hasta", "daṇḍahasta")):
            for rules in (MINE, WITH_EKADESA):
                result = run(given, rules)
                self.assertEqual(result.surfaces, (done,), given)
                self.assertEqual(result.outcomes[0].steps, (), given)

    def test_a_nasal_iK_keeps_its_nasality(self):
        state = parse("ti atra")
        segs = list(state.segs)
        segs[1] = replace(segs[1], marks=segs[1].marks | {"anunāsika"})
        outcome = derive(replace(state, segs=tuple(segs)), MINE)[0]
        self.assertTrue(any(s.nasal for s in outcome.final.segs if s.s == "y"))


class PlutapurvasyaIkah(unittest.TestCase):
    """The vārttika: इकः प्लुतपूर्वस्य सवर्णदीर्घबाधनार्थं यणादेशो वक्तव्यः
    (Kāśikā on 6.1.77) — भो३ इ इन्द्रम् ⟶ भो३यिन्द्रम्; Bhāṣya: अग्ना३इ इन्द्रम्,
    पटा३उ उदकम्, अग्ना३इ आशा, पटा३उ आशा.

    The pluta vowel is held from sandhi by 6.1.125, which is the prakṛtibhāva
    family's; its hold is put on the vowel here by hand, as that rule will.
    The pragṛhya इ or उ that follows is held by the same rule and lifted by
    this vārttika (Padamañjarī: *तस्य प्रकृतिभावे प्राप्ते यण्विधीयते*)."""

    @staticmethod
    def state(text, *, hold_i=False):
        """The row as the prakṛtibhāva family leaves it: the pluta vowel — the
        last sound of the first word — held and, if asked, the pragṛhya vowel
        that is the whole of the second word held too."""
        state = parse(text)
        segs = list(state.segs)
        last = max(i for i, s in enumerate(segs) if s.w == 0)
        second = next(i for i, s in enumerate(segs) if s.w == 1)
        segs[last] = replace(segs[last], marks=segs[last].marks | {PRAKRTYA})
        if hold_i:
            segs[second] = replace(segs[second],
                                   marks=segs[second].marks | {PRAKRTYA})
        return replace(state, segs=tuple(segs))

    def test_the_pluta_preceded_ik_takes_the_yan_before_a_savarna_vowel(self):
        outcome = derive(self.state("bho{pluta} i indra"), WITH_EKADESA)[0]
        self.assertEqual(outcome.surface, "bhoyindra")
        self.assertEqual([s.sutra for s in outcome.steps], ["6.1.77"])
        step = outcome.steps[0]
        self.assertEqual(step.detail.authority, VARTTIKA)
        self.assertEqual(step.detail.varttika, fam.VT_PLUTA)
        self.assertIn("6.1.101", [a.sutra for a in step.against])
        self.assertIn("1.1.9", [v.sutra for v in step.detail.via])

    def test_without_the_vartika_the_two_alike_vowels_join(self):
        rules = without(WITH_EKADESA, "6.1.77", authority=VARTTIKA)
        outcome = derive(self.state("bho{pluta} i indra"), rules)[0]
        self.assertEqual(outcome.surface, "bhoīndra")
        self.assertEqual([s.sutra for s in outcome.steps], ["6.1.101"])

    def test_it_needs_the_word_before_to_be_pluta(self):
        """No `pluta`, no vārttika: the two join."""
        outcome = derive(self.state("bho i indra"), WITH_EKADESA)[0]
        self.assertEqual(outcome.surface, "bhoīndra")
        self.assertEqual([s.sutra for s in outcome.steps], ["6.1.101"])

    def test_the_bhasyas_four_with_the_pragrhya_vowel_held(self):
        """Bhāṣya on 6.1.77: अग्ना३इ इन्द्रम् — अग्ना३यिन्द्रम्। पटा३उ उदकम् —
        पटा३वुदकम्। अग्ना३इ आशा — अग्ना३याशा। पटा३उ आशा — पटा३वाशा. The इ and
        उ are held (pragṛhya) and the yaṇ stands in their place, whether the
        vowel after is alike (the first two) or not (the last two)."""
        for text, done in (("agnā{pluta} i indra", "agnāyindra"),
                           ("paṭā{pluta} u udaka", "paṭāvudaka"),
                           ("agnā{pluta} i āśā", "agnāyāśā"),
                           ("paṭā{pluta} u āśā", "paṭāvāśā")):
            outcome = derive(self.state(text, hold_i=True), WITH_EKADESA)[0]
            self.assertEqual(outcome.surface, done, text)
            self.assertEqual([s.sutra for s in outcome.steps], ["6.1.77"], text)
            self.assertEqual(outcome.steps[-1].detail.varttika,
                             fam.VT_PLUTA, text)

    def test_the_hold_is_what_the_vartika_lifts(self):
        """Take the vārttika away and the held इ stays: the yaṇ of the sūtra
        itself cannot reach a vowel another rule has held."""
        rules = without(WITH_EKADESA, "6.1.77", authority=VARTTIKA)
        for text in ("agnā{pluta} i āśā", "paṭā{pluta} u āśā"):
            outcome = derive(self.state(text, hold_i=True), rules)[0]
            self.assertEqual(outcome.steps, (), text)

    def test_where_the_ik_is_neither_held_nor_alike_the_vartika_is_not_cited(self):
        """An unheld इ before आ needs only 6.1.77: the vārttika adds nothing, so
        the step is the sūtra's own."""
        outcome = derive(self.state("agnā{pluta} i āśā"), WITH_EKADESA)[0]
        self.assertEqual(outcome.surface, "agnāyāśā")
        self.assertEqual(outcome.steps[-1].detail.authority, "sūtra")
        self.assertEqual(outcome.steps[-1].detail.varttika, "")

    def test_the_lifted_hold_is_not_put_back(self):
        outcome = derive(self.state("bho{pluta} i indra", hold_i=True),
                         WITH_EKADESA)[0]
        yan = next(s for s in outcome.final.segs if s.made_by == "6.1.77")
        self.assertNotIn(PRAKRTYA, yan.marks)
        self.assertEqual(yan.s, "y")

    def test_a_held_ik_with_no_pluta_before_it_is_left_alone(self):
        outcome = derive(self.state("bho i indra", hold_i=True),
                         WITH_EKADESA)[0]
        self.assertEqual(outcome.steps, ())

    def test_it_works_with_a_rule_that_holds_the_pluta_and_the_pragrhya_vowel(self):
        """The prakṛtibhāva family's 6.1.125 is not in this workspace; a
        stand-in holds a pluta vowel and a pragṛhya nipāta as that rule will.
        The hold stands later than 6.1.77 (1.4.2 gives it the place), so it is
        made first — on the pluta vowel, which nothing else protects from
        6.1.78, as well — and the vārttika then lifts the hold of the इ. A
        vārttika that had displaced 6.1.125 would have left the pluta vowel to
        become अव्: *bhav i indra*."""

        @rule("6.1.125", name="प्लुतप्रगृह्या अचि नित्यम् (stand-in)",
              families=("ac", "prakrtibhava"))
        def pragrhya(v):
            for j in v.pairs():
                left, right = j.left, j.right
                if left.is_vowel and right.is_vowel \
                        and (v.word(left).has("nipata")
                             or v.word(left).has("pluta")) \
                        and PRAKRTYA not in left.marks:
                    yield Application(
                        site=site(left, right),
                        edits=(remark(left, PRAKRTYA),),
                        detail=Detail(kind=PRAKRTIBHAVA, sthanin=left.s,
                                      adesa=left.s, nimitta="a vowel follows",
                                      because="a stand-in, for this test"))

        text = "bho{pluta} i{nipata} indra"
        rules = WITH_EKADESA + (pragrhya,)
        outcome = derive(parse(text), rules)[0]
        self.assertEqual(outcome.surface, "bhoyindra")
        self.assertIn("6.1.125", [s.sutra for s in taken(outcome)])
        self.assertEqual(taken(outcome)[-1].sutra, "6.1.77")
        self.assertEqual(taken(outcome)[-1].detail.varttika, fam.VT_PLUTA)
        self.assertNotIn("6.1.125", [t for t, _ in next(
            r for r in fam.RULES if r.varttika == fam.VT_PLUTA).overrides])
        without_it = without(rules, "6.1.77", authority=VARTTIKA)
        self.assertEqual(derive(parse(text), without_it)[0].surface,
                         "bhoiindra")


# ---------------------------------------------------------------------------
# 6.1.78 एचोऽयवायावः
# ---------------------------------------------------------------------------


class EcoYavayavah(unittest.TestCase):

    def test_the_kasikas_examples(self):
        """Kāśikā: चयनम्। लवनम्। चायकः। लावकः। कयेते। ययेते। वायाववरुणद्धि."""
        for given, done in (("ce~anam", "cayanam"), ("lo~anam", "lavanam"),
                            ("cai~akaḥ", "cāyakaḥ"), ("lau~akaḥ", "lāvakaḥ"),
                            ("ke ete", "kayete"), ("ye ete", "yayete"),
                            ("vāyau avaruṇaddhi", "vāyāvavaruṇaddhi")):
            result = run(given)
            self.assertEqual(result.surface.replace("ḥ", "s"),
                             done.replace("ḥ", "s"), given)
            self.assertEqual(ids(result.outcomes[0]), ["6.1.78"], given)

    def test_the_laghus_four(self):
        """Laghu: haraye / viṣṇave / nāyakaḥ / pāvakaḥ — each एच् takes its own,
        by 1.3.10, and the step says so."""
        for given, done, sub in (("hare~e", "haraye", "ay"),
                                 ("viṣṇo~e", "viṣṇave", "av"),
                                 ("nai~akaḥ", "nāyakaḥ", "āy"),
                                 ("pau~akaḥ", "pāvakaḥ", "āv")):
            result = run(given)
            self.assertEqual(result.surface.replace("ḥ", "s"),
                             done.replace("ḥ", "s"), given)
            step = result.outcomes[0].steps[0]
            self.assertEqual(step.detail.adesa, sub, given)
            self.assertEqual(
                [v.sutra for v in step.detail.via],
                ["1.1.66", "1.1.71", "1.3.10"], given)

    def test_the_pairing_is_the_one_1_3_10_makes_and_nothing_is_typed(self):
        pairs = dict(yathasamkhya(ec(), AYAV))
        self.assertEqual(len(pairs), 4)
        for sthanin, sub in pairs.items():
            first = run(f"{sthanin} a").outcomes[0].steps[0]
            self.assertEqual(first.detail.adesa, sub)

    def test_a_consonant_after_leaves_the_ec(self):
        """अचि — read down from 6.1.77: नेता, not *नयता*."""
        self.assertEqual(run("ne~ta").surface, "neta")
        self.assertEqual(ids(run("ne~ta").outcomes[0]), [])

    def test_a_short_a_after_a_pada_final_eng_is_6_1_109s(self):
        """हरेऽव: 6.1.109 is the exception, and 6.1.78 does not reach it."""
        result = run("hare ava", WITH_EKADESA)
        self.assertEqual(result.surface, "hare'va")
        self.assertEqual(ids(result.outcomes[0]), ["6.1.109"])
        step = result.outcomes[0].steps[0]
        self.assertIn("6.1.78", [a.sutra for a in step.against])

    def test_the_y_it_makes_is_not_doubled(self):
        """The य् of अय् is followed by a vowel: अनचि च asks for none."""
        self.assertEqual(surfaces("ke ete"), {"kayete"})


# ---------------------------------------------------------------------------
# 6.1.79–83
# ---------------------------------------------------------------------------


class VantoYiPratyaye(unittest.TestCase):

    def test_the_kasikas_examples(self):
        """Kāśikā on 6.1.79: बाभ्रव्यः। माण्डव्यः। शङ्कव्यं दारु। पिचव्यः
        कार्पासः। नाव्यो ह्रदः; Laghu: गव्यम्, नाव्यम्."""
        for given, done in (("go~yam", "gavyam"), ("nau~yam", "nāvyam"),
                            ("bābhro~yaḥ", "bābhravyaḥ"),
                            ("māṇḍo~yaḥ", "māṇḍavyaḥ"),
                            ("śaṅko~yam", "śaṅkavyam"),
                            ("pico~yaḥ", "picavyaḥ"),
                            ("nau~yaḥ", "nāvyaḥ")):
            result = run(given)
            self.assertEqual(result.surfaces, (deviz(done),), given)
            self.assertEqual(ids(result.outcomes[0]), ["6.1.79"], given)

    def test_o_gives_av_and_au_gives_av_by_1_3_10_and_the_vanta_is_cut_from_it(self):
        self.assertEqual(fam._vanta(), {"o": "av", "au": "āv"})
        self.assertEqual(run("go~ya").outcomes[0].steps[0].detail.adesa, "av")
        self.assertEqual(run("nau~ya").outcomes[0].steps[0].detail.adesa, "āv")

    def test_the_counter_examples(self):
        """वान्त इति किम्? रायमिच्छति रैयति (an ऐ). यीति किम्? गोभ्याम्,
        नौभ्याम्. प्रत्यय इति किम्? गोयानम्, नौयानम् — a compound, no affix."""
        for given in ("rai~yati", "go~bhyām", "nau~bhyām",
                      "go-yānam", "nau-yānam"):
            result = run(given)
            self.assertEqual(result.surface, given.replace("~", "")
                             .replace("-", ""), given)
            self.assertEqual(result.outcomes[0].steps, (), given)

    def test_the_affix_is_told_by_the_tilde_and_not_by_the_letters(self):
        """Same letters, one affix and one compound member."""
        self.assertEqual(run("go~yāna").surface, "gavyāna")
        self.assertEqual(run("go-yāna").surface, "goyāna")

    def test_the_step_names_its_sutras(self):
        step = run("go~ya").outcomes[0].steps[0]
        self.assertEqual([v.sutra for v in step.detail.via],
                         ["1.1.66", "1.1.71", "1.3.10"])

    def test_the_vartikas_gavyuti(self):
        """Laghu: (अध्वपरिमाणे च) गव्यूतिः. The sense is a flag; the letters
        of *go-yūti* say nothing of it."""
        result = run("go-yūtiḥ{adhvaparimana}")
        self.assertEqual(result.surfaces, ("gavyūtis",))
        step = result.outcomes[0].steps[0]
        self.assertEqual(step.sutra, "6.1.79")
        self.assertEqual(step.detail.authority, VARTTIKA)
        self.assertEqual(step.detail.varttika, fam.VT_ADHVA)
        self.assertEqual(surfaces("go-yūtiḥ"), {"goyūtis"})

    def test_the_vedic_vartika_needs_the_veda(self):
        """गोर्यूतौ छन्दसि — आ नो मित्रावरुणा घृतैर्गव्यूतिमुक्षतम्."""
        self.assertEqual(surfaces("go-yūtim", veda=True), {"gavyūtim"})
        self.assertEqual(surfaces("go-yūtim"), {"goyūtim"})
        step = run("go-yūtim", veda=True).outcomes[0].steps[0]
        self.assertEqual(step.detail.varttika, fam.VT_GOR_YUTAU)

    def test_only_the_word_yuti_after_go(self):
        """The vārttika names *go* and *yūti*: not another word before yūti,
        not another word after go."""
        self.assertEqual(surfaces("go-yānam", veda=True), {"goyānam"})
        self.assertEqual(surfaces("aśva-yūtim", veda=True), {"aśvayūtim"})
        self.assertEqual(surfaces("viṣṇo-yūtim", veda=True), {"viṣṇoyūtim"})
        self.assertEqual(surfaces("nau-yūtim", veda=True), {"nauyūtim"})
        self.assertEqual(surfaces("nau-yūtiḥ{adhvaparimana}"), {"nauyūtis"})

    def test_the_v_is_not_lost_where_it_ends_a_pada(self):
        """Kaumudī: श्रूयमाणवकारान्त आदेशः स्यात् … वकारो न लुप्यत इति यावत्.
        With the whole rulebook, 8.3.19 would otherwise offer गयूतिः."""
        self.assertEqual(surfaces("go-yūtiḥ{adhvaparimana}", WITH_HAL),
                         {"gavyūtiḥ"})

    def test_without_that_reading_the_option_of_8_3_19_takes_it(self):
        """Take the refusal away and the Śākalya option offers गयूतिः too."""
        rules = without(WITH_HAL, "6.1.79", varttika=fam.GLOSS_V_NOT_LOST)
        self.assertEqual(
            surfaces("go-yūtiḥ{adhvaparimana}", rules),
            {"gavyūtiḥ", "gayūtiḥ"})

    def test_the_refusal_is_a_step_that_displaces_the_loss(self):
        result = run("go-yūtiḥ{adhvaparimana}", WITH_HAL)
        outcome = result.outcomes[0]
        self.assertEqual(ids(outcome)[:2], ["6.1.79", "6.1.79"])
        refusal = taken(outcome)[1]
        self.assertEqual(refusal.detail.kind, "pratiṣedha")
        self.assertEqual(refusal.before, refusal.after)
        self.assertEqual(refusal.detail.sthanin, "v")
        lost = [a for a in refusal.against if a.sutra == "8.3.19"]
        self.assertTrue(lost)
        self.assertIn("वकारो न लुप्यत इति यावत्", lost[0].why)

    def test_the_kaumudis_reading_is_the_sutras_own_and_not_a_varttika(self):
        """The Kaumudī reads 6.1.79's word *vānta*; that is not a vārttika, so
        the rule stays a sūtra's and only its key carries the Kaumudī's words."""
        rules = [r for r in fam.RULES if r.varttika == fam.GLOSS_V_NOT_LOST]
        self.assertEqual(len(rules), 1)
        self.assertEqual((rules[0].sutra, rules[0].authority), ("6.1.79", "sūtra"))
        step = next(s for s in taken(run("go-yūtim", WITH_HAL,
                                         veda=True).outcomes[0])
                    if s.detail.kind == "pratiṣedha")
        self.assertEqual(step.detail.authority, "sūtra")
        self.assertIn("श्रूयमाणवकारान्त", step.detail.note)

    def test_within_a_pada_the_v_needs_no_refusal(self):
        """Where the v does not end a pada (the affix case, `~`) 8.3.19 never
        reaches it, so the ādeśa's own step is all there is and the refusal is
        not made — it is made only where 8.3.19 would be offered."""
        outcome = run("go~yaḥ", WITH_VISARGA).outcomes[0]
        self.assertEqual(ids(outcome), ["6.1.79", "8.2.66", "8.3.15"])
        self.assertEqual(outcome.surface, "gavyaḥ")
        self.assertNotIn("pratiṣedha", [s.detail.kind for s in taken(outcome)])


class DhatostannimittasyaivaTests(unittest.TestCase):
    """6.1.80 — Kāśikā: लव्यम्। पव्यम्। अवश्यलाव्यम्। अवश्यपाव्यम्; not ओयते।
    औयत।; Bhāṣya: शङ्कव्यं दारु, पिचव्यः कार्पासः."""

    def test_a_dhatus_ec_caused_by_the_affix_takes_it(self):
        for given, done in (
                ("lo{dhatu:lū,tannimitta}~yam", "lavyam"),
                ("po{dhatu:pū,tannimitta}~yam", "pavyam"),
                ("avaśyalau{dhatu:lū,tannimitta}~yam", "avaśyalāvyam"),
                ("avaśyapau{dhatu:pū,tannimitta}~yam", "avaśyapāvyam")):
            result = run(given)
            self.assertEqual(result.surface, done, given)
            step = result.outcomes[0].steps[0]
            self.assertEqual(step.sutra, "6.1.79")
            self.assertIn("6.1.80", [v.sutra for v in step.detail.via])

    def test_a_dhatus_own_ec_is_left_and_the_niyama_is_a_step(self):
        """Kāśikā: उपोयते। औयत। लौयमानिः। पौयमानिः — the एच् belongs to the dhātu
        but the y-affix did not cause it (guṇa of āṅ + u, the augment's
        vṛddhi, the iñ's vṛddhi)."""
        for given in ("o{dhatu:ve}~yate", "au{dhatu:ve}~yata",
                      "lau{dhatu:lū}~yamāni", "pau{dhatu:pū}~yamāni"):
            result = run(given)
            self.assertEqual(result.surface, given.split("{")[0]
                             + given.split("}")[1].replace("~", ""))
            outcome = result.outcomes[0]
            self.assertEqual(ids(outcome), ["6.1.80"], given)
            step = outcome.steps[0]
            self.assertEqual(step.detail.kind, "pratiṣedha")
            self.assertIn("6.1.79", [a.sutra for a in step.against])

    def test_a_dhatu_flag_with_no_root_will_do_too(self):
        self.assertEqual(run("o{dhatu}~yate").surface, "oyate")
        self.assertEqual(run("lo{dhatu,tannimitta}~yam").surface, "lavyam")

    def test_the_niyama_does_not_reach_a_stem_that_is_no_dhatu(self):
        """धातोरिति किम्? प्रातिपदिकस्य नियमो मा भूत् — गव्यम्, बाभ्रव्यः, and
        the Bhāṣya's शङ्कव्यम्."""
        for given in ("go~yam", "bābhro~yaḥ", "śaṅko~yam"):
            self.assertEqual(ids(run(given).outcomes[0]), ["6.1.79"], given)

    def test_without_the_niyama_the_dhatus_own_ec_would_change(self):
        rules = without(MINE, "6.1.80")
        for given, done in (("o{dhatu:ve}~yate", "avyate"),
                            ("au{dhatu:ve}~yata", "āvyata"),
                            ("lau{dhatu:lū}~yamāni", "lāvyamāni")):
            self.assertEqual(surfaces(given, rules), {done}, given)


class Nipatanas(unittest.TestCase):

    def test_ksayya_and_jayya(self):
        """Kāśikā on 6.1.81: शक्यः क्षेतुं क्षय्यः। शक्यो जेतुं जय्यः."""
        for given, done in (("kṣe{dhatu:kṣi,shakyartha}~yaḥ", "kṣayyaḥ"),
                            ("je{dhatu:ji,shakyartha}~yaḥ", "jayyaḥ")):
            result = run(given)
            self.assertEqual(deviz(result.surface), deviz(done), given)
            step = result.outcomes[0].steps[0]
            self.assertEqual((step.sutra, step.detail.adesa), ("6.1.81", "ay"))
            self.assertIn("nipātana", step.detail.note)

    def test_the_sense_decides(self):
        """शक्यार्थ इति किम्? क्षेयं पापम्। जेयो वृषलः."""
        self.assertEqual(run("kṣe{dhatu:kṣi}~yam").surface, "kṣeyam")
        self.assertEqual(deviz(run("je{dhatu:ji}~yaḥ").surface), "jeyas")

    def test_only_the_named_roots(self):
        """Not a nipātana for every dhātu: चि has the sense and the affix but is
        not one of the two the sūtra names."""
        self.assertEqual(
            run("ce{dhatu:ci,shakyartha}~yam").surface, "ceyam")
        self.assertEqual(
            run("kre{dhatu:kṣi,krayartha}~yam").surface, "kreyam")

    def test_the_affix_is_yat_and_not_any_y(self):
        """6.1.81 names *yat*: the piece after the `~` is ya-. A y-initial
        piece that is not (yū-) is no yat."""
        self.assertEqual(
            run("kṣe{dhatu:kṣi,shakyartha}~yūtam").surface, "kṣeyūtam")

    def test_krayya(self):
        """Kāśikā on 6.1.82: क्रय्यो गौः। क्रय्यः कम्बलः; not क्रेयं नो
        धान्यम्, न चास्ति क्रय्यम् (Bhāṣya on 6.1.82)."""
        self.assertEqual(
            run("kre{dhatu:krī,krayartha}~yaḥ").surface, "krayyas")
        self.assertEqual(run("kre{dhatu:krī}~yam").surface, "kreyam")
        self.assertEqual(
            ids(run("kre{dhatu:krī,krayartha}~yaḥ").outcomes[0]), ["6.1.82"])

    def test_the_vedic_ones(self):
        """Kāśikā on 6.1.83: भय्यं किलासीत्। वत्सतरी प्रवय्या; not भेयम्।
        प्रवेयम्. The feminine of प्रवय्या is the flag `stri`."""
        self.assertEqual(
            surfaces("bhe{dhatu:bhī}~yam", veda=True), {"bhayyam"})
        self.assertEqual(
            surfaces("prave{dhatu:vī,stri}~yā", veda=True), {"pravayyā"})
        self.assertEqual(
            surfaces("prave{dhatu:vī}~yam", veda=True), {"praveyam"})
        self.assertEqual(surfaces("bhe{dhatu:bhī}~yam"), {"bheyam"})
        self.assertEqual(surfaces("prave{dhatu:vī,stri}~yā"), {"praveyā"})

    def test_the_vartikas_of_6_1_83(self):
        """हृदय्या उपसंख्यानम् (ह्रदय्या आपः); शरस्य च अवादेशो भवतीति वक्तव्यम्
        (Bhāṣya: शरव्याः, ह्रदव्याः आपः)."""
        self.assertEqual(surfaces("hṛde~yāḥ", veda=True), {"hṛdayyās"})
        self.assertEqual(surfaces("hrade~yāḥ", veda=True), {"hradayyās"})
        self.assertEqual(surfaces("śara~yā", veda=True), {"śaravyā"})
        self.assertEqual(surfaces("hrada~yāḥ", veda=True), {"hradavyās"})
        self.assertEqual(surfaces("hṛde~yāḥ"), {"hṛdeyās"})
        step = run("śara~yā", veda=True).outcomes[0].steps[0]
        self.assertEqual(step.detail.varttika, fam.VT_ARSA)

    def test_the_vartikas_name_their_stems_only(self):
        """शरस्य च, ह्रदस्य: the अ of *śara* and *hrada*, not of any stem in the
        Veda; हृदय्या: *hṛde* and *hrade*, not another एकार before यत्."""
        self.assertEqual(surfaces("aśva~yā", veda=True), {"aśvayā"})
        self.assertEqual(surfaces("kṛṣṇa~yā", veda=True), {"kṛṣṇayā"})
        self.assertEqual(surfaces("gṛhe~yāḥ", veda=True), {"gṛheyās"})

    def test_a_nipatana_needs_the_affix_the_tilde_says(self):
        """The affix is a piece of the same pada (`~`): the same letters as two
        words, or as a compound, have no yat."""
        for given in ("kṣe{dhatu:kṣi,shakyartha} yam",
                      "kṣe{dhatu:kṣi,shakyartha}-yam",
                      "kre{dhatu:krī,krayartha} yam"):
            self.assertEqual(run(given).outcomes[0].steps, (), given)
        self.assertEqual(surfaces("bhe{dhatu:bhī} yam", veda=True),
                         {"bheyam"})

    def test_a_nipatana_is_not_derived_by_6_1_78(self):
        """There is no vowel after the एच्, so 6.1.78 cannot have made it."""
        self.assertNotIn("6.1.78", ids(
            run("kṣe{dhatu:kṣi,shakyartha}~yaḥ").outcomes[0]))


# ---------------------------------------------------------------------------
# 8.2.23, 8.2.29 — and the vārttika यणः प्रतिषेधो वाच्यः
# ---------------------------------------------------------------------------


class Samyoganta(unittest.TestCase):
    """8.2.23, 8.2.29 and the vārttika. Both rules read the cluster that ENDS a
    piece (module docstring, item 2); the Kāśikā's own examples are the inputs."""

    def test_the_yan_at_the_end_of_a_cluster_is_not_lost(self):
        """Laghu: इति यलोपे प्राप्ते — यणः प्रतिषेधो वाच्यः; सुद्ध्युपास्यः."""
        for surface in surfaces("sudhī upāsya"):
            self.assertIn("dhy", surface)
            self.assertNotIn("sudhupāsya", surface)

    def test_the_refusal_is_a_step_of_the_vartika_and_names_what_it_refuses(self):
        outcome = run("sudhī upāsya").outcomes[0]
        self.assertEqual(ids(outcome)[:2], ["6.1.77", "8.2.23"])
        step = taken(outcome)[1]
        self.assertEqual(step.detail.kind, "pratiṣedha")
        self.assertEqual(step.detail.authority, VARTTIKA)
        self.assertEqual(step.detail.varttika, fam.VT_YANAH)
        self.assertEqual(step.before, step.after)
        self.assertIn("8.2.23", [a.sutra for a in step.against])
        self.assertIn("1.1.52", [v.sutra for v in step.detail.via])

    def test_it_is_made_once_and_not_again_after_the_doubling(self):
        """The doubling changes the sounds beside the य्; 8.2.1 shows 8.2.23 the
        row without it, and it has had its chance."""
        for outcome in run("sudhī upāsya").outcomes:
            self.assertEqual(ids(outcome).count("8.2.23"), 1, ids(outcome))

    def test_without_the_vartika_the_y_would_go(self):
        """Take the rule out: 8.2.23 takes off the य् (1.1.52) and the ध्, now
        at a pada's end, goes voiced by 8.2.39 — सुदुपास्य, which is not
        the Laghu's."""
        rules = without(WITH_HAL, "8.2.23", authority=VARTTIKA)
        result = run("sudhī upāsya", rules)
        self.assertEqual(result.surfaces, ("sudupāsya",))
        self.assertEqual(ids(result.outcomes[0]), ["6.1.77", "8.2.23", "8.2.39"])

    def test_every_yan_that_ends_a_cluster_is_kept(self):
        """The Kaumudī's four (सुद्ध्युपास्यः, मद्ध्वरिः, धात्रंशः, लाकृतिः's
        neighbours): the yaṇ stays the last sound of the first word in every
        form, and 8.2.23 is refused by the vārttika in each."""
        for given, yan in (("sudhī upāsya", "y"), ("madhu ari", "v"),
                           ("dhātṛ aṃśa", "r"), ("iti ādi", "y"),
                           ("pacati odanam", "y"), ("nahi asti", "y")):
            result = run(given)
            for outcome in result.outcomes:
                first = [s for s in outcome.final.segs if s.w == 0 and s.s]
                self.assertEqual(first[-1].s, yan, (given, outcome.surface))
                refusal = [s for s in taken(outcome) if s.sutra == "8.2.23"]
                self.assertEqual(len(refusal), 1, given)
                self.assertEqual(refusal[0].detail.kind, "pratiṣedha", given)

    def test_a_repha_before_the_yan_keeps_8_2_23_away_altogether(self):
        """8.2.24 रात्सस्य (Kāśikā: *रात् सस्यैव लोपो भवति, नान्यस्येति*): after a
        र् only a स् is lost, so 8.2.23 never reaches *hary* or *gaur* and the
        vārttika has nothing to refuse there. The र् of `samyoganta`'s own
        table of what blocks 8.2.23 is the project's record of the same."""
        from src.astadhyayi import samyoganta
        self.assertIn("8.2.23", samyoganta.provisions_for("8.2.24")[0].blocks)
        for given in ("hari anubhava", "gaurī au"):
            for outcome in run(given).outcomes:
                self.assertNotIn("8.2.23", ids(outcome), given)
        self.assertEqual(surfaces("hary"), {"hary"})

    def test_8_2_24_lets_the_s_after_a_repha_go(self):
        """Kāśikā on 8.2.24: गोभिरक्षाः — अक्षार्स् loses its स्; and the step
        cites 8.2.24 for it."""
        result = run("akṣārs")
        self.assertEqual(result.surfaces, ("akṣār",))
        step = taken(result.outcomes[0])[0]
        self.assertEqual(step.sutra, "8.2.23")
        self.assertIn("8.2.24", [v.sutra for v in step.detail.via])

    def test_a_repha_keeps_any_other_last_sound(self):
        """Kāśikā on 8.2.24: ऊर्जेः क्विप् — ऊर्क् (ऊर्ज्, not *ऊर्*)."""
        for outcome in run("ūrj", WITH_HAL).outcomes:
            self.assertNotIn("8.2.23", ids(outcome))
            # the र् stays; the ज् goes the way a pada's last palatal goes
            self.assertRegex(outcome.surface, "^ūr[gk]$")

    def test_8_2_23_takes_the_last_sound_of_a_pada_final_cluster(self):
        """Kāśikā on 8.2.23: गोमान्। यवमान्। कृतवान्। हतवान् — from the
        stage before (गोमान्त् …); by 1.1.52 the last sound only. The step is
        the sūtra's own, and 8.2.39's voicing of the त् does not get there
        first (8.2.23 stands before it, and 8.2.1 hides 8.2.39 from it)."""
        for given, done in (("gomānt", "gomān"), ("yavamānt", "yavamān"),
                            ("kṛtavānt", "kṛtavān"), ("hatavānt", "hatavān")):
            for rules in (MINE, WITH_HAL):
                result = run(given, rules)
                self.assertEqual(result.surfaces, (done,), given)
                self.assertEqual(ids(result.outcomes[0]), ["8.2.23"], given)
            step = taken(run(given).outcomes[0])[0]
            self.assertEqual(step.detail.kind, "lopa")
            self.assertEqual(step.detail.sthanin, "t")
            self.assertEqual([v.sutra for v in step.detail.via], ["1.1.52"])

    def test_without_8_2_23_the_t_of_gomant_would_be_voiced(self):
        rules = without(WITH_HAL, "8.2.23", authority="sūtra")
        # 8.2.39 voices the त्; 8.4.56 (वा अवसाने) then lets it be voiceless
        # again at a pause, so the pausal form is an option, not a fault.
        self.assertEqual(surfaces("gomānt", rules), {"gomānd", "gomānt"})

    def test_the_rutva_that_comes_later_does_not_displace_it(self):
        """Kāśikā: इह श्रेयान्, भूयानिति रुत्वं परमप्यसिद्धत्वात् संयोगान्तस्य
        लोपं न बाधते — the स् of श्रेयान्स् goes; the रु of 8.2.66 is not made."""
        for given, done in (("śreyāns", "śreyān"), ("bhūyāns", "bhūyān")):
            result = run(given, WITH_HAL)
            self.assertEqual(result.surfaces, (done,), given)
            self.assertEqual(ids(result.outcomes[0]), ["8.2.23"], given)

    def test_only_the_end_of_a_pada_is_a_samyoganta(self):
        """The cluster that ends a PIECE, before an affix (`~`), is no
        saṃyogānta pada; and the inside of a word is never read."""
        self.assertEqual(surfaces("gomānt~a"), {"gomānta"})
        self.assertEqual(surfaces("gomānt~a", WITH_HAL), {"gomānta"})
        for outcome in sandhi("rāmas gacchati").outcomes:
            self.assertIn("gacchati", outcome.surface)
            self.assertNotIn("8.2.23", ids(outcome))

    def test_the_kasika_refuses_8_2_29_for_the_same_reason(self):
        """Kāśikā on 8.2.29: वास्यर्थम्, काक्यर्थम् — the स् or क् at the head of
        the cluster is not lost either, the yaṇ being बहिरङ्ग."""
        for given, done in (("vāsī artham", "vāsyartham"),
                            ("kākī artham", "kākyartham")):
            result = run(given)
            self.assertEqual(result.surface, done, given)
            outcome = result.outcomes[0]
            self.assertIn("8.2.29", ids(outcome))
            step = next(s for s in taken(outcome) if s.sutra == "8.2.29")
            self.assertEqual(step.detail.kind, "pratiṣedha")
            self.assertEqual(step.before, step.after)
            self.assertIn("बहिरङ्ग", step.detail.because)

    def test_the_kasikas_refusal_holds_for_a_yan_the_caller_gave_too(self):
        """A finished pada has no other way to end in स्य् or क्य् than by a yaṇ,
        so a word given as *vāsy* is left as it is — and the refusal is a step."""
        for given, done in (("vāsy artham", "vāsyartham"),
                            ("kāky artham", "kākyartham")):
            result = run(given)
            self.assertEqual(result.surfaces, (done,), given)
            self.assertIn("8.2.29", ids(result.outcomes[0]), given)

    def test_8_2_29_takes_the_first_sound_of_a_pada_final_cluster(self):
        """Kāśikā on 8.2.29: तक्षेः — तट्; लस्जेः — साधुलक्; काष्ठतट् — the क् or
        स् at the head of the cluster goes, and not the last sound (which
        8.2.23 would take: तक्, not तष्). 8.2.29 is 8.2.23's exception here,
        by the Bālamanoramā's *न्याय्यत्वादिह संयोगादिलोप एव भवति*."""
        for given, done in (("takṣ", "taṣ"), ("bhṛsj", "bhṛj"),
                            ("sādhu-lasj", "sādhulaj"),
                            ("kāṣṭha-takṣ", "kāṣṭhataṣ")):
            result = run(given)
            self.assertEqual(result.surfaces, (done,), given)
            self.assertEqual(ids(result.outcomes[0]), ["8.2.29"], given)
            step = taken(result.outcomes[0])[0]
            self.assertEqual(step.detail.kind, "lopa")
            lost = [a for a in step.against if a.sutra == "8.2.23"]
            self.assertTrue(lost, given)
            self.assertIn("न्याय्यत्वादिह संयोगादिलोप एव भवति", lost[0].why)

    def test_without_the_exception_the_last_sound_would_go_instead(self):
        """Take 8.2.29 out and 8.2.23 takes the last sound: तक्, भृस् — which is
        not the Kāśikā's तट् and भृट्."""
        rules = without(MINE, "8.2.29")
        self.assertEqual(surfaces("takṣ", rules), {"tak"})
        self.assertEqual(surfaces("bhṛsj", rules), {"bhṛs"})

    def test_8_2_29_before_a_jhal(self):
        """Kāśikā: झलि परतो वा यः संयोगः — the स् of लस्ज् goes before the
        झल् त (लग्नः); the क् of तक्ष् before त (तष्टः)."""
        for given, done in (("lasj~ta", "lajta"), ("takṣ~ta", "taṣta")):
            result = run(given)
            self.assertEqual(result.surfaces, (done,), given)
            step = taken(result.outcomes[0])[0]
            self.assertEqual(step.sutra, "8.2.29")
            self.assertIn("jhal", step.detail.because)

    def test_the_x_iti_kims_of_8_2_29(self):
        """Kāśikā: अन्ते चेति किम्? तक्षिता। तक्षकः — a vowel follows the cluster
        and the piece goes on, so nothing is lost. स्कोरिति किम्? नर्नर्त्ति —
        a cluster that does not begin with स् or क् keeps its head."""
        self.assertEqual(surfaces("takṣ~ita"), {"takṣita"})
        self.assertEqual(surfaces("takṣ~aka"), {"takṣaka"})
        self.assertEqual(ids(run("narnart~ti").outcomes[0]), [])

    def test_the_site_of_8_2_29_is_what_it_reads_and_changes(self):
        """A place is every sound a rule reads or changes (README): before a
        झल्, that is the cluster and the झल् that is read; at a pada's end,
        the cluster alone."""
        from src.astadhyayi.sandhi.rule import site as make_site
        from src.astadhyayi.sandhi.segs import View
        for text, read in (("takṣ~ta", "kṣt"), ("takṣ", "kṣ")):
            state = parse(text)
            view = View(state, "8.2.29")
            apps = list(fam.skoh_samyogadyor_ante_ca.find(view))
            self.assertEqual(len(apps), 1, text)
            spelt = "".join(s.s for s in state.segs)
            start = spelt.index(read)
            reads = tuple(sorted(s.uid for s in state.segs[start:start + len(read)]))
            self.assertEqual(apps[0].site, reads, text)

    def test_the_kasika_words_of_8_2_29_are_the_corpus_words(self):
        self.assertIn(norm(fam._quote("skoh")),
                      norm(corpus.commentary_on("8.2.29", "kashika")))


# ---------------------------------------------------------------------------
# 8.4.46, 8.4.47 and the vārttika — the doubling; 8.4.51 (and 50, 52) — its option
# ---------------------------------------------------------------------------


class Dvitva(unittest.TestCase):

    def test_the_kasikas_and_kaumudis_examples_under_8_4_47(self):
        """Kāśikā on 8.4.47: दद्ध्यत्र। मद्ध्वत्र (the ध् said twice, and the
        first ध् a द् by 8.4.53); the vārttika: दध्य्यत्र, मध्व्वत्र."""
        for given, four in (
                ("dadhi atra", {"dadhyatra", "daddhyatra", "dadhyyatra",
                                "daddhyyatra"}),
                ("madhu atra", {"madhvatra", "maddhvatra", "madhvvatra",
                                "maddhvvatra"})):
            self.assertEqual(surfaces(given), four, given)

    def test_the_laghus_derivation_step_by_step(self):
        """Laghu: सुध्य् उपास्य — 8.4.47: सुध्ध्य् उपास्य — 8.4.53: सुद्ध्य् उपास्य,
        and 8.2.23, with 1.1.52, refused by the vārttika. The Laghu tells the
        refusal last; the engine takes the tripādī in the order 8.2.1 gives it,
        and 8.2.23 stands before 8.4.47 and 8.4.53, so its refusal is the
        first step after the yaṇ. The sūtras, in order."""
        result = run("sudhī upāsya")
        outcome = outcome_of(result, "suddhyupāsya")
        done = ids(outcome)
        self.assertTrue(in_order(["6.1.77", "8.2.23", "8.4.47", "8.4.53"],
                                 done), done)
        by = {s.sutra: s for s in taken(outcome)}
        self.assertEqual(by["8.4.47"].before, "sudhy upāsya")
        self.assertEqual(by["8.4.47"].after, "sudhdhy upāsya")
        self.assertEqual(by["8.4.53"].before, "sudhdhy upāsya")
        self.assertEqual(by["8.4.53"].after, "suddhy upāsya")
        self.assertEqual(by["8.4.53"].detail.adesa, "d")

    def test_the_kaumudis_four_forms_of_sudhi_upasya(self):
        """Kaumudī on 8.2.23: तदिह धकारयकारयोर्द्वित्वविकल्पाच्चत्वारि रूपाणि —
        ध् and य् each doubled or not."""
        self.assertEqual(
            surfaces("sudhī upāsya"),
            {"sudhyupāsya", "suddhyupāsya", "sudhyyupāsya", "suddhyyupāsya"})

    def test_the_kaumudis_madhu_ari(self):
        """Kaumudī: मद्ध्वरिः (the GRETIL Laghu prints *maddhariḥ*, a letter
        short)."""
        got = surfaces("madhu ari")
        self.assertIn("maddhvari", got)
        self.assertEqual(got, {"madhvari", "maddhvari", "madhvvari",
                               "maddhvvari"})
        self.assertEqual(
            ids(outcome_of(run("madhu ari"), "maddhvari"))[-1], "8.4.53")

    def test_8_4_46_needs_a_vowel_before_the_r_or_h(self):
        """*अचः पराभ्याम्* — the र् or ह् must itself follow a vowel: in *hrī +
        atra* the र् follows the ह्, so its य् is not doubled by 8.4.46 (and no
        मय् stands before it for the vārttika)."""
        self.assertEqual(surfaces("hrī atra"), {"hryatra"})
        self.assertEqual(surfaces("hari atra"), {"haryatra", "haryyatra"})

    def test_the_r_and_h_of_8_4_46_are_never_doubled_themselves(self):
        """Kaumudī: हर्य्यनुभवः। नह्य्यस्ति; Laghu: गौर्य्यौ. The यर् after them is
        doubled, and they are the cause, not the sthānin."""
        for given, forms in (
                ("hari anubhava", {"haryanubhava", "haryyanubhava"}),
                ("nahi asti", {"nahyasti", "nahyyasti"}),
                ("gaurī au", {"gauryau", "gauryyau"})):
            got = surfaces(given)
            self.assertEqual(got, forms, given)
            for surface in got:
                self.assertNotIn("rry", surface)
                self.assertNotIn("hhy", surface)

    def test_8_4_46_is_the_sutra_of_the_doubling_after_r_and_h(self):
        outcome = outcome_of(run("hari anubhava"), "haryyanubhava")
        step = next(s for s in taken(outcome) if s.sutra == "8.4.46")
        self.assertEqual(step.detail.kind, "dvitva")
        self.assertEqual((step.before, step.after),
                         ("hary anubhava", "haryy anubhava"))
        self.assertEqual([v.sutra for v in step.detail.via], ["1.1.67"])

    def test_the_second_reading_of_yano_mayo_dve_is_a_varttika_step(self):
        outcome = outcome_of(run("dadhi atra"), "dadhyyatra")
        step = next(s for s in taken(outcome)
                    if s.detail.varttika == fam.VT_MAYO)
        self.assertEqual(step.sutra, "8.4.47")
        self.assertEqual(step.detail.authority, VARTTIKA)
        self.assertEqual((step.before, step.after),
                         ("dadhy atra", "dadhyy atra"))

    def test_the_t_of_dhatr_amsah_is_doubled_and_the_r_is_not(self):
        """Bālamanoramā on 8.2.23: अत्र तकारस्यैव द्वित्वं न तु रेफस्य;
        Tattvabodhinī: तकारस्य तु द्वित्वं भवत्येव. तच्च वेत्यतो रूपद्वयम्."""
        self.assertEqual(surfaces("dhātṛ aṃśa"),
                         {"dhātraṃśa", "dhāttraṃśa"})

    def test_iti_adi_keeps_its_first_form(self):
        """The README: `sandhi("iti ādi").surface` is ityādi. The option that
        comes first is Śākalya's, no doubling; the doubled forms follow."""
        result = run("iti ādi")
        self.assertEqual(result.surface, "ityādi")
        self.assertEqual(
            set(result.surfaces),
            {"ityādi", "ityyādi", "ittyādi", "ittyyādi"})

    def test_each_doubling_is_its_own_option(self):
        """Neither is offered until the other is settled at that place, so all
        four of the Kaumudī's forms come and none is forced by another."""
        result = run("sudhī upāsya")

        def the_dh_doubled(o):
            return any(s.sutra == "8.4.47" and not s.detail.varttika
                       for s in taken(o))

        def the_y_doubled(o):
            return any(s.detail.varttika == fam.VT_MAYO for s in taken(o))

        pairs = {(the_dh_doubled(o), the_y_doubled(o))
                 for o in result.outcomes}
        self.assertEqual(pairs, {(False, False), (True, False),
                                 (False, True), (True, True)})

    def test_each_course_is_one_derivation_and_none_is_made_twice(self):
        """The doubling of the ध् and of the य् are offered in turn, so a course
        is not found twice by two routes: for *sudhī upāsya* the ध् is left
        single (and the य् is left, or doubled and then kept or lost), or the
        ध् is doubled (and the same three for the य्) — six derivations, every
        one different. For *hari anubhava* only the य् is a place: three."""
        for given, count in (("sudhī upāsya", 6), ("hari anubhava", 3),
                             ("madhu atra", 6)):
            result = run(given)
            self.assertEqual(len(result.outcomes), count, given)
            courses = {tuple((s.sutra, s.declined, s.detail.varttika)
                             for s in o.steps) for o in result.outcomes}
            self.assertEqual(len(courses), count, given)

    def test_a_finished_words_own_consonants_are_not_doubled(self):
        """The engine acts at junctions and at sounds a step made; अर्कः,
        गच्छति, अग्नि stay as they were."""
        self.assertEqual(surfaces("arka atra", WITH_EKADESA), {"arkātra"})
        for outcome in sandhi("rāmas gacchati").outcomes:
            self.assertIn("gacchati", outcome.surface)
        # agni's own g and n are not doubled; only the य् the yaṇ made, after
        # the मय् न् (the vārttika), is.
        self.assertEqual(surfaces("agni atra"), {"agnyatra", "agnyyatra"})

    def test_a_plain_junction_is_not_doubled(self):
        """SCOPE (COVERAGE, 8.4.46): दुर्ल्लभः, कुर्म्मः are the Kāśikā's, and
        need doubling across any junction; the engine offers it only beside the
        yaṇ. A test that would fail the day it is widened."""
        self.assertEqual(surfaces("dur labha"), {"durlabha"})
        self.assertEqual(surfaces("kur ma"), {"kurma"})

    def test_a_pause_does_not_double_a_final_consonant(self):
        """SCOPE: the vārttika अवसाने च यरो द्वे (वाक्क्, षट्ट्)."""
        self.assertEqual(surfaces("vāk"), {"vāk"})
        self.assertEqual(surfaces("ṣaṭ"), {"ṣaṭ"})

    def test_the_x_iti_kims_of_8_4_47(self):
        """अच इत्येव — स्मितम्। ध्मातम्: no vowel before, no doubling."""
        self.assertEqual(surfaces("smitam"), {"smitam"})
        self.assertEqual(surfaces("dhmātam"), {"dhmātam"})

    def test_a_consonant_before_the_yan_is_not_doubled_unless_a_vowel_stands_before(self):
        """A यर् not after a vowel is not 8.4.47's (*अचः परस्य*): the व् of
        *tvī + atra* stands after the consonant त् and after no vowel, and no
        मय् before it makes the vārttika's case either, so it is not doubled."""
        self.assertEqual(surfaces("tvī atra"), {"tvyatra"})

    def test_sibilants_before_a_yan_are_doubled_like_any_other_yar(self):
        """वास्यर्थम् has the स् after a vowel and before a non-vowel."""
        self.assertEqual(surfaces("vāsī artham"),
                         {"vāsyartham", "vāssyartham"})


class TheTeachers(unittest.TestCase):
    """8.4.50 (Śākaṭāyana), 8.4.51 (Śākalya), 8.4.52 (the ācāryas): each says
    there is no doubling, in its domain; the union of what any of them allows,
    with Pāṇini's own doubling, is both forms."""

    def test_sakalyas_option_is_the_first_course_and_the_others_follow(self):
        result = run("sudhī upāsya")
        first = result.outcomes[0]
        self.assertEqual(first.surface, "sudhyupāsya")
        self.assertEqual(ids(first).count("8.4.51"), 2)
        self.assertNotIn("8.4.47", ids(first))
        self.assertEqual(first.choices, (("8.4.51", True), ("8.4.51", True)))

    def test_the_step_is_an_optional_refusal_with_its_reason(self):
        step = next(s for s in taken(run("sudhī upāsya").outcomes[0])
                    if s.sutra == "8.4.51")
        self.assertEqual(step.detail.kind, "pratiṣedha")
        self.assertEqual(step.option, "शाकल्यस्य")
        self.assertEqual(step.before, step.after)
        against = [a for a in step.against if a.sutra == "8.4.47"]
        self.assertTrue(against)
        self.assertIn("सर्वत्र द्विर्वचनं न भवति", against[0].why)

    def test_the_declined_course_says_it_declined_and_then_doubles(self):
        outcome = outcome_of(run("sudhī upāsya"), "suddhyupāsya")
        declined = [s for s in outcome.steps if s.declined]
        self.assertTrue(declined)
        self.assertEqual({s.sutra for s in declined}, {"8.4.51"})
        for note in declined:
            self.assertEqual(note.before, note.after)

    def test_without_sakalya_nothing_would_be_undoubled(self):
        """The option is 8.4.51's: take it out and the doubling is
        unconditional — no undoubled form survives."""
        rules = without(MINE, "8.4.51")
        got = surfaces("sudhī upāsya", rules)
        self.assertNotIn("sudhyupāsya", got)
        self.assertNotIn("sudhyyupāsya", got)
        self.assertIn("suddhyupāsya", got)

    def test_sakatayanas_cluster_of_three_is_cited(self):
        """Kāśikā on 8.4.50: त्रिप्रभृतिषु वर्णेषु संयुक्तेषु … — भक्त्य् has the
        three क्त्य्, and the य् is the sound the vārttika doubles after the
        मय् त्; Śākaṭāyana would not double it there."""
        step = next(s for s in taken(run("bhakti atra").outcomes[0])
                    if s.sutra == "8.4.51")
        self.assertIn("8.4.50", [v.sutra for v in step.detail.via])

    def test_a_cluster_of_two_does_not_cite_him(self):
        step = next(s for s in taken(run("sudhī upāsya").outcomes[0])
                    if s.sutra == "8.4.51")
        self.assertNotIn("8.4.50", [v.sutra for v in step.detail.via])

    def test_the_doubling_does_not_count_towards_his_three(self):
        """After the ध् is doubled the row has three consonants together, but
        the conjunct the word has is two."""
        outcome = outcome_of(run("sudhī upāsya"), "suddhyupāsya")
        for step in taken(outcome):
            if step.sutra == "8.4.51":
                self.assertNotIn("8.4.50", [v.sutra for v in step.detail.via])

    def test_the_acaryas_long_vowel_is_cited(self):
        """Kāśikā on 8.4.52: दीर्घादुत्तरस्याचार्याणां … — धात्रंशः has the त्
        after आ."""
        step = next(s for s in taken(run("dhātṛ aṃśa").outcomes[0])
                    if s.sutra == "8.4.51")
        self.assertIn("8.4.52", [v.sutra for v in step.detail.via])

    def test_a_short_vowel_does_not_cite_them(self):
        step = next(s for s in taken(run("dadhi atra").outcomes[0])
                    if s.sutra == "8.4.51")
        self.assertNotIn("8.4.52", [v.sutra for v in step.detail.via])

    def test_the_union_is_both_forms_in_every_domain(self):
        for given, undoubled, doubled in (
                ("dhātṛ aṃśa", "dhātraṃśa", "dhāttraṃśa"),
                ("bhakti atra", "bhaktyatra", "bhaktyyatra"),
                ("dadhi atra", "dadhyatra", "daddhyatra")):
            got = surfaces(given)
            self.assertIn(undoubled, got, given)
            self.assertIn(doubled, got, given)

    def test_the_teacher_rules_that_are_not_forks_have_no_rule(self):
        """8.4.50 and 8.4.52 are cited in the step of 8.4.51, not made forks."""
        self.assertEqual(
            sorted(r.sutra for r in fam.RULES
                   if r.sutra in ("8.4.50", "8.4.51", "8.4.52")),
            ["8.4.51"])


# ---------------------------------------------------------------------------
# 8.4.53, 8.4.64
# ---------------------------------------------------------------------------


class JhalamJasJhasi(unittest.TestCase):

    def test_the_kasikas_examples(self):
        """Kāśikā on 8.4.53: लब्धा। दोग्धा। बोद्धा — given as the forms 8.2.40 has
        left them, धा after the stem."""
        for given, done in (("labh~dhā", "labdhā"), ("dogh~dhā", "dogdhā"),
                            ("bodh~dhā", "boddhā"), ("labh~dhum", "labdhum"),
                            ("bodh~dhavyam", "boddhavyam")):
            result = run(given)
            self.assertEqual(result.surface, done, given)
            step = result.outcomes[0].steps[0]
            self.assertEqual(step.sutra, "8.4.53")
            self.assertEqual(
                [v.sutra for v in step.detail.via], ["1.1.66", "1.1.50"])

    def test_the_counter_examples(self):
        """झशीति किम्? दत्तः। दत्थः। दध्मः — a झल् before a non-झश् stands."""
        for given in ("dat~taḥ", "dat~thaḥ", "dadh~maḥ"):
            self.assertEqual(ids(run(given).outcomes[0]), [], given)

    def test_it_agrees_with_the_projects_own_question_and_with_1_1_50(self):
        """`anga.jhalam_jas_jhasi` is the sūtra as a question; the step says the
        sound it says, for every झल् before every झश्."""
        jhal, jhas = sorted(S.members("jhaL")), sorted(S.members("jhaś"))
        jas = tuple(sorted(S.members("jaŚ")))
        checked = 0
        for a in jhal:
            for b in jhas:
                asked = jhalam_jas_jhasi(a + b)
                self.assertEqual(asked.now if asked.result else None,
                                 (S.nearest(a, jas)
                                  if S.nearest(a, jas) not in (None, a)
                                  else None), (a, b))
                checked += 1
        self.assertGreater(checked, 200)

    def test_the_first_dh_of_a_doubled_dh_is_the_one_that_changes(self):
        step = next(s for s in taken(outcome_of(run("dadhi atra"),
                                                "daddhyatra"))
                    if s.sutra == "8.4.53")
        self.assertEqual((step.before, step.after),
                         ("dadhdhy atra", "daddhy atra"))

    def test_a_jas_before_a_jhas_stays(self):
        self.assertEqual(ids(run("dad~dhā").outcomes[0]), [])


class AbhyaseCarca(unittest.TestCase):
    """8.4.54 अभ्यासे चर्च — Kāśikā: चिखनिषति। चिच्छित्सति। टिठकारयिषति। तिष्ठासति।
    पिफकारयिषति। बुभूषति। जिघत्सति। डुढौकिषते; प्रकृतिचरां प्रकृतिचरो भवन्ति —
    चिचीषति। टिटीकिषते। तितनिषति; प्रकृतिजशां प्रकृतिजशो भवन्ति — जिजनिषते।
    बुबुधे। ददौ। डिड्ये.

    The engine builds no reduplicate, so the piece that is the अभ्यास is given
    by the caller, flagged `abhyasa`, in front of a `~`."""

    def test_the_kasikas_examples(self):
        for given, done in (
                ("chi{abhyasa}~khaniṣati", "cikhaniṣati"),
                ("chi{abhyasa}~chitsati", "cichitsati"),
                ("ṭhi{abhyasa}~ṭhakārayiṣati", "ṭiṭhakārayiṣati"),
                ("thi{abhyasa}~ṣṭhāsati", "tiṣṭhāsati"),
                ("phi{abhyasa}~phakārayiṣati", "piphakārayiṣati"),
                ("bhu{abhyasa}~bhūṣati", "bubhūṣati"),
                ("jhi{abhyasa}~ghatsati", "jighatsati"),
                ("ḍhu{abhyasa}~ḍhaukiṣate", "ḍuḍhaukiṣate"),
                ("bha{abhyasa}~bhūva", "babhūva")):
            result = run(given)
            self.assertEqual(result.surfaces, (done,), given)
            self.assertEqual(ids(result.outcomes[0]), ["8.4.54"], given)

    def test_a_sound_that_is_already_a_car_or_a_jas_stays(self):
        """प्रकृतिचरां प्रकृतिचरो भवन्ति, प्रकृतिजशां प्रकृतिजशः — no step at all."""
        for given, done in (("ci{abhyasa}~cīṣati", "cicīṣati"),
                            ("ṭi{abhyasa}~ṭīkiṣate", "ṭiṭīkiṣate"),
                            ("ti{abhyasa}~tanuṣati", "titanuṣati"),
                            ("ji{abhyasa}~janiṣate", "jijaniṣate"),
                            ("bu{abhyasa}~budhe", "bubudhe"),
                            ("da{abhyasa}~dau", "dadau"),
                            ("ḍi{abhyasa}~ḍye", "ḍiḍye")):
            result = run(given)
            self.assertEqual(result.surfaces, (done,), given)
            self.assertEqual(result.outcomes[0].steps, (), given)

    def test_it_is_the_flag_that_says_the_piece_is_the_abhyasa(self):
        """The same letters with no flag are a finished word and a stem: the
        engine does not guess that *bha* is a reduplicate."""
        self.assertEqual(run("bha~bhūva").surface, "bhabhūva")
        self.assertEqual(run("bha~bhūva").outcomes[0].steps, ())

    def test_the_step_says_which_sound_and_what_it_became(self):
        step = run("thi{abhyasa}~ṣṭhāsati").outcomes[0].steps[0]
        self.assertEqual((step.detail.sthanin, step.detail.adesa), ("th", "t"))
        self.assertEqual((step.before, step.after),
                         ("thi ṣṭhāsati", "ti ṣṭhāsati"))

    def test_it_is_asked_of_the_projects_question_not_of_the_nearest(self):
        """`anga.abhyase_car` answers by varga; 1.1.50's nearest of चर् and जश्
        to थ् is स् (both dental), and तितनिषति — the vṛtti's own form —
        needs the त्: so the rule takes the project's answer."""
        from src.astadhyayi.anga import abhyase_car
        self.assertEqual(abhyase_car("thi").result, "ti")
        self.assertEqual(S.nearest("th", tuple(sorted(
            S.members("caR") | S.members("jaŚ")))), "s")
        self.assertEqual(run("thi{abhyasa}~ṣṭhāsati").surface, "tiṣṭhāsati")

    def test_the_base_is_left_alone(self):
        """Only the piece flagged is the abhyāsa: the aspirate of the base
        keeps its aspiration (*bubhūṣati*, not *bubbūṣati*)."""
        self.assertEqual(run("bhu{abhyasa}~bhūṣati").surface, "bubhūṣati")


class HaloYamamYamiLopah(unittest.TestCase):

    def test_the_first_of_two_yams_after_a_hal_may_be_lost(self):
        """Kāśikā on 8.4.64: शय्या, शय्य्या — the doubled य् after the hal.
        Here the yy of सुध्य्य्: the option that takes it comes first."""
        result = run("sudhī upāsya")
        lost = [o for o in result.outcomes
                if o.surface == "suddhyupāsya" and "8.4.64" in ids(o)]
        self.assertTrue(lost)
        step = next(s for s in taken(lost[0]) if s.sutra == "8.4.64")
        self.assertEqual(step.option, "अन्यतरस्याम्")
        self.assertEqual(step.detail.kind, "lopa")
        self.assertEqual((step.before, step.after),
                         ("suddhyy upāsya", "suddhy upāsya"))
        self.assertEqual([v.sutra for v in step.detail.via], ["1.1.66", "1.3.10"])

    def test_both_courses_are_returned(self):
        """अन्यतरस्याम् — the loss or no loss: सुद्ध्युपास्य and सुद्ध्य्युपास्य."""
        got = surfaces("sudhī upāsya")
        self.assertIn("suddhyupāsya", got)
        self.assertIn("suddhyyupāsya", got)

    def test_gauryyau_may_lose_the_doubled_y(self):
        result = run("gaurī au")
        lost = [o for o in result.outcomes
                if o.surface == "gauryau" and "8.4.64" in ids(o)]
        self.assertTrue(lost)

    def test_without_the_rule_the_doubled_y_would_always_stay(self):
        got = surfaces("gaurī au", without(MINE, "8.4.64"))
        self.assertEqual(got, {"gauryau", "gauryyau"})
        # ... and the two forms come from the doubling's option alone
        for outcome in run("gaurī au", without(MINE, "8.4.64")).outcomes:
            self.assertNotIn("8.4.64", ids(outcome))

    def test_hal_iti_kim_a_yam_after_a_vowel_stays(self):
        """हल इति किम्? अन्नम् — the first न् has a vowel before it."""
        state = parse("ka~nna", pause=False)
        segs = [replace(s, made_by="8.4.47") if s.s == "n" else s
                for s in state.segs]
        outcome = derive(replace(state, segs=tuple(segs)),
                         (next(r for r in MINE if r.sutra == "8.4.64"),))[0]
        self.assertEqual(outcome.steps, ())
        self.assertEqual(outcome.surface, "kanna")

    def test_it_takes_the_yam_after_a_hal(self):
        state = parse("ka~rnna", pause=False)
        segs = [replace(s, made_by="8.4.47") if s.s == "n" else s
                for s in state.segs]
        outcome = derive(replace(state, segs=tuple(segs)),
                         (next(r for r in MINE if r.sutra == "8.4.64"),))
        self.assertEqual(sorted(o.surface for o in outcome),
                         ["karna", "karnna"])

    def test_yami_iti_kim_a_yam_before_a_non_yam_stays(self):
        """यमीति किम्? शार्ङ्गम् — the ङ् is before ग्, which is no yam."""
        state = parse("śārṅ~ga", pause=False)
        segs = [replace(s, made_by="8.4.47") if s.s == "ṅ" else s
                for s in state.segs]
        outcome = derive(replace(state, segs=tuple(segs)),
                         (next(r for r in MINE if r.sutra == "8.4.64"),))[0]
        self.assertEqual(outcome.steps, ())

    def test_each_yam_is_lost_before_the_yam_of_its_own_kind(self):
        """Kaumudī: यमां यमीति यथासङ्ख्यविज्ञानान्नेह । माहात्म्यम् — the म् of
        *māhātmya* (महात्म + ण्य) stands after a हल् and before a यम् (the य्), and
        keeps its place, because the yam it may go before is a म्."""
        for given, steps in (("ka~rmya", []), ("ka~rnya", []),
                             ("ka~rmma", ["8.4.64"])):
            state = parse(given, pause=False)
            segs = [replace(s, made_by="8.4.47") if s.s in ("m", "n") else s
                    for s in state.segs]
            outcome = derive(replace(state, segs=tuple(segs)),
                             (next(r for r in MINE if r.sutra == "8.4.64"),))[0]
            self.assertEqual(ids(outcome), steps, given)

    def test_the_yams_of_finished_words_are_left_alone(self):
        self.assertEqual(surfaces("kur~maḥ"), {"kurmas"})
        self.assertEqual(ids(run("ādity~ya").outcomes[0]), [])


# ---------------------------------------------------------------------------
# The whole: the Laghu's lines, and the properties the engine promises
# ---------------------------------------------------------------------------


class LaghuLines80To99(unittest.TestCase):
    """Laghusiddhāntakaumudī, the lines on 6.1.77–79 and 8.4.46. Run with the
    whole rulebook, so that the visarga and the rest of the junction are done."""

    def surfaces(self, text, **kw):
        return set(sandhi(text, **kw).surfaces)

    def test_sudhi_upasyah(self):
        self.assertIn("suddhyupāsyaḥ", self.surfaces("sudhī upāsyaḥ"))

    def test_maddhvarih(self):
        self.assertIn("maddhvariḥ", self.surfaces("madhu ariḥ"))

    def test_dhatramsah(self):
        self.assertIn("dhātraṃśaḥ", self.surfaces("dhātṛ aṃśaḥ"))

    def test_lakrtih(self):
        self.assertIn("lākṛtiḥ", self.surfaces("ḷ ākṛtiḥ"))

    def test_the_four_of_yathasamkhya(self):
        for given, done in (("hare~e", "haraye"), ("viṣṇo~e", "viṣṇave"),
                            ("nai~akaḥ", "nāyakaḥ"), ("pau~akaḥ", "pāvakaḥ")):
            self.assertIn(done, self.surfaces(given), given)

    def test_gavyam_navyam_gavyutih(self):
        self.assertIn("gavyam", self.surfaces("go~yam"))
        self.assertIn("nāvyam", self.surfaces("nau~yam"))
        self.assertIn("gavyūtiḥ",
                      self.surfaces("go-yūtiḥ{adhvaparimana}"))

    def test_gauryyau(self):
        self.assertIn("gauryyau", self.surfaces("gaurī au"))

    def test_hare_iha_is_the_laghus_own_illustration_of_8_2_1(self):
        """हरये: 6.1.78, and the य् may go by 8.3.19 — where the two vowels
        then stand apart and 6.1.87 does not join them."""
        got = self.surfaces("hare iha")
        self.assertIn("harayiha", got)
        self.assertIn("haraiha", got)          # the two vowels, side by side

    def test_vapyasvah_is_derived_though_its_vartika_is_not_modelled(self):
        """Laghu: (न समासे) वाप्यश्वः. OPEN (module docstring): the sources do
        not say which doubling it forbids, so it is not a rule; the form is
        derived and comes first."""
        result = sandhi("vāpī-aśvaḥ")
        self.assertIn("vāpyaśvaḥ", result.surfaces)
        self.assertIn("6.1.77", ids(outcome_of(result, "vāpyaśvaḥ")))


class EngineProperties(unittest.TestCase):

    def test_the_first_form_is_every_option_taken_and_is_the_undoubled_one(self):
        for given, first in (("iti ādi", "ityādi"), ("dadhi atra", "dadhyatra"),
                             ("madhu ari", "madhvari"),
                             ("hari anubhava", "haryanubhava")):
            result = run(given)
            self.assertEqual(result.surface, first, given)
            self.assertTrue(all(c[1] for c in result.outcomes[0].choices))

    def test_devanagari_and_iast_give_the_same_derivation(self):
        for latin, deva in (("sudhī upāsya", "सुधी उपास्य"),
                            ("madhu ari", "मधु अरि"),
                            ("hari anubhava", "हरि अनुभव")):
            self.assertEqual(
                [ids(o) for o in run(latin).outcomes],
                [ids(o) for o in run(deva).outcomes])
            self.assertEqual(run(latin).surfaces, run(deva).surfaces)

    def test_the_result_serialises_and_prints_in_both_scripts(self):
        import json
        result = run("sudhī upāsya")
        json.dumps(result.to_dict(), ensure_ascii=False)
        self.assertIn("सुद्ध्युपास्य (suddhyupāsya)", result.trace())
        self.assertIn("संयोगान्तस्य लोपः (saṃyogāntasya lopaḥ)", result.trace())
        self.assertIn("[vārttika]", result.trace())

    def test_every_meeting_of_an_ik_with_a_vowel_after_a_consonant_terminates(self):
        """The doubling and its options, every ik before every vowel, after
        each kind of consonant: no cycle, no cap, sounds only."""
        from src.astadhyayi.varna import SVARA
        for before in ("dh", "t", "r", "h", "s", "k", "m", "y", "st"):
            for ik in ("i", "ī", "u", "ū", "ṛ", "ḷ"):
                for after in ("a", "ā", "i", "u", "e", "ai", "o", "au"):
                    result = run(f"ka{before}{ik} {after}ta")
                    self.assertTrue(result.outcomes)
                    for outcome in result.outcomes:
                        self.assertNotIn("cycling", outcome.stopped)
                        self.assertNotIn("cap", outcome.stopped)
                        for seg in outcome.final.segs:
                            self.assertTrue(seg.s == "" or seg.s in SVARA
                                            or seg.s.isalpha() or seg.s in
                                            ("ṃ", "ḥ"), seg.s)

    def test_a_derivation_stays_in_the_millisecond_range(self):
        """The fastest of ten runs, so that a busy machine does not decide."""
        import time
        sandhi("sudhī upāsya")                   # warm the caches
        best = float("inf")
        for _ in range(10):
            began = time.perf_counter()
            sandhi("sudhī upāsya")
            best = min(best, time.perf_counter() - began)
        self.assertLess(best, 0.25, best)

    def test_the_result_does_not_depend_on_how_often_it_is_asked(self):
        first = run("dadhi atra")
        again = run("dadhi atra")
        self.assertEqual(first.surfaces, again.surfaces)
        self.assertEqual([ids(o) for o in first.outcomes],
                         [ids(o) for o in again.outcomes])

    def test_the_vedic_rules_are_off_without_the_veda(self):
        for given in ("bhe{dhatu:bhī}~yam", "hṛde~yāḥ", "śara~yā",
                      "go-yūtim"):
            self.assertEqual(
                run(given).outcomes[0].steps, (), given)


if __name__ == "__main__":
    unittest.main()
