# -*- coding: utf-8 -*-
"""
प्रकृतिभाव — the vowels that refuse sandhi, and the sounds that go with them.
1.1.11–19, 1.4.56–60, 6.1.115–131, 8.2.82–107, 8.3.33, 8.4.57.

**One idea, said many ways: nothing happens.** From 6.1.72 every rule says what
a junction DOES. These say where it does not: *प्रकृतिरिति स्वभावः* — the sounds
stand in their own nature (Kāśikā on 6.1.115). The engine's way of saying it is
the mark `PRAKRTYA` on the vowel (`remark`), which `View.vowel_pairs` then
leaves out, so that every rule of vowel sandhi — 6.1.77 yaṇ, 6.1.78, 6.1.87,
6.1.101, 6.1.109 — finds nothing to do. The rule that puts the mark must win
against all of them at the very place it stands, and it says so
(`overrides=(("@ac", …),)`).

**6.1.125 प्लुतप्रगृह्या अचि नित्यम् is the centre.** It asks two questions and
answers neither itself. *Is the vowel pragṛhya?* is
`src/astadhyayi/pragrhya.py`'s (1.1.11–1.1.19), called with what the word's
flags say — a dual, a particle, an aḍas, a vocative — because no reading of the
letters settles them (NORTH_STAR §5). *Is it pluta?* is the flag `pluta`, the
caller's word for what 8.2.82–107 made (see COVERAGE). Whichever sūtra
gives the name is cited in the step.

**Flags this family reads** (the closed vocabulary of the README, plus what the
Vedic rules and the go-rules need; each is the caller's statement, never a guess):

    dvivacana  saptamyartha  sambuddhi  adas  nipata  ang  arsa  pluta
    stem:X     she           antahpada   yajus anudatta  vatayana  sakalya
    anunasika

`arsa` — the इति belongs to the ṛṣi's own text and not to the padakāra's (the
*अनार्ष* of 1.1.16, 6.1.129; a Vedic passage is not thereby ārṣa); `she` — the
final e is the Vedic sup-substitute शे (1.1.13); `antahpada` — this
word and the next stand in one pāda of an Ṛk verse (6.1.115); `yajus` — the
passage is Yajurvedic (6.1.117–121); `anudatta` — the first vowel of this word
is anudātta (6.1.120–121); `vatayana` — the compound go-akṣa means a window
(6.1.123); `sakalya` — the caller follows Śākalya's recitation (6.1.127–128);
`anunasika` — the nasal option of 8.4.57 is asked for this word's final vowel.

**Decisions that cost failures, so they are stated.**

* *The junction to the LEFT of a pragṛhya vowel is settled first.* 6.1.125 keeps
  a pragṛhya vowel from changing **when a vowel follows it**; it says nothing of
  a vowel before it, and the Kāśikā's own counter-example shows sandhi there
  still happens: *जानु उ अस्य रुजति* — the second उ is pragṛhya, yet the first
  उ joins it (6.1.101). So a prakṛtibhāva rule waits while a vowel stands
  immediately before its vowel and a rule of sandhi could still join them
  (`_pending`). Without this a one-vowel particle between two words —
  *sa a{nipata} i* — would win, at 6.1.125's place, the very sound the
  junction before it also reaches, and that junction would never be done.
* *A sound this derivation has made is not pragṛhya.* The ekādeśa of
  उ + उ is an ऊ that no one named. The Kāśikā's result is *जान्वस्य रुजति*
  — the ऊ goes on to yaṇ. (The Tattvabodhinī also allows *जानू अस्य*, by
  6.1.85 making the substitute the particle: OPEN, see the note at 6.1.125.)
* *The prakṛtibhāva rules of Śākalya are offered on request.* 6.1.127 and
  6.1.128 make *दधि अत्र* an alternative to *दध्यत्र* for every speaker. The
  engine returns the option-taken course first and README, tests and callers
  expect `iti ādi` → *ityādi*; a rule that offered its option to every ik before
  an unlike vowel would turn the first form of every such junction into *iti
  ādi*. The caller who wants Śākalya's alternative says `{sakalya}`.
* *Rules that only take a name away or set a fiction (6.1.129, 6.1.130) mark the
  vowel and step aside.* They are steps of their own (so the trace can cite
  them) that change no sound; they displace the rules of sandhi for one
  turn only, and those act on the next.

**Sūtras the tradition itself argues about, and what was taken.** Where the
Kāśikā and the Kaumudī share a reading it is implemented; the rest is in an
OPEN note next to the rule and in the report's `open_questions`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, List, Optional, Sequence, Tuple

from src.astadhyayi.adesa import hrasva_of
from src.astadhyayi.pragrhya import Pragrhya
from src.astadhyayi.pragrhya import pragrhya as _pragrhya
from src.astadhyayi.prakrtibhava import AVYADI, YAJUSI_WORDS, stands_open
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi.infer import nipata_source
from src.astadhyayi.sandhi.rule import (
    ADESA, PRAKRTIBHAVA, PRATISEDHA, Application, Detail, NewSeg, Via,
    remark, replace, rule, sk, site)
from src.astadhyayi.sandhi.parse import tokenize
from src.astadhyayi.sandhi.segs import (
    ANGA, ANUNASIKA, HAL, PADA, PLUTA, PRAKRTYA, SAMASA, Junction, Sight,
    View)
from src.astadhyayi.sup import SUP, SUT
from src.astadhyayi.varna import ANUNASIKA_MARK, VARGA, VISARGA, savarna


# ---------------------------------------------------------------------------
# What the tradition says, quoted — and checkable
# ---------------------------------------------------------------------------

_WORKS = {
    "kashika": "Kāśikā", "kaumudi": "Siddhāntakaumudī",
    "balamanorama": "Bālamanoramā", "tattvabodhini": "Tattvabodhinī",
    "bhashya": "Mahābhāṣya",
}

#: Every quotation this module makes, as (sūtra, work, words). A test reads each
#: from the corpus (`corpus.commentary_on`) and fails if one is not there — the
#: reasons the rules give are the tradition's own words or they are not given.
QUOTED: List[Tuple[str, str, str]] = []


def _q(sutra: str, work: str, quote: str) -> str:
    """A verbatim quotation, registered for the test that checks it."""
    QUOTED.append((sutra, work, quote))
    return f"{quote} ({_WORKS[work]} on {sutra})"


# ---------------------------------------------------------------------------
# Words of the tradition the rules quote — the sūtras' own letters
# ---------------------------------------------------------------------------

#: Options, each under the sūtra's own word for it.
_SAKALYA = "शाकल्यस्य"
_CAKRAVARMANA = "चाक्रवर्मणस्य"
_SPHOTAYANA = "स्फोटायनस्य"
_VIBHASA = "विभाषा"
_VA = "वा"

#: 6.1.115's अव्यपरे: no व् or य् after the अ. The Kāśikā spells the two letters
#: out — अवकारयकारपरेऽति (checked by the tests).
_VA_YA = ("v", "y")

#: 1.4.18 यचि भम् — before an affix beginning with य् or a vowel the stem is
#: भ, not पद; the sūtra's own letter.
_YA = "y"

#: A mark for the vowel that a later rule has told to be taken as short: the
#: pluta of 6.1.129–130 that 6.1.125 no longer sees as pluta.
APLUTAVAT = "aplutavat"


# ---------------------------------------------------------------------------
# Reading the junctions
# ---------------------------------------------------------------------------


def _input_sound(seg) -> bool:
    """
    A sound of the input, though a mark-only rule (6.1.125, 6.1.129–130) may
    have re-made it: what such a rule leaves is the same sound with one more
    mark, and it is not a sound this derivation has *made*.
    """
    while seg.made_by:
        if len(seg.prior) != 1:
            return False
        older = seg.prior[0]
        if (older.s, older.w, older.lw) != (seg.s, seg.w, seg.lw):
            return False
        seg = older
    return True


def _pairs(v: View, kinds: Sequence[str] = (PADA,)
           ) -> Iterator[Tuple[Junction, List[Junction]]]:
    """
    Every two vowels across a boundary of one of `kinds`, whose first sound is
    a sound of the input and is not waiting for a junction on its left.

    Yielded with the whole list of vowel pairs, which is what `_pending` asks.
    """
    pairs = v.vowel_pairs()
    for j in pairs:
        if not j.between_words or j.kind not in kinds:
            continue
        if not _input_sound(j.left.seg):
            continue
        if _pending(v, j.left, pairs):
            continue
        yield j, pairs


def _pending(v: View, left: Sight, pairs: Sequence[Junction]) -> bool:
    """
    A vowel stands just before `left` and a rule of sandhi may still join them.

    See the module docstring: the sandhi to the left of a pragṛhya vowel is not
    what 6.1.125 forbids, and it is done first.
    """
    before = v.prev(left)
    return before is not None and any(
        p.left.uid == before.uid and p.right.uid == left.uid for p in pairs)


def _holds(sutra: str, **question) -> bool:
    """
    Ask the project's own codification of 6.1.115–134 (`prakrtibhava.stands_open`)
    whether `sutra` is the one that holds this junction open. A notion another
    module already decides is asked, not redecided.
    """
    return stands_open(**question).sutra == sutra


def _flag(v: View, sight: Sight, name: str) -> bool:
    return name in v.flags(sight)


def _asked(v: View, *names: str) -> bool:
    """Some word of the input carries one of these flags. Every rule of this
    family rests on what a flag says, so a form with none is passed over at
    once — the engine asks each rule, and a rule that has nothing to look at
    should not make it wait."""
    return any(f in w.flags for w in v.state.words for f in names)


def _named(v: View, *texts: str) -> bool:
    return any(w.text in texts for w in v.state.words)


def _pluta_present(v: View) -> bool:
    """A pluta the caller flagged, or one a rule of 8.2.82–107 has marked."""
    return _asked(v, "pluta") or any(PLUTA in s.marks for s in v.state.segs)


def _is_un(word) -> bool:
    """The word is the particle उञ् — the letter उ, said to be a particle
    (`nipata`, or `stem:uñ`): the letters alone do not say it."""
    return word.text == "u" and ("nipata" in word.flags
                                 or word.flag_value("stem") == "uñ")


# ---------------------------------------------------------------------------
# Why a vowel stays: the two grounds of 6.1.125
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class _Ground:
    kind: str                       # "pragṛhya" | "pluta"
    sutra: str                      # the sūtra that gives the name
    because: str
    via: Tuple[Via, ...]
    optional: str = ""


_R116_KIND = _q("1.1.16", "balamanorama", "निपातत्वाऽभावादप्राप्ते विभाषेयम्")


def _nipata_via(v: View, sight: Sight) -> Via:
    """Why the word is a nipāta: the gaṇa that holds it, else the caller."""
    word = v.word(sight)
    if "nipata" in dict(word.inferred):
        return Via(nipata_source(word.text) or "1.4.56",
                   f"{sk(word.text)} is in this gaṇa, so it is a {{nipāta}} "
                   f"(inferred, and shown as an assumption in the trace)")
    return Via("1.4.56",
               f"the caller gives {sk(word.text)} as a {{nipāta}}; 1.4.56 "
               f"names every particle of the following lists so")


def _pragrhya_ground(v: View, left: Sight, right: Sight
                     ) -> Optional[_Ground]:
    """
    `pragrhya.pragrhya` asked with what the word's flags say.

    1.1.12 wants the vowel after the म् of अदस्, so the sound before it is
    looked at, not only the flag. 1.1.17 is *later and more specific* than
    1.1.14 for उञ् before इति and makes the name optional there (Śākalya), which
    is what gives the three forms *उ इति, वि इति, ऊँ इति* the Bālamanoramā
    counts on 1.1.17–18: so 1.1.14 is not offered for that word.
    """
    word = v.word(left)
    flags = word.flags
    nxt = v.word(right)
    before = v.prev(left)
    after_m = before is not None and before.w == left.w and before.s == "m"
    stem_flag = word.flag_value("stem") or ""
    adas = ("adas" in flags or stem_flag == "adas") and after_m
    before_iti = nxt.text == "iti" and v.begins_word(right)
    arsa = "arsa" in flags or "arsa" in nxt.flags
    nipata = "nipata" in flags or _is_un(word)      # उञ् is a particle
    un_before_iti = _is_un(word) and before_iti and not arsa
    stem = "adas" if adas else ("" if stem_flag == "adas" else stem_flag)
    got: Optional[Pragrhya] = _pragrhya(
        "śe" if "she" in flags else word.text,
        dvivacana="dvivacana" in flags and not adas,
        nipata=nipata and not un_before_iti,
        ang="ang" in flags,
        sambuddhi="sambuddhi" in flags,
        # 1.1.17 is for the particle उञ्, not for a letter उ that stands for
        # something else
        before_iti=before_iti and (word.text != "u" or _is_un(word)),
        arsa=arsa,
        saptami_artha="saptamyartha" in flags,
        stem=stem)
    if got is None:
        return None
    name = sk(word.text)
    vowel = sk(left.s)
    roles = {
        "1.1.11": f"{name} is a dual ({{dvivacana}}, as the caller says) and "
                  f"ends in the long {vowel}, so the whole word is named "
                  f"{{pragṛhya}}",
        "1.1.12": f"{vowel} stands after the {sk('m')} of {{adas}}, so it is "
                  f"named {{pragṛhya}} whether or not it is a dual",
        "1.1.13": f"the final {sk('e')} of {name} is the Vedic substitute "
                  f"{sk('śe')}, which is named {{pragṛhya}}",
        "1.1.14": f"{name} is a particle of one vowel and is not the preverb "
                  f"{{āṅ}}, so it is named {{pragṛhya}}",
        "1.1.15": f"{name} is a particle ending in {sk('o')}, so it is named "
                  f"{{pragṛhya}}",
        "1.1.16": f"the {sk('o')} of {name} comes from the vocative ending and "
                  f"{sk('iti')} follows in a non-Vedic text; Śākalya makes the "
                  f"name optional — an {{aprāpta}}-vibhāṣā, " + _R116_KIND,
        "1.1.17": f"{name} is the particle {{uñ}} before {sk('iti')}, and "
                  f"1.1.17, later and more specific than 1.1.14, makes its "
                  f"name optional (Śākalya)",
        "1.1.19": f"{vowel} of {name} stands for the meaning of a locative "
                  f"({{saptamyartha}}, as the caller says), so it is named "
                  f"{{pragṛhya}}",
    }
    via: List[Via] = [Via(got.by, roles.get(got.by, name))]
    if got.by in ("1.1.14", "1.1.15"):
        via.insert(0, _nipata_via(v, left))
    return _Ground(
        "pragṛhya", got.by,
        f"the word {name} bears the name {{pragṛhya}} by {got.by}",
        tuple(via), _SAKALYA if got.optional else "")


def _is_pluta(v: View, sight: Sight) -> bool:
    """
    The vowel is pluta: the caller's flag on the word, or the mark a rule of
    8.2.82–107 would leave. Not if 6.1.129–130 have set it aside.
    """
    if APLUTAVAT in sight.marks:
        return False
    return PLUTA in sight.marks or (_flag(v, sight, "pluta")
                                    and v.ends_word(sight))


def _pluta_ground(v: View, left: Sight) -> Optional[_Ground]:
    if not _is_pluta(v, left):
        return None
    word = v.word(left)
    return _Ground(
        "pluta", "1.2.27",
        f"the vowel {sk(left.s)} is pluta",
        (Via("1.2.27",
             f"{sk(left.s)} is of three mātrās, a {{pluta}} — the caller says "
             f"the last vowel of {sk(word.text)} is one ({{pluta}}), as "
             f"8.2.82–107 make it. Those rules stand in the tripādī and 8.2.1 "
             f"would hide their work; 6.1.125's own wording names the pluta, "
             f"so it may see it (plutamanūdya prakṛtibhāvavidhānasāmarthyāt)"),
         ),
        "")


# ---------------------------------------------------------------------------
# 6.1.125 — the centre
# ---------------------------------------------------------------------------

_R125_AC = _q("6.1.125", "kashika", "प्लुताश्च प्रगृह्याश्चाचि प्रकृत्या भवन्ति")
_R125_NITYA = _q("6.1.125", "kashika",
                 "प्लुतप्रगृह्याणां नित्यमयमेव प्रकृतिभावो यथा स्याद्")


def _keep(left: Sight, right: Sight, because: str, via: Sequence[Via],
          *, nimitta: Optional[str] = None) -> Detail:
    return Detail(
        kind=PRAKRTIBHAVA, sthanin=left.s, adesa="",
        nimitta=nimitta or f"the vowel {sk(right.s)} follows",
        because=because, via=tuple(via))


@rule("6.1.125", name="प्लुतप्रगृह्या अचि नित्यम्",
      families=("ac", "prakrtibhava"),
      overrides=(("6.1.127", _R125_NITYA), ("6.1.128", _R125_AC),
                 ("@ac", _R125_AC)),
      consumes=(PLUTA,))
def plutapragrhya_aci_nityam(v: View):
    """
    प्लुताः प्रगृह्याश्च वक्ष्यन्ते तेऽचि परे नित्यं प्रकृत्या स्युः — *हरी एतौ,
    विष्णू इमौ, गङ्गे अमू, अमी ईशाः, अहो ईशाः, इ इन्द्रः*; *एहि कृष्ण 3 अत्र*
    (Kaumudī).

    The vowel is kept: no rule of अच्-sandhi may change it (`overrides` '@ac'),
    and `नित्यम्` puts it ahead of Śākalya's 6.1.127–128 as well (the Kāśikā:
    "so that this prakṛtibhāva alone is done, and 6.1.127's is not").

    **Two grounds, one rule.** *Pragṛhya* is asked of
    `pragrhya.pragrhya` and the sūtra it returns (1.1.11–19) is cited; *pluta*
    is the flag `pluta`. Both are read from the word of the vowel; neither is
    read from its letters.

    **The second अचि.** The Kāśikā: पुनरज्ग्रहणमादेशनिमित्तस्याचः परिग्रहार्थम् —
    the vowel that follows must be the one that would *cause* a change of the
    pragṛhya vowel. It is what the engine asks: the next vowel is the nimitta of
    every rule here (yaṇ, ayādi, guṇa). The vowel BEFORE a pragṛhya one is a
    different pair, and is settled by the rules of sandhi first (`_pending`).

    OPEN. (1) The Tattvabodhinī reads *जानु उ अस्य रुजति* as also giving
    *जानू अस्य* — the ekādeśa ऊ counting as the particle by 6.1.85 and so
    staying — beside *जान्वस्य*. The Kāśikā gives only *जान्वस्य*; that is what
    is derived: a sound this derivation has made is not pragṛhya. (2) Sandhi
    with a vowel before a one-vowel particle is done first, as said above.
    """
    if not (any(w.flags for w in v.state.words) or _pluta_present(v)):
        return
    if not _holds("6.1.125", after="pluta-pragṛhya", before="ac"):
        return
    for j, _pairs_all in _pairs(v):
        left, right = j.left, j.right
        grounds = [g for g in (_pluta_ground(v, left),
                               _pragrhya_ground(v, left, right)) if g]
        if not grounds:
            continue
        word = v.word(left)
        optional = "" if any(not g.optional for g in grounds) \
            else grounds[0].optional
        subject = (f"{sk(word.text)}: " if word.text == left.s
                   else f"{sk(left.s)} ends {sk(word.text)}: ")
        because = (
            subject + " and ".join(g.because for g in grounds)
            + f"; the vowel {sk(right.s)} follows, so it stays as it is "
              f"({{prakṛtyā}}) and no rule of vowel sandhi may change it "
              f"(nityam)")
        yield Application(
            site=site(left, right), edits=(remark(left, PRAKRTYA),),
            optional=optional,
            detail=_keep(left, right, because,
                         tuple(via for g in grounds for via in g.via)))


# ---------------------------------------------------------------------------
# 6.1.129, 6.1.130 — the pluta that is taken as short
# ---------------------------------------------------------------------------

_R129 = _q("6.1.129", "kashika", "प्लुतकार्यं प्रकृतिभावं न करोति")
_R130 = _q("6.1.130", "kashika",
           "चाक्रवर्मणग्रहणं विकल्पार्थम्, तदुपस्थिते निवृत्त्यर्थम् "
           "अनुपस्थिते प्राप्त्यर्थमित्युभयत्रविभाषेयम्")
_STEP_ASIDE = ("; it takes the pluta's effect away and nothing else, so the "
               "rules it stands before act on the very next step")


def _upasthita(v: View, left: Sight, right: Sight) -> bool:
    """
    उपस्थित / अनार्ष: the इति a later analyst (the padakāra) puts after a word,
    and not one that belongs to the ṛṣi's own text (`arsa`). A Vedic passage
    is not thereby ārṣa: सुश्लोक३ इति is Taittirīya's padapāṭha, and वायो इति
    (ऋ० ४.४६.१) the Kāśikā's own instance of 1.1.16.
    """
    nxt = v.word(right)
    return (nxt.text == "iti" and v.begins_word(right)
            and not ("arsa" in nxt.flags or "arsa" in v.flags(left)))


@rule("6.1.129", name="अप्लुतवदुपस्थिते", families=("prakrtibhava",),
      overrides=(("6.1.125", _R129 + _STEP_ASIDE),
                 ("@ac", _R129 + _STEP_ASIDE)),
      consumes=(PLUTA,))
def aplutavad_upasthite(v: View):
    """
    उपस्थितोऽनार्ष इति शब्दः तस्मिन्परे प्लुतोऽप्लुतवद्भवति (Kaumudī) — *सुश्लोक३
    इति* is *सुश्लोकेति*;
    *सुमङ्गल३ इति* is *सुमङ्गलेति*. The pluta before an अनार्ष *इति* counts as short
    for prakṛtibhāva: प्लुतकार्यं प्रकृतिभावं न करोति. It is *वत्* and not
    'is short', so a vowel that is pluta AND pragṛhya keeps its length and its
    name: *अग्नी३ इति* (Kāśikā: प्लुतस्य श्रवणं न स्यात्).

    A pluta ई that is not also pragṛhya is left to 6.1.130, which makes this
    optional for it (*तदुपस्थिते निवृत्त्यर्थम्*). One that IS pragṛhya
    (*अग्नी३ इति*, the Kāśikā's own instance) is kept by its name whichever
    way the option goes, so the option is idle and this sūtra applies.
    """
    if not _pluta_present(v) or not _holds(
            "6.1.129", after="pluta", before="upasthita"):
        return
    for j, _ in _pairs(v):
        left, right = j.left, j.right
        if not _is_pluta(v, left) or not _upasthita(v, left, right):
            continue
        if savarna(left.s, "i") and _pragrhya_ground(v, left, right) is None:
            continue                      # an ī3 that is not pragṛhya: 6.1.130
        yield Application(
            site=site(left, right), edits=(remark(left, APLUTAVAT),),
            detail=Detail(
                kind=PRATISEDHA, sthanin=left.s, adesa="",
                nimitta=f"the quotation particle {sk('iti')} follows",
                because=(f"{sk(left.s)} is pluta and {sk('iti')}, added by a "
                         f"later analyst (upasthita), follows, so the pluta "
                         f"is taken as short for the prakṛtibhāva that "
                         f"6.1.125 would give a pluta"),
                via=(Via("6.1.125",
                         "the prakṛtibhāva a pluta vowel has — it is what "
                         "the fiction takes away; a vowel that is also "
                         "pragṛhya keeps its own"),)))


@rule("6.1.130", name="ई३ चाक्रवर्मणस्य", families=("prakrtibhava",),
      overrides=(("6.1.125", _R130 + _STEP_ASIDE),
                 ("@ac", _R130 + _STEP_ASIDE)),
      consumes=(PLUTA,))
def i3_cakravarmanasya(v: View):
    """
    ई3 प्लुतोऽचि परेऽप्लुतवद्वा स्यात् (Kaumudī) — *चिनु हीदम्* beside *चिनु ही३ इदम्*,
    *हीत्यब्रूताम्* beside *ही३ इत्यब्रूताम्*. The name of Cākravarmaṇa is what
    MAKES it a choice (चाक्रवर्मणग्रहणं विकल्पार्थम्), and it is an
    उभयत्रविभाषा: before *iti* it loosens the fixed fiction of 6.1.129
    (a prāpta-vibhāṣā), elsewhere it supplies one (an aprāpta-vibhāṣā).

    The ई is the pluta of the इ-varṇa (*हि३*, *ही३*), whichever length is
    written. OPEN: the Kāśikā adds *ईकारादन्यत्राप्ययमप्लुतवद्भाव इष्यते — वशा३
    इयं वशेयम्*, an option for a pluta of any vowel before a vowel other than
    *iti*. That is the vṛtti's own extension beyond the sūtra and the Kaumudī
    does not share it; it is not derived, for it would put an option ahead of
    6.1.125 at every pluta junction and the first course of *कृष्ण३ अत्र* would
    no longer be the Laghukaumudī's *कृष्ण३ अत्र*.
    """
    if not _pluta_present(v) or not _holds(
            "6.1.130", after="ī3", before="ac", teacher="Cākravarmaṇa"):
        return
    for j, _ in _pairs(v):
        left, right = j.left, j.right
        if not _is_pluta(v, left) or not savarna(left.s, "i"):
            continue
        if _pragrhya_ground(v, left, right) is not None:
            continue                      # kept by its name either way
        upasthita = _upasthita(v, left, right)
        yield Application(
            site=site(left, right), edits=(remark(left, APLUTAVAT),),
            optional=_CAKRAVARMANA,
            detail=Detail(
                kind=PRATISEDHA, sthanin=left.s, adesa="",
                nimitta=f"the vowel {sk(right.s)} follows",
                because=(f"{sk(left.s)} is pluta and a vowel follows; in "
                         f"Cākravarmaṇa's opinion it may be taken as short "
                         f"({{aplutavat}}), in which case 6.1.125 does not "
                         f"keep it for being pluta"
                         + (" — before iti this loosens the fixed 6.1.129"
                            if upasthita else "")),
                via=(Via("6.1.129",
                         "the fiction of 'as if not pluta' that this "
                         "sūtra extends — and, before iti, makes optional"),)))


# ---------------------------------------------------------------------------
# 1.1.18 — ऊँ for उञ् before इति
# ---------------------------------------------------------------------------

_R118 = _q("1.1.18", "kashika",
           "शाकल्यस्य ग्रहणं विभाषार्थमिहाप्यनुवर्तते, तेन त्रीणि रूपाणि भवन्ति")


def _un_before_iti(v: View, left: Sight, right: Sight) -> bool:
    """The particle उञ् (the letter उ, flagged a particle) before a
    non-Vedic इति."""
    return _is_un(v.word(left)) and _upasthita(v, left, right)


@rule("1.1.18", name="ऊँ", families=("prakrtibhava",),
      overrides=(("6.1.125", _R118), ("@ac", _R118)))
def um_nasal(v: View):
    """
    उञ इतौ दीर्घोऽनुनासिकः प्रगृह्यश्च ऊँ इत्ययमादेशो वा स्यात् (Kaumudī) — *उ
    इति, वि इति, ऊँ इति*: three
    forms, the Kāśikā's त्रीणि रूपाणि. The ऊँ is long, nasal, and pragṛhya by
    the sūtra's own words, so it is marked `PRAKRTYA` at once.

    The other two are the name of 1.1.17 (optional, carried by 6.1.125's
    application) and neither. This sūtra stands ahead of both, as the
    substitute is made before the name is looked for.
    """
    if not _asked(v, "nipata", "stem:uñ"):
        return
    for j, _ in _pairs(v):
        left, right = j.left, j.right
        if not _un_before_iti(v, left, right):
            continue
        yield Application(
            site=site(left, right),
            edits=(replace(left, NewSeg(
                "ū", frozenset({PRAKRTYA, ANUNASIKA}))),),
            optional=_SAKALYA,
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa="ū" + ANUNASIKA_MARK,
                nimitta=f"{sk('iti')} follows",
                because=(f"{sk('u')} is the particle {{uñ}} and the "
                         f"non-Vedic {sk('iti')} follows, so in Śākalya's "
                         f"opinion it may be replaced by the long, nasal "
                         f"{sk('ū' + ANUNASIKA_MARK)}, which is itself "
                         f"pragṛhya and stays"),
                via=(Via("1.1.17",
                         "without this substitute the name pragṛhya is "
                         "itself optional, which gives the other two forms"),
                     Via("6.1.125", "the substitute is pragṛhya by the "
                                    "sūtra's own words, so it is kept"))))


# ---------------------------------------------------------------------------
# 8.3.33 — the व् for उञ्
# ---------------------------------------------------------------------------

_R833_BH = _q("8.3.33", "bhashya", "प्रगृह्यः प्रकृत्येति प्रकृतिभावः प्राप्नोति")
_R833_KA = _q("8.3.33", "kashika",
              "प्रगृह्यत्वादुञः प्रकृतिभावे प्राप्ते वकारो विधीयते")


@rule("8.3.33", name="मय उञो वो वा", families=("prakrtibhava",),
      overrides=(("6.1.125", _R833_BH), ("@ac", _R833_KA)))
def maya_uno_vo_va(v: View):
    """
    मयः परस्य उञो वो वा स्यादचि — *किमु उक्तम्* is *किम्वुक्तम्*; *तदु अस्य* is
    *तद्वस्य*; *शमु अस्तु* is *शम्वस्तु*.

    उञ् is pragṛhya (1.1.14), so 6.1.125 would keep its उ and yaṇ could not
    reach it: **प्रगृह्यः प्रकृत्येति प्रकृतिभावः प्राप्नोति** (Bhāṣya). This is
    the exception, and it stands in the tripādī on purpose: **वत्वस्यासिद्धत्वान्नानुस्वारः**
    (Kaumudī) — the व् is asiddha to 8.3.23, so the म् before it stays a म्.
    The particle is the letter उ of a word flagged `nipata`; a sound the
    derivation has made (the ऊ of *जानु उ*) is not the particle.
    """
    if not _asked(v, "nipata", "stem:uñ"):
        return
    may = S.members("may")
    for j, _ in _pairs(v):
        left, right = j.left, j.right
        if not _is_un(v.word(left)):
            continue
        before = v.prev(left)
        if before is None or before.s not in may or before.w == left.w:
            continue
        yield Application(
            site=site(before, left, right), edits=(replace(left, "v"),),
            optional=_VA,
            detail=Detail(
                kind=ADESA, sthanin=left.s, adesa="v",
                nimitta=f"a {{may}} letter, {sk(before.s)}, stands before "
                        f"it and the vowel {sk(right.s)} after",
                because=(f"{sk('u')} is the particle {{uñ}} after the "
                         f"{{may}} letter {sk(before.s)} and before the "
                         f"{{aC}} {sk(right.s)}, so it may become "
                         f"{sk('v')}; as a pragṛhya vowel it would otherwise "
                         f"have stayed"),
                via=(_nipata_via(v, left),
                     Via("6.1.125", "the prakṛtibhāva that उञ् would have "
                                    "had, and that this substitute is "
                                    "stated to displace"),
                     Via("8.2.1", "the substitute is asiddha to 8.3.23, so "
                                  "the म् before it is not made an "
                                  "anusvāra"))))


# ---------------------------------------------------------------------------
# 6.1.122–124 — go
# ---------------------------------------------------------------------------

_R122 = _q("6.1.122", "tattvabodhini",
           "निषेधविकल्पे विधिविकल्पः फलित इत्याशयेन पूर्वरूपमेवविकल्प्यत इति")
_R123 = _q("6.1.124", "tattvabodhini",
           "पूर्वरूपापवादत्वस्यापिअवङ्सूत्रस्य सुवचत्वात्")
_R124_OPT = _q("6.1.124", "balamanorama", "विकल्पनिवृत्त्यर्थः")
_R124_NITYA = _q("6.1.124", "kashika",
                 "इन्द्रशब्दस्थेऽचि परतो गोर्नित्यमवङादेशो भवति")


def _go(v: View, j: Junction) -> bool:
    """`go` at the end of a pada — the word गो itself, not a word ending in it
    (Bālamanoramā: प्रतिपदोक्तस्यैवैङो ग्रहणात्, so *चित्रगु*, *हे चित्रगो* stay
    out) — before a vowel."""
    return (v.word(j.left).text == "go" and j.left.s == "o"
            and j.kind in (PADA, SAMASA))


@rule("6.1.122", name="सर्वत्र विभाषा गोः", families=("ac", "prakrtibhava"),
      overrides=(("6.1.109", _R122),))
def sarvatra_vibhasa_goh(v: View):
    """
    लोके वेदे चैङन्तस्य गोरति वा प्रकृतिभावः स्यात्पदान्ते — *गो अग्रम्, गोऽग्रम्*;
    *गो अजिनम्*. The Bālamanoramā: एवं च पूर्वरूपमवादेशश्च न — where it is
    taken neither pūrvarūpa nor a substitute is; the Tattvabodhinī says the
    *option* is really of the pūrvarūpa (निषेधविकल्पे विधिविकल्पः फलित इत्याशयेन). So
    it displaces 6.1.109 and, through it, 6.1.78. Not Vedic only: सर्वत्र.

    चित्रग्वग्रम् (गु, not गो) and *गोः* (the ओ is no pada's end) do not qualify
    (Kaumudī: एङन्तस्य किम्, पदान्ते किम्).
    """
    if not _named(v, "go") or not _holds("6.1.122", stem="go", before="at"):
        return
    for j, _ in _pairs(v, (PADA, SAMASA)):
        left, right = j.left, j.right
        if not _go(v, j) or right.s != "a" or not v.begins_word(right):
            continue
        yield Application(
            site=site(left, right), edits=(remark(left, PRAKRTYA),),
            optional=_VIBHASA,
            detail=_keep(
                left, right,
                f"{sk('o')} ends the pada {sk('go')} and the short "
                f"{sk('a')} follows, so it may stand as it is (सर्वत्र "
                f"विभाषा — the option is of pūrvarūpa, which is not done "
                f"then either)",
                (Via("6.1.109", "the pūrvarūpa that this option displaces "
                                "when it is taken"),)))


@rule("6.1.123", name="अवङ् स्फोटायनस्य", families=("ac",),
      overrides=(("6.1.109", _R123),))
def avan_sphotayanasya(v: View):
    """
    अचि परे पदान्ते गोरवङ् वा स्यात् — *गवाग्रम्* beside *गो अग्रम्, गोऽग्रम्*;
    *गवौदनम्*, *गवोष्ट्रम्*. The ङ् is an इत् (1.1.53 ङिच्च): the substitute is
    the last sound's only. The name of Sphoṭāyana is honour, not the option
    (स्फोटायनग्रहणं पूजार्थम्, विभाषेत्येव हि वर्तते), and it is a
    व्यवस्थितविभाषा: **तेन गवाक्ष इत्यत्र नित्यमवङ् भवति** — where the compound
    *go-akṣa* means a window (`vatayana`) it is done every time.
    *गवि* is no pada's end (Kaumudī: पदान्ते किम्).

    Not offered before अ when 6.1.122's option is also open: the course that
    takes *this* is derived first (the later sūtra), then the other two.
    """
    if not _named(v, "go") or not _holds(
            "6.1.123", stem="go", before="ac", teacher="Sphoṭāyana"):
        return
    for j, _ in _pairs(v, (PADA, SAMASA)):
        left, right = j.left, j.right
        if not _go(v, j) or not v.begins_word(right):
            continue
        fixed = _flag(v, left, "vatayana") or _flag(v, right, "vatayana")
        yield Application(
            site=site(left, right), edits=(replace(left, "a", "v", "a"),),
            optional="" if fixed else _SPHOTAYANA,
            detail=Detail(
                kind=ADESA, sthanin="o", adesa="ava",
                nimitta=f"the vowel {sk(right.s)} follows",
                because=(f"{sk('o')} ends the pada {sk('go')} and a vowel "
                         f"follows, so in Sphoṭāyana's opinion it is replaced "
                         f"by {sk('avaṅ')} (the ṅ an इत्, so the whole "
                         f"substitute {sk('ava')} takes the place of the "
                         f"{sk('o')} alone)"
                         + ("; this is the compound go-akṣa, a window, where "
                            "the option is fixed (vyavasthitavibhāṣā)"
                            if fixed else "")),
                via=(Via("1.1.53", "the ṅ of avaṅ is an इत्, so the "
                                   "substitute takes the last sound only "
                                   "(ङिच्चेत्यन्तादेशः)"),
                     Via("6.1.109", "the pūrvarūpa this substitute displaces"),
                     )))


@rule("6.1.124", name="इन्द्रे च", families=("ac",),
      overrides=(("6.1.123", _R124_OPT), ("6.1.78", _R124_NITYA)))
def indre_ca(v: View):
    """
    गोरवङ् स्यादिन्द्रे — *गवेन्द्रः*. नित्यम्: the option of 6.1.123 is
    withdrawn (विकल्पनिवृत्त्यर्थः). The vowel is the first of the word इन्द्र.
    """
    if not _named(v, "go") or not _holds("6.1.124", stem="go",
                                          before="indra"):
        return
    for j, _ in _pairs(v, (PADA, SAMASA)):
        left, right = j.left, j.right
        if not _go(v, j) or right.s != "i" or not v.begins_word(right):
            continue
        if not v.word(right).text.startswith("indr"):
            continue
        yield Application(
            site=site(left, right), edits=(replace(left, "a", "v", "a"),),
            detail=Detail(
                kind=ADESA, sthanin="o", adesa="ava",
                nimitta=f"the vowel {sk('i')} of {{indra}} follows",
                because=(f"{sk('o')} ends the pada {sk('go')} and the vowel "
                         f"of {sk('indra')} follows, so it is always "
                         f"replaced by {sk('avaṅ')} — nityam, the option of "
                         f"6.1.123 is withdrawn"),
                via=(Via("6.1.123", "the substitute avaṅ, read down, without "
                                    "its option"),
                     Via("1.1.53", "the ṅ of avaṅ is an इत्: the last sound "
                                   "only is replaced"))))


# ---------------------------------------------------------------------------
# 6.1.127, 6.1.128 — Śākalya
# ---------------------------------------------------------------------------

_R127_OPT = _q("6.1.127", "kashika",
               "आरम्भसामर्थ्यादेव हि यणादेशेन सह विकल्पः सिद्धः")
_R128 = _q("6.1.128", "kashika", "सवर्णार्थमनिगर्थं च वचनम्")


def _shorten(left: Sight) -> Tuple:
    """The edit and the sound it leaves: the vowel as a short one, kept."""
    short = hrasva_of(left.s)
    if short is None or short == left.s:
        return remark(left, PRAKRTYA), left.s
    return replace(left, NewSeg(short, left.marks | {PRAKRTYA})), short


@rule("6.1.127", name="इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च",
      families=("ac", "prakrtibhava"),
      overrides=(("6.1.77", _R127_OPT),))
def iko_asavarne_sakalyasya_hrasvas_ca(v: View):
    """
    पदान्ता इकोऽसवर्णेऽचि परे प्रकृत्या स्युर्ह्रस्वश्च वा — *दधि अत्र, दध्यत्र*;
    *कुमारि अत्र, कुमार्यत्र*. इक इति किम्? *खट्वेन्द्रः*. असवर्ण इति किम्?
    *कुमारीन्द्रः* (there 6.1.101 acts). Śākalya's name is honour
    (शाकल्यस्य ग्रहणं पूजार्थम्); the option with yaṇ is the rule's own
    (आरम्भसामर्थ्यादेव हि यणादेशेन सह विकल्पः सिद्धः). A long vowel is
    shortened (`adesa.hrasva_of`), a short one is only kept.

    **न समासे** (vārttika) — not for the first member of a compound, and by the
    Kāśikā's *नित्यसमासे — व्याकरणम्* not before a preverb: so only across a
    plain pada boundary. **सिति च** — a stem made a pada by 1.4.16 before a sit
    affix is never a pada boundary here (a stem | affix junction is not
    pada-final), so nothing further is needed.

    Offered on request (`{sakalya}`): see the module docstring.
    """
    if not _asked(v, "sakalya") or not _holds(
            "6.1.127", after="ik", before="asavarṇa-ac", teacher="Śākalya"):
        return
    for j, _ in _pairs(v, (PADA,)):
        left, right = j.left, j.right
        if not _flag(v, left, "sakalya"):
            continue
        if not S.is_member(left.s, "iK") or savarna(left.s, right.s):
            continue
        edit, short = _shorten(left)
        yield Application(
            site=site(left, right), edits=(edit,), optional=_SAKALYA,
            detail=Detail(
                kind=PRAKRTIBHAVA, sthanin=left.s,
                adesa="" if short == left.s else short,
                nimitta=f"the unlike vowel {sk(right.s)} follows",
                because=(f"{sk(left.s)} is an {{ik}} ending a pada and "
                         f"{sk(right.s)} is not savarṇa to it, so in Śākalya's "
                         f"opinion it may stand as it is"
                         + ("" if short == left.s else
                            f", shortened to {sk(short)}")),
                via=(S.pratyahara("iK", "i, u, ṛ, ḷ"),
                     Via("1.1.9", f"{sk(left.s)} and {sk(right.s)} do not "
                                  f"share place and internal effort, so they "
                                  f"are not savarṇa"),
                     Via("6.1.77", "the yaṇ that stays open as the other "
                                   "course"))))


@rule("6.1.128", name="ऋत्यकः", families=("ac", "prakrtibhava"),
      overrides=(("6.1.77", _R127_OPT), ("6.1.87", _R128),
                 ("6.1.101", _R128)))
def rty_akah(v: View):
    """
    ऋति परेऽकः प्राग्वत् — *ब्रह्म ऋषिः, ब्रह्मर्षिः*; *खट्व ऋश्यः*; *होतृ ऋश्यः*;
    *सप्त ऋषीणाम्, सप्तर्षीणाम्*. सवर्णार्थमनिगर्थं च वचनम्: it reaches a savarṇa
    pair and अ, आ, which 6.1.127 could not. ऋतीति किम्? *खट्वेन्द्रः*. अक इति किम्?
    *वृक्षावृश्यः*. Unlike 6.1.127 it holds in a compound too — **समासेऽप्ययं
    प्रकृतिभावः** (Kaumudī), the vārttika न समासे being read of 6.1.127 only —
    so across a SAMASA boundary as well; and a pada-final अक् only, so
    *आर्च्छत्* (the āṭ, ANGA) is out.

    Offered on request (`{sakalya}`).
    """
    if not _asked(v, "sakalya") or not _holds(
            "6.1.128", after="ak", before="ṛ", teacher="Śākalya"):
        return
    for j, _ in _pairs(v, (PADA, SAMASA)):
        left, right = j.left, j.right
        if not _flag(v, left, "sakalya"):
            continue
        if not S.is_member(left.s, "aK") \
                or not savarna(right.s, "ṛ", varttika=False):
            continue
        edit, short = _shorten(left)
        yield Application(
            site=site(left, right), edits=(edit,), optional=_SAKALYA,
            detail=Detail(
                kind=PRAKRTIBHAVA, sthanin=left.s,
                adesa="" if short == left.s else short,
                nimitta=f"{sk(right.s)} follows",
                because=(f"{sk(left.s)} is an {{ak}} ending a pada and "
                         f"{sk(right.s)} follows, so in Śākalya's opinion it "
                         f"may stand as it is"
                         + ("" if short == left.s else
                            f", shortened to {sk(short)}")),
                via=(S.pratyahara("aK", "a, i, u, ṛ, ḷ"),
                     Via("6.1.127", "the same prakṛtibhāva with hrasva, read "
                                    "down (शाकल्यस्य ह्रस्वश्च)"))))


# ---------------------------------------------------------------------------
# 6.1.115–121, 6.1.126 — the Vedic prakṛtibhāva
# ---------------------------------------------------------------------------

_R115 = _q("6.1.115", "kashika",
           "स्वभावेनावतिष्ठते, कारणात्मना वा भवति, न विकारमापद्यते")
_R116 = _q("6.1.116", "kashika",
           "वकारयकारपरेऽप्यति परतोऽन्तः पादमेङ् प्रकृत्या भवति")
_R117 = _q("6.1.117", "kashika", "यजुषि पादानामभावादनन्तःपादार्थं वचनम्")
_R126 = _q("6.1.126", "kashika", "स च प्रकृत्या भवति")


def _eng_a(v: View) -> Iterator[Junction]:
    """A pada-final एङ् before a short अ that begins the next pada."""
    for j, _ in _pairs(v, (PADA,)):
        if S.is_member(j.left.s, "eṄ") and j.right.s == "a" \
                and v.begins_word(j.right) and PLUTA not in j.right.marks:
            yield j


def _vedic(left: Sight, right: Sight, because: str,
           via: Sequence[Via] = ()) -> Application:
    return Application(
        site=site(left, right), edits=(remark(left, PRAKRTYA),),
        detail=_keep(left, right, because, via,
                     nimitta=f"the short {sk('a')} follows"))


@rule("6.1.115", name="प्रकृत्यान्तःपादमव्यपरे", families=("prakrtibhava",),
      vedic=True, overrides=(("@ac", _R115),))
def prakrtyantahpadam_avyapare(v: View):
    """
    ऋक्पादमध्यस्थ एङ् प्रकृत्या स्यादति परे न तु वकारयकारपरेऽति — *ते अग्ने
    अश्वमायुञ्जन्, उपप्रयन्तो अध्वरम्, सुजाते अश्वसूनृते*. अन्तःपादं किम्?
    *एतास एतेऽर्चन्ति* (the junction at the foot's edge). अव्यपरे किम्? *तेऽवदन्*
    (a व् follows the अ). Only an Ṛk pāda, not a verse-line of a śloka
    (पादशब्देन च ऋक्पादस्यैव ग्रहणमिष्यते): that the junction lies inside one is the
    caller's flag `antahpada`. Vedic.

    OPEN. The Kāśikā reports a reading *नान्तःपादमव्यपरे* that turns the sūtra
    into a refusal of everything under 6.1.72 (केचिदिदं सूत्रं …); it is
    reported and not adopted, as the Kāśikā does.
    """
    for j in _eng_a(v):
        left, right = j.left, j.right
        if not _flag(v, left, "antahpada"):
            continue
        after = v.next(right)
        if after is not None and after.s in _VA_YA:
            continue
        if not _holds("6.1.115", after="eṅ", before="at",
                      result="antaḥpāda", chandasi=True):
            continue
        yield _vedic(
            left, right,
            f"{sk(left.s)} is an {{eṅ}} ending a word inside an Ṛk pāda, the "
            f"short {sk('a')} follows and no {sk('v')} or {sk('y')} comes "
            f"after that {sk('a')}, so both stand as they are")


@rule("6.1.116", name="अव्यादवद्यादवक्रमुरव्रतायमवन्त्वस्युषु च",
      families=("prakrtibhava",), vedic=True, overrides=(("@ac", _R116),))
def avyadavadyada(v: View):
    """
    एषु व्यपरेऽप्यति एङ् प्रकृत्या — *वसुभिर्नो अव्यात्, मित्रमहो अवद्यात्,
    मा शिवासो अवक्रमुः, ते नो अव्रत, शतधारो अयं मणिः, ते नो अवन्तु, कुशिकासो
    अवस्यवः*. The seven words are the Kāśikā's list (`prakrtibhava.AVYADI`); each
    begins with an अ that a व् or य् follows, the very thing 6.1.115 refuses on.
    Still inside a pāda. The Kaumudī remarks that the Bahvṛcas do not keep it in
    *तेनोऽवन्तु, रथतूः, सोऽयमगात्, तेऽरुणेभिः* and settles that by बाहुलक (and in
    the Prātiśākhya by an express statement); not derived.
    """
    for j in _eng_a(v):
        left, right = j.left, j.right
        if not _flag(v, left, "antahpada"):
            continue
        word = v.word(right)
        stem = word.flag_value("stem") or ""
        # a final visarga is read by the parser as स्, so the list is too
        if not any(word.text == w.replace(VISARGA, "s") or stem == w
                   for w in AVYADI):
            continue
        if not _holds("6.1.116", after="eṅ", before="avyādi",
                      result="antaḥpāda", chandasi=True):
            continue
        yield _vedic(
            left, right,
            f"{sk(left.s)} is an {{eṅ}} ending a word inside an Ṛk pāda and "
            f"{sk(word.text)} is one of the seven words of the list, so the "
            f"junction stands open although a {sk('v')} or {sk('y')} follows "
            f"the {sk('a')}",
            (Via("6.1.115", "the prakṛtibhāva read down; it refuses when a v "
                            "or y follows the a, and this list is the "
                            "exception to that refusal"),))


@rule("6.1.117", name="यजुष्युरः", families=("prakrtibhava",), vedic=True,
      overrides=(("@ac", _R117),))
def yajusy_urah(v: View):
    """
    उरःशब्द एङन्तोऽति प्रकृत्या यजुषि — *उरो अन्तरिक्षम्*. The Yajurveda has no
    verse-feet, so the condition of 6.1.115 could not be met there: **यजुषि
    पादानामभावादनन्तःपादार्थं वचनम्**. The word is *उरो* (`yajus`).
    """
    for j in _eng_a(v):
        left, right = j.left, j.right
        if not _flag(v, left, "yajus") or v.word(left).text != "uro":
            continue
        if not _holds("6.1.117", stem="uras", before="at", yajusi=True):
            continue
        yield _vedic(
            left, right,
            f"{sk('uro')} is the word {{uras}} in the Yajurveda and the short "
            f"{sk('a')} follows, so both stand as they are (no pāda is "
            f"needed: the Yajurveda has none)")


@rule("6.1.118", name="आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे",
      families=("prakrtibhava",), vedic=True, overrides=(("@ac", _R117),))
def apo_jusano(v: View):
    """
    यजुषि अति प्रकृत्या — *आपो अस्मान्मातरः, जुषाणो अग्निराज्यस्य, वृष्णो
    अंशुभ्याम्, वर्षिष्ठे अधि नाके, अम्बे अम्बाले अम्बिके*. The six words are
    the Kāśikā's (`prakrtibhava.YAJUSI_WORDS`). *अम्बे* and *अम्बाले* only where
    *अम्बिका* comes after (अम्बिकेपूर्वे): read as the formula *अम्बे अम्बाले
    अम्बिके*, in which each is followed by the next.
    """
    for j in _eng_a(v):
        left, right = j.left, j.right
        if not _flag(v, left, "yajus"):
            continue
        word, nxt = v.word(left).text, v.word(right).text
        if word not in YAJUSI_WORDS:
            continue
        if word == "ambe" and not nxt.startswith("ambāl"):
            continue
        if word == "ambāle" and not nxt.startswith("ambik"):
            continue
        if not _holds("6.1.118", stem=word, before="at", yajusi=True):
            continue
        yield _vedic(
            left, right,
            f"{sk(word)} is one of the words of the list, in the Yajurveda, "
            f"and the short {sk('a')} follows, so both stand as they are")


@rule("6.1.119", name="अङ्ग इत्यादौ च", families=("prakrtibhava",),
      vedic=True, overrides=(("@ac", _R117),))
def anga_ityadau_ca(v: View):
    """
    अङ्गशब्दे य एङ् तदादौ च अकारे य एङ् पूर्वः सोऽति प्रकृत्या यजुषि — *प्राणो अङ्गे
    अङ्गे अदीध्यत्*: the ओ before *अङ्गे*, and the ए of *अङ्गे* before the अ.
    """
    for j in _eng_a(v):
        left, right = j.left, j.right
        if not _flag(v, left, "yajus"):
            continue
        in_word = v.word(left).text == "aṅge"
        before_word = v.word(right).text.startswith("aṅg")
        if not (in_word or before_word):
            continue
        if not _holds("6.1.119", stem="aṅga", before="at", yajusi=True):
            continue
        yield _vedic(
            left, right,
            f"{sk(left.s)} is an {{eṅ}} " + (
                "in the word aṅga" if in_word else
                "standing before the a that begins aṅga")
            + ", in the Yajurveda, so both stand as they are")


@rule("6.1.120", name="अनुदात्ते च कुधपरे", families=("prakrtibhava",),
      vedic=True, overrides=(("@ac", _R117),))
def anudatte_ca_kudhapare(v: View):
    """
    कवर्गधकारपरे अनुदात्तेऽति परे एङ् प्रकृत्या यजुषि — *अयं नो अग्निः, अयं सो
    अध्वरः*. अनुदात्ते किम्? *अधोऽग्रे* (अग्र is ādyudātta). कुधपरे किम्?
    *सोऽयमग्निः*. The accent is the caller's (`anudatta` on the word whose first
    vowel it is); the following sound is a कवर्ग letter or ध्, read from `VARGA`.
    """
    ku = frozenset(VARGA["ku"])
    for j in _eng_a(v):
        left, right = j.left, j.right
        if not _flag(v, left, "yajus") or not _flag(v, right, "anudatta"):
            continue
        after = v.next(right)
        if after is None or not (after.s in ku or after.s == "dh"):
            continue
        if not _holds("6.1.120", after="eṅ", before="at-anudātta-ku-dha",
                      yajusi=True):
            continue
        yield _vedic(
            left, right,
            f"{sk(left.s)} is an {{eṅ}}, the short {sk('a')} after it is "
            f"anudātta and {sk(after.s)} follows that {sk('a')}, in the "
            f"Yajurveda, so both stand as they are")


@rule("6.1.121", name="अवपथासि च", families=("prakrtibhava",), vedic=True,
      overrides=(("@ac", _R117),))
def avapathasi_ca(v: View):
    """
    Before the word *अवपथाः* whose अ is anudātta, in the Yajurveda, an एङ् stays
    (Kaumudī: अनुदात्ते … अवपथाःशब्दे परे यजुषि एङ् प्रकृत्या) — *त्री रुद्रेभ्यो
    अवपथाः*. The अ is anudātta by 8.1.28; put *यद्* before it and 8.1.30 keeps the
    निघात off, so the accent stays and the junction closes: *यद्रुद्रेभ्योऽवपथाः*
    — which is why the accent is the caller's flag and not read off the word.
    """
    for j in _eng_a(v):
        left, right = j.left, j.right
        if not _flag(v, left, "yajus") or not _flag(v, right, "anudatta"):
            continue
        word = v.word(right).text
        if not word.startswith("avapath"):
            continue
        if not _holds("6.1.121", stem=word, before="at-anudātta",
                      yajusi=True):
            continue
        yield _vedic(
            left, right,
            f"{sk(left.s)} is an {{eṅ}} before the word {sk('avapathāḥ')} whose "
            f"first {sk('a')} is anudātta, in the Yajurveda, so both stand "
            f"as they are")


@rule("6.1.126", name="आङोऽनुनासिकश्छन्दसि", families=("prakrtibhava",),
      vedic=True, overrides=(("@ac", _R126),))
def ango_nunasikas_chandasi(v: View):
    """
    आङोऽचि परेऽनुनासिकः स्यात्, स च प्रकृत्या — *अभ्र आँ अपः, गभीर आँ उग्रपुत्रे*.
    The आ is the particle āṅ (`ang`) standing as its own word; the preverb
    joined to its dhātu is not taken (the Kāśikā's second reading, with बहुलम्,
    keeps *आतरत्*: OPEN, not derived). The vowel before it is settled first
    (`_pending`), so *अभ्र आँ अपः* comes from *अभ्रस् आ अपः* — where the loss
    of the य् is asiddha and the अ and आ stay apart — and not from *अभ्र आ*.
    """
    if not _asked(v, "ang"):
        return
    for j, _ in _pairs(v, (PADA,)):
        left, right = j.left, j.right
        if left.s != "ā" or not _flag(v, left, "ang"):
            continue
        if not _holds("6.1.126", stem="āṅ", before="ac", chandasi=True):
            continue
        yield Application(
            site=site(left, right),
            edits=(replace(left, NewSeg(
                "ā", frozenset({ANUNASIKA, PRAKRTYA}))),),
            detail=Detail(
                kind=ADESA, sthanin="ā", adesa="ā" + ANUNASIKA_MARK,
                nimitta=f"the vowel {sk(right.s)} follows",
                because=(f"{sk('ā')} is the particle {{āṅ}} and a vowel "
                         f"follows in the Veda, so it is replaced by the "
                         f"nasal {sk('ā' + ANUNASIKA_MARK)}, which stays as "
                         f"it is (sa ca prakṛtyā)"),
                via=(Via("6.1.125", "the substitute is kept as it is by the "
                                    "sūtra's own words"),)))


# ---------------------------------------------------------------------------
# 6.1.131 — दिव उत्
# ---------------------------------------------------------------------------


def _pada_making_sups() -> Tuple[str, ...]:
    """
    The case-endings before which a stem is a pada by 1.4.17: not a
    sarvanāmasthāna (`sup.SUT`) and not beginning with a vowel or य् (1.4.18).
    Read from the list of the twenty-one (`sup.SUP`), not written again.
    """
    return tuple(sorted({
        e for e in SUP if e not in SUT and e != "sup"
        and tokenize(e)[0][0] in HAL and tokenize(e)[0][0] != _YA}))


@rule("6.1.131", name="दिव उत्", families=("hal",))
def diva_ut(v: View):
    """
    दिवोऽन्तादेश उकारः स्यात्पदान्ते — *सुद्युभ्याम्, सुद्युभिः*; the उ then meets the
    इ before it and 6.1.77 makes it *द्यु*. दिव् is the prātipadika, not the root
    (**दिव इति प्रातिपदिकं गृह्यते न धातुः, सानुबन्धकत्वात्**), so a word flagged
    `dhatu` (*अक्षदिव्* from √दिव्) is out. पदस्येति किम्? *दिवौ, दिवः* — not a pada.
    The उ is short (तपर).

    A pada, here, is one that ends at a PADA boundary or before a consonant-initial
    ending that is not a sarvanāmasthāna (1.4.17, with 1.4.18). PARTIAL: whether
    an affix *is* such a case-ending is read from the list `sup.SUP` by its
    letters; an ending that shares its letters with another affix is not told
    apart (the caller's `~` says stem | affix).
    """
    if not _holds("6.1.131", stem="div", result="pada"):
        return
    for s in v.live:
        if s.s != "v" or not v.ends_word(s):
            continue
        letters = [x.s for x in v.word_sights(s.w)]
        if letters[-3:] != ["d", "i", "v"]:
            continue
        word = v.word(s)
        if word.flag_value("dhatu") is not None or "dhatu" in word.flags:
            continue
        nxt = v.next(s)
        via: List[Via] = []
        if v.pada_final(s):
            pass
        elif v.boundary_after(s) == ANGA and nxt is not None \
                and v.word(nxt).text in _pada_making_sups():
            via.append(Via("1.4.17", f"{sk(v.word(nxt).text)} is a "
                                     f"case-ending that is no "
                                     f"{{sarvanāmasthāna}}, so the stem before "
                                     f"it is a {{pada}}"))
        else:
            continue
        yield Application(
            site=site(s), edits=(replace(s, "u"),),
            detail=Detail(
                kind=ADESA, sthanin="v", adesa="u",
                nimitta="the end of the pada div",
                because=(f"{sk(word.text)} ends in the prātipadika {sk('div')} "
                         f"and is a pada, so its last sound {sk('v')} is "
                         f"replaced by {sk('u')}"),
                via=tuple(via) + (Via("1.1.52", "the substitute takes the "
                                                "last sound only"),
                                  Via("1.1.70", "the उ is followed by त् in "
                                                "the sūtra, so it is the short "
                                                "उ"))))


# ---------------------------------------------------------------------------
# 8.4.57 — the nasal at a pause
# ---------------------------------------------------------------------------


@rule("8.4.57", name="अणोऽप्रगृह्यस्यानुनासिकः", families=("nasal",))
def ano_apragrhyasyanunasikah(v: View):
    """
    अप्रगृह्यस्याणोऽवसानेऽनुनासिको वा स्यात् — *दधिँ, दधि*; *मधुँ, मधु*;
    *कुमारीँ, कुमारी*. अण इति किम्? *कर्तृ, हर्तृ*. अप्रगृह्यस्येति किम्?
    *अग्नी, वायू*. The अण् is a, i, u and their lengths (1.1.69), read from
    `S.members`; the name is asked of `pragrhya.pragrhya` as in 6.1.125.

    **Offered on request** — the word carries the flag `anunasika`. The option
    returns its taken course first and every derivation ends at a pause, so
    offering it after every last a, i, u would turn *iti ādi* into *ityādiँ*
    ahead of *ityādi* (README, the engine's tests), and would give every
    *pausal form* that `split` builds a nasal twin. OPEN: the harness's gold for
    *dadhi*, *madhu*, *kumārī* carries no flag and will list the other form as
    missing.
    """
    if not _asked(v, "anunasika"):
        return
    for s in v.live:
        if not v.at_pause(s) or not S.is_member(s.s, "aṆ") or s.seg.nasal:
            continue
        word = v.word(s)
        flags = word.flags
        if "anunasika" not in flags:
            continue
        if _pragrhya(
                word.text, dvivacana="dvivacana" in flags,
                nipata="nipata" in flags, ang="ang" in flags,
                sambuddhi="sambuddhi" in flags, arsa="arsa" in flags,
                saptami_artha="saptamyartha" in flags,
                stem=word.flag_value("stem") or "") is not None:
            continue
        yield Application(
            site=site(s),
            edits=(replace(s, NewSeg(s.s, s.marks | {ANUNASIKA})),),
            optional=_VA,
            detail=Detail(
                kind=ADESA, sthanin=s.s, adesa=s.s + ANUNASIKA_MARK,
                nimitta="a pause follows (1.4.110)",
                because=(f"{sk(s.s)} is an {{aṇ}} that is not pragṛhya and "
                         f"a pause follows, so it may be nasalised"),
                via=(S.avasana_condition(),)
                + ((S.varna_grahana(s.s, "aṆ"),)
                   if S.long_form_used(s.s, "aṆ") else ())))


# ---------------------------------------------------------------------------
# The family
# ---------------------------------------------------------------------------

RULES = (
    um_nasal, prakrtyantahpadam_avyapare, avyadavadyada, yajusy_urah,
    apo_jusano, anga_ityadau_ca, anudatte_ca_kudhapare, avapathasi_ca,
    sarvatra_vibhasa_goh, avan_sphotayanasya, indre_ca,
    plutapragrhya_aci_nityam, ango_nunasikas_chandasi,
    iko_asavarne_sakalyasya_hrasvas_ca, rty_akah, aplutavad_upasthite,
    i3_cakravarmanasya, diva_ut, maya_uno_vo_va, ano_apragrhyasyanunasikah,
)

_ACCENT = ("the accent (udātta, anudātta, svarita) is not carried by the "
           "engine's sounds")
_MEANING = ("its condition is a meaning — {what} — that no letter and no "
            "flag of this vocabulary says")
_PLUTA_FLAG = ("the pluta it makes is received as the flag `pluta` on the "
               "word, which 6.1.125 and 6.1.129–130 read")

COVERAGE = (
    # -- 1.1.11–19: the names, asked of pragrhya.py by 6.1.125 ---------------
    ("1.1.11", "support", "asked of pragrhya.pragrhya by 6.1.125 with the "
     "flag dvivacana and cited in its step; the Kāśikā's vārttika "
     "(ईदादीनां प्रगृह्यत्वे मणीवादीनां प्रतिषेधो वक्तव्यः: maṇīva, dampatīva) "
     "is NOT applied — the Kaumudī explains maṇīva away (iva-artha va) "
     "instead of adopting it, so the reading the two share is the plain one"),
    ("1.1.12", "support", "asked of pragrhya.pragrhya; the engine also "
     "checks that the vowel stands after the म् of the word, which is what "
     "keeps *amuke* out (Kāśikā: मादिति किम्? अमुकेऽत्र)"),
    ("1.1.13", "support", "asked of pragrhya.pragrhya for a word flagged "
     "`she`; Vedic, and its only Vedic example is asme indrābṛhaspatī"),
    ("1.1.14", "support", "asked of pragrhya.pragrhya for a word flagged "
     "nipata and not ang; a one-vowel particle is not inferred (infer.py), "
     "the caller flags it"),
    ("1.1.15", "support", "asked of pragrhya.pragrhya; a nipāta ending in o, "
     "including one that infer.py proves from the cādi gaṇa (aho, utāho, "
     "āho)"),
    ("1.1.16", "support", "asked of pragrhya.pragrhya for a word flagged "
     "sambuddhi before a non-Vedic iti; optional, so the 6.1.125 application "
     "forks (vāyo iti, vāya iti, vāyaviti)"),
    ("1.1.17", "support", "asked of pragrhya.pragrhya for the particle उ "
     "before a non-Vedic iti; it stands later than 1.1.14 and makes the name "
     "optional there — which is what gives the three forms of 1.1.18"),
    ("1.1.18", "rule", ""),
    ("1.1.19", "support", "asked of pragrhya.pragrhya for a word flagged "
     "saptamyartha; the arthagrahaṇa is the caller's, so *vāpī-aśvaḥ* is "
     "not flagged and takes yaṇ"),
    # -- 1.4.56–60: the names the inference reads -----------------------------
    ("1.4.56", "support", "the heading that makes the particles nipāta; "
     "cited by 6.1.125 where the caller gave the flag"),
    ("1.4.57", "partial", "infer.py reads the cādi gaṇa from the gaṇapāṭha "
     "and infers nipata for a word in it; being absent proves nothing (an "
     "ākṛtigaṇa) and a word naming a substance (asattve) takes the flag "
     "sattva — which is also the escape for a listed word that is another "
     "word here (नो as the pronoun's नः, 6.1.116); a ONE-VOWEL word is not "
     "inferred, because the engine's tests use bare vowels as stand-ins for "
     "a word-final sound"),
    ("1.4.58", "partial", "infer.py reads the prādi gaṇa the same way; the "
     "vārttikas on marut and śrat are lexical additions not made"),
    ("1.4.59", "partial", "infer.py proves upasarga for a prādi word before a "
     "dhātu across the | boundary, but parse does not hand it the boundaries "
     "yet (core request); the rules read the boundary themselves, so a "
     "preverb ā (UPASARGA) is never pragṛhya"),
    ("1.4.60", "scope", "gati is used by compounding (2.2.18) and accent "
     "(6.2.49); the ṇatva/ṣatva its name licenses belong to the natva and "
     "satva families; nothing here for sandhi to run"),
    # -- 6.1.115–131 ---------------------------------------------------------
    ("6.1.115", "vedic", "needs the flag antahpada (a junction inside one Ṛk "
     "pāda); the verse is the caller's"),
    ("6.1.116", "vedic", "the seven words are the Kāśikā's list; needs "
     "antahpada"),
    ("6.1.117", "vedic", "the word uro in the Yajurveda (flag yajus)"),
    ("6.1.118", "vedic", "the six words; ambe and ambāle only in the formula "
     "ambe ambāle ambike"),
    ("6.1.119", "vedic", "the word aṅge and the junction before aṅga (flag "
     "yajus)"),
    ("6.1.120", "vedic", "the accent is the flag anudatta; the following "
     "sound is read from VARGA"),
    ("6.1.121", "vedic", "the accent is the flag anudatta; the word is "
     "avapathāḥ"),
    ("6.1.122", "rule", ""),
    ("6.1.123", "partial", "the option is derived; the vyavasthitavibhāṣā "
     "that fixes it in gavākṣa (window) is the flag vatayana — a lexical "
     "fact the letters cannot give"),
    ("6.1.124", "rule", ""),
    ("6.1.125", "rule", ""),
    ("6.1.126", "vedic", "āṅ as its own pada (flag ang); the preverb joined "
     "to its dhātu is not taken (the Kāśikā's bahulam reading); the "
     "vārttika ईषाअक्षादीनां छन्दसि प्रकृतिभावो वक्तव्यः is a lexical list "
     "and not done"),
    ("6.1.127", "partial", "offered only for a word flagged sakalya (see the "
     "module docstring); the vārttika न समासे is a condition (a plain pada "
     "boundary), सिति च never arises (a stem|affix junction is not "
     "pada-final); the vārttika ईषाअक्षादिषु is a Vedic lexical list"),
    ("6.1.128", "partial", "offered only for a word flagged sakalya; unlike "
     "6.1.127 it holds across a compound boundary"),
    ("6.1.129", "rule", ""),
    ("6.1.130", "partial", "for the pluta of the i-varṇa, as the sūtra says; "
     "the Kāśikā's iṣyate extension to a pluta of any vowel (vaśā3 iyam, "
     "vaśeyam) is not derived — the Kaumudī does not share it and it would "
     "put an option ahead of 6.1.125 at every pluta junction"),
    ("6.1.131", "partial", "the pada is a PADA boundary or a consonant-initial "
     "case-ending known from sup.SUP; not told apart from an affix of the "
     "same letters"),
    # -- 8.2.82–107: the pluta and its accent ---------------------------------
    ("8.2.82", "scope", "the heading of the pluta: the ṭi of a vākya, made "
     "pluta and udātta. The engine works at junctions of padas and has no "
     "notion of where a sentence ends, or of accent; " + _PLUTA_FLAG),
    ("8.2.83", "scope", "return greeting to a non-śūdra: " + _MEANING.format(
        what="the speaker's caste and the greeting") + "; " + _PLUTA_FLAG),
    ("8.2.84", "scope", "a call from a distance (the vocative): "
     + _MEANING.format(what="distance") + "; " + _PLUTA_FLAG),
    ("8.2.85", "scope", "the calling particles hai and he: " + _MEANING.format(
        what="a call from afar") + "; " + _PLUTA_FLAG),
    ("8.2.86", "scope", "a heavy vowel of a call, by the eastern teachers: "
     + _MEANING.format(what="the call") + "; " + _PLUTA_FLAG),
    ("8.2.87", "scope", "Vedic only (the opening of a rite, ओ३म्); "
     + _PLUTA_FLAG),
    ("8.2.88", "scope", "Vedic only (ये३ यजामहे in a sacrifice); "
     + _PLUTA_FLAG),
    ("8.2.89", "scope", "Vedic only (the praṇava at the end of a pāda in a "
     "rite); " + _PLUTA_FLAG),
    ("8.2.90", "scope", "Vedic only (the last vowel of a yājyā); "
     + _PLUTA_FLAG),
    ("8.2.91", "scope", "Vedic only (the first vowel of brūhi, preṣya, "
     "śrauṣaṭ, vauṣaṭ, āvaha in a rite); " + _PLUTA_FLAG),
    ("8.2.92", "scope", "Vedic only (the agnīdh's command); " + _PLUTA_FLAG),
    ("8.2.93", "scope", "hi in an answer: " + _MEANING.format(
        what="an answer to a question") + "; " + _PLUTA_FLAG),
    ("8.2.94", "scope", "cross-examination: " + _MEANING.format(
        what="a refutation") + "; " + _PLUTA_FLAG),
    ("8.2.95", "scope", "the repeated word in a threat: " + _MEANING.format(
        what="abuse") + "; " + _PLUTA_FLAG),
    ("8.2.96", "scope", "a verb with aṅga left hanging: " + _MEANING.format(
        what="a reproach") + "; " + _PLUTA_FLAG),
    ("8.2.97", "scope", "deliberation: " + _MEANING.format(
        what="weighing alternatives") + "; " + _PLUTA_FLAG),
    ("8.2.98", "scope", "which alternative of a deliberation takes the pluta "
     "in the language: " + _MEANING.format(what="a deliberation") + "; "
     + _PLUTA_FLAG),
    ("8.2.99", "scope", "assent or promise: " + _MEANING.format(
        what="assent") + "; " + _PLUTA_FLAG),
    ("8.2.100", "scope", "makes the pluta anudātta: " + _ACCENT),
    ("8.2.101", "scope", "makes the pluta anudātta with cit of comparison: "
     + _ACCENT),
    ("8.2.102", "scope", "makes the pluta anudātta in upariṣvid āsīt: "
     + _ACCENT),
    ("8.2.103", "scope", "makes the pluta svarita: " + _ACCENT),
    ("8.2.104", "scope", "makes the pluta svarita: " + _ACCENT),
    ("8.2.105", "scope", "makes the pluta svarita and extends it to a "
     "non-final vowel: " + _ACCENT),
    ("8.2.106", "scope", "the shape of the pluta of ai and au (ai3, au3): "
     "the engine takes the flag pluta on the vowel and does not build its "
     "three-mora form"),
    ("8.2.107", "scope", "the shape of the pluta of e, o, ai, au outside a "
     "call from afar: the engine takes the flag pluta and does not build "
     "the ā3 + i or u form"),
    # -- the last two ---------------------------------------------------------
    ("8.3.33", "rule", ""),
    ("8.4.57", "partial", "offered for a word flagged anunasika only: the "
     "option returns its taken course first and every derivation ends at a "
     "pause, so offering it always would change every existing derivation and "
     "the pausal forms split.py builds; see the rule's docstring"),
)
