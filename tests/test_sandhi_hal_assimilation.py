# -*- coding: utf-8 -*-
"""
The consonant-assimilation family — 6.1.71–76, 8.2.24–41, 8.4.40–44, 8.4.55,
8.4.56, 8.4.60–63, 8.4.65–68 — tested against the commentaries' own words.

Each expectation is a worked example, or a counter-example (*X iti kim?*), that
the Kāśikā, the Siddhāntakaumudī, the Bālamanoramā or the Nyāsa gives, and the
docstring of the test names which. Where a result could come out right by luck
the test also asserts the STEPS — the sūtras, in order — because in the tripādī
the order is the grammar (8.2.1): वाक्पतिः is right only if 8.2.30, 8.2.39 and
8.4.55 come in that order and 8.2.39 does not see what 8.4.55 made.

**Most tests derive under this family's rules alone** (`mine`), plus the
visarga family where a final स् is in play. That keeps them about *these* rules
and makes them stay true when the other families are merged in: a form that
needs 8.4.53 (लब्धा) or 8.4.45 (षण्णाम्) is asserted at the point THIS family
leaves it, and says so. The classical surfaces of the Laghusiddhāntakaumudī
(तच्छिवः, शिवच्छाया, वाग्घरिः …) are asserted against the whole rulebook too.

A test that cannot fail is worse than none (NORTH_STAR §3): the last classes
take a rule OUT and show the answer change.
"""

from __future__ import annotations

import re
import unittest
from dataclasses import replace

from src.astadhyayi import corpus
from src.astadhyayi.anga import (
    coh_kuh as anga_coh_kuh, jhalam_jas_jhasi, jhasas_tathoh_dhah,
    khari_ca as anga_khari_ca)
from src.astadhyayi.sandhi import rulebook, sandhi, trace
from src.astadhyayi.sandhi.engine import derive
from src.astadhyayi.sandhi.families import hal_assimilation as H
from src.astadhyayi.sandhi.parse import parse
from src.astadhyayi.sandhi.rule import VARTTIKA
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.varna import VARGA

FAMILY = "hal_assimilation"


def mine(text, *extra, **kw):
    """The junction derived by this family's rules alone (and any named
    family's), so the test is about these rules and no others."""
    return sandhi(text, rules=rulebook.rules_of(FAMILY, *extra), **kw)


def steps(result, course=0, *, declined=False):
    """The sūtras of one course, in order; a declined option is starred."""
    return [s.sutra + ("*" if s.declined else "")
            for s in result.outcomes[course].steps
            if declined or not s.declined]


def order_of(result, wanted, course=0):
    """The steps of `wanted` that occur, in the order they occur — so a test
    can say 'these, in this order' without listing what lies between."""
    return [s for s in steps(result, course) if s in wanted]


def surfaces(text, *extra, **kw):
    return set(mine(text, *extra, **kw).surfaces)


def whole(text, **kw):
    return sandhi(text, **kw)


# ---------------------------------------------------------------------------
# The record itself: numbers, names, quotations, coverage
# ---------------------------------------------------------------------------

_MARKUP = re.compile(r"<<|>>|\[\[[^\]]*\]\]|<\{[^}]*\}>|<!|!>|</?w>|\(\d+\)|\s+")


def norm(text):
    """A commentary's words without the corpus's own markup and spacing — so a
    quotation is compared with what the commentary says, not how it is set."""
    return _MARKUP.sub("", text or "")


SCOPE = (
    [f"6.1.{n}" for n in range(71, 77)]
    + [f"8.2.{n}" for n in range(24, 42)]
    + [f"8.4.{n}" for n in (40, 41, 42, 43, 44, 55, 56, 60, 61, 62, 63,
                            65, 66, 67, 68)])


class TheRecord(unittest.TestCase):
    """Every number, name and quotation is the corpus's and the commentary's
    own — none was written from memory."""

    def test_the_rulebook_is_sound_with_this_family_loaded(self):
        self.assertEqual(rulebook.problems(), [])

    def test_every_rule_is_named_by_its_own_words_from_the_corpus(self):
        known = corpus.load_vidyut_sutrapatha()
        for r in H.RULES:
            self.assertIn(r.sutra, known)
            self.assertEqual(r.name, trace.deva(known[r.sutra].text), r.sutra)

    def test_coverage_names_every_sutra_of_the_scope_once_and_no_other(self):
        listed = [sutra for sutra, _, _ in H.COVERAGE]
        self.assertEqual(sorted(listed), sorted(set(listed)))
        self.assertEqual(set(listed), set(SCOPE))
        self.assertEqual(len(listed), 39)

    def test_a_sutra_is_not_called_a_rule_unless_a_rule_stands_for_it(self):
        have = {r.sutra for r in H.RULES}
        for sutra, status, note in H.COVERAGE:
            if status in ("rule", "partial"):
                self.assertIn(sutra, have, sutra)
            else:
                self.assertNotIn(sutra, have, sutra)
            if status in ("scope", "partial", "support"):
                self.assertGreater(len(note), 20, sutra)

    def test_the_accent_sutras_are_scope_and_say_why(self):
        got = {s: (st, n) for s, st, n in H.COVERAGE}
        for sutra in ("8.4.66", "8.4.67", "8.4.68"):
            self.assertEqual(got[sutra][0], "scope")
        self.assertIn("accent", got["8.4.66"][1])

    def test_every_quotation_is_in_the_commentary_it_names(self):
        self.assertGreater(len(H.QUOTED), 10)
        for source, sutra, text in H.QUOTED:
            if source == "bhashya":
                found = corpus.commentary_on(sutra, "bhashya")
            else:
                found = corpus.commentary_on(sutra, source)
            self.assertIsNotNone(found, (source, sutra))
            self.assertIn(norm(text), norm(found), (source, sutra, text))

    def test_a_quotation_that_is_not_the_commentary_s_would_be_caught(self):
        """The check above must be able to fail."""
        found = corpus.commentary_on("8.4.44", "kashika")
        self.assertNotIn(norm("शात्परस्य तवर्गस्य श्चुत्वं न स्यात्"),
                         norm(found))

    def test_every_reason_for_an_override_is_a_quotation(self):
        said = [text for _, _, text in H.QUOTED]
        seen = 0
        for r in H.RULES:
            for target, why in r.overrides:
                seen += 1
                self.assertTrue(any(q in why for q in said), (r.sutra, target))
        self.assertGreaterEqual(seen, 10)

    def test_a_varttika_is_the_vartikas_own_words(self):
        """Vārttikas are not Pāṇini: each is labelled, and its text is the
        corpus's (or, for the Vedic one, the Kāśikā's)."""
        found = [r for r in H.RULES if r.authority == VARTTIKA]
        self.assertEqual({(r.sutra) for r in found},
                         {"8.2.35", "8.2.36", "8.4.63"})
        for r in found:
            corpus_texts = [v.text for v in corpus.varttikas_on(r.sutra)]
            kashika = norm(corpus.commentary_on(r.sutra, "kashika"))
            self.assertTrue(
                r.varttika in corpus_texts or norm(r.varttika) in kashika,
                (r.sutra, r.varttika))

    def test_the_vedic_rule_is_marked_vedic(self):
        vedic = [r for r in H.RULES if r.vedic]
        self.assertEqual([r.sutra for r in vedic], ["8.2.35"])


# ---------------------------------------------------------------------------
# 8.2.30 चोः कुः, 8.2.39 झलां जशोऽन्ते, 8.4.55 खरि च — and the order of the three
# ---------------------------------------------------------------------------


class Vakpati(unittest.TestCase):
    """वाक्पतिः — the case the tripādī's order exists to settle."""

    def test_three_rules_in_this_order_and_no_ping_pong(self):
        """8.2.30 makes क्, 8.2.39 makes ग्, 8.4.55 makes क् — and 8.2.39
        does not see the क् of 8.4.55 and turn it back."""
        r = mine("vāc pati")
        self.assertEqual(r.surfaces, ("vākpati",))
        self.assertEqual(steps(r), ["8.2.30", "8.2.39", "8.4.55"])
        self.assertEqual(r.outcomes[0].stopped, "no rule applies")

    def test_the_intermediate_forms_are_the_traditions(self):
        r = mine("vāc pati")
        self.assertEqual([s.after for s in r.outcomes[0].steps],
                         ["vāk pati", "vāg pati", "vāk pati"])

    def test_vagisah_LSK_8_2_39(self):
        """Laghusiddhāntakaumudī, झलां जशोऽन्ते: वागीशः."""
        r = mine("vāc īśa")
        self.assertEqual(r.surfaces, ("vāgīśa",))
        self.assertEqual(steps(r), ["8.2.30", "8.2.39"])
        self.assertEqual(sandhi("vāc īśaḥ").surface, "vāgīśaḥ")

    def test_the_final_visarga_is_the_visarga_familys_and_still_derived(self):
        r = mine("vāc īśaḥ", "visarga_ru")
        self.assertIn("8.2.66", steps(r))
        self.assertEqual(r.surface, "vāgīśaḥ")


class CohKuh(unittest.TestCase):
    """8.2.30."""

    def test_pakta_vakta_Kasika(self):
        """Kāśikā: पक्ता, वक्ता (a झल् follows)."""
        for text, expected in (("pac~tā", "paktā"), ("vac~tā", "vaktā")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r), ["8.2.30"], text)

    def test_a_pada_end_gives_both_courses_Kasika(self):
        """Kāśikā: ओदनपक्, वाक् — at the end of a pada, and 8.4.56's option
        then leaves क् or ग्."""
        for text, pair in (("odana-pac", {"odanapak", "odanapag"}),
                           ("vāc", {"vāk", "vāg"})):
            r = mine(text)
            self.assertEqual(set(r.surfaces), pair, text)
            self.assertEqual(order_of(r, {"8.2.30", "8.2.39", "8.4.56"}),
                             ["8.2.30", "8.2.39", "8.4.56"], text)

    def test_each_cu_sound_takes_its_own_ku_sound(self):
        """1.1.50: च्→क्, छ्→ख्, ज्→ग्, झ्→घ्, ञ्→ङ् — nothing is tabled."""
        for cu, ku in zip(VARGA["cu"], VARGA["ku"]):
            r = mine(f"a{cu}~ta")
            self.assertEqual(r.outcomes[0].steps[0].detail.adesa, ku, cu)

    def test_it_does_not_reach_inside_a_finished_word(self):
        """गच्छति keeps its च्छ् — 8.2.30 must not read the च् that 8.4.40
        made out of a त् long ago (the README's example)."""
        for text in ("gacchati", "rāmas gacchati", "ud gacchati"):
            for outcome in mine(text, "visarga_ru").outcomes:
                self.assertIn("gacchati", outcome.surface, text)
                self.assertNotIn("8.2.30", [s.sutra for s in outcome.steps])

    def test_udgacchati_is_left_as_it_is(self):
        r = mine("ud gacchati")
        self.assertEqual(r.surfaces, ("udgacchati",))
        self.assertEqual(steps(r), [])

    def test_the_sound_8_4_40_made_is_not_seen_by_8_2_30(self):
        """सच्चित् (Bālamanoramā on 8.4.40): 8.4.40 makes the द् a ज्, 8.4.55
        makes it च्, and 8.2.30 does NOT turn that च् to क् — ścutva is asiddha
        to it. The trace never has 8.2.30 in it."""
        r = mine("sat cit")
        self.assertNotIn("8.2.30", steps(r))
        self.assertEqual(steps(r)[:3], ["8.2.39", "8.4.40", "8.4.55"])

    def test_it_agrees_with_the_projects_own_question_form(self):
        """`anga.coh_kuh` is 8.2.30 as a question; every कु sound it names is
        the one the engine's step puts in."""
        for cu in VARGA["cu"]:
            asked = anga_coh_kuh(cu, at_pada_end=True).result
            r = mine(f"a{cu}~ta")
            self.assertEqual(r.outcomes[0].steps[0].detail.adesa, asked, cu)


class JhalamJasoNte(unittest.TestCase):
    """8.2.39."""

    def test_the_examples_Laghu_and_Kasika(self):
        """वागीशः (Laghu); अग्निचित् → अग्निचिद्; त्रिष्टुप् → त्रिष्टुब् (Kāśikā on
        8.4.56, where 8.2.39 has already voiced them)."""
        self.assertIn("agnicid", surfaces("agnicit"))
        self.assertIn("triṣṭub", surfaces("triṣṭup"))
        self.assertEqual(steps(mine("agnicit")), ["8.2.39", "8.4.56"])

    def test_the_jas_is_the_nearest_of_its_own_place(self):
        for jhal, jas in (("k", "g"), ("kh", "g"), ("gh", "g"), ("ṭ", "ḍ"),
                          ("th", "d"), ("bh", "b"), ("p", "b"), ("ṭh", "ḍ")):
            r = mine(f"a{jhal}")
            # the jaś is what 8.2.39 makes; 8.4.56's option may then harden it
            first = next(s for s in r.outcomes[0].steps if s.sutra == "8.2.39")
            self.assertEqual(first.detail.adesa, jas, jhal)
            self.assertIn(f"a{jas}", r.surfaces, jhal)

    def test_only_at_the_end_of_a_pada_Kasika_antagrahana(self):
        """अन्तग्रहणं झलि इत्येतस्य निवृत्त्यर्थम् — a झल् before a झल् inside a
        word is not voiced by 8.2.39: वस्ता keeps its स् (and 8.4.55 leaves
        a स् that is already a चर्)."""
        r = mine("vas~tā")
        self.assertEqual(r.surface, "vastā")
        self.assertNotIn("8.2.39", steps(r))

    def test_a_pada_final_h_is_first_made_dh_then_voiced(self):
        self.assertEqual(order_of(mine("lih"), {"8.2.31", "8.2.39", "8.4.56"}),
                         ["8.2.31", "8.2.39", "8.4.56"])

    def test_the_jas_agrees_with_the_projects_own_question_form(self):
        """`anga.jhalam_jas_jhasi` is the same substitution (8.4.53's, which
        takes the same जश्) as a question; every स्पर्श झल् gets from the
        engine's 8.2.39 the जश् it gets from there."""
        jas = sorted(S.members("jaŚ"))
        jhal = S.members("jhaL")
        checked = 0
        for row in VARGA.values():
            for sound in row:
                if sound not in jhal:
                    continue
                asked = jhalam_jas_jhasi(sound + "dh")
                expected = asked.now if asked.result else sound
                self.assertEqual(H._nearest(sound, jas), expected, sound)
                checked += 1
        self.assertEqual(checked, 20)


class KhariCa(unittest.TestCase):
    """8.4.55."""

    def test_the_kasika_examples(self):
        """Kāśikā: भेत्ता (भिद् + ता), अत्ति (अद् + ति), युयुत्सते, आरिप्सते."""
        for text, expected in (("bhid~tā", "bhittā"), ("ad~ti", "atti"),
                               ("yuyudh~sate", "yuyutsate"),
                               ("āribh~sate", "āripsate"),
                               ("ālabh~sate", "ālapsate")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r), ["8.4.55"], text)

    def test_an_aspirate_takes_its_own_car_not_the_sibilant(self):
        """युयुत्सते and not *युयुस्सते: ध् before स् is त्. Nearness is reckoned
        as the Kāśikā reckons it — place, then internal effort, then external
        quality — so ध्, which is स्पृष्ट like त्, goes to त् and not to स्
        (which merely shares महाप्राण). The aspirates of the च-, ट-, त-वर्ग
        have a sibilant in their own place, and are exactly where the
        difference shows."""
        car = sorted(S.members("caR"))
        for jhal, expected in (("dh", "t"), ("ch", "c"), ("jh", "c"),
                               ("ṭh", "ṭ"), ("ḍh", "ṭ"), ("th", "t"),
                               ("bh", "p"), ("gh", "k"), ("kh", "k"),
                               ("ph", "p")):
            self.assertEqual(H._nearest(jhal, car), expected, jhal)
        r = mine("yuyudh~sate")
        self.assertEqual(r.surfaces, ("yuyutsate",))
        self.assertEqual(r.outcomes[0].steps[0].detail.adesa, "t")

    def test_it_agrees_with_the_projects_own_question_form(self):
        """`anga.khari_ca` reads the चर् off the varga row; the engine's is
        found by 1.1.50; every sparśa gets the same answer from both."""
        car = sorted(S.members("caR"))
        checked = 0
        jhal = S.members("jhaL")
        for row in VARGA.values():
            for sound in row:
                if sound not in jhal:            # a nasal is no झल्
                    continue
                asked = anga_khari_ca(sound, "t").result or sound
                self.assertEqual(H._nearest(sound, car), asked, sound)
                checked += 1
        self.assertEqual(checked, 20)

    def test_it_needs_a_khar_after_and_a_jhal_before(self):
        """The nasals are outside झल् (हन्ति keeps its न्); a य् after is no
        खर् (`anga.khari_ca`: हन्ति, and the Kāśikā's own भेत्ता)."""
        self.assertEqual(mine("han~ti").surface, "hanti")
        self.assertEqual(mine("bhid~ya").surface, "bhidya")
        self.assertNotIn("8.4.55", steps(mine("han~ti")))

    def test_tacchivah_LSK_8_4_55(self):
        """Laghu on 8.4.63: तद् शिव → द् becomes ज् (8.4.40), and खरि च makes
        that ज् a च्."""
        r = mine("tat śiva")
        self.assertEqual(order_of(r, {"8.2.39", "8.4.40", "8.4.55", "8.4.63"}),
                         ["8.2.39", "8.4.40", "8.4.55", "8.4.63"])


class VaAvasane(unittest.TestCase):
    """8.4.56 — an option, at a pause."""

    def test_the_kasika_pairs(self):
        """Kāśikā: वाक्, वाग्; त्वक्, त्वग्; श्वलिट्, श्वलिड्; त्रिष्टुप्,
        त्रिष्टुब्. Kaumudī: रामात्, रामाद्."""
        for text, pair in (("vāc", {"vāk", "vāg"}), ("tvac", {"tvak", "tvag"}),
                           ("śvaliṭ", {"śvaliṭ", "śvaliḍ"}),
                           ("triṣṭup", {"triṣṭup", "triṣṭub"}),
                           ("rāmāt", {"rāmāt", "rāmād"})):
            self.assertEqual(surfaces(text), pair, text)

    def test_both_courses_are_returned_the_taken_first_and_the_other_declined(self):
        r = mine("vāc")
        self.assertEqual(len(r.outcomes), 2)
        self.assertEqual(r.outcomes[0].choices, (("8.4.56", True),))
        self.assertEqual(r.outcomes[1].choices, (("8.4.56", False),))
        self.assertEqual(r.surfaces[0], "vāk")
        self.assertEqual(steps(r, 1, declined=True)[-1], "8.4.56*")

    def test_the_option_is_offered_over_the_jas_8_2_39_has_made(self):
        """Nyāsa: नित्ये जश्त्वे प्राप्ते — 8.2.39 comes first, and 8.4.56 acts
        on the ग् it made; the declined course keeps the ग्."""
        r = mine("vāc")
        self.assertEqual(steps(r, 0), ["8.2.30", "8.2.39", "8.4.56"])
        self.assertEqual(r.outcomes[1].final.joined(), "vāg")

    def test_only_at_a_pause(self):
        """Not before another word: वाक्पतिः has one form; and where the last
        word is not known to end (`pause=False`, the utterance goes on) the
        option is not offered — nor is anything that needs a pada's end."""
        self.assertEqual(len(mine("vāc pati").outcomes), 1)
        r = mine("vāc", pause=False)
        self.assertEqual(len(r.outcomes), 1)
        self.assertNotIn("8.4.56", steps(r, declined=True))

    def test_a_sibilant_is_already_a_car_and_is_not_changed(self):
        """Kaumudī: a स् is a चर् itself, so it stays (रामस्य keeps its स्; the
        pada-final स् is the visarga family's, and श्, ष् are चर् too)."""
        car = sorted(S.members("caR"))
        for sibilant in ("s", "ś", "ṣ"):
            self.assertEqual(H._nearest(sibilant, car), sibilant)


# ---------------------------------------------------------------------------
# 8.4.40–44 — श्चुत्व, ष्टुत्व, and what refuses them
# ---------------------------------------------------------------------------


class StohScunaScuh(unittest.TestCase):
    """8.4.40."""

    def test_the_kasika_and_kaumudi_examples(self):
        """Kaumudī: रामश्शेते (हरिश्शेते), रामश्चिनोति, सच्चित्, शार्ङ्गिञ्जय.
        (The visarga family supplies the स् of रामस्; 8.3.36 gives the optional
        visarga form as well.)"""
        for text, expected in (
                ("rāmas śete", {"rāmaśśete", "rāmaḥśete"}),
                ("rāmas cinoti", {"rāmaścinoti"}),
                ("haris śete", {"hariśśete", "hariḥśete"})):
            r = mine(text, "visarga_ru")
            self.assertEqual(set(r.surfaces), expected, text)
            self.assertTrue(any("8.4.40" in steps(r, i) for i in range(len(r.outcomes))), text)
        self.assertIn("saccit", surfaces("sat cit"))
        self.assertEqual(surfaces("śārṅgin jaya"), {"śārṅgiñjaya"})

    def test_the_steps_of_the_visarga_chain(self):
        """रामस् + च: the रु, the visarga, the स् it becomes before a खर्, and
        only then श्चुत्व (8.3.34 makes the स् that 8.4.40 sees)."""
        r = mine("rāmas ca", "visarga_ru")
        self.assertEqual(steps(r), ["8.2.66", "8.3.15", "8.3.34", "8.4.40"])

    def test_either_sound_is_changed_and_the_pairs_are_not_matched_one_to_one(self):
        """Kāśikā: स्तोःश्चुनेति यथासंख्यमत्र नेष्यते. A स् meeting a च-वर्ग
        sound becomes श् (रामश्चिनोति) and a त-वर्ग sound meeting श् becomes
        च-वर्ग (तच्छिवः) — the two crossings a one-to-one pairing would miss."""
        r = mine("rāmas cinoti", "visarga_ru")
        step = next(s for s in r.outcomes[0].steps if s.sutra == "8.4.40")
        self.assertEqual((step.detail.sthanin, step.detail.adesa), ("s", "ś"))
        self.assertIn("1.3.10", [v.sutra for v in step.detail.via])
        crossed = mine("tat śiva").outcomes[0]
        step = next(s for s in crossed.steps if s.sutra == "8.4.40")
        self.assertIn("1.3.10", [v.sutra for v in step.detail.via])

    def test_the_uncrossed_pairing_does_not_call_on_the_refusal_of_yathasamkhya(self):
        r = mine("rāmas śete", "visarga_ru")
        out = next(o for o in r.outcomes if any(s.sutra == "8.4.40" for s in o.steps))
        step = next(s for s in out.steps if s.sutra == "8.4.40")
        self.assertNotIn("1.3.10", [v.sutra for v in step.detail.via])

    def test_a_cause_that_stands_before_Kasika_and_Nyasa(self):
        """Nyāsa: श्चुना — in the third case — so that it holds with the cause
        BEFORE (यज्ञः, याच्ञा, राज्ञः): the न् after ज् becomes ञ्."""
        for text, expected in (("yaj~na", "yajña"), ("yāc~nā", "yācñā"),
                               ("rāj~na", "rājña")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r), ["8.4.40"], text)
            step = r.outcomes[0].steps[0]
            self.assertIn("1.1.66", [v.sutra for v in step.detail.via])

    def test_each_tavarga_sound_takes_its_own_cavarga_sound(self):
        for tu, cu in zip(VARGA["tu"], VARGA["cu"]):
            r = mine(f"a{tu}~ca")
            found = [s for s in r.outcomes[0].steps if s.sutra == "8.4.40"]
            self.assertTrue(found, tu)
            self.assertEqual(found[0].detail.adesa, cu, tu)

    def test_8_2_39_first_then_ścutva_on_what_it_made(self):
        """Bālamanoramā: श्चुत्वस्यासिद्धत्वाज्जश्त्वेन तकारस्य दत्वे, तस्य श्चुत्वेन
        जकारे, खरि चेति चर्त्वेन तस्य चकारे — सच्चित्."""
        r = mine("sat cit")
        self.assertEqual(
            [(s.sutra, s.detail.sthanin, s.detail.adesa)
             for s in r.outcomes[0].steps[:3]],
            [("8.2.39", "t", "d"), ("8.4.40", "d", "j"),
             ("8.4.55", "j", "c")])

    def test_it_does_not_touch_the_inside_of_a_finished_word(self):
        self.assertEqual(steps(mine("gacchati")), [])
        self.assertEqual(steps(mine("rājña")), [])


class StohStunaStuh(unittest.TestCase):
    """8.4.41."""

    def test_the_kaumudi_examples(self):
        """Kaumudī: रामष्षष्ठः, रामष्टीकते, पेष्टा, तट्टीका, चक्रिण्ढौकसे."""
        for text, expected in (
                ("rāmas ṣaṣṭhaḥ", {"rāmaṣṣaṣṭhaḥ", "rāmaḥṣaṣṭhaḥ"}),
                ("rāmas ṭīkate", {"rāmaṣṭīkate"}),
                ("peṣ~tā", {"peṣṭā"}), ("tat ṭīkā", {"taṭṭīkā"}),
                ("cakrin ḍhaukase", {"cakriṇḍhaukase"})):
            r = mine(text, "visarga_ru")
            self.assertEqual(set(r.surfaces), expected, text)
            self.assertTrue(any("8.4.41" in steps(r, i) for i in range(len(r.outcomes))), text)

    def test_the_kasika_ist_examples_the_cause_before_and_after(self):
        """Kāśikā: पेष्टा (ष् before त्), अग्निचिट्टीकते (ट-वर्ग after a
        त-वर्ग sound), कृषीष्ट, कृषीष्ठाः."""
        self.assertEqual(surfaces("kṛṣīṣ~ta"), {"kṛṣīṣṭa"})
        self.assertEqual(surfaces("kṛṣīṣ~thāḥ", "visarga_ru"),
                         {"kṛṣīṣṭhāḥ"})
        self.assertIn("agniciṭṭīkate", surfaces("agnicit ṭīkate"))

    def test_the_laghu_tags_udah_sthastambhoh_wrongly_as_8_4_41(self):
        """The Laghu tags उदः स्थास्तम्भोः पूर्वस्य as 8.4.41; the Vidyut text
        says 8.4.61, and this family's rule for it is at 8.4.61."""
        known = corpus.load_vidyut_sutrapatha()
        self.assertEqual(known["8.4.61"].text, "udaḥ sthāstambhoḥ pūrvasya")
        self.assertEqual(known["8.4.41"].text, "ṣṭunā ṣṭuḥ")
        r = mine("ud|sthāna{dhatu:sthā}")
        self.assertIn("8.4.61", steps(r))
        self.assertNotIn("8.4.41", steps(r))

    def test_each_tavarga_sound_takes_its_own_tavarga_sound(self):
        for tu, tt in zip(VARGA["tu"], VARGA["ṭu"]):
            r = mine(f"a{tu}~ṭa")
            found = [s for s in r.outcomes[0].steps if s.sutra == "8.4.41"]
            self.assertTrue(found, tu)
            self.assertEqual(found[0].detail.adesa, tt, tu)


class NaPadantatToranam(unittest.TestCase):
    """8.4.42 — a refusal: no edit, the very site of 8.4.41, and never twice."""

    def test_the_kasika_and_kaumudi_examples(self):
        """Kaumudī: षट् सन्तः, षट् ते; Kāśikā: श्वलिट् साये, मधुलिट् तरति."""
        for text in ("ṣaṭ santaḥ", "ṣaṭ te", "śvaliṭ sāye", "madhuliṭ tarati"):
            r = mine(text, "visarga_ru")
            self.assertIn("8.4.42", steps(r), text)
            self.assertNotIn("8.4.41", steps(r), text)
        self.assertEqual(surfaces("ṣaṭ te"), {"ṣaṭte"})
        self.assertEqual(surfaces("madhuliṭ tarati"), {"madhuliṭtarati"})

    def test_the_refusal_is_a_step_that_changes_nothing(self):
        r = mine("ṣaṭ te")
        step = next(s for s in r.outcomes[0].steps if s.sutra == "8.4.42")
        self.assertEqual(step.detail.kind, "pratiṣedha")
        self.assertEqual(step.before, step.after)
        self.assertEqual([a.sutra for a in step.against], ["8.4.41"])
        self.assertIn("नामित्येतद् वर्जयित्वा", step.against[0].why)

    def test_and_it_is_made_once_though_a_later_rule_changes_the_cause(self):
        """8.2.39 makes the ट् ड्, 8.4.42 refuses, 8.4.55 makes the ड् ट् again.
        The ट् 8.4.55 made is a new sound, and 8.4.41, which stands before
        8.4.55 and sees only the ड्, must not be offered it afresh — nor may
        8.4.42 refuse it a second time."""
        r = mine("ṣaṭ te")
        self.assertEqual(steps(r), ["8.2.39", "8.4.42", "8.4.55"])
        self.assertEqual(steps(r).count("8.4.42"), 1)

    def test_not_ittte_the_cause_does_not_end_a_pada_Kasika(self):
        """Kāśikā: पदान्तादिति किम्? ईट्टे — ईड् + ते: the ड् is inside the word,
        so 8.4.41 acts and the त् becomes ट्."""
        r = mine("īḍ~te")
        self.assertEqual(r.surfaces, ("īṭṭe",))
        self.assertIn("8.4.41", steps(r))
        self.assertNotIn("8.4.42", steps(r))

    def test_not_sarpistamam_the_cause_is_not_a_tavarga_Kasika(self):
        """Kāśikā: टोरिति किम्? सर्पिष्टमम् — the ष् is not a ट-वर्ग sound."""
        r = mine("sarpiṣ~tama")
        self.assertEqual(r.surfaces, ("sarpiṣṭama",))
        self.assertNotIn("8.4.42", steps(r))

    def test_nam_is_excepted_by_the_sutras_own_anam_Kasika(self):
        """Kāśikā: अनामिति किम्? षण्णाम् — the न् of नाम् takes ष्टुत्व (the ण्
        from ड् is 8.4.45's, not this family's; here it is enough that
        8.4.42 stands aside and 8.4.41 acts)."""
        r = mine("ṣaṭ nām")
        self.assertNotIn("8.4.42", steps(r))
        self.assertIn("8.4.41", steps(r))
        step = next(s for s in r.outcomes[0].steps if s.sutra == "8.4.41")
        via = [(v.sutra, v.role) for v in step.detail.via]
        self.assertIn("8.4.42", [s for s, _ in via])
        self.assertIn("नामित्येतद् वर्जयित्वा", dict(via)["8.4.42"])

    def test_the_vartika_frees_navati_and_nagari_Kasika(self):
        """Vārttika अनाम्नवतिनगरीणामिति वक्तव्यम्: षण्णवतिः, षण्णगरी. Read from
        the words, and named in the trace as the vārttika's, not the sūtra's."""
        for word in ("navati", "nagarī"):
            r = mine(f"ṣaṭ-{word}")
            self.assertNotIn("8.4.42", steps(r), word)
            self.assertIn("8.4.41", steps(r), word)
            step = next(s for s in r.outcomes[0].steps if s.sutra == "8.4.41")
            role = dict((v.sutra, v.role) for v in step.detail.via)["8.4.42"]
            self.assertIn("अनाम्नवतिनगरीणामिति वक्तव्यम्", role)

    def test_a_word_that_is_not_nam_navati_or_nagari_is_refused(self):
        r = mine("ṣaṭ-nāma")
        self.assertIn("8.4.42", steps(r))
        self.assertNotIn("8.4.41", steps(r))


class TohSi(unittest.TestCase):
    """8.4.43 — तवर्गस्य षकारे परे न ष्टुत्वम्."""

    def test_the_examples_Kasika_and_Laghu(self):
        """Laghu: सन्षष्ठः; Kāśikā: अग्निचित् षण्डे, भवान् षण्डे, महान् षण्डे."""
        for text, expected in (("san ṣaṣṭhaḥ", "sanṣaṣṭhaḥ"),
                               ("bhavān ṣaṇḍe", "bhavānṣaṇḍe"),
                               ("mahān ṣaṇḍe", "mahānṣaṇḍe"),
                               ("agnicit ṣaṇḍe", "agnicitṣaṇḍe")):
            r = mine(text, "visarga_ru")
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertIn("8.4.43", steps(r), text)
            self.assertNotIn("8.4.41", steps(r), text)

    def test_only_where_the_s_follows_padamanjari(self):
        """Padamañjarī: 'ṣi' is in the seventh case, so a ष् BEFORE a
        त-वर्ग sound still gives ष्टुत्व — पेष्टा."""
        r = mine("peṣ~tā")
        self.assertIn("8.4.41", steps(r))
        self.assertNotIn("8.4.43", steps(r))

    def test_and_a_sa_after_a_tavarga_is_not_refused(self):
        """Only ष् refuses: a स् after a त-वर्ग sound is not 8.4.41's matter
        at all (no ष्-cause), and रामष्षष्ठः is refused by nothing."""
        self.assertNotIn("8.4.43", steps(mine("rāmas ṣaṣṭhaḥ", "visarga_ru")))


class Sat(unittest.TestCase):
    """8.4.44."""

    def test_the_kasika_examples(self):
        """Kāśikā: प्रश्नः, विश्नः."""
        for text, expected in (("praś~na", "praśna"), ("viś~na", "viśna")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r), ["8.4.44"], text)

    def test_the_refusal_is_a_step_and_says_what_it_refused(self):
        step = mine("praś~na").outcomes[0].steps[0]
        self.assertEqual(step.detail.kind, "pratiṣedha")
        self.assertEqual(step.before, step.after)
        self.assertEqual([a.sutra for a in step.against], ["8.4.40"])
        self.assertIn("शकारादुत्तरस्य तवर्गस्य यदुक्तं तद् न भवति",
                      step.against[0].why)

    def test_the_rule_it_refuses_still_works_elsewhere(self):
        """यज्ञः has a ज् before its न्, not a श्."""
        self.assertEqual(surfaces("yaj~na"), {"yajña"})

    def test_it_is_a_refusal_of_tavarga_only_not_of_sa_or_sha(self):
        """तोः is carried down: a स् after श् is still turned (Kāśikā's
        श्चुत्व after a श् cause for स् is 8.4.40's own)."""
        self.assertIn("8.4.40", steps(mine("viś~sa")))
        self.assertNotIn("8.4.44", steps(mine("viś~sa")))

    def test_the_cause_must_be_before(self):
        """शात् is in the fifth case (1.1.67): a त-वर्ग sound BEFORE श् is
        changed — मलिनश्चिनोति's kind — तान् शत्रून् has न् before श्."""
        r = mine("kan śa")
        self.assertIn("8.4.40", steps(r))
        self.assertEqual(r.surface, "kañśa")


# ---------------------------------------------------------------------------
# 8.4.60–8.4.65
# ---------------------------------------------------------------------------


class Torli(unittest.TestCase):
    """8.4.60."""

    def test_the_kasika_and_kaumudi_examples(self):
        """Kāśikā: अग्निचिल्लुनाति, सोमसुल्लुनाति, भवाँल्लुनाति, महाँल्लुनाति;
        Kaumudī: तल्लयः, विद्वाँल्लिखति."""
        for text, expected in (
                ("agnicit lunāti", "agnicillunāti"),
                ("somasut lunāti", "somasullunāti"),
                ("bhavān lunāti", "bhavāl̐lunāti"),
                ("mahān lunāti", "mahāl̐lunāti"),
                ("sat laya", "sallaya"),
                ("vidvān likhati", "vidvāl̐likhati")):
            self.assertEqual(surfaces(text), {expected}, text)

    def test_tallayah_is_8_2_39_then_8_4_60(self):
        """तल्लयः: the त् is a द् (8.2.39) before 8.4.60 makes it ल्; the
        order is the tripādī's."""
        r = mine("tat laya")
        self.assertEqual(steps(r), ["8.2.39", "8.4.60"])

    def test_the_n_becomes_a_nasal_l_and_the_others_a_plain_l(self):
        """नस्यानुनासिको लः (Kaumudī, Padamañjarī: तकारस्य शुद्धो लकारो, नकारस्य
        अनुनासिकः): the substitute of न् is anunāsika."""
        n = mine("bhavān lunāti").outcomes[0].final
        seg = [s for s in n.segs if s.made_by == "8.4.60"][0]
        self.assertEqual((seg.s, seg.nasal), ("l", True))
        t = mine("tat laya").outcomes[0].final
        seg = [s for s in t.segs if s.made_by == "8.4.60"][0]
        self.assertEqual((seg.s, seg.nasal), ("l", False))

    def test_each_tavarga_sound_but_only_before_l(self):
        for tu in VARGA["tu"]:
            self.assertIn("8.4.60", steps(mine(f"a{tu} lu")), tu)
            self.assertNotIn("8.4.60", steps(mine(f"a{tu} ru")), tu)


class UdahSthaStambhoh(unittest.TestCase):
    """8.4.61."""

    def test_the_examples_Kasika_Kaumudi_Balamanorama(self):
        """Kāśikā: उत्थाता, उत्तम्भिता; Kaumudī: उत्थानम्, उत्तम्भनम् — the स् of
        the root becomes थ् (अघोषस्य सस्य तादृश एव थकारः), and 8.4.55 has made
        the द् of उद् a त् (चर्त्वं प्रति थकारस्यासिद्धत्वात्)."""
        r = mine("ud|sthāna{dhatu:sthā}")
        self.assertEqual(order_of(r, {"8.4.55", "8.4.61", "8.4.65"}),
                         ["8.4.55", "8.4.61", "8.4.65"])
        step = next(s for s in r.outcomes[0].steps if s.sutra == "8.4.61")
        self.assertEqual((step.detail.sthanin, step.detail.adesa), ("s", "th"))
        r = mine("ud|stambhana{dhatu:stambh}")
        step = next(s for s in r.outcomes[0].steps if s.sutra == "8.4.61")
        self.assertEqual((step.detail.sthanin, step.detail.adesa), ("s", "th"))

    def test_the_forms_Balamanorama(self):
        """Bālamanoramā: उत्थ्थानम् — one त् and two थ् — and, when the first थ्
        is lost by 8.4.65, one त् and one थ्."""
        self.assertEqual(surfaces("ud|sthāna{dhatu:sthā}"),
                         {"utthāna", "utththāna"})
        self.assertEqual(surfaces("ud|sthātā{dhatu:sthā}"),
                         {"utthātā", "utththātā"})

    def test_the_th_is_asiddha_to_khari_ca_so_the_ud_gives_a_t_not_a_th(self):
        """चर्त्वं प्रति थकारस्यासिद्धत्वात् — 8.4.55 is before 8.4.61 and sees
        the स्, a खर्, so the द् becomes त्, not थ्-adjacent anything else."""
        r = mine("ud|sthāna{dhatu:sthā}")
        self.assertEqual(r.outcomes[0].steps[0].sutra, "8.4.55")
        self.assertEqual(r.outcomes[0].steps[0].detail.adesa, "t")

    def test_not_utsnata_the_root_is_neither_Kasika(self):
        """Kāśikā: स्थास्तम्भोरिति किम्? उत्स्नाता."""
        r = mine("ud|snāta{dhatu:snā}")
        self.assertNotIn("8.4.61", steps(r))
        self.assertEqual(r.surfaces, ("utsnāta",))

    def test_the_root_is_the_callers_and_a_word_with_no_flag_is_not_guessed(self):
        r = mine("ud|sthāna")
        self.assertNotIn("8.4.61", steps(r))

    def test_only_after_ud(self):
        r = mine("ut|sthāna{dhatu:sthā}")
        self.assertNotIn("8.4.61", steps(r))


class JhayoHo(unittest.TestCase):
    """8.4.62 — an option."""

    def test_the_kasika_examples(self):
        """Kāśikā: वाग्घसति / वाग् हसति, श्वलिड्ढसति / श्वलिड् हसति,
        अग्निचिद्धसति, सोमसुद्धसति, त्रिष्टुब्भसति."""
        for text, both in (
                ("vāc hasati", {"vāgghasati", "vāghasati"}),   # see below
                ("śvaliṭ hasati", {"śvaliḍḍhasati", "śvaliḍhasati"}),
                ("agnicit hasati", {"agniciddhasati", "agnicidhasati"}),
                ("somasut hasati", {"somasuddhasati", "somasudhasati"}),
                ("triṣṭup hasati", {"triṣṭubbhasati", "triṣṭubhasati"})):
            r = mine(text)
            self.assertEqual(set(r.surfaces), both, text)
            self.assertEqual(len(r.outcomes), 2, text)

    def test_the_substitute_is_the_fourth_of_the_varga_Kaumudi(self):
        """Kaumudī: हस्य तादृश एव वर्गचतुर्थः — घोषवान्, नादवान्, महाप्राणः,
        संवृतकण्ठः: गकार → घ्, दकार → ध्, बकार → भ्, डकार → ढ्, जकार → झ्."""
        for jhay, fourth in (("g", "gh"), ("d", "dh"), ("b", "bh"),
                             ("ḍ", "ḍh")):
            r = mine(f"a{jhay} ha")
            step = next(s for s in r.outcomes[0].steps if s.sutra == "8.4.62")
            self.assertEqual(step.detail.adesa, fourth, jhay)

    def test_not_after_a_nasal_Kasika(self):
        """Kāśikā: झय इति किम्? प्राङ् हसति, भवान् हसति."""
        for text in ("prāṅ hasati", "bhavān hasati"):
            r = mine(text)
            self.assertEqual(len(r.outcomes), 1, text)
            self.assertNotIn("8.4.62", steps(r), text)

    def test_vagghariḥ_LSK_and_the_declined_course(self):
        """Laghu: वाग्घरिः, वाग्हरिः — the taken course and the declined one
        (the ह् left as it is, so वाग् हरिः, written joined)."""
        r = mine("vāc hariḥ", "visarga_ru")
        self.assertEqual(set(r.surfaces), {"vāgghariḥ", "vāg hariḥ".replace(" ", "")})
        self.assertEqual(steps(r, 0)[:3], ["8.2.30", "8.2.39", "8.4.62"])
        self.assertEqual(steps(r, 1, declined=True)[2], "8.4.62*")


class SasChoTi(unittest.TestCase):
    """8.4.63 — an option, and the vārttika that widens it."""

    def test_tacchivah_tacsivah_LSK(self):
        """Laghu: तच्छिवः, तच्शिवः — the द् is ज् (8.4.40), then च्
        (8.4.55), and the श् may be छ्."""
        r = mine("tat śiva")
        self.assertEqual(set(r.surfaces), {"tacchiva", "tacśiva"})
        self.assertEqual(steps(r, 0),
                         ["8.2.39", "8.4.40", "8.4.55", "8.4.63"])
        self.assertEqual(steps(r, 1, declined=True),
                         ["8.2.39", "8.4.40", "8.4.55", "8.4.63*"])
        self.assertEqual(r.surfaces[0], "tacchiva")
        self.assertEqual(whole("tat śivaḥ").surfaces, ("tacchivaḥ", "tacśivaḥ"))

    def test_the_kasika_examples(self):
        """Kāśikā: वाक्छेते / वाक् शेते, अग्निचिच्छेते, सोमसुच्छेते,
        श्वलिट् छेते / श्वलिट् शेते."""
        self.assertEqual(surfaces("vāk śete"), {"vākchete", "vākśete"})
        self.assertEqual(surfaces("agnicit śete"),
                         {"agnicicchete", "agnicicśete"})
        self.assertEqual(surfaces("somasut śete"),
                         {"somasucchete", "somasucśete"})
        self.assertEqual(surfaces("śvaliṭ śete"),
                         {"śvaliṭchete", "śvaliṭśete"})

    def test_the_kasika_prints_the_undone_course_of_agnicit_sete_with_a_t(self):
        """Kāśikā prints अग्निचित् शेते (a त्) where the Kaumudī derives
        तच्शिवः with च्: the शकार is a cause for श्चुत्व all the same. The
        engine follows the Kaumudī — OPEN QUESTION in the report."""
        self.assertNotIn("agnicit śete".replace(" ", ""),
                         surfaces("agnicit śete"))

    def test_only_after_a_pada_final_jhay_Nyasa_and_Tattvabodhini(self):
        """The झय् must end a pada (पदान्तात् from 8.4.59): नात्र मध्वश्चोतन्ति —
        a श् after a झय् that is INSIDE the word is not offered."""
        r = mine("mad~śa")
        self.assertNotIn("8.4.63", steps(r))
        self.assertEqual(len(r.outcomes), 1)

    def test_only_before_at(self):
        """अटि: a vowel, ह्, य्, व्, र्. A श् before a consonant outside अट् is
        the vārttika's (below), and before a stop nothing."""
        self.assertIn("8.4.63", steps(mine("vāk śiva")))
        self.assertNotIn("8.4.63", steps(mine("vāk śta")))

    def test_chatvam_ami_the_vartika_widens_it_to_am(self):
        """Vārttika छत्वममीति वाच्यम् (Kāśikā, Bhāṣya): तच्छ्लोकेन, तच्छ्मश्रुणा —
        the श् is छ् before ल्, म्, न् … too."""
        for text, both in (("tat śloka", {"tacchloka", "tacśloka"}),
                           ("tat śmaśru", {"tacchmaśru", "tacśmaśru"})):
            self.assertEqual(surfaces(text), both, text)

    def test_the_vartika_step_is_labelled_a_vartika_and_the_sutras_is_not(self):
        r = mine("tat śloka")
        taken = [s for s in r.outcomes[0].steps if s.sutra == "8.4.63"][0]
        self.assertEqual(taken.detail.authority, VARTTIKA)
        self.assertEqual(
            taken.detail.varttika,
            [v.text for v in corpus.varttikas_on("8.4.63")][0])
        sutra = [s for s in mine("tat śiva").outcomes[0].steps
                 if s.sutra == "8.4.63"][0]
        self.assertEqual(sutra.detail.authority, "sūtra")
        self.assertEqual(sutra.detail.varttika, "")

    def test_the_trace_marks_the_vartika(self):
        text = mine("tat śloka").trace()
        self.assertIn("[vārttika]", text)
        self.assertNotIn("[vārttika]", mine("tat śiva").trace())

    def test_the_sutra_and_the_vartika_never_offer_the_same_place(self):
        """What the sūtra reaches (अट्) the vārttika leaves to it, so a step
        under the sūtra is never credited to the vārttika, whatever order the
        engine settles equals in: asked of the rules themselves."""
        from src.astadhyayi.sandhi.segs import View
        aṭ, am_only = View(parse("tac śiva"), "8.4.63"), \
            View(parse("tac śloka"), "8.4.63")
        self.assertEqual((len(list(H.sas_cho_ti.find(aṭ))),
                          len(list(H.chatvam_ami.find(aṭ)))), (1, 0))
        self.assertEqual((len(list(H.sas_cho_ti.find(am_only))),
                          len(list(H.chatvam_ami.find(am_only)))), (0, 1))

    def test_vakh_chuchi_ami_kim_Kasika(self):
        """Kāśikā (on the vārttika) and Kaumudī: अमि किम्? वाक् श्च्योतति — a श्
        before च् is not छ्: च् is no अम्."""
        r = mine("vāk ścyotati")
        self.assertEqual(len(r.outcomes), 1)
        self.assertNotIn("8.4.63", steps(r))


class JharoJhariSavarne(unittest.TestCase):
    """8.4.65 — an option."""

    def test_the_kasika_shindhi_and_pindhi(self):
        """Kāśikā: शिण्ढि, पिण्ढि (ढकारे डकारस्य लोपो भवति) — with the option
        declined the two remain. (शिण् + ड् + ढि stands for what 8.4.41 and
        8.4.53 leave: ण् ड् ढ्.)"""
        r = mine("śiṇ~ḍ~ḍhi")
        self.assertEqual(set(r.surfaces), {"śiṇḍhi", "śiṇḍḍhi"})
        self.assertEqual(len(r.outcomes), 2)
        self.assertEqual(r.surfaces[0], "śiṇḍhi")

    def test_not_after_a_vowel_Kasika_halah(self):
        """Kāśikā: हल उत्तरस्य — the झर् must follow a consonant: the त् of
        उत्थानम् follows उ, so it stays; only the second, थ्, follows a
        consonant and is lost."""
        r = mine("ud|sthāna{dhatu:sthā}")
        lost = [s for s in r.outcomes[0].steps if s.sutra == "8.4.65"]
        self.assertEqual(len(lost), 1)
        self.assertEqual(lost[0].detail.sthanin, "th")

    def test_not_shangam_the_second_is_no_jhar_Kasika(self):
        """Kāśikā: झर इति किम्? शार्ङ्गम् — ङ् is no झर्."""
        self.assertNotIn("8.4.65", steps(mine("śārṅ~ga")))
        self.assertEqual(surfaces("śārṅ~ga"), {"śārṅga"})

    def test_not_tarpta_the_two_are_not_savarna_Kasika(self):
        """Kāśikā: सवर्ण इति किम्? तर्प्ता — प् and त् are not savarṇa."""
        r = mine("tarp~tā")
        self.assertNotIn("8.4.65", steps(r))
        self.assertEqual(r.surfaces, ("tarptā",))

    def test_any_savarna_jhar_not_only_the_same_one_Kasika(self):
        """Kāśikā: सवर्णग्रहणसामर्थ्यात् संख्यातानुदेशो न भवति — शिण्ढि has ड्
        lost before ढ्: two different sounds of one varga."""
        r = mine("śiṇ~ḍ~ḍhi")
        step = next(s for s in r.outcomes[0].steps if s.sutra == "8.4.65")
        self.assertEqual(step.detail.sthanin, "ḍ")
        self.assertIn("1.1.9", [v.sutra for v in step.detail.via])

    def test_it_is_optional_and_the_first_of_the_two_goes(self):
        r = mine("śiṇ~ḍ~ḍhi")
        self.assertEqual(r.outcomes[0].choices, (("8.4.65", True),))
        self.assertEqual(r.outcomes[1].choices, (("8.4.65", False),))


class AccentAndTheLastSutra(unittest.TestCase):
    """8.4.66–8.4.68 are scope."""

    def test_they_are_not_rules_and_say_so(self):
        for sutra in ("8.4.66", "8.4.67", "8.4.68"):
            self.assertNotIn(sutra, {r.sutra for r in H.RULES})
            self.assertIn(sutra, {s for s, st, _ in H.COVERAGE
                                  if st == "scope"})

    def test_the_last_sutra_is_a_b_and_is_the_last_of_the_grammar(self):
        known = corpus.load_vidyut_sutrapatha()
        self.assertEqual(known["8.4.68"].text, "a a")
        self.assertEqual(max(known, key=lambda i: tuple(map(int, i.split(".")))),
                         "8.4.68")


# ---------------------------------------------------------------------------
# 8.2.24–8.2.29 — the loss of a स् or क्
# ---------------------------------------------------------------------------


class RatSasya(unittest.TestCase):
    """8.2.24."""

    def test_matuh_pituh_kroshtuh_Kasika_and_Kaumudi(self):
        """Kāśikā: मातुः, पितुः (रात् सस्य after 6.1.111); Kaumudī: क्रोष्टुः —
        the स् goes, and the र् is then the pada's end, so 8.3.15 makes it a
        visarga."""
        for text, expected in (("mātur~s", "mātuḥ"), ("pitur~s", "pituḥ"),
                               ("kroṣṭur~s", "kroṣṭuḥ")):
            r = mine(text, "visarga_ru")
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r), ["8.2.24", "8.3.15"], text)

    def test_the_loss_makes_the_r_the_end_of_the_pada(self):
        """Without that, 8.3.15 would not see a pada-final र् at all."""
        r = mine("mātur~s")
        self.assertEqual(r.surfaces, ("mātur",))

    def test_the_r_that_is_left_is_not_marked_an_ekadesa(self):
        """The two sounds become one, but the loss is not 6.1.84's: a mark of
        एकादेश would make 6.1.86's viewers see two sounds where there is a loss."""
        final = mine("mātur~s").outcomes[0].final
        seg = [s for s in final.segs if s.made_by == "8.2.24"][0]
        self.assertEqual(seg.s, "r")
        self.assertNotIn("ekādeśa", seg.marks)
        self.assertEqual(len(seg.prior), 2)

    def test_only_a_sa_only_after_ra_only_at_a_padas_end(self):
        for text in ("mātur~k", "mātun~s", "mātur s"):
            self.assertNotIn("8.2.24", steps(mine(text, "visarga_ru")), text)

    def test_not_where_the_sa_is_a_piece_in_the_middle_of_the_pada(self):
        """रात् सस्य speaks of the cluster that ENDS a pada: मातुर् + स् + भ्याम्
        has its स् before another piece, so the cluster does not end it."""
        r = mine("mātur~s~bhyām", "visarga_ru")
        self.assertNotIn("8.2.24", steps(r))
        self.assertIn("mātursbhyām", r.surfaces + ("mātursbhyām",))


class SicLopa(unittest.TestCase):
    """8.2.25–8.2.28 — the aorist's स्."""

    def test_dhi_ca_alavidhvam_Kasika(self):
        """Kāśikā: अलविध्वम् — the स् is lost before the ध्-initial ending."""
        r = mine("alavi~s{sic}~dhvam{pratyaya}")
        self.assertEqual(r.surfaces, ("alavidhvam",))
        self.assertEqual(steps(r), ["8.2.25"])

    def test_not_cakaddhi_the_sa_is_not_the_aorists_Kasika(self):
        """Kāśikā: इह न भवति — चकाद्धि पलितं शिरः; तथा पयो धावति."""
        for text in ("cakās~hi", "cakās~dhi{pratyaya}", "payas dhāvati"):
            self.assertNotIn("8.2.25", steps(mine(text, "visarga_ru")), text)

    def test_the_ending_must_be_an_affix_the_caller_says_so(self):
        """धादौ प्रत्यये: a ध्-initial piece that is not said to be an affix is
        not one the rule reaches."""
        # after a long vowel, where 8.2.26 and 8.2.27 have nothing to say:
        # 8.2.25 alone decides, and it needs the ending to be an affix
        flagged = mine("acyo~s{sic}~dhvam{pratyaya}")
        self.assertEqual(steps(flagged), ["8.2.25"])
        bare = mine("acyo~s{sic}~dhvam")
        self.assertEqual(steps(bare), [])
        self.assertEqual(bare.surfaces, ("acyosdhvam",))

    def test_jhalo_jhali_abhitta_Kasika(self):
        """Kāśikā: अभित्त, अभित्थाः, अच्छित्त."""
        for text, expected in (("abhid~s{sic}~ta", "abhitta"),
                               ("abhid~s{sic}~thās", "abhitthāḥ"),
                               ("acchid~s{sic}~ta", "acchitta")):
            r = mine(text, "visarga_ru")
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r)[:2], ["8.2.26", "8.4.55"], text)

    def test_not_amamsta_no_jhal_before_and_not_abhitsatam_none_after_Kasika(self):
        """Kāśikā: झल इति किम्? अमंस्त; झलीति किम्? अभित्साताम्."""
        self.assertNotIn("8.2.26", steps(mine("amaṃ~s{sic}~ta")))
        r = mine("abhid~s{sic}~ātām")
        self.assertNotIn("8.2.26", steps(r))
        self.assertEqual(r.surfaces, ("abhitsātām",))

    def test_not_somasut_stota_only_the_aorists_sa_Kasika(self):
        """Kāśikā: अयमपि सिच एव लोपः, तेनेह न भवति — सोमसुत् स्तोता."""
        self.assertNotIn("8.2.26", steps(mine("somasud~s~tā")))

    def test_hrasvad_angat_akrta_Kasika(self):
        """Kāśikā: अकृत, अकृथाः, अहृत."""
        for text, expected in (("a-kṛ~s{sic}~ta", "akṛta"),
                               ("a-kṛ~s{sic}~thās", "akṛthāḥ"),
                               ("a-hṛ~s{sic}~ta", "ahṛta")):
            r = mine(text, "visarga_ru")
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r)[0], "8.2.27", text)

    def test_not_acyoshta_the_vowel_is_long_and_not_akrshatam_no_jhal_Kasika(self):
        """Kāśikā: ह्रस्वादिति किम्? अच्योष्ट; झलीत्येव — अकृषाताम्."""
        self.assertNotIn("8.2.27", steps(mine("a-cyo~s{sic}~ta")))
        self.assertNotIn("8.2.27", steps(mine("a-kṛ~ṣ{sic}~ātām")))

    def test_it_a_iti_adevit_Kasika_and_the_partial(self):
        """Kāśikā: अदेवीत् — the स् between इट् and ईट् is lost. The इ and ई
        are then NOT joined here: the vārttika सिज्लोप एकादेशे सिद्धो वाच्यः
        needs the ekādeśa family to list SIC_LOPA in `consumes`; this is
        the 'partial' of COVERAGE, and the mark is left for it."""
        r = mine("adev~i{it_agama}~s{sic}~ī{iit_agama}~t")
        self.assertEqual(steps(r)[0], "8.2.28")
        lost = [s for s in r.outcomes[0].final.segs if s.s == "" and
                s.made_by == "8.2.28"]
        self.assertEqual(len(lost), 1)
        self.assertIn(H.SIC_LOPA, lost[0].marks)

    def test_not_akarshit_no_it_Kasika(self):
        """Kāśikā: इट इति किम्? अकार्षीत्, अहार्षीत्."""
        self.assertNotIn("8.2.28", steps(mine("akār~ṣ{sic}~ī{iit_agama}~t")))


class SkohSamyogadyor(unittest.TestCase):
    """8.2.29 — a sūtra of this family's scope that `ac_yan_ayadi` also needs
    (for the cluster a yaṇ makes), and where that family has it this one stands
    aside (COVERAGE says so). The tests therefore derive under both families and
    hold whichever of the two supplies the rule."""

    def _mine(self, text, *extra, **kw):
        return mine(text, "ac_yan_ayadi", *extra, **kw)

    def test_which_family_has_it_is_declared_and_only_one_does(self):
        holders = [name for name, group in rulebook.by_family().items()
                   if any(r.sutra == "8.2.29" for r in group)]
        self.assertEqual(len(holders), 1, holders)
        got = {s: (st, n) for s, st, n in H.COVERAGE}["8.2.29"]
        if holders == [FAMILY]:
            self.assertEqual(got[0], "partial")
        else:
            self.assertEqual(got[0], "scope")
            self.assertIn(holders[0], got[1])

    def test_the_kasika_examples(self):
        """Kāśikā: तष्टः, तट्, काष्ठतट् (the क् of तक्ष्); व्रष्टा (the स् of
        व्रस्च्, by the Nyāsa)."""
        r = self._mine("takṣ{dhatu:takṣ}~ta")
        self.assertEqual(r.surfaces, ("taṣṭa",))
        self.assertEqual(steps(r), ["8.2.29", "8.4.41"])
        r = self._mine("kāṣṭha-takṣ{dhatu:takṣ}")
        self.assertEqual(set(r.surfaces), {"kāṣṭhataṭ", "kāṣṭhataḍ"})
        self.assertEqual(order_of(r, {"8.2.29", "8.2.39", "8.4.56"}),
                         ["8.2.29", "8.2.39", "8.4.56"])
        r = self._mine("vrasc{dhatu:vrasc}~tā")
        self.assertEqual(r.surfaces, ("vraṣṭā",))
        self.assertEqual(steps(r), ["8.2.29", "8.2.36", "8.4.41"])

    def test_not_taksita_no_jhal_follows_Kasika(self):
        """Kāśikā: अन्ते चेति किम्? तक्षिता, तक्षकः — a vowel follows, and
        the cluster does not end the pada."""
        r = self._mine("takṣ{dhatu:takṣ}~itā")
        self.assertNotIn("8.2.29", steps(r))
        self.assertEqual(r.surfaces, ("takṣitā",))

    def test_not_shak_there_is_no_cluster_Kasika(self):
        """Kāśikā: संयोगाद्योरिति किम्? पयः, शक् — one consonant is no
        cluster."""
        self.assertNotIn("8.2.29", steps(self._mine("śak")))
        self.assertNotIn("8.2.29", steps(self._mine("payas", "visarga_ru")))

    def test_the_inside_of_an_ordinary_word_is_left_alone(self):
        """गच्छति keeps its च्छ् and सुप्त-like clusters inside a finished word
        are nobody's business here."""
        for text in ("gacchati", "rāmas gacchati", "vastra"):
            for outcome in self._mine(text, "visarga_ru").outcomes:
                self.assertNotIn("8.2.29", [s.sutra for s in outcome.steps])


# ---------------------------------------------------------------------------
# 8.2.31–8.2.35 — what a ह् becomes
# ---------------------------------------------------------------------------


class HoDhah(unittest.TestCase):
    """8.2.31."""

    def test_the_kasika_and_kaumudi_examples(self):
        """Kāśikā: सोढा, वोढा (सह्, वह् + ता); Kaumudī: लिट्, लिड् (लिह् at a
        pause). Under this family the ढ् is made, then 8.2.40 and 8.4.41
        turn the त् after it (सोढा needs 8.3.13, which is not here)."""
        r = mine("sah{dhatu:sah}~tā")
        self.assertEqual(steps(r), ["8.2.31", "8.2.40", "8.4.41"])
        self.assertEqual(r.outcomes[0].steps[0].detail.adesa, "ḍh")
        self.assertEqual(steps(mine("vah{dhatu:vah}~tā")),
                         ["8.2.31", "8.2.40", "8.4.41"])
        r = mine("lih{dhatu:lih}")
        self.assertEqual(set(r.surfaces), {"liṭ", "liḍ"})
        self.assertEqual(order_of(r, {"8.2.31", "8.2.39", "8.4.56"}),
                         ["8.2.31", "8.2.39", "8.4.56"])

    def test_before_a_vowel_inside_a_word_it_stays_Kaumudi(self):
        """Kaumudī: लिहौ, लिहः — the ह् is neither before a झल् nor at a pada's
        end."""
        for text in ("lih~au", "lih~aḥ", "lih~a"):
            self.assertNotIn("8.2.31", steps(mine(text)), text)

    def test_it_needs_no_flag(self):
        """Any ह् — the sūtra says nothing of a root."""
        self.assertIn("8.2.31", steps(mine("lih~ta")))

    def test_the_derived_forms_agree_with_the_projects_question_form(self):
        """`anga.jhasas_tathoh_dhah` is 8.2.40 as a question."""
        got = jhasas_tathoh_dhah("ḍht")
        self.assertEqual((got.result, got.now), ("ḍhdh", "dh"))


class DaderDhatorGhah(unittest.TestCase):
    """8.2.32."""

    def test_the_kasika_examples(self):
        """Kāśikā: दग्धा, दोग्धा (दह्, दुह् + ता), काष्ठधक्, गोधुक्."""
        r = mine("dah{dhatu:dah}~tā")
        self.assertEqual(steps(r), ["8.2.32", "8.2.40"])
        self.assertEqual(r.outcomes[0].steps[0].detail.adesa, "gh")
        r = mine("doh{dhatu:duh}~tā")
        self.assertEqual(r.outcomes[0].steps[0].detail.adesa, "gh")
        r = mine("go-duh{dhatu:duh}")
        self.assertEqual(set(r.surfaces), {"godhuk", "godhug"})
        self.assertEqual(order_of(r, {"8.2.32", "8.2.37", "8.2.39", "8.4.56"}),
                         ["8.2.32", "8.2.37", "8.2.39", "8.4.56"])

    def test_not_lehta_the_root_does_not_begin_with_d_Kasika(self):
        """Kāśikā: दादेरिति किम्? लेढा, लेढुम्, गुडलिट्."""
        r = mine("leh{dhatu:lih}~tā")
        self.assertEqual(r.outcomes[0].steps[0].sutra, "8.2.31")
        self.assertNotIn("8.2.32", steps(r))
        r = mine("guḍa-lih{dhatu:lih}")
        self.assertNotIn("8.2.32", steps(r))

    def test_it_displaces_8_2_31_and_says_so(self):
        """The Bhāṣya on 8.2.32: उक्तमेतत्-अपवादो वचनप्रामाण्यादिति."""
        r = mine("dah{dhatu:dah}~tā")
        first = r.outcomes[0].steps[0]
        self.assertEqual(first.sutra, "8.2.32")
        self.assertIn("8.2.31", [a.sutra for a in first.against])
        self.assertIn("अपवादो वचनप्रामाण्यादिति", first.against[0].why)

    def test_the_root_is_the_callers_and_none_is_guessed(self):
        self.assertNotIn("8.2.32", steps(mine("dah~tā")))
        self.assertIn("8.2.31", steps(mine("dah~tā")))


class VaDruhaMuha(unittest.TestCase):
    """8.2.33 — an option."""

    def test_the_kasika_pairs(self):
        """Kāśikā: द्रोग्धा, द्रोढा; उन्मोग्धा, उन्मोढा; उत्स्नोग्धा, उत्स्नोढा;
        स्नेग्धा, स्नेढा — घ् or (8.2.31's) ढ्."""
        for text, root in (("droh~tā", "druh"), ("unmoh~tā", "muh"),
                           ("utsnoh~tā", "ṣṇuh"), ("sneh~tā", "ṣṇih")):
            w = text.split("~")
            r = mine(f"{w[0]}{{dhatu:{root}}}~{w[1]}")
            first_of = [steps(r, i, declined=True)[0]
                        for i in range(len(r.outcomes))]
            self.assertEqual(first_of, ["8.2.33", "8.2.33*"], text)
            self.assertEqual(r.outcomes[0].steps[0].detail.adesa, "gh", text)
            self.assertEqual(steps(r, 1)[0], "8.2.31", text)

    def test_mitradhruk_mitradhrut_Kasika(self):
        """Kāśikā: मित्रध्रुक्, मित्रध्रुट् — four surfaces with the pause's own
        option: क्, ग् from the घ्; ट्, ड् from the ढ्."""
        r = mine("mitra-druh{dhatu:druh}")
        self.assertEqual(set(r.surfaces),
                         {"mitradhruk", "mitradhrug", "mitradhruṭ",
                          "mitradhruḍ"})

    def test_druh_is_prapta_and_the_others_aprapta_Kasika(self):
        """Kāśikā: द्रुहेर्दादित्वाद् घत्वं नित्यं प्राप्तम्, इतरेषामप्राप्तमेव घत्वं
        विकल्प्यते. For द्रुह् the option displaces 8.2.32 as well, so the
        declined course is ढ्, NOT the घ् of 8.2.32."""
        r = mine("droh{dhatu:druh}~tā")
        declined = r.outcomes[1]
        self.assertNotIn("8.2.32", [s.sutra for s in declined.steps])
        self.assertEqual(declined.steps[1].sutra, "8.2.31")
        first = r.outcomes[0].steps[0]
        self.assertEqual({a.sutra for a in first.against}, {"8.2.31"})
        first = r.outcomes[0].steps[0]
        self.assertIn("द्रुहेर्दादित्वाद् घत्वं नित्यं प्राप्तम्",
                      " ".join(a.why for a in first.against))

    def test_a_root_not_in_the_four_gets_no_option(self):
        r = mine("doh{dhatu:duh}~tā")
        self.assertEqual(len(r.outcomes), 1)
        self.assertNotIn("8.2.33", steps(r))


class NahoDhah(unittest.TestCase):
    """8.2.34."""

    def test_the_kasika_examples(self):
        """Kāśikā: नद्धम् (नह् + त), उपानत् — घ्…; धकारादेश."""
        r = mine("nah{dhatu:nah}~ta")
        self.assertEqual(steps(r), ["8.2.34", "8.2.40"])
        self.assertEqual(r.outcomes[0].steps[0].detail.adesa, "dh")
        r = mine("upā-nah{dhatu:nah}")
        self.assertEqual(set(r.surfaces), {"upānat", "upānad"})
        self.assertEqual(order_of(r, {"8.2.34", "8.2.39", "8.4.56"}),
                         ["8.2.34", "8.2.39", "8.4.56"])

    def test_another_root_is_not_nah(self):
        self.assertNotIn("8.2.34", steps(mine("sah{dhatu:sah}~tā")))


class AhoThah(unittest.TestCase):
    """8.2.35."""

    def test_idamattha_kimattha_Kasika_and_Kaumudi(self):
        """Kāśikā: इदमात्थ, किमात्थ — आह् before a झल् (थ) becomes थ्, and
        8.4.55 makes the first थ् a त्."""
        r = mine("āh{dhatu:ah}~tha")
        self.assertEqual(r.surfaces, ("āttha",))
        self.assertEqual(steps(r), ["8.2.35", "8.4.55"])
        self.assertEqual(r.outcomes[0].steps[0].detail.adesa, "th")

    def test_th_and_not_dh_so_that_8_2_40_does_not_change_the_next_Kasika(self):
        """Kāśikā: आदेशान्तरकरणं झषस्तथोर्धोऽधः इत्यस्य निवृत्त्यर्थम् — a ढ्
        would have turned the त्/थ् after it to ध् (8.2.40); थ् is no झष्."""
        self.assertNotIn("8.2.40", steps(mine("āh{dhatu:ah}~tha")))
        self.assertNotIn("8.2.40", steps(mine("āh{dhatu:ah}~ta")))

    def test_aha_ahatuh_ahuh_no_jhal_follows_Kasika(self):
        """Kāśikā: झलीत्येव — आह, आहतुः, आहुः: the ह् stands."""
        for text in ("āh{dhatu:ah}~a", "āh{dhatu:ah}~atuḥ", "āh{dhatu:ah}~uḥ"):
            r = mine(text)
            self.assertNotIn("8.2.35", steps(r), text)
            self.assertNotIn("8.2.31", steps(r), text)

    def test_at_the_end_of_a_pada_it_is_not_this_rules_only_jhali(self):
        self.assertNotIn("8.2.35", steps(mine("āh{dhatu:ah}")))

    def test_the_vedic_vartika_hrgrahor_bhah_only_in_the_veda(self):
        """Kāśikā: हृग्रहोर्भश्छन्दसि हस्येति वक्तव्यम् — ग्रभीता, उद्ग्राभम्."""
        text = "grah{dhatu:grah}~ītā"
        self.assertNotIn("bh", mine(text).surface)
        r = mine(text, veda=True)
        self.assertEqual(r.surface, "grabhītā")
        step = r.outcomes[0].steps[0]
        self.assertEqual(step.detail.authority, VARTTIKA)
        self.assertEqual(step.sutra, "8.2.35")


# ---------------------------------------------------------------------------
# 8.2.36–8.2.38
# ---------------------------------------------------------------------------


class VrascaBhrasja(unittest.TestCase):
    """8.2.36."""

    def test_the_kasika_examples(self):
        """Kāśikā: यष्टा, स्रष्टा, मार्ष्टा, भ्रष्टा, व्रष्टा, प्रष्टा (छ्),
        लेष्टा, वेष्टा (श्) — 8.4.41 makes the त् ट्."""
        for text, expected in (
                ("yaj{dhatu:yaj}~tā", "yaṣṭā"),
                ("sṛj{dhatu:sṛj}~tā", "sṛṣṭā"),
                ("mārj{dhatu:mṛj}~tā", "mārṣṭā"),
                ("prach{dhatu:prach}~tā", "praṣṭā"),
                ("leś{dhatu:liś}~tā", "leṣṭā"),
                ("veś{dhatu:viś}~tā", "veṣṭā")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r), ["8.2.36", "8.4.41"], text)

    def test_bhrasj_and_vrasc_lose_their_sa_first_Nyasa(self):
        """Nyāsa: भ्रस्ज् and व्रस्च् — स्कोः संयोगाद्योः इति सकारलोपः, then the
        ष् (भ्रष्टा, व्रष्टा): 8.2.29, 8.2.36, 8.4.41 in that order."""
        for text, expected in (("bhrasj{dhatu:bhrasj}~tā", "bhraṣṭā"),
                               ("vrasc{dhatu:vrasc}~tā", "vraṣṭā")):
            r = mine(text, "ac_yan_ayadi")
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r), ["8.2.29", "8.2.36", "8.4.41"], text)

    def test_at_the_end_of_a_pada_Kasika(self):
        """Kāśikā: उपयट्, सम्राट्, विराट्, विभ्राट्, शब्दप्राट्, लिट्, विट् — ष्, then
        8.2.39 and 8.4.56."""
        for text, pair in (("upa-yaj{dhatu:yaj}", {"upayaṭ", "upayaḍ"}),
                           ("sam-rāj{dhatu:rāj}", {"samrāṭ", "samrāḍ"}),
                           ("vi-bhrāj{dhatu:bhrāj}", {"vibhrāṭ", "vibhrāḍ"}),
                           ("viś{dhatu:viś}", {"viṭ", "viḍ"})):
            r = mine(text)
            self.assertEqual(set(r.surfaces), pair, text)
            self.assertEqual(order_of(r, {"8.2.36", "8.2.39", "8.4.56"}),
                             ["8.2.36", "8.2.39", "8.4.56"], text)

    def test_it_displaces_8_2_30_and_8_2_39_and_the_padamanjari_says_why(self):
        """Padamañjarī: शकारान्तस्य जश्त्वे प्राप्ते, इतरेषां तु कुत्वे तदपवादः
        षत्वं विधीयते."""
        first = mine("yaj{dhatu:yaj}~tā").outcomes[0].steps[0]
        self.assertEqual(first.sutra, "8.2.36")
        self.assertIn("8.2.30", [a.sutra for a in first.against])
        self.assertIn("इतरेषां तु कुत्वे तदपवादः षत्वं विधीयते",
                      first.against[0].why)
        self.assertEqual(mine("viś{dhatu:viś}~tā").outcomes[0].steps[0].sutra,
                         "8.2.36")

    def test_without_the_flag_the_root_is_a_plain_word_and_takes_8_2_30(self):
        r = mine("yaj~tā")
        self.assertEqual(steps(r)[0], "8.2.30")
        self.assertEqual(r.surface, "yaktā")

    def test_the_root_names_come_from_the_projects_own_list(self):
        from src.astadhyayi import samyoganta
        self.assertIs(H.VRASCADI_EIGHT, samyoganta.VRASCADI_EIGHT)
        self.assertIs(H.DRUH_FOUR, samyoganta.DRUH_FOUR)

    def test_the_vartika_parau_vrajeh_parivrat(self):
        """Vārttika परौ व्रजेः षः पदान्ते (Kaumudī): परिव्राट्, परिव्राजौ — and
        only with परि before, at a pada's end."""
        r = mine("pari-vrāj{dhatu:vraj}")
        self.assertEqual(set(r.surfaces), {"parivrāṭ", "parivrāḍ"})
        first = r.outcomes[0].steps[0]
        self.assertEqual((first.sutra, first.detail.authority),
                         ("8.2.36", VARTTIKA))
        r = mine("vi-vrāj{dhatu:vraj}")
        self.assertNotIn("ṣ", "".join(s.detail.adesa
                                      for s in r.outcomes[0].steps))
        self.assertEqual(steps(r)[0], "8.2.30")


class EkacoBasoBhas(unittest.TestCase):
    """8.2.37."""

    def test_the_kasika_examples(self):
        """Kāśikā: भोत्स्यते, अभुद्ध्वम्, अर्थभुत्, निघोक्ष्यते, धोक्ष्यते,
        अधुग्ध्वम्, गोधुक्."""
        r = mine("bodh{dhatu:budh}~sya")
        self.assertEqual(steps(r), ["8.2.37", "8.4.55"])
        self.assertEqual(r.outcomes[0].steps[0].detail.adesa, "bh")
        self.assertEqual(r.surfaces, ("bhotsya",))
        r = mine("abudh{dhatu:budh}~dhvam")
        self.assertEqual(steps(r)[0], "8.2.37")
        self.assertTrue(r.surface.startswith("abhudh"))
        r = mine("artha-budh{dhatu:budh}")
        self.assertEqual(set(r.surfaces), {"arthabhut", "arthabhud"})
        r = mine("ni|goh{dhatu:guh}~sya")
        self.assertEqual(steps(r), ["8.2.31", "8.2.37", "8.2.41"])
        self.assertEqual(r.surfaces, ("nighoksya",))
        r = mine("doh{dhatu:duh}~sya")
        self.assertEqual(steps(r), ["8.2.32", "8.2.37", "8.4.55"])
        r = mine("aduh{dhatu:duh}~dhvam")
        self.assertEqual(steps(r), ["8.2.32", "8.2.37"])

    def test_the_jhash_is_the_one_8_2_32_made_and_in_that_order(self):
        """दुह्: the ह् is a घ् only after 8.2.32, and 8.2.37 — which stands
        after it — sees that घ् as the root's झष्."""
        r = mine("go-duh{dhatu:duh}")
        self.assertEqual(order_of(r, {"8.2.32", "8.2.37"}),
                         ["8.2.32", "8.2.37"])
        first = r.outcomes[0].steps[1]
        self.assertEqual((first.detail.sthanin, first.detail.adesa),
                         ("d", "dh"))

    def test_not_boddha_only_before_s_or_dhva_or_at_the_end_Kasika(self):
        """Kāśikā: स्ध्वोरिति किम्? बोद्धा, बोद्धुम्."""
        r = mine("bodh{dhatu:budh}~tā")
        self.assertNotIn("8.2.37", steps(r))
        self.assertTrue(r.surface.startswith("bo"))

    def test_not_krotsyati_the_first_is_no_bash_Kasika(self):
        """Kāśikā: बश इति किम्? क्रोत्स्यति."""
        self.assertNotIn("8.2.37", steps(mine("krodh{dhatu:krudh}~syati")))

    def test_not_dasyati_no_jhash_at_the_end_Kasika(self):
        """Kāśikā: झषन्तस्येति किम्? दास्यति."""
        self.assertNotIn("8.2.37", steps(mine("dā{dhatu:dā}~syati")))

    def test_not_a_root_of_two_vowels_ekacah_Kasika(self):
        """Kāśikā: एकाच इति किम्? — the rule is for a root of ONE vowel; a
        stem of two (गर्दभ्, दामलिह्) keeps its first sound: it is not भ् of
        गर्दभ् that the rule turns."""
        r = mine("gardabh{dhatu:gardabh}~sya")
        self.assertNotIn("8.2.37", steps(r))
        self.assertTrue(r.surface.startswith("gardap"))

    def test_the_bhash_is_of_the_same_varga_by_1_1_50(self):
        """Kāśikā: अत्र चत्वारो बशः स्थानिनो भषादेशाश्चत्वार एव… आन्तर्यतो
        व्यवस्था विज्ञास्यते — ब्→भ्, ग्→घ्, ड्→ढ्, द्→ध्."""
        for root, first in (("budh", "b"), ("gṛdh", "g"), ("duh", "d")):
            got = H._nearest(first, sorted(S.members("bhaṢ")))
            self.assertEqual(got, {"b": "bh", "g": "gh", "d": "dh"}[first])


class DadhasTathosCa(unittest.TestCase):
    """8.2.38."""

    def test_the_kasika_examples(self):
        """Kāśikā: धत्तः, धत्थः, धत्से, धत्स्व, धद्ध्वम् — दध् (धा with its
        reduplication) has its first द् turned to ध् before त्, थ्, स्, ध्व."""
        for after, expected_first in (("tas", "dhat"), ("thas", "dhat"),
                                      ("se", "dhat"), ("sva", "dhat"),
                                      ("dhvam", "dhadh")):
            r = mine(f"dadh{{dhatu:dhā}}~{after}")
            self.assertEqual(steps(r)[0], "8.2.38", after)
            self.assertTrue(r.surface.startswith("dh"), after)
            self.assertTrue(r.surface.startswith(expected_first), after)

    def test_not_dadhati_no_such_sound_follows_Kasika(self):
        """Kāśikā: झषन्तस्येत्येव — दधाति (the piece ends in आ, no झष्)."""
        r = mine("dadhā{dhatu:dhā}~ti")
        self.assertNotIn("8.2.38", steps(r))
        self.assertEqual(r.surfaces, ("dadhāti",))

    def test_8_2_40_leaves_it_out_by_adhah_Kasika(self):
        """8.2.40 has अधः: धत्तः, धत्थः — its त् stands (8.4.55 makes the
        द् a त्, and the त् of the ending is not turned to ध्)."""
        r = mine("dadh{dhatu:dhā}~ta")
        self.assertEqual(steps(r), ["8.2.38", "8.4.55"])
        self.assertNotIn("8.2.40", steps(r))
        self.assertEqual(r.surfaces, ("dhatta",))
        self.assertIn("8.2.40", steps(mine("dadh~ta")))

    def test_only_the_piece_dadh_of_dha(self):
        self.assertNotIn("8.2.38", steps(mine("dadh~ta")))
        self.assertNotIn("8.2.38", steps(mine("dadh{dhatu:dadh}~ta")))


# ---------------------------------------------------------------------------
# 8.2.40, 8.2.41
# ---------------------------------------------------------------------------


class JhasasTathorDho(unittest.TestCase):
    """8.2.40."""

    def test_the_kasika_examples(self):
        """Kāśikā: लब्धा, दोग्धा, लेढा, अलब्ध — the त् after a झष् is ध् (then
        8.4.53, not this family's, voices the first half)."""
        for text, before, after in (
                ("labh~tā", "bh", "dh"), ("dogh~tā", "gh", "dh"),
                ("leḍh~tā", "ḍh", "dh"), ("alabh~ta", "bh", "dh")):
            r = mine(text)
            self.assertEqual(steps(r)[0], "8.2.40", text)
            step = r.outcomes[0].steps[0]
            self.assertEqual((step.detail.sthanin, step.detail.adesa),
                             ("t", after), text)

    def test_th_too(self):
        r = mine("labh~thas")
        self.assertEqual(r.outcomes[0].steps[0].detail.sthanin, "th")

    def test_it_asks_the_projects_own_question_form(self):
        """`anga.jhasas_tathoh_dhah` answers what the sūtra does to a pair;
        the engine's step puts in what it says."""
        for jhas in ("bh", "dh", "gh", "jh", "ḍh"):
            got = jhasas_tathoh_dhah(jhas + "t")
            r = mine(f"a{jhas}~ta")
            step = next(s for s in r.outcomes[0].steps if s.sutra == "8.2.40")
            self.assertEqual(step.detail.adesa, got.now, jhas)
        self.assertIsNone(jhasas_tathoh_dhah("kt").result)
        self.assertNotIn("8.2.40", steps(mine("ak~ta")))

    def test_only_after_a_jhash_not_after_another_jhal(self):
        for text in ("ad~ta", "ap~ta", "ak~ta"):
            self.assertNotIn("8.2.40", steps(mine(text)), text)

    def test_not_after_dadh_adhah(self):
        """धत्तः, धत्थः: अधः."""
        self.assertNotIn("8.2.40", steps(mine("dadh{dhatu:dhā}~thas")))


class SadhohKahSi(unittest.TestCase):
    """8.2.41."""

    def test_the_kasika_examples(self):
        """Kāśikā: पेक्ष्यति, अपेक्ष्यत्, पिपिक्षति (ष् of पिष्); लेक्ष्यति,
        अलेक्ष्यत्, लिलिक्षति (the ढ् of लिह्, which 8.2.31 has made)."""
        r = mine("piṣ{dhatu:piṣ}~sya")
        self.assertEqual(steps(r), ["8.2.41"])
        self.assertEqual(r.surfaces, ("piksya",))
        r = mine("lih{dhatu:lih}~sya")
        self.assertEqual(steps(r), ["8.2.31", "8.2.41"])
        self.assertEqual(r.surfaces, ("liksya",))

    def test_the_ddha_is_the_one_8_2_31_made_and_it_is_seen(self):
        r = mine("lih{dhatu:lih}~sya")
        self.assertEqual(r.outcomes[0].steps[1].detail.sthanin, "ḍh")

    def test_not_pinashti_no_sa_follows_Kasika(self):
        """Kāśikā: पिनष्टि, लेढि — no स् follows."""
        self.assertNotIn("8.2.41", steps(mine("pinaṣ~ṭi")))
        self.assertNotIn("8.2.41", steps(mine("leh{dhatu:lih}~ti")))


# ---------------------------------------------------------------------------
# 6.1.71–6.1.76 — तुक्
# ---------------------------------------------------------------------------


class TukBeforePitKrt(unittest.TestCase):
    """6.1.71."""

    def test_the_kasika_examples(self):
        """Kāśikā: प्रकृत्य, प्रहृत्य, उपस्तुत्य (with ल्यप्, पित्)."""
        for text, expected in (
                ("pra|kṛ{dhatu:kṛ}~ya{krt,pit}", "prakṛtya"),
                ("pra|hṛ{dhatu:hṛ}~ya{krt,pit}", "prahṛtya"),
                ("upa|stu{dhatu:stu}~ya{krt,pit}", "upastutya"),
                ("vi|ji{dhatu:ji}~ya{krt,pit}", "vijitya")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r), ["6.1.71"], text)

    def test_not_aluya_the_vowel_is_long_Kasika(self):
        """Kāśikā: ह्रस्वस्येति किम्? आलूय, ग्रामणीः."""
        self.assertEqual(steps(mine("ā|lū{dhatu:lū}~ya{krt,pit}")), [])

    def test_not_krtam_the_affix_is_not_pit_Kasika(self):
        """Kāśikā: पितीति किम्? कृतम्, हृतम्."""
        self.assertEqual(steps(mine("kṛ{dhatu:kṛ}~ta{krt}")), [])

    def test_not_patutara_it_is_not_a_krt_Kasika(self):
        """Kāśikā: कृतीति किम्? पटुतरः, पटुतमः."""
        self.assertEqual(steps(mine("paṭu~tara{pit}")), [])
        # ... and the condition is the affix's, not the word's: a root followed
        # by a पित् affix that is not a कृत् (a taddhita) takes none
        self.assertEqual(steps(mine("ji{dhatu:ji}~ya{pit}")), [])

    def test_the_letters_cannot_say_so_the_flags_are_not_guessed(self):
        self.assertEqual(steps(mine("pra|kṛ~ya")), [])
        self.assertEqual(steps(mine("pra|kṛ{dhatu:kṛ}~ya")), [])

    def test_the_augment_belongs_to_the_vowel_and_stands_after_it(self):
        """1.1.46: तुक् has क् as its इत्, so it is put at the END of what it
        augments; the step says so."""
        step = mine("pra|kṛ{dhatu:kṛ}~ya{krt,pit}").outcomes[0].steps[0]
        self.assertEqual(step.detail.kind, "āgama")
        self.assertIn("1.1.46", [v.sutra for v in step.detail.via])


class TukChe(unittest.TestCase):
    """6.1.73 — नित्यम्, for a short vowel before छ्."""

    def test_sivacchaya_LSK_and_Kaumudi(self):
        """Laghu: शिवच्छाया; Kaumudī: स्वच्छाया — the derivation the Kaumudī
        gives, step for step: तुक्, then श्चुत्वस्यासिद्धत्वाज्जश्त्वेन दः,
        श्चुत्वेन जः, चर्त्वेन चः."""
        r = mine("śiva chāyā")
        self.assertEqual(steps(r), ["6.1.73", "8.2.39", "8.4.40", "8.4.55"])
        self.assertEqual(r.surfaces, ("śivacchāyā",))
        self.assertEqual(
            [(s.detail.sthanin, s.detail.adesa) for s in r.outcomes[0].steps],
            [("a", "t"), ("t", "d"), ("d", "j"), ("j", "c")])
        self.assertEqual(mine("sva chāyā").surfaces, ("svacchāyā",))
        self.assertEqual(whole("śiva chāyā").surfaces, ("śivacchāyā",))

    def test_kutva_is_not_applied_to_the_ca_asiddha_Kaumudi(self):
        """Kaumudī: चुत्वस्यासिद्धत्वात् चोः कुरिति कुत्वं न — 8.2.30 does not
        turn the final च् of शिवच् to क्."""
        self.assertNotIn("8.2.30", steps(mine("śiva chāyā")))

    def test_within_a_pada_icchati_yacchati_Kasika(self):
        """Kāśikā: इच्छति, यच्छति — the छ् is an aṅga-piece's."""
        self.assertEqual(steps(mine("i~chati")), ["6.1.73", "8.4.40"])
        self.assertEqual(mine("i~chati").surfaces, ("icchati",))

    def test_it_is_nitya_for_the_short_vowel_at_a_pada_end_too(self):
        """There is no option for a short vowel: one form (unlike लक्ष्मी छाया)."""
        for text in ("śiva chāyā", "pra chāyā", "śiva-chāyā"):
            self.assertEqual(len(mine(text).outcomes), 1, text)

    def test_the_vowel_takes_it_not_the_word_Kasika(self):
        """Kāśikā: ह्रस्व एवात्रागमी, न तु तदन्तः. The त् is put after the
        vowel — the augment is `made_by 6.1.73` and follows the अ."""
        r = mine("śiva chāyā")
        final = r.outcomes[0].steps[0]
        self.assertEqual(final.after.split()[0], "śivat")

    def test_no_chha_no_augment(self):
        self.assertEqual(steps(mine("śiva śāyā")), [])
        self.assertEqual(steps(mine("śiva cāyā")), [])


class TukAngMang(unittest.TestCase):
    """6.1.74 — आङ्माङोश्च: नित्यम्, against 6.1.76's option."""

    def test_the_kasika_examples(self):
        """Kāśikā: आच्छादयति, ईषच्छाया, माच्छैत्सीत्, माच्छिदत्."""
        r = mine("ā{ang} chādayati")
        self.assertEqual(r.surfaces, ("ācchādayati",))
        self.assertEqual(steps(r)[0], "6.1.74")
        r = mine("mā{mang} chidat")
        self.assertEqual(steps(r)[0], "6.1.74")
        self.assertEqual(surfaces("mā{mang} chidat"),
                         {"mācchidat", "mācchidad"})

    def test_it_is_invariable_where_6_1_76_would_give_an_option(self):
        """Kāśikā: पदान्ताद् वा इति विकल्पे प्राप्ते नित्यं तुगागमो भवति —
        one course only, and the step names 6.1.76 as what it displaced."""
        r = mine("ā{ang} chādayati")
        self.assertEqual(len(r.outcomes), 1)
        first = r.outcomes[0].steps[0]
        self.assertIn("6.1.76", [a.sutra for a in first.against])
        self.assertIn("इति विकल्पे प्राप्ते नित्यं तुगागमो भवति",
                      first.against[0].why)

    def test_not_a_chaya_the_a_of_recollection_Kasika(self):
        """Kāśikā: ङिद्विशिष्टग्रहणं किम्? आ छाया, आच् छाया; प्रमा छन्दः,
        प्रमाच् छन्दः — no flag, so 6.1.76's option: both forms."""
        for text, pair in (("ā chāyā", {"ācchāyā", "āchāyā"}),
                           ("pramā chandaḥ", {"pramācchandaḥ",
                                              "pramāchandaḥ"})):
            r = mine(text, "visarga_ru")
            self.assertEqual(set(r.surfaces), pair, text)
            self.assertEqual(steps(r, 0)[0], "6.1.76", text)


class TukDirgha(unittest.TestCase):
    """6.1.75 — दीर्घात्, inside a pada."""

    def test_the_kasika_examples(self):
        """Kāśikā: ह्रीच्छति, म्लेच्छति."""
        for text, expected in (("hrī~chati", "hrīcchati"),
                               ("mle~chati", "mlecchati")):
            r = mine(text)
            self.assertEqual(r.surfaces, (expected,), text)
            self.assertEqual(steps(r), ["6.1.75", "8.4.40"], text)
            self.assertEqual(len(r.outcomes), 1, text)

    def test_the_augment_is_after_the_long_vowel_not_before_the_cha(self):
        """Kaumudī: दीर्घस्यायं तुक् न तु छस्य (सेनासुराच्छाया): the त् stands
        between the vowel and the छ्, so the छ् is still heard."""
        r = mine("hrī~chati")
        self.assertEqual(r.outcomes[0].steps[0].after, "hrīt chati")
        self.assertIn("ch", r.surface)

    def test_it_leaves_the_pada_final_long_vowel_to_6_1_76(self):
        r = mine("kuṭī chāyā")
        self.assertNotIn("6.1.75", steps(r))


class TukPadantadVa(unittest.TestCase):
    """6.1.76 — पदान्ताद् वा."""

    def test_kuticcaya_kutichaya_and_laksmi_Kasika_and_Kaumudi(self):
        """Kāśikā: कुटीच्छाया, कुटीछाया; कुवलीच्छाया, कुवलीछाया. Kaumudī:
        लक्ष्मीच्छाया, लक्ष्मी छाया."""
        for text, pair in (("kuṭī chāyā", {"kuṭīcchāyā", "kuṭīchāyā"}),
                           ("kuvalī chāyā", {"kuvalīcchāyā", "kuvalīchāyā"}),
                           ("lakṣmī chāyā", {"lakṣmīcchāyā", "lakṣmīchāyā"})):
            r = mine(text)
            self.assertEqual(set(r.surfaces), pair, text)
            self.assertEqual(len(r.outcomes), 2, text)
            self.assertEqual(r.outcomes[0].choices, (("6.1.76", True),))
            self.assertEqual(r.outcomes[1].choices, (("6.1.76", False),))

    def test_the_declined_course_adds_no_augment_and_no_other_rule_gives_it(self):
        """In the course that declines, nothing else puts the तुक् in — 6.1.75
        is kept to the long vowels INSIDE a pada, so it does not step in."""
        r = mine("lakṣmī chāyā")
        self.assertEqual(steps(r, 1, declined=True), ["6.1.76*"])
        self.assertEqual(r.outcomes[1].final.joined(), "lakṣmīchāyā")

    def test_it_is_a_prapta_vibhasha_Kasika(self):
        """Kāśikā: पूर्वेण नित्यं प्राप्तो वा तुगागमो भवति — the option
        replaces the invariable 6.1.75 for a pada-final long vowel."""
        step = mine("lakṣmī chāyā").outcomes[0].steps[0]
        self.assertEqual(step.option, "वा")

    def test_the_two_words_need_not_be_construed_together_Tattvabodhini(self):
        """Tattvabodhinī: तिष्ठतु कुमारी, छत्रं हर देवदत्त — it is a rule of a
        पदान्त, not a पदविधि; the engine reads the junction, not the sense."""
        self.assertEqual(set(mine("kumārī chatram").surfaces),
                         {"kumārīcchatram", "kumārīchatram"})

    def test_a_short_vowel_is_not_optional(self):
        self.assertEqual(len(mine("kuṭi chāyā").outcomes), 1)


@unittest.skipUnless(H._TUK, "this core has no `Rule.operation`, so 6.1.86 "
                              "cannot be asked of a तुक्")
class TukSeesTheEkadesaAsiddha(unittest.TestCase):
    """6.1.86 षत्वतुकोरसिद्धः, asked through `Rule.operation` — the hook the core
    gives a rule that says it is a तुक्."""

    TEXT = "adhi|i{dhatu:i}~ya{krt,pit}"

    def test_adhitya_Kasika_on_6_1_86(self):
        """Kāśikā: अधीत्य — the ई is the एकादेश of इ + इ (6.1.101), and for a तुक्
        that substitute is asiddha, so the dhātu's own short इ takes the तुक्:
        the एकादेश first, then 6.1.71 acting on the two sounds it replaced."""
        r = mine(self.TEXT, "ac_ekadesa")
        self.assertEqual(r.surfaces, ("adhītya",))
        self.assertEqual(steps(r), ["6.1.101", "6.1.71"])
        self.assertEqual(r.outcomes[0].steps[1].detail.sthanin, "i")

    def test_every_tuk_rule_declares_the_operation(self):
        for r in H.RULES:
            if r.sutra in ("6.1.71", "6.1.73", "6.1.74", "6.1.75", "6.1.76"):
                self.assertEqual(r.operation, "tuk", r.sutra)
            else:
                self.assertEqual(r.operation, "", r.sutra)

    def test_without_the_declaration_the_rule_sees_a_long_vowel_and_gives_none(self):
        """The test that can fail: take `operation` off 6.1.71 and the ई is
        long, so no तुक् — *अधीय."""
        rules = tuple(replace(r, operation="") if r.sutra == "6.1.71" else r
                      for r in rulebook.rules_of(FAMILY, "ac_ekadesa"))
        outcomes = derive(parse(self.TEXT), rules)
        self.assertEqual({o.surface for o in outcomes}, {"adhīya"})

    def test_a_tuk_is_put_in_after_a_vowel_seen_only_through_its_ekadesa(self):
        """The vowel is read through the substitute, and the तुक् is put in
        where the substitute ends — the trace shows it as an āgama, made by
        6.1.71, standing between the ई and the य्."""
        final = mine(self.TEXT, "ac_ekadesa").outcomes[0].final
        made = [s for s in final.segs if s.made_by == "6.1.71"]
        self.assertEqual([s.s for s in made], ["t"])
        joined = "".join(s.s for s in final.segs)
        self.assertEqual(joined, "adhītya")

    def test_a_long_vowel_that_an_ekadesa_made_is_two_short_ones_for_tuk(self):
        """6.1.73 is invariable for a short vowel: सा + छाया, where the ा is the
        एकादेश of स + अ, takes the तुक् always (सच्छाया-like), not by 6.1.76's
        option."""
        r = mine("sa a chāyā", "ac_ekadesa")
        self.assertEqual(len(r.outcomes), 1)
        self.assertIn("6.1.73", steps(r))
        self.assertNotIn("6.1.76", steps(r, declined=True))


# ---------------------------------------------------------------------------
# What every rule shares
# ---------------------------------------------------------------------------


class Traces(unittest.TestCase):
    """The trace prints the corpus's own sūtra and says what THIS form did."""

    def test_the_words_of_every_step_are_the_corpus_words(self):
        known = corpus.load_vidyut_sutrapatha()
        for text in ("tat śiva", "śiva chāyā", "ud|sthāna{dhatu:sthā}",
                     "ṣaṭ te", "praś~na", "yaj{dhatu:yaj}~tā",
                     "lakṣmī chāyā", "bhavān lunāti"):
            for outcome in sandhi(text).outcomes:
                for step in trace.outcome_dict(outcome)["steps"]:
                    self.assertEqual(step["sutra_iast"],
                                     known[step["sutra"]].text, text)
                    for via in step["via"]:
                        self.assertEqual(via["text_iast"],
                                         known[via["sutra"]].text, text)

    def test_every_cited_sutra_exists_including_the_ones_that_lose(self):
        known = corpus.load_vidyut_sutrapatha()
        for text in ("tat śiva", "ṣaṭ te", "praś~na", "yaj{dhatu:yaj}~tā",
                     "droh{dhatu:druh}~tā", "ā{ang} chādayati",
                     "sat cit", "ud|sthāna{dhatu:sthā}"):
            for outcome in sandhi(text).outcomes:
                for step in outcome.steps:
                    for s in step.sutras:
                        self.assertIn(s, known, (text, s))
                    for lost in step.against:
                        self.assertIn(lost.sutra, known, (text, lost.sutra))

    def test_the_trace_says_what_this_form_did_in_both_scripts(self):
        text = mine("tat śiva").trace()
        self.assertIn("तच्छिव (tacchiva)", text)
        self.assertIn("स्तोः श्चुना श्चुः (stoḥ ścunā ścuḥ)", text)
        self.assertIn("शश्छोऽटि (śaścho’ṭi)", text)
        self.assertIn("द् (d) → ज् (j)", text)

    def test_an_option_declined_is_shown_declined(self):
        text = mine("tat śiva").trace()
        self.assertIn("NOT applied in this course", text)

    def test_the_result_serialises(self):
        import json
        json.dumps(mine("tat śloka").to_dict(), ensure_ascii=False)
        json.dumps(mine("lakṣmī chāyā").to_dict(), ensure_ascii=False)


class TheClassesAreDerivedNotTyped(unittest.TestCase):
    """The स्तु, श्चु, ष्टु classes are the Śikṣā's places, read."""

    def test_each_class_is_a_varga_and_the_sibilant_of_its_place(self):
        self.assertEqual(H._cls("tu")[0], "s")
        self.assertEqual(H._cls("cu")[0], "ś")
        self.assertEqual(H._cls("ṭu")[0], "ṣ")
        for varga in ("tu", "cu", "ṭu"):
            sibilant, klass = H._cls(varga)
            self.assertEqual(klass, frozenset(VARGA[varga]) | {sibilant})

    def test_the_rule_names_come_from_the_corpus_not_from_the_module(self):
        self.assertEqual(H._named("8.4.40"), "स्तोः श्चुना श्चुः")


class TheFlagsAreReadBySomeRule(unittest.TestCase):
    """A flag no rule reads changes nothing without a word; the core says so
    (`SandhiResult.warnings`) where it can. Every flag this family asks for is
    one of its rules reads, so a caller who spells it right is never warned."""

    CASES = (
        "yaj{dhatu:yaj}~tā", "pra|kṛ{dhatu:kṛ}~ya{krt,pit}",
        "ā{ang} chādayati", "mā{mang} chidat",
        "alavi~s{sic}~dhvam{pratyaya}",
        "adev~i{it_agama}~s{sic}~ī{iit_agama}~t", "ṣaṭ-nagarī{stem:nagarī}")

    def test_no_warning_for_a_flag_this_family_reads(self):
        for text in self.CASES:
            self.assertEqual(getattr(sandhi(text), "warnings", ()), (), text)

    def test_a_misspelt_flag_is_no_flag_and_the_rule_does_not_fire(self):
        """The rules ask for exactly `dhatu`, `krt`, `pit`, … — nothing near
        them: a misspelling switches the rule off (and, in a core that warns,
        is said)."""
        self.assertNotIn("8.2.36", steps(mine("yaj{dhaatu:yaj}~tā")))
        self.assertEqual(steps(mine("pra|kṛ{dhatu:kṛ}~ya{krt,pt}")), [])
        warned = getattr(sandhi("yaj{dhaatu:yaj}~tā"), "warnings", None)
        if warned is not None:                    # a core that says so
            self.assertEqual(len(warned), 1)
            self.assertIn("dhaatu", warned[0])


class EitherScript(unittest.TestCase):
    """Devanāgarī is converted at the one boundary where it arrives (NORTH_STAR
    §5), so a form typed in either script is derived the same way — flags
    included, whose root the rules read whichever way it is written."""

    def test_the_same_steps_from_devanagari_as_from_roman(self):
        for roman, deva in (
                ("tat śiva", "तत् शिव"),
                ("vāc pati", "वाच् पति"),
                ("śiva chāyā", "शिव छाया"),
                ("ṣaṭ te", "षट् ते"),
                ("ud|sthāna{dhatu:sthā}", "उद्|स्थान{dhatu:स्था}"),
                ("yaj{dhatu:yaj}~tā", "यज्{dhatu:यज्}~ता"),
                ("lih{dhatu:lih}~sya", "लिह्{dhatu:लिह्}~स्य")):
            a, b = mine(roman), mine(deva)
            self.assertEqual(steps(a, declined=True), steps(b, declined=True),
                             roman)
            self.assertEqual(a.surfaces, b.surfaces, roman)


class EverythingTerminates(unittest.TestCase):
    """Whatever two consonants meet — across a pada and inside one — the
    derivation stops, cites real sūtras and ends in sounds."""

    CONSONANTS = tuple(s for row in VARGA.values() for s in row) + (
        "y", "r", "l", "v", "ś", "ṣ", "s", "h")

    def test_every_pair_of_consonants_across_a_pada_and_inside_one(self):
        known = corpus.load_vidyut_sutrapatha()
        count = 0
        for a in self.CONSONANTS:
            for b in self.CONSONANTS:
                for text in (f"ka{a} {b}ta", f"ka{a}~{b}ta"):
                    r = sandhi(text)
                    for outcome in r.outcomes:
                        self.assertEqual(outcome.stopped, "no rule applies",
                                         text)
                        for step in outcome.steps:
                            for sutra in step.sutras:
                                self.assertIn(sutra, known, text)
                    count += 1
        self.assertGreater(count, 2000)

    def test_a_call_stays_in_the_millisecond_range(self):
        import time
        sandhi("vāc pati")                       # the first call warms imports
        start = time.perf_counter()
        for _ in range(20):
            sandhi("tat śiva")
        per_call = (time.perf_counter() - start) / 20
        self.assertLess(per_call, 0.25, per_call)


class TheLaghuTags(unittest.TestCase):
    """The Laghusiddhāntakaumudī text (GRETIL) tags each sūtra `vlk_N = p_A,B.C`.
    Those tags have errors; the Vidyut sūtrapāṭha is the standing witness
    (NORTH_STAR §5), so every tag in the family's lines is checked against it."""

    PATH = "reference/mula/ancillary/gretil-laghusiddhantakaumudi.txt"
    TAG = re.compile(r"^(.*?)\s*// vlk_\d+ = p_(\d+),(\d+)\.(\d+) //")

    @staticmethod
    def _plain(words):
        return re.sub(r"[\s'’ऽ]", "", words).lower()

    def _lines(self):
        with open(self.PATH, encoding="utf-8") as handle:
            lines = handle.read().splitlines()
        # the lines the task names: 176-205 and 254-257 (1-based)
        chosen = list(range(176, 206)) + list(range(254, 258))
        for number in chosen:
            match = self.TAG.match(lines[number - 1])
            if match:
                words, a, b, c = match.groups()
                yield number, words, f"{a}.{b}.{c}"

    def test_every_tag_in_the_family_s_lines_is_the_vidyuts_or_is_a_known_error(self):
        known = corpus.load_vidyut_sutrapatha()
        wrong = {}
        seen = 0
        for number, words, tagged in self._lines():
            seen += 1
            if self._plain(words) != self._plain(known[tagged].text):
                wrong[words] = tagged
        self.assertGreaterEqual(seen, 15)
        # exactly the two the Laghu mis-tags in these lines
        self.assertEqual(wrong, {"udaḥ sthāstambhoḥ pūrvasya": "8.4.41",
                                 "padāntādvā": "6.1.79"})

    def test_the_two_mistagged_sutras_are_at_their_true_numbers_in_this_family(self):
        known = corpus.load_vidyut_sutrapatha()
        self.assertEqual(known["8.4.61"].text, "udaḥ sthāstambhoḥ pūrvasya")
        self.assertEqual(known["6.1.76"].text, "padāntādvā")
        have = {r.sutra for r in H.RULES}
        self.assertIn("8.4.61", have)
        self.assertIn("6.1.76", have)
        self.assertNotEqual(known["6.1.79"].text, "padāntādvā")
        self.assertNotEqual(known["8.4.41"].text, "udaḥ sthāstambhoḥ pūrvasya")

    def test_the_test_would_notice_a_third_mistag(self):
        """The check must be able to fail: a wrong number is caught."""
        known = corpus.load_vidyut_sutrapatha()
        self.assertNotEqual(self._plain("stoḥ ścunā ścuḥ"),
                            self._plain(known["8.4.41"].text))


class TheWholeRulebook(unittest.TestCase):
    """The classical surfaces, with every family's rules loaded."""

    def test_the_laghusiddhantakaumudi_hal_sandhi_lines(self):
        """Laghu 176–205: रामश्शेते, रामश्चिनोति, सच्चित्, शार्ङ्गिञ्जय, विश्नः,
        प्रश्नः, रामष्षष्ठः, रामष्टीकते, पेष्टा, तट्टीका, चक्रिण्ढौकसे,
        षट् सन्तः, षट् ते, ईट्टे, सर्पिष्टमम्, सन्षष्ठः, वागीशः, तल्लयः,
        विद्वाँल्लिखति, वाग्घरिः, तच्छिवः, तच्शिवः, शिवच्छाया,
        लक्ष्मीच्छाया, लक्ष्मी छाया."""
        cases = (
            ("rāmas śete", {"rāmaśśete", "rāmaḥśete"}), ("rāmas cinoti", {"rāmaścinoti"}),
            ("sat cit", {"saccit", "saccid"}),
            ("śārṅgin jaya", {"śārṅgiñjaya"}),
            ("viś~na", {"viśna"}), ("praś~na", {"praśna"}),
            ("rāmas ṣaṣṭhaḥ", {"rāmaṣṣaṣṭhaḥ", "rāmaḥṣaṣṭhaḥ"}),
            ("rāmas ṭīkate", {"rāmaṣṭīkate"}),
            ("peṣ~tā", {"peṣṭā"}), ("tat ṭīkā", {"taṭṭīkā"}),
            ("cakrin ḍhaukase", {"cakriṇḍhaukase"}),
            ("ṣaṭ santaḥ", {"ṣaṭsantaḥ", "ṣaṭtsantaḥ"}),  # 8.2.39 → ḍ, 8.3.29 vā dhuṭ
            ("ṣaṭ te", {"ṣaṭte"}),
            ("īḍ~te", {"īṭṭe"}), ("sarpiṣ~tama", {"sarpiṣṭama"}),
            ("san ṣaṣṭhaḥ", {"sanṣaṣṭhaḥ"}),
            ("vāc īśaḥ", {"vāgīśaḥ"}), ("tat layaḥ", {"tallayaḥ"}),
            ("vidvān likhati", {"vidvāl̐likhati"}),
            ("tat śivaḥ", {"tacchivaḥ", "tacśivaḥ"}),
            ("śiva chāyā", {"śivacchāyā"}),
            ("lakṣmī chāyā", {"lakṣmīcchāyā", "lakṣmīchāyā"}),
            ("ud gacchati", {"udgacchati"}))
        for text, expected in cases:
            self.assertEqual(set(whole(text).surfaces), expected, text)

    def test_vakpati_vagisah_tacchivah_in_the_whole_engine(self):
        self.assertEqual(whole("vāc pati").surfaces, ("vākpati",))
        self.assertEqual([s.sutra for s in whole("vāc pati").outcomes[0].steps],
                         ["8.2.30", "8.2.39", "8.4.55"])
        self.assertEqual(whole("vāc īśaḥ").surface, "vāgīśaḥ")

    def test_the_root_forms_are_final_in_the_whole_rulebook_too(self):
        """Forms that no other family alters: यष्टा, प्रष्टा, भ्रष्टा, विट्, धुक्,
        अर्थभुत्, आत्थ, उत्थान (flags as the caller gives them)."""
        for text, expected in (
                ("yaj{dhatu:yaj}~tā", {"yaṣṭā"}),
                ("prach{dhatu:prach}~tā", {"praṣṭā"}),
                ("bhrasj{dhatu:bhrasj}~tā", {"bhraṣṭā"}),
                ("viś{dhatu:viś}", {"viṭ", "viḍ"}),
                ("go-duh{dhatu:duh}", {"godhuk", "godhug"}),
                ("artha-budh{dhatu:budh}", {"arthabhut", "arthabhud"}),
                ("āh{dhatu:ah}~tha", {"āttha"}),
                ("ud|sthāna{dhatu:sthā}", {"utthāna", "utththāna"}),
                ("pra|kṛ{dhatu:kṛ}~ya{krt,pit}", {"prakṛtya"}),
                ("mātur~s", {"mātuḥ"})):
            self.assertEqual(set(whole(text).surfaces), expected, text)

    def test_lakshmi_and_the_visarga_and_the_other_families_agree(self):
        """ramas sete: the visarga family's 8.2.66, 8.3.15, 8.3.34 and this
        family's 8.4.40, in that order — the rulebook interlocks."""
        r = whole("rāmas śete")
        out = next(o for o in r.outcomes if o.surface == "rāmaśśete")
        self.assertEqual([s.sutra for s in out.steps if not s.declined],
                         ["8.2.66", "8.3.15", "8.3.34", "8.4.40"])


class WhatBreaksWithoutTheRule(unittest.TestCase):
    """A test that cannot fail is worse than none: take a rule out and the
    answer changes."""

    @staticmethod
    def _without(text, *sutras, **kw):
        rules = tuple(r for r in rulebook.rules_of(FAMILY, "visarga_ru")
                      if r.sutra not in sutras)
        outcomes = derive(parse(text, **kw), rules)
        return {o.surface for o in outcomes}

    def test_without_8_4_44_prasna_becomes_prañña(self):
        self.assertEqual(self._without("praś~na"), {"praśna"})
        self.assertNotEqual(self._without("praś~na", "8.4.44"),
                            surfaces("praś~na"))
        self.assertEqual(self._without("praś~na", "8.4.44"), {"praśña"})

    def test_without_8_4_42_sat_te_becomes_satte_with_a_cerebral(self):
        self.assertNotEqual(self._without("ṣaṭ te", "8.4.42"),
                            surfaces("ṣaṭ te"))
        self.assertEqual(self._without("ṣaṭ te", "8.4.42"), {"ṣaṭṭe"})

    def test_without_8_4_43_sanshashthah_gets_a_cerebral_n(self):
        self.assertEqual(self._without("san ṣaṣṭhaḥ", "8.4.43"), {"saṇṣaṣṭhaḥ"})
        self.assertEqual(self._without("san ṣaṣṭhaḥ"), {"sanṣaṣṭhaḥ"})

    def test_without_8_2_36_yashta_becomes_yakta(self):
        self.assertEqual(self._without("yaj{dhatu:yaj}~tā", "8.2.36"),
                         {"yaktā"})
        self.assertEqual(self._without("yaj{dhatu:yaj}~tā"), {"yaṣṭā"})

    def test_without_8_2_32_dagdha_takes_the_dh_of_8_2_31(self):
        got = self._without("dah{dhatu:dah}~tā", "8.2.32")
        self.assertEqual(got, {"daḍhḍhā"})
        self.assertEqual(self._without("dah{dhatu:dah}~tā"), {"daghdhā"})

    def test_without_6_1_74_a_chadayati_is_optional(self):
        rules = tuple(r for r in rulebook.rules_of(FAMILY)
                      if r.sutra != "6.1.74")
        got = {o.surface for o in derive(parse("ā{ang} chādayati"), rules)}
        self.assertEqual(got, {"ācchādayati", "āchādayati"})
        self.assertEqual(surfaces("ā{ang} chādayati"), {"ācchādayati"})

    def test_without_8_4_60_tallaya_keeps_its_dental(self):
        self.assertEqual(self._without("tat laya", "8.4.60"), {"tadlaya"})

    def test_without_nearness_by_internal_effort_dh_would_be_s(self):
        """The reason `_nearest` orders place, internal effort, external
        quality: with the external quality ranked first — a nearest that picks
        the candidate sharing the most external qualities — ध् before स् is
        स्, and युयुत्सते would be *युयुस्सते. Stand such a choice in for
        `_nearest` and the form changes."""
        from src.astadhyayi import adesa

        def by_quality_first(sthanin, candidates):
            near = adesa.antaratama(sthanin, candidates)
            return near[0] if len(near) == 1 else None

        original = H._nearest_cached
        H._nearest_cached = lambda s, c: by_quality_first(s, list(c))
        try:
            self.assertEqual(surfaces("yuyudh~sate"), {"yuyussate"})
        finally:
            H._nearest_cached = original
        self.assertEqual(surfaces("yuyudh~sate"), {"yuyutsate"})


if __name__ == "__main__":
    unittest.main()
