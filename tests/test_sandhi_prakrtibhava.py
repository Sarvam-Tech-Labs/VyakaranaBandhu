# -*- coding: utf-8 -*-
"""
The prakṛtibhāva family of the sandhi engine — pragṛhya, pluta, and the sounds
that refuse sandhi (1.1.11–19, 1.4.56–60, 6.1.115–131, 8.2.82–107, 8.3.33,
8.4.57) — and `infer.py`, which fills in only what a closed class proves.

**What the expectations are.** The commentaries' own worked examples, each with
its source named in the test's docstring, and the counter-examples they give
(*X iti kim?*). Where a result could come out right by luck the test also
asserts the STEPS — the sūtra ids, in order — so a rule that gets the right
string by the wrong road fails. Every test can fail: several are written as
*controls* (the same input without the flag that makes the difference) so that
a rule which fired everywhere, or nowhere, would be caught.

**What is asserted about.** The family's own rules and results. The rest of the
rulebook is loaded, as it is in real use, but nothing is asserted about
another family's steps except that they are not in the way.
"""

from __future__ import annotations

import json
import time
import unittest

from src.astadhyayi import corpus
from src.astadhyayi.sandhi import rulebook, trace
from src.astadhyayi.sandhi import sandhi as _sandhi
from src.astadhyayi.sandhi.families import prakrtibhava as family
from src.astadhyayi.sandhi.harness import joined
from src.astadhyayi.sandhi.infer import (
    CADI, PRADI, SVARADI, gana_words, infer_flags, nipata_source)
from src.astadhyayi.sandhi.parse import parse
from src.astadhyayi.sandhi.segs import (
    AC, PLUTA, PRAKRTYA, Seg, View, base_of)
from src.astadhyayi.prakrtibhava import stands_open


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

#: What the expectations below are derived with: this family and the families
#: of vowel and visarga sandhi it stands among, without their consonant rules
#: (below) and without the consonant families (which assimilate and nasalise
#: what a junction leaves). A form here is then what the commentary prints and
#: does not change when another family is added; `WholeRulebook` shows that
#: this family's own steps are the same with every family loaded.
NEIGHBOURS = ("ac_ekadesa", "ac_yan_ayadi", "prakrtibhava", "visarga_ru")


#: `ac_yan_ayadi` also carries consonant rules of the tripādī (the loss of a
#: final cluster, ṇatva, doubling: 8.2.23, 8.2.29, 8.4.x). They turn a form the
#: commentary prints once — *दध्यत्र* — into several. Not this family's, and
#: not what it is tested against: only that family's rules of the sixth
#: adhyāya are kept.
def _rules():
    kept = []
    for name in NEIGHBOURS:
        for r in rulebook.by_family()[name]:
            if name == "ac_yan_ayadi" and not r.sutra.startswith("6."):
                continue
            kept.append(r)
    return tuple(sorted(kept, key=lambda r: (r.order, r.varttika, r.name)))


def sandhi(text, **kw):
    kw.setdefault("rules", _rules())
    return _sandhi(text, **kw)


def outcomes(text, **kw):
    return sandhi(text, **kw).outcomes


def forms(text, **kw):
    """Every form the grammar allows, joined (no spaces, avagraha as ')."""
    return {joined(o.text()) for o in outcomes(text, **kw)}


def spoken(text, **kw):
    """Every form, with the words still standing apart where they do."""
    return {o.text() for o in outcomes(text, **kw)}


def steps(text, course=0, **kw):
    """The sūtras of one derivation, in order; a declined option is not a step."""
    return [s.sutra for s in outcomes(text, **kw)[course].steps
            if not s.declined]


def all_steps(text, **kw):
    return [[s.sutra for s in o.steps if not s.declined]
            for o in outcomes(text, **kw)]


def step_of(text, sutra, course=0, **kw):
    return next(s for s in outcomes(text, **kw)[course].steps
                if s.sutra == sutra and not s.declined)


def cited(text, sutra, course=0, **kw):
    """The sūtras a step of `sutra` leans on."""
    return [v.sutra for v in step_of(text, sutra, course, **kw).detail.via]


def normalised(text):
    return " ".join(text.split())


class Family(unittest.TestCase):
    """Shared: nothing to set up, but every test reads the same rulebook."""


# ---------------------------------------------------------------------------
# what the family claims, and what it quotes
# ---------------------------------------------------------------------------

SCOPE = (
    [f"1.1.{n}" for n in range(11, 20)]
    + [f"1.4.{n}" for n in range(56, 61)]
    + [f"6.1.{n}" for n in range(115, 132)]
    + [f"8.2.{n}" for n in range(82, 108)]
    + ["8.3.33", "8.4.57"])


class Coverage(Family):

    def test_the_scope_is_exactly_fifty_nine_sutras(self):
        self.assertEqual(len(SCOPE), 59)
        self.assertEqual(len(set(SCOPE)), 59)

    def test_coverage_names_every_sutra_of_the_scope_once_and_nothing_else(self):
        declared = [sutra for sutra, _, _ in family.COVERAGE]
        self.assertEqual(sorted(declared), sorted(SCOPE))

    def test_every_sutra_of_the_scope_is_a_sutra_of_the_corpus(self):
        known = corpus.load_vidyut_sutrapatha()
        for sutra in SCOPE:
            self.assertIn(sutra, known, sutra)

    def test_the_rulebook_is_sound_with_this_family_loaded(self):
        self.assertEqual(rulebook.problems(), [])
        self.assertIn("prakrtibhava", rulebook.by_family())

    def test_every_rule_is_declared_as_a_rule_a_partial_or_vedic(self):
        status = {s: st for s, st, _ in family.COVERAGE}
        for r in family.RULES:
            self.assertIn(status[r.sutra], ("rule", "partial", "vedic"),
                          r.sutra)

    def test_a_sutra_marked_vedic_is_only_run_in_the_veda(self):
        for r in family.RULES:
            if dict((s, st) for s, st, _ in family.COVERAGE)[r.sutra] == "vedic":
                self.assertTrue(r.vedic, r.sutra)

    def test_every_scope_or_partial_note_gives_a_reason(self):
        for sutra, status, note in family.COVERAGE:
            if status in ("scope", "partial"):
                self.assertGreater(len(note.strip()), 30, sutra)

    def test_a_scope_sutra_of_the_pluta_names_the_reason_and_where_the_pluta_comes_in(self):
        notes = {s: n for s, st, n in family.COVERAGE if st == "scope"}
        for n in range(82, 108):
            note = notes[f"8.2.{n}"]
            self.assertTrue(
                "accent" in note or "meaning" in note or "Vedic" in note
                or "shape" in note or "sentence" in note, note)
        self.assertIn("pluta", notes["8.2.84"])

    def test_the_rules_declare_the_families_the_others_interlock_on(self):
        by = {r.sutra: r for r in family.RULES}
        for sutra in ("6.1.125", "6.1.127", "6.1.128", "6.1.122"):
            self.assertIn("ac", by[sutra].families, sutra)
            self.assertIn("prakrtibhava", by[sutra].families, sutra)
        self.assertIn("nasal", by["8.4.57"].families)
        # 6.1.125 wins against ALL rules of vowel sandhi
        self.assertIn("@ac", [t for t, _ in by["6.1.125"].overrides])
        # ... and the rules that stand ahead of it are not themselves
        # displaced by it, or the two would cancel out in one group
        for sutra in ("8.3.33", "1.1.18", "6.1.129", "6.1.130", "6.1.115",
                      "6.1.126"):
            self.assertNotIn("ac", by[sutra].families, sutra)

    def test_every_quotation_the_module_makes_is_in_the_commentary(self):
        """The reasons the rules give are the tradition's own words."""
        self.assertGreater(len(family.QUOTED), 12)
        for sutra, work, quote in family.QUOTED:
            text = corpus.commentary_on(sutra, work)
            self.assertTrue(text, (sutra, work))
            self.assertIn(normalised(quote), normalised(text),
                          f"{quote!r} is not in {work} on {sutra}")

    def test_a_quotation_that_is_not_in_the_commentary_would_be_caught(self):
        """The check above is only worth having if it can fail."""
        text = corpus.commentary_on("6.1.125", "kashika")
        self.assertNotIn(normalised("प्लुताश्च प्रगृह्याश्च नित्यं न भवन्ति"),
                         normalised(text))

    def test_the_sutra_text_a_trace_prints_is_the_corpus_text(self):
        known = corpus.load_vidyut_sutrapatha()
        for text, kw in (("harī{dvivacana} etau", {}),
                         ("vāyo{sambuddhi} iti", {}),
                         ("go agram", {}),
                         ("kim u{nipata} uktam", {}),
                         ("suśloka{pluta} iti", {}),
                         ("dadhi{sakalya} atra", {}),
                         ("te{antahpada} agne", {"veda": True}),
                         ("dadhi{anunasika}", {})):
            for o in outcomes(text, **kw):
                for step in trace.outcome_dict(o)["steps"]:
                    self.assertEqual(step["sutra_iast"],
                                     known[step["sutra"]].text)
                    for via in step["via"]:
                        self.assertIn(via["sutra"], known, (text, via))
                        self.assertEqual(via["text_iast"],
                                         known[via["sutra"]].text)
                    for lost in step["against"]:
                        self.assertIn(lost["sutra"], known)

    def test_the_word_lists_the_family_reads_are_the_kasikas(self):
        """6.1.116's seven and 6.1.118's six are the Kāśikā's lists."""
        from src.astadhyayi.prakrtibhava import AVYADI, YAJUSI_WORDS
        k116 = normalised(corpus.commentary_on("6.1.116", "kashika"))
        self.assertEqual(len(AVYADI), 7)
        head = k116.split("इत्येतेषु")[0].split()
        # the Kāśikā lists them in Devanāgarī; the module has them in IAST
        from src.astadhyayi.sandhi.parse import to_iast
        self.assertEqual([to_iast(w) for w in head], list(AVYADI))
        k118 = normalised(corpus.commentary_on("6.1.118", "kashika"))
        for word in YAJUSI_WORDS:
            from src.normalizer import iast_to_devanagari
            self.assertIn(iast_to_devanagari(word), k118, word)

    def test_the_letters_6_1_115_names_are_the_kasikas(self):
        """अव्यपरे is 'no व् or य् after the अ' — the Kāśikā says so in as many
        letters (अवकारयकारपरेऽति)."""
        text = normalised(corpus.commentary_on("6.1.115", "kashika"))
        self.assertIn("अवकारयकारपरेऽति", text)
        self.assertEqual(set(family._VA_YA), {"v", "y"})


# ---------------------------------------------------------------------------
# 6.1.125 with 1.1.11–19: the vowels that are named
# ---------------------------------------------------------------------------


class Dual(Family):
    """1.1.11 ईदूदेद्द्विवचनं प्रगृह्यम् — Kāśikā and Kaumudī."""

    def test_hari_etau_stays(self):
        """Laghukaumudī, Kaumudī: हरी एतौ."""
        r = sandhi("harī{dvivacana} etau")
        self.assertEqual(steps("harī{dvivacana} etau"), ["6.1.125"])
        self.assertEqual(r.outcomes[0].text(), "harī etau")
        self.assertEqual(len(r.outcomes), 1)

    def test_it_is_the_flag_and_not_the_letters_that_decides(self):
        """The control: the same ī with no flag is yaṇ's — हर्येतौ."""
        self.assertEqual(steps("harī etau"), ["6.1.77"])
        self.assertEqual(forms("harī etau"), {"haryetau"})

    def test_the_step_cites_the_sutra_that_gives_the_name(self):
        via = cited("harī{dvivacana} etau", "6.1.125")
        self.assertEqual(via, ["1.1.11"])
        self.assertEqual(step_of("harī{dvivacana} etau",
                                 "6.1.125").detail.kind, "prakṛtibhāva")

    def test_the_step_names_what_it_displaced(self):
        step = step_of("harī{dvivacana} etau", "6.1.125")
        against = {a.sutra: a.why for a in step.against}
        self.assertIn("6.1.77", against)
        self.assertIn("प्लुताश्च प्रगृह्याश्चाचि प्रकृत्या भवन्ति",
                      against["6.1.77"])

    def test_the_vowel_is_kept_long_and_untouched(self):
        final = outcomes("harī{dvivacana} etau")[0].final
        marked = [s for s in final.segs if PRAKRTYA in s.marks]
        self.assertEqual([s.s for s in marked], ["ī"])

    def test_the_kaumudis_other_examples(self):
        """विष्णू इमौ, गङ्गे अमू, पचेते इमौ (Kaumudī on 1.1.11); the last needs
        तदन्तविधि, which is why the whole word carries the flag."""
        for text, expected in (("viṣṇū{dvivacana} imau", "viṣṇū imau"),
                               ("gaṅge{dvivacana} amū", "gaṅge amū"),
                               ("pacete{dvivacana} imau", "pacete imau")):
            self.assertEqual(steps(text), ["6.1.125"], text)
            self.assertEqual(outcomes(text)[0].text(), expected)

    def test_the_kasikas_examples_before_iti(self):
        """अग्नी इति, वायू इति, माले इति, पचेते इति, पचेथे इति (Kāśikā)."""
        for word in ("agnī", "vāyū", "māle", "pacete", "pacethe"):
            text = f"{word}{{dvivacana}} iti"
            self.assertEqual(steps(text), ["6.1.125"], text)
            self.assertEqual(outcomes(text)[0].text(), f"{word} iti")

    def test_khatve_iti_and_a_vowel_of_the_ayadi_rule(self):
        """खट्वे इति (Kāśikā on 6.1.125): 6.1.78 would give खट्वयिति."""
        self.assertEqual(steps("khaṭve{dvivacana} iti"), ["6.1.125"])
        self.assertIn("khaṭvayiti", forms("khaṭve iti"))

    def test_a_dual_in_au_is_not_named(self):
        """ईदूदेदिति किम्? वृक्षावत्र, प्लक्षावत्र (Kāśikā)."""
        for word in ("vṛkṣau", "plakṣau"):
            text = f"{word}{{dvivacana}} atra"
            self.assertNotIn("6.1.125", sum(all_steps(text), []), text)
            self.assertIn(f"{word[:-2]}āvatra", forms(text))

    def test_a_singular_in_i_is_not_named(self):
        """द्विवचनमिति किम्? कुमार्यत्र, किशोर्यत्र (Kāśikā)."""
        for word, expected in (("kumārī", "kumāryatra"),
                               ("kiśorī", "kiśoryatra")):
            text = f"{word} atra"
            self.assertEqual(forms(text), {expected})
            self.assertEqual(steps(text), ["6.1.77"])

    def test_a_short_i_is_not_named_even_when_called_dual(self):
        """तपरकरणमसंदेहार्थम्: the name is for ई ऊ ए, not इ — Bhāṣya: अकुर्वहि
        अत्र, अकुर्वह्यत्र."""
        self.assertEqual(forms("akurvahi{dvivacana} atra"), {"akurvahyatra"})

    def test_the_first_member_of_a_compound_is_not_a_dual(self):
        """कुमार्योरगारं — the dual ending is elided (1.1.62 does not reach a
        name): कुमार्यगारम् (Tattvabodhinī, Balamanoramā)."""
        self.assertEqual(forms("kumārī-agāram"), {"kumāryagāram"})
        self.assertEqual(forms("kumārī{dvivacana}-agāram"), {"kumāryagāram"})

    def test_devanagari_gives_the_same_derivation(self):
        self.assertEqual(steps("हरी{dvivacana} एतौ"),
                         steps("harī{dvivacana} etau"))
        self.assertEqual(sandhi("हरी{dvivacana} एतौ").outcomes[0].text(),
                         "harī etau")


class Adas(Family):
    """1.1.12 अदसो मात्."""

    def test_ami_isah(self):
        """अमी ईशाः (Laghukaumudī, Kaumudī): a plural, so 1.1.11 cannot name it."""
        text = "amī{adas} īśāḥ"
        self.assertEqual(steps(text)[0], "6.1.125")
        self.assertEqual(cited(text, "6.1.125"), ["1.1.12"])
        self.assertEqual(outcomes(text)[0].text(), "amī īśāḥ")

    def test_ami_isah_is_not_named_without_the_flag(self):
        """The control: an ī that nothing names is joined with the ī after it."""
        self.assertEqual(steps("amī īśās")[0], "6.1.101")

    def test_the_kasikas_examples(self):
        """अमी अत्र, अमी आसते, अमू अत्र, अमू आसाते (Kāśikā on 1.1.12)."""
        for text, expected in (("amī{adas} atra", "amī atra"),
                               ("amī{adas} āsate", "amī āsate"),
                               ("amū{adas} atra", "amū atra"),
                               ("amū{adas} āsāte", "amū āsāte")):
            self.assertEqual(steps(text), ["6.1.125"], text)
            self.assertEqual(cited(text, "6.1.125"), ["1.1.12"], text)
            self.assertEqual(outcomes(text)[0].text(), expected)

    def test_the_masculine_dual_is_named_by_this_sutra_not_by_1_1_11(self):
        """Bālamanoramā: रामकृष्णावमू आसाते — the ū is made by an asiddha rule,
        so 1.1.11 does not see a dual ending; 1.1.12 is what names it."""
        text = "amū{adas,dvivacana} āsāte"
        self.assertEqual(cited(text, "6.1.125"), ["1.1.12"])

    def test_only_a_vowel_after_the_ma_of_adas_is_named(self):
        """मादिति किम्? अमुकेऽत्र (Kāśikā): the ए of अमुके follows a क्."""
        text = "amuke{adas} atra"
        self.assertEqual(steps(text), ["6.1.109"])
        self.assertEqual(forms(text), {"amuke'tra"})

    def test_a_word_that_is_not_adas_is_not_named(self):
        """अदस इति किम्? शम्यत्र, दाडिम्यत्र (Kāśikā): शमी and दाडिमी are not
        अदस्, so their ई is joined to the अ by yaṇ."""
        for word, expected in (("śamī", "śamyatra"), ("dāḍimī", "dāḍimyatra")):
            self.assertEqual(steps(f"{word} atra"), ["6.1.77"])
            self.assertEqual(forms(f"{word} atra"), {expected})


class She(Family):
    """1.1.13 शे — Vedic, and its one Vedic example."""

    def test_asme_indrabrhaspati(self):
        """अस्मे इन्द्राबृहस्पती (Kāśikā, Kaumudī on 1.1.13)."""
        text = "asme{she} indrābṛhaspatī"
        self.assertEqual(steps(text), ["6.1.125"])
        self.assertEqual(cited(text, "6.1.125"), ["1.1.13"])
        self.assertEqual(outcomes(text)[0].text(), "asme indrābṛhaspatī")

    def test_the_control_without_the_flag_is_the_ordinary_ayadi(self):
        self.assertIn("asmayindrābṛhaspatī", forms("asme indrābṛhaspatī"))
        self.assertEqual(steps("asme indrābṛhaspatī")[0], "6.1.78")


class Particle(Family):
    """1.1.14 निपात एकाजनाङ् and 1.1.15 ओत्."""

    def test_i_indrah_and_u_umesah(self):
        """इ इन्द्रः, उ उमेशः (Kaumudī on 1.1.14, Laghukaumudī)."""
        for text, expected in (("i{nipata} indraḥ", "i indraḥ"),
                               ("u{nipata} umeśaḥ", "u umeśaḥ")):
            self.assertEqual(steps(text)[0], "6.1.125", text)
            self.assertEqual(cited(text, "6.1.125")[-1], "1.1.14")
            self.assertEqual(outcomes(text)[0].text(), expected.replace(
                "indraḥ", "indraḥ"))

    def test_a_apehi_and_u_uttistha(self):
        """अ अपेहि, उ उत्तिष्ठ (Kāśikā on 1.1.14)."""
        self.assertEqual(steps("a{nipata} apehi"), ["6.1.125"])
        self.assertEqual(steps("u{nipata} uttiṣṭha"), ["6.1.125"])

    def test_the_letters_do_not_say_a_particle_so_the_caller_does(self):
        """The control, and the reason `infer.py` does not guess: a bare इ is
        the last sound of a word as often as a particle, and the engine's own
        tests use it so."""
        self.assertEqual(steps("i indraḥ")[0], "6.1.101")
        self.assertEqual(steps("i{nipata} indraḥ")[0], "6.1.125")

    def test_a_bare_a_is_the_particle_only_if_it_is_not_ang(self):
        """आ एवं नु मन्यसे, आ एवं किल तत् — pragṛhya — against आ उदकान्तात् =
        ओदकान्तात् (Kāśikā on 1.1.14): the आङ् is a ṅit आ."""
        self.assertEqual(steps("ā{nipata} evam nu manyase"), ["6.1.125"])
        self.assertEqual(steps("ā{nipata} evam kila tat")[:1], ["6.1.125"])
        self.assertNotIn("6.1.101", steps("ā{nipata} evam kila tat"))
        self.assertEqual(outcomes("ā{nipata} evam nu manyase")[0].text(),
                         "ā evam nu manyase")
        text = "ā{nipata,ang} udakāntāt"
        self.assertEqual(steps(text)[0], "6.1.87")
        self.assertNotIn("6.1.125", steps(text))
        self.assertTrue(forms(text) <= {"odakāntāt", "odakāntād"})

    def test_the_preverb_aa_before_its_dhatu_is_ang_by_the_boundary(self):
        """The boundary `|` says the आ is the preverb, so it is the आङ् that
        1.1.14 leaves out — with no flag."""
        self.assertNotIn("6.1.125", steps("ā{nipata}|udakāntāt"))

    def test_ekaj_iti_kim_pra_agnaye(self):
        """एकाजिति किम्? प्राग्नये वाचमीरय: प्र has one vowel and two sounds, so it
        is not one of them — and it is a nipāta all the same (prādi)."""
        text = "pra{nipata} agnaye"
        self.assertEqual(steps(text), ["6.1.101"])
        self.assertEqual(forms(text), {"prāgnaye"})
        self.assertEqual(steps("pra agnaye"), ["6.1.101"])

    def test_nipata_iti_kim_cakara_atra(self):
        """निपात इति किम्? चकारात्र, जहारात्र: an ā that ends a verb is no
        particle, and its sandhi goes through."""
        self.assertEqual(forms("cakāra atra"), {"cakārātra"})
        self.assertEqual(forms("jahāra atra"), {"jahārātra"})

    def test_aho_isah_is_named_by_1_1_15_and_the_particle_is_proved(self):
        """अहो ईशाः (Laghukaumudī, Kaumudī on 1.1.15): no flag — अहो is in the
        cādi gaṇa, so `infer` says so and the step cites 1.4.57."""
        text = "aho īśāḥ"
        r = sandhi(text)
        self.assertEqual(steps(text)[0], "6.1.125")
        self.assertEqual(cited(text, "6.1.125"), ["1.4.57", "1.1.15"])
        self.assertEqual(r.outcomes[0].text(), "aho īśāḥ")
        assumptions = trace.assumptions(r.outcomes[0])
        self.assertTrue(any("nipata" in a and "aho" in a for a in assumptions),
                        assumptions)

    def test_the_kasikas_o_particles(self):
        """आहो इति, उताहो इति (Kāśikā on 1.1.15)."""
        for word in ("āho", "utāho"):
            text = f"{word} iti"
            self.assertEqual(steps(text), ["6.1.125"], text)
            self.assertEqual(outcomes(text)[0].text(), f"{word} iti")

    def test_a_word_in_o_that_is_not_a_particle_takes_purvarupa(self):
        """The control (Bhāṣya on 1.1.15: अदोऽभवत्): अदो is a form of अदस्."""
        self.assertEqual(steps("ado abhavat")[:1], ["6.1.109"])
        self.assertNotIn("6.1.125", steps("ado abhavat"))
        self.assertEqual({f[:-1] for f in forms("ado abhavat")},
                         {"ado'bhava"})      # the final त् is 8.2.39's

    def test_a_particle_that_names_a_substance_is_not_named_the_flag_says_so(self):
        """1.4.57 चादयोऽसत्त्वे: the cādi word नो is also the pronoun's. The
        flag `sattva` takes the inference away and the sandhi is the ordinary."""
        self.assertEqual(steps("no atra")[0], "6.1.125")
        self.assertEqual(steps("no{sattva} atra"), ["6.1.109"])


class Vocative(Family):
    """1.1.16 सम्बुद्धौ शाकल्यस्येतावनार्षे."""

    def test_vayo_iti_is_an_option(self):
        """वायो इति, वायविति (Kāśikā); विष्णो इति, विष्ण इति, विष्णविति (Laghukaumudī,
        Kaumudī): three forms, the first with the name."""
        r = sandhi("vāyo{sambuddhi} iti")
        self.assertEqual(len(r.outcomes), 3)
        self.assertEqual({o.text() for o in r.outcomes},
                         {"vāyo iti", "vāya iti", "vāyav iti"})
        self.assertEqual(forms("vāyo{sambuddhi} iti"),
                         {"vāyoiti", "vāyaiti", "vāyaviti"})

    def test_the_first_course_takes_the_option_and_says_so(self):
        r = sandhi("viṣṇo{sambuddhi} iti")
        first = r.outcomes[0]
        self.assertEqual([s.sutra for s in first.steps], ["6.1.125"])
        self.assertEqual(first.steps[0].option, "शाकल्यस्य")
        self.assertEqual(first.choices[0], ("6.1.125", True))
        self.assertEqual(first.text(), "viṣṇo iti")
        self.assertEqual(cited("viṣṇo{sambuddhi} iti", "6.1.125"), ["1.1.16"])

    def test_the_declined_course_is_the_ayadi_rule_and_says_it_declined(self):
        r = sandhi("viṣṇo{sambuddhi} iti")
        second = r.outcomes[1]
        self.assertEqual([s.sutra for s in second.steps if s.declined],
                         ["6.1.125"])
        self.assertEqual([s.sutra for s in second.steps if not s.declined][0],
                         "6.1.78")

    def test_the_kind_of_option_is_the_commentarys(self):
        """Bālamanoramā: 'निपातत्वाऽभावादप्राप्ते विभाषेयम्' — an aprāpta
        vibhāṣā (1.3.43's kind, not 1.3.50's), and the step says so."""
        step = step_of("viṣṇo{sambuddhi} iti", "6.1.125")
        role = next(v.role for v in step.detail.via if v.sutra == "1.1.16")
        self.assertIn("aprāpta", role)
        self.assertIn("निपातत्वाऽभावादप्राप्ते विभाषेयम्", role)

    def test_before_a_vowel_other_than_iti_it_is_purvarupa(self):
        """इताविति किम्? वायोऽत्र (Kāśikā)."""
        self.assertEqual(steps("vāyo{sambuddhi} atra"), ["6.1.109"])
        self.assertEqual(forms("vāyo{sambuddhi} atra"), {"vāyo'tra"})

    def test_it_is_for_the_vocative_alone(self):
        """संबुद्धाविति किम्? गवित्ययमाह (Kāśikā): no name, no 6.1.125."""
        for o in outcomes("go iti"):
            self.assertNotIn("6.1.125", [s.sutra for s in o.steps])
        self.assertIn("gaviti", forms("go iti"))

    def test_a_vedic_iti_takes_no_option(self):
        """अनार्ष इति किम्? एता गा ब्रह्मबन्ध इत्यब्रवीत् (Kāśikā): the iti is
        Vedic, so 1.1.16 is not reached and the vocative goes to yaṇ."""
        text = "brahmabandho{sambuddhi} iti{arsa} abravīt"
        for o in outcomes(text):
            self.assertNotIn("6.1.125", [s.sutra for s in o.steps])
        self.assertIn("brahmabandhavityabravīt", forms(text))
        self.assertTrue(all(o.steps[0].sutra == "6.1.78"
                            for o in outcomes(text)))


class Un(Family):
    """1.1.17 उञः and 1.1.18 ऊँ: three forms."""

    def test_u_iti_is_three_forms(self):
        """उ इति, वि इति, ऊँ इति (Kāśikā on 1.1.18: त्रीणि रूपाणि भवन्ति)."""
        r = sandhi("u{nipata} iti")
        self.assertEqual(len(r.outcomes), 3)
        self.assertEqual({o.text() for o in r.outcomes},
                         {"ū̐ iti", "u iti", "v iti"})
        self.assertEqual(forms("u{nipata} iti"), {"ū̐iti", "uiti", "viti"})

    def test_the_three_courses_are_the_three_sutras(self):
        r = sandhi("u{nipata} iti")
        self.assertEqual([s.sutra for s in r.outcomes[0].steps], ["1.1.18"])
        self.assertEqual([s.sutra for s in r.outcomes[1].steps
                          if not s.declined], ["6.1.125"])
        self.assertEqual([s.sutra for s in r.outcomes[2].steps
                          if not s.declined], ["6.1.77"])
        self.assertEqual(cited("u{nipata} iti", "6.1.125", 1), ["1.1.17"])

    def test_the_substitute_is_long_nasal_and_pragrhya(self):
        """दीर्घोऽनुनासिकः प्रगृह्यश्च (Kāśikā): ऊँ is kept."""
        final = outcomes("u{nipata} iti")[0].final
        made = [s for s in final.segs if s.made_by == "1.1.18"]
        self.assertEqual([(s.s, s.nasal) for s in made], [("ū", True)])
        self.assertIn(PRAKRTYA, made[0].marks)

    def test_the_ṛṣis_own_iti_leaves_only_the_name_of_1_1_14(self):
        """अनार्षे: the इति of the ṛṣi's text is not this sūtra's."""
        self.assertEqual(forms("u{nipata} iti{arsa}"), {"uiti"})

    def test_a_vedic_passage_is_not_thereby_arsa(self):
        """The इति of a padapāṭha is the padakāra's even in the Veda: the
        three forms stand (the Kāśikā's own instance is वायो इति, ऋ० ४.४६.१)."""
        self.assertEqual(forms("u{nipata} iti", veda=True),
                         forms("u{nipata} iti"))
        self.assertEqual(len(outcomes("vāyo{sambuddhi} iti", veda=True)), 3)

    def test_the_letter_is_not_the_particle_unless_it_is_said_to_be(self):
        """The control: with no flag it is yaṇ's alone."""
        self.assertEqual(forms("u iti"), {"viti"})


class Locative(Family):
    """1.1.19 ईदूतौ च सप्तम्यर्थे."""

    def test_the_kasikas_and_the_kaumudis_examples(self):
        """गौरी अधि (Kaumudī: सोमो गौरी अधिश्रितः), मामकी तनू (Kāśikā)."""
        for text, expected in (("gaurī{saptamyartha} adhi", "gaurī adhi"),
                               ("māmakī{saptamyartha} iti", "māmakī iti"),
                               ("tanū{saptamyartha} iti", "tanū iti")):
            self.assertEqual(steps(text), ["6.1.125"], text)
            self.assertEqual(cited(text, "6.1.125"), ["1.1.19"])
            self.assertEqual(outcomes(text)[0].text(), expected)

    def test_a_compound_of_the_word_is_not_the_locative_sense(self):
        """अर्थग्रहणं किम्? वाप्यश्वः, नद्यातिः (Kāśikā): the first member has
        left the locative's meaning, so the ī is joined."""
        self.assertEqual(forms("vāpī-aśvaḥ"), {"vāpyaśvaḥ"})
        self.assertEqual(forms("nadī-ātiḥ"), {"nadyātiḥ"})


# ---------------------------------------------------------------------------
# 6.1.125 — pluta, order, and what a sound may see
# ---------------------------------------------------------------------------


class Pluta(Family):

    def test_the_pluta_is_kept(self):
        """एहि कृष्ण३ अत्र (Kaumudī), देवदत्त३ अत्र न्वसि, यज्ञदत्त३ इदमानय
        (Kāśikā on 6.1.125)."""
        for text, expected in (
                ("kṛṣṇa{pluta} atra", "kṛṣṇa atra"),
                ("devadatta{pluta} atra", "devadatta atra"),
                ("yajñadatta{pluta} idam", "yajñadatta idam")):
            self.assertEqual(steps(text), ["6.1.125"], text)
            self.assertEqual(outcomes(text)[0].text(), expected)

    def test_a_pluta_step_cites_the_measure_and_the_asiddha_exemption(self):
        via = step_of("kṛṣṇa{pluta} atra", "6.1.125").detail.via
        self.assertEqual([v.sutra for v in via], ["1.2.27"])
        self.assertIn("8.2.1", via[0].role)
        self.assertIn("tripādī", via[0].role)

    def test_the_control_without_the_pluta_is_savarna_dirgha(self):
        self.assertEqual(steps("kṛṣṇa atra"), ["6.1.101"])
        self.assertEqual(forms("kṛṣṇa atra"), {"kṛṣṇātra"})

    def test_the_kasika_khatve_male_and_agni_vayu(self):
        """अग्नी इति, वायू इति, खट्वे इति, माले इति (Kāśikā on 6.1.125)."""
        for word in ("agnī", "vāyū", "khaṭve", "māle"):
            self.assertEqual(steps(f"{word}{{dvivacana}} iti"), ["6.1.125"])

    def test_nityam_puts_it_ahead_of_sakalyas_option(self):
        """नित्यग्रहणमिहानुवर्तते। प्लुतप्रगृह्याणां नित्यमयमेव प्रकृतिभावो यथा
        स्याद् इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च इत्येतन् मा भूदिति (Kāśikā). A
        dual ī before an unlike vowel, for a speaker who follows Śākalya, is
        kept LONG and there is no other course."""
        text = "harī{dvivacana,sakalya} etau"
        self.assertEqual(steps(text), ["6.1.125"])
        self.assertEqual(len(outcomes(text)), 1)
        self.assertEqual(outcomes(text)[0].text(), "harī etau")
        step = step_of(text, "6.1.125")
        by = {a.sutra: a.why for a in step.against}
        self.assertIn("6.1.127", by)
        self.assertIn("प्लुतप्रगृह्याणां नित्यमयमेव प्रकृतिभावो यथा स्याद्",
                      by["6.1.127"])

    def test_without_nityam_the_option_would_win_the_place(self):
        """The control for the test above: the option is real. Take away
        what 6.1.125 declares it displaces and 6.1.127, which stands later,
        takes the place and the shortened form appears."""
        from dataclasses import replace
        from src.astadhyayi.sandhi.engine import derive
        rules = tuple(
            replace(r, overrides=()) if r.sutra == "6.1.125" else r
            for r in _rules())
        out = derive(parse("harī{dvivacana,sakalya} etau"), rules)
        self.assertIn("hari etau", {o.text() for o in out})

    def test_the_junction_before_a_pragrhya_vowel_is_settled_first(self):
        """जानु उ अस्य रुजति, जान्वस्य रुजति (Kāśikā on 6.1.125: the second उ is
        pragṛhya, yet the first उ joins it — the second अचि). The engine's
        own `sa a i` → `se` is the same shape."""
        text = "jānu u{nipata} asya rujati"
        self.assertEqual(steps(text), ["6.1.101", "6.1.77"])
        self.assertEqual(forms(text), {"jānvasyarujati"})
        self.assertEqual(steps("sa a i"), ["6.1.101", "6.1.87"])

    def test_a_particle_between_two_words_is_kept_from_the_one_after(self):
        """The particle itself stays: `a iti` — and what stands before it has
        already been dealt with."""
        r = sandhi("a{nipata} iti a iti")
        self.assertEqual(r.outcomes[0].text().split()[0], "a")
        self.assertEqual(steps("a{nipata} iti a iti")[0], "6.1.125")

    def test_a_particle_between_two_words_is_joined_from_the_left_first(self):
        """The design, said as a test (OPEN in the docstring): the junction
        before a one-vowel particle is done by the rules of sandhi, and the
        ekādeśa that results is no one's particle."""
        text = "sa a{nipata} i"
        self.assertEqual(steps(text), ["6.1.101", "6.1.87"])
        self.assertEqual(forms(text), {"se"})
        # the particle is still kept from what FOLLOWS it when no vowel
        # stands before it
        text = "tat a{nipata} i"
        self.assertIn("6.1.125", steps(text))
        self.assertNotIn("6.1.87", steps(text))
        self.assertTrue(outcomes(text)[0].text().endswith("a i"))

    def test_a_sound_this_derivation_made_is_not_pragrhya(self):
        """The ekādeśa ऊ of जानु + उ is no one's particle: the Kāśikā gives
        जान्वस्य. (OPEN: the Tattvabodhinī also allows जानू अस्य.)"""
        out = outcomes("jānu u{nipata} asya rujati")[0]
        self.assertNotIn("6.1.125", [s.sutra for s in out.steps])

    def test_the_pluta_a_tripadi_rule_would_make_is_visible_by_consumes(self):
        """6.1.125's own wording names the pluta, which 8.2.82–107 make in the
        tripādī: 8.2.1 would hide it, and `consumes` is what lets it see
        (plutamanūdya prakṛtibhāvavidhānasāmarthyāt, Tattvabodhinī). Build the
        state a rule of 8.2.84 would leave and ask the rule."""
        rule = next(r for r in _rules() if r.sutra == "6.1.125")
        self.assertIn(PLUTA, rule.consumes)
        state = parse("kṛṣṇa atra", infer=False)
        last = state.segs[4]                       # the final a of kṛṣṇa
        self.assertEqual((last.s, last.w), ("a", 0))
        made = Seg(uid=99, s="a", w=0, marks=frozenset({PLUTA}),
                   made_by="8.2.84", prior=(last,))
        state = state.__class__(
            segs=state.segs[:4] + (made,) + state.segs[5:],
            words=state.words, bounds=state.bounds, next_uid=100)
        seen = list(rule.find(View(state, "6.1.125", rule.consumes)))
        self.assertEqual(len(seen), 1)
        self.assertEqual(seen[0].detail.kind, "prakṛtibhāva")
        self.assertEqual([v.sutra for v in seen[0].detail.via], ["1.2.27"])
        # without the declaration the rule goes as blind as 8.2.1 says
        blind = list(rule.find(View(state, "6.1.125", frozenset())))
        self.assertEqual(blind, [])
        # and the ordinary rules, which are not given the mark, do not see it
        self.assertFalse(View(state, "6.1.101").live[4].has(PLUTA))
        self.assertTrue(View(state, "6.1.125", rule.consumes).live[4].has(PLUTA))

    def test_the_marked_vowel_is_left_out_of_every_rules_pairs(self):
        final = outcomes("harī{dvivacana} etau")[0].final
        self.assertEqual(View(final, "6.1.77").vowel_pairs(), [])


class Aplutavat(Family):
    """6.1.129 अप्लुतवदुपस्थिते and 6.1.130 ई३ चाक्रवर्मणस्य."""

    def test_sushloka_iti(self):
        """सुश्लोक३ इति = सुश्लोकेति, सुमङ्गल३ इति = सुमङ्गलेति (Kāśikā)."""
        for text, expected in (("suśloka{pluta} iti", "suśloketi"),
                               ("sumaṅgala{pluta} iti", "sumaṅgaleti")):
            self.assertEqual(steps(text), ["6.1.129", "6.1.87"], text)
            self.assertEqual(forms(text), {expected})

    def test_it_takes_the_pluta_effect_away_and_says_so(self):
        step = step_of("suśloka{pluta} iti", "6.1.129")
        self.assertEqual(step.detail.kind, "pratiṣedha")
        self.assertEqual(step.before, step.after)
        by = {a.sutra: a.why for a in step.against}
        self.assertIn("6.1.125", by)
        self.assertIn("प्लुतकार्यं प्रकृतिभावं न करोति", by["6.1.125"])
        self.assertIn("next step", by["6.1.125"])

    def test_only_before_an_iti_of_a_later_analyst(self):
        """Not before another vowel; not before a Vedic iti (उपस्थितं नाम
        अनार्ष इतिकरणः)."""
        self.assertEqual(steps("suśloka{pluta} atra"), ["6.1.125"])
        self.assertEqual(steps("suśloka{pluta} iti{arsa}"), ["6.1.125"])
        # ... and a Vedic passage is not itself the ṛṣi's iti: सुश्लोक३ इति
        # is Taittirīya's padapāṭha
        self.assertEqual(steps("suśloka{pluta} iti", veda=True),
                         ["6.1.129", "6.1.87"])

    def test_agni_iti_keeps_its_name_and_its_length(self):
        """वत्करणं किम्? … प्रगृह्याश्रये प्रकृतिभावे प्लुतस्य श्रवणं न स्यात् —
        अग्नी३ इति, वायू३ इति (Kāśikā): 'as if not pluta', so the name
        pragṛhya is untouched. Two steps: the fiction, then the name."""
        for word in ("agnī", "vāyū"):
            text = f"{word}{{dvivacana,pluta}} iti"
            self.assertEqual(steps(text), ["6.1.129", "6.1.125"], text)
            self.assertEqual(outcomes(text)[0].text(), f"{word} iti")
            self.assertEqual(cited(text, "6.1.125"), ["1.1.11"])

    def test_cakravarmana_is_a_named_option(self):
        """अस्तु हीत्यब्रूताम्, अस्ति ही३ इत्यब्रूताम् (Kāśikā on 6.1.130): one
        form takes the pluta as short, the other keeps it."""
        text = "hi{pluta} iti abrūtām"
        r = sandhi(text)
        self.assertEqual(len(r.outcomes), 2)
        self.assertEqual([s.sutra for s in r.outcomes[0].steps][:2],
                         ["6.1.130", "6.1.101"])
        self.assertEqual(r.outcomes[0].steps[0].option, "चाक्रवर्मणस्य")
        self.assertEqual(r.outcomes[0].text(), "hīty abrūtām")
        self.assertEqual(r.outcomes[1].text(), "hi ity abrūtām")
        self.assertEqual([s.sutra for s in r.outcomes[1].steps
                          if not s.declined][0], "6.1.125")

    def test_cinu_hi_idam(self):
        """चिनु हीदम्, चिनु ही३ इदम् (Kāśikā): before a vowel that is not iti,
        where 6.1.129 does not reach — the aprāpta half of the उभयत्रविभाषा."""
        text = "cinu hī{pluta} idam"
        self.assertEqual({o.text() for o in outcomes(text)},
                         {"cinu hīdam", "cinu hī idam"})

    def test_the_option_is_for_the_i_varna_only_as_the_sutra_says(self):
        """कृष्ण३ अत्र stays (the Laghukaumudī's example); the Kāśikā's
        extension (वशा३ इयम्) is not derived — see COVERAGE."""
        self.assertEqual(steps("kṛṣṇa{pluta} atra"), ["6.1.125"])
        self.assertEqual(len(outcomes("vaśā{pluta} iyam")), 1)
        note = {s: n for s, _, n in family.COVERAGE}["6.1.130"]
        self.assertIn("iṣyate", note)


# ---------------------------------------------------------------------------
# 6.1.127, 6.1.128 — Śākalya
# ---------------------------------------------------------------------------


class Sakalya(Family):

    def test_dadhi_atra(self):
        """दधि अत्र, दध्यत्र; मधु अत्र, मध्वत्र (Kāśikā); चक्रि अत्र, चक्र्यत्र
        (Kaumudī)."""
        for word, plain, yan in (("dadhi", "dadhi atra", "dadhy atra"),
                                 ("madhu", "madhu atra", "madhv atra"),
                                 ("cakri", "cakri atra", "cakry atra")):
            text = f"{word}{{sakalya}} atra"
            self.assertEqual(spoken(text), {plain, yan}, text)
            self.assertEqual(all_steps(text),
                             [["6.1.127"], ["6.1.77"]], text)

    def test_the_option_comes_first_and_yan_stays_the_other_course(self):
        r = sandhi("dadhi{sakalya} atra")
        self.assertEqual(r.outcomes[0].steps[0].option, "शाकल्यस्य")
        self.assertEqual(r.outcomes[1].steps[0].declined, True)
        step = step_of("dadhi{sakalya} atra", "6.1.127")
        by = {a.sutra: a.why for a in step.against}
        self.assertIn("आरम्भसामर्थ्यादेव हि यणादेशेन सह विकल्पः सिद्धः",
                      by["6.1.77"])

    def test_it_is_offered_on_request_so_the_ordinary_yan_is_the_default(self):
        """README: `iti ādi` → ityādi. The control for the flag."""
        self.assertEqual(forms("dadhi atra"), {"dadhyatra"})
        self.assertEqual(forms("iti ādi"), {"ityādi"})
        self.assertEqual(sandhi("iti ādi").surface, "ityādi")

    def test_a_long_vowel_is_shortened(self):
        """कुमारि अत्र, कुमार्यत्र; किशोरि अत्र (Kāśikā): ह्रस्वश्च."""
        text = "kumārī{sakalya} atra"
        self.assertEqual(spoken(text), {"kumāri atra", "kumāry atra"})
        step = step_of(text, "6.1.127")
        self.assertEqual((step.detail.sthanin, step.detail.adesa), ("ī", "i"))
        final = outcomes(text)[0].final
        self.assertEqual([s.s for s in final.segs if PRAKRTYA in s.marks],
                         ["i"])

    def test_ik_iti_kim(self):
        """इक इति किम्? खट्वेन्द्रः (Kāśikā): ā is no ik, so guṇa."""
        self.assertEqual(steps("khaṭvā{sakalya} indraḥ")[0], "6.1.87")
        self.assertEqual(forms("khaṭvā{sakalya} indraḥ"), {"khaṭvendraḥ"})

    def test_asavarna_iti_kim(self):
        """असवर्ण इति किम्? कुमारीन्द्रः (Kāśikā): the vowels are savarṇa, so
        6.1.101 alone acts."""
        self.assertEqual(steps("kumārī{sakalya} indraḥ")[0], "6.1.101")
        self.assertEqual(forms("kumārī{sakalya} indraḥ"), {"kumārīndraḥ"})

    def test_na_samase(self):
        """न समासे (vārttika, corpus.varttikas_on): वाप्यश्वः, and by the
        Kāśikā's नित्यसमासे — व्याकरणम्, कुमार्यर्थम्."""
        self.assertEqual(corpus.varttikas_on("6.1.127")[0].text.strip(),
                         "न समासे ।")
        self.assertEqual(forms("vāpī{sakalya}-aśvaḥ"), {"vāpyaśvaḥ"})
        self.assertEqual(forms("vi{sakalya}|ākaraṇam"), {"vyākaraṇam"})
        self.assertEqual(forms("kumārī{sakalya}-artham"), {"kumāryartham"})
        for text in ("vāpī{sakalya}-aśvaḥ", "vi{sakalya}|ākaraṇam"):
            self.assertNotIn("6.1.127", sum(all_steps(text), []), text)

    def test_siti_ca_arises_at_no_pada_boundary(self):
        """सिति च (vārttika): पार्श्वम्. A stem | affix junction is not
        pada-final in the engine, so 6.1.127 never reaches it."""
        self.assertEqual(corpus.varttikas_on("6.1.127")[1].text.strip(),
                         "सिति च ।")
        self.assertEqual(forms("pārśu{sakalya}~a"), {"pārśva"})

    def test_brahma_rsih(self):
        """ब्रह्म ऋषिः, ब्रह्मर्षिः (Laghukaumudī, Kaumudī on 6.1.128)."""
        text = "brahmā{sakalya} ṛṣiḥ"
        self.assertEqual(spoken(text), {"brahma ṛṣiḥ", "brahmarṣiḥ"})
        by_form = {joined(o.text()): [s.sutra for s in o.steps
                                      if not s.declined]
                   for o in outcomes(text)}
        self.assertEqual(by_form["brahmaṛṣiḥ"][0], "6.1.128")
        self.assertEqual(by_form["brahmarṣiḥ"][0], "6.1.87")     # guṇa, ar

    def test_the_kasikas_examples_of_6_1_128(self):
        """खट्व ऋश्यः, माल ऋश्यः, होतृ ऋश्यः (Kāśikā)."""
        self.assertEqual(spoken("khaṭvā{sakalya} ṛśyaḥ"),
                         {"khaṭva ṛśyaḥ", "khaṭvarśyaḥ"})
        self.assertEqual(spoken("mālā{sakalya} ṛśyaḥ"),
                         {"māla ṛśyaḥ", "mālarśyaḥ"})
        # (another family may add a form by a vārttika of 6.1.101; the two
        # of the Kāśikā are there in any case)
        self.assertLessEqual({"hotṛ ṛśyaḥ", "hotṝśyaḥ"},
                             spoken("hotṛ{sakalya} ṛśyaḥ"))

    def test_6_1_128_reaches_savarna_and_a(self):
        """सवर्णार्थमनिगर्थं च वचनम् (Kāśikā): ṛ+ṛ, which 6.1.127 excluded, and
        अ/आ, which are no इक्."""
        first = outcomes("hotṛ{sakalya} ṛśyaḥ")[0]
        self.assertEqual(first.steps[0].sutra, "6.1.128")
        by = {a.sutra: a.why for a in first.steps[0].against}
        self.assertIn("सवर्णार्थमनिगर्थं च वचनम्", by["6.1.101"])

    def test_it_holds_in_a_compound(self):
        """समासेऽप्ययं प्रकृतिभावः — सप्तऋषीणाम्, सप्तर्षीणाम् (Kaumudī)."""
        self.assertEqual(spoken("sapta{sakalya}-ṛṣīṇām"),
                         {"sapta ṛṣīṇām", "saptarṣīṇām"})

    def test_rti_iti_kim_and_ak_iti_kim(self):
        """ऋतीति किम्? खट्वेन्द्रः; अक इति किम्? वृक्षावृश्यः (Kāśikā)."""
        self.assertEqual(forms("vṛkṣau{sakalya} ṛśyaḥ"),
                         {"vṛkṣāvṛśyaḥ", "vṛkṣāṛśyaḥ"})
        self.assertNotIn("6.1.128", sum(all_steps("vṛkṣau{sakalya} ṛśyaḥ"),
                                        []))

    def test_only_a_pada_final_ak(self):
        """आर्च्छत् (Kaumudī: पदान्ता इत्येव): the āṭ is not pada-final."""
        self.assertNotIn("6.1.128", sum(all_steps("ā{sakalya}~ṛcchat"), []))

    def test_both_rules_reach_an_ik_before_ri(self):
        """कुमारि ऋश्यः is the Kāśikā's example of 6.1.128 and 6.1.127 reaches
        it too; the later is done first and the other course remains."""
        text = "kumārī{sakalya} ṛśyaḥ"
        self.assertIn("kumāri ṛśyaḥ", spoken(text))
        self.assertIn("kumāry ṛśyaḥ", spoken(text))
        self.assertEqual(all_steps(text)[0][0], "6.1.128")


# ---------------------------------------------------------------------------
# 6.1.122–124 — go
# ---------------------------------------------------------------------------


class Go(Family):

    def test_go_agram_has_three_forms(self):
        """गो अग्रम्, गोऽग्रम् (6.1.122), गवाग्रम् (6.1.123) — Laghukaumudī,
        Kaumudī."""
        self.assertEqual(spoken("go agram"),
                         {"go agram", "go 'gram", "gavāgram"})

    def test_each_form_by_its_sutra(self):
        by = {o.text(): [s.sutra for s in o.steps if not s.declined]
              for o in outcomes("go agram")}
        self.assertEqual(by["go agram"], ["6.1.122"])
        self.assertEqual(by["go 'gram"], ["6.1.109"])
        self.assertEqual(by["gavāgram"], ["6.1.123", "6.1.101"])

    def test_the_option_of_prakrtibhava_is_really_of_purvarupa(self):
        """निषेधविकल्पे विधिविकल्पः फलित इत्याशयेन पूर्वरूपमेव विकल्प्यत इति
        (Tattvabodhinī): 6.1.122 displaces 6.1.109 and never 6.1.78 — no
        *gav agram*."""
        first = next(o for o in outcomes("go agram")
                     if o.text() == "go agram")
        by = {a.sutra: a.why for a in next(
            s for s in first.steps if s.sutra == "6.1.122").against}
        self.assertIn("6.1.109", by)
        self.assertIn("निषेधविकल्पे विधिविकल्पः फलित इत्याशयेन", by["6.1.109"])
        self.assertNotIn("gavagram", forms("go agram"))

    def test_go_in_a_compound(self):
        """गोऽजिनम्, गो अजिनम्, गवाजिनम् (Kāśikā on 6.1.123)."""
        self.assertEqual(forms("go-ajinam"),
                         {"goajinam", "go'jinam", "gavājinam"})

    def test_avan_before_other_vowels(self):
        """गवौदनम्, गवोदनम्; गवोष्ट्रम्, गवुष्ट्रम् (Kāśikā on 6.1.123): avaṅ then
        vṛddhi/guṇa, or 6.1.78's गव्; the loss of the व् (8.3.19) gives the
        third."""
        self.assertEqual(forms("go odanam"),
                         {"gavaudanam", "gavodanam", "gaodanam"})
        self.assertEqual(forms("go uṣṭram"),
                         {"gavoṣṭram", "gavuṣṭram", "gauṣṭram"})

    def test_the_substitute_is_the_last_sound_only(self):
        """The ṅ of अवङ् is an इत् (Bālamanoramā: ङिच्चेत्यन्तादेशः): गो →
        ग् + अव, not अव for the whole."""
        step = step_of("go agram", "6.1.123", 0)
        self.assertEqual((step.detail.sthanin, step.detail.adesa),
                         ("o", "ava"))
        self.assertIn("1.1.53", [v.sutra for v in step.detail.via])

    def test_indra_is_fixed(self):
        """गवेन्द्रः (Laghukaumudī, Kaumudī): इन्द्रे च — नित्यम्, so there is
        ONE course, and 6.1.123's option is withdrawn."""
        r = sandhi("go indraḥ")
        self.assertEqual(len(r.outcomes), 1)
        self.assertEqual(steps("go indraḥ")[:2], ["6.1.124", "6.1.87"])
        self.assertEqual(r.surface, "gavendraḥ")
        by = {a.sutra: a.why
              for a in step_of("go indraḥ", "6.1.124").against}
        self.assertIn("विकल्पनिवृत्त्यर्थः", by["6.1.123"])
        self.assertIn("इन्द्रशब्दस्थेऽचि परतो गोर्नित्यमवङादेशो भवति",
                      by["6.1.78"])

    def test_gavaksa_is_fixed_by_vyavasthita_vibhasa(self):
        """व्यवस्थितविभाषेयम्, तेन गवाक्ष इत्यत्र नित्यमवङ् भवति (Kāśikā): a
        window. The meaning is a flag; without it the compound is open."""
        fixed = sandhi("go-akṣaḥ{vatayana}")
        self.assertEqual(len(fixed.outcomes), 1)
        self.assertEqual(fixed.surface, "gavākṣaḥ")
        self.assertEqual(steps("go-akṣaḥ{vatayana}")[:2],
                         ["6.1.123", "6.1.101"])
        self.assertEqual(len(outcomes("go-akṣaḥ")), 3)

    def test_ekanta_iti_kim(self):
        """एङन्तस्य किम्? चित्रग्वग्रम् (Kaumudī): the word ends in उ, not ओ."""
        self.assertEqual(forms("citragu agram"), {"citragvagram"})
        self.assertEqual(steps("citragu agram"), ["6.1.77"])

    def test_the_word_go_and_not_a_word_ending_in_it(self):
        """हे चित्रगोऽग्रम् (Bālamanoramā): the ओ is made by guṇa (lākṣaṇika)."""
        self.assertEqual(steps("citrago{sambuddhi} agram"), ["6.1.109"])

    def test_padante_kim(self):
        """पदान्ते किम्? गवि, गोः (Kaumudī): the ओ is no pada's end."""
        self.assertEqual(steps("go~i"), ["6.1.78"])
        self.assertNotIn("6.1.123", sum(all_steps("go~as"), []))


# ---------------------------------------------------------------------------
# 6.1.115–121, 6.1.126 — the Vedic rules
# ---------------------------------------------------------------------------


class Vedic(Family):

    def test_the_vedic_rules_are_asleep_outside_the_veda(self):
        """The control: the same words, not Vedic."""
        self.assertEqual(steps("te{antahpada} agne"), ["6.1.109"])
        self.assertEqual(steps("uro{yajus} antarikṣam"), ["6.1.109"])

    def test_inside_a_pada_te_agne(self):
        """ते अग्ने अश्वमायुञ्जन्, उपप्रयन्तो अध्वरम्, सुजाते अश्वसूनृते
        (Kāśikā, Kaumudī on 6.1.115)."""
        for text, expected in (
                ("te{antahpada} agne", "te agne"),
                ("upaprayanto{antahpada} adhvaram", "upaprayanto adhvaram"),
                ("sujāte{antahpada} aśvasūnṛte", "sujāte aśvasūnṛte")):
            self.assertEqual(steps(text, veda=True), ["6.1.115"], text)
            self.assertEqual(outcomes(text, veda=True)[0].text(), expected)

    def test_the_step_says_what_prakrti_is(self):
        """प्रकृतिरिति स्वभावः … न विकारमापद्यते (Kāśikā)."""
        step = step_of("te{antahpada} agne", "6.1.115", veda=True)
        by = {a.sutra: a.why for a in step.against}
        self.assertIn("स्वभावेनावतिष्ठते, कारणात्मना वा भवति, न विकारमापद्यते",
                      by["6.1.109"])

    def test_antahpadam_iti_kim(self):
        """अन्तःपादं किम्? एतास एतेऽर्चन्ति (Kāśikā): the junction at the edge of
        the pāda — no flag, so purvarūpa."""
        self.assertEqual(forms("ete arcanti", veda=True), {"ete'rcanti"})

    def test_avyapare_iti_kim(self):
        """अव्यपरे किम्? तेऽवदन् (Kāśikā): a व् follows the अ."""
        self.assertEqual(steps("te{antahpada} avadan", veda=True), ["6.1.109"])
        self.assertEqual(forms("te{antahpada} avadan", veda=True),
                         {"te'vadan"})

    def test_the_seven_words_hold_although_a_va_or_ya_follows(self):
        """नो अव्यात्, शिवासो अवक्रमुः, नो अव्रत, शतधारो अयं मणिः, नो अवन्तु,
        कुशिकासो अवस्यवः (Kaumudī on 6.1.116)."""
        cases = (("no{sattva,antahpada} avyāt", "no avyāt"),
                 ("śivāso{antahpada} avakramuḥ", "śivāso avakramuḥ"),
                 ("no{sattva,antahpada} avrata", "no avrata"),
                 ("śatadhāro{antahpada} ayam", "śatadhāro ayam"),
                 ("no{sattva,antahpada} avantu", "no avantu"),
                 ("kuśikāso{antahpada} avasyavaḥ{stem:avasyu}",
                  "kuśikāso avasyavaḥ"))
        for text, expected in cases:
            self.assertEqual(steps(text, veda=True)[0], "6.1.116", text)
            self.assertEqual(outcomes(text, veda=True)[0].text(), expected)

    def test_a_word_not_in_the_list_is_purvarupa_when_a_va_follows(self):
        self.assertEqual(steps("te{antahpada} avadan", veda=True), ["6.1.109"])
        self.assertEqual(steps("ambe{antahpada} avadan", veda=True),
                         ["6.1.109"])

    def test_yajus_uro_antariksam(self):
        """उरो अन्तरिक्षम् (Kāśikā, Kaumudī on 6.1.117): no पाद is needed."""
        self.assertEqual(steps("uro{yajus} antarikṣam", veda=True),
                         ["6.1.117"])

    def test_the_six_words_of_6_1_118(self):
        """आपो अस्मान्मातरः, जुषाणो अग्निराज्यस्य, वृष्णो अंशुभ्याम्, वर्षिष्ठे अधि
        नाके, अम्बे अम्बाले अम्बिके (Kaumudī)."""
        for text in ("āpo{yajus} asmān", "juṣāṇo{yajus} agnirājyasya",
                     "vṛṣṇo{yajus} aṃśubhyām", "varṣiṣṭhe{yajus} adhi",
                     "ambe{yajus} ambāle", "ambāle{yajus} ambike"):
            self.assertEqual(steps(text, veda=True), ["6.1.118"], text)

    def test_ambe_only_before_ambika(self):
        """अम्बिकेपूर्वे: अम्बे is kept before अम्बाले, not before any अ."""
        self.assertEqual(steps("ambe{yajus} agre", veda=True), ["6.1.109"])

    def test_the_word_anga(self):
        """प्राणो अङ्गे अङ्गे अदीध्यत् (Kaumudī on 6.1.119)."""
        self.assertEqual(steps("prāṇo{yajus} aṅge", veda=True), ["6.1.119"])
        self.assertEqual(steps("aṅge{yajus} adīdhyat", veda=True)[0],
                         "6.1.119")

    def test_anudatte_ca_kudhapare(self):
        """अयं सो अग्निः, अयं सो अध्वरः (Kaumudī on 6.1.120)."""
        self.assertEqual(steps("so{yajus} agniḥ{anudatta}", veda=True)[0],
                         "6.1.120")
        self.assertEqual(steps("so{yajus} adhvaraḥ{anudatta}", veda=True)[0],
                         "6.1.120")

    def test_kudhapare_iti_kim(self):
        """कुधपरे किम्? सोऽयमग्निः (Kāśikā): no guttural or ध् follows the अ."""
        self.assertEqual(steps("so{yajus} ayam{anudatta}", veda=True),
                         ["6.1.109"])

    def test_anudatte_iti_kim(self):
        """अनुदात्ते किम्? अधोऽग्रे (Kāśikā): the अ is not anudātta — the
        accent is the caller's, and without it the junction closes."""
        self.assertEqual(steps("adho{yajus} agre", veda=True), ["6.1.109"])
        self.assertEqual(steps("so{yajus} adhvaraḥ", veda=True)[0], "6.1.109")

    def test_avapathah(self):
        """त्री रुद्रेभ्यो अवपथाः (Kāśikā on 6.1.121)."""
        text = "rudrebhyo{yajus} avapathāḥ{anudatta}"
        self.assertEqual(steps(text, veda=True)[0], "6.1.121")

    def test_yad_rudrebhyo_avapathah_the_accent_stays(self):
        """यद्रुद्रेभ्योऽवपथाः (Kāśikā): after यद्, 8.1.30 keeps the निघात off,
        so the अ is not anudātta and the junction closes."""
        text = "yad rudrebhyo{yajus} avapathāḥ"
        self.assertEqual(steps(text, veda=True)[0], "6.1.109")
        self.assertEqual(forms(text, veda=True), {"yadrudrebhyo'vapathāḥ"})

    def test_the_yajus_rules_need_the_yajus(self):
        self.assertEqual(steps("uro antarikṣam", veda=True), ["6.1.109"])

    def test_ang_before_a_vowel_is_nasal_and_stays(self):
        """अभ्र आँ अपः (Kāśikā, Kaumudī on 6.1.126). The अ and आ stay apart
        because the loss of the य् of *अभ्रस् आ* is asiddha to 6.1.101 — the
        junction to the left of the आङ् is settled first."""
        text = "abhras ā{ang} apaḥ"
        r = sandhi(text, veda=True)
        self.assertIn("abhra ā̐ apaḥ", {o.text() for o in r.outcomes})
        first = r.outcomes[0]
        self.assertIn("6.1.126", [s.sutra for s in first.steps])
        made = [s for s in first.final.segs if s.made_by == "6.1.126"]
        self.assertEqual([(s.s, s.nasal) for s in made], [("ā", True)])

    def test_the_step_of_ang_says_the_substitute_stays(self):
        step = step_of("abhras ā{ang} apaḥ", "6.1.126", veda=True)
        self.assertIn("6.1.125", [v.sutra for v in step.detail.via])
        by = {a.sutra for a in step.against}
        self.assertTrue(by)

    def test_ang_is_not_nasal_outside_the_veda(self):
        """The control: the Veda's āṅ only."""
        self.assertNotIn("6.1.126", sum(all_steps("abhras ā{ang} apaḥ"), []))

    def test_a_vowel_before_the_ang_joins_it_first(self):
        """The alternative input: with no loss between them the अ and आ are
        joined by 6.1.101 before the āṅ is looked at (OPEN in the docstring)."""
        self.assertEqual(forms("abhra ā{ang} apaḥ", veda=True), {"abhrāpaḥ"})


# ---------------------------------------------------------------------------
# 8.3.33 — the व् for उञ्
# ---------------------------------------------------------------------------


class UnBecomesVa(Family):

    def test_kim_u_uktam(self):
        """किमु उक्तम् = किम्वुक्तम् (Kaumudī, Laghukaumudī); तदु अस्य = तद्वस्य,
        शमु अस्तु = शम्वस्तु, किमु आवपनम् = किम्वावपनम् (Kāśikā)."""
        cases = (("kim u{nipata} uktam", {"kimvuktam", "kimuuktam"}),
                 ("tad u{nipata} asya", {"tadvasya", "taduasya"}),
                 ("śam u{nipata} astu", {"śamvastu", "śamuastu"}),
                 ("kim u{nipata} āvapanam", {"kimvāvapanam", "kimuāvapanam"}))
        for text, expected in cases:
            self.assertEqual(forms(text), expected, text)

    def test_the_two_courses_and_their_sutras(self):
        r = sandhi("kim u{nipata} uktam")
        self.assertEqual([s.sutra for s in r.outcomes[0].steps], ["8.3.33"])
        self.assertEqual([s.sutra for s in r.outcomes[1].steps
                          if not s.declined], ["6.1.125"])
        self.assertEqual(r.outcomes[0].steps[0].option, "वा")

    def test_it_is_the_exception_to_the_prakrtibhava_and_says_so(self):
        """प्रगृह्यः प्रकृत्येति प्रकृतिभावः प्राप्नोति (Bhāṣya on 8.3.33);
        प्रगृह्यत्वादुञः प्रकृतिभावे प्राप्ते वकारो विधीयते (Kāśikā)."""
        step = step_of("kim u{nipata} uktam", "8.3.33")
        by = {a.sutra: a.why for a in step.against}
        self.assertIn("प्रगृह्यः प्रकृत्येति प्रकृतिभावः प्राप्नोति",
                      by["6.1.125"])
        # the rules of vowel sandhi are set aside for the one step
        self.assertIn("6.1.77", by)
        self.assertIn("6.1.101", by)
        # 8.3.33's own reason for them is the Kāśikā's, declared on the rule
        rule = next(r for r in _rules() if r.sutra == "8.3.33")
        self.assertIn("प्रगृह्यत्वादुञः प्रकृतिभावे प्राप्ते वकारो विधीयते",
                      dict(rule.overrides)["@ac"])

    def test_the_va_is_asiddha_to_the_anusvara_rule(self):
        """वत्वस्यासिद्धत्वान्नानुस्वारः (Kaumudī): a rule of the tripādī that
        stands BEFORE 8.3.33 (8.3.23 मोऽनुस्वारः) sees the उ, not the व्, so the
        म् is not turned to an anusvāra."""
        final = outcomes("kim u{nipata} uktam")[0].final
        made = next(s for s in final.segs if s.made_by == "8.3.33")
        self.assertEqual(made.s, "v")
        self.assertEqual(
            [s.s for s in View(final, "8.3.23").live if s.w == 1], ["u"])
        self.assertEqual(
            [s.s for s in View(final, "8.4.40").live if s.w == 1], ["v"])
        self.assertNotIn("ṃ", [s.s for s in final.segs])

    def test_only_after_a_may_letter(self):
        """मयः: after a letter of the may pratyāhāra (a stop or a nasal). After
        a र् — or a vowel, which can only be a stand-in — the particle keeps
        the name and stays."""
        self.assertEqual(steps("punar u{nipata} uktam"), ["6.1.125"])

    def test_the_particle_only(self):
        """The control: an उ that is not flagged a particle has no name to
        displace and 8.3.33 is not for it."""
        self.assertNotIn("8.3.33", sum(all_steps("kim u uktam"), []))


# ---------------------------------------------------------------------------
# 6.1.131, 8.4.57
# ---------------------------------------------------------------------------


class Div(Family):

    def test_sudyubhyam(self):
        """सुद्युभ्याम्, सुद्युभिः (Kaumudī on 6.1.131): दिव् before a
        consonant-initial case-ending is a pada; its व् becomes उ, and yaṇ
        takes the इ."""
        for ending, expected in (("bhyām", "sudyubhyām"),
                                 ("bhis", "sudyubhiḥ")):    # the स् of भिस् is
            # pada-final, so 8.2.66 and 8.3.15 make it the visarga
            text = f"sudiv~{ending}"
            self.assertEqual(steps(text)[:2], ["6.1.131", "6.1.77"], text)
            self.assertEqual(forms(text), {expected})

    def test_the_step_cites_the_reason_it_is_a_pada(self):
        via = [v.sutra for v in step_of("sudiv~bhyām", "6.1.131").detail.via]
        self.assertIn("1.4.17", via)
        self.assertIn("1.1.70", via)          # the उ is tapara: short

    def test_a_compound_first_member_is_a_pada(self):
        """द्युकामः (Kāśikā): दिवि कामो यस्य."""
        self.assertEqual(steps("div-kāmaḥ")[:2], ["6.1.131", "6.1.77"])
        self.assertEqual(forms("div-kāmaḥ"), {"dyukāmaḥ"})

    def test_padasyeti_kim(self):
        """पदस्येति किम्? दिवौ, दिवः (Kāśikā): before a vowel-initial ending
        the stem is not a pada."""
        self.assertEqual(forms("div~au"), {"divau"})
        self.assertNotIn("6.1.131", sum(all_steps("div~au"), []))

    def test_the_root_is_not_meant(self):
        """दिव इति प्रातिपदिकं गृह्यते न धातुः, सानुबन्धकत्वात् — अक्षद्यूभ्याम्
        (Kāśikā): the flag says the दिव् is the root, and nothing is done."""
        text = "akṣadiv{dhatu:div}~bhyām"
        self.assertNotIn("6.1.131", sum(all_steps(text), []))
        self.assertEqual(forms(text), {"akṣadivbhyām"})


class Nasal(Family):

    def test_dadhi(self):
        """दधिँ, दधि; मधुँ, मधु; कुमारीँ, कुमारी (Kāśikā on 8.4.57)."""
        for word in ("dadhi", "madhu", "kumārī"):
            r = sandhi(f"{word}{{anunasika}}")
            self.assertEqual(len(r.outcomes), 2, word)
            first, second = r.outcomes
            self.assertEqual([s.s for s in first.final.segs if s.nasal],
                             [word[-1]], word)
            self.assertEqual(first.steps[0].option, "वा")
            self.assertEqual(second.text(), word)
            self.assertTrue(second.steps[0].declined)

    def test_the_option_is_offered_on_request_only(self):
        """The reason, checked: the option returns its taken course first, and
        every word's pausal form is asked of the engine by `split`."""
        self.assertEqual(len(outcomes("dadhi")), 1)
        self.assertEqual(steps("dadhi"), [])

    def test_an_iti_adi_with_the_request_on_the_last_word(self):
        self.assertEqual({o.text() for o in outcomes("iti ādi{anunasika}")},
                         {"ity ādi̐", "ity ādi"})

    def test_an_iti_kim_kartr(self):
        """अण इति किम्? कर्तृ, हर्तृ (Kāśikā): ṛ is no aṇ."""
        self.assertEqual(steps("kartṛ{anunasika}"), [])
        self.assertEqual(steps("hartṛ{anunasika}"), [])

    def test_apragrhya_iti_kim(self):
        """अप्रगृह्यस्येति किम्? अग्नी, वायू (Kāśikā, Kaumudī): a pragṛhya vowel
        is not nasalised."""
        self.assertEqual(steps("agnī{dvivacana,anunasika}"), [])
        self.assertEqual(steps("vāyū{dvivacana,anunasika}"), [])
        # the control: a short इ of a word not called dual is
        self.assertEqual(steps("agni{dvivacana,anunasika}"), ["8.4.57"])

    def test_the_anunasika_is_a_mark_and_the_sound_is_the_same(self):
        final = outcomes("dadhi{anunasika}")[0].final
        self.assertEqual("".join(base_of(s.sound) for s in final.segs),
                         "dadhi")

    def test_not_before_a_following_word(self):
        """At a pause only: with a word after it the vowel is not at the
        अवसान (1.4.110)."""
        self.assertEqual(steps("dadhi{anunasika} atra", pause=True),
                         ["6.1.77"])
        self.assertEqual(steps("dadhi{anunasika}", pause=False), [])


# ---------------------------------------------------------------------------
# infer.py
# ---------------------------------------------------------------------------


def _flags(text, **kw):
    return [f for f, _ in infer_flags(
        text, position=kw.pop("position", 0), words=kw.pop("words", [text, "x"]),
        given=kw.pop("given", frozenset()), **kw)]


class Infer(Family):

    def test_the_gana_is_read_from_the_ganapatha_not_typed(self):
        listed = {item for gana in corpus.ganas_for(CADI)
                  for item in gana.items}
        self.assertEqual(gana_words(CADI), frozenset(listed))
        self.assertGreater(len(gana_words(CADI)), 100)
        self.assertIn("aho", gana_words(CADI))
        self.assertIn("pra", gana_words(PRADI))
        # the module writes no list of its own: no literal collection of words
        import ast
        import inspect
        from src.astadhyayi.sandhi import infer
        tree = ast.parse(inspect.getsource(infer))
        listed = (gana_words(CADI) | gana_words(PRADI)
                  | gana_words(SVARADI))
        for node in ast.walk(tree):
            if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
                strings = {e.value for e in node.elts
                           if isinstance(e, ast.Constant)
                           and isinstance(e.value, str)}
                self.assertEqual(strings & listed, set(), strings)

    def test_a_word_of_the_cadi_gana_is_a_nipata_and_says_why(self):
        found = dict(infer_flags("aho", position=0, words=["aho", "īśāḥ"],
                                 given=frozenset()))
        self.assertIn("nipata", found)
        self.assertIn("1.4.57", found["nipata"])
        self.assertIn("cādi", found["nipata"])
        self.assertIn("sattva", found["nipata"])     # the asattve condition

    def test_a_word_of_the_pradi_gana_likewise(self):
        found = dict(infer_flags("pra", position=0, words=["pra", "x"],
                                 given=frozenset()))
        self.assertIn("1.4.58", found["nipata"])

    def test_the_source_sutra_is_named_from_the_gana(self):
        self.assertEqual(nipata_source("aho"), CADI)
        self.assertEqual(nipata_source("pra"), PRADI)
        self.assertIsNone(nipata_source("rāma"))

    def test_absence_from_the_gana_proves_nothing_and_nothing_is_withheld(self):
        """The cādi gaṇa is an ākṛtigaṇa: a word that is not listed is not
        thereby not a particle, and no flag is claimed for it."""
        self.assertEqual(_flags("rāma"), [])
        self.assertEqual(_flags("kṛṣṇa"), [])

    def test_the_callers_flag_wins_and_sattva_takes_it_away(self):
        self.assertEqual(_flags("aho", given=frozenset({"nipata"})), [])
        self.assertEqual(_flags("aho", given=frozenset({"sattva"})), [])
        self.assertEqual(_flags("no", given=frozenset({"sattva"})), [])
        self.assertEqual(_flags("no"), ["nipata"])

    def test_a_one_vowel_word_is_not_inferred_to_be_a_particle(self):
        """1.1.14's a, i, u are in the cādi gaṇa, and the engine's own tests
        use bare vowels as stand-ins for a word-final sound (`i a`). The
        caller says `{nipata}`; the reason is in COVERAGE."""
        for vowel in ("i", "u", "a", "e", "o", "ai", "au", "ṛ", "ḷ"):
            self.assertIn(vowel, gana_words(CADI), vowel)
            self.assertEqual(_flags(vowel), [], vowel)
        self.assertIn("1.4.57", {s for s, _, _ in family.COVERAGE})

    def test_ang_is_not_inferred_from_the_letter(self):
        """A bare आ is either the preverb or the particle; the letters cannot
        say (Kāśikā on 1.1.14: ईषदर्थे क्रियायोगे …)."""
        self.assertEqual(_flags("ā"), [])

    def test_a_preverb_is_proved_by_the_boundary(self):
        """A prādi word before a dhātu across `|` is an upasarga (1.4.59
        क्रियायोगे)."""
        flags = _flags("pra", words=["pra", "nayati"],
                       bounds=["upasarga", "avasana"])
        self.assertIn("upasarga", flags)
        self.assertIn("nipata", flags)
        self.assertNotIn("upasarga", _flags("pra", words=["pra", "nayati"],
                                            bounds=["pada", "avasana"]))
        self.assertNotIn("upasarga", _flags("rāma", words=["rāma", "x"],
                                            bounds=["upasarga", "avasana"]))

    def test_the_preverb_aa_is_ang_by_the_boundary(self):
        flags = _flags("ā", words=["ā", "udakāntāt"],
                       bounds=["upasarga", "avasana"])
        self.assertIn("upasarga", flags)
        self.assertIn("ang", flags)

    def test_the_visarga_of_a_svaradi_word_is_r(self):
        """पुनः, अन्तः, प्रातः are the स्वरादि's पुनर्, अन्तर्, प्रातर् (1.1.37): the
        closed class of r-final indeclinables, read from the gaṇapāṭha."""
        for word in ("punaḥ", "antaḥ", "prātaḥ"):
            found = dict(infer_flags(word, position=0, words=[word, "x"],
                                     given=frozenset()))
            self.assertIn("final:r", found, word)
            self.assertIn("1.1.37", found["final:r"])
        self.assertIn("punar", gana_words(SVARADI))
        self.assertNotIn("punas", gana_words(SVARADI))

    def test_a_visarga_that_is_s_is_proved_where_the_class_says_so(self):
        found = dict(infer_flags("uccaiḥ", position=0, words=["uccaiḥ", "x"],
                                 given=frozenset()))
        self.assertIn("final:s", found)

    def test_a_visarga_of_a_word_outside_the_class_is_not_guessed(self):
        self.assertEqual(_flags("rāmaḥ"), [])
        self.assertEqual(_flags("punaḥ", given=frozenset({"final:s"})), [])

    def test_the_inference_reaches_the_engine_and_the_trace_says_so(self):
        """`parse` records each inference on the word, so the trace prints it
        as an assumption and not as something the caller said."""
        state = parse("aho īśāḥ")
        self.assertIn("nipata", state.words[0].flags)
        self.assertEqual([f for f, _ in state.words[0].inferred], ["nipata"])
        self.assertEqual(parse("aho{nipata} īśāḥ").words[0].inferred, ())
        self.assertEqual(parse("aho īśāḥ", infer=False).words[0].flags,
                         frozenset())
        r = sandhi("punaḥ atra")                    # punar, so no 6.1.113
        self.assertNotIn("6.1.113", [s.sutra for s in r.outcomes[0].steps])
        self.assertTrue(any("final:r" in a and "1.1.37" in a
                            for a in trace.assumptions(r.outcomes[0])))

    def test_a_word_of_no_sounds_is_left_to_parse_to_refuse(self):
        """infer reads sounds; a malformed word must reach parse's own error."""
        from src.astadhyayi.sandhi import SandhiInputError
        with self.assertRaises(SandhiInputError):
            sandhi("hare 'va")


# ---------------------------------------------------------------------------
# the family and the rest of the engine
# ---------------------------------------------------------------------------


class WholeRulebook(Family):
    """The family among every family: whatever the consonant rules add to a
    form, the steps of THIS family's sūtras are the same."""

    def test_this_familys_steps_do_not_depend_on_the_other_families(self):
        mine = {r.sutra for r in family.RULES}
        cases = (
            ("harī{dvivacana} etau", {}, ["6.1.125"]),
            ("amī{adas} īśāḥ", {}, ["6.1.125"]),
            ("aho īśāḥ", {}, ["6.1.125"]),
            ("kṛṣṇa{pluta} atra", {}, ["6.1.125"]),
            ("suśloka{pluta} iti", {}, ["6.1.129"]),
            ("go indraḥ", {}, ["6.1.124"]),
            ("go-akṣaḥ{vatayana}", {}, ["6.1.123"]),
            ("kim u{nipata} uktam", {}, ["8.3.33"]),
            ("dadhi{sakalya} atra", {}, ["6.1.127"]),
            ("brahmā{sakalya} ṛṣiḥ", {}, ["6.1.128"]),
            ("te{antahpada} agne", {"veda": True}, ["6.1.115"]),
            ("sudiv~bhyām", {}, ["6.1.131"]),
            ("dadhi{anunasika}", {}, ["8.4.57"]),
        )
        for text, kw, expected in cases:
            first = _sandhi(text, **kw).outcomes[0]
            got = [s.sutra for s in first.steps if s.sutra in mine]
            self.assertEqual(got, expected, text)

    def test_the_junctions_no_flag_reaches_are_not_touched(self):
        """Not one of this family's sūtras appears where nothing it reads is
        said: the ordinary sandhi of the whole rulebook is as it was."""
        mine = {r.sutra for r in family.RULES}
        for text in ("iti ādi", "agni indra", "hare ava", "kṛṣṇa aikya",
                     "rāmas atra", "manas ratha", "punar ramate", "vāc pati",
                     "mahā ṛṣi", "haras iha", "rāmas ca", "tad ca"):
            for o in _sandhi(text).outcomes:
                self.assertEqual([s.sutra for s in o.steps
                                  if s.sutra in mine], [], text)


class Interlock(Family):

    def test_the_project_codification_agrees_with_the_engine(self):
        """`prakrtibhava.stands_open` is 6.1.115–134 as a question. For each
        case the rule the engine cites is the sūtra it answers."""
        cases = (
            (("te{antahpada} agne", True), "6.1.115",
             dict(after="eṅ", before="at", result="antaḥpāda",
                  chandasi=True)),
            (("śatadhāro{antahpada} ayam", True), "6.1.116",
             dict(after="eṅ", before="avyādi", result="antaḥpāda",
                  chandasi=True)),
            (("uro{yajus} antarikṣam", True), "6.1.117",
             dict(stem="uras", before="at", yajusi=True)),
            (("āpo{yajus} asmān", True), "6.1.118",
             dict(stem="āpo", before="at", yajusi=True)),
            (("prāṇo{yajus} aṅge", True), "6.1.119",
             dict(stem="aṅga", before="at", yajusi=True)),
            (("go agram", False), "6.1.122", dict(stem="go", before="at")),
            (("go indraḥ", False), "6.1.124", dict(stem="go",
                                                   before="indra")),
            (("sudiv~bhyām", False), "6.1.131", dict(stem="div",
                                                     result="pada")),
        )
        for (text, veda), sutra, question in cases:
            self.assertEqual(stands_open(**question).sutra, sutra, sutra)
            cited_by_engine = {s.sutra for o in outcomes(text, veda=veda)
                               for s in o.steps}
            self.assertIn(sutra, cited_by_engine, (text, sutra))

    def test_every_derivation_of_a_flagged_junction_terminates_cleanly(self):
        """Whatever two vowels meet, under every flag this family reads, the
        engine answers with sounds and real sūtras and does not cycle."""
        known = corpus.load_vidyut_sutrapatha()
        vowels = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au")
        flagsets = ("", "{dvivacana}", "{nipata}", "{sambuddhi}", "{pluta}",
                    "{sakalya}", "{ang}", "{antahpada}", "{yajus}",
                    "{nipata,pluta}")
        inventory = set(AC) | {"'", "y", "v", "r", "l", "m", "n", "s", "ṃ",
                               "ḥ", "t", "d", "k", "g", "c", "j", "ṭ", "ḍ",
                               "ś", "ṣ", "h", "p", "b", "ñ", "ṅ", "ṇ"}
        count = 0
        for veda in (False, True):
            for left in vowels:
                for flags in flagsets:
                    for right in ("a", "ā", "i", "ṛ", "e", "o", "au"):
                        result = sandhi(f"k{left}{flags} {right}ta",
                                        veda=veda)
                        for outcome in result.outcomes:
                            self.assertNotIn("cycling", outcome.stopped)
                            self.assertNotIn("cap", outcome.stopped)
                            for seg in outcome.final.segs:
                                self.assertIn(seg.s, inventory | {""},
                                              (left, flags, right, seg.s))
                            for step in outcome.steps:
                                for sutra in step.sutras:
                                    self.assertIn(sutra, known)
                        count += 1
        self.assertGreater(count, 1500)

    def test_the_engines_own_junctions_are_unchanged_by_the_family(self):
        """The family must not touch a form that says nothing it reads."""
        self.assertEqual(steps("iti ādi"), ["6.1.77"])
        self.assertEqual(steps("agni indra"), ["6.1.101"])
        self.assertEqual(steps("hare ava"), ["6.1.109"])
        self.assertEqual(steps("kṛṣṇa aikya"), ["6.1.88"])
        self.assertEqual(steps("sa a i"), ["6.1.101", "6.1.87"])

    def test_a_derivation_is_still_in_the_millisecond_range(self):
        sandhi("iti ādi")
        for text, kw in (("iti ādi", {}), ("harī{dvivacana} etau", {}),
                         ("go agram", {}), ("abhras ā{ang} apaḥ",
                                            {"veda": True})):
            start = time.perf_counter()
            for _ in range(20):
                sandhi(text, **kw)
            per_call = (time.perf_counter() - start) / 20
            self.assertLess(per_call, 0.05, (text, per_call))

    def test_the_result_serialises_with_both_scripts(self):
        r = sandhi("vāyo{sambuddhi} iti")
        data = json.loads(json.dumps(r.to_dict(), ensure_ascii=False))
        self.assertEqual(len(data["outcomes"]), 3)
        first = data["outcomes"][0]["steps"][0]
        self.assertEqual(first["sutra"], "6.1.125")
        self.assertEqual(first["option"], "शाकल्यस्य")
        self.assertIn("प्लुतप्रगृह्या", first["sutra_deva"])
        self.assertEqual(first["via"][0]["sutra"], "1.1.16")

    def test_a_trace_prints_every_term_in_both_scripts(self):
        out = sandhi("harī{dvivacana} etau").trace()
        self.assertIn("प्रगृह्य (pragṛhya)", out)
        self.assertIn("ईदूदेद्द्विवचनं प्रगृह्यम् (īdūdeddvivacanaṃ pragṛhyam)",
                      out)
        self.assertIn("6.1.125 प्लुतप्रगृह्या अचि नित्यम्", out)
        self.assertIn("हरी एतौ (harī etau)", out)

    def test_the_pluta_and_pragrhya_words_of_the_flags_are_not_letters(self):
        """No rule of this family tabulates a pairing or a class: the two
        repository guards read every source file."""
        import pathlib
        text = pathlib.Path(
            "src/astadhyayi/sandhi/families/prakrtibhava.py").read_text(
                encoding="utf-8")
        for pair in ('"i": "y"', "'i': 'y'", '"u": "v"', "'u': 'v'",
                     '"i": "e"', "'i': 'e'", '"c": "k"', "'c': 'k'"):
            self.assertNotIn(pair, text)


if __name__ == "__main__":
    unittest.main()
