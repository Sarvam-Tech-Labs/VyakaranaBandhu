# -*- coding: utf-8 -*-
"""
Nasals, anusvāra, parasavarṇa and the augments कुक्, टुक्, धुट्, तुक्, ङमुट् —
8.3.1–7, 8.3.23–33, 8.4.45, 8.4.58–59.

**What this family is.** Three things that meet at a pada's edge and that the
Laghusiddhāntakaumudī teaches one after the other:

* the **रु of the nasal words** (8.3.1 मतुवसो रु सम्बुद्धौ छन्दसि, 8.3.5 समः सुटि,
  8.3.6 पुमः खय्यम्परे, 8.3.7 नश्छव्यप्रशान्) and the nasal that the sound *before*
  it takes — optionally anunāsika (8.3.2 अत्रानुनासिकः पूर्वस्य तु वा, nitya
  before an अट् by 8.3.3), else an anusvāra put in after it (8.3.4
  अनुनासिकात् परोऽनुस्वारः). The visarga that the रु then becomes is the visarga
  family's (8.3.15, 8.3.34) and is *not* done here;
* the **anusvāra** (8.3.23 मोऽनुस्वारः, 8.3.24 नश्चापदान्तस्य झलि) and the
  places where it is held back (8.3.25 सम्राट्, 8.3.26–27 किं ह्मलयति, 8.3.33
  किम्वुक्तम्), and its **parasavarṇa** (8.4.58, 8.4.59) and the nasal a stop
  takes before a nasal (8.4.45);
* the **augments** a pada-final nasal draws in — कुक्/टुक् (8.3.28), धुट्
  (8.3.29, 8.3.30), तुक् (8.3.31) and ङमुट् (8.3.32).

**Ordering is the grammar again.** Every rule here is in the tripādī, so each
is asiddha to the ones before it (8.2.1), and that settles three things the
tradition argues about, with no extra machinery:

* *पुम् + कोकिलः.* 8.3.6 stands before 8.3.23 and so acts first: the म् is a रु
  before it can be an anusvāra, which is why the Kāśikā gets पुँस्कोकिलः.
* *कुक्, टुक् and धुट् are asiddha to 8.2.39* (Kaumudī: कुक्टुकोरसिद्धत्वाज्जश्त्वं
  न), and the धुट् is asiddha to 8.3.7 (Kāśikā on 8.3.30: धुटश्चर्त्वस्य चासिद्धत्वात् ...
  रुत्वं न भवति). An augment put in by a later rule has no past, so a rule that
  stands before it cannot see it (`Seg.prior` is empty).
* *किम्वुक्तम्.* 8.3.33 makes the उञ् a व्, and the व् is asiddha to 8.3.23, so no
  anusvāra: वत्वस्यासिद्धत्वान्नानुस्वारः (Kaumudī). And *कुर्वन्ति*: 8.3.24 turns
  the न् to an anusvāra, 8.4.58 turns that back to a न्, and the न् 8.4.58 made is
  asiddha to 8.3.24 (no ping-pong) and to 8.4.2 (no ṇatva).

**The रु of 8.3.2's heading is derived, not listed.** The corpus records that
8.3.2 is an अधिकार running to 8.3.12 (`reading.governs`), so a रु that a sūtra of
that stretch made is subject to it — and the रु of 8.2.66 or of 8.3.1 is not:
*इत उत्तरं यस्य स्थाने रुर्विधीयते* (Kāśikā). Those rules read a रु that a LATER
tripādī rule made, which 8.2.1 would hide; their own wording names the रु, so
they list its mark in `consumes` (वचनप्रामाण्यात्, as 6.1.113 does).

**What the letters cannot say is read from the words' flags** (NORTH_STAR §5),
never guessed. Beyond the engine's own (`nipata`, `sambuddhi`, `dhatu:ROOT`,
`pratyaya`) this family reads

  * `sut` — on the word that BEGINS with the augment सुट् (8.3.5): the caller
    says that its first स् is the āgama and not a स् of the root;
  * `kvip` — on a word that ends in the affix क्विप् (8.3.25), with
    `dhatu:rāj`;
  * `matvanta`, `vasvanta` — a word ending in मतुप् or वसु (8.3.1), with
    `sambuddhi`;
  * `nipata` on the piece उ — the particle उञ् of 8.3.33.

**Three vārttikas are done**, each labelled as one (`Detail.authority`): *संपुंकानां
सो वक्तव्यः* (on 8.3.5: the रु of सम् and पुम् before a खर् is a स्), *यवलपरे यवला
वा* (on 8.3.26) and *प्रत्यये भाषायां नित्यम्* (on 8.4.45).

**One home for each provision.** 8.3.33 is in this family's scope and in the
prakṛtibhāva family's, which needs it as the exception to 6.1.125 and displaces
the vowel rules at that place. `rulebook.problems()` refuses two families
defining one sūtra, so where that module has 8.3.33 this one stands aside and
says so in COVERAGE (`_elsewhere`); where it has not, this one has it. The same
goes for *संपुंकानां सो वक्तव्यः*: the Laghusiddhāntakaumudī prints it after 8.3.15,
as a स् for the visarga, which is the visarga family's stage — where that family
states it, this one does not, and the रु goes to the visarga first.

**What is not done, and why.** Each is also in `COVERAGE`.

* 8.3.28's *चयो द्वितीयाः शरि पौष्करसादेः* (प्राङ्ख् षष्ठः) is a general opinion of
  Pauṣkarasādi that the corpus files under 8.4.48, so it is not this family's.
* The second half of *संपुंकानां सो वक्तव्यः*, *समो वा लोपमेके*, is another
  opinion (सम् loses its म्) and is not done.
* 8.3.1's two vārttikas (वन्, भवद्भगवदघवताम्) are Vedic and lexical.
* The *पुंख्यानम्* exception of 8.3.6 (ख्याञादेशे न) turns on a य् that a LATER
  tripādī rule makes out of श्; the engine is given letters.
* The stem before a सुप्/taddhita affix is a pada by 1.4.17. The core has no
  boundary for that, so the vārttika of 8.4.45 (तन्मात्रम्, चिन्मयम्) is written
  for a stem the caller has given as a pada boundary and an affix flagged
  `pratyaya` (see the report).
"""

from __future__ import annotations

import importlib
import pkgutil
import re
from functools import lru_cache
from typing import FrozenSet, List, Optional, Tuple

from src.astadhyayi import corpus, reading
from src.astadhyayi.adesa import AgamaSite, agama_site
from src.astadhyayi.grahana import varieties
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi.parse import to_iast, tokenize
from src.astadhyayi.sandhi.rule import (
    ADESA, AGAMA_KIND, PRATISEDHA, VARTTIKA, Application, Detail, NewSeg, Via,
    insert_after, insert_before, replace, rule, site, sk)
from src.astadhyayi.sandhi.segs import ANUNASIKA, RU, Sight, View, base_of
from src.astadhyayi.sandhi.trace import deva, sutra_text
from src.astadhyayi.sivasutra import resolve
from src.astadhyayi.svara import is_hrasva
from src.astadhyayi.varna import (
    ANTAHSTHA, ANUNASIKA_MARK, ANUSVARA, VARNAS, effort, is_anunasika,
    savarnas_of, varna)
from src.normalizer import devanagari_to_iast


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


def _elsewhere(sutra_id: str, varttika: str = "", *, anywhere: bool = False
               ) -> str:
    """
    The other family module that already defines a rule for this sūtra — the
    sūtra itself, or, with `varttika`, that vārttika on it — or ''. With
    `anywhere`, the vārttika counts wherever the other family has put it (a
    vārttika belongs to the stage of the derivation it acts on, and the corpus
    files it under one sūtra where a family may file it under another).

    A sūtra has one home: `rulebook.problems()` refuses two families defining
    it. 8.3.33 stands in this family's scope and in the prakṛtibhāva family's,
    which needs it as the exception to 6.1.125 and which displaces the vowel
    rules at that place; where that module has it, this one stands aside and
    says so in COVERAGE, and where it has not, this one has it. The same goes
    for a vārttika another family states for itself.
    """
    from src.astadhyayi.sandhi import families
    here = __name__.rsplit(".", 1)[-1]
    for info in pkgutil.iter_modules(families.__path__):
        if info.name == here or info.name.startswith("_"):
            continue
        module = importlib.import_module(f"{families.__name__}.{info.name}")
        for r in getattr(module, "RULES", ()):
            if anywhere and varttika and varttika in r.varttika:
                return info.name
            if r.sutra == sutra_id and r.varttika == varttika:
                return info.name
    return ""


#: Every sentence of the tradition this module quotes, as (source, sūtra, text).
#: `tests/test_sandhi_nasal_anusvara.py` checks each against the commentary on
#: disk, so a quotation that is not the commentary's own fails.
QUOTED: List[Tuple[str, str, str]] = []

_SOURCES = {
    "kashika": "Kāśikā", "kaumudi": "Kaumudī", "balamanorama": "Bālamanoramā",
    "tattvabodhini": "Tattvabodhinī", "bhashya": "Bhāṣya", "nyaas": "Nyāsa",
}


def _said(source: str, sutra_id: str, text: str) -> str:
    """The tradition's own words, recorded for checking, and where they are
    from — the shape a reason in `overrides` and a note must have."""
    QUOTED.append((source, sutra_id, text))
    return (f"{text} ({devanagari_to_iast(text)}; "
            f"{_SOURCES[source]} on {sutra_id})")


#: The option's own word. 8.3.2, 8.3.26, 8.3.33, 8.4.45 and 8.4.59 say वा; 8.3.27
#: to 8.3.31 have it from 8.3.26 by anuvṛtti (Bālamanoramā on each), and 8.3.32's
#: नित्यम् is written to cut that anuvṛtti off.
VA = "वा"

#: Sounds that the sūtras name and that are not classes: the म् and न् of
#: 8.3.24 (नस्य मस्य), the ह् of 8.3.26, the र् of the रु, the उ and the व् of
#: 8.3.33.
_M, _N, _H, _R, _U, _V = "m", "n", "h", "r", "u", "v"


@lru_cache(maxsize=1)
def _ru_prakarana() -> FrozenSet[str]:
    """
    The sūtras whose रु is under 8.3.2's heading.

    Read from the corpus: 8.3.2 is an अधिकार and the corpus records where it
    ends (8.3.12). The रु of 8.3.1 stands BEFORE the heading and so is not
    subject to it (इत उत्तरं यस्य स्थाने रुः), nor is the रु of 8.2.66.
    """
    return frozenset(reading.governs("8.3.2"))


def _prakarana_ru(sight: Sight) -> bool:
    """A रु that a sūtra of 8.3.2's heading substituted."""
    return (sight.s == _R and sight.has(RU)
            and sight.seg.made_by in _ru_prakarana())


def _tadanta(named: str) -> Via:
    return Via(
        "1.1.72",
        f"the sūtra names {sk(named)} and says what to do to a pada, so it is "
        f"read of a pada that ENDS in {sk(named)}")


def _padasya() -> Via:
    return Via(
        "8.1.16",
        "the heading over this stretch: the sound must be the last of a "
        "pada")


def _samhita() -> Via:
    return S.samhita_condition()


def _pratyahara(name: str) -> Via:
    return S.pratyahara(name, ", ".join(resolve(name).sounds))


def _fresh(*sights: Sight) -> bool:
    """
    True where every sound the rule reads is really there.

    A rule sees a sound a LATER tripādī rule has since changed as it was before
    (8.2.1), and that is right for a rule that has not yet acted. But an
    application whose place has been changed under it is one the rule has
    already had its chance at — taken, or (for an option) declined — and the
    engine remembers a declined option only by the place's uids, which the later
    change has renewed. So such a place is not offered again.
    """
    return not any(s.through for s in sights)


def _flag(v: View, sight: Sight, *names: str) -> bool:
    flags = v.flags(sight)
    return any(name in flags for name in names)


def _root_of(v: View, sight: Sight) -> Optional[str]:
    """The root the caller names for this sound's word (`dhatu:ROOT`), IAST."""
    named = v.word(sight).flag_value("dhatu")
    if not named:
        return None
    try:
        root = to_iast(named)
        tokenize(root)
    except Exception:
        return None
    return root


# ---------------------------------------------------------------------------
# The नासिक्य sounds, chosen by 1.1.50 and never listed
# ---------------------------------------------------------------------------


@lru_cache(maxsize=None)
def _nasal_sounds() -> Tuple[str, ...]:
    """
    Every anunāsika sound (1.1.8) there is: the five nasal stops, which are
    mouth-and-nose sounds already, and the nasal forms of the semivowels that
    have one — य् व् ल्, but not र् (रेफवर्जिता यवलाः, Kāśikā on 1.1.9; asked of
    `grahana.varieties`, which reads it).
    """
    found = [s for s in VARNAS if is_anunasika(s)]
    for sound in sorted(ANTAHSTHA):
        found.extend(c for c in varieties(sound)
                     if c != sound and is_anunasika(c))
    return tuple(found)


def _split(sound: str) -> Tuple[str, FrozenSet[str]]:
    """A sound as (plain sound, marks)."""
    if sound.endswith(ANUNASIKA_MARK):
        return base_of(sound), frozenset({ANUNASIKA})
    return sound, frozenset()


@lru_cache(maxsize=None)
def _nasal_of(sthanin: str) -> Optional[str]:
    """
    The anunāsika sound 1.1.50 puts in place of `sthanin` — nearest by place
    AND by internal effort — or None.

    This is 8.4.45's substitute. Nearest by place alone would give र् the ṇ of
    its own place, and the Kaumudī says it does not: *स्थानप्रयत्नाभ्यामन्तरतमे
    स्पर्शे चरितार्थो विधिरयं रेफे न प्रवर्तते* (चतुर्मुखः). So a candidate must
    share the sthānin's place and its effort: a stop takes the nasal stop of its
    varga, य् व् ल् take their own nasal forms, and र् and the ūṣmans (whose
    effort no nasal shares) take nothing.
    """
    here = varna(sthanin)
    if here is None:
        return None
    alike = [c for c in _nasal_sounds()
             if varna(c).sthana is here.sthana
             and effort(c) is effort(sthanin)]
    return S.nearest(sthanin, alike) if alike else None


@lru_cache(maxsize=None)
def _parasavarna(para: str) -> Optional[str]:
    """
    8.4.58's substitute for an anusvāra before the yay sound `para`: of the
    savarṇas of `para` (1.1.9, with the nasal forms 1.1.69 sweeps up with each)
    the one nearest the anusvāra (1.1.50).

    The anusvāra is a nose-sound (नासिकानुस्वारस्य), so the nearest substitute
    is a nasal one, and where a savarṇa has none there is no substitute: the
    Tattvabodhinī says it of the ūṣmans — *शलि तु परसवर्णोऽनुस्वारान्तरतमो न
    संभवतीति*. So र् (whose only savarṇa is र् itself) keeps the anusvāra:
    संराजिता.
    """
    candidates = [c for q in savarnas_of(para) for c in varieties(q)]
    nasal = [c for c in candidates if varna(c).nasika]
    return S.nearest(ANUSVARA, nasal) if nasal else None


def _anunasika_of(sound: str) -> Optional[str]:
    """The nasal form of `sound` itself — what 8.3.2 and 8.3.3 put in place of
    the sound before the रु — or None where it has none (a consonant)."""
    nasal = [c for c in varieties(sound) if c != sound and is_anunasika(c)]
    return S.nearest(sound, nasal) if nasal else None


def _nasal_edit(sight: Sight, sound: str):
    plain, marks = _split(sound)
    return replace(sight, NewSeg(plain, sight.seg.marks | marks))


# ---------------------------------------------------------------------------
# The augments — 1.1.46, and where each stands
# ---------------------------------------------------------------------------


def _agama(name: str) -> Tuple[str, str]:
    """
    An augment as the sūtra writes it — कुक्, टुक्, धुट्, तुक् — as (its sound, its
    इत्). The letters before the उ are the augment, the उ is only there to say
    it (उकार उच्चारणार्थः, Bālamanoramā on 8.3.28), and the last consonant is
    the इत् (1.3.3 हलन्त्यम्) — the one letter 1.1.46 reads.
    """
    sounds = [s for s, _ in tokenize(name)]
    return sounds[0], sounds[-1]


def _agama_site(it: str) -> AgamaSite:
    """1.1.46 and 1.1.47 as `adesa.agama_site` has them: a टित् at the start, a
    कित् at the end, a मित् after the last vowel."""
    where = agama_site((it,))
    if where is None:
        raise ValueError(f"an augment marked {it!r} has no place by 1.1.46/47")
    return where


def _agama_via(name: str, sound: str, it: str, where: AgamaSite,
               beside: str) -> Via:
    if where is AgamaSite.ANTA:
        role = (f"the augment {sk(name)} has {sk(it)} as its {{it}} (1.3.3), so it "
                f"is a {{kit}} and becomes the LAST part of what it augments: "
                f"{sk(sound)} stands right after {sk(beside)}")
    else:
        role = (f"the augment {sk(name)} has {sk(it)} as its {{it}} (1.3.3), so it "
                f"is a {{ṭit}} and becomes the FIRST part of what it augments: "
                f"{sk(sound)} stands right before {sk(beside)}")
    return Via("1.1.46", role)


def _augment(name: str, *, left: Sight, right: Sight, sthanin: Sight,
             nimitta: str, because: str, via: Tuple[Via, ...],
             optional: str = "", also: Tuple[Sight, ...] = ()) -> Application:
    """
    One augment put in beside `sthanin`, at the end (a कित्, after the pada's
    last sound) or at the start (a टित्, before the next pada's first sound).

    The site is what the rule read (`also`: a sound read besides the two that
    meet); the edit is `insert_after` or
    `insert_before`, which give the new sound no past — so every rule that
    stands before this one cannot see it (8.2.1), which is exactly what the
    commentaries rely on (कुक्टुकोरसिद्धत्वात्).
    """
    own, it = _agama(name)
    where = _agama_site(it)
    edit = (insert_after(sthanin, own) if where is AgamaSite.ANTA
            else insert_before(sthanin, own))
    return Application(
        site=site(left, right, *also), edits=(edit,), optional=optional,
        detail=Detail(
            kind=AGAMA_KIND, sthanin=sthanin.s, adesa=own, nimitta=nimitta,
            because=because,
            via=(_agama_via(name, own, it, where, sthanin.s),) + via))


# ---------------------------------------------------------------------------
# The रु and the nasal before it — 8.3.1 to 8.3.7
# ---------------------------------------------------------------------------


def _ru(sight: Sight, sights: Tuple[Sight, ...], nimitta: str, because: str,
        via: Tuple[Via, ...]) -> Application:
    """The last sound of a pada replaced by a रु — a र् whose उ is an इत् and
    gone (1.3.2, 1.3.9), marked `RU` so the rules that name it can find it."""
    return Application(
        site=site(*sights),
        edits=(replace(sight, NewSeg(_R, frozenset({RU}), show="ru")),),
        detail=Detail(
            kind=ADESA, sthanin=sight.s, adesa="ru", nimitta=nimitta,
            because=because,
            via=via + (S.alo_antyasya(sight.s),) + S.it_removed("u")))


@rule("8.3.1", name=_named("8.3.1"), families=("nasal", "visarga"),
      vedic=True)
def matuvaso_ru_sambuddhau_chandasi(v: View):
    """
    मत्वन्तस्य वस्वन्तस्य च पदस्य रुः सम्बुद्धौ परतश्छन्दसि — इन्द्र मरुत्व इह पाहि सोमम्.

    Vedic, so only with `veda=True`. Which words end in मतुप् or वसु, and that
    the form is a vocative, are facts about the derivation of the word and not
    about its letters: the caller writes `{matvanta}` or `{vasvanta}` with
    `{sambuddhi}`. The final न् is what is left of the word once the सुँ has
    gone (6.1.68) and the संयोगान्त लोप (8.2.23) has taken the त्; the रु replaces
    that न् (नकारस्य रुर्भवति, Kāśikā), by 1.1.52.

    The रु stands BEFORE 8.3.2, so the heading of 8.3.2 does not reach it
    (इत उत्तरं यस्य स्थाने रुर्विधीयते): no nasal and no anusvāra follow it.
    """
    for s in v.live:
        if s.s != _N or not v.pada_final(s):
            continue
        if not _flag(v, s, "sambuddhi") or not _flag(v, s, "matvanta",
                                                     "vasvanta"):
            continue
        affix = "matup" if _flag(v, s, "matvanta") else "vasu"
        yield _ru(
            s, (s,), "a vocative, in the Veda",
            (f"{sk(s.s)} ends a pada that ends in {sk(affix)}, in the vocative, "
             f"in the Veda, so it is replaced by {{ru}}"),
            (_padasya(), _tadanta(affix)))


def _ru_word(v: View, sight: Sight, text: str) -> bool:
    """The word the sūtra names (सम्, पुम्, प्रशान्) — read from the letters the
    word was given as."""
    return v.word(sight).text == text


@rule("8.3.5", name=_named("8.3.5"), families=("nasal", "visarga"))
def samah_suti(v: View):
    """
    सम् इत्येतस्य रुर्भवति सुटि परतः — सँस्स्कर्ता, संस्स्कर्ता; उपस्कर्ता, संकृतिः not.

    सुट् is the augment of 6.1.137 समपरिभ्यां करोतौ भूषणे, and the letters of
    सस्कर्ता cannot tell it from a स् of the root, so the caller says which word
    begins with it: `skartā{sut}`. The word must be सम् itself (सम इति किम्?
    उपस्कर्ता — the same augment after उप gives no रु).

    8.3.5 stands before 8.3.23 and so acts first: the म् is a रु before it can
    be an anusvāra. The tradition notes the anusvāra would have given the form
    anyway (यद्यपि मोऽनुस्वारेण सिद्धम्) and that the sūtra is there for the
    anunāsika and the three स्-s — which is 8.3.2's option and 8.3.4's anusvāra.
    """
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != _M or not v.pada_final(left) or not _ru_word(v, left, "sam"):
            continue
        if right.s != "s" or not v.begins_word(right):
            continue
        if not _flag(v, right, "sut"):
            continue
        yield _ru(
            left, (left, right), "the augment {suṭ} follows",
            (f"{sk('m')} is the last sound of {sk('sam')} and the augment "
             f"{{suṭ}} ({sk(right.s)}) follows it, so it is replaced by {{ru}}"),
            (_padasya(), _samhita()))


@rule("8.3.6", name=_named("8.3.6"), families=("nasal", "visarga"))
def pumah_khayy_ampare(v: View):
    """
    पुमित्येतस्य रुर्भवत्यम्परे खयि परतः — पुँस्कोकिलः, पुंस्कोकिलः, पुंस्पुत्रः.

    खयि किम्? पुंदासः. अम्परे किम्? पुंक्षीरम् (the ष् after क् is not an अम्).
    परग्रहणं किम्? पुमाख्यः (the ख् must be next to the म्, not further off).

    OPEN. *ख्याञादेशे न* (पुंख्यानम्, Kaumudī): the य् of ख्या is what a LATER
    tripādī rule makes of the श् of ख्शा, so the tradition does not see an अम् after
    the ख्. The engine is given letters, so पुम् + ख्यानम् would take this रु.
    """
    khay, am = S.members("khaY"), S.members("aM")
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != _M or not v.pada_final(left) or not _ru_word(v, left, "pum"):
            continue
        if right.s not in khay:
            continue
        after = v.next(right)
        if after is None or after.s not in am:
            continue
        yield _ru(
            left, (left, right, after), (f"the {{khay}} {sk(right.s)} follows, with "
                                  f"{sk(after.s)}, an {{am}}, after it"),
            (f"{sk('m')} is the last sound of {sk('pum')}; the {{khay}} "
             f"{sk(right.s)} follows and {sk(after.s)} — an {{am}} — comes "
             f"after that, so it is replaced by {{ru}}"),
            (_padasya(), _pratyahara("khaY"), _pratyahara("aM"), _samhita()))


@rule("8.3.7", name=_named("8.3.7"), families=("nasal", "visarga"))
def nas_chavy_aprasan(v: View):
    """
    नकारान्तस्य पदस्य प्रशान्वर्जितस्य रुर्भवत्यम्परे छवि परतः — भवाँश्छादयति,
    भवांश्छादयति, शार्ङ्गिँश्छिन्धि, चक्रिँस्त्रायस्व.

    छवीति किम्? भवान् करोति. अप्रशानिति किम्? प्रशान् छादयति. अम्पर इत्येव —
    भवान् त्सरुकः. पदस्य किम्? हन्ति (the न् is inside the word).

    The धुट् of 8.3.30 is asiddha to this rule: भवान् + धुट् + साये has no छव् after
    the न् when 8.3.7 looks (धुटश्चर्त्वस्य चासिद्धत्वात्), which the engine gets
    from the धुट् having no past.
    """
    chav, am = S.members("chaV"), S.members("aM")
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != _N or not v.pada_final(left):
            continue
        if _ru_word(v, left, "praśān") or right.s not in chav:
            continue
        after = v.next(right)
        if after is None or after.s not in am:
            continue
        yield _ru(
            left, (left, right, after), (f"the {{chav}} {sk(right.s)} follows, with "
                                  f"{sk(after.s)}, an {{am}}, after it"),
            (f"{sk('n')} ends a pada that is not {sk('praśān')}; the {{chav}} "
             f"{sk(right.s)} follows and {sk(after.s)} — an {{am}} — comes "
             f"after that, so it is replaced by {{ru}}"),
            (_padasya(), _tadanta(_N), _pratyahara("chaV"), _pratyahara("aM"),
             _samhita()))


_SAMPUMKA = _varttika("8.3.5", "संपुंकानां")


@rule("8.3.5", name=_named("8.3.5"), families=("nasal", "visarga"),
      consumes=(RU,), authority=VARTTIKA, varttika=_SAMPUMKA)
def sampumkanam_so_vaktavyah(v: View):
    """
    संपुंकानां सो वक्तव्यः — the रु of सम्, पुम्, कान् before a खर् is a स्, and not the
    visarga that would then be a जिह्वामूलीय or an option: संस्स्कर्ता, पुंस्कामा,
    कांस्कान्.

    A vārttika, not Pāṇini. Its reason is the Kāśikā's: रुविधौ ह्यनिष्टप्रसङ्गः — the
    रु would become a visarga (8.3.15), and 8.3.36 वा शरि would leave it one, and
    8.3.37 कुप्वोः क पौ च would make it a जिह्वामूलीय before the क् of पुंस्कोकिलः.
    So सकार एवादेशो वक्तव्यः (Kāśikā on 8.3.6), and 8.3.5 itself may be read
    with a द्विसकारक निर्देश (समः स्सुटि).

    OPEN. The Laghusiddhāntakaumudī prints the vārttika AFTER 8.3.15, as a स् put
    for the visarga; the corpus and the Kāśikā put it on 8.3.5/8.3.6, as the
    substitute itself. The engine gives a rule of 8.3.5 the view 8.3.5 has, which
    is the रु — the visarga is a later rule's and hidden from it — so this is the
    Kāśikā's course, and the form is the same. The vārttika's second half, समो वा
    लोपमेके, is another opinion and is not done. It comes AFTER 8.3.2 and 8.3.4
    (their numbers are the smaller), so the nasal or the anusvāra is already in.
    """
    khar = S.members("khaR")
    for ru in v.live:
        if not _prakarana_ru(ru) or ru.through or not v.pada_final(ru):
            continue
        if v.word(ru).text not in ("sam", "pum", "kān"):
            continue
        nxt = v.next(ru)
        if nxt is None or nxt.s not in khar or not _fresh(nxt):
            continue
        yield Application(
            site=site(ru, nxt), edits=(replace(ru, NewSeg("s")),),
            detail=Detail(
                kind=ADESA, sthanin="ru", adesa="s",
                nimitta=f"the {{khar}} {sk(nxt.s)} follows",
                because=(f"the {{ru}} of {sk(v.word(ru).text)} stands before "
                         f"the {{khar}} {sk(nxt.s)}, so it is {sk('s')} — not "
                         f"the visarga it would otherwise become"),
                via=(_padasya(), _pratyahara("khaR"), _samhita()),
                authority=VARTTIKA, varttika=_SAMPUMKA,
                note=_said("kashika", "8.3.6",
                           "तस्मादत्र सकार एवादेशो वक्तव्यः")))


@rule("8.3.2", name=_named("8.3.2"), families=("nasal",), consumes=(RU,))
def atra_anunasikah_purvasya_tu_va(v: View):
    """
    इत उत्तरं यस्य स्थाने रुर्विधीयते, ततः पूर्वस्य तु वर्णस्य वानुनासिको भवति —
    सँस्स्कर्ता (the आ of भवान्: भवाँश्छादयति).

    An अधिकार: it does nothing by itself and reaches every रु that a sūtra of
    its own stretch substitutes (`reading.governs` — 8.3.2 to 8.3.12, as the
    corpus records it). The sound before that रु may take its anunāsika form;
    a sound with none (a consonant) is left, and 8.3.4 puts an anusvāra after it.

    **Option (वा).** Both courses are returned: with the sound made nasal
    (8.3.4 then has nothing to add: अनुनासिकं विहाय), and with it left as it is
    (8.3.4 then puts in the anusvāra).
    """
    for ru in v.live:
        if not _prakarana_ru(ru) or ru.through:
            continue
        prev = v.prev(ru)
        if prev is None or prev.seg.nasal or prev.s == ANUSVARA:
            continue
        nasal = _anunasika_of(prev.s)
        if nasal is None:
            continue
        yield Application(
            site=site(prev, ru), edits=(_nasal_edit(prev, nasal),),
            optional=VA,
            detail=Detail(
                kind=ADESA, sthanin=prev.s, adesa=nasal,
                nimitta="a {ru} stands after it",
                because=(f"the {{ru}} that {ru.seg.made_by} put in stands right "
                         f"after {sk(prev.s)}, so {sk(prev.s)} may be made "
                         f"anunāsika: {sk(nasal)}"),
                via=(S.antaratama(prev.s, nasal, "the {anunāsika} sounds"),
                     Via("1.1.69", f"{sk(prev.s)} is named without a {{t}}, so it "
                                   f"stands for its nasal form as well"))))


@rule("8.3.3", name=_named("8.3.3"), families=("nasal",), consumes=(RU,),
      vedic=True,
      overrides=(("8.3.2", _said(
          "kashika", "8.3.3",
          "ततः पूर्वस्यातोऽनुनासिकविकल्पे प्राप्ते नित्यार्थं वचनम्")),))
def ato_ati_nityam(v: View):
    """
    अटि परतो रोः पूर्वस्याकारस्य स्थाने नित्यमनुनासिकादेशो भवति — महाँ असि, महाँ इन्द्रो
    य ओजसा, देवाँ अच्छा दीद्यत्.

    Vedic: the रु is the one 8.3.9 दीर्घादटि समानपादे gives, which is not in this
    family, so the rule is exercised on a रु that some sūtra of 8.3.2's stretch
    has made. The आ is tapara (आत्), long only: आत इति किम्? ये वा वनस्पतीँरनु (a
    ई is left to 8.3.2's option). अटीति किम्? भवांश्चरति (a छव् follows, not an अट्).

    It takes 8.3.2's option away: the नित्य is the point of the sūtra.
    """
    at = S.members("aṬ")
    for ru in v.live:
        if not _prakarana_ru(ru) or ru.through:
            continue
        prev, nxt = v.prev(ru), v.next(ru)
        if prev is None or nxt is None or prev.s != "ā" or prev.seg.nasal:
            continue
        if nxt.s not in at:
            continue
        nasal = _anunasika_of(prev.s)
        if nasal is None:
            continue
        yield Application(
            site=site(prev, ru, nxt), edits=(_nasal_edit(prev, nasal),),
            detail=Detail(
                kind=ADESA, sthanin=prev.s, adesa=nasal,
                nimitta=f"a {{ru}} stands after it and the {{aṭ}} {sk(nxt.s)} "
                        f"after that",
                because=(f"{sk(prev.s)} stands before the {{ru}} and "
                         f"{sk(nxt.s)} — an {{aṭ}} — comes after it, so "
                         f"{sk(prev.s)} is made anunāsika without option: "
                         f"{sk(nasal)}"),
                via=(S.tapara("ā"), _pratyahara("aṬ"),
                     S.antaratama(prev.s, nasal, "the {anunāsika} sounds"))))


@rule("8.3.4", name=_named("8.3.4"), families=("nasal",), consumes=(RU,))
def anunasikat_paro_nusvarah(v: View):
    """
    अनुनासिकं विहाय रोः पूर्वस्मात् परोऽनुस्वारागमः — संस्स्कर्ता, संस्कर्ता, भवांश्छादयति.

    The Kāśikā has to supply a word (अन्यशब्दोऽत्राध्याहर्तव्यः): the sound before
    the रु that was NOT made anunāsika is followed by an anusvāra, an आगम put in
    after it (आगमत्वं परशब्दलभ्यम्, Tattvabodhinī). The anusvāra belongs to the word
    of the sound it stands after, and it is asiddha to 8.3.2 and 8.3.3 — they
    stand before it and never see it.

    Where 8.3.2 has made the sound nasal there is nothing to do; where the
    caller's or the derivation's own anusvāra already stands before the रु the
    āgama is not put in twice.
    """
    for ru in v.live:
        if not _prakarana_ru(ru) or ru.through:
            continue
        prev = v.prev(ru)
        if prev is None or prev.seg.nasal or prev.s == ANUSVARA:
            continue
        yield Application(
            site=site(prev, ru), edits=(insert_after(prev, ANUSVARA),),
            detail=Detail(
                kind=AGAMA_KIND, sthanin=prev.s, adesa=ANUSVARA,
                nimitta="a {ru} stands after a sound that is not anunāsika",
                because=(f"{sk(prev.s)} stands before the {{ru}} and has not "
                         f"been made anunāsika, so an anusvāra {sk(ANUSVARA)} "
                         f"is put in right after it"),
                note="The word 'para' makes the anusvāra an āgama: "
                     + _said("tattvabodhini", "8.3.4",
                             "आगमत्वं च परशब्देनैव लभ्यते")))


# ---------------------------------------------------------------------------
# The anusvāra, and where it is held back — 8.3.23 to 8.3.27, 8.3.33
# ---------------------------------------------------------------------------


def _hal_follows(right: Sight) -> str:
    return f"the {{hal}} {sk(right.s)} follows"


@rule("8.3.23", name=_named("8.3.23"), families=("nasal", "hal"))
def mo_nusvarah(v: View):
    """
    मान्तस्य पदस्यानुस्वारो भवति हलि परतः — हरिं वन्दे, कुण्डं हसति, वनं याति.

    हलीत्येव — त्वमत्र, किमत्र (a vowel follows). पदान्तस्येत्येव — गम्यते, रम्यते
    (the म् is inside the word: the caller writes the two pieces of one pada with
    `~`, and the म् at the end of the first is not pada-final).
    """
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != _M or not v.pada_final(left) or not right.is_consonant:
            continue
        yield Application(
            site=site(left, right), edits=(replace(left, NewSeg(ANUSVARA)),),
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa=ANUSVARA,
                nimitta=_hal_follows(right),
                because=(f"{sk('m')} ends a pada and the {{hal}} {sk(right.s)} "
                         f"follows, so the pada's last sound becomes the "
                         f"anusvāra {sk(ANUSVARA)}"),
                via=(_padasya(), _tadanta(_M), S.alo_antyasya(_M),
                     S.saptami_purva(f"{{hal}} {sk(right.s)}"), _samhita())))


@rule("8.3.24", name=_named("8.3.24"), families=("nasal", "hal"))
def nas_capadantasya_jhali(v: View):
    """
    नकारस्य मकारस्य चापदान्तस्यानुस्वारादेशो भवति झलि परतः — यशांसि, पयांसि,
    आक्रंस्यते, आचिक्रंसते.

    अपदान्तस्येति किम्? राजन् भुङ्क्ष्व. झलीति किम्? रम्यते, गम्यते, मन्यते (a य्
    or a नासिक्य is not a झल्).

    The two pieces of one pada are written with `~` (yaśān~si, ākram~syate):
    the न् or म् at the end of the first is not pada-final. The sounds are those
    the sūtra names — नस्य and, by its च, मस्य.
    """
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s not in (_N, _M) or v.pada_final(left):
            continue
        if not S.is_member(right.s, "jhaL"):
            continue
        yield Application(
            site=site(left, right), edits=(replace(left, NewSeg(ANUSVARA)),),
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa=ANUSVARA,
                nimitta=f"the {{jhal}} {sk(right.s)} follows",
                because=(f"{sk(left.s)} is inside a pada (it does not end one) "
                         f"and the {{jhal}} {sk(right.s)} follows, so it becomes "
                         f"the anusvāra {sk(ANUSVARA)}"),
                via=(S.saptami_purva(f"{{jhal}} {sk(right.s)}"), _samhita())))


_KASIKA_8_3_25 = _said("kashika", "8.3.25",
                       "मकारस्य मकारवचनमनुस्वारनिवृत्त्यर्थम्")


@rule("8.3.25", name=_named("8.3.25"), families=("nasal",),
      overrides=(("8.3.23", _KASIKA_8_3_25),))
def mo_raji_samah_kvau(v: View):
    """
    समो मकारस्य मकार आदेशो भवति राजतौ क्विप्प्रत्ययान्ते परतः — सम्राट्, साम्राज्यम्.

    राजीति किम्? संयत् (the following word is not राज्). सम इति किम्? किंराट् (the
    म् is not सम्'s). क्वाविति किम्? संराजिता (no क्विप्, so the anusvāra stays).
    The word राज् with its क्विप् is not in the letters: the caller writes
    `rāj{dhatu:rāj,kvip}`.

    **This sūtra does nothing to the form.** मकारस्य मकारवचनमनुस्वारनिवृत्त्यर्थम्:
    putting म् for म् is idle except as the way to keep 8.3.23's anusvāra out.
    So it is a refusal, an application with no edit at the very place of 8.3.23,
    and 8.3.23 does not act there again.
    """
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != _M or not v.pada_final(left) or not _ru_word(v, left, "sam"):
            continue
        if (not v.begins_word(right) or _root_of(v, right) != "rāj"
                or not _flag(v, right, "kvip")):
            continue
        yield Application(
            site=site(left, right), edits=(),
            detail=Detail(
                kind=PRATISEDHA, sthanin=left.s, adesa=left.s,
                nimitta="{rāj} with {kvip} follows {sam}",
                because=(f"{sk('m')} ends {sk('sam')} and {sk('rāj')} with "
                         f"{{kvip}} follows, so {sk('m')} is put for {sk('m')}: "
                         f"it stays, and 8.3.23's anusvāra does not come"),
                via=(_padasya(), _samhita())))


def _m_before_ha(v: View):
    """The म् of a pada, the ह् after it and the sound after that — the shape
    8.3.26 and 8.3.27 look for."""
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != _M or not v.pada_final(left) or right.s != _H:
            continue
        after = v.next(right)
        if after is None or not _fresh(left, right, after):
            continue
        yield left, right, after


@rule("8.3.26", name=_named("8.3.26"), families=("nasal",),
      overrides=(("8.3.23", _said(
          "kashika", "8.3.26",
          "हकारे मकारपरे परतो मकारस्य वा मकार आदेशो भवति")),))
def he_mapare_va(v: View):
    """
    हकारे मकारपरे परतो मकारस्य वा मकार आदेशो भवति — किम् ह्मलयति, किं ह्मलयति;
    कथम् ह्मलयति, कथं ह्मलयति.

    Like 8.3.25 this puts म् for म् to keep 8.3.23's anusvāra out, and here as an
    OPTION (वा): the course that declines it is the anusvāra of 8.3.23. The
    commentaries do not say whether this वा is a प्राप्तविभाषा or an
    अप्राप्तविभाषा, and none is claimed.
    """
    for left, right, after in _m_before_ha(v):
        if after.s != _M:
            continue
        yield Application(
            site=site(left, right), edits=(), optional=VA,
            detail=Detail(
                kind=PRATISEDHA, sthanin=left.s, adesa=left.s,
                nimitta=f"{sk('h')} follows, with {sk('m')} after it",
                because=(f"{sk('m')} ends a pada and {sk('h')} follows, itself "
                         f"followed by {sk('m')}, so {sk('m')} may be put for "
                         f"{sk('m')}: it stays and 8.3.23's anusvāra does not "
                         f"come"),
                via=(_padasya(), S.saptami_purva(f"{sk('h')} with "
                                                 f"{sk('m')} after it"),
                     _samhita())))


_YAVALA_VARTTIKA = _varttika("8.3.26", "यवलपरे")


def _yavalah() -> Tuple[str, ...]:
    """
    The vārttika's यवलाः: the semivowels that have a nasal form — रेफवर्जिता
    यवलाः सानुनासिकाः (Kāśikā on 1.1.9). Asked of `grahana.varieties`, which
    reads that, in the order of the śivasūtras.
    """
    return tuple(s for s in resolve("yaṆ").sounds if len(varieties(s)) > 1)


def _yavala_via(sound: str) -> Via:
    lists = ", ".join(_yavalah())
    return Via(
        "1.3.10",
        f"the vārttika names the sounds that may follow the {{h}} ({lists}) and the "
        f"substitutes ({lists}), equal in number, so they correspond in order: "
        f"{sk(sound)} answers to {sk(sound)}")


@rule("8.3.26", name=_named("8.3.26"), families=("nasal",),
      authority=VARTTIKA, varttika=_YAVALA_VARTTIKA,
      overrides=(("8.3.23", _said(
          "kashika", "8.3.26",
          "यवलपरे हकारे मकारस्य यवला यथासंख्यं वा भवन्तीति वक्तव्यम्")),))
def yavalapare_yavala_va(v: View):
    """
    यवलपरे हकारे मकारस्य यवला यथासंख्यं वा भवन्ति — किय् ह्यः, किं ह्यः; किव् ह्वलयति,
    किं ह्वलयति; किल् ह्लादयति, किं ह्लादयति.

    A vārttika, not Pāṇini. The substitute for the म् is the य्, व् or ल् that
    follows the ह् (one to one, 1.3.10), in its nasal form — the form nearest the
    म् (1.1.50), which is the anunāsika य्, व् or ल् the Laghukaumudī prints.
    """
    yavala = _yavalah()
    for left, right, after in _m_before_ha(v):
        if after.s not in yavala:
            continue
        nasal = _anunasika_of(after.s)
        if nasal is None:
            continue
        plain, marks = _split(nasal)
        yield Application(
            site=site(left, right),
            edits=(replace(left, NewSeg(plain, marks)),), optional=VA,
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa=nasal,
                nimitta=f"{sk('h')} follows, with {sk(after.s)} after it",
                because=(f"{sk('m')} ends a pada and {sk('h')} follows, itself "
                         f"followed by {sk(after.s)}, so {sk('m')} may become "
                         f"the nasal {sk(nasal)}, the one that answers to "
                         f"{sk(after.s)}"),
                via=(_padasya(), _yavala_via(after.s),
                     S.antaratama(left.s, nasal, "the {anunāsika} sounds"),
                     _samhita()),
                authority=VARTTIKA, varttika=_YAVALA_VARTTIKA))


@rule("8.3.27", name=_named("8.3.27"), families=("nasal",),
      overrides=(("8.3.23", _said(
          "kashika", "8.3.27",
          "नकारपरे हे परतो मकारस्य वा नकारादेशो भवति")),))
def napare_nah(v: View):
    """
    नकारपरे हे परतो मकारस्य वा नकारादेशो भवति — किन् ह्नुते, किं ह्नुते; कथन् ह्नुते.

    The substitute is the न् the sūtra names twice (नपरे, नः): the sound after the
    ह् and the sound put for the म् are the same न्.
    """
    for left, right, after in _m_before_ha(v):
        if after.s != _N:
            continue
        yield Application(
            site=site(left, right), edits=(replace(left, NewSeg(after.s)),),
            optional=VA,
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa=after.s,
                nimitta=f"{sk('h')} follows, with {sk('n')} after it",
                because=(f"{sk('m')} ends a pada and {sk('h')} follows, itself "
                         f"followed by {sk('n')}, so {sk('m')} may become "
                         f"{sk('n')} — and so has no anusvāra"),
                via=(_padasya(), _samhita())))


@rule("8.3.33", name=_named("8.3.33"), families=("nasal",))
def maya_uno_vo_va(v: View):
    """
    मयः परस्य उञो वा वकारादेशो भवत्यचि परतः — शम्वस्तु वेदिः, तद्वस्य परेतः,
    किम्वावपनम्.

    The उञ् is the particle उ, and only the caller can say that this उ is that
    particle and not a उ of some other word: the piece is written `u{nipata}`.
    A मय् (m, ṅ, ṇ, n, and the stops) must stand right before it and an अच् right
    after. प्रगृह्यत्वादुञः प्रकृतिभावे प्राप्ते वकारो विधीयते: the उञ् is pragṛhya, and
    this sūtra is the reason it does not simply stay.

    **The व् is asiddha to 8.3.23.** With no anusvāra: वत्वस्यासिद्धत्वान्नानुस्वारः.
    The rule that makes the व् stands after 8.3.23, so 8.3.23 still sees the उ.
    """
    may = S.members("maY")
    for u in v.live:
        if u.s != _U or not _flag(v, u, "nipata") or v.word(u).text != _U:
            continue
        prev, nxt = v.prev(u), v.next(u)
        if prev is None or nxt is None or not nxt.is_vowel:
            continue
        if prev.s not in may or not v.pada_final(prev):
            continue
        if not _fresh(prev, u, nxt):
            continue
        yield Application(
            site=site(prev, u, nxt), edits=(replace(u, NewSeg(_V)),),
            optional=VA,
            detail=Detail(
                kind=ADESA, sthanin=u.s, adesa=_V,
                nimitta=f"the {{aC}} {sk(nxt.s)} follows, after a {{maY}}",
                because=(f"the particle {sk('u')} ({{uñ}}) stands after the "
                         f"{{maY}} {sk(prev.s)} and before the {{aC}} "
                         f"{sk(nxt.s)}, so it may become {sk('v')}"),
                via=(S.pancami_para("{maY}"), _pratyahara("maY"), _samhita())))


# ---------------------------------------------------------------------------
# The augments of a pada-final nasal — 8.3.28 to 8.3.32
# ---------------------------------------------------------------------------


def _sutra_words(sutra_id: str) -> List[str]:
    """The words of a sūtra as the corpus has it (IAST)."""
    return sutra_text(sutra_id).split()


@lru_cache(maxsize=1)
def _kuk_tuk() -> Tuple[Tuple[str, str], ...]:
    """
    8.3.28's two lists — the sthānins ङ्, ण् (from ङ्णोः) and the augments कुक्,
    टुक् — and how they go together: 1.3.10, equal in number, so in order. Both
    are read off the sūtra's own text.
    """
    sthanins_word, names_word = _sutra_words("8.3.28")[:2]
    sthanins = [s for s, _ in tokenize(sthanins_word)][:2]
    names = re.findall(r"[^u]+uk", names_word)
    paired = reading.yathasamkhya(sthanins, names)
    assert paired is not None
    return paired


@rule("8.3.28", name=_named("8.3.28"), families=("nasal", "agama"))
def ngnoh_kuktuk_sari(v: View):
    """
    ङकारणकारयोः पदान्तयोः कुक् टुग् इत्येतावागमौ वा भवतः शरि परतः — प्राङ्क् शेते,
    प्राङ् शेते; प्राङ्क् षष्ठः; वण्ट् शेते, वण् शेते.

    The augment is a कित्, so it stands at the END of the ङ् or ण् (पूर्वान्तकरणं
    प्राङ्क् छेते इत्यत्र छत्वार्थम्: it is then the last sound of the pada, as 8.4.63
    needs). कुक्टुकोरसिद्धत्वाज्जश्त्वं न: it is asiddha to 8.2.39 — put in by a later
    rule, it has no past for 8.2.39 to see.

    NOT DONE: प्राङ्ख् षष्ठः needs *चयो द्वितीयाः शरि पौष्करसादेः*, a general opinion the
    corpus files under 8.4.48.
    """
    sar = S.members("śaR")
    pairs = dict(_kuk_tuk())
    lists = (", ".join(p for p, _ in _kuk_tuk()),
             ", ".join(n for _, n in _kuk_tuk()))
    for j in v.junctions():
        left, right = j.left, j.right
        name = pairs.get(left.s)
        if name is None or not v.pada_final(left) or right.s not in sar:
            continue
        if not _fresh(left, right):
            continue
        yield _augment(
            name, left=left, right=right, sthanin=left, optional=VA,
            nimitta=f"the {{śar}} {sk(right.s)} follows",
            because=(f"{sk(left.s)} ends a pada and the {{śar}} {sk(right.s)} "
                     f"follows, so the pada may take {sk(name)}, the augment "
                     f"that answers to {sk(left.s)}"),
            via=(_padasya(), S.yathasamkhya(*lists), _pratyahara("śaR"),
                 _samhita()))


@lru_cache(maxsize=1)
def _dhut() -> str:
    """The augment 8.3.29 names — the last word of the sūtra — धुट्."""
    return _sutra_words("8.3.29")[-1]


def _sa_of_pada(v: View, right: Sight) -> bool:
    """The स् the sūtra means by सि (ḍāt parasya sasya): the first sound of the
    pada after the one that ends in the sthānin."""
    return right.s == "s" and v.begins_word(right)


@rule("8.3.29", name=_named("8.3.29"), families=("nasal", "agama"))
def dah_si_dhut(v: View):
    """
    डकारान्तात् पदादुत्तरस्य सकारादेः पदस्य वा धुडागमो भवति — षट्त्सन्तः, षट् सन्तः;
    श्वलिट्त्साये, श्वलिट् साये.

    परादिकरणं न पदान्ताट्टोरनाम् इति ष्टुत्वप्रतिषेधार्थम्: the augment is a टित्, so it
    stands at the START of the स्, in the second pada — after a pada-final ट-varga
    sound, where 8.4.42 keeps ष्टुत्व away. The ड् is the one 8.2.39 leaves of a
    pada-final ष्; and the augment's later चर्त्व (धकार to त्) is asiddha to this
    rule (Bālamanoramā: चर्त्वस्यासिद्धत्वाड्डात्परत्वात्सस्य धुट्).
    """
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != "ḍ" or not v.pada_final(left) or not _sa_of_pada(v, right):
            continue
        if not _fresh(left, right):
            continue
        yield _augment(
            _dhut(), left=left, right=right, sthanin=right, optional=VA,
            nimitta=f"a pada beginning with {sk('s')} follows",
            because=(f"the pada ends in {sk('ḍ')} and the next begins with "
                     f"{sk('s')}, so that {sk('s')} may take the augment "
                     f"{sk(_dhut())} before it"),
            via=(S.pancami_para(sk("ḍ")), _samhita()))


@rule("8.3.30", name=_named("8.3.30"), families=("nasal", "agama"))
def nas_ca(v: View):
    """
    नकारान्तात् पदादुत्तरस्य सकारस्य वा धुडागमो भवति — भवान्त्साये, भवान् साये;
    सन्त्सः, सन्सः.

    The धुट् is asiddha to 8.3.7 — धुटश्चर्त्वस्य चासिद्धत्वात् नश्छव्यप्रशान् इति रुत्वं न
    भवति — so भवान्त्साये keeps its न् where भवांश्छादयति does not.
    """
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != _N or not v.pada_final(left) or not _sa_of_pada(v, right):
            continue
        if not _fresh(left, right):
            continue
        yield _augment(
            _dhut(), left=left, right=right, sthanin=right, optional=VA,
            nimitta=f"a pada beginning with {sk('s')} follows",
            because=(f"the pada ends in {sk('n')} and the next begins with "
                     f"{sk('s')}, so that {sk('s')} may take the augment "
                     f"{sk(_dhut())} before it"),
            via=(S.pancami_para(sk("n")), _samhita()))


@lru_cache(maxsize=1)
def _tuk() -> str:
    return _sutra_words("8.3.31")[-1]


@rule("8.3.31", name=_named("8.3.31"), families=("nasal", "agama"))
def si_tuk(v: View):
    """
    नकारस्य पदान्तस्य शकारे परतो वा तुगागमो भवति — सञ्छम्भुः, सञ्च्छम्भुः, सञ्च्शम्भुः,
    सञ्शम्भुः.

    The augment is a कित्, so it stands at the END of the pada's न् (पूर्वान्तकरणं
    छत्वार्थम्): the pada then ends in a झय् that 8.4.63 can look back to. The four
    forms need 8.4.40, 8.4.63 and 8.4.65 as well (the hal family), and the तुक्'s
    own जश्त्व does not come (asiddha to 8.2.39).
    """
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != _N or not v.pada_final(left) or right.s != "ś":
            continue
        if not _fresh(left, right):
            continue
        yield _augment(
            _tuk(), left=left, right=right, sthanin=left, optional=VA,
            nimitta=f"{sk('ś')} follows",
            because=(f"{sk('n')} ends a pada and {sk('ś')} follows, so the pada "
                     f"may take the augment {sk(_tuk())} after its {sk('n')}"),
            via=(_padasya(), S.saptami_purva(sk("ś")), _samhita()))


@rule("8.3.32", name=_named("8.3.32"), families=("nasal", "agama"))
def ngamo_hrasvad_aci_ngamun_nityam(v: View):
    """
    ह्रस्वात् परो यो ङम् तदन्तात् पदादुत्तरस्याचो ङमुडागमो भवति नित्यम् — प्रत्यङ्ङास्ते,
    वण्णास्ते, कुर्वन्नास्ते, सुगण्णीशः, सन्नच्युतः.

    ङम इति किम्? त्वमास्से. ह्रस्वादिति किम्? प्राङास्ते, भवानास्ते (a long vowel
    before). अचीति किम्? प्रत्यङ् करोति. The three augments answer to ङ्, ण्, न् one
    to one (1.3.10: ङुट्, णुट्, नुट्) and each is a टित् — at the START of the
    vowel, in the second pada. (The sūtra is written ङमुण् नित्यम्: the ट् of
    ङमुट् has met the न् of नित्यम्; the Bālamanoramā reads it ङमुट् and says
    टकार इत्.)

    परमदण्डिनौ has no augment (Kāśikā: उत्तरपदत्वे चापदादिविधौ प्रत्ययलक्षणप्रतिषेधात्):
    the न् is not a pada's last sound there, and the caller writes the two pieces
    of one pada with `~`, so it is not pada-final for this rule either.
    """
    ngam = resolve("ṅaM").sounds
    paired = reading.yathasamkhya(ngam, ngam)
    listed = ", ".join(ngam)
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s not in ngam or not v.pada_final(left) or not right.is_vowel:
            continue
        prev = v.prev(left)
        if (prev is None or prev.w != left.w or not prev.is_vowel
                or not is_hrasva(prev.s) or not _fresh(prev, left, right)):
            continue
        name = dict(paired)[left.s] + "uṭ"
        yield _augment(
            name, left=left, right=right, sthanin=right, also=(prev,),
            nimitta=f"the vowel {sk(right.s)} begins the next pada",
            because=(f"{sk(left.s)} is a {{ṅam}} ending a pada, after the short "
                     f"vowel {sk(prev.s)}, and the vowel {sk(right.s)} begins "
                     f"the next pada, so {sk(right.s)} takes the augment "
                     f"{sk(name)} before it — always"),
            via=(_padasya(), S.yathasamkhya(listed, listed),
                 _pratyahara("ṅaM"), _samhita()))


# ---------------------------------------------------------------------------
# The nasal a stop takes, and the parasavarṇa of the anusvāra — 8.4.45, 8.4.58–59
# ---------------------------------------------------------------------------


def _nasal_step(left: Sight, right: Sight, sub: str, *, nimitta: str,
                because: str, via: Tuple[Via, ...], optional: str = "",
                authority: str = "sūtra", varttika: str = "") -> Application:
    plain, marks = _split(sub)
    return Application(
        site=site(left, right), edits=(replace(left, NewSeg(plain, marks)),),
        optional=optional,
        detail=Detail(kind=ADESA, sthanin=left.s, adesa=sub, nimitta=nimitta,
                      because=because, via=via, authority=authority,
                      varttika=varttika))


def _would_change(left: Sight, sub: Optional[str]) -> bool:
    """A nasal put where the very nasal stands is no step."""
    if sub is None:
        return False
    plain, marks = _split(sub)
    return plain != left.s or bool(marks) != left.seg.nasal


@rule("8.4.45", name=_named("8.4.45"), families=("nasal", "hal"))
def yaro_nunasike_nunasiko_va(v: View):
    """
    यरः पदान्तस्यानुनासिके परतो वानुनासिक आदेशो भवति — वाङ् नयति, वाग् नयति; श्वलिण् नयति;
    अग्निचिन् नयति; त्रिष्टुम् नयति, त्रिष्टुब् नयति; एतन्मुरारिः, एतद् मुरारिः.

    पदान्तस्येत्येव — वेद्मि, क्षुभ्नाति (inside a word).

    The substitute is chosen by 1.1.50 among the nasal sounds, and must be
    nearest by place AND by effort. That is why रेफ takes nothing (चतुर्मुखः —
    Kaumudī: स्थानप्रयत्नाभ्यामन्तरतमे स्पर्शे चरितार्थो विधिरयं रेफे न प्रवर्तते) and
    neither do श्, ष्, स्: the nasal of their place has another effort. A stop
    takes the fifth of its varga; य्, व्, ल् their own nasal forms.

    `anunāsika` in the right-hand sound is 1.1.8: a nasal stop, or a nasalised
    sound. The anusvāra is not one (Bhāṣya on 1.1.8), so a stop before an anusvāra
    is left alone.
    """
    yar = S.members("yaR")
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s not in yar or not v.pada_final(left):
            continue
        if not is_anunasika(right.sound) or not _fresh(left, right):
            continue
        sub = _nasal_of(left.s)
        if not _would_change(left, sub):
            continue
        yield _nasal_step(
            left, right, sub, optional=VA,
            nimitta=f"the anunāsika {sk(right.sound)} follows",
            because=(f"{sk(left.s)} is a {{yar}} ending a pada and the "
                     f"anunāsika {sk(right.sound)} follows, so it may become "
                     f"the anunāsika {sk(sub)}"),
            via=(_padasya(), _pratyahara("yaR"),
                 S.antaratama(left.s, sub, "the {anunāsika} sounds"),
                 _samhita()))


_NITYAM = _varttika("8.4.45", "प्रत्यये भाषायां नित्यम्")


@rule("8.4.45", name=_named("8.4.45"), families=("nasal", "hal"),
      authority=VARTTIKA, varttika=_NITYAM,
      overrides=(("8.4.45", _said(
          "kashika", "8.4.45",
          "यरोऽनुनासिके प्रत्यये भाषायां नित्यवचनं कर्तव्यम्")),))
def yaro_nunasike_pratyaye_bhasayam_nityam(v: View):
    """
    यरोऽनुनासिके प्रत्यये भाषायां नित्यम् — तन्मात्रम्, चिन्मयम्, वाङ्मयम्, त्वङ्मयम्.

    A vārttika, not Pāṇini, and the Kāśikā adds that व्यवस्थितविभाषाविज्ञानात् सिद्धम्:
    read 8.4.45's option as fixed by its case (always before an affix, in the
    spoken language) and it is not needed. The result is the same.

    Before an affix that begins with a nasal, always, and not in the Veda
    (भाषायाम्). The affix is named by the caller (`maya{pratyaya}`), and the stem
    before it stands as a pada: 1.4.17 स्वादिष्वसर्वनामस्थाने makes it one, and the
    core has no boundary of that name, so the caller writes the junction as a
    pada boundary (`cit maya{pratyaya}`, `vāc-maya{pratyaya}`). Then 8.2.30 and
    8.2.39 see the stem's last sound as pada-final too, and वाक् → वाग् → वाङ् runs
    as in the tradition. The rule does not take a stem written with `~` for a pada:
    that is what the caller said it is not.
    """
    if v.state.veda:
        return
    yar = S.members("yaR")
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s not in yar or not v.pada_final(left):
            continue
        if not v.begins_word(right) or not v.word(right).has("pratyaya"):
            continue
        if not is_anunasika(right.sound) or not _fresh(left, right):
            continue
        sub = _nasal_of(left.s)
        if not _would_change(left, sub):
            continue
        yield _nasal_step(
            left, right, sub, authority=VARTTIKA, varttika=_NITYAM,
            nimitta=f"the affix beginning with {sk(right.sound)} follows",
            because=(f"{sk(left.s)} is a {{yar}} ending the stem and the affix "
                     f"beginning with the anunāsika {sk(right.sound)} follows, "
                     f"in the spoken language, so it becomes the anunāsika "
                     f"{sk(sub)}, without option"),
            via=(Via("1.4.17", "the stem stands before an affix (the caller "
                               "says so) and is a pada, so this {yar} ends "
                               "a pada"),
                 _pratyahara("yaR"),
                 S.antaratama(left.s, sub, "the {anunāsika} sounds"),
                 _samhita()))


def _parasavarna_step(left: Sight, right: Sight, *, optional: str,
                      because: str) -> Optional[Application]:
    sub = _parasavarna(right.s)
    if sub is None:
        return None
    plain, marks = _split(sub)
    via = [S.saptami_purva(f"{{yay}} {sk(right.s)}")]
    if plain != right.s:
        via.append(S.savarna_of(plain, right.s))
    via.append(S.antaratama(left.s, sub, f"the savarṇas of {sk(right.s)}"))
    via.append(_pratyahara("yaY"))
    via.append(_samhita())
    return Application(
        site=site(left, right), edits=(replace(left, NewSeg(plain, marks)),),
        optional=optional,
        detail=Detail(kind=ADESA, sthanin=left.s, adesa=sub,
                      nimitta=f"the {{yay}} {sk(right.s)} follows",
                      because=because.replace("<<sub>>", sk(sub)), via=tuple(via)))


@rule("8.4.58", name=_named("8.4.58"), families=("nasal", "hal"))
def anusvarasya_yayi_parasavarnah(v: View):
    """
    अनुस्वारस्य ययि परतः परसवर्ण आदेशो भवति — शङ्किता, उञ्छिता, कुण्डिता, नन्दिता, कम्पिता,
    कुर्वन्ति, कृषन्ति.

    ययीति किम्? आक्रंस्यते (a स् is not a यय्). The Kāśikā's examples are all of an
    anusvāra INSIDE a word, and 8.4.59 makes the pada-final one optional (Nyāsa on
    8.4.59: वावचनं पूर्वस्य नित्यत्वज्ञापनार्थम्), so this is read of an anusvāra that
    does not end a pada.

    The substitute is the savarṇa of the following sound that is nearest the
    anusvāra, which is a nasal one; where the sound has none (र्, the ūṣmans) there
    is none and the anusvāra stays (`_parasavarna`).

    **कुर्वन्ति.** 8.3.24 makes the न् an anusvāra, and 8.4.58 makes that a न् again.
    The न् 8.4.58 makes is asiddha to 8.4.2 (so no ण) and to 8.3.24 (so no
    anusvāra once more): the View shows both of them the anusvāra.
    """
    yay = S.members("yaY")
    for j in v.pairs():
        left, right = j.left, j.right
        if left.s != ANUSVARA or v.pada_final(left) or right.s not in yay:
            continue
        step = _parasavarna_step(
            left, right, optional="",
            because=(f"the anusvāra does not end a pada and the {{yay}} "
                     f"{sk(right.s)} follows, so it becomes the savarṇa of "
                     f"{sk(right.s)} that is nearest to it: <<sub>>"))
        if step is not None:
            yield step


@rule("8.4.59", name=_named("8.4.59"), families=("nasal", "hal"))
def va_padantasya(v: View):
    """
    पदान्तस्यानुस्वारस्य ययि परतो वा परसवर्णादेशो भवति — त्वङ्करोषि, त्वं करोषि; सय्ँयन्ता,
    संयन्ता; सव्ँवत्सरः, संवत्सरः; यल्ँलोकम्, यंलोकम्.

    The anusvāra is the pada's last sound, whether 8.3.23 made it or the caller
    wrote it. The option is 8.4.59's own word वा.
    """
    yay = S.members("yaY")
    for j in v.junctions():
        left, right = j.left, j.right
        if left.s != ANUSVARA or not v.pada_final(left) or right.s not in yay:
            continue
        if not _fresh(left, right):
            continue
        step = _parasavarna_step(
            left, right, optional=VA,
            because=(f"the anusvāra ends a pada and the {{yay}} {sk(right.s)} "
                     f"follows, so it may become the savarṇa of {sk(right.s)} "
                     f"that is nearest to it: <<sub>>"))
        if step is not None:
            yield step


_EVERY_RULE = (
    matuvaso_ru_sambuddhau_chandasi, atra_anunasikah_purvasya_tu_va,
    ato_ati_nityam, anunasikat_paro_nusvarah, samah_suti,
    sampumkanam_so_vaktavyah, pumah_khayy_ampare, nas_chavy_aprasan,
    mo_nusvarah, nas_capadantasya_jhali, mo_raji_samah_kvau, he_mapare_va,
    yavalapare_yavala_va, napare_nah, ngnoh_kuktuk_sari, dah_si_dhut,
    nas_ca, si_tuk, ngamo_hrasvad_aci_ngamun_nityam, maya_uno_vo_va,
    yaro_nunasike_nunasiko_va, yaro_nunasike_pratyaye_bhasayam_nityam,
    anusvarasya_yayi_parasavarnah, va_padantasya)

#: Who else states what only one family may — 8.3.33, and each vārttika here —
#: and if someone does, this family does not. *संपुंकानां सो वक्तव्यः* is stated
#: on the visarga (the Laghusiddhāntakaumudī prints it after 8.3.15), which is
#: the visarga family's stage: where that family has it, its course is taken.
_SAMPUMKA_OPENING = "संपुंकानां सो वक्तव्यः"
_ELSEWHERE = {
    (r.sutra, r.varttika): (
        _elsewhere(r.sutra, _SAMPUMKA_OPENING, anywhere=True)
        if _SAMPUMKA_OPENING in r.varttika
        else _elsewhere(r.sutra, r.varttika))
    for r in _EVERY_RULE if r.sutra == "8.3.33" or r.varttika}
_MAYA_ELSEWHERE = _ELSEWHERE[("8.3.33", "")]

RULES = tuple(r for r in _EVERY_RULE
              if not _ELSEWHERE.get((r.sutra, r.varttika)))


def _with_vartika(text: str, sutra: str, varttika: str) -> str:
    """A COVERAGE note that names a vārttika only if this family states it."""
    other = _ELSEWHERE.get((sutra, varttika))
    return (text if not other else
            f"the vārttika is the {other} family's, which states it itself")


#: Which sūtras of this family's scope the module implements — the honest
#: account, kept beside the code. See `rulebook.COVERAGE_STATUS`.
COVERAGE = (
    ("8.3.1", "vedic", "the ru only; its two vārttikas (vana upasaṅkhyānam, "
                       "bhavadbhagavadaghavatām ot ca avasya) are Vedic lexical "
                       "lists and are not done"),
    ("8.3.2", "rule", ""),
    ("8.3.3", "vedic", "exercised on any ru of 8.3.2's stretch; the ru of 8.3.9, "
                       "which this family does not make, is what the Kāśikā's "
                       "examples use"),
    ("8.3.4", "rule", ""),
    ("8.3.5", "rule", _with_vartika(
        "with the vārttika saṃpuṃkānāṃ so vaktavyaḥ (the ru is s); its second "
        "half, samo vā lopam eke, is another opinion and is not done",
        "8.3.5", _SAMPUMKA)),
    ("8.3.6", "partial", "the vārttika khyāñādeśe na (puṃkhyānam) turns on a y "
                         "that a later tripādī rule makes out of ś, which the "
                         "engine is given as letters"),
    ("8.3.7", "rule", ""),
    ("8.3.23", "rule", ""),
    ("8.3.24", "rule", ""),
    ("8.3.25", "rule", ""),
    ("8.3.26", "rule", _with_vartika(
        "with the vārttika yavalapare yavalā vā", "8.3.26", _YAVALA_VARTTIKA)),
    ("8.3.27", "rule", ""),
    ("8.3.28", "partial", "prāṅkh ṣaṣṭhaḥ needs Pauṣkarasādi's cayo dvitīyāḥ "
                          "śari, a general opinion the corpus files under 8.4.48"),
    ("8.3.29", "rule", ""),
    ("8.3.30", "rule", ""),
    ("8.3.31", "rule", ""),
    ("8.3.32", "rule", ""),
    (("8.3.33", "scope",
      f"the {_MAYA_ELSEWHERE} family defines 8.3.33 (it is the exception to "
      f"6.1.125 and displaces the vowel rules at that place), so this family "
      f"stands aside")
     if _MAYA_ELSEWHERE else ("8.3.33", "rule", "")),
    ("8.4.45", "partial", "with the vārttika pratyaye bhāṣāyāṃ nityam; the stem "
                          "before an affix is a pada by 1.4.17 and the core has no "
                          "boundary for that, so the vārttika is written for a "
                          "stem the caller gives as a pada boundary and an affix "
                          "flagged pratyaya"),
    ("8.4.58", "rule", ""),
    ("8.4.59", "rule", ""),
    ("1.1.46", "support", ""),
    ("1.1.47", "scope", "no augment of this family is a mit: adesa.agama_site is "
                        "asked for the place and would return AFTER_LAST_VOWEL "
                        "for one"),
)
