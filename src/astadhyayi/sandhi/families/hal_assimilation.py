# -*- coding: utf-8 -*-
"""
Consonant assimilation — the rules of 6.1.71–76, 8.2.24–41 and 8.4.40–68 that
act where two sounds meet.

**What this module is.** The tripādī's consonant rules, each as a step that
names its sūtra: the palatal turned guttural (8.2.30), the aspirate ह् turned
ढ्, घ्, ध् or थ् by root (8.2.31–35), the ष् of eight roots (8.2.36), the भष्
of दुह् and its kind (8.2.37–38), the voicing at a pada's end (8.2.39), the
ध् of लब्ध (8.2.40), the क् of लेक्ष्यति (8.2.41); the two classes of
*sannipāta* — श्चुत्व and ष्टुत्व (8.4.40–44); the unvoicing before a खर्
(8.4.55, 8.4.56); the assimilations of त-वर्ग before ल् (8.4.60), of स् after
उद् (8.4.61), of ह् after a झय् (8.4.62), of श् into छ् (8.4.63), and the
optional loss of a doubled झर् (8.4.65); the loss of a cluster's first sound
and of the aorist's स् (8.2.24–29); and, standing before the tripādī, the
augment तुक् that makes शिवच्छाया (6.1.71–76).

**Ordering is the grammar here.** Every rule of 8.2–8.4 is asiddha to those
before it (8.2.1), and that is what makes **वाक्पतिः** come out (च् → क् by
8.2.30, → ग् by 8.2.39, → क् by 8.4.55: three rules, each seeing what the last
made and none seeing what a *later* one makes) and **सच्चित्** come out (8.2.39
makes the त् a द् first; the श्चुत्व of 8.4.40 then makes it ज्; 8.4.55 hardens
it to च्; and 8.2.30 does *not* turn that च् to क् — it cannot see 8.4.40's
work). The engine keeps each sound's past (`Seg.prior`) and hands each rule a
`View` of the row as *that rule* may see it; nothing here decides visibility.

**Where a sound is chosen, it is chosen by 1.1.50 स्थानेऽन्तरतमः** — the nearest in
place, then in *internal* effort, then in external quality — and never read
from a table (`_nearest`). The Kāśikā's own tie-breaks fall out: स् goes to श्
(not छ्), a ध् before a खर् goes to त् (not स्).

**Options fork the engine** (8.4.56, 8.4.62, 8.4.63, 8.4.65, 8.2.33, 6.1.76): the
course that takes the option and the course that declines it are both
returned, each with its own trace.

**Refusals** (8.4.42, 8.4.43, 8.4.44) are applications with no edit at the very
site of the rule they refuse, winning it by `overrides`. Both the refused rule
and its refusals skip a cause they see only through its past — the rule had its
chance at that place before a later rule changed the sound, and a refusal is not
made twice.

**What the letters cannot say is read from the words' flags** (NORTH_STAR §5),
never guessed. The flags this family reads, beyond the engine's own
(`nipata`, `upasarga`, `ang`, `dhatu:ROOT`):

  * `dhatu:ROOT` — the root, as the dhātupāṭha gives it, in IAST (8.2.29,
    8.2.32–38, 6.1.71). It marks a word as a root-based form not yet finished,
    which is what licenses a rule to reach a sound inside it;
  * `krt`, `pit` — an affix that is a kṛt / carries a पित् marker (6.1.71);
  * `mang` — the prohibitive particle माङ् (6.1.74); `ang` is the engine's आङ्;
  * `sic` — the aorist's सिच्, on the piece स् (8.2.24–28); `pratyaya` — an
    affix (8.2.25); `it_agama`, `iit_agama` — the augments इट्, ईट् (8.2.28).

The rules whose scope is accent (8.4.66, 8.4.67) or a change no letter records
(8.4.68) are marked `scope` in COVERAGE, with the reason.

**One sūtra, one home.** 8.2.29 is in this family's scope and `ac_yan_ayadi` has
it too (for the cluster a yaṇ makes); `rulebook.problems()` refuses two
families defining one sūtra, so where that module has the rule this one stands
aside and says so in COVERAGE (`_elsewhere`). 6.1.86 is asked through
`Rule.operation` where the core has it (`_TUK`): for a तुक् the single
substitute of an एकादेश is asiddha, which is how अधीत्य gets its तुक्.
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
from functools import lru_cache
from typing import Dict, FrozenSet, Iterator, List, Optional, Sequence, Tuple

from src.astadhyayi import adesa as _adesa
from src.astadhyayi import corpus
from src.astadhyayi.anga import jhasas_tathoh_dhah
from src.astadhyayi.samyoganta import DRUH_FOUR, VRASCADI_EIGHT
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi.parse import to_iast, tokenize
from src.astadhyayi.sandhi.rule import (
    ADESA, AGAMA_KIND, LOPA, PRATISEDHA, SUTRA, VARTTIKA, Application, Detail,
    Edit, NewSeg, Via, delete, replace, rule, site, sk)
from src.astadhyayi.sandhi.segs import (
    AGAMA, ANGA, ANUNASIKA, WITHIN, Sight, View)
from src.astadhyayi.sandhi.trace import deva, sutra_text
from src.astadhyayi.svara import is_dirgha, is_hrasva
from src.normalizer import devanagari_to_iast
from src.astadhyayi.varna import USMAN, VARGA, effort, is_anunasika, savarnas_of, varna


# ---------------------------------------------------------------------------
# What the module leans on, and how it says so
# ---------------------------------------------------------------------------


def _named(sutra_id: str) -> str:
    """A rule's name is the sūtra's own words, read from the corpus (the Vidyut
    edition) and printed in Devanāgarī — never typed."""
    return deva(sutra_text(sutra_id))


def _varttika(sutra_id: str, marker: str) -> str:
    """A vārttika's own words, taken from `corpus.varttikas_on` — the one whose
    text contains `marker`. A marker that finds nothing fails at import."""
    for found in corpus.varttikas_on(sutra_id):
        if marker in found.text:
            return found.text
    raise LookupError(f"no vārttika on {sutra_id} contains {marker!r}")


#: Every sentence of the tradition this module quotes, as (source, sūtra, text).
#: `tests/test_sandhi_hal_assimilation.py` checks each against the commentary on
#: disk, so a quotation that is not the commentary's own fails.
QUOTED: List[Tuple[str, str, str]] = []

_SOURCES = {
    "kashika": "Kāśikā", "kaumudi": "Kaumudī", "bhashya": "Bhāṣya",
    "nyaas": "Nyāsa", "padamanjari": "Padamañjarī",
    "tattvabodhini": "Tattvabodhinī", "balamanorama": "Bālamanoramā",
}


def _said(source: str, sutra_id: str, text: str) -> str:
    """The tradition's own words, recorded for checking, and where they are
    from — the shape a reason in `overrides` and a note must have. The words are
    printed as the commentary has them (देवनागरी) and, for the reader who
    cannot read them, in roman beside them."""
    QUOTED.append((source, sutra_id, text))
    return (f"{text} ({devanagari_to_iast(text)}; "
            f"{_SOURCES[source]} on {sutra_id})")


#: The options this family has, each named by the word the sūtra (or the
#: anuvṛtti the Kāśikā names) supplies.
VA = "वा"
ANYATARASYAM = "अन्यतरस्याम्"

#: The mark the loss of a सिच् leaves, so that a rule of the ekādeśa family
#: which the vārttika सिज्लोप एकादेशे सिद्धो वाच्यः lets see that loss may name
#: it in `consumes`.
SIC_LOPA = "sic-lopa"


#: 6.1.86 षत्वतुकोरसिद्धः: for a तुक् the single substitute of an एकादेश is
#: asiddha, so a rule that says it is a तुक् is shown the sounds that substitute
#: replaced (`Rule.operation`, and `asiddha.ekadesa_visible` asked by the View).
#: A core that has not that field simply does not have the hiding.
_TUK = ({"operation": "tuk"}
        if "operation" in inspect.signature(rule).parameters else {})


def _elsewhere(sutra_id: str) -> str:
    """
    The other family module that already defines a rule for this sūtra (the
    sūtra itself, not a vārttika on it), or ''.

    A sūtra has one home: `rulebook.problems()` refuses two families defining
    it. 8.2.29 stands in this family's scope and in `ac_yan_ayadi`'s, which
    needs it for the cluster a yaṇ makes; where that module has it, this one
    stands aside — its COVERAGE says so — and where it has not, this one has it.
    """
    from src.astadhyayi.sandhi import families
    here = __name__.rsplit(".", 1)[-1]
    for info in pkgutil.iter_modules(families.__path__):
        if info.name == here or info.name.startswith("_"):
            continue
        module = importlib.import_module(f"{families.__name__}.{info.name}")
        if any(r.sutra == sutra_id and not r.varttika
               for r in getattr(module, "RULES", ())):
            return info.name
    return ""


@lru_cache(maxsize=None)
def _cls(varga: str) -> Tuple[str, FrozenSet[str]]:
    """
    The classes स्तु, श्चु, ष्टु: the sibilant that stands in a varga's own
    sthāna, together with the varga.

    Not typed. The Śikṣā (`varna.SIKSA_STHANA`) puts इचुयशानां in the palate,
    ऋटुरषाणां in the head, ऌतुलसानां in the teeth, and the ūṣman of each place
    is the sibilant the sūtras join to the varga: श् with चु, ष् with टु, स् with तु.
    """
    place = varna(VARGA[varga][0]).sthana
    sibilant = next(s for s in sorted(USMAN) if varna(s).sthana is place)
    return sibilant, frozenset(VARGA[varga]) | {sibilant}


@lru_cache(maxsize=None)
def _nearest_cached(sthanin: str, candidates: Tuple[str, ...]
                    ) -> Optional[str]:
    scored = [(c, _adesa.nearness(sthanin, c)) for c in candidates]
    scored = [(c, n) for c, n in scored if n is not None]
    if not scored:
        return None
    best = max((n.sthana_shared, -n.sthana_apart) for _, n in scored)
    at_place = [c for c, n in scored
                if (n.sthana_shared, -n.sthana_apart) == best]
    inner = [c for c in at_place if effort(c) is effort(sthanin)]
    return S.nearest(sthanin, inner or at_place)


def _nearest(sthanin: str, candidates) -> Optional[str]:
    """
    1.1.50 स्थानेऽन्तरतमः as the Kāśikā reckons it: nearest by PLACE first; of
    those, the one of the same INTERNAL effort (spṛṣṭa, īṣatspṛṣṭa …); and only
    then by external quality. `supports.nearest` breaks a tie by internal effort
    but ranks external quality above it, which sends a ध् before a खर् to स् (it
    shares महाप्राण) instead of त् (which shares its स्पृष्ट effort). The Kāśikā's
    order is the other one, and is what the tradition's forms require:
    युयुत्सते, not *युयुस्सते.
    """
    return _nearest_cached(sthanin, tuple(sorted(candidates)))


def _sa() -> str:
    """The dental sibilant, स् — the one that stands in the sthāna of त-वर्ग."""
    return _cls("tu")[0]


def _sha() -> str:
    """The retroflex sibilant, ष् — the one that stands with ट-वर्ग."""
    return _cls("ṭu")[0]


def _sha_palatal() -> str:
    """The palatal sibilant, श् — the one that stands with च-वर्ग."""
    return _cls("cu")[0]


def _root(v: View, sight: Sight) -> Optional[str]:
    """The root the caller names for this sound's word (`dhatu:ROOT`), IAST —
    or None if there is none, or it is not written in sounds this engine reads
    (a root nobody can read is a root no rule can name)."""
    named = v.word(sight).flag_value("dhatu")
    if not named:
        return None
    try:
        root = to_iast(named)
        tokenize(root)
    except Exception:
        return None
    return root


def _sounds(text: str) -> List[str]:
    return [sound for sound, _ in tokenize(text)]


def _root_first(v: View, last: Sight, root: str) -> Optional[Sight]:
    """The first sound of the root that ends at `last`: as many sounds back as
    the root has (its sounds may have changed, but not their number), so a
    root-word carrying a prefix is not mistaken for its first sound."""
    sights = v.word_sights(last.w)
    count = len(_sounds(root))
    return sights[-count] if len(sights) >= count else None

def _change(sights: Sequence[Sight], target: Sight, sub: str, *, nimitta: str,
            because: str, via: Sequence[Via], optional: str = "",
            note: str = "", nasal: bool = False, authority: str = SUTRA,
            varttika: str = "") -> Application:
    """One sound replaced by another — the shape of nearly every step here."""
    new = NewSeg(sub, frozenset({ANUNASIKA}) if nasal else frozenset())
    return Application(
        site=site(*sights), edits=(replace(target, new),),
        detail=Detail(kind=ADESA, sthanin=target.s, adesa=sub,
                      nimitta=nimitta, because=because, via=tuple(via),
                      note=note, authority=authority, varttika=varttika),
        optional=optional)


def _lost(sights: Sequence[Sight], target: Sight, *, nimitta: str,
          because: str, via: Sequence[Via] = (), note: str = "",
          marks: Sequence[str] = (), optional: str = "") -> Application:
    return Application(
        site=site(*sights), edits=(delete(target, *marks),),
        detail=Detail(kind=LOPA, sthanin=target.s, adesa="", nimitta=nimitta,
                      because=because, via=tuple(via), note=note),
        optional=optional)


def _refuse(sights: Sequence[Sight], *, sthanin: str, nimitta: str,
            because: str, via: Sequence[Via] = ()) -> Application:
    """A rule that refuses another: no edit, the very site of the refused."""
    return Application(
        site=site(*sights), edits=(),
        detail=Detail(kind=PRATISEDHA, sthanin=sthanin, adesa="",
                      nimitta=nimitta, because=because, via=tuple(via)))


def _merged(left: Sight, right: Sight, sound: str) -> Edit:
    """
    Two sounds become one sound that belongs to the LATER sound's word and
    remembers the earlier one's (as an एकादेश does, 6.1.84–85) — but is not
    marked as an एकादेश, for it is not one: it is a loss, and 6.1.86 (which is
    about the substitutes of 6.1.84) has nothing to say of it.
    """
    def first(sight: Sight) -> int:
        return sight.seg.lw if sight.seg.lw is not None else sight.w
    return Edit(left.real, right.real + 1,
                (NewSeg(sound, frozenset(), right.w, min(first(left),
                                                          first(right))),),
                hidden=left.through or right.through)


def _right_of(v: View) -> Dict[int, Sight]:
    """For each sound, the sound at a junction (or made in this derivation)
    standing immediately after it — `View.pairs`, never the interior of a
    finished word."""
    return {j.left.uid: j.right for j in v.pairs()}


def _left_of(v: View) -> Dict[int, Sight]:
    return {j.right.uid: j.left for j in v.pairs()}


# ---------------------------------------------------------------------------
# 6.1.71–6.1.76 — the augment तुक्, before छ् and before a पित् कृत्
# ---------------------------------------------------------------------------


def _tuk(vowel: Sight, following: Sight, *, why: str, because: str,
         via: Sequence[Via], optional: str = "") -> Application:
    """
    `t` put in after a vowel — an āgama, which 1.1.46 sets at the END of the
    sthānin because तुक् has a क् as its इत्.

    It is put in BEFORE the sound that follows and given the vowel's word: the
    two come to the same place. The vowel may be one this rule sees only through
    the एकादेश that made it (6.1.86: for a तुक् that substitute is asiddha —
    अधीत्य), and a rule may not edit what it sees only through its past; the
    sound that follows is really there. The inserted त् has no predecessor
    (`Seg.prior` is empty), so a rule that stands before the insertion cannot
    see it, and every later one can.
    """
    tuk = Edit(following.real, following.real,
               (NewSeg("t", frozenset({AGAMA}), vowel.w),),
               hidden=following.through)
    v1 = via + (Via("1.1.46", "{tuk} has {k} as its {it}, so it stands at the "
                              "END of what it augments, right after "
                              f"{sk(vowel.s)}"),)
    return Application(
        site=site(vowel, following), edits=(tuk,),
        detail=Detail(kind=AGAMA_KIND, sthanin=vowel.s, adesa="t",
                      nimitta=why, because=because, via=v1),
        optional=optional)


#: 6.1.72 संहितायाम् is an adhikāra — nothing to run, so COVERAGE calls it
#: `support` — and each of the rules it governs cites it here, with 1.4.109
#: which says what संहिता is.
_SAMHITA = (Via("6.1.72", "{saṃhitāyām} governs this whole stretch: the two "
                          "sounds must be spoken in one unbroken flow"),
            S.samhita_condition())


@rule("6.1.71", name=_named("6.1.71"), families=("agama",), **_TUK)
def hrasvasya_piti_krti_tuk(v: View):
    """
    पिति कृति परतो ह्रस्वान्तस्य धातोः तुगागमो भवति — प्रकृत्य, प्रहृत्य,
    उपस्तुत्य (with ल्यप्). Not आलूय, ग्रामणीः (the vowel is long), कृतम्, हृतम् (the
    affix is not पित्), पटुतरः (it is not a कृत्).

    A short vowel ending a word flagged as a root (`dhatu`), before a word that
    is a पित् कृत् (`pit` and `krt`). The letters cannot say whether an affix is
    पित् or कृत्, so the caller does.

    PARTIAL: the Kāśikā's first two examples, अग्निचित् and सोमसुत्, have क्विप्,
    whose sounds are all gone (6.1.67) — there is no junction between the root
    and an affix that has no letters, so such a word is given already finished.
    """
    right_of = _right_of(v)
    for s in v.live:
        word = v.word(s)
        if not (s.is_vowel and is_hrasva(s.s) and v.ends_word(s)
                and (word.has("dhatu") or word.flag_value("dhatu"))):
            continue
        nxt = right_of.get(s.uid)
        if nxt is not None and v.begins_word(nxt) and \
                v.word(nxt).has("pit") and v.word(nxt).has("krt"):
            yield _tuk(
                s, nxt, why=f"a {{pit}} {{kṛt}} ({sk(nxt.s)}…) follows",
                because=(f"{sk(s.s)} is a short vowel ending a root, and the "
                         f"affix that follows is a {{pit}} {{kṛt}}, so it "
                         f"takes the augment {{tuk}}"),
                via=(Via("1.2.27", f"{sk(s.s)} is of one mātrā, so it is short"),))


@rule("6.1.73", name=_named("6.1.73"), families=("agama",), **_TUK)
def che_ca(v: View):
    """
    छकारे परतः संहितायां ह्रस्वस्य तुगागमो भवति — इच्छति, यच्छति, शिवच्छाया,
    स्वच्छाया. Always, for a short vowel; the vowel, not the word ending in it,
    takes the augment (ह्रस्व एवात्रागमी, न तु तदन्तः).

    The त् is put after the vowel and belongs to the vowel's word, so before a
    छ् at the end of a pada it is a pada-final झल् — and 8.2.39, 8.4.40 and
    8.4.55 make it च् in that order, as the Kaumudī derives स्वच्छाया.
    """
    for j in v.pairs():
        left, right = j.left, j.right
        if right.s == "ch" and left.is_vowel and is_hrasva(left.s):
            yield _tuk(
                left, right, why=f"{sk(right.s)} follows a short vowel",
                because=(f"{sk(left.s)} is a short vowel and {sk(right.s)} "
                         f"follows in one flow of speech, so it takes the "
                         f"augment {{tuk}}, always"),
                via=_SAMHITA + (Via("1.2.27", f"{sk(left.s)} is of one mātrā, "
                                              "so it is short"),))


@rule("6.1.74", name=_named("6.1.74"), families=("agama",),
      overrides=(("6.1.76", _said(
          "kashika", "6.1.74", "इति विकल्पे प्राप्ते नित्यं तुगागमो भवति")),),
      **_TUK)
def angmangos_ca(v: View):
    """
    आङो ङित ईषदादिषु चतुर्ष्वर्थेषु वर्तमानस्य माङश्च प्रतिषेधवचनस्य छकारे परतः
    तुगागमो भवति, नित्यम् — आच्छादयति, ईषच्छाया, माच्छिदत्. Not आ छाया / आच् छाया
    (the आ of recollection), nor प्रमा छन्दः / प्रमाच् छन्दः — the ङ् of आङ्माङोः
    is there to keep them out (ङिद्विशिष्टग्रहणं किम्?).

    Whether an आ is आङ् (in one of its four senses) and whether मा is the
    prohibitive माङ् is meaning; the caller says so with the flags `ang`
    and `mang`. It is the अपवाद of the option 6.1.76 would give a pada-final
    long vowel: पदान्ताद् वा इति विकल्पे प्राप्ते नित्यं तुगागमो भवति.
    """
    for j in v.pairs():
        left, right = j.left, j.right
        word = v.word(left)
        if right.s == "ch" and left.is_vowel and \
                (word.has("ang") or word.has("mang")) and v.ends_word(left):
            which = "{āṅ}" if word.has("ang") else "{māṅ}"
            yield _tuk(
                left, right, why=f"{sk(right.s)} follows {which}",
                because=(f"{sk(left.s)} is {which} and {sk(right.s)} follows, "
                         f"so it takes the augment {{tuk}}, and not by option "
                         f"as 6.1.76 would make it"),
                via=_SAMHITA)


@rule("6.1.75", name=_named("6.1.75"), families=("agama",), **_TUK)
def dirghat(v: View):
    """
    छकारे परतो दीर्घात् तस्यैव दीर्घस्य तुगागमो भवति — ह्रीच्छति, म्लेच्छति.

    The augment belongs to the long vowel, not to the छ् (दीर्घस्यायं तुक् न तु
    छस्य: the Kaumudī's proof is सेनासुराच्छाया). Where the long vowel ends a
    पद 6.1.76 governs it instead — पूर्वेण नित्यं प्राप्तो वा तुगागमो भवति — so
    this rule keeps the long vowels inside a pada. (The engine's option blocks
    only the optional rule itself, so a rule that an optional one displaces must
    not be offered where it governs; see the core request in the report.)
    """
    for j in v.pairs():
        left, right = j.left, j.right
        if right.s == "ch" and left.is_vowel and is_dirgha(left.s) and \
                not v.pada_final(left):
            yield _tuk(
                left, right, why=f"{sk(right.s)} follows a long vowel",
                because=(f"{sk(left.s)} is a long vowel inside a pada and "
                         f"{sk(right.s)} follows, so the long vowel takes the "
                         f"augment {{tuk}}, always"),
                via=_SAMHITA + (Via("1.2.27", f"{sk(left.s)} is of two mātrās, "
                                              "so it is long"),))


@rule("6.1.76", name=_named("6.1.76"), families=("agama",), **_TUK)
def padantad_va(v: View):
    """
    दीर्घात् पदान्तात् छे परे तुगागमो वा भवति — कुटीच्छाया, कुटीछाया; लक्ष्मीच्छाया,
    लक्ष्मी छाया. A प्राप्तविभाषा: पूर्वेण नित्यं प्राप्तो वा तुगागमो भवति (Kāśikā) —
    the option displaces the invariable augment of 6.1.75 for a pada-final long
    vowel. This is a rule about a पदान्त and not a पदविधि, so the two words need
    not be construed together (Tattvabodhinī).

    VEDIC vārttika विश्वजनादीनां छन्दसि वा तुगागमो भवति is not done: a list of
    words (विश्वजनच्छत्रम्, न च्छायां करवोऽपरम्) no letter or flag names.
    """
    for j in v.pairs():
        left, right = j.left, j.right
        if right.s == "ch" and left.is_vowel and is_dirgha(left.s) and \
                v.pada_final(left):
            yield _tuk(
                left, right, why=f"{sk(right.s)} follows a pada-final long vowel",
                because=(f"{sk(left.s)} is a long vowel ending a pada and "
                         f"{sk(right.s)} follows, so the long vowel may take "
                         f"the augment {{tuk}} — or not"),
                via=_SAMHITA + (Via("1.2.27", f"{sk(left.s)} is of two mātrās, "
                                              "so it is long"),),
                optional=VA)


# ---------------------------------------------------------------------------
# 8.2.24–8.2.29 — a sound at the head or the end of a cluster is lost
# ---------------------------------------------------------------------------


@rule("8.2.24", name=_named("8.2.24"), families=("hal",))
def rat_sasya(v: View):
    """
    संयोगान्तस्य पदस्य यो रेफस्तस्मादुत्तरस्यान्त्यस्य सकारस्य लोपो भवति — मातुः,
    पितुः, क्रोष्टुः (from मातुर्, पितुर्, क्रोष्टुर् + स्), गोभिरक्षाः.

    A नियम on 8.2.23: the loss is of a स् AND of no other sound after र्. The
    engine has no 8.2.23, so there is nothing for the restriction to restrain and
    this module does only the loss it licenses — see COVERAGE. The र् and the
    final स् must be of one pada (one word, or the pieces of one pada).
    """
    for j in v.pairs():
        left, right = j.left, j.right
        if j.kind not in (WITHIN, ANGA) or left.s != "r" or right.s != "s":
            continue
        if not v.pada_final(right) or right.through or left.through:
            continue
        yield Application(
            site=site(left, right),
            # The स् is a whole piece of its own, and with it gone the र् is
            # the last sound of the pada. A plain loss would leave the piece
            # the र् belongs to still joined to an aṅga-boundary that names
            # nothing, and 8.3.15 would not find the pada's end — so the two
            # sounds become one र् of the LATER piece, which ends the pada.
            edits=(_merged(left, right, left.s),),
            detail=Detail(
                kind=LOPA, sthanin=right.s, adesa="",
                nimitta=f"it follows {sk(left.s)} at the end of a pada",
                because=(f"the pada ends in the cluster {sk('rs')}: a {{s}} after "
                         f"a {{r}} at the end of a pada that ends in a "
                         f"{{saṃyoga}} is lost, and the {{r}} now ends the "
                         f"pada"),
                via=(S.pancami_para("{r}"),)))


def _sic(v: View, s: Sight) -> bool:
    return s.s == "s" and v.word(s).has("sic")


@rule("8.2.25", name=_named("8.2.25"), families=("hal",))
def dhi_ca(v: View):
    """
    धकारादौ प्रत्यये परतः सिचः सकारस्य लोपो भवति — अलविध्वम् / अलविढ्वम् (the
    Bhāṣya: धि सकारे सिचो लोपः; the Kāśikā: इतः प्रभृति सिचः सकारस्य लोप
    इष्यते). Not चकाद्धि पलितं शिरः, पयो धावति — the स् there is not the
    aorist's. The caller flags the piece `sic` and the ending `pratyaya`.
    """
    right_of = _right_of(v)
    for s in v.live:
        nxt = right_of.get(s.uid)
        if not _sic(v, s) or nxt is None or s.through:
            continue
        if nxt.s == "dh" and v.begins_word(nxt) and v.word(nxt).has("pratyaya"):
            yield _lost([s, nxt], s, marks=(SIC_LOPA,),
                        nimitta=f"an ending beginning with {sk(nxt.s)} follows",
                        because=(f"this {{sic}} {{s}} stands before the ending "
                                 f"{sk(nxt.s)}…, so it is lost"),
                        via=(S.saptami_purva("{dh}"),))


@rule("8.2.26", name=_named("8.2.26"), families=("hal",))
def jhalo_jhali(v: View):
    """
    झलः परस्य सिचः सकारस्य झलि परतो लोपो भवति — अभित्त, अभित्थाः, अच्छित्त.
    Not अमंस्त (no झल् before the स्), अभित्साताम् (none after it). The
    Kāśikā holds these rules to the aorist's स् alone: तेनेह न भवति —
    सोमसुत् स्तोता.
    """
    jhal = S.members("jhaL")
    right_of, left_of = _right_of(v), _left_of(v)
    for s in v.live:
        if not _sic(v, s) or s.through:
            continue
        before, after = left_of.get(s.uid), right_of.get(s.uid)
        if before is None or after is None:
            continue
        if before.s in jhal and after.s in jhal:
            yield _lost([before, s, after], s, marks=(SIC_LOPA,),
                        nimitta=(f"the {{jhal}} {sk(before.s)} before it and "
                                 f"the {{jhal}} {sk(after.s)} after"),
                        because=(f"this {{sic}} {{s}} stands after the {{jhal}} "
                                 f"{sk(before.s)} and before the {{jhal}} "
                                 f"{sk(after.s)}, so it is lost"),
                        via=(S.pancami_para("{jhal}"),))


@rule("8.2.27", name=_named("8.2.27"), families=("hal",))
def hrasvad_angat(v: View):
    """
    ह्रस्वान्ताद् अङ्गात् परस्य सिचः सकारस्य झलि परतो लोपो भवति — अकृत, अकृथाः,
    अहृत. Not अच्योष्ट (the aṅga ends in a long vowel), अलाविष्टाम् (the short
    vowel is the augment's, not the aṅga's), अकृषाताम् (no झल् follows).
    """
    jhal = S.members("jhaL")
    right_of, left_of = _right_of(v), _left_of(v)
    for s in v.live:
        if not _sic(v, s) or s.through:
            continue
        before, after = left_of.get(s.uid), right_of.get(s.uid)
        if before is None or after is None or after.s not in jhal:
            continue
        if before.is_vowel and is_hrasva(before.s) and \
                v.boundary_after(before) == ANGA:
            yield _lost([before, s, after], s, marks=(SIC_LOPA,),
                        nimitta=(f"the aṅga ends in the short {sk(before.s)} "
                                 f"and the {{jhal}} {sk(after.s)} follows"),
                        because=(f"this {{sic}} {{s}} follows an aṅga ending in "
                                 f"the short vowel {sk(before.s)} and the "
                                 f"{{jhal}} {sk(after.s)} follows, so it is lost"),
                        via=(Via("1.2.27", f"{sk(before.s)} is of one mātrā"),))


@rule("8.2.28", name=_named("8.2.28"), families=("hal",))
def ita_iti(v: View):
    """
    इटः परस्य सिचः सकारस्य ईटि परतो लोपो भवति — अदेवीत्, असेवीत्, अकोषीत्.
    Not अकार्षीत् (no इट्), अलाविष्टाम् (no ईट्). The caller flags the augments
    `it_agama` and `iit_agama`.

    PARTIAL. The vārttika सिज्लोप एकादेशे सिद्धो वाच्यः says the loss is
    *siddha* to the ekādeśa that joins इ and ई into ई; 8.2.1 would hide it, and
    only a `consumes=(SIC_LOPA,)` on 6.1.101 (the ekādeśa family's) can show it,
    so here the loss is made and the vowels are left as two sounds — reported in
    the open questions.
    """
    right_of, left_of = _right_of(v), _left_of(v)
    for s in v.live:
        if not _sic(v, s) or s.through:
            continue
        before, after = left_of.get(s.uid), right_of.get(s.uid)
        if before is None or after is None:
            continue
        if v.word(before).has("it_agama") and v.word(after).has("iit_agama"):
            yield _lost([before, s, after], s, marks=(SIC_LOPA,),
                        nimitta="the augment {iṭ} before it and {īṭ} after",
                        because=(f"this {{sic}} {{s}} stands between the augments "
                                 f"{{iṭ}} and {{īṭ}}, so it is lost"),
                        via=(S.saptami_purva("{īṭ}"),))


@rule("8.2.29", name=_named("8.2.29"), families=("hal",))
def skoh_samyogadyor_ante_ca(v: View):
    """
    पदस्यान्ते यः संयोगः, झलि परतो वा यः संयोगः, तदाद्योः सकारककारयोर्लोपो भवति —
    तट्, तष्टः, काष्ठतट्, लग्नः, साधुलक्. Not पयः, शक् (no cluster: संयोगाद्योरिति
    किम्?), तक्षिता (no झल् follows: अन्ते चेति किम्?).

    The स् or क् is the FIRST sound of a cluster that ends the root and either
    ends the pada or stands before a झल्. It lies inside the piece, away from the
    junction, so the piece must be one the derivation has not finished: joined
    to another by an aṅga boundary, or flagged `dhatu` (`View.joined_pada`).

    The vārttika झलि सङीति वक्तव्यम् (काष्ठशक् स्थाता) is not done: the Bhāṣya
    rejects it (काष्ठशगेव नास्ति — no such word exists to need it).
    """
    jhal = S.members("jhaL")
    right_of = _right_of(v)
    for last in v.live:
        cluster = v.final_cluster(last)
        if len(cluster) < 2 or not v.ends_word(last):
            continue
        head = cluster[0]
        if head.s not in (_sa(), VARGA["ku"][0]) or head.through:
            continue
        word = v.word(last)
        if not (word.flag_value("dhatu") or word.has("dhatu")
                or v.joined_pada(last)):
            continue
        nxt = right_of.get(last.uid)
        before_jhal = nxt is not None and nxt.s in jhal
        final = v.pada_final(last)
        if not (before_jhal or final):
            continue
        why = " and ".join(([f"the {{jhal}} {sk(nxt.s)} follows"]
                            if before_jhal else []) +
                           (["the cluster ends a pada"] if final else []))
        rest = "".join(x.s for x in cluster)
        yield _lost(
            [head, last] + ([nxt] if before_jhal else []), head,
            nimitta=why,
            because=(f"{sk(head.s)} begins the cluster {sk(rest)} at the end "
                     f"of the root, and {why}, so {sk(head.s)} is lost"),
            via=(Via("1.1.7", "a cluster is consonants with nothing between "
                              "them ({saṃyoga})"),))


# ---------------------------------------------------------------------------
# 8.2.30 चोः कुः
# ---------------------------------------------------------------------------


@rule("8.2.30", name=_named("8.2.30"), families=("hal",))
def coh_kuh(v: View):
    """
    चवर्गस्य कवर्गादेशो भवति झलि परतः पदान्ते च — पक्ता, वक्ता, ओदनपक्, वाक्.

    Both conditions are read from the form: a झल् follows (an adjacent pair),
    or the sound ends a पद. Which कु sound is 1.1.50's business. It does not
    reach the inside of a finished word — the च्छ् of *गच्छति* is a च् 8.4.40
    made long ago (`View.pairs`).

    The roots of 8.2.36 (यज्, सृज्, …) are its exception, and 8.2.36 says so.
    """
    jhal = S.members("jhaL")
    cu, ku = frozenset(VARGA["cu"]), tuple(VARGA["ku"])
    before_jhal = {j.left.uid: j.right for j in v.pairs()
                   if j.right.s in jhal}
    for s in v.live:
        if s.s not in cu:
            continue
        nxt = before_jhal.get(s.uid)
        final = v.pada_final(s)
        if nxt is None and not final:
            continue
        sub = _nearest(s.s, ku)
        if sub is None:
            continue
        why = " and ".join(([f"a {{jhal}} {sk(nxt.s)} follows"] if nxt else [])
                           + (["it ends a pada"] if final else []))
        yield _change(
            [s] + ([nxt] if nxt else []), s, sub, nimitta=why,
            because=(f"{sk(s.s)} is of the {{cu}} class and {why}, so it "
                     f"becomes the {{ku}} sound {sk(sub)}"),
            via=(S.alo_antyasya(s.s),
                 S.antaratama(s.s, sub, "{ku} (" + ", ".join(ku) + ")")))


# ---------------------------------------------------------------------------
# 8.2.31–8.2.35 — what a ह् becomes
# ---------------------------------------------------------------------------


def _h_rule(v: View, sub: str, *, root_ok=None, jhal_only: bool = False,
            optional: str = "") -> Iterator[Application]:
    """The shared shape of 8.2.31–35: a ह् before a झल् or ending a pada — any
    ह् (`root_ok` None), or the last sound of a root the sūtra names."""
    jhal = S.members("jhaL")
    right_of = _right_of(v)
    for s in v.live:
        if s.s != "h" or s.through:
            continue
        root = _root(v, s)
        if root_ok is not None:
            if root is None or not root_ok(root) or not v.ends_word(s):
                continue
        nxt = right_of.get(s.uid)
        nxt = nxt if nxt is not None and nxt.s in jhal else None
        final = v.pada_final(s) and not jhal_only
        if nxt is None and not final:
            continue
        why = " and ".join(([f"the {{jhal}} {sk(nxt.s)} follows"] if nxt else [])
                           + (["it ends a pada"] if final else []))
        yield _change(
            [s] + ([nxt] if nxt else []), s, sub, optional=optional,
            nimitta=why,
            because=(f"{sk(s.s)} " + (f"ends the root {sk(root)}, and "
                                       if root and root_ok else "is here, and ")
                     + f"{why}, so it becomes {sk(sub)}"),
            via=(S.alo_antyasya(s.s),))


@rule("8.2.31", name=_named("8.2.31"), families=("hal",))
def ho_dhah(v: View):
    """
    हकारस्य ढकारादेशो भवति झलि परतः पदान्ते च — सोढा, वोढा, जलाषाट्, लिट्.

    Any ह्. The roots that take घ्, ध् or थ् instead are the exceptions of
    8.2.32–35. The ढ् is an intermediate step: 8.2.39 voices it, 8.4.55/8.4.56
    harden it, 8.2.40 and 8.4.41 turn what follows it — which is why सह् + ता
    goes on to सोढा and लिह् + स् to लिट्.
    """
    yield from _h_rule(v, "ḍh")


_APAVADA = _said("bhashya", "8.2.32", "उक्तमेतत्-अपवादो वचनप्रामाण्यादिति")


@rule("8.2.32", name=_named("8.2.32"), families=("hal",),
      overrides=(("8.2.31", _APAVADA),))
def dader_dhator_ghah(v: View):
    """
    दकारादेर्धातोर्हकारस्य घकारादेशो भवति झलि परतः पदान्ते च — दग्धा, दोग्धा,
    काष्ठधक्, गोधुक्. Not लेढा, गुडलिट् (लिह् does not begin with द्).

    The root is the caller's (`dhatu:duh`); the द् is asked of the root *as
    taught* (उपदेशे — Kaumudī), not of the form the affixes have made. दुह्,
    द्रुह्…: द्रुह् is 8.2.33's — its option is between घ् and ढ् — so 8.2.33
    takes it here (and the engine's option blocks only the optional rule, so
    this rule must not offer the घ् again in the course that declined it).
    """
    yield from _h_rule(
        v, "gh", root_ok=lambda r: _sounds(r)[0] == "d"
        and r not in DRUH_FOUR)


@rule("8.2.33", name=_named("8.2.33"), families=("hal",),
      overrides=(("8.2.31", _said(
          "kashika", "8.2.33",
          "द्रुहेर्दादित्वाद् घत्वं नित्यं प्राप्तम्, इतरेषामप्राप्तमेव घत्वं विकल्प्यते")),
                 ("8.2.32", _said(
                     "kashika", "8.2.33",
                     "द्रुहेर्दादित्वाद् घत्वं नित्यं प्राप्तम्"))))
def va_druhamuha(v: View):
    """
    द्रुह् मुह् ष्णुह् ष्णिह् इत्येतेषां हकारस्य वा घकारादेशो भवति झलि परतः
    पदान्ते च — द्रोग्धा / द्रोढा, मित्रध्रुक् / मित्रध्रुट्, उन्मोग्धा / उन्मोढा.

    The option is between घ् and the ढ् of 8.2.31. For द्रुह् it is a
    प्राप्तविभाषा (its द् made 8.2.32's घ् invariable), for the other three an
    अप्राप्तविभाषा — the Kāśikā says so in as many words. Both courses are
    returned; the one that declines is 8.2.31's.
    """
    yield from _h_rule(v, "gh", root_ok=lambda r: r in DRUH_FOUR,
                       optional=VA)


@rule("8.2.34", name=_named("8.2.34"), families=("hal",),
      overrides=(("8.2.31", _APAVADA),))
def naho_dhah(v: View):
    """
    नहो हकारस्य धकारादेशो भवति झलि परे पदान्ते च — नद्धम्, नद्धुम्, उपानत्.
    The root is the caller's (`dhatu:nah`)."""
    yield from _h_rule(v, "dh", root_ok=lambda r: r == "nah")


@rule("8.2.35", name=_named("8.2.35"), families=("hal",),
      overrides=(("8.2.31", _said(
          "kashika", "8.2.35",
          "आदेशान्तरकरणं झषस्तथोर्धोऽधः इत्यस्य निवृत्त्यर्थम्")),))
def aho_thah(v: View):
    """
    आहो हकारस्य थकारादेशो भवति झलि परतः — इदमात्थ, किमात्थ. Not आह, आहतुः,
    आहुः (no झल् follows). The substitute is थ् and not ढ् so that 8.2.40
    (झषस्तथोर्धोऽधः) shall not turn the त् or थ् that follows into ध् — the
    Kāśikā: आदेशान्तरकरणं झषस्तथोर्धोऽधः इत्यस्य निवृत्त्यर्थम्. The root is the
    caller's (`dhatu:ah`, or `āh` as the sūtra names the aṅga).
    """
    yield from _h_rule(v, "th", root_ok=lambda r: r in _AH, jhal_only=True)


_AH = ("āh", "ah")

_HR_GRAH_TEXT = "हृग्रहोर्भश्छन्दसि हस्येति वक्तव्यम्"
_VEDA_HR_GRAH = _said("kashika", "8.2.35", _HR_GRAH_TEXT)


@rule("8.2.35", name=_named("8.2.35"), families=("hal",),
      authority=VARTTIKA, vedic=True, varttika=_HR_GRAH_TEXT)
def hrgrahor_bhah_chandasi(v: View):
    """
    VEDIC. हृग्रहोर्भश्छन्दसि हस्य — the ह् of हृ and ग्रह् is भ् in the Veda:
    गर्दभेन संभरति, ग्रभीता, जभ्रिरे, उद्ग्राभं च निग्राभं च. Read only when the
    caller asks for the Veda (`veda=True`); the root is the caller's
    (`dhatu:hṛ` or `dhatu:grah`).
    """
    for s in v.live:
        root = _root(v, s)
        if s.s == "h" and root in _HR_GRAH and not s.through:
            yield _change(
                [s], s, "bh", nimitta="the root is {hṛ} or {grah} in the Veda",
                because=(f"{sk(s.s)} is in the root {sk(root)}, and in the Veda "
                         f"the {{h}} of {{hṛ}} and {{grah}} is {{bh}} — "
                         + _VEDA_HR_GRAH),
                via=(), authority=VARTTIKA, varttika=_HR_GRAH_TEXT)


_HR_GRAH = ("hṛ", "grah")


# ---------------------------------------------------------------------------
# 8.2.36–8.2.38 — ष्, and भष् for बश्
# ---------------------------------------------------------------------------


_SATVA_APAVADA = _said(
    "padamanjari", "8.2.36",
    "इतरेषां तु कुत्वे तदपवादः षत्वं विधीयते")


#: व्रश्च as the dhātupāṭha teaches it (ओव्रश्चू): with a स्. The sūtra writes
#: the श् that 8.4.40's श्चुत्व makes of it before the च्.
_VRASC = "vrasc"


def _vrascadi(root: str) -> bool:
    return (root in VRASCADI_EIGHT or root == _VRASC
            or _sounds(root)[-1] in _CH_SA)


_CH_SA = ("ch", "ś")


@rule("8.2.36", name=_named("8.2.36"), families=("hal",),
      overrides=(("8.2.30", _SATVA_APAVADA), ("8.2.39", _SATVA_APAVADA)))
def vrasca_bhrasja(v: View):
    """
    व्रश्च भ्रस्ज सृज मृज यज राज भ्राज इत्येतेषां छकारान्तानां शकारान्तानां च
    षकार आदेशो भवति झलि परतः पदान्ते च — यष्टा, स्रष्टा, मार्ष्टा, उपयट्,
    सम्राट्, प्रष्टा (from प्रच्छ्), लेष्टा, विट्.

    The अपवाद of 8.2.30 for the j-final roots and of 8.2.39 for a श्-final one
    (शकारान्तस्य जश्त्वे प्राप्ते, इतरेषां तु कुत्वे तदपवादः षत्वं विधीयते —
    Padamañjarī). The root is the caller's (`dhatu:yaj`); the substitute takes
    only the root's last sound (1.1.52). 8.4.41 then makes the त् after it ट्
    (यष्टा), and 8.2.39 voices it at a pada's end (उपयड्, उपयट्).
    """
    cu = frozenset(VARGA["cu"])
    sibilant = _sha_palatal()
    right_of = _right_of(v)
    jhal = S.members("jhaL")
    for s in v.live:
        root = _root(v, s)
        if root is None or not _vrascadi(root) or not v.ends_word(s) \
                or s.through or s.s != _sounds(root)[-1] \
                or (s.s not in cu and s.s != sibilant):
            continue
        nxt = right_of.get(s.uid)
        nxt = nxt if nxt is not None and nxt.s in jhal else None
        final = v.pada_final(s)
        if nxt is None and not final:
            continue
        why = " and ".join(([f"the {{jhal}} {sk(nxt.s)} follows"] if nxt else [])
                           + (["it ends a pada"] if final else []))
        yield _change(
            [s] + ([nxt] if nxt else []), s, _sha(), nimitta=why,
            because=(f"{sk(s.s)} ends the root {sk(root)}, of the kind 8.2.36 "
                     f"names, and {why}, so it becomes ṣ"),
            via=(S.alo_antyasya(s.s),))


_PARAU_VRAJEH = _varttika("8.2.36", "व्रजेः")


@rule("8.2.36", name=_named("8.2.36"), families=("hal",),
      authority=VARTTIKA, varttika=_PARAU_VRAJEH,
      overrides=(("8.2.30", _SATVA_APAVADA),))
def parau_vrajeh_sah(v: View):
    """
    परौ व्रजेः षः पदान्ते — परिव्राट्, परिव्राजौ. The final ज् of व्रज् is ष्
    when परि stands before it as its upapada, at the end of a pada (a vārttika,
    not Pāṇini). परि is the previous word, or the beginning of this one.
    """
    cu = frozenset(VARGA["cu"])
    for s in v.live:
        if s.s not in cu or _root(v, s) != "vraj" or not v.pada_final(s) \
                or s.through:
            continue
        first = v.word_sights(s.w)[0]
        before = v.prev(first)
        if not (v.word(s).text.startswith("pari")
                or (before is not None and v.word(before).text == "pari")):
            continue
        yield _change(
            [s], s, _sha(), nimitta="it ends a pada after {pari}",
            because=(f"{sk(s.s)} ends {{vraj}} with {{pari}} before it and "
                     f"ends a pada, so it becomes {sk(_sha())}"),
            via=(S.alo_antyasya(s.s),), authority=VARTTIKA,
            varttika=_PARAU_VRAJEH)


@rule("8.2.37", name=_named("8.2.37"), families=("hal",))
def ekaco_baso_bhas(v: View):
    """
    धातोरवयवो य एकाच् झषन्तस्तदवयवस्य बशः स्थाने भष् आदेशो भवति स्-ध्वयोः
    परतः पदान्ते च — भोत्स्यते, अभुद्ध्वम्, अर्थभुत्, धोक्ष्यते, गोधुक्.

    The root is the caller's (`dhatu:budh`); it must have one vowel, begin with a
    बश् (ब् ग् ड् द्) and END with a झष् — so दुह् reaches it only after 8.2.32
    has made its ह् a घ्, and the rule sees that घ् because 8.2.32 stands before
    it. The भष् is the one of its own varga (1.1.50).

    NOT done: the aṅga formed on a noun (गर्दभयति → गर्धप्), whose 'root' is
    only a part of the word.
    """
    baś = S.members("baŚ")
    bhaṣ = S.members("bhaṢ")
    jhaṣ = S.members("jhaṢ")
    right_of = _right_of(v)
    for last in v.live:
        root = _root(v, last)
        if root is None or last.s not in jhaṣ or not v.ends_word(last) \
                or last.through:
            continue
        sounds = _sounds(root)
        if sum(1 for x in sounds if x in S.members("aC")) != 1 \
                or sounds[0] not in baś:
            continue
        first = _root_first(v, last, root)
        if first is None or first.s not in baś or first.through:
            continue
        nxt = right_of.get(last.uid)
        after = v.next(nxt) if nxt is not None else None
        if v.pada_final(last):
            why = "it ends a pada"
        elif nxt is not None and nxt.s == "s":
            why = f"{sk(nxt.s)} follows"
        elif nxt is not None and nxt.s == "dh" and after is not None \
                and after.s == "v":
            why = "the ending {dhva} follows"
        else:
            continue
        sub = _nearest(first.s, bhaṣ)
        if sub is None or sub == first.s:
            continue
        yield _change(
            [first, last] + ([nxt] if nxt is not None and not v.pada_final(last)
                             else []), first, sub, nimitta=why,
            because=(f"{sk(first.s)} is the {{baś}} that begins the one-vowel "
                     f"root {sk(root)}, which ends in the {{jhaṣ}} "
                     f"{sk(last.s)}, and {why}, so it becomes the {{bhaṣ}} "
                     f"{sk(sub)}"),
            via=(S.antaratama(first.s, sub, "{bhaṣ} (" + ", ".join(sorted(bhaṣ)) + ")"),))


def _dadhati(v: View, sight: Sight) -> bool:
    """दध् — the reduplicated धा (दधाति), which 8.2.38 names and 8.2.40 leaves
    out: the root is धा and the piece is दध्."""
    word = v.word(sight)
    return _root(v, sight) == "dhā" and word.text.startswith("dadh")


@rule("8.2.38", name=_named("8.2.38"), families=("hal",))
def dadhas_tathos_ca(v: View):
    """
    दध् — धा with its reduplication made — has its बश् turned to भष् before त्,
    थ् (dadhas tathoḥ) and before स्, ध्व (the च्): धत्तः, धत्थः, धत्से, धद्ध्वम्.
    Not दधाति (no such sound follows: the sūtra says झषन्तस्येत्येव).

    The piece is the caller's (`dhatu:dhā`, text दध्). The Kāśikā holds that the
    आ's loss (6.4.112) does not stand in for the sound (वचनसामर्थ्यात् आतो
    लोपस्य स्थानिवद्भावो न भवति), so the piece ends in the झष् ध्.
    """
    baś = S.members("baŚ")
    bhaṣ = S.members("bhaṢ")
    right_of = _right_of(v)
    for last in v.live:
        if not _dadhati(v, last) or not v.ends_word(last) or last.s != "dh" \
                or last.through:
            continue
        first = _root_first(v, last, "dadh")
        if first is None or first.s not in baś or first.through:
            continue
        nxt = right_of.get(last.uid)
        after = v.next(nxt) if nxt is not None else None
        if nxt is None:
            continue
        if nxt.s in ("t", "th") or nxt.s == "s" or \
                (nxt.s == "dh" and after is not None and after.s == "v"):
            sub = _nearest(first.s, bhaṣ)
            if sub is None or sub == first.s:
                continue
            yield _change(
                [first, last, nxt], first, sub,
                nimitta=f"{sk(nxt.s)} follows {{dadh}}",
                because=(f"{sk(first.s)} begins {{dadh}}, which ends in the "
                         f"{{jhaṣ}} {sk(last.s)}, and {sk(nxt.s)} follows, so "
                         f"it becomes the {{bhaṣ}} {sk(sub)}"),
                via=(S.antaratama(first.s, sub, "{bhaṣ}"),))


# ---------------------------------------------------------------------------
# 8.2.39–8.2.41
# ---------------------------------------------------------------------------


@rule("8.2.39", name=_named("8.2.39"), families=("hal",))
def jhalam_jaso_nte(v: View):
    """
    पदान्ते झलां जशः स्युः — वागीशः, अग्निचित्, त्रिष्टुप्, षड्. Read at each
    पद's last sound; it does not reach a झल् inside a word (अन्तग्रहणं झलि
    इत्येतस्य निवृत्त्यर्थम्). 8.2.66 is its exception for a final स्.
    """
    jhal = S.members("jhaL")
    jas = tuple(sorted(S.members("jaŚ")))
    for s in v.live:
        if s.s not in jhal or not v.pada_final(s) or s.through:
            continue
        sub = _nearest(s.s, jas)
        if sub is None or sub == s.s:
            continue
        yield _change(
            [s], s, sub, nimitta="the end of a pada",
            because=(f"{sk(s.s)} is a {{jhal}} at the end of a pada, so it "
                     f"becomes its {{jaś}} {sk(sub)}"),
            via=(S.alo_antyasya(s.s),
                 S.antaratama(s.s, sub, "{jaś} (" + ", ".join(jas) + ")")))


@rule("8.2.40", name=_named("8.2.40"), families=("hal",))
def jhasas_tathor_dho_dhah(v: View):
    """
    झषः परयोस्तकारथकारयोः स्थाने धकारादेशो भवति, दधातिं वर्जयित्वा — लब्धा,
    दोग्धा, लेढा, अलब्ध. Not धत्तः, धत्थः (दध् is excepted by अधः, and its त् stands).

    The project's own `anga.jhasas_tathoh_dhah` is asked what the sūtra does to
    the two sounds; the exception is the caller's (`dhatu:dhā`, text दध्).
    """
    for j in v.pairs():
        left, right = j.left, j.right
        if right.through or _dadhati(v, left):
            continue
        got = jhasas_tathoh_dhah(left.s + right.s)
        if got.result is None or got.at != len(left.s):
            continue
        yield _change(
            [left, right], right, got.now,
            nimitta=f"it follows the {{jhaṣ}} {sk(left.s)}",
            because=(f"{sk(right.s)} follows the {{jhaṣ}} {sk(left.s)}, so it "
                     f"becomes {sk(got.now)}"),
            via=(S.pancami_para("{jhaṣ}"),))


_DDHA = "ḍh"


@rule("8.2.41", name=_named("8.2.41"), families=("hal",))
def sadhoh_kah_si(v: View):
    """
    षकारस्य ढकारस्य च कादेशो भवति सकारे परतः — पेक्ष्यति, अपेक्ष्यत्, लेक्ष्यति.
    Not पिनष्टि, लेढि (no स् follows). The ढ् meant is the one 8.2.31 has made
    from a ह्, seen because 8.2.31 stands before this rule.
    """
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s in (_sha(), _DDHA) and right.s == _sa() \
                and not left.through:
            yield _change(
                [left, right], left, "k",
                nimitta=f"{sk(right.s)} follows",
                because=(f"{sk(left.s)} stands before {sk(right.s)}, so it "
                         f"becomes {sk('k')}"),
                via=(S.saptami_purva(sk(right.s)),))


# ---------------------------------------------------------------------------
# 8.4.40–8.4.44 — श्चुत्व and ष्टुत्व, and what refuses them
# ---------------------------------------------------------------------------

#: What the tradition says of 8.4.40 and 8.4.41 alike, which the trace prints
#: where it bites: the pairs are NOT matched one to one (Kāśikā), and the
#: cause need only be ADJACENT — either side (Bhāṣya: the third case is there so
#: that the sannipāta holds for mere adjacency).
_NOT_ONE_TO_ONE = {
    "cu": _said("kashika", "8.4.40", "स्तोःश्चुनेति यथासंख्यमत्र नेष्यते"),
    "ṭu": _said("kashika", "8.4.41", "अत्रापि तथैव संख्यातानुदेशाभावः"),
}
_EITHER_SIDE = {
    "cu": _said("bhashya", "8.4.40", "आनन्तर्यमात्रे श्चुत्वं यथा स्यात्"),
    "ṭu": _said("bhashya", "8.4.41", "आनन्तर्यमात्रे ष्टुत्वं यथास्यात्"),
}


def _sannipata(v: View, cause_varga: str
               ) -> Iterator[Tuple[Sight, Sight, Sight, Sight]]:
    """
    (left, right, target, cause) for every adjacent pair in which a स् or a
    त-वर्ग sound (*stoḥ*) stands beside a sound of the class `cause_varga` names
    (श् or च-वर्ग; ष् or ट-वर्ग), from EITHER side — the sūtra says श्चुना in the
    third case, not श्चौ in the seventh, so 1.1.66 does not confine the cause to
    what follows (Kāśikā, Nyāsa: यज्ञः, याच्ञा have it before).

    A cause seen only through its past is not offered: the rule had its chance
    at that place before a later rule changed the sound.
    """
    stu = _cls("tu")[1]
    cause_class = _cls(cause_varga)[1]
    for j in v.pairs():
        for target, cause in ((j.left, j.right), (j.right, j.left)):
            if target.s in stu and cause.s in cause_class \
                    and not cause.through and not target.through:
                yield j.left, j.right, target, cause


def _crossed(target: Sight, cause: Sight, cause_varga: str) -> bool:
    """True where a one-to-one pairing (यथासंख्यम्) would NOT have joined the two:
    a स् with a चवर्ग sound, or a त-वर्ग sound with श्."""
    return (target.s == _sa()) != (cause.s == _cls(cause_varga)[0])


def _sannipata_step(v: View, cause_varga: str, tail: str
                    ) -> Iterator[Application]:
    _, klass = _cls(cause_varga)
    for left, right, target, cause in _sannipata(v, cause_varga):
        sub = _nearest(target.s, klass)
        if sub is None or sub == target.s:
            continue
        via = [S.antaratama(target.s, sub, "{" + tail + "} (" +
                            ", ".join(sorted(klass)) + ")")]
        if _crossed(target, cause, cause_varga):
            via.append(Via(
                "1.3.10", f"the pairing in order ({{yathāsaṃkhyam}}) would not join "
                          f"{sk(target.s)} with {sk(cause.s)}, and it is not "
                          f"applied here — " + _NOT_ONE_TO_ONE[cause_varga]))
        if cause is left:
            via.append(Via(
                "1.1.66", f"had the cause been named in the seventh case, "
                          f"1.1.66 would confine it to what FOLLOWS "
                          f"{sk(target.s)}; it is named in the third, so "
                          f"{sk(cause.s)}, standing BEFORE, is a cause too — "
                          + _EITHER_SIDE[cause_varga]))
        freed = _freed_by_anam(v, left, right, target)
        if freed:
            via.append(Via("8.4.42", freed))
        yield _change(
            [left, right], target, sub,
            nimitta=f"{sk(cause.s)} is adjacent",
            because=(f"{sk(target.s)} is a {{s}} or {{tavarga}} sound standing beside "
                     f"{sk(cause.s)}, so it takes that class: {sk(sub)}"),
            via=via)


@rule("8.4.40", name=_named("8.4.40"), families=("hal", "cutva"))
def stoh_scuna_scuh(v: View):
    """
    सकारतवर्गयोः शकारचवर्गाभ्यां योगे शकारचवर्गौ स्तः — रामश्शेते, रामश्चिनोति,
    सच्चित्, शार्ङ्गिञ्जय, यज्ञः, याच्ञा, अग्निचिच्छेते.

    From either side, and the pairs are NOT matched one to one: स्तोःश्चुनेति
    यथासंख्यमत्र नेष्यते — a स् meeting a च-वर्ग sound becomes श्, a त-वर्ग sound
    meeting a श् becomes च-वर्ग. The sthānin and ādeśa do correspond (स्→श्,
    त-वर्ग→च-वर्ग), and that is 1.1.50. 8.4.44 is its refusal. It acts on the
    sounds it can see: after 8.2.39 has made a pada-final त् a द्, it is the द्
    that becomes ज् (सच्चित्).
    """
    yield from _sannipata_step(v, "cu", "ścu")


@rule("8.4.41", name=_named("8.4.41"), families=("hal", "stutva"))
def stoh_stuna_stuh(v: View):
    """
    स्तोः ष्टुना योगे ष्टुः स्यात् — रामष्षष्ठः, रामष्टीकते, पेष्टा, तट्टीका,
    चक्रिण्ढौकसे, अग्निचिट्टीकते.

    The retroflex counterpart of 8.4.40, from either side and not one to one
    (अत्रापि तथैव संख्यातानुदेशाभावः). Its refusals are 8.4.42 (a pada-final
    ट-वर्ग sound before a स् or त-वर्ग sound) and 8.4.43 (a त-वर्ग sound before
    ष्) — the Laghu tags the *udaḥ sthāstambhoḥ* as 8.4.41; that is 8.4.61.
    """
    yield from _sannipata_step(v, "ṭu", "ṣṭu")


#: The words the sūtra and its vārttika free from 8.4.42: the ending नाम्
#: (the sūtra's own अनाम्), and, by the vārttika अनाम्नवतिनगरीणामिति वक्तव्यम्,
#: नवति and नगरी.
_NAM = "nām"
_NAVATI_NAGARI = ("navati", "nagarī")


def _anam(v: View, right: Sight) -> str:
    """Why the स् or त-वर्ग sound `right` is NOT refused by 8.4.42, or ''."""
    if not v.begins_word(right):
        return ""
    word = v.word(right)
    if word.text == _NAM:
        return ("the ending {nām} is excepted by the sūtra's own {anām}, so "
                "the refusal is not made: " + _said(
                    "kashika", "8.4.42", "नामित्येतद् वर्जयित्वा"))
    stem = word.flag_value("stem")
    if word.text in _NAVATI_NAGARI or (stem and to_iast(stem) in _NAVATI_NAGARI):
        return (f"{sk(word.text)} is excepted by the vārttika, so the refusal "
                f"is not made: " + _said(
                    "kashika", "8.4.42",
                    "अनाम्नवतिनगरीणामिति वक्तव्यम्"))
    return ""


def _freed_by_anam(v: View, left: Sight, right: Sight, target: Sight) -> str:
    """The reason 8.4.41 is not refused here, when 8.4.42 WOULD have refused it
    but for नाम्, नवति or नगरी — so the trace names the sūtra that stood aside."""
    if target is right and left.s in VARGA["ṭu"] and v.pada_final(left) \
            and not left.through:
        return _anam(v, right)
    return ""


@rule("8.4.42", name=_named("8.4.42"), families=("hal", "stutva"),
      overrides=(("8.4.41", _said(
          "kashika", "8.4.42",
          "पदान्ताट् टवर्गादुत्तरस्य स्तोः ष्टुत्वं न भवति "
          "नामित्येतद् वर्जयित्वा")),))
def na_padantat_tor_anam(v: View):
    """
    पदान्ताट्टवर्गात्परस्यानामः स्तोः ष्टुर्न स्यात् — षट् सन्तः, षट् ते, श्वलिट्
    साये. Not ईट्टे (the ट-वर्ग sound does not end a pada), सर्पिष्टमम् (the cause
    is ष्, not a ट-वर्ग sound), षण्णाम् (नाम् is excepted).

    The VĀRTTIKA अनाम्नवतिनगरीणामिति वक्तव्यम् adds नवति and नगरी to the
    exceptions: षण्णवतिः, षण्णगरी. They are not rules of their own — they are more
    of what this refusal does not reach — so `_anam` reads them, and the trace of
    8.4.41 says which of the two stood aside. Read from the words' letters
    (the ending is the word नाम्; नगरी and नवति may be given by `stem:`).
    """
    ta = frozenset(VARGA["ṭu"])
    stu = _cls("tu")[1]
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s in ta and right.s in stu and v.pada_final(left) \
                and not left.through and not right.through \
                and not _anam(v, right):
            yield _refuse(
                [left, right], sthanin=f"{left.s}+{right.s}",
                nimitta=f"{sk(right.s)} follows a pada-final {{ṭavarga}} sound",
                because=(f"{sk(left.s)} is a {{ṭavarga}} sound ending a pada and "
                         f"{sk(right.s)} follows, so the {{ṣṭutva}} of 8.4.41 is "
                         f"refused"),
                via=(S.pancami_para("{padāntāt} {ṭoḥ}"),))


@rule("8.4.43", name=_named("8.4.43"), families=("hal", "stutva"),
      overrides=(("8.4.41", _said(
          "kashika", "8.4.43", "तवर्गस्य षकारे यदुक्तं तद् न भवति")),))
def toh_si(v: View):
    """
    तवर्गस्य षकारे परे न ष्टुत्वम् — सन्षष्ठः, अग्निचित् षण्डे, भवान् षण्डे, महान्
    षण्डे. Only where ष् FOLLOWS (षि is in the seventh case: 1.1.66); a ष् before
    a त-वर्ग sound still gives पेष्टा (Padamañjarī: पूर्वभूतेनापि सन्निपाते
    भवत्येव).
    """
    tu = frozenset(VARGA["tu"])
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s in tu and right.s == _sha() and not left.through \
                and not right.through:
            yield _refuse(
                [left, right], sthanin=f"{left.s}+{right.s}",
                nimitta=f"{sk(right.s)} follows a {{tavarga}} sound",
                because=(f"{sk(left.s)} is a {{tavarga}} sound and {sk(right.s)} "
                         f"follows it, so the {{ṣṭutva}} of 8.4.41 is refused"),
                via=(S.saptami_purva(sk(right.s)),))


@rule("8.4.44", name=_named("8.4.44"), families=("hal", "cutva"),
      overrides=(("8.4.40", _said(
          "kashika", "8.4.44", "शकारादुत्तरस्य तवर्गस्य यदुक्तं तद् न भवति")),))
def sat(v: View):
    """
    शात्परस्य तवर्गस्य श्चुत्वं न स्यात् — विश्नः, प्रश्नः. Only the त-वर्ग
    (तोः is carried down), not स् or श्; and only a cause that stands BEFORE
    (शात् is in the fifth case, 1.1.67). Vedic optionality (अयोऽश्ञाति) is not
    done.
    """
    tu = frozenset(VARGA["tu"])
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s == _sha_palatal() and right.s in tu and not left.through \
                and not right.through:
            yield _refuse(
                [left, right], sthanin=f"{left.s}+{right.s}",
                nimitta="a {tavarga} sound follows {ś}",
                because=(f"{sk(right.s)} is a {{tavarga}} sound standing after "
                         f"{sk(left.s)}, so the {{ścutva}} of 8.4.40 is refused "
                         f"and it stays"),
                via=(S.pancami_para(sk(left.s)),))


# ---------------------------------------------------------------------------
# 8.4.55, 8.4.56 — चर्
# ---------------------------------------------------------------------------


@rule("8.4.55", name=_named("8.4.55"), families=("hal",))
def khari_ca(v: View):
    """
    खरि परे झलां चरः स्युः — भेत्ता, अत्ति, युयुत्सते, आरिप्सते, वाक्पतिः, तच्छिवः.
    The चर् is the sound of the same place and internal effort (1.1.50, in the
    Kāśikā's order), so ध् becomes त् and भ् becomes प्. `anga.khari_ca` is the
    project's question-form of the same sūtra, and a test holds the two to the
    same answer for every झल्.
    """
    jhal, khar = S.members("jhaL"), S.members("khaR")
    car = tuple(sorted(S.members("caR")))
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s not in jhal or right.s not in khar or left.through:
            continue
        sub = _nearest(left.s, car)
        if sub is None or sub == left.s:
            continue
        yield _change(
            [left, right], left, sub,
            nimitta=f"the {{khar}} {sk(right.s)} follows",
            because=(f"{sk(left.s)} is a {{jhal}} and {sk(right.s)} a {{khar}}, "
                     f"so {sk(left.s)} becomes its {{car}} {sk(sub)}"),
            via=(S.antaratama(left.s, sub, "{car} (" + ", ".join(car) + ")"),))


_VA_AVASANE = _said("nyaas", "8.4.56",
                    "नित्ये जश्त्वे प्राप्तेऽवसाने वा चरो विधीयन्ते")


@rule("8.4.56", name=_named("8.4.56"), families=("hal",))
def va_avasane(v: View):
    """
    अवसाने वर्तमानानां झलां वा चरादेशो भवति — वाक् / वाग्, त्वक् / त्वग्, श्वलिट् /
    श्वलिड्, त्रिष्टुप् / त्रिष्टुब्, रामात् / रामाद्. The Nyāsa: नित्ये जश्त्वे
    प्राप्ते चर्त्वं विधीयते — the जश्त्व of 8.2.39 has made the जश्, and this
    rule offers the चर् in its place; where the option is declined the जश् stays.
    Both courses are returned. Only at a pause (`View.at_pause`); a स्, already
    a चर्, is not changed (रामस्य keeps its स्).
    """
    jhal = S.members("jhaL")
    car = tuple(sorted(S.members("caR")))
    for s in v.live:
        if s.s not in jhal or not v.at_pause(s) or s.through:
            continue
        sub = _nearest(s.s, car)
        if sub is None or sub == s.s:
            continue
        yield _change(
            [s], s, sub, optional=VA, nimitta="a pause follows",
            because=(f"{sk(s.s)} is a {{jhal}} standing before a pause, so it "
                     f"may become its {{car}} {sk(sub)} in place of the "
                     f"{{jaś}} 8.2.39 has made — " + _VA_AVASANE),
            via=(S.avasana_condition(),
                 S.antaratama(s.s, sub, "{car} (" + ", ".join(car) + ")")))


# ---------------------------------------------------------------------------
# 8.4.60–8.4.65 — the assimilations that go forward and backward
# ---------------------------------------------------------------------------


@rule("8.4.60", name=_named("8.4.60"), families=("hal",))
def torli(v: View):
    """
    तवर्गस्य लकारे परे परसवर्णः स्यात् — तल्लयः, अग्निचिल्लुनाति, विद्वाँल्लिखति,
    भवाँल्लुनाति. The substitute is the sound of the ल् that follows — पर-सवर्ण —
    and the न् of the त-वर्ग, being a nasal, has the nasal ल् (नस्यानुनासिको
    लः). The ल् is what 1.1.9 makes savarṇa to ल्; whether it is nasal is
    `varna.is_anunasika` of the sthānin, the sthānin's own quality (1.1.50).
    """
    tu = frozenset(VARGA["tu"])
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s not in tu or right.s != _LA or left.through:
            continue
        pool = savarnas_of(right.s)
        sub = _nearest(left.s, pool) or pool[0]
        nasal = is_anunasika(left.s)
        yield _change(
            [left, right], left, sub, nasal=nasal,
            nimitta=f"{sk(right.s)} follows a {{tavarga}} sound",
            because=(f"{sk(left.s)} is a {{tavarga}} sound and {sk(right.s)} "
                     f"follows, so it becomes the sound savarṇa to {sk(right.s)}"
                     + (f" — nasal, since {sk(left.s)} is" if nasal else "")),
            via=(S.savarna_of(sub, right.s),
                 S.antaratama(left.s, sub + ("̐" if nasal else ""),
                              "{l} and its nasal form")))


_LA = "l"
_STHA_STAMBH = ("sthā", "stambh")


@rule("8.4.61", name=_named("8.4.61"), families=("hal",))
def udah_sthastambhoh_purvasya(v: View):
    """
    उदः परयोः स्थास्तम्भोः पूर्वसवर्णः स्यात् — उत्थानम्, उत्तम्भनम्, उत्थाता,
    उत्तम्भिता. Not उत्स्नाता (the root is neither). The स् of the root takes
    the sound savarṇa to what stands BEFORE it — the द् of उद् (or the त् 8.4.55
    has made of it) — and, being महाप्राण and अघोष, that is थ् (Kaumudī:
    अत्राघोषस्य सस्य तादृश एव थकारः). ('ādeḥ parasya': only the root's FIRST sound.)

    The word उद् is read from its letters; the root (स्था or स्तम्भ्) is the
    caller's, `dhatu:sthā` or `dhatu:stambh`. The Vedic vārttikas on स्कन्देः and
    रोगे are not done.
    """
    for j in v.pairs():
        left, right = j.left, j.right
        if v.word(left).text != _UD or not v.ends_word(left) \
                or right.s != _sa() or not v.begins_word(right) \
                or right.through or _root(v, right) not in _STHA_STAMBH:
            continue
        pool = savarnas_of(left.s)
        sub = _nearest(right.s, pool)
        if sub is None or sub == right.s:
            continue
        yield _change(
            [left, right], right, sub,
            nimitta=f"it stands after {{ud}} and begins {sk(_root(v, right))}",
            because=(f"{sk(right.s)} begins the root {sk(_root(v, right))} "
                     f"after {{ud}} ({sk(left.s)}), so it takes the sound "
                     f"savarṇa to {sk(left.s)}: {sk(sub)}"),
            via=(S.pancami_para("{ud}"), S.adeh_parasya(right.s),
                 S.savarna_of(sub, left.s),
                 S.antaratama(right.s, sub, "savarṇas of " + sk(left.s))))


_UD = "ud"


@rule("8.4.62", name=_named("8.4.62"), families=("hal",))
def jhayo_ho_nyatarasyam(v: View):
    """
    झयः परस्य हस्य वा पूर्वसवर्णः — वाग्घसति / वाग् हसति, श्वलिड्ढसति, अग्निचिद्धसति,
    त्रिष्टुब्भसति, वाग्घरिः / वाग्हरिः. Not प्राङ् हसति, भवान् हसति (ङ्, न् are not
    झय्). The substitute is the वर्गचतुर्थ — the sound savarṇa to the झय् that is
    घोष, नाद, संवार and महाप्राण like the ह् (Kaumudī).

    Optional (the anuvṛtti of अन्यतरस्याम्): the Laghu's two forms are the taken
    course (वाग्घरिः) and the declined one (वाग् हरिः, written joined वाघरिः —
    the second is the ह् left as it is, not a loss).
    """
    jhay = S.members("jhaY")
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s not in jhay or right.s != _HA or right.through \
                or left.through:
            continue
        pool = savarnas_of(left.s)
        sub = _nearest(right.s, pool)
        if sub is None or sub == right.s:
            continue
        yield _change(
            [left, right], right, sub, optional=ANYATARASYAM,
            nimitta=f"it follows the {{jhay}} {sk(left.s)}",
            because=(f"{sk(right.s)} follows the {{jhay}} {sk(left.s)}, so it "
                     f"may take the sound savarṇa to {sk(left.s)}: {sk(sub)}"),
            via=(S.pancami_para("{jhay}"), S.savarna_of(sub, left.s),
                 S.antaratama(right.s, sub, "savarṇas of " + sk(left.s))))


_HA = "h"


def _sha_to_cha(v: View, klass: str, *, vartika: bool
                ) -> Iterator[Application]:
    """श् after a pada-final झय्, before a sound of `klass` (अट्, or अम् in the
    vārttika): optionally छ्."""
    jhay = S.members("jhaY")
    wanted = S.members(klass)
    if vartika:
        wanted = wanted - S.members("aṬ")
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s not in jhay or right.s != _sha_palatal() or right.through \
                or left.through or not v.pada_final(left):
            continue
        after = v.next(right)     # a condition READ, so the sound after श् in
        if after is None or after.s not in wanted:   # its own word counts
            continue
        yield _change(
            [left, right, after], right, _CHA, optional=ANYATARASYAM,
            authority=VARTTIKA if vartika else SUTRA,
            varttika=_CHATVAM_TEXT if vartika else "",
            nimitta=f"it follows the pada-final {{jhay}} {sk(left.s)} and "
                    f"{sk(after.s)} follows it",
            because=(f"{sk(right.s)} follows the {{jhay}} {sk(left.s)} that "
                     f"ends a pada and is followed by the {{{klass.lower()}}} "
                     f"{sk(after.s)}, so it may become {sk(_CHA)}"),
            via=(S.pancami_para("{jhay}"),))


_CHA = "ch"


@rule("8.4.63", name=_named("8.4.63"), families=("hal",))
def sas_cho_ti(v: View):
    """
    पदान्ताद् झयः परस्य शस्य छो वाऽटि — तच्छिवः / तच्शिवः, वाक्छेते / वाक् शेते,
    अग्निचिच्छेते, श्वलिट्छेते. The झय् is the one this rule can see: in *tat
    śiva* the त् has been made द् (8.2.39), ज् (8.4.40) and च् (8.4.55) by the
    time this rule, which stands after all three, is reached. The झय् must end a
    pada (the Nyāsa and Tattvabodhinī carry पदान्तात् from 8.4.59 into it: नात्र
    मध्वश्चोतन्ति). Both courses are returned.
    """
    yield from _sha_to_cha(v, "aṬ", vartika=False)


_CHATVAM_TEXT = _varttika("8.4.63", "छत्वमम")


@rule("8.4.63", name=_named("8.4.63"), families=("hal",), authority=VARTTIKA,
      varttika=_CHATVAM_TEXT)
def chatvam_ami(v: View):
    """
    छत्वममीति वाच्यम् — a VĀRTTIKA: the श् becomes छ् before any अम्, not only
    before an अट्, so ल्, म्, न्, ञ्, ङ्, ण् also: तच्छ्लोकेन, तच्छ्मश्रुणा.
    (Bhāṣya: छत्वममि तच्छ्लोकेन तच्छ्मश्रुणेति प्रयोजनम्.) It is not Pāṇini's:
    the sūtra says अटि. Only what अट् does not already cover is done here, so
    that a step under the sūtra is never credited to the vārttika.
    """
    yield from _sha_to_cha(v, "aM", vartika=True)


@rule("8.4.65", name=_named("8.4.65"), families=("hal",))
def jharo_jhari_savarne(v: View):
    """
    हलः परस्य झरो वा लोपः सवर्णे झरि — शिण्ढि / शिण्डि, पिण्ढि / पिण्डि, उत्थानम् (the
    doubled ones), प्रत्तम्. Not शार्ङ्गम् (ङ् is no झर्), प्रियपञ्च्ञा, तर्प्ता (the
    two are not savarṇa: सवर्णग्रहणसामर्थ्यात् — any savarṇa झर्, not
    one-to-one).

    A झर् after a consonant, and before a savarṇa झर् (1.1.9), is optionally
    lost. Only the FIRST of the two goes. Optional by the anuvṛtti of
    अन्यतरस्याम्; both courses are returned. The doubling of 8.4.46–47 that
    makes clusters this long is not in this family.
    """
    jhar = S.members("jhaR")
    hal = S.members("haL")
    left_of = _left_of(v)
    for j in v.pairs():
        first, second = j.left, j.right
        before = left_of.get(first.uid)
        if first.s not in jhar or second.s not in jhar or before is None \
                or before.s not in hal or first.through or second.through:
            continue
        if not S.is_member(first.s, "jhaR") or not _savarna(first.s, second.s):
            continue
        yield _lost(
            [before, first, second], first, optional=ANYATARASYAM,
            nimitta=f"it follows the consonant {sk(before.s)} and the "
                    f"savarṇa {{jhar}} {sk(second.s)} follows it",
            because=(f"{sk(first.s)} is a {{jhar}} after the consonant "
                     f"{sk(before.s)} and before {sk(second.s)}, a {{jhar}} "
                     f"savarṇa to it, so it may be lost"),
            via=(S.savarna_of(first.s, second.s),))


def _savarna(first: str, second: str) -> bool:
    return second in savarnas_of(first)


#: Which family already has 8.2.29, if any — see `_elsewhere`.
_8_2_29_IS_IN = _elsewhere("8.2.29")

RULES = (
    hrasvasya_piti_krti_tuk, che_ca, angmangos_ca, dirghat, padantad_va,
    rat_sasya, dhi_ca, jhalo_jhali, hrasvad_angat, ita_iti,
    coh_kuh, ho_dhah, dader_dhator_ghah, va_druhamuha, naho_dhah, aho_thah,
    hrgrahor_bhah_chandasi, vrasca_bhrasja, parau_vrajeh_sah,
    ekaco_baso_bhas, dadhas_tathos_ca, jhalam_jaso_nte,
    jhasas_tathor_dho_dhah, sadhoh_kah_si,
    stoh_scuna_scuh, stoh_stuna_stuh, na_padantat_tor_anam, toh_si, sat,
    khari_ca, va_avasane,
    torli, udah_sthastambhoh_purvasya, jhayo_ho_nyatarasyam, sas_cho_ti,
    chatvam_ami, jharo_jhari_savarne,
) + (() if _8_2_29_IS_IN else (skoh_samyogadyor_ante_ca,))


#: Which sūtras of this family's scope the module implements — the honest
#: account, kept beside the code. See `rulebook.COVERAGE_STATUS`.
COVERAGE = (
    ("6.1.71", "partial", "done where a sounded पित् कृत् follows (ल्यप्: "
     "प्रकृत्य, उपस्तुत्य); क्विप्, whose sounds are all lost, leaves no "
     "junction, so अग्निचित् and सोमसुत् arrive already finished"),
    ("6.1.72", "support", "an adhikāra: संहितायाम् makes 6.1.73–6.1.76 hold "
     "only where the sounds are spoken together; each of them cites it, "
     "with 1.4.109"),
    ("6.1.73", "rule", ""),
    ("6.1.74", "rule", ""),
    ("6.1.75", "rule", ""),
    ("6.1.76", "partial", "the sūtra is done; the Vedic vārttika "
     "विश्वजनादीनां छन्दसि वा तुगागमः names a list of words that no letter or "
     "flag identifies"),
    ("8.2.24", "partial", "the loss of a स् after a र् that ends a संयोगान्त "
     "pada is done; its नियम — that no OTHER sound is lost after a र् — "
     "restrains 8.2.23, which the engine does not have"),
    ("8.2.25", "rule", ""),
    ("8.2.26", "rule", ""),
    ("8.2.27", "rule", ""),
    ("8.2.28", "partial", "the loss is done; the vārttika सिज्लोप एकादेशे "
     "सिद्धो वाच्यः needs the ekādeśa family to list SIC_LOPA in `consumes`, "
     "so the इ and ई are left as two sounds"),
    (("8.2.29", "scope", f"the rule stands in {_8_2_29_IS_IN}.py, which needs "
      "it for the cluster a yaṇ makes (with 8.2.23 and the refusals for the "
      "yaṇ) and has the whole of it; a second rule for one sūtra is refused by "
      "`rulebook.problems()`, so this family stands aside")
     if _8_2_29_IS_IN else
     ("8.2.29", "partial", "done for a cluster's head in a flagged root or in "
      "a piece joined by an aṅga boundary; the vārttika झलि सङीति, which the "
      "Bhāṣya rejects, is not done")),
    ("8.2.30", "rule", ""),
    ("8.2.31", "rule", ""),
    ("8.2.32", "rule", ""),
    ("8.2.33", "rule", ""),
    ("8.2.34", "rule", ""),
    ("8.2.35", "rule", ""),
    ("8.2.36", "rule", ""),
    ("8.2.37", "partial", "done for a root the caller names; the aṅga formed "
     "on a noun (गर्दभयति → गर्धप्), whose 'root' is only a part of the "
     "word, is not"),
    ("8.2.38", "rule", ""),
    ("8.2.39", "rule", ""),
    ("8.2.40", "rule", ""),
    ("8.2.41", "rule", ""),
    ("8.4.40", "rule", ""),
    ("8.4.41", "rule", ""),
    ("8.4.42", "rule", ""),
    ("8.4.43", "rule", ""),
    ("8.4.44", "rule", ""),
    ("8.4.55", "rule", ""),
    ("8.4.56", "rule", ""),
    ("8.4.60", "rule", ""),
    ("8.4.61", "partial", "the sūtra is done; the Vedic vārttikas on स्कन्देः "
     "and रोगे are lexical (उत्कन्द, उत्कन्दको रोगः) and are not"),
    ("8.4.62", "rule", ""),
    ("8.4.63", "rule", ""),
    ("8.4.65", "rule", ""),
    ("8.4.66", "scope", "accent only: उदात्तादनुदात्तस्य स्वरितः changes a "
     "tone, and the engine's sounds carry none"),
    ("8.4.67", "scope", "accent only: it refuses 8.4.66, and names the "
     "teachers गार्ग्य, काश्यप, गालव whose view differs"),
    ("8.4.68", "scope", "अ अ makes the अ of the śivasūtras (declared open "
     "for the grammar's purposes) closed again; the change is of "
     "articulation, not of any letter, and asiddha to the whole grammar "
     "(Kaumudī)"),
)
