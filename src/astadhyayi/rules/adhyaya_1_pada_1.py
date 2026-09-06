# -*- coding: utf-8 -*-
"""
Aṣṭādhyāyī 1.1 — codified sūtra by sūtra.

Each entry states only what it alone knows: the executable rule, what that rule
computes, the working notes, and cross-references the data does not already
supply. The mūla, padaccheda, anuvṛtti, adhikāra and every commentary come from
the local corpus through `sources.register`, with locators pointing back at the
file each came from.

Definitions are *derived* wherever the system allows it. vṛddhi and guṇa are
not typed in as letter-lists; they are computed from the śivasūtras through
1.1.71, so the three sūtras stand or fall together and the tests say which.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from src.chandas.core import scan_phonemes
from src.astadhyayi.sivasutra import Pratyahara, resolve
from src.astadhyayi.adesa import (
    agama_site,
    antaratama,
    hrasva_of_ec,
    samprasarana,
    guna_vrddhi_blocked,
    nirdesa,
    raparatva,
    replace_antya,
    site_for,
    sthanin_padas,
    substitution_site,
    ti,
    upadha,
)
from src.astadhyayi.avyaya import avyaya
from src.astadhyayi.sthanivat import sthanivat
from src.astadhyayi.pragrhya import pragrhya
from src.astadhyayi.samjna import (
    is_gha,
    is_ghu,
    is_nistha,
    is_samkhya,
    is_sarvanaman,
    is_sat,
    positions,
    sarvanaman,
    sarvanamasthana,
    vibhasa,
    vrddha,
)
from src.astadhyayi.lopa import (
    adarsana,
    names_of_affix_elision,
    pratyaya_laksana,
)
from src.astadhyayi.grahana import grahana, tadantavidhi
from src.astadhyayi.sources import register
from src.astadhyayi.varna import (
    blocked_by_na_ajjhalau,
    is_anunasika,
    savarna,
)

# ---------------------------------------------------------------------------
# Shared shape: a saṃjñā that names "one stated sound + one pratyāhāra".
#
# 1.1.1 and 1.1.2 have exactly this form — ādaiC is ā + aiC, adeṄ is a + eṄ —
# so the machinery is written once and each sūtra supplies only its own parts.
# ---------------------------------------------------------------------------


def sound_class(stated: str, pratyahara: str) -> Tuple[str, ...]:
    """
    The sounds a saṃjñā of the form `<stated><pratyāhāra>` covers.

    The pratyāhāra is resolved from the śivasūtras by 1.1.71; the separately
    stated sound is prefixed. Nothing is hardcoded, so a change to the
    śivasūtras propagates to every saṃjñā built this way.
    """
    return (stated,) + resolve(pratyahara).sounds


def membership_test(sounds: Tuple[str, ...], name: str):
    """
    A closed membership predicate over a fixed set of sounds.

    `name` is not decoration. The playground shows the reader which function
    answered their question, and it reads that off `__name__` — so without
    it every rule built by this factory announced itself as `test()`, which
    names nothing and appears in no source file the reader could go and
    look at.
    """
    members = frozenset(sounds)

    def test(sound: str) -> bool:
        return sound in members

    test.__name__ = name
    test.__qualname__ = name
    return test


# ---------------------------------------------------------------------------
# 1.1.1  वृद्धिरादैच्  vṛddhir ādaiC — the vṛddhi saṃjñā
# ---------------------------------------------------------------------------

VRDDHI: Tuple[str, ...] = sound_class("ā", "aiC")        # ā, ai, au
is_vrddhi = membership_test(VRDDHI, "is_vrddhi")
is_vrddhi.__doc__ = (
    "1.1.1: does this sound bear the name vṛddhi? True for ā, ai, au.\n\n"
    "The sūtra assigns a name and prescribes no operation; the rules that put "
    "the name to work are elsewhere (7.2.1 sici vṛddhiḥ parasmaipadeṣu is the "
    "first, as the Kāśikā notes). By the tapara of āt (1.1.70) the name reaches "
    "only the two-mātrā forms, so a pluta ā3 is not vṛddhi."
)

register(
    "1.1.1",
    reuses=('1.1.71',),
    samjna="vṛddhi",
    apply=is_vrddhi,
    codification=(
        "is_vrddhi(sound) -> bool. The membership set is derived as ā + aiC, "
        "aiC being resolved from śivasūtras 1–4 through 1.1.71."
    ),
    related=("1.1.2", "1.1.3", "1.1.70", "1.1.71", "6.1.88", "7.2.1"),
    notes=(
        "SETTLED — the tapara question. The t of āt is indicatory: by 1.1.70\n"
        "  taparas tatkālasya the name reaches only the two-mātrā forms. The\n"
        "  Kāśikā says the making of it tapara is for the sake of the aiC, and\n"
        "  excludes the three- and four-mātrā contingency in khaṭvaiḍaka and the\n"
        "  like; Vasu says the same. A pluta ā3 is therefore NOT vṛddhi.\n"
        "  Both sources also confirm the padaccheda vṛddhiḥ / āt / aiC, and the\n"
        "  Kāśikā adds that the name applies tadbhāvita and atadbhāvita alike —\n"
        "  whether or not the sound was produced by a rule.\n"
        "\n"
        "OPEN — why vṛddhi is defined before guṇa, when guṇa is the commoner\n"
        "  operation. The maṅgala reading — vṛddhi means growth, so the work\n"
        "  opens auspiciously — is widely reported.\n"
        "\n"
        "  CHECKED, and it cannot be settled from what is on disk. The\n"
        "  Mahābhāṣya in this corpus is question-openers only: all 220 of its\n"
        "  non-empty readings are a single sentence, usually किमर्थम् or\n"
        "  किम् इदम्, and the entry for 1.1.1 is 46 characters about kutva,\n"
        "  touching nothing about the order of the two saṃjñās. The Kāśikā,\n"
        "  Nyāsa, Padamañjarī and Kaumudī on 1.1.1 do not raise it either.\n"
        "\n"
        "  So it stays OPEN for a stated reason rather than for want of\n"
        "  looking: the text that would settle it is not among the sources\n"
        "  this project holds. Recording the maṅgala reading as Patañjali's\n"
        "  would be repeating what is widely said, which is the one thing\n"
        "  this codification is built not to do.\n"
        "\n"
        "  NOTE — the corpus does carry a maṅgala argument, but about another\n"
        "  sūtra: on 1.3.1 the Kāśikā reports भूवादीनां वकारोऽयं मङ्गलार्थः\n"
        "  प्रयुज्यते, the व of भ्वादि standing there for auspiciousness.\n"
        "  That one is attested locally and is recorded there. It is not\n"
        "  evidence for this one."
    ),
)


# ---------------------------------------------------------------------------
# 1.1.2  अदेङ् गुणः  adeṄ guṇaḥ — the guṇa saṃjñā
# ---------------------------------------------------------------------------

GUNA: Tuple[str, ...] = sound_class("a", "eṄ")           # a, e, o
is_guna = membership_test(GUNA, "is_guna")
is_guna.__doc__ = (
    "1.1.2: does this sound bear the name guṇa? True for अ (a), ए (e) "
    "and ओ (o).\n\n"
    "The same shape as 1.1.1: a separately stated sound (a) plus a pratyāhāra "
    "(eṄ = e, o). As with vṛddhi, the a is tapara by 1.1.70, so the name reaches "
    "the one-mātrā a and not its pluta."
)

register(
    "1.1.2",
    reuses=('1.1.71',),
    samjna="guṇa",
    apply=is_guna,
    codification=(
        "is_guna(sound) -> bool. Derived as a + eṄ, eṄ being resolved from "
        "śivasūtra 3 through 1.1.71 — the same machinery as 1.1.1."
    ),
    related=("1.1.1", "1.1.3", "1.1.70", "1.1.71", "7.3.84", "7.3.86"),
    notes=(
        "SETTLED — built on exactly the shape of 1.1.1, deliberately: the two saṃjñās are\n"
        "  parallel in the text and are parallel here, so a fault in the shared\n"
        "  derivation shows up in both at once rather than in neither.\n"
        "\n"
        "SETTLED — the two names are disjoint: a, e, o against ā, ai, au. The tests\n"
        "  assert it. That disjointness is what lets 1.1.3 name them together\n"
        "  without ambiguity."
    ),
)


# ---------------------------------------------------------------------------
# 1.1.3  इको गुणवृद्धी  iko guṇavṛddhī — what guṇa and vṛddhi replace
# ---------------------------------------------------------------------------

#: iK — the vowels i, u, ṛ, ḷ (and their long counterparts by 1.1.69/savarṇa).
IK: Tuple[str, ...] = resolve("iK").sounds

#: The long counterparts. 1.1.3 names iK; a long ī is savarṇa with i and is
#: taken in by 1.1.69 aṇudit savarṇasya, so both lengths are targets.
_LONG_OF: Dict[str, str] = {"i": "ī", "u": "ū", "ṛ": "ṝ", "ḷ": "ḹ"}
IK_ALL: Tuple[str, ...] = IK + tuple(_LONG_OF[s] for s in IK if s in _LONG_OF)


def is_ik(sound: str) -> bool:
    """Is this sound in iK — the class guṇa and vṛddhi operate on?"""
    return sound in frozenset(IK_ALL)


def guna_vrddhi_target(sound: str) -> bool:
    """
    1.1.3: where a rule prescribes guṇa or vṛddhi without naming what it
    replaces, the substitution falls on an iK vowel.

    The sūtra fixes the *target class* only. Which particular guṇa or vṛddhi
    sound replaces which iK vowel is not stated here — that follows from 1.1.50
    sthāne'ntaratamaḥ (nearest substitute), with 1.1.51 ur aṇ raparaḥ for ṛ.
    Those are separate sūtras and are codified separately; this function
    deliberately answers only what 1.1.3 answers.
    """
    return is_ik(sound)


register(
    "1.1.3",
    reuses=('1.1.71',),
    apply=guna_vrddhi_target,
    codification=(
        "guna_vrddhi_target(sound) -> bool. True for the iK vowels (both "
        "lengths), the class an unqualified guṇa- or vṛddhi-rule operates on. "
        "Which substitute appears is left to 1.1.50/1.1.51."
    ),
    related=("1.1.49", "1.1.50", "1.1.51", "1.1.69"),
    notes=(
        "The corpus records the anuvṛtti for this sūtra as वृद्धिः from 1.1.1 and\n"
        "  गुणः from 1.1.2 — the two names defined immediately before are read\n"
        "  into it. That is why the three sūtras form one unit and are codified\n"
        "  together here.\n"
        "\n"
        "इकः stands in the ṣaṣṭhī (the corpus's padaccheda marks it 6th case,\n"
        "  singular). By 1.1.49 ṣaṣṭhī sthāneyogā a genitive in a rule means\n"
        "  'in place of' — so iK is what guṇa/vṛddhi are substituted FOR, not\n"
        "  what they are substituted BY. The case marking is doing real work,\n"
        "  and is preserved in the record.\n"
        "\n"
        "SCOPE — this function answers only the target class. Resist the\n"
        "  temptation to fold the i→e/ai, u→o/au, ṛ→ar/ār correspondence in\n"
        "  here: that is 1.1.50's work, and putting it in 1.1.3 would attribute\n"
        "  to this sūtra something it does not say."
    ),
)


# ---------------------------------------------------------------------------
# When guṇa and vṛddhi do not happen — 1.1.4 to 1.1.6
#
# Three prohibitions on the operation 1.1.3 set up. All three read इकः and
# गुणवृद्धी down from 1.1.3 and न down from 1.1.4, which the corpus records, so
# they are one unit with it and are codified beside it. Implemented in
# src/astadhyayi/adesa.py next to the guṇa and vṛddhi they veto.
# ---------------------------------------------------------------------------


register(
    "1.1.4",
    reuses=('1.1.3',),
    apply=guna_vrddhi_blocked,
    codification=(
        "The dhātulopa branch of guna_vrddhi_blocked: no guṇa or vṛddhi where "
        "an ārdhadhātuka has elided part of the root. Both conditions are "
        "parameters, because neither can be read off a bare vowel."
    ),
    related=("1.1.3", "1.1.5", "1.1.6", "2.4.74", "3.1.134"),
    notes=(
        "SETTLED — the elision must be of the root and of an ārdhadhātuka, and\n"
        "  the Kāśikā tests each half. धातुग्रहणं किम्? लविता from लूञ् — the\n"
        "  ñ that drops there is an anubandha, not root, so guṇa proceeds;\n"
        "  likewise रेट् where a विच् affix drops. आर्धधातुके इति किम्?\n"
        "  रोरवीति, where the affix is sārvadhātuka and the prohibition does\n"
        "  not reach. Its own examples are लोलुवः, पोपुवः, मरीमृजः, where a\n"
        "  yaṄ has been elided by 2.4.74 under 3.1.134.\n"
        "\n"
        "SETTLED — इकः is still in force: इक इत्येव — अभाजि, रागः. A target\n"
        "  outside iK is not blocked here because 1.1.3 never offered it."
    ),
)


register(
    "1.1.5",
    reuses=('1.1.3',),
    apply=guna_vrddhi_blocked,
    codification=(
        "The kṅit branch. The marks come from the affix's own Adesa, which "
        "1.3.2–1.3.9 can now fill, so being kit is derived from क्त rather "
        "than asserted about it."
    ),
    related=("1.1.3", "1.1.4", "1.1.26", "1.3.8", "3.2.139"),
    notes=(
        "SETTLED — the locative is one of cause, not of place: निमित्तसप्तम्येषा,\n"
        "  क्ङिन्निमित्ते ये गुणवृद्धी प्राप्नुतः ते न भवतः. So the test is on\n"
        "  the affix that would have occasioned the operation.\n"
        "\n"
        "SETTLED — this is where the it-saṃjñā block pays for itself. क्त is\n"
        "  kit because 1.3.8 makes its k indicatory, and that is now computed:\n"
        "  चि + क्त gives चितः and not चेतः because Adesa.from_upadesa finds the\n"
        "  k. Before 1.3.2–1.3.9 were codified this rule could only have been\n"
        "  given a hand-marked affix. The Kāśikā's series चितः, चितवान्,\n"
        "  स्तुतः, स्तुतवान्, भिन्नः, भिन्नवान्, मृष्टः, मृष्टवान् all turn on it,\n"
        "  and चिनुतः, चिन्वन्ति on the ṅit half.\n"
        "\n"
        "SETTLED — g counts too: गकारोऽप्यत्र चर्त्वभूतो निर्दिश्यते, the g is\n"
        "  indicated here as a cartva-form. KNIT therefore holds three letters.\n"
        "  The Kāśikā's example is 3.2.139 giving जिष्णुः, भूष्णुः; all three\n"
        "  witnesses to that sūtra read क्स्नु, so the affix cited there is kit\n"
        "  and the remark exists to cover the variant reading ग्स्नु.\n"
        "\n"
        "SETTLED — इकः again: इकः इत्येव — कामयते.\n"
        "\n"
        "SCOPE — the Kāśikā records two further provisions not codified here. A\n"
        "  vārttika मृजेरजादौ संक्रमे विभाषा वृद्धिरिष्यते makes vṛddhi optional\n"
        "  for मृज् before a vowel (परिमृजन्ति beside परिमार्जन्ति); and a\n"
        "  jñāpaka from the ṅit-marking of यासुट् shows that what is ṅit-\n"
        "  conditioned does not apply to a lakāra. Both are real and both need\n"
        "  machinery — optionality, and lakāra as a category — that does not\n"
        "  exist yet."
    ),
)


register(
    "1.1.6",
    reuses=('1.1.3',),
    apply=guna_vrddhi_blocked,
    codification=(
        "The named-item branch: dīdhī, vevī, iṭ. Three forms, matched as "
        "forms, because the sūtra names them individually rather than by class."
    ),
    related=("1.1.3", "1.1.4", "1.1.5"),
    notes=(
        "SETTLED — a list and not a class. दीधी and वेवी are two roots and इट्\n"
        "  is an augment; nothing groups them but this sūtra. So the check is a\n"
        "  membership test on three names, which is what the rule is.\n"
        "\n"
        "SETTLED — for इट् only guṇa is really at stake: वृद्धिरिटो न संभवतीति\n"
        "  लघूपधगुणस्यात्र प्रतिषेधः, vṛddhi cannot arise for iṭ, so what is\n"
        "  forbidden is the laghūpadha guṇa. The examples are कणिता श्वः,\n"
        "  रणिता श्वः against आदीध्यनम् and आवेव्यनम् for the two roots."
    ),
)


# ---------------------------------------------------------------------------
# The phonetic saṃjñās — 1.1.7 to 1.1.10
#
# All four are bound to src/astadhyayi/varna.py, which carries the Śikṣā's
# sthāna and prayatna tables and derives every phonetic category from a
# pratyāhāra. Nothing phonetic is restated in this file: these entries say
# which feature each sūtra names, and record what the commentaries settled.
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Samyoga:
    """
    One conjunct.

    समुदायः संज्ञी — the Kāśikā is explicit that the name belongs to the
    aggregate and not to each consonant in it, so this is a group with an
    extent, not a flag on a sound.
    """

    sounds: Tuple[str, ...]
    start: int
    end: int

    @property
    def text(self) -> str:
        return "".join(self.sounds)

    def __len__(self) -> int:
        return len(self.sounds)


def samyogas(text: str) -> Tuple[Samyoga, ...]:
    """
    1.1.7 हलोऽनन्तराः संयोगः — consonants with nothing between them.

    अनन्तराः is glossed भिन्नजातीयैरज्भिरव्यवहिताः श्लिष्टोच्चारिताः, "not
    interrupted by vowels of another kind, pronounced conjointly": a run of haL
    with no aC inside it. Only a vowel breaks a run, which is what the gloss
    says; anusvāra and visarga are neither haL nor aC, so they neither join a
    conjunct nor split one.

    The plural is generic — जातौ चेदं बहुवचनम्, तेन द्वयोर्बहूनां च संयोगसंज्ञा
    सिद्धा भवति — so two consonants qualify as readily as three, and the Kāśikā
    illustrates both: अग्निः (g-n), अश्वः (ś-v), कर्णः (r-ṇ) against इन्द्रः
    (n-d-r) and उष्ट्रः (ṣ-ṭ-r).

    Tokenising reuses src/chandas/core.scan_phonemes — the same scanner the
    prosody engine runs on, so grammar and metre cannot drift apart on what
    counts as one sound.
    """
    groups: list = []
    run: list = []

    def flush() -> None:
        if len(run) >= 2:
            groups.append(
                Samyoga(
                    sounds=tuple(x.text for x in run),
                    start=run[0].start,
                    end=run[-1].start + len(run[-1].text),
                )
            )
        run.clear()

    for phoneme in scan_phonemes(text):
        if phoneme.kind == "consonant":
            run.append(phoneme)
        elif phoneme.kind == "vowel":
            flush()
    flush()
    return tuple(groups)


register(
    "1.1.7",
    samjna="saṃyoga",
    apply=samyogas,
    codification=(
        "samyogas(text) -> tuple of Samyoga. Each is a maximal run of haL with "
        "no aC inside it, carrying its extent because the Kāśikā makes the "
        "aggregate the saṃjñin. Phonemes come from chandas.core.scan_phonemes."
    ),
    related=("1.1.9", "1.1.10", "6.1.68", "8.2.23"),
    notes=(
        "SETTLED — the name is borne by the group, not by its members.\n"
        "  समुदायः संज्ञी in the Kāśikā. Modelling it as a predicate on a sound\n"
        "  would have been the obvious mistake, and would have made 8.2.23\n"
        "  संयोगान्तस्य लोपः unstatable, since that rule needs to know where the\n"
        "  conjunct ends.\n"
        "\n"
        "SETTLED — two is enough. The bahuvacana is जातौ, generic, so the name\n"
        "  is not reserved for three or more.\n"
        "\n"
        "The Kāśikā's own worked examples are used as the test data verbatim\n"
        "  rather than invented ones, so a failure indicts the code and not the\n"
        "  expectations."
    ),
)


register(
    "1.1.8",
    samjna="anunāsika",
    apply=is_anunasika,
    codification=(
        "is_anunasika(sound) -> bool, reading the mukha and nāsikā flags on the "
        "varṇa. The sūtra names both organs and the function tests both."
    ),
    related=("1.1.9", "1.1.69", "6.1.126", "8.3.23", "8.4.58"),
    notes=(
        "SETTLED — anusvāra is NOT anunāsika, and मुख is in the sūtra to say so.\n"
        "  The bhāṣya puts it directly — REPORTED, not checkable here: this\n""  passage is in none of the texts on disk, whose bhāṣya is question-\n""  openers only. नासिकावचनः अनुनासिकः इति इयति उच्यमाने\n"
        "  यमानुस्वाराणाम् एव प्रसज्येत — 'were only nose-uttered said, it would\n"
        "  fall on the yamas and the anusvāra alone' — मुखग्रहणे पुनः क्रियमाणे न\n"
        "  दोषो भवति. The Kāśikā agrees: मुखग्रहणं किम्? अनुस्वारस्यैव हि स्यात्.\n"
        "  The Śikṣā gives anusvāra the nose alone as its place\n"
        "  (नासिकाऽनुस्वारस्य), so it fails the mouth half of the test. This was\n"
        "  got wrong on the first pass and corrected against these two passages.\n"
        "\n"
        "SETTLED — नासिका is there for the mirror reason: मुखवचनः अनुनासिकः इति\n"
        "  इयति उच्यमाने कचटतपानाम् एव प्रसज्येत. Each half excludes something.\n"
        "\n"
        "SETTLED — a classificatory saṃjñā, not a constructor. The bhāṣya raises\n"
        "  the itaretarāśraya objection and answers it — REPORTED, not checkable\n"
        "  here; the passage is in none of the texts on disk:  नित्येषु शब्देषु सतः\n"
        "  अनुनासिकस्य सञ्ज्ञा क्रियते, न सञ्ज्ञया अनुनासिको भाव्यते — the name is\n"
        "  given to a sound already nasal; the name does not make it so. Nasality\n"
        "  therefore lives in the varṇa table and this function only reads it\n"
        "  off. 6.1.126 आङोऽनुनासिकश्छन्दसि, the Kāśikā's own example, is where\n"
        "  the name is put to use."
    ),
)


register(
    "1.1.9",
    samjna="savarṇa",
    apply=savarna,
    codification=(
        "savarna(a, b) -> bool: same sthāna and same ābhyantara prayatna. A "
        "two-place relation, not a property. Keyword switches turn off the ṛ/ḷ "
        "vārttika, turn off 1.1.10, or read the prayatnas fourfold, so each "
        "provision can be shown to be load-bearing."
    ),
    related=("1.1.10", "1.1.50", "1.1.69", "1.1.70", "6.1.101", "8.4.58", "8.4.65"),
    notes=(
        "SETTLED — savarṇa is a relation. The bhāṣya calls both terms\n""  — REPORTED, not checkable here; the passage is in none of the texts\n""  on disk —\n"
        "  सम्बन्धिशब्द and spells the reading out: यत् प्रति यत् तुल्यास्यप्रयत्नं\n"
        "  तत् प्रति तत् सवर्णसञ्ज्ञं भवति. Hence two arguments, not a class.\n"
        "\n"
        "SETTLED — only INTERNAL effort counts. k kh g gh ṅ differ in voice,\n"
        "  aspiration and nasality and are savarṇa regardless; that is what makes\n"
        "  8.4.58 parasavarṇa work. The Kāśikā on 1.1.69 states the ignored\n"
        "  dimensions outright: स्वरानुनासिक्यकालभिन्नस्य ग्रहणं भवति — accent,\n"
        "  nasality and duration are all disregarded.\n"
        "\n"
        "SETTLED — why both criteria. The Kāśikā gives the two discriminating\n"
        "  sets, and they are the test data here: आस्यग्रहणं किम्? कचटतपानां\n"
        "  भिन्नस्थानानां तुल्यप्रयत्नानां मा भूत् (k c ṭ t p, same effort,\n"
        "  different place); प्रयत्नग्रहणं किम्? इचुयशानां तुल्यस्थानानां\n"
        "  भिन्नजातीयानां मा भूत् (i c y ś, same place, different kind).\n"
        "\n"
        "SETTLED — ṛ and ḷ by vārttika. ऋकारऌकारयोः सवर्णसञ्ज्ञा विधेया, in\n"
        "  on this sūtra at Kielhorn I.62.27-63.23, repeated in the Kaumudī as\n"
        "  ऋऌवर्णयोर्मिथः सावर्ण्यं वाच्यम्. ṛ is mūrdhanya and ḷ dantya, so the\n"
        "  sūtra alone will not join them.\n"
        "\n"
        "SETTLED — र and the ūṣmans have no savarṇa: रेफोष्मणां सवर्णा न सन्ति.\n"
        "  This falls out of the feature table rather than being asserted —\n"
        "  savarnas_of('r') and savarnas_of('ṣ') each return the sound alone.\n"
        "\n"
        "SETTLED — e is not savarṇa with ai, nor o with au, though the two\n"
        "  criteria taken alone would join them: the Śikṣā gives each pair one\n"
        "  place (कण्ठतालु, कण्ठोष्ठम्) and all four are vivṛta. This was first\n"
        "  recorded here as an open question, on the reasoning that no rule\n"
        "  turns on the answer. That reasoning was wrong, and the code that\n"
        "  followed proved it: aiC in 1.1.1 is not tapara, so 1.1.69 widens it to\n"
        "  the savarṇas of ai and au, and if e were among them then vṛddhi would\n"
        "  contain e, which 1.1.2 makes guṇa. The two saṃjñās would overlap.\n"
        "  The Kāśikā says the same thing directly, in the enumeration on this\n"
        "  sūtra: सन्ध्यक्षराणां ह्रस्वा न सन्ति, तान्यपि द्वादशप्रभेदानि —\n"
        "  twelve sub-varieties, two lengths by three accents by two nasalities.\n"
        "  That passage counts varṇa by varṇa, eighteen for the a-varṇa and\n"
        "  twelve for the ḷ-varṇa, so twelve apiece for e and ai makes them two\n"
        "  varṇas and not one class of twenty-four. The separation is therefore\n"
        "  stated explicitly in varna.py rather than left to the features, and\n"
        "  savarna(enumeration=False) shows what the features alone would do."
    ),
)


register(
    "1.1.10",
    reuses=('1.1.9',),
    apply=blocked_by_na_ajjhalau,
    codification=(
        "The niṣedha lives inside savarna(), where it belongs — a separate "
        "predicate could be forgotten at a call site. What is registered here "
        "is blocked_by_na_ajjhalau(scheme), which reports the pairs the "
        "restriction actually rescues under a given reading of the prayatnas."
    ),
    related=("1.1.9", "6.1.101", "6.4.148"),
    notes=(
        "SETTLED — what it does: no vowel is savarṇa with a consonant, whatever\n"
        "  the features say. अच् च हल् च, अज्झलौ; तुल्यास्यप्रयत्नावपि अज्झलौ\n"
        "  परस्परं सवर्णसंज्ञौ न भवतः — 'even when they have equal place and\n"
        "  effort'. The अपि concedes that the features can match.\n"
        "\n"
        "SETTLED — how much work it does depends on how the prayatnas are\n"
        "  counted, and this is the sharpest place the two accounts part.\n"
        "  The Kāśikā's examples here are अवर्णहकारौ (दण्डहस्तः) and इवर्णशकारौ\n"
        "  (दधिशीतम्) — a with h, i with ś. Those pairs share a place, and share\n"
        "  an effort only if īṣadvivṛta has been folded into vivṛta, which is\n"
        "  precisely the fourfold count the Kāśikā gives on 1.1.9. Run\n"
        "  blocked_by_na_ajjhalau(FOURFOLD) and the sūtra rescues twelve\n"
        "  unordered pairs — a/h, i/ś, ṛ/ṣ, ḷ/s, u/upadhmānīya, a/visarga and\n"
        "  their long counterparts, the Kāśikā's two among them. Run it with\n"
        "  FIVEFOLD and it rescues nothing: the efforts have already parted every\n"
        "  pair. So on the Kaumudī's count 1.1.10 is idle, and on the Kāśikā's it\n"
        "  is indispensable. The pairs are derived from the feature table, not\n"
        "  typed in, so the agreement with the Kāśikā's two named examples is a\n"
        "  check on the table rather than a restatement of it.\n"
        "\n"
        "The Kāśikā's second consequence is worth keeping: without this sūtra\n"
        "  सवर्णदीर्घत्व (6.1.101) would wrongly fire in दधिशीतम्, and 6.4.148\n"
        "  यस्येति च would wrongly elide in वैपाशो मत्स्यः."
    ),
)


# ---------------------------------------------------------------------------
# प्रगृह्य — the vowels that refuse sandhi, 1.1.11 to 1.1.19
#
# Nine alternatives for one name, implemented together in
# src/astadhyayi/pragrhya.py because they are alternatives: a form reached by
# any of them bears the name, and none overrides another. What they have in
# common is the consequence, 6.1.125, which is not codified here.
# ---------------------------------------------------------------------------

register(
    "1.1.11",
    samjna="pragṛhya",
    apply=pragrhya,
    codification=(
        "The 1.1.11 branch of pragrhya(form, ...), which reports "
        "which of the nine gave the name and whether it did so optionally."
    ),
    related=("1.1.12", "1.1.19", "1.1.70", "6.1.125"),
    notes=(
        "SETTLED — three conditions, and the Kāśikā tests two of them.\n"
        "  ईदूदेदिति किम्? वृक्षावत्र — a dual in au is not pragṛhya, so the\n"
        "  three finals are exhaustive. द्विवचनमिति किम्? कुमार्यत्र — ī by\n"
        "  itself is not enough, it must be a dual. अग्नी, वायू, माले, पचेते\n"
        "  and पचेथे are the forms that do qualify.\n"
        "\n"
        "SETTLED — the finals are written tapara and the reason is given:\n"
        "  तपरकरणमसंदेहार्थम्, to remove doubt. By 1.1.70 that holds the name\n"
        "  to these lengths and keeps a pluta out.\n"
        "\n"
        "SETTLED — what the name is for. It has one consequence, 6.1.125\n"
        "  प्लुतप्रगृह्या अचि नित्यम्, which leaves the vowel unchanged before\n"
        "  another. That sūtra is not codified, so `blocks_sandhi` is named to\n"
        "  say only that its condition is met — none of these nine sūtras\n"
        "  performs or prevents a sandhi itself."
    ),
)

register(
    "1.1.12",
    apply=pragrhya,
    codification=(
        "The 1.1.12 branch of pragrhya(form, ...), which reports "
        "which of the nine gave the name and whether it did so optionally."
    ),
    related=("1.1.11", "6.1.125"),
    notes=(
        "SETTLED — both restrictions are tested by the Kāśikā. अदस इति किम्?\n"
        "  शम्यत्र, दाडिम्यत्र — other stems in ī are not reached. मादिति\n"
        "  किम्? अमुकेऽत्र — the vowel must stand after the m of अदस्.\n"
        "  Its own examples are अमी अत्र and अमू अत्र.\n"
        "\n"
        "SETTLED — a gap in the illustration, not in the rule: एकारस्य\n"
        "  नास्त्युदाहरणम्. ईदूदेत् is read down from 1.1.11 and so admits e,\n"
        "  but no form of अदस् supplies one. Recorded because an absent\n"
        "  example is not an absent case."
    ),
)

register(
    "1.1.13",
    apply=pragrhya,
    codification=(
        "The 1.1.13 branch of pragrhya(form, ...), which reports "
        "which of the nine gave the name and whether it did so optionally."
    ),
    related=("1.1.11", "7.1.39"),
    notes=(
        "SETTLED — शे is the Vedic sup-substitute of 7.1.39 सुपां सुलुक्...,\n"
        "  and this rule is Vedic with it: छान्दसमेतत्. The Kāśikā's examples\n"
        "  are युष्मे, अस्मे, त्वे, मे, each cited from the Ṛgveda or a\n"
        "  Saṃhitā with its padapāṭha reading beside it."
    ),
)

register(
    "1.1.14",
    apply=pragrhya,
    codification=(
        "The 1.1.14 branch of pragrhya(form, ...), which reports "
        "which of the nine gave the name and whether it did so optionally."
    ),
    related=("1.1.15", "6.1.125"),
    notes=(
        "SETTLED — एकाच् is a karmadhāraya and not a bahuvrīhi. The Kāśikā\n"
        "  glosses एकश्चासावच्चेत्येकाच् — 'it is one AND it is a vowel' — so\n"
        "  the particle must BE a single vowel, not merely contain one. The\n"
        "  sūtra's own counter-example settles it: एकाजिति किम्? प्राग्नये\n"
        "  वाचमीरय. प्र has one vowel and three sounds, and its sandhi goes\n"
        "  through. Reading एकाच् the other way would have made प्र pragṛhya,\n"
        "  and the first version of this codification did exactly that.\n"
        "\n"
        "SETTLED — अनाङ् excludes the preverb आ and not the vowel ā:\n"
        "  अनाङिति किम्? आ उदकान्तात् gives ओदकान्तात्. A bare ā is pragṛhya,\n"
        "  and the Kāśikā supplies आ एवं नु मन्यसे and आ एवं किल तत् for it,\n""  as do the Nyāsa and the Kaumudī.\n"
        "  So whether आङ् is meant is a fact about the passage and has to be\n"
        "  a parameter; the string cannot say.\n"
        "\n"
        "SETTLED — निपात इति किम्? चकारात्र, जहारात्र — a single-vowel word\n"
        "  that is not a particle is not reached."
    ),
)

register(
    "1.1.15",
    apply=pragrhya,
    codification=(
        "The 1.1.15 branch of pragrhya(form, ...), which reports "
        "which of the nine gave the name and whether it did so optionally."
    ),
    related=("1.1.14", "1.1.16"),
    notes=(
        "SETTLED — निपात is read down from 1.1.14, which the corpus records,\n"
        "  and the o carries तदन्तविधि: तस्यौकारेण तदन्तविधिः — a particle\n"
        "  ENDING in o, not a particle that is o. आहो and उताहो are the\n"
        "  examples, and neither is a bare o."
    ),
)

register(
    "1.1.16",
    apply=pragrhya,
    codification=(
        "The 1.1.16 branch of pragrhya(form, ...), which reports "
        "which of the nine gave the name and whether it did so optionally."
    ),
    related=("1.1.15", "1.1.17"),
    notes=(
        "SETTLED — four conditions at once, and all four are in the sūtra:\n"
        "  a vocative, an o, इति following, and non-Vedic. वायो इति,\n"
        "  भानो इति. सम्बुद्धाविति किम्? गवित्ययमाह. इताविति किम्? वायोऽत्र.\n"
        "\n"
        "SETTLED — naming an authority makes the rule optional:\n"
        "  शाकल्यग्रहणं विभाषार्थम्. This is a convention worth recording,\n"
        "  since nothing in the wording says विभाषा. Both वायो इति and\n"
        "  वायविति stand, so the result carries `optional`."
    ),
)

register(
    "1.1.17",
    apply=pragrhya,
    codification=(
        "The 1.1.17 branch of pragrhya(form, ...), which reports "
        "which of the nine gave the name and whether it did so optionally."
    ),
    related=("1.1.16", "1.1.18"),
    notes=(
        "SETTLED — शाकल्यस्य, इतौ and अनार्षे are all read down from 1.1.16,\n"
        "  which the corpus records, so this rule is optional for the same\n"
        "  reason: शाकल्यस्येति विभाषार्थम्. उ इति beside विति."
    ),
)

register(
    "1.1.18",
    apply=pragrhya,
    codification=(
        "The 1.1.18 branch of pragrhya(form, ...), which reports "
        "which of the nine gave the name and whether it did so optionally."
    ),
    related=("1.1.8", "1.1.17"),
    notes=(
        "SETTLED — this sūtra does two things at once. ऊँ is the substitute\n"
        "  for उञ् before इति, दीर्घोऽनुनासिकश्च — long and nasalised — and\n"
        "  it is pragṛhya as well. With 1.1.17 still optional the result is\n"
        "  त्रीणि रूपाणि: उ इति, विति, ऊँ इति.\n"
        "\n"
        "SETTLED — the form is written with a candrabindu on the vowel, and\n"
        "  the same character the varṇa layer uses for anunāsika, so\n"
        "  1.1.8's test recognises it. One of only three sūtras in the whole\n"
        "  text whose Vidyut witness carries the SLP1 tilde."
    ),
)

register(
    "1.1.19",
    apply=pragrhya,
    codification=(
        "The 1.1.19 branch of pragrhya(form, ...), which reports "
        "which of the nine gave the name and whether it did so optionally."
    ),
    related=("1.1.11",),
    notes=(
        "SETTLED — शाकल्यस्येतावनार्षे इति निवृत्तम्: the anuvṛtti from 1.1.16\n"
        "  stops here, so this rule is not optional and not tied to इति.\n"
        "  Only प्रगृह्यम् carries over.\n"
        "\n"
        "SETTLED — two finals and not three. ईदूताविति किम्? — e is excluded,\n"
        "  which is why the sūtra says ईदूतौ where 1.1.11 said ईदूदेत्.\n"
        "  The examples are Vedic locatives standing without their ending:\n"
        "  मामकी for मामक्याम्, तनू for तन्वाम्, गौरी for गौर्याम्."
    ),
)

# ---------------------------------------------------------------------------
# Saṃjñās that name a class of word or affix — 1.1.20 to 1.1.27
#
# Implemented in src/astadhyayi/samjna.py. Two of them point outside the
# Aṣṭādhyāyī for their membership — 1.1.20 at the dhātupāṭha, 1.1.27 at the
# Gaṇapāṭha — and both texts are on disk, so both lists are read.
# ---------------------------------------------------------------------------

register(
    "1.1.20",
    reuses=('1.3.2', '1.3.9'),
    samjna="ghu",
    apply=is_ghu,
    codification=(
        "is_ghu(root) -> bool, over the list ghu_roots() reads out of the d"
        "hātupāṭha. The shape test runs on the it-stripped stem, so 1.3.2-1"
        ".3.9 have to be right for this to be."
    ),
    related=("1.3.2", "1.3.3", "1.3.5"),
    notes=(
        "SETTLED — the members are in another text, and it is here. The\n"
        "  dhātupāṭha holds eight roots that are or become दा or धा once\n"
        "  1.3.2-1.3.9 have taken their it-letters off: धेट्, दैप्, दाण्,\n"
        "  देङ्, दाप्, डुदाञ्, डुधाञ्, दो. The sūtra's अदाप् removes\n"
        "  दाप्, the Kāśikā removes दैप् with it — दाब्दैपौ वर्जयित्वा —\n"
        "  and the six that remain are exactly the six the Kāśikā names.\n"
        "\n"
        "SETTLED — why the shape test admits दो, दे, दै and धे and not\n"
        "  only दा and धा: 6.1.45 आदेच उपदेशेऽशिति turns a final ec into\n"
        "  ā in upadeśa, so those count as dā- and dhā-roots. It matters\n"
        "  for दैप् above all. A first version left दै out of the shape\n"
        "  set and so reached the right six by the wrong route: दैप् was\n"
        "  being dropped for having the wrong form, where the tradition\n"
        "  drops it by name, and the sūtra's exclusion was doing half the\n"
        "  work it should. A test comparing the candidate count against\n"
        "  the exclusion is what caught it.\n"
        "\n"
        "SETTLED — the Kāśikā's own count is the check:\n"
        "  दारूपाश्चत्वारो धातवो धारूपौ च द्वौ, four of dā-form and two of\n"
        "  dhā-form. डुदाञ्, दाण्, दो, देङ् are the four; डुधाञ् and धेट्\n"
        "  the two. A shape test that admitted one more or one fewer would\n"
        "  fail that count before it failed anything else."
    ),
)

register(
    "1.1.21",
    apply=positions,
    codification=(
        "positions(length, index) -> the set of ādi/anta/madhya an item occ"
        "upies. A sequence of one yields both ends, which is the whole sūtr"
        "a."
    ),
    related=("3.1.3", "7.3.102"),
    notes=(
        "SETTLED — an atideśa for the companionless:\n"
        "  असहायस्याद्यन्तोपदिष्टानि कार्याणि न सिध्यन्तीत्ययमतिदेश आरभ्यते.\n"
        "  A rule taught for a first or a last would slip past something that\n"
        "  is alone, so this makes it both — आदाविव अन्त इव एकस्मिन्नपि\n"
        "  कार्यं भवति.\n"
        "\n"
        "SETTLED — सप्तम्यर्थे वतिः: the वति here has the sense of a locative,\n"
        "  not of comparison, which is why the codification is about position\n"
        "  and not about likeness. The Kāśikā's two illustrations are both of\n"
        "  a one-item sequence: the affix accent of 3.1.3 reaching औपगवम्,\n"
        "  and the lengthening of 7.3.102 reaching आभ्याम्."
    ),
)

register(
    "1.1.22",
    samjna="gha",
    apply=is_gha,
    codification=(
        "is_gha(affix) -> bool over the two the sūtra names."
    ),
    related=("6.3.43",),
    notes=(
        "SETTLED — two affixes and nothing else: तरप् and तमप्, in upadeśa,\n"
        "  each with an indicatory p by 1.3.3. कुमारितरा, कुमारितमा,\n"
        "  ब्राह्मणितरा, ब्राह्मणितमा."
    ),
)

register(
    "1.1.23",
    apply=is_samkhya,
    codification=(
        "is_samkhya(word) -> bool: the four the sūtra adds, and the numeral"
        "s, which bear the name already."
    ),
    related=("1.1.24", "1.1.25"),
    notes=(
        "SETTLED — the sūtra adds four words that are not numerals:\n"
        "  बहु, गण, वतु, डति. भूर्यादीनां निवृत्त्यर्थं संख्यासंज्ञा विधीयते —\n"
        "  the name is prescribed for these so as to keep भूरि and its like\n"
        "  out. Its examples run each of the four through the same four\n"
        "  affixes: बहुकृत्वः, बहुधा, बहुकः, बहुशः, and so for गण, तावत्, कति.\n"
        "\n"
        "SCOPE — a semantic condition is not applied. बहुगणशब्दयोर्वैपुल्ये\n"
        "  संङ्घे च वर्तमानयोरिह ग्रहणं नास्ति, संख्यावाचिनोरेव: बहु and गण\n"
        "  are meant only where they denote number, not where they mean\n"
        "  'much' or 'a troop'. Deciding which sense is in play needs a\n"
        "  semantics this project has not got, so the codification admits the\n"
        "  words and the docstring says a caller who knows the sense should\n"
        "  not pass them in the wrong one."
    ),
)

register(
    "1.1.24",
    reuses=('1.1.23',),
    samjna="ṣaṭ",
    apply=is_sat,
    codification=(
        "The ṣ/n branch of is_sat, on the upadeśa form."
    ),
    related=("1.1.23", "1.1.25", "7.1.22", "7.1.55"),
    notes=(
        "SETTLED — संख्या is read down from 1.1.23, which the corpus records,\n"
        "  so only number words are reached. षष् ends in ṣ; पञ्चन्, सप्तन्,\n"
        "  नवन्, दशन् in n.\n"
        "\n"
        "SETTLED — the final is of the ENUNCIATED form and the sūtra's अन्त\n"
        "  says so: अन्तग्रहणमौपदेशिकार्थम्। तेनेह न भवति — शतानि, सहस्राणि.\n"
        "  शत and सहस्र end in a and are not ṣaṭ, though they are numerals.\n"
        "  So the test is run on पञ्चन् and not on पञ्च, and NUMERALS holds\n"
        "  the upadeśa forms for that reason."
    ),
)

register(
    "1.1.25",
    reuses=('1.1.23',),
    apply=is_sat,
    codification=(
        "The ḍati branch of is_sat."
    ),
    related=("1.1.23", "1.1.24"),
    notes=(
        "SETTLED — षट् and संख्या both come down by anuvṛtti, which the corpus\n"
        "  records, so this adds one more ending to 1.1.24 rather than\n"
        "  starting again: कति तिष्ठन्ति, कति पश्य."
    ),
)

register(
    "1.1.26",
    samjna="niṣṭhā",
    apply=is_nistha,
    codification=(
        "is_nistha(affix) -> bool over the two the sūtra names."
    ),
    related=("1.1.5", "1.3.8", "7.2.14"),
    notes=(
        "SETTLED — क्त and क्तवतु: कृतः, कृतवान्, भुक्तः, भुक्तवान्.\n"
        "\n"
        "SETTLED — the Kāśikā says what each indicatory letter is for, and\n"
        "  both are already codified: ककारः कित्कार्यार्थः — the k makes the\n"
        "  affix kit, which 1.1.5 uses to block guṇa, and 1.3.8 is what makes\n"
        "  the k indicatory in the first place. उकार उगित्कार्यार्थः — the u\n"
        "  makes it ugit. So चि + क्त gives चितः, and that derivation runs\n"
        "  through this sūtra, 1.3.8 and 1.1.5 together."
    ),
)

register(
    "1.1.27",
    samjna="sarvanāman",
    apply=is_sarvanaman,
    codification=(
        "is_sarvanaman(word) -> bool over the sarvādi gaṇa, read from the G"
        "aṇapāṭha rather than copied."
    ),
    related=("2.3.27",),
    notes=(
        "SETTLED — सर्वादि means 'sarva and the rest', and the rest are in\n"
        "  another text. The Gaṇapāṭha keys its सर्वादि to this very sūtra and\n"
        "  gives thirty-five members, from सर्व and विश्व through तद्, यद्,\n"
        "  एतद्, इदम्, अदस् to किम्. A list of that length copied by hand\n"
        "  would be wrong somewhere and nothing would catch it.\n"
        "\n"
        "SETTLED — the gaṇa is closed and not an आकृतिगण, so membership is\n"
        "  decidable. Of the 262 gaṇas in the Gaṇapāṭha 39 are ākṛti and this\n"
        "  is not one, which is what makes is_sarvanaman a total function.\n"
        "\n"
        "SETTLED — three members carry conditions, and the Gaṇapāṭha records\n"
        "  them as comments beside the words: पूर्व and its group are\n"
        "  sarvanāman व्यवस्थायामसंज्ञायाम्, स्व only where it means neither\n"
        "  kinsman nor wealth, अन्तर in the sense of what lies outside or\n"
        "  of an undergarment. Those are not glosses on the gaṇa but pointers\n"
        "  to 1.1.34, 1.1.35 and 1.1.36, and all three are now codified. This\n"
        "  entry admits the words unconditionally, which is right: by this\n"
        "  sūtra they simply are sarvanāman, and the three later ones make\n"
        "  the name optional before jas under those senses. Recorded here\n"
        "  as a SCOPE before they were done, and closed by doing them."
    ),
)

# ---------------------------------------------------------------------------
# What qualifies the sarvanāman saṃjñā — 1.1.28 to 1.1.36
#
# Nine sūtras that take the name away and give it back, each stated against the
# one before. They are read as one decision in src/astadhyayi/samjna.py, which
# is the only way to get the answer right: 1.1.28 relieves a prohibition
# 1.1.29 has not yet made, and 1.1.32 relieves one 1.1.31 just made.
# ---------------------------------------------------------------------------

register(
    "1.1.28",
    reuses=('1.1.27',),
    apply=sarvanaman,
    codification=(
        "The 1.1.28 branch of sarvanaman(word, ...), which reports "
        "whether the name applies, whether by option, and on whose "
        "authority."
    ),
    related=("1.1.27", "1.1.29"),
    notes=(
        "SETTLED — stated in advance of the prohibition it relieves. The\n"
        "  Kāśikā is explicit about the order of argument: न बहुव्रीहौ इति\n"
        "  प्रतिषेधं वक्ष्यति, तस्मिन्नित्ये प्रतिषेधे प्राप्ते विभाषेयम्\n"
        "  आरभ्यते — 1.1.29 is about to forbid the name in every bahuvrīhi,\n"
        "  and this makes it optional in the one kind built of directions.\n"
        "  उत्तरपूर्वस्यै beside उत्तरपूर्वायै, दक्षिणपूर्वस्यै beside\n"
        "  दक्षिणपूर्वायै.\n"
        "\n"
        "SETTLED — which is why the codification tests DIK_BAHUVRIHI before\n"
        "  BAHUVRIHI. Reverse them and this sūtra can never fire."
    ),
)

register(
    "1.1.29",
    reuses=('1.1.27',),
    apply=sarvanaman,
    codification=(
        "The 1.1.29 branch of sarvanaman(word, ...), which reports "
        "whether the name applies, whether by option, and on whose "
        "authority."
    ),
    related=("1.1.27", "1.1.28", "1.1.30"),
    notes=(
        "SETTLED — why a prohibition is needed at all: सर्वनामसंज्ञायां\n"
        "  तदन्तविधेरभ्युपगमाद् बहुव्रीहेरपि सर्वाद्यन्तस्य संज्ञा स्यात्.\n"
        "  The saṃjñā is taken to extend to what ENDS in a sarvādi, so a\n"
        "  bahuvrīhi whose last member is one would pick the name up.\n"
        "  प्रियविश्वाय, प्रियोभयाय, द्व्यन्याय, त्र्यन्याय.\n"
        "\n"
        "SETTLED — a vārttika is recorded on this sūtra and is not codified:\n"
        "  अकच्स्वरौ तु कर्तव्यौ प्रत्यङ्गं मुक्तसंशयम्. It concerns the\n"
        "  अकच् infix and accent, neither of which exists here. The Kāśikā's\n"
        "  त्वत्कपितृको, मत्कपितृको illustrate the akac half."
    ),
)

register(
    "1.1.30",
    reuses=('1.1.27',),
    apply=sarvanaman,
    codification=(
        "The 1.1.30 branch of sarvanaman(word, ...), which reports "
        "whether the name applies, whether by option, and on whose "
        "authority."
    ),
    related=("1.1.29", "1.1.31"),
    notes=(
        "SETTLED — न comes down from 1.1.29, which the corpus records, so\n"
        "  this adds a second compound to the prohibition rather than\n"
        "  starting a new one: मासपूर्वाय, संवत्सरपूर्वाय, द्व्यहपूर्वाय.\n"
        "\n"
        "SETTLED — समास is said again on purpose: समास इति वर्तमाने पुनः\n"
        "  समासग्रहणं तृतीयासमासार्थवाक्येऽपि प्रतिषेधो यथा स्यात् — so that\n"
        "  the prohibition reaches the uncompounded phrase too, मासेन\n"
        "  पूर्वाय. Not represented: the codification takes a compound type\n"
        "  and has no way to be told that a phrase means the same."
    ),
)

register(
    "1.1.31",
    apply=sarvanaman,
    codification=(
        "The 1.1.31 branch of sarvanaman(word, ...), which reports "
        "whether the name applies, whether by option, and on whose "
        "authority."
    ),
    related=("1.1.29", "1.1.32"),
    notes=(
        "SETTLED — the third compound, and the shortest statement of it:\n"
        "  पूर्वापराणाम्, कतरकतमानाम्. न is again read down from 1.1.29."
    ),
)

register(
    "1.1.32",
    apply=sarvanaman,
    codification=(
        "The 1.1.32 branch of sarvanaman(word, ...), which reports "
        "whether the name applies, whether by option, and on whose "
        "authority."
    ),
    related=("1.1.31", "1.1.33"),
    notes=(
        "SETTLED — the same shape as 1.1.28: पूर्वेण नित्ये प्रतिषेधे प्राप्ते\n"
        "  जसि विभाषाऽऽरभ्यते. 1.1.31 forbids the name in a dvandva without\n"
        "  qualification, and before jas this makes the prohibition optional.\n"
        "  कतरकतमे beside कतरकतमाः.\n"
        "\n"
        "SETTLED — the option is of the saṃjñā and not of everything that\n"
        "  follows from it: जसः कार्यं प्रति विभाषाऽकज् हि न भवति. The akac\n"
        "  does not appear either way, so कतरकतमकाः stands alone. Not\n"
        "  codified; akac is elsewhere."
    ),
)

register(
    "1.1.33",
    apply=sarvanaman,
    codification=(
        "The 1.1.33 branch of sarvanaman(word, ...), which reports "
        "whether the name applies, whether by option, and on whose "
        "authority."
    ),
    related=("1.1.27", "1.1.32", "1.1.34"),
    notes=(
        "SETTLED — seven words the gaṇa does NOT contain, given the name\n"
        "  optionally before jas. That is the difference between this sūtra\n"
        "  and the three after it: प्रथम, चरम, अल्प, अर्ध, कतिपय, नेम have no\n"
        "  claim to the name otherwise, while पूर्व, स्व and अन्तर are in the\n"
        "  gaṇa and hold it already. प्रथमे beside प्रथमाः, चरमे beside\n"
        "  चरमाः, अल्पे beside अल्पाः.\n"
        "\n"
        "SETTLED — तय is an affix and not a word. The Kāśikā treats it as\n"
        "  तयबन्त and illustrates with द्वितये beside द्वितयाः, so the test\n"
        "  is on the ending.\n"
        "\n"
        "SETTLED — the anuvṛtti narrows here and the Kāśikā says which part\n"
        "  goes: विभाषा जसि इति वर्त्तते, द्वन्द्वे इति निवृत्तम्. The\n"
        "  dvandva condition stops; the option and the jas carry on. न stops\n"
        "  too, and the corpus records the change — these four sūtras GIVE\n"
        "  the name where 1.1.29 to 1.1.31 withheld it."
    ),
)

register(
    "1.1.34",
    apply=sarvanaman,
    codification=(
        "The 1.1.34 branch of sarvanaman(word, ...), which reports "
        "whether the name applies, whether by option, and on whose "
        "authority."
    ),
    related=("1.1.27", "1.1.33"),
    notes=(
        "SETTLED — these seven ARE in the sarvādi gaṇa, and the Gaṇapāṭha\n"
        "  annotates them with this very sūtra. So 1.1.27 gives them the name\n"
        "  outright — पूर्वेण नित्यायां सर्वनामसञ्ज्ञायां प्राप्तायाम् — and\n"
        "  what this sūtra does is relax it before jas: पूर्वे beside पूर्वाः.\n"
        "  This is the same seven the note on 1.1.27 recorded as a SCOPE, and\n"
        "  codifying it discharges that.\n"
        "\n"
        "SETTLED — व्यवस्था is defined in the Kāśikā and the definition is\n"
        "  what makes the condition testable in principle:\n"
        "  स्वाभिधेयापेक्षावधिनियमो व्यवस्था — a fixed relation of limit with\n"
        "  respect to what the word denotes. Whether a given use has it is a\n"
        "  question about meaning, so it is a parameter."
    ),
)

register(
    "1.1.35",
    apply=sarvanaman,
    codification=(
        "The 1.1.35 branch of sarvanaman(word, ...), which reports "
        "whether the name applies, whether by option, and on whose "
        "authority."
    ),
    related=("1.1.27", "1.1.34"),
    notes=(
        "SETTLED — स्व is in the gaṇa, so again the name is obligatory by\n"
        "  1.1.27 and this relaxes it before jas: स्वे पुत्राः beside स्वाः\n"
        "  पुत्राः, स्वे गावः beside स्वा गावः, in the sense आत्मीय.\n"
        "\n"
        "SETTLED — the exclusion is semantic and doubled: neither ज्ञाति nor\n"
        "  धन. Where स्व names a kinsman or wealth the relaxation is off and\n"
        "  1.1.27 stands. A parameter, for the same reason as 1.1.34's."
    ),
)

register(
    "1.1.36",
    apply=sarvanaman,
    codification=(
        "The 1.1.36 branch of sarvanaman(word, ...), which reports "
        "whether the name applies, whether by option, and on whose "
        "authority."
    ),
    related=("1.1.27", "1.1.35"),
    notes=(
        "SETTLED — अन्तर is in the gaṇa, and the two senses in which the\n"
        "  option holds are named: बहिर्योग, what lies outside — अन्तरे गृहाः\n"
        "  beside अन्तरा गृहाः, glossed नगरबाह्याश्चाण्डालादिगृहाः — and\n"
        "  उपसंव्यान, an undergarment: अन्तरे शाटकाः beside अन्तराः शाटकाः.\n"
        "\n"
        "SCOPE — two vārttikas stand on this sūtra and neither is codified:\n"
        "  अपुरीति वक्तव्यम्, excluding the sense of a city, and\n"
        "  विभाषाप्रकरणे तीयस्य ङित्सूपसंख्यानम्, adding तीय-final words\n"
        "  before ṅit endings. Both were found in the vārttika collection."
    ),
)

# ---------------------------------------------------------------------------
# 1.1.37 to 1.1.48 — indeclinables, sarvanāmasthāna, vibhāṣā, and three
# paribhāṣās about placement
#
# Four small groups. The avyaya block is in src/astadhyayi/avyaya.py, the two
# saṃjñās in samjna.py, and 1.1.45 to 1.1.48 in adesa.py beside the other rules
# about where something goes.
# ---------------------------------------------------------------------------

register(
    "1.1.37",
    samjna="avyaya",
    apply=avyaya,
    codification=(
        "The svarādi and nipāta branch of avyaya(form, ...). Both lists c"
        "ome from the Gaṇapāṭha."
    ),
    related=("1.1.38", "1.4.57", "2.4.82"),
    notes=(
        "SETTLED — two gaṇas, and both are ākṛtigaṇa. स्वरादि lists 160\n"
        "  members and चादि 155, and neither is closed, so a word in the\n"
        "  list is certainly avyaya and a word absent from it may still be\n"
        "  one. `Avyaya.certain` carries the difference. That is the grammar\n"
        "  and not a gap in the data: an ākṛtigaṇa is completed by usage.\n"
        "\n"
        "SETTLED — what the name is for: 2.4.82 अव्ययादाप्सुपः elides the\n"
        "  ending. The five sūtras of this block have nothing else in common,\n"
        "  which is why the codification reports which one applied."
    ),
)

register(
    "1.1.38",
    apply=avyaya,
    codification=(
        "The taddhita branch."
    ),
    related=("1.1.37",),
    notes=(
        "SETTLED — the condition is the absence of a full paradigm, and the\n"
        "  Kāśikā defines it: यस्मान्न सर्वविभक्तेरुत्पत्तिः सोऽसर्वविभक्तिः.\n"
        "  ततः, यतः, तत्र, यत्र, तदा, यदा, सर्वदा, सदा are avyaya;\n"
        "  औपगवः, औपगवौ, औपगवाः are not, because they inflect throughout.\n"
        "\n"
        "SETTLED — तद्धितः इति किम्? एकः, द्वौ, बहवः — a word with a defective\n"
        "  paradigm that does not end in a taddhita is untouched."
    ),
)

register(
    "1.1.39",
    reuses=('1.1.71',),
    apply=avyaya,
    codification=(
        "The kṛt branch: a kṛt-final in m or in eC, the eC resolved throu"
        "gh 1.1.71 rather than listed."
    ),
    related=("1.1.37", "1.1.71"),
    notes=(
        "SETTLED — two endings, and the second is a pratyāhāra, so it is\n"
        "  resolved and not written out. स्वादुंकारं भुङ्क्ते, सम्पन्नंकारं\n"
        "  भुङ्क्ते, लवणंकारं भुङ्क्ते for the m; वक्षे रायः and क्रत्वे\n"
        "  दक्षाय जीवसे for the eC, both Vedic."
    ),
)

register(
    "1.1.40",
    apply=avyaya,
    codification=(
        "The three named affixes."
    ),
    related=("1.1.37", "3.4.16"),
    notes=(
        "SETTLED — क्त्वा, तोसुन्, कसुन्. कृत्वा and हृत्वा for the first;\n"
        "  पुरा सूर्यस्योदेतोः and पुरा वत्सानामपाकर्तोः for तोसुन्, which\n"
        "  3.4.16 prescribes."
    ),
)

register(
    "1.1.41",
    apply=avyaya,
    codification=(
        "The avyayībhāva branch."
    ),
    related=("1.1.37", "2.4.82", "6.2.167"),
    notes=(
        "SETTLED — the Kāśikā asks what the name buys here and answers\n"
        "  लुङ्मुखस्वरोपचाराः: the elision of 2.4.82 giving उपाग्नि and\n"
        "  प्रत्यग्नि, and then the accent that follows, where 6.2.167\n"
        "  मुखं स्वाङ्गम् would otherwise have placed it elsewhere."
    ),
)

register(
    "1.1.42",
    samjna="sarvanāmasthāna",
    apply=sarvanamasthana,
    codification=(
        "sarvanamasthana(affix, napumsaka=...) -> which sūtra names it, o"
        "r None."
    ),
    related=("1.1.43", "7.1.20"),
    notes=(
        "SETTLED — शि is the substitute 7.1.20 जश्शसोः शिः puts for jas and\n"
        "  śas: कुण्डानि तिष्ठन्ति, कुण्डानि पश्य, दधीनि, मधूनि. It is also\n"
        "  the affix 1.1.55 reaches as śit, so the two sūtras meet on it."
    ),
)

register(
    "1.1.43",
    apply=sarvanamasthana,
    codification=(
        "The suṬ branch, with the neuter exception."
    ),
    related=("1.1.42", "4.1.2"),
    notes=(
        "SETTLED — सुट् is the first five sup endings, from the enumeration\n"
        "  4.1.2 स्वौजसमौट्... It is not resolvable from the śivasūtras: the\n"
        "  pratyāhāra is formed inside the sup-list, which is a separate\n"
        "  enunciation, so SUT is stated with that sūtra beside it.\n"
        "  राजा, राजानौ, राजानः, राजानम्. सुडिति किम्? राज्ञः पश्य.\n"
        "\n"
        "SETTLED — the exception does not cut both ways, and this is the\n"
        "  point that decides the order of the tests: नपुंसके न विधिर्न\n"
        "  प्रतिषेधः, तेन जसः शेः सर्वनामस्थानसंज्ञा पूर्वेण भवत्येव. For a\n"
        "  neuter there is here neither a grant nor a refusal, so a neuter's\n"
        "  शि keeps the name 1.1.42 already gave it. Test suṬ first and the\n"
        "  neuter case would wrongly come back empty."
    ),
)

register(
    "1.1.44",
    samjna="vibhāṣā",
    apply=vibhasa,
    codification=(
        "vibhasa(word) -> which of the two the word is, or None."
    ),
    related=("1.1.28", "1.1.32", "1.1.68"),
    notes=(
        "SETTLED — one name for two different things: नेति प्रतिषेधो वेति\n"
        "  विकल्पः. So every rule already codified that reports `optional`\n"
        "  is reporting this saṃjñā — 1.1.28, 1.1.32, 1.1.33 to 1.1.36 all\n"
        "  say विभाषा, and 1.1.16's optionality comes by the same road.\n"
        "\n"
        "SETTLED — how the two act together where both are available:\n"
        "  तत्र प्रतिषेधेन समीकृते विषये पश्चाद् विकल्पः प्रवर्तते, the\n"
        "  prohibition levels the ground and the option then operates. Not\n"
        "  codified — it describes how two rules interact, and nothing here\n"
        "  yet runs rules against each other.\n"
        "\n"
        "SETTLED — the इति is 1.1.68 showing up inside the text:\n"
        "  इतिकरणोऽर्थनिर्देशार्थः, it marks that the WORDS न and वा are\n"
        "  meant and not their senses. Without it the sūtra would be about\n"
        "  prohibition and choice rather than about two syllables."
    ),
)

register(
    "1.1.45",
    samjna="samprasāraṇa",
    apply=samprasarana,
    reuses=("1.1.71",),
    codification=(
        "samprasarana(before, after) -> bool: a yaṆ giving way to an iK. "
        "Both classes resolved through 1.1.71."
    ),
    related=("1.1.71", "6.1.13"),
    notes=(
        "SETTLED — the name is of a relation and not of a sound: इग्यो यणः\n"
        "  स्थाने भूतो भावी वा, an iK that has come to stand in a yaṆ's room\n"
        "  or is about to. Hence two arguments. यज् gives इष्टम्, वप् gives\n"
        "  उप्तम्, ग्रह् gives गृहीतम् — y to i, v to u, r to ṛ.\n"
        "\n"
        "SETTLED — the Kāśikā records a disagreement and does not settle it:\n"
        "  केचिदुभयथा सूत्रमिदं व्याचक्षते — some explain the sūtra both\n"
        "  ways, as naming the whole substitution-relation, and as naming the\n"
        "  vowel alone. The first reading is taken here because it is the one\n"
        "  the Kāśikā states first and at length. Recorded rather than\n"
        "  presented as the only reading."
    ),
)

register(
    "1.1.46",
    apply=agama_site,
    codification=(
        "The ṭit and kit branches of agama_site(its). The marks are read "
        "off the augment by 1.3.2-1.3.9, not declared."
    ),
    related=("1.1.47", "1.3.3", "7.2.35", "7.3.40"),
    notes=(
        "SETTLED — आदिष्टिद् भवति अन्तःकिद् भवति षष्ठीनिर्दिष्टस्य: a ṭit\n"
        "  augment is the beginning of what the genitive named, a kit augment\n"
        "  its end. इट् at 7.2.35 आर्धधातुकस्येड् वलादेः is ṭit, giving\n"
        "  लविता; षुक् at 7.3.40 भियो हेतुभये षुक् is kit, giving\n"
        "  मुण्डो भीषयते.\n"
        "\n"
        "SETTLED — this is the companion of 1.1.52 and 1.1.54. Those say\n"
        "  where a substitute lands, these where an augment does, and both\n"
        "  read the same genitive by 1.1.49."
    ),
)

register(
    "1.1.47",
    apply=agama_site,
    codification=(
        "The mit branch: after the last vowel."
    ),
    related=("1.1.46", "1.1.64", "3.1.1"),
    notes=(
        "SETTLED — अचां संनिविष्टानामन्त्यादचः परो मिद् भवति, and अचः is\n"
        "  again a genitive of selection rather than of substitution —\n"
        "  अचः इति निर्धारणे षष्ठी, जातौ चेदमेकवचनम्, the same wording as\n"
        "  1.1.64. Two of the three ṣaṣṭhīs in this pāda that are not\n"
        "  1.1.49's, and both are flagged as such by the Kāśikā.\n"
        "\n"
        "SETTLED — it is an अपवाद: स्थानेयोगप्रत्ययपरत्वस्य अयमपवादः. Left\n"
        "  alone, an affix would simply follow what it is added to, by 3.1.1\n"
        "  and 3.1.2; a mit augment goes inside instead. विरुणद्धि,\n"
        "  मुञ्चति, पयांसि.\n"
        "\n"
        "SCOPE — a vārttika on this sūtra is not codified:\n"
        "  अन्त्यात्पूर्वो मस्जेरनुषङ्गसंयोगादिलोपार्थम्, putting the\n"
        "  augment BEFORE the last vowel for मस्ज्. Found in the vārttika\n"
        "  collection; it needs the root to be identified, which the\n"
        "  codification does not take."
    ),
)

register(
    "1.1.48",
    reuses=('1.1.50', '1.1.71'),
    apply=hrasva_of_ec,
    codification=(
        "hrasva_of_ec(vowel) -> the short substitute, computed by 1.1.50 "
        "over iK rather than tabulated."
    ),
    related=("1.1.50", "1.1.71", "1.2.47"),
    notes=(
        "SETTLED — इगेव ह्रस्वो भवति नान्यः: the short substitute for an eC\n"
        "  is an iK and nothing else. WHICH iK the sūtra does not say and\n"
        "  need not — 1.1.50 settles it, and the answers are the Kāśikā's:\n"
        "  रै gives अतिरि, नौ gives अतिनु, गो gives उपगु. So e goes to i and\n"
        "  o to u because i shares तालु with e and u shares ओष्ठ with o, and\n"
        "  none of that is written down here.\n"
        "\n"
        "SETTLED — both conditions are tested. एच इति किम्? अतिखट्वः,\n"
        "  अतिमालः — the rule is for the four diphthongs only.\n"
        "  ह्रस्वादेशे इति किम्? देवदत्त, दे३वदत्त — where no short\n"
        "  substitute is called for, nothing happens."
    ),
)

# ---------------------------------------------------------------------------
# The substitution paribhāṣās — 1.1.49 to 1.1.52
#
# Implemented in src/astadhyayi/adesa.py, which measures nearness with the
# feature table 1.1.9 already needed. Together these four discharge the promise
# made in the note on 1.1.3: the guṇa and vṛddhi correspondences are computed
# here, not tabulated anywhere.
# ---------------------------------------------------------------------------


register(
    "1.1.49",
    apply=sthanin_padas,
    codification=(
        "sthanin_padas(sutra_id) -> the sūtra's genitive words, read from the "
        "corpus's own case marking. The rule is a convention about how to read "
        "the text, so applying it is reading the text."
    ),
    related=("1.1.50", "1.1.51", "1.1.52", "1.1.56"),
    notes=(
        "SETTLED — it restricts, it does not add: परिभाषेयं योगनियमार्था. The\n"
        "  genitive already has many senses, and the Kāśikā lists them —\n"
        "  स्वस्वाम्यनन्तरसमीपसमूहविकारावयवाद्याः, ownership, proximity,\n"
        "  aggregate, modification, part. Where a rule leaves the sense open,\n"
        "  this one fixes it as स्थाने, 'in the room of'.\n"
        "\n"
        "SETTLED — स्थान means प्रसङ्ग, occasion, not location: स्थानशब्दश्च\n"
        "  प्रसङ्गवाची, with the simile यथा दर्भाणां स्थाने शरैः प्रस्तरितव्यम्,\n"
        "  'as one strews with śara reeds in the room of darbha grass'. So\n"
        "  अस्तेः स्थाने means where as would have occurred, bhū occurs.\n"
        "\n"
        "SETTLED — the codification is genuine and not a restatement, because\n"
        "  the corpus records vibhakti for every pada of all 3,983 sūtras. That\n"
        "  makes the rule executable over the whole text rather than over a\n"
        "  handful of hand-marked examples, and the tests exercise it that way."
    ),
)


register(
    "1.1.50",
    apply=antaratama,
    codification=(
        "antaratama(sthanin, candidates) -> the nearest, as a tuple, since a "
        "tie is a fact and not an error. `nearness` and `ranked` expose the "
        "comparison so a choice can be explained rather than merely made."
    ),
    related=("1.1.9", "1.1.49", "1.1.51", "6.1.101", "7.3.52", "8.2.80", "8.4.62"),
    notes=(
        "SETTLED — the four dimensions, from the Kāśikā: कुतश्च शब्दस्यान्तर्यम्?\n"
        "  स्थानार्थगुणप्रमाणतः — place, meaning, quality, measure. Each has its\n"
        "  own worked example there, and each is a test case here:\n"
        "    स्थानतः   6.1.101, दण्डाग्रम् — of two a's the long ā, also kaṇṭhya\n"
        "    गुणतः    7.3.52, पाकः/त्यागः — c to k and j to g, matching voice\n"
        "              and aspiration\n"
        "    प्रमाणतः  8.2.80, अमुष्मै/अमूभ्याम् — short for short, long for long\n"
        "    अर्थतः    वातण्ड्ययुवतिः — NOT implemented; it needs a semantics\n"
        "              this project does not have, and is left out rather than\n"
        "              faked. Nearness records the omission.\n"
        "\n"
        "SETTLED — place outranks the rest, and the sūtra repeats स्थाने to say\n"
        "  so: स्थाने इति वर्त्तमाने पुनः स्थानेग्रहणं किम्? यत्रानेकमान्तर्यं\n"
        "  संभवति तत्र स्थानत एवान्तर्यं बलीयो यथा स्यात्. The Kāśikā's example\n"
        "  is the decisive test of the whole design: चेता। स्तोता। प्रमाणतोऽकारो\n"
        "  गुणः प्राप्तः, तत्र स्थानत आन्तर्यादेकारौकारौ भवतः — by measure a\n"
        "  would be the guṇa of i, but place is stronger and gives e.\n"
        "\n"
        "SETTLED — this is why sthāna had to be decomposed into articulators.\n"
        "  As an atomic label, tālavya and kaṇṭhatālavya are simply different\n"
        "  and i would be no nearer to e than to a; the Śikṣā's compound names\n"
        "  say otherwise, and cetā is unexplainable without reading them apart.\n"
        "\n"
        "SETTLED — तम is a real superlative: the count matters, not the mere\n"
        "  fact of a match. तमब्ग्रहणं किम्? वाग्घसति — for h by 8.4.62, being\n"
        "  सोष्मन् argues for the aspirate and being नादवत् for the voiced, and\n"
        "  तमब्ग्रहणाद् ये सोष्माणो नादवन्तश्च ते भवन्ति चतुर्थाः: the fourth of\n"
        "  the varga wins by being both. Hence shared features are counted."
    ),
)


register(
    "1.1.51",
    apply=raparatva,
    codification=(
        "raparatva(sthanin, substitute) -> the substitute with r appended, when "
        "the sthānin is ṛ and the substitute an aṆ. It composes after 1.1.50 "
        "rather than replacing it."
    ),
    related=("1.1.3", "1.1.49", "1.1.50", "4.1.97"),
    notes=(
        "SETTLED — ṛ is not special-cased in the choosing, only in the\n"
        "  finishing. ṛ shares no articulator with a, e or o, but it stands two\n"
        "  articulators from a and three from each of e and o, so 1.1.50 selects\n"
        "  a unaided. This sūtra then supplies the r, which is what its own\n"
        "  wording assumes: उः स्थानेऽण् प्रसज्यमान एव रपरो, 'an aṆ *arising* in\n"
        "  the room of ṛ', takes for granted that something else produced it.\n"
        "  So guṇa of ṛ is ar and vṛddhi ār, both computed.\n"
        "\n"
        "SETTLED — both conditions are tested because the Kāśikā tests both.\n"
        "  उरिति किम्? खेयम्। गेयम् — the sthānin must be ṛ. अण्ग्रहणं किम्?\n"
        "  सुधातुरकङ् च (4.1.97) सौधातकिः — the substitute must be an aṆ, so\n"
        "  where a whole affix takes the place of ṛ no r is added.\n"
        "\n"
        "SETTLED — ḷ, by Kātyāyana rather than by Pāṇini. This was left open\n"
        "  here, on the ground that the l must come from a vārttika that\n"
        "  could not be cited. It can now: the vārttika collection has\n"
        "  लपर इति वक्तव्यम् on this very sūtra — 'it should be stated:\n"
        "  l-para'. So the ḷ-varṇa takes l exactly where the ṛ-varṇa takes\n"
        "  r, and guṇa of ḷ is अल्, vṛddhi आल्. The sūtra alone gives only\n"
        "  the vowel, since its उः is glossed by the Kāśikā as ṛ; the\n"
        "  vārttika supplies the rest, and raparatva(varttika=False) shows\n"
        "  the difference it makes.\n"
        "\n"
        "  Found by reading the vārttika collection, which was on disk and\n"
        "  unconsulted while this question stood open. Worth recording as a\n"
        "  lesson about the apparatus and not only about the sūtra."
    ),
)


register(
    "1.1.52",
    apply=replace_antya,
    codification=(
        "replace_antya(text, substitute) -> the form with its last sound "
        "replaced. Segmentation is chandas.core.scan_phonemes, so a substitute "
        "cannot land inside a digraph."
    ),
    related=("1.1.49", "1.1.54", "1.1.55", "1.2.50"),
    notes=(
        "SETTLED — the default landing site is the last sound, not the whole:\n"
        "  षष्ठीनिर्दिष्टस्य य उच्यत आदेशः, सोऽन्त्यस्यालः स्थाने वेदितव्यः. The\n"
        "  Kāśikā's example is 1.2.50 इद् गोण्याः, giving पञ्चगोणिः — the i\n"
        "  replaces only the final ī of गोणी, and without this rule the stem\n"
        "  would vanish.\n"
        "\n"
        "SETTLED — it is the default of four, and the other three are now\n"
        "  codified beside it: 1.1.53 for a ṅit substitute, 1.1.54 for a rule\n"
        "  stated in the fifth case, 1.1.55 for a substitute that is anekāl\n"
        "  or śit. `substitution_site` weighs the four in that order and\n"
        "  names the one that decided, so a caller never has to remember\n"
        "  which of them applies."
    ),
)


register(
    "1.1.53",
    apply=substitution_site,
    codification=(
        "The ṅit branch of substitution_site. Tested before 1.1.55, because "
        "rescuing anekāl substitutes from 1.1.55 is the only thing it does."
    ),
    related=("1.1.52", "1.1.55", "6.3.25"),
    notes=(
        "SETTLED — it exists to beat 1.1.55, and the Kāśikā states the conflict\n"
        "  in one line: ङिच्च य आदेशः, सोऽनेकालपि अलोऽन्त्यस्य स्थाने भवति — a\n"
        "  ṅit substitute takes the place of the last sound THOUGH IT BE more\n"
        "  than one sound. The अपि is the whole sūtra. Its example आनङ् at\n"
        "  6.3.25 आनङ् ऋतो द्वन्द्वे (होतापोतारौ, मातापितरौ) is both ṅit and\n"
        "  anekāl, so the order of the two tests is what the rule is.\n"
        "\n"
        "SETTLED — the converse case is worth keeping: तातङि ङित्करणस्य\n"
        "  गुणवृद्धिप्रतिषेधार्थत्वात् सर्वादेशस्तातङ् भवति. In तातङ् the ṅ is\n"
        "  there to block guṇa and vṛddhi by 1.1.5, not to invoke this rule, so\n"
        "  तातङ् does replace the whole. A ṅ can be present for more than one\n"
        "  reason, which is a caution against reading it-letters off a string."
    ),
)


register(
    "1.1.54",
    reuses=('1.1.53', '1.1.55'),
    apply=site_for,
    codification=(
        "The pañcamī branch. The trigger is read from the sūtra's own case "
        "marking through pancami_padas, so the rule is executable over the "
        "whole text rather than on a flag the caller sets."
    ),
    related=("1.1.49", "1.1.52", "6.3.97", "7.2.83"),
    notes=(
        "SETTLED — the trigger is the fifth case, and the Kāśikā says so in as\n"
        "  many words: परस्य कार्यं शिष्यमाणमादेरलः प्रत्येतव्यम् । क्व च परस्य\n"
        "  कार्यं शिष्यते? यत्र पञ्चमीनिर्देशः. The corpus records vibhakti for\n"
        "  every pada, so this is read rather than declared — and the two\n"
        "  examples check out: 7.2.83 ईदासः has आसः in the fifth (आसीनो यजते),\n"
        "  and 6.3.97 द्व्यन्तरुपसर्गेभ्योऽप ईत् has द्व्यन्तरुपसर्गेभ्यः in the\n"
        "  fifth (द्वीपम्, अन्तरीपम्, प्रतीपम्, समीपम्), while every example of\n"
        "  1.1.52, 1.1.53 and 1.1.55 stands in the sixth.\n"
        "\n"
        "SETTLED — this is the mirror of 1.1.49. A sixth case names what is\n"
        "  replaced and the operation falls at its end; a fifth case names what\n"
        "  precedes and the operation falls at the start of what follows. The\n"
        "  two paribhāṣās read the same padaccheda from opposite ends."
    ),
)


register(
    "1.1.55",
    apply=substitution_site,
    codification=(
        "The anekāl/śit branch. Length is counted with the prosody scanner, so "
        "a digraph counts once; the it-letters are carried on the Adesa rather "
        "than parsed off it."
    ),
    related=("1.1.52", "1.1.53", "2.4.52", "7.1.20"),
    notes=(
        "SETTLED — two triggers, one consequence. अनेकाल् य आदेशः शिच् च, स\n"
        "  सर्वस्य षष्ठीनिर्दिष्टस्य स्थाने भवति. The Kāśikā gives one example\n"
        "  of each: 2.4.52 अस्तेर्भूः, where भू is two sounds and replaces the\n"
        "  whole of अस् (भविता, भवितुम्), and 7.1.20 जश्शसोः शिः, where शि is\n"
        "  śit though short (कुण्डानि तिष्ठन्ति).\n"
        "\n"
        "SETTLED — अनेकाल् counts sounds, not characters. भू is bh plus ū, two\n"
        "  al and not three, so the count goes through the same scanner the\n"
        "  metre engine uses rather than through len().\n"
        "\n"
        "SETTLED — whether a substitute is śit can now be read off its written\n"
        "  form. That took the it-saṃjñā rules 1.3.2 to 1.3.9, which were the\n"
        "  SCOPE recorded here before they were codified. `Adesa.from_upadesa`\n"
        "  runs them. The contrast that shows they are really being applied is\n"
        "  1.3.8's अतद्धिते: क as a general affix loses its k and yields अ, the\n"
        "  same क as a taddhita keeps it. Neither has to be asserted by a caller.\n"
        "\n"
        "SCOPE — what remains is a question about the form and not the marks:\n"
        "  the it-rules leave the उच्चारणार्थ vowel that makes a consonant-final\n"
        "  anubandha pronounceable, so आनङ् yields आन rather than आन्. See\n"
        "  the note on 1.3.9."
    ),
)


# ---------------------------------------------------------------------------
# स्थानिवद्भाव — 1.1.56 to 1.1.59
#
# An exception, an exception to it, and an exception to that. Implemented in
# src/astadhyayi/sthanivat.py as one decision, taken in an order that is not
# the numbering: 1.1.59 first, because it re-admits what 1.1.58 excluded from
# what 1.1.57 allowed against what 1.1.56 forbade.
# ---------------------------------------------------------------------------

register(
    "1.1.56",
    samjna="sthānivat",
    apply=sthanivat,
    codification=(
        "The general branch of sthanivat(...): a substitute counts as the"
        " substituend wherever the operation does not rest on sounds."
    ),
    related=("1.1.49", "1.1.57", "2.4.52", "3.1.91"),
    notes=(
        "SETTLED — why an atideśa is needed at all, in the Kāśikā's words:\n"
        "  स्थान्यादेशयोः पृथक्त्वात् स्थान्याश्रयं कार्यमादेशे न प्राप्नोति.\n"
        "  The two are distinct things, so an operation conditioned on the\n"
        "  one would slip past the other. स्थानिना तुल्यं वर्तत इति स्थानिवत्.\n"
        "\n"
        "SETTLED — the exception is the whole difficulty: अनल्विधौ, glossed\n"
        "  न अल्विधिरनल्विधिः. Where the operation rests on a sound AS a\n"
        "  sound the likeness does not hold, and 1.1.57 exists to let it back\n"
        "  in under conditions — अल्विध्यर्थमिदमारभ्यते.\n"
        "\n"
        "SETTLED — the range is wide. धात्वङ्गकृत्तद्धिताव्ययसुप्तिङ्पदादेशाः:\n"
        "  a root-substitute counts as a root, an aṅga-substitute as an aṅga,\n"
        "  and so through seven categories. भू replacing अस् by 2.4.52 is\n"
        "  still a root for 3.1.91 धातोः, which is what gives भविता, भवितुम्,\n"
        "  भवितव्यम् — and that same substitution is 1.1.55's worked example,\n"
        "  so the two sūtras meet on it."
    ),
)

register(
    "1.1.57",
    apply=sthanivat,
    codification=(
        "The vowel branch, with its three conditions."
    ),
    related=("1.1.49", "1.1.56", "1.1.58", "1.1.66", "7.2.116"),
    notes=(
        "SETTLED — three words, three different readings of case, and the\n"
        "  Kāśikā gives each: अच इति स्थानिनिर्देशः — the genitive names the\n"
        "  substituend, which is 1.1.49; परस्मिन्निति निमित्तसप्तमी — a\n"
        "  locative of cause; पूर्वविधाविति विषयसप्तमी — a locative of scope.\n"
        "  Only the first is what 1.1.66 would have supplied for a seventh\n"
        "  case, and the other two show that the paribhāṣā about locatives is\n"
        "  not a blanket rule. Worth recording against `nirdesa`, which reads\n"
        "  every seventh case one way.\n"
        "\n"
        "SETTLED — all three conditions are required, and dropping any one\n"
        "  returns the case to 1.1.56's prohibition. पटयति: पटुम् आचष्टे with\n"
        "  ṇic, the ṭi elided, and the elision counting as present is what\n"
        "  keeps 7.2.116 अत उपधायाः from lengthening. अवधीत्: the a-lopa\n"
        "  counting as present blocks 7.2.7. बहुखट्वकः: the shortening of\n"
        "  7.4.15 counting as present blocks the rule that would look at the\n"
        "  last vowel but one."
    ),
)

register(
    "1.1.58",
    apply=sthanivat,
    codification=(
        "The list of ten operations 1.1.57 does not reach. The members co"
        "me from the corpus's own padaccheda of the dvandva."
    ),
    related=("1.1.57", "1.1.59"),
    notes=(
        "SETTLED — ten operations named in one long dvandva, and the corpus\n"
        "  splits it for us: पदान्त, द्विर्वचन, वरे, यलोप, स्वर, सवर्ण,\n"
        "  अनुस्वार, दीर्घ, जश्, चर्. कौ स्तः and तानि सन्ति for padānta;\n"
        "  दद्ध्यत्र and मद्ध्वत्र for dvirvacana; अप्सु यायावरः for वरे.\n"
        "\n"
        "SCOPE — four vārttikas stand on this sūtra and none is codified.\n"
        "  स्वरदीर्घयलोपेषु लोपाजादेशो न स्थानिवद् restates part of the list\n"
        "  for lopa specifically; क्विलुगुपधात्वचङ्परनिर्ह्रासकुत्वेषु-\n"
        "  उपसंख्यानम् adds six more operations to it; पूर्वत्रासिद्धे न\n"
        "  स्थानिवत् bars sthānivadbhāva in the tripādī; and तस्य दोषः\n"
        "  संयोगादिलोपलत्वणत्वेषु objects to that last. The third is the most\n"
        "  consequential — it ties this block to 8.2.1 — and none of the four\n"
        "  can be applied until operations are named as objects rather than\n"
        "  passed as strings."
    ),
)

register(
    "1.1.59",
    apply=sthanivat,
    codification=(
        "The reduplication branch, tested first because it is the innermo"
        "st exception."
    ),
    related=("1.1.56", "1.1.58", "6.1.1", "6.4.64", "6.4.98"),
    notes=(
        "SETTLED — an exception to an exception to an exception, and the\n"
        "  reason the four are read as one decision in an order that is not\n"
        "  their numbering. 1.1.58 has just excluded द्विर्वचन; this puts it\n"
        "  back, for the reduplication itself and no further —\n"
        "  द्विर्वचन एव कर्तव्ये.\n"
        "\n"
        "SETTLED — it is an atideśa of FORM and it expires:\n"
        "  रूपातिदेशश्चायं नियतकालः। तेन कृते द्विर्वचने पुनरादेशरूपमेव\n"
        "  अवतिष्ठते — once the reduplication is done the substitute's own\n"
        "  form stands again. `Sthanivat.provisional` carries that, and it is\n"
        "  true of this sūtra alone among the four.\n"
        "\n"
        "SETTLED — without it several reduplications would be impossible,\n"
        "  because the elision that precedes them leaves no vowel to\n"
        "  reduplicate. पपतुः and पपुः: 6.4.64 elides the ā, and only the\n"
        "  elided ā counting as present lets 6.1.1 reduplicate. जघ्नतुः and\n"
        "  जघ्नुः: after the upadhā-lopa of 6.4.98 the form is अनच्क, without\n"
        "  a vowel, and द्विर्वचनं न स्यात्, अस्माद् वचनाद् भवति. आटिटत्:\n"
        "  after the ṇi-lopa, 6.1.2 needs the vowel that is no longer there."
    ),
)

# ---------------------------------------------------------------------------
# Disappearance, parts, and how to read a case — 1.1.60 to 1.1.67
#
# Three small groups that happen to be adjacent. 1.1.60–1.1.63 are about an
# affix vanishing and what survives it (src/astadhyayi/lopa.py); 1.1.64–1.1.65
# name two stretches of a form so that rules can operate on them; 1.1.66–1.1.67
# complete the set of case-readings begun at 1.1.49, so that between them a
# rule's own vibhaktis say where its operation falls.
# ---------------------------------------------------------------------------


register(
    "1.1.60",
    samjna="lopa",
    apply=adarsana,
    codification=(
        "adarsana(present) -> bool. A fact about an absence, not a name for a "
        "string, because the sūtra names the state."
    ),
    related=("1.1.61", "1.1.62", "4.1.129"),
    notes=(
        "SETTLED — the saṃjñā is of the thing meant, not of a word:\n"
        "  अर्थस्येयं संज्ञा न शब्दस्य. The Kāśikā first piles up synonyms —\n"
        "  अदर्शनम्, अश्रवणम्, अनुच्चारणम्, अनुपलब्धिः, अभावः, वर्णविनाशः —\n"
        "  and then says the name belongs to what all of them mean.\n"
        "\n"
        "SETTLED — only of what would otherwise have been there:\n"
        "  प्रसक्तस्यादर्शनं लोपसंज्ञं भवति. An absence that was never in\n"
        "  question is not a lopa, which is why the codification takes a slot\n"
        "  that could have been filled rather than an arbitrary emptiness."
    ),
)


register(
    "1.1.61",
    apply=names_of_affix_elision,
    codification=(
        "The three members of Elision that name an affix's disappearance. Kept "
        "as distinct enum members rather than aliases, because the Kāśikā "
        "forbids blurring them."
    ),
    related=("1.1.60", "1.1.62", "1.1.63"),
    notes=(
        "SETTLED — the three names do not mix: अनेकसंज्ञाविधानाच् च\n"
        "  तद्भावितग्रहणमिह विज्ञायते ... तेन संज्ञानां संकरो न भवति. Each name\n"
        "  reaches only the elision that name itself prescribed — a luk is not\n"
        "  a ślu that happens to look alike. Hence three members and no\n"
        "  aliasing, which is what makes 1.1.63 statable at all.\n"
        "\n"
        "SETTLED — प्रत्ययग्रहणं किम्? अगस्तयः। कुण्डिनाः। The three names are\n"
        "  for an affix's disappearance and not for any other."
    ),
)


register(
    "1.1.62",
    apply=pratyaya_laksana,
    codification=(
        "pratyaya_laksana(elision, anga=...) -> Laksana. Returns whether the "
        "affix's conditioning survives and which of the two sūtras decided, "
        "since 1.1.62 and 1.1.63 are one question with two answers."
    ),
    related=("1.1.61", "1.1.63", "1.4.14"),
    notes=(
        "SETTLED — the motive, in the Kāśikā's own words: प्रत्ययनिमित्तं\n"
        "  कार्यमसत्यपि प्रत्यये कथं नु नाम स्यादिति सूत्रमिदमारभ्यते. Its\n"
        "  examples are अग्निचित्, सोमसुत्, अधोक् — the sup and tiṅ are gone and\n"
        "  the forms are still pada by 1.4.14, which is what lets 1.3.3 leave\n"
        "  their final consonants alone.\n"
        "\n"
        "SETTLED — प्रत्यय is said twice on purpose: प्रत्यय इति वर्तमाने\n"
        "  पुनः प्रत्ययग्रहणं किम्? कृत्स्नप्रत्ययलोपे यथा स्यात् — so that it\n"
        "  holds when the WHOLE affix has gone, and not when only part of\n"
        "  it has.\n"
        "\n"
        "SETTLED — a third restriction, from Kātyāyana: वर्णाश्रये नास्ति\n"
        "  प्रत्ययलक्षणम्, there is no pratyayalakṣaṇa where the operation\n"
        "  depends on a sound. What survives the elision is conditioning by\n"
        "  the AFFIX and not by the letters it was made of. The Kāśikā puts\n"
        "  the same point with its own examples: प्रत्ययलक्षणं यथा स्यात्\n"
        "  वर्णलक्षणं मा भूत् — गवे हितम् गोहितम्, रायः कुलम् रैकुलम्.\n"
        "\n"
        "SCOPE — that vārttika is NOT codified. It was found by reading the\n"
        "  vārttika collection, which sat on disk unused\n"
        "  until the apparatus was widened, and which the Kāśikā on this\n"
        "  sūtra does not mention. pratyaya_laksana knows the kind of\n"
        "  elision and whether the target is the aṅga, and has no way to\n"
        "  say that an operation is varṇa-based, so the restriction cannot\n"
        "  be applied. Recorded so the gap is visible rather than absent."
    ),
)


register(
    "1.1.63",
    apply=pratyaya_laksana,
    codification="The prohibition inside pratyaya_laksana: aṅga plus a lu-word.",
    related=("1.1.61", "1.1.62"),
    notes=(
        "SETTLED — लुमता means 'by a word containing lu', which is exactly luk,\n"
        "  ślu and lup and not a plain lopa. Pāṇini could have listed the three;\n"
        "  naming them by the syllable they share is shorter and is why LUMAT is\n"
        "  derived from the Elision members rather than written out again.\n"
        "\n"
        "SETTLED — both restrictions are load-bearing and the Kāśikā tests each.\n"
        "  लुमतेति किम्? कार्यते। हार्यते। — an ordinary lopa, so 1.1.62 stands.\n"
        "  अङ्गस्येति किम्? पञ्च। सप्त। पयः। साम। — not an operation on the\n"
        "  aṅga, so it stands too. Its own examples are गर्गाः, मृष्टः, जुहुतः,\n"
        "  where a yaÑ or śap has gone by luk or ślu and the aṅga therefore\n"
        "  takes neither guṇa nor vṛddhi — यञ्शपोर्लुमता लुप्तयोरङ्गस्य\n"
        "  गुणवृद्धी न भवतः."
    ),
)


register(
    "1.1.64",
    samjna="ṭi",
    apply=ti,
    codification=(
        "ti(text) -> the stretch from the last vowel to the end. The vowel is "
        "found with the prosody scanner, so a diphthong is one vowel."
    ),
    related=("1.1.65", "3.4.79"),
    notes=(
        "SETTLED — अचः is a genitive of selection, not of substitution:\n"
        "  अच इति निर्धारणे षष्ठी। जातावेकवचनम् — 'of the vowels, generically,\n"
        "  the last'. This is the one place so far where a ṣaṣṭhī in a sūtra is\n"
        "  NOT the sthānin of 1.1.49, and the Kāśikā says so explicitly rather\n"
        "  than leaving it to be inferred.\n"
        "\n"
        "SETTLED — the name covers the vowel and everything after it, not the\n"
        "  vowel alone: तदादि शब्दरूपम्. अग्निचित् gives इत् and not इ,\n"
        "  सोमसुत् gives उत्, आताम् and आथाम् give आम्."
    ),
)


register(
    "1.1.65",
    samjna="upadhā",
    apply=upadha,
    codification="upadha(text) -> the single sound before the last, or None.",
    related=("1.1.64", "7.2.116"),
    notes=(
        "SETTLED — one sound, not everything before the last: अल इति किम्?\n"
        "  शिष्टः। शिष्टवान्। समुदायात् पूर्वस्य मा भूत्. The अल् in the sūtra\n"
        "  is there for that, and the codification returns a single phoneme for\n"
        "  that reason.\n"
        "\n"
        "SETTLED — the Kāśikā's examples are all roots and all four vowel\n"
        "  qualities: पच्, पठ् give a; भिद्, छिद् give i; बुध्, युध् give u;\n"
        "  वृत्, वृध् give ṛ. They are the test data."
    ),
)


register(
    "1.1.66",
    apply=nirdesa,
    codification=(
        "The seventh-case branch of nirdesa(sutra_id), which reads all three "
        "case-paribhāṣās off the corpus at once."
    ),
    related=("1.1.49", "1.1.67", "6.1.77"),
    notes=(
        "SETTLED — a seventh case points backward: तस्मिन्निति सप्तम्यर्थनिर्देशे\n"
        "  पूर्वस्यैव कार्यं भवति, नोत्तरस्य. The example is 6.1.77 इको यणचि,\n"
        "  and it is the one that shows the three paribhāṣās working together:\n"
        "  इकः is sixth so it is what gets replaced, अचि is seventh so the\n"
        "  operation falls on what precedes the aC — दधि + उदकम् gives\n"
        "  दध्युदकम्, मधु + इदम् gives मध्विदम्. The corpus marks both cases, so\n"
        "  nirdesa() reads that whole analysis out of the sūtra unaided.\n"
        "\n"
        "SETTLED — निर्दिष्ट is in the sūtra for adjacency:\n"
        "  निर्दिष्टग्रहणमानन्तर्यार्थम्। अग्निचिदत्रेति व्यवहितस्य मा भूत् —\n"
        "  what precedes must precede immediately. Not represented in the\n"
        "  codification, which reports the side and not the distance; adjacency\n"
        "  belongs to whatever applies the rule to a string."
    ),
)


register(
    "1.1.67",
    apply=nirdesa,
    codification="The fifth-case branch of nirdesa(sutra_id).",
    related=("1.1.49", "1.1.54", "1.1.66", "8.1.28"),
    notes=(
        "SETTLED — a fifth case points forward: तस्मादिति पञ्चम्यर्थनिर्देश\n"
        "  उत्तरस्यैव कार्यं भवति, न पूर्वस्य. Its example is 8.1.28 तिङ्ङतिङः,\n"
        "  where अतिङः is fifth: in ओदनं पचति the accentless tiṅ is the one\n"
        "  AFTER the non-tiṅ, and in पचत्योदनम् it is not, so the rule does not\n"
        "  apply there.\n"
        "\n"
        "SETTLED — how this sits with 1.1.54 आदेः परस्य, which also concerns a\n"
        "  fifth case. They answer different questions and compose: this sūtra\n"
        "  says WHICH item the operation falls on, the following one; 1.1.54\n"
        "  says WHERE in that item, its first sound. Together with 1.1.49 and\n"
        "  1.1.52 the four make a complete address — which side, and how far in.\n"
        "\n"
        "SETTLED — निर्दिष्टे is read down from 1.1.66 by anuvṛtti, which the\n"
        "  corpus records, so the adjacency requirement carries over."
    ),
)


# ---------------------------------------------------------------------------
# The grahaṇa chain — 1.1.68 to 1.1.70
#
# What a sound named in a rule picks up. The three compose with 1.1.71 below,
# and the composition lives in src/astadhyayi/grahana.py so that any rule can
# ask the question without reimplementing it. Registered here against that one
# implementation.
# ---------------------------------------------------------------------------


register(
    "1.1.68",
    apply=grahana,
    codification=(
        "grahana(term) -> Grahana. This sūtra is the default the other three "
        "amend, so it is not a separate function: it is the base case, and it "
        "shows in the result's `by` field, which begins with 1.1.68 for every "
        "term that is not a saṃjñā."
    ),
    related=("1.1.69", "1.1.70", "1.1.71"),
    notes=(
        "SETTLED — why the sūtra is needed at all. शब्देनार्थावगतेरर्थे\n"
        "  कार्यस्यासंभवात् तद्वाचिनां शब्दानां संप्रत्ययो मा भूदिति सूत्रमिदम्\n"
        "  आरभ्यते: because a word conveys a meaning, and an operation cannot be\n"
        "  performed on a meaning, the rule is begun so that the things words\n"
        "  denote are not understood. अग्नेर्ढक् (4.2.33) is about the word\n"
        "  अग्नि, not about fire.\n"
        "\n"
        "SETTLED — the अशब्दसंज्ञा clause. A technical term denotes what it\n"
        "  names, not its own letters, or वृद्धि in 7.2.1 would mean the three\n"
        "  syllables. Which words are terms of art cannot be read off the\n"
        "  corpus — a saṃjñā-sūtra's padas hold the name and the named alike, and\n"
        "  1.1.1 offers वृद्धिः and आत्-ऐच् with nothing to tell them apart — so\n"
        "  register() takes the name per sūtra and grahana consults that list.\n"
        "  It covers exactly the saṃjñās codified so far, which is the honest\n"
        "  extent of what this project can claim to know."
    ),
)


register(
    "1.1.69",
    reuses=('1.1.9', '1.1.71'),
    apply=grahana,
    codification=(
        "The widening step inside grahana(): an aṆ or an udit term also "
        "denotes its savarṇas, through varna.savarnas_of, and the varieties "
        "that savarṇatva disregards. `pratyaya=True` suppresses it."
    ),
    related=("1.1.9", "1.1.68", "1.1.70", "1.3.7", "6.1.101"),
    notes=(
        "SETTLED — which aṆ. परेण णकारेण प्रत्याहारग्रहणम्: the pratyāhāra is\n"
        "  formed with the LATER ṇ, so aṆ is the fourteen — every vowel together\n"
        "  with h y v r l — and not the three of śivasūtra 1. The semivowels\n"
        "  are in it for a reason: y, v and l have anunāsika counterparts to\n"
        "  sweep up, and r, which has none, is the one the Kāśikā excludes when\n"
        "  it counts sub-varieties (रेफवर्जिता यवलाः).\n"
        "\n"
        "SETTLED — what savarṇa-grahaṇa reaches: स्वरानुनासिक्यकालभिन्नस्य\n"
        "  ग्रहणं भवति — forms differing in accent, nasality or duration.\n"
        "  Duration is covered because the savarṇa relation joins a with ā;\n"
        "  nasality by `varieties`.\n"
        "\n"
        "SCOPE — accent is modelled but is not folded in here, and the\n"
        "  reason is about the texts and not the rule. 1.2.29 to 1.2.32 are\n"
        "  codified and src/astadhyayi/svara.py carries the three accents,\n"
        "  so the earlier note that accent was modelled nowhere no longer\n"
        "  holds. But grahaṇa operates on terms as the sūtrapāṭha writes\n"
        "  them, and the sūtrapāṭha on disk is unaccented — the dhātupāṭha\n"
        "  is the text that marks accent, with 667 anudātta roots and 106\n"
        "  svarita. Widening every term to three accented forms would\n"
        "  therefore produce forms that occur nowhere in the data being\n"
        "  read. Left out for that reason, and not because the dimension is\n"
        "  unrepresentable."
        "\n"
        "SETTLED — the set is closed under savarṇatva. The śivasūtras enumerate\n"
        "  only the hrasva vowels, so read literally aṆ would exclude ā and a\n"
        "  rule writing ā would denote ā alone. 1.1.1 settles it: if a bare ā did\n"
        "  not already reach short a, the t of आत् would have nothing to exclude.\n"
        "\n"
        "SETTLED — अप्रत्ययः. An affix denotes its own form only; otherwise the\n"
        "  affix a would take in ā wherever it occurred."
    ),
)


register(
    "1.1.70",
    reuses=('1.2.27',),
    apply=grahana,
    codification=(
        "The narrowing step inside grahana(): a tapara term denotes only the "
        "savarṇas of its own duration. Duration comes from the prosody "
        "engine's vowel tables through grahana.kala, not a second list."
    ),
    related=("1.1.1", "1.1.68", "1.1.69", "6.4.41", "7.1.9"),
    notes=(
        "SETTLED — it replaces 1.1.69, it does not refine it. अणिति नानुवर्तते:\n"
        "  aṆ does not carry over. अणामन्येषां च तपराणाम् इदमेव ग्रहणकशास्त्रम् —\n"
        "  for tapara sounds, aṆ or not, THIS is the rule of denotation, and\n"
        "  पूर्वग्रहणकशास्त्रं न प्रवर्तत एव, the earlier one does not operate at\n"
        "  all. The code reflects this by testing for tapara before 1.1.69 and\n"
        "  returning, rather than by intersecting two results.\n"
        "\n"
        "SETTLED — what it buys, in the Kāśikā's own words: तत्कालस्येति किम्?\n"
        "  खट्वाभिः। मालाभिः॥ 7.1.9 अतो भिस ऐस् replaces bhis with ais after अत्.\n"
        "  The t is what keeps ā out, so वृक्ष + भिस् gives वृक्षैः while\n"
        "  खट्वा + भिस् stays खट्वाभिः. Without the tapara the second would\n"
        "  wrongly become खट्वैः.\n"
        "\n"
        "SETTLED — other qualities stay free: तुल्यकालस्य गुणान्तरयुक्तस्य\n"
        "  सवर्णस्य ग्राहको भवति. Duration is fixed; nasality and accent are not.\n"
        "  So अत् reaches the nasalised short a and not ā.\n"
        "\n"
        "OPEN — which of the two readings a bare string wants. तः परो यस्मात्\n"
        "  सोऽयं तपरः, तादपि परस्तपरः gives both अत् and ता, and nothing in the\n"
        "  string says which is meant; only the sūtra it stands in does. The\n"
        "  trailing form is taken first because it is far the commoner in the\n"
        "  sūtrapāṭha. A term supplied with its context would settle it, and that\n"
        "  is worth doing when rules are read from the corpus rather than named\n"
        "  by hand."
    ),
)


# ---------------------------------------------------------------------------
# 1.1.71  आदिरन्त्येन सहेता  ādir antyena sahetā — how a pratyāhāra is formed
# ---------------------------------------------------------------------------
#
# Already implemented, in full, in src/astadhyayi/sivasutra.py — it had to be,
# because 1.1.1 could not be stated without it. Registering it here binds the
# sūtra to that implementation rather than writing a second one.


def form_pratyahara(name: str) -> Pratyahara:
    """
    1.1.71: an initial sound, taken together with a final it-marker, denotes
    itself and everything between.

    Delegates to the śivasūtra engine, which resolves the name against the
    fourteen aphorisms and records which sūtra supplied each end. Where the
    it-marker occurs twice (only Ṇ does), `resolve_all` returns every reading
    rather than choosing one silently.
    """
    return resolve(name)


register(
    "1.1.71",
    apply=form_pratyahara,
    codification=(
        "form_pratyahara(name) -> Pratyahara, delegating to sivasutra.resolve. "
        "The same call underlies 1.1.1 and 1.1.2, so this sūtra is not "
        "reimplemented — it is the machinery those two already run on."
    ),
    related=("1.1.1", "1.1.2", "1.1.3", "1.1.69", "1.1.70"),
    notes=(
        "The anuvṛtti recorded in the corpus is स्वम् and रूपम् from 1.1.68\n"
        "  (svaṃ rūpaṃ śabdasya): a sound named in a rule denotes its own form.\n"
        "  1.1.71 is the exception that lets ādaiC and adeṄ be read as classes\n"
        "  rather than as the literal syllables they spell.\n"
        "\n"
        "IMPLEMENTATION — this sūtra was necessarily codified first, since\n"
        "  1.1.1 cannot be stated without it. sivasutra.py carries the fourteen\n"
        "  śivasūtras and the resolution; its tests check every standard\n"
        "  pratyāhāra against its traditional membership and count. Registering\n"
        "  the sūtra against that implementation keeps one source of truth."
    ),
)


# ---------------------------------------------------------------------------
# The close of the pāda — 1.1.72 to 1.1.75
#
# 1.1.72 belongs with the grahaṇa chain and is implemented in grahana.py beside
# it; 1.1.73 to 1.1.75 name वृद्ध and live in samjna.py. The pāda ends here: it
# has 75 sūtras, not 71, which an early version of the tests got wrong and
# which nearly cost the tadantavidhi.
# ---------------------------------------------------------------------------

register(
    "1.1.72",
    reuses=('1.1.68', '1.1.69', '1.1.70'),
    apply=tadantavidhi,
    codification=(
        "tadantavidhi(term, word) -> bool. What the term denotes comes fr"
        "om grahana(), so the extension composes with 1.1.68 to 1.1.71."
    ),
    related=("1.1.68", "1.1.69", "2.1.24", "3.1.125", "3.3.56", "4.1.99"),
    notes=(
        "SETTLED — it belongs beside 1.1.68 and not on its own: स्वम् and\n"
        "  रूपम् are read down into it, which the corpus records. 1.1.68 says\n"
        "  a word denotes its own form; this says it denotes whatever ENDS in\n"
        "  that form as well — येन विशेषणेन विधिर्विधीयते स तदन्तस्य\n"
        "  आत्मान्तस्य समुदायस्य ग्राहको भवति, स्वस्य च रूपस्य. 3.3.56 एरच्\n"
        "  reaches चि and जि, giving चयः and जयः; 3.1.125 ओरावश्यके reaches a\n"
        "  u-final and gives अवश्यलाव्यम्.\n"
        "\n"
        "SETTLED — what is reached is what the term DENOTES and not the\n"
        "  letters it is written with, so this had to be composed with the\n"
        "  grahaṇa chain rather than compare strings. The उ of 3.1.125 is not\n"
        "  tapara, 1.1.69 therefore gives it ū as well, and लू is reached —\n"
        "  a literal comparison misses it. A tapara उत् would reach लु alone,\n"
        "  and does.\n"
        "\n"
        "SCOPE — seven vārttikas stand on this sūtra and one is codified. The\n"
        "  one taken is समासप्रत्ययविधौ प्रतिषेधः, which stops the extension\n"
        "  in a rule about compounds or affixes: without it 2.1.24 would\n"
        "  compound कष्टं परमश्रितः as well as कष्टश्रितः, and 4.1.99 would\n"
        "  make सौत्रनाडिः from सूत्रनडस्य as well as नाडायनः from नडस्य. The\n"
        "  other six — यस्मिन् विधिस्तदादावल्ग्रहणे, उगिद्वर्णग्रहणवर्जम्,\n"
        "  सुसर्वार्धदिक्छब्देभ्यो जनपदस्य, ऋतोर्वृद्धिमद्विधाववयवानाम्,\n"
        "  पदाङ्गाधिकारे तस्य च तदुत्तरपदस्य च, and one more — each qualify\n"
        "  the extension further and need machinery that does not exist yet."
    ),
)

register(
    "1.1.73",
    samjna="vṛddha",
    apply=vrddha,
    reuses=("1.1.71",),
    codification=(
        "The 1.1.73 branch of vrddha(word, ...), which reports which of t"
        "he three gave the name and whether optionally."
    ),
    related=("1.1.1", "1.1.74", "1.1.75", "4.2.114"),
    notes=(
        "SETTLED — the test is on the first VOWEL and not the first sound, and\n"
        "  the Kāśikā underlines it: अचामिति जातौ बहुवचनम्, the plural is\n"
        "  generic. शालीयः, मालीयः, औपगवीयः, कापटवीयः. आदिरिति किम्?\n"
        "  साभासन्नयनः — a vṛddhi that is not first does not count.\n"
        "\n"
        "SETTLED — whether the first vowel IS a vṛddhi is 1.1.1's question,\n"
        "  and is asked of it: `is_vrddhi` is called rather than a list of\n"
        "  ā, ai, au being written here. So the first sūtra of the pāda and\n"
        "  the seventy-third are joined.\n"
        "\n"
        "SETTLED — a vārttika makes the name optional for a proper name:\n"
        "  वा नामधेयस्य वृद्धसंज्ञा वक्तव्या, giving both देवदत्तीयाः and\n"
        "  दैवदत्ताः. Codified, as the `is_name` parameter."
    ),
)

register(
    "1.1.74",
    apply=vrddha,
    codification=(
        "The 1.1.74 branch of vrddha(word, ...), which reports which of t"
        "he three gave the name and whether optionally."
    ),
    related=("1.1.27", "1.1.73"),
    notes=(
        "SETTLED — the list is not a new one. त्यदादि is the TAIL of the\n"
        "  sarvādi gaṇa, from त्यद् to the end: त्यद्, तद्, यद्, एतद्, इदम्,\n"
        "  अदस्, एक, द्वि, युष्मद्, अस्मद्, भवतु, किम्. So it comes from the\n"
        "  Gaṇapāṭha by taking a slice, and the Kāśikā's examples walk that\n"
        "  tail — त्यदीयम्, तदीयम्, एतदीयम्, इदमीयम्, अदसीयम्, त्वदीयम्,\n"
        "  मदीयम्, भवदीयम्, किमीयम्.\n"
        "\n"
        "SETTLED — the anuvṛtti jumps this sūtra and resumes at the next, and\n"
        "  the Kāśikā says so at both ends: यस्याचामादिग्रहणम् उत्तरार्थम्\n"
        "  अनुवर्तते, इह तु न संबध्यते here, and यस्याचामादिग्रहणम् अनुवर्तते\n"
        "  at 1.1.75. So तद् and किम् are vṛddha although neither begins with\n"
        "  a vṛddhi. An anuvṛtti that skips a sūtra is rare enough to be worth\n"
        "  seeing once, and the codification has to leave the first-vowel test\n"
        "  out of this branch for it."
    ),
)

register(
    "1.1.75",
    apply=vrddha,
    codification=(
        "The 1.1.75 branch of vrddha(word, ...), which reports which of t"
        "he three gave the name and whether optionally."
    ),
    related=("1.1.71", "1.1.73", "4.2.117"),
    notes=(
        "SETTLED — the first-vowel condition resumes here, and the class is a\n"
        "  pratyāhāra resolved through 1.1.71 rather than written out:\n"
        "  एङ् is e and o. एणीपचनीयः, भोजकटीयः, गोनर्दीयः.\n"
        "\n"
        "SETTLED — all three conditions are tested by the Kāśikā, and the\n"
        "  first of them needed the Nyāsa to read correctly. एङिति किम्?\n"
        "  आहिच्छत्रः, कान्यकुब्जः — those are the DERIVATIVES, and the Nyāsa\n"
        "  gives the bases: अहिच्छत्रकान्यकुब्जशब्दाभ्याम् अण् एव भवति. The\n"
        "  words tested are अहिच्छत्र and कन्यकुब्ज, whose first vowel is a,\n"
        "  neither a vṛddhi nor an eṄ — so neither this sūtra nor 1.1.73\n"
        "  reaches them and they take aṆ. Feeding the derivative to the\n"
        "  codification instead of the base makes it answer 1.1.73, which is\n"
        "  what happened on the first pass.\n"
        "  प्राचामिति किम्? देवदत्तो नाम वाहीकेषु ग्रामः. देश इति किम्?\n"
        "  गौमताः.\n"
        "\n"
        "SCOPE — a vārttika शैषिकेष्विति वक्तव्यम् restricts the rule to the\n"
        "  śaiṣika affixes. Not codified; the affix is not among the\n"
        "  conditions this function takes."
    ),
)

__all__ = [
    "GUNA",
    "Samyoga",
    "IK",
    "IK_ALL",
    "VRDDHI",
    "form_pratyahara",
    "guna_vrddhi_target",
    "is_guna",
    "is_ik",
    "is_vrddhi",
    "antaratama",
    "blocked_by_na_ajjhalau",
    "adarsana",
    "agama_site",
    "avyaya",
    "grahana",
    "hrasva_of_ec",
    "guna_vrddhi_blocked",
    "names_of_affix_elision",
    "nirdesa",
    "positions",
    "pragrhya",
    "pratyaya_laksana",
    "is_anunasika",
    "is_gha",
    "is_ghu",
    "is_nistha",
    "is_samkhya",
    "is_sarvanaman",
    "is_sat",
    "membership_test",
    "raparatva",
    "replace_antya",
    "samyogas",
    "samprasarana",
    "sarvanaman",
    "sarvanamasthana",
    "sthanivat",
    "tadantavidhi",
    "savarna",
    "sthanin_padas",
    "sound_class",
]
