# -*- coding: utf-8 -*-
"""
The family of the single substitutes — 6.1.84 to 6.1.112 (`families/ac_ekadesa.py`).

**What these tests hold the rules to.** Every expectation is a form the
commentaries themselves work — the Kāśikā's, the Laghusiddhāntakaumudī's, the
Siddhāntakaumudī's, the Bālamanoramā's — with its source named in the test's
docstring, and every counter-example those commentaries give under *X iti
kim?*. Where a result could come out right by luck (a later rule winning where
an earlier rule was *meant* to be displaced), the test also asserts the STEPS:
which sūtra was done, and which the step says it displaced, with the words the
tradition gives for it — and, where a declared relation is what does the work,
that taking the declaration away changes the answer.

**How the assertions are kept about this family.** The tests run against a
STAGE: this family's rules and the few neighbours whose steps they expect to see
— yaṇ and ayavāyāv (6.1.77, 6.1.78), the ru of 8.2.66 with 6.1.113 and 8.3.15,
jaśtva and śākalya's loss. Other families change what a form looks like
afterwards — doubling (8.4.46–47) forks a derivation of *mārutyaḥ* into four,
the retroflex rules turn an n — and a test that read those changes would fail
when a family it never mentions was merged. So an assertion about *this*
family's work reads what the step itself records (`Step.after`, the form as it
stood the moment the rule had acted) and the vowel-junction sūtras
(6.1.77–6.1.112) among the steps; only the invariants of the whole rulebook
(every sūtra named is real, a junction stays fast) are asked of all of it.

**Flags.** What the letters cannot say — a preverb, a dhātu, the particle om,
which case ending `as` is — is given as the caller gives it (the family's module
docstring lists them), and each such test has its control: the same words
without the flag, showing that the flag is what decided.
"""

from __future__ import annotations

import dataclasses
import json
import re
import time
import unittest

from src.astadhyayi import corpus
from src.astadhyayi.adesa import guna_of, vrddhi_of
from src.astadhyayi.anga import akah_savarne_dirghah, ato_gune
from src.astadhyayi.asiddha import ekadesa_visible
from src.astadhyayi.ekadesa import EKADESA_TABLE
from src.astadhyayi.sandhi import rulebook, trace
from src.astadhyayi.sandhi import sandhi as sandhi_of_everything
from src.astadhyayi.sandhi.engine import apply, collect, derive
from src.astadhyayi.sandhi.families import ac_ekadesa as fam
from src.astadhyayi.sandhi.parse import parse
from src.astadhyayi.sandhi.segs import View

#: The sūtras outside this family whose steps the tests expect to see.
NEIGHBOURS = ("6.1.77", "6.1.78", "6.1.113", "8.2.30", "8.2.39", "8.2.66", "8.3.15",
              "8.3.19", "8.4.55")
STAGE = tuple(r for r in rulebook.all_rules()
              if r.sutra in NEIGHBOURS or r in rulebook.rules_of("ac_ekadesa"))


def sandhi(text, **kw):
    """The junction derived on the STAGE, unless the test says which rules."""
    kw.setdefault("rules", STAGE)
    return sandhi_of_everything(text, **kw)


IN_SCOPE = tuple(f"6.1.{n}" for n in range(84, 113))
SUPPORTS = ("1.1.1", "1.1.2", "1.1.3") + tuple(f"1.1.{n}" for n in range(53, 65))


def _order(sutra):
    return tuple(int(p) for p in sutra.split("."))


def vowel_steps(outcome):
    """The vowel-junction sūtras among a derivation's steps (6.1.77–6.1.112), in
    order — the rest (the visarga chain, jaśtva) belong to other families."""
    return [s.sutra for s in outcome.steps
            if not s.declined and _order("6.1.77") <= _order(s.sutra) <= _order("6.1.112")]


def run(text, k=0, **kw):
    return sandhi(text, **kw).outcomes[k]


def steps_of(text, k=0, **kw):
    return vowel_steps(run(text, k, **kw))


def step_of(text, sutra, k=0, **kw):
    """The step of `sutra` in the k-th derivation of `text`."""
    out = run(text, k, **kw)
    for s in out.steps:
        if s.sutra == sutra and not s.declined:
            return s
    raise AssertionError(f"{sutra} is not among the steps of {text!r}: "
                         f"{[x.sutra for x in out.steps]}")


def after(text, sutra, k=0, **kw):
    """The form as it stood when `sutra` had acted, with the words joined."""
    return step_of(text, sutra, k, **kw).after.replace(" ", "")


def lost(step):
    """What a step says it displaced: {sūtra: why}."""
    return {a.sutra: a.why for a in step.against}


def norm(text):
    """The on-disk commentary as `validate.py` reads it: markup off, spaces one."""
    text = re.sub(r"<<|>>", "", text)
    text = re.sub(r"\[\[[^\]]*\]\]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def tradition(work, sutra):
    return norm(corpus.commentary_on(sutra, work) or "")


def rules_without(sutra, varttika="", **change):
    """The whole rulebook with one rule's declaration changed — to see that the
    declaration is what was doing the work."""
    return tuple(
        dataclasses.replace(r, **change)
        if r.sutra == sutra and r.varttika == varttika else r
        for r in STAGE)


def derive_with(rules, text):
    return derive(parse(text), rules)[0]


class Guna(unittest.TestCase):
    """6.1.84 एकः पूर्वपरयोः and 6.1.87 आद्गुणः."""

    def test_the_kasikas_examples_on_6_1_84_and_6_1_87(self):
        """Kāśikā 6.1.84 खट्वेन्द्रः, मालेन्द्रः; 6.1.87 तवेदम्, तवेहते, खट्वेहते,
        तवोदकम्, खट्वोदकम्; Kaumudī उपेन्द्रः, रमेशः, गङ्गोदकम्."""
        for text, form in (
                ("khaṭvā indra", "khaṭvendra"), ("mālā indra", "mālendra"),
                ("tava idam", "tavedam"), ("tava īhate", "tavehate"),
                ("khaṭvā īhate", "khaṭvehate"), ("tava udakam", "tavodakam"),
                ("khaṭvā udakam", "khaṭvodakam"), ("upa indra", "upendra"),
                ("ramā īśa", "rameśa"), ("gaṅgā udakam", "gaṅgodakam")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.87"])
                self.assertEqual(after(text, "6.1.87"), form)

    def test_one_sound_stands_for_two_and_it_belongs_to_the_later_word(self):
        """6.1.84 (Kāśikā: पूर्वपरग्रहणं द्वयोरपि युगपदादेशप्रतिपत्त्यर्थम्, एकग्रहणं
        पृथगादेशनिवृत्त्यर्थम्): ONE sound in the room of both — the ए of खट्वेन्द्रः is
        neither the आ's nor the इ's, and 6.1.85 keeps the earlier word in mind."""
        final = run("khaṭvā indra").final
        made = [s for s in final.segs if s.made_by == "6.1.87"]
        self.assertEqual([s.s for s in made], ["e"])
        self.assertEqual(len(final.segs), 9)          # ten sounds went in, nine stand
        self.assertEqual(made[0].w, 1)                # the later word
        self.assertEqual(made[0].lw, 0)               # remembering the earlier
        self.assertEqual(final.joined(), "khaṭvendra")

    def test_r_and_l_take_their_r_and_l_by_1_1_51(self):
        """Kāśikā 6.1.87 तवर्श्यः, खट्वर्श्यः, तवल्कारः, खट्वल्कारः (ऌकारस्य स्थाने योऽण्
        तस्य लपरत्वमिष्यते); Bālamanoramā कृष्णर्द्धिः."""
        for text, form, r_or_l in (
                ("tava ṛśya", "tavarśya", "r"), ("khaṭvā ṛśya", "khaṭvarśya", "r"),
                ("tava ḷkāra", "tavalkāra", "l"), ("khaṭvā ḷkāra", "khaṭvalkāra", "l"),
                ("kṛṣṇa ṛddhi", "kṛṣṇarddhi", "r")):
            with self.subTest(text=text):
                step = step_of(text, "6.1.87")
                self.assertEqual(after(text, "6.1.87"), form)
                self.assertIn("1.1.51", step.sutras)
                self.assertEqual(step.detail.adesa, "a" + r_or_l)

    def test_no_raparatva_where_there_is_no_r(self):
        self.assertNotIn("1.1.51", step_of("khaṭvā indra", "6.1.87").sutras)

    def test_the_guna_is_the_projects_own_codification(self):
        """Every guṇa of an इक् after an अवर्ण: the step's substitute is
        `adesa.guna_of` — nothing is tabulated here."""
        checked = 0
        for right in ("i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ"):
            for first in ("pa", "pā"):
                text = f"{first} {right}ka"
                self.assertEqual(steps_of(text), ["6.1.87"], text)
                self.assertEqual(step_of(text, "6.1.87").detail.adesa,
                                 guna_of(right), text)
                checked += 1
        self.assertEqual(checked, 14)


class Vrddhi(unittest.TestCase):
    """6.1.88 वृद्धिरेचि — the exception to guṇa."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā ब्रह्मैडका, खट्वैडका, ब्रह्मैतिकायनः, ब्रह्मौदनः, खट्वौपगवः; Kaumudī
        कृष्णैकत्वम्, गङ्गौघः, देवैश्वर्यम्, कृष्णौत्कण्ठ्यम्."""
        for text, form in (
                ("brahma eḍakā", "brahmaiḍakā"), ("khaṭvā eḍakā", "khaṭvaiḍakā"),
                ("brahma aitikāyana", "brahmaitikāyana"),
                ("brahma odana", "brahmaudana"), ("khaṭvā aupagava", "khaṭvaupagava"),
                ("kṛṣṇa-ekatvam", "kṛṣṇaikatvam"), ("gaṅgā-ogha", "gaṅgaugha"),
                ("deva-aiśvaryam", "devaiśvaryam"),
                ("kṛṣṇa-autkaṇṭhyam", "kṛṣṇautkaṇṭhyam")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.88"])
                self.assertEqual(after(text, "6.1.88"), form)

    def test_it_displaces_guna_and_says_why_in_the_kasikas_words(self):
        """Kāśikā 6.1.88: आद्गुणस्यापवादः — and the step carries it."""
        step = step_of("kṛṣṇa aikya", "6.1.88")
        self.assertIn("6.1.87", lost(step))
        self.assertIn("आद्गुणस्यापवादः (Kāśikā on 6.1.88)", lost(step)["6.1.87"])

    def test_the_vrddhi_is_the_projects_own_codification(self):
        checked = 0
        for right in ("e", "ai", "o", "au"):
            for first in ("pa", "pā"):
                text = f"{first} {right}ka"
                self.assertEqual(step_of(text, "6.1.88").detail.adesa,
                                 vrddhi_of(right), text)
                checked += 1
        self.assertEqual(checked, 8)

    def test_the_declaration_is_what_names_the_relation(self):
        """Take it away and 6.1.88 still wins by 1.4.2 (it stands later) — so the
        form is the same — but the step no longer says WHY: the Kāśikā's words are
        gone from what it displaced."""
        step = derive_with(rules_without("6.1.88", overrides=()),
                           "kṛṣṇa aikya").steps[0]
        self.assertEqual(step.sutra, "6.1.88")
        self.assertTrue(all("आद्गुणस्यापवादः" not in a.why for a in step.against))


class EtyEdhatyuthsu(unittest.TestCase):
    """6.1.89 and its vārttikas — the exception to the exception."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā उपैति, उपैषि, उपैमि, उपैधते, प्रैधते, प्रष्ठौहः; Kaumudī उपैति,
        उपैधते, प्रष्ठौहः."""
        for text, form in (
                ("upa|eti{dhatu:i}", "upaiti"), ("upa|eṣi{dhatu:i}", "upaiṣi"),
                ("upa|emi{dhatu:i}", "upaimi"), ("upa|edhate{dhatu:edh}", "upaidhate"),
                ("pra|edhate{dhatu:edh}", "praidhate"),
                ("praṣṭha ūhas{uth}", "praṣṭhauhas")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.89"])
                self.assertEqual(after(text, "6.1.89"), form)

    def test_it_displaces_pararupa_and_guna_and_says_so(self):
        """Kāśikā 6.1.89: एत्येधत्योस्त्वेङिपररूपापवादः; ऊठ्याद्गुणापवादो
        वृद्धिर्विधीयते."""
        eti = lost(step_of("upa|eti{dhatu:i}", "6.1.89"))
        self.assertIn("एत्येधत्योस्त्वेङिपररूपापवादः (Kāśikā on 6.1.89)", eti["6.1.94"])
        uth = lost(step_of("praṣṭha ūhas{uth}", "6.1.89"))
        self.assertIn("ऊठ्याद्गुणापवादो वृद्धिर्विधीयते (Kāśikā on 6.1.89)", uth["6.1.87"])

    def test_without_the_declaration_the_later_pararupa_would_have_won(self):
        """6.1.94 stands later than 6.1.89, so 1.4.2 alone would give उपेति. Take
        the declaration away and it does."""
        without = rules_without("6.1.89", overrides=())
        self.assertEqual(derive_with(without, "upa|eti{dhatu:i}").surface, "upeti")
        self.assertEqual(sandhi("upa|eti{dhatu:i}").surface, "upaiti")

    def test_ejadyoh_kim_upetah(self):
        """Kāśikā/Kaumudī एजाद्योः किम्? उपेतः — the इ of इतः is no एच्; and the
        Kaumudī's मा भवान्प्रेदिधत्: the root is एध् but the form begins with a
        short इ."""
        self.assertEqual(steps_of("upa|ita{dhatu:i}"), ["6.1.87"])
        self.assertEqual(after("upa|ita{dhatu:i}", "6.1.87"), "upeta")
        self.assertEqual(steps_of("pra|ididhat{dhatu:edh}"), ["6.1.87"])
        self.assertEqual(after("pra|ididhat{dhatu:edh}", "6.1.87"), "predidhat")

    def test_the_root_is_the_callers_word_not_the_letters(self):
        """Control: the same letters with no root flag get the general sūtras — a
        pararūpa for the preverb and dhātu, guṇa for the rest."""
        self.assertEqual(steps_of("upa|eti"), ["6.1.94"])
        self.assertEqual(after("upa|eti", "6.1.94"), "upeti")
        self.assertEqual(steps_of("praṣṭha ūhas"), ["6.1.87"])
        self.assertEqual(after("praṣṭha ūhas", "6.1.87"), "praṣṭhohas")

    def test_uth_through_the_substitute_of_6_1_108_visvauhah(self):
        """Bālamanoramā: विश्व ऊ आह् अस् इति स्थिते (the ऊ of ऊठ् and the आ of आह् join by
        6.1.108) … विश्व ऊह् असिति स्थिते आद्गुणमाशङ्क्याह — एत्येधत्यूठ्सु: विश्वौहः. The ऊठ्
        is the ū that the substitute stands for (6.1.85), so 6.1.89 reaches it though
        the flag is on the earlier piece — and 6.1.108 comes first (it stands later:
        1.4.2), as the Bālamanoramā has it."""
        for text in ("viśva ū{uth} āhas", "viśva~ū{stem:ūṭh}~āhas"):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.108", "6.1.89"])
                self.assertEqual(sandhi(text).surface, "viśvauhaḥ")
        step = step_of("viśva ū{uth} āhas", "6.1.108")
        self.assertIn("6.1.89", lost(step))                 # it wanted the ū too
        self.assertIn("1.4.2", lost(step)["6.1.89"])
        self.assertIn("6.1.87", lost(step_of("viśva ū{uth} āhas", "6.1.89")))

    def test_uth_is_asked_of_the_flag_not_of_the_letters(self):
        """Controls. A samprasāraṇa ū that is not the ऊठ् gets 6.1.108 and then guṇa;
        an ū with nothing said gets neither of them."""
        self.assertEqual(steps_of("viśva ū{samprasarana} āhas"), ["6.1.108", "6.1.87"])
        self.assertEqual(sandhi("viśva ū{samprasarana} āhas").surface, "viśvohaḥ")
        text = "viśva ū āhas"
        self.assertNotIn("6.1.108", steps_of(text))
        self.assertNotIn("6.1.89", steps_of(text))

    def test_it_does_not_displace_6_1_95(self):
        """Kāśikā: ओमाङोश्च इत्येतत् तु पररूपं न बाध्यते — पुरस्तादपवादा अनन्तरान् विधीन्
        बाधन्ते नोत्तरान्; उप आ इत उपेतः. Kaumudī: तेनावैहीति वृद्धिरसाधुरेव. So *अव
        एहि* — where एहि begins with the एकादेश of आङ् and इहि, and is a form of √इ —
        is अवेहि: 6.1.95, the later, takes the place from 6.1.89."""
        text = "ava ehi{ang,dhatu:i}"
        self.assertEqual(steps_of(text), ["6.1.95"])
        self.assertEqual(after(text, "6.1.95"), "avehi")
        step = step_of(text, "6.1.95")
        self.assertIn("6.1.89", lost(step))
        self.assertIn("1.4.2", lost(step)["6.1.89"])
        rule89 = next(r for r in fam.RULES if r.sutra == "6.1.89" and not r.varttika)
        self.assertNotIn("6.1.95", [t for t, _ in rule89.overrides])
        self.assertNotIn("6.1.96", [t for t, _ in rule89.overrides])

    def test_the_vartikas_of_6_1_89_kasika_and_kaumudi(self):
        """अक्षादूहिन्यामुपसंख्यानम् (अक्षौहिणी), स्वादीरेरिणोः (स्वैरम्, स्वैरी),
        प्रादूहोढोढ्येषैष्येषु (प्रौहः, प्रौढः, प्रौढिः, प्रैषः, प्रैष्यः), ऋते च
        तृतीयासमासे (सुखार्तः), प्रवत्सतरकम्बलवसनार्णदशानामृणे (प्रार्णम्,
        वत्सतरार्णम्, कम्बलार्णम्, वसनार्णम्, ऋणार्णम्, दशार्णम्)."""
        for text, form, varttika in (
                ("akṣa-ūhinī", "akṣauhinī", fam.V_AKSAT_UHINYAM),
                ("sva-īra", "svaira", fam.V_SVADIRERINOH),
                ("sva-īrin", "svairin", fam.V_SVADIRERINOH),
                ("sva-īriṇī{stem:īrin}", "svairiṇī", fam.V_SVADIRERINOH),
                ("pra-ūha", "prauha", fam.V_PRADUHODHODHYESAISYESU),
                ("pra-ūḍha", "prauḍha", fam.V_PRADUHODHODHYESAISYESU),
                ("pra-ūḍhi", "prauḍhi", fam.V_PRADUHODHODHYESAISYESU),
                ("pra-eṣa{krdanta}", "praiṣa", fam.V_PRADUHODHODHYESAISYESU),
                ("pra-eṣya{krdanta}", "praiṣya", fam.V_PRADUHODHODHYESAISYESU),
                ("sukha{trtiya}-ṛta", "sukhārta", fam.V_RTE_TRTIYASAMASE),
                ("pra-ṛṇam{stem:ṛṇa}", "prārṇam", fam.V_PRAVATSATARA),
                ("vatsatara-ṛṇa", "vatsatarārṇa", fam.V_PRAVATSATARA),
                ("kambala-ṛṇa", "kambalārṇa", fam.V_PRAVATSATARA),
                ("vasana-ṛṇa", "vasanārṇa", fam.V_PRAVATSATARA),
                ("ṛṇa-ṛṇa", "ṛṇārṇa", fam.V_PRAVATSATARA),
                ("daśa-ṛṇa", "daśārṇa", fam.V_PRAVATSATARA)):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.89"])
                step = step_of(text, "6.1.89")
                self.assertEqual(step.detail.authority, "vārttika")
                self.assertEqual(step.detail.varttika, varttika)
                self.assertEqual(after(text, "6.1.89"), form)

    def test_the_vartikas_counter_examples(self):
        """Without the word the vārttika names, the general sūtras act — and the
        Kāśikā's own contrasts: ऊढवत् (प्रोढवान्; अर्थवद्ग्रहणे नानर्थकस्य ग्रहणम्),
        ईष (प्रेषः), परमर्तः (तृतीयेति किम्), सुखेनर्तः (समास इति किम्), सुखेतः
        (ऋत इति किम्), and the Bālamanoramā's प्रेष्य गतः (the lyabanta)."""
        for text, form, general in (
                ("pra-ūḍhavān", "proḍhavān", "6.1.87"),
                ("pra-īṣa", "preṣa", "6.1.87"),
                ("parama-ṛta", "paramarta", "6.1.87"),
                ("sukha ṛta", "sukharta", "6.1.87"),
                ("sukha{trtiya}-ita", "sukheta", "6.1.87"),
                ("pra-eṣya", "praiṣya", "6.1.88"),
                ("akṣa-ūha", "akṣoha", "6.1.87")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), [general])
                self.assertEqual(after(text, general), form)
        # प्रेष्य गतः — the dhātu's form after a preverb, no kṛdanta: 6.1.94
        self.assertEqual(steps_of("pra|eṣya"), ["6.1.94"])
        self.assertEqual(after("pra|eṣya", "6.1.94"), "preṣya")

    def test_a_vartika_before_an_eng_word_displaces_6_1_94(self):
        """Bālamanoramā: प्र एष प्र एष्य इति स्थिते एङि पररूपं बाधित्वाऽनेन वृद्धिः —
        with the preverb and the dhātu named too, the vārttika is what is done."""
        text = "pra|eṣa{krdanta}"
        self.assertEqual(steps_of(text), ["6.1.89"])
        step = step_of(text, "6.1.89")
        self.assertEqual(step.detail.authority, "vārttika")
        self.assertIn("बाधित्वाऽनेन वृद्धिः", lost(step)["6.1.94"])


class AtasCa(unittest.TestCase):
    """6.1.90 आटश्च."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā ऐक्षिष्ट, ऐक्षत, ऐक्षिष्यत, औभीत्, आर्ध्नोत्, औब्जीत्, औस्रीयत्."""
        for text, form in (
                ("ā{aat}~īkṣiṣṭa", "aikṣiṣṭa"), ("ā{aat}~īkṣata", "aikṣata"),
                ("ā{aat}~īkṣiṣyata", "aikṣiṣyata"), ("ā{aat}~ubhīt", "aubhīt"),
                ("ā{aat}~ṛdhnot", "ārdhnot"), ("ā{aat}~ubjīt", "aubjīt"),
                ("ā{aat}~usrīyat", "ausrīyat")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.90"])
                self.assertEqual(after(text, "6.1.90"), form)

    def test_bahusreyasyai_the_augment_after_a_long_i(self):
        """Kaumudī: बहुश्रेयसी आ ए → बहुश्रेयस्यै, बहुश्रेयस्याः (6.1.77 for the ई)."""
        r = sandhi("bahuśreyasī~ā{aat}~e{sup:ṅe}")
        self.assertEqual(r.surface, "bahuśreyasyai")
        # the augment and the ending's vowel first, the yaṇ after — the
        # Bālamanoramā's order: आटश्चेति वृद्धौ यणादेशे च रूपम्
        self.assertEqual(steps_of("bahuśreyasī~ā{aat}~e{sup:ṅe}"), ["6.1.90", "6.1.77"])
        self.assertEqual(sandhi("bahuśreyasī~ā{aat}~as{sup:ṅas}").surface[:12],
                         "bahuśreyasyā")

    def test_the_augment_is_the_callers_word(self):
        """Control: the same letters as an ordinary ā get guṇa (आद्गुणः)."""
        self.assertEqual(steps_of("ā~īkṣata"), ["6.1.87"])
        self.assertEqual(after("ā~īkṣata", "6.1.87"), "ekṣata")

    def test_the_ca_displaces_6_1_96_and_says_so(self):
        """Kāśikā 6.1.90: चकारोऽधिकविधानार्थः, उसि॰, ओमाङोश्च इति पररूपबाधनार्थः —
        औस्रीयत्. 6.1.96 stands LATER, so without the declaration it wins."""
        step = step_of("ā{aat}~usrīyat", "6.1.90")
        self.assertIn("6.1.96", lost(step))
        self.assertIn("इति पररूपबाधनार्थः (Kāśikā on 6.1.90)", lost(step)["6.1.96"])
        without = rules_without("6.1.90", overrides=())
        self.assertEqual(vowel_steps(derive_with(without, "ā{aat}~usrīyat")), ["6.1.96"])

    def test_the_ca_displaces_6_1_95_too(self):
        """The same words for 6.1.95 (Kāśikā औङ्कारीयत्); here the particle ओम्
        follows the augment."""
        text = "ā{aat}~om{nipata}"
        self.assertEqual(steps_of(text), ["6.1.90"])
        self.assertEqual(after(text, "6.1.90"), "aum")
        self.assertIn("6.1.95", lost(step_of(text, "6.1.90")))
        without = rules_without("6.1.90", overrides=())
        self.assertEqual(vowel_steps(derive_with(without, text)), ["6.1.95"])


class UpasargadRti(unittest.TestCase):
    """6.1.91 उपसर्गादृति धातौ and 6.1.92 वा सुप्यापिशलेः."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā उपार्च्छति, प्रार्च्छति, उपार्ध्नोति; Laghukaumudī प्रार्च्छति."""
        for text, form in (("upa|ṛcchati", "upārcchati"), ("pra|ṛcchati", "prārcchati"),
                           ("upa|ṛdhnoti", "upārdhnoti")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.91"])
                self.assertEqual(after(text, "6.1.91"), form)
                self.assertIn("1.1.51", step_of(text, "6.1.91").sutras)

    def test_it_displaces_guna(self):
        step = step_of("pra|ṛcchati", "6.1.91")
        self.assertIn("आद्गुणापवादः (Kāśikā on 6.1.91)", lost(step)["6.1.87"])

    def test_upasargat_kim_and_rti_kim_and_dhatau_kim(self):
        """Kāśikā उपसर्गात् किम्? खट्वर्च्छति, मालर्च्छति, प्रर्च्छको देशः (the प्र that
        goes with no verb); ऋति किम्? उपेतः; Tattvabodhinī धातौ किम्? उपर्कारः."""
        for text, form in (("khaṭvā ṛcchati", "khaṭvarcchati"),
                           ("mālā ṛcchati", "mālarcchati"),
                           ("pra-ṛcchaka", "prarcchaka"),
                           ("upa-ṛkāra", "uparkāra")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.87"])
                self.assertEqual(after(text, "6.1.87"), form)
        self.assertEqual(steps_of("upa|ita"), ["6.1.87"])

    def test_the_preverb_is_the_callers_word(self):
        """`pra` flagged a preverb and its dhātu flagged, on a space; and the same
        two words with nothing said are not one."""
        self.assertEqual(steps_of("pra{upasarga} ṛcchati{dhatu:ṛ}"), ["6.1.91"])
        self.assertEqual(steps_of("pra ṛcchati"), ["6.1.87"])

    def test_taparakarana_the_long_r_is_not_reached(self):
        """Kāśikā तपरकरणं किम्? उप ॠकारीयति उपर्कारीयति."""
        for text in ("upa|ṝkārīyati", "upa|ṝkārīyati{subanta}"):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.87"])
                self.assertEqual(after(text, "6.1.87"), "uparkārīyati")

    def test_the_option_of_a_subanta_dhatu(self):
        """Kāśikā उपर्षभीयति, उपार्षभीयति; उपल्कारीयति, उपाल्कारीयति; Kaumudī
        प्रार्षभीयति, प्रर्षभीयति, प्राल्कारीयति, प्रल्कारीयति."""
        for text, taken, declined in (
                ("upa|ṛṣabhīyati{subanta}", "upārṣabhīyati", "uparṣabhīyati"),
                ("pra|ṛṣabhīyati{subanta}", "prārṣabhīyati", "prarṣabhīyati"),
                ("upa|ḷkārīyati{subanta}", "upālkārīyati", "upalkārīyati"),
                ("pra|ḷkārīyati{subanta}", "prālkārīyati", "pralkārīyati")):
            with self.subTest(text=text):
                r = sandhi(text)
                self.assertEqual(r.surfaces, (taken, declined))       # taken first
                self.assertEqual(vowel_steps(r.outcomes[0]), ["6.1.92"])
                self.assertEqual(r.outcomes[0].choices[-1], ("6.1.92", True))
                # the declined course is guṇa — and NOT 6.1.91 come back
                self.assertEqual(vowel_steps(r.outcomes[1]), ["6.1.87"])
                self.assertEqual(r.outcomes[1].choices[-1], ("6.1.92", False))
                self.assertEqual(after(text, "6.1.87", k=1), declined)

    def test_without_a_subanta_it_is_not_optional(self):
        self.assertEqual(len(sandhi("upa|ṛcchati").outcomes), 1)

    def test_6_1_92_is_a_vibhasa_and_says_which_it_displaces(self):
        step = step_of("upa|ṛṣabhīyati{subanta}", "6.1.92")
        self.assertEqual(step.option, "वा")
        self.assertIn("उपर्षभीयति, उपार्षभीयति (Kāśikā on 6.1.92)", lost(step)["6.1.87"])
        rule92 = next(r for r in fam.RULES if r.sutra == "6.1.92")
        why = dict(rule92.overrides)["6.1.91"]
        self.assertIn("वा सुप्यापिशलेः इति विकल्पः स्यात् (Kāśikā on 6.1.91)", why)


class AutoMSasoh(unittest.TestCase):
    """6.1.93 औतोऽम्शसोः."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā गां पश्य, गाः पश्य, द्यां पश्य, द्याः पश्य; Kaumudī गाम्, गाः, स्मृताम्
        (the ā is one sound, for the o and the a together)."""
        for text, form in (("go~am{sup:am}", "gām"), ("go~as{sup:śas}", "gās"),
                           ("dyo~am{sup:am}", "dyām"), ("dyo~as{sup:śas}", "dyās"),
                           ("smṛto~am{sup:am}", "smṛtām")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.93"])
                self.assertEqual(after(text, "6.1.93"), form)
        self.assertEqual(sandhi("go~as{sup:śas}").surface, "gāḥ")

    def test_acinavam_asunavam_the_tense_ending_is_not_am_of_the_case(self):
        """Kāśikā अमिति द्वितीयैकवचनं गृह्यते … तेनाचिनवमसुनवमित्यत्र न भवति."""
        for text, form in (("acino~am", "acinavam"), ("asuno~am", "asunavam")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.78"])
                self.assertEqual(sandhi(text).surface, form)

    def test_the_ending_is_the_callers_word(self):
        """Kaumudī गवा, गवे (not गा) — the ā is for am and śas only."""
        self.assertEqual(sandhi("go~ā{sup:ṭā}").surface, "gavā")
        self.assertEqual(sandhi("go~e{sup:ṅe}").surface, "gave")
        self.assertNotIn("6.1.93", steps_of("go~as{sup:jas}"))
        self.assertNotIn("6.1.93", steps_of("go~as"))

    def test_ota_is_taparah_only_the_sound_o(self):
        """Balamanoramā: 'ओत' इति तपरकरणम् — ओकारादित्यर्थः. औ before अम् is not it:
        नाव् + अम्, नावम्."""
        self.assertEqual(steps_of("nau~am{sup:am}"), ["6.1.78"])
        self.assertEqual(sandhi("nau~am{sup:am}").surface, "nāvam")

    def test_it_stands_later_than_6_1_78_and_so_takes_the_place(self):
        step = step_of("go~am{sup:am}", "6.1.93")
        self.assertIn("6.1.78", lost(step))
        self.assertIn("1.4.2", lost(step)["6.1.78"])


class EngiPararupam(unittest.TestCase):
    """6.1.94 एङि पररूपम् and its vārttikas."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā उपेलयति, प्रेलयति, उपोषति, प्रोषति; Laghukaumudī प्रेजते, उपोषति."""
        for text, form in (("upa|elayati", "upelayati"), ("pra|elayati", "prelayati"),
                           ("upa|oṣati", "upoṣati"), ("pra|oṣati", "proṣati"),
                           ("pra|ejate", "prejate")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.94"])
                self.assertEqual(after(text, "6.1.94"), form)

    def test_it_displaces_vrddhi_and_says_so(self):
        """Kāśikā 6.1.94: वृद्धिरेचि इत्यस्यापवादः."""
        step = step_of("pra|ejate", "6.1.94")
        self.assertIn("वृद्धिरेचि इत्यस्यापवादः (Kāśikā on 6.1.94)", lost(step)["6.1.88"])

    def test_the_preverb_and_the_dhatu_are_the_callers_words(self):
        """Control: the same letters with no preverb — vṛddhi."""
        self.assertEqual(steps_of("pra ejate"), ["6.1.88"])
        self.assertEqual(after("pra ejate", "6.1.88"), "praijate")

    def test_the_option_of_a_subanta_dhatu_by_vakyabheda(self):
        """Kaumudī: वासुपीत्यनुवर्त्य वाक्यभेदेन व्याख्येयम् … एङादौ सुब्धातौ वा —
        उपेडकीयति, उपैडकीयति; प्रोघीयति, प्रौघीयति; Kāśikā उपोदनीयति, उपौदनीयति."""
        for text, taken, declined in (
                ("upa|eḍakīyati{subanta}", "upeḍakīyati", "upaiḍakīyati"),
                ("upa|odanīyati{subanta}", "upodanīyati", "upaudanīyati"),
                ("pra|oghīyati{subanta}", "proghīyati", "praughīyati")):
            with self.subTest(text=text):
                r = sandhi(text)
                self.assertEqual(r.surfaces, (taken, declined))
                self.assertEqual(vowel_steps(r.outcomes[0]), ["6.1.94"])
                self.assertEqual(vowel_steps(r.outcomes[1]), ["6.1.88"])   # the declined
        self.assertEqual(len(sandhi("upa|elayati").outcomes), 1)

    def test_eve_caniyoge(self):
        """Kāśikā इह एव इहेव, अद्य एव अद्येव; Kaumudī क्व एव → क्वेव; अनियोगे किम्?
        इहैव भव, तवैव (the restrictive एव: 6.1.88)."""
        for text, form in (("iha eva{aniyoga}", "iheva"), ("adya eva{aniyoga}", "adyeva"),
                           ("kva eva{aniyoga}", "kveva")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.94"])
                self.assertEqual(step_of(text, "6.1.94").detail.varttika, fam.V_EVE_CANIYOGE)
                self.assertEqual(after(text, "6.1.94"), form)
        for text, form in (("iha eva", "ihaiva"), ("tava eva", "tavaiva")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.88"])
                self.assertEqual(after(text, "6.1.88"), form)

    def test_otvosthayoh_samase_va(self):
        """Kāśikā स्थूल ओतुः स्थूलौतुः, स्थूलोतुः; बिम्बौष्ठी, बिम्बोष्ठी; समास इति किम्?
        तिष्ठ देवदत्तौष्ठं पश्य. Bālamanoramā: बाधित्वा पाक्षिकं पररूपम्."""
        for text, taken, declined in (("sthūla-otu", "sthūlotu", "sthūlautu"),
                                      ("bimba-oṣṭha", "bimboṣṭha", "bimbauṣṭha")):
            with self.subTest(text=text):
                r = sandhi(text)
                self.assertEqual(r.surfaces, (taken, declined))
                self.assertEqual(vowel_steps(r.outcomes[0]), ["6.1.94"])
                self.assertEqual(vowel_steps(r.outcomes[1]), ["6.1.88"])
        # the counter-case: two words, not a compound. The second is given as its
        # stem (or flagged as one) — were it left as `oṣṭham`, the vārttika's word
        # would not match and the samāsa condition would never be put to the test.
        for text in ("devadatta oṣṭha", "devadatta oṣṭham{stem:oṣṭha}"):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.88"])
                self.assertEqual(len(sandhi(text).outcomes), 1)
        step = step_of("sthūla-otu", "6.1.94")
        self.assertIn("बाधित्वा पाक्षिकं पररूपम् (Bālamanoramā on 6.1.94)",
                      lost(step)["6.1.88"])

    def test_emannadisu_chandasi_is_vedic_only(self):
        """Kāśikā अपां त्वा एमन्, अपां त्वेमन्; अपां त्वा ओद्मन्, अपां त्वोद्मन्."""
        self.assertEqual(sandhi("tvā eman", veda=True).surface, "tveman")
        self.assertEqual(sandhi("tvā odman", veda=True).surface, "tvodman")
        self.assertEqual(sandhi("tvā eman").surface, "tvaiman")

    def test_sakandhvadisu_pararupam_of_the_ti(self):
        """Laghukaumudī शकन्ध्वादिषु पररूपं वाच्यम्, तच्च टेः — शकन्धुः, कर्कन्धुः, मनीषा;
        Bālamanoramā कुलटा, हलीषा, लाङ्गलीषा, पतञ्जलिः, सीमन्तः केशवेशे, सारङ्गः
        पशुपक्षिणोः. The ṭi (1.1.64) goes with the vowel that follows."""
        for text, form in (
                ("śaka-andhu", "śakandhu"), ("karka-andhu", "karkandhu"),
                ("kula-aṭā", "kulaṭā"), ("manas-īṣā", "manīṣā"),
                ("hala-īṣā", "halīṣā"), ("lāṅgala-īṣā", "lāṅgalīṣā"),
                ("patat-añjali", "patañjali"),
                ("sīman{keśaveśe}-anta", "sīmanta"),
                ("sāra{paśupakṣiṇoḥ}-aṅga", "sāraṅga")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.94"])
                step = step_of(text, "6.1.94")
                self.assertEqual(step.detail.varttika, fam.V_SAKANDHVADISU)
                self.assertIn("1.1.64", step.sutras)
                self.assertEqual(after(text, "6.1.94"), form)

    def test_the_ti_goes_and_not_only_the_vowel(self):
        """मनस् + ईषा is मन् + ई: the s is not left (it would be 8.2.66's ru)."""
        self.assertEqual(step_of("manas-īṣā", "6.1.94").detail.sthanin
                         .replace("{", "").replace("}", ""), "as+ī")
        self.assertEqual(sandhi("manas-īṣā").surface, "manīṣā")

    def test_sakandhvadi_counters_and_the_senses_of_the_two_restricted_entries(self):
        """Kāśikā सीमन्तः केशेषु … अन्यत्र सीमान्तः (सीमा + अन्त); Bālamanoramā:
        सारङ्गः is the deer or the bird — the other सार-अङ्ग is सारांग."""
        self.assertEqual(steps_of("sīmā-anta"), ["6.1.101"])
        self.assertEqual(after("sīmā-anta", "6.1.101"), "sīmānta")
        self.assertEqual(steps_of("sāra-aṅga"), ["6.1.101"])         # no sense given
        self.assertEqual(after("sāra-aṅga", "6.1.101"), "sārāṅga")
        self.assertEqual(steps_of("dhana-anta"), ["6.1.101"])         # not on the list

    def test_the_sakandhvadi_vartika_displaces_savarna_dirgha_by_declaration(self):
        """6.1.101 stands later, so only the declaration gives सारङ्गः."""
        without = rules_without("6.1.94", fam.V_SAKANDHVADISU, overrides=())
        self.assertEqual(derive_with(without, "sāra{paśupakṣiṇoḥ}-aṅga").surface, "sārāṅga")
        self.assertEqual(sandhi("sāra{paśupakṣiṇoḥ}-aṅga").surface, "sāraṅga")


class OmangoCa(unittest.TestCase):
    """6.1.95 ओमाङोश्च."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā का ओमित्यवोचत् कोमित्यवोचत्; आ ऊढा ओढा, अद्य ओढा अद्योढा, कदा ओढा
        कदोढा, तदा ओढा तदोढा; Kaumudī शिवायों नमः."""
        for text, form in (("kā om{nipata}", "kom"), ("adya oḍhā{ang}", "adyoḍhā"),
                           ("kadā oḍhā{ang}", "kadoḍhā"), ("tadā oḍhā{ang}", "tadoḍhā"),
                           ("śivāya om{nipata}", "śivāyom")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.95"])
                self.assertEqual(after(text, "6.1.95"), form)

    def test_the_whole_kasika_sentence(self):
        """का ओमित्यवोचत् → कोमित्यवोचत् — through the following इति and अवोचत्."""
        self.assertTrue(sandhi("kā om{nipata} iti avocat").surface
                        .startswith("komityavoca"))

    def test_the_particle_and_the_preverb_are_the_callers_words(self):
        """Control: an ओ-initial word that is not the particle, and one that is not
        आङ्: the sūtra does not reach them (6.1.88)."""
        # `om` is the particle wherever it stands, and infer.py reads it so
        # (a closed list) — so the control for "not the particle" is another word.
        self.assertEqual(steps_of("kā om"), ["6.1.95"])
        self.assertEqual(steps_of("kā oṣadhi"), ["6.1.88"])
        self.assertEqual(after("kā oṣadhi", "6.1.88"), "kauṣadhi")
        self.assertEqual(steps_of("adya oḍhā"), ["6.1.88"])
        self.assertEqual(after("adya oḍhā", "6.1.88"), "adyauḍhā")

    def test_the_kasikas_contrast_with_savarnadirgha(self):
        """Kāśikā इह तु आ ऋश्यात् अर्श्यात्, अद्य अर्श्यात् अद्यर्श्यादिति अकः सवर्णे
        दीर्घत्वं बाधते — the आङ् is what stops the long ā."""
        step = step_of("adya arśyāt{ang}", "6.1.95")
        self.assertEqual(after("adya arśyāt{ang}", "6.1.95"), "adyarśyāt")
        self.assertIn("अकः सवर्णे दीर्घत्वं बाधते (Kāśikā on 6.1.95)", lost(step)["6.1.101"])
        self.assertEqual(steps_of("adya arśyāt"), ["6.1.101"])
        self.assertEqual(after("adya arśyāt", "6.1.101"), "adyārśyāt")
        without = rules_without("6.1.95", overrides=())
        self.assertEqual(vowel_steps(derive_with(without, "adya arśyāt{ang}")), ["6.1.101"])

    def test_sivehi_by_6_1_95_and_6_1_85(self):
        """Laghukaumudī शिव एहि under 6.1.95, शिवेहि under 6.1.85 (योऽयमेकादेशः स
        पूर्वस्यान्तवत्परस्यादिवत्). The ए of एहि is the guṇa that आङ् and इहि made; it
        is the END of आङ् (6.1.85), which is one sound, so it is आङ् — and the step
        cites 6.1.85."""
        text = "śiva ehi{ang}"
        self.assertEqual(steps_of(text), ["6.1.95"])
        self.assertEqual(after(text, "6.1.95"), "śivehi")
        step = step_of(text, "6.1.95")
        self.assertIn("6.1.85", step.sutras)
        self.assertIn("6.1.88", lost(step))
        self.assertEqual(steps_of("śiva ehi"), ["6.1.88"])            # no आङ्: vṛddhi
        self.assertEqual(after("śiva ehi", "6.1.88"), "śivaihi")

    def test_the_substitute_of_the_preverb_and_the_dhatu_counts_as_the_preverb(self):
        """6.1.85 (योऽयमेकादेशः स पूर्वस्यान्तवत्): once आङ् and इहि have made their
        ए — the Bālamanoramā's order, the inner sandhi first — that ए stands as the
        end of आङ्, and आङ् is one sound. Asked of the state after that step, so that
        the earlier word is the one the substitute remembers (`Seg.lw`), and not of
        a word that carries the flag itself."""
        for flagged, offered in (("śiva ā{ang} ihi", True), ("śiva ā ihi", False)):
            with self.subTest(text=flagged):
                state = parse(flagged)
                rules = STAGE
                inner = next((r, a) for r, a in collect(state, rules)
                             if r.sutra == "6.1.87"
                             and any(seg.uid in a.site and seg.s == "i"
                                     for seg in state.segs))
                state = apply(state, *inner)
                made = [seg for seg in state.segs if seg.made_by == "6.1.87"]
                self.assertEqual([(seg.s, seg.w, seg.lw) for seg in made], [("e", 2, 1)])
                found = [r.sutra for r, a in collect(state, rules)
                         if made[0].uid in a.site]
                self.assertEqual("6.1.95" in found, offered)

    def test_the_preverb_and_its_dhatu_in_three_words_give_the_same_form(self):
        """शिव आ इहि: 6.1.95 at the first junction, then guṇa — the tradition's
        order is the other (एहि is made first), and the form is the same."""
        self.assertEqual(sandhi("śiva ā{ang} ihi").surface, "śivehi")
        self.assertEqual(steps_of("śiva ā{ang} ihi"), ["6.1.95", "6.1.87"])
        self.assertEqual(sandhi("ava ā{ang} ihi").surface, "avehi")


class UsyApadantat(unittest.TestCase):
    """6.1.96 उस्यपदान्तात्."""

    def test_the_kasikas_and_laghukaumudis_examples(self):
        """Kāśikā भिन्द्या उस् भिन्द्युः, छिन्द्या उस् छिन्द्युः, अदा उस् अदुः, अया उस्
        अयुः."""
        for text, form in (("bhindyā~us", "bhindyus"), ("chindyā~us", "chindyus"),
                           ("adā~us", "adus"), ("ayā~us", "ayus")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.96"])
                self.assertEqual(after(text, "6.1.96"), form)

    def test_apadantat_kim_and_aditye_va(self):
        """Kāśikā अपदान्तादिति किम्? का उस्रा कोस्रा; आदित्येव — चक्रुः."""
        self.assertEqual(steps_of("kā usrā"), ["6.1.87"])
        self.assertEqual(after("kā usrā", "6.1.87"), "kosrā")
        self.assertEqual(steps_of("cakṛ~us"), ["6.1.77"])
        self.assertEqual(sandhi("cakṛ~us").surface, "cakruḥ")

    def test_it_displaces_guna(self):
        step = step_of("bhindyā~us", "6.1.96")
        self.assertIn("पूर्वपरयोराद्गुणापवादः पररूपमेकादेशो भवति (Kāśikā on 6.1.96)",
                      lost(step)["6.1.87"])


class AtoGune(unittest.TestCase):
    """6.1.97 अतो गुणे."""

    def test_the_kasikas_examples(self):
        """Kāśikā पचन्ति, यजन्ति, and (पचे, यज इत्यत्र वृद्धिः प्राप्नोति) पचे, यजे."""
        for text, form in (("paca~anti", "pacanti"), ("yaja~anti", "yajanti"),
                           ("paca~e", "pace"), ("yaja~e", "yaje")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.97"])
                self.assertEqual(after(text, "6.1.97"), form)

    def test_the_exception_to_savarnadirgha_and_the_words(self):
        """Kāśikā: अकः सवर्णे दीर्घस्य अपवादः — and पचे, यज इत्यत्र वृद्धिरेचि इति
        वृद्धिः प्राप्नोति."""
        step = step_of("paca~anti", "6.1.97")
        self.assertIn("अकः सवर्णे दीर्घस्य अपवादः (Kāśikā on 6.1.97)", lost(step)["6.1.101"])
        self.assertIn("6.1.88", lost(step_of("paca~e", "6.1.97")))

    def test_without_the_declaration_the_later_savarnadirgha_would_win(self):
        """6.1.101 stands later; only the declaration gives पचन्ति, not पचान्ति
        (the Kāśikā's own: 6.1.101 would give it)."""
        without = rules_without("6.1.97", overrides=())
        self.assertEqual(derive_with(without, "paca~anti").surface, "pacānti")
        self.assertEqual(sandhi("paca~anti").surface, "pacanti")

    def test_ata_kim_guna_kim_apadantat_kim(self):
        """Kāśikā अत इति किम्? यान्ति, वान्ति; गुण इति किम्? अपचे, अयजे;
        अपदान्तादित्येव — दण्डाग्रम्, यूपाग्रम्."""
        for text, form, sutra in (
                ("yā~anti", "yānti", "6.1.101"), ("vā~anti", "vānti", "6.1.101"),
                ("apaca~i", "apace", "6.1.87"), ("ayaja~i", "ayaje", "6.1.87"),
                ("daṇḍa-agram", "daṇḍāgram", "6.1.101"),
                ("yūpa-agram", "yūpāgram", "6.1.101")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), [sutra])
                self.assertEqual(after(text, sutra), form)

    def test_it_does_not_displace_purvasavarnadirgha(self):
        """Kaumudī: पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते नोत्तरान् — अकः सवर्णे इत्यस्यैव
        अपवादो न तु प्रथमयोः: रामाः. With the case ending named, 6.1.102 (later)
        is done; 6.1.97 declares nothing against it."""
        text = "rāma~as{sup:jas}"
        self.assertEqual(steps_of(text), ["6.1.102"])
        self.assertEqual(after(text, "6.1.102"), "rāmās")
        step = step_of(text, "6.1.102")
        self.assertIn("6.1.97", lost(step))
        self.assertIn("1.4.2", lost(step)["6.1.97"])
        rule97 = next(r for r in fam.RULES if r.sutra == "6.1.97")
        self.assertNotIn("6.1.102", [t for t, _ in rule97.overrides])
        self.assertEqual(steps_of("rāma~as"), ["6.1.97"])     # no ending named: 6.1.97's

    def test_the_pair_is_asked_of_anga_ato_gune(self):
        for right in ("a", "e", "o", "i", "ai", "ā"):
            with self.subTest(right=right):
                asked = ato_gune("a", right).result
                self.assertEqual("6.1.97" in steps_of(f"paca~{right}ka"), asked is not None)


class AvyaktaAnukarana(unittest.TestCase):
    """6.1.98–6.1.100."""

    def test_the_kasikas_examples_of_6_1_98(self):
        """Kāśikā पटत् इति पटिति, घटत् इति घटिति, झटत् इति झटिति, छमत् इति छमिति."""
        for text, form in (("paṭat{avyakta} iti", "paṭiti"),
                           ("ghaṭat{avyakta} iti", "ghaṭiti"),
                           ("jhaṭat{avyakta} iti", "jhaṭiti"),
                           ("chamat{avyakta} iti", "chamiti")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.98"])
                self.assertEqual(after(text, "6.1.98"), form)

    def test_6_1_98_counter_examples(self):
        """Kāśikā अव्यक्तानुकरणस्येति किम्? जगत् इति जगदिति; अत इति किम्? मरट् इति
        मरडिति; इताविति किम्? पटत् अत्र पटदत्र."""
        for text, form in (("jagat iti", "jagaditi"), ("maraṭ{avyakta} iti", "maraḍiti"),
                           ("paṭat{avyakta} atra", "paṭadatra")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), [])
                self.assertEqual(sandhi(text).surface, form)

    def test_the_word_after_it_is_iti_and_no_other_i_word(self):
        """Kāśikā इताविति किम्? — the word that follows is *iti* (तस्य योऽच्छब्दस्तस्मादितौ),
        not any word that begins with an इ. Its counter-example पटत् अत्र has an अ,
        which would fail on the letter alone; these two have the इ and are not *iti*."""
        for text in ("paṭat{avyakta} idam", "paṭat{avyakta} iha"):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), [])
                self.assertTrue(sandhi(text).surface.startswith("paṭad"))

    def test_the_vartika_ekaco_na(self):
        """Kāśikā अनेकाच इति वक्तव्यम्, इह मा भूत् श्रत् इति श्रदिति; Kaumudī एकाचो न.
        The refusal is a step, done once, and the t is then treated as any other's."""
        text = "śrat{avyakta} iti"
        out = run(text)
        refusal = step_of(text, "6.1.98")
        self.assertEqual(refusal.detail.kind, "pratiṣedha")
        self.assertEqual(refusal.detail.varttika, fam.V_EKACO_NA)
        self.assertEqual(refusal.before, refusal.after)
        self.assertEqual(out.surface, "śraditi")
        self.assertEqual([s.sutra for s in out.steps if not s.declined],
                         ["6.1.98", "8.2.39"])
        self.assertIn("6.1.98", lost(refusal))
        self.assertIn("अनेकाच इति वक्तव्यम् (Kāśikā on 6.1.98)", lost(refusal)["6.1.98"])

    def test_the_whole_pair_goes_because_the_imitation_is_meaningless(self):
        """Bālamanoramā: नानर्थकेऽलोऽन्त्यविधिः — the sthānin is the whole `at` and
        the इ, three sounds for one."""
        step = step_of("paṭat{avyakta} iti", "6.1.98")
        self.assertEqual(step.detail.sthanin.replace("{", "").replace("}", ""), "at+i")
        self.assertEqual(step.detail.adesa.split()[0], "i")

    def test_6_1_99_the_repeated_member_option(self):
        """Kāśikā पटत्पटदिति, पटत्पटेति करोति — the t alone may take the pararūpa,
        which is left as अ + इ, and 6.1.87 makes ए."""
        text = "paṭat{avyakta,amredita} iti"
        r = sandhi(text)
        self.assertEqual(r.surfaces, ("paṭeti", "paṭaditi"))
        self.assertEqual(vowel_steps(r.outcomes[0]), ["6.1.99", "6.1.87"])
        self.assertEqual(vowel_steps(r.outcomes[1]), [])
        self.assertEqual(r.outcomes[0].choices[-1], ("6.1.99", True))
        self.assertEqual(r.outcomes[1].choices[-1], ("6.1.99", False))

    def test_6_1_99_the_pararupa_of_the_whole_at_is_refused_for_the_repeated_member(self):
        """Kāśikā …तस्य पररूपं न भवति — never पटत्पटिति for the repeated member; and
        where the whole doubled thing is imitated (समुदायानुकरणम्), 6.1.98 stands:
        पटत्पटिति करोति."""
        for out in sandhi("paṭat{avyakta,amredita} iti").outcomes:
            self.assertNotIn("6.1.98", [s.sutra for s in out.steps])
        self.assertEqual(sandhi("paṭatpaṭat{avyakta} iti").surface, "paṭatpaṭiti")

    def test_6_1_100_before_dac(self):
        """Kāśikā पटपटा करोति, दमदमा करोति."""
        for text, form in (
                ("paṭat{avyakta} paṭā{avyakta,amredita,dac}", "paṭapaṭā"),
                ("damat{avyakta} damā{avyakta,amredita,dac}", "damadamā")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.100"])
                self.assertEqual(after(text, "6.1.100"), form)
                self.assertEqual(sandhi(text).surface, form)

    def test_6_1_100_needs_the_dac(self):
        """Control: the same two words without ḍāc are not the sūtra's."""
        out = run("paṭat{avyakta} paṭā{avyakta,amredita}")
        self.assertNotIn("6.1.100", [s.sutra for s in out.steps])


class AkahSavarne(unittest.TestCase):
    """6.1.101 अकः सवर्णे दीर्घः — the general rule among alike sounds."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā दण्डाग्रम्, दधीन्द्रः, मधूदके; Kaumudī दैत्यारिः, श्रीशः, विष्णूदयः."""
        for text, form in (
                ("daṇḍa-agram", "daṇḍāgram"), ("dadhi indra", "dadhīndra"),
                ("madhu udake", "madhūdake"), ("daitya-ari", "daityāri"),
                ("śrī-īśa", "śrīśa"), ("viṣṇu-udaya", "viṣṇūdaya")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.101"])
                self.assertEqual(after(text, "6.1.101"), form)

    def test_it_beats_yan_by_1_4_2(self):
        step = step_of("dadhi indra", "6.1.101")
        self.assertIn("6.1.77", lost(step))
        self.assertIn("1.4.2", lost(step)["6.1.77"])

    def test_the_counter_examples(self):
        """Kāśikā अक इति किम्? अग्नये; सवर्ण इति किम्? दध्यत्र; अचीत्येव — कुमारी शेते."""
        self.assertEqual(steps_of("agne~e{sup:ṅe}"), ["6.1.78"])
        self.assertEqual(sandhi("agne~e{sup:ṅe}").surface, "agnaye")
        self.assertEqual(steps_of("dadhi atra"), ["6.1.77"])
        self.assertEqual(sandhi("dadhi atra").surface, "dadhyatra")
        self.assertEqual(steps_of("kumārī śete"), [])
        self.assertEqual(sandhi("kumārī śete").surface, "kumārīśete")

    def test_it_is_the_projects_own_codification_for_every_pair(self):
        """`anga.akah_savarne_dirghah` says what 6.1.101 gives; the engine's step
        agrees, on every pair of vowels it answers for. Where the later sound is a
        short ṛ or ḷ the vārttikas give a first course; the LAST derivation is
        the sūtra's."""
        checked = 0
        vowels = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ")
        for left in vowels:
            for right in vowels:
                asked = akah_savarne_dirghah(left, right).result
                if asked is None:
                    continue
                text = f"k{left} {right}k"
                r = sandhi(text)
                last = len(r.outcomes) - 1
                got = step_of(text, "6.1.101", k=last).detail.adesa
                # ḷ has no long form of its own: the Kāśikā's ṝ
                self.assertEqual(got, "ṝ" if left == "ḷ" else asked, (left, right))
                checked += 1
        self.assertGreaterEqual(checked, 15)

    def test_the_vartikas_r_and_l(self):
        """Kāśikā ऋति सवर्णे परभूते तत्र ऋ वा भवति — होतृ ऋकारो होतृकारः, यदा न ऋ तदा
        दीर्घ एव (होतॄकारः); ऌति ऌ वा — होतृ ऌकारो होत्ऌकारः, … ॠकारः क्रियते
        (दीर्घस्याभावात्); Kaumudī होतृकारः, होतॄकारः / होत्ऌकारः, होतॄकारः."""
        self.assertEqual(sandhi("hotṛ ṛkāraḥ").surfaces, ("hotṛkāraḥ", "hotṝkāraḥ"))
        self.assertEqual(sandhi("hotṛ ḷkāraḥ").surfaces, ("hotḷkāraḥ", "hotṝkāraḥ"))

    def test_the_vartika_step_says_what_it_is(self):
        step = step_of("hotṛ ṛkāraḥ", "6.1.101")
        self.assertEqual(step.detail.authority, "vārttika")
        self.assertEqual(step.detail.varttika, fam.V_RTI_SAVARNE)
        self.assertEqual(step.option, "वा")
        made = [s for s in run("hotṛ ṛkāraḥ").final.segs if s.made_by == "6.1.101"]
        self.assertEqual([s.s for s in made], ["ṛ"])
        self.assertIn(fam.DVIMATRA, made[0].marks)        # two mātrās, and ONE sound

    def test_the_declined_course_is_6_1_101_itself(self):
        second = step_of("hotṛ ṛkāraḥ", "6.1.101", k=1)
        self.assertEqual(second.detail.authority, "sūtra")
        self.assertEqual(second.detail.adesa, "ṝ")
        self.assertEqual(vowel_steps(run("hotṛ ṛkāraḥ", 1)), ["6.1.101"])

    def test_the_vartika_is_for_alike_sounds_only(self):
        """A ṛ after a vowel that is not its savarṇa is no case of it."""
        self.assertEqual(len(sandhi("kṣatra ṛkāraḥ").outcomes), 1)


class Prathamayoh(unittest.TestCase):
    """6.1.102–6.1.106."""

    def test_the_kasikas_examples_of_6_1_102(self):
        """Kāśikā अग्नी, वायू, वृक्षाः, प्लक्षाः, वृक्षान्, प्लक्षान्."""
        for text, form in (
                ("agni~au{sup:au}", "agnī"), ("vāyu~au{sup:au}", "vāyū"),
                ("vṛkṣa~as{sup:jas}", "vṛkṣās"), ("plakṣa~as{sup:jas}", "plakṣās"),
                ("vṛkṣa{pum}~as{sup:śas}", "vṛkṣās"),
                ("plakṣa{pum}~as{sup:śas}", "plakṣās")):
            with self.subTest(text=text):
                self.assertEqual(vowel_steps(run(text))[0], "6.1.102")
                self.assertEqual(after(text, "6.1.102"), form)

    def test_the_case_ending_is_the_callers_word(self):
        """Control: the same letters with no ending named — the pararūpa अ of
        6.1.97 (the sūtra reaches only प्रथमा and द्वितीया); and a ṅas is not one."""
        self.assertEqual(steps_of("vṛkṣa~as"), ["6.1.97"])
        self.assertEqual(steps_of("vṛkṣa~as{sup:ṅas}"), ["6.1.97"])

    def test_the_closed_vocabularys_stem_names_the_ending_the_same_way(self):
        """README: `stem:X` says which lexical item a piece is. Of the piece `as`,
        `stem:jas` is what `sup:jas` says — so the gold cases, which are written
        that way, read the same — and a `stem:` that is no ending changes nothing."""
        for spelled, meant in (("rāma~as{stem:jas}", "rāma~as{sup:jas}"),
                               ("vṛkṣa{pum}~as{stem:śas}", "vṛkṣa{pum}~as{sup:śas}"),
                               ("go~as{stem:śas}", "go~as{sup:śas}"),
                               ("go~as{stem:ṅas}", "go~as{sup:ṅas}"),
                               ("go~am{stem:am}", "go~am{sup:am}")):
            with self.subTest(text=spelled):
                self.assertEqual(steps_of(spelled), steps_of(meant))
                self.assertEqual(sandhi(spelled).surface, sandhi(meant).surface)
        self.assertEqual(steps_of("rāma~as{stem:jas}"), ["6.1.102"])
        self.assertEqual(steps_of("rāma~as{stem:vṛkṣa}"), ["6.1.97"])
        self.assertEqual(steps_of("praṣṭha ūhas{stem:ūṭh}"), ["6.1.89"])
        self.assertEqual(steps_of("praṣṭha ūhas{stem:ūha}"), ["6.1.87"])

    def test_acci_kim_akah_kim_prathamayoh_kim(self):
        """Tattvabodhinī अकः किम्? गावौ, नावौ; प्रथमयोः किम्? वृक्षे, प्लक्षे."""
        self.assertEqual(steps_of("nau~au{sup:au}"), ["6.1.78"])
        self.assertEqual(sandhi("nau~au{sup:au}").surface, "nāvau")
        self.assertNotIn("6.1.102", steps_of("agni~e{sup:ṅe}"))

    def test_the_savarna_dirgha_of_the_earlier_sound(self):
        """Kāśikā पूर्वसवर्णग्रहणं किम्? अग्नी — the earlier sound's long vowel."""
        self.assertEqual(step_of("agni~au{sup:au}", "6.1.102").detail.adesa.split()[0], "ī")
        self.assertEqual(step_of("vāyu~au{sup:au}", "6.1.102").detail.adesa.split()[0], "ū")

    def test_6_1_103_shasah_nah_pumsi(self):
        """Kāśikā वृक्षान्, अग्नीन्, वायून्; शसः किम्? वृक्षाः; पुंसि किम्? धेनूः, बह्वीः,
        कुमारीः; तस्मादिति किम्? एतांश्चरतो गाः पश्य (the ā of गाः is 6.1.93's)."""
        for text, form in (("vṛkṣa{pum}~as{sup:śas}", "vṛkṣān"),
                           ("agni{pum}~as{sup:śas}", "agnīn"),
                           ("vāyu{pum}~as{sup:śas}", "vāyūn")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.102", "6.1.103"])
                self.assertEqual(sandhi(text).surface, form)
        # शसः किम्? — a jas is not the ending 6.1.103 names
        self.assertNotIn("6.1.103", [s.sutra for s in run("vṛkṣa{pum}~as{sup:jas}").steps])
        # पुंसि किम्? — the feminine
        for text in ("dhenu~as{sup:śas}", "kumārī~as{sup:śas}"):
            with self.subTest(text=text):
                self.assertNotIn("6.1.103", [s.sutra for s in run(text).steps])
        # तस्मादिति किम्? — the ā of गाः is 6.1.93's, not 6.1.102's
        self.assertEqual(steps_of("go{pum}~as{sup:śas}"), ["6.1.93"])
        self.assertEqual(sandhi("go{pum}~as{sup:śas}").surface, "gāḥ")

    def test_6_1_104_nadici_and_the_rules_it_lets_back(self):
        """Kāśikā वृक्षौ, प्लक्षौ, कुण्डे — and the Bālamanoramā: बाधके निवृत्ते गुणः
        पुनरुन्मिषति, the guṇa (vṛddhi) is back. The refusal is a step and the
        sthānin is not changed."""
        for text, form, then in (
                ("vṛkṣa~au{sup:au}", "vṛkṣau", "6.1.88"),
                ("plakṣa~au{sup:au}", "plakṣau", "6.1.88"),
                ("rāma~au{sup:au}", "rāmau", "6.1.88"),
                ("kuṇḍa~ī{sup:au}", "kuṇḍe", "6.1.87")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.104", then])
                refusal = step_of(text, "6.1.104")
                self.assertEqual(refusal.detail.kind, "pratiṣedha")
                self.assertEqual(refusal.before, refusal.after)
                self.assertIn("अवर्णादिचि पूर्वसवर्णदीर्घो न भवति (Kāśikā on 6.1.104)",
                              lost(refusal)["6.1.102"])
                self.assertEqual(after(text, then), form)

    def test_sivo_arcyah_the_u_of_the_ru_of_an_ending_is_refused_by_6_1_104(self):
        """Kaumudī on 6.1.104 (आद्गुणः, एङः पदान्तादति। शिवोऽर्च्यः) and the
        Bālamanoramā: शिव उ इति स्थिते आद्गुणे इति गुणं बाधित्वा पूर्वसवर्णदीर्घे प्राप्ते
        तस्मिन्निषिद्धे सति बाधके निवृत्ते गुणः पुनरुन्मिषति. The उ is what 6.1.113 makes
        out of the रु of the ending सु; named as an ending (`śiva~s{sup:su}`) it is a
        प्रथमा vowel, 6.1.102 reaches it, 6.1.104 refuses, and the guṇa comes back, then
        6.1.109. Control: with the ending unnamed, the letters give the same form but
        6.1.102 was never in question, so no refusal is shown."""
        text = "śiva~s{sup:su} arcya"
        self.assertEqual(sandhi(text).surface, "śivo'rcya")
        self.assertEqual(steps_of(text), ["6.1.104", "6.1.87", "6.1.109"])
        self.assertEqual([s.sutra for s in run(text).steps][:3],
                         ["8.2.66", "6.1.113", "6.1.104"])
        refusal = step_of(text, "6.1.104")
        self.assertEqual(refusal.detail.kind, "pratiṣedha")
        self.assertIn("6.1.102", lost(refusal))
        self.assertEqual(steps_of("śiva~s arcya"), ["6.1.87", "6.1.109"])
        self.assertEqual(sandhi("śiva~s arcya").surface, "śivo'rcya")

    def test_6_1_104_counter_examples(self):
        """Kāśikā आदिति किम्? अग्नी; इचीति किम्? वृक्षाः."""
        self.assertEqual(steps_of("agni~au{sup:au}"), ["6.1.102"])
        self.assertEqual(steps_of("vṛkṣa~as{sup:jas}"), ["6.1.102"])

    def test_6_1_104_marks_and_6_1_102_reads_the_mark(self):
        """The refusal is a mark on the earlier vowel, which 6.1.102 reads — take
        the refusal away and वृक्षौ becomes the long ā of 6.1.102."""
        without = tuple(r for r in STAGE if r.sutra != "6.1.104")
        self.assertEqual(derive_with(without, "vṛkṣa~au{sup:au}").surface[:5], "vṛkṣā")
        self.assertEqual(sandhi("vṛkṣa~au{sup:au}").surface, "vṛkṣau")

    def test_6_1_105_dirghaj_jasi_ca(self):
        """Kāśikā कुमार्यौ, कुमार्यः, ब्रह्मबन्ध्वौ, ब्रह्मबन्ध्वः; Laghukaumudī
        विश्वपाः — the refusal, and then the rule it had shadowed (6.1.77's yaṇ, or
        6.1.101 where the two are alike)."""
        for text, form, then in (
                ("kumārī~au{sup:au}", "kumāryau", "6.1.77"),
                ("kumārī~as{sup:jas}", "kumāryas", "6.1.77"),
                ("brahmabandhū~au{sup:au}", "brahmabandhvau", "6.1.77"),
                ("brahmabandhū~as{sup:jas}", "brahmabandhvas", "6.1.77"),
                ("gaurī~au{sup:au}", "gauryau", "6.1.77"),
                ("viśvapā~as{sup:jas}", "viśvapās", "6.1.101")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.105", then])
                self.assertEqual(after(text, then), form)
                self.assertIn("दीर्घात् जसि इचि च परतः पूर्वसवर्णदीर्घो न भवति "
                              "(Kāśikā on 6.1.105)",
                              lost(step_of(text, "6.1.105"))["6.1.102"])

    def test_where_both_refuse_the_later_is_done(self):
        """Bālamanoramā: विश्वपावित्यत्र नादिचि इत्यस्य दीर्घाज्जसि च इत्यस्य च प्राप्तौ
        परत्वेन दीर्घाज्जसि च इत्यस्यैवोपन्यासौचित्यात् — 6.1.105, not 6.1.104: an
        अवर्ण that is long, before an इच्."""
        for text, form in (("viśvapā~au{sup:au}", "viśvapau"),
                           ("khaṭvā~ī{sup:au}", "khaṭve")):
            with self.subTest(text=text):
                step = step_of(text, "6.1.105")
                self.assertNotIn("6.1.104", [s.sutra for s in run(text).steps])
                self.assertIn("6.1.104", lost(step))
                self.assertIn("1.4.2", lost(step)["6.1.104"])
                self.assertEqual(sandhi(text).surface, form)

    def test_6_1_106_the_vedic_option_of_6_1_105(self):
        """Kāśikā मारुतीश्चतस्रः पिण्डीः / मारुत्यश्चतस्रः पिण्ड्यः; वाराही उपानहा /
        वाराह्यौ उपानह्यौ."""
        r = sandhi("mārutī~as{sup:jas}", veda=True)
        self.assertEqual(r.surfaces, ("mārutīḥ", "mārutyaḥ"))
        self.assertEqual(vowel_steps(r.outcomes[0]), ["6.1.106"])
        self.assertEqual(vowel_steps(r.outcomes[1]), ["6.1.105", "6.1.77"])
        self.assertEqual(r.outcomes[1].choices[-1], ("6.1.106", False))
        r = sandhi("vārāhī~au{sup:au}", veda=True)
        self.assertEqual(r.surfaces, ("vārāhī", "vārāhyau"))

    def test_6_1_106_is_only_vedic(self):
        """Control: in the classical language there is one course, the refusal."""
        r = sandhi("mārutī~as{sup:jas}")
        self.assertEqual(r.surfaces, ("mārutyaḥ",))
        self.assertNotIn("6.1.106", steps_of("mārutī~as{sup:jas}"))

    def test_6_1_106_leaves_the_refusal_of_6_1_104_alone(self):
        """It takes the वा of 6.1.105 alone: an अवर्ण before an इच् is refused by
        6.1.104 in the Veda too."""
        self.assertEqual(sandhi("vṛkṣa~au{sup:au}", veda=True).surfaces, ("vṛkṣau",))


class AmiPurvah(unittest.TestCase):
    """6.1.107 अमि पूर्वः."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā वृक्षम्, प्लक्षम्, अग्निम्, वायुम्; कुमारीम्; Kaumudī रामम्."""
        for text, form in (("vṛkṣa~am{sup:am}", "vṛkṣam"),
                           ("plakṣa~am{sup:am}", "plakṣam"),
                           ("agni~am{sup:am}", "agnim"), ("vāyu~am{sup:am}", "vāyum"),
                           ("kumārī~am{sup:am}", "kumārīm"), ("rāma~am{sup:am}", "rāmam")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.107"])
                self.assertEqual(after(text, "6.1.107"), form)

    def test_the_earlier_sound_stands_not_its_long_form(self):
        """Kāśikā पूर्वग्रहणं किम्? … कुमारीमित्यत्र हि त्रिमात्रः स्यात्. And it is the
        exception to 6.1.102 (Tattvabodhinī: पूर्वसवर्णदीर्घे प्राप्तेऽयमारम्भः)."""
        step = step_of("kumārī~am{sup:am}", "6.1.107")
        self.assertIn("6.1.102", lost(step))
        self.assertIn("पूर्वसवर्णदीर्घे प्राप्तेऽयमारम्भः (Tattvabodhinī on 6.1.107)",
                      lost(step)["6.1.102"])

    def test_the_ending_is_the_callers_word(self):
        """Control: the letters `am` of a tense ending are not the case ending."""
        self.assertNotIn("6.1.107", steps_of("vṛkṣa~am"))


class Samprasaranac(unittest.TestCase):
    """6.1.108 सम्प्रसारणाच्च."""

    def test_the_a_after_the_samprasarana_goes(self):
        """Kāśikā यजि — इष्टम्, वपि — उप्तम्: the इ/उ that stands where य्/व् stood,
        and the अ that follows, are one इ/उ."""
        for text, form in (("i{samprasarana}~aj", "ij"), ("u{samprasarana}~ap", "up")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.108"])
                self.assertEqual(after(text, "6.1.108"), form)

    def test_it_displaces_yan_and_the_flag_is_the_callers(self):
        """Kāśikā: संप्रसारणविधानसामर्थ्याद् विगृहीतस्य श्रवणे प्राप्ते पूर्वत्वं विधीयते —
        the यण् (6.1.77) is what is displaced. Control: without the flag, yaṇ."""
        step = step_of("i{samprasarana}~aj", "6.1.108")
        self.assertIn("6.1.77", lost(step))
        self.assertEqual(steps_of("i~aj"), ["6.1.77"])
        self.assertTrue(sandhi("i~aj").surface.startswith("ya"))

    def test_in_the_veda_it_is_optional(self):
        """Kāśikā वा छन्दसीत्येव — मित्रावरुणौ यज्यमानः: the declined course is the
        yaṇ (यज्)."""
        r = sandhi("i{samprasarana}~aj", veda=True)
        self.assertEqual(len(r.outcomes), 2)
        self.assertEqual(vowel_steps(r.outcomes[0]), ["6.1.108"])
        self.assertEqual(vowel_steps(r.outcomes[1]), ["6.1.77"])
        self.assertEqual(len(sandhi("i{samprasarana}~aj").outcomes), 1)


class EngahPadantad(unittest.TestCase):
    """6.1.109 एङः पदान्तादति and 6.1.110 ङसिङसोश्च."""

    def test_the_kasikas_and_kaumudis_examples(self):
        """Kāśikā अग्नेऽत्र, वायोऽत्र; Kaumudī हरेऽव, विष्णोऽव."""
        for text, form in (("agne atra", "agne'tra"), ("vāyo atra", "vāyo'tra"),
                           ("hare ava", "hare'va"), ("viṣṇo ava", "viṣṇo'va")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.109"])
                self.assertEqual(sandhi(text).surface, form)

    def test_it_displaces_ayavadesa(self):
        """Kāśikā: अयवादेशयोरयमपवादः."""
        step = step_of("hare ava", "6.1.109")
        self.assertIn("अयवादेशयोरयमपवादः (Kāśikā on 6.1.109)", lost(step)["6.1.78"])

    def test_the_counter_examples(self):
        """Kāśikā एङ इति किम्? दध्यत्र, मध्वत्र; पदान्तादिति किम्? चयनम्, लवनम्; अतीति
        किम्? वायो इति; तपरकरणं किम्? वायवायाहि (the y before it may be lost, 8.3.19)."""
        for text, form in (("dadhi atra", "dadhyatra"), ("madhu atra", "madhvatra"),
                           ("ce~ana", "cayana"), ("lo~ana", "lavana"),
                           ("vāyo āyāhi", "vāyavāyāhi")):
            with self.subTest(text=text):
                self.assertNotIn("6.1.109", steps_of(text))
                self.assertIn(form, sandhi(text).surfaces)

    def test_6_1_110(self):
        """Kāśikā अग्नेरागच्छति, वायोरागच्छति, अग्नेः स्वम्, वायोः स्वम्; Kaumudī हरेः,
        हरीणाम्; अपदान्तार्थ आरम्भः."""
        for text, form in (("agne~as{sup:ṅasi}", "agneḥ"), ("vāyo~as{sup:ṅas}", "vāyoḥ"),
                           ("hare~as{sup:ṅas}", "hareḥ"), ("go~as{sup:ṅas}", "goḥ")):
            with self.subTest(text=text):
                self.assertEqual(steps_of(text), ["6.1.110"])
                self.assertEqual(sandhi(text).surface, form)
        self.assertEqual(sandhi("agne~as{sup:ṅasi} āgacchati").surface, "agnerāgacchati")
        step = step_of("hare~as{sup:ṅas}", "6.1.110")
        self.assertIn("अपदान्तार्थ आरम्भः (Kāśikā on 6.1.110)", lost(step)["6.1.78"])

    def test_6_1_110_needs_the_ending_named(self):
        """Control: the same letters with no ending named are 6.1.78's; and
        अतिसखेरागच्छति, सेनापतेरागच्छति (Kāśikā) end in ए."""
        self.assertEqual(steps_of("hare~as"), ["6.1.78"])
        self.assertEqual(sandhi("hare~as").surface, "harayaḥ")
        self.assertEqual(sandhi("atisakhe~as{sup:ṅas}").surface, "atisakheḥ")
        self.assertEqual(sandhi("senāpate~as{sup:ṅas}").surface, "senāpateḥ")


class RtaUt(unittest.TestCase):
    """6.1.111 ऋत उत् and 6.1.112 ख्यत्यात् परस्य."""

    def test_6_1_111_with_raparatva(self):
        """Kāśikā होतुरागच्छति, होतुः स्वम् — with उरण् रपरः (the र् is the substitute's)
        and रात् सस्य after it (8.2.24, not this family's, so the s stands)."""
        family_only = rulebook.rules_of("ac_ekadesa")
        for text in ("hotṛ~as{sup:ṅas}", "hotṛ~as{sup:ṅasi}"):
            with self.subTest(text=text):
                out = sandhi(text, rules=family_only).outcomes[0]
                self.assertEqual(vowel_steps(out), ["6.1.111"])
                self.assertEqual(out.surface, "hoturs")
                step = out.steps[0]
                self.assertIn("1.1.51", step.sutras)
                self.assertEqual(step.detail.adesa, "ur")

    def test_6_1_111_the_short_u_only(self):
        """Bālamanoramā उदिति तपरकरणं द्विमात्रनिवृत्त्यर्थम् — not ū, though the
        ṛ-varṇa before it is long: मातृ + अस् gives उर्, the short."""
        out = sandhi("mātṝ~as{sup:ṅas}", rules=rulebook.rules_of("ac_ekadesa")).outcomes[0]
        self.assertEqual(out.surface, "māturs")

    def test_6_1_112_sakhyuh_patyuh(self):
        """Kāśikā सख्युरागच्छति, सख्युः स्वम्, पत्युरागच्छति, पत्युः स्वम्."""
        for text, form in (("sakhi~as{sup:ṅasi}", "sakhyuḥ"),
                           ("sakhi~as{sup:ṅas}", "sakhyuḥ"),
                           ("pati~as{sup:ṅas}", "patyuḥ")):
            with self.subTest(text=text):
                self.assertIn("6.1.112", [s.sutra for s in run(text).steps])
                self.assertEqual(sandhi(text).surface, form)
        self.assertEqual(sandhi("sakhi~as{sup:ṅasi} āgacchati").surface,
                         "sakhyurāgacchati")

    def test_6_1_112_replaces_only_the_later_sound(self):
        """The heading has lapsed: *परस्य* — the अ becomes उ, the y stays, and the
        step is an ādeśa, not an एकादेश (1.1.54 आदेः परस्य)."""
        step = step_of("sakhi~as{sup:ṅas}", "6.1.112")
        self.assertEqual(step.detail.kind, "ādeśa")
        self.assertIn("1.1.54", step.sutras)
        self.assertEqual(step.detail.adesa, "u")
        self.assertEqual(step.after.replace(" ", ""), "sakhyus")

    def test_6_1_112_needs_the_yan_to_have_been_done_and_the_sounds_before(self):
        """Kāśikā …कृतयणादेशयोः: the y is the one 6.1.77 made, out of an इ, after kh
        or t. A y that stands in the input is not; nor is a y after another sound."""
        for text, form in (("sakhy~as{sup:ṅas}", "sakhyaḥ"),
                           ("bandhi~as{sup:ṅas}", "bandhyaḥ")):
            with self.subTest(text=text):
                self.assertNotIn("6.1.112", [s.sutra for s in run(text).steps])
                self.assertEqual(sandhi(text).surface, form)


class TheChain(unittest.TestCase):
    """The arrangement itself — how each rule of the chain stands to the ones it
    displaces."""

    def test_each_declared_relation_carries_the_traditions_words(self):
        """Every reason in an `overrides` entry is a quotation, and it is read
        back out of the commentary it names (see also `Quotes`)."""
        for r in fam.RULES:
            for target, why in r.overrides:
                self.assertTrue(
                    any(words in why and f"on {sutra})" in why
                        for _, sutra, words in fam.QUOTES), (r.sutra, target))

    def test_who_displaces_whom_in_the_chain(self):
        """The Kāśikā's chain, as declared: 6.1.88→87; 6.1.89→94 and 87; 6.1.90→95,
        96; 6.1.91→87; 6.1.94→88; 6.1.95→88, 101; 6.1.96→87; 6.1.97→101, 88 —
        and, by the maxim, 6.1.89 does not reach 6.1.95, nor 6.1.97 6.1.102."""
        declared = {}
        for r in fam.RULES:
            if not r.varttika:
                declared.setdefault(r.sutra, set()).update(t for t, _ in r.overrides)
        expected = {"6.1.88": {"6.1.87"}, "6.1.89": {"6.1.94", "6.1.87"},
                    "6.1.90": {"6.1.95", "6.1.96"}, "6.1.91": {"6.1.87"},
                    "6.1.94": {"6.1.88"}, "6.1.95": {"6.1.88", "6.1.101"},
                    "6.1.96": {"6.1.87"}, "6.1.97": {"6.1.101", "6.1.88"}}
        for sutra, targets in expected.items():
            self.assertEqual(declared[sutra], targets, sutra)

    def test_the_chain_agrees_with_the_projects_table(self):
        """`ekadesa.EKADESA_TABLE` is the project's own record of what each rule
        blocks. Wherever both ends of one of its pairs are rules here, either this
        family declares the pair, or it is one this family models otherwise — and
        says how."""
        ours = {(r.sutra, t) for r in fam.RULES for t, _ in r.overrides}
        modelled_otherwise = {
            # 6.1.98 is not OFFERED to the repeated member; 6.1.99 stands in its
            # place (a declared override would shut 6.1.98 out of the declined course)
            ("6.1.99", "6.1.98"),
            # a different junction: the t and the first sound of what follows
            ("6.1.100", "6.1.99"),
            # the later rule wins by 1.4.2, and the tradition states no exception
            ("6.1.102", "6.1.101"),
            # the table gives 6.1.107 as blocking the guṇa; the declared
            # relation is to 6.1.102, with the Tattvabodhinī's words
            ("6.1.107", "6.1.87"),
        }
        here = {r.sutra for r in fam.RULES}
        seen = 0
        for row in EKADESA_TABLE:
            for target in row.blocks:
                if row.sutra in here and target in here:
                    seen += 1
                    self.assertTrue(
                        (row.sutra, target) in ours
                        or (row.sutra, target) in modelled_otherwise,
                        (row.sutra, target))
        self.assertGreaterEqual(seen, 12)

    def test_every_rule_carries_the_tags_the_others_interlock_on(self):
        """README: every vowel-junction rule 'ac'; ekadesa rules also 'ekadesa';
        consonant rules 'hal'."""
        for r in fam.RULES:
            with self.subTest(rule=r.sutra, varttika=r.varttika[:12]):
                if r.sutra == "6.1.100":
                    self.assertEqual(r.families, frozenset({"ekadesa", "hal"}))
                elif r.sutra == "6.1.103":
                    self.assertEqual(r.families, frozenset({"hal"}))
                elif r.sutra == "6.1.112":
                    self.assertEqual(r.families, frozenset({"ac"}))
                else:
                    self.assertEqual(r.families, frozenset({"ac", "ekadesa"}))

    def test_the_vedic_rules_are_the_vedic_ones(self):
        vedic = sorted(r.sutra for r in fam.RULES if r.vedic)
        self.assertEqual(vedic, ["6.1.106", "6.1.94"])
        for r in fam.RULES:
            if r.vedic and r.sutra == "6.1.94":
                self.assertEqual(r.varttika, fam.V_EMANNADISU)


class Quotes(unittest.TestCase):
    """Nothing is quoted from memory: each quotation is found on disk."""

    def test_every_quotation_is_in_the_commentary_it_names(self):
        self.assertGreater(len(fam.QUOTES), 25)
        for work, sutra, words in fam.QUOTES:
            with self.subTest(work=work, sutra=sutra, words=words[:30]):
                self.assertIn(norm(words), tradition(work, sutra))

    def test_every_varttika_is_a_varttika_of_its_sutra_verbatim(self):
        texts = {(r.sutra, r.varttika) for r in fam.RULES if r.authority == "vārttika"}
        self.assertEqual(len(texts), 12)
        for sutra, text in texts:
            with self.subTest(sutra=sutra, text=text):
                self.assertIn(text, [v.text for v in corpus.varttikas_on(sutra)])

    def test_the_first_line_of_each_rules_docstring_is_the_traditions_own_words(self):
        """The line that states a rule in Sanskrit is quoted, not composed: each
        piece of it (they are cut at the commas) is found, spaces and stops aside,
        in a commentary or the vārttikas on that sūtra. A sentence the module made
        up would fail here."""
        def squeeze(text):
            text = re.sub(r"<<|>>", "", text)
            text = re.sub(r"\[\[[^\]]*\]\]", "", text)
            return re.sub(r"[\s।॥,;?!\-–—.\u200c\u200d]+", "", text)
        works = [w for w in corpus.COMMENTARIES
                 if w not in ("data", "vasu_english", "sutrartha_english", "sutra_prayogas")]
        for r in fam.RULES:
            head = re.split(r"\s+—\s+", r.__doc__.strip().splitlines()[0])[0]
            pool = "".join(squeeze(corpus.commentary_on(r.sutra, w) or "") for w in works)
            pool += "".join(squeeze(v.text) for v in corpus.varttikas_on(r.sutra))
            for piece in re.split(r"\s*,\s*", head):
                with self.subTest(sutra=r.sutra, varttika=r.varttika[:10], piece=piece[:40]):
                    self.assertIn(squeeze(piece), pool)

    def test_the_sutra_names_in_the_modules_table_are_the_corpus_words(self):
        """The table at the head of the module names each sūtra; a name set down there
        is a name typed, so it is read against the corpus like every other."""
        known = corpus.load_vidyut_sutrapatha()
        rows = re.findall(r"^ {4}(6\.1\.\d+) +(\S.*?) {2,}\S", fam.__doc__, flags=re.M)
        self.assertGreaterEqual(len(rows), 20)
        for sutra, name in rows:
            with self.subTest(sutra=sutra):
                self.assertEqual(name.replace(" ", ""),
                                 trace.deva(known[sutra].text).replace(" ", ""))

    def test_every_rule_name_is_the_sutras_own_words(self):
        known = corpus.load_vidyut_sutrapatha()
        for r in fam.RULES:
            if not r.varttika:
                self.assertEqual(r.name, trace.deva(known[r.sutra].text), r.sutra)

    def test_the_two_wordings_of_the_last_vartika_of_6_1_89_are_both_on_disk(self):
        """The corpus's list reads प्रवत्सतरकम्बलवसनदशार्णानामृणे, the Kaumudī
        प्रवत्सतरकम्बलवसनार्णदशानामृणे. The rule quotes the corpus's; the words it
        names are those of the Kāśikā (प्रवत्सतरकम्बलवसनानामृणे, ऋणदशाभ्याम्)."""
        self.assertIn("प्रवत्सतरकम्बलवसनदशार्णानामृणे",
                      [v.text.replace(" ।", "") for v in corpus.varttikas_on("6.1.89")])
        self.assertIn("प्रवत्सतरकम्बलवसनार्णदशानामृणे", tradition("kaumudi", "6.1.89"))
        kasika = tradition("kashika", "6.1.89")
        self.assertIn("प्रवत्सतरकम्बलवसनानामृणे", kasika)
        self.assertIn("ऋणदशाभ्यां", kasika)
        for word in fam._PRAVATSATARA_LEFT:
            self.assertIn(trace.deva(word), kasika.replace("॥", " "))

    def test_the_words_the_vartikas_name_are_the_words_of_the_commentary(self):
        """The words 6.1.89's vārttikas list — the second members and their first
        — are found in the commentaries on the sūtra, not made up in the code."""
        text = " ".join(tradition(work, "6.1.89") for work in
                        ("kashika", "kaumudi", "balamanorama", "tattvabodhini"))
        for word in ("akṣa", "ūhinī", "sva", "īra", "īrin", "ūha", "ūḍha", "ūḍhi",
                     "eṣa", "eṣya", "ṛta") + fam._PRAVATSATARA_LEFT:
            self.assertIn(trace.deva(word), text, word)
        for word in fam._PRA_RIGHT + fam._PRA_RIGHT_KRT:
            self.assertIn(trace.deva(word), text, word)


class Coverage(unittest.TestCase):
    """The family's account of what it does."""

    def test_the_rulebook_is_sound(self):
        self.assertEqual(rulebook.problems(), [])

    def test_every_sutra_in_scope_is_accounted_for_exactly_once(self):
        ids = [s for s, _, _ in fam.COVERAGE]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(sorted(ids, key=_order),
                         sorted(IN_SCOPE + SUPPORTS, key=_order))

    def test_every_sutra_of_the_scope_exists_in_the_corpus(self):
        known = corpus.load_vidyut_sutrapatha()
        for sutra, _, _ in fam.COVERAGE:
            self.assertIn(sutra, known)

    def test_a_scope_or_partial_note_gives_a_real_reason(self):
        for sutra, status, note in fam.COVERAGE:
            if status in ("scope", "partial"):
                self.assertGreater(len(note), 60, sutra)

    def test_the_statuses_match_the_code(self):
        """A `rule`, `partial` or `vedic` sūtra has a Rule; a `support` or `scope`
        one has none of its own."""
        with_rule = {r.sutra for r in fam.RULES}
        for sutra, status, _ in fam.COVERAGE:
            if status in ("rule", "partial", "vedic"):
                self.assertIn(sutra, with_rule, sutra)
            else:
                self.assertNotIn(sutra, with_rule, sutra)

    def test_the_vedic_status_is_for_a_vedic_rule(self):
        vedic = {s for s, st, _ in fam.COVERAGE if st == "vedic"}
        self.assertEqual(vedic, {"6.1.106"})
        self.assertTrue(next(r for r in fam.RULES if r.sutra == "6.1.106").vedic)

    def test_every_rule_is_declared(self):
        declared = {s: st for s, st, _ in fam.COVERAGE}
        for r in fam.RULES:
            self.assertIn(declared[r.sutra], ("rule", "partial", "vedic"), r.sutra)

    def test_every_open_note_is_in_scope_says_which_kind_and_is_said_where_it_applies(self):
        """The commentaries' disagreements are recorded (NORTH_STAR: a limitation that
        is recorded is not a failure). Each note names a sūtra of the scope, is OPEN
        or SCOPE, gives its reason, and is repeated in the docstring of the rule it
        touches — or, where the sūtra has no rule, in its COVERAGE note."""
        scope = set(IN_SCOPE) | set(SUPPORTS)
        docs = {}
        for r in fam.RULES:
            docs.setdefault(r.sutra, "")
            docs[r.sutra] += r.__doc__ or ""
        notes = {sutra: note for sutra, _, note in fam.COVERAGE}
        self.assertGreaterEqual(len(fam.OPEN), 8)
        for kind, sutra, note in fam.OPEN:
            with self.subTest(sutra=sutra, kind=kind):
                self.assertIn(kind, ("OPEN", "SCOPE"))
                self.assertIn(sutra, scope)
                self.assertGreater(len(note), 120)
                where = docs[sutra] if sutra in docs else notes[sutra]
                self.assertIn(kind, where)

    def test_the_open_note_on_6_1_86_is_still_true(self):
        """NORTH_STAR: a test guarding an OPEN note fails the day the question is
        answered. 6.1.86 says the एकादेश is asiddha to ṣatva and tuk, and
        `asiddha.ekadesa_visible` is the project's answer — but `View` shows a
        rule the past of a sound only through `asiddha.visible`, so a ṣatva rule
        would still SEE the substitute. When the core asks 6.1.86, this fails and
        COVERAGE must change."""
        self.assertTrue(ekadesa_visible("ṣatva").asiddha)
        self.assertTrue(ekadesa_visible("tuk").asiddha)
        final = run("hara iha").final
        seen = [s for s in View(final, "8.3.57").live if s.seg.made_by == "6.1.87"]
        self.assertEqual([s.s for s in seen], ["e"])
        self.assertFalse(seen[0].through)


class Citations(unittest.TestCase):
    """Every sūtra a step of this family names is a sūtra, and its quoted words
    are the corpus's."""

    CASES = (
        "khaṭvā indra", "kṛṣṇa aikya", "upa|eti{dhatu:i}", "praṣṭha ūhas{uth}",
        "ā{aat}~usrīyat", "pra|ṛcchati", "upa|ṛṣabhīyati{subanta}", "go~as{sup:śas}",
        "pra|ejate", "upa|eḍakīyati{subanta}", "śiva ehi{ang}", "bhindyā~us",
        "paca~anti", "paṭat{avyakta} iti", "paṭat{avyakta,amredita} iti",
        "śrat{avyakta} iti", "paṭat{avyakta} paṭā{avyakta,amredita,dac}",
        "hotṛ ṛkāraḥ", "vṛkṣa{pum}~as{sup:śas}", "rāma~au{sup:au}",
        "viśvapā~au{sup:au}", "vṛkṣa~am{sup:am}", "i{samprasarana}~aj",
        "hare ava", "hare~as{sup:ṅas}", "sakhi~as{sup:ṅas}", "hotṛ~as{sup:ṅas}",
        "manas-īṣā", "sva-īra", "sukha{trtiya}-ṛta", "sthūla-otu", "iha eva{aniyoga}")

    def test_every_sutra_named_exists_and_its_words_are_the_corpus_words(self):
        known = corpus.load_vidyut_sutrapatha()
        for text in self.CASES:
            for outcome in sandhi_of_everything(text).outcomes:
                for step in trace.outcome_dict(outcome)["steps"]:
                    self.assertEqual(step["sutra_iast"], known[step["sutra"]].text)
                    for via in step["via"]:
                        self.assertIn(via["sutra"], known, (text, via["sutra"]))
                        self.assertEqual(via["text_iast"], known[via["sutra"]].text)
                    for lost_ in step["against"]:
                        self.assertIn(lost_["sutra"], known, (text, lost_["sutra"]))

    def test_the_traces_print_in_both_scripts(self):
        out = sandhi("upa|eti{dhatu:i}").trace()
        self.assertIn("उपैति (upaiti)", out)
        self.assertIn("वृद्धिरेचि", out)
        self.assertIn("एत्येधत्यूठ्सु (etyedhatyūṭhsu)", out)

    def test_a_trace_serialises(self):
        json.dumps(sandhi_of_everything("paṭat{avyakta,amredita} iti").to_dict(),
                   ensure_ascii=False)


class Speed(unittest.TestCase):
    def test_a_junction_stays_in_the_millisecond_range(self):
        sandhi_of_everything("khaṭvā indra")        # the first call loads the corpus
        began = time.perf_counter()
        for _ in range(20):
            sandhi_of_everything("upa|eti{dhatu:i}")
            sandhi_of_everything("vṛkṣa{pum}~as{sup:śas}")
        each = (time.perf_counter() - began) / 40
        self.assertLess(each, 0.05)


if __name__ == "__main__":
    unittest.main()
