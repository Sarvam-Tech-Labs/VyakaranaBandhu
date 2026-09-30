# -*- coding: utf-8 -*-
"""
The nasal family — 8.3.1–7, 8.3.23–33, 8.4.45, 8.4.58–59, with 1.1.46 and 1.1.47
— tested against the commentaries' own words.

Each expectation is a worked example, or a counter-example (*X iti kim?*), that
the Kāśikā, the Siddhāntakaumudī, the Laghusiddhāntakaumudī, the Bālamanoramā or
the Tattvabodhinī gives, and the docstring of the test names which. Where a
result could come out right by luck the test also asserts the STEPS — the
sūtras, in order — because in the tripādī the order is the grammar (8.2.1).

**Most tests derive under this family's rules and the visarga family's**
(`mine`), so that they are about *these* rules and stay true when the other
families are merged in. The visarga family is there only so that a final स् of
the input is read as the visarga the commentary prints. Where the commentary's
form needs a rule of another family — the visarga and the स् the रु becomes
(8.3.15, 8.3.34), the हल् family's जश्त्व and ष्टुत्व — the test asserts the
point where THIS family leaves the form (`Step.after`) and the steps this
family takes, and says so: the end-to-end form is for the integration tests.

A test that cannot fail is worse than none (NORTH_STAR §3): the last classes
take a provision OUT and show the answer change.
"""

from __future__ import annotations

import re
import time
import unittest
from dataclasses import replace

from src.astadhyayi import corpus, reading, ru_anunasika
from src.astadhyayi.adesa import AgamaSite
from src.astadhyayi.sandhi import rulebook, sandhi, trace
from src.astadhyayi.sandhi.engine import derive
from src.astadhyayi.sandhi.families import nasal_anusvara as N
from src.astadhyayi.sandhi.parse import parse
from src.astadhyayi.sandhi.rule import (
    ADESA, AGAMA_KIND, PRATISEDHA, VARTTIKA, Application, Detail,
    replace as edit_replace, rule as make_rule, site)
from src.astadhyayi.sandhi.segs import AGAMA, RU, Seg, View
from src.astadhyayi.varna import ANUNASIKA_MARK, ANUSVARA, VARGA, is_anunasika

FAMILY = "nasal_anusvara"
MY = frozenset(r.sutra for r in N.RULES)

#: Who else states *saṃpuṃkānāṃ so vaktavyaḥ*: the visarga family states it on
#: the visarga where it is there, and then this family stands aside.
SAMPUMKA_ELSEWHERE = N._ELSEWHERE[("8.3.5", N._SAMPUMKA)]
#: What this family's steps are for सम् and पुम् after 8.3.2 or 8.3.4.
VT = [] if SAMPUMKA_ELSEWHERE else ["8.3.5v"]

#: The nasal forms the Laghukaumudī prints with a candrabindu.
NY, NV, NL = ("y" + ANUNASIKA_MARK, "v" + ANUNASIKA_MARK, "l" + ANUNASIKA_MARK)
NA, NI, NU_, NAA = ("a" + ANUNASIKA_MARK, "i" + ANUNASIKA_MARK,
                    "u" + ANUNASIKA_MARK, "ā" + ANUNASIKA_MARK)


def mine(text, *extra, **kw):
    """The junction derived by this family's rules and the visarga family's
    (so a final स् is read as the visarga), and any further family named."""
    return sandhi(text, rules=rulebook.rules_of(FAMILY, "visarga_ru", *extra),
                  **kw)


def alone(text, **kw):
    """This family's rules and no others."""
    return sandhi(text, rules=rulebook.rules_of(FAMILY), **kw)


def label(found):
    """A step's name: its sūtra, a `v` after it for a vārttika on that sūtra,
    and a star for an option declined."""
    return (found.sutra + ("v" if found.detail.authority == VARTTIKA else "")
            + ("*" if found.declined else ""))


def steps(result, course=0):
    """The steps of one course, in order (see `label`)."""
    return [label(s) for s in result.outcomes[course].steps]


def ours(result, course=0):
    """The steps THIS family took in one course."""
    return [s for s in steps(result, course)
            if s.rstrip("*").rstrip("v") in MY]


def step(result, sutra, course=0):
    """The step that applied `sutra` in that course (not the declined one);
    `8.3.5v` asks for the vārttika."""
    want = sutra.rstrip("v")
    for found in result.outcomes[course].steps:
        if found.sutra == want and not found.declined and (
                (found.detail.authority == VARTTIKA) == sutra.endswith("v")
                or not sutra.endswith("v")):
            return found
    raise AssertionError(f"{sutra} did not apply in course {course}: "
                         f"{steps(result, course)}")


def maya(text, **kw):
    """A junction under whichever family holds 8.3.33: this one, or — where
    the prakṛtibhāva family has it and this one stands aside — that one too."""
    other = [N._MAYA_ELSEWHERE] if N._MAYA_ELSEWHERE else []
    return sandhi(text, rules=rulebook.rules_of(FAMILY, *other), **kw)


def surfaces(text, *extra, **kw):
    return set(mine(text, *extra, **kw).surfaces)


def head(after, words=2):
    """The first words of a step's text: a final visarga of the input is read
    as the स् it came from and shows as one until the visarga family has acted,
    so the tests read only as far as the junction."""
    return " ".join(after.split()[:words])


def made_by(result, sutra, course=0):
    return [s for s in result.outcomes[course].final.segs
            if s.made_by == sutra]


# ---------------------------------------------------------------------------
# The record itself: numbers, names, quotations, coverage
# ---------------------------------------------------------------------------

_MARKUP = re.compile(r"<<|>>|\[\[[^\]]*\]\]|<\{[^}]*\}>|<!|!>|</?w>|\(\d+\)|\s+")


def norm(text):
    """A commentary's words without the corpus's own markup and spacing — so a
    quotation is compared with what the commentary says, not how it is set."""
    return _MARKUP.sub("", text or "")


SCOPE = (
    [f"8.3.{n}" for n in range(1, 8)] + [f"8.3.{n}" for n in range(23, 34)]
    + ["8.4.45", "8.4.58", "8.4.59", "1.1.46", "1.1.47"])


class TheRecord(unittest.TestCase):
    """Every number, name and quotation is the corpus's and the commentary's
    own — none was written from memory."""

    def test_the_rulebook_is_sound_with_this_family_loaded(self):
        self.assertEqual(rulebook.problems(), [])

    def test_every_rule_is_named_by_its_own_words_from_the_corpus(self):
        known = corpus.load_vidyut_sutrapatha()
        for r in N.RULES:
            self.assertIn(r.sutra, known)
            self.assertEqual(r.name, trace.deva(known[r.sutra].text), r.sutra)

    def test_coverage_names_every_sutra_of_the_scope_once_and_no_other(self):
        listed = [sutra for sutra, _, _ in N.COVERAGE]
        self.assertEqual(sorted(listed), sorted(set(listed)))
        self.assertEqual(set(listed), set(SCOPE))
        self.assertEqual(len(listed), 23)

    def test_8_3_34_belongs_to_the_visarga_family_and_is_not_here(self):
        self.assertNotIn("8.3.34", {s for s, _, _ in N.COVERAGE})
        self.assertNotIn("8.3.34", MY)

    def test_a_sutra_is_not_called_a_rule_unless_a_rule_stands_for_it(self):
        have = {r.sutra for r in N.RULES}
        for sutra, status, note in N.COVERAGE:
            if status in ("rule", "partial", "vedic") and sutra != "1.1.46":
                self.assertIn(sutra, have, sutra)
            if status in ("support", "scope"):
                self.assertNotIn(sutra, have, sutra)
            if status in ("scope", "partial"):
                self.assertGreater(len(note), 20, sutra)

    def test_the_two_paribhasas_are_a_support_and_a_scope_with_reasons(self):
        got = {s: (st, n) for s, st, n in N.COVERAGE}
        self.assertEqual(got["1.1.46"][0], "support")
        self.assertEqual(got["1.1.47"][0], "scope")
        self.assertIn("mit", got["1.1.47"][1])

    def test_1_1_46_is_cited_by_every_augment_step(self):
        for text in ("prāṅ śete", "ṣaḍ santaḥ", "san śambhuḥ",
                     "pratyaṅ ātmā", "bhavān sāye"):
            first = [s for s in mine(text).outcomes[0].steps
                     if s.sutra in MY][0]
            self.assertEqual(first.detail.kind, AGAMA_KIND, text)
            self.assertIn("1.1.46", [v.sutra for v in first.detail.via], text)

    def test_1_1_47_is_never_cited_since_no_augment_here_is_a_mit(self):
        for text in ("prāṅ śete", "ṣaḍ santaḥ", "san śambhuḥ",
                     "pratyaṅ ātmā", "sam|skartā{sut}", "pum kokilaḥ"):
            for outcome in mine(text).outcomes:
                for found in outcome.steps:
                    self.assertNotIn("1.1.47", found.sutras, text)

    def test_only_the_two_vedic_sutras_are_vedic(self):
        vedic = {r.sutra for r in N.RULES if r.vedic}
        self.assertEqual(vedic, {"8.3.1", "8.3.3"})
        got = {s: st for s, st, _ in N.COVERAGE}
        self.assertEqual(got["8.3.1"], "vedic")
        self.assertEqual(got["8.3.3"], "vedic")

    def test_every_rule_carries_the_family_tags_the_others_look_for(self):
        for r in N.RULES:
            self.assertIn("nasal", r.families, r.sutra)
        for sutra in ("8.3.1", "8.3.5", "8.3.6", "8.3.7"):
            rr = next(r for r in N.RULES if r.sutra == sutra)
            self.assertIn("visarga", rr.families, sutra)
        for sutra in ("8.3.28", "8.3.29", "8.3.30", "8.3.31", "8.3.32"):
            rr = next(r for r in N.RULES if r.sutra == sutra)
            self.assertIn("agama", rr.families, sutra)
        for sutra in ("8.3.23", "8.3.24", "8.4.45", "8.4.58", "8.4.59"):
            rr = next(r for r in N.RULES if r.sutra == sutra
                      and r.authority != VARTTIKA)
            self.assertIn("hal", rr.families, sutra)

    def test_every_vartika_carries_the_corpus_words_and_says_it_is_one(self):
        found = [r for r in N.RULES if r.authority == VARTTIKA]
        self.assertEqual({r.sutra for r in found},
                         {"8.3.26", "8.4.45"}
                         | (set() if SAMPUMKA_ELSEWHERE else {"8.3.5"}))
        for r in found:
            self.assertIn(r.varttika,
                          [v.text for v in corpus.varttikas_on(r.sutra)])

    def test_every_quotation_is_in_the_commentary_it_names(self):
        self.assertGreater(len(N.QUOTED), 8)
        for source, sutra, text in N.QUOTED:
            found = corpus.commentary_on(sutra, source)
            self.assertIsNotNone(found, (source, sutra))
            self.assertIn(norm(text), norm(found), (source, sutra, text))

    def test_a_quotation_that_is_not_the_commentary_s_would_be_caught(self):
        """The check above must be able to fail."""
        found = corpus.commentary_on("8.3.25", "kashika")
        self.assertNotIn(norm("मकारस्य ननकारवचनमनुस्वारनिवृत्त्यर्थम्"),
                         norm(found))
        self.assertIn(norm("मकारस्य मकारवचनमनुस्वारनिवृत्त्यर्थम्"),
                      norm(found))

    def test_every_reason_an_override_gives_quotes_the_commentary(self):
        """`overrides` carries the tradition's reason, verbatim: each reason
        contains one of the recorded quotations."""
        for r in N.RULES:
            for target, why in r.overrides:
                self.assertTrue(
                    any(text in why for _, _, text in N.QUOTED),
                    (r.sutra, target))

    def test_every_sutra_a_step_cites_is_in_the_corpus(self):
        known = corpus.load_vidyut_sutrapatha()
        for text in ("harim vande", "sam|skartā{sut}", "kim hmalayati",
                     "prāṅ śete", "pratyaṅ ātmā", "yaśān~si", "kim u{nipata} uktam"):
            for outcome in mine(text).outcomes:
                for found in outcome.steps:
                    for sutra in found.sutras:
                        self.assertIn(sutra, known, (text, sutra))
                    for lost in found.against:
                        self.assertIn(lost.sutra, known, (text, lost.sutra))


# ---------------------------------------------------------------------------
# 8.3.23 मोऽनुस्वारः and 8.3.24 नश्चापदान्तस्य झलि
# ---------------------------------------------------------------------------


class Anusvara(unittest.TestCase):

    def test_hariṃ_vande_8_3_23(self):
        """Laghusiddhāntakaumudī on 8.3.23 (and Kaumudī): हरिं वन्दे. The म् ends a
        pada and a हल् follows. (8.4.59 then gives its option, the second form.)"""
        r = mine("harim vande")
        self.assertEqual(ours(r, 1), ["8.3.23", "8.4.59*"])
        self.assertEqual(r.outcomes[1].text(), "hariṃ vande")
        found = step(r, "8.3.23", 1)
        self.assertEqual((found.detail.sthanin, found.detail.adesa),
                         ("m", ANUSVARA))
        self.assertEqual(found.after, "hariṃ vande")

    def test_kuṇḍaṃ_hasati_and_vanaṃ_yāti_8_3_23(self):
        """Kāśikā on 8.3.23: कुण्डं हसति, वनं हसति, कुण्डं याति, वनं याति."""
        for text, expected in (("kuṇḍam hasati", "kuṇḍaṃhasati"),
                               ("vanam hasati", "vanaṃhasati")):
            self.assertEqual(surfaces(text), {expected}, text)
        for text in ("kuṇḍam yāti", "vanam yāti"):
            r = mine(text)
            self.assertEqual(ours(r, 0)[0], "8.3.23", text)

    def test_the_m_is_not_changed_before_a_vowel_halīti_kim(self):
        """Kāśikā on 8.3.23: हलीत्येव — त्वमत्र, किमत्र."""
        for text in ("tvam atra", "kim atra"):
            self.assertEqual(ours(mine(text)), [], text)
            self.assertNotIn(ANUSVARA, mine(text).surface, text)

    def test_the_m_is_not_changed_inside_a_pada_padantasyeti_kim(self):
        """Kāśikā on 8.3.23: पदान्तस्येत्येव — गम्यते, रम्यते. The two pieces of one
        pada are written with `~`, so the म् ends a piece and not a pada."""
        for text in ("gam~yate", "ram~yate"):
            self.assertEqual(ours(mine(text)), [], text)

    def test_the_m_at_a_pause_is_left_alone(self):
        """No हल् follows a pause, so 8.3.23 has nothing to see."""
        self.assertEqual(ours(mine("harim")), [])

    def test_the_word_is_a_pada_before_a_compound_and_a_preverb_too(self):
        """1.4.14 with 1.1.62: the first member of a compound and a preverb are
        padas, so their final म् is pada-final (सम्, किम्)."""
        self.assertEqual(ours(mine("kim-cid"))[0], "8.3.23")
        self.assertEqual(ours(mine("sam|kṛ"))[0], "8.3.23")

    def test_yaśāṃsi_and_ākraṃsyate_8_3_24(self):
        """Kāśikā on 8.3.24: यशांसि, पयांसि, सर्पींषि, धनूंषि; for the म् आक्रंस्यते,
        आचिक्रंसते, अधिजिगांसते. The न् or म् ends the first of two pieces of one
        pada (`~`) and a झल् begins the second."""
        for text, expected in (
                ("yaśān~si", "yaśāṃsi"), ("payān~si", "payāṃsi"),
                ("sarpīn~ṣi", "sarpīṃṣi"), ("dhanūn~ṣi", "dhanūṃṣi"),
                ("ākram~syate", "ākraṃsyate"), ("ācikram~sate", "ācikraṃsate"),
                ("adhijigām~sate", "adhijigāṃsate")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(ours(r), ["8.3.24"], text)

    def test_a_pada_final_n_is_not_changed_apadantasyeti_kim(self):
        """Kāśikā on 8.3.24: अपदान्तस्येति किम्? राजन् भुङ्क्ष्व."""
        self.assertEqual(ours(mine("rājan bhuṅkṣva")), [])
        self.assertEqual(mine("rājan bhuṅkṣva").surface, "rājanbhuṅkṣva")

    def test_a_non_jhal_is_not_enough_jhalīti_kim(self):
        """Kāśikā on 8.3.24: झलीति किम्? रम्यते, गम्यते (Kaumudī: मन्यते) — a य् is
        not a झल्."""
        for text in ("man~yate", "ram~yate", "gam~yate"):
            self.assertEqual(ours(mine(text)), [], text)

    def test_the_anusvara_of_8_3_24_is_a_step_of_that_sutra(self):
        found = step(mine("yaśān~si"), "8.3.24")
        self.assertEqual((found.detail.sthanin, found.detail.adesa),
                         ("n", ANUSVARA))
        self.assertEqual(found.before, "yaśān si")
        self.assertEqual(found.after, "yaśāṃ si")

    def test_a_visarga_or_an_avasana_is_not_a_hal(self):
        """The right-hand sound must be a consonant: a visarga is not one."""
        self.assertEqual(ours(mine("kim ḥ")), [])


# ---------------------------------------------------------------------------
# 8.3.25 सम्राट् — an anusvāra held back — and 8.3.26, 8.3.27
# ---------------------------------------------------------------------------

RAJ = "rāj{dhatu:rāj,kvip}"


class AnusvaraHeldBack(unittest.TestCase):

    def test_samrāṭ_8_3_25(self):
        """Kāśikā and Laghusiddhāntakaumudī on 8.3.25: सम्राट्, the म् of सम् kept
        before राज् with क्विप्. (The final ज् is the हल् family's.)"""
        r = mine(f"sam|{RAJ}")
        self.assertEqual(ours(r), ["8.3.25"])
        self.assertNotIn("8.3.23", steps(r))
        self.assertTrue(r.surface.startswith("samrā"), r.surface)
        self.assertNotIn(ANUSVARA, r.surface)

    def test_it_is_a_refusal_at_the_very_place_of_8_3_23(self):
        """मकारस्य मकारवचनमनुस्वारनिवृत्त्यर्थम् (Kāśikā): म् for म् changes nothing
        and is there only to keep 8.3.23 out — an application with no edit,
        which the trace shows as a pratiṣedha displacing 8.3.23."""
        r = mine(f"sam|{RAJ}")
        found = step(r, "8.3.25")
        self.assertEqual(found.detail.kind, PRATISEDHA)
        self.assertEqual(found.before, found.after)
        self.assertEqual((found.detail.sthanin, found.detail.adesa), ("m", "m"))
        against = {a.sutra: a.why for a in found.against}
        self.assertIn("8.3.23", against)
        self.assertIn("मकारस्य मकारवचनमनुस्वारनिवृत्त्यर्थम्", against["8.3.23"])

    def test_rājīti_kim_saṃyat(self):
        """Kāśikā on 8.3.25: राजीति किम्? संयत् — the following word is not राज्."""
        r = mine("sam|yat")
        self.assertNotIn("8.3.25", steps(r))
        self.assertEqual(ours(r, 1), ["8.3.23", "8.4.59*"])

    def test_sama_iti_kim_kiṃrāṭ(self):
        """Kāśikā on 8.3.25: सम इति किम्? किंराट् — the म् is not सम्'s."""
        r = mine(f"kim {RAJ}")
        self.assertEqual(ours(r), ["8.3.23"])
        self.assertIn(ANUSVARA, r.surface)

    def test_kvāviti_kim_saṃrājitā(self):
        """Kāśikā on 8.3.25: क्वाविति किम्? संराजिता — no क्विप्, so the
        anusvāra stays (and 8.4.58 does not turn it into anything: र् has no
        nasal savarṇa — Tattvabodhinī on 8.4.58)."""
        r = mine("sam|rājitā{dhatu:rāj}")
        self.assertEqual(ours(r), ["8.3.23"])
        self.assertEqual(r.surfaces, ("saṃrājitā",))

    def test_without_the_flags_the_rule_cannot_know_and_does_not_guess(self):
        """राज् with क्विप् is not in the letters; with neither flag the
        anusvāra of 8.3.23 comes."""
        self.assertEqual(ours(mine("sam|rāj")), ["8.3.23"])
        self.assertEqual(ours(mine("sam|rāj{kvip}")), ["8.3.23"])
        self.assertEqual(ours(mine("sam|rāj{dhatu:rāj}")), ["8.3.23"])

    def test_kiṃ_hmalayati_8_3_26(self):
        """Kāśikā, Kaumudī, Laghukaumudī on 8.3.26: किम् ह्मलयति, किं ह्मलयति;
        Kāśikā: कथम् ह्मलयति, कथं ह्मलयति. Both forms; the म् kept when the
        option is taken, the anusvāra of 8.3.23 when it is declined."""
        for word in ("kim", "katham"):
            r = mine(f"{word} hmalayati")
            self.assertEqual(r.surfaces, (f"{word}hmalayati",
                                          word[:-1] + f"ṃhmalayati"), word)
            self.assertEqual(ours(r, 0), ["8.3.26"])
            self.assertEqual(ours(r, 1), ["8.3.26*", "8.3.23"])

    def test_the_refusal_is_optional_and_says_so(self):
        r = mine("kim hmalayati")
        self.assertEqual(r.outcomes[0].choices, (("8.3.26", True),))
        self.assertEqual(r.outcomes[1].choices, (("8.3.26", False),))
        found = step(r, "8.3.26")
        self.assertEqual(found.option, N.VA)
        self.assertEqual(found.detail.kind, PRATISEDHA)
        self.assertIn("8.3.23", [a.sutra for a in found.against])

    def test_only_a_ha_with_a_ma_after_it_holds_the_anusvara_back(self):
        """The condition is मपरे: with any other sound after the ह्, 8.3.23's
        anusvāra is not optional but compulsory."""
        r = mine("kim hasati")
        self.assertEqual(r.surfaces, ("kiṃhasati",))
        self.assertEqual(ours(r), ["8.3.23"])

    def test_yavalapare_yavala_va_the_vartika_of_8_3_26(self):
        """Kāśikā and Laghukaumudī on 8.3.26 (यवलपरे यवला वा): किय् ह्यः, किं ह्यः;
        किव् ह्वलयति, किं ह्वलयति; किल् ह्लादयति, किं ह्लादयति — one to one, and
        in the nasal form (the Laghukaumudī prints the candrabindu)."""
        for word, nasal in (("hyaḥ", NY), ("hvalayati", NV),
                            ("hlādayati", NL)):
            r = mine(f"kim {word}")
            self.assertEqual(r.surfaces[0], f"ki{nasal}{word}", word)
            self.assertEqual(r.surfaces[1], f"kiṃ{word}", word)
            self.assertEqual(ours(r, 0), ["8.3.26v"], word)
            self.assertEqual(ours(r, 1), ["8.3.26v*", "8.3.23"], word)

    def test_the_vartika_is_labelled_and_is_the_corpus_s_own(self):
        r = mine("kim hyaḥ")
        found = step(r, "8.3.26")
        self.assertEqual(found.detail.authority, VARTTIKA)
        self.assertEqual(found.detail.varttika,
                         "यवलपरे यवला वेति वक्तव्यम् ।")
        self.assertIn("[vārttika]", r.trace())
        self.assertEqual(found.detail.kind, ADESA)
        self.assertEqual(found.detail.adesa, NY)

    def test_the_sutra_and_the_vartika_do_not_both_fire_at_one_place(self):
        """ह्मलयति has a म् after the ह् (the sūtra); ह्यः has a य् (the
        vārttika). Never both."""
        for text, expected in (("kim hmalayati", False), ("kim hyaḥ", True)):
            found = step(mine(text), "8.3.26")
            self.assertEqual(found.detail.authority == VARTTIKA, expected)

    def test_kin_hnute_8_3_27(self):
        """Kāśikā, Kaumudī, Laghukaumudī on 8.3.27: किन् ह्नुते, किं ह्नुते;
        कथन् ह्नुते, कथं ह्नुते — the म् becomes the न् the sūtra names."""
        for word in ("kim", "katham"):
            r = mine(f"{word} hnute")
            self.assertEqual(r.surfaces, (word[:-1] + "nhnute",
                                          word[:-1] + "ṃhnute"), word)
            found = step(r, "8.3.27")
            self.assertEqual((found.detail.sthanin, found.detail.adesa),
                             ("m", "n"))
            self.assertEqual(ours(r, 1), ["8.3.27*", "8.3.23"])

    def test_8_3_27_does_not_take_a_ha_with_a_ma_and_8_3_26_not_a_na(self):
        self.assertNotIn("8.3.27", steps(mine("kim hmalayati")))
        self.assertNotIn("8.3.26", steps(mine("kim hnute")))

    def test_both_options_displace_8_3_23_and_say_why_in_the_tradition_s_words(self):
        for text, sutra, quote in (
                ("kim hmalayati", "8.3.26",
                 "हकारे मकारपरे परतो मकारस्य वा मकार आदेशो भवति"),
                ("kim hnute", "8.3.27",
                 "नकारपरे हे परतो मकारस्य वा नकारादेशो भवति")):
            found = step(mine(text), sutra)
            why = {a.sutra: a.why for a in found.against}["8.3.23"]
            self.assertIn(quote, why, sutra)

    def test_kimvuktam_8_3_33_and_the_vatva_is_asiddha_to_8_3_23(self):
        """Kaumudī on 8.3.33: किमु उक्तम् (किम्वुक्तम्); वत्वस्यासिद्धत्वान्नानुस्वारः —
        the व् 8.3.33 makes is asiddha to 8.3.23, which still sees the उ, so no
        anusvāra. (Derived under whichever family holds 8.3.33 — this one, or
        the prakṛtibhāva family, which needs it as the exception to 6.1.125 —
        and the vowel rules of the ac families left out, so that the pragṛhya उ
        is not the question.)"""
        r = maya("kim u{nipata} uktam")
        self.assertEqual(r.outcomes[0].text(), "kim v uktam")
        self.assertEqual(steps(r, 0), ["8.3.33"])
        self.assertNotIn("8.3.23", steps(r))
        self.assertEqual(r.surfaces[0], "kimvuktam")
        # the view 8.3.23 has of the result: the उ, not the व्
        view = View(r.outcomes[0].final, "8.3.23")
        self.assertEqual("".join(s.s for s in view.live), "kimuuktam")
        later = View(r.outcomes[0].final, "8.4.58")
        self.assertEqual("".join(s.s for s in later.live), "kimvuktam")

    def test_kimu_uktam_the_other_course_has_no_anusvara_either(self):
        r = maya("kim u{nipata} uktam")
        self.assertEqual(r.surfaces, ("kimvuktam", "kimuuktam"))
        self.assertEqual(steps(r, 1)[0], "8.3.33*")
        self.assertNotIn("8.3.23", steps(r, 1))

    def test_tadvasya_and_shamvastu_8_3_33(self):
        """Kāśikā on 8.3.33: शम्वस्तु वेदिः (शमु अस्तु), तद्वस्य परेतः (तदु अस्य),
        किम्वावपनम् (किमु आवपनम्) — after a मय्, before an अच्."""
        for text, expected in (("śam u{nipata} astu", "śamvastu"),
                               ("tad u{nipata} asya", "tadvasya"),
                               ("kim u{nipata} āvapanam", "kimvāvapanam")):
            r = maya(text)
            self.assertEqual(r.surfaces[0], expected, text)
            self.assertEqual(steps(r, 0), ["8.3.33"], text)

    def test_the_uñ_must_be_the_particle_and_an_ac_must_follow(self):
        """The उञ् is a particle the letters cannot name: without `{nipata}`
        the उ is left; before a consonant the rule has no अच् to see."""
        self.assertNotIn("8.3.33", steps(maya("kim u uktam")))
        self.assertNotIn("8.3.33", steps(maya("kim u{nipata} tatra")))

    def test_a_maya_must_stand_before_the_uñ(self):
        """मयः परस्य: after a vowel the rule does not apply (कथा उ उक्तम्)."""
        self.assertNotIn("8.3.33", steps(maya("kathā u{nipata} uktam")))

    def test_8_3_33_has_one_home_in_the_whole_rulebook(self):
        """`rulebook.problems()` refuses two families defining a sūtra: where the
        prakṛtibhāva family has 8.3.33 this family stands aside, and says so."""
        homes = [name for name, group in rulebook.by_family().items()
                 if any(r.sutra == "8.3.33" and not r.varttika for r in group)]
        self.assertEqual(len(homes), 1, homes)
        status = {s: st for s, st, _ in N.COVERAGE}["8.3.33"]
        self.assertEqual(status, "scope" if N._MAYA_ELSEWHERE else "rule")
        self.assertEqual(homes[0],
                         N._MAYA_ELSEWHERE or FAMILY)


# ---------------------------------------------------------------------------
# 8.4.58 and 8.4.59 — parasavarṇa
# ---------------------------------------------------------------------------


class Parasavarna(unittest.TestCase):

    def test_tvaṅkaroṣi_and_tvaṃ_karoṣi_8_4_59(self):
        """Laghusiddhāntakaumudī on 8.4.59: त्वङ्करोषि, त्वं करोषि — the option
        of the pada-final anusvāra before a यय्."""
        r = mine("tvam karoṣi")
        self.assertEqual(r.surfaces, ("tvaṅkaroṣi", "tvaṃkaroṣi"))
        self.assertEqual(ours(r, 0), ["8.3.23", "8.4.59"])
        self.assertEqual(ours(r, 1), ["8.3.23", "8.4.59*"])
        self.assertEqual(r.outcomes[0].choices[-1], ("8.4.59", True))
        self.assertEqual(r.outcomes[1].choices[-1], ("8.4.59", False))

    def test_the_anusvara_is_the_padas_own_whether_8_3_23_made_it_or_the_caller_wrote_it(self):
        """Kāśikā on 8.4.59: तङ् कथञ् … / तं कथं …"""
        for text in ("tam kathaṃ", "taṃ kathaṃ"):
            r = mine(text)
            self.assertEqual(r.surfaces, ("taṅkathaṃ", "taṃkathaṃ"), text)

    def test_the_kasika_s_whole_sentence_gives_every_combination(self):
        """तं कथं चित्रपक्षं … : each pada-final anusvāra has its own option, so
        two of them give four forms."""
        r = mine("tam kathaṃ citrapakṣam")
        self.assertEqual(len(r.outcomes), 4)
        self.assertIn("taṅkathañcitrapakṣam", r.surfaces)
        self.assertIn("taṃkathaṃcitrapakṣam", r.surfaces)

    def test_the_nasal_forms_of_ya_va_la_8_4_59(self):
        """Kaumudī on 8.4.59: सय्ँयन्ता, संयन्ता; सव्ँवत्सरः, संवत्सरः; यल्ँलोकम्,
        यंलोकम् — अत्रानुस्वारस्य पक्षेऽनुनासिका यवलाः."""
        for text, nasal, plain in (
                ("sam yantā", "say" + ANUNASIKA_MARK + "yantā", "saṃyantā"),
                ("sam vatsaraḥ", "sav" + ANUNASIKA_MARK + "vatsaraḥ",
                 "saṃvatsaraḥ"),
                ("yam lokam", "yal" + ANUNASIKA_MARK + "lokam", "yaṃlokam")):
            r = mine(text)
            self.assertEqual(r.surfaces, (nasal, plain), text)

    def test_the_nasal_is_the_savarna_nearest_the_anusvara(self):
        """Every yay sound: a stop takes the fifth of its varga, ya, va and la
        their nasal forms, and र् takes nothing (Tattvabodhinī on 8.4.58: the
        substitute must be nearest the anusvāra, which is a nose-sound)."""
        for varga, members in VARGA.items():
            for sound in members:
                self.assertEqual(N._parasavarna(sound), members[4], sound)
        for sound in ("y", "v", "l"):
            self.assertEqual(N._parasavarna(sound), sound + ANUNASIKA_MARK)
        self.assertIsNone(N._parasavarna("r"))
        for sound in ("ś", "ṣ", "s", "h"):
            self.assertIsNone(N._parasavarna(sound), sound)

    def test_the_result_was_not_typed_it_is_the_1_1_50_choice(self):
        """A test that a table would fail: the substitute changes with the
        following sound's varga and with nothing else."""
        seen = {}
        for sound in ("k", "c", "ṭ", "t", "p"):
            seen[sound] = N._parasavarna(sound)
        self.assertEqual(len(set(seen.values())), 5)

    def test_yayīti_kim_ākraṃsyate(self):
        """Kāśikā on 8.4.58: ययीति किम्? आक्रंस्यते, आचिक्रंसते — a स् is not a
        यय्, so the anusvāra 8.3.24 made stays."""
        r = mine("ākram~syate")
        self.assertEqual(ours(r), ["8.3.24"])
        self.assertEqual(r.surfaces, ("ākraṃsyate",))

    def test_a_sibilant_after_an_anusvara_takes_no_parasavarna(self):
        """Tattvabodhinī on 8.4.58: शलि तु परसवर्णोऽनुस्वारान्तरतमो न संभवतीति —
        कुण्डं शेते keeps its anusvāra, and 8.4.59 does not offer the option."""
        r = mine("kuṇḍaṃ śete")
        self.assertEqual(ours(r), [])
        self.assertEqual(len(r.outcomes), 1)
        self.assertEqual(ours(mine("kuṇḍam śete")), ["8.3.23"])

    def test_no_anusvara_becomes_a_ra(self):
        """संरक्षति: र् is a यय् but has no nasal savarṇa."""
        r = mine("saṃ rakṣati")
        self.assertEqual(ours(r), [])
        self.assertEqual(r.surfaces, ("saṃrakṣati",))

    def test_saṅkitā_kuṇḍitā_nanditā_kampitā_8_4_58(self):
        """Kāśikā on 8.4.58: शङ्किता, उञ्छिता, कुण्डिता, नन्दिता, कम्पिता (and
        Kaumudī: अङ्कितः, अञ्चितः, कुण्ठितः, शान्तः, गुम्फितः). The न् or म् is
        an anusvāra by 8.3.24 and then the savarṇa of the following stop."""
        for text, expected in (
                ("śan~kitā", "śaṅkitā"), ("un~chitā", "uñchitā"),
                ("kun~ḍitā", "kuṇḍitā"),
                ("nan~ditā", "nanditā"), ("kam~pitā", "kampitā"),
                ("an~kitaḥ", "aṅkitaḥ"), ("an~citaḥ", "añcitaḥ"),
                ("kun~ṭhitaḥ", "kuṇṭhitaḥ"), ("śām~taḥ", "śāntaḥ"),
                ("gum~phitaḥ", "gumphitaḥ")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(ours(r), ["8.3.24", "8.4.58"], text)

    def test_the_savarna_is_of_the_following_sound_and_named_as_such(self):
        found = step(mine("śan~kitā"), "8.4.58")
        self.assertEqual(found.detail.adesa, "ṅ")
        self.assertEqual(found.before, "śaṃ kitā")
        self.assertEqual(found.after, "śaṅ kitā")
        self.assertIn("1.1.9", found.sutras)
        self.assertIn("1.1.50", found.sutras)

    def test_kurvanti_the_nasal_is_not_natva_s_and_not_8_3_24_s_again(self):
        """Kāśikā and Kaumudī on 8.4.58: कुर्वन्ति, कृषन्ति — ṇatva is asiddha, so
        the न् becomes an anusvāra first, and the parasavarṇa gives a न् again
        that 8.4.2 (ṇatva) and 8.3.24 do not see. Shown by what each rule sees."""
        for text, expected in (("kurvan~ti", "kurvanti"),
                               ("kṛṣan~ti", "kṛṣanti")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(ours(r), ["8.3.24", "8.4.58"], text)
            final = r.outcomes[0].final
            self.assertEqual(final.joined()[-3:], "nti")
            for viewer in ("8.4.2", "8.3.24"):
                seen = "".join(s.s for s in View(final, viewer).live)
                self.assertIn("ṃ", seen, viewer)
                self.assertNotIn("nt", seen, viewer)
            # 8.4.58 itself sees what it made
            self.assertIn("nt", "".join(s.s for s in View(final, "8.4.58").live))

    def test_a_pada_final_anusvara_is_8_4_59_s_and_not_8_4_58_s(self):
        """The Kāśikā's examples of 8.4.58 are all inside a word, and 8.4.59
        makes the pada-final anusvāra optional; so the nitya rule is for the
        anusvāra that does not end a pada."""
        r = mine("tam kathaṃ")
        self.assertNotIn("8.4.58", steps(r))
        self.assertIn("8.4.59", steps(r))
        self.assertNotIn("8.4.59", steps(mine("śan~kitā")))

    def test_saṃnyāsa_8_4_59(self):
        """A preverb ends a pada (सम्-न्यासः): both forms."""
        self.assertEqual(surfaces("sam|nyāsaḥ"), {"sannyāsaḥ", "saṃnyāsaḥ"})


# ---------------------------------------------------------------------------
# 8.4.45 यरोऽनुनासिकेऽनुनासिको वा
# ---------------------------------------------------------------------------


class NasalBeforeNasal(unittest.TestCase):

    def test_vāṅ_nayati_and_the_kasika_s_others_8_4_45(self):
        """Kāśikā on 8.4.45: वाङ् नयति, वाग् नयति; श्वलिण् नयति, श्वलिड् नयति;
        अग्निचिन् नयति, अग्निचिद् नयति; त्रिष्टुम् नयति, त्रिष्टुब् नयति. A
        pada-final stop before a nasal takes the nasal of its varga, or not."""
        for text, nasal, plain in (
                ("vāg nayati", "vāṅnayati", "vāgnayati"),
                ("śvaliḍ nayati", "śvaliṇnayati", "śvaliḍnayati"),
                ("agnicid nayati", "agnicinnayati", "agnicidnayati"),
                ("triṣṭub nayati", "triṣṭumnayati", "triṣṭubnayati")):
            r = mine(text)
            self.assertEqual(r.surfaces, (nasal, plain), text)
            self.assertEqual(ours(r, 0), ["8.4.45"])
            self.assertEqual(ours(r, 1), ["8.4.45*"])

    def test_etanmurāriḥ_8_4_45(self):
        """Kaumudī and Laghusiddhāntakaumudī on 8.4.45: एतन्मुरारिः, एतद् मुरारिः."""
        r = mine("etad murāriḥ")
        self.assertEqual(r.surfaces, ("etanmurāriḥ", "etadmurāriḥ"))
        found = step(r, "8.4.45")
        self.assertEqual((found.detail.sthanin, found.detail.adesa), ("d", "n"))
        self.assertEqual(found.option, N.VA)

    def test_the_step_names_1_1_50_and_the_yar(self):
        found = step(mine("vāg nayati"), "8.4.45")
        self.assertIn("1.1.50", found.sutras)
        self.assertIn("1.1.71", found.sutras)
        self.assertEqual(found.after, "vāṅ nayati")

    def test_padantasyeti_eva_vedmi_kṣubhnāti(self):
        """Kāśikā on 8.4.45: पदान्तस्येत्येव — वेद्मि, क्षुभ्नाति (inside a pada)."""
        for text in ("ved~mi", "kṣubh~nāti"):
            self.assertEqual(ours(mine(text)), [], text)

    def test_caturmukhaḥ_repha_takes_no_nasal(self):
        """Kaumudī on 8.4.45: स्थानप्रयत्नाभ्यामन्तरतमे स्पर्शे चरितार्थो विधिरयं रेफे
        न प्रवर्तते — चतुर्मुखः. The nasal of र्'s place has another effort."""
        r = mine("catur-mukhaḥ")
        self.assertEqual(ours(r), [])
        self.assertEqual(r.surface, "caturmukhaḥ")

    def test_the_sibilants_take_no_nasal_either(self):
        """श्, ष्, स् are yar: the nasal of their place has another effort."""
        for sound in ("ś", "ṣ", "s"):
            self.assertIsNone(N._nasal_of(sound), sound)
        self.assertEqual(ours(alone("viś nayati")), [])

    def test_every_stop_takes_the_fifth_of_its_varga_and_a_semivowel_its_nasal(self):
        """Not a table: 1.1.50 among the nasal sounds, by place and effort."""
        for members in VARGA.values():
            for sound in members:
                if sound != members[4]:
                    self.assertEqual(N._nasal_of(sound), members[4], sound)
        for sound in ("y", "v", "l"):
            self.assertEqual(N._nasal_of(sound), sound + ANUNASIKA_MARK)
        self.assertIsNone(N._nasal_of("r"))

    def test_a_nasal_before_a_nasal_is_no_step(self):
        """A न् put where a न् stands changes nothing and is not a step."""
        self.assertEqual(ours(alone("tan mātram")), [])
        self.assertNotIn("8.4.45", steps(alone("tam nayati")))
        self.assertNotIn("8.4.45", steps(alone("vāṅ nayati")))

    def test_only_a_nasal_sound_follows(self):
        """अनुनासिके: before a non-nasal the stop is left (वाग् गच्छति) — and the
        anusvāra is not anunāsika (Bhāṣya on 1.1.8)."""
        self.assertEqual(ours(alone("vāg gacchati")), [])
        self.assertFalse(is_anunasika(ANUSVARA))

    def test_tanmātram_and_cinmayam_the_vartika_makes_it_nitya(self):
        """Kaumudī and Laghukaumudī on 8.4.45 (प्रत्यये भाषायां नित्यम्): तन्मात्रम्,
        चिन्मयम्; Kāśikā: वाङ्मयम्, त्वङ्मयम्. Before an affix the option is not
        one. The stem is a pada by 1.4.17 and the caller gives it as one."""
        for text, expected, before in (
                ("tad-mātra{pratyaya}", "tanmātra", []),
                ("cit maya{pratyaya}", "cinmaya", ["8.2.39"]),
                ("vāc-maya{pratyaya}", "vāṅmaya", ["8.2.30", "8.2.39"]),
                ("tvac-maya{pratyaya}", "tvaṅmaya", ["8.2.30", "8.2.39"])):
            r = mine(text, "hal_assimilation")
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(len(r.outcomes), 1, text)
            order = [s for s in steps(r) if s in before + ["8.4.45v"]]
            self.assertEqual(order, before + ["8.4.45v"], text)

    def test_the_vartika_is_labelled_and_the_corpus_s_own(self):
        r = mine("tad-mātra{pratyaya}")
        found = step(r, "8.4.45")
        self.assertEqual(found.detail.authority, VARTTIKA)
        self.assertEqual(found.detail.varttika, "प्रत्यये भाषायां नित्यम् ।")
        self.assertEqual(found.option, "")
        self.assertIn("[vārttika]", r.trace())

    def test_the_option_stays_where_there_is_no_affix(self):
        """वाङ् मयम्: with no `pratyaya` (two words) the sūtra's own option."""
        r = mine("vāg maya")
        self.assertEqual(len(r.outcomes), 2)
        self.assertEqual(step(r, "8.4.45").detail.authority, "sūtra")

    def test_bhāṣāyām_the_vartika_is_not_for_the_veda(self):
        """भाषायाम्: in the Veda 8.4.45's own option stands."""
        r = mine("tad-mātra{pratyaya}", veda=True)
        self.assertEqual(len(r.outcomes), 2)

    def test_a_stem_written_with_a_tilde_is_not_a_pada_here(self):
        """`cit~maya` says the stem is not a pada, and the rule does not say
        otherwise — 1.4.17 is the caller's to state."""
        self.assertEqual(ours(mine("cit~maya{pratyaya}")), [])


# ---------------------------------------------------------------------------
# 8.3.28–8.3.32 — the augments
# ---------------------------------------------------------------------------


class Augments(unittest.TestCase):

    def test_the_two_lists_of_8_3_28_are_read_off_the_sutra_and_go_in_order(self):
        """1.3.10: ङ्, ण् and कुक्, टुक् — equal in number, so first with
        first. Both lists are read from the sūtra's own text."""
        self.assertEqual(N._kuk_tuk(), (("ṅ", "kuk"), ("ṇ", "ṭuk")))

    def test_the_place_of_each_augment_is_1_1_46_s_from_its_it(self):
        """कुक्, टुक्, तुक् are कित् (at the end); धुट्, ङुट्, णुट्, नुट् टित् (at the
        start) — Bālamanoramā on 8.3.28, 8.3.29, 8.3.32: ककार इत्, टकार इत्;
        उकार उच्चारणार्थः."""
        for name, sound, it, where in (
                ("kuk", "k", "k", AgamaSite.ANTA),
                ("ṭuk", "ṭ", "k", AgamaSite.ANTA),
                ("tuk", "t", "k", AgamaSite.ANTA),
                ("dhuṭ", "dh", "ṭ", AgamaSite.ADI),
                ("ṅuṭ", "ṅ", "ṭ", AgamaSite.ADI),
                ("ṇuṭ", "ṇ", "ṭ", AgamaSite.ADI),
                ("nuṭ", "n", "ṭ", AgamaSite.ADI)):
            self.assertEqual(N._agama(name), (sound, it), name)
            self.assertEqual(N._agama_site(it), where, name)

    def test_prāṅk_śete_8_3_28(self):
        """Kāśikā on 8.3.28: प्राङ्क् शेते, प्राङ् शेते; प्राङ्क् षष्ठः; प्राङ्क्साये.
        The कुक् is a कित्, so it stands at the END of the ङ्, in the first pada."""
        r = mine("prāṅ śete")
        self.assertEqual(r.surfaces, ("prāṅkśete", "prāṅśete"))
        self.assertEqual(ours(r, 0), ["8.3.28"])
        self.assertEqual(ours(r, 1), ["8.3.28*"])
        found = step(r, "8.3.28")
        self.assertEqual(found.after, "prāṅk śete")
        self.assertEqual(found.detail.kind, AGAMA_KIND)
        (aug,) = made_by(r, "8.3.28")
        self.assertEqual((aug.s, aug.w), ("k", 0))
        self.assertTrue(aug.has(AGAMA))

    def test_prāṅk_ṣaṣṭhaḥ_and_prāṅk_sāye(self):
        """Kāśikā and Laghusiddhāntakaumudī on 8.3.28: प्राङ्क्षष्ठः, प्राङ् षष्ठः;
        प्राङ्क्साये, प्राङ् साये (the प्राङ्ख् form of the Laghukaumudī needs
        Pauṣkarasādi's vārttika, not derived here)."""
        for text, aug, plain in (("prāṅ ṣaṣṭhaḥ", "prāṅkṣaṣṭhaḥ", "prāṅṣaṣṭhaḥ"),
                                 ("prāṅ sāye", "prāṅksāye", "prāṅsāye")):
            self.assertEqual(mine(text).surfaces, (aug, plain), text)

    def test_the_kuk_is_for_the_nga_and_the_tuk_for_the_nna_one_to_one(self):
        """Kāśikā on 8.3.28: ण् takes टुक् — वण्ट् शेते, वण् शेते — and Laghukaumudī:
        सुगण्ट् षष्ठः, सुगण् षष्ठः."""
        r = mine("vaṇ śete")
        self.assertEqual(r.surfaces, ("vaṇṭśete", "vaṇśete"))
        self.assertEqual(made_by(r, "8.3.28")[0].s, "ṭ")
        r = mine("sugaṇ ṣaṣṭhaḥ")
        self.assertEqual(r.surfaces, ("sugaṇṭṣaṣṭhaḥ", "sugaṇṣaṣṭhaḥ"))

    def test_the_augment_needs_a_sar_after_it(self):
        """शरि: before a क् (प्राङ् करोति) no augment."""
        self.assertEqual(ours(mine("prāṅ karoti")), [])

    def test_the_augment_is_asiddha_to_8_2_39_no_jasatva(self):
        """Kaumudī on 8.3.28: कुक्टुकोरसिद्धत्वाज्जश्त्वं न. The कुक् is put in by a
        later rule, so 8.2.39 does not see it — shown by what it sees, and by
        the augment still being a क् when 8.2.39 has been through the form."""
        r = mine("prāṅ śete", "hal_assimilation")
        final = r.outcomes[0].final
        (aug,) = made_by(r, "8.3.28")
        self.assertEqual(aug.s, "k")
        seen = "".join(s.s for s in View(final, "8.2.39").live)
        self.assertNotIn("ṅk", seen)
        after = "".join(s.s for s in View(final, "8.4.55").live)
        self.assertIn("ṅk", after)

    def test_ṣaṭ_santaḥ_8_3_29(self):
        """Laghusiddhāntakaumudī and Kaumudī on 8.3.29: षट्त्सन्तः, षट् सन्तः. The
        ष् is a ड् by 8.2.39 first; then the धुट् — a टित्, at the START of the
        स्, in the second pada. (The धुट्'s own चर्त्व, धकार to त्, is the हल्
        family's, and asiddha to this rule.)"""
        r = mine("ṣaṣ santaḥ", "hal_assimilation")
        order = [s for s in steps(r) if s in ("8.2.39", "8.3.29", "8.3.29*")]
        self.assertEqual(order, ["8.2.39", "8.3.29"])
        found = step(r, "8.3.29")
        self.assertEqual(head(found.before), "ṣaḍ santas")
        self.assertEqual(head(found.after), "ṣaḍ dhsantas")
        # the other course has no augment at all
        self.assertEqual(ours(r, 1), ["8.3.29*"])
        # the augment stands at the start of the second pada
        (aug,) = made_by(mine("ṣaḍ santaḥ"), "8.3.29")
        self.assertEqual((aug.s, aug.w), ("dh", 1))
        self.assertTrue(aug.has(AGAMA))

    def test_śvaliṭ_sāye_and_madhuliṭ_sāye_8_3_29(self):
        """Kāśikā on 8.3.29: श्वलिट्त्साये, श्वलिट् साये; मधुलिट्त्साये, मधुलिट् साये."""
        for text in ("śvaliḍ sāye", "madhuliḍ sāye"):
            r = mine(text)
            self.assertEqual(ours(r, 0), ["8.3.29"], text)
            self.assertEqual(head(step(r, "8.3.29").after),
                             head(text.replace(" ", " dh", 1)).replace("ḥ", "s"),
                             text)

    def test_the_dhut_needs_a_da_before_and_an_sa_after(self):
        """डात्परस्य सस्य: not after another sound, not before another."""
        self.assertEqual(ours(mine("ṣaḍ ca")), [])
        self.assertEqual(ours(mine("ṣaṭ santaḥ")), [])

    def test_bhavān_sāye_and_santsaḥ_8_3_30(self):
        """Kāśikā on 8.3.30: भवान्त्साये, भवान् साये; महान्त्साये, महान् साये;
        Kaumudī: सन्त्सः, सन्सः."""
        for text in ("bhavān sāye", "mahān sāye", "san saḥ"):
            r = mine(text)
            self.assertEqual(ours(r, 0), ["8.3.30"], text)
            self.assertEqual(ours(r, 1), ["8.3.30*"], text)
            self.assertEqual(head(step(r, "8.3.30").after),
                             head(text.replace(" ", " dh", 1)).replace("ḥ", "s"),
                             text)

    def test_the_dhut_and_the_kuk_are_invisible_to_the_rules_before_them(self):
        """Kāśikā on 8.3.30: धुटश्चर्त्वस्य चासिद्धत्वात् … रुत्वं न भवति. An
        augment has no past, so a rule that stands before it sees the form
        without it, and a rule after it sees it."""
        r = mine("bhavān sāye")
        final = r.outcomes[0].final
        for viewer, expected in (("8.3.7", "bhavānsāye"),
                                 ("8.3.29", "bhavānsāye"),
                                 ("8.3.30", "bhavāndhsāye"),
                                 ("8.4.55", "bhavāndhsāye")):
            seen = "".join(s.s for s in View(final, viewer).live)
            self.assertEqual(seen, expected, viewer)
        self.assertNotIn("8.3.7", steps(r))

    def test_8_3_7_does_apply_where_the_chav_is_really_there(self):
        """The control of the test above: भवान् छादयति has a छव् after the न्."""
        self.assertEqual(ours(mine("bhavān chādayati"))[0], "8.3.7")

    def test_sañchambhuḥ_8_3_31(self):
        """Laghusiddhāntakaumudī on 8.3.31: सञ्छम्भुः, सञ्च्छम्भुः, सञ्च्शम्भुः,
        सञ्शम्भुः. This family gives the तुक्, at the END of the न् — पूर्वान्तकरणं
        छत्वार्थम् (Kāśikā) — and the four forms need 8.4.40, 8.4.63 and 8.4.65
        (the हल् family); here the forms it can reach without the last two."""
        r = mine("san śambhuḥ")
        self.assertEqual(r.surfaces, ("santśambhuḥ", "sanśambhuḥ"))
        found = step(r, "8.3.31")
        self.assertEqual(head(found.after), "sant śambhus")
        (aug,) = made_by(r, "8.3.31")
        self.assertEqual((aug.s, aug.w), ("t", 0))
        forms = surfaces("san śambhuḥ", "hal_assimilation")
        self.assertLessEqual({"sañcśambhuḥ", "sañśambhuḥ"}, forms)

    def test_bhavāñ_chete_8_3_31(self):
        """Kāśikā on 8.3.31: भवाञ्च्छेते — the तुक् after a pada-final न्."""
        r = mine("bhavān śete")
        self.assertEqual(step(r, "8.3.31").after, "bhavānt śete")
        self.assertEqual(ours(r, 1), ["8.3.31*"])

    def test_the_tuk_needs_a_sa_and_a_final_na(self):
        self.assertEqual(ours(mine("bhavān kaḥ")), [])
        self.assertEqual(ours(mine("bhavāt śete")), [])

    def test_pratyaṅṅātmā_8_3_32(self):
        """Laghusiddhāntakaumudī on 8.3.32: प्रत्यङ्ङात्मा, सुगण्णीशः, सन्नच्युतः;
        Kāśikā: कुर्वन्नास्ते, कृषन्नास्ते, वण्णास्ते, कुर्वन्नवोचत्. The augment is a
        टित्: at the START of the vowel, in the second pada — and it is
        compulsory."""
        for text, expected, aug in (
                ("pratyaṅ ātmā", "pratyaṅṅātmā", "ṅ"),
                ("sugaṇ īśaḥ", "sugaṇṇīśaḥ", "ṇ"),
                ("san acyutaḥ", "sannacyutaḥ", "n"),
                ("kurvan āste", "kurvannāste", "n"),
                ("kṛṣan āste", "kṛṣannāste", "n"),
                ("vaṇ āste", "vaṇṇāste", "ṇ"),
                ("kurvan avocat", "kurvannavocat", "n")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(len(r.outcomes), 1, text)
            self.assertEqual(ours(r), ["8.3.32"], text)
            (made,) = made_by(r, "8.3.32")
            self.assertEqual((made.s, made.w), (aug, 1), text)

    def test_ṅama_iti_kim_tvamāsse(self):
        """Kāśikā on 8.3.32: ङम इति किम्? त्वमास्से."""
        self.assertEqual(ours(mine("tvam āsse")), [])

    def test_hrasvāditi_kim_prāṅāste_bhavānāste(self):
        """Kāśikā on 8.3.32: ह्रस्वादिति किम्? प्राङास्ते, भवानास्ते — a long vowel
        before the ङम्."""
        for text in ("prāṅ āste", "bhavān āste"):
            self.assertEqual(ours(mine(text)), [], text)

    def test_aciti_kim_pratyaṅ_karoti(self):
        """Kāśikā on 8.3.32: अचीति किम्? प्रत्यङ् करोति."""
        self.assertEqual(ours(mine("pratyaṅ karoti")), [])

    def test_paramadaṇḍinau_has_no_augment(self):
        """Kāśikā on 8.3.32: परमदण्डिनौ — the न् does not end a pada
        (उत्तरपदत्वे चापदादिविधौ प्रत्ययलक्षणप्रतिषेधात्); written as two pieces of
        one pada."""
        self.assertEqual(ours(mine("paramadaṇḍin~au")), [])

    def test_the_nasal_augment_is_the_nasal_it_follows_and_a_vowel_is_needed(self):
        """ङमुट् is ङुट्, णुट्, नुट् one to one (1.3.10): the augment repeats
        the न् (ङ्, ण्) it follows, and only a vowel takes it."""
        for sthanin in ("ṅ", "ṇ", "n"):
            r = mine(f"ka{sthanin} āste")
            self.assertEqual(made_by(r, "8.3.32")[0].s, sthanin)
        self.assertNotIn("8.3.32", steps(mine("kan tatra")))


# ---------------------------------------------------------------------------
# 8.3.1–8.3.7 — the रु of the nasal words and the nasal before it
# ---------------------------------------------------------------------------


def with_ru(text, by="8.3.9", **kw):
    """`text` parsed, with the last sound of its first word replaced by a रु
    that the sūtra `by` made — for the sūtras of 8.3.2's heading that no
    rule of this family makes (8.3.9 is Vedic and not in scope)."""
    state = parse(text, **kw)
    last = max(i for i, s in enumerate(state.segs) if s.w == 0)
    old = state.segs[last]
    ru = Seg(uid=state.next_uid, s="r", w=0, marks=frozenset({RU}),
             made_by=by, prior=(old,), show="ru")
    return replace(state, segs=state.segs[:last] + (ru,) + state.segs[last + 1:],
                   next_uid=state.next_uid + 1)


class RuAndTheNasalBefore(unittest.TestCase):

    def test_sam_skartā_the_ru_then_both_courses_8_3_5_8_3_2_8_3_4(self):
        """Kāśikā and Bālamanoramā on 8.3.5, 8.3.2, 8.3.4: सम् + सुट् + कर्ता gives
        सँस्स्कर्ता and संस्स्कर्ता (Laghukaumudī: संस्स्कर्ता). The म् is a रु
        (8.3.5), the sound before it is made anunāsika (8.3.2, an option) or, if
        it is not, an anusvāra follows it (8.3.4); then the vārttika puts स् for
        the रु — here, or, where the visarga family states it on the visarga,
        there. What comes after — the हल् family's work on the स् — is not
        asserted here."""
        r = mine("sam|skartā{sut}")
        self.assertEqual(len(r.outcomes), 2)
        self.assertEqual(ours(r, 0), ["8.3.5", "8.3.2"] + VT)
        self.assertEqual(ours(r, 1), ["8.3.5", "8.3.2*", "8.3.4"] + VT)
        first = r.outcomes[0].steps
        self.assertEqual(first[0].after, "saru skartā")
        self.assertEqual(first[1].after, f"s{NA}ru skartā")
        second = [s for s in r.outcomes[1].steps if s.sutra == "8.3.4"][0]
        self.assertEqual(second.before, "saru skartā")
        self.assertEqual(second.after, "saṃru skartā")

    def test_saṃsskartā_the_classical_forms_as_far_as_the_skeleton_goes(self):
        """Laghusiddhāntakaumudī on 8.3.15/8.3.5: संस्स्कर्ता; Kāśikā: सँस्स्कर्ता.
        Both forms, with the whole rulebook as it stands."""
        self.assertEqual(set(sandhi("sam|skartā{sut}").surfaces),
                         {f"s{NA}sskartā", "saṃsskartā"})

    @unittest.skipIf(SAMPUMKA_ELSEWHERE, "the visarga family states it")
    def test_sampumkanam_so_vaktavyah_the_ru_is_an_s_and_not_a_visarga(self):
        """Kaumudī and Laghukaumudī (संपुंकानां सो वक्तव्यः), Kāśikā on 8.3.5 and
        8.3.6 (सकार एवादेशो वक्तव्यः): the रु of सम् and पुम् before a खर् is a
        स्. The vārttika is labelled as one and carries the corpus's words."""
        for text, sutra in (("sam|skartā{sut}", "8.3.5"),
                            ("pum kokilaḥ", "8.3.6")):
            r = mine(text)
            found = step(r, "8.3.5v")
            self.assertEqual(found.detail.authority, VARTTIKA, text)
            self.assertEqual(found.detail.varttika,
                             "संपुंकानां सो वक्तव्यः, समो वा लोपमेके ।", text)
            self.assertEqual((found.detail.sthanin, found.detail.adesa),
                             ("ru", "s"), text)
            self.assertIn("[vārttika]", r.trace())
            self.assertNotIn("8.3.15", steps(r)[:steps(r).index("8.3.5v")])
            self.assertEqual(found.before.split()[0][-2:], "ru", text)
            self.assertEqual(found.after.split()[0][-1], "s", text)

    @unittest.skipUnless(SAMPUMKA_ELSEWHERE, "this family states it")
    def test_where_the_visarga_family_states_the_vartika_this_family_stands_aside(self):
        """The Laghusiddhāntakaumudī prints saṃpuṃkānāṃ so vaktavyaḥ after
        8.3.15, as a स् for the visarga; where the visarga family states it so,
        the रु goes to the visarga first and the form is the same."""
        for text, expected in (("sam|skartā{sut}", "saṃsskartā"),
                               ("pum kokilaḥ", "puṃskokilaḥ")):
            r = mine(text)
            self.assertIn(expected, r.surfaces, text)
            self.assertIn("8.3.15", steps(r, 1), text)
            self.assertNotIn("8.3.5v", steps(r, 1), text)
            self.assertTrue(
                any(s.detail.authority == VARTTIKA and s.sutra != "8.3.5"
                    for s in r.outcomes[1].steps), text)

    def test_the_vartika_comes_after_the_nasal_and_the_anusvara(self):
        """Its number is the larger, so 8.3.2 and 8.3.4 have had their turn."""
        r = mine("pum kokilaḥ")
        self.assertEqual(ours(r, 0), ["8.3.6", "8.3.2"] + VT)
        self.assertEqual(ours(r, 1), ["8.3.6", "8.3.2*", "8.3.4"] + VT)

    @unittest.skipIf(SAMPUMKA_ELSEWHERE, "the visarga family states it")
    def test_without_the_vartika_the_ru_goes_the_visarga_way(self):
        """The vārttika is what takes the visarga's stage out: without it the
        visarga family's 8.3.15 acts on the रु of पुम्."""
        rules = tuple(r for r in rulebook.rules_of(FAMILY, "visarga_ru")
                      if not (r.sutra == "8.3.5" and r.authority == VARTTIKA))
        r = sandhi("pum kokilaḥ", rules=rules)
        self.assertIn("8.3.15", steps(r))
        self.assertNotIn("8.3.5v", steps(r))

    def test_the_vartika_is_for_sam_pum_kan_and_no_other_ru(self):
        """भवान् (8.3.7) is not named: its रु goes to the visarga and on."""
        r = mine("bhavān chādayati")
        self.assertNotIn("8.3.5v", steps(r))
        self.assertIn("8.3.15", steps(r))

    def test_the_ru_is_a_step_of_8_3_5_replacing_the_last_sound_of_sam(self):
        found = step(mine("sam|skartā{sut}"), "8.3.5")
        self.assertEqual((found.detail.sthanin, found.detail.adesa), ("m", "ru"))
        for sutra in ("1.1.52", "1.3.2", "1.3.9"):
            self.assertIn(sutra, found.sutras)

    def test_sama_iti_kim_upaskartā(self):
        """Kāśikā on 8.3.5: सम इति किम्? उपस्कर्ता — the same augment after उप."""
        self.assertEqual(ours(mine("upa|skartā{sut}")), [])

    def test_suṭīti_kim_saṃkṛtiḥ(self):
        """Kāśikā on 8.3.5: सुटीति किम्? संकृतिः — no augment, so the anusvāra of
        8.3.23 and not a रु."""
        r = mine("sam kṛtiḥ")
        self.assertNotIn("8.3.5", steps(r))
        self.assertEqual(ours(r, 0)[0], "8.3.23")

    def test_the_augment_is_named_by_the_caller_the_letters_cannot_tell(self):
        """स्कर्ता begins with a स् either way; without `{sut}` it is a स् of the
        root and 8.3.5 does not apply."""
        r = mine("sam|skartā")
        self.assertEqual(ours(r), ["8.3.23"])
        self.assertEqual(r.surfaces, ("saṃskartā",))

    def test_the_ru_of_8_3_5_stands_after_8_3_23_and_wins_by_8_2_1(self):
        """Tattvabodhinī on 8.3.5: यद्यपि मोऽनुस्वारेण सिद्धं — the anusvāra would
        have given the form, and 8.3.5 stands before 8.3.23, so it acts first
        and the म् is a रु before it can be an anusvāra."""
        r = mine("sam|skartā{sut}")
        self.assertNotIn("8.3.23", steps(r, 0))
        self.assertNotIn("8.3.23", steps(r, 1))
        self.assertLess(reading_order("8.3.5"), reading_order("8.3.23"))

    def test_puṃskokilaḥ_8_3_6(self):
        """Kaumudī, Laghusiddhāntakaumudī and Kāśikā on 8.3.6: पुँस्कोकिलः,
        पुंस्कोकिलः, पुँस्पुत्रः, पुँस्फलम्, पुँश्चली — the म् of पुम् is a रु before
        a खय् that has an अम् after it. As for 8.3.5, the form where this family
        leaves it is asserted; the rest is the visarga family's."""
        for text, khay in (("pum kokilaḥ", "k"), ("pum putraḥ", "p"),
                           ("pum phalam", "ph"), ("pum calī", "c")):
            r = mine(text)
            self.assertEqual(len(r.outcomes), 2, text)
            self.assertEqual(ours(r, 0), ["8.3.6", "8.3.2"] + VT, text)
            self.assertEqual(ours(r, 1),
                             ["8.3.6", "8.3.2*", "8.3.4"] + VT, text)
            self.assertEqual(step(r, "8.3.6").after.split()[0], "puru", text)
            self.assertEqual(r.outcomes[0].steps[1].after.split()[0],
                             f"p{NU_}ru", text)
            self.assertEqual(step(r, "8.3.4", 1).after.split()[0], "puṃru",
                             text)

    def test_khayīti_kim_puṃdāsaḥ_puṃgavaḥ(self):
        """Kāśikā on 8.3.6: खयीति किम्? पुंदासः, पुंगवः."""
        for text in ("pum dāsaḥ", "pum gavaḥ"):
            r = mine(text)
            self.assertNotIn("8.3.6", steps(r), text)
            self.assertEqual(ours(r, 0)[0], "8.3.23", text)

    def test_amparīti_kim_puṃkṣīram_puṃkṣuram(self):
        """Kāśikā on 8.3.6: अम्पर इति किम्? पुंक्षीरम्, पुंक्षुरम् — the ष् after
        the क् is not an अम्."""
        for text in ("pum kṣīram", "pum kṣuram"):
            r = mine(text)
            self.assertNotIn("8.3.6", steps(r), text)
            self.assertEqual(ours(r, 0)[0], "8.3.23", text)

    def test_paragrahaṇaṃ_kim_pumākhyaḥ_pumācāraḥ(self):
        """Kāśikā on 8.3.6: परग्रहणं किम्? पुमाख्यः, पुमाचारः — a vowel follows the
        म्, so nothing happens."""
        for text in ("pum ākhyaḥ", "pum ācāraḥ"):
            self.assertEqual(ours(mine(text)), [], text)

    def test_the_word_must_be_pum_itself(self):
        """पुमः names the word: any other म्-final word before a खय् takes the
        anusvāra of 8.3.23."""
        r = mine("kim kokilaḥ")
        self.assertNotIn("8.3.6", steps(r))

    def test_bhavāṃś_chādayati_8_3_7(self):
        """Kāśikā on 8.3.7: भवाँश्छादयति, भवांश्छादयति; भवाँश्चिनोति; भवाँष्टीकते;
        भवाँस्तरति. The न् is a रु before a छव् with an अम् after it; the ā
        before it is nasal or followed by the anusvāra. The विसर्ग, the स् and the
        श्चुत्व are other families' work: the form where this family leaves it is
        asserted, and the classical form as far as the visarga skeleton goes."""
        for text, khay in (("bhavān chādayati", "ch"), ("bhavān cinoti", "c"),
                           ("bhavān ṭīkate", "ṭ"), ("bhavān tarati", "t")):
            r = mine(text)
            self.assertEqual(ours(r, 0), ["8.3.7", "8.3.2"], text)
            self.assertEqual(ours(r, 1), ["8.3.7", "8.3.2*", "8.3.4"], text)
            self.assertEqual(step(r, "8.3.7").after.split()[0], "bhavāru", text)
            self.assertEqual(r.outcomes[0].steps[1].after.split()[0],
                             f"bhav{NAA}ru", text)
            self.assertEqual(step(r, "8.3.4", 1).after.split()[0],
                             "bhavāṃru", text)

    def test_the_classical_forms_as_far_as_the_skeleton_goes(self):
        """भवाँश्छादयति, भवांश्छादयति, शार्ङ्गिँश्छिन्धि, चक्रिँस्त्रायस्व — with the
        visarga family's 8.3.15, 8.3.34 and 8.4.40 (which the skeleton has)."""
        self.assertLessEqual(
            {f"bhav{NAA}śchādayati", "bhavāṃśchādayati"},
            surfaces("bhavān chādayati", "hal_assimilation"))
        self.assertLessEqual(
            {f"cakr{NI}strāyasva", "cakriṃstrāyasva"},
            surfaces("cakrin trāyasva", "hal_assimilation"))
        self.assertLessEqual(
            {f"śārṅg{NI}śchindhi", "śārṅgiṃśchindhi"},
            surfaces("śārṅgin chindhi", "hal_assimilation"))

    def test_chavīti_kim_bhavān_karoti(self):
        """Kāśikā on 8.3.7: छवीति किम्? भवान् करोति."""
        r = mine("bhavān karoti")
        self.assertEqual(ours(r), [])
        self.assertEqual(r.surface, "bhavānkaroti")

    def test_apraśānīti_kim_praśān_chādayati(self):
        """Kāśikā on 8.3.7: अप्रशानिति किम्? प्रशान् छादयति, प्रशान् चिनोति."""
        for text in ("praśān chādayati", "praśān cinoti"):
            self.assertEqual(ours(mine(text)), [], text)
        self.assertEqual(ours(mine("bhavān chādayati"))[0], "8.3.7")

    def test_amparīti_eva_bhavān_tsarukaḥ(self):
        """Kāśikā on 8.3.7: अम्पर इत्येव — भवान् त्सरुकः: after the त् comes a स्,
        which is not an अम्."""
        self.assertEqual(ours(mine("bhavān tsarukaḥ")), [])
        self.assertEqual(mine("bhavān tsarukaḥ").surface, "bhavāntsarukaḥ")

    def test_padasyeti_kim_hanti(self):
        """Kaumudī on 8.3.7: पदस्य किम्? हन्ति — the न् is inside the word; it is
        8.3.24 (with 8.4.58) that acts there, and gives हन्ति back."""
        r = mine("han~ti")
        self.assertNotIn("8.3.7", steps(r))
        self.assertEqual(ours(r), ["8.3.24", "8.4.58"])
        self.assertEqual(r.surfaces, ("hanti",))

    def test_8_3_2_reaches_only_the_ru_of_its_own_stretch(self):
        """Kāśikā on 8.3.2: इत उत्तरं यस्य स्थाने रुर्विधीयते. The रु of 8.2.66
        (रामस्, हरिस्) and of 8.3.1 stands before the heading: no nasal, no
        anusvāra."""
        r = sandhi("rāmas ca")
        self.assertEqual(steps(r)[0], "8.2.66")
        self.assertEqual(r.surfaces, ("rāmaśca",))
        self.assertFalse({"8.3.2", "8.3.3", "8.3.4", "8.3.5v"} & set(steps(r)))
        for text in ("haris ramyaḥ", "agnis atra", "manas ratha"):
            for outcome in sandhi(text).outcomes:
                self.assertFalse({"8.3.2", "8.3.3", "8.3.4"}
                                 & {s.sutra for s in outcome.steps}, text)

    def test_the_heading_is_read_from_the_corpus_and_ends_at_8_3_12(self):
        """The corpus records 8.3.2 as an अधिकार to 8.3.12, and the Kāśikā's own
        reason for अत्र: without it the heading would run on to ढो ढे लोपः."""
        heading = N._ru_prakarana()
        self.assertEqual(heading, frozenset(reading.governs("8.3.2")))
        for sutra in ("8.3.5", "8.3.6", "8.3.7"):
            self.assertIn(sutra, heading)
        for sutra in ("8.2.66", "8.3.1", "8.3.13", "8.3.15"):
            self.assertNotIn(sutra, heading)

    def test_the_option_of_8_3_2_forks_and_the_taken_course_is_first(self):
        r = mine("bhavān chādayati")
        self.assertEqual(r.outcomes[0].choices[0], ("8.3.2", True))
        self.assertEqual(r.outcomes[1].choices[0], ("8.3.2", False))
        self.assertEqual(step(r, "8.3.2").option, N.VA)
        declined = [s for s in r.outcomes[1].steps if s.declined]
        self.assertEqual([s.sutra for s in declined], ["8.3.2"])

    def test_8_3_4_puts_no_anusvara_where_the_sound_is_anunasika(self):
        """Bālamanoramā on 8.3.4: अनुनासिकं विहाय — where 8.3.2 made it nasal
        there is nothing to add; where it did not, the anusvāra is put in."""
        r = mine("pum kokilaḥ")
        self.assertNotIn("8.3.4", steps(r, 0))
        self.assertIn("8.3.4", steps(r, 1))
        nasal = [s for s in r.outcomes[0].final.segs if s.made_by == "8.3.2"]
        self.assertEqual(len(nasal), 1)
        self.assertTrue(nasal[0].nasal)
        (anu,) = made_by(r, "8.3.4", 1)
        self.assertEqual(anu.s, ANUSVARA)
        self.assertTrue(anu.has(AGAMA))

    def test_the_anusvara_of_8_3_4_is_asiddha_to_the_rules_before_it(self):
        """Tattvabodhinī and Bālamanoramā treat the anusvāra as an āgama put in
        by 8.3.4 — so 8.3.2 and 8.3.3, which stand before it, never see it,
        and 8.3.4 and the rules after do."""
        r = mine("pum kokilaḥ")
        final = r.outcomes[1].final
        seen = {viewer: "".join(s.s for s in View(final, viewer).live)
                for viewer in ("8.3.2", "8.3.3", "8.3.4", "8.3.5", "8.4.58")}
        self.assertNotIn("ṃ", seen["8.3.2"])
        self.assertNotIn("ṃ", seen["8.3.3"])
        for viewer in ("8.3.4", "8.3.5", "8.4.58"):
            self.assertIn("ṃ", seen[viewer], viewer)

    def test_a_sound_with_no_nasal_form_takes_the_anusvara_and_no_option(self):
        """A consonant has no anunāsika form to be made, so 8.3.2 has nothing to
        offer and 8.3.4 acts alone, without a fork. (Artificial — no Sanskrit
        word ends in त्न् — but it is the branch: 'anunāsikaṃ vihāya'.)"""
        r = mine("katn chādayati")
        self.assertEqual(len(r.outcomes), 1)
        self.assertEqual(ours(r), ["8.3.7", "8.3.4"])
        self.assertEqual(step(r, "8.3.4").after.split()[0], "katṃru")

    def test_the_anusvara_of_8_3_4_is_not_put_in_twice(self):
        r = mine("bhavān chādayati")
        for course in (0, 1):
            self.assertLessEqual(steps(r, course).count("8.3.4"), 1)
        self.assertEqual(len(made_by(r, "8.3.4", 1)), 1)

    def test_marutva_iha_and_mīḍhvastokāya_8_3_1(self):
        """Kāśikā on 8.3.1: इन्द्र मरुत्व इह पाहि सोमम्; मीढ्वस्तोकाय तनयाय मृळ. Vedic
        (`veda=True`): the न् of a मतुप्- or वसु-final vocative is a रु. The रु
        stands before 8.3.2, so no nasal follows (हरिवो मेदिनं त्वा)."""
        r = sandhi("marutvan{sambuddhi,matvanta} iha", veda=True)
        self.assertEqual(steps(r), ["8.3.1", "8.3.17", "8.3.19"])
        self.assertEqual(r.surfaces, ("marutvaiha", "marutvayiha"))
        found = step(r, "8.3.1")
        self.assertEqual((found.detail.sthanin, found.detail.adesa), ("n", "ru"))
        r = sandhi("mīḍhvan{sambuddhi,vasvanta} tokāya", veda=True)
        self.assertEqual(r.surfaces, ("mīḍhvastokāya",))
        self.assertEqual(steps(r), ["8.3.1", "8.3.15", "8.3.34"])

    def test_harivo_medinam_8_3_1_with_the_whole_rulebook(self):
        """Kāśikā and Kaumudī on 8.3.1: हरिवो मेदिनं त्वा — the रु of the मतुप्-final
        vocative, then 6.1.114 (उ) and 6.1.87 (ओ), as far as the rulebook goes."""
        r = sandhi("harivan{sambuddhi,matvanta} medinam", veda=True)
        self.assertEqual(r.surfaces, ("harivomedinam",))
        self.assertEqual(steps(r)[0], "8.3.1")

    def test_8_3_1_is_vedic_only_and_needs_the_caller_to_say_what_the_letters_cannot(self):
        """छन्दसि: not without `veda=True` (हे गोमन्, हे पपिवन् — Kāśikā:
        छन्दसीति किम्?); सम्बुद्धाविति किम्? — without `{sambuddhi}`; and the
        word must be said to end in मतुप् or वसु (मतुवसोरिति किम्? ब्रह्मन्
        स्तोष्यामः)."""
        self.assertNotIn("8.3.1", steps(sandhi("marutvan{sambuddhi,matvanta} iha")))
        for text in ("marutvan{matvanta} iha", "marutvan{sambuddhi} iha",
                     "brahman{sambuddhi} stoṣyāmaḥ"):
            self.assertNotIn("8.3.1", steps(sandhi(text, veda=True)), text)

    def test_mahāṃ_asi_8_3_3_the_ā_before_a_ru_and_an_aṭ_is_always_nasal(self):
        """Kāśikā on 8.3.3: महाँ असि, महाँ इन्द्रो य ओजसा, देवाँ अच्छा दीद्यत्. A रु
        of 8.3.2's stretch (here the one 8.3.9 gives, which this family does not
        make) after आ and before an अट्: the nasal is compulsory — ततः पूर्वस्य
        अतोऽनुनासिकविकल्पे प्राप्ते नित्यार्थं वचनम्."""
        for text in ("mahān asi", "mahān indraḥ", "devān acchā"):
            state = with_ru(text, veda=True)
            outcomes = derive(state, rulebook.rules_of(FAMILY))
            self.assertEqual(len(outcomes), 1, text)
            self.assertEqual([s.sutra for s in outcomes[0].steps], ["8.3.3"], text)
            self.assertTrue(
                [s for s in outcomes[0].final.segs if s.made_by == "8.3.3"][0].nasal)
            self.assertEqual(outcomes[0].steps[0].after.split()[0],
                             text.split()[0][:-2] + NAA + "ru", text)

    def test_the_nitya_takes_the_option_away_and_says_so(self):
        state = with_ru("mahān asi", veda=True)
        outcome = derive(state, rulebook.rules_of(FAMILY))[0]
        against = {a.sutra: a.why for a in outcome.steps[0].against}
        self.assertIn("8.3.2", against)
        self.assertIn("ततः पूर्वस्यातोऽनुनासिकविकल्पे प्राप्ते नित्यार्थं वचनम्",
                      against["8.3.2"])
        self.assertNotIn("8.3.4", [s.sutra for s in outcome.steps])

    def test_ātaḥ_iti_kim_and_aṭīti_kim_leave_the_option_of_8_3_2(self):
        """Kāśikā on 8.3.3: आत इति किम्? ये वा वनस्पतीँरनु (an ई, so 8.3.2's
        option); अटीति किम्? भवांश्चरति (a छव् follows, not an अट्)."""
        for text in ("vanaspatīn anu", "bhavān charati"):
            state = with_ru(text, veda=True)
            outcomes = derive(state, rulebook.rules_of(FAMILY))
            self.assertEqual(len(outcomes), 2, text)
            self.assertNotIn("8.3.3", [s.sutra for s in outcomes[0].steps], text)
            self.assertEqual(outcomes[0].steps[0].sutra, "8.3.2", text)

    def test_8_3_3_is_vedic_and_not_offered_otherwise(self):
        state = with_ru("mahān asi", veda=False)
        outcomes = derive(state, rulebook.rules_of(FAMILY))
        self.assertNotIn("8.3.3", [s.sutra for s in outcomes[0].steps])


def reading_order(sutra):
    return tuple(int(p) for p in sutra.split("."))


class Input(unittest.TestCase):

    def test_devanagari_and_iast_give_the_same_derivation(self):
        for deva_text, iast_text in (("हरिम् वन्दे", "harim vande"),
                                     ("त्वम् करोषि", "tvam karoṣi"),
                                     ("प्राङ् शेते", "prāṅ śete"),
                                     ("भवान् छादयति", "bhavān chādayati")):
            a, b = mine(deva_text), mine(iast_text)
            self.assertEqual(a.surfaces, b.surfaces, iast_text)
            self.assertEqual([steps(a, c) for c in range(len(a.outcomes))],
                             [steps(b, c) for c in range(len(b.outcomes))])

    def test_a_candrabindu_and_an_anusvara_written_either_way_are_read_alike(self):
        """ṃ and ṁ are the same sound to the reader of 8.4.59."""
        self.assertEqual(mine("taṃ kathaṃ").surfaces,
                         mine("taṁ kathaṁ").surfaces)


class TheHeading(unittest.TestCase):

    def test_8_3_2_governs_exactly_8_3_2_to_8_3_12(self):
        """The corpus records the adhikāra's end (the Kāśikā's own reason for
        अत्र is that it should not run on to ढो ढे लोपः, 8.3.13)."""
        self.assertEqual(
            sorted(N._ru_prakarana(), key=lambda s: tuple(map(int, s.split(".")))),
            [f"8.3.{n}" for n in range(2, 13)])


class AgreesWithTheProvisionTable(unittest.TestCase):
    """`ru_anunasika.RU_TABLE` is the project's earlier codification of
    8.3.1–33 as provision rows (which sūtra is an option, which keeps another
    off). The rules here are steps and not rows, so the two are written
    separately — and must say the same."""

    STEP_FOR = {          # a form that meets each sūtra, and its course
        "8.3.2": ("bhavān chādayati", 0), "8.3.4": ("bhavān chādayati", 1),
        "8.3.5": ("sam|skartā{sut}", 0), "8.3.6": ("pum kokilaḥ", 0),
        "8.3.7": ("bhavān chādayati", 0), "8.3.23": ("kuṇḍam hasati", 0),
        "8.3.24": ("yaśān~si", 0), "8.3.25": (f"sam|{RAJ}", 0),
        "8.3.26": ("kim hmalayati", 0), "8.3.27": ("kim hnute", 0),
        "8.3.28": ("prāṅ śete", 0), "8.3.29": ("ṣaḍ santaḥ", 0),
        "8.3.30": ("bhavān sāye", 0), "8.3.31": ("san śambhuḥ", 0),
        "8.3.32": ("pratyaṅ ātmā", 0),
    }

    def test_the_same_sutras_are_options(self):
        for sutra, (text, course) in self.STEP_FOR.items():
            (row,) = ru_anunasika.provisions_for(sutra)
            r = mine(text)
            found = [s for s in r.outcomes[course].steps
                     if s.sutra == sutra and s.detail.authority != VARTTIKA]
            self.assertTrue(found, sutra)
            self.assertEqual(bool(found[0].option), row.optional, sutra)

    def test_the_same_sutras_keep_the_same_others_off(self):
        for sutra in ("8.3.2", "8.3.3", "8.3.4", "8.3.5", "8.3.6", "8.3.7",
                      "8.3.23", "8.3.24", "8.3.25", "8.3.26", "8.3.27",
                      "8.3.28", "8.3.29", "8.3.30", "8.3.31", "8.3.32"):
            (row,) = ru_anunasika.provisions_for(sutra)
            rules = [r for r in N.RULES if r.sutra == sutra]
            self.assertTrue(rules, sutra)
            for rule in rules:
                self.assertEqual({target for target, _ in rule.overrides},
                                 set(row.blocks), sutra)

    def test_the_table_and_the_rules_name_the_same_ru_making_sutras(self):
        """The rows that give a रु are the rules that make the RU."""
        rows = {row.sutra for row in ru_anunasika.RU_TABLE
                if row.does == "ru" and row.sutra in
                {"8.3.1", "8.3.5", "8.3.6", "8.3.7"}}
        made = set()
        for text, veda in (("marutvan{sambuddhi,matvanta} iha", True),
                           ("sam|skartā{sut}", False), ("pum kokilaḥ", False),
                           ("bhavān chādayati", False)):
            for outcome in mine(text, veda=veda).outcomes:
                for found in outcome.steps:
                    if found.detail.adesa == "ru" and found.sutra in MY:
                        made.add(found.sutra)
        self.assertEqual(rows, made)

    def test_where_the_table_is_silent_this_family_says_what_it_reasoned(self):
        """The table marks only 8.3.1 as छान्दस in this run; 8.3.3 is marked
        vedic here because its रु is the one 8.3.9 gives and all the Kāśikā's
        examples are Vedic — a reading, and in `open_questions`."""
        chandasi = {r.sutra for r in ru_anunasika.RU_TABLE if r.chandasi}
        self.assertIn("8.3.1", chandasi)
        for sutra in {r.sutra for r in N.RULES if r.vedic}:
            self.assertIn(sutra, {"8.3.1", "8.3.3"})


class DocstringQuotations(unittest.TestCase):
    """The words of the tradition that the module's docstrings quote, and that
    no reason or note carries, are the commentaries' own."""

    QUOTES = (
        ("kashika", "8.3.2", "इत उत्तरं यस्य स्थाने रुर्विधीयते"),
        ("kashika", "8.3.3", "आत इति किम्?"),
        ("kashika", "8.3.4", "अन्यशब्दोऽत्राध्याहर्तव्यः"),
        ("kashika", "8.3.5", "सम इति किम्? उपस्कर्ता"),
        ("kashika", "8.3.5", "सुटीति किम्? संकृतिः"),
        ("kashika", "8.3.5", "रुविधौ ह्यनिष्टप्रसङ्गः"),
        ("tattvabodhini", "8.3.5", "यद्यपि मोऽनुस्वारेण सिद्धं"),
        ("kashika", "8.3.6", "खयीति किम्? पुंदासः"),
        ("kashika", "8.3.6", "अम्पर इति किम्? पुंक्षीरम्"),
        ("kashika", "8.3.6", "परग्रहणं किम्? पुमाख्यः"),
        ("kaumudi", "8.3.6", "ख्याञादेशे न"),
        ("kashika", "8.3.7", "अप्रशानिति किम्? प्रशान् छादयति"),
        ("kashika", "8.3.7", "अम्पर इत्येव — भवान् त्सरुकः"),
        ("kaumudi", "8.3.7", "पदस्य किम् । हन्ति"),
        ("kashika", "8.3.23", "हलीत्येव — त्वमत्र। किमत्र"),
        ("kashika", "8.3.23", "पदान्तस्येत्येव — गम्यते। रम्यते"),
        ("kashika", "8.3.24", "अपदान्तस्येति किम्? राजन् भुङ्क्ष्व"),
        ("kashika", "8.3.25", "राजीति किम्? संयत्"),
        ("kashika", "8.3.25", "सम इति किम्? किंराट्"),
        ("kashika", "8.3.25", "क्वाविति किम्? संराजिता"),
        ("kaumudi", "8.3.28", "कुक्टुकोरसिद्धत्वाज्जश्त्वं न"),
        ("kashika", "8.3.28", "पूर्वान्तकरणं"),
        ("kashika", "8.3.29", "परादिकरणं"),
        ("balamanorama", "8.3.29", "चर्त्वस्यासिद्धत्वाड्डात्परत्वात्सस्य धुट्"),
        ("kashika", "8.3.30", "धुटश्चर्त्वस्य चासिद्धत्वाद्"),
        ("kashika", "8.3.31", "पूर्वान्तकरणं छत्वार्थम्"),
        ("kashika", "8.3.32", "ङम इति किम्? त्वमास्से"),
        ("kashika", "8.3.32", "ह्रस्वादिति किम्? प्राङास्ते"),
        ("kashika", "8.3.32", "अचीति किम्? प्रत्यङ् करोति"),
        ("kashika", "8.3.32", "उत्तरपदत्वे चापदादिविधौ"),
        ("kaumudi", "8.3.33", "वत्वस्यासिद्धत्वान्नानुस्वारः"),
        ("kashika", "8.3.33", "प्रगृह्यत्वादुञः प्रकृतिभावे प्राप्ते वकारो विधीयते"),
        ("kashika", "8.4.45", "पदान्तस्येत्येव — वेद्मि। क्षुभ्नाति"),
        ("kashika", "8.4.45", "व्यवस्थितविभाषाविज्ञानात् सिद्धम्"),
        ("kaumudi", "8.4.45",
         "स्थानप्रयत्नाभ्यामन्तरतमे स्पर्शे चरितार्थो विधिरयं रेफे न प्रवर्तते"),
        ("kashika", "8.4.58", "ययीति किम्? आक्रंस्यते"),
        ("tattvabodhini", "8.4.58",
         "शलि तु परसवर्णोऽनुस्वारान्तरतमो न संभवतीति"),
        ("nyaas", "8.4.59", "वावचनं पूर्वस्य नित्यात्वज्ञापनार्थम्"),
        ("balamanorama", "8.3.28", "उकार उच्चारणार्थः"),
        ("balamanorama", "8.3.4", "आगमत्वं परशब्दलभ्यम्"),
        ("kashika", "8.3.1", "नकारस्य रुर्भवति"),
        ("kashika", "8.3.1", "छन्दसीति किम्? हे गोमन्"),
        ("kashika", "8.3.1", "मतुवसोरिति किम्? ब्रह्मन् स्तोष्यामः"),
        ("kashika", "8.3.1", "संबुद्धाविति किम्?"),
        ("kashika", "8.3.3", "अटीति किम् ? भवांश्चरति"),
        ("kashika", "8.3.5", "समः स्सुटीति द्विसकारको निर्देशः"),
        ("kashika", "8.3.6", "तस्मादत्र सकार एवादेशो वक्तव्यः"),
    )

    def test_each_is_in_the_commentary_it_is_credited_to(self):
        missing = []
        for source, sutra, text in self.QUOTES:
            found = corpus.commentary_on(sutra, source)
            if found is None or norm(text) not in norm(found):
                missing.append((source, sutra, text))
        self.assertEqual(missing, [])


# ---------------------------------------------------------------------------
# Options and steps, as the engine returns them
# ---------------------------------------------------------------------------


class Options(unittest.TestCase):

    def test_every_option_is_named_by_the_word_va(self):
        for text, sutra in (("bhavān chādayati", "8.3.2"),
                            ("kim hmalayati", "8.3.26"), ("kim hnute", "8.3.27"),
                            ("prāṅ śete", "8.3.28"), ("ṣaḍ santaḥ", "8.3.29"),
                            ("bhavān sāye", "8.3.30"), ("san śambhuḥ", "8.3.31"),
                            ("harim vande", "8.4.59"),
                            ("vāg nayati", "8.4.45"),
                            ("kim u{nipata} uktam", "8.3.33")):
            r = maya(text) if sutra == "8.3.33" else mine(text)
            self.assertEqual(step(r, sutra).option, N.VA, sutra)

    def test_the_rules_that_are_not_options_do_not_fork(self):
        for text in ("yaśān~si", "pratyaṅ ātmā", "kurvan~ti", "tvam atra"):
            self.assertEqual(len(mine(text).outcomes), 1, text)

    def test_the_declined_course_says_it_declined(self):
        r = mine("prāṅ śete")
        declined = [s for s in r.outcomes[1].steps if s.declined]
        self.assertEqual([s.sutra for s in declined], ["8.3.28"])
        self.assertEqual(declined[0].before, declined[0].after)

    def test_a_declined_option_is_not_offered_again_when_a_later_rule_changes_the_place(self):
        """The engine remembers a declined option by the place's uids; a later
        rule that changes a sound of the place renews its uid, and the rule
        would take a second chance on the sound it now sees only through its
        past. It does not: in each course 8.3.29 is offered once, taken or
        declined. (The skeleton's 8.4.55 turns the ḍ of ṣaḍ into ṭ, after
        8.3.29 has been declined.)"""
        r = mine("ṣaḍ santaḥ", "hal_assimilation")
        for course in range(len(r.outcomes)):
            offered = [s for s in steps(r, course) if s.startswith("8.3.29")]
            self.assertEqual(len(offered), 1, (course, steps(r, course)))
        self.assertIn("8.4.55", steps(r, 1))          # the change did happen

    def test_the_same_holds_for_the_option_on_the_anusvara_before_a_changed_yay(self):
        """8.4.59 declined, then a later rule changes the following sound: the
        option is not taken on the second look. (A fixture rule numbered after
        8.4.59 turns क् into ख् once.)"""
        @make_rule("8.4.60", name="fixture", families=())
        def khu(v):
            for j in v.pairs():
                if j.right.s == "k" and not j.right.seg.made_by:
                    yield Application(
                        site=site(j.right), edits=(edit_replace(j.right, "kh"),),
                        detail=Detail(kind=ADESA, sthanin="k", adesa="kh",
                                      nimitta="", because=""))
        rules = rulebook.rules_of(FAMILY) + (khu,)
        r = sandhi("taṃ karoti", rules=rules)
        for course in range(len(r.outcomes)):
            offered = [s for s in steps(r, course) if s.startswith("8.4.59")]
            self.assertEqual(len(offered), 1, (course, steps(r, course)))


# ---------------------------------------------------------------------------
# What the trace says
# ---------------------------------------------------------------------------


class TheTrace(unittest.TestCase):

    CASES = ("harim vande", "sam|skartā{sut}", "pum kokilaḥ", "bhavān chādayati",
             "kim hmalayati", "kim hnute", "kim hyaḥ", "tvam karoṣi",
             "prāṅ śete", "ṣaḍ santaḥ", "bhavān sāye", "san śambhuḥ",
             "pratyaṅ ātmā", "yaśān~si", "kurvan~ti", "vāg nayati",
             "tad-mātra{pratyaya}", f"sam|{RAJ}")

    def test_the_trace_prints_every_form_in_both_scripts(self):
        out = mine("harim vande").trace()
        self.assertIn("हरिं वन्दे (hariṃ vande)", out)
        self.assertIn("मोऽनुस्वारः (mo’nusvāraḥ)", out)
        self.assertIn("अलोऽन्त्यस्य (alo’ntyasya)", out)

    def test_the_quoted_words_of_every_step_are_the_corpus_words(self):
        known = corpus.load_vidyut_sutrapatha()
        for text in self.CASES:
            for outcome in mine(text).outcomes:
                for found in trace.outcome_dict(outcome)["steps"]:
                    self.assertEqual(found["sutra_iast"],
                                     known[found["sutra"]].text)
                    for via in found["via"]:
                        self.assertEqual(via["text_iast"],
                                         known[via["sutra"]].text)

    def _every_step_of_this_family(self):
        """One step of each rule of this family, at least, from real forms and
        from the two Vedic sūtras' own."""
        for text in self.CASES + (
                "kim hyaḥ", "kim hvalayati", "vāc-maya{pratyaya}",
                "sam|rājitā{dhatu:rāj}", "tam kathaṃ", "an~citaḥ",
                "sugaṇ īśaḥ", "vaṇ śete", "śvaliḍ sāye"):
            for outcome in mine(text).outcomes:
                yield text, outcome
        for text in ("marutvan{sambuddhi,matvanta} iha",
                     "mīḍhvan{sambuddhi,vasvanta} tokāya"):
            for outcome in sandhi(text, veda=True).outcomes:
                yield text, outcome
        for outcome in derive(with_ru("mahān asi", veda=True),
                              rulebook.rules_of(FAMILY)):
            yield "mahān asi", outcome
        for outcome in maya("kim u{nipata} uktam").outcomes:
            yield "kim u uktam", outcome

    def test_every_rule_of_the_family_is_seen_in_these_cases(self):
        seen = set()
        for _, outcome in self._every_step_of_this_family():
            seen.update(s.sutra for s in outcome.steps if s.sutra in MY)
        self.assertLessEqual(MY, seen)

    def test_no_explanation_carries_a_devanagari_word_without_its_roman(self):
        """Every Sanskrit term in a reason is in braces, so the trace prints it
        in both scripts: none of a step's own texts holds Devanāgarī. (A `note`
        may quote the tradition, and prints the quotation with its roman.)"""
        deva = re.compile("[\u0900-\u097F]")
        count = 0
        for text, outcome in self._every_step_of_this_family():
            for found in outcome.steps:
                if found.sutra not in MY:
                    continue
                d = found.detail
                # 1.3.2 and 1.3.9 are the core's `supports.it_removed`, 1.1.70
                # its `supports.tapara`: their words are the core's own
                own = [v.role for v in d.via
                       if v.sutra not in ("1.3.2", "1.3.9", "1.1.70")]
                for field in (d.nimitta, d.because, *own):
                    self.assertIsNone(deva.search(field),
                                      (text, found.sutra, field))
                count += 1
        self.assertGreater(count, 60)

    def test_every_sutra_any_step_leans_on_is_the_one_meant(self):
        """A number written wrong would still be a sūtra of the corpus, so it
        is not enough that it exists: each sūtra a step of this family cites is
        checked against the words it must have (the Vidyut text)."""
        meant = {
            "1.1.46": "ādyantau ṭakitau", "1.1.50": "sthāne’ntaratamaḥ",
            "1.1.52": "alo’ntyasya", "1.1.66": "tasminniti nirdiṣṭe pūrvasya",
            "1.1.67": "tasmādityuttarasya", "1.1.69": "aṇudit savarṇasya cāpratyayaḥ",
            "1.1.70": "taparastatkālasya", "1.1.71": "ādirantyena sahetā",
            "1.1.72": "yena vidhistadantasya", "1.1.9": "tulyāsyaprayatnaṃ savarṇam",
            "1.3.10": "yathāsaṃkhyamanudeśaḥ samānām", "1.3.2": "upadeśe’janunāsika it",
            "1.3.9": "tasya lopaḥ", "1.4.109": "paraḥ sannikarṣaḥ saṃhitā",
            "1.4.17": "svādiṣvasarvanāmasthāne", "8.1.16": "padasya",
        }
        used = set()
        for _, outcome in self._every_step_of_this_family():
            for found in outcome.steps:
                if found.sutra in MY:
                    used.update(v.sutra for v in found.detail.via)
        self.assertLessEqual(used, set(meant), used - set(meant))
        for sutra in used:
            self.assertEqual(trace.sutra_text(sutra), meant[sutra], sutra)

    def test_the_result_serialises(self):
        import json
        for text in self.CASES:
            json.dumps(mine(text).to_dict(), ensure_ascii=False)

    def test_every_step_of_this_family_says_what_this_form_did(self):
        """`because` names the sounds of THIS form, not the rule in general."""
        wanted = {
            "harim vande": ("m", "v"), "yaśān~si": ("n", "s"),
            "prāṅ śete": ("ś",), "pratyaṅ ātmā": ("ṅ", "ā"),
            "kim hmalayati": ("h", "m"), "bhavān chādayati": ("n", "ch")}
        for text, sounds in wanted.items():
            first = [s for s in mine(text).outcomes[0].steps
                     if s.sutra in MY][0]
            for sound in sounds:
                self.assertIn("{" + sound + "}", first.detail.because, text)


# ---------------------------------------------------------------------------
# Provisions taken out: the tests above can fail
# ---------------------------------------------------------------------------


class TheseTestsCanFail(unittest.TestCase):

    def _without(self, sutra, **change):
        return tuple(replace(r, **change) if r.sutra == sutra else r
                     for r in rulebook.rules_of(FAMILY, "visarga_ru"))

    def test_without_consumes_8_3_2_goes_blind(self):
        """8.3.2's wording names the रु that a LATER tripādī rule made; 8.2.1
        would hide it. Take `consumes` away and the rule sees only the म्."""
        rules = self._without("8.3.2", consumes=frozenset())
        r = sandhi("sam|skartā{sut}", rules=rules)
        self.assertNotIn("8.3.2", steps(r))
        self.assertEqual(steps(r)[0], "8.3.5")

    def test_without_consumes_8_3_4_puts_in_no_anusvara(self):
        rules = self._without("8.3.4", consumes=frozenset())
        r = sandhi("sam|skartā{sut}", rules=rules)
        self.assertNotIn("8.3.4", [s for c in range(len(r.outcomes))
                                   for s in steps(r, c)])

    def test_without_the_override_8_3_23_takes_the_m_of_samrat(self):
        """The refusal is what keeps the anusvāra out: without 8.3.25 the
        म् is an anusvāra."""
        rules = tuple(r for r in rulebook.rules_of(FAMILY, "visarga_ru")
                      if r.sutra != "8.3.25")
        r = sandhi(f"sam|{RAJ}", rules=rules)
        self.assertEqual(steps(r)[0], "8.3.23")
        self.assertIn(ANUSVARA, r.surface)

    def test_without_the_override_8_3_23_acts_first_at_kim_hmalayati(self):
        """8.3.26 and 8.3.23 both reach the म् of किम् ह्मलयति; with the
        `overrides` taken away the earlier rule is 8.3.23, and the option can no
        longer keep the anusvāra out."""
        rules = tuple(replace(r, overrides=()) if r.sutra == "8.3.26" else r
                      for r in rulebook.rules_of(FAMILY, "visarga_ru"))
        r = sandhi("kim hmalayati", rules=rules)
        self.assertEqual(steps(r)[0], "8.3.23")
        self.assertEqual(r.surfaces, ("kiṃhmalayati",))

    def test_a_bare_r_and_the_ru_of_8_2_66_are_left_alone_by_the_heading(self):
        """The RU mark and the heading decide 8.3.2: the र् of पुनर् (no रु) and
        the रु of 8.2.66 (रामस्) are not under it."""
        for text in ("punar atra", "punar ca", "rāmas ca"):
            r = mine(text)
            self.assertFalse({"8.3.2", "8.3.4", "8.3.5v"} & set(steps(r)), text)

    def test_widen_the_heading_and_the_ru_of_8_2_66_takes_the_nasal(self):
        """The control: were the ru of 8.2.66 under 8.3.2, रामस् + च would get a
        nasal or an anusvāra. It does not, because the heading is what the
        corpus says it is."""
        from unittest import mock
        wide = N._ru_prakarana() | {"8.2.66"}
        with mock.patch.object(N, "_ru_prakarana", lambda: wide):
            r = mine("rāmas ca")
        self.assertIn("8.3.2", steps(r) + steps(r, 1))

    def test_a_visarga_family_without_the_ru_mark_would_hide_the_ru_from_8_3_2(self):
        """`consumes` and the mark are the pair: with the mark left off the ru
        that 8.3.5 makes, 8.3.2 does not know it for a रु."""
        rules = tuple(r for r in rulebook.rules_of(FAMILY, "visarga_ru"))
        state = with_ru("bhavān chādayati", by="8.3.7")
        old = [s for s in state.segs if s.has(RU)][0]
        bare = replace(old, marks=frozenset())
        marked = derive(state, rules)[0]
        plain = derive(replace(state, segs=tuple(
            bare if s is old else s for s in state.segs)), rules)[0]
        self.assertIn("8.3.2", [s.sutra for s in marked.steps])
        self.assertNotIn("8.3.2", [s.sutra for s in plain.steps])


class Timing(unittest.TestCase):

    def test_a_derivation_stays_in_the_millisecond_range(self):
        sandhi("harim vande")                     # warm the lazy imports
        start = time.time()
        for _ in range(20):
            sandhi("sam|skartā{sut}")
            sandhi("pum kokilaḥ")
            sandhi("bhavān chādayati")
        self.assertLess((time.time() - start) / 60, 0.25)


if __name__ == "__main__":
    unittest.main()
